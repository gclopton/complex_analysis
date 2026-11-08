
# Editorial records

Reading note: 13.5 Legendre's Differential Equation.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!definition|e429f6d7-0540-5e28-9e61-221696326ae9.local at=41c415fa-9568-515f-b55a-fd8b0d556215] Legendre polynomial with the normalization at one
> For a nonnegative integer $n$, the Legendre polynomial $P_n$ is the degree-$n$ polynomial solution of
> $$
> (1-x^2)y''-2xy'+n(n+1)y=0
> $$
> normalized by $P_n(1)=1$. Equivalently, its leading coefficient is $(2n)!/[2^n(n!)^2]$, and
> $$
> P_n(x)=\frac1{2^n}\sum_{m=0}^{\lfloor n/2\rfloor}(-1)^m\frac{(2n-2m)!}{m!(n-m)!(n-2m)!}x^{n-2m}.
> $$
````
### After

````text
> [!definition|e429f6d7-0540-5e28-9e61-221696326ae9.local at=41c415fa-9568-515f-b55a-fd8b0d556215] Legendre polynomial with the normalization at one
> For a nonnegative integer $n$, the polynomial solution of $(1-x^2)y^{\prime\prime}-2xy^{\prime}+n(n+1)y=0$, normalized by $P_n(1)=1$, is called the Legendre polynomial of degree $n$ and is denoted by $P_{n}(x)$. Setting $M=n / 2$ if $n$ is even or $(n-1) / 2$ if $n$ is odd, the $n$th Legendre polynomial becomes
>
> $$
> P_{n}(x)=\frac{1}{2^{n}} \sum_{m=0}^{M}(-1)^{m} \frac{(2 n-2 m)!}{m!(n-m)!(n-2 m)!} x^{n-2 m} .
> $$
````

## 2. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!equation|b18296d0-620e-5825-a4de-838c8ec5f642.local at=ab1df737-5909-567a-863a-e8af3166a93f] General solution of Legendre’s equation of integer degree
> For a fixed integer $n\ge0$, the general solution of
> $$
> (1-x^2)y''-2xy'+n(n+1)y=0,\qquad -1<x<1,
> $$
> is
> $$
> y(x)=c_1P_n(x)+c_2Q_n(x),
> $$
> where $P_n$ is the Legendre polynomial normalized by $P_n(1)=1$, $Q_n$ is the real Legendre function of the second kind on $(-1,1)$, and $c_1,c_2$ are arbitrary constants. The function $P_n$ is bounded at both endpoints, whereas $Q_n$ is unbounded there.
````
### After

````text
> [!equation|b18296d0-620e-5825-a4de-838c8ec5f642.local at=ab1df737-5909-567a-863a-e8af3166a93f] General solution of Legendre’s equation of integer degree
> Hence the general solution of Legendre's equation $(1-x^2)y^{\prime\prime}-2xy^{\prime}+n(n+1)y=0$ of order $n\ge0$ on $-1<x<1$ is
>
> $$
> y(x)=c_{1} P_{n}(x)+c_{2} Q_{n}(x)
> $$
>
> where $c_{1}$ and $c_{2}$ are arbitrary constants.
>
> Here $P_n$ is the Legendre polynomial normalized by $P_n(1)=1$. The function $Q_n$ is the Legendre function of the second kind.
````

## 3. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!property|82caf074-b664-5cfc-ae3f-b233b751fd0d.local at=0a04882c-d6f2-52b0-93ba-d9f678235427] Parity, endpoint values, bounds and zeros of Legendre polynomials
> For integers $n\ge0$, let $P_n$ be the Legendre polynomial normalized by $P_n(1)=1$. Then
> $$
> P_n(-x)=(-1)^nP_n(x),\qquad P_n(-1)=(-1)^n,
> $$
> and $|P_n(x)|\le1$ for $-1\le x\le1$. For $n\ge1$, $P_n$ has exactly $n$ distinct zeros in $(-1,1)$, and all its relative extrema lie in $[-1,1]$. The constant polynomial $P_0=1$ is excluded from the extrema-location assertion.
````
### After

````text
> [!property|82caf074-b664-5cfc-ae3f-b233b751fd0d.local at=0a04882c-d6f2-52b0-93ba-d9f678235427] Further Properties of Legendre Polynomials
> $P_{n}$ is even if $n$ is even and odd if $n$ is odd. $P_{n}(1)=1$ and $P_{n}(-1)=(-1)^{n}$ for all $n$.
> $\left|P_{n}(x)\right| \leq 1$ for all $n$ and all $x$ in $[-1,1]$. $P_{n}(x)$ has $n$ distinct zeros in $[-1,1]$. For $n\ge1$, all relative maxima and minima of $P_{n}$ occur in $[-1,1]$.
>
> Here $P_n$ is the Legendre polynomial normalized by $P_n(1)=1$.
````

## 4. Restore source wording; retain only the actual correction.

### Before

````text
The conventional gravitational potential is the negative of this function.
````
### After

````text

````

## 5. Restore source wording; retain only the actual correction.

### Before

````text
[Numbering corrected: the source repeats Exercise 31.]
````
### After

````text

````

## 6. Restore source wording; retain only the actual correction.

### Before

````text
with radii of convergence at least 1 (the zero function $q$ when $\mu=0$ has infinite radius)
````
### After

````text
with radii of convergence at least 1
````
