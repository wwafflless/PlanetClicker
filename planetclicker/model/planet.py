from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum

from pygame.sprite import Sprite

from planetclicker.data import planets
from planetclicker.model.identity import Identity, Resource
from planetclicker.model.position import Position
from planetclicker.asset.sprite_sheet import SpriteStripAnim

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
    sprite: Sprite = SpriteStripAnim(
        "asset/sheet/orb_2.png",
        rect=(0, 0, 51, 51),
        count=10,
        loop=True,
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

    # Load game data from key
    # and create PlanetModel instance
    # if d := planets.get(key):
    #     name = key
    #     radius = d["radius"]
    #     orbit_radius = d["orbit_radius"]
    #     position = d["position"]
    #     velocity = d["velocity"]
    #     sprite = d["sprite"]
    #     match sprite["type"]:
    #         case "sheet":
    #             sheet_name = sprite["name"]
    #             sheet_count = sprite["count"]
    #             sheet_rect = sprite["rect"]
    #             s = SpriteStripAnim(
    #                 f"asset/sheet/{sheet_name}.png",
    #                 sheet_rect,
    #                 sheet_count,
    #             )
    #             return cls.make(
    #                 name,
    #                 "desc",
    #                 100,
    #                 10,
    #                 position,
    #                 velocity,
    #                 mass=999,
    #             )
    # else:
    #     raise ValueError(f"No planet data found for key: {key}")

    # @property
    # def upgraded_stats(self):
    #     stats = self.stats
    #     for upgrade in self.upgrades:
    #         for stat in upgrade.stats:
    #             v = stat.value(stats.__dict__[stat.name])
    #             print(stat.name, v)
    #             stats.__dict__[stat.name] = v
    #     return stats


# EarnDoublePlanetUpgrade = Upgrade(
#     "Earn Double",
#     100,
#     [Upgrade("earn", lambda x: x * 2)],
# )
# HalfDelayPlanetUpgrade = Upgrade(
#     "Half Delay",
#     200,
#     [Upgrade("delay", lambda x: x // 2)],
# )

# PlanetStats: dict[str, int | str | dict] = dict()

# earn_double_upgrade = Upgrade()

# planet_stats = dict(
#     name="planet zybarg",
#     element="earth",
#     triplicity="fixed",
#     upgrades=[earn_double_upgrade],
# )


# @dataclass
# class PlanetQualities:
#     element: ElementEnum
#     triplicity: TriplicityEnum


planets = [
    Planet.make(
        name="Aleph 1",
        desc="desc",
        health=100,
        magic=100,
        position=(5, 0, 0),
        velocity=(1, 0, 0),
        mass=999,
        # age=10_000_000_000,
        # sprite=pygame.Sprite("orb-15"),
    )
]
