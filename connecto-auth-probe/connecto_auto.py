"""
Automated, non-interactive Connecto sign-in/sign-out for the daily
attendance_logger run.

Unlike connecto_cli.py (a manual tool meant to be run BY HAND in the
moment), this is called from attendance_logger/main.py as the first and
last step of the daemon's daily cycle. It never prompts for anything:

  - Auth: reuses the session saved once via `python3 connecto_cli.py
    login` (read from .connecto_session.json). That login is a one-time,
    by-hand step - this assumes the token stays valid across days. If the
    session is missing, or a sign-in/out call fails (e.g. an expired
    token), the step is skipped and logged as a warning rather than
    raising - Connecto is additive to the existing 1thing.in flow and must
    never block or abort it.
  - Location: a fixed lat/long (set below) rather than photo EXIF or a
    typed-in value, since nothing here is interactive.
  - Photos: dropped ahead of time into `photos/signin/` and
    `photos/signout/` next to this file. The newest file in each is used,
    then moved into that folder's `used/` subfolder (timestamped) so a
    rerun after a crash doesn't resend a photo already sent, and a photo
    left over from a prior day can't get reused by accident. If a folder
    has no fresh photo, a file named `fallback.<ext>` in that same folder
    (e.g. `photos/signin/fallback.jpg`) is used instead and, unlike a
    normal photo, is never archived away - it stays in place as the
    standing fallback for the next day that also has no fresh photo.
  - Status: before sending, checks `get-todays-attendance` and skips a
    sign-in that's already been done today, or a sign-out with no matching
    sign-in yet / already done. The response shape isn't documented (see
    connecto_cli.py) - this fuzzy-matches likely field names via
    `cc.dig_for_key`, and if none match, treats status as unknown and sends
    anyway rather than guessing wrong and skipping a real sign-in/out.
"""
import base64
import io
import os
import shutil
import sys
from datetime import datetime

_THIS_DIR = os.path.dirname(os.path.abspath(__file__))
_PROJECT_ROOT = os.path.dirname(_THIS_DIR)
if _PROJECT_ROOT not in sys.path:
    sys.path.insert(0, _PROJECT_ROOT)

from attendance_logger.logging_config import configure_logging, get_logger

configure_logging()
logger = get_logger("connecto_auto")

import connecto_client as cc

# From the `auto_latitude`/`auto_longitude` on today's real sign-in
# (`connecto_cli.py status`) - required since there's no one here to type
# coordinates in and no photo EXIF is read.
FIXED_LATITUDE = "32.154587"
FIXED_LONGITUDE = "77.17662"
FIXED_ADDRESS = ""

SIGNIN_DIR = os.path.join(_THIS_DIR, "photos", "signin")
SIGNOUT_DIR = os.path.join(_THIS_DIR, "photos", "signout")

# Best-effort field-name guesses for today's sign-in/out status - the
# get-todays-attendance response shape isn't documented anywhere public.
# Once a real response has been seen (e.g. via `connecto_cli.py status`),
# add its actual field name here if it isn't already covered.
SIGNIN_TIME_KEYS = ["signin_time", "sign_in_time", "in_time", "signintime", "punch_in_time", "actual_signin_time"]
SIGNOUT_TIME_KEYS = ["signout_time", "sign_out_time", "out_time", "signouttime", "punch_out_time", "actual_signout_time"]


def _ensure_dirs(folder):
    os.makedirs(folder, exist_ok=True)
    os.makedirs(os.path.join(folder, "used"), exist_ok=True)


def _is_fallback_name(name):
    stem, _ext = os.path.splitext(name)
    return stem.lower() == "fallback"


def _pick_photo(folder):
    """Newest non-fallback file dropped in `folder`, or None."""
    _ensure_dirs(folder)
    candidates = [
        os.path.join(folder, name)
        for name in os.listdir(folder)
        if os.path.isfile(os.path.join(folder, name)) and not name.startswith(".") and not _is_fallback_name(name)
    ]
    if not candidates:
        return None
    return max(candidates, key=os.path.getmtime)


def _find_fallback(folder):
    """The standing `fallback.<ext>` file in `folder`, or None."""
    _ensure_dirs(folder)
    for name in os.listdir(folder):
        if os.path.isfile(os.path.join(folder, name)) and _is_fallback_name(name):
            return os.path.join(folder, name)
    return None


def _archive_photo(path, folder):
    stamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    dest = os.path.join(folder, "used", f"{stamp}_{os.path.basename(path)}")
    shutil.move(path, dest)


MAX_PHOTO_DIMENSION = 700


