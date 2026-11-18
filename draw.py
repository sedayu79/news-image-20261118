#!/usr/bin/env python3
"""Draw entry.png: a one-page newspaper infographic summing up
Wednesday 18 November 2026. Pure Pillow, deterministic output.
Run: python3 draw.py  -> writes entry.png next to this file.
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (250, 246, 239)
INK = (20, 20, 20)
GREY = (90, 88, 82)
RED = (176, 42, 30)
RULE = (30, 30, 30)

FONT_DIR = "/usr/share/fonts/truetype/dejavu/"
F_TITLE = ImageFont.truetype(FONT_DIR + "DejaVuSans-Bold.ttf", 54)
F_DATE = ImageFont.truetype(FONT_DIR + "DejaVuSans-Bold.ttf", 40)
F_TAG = ImageFont.truetype(FONT_DIR + "DejaVuSans-Bold.ttf", 22)
F_HEAD = ImageFont.truetype(FONT_DIR + "DejaVuSans-Bold.ttf", 32)
F_BODY = ImageFont.truetype(FONT_DIR + "DejaVuSans.ttf", 26)
F_ALSO = ImageFont.truetype(FONT_DIR + "DejaVuSans.ttf", 24)
F_ALSO_B = ImageFont.truetype(FONT_DIR + "DejaVuSans-Bold.ttf", 24)
F_FOOT = ImageFont.truetype(FONT_DIR + "DejaVuSans.ttf", 20)

TAG_COLORS = {
    "ASIA": (14, 110, 106),
    "EUROPE": (31, 78, 121),
    "MIDDLE EAST": (154, 106, 0),
    "BUSINESS": (46, 107, 46),
    "SPORT": (160, 32, 48),
}

# (tag, headline, one factual line)
STORIES = [
    ("ASIA",
     "Trump lands in Manila for Quad talks",
     "The U.S. president arrives in the Philippines for Quad talks, ahead of his visit to China."),
    ("EUROPE",
     "Ukraine hits Crimean Bridge again",
     "Kyiv strikes the bridge for a second straight day as Russia keeps pounding bridges in Kyiv."),
    ("MIDDLE EAST",
     "Bahrain all-clear after threat alert",
     "Bahrain lifts an overnight potential-threat warning; Kuwait's army says it intercepted drones."),
    ("BUSINESS",
     "Nvidia revenue doubles to $115.84bn",
     "Revenue doubles from a year ago; the board will not reinstate ousted CEO Jensen Huang."),
    ("ASIA",
     "Canada and China extend trade deals",
     "Xi meets Canadian PM Mark Carney to extend trade deals ahead of the APEC summit."),
    ("SPORT",
     "Dhoni retires from the IPL",
     "MS Dhoni ends his IPL playing career and becomes mentor of the Chennai Super Kings."),
]

ALSO = [
    ("Cyclone Akvan", "likely to strengthen over the Bay of Bengal."),
    ("EU plans \u20ac45bn borrowing", "to shore up Ukraine's budget, the FT reports."),
]


def wrap(draw, text, font, max_w):
    words = text.split()
    lines, cur = [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=font) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # --- masthead ---
    title = "THE WORLD IN ONE DAY"
    tw = d.textlength(title, font=F_TITLE)
    d.text(((W - tw) / 2, 22), title, font=F_TITLE, fill=INK)
    date = "WEDNESDAY, 18 NOVEMBER 2026"
    dw = d.textlength(date, font=F_DATE)
    d.text(((W - dw) / 2, 92), date, font=F_DATE, fill=RED)
    d.line([(36, 150), (W - 36, 150)], fill=RED, width=4)
    d.line([(36, 158), (W - 36, 158)], fill=RULE, width=2)

    # --- story grid: 2 columns x 3 rows ---
    mx, gutter, top = 36, 24, 176
    col_w = (W - 2 * mx - gutter) // 2
    row_h, row_gap = 226, 10
    for i, (tag, head, body) in enumerate(STORIES):
        col, row = i % 2, i // 2
        x = mx + col * (col_w + gutter)
        y = top + row * (row_h + row_gap)

        # tag chip
        chip_w = d.textlength(tag, font=F_TAG) + 28
        d.rounded_rectangle([x, y, x + chip_w, y + 34], radius=8,
                            fill=TAG_COLORS[tag])
        d.text((x + 14, y + 4), tag, font=F_TAG, fill=(255, 255, 255))

        # headline, up to 2 lines
        lines = wrap(d, head, F_HEAD, col_w)[:2]
        hy = y + 46
        for line in lines:
            d.text((x, hy), line, font=F_HEAD, fill=INK)
            hy += 36

        # body, up to 3 lines
        blines = wrap(d, body, F_BODY, col_w)[:3]
        by = hy + 4
        for line in blines:
            d.text((x, by), line, font=F_BODY, fill=(52, 52, 48))
            by += 32

        # thin divider under each block except the last row
        if row < 2:
            d.line([(x, y + row_h - 2), (x + col_w, y + row_h - 2)],
                   fill=(200, 194, 182), width=2)

    # --- also today strip ---
    sy = top + 3 * row_h + 2 * row_gap + 12
    d.line([(36, sy), (W - 36, sy)], fill=RULE, width=2)
    label = "ALSO TODAY"
    d.text((36, sy + 10), label, font=F_ALSO_B, fill=RED)
    ay = sy + 42
    for head, tail in ALSO:
        line = wrap(d, "\u2022  " + head + " \u2014 " + tail,
                    F_ALSO, W - 72)[0]
        d.text((36, ay), line, font=F_ALSO, fill=(52, 52, 48))
        ay += 30

    # --- footer ---
    foot = "Events as reported on 18 November 2026  \u2022  One day, in one picture."
    fw = d.textlength(foot, font=F_FOOT)
    d.text(((W - fw) / 2, H - 32), foot, font=F_FOOT, fill=GREY)

    img.save("entry.png", optimize=True)
    print("wrote entry.png", img.size)


if __name__ == "__main__":
    main()
