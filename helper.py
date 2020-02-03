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

    shift_x = 12
    shift_y = -20

    # TODO: determine figure size, avoid additional margin
    fig = plt.figure(figsize=(6, 3))
    #fig = plt.figure(figsize=(6, 3), frameon=False)
    #ax = Axes3D(fig, [0, 0, 1, 1], azim=-90, elev=90, proj_type='ortho')
    ax = fig.add_axes(
        [0, 0, 1, 1],
        projection='3d',
        azim=-90,
        elev=90,
        proj_type='ortho',
        autoscale_on=False,
    )
    ax.disable_mouse_rotation()
    # TODO: determine x/y limits (z can be ignored in ortho projection?)
    # TODO: axis limits same aspect ratio as figure size
    aspect = np.true_divide(*fig.get_size_inches())
    ax.set_xlim(-15, 45)
    ax.set_ylim(-25, 5)
    #ax.set_zlim(-5, 5);

    ax.set_axis_off()

    #ax.set_frame_on(False)
    #ax.set_top_view()
    #ax.set_autoscale_on(False)
    #ax.set_clip_on(True)
    #fig.subplots_adjust(top=1, bottom=0, left=0, right=1)
    #plt.tight_layout()
    #fig.tight_layout()
    #ax.autoscale(tight=True)
    #ax.autoscale_view(tight=True)

    original_polys = np.array(list(faces()))

    ls = LightSource()

    y = 5
    for line in rotations:
        x = -35
        for rot in line:
            if not isinstance(rot, Rotation):
                rot = Rotation.from_quat(rot, normalized=True)
            polys = np.array(list(map(rot.apply, original_polys)))
            polys += [x, y, 0]
            plot_polys(polys, ax=ax, ls=ls)
            x += shift_x
        y += shift_y

    #print(ax.get_axis_position())
    #print(ax.get_frame_on())
    #print(ax.get_proj())
    #print(ax.get_w_lims())
    #print(ax.get_xlim())
    #print(ax.get_xlim3d())
    #print(ax.get_zbound())
    #print(ax.get_zlim())
    #print(ax.get_zlim3d())
    #print(ax.margins())
    #ax.margins(0)
    #print(ax.margins())

    #print(ax.get_position())
    #print(ax.get_aspect())

    # TODO: return fig?
