import os

import pygame


def _load_font(font_name, size):
    path = os.path.join(os.getcwd(), "assets", font_name)
    return pygame.font.Font(path, size)


title_font = _load_font("ThaleahFat.ttf", 64)
text_font = _load_font("ThaleahFat.ttf", 16)
