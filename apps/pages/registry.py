"""The money-page registry: every page that exists, read from the content files

    apps/pages/content/<code>/ui.py           UI: section titles and shared blocks of one language
    apps/pages/content/<code>/<platform>.py   PAGES: one dict per page (docs/CONTENT.md)
    apps/pages/content/<code>/<platform>_<part>.py   more PAGES of that platform (countries, quantities...)
    apps/pages/content/<code>/articles*.py    ARTICLES: guides, alternatives, payment, agency, tool pages

A page is one variant (dimensions.py: platform x service x quantity x modifier x country) in
one language. Its identity is the variant, never the slug: the same variant in two languages
is the same page in two languages (hreflang). A variant a language has no content for doesn't
exist there: no route, no link, no sitemap entry, a 404.

Loading never raises for bad content: a page that can't be placed (unknown service, slug
taken...) is skipped and reported in `problems`; manage.py check_pages reports everything.
"""
import os
import pkgutil
import re
from dataclasses import dataclass, replace
from datetime import date
from importlib import import_module

from apps.core.languages import DEFAULT, LANGS

from . import dimensions as dims
from .archive import ARCHIVED

CONTENT_PACKAGE = "apps.pages.content"
# Lower-case letters or digits (any script), words joined by "-" and path segments by "/".
SLUG_RE = re.compile(r"^[^\W_]+(?:[-/][^\W_]+)*$")
LANG_ORDER = {lang.code: i for i, lang in enumerate(LANGS)}


@dataclass(frozen=True, order=True)
class Variant:
    platform: str
    service: str = ""      # "" = the platform hub
    quantity: int = 0      # 0 = no quantity
    modifier: str = ""
    country: str = ""
    article: str = ""      # a page outside the grid (guide, alternative...): its language-independent key

    @property
    def is_hub(self):
        return not self.service and not self.article

    @property
    def is_base(self):
        """The service page itself (no quantity, modifier or country)."""
        return bool(self.service) and not (self.quantity or self.modifier or self.country)

    @property
    def key(self):
        """'instagram/followers/1000/real/in-us': language-independent, for messages and URL names."""
        if self.article:
            return f"article/{self.article}"
        parts = (self.platform, self.service, str(self.quantity) if self.quantity else "", self.modifier,
                 f"in-{self.country}" if self.country else "")
        return "/".join(part for part in parts if part)

    def sort_key(self):
        services = dims.SERVICES.get(self.platform, ())
        modifiers = list(dims.MODIFIERS)
        return (bool(self.article), self.article,
                dims.PLATFORMS.index(self.platform) if self.platform in dims.PLATFORMS else 99,
                services.index(self.service) if self.service in services else -1,
                self.quantity,
                modifiers.index(self.modifier) if self.modifier in modifiers else -1,
                self.country)


@dataclass(eq=False)
class Page:
    lang: str
    variant: Variant
    data: dict             # the raw content, placeholders unfilled
    source: str            # the content file, for messages
    updated: str = ""      # ISO date of the last real change (sitemap lastmod)

    @property
    def slug(self):
        return self.data["slug"]

    @property
    def path(self):
        prefix = "" if self.lang == DEFAULT else f"/{self.lang}"
        return f"{prefix}/{self.slug}/"

    @property
    def name(self):
        return f"{self.lang} {self.variant.key}"

    @property
    def lastmod(self):
        try:
            return date.fromisoformat(str(self.updated)) if self.updated else None
        except ValueError:
            return None

    def __repr__(self):
        return f"<Page {self.name} {self.path}>"


@dataclass(frozen=True)
class Problem:
    level: str         # "error" or "warning"
    where: str
    message: str

    def __str__(self):
        return f"{self.level.upper():7} {self.where}: {self.message}"


def _import(name):
    """The module, or None when it (or its package) doesn't exist. Errors inside it still raise."""
    try:
        return import_module(name)
    except ModuleNotFoundError as error:
        if error.name and (name == error.name or name.startswith(error.name + ".")):
            return None
        raise


