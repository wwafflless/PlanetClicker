from typing import Dict, Self
import pygame
from abc import ABC, abstractmethod
from dataclasses import dataclass

from planetclicker.scene.manager import SceneManager
from planetclicker.scene.scene import Scene


class Command(ABC):
    @abstractmethod
    def execute(self, *args, **kwargs):
        raise Exception("Command")


class PushScene(Command):
    def exec(
        self,
        scene_manager: SceneManager,
        scene: Scene,
    ):
        scene_manager.push(scene)


class PopScene(Command):
    def execute(self, scene_manager: SceneManager):
        scene_manager.pop()


class QuitGame(Command):
    def execute(self):
        pygame.quit()
