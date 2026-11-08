
# Editorial records

Reading note: 15.1 Schrödinger's Equation.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!equation|54a28dfd-30da-5523-99ec-ce9d48ef36e8.local at=bdd72c66-8c3e-5f08-bbd0-143fc071b740] Born Position Probability Rule for a Normalized Wave Function
> For a normalized wave function $\psi\in L^2(\Omega)$, the position probability density is $\rho(\mathbf x)=|\psi(\mathbf x)|^2$, with $\int_\Omega|\psi|^2\,dV=1$. The probability of finding the particle in a measurable region $D\subseteq\Omega$ is
>
> $$
> \Pr(\mathbf x\in D)=\int_D|\psi(\mathbf x)|^2\,dV.
> $$
````
### After

````text
> [!equation|54a28dfd-30da-5523-99ec-ce9d48ef36e8.local at=bdd72c66-8c3e-5f08-bbd0-143fc071b740] Born Position Probability Rule for a Normalized Wave Function
> For a normalized wave function $\psi$ on the real line, the position probability density is
>
> $$
> \rho(x)=|\psi(x)|^{2}=\psi(x) \overline{\psi(x)} .
> $$
>
> In view of the fact that $\rho$ is a probability density, we have
>
> $$
> \int_{-\infty}^{\infty}|\psi(x)|^{2} d x=1
> $$
````

## 2. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!equation|badc4a50-c499-55b4-bff5-9b6b456cc60e.local at=176aa5f0-d7dc-5812-9efb-664ab086a528] Time-Dependent Schrödinger Equation for a Particle in a Scalar Potential
> For a nonrelativistic spin-free particle of mass $\mu>0$ in a time-independent real scalar potential $V(\mathbf x)$, with no magnetic vector potential,
>
> $$
> i\hbar\frac{\partial\psi}{\partial t}
> =-\frac{\hbar^2}{2\mu}\nabla^2\psi+V(\mathbf x)\psi.
> $$
>
> Here $\hbar=h/(2\pi)$ is the reduced Planck constant, $\psi$ is the wave function, and the Laplacian acts on the spatial variables. The equation is supplied with the physical domain, boundary conditions, and initial state.
````
### After

````text
> [!equation|badc4a50-c499-55b4-bff5-9b6b456cc60e.local at=176aa5f0-d7dc-5812-9efb-664ab086a528] Time-Dependent Schrödinger Equation for a Particle in a Scalar Potential
> $$
> i \hbar \frac{\partial \psi}{\partial t}=-\frac{\hbar^{2}}{2 \mu} \nabla^2\psi+V(x,y,z) \psi
> $$
>
> where $\hbar$ is the reduced Planck constant ( $\hbar\approx1.055 \times 10^{-34} \mathrm{~J} \cdot \mathrm{~s}$ ), $\mu$ is the mass of the particle, and $V$ is the time-independent potential energy of the force field (hence $F=-\nabla V$ ).
````

## 3. Restore source wording; retain only the actual correction.

### Before

````text
Schrödinger's equation is a postulate of this quantum model. Its predictions explain many phenomena at the atomic level.
````
### After

````text
Just as Newton's laws are to classical mechanics, Schrödinger's equation is really an axiom in quantum mechanics that leads to correct physical conclusions and that can be used to explain many phenomena at the atomic level.
````

## 4. Restore source wording; retain only the actual correction.

### Before

````text
In a quantum system the separation constant $E$ has units of energy. Here we first consider normalizable bound states; continuum states require a separate spectral treatment.
````
### After

````text
In a quantum system, the separation constant $E$ has units of energy. Here we consider normalizable bound states.
````

## 5. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!definition|45879971-2f63-545d-9561-b7cd14586826.local at=f4ad4499-052e-5d10-8351-85c6e2652dfd] Normalizable and Normalized Quantum Wave Functions
> A nonzero wave function $u$ on a configuration domain $\Omega$ is normalizable if $\int_\Omega|u|^2\,dV<\infty$. It is normalized if that integral equals one. A normalizable wave function becomes normalized after division by its $L^2$ norm. Pointwise decay at infinity is not part of the abstract $L^2$ definition; the bound-state solutions considered here also decay.
````
### After

````text
> [!definition|45879971-2f63-545d-9561-b7cd14586826.local at=f4ad4499-052e-5d10-8351-85c6e2652dfd] Normalizable and Normalized Quantum Wave Functions
> By normalizable we mean a nonzero function $f$ such that $|f|^2$ has a finite integral over the whole space. Let us also call a normalizable function $f$ normalized if $|f|^2$ has total integral 1.
````

## 6. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!definition|f702ef12-9c84-51b6-8698-798a3021c25a.local at=cc04c61e-0f04-52c0-a04f-9c109182fe94] Stationary State of a Time-Independent Schrödinger Hamiltonian
> For a particle of mass $\mu>0$ with a time-independent real potential $V$, let $H=-\hbar^2\nabla^2/(2\mu)+V$ be the self-adjoint Hamiltonian with the prescribed domain and boundary conditions. If $Hu=Eu$, $E\in\mathbb R$, and $u$ is a normalized eigenfunction, then
>
> $$
> \psi(\mathbf x,t)=e^{-iEt/\hbar}u(\mathbf x)
> $$
>
> is a stationary state of energy $E$. Its position probability density is $|u(\mathbf x)|^2$, independent of time.
````
### After

````text
> [!definition|f702ef12-9c84-51b6-8698-798a3021c25a.local at=cc04c61e-0f04-52c0-a04f-9c109182fe94] Stationary State of a Time-Independent Schrödinger Hamiltonian
> Let $u$ be a normalizable solution of $-\hbar^2\nabla^2u/(2\mu)+Vu=Eu$ satisfying the prescribed boundary conditions, with real time-independent $V$ and real $E$. A product solution of the time-dependent Schrödinger equation corresponding to an admissible value of $E$ is then
> $$
> \psi(x,y,z,t)=Ae^{-iEt/\hbar}u(x,y,z).
> $$
> Such a solution is called a stationary state with energy level $E$. Here $\mu$ is the particle mass, $\hbar$ is the reduced Planck constant, and $A$ normalizes $u$.
````

## 7. Restore source wording; retain only the actual correction.

### Before

````text
[Context for Exercises 4–6.]
````
### After

````text

````
