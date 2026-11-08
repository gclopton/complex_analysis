
# Editorial records

Reading note: 13.7 Associated Legendre Functions and Series Expansions.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!definition|e9be7f8c-6b27-5520-8b51-89b4ef5bb0a1.local at=d9a40629-4938-5adb-a3cb-945f71ab068c] Associated Legendre functions of integer degree and nonnegative order
> Let $n\ge0$ and $0\le m\le n$ be integers, and let $P_n$ be the Legendre polynomial with $P_n(1)=1$. On $-1<x<1$, define
> $$
> P_n^m(x)=(-1)^m(1-x^2)^{m/2}\frac{d^mP_n(x)}{dx^m}.
> $$
> The factor $(-1)^m$ specifies the Condon–Shortley phase convention. Values at $x=\pm1$ are defined by continuous extension. The degree is $n$ and the order is $m$.
````
### After

````text
> [!definition|e9be7f8c-6b27-5520-8b51-89b4ef5bb0a1.local at=d9a40629-4938-5adb-a3cb-945f71ab068c] Associated Legendre functions of integer degree and nonnegative order
> For each $m=0,1,2, \ldots$, we define a family of functions, called the associated Legendre functions of order $m$, by the formula
>
> $$
> P_{n}^{m}(x)=(-1)^{m}\left(1-x^{2}\right)^{m / 2} \frac{d^{m} P_{n}(x)}{d x^{m}}
> $$
>
> where $P_{n}(x)$ is the Legendre polynomial of degree $n\ge m$, normalized by $P_n(1)=1$.
````

## 2. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!convention|219dd4b7-1248-54fb-9a76-50bb1fa8d7c2.local at=0de7a522-0a76-5af5-bd79-6b53cbc83052] Negative-order associated Legendre functions with the Condon–Shortley phase
> For integers $n\ge0$ and $1\le m\le n$, extend the associated Legendre functions by
> $$
> P_n^{-m}(x)=(-1)^m\frac{(n-m)!}{(n+m)!}P_n^m(x),\qquad -1\le x\le1,
> $$
> where positive orders use $P_n^m(x)=(-1)^m(1-x^2)^{m/2}d^mP_n(x)/dx^m$ and $P_n(1)=1$.
````
### After

````text
> [!convention|219dd4b7-1248-54fb-9a76-50bb1fa8d7c2.local at=0de7a522-0a76-5af5-bd79-6b53cbc83052] Negative-order associated Legendre functions with the Condon–Shortley phase
> For the applications, we extend the definition of the associated Legendre functions to negative integer orders $-n\le m<0$ by setting
>
> $$
> P_{n}^{m}(x)=(-1)^{m} \frac{(n+m)!}{(n-m)!} P_{n}^{-m}(x) .
> $$
>
> Here $P_n^m$ are the associated Legendre functions defined by $P_n^m(x)=(-1)^m(1-x^2)^{m/2}d^mP_n(x)/dx^m$ for $0\le m\le n$, with $P_n(1)=1$; negative orders satisfy $P_n^{-m}=(-1)^m(n-m)!P_n^m/(n+m)!$.
````

## 3. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!equation|319b9013-8b17-5eb7-8f78-3c37630e1bbe.local at=25be9b09-5c3c-542d-9b79-be7c91c589ac] Associated Legendre differential equation for integer degree and order
> For integers $n\ge0$ and $|m|\le n$, the associated Legendre function $P_n^m$ satisfies
> $$
> (1-x^2)y''-2xy'+\left(n(n+1)-\frac{m^2}{1-x^2}\right)y=0,\qquad -1<x<1.
> $$
> For nonnegative order, $P_n^m=(-1)^m(1-x^2)^{m/2}d^mP_n/dx^m$, where $P_n$ is the Legendre polynomial; negative orders are proportional to the corresponding positive orders.
````
### After

````text
> [!equation|319b9013-8b17-5eb7-8f78-3c37630e1bbe.local at=25be9b09-5c3c-542d-9b79-be7c91c589ac] Associated Legendre differential equation for integer degree and order
> For $n=0,1,2, \ldots$ and $m=0, \pm 1, \pm 2, \ldots, \pm n$, the associated Legendre differential equation is given by
>
> $$
> \left(1-x^{2}\right) y^{\prime \prime}-2 x y^{\prime}+\left(n(n+1)-\frac{m^{2}}{1-x^{2}}\right) y=0, \quad-1<x<1
> $$
````

