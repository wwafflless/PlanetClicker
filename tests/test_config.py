import pygame

pygame.init()
from planetclicker.data import Game, Dev

import json


def test_planets_loader():
    assert len(Dev.Planets.all) == 8


def test_config_loader():
    assert Dev.Planets.gets("game", "difficulty") == "easy"
    assert Dev.Planets.gets("locale", "timezone") == "pst"
    assert Dev.Planets.gets("locale", "language") == "en-us"
    assert Dev.Planets.gets("font", "title", "path") == "ThaleahFat.ttf"
    assert Dev.Planets.gets("font", "title", "size") == 20

    assert "v_1" in Dev.Planets.gets("bind", "panel", "overview")
    assert "v_k" in Dev.Planets.gets("bind", "camera", "up")


def test_settings_loader():
    assert Game.Settings.gets("ui", "language") == ["en-us"]

    assert Game.Settings.gets("graphics", "resolution") == [
        dict(width=640, height=480),
        dict(width=1280, height=720),
        dict(width=1920, height=1080),
        dict(width=2560, height=1440),
        dict(width=3840, height=2160),
    ]


def test_data():
    print(Dev.Planets)
