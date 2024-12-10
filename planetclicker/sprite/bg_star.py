import numpy as np
from pygame.surface import Surface
import random

import pygame

from planetclicker.color import Colors


class BGStar:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.z = np.random.uniform(0.0, 10.0)
        self.r = 0.5 / self.z
        self.t = np.random.uniform(0.0001, 2.0 * np.pi)
        self.dt = np.random.uniform(0.01, 2.0)
        self.dx = self.r * np.cos(self.t)
        self.dy = self.r * np.sin(self.t)
        self.dz = self.r * np.cos(self.t)
        self.surface = pygame.Surface((self.r, self.r))

    def update(self):
        self.t += self.dt
        self.dx = self.r * np.cos(self.dt)
        self.dy = self.r * np.sin(self.dt)
        # self.dz = np.sin(self.t / 2.0)
        self.x += self.dx / 1
        self.y += self.dy / 1
        # self.z = np.sin(self.t / 10.0)

    def draw(self, surface: Surface):
        pygame.draw.circle(
            surface,
            color=Colors.accent,
            center=(self.x, self.y),
            radius=self.r,
        )
        self.surface.set_alpha(int(10.0 + self.z))


class BGStarSystem:
    def __init__(self, n=100, size=(1600, 900)):
        self.size = size
        self.surface = pygame.Surface(size)

        self.particles = []
        for _ in range(n):
            self.add_particle(random.randint(0, size[0]), random.randint(0, size[1]))

    def add_particle(self, x, y):
        self.particles.append(BGStar(x, y))

    def update(self):
        for particle in self.particles:
            particle.update()
            particle.x %= self.size[0]
            particle.y %= self.size[1]

    def draw(self, surface):
        self.surface.fill(pygame.SRCALPHA)
        for particle in self.particles:
            # pygame.draw.circle(
            #     self.surface,
            #     color=Colors.accent,
            #     center=(particle.x, particle.y),
            #     radius=int(particle.r),
            # )
            particle.draw(self.surface)
        surface.blit(self.surface, (0, 0))
