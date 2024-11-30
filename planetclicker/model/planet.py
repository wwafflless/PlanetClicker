from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum
from typing import Tuple

import numpy as np
from planetclicker.math.rotate import rotate_x, rotate_y, rotate_z
from planetclicker.sprite.animated_sprite import AnimatedSprite
from pygame import Surface


@dataclass
class PhysicsComponent:
    position: Tuple[float, float, float]
    velocity: Tuple[float, float, float]
    camera: Tuple[float, float, float]
    mass: float

    def update(self):
        self.position = rotate_z(self.position, angle=1.0)
        x, y, z = self.position
        dx, dy, dz = self.velocity
        self.position = (x + dx, y + dy, z + dz)
        self.camera = rotate_y(self.position, angle=1.0)
        self.camera = rotate_x(self.camera, angle=1.0)


@dataclass
class Planet:
    physics: PhysicsComponent
    sprite: AnimatedSprite

    def update(self):
        self.physics.update()
        self.sprite.update()
        x, y, _ = self.physics.position
        self.sprite.set_position(x, y)

    def draw(self, surface: Surface):
        # self.sprite.draw(surface)
        surface.blit(
            self.sprite.current_image,
            (
                self.physics.position[0],
                self.physics.position[1],
            ),
            (
                self.sprite.size,
                self.sprite.size,
            ),
        )


# @dataclass
# class SpriteGraphicsComponent(GraphicsComponent):
#     def render(self, surface: Surface):
#         raise NotImplementedError("Subclasses must implement this method")


# @dataclass
# class AnimatedSpriteGraphicsComponent(GraphicsComponent):
#     def render(self, surface: Surface):
#         raise NotImplementedError("Subclasses must implement this method")

Element = StrEnum("Element", ["earth", "water", "air", "fire"])
Triplicity = StrEnum("Triplicity", ["cardinal", "fixed", "mutable"])
