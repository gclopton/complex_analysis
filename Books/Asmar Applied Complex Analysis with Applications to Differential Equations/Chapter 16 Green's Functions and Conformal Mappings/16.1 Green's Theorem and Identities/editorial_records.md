
# Editorial records

Reading note: 16.1 Green's Theorem and Identities.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!proposition] Zero Gradient Implies Constancy on a Connected Region
> If $\Omega\subset\mathbb R^2$ is open and connected and $u\in C^1(\Omega)$ satisfies $u_x=u_y=0$ throughout $\Omega$, then $u$ is constant on $\Omega$.
````
### After

````text
> [!proposition] Zero Gradient Implies Constancy on a Connected Region
> Suppose that $u(x, y)$ is a continuously differentiable function defined on an open connected region $\Omega$ such that $u_x(x,y)=0$ and $u_{y}(x, y)=0$ for all $(x, y)$ in $\Omega$. Then $u$ must be constant on $\Omega$.
````

## 2. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem] Uniqueness of the Classical Dirichlet Solution for Laplace’s Equation
> Let $\Omega\subset\mathbb R^2$ be a bounded connected region with piecewise smooth boundary $\Gamma$. Suppose $u_1,u_2$ are real $C^2$ functions near $\overline\Omega$, harmonic in $\Omega$, and $u_1=u_2$ on $\Gamma$. Then $u_1=u_2$ throughout $\Omega$.
````
### After

````text
> [!theorem] Uniqueness of the Classical Dirichlet Solution for Laplace’s Equation
> Let $\Omega$ be a bounded connected plane region with piecewise smooth boundary $\Gamma$; $n$ denotes its outward unit normal. Functions in boundary identities are $C^2$ near $\overline\Omega$.
>
> Let $\Omega$ be a simply or multiply connected region with boundary $\Gamma$. If $u_{1}$ and $u_{2}$ are harmonic functions on $\Omega$ and $u_{1}=u_{2}$ on the boundary $\Gamma$, then $u_{1}=u_{2}$ on $\Omega$.
````

## 3. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem] Uniqueness up to a Constant for the Classical Neumann Problem
> Let $\Omega\subset\mathbb R^2$ be a bounded connected region with piecewise smooth boundary $\Gamma$ and outward unit normal $n$. If real functions $u_1,u_2\in C^2$ near $\overline\Omega$ are harmonic in $\Omega$ and $\partial_n u_1=\partial_n u_2$ on the smooth pieces of $\Gamma$, then $u_1-u_2$ is constant throughout $\Omega$.
````
### After

````text
> [!theorem] Uniqueness up to a Constant for the Classical Neumann Problem
> Let $\Omega$ be a bounded connected plane region with piecewise smooth boundary $\Gamma$; $n$ denotes its outward unit normal. Functions in boundary identities are $C^2$ near $\overline\Omega$.
>
> Let $\Omega$ be a simply or multiply connected region, with boundary $\Gamma$. If $u_{1}$ and $u_{2}$ are harmonic functions on $\Omega$ and $\frac{\partial u_{1}}{\partial n}=\frac{\partial u_{2}}{\partial n}$ on the boundary $\Gamma$, then $u_{1}=u_{2}+C$ on $\Omega$.
````

## 4. Restore source wording; retain only the actual correction.

### Before

````text
Extending this proof sketch to general piecewise smooth boundaries uses an approximation argument.
````
### After

````text

````

## 5. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!definition] Simple Closed Plane Curve (Jordan Curve)
> A simple closed plane curve (Jordan curve) is the image of a continuous parametrization $C:[a,b]\to\mathbb R^2$ with $a<b$, $C(a)=C(b)$, and no other repeated points: if $a\le t_1<t_2\le b$ and $C(t_1)=C(t_2)$, then $t_1=a$ and $t_2=b$.
````
### After

