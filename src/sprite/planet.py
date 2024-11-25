import math

from src.math.rotate import rotate_z
import numpy as np
import numpy
import pygame
from numpy import cos, cross, dot, eye, sin
from src.asset import planet_images
from src.data import data


class PlanetSprite(pygame.sprite.Sprite):
    def __init__(self, name, radius, orbit_radius, speed, **kwargs):
        super().__init__()
        self.point = rotate_z(
            np.array([[orbit_radius, 0, 0]]),
            3,
        )
        self.name = name
        print("point", self.point)
        self.image = planet_images[name]
        self.image = pygame.transform.scale(self.image, (radius * 2, radius * 2))
        self.radius = radius
        self.orbit_radius = orbit_radius
        self.speed = speed

    @property
    def z(self):
        return np.squeeze(self.point)[2]

    @property
    def size(self):
        return self.radius * 8

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
        self.theta = 29  # HACK
        for i in range(len(signs)):
            if self.theta >= i * 30 and self.theta < (i + 1) * 30:
                return signs[i]
