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
        font_path = os.path.join("assets", "font", f"{font_name}.ttf")
        super().__init__(filename=font_path, size=font_size)
        # super(pygame.font, self).__init__(filename=font_path)

    def render(
        self,
        text: str,
        antialias=False,
        color=Colors.text,
    ) -> Surface:
        return super().render(text, False, color)


class FontEnum(StrEnum):
    jersey25 = "Jersey25-Regular"
    pixelated_elegance = "PixelatedElegance"
    pixelify_sans = "PixelifySans-Regular"
    roboto = "RobotoMono-Regular"
    space_quest = "SpaceQuest"
    thaleah_fat = "ThaleahFat"


TitleFont = Font(
    font_name=FontEnum.thaleah_fat.value,
    font_size=64,
)
TextFont = Font(
    FontEnum.pixelated_elegance,
    16,
)
DebugFont = Font(
    FontEnum.roboto,
    12,
)
