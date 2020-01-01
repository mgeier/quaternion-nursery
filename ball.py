import math as _math

import pythreejs as _three


class Ball:

    def __init__(self):
        # TODO: arguments for width/height
        self._width = 600
        self._height = 400
        self._ball = _three.Mesh(
            geometry=_three.SphereGeometry(
                radius=1,
                widthSegments=30,
                heightSegments=15,
            ),
            material=_three.MeshLambertMaterial(color='lightgray'),
        )
        self._axes = _three.AxesHelper(size=1.2)
        self._ambient_light = _three.AmbientLight(
            intensity=0.5,
        )
        self._directional_light1 = _three.DirectionalLight(
            position=[0, 0, 1],
            intensity=0.6,
        )
        self._directional_light2 = _three.DirectionalLight(
            position=[0, 0, -1],
            intensity=0.6,
        )
        self._scene = _three.Scene(
            children=[
                self._ball,
                self._axes,
                self._ambient_light,
                self._directional_light1,
                self._directional_light2,
            ],
        )
        self._camera = _three.PerspectiveCamera(
            position=[0, 0, 2.4],
            up=[0, 0, 1],
            aspect=self._width/self._height,
        )
        self._controls = _three.OrbitControls(controlling=self._camera)
        self._renderer = _three.Renderer(
            camera=self._camera,
            scene=self._scene,
            controls=[self._controls],
            width=self._width,
            height=self._height,
            #alpha=True,
            #clearOpacity=0.5,
        )

    def add_arrow(self, quaternion, *, scale=1, color='red', linewidth=2):
        vertices = [
            (0, 0, 1),
            (-0.02, -0.01, 1),
            (0, 0.04, 1),
            (0.02, -0.01, 1),
            (0, 0, 1),
        ]
        line = _three.Line2(
            _three.LineGeometry(positions=vertices),
            _three.LineMaterial(color=color, linewidth=linewidth))
        line.scale = scale, scale, 1
        line.quaternion = tuple(quaternion)
        self._scene.add(line)

    def add_arrows(self, quaternions, **kwargs):
        for quaternion in quaternions:
            self.add_arrow(quaternion, **kwargs)

    def show(self):
        # TODO: proper repr?
        display(self._renderer)


def angles2quaternion(azimuth, elevation, roll):
    s_alpha = _math.sin(_math.radians(azimuth) / 2)
    s_beta = _math.sin(_math.radians(elevation) / 2)
    s_gamma = _math.sin(_math.radians(roll) / 2)
    c_alpha = _math.cos(_math.radians(azimuth) / 2)
    c_beta = _math.cos(_math.radians(elevation) / 2)
    c_gamma = _math.cos(_math.radians(roll) / 2)
    return ((c_alpha*c_gamma*s_beta - c_beta*s_alpha*s_gamma),
            (c_alpha*c_beta*s_gamma + c_gamma*s_alpha*s_beta),
            (c_alpha*s_beta*s_gamma + c_beta*c_gamma*s_alpha),
            (c_alpha*c_beta*c_gamma - s_alpha*s_beta*s_gamma))
