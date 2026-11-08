
# Chapter 12 Partial Differential Equations in Polar and Cylindrical Coordinates

## Topics to Review

Fourier series (Sections 7.1-7.4) and the separation of variables method (Section 11.3) are crucial in this chapter. Section 12.1 is self-contained. It presents the Laplacian in polar, cylindrical, and spherical coordinates. Sections 12.2 and 12.3 deal with the vibrating circular membrane. These require knowledge of Bessel functions (Sections 12.7, 12.8) and Fourier series. Section 12.4 requires Fourier series. For Section 12.5, further properties of Bessel functions from Sections 12.7 and 12.8 are needed. Section 12.6 develops the eigenfunction expansions method on the disk. For this section, it is recommended to review the material of Section 11.9.

## Looking Ahead

You recall from Section 11.6 how by varying the boundary conditions we were led to new types of series expansions. In this chapter we will solve boundary value problems over circular and cylindrical domains. It should not surprise you that the solutions will entail new series expansions; for example, Bessel series. These series look quite complicated at first, but with the help of a computer system, you will be able to plot them and see that they behave very much like Fourier series. The ideas of this chapter will be developed further in Chapter 13, where we will consider problems in spherical coordinates, giving rise to new families of special functions.

## Introduction

> One cannot understand … the universality of laws of nature, the relationship of things, without an understanding of mathematics. There is no other way to do it.
> — Richard P. Feynman

In the previous chapter we used our knowledge of Fourier series to solve several interesting boundary value problems by the method of separation of variables. The success of our method depended to a large extent on the fact that the domains under consideration were easily described in Cartesian coordinates. In this chapter we address problems where the domains are easily described in polar and cylindrical coordinates. Specifically, we consider boundary value problems for the wave, heat, Laplace, and Poisson equations over disks or cylinders. Upon restating these problems in suitable coordinate systems and separating variables, we will encounter new ordinary differential equations, Bessel's equation, whose solutions are called Bessel functions. The full implementation of the separation of variables method will lead us to study expansions of functions in terms of Bessel functions in ways analogous to Fourier series expansions.

You do not need to know about Bessel series to start the chapter. As needed, we will refer to Sections 12.7 and 12.8, where you will find a comprehensive treatment of these special series expansions. Section 12.9 contains mostly proofs of interesting properties of Bessel functions, with surprising connections to Fourier series. This section can be omitted without affecting the rest of the chapter.

## Sections

[[Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 12 Partial Differential Equations in Polar and Cylindrical Coordinates/12.1 The Laplacian in Various Coordinate Systems|12.1 The Laplacian in Various Coordinate Systems]]

[[Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 12 Partial Differential Equations in Polar and Cylindrical Coordinates/12.2 Vibrations of a Circular Membrane: Symmetric Case|12.2 Vibrations of a Circular Membrane: Symmetric Case]]

[[Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 12 Partial Differential Equations in Polar and Cylindrical Coordinates/12.3 Vibrations of a Circular Membrane: General Case|12.3 Vibrations of a Circular Membrane: General Case]]

[[Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 12 Partial Differential Equations in Polar and Cylindrical Coordinates/12.4 Laplace's Equation in Circular Regions|12.4 Laplace's Equation in Circular Regions]]

[[Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 12 Partial Differential Equations in Polar and Cylindrical Coordinates/12.5 Laplace's Equation in a Cylinder|12.5 Laplace's Equation in a Cylinder]]

[[Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 12 Partial Differential Equations in Polar and Cylindrical Coordinates/12.6 The Helmholtz and Poisson Equations|12.6 The Helmholtz and Poisson Equations]]

[[Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 12 Partial Differential Equations in Polar and Cylindrical Coordinates/12.7 Bessel's Equation and Bessel Functions|12.7 Bessel's Equation and Bessel Functions]]

[[Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 12 Partial Differential Equations in Polar and Cylindrical Coordinates/12.8 Bessel Series Expansions|12.8 Bessel Series Expansions]]

[[Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 12 Partial Differential Equations in Polar and Cylindrical Coordinates/12.9 Integral Formulas and Asymptotics for Bessel Functions|12.9 Integral Formulas and Asymptotics for Bessel Functions]]
