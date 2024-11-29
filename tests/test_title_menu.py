import pygame

pygame.init()
from planetclicker.game import Game
from planetclicker.scene.title import TitleScene
from planetclicker.data import config

# from planetclicker.data import config


def test_title_menu():
    game = Game(rect=config.get("rect"))
    screen = pygame.display.set_mode((400, 300))
    game.scenes.push_scene(TitleScene)
    while True:
        game.update()
        game.render(screen)
