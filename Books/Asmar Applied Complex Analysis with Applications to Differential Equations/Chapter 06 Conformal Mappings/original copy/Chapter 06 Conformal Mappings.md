<!-- Page 1 -->

Left margin note (page 1)

Topics to Review To motivate the mat tions $6.1-6.3$, you sh Section 2.5. Section 6 ear fractional transfo uses the maximum m ciple (Theorem 5, and Example 3. Secti tion 6.3 expands on tions from Section 2 the Poisson integral the disk in Section 3 the corresponding for upper half-plane. Se based on Section 6.3. to the theory of analy that we have develop ous chapters, in Secti 6.6, we will also deriv facts from calculus of ables, in particular, G tities. The approach functions and Neumar in Sections 6.5 and on a change of variab present in Section 6. can be motivated by of variables that we p Section 3.8 to derive integral formula on th

Looking Ahead This chapter is optio highly recommended tration of the advance of complex analysis in plied problems. Secti 6.2 are background o material. Sections 6. $6.5-6.6$ can be covere dently. Sections 6.5 a at a higher level pel the previous sections. be covered after acqu familiarity with boun problems from Chapte

++++

erial in Sec-
ould review
2 treats lin-
rmations. It
odulus prin-
Section 3.7)
on 3.7. Sec-
the applica-
.5 and uses formula on 8 to derive mula in the ction 6.4 is In addition ic functions ed in previons 6.5 and e additional several varireen's idento Green's in functions J. 6 is based les that we 5 and that the change erformed in the Poisson e disk.
nal, but is as an illused methods solving apons 6.1 and r reference 3, 6.4, and d indepenand 6.6 are haps than They can iring more dary value r 8.

6
CONFORMAL MAPPING
First, it is necessary to study the facts, to multiply the number of servations, and then later to search for formulas that connect ther as thus to discern the particular laws governing a certain class of p nomena. In general, it is not until after these particular laws have $b$ established that one can expect to discover and articulate the more $g$ eral laws that complete theories by bringing a multitude of apparer very diverse phenomena together under a single governing principt
-Augustin Louis Cauc
This chapter presents a sampling of successful applications of co plex analysis in applied mathematics, engineering, and physics. Af laying down the theory and methods of conformal mappings in S tion 6.1 and expanding our list of conformal mappings in Section 6 we revisit in Section 6.3 the Dirichlet problems that we started in S tion 2.5 and go far beyond the examples of that section. In particul we derive Poisson's integral formula in the upper half-plane and ma other regions, by performing a change of variables in the formula the disk. In Section 6.4, we broaden the scope of our applicatic with the Schwarz-Christoffel transformation, which is a method finding conformal mappings of regions bounded by polygonal pat) The section contains interesting applications from fluid flow.

Recall that Poisson's formula on the disk (or the upper half-plan gives the solution of Dirichlet problems in the form of an integral volving the boundary function. A natural question is whether a simil formula, a generalized Poisson integral formula, exists on different gions of the plane. In Section 6.5, we derive this formula on simp connected regions, in terms of the so-called Green's function. The s lution is based on a simple change of variables and the mean val property of harmonic functions. Our approach justifies the properti of this important tool, Green's functions, and illustrates in a natur way their applications to the solution of boundary value problems.

In Section 6.6, we tackle other famous boundary value problen involving Laplace's equation and Poisson's equation. We take t same approach as in Section 6.5, based on changes of variables usi conformal mappings, and derive general formulas for the solution terms of Green's functions and the so-called Neumann function. Bo functions are computed explicitely in important special cases.

---

<!-- Page 2 -->

Left margin note (page 2)

386
Chapter 6
6.1 Basic

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-02_515_532_332_99.jpg)

Figure 1 The dir tangent line at $z( \arg z^{\prime}(t)$.

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-02_492_502_1244_134.jpg)

Figure 2 The $\gamma_{2}$ intersect at a

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-02_513_1088_1989_791.jpg)

Figure 3 A li $f(z)=a z+b($
by an angle ar a factor $|a|$, an b. In particula angles between

Right margin note (page 2)

lytic will the gent the $y(t)$, that line this the
that $\gamma_{2}$ at lines
ed in $z)=$ der a g our abers, otate then es not of the paths in the ve by till $\alpha$. kwise

++++

Conformal Mappings
Properties
Our goal in this section is to present properties of mappings by ana functions. These basic properties are interesting in their own right and
ection of the $t$ ) is given by
curves $\gamma_{1}$ and ngle $\alpha$.
be very useful to us when solving partial differential equations involving Laplacian. We start with a review from calculus of the notion of tan lines to curves in parametric form. We will state these results using convenient complex notation.

Suppose that $\gamma$ is a smooth path parametrized by $z(t)=x(t)+i a \leq t \leq b$. Write $\frac{d z}{d t}=z^{\prime}(t)=x^{\prime}(t)+i y^{\prime}(t)$. Let us also assume $z^{\prime}(t) \neq 0$, as this will guarantee the existence of a tangent. The tangent to the curve at $z(t)$ points in the direction of $z^{\prime}(t)$; we can characterize direction by specifying $\arg z^{\prime}(t)$ (see Figure 1). Thus the direction of tangent line at a point on a path $z(t)$ is given by the argument of $z^{\prime}(t)$

Let $z_{0}$ be a point in the $z$-plane, let $\gamma_{1}$ and $\gamma_{2}$ be two smooth paths intersect at $z_{0}$, and let $L_{1}$ and $L_{2}$ denote the tangent lines to $\gamma_{1}$ and $z_{0}$. We will say that $\gamma_{1}$ and $\gamma_{2}$ intersect at angle $\alpha$ at $z_{0}$ if the tangent $L_{1}$ and $L_{2}$ intersect at angle $\alpha$ at $z_{0}$ (Figure 2).

To explain the geometric meaning of the mapping properties discuss this section, let us consider the simple example of a linear mapping $f a z+b$, where $a \neq 0$ and $b$ are complex numbers. As usual, we consi mapping as taking points in the $z$-plane to points in the $w$-plane. Usin geometric interpretation of addition and multiplication of complex num we see that the effect of the linear mapping $f(z)=a z+b$ is to $r$ by a fixed angle equal to $\arg a$, dilate by a factor equal to $|a|$, and translate by $b$. (Note that the rotation and dilation commute, so it do matter which one you apply first. But you cannot change the order translation; it comes last.) In particular, if $\gamma_{1}$ and $\gamma_{2}$ are two smooth that intersect at angle $\alpha$ at $z_{0}$, then their images by $f$ are two paths $w$-plane that intersect at $w_{0}=f\left(z_{0}\right)$; since $f(z)$ has rotated each cur the same angle $\arg a$, the angle of their intersection in the $w$-plane is $s$ Furthermore, $\gamma_{1}$ 's orientation as being either clockwise or counterclo of $\gamma_{2}$, is preserved (Figure 3).

near mapping
$a \neq 0$ ) rotates
$\mathrm{g} a$, dilates by
1 translates by
ir, it preserves
curves.

---

<!-- Page 3 -->

Left margin note (page 3)

THEOR CONFOR PROPE

Right margin note (page 3)

387
wing
if $f$
tion.
udy
tely
$$
+b,
$$
ered $s$ by the
$z_{0}$.
$(t)$, ized the ule, (t))
ates ves
ms low y a ary the in is $\Omega$.
$2 \pi\}$.

++++

Section 6.1 Basic Properties

With the example of the linear mapping in mind, we introduce the follo basic property. A mapping $w=f(z)$ is said to be conformal at $z_{0}$ preserves angles between curves at $z_{0}$ and preserves their angular orienta

Now suppose that $f(z)$ is analytic at $z_{0}$ and $f^{\prime}\left(z_{0}\right) \neq 0$. From our s of the derivative in Section 2.3 (Theorem 5), we know that $f$ is approxima linear in the neighborhood of $z_{0}$. More precisely, we have
$$
f(z)=f\left(z_{0}\right)+f^{\prime}\left(z_{0}\right)\left(z-z_{0}\right)+\epsilon(z)\left(z-z_{0}\right)
$$
where $\epsilon(z) \rightarrow 0$ as $z \rightarrow z_{0}$. So, near $z_{0}$, we can write $f(z) \approx f^{\prime}\left(z_{0}\right) z$ where $b=-f^{\prime}\left(z_{0}\right) z_{0}+f\left(z_{0}\right)$ is a constant. From what we just discov about linear mappings, this suggests that $f$ is conformal at $z_{0}$; it rotate an angle $\theta=\arg f^{\prime}\left(z_{0}\right)$ and scales by a factor $\left|f^{\prime}\left(z_{0}\right)\right|$. Indeed, we have following important result.

EM 1
MAL
Suppose that $f$ is analytic at $z_{0}$ and $f^{\prime}\left(z_{0}\right) \neq 0$, then $f$ is conformal at
ERTY

Proof Let $\gamma$ be any smooth path through $z_{0}$, parametrized by $z(t)=x(t)+i$ with $z\left(t_{0}\right)=z_{0}$ and $z^{\prime}\left(t_{0}\right) \neq 0$. Then the image of $\gamma$ by $f$ is a path parametr by $f(z(t))$ that goes through $w_{0}=\gamma\left(z_{0}\right)$ in the $w$-plane. Since $z^{\prime}\left(t_{0}\right) \neq 0$, direction of the tangent line to $\gamma$ at $z_{0}$ is $\arg z^{\prime}\left(t_{0}\right)$. Also, from the chain $r \left.\frac{d}{d t} f(z(t))\right|_{t_{0}}=f^{\prime}\left(z\left(t_{0}\right)\right) z^{\prime}\left(t_{0}\right) \neq 0$ and so the direction of the tangent line to $f(z$ at $w_{0}=f\left(z_{0}\right)$ is
$$
\arg \left(\left.\frac{d}{d t} f(z(t))\right|_{t_{0}}\right)=\arg \left(f^{\prime}\left(z\left(t_{0}\right)\right) z^{\prime}\left(t_{0}\right)\right)=\arg f^{\prime}\left(z\left(t_{0}\right)\right)+\arg z^{\prime}\left(t_{0}\right) .
$$

Hence $f(z)$ rotates the tangent line at $z_{0}$ by a fixed angle $\arg f^{\prime}\left(z_{0}\right)$. Since $f$ rot any two tangent lines intersecting at $z_{0}$ by the same angle $\arg f^{\prime}\left(z_{0}\right)$, it prese the angle of intersection and their orientation.
Boundary Behavior
We will use conformal mappings to transform boundary value proble consisting of Laplace's equation along with boundary conditions. We kr from Section 2.5, Theorem 3, that Laplace's equation is not changed b conformal mapping. To handle the effect of the mapping on the bound conditions, it would be nice to know that the boundary is mapped to boundary. But as the following simple example shows, this may fail general.

EXAMPLE 1 Boundary points mapped to interior points
Consider $f(z)=z^{2}$ and $\Omega=\left\{z=r e^{i \theta}: \frac{1}{2}<r<1,-\pi<\theta<\pi\right\}$. Then analytic and $f^{\prime}(z)=2 z \neq 0$ for all $z$ in $\Omega$. Hence $f(z)$ is conformal at each $z$ in Since $z^{2}=r^{2} e^{2 i \theta}$ it is easy to see that $f[\Omega]$ is the annulus
$$
f[\Omega]=\left\{w=r e^{i \theta}: \frac{1}{4}<r<1,-2 \pi<\theta<2 \pi\right\}=\left\{w=r e^{i \theta}: \frac{1}{4}<r<1,0 \leq \theta \leq\right.
$$

---

<!-- Page 4 -->

Left margin note (page 4)

388
Chapter 6

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-04_519_1089_205_728.jpg)

Figure 4 The func $z^{2}$ is conformal in the interval ( -1 , boundary of $\Omega$ to $\left(\frac{1}{4}, 1\right)$ in the inter Thus $f$ does not n ary points to boune

THI
BOI
BE

Right margin note (page 4)

pped $\rho$ the
$f$ is ntire $z$ ) is e we $f$ is the t be cribe lary $\left\{z_{n}\right\}$ any rges, e are egion
ry of lence $w_{0}$.
ps the
$\_\_\_\_$
$f[\Omega]$. 1 that o-one.

++++

Conformal Mappings
tion $f(z)= \Omega$. It takes $-\frac{1}{2}$ ) on the the interval ior of $f[\Omega]$. nap boundlary points.

EOREM 2
UNDARY
JHAVIOR

It is also easy to see that the boundary points $z=x,-1 \leq x \leq-\frac{1}{2}$ are ma to the interior points $w=u, \frac{1}{4} \leq u \leq 1$ (see Figure 4). Thus $f$ does not ma boundary of $\Omega$ to the boundary of $f[\Omega]$.

Recall from Section 5.7 that the condition $f^{\prime}(z) \neq 0$ ensures that one-to-one locally at $z$. The function may fail to be one-to-one on the $\mathbf{e}$ region $\Omega$, which was the case in Example 1. We will show that if $f($ analytic and one-to-one then it will map boundary to boundary. Befor do so, let us clarify certain issues. We know from Section 5.7 that if analytic and nonconstant on a region $\Omega$, then $f[\Omega]$ is a region. So al points in $\Omega$ are mapped to (interior) points in $f[\Omega]$. Now $f$ might no defined on the boundary of $\Omega$, so we need a special definition to des how $f$ maps the boundary of $\Omega$. We will say that $f$ maps the bound of $\Omega$ to the boundary of $f[\Omega]$ if the following condition holds. If is any sequence in $\Omega$ converging to $\alpha_{0}$ on the boundary of $\Omega$ and $\beta$ is point in $f[\Omega]$, then $\left\{f\left(z_{n}\right)\right\}$ does not converge to $\beta$. So if $\left\{f\left(z_{n}\right)\right\}$ conve it must converge to a boundary point of $f[\Omega]$ or to infinity. (Ther examples where $\left\{f\left(z_{n}\right)\right\}$ does not converge; see Exercise 21.) If the r $\Omega$ is unbounded, we allow putting $\alpha_{0}=\infty$.

We will say that $f$ maps the boundary of $\Omega$ onto the bounda $f[\Omega]$ if for every point $w_{0}$ on the boundary of $f[\Omega]$, we can find a sequ $z_{n}$ in $\Omega$ where $z_{n} \rightarrow \alpha_{0}, \alpha_{0}$ being on the boundary of $\Omega$, and $f\left(z_{n}\right) \rightarrow$

We have the following important result.
Suppose that $f$ is analytic and one-to-one in a region $\Omega$. Then $f$ ma boundary of $\Omega$ to the boundary of $f[\Omega]$, and this map is onto.
Proof We will prove that $f$ maps the boundary of $\Omega$ to the boundary of leaving the "onto" part for Exercise 20. Let $\left\{z_{n}\right\}$ be a sequence in $\Omega$ sucl $f\left(z_{n}\right) \rightarrow \beta$, where $\beta$ is an interior point of $f[\Omega]$. Since $f$ is analytic and one-t $f^{-1}$ exists and is analytic, and hence continuous. Thus
$$
\lim _{n \rightarrow \infty} z_{n}=\lim _{n \rightarrow \infty}\left(f^{-1}\left(f\left(z_{n}\right)\right)\right)=f^{-1}\left(\lim _{n \rightarrow \infty} f\left(z_{n}\right)\right)=f^{-1}(\beta),
$$
so $z_{n}$ converges to an interior point of $\Omega$.

---

<!-- Page 5 -->

Left margin note (page 5)

COROLLA

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-05_411_1226_1169_630.jpg)

Figure 5 The fact th boundary of $f[\Omega]$ is axis implies that $f[\Omega]$ ther the upper or lowe plane. We decide whic it is by checking the of one point. Note ho right angles at $z= \pm$ flattened by $f$ in the $w$ The function $f$ is still c mal in $\Omega$, even though $f$ conformal at two points boundary.

++++

Section 6.1 Basic Properties

If the conformal mapping can be extended to a continuous function the boundary, the following version of Theorem 2 will be useful.

RY 1

Suppose that $f$ is analytic and one-to-one in a region $\Omega$. Let $\alpha$ be any p of the boundary of $\Omega$ such that $f$ is continuous at $\alpha$. Then $f(\alpha)$ is a po on the boundary of $f[\Omega]$.
Proof Let $\left\{z_{n}\right\}$ be a sequence in $\Omega$ converging to $\alpha$ on the boundary of $\Omega$. Sin $f$ is continuous at $\alpha, f\left(z_{n}\right)$ converges to $f(\alpha)$. By Theorem 2, $f(\alpha)$ is a bounda point of $f[\Omega]$.

The fact that the boundary is mapped to the boundary helps us dete mine the image of a region from our knowledge of the image of the boundar and one interior point. Let us illustrate this useful technique by revisitin an example from Section 1.6.

EXAMPLE 2 Mapping of regions
Let $f(z)=\sin z$ and $\Omega=\left\{z=x+i y:-\frac{\pi}{2}<x<\frac{\pi}{2}, y>0\right\}$. Thus $\Omega$ is th
at the the $u$ is eir halfh half image w the $\frac{\pi}{2}$ got plane. onforis not on the semi-infinite vertical strip shown in Figure 5. Since $\sin z_{1}=\sin z_{2}$ if and only i $z_{1}=z_{2}+2 k \pi$ ( $k$ an integer), we see that $f$ is one-to-one on $\Omega$. Also, $f$ is continuou on the boundary of $\Omega$.

We start by determining the image of the boundary. For $z=x$ real, we have $f(z)=\sin x$, and so $f$ maps the interval $-\frac{\pi}{2} \leq x \leq \frac{\pi}{2}$ onto the interval $[-1,1]$. For $z=\frac{\pi}{2}+i y$, we have $f(z)=\sin \left(\frac{\pi}{2}+i y\right)=\cosh y$, a real number (see (16), Section 1.6). So $f$ maps the vertical semi-infinite line $z=\frac{\pi}{2}+i y(y \geq 0)$ onto the semiinfinite interval $[1, \infty)$. For $z=-\frac{\pi}{2}+i y$, we have $f(z)=\sin \left(-\frac{\pi}{2}+i y\right)=-\cosh y$ (see (16), Section1.6). So $f$ maps the vertical semi-infinite line $z=-\frac{\pi}{2}+i y(y \geq 0)$ onto the semi-infinite interval $(-\infty,-1]$. Thus, $f$ maps the boundary of $\Omega$ to the real axis. According to Theorem 2, the image of the vertical strip has boundary the $u$-axis, so it is either the upper or the lower half-plane. Checking the value of $f$ at one point in $\Omega$, say $z=i$, we find $f(i)=\sin (i)=i \sinh (1)$, which is a point in the upper half. Thus the image of $\Omega$ is the upper half-plane.

As a further application, we consider the Joukowski function
$$
J(z)=\frac{1}{2}\left(z+\frac{1}{z}\right) \quad(z \neq 0)
$$

This function has applications in aerospace engineering.

---

<!-- Page 6 -->

Left margin note (page 6)

390
Chapter 6

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-06_475_1345_597_700.jpg)

Figure 6 The function maps th one-to-one onto half-plane. It also upper semi-circle $R>1, x^{2}+y^{2}=$ to the upper semi-

Right margin note (page 6)

$$
\begin{array}{l}
\theta \leq \pi\} \\
\text { Arg } z \leq
\end{array}
$$
of the e semiAs $x$ (in the If we y 1 that termine al at all hat $J$ is $1 z_{2}=1$. $\frac{3 i}{4}$. Since lane. all $z$ in vever, if for all 'e know to-one.

++++

Conformal Mappings

EXAMPLE 3 The Joukowski mapping
(a) Show that $J(z)$ maps the upper unit semicircle $\sigma=\left\{z: z=e^{i \theta}, 0 \leq\right.$ onto the real interval $J[\sigma]=[-1,1]$, and the semi-infinite intervals $[1$, $(-\infty,-1]$ onto themselves.
(b) Show that the Joukowski function maps the set $\Omega=\{z:|z| \geq 1,0 \leq \pi\}$ onto the upper half-plane $\{w=u+i v: v \geq 0\}$ (see Figure 6). A more description of the Joukowski mapping is outlined in Exercise 17.

Joukowski region $\Omega$ the upper maps the of radius $R^{2}, y \geq 0$, ellipse $\frac{w)^{2}}{\left.\left.\frac{1}{k}\right)\right]^{2}}=1$, ercise 17.)

Solution (a) For $z=e^{i \theta}, 0 \leq \theta \leq \pi$, we have
$$
w=J(z)=\frac{1}{2}\left(e^{i \theta}+\frac{1}{e^{i \theta}}\right)=\frac{1}{2}\left(e^{i \theta}+e^{-i \theta}\right)=\cos \theta
$$

As $\theta$ varies from 0 to $\pi, w$ varies from 1 to -1 , showing that the imag upper semi-circle is the interval $[-1,1]$. To determine the images of th infinite intervals $[1, \infty)$ and $(-\infty,-1]$, let $z=x$; then $J(z)=\frac{1}{2}\left(x+\frac{1}{x}\right.$ varies through $[1, \infty)$ or $(-\infty,-1], J(x)$ varies through the same interval $w$-plane).
(b) We showed in (a) that $J$ maps the boundary of $\Omega$ onto the real axi can show that $J$ is conformal and one-to-one, it will follow from Corollar $J[\Omega]$ is either the upper or the lower half of the $w$-plane. We can then de which half it is by checking the image of one point in $\Omega$. That $J$ is conform points in $\Omega$ is clear from $J^{\prime}(z)=\frac{1}{2}\left(1-\frac{1}{z^{2}}\right) \neq 0$ for all $|z|>1$. To show $t$ one-to-one, let $z_{1}, z_{2}$ be in $\Omega$, and suppose that $J\left(z_{1}\right)=J\left(z_{2}\right)$. Then
$$
\begin{aligned}
z_{1}+\frac{1}{z_{1}}=z_{2}+\frac{1}{z_{2}} & \Rightarrow \frac{z_{1}^{2}+1}{z_{1}}=\frac{z_{2}^{2}+1}{z_{2}} \\
& \Rightarrow z_{2} z_{1}^{2}+z_{2}-z_{1} z_{2}^{2}-z_{1}=0 \\
& \Rightarrow\left(z_{1}-z_{2}\right)\left(z_{1} z_{2}-1\right)=0
\end{aligned}
$$

So either $z_{1}=z_{2}$ or $z_{1} z_{2}=1$. Since $1<\left|z_{1}\right|$ and $1<\left|z_{2}\right|$, we cannot have So $z_{1}=z_{2}$, implying that $J$ is one-to-one. We have $J(2 i)=\frac{1}{2}\left(2 i+\frac{1}{2 i}\right)= J(2 i)$ is in the upper half-plane, we conclude that $J[\Omega]$ is the upper half-p

As we observed following Example 1 , the condition $f^{\prime}(z) \neq 0$ for a region $\Omega$ is not enough to ensure that $f$ is one-to-one on $\Omega$. Hov $f$ is analytic and one-to-one on the whole region $\Omega$, then $f^{\prime}(z) \neq z$ in $\Omega$, so $f$ is a conformal mapping. Moreover, from Section 5.7, v that the inverse function exists on $\Omega^{\prime}=f[\Omega]$ and is analytic and one

---

<!-- Page 7 -->

Left margin note (page 7)

THEORI
RIEM
MAPF
THEOI

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-07_517_1143_1623_681.jpg)

Figure 7 A one-to-one formal mapping $f$ of $\Omega$ the unit disk $D=f[\Omega]$ boundary to boundary preserves Laplace's equ It transforms a Dirichlet lem on $\Omega$ into a Dir problem on $D$, which ca solved using the Poissor mula. The solution in then $u(z)=U(f(z))$.

++++

Section 6.1 Basic Properties

In this situation, we will say that $\Omega$ and $\Omega^{\prime}$ are conformally equivale regions.

The following famous theorem of Riemann tells us that any simply c nected region of the complex plane other than the plane itself is conforma equivalent to the open unit disk.

EM 3

Let $\Omega$ be a simply connected region in the complex plane other than

ANN complex plane itself. Then there is a one-to-one analytic function $f$

ING maps $\Omega$ onto the unit disk $|w|<1$. The mapping $f$ is unique if we spe

REM that $f\left(z_{0}\right)=0$ and $f^{\prime}\left(z_{0}\right)>0$, for some $z_{0}$ in $\Omega$.

The proof of the Riemann mapping theorem is above the level of $t$ book. We refer you to Ahlfors [1] or Conway [10].

Combined with the Poisson integral formula, which solves the Dirich problem with arbitrary boundary data on the disk, the Riemann mappi theorem implies that we can at least theoretically solve the Dirichlet proble on any simply connected region $\Omega$. As illustrated in Figure 7, it suffices conformally map $\Omega$ in a one-to-one way onto the unit disk. This gives r to a new boundary value problem on the disk, which can be solved using $t$ Poisson formula. The solution of the original problem is then obtained composing the solution on the disk with the conformal mapping. As sim] and elegant as it is, this approach has its limitations. Even though we ha several powerful tools, such as Fourier series and techniques for evaluati integrals using residues, our experience with the Poisson formula tells that this formula is not easy to compute in general. Even more difficult the actual construction of the conformal mapping from $\Omega$ onto the unit dis While the Riemann mapping guarantees its existence, it gives no clue as how to construct it.
$$
\begin{array}{l}
\text { con- } \\
\text { onto } \\
\text { takes } \\
\text { and } \\
\text { ation. } \\
\text { prob- } \\
\text { ichlet } \\
\text { an be } \\
\text { a for- } \\
\Omega \text { is }
\end{array}
$$

In the following sections, we will take up the construction of importa conformal mappings that will lead us to very challenging problems. We u also give several applications to the solution of Laplace's equation.

---

<!-- Page 8 -->

Left margin note (page 8)

392
Chapter 6

++++

Conformal Mappings

Exercises 6.1
In Exercise 1-6, determine where the given mapping is conformal.
1. $\frac{z^{2}+1}{e^{z}}$.
2. $\frac{z+1}{z^{2}+2 z+1}$.
3. $\frac{\sin z}{e^{z}}$.
4. $\frac{e^{z}+1}{e^{z}-1}$.
5. $z+\frac{1}{z}$.
6. $\frac{z+1}{z+i}+\frac{2}{z}$.

In Exercise 7-12, determine the angle of rotation $\alpha=\arg f^{\prime}(z)$ and the factor $\left|f^{\prime}(z)\right|$ of the given mapping at the indicated points.
7. $\frac{1}{z}, z=1, i, 1+i$.
8. $\log z, z=1, i,-i$.
9. $\sin z, z=0, \pi+$
10. $z^{2}, z=0,2 i,-1-i$.
11. $e^{i z}, z=\pi, i \pi, \frac{\pi}{2}$.
12. $\frac{1+e^{z}}{1-e^{z}}, z=1, i \pi, \ln (3)+2 i$.

Consider the orthogonal lines $x=a$ and $y=b$, where $a$ and $b$ are real $r$ Determine their images by the given mapping $f(z)$. For which values of a the images orthogonal at the point of intersection $f(a+i b)$ ? Verify your a computing the angle between the image curves at the point $f(a+i b)$.
13. $e^{z}$.
14. $\sin z$.
15. $(1+i) z$.
16. $\frac{z+1}{z-1}$
17. The Joukowski function. Refer to Example 3.
(a) Show that $J\left(\frac{1}{z}\right)=J(z)$ for all $z \neq 0$.
(b) Fix $R>1$. Show that the upper semicircle of radius $R, S_{R}=\{2 R, 0 \leq \operatorname{Arg} z\}$, is mapped onto the upper semi-ellipse
$$
J\left[S_{R}\right]=\left\{w=u+i v: \frac{u^{2}}{\left[\frac{1}{2}\left(R+\frac{1}{R}\right)\right]^{2}}+\frac{v^{2}}{\left[\frac{1}{2}\left(R-\frac{1}{R}\right)\right]^{2}}=1, v \geq 0\right\}
$$
18. Let $S$ denote the region in the upper half-plane consisting of all $z \mathrm{~s} 1<|z|$. Consider the Dirichlet problem in $S$ with boundary conditions $u$ 100 if ( $x, y$ ) is on the upper unit circle, and $u(x, 0)=0$ for all $1<|x|$. result of Exercise 35, Section 2.5, show that a solution is given by
$$
u(x, y)=\frac{100}{\pi}(\operatorname{Arg}(J(z)-1)-\operatorname{Arg}(J(z)+1)) \quad(z=x+i y)
$$
where $J(z)$ is the Joukowski function.
19. Consider $f(z)=\frac{z}{(1-z)^{2}}$. (a) Show that for all $z \neq 1, f(z)$ is ana $f^{\prime}(z) \neq 0$ for $z \neq-1$. (b) Show that $f$ is one-to-one in the open unit di not one-to-one in any larger disk centered at 0 .
20. Let $f$ be as in Theorem 2. Fill in the details in the following proc maps the boundary of $\Omega$ onto the boundary of $f[\Omega]$. Let $w_{0}$ be on the bot $f[\Omega]$; then we can find points $w_{n}=f\left(z_{n}\right)$ such that $z_{n}$ is in $\Omega$ and $w_{n} \rightarrow w_{1}$ Distinguish two cases. If the sequence $\left\{z_{n}\right\}$ is unbounded, then a subseque tends to $\infty$, which is a point on the boundary of $\Omega$, and $f\left(z_{n_{j}}\right) \rightarrow w_{0}$. bounded, then by the Bolzano-Weierstrass property, we can find a sub $\left\{z_{n_{j}}\right\}$ that converges in $\Omega$ union its boundary. Show that $\left\{z_{n_{j}}\right\}$ cannot

