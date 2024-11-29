import pygame

from planetclicker.scene.manager import SceneManager
from planetclicker.asset.color import Color
from planetclicker.asset.font import GameFont
from planetclicker.data import config
from planetclicker.scene import Scene
from planetclicker.scene.main import MainScene
from planetclicker.scene.settings import SettingsScene
from planetclicker.sprite.circle.bg_star import BGStarSystem
from planetclicker.ui.button import Button


class TitleScene(Scene):
    """
    The title screen
    - Continue
    - New Game
    - Load Game
    - Settings
    """

    def __init__(self, manager: SceneManager):
        super().__init__(
            name="title",
            manager=manager,
        )
        self.particles = BGStarSystem(n=100)  # background animation
        self.title_text = GameFont.title.render(
            config.get("title"),
            False,
            Color.brand,
        )
        self.instruction_text = GameFont.text.render(
            "Press ENTER to start",
            False,
            Color.accent,
        )

        self.buttons = [
            Button(
                text="continue",
                scene=MainScene,
            ),
            Button(
                text="new game",
                scene=MainScene,
            ),
            Button(
                text="load game",
                scene=MainScene,
            ),
            Button(
                text="settings",
                scene=SettingsScene,
            ),
        ]
        self.selected_button = self.buttons[0]

    def select_button(self, offset: int):
        index = (self.buttons.index(self.selected_button) + offset) % len(self.buttons)
        self.selected_button = self.buttons[index]

    def handle_input(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.select_button(-1)
                if event.key == pygame.K_DOWN:
                    self.select_button(1)
                if event.key == pygame.K_RETURN:
                    scene = self.selected_button.scene
                    self.manager.push_scene(
                        self.selected_button.scene(self.manager),
                    )

    def update(self):
        self.particles.update()

    def render(self, screen):
        screen.fill(Color.background)
        self.particles.draw(screen)
        title_rect = self.title_text.get_rect()
        instruction_rect = self.instruction_text.get_rect()
        screen.blit(
            self.title_text,
            (
                self.rect.centerx - title_rect.centerx,
                self.rect.height // 3 - title_rect.centery,
            ),
        )
        for i, button in enumerate(self.buttons):
            color = Color.accent if button == self.selected_button else Color.text
            screen.blit(
                GameFont.text.render(button.text, False, color),
                (
                    self.rect.centerx - GameFont.text.size(button.text)[0] // 2,
                    self.rect.height // 2 + i * 20,
                ),
            )
