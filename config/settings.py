"""Growsterr: Django settings. Every secret and deploy value comes from .env (or Render)."""
import sys
from pathlib import Path

import environ

BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env(BASE_DIR / ".env")

TESTING = "test" in sys.argv[1:2]

SECRET_KEY = env("SECRET_KEY", default="dev-insecure-change-me")
DEBUG = env("DEBUG")
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["growsterr.com", "www.growsterr.com", "localhost", "127.0.0.1"])
CSRF_TRUSTED_ORIGINS = env.list("CSRF_TRUSTED_ORIGINS", default=["https://growsterr.com", "https://www.growsterr.com"])
# Render sets this to the service's *.onrender.com host, so the deploy works before the domain is attached.
RENDER_EXTERNAL_HOSTNAME = env("RENDER_EXTERNAL_HOSTNAME", default="")
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)
    CSRF_TRUSTED_ORIGINS.append(f"https://{RENDER_EXTERNAL_HOSTNAME}")

# Canonical origin, no trailing slash: www redirects here; links in emails use it.
SITE_URL = env("SITE_URL", default="https://growsterr.com").rstrip("/")

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    "apps.core",
    "apps.growth",
    "apps.pages",
    "apps.legal",
]

MIDDLEWARE = [
    "apps.core.health.HealthCheckMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "apps.core.middleware.CanonicalHostMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "apps.core.context_processors.site",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

# SQLite for now: SQLITE_PATH (on Render a file on the persistent disk, e.g. /var/data/db.sqlite3;
# the build step has no disk, so migrations run in the start command), default ./db.sqlite3.
# Later production moves to Postgres on Supabase ("Session pooler": Render has no IPv6) through
# DATABASE_URL, or DB_HOST/DB_PORT/DB_NAME/DB_USER/DB_PASSWORD; either one wins over SQLite.
# Tests always use SQLite.
SQLITE_PATH = env("SQLITE_PATH", default="") or str(BASE_DIR / "db.sqlite3")
ON_RENDER = env.bool("RENDER", default=False)  # Render sets RENDER=true on its services
_postgres = bool(env("DATABASE_URL", default="") or env("DB_HOST", default=""))
if ON_RENDER and not TESTING and not _postgres and not env("SQLITE_PATH", default=""):
    from django.core.exceptions import ImproperlyConfigured
    # Without it the database would sit in the app folder, which every deploy wipes: all users lost.
    raise ImproperlyConfigured("On Render set SQLITE_PATH to a file on the persistent disk "
                               "(e.g. /var/data/db.sqlite3) or DATABASE_URL to Postgres.")
if TESTING:
    DATABASES = {"default": env.db_url_config(f"sqlite:///{BASE_DIR / 'db.sqlite3'}")}
elif env("DATABASE_URL", default=""):
    DATABASES = {"default": env.db("DATABASE_URL")}
elif env("DB_HOST", default=""):
    DATABASES = {"default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("DB_NAME", default="postgres"),
        "USER": env("DB_USER"),
        "PASSWORD": env("DB_PASSWORD"),
        "HOST": env("DB_HOST"),
        "PORT": env("DB_PORT", default="5432"),
    }}
else:
    DATABASES = {"default": env.db_url_config(f"sqlite:///{SQLITE_PATH}")}
DATABASES["default"]["CONN_MAX_AGE"] = env.int("CONN_MAX_AGE", default=60)
if DATABASES["default"]["ENGINE"].endswith("postgresql"):
    DATABASES["default"]["CONN_HEALTH_CHECKS"] = False
    DATABASES["default"].setdefault("OPTIONS", {})["sslmode"] = env("DB_SSLMODE", default="require")
elif not TESTING:
    # Several gunicorn workers share one file: WAL lets reads run during a write, IMMEDIATE takes
    # the write lock up front (no "database is locked" when a read turns into a write), and a
    # writer waits up to 30 s instead of failing (a Stripe webhook must not 500 over a lock).
    DATABASES["default"].setdefault("OPTIONS", {}).update({
        "init_command": "PRAGMA journal_mode=WAL; PRAGMA synchronous=NORMAL",
        "transaction_mode": "IMMEDIATE",
        "timeout": 30,
    })

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "en"
TIME_ZONE = "Europe/Istanbul"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"
# Nothing is uploaded yet; if that changes, point MEDIA_ROOT at the persistent disk on Render.
MEDIA_URL = "media/"
MEDIA_ROOT = env.path("MEDIA_ROOT", default=BASE_DIR / "media")
STORAGES = {
    "default": {"BACKEND": "django.core.files.storage.FileSystemStorage"},
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage"
        if not DEBUG and not TESTING
        else "django.contrib.staticfiles.storage.StaticFilesStorage"
    },
}

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# --- Email (Resend HTTP API); without a key, emails are printed to the console --------------
RESEND_API_KEY = env("RESEND_API_KEY", default="")
EMAIL_BACKEND = ("apps.core.resend_backend.ResendEmailBackend" if RESEND_API_KEY
                 else "django.core.mail.backends.console.EmailBackend")
