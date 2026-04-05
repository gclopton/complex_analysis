## Topics to Review

Green's theorem from calculus is required for this chapter. It is recalled and proved in Section 12.1. The chapter is intended to introduce methods for solving Laplace and Poisson equations. So Sections 3.8, 3.9, 4.4, and 7.5 are essential to appreciate this chapter. Sections 12.5 to 12.8 require familiarity with complex numbers and complex functions. The requisite material is included as a brief review in Section 12.5. Sections 12.5 and 12.6 can be covered independently of the rest of the chapter. Sections 12.7 and 12.8 are based on the preceding sections of the chapter.

## Looking Ahead . . .

In this chapter we introduce new tools for solving Dirichlet problems and Poisson equations: Green's functions, Neumann functions, and conformal mappings. Roughly speaking, Green's function for a given region $\Omega$ is a function that depends only on $\Omega$ and that can be used to solve any Dirichlet problem or Poisson problem on $\Omega$, in the same way that the Poisson kernel on the real line can be used to solve Dirichlet problems in the upper half-plane. A conformal mapping is like a change of variables that we can use to transform a Dirichlet problem from a given region onto another region on which the problem is simpler to solve, in the same way that a change of variables can be used to trasnform a difficult integral.

## 12

## GREEN'S FUNCTIONS AND CONFORMAL MAPPINGS

One cannot escape the feeling that these mathematical formulas have an independent existence and an intellignees of their own, that they are wiser that we are, wiser even than their discoverers, that we get more out of them than was originally put into them.

- HEINRICH HERTZ

The methods of this chapter are new, but the goal is still the same: to solve boundary value problems. To motivate the results of this chapter, review the Poisson integral formula in Section 7.5. Here we will derive similar formulas that solve the Dirichlet and Neumann problems on arbitrary (simply connected) regions in the plane. Like the Poisson integral, these formulas are packed with information about the solution.

In Sections 12.1 and 12.2, we start with Green's theorem from calculus and use simple tricks like integration by parts to clerive two identities, known as Green's first and second identities. We then apply these formulas to obtain important properties of solutions of Laplace's equation. In Section 12.3 we modify our formulas and introduce the amazing Green's functions. Simple manipulations with Green's functions yield formulas for the solutions of Dirichlet problems (Poisson integral-like formulas) and Poisson equations.

These remarkable formulas add to our understanding of properties of solutions of Dirichlet problems and, more important, they lead us to explore an important connection with the theory of analytic functions. Two major results are explored: the invariance of Laplace's equation by a change of variables using analytic functions (Section 12.6), and the composition of Green's functions with analytic functions (Section 12.7). The former yields the powerful method of conformal mappings, and the latter yields a nice way to compute Green's functions.

To simplify the presentation, we only discuss a sample of two dimensional problems. Many more types of problems can be treated in higher dimensions. We hope that this chapter will serve as a motivation to delve into the more advanced theories.

### 12.1 Green's Theorem and Identities

In this section, we prove Green's theorem and derive two identities, known as Green's first and second identities. We then derive several applications that give a flavor of the results of this chapter. We begin our discussion by reviewing basic definitions leading to the line integral.
Parametric Curves. Let $x=x(t)$ and $y=y(t)$ be continuous and piecewise smooth functions of $t$ on a closed interval $[a, b]$. The equations $x=x(t)$ and $y=y(t)$ are called parametric equations with parameter $t$. As $t$ varies over $[a, b]$, the point $(r(t), y(t))$ traces a parametric curve or simply a curve. It is sometimes convenient to set $C(t)=(x(t), y(t))$ and refer to the curve as the curve $C$. The point $(x(a), y(a))$ is called the initial point of $C$ and the point $(x(b), y(b))$ its terminal point. The curve is called closed if its terminal point is equal to its initial point; that is, $(x(a), y(a))=(x(b), y(b))$. In Figure 1 we show an arc of the unit circle parametrized by the equations $x(t)=\cos t$ and $y(t)=\sin t$, for $t$ in the interval $\left[-\frac{\pi}{2}, \pi\right]$.

Figure 1 The parametric interval $\left[-\frac{\pi}{2}, \pi\right]$ mapping to a circular are. Initial point ( $0,-1$ ), terminal point $(-1,0)$. To close the curve, we could use the interval $\left[-\frac{\pi}{2}, \frac{3 \pi}{2}\right]$.

![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-02_507_472_1407_72.jpg)
Figure 2 Simple curves:
(a) positively oriented,
(b) negatively oriented.

![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-02_433_992_895_650.jpg)

Simple Curves. A closed curve is called simple if it does not intersect itself. That is, if $C$ is simple and $C\left(t_{1}\right)=C\left(t_{2}\right)$ for some $t_{1}<t_{2}$ in $[a, b]$, then $t_{1}=a$ and $t_{2}=b$. A simple curve is also known as a Jordan curve, after the French mathematician Camille Jordan (1838-1922). Jordan proved a famous theorem that states that a simple curve $C$ divides the plane into two regions: one bounded and interior to $C$, and one unbounded and exterior to $C$ (see Figure 2).

Orientation. Jordan's theorem allows us to define the orientation of a simple curve $C$. You are moving in the positive direction along $C$ if the interior region is to your left; otherwise. you are moving in the negative direction of $C$. We denote by $-C$ the reverse of $C$. It is the curve that is traversed in the opposite direction as $C$.
Open Sets and Regions. A subset $U$ of the plane is open if for every $\left(x_{0}, y_{0}\right)$ in $U$ there is an open disk $D$ centered at ( $x_{0}, y_{0}$ ) and contained entircly in $U$. In other words, $U$ is open if every point in $U$ is an interior point. Consequently, if $U$ is open, then it cannot contain any of its boundary points, since boundary points are not interior points (Figure 3). A subset
$S$ of the complex plane is called connected if any two points ( $x_{0}, y_{0}$ ) and ( $x_{1}, y_{1}$ ) in $S$ can be joined by a polygonal line segment that is entirely contained in $S$. (By a polygonal line we mean a curve formed by finitely many line segments joined end to end.) If a set is open and connected, then it is called a region.

## Figure 3

(a) Not open.
(b) Open, not connected.
(c) A region: Open and connected.

## Figure 4

(a) Simply connected.
(b) Multiply connected.
(c) Multiply connected.

In (b) and (c) we show a curve whose interior is not contained in the region.
![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-03_429_424_444_495.jpg)

Simply Connected Region. A region $D$ in the plane is called simply connected if the interior region of every simple curve in $D$ is also contained in $D$. Pictorially, $D$ is simply connected if it has no holes in it (Figure 4). A region that is not simply connected is called multiply connected.
![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-03_435_399_1105_499.jpg)
![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-03_431_467_1106_884.jpg)

Line Integral. If $C$ is a curve parametrized by $(x(t), y(t)), a \leq t \leq b$, and $f(x, y)$ is a continuous function on $C$, we define the line integral of $f$ over $C$ to be

$$
\int_{C} f(x, y) d s=\int_{a}^{b} f(x(t), y(t)) \sqrt{\left[x^{\prime}(t)\right]^{2}+\left[y^{\prime}(t)\right]^{2}} d t
$$

Two other integrals will be of interest:
and
(3)
![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-03_426_475_446_899.jpg)
![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-03_425_395_447_1378.jpg)
![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-03_424_470_1112_1310.jpg)

$$
\int_{C} f(x, y) d x=\int_{a}^{b} f(x(t), y(t)) x^{\prime}(t) d t
$$

$$
\begin{aligned}
& \text { " } \\
& \text { L }
\end{aligned}
$$

## THEOREM 1 GREEN'S THEOREM

![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-04_387_389_1615_75.jpg)
Figure 5 Area as a line integral in Example 1.

The line integral has many properties similar to the Riemann integral. We state some of these properties for the integral with $d x$. Similar identities hold for the integrals with $d y$ or $d s$. The integral is linear:

$$
\int_{C}(a f(x, y)+b g(x, y)) d x=a \int_{C} f(x . y) d x+b \int_{C} g(x, y) d x
$$

It is additive over curves: If $C$ is a curve made up of two curves $C_{1}$ and $C_{2}$, joined together end to end, then

$$
\int_{C} f(x, y) d x=\int_{C_{1}} f(x, y) d x+\int_{C_{2}} f(x, y) d x
$$

If $-C$ is the reverse of $C$, then

$$
\int_{-C} f(x, y) d x=-\int_{C} f(x, y) d x
$$

## Green's Theorem

Green's theorem is a striking result from the calculus of several variables that relates a line integral around a closed curve to a double integral over the region bounded by that curve.

Let $C$ be a positively oriented simple curve with interior region $D$. Let $M(x, y)$ and $N(x, y)$ be continuous functions with continuous first partial derivatives on $C$ and $D$. Then

$$
\int_{C}(M(x, y) d x+N(x, y) d y)=\iint_{D}\left(\frac{\partial N}{\partial x}-\frac{\partial M}{\partial y}\right) d x d y
$$

Let us illustrate the theorem with examples and relegate its proof to the end of this section.

## EXAMPLE 1 Area as a line integral

Let $C$ be a positively oriented simple curve and $D$ the region interior to $C$ (Figure 5). Then the area of $D$ is given by any one of the following three integrals:

$$
\int_{C}-y d x, \quad \int_{C} r d y, \quad \frac{1}{2} \int_{C}(-y d x+x d y)
$$

Solution For the first integral, apply Green's theorem with $M(x, y)=-y, N(x, y)= 0, M_{y}=-1$, and $N_{x}=0$, where we are using subscripts to denote partial derivatives. Then

$$
\int_{C}-y d x=\iint_{D} d x d y=\text { area of } D,
$$

as claimed. Similarly, applying Green's theorem with $M=0$ and $N=x$. we find that $\int_{C} x d y=\iint_{D} d x d y=$ area of $D$. Adding the first two intexrals in (5) and dividing by two, we find that the third integral is also equal to ulse area of $D$.

![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-05_396_456_1597_35.jpg)
Figure 6 A typical multiply comected region: positively oriented outer curve, negatively oriented inner curve.

## EXAMPLE 2 Verifying Green's theorem

Let $C$ be the positively oriented unit circle, centered at the origin. Verify Grean's theorem with $M(x, y)=y^{2}$ and $N(x, y)=-x$.
Solution To do this problem, we compute the integrals on both sides of the identity (4) and show that they are equal. We have $M_{y}=2 y$, and $N_{x}=-1$, and (1) becomes

$$
\int_{C}\left(y^{2} d x-x d y\right) \cdots \iint_{D}(-1-2 y) d x d y
$$

To compute the line integral, we parametrize the circle by

$$
x(t)=\cos t, \quad y(t)=\sin t, \quad 0 \leq t \leq 2 \pi .
$$

Then $d x=-\sin t d t, d y=\cos t d t$, and the integral becomes

$$
\int_{C}\left(y^{2} d x-x d y\right)=-\int_{0}^{2 \pi}\left(\sin ^{3} t+\cos ^{2} t\right) d t=-\int_{-\pi}^{\pi}\left(\sin ^{3} t+\cos ^{2} t\right) d t
$$

where we have used Theorem 1, Section 2.1, to shift the interval of integration. Since $\sin ^{3} t$ is an odd function, its integral over a symmetric interval is 0 . Also,

$$
-\int_{-\pi}^{\pi} \cos ^{2} t d t=-\frac{1}{2} \int_{-\pi}^{\pi}(1+\cos 2 t) d t=-\pi
$$

Thus the value of the line integral is $-\pi$. To compute the double integral, because of the shape of the region, it is easier to use polar coordinates: $x=r \cos \theta, y=r \sin \theta$, $0 \leq \theta \leq 2 \pi, 0 \leq r \leq 1$, and $d x d y=r d r d \theta$. Then

$$
\begin{aligned}
\iint_{D}(-1-2 y) d x d y & =\int_{0}^{2 \pi} \int_{0}^{1}(-1-2 r \sin \theta) r d r d \theta \\
& =\int_{0}^{2 \pi}\left(-\frac{1}{2}-\frac{2}{3} \sin \theta\right) d \theta=-\pi
\end{aligned}
$$

Thus Green's theorem is verified. $\square$

## Multiply Connected Regions

For later applications, we will need a version of Green's theorem on multiply connected regions that are described as follows. Let $C$ be a simple closed curve and let $C_{1}, C_{2}, \ldots, C_{n}$ be simple closed curves. contained in the interior of $C$ and such that the interior regions of any two $C_{j}$ s have no common points. We also require that $C$ be positively oriented and all $C_{j} \mathrm{~s}$ be negatively oriented. Let $\Omega$ be the region interior to $C$ and exterior to $C_{1}$, $C_{2} \ldots, C_{n}$ (Figure 6). It will be convenient to refer to all the curves $C, C_{1}$, $C_{2}, \ldots, C_{n}$ collectively as the boundary of $\Omega$, and denote this boundary by $\Gamma$. Thus

$$
\int_{\Gamma} f(x, y) d x=\int_{C} f(x, y) d x+\sum_{j=1}^{n} \int_{C_{j}} f(x, y) d x
$$

## THEOREM 2 GREEN'S THEOREM FOR MULTIPLY CONNECTED REGIONS

![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-06_427_461_714_74.jpg)
Figure 7 for Example 3.

where $C_{j}$ are negatively oriented. A similar meaning is given to the integrals with $d y$ or $d s$.

Let $\Omega$ be a multiply connected region with boundary $\Gamma$, as just described. Suppose that $M(x, y)$ and $N(x, y)$ are continuous with continuous partial derivatives on $\Omega$ and $\Gamma$. Then

$$
\int_{\Gamma} M(x, y) d x+N(x, y) d y=\iint_{\Omega}\left(\frac{\partial N}{\partial x}-\frac{\partial M}{\partial y}\right) d x d y
$$

The proof is based on an interesting reduction to Theorem 1. (See the appendix of this section.)

## EXAMPLE 3 Green's theorem for multiply connected regions

Let $C$ be the positively oriented unit circle, centered at the origin, and let $C_{1}$ be the negatively oriented circle with center at the origin and radius $\frac{1}{2}$ (Figure 7). Evaluate

$$
I=\int_{C} \frac{y}{x^{2}+y^{2}} d x+\int_{C_{1}} \frac{y}{x^{2}+y^{2}} d x
$$

Solution Let $\Omega$ be the region bounded by $C$ and $C_{1}$. Applying (6) with $M=\frac{y}{x^{2}+y^{2}}$, $M_{y}=\frac{x^{2}-y^{2}}{\left(x^{2}+y^{2}\right)^{2}}, N=0$. and $N_{x}=0$, we find

$$
I=\iint_{\Omega} \frac{y^{2}-x^{2}}{\left(x^{2}+y^{2}\right)^{2}} d x d y
$$

where $\Omega$ is the annular region bounded by $C$ and $C_{1}$. Using polar coordinates: $x=r \cos \theta, y=r \sin \theta, 0 \leq \theta \leq 2 \pi, \frac{1}{2} \leq r \leq 1$, and $d x d y=r d r d \theta$, we get.

$$
\begin{aligned}
I=\iint_{\Omega} \frac{y^{2}-x^{2}}{\left(x^{2}+y^{2}\right)^{2}} d x d y & =\int_{0}^{2 \pi} \int_{\frac{1}{2}}^{1} \frac{r^{2}\left(\sin ^{2} \theta-\cos ^{2} \theta\right)}{r^{4}} r d r d \theta \\
& =\int_{0}^{2 \pi} \overbrace{\left(\sin ^{2} \theta-\cos ^{2} \theta\right)}^{-\cos 2 \theta} d \theta \int_{\frac{1}{2}}^{1} \frac{1}{r} d r \\
& =-\ln 2 \int_{0}^{2 \pi} \cos 2 \theta d \theta=0
\end{aligned}
$$

## Green's Identities

In solving Dirichlet and Neumann problems, we are asked to find a harmonic function inside a region $\Omega$, given its values or the values of its normal derivative on the boundary of $\Omega$. Green's theorem relates a line integral to a double integral, and so in a way it gives information about the values of a function inside a region from its values on the boundary of that region. Our goal in this chapter is to use Green's theorem in a very ingenious way and show how we can solve Dirichlet and Neumann problems using line integrals on the boundary. For this purpose, we derive two important formulas, known as Green's firsi and second identities.

## THEOREM 3 GREEN'S IDENTITIES

![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-07_394_458_1188_47.jpg)
Figure 8 Example of the region in Theorem 3.

Let us recall the meaning of a normal derivative. If $u(x, y)$ is a function defined on a curve $C$, parametrized by $x(t)$ and $y(t)$, then the normal derivative of $u$, denoted $\frac{\partial u}{\partial n}$, is the directional derivative of $u$ in the direction of the unit normal vector:

$$
\frac{\partial u}{\partial n}=\nabla u \cdot n=\left(u_{x}, u_{y}\right) \cdot \frac{\left(y^{\prime}(t),-x^{\prime}(t)\right)}{\sqrt{\left[x^{\prime}(t)\right]^{2}+\left[y^{\prime}(t)\right]^{2}}},
$$

where in this expression we recognize the normal vector to the curve $C$ as the vector $\left(y^{\prime}(t),-x^{\prime}(t)\right)$ and its norm $\sqrt{\left[x^{\prime}(t)\right]^{2}+\left[y^{\prime}(t)\right]^{2}}$. Recalling the notation of (1), $d s=\sqrt{\left[x^{\prime}(t)\right]^{2}+\left[y^{\prime}(t)\right]^{2}} d t$, we have, for the points on the curve $C$,

$$
\begin{aligned}
\frac{\partial u}{\partial n} d s & =\left(u_{x}, u_{y}\right) \cdot\left(y^{\prime}(t),-x^{\prime}(t)\right) d t=u_{x} y^{\prime}(t) d t-u_{y} r^{\prime}(t) d t \\
& =-u_{y} d x+u_{x} d y
\end{aligned}
$$

We are now ready to state and prove two important identities.

Let $\Omega$ be a multiply connected region with boundary $\Gamma$, as described in Theorem 2 (Figure 8). (In particular, the outer curve is positively oriented and the inner curves are negatively oriented.) Let $u(x, y)$ and $v(x, y)$ have continuous second order partial derivatives on $\Omega$ and its boundary. Then we have Green's first identity

$$
\iint_{\Omega}\left(u \nabla^{2} v+\nabla u \cdot \nabla v\right) d x d y=\int_{\Gamma} u \frac{\partial v}{\partial n} d s
$$

## and Green's second identity

$$
\iint_{\Omega}\left(u \nabla^{2} v-v \nabla^{2} u\right) d x d y=\int_{\Gamma}\left(u \frac{\partial v}{\partial n}-v \frac{\partial u}{\partial n}\right) d s
$$

Proof Apply Green's theorem with $M(x, y)=-u v_{y}, N(x, y)=u v_{x}, M_{y}= -u_{y} v_{y}-u v_{y y} . N_{x}=u_{x} v_{x}+u v_{x x}$, and get

$$
\iint_{\Omega}\left(u\left(v_{x x}+v_{y y}\right)+\left(u_{x} v_{x}+u_{y} v_{y}\right)\right) d x d y=\int_{\Gamma} u\left(-v_{y} d x+v_{x} d y\right)
$$

The integral on the left is the same as the integral on the left of (9), and the integral on the right is the same as the integral on the right of (9), because of (8). So (9) holds. To prove (10), we reverse the roles of $u$ and $v$ in (9) and get

$$
\iint_{\Omega}\left(v \nabla^{2} u+\nabla u \cdot \nabla u\right) d x d y=\int_{\Gamma} v \frac{\partial u}{\partial n} d s
$$

Subtracting this from (9), we get (10).

## PROPOSITION 1

THEOREM 4 UNIQUENESS OF SOLUTION IN A DIRICHLET PROBLEM

## Applications to Boundary Value Problems

We now derive several interesting applications of Green's identities. In addition to their importance these applications give a flavor of the material of the remaining sections of this chapter.

EXAMPLE 4 Green's formula for the integral of the Laplacian
This formula states that if $v$ has continuous first and second-order partial derivatives in a simply or multiply connected region $\Omega$, as in Theorem 2, with boundary I', then

$$
\iint_{\Omega} \nabla^{2} v(x, y) d x d y=\int_{\Gamma} \frac{\partial v}{\partial n} d s .
$$

To prove this formula, simply take $u=1$ in Green's first identity.

## EXAMPLE 5 Compatibility condition in Neumann problems

Let $\Omega$ be a simply or multiply connected region as in Theorem 2, with boundary $\Gamma$. Suppose that $u$ is harmonic on $\Omega$; that is, $u$ has continuous first- and second-order partial derivatives in $\Omega$ and $u_{x x}+u_{y y}=0$ on $\Omega$. Then the normal derivative of $u$ must integrate to 0 along the boundary. That is, the boundary values of the normal derivative of a harmonic function $u$ cannot be arbitrary; they must satisfy the compatibility condition

$$
\int_{\Gamma^{\Gamma}} \frac{\partial u}{\partial n} d s=0
$$

To prove this fact, just take $v=1$ in Green's second identity.
For the remaining applications, we will need the following result, whose proof can be found in any book on vector calculus (or see [1], Section 2.1).

Suppose that $u(x, y)$ is a function defined on a region $\Omega$ such that $u_{x}(x, y)=$ 0 and $u_{y}(x, y)=0$ for all $(x, y)$ in $\Omega$. Then $u$ must be constant on $\Omega$.

We can now prove the uniqueness of the solution of the Dirichlet problem on a simply or multiply connected region $\Omega$.

Let $\Omega$ be a simply or multiply connected region with boundary $\Gamma$, as in Theorem 3. If $u_{1}$ and $u_{2}$ are harmonic functions on $\Omega$ and $u_{1}=u_{2}$ on the boundary $\Gamma$, then $u_{1}=u_{2}$ on $\Omega$.

Proof Let $u=u_{1}-u_{2}$. Then $u$ is harmonic on $\Omega$ and $u=0$ on $\Gamma$. We must show that $u$ is 0 on $\Omega$. Apply Green's first identity with $u=v$ and use the fact that $\nabla^{2} u=0$. We get

$$
\iint_{\Omega} \nabla u \cdot \nabla u d x d y=\int_{\Gamma} u \frac{\partial u}{\partial n} d s
$$

But $u=0$ on $\Gamma$ and $\nabla u \cdot \nabla u=u_{x}^{2}+u_{y}^{2}$, so

$$
\iint_{\Omega}\left(u_{x}^{2}+u_{y}^{2}\right) d x d y=0
$$

THEOREM 5 UNIQUENESS OF SOLUTION IN A NEUMANN PROBLEM

![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-09_389_412_1528_33.jpg)
Figure 9 A standard curve $C$.

The only way for the integral of a nonnegative continuous function to be 0 is for this function to be identically 0 . Thus $u_{x}^{2}+u_{y}^{2}=0$, which in turn implies that $u_{x}=0$ and $u_{y}=0$ on $\Omega$. By Proposition 1, we conclude that $u$ is constant. But this constant has to be 0 on the boundary, so $u=0$ on $\Omega$. $\square$

In the preceding proof, we showed that if $u$ is harmonic on $\Omega$, then

$$
\iint_{\Omega}\left(u_{x}^{2}+u_{y}^{2}\right) d x d y=\int_{\Gamma} u \frac{\partial u}{\partial n} d s
$$

From this identity it follows that if $\frac{\partial u}{\partial n}=0$ on the boundary $\Gamma$, then

$$
\iint_{\Omega}\left(u_{x}^{2}+u_{y}^{2}\right) d x d y=0
$$

and as we argued previously, we conclude that $u=C$ on $\Omega$. Thus, as in Theorem 4, it follows that the solution of a Neumann problem is unique up to an additive constant.

Let $\Omega$ be a simply or multiply connected region as in Theorem 3, with boundary $\Gamma$. If $u_{1}$ and $u_{2}$ are harmonic functions on $\Omega$ and $\frac{\partial u_{1}}{\partial n}=\frac{\partial u_{2}}{\partial n}$ on the boundary $\Gamma$, then $u_{1}=u_{2}+C$ on $\Omega$.

Further applications of Green's identities to Dirichlet and Neumann problems will be represented in the next sections.

## Appendix: Proofs of Theorems 1 and 2

We will prove Theorem 1 in the case where the simple curve $C$ is a smooth standard curve, where by standard curve we mean that no vertical or horizontal line can intersect $C$ in more than two points. We then indicate how to extend this result to more general situations.

As illustrated by Figure 9, given a standard curve $C$, we can find an interval $[a, b]$ and two differentiable functions $f(x)$ and $g(x)$ on $[a, b]$. such that $C$ is composed of a top portion $C_{1}$, which consists of the graph of $f(x)$, and a bottom portion $C_{2}$, which consists of the graph of $g(x)$. Since $C$ is positively oriented, the reverse of $C_{1}$ is parametrized by ( $x . f(x)$ ), as $x$ runs from $a$ to $b$; while $C_{2}$ is parametrized by $(x, g(x))$, as $x$ runs from $a$ to $b$. So, for example,

$$
-\int_{C_{1}} M(x, y) d x=\int_{a}^{b} M(x, f(x)) d x ; \text { and } \int_{C_{2}} M(x, y) d x=\int_{a}^{b} M(x, g(x)) d x
$$

Also, if $D$ is the interior of $C$, then

$$
\begin{aligned}
\iint_{D} \frac{\partial M}{\partial y} d x d y & =\iint_{D} \frac{\partial M}{\partial y} d y d x=\int_{a}^{b}\left[\int_{g(x)}^{f(x)} \frac{\partial M}{\partial y} d y\right] d x \\
& =\int_{a}^{b}(M(x, f(x))-M \Gamma(x, g(x))) d x \\
& =-\int_{C_{1}} M(x, y) d x-\int_{C^{a}} M(x, y) d x=-\int_{C} M(x, y) d x
\end{aligned}
$$

![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-10_248_341_437_77.jpg)
Figure 10

![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-10_336_366_1495_74.jpg)
Figure 11 Each polygonal path $L_{j}$ is traversed in both directions, so the integral over $L_{y}$ is 0 .

In a similar way, we can show that

$$
\iint_{D} \frac{\partial N}{\partial x} d x d y=\int_{C} N(x, y) d y,
$$

and Green's theorem follows in this case upon subtracting the last two equations. For an arbitrary simple curve $C$ ' we divide the region inside $C$ into regions with boundaries consisting of positively oriented standard curves. Let $C_{j}$, $j=1,2, \ldots, n$, denote the resulting boundary curves, and let $D_{j}$ denote the region inside $C_{j}$. This construction is illustrated in Figure 10 with $n=4$. Each curve consists of portions of the curve $C$ and portions not on $C^{\prime}$. The portions on $C$ are traversed once in the positive direction, while the portions not on $C$ are traversed twice in opposite direction. As a result, the sum of the integrals over all $C_{j}$ add up to the integral over $C$, since the integrals over the portions not on $C$ cancel out. Applying the version of Green's theorem for standard curves and then adding the integrals, we get

$$
\sum_{j=1}^{\prime \prime} \int_{C_{j}}(M(x . y) d x+N(x, y) d y)=\sum_{j=1}^{n} \iint_{D_{j}}\left(\frac{\partial N}{\partial x}-\frac{\partial M}{\partial y}\right) d x d y .
$$

But, as we just argued, the left side equals $\int_{C}(M(x, y) d x+N(x, y) d y)$, and the right side equals $\iint_{D}\left(\frac{\partial N}{\partial x}-\frac{\partial M}{\partial y}\right) d x d y$, because the $D_{j}$ 's are disjoint and cover $D$. Thus Green's theorem holds in this case.

The proof of Green's theorem for multiply connected regions (Theorem 2) follows from the version for simply connected regions, using ideas similar to those in the proof of Theorem 1. Recall that we have a region $\Omega$ with boundary $\Gamma$ consisting of an exterior curve $C$ and interior curves $C_{j}(j=1.2 \ldots, n)$. Join the outer curve $C$ to $C_{1}$ using a polygonal curve $L_{1}$ traversed in two opposite directions. Join $C_{1}$ to $C_{2}$ by a similar polygonal curve $L_{2}$. Continue in this fashion, joining the curve $C_{j}$ to the curve $C_{j+1}$ by a polygonal curve $L_{j+1}$ traversed in two opposite directions and finally join $C_{n}$ to $C$ by a polygonal curve $L_{n+1}$ traversed in two opposite directions. This construction yields two simple closed curves $\Gamma_{1}$ and $\Gamma_{2}$, as illustrated in Figure 11. Let $\Omega_{j}$ denote the region interior to $\Gamma_{j}(j=1,2)$. Apply Theorem 1 on the curves $\Gamma_{1}$ and $I_{2}$ and add the results:

$$
\begin{aligned}
\sum_{j=1}^{2} \int_{\Gamma_{j}}(M(x, y) d x+N(x, y) d y) & =\sum_{j=1}^{2} \iint_{\Omega_{j}}\left(\frac{\partial N}{\partial x}-\frac{\partial M}{\partial y}\right) d x d y \\
& =\iint_{D}\left(\frac{\partial N}{\partial x}-\frac{\partial M}{\partial y}\right) d x d y
\end{aligned}
$$

But the integrals over the polygonal portions $L_{j}$ cancel out because these portions are traversed in opposite direction. As a result, the left side adds up to $\int_{\Gamma}(M(x, y) d x+N(x, y) d y)$, and Theorem 2 follows.

![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-11_396_440_163_35.jpg)
Figure 12

![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-11_393_435_671_38.jpg)

![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-11_472_474_1073_38.jpg)
Figure 14

![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-11_464_474_1594_38.jpg)
Figure 15

## Exercises 12.1

In Exercises 1-4, verify Green's theorem for the given functions $M$ and $N$ and curve $C$. That is, compute both sides of (4) and show that they are equal.

1. $M=x y, N=y, C$ as in Figure 12.
2. $M=x^{2} y, N=x+y, C$ as in Figure 12.
3. $M=x-y, N=y^{2}, C$ as in Figure 13.
4. $M=x^{2}-y^{2}, N=2 x y . C$ as in Figure 14.

In Exercises 5-8, verify Green's theorem (Theorem 2) for the given functions M and $N$, where the curve $\Gamma$, shown in Figure 15, consists of the two rircles $C_{1}$ and $C_{2}$.
5. $M=0, N=x$.
6. $M=-y, N=x$.
7. $M=\frac{-y}{x^{2}+y^{2}}, N=\frac{x}{x^{2}+y^{2}}$.
8. $M=\frac{1}{x^{2}+y^{2}}, N=0$.

In Exercises 9-12, use Green's identities to evaluate the given integral.
9. $\int_{C} y \frac{\partial x}{\partial n} d s$, where $C$ is as in Figure 12.
10. $\int_{C} \frac{\partial f}{\partial n} d s$, where $f(x, y)=x^{2}-2 x+y^{2}$ and $C$ is as in Figure 12.
11. $\int_{C}(x+y) \frac{\partial f}{\partial n} d s$, where $f(x, y)=c^{r} \cos y$ and $C$ is as in Figure 12.
12. $\int_{C} x \frac{\partial f}{\partial n} d s$, where $f(x, y)=\ln \left(x^{2}+y^{2}\right)$ and $C$ is as in Figure 15.
13. Area of multiply connected regions. Let $\Omega$ and $\Gamma$ be as in Theorem 2 . Show that the area of $\Omega$ is given by any one of the integrals

$$
\int_{\Gamma}-y d x, \quad \int_{\Gamma} x d y, \quad \frac{1}{2} \int_{\Gamma}(-y d x+x d y)
$$

14. Let $C$ be any positively oriented simple curve enclosing the origin. Compute

$$
\int_{C} \frac{-y d x+x d y}{x^{2}+y^{2}}
$$

[Hint: Let $C_{r}$ be a negatively oriented circle around the origin, contained in $C$. Apply Theorem 2.]
15. In the notation of Theorem 3, suppose that $u$ is harmonic and $v=0$ on $\Gamma$. Show that

$$
\iint_{\Omega} \nabla u \cdot \nabla v d x d y=0
$$

16. In the notation of Theorem 2. suppose that $y$ is harmonic on $\Omega$. Show that

$$
\int_{\Gamma}\left(\frac{\partial u}{\partial y} d x-\frac{\partial u}{\partial x} d y\right)=0
$$

![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-12_380_463_208_56.jpg)
Figure 16 The hypocycloid in Exercise 18:
$x(t)=a \cos ^{3} t, y(t)=a \sin ^{3} t$, $0 \leq t \leq 2 \pi$.

17. Express the area of the ellipse $\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1$ as a line integral and then find the area. [Hint: Use one of the integrals in Example 1.]
18. Express the area of the hypocycloid $x^{\frac{2}{3}}+y^{\frac{2}{3}}=a^{\frac{2}{3}}$ as a line integral and then find the area (Figure 16). [Hint: Use the 3rd integral in (5).]
19. Consider the Neumann problem in polar coordinates: $\nabla^{2} u=0$ on the unit disk and $\frac{\partial u}{\partial r}(1, \theta)=\sin \theta$ if $0 \leq \theta \leq \pi$ and 0 if $\pi \leq \theta \leq 2 \pi$. Does the problem have a solution? Explain your answer.
20. Project Problem: Dirichlet's Principle. Let $\Omega$ be a simply or multiply connected region with boundary $\Gamma$, as in Theorem 3. Let $h(x, y)$ be defined for ( $x, y$ ) on $\Gamma$, and let $u(x, y)$ denote the (unique) solution of the Dirichlet problem $\nabla^{2} u=0$ on $\Omega$ and $u=h$ on $\Gamma$. The energy of a function $\phi$ defined on $\Omega$ is the nonnegative number

$$
E(\phi)=\frac{1}{2} \iint_{\Omega}|\nabla \phi|^{2} d x d y
$$

where $\nabla \phi=\left(\phi_{x}, \phi_{y}\right)$ is the gradient of 0 . Dirichlet's principle states that of all functions $v(x, y)$ on $\Omega$ that satisfy the Dirichlet boundary condition $v=h$ on $\Gamma$, the one that minimizes the energy integral is the harmonic function $u$. That is, if $v=h$ on $\Gamma$, then $E(v) \geq E(u)$. Follow the outlined steps to prove the principle.
(a) Write $v=u+(v-u)=u+u$, where $w=0$ on l'. Show that $|\nabla v|^{2}= |\nabla u|^{2}+2 \nabla u \cdot \nabla w+|\nabla w|^{2}$.
(b) With the help of Exercise 15, show that $E(v)=E(u)+E(u)$. Since $E(w) \geq 0$, conclude that $E(v) \geq E(u)$.

### 12.2 Harmonic Functions and Green's Identities

In this section, we derive several classical properties of harmonic functions, including Gauss's mean value property, and the maximum and minimum modulus principles. These important results follow from straightforward applications of Green's identities (Section 12.1) using the logarithmic function. For this reason, we start with two simple but very useful properties of the logarithm.

## PROPOSITION 1 NORMAL DERIVATIVE OF THE LOGARITHM

For $(x, y) \neq\left(x_{0}, y_{0}\right)$ let

$$
v(x, y)=\frac{1}{2} \ln \left(\left(x-x_{0}\right)^{2}+\left(y-y_{0}\right)^{2}\right) .
$$

Let $C_{r}$ be a positively oriented circle with center $\left(x_{0}, y_{0}\right)$ and radius $r>0$
(Figure 1). Then

$$
\frac{\partial v}{\partial n}(x, y)=\frac{1}{r} \text { for all }(x, y) \text { on } C_{r} .
$$

Proof Parametrize $C_{r}$ by $x(t)=x_{0}+r \cos t, y(t)=y_{0}+r \sin t, 0 \leq t \leq 2 \pi$; then $x^{\prime}(t)=-r \sin t$ and $y^{\prime}(t)=r \cos t, \sqrt{\left[x^{\prime}(t)\right]^{2}+\left[y^{\prime}(t)\right]^{2}}=r$. So the unit normal

![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-13_382_421_292_47.jpg)
Figure 1 The circle $C_{r}$.

## PROPOSITION 2 HARMONICITY OF THE LOGARITHM

THEOREM 1 GAUSS'S MEAN VALUE PROPERTY

![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-13_356_382_1625_47.jpg)
Figure 2 The circle $C_{r}$ and its interior region are contained in $\Omega$, for all $0 \leq r<a$.

vector on $C_{r}$ is $\frac{1}{r}(r \cos t, r \sin t)=(\cos t$. $\sin t)$. We have

$$
v_{x}=\frac{x-x_{0}}{\left(x-x_{0}\right)^{2}+\left(y-y_{0}\right)^{2}} \quad \text { and } \quad v_{y}=\frac{y-y_{0}}{\left(x-x_{0}\right)^{2}+\left(y-y_{0}\right)^{2}} .
$$

For $(x, y)$ on $C_{r}$, we have

$$
\begin{aligned}
\frac{\partial v}{\partial n}(x, y) & =\left.\left(v_{x}, v_{y}\right) \cdot(\cos t, \sin t)\right|_{x=x_{0}+r \cos t, y=y_{0}+r \sin t} \\
& =\left(\frac{r \cos t}{r^{2}\left(\cos ^{2} t+\sin ^{2} t\right)}, \frac{r \sin t}{r 2\left(\cos ^{2} t+\sin ^{2} t\right)}\right) \cdot(\cos t, \sin t)=\frac{1}{r}
\end{aligned}
$$

as claimed.
The following property was used several times previously.
The function $v(x, y)=\frac{1}{2} \ln \left(\left(x-x_{0}\right)^{2}+\left(y-y_{0}\right)^{2}\right)$ is harmonic at all points $(x, y) \neq\left(x_{0}, y_{0}\right)$.

Proof A quick way to see this is to realize that $v$ is the translate of $\frac{1}{2} \ln \left(x^{2}+y^{2}\right)= \ln r$. Using the polar form of the Laplacian, $\nabla^{2} f=f_{r r}+(1 / r) f_{r}+\left(1 / r^{2}\right) f_{00}$. it follows that $\ln r$ satisfies Laplaces equation for $r \neq 0$. Hence its translate $v(x, y)$ satisfies Laplaces equation for $(x, y) \neq\left(x_{0}, y_{0}\right)$.
We can now prove Gauss's mean value property of harmonic functions. This property says that the value of a harmonic function $u$ at any point ( $x_{0}, y_{0}$ ) is equal to the average value of $u$ over any circle centered around $\left(x_{0}, y_{0}\right)$.

Suppose that $u$ is harmonic on a region $\Omega$. Let $\left(x_{0}, y_{0}\right)$ be any point in $\Omega$ and $r>0$ be any real number such that the closed disk of radius $r>0$ centered at ( $x_{0}, y_{0}$ ) is contained in $\Omega$ (Figure 2). Then

$$
u\left(x_{0} \cdot y_{0}\right)=\frac{1}{2 \pi} \int_{0}^{2 \pi} u\left(x_{0}+r \cos t, y_{0}+r \sin t\right) d t
$$

A function satisfying (1) at all points in $\Omega$ is said to have the mean value property in $\Omega$.

Proof Consider the following function of $r \geq 0$,

$$
\phi(r)=\frac{1}{2 \pi} \int_{0}^{2 \pi} u\left(x_{0}+r \cos t . y_{0}+r \sin t\right) d t
$$

where $r$ is in a small interval, say $[0, a]$, such that the disk of radius $r=a$ with center at ( $x_{0} . y_{0}$ ) is contained in $\Omega$. For $r>0, \phi(r)$ is equal to the average value of $u$ on $C_{r}$, the circle of radius $r$ and center ( $x_{0}, y_{0}$ ). And. for $r=0$,

$$
\phi(0)=\frac{1}{2 \pi} \int_{0}^{2 \pi} u\left(x_{0}, y_{0}\right) d t=u\left(x_{0}, y_{0}\right)
$$

![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-14_355_454_303_65.jpg)
Figure 3 The boundary $\Gamma_{r_{1}, r_{2}}$ consists of $C_{r_{1}}$ and $C_{r_{2}}$.

Because $\phi$ is the integral of the continuous function $u$, it is itself a continuous function of $r$ on $[0, a]$. Our goal is to show that $\phi$ is in fact constant. From this it will follow that $\phi(r)=\phi(0)=u\left(x_{0}, y_{0}\right)$, which is what the theorem asserts.

It is enough to show that $\phi\left(r_{1}\right)=\phi\left(r_{2}\right)$ for all $0<r_{1}<r_{2} \leq a$. Then, by continuity of $\phi$, the equality $\phi\left(r_{1}\right)=\phi\left(r_{2}\right)$ will hold if $0 \leq r_{1}<r_{2} \leq a$. The proof uses Green's identities and properties of the logarithm in a nice way. Parametrize $C^{\prime}$, by $x(t)=x_{0}+r \cos t, y(t)=y_{0}+r \sin t, 0 \leq t \leq 2 \pi, d s=r d t$. Then the right side of (1) becomes

$$
\phi(r)=\frac{1}{2 \pi} \int_{0}^{2 \pi} u\left(x_{0}+r \cos t, y_{0}+r \sin t\right) d t=\frac{1}{2 \pi r} \int_{C_{r}} u d s
$$

Thus, to show that $\phi\left(r_{1}\right)=\omega\left(r_{2}\right)$ for any $0<r_{1}<r_{2} \leq a$, it is enough to show that

$$
\frac{1}{r_{2}} \int_{C_{r_{2}}} u d s-\frac{1}{r_{1}} \int_{C_{r_{1}}} u d s=0
$$

where $C_{r_{1}}$ and $C_{r_{2}}$ are circles centered at ( $x_{0}, y_{0}$ ) with radii $r_{1}$ and $r_{2}$, respectively. Using the result of Proposition 1, we find that on $C_{r_{1}}$

$$
\frac{1}{r_{1}} \int_{C_{r_{1}}} u d s=\int_{C_{r_{1}}} u \frac{\partial v}{\partial n} d s
$$

where $v=\frac{1}{2} \ln \left(\left(x-x_{0}\right)^{2}+\left(y-y_{0}\right)^{2}\right)$. Similarly, on $C_{r_{2}}$,

$$
\frac{1}{r_{2}} \int_{C_{r_{2}}} u d s=\int_{C_{r_{2}}} u \frac{\partial u}{\partial n} d s
$$

Hence

$$
\phi\left(r_{2}\right)-\phi\left(r_{1}\right)=\int_{C_{r_{2}}} u \frac{\partial v}{\partial n} d s-\int_{C_{r_{1}}} u \frac{\partial v}{\partial n} d s=\int_{\Gamma_{r_{1}, r_{2}}} u \frac{\partial v}{\partial n} d s
$$

where $\Gamma_{r_{1}, r_{2}}$ is the boundary of the annular region $\Omega_{r_{1}, r_{2}}$ that consists of the inner negatively oriented circle $C_{r_{1}}$ and the outer positively oriented circle $C_{r_{2}}$ (Figure 3). Since both $u$ and $v$ are harmonic in $\Omega_{r_{1}, r_{2}}$, it follows from Green's second identity that

$$
\int_{\Gamma_{r_{1}, r_{2}}} u \frac{\partial v}{\partial n} d s=\int_{\Gamma_{r_{1}, r_{2}}} v \frac{\partial u}{\partial n} d s
$$

because the left side of Green's identity is 0 in this case. Now using the fact that $v=\ln r_{1}$ on $C_{r_{1}}$ and $v=\ln r_{2}$ on $C_{r_{2}}$, we get

$$
\begin{aligned}
\int_{\Gamma_{r_{1}, r_{2}}} v \frac{\partial u}{\partial n} d s & =\int_{C_{r_{2}}} v \frac{\partial u}{\partial n} d s-\int_{C_{r_{1}}} v \frac{\partial u}{\partial n} d s \\
& =\ln \left(r_{2}\right) \overbrace{\int_{C_{r_{2}}} \frac{\partial u}{\partial n} d s}^{=0}-\ln \left(r_{1}\right) \overbrace{\int_{C_{r_{1}}} \frac{\partial u}{\partial n} d s}^{=0}=0
\end{aligned}
$$

because of the compatibility condition for harmonic functions (Example 5, Section 12.1). Thus $\phi\left(r_{2}\right)-\phi\left(r_{1}\right)=0$, as desired.

THEOREM 2
MAXIMUMMINIMUM PRINCIPLE

It can be shown that the converse of Gauss's mean value property is also true, in the following sense. Suppose that $u(x, y)$ has continuous first and second partial derivatives in a region $\Omega$ and $u$ satisfies the mean value property at all points in $\Omega$, then $u$ is harmonic on $\Omega$.

The mean value property has important consequences, such as the maximum and minimum modulus principles that we prove later in this section. Let us now show an interesting application to the evaluation of certain definite integrals.

## EXAMPLE 1 Applying the mean value property

(a) Verify that $u(x, y)=e^{y} \cos x$ is harmonic for all $(x, y)$.
(b) Show that

$$
\frac{1}{2 \pi} \int_{0}^{2 \pi}, \sin t \cos (\cos t) d t=1
$$

(c) More generally, show that for any real numbers $a$ and $b$

$$
\frac{1}{2 \pi} \int_{0}^{2 \pi} e^{b+\sin t} \cos (a+\cos t) d t=e^{b} \cos a
$$

Solution (a) This part is straightforward:

$$
u_{x x}=-e^{y} \cos x, \quad u_{y y}=e^{y} \cos x
$$

Hence $u_{x, r}+u_{y y}=0$ and the function is harmonic for all ( $x, y$ ). To do part (b), we use the mean value property of $u$ at the origin:

$$
u(0,0)=\frac{1}{2 \pi} \int_{0}^{2 \pi} u(\cos t \cdot \sin t) d t-\frac{1}{2 \pi} \int_{0}^{2 \pi} e^{\sin t} \cos (\cos t) d t
$$

But $u(0,0)=1$ and so (b) holds. To prove (c), we apply the mean value property at the point ( $a, b$ ). Then

$$
\begin{aligned}
e^{b} \cos a & =u(a . b)=\frac{1}{2 \pi} \int_{0}^{2 \pi} u(a+\cos t, b+\sin t) d t \\
& =\frac{1}{2 \pi} \int_{0}^{2 \pi} e^{b+\sin t} \cos (a+\cos t) d t
\end{aligned}
$$

as claimed.
We next prove an important property of harmonic functions.
Let $\Omega$ be a region and $u$ a harmonic function on $\Omega$. If $u$ attains a maximum or a minimum inside $\Omega$, then $u$ is constant on $\Omega$.

If the region $\Omega$ is not bounded, the function $u$ need not attain a maximum or a minimum anywhere inside $\Omega$ or on its boundary. For example. $u(x . y)=x y$ is harmonic in the upper half-plane $\Omega$. It is clear that $u$ takes on arbitrarily large and arbitrarily small values as $(x, y)$ ranges in $\Omega$. So $u$ does not have

## COROLLARY 1

![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-16_369_447_772_74.jpg)
Figure 4 The rectangle in Example 2.

![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-16_368_459_1567_72.jpg)
Figure 5 Maximum and minimum values of a harmonic function.

a maximum or minimum value. However, if $\Omega$ is bounded and u is harmonic on $\Omega$ and continuous on its boundary, then it must attain its maximum and minimum values, by a well-known property of continuous functions on closed and bounded sets. Since these values cannot be attained inside $\Omega$ unless $u$ is constant, we obtain the following useful fact.

Let $\Omega$ be a bounded region and $u$ a harmonic function on $\Omega$. such that $u$ is continuous on the boundary of $\Omega$. Then $u$ attains its maximum value $M$ and its minimum value $m$ on the boundary of $\Omega$. Moreover, either $u$ is constant on $\Omega$ or $m<u(x, y)<M$ for all $(x, y)$ in $\Omega$.

Using Corollary 1, you can give an alternative proof of the uniqueness of the solution of a Dirichlet problem on a bounded region (Theorem 4, Section 12.1). We next illustrate the applications of Corollary 1 and then prove Theorem 2.

## EXAMPLE 2 Applying the maximum-minimum modulus principle Find the maximum and minimum values of $u(x, y)=x^{2}-y^{2}$ for $(x, y)$ in the rectangular region $R$ in Figure 1. where $0 \leq x \leq 2$ and $0 \leq y \leq 1$.

Solution It is straightforward to check that $u$ is harmonic for all ( $. x, y$ ). By Corollary 1, its maximum and minimum values occur on the boundary. Label the sides of $R$ as shown in Figure 4, and let $m_{j}$, respectively $M_{j}$, denote the minimum, respectively maximum, value of $u$ on side $\# j$.
On side \#1, we have $y=0$ and $0 \leq x \leq 2$. So $u(x, y)=x^{2}$, and since $0 \leq x \leq 2$, it follows that $m_{1}=0$ and $M_{1}=4$.
On side \#2, we have $x=2$ and $0 \leq y \leq 1$. So $u(x . y)=4-y^{2}$. and since $0 \leq y \leq 1$, it follows that $n_{2}=3$ and $M_{2}=4$.
On side \#3, we have $y=1$ and $0 \leq x \leq 2$. So $u(x, y)=x^{2}-1, m_{3}=-1$ and $\Lambda_{1}=3$.
On side \#4, we have $x=0$ and $0 \leq y \leq 1$. So $u(x, y)=-y^{2}, m_{4}=-1$ and $M_{4}=0$.
By comparison, we lind the smallest value of $u$ on the boundary to be $m \leq m_{3}= m_{4}=-1$. Note that $m_{3}$ and $m_{4}$ correspond to the value of $u$ at the same point $(0,1)$. Similarly the largest value of $u$ on the boundary is $M=M_{1}=M_{2}=4$, and it occurs at the point ( 2,1$)$ ). In conclusion, the maximum and minimum values of $u$ are attained at two points on the boundary. At all points inside $R$, we have

