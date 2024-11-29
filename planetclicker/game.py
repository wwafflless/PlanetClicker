import pygame

from planetclicker.asset.color import Color

pygame.init()

from dataclasses import dataclass

from pygame.rect import Rect
from planetclicker.level import (
    Level,
    BlankLevel,
    IntroLevel,
    NewLevel,
    SimpleLevel,
    ComplexLevel,
)
from planetclicker.scene.manager import SceneManager
from planetclicker.asset.font import GameFont
from planetclicker.scene.title import TitleScene


@dataclass
class Game:
    rect: Rect
    fps: int = 60
    clock = pygame.Clock()

    def __postinit__(self):
        self.screen = pygame.display.set_mode(
            (self.rect[0], self.rect[1]),
        )

        self.levels: list[Level] = [
            BlankLevel,
            IntroLevel,
            NewLevel,
            SimpleLevel,
            ComplexLevel,
        ]
        self._current_level: int = 0
        self.scenes = SceneManager()
        self.scenes.push_scene(TitleScene(self.scenes))

    @property
    def current_level(self):
        return self.levels[self._current_level % len(self.levels)]

    def update(self):
        self.scenes.update()
        delta = self.clock.tick(60) / 1000
        pressed_keys = pygame.key.get_pressed()

        self.clock.tick(self.fps)

    def render(self, surface: pygame.Surface):
        self.scenes.render(surface)
        GameFont.title.render(
            text="game name",
            antialias=False,
            color=Color.accent,
        )
        pygame.display.flip()

    def handle_input(self, events, pressed_keys): ...

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
