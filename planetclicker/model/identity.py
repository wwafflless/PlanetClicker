from dataclasses import dataclass
from enum import Enum
from typing import Optional


@dataclass
class Identity:
    """Entities have a name and maybe a description."""

    name: str
    desc: Optional[str]


class Resource:
    """There are three types of resources for an entity"""

    name: str
    type: Enum  # Enum("Resource", "health", "mana", "tech" )
    value: int


@dataclass
class Tech(Resource):
    """There are three types of resources for an entity"""

    health = int
    mana = int
    tech = int
