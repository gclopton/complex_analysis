
# Editorial records

Reading note: 13.2 Dirichlet Problems with Symmetry.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|dc29d4e6-1aee-5a21-a63d-46b8e290d2e4.local at=efc6be32-e1e9-5111-9eee-d0464b9e30e5] Axisymmetric Dirichlet solution inside a ball by Legendre series
> Let $a>0$, with colatitude $0\le\theta\le\pi$ and azimuth $\phi$. Let the prescribed surface temperature $f(\theta)$ be independent of $\phi$ and piecewise smooth. The regular harmonic solution inside the ball $r<a$ is
> $$
> u(r,\theta)=\sum_{n=0}^{\infty}A_n\left(\frac ra\right)^nP_n(\cos\theta),
> \qquad
> A_n=\frac{2n+1}{2}\int_0^\pi f(\theta)P_n(\cos\theta)\sin\theta\,d\theta,
> $$
> where $P_n$ is the Legendre polynomial normalized by $P_n(1)=1$. The interior series solves $\Delta u=0$ and has radial boundary limit $f(\theta)$ at continuity points. If $f$ is continuous on $[0,\pi]$, it gives the unique harmonic solution continuous on the closed ball with $u(a,\theta)=f(\theta)$.
````
### After

````text
> [!theorem|dc29d4e6-1aee-5a21-a63d-46b8e290d2e4.local at=efc6be32-e1e9-5111-9eee-d0464b9e30e5] Dirichlet Problem in a Ball
> The solution of the Dirichlet problem $\nabla^2u=0$ for $r<a$, $u(a,\theta)=f(\theta)$ with bounded piecewise smooth axisymmetric boundary data, is given by
>
> $$
> u(r, \theta)=\sum_{n=0}^{\infty} A_{n}\left(\frac{r}{a}\right)^{n} P_{n}(\cos \theta),
> $$
>
> where $P_{n}$ is the $n$th Legendre polynomial, and
>
> $$
> A_{n}=\frac{2 n+1}{2} \int_{0}^{\pi} f(\theta) P_{n}(\cos \theta) \sin \theta d \theta, \quad n=0,1,2, \ldots
> $$ The boundary values are attained at continuity points of $f$.
````
