
# Editorial records

Reading note: 7.6 Proof of the.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Move editorial commentary out of the reading note.

### Before

````text
*Editorial corrections: the cosine difference is $\cos n(x-t)$; the removable value of the proof’s quotient is $-2f'(x)$; the uniform-continuity bound uses $M_n=\max|f(x)-f(x-\pi/n)|$; breakpoint values of the linear correction are specified. These corrections address typographical or omitted details in the source.*
````
### After

````text

````

## Additional source comparison

## 1. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!lemma|54fca167-cfae-5182-8b29-3690782343e5.local at=2a9f1aab-547d-5ac9-bfbc-a48bb9d5c925] Dirichlet Kernel Representation of Fourier Partial Sums
> Let $f$ be a $2\pi$-periodic piecewise continuous function and $N\geq1$. Define
>
> $$
> D_N(\theta)=1+2\sum_{n=1}^{N}\cos(n\theta)=\frac{\sin((N+\tfrac12)\theta)}{\sin(\theta/2)},
> $$
>
> where the quotient has its continuous value $2N+1$ at $\theta\in2\pi\mathbb Z$. If $s_N$ is the Fourier partial sum of order $N$ of $f$, then
>
> $$
> s_N(x)=\frac1{2\pi}\int_{-\pi}^{\pi}f(t)D_N(x-t)\,dt=\frac1{2\pi}\int_{-\pi}^{\pi}f(x-t)D_N(t)\,dt.
> $$
````
### After

````text
> [!lemma|54fca167-cfae-5182-8b29-3690782343e5.local at=2a9f1aab-547d-5ac9-bfbc-a48bb9d5c925] Dirichlet Kernel and Fourier Series
> Let $D_N(\theta)=1+2\sum_{n=1}^N\cos(n\theta)$, and let $s_N$ denote the Fourier partial sum of order $N$.
>
> If $f$ is a $2 \pi$-periodic piecewise continuous function, and $N \geq 1$, then
>
> $$
> s_{N}(x)=\frac{1}{2 \pi} \int_{-\pi}^{\pi} f(t) D_{N}(x-t) d t=\frac{1}{2 \pi} \int_{-\pi}^{\pi} f(x-t) D_{N}(t) d t
> $$
>
> where $D_{N}$ is the $N$ th Dirichlet kernel (1).
````

## 2. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!lemma|d7caace1-7b20-5412-a6f8-6a5d5120b657.local at=682e5486-4d10-51dd-b1a9-927ce7c67216] Piecewise Linear Correction of Jumps in a Periodic Function
> Let $f$ be a $2\pi$-periodic piecewise continuous function. There is a $2\pi$-periodic piecewise linear function $h$, with finitely many discontinuities per period, such that $g=f-h$ is continuous and $2\pi$-periodic. Values of $h$ at the breakpoints are chosen so that $g$ agrees with its common one-sided limit there.
````
### After

````text
> [!lemma|d7caace1-7b20-5412-a6f8-6a5d5120b657.local at=682e5486-4d10-51dd-b1a9-927ce7c67216] Linear Correction
> Suppose that $f$ is a $2 \pi$-periodic piecewise continuous function. Then there is a piecewise linear function $h(x)$ with finitely many discontinuities in $[-\pi, \pi]$, such that the function $g(x)=f(x)-h(x)$ is $2 \pi$-periodic and continuous for all $x$.
````

## 3. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!lemma|8e01686a-b9d7-5239-b8a4-402a244e3fe4.local at=db89ab9f-715b-5293-ae60-2c13fde748c5] Riemann–Lebesgue Decay for Fourier Integrals with Shifted Integer Frequencies
> Suppose that $f$ is a $2 \pi$-periodic piecewise continuous function. Then
> $\lim _{n \rightarrow \infty} \int_{-\pi}^{\pi} f(x) \cos n x d x=0$ and $\lim _{n \rightarrow \infty} \int_{-\pi}^{\pi} f(x) \sin n x d x=0$.
>
> More generally, if $\alpha$ is any fixed real number, then
> $$
> \lim _{n \rightarrow \infty} \int_{-\pi}^{\pi} f(x) \cos [(n+\alpha) x] d x=0 \text { and } \lim _{n \rightarrow \infty} \int_{-\pi}^{\pi} f(x) \sin [(n+\alpha) x] d x=0
> $$
````
### After

````text
> [!lemma|8e01686a-b9d7-5239-b8a4-402a244e3fe4.local at=db89ab9f-715b-5293-ae60-2c13fde748c5] Riemann–Lebesgue Lemma
> Suppose that $f$ is a $2 \pi$-periodic piecewise continuous function. Then
> $\lim _{n \rightarrow \infty} \int_{-\pi}^{\pi} f(x) \cos n x d x=0$ and $\lim _{n \rightarrow \infty} \int_{-\pi}^{\pi} f(x) \sin n x d x=0$.
>
> More generally, if $\alpha$ is any fixed real number, then
> $$
> \lim _{n \rightarrow \infty} \int_{-\pi}^{\pi} f(x) \cos [(n+\alpha) x] d x=0 \text { and } \lim _{n \rightarrow \infty} \int_{-\pi}^{\pi} f(x) \sin [(n+\alpha) x] d x=0
> $$
````
