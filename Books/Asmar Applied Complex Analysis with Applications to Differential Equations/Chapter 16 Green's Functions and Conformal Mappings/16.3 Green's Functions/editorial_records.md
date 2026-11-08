
# Editorial records

Reading note: 16.3 Green's Functions.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|a384e142-071f-55c9-9e2c-1bdedc32d8e9.local at=857e12bf-aded-561d-91f8-323224d3d026] Boundary Representation of a Harmonic Function by the Logarithmic Potential
> Let $\Omega\subset\mathbb R^2$ be a bounded region with piecewise smooth boundary $\Gamma$, consisting of finitely many disjoint simple closed curves, and let $n$ be the outward unit normal. Boundary integrals use arc length $ds$, with normal derivatives taken in the boundary variable $q=(x,y)$.
>
> If $u$ is harmonic in $\Omega$ and $C^2$ near $\overline\Omega$, then, for every $p=(x_0,y_0)\in\Omega$, with $v(q)=\log|q-p|$,
>
> $$
> u(p)=\frac1{2\pi}\int_\Gamma\left(u\frac{\partial v}{\partial n}-v\frac{\partial u}{\partial n}\right)ds.
> $$
````
### After

````text
> [!theorem|a384e142-071f-55c9-9e2c-1bdedc32d8e9.local at=857e12bf-aded-561d-91f8-323224d3d026] Boundary Representation of a Harmonic Function by the Logarithmic Potential
> Let $\Omega$ be a bounded connected plane region with piecewise smooth boundary $\Gamma$; $n$ denotes its outward unit normal. Functions in boundary identities are $C^2$ near $\overline\Omega$.
>
> Suppose that $u$ is harmonic inside $\Omega$ and $C^2$ near its closure with boundary $\Gamma$. Let $\left(x_0,y_0\right)$ be a point inside $\Omega$. Then
>
> $$
> u\left(x_0,y_0\right)=\frac{1}{2 \pi} \int_{\Gamma}\left(u \frac{\partial v}{\partial n}-v \frac{\partial u}{\partial n}\right) d s
> $$
>
> where $v(x, y)=\frac{1}{2} \ln \left(\left(x-x_{0}\right)^{2}+\left(y-y_{0}\right)^{2}\right)$.
````

## 2. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|59691839-c6be-57a1-9e75-19d859e2170f.local at=ecd1d0b6-7014-52f1-b4aa-f1aa6d594d63] Dirichlet Boundary Representation Using a Planar Green Function
> Let $\Omega\subset\mathbb R^2$ be a bounded region with piecewise smooth boundary $\Gamma$, consisting of finitely many disjoint simple closed curves, and let $n$ be the outward unit normal. Boundary integrals use arc length $ds$, with normal derivatives taken in the boundary variable $q=(x,y)$.
>
> For a pole $p=(x_0,y_0)\in\Omega$, use the normalization $G(q,p)=\log|q-p|+h(q,p)$, where $h(\cdot,p)$ is harmonic in $\Omega$ and continuous on $\overline\Omega$, with $h(q,p)=-\log|q-p|$ on $\Gamma$. Thus $G=0$ on the boundary. This is the Green function for $\Delta=\partial_x^2+\partial_y^2$ with logarithmic coefficient $+1$.
>
> If $u$ is harmonic in $\Omega$ and $C^2$ near $\overline\Omega$, then
>
> $$
> u(p)=\frac1{2\pi}\int_\Gamma u(q)\,\partial_{n_q}G(q,p)\,ds_q,\qquad p\in\Omega.
> $$
>
> The same representation extends to continuous boundary data and their continuous harmonic extension on a regular domain, with the boundary integral interpreted via the Poisson kernel.
````
### After

````text
> [!theorem|59691839-c6be-57a1-9e75-19d859e2170f.local at=ecd1d0b6-7014-52f1-b4aa-f1aa6d594d63] Dirichlet Boundary Representation Using a Planar Green Function
> Let $\Omega$ be a bounded connected plane region with piecewise smooth boundary $\Gamma$; $n$ denotes its outward unit normal. Functions in boundary identities are $C^2$ near $\overline\Omega$.
>
> Suppose that $u$ is harmonic on $\Omega$ and continuous on its boundary $\Gamma$. Then for $\left(x_{0}, y_{0}\right)$ in $\Omega$, we have
>
> $$
> u\left(x_{0}, y_{0}\right)=\frac{1}{2 \pi} \int_{\Gamma} u(x, y) \frac{\partial G}{\partial n}\left(x, y, x_{0}, y_{0}\right) d s
> $$
>
> where $G$ is Green's function for $\Omega$.
>
> Here $G(q,p)=\log|q-p|+h(q,p)$, where $h(\cdot,p)$ is harmonic throughout $\Omega$ and $G=0$ on $\Gamma$.
````

