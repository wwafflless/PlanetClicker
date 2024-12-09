"""__main__.py"""

import pygame

pygame.init()

from planetclicker import DEBUG
from planetclicker.game import Game


def main():
    if DEBUG:
        print("Starting Game from main()")
    game = Game()
    game.run()


if __name__ == "__main__":
    main()
