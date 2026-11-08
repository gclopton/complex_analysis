
# Editorial records

Reading note: 3.2 Complex Integration.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Callout 78: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!equation] Integral of a Complex-Valued Function over a Real Interval
> Let $f=u+iv$ on $[a,b]$, where $u,v$ are real-valued Riemann-integrable functions. Then
>
> $$
> \int_{a}^{b} f(x) d x=\int_{a}^{b}(u(x)+i v(x)) d x=\int_{a}^{b} u(x) d x+i \int_{a}^{b} v(x) d x
> $$
````
### After

````text
> [!equation] Equation
> Let $f=u+iv$ on $[a,b]$, where $u,v$ are real-valued Riemann-integrable functions. Then
>
> $$
> \int_{a}^{b} f(x) d x=\int_{a}^{b}(u(x)+i v(x)) d x=\int_{a}^{b} u(x) d x+i \int_{a}^{b} v(x) d x
> $$
````

## 2. Callout 79: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!equation] Integration of Piecewise Continuous Complex Functions
> Write $f=u+iv$ and choose a partition $a=a_0<a_1<\cdots<a_m=b$ on whose open subintervals $f$ is continuous, with finite one-sided limits at the partition points. Then
>
> $$
> \int_{a}^{b} f(x) d x=\sum_{j=1}^{m} \int_{a_{j-1}}^{a_{j}} u(x) d x+i \sum_{j=1}^{m} \int_{a_{j-1}}^{a_{j}} v(x) d x
> $$
````
### After

````text
> [!equation] Equation
> Write $f=u+iv$ and choose a partition $a=a_0<a_1<\cdots<a_m=b$ on whose open subintervals $f$ is continuous, with finite one-sided limits at the partition points. Then
>
> $$
> \int_{a}^{b} f(x) d x=\sum_{j=1}^{m} \int_{a_{j-1}}^{a_{j}} u(x) d x+i \sum_{j=1}^{m} \int_{a_{j-1}}^{a_{j}} v(x) d x
> $$
````

## 3. Callout 80: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!proposition] Linearity and Interval Additivity of Complex-Valued Riemann Integrals
> For complex constants $\alpha,\beta$ and piecewise continuous complex-valued functions $f,g$ on $[a,b]$,
>
> $$
> \int_a^b(\alpha f(x)+\beta g(x))\,dx=\alpha\int_a^b f(x)\,dx+\beta\int_a^b g(x)\,dx.
> $$
>
> For a piecewise continuous complex-valued function $f$ on $[a,c]$ and $a\le b\le c$,
>
> $$
> \int_a^c f(x)\,dx=\int_a^b f(x)\,dx+\int_b^c f(x)\,dx.
> $$
````
### After

````text
> [!proposition] Riemann Integral of Complex-Valued Functions
> (i) If $\alpha$ and $\beta$ are complex numbers and $f$ and $g$ are piecewise continuous complex-valued functions on $[a,b]$, then
> $\quad \int_{a}^{b}(\alpha f(x)+\beta g(x)) d x=\alpha \int_{a}^{b} f(x) d x+\beta \int_{a}^{b} g(x) d x$.
> (ii) If $f$ is a piecewise continuous complex-valued function on $[a,c]$ and $a \leq b \leq c$, then
> $$
> \int_{a}^{c} f(x) d x=\int_{a}^{b} f(x) d x+\int_{b}^{c} f(x) d x
> $$
````

## 4. Callout 81: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Fundamental Theorem of Calculus for Complex-Valued Functions on a Real Interval
> Suppose that $f$ is a piecewise continuous complex-valued function on the interval $[a, b]$ and let $F$ be a continuous antiderivative of $f$ in $[a, b]$. Then
>
> $$
> \int_{a}^{b} f(x) d x=F(b)-F(a)
> $$
````
### After

````text
> [!theorem] Definite Integral of
> Suppose that $f$ is a piecewise continuous complex-valued function on the interval $[a, b]$ and let $F$ be a continuous antiderivative of $f$ in $[a, b]$. Then
>
> $$
> \int_{a}^{b} f(x) d x=F(b)-F(a)
> $$
````

## 5. Callout 82: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!definition] Complex Contour Integral
> Suppose that $\gamma$ is a path over a closed interval $[a, b]$ and that $f$ is a continuous complex-valued function defined on the graph of $\gamma$. The path or contour integral of $f$ on $\gamma$ is given by
>
> $$
> \int_{\gamma} f(z) d z=\int_{a}^{b} f(\gamma(t)) \gamma^{\prime}(t) d t
> $$
>
> Other notations for the path integral are $\int_{\gamma} f(z) d \gamma$ or simply $\int_{\gamma} f d \gamma$.
````
### After

