from datetime import datetime
from tkinter import SE

import pygame
import random

from src.asset.color import Color
from src.data import data
from src.scene import Scene
from src.sprite.planet import PlanetSprite
from src.sprite.solar_system import SolarSystem
from src.ui.panel import Panel
from src.ui.uibutton import UIButton

#   because I don't know how to use the data file yet
ui_bg_color = (100, 100, 100, 155)
ui_unselected_color = (110, 110, 110, 155)
ui_highlight_color = (120, 120, 120, 155)

class ClickerScene(Scene):
    def __init__(self):
        super().__init__("clicker", manager=None)

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
            label = ""
            if i == 0:
                label = "planets"
            next_button = UIButton((self.clicker_panel.pos[0] + (i * 200), self.clicker_panel.pos[1]), (200, 25), ui_unselected_color, label, (i==0), ui_highlight_color, (0, 0, 0, 0), ui_unselected_color)
            next_button.link(2, self.panel_button_click)   # <-- ideally this 2 is an enum, I don't know how to best go about that in python sorry
            self.clicker_panel.add_child(next_button)
            self.panel_buttons.append(next_button)
        self.panel_buttons[0].selected = True
        
        self.tab_panels = []
        self.tab_buttons = []
        
        for i in range(4):
            new_tab = Panel((self.clicker_panel.pos[0],self.clicker_panel.pos[1] + self.panel_buttons[0].width_height[1]), (self.clicker_panel.width_height[0],self.clicker_panel.width_height[1] - self.panel_buttons[0].width_height[1]), (0, 0, 0, 0))
            tab_button = UIButton((random.randint(0, 700), random.randint(450, 500)), (100, 100), (0, 255, 255, 255), "", True, (134, 255, 255, 255))
            tab_button.link(2, self.tab_button_click)
            self.tab_buttons.append(tab_button)
            new_tab.add_child(tab_button)
            self.tab_panels.append(new_tab)
        self.current_tab = self.tab_panels[0]
    
    #   makes them mutually exclusive
    def panel_button_click(self, button, event):
        for i in range(len(self.panel_buttons)):
            if self.panel_buttons[i] == button:
                clicked_index = i
        
        if not self.panel_buttons[clicked_index].selected:
            for b in self.panel_buttons:
                b.selected = False
            button.selected = True
            
            self.current_tab = self.tab_panels[clicked_index]

    def tab_button_click(self, button, event):
        for i in range(len(self.tab_buttons)):
            if self.tab_buttons[i] == button:
                clicked_index = i
               
        if clicked_index < 3:
            panel_labels = ["planets", "zodiac", "stars", "your mom"]
            self.panel_buttons[clicked_index+1].enable()
            self.panel_buttons[clicked_index+1].label = panel_labels[clicked_index+1]

        test_texts = ["Adam, don't click me.", "Adam, leave me alone please.", "Seriously, Adam, stop.", "You clicked me, I get it!"]
        print(test_texts[random.randint(0, len(test_texts)-1)])

    def handle_input(self, events, pressed_keys):
        self.current_tab.handle_input(events, pressed_keys)
        self.clicker_panel.handle_input(events, pressed_keys)

    def update(self):
        self.current_tab.update()
        self.clicker_panel.update()
        self.solar_system.update()

    def render(self, screen):
        screen.fill(Color.black)
        self.solar_system.draw(screen)
        self.clicker_panel.draw(screen)
        self.current_tab.draw(screen)
