#!/usr/bin/env python3
"""
Manual, interactive Connecto sign-in/sign-out helper.

This is meant to be run BY HAND, in the moment, by whoever is physically
signing in or out - never on a timer or as part of the unattended
attendance_logger daemon. Each sign-in/sign-out needs a photo taken just
now and prints exactly what it's about to send so you can confirm before
anything goes over the network.

Usage:
    python3 connecto_cli.py login
    python3 connecto_cli.py login --new-device   # if login says "already registered on another device"
    python3 connecto_cli.py sign-in --photo /path/to/just-taken.jpg
    python3 connecto_cli.py sign-out --photo /path/to/just-taken.jpg
    python3 connecto_cli.py status

The response shape of this API isn't documented anywhere public - it was
reverse engineered from the Android app's endpoint list, not from real
responses. `login` prints the raw JSON it gets back at each step, and
makes a best-effort guess at which fields are the auth token / user id /
config id. If a guess looks wrong, you'll be asked to type the real
value in - that's expected on the first run against a real account.
"""
import argparse
import base64
import getpass
import os
import sys
import uuid
from datetime import datetime, timedelta

import connecto_client as cc

STALE_PHOTO_MINUTES = 15


def _confirm_or_override(label, guessed_path, guessed_value):
    if guessed_value is not None:
        answer = input(f"{label}: guessed {guessed_value!r} (from `{guessed_path}`). Use this? [Y/n] ").strip().lower()
        if answer in ("", "y", "yes"):
            return guessed_value
    manual = input(f"{label}: enter the correct value manually: ").strip()
    return manual


def _check_success(resp, step, hint=None):
    """Some endpoints return HTTP 200 with a `success: false` body instead
    of an HTTP error (e.g. "already registered from another device") - a
    plain response print alone makes that easy to miss and just leads to
    typing in an OTP that was never actually sent. Aborts if so."""
    if isinstance(resp, dict) and resp.get("success") is False:
        print(f"{step} failed: {resp.get('message', resp)}", file=sys.stderr)
        if hint:
            print(hint, file=sys.stderr)
        sys.exit(1)


def cmd_login(args):
    email = args.email or input("Connecto email: ").strip()

    session = cc.load_session() or {}
    udid = session.get("udid") or str(uuid.uuid4())
    device_token = session.get("device_token") or str(uuid.uuid4())

    if args.new_device:
        print(f"Requesting new-device OTP for {email} ...")
        print(
            "This is Connecto's device-switch flow (the app's \"can't login\" option) - it will "
            "likely deregister whatever device is currently registered on this account (e.g. "
            "your phone's Connecto app)."
        )
        if input("Proceed? [y/N] ").strip().lower() not in ("y", "yes"):
            print("Aborted.")
            return

        resp = cc.request_new_device_otp(email)
        print("validate-email-new-device-request response:")
        print(resp)
        _check_success(resp, "validate-email-new-device-request")

        otp = getpass.getpass("Enter the OTP you received: ").strip()
        resp = cc.validate_new_device_otp(email, otp, udid, device_token)
        print("validate-otp-new-device response:")
        print(resp)
        _check_success(resp, "validate-otp-new-device")

        # This udid/device_token pair is now the one the account recognizes
        # as its registered device - save it immediately (before anything
        # below can fail or get interrupted) so a retry reuses the already-
        # approved device instead of generating a new, unrecognized one and
        # having to redo the whole device-switch approval again.
        cc.save_session({**session, "email": email, "udid": udid, "device_token": device_token})

        # validate-otp-new-device only approves the device switch - it
        # doesn't return a token ("try to log-in now"). Chain straight into
        # a normal login, which should succeed now that this device is the
        # registered one.
        print("Device approved - logging in now ...")
        resp = cc.request_otp(email, udid, device_token)
        print("validate-email response:")
        print(resp)
        _check_success(resp, "validate-email")

        otp = getpass.getpass("Enter the OTP you received (a new one, sent for this login): ").strip()
        resp = cc.validate_otp(email, otp)
        print("validate-otp response:")
        print(resp)
        _check_success(resp, "validate-otp")
    else:
        print(f"Requesting OTP for {email} ...")
        resp = cc.request_otp(email, udid, device_token)
        print("validate-email response:")
        print(resp)
        _check_success(
            resp, "validate-email",
            hint="If this is because the account is already registered on another device, "
                 "re-run with --new-device instead.",
        )

        otp = getpass.getpass("Enter the OTP you received: ").strip()
        resp = cc.validate_otp(email, otp)
        print("validate-otp response:")
        print(resp)
        _check_success(resp, "validate-otp")

    token_path, token_val = cc.dig_for_key(resp, ["token", "access_token", "auth_token", "authToken"])
    token = _confirm_or_override("Auth token", token_path, token_val)

    user_id_path, user_id_val = cc.dig_for_key(resp, ["user_id", "userId", "id"])
    user_id = _confirm_or_override("User id", user_id_path, user_id_val)

    print("Fetching configuration details to find config_id ...")
    config_resp = cc.get_configuration_details(int(user_id), token)
    print("get-configuration-details response:")
    print(config_resp)
    config_id_path, config_id_val = cc.dig_for_key(config_resp, ["config_id", "configId", "id"])
    config_id = _confirm_or_override("Config id", config_id_path, config_id_val)

    cc.save_session({
        "email": email,
        "udid": udid,
        "device_token": device_token,
        "token": token,
        "user_id": int(user_id),
        "config_id": int(config_id),
        "logged_in_at": datetime.now().isoformat(),
    })
    print(f"Saved session to {cc.SESSION_PATH} (chmod 600).")


