from datetime import datetime

from src.asset.color import Color
import pygame

from src.asset.font import text_font
from src.data import data
from src.sprite.planet import Planet
from src.scene import Scene


class ClickerScene(Scene):
    def __init__(self):
        super().__init__("clicker")

        self.test_text = text_font.render(
            data["ui"]["welcome_text"], False, (255, 255, 255)
        )
        all_planets = pygame.sprite.Group()
        for k, v in data["planet"].items():
            all_planets.add(Planet(name=k, **v))
        self.all_planets = all_planets
        self.infos = dict()

    def handle_input(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
            if event.type == pygame.KEYDOWN:
                pass

    def update_info(self):
        # self.infos["mana"] = self.mana
        self.infos["time"] = datetime.now().strftime("%H:%M:%S")
        for planet in self.all_planets:
            self.infos[planet.name] = ", ".join(planet.dignity)

    def update(self):
        self.update_info()
        self.all_planets.update()
        pygame.display.update()

    def render(self, screen):
        screen.fill(Color.black)
        screen.blit(self.test_text, (0, 0))
        for i, info in enumerate(self.infos.items()):
            k, v = info
            screen.blit(
                text_font.render(
                    k,
                    False,
                    (255, 255, 255),
                ),
                (550, i * 10),
            )
            screen.blit(
                text_font.render(
                    str(v),
                    False,
                    (255, 255, 255),
                ),
                (650, i * 10),
            )
        self.all_planets.draw(screen)
