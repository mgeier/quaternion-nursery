Quaternion Notes
================

Andrew J. Hanson:
Visualizing Quaternions

Ken Shoemake:
Animating Rotation with Quaternion Curves

Myoung-Jun Kim,  Myung-Soo Kim, and Sung Yong Shin:
A General Construction Scheme for Unit Quaternion Curves
with Simple High Order Derivatives

antipodality!

interpolation: short way vs. long way?
if dot product < 0: long way, negate one input

David Eberly, Geometric Tools:
Quaternion Algebra and Calculus,
https://www.geometrictools.com/

Schlag

"Explorable Videos": https://eater.net/quaternions

commutative, constant velocity, torque-minimal?

torque-minimal = geodesic?

quaternion slerp vs. quaternion nlerp vs. log-quaternion lerp:
http://number-none.com/product/Understanding%20Slerp,%20Then%20Not%20Using%20It/

Python Libs
-----------

https://github.com/moble/quaternion

https://quaternion.readthedocs.io/en/latest/README.html

https://github.com/KieranWynn/pyquaternion

https://kieranwynn.github.io/pyquaternion/

https://pyrr.readthedocs.io/en/latest/api_quaternion.html

SLERP
-----

https://en.wikipedia.org/wiki/Slerp

torque-minimal path

constant velocity

non-commutative?

NLERP
-----

normalized linear interpolation

"gives good results if the interpolated quaternions are reasonably close (difference of about 60 to 90 degrees is still fine) while being very simple and fast"

torque-minimal path

non-constant velocity

commutative

SQUAD
-----

"spherical quadrangle interpolation"

Quaternion Splines
------------------

http://qspline.sourceforge.net/

http://qspline.sourceforge.net/qspline.pdf

SciPy: https://github.com/scipy/scipy/pull/9831

https://github.com/scipy/scipy/files/2932755/attitude_interpolation.pdf
