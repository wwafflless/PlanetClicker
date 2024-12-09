from pygame.surface import Surface
import pygame
from planetclicker.font import TextFont
from planetclicker.scene.scene import Scene
from planetclicker.model.solar_system import SolarSystem, Sun, Planet
from planetclicker.sprite.animated_sprite import AnimatedSprite


class ClickerScene(Scene):
    def __init__(self):
        super().__init__("clicker", game=None)

        self.test_text = TextFont.render("welcome_text", False, (255, 255, 255))

        self.solar_system = SolarSystem.simple()

        # if planet_datas := Dev.Planets.get("planets"):
        #     for planet_data in planet_datas:
        #         size = planet_data["sprite"]["rect"][2]
        #         sprite = AnimatedSprite(
        #             name=planet_data["sprite"]["name"],
        #             w=size,
        #             h=size,
        #             frames=planet_data["sprite"]["count"],
        #         )
        #         planet = Planet(
        #             sprite=sprite,
        #             physics=PhysicsComponent(
        #                 position=(400, 300, 0),
        #                 velocity=(1, 1, 0),
        #                 camera=(0, 0, 0),
        #                 mass=100,
        #             ),
        #         )
        #         print(planet)
        #         self.solar_system.planets.append(planet)

    def handle_input(self, events, pressed_keys): ...

    def update(self):
        for p in self.solar_system.planets:
            p.sprite.update()

    def render(self, surface: pygame.Surface):
        # surface.fill(Game.Color.black)
        # surface.blit(self.test_text, (0, 0))
        self.solar_system.draw(surface)
        for p in self.solar_system.planets:
            p.sprite.draw(surface)
