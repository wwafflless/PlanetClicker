import os
from collections import defaultdict
from tomlkit.api import string
from dataclasses import dataclass
from types import SimpleNamespace

import pygame
import tomlkit

from planetclicker.asset.font import FontsParser


@dataclass
class TOMLReader:
    path: str
    # def read(self, filename: str):
    #     s

    def get(self, key: str):
        return self.data.get(key)

    def gets(self, *keys: str):
        cfg = self.data
        for key in keys:
            cfg = cfg.get(key)
        return cfg

    @property
    def data(self):
        with open(self.path) as fp:
            doc = tomlkit.load(fp)
            # doc.add("path", string(self.path))
            return doc


@dataclass
class FontReader(TOMLReader):
    path: str

    @property
    def fonts(self):
        fonts = {}
        for label, props in self.data.items():
            path = os.path.join("asset", "font", "free", props["name"])
            fonts[label] = pygame.font.Font(path, props["size"])
        return fonts


class Namespace(SimpleNamespace):
    """A simple namespace, plus an `all` getter that returns all items in the space."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # def __setattr__(self, name: str, value, /) -> None:
    #     self.__dict__[name] = value
    #     return super().__setattr__(name, value)

    @property
    def all(self):
        return self.__dict__.items()

    def get(self, key: str):
        return self.__dict__.get(key)

    @property
    def data(self):
        with open(self.path) as fp:
            tomlkit.load(fp)


font_parser = FontsParser()


class Game(Namespace):
    """Namespace for game stuff."""

    Config = Namespace(**TOMLReader("data/config.toml").data)
    Settings = Namespace(**TOMLReader("data/settings.toml").data)
    Graphics = Namespace(**TOMLReader("data/graphics.toml").data)
    Color = Namespace(**TOMLReader("data/color.toml").data)
    Font = Namespace(**FontReader("data/font.toml").fonts)


class Dev(Namespace):
    """Namespace for development stuff."""

    Planets = Namespace(**TOMLReader("data/planets.toml").data)
