"""
Planet Clicker Module
=====================
"""

import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
ASSET_DIR = os.path.join(ROOT_DIR, "asset")
SPRITE_SHEET_DIR = (os.path.join(ASSET_DIR, "spritesheet"),)
PATHS = dict(
    root=ROOT_DIR,
    asset=ASSET_DIR,
    sprite_sheet=SPRITE_SHEET_DIR,
)

for k, v in PATHS.items():
    print(f"{k}: {v}")
