
# Editorial records

Reading note: 13.3 Spherical Harmonics and the General Dirichlet Problem.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!definition|70c0c06d-0abd-5637-a985-60980824a550.local at=867a9f45-675e-5433-9650-fbbd0289b7a8] Orthonormal complex spherical harmonics with the Condon–Shortley phase
> On the unit sphere, let $\theta\in[0,\pi]$ denote colatitude and $\phi$ denote azimuth modulo $2\pi$. For integers $n\ge0$ and $-n\le m\le n$, define
> $$
> Y_{n,m}(\theta,\phi)=\sqrt{\frac{2n+1}{4\pi}\frac{(n-m)!}{(n+m)!}}\,P_n^m(\cos\theta)e^{im\phi}.
> $$
> Here $P_n$ is the Legendre polynomial normalized by $P_n(1)=1$. For $0\le m\le n$,
> $$
> P_n^m(s)=(-1)^m(1-s^2)^{m/2}\frac{d^m}{ds^m}P_n(s),
> $$
> and for $1\le m\le n$,
> $$
> P_n^{-m}(s)=(-1)^m\frac{(n-m)!}{(n+m)!}P_n^m(s).
> $$
> The factor $(-1)^m$ is the Condon–Shortley phase convention. The surface measure used for normalization is $d\Omega=\sin\theta\,d\theta\,d\phi$.
````
### After

````text
> [!definition|70c0c06d-0abd-5637-a985-60980824a550.local at=867a9f45-675e-5433-9650-fbbd0289b7a8] Orthonormal complex spherical harmonics with the Condon–Shortley phase
> We now define the spherical harmonics $Y_{n, m}(\theta, \phi)$ by
>
> $$
> Y_{n, m}(\theta, \phi)=\sqrt{\frac{2 n+1}{4 \pi} \frac{(n-m)!}{(n+m)!}} P_{n}^{m}(\cos \theta) e^{i m \phi},
> $$
>
> where $n=0,1,2, \ldots$, and $m=-n,-n+1, \ldots, n-1, n$.
>
> Here $P_n^m(x)=(-1)^m(1-x^2)^{m/2}d^mP_n(x)/dx^m$ for $0\le m\le n$, and $P_n^{-m}=(-1)^m(n-m)!P_n^m/(n+m)!$ for $1\le m\le n$. Here $P_n$ is the Legendre polynomial normalized by $P_n(1)=1$.
````

## 2. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|10694bbd-a986-5f2c-876f-69b68411a74e.local at=080ce504-87c9-5e15-8fd6-aaa180d59f5d] Orthonormality of complex spherical harmonics on the unit sphere
> Let $Y_{n,m}$ be the standard normalized complex spherical harmonics of degree $n\ge0$ and order $-n\le m\le n$, using colatitude $\theta$ and azimuth $\phi$. For any two admissible degree–order pairs,
> $$
> \int_0^{2\pi}\int_0^\pi Y_{n,m}(\theta,\phi)\overline{Y_{n',m'}(\theta,\phi)}\sin\theta\,d\theta\,d\phi
> =\delta_{nn'}\delta_{mm'},
> $$
> where the overbar denotes complex conjugation and $\delta$ is the Kronecker delta. In particular, each harmonic has squared norm $1$ with respect to unit-sphere area measure.
````
### After

````text
> [!theorem|10694bbd-a986-5f2c-876f-69b68411a74e.local at=080ce504-87c9-5e15-8fd6-aaa180d59f5d] Orthogonality Relations for Spherical Harmonics
> Let $n=0,1,2, \ldots$, and $m=-n,-n+1, \ldots, n-1, n$, and let $Y_{n, m}$ be the normalized spherical harmonics. Then
> $\int_{0}^{2 \pi} \int_{0}^{\pi} Y_{n, m}(\theta, \phi) \bar{Y}_{n^{\prime}, m^{\prime}}(\theta, \phi) \sin \theta d \theta d \phi=0 \quad$ if $n \neq n^{\prime}$ or $m \neq m^{\prime}$, where $\bar{Y}_{n^{\prime}, m^{\prime}}$ is the complex conjugate of $Y_{n^{\prime}, m^{\prime}}$, and
>
> $$
> \int_{0}^{2 \pi} \int_{0}^{\pi}\left|Y_{n, m}(\theta, \phi)\right|^{2} \sin \theta d \theta d \phi=1
> $$
>
> Here $Y_{n,m}(\theta,\phi)=\sqrt{\frac{2n+1}{4\pi}\frac{(n-m)!}{(n+m)!}}P_n^m(\cos\theta)e^{im\phi}$, where $\theta$ is colatitude, $\phi$ is azimuth, and $P_n^m$ is the associated Legendre function.
````

