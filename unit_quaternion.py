import math as _math


class Quaternion:

    __slots__ = '_scalar', '_vector'

    def __new__(cls, scalar, vector):
        obj = super().__new__(cls)
        obj._scalar = scalar
        x, y, z = vector
        obj._vector = x, y, z
        return obj

    @property
    def scalar(self):
        return self._scalar

    @property
    def vector(self):
        return self._vector

    def __repr__(self):
        name = type(self).__name__
        return f'{name}(scalar={self.scalar}, vector={self.vector})'

    def __eq__(self, other):
        if not isinstance(other, Quaternion):
            return NotImplemented
        return self.xyzw == other.xyzw

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
        return Quaternion.__new__(
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

    def __neg__(self):
        x, y, z = self.vector
        return Quaternion.__new__(type(self), -self.scalar, (-x, -y, -z))

    def conjugate(self):
        x, y, z = self.vector
        return Quaternion.__new__(type(self), self.scalar, (-x, -y, -z))

    def normalize(self):
        norm = self.norm
        x, y, z, w = self.xyzw
        return UnitQuaternion.from_unit_xyzw(
            (x / norm, y / norm, z / norm, w / norm))

    def dot(self, other):
        return sum(map(_math.prod, zip(self.xyzw, other.xyzw)))

    @property
    def norm(self):
        x, y, z, w = self.xyzw
        return _math.sqrt(x**2 + y**2 + z**2 + w**2)

    @property
    def xyzw(self):
        x, y, z = self.vector
        return x, y, z, self.scalar

    @property
    def wxyz(self):
        x, y, z = self.vector
        return self.scalar, x, y, z


class UnitQuaternion(Quaternion):

    __slots__ = ()

    def __new__(cls, *args, **kwargs):
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

    @classmethod
    def from_unit_xyzw(cls, xyzw):
        """

        Input is *not* normalized!

        """
        x, y, z, w = xyzw
        return super().__new__(cls, w, (x, y, z))

    def __pow__(self, alpha):
        if self.scalar == 1:
            return super().__new__(UnitQuaternion, self.scalar, self.vector)
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


def slerp(one, two, t):
    """SLERP.

    *t* has to be between 0 and 1.

    """
    return (two * one.inverse())**t * one


def canonicalize_quaternion_sequence(seq):
    seq = iter(seq)
    for p in seq:
        if p.scalar < 0:
            p = -p
        break
    else:
        return
    yield p
    for q in seq:
        if p.dot(q) < 0:
            q = -q
        yield q
        p = q
