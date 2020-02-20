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
approaches:   geometrictransliteration,  differential  equations,  and  arc
blends.  Here  is  a  reference  for  each:  J.Schlag,   “Using   Geometric
Construction   to   Interpolate   Orientations   withQuaternions”  in Graphics
Gems  II,  Academic  Press,  1991,  pp.  377–380;  A.  Barr,  B.Currin,  S.
Gabriel,  and  J.  Hughes,  “Smooth  Interpolation  of  Orientations
withAngular  Velocity  Constraints  using  Quaternions”  in Proceedings  of
SIGGRAPH  ’92,ACM  Press,  1992,  pp.  313–320;  W.  Wang  and  B.  Joe,
“Orientation  Interpolation  inQuaternion  Space  Using  Spherical  Biarcs”  in
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