## 3. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|97f3a242-dfd4-5495-a5fb-a4e2850d691f.local at=c2fd17f9-8f57-5537-837f-b30dad59cd4c] Mean-square expansion of a function on the sphere in spherical harmonics
> Let $f\in L^2(S^2,d\Omega)$, where $d\Omega=\sin\theta\,d\theta\,d\phi$ is unit-sphere area measure, $\theta$ is colatitude, and $\phi$ is azimuth. Let $Y_{n,m}$ be the standard orthonormal complex spherical harmonics. Then
> $$
> f(\theta,\phi)=\sum_{n=0}^{\infty}\sum_{m=-n}^{n}A_{nm}Y_{n,m}(\theta,\phi)
> $$
> with convergence in the $L^2$ norm, where
> $$
> A_{nm}=\int_0^{2\pi}\int_0^\pi f(\theta,\phi)\overline{Y_{n,m}(\theta,\phi)}\sin\theta\,d\theta\,d\phi.
> $$
> Square integrability alone does not assert pointwise convergence.
````
### After

````text
> [!theorem|97f3a242-dfd4-5495-a5fb-a4e2850d691f.local at=c2fd17f9-8f57-5537-837f-b30dad59cd4c] Spherical Harmonics Series Expansions
> Let $f(\theta, \phi)$ be a square-integrable function defined for all $0<\phi<2 \pi, 0<\theta<\pi$, and suppose that $f$ is $2 \pi$-periodic in $\phi$. Then we have the spherical harmonics series expansion
>
> $$
> f(\theta, \phi)=\sum_{n=0}^{\infty} \sum_{m=-n}^{n} A_{n m} Y_{n, m}(\theta, \phi)
> $$
>
> where the spherical harmonics coefficients are given by
>
> $$
> A_{n m}=\int_{0}^{2 \pi} \int_{0}^{\pi} f(\theta, \phi) \bar{Y}_{n, m}(\theta, \phi) \sin \theta d \theta d \phi
> $$
>
> Here $Y_{n,m}(\theta,\phi)=\sqrt{\frac{2n+1}{4\pi}\frac{(n-m)!}{(n+m)!}}P_n^m(\cos\theta)e^{im\phi}$, where $\theta$ is colatitude, $\phi$ is azimuth, and $P_n^m$ is the associated Legendre function. The series converges in mean square.
````

## 4. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|dc75bd76-a3d7-5017-99e8-77e5238bed47.local at=b3ff9dc1-5b54-565e-a598-bd6d0a291469] Interior Dirichlet solution in a ball by spherical harmonics
> Let $a>0$, and prescribe a continuous function $f$ on the sphere of radius $a$. With colatitude $\theta$ and azimuth $\phi$, let
> $$
> A_{nm}=\int_0^{2\pi}\int_0^\pi f(\theta,\phi)\overline{Y_{n,m}(\theta,\phi)}\sin\theta\,d\theta\,d\phi,
> $$
> where $Y_{n,m}$ are the standard orthonormal complex spherical harmonics. The unique solution of $\Delta u=0$ in the ball, continuous on its closure and satisfying $u(a,\theta,\phi)=f(\theta,\phi)$, is
> $$
> u(r,\theta,\phi)=\sum_{n=0}^{\infty}\sum_{m=-n}^{n}A_{nm}\left(\frac ra\right)^nY_{n,m}(\theta,\phi),\qquad0\le r<a.
> $$
> For square-integrable boundary data the same interior series gives the harmonic extension with boundary convergence in $L^2$. For bounded piecewise smooth data, the radial boundary limit equals the data at continuity points.
````
### After