## 3. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|4fe9c616-91e8-5363-b3cb-caddd3fc1715.local at=3eedc89b-aebd-598c-a0d4-921df1967707] Harmonicity, Boundary Values, Sign, Uniqueness, and Symmetry of a Planar Dirichlet Green Function
> Let $\Omega\subset\mathbb R^2$ be a bounded region with piecewise smooth boundary $\Gamma$, consisting of finitely many disjoint simple closed curves, and let $n$ be the outward unit normal. Boundary integrals use arc length $ds$, with normal derivatives taken in the boundary variable $q=(x,y)$.
>
> For a pole $p=(x_0,y_0)\in\Omega$, use the normalization $G(q,p)=\log|q-p|+h(q,p)$, where $h(\cdot,p)$ is harmonic in $\Omega$ and continuous on $\overline\Omega$, with $h(q,p)=-\log|q-p|$ on $\Gamma$. Thus $G=0$ on the boundary. This is the Green function for $\Delta=\partial_x^2+\partial_y^2$ with logarithmic coefficient $+1$.
>
> For distinct $p,q\in\Omega$, $G(\cdot,p)$ is harmonic away from $p$, $G(q,p)\le0$, and $G(q,p)=G(p,q)$. It vanishes on $\Gamma$ and is uniquely determined by the region and this logarithmic normalization. At the pole it has a logarithmic singularity tending to $-\infty$.
````
### After

````text
> [!theorem|4fe9c616-91e8-5363-b3cb-caddd3fc1715.local at=3eedc89b-aebd-598c-a0d4-921df1967707] Harmonicity, Boundary Values, Sign, Uniqueness, and Symmetry of a Planar Dirichlet Green Function
> Let $\Omega$ be a bounded connected plane region with piecewise smooth boundary $\Gamma$; $n$ denotes its outward unit normal. Functions in boundary identities are $C^2$ near $\overline\Omega$.
>
> Let $\Omega$ be a region with boundary $\Gamma$, and let $G$ be its Green's function defined below. Then
> (i) $G\left(x, y, x_{0}, y_{0}\right)$ is a harmonic function of $(x, y)$ in $\Omega$ minus $\left(x_{0}, y_{0}\right)$. Harmonicity fails at ( $x_{0}, y_{0}$ ) due to the logarithmic part $v$.
> (ii) $G\left(x, y, x_{0}, y_{0}\right)=0$ for all $(x, y)$ on the boundary $\Gamma$.
> (iii) $G\left(x, y, x_{0}, y_{0}\right) \leq 0$ for all $(x, y)$ in $\Omega$ minus $\left(x_{0}, y_{0}\right)$.
> (iv) (uniqueness property) Green's function is uniquely determined by the region $\Omega$.
> (v) (symmetry property) $G\left(x, y, x_{0}, y_{0}\right)=G\left(x_{0}, y_{0}, x, y\right)$ for all distinct $\left(x_{0}, y_{0}\right)$ and $(x,y)$ in $\Omega$.
>
> Here $G(q,p)=\log|q-p|+h(q,p)$, where $h(\cdot,p)$ is harmonic throughout $\Omega$ and $G=0$ on $\Gamma$.
````

