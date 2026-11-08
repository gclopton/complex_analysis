
# Editorial records

Reading note: 6.6 Poisson's Equation and Neumann Problems.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Callout 242: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Green Function Representation of a Poisson–Dirichlet Solution
> Let $\Omega$ be a bounded planar region with a piecewise smooth boundary $\Gamma$. Use the Dirichlet Green function convention $G(z,\zeta)=\ln|z-\zeta|+H(z,\zeta)$, where $H$ is harmonic in $\zeta$ throughout $\Omega$ and $G=0$ on $\Gamma$. Let $u$ solve $\Delta u=h$ in $\Omega$ with $u=f$ on $\Gamma$, with sufficient boundary regularity for Green's identity and the following integrals. The normal derivative is outward in the $\zeta$ variable. Then
>
> $$
> u(z)=\frac{1}{2 \pi} \iint_{\Omega} h(\zeta) G(z, \zeta) d A+\frac{1}{2 \pi} \int_{\Gamma} f(\zeta) \frac{\partial}{\partial n} G(z, \zeta) d s
> $$
>
> where $d A$ is the element of area and $d s$ is the element of arc length.
````
### After

````text
> [!theorem] Solution of the Poisson Problem
> Suppose that $\Omega$ is a bounded region with piecewise smooth boundary $\Gamma$, and let $G(z, \zeta)$ denote the Green's function for $\Omega$ with singularity $\ln|z-\zeta|$ and zero boundary values. If $u(z)$ is a solution of $\Delta u=h$ in $\Omega$, $u=f$ on $\Gamma$, then
>
> $$
> u(z)=\frac{1}{2 \pi} \iint_{\Omega} h(\zeta) G(z, \zeta) d A+\frac{1}{2 \pi} \int_{\Gamma} f(\zeta) \frac{\partial}{\partial n} G(z, \zeta) d s
> $$
>
> where $d A$ is the element of area and $d s$ is the element of arc length. The normal derivative is outward in $\zeta$; assume sufficient regularity for the displayed integrals.
````

## 2. Callout 243: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Green Function Representation of a Poisson–Dirichlet Solution
> Let $\Omega$ be a bounded planar region with a piecewise smooth boundary $\Gamma$. Use the Dirichlet Green function convention $G(z,\zeta)=\ln|z-\zeta|+H(z,\zeta)$, where $H$ is harmonic in $\zeta$ throughout $\Omega$ and $G=0$ on $\Gamma$. Let $u$ solve $\Delta u=h$ in $\Omega$ with $u=f$ on $\Gamma$, with sufficient boundary regularity for Green's identity and the following integrals. The normal derivative is outward in the $\zeta$ variable. Then
>
> $$
> u(z)=\frac{1}{2 \pi} \iint_{\Omega} h(\zeta) G(z, \zeta) d A+\frac{1}{2 \pi} \int_{\Gamma} f(\zeta) \frac{\partial}{\partial n} G(z, \zeta) d s
> $$
>
> where $d A$ is the element of area and $d s$ is the element of arc length.
````
### After

````text
> [!theorem] Solution of Poisson Problem
> Suppose that $\Omega$ is a bounded region with piecewise smooth boundary $\Gamma$, and let $G(z, \zeta)$ denote the Green's function for $\Omega$ with singularity $\ln|z-\zeta|$ and zero boundary values. If $u(z)$ is a solution of $\Delta u=h$ in $\Omega$, $u=f$ on $\Gamma$, then
>
> $$
> u(z)=\frac{1}{2 \pi} \iint_{\Omega} h(\zeta) G(z, \zeta) d A+\frac{1}{2 \pi} \int_{\Gamma} f(\zeta) \frac{\partial}{\partial n} G(z, \zeta) d s
> $$
>
> where $d A$ is the element of area and $d s$ is the element of arc length. The normal derivative is outward in $\zeta$; assume sufficient regularity for the displayed integrals.
````

## 3. Callout 244: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Green's First and Second Identities in the Plane
> Assume a piecewise smooth boundary. Here $\Delta=\partial_x^2+\partial_y^2$, $dA=dx\,dy$, $ds$ is arc length, and $\partial_n$ denotes the outward normal derivative.
>
> Suppose that $\Omega$ is a bounded region whose boundary $\Gamma$ consists of a finite number of simple closed positively oriented paths. Let $u(x, y)$ and $v(x, y)$ have continuous second partial derivatives on $\Omega$ and $\Gamma$. Then we have Green's first identity
>
> $$
> \iint_{\Omega}(u \Delta v+\nabla u \cdot \nabla v) d A=\int_{\Gamma} u \frac{\partial v}{\partial n} d s,
> $$
>
> and Green's second identity
>
> $$
> \iint_{\Omega}(u \Delta v-v \Delta u) d A=\int_{\Gamma}\left(u \frac{\partial v}{\partial n}-v \frac{\partial u}{\partial n}\right) d s
> $$
````
### After

