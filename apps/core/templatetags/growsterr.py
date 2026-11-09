"""Template tags of the Growsterr design system: {% load growsterr %}.

    {% site_ui lang as ui %}        chrome strings in a language (apps/core/i18n/<code>.py CHROME),
                                    English key by key where the language has none
    {% site_links lang as site_links %}  the chrome's links in a language (apps.core.i18n.site_links)
    {% icon "check" %}            inline SVG icon (templates/partials/icon.html), aria-hidden
    {% icon "arrow" size=18 cls="x" %}
    {% image_slot "img/photos/hero.webp" alt="..." width=1200 height=1500 variant="violet" art="people" %}
        An image slot: a <figure> with a brand placeholder (variant: violet|soft|coral; art:
        people|rise|platform; glyph: instagram|tiktok|youtube for art="platform"). The <img> is
        rendered only once the file exists in static/, so pages never show a broken image;
        drop the file in and it appears (eager=True for the first image on a page)."""
from functools import lru_cache

from django import template
from django.conf import settings
from django.contrib.staticfiles import finders
from django.templatetags.static import static

from apps.core import i18n
from apps.core.company import COMPANY

register = template.Library()


def _filled(strings):
    out = dict(strings)
    for key, value in COMPANY.items():
        out["company_line"] = out["company_line"].replace("{" + key + "}", str(value))
    return out


@register.simple_tag
def site_ui(lang="en"):
    return _filled(i18n.chrome(lang or "en"))


@register.simple_tag
def site_links(lang="en"):
    return i18n.site_links(lang or "en")


@register.inclusion_tag("partials/icon.html")
def icon(name, size=20, cls=""):
    return {"name": name, "size": size, "cls": cls}


def _find(path):
    return static(path) if finders.find(path) else ""


_find_cached = lru_cache(maxsize=256)(_find)


def static_if_exists(path):
    """The static URL of `path` if the file exists, else "" (cached outside DEBUG)."""
    return _find(path) if settings.DEBUG else _find_cached(path)


@register.inclusion_tag("partials/image_slot.html")
def image_slot(path, alt="", width=1200, height=900, variant="violet", art="rise", glyph="",
               eager=False, sizes="", caption="", cls=""):
    return {
        "url": static_if_exists(path) if path else "",
        "alt": alt, "width": width, "height": height, "variant": variant, "art": art,
        "glyph": glyph, "eager": eager, "sizes": sizes, "caption": caption, "cls": cls,
    }
