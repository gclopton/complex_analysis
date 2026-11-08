
# Editorial records

Reading note: 15.4 Hermite and Laguerre Polynomials.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|6e32b0f4-a134-52da-92b5-4ff791421141.local at=ae4809c8-09c9-592d-b0d6-b8498aa02cc1] Weighted Orthogonality and Norms of Physicists’ Hermite Polynomials
> The physicists' Hermite polynomial $H_n$ is the polynomial solution of $H_n''-2xH_n'+2nH_n=0$ with leading coefficient $2^n$, for $n=0,1,2,\ldots$.
>
> $$
> \int_{-\infty}^\infty H_m(x)H_n(x)e^{-x^2}\,dx
> =\begin{cases}0,&m\ne n,\\2^nn!\sqrt\pi,&m=n.\end{cases}
> $$
````
### After

````text
> [!theorem|6e32b0f4-a134-52da-92b5-4ff791421141.local at=ae4809c8-09c9-592d-b0d6-b8498aa02cc1] Orthogonality of Hermite Polynomials
> (i) For nonnegative integers $m$ and $n$ with $m \neq n$,  we have
>
> $$
> \int_{-\infty}^{\infty} H_{m}(x) H_{n}(x) e^{-x^{2}} d x=0 .
> $$
>
> (ii) For all $n=0,1,2, \ldots$, we have
>
> $$
> \int_{-\infty}^{\infty} H_{n}^{2}(x) e^{-x^{2}} d x=2^{n} n!\sqrt{\pi} .
> $$
>
> Here $H_n$ is the Hermite polynomial of degree $n$ with leading coefficient $2^n$.
````

## 2. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|51b8cc9b-4f9a-524f-93ba-008d2df464c2.local at=6e3b54e0-9c0e-5578-be0f-a15e118f660f] Hermite Series Expansion with Gaussian Weight
> The physicists' Hermite polynomial $H_n$ is the polynomial solution of $H_n''-2xH_n'+2nH_n=0$ with leading coefficient $2^n$, for $n=0,1,2,\ldots$.
>
> For $f\in L^2(\mathbb R,e^{-x^2}dx)$, its Hermite expansion converges in that weighted norm and is
>
> $$
> f=\sum_{j=0}^\infty A_jH_j,\qquad
> A_j=\frac{1}{2^jj!\sqrt\pi}\int_{-\infty}^\infty f(x)H_j(x)e^{-x^2}\,dx.
> $$
>
> If $f$ is also piecewise smooth, the series converges at each finite $x$ to $[f(x+)+f(x-)]/2$, and hence to $f(x)$ at continuity points.
````
### After

````text
> [!theorem|51b8cc9b-4f9a-524f-93ba-008d2df464c2.local at=6e3b54e0-9c0e-5578-be0f-a15e118f660f] Hermite Series Expansions
> If $f$ is piecewise smooth on $(-\infty, \infty)$, and
>
> $$
> \int_{-\infty}^{\infty}|f(x)|^{2} e^{-x^{2}} d x<\infty
> $$
>
> then we have the Hermite series expansion
>
> $$
> f(x)=\sum_{j=0}^{\infty} A_{j} H_{j}(x)
> $$
>
> where the Hermite coefficients $A_{j}$ are given by
>
> $$
> A_{j}=\frac{1}{2^{j} j!\sqrt{\pi}} \int_{-\infty}^{\infty} f(x) H_{j}(x) e^{-x^{2}} d x
> $$
>
> For any $x$, the Hermite series converges to $f(x)$ if $f$ is continuous at $x$ and to $[f(x+)+f(x-)] / 2$ otherwise.
>
> Here $H_n$ is the Hermite polynomial of degree $n$ with leading coefficient $2^n$.
````

## 3. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|67be6b7a-d430-5516-a261-a7c3b3d0d1ee.local at=9a8d7693-19cf-5127-9bf4-bf77f65b0960] Weighted Orthogonality and Unit Norms of Laguerre Polynomials
> The Laguerre polynomial $L_n$ solves $xL_n''+(1-x)L_n'+nL_n=0$ and has leading coefficient $(-1)^n/n!$, for $n=0,1,2,\ldots$.
>
> $$
> \int_0^\infty L_m(x)L_n(x)e^{-x}\,dx
> =\begin{cases}0,&m\ne n,\\1,&m=n.\end{cases}
> $$
````
### After

````text
> [!theorem|67be6b7a-d430-5516-a261-a7c3b3d0d1ee.local at=9a8d7693-19cf-5127-9bf4-bf77f65b0960] Orthogonality of Laguerre Polynomials
> (i) For nonnegative integers $m$ and $n$ such that $m \neq n$, we have
>
> $$
> \int_{0}^{\infty} L_{m}(x) L_{n}(x) e^{-x} d x=0
> $$
>
> (ii) For all $n=0,1,2, \ldots$ we have
>
> $$
> \int_{0}^{\infty} L_{n}^{2}(x) e^{-x} d x=1
> $$
>
> Here $L_n$ is the Laguerre polynomial of degree $n$ with leading coefficient $(-1)^n/n!$.
````