class Registry:
    """files: [(lang, platform, source, PAGES, UPDATED)]; ui: {lang: UI}."""

    def __init__(self, files, ui=None):
        self.ui = dict(ui or {})
        self.pages = []
        self.problems = []
        self._by_variant = {}
        self._by_path = {}
        self._by_article = {}
        for lang, platform, source, entries, updated in files:
            self._add_file(lang, platform, source, entries, updated)
        self.pages.sort(key=lambda page: (LANG_ORDER.get(page.lang, 99), page.variant.sort_key()))

    @classmethod
    def load(cls, package=CONTENT_PACKAGE):
        from django.conf import settings

        files, ui = [], {}
        for lang in LANGS:
            if _import(f"{package}.{lang.code}") is None:
                continue
            ui_module = _import(f"{package}.{lang.code}.ui")
            if ui_module is not None:
                ui[lang.code] = getattr(ui_module, "UI", {})
            for name in content_modules(f"{package}.{lang.code}"):
                module = import_module(f"{package}.{lang.code}.{name}")
                source = os.path.relpath(module.__file__, settings.BASE_DIR)
                kind = name.split("_")[0]
                entries = getattr(module, "ARTICLES" if kind == ARTICLES else "PAGES", None)
                files.append((lang.code, kind, source, entries, getattr(module, "UPDATED", "")))
        return cls(files, ui)

    # --- Loading ------------------------------------------------------------------------
    def _error(self, where, message):
        self.problems.append(Problem("error", where, message))

    def _add_file(self, lang, platform, source, entries, updated):
        if lang not in LANG_ORDER:
            return self._error(source, f"unknown language '{lang}'")
        if platform not in dims.PLATFORMS and platform != ARTICLES:
            return self._error(source, f"unknown platform '{platform}'")
        if not isinstance(entries, (list, tuple)):
            return self._error(source, f"{'ARTICLES' if platform == ARTICLES else 'PAGES'} must be a list of page dicts")
        for number, data in enumerate(entries, 1):
            where = f"{lang} {platform} page #{number} ({source})"
            if not isinstance(data, dict):
                self._error(where, "a page must be a dict")
                continue
            variant, errors = self._variant(lang, platform, data)
            for message in errors:
                self._error(where, message)
            if errors:
                continue
            if variant.key in ARCHIVED:
                continue  # taken off the site (apps/pages/archive.py)
            page = Page(lang, variant, data, source, str(data.get("updated") or updated or ""))
            where = f"{page.name} ({source})"
            other = self._by_variant.get((lang, variant))
            if other is not None:
                self._error(where, f"this page is defined twice (also in {other.source})")
                continue
            other = self._by_path.get(page.path)
            if other is not None:
                self._error(where, f"slug '{page.slug}' is already used by {other.name}")
                continue
            if variant.article:
                other = self._by_article.get((lang, variant.article))
                if other is not None:
                    self._error(where, f"article '{variant.article}' is defined twice (also in {other.source})")
                    continue
                self._by_article[(lang, variant.article)] = page
            self.pages.append(page)
            self._by_variant[(lang, variant)] = page
            self._by_path[page.path] = page

    @staticmethod
    def _variant(lang, platform, data):
        errors = []
        if platform == ARTICLES:
            return Registry._article(lang, data)
        service = data.get("service") or ""
        quantity = data.get("quantity") or 0
        modifier = data.get("modifier") or ""
        country = data.get("country") or ""
        if service and service not in dims.SERVICES[platform]:
            errors.append(f"service '{service}' must be one of {', '.join(dims.SERVICES[platform])} on {platform}")
        if quantity and (not isinstance(quantity, int) or isinstance(quantity, bool)
                         or not dims.QUANTITY_MIN <= quantity <= dims.QUANTITY_MAX):
            errors.append(f"quantity must be a whole number from {dims.QUANTITY_MIN} to {dims.QUANTITY_MAX}")
        if modifier and not dims.modifier_allowed(modifier, platform, service or None):
            errors.append(f"modifier '{modifier}' isn't in dimensions.MODIFIERS for {platform} {service}".rstrip())
        if country and country not in dims.COUNTRIES:
            errors.append(f"country '{country}' isn't in dimensions.COUNTRIES")
        if not service and (quantity or modifier or country):
            errors.append("quantity, modifier and country need a service (a page without a service is the hub)")
        errors += _slug_errors(lang, data.get("slug"))
        variant = Variant(platform, service, quantity if isinstance(quantity, int) else 0, modifier, country)
        return variant, errors

    @staticmethod
    def _article(lang, data):
        """An article: its key (same in every language), kind, and the platform whose words and
        order link it uses (instagram unless it says)."""
        errors = []
        key, kind = data.get("article"), data.get("kind")
        platform = data.get("platform") or dims.PLATFORMS[0]
        if not isinstance(key, str) or not SLUG_RE.match(key or "") or "/" in key:
            errors.append("'article' must be a key like 'can-you-buy-instagram-followers' (the same in every language)")
        if kind not in dims.ARTICLE_KINDS:
            errors.append(f"'kind' must be one of {', '.join(dims.ARTICLE_KINDS)}")
        if platform not in dims.PLATFORMS:
            errors.append(f"'platform' must be one of {', '.join(dims.PLATFORMS)}")
        for field in ("service", "quantity", "modifier", "country"):
            if data.get(field):
                errors.append(f"an article has no '{field}' (that would make it a money page)")
        errors += _slug_errors(lang, data.get("slug"))
        return Variant(platform if platform in dims.PLATFORMS else dims.PLATFORMS[0], article=key or ""), errors

    # --- Lookups ------------------------------------------------------------------------
    def get(self, lang, variant):
        return self._by_variant.get((lang, variant))

    def find(self, lang, platform, service="", quantity=0, modifier="", country=""):
        return self.get(lang, Variant(platform, service, quantity, modifier, country))

    def path(self, lang, platform, service="", quantity=0, modifier="", country=""):
        """The path of a page, or None when that language doesn't have it. For other apps' links."""
        page = self.find(lang, platform, service, quantity, modifier, country)
        return page.path if page else None

    def at(self, path):
        return self._by_path.get(path)

    def languages(self):
        """Codes of the languages that have at least one page, in site order."""
        present = {page.lang for page in self.pages}
        return [lang.code for lang in LANGS if lang.code in present]

    def pages_in(self, lang):
        return [page for page in self.pages if page.lang == lang]

    def ui_for(self, lang):
        """A language's UI; English fills any key it doesn't have yet (check_pages reports those)."""
        return {**self.ui.get(DEFAULT, {}), **self.ui.get(lang, {})}

    def versions(self, variant):
        """The page in every language that has it, in site order."""
        return [page for lang in LANGS if (page := self.get(lang.code, variant))]

    # --- Relations ----------------------------------------------------------------------
    def alternates(self, page):
        """hreflang set: every language that has this variant, plus x-default (English)."""
        alts = [(other.lang, other.path) for other in self.versions(page.variant)]
        default = self.get(DEFAULT, page.variant)
        return alts + [("x-default", default.path)] if default else alts

    def nearest(self, lang, variant):
        """This variant in another language, or its closest parent there (for the language menu)."""
        chain = (variant, replace(variant, country=""), replace(variant, country="", modifier=""),
                 Variant(variant.platform, variant.service), Variant(variant.platform))
        for candidate in chain:
            page = self.get(lang, candidate)
            if page is not None:
                return page
        return None

    def lang_links(self, page):
        """[(Lang, path)] for the language switcher."""
        return [(lang, target.path) for lang in LANGS if (target := self.nearest(lang.code, page.variant))]

    def ancestors(self, page):
        """The pages above this one, top first: the platform hub, then the service page."""
        v = page.variant
        if v.article:
            return []
        chain = []
        if not v.is_hub:
            chain.append(self.get(page.lang, Variant(v.platform)))
            if not v.is_base:
                chain.append(self.get(page.lang, Variant(v.platform, v.service)))
        return [p for p in chain if p is not None]

    def related(self, page, limit=3):
        """A few cross-links, [(group, [pages])]: the other services of this platform (and the
        service page above a deeper page), the same service on the other platforms, and on a
        service page its strongest deeper pages. Kept short on purpose: no long link lists."""
        v, lang = page.variant, page.lang
        if v.is_hub:
            return []
        if v.article:
            kind = page.data.get("kind")
            same = [p for p in self.pages_in(lang) if p is not page and p.variant.article and p.data.get("kind") == kind]
            return [("articles", same[:limit])] if same else []
        own = [] if v.is_base else [self.get(lang, Variant(v.platform, v.service))]
        groups = [("platform", own + [self.get(lang, Variant(v.platform, s)) for s in dims.SERVICES[v.platform] if s != v.service])]
        cross = []
        for platform in dims.PLATFORMS:
            if platform == v.platform:
                continue
            service = dims.counterpart(v.service, platform)
            candidates = (replace(v, platform=platform, service=service), Variant(platform, service), Variant(platform))
            cross.append(next((p for c in candidates if (p := self.get(lang, c))), None))
        groups.append(("platforms", cross))
        if v.is_base:
            groups.append(("modifiers", self.strongest(lang, v.platform, v.service, 4)))
        return [(name, [p for p in pages if p is not None][:limit if name != "modifiers" else 4]) for name, pages in groups
                if any(p is not None for p in pages)]

    def strongest(self, lang, platform, service, count):
        """The deeper pages of a service worth a link: the ways we grow, then the round goals."""
        pages = [p for p in self.pages_in(lang) if p.variant.platform == platform and p.variant.service == service
                 and not p.variant.is_base and not p.variant.country and p.variant.modifier not in dims.INTENT_MODIFIERS]
        rank = {m: i for i, m in enumerate(LINK_ORDER)}
        ways = sorted((p for p in pages if p.variant.modifier and not p.variant.quantity),
                      key=lambda p: rank.get(p.variant.modifier, 50))
        goals = sorted((p for p in pages if p.variant.quantity and not p.variant.modifier),
                       key=lambda p: QUANTITY_ORDER.index(p.variant.quantity) if p.variant.quantity in QUANTITY_ORDER else 99)
        picks = ways[:count - 1] + goals[:1]  # the best ways to grow, plus one round goal
        rest = [p for p in ways + goals if p not in picks]
        return (picks + rest)[:count]

    def tree(self, hub):
        """For a hub: [(service, service page or None, [a few deeper pages])] in display order."""
        platform = hub.variant.platform
        out = []
        for service in dims.SERVICES[platform]:
            base = self.get(hub.lang, Variant(platform, service))
            out.append((service, base, self.strongest(hub.lang, platform, service, 4)))
        return out

    def hubs(self, lang):
        return [page for platform in dims.PLATFORMS if (page := self.get(lang, Variant(platform)))]

    # --- Routing and the sitemap --------------------------------------------------------
    def urlpatterns(self, view):
        from django.urls import path

        return [path(page.path[1:], view, {"page": page, "registry": self},
                     name=f"{page.lang}-{page.variant.key.replace('/', '-')}") for page in self.pages]

    def sitemap_entries(self, lang=None):
        return [{"path": page.path, "lastmod": page.lastmod, "alternates": self.alternates(page)}
                for page in self.pages if lang is None or page.lang == lang]


