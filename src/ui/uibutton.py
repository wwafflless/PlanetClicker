import pygame
from src.ui.uielement import UIElement
from enum import Enum

#   ui button elements, could easily be split up into multiple button types
#   can be disabled and enabled, given different colors whether it's hovered, selected, or disabled
#   mouse input is handled through callbacks which are linked outside of the class, or could be overriden
class UIButton(UIElement):
    def __init__(self, pos, width_height, interactable=True, color=(0, 0, 0, 255), highlight_color=(134, 134, 134, 255), selected_color=(255, 255, 255, 255), disabled_color=(255, 0, 0, 255)):
        super().__init__(pos, width_height, color)
        self.interactable = interactable
        self.selected = False
        self.hovered = False
        self.draw_color = color
        self.selected_color = selected_color
        self.highlight_color = highlight_color
        self.disabled_color = disabled_color

        self.callbacks = [None, None, None, None]

    #   links a mouse action to a function outside of the class
    def link(self, link_to, callback):
        self.callbacks[link_to] = callback

    #   each mouse actions calls the corresponding callback if they have been linked
    def on_mouse_entered(self, event):
        if self.callbacks[0]:
            self.callbacks[0](self, event)
    def on_mouse_exited(self, event):
        if self.callbacks[1]:
            self.callbacks[1](self, event)
    def on_mouse_down(self, event):
        if self.callbacks[2]:
            self.callbacks[2](self, event)
    def on_mouse_up(self, event):
        if self.callbacks[3]:
            self.callbacks[3](self, event)

    def enable(self):
        self.interactable = True
    def disable(self):
        self.interactable = False
        self.selected = False
        self.hovered = False

    #   draws the corresponding color for the current mouse state
    def draw(self, surface):
        if not self.interactable:
            self.color = self.disabled_color
        elif self.selected:
            self.color = self.selected_color
        elif self.hovered:
            self.color = self.highlight_color
        else:
            self.color = self.draw_color
        super().draw(surface)

    #   calls the corresponding mouse actions if they happened
    def handle_input(self, events, pressed_keys):
        if not self.interactable:
            return
        for event in events:
            if event.type == pygame.MOUSEMOTION:
                if self.does_collide(event.pos):
                    if not self.hovered:
                        self.on_mouse_entered(event)
                        self.hovered = True
                else:
                    if self.hovered:
                        self.on_mouse_exited(event)
                        self.hovered = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.does_collide(event.pos):
                    self.on_mouse_down(event)
            elif event.type == pygame.MOUSEBUTTONUP:
                if self.does_collide(event.pos):
                    self.on_mouse_up(event)
    
    #   returns true if the point is within this button (whole screen coords)
    def does_collide(self, to_check) -> bool:
        return to_check[0] > self.pos[0] and to_check[1] > self.pos[1] and to_check[0] < self.pos[0] + self.width_height[0] and to_check[1] < self.pos[1] + self.width_height[1]