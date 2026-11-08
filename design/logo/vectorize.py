"""Vectorize the Gemini logo art (icon + wordmark) into clean SVGs with potrace, in brand colors,
with light and dark versions. usage: vectorize.py SCRATCH OUTDIR"""
import os
import re
import subprocess
import sys
from collections import deque

import numpy as np
from scipy import ndimage
from PIL import Image

S, OUT = sys.argv[1], sys.argv[2]
GEM = f"{S}/gem"
POTRACE = f"{S}/libs/root/usr/bin/potrace"
ENV = {**os.environ, "LD_LIBRARY_PATH": f"{S}/libs/root/usr/lib/x86_64-linux-gnu"}
UP = 4  # trace at 4x for smooth curves
SMOOTH = 0.9  # blur radius in source pixels before tracing

# Brand colors (the art is normalized to these).
VIOLET, CORAL, INK, PAPER, WHITE = "#5B3DF5", "#FF6B4A", "#17142E", "#FAF9FF", "#FFFFFF"
VIOLET_DARK, CORAL_DARK, TEXT_DARK = "#8E7BFF", "#FF7A5C", "#F4F2FF"


def rgb(h):
    return np.array([int(h[i:i + 2], 16) for i in (1, 3, 5)], float)


def load(name):
    return np.asarray(Image.open(f"{GEM}/{name}").convert("RGB"), float)


def border_color(img):
    edge = np.concatenate([img[:6].reshape(-1, 3), img[-6:].reshape(-1, 3), img[:, :6].reshape(-1, 3), img[:, -6:].reshape(-1, 3)])
    return np.median(edge, axis=0)


def toward(img, base, target):
    """How far each pixel is from base toward target (0..1), and how far it is off that line."""
    d = target - base
    v = img - base
    a = np.clip((v @ d) / (d @ d), 0, 1)
    off = np.linalg.norm(v - a[..., None] * d, axis=-1)
    return a, off


def split(img, base, colors, floor=0.12, min_dist=10.0, merge=()):
    """{name: alpha mask}. Each pixel goes to the color whose direction from `base` it follows
    most closely (angle, so a darker shade of violet still counts as violet), and its alpha is
    how far along that direction it is. `merge` names pairs of colors that JPEG edges confuse
    (e.g. violet and ink): inside each connected shape, the minority of the pair joins the majority."""
    names = list(colors)
    v = img - base
    norm = np.linalg.norm(v, axis=-1)
    cos, alpha = [], []
    for n in names:
        d = rgb(colors[n]) - base
        cos.append((v @ d) / (np.maximum(norm, 1e-6) * np.linalg.norm(d)))
        alpha.append(np.clip((v @ d) / (d @ d), 0, 1))
    cos, alpha = np.stack(cos), np.stack(alpha)
    pick = np.argmax(cos, axis=0)
    live = norm > min_dist
    for a_name, b_name in merge:
        ia, ib = names.index(a_name), names.index(b_name)
        both = live & ((pick == ia) | (pick == ib)) & (np.maximum(alpha[ia], alpha[ib]) > 0.25)
        labels, count = ndimage.label(both, structure=np.ones((3, 3)))
        if not count:
            continue
        idx = np.arange(1, count + 1)
        wa = ndimage.sum(np.where(pick == ia, alpha[ia], 0), labels, idx)
        wb = ndimage.sum(np.where(pick == ib, alpha[ib], 0), labels, idx)
        winner = np.where(wa >= wb, ia, ib)
        comp_winner = np.concatenate([[-1], winner])[labels]
        pick = np.where(both, comp_winner, pick)
    out = {}
    for i, n in enumerate(names):
        m = np.where((pick == i) & live, alpha[i], 0.0)
        out[n] = np.where(m < floor, 0.0, m)
    return out


