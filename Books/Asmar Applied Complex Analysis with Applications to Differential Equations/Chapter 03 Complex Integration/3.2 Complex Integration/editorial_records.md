
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

## Source-to-current comparison

Source: /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 03 Complex Integration/3.2 Complex Integration.md

This exact comparison preserves the full change evidence, including formatting, OCR corrections, restored source wording, and required standalone context. The entries above explain the recovery edits. The comparison is not a claim that every difference is a correction; component serialization, callout wrapping, and printed labels outside callouts are formatting.

`````diff
--- /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 03 Complex Integration/3.2 Complex Integration.md
+++ /Users/gradyclopton/ObsidianVaults/complex_analysis/Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/3.2 Complex Integration.md
@@ -59,7 +59,7 @@
 
 
 
-Our goal in this section is to construct the integral of a complex-valued function along a path in the complex plane. Since our construction is mod-
+Our goal in this section is to construct the integral of a complex-valued function along a path in the complex plane. Since our construction is modeled after the Riemann integral from calculus, we start the section with a quick review of some notions from integral calculus.
 
 
 Suppose that $f$ is a real-valued continuous function defined on $[a, b]$. Let $P$ be a partition of $[a, b]$ consisting of closed subintervals of $[a, b]$ with endpoints $a=x_{0}<x_{1}<x_{2}<\cdots<x_{m}=b$. Let $|P|$ denote the norm of the partition, being the largest of the lengths $\Delta x_{k}=x_{k}-x_{k-1}$. Now consider the Riemann sum corresponding to $P$ (see _Figure 1_):
@@ -69,23 +69,24 @@
 \sum_{k=1}^{m} f\left(x_{k}^{\star}\right)\left(x_{k}-x_{k-1}\right),
 $$
 
-where $x_{k}^{\star}$ is a point in $\left[x_{j-1}, x_{j}\right]$. From calculus, we know that as the partition gets finer, that is, as $|P| \rightarrow 0$, the Riemann sum (1) converges to a finite number called the definite integral of $f$ and denoted by $\int_{a}^{b} f(x) d x$. Also, if $F$ is any antiderivative of $f$, then by the fundamental theorem of calculus sums.
-
-
-
-> [!figure] Figure 1
-> 
-> ```horizontal
-> 
-> ![](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-010_381_525_1716_91.jpg)
-> 
-> ---
-> 
-> ![](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-010_401_521_2095_94.jpg)
-> ```
-> 
-> 
-> Figure 1 The Riemann integral as a limit of Riemann eled after the Riemann integral from calculus, we start the section with a quick review of some notions from integral calculus.
+where $x_{k}^{\star}$ is a point in $\left[x_{k-1}, x_{k}\right]$. From calculus, we know that as the partition gets finer, that is, as $|P| \rightarrow 0$, the Riemann sum (1) converges to a finite number called the definite integral of $f$ and denoted by $\int_{a}^{b} f(x) d x$. Also, if $F$ is any antiderivative of $f$, then by the fundamental theorem of calculus
+
+
+
+```scientific-figure
+id: d597ad63-10c5-4ce9-8577-968190d0c2d8
+numbered: false
+title: ""
+caption: "**Figure 1.** The Riemann integral as a limit of Riemann sums."
+captionVisible: true
+captionPosition: below
+columns: 2
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-010_381_525_1716_91.jpg
+    caption: ""
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-010_401_521_2095_94.jpg
+    caption: ""
+```
 
 
 
@@ -240,7 +241,10 @@
 where $x_{k}^{\star}$ is a point in $\left[x_{k-1}, x_{k}\right]$. Since $u$ and $v$ are continuous, the Riemann sums on the right converge to $\int_{a}^{b} u(x) d x+i \int_{a}^{b} v(x) d x$. This leads us to the following definition of the definite integral in the complex-valued case:
 (4)
 
+<!-- Source label: Equation -->
 > [!equation] Equation
+> Let $f=u+iv$ on $[a,b]$, where $u,v$ are real-valued Riemann-integrable functions. Then
+>
 > $$
 > \int_{a}^{b} f(x) d x=\int_{a}^{b}(u(x)+i v(x)) d x=\int_{a}^{b} u(x) d x+i \int_{a}^{b} v(x) d x
 > $$
@@ -248,20 +252,28 @@
 If $f(x)$ is a piecewise continuous complex-valued function on $[a, b]$, to define its integral over $[a, b]$, we write $[a, b]$ as the finite union of adjacent closed subintervals $\left[a_{0}, a_{1}\right],\left[a_{1}, a_{2}\right], \ldots,\left[a_{m-1}, a_{m}\right]$, with $a_{0}=a$ and $a_{m}=b$, such that $f$ is continuous on each subinterval (see _Figure 2_). Using (4), we define
 
 
+<!-- Source label: Equation -->
 > [!equation] Equation
-> 
+> Write $f=u+iv$ and choose a partition $a=a_0<a_1<\cdots<a_m=b$ on whose open subintervals $f$ is continuous, with finite one-sided limits at the partition points. Then
+>
 > $$
 > \int_{a}^{b} f(x) d x=\sum_{j=1}^{m} \int_{a_{j-1}}^{a_{j}} u(x) d x+i \sum_{j=1}^{m} \int_{a_{j-1}}^{a_{j}} v(x) d x
 > $$
-> 
-
-
-
-> [!figure] Figure 2
-> 
-> ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-011_599_475_1482_27.jpg)
-> Figure 2 We integrate a complex-valued function by integrating its real and imagibary parts separately.
-> 
+
+
+
+```scientific-figure
+id: 83201372-c85a-4b91-a6a1-b4cf9b45536c
+numbered: false
+title: ""
+caption: "**Figure 2.** We integrate a complex-valued function by integrating its real and imagibary parts separately."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-011_599_475_1482_27.jpg
+    caption: ""
+```
 
 
 
@@ -272,20 +284,14 @@
 the following properties, whome prows are left to Exercise 10.
 
 
-> [!proposition] Proposition 1:  Reimann Integral of Complex-Valued Functions
-> (i) If $a$ and 3 are complex mambers and $f$ and $g$ are picewise contintoma complex-saluel functions on $\{a, b\}$, then
-> (6) $\quad \int_{a}^{b}(a f(x)+\beta g(x)) d x=a \int_{a}^{b} f(x) d x+1 \int_{a}^{b} g(x) d x$.
-> (ii) If $f$ is a piecewie continuous complex-valued function on $[a, d]$ and 1 $a \leq b \leq c$, then
-> (7)
-> 
-> $$
-> \int_{a}^{a} f(x) d x=\int_{a}^{b} f(x) d x+\int_{b}^{c} f(x) d x
-> $$
-> 
-> 
-
-
-
+<!-- Source label: Proposition 1:  Reimann Integral of Complex-Valued Functions -->
+> [!proposition] Riemann Integral of Complex-Valued Functions
+> (i) If $\alpha$ and $\beta$ are complex numbers and $f$ and $g$ are piecewise continuous complex-valued functions on $[a,b]$, then
+> $\quad \int_{a}^{b}(\alpha f(x)+\beta g(x)) d x=\alpha \int_{a}^{b} f(x) d x+\beta \int_{a}^{b} g(x) d x$.
+> (ii) If $f$ is a piecewise continuous complex-valued function on $[a,c]$ and $a \leq b \leq c$, then
+> $$
+> \int_{a}^{c} f(x) d x=\int_{a}^{b} f(x) d x+\int_{b}^{c} f(x) d x
+> $$
 
 
 > [!exercise] Exercise 1: A complex-valued piecewise continuous function
@@ -548,11 +554,18 @@
 
 
 
-> [!figure] Figure 3
-> 
-> ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-012_582_522_1580_98.jpg)
-> 
-> Figure 3 An antiderivative of a piecewise continuous function may not be continuous.
+```scientific-figure
+id: f5e1e15f-87ff-48f2-8cc6-8370da8c9010
+numbered: false
+title: ""
+caption: "**Figure 3.** An antiderivative of a piecewise continuous function may not be continuous."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-012_582_522_1580_98.jpg
+    caption: ""
+```
 
 
 Let $f_{j}$ denote the restriction of $f$ to $\left[a_{j-1}, a_{j}\right]$, and let $F_{j}$ denote an antiderivative of $f_{j}$ over $\left[a_{j-1}, a_{j}\right]$. Each $F_{j}$ is computed up to an arbitrary complex constant, which can be determined in such a way to make $F$ continuous.
@@ -561,9 +574,18 @@
 
 
 
-> [!figure] Figure 4
-> ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-013_686_444_356_51.jpg)
-> Figure 4 Selecting a continuous ant derivative.
+```scientific-figure
+id: b62b4b20-6709-4b2d-bb41-8839fde31636
+numbered: false
+title: ""
+caption: "**Figure 4.** Selecting a continuous ant derivative."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-013_686_444_356_51.jpg
+    caption: ""
+```
 
 
 
@@ -650,15 +672,13 @@
 
 The following is an extension of the fundamental theorem of calculus to piecewise continuous complex functions.
 
-> [!theorem] Theorem 1: Definite Integral of
-> 
+<!-- Source label: Theorem 1: Definite Integral of -->
+> [!theorem] Definite Integral of
 > Suppose that $f$ is a piecewise continuous complex-valued function on the interval $[a, b]$ and let $F$ be a continuous antiderivative of $f$ in $[a, b]$. Then
-> 
+>
 > $$
 > \int_{a}^{b} f(x) d x=F(b)-F(a)
 > $$
-> 
-> 
 
 **Proof** Suppose first that $f=u+i v$ is continuous on $[a, b]$. Let $F(x)=U(x)+ i V(x)$ be an antiderivative of $f$. Using (4) and the fundamental theorem of calculus, we sce that
 
@@ -945,17 +965,33 @@
 where $a=t_{0}<t_{1}<\cdots<t_{m}=b$ is a partition of $[a, b]$, and $t_{k}^{\star}$ is in $\left[t_{k-1}, t_{k}\right]$. 
 
 
-> [!figure] Figure 5
-> Figure 5 Partitioning a path - into smaller ares with endpoints at $\gamma\left(t_{k}\right)$.
-> ![](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-015_396_1094_1940_590.jpg)
-> 
-
-
-
-> [!figure] Figure 6
-> 
-> ![](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-016_369_514_193_73.jpg)
-> Figure 6 Forming a Riemann-like sum of a complex-valued function of a path $\gamma$.
+```scientific-figure
+id: 1c302081-f300-4fb9-813c-7bd845daa871
+numbered: false
+title: ""
+caption: "**Figure 5.** Partitioning a path - into smaller ares with endpoints at $\\gamma\\left(t_{k}\\right)$."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-015_396_1094_1940_590.jpg
+    caption: ""
+```
+
+
+
+```scientific-figure
+id: 40efd271-20e0-465b-972c-a34c78066bef
+numbered: false
+title: ""
+caption: "**Figure 6.** Forming a Riemann-like sum of a complex-valued function of a path $\\gamma$."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-016_369_514_193_73.jpg
+    caption: ""
+```
 
 
 
@@ -989,13 +1025,14 @@
 
 
 
-> [!definition] definition 1: Path (or Contour) Integrals
-> Suppose that $\gamma$ is a path over a closed interval $[a, b]$ and that $f$ is a cont inuous complex-valued function defined on the graph of $\gamma$. The path or contour integral of $f$ on $\gamma$ is given by
-> 
+<!-- Source label: definition 1: Path (or Contour) Integrals -->
+> [!definition] Path (or Contour) Integrals
+> Suppose that $\gamma$ is a path over a closed interval $[a, b]$ and that $f$ is a continuous complex-valued function defined on the graph of $\gamma$. The path or contour integral of $f$ on $\gamma$ is given by
+>
 > $$
 > \int_{\gamma} f(z) d z=\int_{a}^{b} f(\gamma(t)) \gamma^{\prime}(t) d t
 > $$
-> 
+>
 > Other notations for the path integral are $\int_{\gamma} f(z) d \gamma$ or simply $\int_{\gamma} f d \gamma$.
 
 
@@ -1010,10 +1047,18 @@
 > Let $C_{R}\left(z_{0}\right)$ be the positively oriented circle with center at $z_{0}$ and radius $R>0$ (see _Figure 7_).
 > 
 > 
-> > [!figure] Figure 7
-> > 
-> > ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-017_511_450_636_43.jpg)
-> > Figure 7 for Example 4.
+> ```scientific-figure
+> id: 818e1dd4-792b-432c-950c-a7a43e9e8c72
+> numbered: false
+> title: ""
+> caption: "**Figure 7.** for Example 4."
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-017_511_450_636_43.jpg
+>     caption: ""
+> ```
 > 
 > 
 > (a) Show that
@@ -1029,7 +1074,9 @@
 > $$
 > 
 > 
-**Solution.** Parametrize the positively oriented circle by
+##### solution
+
+Parametrize the positively oriented circle by
 
 $$
 \gamma(t)=z_0+Re^{it}, \qquad 0\le t\le 2\pi.
@@ -1186,26 +1233,25 @@
 
 
 
-> [!proposition] proposition 2: Properties of the Path Integral
-> 
+<!-- Source label: proposition 2: Properties of the Path Integral -->
+> [!proposition] Properties of the Path Integral
 > (i) Suppose that $\gamma(t)$ is a path on $[a, b], f$ and $g$ are continuous functions on $\gamma$, and $\alpha$ and $\beta$ are complex numbers. Then
-> 
+>
 > $$
 > \int_{\gamma}(\alpha f(z)+\beta g(z)) d z=\alpha \int_{\gamma} f(z) d z+\beta \int_{\gamma} g(z) d z
 > $$
-> 
+>
 > (ii) Let $\gamma_{r}$ denote the reverse of $\gamma$. Then
-> 
+>
 > $$
 > \int_{\gamma_{r}} f(z) d z=-\int_{\gamma} f(z) d z
 > $$
-> 
+>
 > (iii) If $\Gamma=\left(\gamma_{1}, \gamma_{2}, \ldots, \gamma_{m}\right)$ is a contour and $f$ is continuous on $\Gamma$, then
-> 
+>
 > $$
 > \int_{\Gamma} f(z) d z=\sum_{k=1}^{m} \int_{\gamma_{k}} f(z) d z
 > $$
-> 
 
 
 **Proof** (i) Express the path integrals as Riemann integrals using (15) and then use (6). (ii) Recall the parametrization of the reverse of $\gamma$ from (3), Section 3.1: $\gamma_{r}(t)=\gamma(b+a-t)$, where $t$ runs over the same interval $[a, b]$ that parametrizes $\gamma$. Then $\gamma_{r}^{\prime}(t)=-\gamma^{\prime}(b+a-t)$ and so
@@ -1274,10 +1320,18 @@
 > Let $z_{1}=-1, z_{2}=1$, and $z_{3}=i$ (Figure 8). 
 > 
 > 
-> > [!figure] Figure 8
-> > 
-> > ![200](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-019_486_448_1725_40.jpg)
-> > Figure 8 for Example 7.
+> ```scientific-figure
+> id: d19f070e-3852-41bc-be72-84ec17f6eccc
+> numbered: false
+> title: ""
+> caption: "**Figure 8.** for Example 7."
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-019_486_448_1725_40.jpg
+>     caption: ""
+> ```
 > 
 > 
 > Compute
@@ -1617,13 +1671,13 @@
 
 
 
-> [!proposition] Proposition 3: Independence of Parametrization
+<!-- Source label: Proposition 3: Independence of Parametrization -->
+> [!proposition] Independence of Parametrization
 > Suppose that $\gamma_{1}(t), a \leq t \leq b$, and $\gamma_{2}(t), c \leq t \leq d$, are equivalent parametrizations of the same path $\gamma$ and let $f$ be a continuous function on $\gamma$. Then
-> 
+>
 > $$
 > \int_{\gamma_{1}} f(z) d z=\int_{\gamma_{2}} f(z) d z
 > $$
-> 
 
 **Proof** Applying the definition of path integrals, and using $\gamma_{2}(t)=\gamma_{1}(\phi(t))$ and $\gamma_{2}^{\prime}(t)=\gamma_{1}^{\prime}(\phi(t)) \phi^{\prime}(t)$, we obtain
 
@@ -1924,10 +1978,18 @@
 
 
 
-> [!figure] Figure 9
-> 
-> ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-022_520_529_324_76.jpg)
-> Figure 9 Approximating the length of a path by adding the length of line segments.
+```scientific-figure
+id: e2d5e889-4c88-4d4b-ace1-3140d47be3b5
+numbered: false
+title: ""
+caption: "**Figure 9.** Approximating the length of a path by adding the length of line segments."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-022_520_529_324_76.jpg
+    caption: ""
+```
 
 
 
@@ -1940,12 +2002,13 @@
 
 Recognizing this sum as a Riemann sum and taking limits as the partition gets finer, we recover the formula for arc length from calculus:
 
+<!-- Source label: Equation -->
 > [!equation] Equation
-> 
+> For a continuous piecewise smooth path $\gamma(t)=x(t)+iy(t)$, $a\le t\le b$, its length is
+>
 > $$
 > l(\gamma)=\int_{a}^{b} \sqrt{x^{\prime}(t)^{2}+y^{\prime}(t)^{2}} d t=\int_{a}^{b}\left|\gamma^{\prime}(t)\right| d t
 > $$
-> 
 
 where the second equality follows from the complex notation $\gamma^{\prime}(t)=x^{\prime}(t)+ i y^{\prime}(t)$ and so $\sqrt{x^{\prime}(t)^{2}+y^{\prime}(t)^{2}}=\left|\gamma^{\prime}(t)\right|$. For piecewise smooth $\gamma$, we can repeat the previous analysis for each smooth part of $\gamma$ and then add the lengths of all smooth parts. This results in formula (27) for the arc length, where the integrand in this case is piecewise continuous. The element of arc length is usually denoted by $d s$. Thus,
 
@@ -1963,11 +2026,18 @@
 > 
 > where $a$ is a positive real number. The curve is illustrated in _Figure 10_.
 > 
-> > [!figure] Figure 10
-> > 
-> > ![[Screenshot 2026-04-02 at 4.59.04 AM.png]]
-> > 
-> > 
+> ```scientific-figure
+> id: 8aa329f0-9e6b-419e-86e0-19e2f739933a
+> numbered: false
+> title: ""
+> caption: "**Figure 10.**"
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Screenshot 2026-04-02 at 4.59.04 AM.png
+>     caption: ""
+> ```
 > 
 > 
 
@@ -2073,14 +2143,13 @@
 
 
 
-> [!theorem] Theorem 2: Bounds for Path Integrals
+<!-- Source label: Theorem 2: Bounds for Path Integrals -->
+> [!theorem] Bounds for Path Integrals
 > Suppose that $\gamma$ is a path over $[a, b]$ with length $l(\gamma)$, and $f$ is a continuous function on $\gamma$ such that $|f(z)| \leq M$ for all $z$ on $\gamma$. Then
-> (29)
-> 
+>
 > $$
 > \left|\int_{\gamma} f(z) d z\right| \leq M l(\gamma) .
 > $$
-> 
 
 
 
@@ -2119,12 +2188,13 @@
 
 as the partition of $[a, b]$ gets finer. Thus going back to (30) and arguing as we did in the proof of Theorem 2, we obtain the inequalities
 
+<!-- Source label: Equation -->
 > [!equation] Equation
-> 
+> Let $\gamma:[a,b]\to\mathbb{C}$ be a continuous piecewise smooth path of length $l(\gamma)$, and let $f$ be continuous on its image with $|f(z)|\le M$ there. Then
+>
 > $$
 > \left|\int_{\gamma} f(z) d z\right| \leq \int_{a}^{b}|f(\gamma(t))|\left|\gamma^{\prime}(t)\right| d t \leq M l(\gamma)
 > $$
-> 
 
 where $f$ and $\gamma$ are as in Theorem 2.
 
@@ -2227,7 +2297,10 @@
 
 showing that a Riemann integral of a piecewise continuous complex-valued function over $[a, b]$ is a special case of a path integral, where the path is the line segment $[a, b]$. So results about path integrals apply in particular to Riemann integrals. For example, if $f$ is a piecewise continuous complex-valued function on $[a, b]$ such that $|f(t)| \leq M$ for all $t$ in $[a, b]$, then inequalities (31) become
 
+<!-- Source label: Equation -->
 > [!equation] Equation
+> Let $f$ be a piecewise continuous complex-valued function on $[a,b]$ with $|f(t)|\le M$. Then
+>
 > $$
 > \left|\int_{a}^{b} f(t) d t\right| \leq \int_{a}^{b}|f(t)| d t \leq M(b-a)
 > $$
@@ -3288,7 +3361,10 @@
 
 Now use the previously established identity
 
+<!-- Source label: Equation -->
 > [!equation] Equation
+> For $k\in\mathbb{Z}$,
+>
 > $$
 > \int_{-\pi}^{\pi} e^{ik u}\,du=
 > \begin{cases}
@@ -3370,7 +3446,10 @@
 
 Now use the previously established identities on the interval $[-\pi,\pi]$:
 
+<!-- Source label: Equation -->
 > [!equation] Equation
+> Let $m,n$ be nonnegative integers. Then
+>
 > $$
 > \int_{-\pi}^{\pi} \cos(mu)\cos(nu)\,du=0
 > \qquad (m\neq n),
@@ -3890,7 +3969,10 @@
 
 From the earlier computation of the same segment with integrand $\bar z\,dz$, we have
 
+<!-- Source label: Equation -->
 > [!equation] Equation
+> The contour $[1,i]$ is the straight line segment oriented from $1$ to $i$.
+>
 > $$
 > \int_{[1,i]} \bar z\,dz=i.
 > $$
@@ -3993,7 +4075,10 @@
 
 Now use the circle integral formula
 
+<!-- Source label: Equation -->
 > [!equation] Equation
+> Let $n\in\mathbb{Z}$, $R>0$, and let $C_R(z_0)$ be the circle $|z-z_0|=R$ traversed once counterclockwise. Then
+>
 > $$
 > \int_{C_R(z_0)} (z-z_0)^n\,dz=
 > \begin{cases}
@@ -4734,7 +4819,10 @@
 
 In each case we use the ML-inequality
 
+<!-- Source label: Equation -->
 > [!equation] Equation
+> Let $\gamma:[a,b]\to\mathbb{C}$ be a continuous piecewise smooth path of length $l(\gamma)$, and let $f$ be continuous on its image with $|f(z)|\le M$ there. Then
+>
 > $$
 > \left|\int_\gamma f(z)\,dz\right|\le Ml(\gamma),
 > $$
@@ -5165,7 +5253,10 @@
 
 Now use the path-reversal property
 
+<!-- Source label: Equation -->
 > [!equation] Equation
+> Let $f$ be continuous along a continuous piecewise smooth contour $\gamma$, and let $-\gamma$ denote the same contour with the opposite orientation. Then
+>
 > $$
 > \int_{-\gamma} f(z)\,dz=-\int_\gamma f(z)\,dz.
 > $$
@@ -5299,7 +5390,10 @@
 
 Now use additivity of the Riemann integral over adjacent intervals:
 
+<!-- Source label: Equation -->
 > [!equation] Equation
+> For a real- or complex-valued Riemann-integrable function $h$ on $[a,c]$,
+>
 > $$
 > \int_a^c h(t)\,dt=\int_a^b h(t)\,dt+\int_b^c h(t)\,dt
 > \qquad (a\le b\le c).

`````
