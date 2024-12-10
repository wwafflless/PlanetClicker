from asyncio.windows_events import NULL
import math
from re import I, S

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
        self.pos = self.pos
        self.radius = radius * 2
        self.speed = speed
        self.image = planet_images[name]
        
        self.leftSide = False
        self.enabled = False

        self.value = 0
        self.cost = -1
        self.on_orbit = NULL

    def update(self):
        self.pos = rotate_z(self.pos, self.speed * 0.5)
        norm = np.linalg.norm(self.pos)
        size = (1 + self.pos[2] / norm) * 2 * self.radius
        self.rect = pygame.Rect(
            (self.pos[0] - self.radius, self.pos[1] - self.radius),
            (size, size),
        )
        
        if not self.leftSide and self.pos[0] < 0:
            self.leftSide = True
        elif self.leftSide and self.pos[0] > 0:
            if self.on_orbit != NULL:
                self.on_orbit(self, self.value)
            self.leftSide = False

    def draw(self, surface):
        pos = rotate_x(self.pos, 80)
        # pygame.draw.circle(
        #     surface,
        #     (255, 255, 255),
        #     (pos[0] + 400, pos[1] + 300),
        #     self.radius,
        # )
        self.image = pygame.transform.scale(
            self.image,
            (self.radius * 2, self.radius * 2),
        )
        surface.blit(
            self.image,
            (pos[0] + (surface.width/2) - self.radius, pos[1] + (surface.height/3) - self.radius),
        )