def trace(mask, name):
    """Alpha mask (1 = shape) -> list of SVG path data in the mask's pixel units."""
    h, w = mask.shape
    # Upscale, then blur away the JPEG's pixel stairs before potrace thresholds at 50%.
    img = Image.fromarray((255 * (1 - mask)).clip(0, 255).astype(np.uint8))
    img = img.resize((w * UP, h * UP), Image.Resampling.BICUBIC)
    smooth = ndimage.gaussian_filter(np.asarray(img, float), sigma=SMOOTH * UP)
    img = Image.fromarray(smooth.clip(0, 255).astype(np.uint8))
    pgm = f"{GEM}/{name}.pgm"
    img.save(pgm)
    out = f"{GEM}/{name}.trace.svg"
    subprocess.run([POTRACE, pgm, "-b", "svg", "-o", out, "--flat", "-k", "0.5", "-t", str(6 * UP),
                    "-a", "1.0", "-O", "1.0", "-u", "10"], check=True, env=ENV)
    text = open(out).read()
    tx, ty, sx, sy = map(float, re.search(
        r'transform="translate\(([-\d.]+),([-\d.]+)\) scale\(([-\d.]+),([-\d.]+)\)"', text).groups())
    paths = re.findall(r'<path d="([^"]+)"', text)
    return [_transform(d, sx / UP, sy / UP, tx / UP, ty / UP) for d in paths]


def _transform(d, sx, sy, tx, ty):
    """Apply x' = sx*x + tx, y' = sy*y + ty to potrace path data (M/m/L/l/C/c/z), round to 2 decimals."""
    tokens = re.findall(r"[MmLlCcZz]|-?\d+(?:\.\d+)?", d)
    out, cmd, nums = [], None, []

    def flush():
        if cmd is None:
            return
        absolute = cmd.isupper()
        vals = []
        for i, n in enumerate(nums):
            if i % 2 == 0:
                vals.append(sx * n + (tx if absolute else 0))
            else:
                vals.append(sy * n + (ty if absolute else 0))
        out.append(cmd + " ".join(f"{v:.2f}".rstrip("0").rstrip(".") for v in vals))

    for t in tokens:
        if t.isalpha():
            flush()
            cmd, nums = t, []
            if t in "Zz":
                out.append("z")
                cmd = None
        else:
            nums.append(float(t))
    flush()
    return "".join(out)


def bbox(*masks, pad=0.0):
    m = np.maximum.reduce([x for x in masks])
    ys, xs = np.where(m > 0.5)
    x0, x1, y0, y1 = xs.min(), xs.max() + 1, ys.min(), ys.max() + 1
    p = pad * max(x1 - x0, y1 - y0)
    return x0 - p, y0 - p, x1 - x0 + 2 * p, y1 - y0 + 2 * p


def svg(view, body, title):
    x, y, w, h = view
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x:.1f} {y:.1f} {w:.1f} {h:.1f}" '
            f'width="{w:.0f}" height="{h:.0f}" role="img" aria-label="{title}"><title>{title}</title>{body}</svg>\n')


def paths(ds, fill):
    return f'<path fill="{fill}" d="{"".join(ds)}"/>'


def outside_region(solid):
    """Pixels connected to the image border through non-solid pixels (flood fill)."""
    h, w = solid.shape
    seen = np.zeros_like(solid, bool)
    q = deque((y, x) for y in range(h) for x in (0, w - 1) if not solid[y, x])
    q.extend((y, x) for x in range(w) for y in (0, h - 1) if not solid[y, x])
    for y, x in q:
        seen[y, x] = True
    while q:
        y, x = q.popleft()
        for ny, nx in ((y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)):
            if 0 <= ny < h and 0 <= nx < w and not seen[ny, nx] and not solid[ny, nx]:
                seen[ny, nx] = True
                q.append((ny, nx))
    return seen


os.makedirs(OUT, exist_ok=True)