ARTICLES = "articles"
# Which deeper pages get the few links there are: the ways we grow first, then round goals.
LINK_ORDER = ("real", "organic", "gradual", "monthly", "targeted", "no-drop", "active", "safe", "reels", "shorts", "fyp",
              "live", "promote", "high-retention", "comment-likes")
QUANTITY_ORDER = (1000, 10000, 5000, 100000)


def content_modules(package):
    """A language's content modules, in name order: <platform>, <platform>_<part>, articles*."""
    pkg = _import(package)
    if pkg is None:
        return []
    names = sorted(m.name for m in pkgutil.iter_modules(pkg.__path__) if not m.ispkg)
    return [name for name in names
            if name.split("_")[0] in dims.PLATFORMS or name == ARTICLES or name.startswith(ARTICLES + "_")]


def _slug_errors(lang, slug):
    if not isinstance(slug, str) or not slug:
        return ["slug is missing"]
    if not SLUG_RE.match(slug) or slug != slug.lower():
        return [f"slug '{slug}' must be lower-case words joined by '-' (path segments by '/'), no slash at either end"]
    if lang == DEFAULT and slug.split("/")[0] in LANG_ORDER:
        return [f"slug '{slug}' starts with a language code: that prefix belongs to that language"]
    return []


REGISTRY = Registry.load()
