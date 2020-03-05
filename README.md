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

exponential map?
rotation axis multiplied by angle?

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
https://www.worldcat.org/search?q=no%3A16843459&qt=advanced&dblist=638

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

---

Pletinckx 1989:

Clark 1981: Matrix for cardinal splines

B-splines: Prenter 1975; Foley 1984

Tensioned B-splines (which are
identical to Beta2-splines, see Barsky 1985) have
the same properties but give something in between
ordinary B-splines and straight lines (Duff 1986).

Already three algorithms have been proposed to
spline quaternions: a Bezier interpolation scheme
by Ken Shoemake (1985), a B-spline interpolation
scheme by T o m Duff (1986) and a Boehm quad-
rangle spline by Ken Shoemake (1987).

[approximation by repeated subdivision with t=0.5?]

In practice, the subdivision operation has to be
repeated only 3 or 4 times.

---

Watt 1992 Advanced Animation and Rendering Techniques
Section 15.3.8: Parameterization of orientation

SLERP: when angle is very small, use linear interpolation

Equations for SQUAD, but no derivation (refers to Shoemake 1987)

---

Nielson 2004:
\nu-Quaternion Splines for the Smooth Interpolation of Orientations

Solve non-linear system of equations with an iterative method.

Initial approximation, for example, 4D-spline interpolation, normalizing the results.

non-uniform knot placement

visualization: triad tracing graph

tension parameters

It is difficult to convey a sense of this experience here
even with triad tracing graphs because they do not show
the rate of transversal, which is one of the useful features of
tension parameters. We urge readers to try our new method
as we believe they will like it very much.

\nu spline is piecewise cubic; has G2 continuity

approximating, not interpolating

"the [control points] are not known a priori and must be
computed so that the curve actually interpolates."

---

Quaternion splines with TCB:

http://www.idea2ic.com/File_Formats/Splines%20&%20Quaternions.pdf

---

Barr, Currin, Gabriel, Hughes (1992):
Smooth Interpolation of Orientations with Angular Velocity Constraints
using Quaternions

Analogous to the mathematical foundations of flat-space spline curves, we
minimize the net “tangential acceleration” of the quaternion path. We replace
the flat-space quantities with curved-space quantities, and numerically solve
the resulting equation with finite difference and optimization methods.

Splining in non-Euclidean Spaces

not found:
S Gabriel, J Kajiya
Spline interpolation in curved space. State of the art in image synthesis. SIGGRAPH 1985 course notes

This paper presents a simpler (and extrinsic) version of the Gabriel/Kajiya
approach to splining on arbitrary manifolds.

Our techniques allow the user to specify arbitrarily large initial and final
angular velocities of a rotating body; by assigning large angular velocities, a
user can make an object tumble several full turns between successive keypoints.

The techniques are fast enough to experiment
with, taking a few minutes per interpolation.

We find a path that minimizes a measure of net
bending.
We implement this, however, using a finite
difference technique, so that we end up with a sequence
of points on the path, rather than a continuous path. To
produce a continuous path, we use Shoemakers slerping
to interpolate between these points.

we will seek a path
in quaternion space, i.e., a path on the unit 3-sphere
in 4-space, that minimizes the total squared tangential
acceleration.

In this section, for our constrained optimization problem, we consider some of
the merits of using a continuous derivative versus using discrete derivatives.
Ultimately we will choose the discrete approach, because it is simpler. The
reader should not infer that continuous approaches are not worthy of further
investigation, however.

angular velocity constraints?
