
# Editorial records

Reading note: 6.5 Green's Functions.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Move editorial commentary out of the reading note.

### Before

````text
*Editorial clarification: the boundary representation statements explicitly require bounded harmonic functions with the stated boundary limits, rather than arbitrary independently assigned boundary values. The missing Green-function properties were restored from the printed theorem; Exercise 11’s conjugates and imaginary unit were corrected against the PDF.*
````
### After

````text

````

## Additional source comparison

## 1. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!lemma|4b5f04b0-9d32-53f2-9c90-5a528244ebc7.local at=d91b3ab8-bb1d-5cc2-ae3b-b8cbb188941f] Boundary Integral Formula at the Center of a Conformal Disk Map
> Let $\Omega$ be a bounded simply connected region with a smooth simple boundary $\Gamma$, and let $\phi$ map $\Omega$ conformally onto the unit disk, extending analytically and one-to-one to the boundary. Let $u$ be a bounded harmonic function on $\Omega$ whose boundary limits give piecewise continuous data on $\Gamma$. Values at the finitely many discontinuities do not affect the integral. The derivative $\partial/\partial n_\zeta$ is along the outward unit normal at $\zeta\in\Gamma$, and $ds=|d\zeta|$ is arc length.
>
> If $z_0\in\Omega$ satisfies $\phi(z_0)=0$, then
>
> $$
> u(z_0)=\frac1{2\pi}\int_\Gamma u(\zeta)\frac{\partial}{\partial n_\zeta}\ln|\phi(\zeta)|\,ds.
> $$
````
### After

````text
> [!lemma|4b5f04b0-9d32-53f2-9c90-5a528244ebc7.local at=d91b3ab8-bb1d-5cc2-ae3b-b8cbb188941f] Change of Variables
> Suppose that $w=\phi(z)$ is a one-to-one analytic mapping of a simply connected region $\Omega$ and its boundary $\Gamma$ onto the open unit disk $D$ and its boundary $C$. Let $u$ be a bounded function harmonic on $\Omega$ and with piecewise continuous boundary limits on the boundary $\Gamma$. Let $z_{0}$ in $\Omega$ be the point such that $\phi\left(z_{0}\right)=0$. Then
>
> $$
> u\left(z_{0}\right)=\frac{1}{2 \pi} \int_{\Gamma} u(\zeta) \frac{\partial \ln |\phi(\zeta)|}{\partial n} d s
> $$
>
> where $d s=|d \zeta|$ is the element of arc length on $\Gamma$. Hence if $\Gamma$ is parametrized by $\gamma(t), a \leq t \leq b$, then $d s=\left|\gamma^{\prime}(t)\right| d t$. The boundary is smooth, and $\partial/\partial n$ denotes the outward normal derivative in $\zeta$.
````

## 2. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|73626c8b-8bf6-5626-ab7f-b5d56507a6bc.local at=a64f3bd8-f4e9-5b3c-bb32-6159d228c043] Green Function Boundary Representation for Planar Harmonic Functions
> Let $\Omega$ be a bounded simply connected region with a smooth simple boundary $\Gamma$, and let $\phi$ map $\Omega$ conformally onto the unit disk, extending analytically and one-to-one to the boundary. Let $u$ be a bounded harmonic function on $\Omega$ whose boundary limits give piecewise continuous data on $\Gamma$. Values at the finitely many discontinuities do not affect the integral. The derivative $\partial/\partial n_\zeta$ is along the outward unit normal at $\zeta\in\Gamma$, and $ds=|d\zeta|$ is arc length.
>
> For $z\in\Omega$, put
>
> $$
> \Phi(z,\zeta)=\frac{\phi(\zeta)-\phi(z)}{1-\overline{\phi(z)}\phi(\zeta)}.
> $$
>
> Then
>
> $$
> u(z)=\frac1{2\pi}\int_\Gamma u(\zeta)\frac{\partial}{\partial n_\zeta}\ln|\Phi(z,\zeta)|\,ds.
> $$
````
### After

````text
> [!theorem|73626c8b-8bf6-5626-ab7f-b5d56507a6bc.local at=a64f3bd8-f4e9-5b3c-bb32-6159d228c043] Green Function Boundary Representation for Planar Harmonic Functions
> Suppose that $\Omega$ is a simply connected region with boundary $\Gamma$, and $\phi$ is a one-to-one analytic function on $\Omega$ and its boundary onto the unit disk and its boundary. Let $u(z)$ be a bounded function harmonic on $\Omega$ and with piecewise continuous boundary limits on $\Gamma$. For $z$ and $\zeta$ in $\Omega$, let $\Phi(z, \zeta)$ $\Phi(z,\zeta)=(\phi(\zeta)-\phi(z))/(1-\overline{\phi(z)}\phi(\zeta))$. Then, for any $z$ in $\Omega$, we have
> $$
> u(z)=\frac{1}{2 \pi} \int_{\Gamma} u(\zeta) \frac{\partial}{\partial n} \ln |\Phi(z, \zeta)| d s
> $$
>
> where $d s=|d \zeta|$ is the element of arc length on $\Gamma$. The boundary is smooth; the normal derivative is outward in $\zeta$.
````

