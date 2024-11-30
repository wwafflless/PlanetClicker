from planetclicker.data import Game
from planetclicker.scene.scene import Scene


class SettingsScene(Scene):
    """
    The settings screen
    TODO
    - Volume
    - Controls
    - Back
    """

    def __init__(self, manager):
        super().__init__("settings", manager)
        # for k, v in settings.items():
        self.back_text = Game.Font.text.render(
            text="Back",
            antialias=False,
            color=Game.Color.text,
        )
        self.title_text = Game.Font.title.render(
            text="Settings",
            antialias=False,
            color=Game.Color.brand,
        )
        self.options = []
        for section in Game.Settings.all:
            section_text = Game.Font.text.render(
                text=section,
                antialias=False,
                color=Game.Color.text,
                wraplength=500,
            )
            # for k, v in settings.get(section, {}).items():
            #     option_text = text_font.render(
            #         text=f"{section}.{k}: {v}",
            #         antialias=False,
            #         color=GameColor.text,
            #         wraplength=500,
            #     )
            #     self.options.append((option_text, (100, 200 + 50 * len(self.options))))
            #
            #
            #
            #
            # if isinstance(v, list):
            #     v = v[0]
            # option_text = text_font.render(
            #     text=f"{k}: {v}",
            #     antialias=False,
            #     color=Color.text,
            #     wraplength=500,
            # )
            # self.options.append((option_text, (100, 200 + 50 * len(self.options))))

    def handle_input(self, events, pressed_keys):
        super().handle_input(events, pressed_keys)

    def update(self):
        pass

    def render(self, screen):
        screen.fill((0, 0, 0))
        screen.blit(self.back_text, (100, 50))
        screen.blit(self.title_text, (100, 100))
        for option, (x, y) in self.options:
            screen.blit(option, (x, y))
