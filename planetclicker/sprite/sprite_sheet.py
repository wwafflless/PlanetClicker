import os
from dataclasses import dataclass

import pygame


class SpriteSheet:
    """Stores multiple images within a single sheet."""

    @dataclass
    class SubRect:
        x: int
        y: int
        w: int
        h: int

    def __init__(self, name: str, ext: str, w: int, h: int):
        self.name = name
        self.ext = ext
        self.path = os.path.join("asset", "sheet", f"{name}.{ext}")
        self.sheet = pygame.image.load(self.path)  # .convert()
        self.rect = pygame.Rect(0, 0, w, h)

    def image_at(self, subrect: pygame.Rect, colorkey=None):
        """Load a specific image from a specific rectangle."""
        image = pygame.Surface(subrect.size)  # .convert()
        image.blit(self.sheet, (0, 0), subrect)
        return image

    def images_at(self, subrects: list[pygame.Rect], colorkey=None):
        """Load a whole bunch of images and return them as a list."""
        return [self.image_at(subrect, colorkey) for subrect in subrects]

    def load_strip(self, rect: pygame.Rect, image_count: int, colorkey=None):
        """Load a whole strip of images, and return them as a list."""
        rects = [
            pygame.Rect(rect[0] + x * rect[2], rect[1], rect[2], rect[3])
            for x in range(image_count)
        ]
        return self.images_at(rects, colorkey)
