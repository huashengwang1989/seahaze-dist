"""Draws the SEA Haze disk image background: a soft hazy dawn behind the app icon,
haze bands like the icon's, and an arrow to the Applications folder.

Writes background.png (640x428) and background@2x.png (1280x856) next to this script. The bottom
28 pt stay plain: Finder may cover them with the path / status bar.
Icon centres for create-dmg: app (170, 185), Applications (470, 185), icon size 128.
"""
import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

W, H = 640, 428
APP, APPS = (170, 185), (470, 185)
OUT = Path(__file__).parent
FONT = "/System/Library/Fonts/SFNS.ttf"
NAVY = (36, 48, 78)


def lerp(a, b, t):
    return tuple(round(x + (y - x) * t) for x, y in zip(a, b))


def font(size, weight):
    f = ImageFont.truetype(FONT, size)
    f.set_variation_by_name(weight)
    return f


def draw(scale):
    w, h = W * scale, H * scale
    s = lambda v: round(v * scale)  # noqa: E731

    # Sky: warm peach at the top fading to a pale lavender haze
    top, mid, bottom = (255, 232, 214), (247, 236, 238), (232, 234, 244)
    sky = Image.new("RGB", (1, h))
    for y in range(h):
        t = y / (h - 1)
        sky.putpixel((0, y), lerp(top, mid, t / 0.55) if t < 0.55 else lerp(mid, bottom, (t - 0.55) / 0.45))
    img = sky.resize((w, h)).convert("RGBA")

    # Sun glow behind the app icon
    glow = Image.new("RGBA", (w, h), (255, 176, 110, 0))
    g = ImageDraw.Draw(glow)
    for r, a in ((160, 55), (110, 80), (72, 95)):
        g.ellipse([s(APP[0] - r), s(APP[1] - 20 - r), s(APP[0] + r), s(APP[1] - 20 + r)], fill=(255, 176, 110, a))
    img.alpha_composite(glow.filter(ImageFilter.GaussianBlur(s(40))))

    # Drifting haze bands, like the waves in the icon
    haze = Image.new("RGBA", (w, h), (255, 255, 255, 0))
    hz = ImageDraw.Draw(haze)
    for y0, amp, alpha, phase in ((290, 6, 150, 0.0), (316, 5, 120, 1.7), (340, 4, 95, 3.1), (92, 5, 90, 0.8)):
        pts = [(x, s(y0 + amp * math.sin(x / s(70) + phase))) for x in range(0, w + 1, max(1, s(4)))]
        hz.line(pts, fill=(255, 255, 255, alpha), width=s(16), joint="curve")
    img.alpha_composite(haze.filter(ImageFilter.GaussianBlur(s(7))))

    # Arrow and text on their own layer so their transparency blends with the sky
    marks = Image.new("RGBA", (w, h), NAVY + (0,))
    d = ImageDraw.Draw(marks)

    # Curved dashed arrow from the app to Applications
    x0, x1, y_base, lift = APP[0] + 88, APPS[0] - 96, APP[1] - 6, 32
    pts = []
    steps = 60
    for i in range(steps + 1):
        t = i / steps
        pts.append((x0 + (x1 - x0) * t, y_base - lift * 4 * t * (1 - t)))
    color = NAVY + (150,)
    for i in range(0, steps - 2, 4):  # dashes
        seg = [(s(px), s(py)) for px, py in pts[i:i + 3]]
        d.line(seg, fill=color, width=s(2.6), joint="curve")
    ex, ey = pts[-1]
    px, py = pts[-4]
    ang = math.atan2(ey - py, ex - px)
    head = [(ex + 4 * math.cos(ang), ey + 4 * math.sin(ang))]
    for da in (2.55, -2.55):
        head.append((ex + 12 * math.cos(ang + da), ey + 12 * math.sin(ang + da)))
    d.polygon([(s(x), s(y)) for x, y in head], fill=color)

    # Title and caption
    title = font(s(15), "Semibold")
    d.text((s(W / 2), s(38)), "SEA Haze", font=title, fill=NAVY + (210,), anchor="mm")
    caption = font(s(13), "Medium")
    d.text((s(W / 2), s(372)), "Drag SEA Haze to Applications to install", font=caption, fill=NAVY + (190,), anchor="mm")
    img.alpha_composite(marks)
    return img.convert("RGB")


if __name__ == "__main__":
    draw(1).save(OUT / "background.png")
    draw(2).save(OUT / "background@2x.png")
    print("written to", OUT)
