
# Editorial records

Reading note: 11.8 Laplace's Equation in Rectangular Coordinates.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!definition] Dirichlet problem for Laplace’s equation
> Given a domain $\Omega$ and prescribed boundary values $h$, the Dirichlet problem for Laplace’s equation asks for a harmonic function $u$ in $\Omega$ satisfying $u=h$ on $\partial\Omega$. For the classical continuous-boundary formulation, $u\in C^2(\Omega)\cap C(\overline\Omega)$.
````
### After

````text
> [!definition] Dirichlet problem for Laplace’s equation
> A problem consisting of Laplace's equation on a region in the plane together with specified boundary values is called a Dirichlet problem.
````

## 2. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!equation] Fourier series solution of the Dirichlet problem for a rectangle
> Let $a,b>0$. For Laplace’s equation $u_{xx}+u_{yy}=0$ on $0<x<a$, $0<y<b$, prescribe piecewise smooth boundary data
> $$
> u(x,0)=f_1(x),\quad u(x,b)=f_2(x),\quad u(0,y)=g_1(y),\quad u(a,y)=g_2(y).
> $$
> The solution in the rectangle is
> $$
> \begin{aligned}
> u(x,y)={}&\sum_{n=1}^{\infty}\left[A_n\sinh\frac{n\pi(b-y)}a+B_n\sinh\frac{n\pi y}a\right]\sin\frac{n\pi x}a\\
> &+\sum_{n=1}^{\infty}\left[C_n\sinh\frac{n\pi(a-x)}b+D_n\sinh\frac{n\pi x}b\right]\sin\frac{n\pi y}b,
> \end{aligned}
> $$
> with
> $$
> \begin{aligned}
> A_n&=\frac{2}{a\sinh(n\pi b/a)}\int_0^a f_1(x)\sin\frac{n\pi x}a\,dx,&
> B_n&=\frac{2}{a\sinh(n\pi b/a)}\int_0^a f_2(x)\sin\frac{n\pi x}a\,dx,\\
> C_n&=\frac{2}{b\sinh(n\pi a/b)}\int_0^b g_1(y)\sin\frac{n\pi y}b\,dy,&
> D_n&=\frac{2}{b\sinh(n\pi a/b)}\int_0^b g_2(y)\sin\frac{n\pi y}b\,dy.
> \end{aligned}
> $$
> Boundary data are attained at continuity points on the open sides. Continuity on the closed rectangle additionally requires compatible values at the corners.
````
### After

````text
> [!equation] Solution of the Dirichlet Problem in a Rectangle
> Let $a,b>0$. For Laplace’s equation $u_{xx}+u_{yy}=0$ on $0<x<a$, $0<y<b$, prescribe piecewise smooth boundary data
> $$
> u(x,0)=f_1(x),\quad u(x,b)=f_2(x),\quad u(0,y)=g_1(y),\quad u(a,y)=g_2(y).
> $$
> The solution of the two dimensional Dirichlet problem with these boundary conditions is
>
> $$
> u(x, y)=\sum_{n=1}^{\infty} A_{n} \sin \frac{n \pi}{a} x \sinh \frac{n \pi}{a}(b-y)+\sum_{n=1}^{\infty} B_{n} \sin \frac{n \pi}{a} x \sinh \frac{n \pi}{a} y
> $$
>
> $$
> +\sum_{n=1}^{\infty} C_{n} \sinh \frac{n \pi}{b}(a-x) \sin \frac{n \pi}{b} y+\sum_{n=1}^{\infty} D_{n} \sinh \frac{n \pi}{b} x \sin \frac{n \pi}{b} y,
> $$
>
> with
> $$
> \begin{aligned}
> A_n&=\frac{2}{a\sinh(n\pi b/a)}\int_0^a f_1(x)\sin\frac{n\pi x}a\,dx,&
> B_n&=\frac{2}{a\sinh(n\pi b/a)}\int_0^a f_2(x)\sin\frac{n\pi x}a\,dx,\\
> C_n&=\frac{2}{b\sinh(n\pi a/b)}\int_0^b g_1(y)\sin\frac{n\pi y}b\,dy,&
> D_n&=\frac{2}{b\sinh(n\pi a/b)}\int_0^b g_2(y)\sin\frac{n\pi y}b\,dy.
> \end{aligned}
> $$
> Boundary data are attained at continuity points on the open sides. Continuity on the closed rectangle additionally requires compatible values at the corners.
````

