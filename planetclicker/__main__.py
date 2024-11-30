"""__main__.py"""

import pygame

pygame.init()

from dataclasses import dataclass
from enum import StrEnum
from typing import Tuple

from pygame.rect import Rect

from planetclicker.data import Game
from planetclicker.level import (
    BlankLevel,
    ComplexLevel,
    IntroLevel,
    Level,
    NewLevel,
    SimpleLevel,
)
from planetclicker.scene.manager import SceneManager
from planetclicker.scene.title import TitleScene

RunMode = StrEnum("RunMode", ["development", "production"])


def main(mode: RunMode = RunMode.development):
    size: Tuple[int, int] = Game.Graphics.size
    clock: pygame.Clock = pygame.time.Clock()
    fps: int = Game.Graphics.fps

    screen = pygame.display.set_mode(size)
    scene_manager = SceneManager()
    scene_manager.push(TitleScene(scene_manager))

    title_text = Game.Font.title.render(
        text="game name",
        antialias=False,
        color=Game.Color.accent,
    )

    while True:
        """Update game state."""
        scene_manager.update()
        delta = clock.tick(fps) / 1000
        pressed_keys = pygame.key.get_pressed()
        """Render graphics."""
        scene_manager.render(screen)
        screen.fill(Game.Color.background)
        screen.blit(title_text, (0, 0))
        pygame.display.flip()

    # def handle_input(self, events, pressed_keys): ...

    #     # Event filtering
    #     filtered_events = []
    #     for event in pygame.event.get():
    #         quit_attempt = False
    #         if event.type == pygame.QUIT:
    #             quit_attempt = True
    #         elif event.type == pygame.KEYDOWN:
    #             alt_pressed = pressed_keys[pygame.K_LALT] or pressed_keys[pygame.K_RALT]
    #             if event.key == pygame.K_ESCAPE:
    #                 quit_attempt = True
    #             elif event.key == pygame.K_F4 and alt_pressed:
    #                 quit_attempt = True
    #         if quit_attempt:
    #             if scene_manager.is_empty():
    #                 pygame.quit()
    #                 return
    #             else:
    #                 scene_manager.pop_scene()
    #         else:
    #             filtered_events.append(event)

    #     scene_manager.handle_input(filtered_events, pressed_keys)
    #     scene_manager.update()
    #     scene_manager.render(screen)

    #     # active_scene = active_scene.next

    #     pygame.display.flip()
    #     clock.tick(fps)


if __name__ == "__main__":
    print(RunMode)
    main()