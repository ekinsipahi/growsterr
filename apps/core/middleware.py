from urllib.parse import urlsplit

from django.conf import settings
from django.http import HttpResponsePermanentRedirect


class CanonicalHostMiddleware:
    """301 www.<domain> -> <domain> (the host in SITE_URL), so there is one origin. Other hosts
    (localhost, health checks) pass through; the *.onrender.com preview host is served noindex."""

    def __init__(self, get_response):
        self.get_response = get_response
        self.canonical = urlsplit(settings.SITE_URL).hostname or ""

    def __call__(self, request):
        host = request.get_host().split(":")[0].lower()
        if self.canonical and host == f"www.{self.canonical}":
            return HttpResponsePermanentRedirect(f"{settings.SITE_URL}{request.get_full_path()}")
        response = self.get_response(request)
        if host.endswith(".onrender.com"):
            response["X-Robots-Tag"] = "noindex, nofollow"
        return response
