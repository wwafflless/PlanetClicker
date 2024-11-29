import pygame

pygame.init()

from planetclicker.data import ConfigLoader
from planetclicker.game import Game


def main():
    print("Loading config:\n")
    cl = ConfigLoader("data/config.toml")
    for k, v in cl.data.items():
        print(f"{k} = {v}")

    game = Game(**config.data)

    while True:
        # game.handle_input(filtered_events, pressed_keys) # TODO FIXME
        game.update()
        game.render(game.screen)


if __name__ == "__main__":
    main()