## 4. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|61e8e2f9-667f-5d9f-a11e-80d555aea9bc.local at=5aeb79af-79f8-5ad5-a857-80bbc215cc05] Green Function Representation of the Poisson Problem with Zero Dirichlet Data
> Let $\Omega\subset\mathbb R^2$ be a bounded region with piecewise smooth boundary $\Gamma$, consisting of finitely many disjoint simple closed curves, and let $n$ be the outward unit normal. Boundary integrals use arc length $ds$, with normal derivatives taken in the boundary variable $q=(x,y)$.
>
> For a pole $p=(x_0,y_0)\in\Omega$, use the normalization $G(q,p)=\log|q-p|+h(q,p)$, where $h(\cdot,p)$ is harmonic in $\Omega$ and continuous on $\overline\Omega$, with $h(q,p)=-\log|q-p|$ on $\Gamma$. Thus $G=0$ on the boundary. This is the Green function for $\Delta=\partial_x^2+\partial_y^2$ with logarithmic coefficient $+1$.
>
> If $u\in C^2$ near $\overline\Omega$ satisfies $\Delta u=f$ in $\Omega$ and $u=0$ on $\Gamma$, then
>
> $$
> u(p)=\frac1{2\pi}\iint_\Omega f(q)G(q,p)\,dA_q,\qquad p\in\Omega.
> $$
>
> The logarithmic singularity is locally integrable, so this integral is well-defined for continuous $f$ on $\overline\Omega$.
````
### After

````text
> [!theorem|61e8e2f9-667f-5d9f-a11e-80d555aea9bc.local at=5aeb79af-79f8-5ad5-a857-80bbc215cc05] Green Function Representation of the Poisson Problem with Zero Dirichlet Data
> Let $\Omega$ be a bounded connected plane region with piecewise smooth boundary $\Gamma$; $n$ denotes its outward unit normal. Functions in boundary identities are $C^2$ near $\overline\Omega$.
>
> Let $\Omega$ be a region with boundary $\Gamma$. Let $f(x, y)$ be a function on $\Omega$ and suppose that $u$ is a solution of Poisson's equation on $\Omega$.
>
> $$
> \nabla^{2} u(x, y)=f(x, y) . \quad(x, y) \text { in } \Omega .
> $$
>
> such that $u=0$ on the boundary $\Gamma$. Then, for all $\left(x_{0}, y_{0}\right)$ in $\Omega$.
>
> $$
> u\left(x_{0}, y_{0}\right)=\frac{1}{2 \pi} \iint_{\Omega} f(x, y) G\left(x, y, x_{0}, y_{0}\right) d x d y
> $$
>
> where $G$ is Green's function for $\Omega$.
>
> Here $G(q,p)=\log|q-p|+h(q,p)$, where $h(\cdot,p)$ is harmonic throughout $\Omega$ and $G=0$ on $\Gamma$.
````

## 5. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|9bba4491-86a2-5ff0-9403-a865611048b7.local at=21b690aa-a8e2-5f23-8f26-4bd4da71a284] Green Function Representation of the Poisson Problem with General Dirichlet Data
> Let $\Omega\subset\mathbb R^2$ be a bounded region with piecewise smooth boundary $\Gamma$, consisting of finitely many disjoint simple closed curves, and let $n$ be the outward unit normal. Boundary integrals use arc length $ds$, with normal derivatives taken in the boundary variable $q=(x,y)$.
>
> For a pole $p=(x_0,y_0)\in\Omega$, use the normalization $G(q,p)=\log|q-p|+h(q,p)$, where $h(\cdot,p)$ is harmonic in $\Omega$ and continuous on $\overline\Omega$, with $h(q,p)=-\log|q-p|$ on $\Gamma$. Thus $G=0$ on the boundary. This is the Green function for $\Delta=\partial_x^2+\partial_y^2$ with logarithmic coefficient $+1$.
>
> If $u\in C^2$ near $\overline\Omega$ satisfies $\Delta u=f$ in $\Omega$ and $u=g$ on $\Gamma$, then
>
> $$
> u(p)=\frac1{2\pi}\iint_\Omega f(q)G(q,p)\,dA_q+\frac1{2\pi}\int_\Gamma g(q)\,\partial_{n_q}G(q,p)\,ds_q.
> $$
````
### After

