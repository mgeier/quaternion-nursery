from collections import namedtuple as _namedtuple
import math as _math


class Vector(_namedtuple('VectorBase', 'x y z')):
    """Three-dimensional vector (named tuple).

    See `collections.namedtuple`.

    Attributes
    ----------
    x : float
        x coordinate.
    y : float
        y coordinate.
    z : float
        z coordinate.

    """

    __slots__ = ()

    def __neg__(self):
        return Vector(
            -self.x,
            -self.y,
            -self.z,
        )

    def __mul__(self, scalar):
        return Vector(
            self.x * scalar,
            self.y * scalar,
            self.z * scalar,
        )

    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    def __truediv__(self, scalar):
        return Vector(
            self.x / scalar,
            self.y / scalar,
            self.z / scalar,
        )

    #def __xor__(self, other):
    #    """Cross product."""
    #    a1, a2, a3 = self
    #    b1, b2, b3 = other
    #    return Vector(
    #        a2 * b3 - a3 * b2,
    #        a3 * b1 - a1 * b3,
    #        a1 * b2 - a2 * b1,
    #    )

    #def __rxor__(self, other):
    #    # TODO: anti-commutative?
    #    return NotImplemented

    #def __matmul__(self, other):
    #    """Dot product."""
    #    a1, a2, a3 = self
    #    b1, b2, b3 = other
    #    return (a1 * b1) + (a2 * b2) + (a3 * b3)

    #def __rmatmul__(self, other):
    #    return self.__matmul__(other)

    @property
    def norm(self):
        return _math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def normalized(self):
        # TODO: return UnitVector?
        return self / self.norm


def ensure_vector(v):
    if not isinstance(v, Vector):
        v = Vector(*v)
    return v


#class UnitVector(Vector):
#
#    __slots__ = ()
#
#    def __new__(cls):
#        raise TypeError('Use UnitVector.from_vector() to create a UnitVector')
#
#    @classmethod
#    def from_vector(cls, v):
#        v = ensure_vector(v)
#        norm = v.norm
#        return super().__new__(cls, v.x / norm, v.y / norm, v.z / norm)


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
            Vector(
                a1*b2 + b1*a2 + c1*d2 - d1*c2,
                a1*c2 - b1*d2 + c1*a2 + d1*b2,
                a1*d2 + b1*c2 - c1*b2 + d1*a2,
            )
        )

    def __rmul__(self, other):
        """Disable inherited concatenation operator."""
        return NotImplemented

    def conjugate(self):
        return super().__new__(
            type(self),
            self.scalar,
            -ensure_vector(self.vector),
        )

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
        return super().__new__(
            cls,
            _math.cos(angle / 2),
            _math.sin(angle / 2) * Vector(*axis).normalized(),
        )

    def __pow__(self, alpha):
        return UnitQuaternion.from_axis_angle(self.axis, alpha * self.angle)

    inverse = Quaternion.conjugate

    # TODO: exponential map
    # TODO: logarithmic map

    @property
    def axis(self):
        assert self.scalar <= 1
        # NB: This is the same as self.vector.normalized()
        return ensure_vector(self.vector) / _math.sqrt(1 - self.scalar**2)

    @property
    def angle(self):
        return 2 * _math.acos(self.scalar)

    def rotate_vector(self, v):
        rotated = self * Quaternion(0, v) * self.inverse()
        return rotated.vector
