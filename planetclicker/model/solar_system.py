from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import List, Optional

import numpy as np
import pygame
from planetclicker import Colors, color
from planetclicker.model import BlankSprite
from pygame.sprite import Group, Sprite
from pygame.surface import Surface


def rand_val(bounds):
    return np.random.uniform(*bounds)


def rand_color(**color):
    r = rand_val(color["color_r"])
    g = rand_val(color["color_g"])
    b = rand_val(color["color_b"])
    a = rand_val(color["color_a"])
    return (r, g, b, a)


Color = pygame.color.Color


@dataclass
class Theme:
    fill: Color
    stroke: Color
    other: Color


class ColorStrat(ABC):
    @abstractmethod
    def fill_color(self) -> Color: ...
    @abstractmethod
    def stroke_color(self) -> Color: ...
    @abstractmethod
    def other_color(self) -> Color: ...


class ComplementaryColors(ColorStrat):
    def __init__(self) -> None:
        self.hue_1 = np.random.randint(0, 255)
        self.hue_2 = (self.hue_1 + 127) % 255

    def stroke_color(self):
        sat = np.random.randint(0, 255)
        alpha = np.random.randint(0, 255)
        return pygame.Color.from_hsla(self.hue_1, sat, 100, alpha)

    def other_color(self):
        alpha = np.random.randint(0, 255)
        return pygame.Color.from_hsla(0, 0, 100, alpha)

    def fill_color(self):
        sat = np.random.randint(0, 255)
        alpha = np.random.randint(0, 255)
        return pygame.Color.from_hsla(self.hue_2, sat, 100, alpha)


class MonochromaticColors(ColorStrat):
    def __init__(self) -> None:
        self.hue = np.random.randint(0, 255)

    def border_color(self):
        sat = np.random.randint(0, 255)
        alpha = np.random.randint(0, 255)
        return pygame.Color.from_hsla(self.hue, sat, 100, alpha)

    def glow_color(self):
        sat = np.random.randint(0, 255)
        alpha = np.random.randint(0, 255)
        return pygame.Color.from_hsla(self.hue, sat, 100, alpha)

    def fill_color(self):
        sat = np.random.randint(0, 255)
        alpha = np.random.randint(0, 255)
        return pygame.Color.from_hsla(self.hue, sat, 100, alpha)


def rand_choice(opts):
    return opts[np.random.randint(len(opts)) % len(opts)]


# SHAPES = [
#     Shape(
#         geometry=Circle(radius=3),
#         colors=Monochromatic(hue=200),
#     ),
#     Shape(
#         geometry=Gram(n=3),
#         colors=Complementary(hue=30),
#     ),
#     Shape(
#         geometry=ShapeGeometry.random(),
#         colors=ShapeColors.random(),
#     ),
# ]


@dataclass
class RenderStrategy(ABC):
    color_strat: ColorStrat
    shape_strat: ShapeStrat

    @classmethod
    def random(cls):
        color_strat = rand_choice([MonochromaticColors, ComplementaryColors])
        shape_strat = rand_choice(
            [
                EllipseShapes,
                CircleShapes,
                GonShapes,
                GramShapes,
            ]
        )
        return cls(
            color_strat=color_strat,
            shape_strat=shape_strat,
        )

    @abstractmethod
    def render(self, shape):
        pass


# Concrete Render Strategies
class ColorfulRenderStrategy(RenderStrategy):
    def render(self, shape):
        if isinstance(shape, Circle):
            print(
                f"Rendering Circle with radius: {shape.radius}, center: {shape.center}"
            )
            circle = plt.Circle(shape.center, shape.radius, color="cyan", alpha=0.5)
            plt.gca().add_artist(circle)

        elif isinstance(shape, Ellipse):
            print(
                f"Rendering Ellipse with width: {shape.width}, height: {shape.height}, center: {shape.center}"
            )
            ellipse = plt.Circle(
                shape.center, shape.width, shape.height, color="magenta", alpha=0.5
            )
            plt.gca().add_artist(ellipse)

        elif isinstance(shape, Polygon):
            print(f"Rendering Polygon with vertices: {shape.vertices}")
            polygon = plt.Polygon(shape.vertices, color="yellow", alpha=0.5)
            plt.gca().add_artist(polygon)


class DashedRenderStrategy(RenderStrategy):
    def render(self, shape):
        line_style = "--"
        if isinstance(shape, Circle):
            print(
                f"Rendering Circle with dashed border and radius: {shape.radius}, center: {shape.center}"
            )
            circle = plt.Circle(
                shape.center,
                shape.radius,
                color="blue",
                fill=False,
                linestyle=line_style,
            )
            plt.gca().add_artist(circle)

        elif isinstance(shape, Ellipse):
            print(
                f"Rendering Ellipse with dashed border, width: {shape.width}, height: {shape.height}, center: {shape.center}"
            )
            ellipse = plt.Circle(
                shape.center,
                shape.width,
                shape.height,
                color="green",
                fill=False,
                linestyle=line_style,
            )
            plt.gca().add_artist(ellipse)

        elif isinstance(shape, Polygon):
            print(
                f"Rendering Polygon with dashed border and vertices: {shape.vertices}"
            )
            polygon = plt.Polygon(
                shape.vertices,
                closed=True,
                fill=None,
                edgecolor="orange",
                linestyle=line_style,
            )
            plt.gca().add_artist(polygon)


@dataclass
class ShapeGeometry:
    width: int
    height: int


@dataclass
class NGramGeometry:
    n: int  #


@dataclass
class EllipseGeometry: ...


@dataclass
class CircleGeometry: ...


class ShapeColors: ...


@dataclass
class Shape(ABC):
    geometry: ShapeGeometry
    colors: ShapeColors

    @abstractmethod
    def draw(self): ...


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
