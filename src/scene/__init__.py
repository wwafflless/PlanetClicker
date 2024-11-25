from dataclasses import dataclass

from typing import Optional
import pygame


class Scene:
    def __init__(
        self,
        name,
        manager,
        top_left=(0, 0),
        width_height=(800, 600),
    ):
        self.name = name
        self.next = self
        self.rect = pygame.Rect(top_left, width_height)
        if manager:
            self.manager = manager
            # manager.push_scene(self)

    def switch(self, next_scene) -> None:
        self.next = next_scene

    def kill(self) -> None:
        self.next = None

    def handle_input(self, events, pressed_keys) -> None:
        pass

    def update(self) -> None:
        raise Exception("not implemented")

    def render(self, screen) -> None:
        raise Exception("not implemented")
