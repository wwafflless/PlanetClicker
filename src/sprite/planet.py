import math

from src.asset.color import Color
from src.asset.font import text_font
import numpy
import numpy as np
import pygame
from numpy import cos, cross, dot, eye, sin

from src.asset import planet_images
from src.data import data
from src.math.rotate import rotate_x, rotate_y, rotate_z


class PlanetSprite(pygame.sprite.Sprite):
    def __init__(self, name, radius, orbit_radius, speed, **kwargs):
        super().__init__()
        self.pos = np.array([orbit_radius * 2, 0, 0])
        self.radius = radius * 2
        self.speed = speed
        self.image = planet_images[name]
        self.name_text = text_font.render(name, False, Color.text)

    def update(self):
        self.pos = rotate_z(self.pos, self.speed * 0.5)
        norm = np.linalg.norm(self.pos)
        size = (1 + self.pos[2] / norm) * 2 * self.radius
        # self.rect = pygame.Rect(
        #     (self.pos[0] - self.radius, self.pos[1] - self.radius),
        #     (size, size),
        # )

    def draw(self, surface):
        pos = rotate_x(self.pos, 80)
        self.image = pygame.transform.scale(
            self.image,
            (self.radius * 2, self.radius * 2),
        )
        center = (
            pos[0] + 400 - self.radius,
            pos[1] + 300 - self.radius,
        )
        surface.blit(self.image, center)
        surface.blit(
            self.name_text, (center[0] + self.radius * 0, center[1] + self.radius * 2.5)
        )