---

<!-- Page 9 -->

Left margin note (page 9)

6.2 Linear Frac

PROPOSITION
BASIC PROPERTI

++++

Section 6.2 Linear Fractional Transformations
393

to a point in $\Omega$ and so it must converge to a point $z_{0}$ on the boundary. Moreover, $f\left(z_{n_{j}}\right) \rightarrow w_{0}$.
21. Let $\Omega$ be the slit plane, $\mathbb{C} \backslash\{z: z \leq 0\}$, and $f(z)=\log z$. Show that the sequence $z_{n}=-1+i \frac{(-1)^{n}}{n}(n=1,2, \ldots)$ converges to -1 on the boundary of $\Omega$ and yet $f\left(z_{n}\right)$ does not converge.
tional Transformations
It should be clear by now from our work in Sections 2.5 and 6.1 that our success in solving boundary value problems involving Laplace's equation is closely tied to our ability to construct conformal mappings between regions in the plane. A good place to start our study of special conformal mappings is on the unit disk, since there we have a general formula for the solution of the Dirichlet problem, namely the Poisson integral formula. As we will soon see, the most suitable mappings for regions involving disks and lines are the linear fractional transformations that we introduced in Section 1.4:
$$
\phi(z)=\frac{a z+b}{c z+d} \quad(a d \neq b c)
$$

Since $\phi^{\prime}(z)=\frac{a d-b c}{(c z+d)^{2}}$, the condition $a d \neq b c$ ensures that $\phi$ does not degenerate into a constant. If $c=0$, the linear fractional transformation reduces to a linear function, which is analytic everywhere or entire. If $c \neq 0$, then $\phi$ is analytic for all $z \neq-\frac{d}{c}$ and has a simple pole at $z=-\frac{d}{c}$.

N 1

Let $\phi(z)$ be a linear fractional transformation as in (1). Then

ES
(i) $\phi$ is one-to-one throughout the complex plane and conformal at every point in the complex plane, except at the pole $z=-\frac{d}{c}(c \neq 0)$.
(ii) The inverse of $\phi(z)$ is the linear fractional transformation given by
(2)
$$
z=\psi(w)=\frac{d w-b}{-c w+a}
$$

Proof The proposition is clear if $c=0$. Suppose $c \neq 0$. Then
$$
\phi^{\prime}(z)=\frac{a d-b c}{(c z+d)^{2}} \neq 0 \text { for all } z \neq-\frac{d}{c}
$$

Hence by Theorem 1, Section 6.1, the mapping is conformal at all $z \neq-\frac{d}{c}$. To get the inverse function, we solve $w=\frac{a z+b}{c z+d}$ for $z$, and get $z=\frac{d w-b}{-c w+a}$. Since $\phi$ has an inverse, it must be one-to-one, for if $\phi\left(z_{1}\right)=\phi\left(z_{2}\right)$ taking the inverse function of both sides, we get $z_{1}=z_{2}$.

It is not hard to see that every linear fractional transformation (1) with $c \neq 0$ is a composition of a linear mapping $w_{1}=c z+d$; an inversion $w_{2}=\frac{1}{w_{1}}$; and a linear mapping $w=\frac{a}{c}+\left(b-\frac{a d}{c}\right) w_{2}$ (see Exercise 41 ). Now linear

---

<!-- Page 10 -->

Left margin note (page 10)

394
Chapter 6

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-10_538_1120_471_762.jpg)

Figure 1 The $f(z)=\frac{1}{z}$ pre collection of lines To verify the ima given lines and the fact that $f$ is (preserves angles) values $f(0)=\infty$; $f( \pm 1)= \pm 1 ; f( \pm i f\left(\frac{3}{4}\right)=\frac{4}{3}$.

PROPO
IMAGES AND

Right margin note (page 10)

lap a
what
ne to
pings,
e 1.)
ight-
rans-
erits
lines
pre-
ry to
ining
plane

ine or cle, it

++++

Conformal Mappings
mappings have a very useful property that is easy to verify: They n line to a line and a circle to a circle. The inversion $w_{2}=\frac{1}{w_{1}}$ has a some similar property: It maps the collection of lines and circles in the $z$-pla the collection of lines and circles in the $w$-plane. (Unlike linear mapI the inversion may map a line to a circle or a circle to a line; see Figur
inversion serves the and circles. iges of the circles, use conformal and the
$$
f(\infty)=0 ;
$$
$$
)=\mp i ;
$$

\section*{SITION 2 DF LINES CIRCLES}

This property of the inversion is not as simple to verify but it is stra forward and is sketched in Exercises 35-40. Since a linear fractional t, formation is a composition of linear mappings and an inversion, it inb this property too. Thus we obtain the following very useful result.
Let $\phi(z)$ be a linear fractional transformation as in (1). Then $\phi$ maps and circles in the $z$-plane to lines and circles in the $w$-plane.

It follows immediately from Proposition 1 and Theorem 2 of the vious section that a linear fractional transformation will map bounda boundary. As we now illustrate, this property is very useful in determ the image of a region.

EXAMPLE 1 Mappings between the unit disk and the upper half-I
(a) Show that the linear fractional transformation
$$
\phi(z)=i \frac{1-z}{1+z}
$$
maps the unit disk onto the upper half-plane.
(b) Show that the linear fractional transformation
$$
\psi(z)=\frac{i-z}{i+z}
$$
maps the upper half-plane onto the unit disk.
Solution (a) By Proposition 2, the image of the circle $C_{1}(0)$ is either a 1 a circle in the $w$-plane. Since three points will determine either a line or cir suffices to check the images of three points on $C_{1}(0)$. We have
$$
\phi(1)=0 ; \quad \phi(i)=i \frac{1-i}{1+i}=1 ; \quad \phi(-i)=i \frac{1+i}{1-i}=-1 .
$$

---

<!-- Page 11 -->

Left margin note (page 11)

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-11_503_1064_531_675.jpg)

Figure 2 The image unit circle is determin the images of three Since these are collinea circle is therefore mapp a line (the real axis, case). Note also that be $\phi$ maps the closed uni to an unbounded regio upper half-plane), $\phi$ l be discontinuous some in the closed unit disk. it is singular at $z=-1$.

PROPOSITI
COMPOSITION
MAPPI

Right margin note (page 11)

To

++++

Section 6.2 Linear Fractional Transformations
395

Thus $\phi(1), \phi(i)$, and $\phi(-i)$ lie on the $u$-axis (the real axis in the $w$-plane), and so the image of $C_{1}(0)$ is the $u$-axis. Because $\phi$ is one-to-one, it maps the boundary $C_{1}(0)$ onto the boundary of the image of the unit disk. Thus the image of the unit disk is either the upper half-plane or the lower half-plane. Checking $\phi(0)=i$ (a point in the upper half-plane), we conclude that $\phi$ maps the unit disk one-to-one onto the upper half-plane (see Figure 2).
(b) We can do this part in two ways. One way is to use Proposition 1(ii) and notice that $\psi$ is the inverse of $\phi$. Another way is to check the image by $\psi$ of the boundary and one interior point. We leave it as an exercise to verify that $\psi(0)=1, \psi(1)=i$, and $\psi(-1)=-i$. Since the images of the three points are not collinear, we conclude that the real axis is mapped onto the circle that goes through the points $1, i$, and $-i$, which is clearly the unit circle. (Here again, we are using the fact that three points determine a circle.) Also, $\psi(i)=0$; hence $\psi$ maps the upper half-plane onto the unit disk.

Another way to realize that the image of the unit circle is a line in Example $1(a)$ is to consider the point -1 on $C_{1}(0)$ and note that $\lim _{z \rightarrow-1} \phi(z)= \infty$. So the image of $C_{1}(0)$ is not bounded and since it is either a line or a circle, it has to be a line (which tends to infinity). Sometimes it is convenient to express the fact that the limit at the point $z_{0}=-\frac{d}{c}$ is infinity by writing $\phi\left(z_{0}\right)=\infty$. Likewise, it will be convenient to express $\lim _{z \rightarrow \infty} \frac{a z+b}{c z+d}=\frac{a}{c}$ by simply writing $\phi(\infty)=\frac{a}{c}$.

Before we present our next example, let us note another useful propert of linear fractional transformations.

ON 3

The composition of any two linear fractional transformations is again a line

N OF fractional transformation.

NGS

Proof Let $\phi_{1}(z)=\frac{a_{1} z+b_{1}}{c_{1} z+d_{1}}$ and $\phi_{2}(z)=\frac{a_{2} z+b_{2}}{c_{2} z+d_{2}}$. Then
$$
\phi(z)=\phi_{2} \circ \phi_{1}(z)=\frac{a_{2} \frac{a_{1} z+b_{1}}{c_{1} z+d_{1}}+b_{2}}{c_{2} \frac{a_{1} z+b_{1}}{c_{1} z+d_{1}}+d_{2}}
$$

Multiplying numerator and denominator by $c_{1} z+d_{1}$, we get
$$
\phi(z)=\frac{\left(a_{2} a_{1}+b_{2} c_{1}\right) z+a_{2} b_{1}+b_{2} d_{1}}{\left(c_{2} a_{1}+d_{2} c_{1}\right) z+d_{2} c_{1}+d_{2} d_{1}}
$$

---

<!-- Page 12 -->

Left margin note (page 12)

396
Chapter 6
C

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-12_500_1979_1176_89.jpg)

Figure 3 To map use the transform

Right margin note (page 12)

nd

with n of halfthe the ps $D$ tate $=-i$.
then
inear the and ary is ick
n we $r$ the From get

++++

onformal Mappings

which is a linear fractional transformation. Notice that when we multiplie $c_{1} z+d_{1}$, we removed the singularity at $z=-\frac{d_{1}}{c_{1}}$; the resulting composition has a single pole, and it is not necessarily at the same location as the poles or $\phi_{2}$.

EXAMPLE 2 Composition of linear fractional transformations
Find a linear fractional transformation that maps the disk $D$ with radius 2 center at -1 onto the right half-plane $\operatorname{Re} w>0$.
Solution We describe two methods for doing this problem. Let us start the quickest one based on the result of Example 1 and a simple applicatio Proposition 3. We know that $\phi(z)=i \frac{1-z}{1+z}$ maps the unit disk onto the upper plane. It is also easy to see that the linear mapping $\tau(z)=\frac{1}{2}(z+1)$ translate center of $D$ to the origin and then scales the radius by $\frac{1}{2}$. Thus $\tau$ maps $D$ ont unit disk. Consequently, $\phi \circ \tau(z)$ is a linear fractional transformation that ma onto the upper half-plane. To map onto the right half-plane, it suffices to rc the upper half-plane by $-\frac{\pi}{2}$. This can be achieved by multiplying by $e^{-i \frac{\pi}{2}}=$ So the desired linear fractional transformation (Figure 3) is
$$
f(z)=-i \phi \circ \tau(z)=(-i) i \frac{1-\frac{1}{2}(z+1)}{1+\frac{1}{2}(z+1)}=\frac{1-z}{3+z}
$$
a disk to a half-plane, it is always advantageous to map the given disk to the unit disk and ation $\phi$ in Example 1.

Another way to do this problem is to start from scratch; we want a 1 fractional transformation $g(z)=\frac{a z+b}{c z+d}$ to map the boundary of the disk ont boundary of the right half-plane. We can pick any three points on the circle $C$ map them to any three points on the imaginary axis. Since our image bounda a line (which extends to infinity), we may map one of our points to $\infty$. We p
$$
g(1)=0, \quad g(-3)=\infty, \quad g(i \sqrt{3})=i .
$$

We use these equations to solve for the coefficients $a, b, c$, and $d$, and the will check whether the interior of the disk is mapped to the right half-plane o left half-plane. Again writing $g(z)=\frac{a z+b}{c z+d}$, from $g(1)=0$ we get $a=-b$. $g(-3)=\infty$ we get $3 c=d$. Thus $g(z)=\frac{a z-a}{c z+3 c}=\frac{a}{c} \frac{z-1}{z+3}$. From $g(i \sqrt{3})=i$ we
$$
i=\frac{a}{c} \frac{i \sqrt{3}-1}{i \sqrt{3}+3} \Rightarrow \frac{a}{c}=i \frac{3+i \sqrt{3}}{-1+i \sqrt{3}}=\sqrt{3}
$$

---

<!-- Page 13 -->

Left margin note (page 13)

PROPOSITIO AN IMPLIC FORMU

PROPOSITION MAPPING A PON TO INFINI?

++++

Section 6.2 Linear Fractional Transformations
397

Then $g(z)=\sqrt{3} \frac{z-1}{z+3}$ will map the circle $C$ onto the $y$-axis. Note that any function of the form $\alpha g(z)$, where $\alpha \neq 0$ is real, will also map the circle $C$ onto the $y$ axis, since multiplying by a nonzero real constant leaves a line through the origin unchanged. So for simplicity we divide by $\sqrt{3}$, still calling the function $g$, and obtain a mapping $g(z)=\frac{z-1}{z+3}$ of the circle $C$ onto the $y$-axis. Does $g(z)$ take the region inside $C$ onto the right half-plane? We check the image of one point inside $C$, say -1 , and find $g(-1)=\frac{-2}{2}=-1$, which is a point in the left half-plane. So we modify $g$ by multiplying it by -1 and obtain the desired linear fractional transformation $g(z)=\frac{1-z}{3+z}$. Clearly any other positive multiple of $g$ will also work, and so the solution to this problem is not unique.

The previous examples illustrate how a linear fractional transformation can be determined from the images of three distinct points. In fact, we have the following useful formula.

N 4

There is a unique linear fractional transformation $w=\phi(z)$ that maps three

CIT distinct points $z_{1}, z_{2}$, and $z_{3}$ onto three distinct points $w_{1}, w_{2}$, and $w_{3}$. The

LA mapping $w$ is implicitly given by
$$
\frac{z-z_{1}}{z-z_{3}} \frac{z_{2}-z_{3}}{z_{2}-z_{1}}=\frac{w-w_{1}}{w-w_{3}} \frac{w_{2}-w_{3}}{w_{2}-w_{1}} .
$$

Proof That $w$ is a linear fractional transformation follows by solving for $w$ in (4). To see that $w$ maps $z_{j}$ to $w_{j}(\mathrm{j}=1,2,3)$ it suffices to note that (4) holds if we replace $z$ by $z_{j}$ and $w$ by $w_{j}$. (For $j=3$, you must take reciprocals in (4) before replacing $z$ by $z_{3}$ and $w$ by $w_{3}$.) The uniqueness part is done in Exercises 9-10.

To map a circle onto a line by a linear fractional transformation, as we saw in Example 2, this can be achieved by requiring that $f(z)=\infty$ for some $z$ on the circle. In this case, the formula in Proposition 4 can be simplified as follows. Say you want $f\left(z_{3}\right)=\infty$. As $w_{3} \rightarrow \infty$, the fraction $\frac{w_{2}-w_{3}}{w-w_{3}}=\frac{1-w_{2} / w_{3}}{1-w / w_{3}} \rightarrow 1$. This suggests that we set $\frac{w_{2}-w_{3}}{w-w_{3}}=1$ on the right side of (4), obtaining the following formula whose verification is left to Exercise 11.

N 5

Let $z_{1}, z_{2}$, and $z_{3}$ be three distinct points. There is a unique linear fractional

NT transformation $w=\phi(z)$ that maps $z_{1}$ and $z_{2}$ onto two distinct points $w_{1}$

ГY and $w_{2}$, and maps $z_{3}$ to $\infty$. The mapping $w$ is implicitly given by
$$
\frac{z-z_{1}}{z-z_{3}} \frac{z_{2}-z_{3}}{z_{2}-z_{1}}=\frac{w-w_{1}}{w_{2}-w_{1}}
$$

There is also a corresponding identity for a linear fractional transformation mapping $\infty$ to a point, obtained by reversing the roles of $z$ and $w$ in (5) (see Exercise 11). Our next example uses the conformal property of linear fractional transformations.

---

<!-- Page 14 -->

Left margin note (page 14)

398
Chapter 6

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-14_493_525_183_115.jpg)

Figure 4 A len gion.

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-14_485_547_1717_113.jpg)

Figure 5 Two circles $C_{1}$ and $C$

Right margin note (page 14)

v-plane

2, and
their
tween
of $C_{1}$
action
maps
ne this
) $=i$.
serves
jual to
"
apac-
unded
prob-
to an
here is
before
ple to
rcises.
isks in
oduced
hus $\phi_{a}$
undary
maps
ill map
e image

++++

Conformal Mappings
EXAMPLE 3 Mapping of a lens-shaped region
The lens-shaped region $\Omega$ in Figure 4 is bounded by the arcs of two circles.
(a) Use a linear fractional transformation $\phi$ to map $\Omega$ onto a sector in the $u$ in such a way that
s-shaped re-
$$
\phi(-2)=0, \quad \phi(-i)=1, \quad \phi(2)=\infty .
$$
(b) Determine the angle between the circles at the point -2 .

Solution (a) We apply (5) with $z_{1}=-2, w_{1}=0, z_{2}=-i, w_{2}=1, z_{3}=$ get
$$
\frac{z+2}{z-2} \frac{-i-2}{-i+2}=\frac{w}{1} \Rightarrow w=\phi(z)=\frac{2+i}{2-i} \frac{2+z}{2-z} .
$$
(b) Of course we can determine the angle between $C_{1}$ and $C_{2}$ by finding equations, then the slopes of the tangent lines at -2 , and then the angle be the tangent lines. A better way is to calculate the angle between the images and $C_{2}$ and use the conformal property of $\phi$.

Because $\phi$ takes lines and circles to lines and circles, it is clear from its on the points $-2,-i$ and 2 that $\phi$ maps the circle $C_{1}$ onto the $u$-axis. It also the circle $C_{2}$ onto a line that goes through the point $\phi(-2)=0$. To determin line, it suffices to check the image of another point on $C_{2}$. We have $\phi\left(\frac{2}{3} i\right.$ Thus $\phi$ maps $C_{2}$ onto the $v$-axis. Because $\phi$ is conformal at $z=-2$, it pre the angles at this point. Thus, the angle between the circles at $z=-2$ is eq the angle between their images, the $u$ - and $v$-axes, which is clearly $\frac{\pi}{2}$.

Some applications concerning the electrostatic potential inside a itor formed by two cylinders lead to Dirichlet problems in regions bo by two circles in the plane, which are not necessarily concentric. The lems are easier to solve when the two circles are concentric, giving rise annular region. (See for examples the exercises of Section 2.5.) Thus t] a great advantage in using a conformal mapping to center the circles solving the Dirichlet problem. In what follows, we use a specific exam illustrate this process. More general examples are presented in the exe

Example 4 Centering disks
Find a one-to-one analytic mapping that maps the region between the Figure 5 to an annular region bounded by two concentric circles.
Solution The idea is to use one of the linear fractional transformations
$$
\phi_{\alpha}(z)=\frac{z-\alpha}{1-\bar{\alpha} z}
$$
where $\alpha$ is a complex number such that $|\alpha|<1$. These functions were intr in Example 3, Section 3.7, where it was shown that $\left|\phi_{\alpha}(z)\right|=1$ if $|z|=1$. T maps the unit circle onto the unit circle. Because $\phi_{\alpha}$ maps boundary to bo and because $\phi_{\alpha}(0)=-\alpha$ (a point inside the unit disk), we conclude that $\phi$. the unit disk onto itself. Since $\phi_{\alpha}$ is a linear fractional transformation, it w the circle $C_{1}$ onto a circle or a line, but because the image has to be inside th

---

<!-- Page 15 -->

Left margin note (page 15)

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-15_401_878_679_715.jpg)

Figure 6 For all $|\alpha|< o_{\mathrm{a}}(z)$ maps the unit circle onto itself. But for one s cial value of $\alpha$, with $|\alpha|< \phi_{a}$ will also map the circle onto a circle centered at origin, thus centering the ages of $C_{1}$ and $C_{2}$.

++++

Section 6.2 Linear Fractional Transformations
399

of the unit disk, it follows that $\phi\left[C_{1}\right]$ is bounded and hence it must be a circle. We now ask the following question: Can we find $\alpha$ so that $\phi_{\alpha}\left[C_{1}\right]$ is a circle centered at the origin? Suppose for a moment that $\alpha$ were real. Then clearly $\phi_{\alpha}(x)$ is also real, and so $\phi_{\alpha}$ maps the real line to the real line. Note that $\phi_{\alpha}(1 / 7)$ and $\phi_{\alpha}(1 / 2)$ are the points where $\phi_{\alpha}\left[C_{1}\right]$ meets the $u$-axis. Also, the circle $\phi_{\alpha}\left[C_{1}\right]$ must meet the $u$-axis in a perpendicular fashion (Figure 6), for the following three reasons:
(i) $C_{1}$ itself meets the real axis in a perpendicular fashion;
(ii) the $x$-axis is mapped to the $u$-axis; and
(iii) the map $\phi_{\alpha}$ is conformal.

1,
$C_{2}$
pe-
1,
$C_{1}$
the
im-

So if we want $\phi_{\alpha}\left[C_{1}\right]$ to be a circle centered at the origin, it is enough to require that $\phi_{\alpha}(1 / 7)=-\phi_{\alpha}(1 / 2)$. This implies that
$$
\frac{\frac{1}{7}-\alpha}{-\frac{\alpha}{7}+1}=-\frac{\frac{1}{2}-\alpha}{-\frac{\alpha}{2}+1} \Rightarrow \frac{1-7 \alpha}{7-\alpha}=-\frac{1-2 \alpha}{2-\alpha} \Rightarrow 9 \alpha^{2}-30 \alpha+9=0
$$

The last equation in $\alpha$ is equivalent to $3 \alpha^{2}-10 \alpha+3=0$, with solutions
$$
\alpha=\frac{5 \pm \sqrt{16}}{3}=\frac{5 \pm 4}{3} \Rightarrow \alpha=3 \text { or } \alpha=\frac{1}{3} .
$$

Since we want $|\alpha|<1$, we take $\alpha=\frac{1}{3}$. Thus
$$
\phi(z)=\phi_{\frac{1}{3}}(z)=\frac{z-\frac{1}{3}}{-\frac{1}{3} z+1}=\frac{3 z-1}{3-z}
$$
will map $C_{2}$ onto $C_{2}$ and $C_{1}$ onto the circle with center at the origin and radius $r=|\phi(1 / 2)|=\frac{\frac{3}{2}-1}{3-\frac{1}{2}}=\frac{1}{5}$.

Composing Elementary Mappings
As the title indicates, we will compose together elementary mappings that we have studied thus far and construct some nontrivial conformal mappings of regions in the plane. We give four examples to illustrate this important process.

---

<!-- Page 16 -->

Left margin note (page 16)

400
Chapter 6

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-16_515_1929_1105_109.jpg)

Figure 7 Mappi which preserved where the angle

Right margin note (page 16)

region of oing that
ped onto no longer ormation nit disk. rest. So trated in
$w$-plane
point -2, e point 0 ,
onto the
erms of $z$
is-shaped
s:

++++

Conformal Mappings

EXAMPLE 5 Mapping a lens onto a disk
Construct a sequence of analytic functions that maps the lens-shaped Example 3 in a one-to-one way onto the unit disk. Write down the mapt results from your construction.
Solution The first step is to use the function of Example 3,
$$
w_{1}=\phi(z)=\frac{2+i}{2-i} \frac{2+z}{2-z}=\alpha \frac{2+z}{2-z} \quad\left(\alpha=\frac{2+i}{2-i}\right),
$$
which maps the lens to the first quadrant. The first quadrant is then map the upper half-plane by the function $w_{2}=w_{1}^{2}$. (Note that our mapping is a linear fractional transformation.) Finally, the linear fractional transf $w=\psi\left(w_{2}\right)$ in Example 1(ii) will take the upper half-plane onto the Each of these mappings is analytic and one-to-one on the region of inte the resulting function is analytic and one-to-one. The mapping is illus Figure 7.
ng a lens onto the unit disk. Note the conformal property in the first mapping at the the right angle. Note the failure of the conformal property in the second mapping at th is doubled.

The explicit formula in terms of $z$ of the conformal mapping of the lens unit disk is
$$
w=\frac{i-w_{2}}{i+w_{2}}=\frac{i-w_{1}^{2}}{i+w_{1}^{2}}=\frac{i-[\phi(z)]^{2}}{i+[\phi(z)]^{2}}
$$
where $\phi(z)=\frac{2+i}{2-i} \frac{2+z}{2-z}$ from Example 3. Replacing $\phi(z)$ by its value in t and simplifying (by hand or with the help of a computer system), we get
$$
w=f(z)=-i \frac{4-28 i z+z^{2}}{28+4 i z+7 z^{2}}
$$

The following values of $w$ confirm the fact that the mapping takes the le region onto the unit disk, also taking boundary points to boundary point
$$
f(0)=-\frac{i}{7}, \quad f(-2)=1, \quad f\left(\frac{2}{3} i\right)=-i, \quad f(-i)=i
$$

---

<!-- Page 17 -->

Left margin note (page 17)

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-17_452_1815_282_57.jpg)

Figure 8 Mapping the $u$

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-17_441_1817_1599_37.jpg)

Figure 9 Mapping a cresc

++++

Section 6.2 Linear Fractional Transformations
401

EXAMPLE 6 Mapping a half-disk onto a disk
The sequence of one-to-one analytic mappings in Figure 8 takes the upper half of the unit disk onto the unit disk.
pper half of the unit disk onto the unit disk.
The first mapping is the linear fractional transformation $w_{1}=\phi(z)=i \frac{1-z}{1+z}$ from Example 1. It takes the unit disk onto the upper half-plane. It also takes the upper half-disk onto the first quadrant, as can be verified by using the conformality at $z=1$ and checking the image of one interior point, say $\phi\left(\frac{i}{2}\right)=\frac{4}{5}+i \frac{3}{5}$, which is in the first quadrant. The action of the second mapping is clear. The third mapping is the mapping $\psi$ from Example 1(ii). The explicit formula of the final mapping $w=f(z)$ is
$$
w=\psi\left(w_{2}\right)=\frac{i-w_{2}}{i+w_{2}}=\frac{i-w_{1}^{2}}{i+w_{1}^{2}}=\frac{i-\left(i \frac{1-z}{1+z}\right)^{2}}{i+\left(i \frac{1-z}{1+z}\right)^{2}}=-i \frac{1+2 i z+z^{2}}{1-2 i z+z^{2}}
$$

The intermediary mapping $w_{2}=w_{1}^{2}=-\left(\frac{1-z}{1+z}\right)^{2}$ is also of interest. It takes the upper half-disk onto the upper half-plane.

EXAMPLE 7 A crescent-shaped region onto the upper half-plane The crescent-shaped region in Figure 9 is bounded by two circles that intersect at angle 0 at the origin. We will describe a sequence of one-to-one analytic mappings that takes this region onto the upper half-plane.
ent onto the upper half-plane.
The first mapping $w_{1}=-\frac{1}{z}$, being conformal at $z=i$ and $z=2 i$, will preserve the right angles at these points. Since it maps the imaginary axis onto the imaginary

---

<!-- Page 18 -->

Left margin note (page 18)

402
Chapter 6

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-18_482_1259_908_775.jpg)

Figure 10 Th branch of the $\log z$, maps half-plane onto horizontal strip.

Right margin note (page 18)

that
varallel
nd the
apping
set us
"

trip e unit ation, ration $e$, and ip the

$i \frac{\pi}{2}$

rithm. which lesired
$d$ three he line of the y lines

++++

Conformal Mappings
axis, and 0 to $\infty$, consequently it will map the two circles onto two line intersect the imaginary axis at right angle. Thus the images of the circles are p horizontal lines as shown in the figure. As we move counterclockwise arou circles in the $z$-plane, we move right ward on the lines in the $w_{1}$-plane. The ma $w_{2}=2 \pi\left(w_{1}-\frac{1}{2}\right)$ translates then scales the horizontal strip appropriately to up for an exponential mapping to the upper half-plane.

EXAMPLE 8 Mapping the unit disk onto an infinite horizontal s We will describe a sequence of analytic and one-to-one mappings that takes th circle onto an infinite horizontal strip. The first linear fractional transform $w_{1}=-i \phi(z)$, is obtained by multiplying by $-i$ the linear fractional transform $\phi(z)$ in Example 1(i). Since $\phi(z)$ maps the unit disk onto the upper half-plan multiplication by $-i$ rotates by the angle $-\frac{\pi}{2}$, the effect of $-i \phi(z)$ is to ma unit disk onto the right half-plane.
e principal logarithm, the right an infinite

In Figure 10, $\log w_{1}=\ln \left|w_{1}\right|+i \operatorname{Arg} w_{1}$ is the principal branch of the loga As $w_{1}$ varies in the right half-plane, $\operatorname{Arg} w_{1}$ varies between $-\frac{\pi}{2}$ and $\frac{\pi}{2}$, explains the location of the horizontal boundary of the infinite strip. The mapping is
$$
w=f(z)=\log (-i \phi(z))=\log \frac{1-z}{1+z}
$$

