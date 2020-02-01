import numpy as np


def faces():
    """Quadratic faces for an F-shaped object."""
    top = np.array([[1, 1, 1], [-1, 1, 1], [-1, -1, 1], [1, -1, 1]])
    north = np.array([[1,  1, -1], [-1,  1, -1], [-1,  1,  1], [1,  1,  1]])
    east = np.array([[1,  1, -1], [1,  1,  1], [1, -1,  1], [1, -1, -1]])
    south = np.array([[1, -1,  1], [-1, -1,  1], [-1, -1, -1], [1, -1, -1]])
    west = np.array([[-1,  1,  1], [-1,  1, -1], [-1, -1, -1], [-1, -1,  1]])
    bottom = np.array([[-1,  1, -1], [1,  1, -1], [1, -1, -1], [-1, -1, -1]])
    origin = np.array([0, 0, 0])
    p = origin + [0, 0, 0]
    yield p + top
    yield p + west
    yield p + bottom
    p += [2, 0, 0]
    yield p + top
    yield p + north
    yield p + bottom
    yield p + south
    p += [2, 0, 0]
    yield p + top
    yield p + north
    yield p + bottom
    yield p + south
    yield p + east
    p = origin + [0, 2, 0]
    yield p + top
    yield p + west
    yield p + bottom
    yield p + east
    p += [0, 2, 0]
    yield p + top
    yield p + west
    yield p + bottom
    yield p + north
    p += [2, 0, 0]
    yield p + top
    yield p + north
    yield p + bottom
    yield p + south
    p += [2, 0, 0]
    yield p + top
    yield p + north
    yield p + bottom
    yield p + south
    yield p + east
    p = origin + [0, -2, 0]
    yield p + top
    yield p + west
    yield p + bottom
    yield p + east
    p += [0, -2, 0]
    yield p + top
    yield p + west
    yield p + bottom
    yield p + east
    yield p + south