````text
> [!theorem|9bba4491-86a2-5ff0-9403-a865611048b7.local at=21b690aa-a8e2-5f23-8f26-4bd4da71a284] Green Function Representation of the Poisson Problem with General Dirichlet Data
> Let $\Omega$ be a bounded connected plane region with piecewise smooth boundary $\Gamma$; $n$ denotes its outward unit normal. Functions in boundary identities are $C^2$ near $\overline\Omega$.
>
> Suppose that $u$ is a solution of Poisson's equation $\nabla^2u=f$ with boundary condition $u(x, y)=g(x, y)$ for all $(x, y)$ on $\Gamma$. Then, for all ( $x_{0}, y_{0}$ ) in $\Omega$.
>
> $$
> \begin{aligned}
> u\left(x_{0}, y_{0}\right)= & \frac{1}{2 \pi} \iint_{\Omega} f(x, y) G\left(x, y, x_{0}, y_{0}\right) d x d y \\
> & +\frac{1}{2 \pi} \int_{\Gamma} g(x, y) \frac{\partial G}{\partial n}\left(x, y, x_{0}, y_{0}\right) d s
> \end{aligned}
> $$
>
> where $G$ is Green's function for $\Omega$.
>
> Here $G(q,p)=\log|q-p|+h(q,p)$, where $h(\cdot,p)$ is harmonic throughout $\Omega$ and $G=0$ on $\Gamma$.
````

## 6. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|a833de56-a04f-5be0-970e-55ea484b3bba.local at=bed2b6f0-4287-5286-9d61-9500aa2d5986] Distributional Poisson Equation for a Planar Dirichlet Green Function
> Let $\Omega\subset\mathbb R^2$ be a bounded region with piecewise smooth boundary $\Gamma$, consisting of finitely many disjoint simple closed curves, and let $n$ be the outward unit normal. Boundary integrals use arc length $ds$, with normal derivatives taken in the boundary variable $q=(x,y)$.
>
> For a pole $p=(x_0,y_0)\in\Omega$, use the normalization $G(q,p)=\log|q-p|+h(q,p)$, where $h(\cdot,p)$ is harmonic in $\Omega$ and continuous on $\overline\Omega$, with $h(q,p)=-\log|q-p|$ on $\Gamma$. Thus $G=0$ on the boundary. This is the Green function for $\Delta=\partial_x^2+\partial_y^2$ with logarithmic coefficient $+1$.
>
> For a fixed $p\in\Omega$, the locally integrable function $U(q)=G(q,p)/(2\pi)$ satisfies $\Delta_qU=\delta_p$ in distributions and $U=0$ on $\Gamma$. Equivalently, for every $\phi\in C_c^\infty(\Omega)$,
>
> $$
> \frac1{2\pi}\iint_\Omega G(q,p)\Delta\phi(q)\,dA_q=\phi(p).
> $$
>
> Here $\delta_p$ is the unit point mass, defined by $\langle\delta_p,\phi\rangle=\phi(p)$.
````
### After

````text
> [!theorem|a833de56-a04f-5be0-970e-55ea484b3bba.local at=bed2b6f0-4287-5286-9d61-9500aa2d5986] Distributional Poisson Equation for a Planar Dirichlet Green Function
> Let $\Omega$ be a bounded connected plane region with piecewise smooth boundary $\Gamma$; $n$ denotes its outward unit normal. Functions in boundary identities are $C^2$ near $\overline\Omega$.
>
> For fixed $\left(x_{0}, y_{0}\right)$ in $\Omega, \frac{1}{2 \pi} G\left(x, y, x_{0}, y_{0}\right)$ is a distributional solution of the following Poisson equation, with zero boundary condition:
>
> $$
> \begin{aligned}
> \nabla^{2} u & =\delta_{\left(x_{0}, y_{0}\right)}(x, y), \quad(x, y) \text { in } \Omega \\
> u(x, y) & =0 \text { for all }(x, y) \text { on the boundary of } \Omega .
> \end{aligned}
> $$
>
> where $\delta_{\left(x_{0}, y_{0}\right)}(x, y)$ is the two dimensional delta Dirac function.
>
> Here $G(q,p)=\log|q-p|+h(q,p)$, where $h(\cdot,p)$ is harmonic throughout $\Omega$ and $G=0$ on $\Gamma$.
````

## 7. Repair the invalid interchange of Laplacians using the author’s Green representation argument; remove the substituted punctured-domain proof.

### Before

````text
Proof. Write $G(q,p)=\log|q-p|+h(q,p)$ and remove the closed disk of radius $r$ centered at $p$, leaving $\Omega_r$. Apply Green’s second identity to $G$ and $\phi\in C_c^\infty(\Omega)$ on $\Omega_r$. The outer-boundary terms vanish because $\phi$ is zero near $\Gamma$, and $\Delta G=0$ away from $p$. With $C_r$ carrying the normal directed into the removed disk,

