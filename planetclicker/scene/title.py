import pygame

from planetclicker.data import Game
from planetclicker.sprite.bg_star import BGStarSystem
from planetclicker.scene.scene import Scene
from planetclicker.scene.main import MainScene
from planetclicker.scene.settings import SettingsScene
from planetclicker.ui.button import UIButton


class TitleScene(Scene):
    """
    The title screen
    - Continue
    - New Game
    - Load Game
    - Settings
    """

    def __init__(self, manager):
        super().__init__(
            name="title",
            manager=manager,
        )
        self.particles = BGStarSystem(n=100)  # background animation
        self.title_text = Game.Font.title.render(
            Game.UI.title,
            False,
            Game.Color.brand,
        )
        self.instruction_text = Game.Font.text.render(
            "press ENTER to start",
            False,
            Game.Color.brand,
        )

        button_data: list[dict] = Game.UI.button

        self.buttons = []
        self.selected_button_index = 0
        for i in range(len(button_data)):
            new_button = UIButton(
                (400 - (75 / 2), 250 + (i * 30)),
                (75, 25),
                (255, 255, 255, 255),
                button_data[i]["text"],
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

        destinations = [MainScene, MainScene, MainScene, SettingsScene]

        self.manager.push(destinations[self.selected_button_index](self.manager))

    def handle_input(self, events, pressed_keys):
        for b in self.buttons:
            b.handle_input(events, pressed_keys)

        for event in events:
            match (event.type):
                case pygame.K_UP:
                    self.selected_button_index -= 1
                    self.selected_button_index %= len(self.buttons)
                    break
                case pygame.K_DOWN:
                    self.selected_button_index += 1
                    self.selected_button_index %= len(self.buttons)
                    self.buttons[self.selected_button_index]
                    break

    @property
    def selected_button(self):
        return self.buttons[self.selected_button_index]

    def update(self):
        self.particles.update()
        for b in self.buttons:
            b.update()

    def render(self, screen):
        screen.fill(Game.Color.background)
        self.particles.draw(screen)
        title_rect = self.title_text.get_rect()
        screen.blit(
            self.title_text,
            (
                self.rect.centerx - title_rect.centerx,
                self.rect.height // 3 - title_rect.centery,
            ),
        )
        for b in self.buttons:
            b.draw(screen)
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
