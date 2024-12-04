import pygame
from src.ui.uielement import UIElement

#   makes another uielement scrollable, the viewable bounds defined by this element
#   current only vertical scroll implemented
class ScrollRect(UIElement):
    def __init__(self, pos, width_height, content):
        super().__init__(pos, width_height, None, "", (0,0,0,0))
        self.content = content
        
    #   updates content
    def update(self):
        self.content.update()

    #   moves content on mouse scroll, clamped to content's height
    #   then pass input to content
    def handle_input(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.MOUSEWHEEL:
                diff = event.y * 2
                
                if self.content.pos[1] + diff > self.pos[1]:
                    diff = self.pos[1] - (self.content.pos[1])
                elif self.content.pos[1] + self.content.width_height[1] + diff < self.pos[1] + self.width_height[1]:
                    diff = (self.pos[1] + self.width_height[1]) - (self.content.pos[1] + self.content.width_height[1])
                
                self.content.move((0, diff))
                
        self.content.handle_input(events, pressed_keys)
                
    #   draw content clipped to this element's bounds
    def draw(self, surface):
        surface.set_clip((self.pos[0], self.pos[1], self.width_height[0], self.width_height[1]))
        self.content.draw(surface)
        surface.set_clip(None)