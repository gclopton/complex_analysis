
# Editorial records

Reading note: 11.10 Neumann and Robin Conditions.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!definition|a4e32151-7186-55cb-85c7-7222899d6f7b.local at=235d7f1f-5602-5e71-8a86-808ae828807c] Dirichlet, Neumann, and Robin boundary conditions
> For a scalar field $u$ and the outward unit normal $n$ to a boundary:
>
> A Dirichlet condition specifies $u=h$.
>
> A Neumann condition specifies $\partial u/\partial n=h$.
>
> A generalized Robin condition specifies $\alpha u+\beta\,\partial u/\partial n=h$, with prescribed coefficients $\alpha,\beta$ not both zero. It includes the Dirichlet case $\beta=0$ and the Neumann case $\alpha=0$. When $\beta\ne0$, it can be normalized to $\partial u/\partial n+(\alpha/\beta)u=h/\beta$.
>
> For a rectangle, the outward normal derivatives on the left, right, bottom, and top sides are respectively $-u_x$, $u_x$, $-u_y$, and $u_y$.
````
### After

````text
> [!definition|a4e32151-7186-55cb-85c7-7222899d6f7b.local at=235d7f1f-5602-5e71-8a86-808ae828807c] Dirichlet, Neumann, and Robin boundary conditions
> In a boundary value problem, we will call a Dirichlet condition any condition that specifies the values of the solution $u$ on the boundary, and a Neumann condition any condition that specifies the normal derivative $\frac{\partial u}{\partial n}$ on the boundary. A Robin condition is any condition that specifies $\beta\frac{\partial u}{\partial n}+\alpha u$ on the boundary, where $\alpha$ and $\beta$ are prescribed functions of $x$ and $y$, not both zero. Thus Dirichlet and Neumann conditions are special cases of Robin conditions. In a rectangular region, the normal derivative on the boundary is a derivative in the positive or negative direction of the $x$ - or $y$-axes. Thus a Robin condition is a condition that specifies the values of $\beta u_x+\alpha u$ or $\beta u_y+\alpha u$, with the normal orientation included in $\beta$, on the boundary of the rectangle.
````

## Source-to-current comparison

Source: /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 11 Partial Differential Equations in Rectangular Coordinates/11.10 Neumann and Robin Conditions.md

This exact comparison preserves the full change evidence, including formatting, OCR corrections, restored source wording, and required standalone context. The entries above explain the recovery edits. The comparison is not a claim that every difference is a correction; component serialization, callout wrapping, and printed labels outside callouts are formatting.

