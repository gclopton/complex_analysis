
# Editorial records

Reading note: 11.9 Poisson's Equation: The Method of Eigenfunction Expansions.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!equation|930aae7c-1ac9-5c9f-be40-285f192fbff5.local at=5ebb093c-bf33-5e97-ad7e-952ab63cd4bb] Eigenfunction solution of the rectangular Poisson problem with Dirichlet data
> Let $a,b>0$, $\Omega=(0,a)\times(0,b)$, and consider $\Delta u=f$ with prescribed Dirichlet boundary values $h$. Write $u=u_0+v$, where $v$ solves $\Delta v=0$ with boundary values $h$. The zero-boundary part is
> $$
> u_0(x,y)=\sum_{n=1}^{\infty}\sum_{m=1}^{\infty}E_{mn}\sin\frac{m\pi x}{a}\sin\frac{n\pi y}{b},
> $$
> where
> $$
> \lambda_{mn}=\left(\frac{m\pi}{a}\right)^2+\left(\frac{n\pi}{b}\right)^2,\qquad
> E_{mn}=-\frac4{ab\lambda_{mn}}\int_0^b\int_0^a f(x,y)\sin\frac{m\pi x}{a}\sin\frac{n\pi y}{b}\,dx\,dy.
> $$
> For $f\in L^2(\Omega)$ the series gives the weak zero-Dirichlet solution; use classical differentiations only when the data and convergence justify them. The harmonic part $v$ must have the prescribed boundary trace, with corner compatibility required for continuity on the closed rectangle.
````
### After

````text
> [!equation|930aae7c-1ac9-5c9f-be40-285f192fbff5.local at=5ebb093c-bf33-5e97-ad7e-952ab63cd4bb] Solution of Poisson's Equation in a Rectangle
> Let $a,b>0$, $\Omega=(0,a)\times(0,b)$, and consider $\Delta u=f$ with prescribed Dirichlet boundary values $h$. Write $u=u_1+u_2$, where $u_2$ solves $\Delta v=0$ with boundary values $h$. The zero-boundary part is
> $$
> u_1(x,y)=\sum_{n=1}^{\infty}\sum_{m=1}^{\infty}E_{mn}\sin\frac{m\pi x}{a}\sin\frac{n\pi y}{b},
> $$
> where
> $$
> \lambda_{mn}=\left(\frac{m\pi}{a}\right)^2+\left(\frac{n\pi}{b}\right)^2,\qquad
> E_{mn}=-\frac4{ab\lambda_{mn}}\int_0^b\int_0^a f(x,y)\sin\frac{m\pi x}{a}\sin\frac{n\pi y}{b}\,dx\,dy.
> $$
> Assume the data and convergence justify the displayed expansion and the required differentiations.
````

## Source-to-current comparison

Source: /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 11 Partial Differential Equations in Rectangular Coordinates/11.9 Poisson's Equation: The Method of Eigenfunction Expansions.md

This exact comparison preserves the full change evidence, including formatting, OCR corrections, restored source wording, and required standalone context. The entries above explain the recovery edits. The comparison is not a claim that every difference is a correction; component serialization, callout wrapping, and printed labels outside callouts are formatting.

