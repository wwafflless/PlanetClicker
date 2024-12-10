from pygame import Surface
import numpy as np
import pygame
from planetclicker.object3d.cube import Cube
from planetclicker.mmath import rotate_x, rotate_z
from planetclicker import Colors
from planetclicker.object3d.icosahedron import Icosahedron
from planetclicker.scene.scene import Scene


class GenerateScene(Scene):
    def __init__(self):
        super().__init__("generate")
        # self.obj = Cube([0.0, 0.0, 150.0])
        self.objs = [
            Cube([0.0, -200.0, 150.0]),
            Icosahedron([200.0, 0.0, 150.0]),
        ]
        self.tick = 0
        self.angles = [[1.0, 2.0], [3.0, 4.0]]

    def update(self, dt=0.1):
        self.tick += 1
        for i, obj in enumerate(self.objs):
            a, b = self.angles[i]
            obj.position[0] = np.sin(a * self.tick / 180.0) * 100.0
            obj.position[1] = np.cos(b * self.tick / 180.0) * 100.0
            obj.vertices = rotate_x(obj.vertices, a)
            obj.vertices = rotate_z(obj.vertices, b)

    def handle_input(self, events, pressed_keys):
        pass

    def render(self, surface: Surface):
        def project(vertex):
            """Project 3D vertex to 2D."""
            factor = 100.0 / (10.0 + vertex[2])
            x = vertex[0] * factor + surface.get_width() // 2
            y = -vertex[1] * factor + surface.get_height() // 2  # Invert y-axis
            return int(x), int(y)

        surface.fill(Colors.black)

        for obj in self.objs:
            obj.draw(surface)
            # projected_vertices = [project(v) for v in obj.vertices]
            # pygame.draw.polygon(surface, Colors.white, projected_vertices)
