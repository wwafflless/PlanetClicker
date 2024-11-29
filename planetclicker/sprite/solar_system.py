from pygame.sprite import Group
from pygame.surface import Surface
from planetclicker.sprite.circle.bg_star import BGStarSystem
from planetclicker.model.planet import Planet


class SolarSystem:
    def __init__(self, planets: list[Planet]):
        self.bg_stars = BGStarSystem(100)
        self.planets = Group([p.sprite for p in planets])

    def update(self):
        self.bg_stars.update()
        self.planets.update()

    def draw(self, surface: Surface):
        self.bg_stars.draw(surface)
        self.planets.draw(surface)
