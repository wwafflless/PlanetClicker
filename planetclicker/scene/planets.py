from datetime import datetime

import pygame

from planetclicker.data import Game
from planetclicker.scene.scene import Scene


class PlanetsScene(Scene):
    def __init__(self):
        super().__init__("planets", None)

    def handle_input(self, events, pressed_keys): ...

    def update(self): ...

    def render(self, screen):
        screen.fill((0, 0, 0))
