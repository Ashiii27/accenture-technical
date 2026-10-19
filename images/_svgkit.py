"""Tiny helper library for drawing the study-guide diagrams as clean SVG files.

Everything is plain shapes + text so the SVGs stay small, readable and
version-controllable (no external fonts, no scripts, no raster assets).
"""
from xml.sax.saxutils import escape

# ---------------------------------------------------------------- palette ----
INK = '#111827'        # primary text
MUTED = '#6b7280'      # secondary text
LINE = '#94a3b8'       # arrows / borders
BG = '#ffffff'

BLUE = '#4f46e5'
BLUE_L = '#eef2ff'
TEAL = '#0d9488'
TEAL_L = '#ecfdf5'
AMBER = '#d97706'
AMBER_L = '#fffbeb'
RED = '#dc2626'
RED_L = '#fef2f2'
SLATE = '#475569'
SLATE_L = '#f1f5f9'
GREEN = '#16a34a'
GREEN_L = '#f0fdf4'
PURPLE = '#7c3aed'
PURPLE_L = '#f5f3ff'

SANS = 'Helvetica, Arial, sans-serif'
MONO = 'Courier New, Courier, monospace'

_CHAR_W = 0.56  # rough Helvetica advance width factor, used for auto-sizing boxes


def tw(s, size, mono=False):
    """Rough rendered width of a string, for layout maths only."""
    return len(s) * size * (0.60 if mono else _CHAR_W)


def esc(s):
    return escape(str(s))


# --------------------------------------------------------------- primitives --
def txt(x, y, s, size=12, fill=INK, anchor='start', weight='normal', mono=False,
        opacity=None, style=''):
    """A single text line. `anchor` = start | middle | end."""
    fam = MONO if mono else SANS
    op = f' opacity="{opacity}"' if opacity else ''
    extra = f' font-style="italic"' if style == 'italic' else ''
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-family="{fam}" font-size="{size}" '
            f'fill="{fill}" text-anchor="{anchor}" font-weight="{weight}"{op}{extra}>'
            f'{esc(s)}</text>')


def box(x, y, w, h, label=None, fill=BLUE_L, stroke=BLUE, lw=1.2, rx=7,
        fs=11.5, tfill=INK, weight='normal', mono=False, dashed=False, opacity=None):
    """Rounded rectangle, optionally centred-labelled."""
    dash = ' stroke-dasharray="5 3"' if dashed else ''
    op = f' opacity="{opacity}"' if opacity else ''
    out = [f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" '
           f'fill="{fill}" stroke="{stroke}" stroke-width="{lw}"{dash}{op}/>']
    if label is not None:
        out.append(txt(x + w / 2, y + h / 2 + fs * 0.36, label, size=fs, fill=tfill,
                       anchor='middle', weight=weight, mono=mono))
    return '\n'.join(out)


