import pygame

#   base ui element, just has a position, size, and color
class UIElement():
    def __init__(self, pos, width_height, color=None):
        self.pos = pos
        self.width_height = width_height
        if color:
            self.color = color
        else:
            self.color = (255, 0, 0, 255)
    
    def update(self):
        pass
        
    def handle_input(self, events, pressed_keys):
        pass

    def draw(self, surface):
        #   subsurface to support transparency
        subsurface = pygame.Surface((self.width_height[0], self.width_height[1]))
        subsurface.set_alpha(self.color[3])
        subsurface.fill(self.color)
        
        surface.blit(subsurface, (self.pos[0],self.pos[1]))