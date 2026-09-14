"""
Thin client for the handful of Connecto endpoints needed for a manual,
human-driven sign-in/sign-out. Nothing here is scheduled or automatic -
every call requires a value (OTP, photo, location) that only exists
because a person is doing this right now.
"""
import json
import os
from datetime import datetime
from typing import Optional

import requests

BASE_URL = "https://connecto.neosofttech.com/public/"
SESSION_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".connecto_session.json")

# Sent only where the API requires a device_os field at all - there's no
# device-model field in this API, so this is the only "device" fingerprint
# we can shape. Kept as a real Android OS designation (matching a Redmi
# Note 12 Pro) rather than an arbitrary/dummy value.
DEVICE_OS = "android"


class ConnectoError(RuntimeError):
    pass


def dig_for_key(obj, candidates):
    """Depth-first search of a nested dict/list for the first value whose
    key case-insensitively matches one of `candidates`. Returns (path, value)
    or (None, None). Used to fuzzy-match fields in Connecto responses, whose
    shape isn't documented anywhere public (see connecto_cli.py)."""
    candidates_lower = {c.lower() for c in candidates}
    stack = [("", obj)]
    while stack:
        path, node = stack.pop(0)
        if isinstance(node, dict):
            for k, v in node.items():
                new_path = f"{path}.{k}" if path else k
                if k.lower() in candidates_lower and not isinstance(v, (dict, list)):
                    return new_path, v
                stack.append((new_path, v))
        elif isinstance(node, list):
            for i, v in enumerate(node):
                stack.append((f"{path}[{i}]", v))
    return None, None


def _post(path: str, fields: dict, headers: Optional[dict] = None) -> dict:
    resp = requests.post(BASE_URL + path, data=fields, headers=headers or {}, timeout=15)
    try:
        body = resp.json()
    except ValueError:
        body = {"raw": resp.text}
    if resp.status_code >= 400:
        raise ConnectoError(f"POST {path} -> HTTP {resp.status_code}: {body}")
    return body


def auth_headers(token: str) -> dict:
    return {"Authorization": f"Bearer {token}", "Accept": "application/json"}


def request_otp(email: str, udid: str, device_token: str, device_os: str = DEVICE_OS) -> dict:
    return _post("api/v1/validate-email", {
        "email": email,
        "udid": udid,
        "device_token": device_token,
        "device_os": device_os,
    })


def validate_otp(email: str, otp: str) -> dict:
    return _post("api/v1/validate-otp", {"email": email, "otp": otp})


def request_new_device_otp(email: str) -> dict:
    """The "can't login" / device-switch flow: requests an OTP to register
    *this* device when the account is already registered on another one
    (e.g. the real phone with the Connecto app). Completing this flow with
    `validate_new_device_otp` likely deregisters that other device."""
    return _post("api/v1/validate-email-new-device-request", {"email": email})


def validate_new_device_otp(email: str, otp: str, udid: str, device_token: str, device_os: str = DEVICE_OS) -> dict:
    return _post("api/v1/validate-otp-new-device", {
        "email": email,
        "otp": otp,
        "udid": udid,
        "device_token": device_token,
        "device_os": device_os,
    })


def get_configuration_details(user_id: int, token: str) -> dict:
    return _post("api/v1/get-configuration-details", {"user_id": user_id}, auth_headers(token))


def get_todays_attendance(user_id: int, token: str) -> dict:
    return _post("api/v1/get-todays-attendance", {"user_id": user_id}, auth_headers(token))


def sign_in(user_id: int, token: str, config_id: int, image_b64: str,
            latitude: str, longitude: str, address: str = "", employee_mood: int = 5,
            reason: str = "", reason_title: str = "") -> dict:
    fields = {
        "user_id": user_id,
        "attendance_date": datetime.now().strftime("%Y-%m-%d"),
        "signin_image": image_b64,
        "signin_address": address,
        # "No" (not "0"/"1"/true/false) - confirmed by trial against the
        # live API, whose validation error for this field ("format is
        # invalid") doesn't match any documented rule.
        "is_manual_signin": "No",
        "auto_latitude": str(latitude),
        "auto_longitude": str(longitude),
        "config_id": config_id,
        "reason": reason,
        "reason_title": reason_title,
        "employee_mood": employee_mood,
    }
    return _post("api/v1/sign-in", fields, auth_headers(token))


def sign_out(user_id: int, token: str, config_id: int, image_b64: str,
             latitude: str, longitude: str, address: str = "") -> dict:
    fields = {
        "user_id": user_id,
        "attendance_date": datetime.now().strftime("%Y-%m-%d"),
        "signout_image": image_b64,
        "manual_latitude": str(latitude),
        "manual_longitude": str(longitude),
        "signout_address": address,
        "is_manual_signout": "0",
        "auto_latitude": str(latitude),
        "auto_longitude": str(longitude),
        "config_id": config_id,
        "reason": "",
        "reason_title": "",
    }
    return _post("api/v1/sign-out", fields, auth_headers(token))


def load_session() -> Optional[dict]:
    if os.path.exists(SESSION_PATH):
        with open(SESSION_PATH) as f:
            return json.load(f)
    return None


def save_session(session: dict) -> None:
    with open(SESSION_PATH, "w") as f:
        json.dump(session, f, indent=2)
    os.chmod(SESSION_PATH, 0o660)
