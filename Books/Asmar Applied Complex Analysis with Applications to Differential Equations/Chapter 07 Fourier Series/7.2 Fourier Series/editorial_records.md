
# Editorial records

Reading note: 7.2 Fourier Series.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Callout 255: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!equation|e35fe69d-eabe-5bfb-bbd4-c2908be0901d.local at=090841af-4f87-5e1c-8852-9e8cfddea8d4] Real Fourier Coefficients on the Symmetric Period Interval
> The Fourier coefficients of an integrable $2\pi$-periodic function $f$ are given by
>
> $$
> a_0=\frac{1}{2 \pi} \int_{-\pi}^\pi f(x) d x,
> $$
>
> $$
> a_n=\frac{1}{\pi} \int_{-\pi}^\pi f(x) \cos n x d x \quad(n=1,2, \ldots),
> $$
>
> $$
> b_n=\frac{1}{\pi} \int_{-\pi}^\pi f(x) \sin n x d x \quad(n=1,2, \ldots)
> $$
````
### After

````text
> [!equation|e35fe69d-eabe-5bfb-bbd4-c2908be0901d.local at=090841af-4f87-5e1c-8852-9e8cfddea8d4] Euler Formulas for the Fourier Coefficients
> The Fourier coefficients of an integrable $2\pi$-periodic function $f$ are given by
>
> $$
> a_0=\frac{1}{2 \pi} \int_{-\pi}^\pi f(x) d x,
> $$
>
> $$
> a_n=\frac{1}{\pi} \int_{-\pi}^\pi f(x) \cos n x d x \quad(n=1,2, \ldots),
> $$
>
> $$
> b_n=\frac{1}{\pi} \int_{-\pi}^\pi f(x) \sin n x d x \quad(n=1,2, \ldots)
> $$
````

## 2. Callout 257: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!equation|74d94a23-240c-50f8-b220-622990d197fb.local at=976188cb-e75d-5df7-8eb5-700c2d19fc99] Real Fourier Coefficients on a Full Positive Period Interval
> For an integrable $2\pi$-periodic function $f$, with constant coefficient $a_0$ rather than $a_0/2$ in the Fourier series,
>
> $$
> a_0=\frac{1}{2 \pi} \int_0^{2 \pi} f(x) d x
> $$
>
> $$
> a_n=\frac{1}{\pi} \int_0^{2 \pi} f(x) \cos n x d x, \text { and } b_n=\frac{1}{\pi} \int_0^{2 \pi} f(x) \sin n x d x, n \geq 1 .
> $$
````
### After

````text
> [!equation|74d94a23-240c-50f8-b220-622990d197fb.local at=976188cb-e75d-5df7-8eb5-700c2d19fc99] Alternative Euler Formulas
> For an integrable $2\pi$-periodic function $f$, with constant coefficient $a_0$ rather than $a_0/2$ in the Fourier series,
>
> $$
> a_0=\frac{1}{2 \pi} \int_0^{2 \pi} f(x) d x
> $$
>
> $$
> a_n=\frac{1}{\pi} \int_0^{2 \pi} f(x) \cos n x d x, \text { and } b_n=\frac{1}{\pi} \int_0^{2 \pi} f(x) \sin n x d x, n \geq 1 .
> $$
````

## 3. Callout 258: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem|8bc02eb9-f2cf-5e29-981e-5e93fbe73ad9.local at=ee1bf1be-a960-5b42-bd43-24305539e2d7] Pointwise Convergence of a Piecewise Smooth Fourier Series
> Write $f(x+)$ and $f(x-)$ for the right and left limits.
>
> Suppose that $f$ is a $2 \pi$-periodic piecewise smooth function. Then for all $x$ we have
>
> $$
> \frac{f(x+)+f(x-)}{2}=a_0+\sum_{n=1}^{\infty}\left(a_n \cos n x+b_n \sin n x\right),
> $$
>
> where the Fourier coefficients are $a_0=(2\pi)^{-1}\int_{-\pi}^{\pi}f(t)\,dt$, $a_n=\pi^{-1}\int_{-\pi}^{\pi}f(t)\cos(nt)\,dt$, and $b_n=\pi^{-1}\int_{-\pi}^{\pi}f(t)\sin(nt)\,dt$ for $n\geq1$. In particular, if $f$ is piecewise smooth and continuous at $x$, then
>
> $$
> f(x)=a_0+\sum_{n=1}^{\infty}\left(a_n \cos n x+b_n \sin n x\right)
> $$
````
### After

