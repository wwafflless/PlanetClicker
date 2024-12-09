import pygame
from abc import ABC, abstractmethod

from planetclicker.scene.manager import SceneManager
from planetclicker.scene.scene import Scene


class Command(ABC):
    @abstractmethod
    def execute(self, *args, **kwargs):
        raise NotImplemented("implement in subclass")


class GameCommand(Command):
    def __init__(self, game):
        self.game = game


# class PushScene(Command):
#     def exec(
#         self,
#         scene_manager: SceneManager,
#         scene: Scene,
#     ):
#         scene_manager.push(scene)


# class PopScene(Command):
#     def execute(self, scene_manager: SceneManager):
#         scene_manager.pop()


class ToggleDebug(GameCommand):
    def execute(self):
        self.game.debug = not self.game.debug


class QuitGame(GameCommand):
    def execute(self):
        pygame.quit()
