from datetime import datetime

import pygame

from src.asset.color import Color
from src.asset.font import text_font
from src.data import data
from src.scene import Scene
from src.sprite.planet import PlanetSprite
from src.sprite.solar_system import SolarSystem


class ClickerScene(Scene):
    def __init__(self):
        super().__init__("clicker", manager=None)

        self.test_text = text_font.render(
            data["ui"]["welcome_text"], False, (255, 255, 255)
        )
        # planets group
        planets = []
        for planet_name, planet_props in data["planet"].items():
            planets.append(
                PlanetSprite(
                    name=planet_name,
                    **planet_props,
                )
            )
        self.solar_system = SolarSystem(planets)

    def handle_input(self, events, pressed_keys): ...

    def update(self):
        self.solar_system.update()

    def render(self, screen):
        screen.fill(Color.black)
        self.solar_system.draw(screen)
        screen.blit(self.test_text, (0, 0))