$$
-1<u(x, y)<4,
$$

as guaranteed by Corollary I (Figure 5).

## EXAMPLE 3 Applying the maximum-minimum modulus principle

Find the maximum and minimum values of $u(x, y)=e^{y} \cos x$ for ( $x, y$ ) in the rectangular region $R$, where $-\frac{\pi}{2} \leq x \leq \frac{\pi}{2}$ and $-1 \leq y \leq 1$.
Solution From Example 1, we know that $u$ is harmonic for all $(x, y)$. We thus look for the maximum and minimum values of $u$ on the boundary. Label the sides as in Figure 4, and let $m_{j}$, respectively $M_{j}$, denote the minimum, respectively maximum. value of $u$ on side $\# j$.

![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-17_499_413_387_35.jpg)
Figure 6 Maximum and minimum values of a harmonic function.

![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-17_425_452_1527_35.jpg)
Figure 7 Covering the polygonal line with finitely many disks in $\Omega$ (here $n=8$ ).

On side \#1, we have $y=-1$ and $-\frac{\pi}{2} \leq x \leq \frac{\pi}{2}$. So $u(x, y)=e^{-1} \cos x$, and it follows that $m_{1}=0$ and $M_{1}=e^{-1}$, because $0 \leq \cos x \leq 1$ for $-\frac{\pi}{2} \leq x \leq \frac{\pi}{2}$.
On sides \#2 and 4, we have $x= \pm \frac{\pi}{2}, \cos x=0$; consequently, $u=0$ on sides \#2 and 4 , and so $m_{2}=M_{2}=m_{4}=M_{4}=0$.
On side $\# 3$, we have $y=1$, hence $u(x, y)=e \cos x$, where $-\frac{\pi}{2} \leq x \leq \frac{\pi}{2}$; and so $m_{3}=0$ and $M_{3}=e$. Comparing the values on the boundary, we find the smallest value of $u$ to be 0 and the largest one to be $e$. At all points inside $R$, we have

$$
0<v(x, y)<e
$$

Unlike the situation in Example 2, here the minimum value is attained at infinitely many points on the boundary, namely on the sides $\# 2$ and 4 . The maximum value $e$ is attained at one point on the boundary ( 0,1 ) (Figure 6).

Proof of Theorem 2. It is enough to prove the statement of the theorem concerning the inaximum of $u$. Then, if we let $v=-u$, we have that $v$ is harmonic and a minimum value of $u$ corresponds to a maximum value of $v$. So suppose that $u$ attains a maximum value at ( $x_{0}, y_{0}$ ) in $\Omega$, and let us prove in two steps that $u$ must be constant on $\Omega$. In a first step, we show that $u$ is constant in the largest disk that you can place around ( $x_{0}, y_{0}$ ) in $\Omega$. Then, using this fact, we show in the second step that $u$ must be constant on $\Omega$.
Step 1: Let $C_{r}$ be any positively oriented circle in $\Omega$, with center at ( $x_{0}, y_{0}$ ). By assumption $M=u\left(x_{0}, y_{0}\right) \geq u(x, y)$ for all $(x, y)$ in $\Omega$. By the mean value theorem, we have

$$
M=u\left(x_{0}, y_{0}\right)=\frac{1}{2 \pi} \int_{0}^{2 \pi} u\left(x_{0}+r \cos t, y_{0}+r \sin t\right) d t
$$

Consider the continuous function $f(t)=u\left(x_{0}+r \cos t, y_{0}+r \sin t\right)$ for $t$ in $[0,2 \pi]$. Since $M \geq u(x, y)$, we have $f(t) \leq M$ for all $t$ in $[0,2 \pi]$. Also, the average of $f$ on the interval $[0,2 \pi]$ is equal to $M$. The only way that this can happen is for $f(t)=M$ for all $t$ in $[0,2 \pi]$ (sec Exercise 12). Thus $M \cdots u\left(x_{0}+r \cos t, y_{0}+r \sin t\right)$ for all $t$ in $[0,2 \pi]$, which shows that $u$ is constant and equal to $u\left(x_{0}, y_{0}\right)$ on $C_{r}$. Since $r$ is arbitrary, it follows that $u$ is constant and equal to $u\left(x_{0}, y_{0}\right)$ on any circle that you can fit around ( $x_{0}, y_{0}$ ) in $\Omega$, which establishes the first part of the proof.

Step 2: Let $(x, y)$ be any point in $\Omega$. Join $\left(x_{0}, y_{0}\right)$ to $(x, y)$ using a polygonal line. Cover the polygonal line by finitely many overlapping disks, $S_{0}, S_{1}, \ldots, S_{n}$, with $S_{0}$ centered at $\left(x_{0}, y_{0}\right)$, and $S_{j}$ centered at $\left(x_{j}, y_{j}\right)$, the point of intersection of $S_{j-1}$ and the polygonal line (Figure 7). (The fact that you can cover the polygonal line with finitely many disks as described is not obvious in general, but it is true because the polygonal line is closed and bounded.) The function $u$ is constant and equals the maximum value $M$ on $S_{0}$. By continuity of $u$, it follows that $u\left(x_{1}, y_{1}\right)=M$. By the previous step, it follows that $u$ is constant in the largest disk that you fit around $\left(x_{1}, y_{1}\right)$. Hence $u$ is constant and equals $M$ in $S_{1}$. Continue in this fashion to conclude that $u$ is constant and equals $M$ in $S_{2}, \ldots, S_{n}$. Thus $u(x, y)=M$, and since ( $x . y$ ) is arbitrary it follows that $u$ is constant in $\Omega$.

## Exercises 12.2

In Exercises 1-4, identify each integral as the mean value of a harmonic function at a point and then evaluate the integral using Theorem 1.

1. $\frac{1}{2 \pi} \int_{0}^{2 \pi} e^{\cos t} \cos (\sin t) d t$.
2. $\frac{1}{2 \pi} \int_{0}^{2 \pi}(3+\cos t)(1+\sin t) d t$.
3. $\frac{1}{2 \pi} \int_{0}^{2 \pi} \cos (1+\cos t) \cosh (2+\sin t) d t$.
4. $\frac{1}{2 \pi} \int_{0}^{2 \pi} \sin (1+\cos t) \sinh (2+\sin t) d t$.

In Exercists 5-8, show that $u$ is harmonic on the given region; find its maximum and minimum values; and determine where they occur in that region.
5. $u(x, y)=x^{2}-y^{2}+x y$, for $0 \leq x \leq 1,0 \leq y \leq 1$.
6. $u(. x . y)=e^{x} \cos y$, for $0 \leq x \leq 1,-\pi \leq y \leq \pi$.
7. $u(x, y)=\frac{x}{x^{2}+y^{2}}$, where $(x, y)$ belongs to the annular region $1 \leq x^{2}+y^{2} \leq 4$.
8. $u(x, y)=x y$, where $(x, y)$ belongs to the annular region $1 \leq x^{2}+y^{2} \leq 4$.
9. Let $\Omega$ be a bounded region with boundary $\Gamma$. Show that if $u$ is harmonic on $\Omega$ and $u=0$ on $\Gamma$, then $u=0$ on $\Omega$.
10. Let $\Omega$ be a bounded region with boundary $\Gamma$. Show that if $u$ and $v$ are harmonic on $\Omega$ and $u=v$ on $\Gamma$, then $u=v$ on $\Omega$. Derive the uniqueness of the solution of the Dirichlet problem on $\Omega$.
11. Review the numerical technique based on the discretization of Laplace's equation (Section 9.3). Explain why the averaging formula ((6), Section 9.3) makes sense in view of the mean value property of harmonic functions.
12. Suppose that $f(t)$ is continuous on $[a, b]$ and that $f(t) \leq M$ for all $t$ in $[a, b]$. Show that if $\frac{1}{b-a} \int_{a}^{b} f(t) d t=M$ (that is, the average of $f$ on $[a, b]$ is equal to $M$ ), then $f(t)$ is constant and equal to $M$ for all $t$ in $[a, b]$. Intuitively the result is clear. To prove it, proceed as follows.
(a) For $x$ in $[a, b]$, let

$$
F(x)=\frac{1}{b-a} \int_{a}^{x}(M-f(t)) d t
$$

Compute $F^{\prime}(x)$ and show that $F^{\prime}(x) \geq 0$ for all $x$ in $[a, b]$. Henee $F$ is increasing on $[a, b]$.
(b) Show that $F(a)=0$ and $F(b)=0$. Conclude that $F$ is identically 0 on $[a, b]$.
(c) Show that $F^{\prime}(x)=0$ on $[a, b]$ and conclude that $f(t)=M$ for all $t$ in $[a, b]$.
13. Modify the outlined proof in Exercise 12 to show the following result. Suppose that $f(t)$ is continuous on $[a, b]$ and that $f(t) \geq M$ for all $t$ in $[a . b]$. Show that if $\frac{1}{b-a} \int_{a}^{b} f(t) d t=M$. then $f(t)$ is constant and equal to $M$ for all $t$ in $[a, b]$.

### 12.3 Green's Functions

In the previous section we proved the mean value property of a harmonic function $u$ on a region $\Omega$. which says that the value of $u$ at a given point ( $x_{0}, y_{0}$ ) in $\Omega$ is obtained by averaging (or integrating and dividing by $2 \pi$ ) the values of $u$ on any circle in $\Omega$ centered at ( $x_{0}, y_{0}$ ). In this section we prove a far-reaching generalization of this fact. We show that if $u$ is harmonic inside a region $\Omega$ and continuous on the boundary of $\Omega$, then we can determine all the values of $u$ inside of $\Omega$ by integrating on the boundary of $\Omega$ the product of $u$ times a fixed function that depends only on $\Omega$ and not $u$. This magical function is the normal derivative of the so-called Green's function for the region $\Omega$, and the integral formula thus obtained solves the Dirichlet

![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-19_392_454_742_42.jpg)
Figure 1 Typical region $\Omega$ for the results of this section.

## THEOREM 1 REPRESENTATION FORMULA

![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-19_329_356_1641_38.jpg)
Figure 2 The circle $C_{r}$ encloses the problem point ( $x_{0}, y_{0}$ ) for the logarithm part $v$ and so $b$ is harmonic on $\Omega_{r}$.

problem inside $\Omega$. Variations on this formula solve Poisson's equation on $\Omega$. Concrete formulas of Green's functions for specific regions are derived in this section and Sections 12.4 and 12.7.

Throughout this section, $\Omega$ is a region with boundary $\Gamma$, where $\Gamma$ consists of simple curves $C$ (exterior boundary, positively oriented) and $C_{1}, \ldots, C_{n}$ (interior boundary, negatively oriented) (see Figure 1 for a case where $n=3$ ). For clarity's sake, as you read through this section, take $\Omega$ to be the unit disk, $\Gamma$ the positively oriented unit circle, and $C_{1}, \ldots, C_{n}$ circles of appropriate radii when present.

We start with an intermediate formula, in which the values of $u$ inside $\Omega$ are determined from its values and the values of its normal derivative on the boundary $\Gamma$.

Suppose that $u$ is harmonic inside $\Omega$ and continuous on its boundary $\Gamma$. Let $\left(x_{0}\right)$. $\left.y_{0}\right)$ be a point inside $\Omega$. Then

$$
u\left(x_{1}, y_{0}\right)=\frac{1}{2 \pi} \int_{\Gamma}\left(u \frac{\partial v}{\partial n}-v \frac{\partial u}{\partial n}\right) d s
$$

where $v(x, y)=\frac{1}{2} \ln \left(\left(x-x_{0}\right)^{2}+\left(y-y_{0}\right)^{2}\right)$.

Proof Draw a negatively oriented circle $C_{r}$ around $\left(r_{0}, y_{0}\right)$ in $\Omega$ and let $\Omega_{r}$ denote the region that consists of $\Omega$ minus the disk of radius $T$ around ( $x_{0}, y_{0}$ ) (Figure 2). The boundary of $\Omega_{r}$ is $\Gamma$ plus $C_{r}$. Both $u$ and $v$ are harmonic in $\Omega_{r}$ (remember. the only problem point for $v$ is $\left(x_{0}, y_{0}\right)$ and this point is not in $\Omega_{r}$ ). Apply Greens second identity over $\Omega_{r}$ (Theorem 3, Section 12.1) and use the fact that the left side of this identity is 0 in this case, because $\nabla^{2} u=0$ and $\nabla^{2} v=0$ on $\Omega_{r}$. Then

$$
\int_{\Gamma}\left(u \frac{\partial v}{\partial n}-v \frac{\partial u}{\partial n}\right) d s+\int_{C_{r}}\left(u \frac{\partial u}{\partial n}-v \frac{\partial u}{\partial n}\right) d s=0
$$

Thus

$$
\int_{\Gamma^{\prime}}\left(u \frac{\partial v}{\partial n}-v \frac{\partial u}{\partial n}\right) d s=-\int_{C_{r}^{\prime}}\left(u \frac{\partial v}{\partial n}-v \frac{\partial u}{\partial n}\right) d s
$$

and so the theorem will follow if we can show that the right side of the last equality is $2 \pi u\left(x_{0}, y_{0}\right)$. Since $C_{r}$ is negatively oriented, we have $-\int_{C_{r}}=\int_{-C_{r}}$, where $-C_{r}$ is now positively oriented. Parametrize $-C_{r}$ by $x(t)=x_{0}+r \cos t, y(t)=y_{0}+r \sin t$, $0 \leq t \leq 2 \pi, d s=r d t, v=\ln r, \frac{\partial v}{\partial n}=\frac{1}{r}$ (Proposition 2, Section 12.2). Then

$$
\begin{aligned}
\int_{-C_{r}}\left(u \frac{\partial v}{\partial n}-r \frac{\partial u}{\partial n}\right) d s & =\overbrace{\int_{0}^{2 \pi} u\left(x_{0}+r \cos t, y_{0}+r \sin t\right) d t}^{=2 \pi u\left(x_{0}, y_{0}\right)}-\ln r \overbrace{\int_{C} \frac{\partial u}{\partial n} d s}^{=0} \\
& =2 \pi u\left(x_{0}, y_{0}\right)
\end{aligned}
$$

where we have used the mean value property of harmonic functions (Theorem 1. Section 12.2), and the compatibility property (Example 5, Section 12.1).

Next, we modify the representation formula in Theorem 1 in such a way that the resulting line integral does not involve the normal derivative of $u$. For this purpose, suppose that there is a harmonic function $h$ on $\Omega$ such that $h=-v$ on $\Gamma$, where $v$ is as in Theorem 1. Applying Green's second identity with $u$ and $h$ (both are harmonic on $\Omega$ ), we get

$$
0=\int_{\Gamma}\left(u \frac{\partial h}{\partial n}-h \frac{\partial u}{\partial n}\right) d s
$$

Dividing by $2 \pi$ and using $h=-v$ on $\Gamma$, we get

$$
0=\frac{1}{2 \pi} \int_{\Gamma}\left(u \frac{\partial h}{\partial n}+v \frac{\partial u}{\partial n}\right) d s
$$

Adding this identity to the representation formula in Theorem 1, we obtain

$$
u\left(x_{0}, y_{0}\right)=\frac{1}{2 \pi} \int_{\Gamma} u \frac{\partial}{\partial n}(h+v) d s
$$

So far ( $x_{0}, y_{0}$ ) is fixed in $\Omega$, and $v$ and $h$. clearly depend on ( $x_{0}, y_{0}$ ). Let $\left(x_{0}, y_{0}\right)$ vary in $\Omega$ and suppose that for each $\left(x_{0}, y_{0}\right)$ we can find $h\left(x, y, x_{0}, y_{0}\right)$, so that (1) holds. Write

$$
G\left(x, y, x_{0}, y_{0}\right)=\overbrace{\frac{1}{2} \ln \left(\left(x-x_{0}\right)^{2}+\left(y-y_{0}\right)^{2}\right)}^{v\left(x, y, x_{0}, y_{0}\right)}+h\left(x, y, x_{0}, y_{0}\right) .
$$

The function $G$ is called Green's function for the region $\Omega$. Because of (1) we have the following important result.

THEOREM 2 SOLUTION OF DIRICHLET PROBLEM

Suppose that $u$ is harmonic on $\Omega$ and continuous on its boundary $\Gamma$. Then for $\left(x_{0}, y_{0}\right)$ in $\Omega$, we have

$$
u\left(x_{0}, y_{0}\right)=\frac{1}{2 \pi} \int_{\Gamma} u(x, y) \frac{\partial G}{\partial n}\left(x, y, x_{0}, y_{0}\right) d s
$$

where $G$ is Green's function for $\Omega$.

## THEOREM 3 PROPERTIES OF GREEN'S FUNCTION

![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-21_349_342_1311_22.jpg)
Figure $3 G \approx v+h$, where $|h| \leq M$ in $D_{R}$ and $v$ tends to $-\infty$ at $\left(x_{0} . y_{0}\right)$. As a result $G$ tends to $-\infty$ at ( $x_{0}, y_{0}$ ).

Formula (3) solves the Dirichlet problem on $\Omega$. The trouble is that Green's functions are not easy to compute for arbitrary regions, and even when they are known, the integral (3) is still difficult to evaluate. Nevertheless, formula (3) offers many advantages. In the following sections, we will compute it explicitely for important regions such as disks, half-planes, and sectors. Furthermore, the same ideas that we used to derive (3) can be used to solve other important equations, such as Poisson's equation and Neumann prollems.