## 3. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!definition|22294c03-a159-5ada-85fa-bda8ea638b64.local at=a0780b4a-230d-5bab-9756-cb379d15b1d0] Logarithmically Normalized Dirichlet Green Function of a Simply Connected Planar Region
> Let $\Omega\subsetneq\mathbb C$ be a simply connected region and let $\phi:\Omega\to\mathbb D$ be a conformal bijection. For distinct $z,\zeta\in\Omega$, the Dirichlet Green function with logarithmic normalization is
>
> $$
> G(z,\zeta)=\ln\left|\frac{\phi(\zeta)-\phi(z)}{1-\overline{\phi(z)}\phi(\zeta)}\right|.
> $$
>
> It has a logarithmic singularity as $\zeta\to z$. This convention makes $G$ negative in the interior; its definition is independent of the choice of $\phi$.
````
### After

````text
> [!definition|22294c03-a159-5ada-85fa-bda8ea638b64.local at=a0780b4a-230d-5bab-9756-cb379d15b1d0] Logarithmically Normalized Dirichlet Green Function of a Simply Connected Planar Region
> Let $\phi$ be a one-to-one analytic map of a simply connected region $\Omega$ onto the unit disk. Put $\Phi(z,\zeta)=(\phi(\zeta)-\phi(z))/(1-\overline{\phi(z)}\phi(\zeta))$.
>
> The function
>
> $$
> G(z, \zeta)=\ln |\Phi(z, \zeta)|=\ln \left|\frac{\phi(\zeta)-\phi(z)}{1-\overline{\phi(z)} \phi(\zeta)}\right|, \quad z,\zeta\in\Omega,\ z\ne\zeta
> $$
>
> is called the Green's function for the region $\Omega$.
````

## 4. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|0bf7894d-52ad-5799-bf75-03148eb29f36.local at=42dc429e-e2cb-51f6-a7e0-31b8aca25f4d] Sign, Symmetry, and Logarithmic Decomposition of Planar Dirichlet Green Functions
> Let $\Omega$ be a simply connected planar region with boundary $\Gamma$, and let $\phi$ be a conformal bijection to the unit disk that extends analytically and one-to-one to the boundary. Define, for $z\ne\zeta$ in $\Omega$,
>
> $$
> G(z,\zeta)=\ln\left|\frac{\phi(\zeta)-\phi(z)}{1-\overline{\phi(z)}\phi(\zeta)}\right|.
> $$
>
> (i) $G(z,\zeta)\leq0$ in the interior (with $G(z,z)=-\infty$ understood at its logarithmic singularity).
>
> (ii) For $z\in\Omega$ and $\zeta\in\Gamma$, the boundary value is $G(z,\zeta)=0$.
>
> (iii) $G(z,\zeta)=G(\zeta,z)$.
>
> (iv) For every fixed $z\in\Omega$, there is a function $u_1(z,\zeta)$ harmonic in $\zeta$ throughout $\Omega$, with boundary values $-\ln|z-\zeta|$, such that
>
> $$
> G(z,\zeta)=u_1(z,\zeta)+\ln|z-\zeta|\qquad(\zeta\ne z).
> $$
````
### After

````text
> [!theorem|0bf7894d-52ad-5799-bf75-03148eb29f36.local at=42dc429e-e2cb-51f6-a7e0-31b8aca25f4d] Properties of Green's Functions
> Suppose that $\Omega$ is a simply connected region with boundary $\Gamma$, and let $\phi$ be a one-to-one analytic mapping of $\Omega$ and its boundary onto the unit disk and its boundary. Put
>
> $$
> \Phi(z,\zeta)=\frac{\phi(\zeta)-\phi(z)}{1-\overline{\phi(z)}\phi(\zeta)},\qquad G(z,\zeta)=\ln|\Phi(z,\zeta)|.
> $$
>
> Then the Green's function $G(z,\zeta)$ has the following properties:
>
> (i) $G(z,\zeta)\leq0$ for all $z$ and $\zeta$ in $\Omega$ (with the logarithmic value $-\infty$ at $z=\zeta$);
>
> (ii) $G(z,\zeta)=0$ for all $z$ in $\Omega$ and $\zeta$ on $\Gamma$;
>
> (iii) $G(z,\zeta)=G(\zeta,z)$ for all $z$ and $\zeta$ in $\Omega$ (symmetric property);
>
> (iv) for each $z$ in $\Omega$, there is a function $\zeta\mapsto u_1(z,\zeta)$, such that $u_1(z,\zeta)$ is harmonic for all $\zeta$ in $\Omega$, $u_1(z,\zeta)=-\ln|z-\zeta|$ for all $\zeta$ on the boundary $\Gamma$, and $G(z,\zeta)=u_1(z,\zeta)+\ln|z-\zeta|$ for all $\zeta\ne z$ in $\Omega$.
````

## Additional source comparison

## 1. Correct duplicated notation in restored sentence.

### Before

````text
let $\Phi(z, \zeta)$ $\Phi(z,\zeta)=(\phi(\zeta)-\phi(z))/(1-\overline{\phi(z)}\phi(\zeta))$
````
### After

````text
let $\Phi(z,\zeta)=(\phi(\zeta)-\phi(z))/(1-\overline{\phi(z)}\phi(\zeta))$
````
