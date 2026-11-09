# Growsterr

Growth packages for Instagram, TikTok and YouTube: followers, subscribers, likes and views.
A sister project of Sterr Agency, built on the same stack: Django 5.2 on Render, Postgres on
Supabase, email through Resend.

## Run locally (WSL)

The venv is built with WSL's own Python (`/usr/bin/python3.12`), not a Windows one.

```bash
python3.12 -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env          # DEBUG=True, SQLite (./db.sqlite3), emails in the console
python manage.py migrate
python manage.py runserver    # http://localhost:8000
```

Tests always run on SQLite: `python manage.py test apps`.

## Brand

- Indigo-violet `#5B3DF5`: trust and creativity, the main color.
- Coral `#FF6B4A`: energy; used for the rising arrow and for buttons.
- Ink `#17142E` and paper `#FAF9FF`.
- Display font: Outfit.
- Logo: a violet G whose top end becomes a coral arrow, wordmark "grow" + "sterr". Light and dark
  versions, icons and exports are in `design/logo/` (see its README); the site uses the copies in
  `static/img/`.

## Deploy (Render, set up by hand in the dashboard; no Blueprint)

Web service: Python, Frankfurt, Starter or higher, branch `main`, health check path `/healthz`.

**Disk** (Settings -> Disks): mount path `/var/data`, 1 GB. SQLite lives there; without a disk every
deploy wipes the database, so the app refuses to start on Render unless `SQLITE_PATH` (or
`DATABASE_URL`) is set. A disk means one instance and a short pause on each deploy. Render keeps
daily snapshots of the disk.

**Build command**

```bash
pip install -r requirements.txt && python manage.py collectstatic --noinput
```

**Start command** (migrations run here: the disk isn't mounted during the build)

```bash
python manage.py migrate --noinput && python manage.py ensure_superuser && gunicorn config.wsgi --bind 0.0.0.0:$PORT --workers 2 --threads 4 --timeout 60 --access-logfile -
```

**Environment** (copy the values from your local `.env`):

- `PYTHON_VERSION=3.12.3`, `SECRET_KEY` (a new random one), `DEBUG=False`, `SITE_URL=https://growsterr.com`
- `SQLITE_PATH=/var/data/db.sqlite3`, `CACHE_DIR=/var/data/cache`
- `RESEND_API_KEY`, `DEFAULT_FROM_EMAIL`, `TEAM_NOTIFY_EMAILS`, `GROWTH_NOTIFY_EMAILS`, `CONTACT_EMAIL`, `ERROR_EMAILS` (500 and webhook error alerts; defaults to the team inbox)
- `DJANGO_SUPERUSER_USERNAME`, `DJANGO_SUPERUSER_EMAIL`, `DJANGO_SUPERUSER_PASSWORD`
- `STRIPE_SECRET_KEY`, `STRIPE_PUBLISHABLE_KEY`, `STRIPE_WEBHOOK_SECRET`, `GROWTH_PAYMENTS`, `GROWTH_VERIFY_EMAIL`, `GROWTH_API_TOKEN`
- `GOOGLE_OAUTH_CLIENT_ID`, `GOOGLE_OAUTH_CLIENT_SECRET`
- `LINKSTERR_API_URL`, `LINKSTERR_AGENCY_TOKEN`, `WHATSAPP_NUMBER`, `WHATSAPP_DISPLAY`

`RENDER`, `RENDER_EXTERNAL_HOSTNAME` and `PORT` are set by Render.

**Stripe webhook** (the account is shared with Sterr Agency, Linksterr, eSIMsterr and others).
Only once https://growsterr.com answers: an endpoint that can't be reached gets every event in the
account, fails, and Stripe ends up disabling it. Run it locally, the secret lands in the local `.env`:

```bash
python manage.py setup_stripe --site-url https://growsterr.com
```

Then copy `STRIPE_WEBHOOK_SECRET` to Render (the webhook answers 503 until it's there), and set
`GROWTH_PAYMENTS=True` when checkout should take real payments.

**Scheduled jobs.** Render cron services can't mount the disk, so `send_renewal_reminders` and
`sync_linksterr` don't run as cron services while the data is on SQLite. Stripe's `invoice.upcoming`
event sends the renewal reminders and the dashboard pulls Linksterr's numbers. Run either command
by hand from the service's Shell if needed.

**Later: Supabase.** Set `DATABASE_URL` (Session pooler) and Postgres wins over SQLite. Move the
data with `dumpdata --natural-foreign --natural-primary -e contenttypes -e auth.permission -e sessions -e admin.logentry`,
then `migrate` and `loaddata` on Supabase.