def _require_session():
    session = cc.load_session()
    if not session or not session.get("token"):
        print("No saved session. Run `python3 connecto_cli.py login` first.", file=sys.stderr)
        sys.exit(1)
    return session


def _load_photo_b64(photo_path):
    if not os.path.isfile(photo_path):
        print(f"Photo not found: {photo_path}", file=sys.stderr)
        sys.exit(1)

    age = datetime.now() - datetime.fromtimestamp(os.path.getmtime(photo_path))
    if age > timedelta(minutes=STALE_PHOTO_MINUTES):
        answer = input(
            f"Warning: {photo_path} is {age} old, not just-taken. "
            f"Use it anyway? [y/N] "
        ).strip().lower()
        if answer not in ("y", "yes"):
            print("Aborted - take a fresh photo and re-run.", file=sys.stderr)
            sys.exit(1)

    with open(photo_path, "rb") as f:
        return base64.b64encode(f.read()).decode("ascii")


def _extract_gps(photo_path):
    """Best-effort EXIF GPS extraction (decimal degrees) from a photo, so
    location comes from the same real photo rather than being typed in
    separately. Returns (lat, lon) or (None, None)."""
    try:
        from PIL import Image, ExifTags
    except ImportError:
        return None, None

    try:
        img = Image.open(photo_path)
        exif = img.getexif()
        gps_ifd = exif.get_ifd(0x8825)  # GPSInfo tag
        if not gps_ifd:
            return None, None

        def to_degrees(value):
            d, m, s = value
            return float(d) + float(m) / 60.0 + float(s) / 3600.0

        lat = to_degrees(gps_ifd[2])
        if gps_ifd[1] == "S":
            lat = -lat
        lon = to_degrees(gps_ifd[4])
        if gps_ifd[3] == "W":
            lon = -lon
        return lat, lon
    except Exception:
        return None, None


def _get_location(photo_path):
    lat, lon = _extract_gps(photo_path)
    if lat is not None and lon is not None:
        answer = input(f"Location from photo EXIF: {lat}, {lon}. Use this? [Y/n] ").strip().lower()
        if answer in ("", "y", "yes"):
            return lat, lon
    lat = input("Enter current latitude: ").strip()
    lon = input("Enter current longitude: ").strip()
    return lat, lon


def cmd_sign_in(args):
    session = _require_session()
    image_b64 = _load_photo_b64(args.photo)
    lat, lon = _get_location(args.photo)
    address = args.address or input("Address (optional, press enter to skip): ").strip()

    print(f"About to sign IN as user_id={session['user_id']} at {lat},{lon} using {args.photo}")
    if input("Proceed? [y/N] ").strip().lower() not in ("y", "yes"):
        print("Aborted.")
        return

    resp = cc.sign_in(
        user_id=session["user_id"],
        token=session["token"],
        config_id=session["config_id"],
        image_b64=image_b64,
        latitude=lat,
        longitude=lon,
        address=address,
    )
    print("sign-in response:")
    print(resp)


def cmd_sign_out(args):
    session = _require_session()
    image_b64 = _load_photo_b64(args.photo)
    lat, lon = _get_location(args.photo)
    address = args.address or input("Address (optional, press enter to skip): ").strip()

    print(f"About to sign OUT as user_id={session['user_id']} at {lat},{lon} using {args.photo}")
    if input("Proceed? [y/N] ").strip().lower() not in ("y", "yes"):
        print("Aborted.")
        return

    resp = cc.sign_out(
        user_id=session["user_id"],
        token=session["token"],
        config_id=session["config_id"],
        image_b64=image_b64,
        latitude=lat,
        longitude=lon,
        address=address,
    )
    print("sign-out response:")
    print(resp)


def cmd_status(args):
    session = _require_session()
    resp = cc.get_todays_attendance(session["user_id"], session["token"])
    print(resp)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)

    p_login = sub.add_parser("login", help="Request OTP, validate it, fetch config_id, save session")
    p_login.add_argument("--email")
    p_login.add_argument(
        "--new-device", action="store_true",
        help="Use the device-switch flow instead of a plain login - needed when validate-email "
             "reports the account is already registered on another device. Will likely "
             "deregister that other device (e.g. your phone's Connecto app).",
    )
    p_login.set_defaults(func=cmd_login)

    p_in = sub.add_parser("sign-in", help="Sign in with a fresh photo")
    p_in.add_argument("--photo", required=True)
    p_in.add_argument("--address")
    p_in.set_defaults(func=cmd_sign_in)

    p_out = sub.add_parser("sign-out", help="Sign out with a fresh photo")
    p_out.add_argument("--photo", required=True)
    p_out.add_argument("--address")
    p_out.set_defaults(func=cmd_sign_out)

    p_status = sub.add_parser("status", help="Fetch today's attendance status")
    p_status.set_defaults(func=cmd_status)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
