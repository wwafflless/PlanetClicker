from __future__ import annotations

import numpy as np
import pygame
from pygame.sprite import Sprite

from planetclicker.data import Game
from planetclicker.math import rotate_x, rotate_z


class PlanetSprite(pygame.sprite.Sprite):
    def __init__(self, name, radius, orbit_radius, speed, **kwargs):
        super().__init__()
        self.pos = np.array([orbit_radius * 2, 0, 0])
        self.radius = radius * 2
        self.speed = speed
        self.image = Sprite().image  # TODO FIXME
        self.name_text = Game.Font.text.render(name, False, GameColor.text)

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
        # self.image = pygame.transform.scale(
        #     self.image.sur,
        #     (self.radius * 2, self.radius * 2),
        # )
        center = (
            pos[0] + 400 - self.radius,
            pos[1] + 300 - self.radius,
        )
        surface.blit(self.image, center)
        surface.blit(
            self.name_text, (center[0] + self.radius * 0, center[1] + self.radius * 2.5)
        )
