
# Chapter 18 Finite Difference Numerical Methods

## Topics to Review

Strictly speaking, the numerical techniques of this chapter do not require previous knowledge of partial differential equations. However, to appreciate these techniques, a familiarity with the boundary value problems of Chapter 11 is required. In particular, the analytical solutions that we developed in Sections 11.3, 11.5, 11.7, and 11.8 are useful in treating their numerical counterparts. This chapter can be covered right after Chapter 11.

## Looking Ahead...

In Section 18.1 we present the finite difference method and apply it to the heat equation. Section 18.1 is essential to the rest of the chapter. In Section 18.2 we apply the finite difference method for the wave equation, and in Section 18.3 we apply this method to Laplace's equation. Section 18.4 expands on the ideas of Section 18.3. For the sake of clarity, we chose simple problems to illustrate the numerical methods. However, you should keep in mind that these methods work equally well with more complicated problems and are very well suited for real-world applications.

## Introduction

> Numbers are intellectual witnesses that belong only to mankind.
>
> — Honoré de Balzac

Suppose that you are studying a concrete heat problem and that you want to know the temperature at times $t_{1}, t_{2}, \ldots, t_{n}$ of certain points $x_{1}, x_{2}, \ldots, x_{m}$ in a bar. If $u(x, t)$ denotes the temperature at time $t$ of the point $x$, then what you are looking for is a table of values for $u\left(x_{j}, t_{k}\right)$, where $1 \leq j \leq m$ and $1 \leq k \leq n$. When an analytical solution is available, you may be able to use it to compute $u\left(x_{j}, t_{k}\right)$. However, in many practical problems, it is impossible to compute the analytical solutions, since the data is known only on a set of discrete points.

To remedy this situation, we may forgo the search for an analytical solution in favor of a numerical solution. In this chapter you will study numerical methods that are based on the principle of discretization. By discretizing a problem, you come up with an algorithm or a formula that can be used to generate numerical values of the solution at a discrete set of points. For example, in the heat problem, after discretizing, you arrive at a formula which can be iterated to generate a numerical solution.

With ubiquity of computers capable of carrying out numerical computations to a very high degree of accuracy, at a minimum cost to the user, the numerical methods are gaining more and more prominence in the world of engineering and science. Moreover, they enjoy the advantage of being applicable with few constraints, as compared to some of the analytical methods. For example, the numerical scheme for the heat equation (Section 18.1) applies with equal ease to problems with a variety of boundary conditions. As you may recall from Chapter 11, with the analytical methods we had to treat these problems separately. Also, in solving Dirichlet problems in rectangular coordinates, with the analytical methods we had to restrict to rectangular regions. You will see in Sections 18.3 and 9.4 that the numerical methods can be applied to less regular regions.

## Sections

[[Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 18 Finite Difference Numerical Methods/18.1 The Finite Difference Method for the Heat Equation|18.1 The Finite Difference Method for the Heat Equation]]

[[Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 18 Finite Difference Numerical Methods/18.2 The Finite Difference Method for the Wave Equation|18.2 The Finite Difference Method for the Wave Equation]]

[[Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 18 Finite Difference Numerical Methods/18.3 The Finite Difference Method for Laplace's Equation|18.3 The Finite Difference Method for Laplace's Equation]]

[[Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 18 Finite Difference Numerical Methods/18.4 Iteration Methods for Laplace's Equation|18.4 Iteration Methods for Laplace's Equation]]
