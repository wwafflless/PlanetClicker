from datetime import datetime

import pygame

from src.asset.font import text_font
from src.data import data
from src.sprite.planet import Planet
from src.scene import Scene


class PlanetsScene(Scene):
    def __init__(self):
        super().__init__("planets", None)

    def handle_input(self, events, pressed_keys): ...

    def update(self): ...
    def render(self, screen):
        screen.fill((0, 0, 0))
