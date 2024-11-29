from planetclicker.data import Dev, Game
import pprint

import pygame


def test_color():
    assert Game.Color.black is not None
    assert Game.Color.text is not None


def test_font():
    fonts = Game.Font.get("font")
    pprint.pp("hi")
    print(Game.Font)


def test_dev():
    assert Dev.Planets is not None
