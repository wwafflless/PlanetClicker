from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional

import pygame
from planetclicker import Colors, color
from planetclicker.model import BlankSprite
from pygame.sprite import Group, Sprite
from pygame.surface import Surface


@dataclass
class Ball:
    sprite: Sprite = BlankSprite()
    position: tuple[float, float, float] = (0, 0, 0)
    velocity: tuple[float, float, float] = (0, 0, 0)


@dataclass
class Sun(Ball):
    planets: List[Planet] = field(default_factory=list)


@dataclass
class Planet(Ball):
    moons: List[Moon] = field(default_factory=list)


class Moon(Ball): ...


@dataclass
class SolarSystem:
    sun: Sun
    sprite: pygame.sprite.Group = Group()

    @property
    def planets(self):
        return self.sun.planets

    @classmethod
    def simple(cls) -> SolarSystem:
        sun = Sun(position=(0, 0, 0), velocity=(0, 0, 0))
        sun.planets.append(
            Planet(
                position=(500, 0, 0),
                velocity=(0, 10, 0),
            )
        )
        return cls(sun=sun)

    def update(self):
        self.sprite.update()

    def render(self, surface: Surface):
        surface.fill(Colors.red)
