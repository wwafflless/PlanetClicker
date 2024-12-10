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
from src.ui.uielement import UIElement
from src.ui.scrollrect import ScrollRect

#   because I don't know how to use the data file yet
ui_bg_color = (100, 100, 100, 155)
ui_unselected_color = (110, 110, 110, 155)
ui_highlight_color = (120, 120, 120, 155)

class ClickerScene(Scene):
    def __init__(self):
        super().__init__("clicker", manager=None)

        # planets group
        self.planets = []
        for planet_name, planet_props in data["planet"].items():
            new_planet = PlanetSprite(
                             name=planet_name,
                             **planet_props,
                         )
            new_planet.on_orbit = self.on_planet_orbit
            self.planets.append(new_planet)
        self.solar_system = SolarSystem([self.planets[0]])
        
        for i in range(1, len(self.planets)):
            self.planets[i].cost = pow(10, i-1)  # <-- ideally this is inside the previous loop, but I don't know how to edit it sorry!
        
        self.tab_buttons = []
        
        self.clicker_panel = Panel((0, 400), (800, 200), ui_bg_color)
        for i in range(4):
            label = ""
            if i == 0:
                label = "planets"
            next_button = UIButton((self.clicker_panel.pos[0] + (i * 200), self.clicker_panel.pos[1]), (200, 25), ui_unselected_color, label, (i==0), ui_highlight_color, (0, 0, 0, 0), ui_unselected_color)
            next_button.link(2, self.tab_button_click)   # <-- ideally this 2 is an enum, but I don't know how to best go about that in python sorry!
            self.clicker_panel.add_child(next_button)
            self.tab_buttons.append(next_button)
        self.tab_buttons[0].selected = True
        
        self.tab_panels = []
        
        self.planet_buttons = []
        self.planet_labels = []
        
        for i in range(4):
            new_tab = Panel((self.clicker_panel.pos[0],self.clicker_panel.pos[1] + self.tab_buttons[0].width_height[1]), (self.clicker_panel.width_height[0],375), (0, 0, 0, 0))
            self.tab_panels.append(new_tab)
        
        for i in range(5):
            label_color = (134, 134, 134, 255)
            if i==0: label_color = (255, 255, 255, 255)
            planet_label = UIElement((self.tab_panels[0].pos[0] + 125, self.tab_panels[0].pos[1] + (75 * i) + 15), (100, 50), (0,0,0,0), "level: 0\ncost: 0", (134, 134, 134, 255))
            self.planet_labels.append(planet_label)            

            planet_names = ["moon", "mercury", "venus", "earth", "mars", "jupiter", "saturn"]   # <-- ideally this is from the data file, but I don't know how to use it sorry!
                
            planet_button_pos = (self.tab_panels[0].pos[0] + 25, self.tab_panels[0].pos[1] + (75 * i) + 15)
            planet_button_size = (100, 50)

            self.tab_panels[0].add_child(UIElement((planet_button_pos[0] - 2, planet_button_pos[1] + 2), planet_button_size, (134, 134, 134, 255)))

            planet_button = UIButton(planet_button_pos, planet_button_size, (255, 255, 255, 255), planet_names[i], True, (220, 255, 255, 255), (220, 255, 255, 255), (134, 134, 134, 255))
            planet_button.text_color = (0, 0, 0, 255)
            planet_button.link(1, self.planet_button_exit)
            planet_button.link(2, self.planet_button_down)
            planet_button.link(3, self.planet_button_up)
            self.planet_buttons.append(planet_button)
            
            self.tab_panels[0].add_child(planet_button)
            self.tab_panels[0].add_child(planet_label)
    
        self.tab_panels[0] = ScrollRect(self.tab_panels[0].pos, (self.clicker_panel.width_height[0],self.clicker_panel.width_height[1] - self.tab_buttons[0].width_height[1]), self.tab_panels[0])
        self.current_tab = self.tab_panels[0]

        self.years = 0
        self.year_label = UIElement((0, 10), (100, 25), (0,0,0,0), "years: " + str(self.years))
        
        self.planet_button_down(self.planet_buttons[0], None)
        self.planet_button_up(self.planet_buttons[0], None)
    
    #   makes them mutually exclusive
    def tab_button_click(self, button, event):
        for i in range(len(self.tab_buttons)):
            if self.tab_buttons[i] == button:
                clicked_index = i
        
        if not self.tab_buttons[clicked_index].selected:
            for b in self.tab_buttons:
                b.selected = False
            button.selected = True
            
            self.current_tab = self.tab_panels[clicked_index]
            
    def planet_button_exit(self, button, event):
        button.selected = False
    def planet_button_down(self, button, event):
        button.selected = True
    def planet_button_up(self, button, event):
        if(button.selected):
            button.selected = False
        else:
            return

        for i in range(len(self.planet_buttons)):
            if self.planet_buttons[i] == button:
                clicked_index = i
               
        planet = self.planets[clicked_index + 1]
        if not planet.enabled:
            if clicked_index + 1 < len(self.planets):
                self.planet_labels[clicked_index].text_color = (255, 255, 255, 255)
                planet.enabled = True
                planet.value = 1
                self.solar_system.add_planet(self.planets[clicked_index + 1])
                
                if(clicked_index + 1 == 4):
                    self.tab_buttons[1].enable()
                    self.tab_buttons[1].label = "star"
        else:
            planet.value += 1
            self.years -= planet.cost

    def on_planet_orbit(self, planet, value):
        self.years += value

    def handle_input(self, events, pressed_keys):
        self.current_tab.handle_input(events, pressed_keys)
        self.clicker_panel.handle_input(events, pressed_keys)

    def update(self):
        for i in range(len(self.planet_labels)):
            if self.planet_buttons[i].interactable:
                if self.years < self.planets[i+1].cost:
                    self.planet_buttons[i].disable()
            else:
                if self.years >= self.planets[i+1].cost:
                    self.planet_buttons[i].enable()
                
            if self.planet_buttons[i].selected or not self.planet_buttons[i].interactable:
                self.planet_buttons[i].draw_offset = (-2, 2)
            else:
                self.planet_buttons[i].draw_offset = (0, 0)
                
            self.planet_labels[i].label = "level: " + str(self.planets[i+1].value) + "\ncost: " + str(self.planets[i+1].cost)

        self.current_tab.update()
        self.clicker_panel.update()
        self.solar_system.update()
        self.year_label.label = "years: " + str(self.years)

    def render(self, screen):
        screen.fill(Color.black)
        self.solar_system.draw(screen)
        self.clicker_panel.draw(screen)
        self.current_tab.draw(screen)
        self.year_label.draw(screen)