## 4. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|46143ca3-2007-5076-af3f-e74922744345.local at=afd136f1-6507-5601-9dfd-278ca930709b] Orthogonality and norms of associated Legendre functions at fixed order
> Fix an integer order $m$. For degrees $k,n\ge |m|$, use associated Legendre functions with the Condon–Shortley phase and the negative-order convention $P_n^{-q}=(-1)^q(n-q)!P_n^q/(n+q)!$. Then
> $$
> \int_{-1}^1P_k^m(x)P_n^m(x)\,dx=0\quad(k\ne n),
> $$
> and
> $$
> \int_{-1}^1[P_n^m(x)]^2\,dx=\frac2{2n+1}\frac{(n+m)!}{(n-m)!}.
> $$
> The underlying Legendre polynomials are normalized by $P_n(1)=1$.
````
### After

````text
> [!theorem|46143ca3-2007-5076-af3f-e74922744345.local at=afd136f1-6507-5601-9dfd-278ca930709b] Orthogonality of Associated Legendre Functions
> Let $k \leq n$ be nonnegative integers and let $m$ be an integer such that $|m| \leq k$. Then
>
> $$
> \int_{-1}^{1} P_{k}^{m}(x) P_{n}^{m}(x) d x=0, \quad k \neq n
> $$
>
> and
>
> $$
> \int_{-1}^{1}\left[P_{n}^{m}(x)\right]^{2} d x=\frac{2}{2 n+1} \frac{(n+m)!}{(n-m)!}, \quad|m| \leq n
> $$
>
> Here $P_n^m$ are the associated Legendre functions defined by $P_n^m(x)=(-1)^m(1-x^2)^{m/2}d^mP_n(x)/dx^m$ for $0\le m\le n$, with $P_n(1)=1$; negative orders satisfy $P_n^{-m}=(-1)^m(n-m)!P_n^m/(n+m)!$.
````

## 5. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|02e0ff4e-38c8-58ec-85b4-8ec243ddc266.local at=95d4c4f4-1f58-5179-b769-a7ad14f862d9] Pointwise convergence of an associated Legendre series at fixed nonnegative order
> Fix an integer $m\ge0$. Suppose $f$ is piecewise smooth on $[-1,1]$, with finitely many continuously differentiable pieces and finite one-sided limits of $f$ and $f'$ at their endpoints. Let
> $$
> P_n^m(x)=(-1)^m(1-x^2)^{m/2}\frac{d^mP_n(x)}{dx^m},\qquad n\ge m,
> $$
> where $P_n(1)=1$. Define
> $$
> A_n=\frac{2n+1}{2}\frac{(n-m)!}{(n+m)!}\int_{-1}^1f(t)P_n^m(t)\,dt.
> $$
> Then, for $-1<x<1$,
> $$
> \sum_{n=m}^{\infty}A_nP_n^m(x)=\frac{f(x+)+f(x-)}2.
> $$
> This equals $f(x)$ at continuity points. Endpoint convergence is not asserted.
````
### After

````text
> [!theorem|02e0ff4e-38c8-58ec-85b4-8ec243ddc266.local at=95d4c4f4-1f58-5179-b769-a7ad14f862d9] Associated Legendre Series Expansions
> Fix a nonnegative integer $m$. Suppose that $f(x)$ is piecewise smooth on $[-1,1]$. Then we have the associated Legendre series expansion of order $m$
>
> $$
> f(x)=\sum_{n=m}^{\infty} A_{n} P_{n}^{m}(x)
> $$
>
> where the associated Legendre coefficient $A_{n}$ is given by
> $A_{n}=\frac{2 n+1}{2} \frac{(n-m)!}{(n+m)!} \int_{-1}^{1} f(x) P_{n}^{m}(x) d x, \quad n=m, m+1, m+2, \ldots$.
>
> For $x$ in the open interval $(-1,1)$, the series converges to $f(x)$ if $f$ is continuous at $x$, and to $(f(x+)+f(x-)) / 2$ otherwise.
>
> Here $P_n^m$ are the associated Legendre functions defined by $P_n^m(x)=(-1)^m(1-x^2)^{m/2}d^mP_n(x)/dx^m$ for $0\le m\le n$, with $P_n(1)=1$; negative orders satisfy $P_n^{-m}=(-1)^m(n-m)!P_n^m/(n+m)!$.
````
