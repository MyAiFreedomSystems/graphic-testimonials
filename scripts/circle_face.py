#!/usr/bin/env python3
"""Composite a circular client photo onto a square testimonial card.
Usage: circle_face.py <card.png> <face.png>
       [--left 420] [--top 55] [--size 240] [--bg "#1B3A5C"] [--ring "#F1EFE9"]

Face prep: pass an already square-cropped image, or any frame and this crops
center-square (landscape) / 0.9xwidth vertically-centered (portrait) first.
Portraits must be vertically centered, NOT top-biased (top bias cuts foreheads)."""
import argparse
from pathlib import Path
from PIL import Image, ImageDraw

def hex2rgb(h):
    return tuple(int(h[i:i+2], 16) for i in (1, 3, 5))

p = argparse.ArgumentParser()
p.add_argument("card"); p.add_argument("face")
p.add_argument("--left", type=int, default=420)
p.add_argument("--top", type=int, default=55)
p.add_argument("--size", type=int, default=240)
p.add_argument("--bg", default="#1B3A5C", help="disc backing color (match card bg)")
p.add_argument("--ring", default="#F1EFE9", help="ring color")
a = p.parse_args()

face = Image.open(a.face).convert("RGB")
w, h = face.size
if h > w:  # portrait: vertically centered square, slight zoom
    side = int(w * 0.9); left = (w - side) // 2; top = (h - side) // 2
else:      # landscape: center square
    side = h; left = (w - h) // 2; top = 0
ss = a.size * 3  # supersample for smooth edges
face = face.crop((left, top, left + side, top + side)).resize((ss, ss), Image.LANCZOS)

mask = Image.new("L", (ss, ss), 0)
inset = max(2, ss // 90)
ImageDraw.Draw(mask).ellipse((inset, inset, ss - inset, ss - inset), fill=255)
disc = Image.new("RGB", (ss, ss), hex2rgb(a.bg))
disc.paste(face, (0, 0), mask)
ImageDraw.Draw(disc).ellipse((inset, inset, ss - inset, ss - inset),
                             outline=hex2rgb(a.ring), width=max(2, ss // 60))

card = Image.open(a.card).convert("RGB")
card.paste(disc.resize((a.size, a.size), Image.LANCZOS), (a.left, a.top))
card.save(a.card)
print(f"{Path(a.card).name}: face composited at ({a.left},{a.top}) size {a.size}")