# --- Wordmark: violet G + "sterr", coral arrow, ink "grow" -----------------------------------
wm = load("wordmark-src.jpg")
bg = border_color(wm)
layers = split(wm, bg, {"violet": "#513FE1", "coral": "#FF7055", "ink": "#141533"}, merge=[("violet", "ink")])
view = bbox(*layers.values(), pad=0.012)
v_d, c_d, i_d = trace(layers["violet"], "wm-violet"), trace(layers["coral"], "wm-coral"), trace(layers["ink"], "wm-ink")
light = paths(v_d, VIOLET) + paths(c_d, CORAL) + paths(i_d, INK)
dark = paths(v_d, VIOLET_DARK) + paths(c_d, CORAL_DARK) + paths(i_d, TEXT_DARK)
open(f"{OUT}/logo.svg", "w").write(svg(view, light, "Growsterr"))
open(f"{OUT}/logo-dark.svg", "w").write(svg(view, dark, "Growsterr"))

# The symbol alone (G + arrow), cut from the wordmark: everything left of "grow".
# "grow" starts where the ink columns become solid; the arrow ends where coral stops.
ink_start = np.where((layers["ink"] > 0.5).sum(axis=0) > 20)[0].min()
coral_end = np.where((layers["coral"] > 0.5).sum(axis=0) > 0)[0].max()
cut = (ink_start + coral_end) // 2
sym = {k: np.where(np.arange(wm.shape[1])[None, :] < cut, m, 0.0) for k, m in layers.items() if k != "ink"}
sv, sc = trace(sym["violet"], "sym-violet"), trace(sym["coral"], "sym-coral")
sview = bbox(*sym.values(), pad=0.04)
side = max(sview[2], sview[3])
sview = (sview[0] - (side - sview[2]) / 2, sview[1] - (side - sview[3]) / 2, side, side)
open(f"{OUT}/mark.svg", "w").write(svg(sview, paths(sv, VIOLET) + paths(sc, CORAL), "Growsterr"))
open(f"{OUT}/mark-dark.svg", "w").write(svg(sview, paths(sv, VIOLET_DARK) + paths(sc, CORAL_DARK), "Growsterr"))

# --- App icon: violet rounded square, white G, coral arrow ----------------------------------
ic = load("icon-src.jpg")
obg = border_color(ic)
violet_src = rgb("#523EE7")
a_sq, _ = toward(ic, obg, violet_src)
solid = a_sq > 0.5
outside = outside_region(solid)
inside = ~outside
ys, xs = np.where(inside)
x0, x1, y0, y1 = xs.min(), xs.max() + 1, ys.min(), ys.max() + 1
# Corner radius from where the diagonal from the bbox corner enters the shape.
t = next(k for k in range(0, (x1 - x0) // 2) if inside[y0 + k, x0 + k])
radius = t / (1 - 2 ** -0.5)
inner = split(ic, violet_src, {"white": "#FDFDFE", "coral": "#FE6850"})
inner = {k: np.where(inside, m, 0.0) for k, m in inner.items()}
g_d, a_d = trace(inner["white"], "ic-white"), trace(inner["coral"], "ic-coral")
side = max(x1 - x0, y1 - y0)
iview = (x0, y0, side, side)
rect = f'<rect x="{x0}" y="{y0}" width="{side}" height="{side}" rx="{radius:.1f}" fill="{{}}"/>'
open(f"{OUT}/icon.svg", "w").write(svg(iview, rect.format(VIOLET) + paths(g_d, WHITE) + paths(a_d, CORAL), "Growsterr"))
open(f"{OUT}/icon-inverse.svg", "w").write(svg(iview, rect.format(WHITE) + paths(g_d, VIOLET) + paths(a_d, CORAL), "Growsterr"))
# Full-bleed square for iOS (it rounds the corners itself).
bleed = f'<rect x="{x0}" y="{y0}" width="{side}" height="{side}" fill="{VIOLET}"/>'
open(f"{OUT}/icon-bleed.svg", "w").write(svg(iview, bleed + paths(g_d, WHITE) + paths(a_d, CORAL), "Growsterr"))

print("wordmark view", [round(v) for v in view], "symbol cut", cut, "icon box", (x0, y0, side), "radius", round(radius, 1))
for f in sorted(os.listdir(OUT)):
    print(f, os.path.getsize(f"{OUT}/{f}"))
