"""Terms, privacy, cookies, refunds (English). The order form links to /terms/#subscription."""
from django.urls import path

from . import views

app_name = "legal"

urlpatterns = [
    path("terms/", views.page, {"key": "terms"}, name="terms"),
    path("privacy/", views.page, {"key": "privacy"}, name="privacy"),
    path("cookies/", views.page, {"key": "cookies"}, name="cookies"),
    path("refunds/", views.page, {"key": "refunds"}, name="refunds"),
]
