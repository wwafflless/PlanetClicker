import pygame

from planetclicker.scene.manager import SceneManager
from planetclicker import Colors
from planetclicker.font import TextFont, TitleFont
from planetclicker.scene.main import MainScene
from planetclicker.scene.scene import Scene
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
            # "load game",
            "settings",
        ]

        self.buttons = []
        self.selected_button_index = 0
        for i in range(len(button_texts)):
            new_button = UIButton(
                (400 - (75 / 2), 250 + (i * 30)),
                (75, 25),
                (255, 255, 255, 255),
                button_texts[i],
                True,
                (43, 127, 148, 255),
                (0, 0, 0, 0),
                (0, 0, 0, 0),
                True,
            )
            new_button.link(2, self.click_button)
            self.buttons.append(new_button)

    def click_button(self, button, event):

        for i, button in enumerate(self.buttons):
            if button == self.buttons[i]:
                self.selected_button_index = i
                break

        destinations = [
            # MainScene,
            MainScene,
            # MainScene,
            SettingsScene,
        ]

        SceneManager().push(destinations[self.selected_button_index]())  # TODO

    def handle_input(self, events, pressed_keys):
        for b in self.buttons:
            b.handle_input(events, pressed_keys)

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    print("pressed enter")
                    self.click_button(self.selected_button, event)
                    break

            # match (event.type):
            #     case pygame.KEYDOWN:
            #         match event.key:
            #             case pygame.K_UP:
            #                 print("pressed up")
            #                 self.selected_button_index -= 1
            #                 self.selected_button_index %= len(self.buttons)
            #                 break
            #             case pygame.K_DOWN:
            #                 self.selected_button_index += 1
            #                 self.selected_button_index %= len(self.buttons)
            #                 self.buttons[self.selected_button_index]
            #                 break

    @property
    def selected_button(self):
        return self.buttons[self.selected_button_index]

    def update(self):
        self.particles.update()
        for b in self.buttons:
            b.update()

    def render(self, surface: pygame.Surface):
        surface.fill(Colors.background)
        self.particles.draw(surface)
        title_rect = self.title_text.get_rect()
        surface.blit(
            self.title_text,
            (
                self.rect.centerx - title_rect.centerx,
                self.rect.height // 3 - title_rect.centery,
            ),
        )
        for b in self.buttons:
            b.draw(surface)
        """
        for i, button in enumerate(self.buttons):
            color = Color.accent if button == self.selected_button else Color.text
            screen.blit(
                text_font.render(button.text, False, color),
                (
                    self.rect.centerx - text_font.size(button.text)[0] // 2,
                    self.rect.height // 2 + i * 20,
                ),
            )
            """
