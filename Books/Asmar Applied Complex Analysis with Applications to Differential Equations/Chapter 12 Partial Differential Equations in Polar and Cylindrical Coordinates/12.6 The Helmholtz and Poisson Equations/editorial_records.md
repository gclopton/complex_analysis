
# Editorial records

Reading note: 12.6 The Helmholtz and Poisson Equations.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|f1738541-0273-5e3e-b782-350615e9efd1.local at=ac537d24-9a90-531a-97d6-1bf73e9e89cb] Dirichlet eigenvalues and eigenfunctions of the negative Laplacian on a disk
> Let $a>0$. For $-\Delta\phi=k\phi$ on the disk of radius $a$, with $\phi=0$ at $r=a$, angular $2\pi$-periodicity and regularity at the origin, the eigenvalues are
> $$
> k=\lambda_{mn}^2=(\alpha_{mn}/a)^2,\qquad m=0,1,2,\ldots,\quad n=1,2,\ldots,
> $$
> where $\alpha_{mn}$ is the $n$th positive zero of the Bessel function $J_m$ of the first kind. The associated eigenfunctions are
> $$
> J_m(\lambda_{mn}r)\cos m\theta\quad(m\ge0),\qquad
> J_m(\lambda_{mn}r)\sin m\theta\quad(m\ge1).
> $$
> For $m=0$ only the cosine function is nonzero; for $m\ge1$ the sine and cosine functions give two linearly independent modes.
````
### After

````text
> [!theorem|f1738541-0273-5e3e-b782-350615e9efd1.local at=ac537d24-9a90-531a-97d6-1bf73e9e89cb] The Helmholtz Equation in a Disk
> Let $a>0$. For $-\Delta\phi=k\phi$ on the disk of radius $a$, with $\phi=0$ at $r=a$, angular $2\pi$-periodicity and regularity at the origin.
>
> The eigenvalues of this problem are
>
> $$
> k=\lambda_{m n}^{2}=\left(\alpha_{m n} / a\right)^{2}, \quad m=0,1,2, \ldots, n=1,2, \ldots
> $$
>
> where $\alpha_{m n}$ is the $n$th positive zero of the Bessel function $J_{m}$. To each eigenvalue $\lambda_{m n}^{2}$ correspond the eigenfunctions
>
> $$
> \cos m \theta J_{m}\left(\lambda_{m n} r\right) \text { and } \sin m \theta J_{m}\left(\lambda_{m n} r\right) .
> $$
>
> (For $m=0$ the sine expression is identically zero and is omitted. Note that for $m=1,2, \ldots$ we have two distinct eigenfunctions for a given eigenvalue.)
````

## 2. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|93faa464-9f3c-571a-b4bf-ff9f7ef2b938.local at=59461e7f-f1a0-5019-969f-69cc5c671c86] Fourier–Bessel eigenfunction expansion of a square-integrable function on a disk
> Let $a>0$, let $f\in L^2(D_a)$ with area measure $r\,dr\,d\theta$, and let $\alpha_{mn}$ be the $n$th positive zero of the Bessel function $J_m$ of the first kind. Set $\lambda_{mn}=\alpha_{mn}/a$. Then
> $$
> f(r,\theta)=\sum_{m=0}^{\infty}\sum_{n=1}^{\infty}J_m(\lambda_{mn}r)\left(a_{mn}\cos m\theta+b_{mn}\sin m\theta\right)
> $$
> in the $L^2$ sense, where $b_{0n}=0$ and
> $$
> \begin{aligned}
> a_{0n}&=\frac1{\pi a^2J_1(\alpha_{0n})^2}\int_0^a\int_0^{2\pi}f(r,\theta)J_0(\lambda_{0n}r)r\,d\theta\,dr,\\
> a_{mn}&=\frac2{\pi a^2J_{m+1}(\alpha_{mn})^2}\int_0^a\int_0^{2\pi}f(r,\theta)\cos m\theta\,J_m(\lambda_{mn}r)r\,d\theta\,dr,\\
> b_{mn}&=\frac2{\pi a^2J_{m+1}(\alpha_{mn})^2}\int_0^a\int_0^{2\pi}f(r,\theta)\sin m\theta\,J_m(\lambda_{mn}r)r\,d\theta\,dr.
> \end{aligned}
> $$
> Here $n\ge1$, and $m\ge1$ in the last two formulas. Pointwise convergence requires additional regularity; it is not asserted merely because $f$ is defined on the disk.
````
### After

