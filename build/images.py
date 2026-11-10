# -*- coding: utf-8 -*-
import os, glob, json, sys
from PIL import Image, ImageOps
sys.path.insert(0, os.path.dirname(__file__))
from data import PROJECTS, SRC, PORTRAIT

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'img')

def find(folder, n):
    fs = sorted(glob.glob(os.path.join(SRC, folder, '%02d_*' % n)))
    return fs[0]

def save(im, path, long_side, q=82):
    im = ImageOps.exif_transpose(im).convert('RGB')
    w, h = im.size
    s = long_side / max(w, h)
    if s < 1:
        im = im.resize((round(w * s), round(h * s)), Image.LANCZOS)
    im.save(path, 'JPEG', quality=q, optimize=True, progressive=True)
    return im.size

meta = {}
for p in PROJECTS:
    d = os.path.join(OUT, p['slug']); os.makedirs(d, exist_ok=True)
    items = []
    for k, n in enumerate(p['photos']):
        src = find(p['folder'], n)
        im = Image.open(src)
        big = os.path.join(d, '%02d.jpg' % k)
        small = os.path.join(d, '%02d-s.jpg' % k)
        if not os.path.exists(big):
            w, h = save(im, big, 1800)
            save(im, small, 900, 80)
        else:
            w, h = Image.open(big).size
        items.append(dict(i=k, w=w, h=h))
    # обложка: горизонтальная 1920 / 960
    src = find(p['folder'], p['cover'])
    im = Image.open(src)
    save(im, os.path.join(d, 'cover.jpg'), 1920)
    save(im, os.path.join(d, 'cover-m.jpg'), 960, 80)
    meta[p['slug']] = items
    print(p['slug'], len(items))

os.makedirs(os.path.join(OUT, 'buro'), exist_ok=True)
save(Image.open(PORTRAIT), os.path.join(OUT, 'buro', 'elena.jpg'), 1600)
json.dump(meta, open(os.path.join(ROOT, 'build', 'meta.json'), 'w'))
