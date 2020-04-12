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

Known approaches:

* interpolate Euler angles
* interpolate rotation matrices (nobody suggested that?)
* interpolate quaternions in R4, then normalize the result
* de Casteljau algorithm with SLERP
* SQUAD?
* spherical biarcs/rational quadratic splines in R4
* intersect S3 with hyperplane, create two arcs in resulting 2-sphere, blend
* iterative methods?
* approximation by subdivision? Pletinckx?

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
Orientation Interpolation in Quaternion Space
Using Spherical Biarcs

[similar to Nielson 1993?]

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
* normalized cubic Hermite interpolant (Ge 1991, not available?)
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

---

Kim, Kim, Shin 1995:
A General Construction Scheme for Unit Quaternion Curves
with Simple High Order Derivatives

the de Casteljau type construction of cubic B-spline quaternion
curves does not preserve C2-continuity

[...] either as an algebraic construction using basis
functions or as a geometric construction based on recursive linear
interpolations [Barry & Goldman 1988].
This paper proposes a general framework which
extends the algebraic construction methods to SO(3).

The two (i.e., algebraic and geometric) construction schemes
generate identical curves in R3; however, this is not the case in
the non-Euclidean space SO (3) [Kim, Kim, Shin 1995 (A C2 ...)].

Though Shoemake [1985, 1991] postulates
correct first derivatives, the quaternion calculus employed there
is incorrect (see [Kim, Kim, Shin 1995 (A compact ...)] for more details).

More seriously, the C2-continuity of a spline curve in R3 may
not carry over to SO(3)

Since it is possible to manipulate the position curve as well as the corresponding orientation
curve in a unified manner, the modeling and manipulation of rigid
motions can be managed more conveniently.

exponential map (see Curtis: Matrix Groups)

For this purpose, we may need to extend
the quaternion curve construction scheme of this paper to that of
quaternion surfaces and volumes. This is currently a difficult open
problem. Therefore, the important problem of torque minimization
for 3D rotations has not been solved in this paper.

The two spaces S3 and SO(3) have the same local topology and
geometry. The major difference is in the distance measures of the
two spaces SO(3) and S3. A rotation curve Rq(t) \in SO(3) is twice
as long as the corresponding unit quaternion curve q(t) \in S3.

Here, we assume each
rotation is specified in the local frame. This is simply for notational
convenience; in the local frame, we can write the multiplications in
the same order as the rotations. By reversing the order of quaternion
multiplications, the same construction schemes can be applied to
the quaternion curves defined in the global frame.

Shoemake (1991) used the formula [...] In general, this formula is incorrect.

Cumulative form

cumulative basis functions

This Bézier quaternion curve has a different
shape from the Bézier quaternion curve of Shoemake (1985)

---

Kim, Kim, Shin 1996:
A Compact Differential Formula for the First Derivative
of a Unit Quaternion Curve

Shoemake (1985) claimed [...]
Shoemake (1991) used the formula [...] in deriving the quaternion curve
differentials on S3 for the purpose of extending the
Boehm (1982) quadrangle to S3.
[...] however, the formula only holds under the cornplanarity condition [...]
Unfortunately, Shoemake misinterpreted the meaning of dq, which is
the differential q'(t), as the logarithm logq.

derivation of q'(0) for previous papers:
Shoemake 1985
Shoemake 1991
Kim, Nam 1993, 1994
Hanotaux and Peroche 1993

---

Kim, Nam 1995:
Interpolating Solid Orientations with Circular Blending Quaternion Curves

Using a similar method to the parabolic blending of Overhauser [...]
we generate a C^k-continuous
quaternion path which smoothly interpolates a given sequence of solid orientations.

Though the squad
method [Shoemake 1991] is computationally (about twice) more efficient than the Bezier method [Shoemake 1985], the
rotational motions generated by squad curves are not as smooth as those generated by the
spherical Bezier curves.

The circle methods [Nielson 1993, Wang and Joe 1993] are
computationally more efficient than other methods; however, they have much limitations
in exibility. Since each circular curve is a planar curve, at each junction of two circular
curves, a large angular acceleration/torque is generated that would cause undesirable e ects
on smooth animation of a moving 3D solid [Barr et al. 1992]

Using a conceptual similarity to the great circle (interpolating two points) on the unit
sphere S2, we consider how to construct a great 2-sphere S which interpolates three points
p1, p2, p3 \in S3 in the 4D Euclidean space R4.

---

Grassia 1998:
Practical Parameterization of Rotations Using the Exponential Map

Unlike the quaternion parameterization, the domain of this parameterization
is Euclidean, so it does contain singularities.

