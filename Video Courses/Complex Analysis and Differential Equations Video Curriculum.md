# Complex Analysis and Differential Equations Video Curriculum

This note organizes a collection of video lecture series into a coherent curriculum modeled on Nakhlé H. Asmar's broad program: rigorous complex analysis followed by Fourier methods, differential equations, integral transforms, special functions, boundary-value problems, and Green functions. No single available video course reproduces the entire book chapter by chapter. The most effective replacement is therefore a carefully staged sequence in which each course has a distinct role.

## Recommended core sequence

The most coherent route through the material is:

1. **Jiří Lebl - Cultivating Complex Analysis** for a rigorous first course in complex analysis.
2. **Jason Bramburger - Partial Differential Equations** for Fourier series, separation of variables, classical PDEs, Sturm-Liouville problems, and eigenfunction expansions.
3. **Sarthok Sircar - Integral Transforms and Their Applications**, especially Weeks 1-5, for systematic Fourier, Laplace, Hankel, and Mellin transform methods.
4. **Auditya Sharma - Mathematical Methods in Physics 2**, selectively, for Legendre functions, Bessel functions, spherical coordinates, and Green-function methods.
5. **V. Balakrishnan - Selected Topics in Mathematical Physics**, especially Lectures 18-33, to consolidate transforms and PDEs through the operator and Green-function viewpoint.

After this core, use **Alex Kontorovich** for a bridge from complex analysis to Fourier analysis and special functions, and use **T. E. Venkata Balaji, Parts I and II**, for a deeper continuation in pure one-variable complex analysis.

---

## I. Rigorous complex-analysis foundation

### Jiří Lebl - Cultivating Complex Analysis

**Role:** Primary foundational course and the recommended starting point.

