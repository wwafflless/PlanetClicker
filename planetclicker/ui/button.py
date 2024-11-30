from dataclasses import dataclass

import pygame
from planetclicker.scene.scene import Scene


@dataclass
class Button(pygame.sprite.Sprite):
    text: str
    scene: Scene
