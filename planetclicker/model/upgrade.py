from dataclasses import dataclass


import numpy as np
from typing import Callable


@dataclass
class StatChange:
    """Changes the value of a Stat"""

    stat_key: str
    stat_op: Callable


def plus_one(n: int) -> int:
    return n + 1


IncreaseLevel = StatChange("level", plus_one)
RestoreHP = StatChange("health", lambda _: 999_999_999)  # TODO MAX_HP
RestoreHP = StatChange("planets", plus_one)


@dataclass
class Upgrade:
    name: str
    cost: int
    stat_changes: list[StatChange]


LevelUpgrade = Upgrade("Leved up!", 0, [IncreaseLevel, RestoreHP])
