from enum import Enum, StrEnum
from datetime import datetime
from planetclicker.color import Colors
from types import SimpleNamespace
from planetclicker import color

import pygame

from planetclicker.command import Command, QuitGame, ToggleDebug

from dataclasses import dataclass

from pygame.locals import *
from pygame.time import Clock

from planetclicker.font import DebugFont, TextFont, TitleFont
from planetclicker.scene import SceneManager
from planetclicker.scene.title import TitleScene
from planetclicker.settings import Settings, Setting, SettingGroup


GameState = StrEnum("GameState", ["Loading", "Running", "Quitting"])


class Game:
    screen = pygame.display.set_mode((800, 600))
    manager = SceneManager()

    def __init__(self, debug=False):
        pygame.display.set_caption("Planet Clicker")
        self.debug = debug
        self.state = GameState.Loading
        self.manager.push(TitleScene())
        self.clock = Clock()
        self.settings = Settings()
        self.state = GameState.Running
        self.show_keys = True

    def run(self):
        while self.state == GameState.Running:
            self.run_loop()

    def run_loop(self):
        self.handle_input()
        self.update()
        self.draw()
        self.clock.tick(self.settings.Graphics.fps)

    def handle_input(self):
        filtered_events = []
        pressed_keys = pygame.key.get_pressed()
        keybinds = {
            K_ESCAPE: QuitGame(self),
            K_d: ToggleDebug(self),
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

    def draw(self):
        self.screen.fill(Colors.background)
        self.manager.render(self.screen)
        if self.debug:
            fps = self.clock.get_fps()
            info = DebugFont.render(
                f"""debug
state:   {self.state}
fps:     {fps:.2f}
time:    {datetime.now()}
            """
            )
            self.screen.blit(info, (5, 5))
            keys = DebugFont.render(
                f"""keys
                todo
            """,
                color=Colors.green,
            )
            self.screen.blit(keys, (5, 500))
        pygame.display.flip()
