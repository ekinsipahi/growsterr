# Growsterr

Growth packages for Instagram, TikTok and YouTube: followers, subscribers, likes and views.
A sister project of Sterr Agency, built on the same stack: Django 5.2 on Render, Postgres on
Supabase, email through Resend.

## Run locally

```bash
python3 -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env          # DEBUG=True, SQLite, emails in the console
python manage.py migrate
python manage.py runserver
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

## Deploy

`render.yaml` is a Render Blueprint. Add the domain block once the domain points at Render.