On the other hand, S3 is an excellent place to interpolate rotations
because it possesses the same local geometry and topology as S0(3).

[Kim et. al. 95] developed closed-form quaternion curves on S3 using Bezier, Hermite,
B-spline (or any) blending functions, and were able to calculate high-order
parametric derivatives over the curves. This is great news for applications
that must compute and optimize or integrate along fixed orientation curves.
It does not aid greatly in differential control or optimization over the curve
shape itself, since it provides no correspondingly simple method for differen-
tiating the curve with respect to the quaternion control points. Even if it
did we would st ill face the inconveniences described in the preceding para-
graphs. Nevertheless, the ability to specify closed-form Hermite curves on
S3 by quaternion keys and angular velocities at the keys seems promising for
use in keyframe animation systems, given suitable methods for visualizing the
quaternion curves.

Given that we a re interest ed in paramet erizing a three-DOF rot ation ,
we would like a paramet erization emb edded in R3 that is free of gimbal lock
and interpolates rotations well using Euclidean interpolants such as cubic
splines. This goal is, of course, unrealizable, as it is a standard exercise in
topology to show that R3 cannot be mapped into S0(3) without singularities,
i.e., gimbal lock.

[exponential map ...]
The only problem with this particular formulation is that calculating [...]
goes to zero becomes numerically unstable.
However, by rearranging the above formula a little, we will be able to see that this exponential
map can be computed robustly even in the neighborhood of the origin: [...]

[not found!]
Hussein Yahia and Andre Gagalowicz.
"Interactive Animation of Object Orientations."
In Proceedings of the 2nd International Conference. Pixim 89.
pp. 265-75 (September 1989) .

[regarding Hanotaux and Peroche 1993:]
Hanotaux
notes that the straight line between two orientations in exponentially-mapped
R3 is not, in general, equivalent to the geodesic between the two orientations
in S3, but that "the approximation is not far from optimal." In fact the approximation can be quite far from optimal--quantifying how far is an open
question, but in general the error increases the further the two axes of rotation diverge from parallel.

However, representing three-DOF rotation functions in R3 is fraught with
peril because whenever the curve crosses one of the singularity shells discussed
in Section 3.2.1, some of the derivatives disappear.

---

Kim and Nam, 1996:
Hermite Interpolation of Solid Orientations with Circular
Blending Quaternion Curves

[about Kim, Kim, Shin: "A General ..."]
However, the curve construction symmetry is not preserved
under this transformation. That is, the Bezier quaternion curve of Reference 4 with control
points q1, ..., qn \in SO(3) has a different curve shape
from the one with qn, ..., q1 as its control points.

Wang and Joe (1993) constructed a Hermite interpolation curve on S3 by using two circular
arcs connected with C1-continuity. At the junction of two circular arcs, however, a large
acceleration/torque is generated that gives an undesirable effect on the smooth animation
of a moving solid (Barr et al. 1992)
This is inevitable as long as circular arcs are used as basic components
(see also the Nielson/Shieh circle spline of Reference 7).

There are many Hermite quaternion curves on S3 which satisfy the same boundary
conditions [many references are mentioned];
however, they generate different curves on S3.

[Idea: Cut S3 with a hyperplane containing the 2 points and velocities,
which results in a 2-sphere.
On that 2-sphere, create 2 arcs based on points and velocities.
Then there are two options: blend and transform back to S3, or vice versa.]

[Appendix I: derivation of quaternion first derivative]

---

Nielson 1993
Smooth Interpolation of Orientations

[rotation matrix]
The axis of rotation is the
eigenvector of O associated with the eigenvalue 1. The angle of rotation, \theta,
satisfies
1 + 2cos(\theta) = tr(O)
where tr(O) denotes the trace (sum of diagonal elements).

In fact, it turns out
that SO(3) can not be embedded in E4. Hopf (1940) has shown the if we wish to embed SO(3) in
Ek, then k must be greater than or equal to 5.

Normalized Cubic Spline [in R4] and Related Methods:
[...] This is really a rather inelegant way to solve the problem, [...]
The basic drawback to this
approach is the potential occurrence of cusps or tight kinks which result form the normalization.

The Nielson/Shieh Circle Method:
The interpolation curve used for this method consists of a
collection of rational quadratic curves constrained to lie on the unit sphere in E4 and joined so as to
have C1 continuity.

[difference to Wang and Joe 1993 (Biarcs)?]

Spherical Bernstein/Bezier Methods: [...]

The Spherical Quadratic B-spline Method:
This method is similar in many respects to the
Nielson/Shieh circle method.

