"""
Probes the Connecto API's error handling using deliberately fake input:
a bogus login (dummy email/OTP), a made-up auth token, and a synthetic
placeholder image generated in-memory. Nothing here is a real credential,
a real token, or a real photo - the goal is only to observe how the
backend responds (status codes, error shapes, validation order).
"""
import base64
import io
from typing import Optional

import requests
from PIL import Image

BASE_URL = "https://connecto.neosofttech.com/public/"
INVALID_TOKEN = "Bearer this-is-not-a-real-token"

COMMON_HEADERS = {
    "Authorization": INVALID_TOKEN,
    "Accept": "application/json",
}

DUMMY_EMAIL = "probe.dummy.test@example.com"
DUMMY_OTP = "000000"
DUMMY_UDID = "dummy-udid-0000"
DUMMY_DEVICE_TOKEN = "dummy-device-token-0000"
DUMMY_DEVICE_OS = "android"


def make_dummy_image_base64() -> str:
    """Synthetic solid-color JPEG, generated in-memory - not a real photo."""
    img = Image.new("RGB", (32, 32), color=(120, 120, 120))
    buf = io.BytesIO()
    img.save(buf, format="JPEG")
    return base64.b64encode(buf.getvalue()).decode("ascii")


DUMMY_IMAGE_B64 = make_dummy_image_base64()

SIGN_IN_FIELDS = {
    "user_id": 0,
    "attendance_date": "1970-01-01",
    "signin_image": DUMMY_IMAGE_B64,
    "manual_latitude": "0",
    "manual_longitude": "0",
    "signin_address": "",
    "is_manual_signin": "0",
    "auto_latitude": "0",
    "auto_longitude": "0",
    "config_id": 0,
    "reason": "",
    "reason_title": "",
    "employee_mood": 0,
}

SIGN_OUT_FIELDS = {
    "user_id": 0,
    "attendance_date": "1970-01-01",
    "signout_image": DUMMY_IMAGE_B64,
    "manual_latitude": "0",
    "manual_longitude": "0",
    "signout_address": "",
    "is_manual_signout": "0",
    "auto_latitude": "0",
    "auto_longitude": "0",
    "config_id": 0,
    "reason": "",
    "reason_title": "",
}

VALIDATE_EMAIL_FIELDS = {
    "email": DUMMY_EMAIL,
    "udid": DUMMY_UDID,
    "device_token": DUMMY_DEVICE_TOKEN,
    "device_os": DUMMY_DEVICE_OS,
}

VALIDATE_OTP_FIELDS = {
    "email": DUMMY_EMAIL,
    "otp": DUMMY_OTP,
}


def probe(name: str, path: str, fields: dict, headers: Optional[dict] = None) -> None:
    url = BASE_URL + path
    resp = requests.post(url, data=fields, headers=headers or {}, timeout=15)
    print(f"=== {name} ===")
    print(f"POST {url}")
    print(f"status: {resp.status_code}")
    print(f"body: {resp.text[:1000]}")
    print()


if __name__ == "__main__":
    # Login/token flow with fake credentials - expected to be rejected.
    probe("validate-email (dummy creds)", "api/v1/validate-email", VALIDATE_EMAIL_FIELDS)
    probe("validate-otp (dummy creds)", "api/v1/validate-otp", VALIDATE_OTP_FIELDS)

    # Sign-in/out with invalid token + synthetic placeholder image.
    probe("sign-in (invalid token, dummy image)", "api/v1/sign-in", SIGN_IN_FIELDS, COMMON_HEADERS)
    probe("sign-out (invalid token, dummy image)", "api/v1/sign-out", SIGN_OUT_FIELDS, COMMON_HEADERS)
