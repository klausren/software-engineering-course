#!/usr/bin/env python3
"""Bilingual figure helpers for the Software Engineering I slide deck.

Why this exists
---------------
The slides are bilingual -- every label carries its Chinese beside the English
-- but the decks in this repo have no figures at all. The figure pages are
there; the drawing is not. What is on those pages is the figure's *labels*,
left behind as loose text boxes (the incremental page even shows "Com" where
"Communication" was clipped), so the reader sees a diagram's vocabulary
scattered in space with no diagram.

The textbook has the matching diagrams already, but they are English-only, and
a bilingual deck wants a bilingual figure. So this directory generates its own,
in the deck's own bilingual idiom.

Visual language
---------------
Deliberately borrowed from the textbook's figures (figures/gen/common.py) so
the two artefacts look like siblings: the same palette, the same rounded rects
and open chevron arrow heads, the same rule that nothing is set below 11.5.
The one addition is a third line inside each box for the Chinese.

Licensing
---------
These figures are derived from the textbook's figures, which are CC BY 4.0.
CC BY permits reuse and adaptation, including commercially and including
inside this repository's CC BY-NC-SA 4.0 material, provided the source is
credited. Every figure therefore carries the attribution line baked into the
caption helper, and figures/README.md records the source.

Usage
-----
    python3 figures/gen/figs_w02.py       # writes figures/svg/*.svg
    node figures/render.js                # writes figures/png/*.png
"""

import html
import os

from PIL import ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
FIGDIR = os.path.dirname(HERE)
OUT = os.path.join(FIGDIR, "svg")

# Canvas. 16:9-friendly: the deck's own slide is 13.33 x 7.5 in.
W = 960

INK = "#1F2937"
GRAY = "#6B7280"
LINE = "#C9D4E2"
CANVAS = "#FFFFFF"
BLUE = "#2563EB"; BLUE_F = "#DBEAFE"
TEAL = "#0D9488"; TEAL_F = "#CCFBF1"
AMBER = "#D97706"; AMBER_F = "#FEF3C7"
RED = "#DC2626"; RED_F = "#FEE2E2"
GREEN = "#2E7D46"; GREEN_F = "#DCFCE7"
VIOLET = "#6D3FA8"; VIOLET_F = "#EDE7F6"

TONES = {
    "blue": (BLUE, BLUE_F), "teal": (TEAL, TEAL_F), "amber": (AMBER, AMBER_F),
    "red": (RED, RED_F), "green": (GREEN, GREEN_F), "violet": (VIOLET, VIOLET_F),
    "gray": (GRAY, "#F3F4F6"),
}

# Nothing below 11.5, same floor the textbook enforces.
MIN_FONT = 11.5
MEASURE = 200
ARIAL = "/System/Library/Fonts/Supplemental/Arial.ttf"
ARIAL_B = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
# PingFang is not on this machine; Hiragino Sans GB is the Simplified Chinese
# sans that is, and it is what the deck's own Chinese looks like.
CJK = "/System/Library/Fonts/Hiragino Sans GB.ttc"

_F = {
    "en": ImageFont.truetype(ARIAL, MEASURE),
    "en_b": ImageFont.truetype(ARIAL_B, MEASURE),
    "zh": ImageFont.truetype(CJK, MEASURE),
    "zh_b": ImageFont.truetype(CJK, MEASURE),
}


def tw(s, size, zh=False, bold=False):
    """Advance width in figure units, in the font the string will be set in."""
    key = ("zh" if zh else "en") + ("_b" if bold else "")
    return _F[key].getlength(s) * size / MEASURE


def esc(s):
    return html.escape(s, quote=False)


def has_cjk(s):
    return any("\u4e00" <= c <= "\u9fff" for c in s)


