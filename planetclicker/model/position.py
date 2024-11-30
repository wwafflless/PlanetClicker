from dataclasses import dataclass


@dataclass
class Position:
    """A 3D Vector"""

    _value: tuple[float, float, float]

    @property
    def x(self):
        return self._value[0]

    @property
    def y(self):
        return self._value[0]

    @property
    def z(self):
        return self._value[0]

    @property
    def length(self):
        """Magnitude of vector."""
        np.sqrt(self.x * self.x + self.y + self.y + self.z + self.z)  # TODO Optimize
