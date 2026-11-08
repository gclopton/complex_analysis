
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

## Source-to-current comparison

Source: /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 12 Partial Differential Equations in Polar and Cylindrical Coordinates/12.8 Bessel Series Expansions.md

This exact comparison preserves the full change evidence, including formatting, OCR corrections, restored source wording, and required standalone context. The entries above explain the recovery edits. The comparison is not a claim that every difference is a correction; component serialization, callout wrapping, and printed labels outside callouts are formatting.

`````diff
--- /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 12 Partial Differential Equations in Polar and Cylindrical Coordinates/12.8 Bessel Series Expansions.md
+++ /Users/gradyclopton/ObsidianVaults/complex_analysis/Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 12 Partial Differential Equations in Polar and Cylindrical Coordinates/12.8 Bessel Series Expansions.md
@@ -1,18 +1,22 @@
+
 ### 12.8 Bessel Series Expansions
 
 In this section we explore some recurrence relations, orthogonality properties of Bessel functions, and expansions of functions in Bessel series. Many of these properties are used in solving the boundary value problems occurring in this chapter and throughout this book.
 
 ## Identities Involving Bessel Functions
 
-We start with two basic identities. For any $p \geq 0$,
-
-$$
-\frac{d}{d x}\left[x^{p} J_{p}(x)\right]=x^{p} J_{p-1}(x)
-$$
-
-$$
-\frac{d}{d x}\left[x^{-p} J_{p}(x)\right]=-x^{-p} J_{p+1}(x)
-$$
+> [!identity|526b6194-6aad-5d21-8f21-aeef31a91829.local at=eb82eefc-b051-5f42-8fc6-5542b40594d1] Differentiation identities for powers times Bessel functions of the first kind
+> For real $p\ge0$ and $x>0$, the Bessel function $J_p$ of the first kind satisfies
+>
+> $$
+> \frac{d}{d x}\left[x^{p} J_{p}(x)\right]=x^{p} J_{p-1}(x)
+> $$
+>
+> $$
+> \frac{d}{d x}\left[x^{-p} J_{p}(x)\right]=-x^{-p} J_{p+1}(x)
+> $$
+
+*Printed equation labels: (1) derivative of $x^pJ_p(x)$; (2) derivative of $x^{-p}J_p(x)$.*
 
 Note that for $p=0$, the second identity yields
 
@@ -33,16 +37,19 @@
 
 In the next to last step we used the basic property of the gamma function to write $\Gamma(k+p+1)=(p+k) \Gamma(p+k)$. The second identity is proved similarly (Exercise 1(a)).
 
-Many other useful identities follow from (1) and (2). We list some of the most commonly used ones:
-
-$$
-\begin{gathered}
-x J_{p}^{\prime}(x)+p J_{p}(x)=x J_{p-1}(x) \\
-x J_{p}^{\prime}(x)-p J_{p}(x)=-x J_{p+1}(x) \\
-J_{p-1}(x)-J_{p+1}(x)=2 J_{p}^{\prime}(x) \\
-J_{p-1}(x)+J_{p+1}(x)=\frac{2 p}{x} J_{p}(x)
-\end{gathered}
-$$
+> [!identity|e810a894-67c4-5fbd-83e2-71c7f99d063e.local at=4c06bf98-c6cc-5e29-a594-79257b2bf3b6] Order recurrences for Bessel functions of the first kind
+> For real $p\ge0$ and $x>0$, the Bessel functions $J_\nu$ of the first kind satisfy
+>
+> $$
+> \begin{gathered}
+> x J_{p}^{\prime}(x)+p J_{p}(x)=x J_{p-1}(x) \\
+> x J_{p}^{\prime}(x)-p J_{p}(x)=-x J_{p+1}(x) \\
+> J_{p-1}(x)-J_{p+1}(x)=2 J_{p}^{\prime}(x) \\
+> J_{p-1}(x)+J_{p+1}(x)=\frac{2 p}{x} J_{p}(x)
+> \end{gathered}
+> $$
+
+*Printed equation labels: (3) lower-order recurrence; (4) higher-order recurrence; (5) difference recurrence; (6) sum recurrence.*
 
 (We note that the corresponding formulas for Bessel functions of the second kind also hold.) To prove (3), we expand the left side of (1) using the product rule and get
 
@@ -52,19 +59,22 @@
 
 Dividing through by $x^{p-1}$ gives (3). Identity (4) is proved similarly by starting with (2) and expanding using the product rule. Adding (3) and (4) and simplifying yields (5). Subtracting (4) from (3) and simplifying yields (6)
 
-There are similar identities involving integrals of Bessel functions. For example, the identities
-
-$$
-\int x^{p+1} J_{p}(x) d x=x^{p+1} J_{p+1}(x)+C
-$$
-
-and
-
-$$
-\int x^{-p+1} J_{p}(x) d x=-x^{-p+1} J_{p-1}(x)+C
-$$
-
-follow easily by integrating both sides of (1) and (2) (Exercise 1).
+> [!identity|04e76fe2-b50e-54bb-a3b6-206f69783650.local at=4bb611bb-6d68-5eeb-8963-11918666e714] Antiderivatives of power-weighted Bessel functions of the first kind
+> For real $p\ge0$ and $x>0$, with arbitrary integration constant $C$,
+>
+> $$
+> \int x^{p+1} J_{p}(x) d x=x^{p+1} J_{p+1}(x)+C
+> $$
+>
+> and
+>
+> $$
+> \int x^{-p+1} J_{p}(x) d x=-x^{-p+1} J_{p-1}(x)+C
+> $$
+
+*Printed equation labels: (7) integral of $x^{p+1}J_p(x)$; (8) integral of $x^{1-p}J_p(x)$.*
+
+These follow by integrating the differentiation identities with the order shifted appropriately (Exercise 1).
 
 ## Orthogonality of Bessel Functions
 
@@ -72,8 +82,19 @@
 
 In constructing systems of orthogonal Bessel functions, we will proceed in a similar way by using a single Bessel function and its zeros. Fix an order $p \geq 0$, and consider the graph of $J_{p}(x)$ for $x>0$. Figure 1 shows typical graphs of Bessel functions.
 
-![](./images/1c611338-958a-44f7-9d79-2dde87e6ac2a-58_468_1196_1190_559.jpg)
-Figure 1 A Bessel function $J_{p}(x)$ has infinitely many positive zeros.
+```scientific-figure
+id: eeaff3c2-ad85-4507-91c3-6cf9b1433fc7
+numbered: false
+title: ""
+caption: Figure 1 A Bessel function $J_{p}(x)$ has infinitely many positive zeros.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 12 Partial Differential Equations in Polar and Cylindrical Coordinates/images/1c611338-958a-44f7-9d79-2dde87e6ac2a-58_468_1196_1190_559.jpg
+    caption: ""
+```
+
 
 We see from Figure 1 that the Bessel function $J_{p}$ has infinitely many zeros on the positive axis $x>0$ (just like $\sin x$ ). This important fact is proved in the following section (see Exercises 14 and 35 for the cases $p=0, \pm 1, \pm 2, \ldots$, and $\frac{1}{2}$ ). We denote these zeros in ascending order
 
@@ -81,58 +102,92 @@
 0<\alpha_{p 1}<\alpha_{p 2}<\cdots<\alpha_{p j}<\cdots .
 $$
 
-Hence $\alpha_{p j}$ denotes the $j$ th positive zero of $J_{p}$. (Sometimes the notation $\alpha_{p, j}$ will be used.) Unlike the case of the sine function, where the zeros are easily determined by $n \pi$, there is no formula for the positive zeros of the Bessel
-
-Let $a$ be a positive number. To generate orthogonal functions on the interval $[0, a]$ from $J_{p}$, we proceed as in the case of the sine function, using $\alpha_{p j}$, the zeros of the Bessel function. We obtain the functions
-
-$$
-J_{p}\left(\frac{\alpha_{p j}}{a} x\right), \quad j=1,2,3, \ldots
-$$
-
-The first four functions, corresponding to $p=0$, are shown in Figure 2.
-
-It is interesting to note that all these functions are bounded by 1 and their number of zeros increase in the interval $(0,1)$. These properties are shared by other systems of orthogonal functions encountered earlier, in particular, the
-functions. Since the numerical values of these zeros are very important in applications, they are found in most mathematical tables and computer systems. For later use, we list in Table 1 the first five positive zeros of $J_{0}$, $J_{1}$, and $J_{2}$.
-
-| $j$ | 1 | 2 | 3 | 4 | 5 |
-| :---: | :---: | :---: | :---: | :---: | :---: |
-| $\alpha_{0 j}$ | 2.40483 | 5.52008 | 8.65373 | 11.7915 | 14.9309 |
-| $\alpha_{1 j}$ | 3.83171 | 7.01559 | 10.1735 | 13.3237 | 16.4706 |
-| $\alpha_{2 j}$ | 5.13562 | 8.41724 | 11.6198 | 14.796 | 18.9801 |
-
-Table 1 Positive zeros of $J_{0}, J_{1}$, and $J_{2}$.
-
-functions. Since the numerical values of these zeros are very important in applications, they are found in most mathematical tables and computer systems. For later use, we list in Table 1 the first five positive zeros of $J_{0}$,
-$J_{1}$, and $J_{2}$. | $j$ | 1 | 2 | 3 | 4 | 5 |
-| :---: | :---: | :---: | :---: | :---: | :---: |
-| $\alpha_{0 j}$ | 2.40483 | 5.52008 | 8.65373 | 11.7915 | 14.9309 |
-| $\alpha_{1 j}$ | 3.83171 | 7.01559 | 10.1735 | 13.3237 | 16.4706 |
-| $\alpha_{2 j}$ | 5.13562 | 8.41724 | 11.6198 | 14.796 | 18.9801 | trigonometric functions.
-
-![](./images/1c611338-958a-44f7-9d79-2dde87e6ac2a-59_481_1075_1262_502.jpg)
-Figure 2 Orthogonal functions generated with $J_{0}(x): J_{0}\left(\alpha_{01} x\right), J_{0}\left(\alpha_{02} x\right), \ldots$.
+Hence $\alpha_{p j}$ denotes the $j$ th positive zero of $J_{p}$. (Sometimes the notation $\alpha_{p, j}$ will be used.) Unlike the sine function, whose positive zeros are $n\pi$, Bessel functions generally require numerical determination of their positive zeros. Table 1 lists the first five positive zeros of $J_0$, $J_1$, and $J_2$.
+
+```scientific-table
+id: 427bc5f6-a0ca-4727-b0a4-e945e1c8287c
+numbered: false
+title: ""
+caption: Table 1 Positive zeros of $J_{0}, J_{1}$, and $J_{2}$.
+captionVisible: true
+captionPosition: below
+rows:
+  - - text: $j$
+    - text: "1"
+    - text: "2"
+    - text: "3"
+    - text: "4"
+    - text: "5"
+  - - text: $\alpha_{0 j}$
+    - text: "2.40483"
+    - text: "5.52008"
+    - text: "8.65373"
+    - text: "11.7915"
+    - text: "14.9309"
+  - - text: $\alpha_{1 j}$
+    - text: "3.83171"
+    - text: "7.01559"
+    - text: "10.1735"
+    - text: "13.3237"
+    - text: "16.4706"
+  - - text: $\alpha_{2 j}$
+    - text: "5.13562"
+    - text: "8.41724"
+    - text: "11.6198"
+    - text: "14.796"
+    - text: "17.9598"
+headerRows: 1
+rowHeaders: true
+style: scientific
+```
+
+
+
+
+Let $a>0$. The zeros of $J_p$ generate functions on $[0,a]$:
+$$
+J_p\left(\frac{\alpha_{pj}}a x\right),\qquad j=1,2,3,\ldots.
+\tag{9}
+$$
+The first four functions for $p=0$ and $a=1$ are shown in Figure 2. They are bounded in absolute value by $1$, and their number of zeros in $(0,1)$ increases with $j$, as happens for the trigonometric orthogonal systems encountered earlier.
+
+```scientific-figure
+id: 88e28a49-5b2c-41ec-8e4e-ff57b47cd898
+numbered: false
+title: ""
+caption: "Figure 2 Orthogonal functions generated with $J_{0}(x): J_{0}\\left(\\alpha_{01} x\\right), J_{0}\\left(\\alpha_{02} x\\right), \\ldots$."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 12 Partial Differential Equations in Polar and Cylindrical Coordinates/images/1c611338-958a-44f7-9d79-2dde87e6ac2a-59_481_1075_1262_502.jpg
+    caption: ""
+```
+
 
 To simplify the notation, we let
 
 $$
 \lambda_{p j}=\frac{\alpha_{p j}}{a} \quad j=1,2,3, \ldots
+\tag{10}
 $$
 
 So $\lambda_{p j}$ is the value of the $j$ th positive zero of $J_{p}$ scaled by a fixed factor $1 / a$. We are now in a position to state some fundamental identities.
 
-THEOREM 1 ORTHOGONALITY OF BESSEL FUNCTIONS WITH RESPECT TO A WEIGHT
-
-Fix $p \geq 0$ and $a>0$. Let $J_{p}\left(\lambda_{p j} x\right)(j=1,2, \ldots)$ be as in (9) and (10). Then
-
-$$
-\int_{0}^{a} J_{p}\left(\lambda_{p j} x\right) J_{p}\left(\lambda_{p k} x\right) x d x=0 \text { for } j \neq k
-$$
-
-and
-
-$$
-\int_{0}^{a} J_{p}^{2}\left(\lambda_{p j} x\right) x d x=\frac{a^{2}}{2} J_{p+1}^{2}\left(\alpha_{p j}\right) \text { for } j=1,2, \ldots
-$$
+> [!theorem|0772d5b0-9a5c-5645-b3fe-75e1d07a2a86.local at=a36dcd1b-ef7a-57c9-9cba-6ee29634022b] Weighted orthogonality and squared norms of Dirichlet Bessel modes
+> Fix $p\ge0$ and $a>0$. Let $J_p$ be the Bessel function of the first kind, let $\alpha_{pj}$ be its $j$th positive zero, and set $\lambda_{pj}=\alpha_{pj}/a$. Then
+>
+> $$
+> \int_{0}^{a} J_{p}\left(\lambda_{p j} x\right) J_{p}\left(\lambda_{p k} x\right) x d x=0 \text { for } j \neq k
+> $$
+>
+> and
+>
+> $$
+> \int_{0}^{a} J_{p}^{2}\left(\lambda_{p j} x\right) x d x=\frac{a^{2}}{2} J_{p+1}^{2}\left(\alpha_{p j}\right) \text { for } j=1,2, \ldots
+> $$
+
+*Printed equation labels: (11) orthogonality of distinct modes; (12) squared norm.*
 
 Note that (12) involves $\lambda_{p j}$ and $\alpha_{p j}$. Property (11) is described by saying that the functions $J_{p}\left(\lambda_{p j} x\right), j=1,2, \ldots$ are orthogonal on the interval $[0, a]$ with respect to the weight $x$. The phrase "with respect to the weight $x$ " refers to the presence of the function $x$ in the integrand in (11). On the interval [ 0,1 ]-that is when $a=1$-formulas (11) and (12) take on a simpler form
 
@@ -143,6 +198,8 @@
 \end{gathered}
 $$
 
+*Printed equation labels: (13) orthogonality on the unit interval; (14) squared norm on the unit interval.*
+
 The proof of (11) is found in the proof of Theorem 3. The proof of (12) is outlined in Exercise 36.
 
 ## Bessel Series and Bessel-Fourier Coefficients
@@ -151,50 +208,52 @@
 
 $$
 f(x)=\sum_{j=1}^{\infty} A_{j} J_{p}\left(\lambda_{p j} x\right)
+\tag{15}
 $$
 
 called the Bessel series of order $p$ of $f$. Putting aside questions of convergence, let us assume (15) is valid and proceed to find the coefficients in the series. Multiplying both sides of (15) by $J_{p}\left(\lambda_{p k} x\right) x$ and integrating term by term on the interval $[0, a]$ gives
 
 $$
 \int_{0}^{a} f(x) J_{p}\left(\lambda_{p k} x\right) x d x=\sum_{j=1}^{\infty} A_{j} \overbrace{\int_{0}^{a} J_{p}\left(\lambda_{p j} x\right) J_{p}\left(\lambda_{p k} x\right) x d x}^{=0 \text { except when } j=k}
+\tag{16}
 $$
 
 The orthogonality property (11) shows that all the terms on the right side of (16) are 0 except when $j=k$. Canceling the zero terms and using (12), we get
 
 $$
 A_{j}=\frac{\int_{0}^{a} f(x) J_{p}\left(\lambda_{p j} x\right) x d x}{\int_{0}^{a} J_{p}^{2}\left(\lambda_{p j} x\right) x d x}=\frac{2}{a^{2} J_{p+1}^{2}\left(\alpha_{p j}\right)} \int_{0}^{a} f(x) J_{p}\left(\lambda_{p j} x\right) x d x
+\tag{17}
 $$
 
 The number $A_{j}$ is called the $\boldsymbol{j}$ th Bessel-Fourier coefficient or simply the Bessel coefficient of the function $f$.
 
-The next theorem gives conditions under which the Bessel series expansion of a function is valid. For the meaning of piecewise smooth, refer to Section 2.2.
-
-THEOREM 2 BESSEL SERIES OF ORDER $p$
-
-Note the similarity with Fourier series. At the points of discontinuity the Bessel series converges to the average of the function.
-
-If $f$ is piecewise smooth on $[0, a]$, then $f$ has a Bessel series expansion of order $p$ on the interval $(0, a)$ given by
-
-$$
-f(x)=\sum_{j=1}^{\infty} A_{j} J_{p}\left(\lambda_{p j} x\right),
-$$
-
-where $\lambda_{p 1}, \lambda_{p 2}, \ldots$ are the scaled positive zeros of the Bessel function $J_{p}$ given by ( 10 ), and $A_{j}$ is given by ( 17 ). In the interval ( $0, a$ ), the series converges to $f(x)$ where $f$ is continuous and converges to the average $\frac{f(x+)+f(x-)}{2}$ at the points of discontinuity.
+The next theorem gives conditions under which the Bessel series expansion of a function is valid. For the meaning of piecewise smooth, refer to Section 7.2.
+
+> [!theorem|cf3f6d2d-dc5a-555b-86e2-323ff9599805.local at=d93068ef-da1e-5cd8-a42e-9b6e1a1173ea] Bessel Series of Order $p$
+> Let $a>0$, $p\geq0$, and let $J_p$ denote the Bessel function of the first kind.
+>
+> If $f$ is piecewise smooth on $[0, a]$, then $f$ has a Bessel series expansion of order $p$ on the interval $(0, a)$ given by
+>
+> $$
+> f(x)=\sum_{j=1}^{\infty} A_{j} J_{p}\left(\lambda_{p j} x\right),
+> $$
+>
+> where $\lambda_{p 1}, \lambda_{p 2}, \ldots$ are the scaled positive zeros of the Bessel function $J_{p}$ $\lambda_{pj}=\alpha_{pj}/a$, with $\alpha_{pj}$ the $j$th positive zero of $J_p$, and $A_j=\frac{2}{a^2J_{p+1}(\alpha_{pj})^2}\int_0^a f(t)J_p(\lambda_{pj}t)t\,dt$. In the interval ( $0, a$ ), the series converges to $f(x)$ where $f$ is continuous and converges to the average $\frac{f(x+)+f(x-)}{2}$ at the points of discontinuity.
 
 Before giving an example of a Bessel series, we make a useful remark about the notation. While the notation $\alpha_{p j}$ and $\lambda_{p j}$ is appropriate to denote the zeros and scaled zeros of the Bessel function of order $p$, it is a little cumbersome to work with. For this reason, when it is understood which order we are dealing with, and so there is no risk of confusion, we will drop the index $p$ and write $\alpha_{j}$ and $\lambda_{j}$ instead of $\alpha_{p j}$ and $\lambda_{p j}$.
 
-EXAMPLE 1 A Bessel series on the interval [0,1]
-Find the Bessel series expansion of order 0 of the function $f(x)=1,0<x<1$.
-Solution Applying Theorem 2, we get
+> [!exercise|672f0f1b-c48b-5e8c-ae64-d0724eecbbf6.local at=7def3341-2c39-5334-9a5b-3b2e7a66c71c] EXAMPLE 1 A Bessel series on the interval [0,1]
+> Find the Bessel series expansion of order 0 of the function $f(x)=1,0<x<1$.
+
+##### solution
+
+Applying Theorem 2, we get
 
 $$
 f(x)=\sum_{j=1}^{\infty} A_{j} J_{0}\left(\alpha_{j} x\right)
 $$
 
 where $\alpha_{j}$ is the $j$ th positive zero of $J_{0}$, and
-
-![](./images/1c611338-958a-44f7-9d79-2dde87e6ac2a-62_390_470_268_59.jpg)
-Figure 3 Partial sums of the Bessel series.
 
 $$
 \begin{aligned}
@@ -212,13 +271,43 @@
 1=\sum_{j=1}^{\infty} \frac{2}{\alpha_{j} J_{1}\left(\alpha_{j}\right)} J_{0}\left(\alpha_{j} x\right) \quad 0<x<1 .
 $$
 
-| $j$ | 1 | 2 | 3 | 4 | 5 |
-| :---: | :---: | :---: | :---: | :---: | :---: |
-| $\alpha_{j}$ | 2.4048 | 5.5201 | 8.6537 | 11.7915 | 14.9309 |
-| $J_{1}\left(\alpha_{j}\right)$ | .5191 | -.3403 | .2714 | -.2325 | .2065 |
-| $\frac{2}{\alpha_{j} J_{1}\left(\alpha_{2}\right)}$ | 1.6020 | -1.0648 | .8514 | -.7295 | .6487 |
-
-Table 2 Numerical data for Example 1
+```scientific-table
+id: 7bb61212-b96c-43c3-b54f-835faff2ee20
+numbered: false
+title: ""
+caption: Table 2 Numerical data for Example 1
+captionVisible: true
+captionPosition: below
+rows:
+  - - text: $j$
+    - text: "1"
+    - text: "2"
+    - text: "3"
+    - text: "4"
+    - text: "5"
+  - - text: $\alpha_{j}$
+    - text: "2.4048"
+    - text: "5.5201"
+    - text: "8.6537"
+    - text: "11.7915"
+    - text: "14.9309"
+  - - text: $J_{1}\left(\alpha_{j}\right)$
+    - text: ".5191"
+    - text: "-.3403"
+    - text: ".2714"
+    - text: "-.2325"
+    - text: ".2065"
+  - - text: $\frac{2}{\alpha_{j} J_{1}\left(\alpha_{j}\right)}$
+    - text: "1.6020"
+    - text: "-1.0648"
+    - text: ".8514"
+    - text: "-.7295"
+    - text: ".6487"
+headerRows: 1
+rowHeaders: true
+style: scientific
+```
+
 
 Using the numerical data provided by Tables 1 and 2, we can write explicitly the first few terms of the series:
 
@@ -231,29 +320,42 @@
 
 It is worth noticing that the Bessel coefficients tend to 0 as $j \rightarrow \infty$. This is a property that holds in general.
 
+```scientific-figure
+id: 0ea48ca9-5079-492b-8a24-d59b2c0f0f47
+numbered: false
+title: ""
+caption: Figure 3 Partial sums of the Bessel series.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 12 Partial Differential Equations in Polar and Cylindrical Coordinates/images/1c611338-958a-44f7-9d79-2dde87e6ac2a-62_390_470_268_59.jpg
+    caption: ""
+```
+
+
 Note that Theorem 2 tells us nothing about the behavior of the Bessel series at the endpoints of the interval. In this example, if we take $x=1$ in the series all the terms become zero, since we are evaluating $J_{0}$ at its zeros. This is also clear from the graphs of the partial sums in Figure 3. So, in this example, the Bessel series does not converge to the function at one of the endpoints.
 
 ## Parametric Form of Bessel's Equation
 
 In the remainder of this section, we explore two important differential equations that are closely related to Bessel's equation.
 
-THEOREM 3 PARAMETRIC FORM OF BESSEL'S EQUATION
-
-The condition that $y(0)$ be finite is effectively a second boundary condition on $y$.
-
-Let $p \geq 0, a>0$, and let $\alpha_{p j}$ denote the $j$ th positive zero of $J_{p}(x)$. For $j=1,2, \ldots$, the functions $J_{p}\left(\frac{\alpha_{p j}}{\alpha} x\right)$ are solutions of the parametric form of Bessel's equation of order $p$,
-
-$$
-x^{2} y^{\prime \prime}(x)+x y^{\prime}(x)+\left(\lambda^{2} x^{2}-p^{2}\right) y(x)=0
-$$
-
-together with the boundary conditions
-
-$$
-y(0) \text { finite, } y(a)=0
-$$
-
-when $\lambda=\lambda_{p j}=\frac{\alpha_{p j}}{a}$, and these are the only solutions of (18), aside from scalar multiples, with these properties. Moreover, these solutions satisfy (11) and (12) and so they are orthogonal on the interval $[0, a]$ with respect to the weight function $x$.
+> [!theorem|ab5e42d2-4be6-53d3-ad29-a2620bbff2c2.local at=12c592fe-9ce1-5ba9-9978-23abf0e09241] Parametric Form of Bessel's Equation
+> Let $p \geq 0, a>0$, and let $\alpha_{p j}$ denote the $j$ th positive zero of $J_{p}(x)$. For $j=1,2, \ldots$, the functions $J_{p}\left(\frac{\alpha_{p j}}{a} x\right)$ are solutions of the parametric form of Bessel's equation of order $p$,
+>
+> $$
+> x^{2} y^{\prime \prime}(x)+x y^{\prime}(x)+\left(\lambda^{2} x^{2}-p^{2}\right) y(x)=0
+> $$
+>
+> together with the boundary conditions
+>
+> $$
+> y(0) \text { finite, } y(a)=0
+> $$
+>
+> when $\lambda=\lambda_{p j}=\frac{\alpha_{p j}}{a}$, and these are the only solutions of the displayed equation, aside from scalar multiples, with these properties. Moreover, these solutions are orthogonal on the interval $[0, a]$ with respect to the weight function $x$.
+
+*Printed equation labels: (18) parametric Bessel equation; (19) boundedness at the origin and zero boundary value.*
 
 Proof We will make a change of variables in (18) and reduce it to Bessel's equation as follows. Let $u=\lambda x, d u=\lambda d x$, and let $y(x)=y\left(\frac{u}{\lambda}\right)=Y(u)$. From the chain rule, $y^{\prime}(x)=Y^{\prime}(u) \frac{d u}{d x}=\lambda Y^{\prime}(u)$, and, likewise, $y^{\prime \prime}(x)=\lambda^{2} Y^{\prime \prime}(u)$. Substituting in (18), we get Bessel's equation of order $p$ in $Y(u)$
 
@@ -275,7 +377,7 @@
 
 are the only positive values of $\lambda$ for which there are nontrivial solutions. Therefore, the solutions of (18) and (19) are as claimed.
 
-We come now to the proof of (11). To simplify notation, let us write $\lambda_{j}$ for $\lambda_{p j}$, and $\phi_{j}(x)$ for $J_{p j}\left(\lambda_{p j} x\right)$. The goal is to show that for $j \neq k$
+We come now to the proof of (11). To simplify notation, let us write $\lambda_{j}$ for $\lambda_{p j}$, and $\phi_{j}(x)$ for $J_{p}\left(\lambda_{p j} x\right)$. The goal is to show that for $j \neq k$
 
 $$
 \int_{0}^{a} \phi_{j}(x) \phi_{k}(x) x d x=0
@@ -308,25 +410,30 @@
 Hence
 
 $$
-\left(\lambda_{k}^{2}-\lambda_{j}^{2}\right) \int_{0}^{a} \phi_{j}(x) \phi_{k}(x) x d x=\phi_{k} x \phi_{j}^{\prime}-\left.\phi_{j} x \phi_{k}^{\prime}\right|_{0} ^{a}=0
-$$
-
-because $\phi_{j}(a)=\phi_{k}(a)=0$, and the desired result follows, since $\lambda_{k}^{2}-\lambda_{j}^{2} \neq 0$. For the proof of (12), see Exercise 36. $\square$
+\left(\lambda_{k}^{2}-\lambda_{j}^{2}\right) \int_{0}^{a} \phi_{j}(x) \phi_{k}(x) x d x=\left[\phi_{k} x \phi_{j}^{\prime}-\phi_{j} x \phi_{k}^{\prime}\right]_{0}^{a}=0
+$$
+
+because $\phi_{j}(a)=\phi_{k}(a)=0$ and the lower-end boundary expression tends to zero for the regular Bessel solutions, and the desired result follows, since $\lambda_{k}^{2}-\lambda_{j}^{2} \neq 0$. For the proof of (12), see Exercise 36. $\square$
 
 Our last example is a differential equation that gives rise to yet another important family of functions.
 
-## EXAMPLE 2 Spherical Bessel functions
+> [!exercise|3692b0f1-7651-56c7-91ef-34c9267bb46b.local at=2abf67b0-26f5-50ba-be70-02174fbd393a] EXAMPLE 2 Spherical Bessel functions
+> For integers $n\ge0$, find the values $k\ge0$ for which $x^2y^{\prime\prime}+2xy^{\prime}+(kx^2-n(n+1))y=0$ on $0<x<a$ has a nonzero bounded solution satisfying $y(a)=0$. Express the corresponding solutions using spherical Bessel functions.
+
+##### solution
 
 The equation
 
 $$
 x^{2} y^{\prime \prime}+2 x y^{\prime}+\left(k x^{2}-n(n+1)\right) y=0, \quad 0<x<a, \quad y(a)=0,
-$$
-
-arises in many important applications in Chapter 5. In this equation, $k$ is a nonnegative real number and $n=0,1,2, \ldots$. We are seeking bounded solutions in the interval $0 \leq x \leq a$. You can check that the substitution
+\tag{20}
+$$
+
+arises in many important applications in Chapter 13. In this equation, $k$ is a nonnegative real number and $n=0,1,2, \ldots$. We are seeking bounded solutions in the interval $0 \leq x \leq a$. You can check that the substitution
 
 $$
 y=x^{-1 / 2} w
+\tag{21}
 $$
 
 transforms (20) into the following parametric form of Bessel's equation:
@@ -355,228 +462,387 @@
 
 Hence, using (21), it follows that the solutions $y_{n j}$ of (20) are scalar multiples of
 
-Figure 4 Spherical Bessel functions, $j_{0}, j_{1}, j_{2}, j_{3}$.
-
-$$
-x^{-1 / 2} J_{n+\frac{1}{2}}\left(\lambda_{n}, j x\right), \quad n=0,1,2, \ldots, \quad j=1,2, \ldots .
-$$
-
-It is customary to express the solutions in terms of the spherical Bessel functions of the first kind (see Figure 4):
-
-$$
-j_{n}(x)=\left(\frac{\pi}{2 x}\right)^{1 / 2} J_{n+\frac{1}{2}}(x), \quad n=0,1,2, \ldots
-$$
+$$
+x^{-1 / 2} J_{n+\frac{1}{2}}\left(\lambda_{n,j} x\right), \quad n=0,1,2, \ldots, \quad j=1,2, \ldots .
+\tag{22}
+$$
+
+> [!definition|ea4affd5-e5a4-5891-a463-4ddc05cd5773.local at=6aaa9d07-2d96-5393-80c7-48608a7f872c] Spherical Bessel functions of the first kind
+> For integers $n\ge0$ and $x>0$, the spherical Bessel function of the first kind is defined by
+>
+> $$
+> j_{n}(x)=\left(\frac{\pi}{2 x}\right)^{1 / 2} J_{n+\frac{1}{2}}(x), \quad n=0,1,2, \ldots
+> $$
+>
+> Here $J_{n+1/2}$ is the ordinary Bessel function of the first kind. Values at $x=0$ are defined by the right-hand limits.
+
+*Printed equation label: (23).*
+
+```scientific-figure
+id: 67f34737-ee38-4739-acc8-dde300cac142
+numbered: false
+title: ""
+caption: Figure 4 Spherical Bessel functions $j_0,j_1,j_2,j_3$.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 12 Partial Differential Equations in Polar and Cylindrical Coordinates/images/asmar-12-8-figure-4-source.png
+    caption: ""
+```
+
 
 Choosing a specific multiple of the functions in (22), we obtain the solutions of (20) as the spherical Bessel functions:
 
 $$
 y_{n, j}(x)=j_{n}\left(\lambda_{n, j} x\right), \quad n=0,1,2, \ldots, \quad j=1,2, \ldots .
-$$ $\square$
-
+\tag{24}
+$$
+
+$\square$
 In the exercises you are asked to study the spherical Bessel functions, including their orthogonality. In most cases, the results are simple consequences of properties of Bessel functions and (23).
 
-## Exercises 4.8
-
-1. (a) Supply the details of the proof of (2), (7), and (8). [Hint: To prove (2), show that the derivative is $\sum_{k=1}^{\infty} \frac{(-1)^{k} 2 k}{k!\Gamma(k+p+1) 2^{2 k+p}} x^{2 k-1}$. Then change $k$ to $k+1$ to start the sum at 0 .]
-(b) Supply the details of the proof of (4), (5), and (6).
-2. (a) On the graphs of $J_{0}$ and $J_{1}$ in Figure 1, Section 12.7, note that the maxima and minima of $J_{0}$ occur at the zeros of $J_{1}$. Prove this fact.
-(b) Show that the maximum and minimum values of $J_{p}$ occur when
-
-$$
-x=\frac{p J_{p}(x)}{J_{p+1}(x)} \quad \text { or } \quad x=\frac{p J_{p}(x)}{J_{p-1}(x)} \quad \text { or } \quad J_{p-1}(x)=J_{p+1}(x) .
-$$
-
-(c) Illustrate (b) graphically when $p=2$.
-(d) Show that at the zeros of $J_{p}, J_{p-1}$ and $J_{p+1}$ have equal absolute values but opposite signs.
-
-In Exercises 3-10, evaluate the given integral.
-3. $\int x J_{0}(x) d x$.
-4. $\int x^{4} J_{3}(x) d x$.
-5. $\int J_{1}(x) d x$.
-6. $\int x^{-2} J_{3}(x) d x$.
-7. $\int x^{3} J_{2}(x) d x$.
-8. $\int x^{3} J_{0}(x) d x$.
-9. $\int J_{3}(x) d x$.
-10. $\int_{0}^{\infty} J_{1}(x)\left[J_{0}(x)\right]^{n} d x$.
-[Hint: Let $u=J_{0}(x)$.]
-11. Use (2) and Example 1 of Section 12.7 to derive the formula
-
-$$
-J_{3 / 2}(x)=\sqrt{\frac{2}{\pi x}}\left[\frac{\sin x}{x}-\cos x\right]
-$$
-
-12. Use (2) and Exercise 11 to derive
-
-$$
-J_{5 / 2}(x)=\sqrt{\frac{2}{\pi x}}\left[\left(\frac{3}{x^{2}}-1\right) \sin x-\frac{3}{x} \cos x\right] .
-$$
-
-13. Express $J_{5}$ in terms of $J_{0}$ and $J_{1}$.
-14. Use the explicit formula for $J_{1 / 2}$ given in Example 1 of Section 12.7 to show that $J_{1 / 2}$ has infinitely many positive zeros in the interval $0<x<\infty$. What are these zeros?
-15. (a) Plot the functions $\frac{\sin x}{x}$ and $\cos x$ on the same graph to illustrate the fact that they intersect at infinitely many points. Conclude that the function $J_{3 / 2}(x)$ has infinitely many zeros in ( $0, \infty$ ).
-(b) Approximate the first three roots of the equation $\frac{\sin x}{x}=\cos x$.
-16. (a) Let $0<\alpha_{p 1}<\alpha_{p 2}<\cdots<\alpha_{p j}<\cdots$ denote the positive zeros of $J_{p}$. How many roots does the function $J_{p}\left(\frac{\alpha_{p j}}{a} x\right)$ have in the interval $0<x<a$ ? Justify your answer.
-(b) Illustrate your answer graphically with $p=2, a=1$, and $j=5$.
-17. Let $0<c<1$, and let
-
-$$
-f(x)= \begin{cases}1 & \text { if } 0<x<c \\ 0 & \text { if } c<x<1\end{cases}
-$$
-
-(a) Derive the Bessel series of order 0 of $f$
-
-$$
-\sum_{j=1}^{\infty} \frac{2 c J_{1}\left(c \alpha_{j}\right)}{\alpha_{j} J_{1}\left(\alpha_{j}\right)^{2}} J_{0}\left(\alpha_{j} x\right), \quad 0<x<1
-$$
-
-(b) Discuss the convergence of the series in the interval $0<x<1$.
-(c) Take $c=\frac{1}{2}$. Investigate the convergence of the series at $x=0$ and $x=1$ numerically. Does the series seem to converge at one or both points? To what values? (Note that convergence at these points is not covered by Theorem 2.)
-18. Take $a=\frac{1}{3}$ in Exercise 17 and write explicitly the first five terms of the series in this case. Plot several partial sums and describe the behavior at and around the point $x=\frac{1}{3}$. Observe how the partial sums overshoot their limiting values regardless of the increase in the number of terms in the approximating partial sums. This illustrates the Gibbs phenomenon at a point of discontinuity for Bessel series expansions.
-19. (a) Obtain the Bessel series expansion
-
-$$
-x^{4}=2 \sum_{j=1}^{\infty} \frac{1}{\alpha_{j} J_{5}\left(\alpha_{j}\right)} J_{4}\left(\alpha_{j} x\right), \quad 0<x<1
-$$
-
-where the $\alpha_{j}$ 's are the positive zeros of $J_{4}$.
-(b) Plot some partial sums and discuss their behavior on the interval $0<x<1$.
-20. Bessel series of order $m$. Fix a number $m \geq 0$ and let $0<\alpha_{1}<\alpha_{2}< \ldots<\alpha_{j}<\ldots$ denote the sequence of positive zeros of $J_{m}$. Obtain the Bessel series expansion
-
-$$
-x^{m}=2 \sum_{j=1}^{\infty} \frac{1}{\alpha_{j} J_{m+1}\left(\alpha_{j}\right)} J_{m}\left(\alpha_{j} x\right), \quad 0<x<1
-$$
-
-21. Refer to Exercise 20.
-(a) Take $m=\frac{1}{2}$, and determine the exact values of the $\alpha_{j}$ 's in this case? [Hint: Example 1 of Section 12.7.]
-(b) Compute explicitly the coefficients in the Bessel series expansion of $f(x)=\sqrt{x}$, $0<x<1$.
-(c) Recall the formula for $J_{\frac{1}{2}}$ in terms of $\sin x$ and show that the expansion in (b) is really a sine Fourier series expansion of $x$.
-(d) Plot some partial sums of the Bessel series and discuss the convergence on the interval $0<x<1$.
-22. Study the behavior of the partial sums of the Bessel series in Exercise 20 when $m=\frac{3}{2}$. What do they converge to in the interval $0<x<1$ ?
-In Exercises 23-30, approximate the given function by a Bessel series of the given order $p$. Plot several partial sums of the series and discuss their convergence on the given interval.
-23. $f(x)=x^{2} ; 0<x<1 ; p=2$.
-24. $f(x)=x^{3} ; 0<x<1 ; p=3$.
-25. $f(x)= \begin{cases}0 & \text { if } 0<x<\frac{1}{2}, \\ \frac{1}{x} & \text { if } \frac{1}{2}<x<1 ;\end{cases}$
-26. $f(x)=x^{2}, 0<x<1, p=0$.
-$p=1$.
-27. $f(x)= \begin{cases}0 & \text { if } 0<x<\frac{1}{2}, \\ \frac{1}{x^{2}} & \text { if } \frac{1}{2}<x<1 ;\end{cases}$
-28. $f(x)= \begin{cases}0 & \text { if } 0<x<\frac{1}{30}, \\ \frac{1}{x^{3}} & \text { if } \frac{1}{30}<x<1 ;\end{cases}$
-$p=2$ 。 $p=3$.
-29. $f(x)=1 ; 0<x<2 ; p=1$.
-30. $f(x)=J_{0}(x) ; 0<x<\alpha_{01} ; p=0$.
-
-In Exercises 31-34, find all $\lambda>0$ for which the given parametric form of Bessel's equation has a solution that is finite at $x=0$ and satisfies the given boundary condition.
-31. $x^{2} y^{\prime \prime}(x)+x y^{\prime}(x)+\left(\lambda^{2} x^{2}-1\right) y(x)=0, \quad y(1)=0$.
-32. $x^{2} y^{\prime \prime}(x)+x y^{\prime}(x)+\lambda^{2} x^{2} y(x)=0, \quad y(2)=0$.
-33. $x^{2} y^{\prime \prime}(x)+x y^{\prime}(x)+\left(\lambda^{2} x^{2}-\frac{1}{4}\right) y(x)=0, \quad y(\pi)=0$.
-34. $x^{2} y^{\prime \prime}(x)+x y^{\prime}(x)+\left(\lambda^{2} x^{2}-1\right) y(x)=0, \quad y\left(\frac{\pi}{2}\right)=0$.
-35. Project Problem: Zeros of $\boldsymbol{J}_{\boldsymbol{n}}$. We will prove that the positive zeros of $J_{n}(x)(n=0 \pm 1, \pm 2, \ldots)$ form an increasing sequence
-
-$$
-0<\alpha_{n 1}<\alpha_{n 2}<\cdots<\alpha_{n k}<\cdots \rightarrow \infty
-$$
-
-Parts (a)-(g) deal with the case $n=0$.
-(a) Plot the graph of $J_{0}(x)$ and note that there are infinitely many positive zeros that we will denote in ascending order by $0<\alpha_{1}<\alpha_{2}<\alpha_{3}<\ldots$
-(b) Show that the substitution $y(x)=\frac{1}{\sqrt{x}} u(x)$ transforms Bessel's equation of order 0 into
-
-$$
-u^{\prime \prime}+\left(1+\frac{1}{4 x^{2}}\right) u=0
-$$
-
-Conclude that $u(x)=\sqrt{x} J_{0}(x)$ is a solution of this differential equation.
-(c) Let $v(x)=\sin x$. Check that
-
-$$
--\left(u^{\prime \prime}+u\right) v(x)=\frac{d}{d x}\left(u v^{\prime}-u^{\prime} v\right)
-$$
-
-(d) Using (b), show that $-\left(u^{\prime \prime}+u\right)=\frac{u}{4 x^{2}}$.
-(e) Show that $\int \frac{u(x) v(x)}{4 x^{2}} d x=u v^{\prime}-u^{\prime} v+C$ and hence
-
-$$
-\int_{2 k \pi}^{(2 k+1) \pi} \frac{u(x) \sin x}{4 x^{2}} d x=-[u(2 k \pi)+u(2 k \pi+\pi)]
-$$
-
-(f) Conclude from (e) that $u(x)$ has at least one zero in $[2 k \pi,(2 k+1) \pi]$. [Hint: Assume the contrary, say $u(x)>0$ for all $x$ in the interval, and get a contradiction by studying the signs of the terms on both sides of the last equality in (e).]
-(g) Conclude that $J_{0}(x)$ has infinitely many positive zeros.
-(h) Suppose that $f$ and $g$ are differentiable functions such that $\frac{d}{d x} f(x)=g(x)$. Show that between any two zeros of $f$ there is at least one zero of $g$.
-(i) Use (2) with $p=0$ to show that $J_{1}$ has infinitely many zeros that tend to $\infty$.
-(j) Use (2) and induction to show that $J_{n}(n>0)$ has infinitely many zeros that tend to $\infty$. Prove this result for all integers $n$.
-36. Project Problem: A proof of (12). Let $0<\alpha_{1}<\alpha_{2}<\cdots<\alpha_{k}<\cdots$ denote the sequence of zeros of $J_{p}$ in ( $0, \infty$ ), and let $\lambda_{k}=\frac{\alpha_{k}}{a}$.
-(a) Rewrite (18) as
-
-$$
-\left(x y^{\prime}\right)^{\prime}+\left(\lambda^{2} x-\frac{p^{2}}{x}\right) y=0, \quad y(a)=0
-$$
-
-Multiply both sides of the equation by $x y^{\prime}$ and put it in the form
-
-$$
-\left[\left(x y^{\prime}\right)^{2}\right]^{\prime}+\left(\lambda^{2} x^{2}-p^{2}\right)\left(y^{2}\right)^{\prime}=0
-$$
-
-(b) Take $y=J_{p}\left(\lambda_{k} x\right)$ and $\lambda=\lambda_{k}$, integrate the equation in (a) over $0<x<a$, and obtain
-
-$$
-\left[a y^{\prime}(a)\right]^{2}+\left(\lambda^{2} a^{2}-p^{2}\right) y(a)^{2}-2 \lambda^{2} \int_{0}^{a} y(x)^{2} x d x=0
-$$
-
-[Hint: Use integration by parts on the second term in (a). Justify the equality $p y(0)=0$.]
-(c) For $y=J_{p}\left(\lambda_{k} x\right)$ and $\lambda=\lambda_{k}$, justify the equality $y(a)=0$, and get
-
-$$
-\left[y^{\prime}(a)\right]^{2}=\frac{2 \lambda^{2}}{a^{2}} \int_{0}^{a} x[y(x)]^{2} d x
-$$
-
-(d) For $y=J_{p}\left(\lambda_{k} x\right)$, use (4) to show that $y^{\prime}(a)=-\lambda_{k} J_{p+1}\left(\alpha_{k}\right)$. Derive (12) from (c).
+## Exercises 12.8
+
+
+> [!exercise|0dd7ec77-88db-5fa9-bcff-d70851762e0a.local at=95dc2400-20d7-58f0-aaf8-fac81e86a4d0] Exercise 1
+> (a) Supply the details of the proof of (2), (7), and (8). [Hint: To prove (2), show that the derivative is $\sum_{k=1}^{\infty} \frac{(-1)^{k} 2 k}{k!\Gamma(k+p+1) 2^{2 k+p}} x^{2 k-1}$. Then change $k$ to $k+1$ to start the sum at 0 .]
+> (b) Supply the details of the proof of (4), (5), and (6).
+
+
+> [!exercise|76478866-11bc-5f37-9eec-6b6dac34cd85.local at=e15c314c-b31a-55a0-aa7b-b6631941809f] Exercise 2
+> (a) On the graphs of $J_{0}$ and $J_{1}$ in Figure 1, Section 12.7, note that the maxima and minima of $J_{0}$ occur at the zeros of $J_{1}$. Prove this fact.
+> (b) For $x>0$, show that extrema of $J_p$ satisfy the following equivalent conditions wherever the displayed denominators are nonzero (the last condition does not require division):
+>
+> $$
+> x=\frac{p J_{p}(x)}{J_{p+1}(x)} \quad \text { or } \quad x=\frac{p J_{p}(x)}{J_{p-1}(x)} \quad \text { or } \quad J_{p-1}(x)=J_{p+1}(x) .
+> $$
+>
+> (c) Illustrate (b) graphically when $p=2$.
+> (d) Show that at the zeros of $J_{p}, J_{p-1}$ and $J_{p+1}$ have equal absolute values but opposite signs.
+
+
+> [!prompt|e317d5a1-80f2-5573-8192-6d43bba6a659.local at=66f58b04-3d72-55e3-972b-7a0e87ab3bc1] Shared exercise instructions
+> In Exercises 3-10, evaluate the given integral.
+
+
+> [!exercise|36d48b21-96d7-558c-8535-3bc2c31e57d5.local at=ffa7608c-4e3c-5a5e-ac0a-e6c2a08a6dc9] Exercise 3
+> $\int x J_{0}(x) d x$.
+
+
+> [!exercise|f1b7177c-9921-5e83-8434-675867b66c0a.local at=aeecc9d5-d62e-50da-9867-a5a3d7d197e3] Exercise 4
+> $\int x^{4} J_{3}(x) d x$.
+
+
+> [!exercise|f4066001-dbf4-5245-84e1-3dff8e77a896.local at=9e49495f-4bad-5f64-a88e-246dbeb17f1f] Exercise 5
+> $\int J_{1}(x) d x$.
+
+
+> [!exercise|9d30b91c-afa1-5c00-9b21-4a585c3accb1.local at=b8d66353-8b08-5c66-a45f-e011d3741a3c] Exercise 6
+> $\int x^{-2} J_{3}(x) d x$.
+
+
+> [!exercise|188f476a-ed2a-5de8-b597-854a224e3b81.local at=a0d7154f-4964-56e1-b324-4f7573b03ef5] Exercise 7
+> $\int x^{3} J_{2}(x) d x$.
+
+
+> [!exercise|b50e169e-1caa-588f-a87f-7f01262c7ee7.local at=a0b3dabc-5625-519a-88c6-58abc1d676f3] Exercise 8
+> $\int x^{3} J_{0}(x) d x$.
+
+
+> [!exercise|0e6f52d0-1f1f-554b-a6bc-8961f1b20f05.local at=71ed4e3b-2c01-57a7-83e3-e1c7dd1047f3] Exercise 9
+> $\int J_{3}(x) d x$.
+
+
+> [!exercise|c75d8892-012f-5816-b17d-371ad60bacc6.local at=8867a9c9-977a-542d-942a-8704e06a356f] Exercise 10
+> For integers $n\ge0$, evaluate $\int_{0}^{\infty} J_{1}(x)\left[J_{0}(x)\right]^{n} d x$.
+> [Hint: Let $u=J_{0}(x)$.]
+
+
+> [!exercise|4800fddc-5902-5761-8a48-867bd9781903.local at=d560d62c-3edf-519f-b10e-f482d74cc65a] Exercise 11
+> Use (2) and Example 1 of Section 12.7 to derive the formula
+>
+> $$
+> J_{3 / 2}(x)=\sqrt{\frac{2}{\pi x}}\left[\frac{\sin x}{x}-\cos x\right]
+> $$
+
+
+> [!exercise|19978ffd-5400-5af9-8d4b-06a52ac1d06b.local at=20c39fed-01ed-564d-93e7-d2458fe55b5d] Exercise 12
+> Use (2) and Exercise 11 to derive
+>
+> $$
+> J_{5 / 2}(x)=\sqrt{\frac{2}{\pi x}}\left[\left(\frac{3}{x^{2}}-1\right) \sin x-\frac{3}{x} \cos x\right] .
+> $$
+
+
+> [!exercise|8477444e-b416-5b4a-a954-d8aa92dca71f.local at=0e8ec8ca-8b6e-5ebc-aaf2-ca3e325d3773] Exercise 13
+> Express $J_{5}$ in terms of $J_{0}$ and $J_{1}$.
+
+
+> [!exercise|4c400560-032d-5638-9b88-0fb9a138531c.local at=8409b65a-24ba-5c43-a553-6679b3f78aee] Exercise 14
+> Use the explicit formula for $J_{1 / 2}$ given in Example 1 of Section 12.7 to show that $J_{1 / 2}$ has infinitely many positive zeros in the interval $0<x<\infty$. What are these zeros?
+
+
+> [!exercise|73a839af-40bb-5776-a0e5-00572b95e58f.local at=5ab98f83-555d-516a-80dc-bf758c401217] Exercise 15
+> (a) Plot the functions $\frac{\sin x}{x}$ and $\cos x$ on the same graph to illustrate the fact that they intersect at infinitely many points. Conclude that the function $J_{3 / 2}(x)$ has infinitely many zeros in ( $0, \infty$ ).
+> (b) Approximate the first three roots of the equation $\frac{\sin x}{x}=\cos x$.
+
+
+> [!exercise|9285ee28-b9b1-5e3b-9546-5ec158e1604d.local at=5812ff4c-6aba-5355-b478-d87981b7f13e] Exercise 16
+> (a) Let $0<\alpha_{p 1}<\alpha_{p 2}<\cdots<\alpha_{p j}<\cdots$ denote the positive zeros of $J_{p}$. How many roots does the function $J_{p}\left(\frac{\alpha_{p j}}{a} x\right)$ have in the interval $0<x<a$ ? Justify your answer.
+> (b) Illustrate your answer graphically with $p=2, a=1$, and $j=5$.
+
+
+> [!exercise|9cea7478-f048-527b-a275-68b616a34d9e.local at=ddd7d9d5-0f5b-5a8a-9e55-827cf7049357] Exercise 17
+> Let $0<c<1$, and let
+>
+> $$
+> f(x)= \begin{cases}1 & \text { if } 0<x<c \\ 0 & \text { if } c<x<1\end{cases}
+> $$
+>
+> (a) Derive the Bessel series of order 0 of $f$
+>
+> $$
+> \sum_{j=1}^{\infty} \frac{2 c J_{1}\left(c \alpha_{j}\right)}{\alpha_{j} J_{1}\left(\alpha_{j}\right)^{2}} J_{0}\left(\alpha_{j} x\right), \quad 0<x<1
+> $$
+>
+> (b) Discuss the convergence of the series in the interval $0<x<1$.
+> (c) Take $c=\frac{1}{2}$. Investigate the convergence of the series at $x=0$ and $x=1$ numerically. Does the series seem to converge at one or both points? To what values? (Note that convergence at these points is not covered by Theorem 2.)
+
+
+> [!exercise|2658171b-ae87-5dce-9dee-20eac29c1ec9.local at=0c21e311-b617-5b66-ae97-a7f8a2efdc3e] Exercise 18
+> Take $c=\frac{1}{3}$ in Exercise 17 and write explicitly the first five terms of the series in this case. Plot several partial sums and describe the behavior at and around the point $x=\frac{1}{3}$. Observe how the partial sums overshoot their limiting values regardless of the increase in the number of terms in the approximating partial sums. This illustrates the Gibbs phenomenon at a point of discontinuity for Bessel series expansions.
+
+
+> [!exercise|5a50e55a-2462-5e1b-89e2-03cab897ea43.local at=c0ed7b1b-900d-5070-a1ed-512632bae505] Exercise 19
+> (a) Obtain the Bessel series expansion
+>
+> $$
+> x^{4}=2 \sum_{j=1}^{\infty} \frac{1}{\alpha_{j} J_{5}\left(\alpha_{j}\right)} J_{4}\left(\alpha_{j} x\right), \quad 0<x<1
+> $$
+>
+> where the $\alpha_{j}$ 's are the positive zeros of $J_{4}$.
+> (b) Plot some partial sums and discuss their behavior on the interval $0<x<1$.
+
+
+> [!exercise|d38c8e9c-1c21-56d2-9aa9-423147828af3.local at=da5b21d2-18d8-59ad-b636-2cb6d5663537] Exercise 20
+> Bessel series of order $m$. Fix a number $m \geq 0$ and let $0<\alpha_{1}<\alpha_{2}< \ldots<\alpha_{j}<\ldots$ denote the sequence of positive zeros of $J_{m}$. Obtain the Bessel series expansion
+>
+> $$
+> x^{m}=2 \sum_{j=1}^{\infty} \frac{1}{\alpha_{j} J_{m+1}\left(\alpha_{j}\right)} J_{m}\left(\alpha_{j} x\right), \quad 0<x<1
+> $$
+
+
+> [!exercise|4971b174-3d6b-56a5-a611-e6d2ab5a8923.local at=bd54340a-217d-5273-b698-4f22bb134dc8] Exercise 21
+> Refer to Exercise 20.
+> (a) Take $m=\frac{1}{2}$, and determine the exact values of the $\alpha_{j}$ 's in this case? [Hint: Example 1 of Section 12.7.]
+> (b) Compute explicitly the coefficients in the Bessel series expansion of $f(x)=\sqrt{x}$, $0<x<1$.
+> (c) Recall the formula for $J_{\frac{1}{2}}$ in terms of $\sin x$ and show that the expansion in (b) is really a sine Fourier series expansion of $x$.
+> (d) Plot some partial sums of the Bessel series and discuss the convergence on the interval $0<x<1$.
+
+
+> [!exercise|aeaf5750-efe0-55f9-a83e-0ae12bc683ba.local at=f5b62302-f35f-52ba-8913-db3461171c38] Exercise 22
+> Study the behavior of the partial sums of the Bessel series in Exercise 20 when $m=\frac{3}{2}$. What do they converge to in the interval $0<x<1$ ?
+
+
+> [!prompt|47989c3d-9583-55e0-b706-b57c8ea7e427.local at=2e1caaa0-083f-5e91-be0d-010b203b2a10] Shared exercise instructions
+> In Exercises 23-30, approximate the given function by a Bessel series of the given order $p$. Plot several partial sums of the series and discuss their convergence on the given interval.
+
+
+> [!exercise|e3b7ee49-78d5-579e-845e-731a90cbd7b2.local at=be29f5bc-bd01-586f-a21b-c99b130696f2] Exercise 23
+> $f(x)=x^{2} ; 0<x<1 ; p=2$.
+
+
+> [!exercise|5e5e2b84-ead0-5de4-a420-95762fb1e8d6.local at=c7c17f42-149b-55ad-b4ac-5b72091c06f8] Exercise 24
+> $f(x)=x^{3} ; 0<x<1 ; p=3$.
+
+
+> [!exercise|cf2e4756-0b3b-5058-b5c8-e9e43fc62b62.local at=4af54785-ddb6-5dfb-b9e3-1afddd6f0092] Exercise 25
+> $f(x)= \begin{cases}0 & \text { if } 0<x<\frac{1}{2}, \\ \frac{1}{x} & \text { if } \frac{1}{2}<x<1 ;\end{cases}$
+> $p=1$.
+
+
+> [!exercise|8792106c-de47-5db4-ac43-9ba352a38cc9.local at=e739199c-8c04-5810-b837-4f9cf9b5fbbe] Exercise 26
+> $f(x)=x^{2}, 0<x<1, p=0$.
+
+
+> [!exercise|06382f00-9ac8-587a-9276-6806a9194114.local at=d1e7c1aa-a7b1-5f20-9d97-a4534e0d89bc] Exercise 27
+> $f(x)= \begin{cases}0 & \text { if } 0<x<\frac{1}{2}, \\ \frac{1}{x^{2}} & \text { if } \frac{1}{2}<x<1 ;\end{cases}$
+> $p=2$.
+
+
+> [!exercise|1bb12c4e-3423-5451-896f-a867105be341.local at=e7fa07a2-7818-52f6-ad03-29c2f0970071] Exercise 28
+> $f(x)= \begin{cases}0 & \text { if } 0<x<\frac{1}{30}, \\ \frac{1}{x^{3}} & \text { if } \frac{1}{30}<x<1 ;\end{cases}$
+> $p=3$.
+
+
+> [!exercise|54069e38-aa0d-591f-9903-7cc9cbb2d6eb.local at=077ca7e5-d778-5d16-b631-20905591aece] Exercise 29
+> $f(x)=1 ; 0<x<2 ; p=1$.
+
+
+> [!exercise|82b82cc3-d99d-5994-8a59-9944719bd142.local at=475a8e5e-6e0c-574c-9246-ad9a6e2671f2] Exercise 30
+> $f(x)=J_{0}(x) ; 0<x<\alpha_{01} ; p=0$.
+
+
+> [!prompt|9e53b6a2-e0f3-5788-a358-b4864047897c.local at=1be8c396-ee97-52fc-b170-30d4a4585760] Shared exercise instructions
+> In Exercises 31-34, find all $\lambda>0$ for which the given parametric form of Bessel's equation has a solution that is finite at $x=0$ and satisfies the given boundary condition.
+
+
+> [!exercise|01bb5fb7-9ef2-5c83-a0cf-ff9ef9a4662d.local at=af9e752a-5d0e-54cc-9081-b1913902b309] Exercise 31
+> $x^{2} y^{\prime \prime}(x)+x y^{\prime}(x)+\left(\lambda^{2} x^{2}-1\right) y(x)=0, \quad y(1)=0$.
+
+
+> [!exercise|54c9b130-d866-5358-90d6-dfedd02db662.local at=9254fe42-74cc-5117-9bf4-9c0d83e7dcc4] Exercise 32
+> $x^{2} y^{\prime \prime}(x)+x y^{\prime}(x)+\lambda^{2} x^{2} y(x)=0, \quad y(2)=0$.
+
+
+> [!exercise|9424c5cb-7422-55a1-bb20-e23dc1a58b73.local at=763ecf28-c6bd-558b-ad2f-69f67e0429bd] Exercise 33
+> $x^{2} y^{\prime \prime}(x)+x y^{\prime}(x)+\left(\lambda^{2} x^{2}-\frac{1}{4}\right) y(x)=0, \quad y(\pi)=0$.
+
+
+> [!exercise|860b783a-667d-5dd1-b3b6-8cc53155b34c.local at=8580d8f6-f848-5723-97a9-cc42c2b4c021] Exercise 34
+> $x^{2} y^{\prime \prime}(x)+x y^{\prime}(x)+\left(\lambda^{2} x^{2}-1\right) y(x)=0, \quad y\left(\frac{\pi}{2}\right)=0$.
+
+
+> [!exercise|8c0e7725-1188-5196-839d-923bbff880e6.local at=ef488119-d223-53d4-960f-76896f704dad] Exercise 35
+> Project Problem: Zeros of $\boldsymbol{J}_{\boldsymbol{n}}$. We will prove that the positive zeros of $J_{n}(x)(n=0, \pm 1, \pm 2, \ldots)$ form an increasing sequence
+>
+> $$
+> 0<\alpha_{n 1}<\alpha_{n 2}<\cdots<\alpha_{n k}<\cdots \rightarrow \infty
+> $$
+>
+> Parts (a)-(g) deal with the case $n=0$.
+> (a) Plot the graph of $J_{0}(x)$ and note that there are infinitely many positive zeros that we will denote in ascending order by $0<\alpha_{1}<\alpha_{2}<\alpha_{3}<\ldots$
+> (b) Show that the substitution $y(x)=\frac{1}{\sqrt{x}} u(x)$ transforms Bessel's equation of order 0 into
+>
+> $$
+> u^{\prime \prime}+\left(1+\frac{1}{4 x^{2}}\right) u=0
+> $$
+>
+> Conclude that $u(x)=\sqrt{x} J_{0}(x)$ is a solution of this differential equation.
+> (c) Let $v(x)=\sin x$. Check that
+>
+> $$
+> -\left(u^{\prime \prime}+u\right) v(x)=\frac{d}{d x}\left(u v^{\prime}-u^{\prime} v\right)
+> $$
+>
+> (d) Using (b), show that $-\left(u^{\prime \prime}+u\right)=\frac{u}{4 x^{2}}$.
+> (e) For integers $k\ge1$, show that $\int \frac{u(x) v(x)}{4 x^{2}} d x=u v^{\prime}-u^{\prime} v+C$ and hence
+>
+> $$
+> \int_{2 k \pi}^{(2 k+1) \pi} \frac{u(x) \sin x}{4 x^{2}} d x=-[u(2 k \pi)+u(2 k \pi+\pi)]
+> $$
+>
+> (f) Conclude from (e) that $u(x)$ has at least one zero in $[2 k \pi,(2 k+1) \pi]$. [Hint: Assume the contrary, say $u(x)>0$ for all $x$ in the interval, and get a contradiction by studying the signs of the terms on both sides of the last equality in (e).]
+> (g) Conclude that $J_{0}(x)$ has infinitely many positive zeros.
+> (h) Suppose that $f$ and $g$ are differentiable functions such that $\frac{d}{d x} f(x)=g(x)$. Show that between any two zeros of $f$ there is at least one zero of $g$.
+> (i) Use (2) with $p=0$ to show that $J_{1}$ has infinitely many zeros that tend to $\infty$.
+> (j) Use (2) and induction to show that $J_{n}(n>0)$ has infinitely many zeros that tend to $\infty$. Prove this result for all integers $n$.
+
+
+> [!exercise|a17c3cd0-1375-5783-b078-2d26bf9e55ef.local at=746129cc-059c-5843-8282-63cadb1d6bd9] Exercise 36
+> Project Problem: A proof of (12). Let $0<\alpha_{1}<\alpha_{2}<\cdots<\alpha_{k}<\cdots$ denote the sequence of zeros of $J_{p}$ in ( $0, \infty$ ), and let $\lambda_{k}=\frac{\alpha_{k}}{a}$.
+> (a) Rewrite (18) as
+>
+> $$
+> \left(x y^{\prime}\right)^{\prime}+\left(\lambda^{2} x-\frac{p^{2}}{x}\right) y=0, \quad y(a)=0
+> $$
+>
+> Multiply both sides of the equation by $x y^{\prime}$ and put it in the form
+>
+> $$
+> \left[\left(x y^{\prime}\right)^{2}\right]^{\prime}+\left(\lambda^{2} x^{2}-p^{2}\right)\left(y^{2}\right)^{\prime}=0
+> $$
+>
+> (b) Take $y=J_{p}\left(\lambda_{k} x\right)$ and $\lambda=\lambda_{k}$, integrate the equation in (a) over $0<x<a$, and obtain
+>
+> $$
+> \left[a y^{\prime}(a)\right]^{2}+\left(\lambda^{2} a^{2}-p^{2}\right) y(a)^{2}-2 \lambda^{2} \int_{0}^{a} y(x)^{2} x d x=0
+> $$
+>
+> [Hint: Use integration by parts on the second term in (a). Justify the equality $p y(0)=0$.]
+> (c) For $y=J_{p}\left(\lambda_{k} x\right)$ and $\lambda=\lambda_{k}$, justify the equality $y(a)=0$, and get
+>
+> $$
+> \left[y^{\prime}(a)\right]^{2}=\frac{2 \lambda^{2}}{a^{2}} \int_{0}^{a} x[y(x)]^{2} d x
+> $$
+>
+> (d) For $y=J_{p}\left(\lambda_{k} x\right)$, use (4) to show that $y^{\prime}(a)=-\lambda_{k} J_{p+1}\left(\alpha_{k}\right)$. Derive (12) from (c).
+
 
 ## Spherical Bessel Functions
 
-37. Use (21) to transform (20) into one of the equations of the form (18).
-38. Use (23) and explicit formulas for the Bessel functions to show that
-
-$$
-\begin{gathered}
-j_{0}(x)=\frac{\sin x}{x} \\
-j_{1}(x)=\frac{\sin x-x \cos x}{x^{2}} \\
-j_{2}(x)=\frac{\left(3-x^{2}\right) \sin x-3 x \cos x}{x^{3}} .
-\end{gathered}
-$$
-
-[Hint: See Exercises 11 and 12.]
-In Exercises 39-42, derive the given recurrence relation for the spherical Bessel functions. [Hint: Use (23) and the corresponding formulas for the Bessel functions.]
-39. $\frac{d}{d x}\left[x^{n+1} j_{n}(x)\right]=x^{n+1} j_{n-1}(x)$.
-40. $\frac{d}{d x}\left[x^{-n} j_{n}(x)\right]=-x^{-n} j_{n+1}(x)$.
-41. $\int x^{n+2} j_{n}(x) d x=x^{n+2} j_{n+1}(x)+C$.
-42. $\int x^{-n+1} j_{n}(x) d x=-x^{-n+1} j_{n-1}(x)+C$.
-43. Recurrence relations. Use the results of Exercises 39 and 40 to obtain that
-
-$$
-j_{n-1}(x)+j_{n+1}(x)=\frac{2 n+1}{x} j_{n}(x)
-$$
-
-and
-
-$$
-n j_{n-1}(x)-(n+1) j_{n+1}(x)=(2 n+1) j_{n}^{\prime}(x) .
-$$
-
-44. Use the results of Exercises 43 and 38 to obtain that
-
-$$
-j_{3}(x)=\frac{\left(15-6 x^{2}\right) \sin x-\left(15 x-x^{3}\right) \cos x}{x^{4}} .
-$$
-
-45. Orthogonality of the spherical Bessel functions. Use (11) and (12) to show that
-
-$$
-\int_{0}^{a} j_{n}\left(\lambda_{n, j} x\right) j_{n}\left(\lambda_{n, j^{\prime}} x\right) x^{2} d x=0 \quad \text { for } j \neq j^{\prime}
-$$
-
-and
-
-$$
-\int_{0}^{a} j_{n}^{2}\left(\lambda_{n, j} x\right) x^{2} d x=\frac{a^{3}}{2} j_{n+1}^{2}\left(\alpha_{n+\frac{1}{2}, j}\right)
-$$
-
-where $\alpha_{n+\frac{1}{2}, j}$ is the $j$ th positive zero of $j_{n}$ (equivalently, of $J_{n+\frac{1}{2}}$ ). Hence the spherical Bessel functions are orthogonal on the interval $[0, a]$ with respect to the weight function $x^{2}$.
+> [!exercise|6ca7e14c-512b-5fb7-a660-afcc438a7df4.local at=977d0950-1fea-538e-97c4-b6e07b44bbbf] Exercise 37
+> Use (21) to transform (20) into one of the equations of the form (18).
+
+
+> [!exercise|061b61b3-7782-577f-9f0a-f16e139fa46f.local at=52341c9c-c1d8-5591-9d8c-98f579007715] Exercise 38
+> Use (23) and explicit formulas for the Bessel functions to show that
+>
+> $$
+> \begin{gathered}
+> j_{0}(x)=\frac{\sin x}{x} \\
+> j_{1}(x)=\frac{\sin x-x \cos x}{x^{2}} \\
+> j_{2}(x)=\frac{\left(3-x^{2}\right) \sin x-3 x \cos x}{x^{3}} .
+> \end{gathered}
+> $$
+>
+> [Hint: See Exercises 11 and 12.]
+
+
+> [!prompt|de09c1e5-2cb9-5dbe-910e-749a9f21862d.local at=617e3c69-a446-5689-adc0-e5284af3c5d3] Shared exercise instructions
+> In Exercises 39-42, derive the given recurrence relation for the spherical Bessel functions. [Hint: Use (23) and the corresponding formulas for the Bessel functions.]
+
+
+> [!exercise|583eb309-0906-5a22-9d18-073a31226987.local at=2174a7c0-bd98-5bfc-bb43-11660fdc146d] Exercise 39
+> $\frac{d}{d x}\left[x^{n+1} j_{n}(x)\right]=x^{n+1} j_{n-1}(x)$.
+
+
+> [!exercise|abf95d1c-451b-50a3-99fb-11921e91a328.local at=6a78f54f-f7b1-51cf-bc59-8a851d869e5b] Exercise 40
+> $\frac{d}{d x}\left[x^{-n} j_{n}(x)\right]=-x^{-n} j_{n+1}(x)$.
+
+
+> [!exercise|09975cb9-e5d1-5d07-b842-ae1a1b4cc216.local at=38c9a24a-e8c6-5dc5-8d56-f636e353a67f] Exercise 41
+> $\int x^{n+2} j_{n}(x) d x=x^{n+2} j_{n+1}(x)+C$.
+
+
+> [!exercise|7a26dfac-6271-5bc1-b850-66ff88740b05.local at=92241a3a-f8f4-577f-ab64-406669ccdab3] Exercise 42
+> $\int x^{-n+1} j_{n}(x) d x=-x^{-n+1} j_{n-1}(x)+C$.
+
+
+> [!exercise|4a97e488-d699-5f99-b30e-9d99bc64a6b9.local at=1daf72f5-9d43-5962-a611-1bec25965442] Exercise 43
+> Recurrence relations. Use the results of Exercises 39 and 40 to obtain that
+>
+> $$
+> j_{n-1}(x)+j_{n+1}(x)=\frac{2 n+1}{x} j_{n}(x)
+> $$
+>
+> and
+>
+> $$
+> n j_{n-1}(x)-(n+1) j_{n+1}(x)=(2 n+1) j_{n}^{\prime}(x) .
+> $$
+
+
+> [!exercise|34f78205-d69b-5802-8a0e-2bbd1b5cb82e.local at=4b72e5aa-bf94-5c6c-9a88-467b949e3bb6] Exercise 44
+> Use the results of Exercises 43 and 38 to obtain that
+>
+> $$
+> j_{3}(x)=\frac{\left(15-6 x^{2}\right) \sin x-\left(15 x-x^{3}\right) \cos x}{x^{4}} .
+> $$
+
+
+> [!exercise|b89c72c9-5705-5749-bf2b-42ca0b72ce41.local at=82d48664-7fdc-5b1a-a890-b3cbcb26873c] Exercise 45
+> Orthogonality of the spherical Bessel functions. Use (11) and (12) to show that
+>
+> $$
+> \int_{0}^{a} j_{n}\left(\lambda_{n, j} x\right) j_{n}\left(\lambda_{n, j^{\prime}} x\right) x^{2} d x=0 \quad \text { for } j \neq j^{\prime}
+> $$
+>
+> and
+>
+> $$
+> \int_{0}^{a} j_{n}^{2}\left(\lambda_{n, j} x\right) x^{2} d x=\frac{a^{3}}{2} j_{n+1}^{2}\left(\alpha_{n+\frac{1}{2}, j}\right)
+> $$
+>
+> where $\alpha_{n+\frac{1}{2}, j}$ is the $j$ th positive zero of $j_{n}$ (equivalently, of $J_{n+\frac{1}{2}}$ ). Hence the spherical Bessel functions are orthogonal on the interval $[0, a]$ with respect to the weight function $x^{2}$.

`````
