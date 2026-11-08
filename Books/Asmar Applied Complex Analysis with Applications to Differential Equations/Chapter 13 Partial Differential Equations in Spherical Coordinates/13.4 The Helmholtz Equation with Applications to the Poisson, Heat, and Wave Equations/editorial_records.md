
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
