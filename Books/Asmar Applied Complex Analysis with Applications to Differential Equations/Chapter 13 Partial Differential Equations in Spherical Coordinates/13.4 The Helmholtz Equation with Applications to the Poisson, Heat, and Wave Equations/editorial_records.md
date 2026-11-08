
# Editorial records

Reading note: 13.4 The Helmholtz Equation with Applications to the Poisson, Heat, and Wave Equations.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|efc5ac01-2469-5568-8a2b-ec8c4e0b0503.local at=6e849eda-9451-5496-91cc-c8f567c7d2f9] Dirichlet eigenfunctions of the negative Laplacian in a ball
> Let $a>0$. Use spherical coordinates with colatitude $\theta$, azimuth $\phi$, and volume measure $dV=r^2\sin\theta\,dr\,d\theta\,d\phi$. Write $Y_{n,m}$ for the standard unit-sphere orthonormal complex spherical harmonics and $j_n$ for the spherical Bessel function of the first kind. Let $\alpha_{n+1/2,j}$ be the $j$th positive zero of the ordinary Bessel function $J_{n+1/2}$, and set $\lambda_{n,j}=\alpha_{n+1/2,j}/a$ and
> $$
> \Psi_{jnm}(r,\theta,\phi)=j_n(\lambda_{n,j}r)Y_{n,m}(\theta,\phi),
> \qquad j\ge1,\ n\ge0,\ -n\le m\le n.
> $$
>
> The problem $-\Delta\Psi=k\Psi$ in the ball $r<a$, with zero boundary value at $r=a$ and regularity throughout the ball, has positive eigenvalues $k=\lambda_{n,j}^2$. For each fixed pair $(n,j)$, the functions $\Psi_{jnm}$ with $-n\le m\le n$ give $2n+1$ linearly independent angular modes. There is no nonzero zero-eigenvalue solution.
````
### After

````text
> [!theorem|efc5ac01-2469-5568-8a2b-ec8c4e0b0503.local at=6e849eda-9451-5496-91cc-c8f567c7d2f9] Helmholtz Equation in a Ball
> The eigenvalue problem $\nabla^2u+ku=0$ in $r<a$, regular at the origin and satisfying $u=0$ at $r=a$, has eigenvalues $k=\lambda^{2}$, where $\lambda=\lambda_{n, j}$ is defined below. To each eigenvalue correspond $2 n+1$ eigenfunctions
>
> $$
> \Psi_{j n m}(r, \theta, \phi)=j_{n}\left(\lambda_{n, j} r\right) Y_{n, m}(\theta, \phi),
> $$
>
> where $|m| \leq n$.
>
> Let $a>0$, let $j_n$ be the spherical Bessel function of the first kind, and set $\lambda_{n,j}=\alpha_{n+1/2,j}/a$, where $\alpha_{n+1/2,j}$ is the $j$th positive zero of $J_{n+1/2}$. Here $Y_{n,m}(\theta,\phi)=\sqrt{\frac{2n+1}{4\pi}\frac{(n-m)!}{(n+m)!}}P_n^m(\cos\theta)e^{im\phi}$, where $\theta$ is colatitude, $\phi$ is azimuth, and $P_n^m$ is the associated Legendre function.
````

