import pygame
import math
from src.asset import planet_images
from src.data import data


class Planet(pygame.sprite.Sprite):
    def __init__(self, name, radius, orbit_radius, speed, **kwargs):
        super().__init__()
        self.name = name
        self.image = planet_images[name]
        self.image = pygame.transform.scale(self.image, (radius * 2, radius * 2))
        self.rect = self.image.get_rect()
        self.angle = 0
        self.radius = radius
        self.orbit_radius = orbit_radius
        self.speed = speed

    @property
    def dignity(self):
        if zodiac_data := data["zodiac"].get(self.zodiac):
            return filter(
                lambda dgnty: self.name == zodiac_data.get(dgnty),
                ["ruler", "exalted", "detriment", "fall"],
            )
        return []

    @property
    def zodiac(self):
        signs = list(data["zodiac"].keys())
        for i in range(len(signs)):
            if self.angle >= i * 30 and self.angle < (i + 1) * 30:
                return signs[i]

    def update(self):
        self.angle += self.speed
        self.angle = self.angle % 360
        self.rect.x = (
            400 + self.orbit_radius * math.cos(math.radians(self.angle)) - self.radius
        )
        self.rect.y = (
            300 + self.orbit_radius * math.sin(math.radians(self.angle)) - self.radius
        )
