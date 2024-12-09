import pygame


from dataclasses import dataclass


class Scene:
    """
    A scene in the game.
    """

    def __init__(
        self,
        name: str,
        top_left=(0, 0),
        width_height=(800, 600),
    ):
        self.name = name
        self.next = self
        self.rect = pygame.Rect(top_left, width_height)

    def switch(self, next_scene) -> None:
        self.next = next_scene

    def kill(self) -> None:
        self.next = None

    def handle_input(self, events, pressed_keys) -> None:
        raise Exception("handle_input not implemented")

    def update(self) -> None:
        raise Exception("update not implemented")

    def render(self, surface: pygame.Surface) -> None:
        raise Exception("render not implemented")
