from datetime import datetime

import pygame

from src.scene import Scene
from src.scene.clicker import ClickerScene
from src.scene.planets import PlanetsScene


class MainScene(Scene):
    def __init__(self, manager):
        super().__init__("main", manager)
        self.left_scene = ClickerScene()
        self.right_scene = PlanetsScene()
        self.left_surface = pygame.Surface((800, 600))
        self.right_surface = pygame.Surface((400, 600))

    def handle_input(self, events, pressed_keys): ...

    def update(self):
        self.left_scene.update()
        self.right_scene.update()

    def render(self, screen):
        self.left_scene.render(self.left_surface)
        self.right_scene.render(self.right_surface)
        screen.blit(self.right_surface, (400, 0))
        screen.blit(self.left_surface, (0, 0))
