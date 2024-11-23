import pygame
import sys
import datetime

pygame.init()
pygame.display.set_caption("Simple Game")

from planet import Planet
from game_data import data
from config import config
from asset import pixel_font


class Game:
    def __init__(self, width=800, height=600):
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.running = True
        self.size = pygame.Rect(0, 0, width, height)

        self.test_text = pixel_font.render(
            data["ui"]["welcome_text"], False, (255, 255, 255)
        )
        all_planets = pygame.sprite.Group()
        for k, v in data["planet"].items():
            all_planets.add(Planet(name=k, **v))
        self.all_planets = all_planets
        self.infos = dict()
        self.mana = 0

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

    def update_info(self):
        self.infos["mana"] = self.mana
        self.infos["time"] = datetime.datetime.now().strftime("%H:%M:%S")
        for planet in self.all_planets:
            self.infos[planet.name] = ", ".join(planet.dignity)

    def update_mana(self):
        self.mana += 1

    def update(self):
        self.update_info()
        self.update_mana()
        mouse = pygame.mouse.get_pos()
        # TODO process mouse key input
        self.all_planets.update()
        pygame.display.update()
        self.clock.tick(5)

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.test_text, (0, 0))
        for i, info in enumerate(self.infos.items()):
            k, v = info
            self.screen.blit(
                pixel_font.render(
                    k,
                    False,
                    (255, 255, 255),
                ),
                (550, i * 10),
            )
            self.screen.blit(
                pixel_font.render(
                    str(v),
                    False,
                    (255, 255, 255),
                ),
                (650, i * 10),
            )
        self.all_planets.draw(self.screen)
        pygame.display.flip()
