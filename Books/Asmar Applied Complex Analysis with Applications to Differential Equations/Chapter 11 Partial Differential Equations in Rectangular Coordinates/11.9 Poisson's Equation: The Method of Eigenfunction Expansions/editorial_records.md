
# Editorial records

Reading note: 11.9 Poisson's Equation: The Method of Eigenfunction Expansions.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!equation|930aae7c-1ac9-5c9f-be40-285f192fbff5.local at=5ebb093c-bf33-5e97-ad7e-952ab63cd4bb] Eigenfunction solution of the rectangular Poisson problem with Dirichlet data
> Let $a,b>0$, $\Omega=(0,a)\times(0,b)$, and consider $\Delta u=f$ with prescribed Dirichlet boundary values $h$. Write $u=u_0+v$, where $v$ solves $\Delta v=0$ with boundary values $h$. The zero-boundary part is
> $$
> u_0(x,y)=\sum_{n=1}^{\infty}\sum_{m=1}^{\infty}E_{mn}\sin\frac{m\pi x}{a}\sin\frac{n\pi y}{b},
> $$
> where
> $$
> \lambda_{mn}=\left(\frac{m\pi}{a}\right)^2+\left(\frac{n\pi}{b}\right)^2,\qquad
> E_{mn}=-\frac4{ab\lambda_{mn}}\int_0^b\int_0^a f(x,y)\sin\frac{m\pi x}{a}\sin\frac{n\pi y}{b}\,dx\,dy.
> $$
> For $f\in L^2(\Omega)$ the series gives the weak zero-Dirichlet solution; use classical differentiations only when the data and convergence justify them. The harmonic part $v$ must have the prescribed boundary trace, with corner compatibility required for continuity on the closed rectangle.
````
### After

````text
> [!equation|930aae7c-1ac9-5c9f-be40-285f192fbff5.local at=5ebb093c-bf33-5e97-ad7e-952ab63cd4bb] Solution of Poisson's Equation in a Rectangle
> Let $a,b>0$, $\Omega=(0,a)\times(0,b)$, and consider $\Delta u=f$ with prescribed Dirichlet boundary values $h$. Write $u=u_1+u_2$, where $u_2$ solves $\Delta v=0$ with boundary values $h$. The zero-boundary part is
> $$
> u_1(x,y)=\sum_{n=1}^{\infty}\sum_{m=1}^{\infty}E_{mn}\sin\frac{m\pi x}{a}\sin\frac{n\pi y}{b},
> $$
> where
> $$
> \lambda_{mn}=\left(\frac{m\pi}{a}\right)^2+\left(\frac{n\pi}{b}\right)^2,\qquad
> E_{mn}=-\frac4{ab\lambda_{mn}}\int_0^b\int_0^a f(x,y)\sin\frac{m\pi x}{a}\sin\frac{n\pi y}{b}\,dx\,dy.
> $$
> Assume the data and convergence justify the displayed expansion and the required differentiations.
````