Exercises 6.2
In Exercises 1-4, you are given a linear fractional transformation $\phi(z)$ an points $z_{1}, z_{2}$, and $z_{3}$. Let $L_{1}$ denote the line through $z_{1}$ and $z_{2}$ and $L_{2} t$ through $z_{2}$ and $z_{3}$. In each case, (a) compute the images $w_{1}, w_{2}$, and $w_{3}$ points $z_{1}, z_{2}$, and $z_{3}$. (b) Describe the images by $\phi$ of $L_{1}$ and $L_{2}$. Are the or circles? (You will need the images of three points on each line.)
1. $\phi(z)=i \frac{1-z}{1+z}, z_{1}=1, z_{2}=0, z_{3}=i$.
2. $\phi(z)=\frac{i+z}{i-z}, z_{1}=1+i, z_{2}=0, z_{3}=i$.
3. $\phi(z)=\frac{1+i-2 z}{i-i z}, z_{1}=i, z_{2}=1, z_{3}=-i$.
4. $\phi(z)=\frac{1+2 z}{i-(1+i) z}, z_{1}=1+i, z_{2}=1, z_{3}=1-i$.

---

<!-- Page 19 -->

Left margin note (page 19)

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-19_473_491_533_53.jpg)

Figure 11 For Exercis

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-19_497_1972_1836_31.jpg)

Figure 12 for Exercise 12

++++

Section 6.2 Linear Fractional Transformations
5. Find the inverse $\psi$ of the linear fractional transformation in Exercise 1, verify that $\psi$ maps $w_{1}, w_{2}$, and $w_{3}$ to $z_{1}, z_{2}$, and $z_{3}$.
6. Repeat Exercise 5 with the linear fractional transformation of Exercise 2.
7. (a) What is the inverse of the function $f(z)=\frac{1}{z}$ ? Answer this question with using (2), then verify your answer using (2).
(b) Describe the images by $f(z)=\frac{1}{z}$ of the unit circle, the unit disk, and the req outside the unit circle.
8. Let $\alpha$ denote the angle between the two circles in Figure 11 at -2 . Show $\tan \alpha=\frac{4(a+1)(a-4)}{3(a+6)\left(a-\frac{2}{3}\right)}$. Discuss the cases when $a=-1,4,-6$, and $\frac{2}{3}$. [Hint: N the circles to lines using the linear fractional transformation in Example 3.]
9. Fixed points. Recall that a point $z_{0}$ is a fixed point of a function $f(z f\left(z_{0}\right)=z_{0}$. Show that a linear fractional transformation $\phi(z)$ can have at m two fixed points in the complex plane, unless $\phi(z)=z$, in which case all points fixed points. [Hint: Discuss all possible solutions of $z=\frac{a z+b}{c z+d}$.]
10. Uniqueness of a linear fractional transformation. Let $z_{1}, z_{2}$, and be three distinct points, and let $w_{1}, w_{2}$, and $w_{3}$ be three distinct points (we all

8. $\infty$ ). Show that there is a unique linear fractional transformation mapping $z_{j}$ to [Hint: The existence is guaranteed by Propositions 4 and 5. To prove uniquene suppose that $f$ and $g$ are two linear fractional transformations mapping $z_{j}$ to 2 Apply the result of Exercise 9 to $f \circ g^{-1}$. How many fixed points does $f \circ g^{-1}$ hav
11. (a) Mapping a point to infinity. Prove Proposition 5.
(b) Mapping infinity to a point. Let $z_{1}$ and $z_{2}$ be two distinct points, a $w_{1}, w_{2}, w_{3}$ be three distinct points. Show that there is a unique linear fractior transformation $w=\phi(z)$ that maps $z_{1}$ to $w_{1}, z_{2}$ to $w_{2}$ and $\infty$ to $w_{3}$. The mappi $w$ is implicitly given by
$$
\frac{z-z_{1}}{z_{2}-z_{1}}=\frac{w-w_{1}}{w-w_{3}} \frac{w_{2}-w_{3}}{w_{2}-w_{1}} .
$$

In Exercises 12-24, (a) supply the formulas of the analytic mappings in each quence of mappings shown in the accompanying figure (Figures 12-24). (b) Ver that the boundary and the interior of the shaded regions are mapped to the boun ary and interior of the shaded regions. (c) Derive the given formula for the fir composite mapping $w=f(z)$. As usual, we start in the $z$-plane and end in $t w$-plane, going through the $w_{j}$-planes.

---

<!-- Page 20 -->

Left margin note (page 20)

404
Chapter 6

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-20_511_1993_335_90.jpg)

Figure 13 for Exe

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-20_509_1991_1051_94.jpg)

Figure 14 for Ex

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-20_521_1988_1757_102.jpg)

Figure 15 for E:

Right margin note (page 20)

ane
$=\infty$

⟶
lane
0)
ane
$\sqrt{3}_{3}(0)$

++++

Conformal Mappings
ercise 14.
xercise 15.

---

<!-- Page 21 -->

Left margin note (page 21)

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-21_468_1339_129_235.jpg)

Figure 16 for Exercise 16.

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-21_453_1329_808_233.jpg)

Figure 17 for Exercise 17.

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-21_459_1812_1489_14.jpg)

Figure 18 for Exercise 18.

++++

Section 6.2 Linear Fractional Transformations
405

---

<!-- Page 22 -->

Left margin note (page 22)

406
Chapter 6
C
$z-$
-2
![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-22_533_1448_345_349.jpg)

Figure 19 for Exe
$z$

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-22_510_1415_1082_380.jpg)

Figure 20 for Ex

2
![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-22_500_1394_1790_401.jpg)

Figure 21 for E

++++

onformal Mappings
rcise 19.
ercise 20.
xercise 21.

---

<!-- Page 23 -->

Left margin note (page 23)

$z$-pla
-1

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-23_502_1402_373_323.jpg)

Figure 22 for Exerci
$$
z \text {-pla }
$$

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-23_463_1386_1084_339.jpg)

Figure 23 for Exerci

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-23_495_1901_1748_50.jpg)

Figure 24 for Exercis

++++

Section 6.2 Linear Fractional Transformations
4
se 22.
se 23.
24.

---

<!-- Page 24 -->

Left margin note (page 24)

408
Chapter 6

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-24_506_496_391_104.jpg)

Figure 25 for E

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-24_480_1073_2010_876.jpg)

Figure 26 fo
Take $a=-\frac{1}{4} a$

Right margin note (page 24)

Examh that g , and where rcepts $\phi_{\alpha}(z)$ tional uffices
1.
$-b)$.]
follows oots of

2 onto region circle.
shaded nto an Refer to the

++++

Conformal Mappings
25. Project Problem: Centering disks. We generalize the process in ple 4 to any region bounded by two non-intersecting circles, $C_{2}$ and $C_{1}$, suc $C_{1}$ is in the interior of $C_{2}$. By translating the center of $C_{1}$ to the origin, scalin rotating, we can always reduce the picture to the one described in Figure 25, $|a|<b<1, C_{2}$ is the unit circle, and $C_{1}$ is centered on the $x$-axis with $x$-inte $a$ and $b$. Our goal is to show that we can choose $\alpha$ such that $-1<\alpha<1$ and maps $C_{1}$ onto a circle centered at the origin. Here $\phi_{\alpha}(z)$ is the linear frac transformation (6), which maps $C_{2}$ onto $C_{2}$. As explained in Example 4, it s to choose $\alpha$ so that $\phi_{\alpha}(a)=-\phi_{\alpha}(b)$.
(a) Show that the latter condition leads to the equation in $\alpha$ :
$$
\alpha^{2}-2 \frac{1+a b}{a+b} \alpha+1=0,
$$
with roots
$$
\alpha_{1}=\frac{1+a b}{a+b}+\sqrt{\left(\frac{1+a b}{a+b}\right)^{2}-1} \quad \text { and } \quad \alpha_{2}=\frac{1+a b}{a+b}-\sqrt{\left(\frac{1+a b}{a+b}\right)^{2}}-
$$
(b) Show that if $|a|<1$ and $|b|<1$, then $1+a b \geq a+b$. [Hint: $1-b \geq a$ (1
(c) Show that $\alpha_{1}>1$, while $0<\alpha_{2}<1$. [Hint: The first inequality from (b). For the second inequality, use the fact that the product of the $\mathbf{r} a x^{2}+b x+c=0$ is $\frac{c}{a}$.]
(d) Conclude that $\phi(z)=\frac{z-\alpha}{1-\alpha z}$ with $\alpha=\frac{1+a b}{a+b}-\sqrt{\left(\frac{1+a b}{a+b}\right)^{2}-1}$ will map $C$
$C_{2}, C_{1}$ onto a circle centered at the origin with radius $r=\phi(b)$, and the between $C_{2}$ and $C_{1}$ onto the annular region bounded by $\phi\left[C_{1}\right]$ and the unit
In Exercises 26-29, derive the linear fractional transformation that maps the region between the two given circles (or circle and line in Exercise 29) o annular region centered at the origin (see the accompanying Figures 26-29) to Exercise 25 for instructions. In Exercises 28-29, you need to reduce situation described in Exercise 25.

Exercise 26.
nd $b=\frac{7}{8}$.

---

<!-- Page 25 -->

Left margin note (page 25)

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-25_504_1131_196_740.jpg)

Figure 27 for Exerc Take $a=0$ and $b=\frac{8}{17}$

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-25_492_1961_722_64.jpg)

Figure 28 for Exercise

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-25_488_1959_1263_56.jpg)

Figure 29 for Exercise then scale the outer rad

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-25_433_407_1924_56.jpg)

Right margin note (page 25)

gog
$A$
9
$\% 0 \%$, 90

++++

Section 6.2 Linear Fractional Transformations

ise 27 .
28. (The figures are not to scale.)
29. [Hint: In the last step, start by rotating the inner circle to center it on the real ax ius to 1 .]
30. A geometric problem. The following is an interesting illustration of th use of linear fractional transformations to prove geometric facts. Consider a circle and a point $z_{0}$ inside $C$ (Figure 30). We will show that all the circles $C^{\prime}$ through that intersect $C$ at right angle, also intersect at a common point $z_{1}$ as in Figure 3 The point $z_{1}$ is called the reflection of $z_{0}$ in $C$. We also say that $z_{0}$ and $z_{1}$ a symmetric with respect to $C$.
(a) There exists a linear fractional transformation $\phi$ that maps $C$ to the real ax and the interior of $C$ to the upper half-plane. Show that $\phi\left[C^{\prime}\right]$ is a circle or a lir that intersects the real axis at a right angle.
(b) Conclude that $\phi\left[C^{\prime}\right]$ passes through the point $-\phi\left(z_{0}\right)$. Setting $z_{1}=\phi^{-1}\left(-\phi\left(z_{0}\right.\right.$ we see that $C$ passes through $z_{1}$.

---

<!-- Page 26 -->

Left margin note (page 26)

410
Chapter 6
Co

Right margin note (page 26)

onto onto hese t is, here arz's
0) $\circ g$ can will
hout also nma and pply
ings $\phi_{\alpha}$ the ange
lane the
ation
tions $S T$
cises and
an be

can

++++

nformal Mappings
31. Project problem: one-to-one analytic mappings of the unit disk itself. Let $\phi_{\alpha}(z)$ be as in (6). We know that $\phi_{\alpha}(z)$ maps the unit disk $D$ itself. In this exercise, we show that, up to a unimodular constant multiple, are the only one-to-one analytic mappings of the unit disk onto itself. Tha if $f$ is a one-to-one analytic mapping of $D$ onto $D$, then $f(z)=c \phi_{\alpha}(z)$, w $|c|=1$. This important result will be obtained as a consequence of Schw lemma (Section 3.7).
(a) Suppose that $g$ is a one-to-one mapping of $D$ onto itself. Show that $f=\phi_{g}$ is a one-to-one analytic mapping of $D$ onto itself such that $f(0)=0$. If we show that $f$ is of the desired form, then because $g=\phi_{g(0)}^{-1} \circ f=\phi_{-g(0)} \circ f$, it follow that $g$ is of the desired form.
(b) Suppose that $g$ is a one-to-one mapping of $D$ onto itself. By (a), we may witl loss of generality assume that $g(0)=0$. Show that the inverse of $g, g^{-1}$, is analytic, one-to-one, and maps $D$ onto $D$ and $g^{-1}(0)=0$. Apply Schwarz's len to $g$ and obtain $|g(z)| \leq|z|$. Apply Schwarz's lemma to $g^{-1}$ at the point $g(z)$ obtain $\left|g^{-1}(g(z))\right| \leq|g(z)|$, or, equivalently, $|z| \leq|g(z)|$. Hence $|g(z)|=|z|$. A Schwarz's lemma again and conclude that $g(z)=c z$, where $|c|=1$.
32. Suppose that $\Omega$ is a region and $f$ and $g$ are two analytic one-to-one mapp of $\Omega$ onto the unit disk $D$. Show that there is a linear fractional transformation of the form (6) such that $f(z)=c \phi_{\alpha} \circ g(z)$, where $|c|=1$. This shows that all one-to-one mappings of a region $\Omega$ onto the unit disk are the same up to a cha of variables effectuated by a linear fractional transformation of the form (6).
33. (a) Characterize all the one-to-one analytic mappings of the upper half-p onto the unit disk. (b) Characterize all the one-to-one analytic mappings of upper half-plane onto itself.
34. Matrix correspondence. (a) Prove Proposition 3.
(b) We define a mapping $\Phi$ that associates to each linear fractional transforma
(1) the $2 \times 2$ matrix with complex entries
$$
S=\left(\begin{array}{ll}
a & b \\
c & d
\end{array}\right) .
$$

Thus $\Phi(\phi)=S$. Suppose that $\phi$ and $\psi$ are two linear fractional transforma with matrices $\Phi(\phi)=S$ and $\Phi(\psi)=T$. Show that the $\Phi(\phi \circ \psi)=S T$, wher denotes the product of the two matrices $S$ and $T$.
Project Problem: Lines and circles under inversion, part I. In Exer 35-37 we will show that the function $f(z)=\frac{1}{2}$ maps lines and circles to lines circles.
35. (a) Show that with $w=u+i v$ and $z=x+i y$, the mapping $w=1 / z$ written as $u(x, y)=\frac{x}{x^{2}+y^{2}}, v(x, y)=-\frac{y}{x^{2}+y^{2}}$.
(b) Deduce that the inverse transformation $z=1 / w$ is given by
$$
x(u, v)=\frac{u}{u^{2}+v^{2}}, \quad y(u, v)=-\frac{v}{u^{2}+v^{2}}
$$
36. (a) Show that any circle of the form $\left(x-x_{0}\right)^{2}+\left(y-y_{0}\right)^{2}=r^{2}, r>$ be written in the form
$$
A\left(x^{2}+y^{2}\right)+B x+C y+D=0, \text { where } B^{2}+C^{2}-4 A D>0 .
$$

---

<!-- Page 27 -->

Left margin note (page 27)

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-27_418_417_317_98.jpg)

Figure 31 For Exerc Note that $S$ and $f[S]$ a ted in the same plane.

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-27_478_484_994_64.jpg)

Figure 32 For Exerc Note that $S$ and $f[S]$ an ted in the same plane.

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-27_489_477_1662_57.jpg)

Figure 33 For Exerci Note that $S$ and $f[S]$ are ted in the same plane.

Right margin note (page 27)

411
with
or
0.

and (9), ing n of xerthe xer-
how uli, rened the the the nes
the the hat igh
ine aps ach $R$ to
ify nain nal

++++

Section 6.2 Linear Fractional Transformations
(b) Show that any line in the plane can be written in the form (9).
(c) Show that any set of points satisfying $A\left(x^{2}+y^{2}\right)+B x+C y+D=0 B^{2}+C^{2}-4 A D>0$ is either a circle or a line depending on whether $A=$
$)_{\vec{x}}^{z_{2}}$
ise 38.
re plot-
) $=\frac{1}{z}$
S]
ise 39 .
e plot-

se 40.
plot-
$A \neq 0$.
(d) Show that such circles or lines pass through the origin if and only if $D=$
37. Suppose a set $S$ is given as those points ( $x, y$ ) satisfying (9). Use (8) conclude that points $(u, v)$ in $f[S]$ satisfy an equation of the same form as including the associated constant inequality. Conclude that under the mapt $f(z)=1 / z$ lines and circles are mapped to lines and circles, with the exceptio the origin.
Project Problem: Lines and circles under inversion, part II. In E cises $38-41$, we investigate how specific lines and circles are mapped under function $f(z)=\frac{1}{z}$ and describe a quick method to obtain the images. These $e$ cises depend on Exercises 35-47, and in particular, (8) and (9).
38. (a) Suppose that $S$ is a circle that does not pass through the origin. that $f[S]$ is also a circle that does not pass through the origin.
(b) Let $z_{1}$ and $z_{2}$ denote the points in $S$ with the smallest and largest mod respectively. Show that $f\left(z_{1}\right)$ and $f\left(z_{2}\right)$ have the largest and smallest moduli, spectively, of those points in $f[S]$. Argue that the circle $f[S]$ is uniquely determi by these two points $f\left(z_{1}\right)$ and $f\left(z_{2}\right)$ (see Figure 31; $S$ and $f[S]$ are plotted on same plane).
39. (a) Suppose $S$ is a line that passes through the origin. Show that with exception of mapping to and from the origin, $f[S]$ is also a line passing through origin.
(b) Argue that the image $f\left(z_{0}\right)$ of any nonzero point $z_{0}$ in $S$ uniquely determi the line $f[S]$ (see Figure 32).
40. (a) Suppose $S$ is a circle that passes through the origin. Show that with exception of mapping from the origin, $f[S]$ is a line that does not pass through origin.
(b) Suppose that $S$ is a line which does not pass through the origin. Show t] with the exception of mapping to the origin, $f[S]$ is a circle that passes throu the origin.
(c) Let $S$ be a circle that passes through the origin and $f[S]$ be the associated 1 that does not. Show that the point $z_{0}$ of maximum modulus on the circle m: to the point $w_{0}$ of minimum modulus on the line, and vice versa. Argue that e of these points uniquely determines the corresponding circle or line. If we let denote the radius of the circle and $a$ the perpendicular distance from the origin the line, show that $2 R=\frac{1}{a}$ (see Figure 33).
41. Lines and circles under linear fractional transformations. (a) that every linear fractional transformation is a composition of a linear transfor tion, followed by an inversion, followed by a linear transformation, as described the section.
(b) Using part (a) and the result of Exercise 37, show that any linear fractio transformation maps lines and circles to lines and circles.

---

<!-- Page 28 -->

Left margin note (page 28)

412
Chapter 6
6.3
Solvin

Right margin note (page 28)

2.5, of the Thepblem Conh the g, the lace's iccess ecific on inon of
stant We angle sative nding cuts.
real O , for with hould This lps us ved a
is kept and $0^{\circ}$ inside
k with semieffect onding nsform ctional verify r semiroblem

++++

Conformal Mappings

Dirichlet Problems with Conformal Mappings
This section continues the applications that we introduced in Sectio using conformal mappings to solve Dirichlet problems. At the heart subject is the invariance of Laplace's equation by conformal mappings, orem 3, Section 2.5. Very often the difficulty in solving a Dirichlet pro is due to the geometry of the region on which the problem is stated. formal mappings can be used to transform a region to one on whic ensuing boundary value problem is easier to solve. Roughly speakin conformal mapping method is like a change of variables that leaves Lap equation unchanged but transforms the boundary conditions. The su of this method is phenomenal. Not only we will be able to solve sp problems, but we will also take general formulas, such as the Poisso tegral formula on a disk, and produce similar formulas for the soluti Dirichlet problems on new regions in the plane.

Recall that for Dirichlet problems where the boundary data is con along rays, we can find a solution using a branch of the argument. denote by $\arg _{\alpha} z$ the branch of the argument with a branch cut at $\alpha$, and by $\operatorname{Arg} z$ the principal branch with a branch cut along the neg real axis. These functions, being the imaginary parts of the correspo logarithm branches, are harmonic everywhere except on their branch

Recall also that a linear combination of harmonic functions witl scalars is again a harmonic function (Proposition 1, Section 2.5). S example, $u(z)=\frac{100}{\pi}(\pi-\operatorname{Arg} z)$ is harmonic in the upper half-plane boundary values $u(x)=100$ if $x>0$ and $u(x)=0$ if $x<0$. (You s review Example 3, Section 2.5, for useful details involving $\operatorname{Arg} z$.) solution to a very simple Dirichlet problem in the upper half-plane he solve a somewhat difficult Dirichlet problem on the unit disk. (We sol similar problem using Fourier series in Section 4.7.)

EXAMPLE 1 Steady-state temperature distribution in a disk
The boundary of a circular plate of unit radius with insulated lateral surface at a fixed temperature distribution equal to $100^{\circ}$ on the upper semi-circle on the lower semi-circle (see Figure 1(a)). Find the steady-state temperature the plate.
Solution To answer this question, we must solve $\Delta u=0$ inside the unit dis boundary values $u=100$ on the upper semi-circle and $u=0$ on the lower circle. While the geometry of the circle makes it difficult to understand the of the boundary conditions on the solution inside the unit disk, the correspe boundary value problem in the upper half-plane has a simple solution. To trat the given problem into a problem in the upper half-plane, we use the linear fra transformation $\phi(z)=i \frac{1-z}{1+z}$ from Example 1(ii), Section 6.2. It is easy to that $\phi(z)$ takes the upper semi-circle onto the positive real axis, and the lowe circle onto the negative real axis. Thus $\phi$ transforms the given Dirichlet p

---

<!-- Page 29 -->

Left margin note (page 29)

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-29_442_487_254_645.jpg)
![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-29_448_494_248_1330.jpg)
![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-29_450_493_1790_617.jpg)
![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-29_452_495_1788_1311.jpg)

Figures 1 (a) and (b) Transforming the Diri problem in Figure 1(a) an easier Dirichlet proble Figure 1(b), by using a li fractional transformation
$$
\phi(z)=i \frac{1-z}{1+z} .
$$

Figures 2(a) and (b) Us a linear fractional transfor tion to transform a Diri let problem in a lens (F ure 2(a)) into a Dirichlet pr lem in the first quadrant (F ure 2(b)). While the probl in the lens is difficult to sol the problem in the first qu tant has a very simple solut $U(w)=\frac{200}{\pi} \operatorname{Arg} w$.

++++

Section 6.3 Solving Dirichlet Problems with Conformal Mappings
413

into a Dirichlet problem in the upper half-plane with boundary values shown in Figure 1(b).

chlet
into
m in
near

According to our preceding discussion, the solution in the upper half of the $w$ plane is $U(w)=\frac{100}{\pi}(\pi-\operatorname{Arg} w)$. By composing the solution in the $w$-plane with the conformal map, we get a solution of our original problem, $u(z)=U(\phi(z))$. Hence the solution of the Dirichlet problem in the unit disk is
$$
u(z)=\frac{100}{\pi}(\pi-\operatorname{Arg} \phi(z))=\frac{100}{\pi}\left(\pi-\operatorname{Arg}\left(i \frac{1-z}{1+z}\right)\right)
$$

For example, the temperature of the center of the circular plate is $u(0)=\frac{100}{\pi}(\pi- \operatorname{Arg}(i))=\frac{100}{\pi} \frac{\pi}{2}=50$, which is, as you would expect, the average value of the temperature on the circumference. With a little extra work, we can express the solution $u(z)$ in terms of $x$ and $y$ instead of $z$ (see Exercise 18).

We next solve a Dirichlet problem in a lens-shaped region.

EXAMPLE 2 Dirichlet problem in a lens-shaped region
Find a harmonic function $u$ in the lens-shaped region $\Omega$ in Figure 2(a), with boundary values $u=100$ on the upper circular arc and $u=0$ on the lower circular arc.
Solution The region $\Omega$ was discussed in Example 3, Section 6.2, from which we recall the linear fractional transformation $\phi(z)=\frac{2+i}{2-i} \frac{2+z}{2-z}$. It is straightforward to check that $\phi$ maps the lower boundary of $\Omega$ onto the positive real axis, and the upper boundary of $\Omega$ onto the positive imaginary axis. By checking the image of one point in $\Omega$, say $z=0$, we find $\phi(0)=\frac{2+i}{2-i}=\frac{1}{5}(3+4 i)$, which is a point in the first quadrant. Thus $\phi$ maps the region $\Omega$ onto the first quadrant and transforms the given problem into a Dirichlet problem in the first quadrant of the $w$-plane, with boundary conditions as shown in Figure 2(b).

ing
na-
ch-
ig-
ob-
ig-
em
ve,
ad-
ion

---

<!-- Page 30 -->

Left margin note (page 30)

414
Chapter 6

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-30_511_528_517_90.jpg)

Figure 3 Dirichle an annulus.

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-30_498_515_1653_789.jpg)

Figures 4(a) an A Dirichlet probl regular annulus is greatly simpl transforming the regular annulus using a linear fra formation.

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-30_498_541_1645_1499.jpg)

Right margin note (page 30)

lution
bblem
o it is les $T_{1}$
fo this
e unit
les
), such
s using
ne

→
circle, region undary ding to

++++

onformal Mappings

It is clear that the solution in the $w$-plane is $U(w)=\frac{200}{\pi} \operatorname{Arg} w$. Thus the so of the Dirichlet problem on $\Omega$ is
$$
u(z)=\frac{200}{\pi} \operatorname{Arg} \phi(z)=\frac{200}{\pi} \operatorname{Arg}\left(\frac{2+i}{2-i} \frac{2+z}{2-z}\right)
$$

For our next application, we recall the solution of the Dirichlet pro in an annular region (Figure 3), with constant boundary values:
$$
u(z)=T_{1}+\left(T_{2}-T_{1}\right) \frac{\ln \left(|z| / R_{1}\right)}{\ln \left(R_{2} / R_{1}\right)}, \quad R_{1}<|z|<R_{2}
$$

This function is harmonic in the complex plane minus the origin and s harmonic in the annulus $R_{1}<|z|<R_{2}$. The fact that it takes the valu and $T_{2}$ on the boundary can be verified directly. For the derivation 0 solution, see Exercise 30, Section 2.5. When the outer circle $C_{2}$ is th circle ( $R_{2}=1$ ), the solution becomes
$$
u(z)=T_{1}+\left(T_{1}-T_{2}\right) \frac{\ln |z|-\ln R_{1}}{\ln R_{1}}, \quad R_{1}<|z|<1
$$

EXAMPLE 3 A problem on a region between nonconcentric circ Find a harmonic function $u$ in the nonregular annular region $\Omega$ in Figure 4(a that $u=50$ on the inner circle $C_{1}$ and $u=100$ on the outer unit circle $C_{2}$.
Solution We transform the problem into a Dirichlet problem on an annulu: the linear fractional transformation of Example 4, Section 6.2,
$$
w=\phi(z)=\frac{3 z-1}{3-z}
$$
d (b) em in a non(Figure 4(a)) ified by first region into a Figure 4(b)), ctional trans-

As shown in Example 4, Section 6.2, $\phi$ maps the unit circle $C_{2}$ onto the uni the inner circle $C_{1}$ onto a circle centered at the origin with radius $\frac{1}{5}$, and the between the unit circle and $C_{2}$ onto the annular region $\frac{1}{5}<|w|<1$. The bo values in the transformed problem are shown in Figure 4(b), and so accor
(2) the solution of the Dirichlet problem in the $w$-plane is
$$
U(w)=50+50 \frac{\ln |w|+\ln 5}{\ln 5}, \quad \frac{1}{5}<|w|<1 .
$$

---

<!-- Page 31 -->

Left margin note (page 31)

\begin{table}
| $(x, y)$ | $(0$ |
| :---: | :---: |
| $u(x+i y)$ | 65 |
\captionsetup{labelformat=empty}
\caption{Table 1.}
\end{table}

THEOR
POISSON INTE FORMULA IN U]
HALF-Pl

Right margin note (page 31)

415
side
are
the
the
uld
the em, ula
tion lane iven

led
ing

$s$.
ane The The nks on

++++

Section 6.3 Solving Dirichlet Problems with Conformal Mappings

Substituting $w=\phi(z)=\frac{3 z-1}{3-z}$, we obtain the solution in the $z$-plane
$$
u(z)=50+50 \frac{\ln \left|\frac{3 z-1}{3-z}\right|+\ln 5}{\ln 5}
$$

With the help of a computer, we have evaluated the solution at various points in the nonregular annular region in Figure 4(a). The values are shown in Table 1

| 0$)$ | $\left(\frac{1}{7}-0.001,0\right)$ | $\left(\frac{1}{2}+0.001,0\right)$ | $(0.99,0.01)$ | $(0.99,-0.01)$ | $\left(\frac{1}{2}, \frac{1}{3}\right)$ | $\left(\frac{1}{2},-\frac{1}{3}\right)$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 87 | 50.15 | 50.20 | 99.38 | 99.38 | 74.73 | 74.73 |