def line(x1, y1, x2, y2, stroke=LINE, lw=1.2, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return (f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
            f'stroke="{stroke}" stroke-width="{lw}"{d}/>')


def arrow(x1, y1, x2, y2, stroke=SLATE, lw=1.4, head=7, dash=None,
          label=None, lsize=9.5, lfill=MUTED, loff=6, lanchor='middle', mono=False):
    """Straight arrow (x1,y1) -> (x2,y2) with an optional label above the shaft."""
    import math
    ang = math.atan2(y2 - y1, x2 - x1)
    a = math.radians(150)
    p1 = (x2 + head * math.cos(ang + a), y2 + head * math.sin(ang + a))
    p2 = (x2 + head * math.cos(ang - a), y2 + head * math.sin(ang - a))
    d = f' stroke-dasharray="{dash}"' if dash else ''
    out = [f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
           f'stroke="{stroke}" stroke-width="{lw}"{d}/>',
           (f'<path d="M {x2:.1f},{y2:.1f} L {p1[0]:.1f},{p1[1]:.1f} '
            f'L {p2[0]:.1f},{p2[1]:.1f} Z" fill="{stroke}"/>')]
    if label is not None:
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        # nudge the label perpendicular to the shaft
        import math as m
        nx, ny = -m.sin(ang), m.cos(ang)
        lx, ly = mx + nx * loff, my + ny * loff - lsize * 0.2
        if abs(ny) < 0.5:  # mostly vertical shaft -> put label beside it
            lx = mx + loff + (tw(label, lsize, mono) / 2 if lanchor == 'start' else 0)
            ly = my + lsize * 0.35
        out.append(txt(lx, ly, label, size=lsize, fill=lfill, anchor=lanchor, mono=mono))
    return '\n'.join(out)


def elbow(x1, y1, x2, y2, stroke=SLATE, lw=1.4, head=7, axis='h', dash=None,
          label=None, lsize=9.5, lfill=MUTED):
    """Right-angled connector: axis 'h' = go horizontal first, 'v' = vertical first."""
    if axis == 'h':
        cx, cy = x2, y1
    else:
        cx, cy = x1, y2
    return '\n'.join([
        line(x1, y1, cx, cy, stroke, lw, dash),
        arrow(cx, cy, x2, y2, stroke, lw, head, dash, label, lsize, lfill),
    ])


def title(x, y, s, size=15, fill=INK, sub=None, ssize=10.5):
    out = [txt(x, y, s, size=size, fill=fill, weight='bold')]
    if sub:
        out.append(txt(x, y + size + 4, sub, size=ssize, fill=MUTED))
    return '\n'.join(out)


def note(x, y, s, size=10, fill=MUTED, anchor='start', mono=False, weight='normal'):
    return txt(x, y, s, size=size, fill=fill, anchor=anchor, mono=mono, weight=weight)


def wrap(x, y, s, maxw=700, size=10, lh=None, fill=MUTED, mono=False, weight='normal'):
    """Same as note() but automatically wraps long strings onto several lines."""
    lh = lh or size * 1.5
    words, lines, cur = str(s).split(), [], ''
    for wd in words:
        trial = (cur + ' ' + wd).strip()
        if cur and tw(trial, size, mono) > maxw:
            lines.append(cur)
            cur = wd
        else:
            cur = trial
    lines.append(cur)
    return '\n'.join(txt(x, y + i * lh, ln, size=size, fill=fill, mono=mono, weight=weight)
                     for i, ln in enumerate(lines))


def pill(x, y, s, fill=BLUE_L, stroke=BLUE, tfill=INK, fs=10.5, padx=8, h=20, mono=False):
    w = tw(s, fs, mono) + padx * 2
    return ('\n'.join([box(x, y, w, h, fill=fill, stroke=stroke, rx=h / 2, lw=1),
                       txt(x + w / 2, y + h / 2 + fs * 0.36, s, size=fs, fill=tfill,
                           anchor='middle', mono=mono)]), w)


def tag(x, y, w, h, s, fill=SLATE_L, stroke=LINE, tfill=SLATE, fs=10, mono=False):
    """Small label chip used for legend/annotation."""
    return '\n'.join([box(x, y, w, h, fill=fill, stroke=stroke, rx=4, lw=1),
                      txt(x + w / 2, y + h / 2 + fs * 0.36, s, size=fs, fill=tfill,
                          anchor='middle', mono=mono)])


def canvas(w, h, body, bg=BG, border=True):
    """Wrap body parts in an <svg> root."""
    parts = [f'<rect x="0" y="0" width="{w}" height="{h}" fill="{bg}"/>']
    if border:
        parts.append(f'<rect x="0.5" y="0.5" width="{w-1}" height="{h-1}" fill="none" '
                     f'stroke="#e2e8f0" stroke-width="1"/>')
    parts.append('\n'.join(p for p in body if p))
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
            f'viewBox="0 0 {w} {h}" font-family="{SANS}">\n'
            + '\n'.join(parts) + '\n</svg>\n')


def write(path, svg_text):
    with open(path, 'w', encoding='utf-8') as fh:
        fh.write(svg_text)