Shoemake (1985) states "For the numerically knowledgeable, this construction approximates the
derivative at points of a sampled function by averaging the central difference of the sample
sequence". The Catmull/Rom spline is also based upon estimates of derivatives based upon central
differences. These ideas can be mapped to the present context by the following choice of inner
Bezier points [...]
Hanson (private communication) has shown that this choice is the same as that of Schlag (1992).

The Nielson/Heiland Spherical B-spline Method:
One the smoothest methods of this type that
we have observed is a method proposed by Nielson and Heiland (1992) which is based upon
"spherical B-splines".

B-splines do not interpolate
to their data, they only approximate it. For the application of animating orientations, it is important
to be able to construct a curve that interpolates the data. In much the same way that B-splines can
be used as a basis for constructing a cubic interpolating spline, Nielson and Heiland use the
spherical B-spline to find an interpolating curve which is composed of joining together segments of
third order spherical B/B [Bernstein/Bezier] curves.
[...] They use an iterative method to solve it: [...]

The Minimum Tangential Acceleration Method:
Barret al (1992)
One of the drawbacks to this method is the difficulty with implementing
it and trusting the canned software to actually compute a true minimum.


When one is trying to assess the quality of some animation technique, it is very helpful to observe
or experience the animation. Conventional publication media do not presently allow this. Possibly
some of the new multimedia publications will remove this problem in the future.

---

Crouch et al. 1999:
The De Casteljau Algorithm on Lie Groups and Spheres

[...] and derive expressions for the derivatives of the generalized polynomial curves obtained from the algorithm.
This does not seem to be done elsewhere in the literature.

Thus the algorithm for S mcan be based upon the
somewhat simpler algorithm for SO(m + 1).

much interest has been demonstrated in developing the technique for S3 viewed as
the space of unit quarternions and a convenient parameterization of SO(3).
[...] However, it is clear that the current literature fails to develop
a satisfactory means of dealing with Ck smoothness, k >= 1, because of the
difficulty in dealing with closed form solutions for the derivatives. This has
been achieved in a limited sense in Ge and Ravini [22], but not in a general
framework applicable in a wide variety of problems.

These references also fail to tackle the smoothness of the interpolants
in a completely satisfactory manner. Clearly the smoothness of a curve in
general depends upon its parameterization. For curves on general Rieman-
nian manifolds, one can develop the notion of arc length, induced by the
Riemannian structure. By also developing a means to differentiate which is
compatible with this metric structure, the so-called Riemannian covariant
derivative, one can consider the Ck , k >= 1, smoothness of curves relative to
the arc length parameterization. This can be considered as a measure of the
intrinsic smoothness of the curve, as measured by the Riemannian structure.

[formulation on Riemannian manifolds, following Park and Ravani (1995)]

[formula for second Bezier control point (x2) from first and second derivative
of x0]

The problem is truly a two-point boundary value problem. In the Euclidean
case this is not an immediate computational problem, see Farin [19].
However, in the non-Euclidean case this issue becomes much more involved.
[ -> specify first and second derivative at t=0]
indeed be calculated recursively
using the formulas above.

Blindly using the schemes above does however lead to interpolating curves
which sometimes display wild departures from the set of interpolating data,
as explained in Farin [19].

A few remarks should be made concerning the general applicability of
the De Casteljau construction. Although the geometry of a Riemannian
manifold possesses enough structure to formulate the construction, the ba-
sic ingredients used, the geodesic arcs, are implicitly defined by a set of
nonlinear differential equations. Thus the basic algorithm can be only prac-
tically implemented when we can reduce the calculation of these geodesies
to a manageable form.

In the case of compact Lie groups, the geodesies are just one-parameter
subgroups and hence for matrix compact Lie groups the computation of a
geodesic is just exponentiation of a matrix.

infinitesimal generators of the geodesic curves on G

[... product of exponentials ...]

[derivatives at t=0 and t=1, many proofs ...]

The Lie algebra of SO (3) is so(3), the vector space of skew symmetric 3x3
matrices.

4.1. Example. We have used the formula (18) recursively to implement
the De Casteljau algorithm for a cubic polynomial on the sphere S3.

Interpolating curves satisfying arbitrary boundary conditions on a Rie-
mannian manifold can also be obtained using a variational approach. While
in the Euclidean case both methods produce exactly the same curves, for
general Riemannian manifolds this situation is highly unlikely.

---

Crouch, Silva Leite, Kun 1999
Geometric splines

