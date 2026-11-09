"""The money pages (cross variants of platform x service x quantity x modifier x language) and
/sitemap.xml. Every page path comes from the content registry: a variant without content has
no route at all. config/urls.py includes this app last, so it never shadows another app."""
from django.urls import path

from . import views
from .registry import REGISTRY

app_name = "pages"


def build(registry):
    return [
        path("sitemap.xml", views.sitemap_index, {"registry": registry}, name="sitemap"),
        path("sitemaps/<slug:name>.xml", views.sitemap_section, {"registry": registry}, name="sitemap_section"),
        *registry.urlpatterns(views.page),
    ]


urlpatterns = build(REGISTRY)
