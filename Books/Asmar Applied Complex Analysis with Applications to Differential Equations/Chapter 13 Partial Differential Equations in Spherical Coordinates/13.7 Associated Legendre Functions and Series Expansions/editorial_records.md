
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

## Source-to-current comparison

Source: /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 13 Partial Differential Equations in Spherical Coordinates/13.7 Associated Legendre Functions and Series Expansions.md

This exact comparison preserves the full change evidence, including formatting, OCR corrections, restored source wording, and required standalone context. The entries above explain the recovery edits. The comparison is not a claim that every difference is a correction; component serialization, callout wrapping, and printed labels outside callouts are formatting.

`````diff
--- /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 13 Partial Differential Equations in Spherical Coordinates/13.7 Associated Legendre Functions and Series Expansions.md
+++ /Users/gradyclopton/ObsidianVaults/complex_analysis/Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 13 Partial Differential Equations in Spherical Coordinates/13.7 Associated Legendre Functions and Series Expansions.md
@@ -1,16 +1,22 @@
+
 ### 13.7 Associated Legendre Functions and Series Expansions
 
 Like Legendre polynomials, the associated Legendre functions arise from the solutions of important problems involving Laplace's equation in spherical coordinates. You should keep in mind the major concepts that you encountered with the Legendre polynomials to guide you through the topics of this section.
 
 ## Rodrigues' Formula
 
-For each $m=0,1,2, \ldots$, we define a family of functions, called the associated Legendre functions of order $m$, by the formula
-
-$$
-P_{n}^{m}(x)=(-1)^{m}\left(1-x^{2}\right)^{m / 2} \frac{d^{m} P_{n}(x)}{d x^{m}}
-$$
-
-where $P_{n}(x)$ is the Legendre polynomial of degree $n$ (see Section 13.5). Following the usual convention that the derivative of order 0 of a function is the function itself, we see that
+> [!definition|e9be7f8c-6b27-5520-8b51-89b4ef5bb0a1.local at=d9a40629-4938-5adb-a3cb-945f71ab068c] Associated Legendre functions of integer degree and nonnegative order
+> For each $m=0,1,2, \ldots$, we define a family of functions, called the associated Legendre functions of order $m$, by the formula
+>
+> $$
+> P_{n}^{m}(x)=(-1)^{m}\left(1-x^{2}\right)^{m / 2} \frac{d^{m} P_{n}(x)}{d x^{m}}
+> $$
+>
+> where $P_{n}(x)$ is the Legendre polynomial of degree $n\ge m$, normalized by $P_n(1)=1$.
+
+*Printed equation label: (1).*
+
+Following the usual convention that the derivative of order 0 of a function is the function itself, we see that
 
 $$
 P_{n}^{0}(x)=P_{n}(x)
@@ -18,17 +24,37 @@
 
 Thus the associated Legendre functions are generalizations of the Legendre polynomials. For this reason, whatever property we derive concerning the associated Legendre functions, it should reduce to a property of the Legendre polynomials when you take $m=0$.
 
-Since $P_{n}(x)$ is a polynomial of degree $n$, we see from (1) that, in order to get nonzero functions, we must take $0 \leq m \leq n$. For the applications, we extend the definition of the associated Legendre functions to negative $m$ 's by setting
-
-$$
-P_{n}^{m}(x)=(-1)^{m} \frac{(n+m)!}{(n-m)!} P_{n}^{-m}(x) .
-$$
+Since $P_{n}(x)$ is a polynomial of degree $n$, we see from (1) that, in order to get nonzero functions, we must take $0 \leq m \leq n$.
+
+> [!convention|219dd4b7-1248-54fb-9a76-50bb1fa8d7c2.local at=0de7a522-0a76-5af5-bd79-6b53cbc83052] Negative-order associated Legendre functions with the Condon–Shortley phase
+> For the applications, we extend the definition of the associated Legendre functions to negative integer orders $-n\le m<0$ by setting
+>
+> $$
+> P_{n}^{m}(x)=(-1)^{m} \frac{(n+m)!}{(n-m)!} P_{n}^{-m}(x) .
+> $$
+>
+> Here $P_n^m$ are the associated Legendre functions defined by $P_n^m(x)=(-1)^m(1-x^2)^{m/2}d^mP_n(x)/dx^m$ for $0\le m\le n$, with $P_n(1)=1$; negative orders satisfy $P_n^{-m}=(-1)^m(n-m)!P_n^m/(n+m)!$.
+
+*Printed equation label: (2).*
 
 Note that for negative $m$ 's, $P_{n}^{m}(x)$ is simply a scalar multiple of $P_{n}^{-m}(x)$. So, for each $n=0,1,2, \ldots$, we have $2 n+1$ associated Legendre functions $P_{n}^{m}(x)$, where $m$ runs from $-n$ to $n$.
 
-## EXAMPLE 1 Associated Legendre functions
-
-Using (1) and (2) with $m=-2,-1,0,1,2$, respectively, we get
+> [!exercise|62439e3d-2e1b-5eb6-93f5-2003a4234a8a.local at=31321d92-87fc-58d7-864e-970aeb52b11c] EXAMPLE 1 Associated Legendre functions
+> Compute the following associated Legendre functions using the definitions for positive and negative order:
+>
+> (a) $P_n^0$ for $n=0,1,2,3$.
+>
+> (b) $P_n^1$ for $n=1,2,3,4$.
+>
+> (c) $P_n^2$ for $n=2,3,4,5$.
+>
+> (d) $P_n^{-1}$ for $n=1,2,3,4$.
+>
+> (e) $P_n^{-2}$ for $n=2,3,4,5$.
+
+##### solution
+
+Using the definitions for the indicated orders, we get
 (a) $P_{0}^{0}(x)=1=P_{0}(x)$,
 $P_{1}^{0}(x)=x=P_{1}(x)$,
 $P_{2}^{0}(x)=\frac{3 x^{2}-1}{2}=P_{2}(x)$,
@@ -50,10 +76,21 @@
 $P_{4}^{-2}(x)=\frac{\left(7 x^{2}-1\right)}{48}\left(1-x^{2}\right)$,
 $P_{5}^{-2}(x)=\frac{\left(3 x^{3}-x\right)}{16}\left(1-x^{2}\right)$.
 
-Figure 1 Associated Legendre functions.
-![](./images/122e2a0e-ba5b-4934-9af1-dcd4ea360903-52_394_617_1548_553.jpg)
-
-![](./images/122e2a0e-ba5b-4934-9af1-dcd4ea360903-52_401_576_1555_1181.jpg)
+```scientific-figure
+id: 9c3825d8-3ccf-44ed-89c6-4196bf7a44f2
+numbered: false
+title: ""
+caption: Figure 1 Associated Legendre functions.
+captionVisible: true
+captionPosition: below
+columns: 2
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 13 Partial Differential Equations in Spherical Coordinates/images/122e2a0e-ba5b-4934-9af1-dcd4ea360903-52_394_617_1548_553.jpg
+    caption: ""
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 13 Partial Differential Equations in Spherical Coordinates/images/122e2a0e-ba5b-4934-9af1-dcd4ea360903-52_401_576_1555_1181.jpg
+    caption: ""
+```
+
 
 It is clear from (1) that if $m$ is odd and nonzero, $P_{n}^{m}$ is not a polynomial, because of the factor $\left(1-x^{2}\right)^{m / 2}$. Also, as illustrated by Figure 1, $P_{n}^{m}$ is even if $n+m$ is even and it is odd if $n+m$ is odd.
 
@@ -61,22 +98,27 @@
 
 We know from Section 13.5 that the Legendre polynomials satisfy the (Legendre) differential equation $\left(1-x^{2}\right) y^{\prime \prime}-2 x y^{\prime}+n(n+1) y=0$. We now establish a similar result for the associated Legendre functions.
 
-For $n=0,1,2, \ldots$ and $m=0, \pm 1, \pm 2, \ldots, \pm n$, the associated Legendre differential equation is given by
-
-$$
-\left(1-x^{2}\right) y^{\prime \prime}-2 x y^{\prime}+\left(n(n+1)-\frac{m^{2}}{1-x^{2}}\right) y=0, \quad-1<x<1
-$$
-
-When $m=0$, the equation reduces to Legendre's differential ((1), Section 13.5), and so it is satisfied by the Legendre polynomials $P_{n}=P_{n}^{0}$. Thus in showing that the associated Legendre functions are solutions of (3), it suffices to consider the case $m \neq 0$. Moreover, since for negative $m, P_{n}^{m}$ is proportional to $P_{n}^{-m}$ (see (2)), it suffices to consider $m>0$. Let us start with Legendre's equation, which is satisfied by the $n$th Legendre polynomial $P_{n}$. Using the Leibniz rule to differentiate this equation $m$ times with respect to $x$ and then plugging $P_{n}$ for $y$, we arrive at
+> [!equation|319b9013-8b17-5eb7-8f78-3c37630e1bbe.local at=25be9b09-5c3c-542d-9b79-be7c91c589ac] Associated Legendre differential equation for integer degree and order
+> For $n=0,1,2, \ldots$ and $m=0, \pm 1, \pm 2, \ldots, \pm n$, the associated Legendre differential equation is given by
+>
+> $$
+> \left(1-x^{2}\right) y^{\prime \prime}-2 x y^{\prime}+\left(n(n+1)-\frac{m^{2}}{1-x^{2}}\right) y=0, \quad-1<x<1
+> $$
+
+*Printed equation label: (3).*
+
+When $m=0$, the equation reduces to Legendre's differential equation ((1), Section 13.5), and so it is satisfied by the Legendre polynomials $P_{n}=P_{n}^{0}$. Thus in showing that the associated Legendre functions are solutions of (3), it suffices to consider the case $m \neq 0$. Moreover, since for negative $m, P_{n}^{m}$ is proportional to $P_{n}^{-m}$ (see (2)), it suffices to consider $m>0$. Let us start with Legendre's equation, which is satisfied by the $n$th Legendre polynomial $P_{n}$. Using the Leibniz rule to differentiate this equation $m$ times with respect to $x$ and then plugging $P_{n}$ for $y$, we arrive at
 
 $$
 \left(1-x^{2}\right) P_{n}^{(m+2)}-2(m+1) x P_{n}^{(m+1)}+(n-m)(n+m+1) P_{n}^{(m)}=0
+\tag{4}
 $$
 
 (Exercise 14). Thus the function $P_{n}^{(m)}$ satisfies the differential equation
 
 $$
 \left(1-x^{2}\right) y^{\prime \prime}-2(m+1) x y^{\prime}+(n-m)(n+m+1) y=0
+\tag{5}
 $$
 
 Now you can verify that this equation reduces to (3) if we use the substitution
@@ -91,133 +133,236 @@
 
 Like Legendre polynomials, the associated Legendre functions enjoy orthogonality relations on the interval $[-1,1]$. The proofs are very much like the ones for Legendre polynomials. They will be outlined in the exercises.
 
-## THEOREM 1 ORTHOGONALITY OF ASSOCIATED LEGENDRE FUNCTIONS
-
-Let $k \leq n$ be nonnegative integers and let $m$ be an integer such $|m| \leq k$. Then
-
-$$
-\int_{-1}^{1} P_{k}^{m}(x) P_{n}^{m}(x) d x=0, \quad k \neq n
-$$
-
-and
-
-$$
-\int_{-1}^{1}\left[P_{n}^{m}(x)\right]^{2} d x=\frac{2}{2 n+1} \frac{(n+m)!}{(n-m)!}, \quad|m| \leq n
-$$
-
-## THEOREM 2 ASSOCIATED LEGENDRE SERIES EXPANSIONS
-
-![](./images/122e2a0e-ba5b-4934-9af1-dcd4ea360903-54_369_465_1585_59.jpg)
-Figure 2 Partial sum of the associated Legendre series $\sum_{n=2}^{\infty} A_{n} P_{n}^{2}(x)$.
+> [!theorem|46143ca3-2007-5076-af3f-e74922744345.local at=afd136f1-6507-5601-9dfd-278ca930709b] Orthogonality of Associated Legendre Functions
+> Let $k \leq n$ be nonnegative integers and let $m$ be an integer such that $|m| \leq k$. Then
+>
+> $$
+> \int_{-1}^{1} P_{k}^{m}(x) P_{n}^{m}(x) d x=0, \quad k \neq n
+> $$
+>
+> and
+>
+> $$
+> \int_{-1}^{1}\left[P_{n}^{m}(x)\right]^{2} d x=\frac{2}{2 n+1} \frac{(n+m)!}{(n-m)!}, \quad|m| \leq n
+> $$
+>
+> Here $P_n^m$ are the associated Legendre functions defined by $P_n^m(x)=(-1)^m(1-x^2)^{m/2}d^mP_n(x)/dx^m$ for $0\le m\le n$, with $P_n(1)=1$; negative orders satisfy $P_n^{-m}=(-1)^m(n-m)!P_n^m/(n+m)!$.
+
+*Printed equation labels: (6) orthogonality of distinct degrees; (7) squared norm.*
 
 We next state a very useful series expansion theorem for associated Legendre functions. You should check that it reduces to Theorem 2, Section 13.6, when $m=0$.
 
-Fix a nonnegative integer $m$. Suppose that $f(x)$ is piecewise smooth on $[-1,1]$. Then we have the associated Legendre series expansion of order $m$
-
-$$
-f(x)=\sum_{n=m}^{\infty} A_{n} P_{n}^{m}(x)
-$$
-
-where the associated Legendre coefficient $A_{n}$ is given by
-(9) $A_{n}=\frac{2 n+1}{2} \frac{(n-m)!}{(n+m)!} \int_{-1}^{1} f(x) P_{n}^{m}(x) d x, \quad n=m, m+1, m+2, \ldots$.
-
-For $x$ in the open interval $(-1,1)$, the series converges to $f(x)$ if $f$ is continuous at $x$, and to $(f(x+)+f(x-)) / 2$ otherwise.
+> [!theorem|02e0ff4e-38c8-58ec-85b4-8ec243ddc266.local at=95d4c4f4-1f58-5179-b769-a7ad14f862d9] Associated Legendre Series Expansions
+> Fix a nonnegative integer $m$. Suppose that $f(x)$ is piecewise smooth on $[-1,1]$. Then we have the associated Legendre series expansion of order $m$
+>
+> $$
+> f(x)=\sum_{n=m}^{\infty} A_{n} P_{n}^{m}(x)
+> $$
+>
+> where the associated Legendre coefficient $A_{n}$ is given by
+> $A_{n}=\frac{2 n+1}{2} \frac{(n-m)!}{(n+m)!} \int_{-1}^{1} f(x) P_{n}^{m}(x) d x, \quad n=m, m+1, m+2, \ldots$.
+>
+> For $x$ in the open interval $(-1,1)$, the series converges to $f(x)$ if $f$ is continuous at $x$, and to $(f(x+)+f(x-)) / 2$ otherwise.
+>
+> Here $P_n^m$ are the associated Legendre functions defined by $P_n^m(x)=(-1)^m(1-x^2)^{m/2}d^mP_n(x)/dx^m$ for $0\le m\le n$, with $P_n(1)=1$; negative orders satisfy $P_n^{-m}=(-1)^m(n-m)!P_n^m/(n+m)!$.
+
+*Printed equation labels: (8) associated Legendre expansion at continuity points; (9) associated Legendre coefficients.*
 
 The proof of Theorem 2 is beyond the level of this text and will be omitted. You can test the validity of the result by considering concrete applications. In the following example, we have computed the associated Legendre series expansion of a simple function, when $m=2$. We have used a computer to carry out the computation of the associated Legendre coefficients and plot some partial sums of the associated Legendre series. As you can imagine, the explicit expressions of these series are very complicated.
 
-EXAMPLE 2 An associated Legendre series expansion of order $m=2$
-Consider the function
-
-$$
-f(x)= \begin{cases}0 & \text { if }-1<x<0 \\ 1 & \text { if } 0<x<1\end{cases}
-$$
-
-We will illustrate its associated Legendre series expansion of order $m=2$. For this purpose, we will compute the coefficients $A_{n}$ for $n=2,3,4, \ldots, 10$ (note that $n \geq m$ ). Then using these coefficients, we will form and plot a partial sum of the associated Legendre series with $n$ up to 10 . With the help of a computer, the coefficients are found to be as shown in Table 1.
-
-| $n$ | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
-| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
-| $A_{n}$ | $\frac{5}{24}$ | $\frac{7}{64}$ | $\frac{1}{40}$ | 0 | $\frac{13}{1680}$ | $\frac{65}{6144}$ | $\frac{17}{5040}$ | $-\frac{19}{30720}$ | $\frac{7}{3960}$ |
-
-Table 1 Associated Legendre coefficients
+> [!exercise|44e75ead-ae72-5970-af5d-75f3934ad28e.local at=0f2682e8-fff0-5f45-8b42-014cfd5b9485] EXAMPLE 2 An associated Legendre series expansion of order $m=2$
+> Consider the function
+>
+> $$
+> f(x)= \begin{cases}0 & \text { if }-1<x<0 \\ 1 & \text { if } 0<x<1\end{cases}
+> $$
+>
+> Illustrate its associated Legendre series expansion of order $m=2$. Compute the coefficients $A_{n}$ for $n=2,3,4, \ldots, 10$ (note that $n \geq m$ ). Then using these coefficients, form and plot a partial sum of the associated Legendre series with $n$ up to 10 .
+
+##### solution
+
+With the help of a computer, the coefficients are found to be as shown in Table 1.
+
+```scientific-table
+id: 5bfcddc2-8eac-4ad8-9bf1-3349b22707fa
+numbered: false
+title: ""
+caption: Table 1 Associated Legendre coefficients
+captionVisible: true
+captionPosition: below
+rows:
+  - - text: $n$
+    - text: "2"
+    - text: "3"
+    - text: "4"
+    - text: "5"
+    - text: "6"
+    - text: "7"
+    - text: "8"
+    - text: "9"
+    - text: "10"
+  - - text: $A_{n}$
+    - text: $\frac{5}{24}$
+    - text: $\frac{7}{64}$
+    - text: $\frac{1}{40}$
+    - text: "0"
+    - text: $\frac{13}{1680}$
+    - text: $\frac{65}{6144}$
+    - text: $\frac{17}{5040}$
+    - text: $-\frac{19}{30720}$
+    - text: $\frac{7}{3960}$
+headerRows: 1
+rowHeaders: true
+style: scientific
+```
+
+
+```scientific-figure
+id: 9d5d7e31-4d22-4dc8-8c0e-5dd363233cb6
+numbered: false
+title: ""
+caption: Figure 2 Partial sum of the associated Legendre series $\sum_{n=2}^{\infty} A_{n} P_{n}^{2}(x)$.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 13 Partial Differential Equations in Spherical Coordinates/images/122e2a0e-ba5b-4934-9af1-dcd4ea360903-54_369_465_1585_59.jpg
+    caption: ""
+```
+
 
 The graphs of $f$ and a partial sum of the associated Legendre series (with $n$ up to 10) are shown in Figure 2. Note that the associated Legendre coefficients tend to
 zero as $n$ increases. Also note the overshoot of the partial sum of the associated Legendre series near the points of discontinuity. As you would expect, both of these facts are true for general associated Legendre series.
 
-## Exercises 5.7
-
-In Exercises 1-4, use (1) and (2) to derive $P_{n}^{m}$ for the given $m$ and $n$.
-
-1. $m= \pm 1, n=2$.
-2. $m=1, n=1,2,3$.
-3. $m=3, n=4$.
-4. $m=-3, n=4$.
-
-In Exercises 5-8, (a) determine $m$ and $n$ for the given associated Legendre differential equation. (b) Use the list of Legendre functions in Example 1 to find one solution. (c) Verify your answer in (b) by plugging back into the differential equation.
-5. $\left(1-x^{2}\right) y^{\prime \prime}-2 x y^{\prime}+\left(2-\frac{1}{1-x^{2}}\right) y=0$.
-6. $\left(1-x^{2}\right) y^{\prime \prime}-2 x y^{\prime}+\left(6-\frac{4}{1-x^{2}}\right) y=0$.
-7. $\left(1-x^{2}\right) y^{\prime \prime}-2 x y^{\prime}+\left(6-\frac{1}{1-x^{2}}\right) y=0$.
-8. $\left(1-x^{2}\right) y^{\prime \prime}-2 x y^{\prime}+\left(12-\frac{4}{1-x^{2}}\right) y=0$.
-9. Verify (6) and (7) with $m=1$, and $n=1,2$.
-
-In Exercises 10-15, you are given an order $m$ and a function $f(x)$ defined on the interval $[-1,1]$. (a) Use a computer system with built-in associated Legendre functions to compute the associated Legendre coefficients of $f(x)$ of order $m$. Take $n=m, m+1, \ldots, m+10$. (b) Use the coefficients in (a) to construct several partial sums of the associated Legendre series expansion of order $m$. Plot these partial sums along with the given function to illustrate Theorem 2.
-10. $m=1, f(x)=\sin \pi x$.
-11. $m=1, f(x)=(x-1)(x+1)$.
-12. $m=2, f(x)=x$.
-13. $m=2, f(x)=|x|$.
-14. (a) Prove (4) using the Leibnitz rule for differentiation.
-(b) With the help of a computer system, verify that the substitution $y=(1- \left.x^{2}\right)^{-m / 2} v$ transforms (5) into (3).
-15. Prove (6) by following the steps of the proof of Theorem 1, (i), Section 13.6. [Hint: Show that (3) can be put in the form
-
-$$
-\left.\left(\left(1-x^{2}\right) y^{\prime}\right)^{\prime}+\left(n(n+1)-\frac{m^{2}}{1-x^{2}}\right) y=0 .\right]
-$$
-
-16. Project Problem: Proof of (7).
-(a) Use (1) to show that
-
-$$
-P_{n}^{m+1}=-\left(1-x^{2}\right)^{1 / 2} \frac{d P_{n}^{m}}{d x}-m\left(1-x^{2}\right)^{-1 / 2} x P_{n}^{m}
-$$
-
-(b) Square both sides of (a) and integrate to get
-
-$$
-\begin{aligned}
-\int_{-1}^{1}\left[P_{n}^{m+1}(x)\right]^{2} d x= & \int_{-1}^{1}\left(1-x^{2}\right)\left[\frac{d P_{n}^{m}}{d x}\right]^{2} d x+2 m \int_{-1}^{1} x P_{n}^{m}(x) \frac{d P_{n}^{m}}{d x} d x \\
-& +\int_{-1}^{1} \frac{m^{2} x^{2}}{1-x^{2}}\left[P_{n}^{m}(x)\right]^{2} d x
-\end{aligned}
-$$
-
-(c) Show that $\left[m x\left[P_{n}^{m}(x)\right]^{2}\right]_{-1}^{1}=0$.
-(d) Use integration by parts to show that the right side of the equation in (b) is equal to
-
-$$
-\begin{array}{r}
--\int_{-1}^{1} P_{n}^{m}(x) \frac{d}{d x}\left[\left(1-x^{2}\right) \frac{d P_{n}^{m}}{d x}\right] d x-m \int_{-1}^{1}\left[P_{n}^{m}(x)\right]^{2} d x \\
-+\int_{-1}^{1} \frac{m^{2} x^{2}}{1-x^{2}}\left[P_{n}^{m}(x)\right]^{2} d x
-\end{array}
-$$
-
-(e) Explain why
-
-$$
-\frac{d}{d x}\left[\left(1-x^{2}\right) \frac{d P_{n}^{m}}{d x}\right]=-\left[n(n+1)-\frac{m^{2}}{1-x^{2}}\right] P_{n}^{m}(x)
-$$
-
-[Hint: See the hint for Exercise 15.]
-(f) Combine (d)-(e) to get
-
-$$
-\int_{-1}^{1}\left[P_{n}^{m+1}(x)\right]^{2} d x=(n-m)(n+m+1) \int_{-1}^{1}\left[P_{n}^{m}(x)\right]^{2} d x
-$$
-
-(g) Use (f) to get
-
-$$
-\begin{aligned}
-& \int_{-1}^{1}\left[P_{n}^{m}(x)\right]^{2} d x \\
-& \quad=(n-m+1)(n-m+2) \ldots n(n+m)(n+m-1) \ldots(n+1) \int_{-1}^{1}\left[P_{n}(x)\right]^{2} d x
-\end{aligned}
-$$
-
-(h) Use (g) and Theorem 1 (ii), Section 13.6, to get (7).
+## Exercises 13.7
+
+
+> [!prompt|2493fe2f-71d9-51de-b692-c78d436acb2b.local at=69eae938-0c83-5e73-b9d0-13d8eded9130] Shared exercise instructions
+> In Exercises 1-4, use (1) and (2) to derive $P_{n}^{m}$ for the given $m$ and $n$.
+
+
+> [!exercise|da00bf37-eaf0-5b71-9f97-b3b8ca3f8097.local at=fa7b5680-92e8-5680-b06d-b864fb7f320d] Exercise 1
+> $m= \pm 1, n=2$.
+
+
+> [!exercise|a2da4368-470b-54db-8fc0-00fbceb41112.local at=55cc21b4-13a5-5bfc-bce5-3c9d959d2de3] Exercise 2
+> $m=1, n=1,2,3$.
+
+
+> [!exercise|5837b494-e017-5446-8573-29262ce7040b.local at=af919475-969e-581d-ad46-8b9ba8a05086] Exercise 3
+> $m=3, n=4$.
+
+
+> [!exercise|6acd5534-710c-5a91-8225-d133e15fab1c.local at=f37accb3-31bb-5b26-9fe5-eae62d4c296e] Exercise 4
+> $m=-3, n=4$.
+
+
+> [!prompt|a25d8ca9-df15-5e2f-aeb3-a983f3dd0187.local at=1249e209-bd57-5b10-8bfb-2ccec9fa895d] Shared exercise instructions
+> In Exercises 5-8, (a) determine $m$ and $n$ for the given associated Legendre differential equation. (b) Use the list of Legendre functions in Example 1 to find one solution. (c) Verify your answer in (b) by plugging back into the differential equation.
+
+
+> [!exercise|31115825-59ca-5555-957d-bf52056008d4.local at=227e8113-db72-5e47-8e35-383701d8af5b] Exercise 5
+> $\left(1-x^{2}\right) y^{\prime \prime}-2 x y^{\prime}+\left(2-\frac{1}{1-x^{2}}\right) y=0$.
+
+
+> [!exercise|cea360bc-caa0-56f2-91e3-ffc8fb004c9a.local at=27106cb6-5902-5c76-a8fa-0456ad800987] Exercise 6
+> $\left(1-x^{2}\right) y^{\prime \prime}-2 x y^{\prime}+\left(6-\frac{4}{1-x^{2}}\right) y=0$.
+
+
+> [!exercise|cac2e845-ddd0-50a4-9393-642c42cf16fb.local at=2419bf2d-a93c-523d-8f2c-7f5d0f1c1073] Exercise 7
+> $\left(1-x^{2}\right) y^{\prime \prime}-2 x y^{\prime}+\left(6-\frac{1}{1-x^{2}}\right) y=0$.
+
+
+> [!exercise|70ce6f64-4ea5-55ff-9943-0543fcfeb549.local at=bdfca68e-ffc7-5700-9f78-05901ca8b466] Exercise 8
+> $\left(1-x^{2}\right) y^{\prime \prime}-2 x y^{\prime}+\left(12-\frac{4}{1-x^{2}}\right) y=0$.
+
+
+> [!exercise|9123cd60-536b-5cae-bf90-e9d20069a0e6.local at=8eb9e53a-dfb5-525a-89f6-eda866a90f87] Exercise 9
+> Verify (6) and (7) with $m=1$, and $n=1,2$.
+
+
+> [!prompt|fec2cee7-03cc-5c20-aa68-ee4ac9454b2d.local at=f8378cfd-85be-5017-80b9-3a72a0512cdc] Shared exercise instructions
+> In Exercises 10-13, you are given an order $m$ and a function $f(x)$ defined on the interval $[-1,1]$. (a) Use a computer system with built-in associated Legendre functions to compute the associated Legendre coefficients of $f(x)$ of order $m$. Take $n=m, m+1, \ldots, m+10$. (b) Use the coefficients in (a) to construct several partial sums of the associated Legendre series expansion of order $m$. Plot these partial sums along with the given function to illustrate Theorem 2.
+
+
+> [!exercise|ccd7ee93-4d35-5d8f-ac4b-3f9428892f55.local at=b2eba898-d5ca-5686-b6b6-df03eb83e5ae] Exercise 10
+> $m=1, f(x)=\sin \pi x$.
+
+
+> [!exercise|d6b6f4da-56b4-5e3b-a7ca-05b5438f2969.local at=85af3e9f-e94c-53dc-916d-d7e46386dd01] Exercise 11
+> $m=1, f(x)=(x-1)(x+1)$.
+
+
+> [!exercise|16876f0c-446d-50bd-9803-77a919d9e3a1.local at=21965747-4767-5172-ad7b-e0bf363ff898] Exercise 12
+> $m=2, f(x)=x$.
+
+
+> [!exercise|d14c229c-9b12-59dc-83f4-38fc87e1ce91.local at=cd093b4b-0880-5418-bdd6-efb0357f0fce] Exercise 13
+> $m=2, f(x)=|x|$.
+
+
+> [!exercise|d07134a6-49ca-55fe-8ce8-ece616044f7b.local at=6248a94f-0e82-53c4-942d-7bfd5adf641d] Exercise 14
+> (a) Prove (4) using the Leibniz rule for differentiation.
+> (b) With the help of a computer system, verify that the substitution $y=(1-x^2)^{-m/2}v$ transforms (5) into (3).
+
+
+> [!exercise|45efd5cb-c23f-53f6-8265-6a5bbec7ddfc.local at=e0558229-8f0b-5ffd-8d76-305ef1a9254d] Exercise 15
+> Prove (6) by following the steps of the proof of Theorem 1, (i), Section 13.6. [Hint: Show that (3) can be put in the form
+>
+> $$
+> \left(\left(1-x^{2}\right) y^{\prime}\right)^{\prime}+\left(n(n+1)-\frac{m^{2}}{1-x^{2}}\right) y=0.
+> $$
+>
+> ]
+
+
+> [!exercise|b1564a98-72aa-520a-bc0d-950fdb7204d8.local at=38029046-4ae0-5a3e-9587-f7330d7d4058] Exercise 16
+> Project Problem: Proof of the squared-norm formula. First take integers $0\le m\le n$; after part (h), extend the result to negative orders using their definition.
+> (a) Use (1) to show that
+>
+> $$
+> P_{n}^{m+1}=-\left(1-x^{2}\right)^{1 / 2} \frac{d P_{n}^{m}}{d x}-m\left(1-x^{2}\right)^{-1 / 2} x P_{n}^{m}
+> $$
+>
+> (b) Square both sides of (a) and integrate to get
+>
+> $$
+> \begin{aligned}
+> \int_{-1}^{1}\left[P_{n}^{m+1}(x)\right]^{2} d x= & \int_{-1}^{1}\left(1-x^{2}\right)\left[\frac{d P_{n}^{m}}{d x}\right]^{2} d x+2 m \int_{-1}^{1} x P_{n}^{m}(x) \frac{d P_{n}^{m}}{d x} d x \\
+> & +\int_{-1}^{1} \frac{m^{2} x^{2}}{1-x^{2}}\left[P_{n}^{m}(x)\right]^{2} d x
+> \end{aligned}
+> $$
+>
+> (c) Show that $\left[m x\left[P_{n}^{m}(x)\right]^{2}\right]_{-1}^{1}=0$.
+> (d) Use integration by parts to show that the right side of the equation in (b) is equal to
+>
+> $$
+> \begin{array}{r}
+> -\int_{-1}^{1} P_{n}^{m}(x) \frac{d}{d x}\left[\left(1-x^{2}\right) \frac{d P_{n}^{m}}{d x}\right] d x-m \int_{-1}^{1}\left[P_{n}^{m}(x)\right]^{2} d x \\
+> +\int_{-1}^{1} \frac{m^{2} x^{2}}{1-x^{2}}\left[P_{n}^{m}(x)\right]^{2} d x
+> \end{array}
+> $$
+>
+> (e) Explain why
+>
+> $$
+> \frac{d}{d x}\left[\left(1-x^{2}\right) \frac{d P_{n}^{m}}{d x}\right]=-\left[n(n+1)-\frac{m^{2}}{1-x^{2}}\right] P_{n}^{m}(x)
+> $$
+>
+> [Hint: See the hint for Exercise 15.]
+> (f) Combine (d)-(e) to get
+>
+> $$
+> \int_{-1}^{1}\left[P_{n}^{m+1}(x)\right]^{2} d x=(n-m)(n+m+1) \int_{-1}^{1}\left[P_{n}^{m}(x)\right]^{2} d x
+> $$
+>
+> (g) Use (f) to get
+>
+> $$
+> \begin{aligned}
+> & \int_{-1}^{1}\left[P_{n}^{m}(x)\right]^{2} d x \\
+> & \quad=(n-m+1)(n-m+2) \ldots n(n+m)(n+m-1) \ldots(n+1) \int_{-1}^{1}\left[P_{n}(x)\right]^{2} d x
+> \end{aligned}
+> $$
+>
+> (h) Use (g) and Theorem 1 (ii), Section 13.6, to get (7).

`````
