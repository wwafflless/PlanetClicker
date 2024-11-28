from dataclasses import dataclass
from typing import Any, Callable, Type

import pygame

from planetclicker.scene import Scene


@dataclass
class Button(pygame.sprite.Sprite):
    text: str
    scene: Type[Scene]