$$
\iint_{\Omega_r}G\Delta\phi\,dA
=\int_{C_r}\left(G\partial_n\phi-\phi\partial_nG\right)ds
\longrightarrow 0+2\pi\phi(p).
$$

The first term is $O(r|\log r|)$, while $\partial_nG=-1/r+O(1)$ on $C_r$. Local integrability of $\log|q-p|$ permits the limit on the left. Dividing by $2\pi$ proves the distributional equation; the zero boundary value is part of the definition of $G$.

[Source-proof clarification: symmetry alone does not justify interchanging the two Laplacians pointwise or differentiating through a singular integral. The punctured-domain argument above supplies the needed distributional justification.]
````
### After

````text
Proof of Theorem 6. That $G$ satisfies the zero boundary condition follows from Theorem 3(ii). We now show that the distributional equation holds when $u(x,y)=\frac1{2\pi}G(x,y,x_0,y_0)$. Letting $\phi\in C_c^\infty(\Omega)$ be any test function, we must show that
$$
\frac1{2\pi}\iint_\Omega G(x,y,x_0,y_0)\nabla^2\phi(x,y)\,dx\,dy=\phi(x_0,y_0).
$$
By Theorem 4, this is the representation formula for the function $\phi$, which solves Poisson's equation with source $\nabla^2\phi$ and zero boundary data. Thus the distributional equation follows.
````

## 8. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|a384e142-071f-55c9-9e2c-1bdedc32d8e9.local at=857e12bf-aded-561d-91f8-323224d3d026] Boundary Representation of a Harmonic Function by the Logarithmic Potential
> Let $\Omega$ be a bounded connected plane region with piecewise smooth boundary $\Gamma$; $n$ denotes its outward unit normal. Functions in boundary identities are $C^2$ near $\overline\Omega$.
>
> Suppose that $u$ is harmonic inside $\Omega$ and $C^2$ near its closure with boundary $\Gamma$. Let $\left(x_0,y_0\right)$ be a point inside $\Omega$. Then
>
> $$
> u\left(x_0,y_0\right)=\frac{1}{2 \pi} \int_{\Gamma}\left(u \frac{\partial v}{\partial n}-v \frac{\partial u}{\partial n}\right) d s
> $$
>
> where $v(x, y)=\frac{1}{2} \ln \left(\left(x-x_{0}\right)^{2}+\left(y-y_{0}\right)^{2}\right)$.
````
### After

````text
> [!theorem|a384e142-071f-55c9-9e2c-1bdedc32d8e9.local at=857e12bf-aded-561d-91f8-323224d3d026] Representation Formula
> Let $\Omega$ be a bounded connected plane region with piecewise smooth boundary $\Gamma$; $n$ denotes its outward unit normal. Functions in boundary identities are $C^2$ near $\overline\Omega$.
>
> Suppose that $u$ is harmonic inside $\Omega$ and $C^2$ near its closure with boundary $\Gamma$. Let $\left(x_0,y_0\right)$ be a point inside $\Omega$. Then
>
> $$
> u\left(x_0,y_0\right)=\frac{1}{2 \pi} \int_{\Gamma}\left(u \frac{\partial v}{\partial n}-v \frac{\partial u}{\partial n}\right) d s
> $$
>
> where $v(x, y)=\frac{1}{2} \ln \left(\left(x-x_{0}\right)^{2}+\left(y-y_{0}\right)^{2}\right)$.
````

## 9. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|59691839-c6be-57a1-9e75-19d859e2170f.local at=ecd1d0b6-7014-52f1-b4aa-f1aa6d594d63] Dirichlet Boundary Representation Using a Planar Green Function
> Let $\Omega$ be a bounded connected plane region with piecewise smooth boundary $\Gamma$; $n$ denotes its outward unit normal. Functions in boundary identities are $C^2$ near $\overline\Omega$.
>
> Suppose that $u$ is harmonic on $\Omega$ and continuous on its boundary $\Gamma$. Then for $\left(x_{0}, y_{0}\right)$ in $\Omega$, we have
>
> $$
> u\left(x_{0}, y_{0}\right)=\frac{1}{2 \pi} \int_{\Gamma} u(x, y) \frac{\partial G}{\partial n}\left(x, y, x_{0}, y_{0}\right) d s
> $$
>
> where $G$ is Green's function for $\Omega$.
>
> Here $G(q,p)=\log|q-p|+h(q,p)$, where $h(\cdot,p)$ is harmonic throughout $\Omega$ and $G=0$ on $\Gamma$.
````
### After

