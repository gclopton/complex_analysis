
# Editorial records

Reading note: 15.2 The Hydrogen Atom.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|474dbf46-4fc8-53fb-ad79-c93a4768353f.local at=127d6c35-7f7c-5731-8c36-127f30424887] Bound-State Energies and Degeneracy of the Spin-Free Hydrogen Atom
> Consider the nonrelativistic, spin-free hydrogen Coulomb Hamiltonian $H=-\hbar^2\nabla^2/(2\mu)-\epsilon^2/r$ with a fixed nucleus, electron mass $\mu>0$, and the usual regular physical domain at the origin. Here $\epsilon^2$ is the Coulomb coupling (in SI, $e^2/(4\pi\varepsilon_0)$), $\hbar$ is the reduced Planck constant, and $a=\hbar^2/(\mu\epsilon^2)$.
>
> Write $\nu=1,2,\ldots$, $n=0,\ldots,\nu-1$, and $m=-n,\ldots,n$. Let $Y_{n,m}$ be orthonormal spherical harmonics and $L_j^\alpha$ the generalized Laguerre polynomials. Define
>
> $$
> R_{\nu n}(r)=e^{-r/(\nu a)}\left(\frac{2r}{\nu a}\right)^n L_{\nu-n-1}^{2n+1}\left(\frac{2r}{\nu a}\right).
> $$
>
> The bound-state energies and a basis of their spatial eigenspaces are
>
> $$
> E_\nu=-\frac{\mu\epsilon^4}{2\hbar^2\nu^2},\qquad
> u_{\nu nm}(r,\theta,\phi)=R_{\nu n}(r)Y_{n,m}(\theta,\phi).
> $$
>
> The eigenspace at $E_\nu$ has dimension $\nu^2$ before spin is included. Arbitrary linear combinations within that eigenspace are also states of the same energy.
````
### After

````text
> [!theorem|474dbf46-4fc8-53fb-ad79-c93a4768353f.local at=127d6c35-7f7c-5731-8c36-127f30424887] Energy Levels and Bound States of the Hydrogen Atom
> Consider the nonrelativistic, spin-free hydrogen Coulomb Hamiltonian $H=-\hbar^2\nabla^2/(2\mu)-\epsilon^2/r$ with a fixed nucleus, electron mass $\mu>0$, and the usual regular physical domain at the origin. Here $\epsilon^2$ is the Coulomb coupling (in SI, $e^2/(4\pi\varepsilon_0)$), $\hbar$ is the reduced Planck constant, and $a=\hbar^2/(\mu\epsilon^2)$.
>
> Write $\nu=1,2,\ldots$, $n=0,\ldots,\nu-1$, and $m=-n,\ldots,n$. Let $Y_{n,m}$ be orthonormal spherical harmonics and $L_j^\alpha$ the generalized Laguerre polynomials. Define
>
> $$
> R_{\nu n}(r)=e^{-r/(\nu a)}\left(\frac{2r}{\nu a}\right)^n L_{\nu-n-1}^{2n+1}\left(\frac{2r}{\nu a}\right).
> $$
>
> (i) The bound states of the hydrogen atom have negative energies
>
> $$
> E_{\nu}=-\frac{\epsilon^{4} \mu}{2 \hbar^{2}} \frac{1}{\nu^{2}}, \quad \nu=1,2,3, \ldots
> $$
>
> (ii) To each energy level $E_{\nu}$ correspond $\nu^{2}$ bound states with
>
> $$
> u_{\nu n m}(r, \theta, \phi)=R_{\nu n}(r) Y_{n, m}(\theta, \phi), \quad|m| \leq n<\nu
> $$
>
> where the radial function $R_{\nu n}(r)$ is defined above and $Y_{n, m}(\theta, \phi)$ is a normalized spherical harmonic.
````