DEFAULT_FROM_EMAIL = env("DEFAULT_FROM_EMAIL", default="Growsterr <noreply@growsterr.com>")
# The team's inbox for new orders and other events (comma-separated).
TEAM_NOTIFY_EMAILS = env.list("TEAM_NOTIFY_EMAILS", default=["ekinsipahi8@gmail.com"])
CONTACT_EMAIL = env("CONTACT_EMAIL", default="hello@growsterr.com")

# --- Growth packages: accounts, Stripe subscriptions, the dashboard (apps.growth) ----------
# Every package event (new request, payment, renewal, cancel, dispute) also goes to these,
# on top of TEAM_NOTIFY_EMAILS.
GROWTH_NOTIFY_EMAILS = env.list("GROWTH_NOTIFY_EMAILS", default=["ekinsipahi8@gmail.com"])
# Tests never reach Stripe, Google or Linksterr: their secrets are empty there and the tests
# that need them set their own.
_secret = (lambda name: "") if TESTING else (lambda name: env(name, default=""))
# The Stripe account is shared with Sterr Agency, Linksterr and other sites: Growsterr only
# touches its own objects (lookup keys growsterr_<plan>_monthly, metadata site=growsterr, its
# own webhook endpoint and portal configuration). Prices live in apps/growth/plan.py;
# `python manage.py setup_stripe` creates the prices, the portal configuration and the webhook.
STRIPE_SECRET_KEY = _secret("STRIPE_SECRET_KEY")
STRIPE_PUBLISHABLE_KEY = _secret("STRIPE_PUBLISHABLE_KEY")
STRIPE_WEBHOOK_SECRET = _secret("STRIPE_WEBHOOK_SECRET")
# Off: orders are taken as requests (team email, English auto-reply). On: Stripe Checkout.
GROWTH_PAYMENTS = env.bool("GROWTH_PAYMENTS", default=False)
# A confirmed email before the first payment (keeps card-testing scripts out).
GROWTH_VERIFY_EMAIL = env.bool("GROWTH_VERIFY_EMAIL", default=True)
LOGIN_URL = "growth:login"
# Sign in with Google (Google Cloud -> OAuth client, Web application). Authorized redirect URI:
# https://growsterr.com/account/google/complete/
GOOGLE_OAUTH_CLIENT_ID = _secret("GOOGLE_OAUTH_CLIENT_ID")
GOOGLE_OAUTH_CLIENT_SECRET = _secret("GOOGLE_OAUTH_CLIENT_SECRET")
# Bearer token of the growth system's API (/growth/api/...). Unset = API off.
GROWTH_API_TOKEN = _secret("GROWTH_API_TOKEN")
# Linksterr runs the promoted campaigns behind each package. GET /user-api/v1/agency/accounts/
# brings the delivery numbers; the same token (set on Linksterr too) also lets Linksterr read
# /growth/api/subscriptions/. Unset = no sync.
LINKSTERR_API_URL = env("LINKSTERR_API_URL", default="https://linksterr.com")
LINKSTERR_AGENCY_TOKEN = _secret("LINKSTERR_AGENCY_TOKEN")
del _secret
# WhatsApp line shown to customers (success page, emails).
WHATSAPP_NUMBER = env("WHATSAPP_NUMBER", default="905414487561")
WHATSAPP_DISPLAY = env("WHATSAPP_DISPLAY", default="+90 541 448 75 61")

# Rate limits and throttles live in the cache, so every gunicorn worker must see the same one:
# CACHE_DIR (on Render a folder on the persistent disk, e.g. /var/data/cache) = a file cache
# shared by the workers. Empty = in-memory, fine for runserver and tests.
CACHE_DIR = "" if TESTING else env("CACHE_DIR", default="")
CACHES = {"default": {"BACKEND": "django.core.cache.backends.filebased.FileBasedCache", "LOCATION": CACHE_DIR}
          if CACHE_DIR else {"BACKEND": "django.core.cache.backends.locmem.LocMemCache"}}

if not DEBUG:
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    SECURE_SSL_REDIRECT = env.bool("SECURE_SSL_REDIRECT", default=not TESTING)
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_HSTS_SECONDS = 60 * 60 * 24 * 30
    SECURE_CONTENT_TYPE_NOSNIFF = True

# Errors by email: a 500 (a Stripe webhook included) or an error logged by our apps goes to
# ERROR_EMAILS (default: the team inbox). Off with DEBUG and in tests.
ADMINS = [("Growsterr", email) for email in env.list("ERROR_EMAILS", default=TEAM_NOTIFY_EMAILS)]
SERVER_EMAIL = DEFAULT_FROM_EMAIL
EMAIL_SUBJECT_PREFIX = "[Growsterr hata] "
_alerts = not DEBUG and not TESTING
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {"class": "logging.StreamHandler"},
        "mail_admins": {"class": "django.utils.log.AdminEmailHandler", "level": "ERROR"},
    },
    "root": {"handlers": ["console"], "level": "INFO"},
    "loggers": {
        "django.request": {"handlers": ["mail_admins"] if _alerts else [], "level": "ERROR", "propagate": True},
        "apps": {"handlers": ["mail_admins"] if _alerts else [], "level": "ERROR", "propagate": True},
    },
}
