
# Editorial records

Reading note: 12.3 Vibrations of a Circular Membrane: General Case.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

No recovery content changes were needed in this note. Existing genuine corrections and formatting were retained.

## Additional source comparison

## 1. Move the remaining editorial notice into the separate record.

### Before

````text
[Source-data qualification: the displayed initial displacement has no unique limit at the center. Interpret this exercise through the generalized expansion, rather than as a smooth classical membrane displacement at $r=0$.]
````
### After

````text

````

## Source-to-current comparison

Source: /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 12 Partial Differential Equations in Polar and Cylindrical Coordinates/12.3 Vibrations of a Circular Membrane: General Case.md

This exact comparison preserves the full change evidence, including formatting, OCR corrections, restored source wording, and required standalone context. The entries above explain the recovery edits. The comparison is not a claim that every difference is a correction; component serialization, callout wrapping, and printed labels outside callouts are formatting.

`````diff
--- /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 12 Partial Differential Equations in Polar and Cylindrical Coordinates/12.3 Vibrations of a Circular Membrane: General Case.md
+++ /Users/gradyclopton/ObsidianVaults/complex_analysis/Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 12 Partial Differential Equations in Polar and Cylindrical Coordinates/12.3 Vibrations of a Circular Membrane: General Case.md
@@ -1,27 +1,32 @@
+
 ### 12.3 Vibrations of a Circular Membrane: General Case
 
 We continue our study of the vibrating circular membrane, now without any symmetry assumptions. We will solve the two dimensional wave equation in polar coordinates:
 
 $$
 \frac{\partial^{2} u}{\partial t^{2}}=c^{2}\left(\frac{\partial^{2} u}{\partial r^{2}}+\frac{1}{r} \frac{\partial u}{\partial r}+\frac{1}{r^{2}} \frac{\partial^{2} u}{\partial \theta^{2}}\right)
+\tag{1}
 $$
 
 where $0<r<a, 0<\theta<2 \pi, t>0$. Here $u=u(r, \theta, t)$ denotes the deflection of the membrane at the point $(r, \theta)$ at time $t$. The initial conditions (displacement and velocity) are
 
 $$
 u(r, \theta, 0)=f(r, \theta), \quad \frac{\partial u}{\partial t}(r, \theta, 0)=g(r, \theta)
+\tag{2}
 $$
 
 $0<r<a, 0<\theta<2 \pi$. The requirement that the edges of the membrane be held fixed translates into the boundary condition
 
 $$
 u(a, \theta, t)=0, \quad 0<\theta<2 \pi, t>0
+\tag{3}
 $$
 
 Since $\theta$ is a polar angle, ( $r, \theta$ ) and ( $r, \theta+2 \pi$ ) represent the same point, and hence $u(r, \theta, t)=u(r, \theta+2 \pi, t)$. In other words, $u$ is $2 \pi$-periodic in $\theta$. Consequently,
 
 $$
 u(r, 0, t)=u(r, 2 \pi, t) \quad \text { and } \quad \frac{\partial u}{\partial \theta}(r, 0, t)=\frac{\partial u}{\partial \theta}(r, 2 \pi, t) .
+\tag{4}
 $$
 
 ## Separation of Variables
@@ -88,12 +93,14 @@
 
 $$
 u_{m n}(r, \theta, t)=J_{m}\left(\lambda_{m n} r\right)\left(a_{m n} \cos m \theta+b_{m n} \sin m \theta\right) \cos c \lambda_{m n} t
+\tag{5}
 $$
 
 and
 
 $$
 u_{m n}^{*}(r, \theta, t)=J_{m}\left(\lambda_{m n} r\right)\left(a_{m n}^{*} \cos m \theta+b_{m n}^{*} \sin m \theta\right) \sin c \lambda_{m n} t
+\tag{6}
 $$
 
 where $m=0,1,2, \ldots, n=1,2, \ldots$. Note that we have replaced the coefficient $A_{m} A_{m n}$ by $a_{m n}$, and similarly for $b_{m n}, a_{m n}^{*}$, and $b_{m n}^{*}$. While this may appear to be just relabeling of the unknown coefficients, in fact, it provides a more convenient choice of solutions that will be needed as we proceed. Note too that $b_{0 n}$ and $b_{0 n}^{*}$ will never be needed, since $\sin m \theta=0$ when $m=0$, and so for the sake of definiteness we take them to be 0 .
@@ -102,10 +109,12 @@
 
 The superposition principle suggests adding all the functions in (5) and (6). The resulting sum is displayed in (16) below. Because of the complexity of this solution, we consider two cases separately: one in which the initial velocity $g$ is zero, and a second in which the initial displacement $f$ is zero. The general solution is then obtained by combining these two cases.
 
-## EXAMPLE 1 Vibrations of a membrane with zero initial velocity
-
-Solve the boundary value problem consisting of (1)-(3) given that $g=0$.
-Solution The initial conditions in this case are
+> [!exercise|d152b197-97d4-5784-88a1-8426fb9e4976.local at=35092c65-a3e0-5bcc-ad6e-d4b311f913a2] EXAMPLE 1 Vibrations of a membrane with zero initial velocity
+> Solve the boundary value problem consisting of (1)-(3) given that $g=0$.
+
+##### solution
+
+The initial conditions in this case are
 
 $$
 u(r, \theta, 0)=f(r, \theta), \quad \frac{\partial u}{\partial t}(r, \theta, 0)=0, \quad 0<r<a, 0<\theta<2 \pi .
@@ -115,12 +124,14 @@
 
 $$
 u(r, \theta, t)=\sum_{m=0}^{\infty} \sum_{n=1}^{\infty} J_{m}\left(\lambda_{m n} r\right)\left(a_{m n} \cos m \theta+b_{m n} \sin m \theta\right) \cos c \lambda_{m n} t
+\tag{7}
 $$
 
 Setting $t=0$, we get
 
 $$
 f(r, \theta)=\sum_{m=0}^{\infty} \sum_{n=1}^{\infty} J_{m}\left(\lambda_{m n} r\right)\left(a_{m n} \cos m \theta+b_{m n} \sin m \theta\right) .
+\tag{8}
 $$
 
 This surely is a sort of a generalized Fourier series of $f(r, \theta)$ in terms of the functions $J_{m}\left(\lambda_{m n} r\right) \cos m \theta$ and $J_{m}\left(\lambda_{m n} r\right) \sin m \theta$, and hence $a_{m n}$ and $b_{m n}$ are the corresponding generalized Fourier coefficients of the function $f$. This fact and many important related applications are explored in Section 12.6 (see in particular Theorems 1 and 2 of that section). We now proceed to determine $a_{m n}$ and $b_{m n}$, using properties of the usual Fourier series and Bessel series.
@@ -135,7 +146,7 @@
 \end{aligned}
 $$
 
-Now we see clearly that (for fixed $r$ ) $a_{0}(r), a_{m}(r)$, and $b_{m}(r)$ are the Fourier coefficients in the Fourier series expansion of $\theta \mapsto f(r, \theta)$. Using (2)-(4), Section 2.2, we
+Now we see clearly that (for fixed $r$ ) $a_{0}(r), a_{m}(r)$, and $b_{m}(r)$ are the Fourier coefficients in the Fourier series expansion of $\theta \mapsto f(r, \theta)$. Using (2)-(4), Section 7.2, we
 conclude that
 
 $$
@@ -146,6 +157,8 @@
 \end{gathered}
 $$
 
+*Printed equation labels: (9) angular mean $a_0(r)$; (10) angular cosine coefficients $a_m(r)$; (11) angular sine coefficients $b_m(r)$.*
+
 for $m=1,2, \ldots$. Now let $r$ vary and think of the last three series as the Bessel series expansions of order $m=0,1,2, \ldots$ of the functions $a_{0}(r), a_{m}(r)$, and $b_{m}(r)$, respectively. The coefficients in these series are Bessel coefficients and so from (17), Section 12.8, we obtain
 
 $$
@@ -166,17 +179,20 @@
 \end{gathered}
 $$
 
+*Printed equation labels: (12) coefficients $a_{0n}$; (13) coefficients $a_{mn}$; (14) coefficients $b_{mn}$.*
+
 for $m, n=1,2 \ldots$. Substituting these coefficients in (7) completes the solution of the problem. $\square$
 
 Before giving a numerical application, we present a useful identity involving Bessel functions.
 
-## A USEFUL IDENTITY
-
-For any $k \geq 0, a>0$, and $\alpha>0$, we have
-
-$$
-\int_{0}^{a}\left(a^{2}-r^{2}\right) r^{k+1} J_{k}\left(\frac{\alpha}{a} r\right) d r=2 \frac{a^{k+4}}{\alpha^{2}} J_{k+2}(\alpha)
-$$
+> [!identity|af8d9359-9d57-580d-97d9-457e815c37d6.local at=c9cc37cd-01bf-5bf0-aded-7a850779c2ae] Definite Bessel integral with a quadratic radial weight
+> For the Bessel functions of the first kind $J_k,J_{k+2}$ and any $k \geq 0, a>0$, and $\alpha>0$, we have
+>
+> $$
+> \int_{0}^{a}\left(a^{2}-r^{2}\right) r^{k+1} J_{k}\left(\frac{\alpha}{a} r\right) d r=2 \frac{a^{k+4}}{\alpha^{2}} J_{k+2}(\alpha)
+> $$
+
+*Printed equation label: (15).*
 
 Proof We first make a change of variables, $\frac{\alpha}{a} r=x, d r=\frac{a}{\alpha} d x$, and transform the integral into
 
@@ -187,9 +203,6 @@
 \end{aligned}
 $$
 
-![](./images/1c611338-958a-44f7-9d79-2dde87e6ac2a-20_285_455_1666_59.jpg)
-Figure $1 J_{1}(r)$ and its first four positive zeros.
-
 From (7), Section 12.8, with $p=k$, the first term is
 
 $$
@@ -210,10 +223,26 @@
 
 and (15) follows.
 
-## EXAMPLE 2 A vibrating membrane
-
-Refer to Example 1 and determine the solution $u(r, \theta, t)$ when $a=c=1, f(r, \theta)= \left(1-r^{2}\right) r \sin \theta, g(r, \theta)=0$.
-Solution From (12), we have
+```scientific-figure
+id: f9bd6639-5185-4318-92f8-d4f720a3e0cc
+numbered: false
+title: ""
+caption: Figure 1 $J_1(r)$ and its first four positive zeros.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 12 Partial Differential Equations in Polar and Cylindrical Coordinates/images/1c611338-958a-44f7-9d79-2dde87e6ac2a-20_285_455_1666_59.jpg
+    caption: ""
+```
+
+
+> [!exercise|3fad4afb-7c2a-54a3-927d-9d8cb9f20377.local at=92a0fcb7-4b66-5d62-8997-71f0b0dde389] EXAMPLE 2 A vibrating membrane
+> Refer to Example 1 and determine the solution $u(r, \theta, t)$ when $a=c=1, f(r, \theta)= \left(1-r^{2}\right) r \sin \theta, g(r, \theta)=0$.
+
+##### solution
+
+From (12), we have
 
 $$
 a_{0 n}=\frac{1}{\pi J_{1}^{2}\left(\alpha_{0 n}\right)} \int_{0}^{1} \int_{0}^{2 \pi}\left(1-r^{2}\right) r \sin \theta J_{0}\left(\alpha_{0 n} r\right) r d \theta d r=0
@@ -242,48 +271,73 @@
 
 With the help of a computer system we found approximate numerical values of the first three coefficients in the series and plotted in Figure 2 the partial sum of the series solution (with $n$ up to 3) at various values of $t$.
 
-![](./images/1c611338-958a-44f7-9d79-2dde87e6ac2a-21_766_1683_190_10.jpg)
-Figure 2 Vibrating circular membrane: a nonradially symmetric case.
+```scientific-figure
+id: e574e6a6-a219-41ac-950d-f1e6bc15da5d
+numbered: false
+title: ""
+caption: "Figure 2 Vibrating circular membrane: a nonradially symmetric case."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 12 Partial Differential Equations in Polar and Cylindrical Coordinates/images/1c611338-958a-44f7-9d79-2dde87e6ac2a-21_766_1683_190_10.jpg
+    caption: ""
+```
+
 
 To complete the solution of the vibrating membrane, we need to treat the case of a nonzero initial velocity. Save for some minor differences, this case is similar to the one we just treated. The proof is outlined in Exercises 7 and 8 . For ease of reference, we state the entire solution for this case in the following box.
 
-## THE WAVE EQUATION IN POLAR COORDINATES: GENERAL CASE
-
-The solution of the boundary value problem (1)-(3) is given by
-
-$$
-u(r, \theta, t)=\sum_{m=0}^{\infty} \sum_{n=1}^{\infty} J_{m}\left(\lambda_{m n} r\right)\left(a_{m n} \cos m \theta+b_{m n} \sin m \theta\right) \cos c \lambda_{m n} t
-$$
-
-$$
-+\sum_{m=0}^{\infty} \sum_{n=1}^{\infty} J_{m}\left(\lambda_{m n} r\right)\left(a_{m n}^{*} \cos m \theta+b_{m n}^{*} \sin m \theta\right) \sin c \lambda_{m n} t
-$$
-
-where $\lambda_{m n}=\frac{\alpha_{m n}}{a} ; \alpha_{m n}$ is the $n$th positive zero of $J_{m} ; a_{m n}, b_{m n}$ are given by (12)-(14); and
-
-$$
-a_{0 n}^{*}=\frac{1}{\pi c \alpha_{0 n} a J_{1}^{2}\left(\alpha_{0 n}\right)} \int_{0}^{a} \int_{0}^{2 \pi} g(r, \theta) J_{0}\left(\lambda_{0 n} r\right) r d \theta d r
-$$
-
-$$
-a_{m n}^{*}=\frac{2}{\pi c \alpha_{m n} a J_{m+1}^{2}\left(\alpha_{m n}\right)} \int_{0}^{a} \int_{0}^{2 \pi} g(r, \theta) \cos m \theta J_{m}\left(\lambda_{m n} r\right) r d \theta d r
-$$
-
-$$
-b_{m n}^{*}=\frac{2}{\pi c \alpha_{m n} a \cdot J_{m+1}^{2}\left(\alpha_{m n}\right)} \int_{0}^{a} \int_{0}^{2 \pi} g(r, \theta) \sin m \theta \cdot J_{m}\left(\lambda_{m n} r\right) r d \theta d r
-$$
-
-for $m, n=1,2, \ldots$.
-
-## EXAMPLE 3 Nonzero initial displacement and velocity
-
-Determine the solution $u(r, \theta, t)$ of (1)-(3) when
-
-$$
-a=c=1, f(r, \theta)=\left(1-r^{2}\right) r \sin \theta, g(r, \theta)=\left(1-r^{2}\right) r^{2} \sin 2 \theta
-$$
-
-Solution The solution is given by (16). We only need to compute the second double series since the first one is computed in Example 2. Using the orthogonality of the trigonometric functions and arguing as we did in Example 2, we find that $a_{m n}^{*}=0$ for all $m$ and $n$, and $b_{m n}^{*}=0$, except when $m=2$. To compute $b_{2 n}^{*}$, we use (19) with $g(r, \theta)=\left(1-r^{2}\right) r^{2} \sin 2 \theta, a=c=1$, and $\lambda_{m n}=\alpha_{m n}$, and get
+> [!equation|862493e4-3880-5679-882b-4991975f7421.local at=c892da15-c887-5400-a40f-75f44457dec3] Fourier–Bessel solution for a clamped circular membrane with general initial data
+> Let $a,c>0$. Consider $u_{tt}=c^2(u_{rr}+r^{-1}u_r+r^{-2}u_{\theta\theta})$ on the disk $0<r<a$, with $u(a,\theta,t)=0$, angular $2\pi$-periodicity, regularity at the center, and initial data $u(r,\theta,0)=f(r,\theta)$, $u_t(r,\theta,0)=g(r,\theta)$. The solution has the Fourier–Bessel expansion
+>
+> $$
+> u(r, \theta, t)=\sum_{m=0}^{\infty} \sum_{n=1}^{\infty} J_{m}\left(\lambda_{m n} r\right)\left(a_{m n} \cos m \theta+b_{m n} \sin m \theta\right) \cos c \lambda_{m n} t
+> $$
+>
+> $$
+> +\sum_{m=0}^{\infty} \sum_{n=1}^{\infty} J_{m}\left(\lambda_{m n} r\right)\left(a_{m n}^{*} \cos m \theta+b_{m n}^{*} \sin m \theta\right) \sin c \lambda_{m n} t
+> $$
+>
+> where $\lambda_{m n}=\frac{\alpha_{m n}}{a} ; \alpha_{m n}$ is the $n$th positive zero of $J_{m} ; a_{mn},b_{mn}$ are the displacement coefficients defined below; and
+>
+> $$
+> a_{0 n}^{*}=\frac{1}{\pi c \alpha_{0 n} a J_{1}^{2}\left(\alpha_{0 n}\right)} \int_{0}^{a} \int_{0}^{2 \pi} g(r, \theta) J_{0}\left(\lambda_{0 n} r\right) r d \theta d r
+> $$
+>
+> $$
+> a_{m n}^{*}=\frac{2}{\pi c \alpha_{m n} a J_{m+1}^{2}\left(\alpha_{m n}\right)} \int_{0}^{a} \int_{0}^{2 \pi} g(r, \theta) \cos m \theta J_{m}\left(\lambda_{m n} r\right) r d \theta d r
+> $$
+>
+> $$
+> b_{m n}^{*}=\frac{2}{\pi c \alpha_{m n} a \cdot J_{m+1}^{2}\left(\alpha_{m n}\right)} \int_{0}^{a} \int_{0}^{2 \pi} g(r, \theta) \sin m \theta \cdot J_{m}\left(\lambda_{m n} r\right) r d \theta d r
+> $$
+>
+> Here $n\ge1$ throughout, and $m\ge1$ in the formulas involving $a^*_{mn}$ and $b^*_{mn}$. Set $b_{0n}=b^*_{0n}=0$.
+>
+>
+>
+> The displacement coefficients are
+> $$
+> \begin{aligned}
+> a_{0n}&=\frac{1}{\pi a^2J_1(\alpha_{0n})^2}\int_0^a\int_0^{2\pi}f(r,\theta)J_0(\lambda_{0n}r)r\,d\theta\,dr,\\
+> a_{mn}&=\frac{2}{\pi a^2J_{m+1}(\alpha_{mn})^2}\int_0^a\int_0^{2\pi}f(r,\theta)\cos(m\theta)J_m(\lambda_{mn}r)r\,d\theta\,dr,\\
+> b_{mn}&=\frac{2}{\pi a^2J_{m+1}(\alpha_{mn})^2}\int_0^a\int_0^{2\pi}f(r,\theta)\sin(m\theta)J_m(\lambda_{mn}r)r\,d\theta\,dr,
+> \end{aligned}
+> $$
+> with $m,n\ge1$ in the last two lines. The functions $J_m$ are Bessel functions of the first kind. For square-integrable initial data on the disk the formula is interpreted as an eigenfunction expansion; pointwise differentiation requires additional smoothness and compatibility with the clamped edge and center regularity.
+
+*Printed equation labels: (16) full displacement solution; (17) velocity coefficients $a^*_{0n}$; (18) velocity coefficients $a^*_{mn}$; (19) velocity coefficients $b^*_{mn}$.*
+
+> [!exercise|ffae5f99-1f35-5762-abd4-fb8f93b365f8.local at=e7782d03-abf9-5ede-b947-7fe2ec6a883c] EXAMPLE 3 Nonzero initial displacement and velocity
+> Determine the solution $u(r, \theta, t)$ of (1)-(3) when
+>
+> $$
+> a=c=1, f(r, \theta)=\left(1-r^{2}\right) r \sin \theta, g(r, \theta)=\left(1-r^{2}\right) r^{2} \sin 2 \theta
+> $$
+
+##### solution
+
+The solution is given by (16). We only need to compute the second double series since the first one is computed in Example 2. Using the orthogonality of the trigonometric functions and arguing as we did in Example 2, we find that $a_{m n}^{*}=0$ for all $m$ and $n$, and $b_{m n}^{*}=0$, except when $m=2$. To compute $b_{2 n}^{*}$, we use (19) with $g(r, \theta)=\left(1-r^{2}\right) r^{2} \sin 2 \theta, a=c=1$, and $\lambda_{m n}=\alpha_{m n}$, and get
 
 $$
 \begin{aligned}
@@ -311,84 +365,124 @@
 
 In the exercises, we will use the methods of this section to solve the general heat problem on the disk.
 
-## Exercises 4.3
-
-In Exercises 1-8, solve the vibrating membrane problem (1)-(3) for the given data. If possible, with the help of a computer, find numerical values for the first five nonzero coefficients of the series solution and plot the shape of the membrane at various values of $t$. (Formula (15) is helpful in doing these problems.)
-
-1. $f(r, \theta)=\left(1-r^{2}\right) r^{2} \sin 2 \theta, g(r, \theta)=0, a=c=1$.
-2. $f(r, \theta)=\left(9-r^{2}\right) \cos 2 \theta, g(r, \theta)=0, a=3, c=1$.
-3. $f(r, \theta)=\left(4-r^{2}\right) r \sin \theta, g(r, \theta)=1, a=2, c=1$.
-4. $f(r, \theta)=J_{3}\left(\alpha_{32} r\right) \sin 3 \theta, g(r, \theta)=0, a=c=1$.
-5. $f(r, \theta)=0, g(r, \theta)=\left(1-r^{2}\right) r^{2} \sin 2 \theta, a=c=1$.
-6. $f(r, \theta)=1-r^{2}, g(r, \theta)=J_{0}(r), a=c=1$.
-7. Project Problem: Circular membrane with zero initial displacement. Follow the steps outlined in this exercise to determine the vibrations of a circular membrane with radius $a$ and fixed boundary, given that the initial displacement of the membrane is 0 , and its initial velocity is $g(r, \theta)$. Review the solution of Example 1 for hints.
-(a) Write down explicitly the differential equation, the boundary conditions, and the initial conditions.
-(b) Assume a product solution of the form $R(r) \Theta(\theta) T(t)$ and show that $T(0)=0$. Conclude that
-
-$$
-u(r, \theta, t)=\sum_{m=0}^{\infty} \sum_{n=1}^{\infty} J_{m}\left(\lambda_{m n} r\right)\left(a_{m n}^{*} \cos m \theta+b_{m n}^{*} \sin m \theta\right) \sin c \lambda_{m n} t
-$$
-
-(c) Use the given initial velocity and (b) to obtain
-
-$$
-\begin{array}{r}
-g(r, \theta)=\sum_{n=1}^{\infty} c \lambda_{0 n} a_{0 n}^{*} J_{0}\left(\lambda_{0 n} r\right)+\sum_{m=1}^{\infty}\left\{\left(\sum_{n=1}^{\infty} c \lambda_{m n} a_{m n}^{*} J_{m}\left(\lambda_{m n} r\right)\right) \cos m \theta\right. \\
-\left.+\left(\sum_{n=1}^{\infty} c \lambda_{m n} b_{m n}^{*} J_{m}\left(\lambda_{m n} r\right)\right) \sin m \theta\right\}
-\end{array}
-$$
-
-(d) Derive (17)-(19) by proceeding from here as we did in the derivation of (12)(14).
-8. General solution of the vibrating circular membrane problem.
-(a) Show that the solution of the boundary value problem (1)-(3) can be written as $u(r, \theta, t)=u_{1}(r, \theta, t)+u_{2}(r, \theta, t)$, where $u_{1}$ and $u_{2}$ satisfy (1) and (3) and the following initial conditions:
-
-$$
-\begin{aligned}
-& u_{1}(r, \theta, 0)=f(r, \theta), \quad \frac{\partial u_{1}}{\partial t}(r, \theta, 0)=0 ; \\
-& u_{2}(r, \theta, 0)=0, \quad \frac{\partial u_{2}}{\partial t}(r, \theta, 0)=g(r, \theta) .
-\end{aligned}
-$$
-
-(b) Combine the results of Example 1 and Exercise 7 to derive the general solution (16).
-9. Project Problem: An integral formula for Bessel functions. Follow the outlined steps to prove that for any $k \geq 0$, and any integer $l \geq 0$, we have
-
-$$
-\int r^{k+1+2 l} J_{k}(r) d r=\sum_{n=0}^{l}(-1)^{n} 2^{n} \frac{l!}{(l-n)!} r^{k+1+2 l-n} J_{k+n+1}(r)+C .
-$$
-
-(a) Show that the formula holds for $l=0$ and all $k \geq 0$. [Hint: Use (7), Section 12.8.]
-(b) Complete the proof by induction on $l$. [Hint: Assume the formula is true for $l-1$ and all $k$. To establish the formula for $l$, integrate by parts and use the formula with $l-1$ and $k+1$.]
-10. Solve the boundary value problem (1)-(3) when $a=c=1, f(r, \theta)=(1- \left.r^{2}\right)\left(\frac{1}{4}-r^{2}\right) r^{3} \sin 3 \theta$, and $g(r, \theta)=0$. [Hint: Exercise 9 is useful.]
-11. Project Problem: Two-dimensional heat equation (general case). Use the methods of this section to show that the solution of heat boundary value problem
-
-$$
-\begin{gathered}
-\frac{\partial u}{\partial t}=c^{2}\left(\frac{\partial^{2} u}{\partial r^{2}}+\frac{1}{r} \frac{\partial u}{\partial r}+\frac{1}{r^{2}} \frac{\partial^{2} u}{\partial \theta^{2}}\right), \quad 0<r<a, 0<\theta<2 \pi, t>0, \\
-u(a, \theta, t)=0, \quad 0<\theta<2 \pi, t>0, \\
-u(r, \theta, 0)=f(r, \theta), \quad 0<r<a, 0<\theta<2 \pi,
-\end{gathered}
-$$
-
-is
-
-$$
-u(r, \theta, t)=\sum_{m=0}^{\infty} \sum_{n=1}^{\infty} J_{m}\left(\lambda_{m n} r\right)\left(a_{m n} \cos m \theta+b_{m n} \sin m \theta\right) e^{-c^{2} \lambda_{m n}^{2} t}
-$$
-
-where $\lambda_{m n}=\frac{\alpha_{m n}}{a} ; \alpha_{m n}$ is the $n$th positive zero of $J_{m}$; and $a_{m n}, b_{m n}$ are given by (12)-(14).
-12. (a) Solve the heat problem in Exercise 11 for the following data: $a=c=$ 1, $f(r, \theta)=\left(1-r^{2}\right) r \sin \theta$. [Hint: Example 2.]
-(b) What are the hottest points when $t=0$ ?
-(c) Locate the hottest point in the plate for $t=1,2$. Approximate the temperature of these points at the given times.
-13. Solve the heat equation
-
-$$
-\frac{\partial u}{\partial t}=\frac{\partial^{2} u}{\partial r^{2}}+\frac{1}{r} \frac{\partial u}{\partial r}+\frac{1}{r^{2}} \frac{\partial^{2} u}{\partial \theta^{2}}, \quad 0<r<1,0<\theta<2 \pi, t>0,
-$$
-
-given the nonzero boundary condition
-
-$$
-u(1, \theta, t)=\sin 3 \theta
-$$
-
-and the initial condition $u(r, \theta, 0)=0$.
+## Exercises 12.3
+
+
+> [!prompt|4cf51c85-358b-5575-95c0-dcd69374a7f2.local at=4a39f4b9-ebb6-5cfe-a58c-3306da36ce7d] Shared exercise instructions
+> In Exercises 1–6, solve the vibrating membrane problem (1)-(3) for the given data. If possible, with the help of a computer, find numerical values for the first five nonzero coefficients of the series solution and plot the shape of the membrane at various values of $t$. (Formula (15) is helpful in doing these problems.)
+
+
+> [!exercise|c95c5c5e-850e-55ac-bb7c-af46e5a9739f.local at=e957336a-01e8-5f7f-accf-6b23f27127a0] Exercise 1
+> $f(r, \theta)=\left(1-r^{2}\right) r^{2} \sin 2 \theta, g(r, \theta)=0, a=c=1$.
+
+
+> [!exercise|519b6dcb-6f91-5512-aeff-374b9b445cdf.local at=2e5adc19-7655-58a4-9f9c-e6041b2299d1] Exercise 2
+> $f(r,\theta)=(9-r^2)\cos2\theta$, $g(r,\theta)=0$, $a=3$, $c=1$. 
+
+
+> [!exercise|5191495d-af2e-5e40-a585-17be2810168b.local at=d715f195-7a24-5ea7-9349-c6b4e84447d0] Exercise 3
+> $f(r, \theta)=\left(4-r^{2}\right) r \sin \theta, g(r, \theta)=1, a=2, c=1$.
+
+
+> [!exercise|60de2910-0462-5312-9cc8-3cc91f7d7791.local at=78434cad-f8bd-5c72-a3cb-49402545bcbb] Exercise 4
+> $f(r, \theta)=J_{3}\left(\alpha_{32} r\right) \sin 3 \theta, g(r, \theta)=0, a=c=1$.
+
+
+> [!exercise|b2726f0b-5c33-5665-a625-bd0f41a6354c.local at=99c0f380-3055-52ca-bade-4099063f87fe] Exercise 5
+> $f(r, \theta)=0, g(r, \theta)=\left(1-r^{2}\right) r^{2} \sin 2 \theta, a=c=1$.
+
+
+> [!exercise|f2a87166-c1c6-54e7-9e01-935c8499c298.local at=e8e9f644-7d2d-5438-b9e4-329027556a32] Exercise 6
+> $f(r, \theta)=1-r^{2}, g(r, \theta)=J_{0}(r), a=c=1$.
+
+
+> [!exercise|38980ffa-bec4-5523-9055-825c6b713623.local at=c374aca6-4a3f-57bc-9783-122abb21bd0a] Exercise 7
+> Project Problem: Circular membrane with zero initial displacement. Follow the steps outlined in this exercise to determine the vibrations of a circular membrane with radius $a$ and fixed boundary, given that the initial displacement of the membrane is 0 , and its initial velocity is $g(r, \theta)$. Review the solution of Example 1 for hints.
+> (a) Write down explicitly the differential equation, the boundary conditions, and the initial conditions.
+> (b) Assume a product solution of the form $R(r) \Theta(\theta) T(t)$ and show that $T(0)=0$. Conclude that
+>
+> $$
+> u(r, \theta, t)=\sum_{m=0}^{\infty} \sum_{n=1}^{\infty} J_{m}\left(\lambda_{m n} r\right)\left(a_{m n}^{*} \cos m \theta+b_{m n}^{*} \sin m \theta\right) \sin c \lambda_{m n} t
+> $$
+>
+> (c) Use the given initial velocity and (b) to obtain
+>
+> $$
+> \begin{array}{r}
+> g(r, \theta)=\sum_{n=1}^{\infty} c \lambda_{0 n} a_{0 n}^{*} J_{0}\left(\lambda_{0 n} r\right)+\sum_{m=1}^{\infty}\left\{\left(\sum_{n=1}^{\infty} c \lambda_{m n} a_{m n}^{*} J_{m}\left(\lambda_{m n} r\right)\right) \cos m \theta\right. \\
+> \left.+\left(\sum_{n=1}^{\infty} c \lambda_{m n} b_{m n}^{*} J_{m}\left(\lambda_{m n} r\right)\right) \sin m \theta\right\}
+> \end{array}
+> $$
+>
+> (d) Derive (17)-(19) by proceeding from here as we did in the derivation of (12)(14).
+
+
+> [!exercise|4410fe33-34e0-5791-a380-4d170f308d9e.local at=f905440e-5330-5eee-8659-2d5db6b4f136] Exercise 8
+> General solution of the vibrating circular membrane problem.
+> (a) Show that the solution of the boundary value problem (1)-(3) can be written as $u(r, \theta, t)=u_{1}(r, \theta, t)+u_{2}(r, \theta, t)$, where $u_{1}$ and $u_{2}$ satisfy (1) and (3) and the following initial conditions:
+>
+> $$
+> \begin{aligned}
+> & u_{1}(r, \theta, 0)=f(r, \theta), \quad \frac{\partial u_{1}}{\partial t}(r, \theta, 0)=0 ; \\
+> & u_{2}(r, \theta, 0)=0, \quad \frac{\partial u_{2}}{\partial t}(r, \theta, 0)=g(r, \theta) .
+> \end{aligned}
+> $$
+>
+> (b) Combine the results of Example 1 and Exercise 7 to derive the general solution (16).
+
+
+> [!exercise|0736afe4-344b-5908-bda8-511758393f62.local at=d65b2cff-f96b-5b96-b06e-e29d3f4ecacd] Exercise 9
+> Project Problem: An integral formula for Bessel functions. Follow the outlined steps to prove that for any $k \geq 0$, and any integer $l \geq 0$, we have
+>
+> $$
+> \int r^{k+1+2 l} J_{k}(r) d r=\sum_{n=0}^{l}(-1)^{n} 2^{n} \frac{l!}{(l-n)!} r^{k+1+2 l-n} J_{k+n+1}(r)+C .
+> $$
+>
+> (a) Show that the formula holds for $l=0$ and all $k \geq 0$. [Hint: Use (7), Section 12.8.]
+> (b) Complete the proof by induction on $l$. [Hint: Assume the formula is true for $l-1$ and all $k$. To establish the formula for $l$, integrate by parts and use the formula with $l-1$ and $k+1$.]
+
+
+> [!exercise|d6a7799c-ac3c-5fbb-9d7a-2a1306116c48.local at=bbefef64-3b21-51c5-807d-baee04ad6605] Exercise 10
+> Solve the boundary value problem (1)-(3) when $a=c=1, f(r, \theta)=\left(1-r^{2}\right)\left(\frac{1}{4}-r^{2}\right) r^{3} \sin 3 \theta$, and $g(r, \theta)=0$. [Hint: Exercise 9 is useful.]
+
+
+> [!exercise|6a5dc6f0-a3ef-5c2e-b3bd-d33a330f87b4.local at=a4d7cddb-7733-5385-9f91-619c99227360] Exercise 11
+> Project Problem: Two-dimensional heat equation (general case). Use the methods of this section to show that the solution of heat boundary value problem
+>
+> $$
+> \begin{gathered}
+> \frac{\partial u}{\partial t}=c^{2}\left(\frac{\partial^{2} u}{\partial r^{2}}+\frac{1}{r} \frac{\partial u}{\partial r}+\frac{1}{r^{2}} \frac{\partial^{2} u}{\partial \theta^{2}}\right), \quad 0<r<a, 0<\theta<2 \pi, t>0, \\
+> u(a, \theta, t)=0, \quad 0<\theta<2 \pi, t>0, \\
+> u(r, \theta, 0)=f(r, \theta), \quad 0<r<a, 0<\theta<2 \pi,
+> \end{gathered}
+> $$
+>
+> is
+>
+> $$
+> u(r, \theta, t)=\sum_{m=0}^{\infty} \sum_{n=1}^{\infty} J_{m}\left(\lambda_{m n} r\right)\left(a_{m n} \cos m \theta+b_{m n} \sin m \theta\right) e^{-c^{2} \lambda_{m n}^{2} t}
+> $$
+>
+> where $\lambda_{m n}=\frac{\alpha_{m n}}{a} ; \alpha_{m n}$ is the $n$th positive zero of $J_{m}$; and $a_{m n}, b_{m n}$ are given by (12)-(14).
+
+
+> [!exercise|7fd7b62d-9eeb-55e2-9ef1-26f52fc950cb.local at=62ca37ce-3801-5fe9-9d5d-fbdbcf7958f2] Exercise 12
+> (a) Solve the heat problem in Exercise 11 for the following data: $a=c=1$, $f(r, \theta)=\left(1-r^{2}\right) r \sin \theta$. [Hint: Example 2.]
+> (b) What are the hottest points when $t=0$ ?
+> (c) Locate the hottest point in the plate for $t=1,2$. Approximate the temperature of these points at the given times.
+
+
+> [!exercise|aa2d43df-7092-5483-9422-334cf844bf6b.local at=649f62ab-b70b-560f-8479-485671265d47] Exercise 13
+> Solve the heat equation
+>
+> $$
+> \frac{\partial u}{\partial t}=\frac{\partial^{2} u}{\partial r^{2}}+\frac{1}{r} \frac{\partial u}{\partial r}+\frac{1}{r^{2}} \frac{\partial^{2} u}{\partial \theta^{2}}, \quad 0<r<1,0<\theta<2 \pi, t>0,
+> $$
+>
+> given the nonzero boundary condition
+>
+> $$
+> u(1, \theta, t)=\sin 3 \theta
+> $$
+>
+> and the initial condition $u(r, \theta, 0)=0$.

`````
