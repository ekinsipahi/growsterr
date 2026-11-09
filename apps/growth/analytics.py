"""Hashed user data for conversion events on the success and account pages
(gtag('set', 'user_data') when analytics is set up). Only SHA-256 hashes leave the server."""
import hashlib
import re


def _sha256(value):
    return hashlib.sha256(value.encode()).hexdigest()


def hashed_user_data(email, phone=""):
    """{"sha256_email_address": ..., "sha256_phone_number": ...}; the phone only in E.164 (+...)."""
    data = {}
    email = (email or "").strip().lower()
    if "@" in email:
        data["sha256_email_address"] = _sha256(email)
    raw = (phone or "").strip()
    digits = re.sub(r"\D", "", raw)
    e164 = f"+{digits}" if raw.startswith("+") else (f"+{digits[2:]}" if digits.startswith("00") else "")
    if 8 <= len(e164) <= 16:
        data["sha256_phone_number"] = _sha256(e164)
    return data
