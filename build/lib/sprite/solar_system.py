import numpy as np
import pygame

from src.asset import planet_images
from src.math.rotate import rotate_x, rotate_y, rotate_z
from src.particle.bg_star import BGStarSystem
from src.sprite.planet import PlanetSprite


class SolarSystem:
    def __init__(self, planets: list[PlanetSprite]):
        self.planets = planets
        self.bg_stars = BGStarSystem(100)

    def update(self):
        self.bg_stars.update()
        for planet in self.planets:
            planet.update()

    def draw(self, surface):
        self.bg_stars.draw(surface)
        for planet in self.planets:
            planet.draw(surface)