**Video series:** [Cultivating Complex Analysis - YouTube playlist](https://www.youtube.com/playlist?list=PLRfQb6m35rf5vZaOlSXVmt0hgJepfEqCw)

**Course materials:** [Oklahoma State University Math 5283 course page](https://math.okstate.edu/people/lebl/osu5283-s22/)

Lebl's series is designed as a coherent, proof-oriented first graduate course rather than a collection of computational techniques. It begins with the topology and geometry of the complex plane and develops holomorphic functions, Cauchy's theorem and integral formula, zeros and singularities, meromorphic functions, maximum principles, normal families, the Riemann mapping theorem, and harmonic functions.

The strongest reason to use this as the main course is its integration with a freely available textbook and a large body of exercises. The exposition is deliberate and self-contained, and the course materials supply much of the metric-space and real-analysis background needed to follow the proofs. The videos use slides rather than a traditional blackboard, but the sequence is considerably more systematic than most YouTube treatments.

This course corresponds most closely to Asmar's Chapters 1-6. It should be treated as the actual complex-analysis course, with Asmar used alongside it for applications and additional exercises.

### Pranav Haridas - Complex Analysis

**Role:** Slower alternative first course from the ground up.

**Video series:** [Complex Analysis - YouTube playlist](https://www.youtube.com/playlist?list=PLyqSpQzTE6M_fDgY78f5lAT5zR6xHAajo)

Haridas develops a conventional rigorous first course beginning with the complex field and the topology of the complex plane. The sequence proceeds through holomorphic functions, Cauchy theory, singularities, residues, maximum principles, branches of the logarithm, and more advanced consequences such as Picard-type results.

This is a good alternative when Lebl feels too compressed or when a slower construction from first principles is desirable. It is systematic and mathematically serious, although less ambitious overall than Lebl's graduate treatment. It should normally replace Lebl rather than be watched in full in addition to it.

### Richard Borcherds - Complex Analysis

**Role:** Compact conceptual introduction, rapid review, or alternate explanation.

**Video series:** [Complex Analysis - YouTube playlist](https://www.youtube.com/playlist?list=PL8yHsr3EFj537_iYA5QrvwhvMlpkJ1yGN)

Borcherds presents a concise undergraduate introduction covering complex arithmetic and elementary functions, holomorphic and harmonic functions, contour integration, Cauchy theory, Laurent series, singularities, residues, analytic continuation, conformal ideas, and short introductions to the gamma and zeta functions.

The series is unusually effective at isolating the main structural idea behind a topic. Its brevity makes it valuable as a preparatory pass before Lebl, a review after time away from the subject, or a source of alternate explanations. It is not a replacement for a full graduate course because it has much less time for proofs, exercises, and systematic development.

### Steven J. Miller - Complex Analysis, Math 372

**Role:** Fast, proof-intensive alternate first course.

**Video series:** [Complex Analysis Math 372 - Steven Miller - YouTube playlist](https://www.youtube.com/playlist?list=PL71JUoXcec_mmLm9psjMKo1FYBXS9WHb7)

**Course document:** [Williams College Math 372 syllabus and course information](https://web.williams.edu/Mathematics/sjmiller/public_html/372Fa17/MATH372Welcome.pdf)

Miller's Williams College course follows Stein and Shakarchi's *Complex Analysis* and moves at a demanding classroom pace. It emphasizes proof strategy, problem solving, and the connections between complex analysis, number theory, and mathematical physics. Its principal subjects include real-analysis preliminaries, Cauchy theory, meromorphic functions, logarithms, selected topics on entire functions, and conformal mapping.

This is especially useful for strengthening proof fluency or preparing for graduate mathematics. The course is less convenient for independent study than Lebl because the pace is faster, the coverage of its reference text is selective, and the video quality is older. Use it as an alternate full course or as a source of demanding supplementary lectures.

### MIT 18.04 - Complex Variables with Applications

**Role:** Applied companion for engineering, PDEs, and mathematical physics.

**Video course and materials:** [MIT OpenCourseWare: Complex Variables with Applications](https://ocw.mit.edu/courses/18-04-complex-variables-with-applications-spring-2018/)

MIT 18.04 emphasizes the parts of complex analysis that transfer most directly to applied mathematics: contour integration, harmonic functions, two-dimensional potential and fluid flow, conformal mapping, evaluation of real integrals, and Fourier and Laplace transform methods. Its notes, recitations, problem sets, and solutions are particularly valuable.

This is not the best sole source for a proof-based graduate course, but it is an excellent companion to Lebl. It helps connect Asmar's early complex-analysis chapters to the later material on Laplace's equation, Green functions, transforms, and boundary-value problems.

### Steve Brunton - Engineering Math: Crash Course in Complex Analysis

**Role:** Physical motivation and rapid computational review.

**Video series:** [Engineering Math: Crash Course in Complex Analysis - YouTube playlist](https://www.youtube.com/playlist?list=PLMrJAkhIeNNQBRslPb7I0yTnES981R8Cg)

Brunton's compact series is oriented toward engineers and applied scientists. It emphasizes visualization, physical motivation, computational intuition, and the rapid use of complex-variable methods. It is helpful before a more rigorous course or when reviewing techniques for an applied problem.

Because it is explicitly a crash course, it does not develop the standard theory with the completeness of Lebl, Haridas, or Miller. It should be treated as a supplement, not as the primary education in complex analysis.

### Michael Penn / MathMajor - Complex Analysis

**Role:** Worked examples and computational reinforcement.

**Video series:** [Complex Analysis - MathMajor - YouTube playlist](https://www.youtube.com/playlist?list=PLJp-g8uP8qlakkdOFIW2PlufApJWFxO-U)

Penn's numbered lecture sequence begins with complex arithmetic, polar form, and visualization of complex functions before moving into analyticity, Cauchy theory, contour integration, and residue methods. His explanations are accessible and particularly useful for calculations and worked examples.

The series substantially overlaps the introductory material covered more systematically by Lebl, Borcherds, and Haridas. Its best use in this curriculum is as a lookup resource whenever another presentation is needed or when additional computational examples would make an abstract result more concrete.

---

## II. Advanced complex analysis and the bridge to Fourier analysis

### Alex Kontorovich - Rutgers Math 503: Complex Analysis

**Role:** Advanced bridge connecting complex analysis with Fourier analysis, integral transforms, special functions, and analytic number theory.

**Video series:** [Rutgers Math 503 Complex Analysis - YouTube playlist](https://www.youtube.com/playlist?list=PLVMgvCDIRy1wzJcFNGw7t4tehgzhFtBpm)

**Lecture notes and assignments:** [Rutgers Math 503 course page](https://sites.math.rutgers.edu/~alexk/2020F503/lectures.html)

Kontorovich's graduate course begins with Cauchy theory, residues, analytic continuation, the argument principle, complex logarithms, harmonic functions, and conformal mapping. It then extends well beyond an ordinary first course into Fourier series and transforms, Poisson summation, the Paley-Wiener theorem, Phragmén-Lindelöf theory, Montel's theorem, the Dirichlet problem, gamma and zeta functions, Mellin transforms, Hadamard factorization, and the prime number theorem. Additional lectures treat elliptic functions, theta functions, modularity, and elliptic curves.

This is the most useful addition to the core complex-analysis sequence because it creates a direct conceptual bridge

$$
\text{complex analysis}
\longleftrightarrow
\text{Fourier analysis}
\longleftrightarrow
\text{integral transforms}
\longleftrightarrow
\text{spectral and asymptotic methods}.
$$

Rather than watching both Lebl and Kontorovich consecutively in full, use Lebl for the systematic foundation and then enter Kontorovich selectively around Fourier series, the Fourier transform, Poisson summation, Paley-Wiener theory, Mellin transforms, and special functions. The later elliptic and modular material is valuable enrichment.

### T. E. Venkata Balaji - Advanced Complex Analysis, Part I

**Role:** First advanced continuation after a rigorous introductory course.

**Video series:** [Advanced Complex Analysis, Part I - YouTube playlist](https://www.youtube.com/playlist?list=PLbMVogVj5nJTLfYTwvct_SlLaxv1b50Vk)

**Official course page:** [NPTEL Advanced Complex Analysis, Part I](https://nptel.ac.in/courses/111106084)

Part I assumes familiarity with contour integration, Taylor and Laurent series, residues, and elementary topology. It develops Rouché's and Hurwitz's theorems, the open mapping theorem, complex inverse and implicit function theorems, analytic branches, Riemann surfaces associated with multivalued functions, analytic continuation, monodromy, Schwarz-Pick theory, hyperbolic geometry, normal families, and the Riemann mapping theorem.

This is not an applied PDE supplement. Its purpose is to deepen the one-variable function theory begun in Lebl and to supply the geometric and analytic-continuation machinery expected in a serious second course.

### T. E. Venkata Balaji - Advanced Complex Analysis, Part II

**Role:** Deep advanced one-variable function theory culminating in Picard's theorems.

**Video series:** [Advanced Complex Analysis, Part II - YouTube playlist](https://www.youtube.com/playlist?list=PLEAYkSg4uSQ0g2wPbcWRFhAerDwpRbR5U)

**Official course page:** [NPTEL Advanced Complex Analysis, Part II](https://nptel.ac.in/courses/111106094)

Part II studies the Riemann sphere, singularities and residues at infinity, spherical distance and spherical derivatives, meromorphic functions as maps into the sphere, compactness of meromorphic-function families, Marty's theorem, Zalcman's lemma, Montel-type theorems, Schottky's theorem, and the small and large Picard theorems.

The Riemann-surface constructions, analytic continuation, monodromy, hyperbolic geometry, and Riemann mapping theorem occur mainly in Part I. Part II is therefore best understood as the compactness, normal-family, and value-distribution continuation of that course. It reaches substantially beyond Asmar's main complex-analysis requirements.

---

## III. Fourier series, classical PDEs, and Sturm-Liouville theory

### Jason Bramburger - Partial Differential Equations

**Role:** Main PDE course and the structural spine for the second half of the Asmar curriculum.

**Video series:** [Partial Differential Equations - YouTube playlist](https://www.youtube.com/playlist?list=PLXsDp0z6VWFQJ6BY1O6Hz5XX2ppgGvEAu)

Bramburger's course develops the derivation and interpretation of the heat, wave, and Laplace equations, then builds the classical solution machinery around them. Major topics include separation of variables, Fourier sine and cosine series, D'Alembert's method, Sturm-Liouville eigenvalue problems, eigenfunction expansions, nonhomogeneous boundary conditions, Fourier-transform solutions, and qualitative properties of PDEs.

The course is especially close to Asmar's applied style because it repeatedly follows the chain

$$
\text{physical model}
\longrightarrow
\text{initial-boundary-value problem}
\longrightarrow
\text{coordinate choice}
\longrightarrow
\text{separation of variables}
\longrightarrow
\text{eigenvalue problem}
\longrightarrow
\text{eigenfunction expansion}.
$$

It also moves beyond rectangular domains to Laplace's equation on a disk, polar-coordinate separation, circular membranes, Bessel functions and Bessel-series solutions, higher-dimensional heat and wave equations, and problems with inhomogeneous data. This makes it the closest single video replacement for Asmar's chapters on Fourier series, rectangular PDEs, polar and cylindrical PDEs, and Sturm-Liouville theory.

Its principal gaps are systematic Laplace and Hankel transform theory, a full spherical-coordinate treatment, Legendre expansions and spherical harmonics, and the broader family of integral transforms. Sircar and Sharma supply those missing pieces.

---

## IV. Integral transforms

### Sarthok Sircar - Integral Transforms and Their Applications

**Role:** Systematic transform supplement and the main replacement for Asmar's transform chapters.

**Video series:** [Integral Transforms and Their Applications - YouTube playlist](https://www.youtube.com/playlist?list=PLOVXtREUtUHNVmB2hrnss_IlimYdh6nrc)

**Official course page:** [NPTEL Integral Transforms and Their Applications](https://nptel.ac.in/courses/111102129)

Sircar's course is aimed at advanced undergraduate and graduate students and applies integral transforms to ODEs, PDEs, initial-value problems, boundary-value problems, and continuum mechanics. The early part develops Fourier transforms and their operational properties, transform solutions of ODEs and PDEs, Laplace transforms and inverses, convolution, differentiation and integration rules, and transform methods for initial and boundary data. It then introduces joint Fourier-Laplace transforms, Hankel transforms for radially symmetric problems, and Mellin transforms.

For an Asmar-equivalent curriculum, Weeks 1-5 are the essential block. They cover the Fourier, Laplace, joint Fourier-Laplace, Hankel, and Mellin machinery needed for the book's classical applications. Later weeks broaden the course to Hilbert, Stieltjes, Radon, fractional, and wavelet transforms. Those later topics are optional for the immediate Asmar program, although the Hilbert transform is a particularly worthwhile extension because of its connections with causality, response functions, singular integral operators, and Fourier analysis.

---

## V. Special functions and curvilinear-coordinate PDEs

### Auditya Sharma - Mathematical Methods in Physics 2

**Role:** Targeted supplement for Legendre functions, Bessel functions, spherical coordinates, and Green functions.

**Primary video series:** [Mathematical Methods in Physics 2 - YouTube playlist](https://www.youtube.com/playlist?list=PLbJCOW-02l3-IOVGsMmV0JYmIBsI3ksLO)

**Alternative full-course mirror:** [Mathematical Methods in Physics II - YouTube playlist](https://www.youtube.com/playlist?list=PLOVXtREUtUHPYkgqrqThMQ4BoaUEPZcUp)

**Official course page:** [NPTEL Mathematical Methods in Physics 2](https://nptel.ac.in/courses/111106152)

This large course should be used selectively rather than watched from beginning to end solely for the Asmar curriculum. Its relevant special-function block develops orthogonal functions, Legendre polynomials, associated Legendre functions, Bessel functions, recurrence relations, series representations, and the differential equations from which those functions arise.

The Legendre material begins around Lectures 48-50 and continues into the associated theory. The Bessel block continues through approximately Lecture 58. The PDE block around Lectures 69-73 treats Laplace's equation in spherical coordinates, separation of radial and angular variables, the emergence of Legendre's equation, expansions in Legendre polynomials, Poisson's equation, and Green-function solutions.

These lectures complete the geometry-driven progression

$$
\begin{aligned}
\text{rectangular geometry} &\longrightarrow \text{Fourier series},\\
\text{cylindrical geometry} &\longrightarrow \text{Bessel functions},\\
\text{spherical geometry} &\longrightarrow \text{Legendre functions and spherical harmonics}.
\end{aligned}
$$

This material is particularly useful for electrostatics, diffusion around spherical objects, elasticity, scattering, multipole expansions, and continuum fields around localized sources or defects.

---

## VI. Green functions and mathematical-physics consolidation

### V. Balakrishnan - Selected Topics in Mathematical Physics

**Role:** Advanced conceptual bridge from transforms and classical PDE methods to operator inversion, Green functions, propagation, and scattering.

**Video series:** [Selected Topics in Mathematical Physics - YouTube playlist](https://www.youtube.com/playlist?list=PLbMVogVj5nJRhl_6TUGChpnt2Lg0AZvZu)

**Course syllabus:** [NPTEL Selected Topics in Mathematical Physics syllabus](https://archive.nptel.ac.in/content/syllabus_pdf/115106086.pdf)

Balakrishnan does not methodically replace a first PDE course, so it should follow Bramburger rather than precede it. The course treats Laplace and Fourier transforms, multidimensional Fourier analysis, convolution, Parseval identities, delta functions, Green functions for the Laplacian, Poisson's equation and Coulomb potentials, diffusion equations, Helmholtz Green functions, causal Green functions for wave equations, and scattering.

Lectures 18-33 form the most relevant block for this curriculum. They begin with transform methods and move into Green functions for Laplace, diffusion, Helmholtz, and wave operators. This recasts the individual solution techniques as instances of operator inversion:

$$
Lu=f
\quad\Longrightarrow\quad
u(x)=\int G(x,x')f(x')\,dx'.
$$

The course also extends beyond Asmar through multidimensional transforms, outgoing-wave conditions, the Born approximation, and the differing behavior of wave propagation across spatial dimensions. It is especially valuable for connecting the classical material to continuum mechanics, electronic structure, linear response, scattering theory, spectral methods, and mathematical physics.

---

## VII. Optional deeper Fourier analysis

### MIT - Topics in Fourier Analysis

**Role:** Later theoretical extension, not part of the minimum Asmar-equivalent route.

**Video course and materials:** [MIT OpenCourseWare: Topics in Fourier Analysis](https://ocw.mit.edu/courses/res-18-015-topics-in-fourier-analysis-spring-2024/)

This course studies Fourier analysis as a mathematical subject rather than merely as a tool for solving classical boundary-value problems. Its topics include convergence of Fourier series, transforms on $L^1$ and $L^2$, Hermite functions, and tempered distributions.

It is best taken after the core Asmar-equivalent sequence. Bramburger and Sircar first build operational fluency with eigenfunction expansions and transforms; the MIT course then supplies a deeper functional-analytic understanding of convergence, transform theory, and distributions.

---

## Correspondence with the Asmar sequence

### Asmar Chapters 1-6: complex analysis

Use Lebl as the primary course. Borcherds provides a fast conceptual pass, Haridas provides a slower alternative, Miller provides a demanding proof-intensive alternative, and MIT 18.04 supplies applied examples. Kontorovich and Balaji should follow the first course rather than replace it.

### Asmar Chapter 7: Fourier series

Use Bramburger for Fourier series as eigenfunction expansions arising naturally from PDEs. Use Kontorovich selectively for the deeper relationship between complex analysis, Fourier analysis, Poisson summation, and transform methods.

### Asmar Chapters 8-9: Fourier, Laplace, and Hankel transforms

Use Sircar, especially Weeks 1-5. Bramburger supplies the PDE motivation and operational use, while Sircar systematizes transforms, inverses, convolution, and initial- and boundary-value methods.

### Asmar Chapters 10-14: ODE review, classical PDEs, special functions, and Sturm-Liouville theory

Use Bramburger as the main course for heat, wave, Laplace, Poisson, and Helmholtz problems; separation of variables; boundary conditions; Sturm-Liouville problems; and eigenfunction expansions. Add Sharma for Bessel functions, Legendre functions, spherical harmonics, and spherical-coordinate problems.

### Asmar Chapter 16: Green functions and conformal mappings

Combine Lebl or MIT 18.04 for conformal mapping with Balakrishnan for Green functions and operator inversion. Sharma's later PDE lectures provide an additional treatment of Poisson problems and Green-function solutions in curvilinear coordinates.

### Topics not fully replaced by this collection

The collection does not supply an exact chapter-by-chapter replacement for Asmar's introduction to quantum mechanics, sampling theorem and discrete Fourier analysis, or finite-difference numerical methods. Sharma provides some of the special-function background relevant to quantum mechanics, and the MIT Fourier course supplies deeper transform theory, but dedicated courses would still be preferable for quantum mechanics, FFT-based numerical analysis, and finite-difference PDE methods.

---

## Practical viewing plan

Begin with Lebl and work problems from Asmar in parallel. After the complex-analysis foundation, move to Bramburger and let Fourier series arise in the solution of heat, wave, and Laplace problems. Study Sircar's first five weeks when transform methods begin to appear. Return to Bramburger for polar-coordinate problems and circular membranes, using Sharma's Bessel lectures when the special-function theory needs reinforcement. Then study Sharma's Legendre and spherical-coordinate blocks. Finish the core with Balakrishnan's Lectures 18-33 so that transforms, Green functions, diffusion, Helmholtz equations, wave propagation, and scattering become parts of one operator-based framework.

Kontorovich can be inserted after Lebl or alongside the transform phase, particularly from Fourier series through Mellin transforms and special functions. Balaji Parts I and II belong after the first rigorous complex-analysis course and may be studied independently of the applied PDE sequence.

