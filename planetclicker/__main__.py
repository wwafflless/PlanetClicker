import pygame

pygame.init()

from planetclicker.data import config
from planetclicker.game import GameController

if __name__ == "__main__":

    print("Loading config:\n")
    for k, v in config.items():
        print(f"{k} = {v}")

    game = GameController(**config)

    while True:
        # game.handle_input(filtered_events, pressed_keys) # TODO FIXME
        game.update()
        game.render(game.screen)
