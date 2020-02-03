from functools import partial

from matplotlib.colors import LightSource
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np
from scipy.spatial.transform import Rotation


shade_colors = partial(Axes3D._shade_colors, 'dummy')
generate_normals = partial(Axes3D._generate_normals, 'dummy')


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


def plot_polys(polys, *, ax=None, ls=None):
    if ax is None:
        raise TypeError('TODO: create default axes (and figure?)')
    if ls is None:
        ls = LightSource()
    color = 'white'
    alpha = 1
    linewidth = 0.5
    edgecolor = 'black'
    coll = Poly3DCollection(
        polys,
        closed=True,
        alpha=alpha,
        linewidth=linewidth,
        edgecolor=edgecolor,
    )

    colset = shade_colors(color, generate_normals(polys), ls)
    coll.set_facecolors(colset)
    ax.add_collection3d(coll)


def plot_rotations(rotations):
    # TODO: pass list of lists of quaternions (optionally scipy rotations?)
    # TODO: description/title text for each line of rotations


    # TODO: determine figure size, avoid additional margin
    fig = plt.figure(figsize=(6, 2))
    ax = fig.add_axes([0, 0, 1, 1], projection='3d')
    ax.view_init(azim=-90, elev=90)
    ax.set_proj_type('ortho')
    # TODO: determine x/y limits (z can be ignored in ortho projection?)
    # TODO: axis limits same aspect ratio as figure size
    aspect = np.true_divide(*fig.get_size_inches())
    ax.set_xlim(-5, 25)
    ax.set_ylim(-5, 5)
    #ax.set_zlim(-5, 5);
    ax.set_axis_off()

    polys = np.array(list(faces()))

    ls = LightSource()

    # TODO: go through lines
    # TODO: go through rotations
    # TODO: rotate and call plot_polys()

    plot_polys(polys, ax=ax, ls=ls)

    # TODO: return fig?
