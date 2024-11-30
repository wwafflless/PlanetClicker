from types import SimpleNamespace

import tomlkit
from planetclicker.data.loader import FontReader, TOMLReader


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


class Game(Namespace):
    """Namespace for game stuff."""

    Config = Namespace(**TOMLReader("data/config.toml").data)
    Settings = Namespace(**TOMLReader("data/settings.toml").data)
    Graphics = Namespace(**TOMLReader("data/graphics.toml").data)
    UI = Namespace(**TOMLReader("data/ui.toml").data)
    Color = Namespace(**TOMLReader("data/color.toml").data)
    Font = Namespace(**FontReader("data/font.toml").fonts)


class Dev(Namespace):
    """Namespace for development stuff."""

    Planets = Namespace(**TOMLReader("data/planets.toml").data)
