
# Chapter 13 Partial Differential Equations in Spherical Coordinates

## Topics to Review

As in the previous chapter, the separation of variables method is crucial. The other essential tools are developed as needed. Section 13.1 is self-contained. Section 13.2 refers to Sections 13.1, 13.5 and 13.6. Sections 13.3 and 13.4 refer to Sections 13.1 and 13.5-13.7. Also, in Section 13.4, Bessel functions will reappear, and the material from Section 12.8 will be used again. Prior knowledge of the eigenfunction expansions method (Sections 11.9 and 12.6) is helpful but not required for Section 13.4. The supplementary material (Sections 13.5-13.7) is self-contained and can be covered before starting the chapter. For Section 13.5 you need to review the power series method of Appendix 10.4.

## Looking Ahead

Legendre polynomials and the associated Legendre functions and their expansion theories arise frequently in physics, engineering, applied mathematics, and numerical analysis. Spherical harmonics, developed and used in Section 13.3, are also very useful in these areas. Their construction requires both Fourier series and the associated Legendre functions. As you will see in this chapter, spherical harmonics are the natural analogs of Fourier series for functions defined on the sphere. All the new functions that you will encounter in this chapter are available in most computer systems. To get acquainted with their many new features, it is strongly recommended that you experiment with them graphically and numerically with a computer.

## Introduction

> Don't just read it; fight it! Ask your own questions, look for your own examples, discover your own proofs.
> — Paul Halmos

In this chapter we turn our attention to problems in spheres and other regions, such as the region between two spheres or the region outside a sphere, for which it is natural to use spherical coordinates. For example, to find the steady-state temperature in a metallic ball whose surface is kept at a given temperature distribution, we need to solve Laplace's equation inside the ball that takes the given boundary values on its surface. These and related problems can be treated by the same techniques as in the previous two chapters; in particular, the method of separation of variables and the method of eigenfunction expansions can be applied.

You may recall from the previous chapters how Fourier series and Bessel series arose from applying the separation of variables method to equations involving the Laplacian in polar coordinates. Here, with equations involving the Laplacian in spherical coordinates, we will encounter other special functions when carrying the method of separation of variables to completion. A comprehensive treatment of this requisite material is presented in the last three sections of the chapter. It covers in detail Legendre polynomials and associated Legendre functions, and their corresponding expansion theories. You do not need to cover this material before starting the chapter; we will refer to it as needed.

## Sections

[[Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 13 Partial Differential Equations in Spherical Coordinates/13.1 Preview of Problems and Methods|13.1 Preview of Problems and Methods]]

[[Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 13 Partial Differential Equations in Spherical Coordinates/13.2 Dirichlet Problems with Symmetry|13.2 Dirichlet Problems with Symmetry]]

[[Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 13 Partial Differential Equations in Spherical Coordinates/13.3 Spherical Harmonics and the General Dirichlet Problem|13.3 Spherical Harmonics and the General Dirichlet Problem]]

[[Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 13 Partial Differential Equations in Spherical Coordinates/13.4 The Helmholtz Equation with Applications to the Poisson, Heat, and Wave Equations|13.4 The Helmholtz Equation with Applications to the Poisson, Heat, and Wave Equations]]

[[Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 13 Partial Differential Equations in Spherical Coordinates/13.5 Legendre's Differential Equation|13.5 Legendre's Differential Equation]]

[[Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 13 Partial Differential Equations in Spherical Coordinates/13.6 Legendre Polynomials and Legendre Series Expansions|13.6 Legendre Polynomials and Legendre Series Expansions]]

[[Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 13 Partial Differential Equations in Spherical Coordinates/13.7 Associated Legendre Functions and Series Expansions|13.7 Associated Legendre Functions and Series Expansions]]