We examine the De Casteljau Algorithm in the context of Lie groups
and spheres. [...]
We are able to fully develop the algorithm for cubic splines with Hermite boundary
conditions for general n. We implement more general boundary conditions for cubic
splines on the 2-sphere.

[very similar to Crouch et al. 1999 above]

---

Ge and Ravani 1994
Geometric Construction of Bezier Motions

This paper compliments the analytical results presented
in our companion paper (Ge and Ravani, 1994) [Computer Aided ...] in providing
discrete (rather than continuous) computational algorithms for
motion interpolation and approximation.

screw axis, Plücker vectors, dual vector

---

Park and Ravani 1995
Bezier Curves on Riemannian Manifolds and Lie Groups with Kinematics Applications

In principle one can obtain a col-
lection of local coordinate charts for a given curved space, and
apply existing Euclidean interpolation techniques to these co-
ordinates. The resulting curves, however, will depend on the
choice of local coordinates, which clearly leaves something to
be desired from both a mathematical as well as an engineering
perspective. Another requirement motivated by the moving
rigid body problem is that, to the extent possible, the resulting
motions should not depend on the choice of inertial or body-
fixed reference frames; in the language of Lie groups this can
be phrased as the question of whether a group admits a bi-
invariant Riemannian metric. Using standard results from Lie
theory it can be shown that bi-invariant orientation trajectories
can be constructed, but that in general there is no bi-invariant
metric for the spatial displacements (see, e.g., Park et al.,
1993).

Shoemake
(1985) presents a class of methods for generating curves on
rotations that are based on unit quaternion representation.
Although unit quaternions have certain well-known advantages
over other representations of rotations (e.g., Euler angles),
Shoemake's approach is essentially coordinate dependent: the
resulting motions are not invariant with respect to choice of
inertial and body-fixed frames, and his methods do not ade-
quately address the underlying geometry of the space of ro-
tations (e.g., the 2-1 nature of the unit quaternion
representation).

Juettler (1994) has provided a theoretical eval-
uation of several approaches for motion interpolation and has
discussed coordinate frame dependency of some of these ap-
proaches.

In this article we formulate a general framework for con-
structing Bezier curves on Riemannian manifolds, and then
focus specifically on a special class of Riemannian manifold,
the compact Lie groups.

Classical Bezier Curves [...]
Reversing the order of the vertexes results in the same curve.

That Bezier's original construction and De Casteljau's al-
gorithm are equivalent is remarkable, and can fundamentally
be traced to the fact that the curve lies in Euclidean space.

In the De Casteljau method
the concept of linear interpolation between two points in a
curved space needs to be defined; this can be readily done on
a Riemannian manifold, where the minimal geodesic plays the
role of the straight line for curved spaces, and lengths can be
measured in terms of the Riemannian metric. Bezier's con-
struction, however, does not seem to generalize in a natural
way to the Riemannian setting. Although tangency between
curves is well-defined, the notion of an osculating plane relies
inherently on the manifold being embedded in some larger
ambient Euchdean space, and in general there exist several
differnt ways to do this. It is also more desirable to define a
Bezier curve in terms of the intrinsic geometry of the manifold,
rather than the underlying space in which it lies. For Rieman-
nian manifolds, therefore, the natural way to define Bezier
curves is by generalizing De Casteljau's algorithm. Naturally
for certain manifolds the minimal geodesic between two points
may not always be unique, so that a number of subtleties
(addressed below) will arise.

It is clear that constructing Bdzier curves on Riemannian
manifolds by this algorithm is computationally more involved
than for the Euclidean case: computing the geodesic between
any two points involves the solution of the nonUnear differ-
ential equation (1), a two-point boundary value problem (and
therefore more difficult than integrating a differential equation
with only initial conditions). Even if we assume that the geo-
desies forming the control polygon have been precomputed
and stored in a table, for each instant t the geodesic equations
still need to be solved (n-1)(n-2)/2 times. Clearly this
presents difficulties for interactive design applications.

the set of all tangent vectors at p, denoted TpG,
forms a vector space, called the tangent space to G at p. The
tangent space at the identity p = I is given a special name,
called the Lie algebra of G, and denoted by a lower-case g.
On a matrix Lie group the Lie algebra is also given by matrices.
For example, the Lie algebra of SO(3), denoted so(3), is the
set of 3 x 3 real skew-symmetric matrices

one-parameter subgroups of a Lie group [...] minimal-length paths

Riemannian metrics

Any Lie group admits a left- or right
invariant metric from the construction above, but not all Lie
groups admit a bi-invariant metric.

One well-known condition
in which a bi-invariant metric is always guaranteed to exist is
if the Lie group is compact.