````text
> [!definition] Path (or Contour) Integrals
> Suppose that $\gamma$ is a path over a closed interval $[a, b]$ and that $f$ is a continuous complex-valued function defined on the graph of $\gamma$. The path or contour integral of $f$ on $\gamma$ is given by
>
> $$
> \int_{\gamma} f(z) d z=\int_{a}^{b} f(\gamma(t)) \gamma^{\prime}(t) d t
> $$
>
> Other notations for the path integral are $\int_{\gamma} f(z) d \gamma$ or simply $\int_{\gamma} f d \gamma$.
````

## 6. Callout 83: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!proposition] Linearity, Orientation Reversal, and Additivity of Contour Integrals
> (i) Suppose that $\gamma(t)$ is a path on $[a, b], f$ and $g$ are continuous functions on $\gamma$, and $\alpha$ and $\beta$ are complex numbers. Then
>
> $$
> \int_{\gamma}(\alpha f(z)+\beta g(z)) d z=\alpha \int_{\gamma} f(z) d z+\beta \int_{\gamma} g(z) d z
> $$
>
> (ii) Let $\gamma_{r}$ denote the reverse of $\gamma$. Then
>
> $$
> \int_{\gamma_{r}} f(z) d z=-\int_{\gamma} f(z) d z
> $$
>
> (iii) If $\Gamma=\left(\gamma_{1}, \gamma_{2}, \ldots, \gamma_{m}\right)$ is a contour and $f$ is continuous on $\Gamma$, then
>
> $$
> \int_{\Gamma} f(z) d z=\sum_{k=1}^{m} \int_{\gamma_{k}} f(z) d z
> $$
````
### After

````text
> [!proposition] Properties of the Path Integral
> (i) Suppose that $\gamma(t)$ is a path on $[a, b], f$ and $g$ are continuous functions on $\gamma$, and $\alpha$ and $\beta$ are complex numbers. Then
>
> $$
> \int_{\gamma}(\alpha f(z)+\beta g(z)) d z=\alpha \int_{\gamma} f(z) d z+\beta \int_{\gamma} g(z) d z
> $$
>
> (ii) Let $\gamma_{r}$ denote the reverse of $\gamma$. Then
>
> $$
> \int_{\gamma_{r}} f(z) d z=-\int_{\gamma} f(z) d z
> $$
>
> (iii) If $\Gamma=\left(\gamma_{1}, \gamma_{2}, \ldots, \gamma_{m}\right)$ is a contour and $f$ is continuous on $\Gamma$, then
>
> $$
> \int_{\Gamma} f(z) d z=\sum_{k=1}^{m} \int_{\gamma_{k}} f(z) d z
> $$
````

## 7. Callout 84: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!proposition] Invariance of Contour Integrals under Orientation-Preserving Reparametrization
> Suppose that $\gamma_{1}(t), a \leq t \leq b$, and $\gamma_{2}(t), c \leq t \leq d$, are equivalent, orientation-preserving parametrizations of the same path $\gamma$ and let $f$ be a continuous function on $\gamma$. Then
>
> $$
> \int_{\gamma_{1}} f(z) d z=\int_{\gamma_{2}} f(z) d z
> $$
````
### After

````text
> [!proposition] Independence of Parametrization
> Suppose that $\gamma_{1}(t), a \leq t \leq b$, and $\gamma_{2}(t), c \leq t \leq d$, are equivalent parametrizations of the same path $\gamma$ and let $f$ be a continuous function on $\gamma$. Then
>
> $$
> \int_{\gamma_{1}} f(z) d z=\int_{\gamma_{2}} f(z) d z
> $$
````

## 8. Callout 85: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!equation] Arc Length of a Complex Path
> For a continuous piecewise smooth path $\gamma(t)=x(t)+iy(t)$, $a\le t\le b$, its length is
>
> $$
> l(\gamma)=\int_{a}^{b} \sqrt{x^{\prime}(t)^{2}+y^{\prime}(t)^{2}} d t=\int_{a}^{b}\left|\gamma^{\prime}(t)\right| d t
> $$
````
### After