````text
> [!definition] Simple Closed Curves
> A simple closed plane curve (Jordan curve) is the image of a continuous parametrization $C:[a,b]\to\mathbb R^2$ with $a<b$, $C(a)=C(b)$, and no other repeated points: if $a\le t_1<t_2\le b$ and $C(t_1)=C(t_2)$, then $t_1=a$ and $t_2=b$.
````

## 6. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!convention] Positive Orientation of a Simple Closed Plane Curve
> Orientation. Jordan's theorem allows us to define the orientation of a simple curve $C$. You are moving in the positive direction along $C$ if the interior region is to your left; otherwise. you are moving in the negative direction of $C$. We denote by $-C$ the reverse of $C$. It is the curve that is traversed in the opposite direction as $C$.
````
### After

````text
> [!convention] Orientation
> Orientation. Jordan's theorem allows us to define the orientation of a simple curve $C$. You are moving in the positive direction along $C$ if the interior region is to your left; otherwise. you are moving in the negative direction of $C$. We denote by $-C$ the reverse of $C$. It is the curve that is traversed in the opposite direction as $C$.
````

## 7. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!definition] Open Sets and Connected Regions in the Plane
> Open Sets and Regions. A subset $U$ of the plane is open if for every $\left(x_{0}, y_{0}\right)$ in $U$ there is an open disk $D$ centered at ( $x_{0}, y_{0}$ ) and contained entirely in $U$. In other words, $U$ is open if every point in $U$ is an interior point. Consequently, if $U$ is open, then it cannot contain any of its boundary points, since boundary points are not interior points. An open subset $S$ of the plane is connected if and only if any two points ( $x_{0}, y_{0}$ ) and ( $x_{1}, y_{1}$ ) in $S$ can be joined by a polygonal line that is entirely contained in $S$. (By a polygonal line we mean a curve formed by finitely many line segments joined end to end.) A nonempty open connected subset of the plane is called a region.
````
### After

````text
> [!definition] Open Sets and Regions
> Open Sets and Regions. A subset $U$ of the plane is open if for every $\left(x_{0}, y_{0}\right)$ in $U$ there is an open disk $D$ centered at ( $x_{0}, y_{0}$ ) and contained entirely in $U$. In other words, $U$ is open if every point in $U$ is an interior point. Consequently, if $U$ is open, then it cannot contain any of its boundary points, since boundary points are not interior points. An open subset $S$ of the plane is connected if and only if any two points ( $x_{0}, y_{0}$ ) and ( $x_{1}, y_{1}$ ) in $S$ can be joined by a polygonal line that is entirely contained in $S$. (By a polygonal line we mean a curve formed by finitely many line segments joined end to end.) A nonempty open connected subset of the plane is called a region.
````

## 8. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!definition] Simply Connected and Multiply Connected Plane Regions
> An open connected plane region $D\subseteq\mathbb R^2$ is simply connected if the bounded interior of every simple closed curve lying in $D$ is also contained in $D$. A region that is not simply connected is called multiply connected. Geometrically, a simply connected plane region has no holes.
````
### After

````text
> [!definition] Simply Connected Region
> An open connected plane region $D\subseteq\mathbb R^2$ is simply connected if the bounded interior of every simple closed curve lying in $D$ is also contained in $D$. A region that is not simply connected is called multiply connected. Geometrically, a simply connected plane region has no holes.
````

## 9. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!definition] Line Integrals Along Piecewise Smooth Plane Curves
> Line Integral. If $C$ is a continuous, piecewise continuously differentiable curve parametrized by $(x(t), y(t)), a \leq t \leq b$, and $f(x, y)$ is a continuous function on $C$, we define the line integral of $f$ over $C$ to be
>
> $$
> \int_{C} f(x, y) d s=\int_{a}^{b} f(x(t), y(t)) \sqrt{\left[x^{\prime}(t)\right]^{2}+\left[y^{\prime}(t)\right]^{2}} d t
> $$
>
> Two other integrals will be of interest:
>
> $$
> \int_{C} f(x, y) d x=\int_{a}^{b} f(x(t), y(t)) x^{\prime}(t) d t
> $$
>
> $$
> \int_C f(x,y)\,dy=\int_a^b f(x(t),y(t))y'(t)\,dt.
> $$
````
### After

