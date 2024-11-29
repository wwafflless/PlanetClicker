import pygame

from src.asset.font import text_font

#   base ui element, has a position, size, color, and label
class UIElement():
    def __init__(self, pos, width_height, color=None, label="", text_color=(255, 255, 255, 255)):
        self.pos = pos
        self.width_height = width_height
        if color:
            self.color = color
        else:
            self.color = (255, 0, 0, 255)
            
        self.label = label
        self.text_color = text_color

        self.test_text = text_font.render(label, False, text_color)
        self.test_text.set_alpha(text_color[3])
    
    def update(self):
        pass
        
    def handle_input(self, events, pressed_keys):
        pass

    def draw(self, surface):
        #   subsurface to support transparency
        subsurface = pygame.Surface((self.width_height[0], self.width_height[1]))
        subsurface.set_alpha(self.color[3])
        subsurface.fill(self.color)
        
        surface.blit(subsurface, self.pos)
        
        #   rerender in case label or text color change
        self.test_text = text_font.render(self.label, False, self.text_color)
        self.test_text.set_alpha(self.text_color[3])
        
        text_width = self.test_text.get_width()
        text_height = self.test_text.get_height()
        #   always center text
        text_pos = (self.pos[0] + ((self.width_height[0] - text_width) / 2), self.pos[1] + ((self.width_height[1] - text_height) / 2))
        
        surface.blit(self.test_text, text_pos)