class Scene:
    def __init__(self, scene_name):
        self.next = self
        self.name = scene_name

    def handle_input(self, events, pressed_keys) -> None:
        raise Exception("Implement handle_input in subclass")

    def update(self) -> None:
        raise Exception("Implement update in subclass")

    def render(self, screen) -> None:
        raise Exception("Implement render in subclass")

    def switch(self, next_scene) -> None:
        self.next = next_scene

    def kill(self) -> None:
        self.switch(None)
