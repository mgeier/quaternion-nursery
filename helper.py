from functools import partial

import matplotlib
from matplotlib.colors import LightSource
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D, proj3d
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
    p = origin + [-2, 0, 0]
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
    p = origin + [-2, 2, 0]
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
    p = origin + [-2, -2, 0]
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
    # TODO: description/title text for each line of rotations

    shift_x = 12
    shift_y = -20

    # TODO: determine figure size, avoid additional margin
    fig = plt.figure(figsize=(6, 3))
    ax = DumbAxes3D(fig)

    # TODO: determine x/y limits (z can be ignored in ortho projection?)
    # TODO: axis limits same aspect ratio as figure size
    aspect = np.true_divide(*fig.get_size_inches())
    ax.set_xlim(-5, 55)
    ax.set_ylim(-25, 5)

    ls = LightSource()

    y = 0
    for line in rotations:
        x = 0
        for rot in line:
            if not isinstance(rot, Rotation):
                rot = Rotation.from_quat(rot, normalized=True)
            polys = np.array(list(map(rot.apply, faces())))
            polys += [x, y, 0]
            plot_polys(polys, ax=ax, ls=ls)
            x += shift_x
        y += shift_y

    #print(ax.get_position())

    # TODO: return fig?


def plot_line(rotations, *, ax=None):
    if ax is None:
        raise TypeError('TODO: create default axes (and figure?)')
    shift_x = 12

    ax.set_xlim(-5, 55)
    ax.set_ylim(-25, 5)

    ls = LightSource()

    x = 0
    y = 0
    for rot in rotations:
        if not isinstance(rot, Rotation):
            rot = Rotation.from_quat(rot, normalized=True)
        polys = np.array(list(map(rot.apply, faces())))
        polys += [x, y, 0]
        plot_polys(polys, ax=ax, ls=ls)
        x += shift_x


class DumbAxes3D(Axes3D):

    name = 'dumb3d'

    def __init__(self, figure, rect=[0, 0, 1, 1], sharex=None, sharey=None):
        if sharex is not None:
            raise TypeError('sharex not supported')
        if sharey is not None:
            raise TypeError('sharey not supported')
        super().__init__(figure, rect=rect)
        self.set_axis_off()
        self.set_figure(figure)
        self.disable_mouse_rotation()

    @matplotlib.artist.allow_rasterization
    def draw(self, renderer):
        self.patch.draw(renderer)  # background (axes.facecolor)
        xmin, xmax = self.get_xlim3d()
        ymin, ymax = self.get_ylim3d()
        zmin, zmax = self.get_zlim3d()
        self.M = proj3d.world_transformation(xmin, xmax,
                                             ymin, ymax,
                                             zmin, zmax)
        self.vvec = NotImplemented
        self.eye = NotImplemented

        renderer.M = self.M
        renderer.vvec = self.vvec
        renderer.eye = self.eye
        renderer.get_axis_position = NotImplemented

        for coll in self.collections:
            coll.do_3d_projection(renderer)
        for patch in self.patches:
            patch.do_3d_projection(renderer)

        super(Axes3D, self).draw(renderer)

    def apply_aspect(self, position=None):
        super(Axes3D, self).apply_aspect(position=position)


matplotlib.projections.register_projection(DumbAxes3D)
