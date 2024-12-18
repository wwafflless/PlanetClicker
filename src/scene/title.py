from dataclasses import dataclass
from struct import calcsize
from typing import Callable, ForwardRef

import pygame

from src.asset.color import Color
from src.asset.font import text_font, title_font
from src.data import config
from src.particle.bg_star import BGStarSystem
from src.scene import Scene
from src.scene.main import MainScene
from src.scene.settings import SettingsScene
from src.ui.button import Button
from src.ui.uibutton import UIButton


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
        self.title_text = title_font.render(
            config.get("title"),
            False,
            Color.brand,
        )
        self.instruction_text = text_font.render(
            "Press ENTER to start",
            False,
            Color.accent,
        )

        button_texts = ["continue", "new game", "load game", "settings"]
        
        #"""
        self.buttons = []
        for i in range(len(button_texts)):
            new_button = UIButton((400-(75/2), 250 + (i * 30)), (75, 25), (255, 255, 255, 255), button_texts[i], True, (43, 127, 148, 255), (0, 0, 0, 0), (0, 0, 0, 0), True)
            new_button.link(2, self.click_button)
            self.buttons.append(new_button)
        #"""
        """
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
        """
        #self.selected_button = self.buttons[0]
        
    #def select_button(self, offset: int):
    #    index = (self.buttons.index(self.selected_button) + offset) % len(self.buttons)
    #    self.selected_button = self.buttons[index]

    def click_button(self, button, event):
        for i in range(len(self.buttons)):
            if button == self.buttons[i]:
                clicked_index = i    
        
        destinations = [MainScene, MainScene, MainScene, SettingsScene]
        
        self.manager.push_scene(destinations[clicked_index](self.manager))
        

    def handle_input(self, events, pressed_keys):
        for b in self.buttons:
            b.handle_input(events, pressed_keys)
        """
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
                    """

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
