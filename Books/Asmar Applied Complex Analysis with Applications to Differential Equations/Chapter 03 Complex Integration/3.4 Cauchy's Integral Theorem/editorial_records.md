
# Editorial records

Reading note: 3.4 Cauchy's Integral Theorem.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Callout 99: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Straight-Line Homotopies in Convex Plane Regions
> Let $\Omega\subset\mathbb{C}$ be a convex region and let $\gamma_0,\gamma_1:[0,1]\to\Omega$ be paths. The straight-line homotopy
>
> $$
> H(t,s)=(1-s)\gamma_0(t)+s\gamma_1(t),\qquad 0\le t,s\le1,
> $$
>
> stays in $\Omega$. If the paths have the same endpoints, this homotopy fixes those endpoints. If both paths are closed, every intermediate path is closed. In particular, taking $\gamma_1(t)=z_1$ for a fixed $z_1\in\Omega$ contracts any closed path to a point.
````
### After

````text
> [!theorem] Deformation of Paths in Convex Sets
> Suppose that $\Omega$ is a convex region. (i) Any two paths $\gamma_{0}$ and $\gamma_{1}$ in $\Omega$, joining two points $\alpha$ and $\beta$ in $\Omega$, are mutually continuously deformable relative to $\Omega$. The continuous mapping $H$ that deforms $\gamma_{0}$ into $\gamma_{1}$ is given by $H(t,s)=(1-s)\gamma_0(t)+s\gamma_1(t)$, $0\le t,s\le1$.
> (ii) Any two closed paths $\gamma_{0}$ and $\gamma_{1}$ in $\Omega$ are mutually continuously deformable relative to $\Omega$. The continuous mapping $H$ that deforms $\gamma_{0}$ into $\gamma_{1}$ is given by $H(t,s)=(1-s)\gamma_0(t)+s\gamma_1(t)$, $0\le t,s\le1$.
> (iii) Any closed path $\gamma_{0}$ in $\Omega$ is continuously deformable into a point in $\Omega$. The continuous mapping $H$ that deforms a closed path $\gamma_{0}$ into a point $z_{1}$ in $\Omega$ is given by $H(t,s)=(1-s)\gamma_0(t)+s\gamma_1(t)$, $0\le t,s\le1$, where $\gamma_{1}(t)=z_{1}$ is constant for all $t$ in $[0,1]$.
````

## 2. Callout 100: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Cauchy’s Integral Theorem for Homotopic Paths
> Let $f$ be a function analytic in a region $\Omega$. (i) If $\gamma_{0}$ and $\gamma_{1}$ are two paths joining $\alpha$ to $\beta$ in $\Omega$, and if $\gamma_{0}$ is continuously deformable into $\gamma_{1}$ relative to $\Omega$, then
>
> $$
> \int_{\gamma_{0}} f(z) d z=\int_{\gamma_{1}} f(z) d z
> $$
>
> (ii) If $\gamma_{0}$ and $\gamma_{1}$ are closed paths in $\Omega$ and $\gamma_{0}$ is continuously deformable into $\gamma_{1}$ relative to $\Omega$, then
>
> $$
> \int_{\gamma_{0}} f(z) d z=\int_{\gamma_{1}} f(z) d z
> $$
>
> In particular, if $\gamma_{0}$ is a closed path in $\Omega$ that is continuously deformable into a point in $\Omega$, then
>
> $$
> \int_{\gamma_{0}} f(z) d z=0
> $$
````
### After

````text
> [!theorem] Cauchy's Integral Theorem for Deformable Paths
> Let $f$ be a function analytic in a region $\Omega$. (i) If $\gamma_{0}$ and $\gamma_{1}$ are two paths joining $\alpha$ to $\beta$ in $\Omega$, and if $\gamma_{0}$ is continuously deformable into $\gamma_{1}$ relative to $\Omega$, then
>
> $$
> \int_{\gamma_{0}} f(z) d z=\int_{\gamma_{1}} f(z) d z
> $$
>
> (ii) If $\gamma_{0}$ and $\gamma_{1}$ are closed paths in $\Omega$ and $\gamma_{0}$ is continuously deformable into $\gamma_{1}$ relative to $\Omega$, then
>
> $$
> \int_{\gamma_{0}} f(z) d z=\int_{\gamma_{1}} f(z) d z
> $$
>
> In particular, if $\gamma_{0}$ is a closed path in $\Omega$ that is continuously deformable into a point in $\Omega$, then
>
> $$
> \int_{\gamma_{0}} f(z) d z=0
> $$
````

## 3. Callout 101: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!corollary] Vanishing Closed-Path Integrals of Functions Analytic on a Disk
> Suppose that $\gamma$ is a closed path and $f$ is analytic on an open disk containing $\gamma$. Then
>
> $$
> \int_{\gamma} f(z) d z=0
> $$
>
> In particular, if $f$ is entire then the displayed integral is zero for any closed path $\gamma$.
````
### After

````text
> [!corollary] Path Integrals of Functions Analytic on Disks
> Suppose that $\gamma$ is a closed path and $f$ is analytic on an open disk containing $\gamma$. Then
>
> $$
> \int_{\gamma} f(z) d z=0
> $$
>
> In particular, if $f$ is entire then the displayed integral is zero for any closed path $\gamma$.
````

## 4. Callout 103: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!definition] Simply Connected and Multiply Connected Plane Regions
> A region $\Omega$ is called **simply connected** if, for every pair $\alpha,\beta\in\Omega$, all paths joining $\alpha$ to $\beta$ in $\Omega$ are mutually continuously deformable relative to $\Omega$. If a region is not simply connected, then it is called **multiply connected**.
````
### After