````text
> [!theorem] Green's Identities
> Assume a piecewise smooth boundary. Here $\Delta=\partial_x^2+\partial_y^2$, $dA=dx\,dy$, $ds$ is arc length, and $\partial_n$ denotes the outward normal derivative.
>
> Suppose that $\Omega$ is a bounded region whose boundary $\Gamma$ consists of a finite number of simple closed positively oriented paths. Let $u(x, y)$ and $v(x, y)$ have continuous second partial derivatives on $\Omega$ and $\Gamma$. Then we have Green's first identity
>
> $$
> \iint_{\Omega}(u \Delta v+\nabla u \cdot \nabla v) d A=\int_{\Gamma} u \frac{\partial v}{\partial n} d s,
> $$
>
> and Green's second identity
>
> $$
> \iint_{\Omega}(u \Delta v-v \Delta u) d A=\int_{\Gamma}\left(u \frac{\partial v}{\partial n}-v \frac{\partial u}{\partial n}\right) d s
> $$
````

## 4. Callout 245: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!proposition] Zero Total Normal Flux of a Harmonic Function
> Assume $\Omega$ has piecewise smooth boundary and $u\in C^2(\overline\Omega)$ is real-valued. The derivative $\partial_nu$ is taken in the outward normal direction.
>
> Suppose that $u$ is harmonic in a bounded region $\Omega$ and its boundary $\Gamma$. Then
>
> $$
> \int_{\Gamma} \frac{\partial u}{\partial n} d s=0
> $$
````
### After

````text
> [!proposition] Normal Derivative of Harmonic Functions
> Assume $\Omega$ has piecewise smooth boundary and $u\in C^2(\overline\Omega)$ is real-valued. The derivative $\partial_nu$ is taken in the outward normal direction.
>
> Suppose that $u$ is harmonic in a bounded region $\Omega$ and its boundary $\Gamma$. Then
>
> $$
> \int_{\Gamma} \frac{\partial u}{\partial n} d s=0
> $$
````

## 5. Callout 246: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Constancy of a Harmonic Function with Zero Neumann Data
> Assume $\Omega$ has piecewise smooth boundary and $u\in C^2(\overline\Omega)$ is real-valued. The derivative $\partial_nu$ is taken in the outward normal direction.
>
> Suppose that $u$ is harmonic on a bounded region $\Omega$ such that $\frac{\partial u}{\partial n}=0$ on the boundary $\Gamma$ of $\Omega$. Then $u$ is identically constant in $\Omega$.
````
### After

````text
> [!theorem] Uniqueness of Neumann Solution
> Assume $\Omega$ has piecewise smooth boundary and $u\in C^2(\overline\Omega)$ is real-valued. The derivative $\partial_nu$ is taken in the outward normal direction.
>
> Suppose that $u$ is harmonic on a bounded region $\Omega$ such that $\frac{\partial u}{\partial n}=0$ on the boundary $\Gamma$ of $\Omega$. Then $u$ is identically constant in $\Omega$.
````

## 6. Callout 247: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!definition] Planar Neumann Function with a Logarithmic Singularity
> Assume the boundary is piecewise smooth; normal derivatives act in the $\zeta$ variable and point outward. The constant $C$ is independent of $z$ and $\zeta$.
>
> Suppose that $\Omega$ is a simply connected region with boundary $\Gamma$. A Neumann function $N(z, \zeta)(z, \zeta$ in $\Omega)$ for the region $\Omega$ is a function with the following properties:
> (i) for each $z$ in $\Omega, N(z, \zeta)$ is harmonic for all $\zeta \neq z$ in $\Omega$;
> (ii) $\frac{\partial N}{\partial n}(z, \zeta)=C$ for all $z$ in $\Omega$ and $\zeta$ on $\Gamma$;
> (iii) for each $z$ in $\Omega$, there is a function $\zeta \mapsto u_1(z, \zeta)$ such that $u_1(z, \zeta)$ is harmonic for all $\zeta$ in $\Omega$, and $N(z, \zeta)=\ln |z-\zeta|+u_1(z, \zeta)$ for all $\zeta\in\Omega\setminus\{z\}$.
````
### After