We now list fundamental properties of Green's function for future reference.

Let $\Omega$ be a region with boundary $\Gamma$, and let $G$ be its Green's function as in (2). Then
(i) $G\left(x, y, x_{0}, y_{0}\right)$ is a harmonic function of $(x, y)$ in $\Omega$ minus $\left(x_{0}, y_{0}\right)$. Harmonicity fails at ( $x_{0}, y_{0}$ ) due to the logarithmic part $v$.
(ii) $G\left(x, y, x_{0}, y_{0}\right)=0$ for all $(x, y)$ on the boundary $\Gamma$.
(iii) $G\left(x, y, x_{0}, y_{0}\right) \leq 0$ for all $(x, y)$ in $\Omega$ minus $\left(x_{0}, y_{0}\right)$.
(iv) (uniqueness property) Green's function is uniquely determined by the region $\Omega$.
(v) (symmetry property) $G\left(x, y, x_{0}, y_{0}\right)=G\left(x_{0}, y_{0}, x, y\right)$ for all $\left(x_{0}, y_{0}\right)$ and ( $x, y$ ) in $\Omega$.

Proof Properties (i) and (ii) are immediate from the definition of Green's function. Property (v) is not obvious but its proof is based on ideas that we have used throughout this section. We outline it in the exercises. (Another proof, based on conformal mappings, is given in Section 12.7, following Theorem 3.) Let us prove (iii) and (iv), starting with (iv). Write $G=v+h$ as in (2). If $Q=v+q$ is another Green's function for $\Omega$, then because $Q=0$ on $\Gamma$, it follows that $q=-v$ on $\Gamma$. But, $h=-v$ on $\Gamma$, so $h=q$ on $\Gamma$. Since both $h$ and $q$ are harmonic, it follows that $h=q$ on $\Omega$, by Theorem 4, Section 12.1. Hence $G=Q$ on $\Omega$.

To prove (iii), again write $G=v+h$ as in (2). Fix a closed disk $D_{R}$ centered at ( $x_{0}, y_{0}$ ) and contained in $\Omega$. Since $h$ is harmonic on $\Omega$, it is continuous and hence bounded in $D_{R}$, say $\left|h\left(x, y, x_{0}, y_{0}\right)\right| \leq M$ on $D_{R}$. Now, $v$ tends to $-\infty$ as $(x . y)$ approaches $\left(x_{0}, y_{0}\right)$. So we can find $0<r_{0}<R$ such that $v\left(x, y, x_{0}, y_{0}\right)<2 M$ on $C_{T}$ for all $0<r \leq r_{0}<R$ (see Figure 3). Hence $G\left(x, y, x_{0}, y_{0}\right) \leq-M$ on $C_{r}$. because $G=h+v, v\left(x, y, x_{0}, y_{0}\right)<-2 M$ and $\left|h\left(x, y, x_{0}, y_{0}\right)\right| \leq M$ on $C_{r}$. Denote the region $\Omega$ minus the disk of radius $r$ centered at ( $x_{0}, y_{0}$ ) by $\Omega_{r}$. The boundary of $\Omega_{r}$ consists of $\Gamma$ and $C_{r}$. The function $G$ is harmonic in $\Omega_{r}$ and we just proved that it is $\leq 0$ on its boundary. By the maximum principle for harmonic functions, it follows that $G \leq 0$ on $\Omega_{r}$. Since this is true for all $0<r \leq r_{0}$, letting $r \rightarrow 0$, we see that $G \leq 0$ on $\Omega$ minus ( $x_{0}, y_{0}$ ). Hence (iii) holds.

## Solution of Poisson's Equation

We consider Poisson equation on $\Omega$ and solve this important equation using ideas similar to those of the proof of Theorem 2.

THEOREM 4 SOLUTION OF POISSON'S EQUATION WITH ZERO BOUNDARY DATA

Let $\Omega$ be a region with boundary $\Gamma$ as in Theorem 1. Let $f(x, y)$ be a function on $\Omega$ and suppose that $u$ is a solution of Poisson's equation on $\Omega$.

$$
\nabla^{2} u(x, y)=f(x, y) . \quad(x, y) \text { in } \Omega .
$$

such that $u=0$ on the boundary $\Gamma$. Then, for all $\left(x_{0}, y_{0}\right)$ in $\Omega$.

$$
u\left(x_{0}, y_{0}\right)=\frac{1}{2 \pi} \iint_{\Omega} f(x, y) G\left(x, y, x_{0}, y_{0}\right) d x d y
$$

where $G$ is Green's function for $\Omega$.
Proof If $u$ is a solution, then $\nabla^{2} u(x, y)=f(x, y)$ on $\Omega$, and so

$$
\iint_{\Omega} f(x, y) G\left(x, y, x_{0}, y_{0}\right) d x d y=\iint_{\Omega} \nabla^{2} u(x, y) G\left(x, y, x_{0}, y_{0}\right) d x d y
$$

Let $C_{r}$ be a negatively oriented circle around ( $x_{0}, y_{0}$ ) and let $\Omega_{r}$ be $\Omega$ minus $D_{r}$. the closed disk of radius $r$ centered at ( $x_{0}, y_{0}$ ) (Figure 2). The boundary of $\Omega_{r}$ consists of $\Gamma$ plus the negatively oriented circle $C_{r}$. Apply Green's second identity in $\Omega_{r}$, use that $u=0$ on $\Gamma, G$ is harmonic in $\Omega_{T}$ and $G=0$ on $\Gamma$, and get

$$
\begin{aligned}
& -\iint_{\Omega_{r}} G\left(x, y, x_{0}, y_{0}\right) \nabla^{2} u(x, y) d x d y \\
& \quad=\int_{C_{r}} u(x, y) \frac{\partial G}{\partial n}\left(x, y, x_{0}, y_{0}\right) d s-\int_{C_{r}} G\left(x, y, x_{0}, y_{0}\right) \frac{\partial u}{\partial n}(x, y) d s
\end{aligned}
$$

To complete the proof of the theorem, we let $r \rightarrow 0$ in (6) and establish the following three limits:

$$
\begin{gathered}
\lim _{r \rightarrow 0}-\iint_{\Omega} G\left(x, y, x_{0}, y_{0}\right) \nabla^{2} u(x, y) d x d y \\
=-\iint_{\Omega} G\left(x, y, x_{0}, y_{0}\right) \nabla^{2} u(x, y) d x d y \\
\lim _{r \rightarrow 0} \int_{C_{r}} u(x, y) \frac{\partial G}{\partial n}\left(x, y, x_{0}, y_{0}\right) d s=-2 \pi u\left(x_{0} . y_{0}\right) \\
\lim _{r \rightarrow 0}-\int_{C_{r}} G\left(x, y, r_{0}, y_{0}\right) \frac{\partial u}{\partial n}(x, y) d s=0
\end{gathered}
$$

We shall prove (9) and leave the proofs of (7) and (8) to the exercises (with copious hints). Write $G\left(x, y, x_{0}, y_{0}\right)=h\left(x, y, x_{0}, y_{0}\right)+\frac{1}{2} \ln \left(\left(x-x_{0}\right)^{2}+\left(y-y_{0}\right)^{2}\right)$, where $h\left(x, y, x_{0}, y_{0}\right)$ is harmonic, hence continuous, and hence bounded by a constant $M$ on $D_{r}$ (in particular, $h$ is bounded by $M$ on $C_{r}$ ). Also, since $u$ has continuous partial derivatives in $\Omega . \frac{\partial u}{\partial n}$ is continuous on $D_{r}$ and bounded on $D_{r}$ (say, $\left|\frac{\partial u}{\partial n}\right| \leq A$ on $D_{r}$ ). Furthermore, for $(r \cdot y)$ on $C_{r}$, we have $\left|v\left(x, y, x_{0}, y_{0}\right)\right|=|\ln r|$; hence $\left|G\left(x, y, x_{0}, y_{0}\right) \frac{i_{n}}{\partial n}\right| \leq(M+|\ln r|), A$. and so

$$
\begin{aligned}
\left|\int_{C_{r}} G\left(x, y_{0}, x_{0}, y_{0}\right) \frac{\partial u}{\partial n}(x, y) d s\right| & \leq(M+|\ln r|) A \int_{C_{r}} d s \\
& =2 \pi r(M+|\ln r|) A \rightarrow 0, \text { as } r \rightarrow 0
\end{aligned}
$$

which completes the proof of (9). $\square$

To solve the general Poisson equation with arbitrary boundary values, we combine the solutions of the Dirichlet problem and Poisson's equation with zero boundary values, as illustrated by Figure 4. We state the result in a theorem and omit the proof which is similar to a proof that we gave in Section 3.9 for the Poisson problem on a rectangle.

## THEOREM 5 GENERAL SOLUTION OF POISSON'S EQUATION

With the notation of Theorem 4, suppose that $u$ is a solution of Poisson's equation (4) with boundary condition $u(x, y)=g(x, y)$ for all $(x, y)$ on $\Gamma$. Then, for all ( $x_{0}, y_{0}$ ) in $\Omega$.

$$
\begin{aligned}
u\left(x_{0}, y_{0}\right)= & \frac{1}{2 \pi} \iint_{\Omega} f(x, y) G\left(x, y, x_{0}, y_{0}\right) d x d y \\
& +\frac{1}{2 \pi} \int_{\Gamma} g(x, y) \frac{\partial G}{\partial n}\left(x, y, x_{0}, y_{0}\right) d s
\end{aligned}
$$

where $G$ is Green's function for $\Omega$.

Figure 4 Decomposition of a general Poisson problem into two simpler subproblems.
![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-23_439_1277_1057_500.jpg)

## Green's Function, Method of Eigenfunction Expansions

