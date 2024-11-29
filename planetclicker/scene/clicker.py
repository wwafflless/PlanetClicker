from planetclicker.asset.color import Color
from planetclicker.asset.font import GameFont
from planetclicker.asset.spritesheet import AnimatedSprite
from planetclicker.scene import Scene
from planetclicker.data import planets, config
from planetclicker.model.planet import Planet
from planetclicker.sprite.solar_system import SolarSystem


class ClickerScene(Scene):
    def __init__(self):
        super().__init__("clicker", manager=None)

        self.test_text = GameFont.text.render(
            config.gets("ui", "welcome_text"), False, (255, 255, 255)
        )
        # self.solar_system = SolarSystem(Planet.from_game_data())
        self.solar_system = SolarSystem(
            [
                # Planet.make(
                #     "sun",
                #     "Sun",
                #     51,
                #     51,
                #     (0, 0, 0),
                #     (1, 0, 0),
                #     200,
                # ),
            ]
        )

        for planet in planets.get("planet"):
            # planet = Planet.from_game_data(planet["name"])
            s_name = planet.get("sprite", "name")
            s_rect = planet.get("sprite", "rect")

            # sprite = AnimatedSprite(
            #     filename=f"asset/sheet/{s_name}.png",
            #     rect=(0, 0, 10, 10),
            #     # rect=s_rect,
            #     count=planet.get("sprite", "count"),
            # )
            ps = Planet(
                _value=(0, planet.get("orbit_radius"), 0),
                **planet,
                sprite=sprite,
            )
            self.solar_system.planets.add(ps.sprite)

    def handle_input(self, events, pressed_keys): ...

    def update(self):
        for p in self.solar_system.planets:
            p.update()

    def render(self, screen):
        screen.fill(Color.black)
        screen.blit(self.test_text, (0, 0))
        for p in self.solar_system.planets:
            p.draw(screen)
