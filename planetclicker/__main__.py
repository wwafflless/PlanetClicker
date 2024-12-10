"""__main__.py"""

import pygame

pygame.init()

from planetclicker.game import Game


def main():
    game = Game(debug=False)
    game.run()


if __name__ == "__main__":
    main()