````text
> [!definition] Neumann Functions
> Assume the boundary is piecewise smooth; normal derivatives act in the $\zeta$ variable and point outward. The constant $C$ is independent of $z$ and $\zeta$.
>
> Suppose that $\Omega$ is a simply connected region with boundary $\Gamma$. A Neumann function $N(z, \zeta)(z, \zeta$ in $\Omega)$ for the region $\Omega$ is a function with the following properties:
> (i) for each $z$ in $\Omega, N(z, \zeta)$ is harmonic for all $\zeta \neq z$ in $\Omega$;
> (ii) $\frac{\partial N}{\partial n}(z, \zeta)=C$ for all $z$ in $\Omega$ and $\zeta$ on $\Gamma$;
> (iii) for each $z$ in $\Omega$, there is a function $\zeta \mapsto u_1(z, \zeta)$ such that $u_1(z, \zeta)$ is harmonic for all $\zeta$ in $\Omega$, and $N(z, \zeta)=\ln |z-\zeta|+u_1(z, \zeta)$ for all $\zeta\in\Omega\setminus\{z\}$.
````

## 7. Callout 248: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!proposition] Constant Boundary Normal Derivative of a Planar Neumann Function
> Let $\Omega$ be a bounded simply connected planar region with piecewise smooth boundary $\Gamma$ of length $L$. For a Neumann function $N(z,\zeta)=\ln|z-\zeta|+H(z,\zeta)$, with $H$ harmonic in $\zeta$ throughout $\Omega$, suppose its outward normal derivative in $\zeta$ is constant on the boundary. Then
>
> $$
> \partial_nN(z,\zeta)=C=\frac{2\pi}{L}\qquad(\zeta\in\Gamma).
> $$
>
> For the unbounded-region convention with infinite boundary length, the boundary constant is taken to be $C=0$.
````
### After

````text
> [!proposition] Constant Boundary Normal Derivative of a Planar Neumann Function
> The constant $C$ in $\partial_nN(z,\zeta)=C$ for $\zeta\in\Gamma$, which represents the boundary value of the normal derivative of the Neumann function, is given, for the convention $N(z,\zeta)=\ln|z-\zeta|+H(z,\zeta)$ with $H$ harmonic in $\zeta$ and outward normal derivative on the piecewise smooth boundary $\Gamma$, by
> $$
> C=\frac{2 \pi}{L},
> $$
>
> where $L=\int_{\Gamma} d s$ is the length of $\Gamma$. If $L$ is infinite, we take $C=0$.
````

## 8. Callout 249: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Neumann Function Representation of a Harmonic Neumann Solution
> Use a Neumann function with singularity $\ln|z-\zeta|$ and constant outward boundary normal derivative in $\zeta$. Assume a bounded region with piecewise smooth boundary and sufficient regularity for Green\'s identity and the integrals below.
>
> Suppose that $\Omega$ is a region bounded by a simple path $\Gamma$, and let $N(z, \zeta)$ denote a Neumann function, where $z$ and $\zeta$ are in $\Omega$. Then, up to an additive constant, the solution $u(z)$ of $\Delta u=0$ in $\Omega$, $\partial_nu=f$ on $\Gamma$, with the compatibility condition $\int_\Gamma f\,ds=0$ is given by
>
> $$
> u(z)=-\frac{1}{2 \pi} \int_{\Gamma} N(z, \zeta) f(\zeta) d s
> $$
````
### After

````text
> [!theorem] Solution of Neumann Problems
> Use a Neumann function with singularity $\ln|z-\zeta|$ and constant outward boundary normal derivative in $\zeta$. Assume a bounded region with piecewise smooth boundary and sufficient regularity for Green\'s identity and the integrals below.
>
> Suppose that $\Omega$ is a region bounded by a simple path $\Gamma$, and let $N(z, \zeta)$ denote a Neumann function, where $z$ and $\zeta$ are in $\Omega$. Then, up to an additive constant, the solution $u(z)$ of $\Delta u=0$ in $\Omega$, $\partial_nu=f$ on $\Gamma$, with the compatibility condition $\int_\Gamma f\,ds=0$ is given by
>
> $$
> u(z)=-\frac{1}{2 \pi} \int_{\Gamma} N(z, \zeta) f(\zeta) d s
> $$
````

## 9. Callout 250: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!proposition] Neumann Function from a Conformal Map to the Upper Half-Plane
> Assume the conformal mapping extends smoothly to the boundary portions where outward normal derivatives are evaluated, with nonzero derivative there. The Neumann-function convention uses a positive logarithmic singularity and zero boundary normal derivative for this unbounded setting.
>
> Suppose that $\Omega$ is an unbounded region with boundary $\Gamma$, and $\phi$ is a one-to-one analytic mapping of $\Omega$ onto the upper half-plane, taking $\Gamma$ onto the real axis. Then the Neumann function for $\Omega$ is given by
>
> $$
> N(z, \zeta)=\ln |\phi(z)-\phi(\zeta)|+\ln |\overline{\phi(z)}-\phi(\zeta)| \quad(z, \zeta \text { in } \Omega) .
> $$
````
### After

