
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

## Source-to-current comparison

Source: /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 15 An Introduction to Quantum Mechanics/15.1 Schrödinger's Equation.md

This exact comparison preserves the full change evidence, including formatting, OCR corrections, restored source wording, and required standalone context. The entries above explain the recovery edits. The comparison is not a claim that every difference is a correction; component serialization, callout wrapping, and printed labels outside callouts are formatting.

`````diff
--- /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 15 An Introduction to Quantum Mechanics/15.1 Schrödinger's Equation.md
+++ /Users/gradyclopton/ObsidianVaults/complex_analysis/Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 15 An Introduction to Quantum Mechanics/15.1 Schrödinger's Equation.md
@@ -1,6 +1,7 @@
+
 ## Topics to Review
 
-In Sections 15.1 and 15.2 we will use the method of separation of variables in solving certain special cases of the time-dependent Schrödinger equation. The detailed solutions of these problems require the use of the Hermite and Laguerre polynomials. The basic properties of these polynomials are covered in Section 15.4 and will be called upon as needed. A thorough treatment of Section 15.4 is not a prerequisite for this chapter. Spherical harmonics as presented in Section 5.4 are used in Section 15.2; however, as with the Lagnerre and Hermite polynomials, this material need not have been studied previously but can be referred to as needed. The Fourier transform, as presented in Section 7.2. plays a crucial role in Section 15.3.
+In Sections 15.1 and 15.2 we will use the method of separation of variables in solving certain special cases of the time-dependent Schrödinger equation. The detailed solutions of these problems require the use of the Hermite and Laguerre polynomials. The basic properties of these polynomials are covered in Section 15.4 and will be called upon as needed. A thorough treatment of Section 15.4 is not a prerequisite for this chapter. Spherical harmonics as presented in Section 13.3 are used in Section 15.2; however, as with the Laguerre and Hermite polynomials, this material need not have been studied previously but can be referred to as needed. The Fourier transform, as presented in Section 8.2. plays a crucial role in Section 15.3.
 
 ## Looking Ahead...
 
@@ -10,20 +11,29 @@
 
 ## AN INTRODUCTION TO QUANTUM MECHANICS
 
-The final truth about a phenomenon resides in the mathematical de-
-scription of it; so long as there is no imperfection in this, our knowl-
-edge of the phenomenon is complete. We go beyond mathematical
-formulas at our oun risk:
+The final truth about a phenomenon resides in the mathematical description of it; so long as there is no imperfection in this, our knowledge of the phenomenon is complete. We go beyond mathematical
+formulas at our own risk:
 -SIR JAMES JEANS
 
 Up to now we have considered very classical topics from physics and engineering: primarily the heat (or diffusion) equation, the wave equation, Laplace's equation, and Poisson's equation. We now take up some interesting topics that arise in quantum theory. In Section 15.1 we begin with a brief introduction to the fundamental objects and concepts of quantum mechanics, show how Schrödinger's equation enters the picture and then proceed with the method of separation of variables. In Section 15.2 we present the most successful application of our tools and methods in quantum mechanics: the model of the hydrogen atom. In Section 15.3 we present a connection with the Fourier transform and then proceed to develop the Heisenberg uncertainty principle in this context. The final section is a supplement on orthogonal polynomials. These polynomials are needed in the solution of partial differential equations arising in our models from quantum mechanics. The applications of this chapter will give us the opportunity of applying the method of separation of variables in a new and very interesting setting. Indeed, the model of the hydrogen atom, as presented in Section 15.2, was among the major successes of quantum mechanics.
 
 ### 15.1 Schrödinger's Equation
 
-![](./images/68a1ca9d-3a11-44bb-a7dd-ac2482ab3577-02_450_444_1259_67.jpg)
-Figure 1 Probability as an area.
-
-In classical mechanics, the trajectory of an object moving under the influence of a force can be completely determined once we know the initial position and velocity. Newton's second law of motion, $F=m a$, lies at the foundation of this theory. It is the key in deriving the differential equations that govern the behavior of the moving object (c.g., a mass on a spring, a vibrating string or membrane, a hanging chain). In the early 1900 s, it was discovered that the classical models based on Newton's law do not adequately describe the motion of very small objects, such as electrons. Indeed, it is a fact that one cannot measure accurately and simultaneously the position and velocity of an atomic particle (see Heisenberg's uncertainty principle, Section 15.3). Because of this sharp distinction from classical mechanics, and because the state of particles cannot be determined with an absolute certainty, a new theory emerged based on statistical viewpoints. This revolutionary theory, known as quantum mechanics, postulates that the position of atomic particles can only be determined with a certain probability.
+```scientific-figure
+id: 3a517690-30e2-4f94-ab74-1faec9adfea3
+numbered: false
+title: ""
+caption: Figure 1 Probability as an area.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 15 An Introduction to Quantum Mechanics/images/68a1ca9d-3a11-44bb-a7dd-ac2482ab3577-02_450_444_1259_67.jpg
+    caption: ""
+```
+
+
+In classical mechanics, the trajectory of an object moving under the influence of a force can be completely determined once we know the initial position and velocity. Newton's second law of motion, $F=m a$, lies at the foundation of this theory. It is the key in deriving the differential equations that govern the behavior of the moving object (e.g., a mass on a spring, a vibrating string or membrane, a hanging chain). In the early 1900 s, it was discovered that the classical models based on Newton's law do not adequately describe the motion of very small objects, such as electrons. Indeed, it is a fact that one cannot measure accurately and simultaneously the position and velocity of an atomic particle (see Heisenberg's uncertainty principle, Section 15.3). Because of this sharp distinction from classical mechanics, and because the state of particles cannot be determined with an absolute certainty, a new theory emerged based on statistical viewpoints. This revolutionary theory, known as quantum mechanics, postulates that the position of atomic particles can only be determined with a certain probability.
 
 ## Born's Statistical Interpretation
 
@@ -33,26 +43,30 @@
 
 Because the total probability is one, we have $\int_{-\infty}^{\infty} \rho(x) d x=1$. In Figure 1, this probability is the shaded area under the graph of $\rho$ between $x=a$ and $x=b$.
 
-A quantity of fundamental importance is the electrons wave function, $\psi(x)$. Knowledge of this function allows us to predict the whole behavior of the clectron. We can use it to determine the probability density for the electron's momentum and velocity, and many other quantities. For example, one of the fundamental axioms of quantum mechanics states that the position density $\rho$ can be computed from the wave function $\psi$ via the formula
-
-$$
-\rho(x)=|\psi(x)|^{2}=\psi(x) \overline{\psi(x)} .
-$$
-
-Strictly spcaking, Planck's constant refers to the constant $h=6.626 \times 10^{-34} \mathrm{~J} \cdot \mathrm{~s}$, introduced by Max Planck in 1900 to explain the black body radiation problem, and used by Einstein five years later to explain the photoelectric effect. The constant $h$ is oqual to $h /(2 \pi)$ and serves as a much more fundamental constant in the formulation of quantum mechanies.
-
-In view of the fact that $\rho$ is a probability density, we have
-
-$$
-\int_{-\infty}^{\infty}|\psi(x)|^{2} d x=1
-$$
+A quantity of fundamental importance is the electron’s wave function, $\psi(x)$. Knowledge of this function allows us to predict the whole behavior of the electron. We can use it to determine the probability density for the electron's momentum and velocity, and many other quantities. For example, one of the fundamental axioms of quantum mechanics states that the position density $\rho$ can be computed from the wave function $\psi$ via the formula
+
+> [!equation|54a28dfd-30da-5523-99ec-ce9d48ef36e8.local at=bdd72c66-8c3e-5f08-bbd0-143fc071b740] Born Position Probability Rule for a Normalized Wave Function
+> For a normalized wave function $\psi$ on the real line, the position probability density is
+>
+> $$
+> \rho(x)=|\psi(x)|^{2}=\psi(x) \overline{\psi(x)} .
+> $$
+>
+> In view of the fact that $\rho$ is a probability density, we have
+>
+> $$
+> \int_{-\infty}^{\infty}|\psi(x)|^{2} d x=1
+> $$
+
+*Printed equation labels: (1) position probability density; (2) normalization.*
 
 The probability density for the electron's momentum is related to the wave function $\psi$ via the Fourier transform. This connection is explored in Section 15.3.
 
-For particles moving in a force field in two or three dimensions, the same definitions apply. In addition, we may have to account for time-dependence. In this case, the probability densities are functions of two, three, or more variables. For example, for a particle moving in three dimensions with timedependent wave function $\psi$, the probability of finding this particle in a region $D$ at a given time $t$ is
+For particles moving in a force field in two or three dimensions, the same definitions apply. In addition, we may have to account for time-dependence. In this case, the probability densities are functions of two, three, or more variables. For example, for a particle moving in three dimensions with time-dependent wave function $\psi$, the probability of finding this particle in a region $D$ at a given time $t$ is
 
 $$
 \iiint_{D}|\psi(x, y, z, t)|^{2} d x d y d z
+\tag{3}
 $$
 
 Thus, for fixed $t$, the probability density for the particle's position is
@@ -67,11 +81,16 @@
 
 It is a fact from quantum mechanics that the wave function $\psi(x, y, z, t)$ is a solution of the Schrödinger equation
 
-$$
-i \hbar \frac{\partial \psi}{\partial t}=-\frac{\hbar^{2}}{2 \mu} \nabla^{2} \uparrow+V(x . y, z) \psi
-$$
-
-where $\hbar$ is Planck's constant ( $\hbar=1.054 \times 10^{-34} \mathrm{~J} \cdot \mathrm{~s}$ ), $\mu$ is the mass of the particle, and $V$ is the time-independent potential energy of the force field (hence $F=-\nabla V$ ). Just as Newton's laws are to classical mechanics. Schrödinger's equation is really an axiom in quantum mechanics that leads to correct physical conclusions and that can be used to explain many phenomena at the atomic level.
+> [!equation|badc4a50-c499-55b4-bff5-9b6b456cc60e.local at=176aa5f0-d7dc-5812-9efb-664ab086a528] Time-Dependent Schrödinger Equation for a Particle in a Scalar Potential
+> $$
+> i \hbar \frac{\partial \psi}{\partial t}=-\frac{\hbar^{2}}{2 \mu} \nabla^2\psi+V(x,y,z) \psi
+> $$
+>
+> where $\hbar$ is the reduced Planck constant ( $\hbar\approx1.055 \times 10^{-34} \mathrm{~J} \cdot \mathrm{~s}$ ), $\mu$ is the mass of the particle, and $V$ is the time-independent potential energy of the force field (hence $F=-\nabla V$ ).
+
+*Printed equation label: (4).*
+
+Just as Newton's laws are to classical mechanics, Schrödinger's equation is really an axiom in quantum mechanics that leads to correct physical conclusions and that can be used to explain many phenomena at the atomic level.
 
 ## Solution by Separation of Variables
 
@@ -79,6 +98,7 @@
 
 $$
 \psi(x, y, z, 0)=f(x, y, z)
+\tag{5}
 $$
 
 For now we will simply apply the separation of variables method to (4), without specifying the potential $V$ or the initial condition (5).
@@ -99,31 +119,42 @@
 
 $$
 T^{\prime}=-\frac{i}{\hbar} E T
+\tag{6}
 $$
 
 and the time-independent Schrödinger equation for $u$,
 
 $$
 -\frac{\hbar^{2}}{2 \mu} \nabla^{2} u+V(x, y, z) u=E u .
+\tag{7}
 $$
 
 You can easily check that the solutions of (6) are the simple harmonic functions
 
 $$
 T(t)=A e^{-i E t / \hbar}
+\tag{8}
 $$
 
 where $A$ is a constant. Equation (7) is much more difficult to solve. Its solutions have been computed in only a few but important cases of the potential $V$; some of them will be discussed in this chapter.
 
 ## Stationary States and the General Solution
 
-In a quantum system, the separation constant $E$ has units of energy. An admissible value of $E$, or eigenvalue, is one for which we have a nontrivial solution of (7) that is normalizable, where by normalizable we mean a function $f$ that tends to zero at infinity and such that $|f|^{2}$ has a finite integral over the whole space. Let us also call a normalizable function $f$ normalized if $|f|^{2}$ has total integral 1. A product solution of (4) corresponding to an admissible value of $E$ is then
-
-$$
-\psi(x, y, z, t)=A e^{-i E t / h} u(x, y, z) .
-$$
-
-Such solution of (4) is called a stationary state with energy level $E$. For a stationary state, although $\psi$ is time-dependent, the probability density
+In a quantum system, the separation constant $E$ has units of energy. Here we consider normalizable bound states.
+
+> [!definition|45879971-2f63-545d-9561-b7cd14586826.local at=f4ad4499-052e-5d10-8351-85c6e2652dfd] Normalizable and Normalized Quantum Wave Functions
+> By normalizable we mean a nonzero function $f$ such that $|f|^2$ has a finite integral over the whole space. Let us also call a normalizable function $f$ normalized if $|f|^2$ has total integral 1.
+
+> [!definition|f702ef12-9c84-51b6-8698-798a3021c25a.local at=cc04c61e-0f04-52c0-a04f-9c109182fe94] Stationary State of a Time-Independent Schrödinger Hamiltonian
+> Let $u$ be a normalizable solution of $-\hbar^2\nabla^2u/(2\mu)+Vu=Eu$ satisfying the prescribed boundary conditions, with real time-independent $V$ and real $E$. A product solution of the time-dependent Schrödinger equation corresponding to an admissible value of $E$ is then
+> $$
+> \psi(x,y,z,t)=Ae^{-iEt/\hbar}u(x,y,z).
+> $$
+> Such a solution is called a stationary state with energy level $E$. Here $\mu$ is the particle mass, $\hbar$ is the reduced Planck constant, and $A$ normalizes $u$.
+
+*Printed equation label: (9).*
+
+More generally a constant factor $A$ can be included in the spatial normalization. For such a product solution, For a stationary state, although $\psi$ is time-dependent, the probability density
 
 $$
 |\psi(x, y, z, t)|^{2}=|A|^{2}\left|e^{-i E t / \hbar}\right|^{2}|u(x, y, z)|^{2}=|A|^{2}|u(x, y, z)|^{2}
@@ -131,7 +162,7 @@
 
 is not, and thus the term stationary. This is clearly not the case with arbitrary solutions of (4).
 
-To proceed any further with the solution requires knowing the potential $V$ and the initial wave function in (5). We can gain some insight, however, by tying in our discussion with Sturm-Liouville theory from Section 6.2. For this purpose, let us consider the one dimensional problem
+To proceed any further with the solution requires knowing the potential $V$ and the initial wave function in (5). We can gain some insight, however, by tying in our discussion with Sturm-Liouville theory from Section 14.2. For this purpose, let us consider the one dimensional problem
 
 $$
 \begin{gathered}
@@ -140,64 +171,85 @@
 \end{gathered}
 $$
 
+*Printed equation labels: (10) one-dimensional Schrödinger equation; (11) initial wave function.*
+
 Here we are looking for product solutions of the form $\psi(x, t)=u(x) T(t)$, where $T$ is given by (8). From (7), we get the equation for $u$
 
 $$
 -\frac{\hbar^{2}}{2 \mu} u^{\prime \prime}+V(x) u=E u
-$$
-
-where $E$ is a separation constant. Equation (12) can be put in the SturmLiouville form ((1), Section 6.2)
+\tag{12}
+$$
+
+where $E$ is a separation constant. Equation (12) can be put in the Sturm-Liouville form ((1), Section 14.2)
 
 $$
 u^{\prime \prime}+[q(x)+\lambda] u=0
+\tag{13}
 $$
 
 where
 
 $$
 q(x)=-\frac{2 \mu}{\hbar^{2}} V(x), \quad \lambda=\frac{2 \mu E}{\hbar^{2}} .
-$$
-
-The set of admissible values of $E$ is called the spectrum. Since in most applications we are interested in solving (13) on the infinite interval ( $-\infty, \infty$ ). the Sturm-Liouville problem will be singular, in general (see Section 6.2 for the terminology). We can appeal to results from Section 6.2 to obtain properties of the solutions of (13). In the notation of that section, $r(x)=1$ in (13). Thus, according to Theorem 2, Section 6.2, the solutions will be orthogonal with respect to the weight function $r(x)=1$ on the interval $(-\infty, \infty)$. Beyond this nothing else can be guaranteed. The spectrum of (13) may be discrete as described by Theorem 1, Section 6.2. It may be continuous (for example, it may consist of all $\lambda \geq 0$, or all $\lambda \leq 0$ ). Or, it may be partly discrete and partly continuous.
-
-Most applications in this chapter involve a Schrödinger equation with discrete spectrum: $E_{1}, E_{2}, E_{3}, \ldots$. Denote the corresponding solutions of (13) by $u_{1}, u_{2}, u_{3}, \ldots$. By superposing product solutions, the general solution of (10)-(11) becomes
-
-$$
-\psi(x, t)=\sum_{n=1}^{\infty} A_{n} e^{-i E_{n} t / \hbar} u_{n_{0}}(x),
+\tag{14}
+$$
+
+The energy spectrum includes discrete eigenvalues and, when present, continuous spectral values; the latter need not have normalizable eigenfunctions. Since in most applications we are interested in solving (13) on the infinite interval ( $-\infty, \infty$ ). the Sturm-Liouville problem will be singular, in general (see Section 14.2 for the terminology). We can appeal to results from Section 14.2 to obtain properties of the solutions of (13). In the notation of that section, $r(x)=1$ in (13). For square-integrable eigenfunctions of distinct energies satisfying the self-adjoint endpoint conditions, the boundary-form orthogonality result in Section 14.2 makes the eigenfunctions orthogonal with respect to the weight function $r(x)=1$ on the interval $(-\infty, \infty)$. Beyond this nothing else can be guaranteed. The spectrum of (13) may be discrete as described by Theorem 1, Section 14.2. It may be continuous (for example, it may consist of all $\lambda \geq 0$, or all $\lambda \leq 0$ ). Or, it may be partly discrete and partly continuous.
+
+Most applications in this chapter involve a Schrödinger equation with discrete spectrum: $E_{1}, E_{2}, E_{3}, \ldots$. Denote the corresponding solutions of (13) by $u_{1}, u_{2}, u_{3}, \ldots$. If these eigenfunctions form a complete orthogonal basis for the initial state, superposition gives the solution of the initial-value problem as
+
+$$
+\psi(x, t)=\sum_{n=1}^{\infty} A_{n} e^{-i E_{n} t / \hbar} u_n(x),
+\tag{15}
 $$
 
 where
 
 $$
 \psi(x, 0)=f(x)=\sum_{n=1}^{\infty} A_{n} u_{n}(x) .
+\tag{16}
 $$
 
 The coefficients in (16) are determined using orthogonality in the usual way,
 
 $$
-A_{n}=\int_{-\infty}^{\infty} f(x) u_{n}(x) d x / \int_{-\infty}^{\infty} u_{n}^{2}(x) d x
+A_{n}=\int_{-\infty}^{\infty} f(x)\overline{u_n(x)} d x / \int_{-\infty}^{\infty}|u_n(x)|^2 d x
 $$
 
 We illustrate these ideas with an example involving Fourier series.
 
-![](./images/68a1ca9d-3a11-44bb-a7dd-ac2482ab3577-06_435_468_752_70.jpg)
-Figure 2 Infinite square well potential.
-
-## EXAMPLE 1 The infinite square well
-
-The wave function for a small particle confined to move freely inside an interval $[0, L]$ satisfies the one dimensional version of the Schrödinger equation (4) with potential
-
-$$
-V(x)= \begin{cases}0 & \text { if } 0 \leq x \leq L, \\ \infty & \text { otherwise } .\end{cases}
-$$
-
-The infinite value of the potential outside the interval $[0, L]$ represents a force of very large (infinite) magnitude that prevents the particle from bouncing outside the interval (Figure 2). Our goal is to find the wave function $\psi(x, t)$, subject to a given initial wave function
-
-$$
-\psi(x, 0)=f(x) .
-$$
-
-Clearly, the probability of finding the particle outside the interval $\left[0, L_{1}\right]$ is 0 . Thus, $\psi(x, t)=0$ for $x<0$ or $x>L$. For $0 \leq x \leq L$, the time-independent Schrödinger equation (7) becomes
+```scientific-figure
+id: 098853b4-f2f4-400a-a661-9df71ecb89f9
+numbered: false
+title: ""
+caption: Figure 2 Infinite square well potential.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 15 An Introduction to Quantum Mechanics/images/68a1ca9d-3a11-44bb-a7dd-ac2482ab3577-06_435_468_752_70.jpg
+    caption: ""
+```
+
+
+> [!exercise|53dc86d5-570a-5c53-9a10-74ecc888f538.local at=c5b9430a-9ef8-55b9-aab0-e229cbbc3690] EXAMPLE 1 The infinite square well
+> The wave function for a small particle confined to move freely inside an interval $[0, L]$ satisfies the one dimensional version of the Schrödinger equation (4) with potential
+>
+> $$
+> V(x)= \begin{cases}0 & \text { if } 0 \leq x \leq L, \\ \infty & \text { otherwise } .\end{cases}
+> $$
+>
+> The infinite value of the potential outside the interval $[0, L]$ represents a force of very large (infinite) magnitude that prevents the particle from bouncing outside the interval (Figure 2). Our goal is to find the wave function $\psi(x, t)$, subject to a given initial wave function
+>
+> $$
+> \psi(x, 0)=f(x) .
+> $$
+
+*Printed equation label: (17).*
+
+##### solution
+
+Clearly, the probability of finding the particle outside the interval $[0,L]$ is 0 . Thus, $\psi(x, t)=0$ for $x<0$ or $x>L$. For $0 \leq x \leq L$, the time-independent Schrödinger equation (7) becomes
 
 $$
 -\frac{\hbar^{2}}{2 \mu} \frac{d^{2} u}{d x^{2}}=E u \quad \text { or } \quad \frac{d^{2} u}{d x^{2}}=-\frac{2 \mu E}{\hbar^{2}} u, \quad 0<x<L
@@ -206,13 +258,14 @@
 Note that, outside $[0, L] . u$ must be 0 , since $\psi(x, t)=u(x) T(t)$, and $T$ does not vanish, by (8). If $E=0$, then $u(x)=a x+b$. If $E<0$, then
 
 $$
-u(x)=a c^{\lambda x}+b e^{-\lambda x}, \quad \text { where } \lambda=\sqrt{-\frac{2 \mu E}{h^{2}}} .
+u(x)=a e^{\lambda x}+b e^{-\lambda x}, \quad \text { where } \lambda=\sqrt{-\frac{2 \mu E}{\hbar^{2}}} .
 $$
 
 Finally, if $E>0$, then
 
 $$
 u(x)=a \cos \lambda x+b \sin \lambda x, \quad \text { where } \lambda=\sqrt{\frac{2 \mu E}{\hbar^{2}}} .
+\tag{18}
 $$
 
 At this point, we have to decide which functions to allow as solutions. As you recall, when applying the separation of variables method, you used boundary conditions to rule out certain solutions. Here, we will use the plausible condition that $u(x)$ must be continuous. Since it has to vanish at $x=0$ and $x=L$ (recall that $u$
@@ -246,105 +299,131 @@
 b_{n}=\frac{2}{L} \int_{0}^{L} f(x) \sin \frac{n \pi}{L} x d x, \quad n=1,2, \ldots
 $$
 
-(See (3), (4), Section 2.4.) Collecting results, we obtain the wave function
-
-$$
-\psi(x, t)= \begin{cases}\sum_{n=1}^{\infty} b_{n} \sin \frac{n \pi}{L} x e^{-i E_{n} t / h}, & \text { if } 0 \leq x \leq L \\ 0 & \text { if } x<0 \text { or } x>L\end{cases}
+(See (3), (4), Section 7.4.) Collecting results, we obtain the wave function
+
+$$
+\psi(x, t)= \begin{cases}\sum_{n=1}^{\infty} b_{n} \sin \frac{n \pi}{L} x e^{-i E_{n} t / \hbar}, & \text { if } 0 \leq x \leq L \\ 0 & \text { if } x<0 \text { or } x>L\end{cases}
 $$
 
 where $b_{n}$ and $E_{n}$ are as above.
 
-## Exercises 11.1
-
-1. Derive (6) and (7) from (4).
-2. Determine the constant $A$ so as to normalize $\psi$.
-(a) $\psi(x)=A e^{-x^{2}}$.
-(b) $\psi(x, y)=A e^{-\left(x^{2}+y^{2}\right)}$.
-(c) $\psi(x)= \begin{cases}A e^{2 i x} x(1-x) & \text { if } 0<x<1, \\ 0 & \text { otherwise } .\end{cases}$
-3. Experimenting with Example 1. At time $t=0$, a particle in the infinite square well (with $L=1$ ) is represented by the wave function $\psi(x, 0)=f(x)= A x(1-x)$, for $0 \leq x \leq 1$. In what follows take $\frac{\hbar}{2 \mu}=1$.
-(a) Find the value of $A$ that normalizes $f$.
-(b) What is the probability of finding the particle in the interval $[0,1 / 2]$ at time $t=0$ ?
-(c) What is the wave function that represents this particle?
-
-Project Problem: The quantum harmonic oscillator. This project requires a knowledge of Hermite's differential equation from Section 15.4. Let us recall from classical mechanics the model of an undamped spring-mass system. Let $m$ denote the mass of the system and $k$ denote the spring constant. From Hooke's law, the restoring force is $F=-k x$. Hence from Newton's second law of motion we have $m \frac{d^{2} x}{d t^{2}}=-k x$. (The potential in this case is $V(x)=\frac{1}{2} k x^{2}$.) Solving the differential equation, we obtain $x(t)=A e^{i \omega t}+B e^{-i \omega t}$, where $\omega=\sqrt{\frac{k}{m}}$, and $A$ and $B$ are constants that can be determined from the initial conditions of the spring-mass system.
-
-Now let us turn to the quantum harmonic oscillator, which is the quantum mechanical analog of the spring-mass system. This models the small vibrations of a particle of mass $\mu$ moving along the $x$-axis under the influence of a restoring force given by a potential $V(x)=\frac{1}{2} \kappa x^{2}$. In this case, Schrödinger's equation (4) becomes
-
-$$
-i \hbar \frac{\partial \psi}{\partial t}=-\frac{\hbar^{2}}{2 \mu} \frac{\partial^{2}}{\partial x^{2}} \psi+\frac{1}{2} \kappa x^{2} \psi,
-$$
-
-where $\psi=\psi(x, t)$ is the unknown wave function. We will be interested in solving this equation given an initial wave function
-
-$$
-\psi(x, 0)=f(x)
-$$
-
-The separated equations consist now of (6) and the one dimensional time-independent Schrödinger equation
-
-$$
--\frac{\hbar^{2}}{2 \mu} u^{\prime \prime}+\frac{1}{2} \kappa x^{2} u=E u
-$$
-
-This equation is obtained from (7) by using $V(x)=\frac{1}{2} \kappa x^{2}$. In solving (21), we will require that the solutions be normalizable. Our next step is to show a connection to Hermite's differential equation ((1), Section 15.4).
-
-## 4. Hermite functions.
-
-(a) Show that the substitution $\phi(x)=e^{-\frac{x^{2}}{2}} y(x)$ transforms Hermite's equation
-(1), Section 15.4, into $\phi^{\prime \prime}+\left(2 n+1-x^{2}\right) \phi=0,-\infty<x<\infty$.
-(b) Conclude that the solutions of the equation in (a) are $\varphi_{n}(x)=e^{-\frac{x^{2}}{2}} H_{n}(x)$, $n=0,1,2, \ldots$. These are called Hermite functions.
-(c) Show that $\int_{-\infty}^{\infty} \phi_{m}(x) \phi_{n}(x) d x=0$ for $m \neq n$. [Hint: Theorem 1, Section 15.4.]
-(d) Show that $\int_{-\infty}^{\infty}\left[\phi_{m}(x)\right]^{2} d x=2^{n} n!\sqrt{\pi}$. Hence the Hermite functions are square integrable on $(-\infty, \infty)$ and tend to 0 at infinity. [Hint: Theorem 1, Section 15.4.]
-
-In closing, we note that it can be shown that the differential equation $\phi^{\prime \prime}+ \left(\lambda-x^{2}\right) \phi=0$ admits normalizable solutions on the interval $(-\infty, \infty)$ only when $\lambda=2 n+1, n=0,1,2, \ldots$. In this case, as we just saw, the solutions are constant multiples of the Hermite functions.
-5. (a) Returning to (21), show that the change of variables $x=\sqrt{\frac{h}{\mu \omega}} s$, where $\kappa=\mu \omega^{2}$, transforms the equation into
-
-$$
-\frac{d^{2} u}{d s^{2}}+\left(\frac{2 E}{\hbar \omega}-s^{2}\right) u=0
-$$
-
-(b) Using Exercise 4, conclude that the normalizable solutions of (21) occur when
-
-$$
-E=E_{n}=\hbar \omega\left(n+\frac{1}{2}\right), \quad n=0,1,2, \ldots .
-$$
-
-To each $E_{n}$ we have the solution
-
-$$
-u_{n}(. x)=e^{-\frac{\mu \omega x^{2}}{2 \hbar}} H_{n}\left(\sqrt{\frac{\mu \omega}{\hbar}} x\right), \quad n=0,1,2, \ldots
-$$
-
-## 6. Hermite series solution of the quantum harmonic oscillator
-
-(a) Show that the product solutions of (19) are
-
-$$
-\psi_{n}(x, t)=A_{n} e^{-i E_{n} t / \hbar} e^{-\frac{\mu \omega x^{2}}{2 \hbar}} H_{n}\left(\sqrt{\frac{\mu \omega}{\hbar}} x\right) .
-$$
-
-(b) Using the result of Exercise 4, show that the solution of (19) and (20) is
-
-$$
-\psi(x, t)=e^{-\frac{\mu \omega x^{2}}{2 n}} \sum_{n=0}^{\infty} A_{n} e^{-i E_{n} t / h} H_{n}\left(\sqrt{\frac{\mu \omega}{\hbar}} x\right),
-$$
-
-where
-
-$$
-A_{n}=\sqrt{\frac{\mu \omega}{\hbar}} \frac{1}{2^{n} n!\sqrt{\pi}} \int_{-\infty}^{\infty} f(x) e^{-\frac{\mu \omega x^{2}}{2 \hbar}} H_{n}\left(\sqrt{\frac{\mu \omega}{\hbar}} x\right) d x
-$$
-
-7. In this problem, we take $\frac{\mu \omega}{\hbar}=1$ and consider the initial value problem (19)-(20) with initial wave function
-
-$$
-f(x)=A e^{-\frac{x^{2}}{2}}
-$$
-
-(a) Normalize $f(x)$.
-(b) Approximate the probability of finding the oscillator in the interval $[-1,1]$.
-(c) Find the wave function.
-(d) What is the probability density for position? (Note that it is independent of time.)
-(e) Approximate the probability of finding the oscillator in the interval $[-1,1]$ at time $t=1$.
-f) Approximate the value of $a$ so that, at $t=1$, the probability of finding the oscillator in $[-a, a]$ is at least $90 \%$.
-8. Repeat Exercise 7 with $f(x)=A e^{-\frac{x^{2}}{2}}[1+\sqrt{2} x]$. (In contrast with the previous exercise, the probability density in (d) is not independent of time.)
+## Exercises 15.1
+
+
+> [!exercise|7e67cad2-73ca-51a9-85a9-5fad843b43d9.local at=d5e46e16-9732-56cc-bb61-9a225f049dcc] Exercise 1
+> Derive (6) and (7) from (4).
+
+
+> [!exercise|0562d828-fd75-5e4e-929b-9f616f4e7a97.local at=7faab3ab-9974-5420-8eb6-d76478930d94] Exercise 2
+> Determine the constant $A$ so as to normalize $\psi$.
+> (a) $\psi(x)=A e^{-x^{2}}$.
+> (b) $\psi(x, y)=A e^{-\left(x^{2}+y^{2}\right)}$.
+> (c) $\psi(x)= \begin{cases}A e^{2 i x} x(1-x) & \text { if } 0<x<1, \\ 0 & \text { otherwise } .\end{cases}$
+
+
+> [!exercise|517202c7-2dec-5143-b0c3-0bc8d034e711.local at=b03a0802-ff33-54e8-b45e-6e497f11d642] Exercise 3
+> Experimenting with Example 1. At time $t=0$, a particle in the infinite square well (with $L=1$ ) is represented by the wave function $\psi(x, 0)=f(x)= A x(1-x)$, for $0 \leq x \leq 1$. In what follows take $\frac{\hbar}{2 \mu}=1$.
+> (a) Find the value of $A$ that normalizes $f$.
+> (b) What is the probability of finding the particle in the interval $[0,1 / 2]$ at time $t=0$ ?
+> (c) What is the wave function that represents this particle?
+
+
+> [!prompt|993702f0-7cdc-5c0f-94a4-d5aacf9dc323.local at=648a0ff9-8396-5170-9313-c8a93e2d5d79] Shared exercise instructions
+> Project Problem: The quantum harmonic oscillator. This project requires a knowledge of Hermite's differential equation from Section 15.4. Let us recall from classical mechanics the model of an undamped spring-mass system. Let $m$ denote the mass of the system and $k$ denote the spring constant. From Hooke's law, the restoring force is $F=-k x$. Hence from Newton's second law of motion we have $m \frac{d^{2} x}{d t^{2}}=-k x$. (The potential in this case is $V(x)=\frac{1}{2} k x^{2}$.) Solving the differential equation, we obtain $x(t)=A e^{i \omega t}+B e^{-i \omega t}$, where $\omega=\sqrt{\frac{k}{m}}$, and $A$ and $B$ are constants that can be determined from the initial conditions of the spring-mass system.
+>
+> Now let us turn to the quantum harmonic oscillator, which is the quantum mechanical analog of the spring-mass system. This models the small vibrations of a particle of mass $\mu$ moving along the $x$-axis under the influence of a restoring force given by a potential $V(x)=\frac{1}{2} \kappa x^{2}$. In this case, Schrödinger's equation (4) becomes
+>
+> $$
+> i \hbar \frac{\partial \psi}{\partial t}=-\frac{\hbar^{2}}{2 \mu} \frac{\partial^{2}}{\partial x^{2}} \psi+\frac{1}{2} \kappa x^{2} \psi,
+> $$
+>
+> where $\psi=\psi(x, t)$ is the unknown wave function. We will be interested in solving this equation given an initial wave function
+>
+> $$
+> \psi(x, 0)=f(x)
+> $$
+>
+> The separated equations consist now of (6) and the one dimensional time-independent Schrödinger equation
+>
+> $$
+> -\frac{\hbar^{2}}{2 \mu} u^{\prime \prime}+\frac{1}{2} \kappa x^{2} u=E u
+> $$
+>
+> This equation is obtained from (7) by using $V(x)=\frac{1}{2} \kappa x^{2}$. In solving (21), we will require that the solutions be normalizable. Our next step is to show a connection to Hermite's differential equation ((1), Section 15.4).
+
+*Printed equation labels: (19) time-dependent harmonic-oscillator equation; (20) initial wave function; (21) stationary harmonic-oscillator equation.*
+
+
+> [!exercise|bb625381-c866-5484-b179-73975a7e0585.local at=81750910-f986-5a20-85a8-35ecf02ff908] Exercise 4
+> Hermite functions.
+>
+> (a) Show that the substitution $\phi(x)=e^{-\frac{x^{2}}{2}} y(x)$ transforms Hermite's equation
+> (1), Section 15.4, into $\phi^{\prime \prime}+\left(2 n+1-x^{2}\right) \phi=0,-\infty<x<\infty$.
+> (b) Conclude that the solutions of the equation in (a) are $\varphi_{n}(x)=e^{-\frac{x^{2}}{2}} H_{n}(x)$, $n=0,1,2, \ldots$. These are called Hermite functions.
+> (c) Show that $\int_{-\infty}^{\infty} \phi_{m}(x) \phi_{n}(x) d x=0$ for $m \neq n$. [Hint: Theorem 1, Section 15.4.]
+> (d) Show that $\int_{-\infty}^{\infty}\left[\phi_n(x)\right]^2 d x=2^{n} n!\sqrt{\pi}$. Hence the Hermite functions are square integrable on $(-\infty, \infty)$ and tend to 0 at infinity. [Hint: Theorem 1, Section 15.4.]
+
+
+ It can be shown that the differential equation $\phi^{\prime \prime}+ \left(\lambda-x^{2}\right) \phi=0$ admits normalizable solutions on the interval $(-\infty, \infty)$ only when $\lambda=2 n+1, n=0,1,2, \ldots$. In this case, as we just saw, the solutions are constant multiples of the Hermite functions.
+
+> [!exercise|f731a105-3679-5eec-a709-aec8e371a602.local at=4100d6eb-9d65-5319-a97f-45d724302b34] Exercise 5
+> (a) Returning to (21), show that the change of variables $x=\sqrt{\frac{\hbar}{\mu \omega}} s$, where $\kappa=\mu \omega^{2}$, transforms the equation into
+>
+> $$
+> \frac{d^{2} u}{d s^{2}}+\left(\frac{2 E}{\hbar \omega}-s^{2}\right) u=0
+> $$
+>
+> (b) Using Exercise 4, conclude that the normalizable solutions of (21) occur when
+>
+> $$
+> E=E_{n}=\hbar \omega\left(n+\frac{1}{2}\right), \quad n=0,1,2, \ldots .
+> $$
+>
+> To each $E_{n}$ we have the solution
+>
+> $$
+> u_n(x)=e^{-\frac{\mu \omega x^{2}}{2 \hbar}} H_{n}\left(\sqrt{\frac{\mu \omega}{\hbar}} x\right), \quad n=0,1,2, \ldots
+> $$
+
+*Printed equation label: (22).*
+
+
+> [!exercise|ece3f293-05e0-5d99-a8f0-3f7caabde61b.local at=64d7371d-1ca9-5f17-88c1-6c8c0c290139] Exercise 6
+> Hermite series solution of the quantum harmonic oscillator
+>
+> (a) Show that the product solutions of (19) are
+>
+> $$
+> \psi_{n}(x, t)=A_{n} e^{-i E_{n} t / \hbar} e^{-\frac{\mu \omega x^{2}}{2 \hbar}} H_{n}\left(\sqrt{\frac{\mu \omega}{\hbar}} x\right) .
+> $$
+>
+> (b) Using the result of Exercise 4, show that the solution of (19) and (20) is
+>
+> $$
+> \psi(x, t)=e^{-\frac{\mu \omega x^{2}}{2 \hbar}} \sum_{n=0}^{\infty} A_{n} e^{-i E_{n} t / \hbar} H_{n}\left(\sqrt{\frac{\mu \omega}{\hbar}} x\right),
+> $$
+>
+> where
+>
+> $$
+> A_{n}=\sqrt{\frac{\mu \omega}{\hbar}} \frac{1}{2^{n} n!\sqrt{\pi}} \int_{-\infty}^{\infty} f(x) e^{-\frac{\mu \omega x^{2}}{2 \hbar}} H_{n}\left(\sqrt{\frac{\mu \omega}{\hbar}} x\right) d x
+> $$
+
+
+> [!exercise|bdc3784c-e9cb-5e67-a006-7a0ef7ee6a73.local at=15ffe4d2-a52b-5b3f-a2cb-eabc43649c6e] Exercise 7
+> In this problem, we take $\frac{\mu \omega}{\hbar}=1$ and consider the initial value problem (19)-(20) with initial wave function
+>
+> $$
+> f(x)=A e^{-\frac{x^{2}}{2}}
+> $$
+>
+> (a) Normalize $f(x)$.
+> (b) Approximate the probability of finding the oscillator in the interval $[-1,1]$.
+> (c) Find the wave function.
+> (d) What is the probability density for position? (Note that it is independent of time.)
+> (e) Approximate the probability of finding the oscillator in the interval $[-1,1]$ at time $t=1$.
+> (f) Approximate the value of $a$ so that, at $t=1$, the probability of finding the oscillator in $[-a, a]$ is at least $90 \%$.
+
+
+> [!exercise|ed0159d3-cba0-55c5-92f1-00ff5d8d471f.local at=87dace2e-6a70-5a41-bd84-e1d47a30dd5d] Exercise 8
+> Repeat Exercise 7 with $f(x)=A e^{-\frac{x^{2}}{2}}[1+\sqrt{2} x]$. (In contrast with the previous exercise, the probability density in (d) is not independent of time.)

`````
