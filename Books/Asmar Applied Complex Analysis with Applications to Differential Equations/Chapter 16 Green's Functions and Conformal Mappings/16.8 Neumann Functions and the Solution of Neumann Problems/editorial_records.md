
# Editorial records

Reading note: 16.8 Neumann Functions and the Solution of Neumann Problems.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!definition|e7c59d8b-44bd-5b15-99f3-dedc446a016f.local at=0ad9873a-c103-53c8-bcbb-90a90c293734] Planar Neumann Function with Positive Logarithmic Singularity
> Let $\Omega\subset\mathbb R^2$ be a simply connected plane region with piecewise smooth boundary $\Gamma$ and outward unit normal $n$. For each pole $p\in\Omega$, a Neumann function in this convention satisfies:
>
> (i) $N(\cdot,p)$ is harmonic on $\Omega\setminus\{p\}$.
> (ii) $\partial_{n_z}N(z,p)=C$ on smooth pieces of $\Gamma$, for a constant independent of the boundary point and pole.
> (iii) $N(z,p)=\log|z-p|+H(z,p)$, where $H(\cdot,p)$ is harmonic throughout $\Omega$.
>
> For bounded $\Omega$ of boundary length $L$, necessarily $C=2\pi/L$.
````
### After

````text
> [!definition|e7c59d8b-44bd-5b15-99f3-dedc446a016f.local at=0ad9873a-c103-53c8-bcbb-90a90c293734] Planar Neumann Function with Positive Logarithmic Singularity
> Let $\Omega\subset\mathbb R^2$ be a simply connected plane region with piecewise smooth boundary $\Gamma$ and outward unit normal $n$. For each pole $p\in\Omega$, a Neumann function in this convention satisfies:
>
> (i) $N(\cdot,p)$ is harmonic on $\Omega\setminus\{p\}$.
> (ii) $\partial_{n_z}N(z,p)=C$ on smooth pieces of $\Gamma$, for a constant independent of the boundary point and pole.
> (iii) $N(z,p)=\log|z-p|+H(z,p)$, where $H(\cdot,p)$ is harmonic throughout $\Omega$.
````

## 2. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!definition|e7c59d8b-44bd-5b15-99f3-dedc446a016f.local at=0ad9873a-c103-53c8-bcbb-90a90c293734] Planar Neumann Function with Positive Logarithmic Singularity
> Let $\Omega\subset\mathbb R^2$ be a simply connected plane region with piecewise smooth boundary $\Gamma$ and outward unit normal $n$. For each pole $p\in\Omega$, a Neumann function in this convention satisfies:
>
> (i) $N(\cdot,p)$ is harmonic on $\Omega\setminus\{p\}$.
> (ii) $\partial_{n_z}N(z,p)=C$ on smooth pieces of $\Gamma$, for a constant independent of the boundary point and pole.
> (iii) $N(z,p)=\log|z-p|+H(z,p)$, where $H(\cdot,p)$ is harmonic throughout $\Omega$.
````
### After

````text
> [!definition|e7c59d8b-44bd-5b15-99f3-dedc446a016f.local at=0ad9873a-c103-53c8-bcbb-90a90c293734] Neumann Functions
> Let $\Omega\subset\mathbb R^2$ be a simply connected plane region with piecewise smooth boundary $\Gamma$ and outward unit normal $n$. For each pole $p\in\Omega$, a Neumann function in this convention satisfies:
>
> (i) $N(\cdot,p)$ is harmonic on $\Omega\setminus\{p\}$.
> (ii) $\partial_{n_z}N(z,p)=C$ on smooth pieces of $\Gamma$, for a constant independent of the boundary point and pole.
> (iii) $N(z,p)=\log|z-p|+H(z,p)$, where $H(\cdot,p)$ is harmonic throughout $\Omega$.
````

## 3. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|d00d8502-4689-5ddc-a0cc-bd3046064426.local at=cfac0fd2-3132-553e-b16f-7565120e5820] Neumann Boundary Representation for Harmonic Functions on a Bounded Plane Region
> Let $\Omega\subset\mathbb R^2$ be bounded, simply connected, and have piecewise smooth boundary $\Gamma$ of length $L>0$, with outward unit normal $n$. Write $z=x+iy$ and $p=x_0+iy_0\in\Omega$.
>
> A Neumann function in the positive-logarithmic convention has the form $N(z,p)=\log|z-p|+H(z,p)$, where $H(\cdot,p)$ is harmonic throughout $\Omega$, and satisfies $\partial_{n_z}N(z,p)=2\pi/L$ on the smooth boundary pieces.
>
> If a real $C^2$ function $u$ near $\overline\Omega$ is harmonic in $\Omega$ and satisfies $\partial_n u=f$ on $\Gamma$, then $\int_\Gamma f\,ds=0$ and
>
> $$
> u(p)=A-\frac1{2\pi}\int_\Gamma N(z,p)f(z)\,ds_z,\qquad A=\frac1L\int_\Gamma u\,ds.
> $$
>
> Thus the representation determines the solution up to an additive constant.
````
### After

````text
> [!theorem|d00d8502-4689-5ddc-a0cc-bd3046064426.local at=cfac0fd2-3132-553e-b16f-7565120e5820] Solution of Neumann Problems
> Let $\Omega\subset\mathbb R^2$ be bounded, simply connected, and have piecewise smooth boundary $\Gamma$ of length $L>0$, with outward unit normal $n$. Write $z=x+iy$ and $p=x_0+iy_0\in\Omega$.
>
> A Neumann function in the positive-logarithmic convention has the form $N(z,p)=\log|z-p|+H(z,p)$, where $H(\cdot,p)$ is harmonic throughout $\Omega$, and satisfies $\partial_{n_z}N(z,p)=2\pi/L$ on the smooth boundary pieces.
>
> If a real $C^2$ function $u$ near $\overline\Omega$ is harmonic in $\Omega$ and satisfies $\partial_n u=f$ on $\Gamma$, then $\int_\Gamma f\,ds=0$ and
>
> $$
> u(p)=A-\frac1{2\pi}\int_\Gamma N(z,p)f(z)\,ds_z,\qquad A=\frac1L\int_\Gamma u\,ds.
> $$
>
> Thus the representation determines the solution up to an additive constant.
````

