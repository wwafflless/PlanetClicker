import os
import pygame
from tomlkit import TOMLDocument
from dataclasses import dataclass
from planetclicker.model.planet import Planet
from planetclicker.sprite.animated_sprite import AnimatedSprite

from typing import Generic, TypeVar


T = TypeVar("T")


class Parser(Generic[T]):
    def parse(self, data: T) -> dict | list:
        raise NotImplementedError("Subclasses must implement parse method")


class PlanetsParser(Parser[TOMLDocument]):
    def parse(self, data: TOMLDocument):
        planets = []
        for planet in data["planet"]:
            planet_radius: int = planet["radius"]
            planet_orbit: int = planet["orbit_radius"]
            planet_speed: int = planet["speed"]
            planet_name: str = planet["color"]
            sprite_name: str = planet["sprite"]["name"]
            sprite_count: int = planet["sprite"]["count"]
            sprite_rect: Tuple[int, int, int, int] = planet["sprite"]["rect"]
            planets.append(
                Planet(
                    name=planet_name,
                    health=100,
                    magic=100,
                    position=(5, 0, 0),
                    velocity=(0.1, 0, 0),
                    mass=999999,
                    sprite=AnimatedSprite(
                        filename=sprite_name,
                        width=sprite_rect[2],
                        height=sprite_rect[3],
                    ),
                )
            )
        return planets
