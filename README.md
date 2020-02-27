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

Ken Shoemake:
https://web.archive.org/web/20120915153625/http://courses.cms.caltech.edu/cs171/quatut.pdf

"Any  continuous  quaternion  curve  which  does  not  pass  through  [0,  0]
gives  a continuous  sequence  of  rotations,  and  so  may  be  used  for
animation.  However  the consequences  of  part  3  of  Theorem  1  explored
in  the  last  section  tell  us  that  to  gain control  of  what  happens
with  the  rotations  we  should  confine  our  attention  to  unit quaternion
curves."

"Curves  on  a  sphere  are  harder  to  create,  understand,  and  control
than  ordinarysplines.   The   recent   literature   contains   three   main
approaches:   geometric transliteration,  differential  equations,  and  arc
blends.  Here  is  a  reference  for  each:  J.Schlag,   “Using   Geometric
Construction   to   Interpolate   Orientations   with Quaternions”  in Graphics
Gems  II,  Academic  Press,  1991,  pp.  377–380;  A.  Barr,  B.Currin,  S.
Gabriel,  and  J.  Hughes,  “Smooth  Interpolation  of  Orientations
with Angular  Velocity  Constraints  using  Quaternions”  in Proceedings  of
SIGGRAPH  ’92,ACM  Press,  1992,  pp.  313–320;  W.  Wang  and  B.  Joe,
“Orientation  Interpolation  in Quaternion  Space  Using  Spherical  Biarcs”  in
Proceedings  of  Graphics  Interface  ’93,Morgan  Kaufmann,  1993,  pp.
24–32."

"Great  arcs  traversed  at  constant  speed  are,  in  fact,geodesics;  that
is,  they  are  paths  with  minimal  acceleration,  and  so  as  straight
aspossible.  A  unit  quaternion  great  circle  arc  gives  a  constant  speed
rotation  around  afixed axis, and can be written C(t) = (q1 q0^–1)^t q0."

"The  geometric  transliteration  approach  treats  great  arcs  as  the
“moral  equivalent”  ofline  segments  and  interprets  geometric
constructions  like  de  Casteljau’s  algorithmin  those  terms.  The
differential  equation  approach  notes  that  natural  cubic  splinesalso
minimize  acceleration,  and  imposes  a  spherical  constraint  to  get
equations  ofmotion.  The  arc  blend  approach—by  far  the  cheapest  of  the
three—combines  small 10arc  segments  to  get  a  smooth  curve.  Given  only
two  points  to  interpolate,  all  threeapproaches normally give a great arc."

C implementation:
https://github.com/erich666/GraphicsGems/tree/master/gemsiv/arcball

Rotate vector by quaternion:

`q**-1 v q` (Shoemake 85) or `q v q**-1`?
Or is it the same?

Python Libs
-----------

https://github.com/moble/quaternion (dtype=quaternion)

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

"great arc in-betweening" (Shoemake 85)

`q1 (q1**-1 q2)**u` (Shoemake 85)

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

Shoemake 1985

"There are lots of ways to achieve it---off the sphere; unfortunately we've
learned too much."
???

XMQuaternionSquad function:
https://docs.microsoft.com/en-us/windows/win32/api/directxmath/nf-directxmath-xmquaternionsquad

John Schlag: Graphics Gems II, VIII.4 - Using Geometric Constructions to Interpolate Orientation with Quaternions

Catmull--Rom using SLERP (but only uniform!)

---

Wang and Joe:
Orientation Interpolation in Quatemion Space
Using Spherical Biarcs

In this paper we will use spherical biarcs represented as
piecewise rational quadratic Bezier curves to interpolate points
on S3. The spherical biarcs are then stitched together to design
a G1, i.e. unit tangent vector continuous, interpolating spline
curve on S3. The result is a locally controllable circular arc
spline curve, or a rational quadratic spline curve on S3. This
curve can be made C1 using a simple arclength parameteriza-
tion or other reparameterization methods.

mentioned methods:

* spherical analogue of the cubic Bezier curve (Shoemake 1985)
* SQUAD (Shoemake 1987, not available?)
* the spherical analogues of the cubic cardinal spline and tensioned B-spline
  (Pletinckx)
* normalized cubic Hennite interpolant (Ge 1991, not available?)
* spherical biarc (topic of the paper)

So far there has been no comparison of the quality of the
above interpolation methods, because of the difficulty of visu-
alization in E4. [...]
The main criterion for comparing the various methods
has been the efficiency of computing in-between quaternions.
[and this paper also only compares efficiency]


Based on our experiments, we
have chosen equal chord biarcs. But this choice is yet to be
justified theoretically.


SQUAD: analogue of Boehm's quadrangle construction of cubic curves
not available:
Shoemake, K. (1987), Quaternion Calculus and Fast An-
imation, SIGGRAPH 87 Course Notes #10 : Computer
Animation : 3D Motion Specification and Control, pp.
101-121.

spherical analogues of the cubic cardinal spline
and the tensioned B-spline curve are used, where the curves
are defined by subdivision procedures.
Pletinckx, D. (1989), Quatemion Calculus as a Basic Tool
in Computer Graphics, The Visual Computer, vo!. 5, pp.
2-13.

Hermite cubic interpolant is used to
interpolate two points and the end tangents on S3, and then the
interpolant is projected onto the sphere S3 through the center
of S3, as in general the interpolant is not contained in S3.
not available:
Ge, Q.1. and Ravani, B. (1991), Computational Geome-
try and Mechanical Design Synthesis, 13th IMAC World
Congress on Computation and Applied Math. , Dublin,
Ireland, pp. 1013-1015.

---

Biarcs in 2D and 3D (no rotations):
http://www.ryanjuckett.com/programming/biarc-interpolation/


Crouch, P., G. Kun, und F. Silva Leite. „The De Casteljau Algorithm on Lie Groups and Spheres“. Journal of Dynamical and Control Systems 5, Nr. 3 (1. Juli 1999): 397–429. https://doi.org/10.1023/A:1021770717822.
