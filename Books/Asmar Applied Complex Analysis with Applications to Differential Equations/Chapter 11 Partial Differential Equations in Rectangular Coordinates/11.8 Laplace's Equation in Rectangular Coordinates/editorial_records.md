
# Editorial records

Reading note: 11.8 Laplace's Equation in Rectangular Coordinates.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!definition] Dirichlet problem for Laplace’s equation
> Given a domain $\Omega$ and prescribed boundary values $h$, the Dirichlet problem for Laplace’s equation asks for a harmonic function $u$ in $\Omega$ satisfying $u=h$ on $\partial\Omega$. For the classical continuous-boundary formulation, $u\in C^2(\Omega)\cap C(\overline\Omega)$.
````
### After

````text
> [!definition] Dirichlet problem for Laplace’s equation
> A problem consisting of Laplace's equation on a region in the plane together with specified boundary values is called a Dirichlet problem.
````

## 2. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!equation] Fourier series solution of the Dirichlet problem for a rectangle
> Let $a,b>0$. For Laplace’s equation $u_{xx}+u_{yy}=0$ on $0<x<a$, $0<y<b$, prescribe piecewise smooth boundary data
> $$
> u(x,0)=f_1(x),\quad u(x,b)=f_2(x),\quad u(0,y)=g_1(y),\quad u(a,y)=g_2(y).
> $$
> The solution in the rectangle is
> $$
> \begin{aligned}
> u(x,y)={}&\sum_{n=1}^{\infty}\left[A_n\sinh\frac{n\pi(b-y)}a+B_n\sinh\frac{n\pi y}a\right]\sin\frac{n\pi x}a\\
> &+\sum_{n=1}^{\infty}\left[C_n\sinh\frac{n\pi(a-x)}b+D_n\sinh\frac{n\pi x}b\right]\sin\frac{n\pi y}b,
> \end{aligned}
> $$
> with
> $$
> \begin{aligned}
> A_n&=\frac{2}{a\sinh(n\pi b/a)}\int_0^a f_1(x)\sin\frac{n\pi x}a\,dx,&
> B_n&=\frac{2}{a\sinh(n\pi b/a)}\int_0^a f_2(x)\sin\frac{n\pi x}a\,dx,\\
> C_n&=\frac{2}{b\sinh(n\pi a/b)}\int_0^b g_1(y)\sin\frac{n\pi y}b\,dy,&
> D_n&=\frac{2}{b\sinh(n\pi a/b)}\int_0^b g_2(y)\sin\frac{n\pi y}b\,dy.
> \end{aligned}
> $$
> Boundary data are attained at continuity points on the open sides. Continuity on the closed rectangle additionally requires compatible values at the corners.
````
### After

````text
> [!equation] Solution of the Dirichlet Problem in a Rectangle
> Let $a,b>0$. For Laplace’s equation $u_{xx}+u_{yy}=0$ on $0<x<a$, $0<y<b$, prescribe piecewise smooth boundary data
> $$
> u(x,0)=f_1(x),\quad u(x,b)=f_2(x),\quad u(0,y)=g_1(y),\quad u(a,y)=g_2(y).
> $$
> The solution of the two dimensional Dirichlet problem with these boundary conditions is
>
> $$
> u(x, y)=\sum_{n=1}^{\infty} A_{n} \sin \frac{n \pi}{a} x \sinh \frac{n \pi}{a}(b-y)+\sum_{n=1}^{\infty} B_{n} \sin \frac{n \pi}{a} x \sinh \frac{n \pi}{a} y
> $$
>
> $$
> +\sum_{n=1}^{\infty} C_{n} \sinh \frac{n \pi}{b}(a-x) \sin \frac{n \pi}{b} y+\sum_{n=1}^{\infty} D_{n} \sinh \frac{n \pi}{b} x \sin \frac{n \pi}{b} y,
> $$
>
> with
> $$
> \begin{aligned}
> A_n&=\frac{2}{a\sinh(n\pi b/a)}\int_0^a f_1(x)\sin\frac{n\pi x}a\,dx,&
> B_n&=\frac{2}{a\sinh(n\pi b/a)}\int_0^a f_2(x)\sin\frac{n\pi x}a\,dx,\\
> C_n&=\frac{2}{b\sinh(n\pi a/b)}\int_0^b g_1(y)\sin\frac{n\pi y}b\,dy,&
> D_n&=\frac{2}{b\sinh(n\pi a/b)}\int_0^b g_2(y)\sin\frac{n\pi y}b\,dy.
> \end{aligned}
> $$
> Boundary data are attained at continuity points on the open sides. Continuity on the closed rectangle additionally requires compatible values at the corners.
````
