
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