## 2. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|b5a977f6-80ae-5e5d-893a-641f2e6133da.local at=d53f3db2-ed96-5b4d-a721-171b5604e268] Orthogonality and norms of spherical Dirichlet modes in a ball
> Let $a>0$. Use spherical coordinates with colatitude $\theta$, azimuth $\phi$, and volume measure $dV=r^2\sin\theta\,dr\,d\theta\,d\phi$. Write $Y_{n,m}$ for the standard unit-sphere orthonormal complex spherical harmonics and $j_n$ for the spherical Bessel function of the first kind. Let $\alpha_{n+1/2,j}$ be the $j$th positive zero of the ordinary Bessel function $J_{n+1/2}$, and set $\lambda_{n,j}=\alpha_{n+1/2,j}/a$ and
> $$
> \Psi_{jnm}(r,\theta,\phi)=j_n(\lambda_{n,j}r)Y_{n,m}(\theta,\phi),
> \qquad j\ge1,\ n\ge0,\ -n\le m\le n.
> $$
>
> These modes are orthogonal for the volume inner product:
> $$
> \int_{r<a}\Psi_{jnm}\overline{\Psi_{j'n'm'}}\,dV=0\quad\text{if }(j,n,m)\ne(j',n',m'),
> $$
> and
> $$
> \int_{r<a}|\Psi_{jnm}|^2\,dV=\frac{a^3}2j_{n+1}(\alpha_{n+1/2,j})^2.
> $$
````
### After

````text
> [!theorem|b5a977f6-80ae-5e5d-893a-641f2e6133da.local at=d53f3db2-ed96-5b4d-a721-171b5604e268] Orthogonality of Solutions of the Helmholtz Equation
> For $j=1,2, \ldots, n=0,1,2, \ldots$, and $|m| \leq n$, we have
>
> $$
> \int_{0}^{a} \int_{0}^{2 \pi} \int_{0}^{\pi} j_{n}\left(\lambda_{n, j} r\right) Y_{n, m}(\theta, \phi) j_{n^{\prime}}\left(\lambda_{n^{\prime}, j^{\prime}} r\right) \bar{Y}_{n^{\prime}, m^{\prime}}(\theta, \phi) r^{2} \sin \theta d \theta d \phi d r=0
> $$
>
> for $(j, n, m) \neq\left(j^{\prime}, n^{\prime}, m^{\prime}\right)$, and
>
> $$
> \int_{0}^{a} \int_{0}^{2 \pi} \int_{0}^{\pi} j_{n}^{2}\left(\lambda_{n, j} r\right)\left|Y_{n, m}(\theta, \phi)\right|^{2} r^{2} \sin \theta d \theta d \phi d r=\frac{a^{3}}{2} j_{n+1}^{2}\left(\alpha_{n+\frac{1}{2}, j}\right)
> $$
>
> where $\alpha_{n+\frac{1}{2}, j}$ is the $j$ th positive zero of $J_{n+\frac{1}{2}}$.
>
> Let $a>0$, let $j_n$ be the spherical Bessel function of the first kind, and set $\lambda_{n,j}=\alpha_{n+1/2,j}/a$, where $\alpha_{n+1/2,j}$ is the $j$th positive zero of $J_{n+1/2}$. Here $Y_{n,m}(\theta,\phi)=\sqrt{\frac{2n+1}{4\pi}\frac{(n-m)!}{(n+m)!}}P_n^m(\cos\theta)e^{im\phi}$, where $\theta$ is colatitude, $\phi$ is azimuth, and $P_n^m$ is the associated Legendre function.
````

## 3. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|8916bd16-dbad-5696-87d2-ac7d7eb4e660.local at=17efe8e4-cb89-5128-9528-308d98f0a88f] Mean-square expansion in spherical Dirichlet eigenfunctions inside a ball
> Let $a>0$. Use spherical coordinates with colatitude $\theta$, azimuth $\phi$, and volume measure $dV=r^2\sin\theta\,dr\,d\theta\,d\phi$. Write $Y_{n,m}$ for the standard unit-sphere orthonormal complex spherical harmonics and $j_n$ for the spherical Bessel function of the first kind. Let $\alpha_{n+1/2,j}$ be the $j$th positive zero of the ordinary Bessel function $J_{n+1/2}$, and set $\lambda_{n,j}=\alpha_{n+1/2,j}/a$ and
> $$
> \Psi_{jnm}(r,\theta,\phi)=j_n(\lambda_{n,j}r)Y_{n,m}(\theta,\phi),
> \qquad j\ge1,\ n\ge0,\ -n\le m\le n.
> $$
>
> For every $f\in L^2(\{r<a\},dV)$,
> $$
> f=\sum_{j=1}^{\infty}\sum_{n=0}^{\infty}\sum_{m=-n}^{n}A_{jnm}\Psi_{jnm},
> \qquad
> A_{jnm}=\frac{2}{a^3j_{n+1}(\alpha_{n+1/2,j})^2}\int_{r<a}f\overline{\Psi_{jnm}}\,dV,
> $$
> with convergence in the $L^2$ norm. This statement does not by itself guarantee pointwise convergence.
````
### After

````text
> [!theorem|8916bd16-dbad-5696-87d2-ac7d7eb4e660.local at=17efe8e4-cb89-5128-9528-308d98f0a88f] Series Expansions of Functions Defined in a Ball
> Let $f(r, \theta, \phi)$ be a square integrable function, defined for $0<r<a, 0<\theta< \pi, 0<\phi<2 \pi$, and $2 \pi$-periodic in $\phi$. Then we have
>
> $$
> f(r, \theta, \phi)=\sum_{j=1}^{\infty} \sum_{n=0}^{\infty} \sum_{m=-n}^{n} A_{j n m} j_{n}\left(\lambda_{n, j} r\right) Y_{n, m}(\theta, \phi),
> $$
>
> where
>
> $$
> A_{j n m}=\frac{2}{a^{3} j_{n+1}^{2}\left(\alpha_{n+\frac{1}{2}, j}\right)}
> $$
> $\quad \times \int_{0}^{a} \int_{0}^{2 \pi} \int_{0}^{\pi} f(r, \theta, \phi) j_{n}\left(\lambda_{n, j} r\right) \bar{Y}_{n, m}(\theta, \phi) r^{2} \sin \theta d \theta d \phi d r
> $$
>
> Let $a>0$, let $j_n$ be the spherical Bessel function of the first kind, and set $\lambda_{n,j}=\alpha_{n+1/2,j}/a$, where $\alpha_{n+1/2,j}$ is the $j$th positive zero of $J_{n+1/2}$. Here $Y_{n,m}(\theta,\phi)=\sqrt{\frac{2n+1}{4\pi}\frac{(n-m)!}{(n+m)!}}P_n^m(\cos\theta)e^{im\phi}$, where $\theta$ is colatitude, $\phi$ is azimuth, and $P_n^m$ is the associated Legendre function. The series converges in mean square with respect to volume measure.
````

## 4. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|8342a5a1-aa39-5e98-a879-b986f22aa73e.local at=60829fdd-9adc-5374-bc5a-69b98ee6c344] Poisson–Dirichlet solution in a ball by harmonic lifting and eigenfunction expansion
> Let $a>0$. Use spherical coordinates with colatitude $\theta$, azimuth $\phi$, and volume measure $dV=r^2\sin\theta\,dr\,d\theta\,d\phi$. Write $Y_{n,m}$ for the standard unit-sphere orthonormal complex spherical harmonics and $j_n$ for the spherical Bessel function of the first kind. Let $\alpha_{n+1/2,j}$ be the $j$th positive zero of the ordinary Bessel function $J_{n+1/2}$, and set $\lambda_{n,j}=\alpha_{n+1/2,j}/a$ and
> $$
> \Psi_{jnm}(r,\theta,\phi)=j_n(\lambda_{n,j}r)Y_{n,m}(\theta,\phi),
> \qquad j\ge1,\ n\ge0,\ -n\le m\le n.
> $$
>
> Consider $\Delta u=f$ in $r<a$, with $u=g$ at $r=a$. For $f\in L^2$ and continuous boundary data $g$, let $v$ be the harmonic extension of $g$. Set
> $$
> F_{jnm}=\frac{\int_{r<a}f\overline{\Psi_{jnm}}\,dV}{\int_{r<a}|\Psi_{jnm}|^2\,dV}.
> $$
> Then the solution is
> $$
> u=v-\sum_{j=1}^{\infty}\sum_{n=0}^{\infty}\sum_{m=-n}^{n}\frac{F_{jnm}}{\lambda_{n,j}^2}\Psi_{jnm}.
> $$
> The sum gives the weak zero-Dirichlet correction; smooth data yield the corresponding classical solution. The harmonic term $v$ supplies the prescribed boundary values.
````
### After

````text
> [!theorem|8342a5a1-aa39-5e98-a879-b986f22aa73e.local at=60829fdd-9adc-5374-bc5a-69b98ee6c344] Poisson Problem in a Ball
> The solution of the Poisson problem $\nabla^2u=f$ in $r<a$, $u(a,\theta,\phi)=g(\theta,\phi)$ with smooth data is
>
> $$
> u(r, \theta, \phi)=u_{1}(r, \theta, \phi)+u_{2}(r, \theta, \phi)
> $$
>
> where $u_{1}$ is the solution of the Poisson problem with zero boundary data, and $u_{2}$ is the solution of the Dirichlet problem inside the ball of radius $a$ with boundary condition $u_2(a,\theta,\phi)=g(\theta,\phi)$. The function $u_1$ is given by
> $$
> u_1=-\sum_{j=1}^{\infty}\sum_{n=0}^{\infty}\sum_{m=-n}^{n}\frac{A_{jnm}}{\lambda_{n,j}^2}j_n(\lambda_{n,j}r)Y_{n,m}(\theta,\phi),
> $$
> where
> $$
> A_{jnm}=\frac{2}{a^3j_{n+1}^2(\alpha_{n+1/2,j})}\int_0^a\int_0^{2\pi}\int_0^\pi f(r,\theta,\phi)j_n(\lambda_{n,j}r)\overline{Y_{n,m}(\theta,\phi)}r^2\sin\theta\,d\theta\,d\phi\,dr.
> $$
> Let $a>0$, let $j_n$ be the spherical Bessel function of the first kind, and set $\lambda_{n,j}=\alpha_{n+1/2,j}/a$, where $\alpha_{n+1/2,j}$ is the $j$th positive zero of $J_{n+1/2}$. Here $Y_{n,m}(\theta,\phi)=\sqrt{\frac{2n+1}{4\pi}\frac{(n-m)!}{(n+m)!}}P_n^m(\cos\theta)e^{im\phi}$, where $\theta$ is colatitude, $\phi$ is azimuth, and $P_n^m$ is the associated Legendre function.
````

## 5. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|34973adc-a87d-5d10-8d23-6589cf30567c.local at=b867b412-21bd-5e92-924e-4f5d556c8059] Zero-Dirichlet wave evolution in a ball by spherical eigenmodes
> Let $a>0$. Use spherical coordinates with colatitude $\theta$, azimuth $\phi$, and volume measure $dV=r^2\sin\theta\,dr\,d\theta\,d\phi$. Write $Y_{n,m}$ for the standard unit-sphere orthonormal complex spherical harmonics and $j_n$ for the spherical Bessel function of the first kind. Let $\alpha_{n+1/2,j}$ be the $j$th positive zero of the ordinary Bessel function $J_{n+1/2}$, and set $\lambda_{n,j}=\alpha_{n+1/2,j}/a$ and
> $$
> \Psi_{jnm}(r,\theta,\phi)=j_n(\lambda_{n,j}r)Y_{n,m}(\theta,\phi),
> \qquad j\ge1,\ n\ge0,\ -n\le m\le n.
> $$
>
> Let $c>0$. For $u_{tt}=c^2\Delta u$ in $r<a$, zero boundary displacement at $r=a$, and initial data $u(\cdot,0)=f$, $u_t(\cdot,0)=g$, define
> $$
> F_{jnm}=\frac{\int_{r<a}f\overline{\Psi_{jnm}}\,dV}{\int_{r<a}|\Psi_{jnm}|^2\,dV},\qquad
> G_{jnm}=\frac{\int_{r<a}g\overline{\Psi_{jnm}}\,dV}{\int_{r<a}|\Psi_{jnm}|^2\,dV}.
> $$
> The modal solution is
> $$
> u(r,\theta,\phi,t)=\sum_{j=1}^{\infty}\sum_{n=0}^{\infty}\sum_{m=-n}^{n}\Psi_{jnm}(r,\theta,\phi)
> \left[F_{jnm}\cos(c\lambda_{n,j}t)+\frac{G_{jnm}}{c\lambda_{n,j}}\sin(c\lambda_{n,j}t)\right].
> $$
> For $f\in H_0^1$ and $g\in L^2$ this is the energy solution; smooth compatible data give a classical solution. Here $H_0^1$ denotes square-integrable functions with square-integrable first derivatives and zero boundary trace.
````
### After

````text
> [!theorem|34973adc-a87d-5d10-8d23-6589cf30567c.local at=b867b412-21bd-5e92-924e-4f5d556c8059] Wave Equation in a Ball
> The solution of wave boundary value problem $u_{tt}=c^2\nabla^2u$ in $r<a$, $u(a,\theta,\phi,t)=0$, $u(\cdot,0)=f$, $u_t(\cdot,0)=g$, for $c>0$ and smooth compatible data, is
>
> $$
> \begin{gathered}
> u(r, \theta, \phi, t)=\sum_{j=1}^{\infty} \sum_{n=0}^{\infty} \sum_{m=-n}^{n} j_{n}\left(\lambda_{n, j} r\right) Y_{n, m}(\theta, \phi) \\
> \times\left(C_{j n m} \cos c \lambda_{n, j} t+D_{j n m} \sin c \lambda_{n, j} t\right)
> \end{gathered}
> $$
>
> where
>
> $$
> \begin{array}{r}
> C_{j n m}=\frac{2}{a^{3} j_{n+1}^{2}\left(\alpha_{n+\frac{1}{2}, j}\right)} \int_{0}^{a} \int_{0}^{2 \pi} \int_{0}^{\pi} f(r, \theta, \phi) j_{n}\left(\lambda_{n, j} r\right) \\
> \times \bar{Y}_{n, m}(\theta, \phi) r^{2} \sin \theta d \theta d \phi d r
> \end{array}
> $$
>
> and
>
> $$
> \begin{array}{r}
> D_{j n m}=\frac{2}{c \lambda_{n j} a^{3} j_{n+1}^{2}\left(\alpha_{n+\frac{1}{2}, j}\right)} \int_{0}^{a} \int_{0}^{2 \pi} \int_{0}^{\pi} g(r, \theta, \phi) j_{n}\left(\lambda_{n, j} r\right) \\
> \times \bar{Y}_{n, m}(\theta, \phi) r^{2} \sin \theta d \theta d \phi d r
> \end{array}
> $$
>
> Let $a>0$, let $j_n$ be the spherical Bessel function of the first kind, and set $\lambda_{n,j}=\alpha_{n+1/2,j}/a$, where $\alpha_{n+1/2,j}$ is the $j$th positive zero of $J_{n+1/2}$. Here $Y_{n,m}(\theta,\phi)=\sqrt{\frac{2n+1}{4\pi}\frac{(n-m)!}{(n+m)!}}P_n^m(\cos\theta)e^{im\phi}$, where $\theta$ is colatitude, $\phi$ is azimuth, and $P_n^m$ is the associated Legendre function.
````

## 6. Restore source wording; retain only the actual correction.

### Before

````text
Our notation anticipates the spherical harmonics in the angular factor $Y$.
````
### After

````text
Our notation already suggests that the solution in $Y$ will involve spherical harmonics.
````

## Additional source comparison

## 1. Join the two OCR fragments of the coefficient formula into one display.

### Before

````text
> $$
> $\quad \times
````
### After

````text
> \times
````

## Source-to-current comparison

Source: /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 13 Partial Differential Equations in Spherical Coordinates/13.4 The Helmholtz Equation with Applications to the Poisson, Heat, and Wave Equations.md

This exact comparison preserves the full change evidence, including formatting, OCR corrections, restored source wording, and required standalone context. The entries above explain the recovery edits. The comparison is not a claim that every difference is a correction; component serialization, callout wrapping, and printed labels outside callouts are formatting.

`````diff
--- /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 13 Partial Differential Equations in Spherical Coordinates/13.4 The Helmholtz Equation with Applications to the Poisson, Heat, and Wave Equations.md
+++ /Users/gradyclopton/ObsidianVaults/complex_analysis/Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 13 Partial Differential Equations in Spherical Coordinates/13.4 The Helmholtz Equation with Applications to the Poisson, Heat, and Wave Equations.md
@@ -1,6 +1,7 @@
+
 ### 13.4 The Helmholtz Equation with Applications to the Poisson, Heat, and Wave Equations
 
-In this section we complete our treatment of problems in spherical coordinates by considering the Helmholtz equation and boundary value problems involving the heat, wave, and Poisson equations. We will start by solving an eigenvalue problem involving the Helmholtz equation. The remaining boundary value problems will be solved using the eigenfunction expansions method. This was the approach that we took in Sections 3.9 and 4.6, where we treated similar problems in Cartesian and polar coordinates.
+In this section we complete our treatment of problems in spherical coordinates by considering the Helmholtz equation and boundary value problems involving the heat, wave, and Poisson equations. We will start by solving an eigenvalue problem involving the Helmholtz equation. The remaining boundary value problems will be solved using the eigenfunction expansions method. This was the approach that we took in Sections 11.9 and 12.6, where we treated similar problems in Cartesian and polar coordinates.
 
 ## The Helmholtz Equation in a Ball
 
@@ -13,11 +14,13 @@
 \end{gathered}
 $$
 
+*Printed equation labels: (1) Helmholtz eigenvalue equation; (2) zero boundary value.*
+
 where $0<r<a, 0<\theta<\pi, 0<\phi<2 \pi, k$ is a nonnegative constant, and $\nabla^{2} \Psi$ denotes the Laplacian of $\Psi$ in spherical coordinates. Furthermore, we require that $\Psi$ be bounded and $2 \pi$-periodic in $\phi$. Equation (1) is the Helmholtz equation in spherical coordinates. The eigenvalue problem (1)--(2) is homogeneous and can be solved using the separation of variables method. To this end, let
-Our notation already suggests that the solution in $Y$ will in-
 
 $$
 \Psi(r, \theta, \phi)=R(r) Y(\theta, \phi)
+\tag{3}
 $$
 
 (Note that, unlike previous instances where we used the separation of variables method, here we do not separate the variables $\theta$ and $\phi$. The reason will become apparent when we derive the equation for $Y$.) To separate variables in (1), we use (3) and the explicit form of the Laplacian in spherical
@@ -25,24 +28,28 @@
 
 $$
 r^{2} R^{\prime \prime}+2 r R^{\prime}+\left(k r^{2}-\mu\right) R=0, \quad R(a)=0,
+\tag{4}
 $$
 
 and
 
 $$
 \frac{\partial^{2} Y}{\partial \theta^{2}}+\cot \theta \frac{\partial Y}{\partial \theta}+\csc ^{2} \theta \frac{\partial^{2} Y}{\partial \phi^{2}}+\mu Y=0
+\tag{5}
 $$
 
 where $\mu$ is the separation constant and $Y$ is $2 \pi$-periodic in $\phi$. (The details of the separation of the variables are left to Exercise 1.) Appealing to Theorem 4, Section 13.3, we see that (5) is the differential equation for the spherical harmonics. It has nontrivial bounded solutions that are $2 \pi$-periodic in $\phi$ when
 
 $$
 \mu=n(n+1), \quad n=0,1,2, \ldots
+\tag{6}
 $$
 
 For each $\mu=n(n+1)$, we have $2 n+1$ solutions, the spherical harmonics
 
 $$
 Y_{n, m}(\theta, \phi) \quad m=-n,-n+1, \ldots, 0, \ldots, n-1, n .
+\tag{7}
 $$
 
 Putting the values of $\mu$ from (6) into (4), and letting
@@ -55,75 +62,91 @@
 
 $$
 r^{2} R^{\prime \prime}+2 r R^{\prime}+\left(\lambda^{2} r^{2}-n(n+1)\right) R=0, \quad R(a)=0
-$$
-
-(see Example 2, Section 4.8). For each $n$, we have infinitely many nontrivial solutions
+\tag{8}
+$$
+
+(see Example 2, Section 12.8). For each $n$, we have infinitely many nontrivial solutions
 
 $$
 R_{n, j}(r)=j_{n}\left(\lambda_{n, j} r\right), \quad n=0,1,2, \ldots, j=1,2, \ldots,
+\tag{9}
 $$
 
 where
 
 $$
 \lambda=\lambda_{n, j}=\frac{\alpha_{n+1 / 2, j}}{a},
-$$
-
-THEOREM 1 HELMHOLTZ EQUATION IN A BALL
-
-THEOREM 2 ORTHOGONALITY OF SOLUTIONS OF THE HELMHOLTZ EQUATION
+\tag{10}
+$$
+
 $\alpha_{n+1 / 2, j}$ denotes the $j$ th positive zero of the Bessel function $J_{n+\frac{1}{2}}$ and $j_{n}$ is the spherical Bessel function of the first kind, which is defined in terms of the Bessel function by
 
 $$
 j_{n}(r)=\left(\frac{\pi}{2 r}\right)^{1 / 2} J_{n+\frac{1}{2}}(r) .
-$$
+\tag{11}
+$$
+
+Our notation already suggests that the solution in $Y$ will involve spherical harmonics.
 
 The complete solution of (1) and (2) can now be stated in terms of products of spherical harmonics and spherical Bessel functions as follows.
 
-The eigenvalue problem (1)-(2) has eigenvalues $k=\lambda^{2}$, where $\lambda=\lambda_{n, j}$ is as in (10). To each eigenvalue correspond $2 n+1$ eigenfunctions
-
-$$
-\Psi_{j n m}(r, \theta, \phi)=j_{n}\left(\lambda_{n, j} r\right) Y_{n, m}(\theta, \phi),
-$$
-
-where $|m| \leq n$.
+> [!theorem|efc5ac01-2469-5568-8a2b-ec8c4e0b0503.local at=6e849eda-9451-5496-91cc-c8f567c7d2f9] Helmholtz Equation in a Ball
+> The eigenvalue problem $\nabla^2u+ku=0$ in $r<a$, regular at the origin and satisfying $u=0$ at $r=a$, has eigenvalues $k=\lambda^{2}$, where $\lambda=\lambda_{n, j}$ is defined below. To each eigenvalue correspond $2 n+1$ eigenfunctions
+>
+> $$
+> \Psi_{j n m}(r, \theta, \phi)=j_{n}\left(\lambda_{n, j} r\right) Y_{n, m}(\theta, \phi),
+> $$
+>
+> where $|m| \leq n$.
+>
+> Let $a>0$, let $j_n$ be the spherical Bessel function of the first kind, and set $\lambda_{n,j}=\alpha_{n+1/2,j}/a$, where $\alpha_{n+1/2,j}$ is the $j$th positive zero of $J_{n+1/2}$. Here $Y_{n,m}(\theta,\phi)=\sqrt{\frac{2n+1}{4\pi}\frac{(n-m)!}{(n+m)!}}P_n^m(\cos\theta)e^{im\phi}$, where $\theta$ is colatitude, $\phi$ is azimuth, and $P_n^m$ is the associated Legendre function.
+
+*Printed equation label: (12) spherical eigenmodes.*
+
 The eigenfunctions (12) enjoy orthogonality relations that will be used to expand functions defined inside the ball. The following results are straightforward to check, using the orthogonality of the spherical harmonics and spherical Bessel functions. (See Exercise 3.)
 
-For $j=1,2, \ldots, n=0,1,2, \ldots$, and $|m| \leq n$, we have
-
-$$
-\int_{0}^{a} \int_{0}^{2 \pi} \int_{0}^{\pi} j_{n}\left(\lambda_{n, j} r\right) Y_{n, m}(\theta, \phi) j_{n^{\prime}}\left(\lambda_{n^{\prime}, j^{\prime}} r\right) \bar{Y}_{n^{\prime}, m^{\prime}}(\theta, \phi) r^{2} \sin \theta d \theta d \phi d r=0
-$$
-
-for $(j, n, m) \neq\left(j^{\prime}, n^{\prime}, m^{\prime}\right)$, and
-
-$$
-\int_{0}^{a} \int_{0}^{2 \pi} \int_{0}^{\pi} j_{n}^{2}\left(\lambda_{n, j} r\right)\left|Y_{n, m}(\theta, \phi)\right|^{2} r^{2} \sin \theta d \theta d \phi d r=\frac{a^{3}}{2} j_{n+1}^{2}\left(\alpha_{n+\frac{1}{2}, j}\right)
-$$
-
-where $\alpha_{n+\frac{1}{2}, j}$ is the $j$ th positive zero of $J_{n+\frac{1}{2}}$.
+> [!theorem|b5a977f6-80ae-5e5d-893a-641f2e6133da.local at=d53f3db2-ed96-5b4d-a721-171b5604e268] Orthogonality of Solutions of the Helmholtz Equation
+> For $j=1,2, \ldots, n=0,1,2, \ldots$, and $|m| \leq n$, we have
+>
+> $$
+> \int_{0}^{a} \int_{0}^{2 \pi} \int_{0}^{\pi} j_{n}\left(\lambda_{n, j} r\right) Y_{n, m}(\theta, \phi) j_{n^{\prime}}\left(\lambda_{n^{\prime}, j^{\prime}} r\right) \bar{Y}_{n^{\prime}, m^{\prime}}(\theta, \phi) r^{2} \sin \theta d \theta d \phi d r=0
+> $$
+>
+> for $(j, n, m) \neq\left(j^{\prime}, n^{\prime}, m^{\prime}\right)$, and
+>
+> $$
+> \int_{0}^{a} \int_{0}^{2 \pi} \int_{0}^{\pi} j_{n}^{2}\left(\lambda_{n, j} r\right)\left|Y_{n, m}(\theta, \phi)\right|^{2} r^{2} \sin \theta d \theta d \phi d r=\frac{a^{3}}{2} j_{n+1}^{2}\left(\alpha_{n+\frac{1}{2}, j}\right)
+> $$
+>
+> where $\alpha_{n+\frac{1}{2}, j}$ is the $j$ th positive zero of $J_{n+\frac{1}{2}}$.
+>
+> Let $a>0$, let $j_n$ be the spherical Bessel function of the first kind, and set $\lambda_{n,j}=\alpha_{n+1/2,j}/a$, where $\alpha_{n+1/2,j}$ is the $j$th positive zero of $J_{n+1/2}$. Here $Y_{n,m}(\theta,\phi)=\sqrt{\frac{2n+1}{4\pi}\frac{(n-m)!}{(n+m)!}}P_n^m(\cos\theta)e^{im\phi}$, where $\theta$ is colatitude, $\phi$ is azimuth, and $P_n^m$ is the associated Legendre function.
+
+*Printed equation labels: (13) orthogonality of distinct modes; (14) squared norm of a mode.*
+
 Note that the integrals in Theorem 2 are with respect to the element of volume in spherical coordinates, $r^{2} \sin \theta d \theta d \phi d r$. Our next result, Theorem 3, states that functions defined in a ball can be expanded in series in terms of the eigenfunctions in Theorem 1. The coefficients in these series are defined by integrals using the element of volume in spherical coordinates. As you would expect, these series have to include all the eigenfunctions; thus three indices of summation are required.
 
-Theorems 2 and 3 of this section are the higher-dimensional analogues of Theorems 1 and 2 of Section 4.6. In both situations, the eigenfunctions of the Helmholtz equation are used to expand functions that are defined on the disk (in Section 4.6) and in the ball (in Section 13.4).
-
-THEOREM 3 SERIES EXPANSIONS OF FUNCTIONS
-DEFINED IN A BALL
-
-Let $f(r, \theta, \phi)$ be a square integrable function, defined for $0<r<a, 0<\theta< \pi, 0<\phi<2 \pi$, and $2 \pi$-periodic in $\phi$. Then we have
-
-$$
-f(r, \theta, \phi)=\sum_{j=1}^{\infty} \sum_{n=0}^{\infty} \sum_{m=-n}^{n} A_{j n m} j_{n}\left(\lambda_{n, j} r\right) Y_{n, m}(\theta, \phi),
-$$
-
-where
-
-$$
-A_{j n m}=\frac{2}{a^{3} j_{n+1}^{2}\left(\alpha_{n+\frac{1}{2}, j}\right)}
-$$
-
-(16) $\quad \times \int_{0}^{a} \int_{0}^{2 \pi} \int_{0}^{\pi} f(r, \theta, \phi) j_{n}\left(\lambda_{n, j} r\right) \bar{Y}_{n, m}(\theta, \phi) r^{2} \sin \theta d \theta d \phi d r$.
-
-We are now ready to tackle boundary value problems using the eigenfunction expansions method. For motivation, you should review the lowerdimensional problems that are treated in Sections 3.9 and 4.6.
+Theorems 2 and 3 of this section are the higher-dimensional analogues of Theorems 1 and 2 of Section 12.6. In both situations, the eigenfunctions of the Helmholtz equation are used to expand functions that are defined on the disk (in Section 12.6) and in the ball (in Section 13.4).
+
+> [!theorem|8916bd16-dbad-5696-87d2-ac7d7eb4e660.local at=17efe8e4-cb89-5128-9528-308d98f0a88f] Series Expansions of Functions Defined in a Ball
+> Let $f(r, \theta, \phi)$ be a square integrable function, defined for $0<r<a, 0<\theta< \pi, 0<\phi<2 \pi$, and $2 \pi$-periodic in $\phi$. Then we have
+>
+> $$
+> f(r, \theta, \phi)=\sum_{j=1}^{\infty} \sum_{n=0}^{\infty} \sum_{m=-n}^{n} A_{j n m} j_{n}\left(\lambda_{n, j} r\right) Y_{n, m}(\theta, \phi),
+> $$
+>
+> where
+>
+> $$
+> A_{j n m}=\frac{2}{a^{3} j_{n+1}^{2}\left(\alpha_{n+\frac{1}{2}, j}\right)}
+> \times \int_{0}^{a} \int_{0}^{2 \pi} \int_{0}^{\pi} f(r, \theta, \phi) j_{n}\left(\lambda_{n, j} r\right) \bar{Y}_{n, m}(\theta, \phi) r^{2} \sin \theta d \theta d \phi d r
+> $$
+>
+> Let $a>0$, let $j_n$ be the spherical Bessel function of the first kind, and set $\lambda_{n,j}=\alpha_{n+1/2,j}/a$, where $\alpha_{n+1/2,j}$ is the $j$th positive zero of $J_{n+1/2}$. Here $Y_{n,m}(\theta,\phi)=\sqrt{\frac{2n+1}{4\pi}\frac{(n-m)!}{(n+m)!}}P_n^m(\cos\theta)e^{im\phi}$, where $\theta$ is colatitude, $\phi$ is azimuth, and $P_n^m$ is the associated Legendre function. The series converges in mean square with respect to volume measure.
+
+*Printed equation labels: (15) eigenfunction expansion; (16) coefficients $A_{jnm}$.*
+
+We are now ready to tackle boundary value problems using the eigenfunction expansions method. For motivation, you should review the lower-dimensional problems that are treated in Sections 11.9 and 12.6.
 
 ## Poisson's Equation in a Ball
 
@@ -131,36 +154,46 @@
 
 $$
 \nabla^{2} u(r, \theta, \phi)=f(r, \theta, \phi)
+\tag{17}
 $$
 
 where $0<r<a, 0<\theta<\pi, 0<\phi<2 \pi$, along with the boundary condition
 
 $$
 u(a, \theta, \phi)=g(\theta, \phi)
-$$
-
-![](./images/122e2a0e-ba5b-4934-9af1-dcd4ea360903-26_490_521_1440_141.jpg)
-General Poisson problem
-
-![](./images/122e2a0e-ba5b-4934-9af1-dcd4ea360903-26_489_528_1442_680.jpg)
-Poisson problem with zero boundary data
-
-![](./images/122e2a0e-ba5b-4934-9af1-dcd4ea360903-26_493_473_1442_1241.jpg)
-General Dirichlet problem
-
-Figure 1 Decomposition of a general Poisson problem.
-
-As in the lower-dimensional cases, the first step is to reduce to two subprob-
-lems: a Dirichlet problem with boundary data given by (18), and a Poisson problem with zero boundary data (see Figure 1). For the Dirichlet problem, you are referred to the previous section. Thus, it remains to solve (17) with the homogeneous boundary condition
+\tag{18}
+$$
+
+```scientific-figure
+id: 136191a1-125e-4bfb-a77c-5fc60062323b
+numbered: false
+title: ""
+caption: "Figure 1 Decomposition into a Poisson problem with zero boundary data and a harmonic Dirichlet problem. Panels from left to right: original Poisson problem; zero-boundary Poisson problem; Dirichlet problem."
+captionVisible: true
+captionPosition: below
+columns: 3
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 13 Partial Differential Equations in Spherical Coordinates/images/122e2a0e-ba5b-4934-9af1-dcd4ea360903-26_490_521_1440_141.jpg
+    caption: ""
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 13 Partial Differential Equations in Spherical Coordinates/images/122e2a0e-ba5b-4934-9af1-dcd4ea360903-26_489_528_1442_680.jpg
+    caption: ""
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 13 Partial Differential Equations in Spherical Coordinates/images/122e2a0e-ba5b-4934-9af1-dcd4ea360903-26_493_473_1442_1241.jpg
+    caption: ""
+```
+
+
+As in the lower-dimensional cases, the first step is to reduce to two subproblems: a Dirichlet problem with boundary data given by (18), and a Poisson problem with zero boundary data (see Figure 1). For the Dirichlet problem, you are referred to the previous section. Thus, it remains to solve (17) with the homogeneous boundary condition
 
 $$
 u(a, \theta, \phi)=0
+\tag{19}
 $$
 
 In solving (17) and (19), we will use the method of eigenfunction expansions. Accordingly, we start by assuming that the solution has a series expansion in terms of the eigenfunctions of the Helmholtz problem (1) and (2). Hence,
 
 $$
 u(r, \theta, \phi)=\sum_{j=1}^{\infty} \sum_{n=0}^{\infty} \sum_{m=-n}^{n} B_{j n m} j_{n}\left(\lambda_{n, j} r\right) Y_{n, m}(\theta, \phi)
+\tag{20}
 $$
 
 To determine $B_{j n m}$, we plug the triple series into (17), use the fact that each term satisfies (1) with $k=\lambda_{n, j}^{2}$, and get
@@ -173,19 +206,27 @@
 
 $$
 B_{j n m}=\frac{-1}{\lambda_{n, j}^{2}} A_{j n m}
+\tag{21}
 $$
 
 where $A_{\text {jnm }}$ is given by (16). This completely determines the solution of the Poisson problem. We summarize our findings as follows.
 
-THEOREM 4 POISSON PROBLEM IN A BALL
-
-The solution of the Poisson problem (17)-(18) is
-
-$$
-u(r, \theta, \phi)=u_{1}(r, \theta, \phi)+u_{2}(r, \theta, \phi)
-$$
-
-where $u_{1}$ is the solution of the Poisson problem with zero boundary data, and $u_{2}$ is the solution of the Dirichlet problem inside the ball of radius $a$ with boundary condition (18). The function $u_{1}$ is given by (20) and (21), and the function $u_{2}$ is given by Theorem 3, Section 13.3. (The coefficients in the series solution (11), Section 13.3, are the spherical harmonics coefficients of the boundary function g .)
+> [!theorem|8342a5a1-aa39-5e98-a879-b986f22aa73e.local at=60829fdd-9adc-5374-bc5a-69b98ee6c344] Poisson Problem in a Ball
+> The solution of the Poisson problem $\nabla^2u=f$ in $r<a$, $u(a,\theta,\phi)=g(\theta,\phi)$ with smooth data is
+>
+> $$
+> u(r, \theta, \phi)=u_{1}(r, \theta, \phi)+u_{2}(r, \theta, \phi)
+> $$
+>
+> where $u_{1}$ is the solution of the Poisson problem with zero boundary data, and $u_{2}$ is the solution of the Dirichlet problem inside the ball of radius $a$ with boundary condition $u_2(a,\theta,\phi)=g(\theta,\phi)$. The function $u_1$ is given by
+> $$
+> u_1=-\sum_{j=1}^{\infty}\sum_{n=0}^{\infty}\sum_{m=-n}^{n}\frac{A_{jnm}}{\lambda_{n,j}^2}j_n(\lambda_{n,j}r)Y_{n,m}(\theta,\phi),
+> $$
+> where
+> $$
+> A_{jnm}=\frac{2}{a^3j_{n+1}^2(\alpha_{n+1/2,j})}\int_0^a\int_0^{2\pi}\int_0^\pi f(r,\theta,\phi)j_n(\lambda_{n,j}r)\overline{Y_{n,m}(\theta,\phi)}r^2\sin\theta\,d\theta\,d\phi\,dr.
+> $$
+> Let $a>0$, let $j_n$ be the spherical Bessel function of the first kind, and set $\lambda_{n,j}=\alpha_{n+1/2,j}/a$, where $\alpha_{n+1/2,j}$ is the $j$th positive zero of $J_{n+1/2}$. Here $Y_{n,m}(\theta,\phi)=\sqrt{\frac{2n+1}{4\pi}\frac{(n-m)!}{(n+m)!}}P_n^m(\cos\theta)e^{im\phi}$, where $\theta$ is colatitude, $\phi$ is azimuth, and $P_n^m$ is the associated Legendre function.
 
 ## A Nonhomogeneous Heat Problem
 
@@ -195,36 +236,42 @@
 
 $$
 \frac{\partial u}{\partial t}=c^{2}\left\{\frac{\partial^{2} u}{\partial r^{2}}+\frac{2}{r} \frac{\partial u}{\partial r}+\frac{1}{r^{2}}\left(\frac{\partial^{2} u}{\partial \theta^{2}}+\cot \theta \frac{\partial u}{\partial \theta}+\csc ^{2} \theta \frac{\partial^{2} u}{\partial \phi^{2}}\right)\right\}+q(r, \theta, \phi),
+\tag{22}
 $$
 
 where $0<r<a, 0<\theta<\pi, 0<\phi<2 \pi, t>0$, with boundary condition
 
 $$
 u(a, \theta, \phi, t)=0
+\tag{23}
 $$
 
 and initial condition
 
 $$
 u(r, \theta, \phi, 0)=f(r, \theta, \phi)
+\tag{24}
 $$
 
 We solve this problem using the method of eigenfunction expansions, and hence start by assuming that $u$ has an expansion in terms of the eigenfunctions of the Helmholtz problem (1)-(2). Thus
 
 $$
 u(r, \theta, \phi, t)=\sum_{j=1}^{\infty} \sum_{n=0}^{\infty} \sum_{m=-n}^{n} B_{j n m}(t) j_{n}\left(\lambda_{n, j} r\right) Y_{n, m}(\theta, \phi)
+\tag{25}
 $$
 
 where the coefficients $B_{j n m}(t)$ are functions of $t$, and $\lambda_{n, j}=\frac{\alpha_{n+1 / 2, j}}{a}$. We now expand $f$ and $q$ using Theorem 3 and obtain
 
 $$
 f(r, \theta, \phi)=\sum_{j=1}^{\infty} \sum_{n=0}^{\infty} \sum_{m=-n}^{n} f_{j n m} j_{n}\left(\lambda_{n, j} r\right) Y_{n, m}(\theta, \phi)
+\tag{26}
 $$
 
 and
 
 $$
 q(r, \theta, \phi)=\sum_{j=1}^{\infty} \sum_{n=0}^{\infty} \sum_{m=-n}^{n} q_{j n m} j_{n}\left(\lambda_{n, j} r\right) Y_{n, m}(\theta, \phi),
+\tag{27}
 $$
 
 where $f_{j n m}$ and $q_{j n m}$ are computed with the help of (16) by using $f$ and $q$, respectively. To complete the solution, we must determine the coefficients
@@ -241,18 +288,21 @@
 
 $$
 B_{j n m}^{\prime}(t)+\lambda_{n, j}^{2} c^{2} B_{j n m}(t)=q_{j n m} .
+\tag{28}
 $$
 
 The initial condition for this equation is obtained by using (24), (25), and (26), thus implying
 
 $$
 B_{j n m}(0)=f_{j n m}
+\tag{29}
 $$
 
 As you can check directly, the solution of the initial value problem (28)-(29) is
 
 $$
 B_{j n m}(t)=e^{-\lambda_{n, j}^{2} c^{2} t}\left(f_{j n m}-\frac{q_{j n m}}{c^{2} \lambda_{n, j}^{2}}\right)+\frac{q_{j n m}}{c^{2} \lambda_{n, j}^{2}}
+\tag{30}
 $$
 
 This determines the unknown coefficients in (25) and completes the solution of the heat problem. Note that the final answer involves the coefficients of the eigenfunction expansions of $f$ and $q$ and the familiar "heat kernel" $e^{-\lambda_{n, j}^{2} c^{2} t}$.
@@ -263,80 +313,139 @@
 
 $$
 \frac{\partial^{2} u}{\partial t^{2}}=c^{2}\left\{\frac{\partial^{2} u}{\partial r^{2}}+\frac{2}{r} \frac{\partial u}{\partial r}+\frac{1}{r^{2}}\left(\frac{\partial^{2} u}{\partial \theta^{2}}+\cot \theta \frac{\partial u}{\partial \theta}+\csc ^{2} \theta \frac{\partial^{2} u}{\partial \phi^{2}}\right)\right\}
+\tag{31}
 $$
 
 where $0<r<a, 0<\theta<\pi, 0<\phi<2 \pi, t>0$, with boundary condition
 
 $$
 u(a, \theta, \phi, t)=0
+\tag{32}
 $$
 
 and initial conditions
 
 $$
 u(r, \theta, \phi, 0)=f(r, \theta, \phi), \quad u_{t}(r, \theta, \phi, 0)=g(r, \theta, \phi)
-$$
-
-THEOREM 5 WAVE EQUATION IN A BALL
+\tag{33}
+$$
 
 To solve this problem, we use the eigenfunction expansions method and assume that the solution $u$ is a series in terms of the eigenfunctions of the Helmholtz problem (1)-(2). We obtain the following solution.
 
-The solution of wave boundary value problem (31)-(33) is
-
-$$
-\begin{gathered}
-u(r, \theta, \phi, t)=\sum_{j=1}^{\infty} \sum_{n=0}^{\infty} \sum_{m=-n}^{n} j_{n}\left(\lambda_{n, j} r\right) Y_{n, m}(\theta, \phi) \\
-\times\left(C_{j n m} \cos c \lambda_{n, j} t+D_{j n m} \sin c \lambda_{n, j} t\right)
-\end{gathered}
-$$
-
-where
-
-$$
-\begin{array}{r}
-C_{j n m}=\frac{2}{a^{3} j_{n+1}^{2}\left(\alpha_{n+\frac{1}{2}, j}\right)} \int_{0}^{a} \int_{0}^{2 \pi} \int_{0}^{\pi} f(r, \theta, \phi) j_{n}\left(\lambda_{n, j} r\right) \\
-\times \bar{Y}_{n, m}(\theta, \phi) r^{2} \sin \theta d \theta d \phi d r
-\end{array}
-$$
-
-and
-
-$$
-\begin{array}{r}
-D_{j n m}=\frac{2}{c \lambda_{n j} a^{3} j_{n+1}^{2}\left(\alpha_{n+\frac{1}{2}, j}\right)} \int_{0}^{a} \int_{0}^{2 \pi} \int_{0}^{\pi} g(r, \theta, \phi) j_{n}\left(\lambda_{n, j} r\right) \\
-\times \bar{Y}_{n, m}(\theta, \phi) r^{2} \sin \theta d \theta d \phi d r
-\end{array}
-$$
+> [!theorem|34973adc-a87d-5d10-8d23-6589cf30567c.local at=b867b412-21bd-5e92-924e-4f5d556c8059] Wave Equation in a Ball
+> The solution of wave boundary value problem $u_{tt}=c^2\nabla^2u$ in $r<a$, $u(a,\theta,\phi,t)=0$, $u(\cdot,0)=f$, $u_t(\cdot,0)=g$, for $c>0$ and smooth compatible data, is
+>
+> $$
+> \begin{gathered}
+> u(r, \theta, \phi, t)=\sum_{j=1}^{\infty} \sum_{n=0}^{\infty} \sum_{m=-n}^{n} j_{n}\left(\lambda_{n, j} r\right) Y_{n, m}(\theta, \phi) \\
+> \times\left(C_{j n m} \cos c \lambda_{n, j} t+D_{j n m} \sin c \lambda_{n, j} t\right)
+> \end{gathered}
+> $$
+>
+> where
+>
+> $$
+> \begin{array}{r}
+> C_{j n m}=\frac{2}{a^{3} j_{n+1}^{2}\left(\alpha_{n+\frac{1}{2}, j}\right)} \int_{0}^{a} \int_{0}^{2 \pi} \int_{0}^{\pi} f(r, \theta, \phi) j_{n}\left(\lambda_{n, j} r\right) \\
+> \times \bar{Y}_{n, m}(\theta, \phi) r^{2} \sin \theta d \theta d \phi d r
+> \end{array}
+> $$
+>
+> and
+>
+> $$
+> \begin{array}{r}
+> D_{j n m}=\frac{2}{c \lambda_{n j} a^{3} j_{n+1}^{2}\left(\alpha_{n+\frac{1}{2}, j}\right)} \int_{0}^{a} \int_{0}^{2 \pi} \int_{0}^{\pi} g(r, \theta, \phi) j_{n}\left(\lambda_{n, j} r\right) \\
+> \times \bar{Y}_{n, m}(\theta, \phi) r^{2} \sin \theta d \theta d \phi d r
+> \end{array}
+> $$
+>
+> Let $a>0$, let $j_n$ be the spherical Bessel function of the first kind, and set $\lambda_{n,j}=\alpha_{n+1/2,j}/a$, where $\alpha_{n+1/2,j}$ is the $j$th positive zero of $J_{n+1/2}$. Here $Y_{n,m}(\theta,\phi)=\sqrt{\frac{2n+1}{4\pi}\frac{(n-m)!}{(n+m)!}}P_n^m(\cos\theta)e^{im\phi}$, where $\theta$ is colatitude, $\phi$ is azimuth, and $P_n^m$ is the associated Legendre function.
+
+*Printed equation labels: (34) wave solution; (35) initial-displacement coefficients $C_{jnm}=F_{jnm}$; (36) initial-velocity coefficients $D_{jnm}=G_{jnm}/(c\lambda_{n,j})$.*
 
 The interesting details of the derivation are very similar to those of the heat equation and are left to the exercises.
 
-## Exercises 5.4
-
-1. Derive (4) and (5) from (1) and (2).
-2. Use the explicit formulas for the spherical Bessel functions and the spherical harmonics to verify (13) and (14) when $j=1, n=0,1$, and $m=-1,0,1$.
-3. (a) Use the orthogonality properties of the spherical Bessel functions (Exercise 45, Section 4.8) and the spherical harmonics (Section 13.3) to prove (13) and (14). (b) Use Theorem 2 to justify (16).
-4. What does Theorem 3 reduce to if $f$ depends only on $r$ ?
-5. Define a function inside the unit ball by $f(r)=1$ for $0<r<1$. Compute the series expansion (15) for $f$.
-6. Define a function inside the unit ball by $f(r)=1$ if $0<r<1 / 2$ and $f(r)=0$ if $1 / 2<r<1$. Compute the series expansion (15) for $f$.
-7. Define a function inside the unit ball by $f(r)=r^{2}$. Compute the series expansion (15) for $f$.
-8. Define a function inside the unit ball by $f(r, \phi)=r^{2} \phi$. Compute the series expansion (15) for $f$.
-9. Solve the Poisson problem (17), (19) inside the unit ball with $f=1$, and $g=0$.
-10. Solve the Poisson problem (17), (18) inside the unit ball with $f=1$ and $g=\frac{1}{2 \pi} \phi$.
-11. Derive (29), then solve (28)-(29) to get (30).
-12. What is the solution of the heat problem (22)-(24) if $q=0$ ?
-13. Project Problem: A problem with time-dependent heat source. Solve the heat problem (22)-(24) with a time-dependent heat source $q(r, \theta, \phi, t)$. [Hint: Modify the solution of (22)-(24) as follows. In (27), you should allow the coefficients $q_{j m n}$ to depend on $t$. In (28), the right side depends on $t$. Solve (28)-(29) as in Exercise 18(c), Section 3.9.]
-14. A nonhomogeneous heat problem. Solve the heat equation (22) subject to the initial condition (24), and the nonhomogeneous boundary condition $u(a, \theta, \phi, t)=g(\theta, \phi)$. [Hint: Decompose the problem into two subproblems. See, for example, Exercise 17, Section 4.4.]
-15. A heat problem with symmetry. A solid ball at $30^{\circ} \mathrm{C}$ with radius $a=1$ is placed in a refrigerator that maintains a constant temperature of $0^{\circ} \mathrm{C}$. (a) Take $c=1$ and determine the temperature $u(r, \theta, \phi, t)$ inside the ball.
-(b) The function
-
-$$
-\theta_{4}(u, q)=1+2 \sum_{n=1}^{\infty}(-1)^{n} q^{n^{2}} \cos 2 n u
-$$
-
-is called an elliptic theta function. This type of function is built into many computer systems. Express the temperature of the center in part (a) in terms of $\theta_{4}$, then plot the temperature for $t>0$.
-(c) Use your graph in (b) to determine how long it will take for the temperature at the center to drop to $10^{\circ} \mathrm{C}$.
-16. (a) Solve the heat problem in the ball of radius 1 with $c=1$, given that the surface temperature is kept at $0^{\circ}$ and that the initial temperature distribution is $f(r, \theta, \phi)=r^{2}$. Assume that there is no internal source of heat.
-(b) Plot the temperature of the center for $t>0$.
-17. (a) Solve the heat problem (22)-(24) inside the unit ball. Take $c=1, q= 20 r^{2}$, and $f(r, \theta, \phi)=100$.
-(b) Plot the temperature of the center for $t>0$.
-18. Project Problem: The wave equation in a ball. Derive (34)-(36).
+## Exercises 13.4
+
+
+> [!exercise|64856d28-5087-566c-9fcc-5e352f63d79e.local at=fad3811d-ea6e-59a2-9d57-75657553d1e6] Exercise 1
+> Derive (4) and (5) from (1) and (2).
+
+
+> [!exercise|853f56a1-fdb7-5dde-9048-4c174cb3c8a2.local at=d837cbf9-209f-57ee-b517-ef1323939bf1] Exercise 2
+> Use the explicit formulas for the spherical Bessel functions and the spherical harmonics to verify (13) and (14) when $j=1$, $n=0,1$, and the admissible orders $-n\le m\le n$.
+
+
+> [!exercise|a0951be1-27f9-57d1-beef-165dd4e769d0.local at=2cf00c39-4351-5ab2-8279-2960a79cd876] Exercise 3
+> (a) Use the orthogonality properties of the spherical Bessel functions (Exercise 45, Section 12.8) and the spherical harmonics (Section 13.3) to prove (13) and (14). (b) Use Theorem 2 to justify (16).
+
+
+> [!exercise|7f863a09-0d66-5b1d-abb4-0cd3afe0a195.local at=0cca9a5b-b1f1-5146-b5f3-c389a1d0d2e4] Exercise 4
+> What does Theorem 3 reduce to if $f$ depends only on $r$ ?
+
+
+> [!exercise|6ad84a32-3586-561f-8e4a-df26a6ad4198.local at=e1e270c3-6a5c-5a9e-bc84-eeefe5d08f94] Exercise 5
+> Define a function inside the unit ball by $f(r)=1$ for $0<r<1$. Compute the series expansion (15) for $f$.
+
+
+> [!exercise|4efb02ab-0301-520c-9f6b-a696ddc39157.local at=465bfd88-2a7b-56d0-ab41-051731754dcd] Exercise 6
+> Define a function inside the unit ball by $f(r)=1$ if $0<r<1 / 2$ and $f(r)=0$ if $1 / 2<r<1$. Compute the series expansion (15) for $f$.
+
+
+> [!exercise|b4c19f85-67ed-5e0f-b4cd-76e81032f394.local at=032f7fcb-1258-57ce-9fa5-90d9f6250459] Exercise 7
+> Define a function inside the unit ball by $f(r)=r^{2}$. Compute the series expansion (15) for $f$.
+
+
+> [!exercise|91d8bc62-bf6a-5f0a-8da6-e6f6cbdd22ea.local at=b9f5e08b-f228-5b5f-b945-7a1211af1047] Exercise 8
+> Define a function inside the unit ball by $f(r, \phi)=r^{2} \phi$. Compute the series expansion (15) for $f$.
+
+
+> [!exercise|1fa6c14b-6712-5d5e-b261-2cf74570e494.local at=f4fbf79a-3cc8-5197-9e62-2ddd10537937] Exercise 9
+> Solve the Poisson problem (17), (19) inside the unit ball with $f=1$, and $g=0$.
+
+
+> [!exercise|27f7abf6-0e37-5b01-9a1b-4255a1596771.local at=654b58f8-88f0-58a4-a8f4-717b526e4243] Exercise 10
+> Solve the Poisson problem (17), (18) inside the unit ball with $f=1$ and $g=\frac{1}{2 \pi} \phi$.
+
+
+> [!exercise|c1d48f7f-46c8-56c4-9aea-f30509696e15.local at=1f23c1fd-70e8-5808-98f5-7ed6ddac0afe] Exercise 11
+> Derive (29), then solve (28)-(29) to get (30).
+
+
+> [!exercise|c97f7d4d-54ae-5fb1-a812-a3a57afddcd0.local at=70575be1-8d57-5fe7-ad4f-d9cb3ab74600] Exercise 12
+> What is the solution of the heat problem (22)-(24) if $q=0$ ?
+
+
+> [!exercise|83c52217-9d82-5673-8275-db62af34ae8b.local at=8b51ab0b-3ede-51ed-8dad-c5171ccc9579] Exercise 13
+> Project Problem: A problem with time-dependent heat source. Solve the heat problem (22)-(24) with a time-dependent heat source $q(r, \theta, \phi, t)$. [Hint: Modify the solution of (22)-(24) as follows. In (27), you should allow the coefficients $q_{j n m}$ to depend on $t$. In (28), the right side depends on $t$. Solve (28)-(29) as in Exercise 18(c), Section 11.9.]
+
+
+> [!exercise|f31e1677-2016-56b2-96aa-35435b01f0fa.local at=3b78b980-d70d-59c2-91c5-87202d08db26] Exercise 14
+> A nonhomogeneous heat problem. Solve the heat equation (22) subject to the initial condition (24), and the nonhomogeneous boundary condition $u(a, \theta, \phi, t)=g(\theta, \phi)$. [Hint: Decompose the problem into two subproblems. See, for example, Exercise 17, Section 12.4.]
+
+
+> [!exercise|390e5a7f-4723-52c7-8ea1-cc6975a90b5c.local at=3a357e84-694f-5920-97af-f6357b828915] Exercise 15
+> A heat problem with symmetry. A solid ball at $30^{\circ} \mathrm{C}$ with radius $a=1$ is placed in a refrigerator that maintains a constant temperature of $0^{\circ} \mathrm{C}$. (a) Take $c=1$ and determine the temperature $u(r, \theta, \phi, t)$ inside the ball.
+> (b) The function
+>
+> $$
+> \theta_{4}(u, q)=1+2 \sum_{n=1}^{\infty}(-1)^{n} q^{n^{2}} \cos 2 n u
+> $$
+>
+> is called an elliptic theta function. This type of function is built into many computer systems. Express the temperature of the center in part (a) in terms of $\theta_{4}$, then plot the temperature for $t>0$.
+> (c) Use your graph in (b) to determine how long it will take for the temperature at the center to drop to $10^{\circ} \mathrm{C}$.
+
+
+> [!exercise|c09ffa86-a39a-5b53-8ee6-82f01444061e.local at=37bbb85d-59aa-5eb2-bf75-46a4ac457655] Exercise 16
+> (a) Solve the heat problem in the ball of radius 1 with $c=1$, given that the surface temperature is kept at $0^{\circ}$ and that the initial temperature distribution is $f(r, \theta, \phi)=r^{2}$. Assume that there is no internal source of heat.
+> (b) Plot the temperature of the center for $t>0$.
+
+
+> [!exercise|74918948-6ebb-5006-b4aa-3624a95f1a62.local at=98aee3e2-1da0-534c-abab-01b4f8e206ed] Exercise 17
+> (a) Solve the heat problem (22)-(24) inside the unit ball. Take $c=1, q= 20 r^{2}$, and $f(r, \theta, \phi)=100$.
+> (b) Plot the temperature of the center for $t>0$.
+
+
+> [!exercise|0021b4e5-ae1b-55b8-a22e-764c340d12d1.local at=48974c37-991b-5e56-8f16-6c5fd05a8b7b] Exercise 18
+> Project Problem: The wave equation in a ball. Derive (34)-(36).

`````
