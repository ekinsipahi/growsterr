"""What the core pages show besides text: images, icons, artwork and link targets, the same in
every language. The text lives in apps/core/i18n/<code>.py (English: en.py, with the copy rules
in its docstring; the translator's guide is docs/I18N.md). Lists here line up with the copy's
lists by position (check_i18n keeps their lengths equal to English)."""

PLATFORMS = (("instagram", "Instagram"), ("tiktok", "TikTok"), ("youtube", "YouTube"))

# HOME["platforms"][key]: the card image and the placeholder artwork color
PLATFORM_CARDS = {
    "instagram": {"image": "img/photos/platform-instagram.webp", "variant": "soft"},
    "tiktok": {"image": "img/photos/platform-tiktok.webp", "variant": "violet"},
    "youtube": {"image": "img/photos/platform-youtube.webp", "variant": "coral"},
}

HERO_IMAGE = "img/photos/hero-creator.webp"

# HOME["dash"]["points"], in order
DASHBOARD_ICONS = ("eye", "user-plus", "chart", "globe", "sparkle")
# The dashboard illustration's bar heights in % of the chart: no scale, no values.
DASHBOARD_BARS = (52, 64, 44, 70, 58, 48, 66, 74, 50, 60, 68, 46, 72, 56, 62, 78, 54, 66, 48, 70,
                  60, 74, 52, 64, 58, 76, 50, 68, 62, 56)

# PRICING["included"], in order
INCLUDED_ICONS = ("users", "heart", "calendar", "pin", "dashboard", "lock", "refresh", "card")

# HOW["flow"], in order: the photo, and the placeholder artwork until it exists
FLOW = (
    {"image": "img/photos/how-choose.webp", "art": "cards", "variant": "soft"},
    {"image": "img/photos/how-campaign.webp", "art": "rise", "variant": "violet"},
    {"image": "img/photos/how-people.webp", "art": "people", "variant": "coral"},
    {"image": "img/photos/how-dashboard.webp", "art": "dash", "variant": "soft"},
)

ABOUT_IMAGE = "img/photos/about-team.webp"
# ABOUT["values"], in order
VALUES_ICONS = ("users", "chart", "shield")

# Where each page's closing band sends its secondary button (a core page, in the page's language).
CTA_SECONDARY = {"home": "pricing", "pricing": "how", "how": "pricing", "about": "pricing"}