Recall that we have solved Poisson's equation on regions such as a rectangle or a disk, by using the eigenfunction expansion method. The solution in each case is given by an infinite or doubly infinite series. The plan now is to identify Green's function in these formulas by comparing them with (5). This will yield Green's functions on a rectangle and a disk in a double series form. Even though this form does not match (2), it does serve to illustrate some properties of Green's functions. (In the next section we will construct Green's function on a disk and obtain a formula that matches (2).)

Figure 5 Poisson problem on a rectangle, with zero boundary values.
Figure 5 Poisson problem on a rectangle, with zero boundary values.

## EXAMPLE 1 Green's function for a rectangle

Consider Poisson's equation $\nabla^{2} u(x, y)=f(x, y)$ on all $a \times b$ rectangle $R$ with 0 boundary values, as illustrated in Figure 5. From Section 3.9, we have, for any

![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-24_352_468_544_65.jpg)
Figure 6 Green's function for a $1 \times 1$-rectangle at $\left(x_{0}, y_{0}\right)= \left(\frac{1}{2}, \frac{1}{2}\right)$, drawn using a partial sum of (10) with $m=n=$ 40.

![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-24_543_449_1452_72.jpg)
Figure 7 Poisson's equation in a disk of radius $\alpha$ and zero boundary values.

( $x_{0} \cdot y_{0}$ ) in $R$,

$$
u\left(x_{0}, y_{0}\right)=\sum_{n=1}^{\infty} \sum_{m=1}^{\infty} E_{m n} \sin \frac{m \pi x_{0}}{a} \sin \frac{n \pi y_{0}}{b},
$$

where

$$
E_{m n}=\frac{-4}{a b \lambda_{m n}} \int_{0}^{b} \int_{0}^{a} f(x, y) \sin \frac{m \pi x}{a} \sin \frac{n \pi y}{b} d x d y
$$

and $\lambda_{m n}=\pi^{2}\left[\left(\frac{m}{a}\right)^{2}+\left(\frac{n}{b}\right)^{2}\right](m, n-1,2, \ldots)$. Substituting $E_{m n}$ by its value in the formula for $u$, and then interchanging the sum and integral signs, we get

$$
\begin{aligned}
& u\left(x_{0}, y_{0}\right)= \\
& \quad \int_{0}^{b} \int_{0}^{a} f(x, y)\left(\sum_{n=1}^{\infty} \sum_{m=1}^{\infty} \frac{-4}{a b \lambda_{m n}} \sin \frac{m \pi x}{a} \sin \frac{n \pi y}{b} \sin \frac{m \pi x_{0}}{a} \sin \frac{n \pi y_{0}}{b}\right) d x d y
\end{aligned}
$$

Comparing this formula with (5), we conclude that Green's function for the rectangle is

$$
G\left(x, y, x_{0} . y_{0}\right)=\frac{-8}{a b \pi} \sum_{n=1}^{\infty} \sum_{m=1}^{\infty} \frac{\sin \frac{m \pi x}{a} \sin \frac{n \pi y}{b} \sin \frac{m \pi x_{0}}{a} \sin \frac{n \pi y_{0}}{b}}{\left(\frac{m}{a}\right)^{2}+\left(\frac{n}{b}\right)^{2}} .
$$

For any given ( $x_{0}, y_{0}$ ) in $R$, it can be shown that the series converges conditionally for all $(x, y) \neq\left(x_{0}, y_{0}\right)$ in $R$ and diverges for $(x, y)=\left(x_{0}, y_{0}\right)$. This fact is illustrated in Figure 6. Some properties of Green's function that are listed in Theorem 3 can be verified directly by considering (10) (see the exercises). $\square$

## EXAMPLE 2 Green's function for a disk

We use polar coordinates for convenience. Consider Poisson's equation $\nabla^{2} u(r, \theta)= f(r, \theta)$ on a disk $D$ of radius $a>0$, with 0 boundary values, as illustrated in Figure 7. Using the results of Section 4.6, and then comparing with (5), we find that for ( $r_{0}, \theta_{0}$ ) in $D$ :

$$
u\left(r_{0}, \theta_{0}\right)=\frac{1}{2 \pi} \int_{0}^{a} \int_{0}^{2 \pi} G\left(r, \theta, r_{0}, \theta_{0}\right) f(r, \theta) r d r d \theta
$$

where

$$
\begin{aligned}
& G\left(r, \theta, r_{0}, \theta_{0}\right)=-2 \sum_{n=1}^{\infty} \frac{J_{0}\left(\lambda_{0 n} r\right) J_{0}\left(\lambda_{0 n} r_{0}\right)}{\alpha_{0 n}^{2} J_{1}^{2}\left(\alpha_{0 n}\right)} \\
& \quad-4 \sum_{m=1}^{\infty} \sum_{n=1}^{\infty} \frac{J_{m}\left(\lambda_{m n} r\right) J_{m}\left(\lambda_{m n} r_{0}\right)}{\alpha_{m n}^{2} J_{m+1}^{2}\left(\alpha_{m n}\right)}\left(\cos m \theta \cos m \theta_{0}+\sin m \theta \sin m \theta_{0}\right) \\
& \quad=-2 \sum_{n=1}^{\infty} \frac{J_{0}\left(\lambda_{0 n} r\right) J_{0}\left(\lambda_{0 n} r_{0}\right)}{\alpha_{0 n}^{2} J_{1}^{2}\left(\alpha_{0 n}\right)}-4 \sum_{m=1}^{\infty} \sum_{n=1}^{\infty} \frac{J_{m}\left(\lambda_{m n} r\right) J_{m}\left(\lambda_{m n} r_{0}\right)}{\alpha_{m n}^{2} J_{m+1}^{2}\left(\alpha_{m n}\right)} \cos m\left(\theta-\theta_{0}\right)
\end{aligned}
$$

where $\lambda_{m n}=\frac{\alpha_{m n}}{a}$ and $\alpha_{m n}$ is the $n$th positive zero of the Bessel function $J_{m}$. The details of the derivation are straightforward and are left to the exercises. An

THEOREM 6 POISSON'S
EQUATION WITH A DIRAC FUNCTION
alternative simpler formula for Green's function for the disk is derived in the next section.

## Green's Function and the Dirac Delta Function

There is a concrete description of Green's function, $G\left(x . y, x_{0}, y_{0}\right)$, as the steady-state solution of a heat problem on a plate $\Omega$ with a heat source at ( $x_{0}, y_{0}$ ), where the boundary of $\Omega$ is kept at 0 temperature. More precisely, we have the following result.

For fixed $\left(x_{0}, y_{0}\right)$ in $\Omega, \frac{1}{2 \pi} G\left(x, y, x_{0}, y_{0}\right)$ is a solution of the following Poisson equation, with zero boundary condition:

$$
\begin{aligned}
\nabla^{2} u & =\delta_{\left(x_{0}, y_{0}\right)}(x, y), \quad(x, y) \text { in } \Omega \\
u(x, y) & =0 \text { for all }(x, y) \text { on the boundary of } \Omega .
\end{aligned}
$$

where $\delta_{\left(x_{0}, y_{0}\right)}(x, y)$ is the two dimensional delta Dirac function.
Before we prove the theorem, we explain a few facts about the two dimensional Dirac function. This function is defined in terms of the one dimensional Dirac function by

$$
\delta_{\left(x_{0}, y_{0}\right)}(x, y)=\delta_{x_{0}}(x) \delta_{y_{0}}(y)
$$

Consequently, if $f(x, y)$ is a function and $D$ is a subset of the plane, then

$$
\iint_{D} f(x, y) \delta_{\left(x_{0}, y_{0}\right)}(x, y) d x d y= \begin{cases}f\left(x_{0}, y_{0}\right) & \text { if }\left(x_{0}, y_{0}\right) \text { is in } D \\ 0 & \text { otherwise. }\end{cases}
$$

To explain what we mean by a solution of (11), we recall the definition of equality between two generalized functions from Section 7.8. For $u(x, y)$ to be a solution of (11), we must show that if $\phi(x, y)$ is any (test) function, then

$$
\iint_{\Omega} \phi(x, y) \nabla^{2} u d x d y=\iint_{\Omega} \phi(x, y) \delta_{\left(x_{0}, y_{0}\right)}(x, y) d x d y=\phi\left(x_{0}, y_{0}\right)
$$

Proof of Theorem 6. That $G$ satisfies (12) follows from Theorem 3(ii). We now show that (14) holds when $u(x, y)=\frac{1}{2 \pi} G\left(x, y, x_{0}, y_{0}\right)$. Letting $\phi(x, y)$ be any (test) function, we must show that

$$
\frac{1}{2 \pi} \iint_{\Omega} \phi(x, y) \nabla^{2} G\left(x, y, x_{0}, y_{0}\right) d x d y=\phi\left(x_{0}, y_{0}\right)
$$

where in the double integral, the Laplacian is computed with respect to ( $x, y$ ). But since $G$ is symmetric, we can write the Laplacian inside the double integral with respect to $\left(x_{0}, y_{0}\right)$, instead of $(x, y)$, without changing the values of the integrand. But then we can pull the Laplacian symbol outside the integral and write

$$
\frac{1}{2 \pi} \iint_{\Omega} \phi(x, y) \nabla^{2} G\left(x, y, x_{0}, y_{0}\right) d x d y=\nabla^{2}\left(\frac{1}{2 \pi} \iint_{\Omega} \phi(x, y) G\left(x, y, x_{0} . y_{0}\right) d x d y\right)
$$

By Theorem 4, the function defined by the clouble integral on the right side solves Poisson's equation $\nabla^{2} u=\infty$. So its Laplacian (with respect to $\left(x_{0}, y_{0}\right)$ ) is equal to $\phi\left(x_{0}, y_{0}\right)$, and (15) follows.

Many examples of Green's functions will be derived in the the next section and Section 12.7.

## Exercises 12.3

In Exercises 1-8, evaluate the given expression without computing. Appeal to various results from this section and explain how you are using them. In all cases, if not otherwise specified, take $\Omega$ to be a region with boundary $\Gamma$, as in Theorem 1 , ( $x_{0}, y_{0}$ ) a point in $\Omega$, and $G$ Green's function for $\Omega$.

1. $\int_{\Gamma} G\left(x, y, x_{\cup}, y_{0}\right) d s$.
2. $\int_{\Gamma} f(x, y) G\left(x, y, x_{0}, y_{0}\right) d s, f(x, y)$ an arbitrary function defined on $\Gamma$.
3. $\int_{\Gamma} \frac{\partial}{\partial n} G\left(x, y, x_{0}, y_{0}\right) d s$.
4. $\int_{\Gamma} x y \frac{\partial}{\partial n} G\left(x, y, x_{0}, y_{0}\right) d s$.
5. $\int_{\Gamma} x \frac{\partial}{\partial n} G\left(x, y, \frac{1}{2}, \frac{1}{3}\right) d s$, where $\Omega$ is the unit disk and $\Gamma$ its positively oriented boundary.
6. $\int_{\Gamma}\left(x^{2}-y^{2}\right) \frac{\partial}{\partial n} G\left(x, y, \frac{1}{2}, \frac{1}{3}\right) d s$.
7. $\nabla^{2}\left(\iint_{\Omega} G\left(x, y, x_{0}, y_{0}\right) d x d y\right)$.
8. $\nabla^{2}\left(\iint_{\Omega}\left(2 x+3 y^{3}\right) G\left(x, y, x_{0}, y_{0}\right) d y\right)$.
9. $\nabla^{2}\left(\iint_{\Omega} x^{2} y^{3} G\left(x, y . x_{0}, y_{0}\right) d x d y\right)$.
10. $\nabla^{2}\left(\iint_{\Omega} f(x, y) G\left(x, y, x_{0}, y_{0}\right) d x d y\right)$.
11. Derive Gauss's mean value property (Theorem 1, Section 12.2) from the representation formula in Theorem 1.
12. (a) Verify (i) of Theorem 3 for Green's function for a rectangle (10). (Assume that you can interchange the derivatives and the sums.)
(b) Verify (ii) and (v) of Theorem 3 for Green's function for a rectangle (10).
13. Verify (i) of Theorem 3 for Green's function for a disk in Example 2. (Assume that you can interchange the derivatives and the sums.)
14. Verify (ii) and (v) of Theorem 3 for Green's function for a disk in Example 2.
15. In the notation of Theorem 2, show that

$$
\frac{1}{4 \pi} \int_{\Gamma} \frac{\partial}{\partial n} \ln \left(\left(x-x_{0}\right)^{2}+\left(y-y_{0}\right)^{2}\right) d s=1
$$

[Hint: Take $u=1$ and use (2).]
16. Derive the solution of the Dirichlet problem on a rectangle in Section 3.8, starting with Green's function (10) and using Theorem 2. In computing the normal derivative of Green's function, you have to distinguish four cases, depending on the side of the rectangle.
17. Reverse the steps in the proof in Example 1 and show how you would solvc Poisson's equation with zero boundary values on a rectangle starting with Green's function (10) and using Theorem 4.
18. Supply more details in Example 2 showing clearly how to obtain Green's function from the results of Section 4.6.
19. Solve the Poisson problem in the plane $\nabla^{2} u=\delta_{(0,0)}(x, y)$.

In what follows, we use the notation of Theorem 1. Unless otherwise specified, ( $x_{0}, y_{0}$ ) denotes a point in $\Omega$, and $C_{r}$ is a positively oriented circle, contained in $\Omega$, with center ( $x_{0}, y_{0}$ ) and radius $r>0$. The Green's function for $\Omega$ is denoted by $G$. Hence $G=h+v$, where, $b y(2), v(x, y)=\frac{1}{2} \ln \left(\left(x-x_{0}\right)^{2}+\left(y-y_{0}\right)^{2}\right)$ and $h$ is harmonic on $\Omega$ and equals $v$ on $\Gamma$.
20. Suppose that $u$ is continuous (not necessarily harmonic) on an open disk around ( $x_{0}, y_{0}$ ) in $\Omega$. Show that

$$
\lim _{r \rightarrow 0} \int_{C_{r}} u \frac{\partial v}{\partial n} d s=2 \pi u\left(x_{0}, y_{0}\right)
$$

[Hint: From Proposition 1, Section 12.2, $\int_{C_{r}} u \frac{\partial v}{\partial n} d s=\int_{0}^{2 \pi} u\left(x_{0}+r \cos \theta_{s} y_{0}+\right. r \sin \theta) d \theta=\phi(r)$, where $\phi(r)$ is continuous. What is $\phi(0) ?]$
21. Suppose that $u$ is continuous and $h$ is harmonic on an open disk around ( $x_{0}, y_{0}$ ) in $\Omega$. Show that

$$
\lim _{r \rightarrow 0} \int_{C_{r}} u \frac{\partial h}{\partial n} d s=0
$$

[Hint: Both $|u|$ and $\left|\frac{\partial h}{\partial n}\right|$ are bounded near ( $x_{0}, y_{0}$ ), say by $M$. If $I_{r}$ denotes the integral in question, then $\left|I_{r}\right| \leq 2 \pi M r \rightarrow 0$ as $r \rightarrow 0$.]
22. A useful limit. Suppose that $u$ is continuous (not necessarily harmonic) on an open disk around $\left(x_{0}, y_{0}\right)$ in $\Omega$. Show that

$$
\lim _{r \rightarrow 0} \int_{C_{r}} u \frac{\partial G}{\partial n}\left(x, y, x_{0}, y_{0}\right) d s=2 \pi u\left(x_{0}, y_{0}\right)
$$

[Hint: Combine the previous two exercises.]
23. Another useful limit. Suppose that $u$ is continuous (not necessarily harmonic) on an open disk around ( $x_{0}, y_{0}$ ) in $\Omega$. Show that

$$
\lim _{r \rightarrow 0} \int_{C_{r}} u(x, y) G\left(x, y, x_{0}, y_{0}\right) d s=0
$$

[Hint: Repeat the end of the proof of Theorem 4 with minor modifications.]
24. Proof of (8). Prove (8) by appealing to Exercise 22. (Just note the difference in the orientation of the curves in the integrals.)

![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-28_331_343_761_74.jpg)
Figure 8 for Exercise 26.

25. Proof of (7). Justify the following steps:

$$
\begin{gathered}
\left|\iint_{\Omega_{r}} G\left(x, y, x_{0}, y_{0}\right) f(x, y) d x d y-\iint_{\Omega} G\left(x, y, x_{0}, y_{0}\right) f(x, y) d x d y\right| \\
=\left|\iint_{D_{r}} G\left(x, y, x_{0}, y_{0}\right) f(x, y) d x d y\right| \\
\leq \iint_{D_{r}}\left|h\left(x, y, x_{0}, y_{0}\right) f(x, y)\right| d x d y \\
+\iint_{D_{r}}\left|\frac{1}{2} \ln \left(\left(x-x_{0}\right)^{2}+\left(y-y_{0}\right)^{2}\right) f(x, y)\right| d x d y \\
\leq A \iint_{D_{r}} d x d y+B \iint_{D_{r}} \frac{1}{2}\left|\ln \left(\left(x-x_{0}\right)^{2}+\left(y \quad y_{0}\right)^{2}\right)\right| d x d y \\
=A r^{2} \pi+B \int_{0}^{2 \pi} \int_{0}^{r} \rho|\ln \rho| d \rho d \theta
\end{gathered}
$$

Evaluate the last integral and show that the resulting expression on the right side tends to 0 as $r \rightarrow 0$.
26. Proof of Theorem 3(v). Let $\boldsymbol{a}=\left(x_{1}, y_{1}\right)$ and $\boldsymbol{b}=\left(x_{2}, y_{2}\right)$ be any two points in $\Omega$. Follow the outlined steps to show that $G(\boldsymbol{a}, \boldsymbol{b})=G(\boldsymbol{b}, \boldsymbol{a})$.
(a) In $\Omega$, draw small negatively oriented circles $C_{r}(a)$ and $C_{r}(b)$ around $\boldsymbol{a}$ and $b$, respectively, with radii $r$. Let $\Omega_{r}$. denote the region $\Omega$ minus the closed disks $D_{r}(\boldsymbol{a})$ and $D_{r}(b)$, and let $\Gamma_{r}$ denote the boundary of $\Omega_{r}$ (Figure 8). Show that

$$
\int_{\Gamma_{r}}\left(G(x, y, \boldsymbol{a}) \frac{\partial}{\partial n} G(x, y, \boldsymbol{b})-G(x, y, \boldsymbol{b}) \frac{\partial}{\partial n} G(x, y, \boldsymbol{a})\right) d s=0
$$

(b) Using Theorem 3(ii), conclude that

$$
\begin{aligned}
\int_{C_{r}(\boldsymbol{a})} & \left(G(x, y, \boldsymbol{a}) \frac{\partial}{\partial n} G(x, y, \boldsymbol{b})-G(x, y, \boldsymbol{b}) \frac{\partial}{\partial n} G(x, y, \boldsymbol{a})\right) d s \\
& +\int_{C_{r}(\boldsymbol{b})}\left(G(x, y, \boldsymbol{a}) \frac{\partial}{\partial n} G(x, y, \boldsymbol{b})-G(x, y, \boldsymbol{b}) \frac{\partial}{\partial n} G(x, y, \boldsymbol{a})\right) d s=0
\end{aligned}
$$

(c) Using Exercises 22 and 23, show that

$$
\begin{gathered}
\lim _{r \rightarrow 0} \int_{C_{r}(\boldsymbol{a})} G(x, y, \boldsymbol{a}) \frac{\partial}{\partial n} G(x, y, \boldsymbol{b}) d s=0 \\
\lim _{r \rightarrow 0}-\int_{C_{r}(\boldsymbol{a})} G(x, y, \boldsymbol{b}) \frac{\partial}{\partial n} G(x, y, \boldsymbol{a}) d s=2 \pi G(\boldsymbol{a}, \boldsymbol{b}) \\
\lim _{r \rightarrow 0} \int_{C_{r}(\boldsymbol{b})} G(x, y, \boldsymbol{a}) \frac{\partial}{\partial n} G(x, y, \boldsymbol{b}) d s=-2 \pi G(\boldsymbol{b}, \boldsymbol{a}) \\
\lim _{r \rightarrow 0}-\int_{C_{r}(\boldsymbol{b})} G(x, y, \boldsymbol{b}) \frac{\partial}{\partial n} G(x, y, \boldsymbol{a}) d s=0
\end{gathered}
$$

(d) Conclude from (b) and (c) that $G(\boldsymbol{a}, \boldsymbol{b})=G(\boldsymbol{b}, \boldsymbol{a})$.

### 12.4 Green's Functions for the Disk and the Upper Half-Plane

Green's function for the unit disk was computed in the previous section using the method of eigenfunction expansions and was obtained in the form of a double series that involves cosine, sine and Bessel functions. In this section we apply the so-called method of images, which uses basic facts from plane geometry about the circle and gives a much simpler derivation of

![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-29_403_394_622_31.jpg)
Figure 1 The point $A^{*}$ is such that for all points $P$ on $C_{R}$, we have $A P=k \cdot A^{*} P$ for some $k>0$.

![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-29_397_379_1541_29.jpg)
Figure 2 The point $A^{*}$ is the image of $A$ by the Steiner inversion. $A^{*}$ is on the ray $O A$, such that $O A \cdot O A^{*}=R^{2}$.

Green's function. These geometric ideas apply as well on other regions and yield concrete formulas for Green's functions.

Throughout this section, let $D_{R}$ denote a disk centered at the origin with radius $R>0$, and $C_{R}$ its positively oriented boundary. Recall from (2) of the previous section that Green's function is of the form

$$
G\left(x, y, x_{0}, y_{0}\right)=\overbrace{\frac{1}{2} \ln \left(\left(x-x_{0}\right)^{2}+\left(y-y_{0}\right)^{2}\right)}^{v\left(x, y, x_{0}, y_{0}\right)}+h\left(x, y, x_{0}, y_{0}\right)
$$

where $h$ is harmonic on $D_{R}$ and $h\left(x, y, x_{0}, y_{0}\right)=-v\left(x, y, x_{0}, y_{0}\right)$ for all ( $x . y$ ) on $C_{R}$. So the first half of the formula for $G$ is known, and to determine the second half, we must find a harmonic function $h$ on $D_{R}$ that equals $-v$ on $C_{R}$. Thus $h$ is the solution of a particular Dirichlet problem on $D_{R}$, with boundary condition $h=-v$ on $C_{R}$. Suppose for a moment that there is a point $A^{*}=\left(x_{0}^{*}, y_{0}^{*}\right)$ outside $D_{R}$ such that the distance from $A=\left(x_{0}, y_{0}\right)$ to any point $P=(x, y)$ on $C_{R}$ is proportional to the distance from ( $x_{0}^{*}, y_{0}^{*}$ ) to $(x, y)$ (Figure 1). That is, $\left(x_{0}^{*}, y_{0}^{*}\right)$ is such that there is a constant $k>0$ with

$$
\sqrt{\left(x-x_{0}\right)^{2}+\left(y-y_{0}\right)^{2}}=k \sqrt{\left(x-x_{0}^{*}\right)^{2}+\left(y-y_{0}^{*}\right)^{2}}
$$

for all $(x, y)$ on $C_{R}$. Given such a point $\left(x_{0}^{*}, y_{0}^{*}\right)$, define

$$
\begin{aligned}
h\left(x, y, x_{0}, y_{0}\right) & =-\ln \left(k \sqrt{\left(x-x_{0}^{*}\right)^{2}+\left(y-y_{0}^{*}\right)^{2}}\right) \\
& =-\frac{1}{2} \ln \left(\left(x-x_{0}^{*}\right)^{2}+\left(y-y_{0}^{*}\right)^{2}\right)-\ln k
\end{aligned}
$$

Then $h$ is harmonic for all $(x, y) \neq\left(x_{0}^{*}, y_{0}^{*}\right)$, in particular, $h$ is harmonic on $D_{R}$; and for all $(x, y)$ on $C_{R}$, we have $h\left(x, y, x_{0}, y_{0}\right)=-v\left(x, y, r_{U}, y_{0}\right)$, by (1). Thus $h$ is precisely the function that we are looking for, and consequently, Green's function for $D_{R}$ is
$G\left(x, y, x_{0}, y_{0}\right)=\frac{1}{2} \ln \left(\left(x-x_{0}\right)^{2}+\left(y-y_{0}\right)^{2}\right)-\frac{1}{2} \ln \left(\left(x-x_{0}^{*}\right)^{2}+\left(y-y_{0}^{*}\right)^{2}\right)-\ln k$.
Simplifying, we find that, for all $(x, y) \neq\left(x_{0}, y_{0}\right)$ in $D_{R}$,

$$
G\left(x, y, x_{0}, y_{0}\right)=\frac{1}{2} \ln \left[\frac{\left(x-x_{0}\right)^{2}+\left(y-y_{0}\right)^{2}}{\left(x-x_{0}^{*}\right)^{2}+\left(y-y_{0}^{*}\right)^{2}}\right]-\ln k
$$

With this we have reduced the construction of Green's function on the disk $D_{R}$ to the following geometric problem. Given a point $A=\left(x_{0}, y_{0}\right)$ inside $D_{R}$, find a point $A^{*}=\left(x_{0}^{*}, y_{0}^{*}\right)$ outside $D_{R}$ and a constant $k>0$ so that (1) holds for all points ( $x, y$ ) on the circle $C_{R}$.

The solution of this problem is given by a well-known geometric construction or transformation called the Steiner inversion: When $A$ is not

## PROPOSITION 1 STEINER INVERSION

![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-30_731_475_1184_70.jpg)
Figure 3 Rotate the picture in Figure 3(a) to bring $A$ and $A^{*}$ to the positive $x$-axis (Figure 3(b)). A rotation does not change distances.

the origin, the point $A^{*}$ is the inverse of the point $A$ through the circle $C_{R}$. By definition of the Steiner inversion, $A^{*}$ is the point on the ray from the origin $O$ through $A$ at a distance such that

$$
O A \cdot O A^{*}=R^{2}
$$

(Figure 2). (Even though we exclude from our discussion the case where $A$ is the center of $C_{R}$, the formulas that we derive apply even when $A$ is the center of $C_{R}$.) We next state the property of the inversion that is key to the construction of Green's function. We use the notation $|A-B|= \sqrt{\left(x_{1}-x_{2}\right)^{2}+\left(y_{1}-y_{2}\right)^{2}}$ for the distance between the points $A=\left(x_{1}, y_{1}\right)$ and $B=\left(x_{2}, y_{2}\right)$, and $|A|=\sqrt{x_{1}^{2}+y_{1}^{2}}$ for the distance from $A$ to the origin.

Let $A=\left(x_{0}, y_{0}\right)$ be a a fixed point in $D_{R}$ minus its center and let $A^{*}= \left(x_{0}^{*}, y_{0}^{*}\right)$ be its image by the Steiner inversion. For any point $P=(x, y)$ on $C_{R}$, we have
(5)

$$
|A-P|=\frac{|A|}{R}\left|A^{*}-P\right|=k \cdot\left|A^{*}-P\right|,
$$

where $k=\frac{|A|}{R}=\frac{\sqrt{x_{0}^{2}+y_{0}^{2}}}{R}$.
Proof By rotating the picture, if necessary, we may assume that the points $A$ and $A^{*}$ are on the positive $x$-axis, located at the distances $|A|$ and $\left|A^{*}\right|$, respectively, where $\left|A^{*}\right|=\frac{R^{2}}{|A|}$, by (4) (Figure 3). Using polar coordinates, write $P=(R \cos \theta, R \sin \theta)$. Then

$$
\begin{aligned}
\frac{|A-P|^{2}}{\left|A^{*}-P\right|^{2}} & =\frac{(|A|-R \cos \theta)^{2}+R^{2} \sin ^{2} \theta}{\left(\left|A^{*}\right|-R \cos \theta\right)^{2}+R^{2} \sin ^{2} \theta} \\
& =\frac{|A|^{2}+R^{2}-2 R|A| \cos \theta}{\frac{R^{4}}{|A|^{2}}+R^{2}-2 \frac{R^{3}}{|A|} \cos \theta}=\frac{|A|^{2}}{R^{2}}
\end{aligned}
$$

where the last equality follows by simplifying. Thus (5) holds.
Combining the proposition with (3), we find that for $(x, y) \neq\left(x_{0}, y_{0}\right)$ in $D_{R}$, Green's function for $D_{R}$ is

$$
G\left(x, y, x_{0}, y_{0}\right)=\frac{1}{2} \ln \left[\frac{\left(x-x_{0}\right)^{2}+\left(y-y_{0}\right)^{2}}{\left(x-x_{0}^{*}\right)^{2}+\left(y-y_{0}^{*}\right)^{2}}\right]-\ln \frac{\sqrt{x_{0}^{2}+y_{0}^{2}}}{R} .
$$

It will be useful to have and expression for Green's function in polar coordinates. If $A=\left(r_{0} \cos \phi, r_{0} \sin \phi\right)$, then $A^{*}=\left(\frac{R^{2}}{r_{0}} \cos \phi, \frac{R^{2}}{r_{0}} \sin \phi\right)$. For $P=(r \cos \theta, r \sin \theta)$, using the law of cosines in the triangles $O A P$ and $O A^{*} P$ (Figure 4), we find $|A-P|^{2}=r^{2}+r_{0}^{2}-2 r r_{0} \cos (\theta-\phi)$ and $\left|A^{*}-P\right|^{2}=$

![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-31_406_433_220_37.jpg)
Figure 4 Law of cosines in a triangle.

> THEOREM 1 SOLUTION OF POISSON'S EQUATION ON THE DISK
$r^{2}+\frac{R^{1}}{r_{0}^{2}}-2 r \frac{R^{2}}{r_{0}} \cos (\theta-\phi)$, and so

$$
\begin{aligned}
G\left(r, \theta, r_{0}, \phi\right) & =\frac{1}{2} \ln \left[\frac{|A-P|^{2}}{\left|A-P^{*}\right|^{2}}\right]-\ln \frac{|A|}{R} \\
& =\frac{1}{2} \ln \left[\frac{r^{2}+r_{0}^{2}-2 r r_{0} \cos (\theta-\phi)}{r^{2}+\frac{R^{4}}{r_{0}^{2}}-2 r \frac{R^{2}}{r_{0}} \cos (\theta-\phi)}\right]-\frac{1}{2} \ln \frac{r_{0}^{2}}{R^{2}} \\
& =\frac{1}{2} \ln \left[R^{2} \frac{r^{2}+r_{0}^{2}-2 r r_{0} \cos (\theta-\phi)}{r^{2} r_{0}^{2}+R^{4}-2 r r_{0}} \frac{R^{2} \cos (\theta-\phi)}{}\right]
\end{aligned}
$$

With this formula in hand, we can now return to the previous section and derive concrete formulas for the solutions of Poisson's equation and the Dirichlet problem on the disk. For example, appealing to Theorem 4 of the previous section, we obtain the following interesting formula.
Let $f(r, \theta)$ be a function on the disk $D_{R}$. The solution of

$$
\nabla^{2} u(r, \theta)=f(r, \theta), \quad 0 \leq r<R, 0 \leq \theta \leq 2 \pi,
$$

with boundary values $u=0$ on $C_{R}$, is

$$
u\left(r_{0}, \phi\right)=\frac{1}{4 \pi} \int_{0}^{2 \pi} \int_{0}^{R} f(r, \theta) \ln \left[R^{2} \frac{r^{2}+r_{0}^{2}-2 r r_{0} \cos (\theta-\phi)}{r^{2} r_{0}^{2}+R^{4}-2 r r_{0} R^{2} \cos (\theta-\phi)}\right] r d r d \theta
$$

where $0 \leq r_{0}<R$ and $0 \leq \phi \leq 2 \pi$.
Our next goal is to derive a concrete formula for the solution of the Dirichlet problem (Theorem 2, Section 12.3). For this purpose, we need to find the normal derivative $\partial / \partial r_{0}$ of Green's function at the points on the circle $C_{R}$. Computing directly from (7), we get

$$
\begin{aligned}
\left.\frac{\partial}{\partial r_{0}} G\left(r, \theta, r_{0},()\right)\right|_{r_{0}=R} & =\left.\frac{1}{2} \frac{\partial}{\partial r_{0}} \ln \left[R^{2} \frac{r^{2}+r_{0}^{2}-2 r r_{0} \cos (\theta-\phi)}{r^{2} r_{0}^{2}+R^{4}-2 r r_{0} R^{2} \cos (\theta-\omega)}\right]\right|_{r_{0}=R} \\
& =\frac{1}{2} \frac{1}{N} \times\left.\frac{N^{\prime} \cdot D-N \cdot D^{\prime}}{D}\right|_{r_{0} \cdot R},
\end{aligned}
$$

where $N=r^{2}+r_{0}^{2}-2 r r_{0} \cos (\theta-\phi)$ and $D=r^{2} r_{0}^{2}+R^{4}-2 r r_{0} R^{2} \cos (\theta-\phi)$ and the prime denotes taking the derivative with respect to $r_{0}$. Straightforward computations yield:

$$
\begin{aligned}
\left.N\right|_{r_{0}=R} & =r^{2}+R^{2}-2 r R \cos (\theta-\phi) \\
\left.D\right|_{r_{0}=R} & =r^{2} R^{2}+R^{4}-2 r R^{3} \cos (\theta-\phi)=\left.R^{2} N\right|_{r_{0}=R} \\
\left.N^{\prime}\right|_{r_{0}=R} & =2 R-2 r \cos (\theta-\phi) \\
\left.D^{\prime}\right|_{r_{0}=R} & =2 r^{2} R-2 r R^{2} \cos (\theta-\phi)
\end{aligned}
$$

## THEOREM 2 SOLUTION OF DIRICHLET'S PROBLEM ON THE DISK

![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-32_444_440_1597_74.jpg)
Figure 5 Image of a source point in the upper half-plane.

Using this in the normal derivative and simplifying, we obtain

$$
\left.\frac{\partial}{\partial r_{0}} G\left(r, \theta, r_{0}, \phi\right)\right|_{r_{0}=R}=\frac{R^{2}-r^{2}}{R\left(R^{2}+r^{2}-2 r R \cos (\theta-\phi)\right)} .
$$

We now restate Theorem 2, Section 12.3, using (9), with $d s=R d \theta$, and the following minor modification: Since the points on the boundary depend only on $\theta$, we set $u(x, y)=f(\theta)$ for all $(x, y)$ on $C_{R}$.

Suppose that $u$ is harmonic in $D_{R}$ and $u(R, \theta)=f(\theta)$ on the boundary $C_{R}$. Then

$$
u(r, \phi)=\frac{R^{2}-r^{2}}{2 \pi} \int_{0}^{2 \pi} \frac{f(\theta)}{R^{2}+r^{2}-2 r R \cos (\theta-\phi)} d \theta
$$

where $0 \leq r<R$ and $0 \leq \phi \leq 2 \pi$.
Formula (10) is know as the Poisson integral formula on the disk $D_{R}$. The function

$$
P(r, \theta)=\frac{R^{2}-r^{2}}{R^{2}+r^{2}-2 r R \cos (\theta-\phi)}, \quad 0 \leq r<R, 0 \leq \phi \leq 2 \pi
$$

is called the Poisson kernel on the disk $D_{R}$. Both formulas (10) and (11) were derived in the exercises of Section 4.4 using Fourier series.

## Green's Function for the Upper Half-Plane

We now turn our attention to the upper half-plane $\Omega$. The region $\Omega$ is obviously not bounded; so, strictly speaking, the results of the previous section do not apply. However, it can be shown that the results are still valid under added assumptions, such as boundedness of the harmonic functions on $\Omega$. For this reason, we will not hesitate to use the results of Section 12.3. To construct Green's function for the upper half-plane, we repeat the steps of the method of images as in the case of the disk; only here the computations turn out to be much easier, as you will see shortly.

Start by setting

$$
G\left(x, y, x_{0}, y_{0}\right)=\overbrace{\frac{1}{2} \ln \left(\left(x-x_{0}\right)^{2}+\left(y-y_{0}\right)^{2}\right)}^{v\left(x, y, x_{0}, y_{0}\right)}+h\left(x, y, x_{0}, y_{0}\right),
$$

and let us look for a harmonic function $h$ on $\Omega$ such that $h\left(. x . y, x_{0}, y_{0}\right)= -v\left(x, y, x_{0}, y_{0}\right)$ on the boundary of $\Omega$; that is, when $y=0$. The image, $A^{*}$, of the point $A$ is clear in this case: Take $A^{*}=\left(x_{0},-y_{0}\right)$. If you think of $A$ as the location of a heat source in the upper half-plane, then $A^{*}$ is the location of the heat source in the lower half-plane that yields a similar effect

## THEOREM 3 SOLUTION OF POISSON'S EQUATION ON THE UPPER HALF-PLANE

## THEOREM 4 SOLUTION OF DIRICHLET'S PROBLEM ON THE UPPER HALF-PLANE

on the boundary (Figure 5). Set $h\left(x, y, x_{0}, y_{0}\right)=-\frac{1}{2} \ln \left(\left(x-x_{0}\right)^{2}+(y+\right. \left.\left.y_{0}\right)^{2}\right)$. On the boundary, $y=0$, we see immediately that $h\left(x, 0, x_{0}, y_{0}\right)= -v\left(x, 0, x_{0}, y_{0}\right)$. Thus Green's function for the upper half-plane is

$$
G\left(x, y ., r_{0}, y_{0}\right)=\frac{1}{2} \ln \frac{\left(x-x_{0}\right)^{2}+\left(y-y_{0}\right)^{2}}{\left(x-x_{0}\right)^{2}+\left(y+y_{0}\right)^{2}}
$$

where $x_{0}$ and $x$ are arbitrary and $y_{0}$ and $y$ are $>0$. For future reference, we write the solution of Poisson's problem in the upper half-plane as follows.

Let $f(x, y)$ be a function defined on the upper half-plane. The solution of

$$
\nabla^{2} u(r, \theta)=f(x, y), \quad-\infty<x<\infty, 0<y .
$$

with boundary values $u=0$ on the $x$-axis $(y=0)$, is

$$
u\left(x_{0}, y_{0}\right)=\frac{1}{4 \pi} \int_{0}^{\infty} \int_{-\infty}^{\infty} f(x, y) \ln \frac{\left(x-x_{0}\right)^{2}+\left(y-y_{0}\right)^{2}}{\left(x-x_{0}\right)^{2}+\left(y+y_{0}\right)^{2}} d x d y
$$

To derive the solution of the Dirichlet problem in the upper half-plane, we first compute the normal derivative of $G$ at the points on the $x$-axis. The normal derivative in this case is $-\partial / \partial y_{0}$. Computing directly from (12), we get

$$
\begin{aligned}
& -\left.\frac{1}{2} \frac{\partial}{\partial y_{0}}\left[\ln \left[\left(x-x_{0}\right)^{2}+\left(y-y_{0}\right)^{2}\right]-\ln \left[\left(x-x_{0}\right)^{2}+\left(y+y_{0}\right)^{2}\right]\right]\right|_{y_{0}=0} \\
& \quad=-\left.\frac{1}{2}\left[\frac{-2\left(y-y_{0}\right)}{\left(x-x_{0}\right)^{2}+\left(y-y_{0}\right)^{2}}-\frac{2\left(y+y_{0}\right)}{\left(x-x_{0}\right)^{2}+\left(y+y_{0}\right)^{2}}\right]\right|_{y_{0}=0} \\
& \quad=\frac{2 y}{\left(x-x_{0}\right)^{2}+y^{2}}
\end{aligned}
$$

With this, Theorem 2, Section 12.3, takes the following form.
Suppose that $u$ is harmonic in the upper half-plane and $u(x, 0)=f(x)$ on the boundary. Then

$$
u\left(x_{0}, y\right)=\frac{y}{\pi} \int_{-\infty}^{\infty} \frac{f(x)}{\left(x-x_{0}\right)^{2}+y^{2}} d x
$$

where $-\infty<x_{0}<\infty$ and $0<y$.
We recognize (14) as the Poisson integral formula for the upper halfplane, which we have derived in Section 7.5 using the Fourier transform.

In the next sections, we introduce the powerful method of conformal mappings and derive formulas for Green's functions on various regions and
corresponding formulas for the solutions of Dirichlet's problem and Poisson's equation.

## Exercises 12.4

In Exercises 1-8, evaluate the given expression without computing. Appeal to various results from this section and uplain how you are using them.

1. $\frac{1}{2 \pi} \int_{0}^{2 \pi} \frac{1-r^{2}}{1+r^{2}-2 r \cos (\theta-\phi)} d \theta$. (This is the integral of the Poisson kernel on the unit disk.)
2. $\frac{1}{2 \pi} \int_{0}^{2 \pi} \frac{R^{2}-r^{2}}{R^{2}+r^{2}-2 r R \cos (\theta-\phi)} d \theta$.
3. $\quad \frac{1-r^{2}}{2 \pi} \int_{0}^{2 \pi} \frac{\cos n \theta}{1+r^{2}-2 r \cos (\theta-r)} d \theta$, where $n=1,2, \ldots$.
4. $\quad \frac{1-r^{2}}{2 \pi} \int_{0}^{2 \pi} \frac{\sin n \theta}{1+r^{2}-2 r \cos (\theta-\phi)} d \theta$, where $n=1,2, \ldots$.
5. $\frac{R^{n}\left(R^{2}-r^{2}\right)}{2 \pi} \int_{0}^{2 \pi} \frac{\cos n \theta}{R^{2}+r^{2}-2 r R \cos (\theta-\phi)} d \theta$, where $n=1,2, \ldots$.
6. $\frac{R^{n}\left(R^{2}-r^{2}\right)}{2 \pi \bar{R}^{n}} \int_{0}^{2 \pi} \frac{r^{n} \sin n \theta}{R^{2}+r^{2}-2 r R \cos (\theta-\phi)} d \theta$, where $n=1,2, \ldots$.
7. $\frac{-\alpha_{n}^{2}}{4 \pi} \int_{0}^{2 \pi} \int_{0}^{1} J_{0}\left(\alpha_{n} r\right) \ln \left[\frac{r^{2}+r_{0}^{2}-2 r r_{0} \cos (\theta-\phi)}{r^{2} r_{0}^{2}+1-2 r r_{0} \cos (\theta-\phi)}\right] r d r d \theta$, where $\alpha_{n}$ is the $n$th positive zero of Bessel's function $J_{0}$.
8. $\frac{-\alpha_{m, n}^{2}}{4 \pi} \int_{0}^{2 \pi} \int_{0}^{1} J_{m}\left(\alpha_{m, n} r\right) \cos (m \theta) \ln \left[\frac{r^{2}+r_{0}^{2}-2 r r_{0} \cos (\theta-\phi)}{r^{2} r_{0}^{2}+1-2 r r_{0} \cos (\theta-\phi)}\right] r d r d \theta$. where $m$ is a positive integer and $\alpha_{m, n}$ is the $n$th positive zero of Bessel's function $J_{m}$.
9. Verify directly from (7) that Green's function for the disk is 0 on the boundary $(r=R)$.
10. Verify directly from (7) that Green's function for the disk is $\leq 0$ for $0 \leq r<R$ and all $\theta$.
11. Verify directly from (7) that Green's function for the disk is symmetric.
12. Verify directly from (12) that Green's function in the upper half-plane satisfies properties (ii), (iii), and (v) of Theorem 3, Section 12.3.
13. Verify directly from (12) that Green's function in the upper half-plane satisfies Theorem 3(i), Section 12.3.
14. Combine Theorems 1 and 2 to solve the general Poisson problem: $\nabla^{2} u=f(r, \theta)$ on $D_{R}$, with boundary condition $u(R, \theta)=g(\theta)$ on $C_{R}$.
15. Combine Theorems 3 and 4 to solve the general Poisson problem: $\nabla^{2} u=f(x, y)$ in the upper half-plane, with boundary condition $u(x, 0)=g(x)$ on the $x$-axis.
16. Suppose in Theorem 1 that $f(r, \theta)=f(r)$ (thus $f$ depends only on $r$ and not
on $\theta)$. Show that the solution depends only on $r$. [Hint: Differentiate under the double integral sign with respect to $\phi$ and show that the derivative is 0 .]
17. Project Problem: A Neumann problem in the upper half-plane. In this exercise, you are asked to show that the solution of

$$
\phi_{x x}+\phi_{y y}=0 \quad(-\infty<x<\infty, y>0),
$$

subject to the Neumann boundary condition, $\phi_{y}(x, 0)=f(x)$, is

$$
\phi(x, y)=\frac{1}{2 \pi} \int_{-\infty}^{\infty} \ln \left((x-t)^{2}+y^{2}\right) f(t) d t
$$

Note that the solution can be determined only up to an arbitrary additive constant. For an alternative derivation, see Section 12.8 .
(a) Show that if 0 satisfies the stated Neumann problem, then $v=\frac{\partial \rho}{\partial y}$ satisfies the Dirichlet problem: For $-\infty<x<\infty$ and $y>0$,

$$
v_{x x}+v_{y y}=0, \text { and } v(x, 0)=f(x)
$$

(b) Apply Poisson's formula to obtain

$$
v(r . y)=\frac{y}{\pi} \int_{-\infty}^{\infty} \frac{f(t)}{(x-t)^{2}+y^{2}} d t
$$

(c) Derive the solution of the Neumann problem.

### 12.5 Analytic Functions

In the remaining sections of this chapter we explore a connection between complex-valued functions and the solution of partial differential equations.

![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-35_426_391_1313_38.jpg)
Figure 1 Identifying a complex number $z$ with a point in the Cartesian plane; the complex conjugate $Z$; the norm $|z|$ of $z$.

If $z=x+i y$, where $x$ and $y$ are real numbers, we call $x$ the real part of $z$ and $y$ its imaginary part, and set $x=\operatorname{Re} z$ and $y=\operatorname{Im} z$. We denote the set of all complex numbers by $\mathbb{C}$. We identify a complex number $z=x+i y$ with a point ( $x, y$ ) in the Cartesian plane (referred to as the complex plane), much like a real number is identified with a point on the real number line (Figure 1). We introduce the notion of distance between two complex numbers, using the distance formula from the Cartesian plane: If $z_{1}=x_{1}+i y_{1}$ and $z_{2}=x_{2}+i y_{2}$, then the distance between $z_{1}$ and $z_{2}$ is

$$
\left|z_{1}-z_{2}\right|=\sqrt{\left(x_{1}-x_{2}\right)^{2}+\left(y_{1}-y_{2}\right)^{2}}
$$

(Figure 2). In particular, the modulus or absolute value of a complex number $z=x+i y$ is its distance to the origin: $|z|=\sqrt{x^{2}+y^{2}}$ (Figure 1). The complex conjugate of $z=x+i y$ is the complex number $\bar{z}=x-i y$. We have

$$
z \cdot \bar{z}=x^{2}+y^{2}
$$

![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-36_340_352_172_65.jpg)
Figure 2 Distance between two complex numbers $z_{1}$ and $z_{2}$.

![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-36_410_454_754_63.jpg)
Figure 3 Polar representation $z=|z| e^{i \theta}, \theta$ is the argument of $z$.

Thus $z \cdot \bar{z}$ is always a nonnegative real number and $z \cdot \bar{z}=0 \Leftrightarrow z=0$. In terms of the complex conjugate, we have $|z|=\sqrt{z \bar{z}}$.

Using polar coordinates, we write a nonzero complex number in polar form, $z=r(\cos \theta+i \sin \theta)$, where $r=|z|=\sqrt{x^{2}+y^{2}}$ and $\theta$ is the polar angle in Figure 3. With the help of Euler's identity, $e^{i \theta}=\cos \theta+i \sin \theta$, we can also write $z=r e^{i \theta}$. The angle $\theta$ is called the argument of $z$ and is denoted $\arg z$. It is clear that $\arg z$ is not single-valued: If $\alpha$ is one value of the argument, then any value of the form $\alpha+2 k \pi$, where $k$ is an integer, is also the argument of $z$. The unique value of $\arg z$ in the interval $(-\pi, \pi]$ is called the principal value of the argument and is clenoted by $\operatorname{Arg} z$.

The polar representation can be used to describe geometrically the effect of multiplication. Given two complex numbers $z_{1}=r_{1} e^{i \theta_{1}}$ and $z_{2}=r_{2} e^{i \theta_{2}}$, we have

$$
z_{1} \cdot z_{2}=r_{1} e^{i \theta_{1}} r_{2} e^{i \theta_{2}}=r_{1} r_{2} e^{i\left(\theta_{1}+\theta_{2}\right)}
$$

Thus to multiply two complex numbers we multiply their moduli and add their arguments.

## Complex Functions

A complex-valued function of a complex variable, or simply a complex function, is a mapping $w=f(z)$ whose domain is a subset of the complex $z$-plane and whose range is a subset of the complex $w$-plane. By taking real and imaginary parts. we can visualize such a function as a mapping from a subset of the Cartesian $x y$-plane into the Cartesian $u v$-plane. We have the relations, $f(z)=u(z)+i v(z)$ or $f(z)=u(x, y)+i v(x, y)$, where $u(x, y)=\operatorname{Re}(f(z))$ and $v(x, y)=\operatorname{Im}(f(z))$ (Figure 4).

![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-36_439_1117_1445_641.jpg)
The following examples illustrate these concepts.

## EXAMPLE 1 Functions of a complex variable

In each of the following examples, we express the function in the form $f(z)= u(x, y)+i v(x, y)$, where $z=x+i y$.
(a) The function $f(z)=\operatorname{Im} z$ is real-valued. We have $u(x, y)=y$ and $v(x, y)=0$.
(b) A linear function is of the form $f(z)=\alpha z+\beta$, where $\alpha$ and $\beta$ are complex numbers. Write $\alpha=a+i b$ and $\beta=c+i d$ where $a, b, c$, and $d$ are real. Then

$$
f(z)=(a+i b)(x+i y)+c+i d=a x-b y+c+i(b x+a y+d)
$$

Thus $u(x, y)=a x-b y+c$ and $v(x, y)=b x+a y+d$.
(c) For the exponential function, $f(z)=e^{z}$, we have

$$
e^{z}=e^{x+i y}=e^{x} e^{i y}=e^{x}(\cos y+i \sin y)
$$

Thus $u(x, y)=e^{x} \cos y$ and $v(x, y)=e^{x} \sin y$.
(d) The sine function is defined in terms of the exponential function as follows:

$$
\sin z=\frac{e^{i z}-e^{-i z}}{2 i}
$$

Notice that if $z=x$ is real, then $\sin z$ reduces to the usual sine function because $\frac{e^{i x}-e^{-i x}}{2 i}=\sin x$, by Euler's identity. Using $e^{i x}=\cos x+i \sin x$ and $\frac{1}{i}=-i$, we have

$$
\begin{aligned}
\sin z & =\frac{e^{i(x+i y)}-e^{-i(x+i y)}}{2 i}=\frac{e^{i x} e^{-y}-e^{-i x} e^{y}}{2 i} \\
& =\sin x \frac{e^{y}+e^{-y}}{2}+i \cos x \frac{e^{y}+e^{-y}}{2} \\
& =\sin x \cosh y+i \cos x \sinh y
\end{aligned}
$$

(e) We define the cosine function by

$$
\cos z=\frac{e^{i z}+e^{-i z}}{2}
$$

Computing as in (d), we find

$$
\cos z=\cos x \cosh y-i \sin x \sinh y
$$

(f) The complex logarithm is trickier to define. There are many "branches" of the logarithm. The principal branch of the logarithm is defined for all $z \neq 0$ by

$$
\log z=\ln |z|+i \operatorname{Arg} z
$$

where $\operatorname{Arg} z$ is the principal value of the argument. Taking real and imaginary parts of the function $\log z$, we find $u(x, y)=\ln |z|=\frac{1}{2} \ln \left(x^{2}+y^{2}\right)$ and $v(x, y)= \tan ^{-1}\left(\frac{y}{x}\right)$, where the value of the inverse tangent must be chosen in the interval ( $-\pi, \pi]$ (see (8)-(10) for explicit formulas for Arg $z$ in terms of $x$ and $y$ ). For any complex number $z \neq 0$, we have

$$
e^{\log z}=e^{\ln |z|+i \operatorname{Arg} z}=e^{\ln |z|} e^{i \operatorname{Arg} z}=|z| e^{i \operatorname{Arg} z}=z
$$

where we have used the fact that $\ln x$ and $e^{r}$ are inverse functions (hence $e^{\ln |z|}= |z|$ ), and we have used the polar representation $z=|z| e^{i \operatorname{Arg} z}$. As a result, we see that $e^{\log z}=z$, which is analogous to the inverse function relationship between $e^{x}$ and $\operatorname{In} x$. Notice however that the identity $\log \left(e^{z}\right)=z$ does not always hold (Exercise 22).

![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-38_435_466_218_65.jpg)
Figure $5 \operatorname{Arg} z$ is not continuous when $z_{0}=x_{0} \leq 0$. Limit of $\operatorname{Arg} z$ along the curve $C$ is $\pi$, but the limit along the curve $C^{\prime}$ is $-\pi$

![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-38_438_462_1026_67.jpg)
Figure 6 Branch cut of $\log 2$, where the function fails to be continuous.

A complex function $f(z)=u(x, y)+i v(x, y)$ is continuous if and only if both $u$ and $v$ are continuous. You can verify that the functions in Example 1(a)-(e) are continuous for all $z=x+i y$. The logarithmic function $\log z$ is not defined at $z=0$ and is not continuous at all $z$ on the negative real axis. To see this, let $z_{0}=x_{0}$ with $x_{0}<0$. By definition of the principal value, we have $\operatorname{Arg} z_{0}=\pi$. If $z$ approaches the point $z_{0}$ from the lower half-plane, then $\operatorname{Arg} z$ tends to $-\pi$ which is not equal to $\operatorname{Arg} z_{0}$. Thus $\lim _{z \rightarrow z_{0}} \operatorname{Arg} z \neq \operatorname{Arg} z_{0}$ and so $\operatorname{Arg} z$ is not continuous at the point $z_{0}$ (Figure 5). It follows that $\log z$ is not continuous at $\varepsilon_{0}$. The set of points $z=x$, where $x \leq 0$ is called a branch cut for $\log z$ (Figure 6). We just proved that $\log z$ is not continuous at all the points on its branch cut. At all other points in the plane, $\log z$ is continuous.

## Analytic Functions, the Cauchy-Riemann Equations

We say that $f(z)$ is differentiable at $z$ if its derivative $f^{\prime}(z)$, or $\frac{d}{d z} f(z)$, exists and is finite at $z$, where

$$
f^{\prime}(z)=\lim _{\zeta \rightarrow z} \frac{f(\zeta)-f(z)}{\zeta-z}
$$

If $S$ is an open set in the complex plane we say that $f$ is analytic on $S$ if $f$ is differentiable at all points $z$ in $S$. A function is analytic at one point $z_{0}$ if it is analytic on an open set that contains $z_{0}$. Definition (1) resembles the familiar definition of the derivative of a function of a real variable from calculus. So you should not hesitate to try techniques from calculus in computing the limit in (1), especially if $f$ is a polynomial or a rational function. For example, if $f(z)=z$, then

$$
f^{\prime}(z)=\lim _{\zeta \rightarrow z} \frac{f(\zeta)-f(z)}{\zeta-z}=\lim _{\zeta \rightarrow z} \frac{\zeta-z}{\zeta-z}=1
$$

as expected. However, keep in mind that unlike a real variable which can vary in only two directions, the complex variable $\zeta$ in (1) can approach $z$ in infinitely many ways, and to say that (1) exists we mean that it exists and is the same no matter how we approach $z$. This is clearly a stronger requirement than the existence of the derivative in the real variable case. For this reason analytic functions have distinctive properties that are not shared by differentiable functions of a real variable. One of these striking propertios is expressed by the following result.

THEOREM 1 CAUCHY-RIEMANN EQUATIONS

![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-39_429_452_1359_36.jpg)
Figure 7 Evaluating the limit (1), as $\zeta$ approaches $z$ in two different (special) ways.

The function $f(z)=u(x, y)+i v(x, y)$ is analytic in an open set $S$ if and only if the partial derivatives of $u$ and $v$ are continuous and satisfy the Cauchy-Riemann equations

$$
u_{x}=v_{y} \quad \text { and } \quad u_{y}=-v_{x} .
$$

Furthermore, if $f$ is analytic, then the derivative $f^{\prime}(z)$ is given as either of

$$
f^{\prime}(z)=u_{x}(x, y)+i v_{x}(x, y) \text { or } f^{\prime}(z)=v_{y}(x, y)-i u_{y}(x, y) .
$$

Thus the real and imaginary parts of an analytic function cannot be arbitrary of each other: They depend on each other in a precise manner described by the Cauchy-Riemann equations.
Proof Here we shall prove only one direction in the theorem. (For the full proof see [1], Chapter 2.) Suppose that $f$ is analytic at $z=x+i y$ so that the limit (1) exists. To prove that the Cauchy Riemann equations and (3) hold, we compute the limit (1) in two different ways: once by taking $\zeta=z+\Delta x$ and once by taking $\zeta=z+i \Delta y$, where $\Delta x$ and $\Delta y$ are small increments in $x$ and $y$ (Figure 7). If $\zeta=z+\Delta x=x+\Delta x+i y, \zeta-z=\Delta x$, and (1) becomes

$$
\begin{aligned}
f^{\prime}(z) & =\lim _{\Delta x \rightarrow 0} \frac{u(x+\Delta x, y)+i v(x+\Delta x, y)-(u(x, y)+i v(x, y))}{\Delta x} \\
& =\lim _{\Delta x \rightarrow 0} \frac{u(x+\Delta x, y)-u(x, y)}{\Delta x}+i \lim _{\Delta x \rightarrow 0} \frac{v(x+\Delta x, y)-v(x, y)}{\Delta x} \\
& =\frac{\partial u}{\partial x}+i \frac{\partial v}{\partial x} .
\end{aligned}
$$

In a similar way, if $\zeta=z+i \Delta y=x+i(y+\Delta y), \zeta-z=i \Delta y$, and (1) becomes

$$
\begin{aligned}
f^{\prime}(z) & =\lim _{\Delta y \rightarrow 0} \frac{u(x, y+\Delta y)+i v(x, y+\Delta y)-(u(x, y)+i v(x, y))}{i \Delta y} \\
& =\lim _{\Delta y \rightarrow 0}(-i) \frac{u(x, y+\Delta y)-u(x, y)}{\Delta y}+\lim _{\Delta y \rightarrow 0} \frac{v(x, y+\Delta y)-v(x, y)}{\Delta y} \\
& =\frac{\partial v}{\partial y}-i \frac{\partial u}{\partial y},
\end{aligned}
$$

where on the second line we have $1 / i=-i$ and $(-i) \cdot i=1$. Since $f^{\prime}(z)$ does not depend on how we approach $z$, equating the previous two limits, we see that (2) and (3) hold.

The following examples illustrate how Theorem 1 can be used to establish analyticity and compute derivatives.

## EXAMPLE 2 Applying the Cauchy-Riemann equations

Refer to the functions in Example 1.
(a) The function $f(z)=\operatorname{Im} z=y$ has real part $u(x, y)=y$ and imaginary part $v(x, y)=0$. Computing partial derivatives, we find $u_{x}=0, u_{y}=1, v_{x}=v_{y}=0$. Thus the equality $u_{y}=-v_{x}$ holds nowhere, and so the Cauchy-Riemann equations do not hold for any $z=x+i y$. Consequently, the function is not analytic at any point in the complex plane.
(b) Using the definition (1), it is straightforward to show that the derivative of the linear function $f(z)=\alpha z+\beta$ is $f^{\prime}(z)=\alpha$. Let us derive this result using Theorem 1 . Write $\alpha=a+i b$ and $\beta=c+i d, u(x, y)=a x-b y+c$ and $v(x, y)=b x+a y+d$. Then $u_{x}=a, u_{y}=-b, v_{x}=b$, and $v_{y}=a$. Thus $u_{x}=v_{y}$ and $u_{y}=-v_{x}$ for all $(x, y)$. Hence the Cauchy-Riemann equations hold and the partial derivatives are continuous at all points. It follows that the function is analytic for all $z$. Moreover, $f^{\prime}(z)=u_{x}+i v_{x}=a+i b=\alpha$.
(c) If $f(z)=e^{z}$, then $u=e^{x} \cos y, v=e^{x} \sin y, u_{x}=e^{x} \cos y, u_{y}=-e^{x} \sin y$, $v_{x}=e^{x} \sin y$, and $v_{y}=e^{x} \cos y$. The partial derivatives are continuous and satisfy the Cauchy-Riemann equations: $u_{x}=v_{y}$ and $u_{y}=-v_{x}$ for all $(x, y)$. Consequently, $f(z)=e^{z}$ is analytic for all $z$ and $f^{\prime}(z)=u_{x}+i v_{x}=e^{x} \cos y+i \rho^{x} \sin y=e^{z}$.
(d) It is a straightforward exercise to show that $\sin z$ is analytic for all $z$ and $\frac{d}{d z} \sin z=\cos z$ (Exercise 27(a)).
(e) Similarly, $\cos z$ is analytic for all $z$ and $\frac{d}{d z} \cos z=-\sin z$ (Exercise 27(b)).
(f) As in the real case, if $f(z)$ is analytic at a point $z$ then it is necessarily continuous at $z$. Thus $\log z$ is not analytic at the branch cut since it is not continuous there. For all other points in the complex plane, recall from Example 1(f) that $u(x, y)=\frac{1}{2} \ln \left(x^{2}+y^{2}\right)$. So

$$
u_{x}=\frac{x}{x^{2}+y^{2}} \quad \text { and } \quad u_{y}=\frac{y}{x^{2}+y^{2}} .
$$

In terms of the inverse tangent, the imaginary part of $\log z$ is $v(x, y)=\tan ^{-1} \underset{x}{y}+ k \pi$, where $k=0, \pm 1$, depending on the location of the point ( $x, y$ ) (see the discussion following Example 3, below). Using that $\frac{d}{d x} \tan ^{-1} x=\frac{1}{1+x^{2}}$ and the chain rule, it is straightforward to show that

$$
v_{x}=\frac{-y}{x^{2}+y^{2}} \quad \text { and } \quad v_{y}=\frac{x}{x^{2}+y^{2}}
$$

(Exercise 53). Thus, the partial derivatives are continuous and the Cauchy-Riemann equations, $u_{x}=v_{y}$ and $u_{y}=-v_{x}$, hold. It follows that, for all $z=x+i y$ not on the branch cut of $\log z$,

$$
\frac{d}{d z} \log z=u_{x}+i v_{x}=\frac{x-i y}{x^{2}+y^{2}}=\frac{1}{z} .
$$

You should justify the last equality (Exercise 53). $\square$

Functions that are analytic for all $z$ are called entire. Thus $\alpha z+\beta, e^{z}$, $\cos z$, and $\sin z$ are all entire functions, but $\log z$ is not entire.

For ease of reference, we now state some properties of the derivative, which are similar to properties of the derivative of a function of a real variable.

THEOREM 2 PROPERTIES OF ANALYTIC FUNCTIONS

THEOREM 3 ANALYTIC FUNCTIONS AND LAPLACE'S EQUATION

Suppose that $f$ and $g$ are analytic on an open set $S$ and $c_{1}, c_{2}$ are complex constants. Then $c_{1} f+c_{2} g$ and $f g$ are analytic on $S$ with

$$
\begin{aligned}
\left(c_{1} f+c_{2} g\right)^{\prime}(z) & =c_{1} f^{\prime}(z)+c_{2} g^{\prime}(z) \text { and } \\
(f g)^{\prime}(z) & =f^{\prime}(z) g(z)+f(z) g^{\prime}(z) .
\end{aligned}
$$

Also, $\frac{f}{g}$ is analytic on $S$ minus the points where $g=0$, and

$$
\left(\frac{f}{g}\right)^{\prime}(z)=\frac{f^{\prime}(z) g(z)-f(z) g^{\prime}(z)}{(g(z))^{2}} \quad(g(z) \neq 0) .
$$

If $g$ is analytic at $z_{0}$ and $f$ is analytic at $g\left(z_{0}\right)$, then the composition $(f \circ g)(z)$ is analytic at $z_{0}$ and we have the chain rule

$$
(f \circ g)^{\prime}\left(z_{0}\right)=f^{\prime}\left(g\left(z_{0}\right)\right) g^{\prime}\left(\sigma_{0}\right)
$$

Using linear combinations of powers of $z$ and appealing to Theorem 2, we conclude that a polynomial $p(z)=a_{n} z^{n}+a_{n-1} z^{n-1}+\cdots+a_{1} z+a_{0}$ is an entire function. Appealing to the quotient rule, we see that a rational function $q(z)=\frac{f(z)}{g(z)}$, where $f$ and $g$ are polynomials, is analytic at all $z$ where $g(z) \neq 0$.

Typically, any function that algebraically manipulates $z$ will be differentiable; however, as we saw in Example 2(a), analyticity can easily fail. Functions such as $\operatorname{Re} z, \operatorname{Im} z$, and $\bar{z}$ are not analytic at any point. (See Exercise 30.)

## The Role of Analytic Functions

Soon we will show powerful applications of analytic functions to partial differential equations. Indeed, the connection between these two fields can be established at this point using the Cauchy-Riemann equations. We have the following important result.

Suppose that $f=u+i v$ is analytic on an open set $S$. Then its real and imaginary parts, $u(x, y)$ and $v(x, y)$, are harmonic on $S$; that is, $u$ and $v$ satisfy Laplace's equation $\nabla^{2} \phi=0$ on $S$.

Proof By a well-know property of analytic functions, if $f$ is analytic then it has derivatives of all orders. This implies that if $f=u+i v$ is analytic then $u$ and $v$ have partial derivatives of all orders and these derivatives are continuous. Moreover, since $f$ is analytic, by the Cauchy-Riemann equations, we have

$$
u_{x}=v_{y} \quad \text { and } \quad u_{y}=-v_{x} .
$$

![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-42_332_465_987_61.jpg)
Figure 8 The inverse tangent takes its values in $\left(\frac{-\pi}{2}, \frac{\pi}{2}\right)$.

![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-42_366_469_1728_59.jpg)
Figure 9 Computing $\operatorname{Arg} z$.

Taking derivatives of second order, we find

$$
\begin{aligned}
u_{x}=v_{y} & \Rightarrow u_{x x}=v_{y x} \\
u_{y}=-v_{x} & \Rightarrow u_{y y}=-v_{y x}
\end{aligned}
$$

where we have interchanged the order of the derivatives-a step that is justified because the partial derivatives are continuous. Hence $u_{x x}+u_{y y}=v_{y x}-v_{y x}=0$. and so $u$ satisfies Laplace's equation. A similar proof works for $v$.

We can use Theorem 3 to generate many interesting examples of harmonic functions; simply take the real or imaginary part of any analytic function.

## EXAMPLE 3 Harmonic functions

(a) The function $f(z)=z^{2}=x^{2}-y^{2}+2 i x y$ is entire. Thus $u(x, y)=x^{2}-y^{2}$ and $v(x, y)=x y$ are harmonic for all $(x, y)$, because $u=\operatorname{Re} f$ and $v=\frac{1}{2} \operatorname{Im} f$.
(b) The function $f(z)=e^{z}=e^{x}(\cos y+i \sin y)$ is entire. Thus $u(x, y)=e^{x} \sin y$ and $v(x, y)=e^{x} \cos y$ are harmonic for all $(x, y)$.
(c) The function $f(z)=\log z=\ln |z|+i \operatorname{Arg} z$ is analytic on $\mathbb{C}$ minus $(-\infty, 0]$. Thus $u(x, y)=\ln |z|=\frac{1}{2} \ln \left(x^{2}+y^{2}\right)$ and $v(x, y)=\operatorname{Arg} ;$ are harmonic on the region $\Omega=\mathbb{C} \backslash(-\infty, 0]$. (In fact, we know from Proposition 2. Section 12.2, that $\frac{1}{2} \ln \left(x^{2}+y^{2}\right)$ is harmonic for all $(x, y) \neq(0,0)$.)

The function $\operatorname{Arg} z$ is harmonic for all $z$ except for $z=a$ : with $x \leq 0$. It is useful to have an expression of $\operatorname{Arg} z$ in terms of $x$ and $y$. Recall that the inverse tangent is a function that takes values in the interval $\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$ (Figure 8), thus the equality $\operatorname{Arg} z=\tan ^{-1}\left(\frac{y}{x}\right)$ holds only when $\operatorname{Arg} z$ is in the interval $\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$. If $\operatorname{Arg} z$ is not in this interval, we need to modify the value of the inverse tangent by adding $\pm \pi$. You can check that for $z=x+i y$ with $x \neq 0$,

$$
\operatorname{Arg} z= \begin{cases}\tan ^{-1}\left(\frac{y}{x}\right) & \text { if } x>0 ; \\ \tan ^{-1}\left(\frac{y}{x}\right)+\pi & \text { if } x<0 \text { and } y \geq 0 ; \\ \tan ^{-1}\left(\frac{y}{x}\right)-\pi & \text { if } x<0 \text { and } y<0 .\end{cases}
$$

For example, in Figure 9, the point $z_{1}=2+3 i$ is in the first quadrant. Using a calculator, we find $\operatorname{Arg} z_{1}=\tan ^{-1} \frac{3}{2} \approx 0.983$. The point $z_{2}=-2-3 i$, is in the third quadrant, $\operatorname{Arg} z_{2}=\tan ^{-1} \frac{3}{2}-\pi \approx-2.159$. (We remind you that all angles are measured in radians.)

When $x$ is zero, we have

$$
\operatorname{Arg} z=\operatorname{Arg}(i y)= \begin{cases}\frac{\pi}{2} & \text { if } y>0 \\ -\frac{\pi}{2} & \text { if } y<0\end{cases}
$$

![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-43_311_456_347_49.jpg)
Figure 10 The inverse cotangent takes its values in $(0, \pi)$.

It is sometimes more convenient to use the inverse cotangent, especially for points in the upper half-plane. The inverse cotangent bakes its values in $(0, \pi)$ (Figure 10) and hence coincides with the values of $\operatorname{Arg} z$ if $\operatorname{Im} z>0$. We have

$$
\operatorname{Arg} z=\cot ^{-1}\left(\frac{x}{y}\right) \text { if } y>0 .
$$

Notice that $\operatorname{Arg} z$ is constant on rays through the origin; more generally, the function $u(z)=a \operatorname{Arg} z+b$, where $a$ and $b$ are real numbers, is constant on rays through the origin. This characteristic property of the argument function helps us solve certain Dirichlet problems, as we now illustrate.

## EXAMPLE 4 Using the argument function

Solve the Dirichlet problem $\nabla^{2} u=0$ in the half-plane $y>0$, given the boundary values

$$
u(x, 0)= \begin{cases}100 & \text { if } x>0 \\ 50 & \text { if } x<0\end{cases}
$$

Solution Since the boundary condition is constant on the rays $x \geq 0$ and $x \leq 0$, it is reasonable to expect that the solution be constant on rays in the upper half-plane. Based on this expectation, we try for a solution the function $u(x, y)=a \operatorname{Arg} z+b$, where $a$ and $b$ are real numbers and $z=x+i y$. The function is harmonic in the upper half-plane. Its values on the boundary are $u(x, 0)=b$ if $x>0$ and $u(x, 0)=a \pi+b$ if $x<0$. Thus, to satisty the boundary conditions, take $b=100$ and $a \pi+100=50$, so $a=-\frac{50}{\pi}$. Hence

$$
u(x, y)=-\frac{50}{\pi} \operatorname{Arg} z+100 .
$$

In terms of $x$ and $y$, we can use (10), since $y>0$, and get

$$
u(x, y)=-\frac{50}{\pi} \cot ^{-1}\left(\frac{x}{y}\right)+100 .
$$

As $y \rightarrow 0^{+}, \cot ^{-1}\left(\frac{x}{y}\right)$ tends to 0 if $x>0$ and $\pi$ if $x<0$, which shows that $u$ satisfies the boundary condition.

If we translate the boundary condition in Example 4 and center it at some point $x_{0}$ other than the origin, then it is necessary to translate the candidate function and consider instead the function $u(z)=a \operatorname{Arg}\left(z-x_{0}\right)+b$, which is also a harmonic function in the upper half-plane. The boundary values in this case are constant on the half-lines $x>x_{0}$ and $x<x_{0}$. As our next example illustrates, we can gencralize this process further and solve an important type of Dirichlet problems, in which the boundary values are constant on intervals. Similar problems were considered in Section 7.5.

![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-44_428_456_481_65.jpg)
Figure 11 A Dirichlet problem in the upper half-plane.

![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-44_341_454_1144_72.jpg)
Figure 12 The angle $\alpha(x, y)$ tends to 0 if $(x, y)$ approaches a point on the $x$-axis outside the interval $(a, b)$ and it tends to $\pi$ if $(x, y)$ approaches a point on the $x$-axis inside the interval ( $a, b$ ).

## EXAMPLE 5 Using translates of the argument function

Given $a \therefore b$, solve the Dirichlet problem $\nabla^{2} u=0$ in the upper half-plane, with the boundary values (Figure 11)

$$
u(x, 0)= \begin{cases}0 & \text { if } x<a, \\ T & \text { if } a<x<b, \\ 0 & \text { if } b<x .\end{cases}
$$

Solution Due to the nature of the boundary values, we must involve the translates of $\operatorname{Arg} z$ by $a$ and $b$. We thus try for a solution the harmonic function $u(x, y)= \frac{a_{1}}{\pi} \operatorname{Arg}(z-a)+\frac{a_{2}}{\pi} \operatorname{Arg}(z-b)+a_{3}$, where $a_{j}(j=1,2,3)$ are real numbers to be determined. The function is harmonic in the upper half-plane. In order to determine its coefficients, we compute its boundary valucs. For any real number $w$, $\frac{a}{\pi} \operatorname{Arg} w=0$ if $w>0$ and $\frac{a}{\pi} \operatorname{Arg} w=a$ if $w<0$. So you can verify that

$$
u(x, 0)=\left\{\begin{aligned}
a_{1}+a_{2}+a_{3} & \text { if } x<a, \\
a_{2}+a_{3} & \text { if } a<x<b, \\
a_{3} & \text { if } b \cdot x .
\end{aligned}\right.
$$

Comparing with the given boundary values, we obtain a system of three equations in the unknowns $a_{1}, a_{2}$, and $a_{3}$ :

$$
\left\{\begin{aligned}
a_{1}+a_{2}+a_{3} & =0, \\
a_{2}+a_{3} & =T, \\
a_{3} & =0 .
\end{aligned}\right.
$$

Starting from the third equation and working our way up, we see that $a_{3}=0$, $a_{2}=T$, and $a_{1}=-T$. Thus $u(x, y)=\frac{T}{\pi}(\operatorname{Arg}(z-b)-\operatorname{Arg}(z-a))$. To write the solution in terms of $x$ and $y$, we use the inverse cotangent, since the imaginary parts of $z-a=(x-a)+i y$ and $z-b=(x-b)+i y$ are positive. We get

$$
u(x, y)=\frac{T}{\pi}\left[\cot ^{-1}\left(\frac{x-b}{y}\right)-\cot ^{-1}\left(\frac{x-a}{y}\right)\right] .
$$

In Figure 12, we have $\cot ^{-1}\left(\frac{x-b}{y}\right)=\alpha_{2}$ and $\cot ^{-1}\left(\frac{x-a}{y}\right)=\alpha_{1}$. Since the sum of the interior angles in a triangle is $\pi$, we obtain $\alpha_{1}+\left(\pi-\alpha_{2}\right)+\alpha(x, y)=\pi$, where $\alpha(x, y)$ is the angle at the point ( $x, y$ ) subtended by the interval ( $a, b$ ). Hence $\alpha(x, y)=\alpha_{2}-\alpha_{1}$, and so $u(x, y)$ is equal to a constant times $\alpha(x, y)$. In particular, $\alpha(x, y)$ is a harmonic function of ( $x, y$ ) in the upper half-plane, which tends to $\pi$ if we approach a boundary point in the interval $(a, b)$ and to 0 if we approach a boundary point outside the interval $(a, b)$. This is a useful fact that was observed in the exercises of Section 7.5. The function $\alpha(x, y)$ is called the harmonic measure of the interval ( $a, b$ ).

## The Harmonic Conjugate

Theorem 3 tells us that the real and imaginary parts of an analytic function are harmonic. Is every harmonic function the real or imaginary part of an

THEOREM 4 HARMONIC CONJUGATE
analytic function? More specifically, given a harmonic function $u$ on a region $\Omega$, can we find another harmonic function $v$ on $\Omega$ such that $f=u+i v$ is analytic on $\Omega$ ? If such a function $v$ exists, it is called a harmonic conjugate of $u$. The following result answers our question.

Suppose that $\Omega$ is a region (open and connected). Then every harmonic function $u$ on $\Omega$ has a harmonic conjugate $v$ on $\Omega$ if and only if $\Omega$ is simply connected (see Section 12.1 for the definition).

The statement of the theorem may appear unusual since the condition for the existence of the harmonic conjugate of $u$ is placed on the region and not on $u$ itself. To understand this peculiarity, consider the function $\frac{1}{2} \ln \left(x^{2}+y^{2}\right)$, which is harmonic on the region $\Omega_{1}=\mathbb{C}$ minus ( 0,0 ). It can be shown that $\frac{1}{2} \ln \left(x^{2}+y^{2}\right)$ does not have a harmonic conjugate on $\Omega_{1}$. However, since $\log z=\frac{1}{2} \ln \left|\ln \left(x^{2}+y^{2}\right)\right|+i \operatorname{Arg} z$ is analytic in $\Omega_{2}=\mathbb{C}$ minus $(-\infty, 0]$, it follows that a harmonic conjugate of $\frac{1}{2} \ln \left(x^{2}+y^{2}\right)$ in $\Omega_{2}$ is $\operatorname{Arg} z$. This example shows that the underlying region is crucial for the existence of the harmonic conjugate.

Theorem 4 guarantees the existence of a harmonic conjugate on any simply connected region such as the entire plane, a disk, a half-plane, a sector, or any other open and connected region with no holes in it. For an arbitrary region, we can always take a disk inside the region around any given point and then apply Theorem 4. As a result, we can say that any harmonic function is locally the real (or imaginary) part of an analytic function, where by "locally" we mean on any disk in the region where the function is harmonic.

Finding the harmonic conjugate can be achieved with the help of the Cauchy-Riemann equations, as we now illustrate.

## EXAMPLE 6 Finding harmonic conjugates

Show that $u(x, y)=x^{2}-y^{2}+x$ is harmonic in the entire plane and find a harmonic conjugate.
Solution We have $u_{x x}=2$ and $u_{y y}=-2$; hence $u_{x x}+u_{y y}=0$, and so $u$ is harmonic. To find a harmonic conjugate $v$, we use the Cauchy-Riemann equations as follows. We want $u+i v$ to be analytic. Hence $v$ must satisfy the Cauchy-Riemann equations

$$
\frac{\partial u}{\partial x}=\frac{\partial v}{\partial y}, \quad \text { and } \quad \frac{\partial u}{\partial y}=-\frac{\partial v}{\partial x} .
$$

Since $\frac{\partial u}{\partial x}=2 x+1$, the first equation implies that

$$
2 x+1=\frac{\partial v}{\partial y}
$$

To get $v$ we will integrate both sides of this equation with respect to $y$. However, because $v$ is a function of $x$ and $y$, the constant of integration in your answer may
be a function of $x$. Thus integrating with respect to $y$ yields

$$
v(x, y)=(2 x+1) y+c(x)
$$

where $c(x)$ is a function of $x$ alone. Plugging this into the second equation in (11), we get

$$
-2 y=-\left(2 y+\frac{d}{d x} c(x)\right)
$$

Hence $c(x)$ has zero derivative and so must be a constant. Let us pick any such constant and write $c(x)=C$. Substituting into the expression for $v$, we get $v(x, y)= (2 x+1) y+c(x)=2 x y+y+C$. You should verify the Cauchy-Riemann equations for the pair of functions $u$ and $v$ and conclude that $\left(x^{2}-y^{2}+x\right)+i(2 x y+y+C)$ is entire.

If $v$ is a harmonic conjugate of $u$, two questions come to mind:

- Is $v$ unique?
- What is a harmonic conjugate of $v$ ?

On any given simply connected region, $v$ is unique up to an additive constant. Also, if $v$ is a harmonic conjugate of $u$, then $-u$ is a harmonic conjugate of $v$ (Exercise 54).

## Orthogonal Trajectories and Harmonic Conjugates

So far we have defined the harmonic conjugate of a harmonic function $u$ as the imaginary part of an analytic function, $f=u+i v$, whose real part is $u$. We now interpret the harmonic conjugate in terms of orthogonal trajectories. This geometric interpretation gives the harmonic conjugate a concrete meaning.

Given a function of two variables, $u(x, y)$, the level curves of $u$ are defined by the equation $u(x . y)=C$. where $C$ is a constant in the range of $u$. To compute the slope of the tangent line, $\frac{d y}{d x}$, at a point on a level curve, we use the chain rule in two dimensions and differentiate with respect to $x$ both sides of $u(x, y)=C$ and get

$$
u_{x} \frac{d x}{d x}+u_{y} \frac{d y}{d x}=0
$$

Since $\frac{d x}{d x}=1$, we solve for $\frac{d y}{d x}\left(=m_{1}\right)$ and get

$$
m_{1}=\frac{d y}{d x}=-\frac{u_{x}}{u_{y}} .
$$

The orthogonal trajectories to the level curves $u(x, y)=C$ is the family of curves that intersects the level curves $u(x, y)=C$ at right angle at each point. Clearly, the two families of curves are mutually orthogonal.

Suppose that we have expressed the orthogonal trajectories in the form $\dot{\psi}(x, y)=C^{\prime}$ for some function $\psi$. As we just showed, the slope of the tangent line at any point of the orthogonal curves is given by $m_{2}=\frac{d y}{d x}=-\frac{v_{x}}{v_{y}}$. Since the slopes of orthogonal curves are negative reciprocals, we have
equivalently, the condition for two families to be mutually orthogonal is

Now suppose that $u$ is a harmonic function with harmonic conjugate $v$, and let us consider the level curves $u(x, y)=C$ and $v(x, y)=C^{\prime}$. Since $u+i v$ is analytic, the Cauchy Riemann equations hold: $u_{x}=v_{y}$ and $u_{y}=-v_{x}$. By (12), it follows that $u(x, y)=C$ and $v(x, y)=C^{\prime}$ are orthogonal families of curves. We thus have the following useful result.

Suppose that we have expressed the orthogonal trajectories in the form $\psi(x, y)=C^{\prime}$ for some function $\psi$. As we just showed, the slope of the tangent
line at any point of the orthogonal curves is given by $m_{2}=\frac{d y}{d x}=-\frac{v_{x}}{v_{y}}$. Since
the slopes of orthogonal curves are negative reciprocals, we have

$$
m_{1} \cdot m_{2}=-1 \Leftrightarrow \frac{u_{x}}{u_{y}} \cdot \frac{\psi_{x}}{\psi_{y}}=-1
$$

equivalently, the condition for two families to be mutually orthogonal is

$$
\frac{u_{x}}{u_{y}}=-\frac{\psi_{y}}{\psi_{x}}
$$

![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-47_50_1159_825_652.jpg)
![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-47_45_58_782_1008.jpg)增 Now suppose that $u$ is a harmonic function with harmonic conjugate $v$, and
let us consider the level curves $u(x, y)=C$ and $v(x, y)=C^{\prime}$. Since $u+i v$ is
analytic, the Cauchy Riemann equations hold: $u_{x}=v_{y}$ and $u_{y}=-v_{x}$. By
(12), it follows that $u(x, y)=C$ and $v(x, y)=C^{\prime}$ are orthogonal familics of
curves. We thus have the following useful result. "

## THEOREM 5 ORTHOGONAL TRAJECTORIES <br> THEOREM 5 ORTHOGONAL S

If $u$ is harmonic and $v$ is a harmonic conjugate of $u$, then the level curves $u(x, y)=C$ and $v(x, y)=C^{\prime}$ are mutually orthogonal.

We give two interpretations of a harmonic conjugate. In heat flow, we can think of $u(x, y)$ as the solution of a Dirichlet problem on a region $\Omega$. Then the level curves $u(. x . y)=C$ represent the isotherms or curves of constant temperature inside $\Omega$. The curves of heat flow inside $\Omega$ are the curves that give the direction along which heat is flowing inside $\Omega$. According to Fourier's law of heat conduction, heat flows from hot to cold in the direction in which the temperature difference is the greatest. If along the isotherms the temperature difference is 0 (the temperature is constant), then the temperature difference is largest along the curves that are orthogonal to the isotherms. (Recall that the gradient of $u, \nabla u=\left(u_{x}, u_{y}\right)$, points in the direction of greatest change in a function, and the gradient is perpendicular to the level curves of $u$.) Consequently, by Theorem 5, the curves of heat flow are given by the level curves of the harmonic conjugate $v$ of $u$.

In electricity and magnetism, the force of attraction or repulsion between charged particles is the gradient of a harmonic function $u$, known as the electrostatic potential. The level curves, $u(x, y)=C$, represcut the equipotential lines. In this case, the level curves of a harmonic conjugate $v$ of $u$ give the direction of the electric force in the field and are known as the lines of force.

![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-48_329_459_414_74.jpg)
Figure 13 The isotherms are rays at angle $\frac{\pi}{50}(100-T)$.

![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-48_336_463_1066_72.jpg)
Figure 14 The isotherms and curves of heat flow are orthogonal.

## EXAMPLE 7 Isotherms and curves of heat flow

Determine the isotherms and curves of heat flow in Example 4.
Solution The boundary values are 50 and 100 , so the temperature inside the region will vary between these two values. For $50<T<100$, the isotherms are given by the level curves $u(x, y)=T$, or

$$
\begin{aligned}
-\frac{50}{\pi} \cot ^{-1}\left(\frac{x}{y}\right)+100=T & \Rightarrow \cot ^{-1}\left(\frac{x}{y}\right)=\frac{\pi}{50}(100-T) \\
& \Rightarrow \frac{x}{y}=\cot \left[\frac{\pi}{50}(100-T)\right] \\
& \Rightarrow y=\tan \left[\frac{\pi}{50}(100-T)\right] x
\end{aligned}
$$

Thus the isotherms are rays through the origin at angle $\frac{\pi}{50}(100-T)$, since the slope is $\tan \left[\frac{\pi}{50}(100-T)\right]$. As $T$ varies from 100 to 50 , this angle varies from 0 to $\pi$, which agrees with our expectation, given the boundary conditions. Some isotherms are shown in Figure 13.

The curves of heat flow are the level curves of a harmonic conjugate of $u$. From Example 4, $u=-\frac{50}{\pi} \operatorname{Arg} z+100$. Now, recall that $\log z=\ln |z|+i \operatorname{Arg} z$ is analytic in the upper half-plane. So Arg $z$ is a harmonic conjugate of $\ln |z|$; consequently, $-\ln |z|$ is a harmonic conjugate of $\operatorname{Arg} z$. Hence a harmonic conjugate of $u$ is $v=\frac{50}{\pi} \ln |z|$. (Here we have used that if $v$ is a harmonic conjugate of $u$, then $\alpha v$ is a harmonic conjugate of $\alpha u+\beta$, where $\alpha$ and $\beta$ are real constants.) In terms of $x$ and $y$, we have $v(x, y)=(25 / \pi) \ln \left(x^{2}+y^{2}\right)$, and so the curves of heat flow are given by the level curves $(25 / \pi) \ln \left(x^{2}+y^{2}\right)=C$. Multiplying by $\frac{\pi}{25}$ and then taking the exponential, we get $x^{2}+y^{2}=R$, where $R>0$. Thus the curves of heat flow are semi-circles centered at the origin. In Figure 14 we show some isotherms and curves of heat flow. Notice the orthogonality of these two families of curves. Figure 14 also illustrates Fourier's law that heat is flowing from hot to cold in the direction in which the temperature difference is the greatest .

In the following section we explore another connection between analytic functions and harmonic functions, and develop the method of conformal mappings for solving Laplace's equation.

## Exercises 12.5

Exercises 1-20 are intended as reviow of basic topies in complex numbers and functions. In these exercises, take $n=0 \pm 1, \pm 2, \ldots$, and $z=x+i y$, unless otherwise specified.
In Exercises 1-4, write the given complex number in the form $a+i b$, where $a$ and $b$ are real numbers.
1.
(a) $(3+2 i)(2-i)$.
(b) $\quad(3-i) \overline{(2-i)}$.
(c) $\frac{1+i}{1-i}$.
2. (a) $\quad i(2-i)^{2}$.
(b) $\overline{(3+i) \overline{(1-i)}}$.
(c) $\frac{2-i}{i}$.
3. (a) $\frac{1}{i}$.
(b) $(i)^{n}$.
(c) $(\bar{i})^{n}$.
4. (a) $\overline{\left(\frac{3+i}{1-i}\right)}$.
(b) $i^{2}+i^{20}+i^{200}+i^{202}$.
(c) $\sum_{n=0}^{1001} i^{n}$.

For the given complex number in Exercises 5-16, (a) find the principal value of the argument. (b) Compute the modulus. (c) Write the number in the form $r^{i \theta}$.
5. $\quad i$.
6. $-i$.
7. $\pi$.
8. $-\pi$.
9. $1+i$.
10. $1-i$.
11. $-1+i$.
12. $-1-i$.
13. $(1+i)^{2}$.
14. $\frac{1}{1+i}$.
15. $\cos \alpha+i \sin \alpha$. 16. $\cos \alpha-i \sin \alpha$.

In Exercises 17-20, evaluate the function and write your answer in the form $a+i b$, where $a$ and $b$ are real numbers.
17.
(a) $e^{2 i}$.
(b) $\sin i$.
(c) $\cos i$.
(d) $\log i$.
18.
(a) $e^{1-\pi i}$.
(b) $\sin (2+\pi i)$.
(c) $\log (-7)$.
(d) $\quad \log 1$.
19.
(a) $e^{-\frac{\pi}{2} i}$.
(b) $e^{2-\frac{\pi}{2} i}$.
(c) $\quad \log (1-i)$.
(d) $\quad \log (1-i)^{2}$.
20.
(a) $e^{\log (1+5 \pi i)}$.
(b) $\quad \log \left(e^{1+5 \pi i}\right)$.
(c) $\log [(-1) \cdot i]$.
(d) $\log (-1)+\log i$.
21. Give an example to show that $\log \left(z_{1} \cdot z_{2}\right)$ is not always equal to $\log \left(z_{1}\right)+ \log \left(z_{2}\right)$.
22. Give an example to show that $\log \left(e^{z}\right)$ is not always equal to $z$. Find a necessary and sufficient condition on $z$ for the equality $\log \left(e^{z}\right)=z$ to hold.

In Exercises 23-26, derive the given identity. Take $z=x+i y$.
23.
(a) $\left|e^{z}\right|=e^{x}$.
(b) $\left|e^{i z}\right|=e^{-y}$.
24.
(a) $|\sin z|=\sqrt{\sin ^{2} x+\sinh ^{2} y}$.
(b) $|\cos z|=\sqrt{\cos ^{2} x+\sinh ^{2} y}$.
25.
(a) $\cos (i x)=\cosh x$.
(b) $\quad \sin (i x)=i \sinh x$.
26.
(a) $\overline{e^{z}}=e^{\bar{z}}$.
(b) $\overline{\sin z}=\sin \bar{z}$.

In Exercises 27-30, use the Cauchy-Riemann equations to verify whether the given function is analytic. If it is, compute its derivative using either one of the identities in (9).
27.
(a) $\sin z$.
(b) $\cos z$.
28.
(a) $e^{z}+z$.
(b) $z^{2}$.
29.
(a) $\frac{x+i y}{x^{2}+y^{2}}$.
(b) $\frac{x-i y}{x^{2}+y^{2}}$.
30.
(a) $\bar{z}$.
(b) $\operatorname{Re} z$.

In Exercises 31-34, verify that the given function is harmonic, and then find a harmonic conjugate using the technique of Example 6.
31. $x^{2}-y^{2}+x y$.
32. $x^{2}-y^{2}-2 x+1$.
33. $e^{x} \cos y$.
34. $\cos x \sinh y$.

![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-50_428_464_1008_88.jpg)
Figure 15 Dirichlet problem in Exercise 42.

![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-50_426_460_1650_89.jpg)
Figure 16 Dirichlet problem in Exercise 43.

In Exercises 35-36, by guessing find an analytic function $f$ such that the given function is the real or imaginary part of $f$. Using Theorem 3, determine where the given function is harmonic.
35. $\frac{y}{x^{2}+y^{2}}$.
36. $e^{2 x} \cos (2 y)$.
37. (a) Plot the level curves of the harmonic function $u(x, y)=\frac{y}{x^{2}+y^{2}}$.
(b) Find and plot the orthogonal trajectories.
38. (a) Plot the level curves of the harmonic function $u(x, y)=\ln \left(x^{2}+y^{2}\right)$.
(b) Find and plot the orthogonal trajectories.
39. (a) For any integer $n$, show that $u(r, \theta)=r^{n} \cos (n \theta)$ and $v(r, \theta)=r^{n} \sin (n \theta)$ are harmonic on $\mathbb{C}$ if $n \geq 0$ and on $\mathbb{C} \backslash\{0\}$ if $n<0$.
(b) Find the harmonic conjugates of $u$ and $v$. [Hint: Consider $f(z)=z^{n}$ in polar coordinates.]
40. Translating and dilating a harmonic function. Suppose that $u$ is harmonic. Show that the following functions are also harmonic:
(a) $\quad u(x-\alpha, y-\beta)$, where $\alpha$ and $\beta$ are real numbers;
(b) $u(\alpha x, \alpha y)$, where $\alpha \neq 0$ is a real number.
41. Harmonic functions independent of $y$. Suppose that $u(x, y)$ is a harmonic function whose values depend only on $x$ and not on $y$. Using Laplace's equation, show that $u(x, y)=a x+b$, where $a$ and $b$ are real constants.

42 (a) Use Exercise 41 to solve the Dirichlet problem in the infinite vertical strip in Figure 15.
(b) Determine and plot the isotherms and curves of heat flow.
43. Solve the Dirichlet problem in Figure 16.
44. Solve the Dirichlet problem in Figure 17.
45. Solve the Dirichlet problem in Figure 18.
46. Determine and plot the isotherms and curves of heat flow in Exercise 42.

![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-50_426_463_1646_740.jpg)
Figure 17 Dirichlet problem in Exercise 44.

![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-50_420_454_1652_1389.jpg)
Figure 18 Dirichlet problem in Exercise 45.

![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-51_427_456_416_49.jpg)
Figure 19 Dirichlet problem for Exercise 48.

![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-51_434_462_1571_45.jpg)
Figure 20 Dirichlet problem for Exercise 49.

47. Solve the Dirichlet problem in the upper half-plane with boundary data on the $r$-axis given by

$$
u(x, 0)= \begin{cases}T_{1} & \text { if } a<x<b \\ T_{2} & \text { otherwise }\end{cases}
$$

where $a<b$ are fixed real numbers.
48. Project Problem: Harmonic measures of two disjoint intervals. In this exercise, we generalize the result of Example 5 by solving the Dirichlet problem in the upper half-plane with boundary data.

$$
u(x, 0)= \begin{cases}T_{1} & \text { if } a<x<b \\ T_{2} & \text { if } c<x<d \\ 0 & \text { otherwise }\end{cases}
$$

where $a<b \leq c<d$ (Figure 19).
(a) Show that if $u_{1}$ is a solution of the Dirichlet problem in the upper half-plane with boundary conditions

$$
u_{1}(x, 0)= \begin{cases}T_{1} & \text { if } a<x<b \\ 0 & \text { otherwise }\end{cases}
$$

and $u_{2}$ is a solution of the Dirichlet problem in the upper half-plane with boundary conditions

$$
u_{2}(x, 0)= \begin{cases}T_{2} & \text { if } c<x<d . \\ 0 & \text { otherwise },\end{cases}
$$

then the solution of the Dirichle problem in the upper half-plane with boundary data $u(x, 0)$ is $u(x, y)=u_{1}(x, y)+u_{2}(x, y)$.
(b) Show that $n(x, y)=\left(T_{1} / \pi\right) \alpha_{1}(x, y)+\left(T_{2} / \pi\right) \alpha_{2}(x, y)$ where $\alpha_{1}(x, y)$, respectively, $\alpha_{2}(x, y)$, is the angle at ( $x, y$ ) subtended by the interval ( $a, b$ ), respectively. (c, d).
49. (a) Solve the Dirichlet problem in Figure 20.
(b) Plot the isotherms.
50. Project Problem: Harmonic measures of several disjoint intervals. Generalize the result of Exercise 48 as follows. Suppose that $I_{1}, I_{2}, \ldots, I_{n}$ are disjoint open intervals on the $r$-axis, and $T_{1}, T_{2}, \ldots, T_{n}$ are real numbers. Consider the Dirichlet problem in the upper half-plane with boundary condition

$$
u(x, 0)= \begin{cases}T_{j} & \text { if } x \text { in } I_{j} \\ 0 & \text { otherwise } .\end{cases}
$$

Show that the solution is

$$
u(x, y)=\frac{1}{\pi} \sum_{j=1}^{n} T_{j} \alpha_{j}(x, y),
$$

where $\omega_{j}(x, y)$ is the angle at ( $x, y$ ) subtended by the interval $I_{j}$.
51. Project Problem: Approximation of steady-state solutions. Consider the Dirichlet problem in the upper half-plane with boundary values $u(x, 0)=f(x)$
$(-\infty<x<\infty)$, where $f(x)$ is an arbitrary function that represents the temperature of the points on the $x$-axis. In this exercise, we will show how we can use the result of Exercise 50 to approximate the solution for a given $f(x)$. The approach that we take has merit, since it can be used to obtain approximate numerical values for the steady-state temperature. Moreover, we will use it in Exercise 52 to justify the Poisson integral formula in the upper half-plane.

To be able to compare our numerical approximation with the exact solution, let us take $f(x)=\left(1+x^{2}\right)^{-1},-\infty<x<\infty$. In this case, using properties of the Poisson integral, we have the solution

$$
u(x, y)=\frac{1+y}{x^{2}+(1+y)^{2}}
$$

(see Exercise 6, Section 7.5).
(a) Pretend that we do not know the exact solution and proceed to find an approximate solution. The idea is to approximate $f(x)$ by a function that takes on constant values on disjoint intervals. Take the interval $(-5,5)$ and subdivide it into 40 smaller intervals of equal length, $\left(x_{j}, x_{j+1}\right), j=1,2, \ldots, 40$. Approximate $f$ on $\left(x_{j}, x_{j+1}\right)$ by $f\left(x_{j}\right)$, and by 0 outside the interval $(-5,5)$. Thus the boundary valucs are now replaced by

$$
u(x, 0)= \begin{cases}\frac{1}{1+x_{j}^{2}} & \text { if } x_{j}<x<x_{j+1} \\ 0 & \text { otherwise }\end{cases}
$$

Show that the solution is

$$
u(x, y)=\frac{1}{\pi} \sum_{j=1}^{40} \frac{1}{1+x_{j}^{2}} \alpha_{j}(x, y)
$$

where $\alpha_{j}(x, y)$ is the angle at $(x, y)$ subtended by the interval $\left(x_{j}, x_{j+1}\right)$.
(b) With the help of a computer, evaluate your approximate solution at various points, $\left(x_{0}, y_{0}\right)$, in the upper half-plane and compare with the exact solution (13).
52. Project Problem: From the harmonic measure to the Poisson integral formula. Consider the Dirichlet problem in the upper half-plane with boundary values $u(x, 0)=f(x),-\infty<x<\infty$, whose solution is given by the Poisson integral formula

$$
u(s, y)=\frac{y}{\pi} \int_{-\infty}^{\infty} \frac{f(x)}{(s-x)^{2}+y^{2}} d x, \quad-\infty<s<\infty, y>0
$$

Our goal in this exercise is to obtain this formula by using the numerical scheme of Exercise 51.
(a) Based on the approach in Exercise 51, explain how you would derive the approximate solution

$$
u_{\mathrm{app}}(s, y)=\frac{1}{\pi} \sum_{j=1}^{n} f\left(x_{j}\right) \alpha_{j}(s, y)
$$

where $x_{j}$ are equally spaced points on the $x$-axis and $\alpha_{j}(s, y)$ is the angle at the point $(s, y)$ subtended by the interval $\left(x_{j}, x_{j+1}\right)$.
(b) Show that

$$
u_{\text {app }}(s, y)=\frac{1}{\pi} \sum_{j=1}^{n} f\left(x_{j}\right)\left(\operatorname{Arg}\left(z-x_{j+1}\right)-\operatorname{Arg}\left(z-x_{j}\right)\right),
$$

where $z=s+i y$.
(c) Use the mean value theorem to show that there exists a $\xi_{j}$ in the interval $\left(x_{j}, x_{j+1}\right)$ such that $\operatorname{Arg}\left(z-x_{j+1}\right)-\operatorname{Arg}\left(z-x_{j}\right)=\frac{y}{\left(s-\xi_{j}\right)^{2}+y^{2}} \Delta x$, where $\Delta x= x_{j+1}-x_{j}$.
(d) Thus the approximate solution

$$
u_{\mathrm{app}}(s, y)=\frac{y}{\pi} \sum_{j=1}^{n} \frac{f\left(x_{j}\right)}{\left(s-\xi_{j}\right)^{2}+y^{2}} \Delta x .
$$

Let $\Delta x \rightarrow 0$ and explain why $u_{\text {app }}(s, y)$ should approach the Poisson integral (14). Hint: Interpret $u_{\text {app }}(s, y)$ as a Riemann sum that approximates the Poisson integral (14).]
53. Complete the details of Example 2(f) to show that $\log z$ is analytic off its branch cut and then show that its derivative is $\frac{1}{z}$.
54. Show that if $v$ is the harmonic conjugate of $u$, then $-u$ is the harmonic conjugate of $v$. [Hint: If $f=u+i v$ is analytic, what can you say about $i f$ ?]

### 12.6 Solving Dirichlet Problems with Conformal Mappings

In solving a Dirichlet problem, it is sometimes advantageous to map the region under consideration to a simpler region or one on which the transformed problem is easier to solve. This is the idea behind the method of conformal mappings, which we now explain. Let a Dirichlet problem be given on a region $\Omega$ with boundary $\Gamma$. Suppose that we want to solve this problem by somehow transforming it first to the $w$-plane by means of a mapping $w=f(z)$, where $f$ is analytic on $\Omega$. If $f^{\prime}(z) \neq 0$ for all $z$ on $\Omega$, we call $f$ a conformal mapping of $\Omega$. These mappings are known to preserve the angles between curves and their orientation, and thus the term conformal. One of the important properties of a conformal mapping $f$ is that it takes regions into regions; that is, if $\Omega$ is a region (open, connected set), then $\Omega^{\prime}=f[\Omega]$ is also a region. More important, if $f$ is one-to-one, then $f$ will map $\Gamma$, the boundary of $\Omega$, into $\Gamma^{\prime}$, the boundary of $\Omega^{\prime}$. Although we will not prove these results. they can be checked on a case-by-case basis in the examples of this section. (See [1] for the proofs.)

When we apply the conformal mapping method to a Dirichlet problem. we need to know what happens to the equation and the boundary conditions. Because $f$ maps boundary to boundary, the boundary conditions on $\Gamma$ will be transformed into boundary conditions on $\Gamma^{\prime}$ as we will explain shortly. However, the most important feature of the method is stated in the next theorem. It tells us that Laplace's equation is invariant under a conformal mapping.

## THEOREM 1 INVARIANCE OF LAPLACE'S EQUATION

To understand the meaning of $U \circ f(:)$, where $f$ is complexvalued and ${ } i$ is a function of two variables, write $U \circ f(z)=U(\operatorname{Re} f(z), \operatorname{Im} f(z))$. For example, if $f(z)= e^{z}=e^{x} \cos y+i e^{x} \sin y$ and $U(s, t)=s t$. then $U \circ f(z)= e^{2 x} \cos y \sin y$.

Figure 1 If $f(z)$ is analytic and one-to-one on $\Omega$ and its boundary $I$ ', then $\Omega^{\prime}=f[\Omega]$ is a region with boundary $\Gamma^{\prime}= f[\Gamma]$. The boundary function $b(z)$ ( $z$ on $\Gamma$ ) is used to define a boundary function $b \circ f^{-1}(w)$ for all $w$ on $\Gamma^{\prime}$. where $f^{-1}$ is the inverse of $f$.

Suppose that $f$ is an analytic function mapping a region $\Omega$ into a region $\Omega^{\prime}$, and $U$ is a harmonic function on $\Omega^{\prime}$. Then the function $\phi=U \circ f$ is harmonic on $\Omega$. Thus, if $U$ satisfies $\nabla^{2} U=0$ on $\Omega^{\prime}$. then $\phi=U \circ f$ satisfies $\nabla^{2} \phi=0$ on $\Omega$.

Proof Let $z_{0}$ be a point in $\Omega$ and $w_{0}=f\left(z_{0}\right)$. By Theorem 4. Section 12.5, $U$ has a harmonic conjugate $V$ on a disk around $w_{0}$. Then $U+i V$ is analytic on this disk, and by the composition of analytic functions, $(U+i V) \circ f$ is analytic at $z_{0}$. Hence by Theorem 3, Section 12.5. $\operatorname{Re}[(U+i V) \circ f]=\operatorname{Re}[U \circ f+i(V \circ f)]=U \circ f$ is harmonic at $z_{0}$. Since $z_{0}$ is arbitrary, it follows that $U \circ f$ is harmonic on $\Omega$.

Now suppose that you want to use a conformal mapping $w=f(z)$ to solve the Dirichlet problem $\nabla^{2} \phi=0$ in $\Omega$ and $\phi(z)=b(z)$ on the boundary $\Gamma$ of $\Omega$. Suppose also that $f$ is one-to-one on $\Omega$ and its boundary $\Gamma$. Here is how the method works (see Figure 1 as you read through the steps).
![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-54_434_992_848_650.jpg)

Step 1: Describe clearly the region $\Omega^{\prime}=f[\Omega]$ and its boundary $\Gamma^{\prime}=f[\Gamma]$ in the $w$-plane.
Step 2: Since $f$ is one-to-one, we have an inverse function $f^{-1}$ defined on $\Omega^{\prime}$ and $\Gamma^{\prime}$. For $w$ on $\Gamma^{\prime}, f^{-1}(w)$ is on $\Gamma$ and so we can define the function $b \circ f^{-1}(w)$ for all $w$ on $\Gamma^{\prime}$. This determines the boundary values on $\Gamma^{\prime}$.
Step 3: Set up and solve the Dirichlef problem on $\Omega^{\prime}$ consisting of Laplace's equation $\nabla^{2} U(w)=0$ for all $w$ in $\Omega^{\prime}$ and $V^{\prime}(w)=b \circ f^{-1}(w)$ for all $w$ on $\Gamma^{\prime}$. (This is our transformed Dirichlet problem.)
Step 4: Let $\phi(z)=l^{c} \circ f(z)$ for all $z$ in $\Omega$. Then $\phi(z)$ is a solution of our original Dirichlet problem on $\Omega$. Indeed, by Theorem $1, \phi$ is harmonic on $\Omega$. For $z$ on $\Gamma, f(z)$ belongs to $\Gamma^{\prime}$, and $\phi(z)=U \circ f(z)=b \circ f^{-1}(f(z))=b(z)$. Hence " satisfies the desired boundary condition.

In what follows, we illustrate the conformal mappings method with several examples. We will give the conformal mapping and focus on the remaining details of the solution. The actual construction of the conformal mapping could be by itself a very challenging problem. Also, in Examples 1-3, Steps 2 and 3 can be performed without actually computing $f^{-1}$.

In the first example, we use the analytic mapping $f(z)=z^{2}$. Since

![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-55_334_458_451_45.jpg)
Figure 2 The Dirichlet problem in Example 1.

Figure 3 Transsorming a Dirichlet problem from the first quadrant onto the upper half-plane. Notice the boundary correspondence.
squaring a complex number doubles its argument, it is not hard to see that $f(z)$ maps the first quadrant $\Omega$ onto the upper half-plane $\Omega^{\prime}$. It is also one-to-one in the first quadrant.

## EXAMPLE 1 Conformal mapping method

Solve the Dirichlet problem in the first quadrant $\Omega$ shown in Figure 2.
Solution We use the method of conformal mappings to transform the given problem into a problem on the upper half-plane. As we will see momentarily, the transformed problem is easy to solve.
Step 1: As wo just discussed, $f(z)=z^{2}$ takes $\Omega$ in the $z$-plane onto the upper half of the $w$-plane (Figure 3). Moreover, the boundary of $\Omega$ is mapped to the boundary of the upper half-plane as follows. The nonnegative real line ( $x \geq 0$ ) is mapped to the nonnegative real line ( $u \geq 0$ ), and the imaginary semi-axis iy with $y \geq 0$ is mapped to the nonpositive real line ( $u \geq 0$ ).
Step 2: Describe the boundary function in the Dirichlet problem in the $w$-plane. The boundary function in the $w$-plane is $b \circ f^{-1}(w)$, where $b(z)$ is the boundary function in the $z$-plane. With the help of Figure 3, we see that $b \circ f^{-1}((u, 0))=0$ if $|u|>1$ and $b \circ f^{-1}((u, 0))=100$ if $|u|<1$.
Step 3: The transformed Dirichlet problem in the upper half-plane is described by Figure 3 and given by

$$
\begin{aligned}
& \nabla^{2} U(u)=0, w \text { in the upper half-plane; } \\
& U(u, 0)=0,|u|>1, \quad U(u, 0)=100,|u|<1 .
\end{aligned}
$$

![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-55_334_1196_1354_566.jpg)

To solve the boundary value problem in the $w$-plane, we appeal to Example 5, Section 12.5, and get $U(w)=\frac{100}{\pi}(\operatorname{Arg}(w-1)-\operatorname{Arg}(w+1))$.
Step 4: The solution of the original Dirichlet problem in the $z$-plane is $\phi(z)= U(f(z))=\frac{100}{\pi}\left[\operatorname{Arg}\left(z^{2}-1\right)-\operatorname{Arg}\left(z^{2}+1\right)\right]$. In terms of $x$ and $y$, we have $z^{2}-1= x^{2}-y^{2}-1+2 i x y$ and $z^{2}+1=x^{2}-y^{2}+1+2 i x y$. Since the imaginary parts of $z^{2}-1$ and $z^{2}+1$ are positive, we use the inverse cotangent, as in the previous section, and get

$$
\begin{aligned}
\phi(x, y) & =\frac{100}{\pi}\left[\operatorname{Arg}\left(x^{2}-y^{2}-1+2 i x y\right)-\operatorname{Arg}\left(x^{2}-y^{2}+1+2 i x y\right)\right] \\
& =\frac{100}{\pi}\left[\cot ^{-1}\left(\frac{x^{2}-y^{2}-1}{2 x y}\right)-\cot ^{-1}\left(\frac{x^{2}-y^{2}+1}{2 x y}\right)\right] .
\end{aligned}
$$

$$
\begin{aligned}
& f(-1)=1 / e, f(1)=e \\
& f(i \pi)=-1 \\
& f(x)>0, f(x+i \pi)<0
\end{aligned}
$$

Let us quickly verify some of the boundary conditions. If $0<x<1$ and $y \rightarrow 0^{+}$, then $\frac{x^{2}-y^{2}-1}{2 x y} \rightarrow-\infty$ and $\frac{x^{2}-y^{2}+1}{2 x y} \rightarrow+\infty$. Hence

$$
\lim _{y \rightarrow 0^{+}}\left[\cot ^{-1}\left(\frac{x^{2}-y^{2}-1}{2 x y}\right)-\cot ^{-1}\left(\frac{x^{2}-y^{2}+1}{2 x y}\right)\right]=\pi-0=\pi
$$

and so $\lim _{y \rightarrow 0^{+}} \phi(x, y)=100$, if $0<x<1$, which is in agreement with the boundary condition. The other boundary values can be verified similarly.

The next example uses the analytic function $f(z)=e^{z}=e^{x}(\cos y+ i \sin y$ ), where $z=x+i y$ belongs to the horizontal strip $\Omega$ in Figure 4. If $z=x$ is real, then $f(z)=e^{x}$; hence $f$ maps the real line onto the positive real axis $u>0$ in the $w$-plane. If $z=x+i \pi$, then $f(z)=e^{x+i \pi}=e^{x} e^{i \pi}=-e^{x}$. Hence $f$ maps the horizontal line $y=\pi$ onto the negative real axis $u<0$ in the $w$-plane. You can check that for $z$ in $\Omega, f(z)$ is in the upper half-plane and that $f[\Omega]$ is equal to the upper half-plane.

## EXAMPLE 2 The exponential function as a conformal mapping

Solve the Dirichlet problem on the horizontal strip $\Omega$ shown in Figure 4.
Solution We follow the four steps of the conformal mapping method.
Step 1: We already verified that $f(z)=\epsilon^{2}$ takes $\Omega$ in the $z$-plane onto the upper half of the $w$-plane, and takes the boundary of $\Omega$ to the boundary of the upper half-plane.
Step 2: Reviewing carefully the effect of $f$ on the boundary, we find that $f$ maps the interval $[-1,1]$ on the $x$-axis onto the interval $\left[\frac{1}{e}, e\right]$ on the $u$-axis in the $w$-plane. Thus the boundary values for the problem on the region $\Omega^{\prime}$ are $U((u, 0))=T$ if $u$ is in $\left[\frac{1}{e}, c\right]$ and $U((u, 0))=0$ otherwise.
Step 3: To solve the transformed boundary value problem, we appeal to Example 5, Section 12.5, and get

$$
U(w)=\frac{T}{\pi}\left[\operatorname{Arg}(w-e)-\operatorname{Arg}\left(w-\frac{1}{e}\right)\right]
$$

Figure 4 Mapping the horizontal strip by $f(z)=e^{z}$ onto the upper half-plane. Some special values:
![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-56_341_1196_1701_594.jpg)

Step 4: The solution of the original Dirichlet problem in the $z$-plane is $\%(x, y)= U(f(z))=\frac{T}{\pi}\left[\operatorname{Arg}\left(e^{z}-e\right)-\operatorname{Arg}\left(e^{z}-\frac{1}{e}\right)\right]$. Using the inverse cotangent and the
explicit formula for '' we get

$$
\begin{aligned}
\phi(x, y) & =\frac{T}{\pi}\left[\operatorname{Arg}\left(e^{x} \cos y-e+i e^{x} \sin y\right)-\operatorname{Arg}\left(e^{x} \cos y-\frac{1}{e}+i e^{x} \sin y\right)\right] \\
& =\frac{T}{\pi}\left[\cot ^{-1}\left(\frac{e^{x} \cos y-e}{e^{x} \sin y}\right)-\cot ^{-1}\left(\frac{e^{x} \cos y-\frac{1}{e}}{e^{x} \sin y}\right)\right] \\
& =\frac{T}{\pi}\left[\cot ^{-1}\left(\frac{\cos y-e^{1} x}{\sin y}\right)-\cot ^{-1}\left(\frac{\cos y-e^{-(x+1)}}{\sin y}\right)\right] .
\end{aligned}
$$

It is instructive to verify the boundary condition for this solution.
Our next example uses the function $f(z)=\sin z$.

## EXAMPLE 3 The sine function as a conformal mapping

Solve the Dirichlet problem in the semi-infinite strip $\Omega$ shown in Figure 5.
Solution We use the analytic function $f(z)=\sin z$.
Step 1: To determine the image of $\Omega$, we use the fact that $\sin z$ is a one-to-one conformal mapping on $\Omega$ (you should check these properties). We will show that $f$ maps the boundary of $\Omega$ onto the real axis in the $w$-plane. This will imply that the image of $\Omega$ is either the upper or lower half-plane. Wo then determine which half-plane it is by checking the image of just one point in $\Omega$.

Let us determine the image of the boundary of $\Omega$. The line segment $\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$ on the $x$-axis is mapped onto the line segment $[-1,1]$ in the $w$-plane, because the image of the interval $\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$ by the function $\sin x$ is the interval $[-1,1]$. We claim that the vertical half-line $x=\frac{\pi}{2}$ and $y \geq 0$ is mapped onto the half-line $[1, \infty)$ in the $w$-plane. To see this, use

$$
\sin z=\sin x \cosh y+i \cos x \sinh y
$$

(Example 1 (d), Section 12.5). If $x=\frac{\pi}{2}$, then $\sin z=\cosh y$. As $y$ varies in $(0, \infty)$, $\cosh y$ varies in the interval $(1, \infty)$, establishing our claim. Similarly, we show that $\sin z$ maps the vertical half-line $x=-\frac{\pi}{2}$ and $y \geq 0$ onto the half-line $(-\infty,-1]$ in the $w$-plane. In conclusion, $\sin z$ maps the boundary of $\Omega$ onto the real line in the $u$-plane. Now pick one point in $\Omega$, say $z=i$. We have $f(i)=\sin i=i \sinh 1$, which is a point in the upper half of the $w$-plane. Thus $f$ maps $\Omega$ onto the upper half-plane.
Step 2: From the boundary correspondence that we just described, we derive the following boundary values for the Dirichlet problem in the upper half of the $w$-plane:

$$
C^{r}(u, 0)= \begin{cases}0 & \text { if } u>0 \\ 100 & \text { if } u<0\end{cases}
$$

Step 3: The transformed Dirichlet problem in the upper half-plane is described by Figure 5. Its solution is derived immediately with the help of the argument function. We have $U(w)=\frac{100}{\pi} \operatorname{Arg} w$, because $\operatorname{Arg} w=0$ if $w$ is real and positive, and $\operatorname{Arg} w=\pi$ if $w$ is real and negative.

![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-58_518_461_853_72.jpg)
Figure 6 Isotherms and curves of heat flow.

Figure 5 Mapping the semiinfinite vertical strip onto the upper half-plane. Note the boundary correspondence.
![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-58_383_1131_206_631.jpg)

Step 4: The solution of the original Dirichlet problem in the $z$-plane is $\phi(z)= U(f(z))=\frac{100}{\pi} \operatorname{Arg}(\sin z)$. To express our answer in terms of $x$ and $y$, we use the real and imaginary parts of $\sin z$ and the inverse cotangent. We have

$$
\operatorname{Arg}(\sin z)=\cot ^{-1}\left(\frac{\sin x \cosh y}{\cos x \sinh y}\right)=\cot ^{-1}(\tan x \operatorname{coth} y) .
$$

Hence

$$
\phi(z)=\phi(x, y)=\frac{100}{\pi} \cot ^{-1}(\tan x \operatorname{coth} y) .
$$

In Figure 6 we show the isotherms and the curves of heat flow. (For the equation of the curves of heat flow, see Exercise 38.) A few gcometric observations can be made. Note that at the top of Figure 6, the isotherms look like vertical lines. This is to be expected, since the lower boundary, being remote, can be ignored, and we may think of the problem as one on a doubly infinite vertical strip, in which the isotherms are vertical lines. Near the origin, the isotherms look like rays, and the curves of heat flow like circles. These are the isotherms and curves of leat flow in a Dirichlet problem with boundary data constant on rays. This too is to be expected since near the origin the vertical boundary data have less effect as compared with the boundary data on the $x$-axis. So near the origin, we can ignore the vertical boundary data and consider only the horizontal boundary data, which is constant on rays in this case and so the isotherms and curves of heat flow are circular arcs (see Example 7, Section 12.5). $\square$

The following example deals with a circular region, bounded by the rays at angle $0 \leq \alpha_{1}$ and $\alpha_{2} \leq \pi$, and the circular arcs with radii $a$ and $b$, as shown in Figure 7. Such a region is mapped to a rectangle in the $w$-plane using the function $f(z)=\log z$. To see this, consider a line segment $L$ on the ray at angle $\alpha$, where $\alpha_{1} \leq \alpha \leq \alpha_{2}$. For : on this ray, we have $\operatorname{Arg} z=\alpha$ and so $\log z=\ln |z|+i \operatorname{Arg} z=\ln |z|+i \alpha$. As $|z|$ varies from $a$ to $b, \ln |z|$ varies from $\ln a$ to $\ln b$, and thus $\log z$ describes the horizontal line segment $u+i \alpha$, where $\ln a \leq u \leq \ln b$. By letting $\alpha$ vary from $\alpha_{1}$ to $\alpha_{2}$, the image of the line segment $L$ sweeps the rectangular area with vertices $\left(\ln a, \alpha_{1}\right)$. $\left(\ln b, \alpha_{1}\right),\left(\ln b, \alpha_{2}\right)$ and $\left(\ln a, \alpha_{2}\right)$, as shown in Figure 7.

Figure $7 \log z$ is a one-toone conformal mapping of the circular region onto a rectangle. The boundary of the circular region is mapped onto the boundary of the rectangle in the following manner: Side \# $j$ in the domain is mapped to side $\# j$ in the range.
![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-59_401_983_247_732.jpg)

The mapping $\log z$ allows us to transform problems on circular regions to problems on rectangles on which we can use the method of separation of variables (Section 3.8).

EXAMPLE $4 \quad \log z$ as a conformal mapping, separation of variables Solve the Dirichlet problem in the circular region $\Omega$ shown in Figure 8. (Notice that on the circular boundary, the boundary function is not constant: It is equal to $\operatorname{Arg} z$.)

Solution Step 1: As we just explained, the mapping $f(z)=\log z$ takes $\Omega$ in the $z$-plane onto the rectangle in the $w$-plane, as shown in Figure 8, and the boundary sides correspond as described in Figure 8.

Step 2: As in previous examples, the boundary values on sides $\# 1$ and $\# 3$ are constant. They are equal to 0 and $\pi$, respectively. To determine the boundary values on sides \#2 and \#4, we use the fact that the boundary function in the $w^{1}$ plane is $b \circ f^{-1}(w)$, where $b(z)$ is the boundary function in the $z$-plane. The inverse mapping is $f^{-1}(w)=e^{w}$. For $w$ on side $\# 2$, write $w=2+i v$, where $0 \leq v \leq \pi$. Then the boundary value at $w$ is given by $\operatorname{Arg}\left(e^{w}\right)=\operatorname{Arg}\left(e^{2+i v}\right)=\operatorname{Arg}\left(e^{2} e^{i v}\right)=v$. Hence the boundary function on side \#2 is $U(2, v)=v$. In a similar way. you can show that $U(1, v)=v$. Thus the boundary function in the transformed problem is as described in Figure 8.
![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-59_403_1078_1708_682.jpg)

Step 3: The transformed Dirichlet problem in the rectangle is described by Figure 8. We state it here using the variables $s$ and $t$ in place of $u$ and $v$ to simplify the
formulas:

$$
\begin{aligned}
& \nabla^{2} U(s, t)=0, \quad 1 \leq s \leq 2, \quad 0 \leq t \leq \pi \\
& U(s, 0)=0 . \quad U(s, \pi)=\pi, \quad 1<s<2 \\
& U(1, t)=t, \quad U(2, t)=t, \quad 0<t<\pi
\end{aligned}
$$

To solve the boundary value problem in the $w$-plane, we use the method of separation of variables (Section 3.8). The solution has three nonzero parts corresponding to the nonzero boundary values on sides $\# 2,3$, and 4 . Furthermore, to use the results of Section 3.8, we must position the lower left vertex of the rectangle at the origin. We do this by translating the rectangle one unit to the left. With this in mind, we apply (9), Section 3.8 (with $a=1$, and $b=\pi$ ), and let $s=x+1$ or $x=s-1$. Then

$$
\begin{aligned}
U(s, t)= & \sum_{n=1} B_{n} \sin [n \pi(s-1)] \sinh n \pi t \\
& +\sum_{n=1} C_{n} \sinh [n(2-s)] \sin n t+\sum_{n=1} D_{n} \sinh [n(s-1)] \sin n t
\end{aligned}
$$

where

$$
\begin{aligned}
B_{n} & =\frac{2}{\sinh \left(n \pi^{2}\right)} \int_{0}^{1} \pi \sin n \pi s d s \\
C_{n}=D_{n} & =\frac{2}{\pi \sinh n} \int_{0}^{\pi} t \sin n t d t
\end{aligned}
$$

Evaluating the integrals, we find

$$
\begin{aligned}
B_{n} & =\frac{2}{n \sinh \left(n \pi^{2}\right)}(1-\cos n \pi) \\
C_{n}=D_{n} & =\frac{-2}{n \sinh n} \cos n \pi=\frac{2}{n \sinh n}(-1)^{n+1}
\end{aligned}
$$

Thus

$$
\begin{aligned}
U(s, t)= & \sum_{n=1} \frac{2}{n \sinh \left(n \pi^{2}\right)}(1-\cos n \pi) \sin [n \pi(s-1)] \sinh n \pi t \\
& +\sum_{n=1} \frac{2}{n \sinh n}(-1)^{n+1} \sinh [n(2-s)] \sin n t \\
& +\sum_{n=1} \frac{2}{n \sinh n}(-1)^{n+1} \sinh [n(s-1)] \sin n t
\end{aligned}
$$

Step 4: The solution of the original Dirichlet problem in the $z$-plane is

$$
\phi(x, y)=\phi(z)=U(f(z))=U(\ln |z|+i \operatorname{Arg} z)=U\left(\ln \left(\sqrt{x^{2}+y^{2}}\right), \cot ^{-1}\left(\frac{x}{y}\right)\right)
$$

So

$$
\begin{aligned}
\phi(x, y)= & \sum_{n=1} \frac{2(1-\cos n \pi)}{n \sinh \left(n \pi^{2}\right)} \sin \left[n \pi\left(\ln \left(\sqrt{x^{2}+y^{2}}\right)-1\right)\right] \sinh \left[n \pi \cot ^{-1}\left(\frac{x}{y}\right)\right] \\
& +\sum_{n=1} \frac{2}{n \sinh n}(-1)^{n+1} \sinh \left[n\left(2-\ln \left(\sqrt{x^{2}+y^{2}}\right)\right]\right) \sin \left[n \cot ^{-1}\left(\frac{x}{y}\right)\right] \\
& +\sum_{n=1} \frac{2}{n \sinh n}(-1)^{n+1} \sinh \left[n\left(\ln \left(\sqrt{x^{2}+y^{2}}\right)-1\right)\right] \sin \left[n \cot ^{-1}\left(\frac{x}{y}\right)\right]
\end{aligned}
$$

It is a good exercise to check the boundary conditions for this solution.
As we mentioned earlier, and as clearly illustrated by the examples of this section, the construction of a conformal mapping could be a very challenging problem. Additional interesting examples will be presented in the exercises and in the next section.

## Exercises 12.6

In Exercises 1-4, an analytic function $f(z)$ is given from the $x y$-plane into the $u v$ plane, and a harmonic function $U(u, v)$ is defined on the range of $f$.
(a) Verify that $f$ is analytic and $U$ is harmonic.
(b) Find the real and imaginary parts of $f(z)$ and write $f(z)=u(x, y)+i v(x, y)$.
(c) Let $\phi(x, y)=U \circ f(z)$. Compute $\phi$ explicitly in terms of $x$ and $y$ and erplain why $\phi$ is harmonic.

1. $f(z)=\frac{1}{z} ; U(u, v)=u v$.
2. $f(z)=\frac{1}{z} ; U(u, v)=e^{u} \cos v$.
3. $f(z)=e^{z} ; U(u, v)=u^{2}-v^{2}$.
4. $f(z)=z^{2} ; U(u, v)=\ln \left(u^{2}+v^{2}\right)$.
5. Refer to the mapping $f(z)=e^{z}$ in Example 2. Let $S=\{x+i y: x=a, b \leq y \leq c\}$ be a vertical line segment in the $x y$-plane.
(a) Show that $f[S]$ is a circular arc in the $u v$-plane with radius $e^{a}$.
(b) Plot $S$ and $f[S]$ in the two cases when $a=1, b=0$, and $c=\frac{\pi}{2}$ and $\pi$.
6. Refer to the mapping $f(z)=\sin z$ in Example 3. Let

$$
S=\left\{x+i y:-\frac{\pi}{2} \leq x \leq \frac{\pi}{2}, y=y_{0}>0\right\}
$$

be a horizontal line segment in the region $\Omega$ in the $x y$-plane (Figure 5).
(a) Show that $f[S]$ is the upper half of an ellipse in the $u v$-plane, with $u$-intercepts at $\pm \cosh y_{0}$ and $v$-intercept at $\sinh y_{0}$.
(b) Plot $S$ and $f[S]$ in the two cases: $y_{0}=1$ and $y_{0}=.1$.
(c) Which region in the $w$-plane is swept by $f[S]$ as $y_{0}$ varies from 0 to $\infty$ ?
7. Verify the boundary conditions for the solution in Example 3.
8. Verify the boundary conditions for the solution in Example 4.
![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-62_342_479_359_52.jpg)
9.

Figure 9
12.

![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-62_328_469_835_59.jpg)
Figure 12

15. 

![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-62_329_477_1301_72.jpg)
Figure 15

18. 

![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-62_328_484_1773_70.jpg)
Figure 18

10. 

![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-62_338_467_359_664.jpg)
Figure 10

13. 

![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-62_328_467_835_666.jpg)
Figure 13

16. 

![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-62_328_476_1304_678.jpg)
Figure 16

19. 

![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-62_331_470_1773_666.jpg)
Figure 19

In Exercises 9-20 (Figures 9-20), Follow the four-step method of this section to solve
11.

![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-62_329_461_366_1269.jpg)
Figure 11

14. 

![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-62_331_475_832_1283.jpg)
Figure 14

17. 

![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-62_331_463_1301_1269.jpg)
Figure 17

20. 

![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-62_331_463_1773_1271.jpg)
Figure 20

In Exercises 21-24 (Figures 21-24), solve the Dirichlet problem using the method of Example 4.

![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-63_381_470_305_19.jpg)
Figure 21

22. 

![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-63_327_447_359_465.jpg)
Figure 22

23. 

![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-63_327_440_359_909.jpg)
Figure 23

24. 

![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-63_324_449_359_1347.jpg)
Figure 24

25. Translation. Let $z_{0}=a_{0}+i b_{0}$ be a given complex number. Explain why the mapping $f(z)=z+z_{0}$ is a translation by the vector $\left(a_{0}, b_{0}\right)$.
26. Rotation and dilation. Let $z_{0}=r e^{i \theta_{0}}$ be a given complex number with $r=\left|z_{0}\right| \neq 0$. Explain why the mapping $f(z)=z_{0} \cdot z$ is a dilation by a factor $\left|z_{0}\right|$, followed by a rotation by an angle $\theta_{0}$. (The order of the dilation and the rotation does not matter: You can apply the rotation first. and then the rotation.) [Hint: What does multiplication do to the moduli and arguments of two complex numbers?]
27. If $f(z)$ is a rotation by an angle $\alpha$, what is a formula for $f(z)$ ?
28. Describe the mapping $f(z)=\alpha z+\beta$, where $\alpha$ and $\beta$ are complex numbers.

In Exercises 29-36, let $S$ be the square with vertices at $1-i, 1+i,-1+i$, and $-1-i$, and let $C$ be the unit circle, centered at the origin.
29. Describe the image of $S$ by the mapping $f(z)=z+1-i$.
30. Describe the image of $S$ by the mapping $f(z)=z-2-3 i$.
31. Describe the image of $S$ by the mapping $f(z)=i z$.
32. Describe the image of $S$ by the mapping $f(z)=i z+1+i$.
33. Describe the image of $S$ by the mapping $f(z)=e^{i \frac{\pi}{4}} z+1$.
34. Describe the image of $S$ by the mapping $f(z)=e^{-i \frac{\pi}{4}} z-1-i$.
35. Describe the image of $C$ by the mapping $f(z)=3 e^{i \alpha} z+1$, where $\alpha$ is a real number.
36. Describe the image of $C$ by the mapping $f(z)=3 e^{i \frac{\pi}{4}} z-1-i$.
37. Suppose that $f: \Omega \longrightarrow \Omega^{\prime}$ is analytic, $U$ is harmonic on $\Omega^{\prime}$, and let $\phi=U \circ f$. Let $V$ be a harmonic conjugate of $U$. Show that $\psi^{\prime}=V \circ f$ is a harmonic conjugate of $\phi$.
38. Using the result of Exercise 37, find a harmonic conjugate of the solution in Example 3, then determine the equation of the curves of heat flow.

### 12.7 Green's Functions and Conformal Mappings

In this section we present useful formulas for Green's function on a simply connected region $\Omega$ in terms of conformal mappings of $\Omega$ onto the unit disk or the upper half-plane. We then calculate these formulas explicitely for regions such as disks, half-planes, sectors, and strips (semi-infinite and infinite). Wo begin by setting the notation: $D$ denotes the open unit disk, $C$ the unit circle, and $\Omega$ a simply connected region other than the entire plane, with boundary $\Gamma$. Thus $\Omega$ is open, connected, with no holes in it, and its boundary is nonempty. For $z_{0}$ in $\Omega$, let $\phi\left(z, z_{0}\right)$ denote a one-to-one conformal mapping of $\Omega$ onto $D$, such that $\phi$ maps the boundary $\Gamma$ into $C$ and $\phi\left(z_{0}, z_{0}\right)=0$ (Figure 1). Thus

$$
\left|\phi\left(z, z_{0}\right)\right|=1 \text { for all } z \text { on } \Gamma .
$$

## THEOREM 1 CONFORMAL MAPPING FORMULA FOR GREEN'S FUNCTION

Figure 1 Because $\phi\left(z, z_{0}\right)$ belongs to the unit circle if $z$ is on $\Gamma$, we have $\left|\phi\left(z, z_{0}\right)\right|=1$ for $z$ on $\Gamma$. Moreover, since $\phi$ is one-to-one, $z_{0}$ is the only complex number in $\Omega$ such that $\phi\left(z, z_{0}\right)=0$.
![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-64_433_992_804_648.jpg)

Write $z=x+i y$ and $z_{0}=x_{0}+i y_{0}$, and think of $\phi\left(s, z_{0}\right)$ as a function of $x$, $y, x_{0}$, and $y_{0}$, in the obvious way. Here is the main result of the section.

Suppose that $\Omega$ is a simply connected region with (nonempty) boundary $\Gamma$. Let $z=x+i y$ and $z_{0}=x_{0}+i y_{0}$ be in $\Omega$, and let $\phi\left(z, z_{0}\right)$ be the conformal mapping as described above. Then the Green's function on $\Omega$ is

$$
G\left(x, y, x_{0}, y_{0}\right)=\ln \left|\phi\left(z, x_{0}\right)\right| .
$$

It is instructive at this point to verify some of the characteristic properties of Green's function that we stated in Theorem 3, Section 12.3, using properties of the conformal mapping $\phi$. We postpone the full proof of the theorem until the end of this section.

- The function $\ln \left|\phi\left(z, z_{0}\right)\right|$ is the composition of $\phi\left(z, z_{0}\right)$ and $\ln |z|$. The function $\phi$ is analytic on $\Omega$ and is nonzero for all $z \neq z_{0}$, because only $z_{0}$ is mapped to 0 in $D$. The function $\ln |z|=\frac{1}{2} \ln \left(x^{2}+y^{2}\right)$ is harmonic for all $z \neq 0$. Consequently, by Theorem 1, Section 12.6, $\ln \left|\phi\left(z, z_{0}\right)\right|$ is harmonic for all $z \neq z_{0}$ in $\Omega$. Thus property (i) of Theorem 3, Section 12.3, is verified.
- Recall that $\phi\left(z, z_{0}\right)$ belongs to the unit circle $C$ if $z$ is on $\Gamma$; hence, for $z$ on $\Gamma,\left|\phi\left(z, z_{0}\right)\right|=1$, and so $\ln \left|\phi\left(z, z_{0}\right)\right|=\ln 1=0$. Thus property (ii) of Theorem 3, Section 12.3, is verified.
- Recall that $\phi\left(z, z_{0}\right)$ belongs to $D$, for all $z$ in $\Omega$. So $\left|\phi\left(z, z_{0}\right)\right| \leq 1$, and so $\ln \left|\phi\left(z, z_{0}\right)\right| \leq 0$, for all $z$ in $\Omega$. Thus property (iii) of Theorem 3, Section 12.3, is verified.
- The symmetry property of $\phi\left(z, z_{0}\right)$ will become more evident as soon as we investigate the conformal mapping $\phi$ (see Theorem 3 of this section).

We make a few additional points regarding Theorem 1.

- According to Theorem 1, we have to construct a conformal mapping of $\Omega$ onto $D$ for each $z_{0}$ in $\Omega$. While this is true, you will shortly see that in fact all we need is just one conformal mapping of $\Omega$ onto $D$.
- The existence of a conformal mapping of $\Omega$ onto $D$ is guaranteed by a famous theorem, called the Riemann mapping theorem, that states that if $\Omega$ is any simply connected region in the complex plane other than the complex plane itself, then there is a one-to-one analytic function $f$ that maps $\Omega$ onto the unit disk $D$. The mapping $f$ is unique if we specify that $f\left(z_{0}\right)=0$ and $f^{\prime}\left(z_{0}\right)>0$, for some $z_{0}$ in $\Omega$.
- While the Riemann mapping theorem does not tells us how to construct the conformal mapping, it does guarantee its existence. Combining this with Theorem 1, we conclude that Green's function exists on any simply connected region. (When $\Omega$ is the entire plane, we take $\left.G\left(z, z_{0}\right)=\ln \left|z-z_{0}\right|.\right)$

Next, we describe all the conformal mappings of the unit disk onto itself. In addition to being interesting in its own right, this result has two purposes for us: We will use it to rederive Green's function on the disk and to simplify the construction of the conformal mapping in Theorem 1.

## Linear Fractional Transformations

Let $a, b, c$, and $d$ be complex numbers with $a d-b c \neq 0$. The function

$$
f(z)=\frac{a z+b}{c z+d}
$$

is called a linear fractional transformation or Möbius transformation. If $c=0, f$ is a linear function and hence it is entire. If $c \neq 0, f(z)$ is a rational function. It is analytic for all $z \neq-\frac{d}{c}$, where the denominator vanishes. The following properties are straightforward to check.

PROPOSITION 1 LINEAR FRACTIONAL TRANSFORMATIONS

THEOREM 2 CONFORMAL MAPPINGS OF THE DISK ONTO ITSELF
(i) A linear fractional transformation is one-to-one.
(ii) The composition of any two linear fractional transformations is another linear fractional transformation.
(iii) The inverse of the linear fractional transformation (3) is the linear fractional transformation

$$
f^{-1}(z)=\frac{d z-b}{-c z+a}
$$

Proof We prove (i) and (iii) and leave (ii) as an exercise. We start with (iii). We have to check that $f \circ f^{-1}(z)=f^{-1} \circ f(z)=z$. We have

$$
\begin{aligned}
f^{-1} \circ f(z) & =\frac{d f(z)-b}{-c f(z)+a}=\frac{\frac{a d z+b d}{c z+d}-b}{\frac{-a c z-b c}{c z+d}+a} \\
& =\frac{a d z+b d-b(c z+d)}{-a c z-b c+a(c z+d)}=z
\end{aligned}
$$

Similarly, we have $f \circ f^{-1}(z)=z$. To prove (i), we use the fact that $f$ has an inverse. Indeed $f\left(z_{1}\right)=f\left(z_{2}\right) \Rightarrow f^{-1} \circ f\left(z_{1}\right)=f^{-1} \circ f\left(z_{2}\right) \Rightarrow z_{1}=z_{2}$.

The next theorem deals with a particular family of linear fractional transformations.

Let $z_{0}$ be a complex number in $D$ (thus $\left.\right|_{0} \mid<1$ ). Consider the linear fractional transformation

$$
f_{z_{0}}(z)=\frac{z-z_{0}}{1-\overline{z_{0}} z} .
$$

Then (i) $f_{z_{0}}$ is analytic on $D$;
(ii) $f_{z_{0}}$ maps $D$ one-to-one onto $D$;
(iii) $f_{z_{0}}$ maps the unit circle onto the unit circle;
(iv) $f_{z_{0}}\left(z_{0}\right)=0$.

Proof Part (iv) is clear. From Proposition 1, we know that $f_{z_{0}}$ is one-to-one. It is also analytic for all $z \neq \frac{1}{\frac{1}{20}^{\circ}}$. But

$$
\left|\frac{1}{\bar{z}_{0}}\right|=\frac{1}{\left|\overline{z_{0}}\right|}=\frac{1}{\left|z_{0}\right|}>1,
$$

because $\left|z_{0}\right|<1$. So the point where $f_{z_{0}}$ is not analytic, $\left(\overline{z_{0}}\right)^{-1}$, is not in $D$, which proves (i). Parts (ii) and (iii) are more interesting. For (iii), let $\varepsilon^{i \theta}$ denote a complex number with modulus 1 . We want to show that $\left|f_{z_{0}}\left(e^{i \theta}\right)\right|=1$. We use tricks with the absolute value and complex conjugation:

$$
\begin{aligned}
&\left|f_{z_{0}}\left(e^{i \theta}\right)\right|=\frac{\left|e^{i \theta}-z_{0}\right|}{\left|1-\overline{z_{0}} e^{i \theta}\right|}=\frac{\left|e^{i \theta}-z_{0}\right|}{\left|e^{i \theta}\left(e^{-i \theta}-\overline{z_{0}}\right)\right|}=\frac{\left|e^{i \theta}-z_{0}\right|}{\left|e^{i \theta}\right| \cdot\left|e^{-i \theta}-\overline{z_{0}}\right|} \\
& \left.=\frac{\left|e^{i \theta}-z_{0}\right|}{\left|e^{-i \theta}-\overline{z_{0}}\right|}=\frac{\left|e^{i \theta}-z_{0}\right|}{\mid \overline{e^{i \theta}}-z_{0}} \right\rvert\, \\
& \left\lvert\, \frac{\left|e^{i \theta}-z_{0}\right|}{\left|e^{i \theta}-z_{0}\right|}=1 .\right.
\end{aligned}
$$

To prove (ii), we note that $f_{z_{0}}[D]$ is a region whose boundary is the unit circle, by (iii). Since $f_{z_{0}}\left(z_{0}\right)=0$, we conclude that this region is $D$.

Using properties of analytic functions, it can be shown that, up to a constant factor of modulus 1 , any one-to-one conformal mapping of the unit disk onto itself is of the form (5) (see [1], Section 6.2). Thus Theorem 2 characterizes all the conformal mappings of the unit disk onto itself. We now combine Theorems 1 and 2 to obtain the Green's function for the unit disk.

## EXAMPLE 1 Green's function for the unit disk

Let $z$ and $z_{0}$ be in $D$. By Theorem 2, $f_{z_{0}}(z)=\frac{z-z_{0}}{1-\overline{z_{0}} z}$ is a one-to-one conformal mapping of the unit clisk onto itself that maps $z_{0}$ to 0 . By Theorem 1 Green's function for the unit disk is

$$
G\left(z, z_{0}\right)=\ln \left|\frac{z-z_{0}}{1-\overline{z_{0}} z}\right| .
$$

To compare with the formula that we found in Section 12.4 , substitute $z=x+i y$ and $z_{0}=x_{0}+i y_{0}$ (Exercise 13).

Our second application of Theorem 2 is to simplify the construction of the mappings in Theorem 1. We have the following version of Green's formula.

THEOREM 3 CONFORMAL MAPPING FORMULA FOR GREEN'S FUNCTION

Suppose that $\Omega$ is a simply connected region with (nonempty) boundary $\Gamma$. Let $\phi$ be a one-to-one conformal mapping of $\Omega$ onto the unit disk. Let $\approx=x+i y$ and $\varepsilon_{0}=x_{0}+i y_{0}$ be in $\Omega$. Then Green's function for $\Omega$ is

$$
G\left(x, y, x_{0}, y_{0}\right)=\ln \left|\frac{\phi(z)-\phi\left(\sigma_{0}\right)}{1-\overline{\phi\left(\sigma_{0}\right)} \phi(z)}\right| .
$$

It is immediate from (7) that Greens function is symmetric (Thcorem 3 (v). Section 12.3); that is, $G\left(z, z_{0}\right)=G\left(z_{0}, z\right)$.
Proof Note that the function insicle the absolute value in (7) is $f_{\phi\left(z_{0}\right)} \circ \phi(z)$, where $f_{\phi\left(z_{0}\right)}$ is a linear fractional transformation of the form (5), with $z_{0}$ replaced by $\phi\left(z_{0}\right)$. Since $\phi$ is a one-to-one conformal mapping of $\Omega$ onto $D$ and $f_{\phi\left(z_{0}\right)}$ is a one-to-one conformal mapping of $D$ onto $D$. it follows that $f_{\phi\left(z_{0}\right)} \circ \phi(z)$ is a one-to-one conformal mapping of $\Omega$ onto $D$. Clearly, $f_{\phi\left(z_{0}\right)} \circ \phi\left(z_{0}\right)=0$; hence the mapping $f_{\phi\left(z_{0}\right)} \circ \phi(z)$ has all the properties of the mapping $\phi\left(z . z_{0}\right)$ in Theorem 1, and so Theorem 3 follows now from Theorem 1.

From this point, the scope of the applications is unlimited. For example, given a simply connected region $\Omega$, (a) find a one-to-one conformal mapping of $\Omega$ onto the unit $D$. (b) Use Theorem 3 to get the Green's function for $\Omega$. (c) Use results, such as the ones of Section 12.3, to derive formulas for the solutions of Dirichlet problems and Poisson equations on $\Omega$.

Our examples in Section 12.6 involved conformal mappings from a region $\Omega$ onto the upper half-plane. To be able to use these examples with

Theorem 3, we now describe a conformal mapping of the upper half-plane onto the unit disk. Then by composing mappings, we obtain a conformal mapping of the region $\Omega$ onto the unit disk.

To construct the desired conformal mapping, we use a linear fractional transformation and the following properties:

- A linear fractional transformation is uniquely determined by the images of three points.
- The image of a circle by a linear fractional transformation is another circle or a line, and the image of a line is also a circle or a line.

The first property follows because we may assume that one of the coefficients in the linear fractional transformation is 1 . Then the other three coefficients are uniquely determined by three equations with three unknowns. One way to prove the second property is to verify it first in the case of a linear mapping. Next, verify it for the inversion mapping, $f(z)=\frac{1}{z}$. Then because an arbitrary linear fractional transformation is the composition of linear mappings and inversions, it follows that the property holds for lincar fractional transformations.

## EXAMPLE 2 Mappings between the upper half-plane and the unit disk

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
Solution (a) Our goal is to show that the unit circle $C$ is mapped to the real axis. Because the image of a circle is either a line or a circle and because three points determine either a line or a circle, it suffices to check the images of three points on the unit circle. We have

$$
\phi(1)=0 ; \quad \phi(i)=i \frac{1-i}{1+i}=1 ; \quad \phi(-i)=i \frac{1+i}{1-i}=-1 .
$$

Thus $\phi(1), \phi(i)$, and $\phi(-i)$ lie on the $u$-axis (the real axis in the $u$-planc), and so the image of $C$ is the $u$-axis. Because $\phi$ is one-to-one, it maps the boundary $C$ onto the boundary of the image of the unit disk. Thus the image of the unit disk is either the upper half-plane or the lower half-plane. Checking $\phi(0)=i$ (a point in the upper half-plane), we conclude that $\phi$ maps the unit disk one-to-one onto the upper half-plane (see Figure 2).

Figure 2 One-fo one conformal mappings between the unit disk and the upper halfplane.
![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-69_427_992_245_634.jpg)

(b) We can do this part in at least two ways. One way is to use Proposition 1(iii) and notice that $\psi$ is the inverse of $\phi$. Another way is to check the image by $\psi$ of the boundary and one interior point. We leave it as an exercise to verify that $\psi(0)=1$, $\psi(1)=i$, and $\psi(-1)=-i$. Since the images of the three points are not collinear. we conclude that the real axis is mapped onto the circle that goes through the points $1, i$, and $-i$, which is clearly the unit circle. (Here again, we are using the fact that three points determine a circle.) Also, $v(i)=0$; hence $i$ - maps the upper half-plane onto the unit disk.

Example 2(b) and Theorem 3 combine to give us Green's function for the upper half-plane. The formula was derived in Section 12.4 by the method of images.

## EXAMPLE 3 Green's function for the upper half-plane

Let $z$ and $z_{0}$ be in the upper half-plane. Then Green's function for the upper half-plane is

$$
G\left(\therefore z_{0}\right)=\ln \left|\frac{z-z_{0}}{z-\overline{z_{0}}}\right|=\frac{1}{2} \ln \frac{\left(x-x_{0}\right)^{2}+\left(y-y_{0}\right)^{2}}{\left(x-x_{0}\right)^{2}+\left(y+y_{0}\right)^{2}} .
$$

To derive the formula, we use (7) and the conformal mapping in Example 2(b):

$$
\begin{aligned}
G\left(c, z_{0}\right) & =\ln \left|\frac{\frac{i-z}{i+z}-\frac{i-z_{0}}{i+z_{0}}}{1-\overline{\left(\frac{i-z_{0}}{i+z_{0}}\right)} \frac{i-z}{i+z}}\right|=\ln \left|\frac{\frac{(i-z)\left(i+z_{0}\right)-\left(i-z_{0}\right)(i+z)}{(i+z)\left(i+z_{0}\right)}}{1-\frac{-i-\overline{z_{0}}}{-i+z_{0}} \frac{i-z}{i+z}}\right| \\
& =\ln \left|\frac{\frac{2 i\left(z_{0}-z\right)}{(i+z)\left(i+z_{0}\right)}}{\frac{2 i\left(\overline{z_{0}}-z\right)}{(i+z)\left(-i+\overline{z_{0}}\right)}}\right|=\ln \left|\frac{z-z_{0}}{z-\overline{z_{0}}} \frac{-i+\overline{z_{0}}}{i+\overline{z_{0}}}\right|=\ln \left(\left|\frac{z-z_{0}}{z-\overline{z_{0}}}\right|\left|\frac{-i+\overline{z_{0}}}{i+z_{0}}\right|\right) .
\end{aligned}
$$

But $-i+\overline{z_{0}}$ is the complex conjugate of $i+z_{0}$, so $\left|\frac{\overline{-i+\bar{z}_{0}}}{i+z_{0}}\right|=1$, and the formula follows. $\square$

We now add a new Green's function to our list.

![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-70_456_466_1595_65.jpg)
Figure 3 A general Dirichlet problem in the first quadrant.

## EXAMPLE 4 Green's function for the first quadrant

Let us start by constructing a one-to-one conformal mapping of the first quadrant onto the unit disk by mapping the first quadrant onto the upper half-plane and then using the mapping in Example 2(b). Thus $\phi(z)=\frac{i-z^{2}}{i+z^{2}}$ is a one-to-one conformal mapping of the first quadrant onto the unit disk. For $z$ and $z_{0}$ in the first quadrant, use Theorem 3 to get the Green's function for the first quadrant in the form

$$
G\left(z, z_{0}\right)=\ln \left|\frac{\frac{i-\phi(z)}{i+\phi(z)}-\frac{i-\phi\left(z_{0}\right)}{i+\phi\left(z_{0}\right)}}{1-\overline{\left(\frac{i-\phi\left(z_{0}\right)}{i+\phi\left(z_{0}\right)}\right)} \overline{i-\phi(z)} \overline{i+\phi(z)}}\right| .
$$

This is the same expression as what we had in the previous example, except that $z$ and $z_{0}$ are now replaced by $\phi(z)$ and $o\left(i_{0}\right)$. Using the result of the previous example, we find:

$$
G\left(z, z_{0}\right)=\ln \left|\frac{\phi(z)-\phi\left(z_{0}\right)}{\phi(z)-\overline{\phi\left(z_{0}\right)}}\right|=\ln \left|\frac{z^{2}-z_{0}^{2}}{z^{2}-{\overline{z_{0}}}^{2}}\right| .
$$

To express $G$ in terms of $x, y, x_{0}$, and $y_{0}$, we proceed as follows:

$$
\begin{aligned}
G\left(x, y, x_{0}, y_{0}\right)= & \ln \left|\left(z-z_{0}\right)\left(z+z_{0}\right)\right|-\ln \left|\left(z-\overline{z_{0}}\right)\left(z+\overline{z_{0}}\right)\right| \\
= & \ln \left|z-z_{0}\right|+\ln \left|z+z_{0}\right|-\ln \left|z-\overline{z_{0}}\right|-\ln \left|z+\overline{z_{0}}\right| \\
= & \frac{1}{2} \ln \left(\left(x-x_{0}\right)^{2}+\left(y-y_{0}\right)^{2}\right)+\frac{1}{2} \ln \left(\left(x+x_{0}\right)^{2}+\left(y+y_{0}\right)^{2}\right) \\
& -\frac{1}{2} \ln \left(\left(x-x_{0}\right)^{2}+\left(y+y_{0}\right)^{2}\right)-\frac{1}{2} \ln \left(\left(x+x_{0}\right)^{2}+\left(y-y_{0}\right)^{2}\right) \\
= & \frac{1}{2} \ln \frac{\left(\left(x-x_{0}\right)^{2}+\left(y-y_{0}\right)^{2}\right)\left(\left(x+x_{0}\right)^{2}+\left(y+y_{0}\right)^{2}\right)}{\left(\left(x-x_{0}\right)^{2}+\left(y+y_{0}\right)^{2}\right)\left(\left(x+x_{0}\right)^{2}+\left(y-y_{0}\right)^{2}\right)} .
\end{aligned}
$$

In the following example, we use Green's function to derive a Poisson integral formula for the first quadrant.

## EXAMPLE 5 Poisson integral formula for the first quadrant

Consider the Dirichlet problem in the first quadrant $\Omega$, shown in Figure 3: $\nabla^{2} u(x, y)=$ 0 for all $(x, y)$ in $\Omega ; u(x, 0)=f(x)$ for all $x>0, u(0, y)=g(y)$ for all $y>0$. Show that the solution is given by the Poisson integral formula:

$$
\begin{aligned}
u(x, y)= & \frac{y}{\pi} \int_{0}^{\infty} f(s)\left(\frac{1}{(x-s)^{2}+y^{2}}-\frac{1}{(x+s)^{2}+y^{2}}\right) d s \\
& +\frac{x}{\pi} \int_{0}^{\infty} g(t)\left(\frac{1}{x^{2}+(y-t)^{2}}-\frac{1}{x^{2}+(y+t)^{2}}\right) d t
\end{aligned}
$$

Solution According to Theorem 2, Section 12.3,

$$
u\left(x_{0}, y_{0}\right)=\frac{1}{2 \pi} \int_{\Gamma} u(x, y) \frac{\partial G}{\partial n}\left(x, y, x_{0}, y_{0}\right) d s
$$

where $G$ is the Green's function for the first quadrant, and $\Gamma$ is the boundary of the first quadrant. On the nonnegative $x$-axis, we have $d s=d x$ and $\frac{\partial G}{\partial n}=-\left.\frac{\partial G}{\partial y}\right|_{y=0}$.

THEOREM 4 CONFORMAL MAPPING FORMULA FOR GREEN'S FUNCTION

On the nonnegative $y$-axis, we have $d s=d y$ and $\frac{\partial G}{\partial n}=-\left.\frac{\partial G}{\partial x}\right|_{x=0}$. Using the explicit formula for $G$ from Example 4, we compute:

$$
\begin{aligned}
-\frac{\partial G}{\partial y}= & \frac{\partial}{\partial y}\left[-\frac{1}{2} \ln \left(\left(x-x_{0}\right)^{2}+\left(y-y_{0}\right)^{2}\right)-\frac{1}{2} \ln \left(\left(x+x_{0}\right)^{2}+\left(y+y_{0}\right)^{2}\right)\right] \\
& +\frac{\partial}{\partial y}\left[\frac{1}{2} \ln \left(\left(x-x_{0}\right)^{2}+\left(y+y_{0}\right)^{2}\right)+\frac{1}{2} \ln \left(\left(x+x_{0}\right)^{2}+\left(y-y_{0}\right)^{2}\right)\right] \\
= & -\frac{y-y_{0}}{\left(x-x_{0}\right)^{2}+\left(y-y_{0}\right)^{2}}-\frac{y+y_{0}}{\left(x+x_{0}\right)^{2}+\left(y+y_{0}\right)^{2}} \\
& +\frac{y+y_{0}}{\left(x-x_{0}\right)^{2}+\left(y+y_{0}\right)^{2}}+\frac{y-y_{0}}{\left(x+x_{0}\right)^{2}+\left(y-y_{0}\right)^{2}} .
\end{aligned}
$$

Setting $y=0$. we find that on the $x$-axis

$$
\begin{aligned}
\frac{\partial G}{\partial n} & =\frac{y_{0}}{\left(x-x_{0}\right)^{2}+y^{2}}-\frac{y_{0}}{\left(x+x_{0}\right)^{2}+y_{0}^{2}}+\frac{y_{0}}{\left(x-x_{0}\right)^{2}+y_{0}^{2}}-\frac{y_{0}}{\left(x+x_{0}\right)^{2}+y_{0}^{2}} \\
& =\frac{2 y_{0}}{\left(x-x_{0}\right)^{2}+y^{2}}-\frac{2 y_{0}}{\left(x+x_{0}\right)^{2}+y_{0}^{2}} .
\end{aligned}
$$

In a similar way, we find that on the $y$-axis

$$
\frac{\partial G}{\partial n}=\frac{2 x_{0}}{x_{0}^{2}+\left(y-y_{0}\right)^{2}}-\frac{2 x_{0}}{x_{0}^{2}+\left(y+y_{0}\right)^{2}}
$$

Substituting into (11), we obtain the desired Poisson integral formula (up to a relabeling of the variables).

The steps that we took to go from (9) to (10) in Example 4 can be applied with any conformal mapping. This yields the following variation on Theorem 3, which may be more useful in computations.

Suppose that $\Omega$ is a simply connected region with (nonempty) boundary $\Gamma$. Let $\phi$ be a one-to-one conformal mapping of $\Omega$ onto the upper half-plane. taking $\Gamma$ into the real line. Then Green's function for $\Omega$ is

$$
G\left(x, y, x_{0}, y_{0}\right)=\ln \left|\frac{\phi(z)-\phi\left(z_{0}\right)}{\phi(z)-\overline{\phi\left(z_{0}\right)}}\right|,
$$

where $z=x+i y$ and $z_{0}=x_{0}+i y_{0}$ are in $\Omega$.
Here is an interesting application.
EXAMPLE 6 Green's function for a semi-infinite vertical strip
Let $\Omega$ be the semi-infinite vertical strip $\left\{z=x+i y:-\frac{\pi}{2} \leq x \leq \frac{\pi}{2}, y \geq 0\right\}$. The function $\phi(z)=\sin z$ is a one-to-one conformal mapping of $\Omega$ onto the upper half-plane. (See Example 3, Section 12.6.) Thus by Theorem 4, Green's function for $\Omega$ is

$$
G\left(z, z_{0}\right)=\ln \left|\frac{\sin z-\sin z_{0}}{\sin z-\overline{\sin z_{0}}}\right|=\ln \left|\sin z-\sin z_{0}\right|-\ln \left|\sin z-\overline{\sin z_{0}}\right|
$$

## THEOREM 5 COMPOSITION OF GREEN'S FUNCTIONS AND CONFORMAL MAPPINGS

To express $G$ in terms of $x, y, x_{0}$, and $y_{0}$, you can use the formula for $\sin z$ in terms of these variables. We leave the details to the exercises.

The following theorem describes yet another way to construct new Green's functions by composing known Green's functions with one-to-one conformal mappings. The proof of the theorem is very much like the proof of Theorem 1 and will be left to the exercises.

Suppose that $\Omega$ and $\Omega^{\prime}$ are simply connected regions with (nonempty) boundaries $\Gamma$ and $\Gamma^{\prime}$, respectively. Suppose that $\phi$ is a one-to-one conformal mapping of $\Omega$ onto $\Omega^{\prime}$, such that $\phi[\Gamma]$ is contained in $\Gamma^{\prime}$. Let $g\left(x, y, x_{0}, y_{0}\right)=g\left(x+i y, x_{0}+i y_{0}\right)$ denote the Green's function for $\Omega^{\prime}$. Then Green's function for $\Omega$ is

$$
G\left(x, y, x_{0}, y_{0}\right)=g\left(\phi(x+i y), \phi\left(x_{0}+i y_{0}\right)\right)
$$

As an illustration, write Green's function for the upper half-plane in the form $g\left(x, y, x_{0}, y_{0}\right)=\ln \left|z-z_{0}\right|-\ln \left|z-\bar{z}_{0}\right|$ (Example 3). Let $\phi(z)$ denote a one-to-one conformal mapping of a region $\Omega$ onto the upper half-plane, taking $\Gamma$ into the real line. Then Green's function for $\Omega$ is

$$
G\left(x, y, x_{0}, y_{0}\right)=\ln \left|\phi(z)-\phi\left(z_{0}\right)\right|-\ln \left|\phi(z)-\overline{\phi\left(z_{0}\right)}\right|
$$

which is the formula in Theorem 4.
We close this section by completing the proof of Theorem 1. The proof requires some properties of analytic functions that are recalled where needed.
Proof of Theorem 1. Suppose that $\Omega$ is a simply connected region with (nonempty) boundary $\Gamma . z=x+i y$ and $z_{0}=x_{0}+i y_{0}$ are in $\Omega$, and $\phi\left(z, z_{0}\right)$ is a one-to-one conformal mapping of $\Omega$ onto the unit disk. We want to show that Green's function for $\Omega$ is given by (2): $G\left(z, z_{0}\right)=\ln \left|\phi\left(z, z_{0}\right)\right|$. We have already proved that the function $\ln \left|\infty\left(z, z_{0}\right)\right|$ is harmonic on $\Omega$, except at $z=z_{0}$, and that it vanishes on the boundary of $\Omega$. To prove that it is the Green's function for $\Omega$, by (2), Section 12.3, we must show that, for $z \neq z_{0}$,

$$
\ln \left|\phi\left(z, z_{0}\right)\right|=\frac{1}{2} \ln \left(\left(x-x_{0}\right)^{2}+\left(y-y_{0}\right)^{2}\right)+h\left(z, z_{0}\right)=\ln \left|z-z_{0}\right|+h\left(z, z_{0}\right)
$$

where $h$ is harmonic for all $z$ in $\Omega$. We need the following fact about analytic functions. Suppose that $f(z)$ is analytic in a disk containing $z_{0}$, but not at $z_{0}$. Then $z_{0}$ is called an isolated singularity. It is a fact that if $z_{0}$ is an isolated singularity and $\lim _{z \rightarrow z_{0}} f(z)=A$ exists, then $z_{0}$ is a removable singularity. That is, if we define $f\left(z_{0}\right)=A$, then $f$ becomes analytic at $z_{0}$ (see [1], Section 4.6). With this property in mind. consider the function $f(z)=\frac{\phi\left(z, z_{0}\right)}{z-z_{0}}\left(z \neq z_{0}\right.$ in $\left.\Omega\right)$, where, as in Theorem 1. $\phi\left(z, z_{0}\right)$ is analytic on $\Omega$ and $\phi\left(z_{0}, z_{0}\right)=0$. It is clear that $f$ is analytic on $\Omega$ except at $z_{0}$. Thus $z_{0}$ is an isolated singularity of $f$. Also,

$$
\lim _{z \rightarrow 0} f(z)=\lim _{z \rightarrow z_{0}} \frac{\phi\left(z, z_{0}\right)}{z-z_{0}}=\lim _{z \rightarrow z_{0}} \frac{\phi\left(z, z_{0}\right)-\overbrace{\phi\left(z_{0}, z_{0}\right)}^{=0}}{z-z_{0}}=\left.\frac{d}{d z} \phi\left(z, z_{0}\right)\right|_{z=z_{0}},
$$

![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-73_325_462_1384_52.jpg)
Figure 4 A general Dirichlet problem on a horizontal strip (Exercises 9 and 10).

by definition of the derivative. Hence $z_{0}$ is a removable singularity of $f(z)$. Define

$$
f(z)= \begin{cases}\frac{\phi\left(z, z_{0}\right)}{z-z_{0}} & \text { if } z \neq z_{0} \\ \left.\phi^{\prime}\left(z, z_{0}\right)\right|_{z=z_{0}} & \text { if } z=z_{0}\end{cases}
$$

Then $f$ is analytic on $\Omega$. Also, $f(z) \neq 0$ for all $z$ in $\Omega$. This last assertion is clear for $z \neq z_{0}$, since $\phi$ is onc-to-one and $\phi\left(z_{0}, z_{0}\right)=0$. For $z=z_{0}$, we use the fact that $\phi$ is one-to-one to infer that $\phi^{\prime}\left(z, z_{0}\right) \neq 0$ for all $z$ in $\Omega$; in particular, $\left.\phi^{\prime}\left(z, z_{0}\right)\right|_{z=z_{0}} \neq 0$. Now, set $h\left(z, z_{0}\right)=\ln |f(z)|$. Then $h$ is harmonic on $\Omega$, by Theorem 1, Section 12.6, because it is the composition of the analytic function $f$ and the harmonic function $\ln |z|(z \neq 0)$. For $z \neq z_{0}$, using the definition of $f(z)$, we see that

$$
\begin{aligned}
\ln \left|z-z_{0}\right|+h\left(z, z_{0}\right) & =\ln \left|z-z_{0}\right|+\ln |f(z)| \\
& \left.=\ln \left|z-z_{0}\right|+\ln \left|\phi\left(z, z_{0}\right)\right|-\ln \mid z-z_{0}\right)|=\ln | \phi\left(z, z_{0}\right) \mid .
\end{aligned}
$$

Thus (15) holds.

## Exercises 12.7

In Exercises 1-8, find Green's function for the region $\Omega$.

1. $\Omega$ is the open disk of radius 1 and center at $(1,0)$.
2. $\Omega$ is the open disk of radius 2 and center at $(4,4)$.
3. $\Omega$ is the half-plane above the line $y=x$.
4. $\Omega$ is the half-plane to the right of the line $x=1$.
5. $\Omega$ is the infinite horizontal strip bounded by the lines $y=0$ and $y=\pi$.
6. $\Omega$ is the infinite horizontal strip bounded by the lines $y=0$ and $y=\frac{\pi}{2}$.
7. $\Omega$ is the infinite sector bounded by the rays through the origin at angles 0 and $\frac{\pi}{4}$.
8. $\Omega$ is the infinite sector bounded by the rays through the origin at angles 0 and $\frac{3 \pi}{4}$.
9. Derive a Poisson integral formula that solves the Dirichlet problem on the horizontal strip in Figure 4 for the case when $f(x)=0$ and $g(x)$ is arbitrary.
10. Derive a Poisson integral formula that solves the Dirichlet problem on the horizontal strip in Figure 4 when both $f(x)$ and $g(x)$ are arbitrary
11. Solve the Dirichlet problem in the first quadrant in Figure 3, given that $f(x)=x$ if $0<x<1$ and 0 otherwise, and $g(y)=0$ for all $y>0$.
12. Derive a Poisson integral formula for the semi-infinite strip in Example 6.
13. Show that the formula that we found in Example 1 for Green's function for a disk is identical with the formula that we have in Section 12.4.
14. Study the proof of Theorem 1 and then prove Theorem 5.

### 12.8 Neumann Functions and the Solution of Neumann Problems

We use the methods of the previous sections to solve the Neumann problem on a simply connected region $\Omega$, other than the entire plane:

$$
\begin{aligned}
\nabla^{2} u(x, y) & =0 \text { for all }(x, y) \text { in } \Omega \\
\frac{\partial u}{\partial n}(x, y) & =f(x, y) \text { for all }(x, y) \text { on the boundary } \Gamma .
\end{aligned}
$$

We know from Example 5, Section 12.1. that the boundary function $f$ cannot be arbitrary; it has to satisfy the compatibility condition

$$
\int_{\Gamma} f(x, y) d s=0
$$

Let us recall the meaning of the symbol $d s$, which stands for the element of arc length. If we parametrize the boundary $\Gamma$ by $(x(t), y(t))(a \leq t \leq b)$, then

$$
\int_{\Gamma} f(x, y) d s=\int_{a}^{b} f(x(t), y(t)) \sqrt{\left[x^{\prime}(t)\right]^{2}+\left[y^{\prime}(t)\right]^{2}} d t
$$

Just as we expressed the solution of the Dirichlet problem as a line integral involving the boundary function and Green's function, our goal here is to express the solution of the Neumann problem as a line integral involving the boundary function and a fixed function, known as a Neumann function, that depends only on the region. Motivated by properties of Green's function (see Theorem 3, Section 12.3), we make the following definition.

## DEFINITION 1 NEUMANN FUNCTIONS

Suppose that $\Omega$ is a simply connected region with boundary $\Gamma$. A Neumann function $N\left(x, y, x_{0}, y_{0}\right)\left((x, y),\left(x_{0}, y_{0}\right)\right.$ in $\left.\Omega\right)$ for the region $\Omega$ is a function with the following properties:
(i) for each $(x, y)$ in $\Omega, N\left(x, y, x_{0}, y_{0}\right)$ is harmonic for all $(x, y) \neq\left(x_{0}, y_{0}\right)$ in Ω:
(ii) $\frac{\partial N}{\partial n}\left(x, y, x_{0}, y_{0}\right)=C$ for all $\left(x_{0}, y_{0}\right)$ in $\Omega$ and $(x, y)$ on $\Gamma$ :
(iii) for each $\left(x_{0}, y_{0}\right)$ in $\Omega$, there is a function $u_{1}$ such that $u_{1}\left(x, y, x_{0}, y_{0}\right)$ is harmonic for all $(x, y)$ in $\Omega$, and $N\left(x, y, x_{0}, y_{0}\right)=v\left(x, y, x_{0}, y_{0}\right)+ u_{1}\left(x, y, x_{0}, y_{0}\right)=\frac{1}{2} \ln \left(\left(x-x_{0}\right)^{2}+\left(y-y_{0}\right)^{2}\right)+u_{1}\left(x, y, x_{0}, y_{0}\right)$ for all $(x, y)$ in $\Omega$.

To simplify the notation, we will write $z=x+i y, z_{0}=x_{0}+i y_{0}$, and denote a function of $\left(x, y, x_{0}, y_{0}\right)$ by a function of $z$ and $z_{0}$; for example, $v\left(z, z_{0}\right)= \frac{1}{2} \ln \left(\left(x-x_{0}\right)^{2}+\left(y-y_{0}\right)^{2}\right)=\ln \left|z-z_{0}\right|$, and $N\left(x, y, x_{0}, y_{0}\right)=N\left(z, z_{0}\right)$. With this notation, parts (i) and (iii) state that a Neumann function, like a Green's function, is harmonic on $\Omega$, except at $z_{0}$, due to the term $\ln \left|z-z_{0}\right|$. Part (ii) tells us that the boundary values of the normal derivative of the Neumann function are constant. This is the counterpart of the boundary condition for a Green's function, which states that a Green's function must

## PROPOSITION 1

## THEOREM 1 SOLUTION OF NEUMANN PROBLEMS

vanish identically on the boundary. As we now show, the constant ( ${ }^{\gamma}$ depends on the length of $\Gamma$ and is not 0 in general.

The constant $C$ in Definition 1(ii), which is cqual to the boundary value of the mormal derivative of the Nemmann function, is given by

$$
C=\frac{2 \pi}{L} .
$$

where $L=\int_{\Gamma} d s$ is the length of $\Gamma$. If $L$ is infinite, we take $C=0$.
Proof For fixed $z_{0}$ in $\Omega$, since $\partial N / \partial n$ is constant on $\Gamma$, we have, on the one hand.

$$
\int_{\Gamma^{\prime}} \frac{\partial}{\partial n} N\left(z, z_{0}\right) d s=\int_{\Gamma} C d s=C L
$$

where $L$ is the length of $\Gamma$. On the other hand, using $N=u_{1}\left(z, z_{0}\right)+\ln \left|z-z_{0}\right|$,

$$
\int_{\Gamma} \frac{\partial}{\partial n} N\left(z, z_{0}\right) d s=\int_{\Gamma} \frac{\partial}{\partial n} u_{1}\left(z, z_{0}\right) d s+\int_{\Gamma} \frac{\partial}{\partial n} \ln \left|z-z_{0}\right| d s=2 \pi
$$

because $\int_{\Gamma} \partial u_{1} / \partial n d s=0$ by the compatibility condition for harmonic functions (Example 5, Section 12.1). and $\int_{\Gamma} \frac{\partial}{\partial n} \ln \left|z-z_{0}\right| d s=2 \pi$, by Exercise 15, Section 12.3. Hence $C L=2 \pi$ and (3) follows.

We are now ready to express the solution of the Neumann problem in terms of the Neumann function. Let us note that from Theorem 5. Section 12.1, if a solution of a Neumann problem exists, then it is unique up to an additive constant, and thus the solution can be determined only up to an additive constant.

Suppose that $\Omega$ is a simply connected region with boundary $\Gamma$, and let $N\left(z, z_{0}\right)$ denote a Neumann function, where $z=x+i y$ and $z_{0}=x_{0}+i y_{0}$ are in $\Omega$. Then, up to an additive constant. the solution $u$ of the Nemmann problem (1) (2) is given by

$$
\left.u\left(x_{0}\right) \cdot y_{0}\right)=-\frac{1}{2 \pi} \int_{1} N\left(z, z_{0}\right) f(z) d s
$$

Proof Suppose that $u$ is a solution and let $A=\frac{C}{2 \pi} \int_{\Gamma} u d s$. We will show that ( $d$ ) determines $u$ up to the constant $A$. We go back to the representation formula for harmonic functions (Theorem 1. Section 12.3):

$$
u\left(x_{0}, y_{0}\right)=\frac{1}{2 \pi} \int_{\Gamma}\left(u \frac{\partial v}{\partial n}-v \frac{\partial u}{\partial n}\right) d s
$$

Unlike the case of a Dirichlet problem, here we must modify the formula in order to get rid of $u$ from the integrand. (Recall $v=\ln \left|z-z_{0}\right|$.) From Definition 1 (ii) and (iii), we see that $\partial v / \partial n=C-\partial u_{1} / \partial n$ on $\Gamma$. Also, since $u$ and $u_{1}$ are harmonic, by

Green's second identity we have $\int_{\Gamma} u_{1} \frac{\partial u}{\partial n} d s=\int_{\Gamma} u \frac{\partial u_{1}}{\partial n} d s$. Thus,

$$
\begin{aligned}
u\left(x_{0}, y_{0}\right) & =\frac{1}{2 \pi} \int_{\Gamma}\left(u\left(C-\frac{\partial u_{1}}{\partial n}\right)-v \frac{\partial u}{\partial n}\right) d s \\
& =\frac{C}{2 \pi} \int_{\Gamma} u d s-\frac{1}{2 \pi} \int_{\Gamma}\left(u_{1} \frac{\partial u}{\partial n}+v \frac{\partial u}{\partial n}\right) d s \\
& =A-\frac{1}{2 \pi} \int_{\Gamma} N\left(z, z_{0}\right) f(z) d s
\end{aligned}
$$

where on the last line, we used $N=u_{1}+v$ and $f=\partial u / \partial n$ on $\Gamma$.

## EXAMPLE 1 Neumann function for the upper half-plane

Verify that a Neumann function for the upper half-plane is

$$
\begin{aligned}
N\left(x, z_{0}\right) & =\ln \left|z-z_{0}\right|+\ln \left|z-\overline{z_{0}}\right| \\
& =\frac{1}{2} \ln \left(\left(x-x_{0}\right)^{2}+\left(y-y_{0}\right)^{2}\right)+\frac{1}{2} \ln \left(\left(x-x_{0}\right)^{2}+\left(y+y_{0}\right)^{2}\right)
\end{aligned}
$$

for $z=x+i y$ and $z_{0}=x_{0}+i y_{0}, y, y_{0}>0$.
Solution We will simply verify that the given function is a Neumann function for the upper half-plane by showing that it has properties (i)-(iii) of Definition 1. Given $z_{0}$ in the upper half-plane, the function $u_{1}\left(z, z_{0}\right)=\ln \left|z-\overline{z_{0}}\right|$ is harmonic for all $z$ except $z=\overline{z_{0}}$. Since $z_{0}$ is in the upper half-plane, $\overline{z_{0}}$ is in the lower half-plane and it follows that $u_{1}\left(z, z_{0}\right)$ is harmonic on the upper half-plane. This establishes (i) and (iii). We now prove (ii). The normal derivative in this case is $-\frac{\partial}{\partial y}$. We have

$$
\begin{aligned}
-\left.\frac{\partial}{\partial y} \ln \left|z-z_{0}\right|\right|_{y=0} & =-\left.\frac{1}{2} \frac{\partial}{\partial y} \ln \left(\left(x-x_{0}\right)^{2}+\left(y-y_{0}\right)^{2}\right)\right|_{y=0} \\
& =\left.\frac{y_{0}-y}{\left(x-x_{0}\right)^{2}+\left(y-y_{0}\right)^{2}}\right|_{y=0}=\frac{y_{0}}{\left(x-x_{0}\right)^{2}+y_{0}^{2}}
\end{aligned}
$$

Since $\operatorname{Im}\left(\overline{z_{0}}\right)=-\operatorname{Im}\left(z_{0}\right)$, we see from the preceding computation (with $z_{0}$ replaced by $\overline{z_{0}}$ ) that

$$
-\left.\frac{\partial}{\partial y} \ln \left|z-\overline{z_{0}}\right|\right|_{y=0}=\frac{-y_{0}}{\left(x-x_{0}\right)^{2}+\left(-y_{0}\right)^{2}}==\frac{-y_{0}}{\left(x-x_{0}\right)^{2}+y_{0}^{2}} .
$$

Adding the two normal derivatives, we find that the normal derivative of $\ln \mid z- z_{0}|+\ln | z-\overline{z_{0}} \mid$ is zero on the real axis. This shows that (ii) of Definition 1 holds with $C=0$.

Let us now solve the Neumann problem in the upper half-plane.

## EXAMPLE 2 Solution of the Neumann problem in the upper half-plane

Applying Theorem 1 and using the Noumann function that we computed in Example 1, we find that a solution of the Noumann problem in the upper half-plane,

$$
\begin{aligned}
& \nabla^{2} u(x, y)=0,-\infty<x<\infty, y>0, \\
& -\frac{\partial u}{\partial y}(x, 0)=f(x),
\end{aligned}
$$

is

$$
u\left(x_{0}, y_{0}\right)=\frac{-1}{2 \pi} \int_{-\infty}^{\infty} f(x) \ln \left(\left(x-x_{0}\right)^{2}+y_{0}^{2}\right) d x
$$

This solution was derived by a different method in Exercise 17, Section 12.4.

## Neumann Functions and Conformal Mappings

We now investigate the action of a conformal mapping on a Neumann function. Our approach is motivated by the results of the previous section. We use the following notation: $\Omega$ and $\Omega^{\prime}$ are two simply connected regions with nonempty boundaries $\Gamma$ and $\Gamma^{\prime}$, and $\phi$ is a one-to-one conformal mapping of $\Omega$ onto $\Omega^{\prime}$, such that $\phi[\Gamma]$ is contained in $\Gamma^{\prime}$. Suppose that $N\left(w, w_{0}\right)$ is a Neumann function for $\Omega^{\prime}$ and form the composition of $N$ with $\phi: N_{\phi}\left(z, z_{0}\right)=N\left(\phi(z), \phi\left(z_{0}\right)\right)$, where $z$ and $z_{0}$ are in $\Omega$. We now ask the question: Is $N_{\phi}\left(z, z_{0}\right)$ a Neumann function for $\Omega$ ?

By following a proof similar to that of Theorem 1, Section 12.5, we can show that $N_{0}\left(z, z_{0}\right)$ is harmonic on $\Omega$, except at $z_{0}$, and that $N_{\phi}\left(z, z_{1}\right)$ :In $\left|z-z_{0}\right|$ plus a harmonic function on $\Omega$. Thus $N_{\phi}\left(z, z_{0}\right)$ has two of the defining properties of a Neumann function for $\Omega$. It remains to verify whether the normal derivative of $N_{\phi}\left(z, z_{0}\right)$ is constant on the boundary, as required by Proposition 1. As it turns out, this property is not satisfied in general. However, it is satisfied when both $\Omega$ and $\Omega^{\prime}$ are not bounded.

To explain this peculiar difference between bounded and unbounded region, we recall the following formula for a change of variables by a conformal mapping:

$$
\frac{\partial\left(N_{\phi}\right)}{\partial n_{\Gamma}}\left(z, z_{0}\right)=\left|\phi^{\prime}(z)\right| \frac{\partial N}{\partial n_{\Gamma^{\prime}}}\left(\phi(z), \phi\left(z_{0}\right)\right)
$$

where on the left side we are computing the normal derivative along the curve $\Gamma$ at the point $z$ on $\Gamma$, and on the right side we are computing the normal derivative along the curve $\Gamma^{\prime}$ at the point $\varphi(z)$ on $\Gamma^{\prime}$. (For a proof, see $[1]$, Section 6.5.) Thus the conformal mapping preserves the normal derivative but scales it by a factor $\left|\phi^{\prime}(z)\right|$. Hence after composing a Neumann function with a conformal mapping, the resulting function may not have a constant normal derivative as expressed by Proposition 1, unless $\left|\phi^{\prime}(z)\right|=1$ or the constant values of the normal derivatives on the boundary are 0 . We know

THEOREM 2 NEUMANN FUNCTION FOR UNBOUNDED REGIONS
by Proposition 1 that the latter condition is satisfied when both $\Gamma$ and $\Gamma^{\prime}$ have infinite length. We thus have the following useful result.

Suppose that $\Omega$ is an unbounded region with boundary $\Gamma$, and $\phi$ is a one-toone analytic mapping of $\Omega$ onto the upper half-plane, taking $\Gamma$ onto the real axis. Then a Nemmann function for $\Omega$ is
(7) $\quad N\left(z, z_{0}\right)=\ln \left|\phi(z)-\phi\left(z_{0}\right)\right|+\ln \left|\phi(z)-\overline{\phi\left(z_{0}\right)}\right| \quad\left(z, z_{0}\right.$ in $\left.\Omega\right)$.

As an application, we derive a Neumann function for the first quadrant.

## EXAMPLE 3 Neumann function for the first quadrant

Applying Theorem 2 with $\phi(z)=z^{2}$, we obtain a. Neumann function for the first quadrant:

$$
\begin{aligned}
N\left(\therefore a_{0}\right)= & \ln \left|z^{2}-z_{0}^{2}\right|+\ln \left|z^{2}-\overline{z_{0}^{2}}\right| \\
= & \ln \left|z-z_{0}\right|+\ln \left|z+z_{0}\right|+\ln \left|z-\overline{z_{0}}\right|+\ln \left|z+\overline{z_{0}}\right| \\
= & \frac{1}{2} \ln \left(\left(x-x_{0}\right)^{2}+\left(y-y_{0}\right)^{2}\right)+\frac{1}{2} \ln \left(\left(x+x_{0}\right)^{2}+\left(y+y_{0}\right)^{2}\right) \\
& +\frac{1}{2} \ln \left(\left(x-x_{0}\right)^{2}+\left(y+y_{0}\right)^{2}\right)+\frac{1}{2} \ln \left(\left(x+x_{0}\right)^{2}+\left(y-y_{0}\right)^{2}\right) .
\end{aligned}
$$

Using this function, you can find the general solution of the Neumann problem in the first quadrant (Exercise 7).

## Poisson Problems with Neumann Conditions

We mention one more application that is directly within our reach. Consider the Poisson problem

$$
\begin{array}{ll}
\nabla^{2} u(x, y)=h(x, y) & \text { for all }(x, y) \text { in } \Omega \\
\frac{\partial u}{\partial n}(x, y)=f(x, y) & \text { for all }(x, y) \text { on } \Gamma .
\end{array}
$$

Bocause of the Neumann type condition on the boundary, the functions $h$ and $f$ are related by Green's first identity, as follows:

$$
\iint_{\Omega} \nabla^{2} u d x d y=\int_{\Gamma} \frac{\partial u}{\partial n} d s
$$

hence by (8) and (9),

$$
\iint_{\Omega} \nabla^{2} h(x, y) d x d y=\int_{\Gamma} f d s
$$

Thus the double integral of $h$ over $\Omega$ must equal the line integral of $f$ over $\Gamma$. Suppose that $h$ and $f$ satisfy this compatibility condition. Then we have the following solution of the Poisson problem with a Neumann condition.

THEOREM 3 SOLUTION OF POISSON-NEUMANN PROBLEM

Suppose that $\Omega$ is a region with boundary $\Gamma$ and let $N\left(z, z_{0}\right)$ denote a Neumann function for $\Omega$, where $z=x+i y$ and $z_{0}=x_{0}+i y_{0}$ are in $\Omega$. If $u(x, y)$ is a solution to Poisson's equation (8) subject to a Neumann boundary con-
2.

![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-79_295_458_846_648.jpg)
Figure 2

5. 

![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-79_292_458_1237_648.jpg)
Figure 5

$$
u(x, y)=\frac{1}{2 \pi} \iint_{\Omega} h(x, y) N\left(z, z_{0}\right) d x d y-\frac{1}{2 \pi} \int_{\Gamma} N\left(z, z_{0}\right) f(z) d s
$$

The proof mirrors the proof of Theorem 4, Section 12.3. It will be omitted.

## Exercises 12.8

In Erercises 1-6. derive the Neumann function for the region depicted in the ac-
3.

![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-79_292_462_846_1251.jpg)
Figure 3

6. 

![](./images/cca7b26c-6b40-433b-b512-db4e7016f7a5-79_287_465_1241_1248.jpg)
Figure 6

7. Solution of the Neumann problem in the first quadrant. Show that the solution of the Nemmann problem

$$
\begin{aligned}
& \nabla^{2} u(x, y)=0, x, y>0 \\
& \frac{\partial u}{\partial y}(x, 0)=f(x), \quad \frac{\partial u}{\partial x}(0, y)=g(y)
\end{aligned}
$$

is

$$
\begin{aligned}
u\left(x_{0} . y_{0}\right)= & \frac{1}{2 \pi} \int_{0}^{\infty} f(x)\left[\ln \left(\left(x-x_{0}\right)^{2}+y_{0}^{2}\right)+\ln \left(\left(x+x_{0}\right)^{2}+y_{0}^{2}\right)\right] d x \\
& +\frac{1}{2 \pi} \int_{0}^{\infty} g(y)\left[\ln \left(x_{0}^{2}+\left(y-y_{0}\right)^{2}\right)+\ln \left(x_{0}^{2}+\left(y+y_{0}\right)^{2}\right)\right] d y
\end{aligned}
$$

8. Verify the following integral formula, which arises from solutions of Neumann
problems such as the one in the previous exercise: For $a, b \neq 0$,

$$
\begin{aligned}
& \int \ln \left[(x-a)^{2}+b^{2}\right] d x \\
& \quad=2(x-a)+2 b \tan ^{-1}\left(\frac{x-a}{b}\right)+(x-a) \ln \left[(x-a)^{2}+b^{2}\right]+C
\end{aligned}
$$

9. (a) Solve the problem in Exercise 7, given that $g(y)=0$ for all $y>0$, and $f(x)=1$ if $0<x<1$ and 0 otherwise.
(b) Verify your answer by direct computation.
10. A Neumann function for the unit disk. This function is defined for : and $z_{0}$ in the unit disk by

$$
N\left(z, z_{0}\right)= \begin{cases}\ln \left|z-z_{0}\right|+\ln \left|\frac{1}{\bar{z}_{0}}-z\right|+\ln \left|z_{0}\right| & \text { if } z_{0} \neq 0 \\ \ln |z| & \text { if } z_{0}=0\end{cases}
$$

Derive this formula by following the outlined steps.
(a) Write $z_{0}=r e^{i \theta}$ and $z=\rho e^{i \eta}$. Fix $z_{0} \neq 0$ and show that

$$
\begin{aligned}
\left.\frac{\partial}{\partial n} \ln \left|z-z_{0}\right|\right|_{\rho=1} & =\left.\frac{\partial}{\partial \rho} \frac{1}{2} \ln \left|z-z_{0}\right|^{2}\right|_{\rho=1} \\
& =\left.\frac{1}{2} \frac{\partial}{\partial \rho} \ln \left(r^{2}+\rho^{2}+2 r \rho \cos (\theta-\eta)\right)\right|_{\rho=1} \\
& =\frac{1+r \cos (\theta \cdots \eta)}{1+r^{2}+2 r \cos (\theta-\eta)}
\end{aligned}
$$

(b) Write $\frac{1}{\bar{z}_{0}}=\frac{1}{r} e^{i \theta}$, use (a), and conclude that

$$
\left.\frac{\partial}{\partial n} \ln \left|\frac{1}{\overline{z_{0}}}-z\right|\right|_{\rho=1}=\frac{1+\frac{1}{r} \cos (\theta-\eta)}{\left(\frac{1}{r}\right)^{2}+1+\frac{2}{r} \cos (\theta-\eta)}=\frac{r^{2}+r \cos (\theta-\eta)}{1+r^{2}+2 r \cos (\theta-\eta)}
$$

(c) Use (a) and (b) to show that for $z_{0} \neq 0,\left.\frac{\partial}{\partial n} N\left(z, z_{0}\right)\right|_{|z|=1}=1$.
(d) Verify the remaining properties of the Neumann function for the given $N\left(z, z_{0}\right)$.
11. Solution of the Neumann problem on the disk. Use the result of the previous exercise to show that the solution of $\nabla^{2} u(r, \theta)=0$ for $0 \leq r<1$ and all $\theta$, given the Neumann condition $\frac{\partial u}{\partial r}(1, \theta)=f(\theta)$, for all $\theta$, is

$$
u(r, \theta)=-\frac{1}{2 \pi} \int_{0}^{2 \pi} f(\eta) \ln \left[1+r^{2}+2 r \cos (\theta-\eta)\right] d \eta
$$

Here $f$ satisfies the compatibility condition $\int_{0}^{2 \pi} f(\theta) d \theta=0$.

