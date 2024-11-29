class SceneManager:
    def __init__(self) -> None:
        self.stack = []

    @property
    def scene(self):
        """returns the top scene"""
        return self.stack[-1]

    def push_scene(self, *scene):
        """adds scene to stack, set its manager to self"""
        self.print()
        self.stack.append(*scene)

    def print(self):
        print("StackManager")
        for scene in reversed(self.stack):
            print(f"\t{scene.name}")

    def pop_scene(self):
        """removes the top scene"""
        self.stack.pop()

    # convenience methods for top scene

    def handle_input(self, events, pressed_keys) -> None:
        self.scene.handle_input(events, pressed_keys)

    def is_empty(self) -> bool:
        return len(self.stack) == 0

    def update(self):
        self.scene.update()

    def render(self, screen) -> None:
        self.scene.render(screen)