````text
> [!theorem|93faa464-9f3c-571a-b4bf-ff9f7ef2b938.local at=59461e7f-f1a0-5019-969f-69cc5c671c86] Expansions in Terms of the Eigenfunctions of the Helmholtz Equation
> Let $J_m$ be the Bessel function of the first kind, $\alpha_{mn}$ its $n$th positive zero, and $\lambda_{mn}=\alpha_{mn}/a$.
>
> Suppose that $f(r, \theta)$ is smooth on the closed disk $0\leq r\leq a$, where $a>0$. Then, at interior points,
>
> $$
> f(r, \theta)=\sum_{m=0}^{\infty} \sum_{n=1}^{\infty} J_{m}\left(\lambda_{m n} r\right)\left(a_{m n} \cos m \theta+b_{m n} \sin m \theta\right)
> $$
>
> where $b_{0n}=0$ and
> $$
> \begin{aligned}
> a_{0n}&=\frac1{\pi a^2J_1(\alpha_{0n})^2}\int_0^a\int_0^{2\pi}f(r,\theta)J_0(\lambda_{0n}r)r\,d\theta\,dr,\\
> a_{mn}&=\frac2{\pi a^2J_{m+1}(\alpha_{mn})^2}\int_0^a\int_0^{2\pi}f(r,\theta)\cos m\theta\,J_m(\lambda_{mn}r)r\,d\theta\,dr,\\
> b_{mn}&=\frac2{\pi a^2J_{m+1}(\alpha_{mn})^2}\int_0^a\int_0^{2\pi}f(r,\theta)\sin m\theta\,J_m(\lambda_{mn}r)r\,d\theta\,dr.
> \end{aligned}
> $$
> Here $n\ge1$, and $m\ge1$ in the last two formulas.
````

## 3. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!procedure|ef333ef0-c62d-5624-8af6-a14de4c83bf7.local at=b9005dd7-d04c-5890-abef-5069ca7a91b6] Eigenfunction solution of a Poisson–Dirichlet problem on a disk
> To solve $\Delta u=f$ on a disk of radius $a>0$ with $u(a,\theta)=g(\theta)$, first find a harmonic function $v$ with boundary values $g$. Expand $f$ in the regular zero-Dirichlet eigenfunctions
> $$
> \phi_{mn}^{c}=J_m(\alpha_{mn}r/a)\cos m\theta,\qquad
> \phi_{mn}^{s}=J_m(\alpha_{mn}r/a)\sin m\theta,
> $$
> where $\alpha_{mn}$ is the $n$th positive zero of $J_m$, $m\ge0$, $n\ge1$, and the zero sine mode is omitted. Their positive eigenvalues for $-\Delta$ are $\lambda_{mn}^2=(\alpha_{mn}/a)^2$.
>
> For either nonzero mode $\phi$, its source coefficient is $F_\phi=\langle f,\phi\rangle/\langle\phi,\phi\rangle$, using disk area measure $r\,dr\,d\theta$. Set
> $$
> u=v-\sum_{\phi}\frac{F_\phi}{\lambda_\phi^2}\phi.
> $$
> For $f\in L^2$ this gives the weak zero-boundary correction to $v$. Pointwise differentiation and continuous boundary values require the corresponding regularity and boundary compatibility.
````
### After

````text
> [!procedure|ef333ef0-c62d-5624-8af6-a14de4c83bf7.local at=b9005dd7-d04c-5890-abef-5069ca7a91b6] Solution of Poisson's Problem in a Disk
> The solution of the Poisson problem (9)-(10) is given by
>
> $$
> u(r, \theta)=u_{1}(r, \theta)+u_{2}(r, \theta),
> $$
>
> where $u_{1}$ is the solution of the Poisson problem with zero boundary data in Figure 1(a), and $u_{2}$ is the solution of the Dirichlet problem in Figure 1(b). The function $u_{1}$ is given by (11)-(14), and the function $u_{2}$ is given by (4)-(5), Section 12.4.
````

## 4. Restore this source recap as local teaching material, excluded from Index candidates. Preserve its identity.

### Before

````text
> [!procedure|ef333ef0-c62d-5624-8af6-a14de4c83bf7.local at=b9005dd7-d04c-5890-abef-5069ca7a91b6] Solution of Poisson's Problem in a Disk
> The solution of the Poisson problem (9)-(10) is given by
>
> $$
> u(r, \theta)=u_{1}(r, \theta)+u_{2}(r, \theta),
> $$
>
> where $u_{1}$ is the solution of the Poisson problem with zero boundary data in Figure 1(a), and $u_{2}$ is the solution of the Dirichlet problem in Figure 1(b). The function $u_{1}$ is given by (11)-(14), and the function $u_{2}$ is given by (4)-(5), Section 12.4.
````
### After

````text
> [!note|ef333ef0-c62d-5624-8af6-a14de4c83bf7.local at=b9005dd7-d04c-5890-abef-5069ca7a91b6] Solution of Poisson's Problem in a Disk
> The solution of the Poisson problem (9)-(10) is given by
>
> $$
> u(r, \theta)=u_{1}(r, \theta)+u_{2}(r, \theta),
> $$
>
> where $u_{1}$ is the solution of the Poisson problem with zero boundary data in Figure 1(a), and $u_{2}$ is the solution of the Dirichlet problem in Figure 1(b). The function $u_{1}$ is given by (11)-(14), and the function $u_{2}$ is given by (4)-(5), Section 12.4.
````

## 5. Move correction/commentary into the separate editorial record; keep the actual correction in the reading text.

### Before

