from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum

from pygame.sprite import Sprite

from planetclicker.model.identity import Identity, Resource
from planetclicker.model.position import Position
from planetclicker.sprite.animated_sprite import AnimatedSprite

Element = StrEnum("Element", ["earth", "water", "air", "fire"])
Triplicity = StrEnum("Triplicity", ["cardinal", "fixed", "mutable"])


@dataclass
class Planet(Identity, Resource, Position):
    name: str
    description: str
    health: int
    magic: int
    position: tuple = (5, 0, 0)
    velocity: tuple = (0, 1, -1)
    mass: int = 100_000_000
    sprite: Sprite = AnimatedSprite(
        name="orb_2",
        w=51,
        h=51,
        frames=10,
    )

    @classmethod
    def make(cls, name, desc, health, magic, position, velocity, mass):
        return cls(
            name,
            desc,
            health,
            magic,
            position,
            velocity,
            mass,
        )
