"""The dimensions a money page is made of. Keys here are language-independent; the words
people see come from the content files (apps/pages/content/<code>/).

A page = one variant (platform x service x quantity x modifier x country) in one language.
Only the platform is required: a variant with no service is the platform hub.
"""

PLATFORMS = ("instagram", "tiktok", "youtube")
PLATFORM_NAMES = {"instagram": "Instagram", "tiktok": "TikTok", "youtube": "YouTube"}

# What we grow on each platform, in display order. YouTube has subscribers where the others
# have followers; the two are the same thing (the audience), see family().
SERVICES = {
    "instagram": ("followers", "likes", "views", "comments"),
    "tiktok": ("followers", "likes", "views", "comments"),
    "youtube": ("subscribers", "likes", "views", "comments"),
}
ALL_SERVICES = ("followers", "subscribers", "likes", "views", "comments")


def family(service):
    """followers and subscribers are both 'audience'; likes, views, comments are themselves."""
    return "audience" if service in ("followers", "subscribers") else service


def counterpart(service, platform):
    """The same service on another platform: followers on YouTube is subscribers, and back."""
    for candidate in SERVICES[platform]:
        if family(candidate) == family(service):
            return candidate
    return None


# The package figure (apps.growth.plan.PLANS) a quantity of this service is measured against.
# Views have no typical ratio yet: a views page with a quantity names its package ("plan").
METRIC = {"audience": "followers", "likes": "likes", "comments": "comments"}

# A quantity is a goal ("1,000 followers"), never a pack we deliver.
QUANTITY_MIN, QUANTITY_MAX = 5, 1_000_000

# Modifiers come from keyword research (docs/keywords/). Add the key here first, then pages may use it.
# None = every platform; a tuple limits it, e.g. "reels": ("instagram",).
MODIFIERS = {
    # What we do: real people, every day, a monthly package.
    "real": None,
    "organic": None,
    "active": None,
    "monthly": None,
    "targeted": None,
    "gradual": None,
    "no-drop": None,
    "safe": None,
    "viral": None,
    "reels": ("instagram",),
    "shorts": ("youtube",),
    "fyp": ("tiktok",),
    "live": None,
    "comment-likes": None,
    "private-account": ("instagram", "tiktok"),
    "high-retention": ("youtube", "tiktok"),
    "promote": None,
    # Intent pages: people search for these; the page answers honestly (no, and here's what
    # works instead) and leads to the packages. INTENT_ALLOWS lets that one word through the
    # copy rules on that page only; nothing else is relaxed.
    "cheap": None,
    "fast": None,
    "free-trial": None,
    "free": None,
    "smm-panel": None,
    "verified": None,
    "female": ("instagram", "tiktok"),
    "ai": None,
    "custom": None,
}
# Modifiers that only make sense for some services.
MODIFIER_SERVICES = {
    "comment-likes": ("likes",),
    "high-retention": ("views",),
    "reels": ("likes", "views", "comments"),
    "shorts": ("likes", "views", "comments"),
    "live": ("likes", "views", "comments", "followers"),
    "ai": ("comments",),
    "custom": ("comments",),
}
INTENT_MODIFIERS = ("cheap", "fast", "free-trial", "free", "smm-panel", "verified", "female", "ai", "custom")
# Copy rules (checks.FORBIDDEN_ALL names) a page may break because the searcher's own word is
# the page's topic. Only on that page, and the copy must say plainly that we don't sell it.
INTENT_ALLOWS = {
    "free": ("free",),
    "free-trial": ("free",),
    "verified": ("celebrity or verified",),
    "female": ("gender targeting",),
}

# Country pages: ISO 3166-1 alpha-2 codes, lower case. The page's own copy names the country.
COUNTRIES = (
    "us", "gb", "ca", "au", "nz", "ie", "de", "fr", "es", "it", "nl", "se", "no", "dk", "fi", "pl", "pt", "ch",
    "gr", "tr", "ae", "sa", "qa", "kw", "eg", "lb", "in", "pk", "bd", "np", "lk", "ph", "vn", "id", "my", "kh",
    "jp", "kr", "cn", "ng", "ke", "gh", "ug", "za", "az", "pr", "br", "mx",
)

# Pages outside the platform x service grid (registry.Variant.article): guides, competitor
# alternatives, payment answers, agency services, free tools. ARTICLE_ALLOWS: as INTENT_ALLOWS,
# per kind (a guide may ask "do celebrities buy followers?", a payment page may say "crypto").
ARTICLE_KINDS = ("guide", "alternative", "payment", "agency", "tool", "intent")
ARTICLE_ALLOWS = {
    "guide": ("free", "celebrity or verified"),
    "payment": ("crypto",),
    "tool": ("free",),
    "intent": ("free",),
}


def modifier_allowed(modifier, platform, service=None):
    if modifier not in MODIFIERS:
        return False
    platforms = MODIFIERS[modifier]
    if platforms is not None and platform not in platforms:
        return False
    services = MODIFIER_SERVICES.get(modifier)
    return service is None or services is None or family(service) in {family(s) for s in services}


def allowed_rules(variant, kind=""):
    """The copy rules this page may break: its intent's own word, nothing else."""
    if variant.article:
        return ARTICLE_ALLOWS.get(kind, ())
    return INTENT_ALLOWS.get(variant.modifier, ())