Cemperature of various points inside the nonregular annular region in Figure 4(a).
The table seems to confirm the solution that we found. The values of $u(z)$ between 50 and 100. They are closer to the boundary values as $z$ approaches boundary (inner and outer). Note also the symmetric property of $u$, due to symmetries in the given problem: We have $u(x+i y)=u(x-i y)$. You sho expand the table of values and make your own conclusions about the solution.

We next derive the Poisson formula in the upper half-plane by using corresponding formula in the unit disk. We state the result in a theor but its proof is a simple application of the ideas of this section. (The form was also derived by a different method in the exercises of Section 2.5.)

LEM 1
GRAL
THE
PPER
LANE

Let $f(x)$ be a bounded piecewise smooth function on the real line. A solu of the Dirichlet problem $\Delta u(x+i y)=0$ for $x+i y$ in the upper half-p $(y>0)$ with boundary condition $u(x)=f(x)$ for all $-\infty<x<\infty$ is g by the Poisson integral formula
(3)
$$
u(x+i y)=\frac{y}{\pi} \int_{-\infty}^{\infty} \frac{f(s)}{(x-s)^{2}+y^{2}} d s=\frac{y}{\pi} \int_{-\infty}^{\infty} \frac{f(x-s)}{s^{2}+y^{2}} d s
$$

For $y>0$, the function $P_{y}(x)=\sqrt{\frac{2}{\pi}} \frac{y}{x^{2}+y^{2}} \quad(-\infty<x<\infty)$ is cal the Poisson kernel on the real line. (The constant $\sqrt{\frac{2}{\pi}}$ is a normaliz constant.) We can write (3) in terms of the Poisson kernel as
$$
u(x+i y)=\frac{1}{\sqrt{2 \pi}} \int_{-\infty}^{\infty} f(s) P_{y}(x-s) d s=\frac{1}{\sqrt{2 \pi}} \int_{-\infty}^{\infty} f(x-s) P_{y}(s) d
$$

This features the solution of the Dirichlet problem in the upper half-pl as a convolution of the boundary function $f$ with the Poisson kernel.
notion of convolution of functions will be discussed in later chapters.
Poisson kernel has a wealth of properties. This fundamental function li complex analysis in the upper half-plane to Fourier analysis of functions the real line.

---

<!-- Page 32 -->

Left margin note (page 32)

416
Chapter 6

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-32_525_1116_443_744.jpg)

Figure 5 How the values in a Dirichl are transformed, a linear fractional t tion that takes bo boundary.

++++

onformal Mappings

Proof We will prove the first equality in (3); the second one follows by m the change of variables $s^{\prime}=x-s$. Transform the given problem into a Dir problem in the unit disk using the linear fractional transformation $w=\psi(z)$ (Example 1(ii), Section 6.2). This mapping takes the real line onto the unit and the upper half-plane onto the unit disk. Denote the image of a point $s$ real line by $e^{i \phi}$ on the unit circle, so $e^{i \phi}=\psi(s)$.
boundary et problem after using ransformaundary to

As illustrated in Figure 5, the boundary data that we get for the problem on th disk is given by $U\left(e^{i \phi}\right)=f\left(\psi^{-1}\left(e^{i \phi}\right)\right)$, for all $e^{i \phi}$ on the unit circle. The solut the Dirichlet problem in the unit disk $(|w|<1)$ with this boundary data is obt from the Poisson integral formula, which we recall from (10), Section 3.8:
$$
U(w)=\frac{1-|w|^{2}}{2 \pi} \int_{0}^{2 \pi} \frac{f\left(\psi^{-1}\left(e^{i \phi}\right)\right)}{\left|e^{i \phi}-w\right|^{2}} d \phi
$$

Hence the solution in the upper half-plane is (set $w=\psi(z)$ in (5))
$$
u(x+i y)=U(\psi(x+i y))=U(\psi(z))=\frac{1-|\psi(z)|^{2}}{2 \pi} \int_{0}^{2 \pi} \frac{f\left(\psi^{-1}\left(e^{i \phi}\right)\right)}{\left|e^{i \phi}-\psi(z)\right|^{2}}
$$

Our goal is to show that (6) is precisely (3). The details are straightforward little tedious. Make the change of variables $s=\psi^{-1}\left(e^{i \phi}\right)$. Since the integra (6) is $2 \pi$-periodic, we get the same result if we integrate from $-\pi$ to $\pi$ instea to $2 \pi$; and as $\phi$ runs from $-\pi$ to $\pi, s$ runs from $-\infty$ to $\infty$. We have
$$
s=\psi^{-1}\left(e^{i \phi}\right) \Rightarrow \psi(s)=\frac{i-s}{i+s}=e^{i \phi}
$$

Taking differentials and using $e^{i \phi}=\frac{i-s}{i+s}$, we get
$$
\frac{-2 i}{(i+s)^{2}} d s=i e^{i \phi} d \phi=i \frac{i-s}{i+s} d \phi \Rightarrow d \phi=\frac{2}{1+s^{2}} d s
$$

Substituting what we have so far into (6), we obtain
$$
u(x+i y)=\frac{1-|\psi(z)|^{2}}{\pi} \int_{-\infty}^{\infty} \frac{f(s)}{\left|e^{i \phi}-\psi(z)\right|^{2}} \frac{d s}{1+s^{2}}
$$

Comparing (7) and (3), it suffices to show that for $z=x+i y$ and $e^{i \phi}=s$,
$$
\frac{1-|\psi(z)|^{2}}{\left|e^{i \phi}-\psi(z)\right|^{2}}=\left(1+s^{2}\right) \frac{y}{(x-s)^{2}+y^{2}}
$$

This part is straightforward and is left to Exercise 21.

---

<!-- Page 33 -->

Left margin note (page 33)

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-33_480_472_545_55.jpg)

Figure 6 For a given in $(a, b)$, the angle at $x+i$ tended by $(a, b)$ is a har function $\alpha(x+i y)$ calle harmonic measure of ( $a$.

++++

Section 6.3 Solving Dirichlet Problems with Conformal Mappings
41

EXAMPLE 4 Applying Poisson's integral formula
Solve the Dirichlet problem in the upper half-plane with boundary data on the re line given by
$$
f(x)=u(x)=\left\{\begin{array}{ll}
C & \text { if } a<x<b \\
0 & \text { otherwise }
\end{array}\right.
$$
where $C$ is a constant.
Solution We apply the first formula in (3) and get for $-\infty<x<\infty, y>0$,
$$
u(x+i y)=\frac{y}{\pi} \int_{-\infty}^{\infty} \frac{f(s)}{(x-s)^{2}+y^{2}} d s=\frac{y}{\pi} \int_{a}^{b} \frac{C}{(x-s)^{2}+y^{2}} d s
$$
since $f(s)$ is 0 outside the interval $a<s<b$. We evaluate the integral in terms the inverse tangent, using an obvious change of variables,
$$
\begin{aligned}
u(x+i y) & =\frac{y}{\pi} \int_{a}^{b} \frac{C}{(x-s)^{2}+y^{2}} d s=\frac{y}{\pi} \frac{C}{y^{2}} \int_{a}^{b} \frac{1}{\left(\frac{s-x}{y}\right)^{2}+1} d s \\
& =\frac{C}{\pi} \int_{\frac{a-x}{y}}^{\frac{b-x}{y}} \frac{d s}{s^{2}+1} \\
& =\frac{C}{\pi}\left[\tan ^{-1}\left(\frac{b-x}{y}\right)+\tan ^{-1}\left(\frac{x-a}{y}\right)\right]
\end{aligned}
$$

We can give a concrete geometric interpretation of this answer. Let $\alpha_{1}=\tan ^{-1}\left(\frac{b-}{3}\right.$ and $\alpha_{2}=\tan ^{-1}\left(\frac{x-a}{y}\right)$ (Figure 6). Then $u(x+i y)=\frac{C}{\pi}\left(\alpha_{1}+\alpha_{2}\right)=\frac{C}{\pi} \alpha(x+i y$ where $\alpha(x+i y)$ is the harmonic measure of the interval $(a, b)$; that is, $\alpha$ is the ang at the point $x+i y$ subtended by the interval $(a, b)$ (Figure 6). You should revie Exercise 35, Section 2.5, where this result was derived using guessing methods an properties of the argument function.

Suppose that $\Omega$ is a region, $f_{1}$ and $f_{2}$ are two functions defined on th boundary of $\Omega$. Suppose that $u_{1}$ and $u_{2}$ are solutions of the Dirichlet prob lems on $\Omega$ with boundary values $f_{1}$ and $f_{2}$, respectively. Because Laplace equation $\Delta u=0$ is linear, it is straightforward to check that $u=u_{1}+v$ solves the Dirichlet problem on $\Omega$ with boundary values $u=f_{1}+f_{2}$ on th boundary of $\Omega$. This useful process of generating a solution by adding sol tions of two or more related problems is called superposition of solution It will appear again in our study of other linear equations.

EXAMPLE 5 Superposing solutions
Let $\left(a_{1}, b_{1}\right)$ and $\left(a_{2}, b_{2}\right)$ be two disjoint intervals on the real line, and let $T_{1}$ an $T_{2}$ be two complex numbers. Solve the Dirichlet problem in the upper half-plat with boundary data on the real line given by $f(x)=T_{1}$ if $x$ is in $\left(a_{1}, b_{1}\right), T_{2}$ if $x$ in ( $a_{2}, b_{2}$ ) and 0 otherwise.
Solution For $j=1,2$, let $f_{j}(x)=T_{j}$ if $x$ is in $\left(a_{j}, b_{j}\right), 0$ otherwise. Clear $f(x)=f_{1}(x)+f-2(x)$. From Example 4, the solution of the Dirichlet proble

---

<!-- Page 34 -->

Left margin note (page 34)

418
Chapter 6

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-34_498_492_544_110.jpg)

Figure 7 for Ex

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-34_498_509_1604_126.jpg)

Figure 8 for E

Right margin note (page 34)

${ }_{j}(x)$ is riginal
ukowski
ane by ple 3, nfinite ions in $=100$ ling to
ad $y$.
sidues.
ry data
al with ed temed. The o $\infty$ as $\left.2+a^{2}\right)$. entrated
$$
>0,
$$
$$
\left.+y^{2}\right)
$$

++++

Conformal Mappings
in the upper half-plane with boundary values on the real line given by $f$. $u_{j}(z)=\frac{T_{j}}{\pi}\left[\tan ^{-1}\left(\frac{b_{j}-x}{y}\right)-\tan ^{-1}\left(\frac{a_{j}-x}{y}\right)\right]$. Thus the solution to our o problem is $u(z)=u_{1}(z)+u_{2}(z)$.

In the next example, we use the Poisson integral formula and the Jor mapping from Example 3, Section 6.1.
$\Delta u(z)=0$
ample 6 .
$$
\Delta u(z)=0
$$
$$
x)=P_{a}(x)
$$
xample 7 .

EXAMPLE 6 Joukowski mapping
Solve the Dirichlet problem shown in Figure 7.
Solution We transform the problem into a problem in the upper half-pl using the Joukowski mapping $w=J(z)=\frac{1}{2}\left(z+\frac{1}{z}\right)$. As shown in Exan Section 6.1, $J(z)$ takes the upper-unit circle onto $[-1,1]$, and the semi-i intervals $(-\infty,-1]$ and $[1, \infty)$ onto themselves. Thus the boundary condit the transformed Dirichlet problem in the upper half-plane are given by $f(w)$ for real $-1<w<1$ and $f(w)=0$ for real $w$ outside this interval. Accorc Example 4, the solution in the upper half of the $w$-plane is given by
$$
\frac{100}{\pi}\left[\tan ^{-1}\left(\frac{1-\operatorname{Re} w}{\operatorname{Im} w}\right)+\tan ^{-1}\left(\frac{1+\operatorname{Re} w}{\operatorname{Im} w}\right)\right] .
$$

Replacing $w$ by $J(z)$ we obtain the solution in the region $S$ :
$$
u(x+i y)=\frac{100}{\pi}\left[\tan ^{-1}\left(\frac{1-\operatorname{Re} J(z)}{\operatorname{Im} J(z)}\right)+\tan ^{-1}\left(\frac{1+\operatorname{Re} J(z)}{\operatorname{Im} J(z)}\right)\right]
$$

With a little bit more work, the answer could be expressed in terms of $x$ a
Our next example retests our ability to evaluate integrals using re

EXAMPLE 7 A Poisson boundary distribution
Solve the Dirichlet problem (Figure 8) in the upper half-plane with bounda on the real line given by a Poisson temperature distribution
$$
f(x)=u(x)=P_{a}(x)=\sqrt{\frac{2}{\pi}} \frac{a}{x^{2}+a^{2}}, \text { where } a>0 .
$$

This problem models the steady-state distribution in a large sheet of met insulated lateral surface, whose boundary along the $x$-axis is kept at a fix perature distribution given by a Poisson kernel $P_{a}(x)$, where $a>0$ is a fix temperature at the origin is $f(0)=u(0)=P_{a}(0)=\sqrt{\frac{2}{\pi}} \frac{1}{a}$, which tends $a$ tends to 0 . Away from the origin, the temperature decays to 0 like $a /(x$ So smaller values of $a>0$ correspond to temperature distributions conce around 0 (Figure 9).
Solution We apply the first formula in (3) and get for $-\infty<x<\infty$, $y$
$$
u(x+i y)=\frac{y}{\pi} \int_{-\infty}^{\infty} \frac{P_{a}(s)}{(x-s)^{2}+y^{2}} d s=\frac{a y}{\pi} \sqrt{\frac{2}{\pi}} \int_{-\infty}^{\infty} \frac{d s}{\left(s^{2}+a^{2}\right)\left((x-s)^{2}\right.}
$$

---

<!-- Page 35 -->

Left margin note (page 35)

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-35_361_456_205_76.jpg)

Figure 9 The Poisson $P_{y}(x)$ for various values 0 . Properties to note graphs of $P_{y}(x)$ as a fu of $x$ :
$P_{y}(x)>0$ for all $x$;
$P_{y}(x)$ is even;
$P_{y}(x)$ is a bell-shaped $\lim _{y\lfloor 0} P_{y}(0)=\infty$.
1.

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-35_475_481_1771_48.jpg)

Figure 10

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-35_469_524_1769_677.jpg)
![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-35_477_537_1767_1347.jpg)

++++

Section 6.3 Solving Dirichlet Problems with Conformal Mappings
419

We evaluate the last integral using the residue method of Section 5.3, by completing the contour with a semicircle in the upper half-plane. The function $h(z)= \frac{1}{\left(z^{2}+a^{2}\right)\left((x-z)^{2}+y^{2}\right)}$ has two simple poles in the upper half-plane, at $z=i a$ and at $z=x+i y$. We compute the residues at these points using Proposition 1, Section 5.1(iii). We have
$$
\operatorname{Res}(h(z), i a)=\frac{1}{(x-i a)^{2}+y^{2}} \operatorname{Res}\left(\frac{1}{\left(z^{2}+a^{2}\right)}, i a\right)=\frac{1}{(x-i a)^{2}+y^{2}} \frac{1}{2 i a}
$$
and
kernel of $y>$ on the nction
urve;
$$
\operatorname{Res}(h(z), x+i y)=\frac{1}{(x+i y)^{2}+a^{2}} \operatorname{Res}\left(\frac{1}{(x-z)^{2}+y^{2}}, x+i y\right)=\frac{1}{(x+i y)^{2}+a^{2}} \frac{1}{2 i y}
$$

Applying Proposition 2, Section 5.3, we obtain
$$
\begin{aligned}
u(x+i y) & =\frac{a y}{\pi} \sqrt{\frac{2}{\pi}} 2 \pi i(\operatorname{Res}(h(z), i a)+\operatorname{Res}(h(z), x+i y)) \\
& =2 a y i \sqrt{\frac{2}{\pi}}\left(\frac{1}{(x-i a)^{2}+y^{2}} \frac{1}{2 i a}+\frac{1}{(x+i y)^{2}+a^{2}} \frac{1}{2 i y}\right) \\
& =\sqrt{\frac{2}{\pi}}\left(\frac{y}{(x-i a)^{2}+y^{2}}+\frac{a}{(x+i y)^{2}+a^{2}}\right) \\
& =\sqrt{\frac{2}{\pi}} \frac{a+y}{x^{2}+(a+y)^{2}}
\end{aligned}
$$
where the last equality follows by elementary algebraic manipulations. This solves the problem. But note that the last expression is precisely $P_{a+y}(x)$. Thus $u(x+ i y)=P_{a+y}(x)$, which shows that the solution of the Dirichlet problem with a Poisson boundary data $P_{a}(x)$ is another Poisson distribution $P_{a+y}(x)$. This amazing fact about temperature problems with Poisson boundary data has a direct interpretation in terms of convolutions and Fourier transforms, which will be discussed in later chapters.
Exercises 6.3
In Exercises 1-15, (a) solve the Dirichlet problem described by the accompanying figure (Figures 10-24), using the methods of this section. Examples 4 and 5 and superposition of solutions are useful.
(b) Evaluate your answer at various points inside the region and comment on your data, as we did in Example 3.
2.

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-70_509_517_216_742.jpg)
Figure 11
3.

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-70_509_537_214_1407.jpg)
Figure 12

---

<!-- Page 36 -->

Left margin note (page 36)

420
Chapter 6
4.

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-36_498_521_229_81.jpg)

Figure 13
7.

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-36_490_518_822_98.jpg)

Figure 16
10.

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-36_490_531_1407_98.jpg)

Figure 19
13.

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-36_494_555_1988_94.jpg)

Figure 22

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-36_500_514_223_757.jpg)
![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-36_490_502_822_769.jpg)
![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-36_474_496_1407_783.jpg)
![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-36_464_486_1980_804.jpg)
![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-36_501_531_218_1424.jpg)
![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-36_494_536_818_1419.jpg)
![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-36_482_524_1399_1426.jpg)
![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-36_478_519_1980_1436.jpg)

Right margin note (page 36)

6.

Figure 15
9.

Figure 18
12.

Figure 21
15.

Figure 24

++++

onformal Mappings
5.

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-60_512_526_235_94.jpg)
Figure 14
8.

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-60_482_533_851_102.jpg)
Figure 17
11.

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-48_498_517_417_108.jpg)
Figure 20
14.

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-49_481_481_1599_51.jpg)
Figure 23

---

<!-- Page 37 -->

Left margin note (page 37)

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-37_442_483_1171_548.jpg)
![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-37_450_498_1165_1205.jpg)

Figures 25(a) and (b) Exercise 17.

++++

Section 6.3 Solving Dirichlet Problems with Conformal Mappings
421
16. Generalize Example 4 as follows. Suppose that $I_{1}=\left(a_{1}, b_{1}\right), I_{2}=\left(a_{2}, b_{2}\right)$, $\ldots, I_{n}=\left(a_{n}, b_{n}\right)$ are $n$ disjoint intervals on the real line, $T_{1}, T_{2}, \ldots, T_{n}$ are $n$ real or complex values. (a) Show that a solution of the Dirichlet problem in the upper half-plane with boundary data
$$
f(x)=\left\{\begin{array}{ll}
T_{j} & \text { if } a_{j}<x<b_{j}, \\
0 & \text { otherwise },
\end{array}\right.
$$
is
$$
u(x+i y)=\frac{1}{\pi} \sum_{j=1}^{n} T_{j}\left[\tan ^{-1}\left(\frac{b_{j}-x}{y}\right)-\tan ^{-1}\left(\frac{a_{j}-x}{y}\right)\right] .
$$

If any one of the $a_{j}$ 's is infinite, say $a_{1}=-\infty$, then $\tan ^{-1}\left(\frac{a_{1}-x}{y}\right)=\tan ^{-1}(-\infty)= -\frac{\pi}{2}$. Similarly, if one of the $b_{j}$ 's is infinite, say $b_{n}=\infty$, then $\tan ^{-1}\left(\frac{b_{n}-x}{y}\right)= \tan ^{-1}(\infty)=\frac{\pi}{2}$.
(b) Let $z=x+i y$. Show that the answer can be written as
$$
u(z)=\frac{1}{\pi} \sum_{j=1}^{n} T_{j}\left(\operatorname{Arg}\left(z-b_{j}\right)-\operatorname{Arg}\left(z-a_{j}\right)\right)
$$
17. (a) Solve the Dirichlet Problem in Figure 25(a) by using the Poisson integral formula.
for
(b) Solve the Dirichlet problem in Figure 25(b) by using the conformal map $w= \sin z$ and the result in part (a).
18. Show that the solution in Example 1 is
$$
u(x+i y)=50+\frac{100}{\pi}\left[\tan ^{-1}\left(\frac{y}{1-x}\right)+\tan ^{-1}\left(\frac{y}{1+x}\right)\right], \quad x^{2}+y^{2}<1 .
$$
19. Isotherms in Example 1. Recall the solution of the corresponding Dirichlet problem in the upper half of the $w$-plane, $\frac{100}{\pi}(\pi-\operatorname{Arg} w)$.
(a) Show that the isotherms in the $w$-plane are rays emanating from the origin.
(b) Conclude that the isotherms in the $z$-plane are arcs of circles in the unit disk. Describe the centers and radii of the circles that define the isotherms in the unit disk. [Hint: Consider the pre-image of the isotherms in the $w$-plane by the mapping $\phi(z)=i \frac{1-z}{1+z}$.]

---

<!-- Page 38 -->

Left margin note (page 38)

422
Chapter 6
30.

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-38_490_536_1374_88.jpg)

Figure 26
33.

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-38_511_550_1964_84.jpg)

Figure 29

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-38_493_513_1372_762.jpg)
![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-38_485_507_1964_775.jpg)
![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-38_496_550_1364_1415.jpg)
![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-38_495_546_1962_1423.jpg)

Right margin note (page 38)

oblem em in
stion:
$$
e^{i \pi}
$$
$\_\_\_\_$
graph of $a$.
bisson
th the aluate
rming
halfrmula
tegral

++++

onformal Mappings
20. Isotherms in Example 3. By studying the isotherms of the Dirichlet pr in the $w$-plane in Example 3, determine the isotherms of the original probl the $z$-plane.
21. Complete the proof of Theorem 1 by showing that (8) holds. [Sugge Organize your proof as follows. Show $1-|\psi(z)|^{2}=\frac{4 y}{x^{2}+(1+y)^{2}}$. Then show $\left.\psi(z)\right|^{2}=|\psi(s)-\psi(z)|^{2}=4 \frac{(x-s)^{2}+y^{2}}{\left(1+s^{2}\right)\left(x^{2}+(1+y)^{2}\right.}$. $]$
22. Show that $P_{a}(x)=\frac{1}{a} P_{1}\left(\frac{x}{a}\right)$ for all $a>0$. Thus the graph of $P_{a}(x)$ is the of $P_{1}(x)$, scaled vertically by a factor of $\frac{1}{a}$ and scaled horizontally by a factor
23. Show that for any $y>0, \frac{1}{\sqrt{2 \pi}} \int_{\infty}^{\infty} P_{y}(x) d x=1$, where $P_{y}(x)$ is the P kernel.
In Exercises 24-29, solve the Dirichlet problem in the upper half-plane wi boundary values on the $x$-axis given by $f(x)$ as indicated. Use residues to ev the Poisson integral. Take a real and $\neq 0$ in Exercises 28 and 29.
24. $f(x)=\frac{x}{x^{2}+x+1}$.
25. $f(x)=\frac{1}{x^{4}+1}$.
26. $f(x)=\frac{\sin x}{x}$.
27. $f(x)=\cos x$.
28. $f(x)=\cos a x$.
29. $f(x)=\sin a x$.

Solve the Dirichlet problem depicted in the figure (Figures 26-31) by transfo it into a Dirichlet problem in the upper half-plane. To solve in the upper plane, use the Arg function in Exercises 30-32, and the Poisson integral fo in Exercises 33-35. Leave your answer in Exercise 35 in the form of an ir involving the Chebyshev polynomials. Compute the integral when $n=2$.
31.

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-38_493_513_1372_762.jpg)
Figure 27
34.

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-38_485_507_1964_775.jpg)
Figure 30
32.

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-38_496_550_1364_1415.jpg)
Figure 28
35.

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-38_495_546_1962_1423.jpg)
Figure 31

---

<!-- Page 39 -->

Left margin note (page 39)

6.4 The Schwa

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-39_461_470_220_51.jpg)

Figure 1 Positively ori polygonal boundary witl ner angles measured fror outside.

THEORE SCHWA
CHRISTOF]
TRANSFORMATI

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-39_446_451_1420_51.jpg)

Figure 2 Unbounded pol nal region with $n$ sides ( $n$ and $n-1$ vertices.

++++

Section 6.4 The Schwarz-Christoffel Transformation
423
rz-

Christoffel Transformation
In this section we describe a method for constructing one-to-one analytic mappings of the upper half-plane onto polygonal regions. We start by setting the notation.

Suppose that $\Omega$ is a region in the $w$-plane, bounded by a positively oriented polygonal path $P$ with $n$ sides. Let $w_{1}, w_{2}, \ldots, w_{n}$ denote the vertices of $P$, counted consecutively as we trace the path through its positive orientation (see Figure 1, where $n=5$ ). If $P$ is bounded, then the point $w_{n}$ is taken to be the initial and terminal point of the closed path $P$. If $P$ is unbounded, we take $w_{n}=\infty$ and think of $P$ as a polygon with $n-1$ vertices $w_{1}, w_{2}, \ldots, w_{n-1}$ (Figure 2). It will be convenient to measure the exterior angle at a vertex, and so we let $\theta_{j}$ denote the angle that we make as we turn the corner of the polygon at $w_{j}$. We choose $0<\left|\theta_{j}\right|<\pi(j=1, \ldots, n)$; a positive value corresponds to a left turn and a negative value corresponds to a right turn. In Figure 1, $\theta_{2}$ is negative while all other $\theta_{j}$ are positive.

M 1

Let $\Omega$ be a region bounded by a polygonal path $P$ with vertices at $w_{j}$

RZ- (counted consecutively) and corresponding exterior angles $\theta_{j}$. Then there

FEL is a one-to-one conformal mapping $f(z)$ of the upper half-plane onto $\Omega$, such

ON that
$$
f^{\prime}(z)=A\left(z-x_{1}\right)^{-\frac{\theta_{1}}{\pi}}\left(z-x_{2}\right)^{-\frac{\theta_{2}}{\pi}} \cdots\left(z-x_{n-1}\right)^{-\frac{\theta_{n-1}}{\pi}},
$$
where the $x_{j}$ 's are real, $x_{1}<x_{2}<\cdots<x_{n-1}, f\left(x_{j}\right)=w_{j}, \lim _{z \rightarrow \infty} f(z)= w_{n}, A$ is a constant, and principal branches are used to define the powers.

The points $x_{j}(j=1, \ldots, n-1)$ on the $x$-axis are the pre-images of the vertices of the polygonal path $P$ in the $w$-plane. Two of the $x_{j}$ 's may be

$w_{3}$ chosen arbitrarily, so long as they are arranged in ascending order. We can express the fact that $\lim _{z \rightarrow \infty} f(z)=w_{n}$ by writing $f(\infty)=w_{n}$. In the case of an unbounded polygon $P$, we have $f(\infty)=\infty$.

The mapping $f(z)$ is called a Schwarz-Christoffel transformation, after the German mathematicians Herman Amandus Schwarz (1843-1921) and Elwin Bruno Christoffel (1829-1900). Since $f(z)$ is an antiderivative of (1), we can write

ygo-
$$
f(z)=A \int\left(z-x_{1}\right)^{-\frac{\theta_{1}}{\pi}}\left(z-x_{2}\right)^{-\frac{\theta_{2}}{\pi}} \cdots\left(z-x_{n-1}\right)^{-\frac{\theta_{n-1}}{\pi}} d z+B
$$

The constants $A$ and $B$ depend on the size and location of the polygonal path $P$. The full proof of Theorem 1 is quite complicated. We only sketch a part that illustrates the ideas behind the construction of the transformation.
Sketch of Proof of Theorem 1. Consider a mapping $f(z)$ whose derivative is given by (1) and let $w_{j}$ denote the image of $x_{j}$, where $x_{1}<x_{2}<\cdots<x_{n-1}$

---

<!-- Page 40 -->

Left margin note (page 40)

424
Chapter 6 Co

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-40_510_545_233_73.jpg)

Figure 3 Argumen line segments of th $P$.

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-40_485_501_933_83.jpg)

Figure 4 As $x$ cro left to right, $\arg f^{\prime}$ abruptly by $\theta_{j}$ th constant until it

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-40_514_519_1821_85.jpg)

Figure 5 for Exa

Right margin note (page 40)

rom by ke a -1 ,
onto iven and for by nent (5) rupt to a se of The ngle ative and real race or of e it. n be abers akes
o the swer re 5, ields

++++

nformal Mappings

