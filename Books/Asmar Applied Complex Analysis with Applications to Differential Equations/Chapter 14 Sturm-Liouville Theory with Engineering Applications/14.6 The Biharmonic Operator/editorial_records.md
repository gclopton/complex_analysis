
# Editorial records

Reading note: 14.6 The Biharmonic Operator.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!definition|76835f9d-28d6-5f69-8417-b4f9e1169841.local at=1be6cc23-0b90-5b50-91a0-067c983cefa0] Biharmonic Operator and Biharmonic Functions
> For $u\in C^4(\Omega)$ on an open set $\Omega\subset\mathbb R^2$, the biharmonic operator is the iterated Laplacian,
>
> $$
> \nabla^4u=\nabla^2(\nabla^2u)=u_{xxxx}+2u_{xxyy}+u_{yyyy}.
> $$
>
> The function $u$ is biharmonic on $\Omega$ if $\nabla^4u=0$ there.
````
### After

````text
> [!definition|76835f9d-28d6-5f69-8417-b4f9e1169841.local at=1be6cc23-0b90-5b50-91a0-067c983cefa0] Biharmonic Operator and Biharmonic Functions
> The biharmonic operator of $u(x, y)$ is defined as
>
> $$
> \nabla^{4} u=\nabla^{2}\left(\nabla^{2} u\right) .
> $$ A function $u\in C^4$ is biharmonic if $\nabla^4u=0$.
````

## 2. Restore source wording; retain only the actual correction.

### Before

````text
The fourth partial derivatives introduce a mixed term. Substituting $u(x,y)=X(x)Y(y)$ into the Cartesian biharmonic equation gives

$$
X^{(4)}Y+2X^{\prime\prime}Y^{\prime\prime}+XY^{(4)}=0.
$$

This does not separate by the same immediate division-and-constant argument used for Laplace's equation. Special separated solutions still exist—for example, prescribing a sinusoidal factor in one coordinate reduces the equation to an ODE in the other. For the disk problems below, polar coordinates and a reduction to harmonic functions are particularly convenient.

[Source clarification: the printed assertion that Cartesian separation is impossible is too broad. The obstruction is to the simple separation step, not to all Cartesian separated solutions.]
````
### After

````text
The fourth partial derivatives present a mixed term, so the Cartesian biharmonic equation does not separate by the same immediate division-and-constant step used for Laplace's equation.
````

## 3. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|370f36f3-d8bc-5f47-90f8-c6b10700f5fe.local at=5369b0e0-c11b-5a65-b241-3e717de98fa2] Biharmonic Dirichlet Problem on a Disk via Two Harmonic Extensions
> Let $a>0$ and prescribe smooth $2\pi$-periodic functions $f,g$ on the boundary of the disk $D_a=\{r<a\}$. Let $w$ and then $v$ be the regular harmonic functions in the disk with boundary data
>
> $$
> w(a,\theta)=f(\theta),\qquad
> v(a,\theta)=\frac{w_r(a,\theta)-g(\theta)}{2a}.
> $$
>
> Then the unique smooth biharmonic solution of
>
> $$
> \nabla^4u=0\ \text{in }D_a,\qquad
> u(a,\theta)=f(\theta),\quad u_r(a,\theta)=g(\theta)
> $$
>
> is $u(r,\theta)=(a^2-r^2)v(r,\theta)+w(r,\theta)$.
````
### After

````text
> [!theorem|370f36f3-d8bc-5f47-90f8-c6b10700f5fe.local at=5369b0e0-c11b-5a65-b241-3e717de98fa2] Solution of the Biharmonic Equation
> The solution of the boundary value problem $\nabla^4u=0$ in the disk $r<a$, $u(a,\theta)=f(\theta)$, $u_r(a,\theta)=g(\theta)$, for smooth periodic data, is the biharmonic function
> $$
> u(r,\theta)=(a^2-r^2)v(r,\theta)+w(r,\theta),
> $$
> where $v$ and $w$ are solutions of the Dirichlet problems on the disk with boundary values $w(a,\theta)=f(\theta)$ (same as the boundary values of $u$) and $v(a,\theta)=[w_r(a,\theta)-g(\theta)]/(2a)$.
````

