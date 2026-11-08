# Growsterr logo

The artwork came from Gemini (`source/`). These are clean vectors traced from it with potrace
(`vectorize.py`), with the colors snapped to the brand palette.

| File | Use |
|---|---|
| `logo.svg` | Wordmark on light backgrounds: violet G, coral arrow, "grow" ink, "sterr" violet |
| `logo-dark.svg` | Wordmark on dark backgrounds: light violet G and "sterr", white "grow" |
| `mark.svg` / `mark-dark.svg` | The symbol alone (G + rising arrow) |
| `icon.svg` | App icon: white G on a violet rounded square (works on light and dark) |
| `icon-inverse.svg` | Violet G on a white rounded square |
| `icon-bleed.svg` | Full square, for iOS, which rounds the corners itself |
| `export/` | Transparent PNGs: logos at 2x, icons and marks at 1024 px |

Colors: violet `#5B3DF5` (on dark `#8E7BFF`), coral `#FF6B4A` (on dark `#FF7A5C`),
ink `#17142E` (on dark `#F4F2FF`).

The site uses copies in `static/img/` (logo, logo-dark, mark, mark-dark, icon, icon-inverse,
favicon.svg/.ico, apple-touch-icon.png, icon-192/512.png). The header shows `logo.svg` or
`logo-dark.svg` with the `.only-light` / `.only-dark` classes, so the logo follows both the system
theme and the theme toggle.
