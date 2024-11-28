from datetime import datetime

import pygame

from planetclicker.asset.font import text_font
from planetclicker.data import data
from planetclicker.scene import Scene
from planetclicker.sprite.planet import PlanetSprite


class PlanetsScene(Scene):
    def __init__(self):
        super().__init__("planets", None)

    def handle_input(self, events, pressed_keys): ...

    def update(self): ...

    def render(self, screen):
        screen.fill((0, 0, 0))
