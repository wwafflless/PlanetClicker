import pygame
import sys

pygame.init()
pygame.display.set_caption("Simple Game")

from planet import Planet
from assets import pixel_font


class Game:
    def __init__(self, width=800, height=600):
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.running = True
        self.size = pygame.Rect(0, 0, width, height)

        self.test_text = pixel_font.render(
            "Hello there, beautiful weather today!", True, (255, 255, 255)
        )
        all_planets = pygame.sprite.Group()
        all_planets.add(
            Planet(
                name="earth",
                radius=20,
                orbit_radius=0,
                speed=0,
            ),
            Planet(
                name="moon",
                radius=3,
                orbit_radius=30,
                speed=5,
            ),
            Planet(
                name="mercury",
                radius=7,
                orbit_radius=50,
                speed=3,
            ),
            Planet(
                name="venus",
                radius=10,
                orbit_radius=80,
                speed=2,
            ),
            Planet(
                name="mars",
                radius=12,
                orbit_radius=120,
                speed=1,
            ),
            Planet(
                name="jupiter",
                radius=40,
                orbit_radius=200,
                speed=0.2,
            ),
            Planet(
                name="saturn",
                radius=50,
                orbit_radius=330,
                speed=0.1,
            ),
        )
        self.all_planets = all_planets

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)
        pygame.quit()
        sys.exit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
            if event.type == pygame.KEYDOWN:
                pass

    def update(self):
        mouse = pygame.mouse.get_pos()
        # TODO process mouse key input
        self.all_planets.update()
        pygame.display.update()

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.test_text, (0, 0))
        self.all_planets.draw(self.screen)
        pygame.display.flip()
        self.clock.tick(60)
