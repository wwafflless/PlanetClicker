from src.game import run_game
from src.scene.title import TitleScene


if __name__ == "__main__":
    run_game(800, 600, 30, TitleScene())