````text
> [!definition] Line Integral
> Line Integral. If $C$ is a continuous, piecewise continuously differentiable curve parametrized by $(x(t), y(t)), a \leq t \leq b$, and $f(x, y)$ is a continuous function on $C$, we define the line integral of $f$ over $C$ to be
>
> $$
> \int_{C} f(x, y) d s=\int_{a}^{b} f(x(t), y(t)) \sqrt{\left[x^{\prime}(t)\right]^{2}+\left[y^{\prime}(t)\right]^{2}} d t
> $$
>
> Two other integrals will be of interest:
>
> $$
> \int_{C} f(x, y) d x=\int_{a}^{b} f(x(t), y(t)) x^{\prime}(t) d t
> $$
>
> $$
> \int_C f(x,y)\,dy=\int_a^b f(x(t),y(t))y'(t)\,dt.
> $$
````

## 10. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem] Green’s Theorem for a Simply Connected Plane Region
> Let $C$ be a positively oriented, piecewise smooth simple closed plane curve, and let $D$ be its bounded interior. If $M,N$ are real functions of class $C^1$ on a neighborhood of $\overline D$, then
>
> $$
> \int_{C}(M(x, y) d x+N(x, y) d y)=\iint_{D}\left(\frac{\partial N}{\partial x}-\frac{\partial M}{\partial y}\right) d x d y
> $$
````
### After

````text
> [!theorem] Green's Theorem
> Let $C$ be a positively oriented, piecewise smooth simple closed plane curve, and let $D$ be its bounded interior. If $M,N$ are real functions of class $C^1$ on a neighborhood of $\overline D$, then
>
> $$
> \int_{C}(M(x, y) d x+N(x, y) d y)=\iint_{D}\left(\frac{\partial N}{\partial x}-\frac{\partial M}{\partial y}\right) d x d y
> $$
````

## 11. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem] Green’s Theorem for a Multiply Connected Plane Region
> Let $\Omega$ be a bounded plane region whose boundary $\Gamma$ consists of finitely many disjoint piecewise smooth simple closed curves. Orient the outer curve counterclockwise and the inner curves clockwise, so $\Omega$ is on the left. If $M,N\in C^1$ on a neighborhood of $\overline\Omega$, then
>
> $$
> \int_{\Gamma} M(x, y) d x+N(x, y) d y=\iint_{\Omega}\left(\frac{\partial N}{\partial x}-\frac{\partial M}{\partial y}\right) d x d y
> $$
````
### After

````text
> [!theorem] Green's Theorem for Multiply Connected Regions
> Let $\Omega$ be a bounded plane region whose boundary $\Gamma$ consists of finitely many disjoint piecewise smooth simple closed curves. Orient the outer curve counterclockwise and the inner curves clockwise, so $\Omega$ is on the left. If $M,N\in C^1$ on a neighborhood of $\overline\Omega$, then
>
> $$
> \int_{\Gamma} M(x, y) d x+N(x, y) d y=\iint_{\Omega}\left(\frac{\partial N}{\partial x}-\frac{\partial M}{\partial y}\right) d x d y
> $$
````

## 12. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem] Green’s First and Second Identities in the Plane
> Let $\Omega$ be a bounded plane region with a boundary $\Gamma$ consisting of finitely many disjoint piecewise smooth simple closed curves. Let $n$ be the outward unit normal, $ds$ arc length, and $u,v$ real $C^2$ functions on a neighborhood of $\overline\Omega$. Write $\nabla^2=\partial_x^2+\partial_y^2$ and $\partial_n u=\nabla u\cdot n$. Then we have Green's first identity
>
> $$
> \iint_{\Omega}\left(u \nabla^{2} v+\nabla u \cdot \nabla v\right) d x d y=\int_{\Gamma} u \frac{\partial v}{\partial n} d s
> $$
>
> and Green's second identity
>
> $$
> \iint_{\Omega}\left(u \nabla^{2} v-v \nabla^{2} u\right) d x d y=\int_{\Gamma}\left(u \frac{\partial v}{\partial n}-v \frac{\partial u}{\partial n}\right) d s
> $$
````
### After

