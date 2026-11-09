"""Every image a money page shows, declared once and shared by all languages. A content file
points at an image by its id and writes its own alt text:

    "hero": {"image": "instagram-followers", "alt": "..."}

    "<id>": {"src": "img/pages/<platform>/<name>.webp",   # path under static/
             "width": 1600, "height": 1200,               # the file's real size (sets the slot's shape)
             "art": "followers",                          # placeholder drawing until the file exists
             "pending": True}                             # the file isn't there yet

Until the file exists the page shows a brand placeholder in the same proportions, so nothing
moves when the photo lands. Add the file, remove "pending", run manage.py check_pages.
check_pages fails for a missing file that isn't pending.
"""

# Placeholder drawings (templates/pages/_art.html).
ARTS = ("hub", "followers", "subscribers", "likes", "views", "comments", "growth")

HERO = {"width": 1600, "height": 1200}
SECTION = {"width": 1200, "height": 900}

IMAGES = {
    # Platform hubs
    "instagram-hub": {"src": "img/pages/instagram/hub.webp", **HERO, "art": "hub", "pending": True},
    "tiktok-hub": {"src": "img/pages/tiktok/hub.webp", **HERO, "art": "hub", "pending": True},
    "youtube-hub": {"src": "img/pages/youtube/hub.webp", **HERO, "art": "hub", "pending": True},
    # Money pages (heroes)
    "instagram-followers": {"src": "img/pages/instagram/followers.webp", **HERO, "art": "followers", "pending": True},
    "instagram-followers-1000": {"src": "img/pages/instagram/followers-1000.webp", **HERO, "art": "growth", "pending": True},
    "tiktok-likes": {"src": "img/pages/tiktok/likes.webp", **HERO, "art": "likes", "pending": True},
    "youtube-subscribers": {"src": "img/pages/youtube/subscribers.webp", **HERO, "art": "subscribers", "pending": True},
    # Section images
    "instagram-creator-studio": {"src": "img/pages/instagram/creator-studio.webp", **SECTION, "art": "growth", "pending": True},
    "instagram-real-people": {"src": "img/pages/instagram/real-people.webp", **SECTION, "art": "comments", "pending": True},
    "tiktok-creator": {"src": "img/pages/tiktok/creator.webp", **SECTION, "art": "views", "pending": True},
    "tiktok-watch-time": {"src": "img/pages/tiktok/watch-time.webp", **SECTION, "art": "views", "pending": True},
    "youtube-channel": {"src": "img/pages/youtube/channel.webp", **SECTION, "art": "growth", "pending": True},
    "youtube-viewers": {"src": "img/pages/youtube/viewers.webp", **SECTION, "art": "comments", "pending": True},
}
