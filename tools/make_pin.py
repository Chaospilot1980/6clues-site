"""Make a 1000x1500 Pinterest pin: background image (cover/scene), dark band, kicker, title, footer.
usage: make_pin.py <bg.jpg> <out.jpg> <kicker> <title> [footer]"""
import sys, textwrap
from PIL import Image, ImageDraw, ImageFont, ImageFilter
F = '/tmp/fonts/'
bg, out, kicker, title = sys.argv[1:5]
footer = sys.argv[5] if len(sys.argv) > 5 else 'Free to play · 6clues.com'
W, H = 1000, 1500
im = Image.open(bg).convert('RGB'); w, h = im.size
s = max(W / w, H / h); im = im.resize((int(w * s) + 1, int(h * s) + 1), Image.LANCZOS)
w, h = im.size; im = im.crop(((w - W) // 2, (h - H) // 2, (w - W) // 2 + W, (h - H) // 2 + H))
ov = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(ov)
for y in range(H):  # gradient bottom
    a = max(0, min(235, int((y - 650) / 850 * 300))) if y > 650 else 0
    d.line([(0, y), (W, y)], fill=(18, 14, 12, a))
im = Image.alpha_composite(im.convert('RGBA'), ov).convert('RGB'); d = ImageDraw.Draw(im)
fk = ImageFont.truetype(F + 'inter-latin-700-normal.ttf', 34)
ft = ImageFont.truetype(F + 'special-elite-latin-400-normal.ttf', 88)
ff = ImageFont.truetype(F + 'inter-latin-700-normal.ttf', 36)
lines = textwrap.wrap(title, 16)
y = H - 150 - 100 * len(lines) - 70
d.text((70, y), kicker.upper(), font=fk, fill=(232, 90, 80)); y += 70
for ln in lines: d.text((70, y), ln, font=ft, fill=(243, 238, 228)); y += 100
d.rectangle([70, H - 130, 120, H - 124], fill=(232, 90, 80))
d.text((70, H - 110), footer, font=ff, fill=(243, 238, 228))
im.save(out, 'JPEG', quality=82, optimize=True, progressive=True)
