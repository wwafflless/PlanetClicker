from enum import Enum, StrEnum
from types import SimpleNamespace
from planetclicker import color

import pygame

from planetclicker.command import Command, QuitGame

from dataclasses import dataclass

from pygame.locals import *
from pygame.time import Clock

from planetclicker.scene import SceneManager
from planetclicker.scene.title import TitleScene
from planetclicker.settings import Settings, Setting, SettingGroup


GameState = StrEnum("GameState", ["Loading", "Running", "Quitting"])


class Game:
    screen = pygame.display.set_mode((800, 600))
    manager = SceneManager()

    def __init__(self):
        self.state = GameState.Loading
        pygame.display.set_caption("Planet Clicker")
        self.manager.push(TitleScene())
        self.clock = Clock()
        self.settings = Settings()

    def run(self):
        self.state = GameState.Running
        while self.state == GameState.Running:
            self.handle_input()
            self.update()
            self.draw()

    def handle_input(self):
        filtered_events = []
        pressed_keys = pygame.key.get_pressed()
        keybinds = {
            K_ESCAPE: QuitGame(),
        }
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
            elif event.type == KEYDOWN:
                key = event.key
                if key in keybinds:
                    keybinds[key].execute()

        self.manager.handle_input(filtered_events, pressed_keys)

    def update(self):
        self.manager.update()
        # delta = self.clock.tick(self.settings.graphics.fps) / 1000

    def draw(self):
        self.screen.fill(color.background)
        self.manager.render(self.screen)
        pygame.display.flip()
