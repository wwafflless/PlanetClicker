from __future__ import annotations

from dataclasses import dataclass, field
from types import NoneType


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

    @classmethod
    def Bool(cls, name, default_value):
        return SettingOption(name=name, value=default_value, options=[True, False])


@dataclass
class SettingOptionBool(SettingOption):
    options: list[SettingValue] = field()


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


def default_settings():
    return SettingGroup(
        "root",
        [
            SettingGroup(
                "ui",
                [
                    SettingOption("lang", "en-us", ["en-us"]),
                    SettingOption("theme", "dark", ["dark", "light"]),
                    SettingOption(
                        "font", "pixelated_elegance", ["jersey25", "pixelated_elegance"]
                    ),
                    SettingOption.Bool("show_keys", True),
                    SettingOption.Bool("show_fps", True),
                ],
            ),
            SettingGroup(
                "graphics",
                [
                    SettingOption("fps", 30, [30, 60]),
                    SettingOption("dpi", 72, [72, 300]),
                    SettingOption.Bool("fullscreen", False),
                    SettingOption("resolution", (1600, 900), [(1600, 900), (800, 600)]),
                ],
            ),
        ],
    )
