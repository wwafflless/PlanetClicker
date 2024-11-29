import tomlkit
import pygame
from dataclasses import dataclass


@dataclass
class FileLoader:
    filename: str

    @property
    def data(self):
        raise NotImplementedError("Subclasses must implement the data property")


@dataclass
class ImageLoader(FileLoader):
    filename: str

    @property
    def data(self):
        with open(self.filename) as fp:
            return pygame.image.load(fp)


@dataclass
class ConfigLoader(FileLoader):

    def get(self, key: str):
        return self.data.get(key)

    def gets(self, *keys: str):
        cfg = self.data
        for key in keys:
            cfg = cfg.get(key)
        return cfg

    @property
    def data(self):
        with open(self.filename) as fp:
            return tomlkit.load(fp)


config = ConfigLoader(filename="data/config.toml")
planets = ConfigLoader(filename="data/planets.toml")
settings = ConfigLoader(filename="data/settings.toml")
