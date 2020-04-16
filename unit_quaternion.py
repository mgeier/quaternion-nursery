from collections import namedtuple as _namedtuple
import math as _math


class Quaternion(_namedtuple('QuaternionBase', 'scalar vector')):

    __slots__ = ()

    def __mul__(self, other):
        if not isinstance(other, Quaternion):
            return NotImplemented
        if isinstance(self, UnitQuaternion) and isinstance(other, UnitQuaternion):
            result_type = UnitQuaternion
        else:
            result_type = Quaternion
        a1 = self.scalar
        b1, c1, d1 = self.vector
        a2 = other.scalar
        b2, c2, d2 = other.vector
        return super().__new__(
            result_type,
            # TODO: properly derive this
            a1*a2 - b1*b2 - c1*c2 - d1*d2,
            (
                a1*b2 + b1*a2 + c1*d2 - d1*c2,
                a1*c2 - b1*d2 + c1*a2 + d1*b2,
                a1*d2 + b1*c2 - c1*b2 + d1*a2,
            )
        )

    def __rmul__(self, other):
        """Disable inherited concatenation operator."""
        return NotImplemented

    def conjugate(self):
        x, y, z = self.vector
        return super().__new__(type(self), self.scalar, (-x, -y, -z))

    @property
    def xyzw(self):
        return *self.vector, self.scalar

    @property
    def wxyz(self):
        return self.scalar, *self.vector


class UnitQuaternion(Quaternion):

    __slots__ = ()

    def __new__(cls):
        raise TypeError('Use UnitQuaternion.from_*() to create a UnitQuaternion')

    @classmethod
    def from_axis_angle(cls, axis, angle):
        """

        *axis* will be normalized.
        *angle* in radians.

        """
        # TODO: implement with exponential map?
        x, y, z = axis
        norm = _math.sqrt(x**2 + y**2 + z**2)
        s = _math.sin(angle / 2)
        return super().__new__(
            cls,
            _math.cos(angle / 2),
            (s * x / norm, s * y / norm, s * z / norm),
        )

    def __pow__(self, alpha):
        return UnitQuaternion.from_axis_angle(self.axis, alpha * self.angle)

    # TODO: proper implementation to get meaningful docstring?
    inverse = Quaternion.conjugate

    # TODO: exponential map
    # TODO: logarithmic map

    @property
    def axis(self):
        assert self.scalar <= 1
        # NB: This is the same as sqrt(x**2 + y**2 + z**2)
        norm = _math.sqrt(1 - self.scalar**2)
        x, y, z = self.vector
        return x / norm, y / norm, z / norm

    @property
    def angle(self):
        return 2 * _math.acos(self.scalar)

    def rotate_vector(self, v):
        rotated = self * Quaternion(0, v) * self.inverse()
        return rotated.vector
