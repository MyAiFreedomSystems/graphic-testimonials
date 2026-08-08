#!/usr/bin/env python3
"""Recolor flat card backgrounds to a target brand color.
Detects background from 10px corner patches, blends proportionally
(w = clip((90-dist)/60)) so anti-aliased text edges survive.
Usage: recolor_bg.py <png> [<png>...] [--target "#1B3A5C"]"""
import argparse
from pathlib import Path
import numpy as np
from PIL import Image

p = argparse.ArgumentParser()
p.add_argument("pngs", nargs="+")
p.add_argument("--target", default="#1B3A5C", help="hex color for the new background")
a = p.parse_args()
TARGET = np.array([int(a.target[i:i+2], 16) for i in (1, 3, 5)], dtype=float)

def recolor(path: Path):
    img = Image.open(path).convert("RGB")
    arr = np.asarray(img).astype(float)
    corners = np.concatenate([
        arr[:10, :10].reshape(-1, 3), arr[:10, -10:].reshape(-1, 3),
        arr[-10:, :10].reshape(-1, 3), arr[-10:, -10:].reshape(-1, 3),
    ])
    bg = np.median(corners, axis=0)
    dist = np.linalg.norm(arr - bg, axis=2)
    w = np.clip((90.0 - dist) / 60.0, 0.0, 1.0)
    out = arr * (1 - w[..., None]) + TARGET * w[..., None]
    Image.fromarray(out.astype(np.uint8)).save(path)
    print(f"{path.name}: bg {bg.astype(int)} -> {TARGET.astype(int)}, recolored {(w > 0.5).mean()*100:.1f}%")

for arg in a.pngs:
    recolor(Path(arg))