````text
> [!theorem|8bc02eb9-f2cf-5e29-981e-5e93fbe73ad9.local at=ee1bf1be-a960-5b42-bd43-24305539e2d7] Fourier Series Representation
> Write $f(x+)$ and $f(x-)$ for the right and left limits.
>
> Suppose that $f$ is a $2 \pi$-periodic piecewise smooth function. Then for all $x$ we have
>
> $$
> \frac{f(x+)+f(x-)}{2}=a_0+\sum_{n=1}^{\infty}\left(a_n \cos n x+b_n \sin n x\right),
> $$
>
> where the Fourier coefficients are $a_0=(2\pi)^{-1}\int_{-\pi}^{\pi}f(t)\,dt$, $a_n=\pi^{-1}\int_{-\pi}^{\pi}f(t)\cos(nt)\,dt$, and $b_n=\pi^{-1}\int_{-\pi}^{\pi}f(t)\sin(nt)\,dt$ for $n\geq1$. In particular, if $f$ is piecewise smooth and continuous at $x$, then
>
> $$
> f(x)=a_0+\sum_{n=1}^{\infty}\left(a_n \cos n x+b_n \sin n x\right)
> $$
````

## 4. Callout 259: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!corollary|4b2b0a41-0cc6-5959-8abd-036e2a16f028.local at=c916d5c4-f347-539c-b9ca-bf8238ffd65c] Uniqueness of Piecewise Smooth Fourier Series Representations
> Suppose that $f$ and $g$ are $2 \pi$-periodic piecewise smooth functions. If $f$ and $g$ have the same Fourier coefficients, then $f(x)=g(x)$ for all $x$, except possibly at the points where $f$ or $g$ are discontinuous. Consequently, if $f$ and $g$ are continuous and have the same Fourier coefficients, then they are equal everywhere.
````
### After

````text
> [!corollary|4b2b0a41-0cc6-5959-8abd-036e2a16f028.local at=c916d5c4-f347-539c-b9ca-bf8238ffd65c] Uniqueness of Fourier Series Representation
> Suppose that $f$ and $g$ are $2 \pi$-periodic piecewise smooth functions. If $f$ and $g$ have the same Fourier coefficients, then $f(x)=g(x)$ for all $x$, except possibly at the points where $f$ or $g$ are discontinuous. Consequently, if $f$ and $g$ are continuous and have the same Fourier coefficients, then they are equal everywhere.
````

## 5. Callout 260: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem|5c662c09-67e6-5224-afad-068e094a800e.local at=d8453e12-9618-5b91-9a78-b048346d5e32] Uniform Convergence of Fourier Series of Piecewise Smooth Functions
> The coefficient convention is $a_0=(2\pi)^{-1}\int_{-\pi}^{\pi}f(t)\,dt$, $a_n=\pi^{-1}\int_{-\pi}^{\pi}f(t)\cos(nt)\,dt$, and $b_n=\pi^{-1}\int_{-\pi}^{\pi}f(t)\sin(nt)\,dt$ for $n\geq1$.
>
> Suppose that $f$ is a $2 \pi$-periodic piecewise smooth function. Then the Fourier series of $f$ converges uniformly for all $x$ to $f(x)$ if and only if $f$ is continuous for all $x$. Thus, if $f$ is continuous and piecewise smooth, then
>
> $$
> f(x)=a_0+\sum_{n=1}^{\infty}\left(a_n \cos n x+b_n \sin n x\right),
> $$
>
> where the Fourier series converges uniformly for all $x$.
````
### After

````text
> [!theorem|5c662c09-67e6-5224-afad-068e094a800e.local at=d8453e12-9618-5b91-9a78-b048346d5e32] Uniform Convergence of Fourier Series
> The coefficient convention is $a_0=(2\pi)^{-1}\int_{-\pi}^{\pi}f(t)\,dt$, $a_n=\pi^{-1}\int_{-\pi}^{\pi}f(t)\cos(nt)\,dt$, and $b_n=\pi^{-1}\int_{-\pi}^{\pi}f(t)\sin(nt)\,dt$ for $n\geq1$.
>
> Suppose that $f$ is a $2 \pi$-periodic piecewise smooth function. Then the Fourier series of $f$ converges uniformly for all $x$ to $f(x)$ if and only if $f$ is continuous for all $x$. Thus, if $f$ is continuous and piecewise smooth, then
>
> $$
> f(x)=a_0+\sum_{n=1}^{\infty}\left(a_n \cos n x+b_n \sin n x\right),
> $$
>
> where the Fourier series converges uniformly for all $x$.
````

## 6. Move editorial commentary out of the reading note.

### Before

````text
*Editorial corrections to source details: The coefficient-decay comparison uses absolute values. In Exercise 16, the requested illustration $c=d=\pi/2$ is the limiting case $c+d=\pi$, rather than a case satisfying the printed strict inequality.*
````
### After

````text

````
