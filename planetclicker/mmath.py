import numpy as np


def rotate_x(matrix, angle):
    theta = np.radians(angle)
    rotation_matrix = np.array(
        [
            [1, 0, 0],
            [0, np.cos(theta), -np.sin(theta)],
            [0, np.sin(theta), np.cos(theta)],
        ]
    )
    return np.dot(matrix, rotation_matrix.T)


def rotate_y(matrix, angle):
    theta = np.radians(angle)
    rotation_matrix = np.array(
        [
            [np.cos(theta), 0, np.sin(theta)],
            [0, 1, 0],
            [-np.sin(theta), 0, np.cos(theta)],
        ]
    )

    return np.dot(matrix, rotation_matrix.T)


def rotate_z(matrix, angle):
    theta = np.radians(angle)
    rotation_matrix = np.array(
        [
            [np.cos(theta), -np.sin(theta), 0],
            [np.sin(theta), np.cos(theta), 0],
            [0, 0, 1],
        ]
    )

    return np.dot(matrix, rotation_matrix.T)
