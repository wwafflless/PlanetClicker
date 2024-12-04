import numpy as np
import pygame

from src.asset import planet_images
from src.math.rotate import rotate_x, rotate_y, rotate_z
from src.particle.bg_star import BGStarSystem
from src.sprite.planet import PlanetSprite


class SolarSystem:
    def __init__(self, planets: list[PlanetSprite]):
        self.planets = []
        for planet in planets:
            self.add_planet(planet)
        self.bg_stars = BGStarSystem(100)

    def add_planet(self, to_add):
        shouldAdd = True
        for planet in self.planets:
            if planet == to_add:
                shouldAdd = False
                break;
        
        if shouldAdd:
            self.planets.append(to_add)

    def update(self):
        self.bg_stars.update()
        for planet in self.planets:
            planet.update()

    def draw(self, surface):
        #selection sort planets by y value for correct draw order
        for i in range(len(self.planets) - 2):
            lowest = i
            for j in range(i, len(self.planets) - 1):
                if self.planets[j].pos[1] < self.planets[lowest].pos[1]:
                    lowest = j
            temp = self.planets[i]
            self.planets[i] = self.planets[lowest]
            self.planets[lowest] = temp
        
        self.bg_stars.draw(surface)
        for planet in self.planets:
            planet.draw(surface)