````text
> [!theorem|59691839-c6be-57a1-9e75-19d859e2170f.local at=ecd1d0b6-7014-52f1-b4aa-f1aa6d594d63] Solution of Dirichlet Problem
> Let $\Omega$ be a bounded connected plane region with piecewise smooth boundary $\Gamma$; $n$ denotes its outward unit normal. Functions in boundary identities are $C^2$ near $\overline\Omega$.
>
> Suppose that $u$ is harmonic on $\Omega$ and continuous on its boundary $\Gamma$. Then for $\left(x_{0}, y_{0}\right)$ in $\Omega$, we have
>
> $$
> u\left(x_{0}, y_{0}\right)=\frac{1}{2 \pi} \int_{\Gamma} u(x, y) \frac{\partial G}{\partial n}\left(x, y, x_{0}, y_{0}\right) d s
> $$
>
> where $G$ is Green's function for $\Omega$.
>
> Here $G(q,p)=\log|q-p|+h(q,p)$, where $h(\cdot,p)$ is harmonic throughout $\Omega$ and $G=0$ on $\Gamma$.
````

## 10. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|4fe9c616-91e8-5363-b3cb-caddd3fc1715.local at=3eedc89b-aebd-598c-a0d4-921df1967707] Harmonicity, Boundary Values, Sign, Uniqueness, and Symmetry of a Planar Dirichlet Green Function
> Let $\Omega$ be a bounded connected plane region with piecewise smooth boundary $\Gamma$; $n$ denotes its outward unit normal. Functions in boundary identities are $C^2$ near $\overline\Omega$.
>
> Let $\Omega$ be a region with boundary $\Gamma$, and let $G$ be its Green's function defined below. Then
> (i) $G\left(x, y, x_{0}, y_{0}\right)$ is a harmonic function of $(x, y)$ in $\Omega$ minus $\left(x_{0}, y_{0}\right)$. Harmonicity fails at ( $x_{0}, y_{0}$ ) due to the logarithmic part $v$.
> (ii) $G\left(x, y, x_{0}, y_{0}\right)=0$ for all $(x, y)$ on the boundary $\Gamma$.
> (iii) $G\left(x, y, x_{0}, y_{0}\right) \leq 0$ for all $(x, y)$ in $\Omega$ minus $\left(x_{0}, y_{0}\right)$.
> (iv) (uniqueness property) Green's function is uniquely determined by the region $\Omega$.
> (v) (symmetry property) $G\left(x, y, x_{0}, y_{0}\right)=G\left(x_{0}, y_{0}, x, y\right)$ for all distinct $\left(x_{0}, y_{0}\right)$ and $(x,y)$ in $\Omega$.
>
> Here $G(q,p)=\log|q-p|+h(q,p)$, where $h(\cdot,p)$ is harmonic throughout $\Omega$ and $G=0$ on $\Gamma$.
````
### After

````text
> [!theorem|4fe9c616-91e8-5363-b3cb-caddd3fc1715.local at=3eedc89b-aebd-598c-a0d4-921df1967707] Properties of Green's Function
> Let $\Omega$ be a bounded connected plane region with piecewise smooth boundary $\Gamma$; $n$ denotes its outward unit normal. Functions in boundary identities are $C^2$ near $\overline\Omega$.
>
> Let $\Omega$ be a region with boundary $\Gamma$, and let $G$ be its Green's function defined below. Then
> (i) $G\left(x, y, x_{0}, y_{0}\right)$ is a harmonic function of $(x, y)$ in $\Omega$ minus $\left(x_{0}, y_{0}\right)$. Harmonicity fails at ( $x_{0}, y_{0}$ ) due to the logarithmic part $v$.
> (ii) $G\left(x, y, x_{0}, y_{0}\right)=0$ for all $(x, y)$ on the boundary $\Gamma$.
> (iii) $G\left(x, y, x_{0}, y_{0}\right) \leq 0$ for all $(x, y)$ in $\Omega$ minus $\left(x_{0}, y_{0}\right)$.
> (iv) (uniqueness property) Green's function is uniquely determined by the region $\Omega$.
> (v) (symmetry property) $G\left(x, y, x_{0}, y_{0}\right)=G\left(x_{0}, y_{0}, x, y\right)$ for all distinct $\left(x_{0}, y_{0}\right)$ and $(x,y)$ in $\Omega$.
>
> Here $G(q,p)=\log|q-p|+h(q,p)$, where $h(\cdot,p)$ is harmonic throughout $\Omega$ and $G=0$ on $\Gamma$.
````

