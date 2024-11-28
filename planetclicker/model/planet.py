from typing import Callable
from dataclasses import dataclass
from enum import StrEnum


ElementEnum = StrEnum("Element", ["earth", "water", "air", "fire"])
TriplicityEnum = StrEnum("Triplicity", ["cardinal", "fixed", "mutable"])


@dataclass
class PlanetStat:
    name: str
    value: Callable


@dataclass
class PlanetStats:
    earn: int
    delay: int
    level: int
    velocity: int


@dataclass
class PlanetUpgrade:
    name: str
    cost: int
    stats: list[PlanetStat]


class PlanetModifier:
    def __init__(self, name, cost, stats):
        self.name = name
        self.stats = stats


EarnDoublePlanetUpgrade = PlanetUpgrade(
    "Earn Double",
    100,
    [PlanetStat("earn", lambda x: x * 2)],
)
HalfDelayPlanetUpgrade = PlanetUpgrade(
    "Half Delay",
    200,
    [PlanetStat("delay", lambda x: x // 2)],
)


@dataclass
class PlanetQualities:
    element: ElementEnum
    triplicity: TriplicityEnum


class Planet:
    def __init__(self, name, radius, orbit_radius, speed, **kwargs):
        super().__init__()
        self.upgrades = [
            EarnDoublePlanetUpgrade,
            HalfDelayPlanetUpgrade,
        ]
        self.name = name
        self.orbit_radius = orbit_radius
        self.qualities = PlanetQualities(
            element=ElementEnum.earth,
            triplicity=TriplicityEnum.cardinal,
        )
        self.stats = PlanetStats(
            earn=10,
            delay=10,
            level=1,
            velocity=3,
        )

    @property
    def upgraded_stats(self):
        stats = self.stats
        for upgrade in self.upgrades:
            for stat in upgrade.stats:
                v = stat.value(stats.__dict__[stat.name])
                print(stat.name, v)
                stats.__dict__[stat.name] = v
        return stats