## 2. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|a73411ee-5af7-5520-8526-ddcb1974396a.local at=088227d9-a316-582e-8873-563a8329e78a] Normalized Hydrogen Bound-State Wave Functions and Position Densities
> Consider the nonrelativistic, spin-free hydrogen Coulomb Hamiltonian $H=-\hbar^2\nabla^2/(2\mu)-\epsilon^2/r$ with a fixed nucleus, electron mass $\mu>0$, and the usual regular physical domain at the origin. Here $\epsilon^2$ is the Coulomb coupling (in SI, $e^2/(4\pi\varepsilon_0)$), $\hbar$ is the reduced Planck constant, and $a=\hbar^2/(\mu\epsilon^2)$.
>
> Write $\nu=1,2,\ldots$, $n=0,\ldots,\nu-1$, and $m=-n,\ldots,n$. Let $Y_{n,m}$ be orthonormal spherical harmonics and $L_j^\alpha$ the generalized Laguerre polynomials. Define
>
> $$
> R_{\nu n}(r)=e^{-r/(\nu a)}\left(\frac{2r}{\nu a}\right)^n L_{\nu-n-1}^{2n+1}\left(\frac{2r}{\nu a}\right).
> $$
>
> For $E_\nu=-\mu\epsilon^4/(2\hbar^2\nu^2)$, a normalized stationary basis state is
>
> $$
> \begin{aligned}
> \psi_{\nu nm}(r,\theta,\phi,t)&=A_{\nu n}e^{-iE_\nu t/\hbar}R_{\nu n}(r)Y_{n,m}(\theta,\phi),\\
> A_{\nu n}&=\left[\left(\frac{2}{a\nu}\right)^3\frac{(\nu-n-1)!}{2\nu(\nu+n)!}\right]^{1/2}.
> \end{aligned}
> $$
>
> Its position density with respect to volume measure is $\rho_{\nu nm}=A_{\nu n}^2R_{\nu n}(r)^2|Y_{n,m}(\theta,\phi)|^2$. Probabilities in spherical coordinates integrate this density against $r^2\sin\theta\,dr\,d\theta\,d\phi$.
````
### After

````text
> [!theorem|a73411ee-5af7-5520-8526-ddcb1974396a.local at=088227d9-a316-582e-8873-563a8329e78a] Time-Dependent Wave Function and Probability Distribution
> Consider the nonrelativistic, spin-free hydrogen Coulomb Hamiltonian $H=-\hbar^2\nabla^2/(2\mu)-\epsilon^2/r$ with a fixed nucleus, electron mass $\mu>0$, and the usual regular physical domain at the origin. Here $\epsilon^2$ is the Coulomb coupling (in SI, $e^2/(4\pi\varepsilon_0)$), $\hbar$ is the reduced Planck constant, and $a=\hbar^2/(\mu\epsilon^2)$.
>
> Write $\nu=1,2,\ldots$, $n=0,\ldots,\nu-1$, and $m=-n,\ldots,n$. Let $Y_{n,m}$ be orthonormal spherical harmonics and $L_j^\alpha$ the generalized Laguerre polynomials. Define
>
> $$
> R_{\nu n}(r)=e^{-r/(\nu a)}\left(\frac{2r}{\nu a}\right)^n L_{\nu-n-1}^{2n+1}\left(\frac{2r}{\nu a}\right).
> $$
>
> The energy is $E_\nu=-\mu\epsilon^4/(2\hbar^2\nu^2)$.
>
> (i) The time-dependent wave function of the electron in a hydrogen atom in a state at energy level $E_{\nu}$ is
>
> $$
> \psi_{\nu n m}(r, \theta, \phi, t)=A_{\nu n} e^{-i E_{\nu} t / \hbar} R_{\nu n}(r) Y_{n, m}(\theta, \phi)
> $$
>
> where
>
> $$
> A_{\nu n}=\sqrt{\left(\frac{2}{a \nu}\right)^{3} \frac{(\nu-n-1)!}{2 \nu(\nu+n)!}}, \quad|m| \leq n<\nu, \nu=1,2, \ldots .
> $$
>
> (ii) The probability density for the electron's position in a state at energy level $E_{\nu}$ is given by
>
> $$
> \rho_{\nu n m}(r, \theta, \phi)=A_{\nu n}^{2} R_{\nu n}^{2}(r)\left|Y_{n, m}(\theta, \phi)\right|^{2}
> $$
````

## 3. Restore source wording; retain only the actual correction.

### Before

````text
(about 1836 times heavier; the printed “1864” is corrected)
````
### After

````text
(about 1836 times heavier)
````

## 4. Restore source wording; retain only the actual correction.

### Before

````text
because imposing both the physical regularity condition at the origin and square integrability at infinity selects these values. Square integrability alone, without the Hamiltonian’s origin condition, is insufficient to exclude all singular radial branches.
````
### After

````text
since for all other values of $\nu$ the product solutions that are regular at the origin are not square integrable, and hence not normalizable.
````

## 5. Move correction/commentary into the separate editorial record; keep the actual correction in the reading text.

### Before

````text
[Source correction: the density in Exercise 7(a) lacks the normalization factor $(2\nu-1)!$, while part (b) has an extra copy of that factor. Both formulas below are corrected; the printed probability would fail to vanish at $s=0$ for $\nu>1$.]
````
### After

````text

````