## Source-to-current comparison

Source: /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 14 Sturm-Liouville Theory with Engineering Applications/14.6 The Biharmonic Operator.md

This exact comparison preserves the full change evidence, including formatting, OCR corrections, restored source wording, and required standalone context. The entries above explain the recovery edits. The comparison is not a claim that every difference is a correction; component serialization, callout wrapping, and printed labels outside callouts are formatting.

`````diff
--- /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 14 Sturm-Liouville Theory with Engineering Applications/14.6 The Biharmonic Operator.md
+++ /Users/gradyclopton/ObsidianVaults/complex_analysis/Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 14 Sturm-Liouville Theory with Engineering Applications/14.6 The Biharmonic Operator.md
@@ -1,10 +1,16 @@
+
 ### 14.6 The Biharmonic Operator
 
-In this and the following sections we consider boundary value problems on plates. As in the case of beams, the equations will involve fourth-order partial derivatives with respect to the spacial variables, due to the rigidity of the plates. Whereas with membranes the Laplacian plays a central role, here the iterated Laplacian or biharmonic operator will be at the heart of most equations. The biharmonic operator of $u(x, y)$ is defined as
-
-$$
-\nabla^{4} u=\nabla^{2}\left(\nabla^{2} u\right) .
-$$
+In this and the following sections we consider boundary value problems on plates. As in the case of beams, the equations will involve fourth-order partial derivatives with respect to the spatial variables, due to the rigidity of the plates. Whereas with membranes the Laplacian plays a central role, here the iterated Laplacian or biharmonic operator will be at the heart of most equations.
+
+> [!definition|76835f9d-28d6-5f69-8417-b4f9e1169841.local at=1be6cc23-0b90-5b50-91a0-067c983cefa0] Biharmonic Operator and Biharmonic Functions
+> The biharmonic operator of $u(x, y)$ is defined as
+>
+> $$
+> \nabla^{4} u=\nabla^{2}\left(\nabla^{2} u\right) .
+> $$ A function $u\in C^4$ is biharmonic if $\nabla^4u=0$.
+
+*Printed equation label: (1).*
 
 In Cartesian coordinates,
 
@@ -14,37 +20,31 @@
 & =u_{x x x x}+u_{y y x x}+u_{x x y y}+u_{y y y y} \\
 & =u_{x x x x}+2 u_{y y x x}+u_{y y y y}
 \end{aligned}
-$$
-
-The fourth partial derivatives present a new challenge. Moreover, unlike Laplace's equation, you cannot separate the variables in the biharmonic equation in Cartesian coordinates:
-
-$$
-u_{x x x x}+2 u_{y y x x}+u_{y y y y}=0
-$$
-
-In fact, if we set $u(x, y)=X(x) Y(y)$ and plug into the equation, we get
-
-$$
-X^{\prime \prime \prime \prime} Y+2 X^{\prime \prime} Y^{\prime \prime}+X Y^{\prime \prime \prime \prime}=0,
-$$
-
-and clearly the variables cannot be separated in this equation. It turns out, however, that we can separate the variables in the biharmonic equation in polar coordinates. It is still an overwhelming task to work with the biharmonic equation directly. Instead, in this and the following section, as we search for analytical solutions, we will use clever methods to reduce to problems involving the Laplacian. These reductions work in polar coordinates but again fail in Cartesian coordinates. Because of this fact, we will forgo the search for analytical solutions in Cartesian coordinates (numerical solutions can be used for such problems) and work in polar coordinates.
+\tag{2}
+$$
+
+The fourth partial derivatives present a mixed term, so the Cartesian biharmonic equation does not separate by the same immediate division-and-constant step used for Laplace's equation.
 
 We call a biharmonic function any solution of the biharmonic equation. Observe that any harmonic function $u$ is also biharmonic. This is clear, since if $\nabla^{2} u=0$, then $\nabla^{4}(u)=\nabla^{2}\left(\nabla^{2}(u)\right)=\nabla^{2}(0)=0$. The following provides a way to construct biharmonic functions, which are not necessarily harmonic.
 
-## EXAMPLE 1 Biharmonic functions
-
-Show that if $u=u(x, y)$ is harmonic and
-
-$$
-v=u \cdot\left(A\left(x^{2}+y^{2}\right)+B x+C y+D\right),
-$$
-
-where $A, B, C$, and $D$ are constants, then $v$ is biharmonic.
-Solution We have to verify that $\nabla^{4} v=0$. As a first step, establish the identity
+> [!exercise|3c4358c4-1c42-5b00-9e7f-7f2dbdbacde5.local at=873588bc-c7e3-5021-a63d-7bd824a37fc1] EXAMPLE 1 Biharmonic functions
+> Show that if $u=u(x, y)$ is harmonic and
+>
+> $$
+> v=u \cdot\left(A\left(x^{2}+y^{2}\right)+B x+C y+D\right),
+> $$
+>
+> where $A, B, C$, and $D$ are constants, then $v$ is biharmonic.
+
+*Printed equation label: (3).*
+
+##### solution
+
+We have to verify that $\nabla^{4} v=0$. As a first step, establish the identity
 
 $$
 \nabla^{2}(\phi \cdot \psi)=\psi \nabla^{2}(\phi)+\phi \nabla^{2}(\psi)+2 \phi_{x} \psi_{x}+2 \phi_{y} \psi_{y}
+\tag{4}
 $$
 
 (Exercise 10). Apply this identity with $u=\phi$ and $\psi=A\left(x^{2}+y^{2}\right)+B x+C y+D$, $\nabla^{2} u=0(u$ is harmonic $), \nabla^{2}\left(A\left(x^{2}+y^{2}\right)+B x+C y+D\right)=4 A, \psi_{x}=2 A x+B$, and $\psi_{y}=2 A y+C$; then
@@ -66,8 +66,19 @@
 
 because $(2 A x+B)_{y}=0$. Similarly, $\nabla^{2}\left(u_{y}(2 A y+C)\right)=4 A u_{y y}$. Hence $\nabla^{4} v= 8 A u_{x x}+8 A u_{y y}=8 A\left(u_{x x}+u_{y y}\right)=0$.
 
-![](./images/28f4ed6f-dce0-442f-8bed-abc918ef4e83-47_486_463_359_42.jpg)
-Figure 1 A biharmonic function that attains its maximum inside a region.
+```scientific-figure
+id: 40bcd4ad-3796-4d0d-9c81-ff22a2af5122
+numbered: false
+title: ""
+caption: Figure 1 A biharmonic function that attains its maximum inside a region.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 14 Sturm-Liouville Theory with Engineering Applications/images/28f4ed6f-dce0-442f-8bed-abc918ef4e83-47_486_463_359_42.jpg
+    caption: ""
+```
+
 
 Taking $u(x, y)=1, A=-1, D=1$, and $B=C=0$ in (3), we obtain
 
@@ -75,7 +86,7 @@
 v(x, y)=1-x^{2}-y^{2} .
 $$
 
-We have $\nabla^{2} v=-2-2=-4$ and $\nabla^{4} v=\nabla^{2}(-4)=0$. Thus, as expected, $v$ is biharmonic but not harmonic. The graph of $v$ over the rectangle $-1 \leq x, y \leq 1$, in Figure 1, illustrates an important distinction between harmonic and biharmonic functions. The maximum value of $v$ is attained at the point $(0,0)$ inside the rectangle, which is unlike nonconstant harmonic functions whose maximum and minimum values must occur on the boundary (the maximum principle, Section 3.11). Thus the maximum principle, which holds for harmonic functions, fails for biharmonic functions.
+We have $\nabla^{2} v=-2-2=-4$ and $\nabla^{4} v=\nabla^{2}(-4)=0$. Thus, as expected, $v$ is biharmonic but not harmonic. The graph of $v$ over the rectangle $-1 \leq x, y \leq 1$, in Figure 1, illustrates an important distinction between harmonic and biharmonic functions. The maximum value of $v$ is attained at the point $(0,0)$ inside the rectangle, which is unlike nonconstant harmonic functions whose maximum and minimum values must occur on the boundary (the maximum principle, Section 11.11). Thus the maximum principle, which holds for harmonic functions, fails for biharmonic functions.
 
 ## Solution of the Biharmonic Equation
 
@@ -83,29 +94,31 @@
 
 $$
 \nabla^{4} u=0, \quad 0 \leq r<a, \quad 0 \leq \theta \leq 2 \pi .
+\tag{5}
 $$
 
 Because the biharmonic equation involves fourth order derivatives, we impose two conditions on the boundary that specify the boundary values of $u$ and its normal derivative. Since the normal derivative is $\frac{\partial u}{\partial r}$ (or simply $u_{r}$ ) for the disk, we will consider (5) subject to the boundary conditions
 
 $$
 u(a, \theta)=f(\theta), \quad \frac{\partial u}{\partial r}(a, \theta)=g(\theta), \quad 0 \leq \theta \leq 2 \pi .
+\tag{6}
 $$
 
 We solve the boundary value problem (5)-(6) by reducing it to two Dirichlet problems on the disk, as follows. Consider a function of the form
 
 $$
 u(r, \theta)=\left(a^{2}-r^{2}\right) v(r, \theta)+w(r, \theta)
+\tag{7}
 $$
 
 where $v$ and $w$ are harmonic. Since $r^{2}=x^{2}+y^{2}$, it follows from Example 1 that $\left(a^{2}-r^{2}\right) v$ is biharmonic. And since $w$ is biharmonic, it follows that the right side of (7) is biharmonic, being the sum of two biharmonic functions. So $u$ satisfies (5). We next determine $v$ and $w$ so as to satisfy the boundary conditions (6). Since both $v$ and $w$ are harmonic, they are determined by their values on the boundary of the disk. Setting $r=a$ in (7) and using $u(a, \theta)=f(\theta)$, we determine the boundary values for $w$ :
 
 $$
 w(a, \theta)=f(\theta)
-$$
-
-Thus $w$ is the (unique) solution of the Dirichlet problem on the disk with boundary values (8). To find $w$, we use techniques from Section 4.4. Next, we determine the boundary values of $v$, which in turn will determine $v$ itself.
-
-## THEOREM 1 SOLUTION OF THE BIHARMONIC EQUATION
+\tag{8}
+$$
+
+Thus $w$ is the (unique) solution of the Dirichlet problem on the disk with boundary values (8). To find $w$, we use techniques from Section 12.4. Next, we determine the boundary values of $v$, which in turn will determine $v$ itself.
 
 For this purpose, differentiate both sides of (7) with respect to $r$, set $r=a$, use $u_{r}(a, \theta)=g(\theta)$, and get
 
@@ -115,32 +128,52 @@
 u_{r}(a, \theta)=g(\theta) & =-2 a v(a, \theta)+w_{r}(a, \theta) ; \\
 v(a, \theta) & =\frac{1}{2 a}\left(w_{r}(a, \theta)-g(\theta)\right) .
 \end{aligned}
-$$
-
-Figure 2 Decomposition of a biharmonic problem with two boundary conditions into two Dirichlet problems with one boundary condition each.
-![](./images/28f4ed6f-dce0-442f-8bed-abc918ef4e83-48_462_1285_566_569.jpg)
-
-Since $w$ is determined at this point, $w_{r}(a, \theta)$ is therfore known and the last equation determines the boundary values of $v$. Thus $v$ is the (unique) solution of the Dirichlet problem inside the disk with boundary values (9). This determines $v$ and $w$ in (7) and solves the boundary value problem (5)(6). The method is illustrated in Figure 2 and summarized in Theorem 1.
-
-The solution of the boundary value problem (5)-(6) is the biharmonic function $u$ given by (7), where $v$ and $w$ are solutions of the Dirichlet problems on the disk with boundary values for $w$ given by (8) (same as the boundary values of $u$ ) and boundary values for $v$ given by (9).
+\tag{9}
+$$
+
+```scientific-figure
+id: 78991899-383c-4b52-bdbd-5839ef8f1a2d
+numbered: false
+title: ""
+caption: Figure 2 Decomposition of a biharmonic problem with two boundary conditions into two Dirichlet problems with one boundary condition each.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 14 Sturm-Liouville Theory with Engineering Applications/images/28f4ed6f-dce0-442f-8bed-abc918ef4e83-48_462_1285_566_569.jpg
+    caption: ""
+```
+
+
+Since $w$ is determined at this point, $w_{r}(a, \theta)$ is therefore known and the last equation determines the boundary values of $v$. Thus $v$ is the (unique) solution of the Dirichlet problem inside the disk with boundary values (9). This determines $v$ and $w$ in (7) and solves the boundary value problem (5)(6). The method is illustrated in Figure 2 and summarized in Theorem 1.
+
+> [!theorem|370f36f3-d8bc-5f47-90f8-c6b10700f5fe.local at=5369b0e0-c11b-5a65-b241-3e717de98fa2] Solution of the Biharmonic Equation
+> The solution of the boundary value problem $\nabla^4u=0$ in the disk $r<a$, $u(a,\theta)=f(\theta)$, $u_r(a,\theta)=g(\theta)$, for smooth periodic data, is the biharmonic function
+> $$
+> u(r,\theta)=(a^2-r^2)v(r,\theta)+w(r,\theta),
+> $$
+> where $v$ and $w$ are solutions of the Dirichlet problems on the disk with boundary values $w(a,\theta)=f(\theta)$ (same as the boundary values of $u$) and $v(a,\theta)=[w_r(a,\theta)-g(\theta)]/(2a)$.
 
 As in the derivation of the solution, when solving a biharmonic equation inside the disk, we first find $w$ and then $v$, since the boundary values of $v$ depend on those of $w$.
 
-## EXAMPLE 2 Biharmonic equation
-
-On the unit disk, solve
-
-$$
-\nabla^{4} u=0, \quad u(1, \theta)=\cos \theta \quad \text { and } \quad u_{r}(1, \theta)=\sin \theta .
-$$
-
-Solution According to Theorem 1, the solution is of the form
+> [!exercise|c28a406a-a1ca-5186-bfa0-71977fd55516.local at=330a42e1-a530-5d48-95ab-ed6a3cfe99b9] EXAMPLE 2 Biharmonic equation
+> On the unit disk, solve
+>
+> $$
+> \nabla^{4} u=0, \quad u(1, \theta)=\cos \theta \quad \text { and } \quad u_{r}(1, \theta)=\sin \theta .
+> $$
+
+*Printed equation label: (10).*
+
+##### solution
+
+According to Theorem 1, the solution is of the form
 
 $$
 u(r, \theta)=\left(1-r^{2}\right) v+w
 $$
 
-where $v$ and $w$ are harmonic functions in the unit disk. The boundary values of $w$ are the same as those of $u$. Thus, to find $w$, we must solve $\nabla^{2} w=0$ subject to $w(1, \theta)=\cos \theta$. We know from Section 4.4 that the solution of this problem is given by $w(r, \theta)=a_{0}+\sum_{n=1}^{\infty} r^{n}\left(a_{n} \cos n \theta+b_{n} \sin n \theta\right)$, where $a_{n}$ and $b_{n}$ are the Fourier coefficients of the boundary function, $f(\theta)=\cos \theta$. Immediately, we conclude that $a_{1}=1$ and all other coefficients are 0 . So $w(r, \theta)=r \cos \theta$.
+where $v$ and $w$ are harmonic functions in the unit disk. The boundary values of $w$ are the same as those of $u$. Thus, to find $w$, we must solve $\nabla^{2} w=0$ subject to $w(1, \theta)=\cos \theta$. We know from Section 12.4 that the solution of this problem is given by $w(r, \theta)=a_{0}+\sum_{n=1}^{\infty} r^{n}\left(a_{n} \cos n \theta+b_{n} \sin n \theta\right)$, where $a_{n}$ and $b_{n}$ are the Fourier coefficients of the boundary function, $f(\theta)=\cos \theta$. Immediately, we conclude that $a_{1}=1$ and all other coefficients are 0 . So $w(r, \theta)=r \cos \theta$.
 
 Having found $w$, we can determine the boundary values of $v$ from (9), using $g(\theta)=\sin \theta$ and $\left.w_{r}(r, \theta)\right|_{r=1}=\cos \theta$. We have
 
@@ -158,22 +191,26 @@
 
 Even though the boundary conditions in Example 2 are somewhat special, they do illustrate the process of solving a biharmonic equation by reducing to two Dirichlet problems and the role of Fourier series. Here is one more illustration.
 
-## EXAMPLE 3 Biharmonic function with 0 boundary values
-
-On the unit disk, show that the solution of the boundary value problem
-
-$$
-\nabla^{4} u=0, \quad u(1, \theta)=0 \text { and } u_{r}(1, \theta)=g(\theta)
-$$
-
-is given by
-
-$$
-u(r, \theta)=-\frac{1}{2}\left(1-r^{2}\right)\left[a_{0}+\sum_{n=1}^{\infty} r^{n}\left(a_{n} \cos n \theta+b_{n} \sin n \theta\right)\right]
-$$
-
-where $a_{0}, a_{n}$ and $b_{n}$ are the Fourier coefficients of $g$.
-Solution By Theorem 1, the solution is of the form
+> [!exercise|0c0780b4-0c97-596b-a2ea-c24123f14ffe.local at=f45108c7-2d9b-59fa-b93e-6336440e5c47] EXAMPLE 3 Biharmonic function with 0 boundary values
+> On the unit disk, show that the solution of the boundary value problem
+>
+> $$
+> \nabla^{4} u=0, \quad u(1, \theta)=0 \text { and } u_{r}(1, \theta)=g(\theta)
+> $$
+>
+> is given by
+>
+> $$
+> u(r, \theta)=-\frac{1}{2}\left(1-r^{2}\right)\left[a_{0}+\sum_{n=1}^{\infty} r^{n}\left(a_{n} \cos n \theta+b_{n} \sin n \theta\right)\right]
+> $$
+>
+> where $a_{0}, a_{n}$ and $b_{n}$ are the Fourier coefficients of $g$.
+
+*Printed equation label: (11).*
+
+##### solution
+
+By Theorem 1, the solution is of the form
 
 $$
 u(r, \theta)=\left(1-r^{2}\right) v+w
@@ -185,15 +222,13 @@
 u(r, \theta)=\left(1-r^{2}\right) v
 $$
 
-To solve the given problem, start with a biharmonic function of the form described by Exercise 9 and determine the constants in order to satisfy the boundary conditions.
-
 Using (9) and the fact that $w_{r}=0$, we obtain the boundary values of $v$ :
 
 $$
 v(1, \theta)=-\frac{1}{2} g(\theta) .
 $$
 
-Using results from Section 4.4, we find that the solution of the Dirichlet problem with boundary values $-\frac{1}{2} g(\theta)$ is
+Using results from Section 12.4, we find that the solution of the Dirichlet problem with boundary values $-\frac{1}{2} g(\theta)$ is
 
 $$
 v(r, \theta)=-\frac{1}{2}\left[a_{0}+\sum_{n=1}^{\infty} r^{n}\left(a_{n} \cos n \theta+b_{n} \sin n \theta\right)\right],
@@ -201,36 +236,110 @@
 
 where $a_{0}, a_{n}$ and $b_{n}$ are the Fourier coefficients of $g$. This determines $v$ and shows that the desired solution is as claimed.
 
-## Exercises 6.6
-
-In Exercises 1-8, verify that the given function is biharmonic. Use the result of Example 1 where appropriate. In what follows, $(x, y)$ denote Cartesian coordinates, $(r, \theta)$ polar coordinates, and $n$ an integer.
-
-1. $x^{4}-y^{4}$.
-2. $x y^{2}+y x^{2}+x^{3}-2 y^{3}$.
-3. $\frac{x^{2}}{x^{2}+y^{2}}$.
-4. $\frac{x y}{x^{2}+y^{2}}$.
-5. $\left(1-r^{2}\right) r^{2} \cos 2 \theta$.
-6. $r^{3}(\cos \theta+\sin \theta)$.
-7. $r^{n+2} \cos n \theta$.
-8. $r^{2} \ln r$.
-
-## 11.
-
-![](./images/28f4ed6f-dce0-442f-8bed-abc918ef4e83-50_398_493_1336_578.jpg)
-Figure 3 for Exercise 11.
-
-12. 
-
-![](./images/28f4ed6f-dce0-442f-8bed-abc918ef4e83-50_401_495_1333_1216.jpg)
-Figure 4 for Exercise 12.
-
-9. Show that $a r^{2} \ln r+b r^{2}+c \ln r+d$ is biharmonic, where $a, b, c, d$ are constants. This function is useful in solving the biharmonic equation in an annulus with boundary data independent of $\theta$. See Exercises 11 and 12 .
-10. Prove (4).
-
-In Exercises 11 and 12, solve the problem that is described in the figure.
-13. On the unit disk, solve $\nabla^{4} u=0$, subject to $u(1, \theta)=\cos 2 \theta$ and $u_{r}(1, \theta)=0$.
-14. On the unit disk, solve $\nabla^{4} u=0$, subject to $u(1, \theta)=0$ and $u_{T}(1, \theta)=1$.
-15. On the unit disk, solve $\nabla^{4} u=0$, subject to $u(1, \theta)=1$ and $u_{T}(1, \theta)=\cos \theta$.
-16. On the unit disk, solve $\nabla^{4} u=0, u(1, \theta)=0$ and $u_{r}(1, \theta)=\theta^{2},-\pi<\theta<\pi$.
-17. On the unit disk, solve $\nabla^{4} u=0$, subject to $u(1, \theta)=0$ and $u_{r}(1, \theta)=g(\theta)$.
-18. On the unit disk, solve $\nabla^{4} u=0$, subject to $u(1, \theta)=f(\theta)$ and $u_{r}(1, \theta)=0$.
+## Exercises 14.6
+
+
+> [!prompt|c79250fe-2137-5e49-85c9-8088a94de732.local at=9241cca8-b60a-55aa-a0b4-0c30be260d80] Shared exercise instructions
+> In Exercises 1-8, verify that the given function is biharmonic. Use the result of Example 1 where appropriate. In what follows, $(x, y)$ denote Cartesian coordinates, $(r, \theta)$ polar coordinates, and $n$ an integer. Work away from $r=0$ wherever the expression is singular; no smooth extension through the origin is claimed in those cases.
+
+
+> [!exercise|f1588d83-0c18-577d-909b-bdce08bd8241.local at=ca5b9201-7bc2-5bb8-9274-53b69b66f1a1] Exercise 1
+> $x^{4}-y^{4}$.
+
+
+> [!exercise|833f1ccb-c0ac-5d9b-95e5-691eb2b7e7e4.local at=1c78f119-61f0-5a9f-bab0-6726a6bd4658] Exercise 2
+> $x y^{2}+y x^{2}+x^{3}-2 y^{3}$.
+
+
+> [!exercise|8512c849-982d-5a5c-9de0-05f433944191.local at=340b5d24-0bdf-5c83-a349-525f7cfc8709] Exercise 3
+> $\frac{x^{2}}{x^{2}+y^{2}}$.
+
+
+> [!exercise|07ae8016-d305-5be7-9ac3-53cf284b79d3.local at=cce9f435-c1af-56f5-8acc-7100fe3ffbcf] Exercise 4
+> $\frac{x y}{x^{2}+y^{2}}$.
+
+
+> [!exercise|54c46fc5-2563-5873-bdc2-ed437f100192.local at=4c81c037-69ba-5b9e-929d-8acc53ae989b] Exercise 5
+> $\left(1-r^{2}\right) r^{2} \cos 2 \theta$.
+
+
+> [!exercise|22a4c812-b9e6-589e-a974-ac8c568d5e8a.local at=0973fb5e-affc-5c1f-a1f4-c9cc3c2a5196] Exercise 6
+> $r^{3}(\cos \theta+\sin \theta)$.
+
+
+> [!exercise|c2834f4f-4cd3-593e-a765-8e6d68db5df1.local at=25a43fe5-6747-523f-8789-15a079cea746] Exercise 7
+> $r^{n+2} \cos n \theta$.
+
+
+> [!exercise|220b734d-5479-5e10-aafd-2d89f5245f87.local at=321b4d83-25ea-55bb-a67e-f2d5796af5c4] Exercise 8
+> $r^{2} \ln r$.
+
+
+> [!exercise|169d8910-74f2-5169-acd7-dd2b148cc28a.local at=11ed9d0c-1734-571e-b698-743fe3a3c189] Exercise 9
+> Show that $a r^{2} \ln r+b r^{2}+c \ln r+d$ is biharmonic, where $a, b, c, d$ are constants. This function is useful in solving the biharmonic equation in an annulus with boundary data independent of $\theta$. See Exercises 11 and 12 .
+
+
+> [!exercise|ddb19ac0-62d9-587f-b70d-984eec504518.local at=a374d2a8-7cce-5d0c-be23-291e119fa464] Exercise 10
+> Prove (4).
+
+
+> [!prompt|828797b5-a48d-59b3-a444-36e380bc06ea.local at=e8c80602-c10f-5992-8e99-5598ec15f696] Shared exercise instructions
+> In Exercises 11 and 12, solve the problem described in the corresponding figure.
+>
+> To solve the given problem, start with a biharmonic function of the form described by Exercise 9 and determine the constants in order to satisfy the boundary conditions.
+
+
+> [!exercise|5bf8a915-cd1d-5562-bdf9-72404c4f3052.local at=73de5f58-5d49-5013-b858-623bca33497b] Exercise 11
+> Solve the annular biharmonic problem in Figure 3.
+
+
+```scientific-figure
+id: 4be79bba-12a5-437b-88a6-1ad5c44f4ebb
+numbered: false
+title: ""
+caption: Figure 3 for Exercise 11.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 14 Sturm-Liouville Theory with Engineering Applications/images/28f4ed6f-dce0-442f-8bed-abc918ef4e83-50_398_493_1336_578.jpg
+    caption: ""
+```
+> [!exercise|2912b4e3-4079-5e82-bcf8-680dcb42b136.local at=cf8bd93a-9f11-5f24-b0d4-5e881ac161e4] Exercise 12
+> Solve the annular biharmonic problem in Figure 4.
+
+
+```scientific-figure
+id: 6397e524-8a1e-4fde-bb80-123a9bb2d143
+numbered: false
+title: ""
+caption: Figure 4 for Exercise 12.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 14 Sturm-Liouville Theory with Engineering Applications/images/28f4ed6f-dce0-442f-8bed-abc918ef4e83-50_401_495_1333_1216.jpg
+    caption: ""
+```
+> [!exercise|10af56d4-776b-5ca3-a246-bdcbc96404b1.local at=683130f5-87c8-5a14-93eb-5e45c7026797] Exercise 13
+> On the unit disk, solve $\nabla^{4} u=0$, subject to $u(1, \theta)=\cos 2 \theta$ and $u_{r}(1, \theta)=0$.
+
+
+> [!exercise|5f9ece0a-84d8-5f97-9392-995311b292ac.local at=cf55d92c-a01a-5fe3-8871-c5fb7fc9553c] Exercise 14
+> On the unit disk, solve $\nabla^{4} u=0$, subject to $u(1, \theta)=0$ and $u_{r}(1, \theta)=1$.
+
+
+> [!exercise|8524255b-82cd-5cad-ad74-1b7eeaff45dd.local at=f7ded791-06de-5979-aee8-6ef9b39c13ec] Exercise 15
+> On the unit disk, solve $\nabla^{4} u=0$, subject to $u(1, \theta)=1$ and $u_{r}(1, \theta)=\cos \theta$.
+
+
+> [!exercise|73aabe49-4a48-5a39-9f27-a6e8e03504ce.local at=e402d7d5-c7e7-51cc-9329-6692c502498f] Exercise 16
+> On the unit disk, solve $\nabla^{4} u=0, u(1, \theta)=0$ and $u_{r}(1, \theta)=\theta^{2},-\pi<\theta<\pi$.
+
+
+> [!exercise|ad02e7c8-23b5-5c12-b61a-b59bbf6c3586.local at=12af4f49-b3b4-5971-8d27-005385ba04e5] Exercise 17
+> On the unit disk, solve $\nabla^{4} u=0$, subject to $u(1, \theta)=0$ and $u_{r}(1, \theta)=g(\theta)$.
+
+
+> [!exercise|f8a6a1be-968a-55ea-acd0-6c241e772441.local at=1d1dcf72-5599-5048-a0d9-5faa2855e91a] Exercise 18
+> On the unit disk, solve $\nabla^{4} u=0$, subject to $u(1, \theta)=f(\theta)$ and $u_{r}(1, \theta)=0$.

`````