````text
> [!equation] Equation
> For a continuous piecewise smooth path $\gamma(t)=x(t)+iy(t)$, $a\le t\le b$, its length is
>
> $$
> l(\gamma)=\int_{a}^{b} \sqrt{x^{\prime}(t)^{2}+y^{\prime}(t)^{2}} d t=\int_{a}^{b}\left|\gamma^{\prime}(t)\right| d t
> $$
````

## 9. Callout 86: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] ML Bound for a Complex Contour Integral
> Suppose that $\gamma$ is a path over $[a, b]$ with length $l(\gamma)$, and $f$ is a continuous function on $\gamma$ such that $|f(z)| \leq M$ for all $z$ on $\gamma$. Then
>
> $$
> \left|\int_{\gamma} f(z) d z\right| \leq M l(\gamma) .
> $$
````
### After

````text
> [!theorem] Bounds for Path Integrals
> Suppose that $\gamma$ is a path over $[a, b]$ with length $l(\gamma)$, and $f$ is a continuous function on $\gamma$ such that $|f(z)| \leq M$ for all $z$ on $\gamma$. Then
>
> $$
> \left|\int_{\gamma} f(z) d z\right| \leq M l(\gamma) .
> $$
````

## 10. Callout 87: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!equation] Integral Triangle Inequality and ML Bound for a Complex Path
> Let $\gamma:[a,b]\to\mathbb{C}$ be a continuous piecewise smooth path of length $l(\gamma)$, and let $f$ be continuous on its image with $|f(z)|\le M$ there. Then
>
> $$
> \left|\int_{\gamma} f(z) d z\right| \leq \int_{a}^{b}|f(\gamma(t))|\left|\gamma^{\prime}(t)\right| d t \leq M l(\gamma)
> $$
````
### After

````text
> [!equation] Equation
> Let $\gamma:[a,b]\to\mathbb{C}$ be a continuous piecewise smooth path of length $l(\gamma)$, and let $f$ be continuous on its image with $|f(z)|\le M$ there. Then
>
> $$
> \left|\int_{\gamma} f(z) d z\right| \leq \int_{a}^{b}|f(\gamma(t))|\left|\gamma^{\prime}(t)\right| d t \leq M l(\gamma)
> $$
````

## 11. Callout 88: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!equation] Integral Triangle Inequality on a Real Interval
> Let $f$ be a piecewise continuous complex-valued function on $[a,b]$ with $|f(t)|\le M$. Then
>
> $$
> \left|\int_{a}^{b} f(t) d t\right| \leq \int_{a}^{b}|f(t)| d t \leq M(b-a)
> $$
````
### After

````text
> [!equation] Equation
> Let $f$ be a piecewise continuous complex-valued function on $[a,b]$ with $|f(t)|\le M$. Then
>
> $$
> \left|\int_{a}^{b} f(t) d t\right| \leq \int_{a}^{b}|f(t)| d t \leq M(b-a)
> $$
````

## 12. Callout 89: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!equation] Orthogonality Integral for Integer Complex Exponentials
> For $k\in\mathbb{Z}$,
>
> $$
> \int_{-\pi}^{\pi} e^{ik u}\,du=
> \begin{cases}
> 0, & \text{if } k\neq 0,\\[4pt]
> 2\pi, & \text{if } k=0,
> \end{cases}
> $$
````
### After

````text
> [!equation] Equation
> For $k\in\mathbb{Z}$,
>
> $$
> \int_{-\pi}^{\pi} e^{ik u}\,du=
> \begin{cases}
> 0, & \text{if } k\neq 0,\\[4pt]
> 2\pi, & \text{if } k=0,
> \end{cases}
> $$
````

## 13. Callout 90: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!equation] Orthogonality and Squared Norms of Integer Sines and Cosines
> Let $m,n$ be nonnegative integers. Then
>
> $$
> \int_{-\pi}^{\pi} \cos(mu)\cos(nu)\,du=0
> \qquad (m\neq n),
> $$
> $$
> \int_{-\pi}^{\pi} \cos(mu)\sin(nu)\,du=0
> \qquad \text{for all } m,n,
> $$
> $$
> \int_{-\pi}^{\pi} \sin(mu)\sin(nu)\,du=0
> \qquad (m\neq n),
> $$
> $$
> \int_{-\pi}^{\pi} \cos^2(mu)\,du=\int_{-\pi}^{\pi} \sin^2(mu)\,du=\pi
> \qquad (m\neq 0).
> $$
````
### After

