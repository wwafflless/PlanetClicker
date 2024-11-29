from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Level:
    name: str
    desc: str
    parent: Optional[Level] = None


IntroLevel = Level(
    name="intro",
    desc="intoduction level",
    parent=None,
)

BlankLevel = Level(
    name="blank",
    desc="blank slate",
    parent=None,
)

SimpleLevel = Level(
    name="simple",
    desc="some things",
    parent=BlankLevel,
)

NewLevel = Level(
    name="new",
    desc="another simple level",
    parent=SimpleLevel,
)

ComplexLevel = Level(
    name="complex",
    desc="wow",
    parent=NewLevel,
)
