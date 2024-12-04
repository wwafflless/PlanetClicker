from src.ui.uielement import UIElement

#   panel element, just a base ui element that has children, updates those children as well
class Panel(UIElement):
    def __init__(self, pos, width_height, color=None, label=""):
        super().__init__(pos, width_height, color, label)
        self.children = []

    #   also move children, necessary because positions aren't relative to parent
    def move(self, to_move):
        super().move(to_move)
        for child in self.children:
            child.move(to_move)

    def add_child(self, to_add):
        self.children.append(to_add)
        
    #   update children input
    def handle_input(self, events, pressed_keys):
        super().handle_input(events, pressed_keys)
        for child in self.children:
            child.handle_input(events, pressed_keys)

    #   update children
    def update(self):
        for child in self.children:
            child.update()
            
    #   draw children
    def draw(self, surface):
        super().draw(surface)
        for child in self.children:
            child.draw(surface)