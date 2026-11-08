from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.templatetags.static import static
from django.views.decorators.cache import cache_page

PLATFORMS = [
    ("Instagram", "Followers, likes, views"),
    ("TikTok", "Followers, likes, views"),
    ("YouTube", "Subscribers, likes, views"),
]


def home(request):
    return render(request, "core/home.html", {"platforms": PLATFORMS})


@cache_page(60 * 60)
def robots_txt(request):
    lines = ["User-agent: *", "Allow: /", "Disallow: /admin/", "Disallow: /account/", "Disallow: /order/",
             f"Sitemap: {settings.SITE_URL}/sitemap.xml"]
    return HttpResponse("\n".join(lines) + "\n", content_type="text/plain")


def favicon(request):
    """Browsers ask for /favicon.ico; send them to the SVG icon."""
    response = HttpResponse(status=301)
    response["Location"] = static("img/favicon.ico")
    return response