## 4. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|a4e31473-2fcb-525c-958f-476f80490a1a.local at=0ce9b992-9e38-556e-b4d2-89da4eebc5e9] Laguerre Series Expansion with Exponential Weight
> The Laguerre polynomial $L_n$ solves $xL_n''+(1-x)L_n'+nL_n=0$ and has leading coefficient $(-1)^n/n!$, for $n=0,1,2,\ldots$.
>
> For $f\in L^2((0,\infty),e^{-x}dx)$, its Laguerre expansion converges in that weighted norm and is
>
> $$
> f=\sum_{j=0}^\infty A_jL_j,\qquad A_j=\int_0^\infty f(x)L_j(x)e^{-x}\,dx.
> $$
>
> If $f$ is also piecewise smooth on $[0,\infty)$, the series converges at every $x>0$ to $[f(x+)+f(x-)]/2$, and hence to $f(x)$ at continuity points.
````
### After

````text
> [!theorem|a4e31473-2fcb-525c-958f-476f80490a1a.local at=0ce9b992-9e38-556e-b4d2-89da4eebc5e9] Laguerre Series Expansions
> Suppose that $f$ is piecewise smooth on $[0, \infty)$, and that $\int_{0}^{\infty}|f(x)|^{2} e^{-x} d x< \infty$. Then we have the Laguerre series expansion
>
> $$
> f(x)=\sum_{j=0}^{\infty} A_{j} L_{j}(x)
> $$
>
> where the Laguerre coefficients $A_{j}$ are given by
>
> $$
> A_{j}=\int_{0}^{\infty} f(x) L_{j}(x) e^{-x} d x
> $$
>
> For any $0<x<\infty$, the Laguerre series converges to $f(x)$ if $f$ is continuous at $x$ and to $[f(x+)+f(x-)] / 2$ otherwise.
>
> Here $L_n$ is the Laguerre polynomial of degree $n$ with leading coefficient $(-1)^n/n!$.
````

## 5. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|7f66db87-1a71-5e78-99e1-964dc08b0749.local at=b5fa0093-3e56-57e1-9f10-12b71ab4dfc1] Weighted Orthogonality and Norms of Generalized Laguerre Polynomials
> For $\alpha>-1$ and integers $n\ge0$, let $L_n^\alpha$ denote the generalized Laguerre polynomial solving $xy''+(\alpha+1-x)y'+ny=0$ with leading coefficient $(-1)^n/n!$.
>
> $$
> \int_0^\infty L_m^\alpha(x)L_n^\alpha(x)x^\alpha e^{-x}\,dx
> =\begin{cases}0,&m\ne n,\\\Gamma(n+\alpha+1)/n!,&m=n.\end{cases}
> $$
````
### After

````text
> [!theorem|7f66db87-1a71-5e78-99e1-964dc08b0749.local at=b5fa0093-3e56-57e1-9f10-12b71ab4dfc1] Orthogonality of Generalized Laguerre Polynomials
> (i) If $m \neq n$ are nonnegative integers, then
>
> $$
> \int_{0}^{\infty} L_{m}^{\alpha}(x) L_{n}^{\alpha}(x) e^{-x} x^{\alpha} d x=0
> $$
>
> (ii) For all $n=0,1,2, \ldots$, we have
>
> $$
> \int_{0}^{\infty}\left[L_{n}^{\alpha}(x)\right]^{2} e^{-x} x^{\alpha} d x=\frac{\Gamma(n+\alpha+1)}{n!}
> $$
>
> Here $\alpha>-1$ and $L_n^\alpha$ is the generalized Laguerre polynomial solving $xy^{\prime\prime}+(\alpha+1-x)y^{\prime}+ny=0$, with leading coefficient $(-1)^n/n!$.
````

## 6. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|af060bf3-e630-597f-9052-f92a4f18ff42.local at=ce33c97d-86a8-525e-8c2a-af2f045154fb] Generalized Laguerre Series Expansion with Gamma Weight
> For $\alpha>-1$ and integers $n\ge0$, let $L_n^\alpha$ denote the generalized Laguerre polynomial solving $xy''+(\alpha+1-x)y'+ny=0$ with leading coefficient $(-1)^n/n!$.
>
> For $f\in L^2((0,\infty),x^\alpha e^{-x}dx)$, the generalized Laguerre expansion converges in that weighted norm and is
>
> $$
> f=\sum_{j=0}^\infty A_jL_j^\alpha,\qquad
> A_j=\frac{j!}{\Gamma(j+\alpha+1)}\int_0^\infty f(x)L_j^\alpha(x)x^\alpha e^{-x}\,dx.
> $$
>
> If $f$ is also piecewise smooth on $[0,\infty)$, the series converges for $x>0$ to $[f(x+)+f(x-)]/2$, and hence to $f(x)$ at continuity points.
````
### After

