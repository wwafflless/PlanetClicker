# pip install numpy matplotlib noise
from typing import Sequence
import pygame
import numpy as np
from planetclicker.mmath import rotate_x, rotate_z

from noise import snoise3


def apply_perlin_noise(vertices, scale=2.0, octaves=6):
    """Apply Perlin noise to the vertices."""
    for i, vertex in enumerate(vertices):
        noise_value = snoise3(
            vertex[0] / scale, vertex[1] / scale, vertex[2] / scale, octaves
        )
        vertex = np.array(vertex)
        vertices[i] = vertex * (
            1 + 0.2 * noise_value
        )  # Scale noise to adjust displacement
    return vertices


class Object3D:
    def __init__(
        self,
        vertices: list[list[float]],
        edges: list[list[int]],
        faces: list[list[int]],
        position: list[float],
    ) -> None:
        self.vertices = vertices
        self.edges = edges
        self.faces = faces
        self.position = position
        self.vertices = apply_perlin_noise(self.vertices)

    def draw(self, surface: pygame.Surface) -> None:
        focal_length = 400.0
        halfWidth = surface.get_width() / 2
        halfHeight = surface.get_height() / 2
        verts = [
            [o[u] * 10 + self.position[u] for u in range(3)] for o in self.vertices
        ]
        for edge in self.edges:
            point1Div = verts[edge[0]][2] / focal_length
            if point1Div == 0:
                continue
            point2Div = verts[edge[1]][2] / focal_length
            if point2Div == 0:
                continue
            point1 = [
                verts[edge[0]][0] / point1Div + halfWidth,
                verts[edge[0]][1] / point1Div + halfHeight,
            ]
            point2 = [
                verts[edge[1]][0] / point2Div + halfWidth,
                verts[edge[1]][1] / point2Div + halfHeight,
            ]
            pygame.draw.line(surface, (255, 255, 255), point1, point2, width=2)
