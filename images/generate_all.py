#!/usr/bin/env python3
"""Build every study-guide diagram.

    cd images && python3 generate_all.py

Writes one SVG per diagram next to this script and prints a layout report
(off-canvas or overlapping text is flagged so you can fix coordinates).
"""
import os
import sys
import xml.etree.ElementTree as ET

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import diagrams_networking as dn  # noqa: E402
import diagrams_office_code as doc  # noqa: E402
import diagrams_data_web as ddw  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = HERE

SETS = [
    ('networking', dn.NETWORKING),
    ('office & pseudocode', doc.OFFICE_CODE),
    ('dsa / dbms / sql / frontend', ddw.DATA_WEB),
]

CHAR_W = 0.56


def check(svg_text, name):
    """Return a list of layout warnings: out-of-bounds text and overlapping text."""
    root = ET.fromstring(svg_text)
    w = float(root.get('width'))
    h = float(root.get('height'))
    warns = []
    texts = []
    for t in root.iter('{http://www.w3.org/2000/svg}text'):
        try:
            x = float(t.get('x'))
            y = float(t.get('y'))
        except (TypeError, ValueError):
            continue
        size = float(t.get('font-size', 12))
        s = (t.text or '')
        mono = 'Courier' in (t.get('font-family') or '')
        width = len(s) * size * (0.60 if mono else CHAR_W)
        anchor = t.get('text-anchor', 'start')
        if anchor == 'middle':
            x0, x1 = x - width / 2, x + width / 2
        elif anchor == 'end':
            x0, x1 = x - width, x
        else:
            x0, x1 = x, x + width
        y0, y1 = y - size * 0.85, y + size * 0.25
        if x0 < -2 or x1 > w + 2 or y0 < -2 or y1 > h + 2:
            warns.append(f'    OUT OF BOUNDS: {s[:42]!r}  x[{x0:.0f},{x1:.0f}] '
                         f'y[{y0:.0f},{y1:.0f}] canvas {w:.0f}x{h:.0f}')
        texts.append((x0, y0, x1, y1, s))
    # overlaps
    for i in range(len(texts)):
        for j in range(i + 1, len(texts)):
            a, b = texts[i], texts[j]
            ox = min(a[2], b[2]) - max(a[0], b[0])
            oy = min(a[3], b[3]) - max(a[1], b[1])
            if ox > 6 and oy > 5:
                warns.append(f'    OVERLAP {ox:.0f}x{oy:.0f}px: {a[4][:28]!r} <> {b[4][:28]!r}')
    return warns


def main():
    total, problems = 0, 0
    for section, diagrams in SETS:
        for fname, fn in diagrams:
            svg_text = fn()
            path = os.path.join(OUT, fname + '.svg')
            with open(path, 'w', encoding='utf-8') as fh:
                fh.write(svg_text)
            total += 1
            try:
                warns = check(svg_text, fname)
            except ET.ParseError as exc:
                print(f'  !! INVALID XML: {fname}: {exc}')
                problems += 1
                continue
            if warns:
                problems += 1
                print(f'  ~ {fname}.svg')
                for wline in warns[:8]:
                    print(wline)
    print(f'\n{total} diagrams written, {problems} with layout warnings -> {OUT}')


if __name__ == '__main__':
    main()