`````diff
--- /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 11 Partial Differential Equations in Rectangular Coordinates/11.9 Poisson's Equation: The Method of Eigenfunction Expansions.md
+++ /Users/gradyclopton/ObsidianVaults/complex_analysis/Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 11 Partial Differential Equations in Rectangular Coordinates/11.9 Poisson's Equation: The Method of Eigenfunction Expansions.md
@@ -1,3 +1,4 @@
+
 ### 11.9 Poisson's Equation: The Method of Eigenfunction Expansions
 
 In this section, we present a new approach to boundary value problems involving the Laplacian. The method that we describe is called the eigenfunction expansion method. We will use it to derive alternative solutions of previous problems that were solved using the separation of variables method. More importantly, we will solve nonhomogeneous problems that we could not solve by previous methods.
@@ -7,22 +8,43 @@
 
 $$
 \nabla^{2} u=\frac{\partial^{2} u}{\partial x^{2}}+\frac{\partial^{2} u}{\partial y^{2}}=f(x, y)
+\tag{1}
 $$
 
 Poisson's equation arises in steady-state heat problems with time independent heat sources. It is nonhomogeneous when $f(x, y) \neq 0$ and cannot be solved directly by the method of separation of variables. Our goal in this section is to solve boundary value problems involving this equation and introduce in the process the very useful method of eigenfunction expansions.
 
-Figure 1 A general Poisson problem on a rectangle.
-![](./images/e7203df9-f76c-453b-be1e-147d5ba42d96-68_398_1031_1641_698.jpg)
-
-As we did in Section 11.8, the first step in solving the general Poisson problem in Figure 1 consists of decomposing the problem into simpler subproblems,
-
-Figure 2 Decomposition of a general Poisson problem.
+```scientific-figure
+id: 32594c9b-4e5d-4a26-9574-16df55bf8f57
+numbered: false
+title: ""
+caption: Figure 1 A general Poisson problem on a rectangle.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 11 Partial Differential Equations in Rectangular Coordinates/images/e7203df9-f76c-453b-be1e-147d5ba42d96-68_398_1031_1641_698.jpg
+    caption: ""
+```
+
+
+As we did in Section 11.8, the first step in solving the general Poisson problem in Figure 1 consists of decomposing the problem into simpler subproblems, using the superposition principle. The decomposition in the present case is described by Figure 2.
+```scientific-figure
+id: d806bb8d-f2a7-4004-b2f3-8fd908bd15db
+numbered: false
+title: ""
+caption: Figure 2 Decomposition of a general Poisson problem.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 11 Partial Differential Equations in Rectangular Coordinates/images/e7203df9-f76c-453b-be1e-147d5ba42d96-69_500_1275_299_513.jpg
+    caption: ""
+```
+
+
+Figure 2(b) describes a Dirichlet problem that can be solved by the methods of the previous section. Thus, to complete the solution of the problem in Figure 1, we only need to treat Poisson's equation with zero boundary data (Figure 2(a)).
 
 Note that summing over all the functions $\sin \frac{m \pi}{a} x \sin \frac{n \pi}{b} y$ leads to a double Fourier sine series form of the solution (Section 11.7).
-using the superposition principle. The decomposition in the present case is described by Figure 2.
-![](./images/e7203df9-f76c-453b-be1e-147d5ba42d96-69_500_1275_299_513.jpg)
-
-Figure 2(b) describes a Dirichlet problem that can be solved by the methods of the previous section. Thus, to complete the solution of the problem in Figure 1, we only need to treat Poisson's equation with zero boundary data (Figure 2(a)).
 
 We will take a hint from the solution of the Dirichlet problem (Section 11.8), which is a special case of our problem when $f(x, y)=0$, and consider the function $\phi_{m n}(x, y)=\sin \frac{m \pi}{a} x \sin \frac{n \pi}{b} y$, which clearly satisfies the 0 boundary conditions in Figure 2(a). The function $\phi_{m n}$ also satisfies another important property. Computing the Laplacian of $\phi_{m n}(x, y)$ we find
 
@@ -39,41 +61,47 @@
 \lambda_{m n}=\left(\frac{m \pi}{a}\right)^{2}+\left(\frac{n \pi}{b}\right)^{2} \quad(m, n=1,2, \ldots)
 $$
 
-an eigenvalue of the Laplacian and the function $\phi_{m n}(x, y)=\sin \frac{m \pi}{a} x \sin \frac{n \pi}{b} y$ the corresponding eigenfunction. Because the effect of the Laplacian on an eigenfunction is very simple to describe (it just multiplies the eigenfunction by a constant), it makes sense to try a series of eigenfunctions for a solution to a problem that involves the Laplacian over a rectangle. This idea will be clarified as we carry out the solution of the problem in Figure 2(a). Let us try for a solution
+an eigenvalue of the negative Laplacian $-\nabla^2$ (the eigenvalue of $\nabla^2$ itself is $-\lambda_{mn}$), and the function $\phi_{m n}(x, y)=\sin \frac{m \pi}{a} x \sin \frac{n \pi}{b} y$ the corresponding eigenfunction. Because the effect of the Laplacian on an eigenfunction is very simple to describe (it just multiplies the eigenfunction by a constant), it makes sense to try a series of eigenfunctions for a solution to a problem that involves the Laplacian over a rectangle. This idea will be clarified as we carry out the solution of the problem in Figure 2(a). Let us try for a solution
 
 $$
 u(x, y)=\sum_{n=1}^{\infty} \sum_{m=1}^{\infty} E_{m n} \sin \frac{m \pi}{a} x \sin \frac{n \pi}{b} y
+\tag{2}
 $$
 
 where $E_{m n}$ are constants to be determined. It is straightforward to check that $u$ satisfies the zero boundary conditions in Figure 2(a). We now solve for $E_{m n}$ so as to satisfy Poisson's equation (1). As usual, in this process, we will assume that we can interchange the sums and the derivatives. Differentiating twice in (2) and plugging into (1), we obtain
 
 $$
 \sum_{n=1}^{\infty} \sum_{m=1}^{\infty}-E_{m n} \underbrace{\left[\left(\frac{m \pi}{a}\right)^{2}+\left(\frac{n \pi}{b}\right)^{2}\right]}_{\lambda_{m n}} \sin \frac{m \pi}{a} x \sin \frac{n \pi}{b} y=f(x, y) .
+\tag{3}
 $$
 
 Thinking of (3) as a double Fourier sine series expansion of $f(x, y)$ (Theorem 1, Section 11.7), we conclude that
 
 $$
 E_{m n}=\frac{-4}{a b \lambda_{m n}} \int_{0}^{b} \int_{0}^{a} f(x, y) \sin \frac{m \pi}{a} x \sin \frac{n \pi}{b} y d x d y
+\tag{4}
 $$
 
 We have thus completely solved Poisson's problem in Figure 1. We summarize our findings as follows.
 
-SOLUTION OF POISSON'S EQUATION IN A RECTANGLE
-
-The solution of the Poisson problem in Figure 1 is
-
-$$
-u(x, y)=u_{1}(x, y)+u_{2}(x, y)
-$$
-
-where $u_{1}$ is the solution of the Poisson problem with zero boundary data in Figure 2(a), and $u_{2}$ is the solution of the Dirichlet problem in Figure 2(b). The function $u_{1}$ is given by (2) and (4), and the function $u_{2}$ is given by (5)-(9), Section 11.8.
-
-## EXAMPLE 1 A Poisson problem with zero boundary data
-
-Solve $\nabla^{2} u=1$ in a $1 \times 1$ square, subject to the boundary condition $u=0$ on all four sides of the square.
-
-Solution Note that in this case $u_{2}=0$. The function $u_{1}$ is given by (2) and (4) with $a=b=1$ and $f(x, y)=1$. Thus
+> [!equation|930aae7c-1ac9-5c9f-be40-285f192fbff5.local at=5ebb093c-bf33-5e97-ad7e-952ab63cd4bb] Solution of Poisson's Equation in a Rectangle
+> Let $a,b>0$, $\Omega=(0,a)\times(0,b)$, and consider $\Delta u=f$ with prescribed Dirichlet boundary values $h$. Write $u=u_1+u_2$, where $u_2$ solves $\Delta v=0$ with boundary values $h$. The zero-boundary part is
+> $$
+> u_1(x,y)=\sum_{n=1}^{\infty}\sum_{m=1}^{\infty}E_{mn}\sin\frac{m\pi x}{a}\sin\frac{n\pi y}{b},
+> $$
+> where
+> $$
+> \lambda_{mn}=\left(\frac{m\pi}{a}\right)^2+\left(\frac{n\pi}{b}\right)^2,\qquad
+> E_{mn}=-\frac4{ab\lambda_{mn}}\int_0^b\int_0^a f(x,y)\sin\frac{m\pi x}{a}\sin\frac{n\pi y}{b}\,dx\,dy.
+> $$
+> Assume the data and convergence justify the displayed expansion and the required differentiations.
+
+> [!exercise|8abfd9b1-d075-5454-89a4-f06b23aaef8b.local at=7fe8118e-3c52-57b3-8a8a-738706e658a5] EXAMPLE 1 A Poisson problem with zero boundary data
+> Solve $\nabla^{2} u=1$ in a $1 \times 1$ square, subject to the boundary condition $u=0$ on all four sides of the square.
+
+##### solution
+
+Note that in this case $u_{2}=0$. The function $u_{1}$ is given by (2) and (4) with $a=b=1$ and $f(x, y)=1$. Thus
 
 $$
 E_{m n}=\frac{-4}{\lambda_{m n}} \int_{0}^{1} \int_{0}^{1} \sin m \pi x \sin n \pi y d x d y
@@ -88,17 +116,17 @@
 Evaluating the integrals (as we did in Example 2, Section 11.7), and plugging into (2), we obtain the solution
 
 $$
-u(x, y)=\frac{-16}{\pi^{4}} \sum_{l=0}^{\infty} \sum_{k=0}^{\infty} \frac{\sin (2 k+1) \pi x \sin (2 l+1) y}{(2 k+1)(2 l+1)\left((2 k+1)^{2}+(2 l+1)^{2}\right)}
-$$ $\square$
-
-These are the same boundary conditions as in Figure 2(a).
-
+u(x, y)=\frac{-16}{\pi^{4}} \sum_{l=0}^{\infty} \sum_{k=0}^{\infty} \frac{\sin (2 k+1) \pi x \sin (2 l+1) \pi y}{(2 k+1)(2 l+1)\left((2 k+1)^{2}+(2 l+1)^{2}\right)}
+$$
+
+$\square$
 ## The Method of Eigenfunction Expansions
 
 Let us summarize the steps that we used to solve Poisson's problem and describe in the process a general method for solving boundary value problems involving the Laplacian. We considered the functions
 
 $$
 \phi_{m n}(x, y)=\sin \frac{m \pi}{a} x \sin \frac{n \pi}{b} y,
+\tag{5}
 $$
 
 which are solutions (or eigenfunctions) of the following eigenvalue problem:
@@ -110,21 +138,32 @@
 \end{gathered}
 $$
 
+*Printed equation labels: (6) rectangular eigenvalue equation; (7) zero boundary values.*
+
+> [!equation|0e3cc99c-6c2e-55ee-a48d-19e148c954f5.local at=4d6f6877-7109-5c46-8929-86d0cef0a304] Helmholtz equation and the negative Laplacian eigenvalue convention
+> For a scalar field $\phi$ on a spatial domain and a constant spectral parameter $\lambda$, the Helmholtz equation is
+> $$
+> \Delta\phi+\lambda\phi=0.
+> $$
+> A nonzero solution satisfying specified homogeneous boundary conditions is an eigenfunction of $-\Delta$ with eigenvalue $\lambda$. Its eigenvalue for $\Delta$ is $-\lambda$.
+
 Equation (6) is known as the Helmholtz equation. It arises when separating variables in the heat and wave equations (see Exercise 16). Each $\phi_{m n}$ corresponds to the eigenvalue
 
 $$
 \lambda=\lambda_{m n}=\left(\frac{m \pi}{a}\right)^{2}+\left(\frac{n \pi}{b}\right)^{2}, \quad m, n=1,2,3, \ldots .
+\tag{8}
 $$
 
 The method that consists of building up the solution of a boundary value problem as a sum of eigenfunctions of a related Helmholtz problem is known as the method of eigenfunction expansions. The success of this method on a given region depends on whether the eigenfunctions of the Helmholtz problem on that region form a complete set, in the sense that a function defined on the region can be expanded in a series in terms of the eigenfunctions, called an eigenseries expansion. For the rectangle, the eigenseries expansion is the double sine series expansion. Other regions will give rise to different types of series expansions, as we will see in the following chapters.
 
-In our next example, we use the eigenfunction expansion method to solve a nonhomogeneous problems that cannot be tackled directly by the method of separation of variables.
-
-## EXAMPLE 2 The eigenfunction expansion method
-
-Solve $\nabla^{2} u=u+3$ in a $1 \times 1$ square ( $0<x<1,0<y<1$ ), subject to the boundary condition $u=0$ on all four sides of the square.
-
-Solution The associated eigenfunction problem is precisely the one given by (6)(7), with $a=b=1$. The eigenvalues are $\lambda_{m n}=(m \pi)^{2}+(n \pi)^{2}$, with corresponding eigenfunctions $\phi_{m n}(x, y)=\sin m \pi x \sin n \pi y$. This means that $\nabla^{2}\left(\phi_{m n}(x, y)\right)= -\left((m \pi)^{2}+(n \pi)^{2}\right) \phi_{m n}(x, y)$, as you can easily check. Our candidate for a solution is
+In our next example, we use the eigenfunction expansion method to solve a nonhomogeneous problem that cannot be tackled directly by the method of separation of variables.
+
+> [!exercise|3a9e1ce8-c126-547f-a05c-73c8b8a14ed8.local at=81f96e4f-dfe5-559c-8eee-47ba36805cff] EXAMPLE 2 The eigenfunction expansion method
+> Solve $\nabla^{2} u=u+3$ in a $1 \times 1$ square ( $0<x<1,0<y<1$ ), subject to the boundary condition $u=0$ on all four sides of the square.
+
+##### solution
+
+The associated eigenfunction problem is precisely the one given by (6)(7), with $a=b=1$. The eigenvalues are $\lambda_{m n}=(m \pi)^{2}+(n \pi)^{2}$, with corresponding eigenfunctions $\phi_{m n}(x, y)=\sin m \pi x \sin n \pi y$. This means that $\nabla^{2}\left(\phi_{m n}(x, y)\right)= -\left((m \pi)^{2}+(n \pi)^{2}\right) \phi_{m n}(x, y)$, as you can easily check. Our candidate for a solution is
 
 $$
 u(x, y)=\sum_{n=1}^{\infty} \sum_{m=1}^{\infty} E_{m n} \sin m \pi x \sin n \pi y
@@ -173,37 +212,44 @@
 \end{gathered}
 $$
 
+*Printed equation labels: (9) interval eigenvalue equation; (10) zero endpoint values.*
+
 It is easy to check that the eigenfunctions of this problem are
 
 $$
 \phi_{m}(x)=\sin \frac{m \pi}{a} x
+\tag{11}
 $$
 
 corresponding to the eigenvalues
 
 $$
 \lambda=\lambda_{m}=\left(\frac{m \pi}{a}\right)^{2}, \quad m=1,2,3, \ldots .
+\tag{12}
 $$
 
 Now for a solution of the problem in Figure 2(a), we try
 
 $$
 u(x, y)=\sum_{m=1}^{\infty} E_{m}(y) \sin \frac{m \pi}{a} x
-$$
-
-Here we have to allow the coefficients $E_{m n}$ to be functions of the second variable $y$. To complete the solution, we must solve for $E_{m}(y)$. Plugging (13) into (1), we obtain
+\tag{13}
+$$
+
+Here we have to allow the coefficients $E_m$ to be functions of the second variable $y$. To complete the solution, we must solve for $E_{m}(y)$. Plugging (13) into (1), we obtain
 
 $$
 \sum_{m=1}^{\infty} \underbrace{\left(E_{m}^{\prime \prime}(y)-\left(\frac{m \pi}{a}\right)^{2} E_{m}(y)\right)}_{b_{m}(y)} \sin \frac{m \pi}{a} x=f(x, y)
-$$
-
-where $0<x<a, 0<y<b$. For each $y$ in the interval $(0, b)$, think of (14) as a Fourier sine series expansion of the function $x \mapsto f(x, y)$. The Fourier sine coefficients in (14) are functions of $y$ that we denote by $b_{m}(y)$. From (4), Section 2.4, we have
+\tag{14}
+$$
+
+where $0<x<a, 0<y<b$. For each $y$ in the interval $(0, b)$, think of (14) as a Fourier sine series expansion of the function $x \mapsto f(x, y)$. The Fourier sine coefficients in (14) are functions of $y$ that we denote by $b_{m}(y)$. From (4), Section 7.4, we have
 
 $$
 b_{m}(y)=\frac{2}{a} \int_{0}^{a} f(x, y) \sin \frac{m \pi}{a} x d x
-$$
-
-Hence $E_{m}(y)$ is the unique solution of the second order nonhomogeneous initial value problem
+\tag{15}
+$$
+
+Hence $E_{m}(y)$ is the unique solution of the second order nonhomogeneous boundary value problem
 
 $$
 \begin{gathered}
@@ -212,7 +258,9 @@
 \end{gathered}
 $$
 
-where the initial conditions (17) follow from (13) and the fact that $u(x, 0)=0$ and $u(x, b)=0$. We now proceed to solve (16) using the variation of parameters formula (Appendix A.3). Two solutions of the associated homogeneous equation
+*Printed equation labels: (16) coefficient differential equation; (17) zero endpoint values.*
+
+where the boundary conditions (17) follow from (13) and the fact that $u(x, 0)=0$ and $u(x, b)=0$. We now proceed to solve (16) using the variation of parameters formula (Section 10.3). Two solutions of the associated homogeneous equation
 
 $$
 E_{m}^{\prime \prime}(y)-\left(\frac{m \pi}{a}\right)^{2} E_{m}(y)=0
@@ -222,21 +270,23 @@
 
 $$
 h_{1}(y)=\sinh \left(\frac{m \pi}{a}(b-y)\right) \quad \text { and } \quad h_{2}(y)=\sinh \left(\frac{m \pi}{a} y\right) .
+\tag{18}
 $$
 
 A straightforward computation shows that the Wronskian of $h_{1}$ and $h_{2}$ is
 
-Recall from Appendix A.1:
-$W\left(h_{1}, h_{2}\right)=h_{1} h_{2}^{\prime}-h_{1}^{\prime} h_{2}$.
+Recall from Section 10.1:
+$W\left(h_{1}, h_{2}\right)=h_{1} h_{2}^{\prime}-h_{1}^{\prime} h_{2}$ (printed equation (19)).
 
 $$
 W\left(h_{1}, h_{2}\right)=\frac{m \pi}{a} \sinh \left(\frac{m \pi}{a} b\right) .
 $$
 
-Since $W\left(h_{1}, h_{2}\right) \neq 0$, the two solutions are linearly independent. Applying the variation of parameters formula ((4), Appendix A.3), we obtain a particular solution of (16) in the form
+Since $W\left(h_{1}, h_{2}\right) \neq 0$, the two solutions are linearly independent. Applying the variation of parameters formula ((4), Section 10.3), we obtain a particular solution of (16) in the form
 
 $$
 h_{1}(y) \int \frac{-h_{2}(y)}{W\left(h_{1}, h_{2}\right)} b_{m}(y) d y+h_{2}(y) \int \frac{h_{1}(y)}{W\left(h_{1}, h_{2}\right)} b_{m}(y) d y
+\tag{20}
 $$
 
 Each integral in this formula is determined up to an arbitrary constant of integration. Different constants yield particular solutions of (16) that differ by linear combinations of $h_{1}$ and $h_{2}$. The (unique) solution of (16)-(17) is determined by a specific choice of the constants of integration. From (19), we see that $W\left(h_{1}, h_{2}\right)$ is independent of $y$, and hence it can be pulled outside the integrals in (20). You can check that
@@ -246,16 +296,21 @@
 E_{m}(y)=\frac{-1}{\frac{m \pi}{a} \sinh \left(\frac{m \pi}{a} b\right)}\left[h_{1}(y) \int_{0}^{y} h_{2}(s) b_{m}(s) d s\right. \\
 \left.\quad+h_{2}(y) \int_{y}^{b} h_{1}(s) b_{m}(s) d s\right]
 \end{gathered}
-$$
-
-satisfies the initial conditions and hence is the unique solution of the initial value problem (16)-(17). (Use the fact that $h_{1}(b)=0$ and $h_{2}(0)=0$.) This completely solves the problem in Figure 2(a) and yields a single series solution (13) with coefficients given by (21).
-
-## EXAMPLE 3 A single series solution of a Poisson problem
+\tag{21}
+$$
+
+satisfies the boundary conditions and hence is the unique solution of the boundary value problem (16)-(17). (Use the fact that $h_{1}(b)=0$ and $h_{2}(0)=0$.) This completely solves the problem in Figure 2(a) and yields a single series solution (13) with coefficients given by (21).
+
+> [!exercise|b83a5baf-e7a9-54fa-a40f-6dfebf91d0d2.local at=23f77d64-0815-5797-9e5d-0a58a7561fd8] EXAMPLE 3 A single series solution of a Poisson problem
+> Obtain a single-series solution of $\Delta u=1$ in the unit square with $u=0$ on all four sides, using one-dimensional eigenfunctions in $x$.
+
+##### solution
 
 To find a single series expression of the solution in Example 1, we use (13). From (15), we have
 
 $$
 b_{m}(y)=2 \int_{0}^{1} \sin m \pi x d x=\frac{-2(\cos m \pi-1)}{m \pi}= \begin{cases}\frac{4}{m \pi} & \text { if } m \text { is odd } \\ 0 & \text { if } m \text { is even }\end{cases}
+\tag{22}
 $$
 
 From (18), we have
@@ -290,140 +345,204 @@
 
 In Exercise 12 you are asked to use a computer to verify that indeed this solution is equal to the double series solution of Example 1.
 
-## Exercises 3.9
-
-In Exercises 1-4, use double Fourier series to solve the Poisson problem in Figure 1 for the given data. Take $a=b=1$.
-
-1. $f(x, y)=x, f_{1}=f_{2}=0, g_{1}=g_{2}=0$.
-2. $f(x, y)=\sin 2 \pi x, f_{1}=f_{2}=0, g_{1}=g_{2}=0$.
-3. $f(x, y)=\sin \pi x, f_{1}(x)=0, f_{2}(x)=x, g_{1}=g_{2}=0$.
-4. $f(x, y)=x y, f_{1}(x)=0, f_{2}(x)=x, g_{1}=g_{2}=0$.
-5. Use the eigenfunction expansions method to solve $\nabla^{2} u=3 u-1$ inside the unit square $(0<x<1,0<y<1)$, given that $u$ is zero on the boundary.
-6. Use the eigenfunction expansions method to solve $\nabla^{2} u=u_{x x}+u$ inside the unit square ( $0<x<1,0<y<1$ ), given that $u$ is zero on the boundary.
-7. Solve the problem in Exercise 2 using one dimensional eigenfunction expansions.
-8. Solve the problem in Exercise 1 using one dimensional eigenfunction expansions.
-9. Solve the eigenfunction problem (6)-(7) by deriving (5) and (8).
-10. Derive (18) and (19).
-11. Show that (21) is a solution of (16)-(17).
-12. Using a computer, verify that the solutions in Examples 1 and 3 are the same by evaluating them at various points inside the $1 \times 1$ square.
-13. Project Problem: Dirichlet problem in a rectangle. Derive the result of Example 1, Section 11.8, using the method of eigenfunction expansions. Start by considering the following related one dimensional eigenvalue problem:
-
-$$
-\frac{d^{2} \phi}{d x^{2}}=-\lambda \phi(x), \quad \phi(0)=0, \quad \phi(a)=0
-$$
-
-14. Project Problem: A Poisson problem in a box. Use (triple) Fourier series expansions to solve Poisson's equation
-
-$$
-\nabla^{2} u(x, y, z)=f(x, y, z)
-$$
-
-inside a rectangular box $(0<x<a, 0<y<b, 0<z<c)$ subject to the boundary condition $u=0$ on all six sides. In solving this problem, you should answer the
-following questions:
-(a) What is the related homogeneous problem?
-(b) What are the eigenvalues and their corresponding eigenfunctions?
-(c) What is the analog of Theorem 1, Section 11.7, for functions of three variables?
-15. Describe the solution of the problem in Exercise 14 if $u$ is not zero on all sides of the box. [Hint: Exercises 12 and 13, Section 11.8.]
-16. The Helmholtz equation. (a) Separate variables in the heat equation
-
-$$
-u_{t}=c^{2}\left(u_{x x}+u_{y y}+u_{z z}\right)
-$$
-
-by letting $u(x, y, z, t)=\phi(x, y, z) T(t)$, where $(x, y, z)$ is the spatial variable and $t$ is the time variable. Show that the spatial part $\phi$ satisfies the Helmholtz equation.
-(b) Repeat part (a) for the one and two dimensional heat equations.
-(c) Repeat part (a) for the three dimensional wave equation.
-17. Project Problem: The heat equation via the eigenfunction expansions method. Solve the two dimensional heat boundary value problem of Section 11.7 by using the eigenfunction expansions method. Note: The related eigenfunction problem is given by (6) and (7). The coefficients in the series solution should be functions of $t$.
-
-Project Problem: Nonhomogeneous heat boundary value problem. Do Exercises 18 and 20 to solve a nonhomogeneous heat boundary value problem. To illustrate the solution, do Exercises 19 and 21.
-18. Nonhomogeneous heat boundary value problem: a special case The boundary value problem
-
-$$
-\begin{gathered}
-u_{t}=c^{2} u_{x x}+q(x, t), \quad t>0, \quad 0<x<L \\
-u(0, t)=0, u(L, t)=0, \quad t>0 \\
-u(x, 0)=f(x)
-\end{gathered}
-$$
-
-models heat transfer in a uniform bar of length $L$ with insulated lateral surface and initial temperature distribution $f(x)$, given that the ends of the bar are kept at $0^{\circ}$ temperature. The addition of the term $q(x, t)$ accounts for a time dependent heat source. We will solve this problem using the eigenfunction expansions method.
-(a) Solve the related eigenvalue problem
-
-$$
-\frac{d^{2} \phi}{d x^{2}}=-\lambda \phi(x), \quad \phi(0)=0, \quad \phi(L)=0 .
-$$
-
-(b) Write the Fourier sine series of $f$ and $q$ as
-
-$$
-f(x)=\sum_{n=1}^{\infty} b_{n} \sin \frac{n \pi}{L} x
-$$
-
-where
-
-$$
-b_{n}=\frac{2}{L} \int_{0}^{L} f(x) \sin \frac{n \pi}{L} x d x
-$$
-
-and
-
-$$
-q(x, t)=\sum_{n=1}^{\infty} q_{n}(t) \sin \frac{n \pi}{L} x
-$$
-
-where
-
-$$
-q_{n}(t)=\frac{2}{L} \int_{0}^{L} q(x, t) \sin \frac{n \pi}{L} x d x
-$$
-
-To apply the eigenfunction expansions method, let
-
-$$
-u(x, t)=\sum_{n=1}^{\infty} B_{n}(t) \sin \frac{n \pi}{L} x
-$$
-
-Show that $B_{n}(t)$ satisfies the first order initial value problem
-
-$$
-\frac{d B_{n}}{d t}+c^{2} \lambda_{n} B_{n}=q_{n}(t), \quad B_{n}(0)=b_{n}
-$$
-
-where $\lambda_{n}=\left(\frac{n \pi}{L}\right)^{2}$.
-(c) Show that
-
-$$
-B_{n}(t)=e^{-c^{2} \lambda_{n} t}\left(b_{n}+\int_{0}^{t} q_{n}(s) e^{c^{2} \lambda_{n} s} d s\right)
-$$
-
-19. (a) Work out all the details in Exercise 18 for the specific case when $c= 1, L=\pi, q(x, t)=x e^{-t}$, and $f(x)=0$.
-(b) Plot the solution for various values of $t$ and comment on the graphs as $t \rightarrow \infty$.
-
-Does the behavior of the graphs meet with your expectations?
-20. Nonhomogeneous heat boundary value problem: general case. In this exercise, we will solve the heat equation of Exercise 18 with the same initial condition but with the following time-dependent boundary conditions:
-
-$$
-u(0, t)=A(t), \quad u(L, t)=B(t), \quad t>0
-$$
-
-To motivate the solution, refer to Section 11.5 (problem (6)-(8)), where we did the case when $A(t)$ and $B(t)$ are constant.
-(a) Show that the solution is of the form
-
-$$
-u(x, t)=v(x, t)+\frac{B(t)-A(t)}{L} x+A(t)
-$$
-
-where $v(x, t)$ is the solution of the following heat problem:
-
-$$
-\begin{gathered}
-v_{t}=c^{2} v_{x x}+q(x, t)-\frac{B^{\prime}(t)-A^{\prime}(t)}{L} x-A^{\prime}(t), \quad t>0, \quad 0<x<L, \\
-v(0, t)=0, \quad v(L, t)=0, \quad t>0, \\
-v(x, 0)=f(x)-\frac{B(0)-A(0)}{L} x-A(0)
-\end{gathered}
-$$
-
-(b) Solve the problem using (a) and Exercise 18.
-(c) Describe what you get when $A(t)$ and $B(t)$ are constant. Compare your result to that of Section 11.5.
-21. (a) Work out all the details in Exercise 20 for the specific case: $c=1, L= \pi, q(x, t)=0, A(t)=t e^{-t}, B(t)=0$, and $f(x)=0$.
-(b) Plot the solution for various values of $t$ and comment on the graphs as $t \rightarrow \infty$.
+## Exercises 11.9
+
+
+> [!prompt|eb15414d-ce6b-58f6-953a-5415ee67935e.local at=e54c2bfb-80c8-5686-8adc-059f8ccff345] Shared exercise instructions
+> In Exercises 1-4, use double Fourier series to solve the Poisson problem in Figure 1 for the given data. Take $a=b=1$.
+
+
+> [!exercise|7837242a-f233-5876-8c79-7db94f4420d6.local at=a86de223-4471-58af-a6a9-30bc5d3763d9] Exercise 1
+> $f(x, y)=x, f_{1}=f_{2}=0, g_{1}=g_{2}=0$.
+
+
+> [!exercise|4971925e-933c-5f6b-b61c-2224a76baeb3.local at=9231a3f0-9dde-58cf-ac7e-08a7f6619d83] Exercise 2
+> $f(x, y)=\sin 2 \pi x, f_{1}=f_{2}=0, g_{1}=g_{2}=0$.
+
+
+> [!exercise|ec1f2b2e-479f-5138-9d1d-5e16f2da4859.local at=f4db84e3-d8cb-542d-912e-48a2e656398d] Exercise 3
+> $f(x, y)=\sin \pi x, f_{1}(x)=0, f_{2}(x)=x, g_{1}=g_{2}=0$.
+
+
+> [!exercise|c0d82855-d0a3-5680-be57-a37fd7477604.local at=f6f1d081-c398-50c2-baf1-3bb218c47cf6] Exercise 4
+> $f(x, y)=x y, f_{1}(x)=0, f_{2}(x)=x, g_{1}=g_{2}=0$.
+
+
+> [!exercise|f1968a53-d967-50fe-a7fc-78490fed18bb.local at=f03c843f-7eb6-5727-b3f4-7b173392c24f] Exercise 5
+> Use the eigenfunction expansions method to solve $\nabla^{2} u=3 u-1$ inside the unit square $(0<x<1,0<y<1)$, given that $u$ is zero on the boundary.
+
+
+> [!exercise|eb843133-a221-5a7b-b48f-9dfbc4b076fc.local at=6d041937-2067-59c2-8e87-2fa3accdfc4d] Exercise 6
+> Use the eigenfunction expansions method to solve $\nabla^{2} u=u_{x x}+u$ inside the unit square ( $0<x<1,0<y<1$ ), given that $u$ is zero on the boundary.
+
+
+> [!exercise|4ce7b4cb-d2d5-53ff-9996-3548ef695cae.local at=a35157c3-02f7-51c3-bef5-42e449a394c2] Exercise 7
+> Solve the problem in Exercise 2 using one dimensional eigenfunction expansions.
+
+
+> [!exercise|6f6246e6-09c7-5ca6-9114-d963b19322a4.local at=fa505368-0ab9-5824-b4ca-03fa41fde8c7] Exercise 8
+> Solve the problem in Exercise 1 using one dimensional eigenfunction expansions.
+
+
+> [!exercise|ba5c9ab6-68c0-5a10-955e-7488ef5c5f51.local at=b23a2139-5b1e-5087-bea3-08b830cae7f4] Exercise 9
+> Solve the eigenfunction problem (6)-(7) by deriving (5) and (8).
+
+
+> [!exercise|f56ac2c5-cb24-58e6-b61b-77f95d29084d.local at=225c7edc-0391-5266-ade4-52286ac44941] Exercise 10
+> Derive (18) and (19).
+
+
+> [!exercise|85b90c9d-3f5a-531d-8df0-a0a16ea07ac1.local at=ee49bbd1-1111-5f90-b5c0-43ec1a833931] Exercise 11
+> Show that (21) is a solution of (16)-(17).
+
+
+> [!exercise|34a1912b-830d-5dff-8d89-63388f06e2f0.local at=f445a31a-4d4d-5f29-bed1-908c807093d0] Exercise 12
+> Using a computer, verify that the solutions in Examples 1 and 3 are the same by evaluating them at various points inside the $1 \times 1$ square.
+
+
+> [!exercise|42a2a668-287b-5a40-a057-556247e4ac60.local at=5e4bf338-eeca-587d-a830-e09aa861fc9d] Exercise 13
+> Project Problem: Dirichlet problem in a rectangle. Derive the result of Example 1, Section 11.8, using the method of eigenfunction expansions. Start by considering the following related one dimensional eigenvalue problem:
+>
+> $$
+> \frac{d^{2} \phi}{d x^{2}}=-\lambda \phi(x), \quad \phi(0)=0, \quad \phi(a)=0
+> $$
+
+
+> [!exercise|9d7ebc94-e7ca-5223-9128-70085db08317.local at=4ba1d6a9-0607-5163-990e-2992d9d2bbc0] Exercise 14
+> Project Problem: A Poisson problem in a box. Use (triple) Fourier series expansions to solve Poisson's equation
+>
+> $$
+> \nabla^{2} u(x, y, z)=f(x, y, z)
+> $$
+>
+> inside a rectangular box $(0<x<a, 0<y<b, 0<z<c)$ subject to the boundary condition $u=0$ on all six sides. In solving this problem, you should answer the
+> following questions:
+> (a) What is the related homogeneous problem?
+> (b) What are the eigenvalues and their corresponding eigenfunctions?
+> (c) What is the analog of Theorem 1, Section 11.7, for functions of three variables?
+
+
+> [!exercise|a3792150-d28b-568a-91a7-5f88ab7290b7.local at=52b44a1b-7313-51fc-8423-fa0f7af535a1] Exercise 15
+> Describe the solution of the problem in Exercise 14 if $u$ is not zero on all sides of the box. [Hint: Exercises 12 and 13, Section 11.8.]
+
+
+> [!exercise|b6fa0251-2581-544d-b82d-afa18345e2a2.local at=d8ca021a-e7a6-5dcf-a9c6-8c96e86ff16b] Exercise 16
+> The Helmholtz equation. (a) Separate variables in the heat equation
+>
+> $$
+> u_{t}=c^{2}\left(u_{x x}+u_{y y}+u_{z z}\right)
+> $$
+>
+> by letting $u(x, y, z, t)=\phi(x, y, z) T(t)$, where $(x, y, z)$ is the spatial variable and $t$ is the time variable. Show that the spatial part $\phi$ satisfies the Helmholtz equation.
+> (b) Repeat part (a) for the one and two dimensional heat equations.
+> (c) Repeat part (a) for the three dimensional wave equation.
+
+
+> [!exercise|04f15bbd-b760-566a-801f-7aaaefd8cb27.local at=7b5b302a-b5c3-547f-be78-3d4fd30fb170] Exercise 17
+> Project Problem: The heat equation via the eigenfunction expansions method. Solve the two dimensional heat boundary value problem of Section 11.7 by using the eigenfunction expansions method. Note: The related eigenfunction problem is given by (6) and (7). The coefficients in the series solution should be functions of $t$.
+
+
+> [!prompt|173bd07e-6062-59f4-9ce7-adc3ee910756.local at=f528bd72-c121-5e89-bf98-c7c36714df93] Shared exercise instructions
+> Project Problem: Nonhomogeneous heat boundary value problem. Do Exercises 18 and 20 to solve a nonhomogeneous heat boundary value problem. To illustrate the solution, do Exercises 19 and 21.
+
+
+> [!exercise|977ca9f5-210a-5851-bb43-30bc8a892329.local at=274f8d79-477d-592e-8f57-cc796ff81e6f] Exercise 18
+> Nonhomogeneous heat boundary value problem: a special case The boundary value problem
+>
+> $$
+> \begin{gathered}
+> u_{t}=c^{2} u_{x x}+q(x, t), \quad t>0, \quad 0<x<L \\
+> u(0, t)=0, u(L, t)=0, \quad t>0 \\
+> u(x, 0)=f(x)
+> \end{gathered}
+> $$
+>
+> models heat transfer in a uniform bar of length $L$ with insulated lateral surface and initial temperature distribution $f(x)$, given that the ends of the bar are kept at $0^{\circ}$ temperature. The addition of the term $q(x, t)$ accounts for a time dependent heat source. We will solve this problem using the eigenfunction expansions method.
+> (a) Solve the related eigenvalue problem
+>
+> $$
+> \frac{d^{2} \phi}{d x^{2}}=-\lambda \phi(x), \quad \phi(0)=0, \quad \phi(L)=0 .
+> $$
+>
+> (b) Write the Fourier sine series of $f$ and $q$ as
+>
+> $$
+> f(x)=\sum_{n=1}^{\infty} b_{n} \sin \frac{n \pi}{L} x
+> $$
+>
+> where
+>
+> $$
+> b_{n}=\frac{2}{L} \int_{0}^{L} f(x) \sin \frac{n \pi}{L} x d x
+> $$
+>
+> and
+>
+> $$
+> q(x, t)=\sum_{n=1}^{\infty} q_{n}(t) \sin \frac{n \pi}{L} x
+> $$
+>
+> where
+>
+> $$
+> q_{n}(t)=\frac{2}{L} \int_{0}^{L} q(x, t) \sin \frac{n \pi}{L} x d x
+> $$
+>
+> To apply the eigenfunction expansions method, let
+>
+> $$
+> u(x, t)=\sum_{n=1}^{\infty} B_{n}(t) \sin \frac{n \pi}{L} x
+> $$
+>
+> Show that $B_{n}(t)$ satisfies the first order initial value problem
+>
+> $$
+> \frac{d B_{n}}{d t}+c^{2} \lambda_{n} B_{n}=q_{n}(t), \quad B_{n}(0)=b_{n}
+> $$
+>
+> where $\lambda_{n}=\left(\frac{n \pi}{L}\right)^{2}$.
+> (c) Show that
+>
+> $$
+> B_{n}(t)=e^{-c^{2} \lambda_{n} t}\left(b_{n}+\int_{0}^{t} q_{n}(s) e^{c^{2} \lambda_{n} s} d s\right)
+> $$
+
+
+> [!exercise|ef2b5c28-3ee5-569e-bd51-0d9d56182442.local at=9abc8dd8-69c0-5caf-970e-0fcaa718e5d7] Exercise 19
+> (a) Work out all the details in Exercise 18 for the specific case when $c= 1, L=\pi, q(x, t)=x e^{-t}$, and $f(x)=0$.
+> (b) Plot the solution for various values of $t$ and comment on the graphs as $t \rightarrow \infty$.
+>
+> Does the behavior of the graphs meet with your expectations?
+
+
+> [!exercise|543c0ca6-a7ee-5f56-810b-80b0d7622648.local at=fe3c5c19-7f20-55e3-ac97-5fcc709629e3] Exercise 20
+> Nonhomogeneous heat boundary value problem: general case. In this exercise, we will solve the heat equation of Exercise 18 with the same initial condition but with the following time-dependent boundary conditions:
+>
+> $$
+> u(0, t)=A(t), \quad u(L, t)=B(t), \quad t>0
+> $$
+>
+> To motivate the solution, refer to Section 11.5 (problem (6)-(8)), where we did the case when $A(t)$ and $B(t)$ are constant.
+> (a) Show that the solution is of the form
+>
+> $$
+> u(x, t)=v(x, t)+\frac{B(t)-A(t)}{L} x+A(t)
+> $$
+>
+> where $v(x, t)$ is the solution of the following heat problem:
+>
+> $$
+> \begin{gathered}
+> v_{t}=c^{2} v_{x x}+q(x, t)-\frac{B^{\prime}(t)-A^{\prime}(t)}{L} x-A^{\prime}(t), \quad t>0, \quad 0<x<L, \\
+> v(0, t)=0, \quad v(L, t)=0, \quad t>0, \\
+> v(x, 0)=f(x)-\frac{B(0)-A(0)}{L} x-A(0)
+> \end{gathered}
+> $$
+>
+> (b) Solve the problem using (a) and Exercise 18.
+> (c) Describe what you get when $A(t)$ and $B(t)$ are constant. Compare your result to that of Section 11.5.
+
+
+> [!exercise|d1b899fd-4167-5297-aefa-63a2362d8870.local at=dfcc7379-01a6-52a8-8baf-0fcedd95a25a] Exercise 21
+> (a) Work out all the details in Exercise 20 for the specific case: $c=1, L= \pi, q(x, t)=0, A(t)=t e^{-t}, B(t)=0$, and $f(x)=0$.
+> (b) Plot the solution for various values of $t$ and comment on the graphs as $t \rightarrow \infty$.

`````
