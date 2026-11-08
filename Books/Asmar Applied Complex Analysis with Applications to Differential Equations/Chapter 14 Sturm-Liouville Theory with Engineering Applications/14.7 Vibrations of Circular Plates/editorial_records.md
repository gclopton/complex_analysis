
# Editorial records

Reading note: 14.7 Vibrations of Circular Plates.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!proposition] Radial Scaling of Solutions of the Laplace Eigenvalue Equation
> Suppose $\phi(r,\theta)$ satisfies $\nabla^2\phi=\lambda\phi$ on a planar domain. For a positive real dilation $\alpha$ and a nonzero constant $A$, define $\psi(r,\theta)=A\phi(\alpha r,\theta)$ on the correspondingly rescaled domain. Then $\nabla^2\psi=\alpha^2\lambda\psi$. This is a statement about the differential equation; boundary conditions must also be rescaled.
>
> The same algebra applies to a complex value of $\alpha$ when the radial factor has an analytic continuation to the required complex arguments, as for integer-order Bessel functions.
````
### After

````text
> [!proposition] Dilation of Eigenfunctions
> Suppose that $\phi(r, \theta)$ satisfies $\nabla^{2} \phi=\lambda \phi(\lambda \neq 0)$, and let $\psi(r, \theta)=A \phi(\alpha r, \theta)$, where $A$ and $\alpha$ are nonzero constants. Then $\nabla^{2} \psi=\alpha^{2} \lambda \psi$. The domain is rescaled accordingly. Complex $\alpha$ requires analytic continuation of the radial factor to the arguments used.
````

## 2. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem] Clamped Circular-Plate Eigenfunctions from Bessel Functions
> Let $a>0$. For each integer $m\ge0$, let $k_{mn}$, $n=1,2,\ldots$, be the positive roots in increasing order of
>
> $$
> J_m(ka)I_m'(ka)-I_m(ka)J_m'(ka)=0,
> $$
>
> where $J_m$ and $I_m$ are the Bessel and modified Bessel functions of order $m$, and primes denote derivatives of their arguments. Define
>
> $$
> R_{mn}(r)=I_m(k_{mn}a)J_m(k_{mn}r)-J_m(k_{mn}a)I_m(k_{mn}r).
> $$
>
> The nonzero modes $R_{mn}(r)\cos(m\theta)$ for $m\ge0$, and $R_{mn}(r)\sin(m\theta)$ for $m\ge1$, are smooth at the center and satisfy
>
> $$
> \nabla^4\phi=k_{mn}^4\phi\quad(r<a),\qquad
> \phi(a,\theta)=\phi_r(a,\theta)=0.
> $$
````
### After

````text
> [!theorem] Eigenfunctions of the Biharmonic Operator
> For $m=0,1,2, \ldots, n=1,2, \ldots$, consider the function $\phi_{m n}(r, \theta)$ given by
>
> $$
> \left[I_{m}\left(k_{m n} a\right) J_{m}\left(k_{m n} r\right)-J_{m}\left(k_{m n} a\right) I_{m}\left(k_{m n} r\right)\right] \cos m \theta
> $$
>
> or, for $m\ge1$,
>
> $$
> \left[I_{m}\left(k_{m n} a\right) J_{m}\left(k_{m n} r\right)-J_{m}\left(k_{m n} a\right) I_m\left(k_{m n} r\right)\right] \sin m \theta
> $$
>
> where $k_{m n}$ is a positive root of
>
> $$
> J_{m}(k a) I_{m}^{\prime}(k a)-I_{m}(k a) \cdot J_{m}^{\prime}(k a)=0
> $$
>
> Then $\nabla^{4} \phi_{m n}=k_{m n}^{4} \phi_{m n}$ and $\phi_{m n}$ satisfies the boundary conditions $\phi_{mn}(a,\theta)=\partial_r\phi_{mn}(a,\theta)=0$. Here $a>0$, $J_m$ and $I_m$ are the Bessel and modified Bessel functions, and $k_{mn}$ denotes the $n$th positive root.
````

## 3. Restore source wording; retain only the actual correction.

### Before

````text
The radial case $m=0$ below illustrates the coefficient calculation.
````
### After

````text
We will prove these facts when $m=0$ in the second part of this section.
````

## 4. Preserve the source limitation/correction history in the editorial record only.

### Before

````text
[Source corrections: the signs and factors in Exercises 2 and 6, the order restriction in Exercise 7, and the $y_2$ definition and derivative sum in Exercise 12 are corrected. The sequence is restored to Exercises 1–22.]
````
### After

````text

````

## 5. Move correction/commentary into the separate editorial record; keep the actual correction in the reading text.

### Before

````text
[Source correction: the printed real-axis asymptotic formula for $J_0$ does not by itself justify substituting an imaginary argument. Exercise 22 now uses the preceding integral representation to establish the stated result.]
````
### After

````text

````