````text
> [!definition] Simply Connected Region, Multiply Connected Region
> A region $\Omega$ is called **simply connected** if, for every pair $\alpha,\beta\in\Omega$, all paths joining $\alpha$ to $\beta$ in $\Omega$ are mutually continuously deformable relative to $\Omega$. If a region is not simply connected, then it is called **multiply connected**.
````

## 5. Callout 104: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Cauchy’s Integral Theorem in a Simply Connected Region
> Suppose that $\Omega$ is a simply connected region and that $f$ is analytic in $\Omega$. (i) If $\gamma_{0}$ and $\gamma_{1}$ are two paths joining $\alpha$ to $\beta$ in $\Omega$, then
>
> $$
> \int_{\gamma_{0}} f(z) d z=\int_{\gamma_{1}} f(z) d z
> $$
>
> (ii) If $\gamma$ is a closed path in $\Omega$, then
>
> $$
> \int_{\gamma} f(z) d z=0
> $$
````
### After

````text
> [!theorem] Cauchy's Theorem for Simply Connected Regions
> Suppose that $\Omega$ is a simply connected region and that $f$ is analytic in $\Omega$. (i) If $\gamma_{0}$ and $\gamma_{1}$ are two paths joining $\alpha$ to $\beta$ in $\Omega$, then
>
> $$
> \int_{\gamma_{0}} f(z) d z=\int_{\gamma_{1}} f(z) d z
> $$
>
> (ii) If $\gamma$ is a closed path in $\Omega$, then
>
> $$
> \int_{\gamma} f(z) d z=0
> $$
````

## 6. Callout 105: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Analytic Antiderivatives in a Simply Connected Region
> Suppose that $\Omega$ is a simply connected region and that $f$ is analytic in $\Omega$. Then there is an analytic function $F$ in $\Omega$ such that $F^{\prime}=f$. In other words, every analytic function in $\Omega$ has an antiderivative in $\Omega$. Up to an arbitrary additive constant, we have
>
> $$
> F(z)=\int_{z_{0}}^{z} f(\zeta) d \zeta
> $$
>
> where $z_{0}$ is a fixed point in $\Omega$ and the integral is taken over any path in $\Omega$ joining $z_{0}$ to $z$.
````
### After

````text
> [!theorem] Existence of Antiderivatives
> Suppose that $\Omega$ is a simply connected region and that $f$ is analytic in $\Omega$. Then there is an analytic function $F$ in $\Omega$ such that $F^{\prime}=f$. In other words, every analytic function in $\Omega$ has an antiderivative in $\Omega$. Up to an arbitrary additive constant, we have
>
> $$
> F(z)=\int_{z_{0}}^{z} f(\zeta) d \zeta
> $$
>
> where $z_{0}$ is a fixed point in $\Omega$ and the integral is taken over any path in $\Omega$ joining $z_{0}$ to $z$.
````

## 7. Callout 106: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!definition] Simple Closed Path in the Complex Plane
> A closed path $\gamma$ is called simple or a simple curve if $\gamma$ intersects itself only at the endpoints. That is, if $\gamma(t), a \leq t \leq b$, is a parametrization of $\gamma$, and $a \leq t_{1}<t_{2} \leq b$, then $\gamma\left(t_{1}\right)=\gamma\left(t_{2}\right) \Leftrightarrow t_{1}=a$ and $t_{2}=b$.
````
### After

````text
> [!definition] Simple Path
> A closed path $\gamma$ is called simple or a simple curve if $\gamma$ intersects itself only at the endpoints. That is, if $\gamma(t), a \leq t \leq b$, is a parametrization of $\gamma$, and $a \leq t_{1}<t_{2} \leq b$, then $\gamma\left(t_{1}\right)=\gamma\left(t_{2}\right) \Leftrightarrow t_{1}=a$ and $t_{2}=b$.
````

## 8. Callout 107: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Cauchy’s Integral Theorem inside a Simple Closed Path
> Suppose that $f$ is analytic on a simple closed path $C$ and its interior.
> (i) We have
>
> $$
> \int_{C} f(z) d z=0
> $$
>
> (ii) If $\gamma$ is a closed path (not necessarily simple) contained in the interior of $C$, then
>
> $$
> \int_{\gamma} f(z) d z=0
> $$
````
### After

````text
> [!theorem] Cauchy's Theorem for Simple Paths
> Suppose that $f$ is analytic on a simple closed path $C$ and its interior.
> (i) We have
>
> $$
> \int_{C} f(z) d z=0
> $$
>
> (ii) If $\gamma$ is a closed path (not necessarily simple) contained in the interior of $C$, then
>
> $$
> \int_{\gamma} f(z) d z=0
> $$
````

## 9. Callout 108: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Cauchy’s Integral Theorem for a Region with Multiple Boundary Curves
> Let $C,C_1,\ldots,C_n$ be positively oriented simple closed paths. Suppose the $C_j$ lie inside $C$, their interiors are pairwise disjoint, and their boundaries are disjoint from one another and from $C$. If $f$ is analytic on an open set containing the boundaries and the closed region inside $C$ and outside all the $C_j$, then
>
> $$
> \int_C f(z)\,dz=\sum_{j=1}^n\int_{C_j}f(z)\,dz.
> $$
````
### After

````text
> [!theorem] Cauchy's Theorem for Multiply Connected Regions
> Suppose that $f$ is analytic on a region $\Omega$ with simple paths $C$ and $C_{j}(j= 1,2, \ldots, n)$ positively oriented and contained in $\Omega$, where the $C_j$ are inside $C$ with pairwise disjoint interiors and boundaries, and the closed region inside $C$ and outside the $C_j$ is contained in $\Omega$. Then
>
> $$
> \int_{C} f(z) d z=\sum_{j=1}^{n} \int_{C_{j}} f(z) d z
> $$
````