The rotation group SO(3), consisting of the 3x3 real or-
thogonal matrices with unit determinant, forms a [compact] Lie group,
with its Lie algebra so(3) given by the vector space of 3 x 3
real skew-symmetric matrices of the form [...]

Lemmas 1 and 2 suggest the standard visualization
of SO(3) as a solid ball of radius \pi, centered at the origin with
the antipodal points identified

[...] the Bezier curve is given by [...]

Hence, given a particular left- or right-invariant Riemannian
metric on SE(3), the corresponding Bezier curve can be con-
structed by combining the appropriate B6zier curves in (R^ and
SO(3). From a physical viewpoint this is more appealing, since
there is nothing natural about the screw motions from the
point of view of dynamics.

---

Jüttler, 1994:
VISUALIZATION OF MOVING OBJECTS USING DUAL QUATERNION CURVES

an interpolating motion whose trajectories are rational Bezier curves is constructed

Dual quaternions
prove to be very useful in computer graphics.

Let some positions ( = points + orientations)
of a moving object in 3-space be given. A continuous
motion interpolating these positions is to be found.

The method [spherical Casteljau] has proved to be powerful, but the in-
terpolating motion possesses some disadvantages: The
trajectories of the moving object are nonrational curves.
( In fact, their explicit parametric representation seems
to be unknown!) The interpolation of more than two
positions by one motion and the construction of higher
than first order continuous spline motions turn out to
be difficult.

Another approach to the solution of the interpolation
problem has been suggested by Ge and Ravani[6].
The positions of the moving objects are represented
using dual quaternion curves without any normaliza-
tion conditions. A multiplication of these curves with
arbitrary dual factors does not change the described
motion. A de Casteljau-like algorithm is formulated,
but the influence of the weights of the control points
(which are dual numbers!) is very complex.

In this paper, the positions of the moving object
will be represented by dual quaternion curves satis-
fying a quadratic normalization condition (Plücker's
condition). These curves can be multiplied with ar-
bitrary real factors without influencing the described
motion. They are described by Bezier curves, therefore
the trajectories of the moving object are rational
Bezier curves, too.

The use of rational motions (i.e., motions with ra-
tional trajectories) has some important advantages: [...]

[...]

The author thinks
that dual quaternion curves have proved to be a very
useful tool in computer graphics.


---

Kuipers 1999
Quaternions and Rotation Sequences

[some Quaternion basics, no splines]

set of all quaternions: non-commutative division ring

section 7: rotation operator geometry

---

Pobegailo 1994
Spherical splines and orientation interpolation

This paper presents a method for design-
ing spherical curves by two weighted spa-
tial rotations.

The de-
signed curves have the following features:
C 1 continuity, local control, and invari-
ance under orthogonal transformations of
coordinate systems.

---

Hanotaux and Peroche 1993
Interactive Control of Interpolations for Animation and Modeling

The parametrization is based on an opti-
mization process.

We distinguish three different ap-
proaches:
• Geometrical construction in quaternion space
• Parametrization of quaternion space
  Our solution, built on a parametrization using quater-
  nion logarithms, is presented below but belongs to this
  category.
• Optimization process

[log, Catmull--Rom interpolation, exp]

it is possible to integrate posi-
tion and orientation in the same interpolation process
[position and logarithm of quaternion]

Indeed, tangents were
designed for finely tuning the curve's appearance, not for
specifying velocity at key-frames.

A standard solution to solve these problems is based on a
reparametrization of the trajectory.

However, such a reparametrization presents, from our point
of view, the drawback to require the specification of still an-
other curve, hence more and more interaction. Our aim is to
develop a technique allowing the automatic reparametriza-
tion of interpolation curves. However, we also wish to let
the user have the possibility to modify the proposed solution
with the help of additional constraints.

As we want to generate realistic motion, we choose to min-
imize the sum of the forces required to realize this motion.
This principle is suggested by the fact that realistic motions
tend to minimize the energy expanded to perform them [17] .
According to Newton's law, it comes down in fact to min-
imizing the sum of the accelerations occurring during the
motion. The scheme we have chosen is based on an opti-
mization technique.

Of course, we also want to reparametrize orientation curves.
The objectives are equivalent to those regarding positions,
except we now have to minimize the sum of the torques
applied to the animated body.

In fact, we do not parametrize positions independently from
orientations. Indeed, it would lead in most cases to two dif-
ferents time parameter sets. In consequence, we choose to
minimize both translational and angular accelerations. The
new criterion is the sum of the previous criterions for po-
sition and orientation.

The parametrization
used seems easier to understand and to implement than those
previously presented.