````text
> [!theorem|dc75bd76-a3d7-5017-99e8-77e5238bed47.local at=b3ff9dc1-5b54-565e-a598-bd6d0a291469] Dirichlet Problem in a Ball
> The solution of $\nabla^2u=0$ in the ball $r<a$, subject to the boundary condition $u(a,\theta,\phi)=f(\theta,\phi)$ for continuous $f$, is given by
> $$
> u(r,\theta,\phi)=\sum_{n=0}^{\infty}\sum_{m=-n}^{n}A_{nm}\left(\frac ra\right)^nY_{n,m}(\theta,\phi),\qquad 0\le r<a,
> $$
> where $A_{nm}$ is the spherical harmonics coefficient of the boundary function $f$ and is given by
> $$
> A_{nm}=\int_0^{2\pi}\int_0^\pi f(\theta,\phi)\overline{Y_{n,m}(\theta,\phi)}\sin\theta\,d\theta\,d\phi.
> $$
> Here $Y_{n,m}(\theta,\phi)=\sqrt{\frac{2n+1}{4\pi}\frac{(n-m)!}{(n+m)!}}P_n^m(\cos\theta)e^{im\phi}$, where $\theta$ is colatitude, $\phi$ is azimuth, and $P_n^m$ is the associated Legendre function.
````

## 5. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|44585a75-2600-5aa5-b0a5-51337f490e14.local at=ef29e080-d5f4-5424-8a53-a0dc8ede9de5] Eigenvalues and eigenspaces of the Laplace–Beltrami operator on the unit sphere
> In colatitude $\theta$ and azimuth $\phi$, consider functions smooth on the unit sphere and the equation
> $$
> \Delta_{S^2}Y+\mu Y=0,\qquad
> \Delta_{S^2}Y=Y_{\theta\theta}+\cot\theta\,Y_\theta+\csc^2\theta\,Y_{\phi\phi}.
> $$
> Nonzero solutions exist exactly for $\mu=n(n+1)$, $n=0,1,2,\ldots$. The corresponding eigenspace of $-\Delta_{S^2}$ has dimension $2n+1$ and an orthonormal basis
> $$
> Y_{n,m}(\theta,\phi),\qquad m=-n,-n+1,\ldots,n,
> $$
> given by the normalized complex spherical harmonics. Orthogonality uses surface measure $\sin\theta\,d\theta\,d\phi$. The coordinate formula is used for $0<\theta<\pi$ with regularity at the poles and $2\pi$-periodicity in $\phi$.
````
### After

````text
> [!theorem|44585a75-2600-5aa5-b0a5-51337f490e14.local at=ef29e080-d5f4-5424-8a53-a0dc8ede9de5] Differential Equation for the Spherical Harmonics
> The equation
>
> $$
> \frac{\partial^{2} Y}{\partial \theta^{2}}+\cot \theta \frac{\partial Y}{\partial \theta}+\csc ^{2} \theta \frac{\partial^{2} Y}{\partial \phi^{2}}+\mu Y=0
> $$
>
> where $0<\theta<\pi, 0<\phi<2 \pi$, admits nontrivial bounded solutions that are $2 \pi$-periodic in $\phi$ when
>
> $$
> \mu=n(n+1), \quad n=0,1,2,3, \ldots .
> $$
>
> To each acceptable value of $\mu$ (or eigenvalue) we have $2 n+1$ nontrivial solutions (or eigenfunctions) given by the spherical harmonics
>
> $$
> Y(\theta, \phi)=Y_{n, m}(\theta, \phi), \quad|m| \leq n .
> $$
>
> Here $Y_{n,m}(\theta,\phi)=\sqrt{\frac{2n+1}{4\pi}\frac{(n-m)!}{(n+m)!}}P_n^m(\cos\theta)e^{im\phi}$, where $\theta$ is colatitude, $\phi$ is azimuth, and $P_n^m$ is the associated Legendre function.
````
