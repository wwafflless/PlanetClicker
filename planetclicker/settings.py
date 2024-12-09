from __future__ import annotations
from numbers import Number
from types import NoneType, SimpleNamespace
from typing import List, Optional, Self, Union
from dataclasses import dataclass

from planetclicker.util import singleton

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
class Setting:
    name: str
    value: SettingValue
    options: list[SettingValue]


class SettingGroup:
    """Is this even necessary?"""

    def __init__(self, *settings: Setting):
        self.settings = settings

    def __getattr__(self, name: str) -> SettingValue:
        for setting in self.settings:
            if setting.name == name:
                return setting.value
        raise AttributeError(f"No setting found with name '{name}'")


@singleton
@dataclass
class Settings:
    UI = SettingGroup(
        Setting(
            "language",
            "en-us",
            ["en-us"],
        )
    )
    Graphics = SettingGroup(
        Setting(
            name="fps",
            value=30,
            options=[30, 60],
        ),
        Setting(
            name="dpi",
            value=72,
            options=[72],
        ),
        Setting(
            name="fullscreen",
            value=False,
            options=[True, False],
        ),
        Setting(
            name="resolution",
            value=(800, 600),
            options=[
                (640, 480),
                (1280, 720),
                (1920, 1080),
                (2560, 1440),
                (3840, 2160),
            ],
        ),
        Setting(
            "quality",
            value="high",
            options=["low", "high"],
        ),
    )
