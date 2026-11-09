"""URL contract other apps rely on (names and paths must stay):
    core:home     /
    core:pricing  /pricing/          ?platform=instagram|tiktok|youtube opens that tab
    core:how      /how-it-works/
    core:about    /about/
    core:robots   /robots.txt        keeps its Sitemap line
    core:favicon  /favicon.ico
The same pages in another language: /<code>/, /<code>/pricing/, /<code>/how-it-works/,
/<code>/about/ (names core:home-<code>, core:pricing-<code>...), each only when
apps/core/i18n/<code>.py has that page's copy (apps/core/i18n/__init__.py)."""
from django.urls import path

from . import i18n, views
from .languages import DEFAULT

app_name = "core"

VIEWS = {"home": views.home, "pricing": views.pricing, "how": views.how, "about": views.about}


def build():
    """The routes, with one per language for each core page that language has."""
    patterns = [path(i18n.PAGES[name][1], view, name=name) for name, view in VIEWS.items()]
    patterns += [
        path("robots.txt", views.robots_txt, name="robots"),
        path("favicon.ico", views.favicon, name="favicon"),
    ]
    for name, view in VIEWS.items():
        for code in i18n.languages(name):
            if code != DEFAULT:
                patterns.append(path(i18n.path(name, code)[1:], view, {"lang": code}, name=f"{name}-{code}"))
    return patterns


urlpatterns = build()