````text
[Corrected: the factors $c^2$ required by the PDE have been restored in the modal ODEs and integrating factors below.]
````
### After

````text

````

## Source-to-current comparison

Source: /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 12 Partial Differential Equations in Polar and Cylindrical Coordinates/12.6 The Helmholtz and Poisson Equations.md

This exact comparison preserves the full change evidence, including formatting, OCR corrections, restored source wording, and required standalone context. The entries above explain the recovery edits. The comparison is not a claim that every difference is a correction; component serialization, callout wrapping, and printed labels outside callouts are formatting.

`````diff
--- /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 12 Partial Differential Equations in Polar and Cylindrical Coordinates/12.6 The Helmholtz and Poisson Equations.md
+++ /Users/gradyclopton/ObsidianVaults/complex_analysis/Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 12 Partial Differential Equations in Polar and Cylindrical Coordinates/12.6 The Helmholtz and Poisson Equations.md
@@ -1,15 +1,18 @@
+
 ### 12.6 The Helmholtz and Poisson Equations
 
-We know from Section 3.9 that several important boundary value problems can be solved by applying the method of eigenfunction expansions. In this section, we will present some applications of this method on the disk. For this purpose, we start by solving the eigenvalue problem consisting of the Helmholtz equation on a disk of radius $a$,
+We know from Section 11.9 that several important boundary value problems can be solved by applying the method of eigenfunction expansions. In this section, we will present some applications of this method on the disk. For this purpose, we start by solving the eigenvalue problem consisting of the Helmholtz equation on a disk of radius $a$,
 
 $$
 \nabla^{2} \phi(r, \theta)=-k \phi(r, \theta), 0<r<a, 0<\theta<2 \pi,
+\tag{1}
 $$
 
 with the boundary condition
 
 $$
 \phi(a, \theta)=0,0<\theta<2 \pi .
+\tag{2}
 $$
 
 To solve this problem means to determine the values of $k$ (or eigenvalues) for which we have nontrivial solutions and find these nontrivial solutions (or eigenfunctions).
@@ -23,31 +26,34 @@
 \end{gathered}
 $$
 
+*Printed equation labels: (3) angular equation; (4) radial equation and boundary value.*
+
 The solutions of (3) are
 
 $$
 \cos m \theta, \text { and } \sin m \theta, \quad m=0,1,2, \ldots .
 $$
 
-If $k<0$, equation (4) becomes the modified Bessel equation of order $m$, and it can be shown that in this case the only bounded solution with $R(a)=0$ is the zero solution. So we take $k \geq 0$ and (4) becomes the parametric form of Bessel's equation of order $m$. We know from Theorem 3, Section 12.8, that the nontrivial solutions of (4) are constant multiples of $J_{m}\left(\lambda_{m n} r\right)$, which is the solution corresponding to the eigenvalue $k=\lambda_{m n}^{2}$. Piecing together the product solutions, we obtain the following important result.
-
-THEOREM 1 THE HELMHOLTZ EQUATION IN A DISK
-
-THEOREM 2 EXPANSIONS IN TERMS OF THE EIGENFUNCTIONS OF THE HELMHOLTZ EQUATION
-
-The eigenvalues of the problem (1)-(2) are
-
-$$
-k=\lambda_{m n}^{2}=\left(\alpha_{m n} / a\right)^{2}, \quad m=0,1,2, \ldots, n=1,2, \ldots
-$$
-
-where $\alpha_{m n}$ is the $n$th positive zero of the Bessel function $J_{m}$. To each eigenvalue $\lambda_{m n}^{2}$ correspond the eigenfunctions
-
-$$
-\cos m \theta J_{m}\left(\lambda_{m n} r\right) \text { and } \sin m \theta J_{m}\left(\lambda_{m n} r\right) .
-$$
-
-(Note that for $m=1,2, \ldots$ we have two distinct eigenfunctions for a given eigenvalue.)
+If $k<0$, equation (4) becomes the modified Bessel equation of order $m$, and it can be shown that in this case the only bounded solution with $R(a)=0$ is the zero solution. The case $k=0$ also yields only the zero regular solution under $R(a)=0$. Thus $k>0$, and (4) becomes the parametric form of Bessel's equation of order $m$. We know from Theorem 3, Section 12.8, that the nontrivial solutions of (4) are constant multiples of $J_{m}\left(\lambda_{m n} r\right)$, which is the solution corresponding to the eigenvalue $k=\lambda_{m n}^{2}$. Piecing together the product solutions, we obtain the following important result.
+
+> [!theorem|f1738541-0273-5e3e-b782-350615e9efd1.local at=ac537d24-9a90-531a-97d6-1bf73e9e89cb] The Helmholtz Equation in a Disk
+> Let $a>0$. For $-\Delta\phi=k\phi$ on the disk of radius $a$, with $\phi=0$ at $r=a$, angular $2\pi$-periodicity and regularity at the origin.
+>
+> The eigenvalues of this problem are
+>
+> $$
+> k=\lambda_{m n}^{2}=\left(\alpha_{m n} / a\right)^{2}, \quad m=0,1,2, \ldots, n=1,2, \ldots
+> $$
+>
+> where $\alpha_{m n}$ is the $n$th positive zero of the Bessel function $J_{m}$. To each eigenvalue $\lambda_{m n}^{2}$ correspond the eigenfunctions
+>
+> $$
+> \cos m \theta J_{m}\left(\lambda_{m n} r\right) \text { and } \sin m \theta J_{m}\left(\lambda_{m n} r\right) .
+> $$
+>
+> (For $m=0$ the sine expression is identically zero and is omitted. Note that for $m=1,2, \ldots$ we have two distinct eigenfunctions for a given eigenvalue.)
+
+*Printed equation labels: (5) eigenvalues; (6) cosine and sine eigenmodes.*
 
 In other words, if $\phi_{m n}(r, \theta)=\cos m \theta J_{m}\left(\lambda_{m n} r\right)$ or $\phi_{m n}(r, \theta)=\sin m \theta J_{m}\left(\lambda_{m n} r\right)$, then $\nabla^{2} \phi_{m n}=-\lambda_{m n}^{2} \phi_{m n}$ and $\phi(a, \theta)=0$.
 
@@ -55,25 +61,40 @@
 
 $$
 \int_{0}^{2 \pi} \int_{0}^{a} \sin m \theta J_{m}\left(\lambda_{m n} r\right) \cos m \theta J_{m}\left(\lambda_{m n} r\right) r d r d \theta=0
+\tag{7}
 $$
 
 Putting these facts together, we obtain the following expansion theorem, which was already used in (8), Section 12.3.
 
-Suppose that $f(r, \theta)$ is defined for all $0<r<a$ and $0<\theta<2 \pi$. Then
-
-$$
-f(r, \theta)=\sum_{m=0}^{\infty} \sum_{n=1}^{\infty} J_{m}\left(\lambda_{m n} r\right)\left(a_{m n} \cos m \theta+b_{m n} \sin m \theta\right)
-$$
-
-where (the generalized Fourier coefficients) $a_{m n}$ and $b_{m n}$ are given by (12)(14), Section 12.3.
+> [!theorem|93faa464-9f3c-571a-b4bf-ff9f7ef2b938.local at=59461e7f-f1a0-5019-969f-69cc5c671c86] Expansions in Terms of the Eigenfunctions of the Helmholtz Equation
+> Let $J_m$ be the Bessel function of the first kind, $\alpha_{mn}$ its $n$th positive zero, and $\lambda_{mn}=\alpha_{mn}/a$.
+>
+> Suppose that $f(r, \theta)$ is smooth on the closed disk $0\leq r\leq a$, where $a>0$. Then, at interior points,
+>
+> $$
+> f(r, \theta)=\sum_{m=0}^{\infty} \sum_{n=1}^{\infty} J_{m}\left(\lambda_{m n} r\right)\left(a_{m n} \cos m \theta+b_{m n} \sin m \theta\right)
+> $$
+>
+> where $b_{0n}=0$ and
+> $$
+> \begin{aligned}
+> a_{0n}&=\frac1{\pi a^2J_1(\alpha_{0n})^2}\int_0^a\int_0^{2\pi}f(r,\theta)J_0(\lambda_{0n}r)r\,d\theta\,dr,\\
+> a_{mn}&=\frac2{\pi a^2J_{m+1}(\alpha_{mn})^2}\int_0^a\int_0^{2\pi}f(r,\theta)\cos m\theta\,J_m(\lambda_{mn}r)r\,d\theta\,dr,\\
+> b_{mn}&=\frac2{\pi a^2J_{m+1}(\alpha_{mn})^2}\int_0^a\int_0^{2\pi}f(r,\theta)\sin m\theta\,J_m(\lambda_{mn}r)r\,d\theta\,dr.
+> \end{aligned}
+> $$
+> Here $n\ge1$, and $m\ge1$ in the last two formulas.
+
+*Printed equation label: (8).*
 
 In Section 12.3, we established (8) as a consequence of Fourier series and Bessel-Fourier series. A simpler and more direct derivation can be obtained using the orthogonality of the eigenfunctions (6) (see Exercise 4).
 
-## EXAMPLE 1 The method of eigenfunction expansions
-
-Solve $\nabla^{2} u(r, \theta)=u(r, \theta)+3 r^{2} \cos 2 \theta$ in the unit disk, given that $u=0$ on the boundary.
-
-Solution We look for a solution in the form of an eigenfunction expansion
+> [!exercise|4f5c71bb-48e5-5958-a0a3-959f43147764.local at=ed8d4fe0-8bf4-560f-a6c9-3e1ac832ab86] EXAMPLE 1 The method of eigenfunction expansions
+> Solve $\nabla^{2} u(r, \theta)=u(r, \theta)+3 r^{2} \cos 2 \theta$ in the unit disk, given that $u=0$ on the boundary.
+
+##### solution
+
+We look for a solution in the form of an eigenfunction expansion
 
 $$
 u(r, \theta)=\sum_{m=0}^{\infty} \sum_{n=1}^{\infty} J_{m}\left(\alpha_{m n} r\right)\left(A_{m n} \cos m \theta+B_{m n} \sin m \theta\right)
@@ -124,18 +145,29 @@
 \end{gathered}
 $$
 
-Figure 1 Decomposition of a Poisson problem.
+*Printed equation labels: (9) Poisson equation; (10) boundary data.*
 
 Our first step is to decompose the problem into the two simpler subproblems in Figure 1.
 
-![](./images/1c611338-958a-44f7-9d79-2dde87e6ac2a-42_534_1209_253_593.jpg)
-(a) Poisson problem with zero boundary data
-(b) Dirichlet problem
+```scientific-figure
+id: 61398d7a-1670-4663-91ae-eb64eaf47adc
+numbered: false
+title: ""
+caption: Figure 1 Decomposition into (a) a Poisson problem with zero boundary data and (b) a harmonic Dirichlet problem.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 12 Partial Differential Equations in Polar and Cylindrical Coordinates/images/1c611338-958a-44f7-9d79-2dde87e6ac2a-42_534_1209_253_593.jpg
+    caption: ""
+```
+
 
 The Dirichlet problem in Figure 1(b) can be solved by the methods of Section 12.4. Thus, to complete the solution, we need only solve Poisson's equation with zero boundary data (Figure 1(a)). We will use the method of eigenfunction expansions. This method tells us to look for a solution of (9) (with zero boundary data) in the form
 
 $$
 u(r, \theta)=\sum_{m=0}^{\infty} \sum_{n=1}^{\infty} J_{m}\left(\lambda_{m n} r\right)\left(A_{m n} \cos m \theta+B_{m n} \sin m \theta\right)
+\tag{11}
 $$
 
 Plugging into (9) and using the fact that each eigenfunction satisfies (1), we obtain
@@ -148,32 +180,38 @@
 
 $$
 A_{0 n}=\frac{-1}{\pi \alpha_{0 n}^{2} J_{1}^{2}\left(\alpha_{0 n}\right)} \int_{0}^{a} \int_{0}^{2 \pi} f(r, \theta) J_{0}\left(\lambda_{0 n} r\right) r d \theta d r
+\tag{12}
 $$
 
 $$
 A_{m n}=\frac{-2}{\pi \alpha_{m n}^{2} J_{m+1}^{2}\left(\alpha_{m n}\right)} \int_{0}^{a} \int_{0}^{2 \pi} f(r, \theta) \cos m \theta J_{m}\left(\lambda_{m n} r\right) r d \theta d r
+\tag{13}
 $$
 
 $$
 B_{m n}=\frac{-2}{\pi \alpha_{m n}^{2} J_{m+1}^{2}\left(\alpha_{m n}\right)} \int_{0}^{a} \int_{0}^{2 \pi} f(r, \theta) \sin m \theta J_{m}\left(\lambda_{m n} r\right) r d \theta d r
+\tag{14}
 $$
 
 This completely determines the solutions of the problem in Figure 1(a). We summarize our findings as follows.
 
-## SOLUTION OF POISSON'S PROBLEM IN A DISK
-
-The solution of the Poisson problem (9)-(10) is given by
-
-$$
-u(r, \theta)=u_{1}(r, \theta)+u_{2}(r, \theta),
-$$
-
-where $u_{1}$ is the solution of the Poisson problem with zero boundary data in Figure 1(a), and $u_{2}$ is the solution of the Dirichlet problem in Figure 1(b). The function $u_{1}$ is given by (11)-(14), and the function $u_{2}$ is given by (4)-(5), Section 12.4.
-
-## EXAMPLE 2 A Poisson problem with zero boundary data
-
-Solve $\nabla^{2} u=1$ in the unit disk, given that $u=0$ on the boundary.
-Solution Note that in this case $u_{2}=0$ in (15). The function $u_{1}$ is given by (11). Since the whole problem is independent of $\theta$, we expect the solution to be inclependent of $\theta$. Indeed, plugging $f(r, \theta)=1$ into (13) and (14), we get 0 because of the integral in $\theta$. Now (12) yields
+> [!note|ef333ef0-c62d-5624-8af6-a14de4c83bf7.local at=b9005dd7-d04c-5890-abef-5069ca7a91b6] Solution of Poisson's Problem in a Disk
+> The solution of the Poisson problem (9)-(10) is given by
+>
+> $$
+> u(r, \theta)=u_{1}(r, \theta)+u_{2}(r, \theta),
+> $$
+>
+> where $u_{1}$ is the solution of the Poisson problem with zero boundary data in Figure 1(a), and $u_{2}$ is the solution of the Dirichlet problem in Figure 1(b). The function $u_{1}$ is given by (11)-(14), and the function $u_{2}$ is given by (4)-(5), Section 12.4.
+
+*Printed equation label: (15) sum of the zero-boundary Poisson solution and the harmonic boundary lifting.*
+
+> [!exercise|94a1510d-9aac-5c6a-b407-7e32c73216e7.local at=3c980f13-90a5-56cf-8f11-8ecd9eca3180] EXAMPLE 2 A Poisson problem with zero boundary data
+> Solve $\nabla^{2} u=1$ in the unit disk, given that $u=0$ on the boundary.
+
+##### solution
+
+Note that in this case $u_{2}=0$ in (15). The function $u_{1}$ is given by (11). Since the whole problem is independent of $\theta$, we expect the solution to be independent of $\theta$. Indeed, plugging $f(r, \theta)=1$ into (13) and (14), we get 0 because of the integral in $\theta$. Now (12) yields
 
 $$
 A_{0 n}=\frac{-2}{\alpha_{0 n}^{2} J_{1}^{2}\left(\alpha_{0 n}\right)} \int_{0}^{1} J_{0}\left(\alpha_{0 n} r\right) r d r
@@ -187,82 +225,127 @@
 
 Interesting applications of the eigenfunction expansions method are presented in the exercises.
 
-## Exercises 4.6
-
-1. Derive (3) and (4) from (1) and (2).
-2. State and prove all the orthogonality relations for the eigenfunctions of the Helmholtz problem (1) and (2) ((7) is one of them).
-3. Let $\phi_{m n}(r, \theta)$ denote either one of the eigenfunctions in (6). Evaluate
-
-$$
-\int_{0}^{2 \pi} \int_{0}^{a} \phi_{m n}^{2}(r, \theta) r d r d \theta
-$$
-
-Treat the case $m=0$ separately. [Hint: Use (12), Section 12.8.]
-4. Derive the coefficients in Theorem 2 by using the orthogonality of the eigenfunctions (6). [Hint: Multiply both sides of (8) by an eigenfunction, interchange integrals and summation signs, then integrate over the disk with respect to $r d \theta d r$.]
-
-In Exercises 5-12, use the method of eigenfunction expansions to solve the given problem in the unit disk.
-5. $\nabla^{2} u=-u+1, u(1, \theta)=0$.
-6. $\nabla^{2} u=3 u+r \sin \theta, u(1, \theta)=0$.
-7. $\nabla^{2} u=2+r^{3} \cos 3 \theta, u(1, \theta)=0$.
-8. $\nabla^{2} u=r^{2}, u(1, \theta)=0$.
-9.
-
-$$
-\begin{gathered}
-\nabla^{2} u= \begin{cases}r \sin \theta & \text { if } 0<r<\frac{1}{2} \\
-0 & \text { if } \frac{1}{2}<r<1\end{cases} \\
-u(1, \theta)=0 .
-\end{gathered}
-$$
-
-10. $\nabla^{2} u=r^{m} \sin m \theta, u(1, \theta)=0$.
-11. $\nabla^{2} u=1, u(1, \theta)=\sin 2 \theta$.
-12. $\nabla^{2} u=1+r \cos \theta, u(1, \theta)=1$.
-13. A heat problem. Do Exercise 11, Section 12.3, using the method of eigenfunction expansions.
-14. Project Problem: A nonhomogeneous heat problem. For this project, you are asked to use the eigenfunction expansions method to solve the nonhomogeneous heat boundary value problem, with time-dependent heat source,
-
-$$
-\begin{gathered}
-\frac{\partial u}{\partial t}=c^{2}\left(\frac{\partial^{2} u}{\partial r^{2}}+\frac{1}{r} \frac{\partial u}{\partial r}+\frac{1}{r^{2}} \frac{\partial^{2} u}{\partial \theta^{2}}\right)+q(r, \theta, t) \\
-u(a, \theta, t)=0 \\
-u(r, \theta, 0)=f(r, \theta)
-\end{gathered}
-$$
-
-where $0<r<a, 0<\theta<2 \pi$, and $t>0$. Justify the following steps.
-(a) Let
-
-$$
-\begin{gathered}
-u(r, \theta, t)=\sum_{m=0}^{\infty} \sum_{n=1}^{\infty} J_{m}\left(\lambda_{m n} r\right)\left(A_{m n}(t) \cos m \theta+B_{m n}(t) \sin m \theta\right) \\
-f(r, \theta)=\sum_{m=0}^{\infty} \sum_{n=1}^{\infty} J_{m}\left(\lambda_{m n} r\right)\left(a_{m n} \cos m \theta+b_{m n} \sin m \theta\right) \\
-q(r, \theta, t)=\sum_{m=0}^{\infty} \sum_{n=1}^{\infty} J_{m}\left(\lambda_{m n} r\right)\left(c_{m n}(t) \cos m \theta+d_{m n}(t) \sin m \theta\right)
-\end{gathered}
-$$
-
-(Why should this be your starting point?) What are $a_{m n}, b_{m n}, c_{m n}(t)$, and $d_{m n}(t)$, in terms of $f$ and $q$ ?
-(b) Show that $A_{m n}$ and $B_{m n}$ are solutions of the following initial value problems:
-
-$$
-\begin{array}{ll}
-A_{m n}^{\prime}(t)+\lambda_{m n}^{2} A_{m n}(t)=c_{m n}(t), & A_{m n}(0)=a_{m n} \\
-B_{m n}^{\prime}(t)+\lambda_{m n}^{2} B_{m n}(t)=d_{m n}(t), & B_{m n}(0)=b_{m n}
-\end{array}
-$$
-
-(c) Complete the solution by showing that
-
-$$
-A_{m n}(t)=e^{-\lambda_{m n}^{2} t}\left(a_{m n}+\int_{0}^{t} e^{\lambda_{m n}^{2} s} c_{m n}(s) d s\right)
-$$
-
-and
-
-$$
-B_{m n}(t)=e^{-\lambda_{m n}^{2} t}\left(b_{m n}+\int_{0}^{t} e^{\lambda_{m n}^{2} s} d_{m n}(s) d s\right)
-$$
-
-15. (a) Work out the details in Exercise 14 when $c=1, f=1$, and $q(r, \theta, t)=e^{-t}$.
-(b) Plot the temperature of the center and describe what happens as $t \rightarrow \infty$.
-16. (a) Work out the details in Exercise 14 when $c=1, f=r \sin \theta$, and $q=1$.
-(b) Plot the temperature of the center and describe what happens as $t \rightarrow \infty$.
+## Exercises 12.6
+
+
+> [!exercise|8c1583bc-5087-5334-8bb7-0e6091bd1d3f.local at=a56c3933-a5b0-5973-81d7-611ee83e1012] Exercise 1
+> Derive (3) and (4) from (1) and (2).
+
+
+> [!exercise|7ff9d989-3925-5374-b292-7a9adfdbf16b.local at=e4c16987-4f11-5230-b1a1-3d604db06be6] Exercise 2
+> State and prove all the orthogonality relations for the eigenfunctions of the Helmholtz problem (1) and (2) ((7) is one of them).
+
+
+> [!exercise|96c88032-3548-5e04-a849-00789224022c.local at=2082eaf7-9594-55f0-95b2-5d06c6fc00c2] Exercise 3
+> Let $\phi_{m n}(r, \theta)$ denote either one of the eigenfunctions in (6). Evaluate
+>
+> $$
+> \int_{0}^{2 \pi} \int_{0}^{a} \phi_{m n}^{2}(r, \theta) r d r d \theta
+> $$
+>
+> Treat the case $m=0$ separately. [Hint: Use (12), Section 12.8.]
+
+
+> [!exercise|e0ede150-d784-56c4-8bbe-845f5d0798f8.local at=548b200d-459c-582b-bfea-c9ec637ead4f] Exercise 4
+> Derive the coefficients in Theorem 2 by using the orthogonality of the eigenfunctions (6). [Hint: Multiply both sides of (8) by an eigenfunction, interchange integrals and summation signs, then integrate over the disk with respect to $r d \theta d r$.]
+
+
+> [!prompt|8a1a701e-599b-53ef-bd62-4aced1d3c107.local at=abf333f1-21dc-5b63-87f4-526f69591a6e] Shared exercise instructions
+> In Exercises 5-12, use the method of eigenfunction expansions to solve the given problem in the unit disk.
+
+
+> [!exercise|bce38a2e-90bc-511d-b587-3676ebc52ffc.local at=55bf5f12-3120-5901-ac75-eaa756130d83] Exercise 5
+> $\nabla^{2} u=-u+1, u(1, \theta)=0$.
+
+
+> [!exercise|03744466-6626-5e2b-9109-9e9e3bf3c14f.local at=2c0c5662-2a74-5e97-a0c9-379d028566fb] Exercise 6
+> $\nabla^{2} u=3 u+r \sin \theta, u(1, \theta)=0$.
+
+
+> [!exercise|e377614f-eead-5012-9cb7-674c0d015c34.local at=6ea6a72c-518e-5f12-bf59-52a7957fbab0] Exercise 7
+> $\nabla^{2} u=2+r^{3} \cos 3 \theta, u(1, \theta)=0$.
+
+
+> [!exercise|2a9b153f-6cba-540d-8311-7ec550b312a2.local at=9a058462-8bed-508d-af1e-429c56bfdec5] Exercise 8
+> $\nabla^{2} u=r^{2}, u(1, \theta)=0$.
+
+
+> [!exercise|80d7148c-7d49-5419-8e37-e3102ea51d73.local at=de37da36-40ff-5000-9c88-821efeef04c9] Exercise 9
+> $$
+> \begin{gathered}
+> \nabla^{2} u= \begin{cases}r \sin \theta & \text { if } 0<r<\frac{1}{2} \\
+> 0 & \text { if } \frac{1}{2}<r<1\end{cases} \\
+> u(1, \theta)=0 .
+> \end{gathered}
+> $$
+
+
+> [!exercise|daa2af10-96d2-5f03-990f-bfe9ff8ea73c.local at=f3487448-ea79-590e-b4df-4106822b25e5] Exercise 10
+> $\nabla^{2} u=r^{m} \sin m \theta, u(1, \theta)=0$.
+
+
+> [!exercise|0553f8f7-d7aa-5a75-bd70-f332d5cef9c1.local at=fb51769a-6b5c-584f-9e19-9cd6fdac2194] Exercise 11
+> $\nabla^{2} u=1, u(1, \theta)=\sin 2 \theta$.
+
+
+> [!exercise|e4615913-e7d3-5da6-ba23-e09283201d2b.local at=2dc6120a-f3bb-50fd-8f89-12f31b6a7e60] Exercise 12
+> $\nabla^{2} u=1+r \cos \theta, u(1, \theta)=1$.
+
+
+> [!exercise|eccb84d3-bef9-5c6e-9081-a5039f8fada7.local at=3e763d87-a64c-56ce-bf92-961bce431ee6] Exercise 13
+> A heat problem. Do Exercise 11, Section 12.3, using the method of eigenfunction expansions.
+
+
+> [!exercise|cfcd8036-3586-5394-91ee-5fb189a4d2a0.local at=dff1d6ac-8388-5fd4-95c1-a7cdf8aa14e3] Exercise 14
+> Project Problem: A nonhomogeneous heat problem. For this project, you are asked to use the eigenfunction expansions method to solve the nonhomogeneous heat boundary value problem, with time-dependent heat source,
+>
+> $$
+> \begin{gathered}
+> \frac{\partial u}{\partial t}=c^{2}\left(\frac{\partial^{2} u}{\partial r^{2}}+\frac{1}{r} \frac{\partial u}{\partial r}+\frac{1}{r^{2}} \frac{\partial^{2} u}{\partial \theta^{2}}\right)+q(r, \theta, t) \\
+> u(a, \theta, t)=0 \\
+> u(r, \theta, 0)=f(r, \theta)
+> \end{gathered}
+> $$
+>
+> where $0<r<a, 0<\theta<2 \pi$, and $t>0$. Justify the following steps. 
+> (a) Let
+>
+> $$
+> \begin{gathered}
+> u(r, \theta, t)=\sum_{m=0}^{\infty} \sum_{n=1}^{\infty} J_{m}\left(\lambda_{m n} r\right)\left(A_{m n}(t) \cos m \theta+B_{m n}(t) \sin m \theta\right) \\
+> f(r, \theta)=\sum_{m=0}^{\infty} \sum_{n=1}^{\infty} J_{m}\left(\lambda_{m n} r\right)\left(a_{m n} \cos m \theta+b_{m n} \sin m \theta\right) \\
+> q(r, \theta, t)=\sum_{m=0}^{\infty} \sum_{n=1}^{\infty} J_{m}\left(\lambda_{m n} r\right)\left(c_{m n}(t) \cos m \theta+d_{m n}(t) \sin m \theta\right)
+> \end{gathered}
+> $$
+>
+> (Why should this be your starting point?) What are $a_{m n}, b_{m n}, c_{m n}(t)$, and $d_{m n}(t)$, in terms of $f$ and $q$ ?
+> (b) Show that $A_{m n}$ and $B_{m n}$ are solutions of the following initial value problems:
+>
+> $$
+> \begin{array}{ll}
+> A_{m n}^{\prime}(t)+c^{2}\lambda_{m n}^{2} A_{m n}(t)=c_{m n}(t), & A_{m n}(0)=a_{m n} \\
+> B_{m n}^{\prime}(t)+c^{2}\lambda_{m n}^{2} B_{m n}(t)=d_{m n}(t), & B_{m n}(0)=b_{m n}
+> \end{array}
+> $$
+>
+> (c) Complete the solution by showing that
+>
+> $$
+> A_{m n}(t)=e^{-c^{2}\lambda_{m n}^{2} t}\left(a_{m n}+\int_{0}^{t} e^{c^{2}\lambda_{m n}^{2} s} c_{m n}(s) d s\right)
+> $$
+>
+> and
+>
+> $$
+> B_{m n}(t)=e^{-c^{2}\lambda_{m n}^{2} t}\left(b_{m n}+\int_{0}^{t} e^{c^{2}\lambda_{m n}^{2} s} d_{m n}(s) d s\right)
+> $$
+
+
+> [!exercise|1aed32f5-fcf4-5c11-8c1b-a608c65e4316.local at=ce113b92-9923-5053-8592-f155064187e3] Exercise 15
+> (a) Work out the details in Exercise 14 when $c=1, f=1$, and $q(r, \theta, t)=e^{-t}$.
+> (b) Plot the temperature of the center and describe what happens as $t \rightarrow \infty$.
+
+
+> [!exercise|7c1fec9f-fa0b-594a-8902-fa49df3a0d60.local at=794c2de6-37c9-5faf-bbc3-6fa8a16558ae] Exercise 16
+> (a) Work out the details in Exercise 14 when $c=1, f=r \sin \theta$, and $q=1$.
+> (b) Plot the temperature of the center and describe what happens as $t \rightarrow \infty$.

`````
