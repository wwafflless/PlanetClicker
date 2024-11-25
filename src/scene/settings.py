from src.scene import Scene
from src.asset.color import Color
from src.asset.font import text_font, title_font
from src.data import settings


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
        self.back_text = text_font.render(
            text="Back",
            antialias=False,
            color=Color.text,
        )
        self.title_text = title_font.render(
            text="Settings",
            antialias=False,
            color=Color.brand,
        )
        self.options = []
        for section in settings.keys():
            section_text = text_font.render(
                text=section,
                antialias=False,
                color=Color.text,
                wraplength=500,
            )
            for k, v in settings.get(section, {}).items():
                option_text = text_font.render(
                    text=f"{section}.{k}: {v}",
                    antialias=False,
                    color=Color.text,
                    wraplength=500,
                )
                self.options.append((option_text, (100, 200 + 50 * len(self.options))))
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
