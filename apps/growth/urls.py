"""URL contract other apps rely on (names and paths must stay):
    growth:order    /order/            GET ?plan=starter|rising|pro&platform=instagram|tiktok|youtube&lang=<code>
    growth:account  /account/          the customer's dashboard
    growth:login    /account/login/
    growth:signup   /account/signup/
    growth:logout   /account/logout/
PLACEHOLDER views until the port lands."""
from django.urls import path

from . import views

app_name = "growth"

urlpatterns = [
    path("order/", views.placeholder, name="order"),
    path("account/", views.placeholder, name="account"),
    path("account/login/", views.placeholder, name="login"),
    path("account/signup/", views.placeholder, name="signup"),
    path("account/logout/", views.placeholder, name="logout"),
]
