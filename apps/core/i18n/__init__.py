"""The core site in every language: one module per language, English as the source.

    apps/core/i18n/en.py       the English source: CHROME, HOME, PRICING, HOW, ABOUT, UPDATED
    apps/core/i18n/<code>.py   the same names in another language (docs/I18N.md)

A language's module is merged over English key by key (nested dicts too), so a key it leaves
out, or writes in a different shape (a string where English has a list...), shows in English.
A language without a module uses the English chrome, and has none of the core pages: /<code>/,
/<code>/pricing/, /<code>/how-it-works/ and /<code>/about/ exist only once its module defines
HOME, PRICING, HOW or ABOUT (English copy under /de/ would be duplicate content).
`python manage.py check_i18n [codes]` lists what each language is missing.

Routes are built when the URLconf loads: restart the server after adding a module."""
import logging
from functools import lru_cache
from importlib import import_module

from apps.core.languages import DEFAULT, LANG_BY_CODE, LANGS

logger = logging.getLogger(__name__)

# Page key -> (the module's dict, path after the language prefix).
PAGES = {
    "home": ("HOME", ""),
    "pricing": ("PRICING", "pricing/"),
    "how": ("HOW", "how-it-works/"),
    "about": ("ABOUT", "about/"),
}
SECTIONS = ("CHROME", "HOME", "PRICING", "HOW", "ABOUT")
PLATFORMS = ("instagram", "tiktok", "youtube")
LEGAL = ("terms", "privacy", "cookies", "refunds")


def module_name(code):
    return f"{__name__}.{code}"


@lru_cache(maxsize=None)
def load(code):
    """A site language's module, or None when it has none. A module that fails to import is
    logged and treated as missing, so one broken translation never takes the site down
    (check_i18n and the tests report it)."""
    if code not in LANG_BY_CODE:
        return None
    name = module_name(code)
    try:
        return import_module(name)
    except ModuleNotFoundError as error:
        if error.name != name:
            logger.exception("apps/core/i18n/%s.py can't be imported; English is used", code)
        return None
    except Exception:  # noqa: BLE001 - a syntax or runtime error in a translation file
        logger.exception("apps/core/i18n/%s.py can't be imported; English is used", code)
        return None


def shape(value):
    """The structure of a value without its text: lists and tuples by length, dicts by key."""
    if isinstance(value, dict):
        return {k: shape(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [shape(v) for v in value]
    return type(value).__name__


def merge(english, own):
    """`own` over `english`, key by key; nested dicts merge too. A value whose shape differs from
    the English one is left out (English shows), so a page never renders half a structure."""
    out = dict(english)
    for key, value in own.items():
        if key not in english:
            continue
        ref = english[key]
        if isinstance(ref, dict) and isinstance(value, dict):
            out[key] = merge(ref, value)
        elif shape(value) == shape(ref):
            out[key] = value
    return out


@lru_cache(maxsize=None)
def section(code, name):
    """One of SECTIONS in a language, merged over English. Shared: don't modify the result."""
    english = getattr(load(DEFAULT), name)
    own = getattr(load(code), name, None) if code != DEFAULT else None
    return merge(english, own) if isinstance(own, dict) else english


def chrome(code):
    return section(code if code in LANG_BY_CODE else DEFAULT, "CHROME")


def has_module(code):
    return code == DEFAULT or load(code) is not None


def has_page(code, page):
    """True when this language has its own copy of the core page (en always has)."""
    if code == DEFAULT:
        return True
    return isinstance(getattr(load(code), PAGES[page][0], None), dict)


def page(code, name):
    """The copy of a core page in a language, or None when the language doesn't have that page."""
    return section(code, PAGES[name][0]) if has_page(code, name) else None


def languages(page_name):
    """Codes of the languages that have this core page, in site order (English first)."""
    return [lang.code for lang in LANGS if has_page(lang.code, page_name)]


def path(page_name, code=DEFAULT):
    """/pricing/ for English, /de/pricing/ for German (whether or not it exists)."""
    prefix = "/" if code == DEFAULT else f"/{code}/"
    return prefix + PAGES[page_name][1]


def alternates(page_name):
    """The hreflang set of a core page: every language that has it, plus x-default (English).
    Empty while English is the only one."""
    codes = languages(page_name)
    if len(codes) < 2:
        return []
    return [(code, path(page_name, code)) for code in codes] + [("x-default", path(page_name))]


def lang_links(page_name):
    """[(Lang, path)] for the language switcher: this page in every language that has it, else
    that language's home page. Empty while English is the only one."""
    links = []
    for lang in LANGS:
        if has_page(lang.code, page_name):
            links.append((lang, path(page_name, lang.code)))
        elif has_page(lang.code, "home"):
            links.append((lang, path("home", lang.code)))
    return links if len(links) > 1 else []


def updated(code):
    """When a language's copy last changed: its UPDATED, else the English one."""
    english = getattr(load(DEFAULT), "UPDATED", None)
    return getattr(load(code), "UPDATED", english) if code != DEFAULT else english


def _hub(code, platform):
    """The platform hub of the money pages in this language, else the English one."""
    try:
        from apps.pages.registry import REGISTRY

        return REGISTRY.path(code, platform) or REGISTRY.path(DEFAULT, platform) or f"/{platform}/"
    except Exception:  # noqa: BLE001 - the page engine is someone else's: never break the chrome over it
        logger.exception("no hub path for %s/%s", code, platform)
        return f"/{platform}/"


@lru_cache(maxsize=None)
def site_links(code):
    """The links of the chrome in this language: a core page in the language when it has that
    page (else English), the platform hubs likewise, and the order, account and legal pages with
    ?lang= so they follow the visitor's language (the legal text itself stays English)."""
    code = code if code in LANG_BY_CODE else DEFAULT
    query = "" if code == DEFAULT else f"?lang={code}"
    links = {name: path(name, code if has_page(code, name) else DEFAULT) for name in PAGES}
    links.update({platform: _hub(code, platform) for platform in PLATFORMS})
    links.update(order="/order/" + query, login="/account/login/" + query, account="/account/" + query)
    legal_query = query if has_module(code) else ""
    links.update({name: f"/{name}/{legal_query}" for name in LEGAL})
    return links


def path_lang(request_path):
    """The language of a path by its prefix (/de/... -> "de") when that language has a module, else English."""
    code = request_path.lstrip("/").split("/", 1)[0]
    return code if code != DEFAULT and code in LANG_BY_CODE and has_module(code) else DEFAULT


def reset():
    """Forget the loaded modules and merged copy (tests that add a language)."""
    for cached in (load, section, site_links):
        cached.cache_clear()
