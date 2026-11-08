"""Names shared by the growth app that must not pull in the 16-language content
(the admin and models import these at startup)."""

PLATFORMS = ("instagram", "tiktok", "youtube")
PLATFORM_NAMES = {"instagram": "Instagram", "tiktok": "TikTok", "youtube": "YouTube"}
PROFILE_URL = {
    "instagram": "https://www.instagram.com/{}/",
    "tiktok": "https://www.tiktok.com/@{}",
    "youtube": "https://www.youtube.com/@{}",
}
# What a new member of the audience is called on each platform (UI strings use {audience}).
AUDIENCE = {"instagram": "followers", "tiktok": "followers", "youtube": "subscribers"}

# Version of the terms a customer accepts on the order form; bump it when the terms change.
TERMS_VERSION = "2026-11-08"
