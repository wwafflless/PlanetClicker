import pygame
import sys

pygame.init()
pygame.display.set_caption("Simple Game")

from planet import Planet
from assets import pixel_font
from game_data import data


class Game:
    def __init__(self, width=800, height=600):
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.running = True
        self.size = pygame.Rect(0, 0, width, height)

        self.test_text = pixel_font.render(
            data["welcome_message"], True, (255, 255, 255)
        )
        all_planets = pygame.sprite.Group()
        for k, v in data["planets"].items():
            all_planets.add(Planet(name=k, **v))
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
