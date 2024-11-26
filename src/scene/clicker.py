from datetime import datetime
from tkinter import SE

import pygame

from src.asset.color import Color
from src.asset.font import text_font
from src.data import data
from src.scene import Scene
from src.sprite.planet import PlanetSprite
from src.sprite.solar_system import SolarSystem
from src.ui.panel import Panel
from src.ui.uibutton import UIButton

#   because I don't know how to use the data file yet
ui_bg_color = (200, 200, 200, 255)
ui_unselected_color = (210, 210, 210, 255)
ui_highlight_color = (220, 220, 220, 255)

class ClickerScene(Scene):
    def __init__(self):
        super().__init__("clicker", manager=None)

        #self.test_text = text_font.render(
        #    data["ui"]["welcome_text"], False, (255, 255, 255)
        #)

        # planets group
        planets = []
        for planet_name, planet_props in data["planet"].items():
            planets.append(
                PlanetSprite(
                    name=planet_name,
                    **planet_props,
                )
            )
        self.solar_system = SolarSystem(planets)
        
        self.panel_buttons = []
        
        self.clicker_panel = Panel((0, 400), (800, 200), ui_bg_color)
        for i in range(4):
            next_button = UIButton((self.clicker_panel.pos[0] + (i * 200), self.clicker_panel.pos[1]), (200, 50), True, ui_unselected_color, (0, 0, 0, 0), ui_highlight_color)
            next_button.link(2, self.on_button_click)   # <-- ideally this 2 is an enum, I don't know how to best go about that in python sorry
            self.clicker_panel.add_child(next_button)
            self.panel_buttons.append(next_button)
        self.panel_buttons[0].selected = True
    
    #   makes them mutually exclusive
    def on_button_click(self, button, event):
        for b in self.panel_buttons:
            b.selected = False
        button.selected = True

    def handle_input(self, events, pressed_keys):
        self.clicker_panel.handle_input(events, pressed_keys)

    def update(self):
        self.clicker_panel.update()
        self.solar_system.update()

    def render(self, screen):
        screen.fill(Color.black)
        self.solar_system.draw(screen)
        #screen.blit(self.test_text, (0, 0))
        self.clicker_panel.draw(screen)
