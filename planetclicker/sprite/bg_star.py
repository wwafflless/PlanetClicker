import random

import pygame

from planetclicker.color import Colors


class BGStar:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = random.uniform(-1, 1)
        self.dy = random.uniform(-1, 1)
        self.surface = pygame.Surface((1, 1))
        self.surface.set_alpha(random.randint(0, 200))

    def update(self):
        self.x += self.dx / 10
        self.y += self.dy / 10

    def draw(self, window):
        self.surface.fill(Colors.text)
        window.blit(self.surface, (self.x, self.y))


class BGStarSystem:
    def __init__(self, n=100, size=(800, 600)):
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
            particle.draw(self.surface)
        surface.blit(self.surface, (0, 0))
