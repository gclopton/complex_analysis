
# Editorial records

Reading note: 12.8 Bessel Series Expansions.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|cf3f6d2d-dc5a-555b-86e2-323ff9599805.local at=d93068ef-da1e-5cd8-a42e-9b6e1a1173ea] Pointwise convergence of a Fourier–Bessel series on an open finite interval
> Fix $a>0$ and real $p\ge0$. Suppose $f$ is piecewise smooth on $[0,a]$: it has a finite partition into continuously differentiable pieces with finite one-sided limits of the function and its derivative. Let $\alpha_{pj}$ be the $j$th positive zero of the Bessel function $J_p$ of the first kind, and put $\lambda_{pj}=\alpha_{pj}/a$. The Fourier–Bessel series
> $$
> \sum_{j=1}^{\infty}A_jJ_p(\lambda_{pj}x),\qquad
> A_j=\frac{2}{a^2J_{p+1}(\alpha_{pj})^2}\int_0^a f(t)J_p(\lambda_{pj}t)t\,dt,
> $$
> converges at every $0<x<a$ to
> $$
> \frac{f(x+)+f(x-)}2.
> $$
> At continuity points this equals $f(x)$. No endpoint-convergence assertion is included.
````
### After

````text
> [!theorem|cf3f6d2d-dc5a-555b-86e2-323ff9599805.local at=d93068ef-da1e-5cd8-a42e-9b6e1a1173ea] Bessel Series of Order $p$
> Let $a>0$, $p\geq0$, and let $J_p$ denote the Bessel function of the first kind.
>
> If $f$ is piecewise smooth on $[0, a]$, then $f$ has a Bessel series expansion of order $p$ on the interval $(0, a)$ given by
>
> $$
> f(x)=\sum_{j=1}^{\infty} A_{j} J_{p}\left(\lambda_{p j} x\right),
> $$
>
> where $\lambda_{p 1}, \lambda_{p 2}, \ldots$ are the scaled positive zeros of the Bessel function $J_{p}$ $\lambda_{pj}=\alpha_{pj}/a$, with $\alpha_{pj}$ the $j$th positive zero of $J_p$, and $A_j=\frac{2}{a^2J_{p+1}(\alpha_{pj})^2}\int_0^a f(t)J_p(\lambda_{pj}t)t\,dt$. In the interval ( $0, a$ ), the series converges to $f(x)$ where $f$ is continuous and converges to the average $\frac{f(x+)+f(x-)}{2}$ at the points of discontinuity.
````

## 2. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|ab5e42d2-4be6-53d3-ad29-a2620bbff2c2.local at=12c592fe-9ce1-5ba9-9978-23abf0e09241] Regular Dirichlet eigenmodes of the parametric Bessel equation
> Let $a>0$, $p\ge0$, and $\lambda>0$. The boundary-value problem
> $$
> x^2y''+xy'+(\lambda^2x^2-p^2)y=0,\qquad 0<x<a,
> $$
> with $y$ bounded as $x\to0^+$ and $y(a)=0$ has a nonzero solution exactly when
> $$
> \lambda=\lambda_{pj}=\frac{\alpha_{pj}}a,\qquad j=1,2,\ldots,
> $$
> where $\alpha_{pj}$ is the $j$th positive zero of the Bessel function $J_p$ of the first kind. Each such solution is a scalar multiple of $J_p(\lambda_{pj}x)$. Distinct modes are orthogonal with weight $x$, and
> $$
> \int_0^a J_p(\lambda_{pj}x)J_p(\lambda_{pk}x)x\,dx=
> \begin{cases}0,&j\ne k,\\[2pt]\dfrac{a^2}2J_{p+1}(\alpha_{pj})^2,&j=k.\end{cases}
> $$
````
### After

````text
> [!theorem|ab5e42d2-4be6-53d3-ad29-a2620bbff2c2.local at=12c592fe-9ce1-5ba9-9978-23abf0e09241] Parametric Form of Bessel's Equation
> Let $p \geq 0, a>0$, and let $\alpha_{p j}$ denote the $j$ th positive zero of $J_{p}(x)$. For $j=1,2, \ldots$, the functions $J_{p}\left(\frac{\alpha_{p j}}{a} x\right)$ are solutions of the parametric form of Bessel's equation of order $p$,
>
> $$
> x^{2} y^{\prime \prime}(x)+x y^{\prime}(x)+\left(\lambda^{2} x^{2}-p^{2}\right) y(x)=0
> $$
>
> together with the boundary conditions
>
> $$
> y(0) \text { finite, } y(a)=0
> $$
>
> when $\lambda=\lambda_{p j}=\frac{\alpha_{p j}}{a}$, and these are the only solutions of the displayed equation, aside from scalar multiples, with these properties. Moreover, these solutions are orthogonal on the interval $[0, a]$ with respect to the weight function $x$.
````

## 3. Move correction/commentary into the separate editorial record; keep the actual correction in the reading text.

### Before

````text
[Corrected: the printed fifth positive zero of $J_2$ is incorrect; its value is approximately $17.9598$.]
````
### After

````text

````
