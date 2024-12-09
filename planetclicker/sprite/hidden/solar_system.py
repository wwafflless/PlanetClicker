from pygame.surface import Surface
from planetclicker.sprite.bg_star import BGStarSystem
from planetclicker.model.planet import Planet


class SolarSystem:
    def __init__(self, planets: list[Planet]):
        self.bg_stars = BGStarSystem(100)
        self.planets = planets

    def update(self):
        self.bg_stars.update()
        for p in self.planets:
            p.sprite.update()

    def draw(self, surface: Surface):
        self.bg_stars.draw(surface)
        for p in self.planets:
            p.sprite.draw(surface)
