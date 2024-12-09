from __future__ import annotations

from dataclasses import dataclass
from numbers import Number
from types import NoneType, SimpleNamespace, UnionType
from typing import Dict, List, Optional, Self, Union

from planetclicker.util import singleton


@dataclass
class Setting:
    name: str


SettingValue = (
    int
    | float
    | bool
    | str
    | list["SettingValue"]
    | tuple["SettingValue", ...]
    | NoneType
)


@dataclass
class SettingOption(Setting):
    value: SettingValue
    options: list[SettingValue]


@dataclass
class SettingOptionBool(SettingOption):
    options = [True, False]


@dataclass
class SettingGroup(Setting):
    children: list[Setting]

    def get(self, name):
        for child in self.children:
            if child.name.lower() == name:
                match child:
                    case SettingOption():
                        return child.value
                    case SettingGroup():
                        return child
        raise ValueError(f"Not found: {name}")

    def gets(self, *names):
        s = self.get(names[0])
        if isinstance(s, SettingGroup):
            for n in names[1:]:
                s = s.get(n)
        return s


settings = SettingGroup(
    "root",
    [
        SettingGroup(
            "ui",
            [
                SettingOption("lang", "en-us", ["en-us", "fr-fr"]),
                SettingOption("theme", "dark", ["dark", "light"]),
                SettingOption(
                    "font", "pixelated_elegance", ["jersey25", "pixelated_elegance"]
                ),
                SettingOption("show_keys", True, [True, False]),
                SettingOption("show_fps", True, [True, False]),
            ],
        ),
        SettingGroup(
            "graphics",
            [
                SettingOption("fps", 30, [30, 60]),
                SettingOption("dpi", 72, [72, 300]),
                SettingOption("fullscreen", True, [True, False]),
                SettingOption("resolution", (1600, 900), [(1600, 900), (800, 600)]),
            ],
        ),
    ],
)
