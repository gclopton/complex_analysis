
# Chapter 16 Green's Functions and Conformal Mappings

## Topics to Review

Green's theorem from calculus is required for this chapter. It is recalled and proved in Section 16.1. The chapter is intended to introduce methods for solving Laplace and Poisson equations. So Sections 11.8, 11.9, 12.4, and 8.5 are essential to appreciate this chapter. Sections 16.5 to 16.8 require familiarity with complex numbers and complex functions. The requisite material is included as a brief review in Section 16.5. Sections 16.5 and 16.6 can be covered independently of the rest of the chapter. Sections 16.7 and 16.8 are based on the preceding sections of the chapter.

## Looking Ahead

In this chapter we introduce new tools for solving Dirichlet problems and Poisson equations: Green's functions, Neumann functions, and conformal mappings. Roughly speaking, Green's function for a given region $\Omega$ is a function that depends only on $\Omega$ and that can be used to solve any Dirichlet problem or Poisson problem on $\Omega$, in the same way that the Poisson kernel on the real line can be used to solve Dirichlet problems in the upper half-plane. A conformal mapping is like a change of variables that we can use to transform a Dirichlet problem from a given region onto another region on which the problem is simpler to solve, in the same way that a change of variables can be used to transform a difficult integral.

## Introduction

> One cannot escape the feeling that these mathematical formulas have an independent existence and an intelligence of their own, that they are wiser than we are, wiser even than their discoverers, that we get more out of them than was originally put into them.
> — Heinrich Hertz

The methods of this chapter are new, but the goal is still the same: to solve boundary value problems. To motivate the results of this chapter, review the Poisson integral formula in Section 8.5. Here we will derive similar formulas that solve the Dirichlet and Neumann problems on arbitrary (simply connected) regions in the plane. Like the Poisson integral, these formulas are packed with information about the solution.

In Sections 16.1 and 16.2, we start with Green's theorem from calculus and use simple tricks like integration by parts to derive two identities, known as Green's first and second identities. We then apply these formulas to obtain important properties of solutions of Laplace's equation. In Section 16.3 we modify our formulas and introduce the amazing Green's functions. Simple manipulations with Green's functions yield formulas for the solutions of Dirichlet problems (Poisson integral-like formulas) and Poisson equations.

These remarkable formulas add to our understanding of properties of solutions of Dirichlet problems and, more important, they lead us to explore an important connection with the theory of analytic functions. Two major results are explored: the invariance of Laplace's equation by a change of variables using analytic functions (Section 16.6), and the composition of Green's functions with analytic functions (Section 16.7). The former yields the powerful method of conformal mappings, and the latter yields a nice way to compute Green's functions.

To simplify the presentation, we only discuss a sample of two dimensional problems. Many more types of problems can be treated in higher dimensions. We hope that this chapter will serve as a motivation to delve into the more advanced theories.

## Sections

[[Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 16 Green's Functions and Conformal Mappings/16.1 Green's Theorem and Identities|16.1 Green's Theorem and Identities]]

[[Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 16 Green's Functions and Conformal Mappings/16.2 Harmonic Functions and Green's Identities|16.2 Harmonic Functions and Green's Identities]]

[[Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 16 Green's Functions and Conformal Mappings/16.3 Green's Functions|16.3 Green's Functions]]

[[Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 16 Green's Functions and Conformal Mappings/16.4 Green's Functions for the Disk and the Upper Half-Plane|16.4 Green's Functions for the Disk and the Upper Half-Plane]]

[[Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 16 Green's Functions and Conformal Mappings/16.5 Analytic Functions|16.5 Analytic Functions]]

[[Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 16 Green's Functions and Conformal Mappings/16.6 Solving Dirichlet Problems with Conformal Mappings|16.6 Solving Dirichlet Problems with Conformal Mappings]]

[[Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 16 Green's Functions and Conformal Mappings/16.7 Green's Functions and Conformal Mappings|16.7 Green's Functions and Conformal Mappings]]

[[Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 16 Green's Functions and Conformal Mappings/16.8 Neumann Functions and the Solution of Neumann Problems|16.8 Neumann Functions and the Solution of Neumann Problems]]
