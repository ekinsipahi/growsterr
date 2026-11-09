from django.apps import AppConfig


class GrowthConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.growth"
    verbose_name = "Büyüme paketleri"

    def ready(self):
        from . import activity  # noqa: F401  (sign-in signal)