## Source-to-current comparison

Source: /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 11 Partial Differential Equations in Rectangular Coordinates/11.8 Laplace's Equation in Rectangular Coordinates.md

This exact comparison preserves the full change evidence, including formatting, OCR corrections, restored source wording, and required standalone context. The entries above explain the recovery edits. The comparison is not a claim that every difference is a correction; component serialization, callout wrapping, and printed labels outside callouts are formatting.

`````diff
--- /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 11 Partial Differential Equations in Rectangular Coordinates/11.8 Laplace's Equation in Rectangular Coordinates.md
+++ /Users/gradyclopton/ObsidianVaults/complex_analysis/Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 11 Partial Differential Equations in Rectangular Coordinates/11.8 Laplace's Equation in Rectangular Coordinates.md
@@ -1,3 +1,4 @@
+
 ### 11.8 Laplace's Equation in Rectangular Coordinates
 
 In Section 11.5 we saw that the steady-state temperature distributions associated with the one dimensional heat equation
@@ -10,6 +11,7 @@
 
 $$
 \frac{\partial^{2} u}{\partial x^{2}}+\frac{\partial^{2} u}{\partial y^{2}}=0, \quad 0<x<a, \quad 0<y<b
+\tag{1}
 $$
 
 This equation is known as Laplace's equation in two variables and is obtained by setting the time derivative equal to zero in the heat equation (11), Section 11.7. As we saw in Section 11.1, Laplace's equation has a wide variety of solutions. In a typical problem, the solution that we seek will be determined by the given boundary conditions. In the rest of the section, we solve (1) when $u$ is specified along the boundary of the rectangle. More specifically, we impose the boundary conditions
@@ -23,19 +25,45 @@
 
 as illustrated in Figure 1.
 
-Figure 1 A general Dirichlet problem on a rectangle.
-![](./images/e7203df9-f76c-453b-be1e-147d5ba42d96-62_391_1020_685_670.jpg)
-
-![](./images/e7203df9-f76c-453b-be1e-147d5ba42d96-62_366_439_1507_61.jpg)
-Figure 2 Dirichlet problem in Example 1.
-
-A problem consisting of Laplace's equation on a region in the plane together with specified boundary values is called a Dirichlet problem. Thus the problem we described above is a Dirichlet problem on a rectangle. Rather than attacking this problem in its full generality, we will start by solving the special case when $f_{1}, g_{1}$, and $g_{2}$ are all zero. We will return to the general problem at the end of the section.
-
-## EXAMPLE 1 A Dirichlet problem on a rectangle
-
-Solve the boundary value problem described in Figure 2 using the method of separation of variables.
-
-Solution We begin by looking for product solutions $u(x, y)=X(x) Y(y)$. Substituting into (1) and using the separation method, we arrive at the equations
+```scientific-figure
+id: e8842489-ce5e-4879-a272-d1d2b8062cf9
+numbered: false
+title: ""
+caption: Figure 1 A general Dirichlet problem on a rectangle.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 11 Partial Differential Equations in Rectangular Coordinates/images/e7203df9-f76c-453b-be1e-147d5ba42d96-62_391_1020_685_670.jpg
+    caption: ""
+```
+
+
+```scientific-figure
+id: 2b874ee1-bd49-4531-96fc-c8697bc0b537
+numbered: false
+title: ""
+caption: Figure 2 Dirichlet problem in Example 1.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 11 Partial Differential Equations in Rectangular Coordinates/images/e7203df9-f76c-453b-be1e-147d5ba42d96-62_366_439_1507_61.jpg
+    caption: ""
+```
+
+
+> [!definition] Dirichlet problem for Laplace’s equation
+> A problem consisting of Laplace's equation on a region in the plane together with specified boundary values is called a Dirichlet problem.
+
+Thus the problem we described above is a Dirichlet problem on a rectangle. Rather than attacking this problem in its full generality, we will start by solving the special case when $f_{1}, g_{1}$, and $g_{2}$ are all zero. We will return to the general problem at the end of the section.
+
+> [!exercise] EXAMPLE 1 A Dirichlet problem on a rectangle
+> Using separation of variables, solve $u_{xx}+u_{yy}=0$ on $0<x<a$, $0<y<b$, with $u(0,y)=u(a,y)=u(x,0)=0$ and $u(x,b)=f_2(x)$ (Figure 2).
+
+##### solution
+
+We begin by looking for product solutions $u(x, y)=X(x) Y(y)$. Substituting into (1) and using the separation method, we arrive at the equations
 
 $$
 X^{\prime \prime}+k X=0, \quad Y^{\prime \prime}-k Y=0
@@ -81,6 +109,7 @@
 
 $$
 u(x, y)=\sum_{n=1}^{\infty} B_{n} \sin \frac{n \pi}{a} x \sinh \frac{n \pi}{a} y
+\tag{2}
 $$
 
 Finally, the boundary condition $u(x, b)=f_{2}(x)$ implies that
@@ -89,22 +118,24 @@
 f_{2}(x)=\sum_{n=1}^{\infty} B_{n} \sinh \frac{n \pi b}{a} \sin \frac{n \pi}{a} x
 $$
 
-To meet this last requirement, we choose the coefficients $B_{n} \sinh \frac{n \pi b}{a}$ to be the Fourier sine coefficients of $f_{2}$ on the interval $0<x<a$. Thus from Theorem 1, Section 2.4, it follows that
+To meet this last requirement, we choose the coefficients $B_{n} \sinh \frac{n \pi b}{a}$ to be the Fourier sine coefficients of $f_{2}$ on the interval $0<x<a$. Thus from Theorem 1, Section 7.4, it follows that
 
 $$
 B_{n}=\frac{2}{a \sinh \frac{n \pi b}{a}} \int_{0}^{a} f_{2}(x) \sin \frac{n \pi}{a} x d x, \quad n=1,2, \ldots
+\tag{3}
 $$
 
 The solution of the Dirichlet problem described in Figure 2 is therefore given by (2) with coefficients determined by (3).
 
 The following is a specific application of Example 1.
 
-## EXAMPLE 2 Steady-state temperature in a square plate
-
-(a) Determine the steady-state temperature distribution in a $1 \times 1$ square plate where one side is held at $100^{\circ}$ and the other three sides are held at $0^{\circ}$.
-(b) In particular, find the steady-state temperature at the center of the plate.
-
-Solution (a) By choosing coordinates appropriately, we can do this problem as a special case of Example 1, where $f_{2}(x)=100^{\circ}$ and $a=b=1$. From (2) and (3), we have
+> [!exercise] EXAMPLE 2 Steady-state temperature in a square plate
+> (a) Determine the steady-state temperature distribution in a $1 \times 1$ square plate where one side is held at $100^{\circ}$ and the other three sides are held at $0^{\circ}$.
+> (b) In particular, find the steady-state temperature at the center of the plate.
+
+##### solution
+
+(a) By choosing coordinates appropriately, we can do this problem as a special case of Example 1, where $f_{2}(x)=100^{\circ}$ and $a=b=1$. From (2) and (3), we have
 
 $$
 u(x, y)=\sum_{n=1}^{\infty} B_{n} \sin n \pi x \sinh n \pi y
@@ -127,6 +158,7 @@
 
 $$
 u\left(\frac{1}{2}, \frac{1}{2}\right)=\frac{200}{\pi} \sum_{k=0}^{\infty} \frac{(-1)^{k}}{(2 k+1)} \frac{1}{\cosh (2 k+1) \frac{\pi}{2}},
+\tag{4}
 $$
 
 where we have simplified using
@@ -145,8 +177,19 @@
 
 We now return to the general problem described in Figure 1. It turns out that this problem can be solved by using the solution to Example 1. The trick is to decompose the original problem into four subproblems, as described by Figure 3.
 
-Figure 3 Linearity is used here to decompose the Dirichlet problem into the "sum" of four simpler Dirichlet subproblems.
-![](./images/e7203df9-f76c-453b-be1e-147d5ba42d96-64_687_1182_1468_594.jpg)
+```scientific-figure
+id: 0fac5359-4aed-4e6b-a05b-fb448f8a7a94
+numbered: false
+title: ""
+caption: Figure 3 Linearity is used here to decompose the Dirichlet problem into the "sum" of four simpler Dirichlet subproblems.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 11 Partial Differential Equations in Rectangular Coordinates/images/e7203df9-f76c-453b-be1e-147d5ba42d96-64_687_1182_1468_594.jpg
+    caption: ""
+```
+
 
 Let $u_{1}, u_{2}, u_{3}, u_{4}$ be the solutions of subproblems $1,2,3,4$, respectively. By direct computation, we see that the function
 
@@ -164,6 +207,7 @@
 
 $$
 B_{n}=\frac{2}{a \sinh \frac{n \pi b}{a}} \int_{0}^{a} f_{2}(x) \sin \frac{n \pi}{a} x d x
+\tag{5}
 $$
 
 The other solutions can be found analogously. In particular, $u_{4}$ is the same as $u_{2}$ except that $a$ and $b$ are interchanged, as are $x$ and $y$. Thus
@@ -176,6 +220,7 @@
 
 $$
 D_{n}=\frac{2}{b \sinh \frac{n \pi a}{b}} \int_{0}^{b} g_{2}(y) \sin \frac{n \pi}{b} y d y
+\tag{6}
 $$
 
 The solutions $u_{1}$ and $u_{3}$ are found similarly. We have
@@ -188,6 +233,7 @@
 
 $$
 A_{n}=\frac{2}{a \sinh \frac{n \pi b}{a}} \int_{0}^{a} f_{1}(x) \sin \frac{n \pi}{a} x d x
+\tag{7}
 $$
 
 and
@@ -200,23 +246,37 @@
 
 $$
 C_{n}=\frac{2}{b \sinh \frac{n \pi a}{b}} \int_{0}^{b} g_{1}(y) \sin \frac{n \pi}{b} y d y
-$$
-
-SOLUTION OF THE DIRICHLET PROBLEM IN A RECTANGLE
-
-We have thus completely solved the Dirichlet problem in Figure 1. We summarize the solution as follows.
-
-The solution of the two dimensional Dirichlet problem in Figure 1 is
-
-$$
-u(x, y)=\sum_{n=1}^{\infty} A_{n} \sin \frac{n \pi}{a} x \sinh \frac{n \pi}{a}(b-y)+\sum_{n=1}^{\infty} B_{n} \sin \frac{n \pi}{a} x \sinh \frac{n \pi}{a} y
-$$
-
-$$
-+\sum_{n=1}^{\infty} C_{n} \sinh \frac{n \pi}{b}(a-x) \sin \frac{n \pi}{b} y+\sum_{n=1}^{\infty} D_{n} \sinh \frac{n \pi}{b} x \sin \frac{n \pi}{b} y,
-$$
-
-where the coefficients $A_{n}, B_{n}, C_{n}$, and $D_{n}$ are given by (5)-(8).
+\tag{8}
+$$
+
+> [!equation] Solution of the Dirichlet Problem in a Rectangle
+> Let $a,b>0$. For Laplace’s equation $u_{xx}+u_{yy}=0$ on $0<x<a$, $0<y<b$, prescribe piecewise smooth boundary data
+> $$
+> u(x,0)=f_1(x),\quad u(x,b)=f_2(x),\quad u(0,y)=g_1(y),\quad u(a,y)=g_2(y).
+> $$
+> The solution of the two dimensional Dirichlet problem with these boundary conditions is
+>
+> $$
+> u(x, y)=\sum_{n=1}^{\infty} A_{n} \sin \frac{n \pi}{a} x \sinh \frac{n \pi}{a}(b-y)+\sum_{n=1}^{\infty} B_{n} \sin \frac{n \pi}{a} x \sinh \frac{n \pi}{a} y
+> $$
+>
+> $$
+> +\sum_{n=1}^{\infty} C_{n} \sinh \frac{n \pi}{b}(a-x) \sin \frac{n \pi}{b} y+\sum_{n=1}^{\infty} D_{n} \sinh \frac{n \pi}{b} x \sin \frac{n \pi}{b} y,
+> $$
+>
+> with
+> $$
+> \begin{aligned}
+> A_n&=\frac{2}{a\sinh(n\pi b/a)}\int_0^a f_1(x)\sin\frac{n\pi x}a\,dx,&
+> B_n&=\frac{2}{a\sinh(n\pi b/a)}\int_0^a f_2(x)\sin\frac{n\pi x}a\,dx,\\
+> C_n&=\frac{2}{b\sinh(n\pi a/b)}\int_0^b g_1(y)\sin\frac{n\pi y}b\,dy,&
+> D_n&=\frac{2}{b\sinh(n\pi a/b)}\int_0^b g_2(y)\sin\frac{n\pi y}b\,dy.
+> \end{aligned}
+> $$
+> Boundary data are attained at continuity points on the open sides. Continuity on the closed rectangle additionally requires compatible values at the corners.
+
+*Printed equation label: (9).*
+
 Let us now revisit Example 2(b). We shall derive the value of $u\left(\frac{1}{2}, \frac{1}{2}\right)$ by using a symmetry argument. Consider the problem where the boundary data 100 is specified on all four sides of the plate. Clearly, this problem has solution $u(x, y)=100$ throughout the square. On the other hand, we can certainly decompose this problem into the four subproblems described in Figure 3. Because of the symmetry, the four functions $u_{1}, u_{2}, u_{3}$, and $u_{4}$ assume the same value at the center. Equating the two versions of the solution at the center, we see that
 
 $$
@@ -227,78 +287,145 @@
 
 You may recall how in Section 11.5 we used steady-state solutions to solve heat problems with nonhomogeneous boundary conditions. As you can imagine, these methods are also useful in solving nonhomogeneous heat problems in higher dimensions. See Exercise 11 for an illustration.
 
-## Exercises 3.8
-
-In Exercises 1-6, solve the Dirichlet problem in Figure 1 for the given data.
-
-1. $a=1, b=2, f_{2}(x)=x, f_{1}=g_{1}=g_{2}=0$.
-2. $a=1, b=1, f_{1}(x)=0, f_{2}=100, g_{1}=0, g_{2}=100$.
-3. $a=2, b=1, f_{1}(x)=100, f_{2}=g_{1}=0, g_{2}(y)=100(1-y)$.
-4. $a=b=1, f_{1}(x)=1-x, f_{2}(x)=x, g_{1}=g_{2}=0$.
-5. $a=b=1, f_{1}(x)=\sin 7 \pi x, f_{2}(x)=\sin \pi x, g_{1}(y)=\sin 3 \pi y, g_{2}(y)=\sin 6 \pi y$.
-6. $a=b=\pi, f_{1}(x)=\cos x, f_{2}(x)=x \sin x, g_{1}(y)=\pi-y$,
-
-$$
-g_{2}(y)= \begin{cases}3 & \text { if } 0<y<\pi / 2 \\ 0 & \text { if } \frac{\pi}{2}<y<\pi\end{cases}
-$$
-
-![](./images/e7203df9-f76c-453b-be1e-147d5ba42d96-67_373_470_627_35.jpg)
-Figure 4
-
-![](./images/e7203df9-f76c-453b-be1e-147d5ba42d96-67_460_463_1484_42.jpg)
-Figure 5 The boundary values for $u$ are 0 except on the upper horizontal face, we have $u(x, y, c)=f(x, y)$.
-
-7. (a) Show that the solution to Example 1, when expressed in terms of the Fourier sine coefficients $b_{n}$ of $f_{2}(x)$, is
-
-$$
-u(x, y)=\sum_{n=1}^{\infty} b_{n} \sin \frac{n \pi}{a} x \frac{\sinh \frac{n \pi}{a} y}{\sinh \frac{n \pi b}{a}} .
-$$
-
-(b) State the corresponding result for the solution of the general problem (9).
-8. Approximate the temperature at the center of the plate in Exercise 1.
-9. Use the method of separation of variables to derive $u_{1}$ and $A_{n}$ in (7).
-10. Maximum principle for solutions of Laplace's equation. Plot the graph of the solution in Example 2. Observe that the maxima and minima of the solution occur at the boundary. This property of the solution holds for more general boundary data and is known as the maximum principle. For more details on this subject, see Section 11.11.
-11. Project Problem: Two dimensional heat problem with nonzero boundary data. Consider the nonhomogeneous heat problem in Figure 4. Let $v(x, y)$ denote the solution of the Dirichlet problem $\nabla^{2} v=0$ with boundary values as in the figure, and let $w(x, y, t)$ denote the solution of the heat problem $w_{t}=c^{2} \nabla^{2} w$ with 0 boundary data and initial temperature distribution $w(x, y, 0)=f(x, y)-v(x, y)$.
-(a) Show that the solution of the heat problem in Figure 4 is $u(x, y, t)=v(x, y)+ w(x, y, t)$, where $v$ is given by (9), and $w$ is given by (13)-(15), Section 11.7, where, in (15), $f(x, y)$ is to be replaced by $f(x, y)-v(x, y)$.
-(b) Solve the problem in the figure when $a=b=1, c=1, f_{1}=0, f_{2}=100$, $g_{1}=g_{2}=0$, and $f(x, y)=0$.
-(c) Plot the temperature of the center in part (b) for $t>0$ and discuss its behavior as $t \rightarrow \infty$.
-12. Project Problem: Three dimensional Laplace's equation and Dirichlet problems. Steady-state temperature problems inside a three dimensional solid lead to Dirichlet problems associated with Laplace's equation in three dimensions:
-
-$$
-\nabla^{2} u=\frac{\partial^{2} u}{\partial x^{2}}+\frac{\partial^{2} u}{\partial y^{2}}+\frac{\partial^{2} u}{\partial z^{2}}=0
-$$
-
-Consider such a problem as described in Figure 5. (See Exercise 13 for a generalization.) Follow the outlined steps to derive the solution
-
-$$
-\begin{gathered}
-u(x, y, z)=\sum_{n=1}^{\infty} \sum_{m=1}^{\infty} A_{m n} \sin \frac{m \pi}{a} x \sin \frac{n \pi}{b} y \sinh \lambda_{m n} z \\
-\lambda_{m n}=\pi \sqrt{\left(\frac{m}{a}\right)^{2}+\left(\frac{n}{b}\right)^{2}} \\
-A_{m n}=\frac{4}{a b \sinh \left(c \lambda_{m n}\right)} \int_{0}^{b} \int_{0}^{a} f(x, y) \sin \frac{m \pi}{a} x \sin \frac{n \pi}{b} y d x d y
-\end{gathered}
-$$
-
-(a) Step 1: Look for product solutions of the form $X(x) Y(y) Z(z)$. Use separation of variables and derive the equations
-
-$$
-\begin{gathered}
-X^{\prime \prime}+\mu^{2} X=0, \quad Y^{\prime \prime}+\nu^{2} Y=0, \quad Z^{\prime \prime}-\left(\mu^{2}+\nu^{2}\right) Z=0 \\
-X(0)=X(a)=0, \quad Y(0)=Y(b)=0, \quad Z(0)=0
-\end{gathered}
-$$
-
-(You should justify the signs of the separation constants.)
-(b) Step 2: Show that
-
-$$
-\mu=\frac{m \pi}{a}, \quad \nu=\frac{n \pi}{b}, \quad m, n=1,2, \ldots,
-$$
-
-and derive the product solutions
-
-$$
-u_{m n}(x, y, z)=A_{m n} \sin \frac{m \pi}{a} x \sin \frac{n \pi}{b} y \sinh \lambda_{m n} z
-$$
-
-(c) Step 3: Complete the solution using Theorem 1 of Section 11.7.
-13. How would you solve the problem in Exercise 12 if the boundary data were nonzero on some of the six faces?
+## Exercises 11.8
+
+
+> [!prompt] Shared exercise instructions
+> In Exercises 1-6, solve the Dirichlet problem in Figure 1 for the given data.
+
+
+> [!exercise] Exercise 1
+> $a=1, b=2, f_{2}(x)=x, f_{1}=g_{1}=g_{2}=0$.
+
+
+> [!exercise] Exercise 2
+> $a=1, b=1, f_{1}(x)=0, f_{2}=100, g_{1}=0, g_{2}=100$.
+
+
+> [!exercise] Exercise 3
+> $a=2, b=1, f_{1}(x)=100, f_{2}=g_{1}=0, g_{2}(y)=100(1-y)$.
+
+
+> [!exercise] Exercise 4
+> $a=b=1, f_{1}(x)=1-x, f_{2}(x)=x, g_{1}=g_{2}=0$.
+
+
+> [!exercise] Exercise 5
+> $a=b=1, f_{1}(x)=\sin 7 \pi x, f_{2}(x)=\sin \pi x, g_{1}(y)=\sin 3 \pi y, g_{2}(y)=\sin 6 \pi y$.
+
+
+> [!exercise] Exercise 6
+> $a=b=\pi, f_{1}(x)=\cos x, f_{2}(x)=x \sin x, g_{1}(y)=\pi-y$,
+>
+> $$
+> g_{2}(y)= \begin{cases}3 & \text { if } 0<y<\pi / 2 \\ 0 & \text { if } \frac{\pi}{2}<y<\pi\end{cases}
+> $$
+
+
+> [!exercise] Exercise 7
+> (a) Show that the solution to Example 1, when expressed in terms of the Fourier sine coefficients $b_{n}$ of $f_{2}(x)$, is
+>
+> $$
+> u(x, y)=\sum_{n=1}^{\infty} b_{n} \sin \frac{n \pi}{a} x \frac{\sinh \frac{n \pi}{a} y}{\sinh \frac{n \pi b}{a}} .
+> $$
+>
+> (b) State the corresponding result for the solution of the general problem (9).
+
+
+> [!exercise] Exercise 8
+> Approximate the temperature at the center of the plate in Exercise 1.
+
+
+> [!exercise] Exercise 9
+> Use the method of separation of variables to derive $u_{1}$ and $A_{n}$ in (7).
+
+
+> [!exercise] Exercise 10
+> Maximum principle for solutions of Laplace's equation. Plot the graph of the solution in Example 2. Observe that the maxima and minima of the solution occur at the boundary. This property of the solution holds for more general boundary data and is known as the maximum principle. For more details on this subject, see Section 11.11.
+
+
+> [!exercise] Exercise 11
+> Project Problem: Two dimensional heat problem with nonzero boundary data. Consider the nonhomogeneous heat problem in Figure 4. Let $v(x, y)$ denote the solution of the Dirichlet problem $\nabla^{2} v=0$ with boundary values as in the figure, and let $w(x, y, t)$ denote the solution of the heat problem $w_{t}=c^{2} \nabla^{2} w$ with 0 boundary data and initial temperature distribution $w(x, y, 0)=f(x, y)-v(x, y)$.
+>
+> (a) Show that the solution of the heat problem in Figure 4 is $u(x, y, t)=v(x, y)+ w(x, y, t)$, where $v$ is given by (9), and $w$ is given by (13)-(15), Section 11.7, where, in (15), $f(x, y)$ is to be replaced by $f(x, y)-v(x, y)$.
+> (b) Solve the problem in the figure when $a=b=1, c=1, f_{1}=0, f_{2}=100$, $g_{1}=g_{2}=0$, and $f(x, y)=0$.
+> (c) Plot the temperature of the center in part (b) for $t>0$ and discuss its behavior as $t \rightarrow \infty$.
+
+
+```scientific-figure
+id: 7f882966-8471-4199-a651-17e01932a65a
+numbered: false
+title: ""
+caption: Figure 4 Rectangular heat problem with prescribed nonzero edge temperatures.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 11 Partial Differential Equations in Rectangular Coordinates/images/e7203df9-f76c-453b-be1e-147d5ba42d96-67_373_470_627_35.jpg
+    caption: ""
+```
+
+
+
+
+> [!exercise] Exercise 12
+> Project Problem: Three dimensional Laplace's equation and Dirichlet problems. Steady-state temperature problems inside a three dimensional solid lead to Dirichlet problems associated with Laplace's equation in three dimensions:
+>
+> $$
+> \nabla^{2} u=\frac{\partial^{2} u}{\partial x^{2}}+\frac{\partial^{2} u}{\partial y^{2}}+\frac{\partial^{2} u}{\partial z^{2}}=0
+> $$
+>
+> Consider such a problem as described in Figure 5. (See Exercise 13 for a generalization.) Follow the outlined steps to derive the solution
+>
+> $$
+> \begin{gathered}
+> u(x, y, z)=\sum_{n=1}^{\infty} \sum_{m=1}^{\infty} A_{m n} \sin \frac{m \pi}{a} x \sin \frac{n \pi}{b} y \sinh \lambda_{m n} z \\
+> \lambda_{m n}=\pi \sqrt{\left(\frac{m}{a}\right)^{2}+\left(\frac{n}{b}\right)^{2}} \\
+> A_{m n}=\frac{4}{a b \sinh \left(c \lambda_{m n}\right)} \int_{0}^{b} \int_{0}^{a} f(x, y) \sin \frac{m \pi}{a} x \sin \frac{n \pi}{b} y d x d y
+> \end{gathered}
+> $$
+>
+> (a) Step 1: Look for product solutions of the form $X(x) Y(y) Z(z)$. Use separation of variables and derive the equations
+>
+> $$
+> \begin{gathered}
+> X^{\prime \prime}+\mu^{2} X=0, \quad Y^{\prime \prime}+\nu^{2} Y=0, \quad Z^{\prime \prime}-\left(\mu^{2}+\nu^{2}\right) Z=0 \\
+> X(0)=X(a)=0, \quad Y(0)=Y(b)=0, \quad Z(0)=0
+> \end{gathered}
+> $$
+>
+> (You should justify the signs of the separation constants.)
+> (b) Step 2: Show that
+>
+> $$
+> \mu=\frac{m \pi}{a}, \quad \nu=\frac{n \pi}{b}, \quad m, n=1,2, \ldots,
+> $$
+>
+> and derive the product solutions
+>
+> $$
+> u_{m n}(x, y, z)=A_{m n} \sin \frac{m \pi}{a} x \sin \frac{n \pi}{b} y \sinh \lambda_{m n} z
+> $$
+>
+> (c) Step 3: Complete the solution using Theorem 1 of Section 11.7.
+
+
+```scientific-figure
+id: e580958e-461e-4652-ae58-9b8f32af71c6
+numbered: false
+title: ""
+caption: Figure 5 The boundary values for $u$ are 0 except on the upper horizontal face, we have $u(x, y, c)=f(x, y)$.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 11 Partial Differential Equations in Rectangular Coordinates/images/e7203df9-f76c-453b-be1e-147d5ba42d96-67_460_463_1484_42.jpg
+    caption: ""
+```
+
+
+
+
+
+> [!exercise] Exercise 13
+> How would you solve the problem in Exercise 12 if the boundary data were nonzero on some of the six faces?

`````