are real. To understand the effect of the mapping $f$ on the real axis, recall $\mathfrak{f}$ Section 6.1 that a conformal mapping $f(z)$ at a point $z_{0}$ acts like a rotation an angle $\arg f^{\prime}\left(z_{0}\right)$. Thus the mapping whose derivative is given by (1) acts li rotation by an angle
$-\left(\theta_{2}+\theta_{3}+\theta_{4}\right) \left(x_{1}\right)$
ts of the e polygon
sses $x_{j}$ from ( $x$ ) changes aen remains rosses $x_{j+1}$.
$\Omega$
mple 1.
$$
\begin{array}{l}
\arg f^{\prime}(z)= \\
\quad \arg A-\frac{\theta_{1}}{\pi} \arg \left(z-x_{1}\right)-\frac{\theta_{2}}{\pi} \arg \left(z-x_{2}\right)-\cdots-\frac{\theta_{n-1}}{\pi} \arg \left(z-x_{n-1}\right) .
\end{array}
$$

For $z=x$ on the $x$-axis with $z<x_{1}$, we have $z-x_{j}<0$ for all $j=1,2, \ldots, n$ hence $\arg \left(z-x_{j}\right)=\pi$ for all $j=1,2, \ldots, n-1$, and so from (3) we get
$$
\arg f^{\prime}(z)=\arg A-\left(\theta_{1}+\theta_{2}+\cdots+\theta_{n-1}\right) .
$$

Thus if $w_{n}=f(\infty)$, then all the points in the interval $\left(-\infty, x_{1}\right)$ are mapped a line segment starting with $w_{n}$ and ending with $w_{1}=f\left(x_{1}\right)$ and at an angle $\mathbf{g}$ by (4) (Figure 3). For the points in the interval $\left(x_{1}, x_{2}\right)$, we have $z-x_{1}>0 z-x_{j}<0$ for all $j=2, \ldots, n-1$, hence $\arg \left(z-x_{1}\right)=0$ and $\arg \left(z-x_{j}\right)=\pi$ all $j=2, \ldots, n-1$, and so from (3)
$$
\arg f^{\prime}(z)=\arg A-\left(\theta_{2}+\cdots+\theta_{n-1}\right) .
$$

Thus, at $x_{1}$ we have an abrupt change in the argument (the path turns lef angle $\theta_{1}$ ) and then all the points in ( $x_{1}, x_{2}$ ) are mapped onto the line segn with initial point $w_{1}$ and terminal point $w_{2}=f\left(x_{2}\right)$, and at an angle given by (Figure 4). We continue in this fashion, and finally we find that after an ab change in the argument, the points in the interval $\left(x_{n-1}, \infty\right)$ are mapped on line segment with initial point $w_{n-1}$, and at angle $\arg f^{\prime}(z)=\arg A$. In the ca a bounded polygon, this line segment will connect back to $w_{n}$ (Exercise 11). polygon is then closed; after turning the last corner we have gone through an a $\theta_{1}+\theta_{2}+\cdots+\theta_{n}=2 \pi$. Thus we have shown that the mapping whose derive is given by (1) takes the real line onto a polygon with vertices $w_{j}=f\left(x_{j}\right)$ exterior angles $\theta_{j}$. Since the upper half-plane is to our left as we traverse the line rightward, conformality ensures that the image region is to our left as we $P$ in the positive sense (that is, $f$ maps the upper half-plane onto the interi $P)$. The converse of these statements is also true, although we will not prov That is, given a polygonal path $P$ with vertices $w_{j}$ and exterior angles $\theta_{j}$, it ca shown that we can find ordered real numbers $x_{1}, \ldots, x_{n-1}$, and complex num $A$ and $B$ such that the mapping given by (2) whose derivative is given by (1), the real line onto $P$. Moreover, two of the $x_{j}$ 's can be chosen arbitrarily.

EXAMPLE 1 Schwarz-Christoffel transformation for a sector
Find a Schwarz-Christoffel transformation that maps the upper half-plane ont sector at angle $0<\alpha<\pi$ in Figure 5.
Solution Obviously one answer is $f(z)=z^{\frac{\alpha}{\pi}}$, but let us see how this an comes out of (2). Since the region has two sides, we have $n=2$. From Figu the exterior angle at $w_{1}=0$ is $\pi-\alpha$. In the $z$-plane, choose $x_{1}=0$, then (2)
$$
f(z)=A \int z^{-\frac{\pi-\alpha}{\pi}} d z+B=A \int z^{-1+\alpha / \pi} d z+B=A \frac{\pi}{\alpha} z^{\frac{\alpha}{\pi}}+B
$$

---

<!-- Page 41 -->

Left margin note (page 41)

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-41_470_474_1028_47.jpg)

Figure 6 A semi-infinit tical strip with positivel ented boundary.

++++

Section 6.4 The Schwarz-Christoffel Transformation

where all branches are principal. In order to have $f(0)=0$, we take $B=$ Obviously any positive value of $A$ will work, so we can take $f(z)=z^{\frac{a}{\pi}}$.

For our next example, we will need the following useful formula, who proof is sketched in Exercise 12. For $z$ in the upper half-plane ( $\operatorname{Im} z>0 0 \leq \alpha \leq \pi$, and all real numbers $a$, we have
(6) $(z+a)^{\frac{\alpha}{\pi}}(z-a)^{\frac{\alpha}{\pi}}=(-1)^{\frac{\alpha}{\pi}}\left(a^{2}-z^{2}\right)^{\frac{\alpha}{\pi}}$, all branches are principal.

For example, if $\alpha=\frac{\pi}{2}, a=1$, and $\operatorname{Im} z>0$, then
$$
(z+1)^{\frac{1}{2}}(z-1)^{\frac{1}{2}}=i\left(1-z^{2}\right)^{\frac{1}{2}}
$$

EXAMPLE 2 The inverse sine as a Schwarz-Christoffel transformatic
Find a Schwarz-Christoffel transformation that maps the upper half-plane onto th the semi-infinite vertical strip in Figure 6.
Solution We know that $\sin z$ maps the infinite strip in Figure 6 onto the upp half-plane. So the mapping that we are looking for is the inverse of $\sin z$. Let us s how this comes out of (2). In the $w$-plane, take $w_{1}=-\frac{\pi}{2}, w_{2}=\frac{\pi}{2}$, with exteri angles $\theta_{1}=\theta_{2}=\frac{\pi}{2}$. In the $z$-plane, take $x_{1}=-1$ and $x_{2}=1$. Then (2) yields
$$
f(z)=A \int(z+1)^{-\frac{1}{2}}(z-1)^{-\frac{1}{2}} d z+B
$$

Using (7) and a well-known antiderivative, we get
$$
f(z)=-A i \int \frac{1}{\sqrt{1-z^{2}}} d z+B=-A i \sin ^{-1} z+B
$$
where $\sin ^{-1} z$ is the principal branch of the inverse sine function; that is,
$$
\sin ^{-1} z=-i \log \left(i z+e^{\frac{1}{2} \log \left(1-z^{2}\right)}\right)
$$
(see Example 3, Section 1.7). Setting $f(-1)=-\frac{\pi}{2}$, we find
$$
-A i \sin ^{-1}(-1)+B=-\frac{\pi}{2} \quad \Rightarrow \quad A i \frac{\pi}{2}+B=-\frac{\pi}{2}
$$

Setting $f(1)=\frac{\pi}{2}$, we find
$$
-A i \sin ^{-1}(1)+B=\frac{\pi}{2} \quad \Rightarrow \quad-A i \frac{\pi}{2}+B=\frac{\pi}{2} .
$$

Solving for $A$ and $B$, we find $A=i$ and $B=0$. Hence $f(z)=\sin ^{-1} z$.

---

<!-- Page 42 -->

Left margin note (page 42)

426
Chapter 6

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-42_501_498_658_120.jpg)

Figure 7 Posit isosceles triangl

Right margin note (page 42)

ations, hough ulated ons in
nto the ertices , with $=-1$
rms of $= \pm 1$ using
os $x d x$,
gral in tained
puting

++++

Conformal Mappings

Like many constructions involving Schwarz-Christoffel transform the next example gives rise to elliptic integrals (see Section 5.5). Alt these integrals are very difficult to evaluate, they are extensively tab and can be conveniently evaluated numerically using standard functi most computer systems.

EXAMPLE 3 Schwarz-Christoffel transformation for a triangle
Find a Schwarz-Christoffel transformation that maps the upper half-plane or right isosceles triangle in Figure 7.

lane

Solution It is clear that the triangle is determined by two consecutive and their corresponding angles. In the $w$-plane, take $w_{1}=-1, w_{2}=1$ exterior angles $\theta_{1}=\theta_{2}=\frac{3 \pi}{4}$. In the $z$-plane, we freely choose the points $x_{1}$ and $x_{2}=1$. Then (2) yields
$$
f(z)=A \int_{0}^{z}(\zeta+1)^{-\frac{3}{4}}(\zeta-1)^{-\frac{3}{4}} d \zeta+B=A \int_{0}^{z} \frac{d \zeta}{(-1)^{\frac{3}{4}}\left(1-\zeta^{2}\right)^{\frac{3}{4}}}+B
$$
where we have used (6) with $\alpha=\frac{3 \pi}{4}$. This integral cannot be expressed in te elementary functions for arbitrary $z$, but we will be able to evaluate it for $z$ in order to determine the constants $A$ and $B$. Setting $f(-1)=-1$ and $(-1)^{\frac{3}{4}}=e^{\frac{3 \pi i}{4}}$, we get
$$
-1=e^{-\frac{3 \pi i}{4}} A \int_{0}^{-1} \frac{d \zeta}{\left(1-\zeta^{2}\right)^{\frac{3}{4}}}+B=-e^{-\frac{3 \pi i}{4}} A \int_{0}^{1} \frac{d \zeta}{\left(1-\zeta^{2}\right)^{\frac{3}{4}}}+B
$$
or
$$
-e^{-\frac{3 \pi i}{4}} A I+B=-1, \text { where } I=\int_{0}^{1} \frac{d \zeta}{\left(1-\zeta^{2}\right)^{\frac{3}{4}}}
$$

To evaluate the integral $I$, we make the change of variables $\zeta=\sin x, d \zeta=\mathrm{cc}$ then
$$
I=\int_{0}^{\frac{\pi}{2}} \frac{d x}{(\cos x)^{\frac{1}{2}}}=\frac{1}{2} \frac{\Gamma(1 / 4) \Gamma(1 / 2)}{\Gamma(3 / 4)} \approx 2.622,
$$
where we have appealed to Exercise 25, Section 4.3, to evaluate the inte terms of the gamma function. The approximate value of the integral was ob with the help of a computer. Setting $1=f(1)$, we get
$$
e^{-\frac{3 \times i}{4}} A I+B=1 .
$$

Solving for $A$ and $B$ in (9) and (8), we find $B=0$ and $A=\frac{e^{\frac{3 \pi}{T}}}{T}$, and so
$$
f(z)=\frac{e^{\frac{3 \pi}{4}}}{I} e^{-\frac{3 \pi}{4}} \int_{0}^{z} \frac{d \zeta}{\left(1-\zeta^{2}\right)^{\frac{3}{4}}}=\frac{1}{I} \int_{0}^{z} \frac{d \zeta}{\left(1-\zeta^{2}\right)^{\frac{3}{4}}} .
$$

The next two examples illustrate a limiting technique in com Schwarz-Christoffel transformations.

---

<!-- Page 43 -->

Left margin note (page 43)

An $L$-shaped region wi itively oriented bounda we follow the bounda cording to this orien the region is to our left

Right margin note (page 43)

427
the
the
gion
and
g a
cior
ose
-1 ,
ped
$+$
for
圆

++++

Section 6.4 The Schwarz-Christoffel Transformation

EXAMPLE 4 An $L$-shaped region
Find a Schwarz-Christoffel transformation that maps the upper half-plane onto $L$-shaped region in Figure 8.
Solution To determine the orientation of the boundary in such a way that region becomes interior to a positively oriented boundary, we think of the re as a limit of a region with vertices at $w_{1}=0, w_{2}>0$, and $w_{3}=1+i$, corresponding exterior angles $\theta_{1}=\frac{\pi}{2}, \theta_{2}=\alpha$, and $\theta_{3}=\beta$ (Figure 9).

th pos-
ry. As
ry ac-
tation,

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-69_502_533_1955_687.jpg)
Figure 8

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-69_506_541_1949_1375.jpg)
Figure 9

As $w_{2} \rightarrow \infty, \theta_{2} \rightarrow \pi$, and $\theta_{3} \rightarrow-\frac{\pi}{2}$. Thus, we may think of our region as havin vertex at infinity with exterior angle $\theta_{2}=\pi$ and a vertex at $w_{3}=1+i$ with exter angle $-\frac{\pi}{2}$. In fact, setting $\theta_{j}=\pi$ will force $f\left(x_{j}\right)=\infty$. Now we may only cho two of the three $x_{j}$ 's arbitrarily, but in fact a solution can be found in $x_{1}= x_{2}=0$, and $x_{3}=1$. Other choices of the three $x_{j}$ 's will typically result in $L$-sha regions where the angle $\phi$ in Figure 8 is not $\pi / 4$. From (2) and (7)
$$
f(z)=A \int(z+1)^{-\frac{1}{2}} z^{-1}(z-1)^{\frac{1}{2}} d z+B=A \int \frac{z-1}{i z\left(1-z^{2}\right)^{\frac{1}{2}}} d z+B
$$

We have
$$
\frac{z-1}{i z\left(1-z^{2}\right)^{\frac{1}{2}}}=\frac{-i}{\left(1-z^{2}\right)^{\frac{1}{2}}}+\frac{i}{z\left(1-z^{2}\right)^{\frac{1}{2}}} .
$$

We have $\int \frac{-i d z}{\left(1-z^{2}\right)^{\frac{1}{2}}}=-i \sin ^{-1} z+C$, and letting $z=\frac{1}{\zeta}, d z=-\frac{d \zeta}{\zeta^{2}}$, we have
$$
\int \frac{i d z}{z\left(1-z^{2}\right)^{\frac{1}{2}}}=-i \int \frac{d \zeta}{\zeta\left(1-\frac{1}{\zeta^{2}}\right)^{\frac{1}{2}}}=\int \frac{d \zeta}{\left(1-\zeta^{2}\right)^{\frac{1}{2}}}=\sin ^{-1} \zeta+C
$$
where justification involving the square root is left to Exercise 13. Thus
$$
f(z)=A\left(-i \sin ^{-1} z+\sin ^{-1} \frac{1}{z}\right)+B,
$$
where inverse sines are principal branches. Setting $f(-1)=0$, we get $A\left(-i\left(-\frac{\pi}{2}\right)\right. \left.\left(-\frac{\pi}{2}\right)\right)+B=0$. Setting $f(1)=1+i$, we get $A\left(-i \frac{\pi}{2}+\frac{\pi}{2}\right)+B=1+i$. Solving $A$ and $B$, we get $A=\frac{i}{\pi}$ and $B=\frac{1+i}{2}$, and so
$$
f(z)=\frac{1}{\pi}\left(\sin ^{-1} z+i \sin ^{-1} \frac{1}{z}\right)+\frac{1+i}{2} .
$$

---

<!-- Page 44 -->

Left margin note (page 44)

428
Chapter 6

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-44_502_514_182_75.jpg)

Figure 10 A d plane with a posi ented boundary co four sides.

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-44_474_520_921_87.jpg)

Figure 11

PROPOS
IMAGE OI

Right margin note (page 44)

$+B$.
the ve a to a tion be $w)$ ). ad it es 3, lows now ce $C$ curve herm
), we
$U$.

++++

nformal Mappings

EXAMPLE 5 A doubly slit plane
Find a Schwarz-Christoffel transformation that maps the upper half-plane the doubly slit plane in Figure 10, which consists of the $w$-plane minus the semi-infinite horizontal lines $\operatorname{Im} w= \pm i$ and $\operatorname{Re} w<0$.
Solution To define the region as the interior of a positively oriented bound requires four sides as shown in Figure 10. We think of the region as a limit of a re with vertices at $w_{1}=i, w_{2}=t$ (where $t<0$ ) and $w_{3}=-i$, and correspon exterior angles $\theta_{1}=\alpha, \theta_{2}=\beta$, and $\theta_{3}=\gamma$ (Figure 11). As $t \rightarrow-\infty, \theta_{1} \rightarrow \theta_{2} \rightarrow \pi$, and $\theta_{3} \rightarrow-\pi$. Thus, we may think of our region as having a verte $w_{2}=\infty$ with exterior angle $\theta_{2}=\pi$ and two vertices at $\pm i$ with each exterior a being $-\pi$. Taking $x_{1}=-1, x_{2}=0$, and $x_{3}=1$, we get from (2)
$$
f(z)=A \int(z+1) \frac{1}{z}(z-1) d z+B=A \int\left(z-\frac{1}{z}\right) d z+B=\frac{A}{2} z^{2}-A \log z
$$

Setting $f(-1)=i$ and $f(1)=-i$, we get
$$
\left\{\begin{array} { r l } 
{ i } & { = \frac { A } { 2 } - A \operatorname { L o g } ( - 1 ) + B } \\
{ - i } & { = \frac { A } { 2 } - A \operatorname { L o g } ( 1 ) + B , }
\end{array} \Rightarrow \left\{\begin{array}{rl}
i & =\frac{A}{2}-A i \pi+B \\
-i & =\frac{A}{2}+B
\end{array}\right.\right.
$$

Solving for $A$ and $B$ we get $A=-\frac{2}{\pi}$ and $B=\frac{1}{\pi}-i$, and so
$$
f(z)=-\frac{1}{\pi} z^{2}+\frac{2}{\pi} \log z+\frac{1}{\pi}-i
$$

Image of Level Curves
Suppose that $f(z)$ is a Schwarz-Christoffel transformation taking upper half-plane onto a region $\Omega$ in the $w$-plane. If we want to sol Dirichlet problem $\Delta U(w)=0$, the technique is to map the problem corresponding problem in the upper half of the $z$-plane, where a solu $u(z)$ of Laplace's equation $\Delta u(z)=0$ with boundary conditions car obtained more easily. The solution in the $w$-plane is then $U(w)=u\left(f^{-1}(\right.$ However, the Schwarz-Christoffel transformation gives us $f$, not $f^{-1}$, ar is not always possible or easy to invert $f(z)$ in closed form (try Exampl 4 , and 5). Nevertheless, the conformal map $f(z)$ is still very useful: It al us to find isotherms of $U(w)$ without actually knowing $U(w)$. As we show, this is because the image under $f$ of an isotherm $u(z)=C$ (wher is a constant) is an isotherm $U(w)=C$ in the region $\Omega$.

ITION 1
LEVEL
CURVES
With the preceding notation, the image under $w=f(z)$ of the level $u(z)=C$ is a level curve $U(w)=C$. Thus, if $\gamma(t)$ parametrizes an isot of $u$, then $f(\gamma(t))$ parametrizes a corresponding isotherm of $U$.

Proof Since $\gamma(t)$ is a level curve of $u, u(\gamma(t))=C$. Since $U(w)=u\left(f^{-1}(w)\right.$ conclude that $U(f(\gamma(t)))=u(\gamma(t))=C$, and hence $f(\gamma(t))$ is a level curve of

---

<!-- Page 45 -->

Left margin note (page 45)

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-45_447_460_199_64.jpg)

Figure 12 for Example

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-45_445_456_705_61.jpg)

Figure 13 Isotherms ir ample 6 .

++++

Section 6.4 The Schwarz-Christoffel Transformation
429

This proposition is of course true for any one-to-one conformal map, not just for Schwarz-Christoffel transformations acting on the upper half-plane. We illustrate with an example.

EXAMPLE 6 Isotherms in the $L$-shaped region
Find the isotherms of the Dirichlet problem $\Delta U(w)=0$ in Figure 12.
Solution From Example 4, we know that the Schwarz-Christoffel transformation $f(z)=\frac{1}{\pi}\left(\sin ^{-1} z+i \sin ^{-1} \frac{1}{z}\right)+\frac{1+i}{2}$ will map the upper half-plane onto the $L$ shaped region. Since the boundary data switches from 0 to 100 at $f(1)=1+i$, the corresponding Dirichlet problem in the upper half-plane is $\Delta u(z)=0, u(x)=0$ for

6. $x<1$, and $u(x)=100$ for $x>1$. We immediately write down the solution using the argument function:
$$
u(z)=100-\frac{100}{\pi} \operatorname{Arg}(z-1)
$$

The isotherms $u=C$ thus satisfy $\operatorname{Arg}(z-1)=\pi-\frac{\pi C}{100}$ and are rays emanating from the point $z=1$. Each ray is parametrized by $\gamma(t)=1+t e^{i\left(\pi-\frac{\pi C}{100}\right)}$, where $0<t<\infty$. By Proposition 1, the image of this ray under $w=f(z)$ is the isotherm $U=C$ in the $L$-shaped region; and it is parametrized by
$$
f(\gamma(t))=\frac{1}{\pi}\left(\sin ^{-1}\left(1+t e^{i\left(\pi-\frac{\pi C}{100}\right)}\right)+i \sin ^{-1}\left(\frac{1}{1+t e^{i\left(\pi-\frac{\pi C}{100}\right)}}\right)\right)+\frac{1+i}{2}
$$

Some isotherms are plotted in Figure 13.
Fluid Flow
We will investigate problems in two-dimensional fluid flow, using our knowledge of harmonic functions and the technique of conformal mapping. In an ideal situation where fluid is flowing over a two-dimensional surface represented by an unbounded region $\Omega$ in the $z$-plane, assuming that the fluid is incompressible (fixed density) and irrotational (circulation around a closed path is zero), it can be shown that there is a harmonic function $\phi(x, y)$ such that the velocity $V(x, y)$ of a point $(x, y)$ in $\Omega$ is given by the gradient of $\phi$. That is,
$$
V(x, y)=\nabla \phi(x, y)=\left(\frac{\partial \phi}{\partial x}, \frac{\partial \phi}{\partial y}\right)=\left(\phi_{x}, \phi_{y}\right) .
$$

The function $\phi$ is called the velocity potential of the flow. The curves defined by the relation
$$
\phi(x, y)=C_{1}
$$
are called the equipotential curves or equipotential lines. The streamlines of the flow are the curves that are orthogonal to the equipotential curves. If the streamlines are expressed in the form
$$
\psi(x, y)=C_{2},
$$

---

<!-- Page 46 -->

Left margin note (page 46)

430
Chapter 6
C

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-46_498_535_686_80.jpg)

Figure 14 Streat uniform rightward upper half-plane.

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-46_516_543_1829_96.jpg)

Figure 15 Stre sector.

Right margin note (page 46)

ow. and s the one
form $z=$ the nt of given rties o the
the be a takz) be ings, tells are nd $\Gamma (w)$.
$$
=y
$$
using
along
$=z^{\frac{1}{4}}$
ream
nes in
he $w$ -
meter
Fluid

++++

onformal Mappings

for some function $\psi$, then, from Section 2.5, we know that we can take be the harmonic conjugate of $\phi$ in $\Omega$. The function $\psi$ is called the st function. The fluid will flow on the level curves of $\psi$. If we let
$$
\Phi(z)=\phi(x, y)+i \psi(x, y) \quad(z=x+i y \text { in } \Omega)
$$
then $\Phi$ is analytic in $\Omega$. It is called the complex potential of the Thus the real part of the complex potential is the velocity potential the level curves of its imaginary part are the streamlines. If $\Gamma$ denote boundary of $\Omega$, we would expect the fluid to flow along $\Gamma$ or that $\Gamma$ i of the streamlines. Thus the points on $\Gamma$ should satisfy (12).

For a simple example of a complex potential, we consider a uni rightward flow in the upper half-plane with complex potential $\Phi(z)= x+i y$ (Figure 14). Here the velocity potential is $\phi(x, y)=x$, and velocity at each point is given by the vector $(1,0)$, which is the gradie $\phi(x, y)=x$. The stream function is $\psi(x, y)=y$, and streamlines are as $\psi(x, y)=C$ for some constant $C \geq 0$. In accordance with the prope of a flow, the boundary $y=0$ is one of the streamlines corresponding t value $C=0$.

Given an unbounded region $\Omega$ in the $w$-plane, how can we find streamlines? We will apply conformal mapping techniques. Let $f$ one-to-one conformal mapping of the upper half of the $z$-plane onto $\Omega$, ing the $x$-axis onto $\Gamma$, the boundary of $\Omega$. Let a stream function $\psi(z$ given for the upper half-plane. By the properties of conformal mapp $\Psi(w)=\psi\left(f^{-1}(w)\right)$ will be harmonic for all $w$ in $\Omega$. Proposition 1 us that the images of streamlines $\psi(z)=C$ under the mapping $f(z$ streamlines $\Psi(w)=C$. Since the real axis is a streamline for $\psi(z)$ a is the image of the real axis, we conclude that $\Gamma$ is a streamline for $\Psi$ Thus $\Psi(w)$ is a stream function for $\Omega$.

In the following examples, we take the simple stream function $\psi(z$ for the upper half-plane. Streamlines for the region $\Omega$ are found by Proposition 1.

EXAMPLE 7 Fluid flow in a sector
Find and plot the streamlines for the sector in Figure 15, where fluid flows in the line $\operatorname{Arg} w=\frac{\pi}{4}$ and flows out along $\operatorname{Arg} w=0$.
Solution From Example 1, the Schwarz-Christoffel transformation $f(z)$ maps the upper half-plane to the given sector. We will use the simple s function in the upper half-plane, $\psi(z)=y$, to generate a solution. Streamli the $z$-plane are parametrized as $\gamma(x)=x+i y_{0}$ for fixed $y_{0}$. Streamlines in $t$ plane are images of these under $f$; we have $f(\gamma(x))=\left(x+i y_{0}\right)^{\frac{1}{4}}$. As the para $x$ increases, the streamlines are traced in the manner shown in Figure 15. comes in along $\operatorname{Arg} w=\frac{\pi}{4}$ and out along $\operatorname{Arg} w=0$.

---

<!-- Page 47 -->

Left margin note (page 47)

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-47_489_485_330_67.jpg)

Figure 16 Streamline doubly slit plane.

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-47_473_469_1445_67.jpg)

Figure 17

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-47_469_514_1449_693.jpg)
![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-47_477_524_1445_1366.jpg)

Right margin note (page 47)

$\bar{m}$
M
□

"be
Oveñ
Sour
□

Lurt
$\Xi$
of
$110 \dot{=}$
ت

++++

Section 6.4 The Schwarz-Christoffel Transformation

EXAMPLE 8 Fluid flow in the doubly slit plane
Find and plot the streamlines for the doubly slit plane in Figure 16, where f flows in from the upper left, past the double obstacle, and flows out to the lo left.

Solution In Example 5, we found that $f(z)=-\frac{1}{\pi} z^{2}+\frac{2}{\pi} \log z+\frac{1}{\pi}-i$ conformal mapping of the upper half-plane onto the doubly slit plane $\Omega$. Tak $\psi(z)=y$ to be the stream function for the upper half-plane, for each $y_{0} \geq 0$ we h a streamline parametrized by $\gamma(x)=x+i y_{0},-\infty<x<\infty$. By Proposition 1, images $f(\gamma(x))$ are streamlines in the doubly slit plane. They are
$$
f\left(x+i y_{0}\right)=-\frac{1}{\pi}\left(x+i y_{0}\right)^{2}+\frac{2}{\pi} \log \left(x+i y_{0}\right)+\frac{1}{\pi}-i \quad(-\infty<x<\infty) .
$$

The streamlines are plotted in Figure 16. Note that the central channel ser neither as a source of fluid nor as a final destination; fluid flows in and then flo out. The fluid far into the central channel is almost stagnant.

Exercises 6.4
In Exercises 1-6, find the Schwarz-Christoffel transformation of the upper half-plo onto the given region. Use the labeled points to set-up the integral (2).
1. See Figure 17. [Hint: Use (7) and integrate.]
2. See Figure 18. [Hint: $\frac{z+1}{(z-1)^{\frac{1}{2}}}=\frac{z-1+2}{(z-1)^{\frac{1}{2}}}=(z-1)^{\frac{1}{2}}+\frac{2}{(z-1)^{\frac{1}{2}}}$.]
3. See Figure 19. [Hint: $\frac{(z+1)^{\frac{1}{2}}}{(z-1)^{\frac{1}{2}}}=\frac{z+1}{i\left(1-z^{2}\right)^{\frac{1}{2}}}=\frac{z}{i\left(1-z^{2}\right)^{\frac{1}{2}}}+\frac{1}{i\left(1-z^{2}\right)^{\frac{1}{2}}}$.]

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-60_492_513_838_785.jpg)
Figure 18

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-60_495_549_828_1440.jpg)
Figure 19
4. See Figure 20. [Hint: $\frac{(z-1)^{\frac{1}{2}}}{(z+1)^{\frac{1}{2}}}=\frac{z-1}{i\left(1-z^{2}\right)^{\frac{1}{2}}}=\frac{z}{i\left(1-z^{2}\right)^{\frac{1}{2}}}-\frac{1}{i\left(1-z^{2}\right)^{\frac{1}{2}}}$.]
5. See Figure 21. [Hint: Let $z=\sin \zeta$, where $-\frac{\pi}{2} \leq \operatorname{Re} \zeta \leq \frac{\pi}{2}$ and $\operatorname{Im} \zeta \geq 0$. Th $\left(1-z^{2}\right)^{\frac{1}{2}}=\cos \zeta$. Use $\cos ^{2} \zeta=\frac{1+\cos 2 \zeta}{2}$, integrate, then use $\sin 2 \zeta=2 \sin \zeta \cos \zeta$.
6. See Figure 22. [Hints: $\frac{(z-1)^{\frac{1}{2}}}{z+1}=\frac{1}{(z-1)^{\frac{1}{2}}} \frac{z-1}{z+1}=\frac{1}{(z-1)^{\frac{1}{2}}}-\frac{2}{(z-1)^{\frac{1}{2}}} \frac{1}{z+1}$. In t second term, use $\frac{1}{z+1}=\frac{i}{2 \sqrt{2}}\left(\frac{1}{\sqrt{z-1}+i \sqrt{2}}-\frac{1}{\sqrt{z-1}-i \sqrt{2}}\right)$, and change variables $u \sqrt{z-1}-i \sqrt{2}$ and $v=\sqrt{z-1}-i \sqrt{2}$. You cannot find $A$ and $B$ just from $f(1)=$ Instead, first argue that $\operatorname{Arg} A=-\frac{\pi}{2}$ (look at the angle of the final line segmer

---

<!-- Page 48 -->

Left margin note (page 48)

432
Chapter 6

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-48_498_517_417_108.jpg)

Figure 20

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-48_502_508_407_775.jpg)
![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-48_498_539_401_1428.jpg)

Right margin note (page 48)

from width
ere the $1^{\circ}$. (a) rms in ).
ere the rature nple 6.
rcise 1.
1 show
r $f(z)$,
. $n-1$.
ate the ve take and 1 .
$x$ real, o show to be

