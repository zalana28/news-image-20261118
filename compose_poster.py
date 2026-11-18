#!/usr/bin/env python3
"""Compose the 18 November 2026 world-news poster (1024x1024).

Own work: headlines researched from Reuters / AP / Al Jazeera / MetService
briefings of 18 Nov 2026; hero illustration generated for this entry;
layout and typography composed here with PIL. No copied news photos.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = "/home/hatch/workspace/fonts"
HERO = os.path.join(
    HERE, "assets",
    "media-generation-news-hero-20261118-0-ffdb19c3-a3a7-40b3-8086-70049624236f.png",
)

W, H = 1024, 1024
NAVY = (13, 27, 46)
NAVY2 = (18, 38, 62)
GOLD = (212, 160, 60)
PAPER = (247, 243, 234)
INK = (18, 24, 33)
MUTED = (90, 96, 104)
RULE = (200, 192, 172)
WHITE = (255, 255, 255)

TAG_COLORS = {
    "GULF": (168, 42, 42),
    "APEC": (24, 96, 74),
    "USA": (30, 90, 140),
    "EUROPE": (110, 60, 130),
    "PACIFIC": (58, 74, 140),
    "QUAKE": (176, 92, 12),
}


def font(name, size):
    return ImageFont.truetype(os.path.join(FONTS, name), size)


F_MAST = font("PlusJakartaSans-Bold.ttf", 58)
F_DATE = font("PlusJakartaSans-SemiBold.ttf", 30)
F_TAG = font("PlusJakartaSans-Bold.ttf", 21)
F_HEAD = font("PlusJakartaSans-Bold.ttf", 27)
F_BODY = font("PlusJakartaSans-Regular.ttf", 19)
F_FOOT = font("PlusJakartaSans-Regular.ttf", 17)

STORIES = [
    ("GULF", "Iran hits US bases in Kuwait\nand Bahrain",
     "US jets hit a missile site on Qeshm Island; Iran fired drones at "
     "US radar sites in Kuwait and Bahrain.",
     "Reuters"),
    ("APEC", "Xi opens APEC in Shenzhen,\ndefends free trade",
     "Xi pledges tariff cuts and market opening; Putin denounces "
     "sanctions. Trio meets Thursday.",
     "Reuters"),
    ("USA", "Peltola flips Alaska;\nDemocrats take 56 seats",
     "First Democrat to win an Alaska Senate race since 2008, and the "
     "first Alaska Native in the Senate.",
     "AP / Reuters"),
    ("EUROPE", "Freezer hacks spread to\n11 countries; blood banks hit",
     "The EU promises a collective response as hackers hit stores in "
     "Germany, Romania and the UK.",
     "Al Jazeera"),
    ("PACIFIC", "Category 5 Cyclone Xavier\nbears down on Cook Islands",
     "Winds of 220 km/h near Pukapuka and Nassau; gale warnings in "
     "force as shelters open.",
     "MetService / RNZ"),
    ("QUAKE", "Magnitude 6.0 quake\nstrikes Papua New Guinea",
     "The shallow quake, 10 km deep, struck on Wednesday, German "
     "researchers say.",
     "Reuters / GFZ"),
]


def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def build():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # --- masthead ---
    d.rectangle([0, 0, W, 118], fill=NAVY)
    d.rectangle([0, 118, W, 122], fill=GOLD)
    d.text((48, 22), "THE WORLD IN ONE DAY", font=F_MAST, fill=WHITE)
    d.text((48, 84), "WEDNESDAY  \u00b7  18 NOVEMBER 2026", font=F_DATE, fill=GOLD)

    # --- hero illustration ---
    hero = Image.open(HERO).convert("RGB")
    # cover-crop to 1024x300
    tw, th = 1024, 300
    scale = max(tw / hero.width, th / hero.height)
    hero = hero.resize((int(hero.width * scale) + 1, int(hero.height * scale) + 1),
                       Image.LANCZOS)
    x0 = (hero.width - tw) // 2
    y0 = (hero.height - th) // 2
    hero = hero.crop((x0, y0, x0 + tw, y0 + th))
    img.paste(hero, (0, 122))
    d.rectangle([0, 422, W, 426], fill=GOLD)

    # --- story grid: 2 cols x 3 rows ---
    gx, gy = 48, 448
    cw, ch = 448, 168
    gapx, gapy = 32, 10
    for i, (tag, head, body, src) in enumerate(STORIES):
        col, row = i % 2, i // 2
        x = gx + col * (cw + gapx)
        y = gy + row * (ch + gapy)
        color = TAG_COLORS[tag]
        d.text((x, y), tag, font=F_TAG, fill=color)
        d.line([(x, y + 30), (x + 64, y + 30)], fill=color, width=3)
        yy = y + 42
        for line in head.split("\n"):
            d.text((x, yy), line, font=F_HEAD, fill=INK)
            yy += 32
        for line in wrap(d, body, F_BODY, cw):
            d.text((x, yy), line, font=F_BODY, fill=MUTED)
            yy += 24
        d.text((x, yy + 2), "Source: " + src, font=F_FOOT, fill=(140, 130, 110))
        if col == 0:
            d.line([(x + cw + 16, y + 4), (x + cw + 16, y + ch - 8)], fill=RULE, width=1)

    # --- footer ---
    d.line([(48, 994), (976, 994)], fill=RULE, width=1)
    d.text((48, 1001), "Six stories that defined the day  \u00b7  Headlines as reported 18 Nov 2026",
           font=F_FOOT, fill=MUTED)

    out = os.path.join(HERE, "entry.png")
    img.save(out, "PNG", optimize=True)
    return out


if __name__ == "__main__":
    path = build()
    im = Image.open(path)
    print(path, im.size, os.path.getsize(path), "bytes")
