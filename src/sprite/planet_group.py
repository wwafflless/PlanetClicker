import numpy
from src.math.rotate import rotate_x, rotate_y, rotate_z
from src.asset import planet_images
import numpy as np
import pygame
from numpy import cos, eye, sin
from src.sprite.planet import PlanetSprite


class PlanetGroup(pygame.sprite.Group):
    def __init__(self, planets: list[PlanetSprite]):
        super().__init__()
        self.planets = planets
        for p in planets:
            self.add(p)

    def update(self):
        super().update()

        print(self.planets)
        for planet in self.planets:
            spd = planet.speed
            point = planet.point
            point = rotate_x(point, spd * 0)
            point = rotate_y(point, spd * 1)
            point = rotate_z(point, spd * 1)
            # point = rotate_x(point, spd * 0.9)
            pt = np.squeeze(point)
            z = planet.size / 2 - np.asarray(pt)[2] / 8
            print("rad", planet.radius)
            print("z", z)
            planet.rect = pygame.Rect(
                (
                    400 + pt[0] - z / 2,
                    300 + pt[1] - z / 2,
                ),
                (z, z),
            )
            planet.image = planet_images[planet.name]
            planet.image = pygame.transform.scale(
                planet.image,
                (z, z),
            )
            planet.point = point
            self.planets = sorted(
                self.planets,
                key=lambda p: p.z,
            )
