
# Editorial records

Reading note: 12.9 Integral Formulas and Asymptotics for Bessel Functions.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem] Integral representation of integer-order Bessel functions of the first kind
> For every integer $n$ and every real $x$, the Bessel function $J_n$ of the first kind satisfies
> $$
> J_n(x)=\frac1\pi\int_0^\pi\cos(n\theta-x\sin\theta)\,d\theta.
> $$
````
### After

````text
> [!theorem] Integral Representation
> Here $J_n$ is the Bessel function of the first kind.
>
> Let $n=0, \pm 1, \pm 2, \ldots$. Then for all real $x$, we have
>
> $$
> J_{n}(x)=\frac{1}{\pi} \int_{0}^{\pi} \cos (n \theta-x \sin \theta) d \theta
> $$
````

## 2. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem] Jacobi–Anger Fourier expansion of a sinusoidal complex exponential
> For real $x$ and $\theta$,
> $$
> e^{ix\sin\theta}=\sum_{n=-\infty}^{\infty}J_n(x)e^{in\theta},
> $$
> where $J_n$ denotes the Bessel function of the first kind of integer order $n$. For each fixed $x$, the series converges absolutely and uniformly in $\theta$.
````
### After

````text
> [!theorem] Fourier Series Generating Bessel Functions
> Here $J_n$ is the Bessel function of the first kind.
>
> For all real $x$ and all real $\theta$, we have
>
> $$
> e^{i x \sin \theta}=\sum_{n=-\infty}^{\infty} J_{n}(x) e^{i n \theta}
> $$
````

## 3. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem] Large-argument asymptotic expansion of integer-order Bessel functions
> For each fixed nonnegative integer $n$, as $x\to+\infty$,
> $$
> J_n(x)=\sqrt{\frac2{\pi x}}\cos\left(x-\frac\pi4-\frac{n\pi}2\right)+O(x^{-3/2}),
> $$
> where $J_n$ is the Bessel function of the first kind. Thus a constant $C_n$ bounds the absolute error by $C_nx^{-3/2}$ for all sufficiently large positive $x$. The error is additive; no ratio limit is asserted at the zeros of the oscillatory leading term.
````
### After

````text
> [!theorem] Asymptotic Formula
> Here $J_n$ is the Bessel function of the first kind, and $x\to+\infty$.
>
> Let $n \geq 0$ be an integer. Then for all large $x$, we have
>
> $$
> J_{n}(x) = \sqrt{\frac{2}{\pi x}} \cos \left(x-\frac{\pi}{4}-\frac{n \pi}{2}\right)+\mathcal{O}\left(\frac{1}{x^{3 / 2}}\right)
> $$
>
> where the big oh notation means that the approximation is of the order $\frac{1}{x^{3 / 2}}$.
````

## 4. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!lemma] Stationary-phase approximation at a single nondegenerate interior critical point
> Let $a<b$, and let $f$ be real-valued and smooth on $[a,b]$, with a Taylor expansion near $t_0\in(a,b)$. Suppose $f'(t_0)=0$, $f''(t_0)\ne0$, and $f'(t)\ne0$ for $t\ne t_0$ in $[a,b]$. Let $g$ be a smooth complex-valued function on $[a,b]$. As $x\to+\infty$,
> $$
> \int_a^b e^{ixf(t)}g(t)\,dt=
> \sqrt{\frac{2\pi}{x}}\,\frac{g(t_0)}{\sqrt{|f''(t_0)|}}
>  e^{i\left(xf(t_0)+\frac\pi4\operatorname{sgn}f''(t_0)\right)}+O(x^{-1}).
> $$
> The phase shift is $+\pi/4$ when $f''(t_0)>0$ and $-\pi/4$ when $f''(t_0)<0$. If $g(t_0)\ne0$, the displayed leading term is an asymptotic equivalent. If $g(t_0)=0$, further terms and endpoint contributions must be examined to obtain the first nonzero approximation.
````
### After

````text
> [!lemma] Method of Stationary Phase
> Suppose that $f(t)$ is a smooth real-valued function on $[a,b]$ with a Taylor series centered at $t_0$ in the open interval $(a,b)$, such that $f^{\prime}\left(t_{0}\right)=0, f^{\prime}(t) \neq 0$ for all $t \neq t_{0}$, and $f^{\prime \prime}\left(t_{0}\right) \neq 0$. Let $g(t)$ be an arbitrary smooth complex-valued function on $[a,b]$ with $g(t_0)\ne0$. Then for large positive $x$
> $$
> \int_{a}^{b} e^{i x f(t)} g(t) d t \sim \sqrt{\frac{2 \pi}{x}} g\left(t_{0}\right) \frac{e^{i\left(x f\left(t_{0}\right) \pm \frac{\pi}{4}\right)}}{\sqrt{\left|f^{\prime \prime}\left(t_{0}\right)\right|}}
> $$
>
> where we use the plus sign if $f^{\prime \prime}\left(t_{0}\right)>0$ and the minus sign if $f^{\prime \prime}\left(t_{0}\right)<0$.
````

## 5. Move correction/commentary into the separate editorial record; keep the actual correction in the reading text.

### Before

````text
[Corrected: the printed statement omits the restriction to even $n$; the claim is false in general for odd $n$.]
````
### After

````text

````

## 6. Move correction/commentary into the separate editorial record; keep the actual correction in the reading text.

### Before

````text
[Corrected: the sine series starts at $n=0$; the printed lower limit omits its first term.]
````
### After

````text

````