## 11. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|61e8e2f9-667f-5d9f-a11e-80d555aea9bc.local at=5aeb79af-79f8-5ad5-a857-80bbc215cc05] Green Function Representation of the Poisson Problem with Zero Dirichlet Data
> Let $\Omega$ be a bounded connected plane region with piecewise smooth boundary $\Gamma$; $n$ denotes its outward unit normal. Functions in boundary identities are $C^2$ near $\overline\Omega$.
>
> Let $\Omega$ be a region with boundary $\Gamma$. Let $f(x, y)$ be a function on $\Omega$ and suppose that $u$ is a solution of Poisson's equation on $\Omega$.
>
> $$
> \nabla^{2} u(x, y)=f(x, y) . \quad(x, y) \text { in } \Omega .
> $$
>
> such that $u=0$ on the boundary $\Gamma$. Then, for all $\left(x_{0}, y_{0}\right)$ in $\Omega$.
>
> $$
> u\left(x_{0}, y_{0}\right)=\frac{1}{2 \pi} \iint_{\Omega} f(x, y) G\left(x, y, x_{0}, y_{0}\right) d x d y
> $$
>
> where $G$ is Green's function for $\Omega$.
>
> Here $G(q,p)=\log|q-p|+h(q,p)$, where $h(\cdot,p)$ is harmonic throughout $\Omega$ and $G=0$ on $\Gamma$.
````
### After

````text
> [!theorem|61e8e2f9-667f-5d9f-a11e-80d555aea9bc.local at=5aeb79af-79f8-5ad5-a857-80bbc215cc05] Solution of Poisson's Equation with Zero Boundary Data
> Let $\Omega$ be a bounded connected plane region with piecewise smooth boundary $\Gamma$; $n$ denotes its outward unit normal. Functions in boundary identities are $C^2$ near $\overline\Omega$.
>
> Let $\Omega$ be a region with boundary $\Gamma$. Let $f(x, y)$ be a function on $\Omega$ and suppose that $u$ is a solution of Poisson's equation on $\Omega$.
>
> $$
> \nabla^{2} u(x, y)=f(x, y) . \quad(x, y) \text { in } \Omega .
> $$
>
> such that $u=0$ on the boundary $\Gamma$. Then, for all $\left(x_{0}, y_{0}\right)$ in $\Omega$.
>
> $$
> u\left(x_{0}, y_{0}\right)=\frac{1}{2 \pi} \iint_{\Omega} f(x, y) G\left(x, y, x_{0}, y_{0}\right) d x d y
> $$
>
> where $G$ is Green's function for $\Omega$.
>
> Here $G(q,p)=\log|q-p|+h(q,p)$, where $h(\cdot,p)$ is harmonic throughout $\Omega$ and $G=0$ on $\Gamma$.
````

## 12. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|9bba4491-86a2-5ff0-9403-a865611048b7.local at=21b690aa-a8e2-5f23-8f26-4bd4da71a284] Green Function Representation of the Poisson Problem with General Dirichlet Data
> Let $\Omega$ be a bounded connected plane region with piecewise smooth boundary $\Gamma$; $n$ denotes its outward unit normal. Functions in boundary identities are $C^2$ near $\overline\Omega$.
>
> Suppose that $u$ is a solution of Poisson's equation $\nabla^2u=f$ with boundary condition $u(x, y)=g(x, y)$ for all $(x, y)$ on $\Gamma$. Then, for all ( $x_{0}, y_{0}$ ) in $\Omega$.
>
> $$
> \begin{aligned}
> u\left(x_{0}, y_{0}\right)= & \frac{1}{2 \pi} \iint_{\Omega} f(x, y) G\left(x, y, x_{0}, y_{0}\right) d x d y \\
> & +\frac{1}{2 \pi} \int_{\Gamma} g(x, y) \frac{\partial G}{\partial n}\left(x, y, x_{0}, y_{0}\right) d s
> \end{aligned}
> $$
>
> where $G$ is Green's function for $\Omega$.
>
> Here $G(q,p)=\log|q-p|+h(q,p)$, where $h(\cdot,p)$ is harmonic throughout $\Omega$ and $G=0$ on $\Gamma$.
````
### After