````text
> [!equation] Equation
> Let $m,n$ be nonnegative integers. Then
>
> $$
> \int_{-\pi}^{\pi} \cos(mu)\cos(nu)\,du=0
> \qquad (m\neq n),
> $$
> $$
> \int_{-\pi}^{\pi} \cos(mu)\sin(nu)\,du=0
> \qquad \text{for all } m,n,
> $$
> $$
> \int_{-\pi}^{\pi} \sin(mu)\sin(nu)\,du=0
> \qquad (m\neq n),
> $$
> $$
> \int_{-\pi}^{\pi} \cos^2(mu)\,du=\int_{-\pi}^{\pi} \sin^2(mu)\,du=\pi
> \qquad (m\neq 0).
> $$
````

## 14. Callout 91: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!equation] Conjugate Integral along the Segment from 1 to i
> The contour $[1,i]$ is the straight line segment oriented from $1$ to $i$.
>
> $$
> \int_{[1,i]} \bar z\,dz=i.
> $$
````
### After

````text
> [!equation] Equation
> The contour $[1,i]$ is the straight line segment oriented from $1$ to $i$.
>
> $$
> \int_{[1,i]} \bar z\,dz=i.
> $$
````

## 15. Callout 92: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!equation] Integral of an Integer Power around a Positively Oriented Circle
> Let $n\in\mathbb{Z}$, $R>0$, and let $C_R(z_0)$ be the circle $|z-z_0|=R$ traversed once counterclockwise. Then
>
> $$
> \int_{C_R(z_0)} (z-z_0)^n\,dz=
> \begin{cases}
> 0, & \text{if } n\neq -1,\\[4pt]
> 2\pi i, & \text{if } n=-1.
> \end{cases}
> $$
````
### After

````text
> [!equation] Equation
> Let $n\in\mathbb{Z}$, $R>0$, and let $C_R(z_0)$ be the circle $|z-z_0|=R$ traversed once counterclockwise. Then
>
> $$
> \int_{C_R(z_0)} (z-z_0)^n\,dz=
> \begin{cases}
> 0, & \text{if } n\neq -1,\\[4pt]
> 2\pi i, & \text{if } n=-1.
> \end{cases}
> $$
````

## 16. Callout 93: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!equation] ML Bound for a Complex Contour Integral
> Let $\gamma:[a,b]\to\mathbb{C}$ be a continuous piecewise smooth path of length $l(\gamma)$, and let $f$ be continuous on its image with $|f(z)|\le M$ there. Then
>
> $$
> \left|\int_\gamma f(z)\,dz\right|\le Ml(\gamma),
> $$
````
### After

````text
> [!equation] Equation
> Let $\gamma:[a,b]\to\mathbb{C}$ be a continuous piecewise smooth path of length $l(\gamma)$, and let $f$ be continuous on its image with $|f(z)|\le M$ there. Then
>
> $$
> \left|\int_\gamma f(z)\,dz\right|\le Ml(\gamma),
> $$
````

## 17. Callout 94: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!equation] Reversing the Orientation of a Complex Contour Integral
> Let $f$ be continuous along a continuous piecewise smooth contour $\gamma$, and let $-\gamma$ denote the same contour with the opposite orientation. Then
>
> $$
> \int_{-\gamma} f(z)\,dz=-\int_\gamma f(z)\,dz.
> $$
````
### After

````text
> [!equation] Equation
> Let $f$ be continuous along a continuous piecewise smooth contour $\gamma$, and let $-\gamma$ denote the same contour with the opposite orientation. Then
>
> $$
> \int_{-\gamma} f(z)\,dz=-\int_\gamma f(z)\,dz.
> $$
````

## 18. Callout 95: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!equation] Additivity of a Riemann Integral over Adjacent Intervals
> For a real- or complex-valued Riemann-integrable function $h$ on $[a,c]$,
>
> $$
> \int_a^c h(t)\,dt=\int_a^b h(t)\,dt+\int_b^c h(t)\,dt
> \qquad (a\le b\le c).
> $$
````
### After

````text
> [!equation] Equation
> For a real- or complex-valued Riemann-integrable function $h$ on $[a,c]$,
>
> $$
> \int_a^c h(t)\,dt=\int_a^b h(t)\,dt+\int_b^c h(t)\,dt
> \qquad (a\le b\le c).
> $$
````

## 19. Move editorial commentary out of the reading note.

### Before

````text
*Editorial note: Restored corrupted OCR coefficients, interval endpoints, and upper integration limit.*
````
### After

````text

````
