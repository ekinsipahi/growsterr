from django.contrib import admin
from django.urls import include, path

admin.site.site_header = admin.site.site_title = "Growsterr"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.core.urls")),
    path("", include("apps.growth.urls")),
    path("", include("apps.legal.urls")),
    # Last: the page engine owns the generated money-page paths and /sitemap.xml.
    path("", include("apps.pages.urls")),
]
