
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
