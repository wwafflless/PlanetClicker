from planetclicker.scene.scene import Scene
from planetclicker.data import Game, Dev
from planetclicker.model.planet import Planet
from planetclicker.sprite.solar_system import SolarSystem
from planetclicker.sprite.animated_sprite import AnimatedSprite


class ClickerScene(Scene):
    def __init__(self):
        super().__init__("clicker", manager=None)

        self.test_text = Game.Font.text.render("welcome_text", False, (255, 255, 255))
        self.solar_system = SolarSystem([])

        for planet in Dev.Planets.all:
            sprite = AnimatedSprite(
                filename=f"asset/sheet/{planet.name}.png",
                width=10,
                height=10,
                frames=planet.get("sprite", "count"),
            )
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
        screen.fill(GameColor.black)
        screen.blit(self.test_text, (0, 0))
        for p in self.solar_system.planets:
            screen.blit(p.image, (0, 0))
