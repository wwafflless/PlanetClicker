import pygame

pygame.init()
import pprint

from src.data import Dev, Game


def test_color():
    assert Game.Color.black is not None
    assert Game.Color.text is not None


def test_font():
    fonts = Game.Font.fonts
    pprint.pp("hi")
    print(Game.Font)
    pprint.pp(fonts)


def test_dev():
    assert Dev.Planets is not None