Then
$I(R)$.

++++

Conformal Mappings

see the proof of Theorem 1) and thus $A=-i|A|$. Now get $B=i \pi \sqrt{2} \mid A f(1)=0$. To get $|A|$, either use $\operatorname{Im} f(x)=1$ for $x<1$, or use the channel formula (16) $1=|s|=\pi|A|\left|x_{2}-x_{1}\right|^{-\frac{\theta_{2}}{\pi}}$.]

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-48_502_508_407_775.jpg)
Figure 21

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-48_498_539_401_1428.jpg)
Figure 22
7. Consider the Dirichlet problem in the triangular region of Example 3, whe base is kept at temperature $100^{\circ}$ and the other two sides at temperature 0 Determine the isotherms in the triangular region by first studying the isothe the upper half-plane of the corresponding Dirichlet problem (see Example 6
(b) Plot several isotherms to illustrate your answer in (a).
8. Consider the Dirichlet problem in the semi-infinite strip of Example 2, whe base is kept at temperature $100^{\circ}$ and the other two vertical sides at tempe $0^{\circ}$. (a) Determine the isotherms in the region by following the method of Exar
(b) Plot several isotherms to illustrate your answer in (a).
9. Find and plot the streamlines in the region of Example 1.
10. Find and plot the streamlines in the image of the upper half-plane in Exe
11. Project Problem: Closure of the polygon. In this exercise, we wil that for a closed polygon where $\theta_{1}+\cdots+\theta_{n}=2 \pi$, the integral formula fo (2), converges to $w_{n}$ as $z \rightarrow \infty$.
(a) Use $\theta_{n}<\pi$ to show that $\theta_{1}+\cdots+\theta_{n-1}>\pi$. Define $\beta_{j}=\frac{\theta_{j}}{\pi}$ for $j=1, \ldots$ Then $\beta_{1}+\cdots+\beta_{n-1}>1$.
(b) Note that the coefficients $A$ and $B$ in (1) will dilate, rotate, and transla mapping and do not affect convergence of $f(z)$ or closure of the polygon, so $\mathbf{v} A=1$ and $B=0$. For concreteness, pick $z_{0}$ real to be the larger of $x_{n-1}$ and set
$$
f(z)=\int_{z_{0}}^{z} \frac{d \zeta}{\left(\zeta-x_{1}\right)^{\beta_{1}}\left(\zeta-x_{2}\right)^{\beta_{2}} \cdots\left(\zeta-x_{n-1}\right)^{\beta_{n-1}}}
$$
(c) We show that $f(z)$ has a limit on the positive real axis. Restrict $z=$ and use the limit comparison test for the integrand (against $\frac{1}{x^{s_{1}+\cdots+s_{n-1}}}$ ) t that $\lim _{x \rightarrow \infty} f(x)=\int_{z_{0}}^{\infty} \frac{d \zeta}{\left(x-x_{1}\right)^{\beta_{1}\left(x-x_{2}\right)^{\beta_{2} \ldots\left(x-x_{n-1}\right)^{\beta_{n-1}}}}}$ is finite. Define $w_{r}$ this number.
(d) To show that $\lim _{z \rightarrow \infty} f(z)=w_{n}$ for any $|z| \rightarrow \infty$, write $z=R e^{i \theta}, R>0$
$$
\left|f\left(R e^{i \theta}\right)-f(R)\right|=\left|\int_{R}^{R e^{i \theta}} \frac{d z}{\left(z-x_{1}\right)^{\beta_{1}}\left(z-x_{2}\right)^{\beta_{2}} \cdots\left(z-x_{n-1}\right)^{\beta_{n-1}}}\right| \leq R \pi \Lambda
$$

---

<!-- Page 49 -->

Left margin note (page 49)

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-49_481_481_1599_51.jpg)

Figure 23 The channel separation $s$.

Right margin note (page 49)

$1 \equiv$
$\Xi=7=1$
$0=y^{-1} 0$
$\Rightarrow \quad \Xi \| \varphi$

++++

Section 6.4 The Schwarz-Christoffel Transformation

where $M(R)$ is the maximum of the absolute value of the integrand on the u per semicircle of radius $R$. Now $\lim _{R \rightarrow \infty}\left(M(R) R^{\beta_{1}+\cdots+\beta_{n-1}}\right)=1$, so $R M(R) R^{1-\beta_{1}-\cdots-\beta_{n-1}}\left(M(R) R^{\beta_{1}+\cdots+\beta_{n-1}}\right) \longrightarrow 0$, and so $\left|f\left(R e^{i \theta}\right)-f(R)\right| \rightarrow 0$ uniformly $\theta$ as $R \rightarrow \infty$. Since $f(R) \rightarrow w_{n}$, we conclude that $f(z) \rightarrow w_{n}$ as $z \rightarrow \infty$.
12. (a) Follow the outlined steps to show that for $\operatorname{Im} z>0$, a real, and $0 \leq \alpha \leq$
$$
(z-a)^{\frac{\alpha}{\pi}}=(-1)^{\frac{\alpha}{\pi}}(a-z)^{\frac{\alpha}{\pi}}, \text { all branches principal. }
$$

Fix $z$ with $\operatorname{Im} z>0$. We must prove $e^{\frac{\alpha}{\pi} \log (z-a)}=e^{i \alpha} e^{\frac{\alpha}{\pi} \log (a-z)}$, and it will sufficient to prove $\log (z-a)=\log (a-z)+i \pi$, or that $\operatorname{Arg}(z-a)=\operatorname{Arg}(a-z)+$ We know that for each $z, \operatorname{Arg}(z-a)=\operatorname{Arg}(a-z) \pm \pi$. However, $0<\operatorname{Arg}(z-a)<$ and $-\pi<\operatorname{Arg}(a-z)<0$, so $0<\operatorname{Arg}(z-a)-\operatorname{Arg}(a-z)<2 \pi$ and we must $u$ the plus sign. This proves (14).
(b) Follow the outlined steps to prove (6). Use part (a) to show $(z-a)^{\frac{\alpha}{\pi}}(z+a)^{\frac{\alpha}{\pi}} (-1)^{\frac{\alpha}{\pi}}(a-z)^{\frac{\alpha}{\pi}}(a+z)^{\frac{\alpha}{\pi}}$, and so we must show $(a-z)^{\frac{\alpha}{\pi}}(a+z)^{\frac{\alpha}{\pi}}=\left(a^{2}-z^{2}\right)^{\frac{\alpha}{\pi}}$. is sufficient to show that $\operatorname{Arg}(a-z)+\operatorname{Arg}(a+z)=\operatorname{Arg}\left(a^{2}-z^{2}\right)$. We know the for each $z, \operatorname{Arg}(a-z)+\operatorname{Arg}(a+z)=\operatorname{Arg}\left(a^{2}-z^{2}\right)+2 k \pi$, where $k$ is 0,1 , -1 . However $-\pi<\operatorname{Arg}(a-z)<0$ and $0<\operatorname{Arg}(a+z)<\pi$, so the left side is $(-\pi, \pi)$, and hence $k=0$.
13. In this exercise we prove that for $\operatorname{Im} \zeta<0$,
$$
\zeta\left(1-\frac{1}{\zeta^{2}}\right)^{\frac{1}{2}}=-i\left(1-\zeta^{2}\right)^{\frac{1}{2}}, \text { all branches principal. }
$$

Expanding in terms of the logarithm, it will be sufficient to show that $\operatorname{Arg} \zeta \frac{1}{2} \operatorname{Arg}\left(1-\frac{1}{\zeta^{2}}\right)=-\frac{\pi}{2}+\frac{1}{2} \operatorname{Arg}\left(1-\zeta^{2}\right)$, or that $h(\zeta)=2 \operatorname{Arg} \zeta+\operatorname{Arg}\left(1-\frac{1}{\zeta^{2}}\right)+\pi \operatorname{Arg}\left(1-\zeta^{2}\right)=0$. We know that $h(\zeta)=2 k \pi$, where $k$ is an integer that may deper on $\zeta$. However, since the images under $w_{1}=\left(1-\frac{1}{\zeta^{2}}\right)$ and $w_{2}=\left(1-\zeta^{2}\right)$ of t lower half-plane $\operatorname{Im} \zeta<0$ do not include the negative real axis, $h(\zeta)$ is continuou A continuous function which takes on discrete values must be constant (Lemma Section 5.7), and so $k$ cannot depend on $\zeta$. Pick $\zeta=-i$ and conclude $k=0$.
14. Project Problem: Channel width formula. We can write the logarith as a Schwarz-Christoffel transformation $\log z=\int \frac{d z}{z}$, where there is one verte $x_{1}=0, \theta_{1}=\pi, w_{1}=\infty$. The selection of $\theta_{1}=\pi$ forces a semi-infinite channel the left half-plane (in this case the channel is also infinite into the right half-plane For points $\Delta x$ on the real axis near $x_{1}=0$, we have $f(\Delta x)-f(-\Delta x)=-i$ and so the channel width is $\pi$. We now see that this type of behavior is exhibit wherever we set an angle $\theta_{j_{0}}=\pi$.
(a) Take a Schwarz-Christoffel transformation where a particular $\theta_{j_{0}}=\pi$, and oth $\theta_{j} \leq \pi$. Then
$$
f(z)=A \int \frac{d z}{\left(z-x_{1}\right)^{\frac{\theta_{1}}{\pi}} \cdots\left(z-x_{j_{0}}\right) \cdots\left(z-x_{n-1}\right)^{\frac{\theta_{n-1}}{\pi}}}+B .
$$

Argue briefly that $\lim _{z \rightarrow x_{10}} f(z)=\infty$ by considering the fact that each factor in $t$ integrand is approximately constant near $x_{j_{0}}$ except $\frac{1}{z-x_{j_{0}}}$ which has a diverge integral.
(b) Define the channel separation complex number $s$ by $s=\lim _{r 10}\left(f\left(x_{j_{0}}+r\right)\right.$

---

<!-- Page 50 -->

Left margin note (page 50)

434
Chapter 6 Co
6.5 Green'

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-50_460_542_1377_93.jpg)

Figure 1 A Diric in a simply conne

Right margin note (page 50)

esents $r$ and
1) $\frac{9 n-1}{7}$
pped.
d the
hese
blem.
th $\Gamma$.
chlet
n by mula For as a a on al to only ction erive lving gion ed in ts of ught 11 be tools

++++

nformal Mappings

$\left.f\left(x_{j 0}-r\right)\right)$. A typical case is shown in Figure 23, and its absolute value $|s|$ repr the channel width. Parametrize the upper semicircle from $x_{j_{0}}-r$ to $x_{j_{0}}+$ get
$$
\begin{aligned}
s & =A \lim _{r 10} \int_{0}^{\pi} \frac{-i r e^{i(\pi-t)} d t}{\left(x_{j_{0}}+r e^{i(\pi-t)}-x_{1}\right)^{\frac{\theta_{1}}{\pi}} \cdots\left(r e^{i(\pi-t)}\right) \cdots\left(x_{j_{0}}+r e^{i(\pi-t)}-x_{n}\right.} \\
& =\frac{-i A \pi}{\left(x_{j_{0}}-x_{1}\right)^{\frac{\theta_{1}}{\pi}} \cdots\left(x_{j_{0}}-x_{n-1}\right)^{\frac{\theta_{n-1}}{\pi}}},
\end{aligned}
$$
where in the denominator of the final expression, the term $x_{j_{0}}-x_{j_{0}}$ is ski Conclude that the channel width is
$$
|s|=\frac{|A| \pi}{\left|x_{j_{0}}-x_{1}\right|^{\frac{\theta_{1}}{\pi}} \cdots\left|x_{j_{0}}-x_{n-1}\right|^{\frac{\theta_{n-1}}{\pi}}}
$$
where again $\left|x_{j_{0}}-x_{j_{0}}\right|$ is skipped.
(c) Verify the channel width formula for the $L$-shaped region of Example 4 an doubly slit plane of Example 5.
Functions
What is a Green's function and what can it do for us? To answer questions, let us review a few facts about the solution of a Dirichlet prob Suppose that $\Omega$ is a simply connected region bounded by a simple pa Let $f$ be a piecewise continuous function on $\Gamma$ and consider the Diri problem (Figure 1)
$$
\begin{array}{c}
\Delta u(z)=0 \quad \text { for all } z \text { in } \Omega \\
u(\zeta)=f(\zeta) \quad \text { for all } \zeta \text { on } \Gamma
\end{array}
$$

If $\Omega$ is the unit disk $D$, then the solution of the problem (1)-(2) is give the Poisson formula (see (12), Section 3.8). The importance of this for is that it depends only on the region and the boundary function $f$. an arbitrary simply connected region $\Omega$, we saw in Section 6.1 that, consequence of the Riemann mapping theorem and the Poisson formul the disk, the Dirichlet problem (1)-(2) on $\Omega$ has a solution. It is natur ask whether we can express this solution as an integral that depends on the region $\Omega$ and works for any piecewise continuous boundary fun $f$. Amazingly, the answer is affirmative! Our goal in this section is to d a formula that expresses the solution as a path integral over $\Gamma$, invo the boundary function $f$ and the so-called Green's function of the re $\Omega$, which is a function that depends only on $\Omega$. The formula is name honor of its discoverer, one of the leading mathematicians and physicis the nineteenth century, George Green (1793-1841), who was a self-ta mathematician from England. The importance of Green's functions wi appreciated in later sections, where they will be presented as the only

---

<!-- Page 51 -->

Left margin note (page 51)

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-51_488_489_1764_55.jpg)

Figure 2 The mappir analytic and one-to-one it maps boundary to ary and preserves angle

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-51_484_1117_1244_709.jpg)

Figure 3 For a circl tered at the origin, the 1 derivative is the radial tive.

Right margin note (page 51)

435
m's
the
mic
ex-
ling
and
ose
t $\phi$
ion
nts
or
the
dot
nal
sy
cle
3):
cle
ive
tes

++++

Section 6.5 Green's Functions

for solving boundary value problems on certain regions involving Poiss equation and other important equations in applied mathematics.

If you recall in Section 3.8, we used a change of variables to derive Poisson integral on the unit disk from the mean value property of harm functions. We will take the same approach on $\Omega$, and so we begin by plaining the change of variables that is a key to deriving and understand Green's functions.

Suppose that $\Omega$ and $\Omega^{\prime}$ are two regions bounded by simple paths $\Gamma \Gamma^{\prime}$. Let $\phi$ be a one-to-one analytic map of $\Omega$ onto $\Omega^{\prime}$. We will further supp that $\phi$ is analytic and one-to-one on $\Gamma$. It follows from Section 6.1 tha maps boundary to boundary. Suppose that $F$ is a real differentiable funct of two variables defined on $\Gamma^{\prime}$. We will think of complex numbers as poi in the complex plane, and consider $F(z)$ for $z$ on $\Gamma^{\prime}$. We will write $\frac{\partial F}{\partial n_{\Gamma^{\prime}}}$ simply $\frac{\partial F}{\partial n}$ to denote the directional derivative of $F$ in the direction of outward unit normal vector to the path $\Gamma^{\prime}$. By definition, this is the product of the gradient of $F, \nabla F=\left(F_{x}, F_{y}\right)$, with the outward unit norr vector $n_{\Gamma}^{\prime}$. Thus
$$
\frac{\partial F}{\partial n_{\Gamma^{\prime}}}=\nabla F \cdot n_{\Gamma^{\prime}}
$$
where each expression is computed at a given point on $\Gamma^{\prime}$ (Figure 2).

Although normal derivatives are tedious to compute in general, they are ea to express in some important special cases. For example, if $\Gamma^{\prime}$ is any cir centered at the origin, then $\frac{\partial F}{\partial n_{\Gamma^{\prime}}}$ is just the radial derivative of $F$ (Figure
$$
\frac{\partial F}{\partial n_{\Gamma^{\prime}}}=\frac{\partial F}{\partial r} .
$$

If $F(z)=\ln |z|$ and $\Gamma^{\prime}$ is the unit circle, then for all points on the unit cir
$$
\left.\frac{\partial F}{\partial n_{\Gamma^{\prime}}}\right|_{|z|=1}=\left.\frac{\partial}{\partial r} \ln r\right|_{r=1}=\left.\frac{1}{r}\right|_{r=1}=1 .
$$

Our goal is to relate the normal derivative of $F$ on $\Gamma^{\prime}$ to the normal derivat of $F(\phi(z))$ on $\Gamma$. Recall that if $\phi$ is analytic and $\left|\phi^{\prime}(z)\right| \neq 0$, then $\phi$ rota

---

<!-- Page 52 -->

Left margin note (page 52)

436
Chapter 6
C
$\mathbf{L}$
CHA
VA]

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-52_524_1097_1892_786.jpg)

Figure 4 If $\phi$ is one-to-one, the analytic.

Right margin note (page 52)

nap a scale ate of curve, ive of This ige of
chain ive it The ormal esired idary hould roof.
y connd its nuous ten
etrized
e 4 for

$\Omega$ and
ne open

++++

onformal Mappings

a path through $z$ by a fixed angle and scales by $\left|\phi^{\prime}(z)\right|$. So $\phi$ will 1 normal vector to $\Gamma$ at $\zeta$ to a normal vector to $\Gamma^{\prime}$ at $\phi(\zeta)$, and it will its modulus by $\left|\phi^{\prime}(\zeta)\right|$. Since the normal derivative measures the $r$, change of the function in the direction of the normal vector to the thinking as we do with the chain rule, we expect the normal derivat $F \circ \phi$ at $\zeta$ to equal the normal derivative of $F$ at $\phi(\zeta)$ times $\left|\phi^{\prime}(\zeta)\right|$. expectation turns out to be correct, and we have the following chan variables formula:
$$
\frac{\partial(F \circ \phi)}{\partial n_{\Gamma}}(\zeta)=\left|\phi^{\prime}(\zeta)\right| \frac{\partial F}{\partial n_{\Gamma^{\prime}}}(\phi(\zeta)) .
$$

The proof of (3) is a nice application of conformal properties, the rule in two dimensions, and the Cauchy-Riemann equations. We gi at the end of this section in order not to interrupt the presentation. importance of this formula is that it incorporates the effect of the confe properties of analytic functions. Let us move a step closer to the de formula for Green's functions and derive a formula that uses the bour

EMMA 1 NGE OF RIABLES values of $u$ to reproduce its value at a special point inside $\Omega$. You sl note the role of the mean value property of harmonic functions in the F
Suppose that $w=\phi(z)$ is a one-to-one analytic mapping of a simpl nected region $\Omega$ and its boundary $\Gamma$ onto the open unit disk $D$ a boundary $C$. Let $u$ be a function harmonic on $\Omega$ and piecewise conti on the boundary $\Gamma$. Let $z_{0}$ in $\Omega$ be the point such that $\phi\left(z_{0}\right)=0$. Th
$$
u\left(z_{0}\right)=\frac{1}{2 \pi} \int_{\Gamma} u(\zeta) \frac{\partial \ln |\phi(\zeta)|}{\partial n} d s
$$
where $d s=|d \zeta|$ is the element of arc length on $\Gamma$. Hence if $\Gamma$ is param by $\gamma(t), a \leq t \leq b$, then $d s=\left|\gamma^{\prime}(t)\right| d t$.
Proof We will apply (3), but first we note one useful result. (Refer to Figur help with the notation.)

analytic and
$\phi^{-1}$ is also

The function $\phi^{-1}$ is analytic from the closed unit disk (in the $w$-plane) ontc its boundary (in the $z$-plane). So the function $u\left(\phi^{-1}(w)\right)$ is harmonic on $t$ l

---

<!-- Page 53 -->

Section 6.5 Green's Functions
437

unit disk, being the composition of a harmonic function $u$ with an analytic function $\phi^{-1}$ (Theorem 3, Section 2.5). Moreover, $u\left(\phi^{-1}(w)\right)$ is piecewise continuous on $C$. Thus, by the mean value property of harmonic functions (Corollary 7, Section 3.8), we have
$$
\frac{1}{2 \pi} \int_{0}^{2 \pi} u\left(\phi^{-1}\left(e^{i t}\right)\right) d t=u\left(\phi^{-1}(0)\right)=u\left(z_{0}\right)
$$

Our goal now is to show that the integral in (4) is precisely the integral that we just evaluated in (5). Parametrize $C$ by $e^{i t}, 0 \leq t \leq 2 \pi$. Then $\Gamma$ will be parametrized by $\phi^{-1}\left(e^{i t}\right), 0 \leq t \leq 2 \pi$. The element of arc length on $\Gamma$ is
$$
\left|\frac{d}{d t} \phi^{-1}\left(e^{i t}\right)\right| d t=\left|\frac{i e^{i t}}{\phi^{\prime}\left(\phi^{-1}\left(e^{i t}\right)\right)}\right| d t=\frac{1}{\left|\phi^{\prime}\left(\phi^{-1}\left(e^{i t}\right)\right)\right|} d t
$$

Using (3) to perform the change of variables $\zeta=\phi^{-1}\left(e^{i t}\right)$, we transform the integral in (4) into
$$
\begin{array}{c}
\left.\frac{1}{2 \pi} \int_{0}^{2 \pi} u\left(\phi^{-1}\left(e^{i t}\right)\right) \frac{\partial \ln |w|}{\partial r}\right|_{w=e^{i t}}\left|\phi^{\prime}\left(\phi^{-1}\left(e^{i t}\right)\right)\right| \frac{d t}{\left|\phi^{\prime}\left(\phi^{-1}\left(e^{i t}\right)\right)\right|} \\
=\frac{1}{2 \pi} \int_{0}^{2 \pi} u\left(\phi^{-1}\left(e^{i t}\right)\right) d t=u\left(z_{0}\right)
\end{array}
$$
by (5).
Let us note the following interesting property of the logarithm that we derived in the preceding proof: If $\phi$ is a conformal mapping of $\Gamma$ and its interior onto the unit circle $C$ and its interior, then for a point $\zeta$ on $\Gamma$ we have
$$
\left.\frac{\partial \ln |\phi(z)|}{\partial n_{\Gamma}}\right|_{z=\zeta}=\left|\phi^{\prime}(\zeta)\right|
$$

By composing $\phi$ with an appropriate linear fractional transformation, we will be able to reproduce the values of $u$ at any point inside $\Omega$, not just $z_{0}=\phi^{-1}(0)$ as shown in (4). Let $z$ be in $\Omega$ and think of $\phi(z)$ as a fixed point inside the unit disk in the $w$-plane. Consider the linear fractional transformation
$$
\tau_{z}(w)=\frac{w-\phi(z)}{1-\overline{\phi(z)} w}
$$

It is one-to-one and maps the unit disk onto the unit disk and the unit circle onto the unit circle (Example 3, Section 3.7). Let us compose $\tau_{z}$ with $\phi$ and define
$$
\Phi(z, \zeta)=\tau_{z}(\phi(\zeta))=\frac{\phi(\zeta)-\phi(z)}{1-\overline{\phi(z)} \phi(\zeta)}, \quad z, \zeta \text { in } \Omega
$$

---

<!-- Page 54 -->

Left margin note (page 54)

438
Chapter 6
C

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-54_554_1119_333_736.jpg)

Figure 5 We think as a function of on $\zeta$ in $\Omega$, for fixed $z$ a function of $\zeta, \Phi(2$ alytic and one-to-o onto the unit disk a to 0 ; that is, $\Phi(z$,

THE
G
FUN

Right margin note (page 54)

as a
naps

ue of
$\phi$ is a and its inuous $\Omega$, we
nental lace's isson
e, forimply is. Of mapreen's these oisson
al and

++++

onformal Mappings

This is a function of two variables $z$ and $\zeta$, but we will often think of it function of $\zeta$ alone for a fixed value of $z$. As a function of $\zeta$, it clearly $z$ to 0 ; that is, $\Phi(z, z)=0$ (Figure 5).
of $\Phi(z, \zeta)$ e variable in $\Omega$. As , $\zeta$ ) is anne from $\Omega$ nd takes $z$ ) $=0$.

OREM 1 REEN'S CTIONS

Using $\Phi(z, \zeta)$ in place of $\phi(\zeta)$ in (4), we are able to reproduce the val $u$ at any point $z$ in $\Omega$.
Suppose that $\Omega$ is a simply connected region with boundary $\Gamma$, and one-to-one analytic function on $\Omega$ and its boundary onto the unit disk boundary. Let $u(z)$ be a function harmonic on $\Omega$ and piecewise cont on $\Gamma$. For $z$ and $\zeta$ in $\Omega$, let $\Phi(z, \zeta)$ be as in (8). Then, for any $z$ in have
(9)
$$
u(z)=\frac{1}{2 \pi} \int_{\Gamma} u(\zeta) \frac{\partial}{\partial n} \ln |\Phi(z, \zeta)| d s
$$
where $d s=|d \zeta|$ is the element of arc length on $\Gamma$.
The function
$$
G(z, \zeta)=\ln |\Phi(z, \zeta)|=\ln \left|\frac{\phi(\zeta)-\phi(z)}{1-\overline{\phi(z)} \phi(\zeta)}\right|, \quad z, \zeta \text { in } \Omega
$$
is called the Green's function for the region $\Omega$. It plays a fundan role in the solution of important partial differential equations (Lap equation and Poisson's equation). Formula (9) is a generalized Po integral formula for the simply connected region $\Omega$.

Like the Poisson formulas on the disk and in the upper half-plan mula (9) can be used to solve a general Dirichlet problem in a $s$ connected region $\Omega$, where the boundary data is piecewise continuou course, this solution depends on the explicit formula for the conformal ping of $\Omega$ onto the unit disk. Once this mapping is determined, G functions can be used to solve the Dirichlet problem. We illustrate ideas with several examples and show how we can recapture the P formulas from Green's functions.

We will often write the Green's function $G(z, \zeta)$ in terms of the re

---

<!-- Page 55 -->

Section 6.5 Green's Functions
439

imaginary parts of $z=x+i y$ and $\zeta=s+i t$. We will also write the Green's function using polar coordinates of $z$ and $\zeta$, where $z=r e^{i \theta}$ and $\zeta=\rho e^{i \eta}$

EXAMPLE 1 Green's function and Poisson formula for the disk
(a) Show that the Green's function for the unit disk in polar coordinates is
$$
G(z, \zeta)=\ln \left|\frac{\rho e^{i \eta}-r e^{i \theta}}{1-r \rho e^{i(\eta-\theta)}}\right|, \quad \text { for } z=r e^{i \theta} \text { and } \zeta=\rho e^{i \eta}
$$

As a specific illustration, we fix $z=\frac{2}{5}$ in the unit disk, and plot in Figure 6 the function $\zeta \mapsto G\left(\frac{2}{5}, \zeta\right)$, for $\zeta$ in the unit disk. This is Green's function for the unit disk anchored at a specific point $z=\frac{2}{5}$ in the unit disk.
(b) Derive the Poisson integral formula for the unit disk.

Solution (a) We will use (10). In this case, the conformal mapping $\phi(z)$ of the unit disk onto itself is simply $\phi(z)=z$, and so
$$
G(z, \zeta)=\ln |\Phi(z, \zeta)|=\ln \left|\frac{\phi(\zeta)-\phi(z)}{1-\overline{\phi(z)} \phi(\zeta)}\right|=\ln \left|\frac{\zeta-z}{1-\bar{z} \zeta}\right|
$$
and (11) follows upon replacing $z$ by $r e^{i \theta}$ and $\zeta$ by $\rho e^{i \eta}$.
(b) To derive the Poisson integral formula for the unit disk, we must write out (9) when $\Gamma$ is the unit circle. In this case, $d s=d \eta$, where $0 \leq \eta \leq 2 \pi$. Using (6), we find that
$$
\begin{aligned}
\frac{\partial}{\partial n} \ln \left|\frac{\zeta-z}{1-\bar{z} \zeta}\right|_{|\zeta|=1} & =\left|\frac{d}{d \zeta}\left(\frac{\zeta-z}{1-\bar{z} \zeta}\right)\right|_{\zeta=e^{i \eta}}=\left|\frac{1-|z|^{2}}{(1-\bar{z} \zeta)^{2}}\right|_{\zeta=e^{i \eta}} \\
& =\frac{1-r^{2}}{\left|1-r e^{-i \theta} e^{i \eta}\right|^{2}}=\frac{1-r^{2}}{1-2 r \cos (\theta-\eta)+r^{2}}
\end{aligned}
$$

