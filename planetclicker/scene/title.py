import pygame

from planetclicker.scene.manager import SceneManager
from planetclicker import Colors
from planetclicker.font import TextFont, TitleFont
from planetclicker.scene.main import MainScene
from planetclicker.scene.scene import Scene
from planetclicker.scene.generate import GenerateScene
from planetclicker.scene.settings import SettingsScene
from planetclicker.sprite.bg_star import BGStarSystem
from planetclicker.ui.button import UIButton


class TitleScene(Scene):
    """
    The title screen
    - Continue
    - New Game
    - Load Game
    - Settings
    """

    def __init__(self):
        super().__init__(
            name="title",
        )
        self.particles = BGStarSystem(n=500, size=(1600, 900))  # background animation
        self.title_text = TitleFont.render(
            text="Planet Clicker",
            # antialias=False,
            color=Colors.brand,
        )

        button_texts = [
            # "continue",
            "new game",
            "generate",
            "settings",
        ]

        self.buttons: list[UIButton] = []
        self.selected_button_index = 0
        for i in range(len(button_texts)):
            new_button = UIButton(
                (400 - (75 / 2), 450 + (i * 30)),
                (125, 25),
                (255, 255, 255, 100),
                button_texts[i],
                True,
                (43, 127, 148, 255),
                # (0, 0, 0, 0),
                # (0, 0, 0, 0),
                # True,
            )
            new_button.link(2, self.click_button)
            self.buttons.append(new_button)

    def click_button(self, button, event):

        for i, button in enumerate(self.buttons):
            if button == self.buttons[i]:
                self.selected_button_index = i
                button.selected = True
                break

        destinations = [
            # MainScene,
            MainScene,
            GenerateScene,
            SettingsScene,
        ]

        SceneManager().push(destinations[self.selected_button_index]())

    def handle_input(self, events, pressed_keys):

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    print("pressed enter")
                    self.click_button(self.selected_button, event)
                    break

                elif event.key == pygame.K_DOWN:
                    self.select_button(1)
                    break
                elif event.key == pygame.K_UP:
                    self.select_button(-1)
                    break
        for b in self.buttons:
            b.handle_input(events, pressed_keys)

    @property
    def selected_button(self):
        return self.buttons[self.selected_button_index]

    def select_button(self, dir):
        for button in self.buttons:
            button.selected = False
        self.selected_button_index += dir + len(self.buttons)
        self.selected_button_index %= len(self.buttons)
        self.buttons[self.selected_button_index].selected = True

    def update(self):
        self.particles.update()
        for b in self.buttons:
            b.update()

    def render(self, surface: pygame.Surface):
        surface.fill(Colors.background)
        self.particles.draw(surface)
        rect = surface.get_rect()
        surface.blit(
            self.title_text,
            (
                rect.centerx - self.title_text.get_rect().centerx,
                rect.height // 3,
            ),
        )
        for b in self.buttons:
            b.pos = (rect.centerx, b.pos[1])
            b.draw(surface)