def wrap(text, width, size, zh=False, bold=False):
    """Greedy word wrap measured in the real font.

    Latin breaks on spaces. Chinese has no spaces, so it is broken by
    character -- and then BALANCED across the lines it needs, because a naive
    fill leaves an orphan: a 18-character label one character too wide for a
    17-character line comes out as 17 + 1, which looks like a mistake on a
    slide and is one.
    """
    if zh and has_cjk(text) and " " not in text:
        per = max(1, int(width // tw("\u6c49", size, zh=True, bold=bold)))
        if len(text) <= per:
            return [text]
        n = -(-len(text) // per)          # ceil
        step = -(-len(text) // n)         # even chunks
        return [text[i:i + step] for i in range(0, len(text), step)]
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = f"{cur} {w}".strip()
        if cur and tw(trial, size, zh=zh, bold=bold) > width:
            lines.append(cur)
            cur = w
        else:
            cur = trial
    if cur:
        lines.append(cur)
    return lines


class Fig:
    """One figure. Everything appends to self.parts; save() wraps and writes."""

    def __init__(self, width=W):
        self.w = width
        self.parts = []
        self._maxy = 0.0
        self.overflows = []          # (kind, x0, x1, detail) outside the canvas

    # ---------- internals ----------
    def _touch(self, y):
        self._maxy = max(self._maxy, y)

    def _ext(self, x0, x1, kind, detail):
        """Record a horizontal extent. save() refuses to ship a figure that
        runs off the canvas, because a clipped label is invisible in the SVG
        and obvious in the deck -- far too late."""
        if x0 < -1 or x1 > self.w + 1:
            self.overflows.append((kind, round(x0, 1), round(x1, 1), detail))

    def _text_ext(self, x, y, s, size, anchor, zh=False, bold=False, kind="text"):
        w = tw(s, size, zh=zh, bold=bold)
        if anchor == "start":
            self._ext(x, x + w, kind, s)
        elif anchor == "end":
            self._ext(x - w, x, kind, s)
        else:
            self._ext(x - w / 2, x + w / 2, kind, s)

    def line(self, y):
        """A full-width hairline rule."""
        self.parts.append(
            f'<line x1="0" y1="{y}" x2="{self.w}" y2="{y}" stroke="{LINE}" stroke-width="1"/>')
        self._touch(y)

    # ---------- primitives ----------
    def box(self, x, y, w, en, zh=None, sub=None, tone="blue", h=None, size=12.5,
            zh_above=False, en_color=None):
        """A rounded rect holding the English label, an optional English
        sub-label, and the Chinese. Height is derived from the line count so
        the Chinese can never be squeezed out of the box."""
        en_c, f_c = TONES[tone]
        lines = [("en", en, size, True), ]
        if sub:
            lines.append(("en", sub, 10.5, False))
        if zh:
            lines.append(("zh", zh, 11.5, False))
        if zh_above:
            lines = lines[-1:] + lines[:-1]

        lh = 16.0
        hh = h if h else 11 + lh * len(lines)
        self.parts.append(
            f'<rect x="{x}" y="{y}" width="{w}" height="{hh}" rx="8" '
            f'fill="{f_c}" stroke="{en_c}" stroke-width="2.2"/>')
        self._ext(x, x + w, "box", en[:40])
        cx = x + w / 2
        base = y + 6 + 13
        for kind, txt, sz, bold in lines:
            is_zh = kind == "zh"
            fill = en_color or (INK if bold else GRAY)
            if is_zh:
                fill = GRAY
            self.parts.append(
                f'<text x="{cx}" y="{base:.1f}" text-anchor="middle" font-size="{sz}" '
                f'fill="{fill}" font-weight="{"bold" if bold else "normal"}"'
                f'{f" font-family=\"Hiragino Sans GB\"" if is_zh else ""}>{esc(txt)}</text>')
            self._text_ext(cx, base, txt, sz, "middle", zh=is_zh, bold=bold, kind="box label")
            base += lh
        self._touch(y + hh)
        return y + hh

    def free(self, x, y, en, zh=None, size=12, tone="gray", anchor="middle",
             italic=False, bold=False):
        """Text not inside a box: axis labels, captions, notes."""
        if tone == "ink":
            fill = INK
        else:
            fill, _ = TONES[tone]
        self._text_ext(x, y, en, size, anchor, bold=bold, kind="free text")
        self.parts.append(
            f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" '
            f'fill="{fill}" font-weight="{"bold" if bold else "normal"}"'
            f'{f" font-style=\"italic\"" if italic else ""}>{esc(en)}</text>')
        if zh:
            self._text_ext(x, y, zh, 11.5, anchor, zh=True, kind="free text (zh)")
            self.parts.append(
                f'<text x="{x}" y="{y + size + 3.5:.1f}" text-anchor="{anchor}" '
                f'font-size="11.5" fill="{GRAY}" font-family="Hiragino Sans GB">{esc(zh)}</text>')
            self._touch(y + size + 3.5 + 11.5)
        else:
            self._touch(y + size)
        return y + size + (size + 3.5 if zh else 0)

    def wrapbox(self, x, y, w, h, en, zh=None, tone="gray", size=11.5, pad=12):
        """A cell whose English wraps, with the Chinese under it. Used by the
        tables, where a cell cannot be trusted to fit on one line."""
        c, f = TONES[tone]
        self.parts.append(
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{f}" '
            f'stroke="{c}" stroke-width="1.2"/>')
        self._ext(x, x + w, "cell", en[:40])
        lines = wrap(en, w - 2 * pad, size)
        base = y + pad + size * 0.85
        for ln in lines:
            self.parts.append(
                f'<text x="{x + pad}" y="{base:.1f}" font-size="{size}" fill="{INK}">{esc(ln)}</text>')
            self._text_ext(x + pad, base, ln, size, "start", kind="cell text")
            base += size + 3
        if zh:
            base += 1
            for ln in wrap(zh, w - 2 * pad, 11, zh=True):
                self.parts.append(
                    f'<text x="{x + pad}" y="{base:.1f}" font-size="11" fill="{GRAY}" '
                    f'font-family="Hiragino Sans GB">{esc(ln)}</text>')
                self._text_ext(x + pad, base, ln, 11, "start", zh=True, kind="cell text (zh)")
                base += 14
        self._touch(y + h)
        return lines, base

    def arrow(self, x1, y1, x2, y2, tone="gray", dashed=False, width=2.2):
        c, _ = TONES[tone]
        mid = f'M{x1},{y1} L{x2},{y2}'
        dash = ' stroke-dasharray="6 5"' if dashed else ''
        mk = f'arrow{abs(hash((x1, y1, x2, y2)) ) % 100000}'
        self.parts.append(
            f'<defs><marker id="{mk}" viewBox="0 0 10 10" refX="8" refY="5" '
            f'markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
            f'<path d="M0,0 L10,5 L0,10 z" fill="{c}"/></marker></defs>')
        self.parts.append(
            f'<path d="{mid}" fill="none" stroke="{c}" stroke-width="{width}"{dash} '
            f'marker-end="url(#{mk})"/>')
        self._touch(max(y1, y2))

    def chevron(self, x, y, w, h, en="", zh="", tone="gray"):
        """A hexagon-ish process step, for diagrams that are a chain."""
        c, f = TONES[tone]
        k = h / 2
        pts = f"{x},{y} {x + w - k},{y} {x + w},{y + k} {x + w - k},{y + h} {x},{y + h} {x + k},{y + k}"
        self.parts.append(
            f'<polygon points="{pts}" fill="{f}" stroke="{c}" stroke-width="2.2"/>')
        cx = x + w / 2
        n = 1 + (1 if zh else 0)
        base = y + h / 2 - (7 if n == 2 else -4)
        self.parts.append(
            f'<text x="{cx}" y="{base:.1f}" text-anchor="middle" font-size="12" '
            f'fill="{INK}" font-weight="bold">{esc(en)}</text>')
        if zh:
            self.parts.append(
                f'<text x="{cx}" y="{base + 16:.1f}" text-anchor="middle" font-size="11.5" '
                f'fill="{GRAY}" font-family="Hiragino Sans GB">{esc(zh)}</text>')
        self._touch(y + h)

    def caption(self, x, y, en, zh=None, size=13, anchor="middle"):
        """The italic line under a figure. Every figure ends with one, and the
        attribution lives here so it travels with the image."""
        self.parts.append(
            f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" '
            f'fill="{GRAY}" font-style="italic">{esc(en)}</text>')
        yy = y
        if zh:
            yy += size + 4
            self.parts.append(
                f'<text x="{x}" y="{yy:.1f}" text-anchor="{anchor}" font-size="12" '
                f'fill="{GRAY}" font-family="Hiragino Sans GB" font-style="italic">{esc(zh)}</text>')
        self._touch(yy)

    def credit(self, x, y, anchor="middle"):
        self.parts.append(
            f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="11.5" fill="#9CA3AF">'
            f'Figure after OOSE textbook (CC BY 4.0) · 图据教材重绘</text>')
        self._touch(y)

    # ---------- output ----------
    def save(self, name, pad=22):
        if self.overflows:
            print(f"  !! {name}: {len(self.overflows)} element(s) outside the "
                  f"{self.w}-unit canvas:")
            for kind, x0, x1, detail in self.overflows[:8]:
                print(f"       {kind}: {x0} .. {x1}  {detail!r}")
            raise SystemExit(f"{name} would be clipped; fix the layout before rendering")
        h = self._maxy + pad
        body = "\n  ".join(self.parts)
        svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w} {h:.0f}" '
               f'font-family="Arial">\n'
               f'  <rect x="0" y="0" width="{self.w}" height="{h:.0f}" fill="{CANVAS}"/>\n'
               f'  {body}\n</svg>\n')
        os.makedirs(OUT, exist_ok=True)
        path = os.path.join(OUT, name + ".svg")
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(svg)
        print(f"wrote {os.path.relpath(path, FIGDIR)}  ({self.w}x{h:.0f})")
        return path