`````diff
--- /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 11 Partial Differential Equations in Rectangular Coordinates/11.10 Neumann and Robin Conditions.md
+++ /Users/gradyclopton/ObsidianVaults/complex_analysis/Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 11 Partial Differential Equations in Rectangular Coordinates/11.10 Neumann and Robin Conditions.md
@@ -1,8 +1,19 @@
+
 ### 11.10 Neumann and Robin Conditions
 
-![](./images/e7203df9-f76c-453b-be1e-147d5ba42d96-78_371_461_314_59.jpg)
-
-Figure 1 Laplace's equation in a rectangle with zero boundary conditions on the vertical sides.
+```scientific-figure
+id: 3117b125-6a8b-4dfa-94c7-63093c008635
+numbered: false
+title: ""
+caption: Figure 1 Laplace's equation in a rectangle with zero boundary conditions on the vertical sides.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 11 Partial Differential Equations in Rectangular Coordinates/images/e7203df9-f76c-453b-be1e-147d5ba42d96-78_371_461_314_59.jpg
+    caption: ""
+```
+
 
 So far we have successfully solved boundary value problems using the separation of variables method and the eigenfunction expansion method. We took advantage of linearity and used superposition principles to simplify problems and break them up into simpler subproblems. In this section, we devise methods based on a combination of the tools that we just listed and greatly expand the scope of our applications.
 
@@ -10,53 +21,69 @@
 
 $$
 u(0, y)=0 \quad \text { and } \quad u(a, y)=0 \quad \text { for all } 0<y<b
+\tag{1}
 $$
 
 as shown in Figure 1. It will become clear from the examples that more general problems can be reduced to this situation using superposition.
 
 We start with a simple result that will be used often.
 
-## PROPOSITION 1 PRODUCT SOLUTIONS
-
-If $\phi(x, y)=X(x) Y(y)$ is a product solution of Laplace's equation in the $a \times b$-rectangle of Figure 1, with the zero boundary conditions on the vertical sides, then
-
-$$
-\phi(x, y)=\phi_{m}(x, y)=\sin \frac{m \pi}{a} x\left(A_{m} \cosh \frac{m \pi}{a} y+B_{m} \sinh \frac{m \pi}{a} y\right)
-$$
-
-where $m=1,2, \ldots$, and $A_{m}$ and $B_{m}$ are arbitrary constants.
-In some applications, it will be convenient to write the solution (2) in the form
-
-$$
-\phi_{m}(x, y)=\sin \frac{m \pi}{a} x\left(\alpha_{m} \cosh \frac{m \pi}{a}(\beta-y)+\beta_{m} \sinh \frac{m \pi}{a}(\beta-y)\right),
-$$
-
-where $\beta$ is a fixed number. You can check directly that (3) is a solution of the problem in Figure 1, or you can verify that (2) and (3) are equivalent by expressing the hyperbolic cosine and sine in terms of the exponential function.
+> [!proposition|69421399-4f98-5528-9247-fac030cee062.local at=9b6c5129-a47d-56f3-9124-4ea89a4c631b] Separated harmonic functions in a rectangle with zero values on opposite sides
+> If a nonzero function $\phi(x, y)=X(x) Y(y)$ is a product solution of $\phi_{xx}+\phi_{yy}=0$ on $0<x<a$, $0<y<b$, where $a,b>0$, with $\phi(0,y)=\phi(a,y)=0$, then
+>
+> $$
+> \phi(x, y)=\phi_{m}(x, y)=\sin \frac{m \pi}{a} x\left(A_{m} \cosh \frac{m \pi}{a} y+B_{m} \sinh \frac{m \pi}{a} y\right)
+> $$
+>
+> where $m=1,2, \ldots$, and $A_{m}$ and $B_{m}$ are arbitrary constants.
+> In some applications, it will be convenient to write the same solution in the form
+>
+> $$
+> \phi_{m}(x, y)=\sin \frac{m \pi}{a} x\left(\alpha_{m} \cosh \frac{m \pi}{a}(\beta-y)+\beta_{m} \sinh \frac{m \pi}{a}(\beta-y)\right),
+> $$
+>
+> where $\beta$ is a fixed number. The two displayed forms are equivalent, as can be verified by expressing the hyperbolic cosine and sine in terms of the exponential function.
+
+*Printed equation labels: (2) separated solution in $y$; (3) equivalent form using $b-y$.*
 
 Proof As we have done several times before (see, for example, Section 11.8), applying the separation of variables method, we find that if $\phi(x, y)=X Y$ is a solution, then $X$ satisfies $X^{\prime \prime}+k X=0$ and $X(0)=X(a)=0$, and $Y$ satisfies $Y^{\prime \prime}-k Y=0$. The only nontrivial solutions are $X=X_{m}=\sin \frac{m \pi}{a} x$, which correspond to $k=\left(\frac{m \pi}{a}\right)^{2}$. Moving to the $Y$ component, we have $Y^{\prime \prime}-\left(\frac{m \pi}{a}\right)^{2} Y=0$, which implies that $Y=A_{m} \cosh \frac{m \pi}{a} y+B_{m} \sinh \frac{m \pi}{a} y$, as claimed.
 
-In a boundary value problem, we will call a Dirichlet condition any condition that specifies the values of the solution $u$ on the boundary, and
-
-![](./images/e7203df9-f76c-453b-be1e-147d5ba42d96-79_368_456_777_35.jpg)
-Figure 2 Mixed Dirichlet and Neumann boundary conditions in Example 1. The Neumann condition is nonhomogeneous.
-
-a Neumann condition any condition that specifies the normal derivative $\frac{\partial u}{\partial n}$ on the boundary. A Robin condition is any condition that specifies $\frac{\partial u}{\partial n}+\alpha u$ on the boundary, where $\alpha$ is a function of $x$ and $y$. Thus Dirichlet and Neumann conditions are special cases of Robin conditions. In a rectangular region, the normal derivative on the boundary is a derivative in the positive or negative direction of the $x$ - or $y$-axes. Thus a Robin condition is a condition that specifies the values of $u_{x}+\alpha u$ or $u_{y}+\alpha u$ on the boundary of the rectangle.
+> [!definition|a4e32151-7186-55cb-85c7-7222899d6f7b.local at=235d7f1f-5602-5e71-8a86-808ae828807c] Dirichlet, Neumann, and Robin boundary conditions
+> In a boundary value problem, we will call a Dirichlet condition any condition that specifies the values of the solution $u$ on the boundary, and a Neumann condition any condition that specifies the normal derivative $\frac{\partial u}{\partial n}$ on the boundary. A Robin condition is any condition that specifies $\beta\frac{\partial u}{\partial n}+\alpha u$ on the boundary, where $\alpha$ and $\beta$ are prescribed functions of $x$ and $y$, not both zero. Thus Dirichlet and Neumann conditions are special cases of Robin conditions. In a rectangular region, the normal derivative on the boundary is a derivative in the positive or negative direction of the $x$ - or $y$-axes. Thus a Robin condition is a condition that specifies the values of $\beta u_x+\alpha u$ or $\beta u_y+\alpha u$, with the normal orientation included in $\beta$, on the boundary of the rectangle.
+
+```scientific-figure
+id: 6a503e7f-6a7b-45d0-9f34-3e6afa4a17f3
+numbered: false
+title: ""
+caption: Figure 2 Mixed Dirichlet and Neumann boundary conditions in Example 1. The Neumann condition is nonhomogeneous.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 11 Partial Differential Equations in Rectangular Coordinates/images/e7203df9-f76c-453b-be1e-147d5ba42d96-79_368_456_777_35.jpg
+    caption: ""
+```
+
 
 With this terminology, let us solve a problem with mixed Dirichlet and Neumann conditions.
 
-## EXAMPLE 1 Mixed Dirichlet and Neumann conditions
-
-Solve the boundary value problem in Figure 2.
-Solution Appealing to Proposition 1, the product solutions are of the form
+> [!exercise|d99c26aa-bbfb-5951-8489-14ba7f2de9a1.local at=7c930d39-d793-5758-9ea2-5878e98734b4] EXAMPLE 1 Mixed Dirichlet and Neumann conditions
+> Solve $u_{xx}+u_{yy}=0$ on $0<x<a$, $0<y<b$, with $u(0,y)=u(a,y)=u(x,0)=0$ and $u_y(x,b)=f(x)$ (Figure 2).
+
+##### solution
+
+Appealing to Proposition 1, the product solutions are of the form
 
 $$
 \phi_{m}(x, y)=\sin \frac{m \pi}{a} x\left(A_{m} \cosh \frac{m \pi}{a} y+B_{m} \sinh \frac{m \pi}{a} y\right) .
+\tag{4}
 $$
 
 As we know, these solutions already satisfy the boundary conditions on the vertical sides. Next, we specify the constants $A_{m}$ and $B_{m}$ in order to satisfy the zero Dirichlet condition on the horizontal side $y=0$. Indeed, $u(x, 0)=0$ implies that $A_{m} \sin \frac{m \pi}{a} x=0$, which in turn implies that $A_{m}=0$. So $\phi_{m}(x, y)= B_{m} \sin \frac{m \pi}{a} x \sinh \frac{m \pi}{a} y$. To satisfy the nonhomogeneous Neumann condition on the upper horizontal side, we will superpose the product solutions and try
 
 $$
 u(x, y)=\sum_{m=1}^{\infty} B_{m} \sin \frac{m \pi}{a} x \sinh \frac{m \pi}{a} y .
+\tag{5}
 $$
 
 Proceeding formally to compute $u_{y}$ by differentiating the series term by term, and then setting $u_{y}=f(x)$ when $y=b$, we obtain
@@ -69,18 +96,32 @@
 
 $$
 B_{m}=\frac{2}{\pi m \cosh \left(\frac{m \pi}{a} b\right)} \int_{0}^{a} f(x) \sin \frac{m \pi}{a} x d x
+\tag{6}
 $$
 
 This determines the coefficients $B_{m}$ and solves the problem completely.
 We next consider a problem with a Robin condition.
 
-![](./images/e7203df9-f76c-453b-be1e-147d5ba42d96-80_368_458_213_59.jpg)
-Figure 3 Mixed homogeneous Robin condition and nonhomogeneous Neumann boundary condition in Example 2.
-
-## EXAMPLE 2 Robin conditions
-
-Solve the boundary value problem in Figure 3.
-Solution From (2), we have the product solutions
+```scientific-figure
+id: 083b388a-ce66-47f6-8c45-dc8c976f5410
+numbered: false
+title: ""
+caption: Figure 3 Mixed homogeneous Robin condition and nonhomogeneous Neumann boundary condition in Example 2.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 11 Partial Differential Equations in Rectangular Coordinates/images/e7203df9-f76c-453b-be1e-147d5ba42d96-80_368_458_213_59.jpg
+    caption: ""
+```
+
+
+> [!exercise|23938a8d-387f-548a-b35a-5c9cfdd36690.local at=5de982fd-b703-52e5-b401-86a7bbfb153d] EXAMPLE 2 Robin conditions
+> Solve $u_{xx}+u_{yy}=0$ on $0<x<a$, $0<y<b$, with $u(0,y)=u(a,y)=0$, $u_y(x,0)+2u(x,0)=0$, and $u_y(x,b)=f(x)$ (Figure 3).
+
+##### solution
+
+From (2), we have the product solutions
 
 $$
 \phi(x, y)=\sin \frac{m \pi}{a} x\left(A_{m} \cosh \frac{m \pi}{a} y+B_{m} \sinh \frac{m \pi}{a} y\right) .
@@ -102,6 +143,7 @@
 
 $$
 u(x, y)=\sum_{m=1}^{\infty} A_{m} \sin \frac{m \pi}{a} x\left(\cosh \frac{m \pi}{a} y-\frac{2 a}{m \pi} \sinh \frac{m \pi}{a} y\right) .
+\tag{7}
 $$
 
 (We always deal with the nonhomogeneous condition last.) From $u_{y}(x, b)=f(x)$, we get
@@ -114,18 +156,35 @@
 
 $$
 A_{m}=\frac{2}{a\left(\frac{m \pi}{a} \sinh \left(\frac{m \pi}{a} b\right)-2 \cosh \left(\frac{m \pi}{a} b\right)\right)} \int_{0}^{a} f(x) \sin \frac{m \pi}{a} x d x
-$$
-
-This determines $A_{m}$ and solves the problem. $\square$
+\tag{8}
+$$
+
+This determines $A_m$ whenever its denominator is nonzero. With $k_m=m\pi/a$, a resonant mode satisfies $k_m\sinh(k_mb)-2\cosh(k_mb)=0$. At such a mode the corresponding sine coefficient of $f$ must vanish for solvability, and then $A_m$ is arbitrary. Thus arbitrary $a,b$ do not guarantee a unique solution. $\square$
 
 In the previous examples, we always dealt with the nonhomogeneous condition last. This approach relied heavily on the fact that in each case the partial differential equation and three of the boundary conditions were homogeneous; so the infinite sum of product solutions still satisfied the equation and the homogeneous conditions. In boundary value problems where more than one boundary condition is nonhomogeneous, we can use linearity to break up the problem into subproblems in which at most one boundary condition is nonhomogeneous. We illustrate with examples.
 
-## EXAMPLE 3 Decomposition of boundary conditions
+> [!exercise|becdcdcf-b68d-5889-8f88-941586b914ac.local at=0c952943-3068-5441-9789-5bf3b2956343] EXAMPLE 3 Decomposition of boundary conditions
+> Solve $\Delta u=0$ on $0<x<a$, $0<y<b$, with $u(0,y)=u(a,y)=0$, $u(x,0)=g(x)$ and $u_y(x,b)=f(x)$, by decomposing the boundary data as in Figure 4.
+
+##### solution
 
 The boundary value problem in Figure 4(a) has two nonhomogeneous boundary conditions on the horizontal sides. We can write it as the sum of two subproblems where in each case three of the boundary conditions are homogeneous (Figures 4(b) and (c)). You should check that if $u_{1}$ is a solution of problem $\# 1$ and $u_{2}$ is a solution of problem \#2, then $u=u_{1}+u_{2}$ is a solution of the original problem in Figure 4(a). We now proceed to solve the subproblems.
 
-![](./images/e7203df9-f76c-453b-be1e-147d5ba42d96-81_386_1639_551_88.jpg)
-Figure 4 Decomposition of the boundary value problem in Example 3. Problem \# 1 in Figure 4(b) is solved in Example 1. We have from (5) and (6)
+```scientific-figure
+id: 5cea5edb-b4dc-49f8-8afd-c98695a66c4e
+numbered: false
+title: ""
+caption: Figure 4 Decomposition of the boundary value problem in Example 3.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 11 Partial Differential Equations in Rectangular Coordinates/images/e7203df9-f76c-453b-be1e-147d5ba42d96-81_386_1639_551_88.jpg
+    caption: ""
+```
+
+
+Problem \# 1 in Figure 4(b) is solved in Example 1. We have from (5) and (6)
 
 $$
 u_{1}(x, y)=\sum_{m=1}^{\infty} B_{m} \sin \frac{m \pi}{a} x \sinh \frac{m \pi}{a} y
@@ -159,149 +218,287 @@
 
 In the next example, we have to break up nonhomogeneous boundary conditions (including a Robin condition) into two parts.
 
-## EXAMPLE 4 Decomposition of boundary conditions
+> [!exercise|104cbe3f-8030-57e9-9180-662cff937a6f.local at=e8cfd92a-747d-5f2e-a526-f195ca5e712e] EXAMPLE 4 Decomposition of boundary conditions
+> Decompose the problem $\Delta u=0$ on $0<x<a$, $0<y<b$, with $u(0,y)=u(a,y)=0$, $u_y(x,0)+2u(x,0)=g(x)$ and $u_y(x,b)=f(x)$, into problems with one nonhomogeneous boundary condition each (Figure 5).
+
+##### solution
 
 The boundary value problem in Figure 5(a) has two nonhomogeneous boundary conditions on the horizontal sides. To solve the problem, we break it up into two subproblems with three homogeneous boundary conditions each. It is straightforward to check that if $u_{1}$ is a solution of problem \#1 and $u_{2}$ is a solution of problem \#2, then $u=u_{1}+u_{2}$ is a solution of the original problem.
 
-![](./images/e7203df9-f76c-453b-be1e-147d5ba42d96-82_383_1626_430_134.jpg)
-Figure 5 Decomposition of the boundary value problem in Example 4.
+```scientific-figure
+id: 62a5f321-85f2-441b-8097-d9ae05b88c82
+numbered: false
+title: ""
+caption: Figure 5 Decomposition of the boundary value problem in Example 4.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 11 Partial Differential Equations in Rectangular Coordinates/images/e7203df9-f76c-453b-be1e-147d5ba42d96-82_383_1626_430_134.jpg
+    caption: ""
+```
+
 The problem in Figure 5(b) was solved in Example 2. The problem in Figure 5(c) has only one nonhomogeneous boundary condition and can be solved by the methods of this section. We leave the details to Exercise 3.
 
 Further properties of Neumann conditions (e.g., their compatibility) and interesting applications involving the two-dimensional heat equation are presented in the exercises.
 
-## Exercises 3.10
-
-In Exercises 1-3, solve the boundary value problem described by the figure (Figures 6-8).
-1.
-
-![](./images/e7203df9-f76c-453b-be1e-147d5ba42d96-82_366_448_1322_126.jpg)
-Figure 6 for Exercise 1.
-
-2. 
-
-![](./images/e7203df9-f76c-453b-be1e-147d5ba42d96-82_363_452_1325_714.jpg)
-Figure 7 for Exercise 2.
-
-3. 
-
-![](./images/e7203df9-f76c-453b-be1e-147d5ba42d96-82_366_440_1325_1322.jpg)
-Figure 8 for Exercise 3.
-
-4. (a) Prove the following variant of Proposition 1: If $\phi(x, y)=X(x) Y(y)$ is a product solution of Laplace's equation in the $a \times b$-rectangle of Figure 9, with the zero Neumann conditions on the vertical sides, then $\phi(x, y)=B_{0} y+A_{0}$ or
-
-$$
-\phi(x, y)=\phi_{m}(x, y)=\cos \frac{m \pi}{a} x\left(A_{m} \cosh \frac{m \pi}{a} y+B_{m} \sinh \frac{m \pi}{a} y\right),
-$$
-
-where $m=1,2, \ldots$, and $A_{m}$ and $B_{m}$ are arbitrary constants.
-(b) For $m=1,2, \ldots$, show that, alternatively,
-
-$$
-\phi_{m}(x, y)=\cos \frac{m \pi}{a} x\left(\alpha_{m} \cosh \frac{m \pi}{a}(\beta-y)+\beta_{m} \sinh \frac{m \pi}{a}(\beta-y)\right) .
-$$
-
-In Exercises 5-6, solve the boundary value problem described by the figure (Figures 10-11). Use Exercise 4.
-5.
-
-![](./images/e7203df9-f76c-453b-be1e-147d5ba42d96-83_366_442_317_75.jpg)
-Figure 9 for Exercise 4.
-
-![](./images/e7203df9-f76c-453b-be1e-147d5ba42d96-83_380_463_1287_21.jpg)
-Figure 12 Plate with one radiating side.
-
-6. 
-
-![](./images/e7203df9-f76c-453b-be1e-147d5ba42d96-83_366_448_317_662.jpg)
-Figure 10 for Exercise 5.
-
-![](./images/e7203df9-f76c-453b-be1e-147d5ba42d96-83_366_445_317_1269.jpg)
-Figure 11 for Exercise 6.
-
-In Exercises 7-10, (a) solve the given boundary value problem. (b) Check the validity of your answer by verifying the boundary conditions.
-7. The boundary value problem in Figure 2, with $a=b=\pi$ and $f(x)=\sin 2 x$.
-8. The boundary value problem in Figure 3, with $a=b=\pi$ and $f(x)=\sin x$.
-9. The boundary value problem in Figure 4(a), with $a=b=\pi$ and $f(x)=g(x)=1$.
-10. The boundary value problem in Figure 8 with $a=b=\pi$ and $g(x)=1$.
-11. Project Problem: Insulated plate with one radiating side. Here we outline a solution of the heat equation
-
-$$
-u_{t}=c^{2}\left(u_{x x}+u_{y y}\right), \quad 0<x<a, 0<y<b, t>0
-$$
-
-subject to the initial condition $u(x, y, 0)=f(x, y)$ and the (Robin) boundary conditions described in Figure 12. The problem models the temperature distribution in an insulated rectangular plate with three sides kept at 0 temperature and one side loosing heat to the surrounding medium at a rate proportional to its temperature, with convection coefficient (or heat transfer constant) $\kappa>0$.
-(a) Use the separation of variables method to show that, if $u(x, y, t)=X(x) Y(y) T(t)$ is a product solution of the equation and the boundary conditions (do not worry about the initial condition at this point), then
-
-$$
-\begin{gathered}
-X^{\prime \prime}+\mu^{2} X=0, \quad X(0)=0, \quad X^{\prime}(a)=-\kappa X(a), \\
-Y^{\prime \prime}+\nu^{2} Y=0, \quad Y(0)=0, \quad Y(b)=0, \\
-T^{\prime}+c^{2}\left(\mu^{2}+\nu^{2}\right) T=0 .
-\end{gathered}
-$$
-
-(b) Show that
-
-$$
-\begin{gathered}
-X=X_{m}=\sin \mu_{m} x, \quad m=1,2, \ldots, \\
-Y=Y_{n}=\sin \frac{n \pi}{b} y, \quad n=1,2, \ldots, \\
-T=T_{m n}=e^{-\lambda_{m n}^{2} t}, \quad m, n=1,2, \ldots,
-\end{gathered}
-$$
-
-where $\mu_{m}$ is the $m$ th positive root of the transcendental equation $\tan a \mu=-\frac{\mu}{\kappa}$, and $\lambda_{m n}^{2}=c^{2}\left(\mu_{m}^{2}+\left(\frac{n \pi}{b}\right)^{2}\right)$. (See Example 2, Section 11.6.)
-(c) Superpose the product solutions and use the initial condition to show that the solution of the problem is
-
-$$
-u(x, y, t)=\sum_{n=1}^{\infty} \sum_{m=1}^{\infty} B_{m n} e^{-\lambda_{m n}^{2} t} \sin \mu_{m} x \sin \frac{n \pi}{b} y,
-$$
-
-where
-
-$$
-B_{m n}=\frac{2}{b \int_{0}^{a} \sin ^{2} \mu_{m} x d x} \int_{0}^{b} \int_{0}^{a} f(x, y) \sin \mu_{m} x \sin \frac{n \pi}{b} y d x d y .
-$$
-
-(Note: The double sine series that arise here differ from those of Section 11.7 in one major way: The functions $\sin \mu_{m} x$ do not have a common period. But like the double Fourier sine series of Section 11.7, these "generalized double Fourier series" can be used to expand any reasonably well-behaved function $f(x, y)$. This follows because the functions $\sin \mu_{m} x$ form a complete orthogonal set of functions on the interval $[0, a]$ (see the comments preceeding Example 3 in Section 11.6), and the functions $\sin \frac{n \pi}{b} y$ form a complete orthogonal set of functions on the interval $[0, b]$ (half-range sine series expansions). In general, whenever $\left(f_{m}(x)\right)_{m=1}^{\infty}$ is a complete set of orthogonal functions on $[a, b]$ and $\left(g_{n}(y)\right)_{n=1}^{\infty}$ is a complete set of orthogonal functions on $[c, d]$, it is straightforward to show that $\left(f_{m}(x) g_{n}(y)\right)_{m, n=1}^{\infty}$ are orthogonal functions on the rectangle $[a, b] \times[c, d]$. Using basic tools from analysis in higher dimensions, we can show that they also form a complete set of functions on $[a, b] \times[c, d]$.)
-12. (a) Solve the heat problem in Exercise 11 with $a=1, b=\pi, c=1, \kappa=1$, $f(x, y)=x(1-x) \sin y$. (Example 3, Section 11.6, is very helpful.)
-(b) Write down at least five product solutions and form a partial sum of the series solution.
-(c) Consider $u\left(\frac{1}{2}, \frac{\pi}{2}, t\right)$, the temperature of the point $\left(\frac{1}{2}, \frac{\pi}{2}\right)$, and $u\left(\frac{1}{2}, t\right)$, the temperature of the point $x=\frac{1}{2}$ in Example 3, Section 11.6. Which temperature decays faster? Justify your answer by comparing the analytical series solutions and by giving reasons based on the physical interpretation of the problems.
-13. Project Problem: Compatibility of boundary conditions in Neumann problems. A Neumann problem on a rectangle $R$ is a boundary value problem consisting of Laplace's equation and Neumann boundary conditions: $\nabla^{2} u(x, y)=0$ for all $(x, y)$ in $R$, and $\frac{\partial u}{\partial n} u(x, y)=f(x, y)$ for all $(x, y)$ on the boundary of $R$. In this problem, all sides are exchanging heat with the surrounding medium at a rate given by $f$. The total flux of heat is the integral of $f$ along the boundary of $R$. Since $u$ is a steady-state solution, the total flux of heat across the boundary must be 0 . This means that $f$ cannot be arbitrary; it must satisfy the compatibility condition
-
-$$
-\int_{0}^{a} f(x, 0) d x+\int_{0}^{b} f(a, y) d y-\int_{0}^{a} f(x, b) d x-\int_{0}^{b} f(0, y) d y=0
-$$
-
-This condition can be derived by using properties of harmonic functions and Green's identities (see Chapter 12). Here we show that it is necessary in order to solve the Neumann problem using Fourier series and separation of variables. To simplify the
-presentation, we consider the problem in Figure 13.
-
-![](./images/e7203df9-f76c-453b-be1e-147d5ba42d96-85_378_414_278_31.jpg)
-Figure 13 A Neumann problem.
-
-(a) Using the product solutions found in Exercise 4, show that the solution is of the form
-
-$$
-u(x, y)=A_{0}+\sum_{m=1}^{\infty} A_{m} \cos \frac{m \pi}{a} x \cosh \frac{m \pi}{a} y
-$$
-
-(b) Show that
-
-$$
-f(x)=\sum_{m=1}^{\infty} \frac{m \pi}{a} A_{m} \sinh \frac{m \pi b}{a} \cos \frac{m \pi}{a} x .
-$$
-
-(c) Conclude from (b) that $f$ must satisfy the compatibility condition
-
-$$
-\int_{0}^{a} f(x) d x=0
-$$
-
-[Hint: What are the cosine Fourier coefficients of $f$ ?]
-(d) Show that for $m=1,2, \ldots$,
-
-$$
-A_{m}=\frac{2}{m \pi \sinh \frac{m \pi b}{a}} \int_{0}^{a} f(x) \cos \frac{m \pi}{a} x d x
-$$
-
-This determines the solution $u(x, y)$ up to an arbitrary constant $A_{0}$. This is to be expected, since the problem does not have a unique solution. Indeed, if $u(x, y)$ is a solution, then it is not difficult to check that $u(x, y)+C$ is also a solution, where $C$ is an arbitrary constant.
-14. Solve the problem in Figure 13, with $a=b=\pi$, and $f(x)=\frac{\pi}{2}-x$ for $0<x<\pi$.
+## Exercises 11.10
+
+
+> [!prompt|90673ce8-04cc-59e9-8b22-7fafabfc6ddf.local at=a62cebca-e2bf-50b2-b276-ff23c6ffdb3d] Shared exercise instructions
+> In Exercises 1-3, solve the boundary value problem described by the figure (Figures 6-8).
+
+
+> [!exercise|20289241-c005-59aa-afa4-77bf61e729f4.local at=3bdc7679-181d-5937-b220-55de1b42c677] Exercise 1
+> Use the accompanying figure and the shared instructions.
+
+
+```scientific-figure
+id: bcf2ac39-dd12-4439-a998-12611f5892a2
+numbered: false
+title: ""
+caption: Figure 6 for Exercise 1.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 11 Partial Differential Equations in Rectangular Coordinates/images/e7203df9-f76c-453b-be1e-147d5ba42d96-82_366_448_1322_126.jpg
+    caption: ""
+```
+> [!exercise|9015efd6-a148-5d45-a740-9362b0f6e46b.local at=b4078381-a84c-5c63-86fd-e093129a2b9e] Exercise 2
+> Use the accompanying figure and the shared instructions.
+
+
+```scientific-figure
+id: d7585611-01f1-4899-88d2-97dd294086ad
+numbered: false
+title: ""
+caption: Figure 7 for Exercise 2.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 11 Partial Differential Equations in Rectangular Coordinates/images/e7203df9-f76c-453b-be1e-147d5ba42d96-82_363_452_1325_714.jpg
+    caption: ""
+```
+> [!exercise|f1e0b7ca-37bd-5062-9114-7cbae2b6356a.local at=9d14e5b0-8cbf-5eea-80d4-7234da364caf] Exercise 3
+> Use the accompanying figure and the shared instructions.
+
+
+```scientific-figure
+id: d106e911-4bc2-4d17-bdbc-de97d915fa7f
+numbered: false
+title: ""
+caption: Figure 8 for Exercise 3.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 11 Partial Differential Equations in Rectangular Coordinates/images/e7203df9-f76c-453b-be1e-147d5ba42d96-82_366_440_1325_1322.jpg
+    caption: ""
+```
+> [!exercise|22196233-74cc-5ad5-86f4-f0a7a528b6f3.local at=4d925fd3-989e-5273-a6fb-f90b79f59a55] Exercise 4
+> (a) Prove the following variant of Proposition 1: If $\phi(x, y)=X(x) Y(y)$ is a product solution of Laplace's equation in the $a \times b$-rectangle of Figure 9, with the zero Neumann conditions on the vertical sides, then $\phi(x, y)=B_{0} y+A_{0}$ or
+>
+> $$
+> \phi(x, y)=\phi_{m}(x, y)=\cos \frac{m \pi}{a} x\left(A_{m} \cosh \frac{m \pi}{a} y+B_{m} \sinh \frac{m \pi}{a} y\right),
+> $$
+>
+> where $m=1,2, \ldots$, and $A_{m}$ and $B_{m}$ are arbitrary constants.
+> (b) For $m=1,2, \ldots$, show that, alternatively,
+>
+> $$
+> \phi_{m}(x, y)=\cos \frac{m \pi}{a} x\left(\alpha_{m} \cosh \frac{m \pi}{a}(\beta-y)+\beta_{m} \sinh \frac{m \pi}{a}(\beta-y)\right) .
+> $$
+
+
+```scientific-figure
+id: 7bff47e4-58ea-429f-be38-89a2eac81e23
+numbered: false
+title: ""
+caption: Figure 9 for Exercise 4.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 11 Partial Differential Equations in Rectangular Coordinates/images/e7203df9-f76c-453b-be1e-147d5ba42d96-83_366_442_317_75.jpg
+    caption: ""
+```
+> [!prompt|11cdb13a-b253-5947-8430-341cea9c7ccb.local at=8516c069-32e1-58c6-9cfa-ed4578ff988e] Shared exercise instructions
+> In Exercises 5-6, solve the boundary value problem described by the figure (Figures 10-11). Use Exercise 4.
+
+
+> [!exercise|319a73a3-d8b8-512a-8f59-3f94e12693e6.local at=f4cd1347-e96d-52a1-b97a-5962d3389165] Exercise 5
+> Solve the problem in Figure 10.
+
+
+```scientific-figure
+id: 2a74babf-cf9f-41af-8ef6-9bc8cd410c29
+numbered: false
+title: ""
+caption: Figure 10 for Exercise 5.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 11 Partial Differential Equations in Rectangular Coordinates/images/e7203df9-f76c-453b-be1e-147d5ba42d96-83_366_448_317_662.jpg
+    caption: ""
+```
+> [!exercise|26a8e453-6207-5b28-8480-53520358449b.local at=21ee9d3b-d07c-5ad0-a44e-98f38f6b07aa] Exercise 6
+> Solve the problem in Figure 11.
+
+
+```scientific-figure
+id: d8d8156d-f32c-449d-a3d9-b5cd07495c1c
+numbered: false
+title: ""
+caption: Figure 11 for Exercise 6.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 11 Partial Differential Equations in Rectangular Coordinates/images/e7203df9-f76c-453b-be1e-147d5ba42d96-83_366_445_317_1269.jpg
+    caption: ""
+```
+> [!prompt|03983474-7f60-56cc-ba7e-35cf3c75b574.local at=bb63475a-9895-588c-86da-7ea96e796a2b] Shared exercise instructions
+> In Exercises 7-10, (a) solve the given boundary value problem. (b) Check the validity of your answer by verifying the boundary conditions.
+
+
+> [!exercise|18e4345b-22b0-546f-8c34-7dfca6915043.local at=26b86322-c69e-54fe-9d3a-e0ae3a934ee7] Exercise 7
+> The boundary value problem in Figure 2, with $a=b=\pi$ and $f(x)=\sin 2 x$.
+
+
+> [!exercise|bf6aac60-077c-5849-b096-31587ef7fb4f.local at=f11f59e1-a9ec-5248-93d9-0512007cdfcf] Exercise 8
+> The boundary value problem in Figure 3, with $a=b=\pi$ and $f(x)=\sin x$.
+
+
+> [!exercise|d9bf3b06-208f-5bae-a349-88609c0611eb.local at=34e3acc9-f4dd-588f-a337-d67872267c7e] Exercise 9
+> The boundary value problem in Figure 4(a), with $a=b=\pi$ and $f(x)=g(x)=1$.
+
+
+> [!exercise|80db4e15-fb59-50ac-8782-dd99e09e9377.local at=7d68f45d-c7e9-5d4f-8696-ec4cd2b274f2] Exercise 10
+> The boundary value problem in Figure 8 with $a=b=\pi$ and $g(x)=1$.
+
+
+> [!exercise|9f129952-3162-56fe-9c35-4415780b3c30.local at=dc9a61f4-d3fb-5562-85f0-76479f4a9fa0] Exercise 11
+> Project Problem: Insulated plate with one radiating side. Here we outline a solution of the heat equation
+>
+> $$
+> u_{t}=c^{2}\left(u_{x x}+u_{y y}\right), \quad 0<x<a, 0<y<b, t>0
+> $$
+>
+> subject to the initial condition $u(x, y, 0)=f(x, y)$ and the (Robin) boundary conditions described in Figure 12. The problem models the temperature distribution in an insulated rectangular plate with three sides kept at 0 temperature and one side losing heat to the surrounding medium at a rate proportional to its temperature, with convection coefficient (or heat transfer constant) $\kappa>0$.
+> (a) Use the separation of variables method to show that, if $u(x, y, t)=X(x) Y(y) T(t)$ is a product solution of the equation and the boundary conditions (do not worry about the initial condition at this point), then
+>
+> $$
+> \begin{gathered}
+> X^{\prime \prime}+\mu^{2} X=0, \quad X(0)=0, \quad X^{\prime}(a)=-\kappa X(a), \\
+> Y^{\prime \prime}+\nu^{2} Y=0, \quad Y(0)=0, \quad Y(b)=0, \\
+> T^{\prime}+c^{2}\left(\mu^{2}+\nu^{2}\right) T=0 .
+> \end{gathered}
+> $$
+>
+> (b) Show that
+>
+> $$
+> \begin{gathered}
+> X=X_{m}=\sin \mu_{m} x, \quad m=1,2, \ldots, \\
+> Y=Y_{n}=\sin \frac{n \pi}{b} y, \quad n=1,2, \ldots, \\
+> T=T_{m n}=e^{-\lambda_{m n}^{2} t}, \quad m, n=1,2, \ldots,
+> \end{gathered}
+> $$
+>
+> where $\mu_{m}$ is the $m$ th positive root of the transcendental equation $\tan a \mu=-\frac{\mu}{\kappa}$, and $\lambda_{m n}^{2}=c^{2}\left(\mu_{m}^{2}+\left(\frac{n \pi}{b}\right)^{2}\right)$. (See Example 2, Section 11.6.)
+> (c) Superpose the product solutions and use the initial condition to show that the solution of the problem is
+>
+> $$
+> u(x, y, t)=\sum_{n=1}^{\infty} \sum_{m=1}^{\infty} B_{m n} e^{-\lambda_{m n}^{2} t} \sin \mu_{m} x \sin \frac{n \pi}{b} y,
+> $$
+>
+> where
+>
+> $$
+> B_{m n}=\frac{2}{b \int_{0}^{a} \sin ^{2} \mu_{m} x d x} \int_{0}^{b} \int_{0}^{a} f(x, y) \sin \mu_{m} x \sin \frac{n \pi}{b} y d x d y .
+> $$
+>
+> (Note: The double sine series that arise here differ from those of Section 11.7 in one major way: The functions $\sin \mu_{m} x$ do not have a common period. But like the double Fourier sine series of Section 11.7, these "generalized double Fourier series" can be used to expand any reasonably well-behaved function $f(x, y)$. This follows because the functions $\sin \mu_{m} x$ form a complete orthogonal set of functions on the interval $[0, a]$ (see the comments preceding Example 3 in Section 11.6), and the functions $\sin \frac{n \pi}{b} y$ form a complete orthogonal set of functions on the interval $[0, b]$ (half-range sine series expansions). In general, whenever $\left(f_{m}(x)\right)_{m=1}^{\infty}$ is a complete set of orthogonal functions on $[a, b]$ and $\left(g_{n}(y)\right)_{n=1}^{\infty}$ is a complete set of orthogonal functions on $[c, d]$, it is straightforward to show that $\left(f_{m}(x) g_{n}(y)\right)_{m, n=1}^{\infty}$ are orthogonal functions on the rectangle $[a, b] \times[c, d]$. Using basic tools from analysis in higher dimensions, we can show that they also form a complete set of functions on $[a, b] \times[c, d]$.)
+
+
+```scientific-figure
+id: 1a6296f0-e422-4bba-9b69-c85bcec7986d
+numbered: false
+title: ""
+caption: Figure 12 Plate with one radiating side.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 11 Partial Differential Equations in Rectangular Coordinates/images/e7203df9-f76c-453b-be1e-147d5ba42d96-83_380_463_1287_21.jpg
+    caption: ""
+```
+
+
+
+
+
+> [!exercise|173746f3-3e06-5cf6-81ce-9c36c7b2069b.local at=8ca7b81d-c47a-5803-a109-55dbf37d0260] Exercise 12
+> (a) Solve the heat problem in Exercise 11 with $a=1, b=\pi, c=1, \kappa=1$, $f(x, y)=x(1-x) \sin y$. (Example 3, Section 11.6, is very helpful.)
+> (b) Write down at least five product solutions and form a partial sum of the series solution.
+> (c) Consider $u\left(\frac{1}{2}, \frac{\pi}{2}, t\right)$, the temperature of the point $\left(\frac{1}{2}, \frac{\pi}{2}\right)$, and $u\left(\frac{1}{2}, t\right)$, the temperature of the point $x=\frac{1}{2}$ in Example 3, Section 11.6. Which temperature decays faster? Justify your answer by comparing the analytical series solutions and by giving reasons based on the physical interpretation of the problems.
+
+
+> [!exercise|be320946-b233-5127-a022-843857857537.local at=35aae433-a4d6-52e3-891f-5bac74cfe8d4] Exercise 13
+> Project Problem: Compatibility of boundary conditions in Neumann problems. A Neumann problem on a rectangle $R$ is a boundary value problem consisting of Laplace's equation and Neumann boundary conditions: $\nabla^{2} u(x, y)=0$ for all $(x, y)$ in $R$, and $\frac{\partial u}{\partial n}(x, y)=f(x, y)$ for all $(x, y)$ on the boundary of $R$. In this problem, all sides are exchanging heat with the surrounding medium at a rate given by $f$. For constant thermal conductivity $K>0$, the total outward heat flux is $-K\int_{\partial R}f\,ds$, because $f$ is the outward normal temperature derivative. Since $u$ is a steady-state solution, the total flux of heat across the boundary must be 0 . This means that $f$ cannot be arbitrary; it must satisfy the compatibility condition
+>
+> $$
+> \int_{0}^{a} f(x,0)\,dx+\int_{0}^{b}f(a,y)\,dy+\int_{0}^{a}f(x,b)\,dx+\int_{0}^{b}f(0,y)\,dy=0
+> $$
+>
+> All four integrals have plus signs because $f$ is defined as the outward normal derivative on each side; the outward-normal signs are already included in $f$. This condition can be derived by using properties of harmonic functions and Green's identities (see Chapter 16). Here we show that it is necessary in order to solve the Neumann problem using Fourier series and separation of variables. To simplify the
+> presentation, we consider the problem in Figure 13.
+>
+> (a) Using the product solutions found in Exercise 4, show that the solution is of the form
+>
+> $$
+> u(x, y)=A_{0}+\sum_{m=1}^{\infty} A_{m} \cos \frac{m \pi}{a} x \cosh \frac{m \pi}{a} y
+> $$
+>
+> (b) Show that
+>
+> $$
+> f(x)=\sum_{m=1}^{\infty} \frac{m \pi}{a} A_{m} \sinh \frac{m \pi b}{a} \cos \frac{m \pi}{a} x .
+> $$
+>
+> (c) Conclude from (b) that $f$ must satisfy the compatibility condition
+>
+> $$
+> \int_{0}^{a} f(x) d x=0
+> $$
+>
+> [Hint: What are the cosine Fourier coefficients of $f$ ?]
+> (d) Show that for $m=1,2, \ldots$,
+>
+> $$
+> A_{m}=\frac{2}{m \pi \sinh \frac{m \pi b}{a}} \int_{0}^{a} f(x) \cos \frac{m \pi}{a} x d x
+> $$
+>
+> This determines the solution $u(x, y)$ up to an arbitrary constant $A_{0}$. This is to be expected, since the problem does not have a unique solution. Indeed, if $u(x, y)$ is a solution, then it is not difficult to check that $u(x, y)+C$ is also a solution, where $C$ is an arbitrary constant.
+
+
+```scientific-figure
+id: e80cda8b-1056-42d4-ac3e-9df5ac0e25ee
+numbered: false
+title: ""
+caption: Figure 13 A Neumann problem.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 11 Partial Differential Equations in Rectangular Coordinates/images/e7203df9-f76c-453b-be1e-147d5ba42d96-85_378_414_278_31.jpg
+    caption: ""
+```
+
+
+
+> [!exercise|0b4d5752-def5-5144-ac9e-8872a5a23801.local at=f0908e54-a8ba-5a3b-a35e-41dbfe78dccf] Exercise 14
+> Solve the problem in Figure 13, with $a=b=\pi$, and $f(x)=\frac{\pi}{2}-x$ for $0<x<\pi$.

`````