## 4. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|615861ea-6882-597e-8521-eb95d663fba0.local at=c0635cfb-c82f-5b89-a930-5a2e089b91b7] Zero-Flux Neumann Kernel Obtained from a Conformal Half-Plane Map
> Let $\phi$ be a conformal bijection from an unbounded simply connected plane region $\Omega$ onto the upper half-plane. Assume it extends smoothly with nonzero derivative on the boundary arcs under consideration and takes them to the real axis. For distinct $z,p\in\Omega$,
>
> $$
> N(z,p)=\log|\phi(z)-\phi(p)|+\log|\phi(z)-\overline{\phi(p)}|
> $$
>
> is harmonic away from $p$, has singular part $\log|z-p|$, and satisfies $\partial_{n_z}N=0$ on those arcs. Behavior at boundary corners, exceptional points, and infinity must be checked for the intended boundary-value representation.
````
### After

````text
> [!theorem|615861ea-6882-597e-8521-eb95d663fba0.local at=c0635cfb-c82f-5b89-a930-5a2e089b91b7] Neumann Function for Unbounded Regions
> Let $\phi$ be a conformal bijection from an unbounded simply connected plane region $\Omega$ onto the upper half-plane. Assume it extends smoothly with nonzero derivative on the boundary arcs under consideration and takes them to the real axis. For distinct $z,p\in\Omega$,
>
> $$
> N(z,p)=\log|\phi(z)-\phi(p)|+\log|\phi(z)-\overline{\phi(p)}|
> $$
>
> is harmonic away from $p$, has singular part $\log|z-p|$, and satisfies $\partial_{n_z}N=0$ on those arcs. Behavior at boundary corners, exceptional points, and infinity must be checked for the intended boundary-value representation.
````

## 5. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|52cbf0f8-4130-52e9-9a70-64404837c141.local at=2e3bcc5d-117a-58a4-816b-ef77d1fc988a] Neumann Function Representation for the Poisson–Neumann Problem on a Bounded Plane Region
> Let $\Omega\subset\mathbb R^2$ be bounded, simply connected, and have piecewise smooth boundary $\Gamma$ of length $L>0$, with outward unit normal $n$. Write $z=x+iy$ and $p=x_0+iy_0\in\Omega$.
>
> A Neumann function in the positive-logarithmic convention has the form $N(z,p)=\log|z-p|+H(z,p)$, where $H(\cdot,p)$ is harmonic throughout $\Omega$, and satisfies $\partial_{n_z}N(z,p)=2\pi/L$ on the smooth boundary pieces.
>
> If $u\in C^2$ near $\overline\Omega$ satisfies $\Delta u=h$ in $\Omega$ and $\partial_n u=f$ on $\Gamma$, then $\iint_\Omega h\,dA=\int_\Gamma f\,ds$ and
>
> $$
> u(p)=A+\frac1{2\pi}\iint_\Omega h(z)N(z,p)\,dA_z-\frac1{2\pi}\int_\Gamma N(z,p)f(z)\,ds_z,
> \qquad A=\frac1L\int_\Gamma u\,ds.
> $$
>
> In particular, the solution is determined up to an additive constant.
````
### After

````text
> [!theorem|52cbf0f8-4130-52e9-9a70-64404837c141.local at=2e3bcc5d-117a-58a4-816b-ef77d1fc988a] Solution of Poisson-Neumann Problem
> Let $\Omega\subset\mathbb R^2$ be bounded, simply connected, and have piecewise smooth boundary $\Gamma$ of length $L>0$, with outward unit normal $n$. Write $z=x+iy$ and $p=x_0+iy_0\in\Omega$.
>
> A Neumann function in the positive-logarithmic convention has the form $N(z,p)=\log|z-p|+H(z,p)$, where $H(\cdot,p)$ is harmonic throughout $\Omega$, and satisfies $\partial_{n_z}N(z,p)=2\pi/L$ on the smooth boundary pieces.
>
> If $u\in C^2$ near $\overline\Omega$ satisfies $\Delta u=h$ in $\Omega$ and $\partial_n u=f$ on $\Gamma$, then $\iint_\Omega h\,dA=\int_\Gamma f\,ds$ and
>
> $$
> u(p)=A+\frac1{2\pi}\iint_\Omega h(z)N(z,p)\,dA_z-\frac1{2\pi}\int_\Gamma N(z,p)f(z)\,ds_z,
> \qquad A=\frac1L\int_\Gamma u\,ds.
> $$
>
> In particular, the solution is determined up to an additive constant.
````

## 6. Move correction/commentary into the separate editorial record; keep the actual correction in the reading text.

### Before

````text
[Source correction: Exercises 10–11 use squared differences, so the cosine cross terms carry minus signs. The Neumann representation in Exercise 11 also requires the negative prefactor shown below.]
````
### After

````text

````

## 7. Move correction/commentary into the separate editorial record; keep the actual correction in the reading text.

### Before

````text
[Source correction: the antiderivative in Exercise 8 has a negative $2(x-a)$ term; differentiating the printed positive-sign version gives an extra $4$.]
````
### After

````text

````