Plugging into (9), we find, for $z=r e^{i \theta}$ with $0 \leq r<1$,
$$
u(z)=\frac{1-r^{2}}{2 \pi} \int_{0}^{2 \pi} \frac{u\left(e^{i \eta}\right)}{1-2 r \cos (\theta-\eta)+r^{2}} d \eta
$$
which is Poisson's formula on the unit disk.
Before we move to our next example, let us understand the role of $\Phi(z, \zeta)$ in (8). Since $\Phi$ is the composition of two conformal mappings, it is itself a conformal mapping of $\Omega$ onto the unit disk, and from (8) we have $\Phi(z, z)=$ 0 . By the Riemann mapping theorem, $\Phi(z, \zeta)$ is uniquely determined by these properties, up to a unimodular multiplicative constant. In particular $|\Phi(z, \zeta)|$ is uniquely determined and so is the Green's function for the region. (The uniqueness part in the Riemann mapping theorem is not difficult to prove, and so we are not appealing to a deep result here.) Consider, for example, the linear fractional transformation
$$
\tau(\zeta)=\frac{z-\zeta}{\bar{z}-\zeta}
$$

---

<!-- Page 56 -->

Left margin note (page 56)

440
Chapter 6

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-56_319_529_797_106.jpg)

Figure 7 Green $G(1+i, \zeta)$ for the plane anchored a Note that $G(1$ for all $\zeta$ on the b $G(1+i, \zeta)$ has a $\zeta=1+i$.

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-56_508_543_1954_108.jpg)

Figure 8 for Ex

Right margin note (page 56)

$z$ onto
t disk,
half-
$>0$ ).
plot in Green's upper
$\boldsymbol{\Phi}(z, \zeta) \mid$
ute the clearly
sing the -to-one

++++

Conformal Mappings

where $z$ is in the upper half-plane. If $\zeta$ is real so that $\bar{\zeta}=\zeta$, then
$$
\left|\frac{z-\zeta}{\bar{z}-\zeta}\right|=\left|\frac{z-\zeta}{\bar{z}-\bar{\zeta}}\right|=\frac{|z-\zeta|}{|\overline{z-\zeta}|}=1
$$

Thus $\tau(\zeta)$ maps the real line onto the unit circle and since it takes the origin, it follows that $\tau$ maps the upper half-plane onto the uni and thus $\tau(\zeta)=\Phi(z, \zeta)$ for the upper half-plane.

EXAMPLE 2 Green's function and Poisson's formula in the uppe plane (a) Show that the Green's function for the upper half-plane is
$$
G(z, \zeta)=\frac{1}{2} \ln \frac{(x-s)^{2}+(y-t)^{2}}{(x-s)^{2}+(y+t)^{2}}, \quad \text { for } z=x+i y, \zeta=s+i t(y, t
$$

As a specific illustration, we fix $z=1+i$ in the upper half-plane, and Figure 7 the function $\zeta \mapsto G(1+i, \zeta)$, for $\zeta$ in the upper half-plane. This is function for the upper half-plane anchored at a specific point $z=1+i$ in the half-plane.

1's function upper half$\mathrm{t} z=1+i$. $-i, \zeta)=0$ oundary and ingularity at

ample 3.
(b) Derive the Poisson integral formula for the upper half-plane.

Solution According to (10), Green's function for the upper half-plane is $\ln$ where $\Phi(z, \zeta)$ is given by (12). Thus,
$$
G(z, \zeta)=\ln \left|\frac{z-\zeta}{\bar{z}-\zeta}\right|=\frac{1}{2} \ln \frac{|z-\zeta|^{2}}{|\bar{z}-\zeta|^{2}}=\frac{1}{2} \ln \frac{(x-s)^{2}+(y-t)^{2}}{(x-s)^{2}+(-y-t)^{2}}
$$
which is equivalent to (13).
(b) To derive Poisson's integral formula in the upper half-plane we comp normal derivative in (9). If $\Gamma$ ' is the real $s$-axis, then the normal derivative is the derivative in the negative direction along the imaginary $t$-axis. Thus,
$$
\frac{\partial}{\partial n} G(z, \zeta)=-\frac{1}{2} \frac{\partial}{\partial t} \ln \frac{(x-s)^{2}+(y-t)^{2}}{(x-s)^{2}+(y+t)^{2}}
$$

A straightforward calculation of the derivative, then setting $t=0$, yields
$$
\frac{\partial}{\partial n} G(z, \zeta)=\frac{2 y}{(x-s)^{2}+y^{2}}
$$

Plugging into (9) yields
$$
u(z)=\frac{y}{\pi} \int_{-\infty}^{\infty} \frac{u(s)}{(x-s)^{2}+y^{2}} d s \quad(z=x+i y)
$$
which is Poisson's formula for the upper half-plane.
We give one more example of a Green's function.

EXAMPLE 3 Green's function for a semi-infinite vertical strip
We can map the strip $\Omega$ in Figure 8 conformally onto the upper half-plane us mapping $w=\sin z$. Composing the function (12) with this, we obtain a one

---

<!-- Page 57 -->

Left margin note (page 57)

THEORE PROPERTIES GREE FUNCTIC

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-57_427_1842_1086_41.jpg)

Figure 9 A Green's func function, $u_{1}(\zeta)$, such that has a singularity at $z_{0}$ like

++++

Section 6.5 Green's Functions
441

analytic mapping of $\Omega$ onto the unit disk, taking $z$ in $\Omega$ onto the origin. Thus the Green's function for $\Omega$ is
$$
G(z, \zeta)=\ln \left|\frac{\sin z-\sin \zeta}{\overline{\sin z}-\sin \zeta}\right|
$$

We prove next some interesting properties of Green's functions.

M2

Suppose that $\Omega$ is a simply connected region with boundary $\Gamma$, and let $\phi$,

OF $\Phi(z, \zeta)$, and $G(z, \zeta)$ be as in Theorem 1. Then the Green's function $G(z, \zeta)$

N'S has the following properties:

ONS
(i) $G(z, \zeta) \leq 0$ for all $z$ and $\zeta$ in $\Omega$;
(ii) $G(z, \zeta)=0$ for all $z$ in $\Omega$ and $\zeta$ on $\Gamma$;
(iii) $G(z, \zeta)=G(\zeta, z)$ for all $z$ and $\zeta$ in $\Omega$ (symmetric property);
(iv) for each $z$ in $\Omega$, there is a function $\zeta \mapsto u_{1}(z, \zeta)$ such that $u_{1}(z, \zeta)$ is harmonic for all $\zeta$ in $\Omega, u_{1}(z, \zeta)=-\ln |z-\zeta|$ for all $\zeta$ on the boundary $\Gamma$, and $G(z, \zeta)=u_{1}(z, \zeta)+\ln |z-\zeta|$ for all $\zeta \neq z$ in $\Omega$.
You should verify properties (i) and (ii) on the graphs of the Green's functions in Figures 6 and 7. Before we prove the theorem, we illustrate the properties in Figure 9 for a typical case where $\Omega$ is the upper half-plane and Green's function is anchored at $z=1+i$.
tion $G\left(z_{0}, \zeta\right)$ anchored at $z_{0}=1+i$ is the sum of a logarithm, $\ln \left|z_{0}-\zeta\right|$, and a harmonic $u_{1}(\zeta)=-\ln \left|z_{0}-\zeta\right|$ on the boundary. As a result, $G\left(z_{0}, \zeta\right)$ vanishes on the boundary and $\ln \left|z_{0}-\zeta\right|$.

Proof Fix $z$ in $\Omega$. From the definition of $\phi$ and $\Phi$ (see (7) and (8)), we have that $\Phi(z, \zeta)$ is in the open unit disk $D$ (that is, $|\Phi(z, \zeta)|<1$ ) for all $\zeta$ in $\Omega$ and $\Phi(z, \zeta)$ is on the unit circle $C$ (that is, $|\Phi(z, \zeta)|=1$ ) for all $\zeta$ on $\Gamma$. This clearly proves (i) and (ii), because $\ln |x|<0$ if $|x|<1$ and $\ln |x|=0$ if $|x|=1$. For (iii), we have
$$
G(z, \zeta)=\ln \left|\frac{\phi(\zeta)-\phi(z)}{1-\overline{\phi(z)} \phi(\zeta)}\right|=\ln \left|\frac{\phi(z)-\phi(\zeta)}{1-\overline{\phi(z)} \phi(\zeta)}\right|=\ln \left|\frac{\phi(\zeta)-\phi(z)}{1-\overline{\phi(\zeta)} \phi(z)}\right|=G(\zeta, z) .
$$

To prove (iv), fix $z$ in $\Omega$ and consider
$$
\psi(z, \zeta)=\frac{\phi(\zeta)-\phi(z)}{\zeta-z} \frac{1}{1-\overline{\phi(z)} \phi(\zeta)} \quad(\zeta \neq z \text { in } \Omega)
$$

---

<!-- Page 58 -->

Left margin note (page 58)

442
Chapter 6
C

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-58_500_529_1600_108.jpg)

Figure 10

Right margin note (page 58)

hes $z$ ?
and so n 4.6).
$z, \zeta) \mid ;$
$\zeta \mid$.
ndary,
oblem ion is (iv) is sed to that
$\gamma^{\prime}(t)=$ utward /2 and
s write ives by
larly,

++++

onformal Mappings

Clearly, $\psi(z, \zeta)$ is analytic for all $\zeta \neq z$ in $\Omega$. What happens as $\zeta$ approad We have
$$
\lim _{\zeta \rightarrow z} \psi(z, \zeta)=\lim _{\zeta \rightarrow z} \frac{\phi(\zeta)-\phi(z)}{\zeta-z} \frac{1}{1-\overline{\phi(z)} \phi(\zeta)}=\frac{\phi^{\prime}(z)}{1-|\phi(z)|^{2}},
$$
which is finite because $|\phi(z)|<1$ and nonzero because $\phi$ is one-to-one $\phi^{\prime}(z) \neq 0$. Hence $\psi(z, \zeta)$ has a removable singularity at $z$ (Theorem 6, Sectio By defining $\psi$ at $\zeta=z$ to be
$$
\psi(z, z)=\frac{\phi^{\prime}(z)}{1-|\phi(z)|^{2}}
$$
$\psi(z, \zeta)$ becomes analytic and nonzero for all $\zeta$ in $\Omega$. Set $u_{1}(z, \zeta)=\ln \mid \psi($ then $u_{1}$ is harmonic for all $\zeta$ in $\Omega$. But for $\zeta \neq z$
$$
\left.u_{1}(z, \zeta)=\ln |\psi(z, \zeta)|=\ln \left|\frac{\phi(\zeta)-\phi(z)}{1-\overline{\phi(z)} \phi(\zeta)}\right|-\ln |\zeta-z|=G(z, \zeta)-\ln \right\rvert\, z-
$$

Also, $u_{1}(z, \zeta)=-\ln |z-\zeta|$ on the boundary because $G(z, \zeta)=0$ on the bou and so (iv) holds.

Because the function $\zeta \mapsto u_{1}(z, \zeta)$ is the solution of a Dirichlet pr in $\Omega$ with boundary values $-\ln |z-\zeta|$, if $\Omega$ is bounded, this solut unique. Thus the representation of Green's function in Theorem 2 unique when $\Omega$ is bounded. Property (iv) in Theorem 2 can be us define the Green's function of a domain. That is, any function $G(z, \zeta$ satisfies (iv) also satisfies (9).
Appendix: Proof of the change of variables formula (3)
Suppose that $\gamma(t)=x(t)+i y(t)$ is a parametrization of a smooth path with

(t) $x^{\prime}(t)+i y(t) \neq 0$. If we assume our path has a positive orientation, then an o unit normal may be obtained by rotating the tangent $\gamma^{\prime}(t)$ clockwise by $\pi$ dividing by its absolute value (Figure 10). Hence $n(t)=\frac{\gamma^{\prime}(t)}{\left\{\gamma^{\prime}(t) \mid\right.}$ or
$$
n_{\Gamma}=\frac{1}{\left|\gamma^{\prime}(t)\right|}\left(y^{\prime}(t),-x^{\prime}(t)\right)
$$

Let $\phi(z)$ be as in the text preceding (3). To simplify the notation, let $u \phi(z)=u(x, y)+i v(x, y)$, write $F$ as $F(u, v)$, and denote partial derivat subscripts. So
$$
(F \circ \phi)_{x}=\frac{\partial}{\partial x} F(u(x, y), v(x, y))=F_{u} u_{x}+F_{v} v_{x}
$$
where the last equality follows from the chain rule in two dimensions. Simi
$$
(F \circ \phi)_{y}=\frac{\partial}{\partial y} F(u(x, y), v(x, y))=F_{u} u_{y}+F_{v} v_{y}
$$

---

<!-- Page 59 -->

Left margin note (page 59)

1.

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-59_487_467_1934_48.jpg)

Figure 11

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-59_491_526_1932_674.jpg)
![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-59_491_538_1934_1361.jpg)

Right margin note (page 59)

$$
\dddot{H}
$$
So

II
ப்

++++

Section 6.5 Green's Functions

Using the definition of the normal derivative, (14), (15), and (16), we get
$$
\begin{aligned}
\frac{\partial}{\partial n_{\Gamma}} F \circ \phi & =\nabla(F \circ \phi) \cdot n_{\Gamma}=\frac{1}{\left|\gamma^{\prime}(t)\right|}\left((F \circ \phi)_{x},(F \circ \phi)_{y}\right) \cdot\left(y^{\prime}(t),-x^{\prime}(t)\right) \\
& =\frac{1}{\left|\gamma^{\prime}(t)\right|}\left(\left(F_{u} u_{x}+F_{v} v_{x}\right) y^{\prime}(t)-\left(F_{u} u_{y}+F_{v} v_{y}\right) x^{\prime}(t)\right)
\end{aligned}
$$

Consider now the path $\Gamma^{\prime}$, which is parametrized by
$$
\phi(\gamma(t))=u(x(t), y(t))+i v(x(t), y(t)) .
$$

Conformality ensures that the outward normal to $\phi(\gamma(t))$ is still turned clockw from the tangent; so in analogy with (14) we obtain
$$
\begin{aligned}
n_{\Gamma^{\prime}} & =\frac{1}{\left|\frac{d}{d t} \phi(\gamma(t))\right|}\left(\frac{d}{d t} v(x(t), y(t)),-\frac{d}{d t} u(x(t), y(t))\right) \\
& =\frac{1}{\left|\phi^{\prime}(\gamma(t)) \gamma^{\prime}(t)\right|}\left(v_{x} x^{\prime}(t)+v_{y} y^{\prime}(t),-u_{x} x^{\prime}(t)-u_{y} y^{\prime}(t)\right)
\end{aligned}
$$

Thus
$$
\begin{aligned}
\frac{\partial F}{\partial n_{\Gamma^{\prime}}} & =\nabla F \cdot n_{\Gamma^{\prime}} \\
& =\frac{1}{\left|\gamma^{\prime}(t)\right|\left|\phi^{\prime}(\gamma(t))\right|}\left(F_{u}, F_{v}\right) \cdot\left(v_{x} x^{\prime}(t)+v_{y} y^{\prime}(t),-u_{x} x^{\prime}(t)-u_{y} y^{\prime}(t)\right) \\
& =\frac{1}{\left|\gamma^{\prime}(t)\right|\left|\phi^{\prime}(\gamma(t))\right|}\left(F_{u}\left(v_{x} x^{\prime}(t)+v_{y} y^{\prime}(t)\right)+F_{v}\left(-u_{x} x^{\prime}(t)-u_{y} y^{\prime}(t)\right)\right)
\end{aligned}
$$

Comparing (17) and (18) and using the Cauchy-Riemann equations, $u_{x}=v_{y}, u_{y} -v_{x}$, we see that (3) holds.

Exercises 6.5
In Exercises 1-8, derive the Green's function for the region depicted in the acco panying figure (Figures 11-18).
2.

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-70_509_537_214_1407.jpg)
Figure 12
3.

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-59_491_538_1934_1361.jpg)
Figure 13

---

<!-- Page 60 -->

Left margin note (page 60)

444
Chapter 6
4.

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-60_512_526_235_94.jpg)

Figure 14
7.

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-60_482_533_851_102.jpg)

Figure 17

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-60_514_528_227_771.jpg)
![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-60_492_513_838_785.jpg)
![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-60_515_547_218_1444.jpg)
![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-60_495_549_828_1440.jpg)

Right margin note (page 60)

9.

Derive blem in
to show drant of ry data
mmetry ction to If-plane 0 and
for the ve your
oisson's

++++

Conformal Mappings
5.
8.

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-60_514_528_227_771.jpg)
Figure 15

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-60_492_513_838_785.jpg)
Figure 18
6.

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-60_515_547_218_1444.jpg)
Figure 16

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-60_495_549_828_1440.jpg)
Figure 19 for Exercise
9. Project Problem: Poisson's formula in the first quadrant. (a) the following Poisson formula in the first quadrant for the Dirichlet pro Figure 19, using Green's function:
$$
\begin{aligned}
u(x+i y)= & \frac{y}{\pi} \int_{0}^{\infty} f(s)\left(\frac{1}{(x-s)^{2}+y^{2}}-\frac{1}{(x+s)^{2}+y^{2}}\right) d s \\
& +\frac{x}{\pi} \int_{0}^{\infty} g(t)\left(\frac{1}{x^{2}+(y-t)^{2}}-\frac{1}{x^{2}+(y+t)^{2}}\right) d t
\end{aligned}
$$
(b) Consider the special case in which $g(t)=0$. Use a symmetry argument that the solution in this case is the same as the restriction to the first quad the solution of the Dirichlet problem in the upper half-plane with bounda on the real axis given by $u(s)=f(s)$ if $s>0$ and $u(s)=-f(-s)$ if $s<0$. (c) Consider the special case in Figure 19 in which $f(s)=0$. Use a sy argument to show that the solution in this case is the same as the restri the first quadrant of the solution of the Dirichlet problem in the right ha with boundary data on the imaginary axis given by $u(i t)=g(t)$ if $t> u(i t)=-g(-t)$ if $t<0$.
(d) Write your answers in (b) and (c) using the Poisson integral formula upper half-plane and the right half-plane. Then sum the solutions to rederi answer in (a).
10. Poisson's formula in a semi-infinite vertical strip. Derive P formula in the region of Example 3, using Green's function.

---

<!-- Page 61 -->

Left margin note (page 61)

6.6 Poisson's

++++

Section 6.6 Poisson's Equation and Neumann Problems
445
11. By composing $\phi_{\alpha}(z)=\frac{z-\alpha}{1-\bar{\alpha} z}$ with $\psi(z)=\frac{1-z}{1+z}$, you should be able to construct your own map $\Phi(z, \zeta)$ from the upper half-plane to the disk, satisfying $\Phi(z, z)=0$.
(a) Find the value of $\alpha$ (it will depend on $z$ ).
(b) Check that your final map $\Phi(z, \zeta)$ is the same as given in this section, $\frac{z-\zeta}{z-\zeta}$, times the unimodular constant $\frac{\mathrm{Z}-\mathrm{i}}{\mathrm{z}+\mathrm{i}}$.
Equation and Neumann Problems
In this section we use Green's functions to solve the Poisson boundary value problem on a region $\Omega$, then apply similar techniques to solve another important type of problem known as a Neumann problem. We start with the Poisson problem, which consists of the inhomogeneous Laplace's equation known as Pois

---

<!-- Page 62 -->

Left margin note (page 62)

446
Chapter 6

\section*{THE \\ SOLU? POISSON PE}

THI

IDE

Right margin note (page 62)

ms of ppose or the
te the 1)-(2),
ciple. of the em 1,
s.
finite , Secatives
nected nected s first using

++++

Conformal Mappings

We now express the solution of the Poisson problem on $\Omega$ in ter Green's functions. We use the notation of the previous section and su that $f$ and $h$ have enough smoothness and integrability properties fo formulas in Theorems 2 and 3 to hold.

OREM 2 TION OF ROBLEM

EOREM 3
GREEN'S
NTITIES

Suppose that $\Omega$ is a region with boundary $\Gamma$, and let $G(z, \zeta)$ deno Green's function for $\Omega$. If $u(z)$ is a solution of Poisson's problem ( then
$$
u(z)=\frac{1}{2 \pi} \iint_{\Omega} h(\zeta) G(z, \zeta) d A+\frac{1}{2 \pi} \int_{\Gamma} f(\zeta) \frac{\partial}{\partial n} G(z, \zeta) d s
$$
where $d A$ is the element of area and $d s$ is the element of arc length.
This form of the solution clearly illustrates the superposition prin We recognize the second term on the right side of (3) as the solution Dirichlet problem on $\Omega$ with boundary values $f$ (compare with Theore Section 6.5). Looking at the other term, we also have
$$
u(z)=\frac{1}{2 \pi} \iint_{\Omega} h(\zeta) G(z, \zeta) d A
$$
as a solution of Poisson's equation (1) with zero boundary values.
The proof of Theorem 2 is based on the following Green's identitie
Suppose that $\Omega$ is a bounded region whose boundary $\Gamma$ consists of a number of simple closed positively oriented paths (as in Theorem 6 tion 3.4). Let $u(x, y)$ and $v(x, y)$ have continuous second partial deriv on $\Omega$ and $\Gamma$. Then we have Green's first identity
$$
\iint_{\Omega}(u \Delta v+\nabla u \cdot \nabla v) d A=\int_{\Gamma} u \frac{\partial v}{\partial n} d s
$$
and Green's second identity
$$
\iint_{\Omega}(u \Delta v-v \Delta u) d A=\int_{\Gamma}\left(u \frac{\partial v}{\partial n}-v \frac{\partial u}{\partial n}\right) d s
$$

Proof We will appeal to Green's theorem from calculus. For simply conr regions, this theorem is stated in Exercise 40, Section 3.4. For multiply conr regions, the version goes as follows. Let $p(x, y)$ and $q(x, y)$ have continuou partial derivatives in $\Omega$ and on its positively oriented boundary $\Gamma$. Then, subscripts to denote partial derivatives, we have
$$
\iint_{\Omega}\left(p_{x}(x, y)+q_{y}(x, y)\right) d x d y=\int_{\Gamma}(p(x, y) d y-q(x, y) d x)
$$

---

<!-- Page 63 -->

Section 6.6 Poisson's Equation and Neumann Problems
447

Apply (7) with
$$
p(x, y)=u v_{x} \quad \text { and } \quad q(x, y)=u v_{y},
$$
and get
$$
\iint_{\Omega}\left(u\left(v_{x x}+v_{y y}\right)+\left(u_{x} v_{x}+u_{y} v_{y}\right)\right) d x d y=\int_{\Gamma} u\left(v_{x} d y-v_{y} d x\right)
$$

The integrand on the left is the same as the integrand on the left of (5). To understand the integrand on the right, let us recall that for a positively oriented curve parametrized by $\gamma(t)=x(t)+i y(t)$, the outward unit normal may be obtained by rotating the tangent $\gamma^{\prime}(t)=x^{\prime}(t)+i y^{\prime}(t)$ clockwise by $\frac{\pi}{2}$ and dividing by its absolute value. Hence
$$
n(t)=\frac{\gamma^{\prime}(t)}{i\left|\gamma^{\prime}(t)\right|}=\frac{1}{\left|\gamma^{\prime}(t)\right|}\left(y^{\prime}(t), x^{\prime}(t)\right) .
$$

Thus since the normal derivative $\frac{\partial v}{\partial n}$ is by definition the gradient of $v$ dotted with the outward unit normal vector and $d s=\left|\gamma^{\prime}(t)\right| d t$, we have
$$
\frac{\partial v}{\partial n} d s=\left(v_{x}, v_{y}\right) \cdot\left(y^{\prime}(t),-x^{\prime}(t)\right) d t=v_{x} d y-v_{y} d x
$$
which shows that the right side of (8) is the same as the right side of (5), and so (5) follows. To prove (6), we reverse the roles of $u$ and $v$ in (5) and get
$$
\iint_{\Omega}(v \Delta u+\nabla u \cdot \nabla v) d x d y=\int_{\Gamma} v \frac{\partial u}{\partial n} d s
$$

Subtracting this from (5), we get (6).

Green's formulas do not hold in general on unbounded regions. Since we will use them to prove (4), we will suppose throughout the proof that $\Omega$ is bounded. Nevertheless, formula (3) can be used on unbounded regions and its validity there can be checked on a case by case basis.

Proof of Theorem 2 Fix $z$ in $\Omega$ and let $S_{\epsilon}(z)$ denote the closed disk of radius $\epsilon>0$ around $z$ in $\Omega$, and $\Omega_{\epsilon}=\Omega \backslash S_{\epsilon}$. We are going to apply Green's second identity
$=0$
$\overrightarrow{\operatorname{Re} \zeta}$ in $\Omega_{\epsilon}$. By Theorem 2(iv) of Section 6.5, $G(z, \zeta)$ is a harmonic function of $\zeta$ for all $\zeta \neq z$ in $\Omega$. In particular, for $\zeta$ in $\Omega_{\epsilon}, \Delta G(z, \zeta)=0$, we also have $\Delta u(\zeta)=h(\zeta)$ because $u$ satisfies Poisson's equation (1). We apply Green's second identity on the region $\Omega_{\epsilon}$ whose boundary $\Gamma_{\epsilon}$ consists of $\Gamma$ and the circle $C_{\epsilon}(z)$ (Figure 3), taking $v=G(z, \zeta)$ and $u$ equal the solution of the Poisson problem, and get
$$
\begin{aligned}
-\iint_{\Omega_{e}} G(z, \zeta) h(\zeta) d A= & \int_{\Gamma}(u(\zeta) \frac{\partial G(z, \zeta)}{\partial n}-\overbrace{G(z, \zeta)}^{=0} \frac{\partial u(\zeta)}{\partial n}) d s \\
& +\int_{C_{e}(z)}\left(u(\zeta) \frac{\partial G(z, \zeta)}{\partial n}-G(z, \zeta) \frac{\partial u(\zeta)}{\partial n}\right) d s
\end{aligned}
$$

---

<!-- Page 64 -->

Left margin note (page 64)

448
Chapter 6
Conform

Right margin note (page 64)

$$
\begin{array}{l}
(z, \zeta)= \\
\text { int } M \text { in } \\
\left.\left.\frac{u}{n} \right\rvert\, \leq A\right), \\
-\zeta \mid=\epsilon,
\end{array}
$$
as $\epsilon \rightarrow 0$.
$s$.
$(z, \zeta)$ is note that eorem 5 ,
se 9).
ater secive ways ittention ar to the

++++

Mappings

because $G(z, \zeta)=0$ for $\zeta$ on $\Gamma$. We will let $\epsilon \downarrow 0$ and show that
$$
\begin{array}{l}
\iint_{\Omega_{e}} G(z, \zeta) h(\zeta) d A \rightarrow \iint_{\Omega} G(z, \zeta) h(\zeta) d A \\
\int_{C_{e}(z)} u(\zeta) \frac{\partial G(z, \zeta)}{\partial n} d s \rightarrow-2 \pi u(z) \\
\int_{C_{e}(z)} G(z, \zeta) \frac{\partial u(\zeta)}{\partial n} d s \rightarrow 0
\end{array}
$$