````text
> [!proposition] Neumann Function for Unbounded Regions
> Assume the conformal mapping extends smoothly to the boundary portions where outward normal derivatives are evaluated, with nonzero derivative there. The Neumann-function convention uses a positive logarithmic singularity and zero boundary normal derivative for this unbounded setting.
>
> Suppose that $\Omega$ is an unbounded region with boundary $\Gamma$, and $\phi$ is a one-to-one analytic mapping of $\Omega$ onto the upper half-plane, taking $\Gamma$ onto the real axis. Then the Neumann function for $\Omega$ is given by
>
> $$
> N(z, \zeta)=\ln |\phi(z)-\phi(\zeta)|+\ln |\overline{\phi(z)}-\phi(\zeta)| \quad(z, \zeta \text { in } \Omega) .
> $$
````

## 10. Callout 251: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Neumann Function Representation of a Poisson–Neumann Solution
> Use a Neumann function with singularity $\ln|z-\zeta|$ and constant outward boundary normal derivative in $\zeta$. Assume a bounded region with piecewise smooth boundary and sufficient regularity for Green\'s identity and the integrals below.
>
> Suppose that $\Omega$ is a region with boundary $\Gamma$, let $N(z, \zeta)$ denote a Neumann function for this region, where $z$ and $\zeta$ are in $\Omega$. If $u(z)$ is a solution to $\Delta u=h$ in $\Omega$ with $\partial_nu=f$ on $\Gamma$ and $\iint_\Omega h\,dA=\int_\Gamma f\,ds$, then up to an additive constant
>
> $$
> u(z)=\frac{1}{2 \pi} \iint_{\Omega} h(\zeta) N(z, \zeta) d A-\frac{1}{2 \pi} \int_{\Gamma} N(z, \zeta) f(\zeta) d s
> $$
````
### After

````text
> [!theorem] Solution of Poisson-Neumann Problem
> Use a Neumann function with singularity $\ln|z-\zeta|$ and constant outward boundary normal derivative in $\zeta$. Assume a bounded region with piecewise smooth boundary and sufficient regularity for Green\'s identity and the integrals below.
>
> Suppose that $\Omega$ is a region with boundary $\Gamma$, let $N(z, \zeta)$ denote a Neumann function for this region, where $z$ and $\zeta$ are in $\Omega$. If $u(z)$ is a solution to $\Delta u=h$ in $\Omega$ with $\partial_nu=f$ on $\Gamma$ and $\iint_\Omega h\,dA=\int_\Gamma f\,ds$, then up to an additive constant
>
> $$
> u(z)=\frac{1}{2 \pi} \iint_{\Omega} h(\zeta) N(z, \zeta) d A-\frac{1}{2 \pi} \int_{\Gamma} N(z, \zeta) f(\zeta) d s
> $$
````

## 11. Move editorial commentary out of the reading note.

### Before

````text
*Editorial note: [corrected] The logarithmic-singularity decomposition in (iii) holds in the punctured region, as the immediately following explanation requires, not merely on its boundary.*
````
### After

````text

````

## 12. Move editorial commentary out of the reading note.

### Before

````text
*Editorial note: [clarified] Restated the governing equation, boundary data, logarithmic Green-function convention, and the bounded-region setting used in the source proof.*
````
### After

````text

````

## 13. Move editorial commentary out of the reading note.

### Before

````text
*Editorial note: [clarified] Restated the governing equation, boundary data, logarithmic Green-function convention, and the bounded-region setting used in the source proof.*
````
### After

````text

````

## Additional source comparison

## 1. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem] Superposition for a Poisson–Dirichlet Boundary Value Problem
> Let $\Omega$ be a planar region with boundary $\Gamma$. Suppose $\Delta u_1=h$ in $\Omega$ and $u_1=0$ on $\Gamma$, while $\Delta u_2=0$ in $\Omega$ and $u_2=f$ on $\Gamma$. Then $u=u_1+u_2$ satisfies $\Delta u=h$ in $\Omega$ and $u=f$ on $\Gamma$.
````
### After

````text
> [!theorem] Superposition Principle
> Let $\Omega$ be a region with boundary $\Gamma$.
>
> Suppose that $u_1$ satisfies $\Delta u_1=h$ in $\Omega$ and $u_1(\zeta)=0$ for all $\zeta$ on $\Gamma$. Suppose that $u_2$ satisfies Laplace's equation in $\Omega$ and $u_2(\zeta)=f(\zeta)$ for all $\zeta$ on $\Gamma$. Then $u=u_1+u_2$ satisfies Poisson's equation $\Delta u=h$ with boundary conditions $u=f$ on $\Gamma$.
````