````text
> [!theorem|9bba4491-86a2-5ff0-9403-a865611048b7.local at=21b690aa-a8e2-5f23-8f26-4bd4da71a284] General Solution of Poisson's Equation
> Let $\Omega$ be a bounded connected plane region with piecewise smooth boundary $\Gamma$; $n$ denotes its outward unit normal. Functions in boundary identities are $C^2$ near $\overline\Omega$.
>
> Suppose that $u$ is a solution of Poisson's equation $\nabla^2u=f$ with boundary condition $u(x, y)=g(x, y)$ for all $(x, y)$ on $\Gamma$. Then, for all ( $x_{0}, y_{0}$ ) in $\Omega$.
>
> $$
> \begin{aligned}
> u\left(x_{0}, y_{0}\right)= & \frac{1}{2 \pi} \iint_{\Omega} f(x, y) G\left(x, y, x_{0}, y_{0}\right) d x d y \\
> & +\frac{1}{2 \pi} \int_{\Gamma} g(x, y) \frac{\partial G}{\partial n}\left(x, y, x_{0}, y_{0}\right) d s
> \end{aligned}
> $$
>
> where $G$ is Green's function for $\Omega$.
>
> Here $G(q,p)=\log|q-p|+h(q,p)$, where $h(\cdot,p)$ is harmonic throughout $\Omega$ and $G=0$ on $\Gamma$.
````

## 13. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|a833de56-a04f-5be0-970e-55ea484b3bba.local at=bed2b6f0-4287-5286-9d61-9500aa2d5986] Distributional Poisson Equation for a Planar Dirichlet Green Function
> Let $\Omega$ be a bounded connected plane region with piecewise smooth boundary $\Gamma$; $n$ denotes its outward unit normal. Functions in boundary identities are $C^2$ near $\overline\Omega$.
>
> For fixed $\left(x_{0}, y_{0}\right)$ in $\Omega, \frac{1}{2 \pi} G\left(x, y, x_{0}, y_{0}\right)$ is a distributional solution of the following Poisson equation, with zero boundary condition:
>
> $$
> \begin{aligned}
> \nabla^{2} u & =\delta_{\left(x_{0}, y_{0}\right)}(x, y), \quad(x, y) \text { in } \Omega \\
> u(x, y) & =0 \text { for all }(x, y) \text { on the boundary of } \Omega .
> \end{aligned}
> $$
>
> where $\delta_{\left(x_{0}, y_{0}\right)}(x, y)$ is the two dimensional delta Dirac function.
>
> Here $G(q,p)=\log|q-p|+h(q,p)$, where $h(\cdot,p)$ is harmonic throughout $\Omega$ and $G=0$ on $\Gamma$.
````
### After

````text
> [!theorem|a833de56-a04f-5be0-970e-55ea484b3bba.local at=bed2b6f0-4287-5286-9d61-9500aa2d5986] Poisson's Equation with a Dirac Function
> Let $\Omega$ be a bounded connected plane region with piecewise smooth boundary $\Gamma$; $n$ denotes its outward unit normal. Functions in boundary identities are $C^2$ near $\overline\Omega$.
>
> For fixed $\left(x_{0}, y_{0}\right)$ in $\Omega, \frac{1}{2 \pi} G\left(x, y, x_{0}, y_{0}\right)$ is a distributional solution of the following Poisson equation, with zero boundary condition:
>
> $$
> \begin{aligned}
> \nabla^{2} u & =\delta_{\left(x_{0}, y_{0}\right)}(x, y), \quad(x, y) \text { in } \Omega \\
> u(x, y) & =0 \text { for all }(x, y) \text { on the boundary of } \Omega .
> \end{aligned}
> $$
>
> where $\delta_{\left(x_{0}, y_{0}\right)}(x, y)$ is the two dimensional delta Dirac function.
>
> Here $G(q,p)=\log|q-p|+h(q,p)$, where $h(\cdot,p)$ is harmonic throughout $\Omega$ and $G=0$ on $\Gamma$.
````