def _strip_exif(path):
    """Re-encodes the photo from pixel data alone, dropping EXIF/ICC/other
    metadata (e.g. the camera's real GPS tags) before it's uploaded - the
    fixed lat/long above is what's actually sent, so the source photo's own
    metadata has no reason to leave this machine too. Also downsizes it so
    neither edge exceeds MAX_PHOTO_DIMENSION, since the source photo (a
    full phone-camera capture) is far larger than Connecto needs."""
    try:
        from PIL import Image
    except ImportError:
        logger.warning("Pillow not installed - uploading %s with metadata intact.", path)
        with open(path, "rb") as f:
            return f.read()

    img = Image.open(path)
    img.thumbnail((MAX_PHOTO_DIMENSION, MAX_PHOTO_DIMENSION), Image.LANCZOS)
    clean = Image.new(img.mode, img.size)
    clean.putdata(list(img.getdata()))

    save_kwargs = {"format": img.format or "JPEG"}
    if save_kwargs["format"] == "JPEG":
        save_kwargs["quality"] = 95
    buffer = io.BytesIO()
    clean.save(buffer, **save_kwargs)
    return buffer.getvalue()


def _load_image_b64(path):
    return base64.b64encode(_strip_exif(path)).decode("ascii")


def _todaysStatus(session):
    """Returns (signedIn, signedOut) as True/False/None (None = couldn't
    tell from the response). Never raises - a failed status check just
    means callers proceed without it, same as an unknown result."""
    try:
        response = cc.get_todays_attendance(session["user_id"], session["token"])
    except Exception:
        logger.exception("Connecto get-todays-attendance failed - proceeding without a status check.")
        return None, None

    _, signinVal = cc.dig_for_key(response, SIGNIN_TIME_KEYS)
    _, signoutVal = cc.dig_for_key(response, SIGNOUT_TIME_KEYS)
    signedIn = bool(signinVal) if signinVal is not None else None
    signedOut = bool(signoutVal) if signoutVal is not None else None

    if signedIn is None and signedOut is None:
        logger.info("Connecto today's-attendance status unknown (no matching fields) - raw response: %s", response)

    return signedIn, signedOut


def _run(action, api_call, folder):
    if not FIXED_LATITUDE or not FIXED_LONGITUDE:
        logger.warning("Connecto %s skipped: FIXED_LATITUDE/FIXED_LONGITUDE not set in connecto_auto.py.", action)
        return

    session = cc.load_session()
    if not session or not session.get("token"):
        logger.warning("Connecto %s skipped: no saved session - run `python3 connecto_cli.py login` once by hand.", action)
        return

    signedIn, signedOut = _todaysStatus(session)
    if action == "sign-in" and signedIn:
        logger.info("Connecto sign-in skipped: already signed in today.")
        return
    if action == "sign-out":
        if signedOut:
            logger.info("Connecto sign-out skipped: already signed out today.")
            return
        if signedIn is False:
            logger.warning("Connecto sign-out skipped: not signed in today yet.")
            return

    photoPath = _pick_photo(folder)
    usingFallback = False
    if not photoPath:
        photoPath = _find_fallback(folder)
        usingFallback = True
        if not photoPath:
            logger.warning("Connecto %s skipped: no photo (and no fallback.<ext>) found in %s.", action, folder)
            return
        logger.warning("Connecto %s: no fresh photo in %s, using fallback image %s.", action, folder, photoPath)

    try:
        imageB64 = _load_image_b64(photoPath)
        call_kwargs = dict(
            user_id=session["user_id"],
            token=session["token"],
            config_id=session["config_id"],
            image_b64=imageB64,
            latitude=FIXED_LATITUDE,
            longitude=FIXED_LONGITUDE,
            address=FIXED_ADDRESS,
        )
        response = api_call(**call_kwargs)
        logger.info("Connecto %s response: %s", action, response)

        # show_alert (e.g. "You are working on Holidays.") means the photo/
        # location were accepted but the sign-in itself needs a reason -
        # checked via show_alert rather than the message text, since that's
        # the field the API itself uses to flag this case.
        if action == "sign-in" and (response.get("data") or {}).get("show_alert"):
            reasonTitle = response["data"].get("reason_title", "")
            logger.info("Connecto sign-in needs a reason (reason_title=%r) - retrying.", reasonTitle)
            response = api_call(**call_kwargs, reason="Client Meeting", reason_title=reasonTitle)
            logger.info("Connecto sign-in retry response: %s", response)
    except Exception:
        logger.exception("Connecto %s failed - continuing with the existing attendance flow regardless.", action)
        return

    if not usingFallback:
        _archive_photo(photoPath, folder)


def signin():
    _run("sign-in", cc.sign_in, SIGNIN_DIR)


def signout():
    _run("sign-out", cc.sign_out, SIGNOUT_DIR)


if __name__ == "__main__":
    action = sys.argv[1] if len(sys.argv) > 1 else None
    if action == "signin":
        signin()
    elif action == "signout":
        signout()
    else:
        print("Usage: python3 connecto_auto.py [signin|signout]", file=sys.stderr)
        sys.exit(1)