This will imply (3) and complete the proof. Let us start with (11). Write $G u_{1}(z, \zeta)+\ln |z-\zeta|$, where $u_{1}(z, \zeta)$ is harmonic, hence bounded by a consta some fixed disk centered at $z$. Also, $\frac{\partial u}{\partial n}$ is bounded in this fixed disk (say, $\left\lvert\, \frac{\partial}{\partial}\right.$ since $u$ has continuous partial derivatives in $\Omega$. For $\zeta$ on $C_{\epsilon}(z)$, we have $\mid z$ hence $\left|G(z, \zeta) \frac{\partial u}{\partial n}\right| \leq(M+|\ln \epsilon|) A$, and so
$$
\left|\int_{C_{\epsilon}(z)} G(z, \zeta) \frac{\partial u(\zeta)}{\partial n} d s\right| \leq(M+|\ln \epsilon|) A \int_{C_{\epsilon}(z)} d s=2 \pi \epsilon(M+|\ln \epsilon|) A \rightarrow 0
$$

To prove (10), we note that on $C_{\epsilon}(z)$,
$$
\frac{\partial G(z, \zeta)}{\partial n}=\frac{\partial}{\partial n}\left(u_{1}(z, \zeta)+\ln |z-\zeta|\right)=\frac{\partial}{\partial n} u_{1}(z, \zeta)-\frac{1}{\epsilon}
$$

Now
$$
\int_{C_{e}(z)} u(\zeta) \frac{\partial G(z, \zeta)}{\partial n} d s=\int_{C_{e}(z)} u(\zeta) \frac{\partial}{\partial n} u_{1}(z, \zeta) d s-\frac{1}{\epsilon} \int_{C_{e}(z)} u(\zeta) d
$$

The first integral on the right tends to 0 as $\epsilon \rightarrow 0$, because $u(\zeta) \frac{\partial}{\partial n} u$, bounded in $S_{\epsilon}(z)$, as in the proof of (10). To handle the second integral, i the function $I(\epsilon)=\frac{1}{\epsilon} \int_{C_{\epsilon}(z)} u(\zeta) d s=\int_{0}^{2 \pi} u\left(z+\epsilon e^{i \theta}\right) d \theta$ is continuous (Th Section 3.5). So
$$
\lim _{\epsilon \rightarrow 0} \int_{0}^{2 \pi} u\left(z+\epsilon e^{i \theta}\right) d \theta=I(0)=\int_{0}^{2 \pi} u(z) d \theta=2 \pi u(z)
$$
which completes the proof of (10). The proof of (9) is similar (see Exerci
In practice, (3) is difficult to compute in its present form. In l tions, we will relate it to generalized Fourier series and offer alternat for computing the solution of Poisson's equation. We now turn our a to a different problem, which can be solved using an approach simil one we took with Green's functions.

---

<!-- Page 65 -->

Left margin note (page 65)

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-65_448_446_460_61.jpg)

Figure 4 A Neumann lem in a region $\Omega$.

PROPOSITIO]
NORM
DERIVATIVE
HARMON
FUNCTIO

++++

Section 6.6 Poisson's Equation and Neumann Problems
449

Neumann Condition and Neumann Problems
When modeling heat problems in an insulated plate $\Omega$, where heat exchange on the boundary is prescribed, we are led to a boundary value problem that consists of Laplace's equation along with a condition that describes the values of the normal derivative on the boundary (Figure 4):
$$
\begin{array}{c}
\Delta u(z)=0 \quad \text { for all } z \text { in } \Omega \\
\frac{\partial u}{\partial n}(\zeta)=f(\zeta) \quad \text { for all } \zeta \text { on } \Gamma
\end{array}
$$

Such a problem is called a Neumann problem (after the German mathematician Carl Gottfried Neumann (1832-1925)) and sometime referred to as a Dirichlet problem of the second kind. Condition (13) is known as a Neumann condition. The normal derivative at the boundary describes the rate of exchange of heat with the surrounding medium or the flux of heat across the boundary. For example, the condition $f(\zeta)=0$ corresponds to an insulated point where there is no exchange of heat with the surrounding medium. Since $f(\zeta)$ represents the flux of heat across the boundary of $u$ and $u$ represents a steady-state temperature distribution inside $\Omega$, we would expect the total flux across the boundary to be zero; that is, $f$ cannot be arbitrary, it has to satisfy the compatibility condition
$$
\int_{\Gamma} f(\zeta) d s=0
$$

Indeed, (14) follows from the following useful property of harmonic functions, by setting $f(\zeta)=\frac{\partial u}{\partial n}$.

N 1
AL
OF
JIC

Suppose that $u$ is harmonic in a bounded region $\Omega$ and its boundary $\Gamma$. Then

NS
$$
\int_{\Gamma} \frac{\partial u}{\partial n} d s=0
$$

Proof Reversing the roles of $u$ and $v$ in Green's first identity (5) and then picking $v=1$, we get
$$
\iint_{\Omega} \Delta u d A=\int_{\Gamma} \frac{\partial u}{\partial n} d s
$$

Since $\Delta u=0$, the proposition follows.

In a Neumann problem, we are asked to find a harmonic function given the values of its normal derivative on the boundary. Such a solution is not unique, since we can add an arbitrary constant to a solution of (12)-(13) and get another solution of (12)-(13). So now we ask: Is the solution unique up

---

<!-- Page 66 -->

Left margin note (page 66)

450
Chapter 6
C

THEC
UNIQUEN
NEU
SOL

DEFIN
NE
FUN
PROPO

Right margin note (page 66)

sider rmal nonic
on the
la, so
and grate .7 in $\left(u_{y}\right)^{2}$ lying
gral, 1, we

nann
owing

$\zeta$ ) is Γ.
are ar to es of s the tates now
lue of
ithm.

++++

onformal Mappings
to an arbitrary constant? The answer is affirmative. To show this, con the difference between two solutions, which is harmonic and has zero no derivative on the boundary. As we now show, a function that is harn and has zero normal derivative is a constant.

REM 4

Suppose that $u$ is harmonic on a bounded region $\Omega$ such that $\frac{\partial u}{\partial n}=0$

ESS OF boundary $\Gamma$ of $\Omega$. Then $u$ is identically constant in $\Omega$.

MANN

Proof Suppose that $u$ is harmonic in $\Omega$ and take $u=v$ in Green's first formu

UTION that $\Delta v=0$ in $\Omega$, and get
$$
\iint_{\Omega}(\nabla u \cdot \nabla u) d A=\int_{\Gamma} u \frac{\partial u}{\partial n} d s=0
$$
because $\frac{\partial u}{\partial n}=0$ on $\Gamma$. Now the function $\nabla u \cdot \nabla u=\left(u_{x}\right)^{2}+\left(u_{y}\right)^{2}$ is continuous on $\Omega$. The only way for a nonnegative continuous function to inte to zero is to vanish identically. (This fact is proved in Lemma 1, Section 3 one dimension, but the argument works in higher dimensions.) Hence $\left(u_{x}\right)^{2}+$ is identically zero in $\Omega$, and so $u_{x}=0$ and $u_{y}=0$ identically in $\Omega$. App Theorem 1, Section 2.1, we see that $u$ is constant on $\Omega$.

In order to express the solution of the Neumann problem as an inte motivated by Green's function and the solution of the Dirichlet problen make the following definition.

ITION 1 UMANN CTIONS

Suppose that $\Omega$ is a simply connected region with boundary $\Gamma$. A Neur function $N(z, \zeta)(z, \zeta$ in $\Omega)$ for the region $\Omega$ is a function with the foll properties:
(i) for each $z$ in $\Omega, N(z, \zeta)$ is harmonic for all $\zeta \neq z$ in $\Omega$;
(ii) $\frac{\partial N}{\partial n}(z, \zeta)=C$ for all $z$ in $\Omega$ and $\zeta$ on $\Gamma$;
(iii) for each $z$ in $\Omega$, there is a function $\zeta \mapsto u_{1}(z, \zeta)$ such that $u_{1}(z$ harmonic for all $\zeta$ in $\Omega$, and $N(z, \zeta)=\ln |z-\zeta|+u_{1}(z, \zeta)$ for all $\zeta$ in

SITION 2

Parts (i) and (iii) state that Neumann functions, like Green's functions harmonic inside $\Omega$ except for a singularity at $z=\zeta$, which is simil the singularity of $\ln |z-\zeta|$. Part (ii) tells us that the boundary valu the normal derivative of the Neumann function are constant. This i counterpart of the boundary condition for a Green's function, which s that a Green's function must vanish identically on the boundary. As we show, the constant $C$ in (ii) depends on the length of the boundary $\Gamma$.
The constant $C$ in Definition 1(ii), which represents the boundary va the normal derivative of the Neumann function, is given by
(17)
$$
C=\frac{2 \pi}{L},
$$
where $L=\int_{\Gamma} d s$ is the length of $\Gamma$. If $L$ is infinite, we take $C=0$.
Proof The proof is based on the following interesting property of the logar

---

<!-- Page 67 -->

Left margin note (page 67)

THEOREM 5 SOLUTION OF NEUMANN PROBLEMS

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-67_517_495_1823_53.jpg)

Figure 5 A Neumann function for the upper half-plane, anchored at $z=1+i$.

Right margin note (page 67)

451 and □

ons
$\_\_\_\_$

nn
ms
f a
◯ ju tive by ise

++++

Section 6.6 Poisson's Equation and Neumann Problems
For any fixed $z$ inside $\Omega$, we have
$$
\int_{\Gamma} \frac{\partial}{\partial n} \ln |z-\zeta| d s=2 \pi
$$

To see this, let $S_{\epsilon}(z)$ be a disk of radius $\epsilon>0$ centered at $z$ and contained in $\Omega$, let $C_{\epsilon}(z)$ denote the circle centered at $z$ with radius $\epsilon$. The function $\zeta \mapsto \ln \mid z$ is harmonic in $\Omega \backslash S_{\epsilon}$, so according to Proposition 1, we have
$$
0=\int_{C_{e}(z)} \frac{\partial}{\partial n} \ln |z-\zeta| d s+\int_{\Gamma} \frac{\partial}{\partial n} \ln |z-\zeta| d s
$$

Parametrizing $C_{\epsilon}(z)$ by $\zeta=z+\epsilon e^{i t}, 0 \leq t \leq 2 \pi, \frac{\partial}{\partial n} \ln |z-\zeta|=-\frac{1}{\epsilon}$ and $d s=$ and so
$$
0=-\int_{0}^{2 \pi} d t+\int_{\Gamma} \frac{\partial}{\partial n} \ln |z-\zeta| d s
$$
implying (18). Now, using (ii) and (iii) of Definition 1, write
$$
C L=\int_{\Gamma} C d s=\int_{\Gamma} \frac{\partial N}{\partial n} d s=\overbrace{\int_{\Gamma} \frac{\partial N_{1}}{\partial n} d s}^{=0, \text { by Proposition } 1}+\int_{\Gamma} \frac{\partial}{\partial n} \ln |z-\zeta| d s=0+2 \pi
$$
which implies (17).
Neumann functions are not unique for a region (two Neumann functi can differ by a function of $z$ and not $\zeta$; see Exercise 12). However, Neumann function satisfying Definition 1 will work to solve a Neum problem. Before we express the solution of the Neumann problem in te of the Neumann function, we note that from Theorem 4 if a solution Neumann problem exists, then it is unique up to an additive constant.
Suppose that $\Omega$ is a region bounded by a simple path $\Gamma$, and let $N($ denote a Neumann function, where $z$ and $\zeta$ are in $\Omega$. Then, up to an add constant, the solution $u(z)$ of the Neumann problem (12)-(14) is given
$$
u(z)=-\frac{1}{2 \pi} \int_{\Gamma} N(z, \zeta) f(\zeta) d s
$$

The proof of Theorem 5 is just like the proof of Theorem 2 (see Exer 10). Now we derive some classical Neumann functions.

EXAMPLE 1 Neumann function for the upper half-plane
Show that the Neumann function for the upper half-plane is
$$
\begin{aligned}
N(z, \zeta) & =\ln |z-\zeta|+\ln |\bar{z}-\zeta| \\
& =\frac{1}{2} \ln \left((x-s)^{2}+(y-t)^{2}\right)+\frac{1}{2} \ln \left((x-s)^{2}+(y+t)^{2}\right)
\end{aligned}
$$
for $z=x+i y$ and $\zeta=s+i t, y, t>0$ (Figure 5).

---

<!-- Page 68 -->

Left margin note (page 68)

452
Chapter 6
C

PROPOS NEI
FUNCTI UNBO

R

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-68_688_546_1679_85.jpg)

Figure 6 A Neu tion for the first q chored at $z=1+$ singularity at $\zeta=$

Right margin note (page 68)

rmal
$\overline{2}$
to
$\mid z-$
(20)
All
untann halfsely, is.

1e-toreal
$-w \mid$, r all 5, it ative is in Now
finite ction
r the

++++

nformal Mappings

Solution We know that $N(z, \zeta)=\ln |z-\zeta|+N_{1}(z, \zeta)$. Computing the no derivative of $\ln |z-\zeta|=\frac{1}{2} \ln \left((x-s)^{2}+(y-t)^{2}\right)$ along the real axis, we find
$$
-\left.\frac{d}{d t} \frac{1}{2} \ln \left((x-s)^{2}+(y-t)^{2}\right)\right|_{t=0}=\left.\frac{y-t}{(x-s)^{2}+(y-t)^{2}}\right|_{t=0}=\frac{y}{(x-s)^{2}+y}
$$

By adding $\frac{1}{2} \ln |\bar{z}-\zeta|=\frac{1}{2} \ln \left((x-s)^{2}+(y+t)^{2}\right)$ to $\ln |z-\zeta|$, this adds $\frac{-y}{(x-s)^{2}+}$ the normal derivative along the real axis, making the normal derivative of $\frac{1}{2} \ln \left.\zeta\left|+\frac{1}{2} \ln \right| \bar{z}-\zeta \right\rvert\,$ zero along the real axis. This shows that $N(z, \zeta)$ as defined by has 0 normal derivative along the boundary, in accordance with Proposition 2 other properties of the Neumann function in Definition 1 are easily verified.

The fact that the normal derivative of the Neumann function of an bounded region is zero on the boundary allows us to construct the Neum function for this region by using the Neumann function for the upper plane and a change of variables via a conformal mapping. More preci we have the following construction, which is valid for unbounded regior

ITION 3 JMANN ON FOR UNDED EGIONS

Suppose that $\Omega$ is an unbounded region with boundary $\Gamma$, and $\phi$ is a or one analytic mapping of $\Omega$ onto the upper half-plane, taking $\Gamma$ onto the axis. Then the Neumann function for $\Omega$ is given by
$$
N(z, \zeta)=\ln |\phi(z)-\phi(\zeta)|+\ln |\overline{\phi(z)}-\phi(\zeta)| \quad(z, \zeta \text { in } \Omega) .
$$

Proof Fix $z$ in $\Omega$ and consider the function $F(w)=\ln |\phi(z)-w|+\ln \mid \overline{\phi(z)}$ where $\phi(z)$ and $w$ are in the upper half-plane. By Example $1, \frac{\partial F}{\partial n}(w)=0$, fo $w$ on the real axis. Applying the change of variables formula (3), Section 6. follows that $\frac{\partial F \circ \phi}{\partial n}(\zeta)=0$ for all $\zeta$ on $\Gamma$. So $N(z, \zeta)$ has the right normal deriv on the boundary $\Gamma$. Does it have the right singularity at $\zeta=z$ ? Since $\overline{o(z)}$ the lower half-plane, it follows that $\ln |\overline{\phi(z)}-\phi(\zeta)|$ is harmonic for all $\zeta$ in $\Omega$. let us compare $\ln |\phi(z)-\phi(\zeta)|$ to $\ln |z-\zeta|$. We have
$$
\lim _{\zeta \rightarrow z}(\ln |\phi(z)-\phi(\zeta)|-\ln |z-\zeta|)=\lim _{\zeta \rightarrow z} \ln \left|\frac{\phi(z)-\phi(\zeta)}{z-\zeta}\right|=\ln \left|\phi^{\prime}(z)\right|
$$
because $\phi$ is analytic. Since $\phi^{\prime}(z) \neq 0, \ln |\phi(z)-\phi(\zeta)|$ and $\ln |z-\zeta|$ differ by a constant near $z$. Hence the function $N(z, \zeta)=\ln |z-\zeta|$ plus a harmonic fun in $\Omega$.

Let us give an application of Proposition 3.
EXAMPLE 2 Neumann function for the first quadrant
Applying Proposition 3 with $\phi(z)=z^{2}$, we obtain the Neumann function fo first quadrant (shown in Figure 6 at $z=1+i$ )
$$
\begin{aligned}
N(z, \zeta) & =\ln \left|z^{2}-\zeta^{2}\right|+\ln \left|\overline{z^{2}}-\zeta^{2}\right| \\
& =\ln |z-\zeta|+\ln |z+\zeta|+\ln |\bar{z}-\zeta|+\ln |\bar{z}+\zeta|
\end{aligned}
$$

---

<!-- Page 69 -->

Left margin note (page 69)

THEOREM 6 SOLUTION OF POISSON-NEUMANN PROBLEM
1.

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-69_502_533_1955_687.jpg)

Figure 7

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-69_506_541_1949_1375.jpg)

++++

Section 6.6 Poisson's Equation and Neumann Problems

Finding Neumann functions for bounded regions is more difficult beca the condition $\frac{\partial N}{\partial n}=C$ is not preserved by a conformal mapping $\phi(z)$; normal derivative is scaled by $\left|\phi^{\prime}(z)\right|$. In the exercises, we will compute Neumann function for the unit disk.

What if we are to solve Poisson's equation (1) with Neumann bound conditions (13)? The compatibility condition on $h$ and $f$ has already b handled by (16); it is
$$
\iint_{\Omega} h(\zeta) d A=\int_{\Gamma} f(\zeta) d s
$$

This problem is also solvable with the Neumann function, and for referen we present an analog of Theorem 2.

Suppose that $\Omega$ is a region with boundary $\Gamma$, let $N(z, \zeta)$ denote a Neum function for this region, where $z$ and $\zeta$ are in $\Omega$. If $u(z)$ is a solutio Poisson's equation (1) subject to a Neumann boundary condition (13) satisfying (23), then up to an additive constant
$$
u(z)=\frac{1}{2 \pi} \iint_{\Omega} h(\zeta) N(z, \zeta) d A-\frac{1}{2 \pi} \int_{\Gamma} N(z, \zeta) f(\zeta) d s
$$

Exercises 6.6
In Exercises 1-6, derive the Neumann function for the region depicted in the companying figure (Figures 7-12).
2.

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-69_502_533_1955_687.jpg)
Figure 8
3.

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-69_506_541_1949_1375.jpg)
Figure 9

---

<!-- Page 70 -->

Left margin note (page 70)

454
Chapter 6
4.

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-70_562_543_171_59.jpg)

Figure 10

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-70_509_517_216_742.jpg)
![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-70_509_537_214_1407.jpg)

Right margin note (page 70)

ution rence
ed for
$\left.\right|_{\rho=1}$
$(z, \zeta)$.

++++

onformal Mappings
5.

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-70_509_517_216_742.jpg)
Figure 11
6.

![](./images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-70_509_537_214_1407.jpg)
Figure 12
7. Uniqueness of the solution in a Poisson problem. Show that the sol of the Poisson problem in a bounded region $\Omega$ is unique. [Hint: The diffe between any two solutions is harmonic and has zero boundary values.]
8. Neumann function for the unit disk. Show that this function is defin $z, \zeta$ in the unit disk by
$$
N(z, \zeta)=\left\{\begin{array}{ll}
\ln |z-\zeta|+\ln \left|\frac{1}{\bar{z}}-\zeta\right|+\ln |z| & \text { if } z \neq 0 \\
\ln |\zeta| & \text { if } z=0
\end{array}\right.
$$

Derive this function by following the outlined steps.
(a) Write $z=r e^{i \theta}$ and $\zeta=\rho e^{i \eta}$. Fix $z \neq 0$, and show that
$$
\begin{aligned}
\frac{\partial}{\partial n} \ln |z-\zeta|_{\rho=1} & =\left.\frac{\partial}{\partial \rho} \frac{1}{2} \ln |z-\zeta|^{2}\right|_{\rho=1}=\frac{1}{2} \frac{\partial}{\partial \rho} \ln \left(r^{2}+\rho^{2}+2 r \rho \cos (\theta-\eta\right. \\
& =\frac{1+r \cos (\theta-\eta)}{1+r^{2}+2 r \cos (\theta-\eta)}
\end{aligned}
$$
(b) Write $\frac{1}{\bar{z}}=\frac{1}{r} e^{i \theta}$, use (a), and conclude that
$$
\left.\frac{\partial}{\partial n} \ln \left|\frac{1}{\bar{z}}-\zeta\right\rangle\right|_{\rho=1}=\frac{1+\frac{1}{r} \cos (\theta-\eta)}{\left(\frac{1}{r}\right)^{2}+1+2 \cos (\theta-\eta)}=\frac{r^{2}+r \cos (\theta-\eta)}{1+r^{2}+2 r \cos (\theta-\eta)} .
$$
(c) Use (a) and (b) to show that for $z \neq 0,\left.\frac{\partial}{\partial n} N(z, \zeta)\right|_{|\zeta|=1}=1$.
(d) Verify the remaining properties of the Neumann function for the given $N$
9. Prove (9) by justifying the following steps:
$$
\begin{array}{l}
\left|\iint_{\Omega_{e}} G(z, \zeta) h(\zeta) d A-\iint_{\Omega} G(z, \zeta) h(\zeta) d A\right| \\
\quad=\left|\iint_{B_{e}(z)} G(z, \zeta) h(\zeta) d A\right| \\
\quad \leq \iint_{B_{e}(z)}\left|u_{1}(z, \zeta) h(\zeta)\right| d A+\iint_{B_{e}(z)}|\ln | z-\zeta|h(\zeta)| d A \\
\quad \leq C_{1} \iint_{B_{e}(z)} d A+C_{2} \iint_{C_{e}(z)} \ln |z-\zeta| d A \\
\quad=C_{1} \epsilon^{2} \pi+C_{2} \int_{0}^{2 \pi} \int_{0}^{\epsilon} r \ln |r| d r d \theta
\end{array}
$$

---

<!-- Page 71 -->

Section 6.6 Poisson's Equation and Neumann Problems
455

Evaluate the last integral and show that the resulting expression on the right side tends to 0 as $\epsilon \rightarrow 0$.
10. Proof of Theorem 5. In addition to the hypothesis of the theorem, we further suppose that $\int_{\Gamma} u(\zeta) d s=A$ is finite.
(a) For fixed $z$ in $\Omega$, let $C_{\epsilon}(z), S_{\epsilon}(z)$, and $\Gamma_{\epsilon}$ be as in the proof of Theorem 2. Since $f(\zeta)=\frac{\partial u}{\partial n}$ in (19), we have
$$
\begin{aligned}
\int_{\Gamma} N(z, \zeta) \frac{\partial u}{\partial n} d s & =\int_{\Gamma} N(z, \zeta) \frac{\partial u}{\partial n} d s+\int_{C_{\epsilon}(z)} N(z, \zeta) \frac{\partial u}{\partial n} d s-\int_{C_{\epsilon}(z)} N(z, \zeta) \frac{\partial u}{\partial n} d s \\
& =\int_{\Gamma_{\epsilon}} N(z, \zeta) \frac{\partial u}{\partial n} d s-\int_{C_{\epsilon}(z)} N(z, \zeta) \frac{\partial u}{\partial n} d s \\
& =\int_{\Gamma_{\epsilon}} u(\zeta) \frac{\partial}{\partial n} N(z, \zeta) d s+\int_{C_{\epsilon}(z)} N(z, \zeta) \frac{\partial u}{\partial n} d s
\end{aligned}
$$
(b) As in the proof of (11)), show that $\int_{C_{e}(z)} N(z, \zeta) \frac{\partial u}{\partial n} d s \rightarrow 0$ as $\epsilon \rightarrow 0$.
(c) Justify the following steps:
$$
\int_{\Gamma_{e}} u(\zeta) \frac{\partial}{\partial n} N(z, \zeta) d s=\int_{C_{e}(z)} u(\zeta) \frac{\partial}{\partial n} N(z, \zeta) d s+\int_{\Gamma} u(\zeta) \frac{\partial}{\partial n} N(z, \zeta) d s
$$
$\int_{C_{\epsilon}(z)} u(\zeta) \frac{\partial}{\partial n} N(z, \zeta) d s \rightarrow-2 \pi u(z)$ (see the proof of (10)), and $\int_{\Gamma} u(\zeta) \frac{\partial}{\partial n} N(z, \zeta) d s= C \int_{\Gamma} u(\zeta) d s=A C=C^{\prime}$, where $C$ is as in Definition 1(ii).
(d) Complete the proof of Theorem 5.
11. Proof of Theorem 6. The proof mirrors the proof in the text of Theorem 2, using Green's second identity.
(a) Let $\Omega_{\epsilon}=\Omega \backslash S_{\epsilon}(z)$, where $S_{\epsilon}(z)$ is the closed disk of radius $\epsilon>0$, centered at $z$. Apply Green's second identity to $u$ and $N$ over the region $\Omega_{\epsilon}$ to get
$$
\begin{aligned}
-\iint_{\Omega_{e}} N(z, \zeta) h(\zeta) d A= & C \int_{\Gamma} u(\zeta) d s-\int_{\Gamma} N(z, \zeta) \frac{\partial u}{\partial n} d s \\
& +\int_{C_{e}} u(\zeta) \frac{\partial N}{\partial n} d s-\int_{C_{e}} N(z, \zeta) \frac{\partial u}{\partial n} d s
\end{aligned}
$$
where $C$ is the fixed value of the normal derivative of $N$ along $\Gamma$.
(b) Argue, as in Exercise 10, that as $\epsilon \rightarrow 0$,
$$
\iint_{\Omega_{e}} N(z, \zeta) h(\zeta) d A \rightarrow \iint_{\Omega} N(z, \zeta) h(\zeta) d A
$$
(c) Note that $C \int_{\Gamma} u(\zeta) d s$ is a constant; in fact, it is $2 \pi$ times the average value of $u$ on $\Gamma$.
(d) Just as we proved (10), show that $\int_{C_{\epsilon}} u(\zeta) \frac{\partial N}{\partial n} d s \rightarrow-2 \pi u(z)$, as $\epsilon \rightarrow 0$.
(e) Just as we proved (11), show that $\int_{C_{\epsilon}} N(z, \zeta) \frac{\partial u}{\partial n} d s \rightarrow 0$, as $\epsilon \rightarrow 0$.
(f) Complete the proof of Theorem 6.
12. Project Problem: On the uniqueness of the Neumann function. Suppose we have two Neumann functions $N_{1}(z, \zeta)$ and $N_{2}(z, \zeta)$ for the same region $\Omega$. They can be written in the form $N_{1}(z, \zeta)=\ln |z-\zeta|+u_{1}(z, \zeta), N_{2}(z, \zeta)=$

---

<!-- Page 72 -->

Left margin note (page 72)

456
Chapter 6

Right margin note (page 72)

the is, an same Theomann $t$ the an be this annd get Show $F(z)$ has n $\Omega_{\epsilon}$ (a) quas the nann here disk. of $\theta$

++++

Conformal Mappings
$\ln |z-\zeta|+u_{2}(z, \zeta)$, where $u_{1}$ and $u_{2}$ are harmonic functions of $\zeta$.
(a) Show that $N_{2}-N_{1}$ is harmonic. What is its normal derivative on I boundary of $\Omega$ ?
(b) Apply Theorem 4 and conclude that $N_{1}$ and $N_{2}$ differ by a constant-that expression independent of $\zeta$. Can this expression depend on $z$ ?
(c) Conclude that $N_{1}(z, \zeta)$ and $N_{2}(z, \zeta)$ are two Neumann functions for the region if and only if they differ by any function of $z$ alone.
13. Project Problem: Symmetry of the Neumann function. Unlike ? rem 2 of Section 6.5 for Green's functions, Definition 1 in this section for Neur functions does not mention that they are symmetric, and in general it is no case that $N(z, \zeta)=N(\zeta, z)$. In this problem we discover that symmetry $c$ z recaptured by imposing an extra condition on the Neumann function, and that can always be done without disrupting its role in the solution of the Neum Poisson problem.
(a) Refer to Exercise 12. We may add a function of $z$ to a Neumann function an another Neumann function. Let $N(z, \zeta)$ be a given Neumann function for $\Omega$. that we can find a function $F(z)$ and a Neumann function $N_{0}(z, \zeta)=N(z, \zeta)$ such that $\int_{\Gamma} N_{0}(z, \zeta) d s(d s=|d \zeta|)$ is independent of $z$. (It is crucial that $\Gamma$ finite length.)
(b) Applying Green's second identity to $N\left(z_{1}, \zeta\right)$ and $N\left(z_{2}, \zeta\right)$ over the regio and taking the limit as $\epsilon \rightarrow 0$ (as in the proof of Theorem 2), we get
$$
N\left(z_{1}, z_{2}\right)-N\left(z_{2}, z_{1}\right)=\int_{\Gamma}\left(N\left(z_{1}, \zeta\right) \frac{\partial N\left(z_{2}, \zeta\right)}{\partial n}-N\left(z_{2}, \zeta\right) \frac{\partial N\left(z_{1}, \zeta\right)}{\partial n}\right) d s
$$

Use the fact that the normal derivative of $N(z, \zeta)$ is $C$ (a constant) and par to conclude that $N_{0}(z, \zeta)=N_{0}(\zeta, z)$.
(c) As a double-check, replace $N(z, \zeta)$ by $N_{0}(z, \zeta)$ in (24) and show that the tion remains unchanged. [Hint: Remember that $F(z)$ is a constant as far a: integration is concerned, and use the compatibility condition (23).]
14. Neumann problem with odd boundary data. Consider a Neun problem in the unit disk in which $f(\zeta)=f\left(e^{i \theta}\right)$ is an odd function of $\theta$, w $-\pi \leq \theta \leq \pi$. Show that $u(z)=0$ for all $z$ on the real axis inside the unit [Hint: The functions $\ln \left|z-e^{i \theta}\right| f\left(e^{i \theta}\right)$ and $\ln \left|\frac{1}{z}-e^{i \theta}\right| f\left(e^{i \theta}\right)$ are odd functions if $z$ is a real number.]
