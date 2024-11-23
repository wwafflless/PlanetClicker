from __future__ import annotations
import pygame
import math
from pprint import pp
from pygame import Vector2
from font import pixel_font


class Planet(pygame.sprite.Sprite):
    def __init__(self, radius, orbit_radius, speed):
        super().__init__()
        self.image = pygame.image.load("assets/earth.png")
        self.image = pygame.transform.scale(self.image, (radius * 2, radius * 2))
        self.rect = self.image.get_rect()
        self.angle = 0
        self.radius = radius
        self.orbit_radius = orbit_radius
        self.speed = speed

    def update(self):
        self.angle += self.speed
        self.rect.x = (
            400 + self.orbit_radius * math.cos(math.radians(self.angle)) - self.radius
        )
        self.rect.y = (
            300 + self.orbit_radius * math.sin(math.radians(self.angle)) - self.radius
        )
