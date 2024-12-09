from __future__ import annotations
from pygame.surface import Surface
import pygame
import os

from dataclasses import dataclass
from typing import Self


@dataclass
class Font:
    font: pygame.font.Font
    _size: int = 12

    @classmethod
    def load(cls, name: str):
        font_path = os.path.join("asset", "font", f"{name}.ttf")
        font = pygame.font.Font(font_path)
        return cls(font)

    def size(self, size: int) -> Font:
        self._size = size
        return self

    def render(self, *args, **kwargs) -> Surface:
        return self.font.render(*args, **kwargs)


TitleFont = Font.load("ThaleahFat").size(20)
TextFont = Font.load("ThaleahFat").size(12)
