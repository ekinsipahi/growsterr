"""Test helpers: content registries built from data, and a URLconf that routes them."""
import json
import re
import types
from copy import deepcopy
from html.parser import HTMLParser

from django.urls import include, path

from apps.pages.registry import REGISTRY, Registry

UI = REGISTRY.ui


def page_data(lang="en", platform="instagram", **variant):
    """A copy of a real English page's content (the variant chooses which)."""
    page = REGISTRY.find("en", platform, **variant)
    return deepcopy(page.data)


def registry(files, ui=None):
    """files: {(lang, platform): [page dicts]}. Every language gets the English UI unless given."""
    ui = ui if ui is not None else {lang: UI["en"] for lang, _ in files}
    ui.setdefault("en", UI["en"])
    return Registry([(lang, platform, f"test/{lang}/{platform}.py", pages, "2026-11-08")
                     for (lang, platform), pages in files.items()], ui)


def urlconf(reg):
    """The project's URLs with the money pages built from `reg` (for override_settings(ROOT_URLCONF=...))."""
    from config import urls as project_urls
    from apps.pages.urls import build

    module = types.ModuleType("pages_test_urls")
    module.urlpatterns = [p for p in project_urls.urlpatterns if getattr(p, "app_name", None) != "pages"]
    module.urlpatterns.append(path("", include((build(reg), "pages"))))
    return module


def jsonld(html):
    """Every JSON-LD block of a page, parsed."""
    blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.S)
    return [json.loads(block) for block in blocks]


class TextOf(HTMLParser):
    """The visible text of a page's <main>, minus the subtrees whose class is in `skip`."""

    VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}

    def __init__(self, skip=()):
        super().__init__()
        self.skip, self.parts, self.depth, self.skipping, self.in_main = set(skip), [], 0, 0, False

    def handle_starttag(self, tag, attrs):
        if tag == "main":
            self.in_main = True
        if tag in self.VOID or not self.in_main:
            return
        self.depth += 1
        classes = set((dict(attrs).get("class") or "").split())
        if self.skipping or classes & self.skip or tag in ("script", "style"):
            self.skipping += 1

    def handle_endtag(self, tag):
        if tag == "main":
            self.in_main = False
        if tag in self.VOID or not self.in_main or self.depth == 0:
            return
        self.depth -= 1
        if self.skipping:
            self.skipping -= 1

    def handle_data(self, data):
        if self.in_main and not self.skipping and data.strip():
            self.parts.append(data.strip())


def visible_text(html, skip=()):
    parser = TextOf(skip)
    parser.feed(html)
    return " ".join(parser.parts)
