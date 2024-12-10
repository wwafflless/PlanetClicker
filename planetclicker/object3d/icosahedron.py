from planetclicker.object3d.object import Object3D
import numpy as np


class Icosahedron(Object3D):
    phi: float = (1 + np.sqrt(5)) / 2  # golden ratio
    vertices: list[list[float]] = [
        [-1, phi, 0],
        [1, phi, 0],
        [-1, -phi, 0],
        [1, -phi, 0],
        [0, -1, phi],
        [0, 1, phi],
        [0, -1, -phi],
        [0, 1, -phi],
        [phi, 0, -1],
        [phi, 0, 1],
        [-phi, 0, -1],
        [-phi, 0, 1],
    ]
    faces: list[list[int]] = [
        [0, 11, 5],
        [0, 5, 1],
        [0, 1, 7],
        [0, 7, 10],
        [0, 10, 11],
        [1, 5, 9],
        [5, 11, 4],
        [11, 10, 2],
        [10, 7, 6],
        [7, 1, 8],
        [3, 9, 4],
        [3, 4, 2],
        [3, 2, 6],
        [3, 6, 8],
        [3, 8, 9],
        [4, 9, 1],
        [2, 4, 11],
        [6, 2, 10],
        [8, 6, 7],
        [9, 8, 1],
    ]

    def __init__(self, position):
        edges = []
        for face in Icosahedron.faces:
            for v in face:
                edges.append([v, face[(v + 1) % len(face)]])

        return super().__init__(
            Icosahedron.vertices,
            edges,
            Icosahedron.faces,
            position,
        )
