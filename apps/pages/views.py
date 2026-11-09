from django.conf import settings
from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.cache import cache_page

from . import context, sitemaps

SITEMAP_CACHE = 60 * 60


def page(request, page, registry):
    """A money page or a platform hub. The route itself comes from the registry: a page
    without content has no route, so it is a 404 before it gets here."""
    if page.variant.is_hub:
        template = "pages/hub.html"
    elif page.variant.article and page.data.get("kind") == "guide":
        template = "pages/article.html"  # reading first, packages after
    else:
        template = "pages/page.html"
    return render(request, template, context.build(request, page, registry))


@cache_page(SITEMAP_CACHE)
def sitemap_index(request, registry):
    items = []
    for name, entries in sitemaps.sections(registry).items():
        rows = sitemaps.rows(entries, name)
        if rows:
            items.append((reverse("pages:sitemap_section", args=[name]), sitemaps.latest(rows)))
    return HttpResponse(sitemaps.index(items, settings.SITE_URL), content_type="application/xml; charset=utf-8")


@cache_page(SITEMAP_CACHE)
def sitemap_section(request, name, registry):
    entries = sitemaps.sections(registry).get(name)
    rows = sitemaps.rows(entries, name) if entries else []
    if not rows:
        raise Http404
    return HttpResponse(sitemaps.urlset(rows, settings.SITE_URL), content_type="application/xml; charset=utf-8")
