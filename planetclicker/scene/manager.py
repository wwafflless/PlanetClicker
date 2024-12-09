from planetclicker.scene import Scene


from planetclicker.util import singleton


@singleton
class SceneManager:

    def __init__(self, *scenes: Scene) -> None:
        self.stack = []
        for scene in scenes:
            self.push(scene)

    @property
    def top(self):
        """returns the top scene"""
        if self.stack:
            return self.stack[-1]
        raise ValueError("No scene found")

    def push(self, scene: Scene):
        """adds scene to stack, set its manager to self"""
        # scene.manager = self # do we need this?
        self.stack.append(scene)

    def print(self):
        print("SceneManager stack:")
        for scene in reversed(self.stack):
            print(f"\t{scene.name}")

    def pop(self):
        """removes the top scene"""
        self.stack.pop()

    def handle_input(self, events, pressed_keys) -> None:
        self.top.handle_input(events, pressed_keys)

    def is_empty(self) -> bool:
        return len(self.stack) == 0

    def update(self):
        self.top.update()

    def render(self, screen) -> None:
        self.top.render(screen)
