from __future__ import annotations

import os
from dataclasses import dataclass
import os
from enum import Enum, StrEnum
from types import SimpleNamespace

import pygame
from pygame.surface import Surface

from planetclicker.color import Colors


class Font(pygame.font.Font):
    """A simple font class that uses Pygame's built-in font rendering."""

    def __init__(self, font_name: str, font_size=12):
        font_path = os.path.join("asset", "font", f"{font_name}.ttf")
        super(Font, self).__init__(filename=font_path, size=font_size)

    def render(
        self,
        text: str,
        antialias=False,
        color=Colors.text,
    ) -> Surface:
        return super(Font, self).render(text, False, color)


TitleFont = Font(
    FontEnum.thaleah_fat,
    64,
)
TextFont = Font(
    FontEnum.pixelated_elegance,
    16,
)
DebugFont = Font(
    FontEnum.roboto,
    12,
)