````text
> [!theorem|af060bf3-e630-597f-9052-f92a4f18ff42.local at=ce33c97d-86a8-525e-8c2a-af2f045154fb] Generalized Laguerre Series Expansions
> Suppose that $f$ is piecewise smooth on $[0, \infty)$, and that $\int_{0}^{\infty}|f(x)|^{2} e^{-x} x^{\alpha}\,dx<\infty$. Then we have the generalized Laguerre series expansion
>
> $$
> f(x)=\sum_{j=0}^{\infty} A_{j} L_{j}^{\alpha}(x)
> $$
>
> where the generalized Laguerre coefficients $A_{j}$ are given by
>
> $$
> A_{j}=\frac{j!}{\Gamma(j+\alpha+1)} \int_{0}^{\infty} f(x) L_{j}^{\alpha}(x) e^{-x} x^{\alpha} d x
> $$
>
> For any $0<x<\infty$, the Laguerre series converges to $f(x)$ if $f$ is continuous at $x$ and to $[f(x+)+f(x-)] / 2$ otherwise.
>
> Here $\alpha>-1$ and $L_n^\alpha$ is the generalized Laguerre polynomial solving $xy^{\prime\prime}+(\alpha+1-x)y^{\prime}+ny=0$, with leading coefficient $(-1)^n/n!$.
````

## 7. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|3d2d887f-90dc-5099-a66f-293a73c26db4.local at=889768a9-4bc1-5575-b0e4-0b909f6c744c] Derivative and Three-Term Recurrences for Generalized Laguerre Polynomials
> For $\alpha>-1$ and integers $n\ge0$, let $L_n^\alpha$ denote the generalized Laguerre polynomial solving $xy''+(\alpha+1-x)y'+ny=0$ with leading coefficient $(-1)^n/n!$.
>
> For integers $n\ge1$,
>
> $$
> \begin{aligned}
> (L_n^\alpha)'&=-L_{n-1}^{\alpha+1},\\
> L_n^\alpha&=\frac{x}{n}(L_{n-1}^\alpha)'+\left(1+\frac{\alpha}{n}-\frac{x}{n}\right)L_{n-1}^\alpha,\\
> (L_n^\alpha)'&=(L_{n-1}^\alpha)'-L_{n-1}^\alpha,\\
> (n+1)L_{n+1}^\alpha&=(2n+\alpha+1-x)L_n^\alpha-(n+\alpha)L_{n-1}^\alpha.
> \end{aligned}
> $$
````
### After

````text
> [!theorem|3d2d887f-90dc-5099-a66f-293a73c26db4.local at=889768a9-4bc1-5575-b0e4-0b909f6c744c] Formulas for Generalized Laguerre Polynomials
> For integers $n\ge1$, we have
>
> $$
> \left[L_{n}^{\alpha}(x)\right]^{\prime}=-L_{n-1}^{\alpha+1}(x) ;
> $$
>
> $$
> L_{n}^{\alpha}(x)=\frac{x}{n}\left[L_{n-1}^{\alpha}(x)\right]^{\prime}+\left(1+\frac{\alpha}{n}-\frac{x}{n}\right) L_{n-1}^{\alpha}(x) ;
> $$
>
> $$
> \left[L_{n}^{\alpha}(x)\right]^{\prime}=\left[L_{n-1}^{\alpha}(x)\right]^{\prime}-L_{n-1}^{\alpha}(x) ;
> $$
>
> $$
> (n+1) L_{n+1}^{\alpha}(x)-(2 n+\alpha+1-x) L_{n}^{\alpha}(x)+(n+\alpha) L_{n-1}^{\alpha}(x)=0
> $$
>
> Here $\alpha>-1$ and $L_n^\alpha$ is the generalized Laguerre polynomial solving $xy^{\prime\prime}+(\alpha+1-x)y^{\prime}+ny=0$, with leading coefficient $(-1)^n/n!$.
````

## 8. Restore source wording; retain only the actual correction.

### Before

````text
No antiderivative of a strictly positive integrand can vanish at both endpoints.
````
### After

````text

````

## 9. Move correction/commentary into the separate editorial record; keep the actual correction in the reading text.

### Before

````text
[Source correction: the generating function uses $(1-t)^{\alpha+1}$ in the denominator, not its reciprocal.]
````
### After

````text

````

## 10. Move correction/commentary into the separate editorial record; keep the actual correction in the reading text.

### Before

````text
[Source correction: Exercise 13 has an extra factorial on $(2k+1)$ in the printed coefficient. The corrected coefficient below follows from the endpoint value $H_{2k}(0)=(-1)^k(2k)!/k!$.]
````
### After

````text

````
