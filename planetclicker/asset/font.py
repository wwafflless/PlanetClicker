import os
from dataclasses import dataclass
from types import SimpleNamespace

import pygame


def _load_font(font_name, size) -> pygame.font.Font:
    path = os.path.join("asset", "font", "free", font_name)
    print("Loading font: " + path)

    return pygame.font.Font("asset/font/free/" + font_name, size)


class GameFont(SimpleNamespace):
    title: pygame.font.Font = _load_font("ThaleahFat.ttf", 40)
    text: pygame.font.Font = _load_font("ThaleahFat.ttf", 20)
