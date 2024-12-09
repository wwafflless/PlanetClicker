from __future__ import annotations
from planetclicker.color import Colors
from pygame.surface import Surface
import pygame
import os

from dataclasses import dataclass
from typing import Self


class Font(pygame.font.Font):
    """A simple font class that uses Pygame's built-in font rendering."""

    def __init__(
        self,
        font_name,
        font_size,
    ):
        self.font_path = os.path.join("asset", "font", f"{font_name}.ttf")
        super(Font, self).__init__(self.font_path, font_size)

    def render(
        self,
        text: str,
        antialias: bool = True,
        color=Colors.debug,
    ) -> Surface:
        """Render a text string onto a new surface."""
        return super().render(text, antialias, color)


TitleFont = Font("ThaleahFat", 64)
TextFont = Font("ThaleahFat", 32)
DebugFont = Font("RobotoMono-Regular", 12)