````text
> [!theorem] Green's Identities
> Let $\Omega$ be a bounded plane region with a boundary $\Gamma$ consisting of finitely many disjoint piecewise smooth simple closed curves. Let $n$ be the outward unit normal, $ds$ arc length, and $u,v$ real $C^2$ functions on a neighborhood of $\overline\Omega$. Write $\nabla^2=\partial_x^2+\partial_y^2$ and $\partial_n u=\nabla u\cdot n$. Then we have Green's first identity
>
> $$
> \iint_{\Omega}\left(u \nabla^{2} v+\nabla u \cdot \nabla v\right) d x d y=\int_{\Gamma} u \frac{\partial v}{\partial n} d s
> $$
>
> and Green's second identity
>
> $$
> \iint_{\Omega}\left(u \nabla^{2} v-v \nabla^{2} u\right) d x d y=\int_{\Gamma}\left(u \frac{\partial v}{\partial n}-v \frac{\partial u}{\partial n}\right) d s
> $$
````

## 13. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem] Uniqueness of the Classical Dirichlet Solution for Laplace’s Equation
> Let $\Omega$ be a bounded connected plane region with piecewise smooth boundary $\Gamma$; $n$ denotes its outward unit normal. Functions in boundary identities are $C^2$ near $\overline\Omega$.
>
> Let $\Omega$ be a simply or multiply connected region with boundary $\Gamma$. If $u_{1}$ and $u_{2}$ are harmonic functions on $\Omega$ and $u_{1}=u_{2}$ on the boundary $\Gamma$, then $u_{1}=u_{2}$ on $\Omega$.
````
### After

````text
> [!theorem] Uniqueness of Solution in a Dirichlet Problem
> Let $\Omega$ be a bounded connected plane region with piecewise smooth boundary $\Gamma$; $n$ denotes its outward unit normal. Functions in boundary identities are $C^2$ near $\overline\Omega$.
>
> Let $\Omega$ be a simply or multiply connected region with boundary $\Gamma$. If $u_{1}$ and $u_{2}$ are harmonic functions on $\Omega$ and $u_{1}=u_{2}$ on the boundary $\Gamma$, then $u_{1}=u_{2}$ on $\Omega$.
````

## 14. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem] Uniqueness up to a Constant for the Classical Neumann Problem
> Let $\Omega$ be a bounded connected plane region with piecewise smooth boundary $\Gamma$; $n$ denotes its outward unit normal. Functions in boundary identities are $C^2$ near $\overline\Omega$.
>
> Let $\Omega$ be a simply or multiply connected region, with boundary $\Gamma$. If $u_{1}$ and $u_{2}$ are harmonic functions on $\Omega$ and $\frac{\partial u_{1}}{\partial n}=\frac{\partial u_{2}}{\partial n}$ on the boundary $\Gamma$, then $u_{1}=u_{2}+C$ on $\Omega$.
````
### After

````text
> [!theorem] Uniqueness of Solution in a Neumann Problem
> Let $\Omega$ be a bounded connected plane region with piecewise smooth boundary $\Gamma$; $n$ denotes its outward unit normal. Functions in boundary identities are $C^2$ near $\overline\Omega$.
>
> Let $\Omega$ be a simply or multiply connected region, with boundary $\Gamma$. If $u_{1}$ and $u_{2}$ are harmonic functions on $\Omega$ and $\frac{\partial u_{1}}{\partial n}=\frac{\partial u_{2}}{\partial n}$ on the boundary $\Gamma$, then $u_{1}=u_{2}+C$ on $\Omega$.
````
