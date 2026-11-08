
# Editorial records

Reading note: 11.7 The Two Dimensional Wave and Heat Equations.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!equation|c7aedb00-3e43-5e30-a0c8-8df3b6883019.local at=44160e7e-a39e-530b-8253-84cfc783831e] Double sine series solution for a rectangular membrane with fixed edges
> Let $a,b,c>0$. On $0<x<a$, $0<y<b$, consider $u_{tt}=c^2(u_{xx}+u_{yy})$, with $u=0$ on all four edges, $u(x,y,0)=f(x,y)$ and $u_t(x,y,0)=g(x,y)$. Its eigenfunction expansion is
> $$
> u(x,y,t)=\sum_{n=1}^{\infty}\sum_{m=1}^{\infty}\left(B_{mn}\cos\lambda_{mn}t+B^*_{mn}\sin\lambda_{mn}t\right)\sin\frac{m\pi x}{a}\sin\frac{n\pi y}{b},
> $$
> where
> $$
> \begin{aligned}
> \lambda_{mn}&=c\pi\sqrt{m^2/a^2+n^2/b^2},\\
> B_{mn}&=\frac4{ab}\int_0^b\int_0^a f(x,y)\sin\frac{m\pi x}{a}\sin\frac{n\pi y}{b}\,dx\,dy,\\
> B^*_{mn}&=\frac4{ab\lambda_{mn}}\int_0^b\int_0^a g(x,y)\sin\frac{m\pi x}{a}\sin\frac{n\pi y}{b}\,dx\,dy.
> \end{aligned}
> $$
> For a classical solution, the initial data must satisfy the boundary compatibility conditions and the series must permit the required differentiations. For square-integrable data the expansion is understood in the spectral, generalized sense rather than as an assertion of pointwise second differentiability.
````
### After

````text
> [!equation|c7aedb00-3e43-5e30-a0c8-8df3b6883019.local at=44160e7e-a39e-530b-8253-84cfc783831e] Solution of the Two Dimensional Wave Equation
> Let $a,b,c>0$. On $0<x<a$, $0<y<b$, consider $u_{tt}=c^2(u_{xx}+u_{yy})$, with $u=0$ on all four edges, $u(x,y,0)=f(x,y)$ and $u_t(x,y,0)=g(x,y)$. Assume compatible initial data and convergence permitting the required differentiations.
>
> The solution of the two dimensional wave equation with the stated boundary and initial conditions is
>
> $$
> u(x, y, t)=\sum_{n=1}^{\infty} \sum_{m=1}^{\infty}\left(B_{m n} \cos \lambda_{m n} t+B_{m n}^{*} \sin \lambda_{m n} t\right) \sin \frac{m \pi}{a} x \sin \frac{n \pi}{b} y
> $$
>
> where
>
> $$
> \lambda_{m n}=c \pi \sqrt{\frac{m^{2}}{a^{2}}+\frac{n^{2}}{b^{2}}}
> $$
>
> where
> $$
> \begin{aligned}
> \lambda_{mn}&=c\pi\sqrt{m^2/a^2+n^2/b^2},\\
> B_{mn}&=\frac4{ab}\int_0^b\int_0^a f(x,y)\sin\frac{m\pi x}{a}\sin\frac{n\pi y}{b}\,dx\,dy,\\
> B^*_{mn}&=\frac4{ab\lambda_{mn}}\int_0^b\int_0^a g(x,y)\sin\frac{m\pi x}{a}\sin\frac{n\pi y}{b}\,dx\,dy.
> \end{aligned}
> $$
````

## 2. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|fd168324-0286-5644-8537-4b299510d6bb.local at=33b94323-398f-5887-bbb2-160e06024e5c] Double Fourier sine series representation on a rectangle
> Let $a,b>0$ and let $f$ and its first and second partial derivatives be continuous on $[0,a]\times[0,b]$. At interior points $0<x<a$, $0<y<b$,
> $$
> f(x,y)=\sum_{n=1}^{\infty}\sum_{m=1}^{\infty}B_{mn}\sin\frac{m\pi x}{a}\sin\frac{n\pi y}{b},
> $$
> where
> $$
> B_{mn}=\frac4{ab}\int_0^b\int_0^a f(x,y)\sin\frac{m\pi x}{a}\sin\frac{n\pi y}{b}\,dx\,dy,\qquad m,n\ge1.
> $$
> The sine series is zero on the edges; matching nonzero edge values is not asserted.
````
### After

````text
> [!theorem|fd168324-0286-5644-8537-4b299510d6bb.local at=33b94323-398f-5887-bbb2-160e06024e5c] Double Sine Series Representation
> Suppose that $f(x, y)$ and its first and second partial derivatives are continuous on $[0,a]\times[0,b]$, where $a,b>0$. For $0<x<a$, $0<y<b$, we have the double Fourier sine series expansion
>
> $$
> f(x, y)=\sum_{n=1}^{\infty} \sum_{m=1}^{\infty} B_{m n} \sin \frac{m \pi}{a} x \sin \frac{n \pi}{b} y
> $$
>
> where
> $$
> B_{mn}=\frac4{ab}\int_0^b\int_0^a f(x,y)\sin\frac{m\pi x}{a}\sin\frac{n\pi y}{b}\,dx\,dy,\qquad m,n\ge1.
> $$
````
