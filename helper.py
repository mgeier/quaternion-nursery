from functools import partial
from math import radians

import matplotlib
from matplotlib.colors import LightSource
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D, proj3d
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

from unit_quaternion import UnitQuaternion


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


def create_polys(rot, *, ls=None):
    if not isinstance(rot, UnitQuaternion):
        rot = UnitQuaternion.from_unit_xyzw(rot)
    polys = np.array([list(map(rot.rotate_vector, face)) for face in faces()])
    if ls is None:
        ls = LightSource()
    color = 'white'
    facecolors = shade_colors(color, generate_normals(polys), ls)
    return polys, facecolors


def create_collection(ax):
    alpha = 1
    linewidth = 0.5
    edgecolor = 'black'
    coll = Poly3DCollection(
        [],
        closed=True,
        alpha=alpha,
        linewidth=linewidth,
        edgecolor=edgecolor,
    )
    ax.add_collection3d(coll)
    return coll


def prepare_axis(n, *, ax=None):
    """

    Returns collections together with their offsets.

    """
    if ax is None:
        ax = plt.gca(projection='dumb3d')
    object_width = 12
    shift_x = object_width
    _, _, x1, y1 = ax.bbox.bounds
    aspect = x1 / y1
    total_width = object_width * n
    total_height = total_width / aspect
    ax.set_xlim(0, total_width)
    ax.set_ylim(0, total_height)
    x = object_width / 2
    y = total_height / 2
    z = 0
    return [(create_collection(ax), [x + i * shift_x, y, z]) for i in range(n)]


def update_plot(collections_and_offsets, rotations, *, ls=None):
    if ls is None:
        ls = LightSource()
    collections = []
    for (coll, offset), rot in zip(collections_and_offsets, rotations):
        polys, facecolors = create_polys(rot, ls=ls)
        polys += offset
        coll.set_verts(polys)
        coll.set_facecolors(facecolors)
        collections.append(coll)
    return collections


def plot_rotations(rotations, *, ax=None):
    collections = prepare_axis(len(rotations), ax=ax)
    ls = LightSource()
    collections = update_plot(collections, rotations, ls=ls)
    return collections


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
        # NB: z limits are deliberately swapped to switch to right-handed
        #     coordinates, z pointing out of the figure (towards the viewer)
        self.M = proj3d.world_transformation(xmin, xmax,
                                             ymin, ymax,
                                             zmax, zmin)
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


def angles2quat(azimuth, elevation, roll):
    return (
        UnitQuaternion.from_axis_angle((0, 0, 1), radians(azimuth)) *
        UnitQuaternion.from_axis_angle((1, 0, 0), radians(elevation)) *
        UnitQuaternion.from_axis_angle((0, 1, 0), radians(roll))
    )
