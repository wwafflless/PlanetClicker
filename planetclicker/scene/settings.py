from pygame import Surface
from planetclicker import Colors
from planetclicker.font import TextFont
from planetclicker.scene.scene import Scene


class SettingsScene(Scene):
    """
    The settings screen
    """

    def __init__(self):
        super().__init__("settings")
        # for k, v in settings.items():
        self.back_text = TextFont.render(
            text="Back",
            antialias=False,
            color=Colors.text,
        )
        self.title_text = TextFont.render(
            text="Settings",
            antialias=False,
            color=Colors.brand,
        )
        self.options = []
        # for section in Settings.all:
        #     section_text = TextFont.render(
        #         text=section,
        #         antialias=False,
        #         color=Game.Color.text,
        #         wraplength=500,
        #     )
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

    def render(self, surface: Surface):
        surface.fill((0, 0, 0))
        surface.blit(self.back_text, (100, 50))
        surface.blit(self.title_text, (100, 100))
        for option, (x, y) in self.options:
            surface.blit(option, (x, y))
