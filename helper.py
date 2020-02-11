from functools import partial

from matplotlib import artist
from matplotlib.colors import LightSource
import matplotlib.pyplot as plt
from matplotlib.transforms import TransformedBbox
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

    #ax.dist = 6

    ax.disable_mouse_rotation()
    # TODO: determine x/y limits (z can be ignored in ortho projection?)
    # TODO: axis limits same aspect ratio as figure size
    aspect = np.true_divide(*fig.get_size_inches())
    ax.set_xlim(-15, 45)
    ax.set_ylim(-25, 5)
    #ax.set_zlim(-5, 5);

    #ax.set_axis_off()

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


class DumbAxes3D(Axes3D):

    def __init__(self, figure, *args, **kwargs):
        super().__init__(figure, *args, **kwargs)
        self.set_axis_off()

        #self._position = self._originalPosition
        #self.bbox = TransformedBbox(self._position, figure.transFigure)
        #self.bbox = TransformedBbox(self._originalPosition, figure.transFigure)
        #self._set_lim_and_transforms()
        #self.patch.set_transform(self.transAxes)

        #self._position = self._originalPosition
        self.set_figure(figure)
        #self.patch.set_transform(self.transAxes)

        # TODO: deactivate mouse interaction?

    @artist.allow_rasterization
    def draw(self, renderer):
        self.patch.draw(renderer)  # background (axes.facecolor)

        xmin, xmax = self.get_xlim3d()
        ymin, ymax = self.get_ylim3d()
        zmin, zmax = self.get_zlim3d()

        worldM = proj3d.world_transformation(xmin, xmax,
                                             ymin, ymax,
                                             zmin, zmax)

        zfront, zback = -1, 1
        projM = proj3d.ortho_transformation(zfront, zback)

        Mt = [[1, 0, 0, -0.5],
              [0, 1, 0, -0.5],
              [0, 0, 1, -0.5],
              [0, 0, 0, 1]]

        #self.eye = [0, 0, -0.5]
        #self.eye = [1, 0, 0]
        #self.vvec = [0.5, 0.5, 1]
        #self.vvec = [1, 0, 0]
        #self.eye = [0, 0, 0.5]
        #self.vvec = [0, 0, 0]
        self.vvec = NotImplemented
        self.eye = NotImplemented
        #self.M = np.dot(projM, worldM)
        #self.M = projM @ worldM
        self.M = worldM
        #self.M = projM @ Mt @ worldM
        #self.M = Mt @ worldM

        renderer.M = self.M
        renderer.vvec = self.vvec
        renderer.eye = self.eye
        #renderer.get_axis_position = self.get_axis_position
        #renderer.vvec = NotImplemented
        #renderer.eye = NotImplemented
        renderer.get_axis_position = NotImplemented

        for coll in self.collections:
            coll.do_3d_projection(renderer)
        for patch in self.patches:
            patch.do_3d_projection(renderer)

        super(Axes3D, self).draw(renderer)

    def apply_aspect(self, position=None):
        #pass
        super(Axes3D, self).apply_aspect(position=position)
