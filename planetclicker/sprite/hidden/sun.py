from dataclasses import dataclass

from planetclicker.model.planet import Planet


@dataclass
class SolarSystem:
    suns: dict
    planets: dict

    def add_sun(self, sun: Sun):
        """Solar sytems can have multiple suns."""
        self.suns[sun.name] = sun

    def add_planet(self, planet: Planet):
        self.planets[planet.name] = planet
