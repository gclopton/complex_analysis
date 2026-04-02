## Topics to Review

The core material in Sections 7.17.4 is independent from the previous chapters and requires only a basic knowledge of calculus. Methods from complex analysis will be used in applications and to develop tools for computing Fourier series. These topics are usually included at the end of sections and can be omitted without affecting the continuity of the course. Complex numbers and the complex exponential function are required in Section 7.5 to define the complex form of Fourier series.

## Looking Ahead

Fourier series, as presented in Sections 7.1-7.4, are essential for all that follows and cannot be omitted. The proof of convergence of Fourier series in Section 7.6 is optional. Sections 7.2 and 7.5 contain applications based on tools from complex analysis, such as Taylor and Laurent series, and integrals by tesidues. These applications take you deeper in the computation of Fourier series. You are encouraged to cover at least some of them, since these methods will be used again in later chapters to expand the scope of the theory and derive important properties of special functions.

## 7

## FOURIER SERIES

Mathematics compares the most diverse phenomena and discovers the secret analogies that unite them.

-Joseph Fourier

Like the familiar Taylor series, Fourier series are special types of expansions of functions. With a Taylor series, the expansion is in terms of the special set of functions $1, x, x^{2}, x^{3}, \ldots$. With a Fourier series, we are interested in expanding a function in terms of the special set of functions $1, \cos x, \cos 2 x, \cos 3 x, \ldots, \sin x, \sin 2 x, \sin 3 x, \ldots$. Thus, a Fourier series expansion of a function $f$ is an expression of the form

$$
f(x)=a_{0}+\sum_{n=1}^{\infty}\left(a_{n} \cos n x+b_{n} \sin n x\right)
$$

where $a_{0}, a_{n}$, and $b_{n}$ are the Fourier coefficients. Fourier series arose naturally when solving Dirichlet problems on the disk in Section 4.7. As we will see in the remaining chapters, Fourier series are fundamental tools for the implementation of important methods for solving boundary value problems, such as the separation of variables method and the eigenfunction expansions method. Also the theory of Fourier series will serve as a model for theories involving other special functions such as Bessel functions and Legendre polynomials. The latter are the tools of choice for solving boundary value problems involving Laplace's equation on disks, cylinders and spheres.

In this chapter, we will present basic properties of Fourier series that will be used throughout the rest of the book.

### 7.1 Periodic Functions

![](./images/3daa498e-ff33-460f-afa4-7af2cd933f9d-02_469_505_312_110.jpg)
Figure 1 The boundary function $f(\theta)$ in a Dirichlet problem on a disk centered at the origin is $2 \pi$-periodic.

![](./images/3daa498e-ff33-460f-afa4-7af2cd933f9d-02_334_520_1173_120.jpg)
Figure $2 \mathrm{~A} T$-periodic function.

![](./images/3daa498e-ff33-460f-afa4-7af2cd933f9d-02_412_528_1843_120.jpg)
Figure 3 The 2-periodic func-

tion in Example 1.

One of the problems that we have discussed at length in previous sections was the Dirichlet problem on a disk of radius $R>0$, centered at the origin. In such a problem, we are supposed to solve Laplace's equation inside the disk, given the values of the function on the boundary of the disk. Using polar coordinates, the boundary data was given by a function $f(\boldsymbol{\theta})$ of the polar angle $\theta$. Because $\theta$ and $\theta+2 \pi$ correspond to the same point on the unit circle, we have $f(\theta)=f(\theta+2 \pi)$. In other words, the function $f$ is $2 \pi$-periodic (Figure 1). Periodic functions will arise naturally not only in boundary value problems on a disk but also in wave and heat problems over a finite interval. A function $f$ satisfying the identity

$$
f(x)=f(x+T) \quad \text { for all } x,
$$

where $T>0$, is called periodic or, more specifically, $T$-periodic (Figure 2). The number $T$ is called a period of $f$. If $f$ is nonconstant, we define the fundamental period, or simply, the period of $f$ to be the smallest positive number $T$ for which (1) holds. For example, the functions $3 \sin x, \sin 2 x$ are all $2 \pi$-periodic. The period of $\sin x$ is $2 \pi$, while the period of $\sin 2 x$ is $\pi$.

Using (1) repeatedly, we get

$$
f(x)=f(x+T)=f(x+2 T)=\cdots=f(x+n T) .
$$

Hence if $T$ is a period, then $n T$ is also a period for any integer $n>0$. In the case of the sine function, this amounts to saying that $2 \pi, 4 \pi, 6 \pi, \ldots$ are all periods of $\sin x$, but only $2 \pi$ is the fundamental period. Because the values of a $T$-periodic function repeat every $T$ units, its graph is obtained by repeating the portion over any interval of length $T$ (Figure 2). As a consequence, to define a $T$-periodic function, it is enough to describe it over an interval of length $T$. Obviously, the interval can be chosen in many different ways. The following example illustrates these ideas.

## EXAMPLE 1 Describing a periodic function

Describe the 2-periodic function $f$ in Figure 3 in two different ways:
(a) by considering its values on the interval $0 \leq x<2$;
(b) by considering its values on the interval $-1 \leq x<1$.

Solution (a) On the interval $0 \leq x<2$ the graph is a portion of the straight line $y=-x+1$. Thus

$$
f(x)=-x+1 \text { if } 0 \leq x<2 .
$$

Now the relation $f(x+2)=f(x)$ describes $f$ for all other values of $x$.

![](./images/3daa498e-ff33-460f-afa4-7af2cd933f9d-03_430_455_197_63.jpg)
Figure 4 Areas over one period are equal.

THEOREM 1 INTEGRAL OVER ONE PERIOD
(b) On the interval $-1 \leq x<1$, the graph consists of two straight lines (Figure 3). We have

$$
f(x)= \begin{cases}-x-1 & \text { if }-1 \leq x<0 \\ -x+1 & \text { if } 0 \leq x<1\end{cases}
$$

As in part (a), the relation $f(x+2)=f(x)$ describes $f$ for all values of $x$ outside the interval $[-1,1)$.

Although the formulas in Example 1(a) and (b) are different, they describe the same periodic function. In practice, we use common sense in choosing the most convenient formula. Before we illustrate with an example, we introduce a very useful theorem whose content is intuitively clear. It says that the definite integral of a $T$-periodic function is the same over any interval of length $T$ (Figure 4).

Suppose that $f$ is $T$-periodic. Then, for any real number $a$, we have

$$
\int_{0}^{T} f(x) d x=\int_{a}^{a+T} f(x) d x
$$

Proof Define

$$
F(a)=\int_{a}^{a+T} f(x) d x
$$

By the fundamental theorem of calculus, we have $F^{\prime}(a)=f(a+T)-f(a)=0$, because $f$ is periodic with period $T$. Hence $F(a)$ is constant for all $a$, and so $F(0)=F(a)$, which implies the theorem. $\square$

## EXAMPLE 2 Integrating periodic functions

Let $f$ be the 2 -periodic function in Example 1. Use Theorem 1 to compute
(a) $\int_{-1}^{1} f^{2}(x) d x$,
(b) $\int_{-N}^{N} f^{2}(x) d x, N$ a positive integer.

Solution (a) Observe that $f^{2}(x)$ is also 2 -periodic. Thus, by Theorem 1, to compute the integral in (a) we may choose any interval of length 2 . Using the formula from Example 1 (a), we have

$$
\int_{-1}^{1} f^{2}(x) d x=\int_{0}^{2} f^{2}(x) d x=\int_{0}^{2}(-x+1)^{2} d x=-\left.\frac{1}{3}(-x+1)^{3}\right|_{0} ^{2}=\frac{2}{3}
$$

(b) We break up the integral $\int_{-N}^{N}$ into the sum of $N$ integrals over intervals of length 2 , of the form $\int_{n}^{n+2}, n=-N,-N+2, \ldots, N-2$, as follows:

$$
\int_{-N}^{N} f^{2}(x) d x=\int_{-N}^{-N+2} f^{2}(x) d x+\int_{-N+2}^{-N+4} f^{2}(x) d x+\cdots+\int_{N-2}^{N} f^{2}(x) d x
$$

Since $f^{2}(x)$ is 2 -periodic, by Theorem 1, each integral on the right side is equal to $\int_{-1}^{1} f^{2}(x) d x=\frac{2}{3}$, by (a). Hence the desired integral is $N \frac{2}{3}=\frac{2 N}{3}$.

The most important periodic functions are those in the ( $2 \pi$-periodic) trigonometric system

$$
\begin{gathered}
1, \cos x, \cos 2 x, \cos 3 x, \ldots, \cos m x, \ldots, \\
\sin x, \sin 2 x, \sin 3 x, \ldots, \sin n x, \ldots
\end{gathered}
$$

They are $2 \pi$-periodic, and orthogonal on the interval $[0,2 \pi]$. Recall the orthogonality properties of the trigonometric system from Exercise 12, Section 3.2 (in what follows, the indices $m$ and $n$ are nonnegative integers):

$$
\begin{array}{ll}
\int_{-\pi}^{\pi} \cos m x \cos n x d x=0 & \text { if } m \neq n \\
\int_{-\pi}^{\pi} \cos m x \sin n x d x=0 & \text { for all } m \text { and } n \\
\int_{-\pi}^{\pi} \sin m x \sin n x d x=0 & \text { if } m \neq n
\end{array}
$$

We also have the useful identities:

$$
\int_{-\pi}^{\pi} \cos ^{2} m x d x=\int_{-\pi}^{\pi} \sin ^{2} m x d x=\pi \quad \text { for all } m \neq 0
$$

To prove these, we can use the complex integral, as suggested in Exercise 12, Section 3.2, or just use trigonometric identities. For example, to prove the first one, use

$$
\cos m x \cos n x=\frac{1}{2}(\cos (m+n) x+\cos (m-n) x)
$$

Since $m \pm n \neq 0$, we get

$$
\begin{aligned}
\int_{-\pi}^{\pi} & \cos m x \cos n x d x \\
\quad= & \frac{1}{2}\left[\frac{1}{m+n} \sin (m+n) x+\frac{1}{m-n} \sin (m-n) x\right]_{-\pi}^{\pi}=0 .
\end{aligned}
$$

## Exercises 7.1

In Exercises 1-2, find a period of the given function and sketch its graph.

1. (a) $\cos x$,
(b) $\cos \pi x$,
(c) $\cos \frac{2}{3} x$,
(d) $\cos x+\cos 2 x$.
2. (a) $\sin 7 \pi x$,
(b) $\sin n \pi x$,
(d) $\sin x+\cos x$, (e) $\sin ^{2} 2 x$.

In Exercises 3-6, find a formula that describes the function in the accompanying figure (Figures 5-8).
3.

![](./images/3daa498e-ff33-460f-afa4-7af2cd933f9d-05_294_516_380_736.jpg)
Figure 5

5. 

![](./images/3daa498e-ff33-460f-afa4-7af2cd933f9d-05_297_549_807_732.jpg)
Figure 7

4. 

![](./images/3daa498e-ff33-460f-afa4-7af2cd933f9d-05_292_544_382_1416.jpg)
Figure 6

6. 

![](./images/3daa498e-ff33-460f-afa4-7af2cd933f9d-05_297_548_805_1412.jpg)
Figure 8

7. Sums of periodic functions. Show that if $f_{1}, f_{2}, \ldots, f_{n}, \ldots$ are $T$-periodic functions, then $a_{1} f_{1}+a_{2} f_{2}+\cdots+a_{n} f_{n}$ is also $T$-periodic. More generally, show that if the series $\sum_{n=1}^{\infty} a_{n} f_{n}(x)$ converges for all $x$ in $0<x \leq T$, then its limit is a $T$-periodic function.
8. Sums of periodic functions need not be periodic. Let $f(x)=\cos x+ \cos \pi x$. (a) Show that the equation $f(x)=2$ has a unique solution.
(b) Conclude from (a) that $f$ is not periodic. Does this contradict Exercise 7? The function $f$ is called almost periodic. These functions are of considerable interest and have many useful applications.
9. Operations on periodic functions. (a) Let $f$ and $g$ be two $T$-periodic functions. Show that the product $f(x) g(x)$ and the quotient $f(x) / g(x)(g(x) \neq 0)$ are also $T$-periodic.
(b) Show that if $f$ has period $T$ and $a>0$, then $f\left(\frac{x}{a}\right)$ has period $a T$ and $f(a x)$ has period $\frac{T}{a}$.
(c) Show that if $f$ has period $T$ and $g$ is any function (not necessarily periodic), then the composition $g \circ f$ has period $T$.
10. With the help of Exercise 9, determine the period of the given function.
(a) $\sin 2 x$
(b) $\cos \frac{1}{2} x+3 \sin 2 x$
(c) $\frac{1}{2+\sin x}$
(d) $e^{\cos x}$

In Exercises 11-14, a $\pi$-periodic function is described over an interval of length $\pi$. In each case plot the graph over three periods and compute the integral

$$
\int_{-\pi / 2}^{\pi / 2} f(x) d x
$$

11. $f(x)=\sin x, \quad 0 \leq x<\pi$.
12. $f(x)=\cos x, \quad 0 \leq x<\pi$.
13. 
14. $f(x)=x^{2}, \quad-\frac{\pi}{2} \leq x<\frac{\pi}{2}$.

$$
f(x)= \begin{cases}1 & \text { if } 0 \leq x \leq \frac{\pi}{2} \\ 0 & \text { if }-\frac{\pi}{2}<x<0\end{cases}
$$

15. Antiderivatives of periodic functions. Suppose that $f$ is $2 \pi$-periodic and let $a$ be a fixed real number. Define

$$
F(x)=\int_{a}^{x} f(t) d t, \text { for all } x
$$

Show that $F$ is $2 \pi$-periodic if and only if $\int_{0}^{2 \pi} f(t) d t=0$. [Hint: Theorem 1.]
16. Suppose that $f$ is $T$-periodic and let $F$ be an antiderivative of $f$, defined as in Exercise 15. Show that $F$ is $T$-periodic if and only if the integral of $f$ over an interval of length $T$ is 0 .
17. (a) Let $f$ be as in Example 1. Describe the function

$$
F(x)=\int_{0}^{x} f(t) d t
$$

[Hint: By Exercise 16, it is enough to consider $x$ in $[0,2]$.]
(b) Plot $F$ over the interval $[-4,4]$.

### 7.2 Fourier Series

Fourier series arose naturally in Section 4.7 from our solution of the Dirichlet problem in a disk centered at 0 . They are special expansions of $2 \pi$-period functions of the form

$$
f(x)=a_{0}+\sum_{n=1}^{\infty}\left(a_{n} \cos n x+b_{n} \sin n x\right)
$$

where the coefficients $a_{0}, a_{n}$, and $b_{n}$ are called the Fourier coefficients of $f$ and are given by the following Euler formulas.
The Fourier coefficients of of a function $f$ are given by

## EULER FORMULAS FOR THE FOURIER COEFFICIENTS

$$
\begin{aligned}
& a_{0}=\frac{1}{2 \pi} \int_{-\pi}^{\pi} f(x) d x \\
& a_{n}=\frac{1}{\pi} \int_{-\pi}^{\pi} f(x) \cos n x d x \quad(n=1,2, \ldots) \\
& b_{n}=\frac{1}{\pi} \int_{-\pi}^{\pi} f(x) \sin n x d x \quad(n=1,2, \ldots)
\end{aligned}
$$

For a positive integer $N$, we denote the $N$ th partial sum of the Fourier series
of $f$ by $s_{N}(x)$. Thus

$$
s_{N}(x)=a_{0}+\sum_{n=1}^{N}\left(a_{n} \cos n x+b_{n} \sin n x\right)
$$

Because all the integrands in (2)-(4) are $2 \pi$-periodic, we can use Theorem 1, Section 7.1, to rewrite these formulas using integrals over the interval $[0,2 \pi]$ (or any other interval of length $2 \pi$ ). Such alternative formulas are sometimes useful.

## ALTERNATIVE EULER FORMULAS

$$
a_{0}=\frac{1}{2 \pi} \int_{0}^{2 \pi} f(x) d x
$$

$$
a_{n}=\frac{1}{\pi} \int_{0}^{2 \pi} f(x) \cos n x d x, \text { and } b_{n}=\frac{1}{\pi} \int_{0}^{2 \pi} f(x) \sin n x d x, n \geq 1
$$

The Fourier coefficients were known to Euler before Fourier and for this reason they bear Euler's name. Euler used them to derive particular Fourier series such as the one presented in Example 1 below.

Before we consider some examples of Fourier series, it is instructive to motivate the Euler formulas by deriving them from the Fourier series, using the orthogonality of the trigonometric system. For this purpose, we proceed as Fourier himself did. We integrate both sides of (1) over the interval $[-\pi, \pi]$, assuming term-by-term integration is justified, and get

$$
\int_{-\pi}^{\pi} f(x) d x=\int_{-\pi}^{\pi} a_{0} d x+\sum_{n=1}^{\infty} \int_{-\pi}^{\pi}\left(a_{n} \cos n x+b_{n} \sin n x\right) d x
$$

But $\int_{-\pi}^{\pi} \cos n x d x=\int_{-\pi}^{\pi} \sin n x d x=0$ for $n=1,2, \ldots$, so

$$
\int_{-\pi}^{\pi} f(x) d x=\int_{-\pi}^{\pi} a_{0} d x=2 \pi a_{0} \quad \Rightarrow \quad a_{0}=\frac{1}{2 \pi} \int_{-\pi}^{\pi} f(x) d x
$$

Similarly, starting with (1), we multiply both sides by $\cos m x(m \geq 1)$, integrate term by term, use the orthogonality of the trigonometric system
(Section 7.1), and get

$$
\begin{aligned}
\int_{-\pi}^{\pi} f(x) \cos m x d x= & \overbrace{\int_{-\pi}^{\pi} a_{0} \cos m x d x}^{=0}+\sum_{n=1}^{\infty} \overbrace{\int_{-\pi}^{\pi} a_{n} \cos n x \cos m x d x}^{=0 \text { for } m \neq n} \\
& +\sum_{n=1}^{\infty} \overbrace{\int_{-\pi}^{\pi} b_{n} \sin n x \cos m x d x}^{=0} \\
= & a_{m} \overbrace{\int_{-\pi}^{\pi} \cos ^{2} m x d x}^{=\pi}=\pi a_{m}
\end{aligned}
$$

Solving for $a_{m}$, we obtain (3). By a similar procedure, we derive (4).
Our first example displays many of the peculiar properties of Fourier series.

![](./images/3daa498e-ff33-460f-afa4-7af2cd933f9d-08_432_535_1113_120.jpg)
Figure 1 Sawtooth function.

In evaluating $a_{n}$, we use the formula $\int x \cos n x d x= \frac{1}{n^{2}} \cos n x+\frac{x}{n} \sin n x$, which is obtained by integrating by parts.

## EXAMPLE 1 Fourier series of the sawtooth function

The sawtooth function, shown in Figure 1, is determined by the formulas

$$
f(x)= \begin{cases}\frac{1}{2}(\pi-x) & \text { if } 0<x \leq 2 \pi, \\ f(x+2 \pi) & \text { otherwise } .\end{cases}
$$

(a) Find its Fourier series.
(b) With the help of a computer, plot the partial sums $s_{1}(x), s_{7}(x)$, and $s_{20}(x)$, and determine the graph of the Fourier series.
Solution (a) Using (5) and (6), we have

$$
a_{0}=\frac{1}{2 \pi} \int_{0}^{2 \pi} f(x) d x=\frac{1}{2 \pi} \int_{0}^{2 \pi} \frac{1}{2}(\pi-x) d x=0 ;
$$

$$
\begin{aligned}
a_{n} & =\frac{1}{\pi} \int_{0}^{2 \pi} \frac{1}{2}(\pi-x) \cos n x d x \\
& =\frac{1}{2 \pi}\left\{\int_{0}^{2 \pi} \pi \cos n x d x-\int_{0}^{2 \pi} x \cos n x d x\right\}=0
\end{aligned}
$$

$$
\begin{aligned}
b_{n} & =\frac{1}{\pi} \int_{0}^{2 \pi} \frac{1}{2}(\pi-x) \sin n x d x \\
& =\frac{1}{2 \pi}\left\{\int_{0}^{2 \pi} \pi \sin n x d x-\int_{0}^{2 \pi} x \sin n x d x\right\} \\
& =\frac{1}{2 \pi}\left\{\frac{-1}{n^{2}} \sin n x+\left.\frac{x}{n} \cos n x\right|_{0} ^{2 \pi} \quad\right. \text { (integration by parts) } \\
& =\frac{1}{2 \pi} \frac{2 \pi}{n}=\frac{1}{n} .
\end{aligned}
$$

Figure 2 To distinguish the graphs of the $n$th partial sums of the Fourier series, $s_{n}(x)=\sum_{k=1}^{n} \frac{\sin k x}{k}$, note that as $n$ increases, the frequencies of the sine terms increase. This causes the graphs of the higher partial sums to be more wiggly. The limiting graph is the graph of the whole Fourier series, shown in Figure 3. It is identical to the graph of the function, except at points of discontinuity.

![](./images/3daa498e-ff33-460f-afa4-7af2cd933f9d-09_384_459_876_49.jpg)
Figure 3 The graph of the Fourier series $\sum_{n=1}^{\infty} \frac{\sin n x}{n}$ coincides with the graph of the function, except at the points of the discontinuity.

![](./images/3daa498e-ff33-460f-afa4-7af2cd933f9d-09_475_453_1574_37.jpg)
Figure 4 Left and right

limits of a function at a point of discontinuity: $f(1+)=\frac{1}{2}$, $f(1-)=1$.

Substituting these values for $a_{n}$ and $b_{n}$ into (1), we obtain $\sum_{n=1}^{\infty} \frac{\sin n x}{n}$ as the Fourier series of $f$.
![](./images/3daa498e-ff33-460f-afa4-7af2cd933f9d-09_486_1345_309_549.jpg)
(b) Figure 2 shows the first, seventh and twentieth partial sums of the Fourier series. We see clearly that the Fourier series of $f$ converges to $f(x)$ at each point $x$ where $f$ is continuous. In particular, for $0<x<2 \pi$, we have

$$
\sum_{n=1}^{\infty} \frac{\sin n x}{n}=\frac{1}{2}(\pi-x)
$$

At the points of discontinuity ( $x=2 k \pi, k=0, \pm 1, \pm 2, \ldots$ ), the series converges to 0 . The graph of the Fourier series $\sum_{n=1}^{\infty} \frac{\sin n x}{n}$ is shown in Figure 3. It agrees with the graph of the function, except at the points of discontinuity.

Two important facts are worth noting concerning the behavior of Fourier series near points of discontinuity. As we will see shortly, these observations are true in a very general sense.
Note 1: At the points of discontinuity ( $x=2 k \pi$ ) in Example 1, the Fourier series converges to 0 , which is the average value of the function from the left and the right at these points.
Note 2: Near the points of discontinuity, the Fourier series overshoots its limiting values. This is apparent in Figure 2, where humps form on the graphs of the partial sums near the points of discontinuity. This curious phenomenon is known as the Gibbs (or Wilbraham-Gibbs) phenomenon. (See the paper [15] for an interesting historical account.)

## Fourier Series Representation

To state our main result, we recall from Section 3.1 the definitions of piecewise continuous and piecewise smooth functions. We will write

$$
f(c-)=\lim _{x \rightarrow c^{-}} f(x)
$$

to denote the fact that $f$ approaches the number $f(c-)$ as $x$ approaches $c$ from below (Figure 4). Similarly, if the limit of $f$ exists as $x$ approaches $c$

![](./images/3daa498e-ff33-460f-afa4-7af2cd933f9d-10_484_530_303_85.jpg)
Figure 5 A continuous $2 p$ periodic function.

![](./images/3daa498e-ff33-460f-afa4-7af2cd933f9d-10_467_541_1065_93.jpg)
Figure 6 Average of $f(x)$ at $x=1$.

## THEOREM 1 FOURIER SERIES REPRESENTATION

from above, we denote this limit $f(c+)$ and write

$$
f(c+)=\lim _{x \rightarrow c^{+}} f(x) .
$$

A function $f$ is thus continuous at $c$ if and only if

$$
f(c-)=f(c+)=f(c) .
$$

In this notation, a function $f$ is said to be piecewise continuous on the interval $[a, b]$ if $f(a+)$ and $f(b-)$ exist, and $f$ is defined and continuous on $(a, b)$ except at a finite number of points in $(a, b)$ where the left and right limits exist. A periodic function is said to be piecewise continuous if it is piecewise continuous on every interval of the form $[a, b]$. A periodic function is said to be continuous if it is continuous on the entire real line. Note that continuity forces a certain behavior of the periodic function at the endpoints of any interval of length one period. For example, if $f$ is $2 p$-periodic and continuous, then necessarily $f(-p)=f(p)$ (Figure 5). The function of Example 1 is piecewise continuous, while the function in Example 2 below is continuous. Let us also recall that a function $f$ is said to be piecewise smooth if $f$ and $f^{\prime}$ are piecewise continuous on $[a, b]$. Similarly, a periodic function is piecewise smooth if it is piecewise smooth on every interval $[a, b]$. One more item of terminology is needed. The average (or arithmetic average) of $f$ at $c$ is

$$
\frac{f(c-)+f(c+)}{2} .
$$

Clearly if $f$ is continuous at $c$, then its average at $c$ is $f(c)$. Thus the notion of average will be of interest only at points of discontinuity.

As an illustration, consider the function in Figure 6. It has a discontinuity at $x=1$ and its average there is $\frac{1+\frac{1}{2}}{2}=\frac{3}{4}$. We can now state a fundamental result in the theory of Fourier series. The proof of this theorem is presented in Section 7.6.
Suppose that $f$ is a $2 \pi$-periodic piecewise smooth function. Then for all $x$ we have

$$
\frac{f(x+)+f(x-)}{2}=a_{0}+\sum_{n=1}^{\infty}\left(a_{n} \cos n x+b_{n} \sin n x\right),
$$

where the Fourier coefficients $a_{0}, a_{n}, b_{n}$ are given by (2)-(4). In particular, if $f$ is piecewise smooth and continuous at $x$, then

$$
f(x)=a_{0}+\sum_{n=1}^{\infty}\left(a_{n} \cos n x+b_{n} \sin n x\right) .
$$

![](./images/3daa498e-ff33-460f-afa4-7af2cd933f9d-11_849_480_849_48.jpg)
Figure 7 At a point of discontimuity of a piecewise smooth function, the Fourier series converges to the average of the function at that point.

Let us see what (7) is telling us. At a point of continuity of $f$, the Fourier series converges to $f(x)$. At a point of discontinuity, the Fourier series does its best to converge, and having no reason to favor one side over the other, it converges to the average of the left and right limits (see Figure 7). Note that in (7) the value of the Fourier series of $f$ at a given point $x$ does not depend on $f(x)$ but on the limit of $f$ from the left and right at $x$. For this reason, we may define (or redefine) $f$ at isolated points without affecting its Fourier series. This is illustrated by the behavior of the Fourier series in Example 1, where, at the points of discontinuity, we could have assigned any values for the function without affecting the behavior of the Fourier series. If we redefine the function at points of discontinuity to be

$$
\frac{f(x+)+f(x-)}{2},
$$

we then have the equality

$$
f(x)=a_{0}+\sum_{n=1}^{\infty}\left(a_{n} \cos n x+b_{n} \sin n x\right)
$$

holding at all $x$. We will often assume such a modification at the points of discontinuity and not worry about the more precise, but cumbersome, equality (7).

It is important to keep in mind that continuity of $f$ alone is not enough to ensure the convergence of its Fourier series. Although we will not encounter such functions, there are continuous functions with Fourier series that diverge at an infinite number of points in $[0,2 \pi]$.

The problem of convergence for Fourier series was tackled by Fourier, Cauchy, and many other prominent mathematicians, who tried but could not establish the convergence for arbitrary $f$. We owe it to Peter Gustav Lejeune Dirichlet (1805-1859), who took a different approach to this problem by first formulating sufficient conditions on $f$ that ensure the convergence of its Fourier series representation. Dirichlet's theorem about Fourier series is basically what we have stated in Theorem 1. Determining conditions on $f$ that ensure the convergence of its Fourier series is an extremely hard problem. The most general results in this direction were obtained in the 1960s by Lennart Carleson (University of Uppsala, Sweden, and University of California, Los Angeles) and Richard Hunt (University of Indiana). These spectacular results are far beyond the level of this book. For a modern account of this theory, see the book by Grafakos [14].

Let us note one more property of Fourier series, which is an immediate consequence of Theorem 1.

## COROLLARY 1 UNIQUENESS OF FOURIER SERIES REPRESENTATION

![](./images/3daa498e-ff33-460f-afa4-7af2cd933f9d-12_431_529_1444_106.jpg)
Figure 8 Triangular wave.

Suppose that $f$ and $g$ are $2 \pi$-periodic piecewise smooth functions. If $f$ and $g$ have the same Fourier coefficients, then $f(x)=g(x)$ for all $x$, except possibly at the points where $f$ or $g$ are discontinuous. Consequently, if $f$ and $g$ are continuous and have the same Fourier coefficients, then they are equal everywhere.
Proof Since the Fourier series of a function converges to the value of the function at the points of continuity, it follows that if $f$ and $g$ have the same Fourier series, then they must be equal at all the points of continuity.

For all practical purposes in analysis, if $f$ and $g$ have the same Fourier series, then they are considered to be the same function.

## EXAMPLE 2 Triangular wave

(a) Find the Fourier series of the $2 \pi$-periodic triangular function, which is given on the interval $[-\pi, \pi]$ by

$$
f(x)= \begin{cases}\pi+x & \text { if }-\pi \leq x \leq 0, \\ \pi-x & \text { if } 0 \leq x \leq \pi .\end{cases}
$$

(b) Plot some partial sums and the Fourier series.

Solution Figure 8 shows that the function is piecewise smooth and continuous for all $x$. So, from the second part of Theorem 1, we expect the Fourier series to converge to $f(x)$ for all $x$. Using (2), we have

$$
a_{0}=\frac{1}{2 \pi} \int_{-\pi}^{\pi} f(x) d x=\frac{1}{2 \pi} \pi^{2}=\frac{1}{2} \pi
$$

(This is the area of the triangular region in Figure 8 with base $[-\pi, \pi]$ divided by $2 \pi$.) Using (3), we have

$$
\begin{aligned}
a_{n} & =\frac{1}{\pi} \int_{-\pi}^{0}(\pi+x) \cos n x d x+\frac{1}{\pi} \int_{0}^{\pi}(\pi-x) \cos n x d x \\
& =\frac{2}{\pi} \int_{0}^{\pi}(\pi-x) \cos n x d x \quad \text { (change } x \text { to }-x \text { in the first integral) } \\
& =\frac{2}{\pi}\left\{\frac{1}{n^{2}}-\frac{\cos n \pi}{n^{2}}\right\} \quad \text { (integration by parts). }
\end{aligned}
$$

Since $\cos n \pi=(-1)^{n}$, we see that $a_{n}=0$ if $n$ is even, and $a_{n}=\frac{4}{\pi n^{2}}$ if $n$ is odd. Finally, using (4), we find

$$
b_{n}=\frac{1}{\pi} \int_{-\pi}^{\pi} \overbrace{f(x) \sin n x}^{\text {odd function }} d x=0
$$

since we are integrating an odd function over a symmetric interval. Now Theorem 1 implies that

$$
f(x)=\frac{1}{2} \pi+\sum_{n \text { odd }} \frac{4}{\pi n^{2}} \cos n x=\frac{1}{2} \pi+\frac{4}{\pi} \sum_{k=0}^{\infty} \frac{1}{(2 k+1)^{2}} \cos (2 k+1) x
$$

The partial sums of the Fourier series, illustrated in Figure 9, are converging very fast. much faster than those in Example 1. This is due to the magnitudes of the Fourier coefficients. In Example 1 the coefficients are of the order 1/ $n$, while in Example 2 the coefficients are of the order $1 / n^{2}$.

THEOREM 2 UNIFORM CONVERGENCE OF FOURIER SERIES

![](./images/3daa498e-ff33-460f-afa4-7af2cd933f9d-13_433_659_361_536.jpg)
Figure 9 Partial sums of the Fourier series.

![](./images/3daa498e-ff33-460f-afa4-7af2cd933f9d-13_425_678_365_1259.jpg)
Figure 10 The Fourier series.

for all $x$. Since the function and its Fourier series are equal at all points, their graphs coincide (compare Figures 8 and 10).

In (9), letting $k$ run from 0 to 1,2 , and 5 , respectively, we generate the third, fifth, and eleventh partial sums of the Fourier series. These are plotted in Figure 9. Note the fast convergence of the Fourier series.

Figure 9 suggests that the Fourier series in Example 2 converges uniformly to the function. This is indeed true and follows from the following important result.

Suppose that $f$ is a $2 \pi$-periodic piecewise smooth function. Then the Fourier series of $f$ converges uniformly for all $x$ to $f(x)$ if and only if $f$ is continuous for all $x$. Thus, if $f$ is continuous and piecewise smooth, then

$$
f(x)=a_{0}+\sum_{n=1}^{\infty}\left(a_{n} \cos n x+b_{n} \sin n x\right),
$$

where the Fourier series converges uniformly for all $x$.

Proof One direction is immediate from Theorem 1, Section 4.2, which asserts that the uniform limit of continuous functions is continuous. Since a partial sum of a Fourier series is a finite linear combination of sines and cosines, it is clearly continuous. So, if $s_{N}(x)$ converges uniformly to $f(x)$ for all $x$, then $f(x)$ is necessarily continuous for all $x$. For the other direction, we know from Theorem 1 that the Fourier series converges to $f(x)$ for all $x$. To prove that the convergence is uniform, we will show that there is a constant $M$ such that $\left|a_{n}\right| \leq \frac{M}{n^{2}}$ and $\left|b_{n}\right| \leq \frac{M}{n^{2}}$. Then $\left|a_{n} \cos n x+b_{n} \sin n x\right| \leq \frac{2 M}{n^{2}}$, and the uniform convergence will follow from the Weierstrass $M$-test (Theorem 3, Section 4.2) since $\sum \frac{2 M}{n^{2}}<\infty$. To simplify the proof, we will further suppose that $f^{\prime}$ is piecewise smooth. (This condition is satisfied in all the examples in this book, and indeed most applications. A proof that does not depend on it is presented in Section 7.5 and uses Parseval's theorem.)

Integrating by parts, we find that

$$
\begin{aligned}
a_{n} & =\frac{1}{\pi} \int_{-\pi}^{\pi} f(x) \cos n x d x=\left.\frac{1}{n \pi} f(x) \sin n x\right|_{-\pi} ^{\pi}-\frac{1}{n \pi} \int_{-\pi}^{\pi} f^{\prime}(x) \sin n x d x \\
& =-\frac{1}{n \pi} \int_{-\pi}^{\pi} f^{\prime}(x) \sin n x d x
\end{aligned}
$$

because $\sin n \pi=\sin (-n \pi)=0$. Similarly, integrating by parts and using the fact that $f(\pi)=f(-\pi)$, we obtain that

$$
b_{n}=\frac{1}{\pi} \int_{-\pi}^{\pi} f(x) \sin n x d x=\frac{1}{n \pi} \int_{-\pi}^{\pi} f^{\prime}(x) \cos n x d x
$$

The function $f^{\prime}(x)$ has a piecewise continuous derivative $f^{\prime \prime}(x)$. So $\left|f^{\prime}(x)\right| \leq A$ and $\left|f^{\prime \prime}(x)\right| \leq B$ for all $x$. Let $(a, b)$ be an interval on which $f^{\prime \prime}$ is continuous. Then integrating by parts, we find that

$$
\frac{1}{n \pi} \int_{a}^{b} f^{\prime}(x) \sin n x d x=\frac{1}{n^{2} \pi}\left(\left(f^{\prime}(a) \cos n a-f^{\prime}(b) \cos n b\right)+\int_{a}^{b} f^{\prime \prime}(x) \cos n x d x\right)
$$

Hence, because $\left|f^{\prime}(a)\right| \leq A,\left|f^{\prime}(b)\right| \leq A$, and $\left|f^{\prime \prime}(x) \cos n x\right| \leq B$, we obtain

$$
\frac{1}{n \pi}\left|\int_{a}^{b} f^{\prime}(x) \sin n x d x\right| \leq \frac{1}{n^{2} \pi}(2 A+(b-a) B) \leq \frac{C}{n^{2}}
$$

where $C$ is a constant that does not depend on $n$. Since $f^{\prime \prime}$ has a finite number of discontinuities, we can write the integral $\int_{-\pi}^{\pi} f^{\prime}(x) \sin n x d x$ as the finite sum of integrals of the form $\int_{a}^{b} f^{\prime}(x) \sin n x d x$ (say, $k$ of them), where $f^{\prime \prime}(x)$ is continuous on each interval $(a, b)$. It follows from our estimate on the latter integral that $\left|a_{n}\right| \leq \frac{k C}{n^{2}}=\frac{M}{n^{2}}$, where $M=k C$ is a constant independent of $n$. The inequality for $b_{n}$ is obtained in a similar way.

Theorems 1 or 2 can be used to sum interesting series.

## EXAMPLE 3 Using Fourier series to sum series

If we take $x=0$ on both sides of (9), we get

$$
\pi=f(0)=\frac{1}{2} \pi+\frac{4}{\pi} \sum_{k=0}^{\infty} \frac{1}{(2 k+1)^{2}}
$$

Subtracting $\frac{1}{2} \pi$ and then multiplying by $\frac{\pi}{4}$, we get the interesting identity

$$
\frac{\pi^{2}}{8}=1+\frac{1}{3^{2}}+\frac{1}{5^{2}}+\frac{1}{7^{2}}+\ldots
$$

which can be used to approximate $\pi^{2}$ (and hence also $\pi$ ). $\square$

The Fourier series in Examples 1 and 2 are special in the sense that one of them contains only sine terms, while the other one contains only cosine terms. Fourier series of this type will be studied in the next section. The following Fourier series contains both sine and cosine terms. It is computed using the previous examples and the linearity property of Fourier series.

Figure 11 Note the Gibbs phenomenon at the points of discontinuity $(x=2 k \pi)$. This is due to the fact that the Fourier series consists of a cosine part that is converging very fast (Figure 9) and a sine part that overshoots at the points of discontinuity.

![](./images/3daa498e-ff33-460f-afa4-7af2cd933f9d-15_489_476_1787_39.jpg)
Figure 12 The function in Example 5 and the the partial sums of its Fourier series $s_{n}(\theta)$ with $n=1$ and 2 .

## EXAMPLE 4 A Fourier series with cosine and sine terms

Adding the two functions of Examples 1 and 2, we obtain a $2 \pi$-periodic function which is defined on the interval $[0,2 \pi]$ by

$$
f(x)= \begin{cases}\frac{3}{2}(\pi-x) & \text { if } 0<x<\pi \\ \frac{1}{2}(-\pi+x) & \text { if } \pi<x<2 \pi\end{cases}
$$

(You should check this formula and plot the function.) To compute the Fourier series, we can use the Euler formulas or, better yet, we can simply add the Fourier series of Examples 1 and 2, thanks to the linearity of the Fourier coefficients (see Exercise 18). We thus obtain the Fourier series representation

$$
f(x)=\frac{1}{2} \pi+\sum_{n=1}^{\infty}\left\{\frac{2}{\pi}\left(\frac{1}{n^{2}}-\frac{\cos n \pi}{n^{2}}\right) \cos n x+\frac{\sin n x}{n}\right\}
$$

![](./images/3daa498e-ff33-460f-afa4-7af2cd933f9d-15_404_1450_943_558.jpg)

As illustrated in Figure 11, at the points of discontinuity, the Fourier series converges to the average value $\pi$. At all other points, the Fourier series converges to $f(x)$.

## Complex Methods for Finding Fourier Series

Because of Euler's identity $e^{i n \theta}=\cos n \theta+i \sin n \theta$, which relates the complex exponential to the trigonometric functions, we expect the complex exponential function and complex analysis in general to play a role in the theory of Fourier series. This will become clear at many stages in our development of Fourier series and their applications. In what follows, we illustrate the use of major tools from complex analysis, such as residues and Laurent series, in computing Fourier series.

EXAMPLE 5 Using residues to compute Fourier series
Find the Fourier series of $f(\theta)=\frac{1}{2+\cos \theta}$.
Solution The function is $2 \pi$-periodic and even. We have $b_{n}=\frac{1}{\pi} \int_{-\pi}^{\pi} f(\theta) \sin n \theta d \theta=$ 0 , because $f(\theta) \sin n \theta$ is an odd function so its integral over a symmetric interval is 0 . In computing $a_{n}$ for $n \geq 0$, we will evaluate the integral

$$
I_{n}=\int_{0}^{2 \pi} \frac{\cos n \theta}{2+\cos \theta} d \theta \quad(n=0,1, \ldots)
$$

using a slight variation on the methods of Section 5.2. By Theorem 1, Section 7.1,

$$
\int_{0}^{2 \pi} \frac{\sin n \theta}{2+\cos \theta} d \theta=\int_{-\pi}^{\pi} \frac{\sin n \theta}{2+\cos \theta} d \theta=0
$$

because the integrand in the second integral is odd. So

$$
I_{n}=\int_{0}^{2 \pi} \frac{\cos n \theta}{2+\cos \theta} d \theta+i \int_{0}^{2 \pi} \frac{\sin n \theta}{2+\cos \theta} d \theta=\int_{0}^{2 \pi} \frac{e^{i n \theta}}{2+\cos \theta} d \theta
$$

where we have used $e^{i n \theta}=\cos n \theta+i \sin n \theta$. We now use the method of Section 5.2, as follows. Let $z=e^{i \theta}, d z=i e^{i \theta} d \theta$ or $d \theta=\frac{d z}{i z}, z^{n}=e^{i n \theta}$, and $\cos \theta=\frac{e^{i \theta}+e^{-i \theta}}{2}$. As $\theta$ varies over the interval $[0,2 \pi], z$ traverses the unit circle $C_{1}(0)$, in the positive direction. So

$$
\begin{aligned}
I_{n} & =\int_{0}^{2 \pi} \frac{e^{i n \theta}}{2+\cos \theta} d \theta=\int_{0}^{2 \pi} \frac{e^{i n \theta}}{2+\frac{e^{\mathrm{i} \theta}+e^{-\mathrm{i} \theta}}{2}} d \theta \\
& =\int_{C_{1}(0)} \frac{2 z^{n}}{4+z+\frac{1}{z}} \frac{d z}{i z}=-i \int_{C_{1}(0)} \frac{2 z^{n}}{z^{2}+4 z+1} d z
\end{aligned}
$$

We compute the last integral using residues. We have $z^{2}+4 z+1=\left(z-z_{1}\right)\left(z-z_{2}\right)$, where $z_{1}=-2+\sqrt{3}$ and $z_{2}=-2-\sqrt{3}$. We have two simple poles at $z_{1}$ and $z_{2}$. But since $\left|z_{1}\right| \approx .3$ and $\left|z_{2}\right| \approx 3.7$, only $z_{1}$ is inside the unit disk. By Proposition 1(i), Section 5.1, we have

$$
I_{n}=\left.(-2 i) 2 \pi i \frac{z^{n}}{z-z_{2}}\right|_{z=z_{1}}=2 \pi \frac{(-2+\sqrt{3})^{n}}{\sqrt{3}} .
$$

Using the formula for $I_{n}$, we obtain

$$
a_{0}=\frac{1}{2 \pi} I_{0}=\frac{1}{\sqrt{3}} \quad \text { and } \quad a_{n}=\frac{1}{\pi} I_{n}=2 \frac{(-2+\sqrt{3})^{n}}{\sqrt{3}}, \quad n=1,2, \ldots .
$$

Thus the Fourier series representation

$$
\frac{1}{2+\cos \theta}=\frac{1}{\sqrt{3}}+\frac{2}{\sqrt{3}} \sum_{n=1}^{\infty}(-2+\sqrt{3})^{n} \cos n \theta,
$$

which is valid for all $\theta$. Partial sums of the Fourier series are plotted in Figure 12. Note how fast the series is converging, because the coefficients are of the order $(-2+\sqrt{3})^{n}=\left|z_{1}\right|^{n}$, where $0<\left|z_{1}\right| \approx .3<1$.

Our next example generalizes the result of Example 5 and illustrates the use of Laurent series in computing Fourier series.

## EXAMPLE 6 Using Laurent series to compute Fourier series

Let $a>1$ be a real number. Derive the Fourier series representation

$$
f(\theta)=\frac{1}{a+\cos \theta}=\frac{1}{\sqrt{a^{2}-1}}+\frac{2}{\sqrt{a^{2}-1}} \sum_{n=1}^{\infty}\left(-a+\sqrt{a^{2}-1}\right)^{n} \cos n \theta,
$$

![](./images/3daa498e-ff33-460f-afa4-7af2cd933f9d-17_487_440_887_54.jpg)
Figure 13 The annulus of convergence of the Laurent series in Example 6.

which is valid for all $\theta$.
Solution The function is $2 \pi$-periodic and smooth. By Theorem 2, its Fourier series converges uniformly for all $\theta$ to $f(\theta)$. To find the Fourier series, we will not compute the Fourier coefficients directly; instead we will match the function with the restriction of a rational function and use Laurent series. As a first step, using the substitution $\cos \theta=\frac{1}{2}\left(z+\frac{1}{z}\right)$, where $z=e^{i \theta}$, we write

$$
\frac{1}{a+\cos \theta}=\frac{1}{a+\frac{1}{2}\left(z+\frac{1}{z}\right)}=\frac{2 z}{z^{2}+2 a z+1}
$$

Next, we expand $\frac{2 z}{z^{2}+2 a z+1}$ in an annulus that contains the unit circle $|z|=1$. As we will see in a moment, this will allow us to use the Laurent series with $z=e^{i \theta}$ and obtain the desired Fourier series.

The quadratic equation $z^{2}+2 a z+1=0$ has two real roots $z_{1}=-a-\sqrt{a^{2}-1}$ and $z_{2}=-a+\sqrt{a^{2}-1}$. Because $a>1$, we have $z_{1}<-1$ and $-1<z_{2}<0$ (you should check these assertions). By Theorem 1, Section 4.5, we have a Laurent series expansion in the annulus $\left|z_{2}\right|<|z|<\left|z_{1}\right|$ (Figure 13), and to find it we employ methods from Section 4.5. We have the partial fraction decomposition

$$
\begin{aligned}
\frac{2 z}{z^{2}+2 a z+1} & =\frac{A}{z-z_{1}}+\frac{B}{z-z_{2}}=\frac{A\left(z-z_{2}\right)+B\left(z-z_{1}\right)}{z^{2}+2 a z+1} \\
& =\frac{z(A+B)-\left(A z_{2}+B z_{1}\right)}{z^{2}+2 a z+1}
\end{aligned}
$$

Solving

$$
\begin{cases}A+B & =2 \\ A z_{2}+B z_{1} & =0\end{cases}
$$

we find $A=\frac{2 z_{1}}{z_{1}-z_{2}}=-\frac{z_{1}}{\sqrt{a^{2}-1}}$ and $B=-\frac{2 z_{2}}{z_{1}-z_{2}}=\frac{z_{2}}{\sqrt{a^{2}-1}}$, where we have used $z_{2}-z_{1}=2 \sqrt{a^{2}-1}$. So we have the partial fraction decomposition

$$
\frac{2 z}{z^{2}+2 a z+1}=\frac{1}{\sqrt{a^{2}-1}}\left(-\frac{z_{1}}{z-z_{1}}+\frac{z_{2}}{z-z_{2}}\right) .
$$

In the annulus $\left|z_{2}\right|<|z|<\left|z_{1}\right|$, the first term inside the parentheses on the right can be expanded in a power series and the second one in a Laurent series, using the geometric series as follows. For $|z|<\left|z_{1}\right|$, we have $\left|z / z_{1}\right|<1$ and so

$$
-\frac{z_{1}}{z-z_{1}}=-\frac{z_{1}}{z_{1}\left(\frac{z}{z_{1}}-1\right)}=\frac{1}{1-\left(\frac{z}{z_{1}}\right)}=\sum_{n=0}^{\infty}\left(\frac{z}{z_{1}}\right)^{n}, \quad|z|<\left|z_{1}\right|
$$

For $\left|z_{2}\right|<|z|$, we have $\left|z_{2} / z\right|<1$ and so

$$
\frac{z_{2}}{z-z_{2}}=\frac{z_{2}}{z\left(1-\frac{z_{2}}{z}\right)}=\frac{z_{2}}{z} \sum_{n=0}^{\infty}\left(\frac{z_{2}}{z}\right)^{n}, \quad\left|z_{2}\right|<|z| .
$$

Plugging into (11) and simplifying with the help of the identity $z_{1} z_{2}=1$ or $z_{2}=\frac{1}{z_{1}}$,
we get the Laurent series expansion

$$
\begin{aligned}
\frac{2 z}{z^{2}+2 a z+1} & =\frac{1}{\sqrt{a^{2}-1}} \sum_{n=0}^{\infty}\left[\left(\frac{z}{z_{1}}\right)^{n}+\frac{z_{2}}{z}\left(\frac{z_{2}}{z}\right)^{n}\right] \\
& =\frac{1}{\sqrt{a^{2}-1}}\left\{1+\sum_{n=1}^{\infty}\left[\left(\frac{z}{z_{1}}\right)^{n}+\left(\frac{z_{2}}{z}\right)^{n}\right]\right\} \\
& =\frac{1}{\sqrt{a^{2}-1}}\left\{1+\sum_{n=1}^{\infty} z_{2}^{n}\left(z^{n}+\frac{1}{z^{n}}\right)\right\}
\end{aligned}
$$

which is valid in the annulus $\left|z_{2}\right|<|z|<\left|z_{1}\right|$. In particular, for $z=e^{i \theta}$ the left side becomes $\frac{1}{a+\cos \theta}$ and the right side reduces to $\frac{1}{\sqrt{a^{2}-1}}\left\{1+\sum_{n=1}^{\infty} 2 z_{2}^{n} \cos n \theta\right\}$, after using the identity $z^{n}+\frac{1}{z^{n}}=2 \cos n \theta$, which completes the proof.

## Exercises 7.2

In Exercises 1-4, a $2 \pi$-periodic function is specified on the interval $[-\pi, \pi]$ in the accompanying figure (Figures 14-17). (a) Plot the function on the interval $[-3 \pi, 3 \pi]$.
(b) Plot its Fourier series (without computing it) on the interval $[-3 \pi, 3 \pi]$.
1.

![](./images/3daa498e-ff33-460f-afa4-7af2cd933f9d-18_226_568_1276_705.jpg)
Figure 14

3. 

![](./images/3daa498e-ff33-460f-afa4-7af2cd933f9d-18_226_566_1620_709.jpg)
Figure 16

2. 

![](./images/3daa498e-ff33-460f-afa4-7af2cd933f9d-18_226_613_1268_1411.jpg)
Figure 15

4. 

![](./images/3daa498e-ff33-460f-afa4-7af2cd933f9d-18_230_610_1614_1423.jpg)
Figure 17

In Exercises 5-16, the equation of a $2 \pi$-periodic function is given on an interval of length $2 \pi$. You are also given the Fourier series of the function. (a) Sketch the function and its Fourier series on $[-2 \pi, 2 \pi]$, and decide whether the series converges uniformly for all $x$. (b) Derive the given Fourier series.
(c) Plot the $N$ th partial sums of the Fourier series for $N=1,2, \ldots, 20$. Discuss the convergence of the partial sums by considering their graphs. Be specific at the points of discontinuity.
5. $f(x)=|x|$ if $-\pi \leq x<\pi$.

Fourier series: $\quad \frac{\pi}{2}-\frac{4}{\pi} \sum_{k=0}^{\infty} \frac{1}{(2 k+1)^{2}} \cos (2 k+1) x$.
6. $f(x)=\left\{\begin{array}{lll}\frac{1}{\pi} x & \text { if } & 0 \leq x \leq \pi, \\ 0 & \text { if } & -\pi<x \leq 0 .\end{array}\right.$

Fourier series: $\quad \frac{1}{4}-\frac{1}{\pi^{2}} \sum_{n=1}^{\infty}\left\{\left(\frac{1}{n^{2}}-\frac{(-1)^{n}}{n^{2}}\right) \cos n x+\frac{\pi(-1)^{n}}{n} \sin n x\right\}$.
7. $f(x)=|\sin x|$ if $-\pi \leq x<\pi$.

Fourier series: $\quad \frac{2}{\pi}-\frac{4}{\pi} \sum_{k=1}^{\infty} \frac{1}{(2 k)^{2}-1} \cos 2 k x$.
8. $f(x)=|\cos x|$ if $-\pi \leq x \leq \pi$.

Fourier series: $\quad \frac{2}{\pi}-\frac{4}{\pi} \sum_{k=1}^{\infty} \frac{(-1)^{k}}{(2 k)^{2}-1} \cos 2 k x$.
[Hint: You can compute directly, or, if you have done Exercise 7, substitute $x-\pi / 2$ for $x$.]
9. $f(x)=x^{2}$ if $-\pi \leq x \leq \pi$.

Fourier series: $\quad \frac{\pi^{2}}{3}+4 \sum_{n=1}^{\infty} \frac{(-1)^{n}}{n^{2}} \cos n x$.
10. $f(x)=1+\sin x+\cos 2 x$.

Fourier series: same as $f(x)$.
11. $f(x)=\sin ^{2} x ; \quad f(x)=\cos ^{2} x$.

Fourier series: $\quad \frac{1}{2}-\frac{\cos 2 x}{2}$; Fourier series: $\quad \frac{1}{2}+\frac{\cos 2 x}{2}$.
12. $f(x)=\pi^{2} x-x^{3}$ if $-\pi<x<\pi$.

Fourier series: $\quad 12 \sum_{n=1}^{\infty} \frac{(-1)^{n+1}}{n^{3}} \sin n x$.
13. $f(x)=x$ if $-\pi<x<\pi$.

Fourier series: $\quad 2 \sum_{n=1}^{\infty} \frac{(-1)^{n+1}}{n} \sin n x$.
[Hint: Let $x=\pi-t$ in Example 1.]
14.

$$
f(x)= \begin{cases}0 & \text { if }-\pi \leq x \leq-d, \\ \frac{c}{d}(x+d) & \text { if }-d \leq x \leq 0, \\ -\frac{c}{d}(x-d) & \text { if } 0 \leq x \leq d, \\ 0 & \text { if } d \leq x \leq \pi,\end{cases}
$$

where $c, d>0$ and $d<\pi$.
Fourier series: $\quad \frac{c d}{2 \pi}+\frac{4 c}{d \pi} \sum_{n=1}^{\infty} \frac{\sin ^{2}\left(\frac{d n}{2}\right)}{n^{2}} \cos n x$.
For part (c), take $c=d=\pi / 2$.
15. $f(x)=e^{-|x|}$ if $-\pi \leq x \leq \pi$.

Fourier series: $\quad \frac{e^{\pi}-1}{\pi e^{\pi}}+\frac{2}{\pi e^{\pi}} \sum_{n=1}^{\infty} \frac{1}{n^{2}+1}\left(e^{\pi}-(-1)^{n}\right) \cos n x$.
16.

$$
f(x)= \begin{cases}1 /(2 c) & \text { if }|x-d|<c, \\ 0 & \text { if } c<|x-d|<\pi,\end{cases}
$$

where $c, d>0$, and $c+d<\pi$.
Fourier series: $\frac{1}{2 \pi}+\frac{1}{c \pi} \sum_{n=1}^{\infty}\left(\frac{\sin (n c) \cos (n d)}{n} \cos n x+\frac{\sin (n c) \sin (n d)}{n} \sin n x\right)$.
For part (c), take $c=d=\pi / 2$.
17. (a) Use the Fourier series of Exercise 9 to obtain

$$
\frac{\pi^{2}}{6}=1+\frac{1}{2^{2}}+\frac{1}{3^{2}}+\frac{1}{4^{2}}+\ldots
$$

(b) Use the Fourier series of Exercise 13 to obtain

$$
\frac{\pi}{4}=1-\frac{1}{3}+\frac{1}{5}-\frac{1}{7}+\ldots
$$

18. Linearity of Fourier coefficients and Fourier series Let $\alpha$ and $\beta$ be any real numbers. Show that if $f$ and $g$ have Fourier coefficients $a_{0}, a_{1}, a_{2}, \ldots, b_{1}, b_{2}$, $\ldots$, respectively, $a_{0}^{*}, a_{1}^{*}, a_{2}^{*}, \ldots, b_{1}^{*}, b_{2}^{*}, \ldots$, then the function $\alpha f+\beta g$ has Fourier coefficients $\alpha a_{0}+\beta a_{0}^{*}, \alpha a_{1}+\beta a_{1}^{*}, \alpha a_{2}+\beta a_{2}^{*}, \ldots, \alpha b_{1}+\beta b_{1}^{*}, \alpha b_{2}+\beta b_{2}^{*}, \ldots$.

## Methods from Complex Analysis

In Exercise 19-20, compute the Fourier series of the given function, following the method in Example 5. Verify your answer by using the result of Example 6.
19. $\frac{1}{3+2 \cos \theta}$.
20. $\frac{3 \sin \theta}{10-6 \cos \theta}$.

In Exercise 21-24, compute the Fourier series of the given function, using Laurent series as we did in Example 6.
21. $\frac{1}{3+\cos \theta}$.
22. $e^{2 \cos \theta}$.
23. $\frac{1}{3+\cos \theta+\sin \theta}$.
24. $e^{\cos \theta} \cos (\sin \theta)$.

In Exercise 25-26, derive the given Fourier series by using the Fourier series of Example 6 and various manipulations, including appropriate changes of variables.
25. Let $a>1$ be a real number. Then

$$
\frac{1}{a-\cos \theta}=\frac{1}{\sqrt{a^{2}-1}}+\frac{2}{\sqrt{a^{2}-1}} \sum_{n=1}^{\infty}(-1)^{n}\left(-a+\sqrt{a^{2}-1}\right)^{n} \cos n \theta,
$$

which is valid for all $\theta$.
26. Let $a>1$ be a real number. Then for all $\theta$,

$$
\frac{1}{a+\sin \theta}=\frac{1}{\sqrt{a^{2}-1}}+\frac{2}{\sqrt{a^{2}-1}} \sum_{n=1}^{\infty}\left(-a+\sqrt{a^{2}-1}\right)^{n}\left(\cos \frac{n \pi}{2} \cos n \theta+\sin \frac{n \pi}{2} \sin n \theta\right) ;
$$

and

$$
\frac{1}{a-\sin \theta}=\frac{1}{\sqrt{a^{2}-1}}+\frac{2}{\sqrt{a^{2}-1}} \sum_{n=1}^{\infty}\left(-a+\sqrt{a^{2}-1}\right)^{n}\left(\cos \frac{n \pi}{2} \cos n \theta-\sin \frac{n \pi}{2} \sin n \theta\right) .
$$

27. Let $a>1$ be a real number. Use Example 6 and Exercise 25 to derive the following formulas: for $n \geq 1$,

$$
\begin{aligned}
\frac{1}{2 \pi} \int_{-\pi}^{\pi} \frac{d \theta}{a+\cos \theta} & =\frac{1}{\sqrt{a^{2}-1}} \\
\frac{1}{2 \pi} \int_{-\pi}^{\pi} \frac{\cos n \theta}{a+\cos \theta} d \theta & =\frac{1}{\sqrt{a^{2}-1}}\left(-a+\sqrt{a^{2}-1}\right)^{n} \\
\frac{1}{2 \pi} \int_{-\pi}^{\pi} \frac{\cos n \theta}{a-\cos \theta} d \theta & =\frac{(-1)^{n}}{\sqrt{a^{2}-1}}\left(-a+\sqrt{a^{2}-1}\right)^{n}
\end{aligned}
$$

### 7.3 Fourier Series of Functions with Arbitrary Periods

In the preceding section we worked with functions of period $2 \pi$. The choice of this period was merely for convenience. In this section, we show how

![](./images/3daa498e-ff33-460f-afa4-7af2cd933f9d-21_409_489_820_83.jpg)
Figure 1 A $2 p$-periodic function.

THEOREM 1 FOURIER SERIES REPRESENTATION: ARBITRARY PERIOD

By Theorem 1, Section 7.1, all the integrals $\int_{-p}^{p}$ can be replaced by $\int_{0}^{2 p}$ without changing the values of the coefficients. to extend our results to functions with arbitrary period by using a simple change of variables. Suppose that $f$ is a function with period $T=2 p>0$, and let

$$
g(x)=f\left(\frac{p}{\pi} x\right)
$$

Since $f$ is $2 p$-periodic, we have

$$
g(x+2 \pi)=f\left(\frac{p}{\pi}(x+2 \pi)\right)=f\left(\frac{p}{\pi} x+2 p\right)=f\left(\frac{p}{\pi} x\right)=g(x)
$$

Hence $g$ is $2 \pi$-periodic. This reduction enables us to extend the main results of Section 7.2 to functions of arbitrary period.

Suppose that $f$ is a $2 p$-periodic piecewise smooth function. Then $f$ has a unique Fourier series representation

$$
\frac{f(x-)+f(x+)}{2}=a_{0}+\sum_{n=1}^{\infty}\left(a_{n} \cos \frac{n \pi}{p} x+b_{n} \sin \frac{n \pi}{p} x\right)
$$

where the Fourier coefficients are given by

$$
a_{0}=\frac{1}{2 p} \int_{-p}^{p} f(x) d x
$$

(4)

$$
a_{n}=\frac{1}{p} \int_{-p}^{p} f(x) \cos \frac{n \pi}{p} x d x \quad(n=1,2, \ldots)
$$

(5)

$$
b_{n}=\frac{1}{p} \int_{-p}^{p} f(x) \sin \frac{n \pi}{p} x d x \quad(n=1,2, \ldots)
$$

If $f$ is continuous at $x$, then the Fourier series converges to $f(x)$. The series converges uniformly for all $x$ if and only if $f$ is continuous for all $x$.

Proof Since $f$ is piecewise smooth, it follows that the $2 \pi$-periodic function $g$ defined by (1) is also piecewise smooth. By Theorem 1 of Section 7.2 we have

$$
\frac{g(x-)+g(x+)}{2}=a_{0}+\sum_{n=1}^{\infty}\left(a_{n} \cos n x+b_{n} \sin n x\right) \quad(\text { for all } x),
$$

where

$$
a_{0}=\frac{1}{2 \pi} \int_{-\pi}^{\pi} g(x) d x ; a_{n}=\frac{1}{\pi} \int_{-\pi}^{\pi} g(x) \cos n x d x ; b_{n}=\frac{1}{\pi} \int_{-\pi}^{\pi} g(x) \sin n x d x .
$$

Replacing $x$ by $\frac{\pi}{p} x$ in (6) and using (1) gives

$$
\frac{f(x-)+f(x+)}{2}=a_{0}+\sum_{n=1}^{\infty}\left(a_{n} \cos \frac{n \pi}{p} x+b_{n} \sin \frac{n \pi}{p} x\right),
$$

where the coefficients are given by (7). To express the coefficients in terms of $f$ as in (3)-(5), we use (1) again. For example, to obtain (3), start with the first formula in (7), use (1), then use the change of variables $t=\frac{p}{\pi} x$, and get

$$
a_{0}=\frac{1}{2 \pi} \int_{-\pi}^{\pi} g(x) d x=\frac{1}{2 \pi} \int_{-\pi}^{\pi} f\left(\frac{p}{\pi} x\right) d x=\frac{1}{2 p} \int_{-p}^{p} f(t) d t .
$$

Formulas (4) and (5) are derived in a similar way. The details are left to the exercises. The uniqueness and the uniform convergence in the theorem follow from the corresponding results for $2 \pi$-periodic functions (Corollary 1 and Theorem 2, Section 7.2).

## EXAMPLE 1 A Fourier series with arbitrary period

Find the Fourier series of the $2 p$-periodic function given by $f(x)=|x|$ if $-p \leq x \leq p$

![](./images/3daa498e-ff33-460f-afa4-7af2cd933f9d-22_373_523_1684_109.jpg)
Figure 2 Triangular wave with period $2 p$.

Solution We compute the Fourier coefficients using Theorem 1. The area under the graph of $f$ in Figure 2 gives

$$
a_{0}=\frac{1}{2 p} \int_{-p}^{p} f(x) d x=\frac{p}{2}
$$

To compute $a_{n}$ we take advantage of the fact that $f(x) \cos \frac{n \pi}{p} x$ is an even function and write

$$
\begin{aligned}
a_{n} & =\frac{1}{p} \int_{-p}^{p} f(x) \cos \frac{n \pi}{p} x d x=\frac{2}{p} \int_{0}^{p} f(x) \cos \frac{n \pi}{p} x d x \\
& =\frac{2}{p} \int_{0}^{p} x \cos \frac{n \pi}{p} x d x=\frac{-2 p}{\pi^{2} n^{2}}(1-\cos n \pi)
\end{aligned}
$$

where the last integral is evaluated by parts. Since $\cos n \pi=(-1)^{n}, a_{n}=0$ if $n$ is even, and $a_{n}=\frac{-4 p}{\pi^{2} n^{2}}$ if $n$ is odd. A similar computation shows that $b_{n}=0$ for all $n$ (since $f$ is even). We thus obtain the Fourier series

$$
f(x)=\frac{p}{2}-\frac{4 p}{\pi^{2}}\left(\cos \frac{\pi}{p} x+\frac{1}{3^{2}} \cos \frac{3 \pi}{p} x+\frac{1}{5^{2}} \cos \frac{5 \pi}{p} x+\ldots\right)
$$

![](./images/3daa498e-ff33-460f-afa4-7af2cd933f9d-23_338_471_229_67.jpg)

Figure 3 Partial sums of the Fourier series ( $p=1$ ), in Example 1.

![](./images/3daa498e-ff33-460f-afa4-7af2cd933f9d-23_386_463_728_62.jpg)
Figure $4 \mathrm{~A} 2 p$-periodic triangular wave.

![](./images/3daa498e-ff33-460f-afa4-7af2cd933f9d-23_399_458_1691_51.jpg)
Figure 5 A $2 p$-periodic sawtooth function.

Because $f$ is continuous and piecewise smooth, Theorem 1 implies that the Fourier series converges uniformly to $f(x)$ for all $x$, as can be seen in Figure 3.

Sometimes we can derive a new Fourier series from a known one without performing many additional computations. The following examples illustrate this process.

## EXAMPLE 2 Triangular wave with arbitrary period and amplitude

Find the Fourier series of the $2 p$-periodic function given by

$$
g(x)= \begin{cases}a\left(1+\frac{1}{p} x\right) & \text { if }-p \leq x \leq 0, \\ a\left(1-\frac{1}{p} x\right) & \text { if } 0 \leq x \leq p .\end{cases}
$$

Solution Comparing Figures 4 and 2 shows that we can obtain the graph of $g$ by reflecting the graph of $f$ in the $x$-axis, translating it upward by $p$ units, and then scaling it by a factor of $\frac{a}{p}$. This is expressed by writing

$$
g(x)=\frac{a}{p}(-f(x)+p)=a-\frac{a}{p} f(x)
$$

Now to get the Fourier series of $g$, all we have to do is perform these operations on the Fourier series of $f$ from Example 1. We get

$$
\begin{aligned}
g(x) & =a-a\left(\frac{1}{2}-\frac{4}{\pi^{2}}\left(\cos \frac{\pi}{p} x+\frac{1}{3^{2}} \cos \frac{3 \pi}{p} x+\frac{1}{5^{2}} \cos \frac{5 \pi}{p} x+\ldots\right)\right) \\
& =\frac{a}{2}+\frac{4 a}{\pi^{2}}\left(\cos \frac{\pi}{p} x+\frac{1}{3^{2}} \cos \frac{3 \pi}{p} x+\frac{1}{5^{2}} \cos \frac{5 \pi}{p} x+\ldots\right)
\end{aligned}
$$

In compact form we have

$$
g(x)=\frac{a}{2}+\frac{4 a}{\pi^{2}} \sum_{k=0}^{\infty} \frac{1}{(2 k+1)^{2}} \cos \frac{(2 k+1) \pi}{p} x
$$

(You should check that the special case with $p=a=\pi$ yields the Fourier series of Example 2 of the previous section.)

Changing variables as we did at the outset of the section can be very useful in deriving new Fourier series from known ones.

## EXAMPLE 3 Varying the period in a Fourier series

Find the Fourier series of the function in Figure 5.
Solution Let us start by defining the function in Figure 5. On the interval $0<x<2 p$, we have $f(x)=c\left(1-\frac{x}{p}\right)$. Now, from Example 1, Section 7.2, we have the Fourier series expansion

$$
\frac{1}{2}(\pi-x)=\sum_{n=1}^{\infty} \frac{\sin n x}{n}, \quad \text { for } 0<x<2 \pi
$$

Replacing $x$ by $\frac{\pi}{p} x$ in the formula and the interval for $x$, we get

$$
\frac{1}{2}\left(\pi-\frac{\pi}{p} x\right)=\sum_{n=1}^{\infty} \frac{\sin \frac{n \pi}{p} x}{n}, \text { for } 0<\frac{\pi}{p} x<2 \pi
$$

Simplifying and multiplying both sides by $c$ to match the formula for $f$, we get

$$
c\left(1-\frac{x}{p}\right)=\frac{2 c}{\pi} \sum_{n=1}^{\infty} \frac{\sin \frac{n \pi}{p} x}{n}, \text { for } 0<x<2 p
$$

which yields the Fourier series of $f$.
The ideas behind Examples 2 and 3 are quite simple. They are based on the fact that a Fourier series is really a function and can be manipulated as such. As with any infinite series, when you manipulate a formula involving a Fourier series, you must keep in mind the interval on which this formula is valid. In particular, when you perform an operation on a Fourier series, it may affect the interval on which the resulting series is defined. This was the case when we performed a change of variables in Example 3.

## Even and Odd Functions

As we noticed already, geometric considerations are helpful in computing Fourier coefficients. This is particularly the case when dealing with even and odd functions. Recall the following definitions:

A function $f$ is even if $f(-x)=f(x)$ for all $x$.
A function $f$ is odd if $f(-x)=-f(x)$ for all $x$.

Figure 6 (a) Even function: The graph is symmetric with respect to the $y$-axis. (b) Odd function: The graph is symmetric with respect to the ori-

![](./images/3daa498e-ff33-460f-afa4-7af2cd933f9d-24_449_635_1836_629.jpg)
(a) Even function

![](./images/3daa498e-ff33-460f-afa4-7af2cd933f9d-24_450_665_1830_1310.jpg)
(b) Odd function

It is clear from the graphs in Figure 6 (or by a simple change of variables) that if $f$ is even, then

$$
\int_{-p}^{p} f(x) d x=2 \int_{0}^{p} f(x) d x
$$

and if $f$ is odd, then

$$
\int_{-p}^{p} f(x) d x=0
$$

The following useful properties concerning the products of these functions are easily verified.

$$
\begin{aligned}
(\text { Even })(\text { Even }) & =\text { Even } \\
(\text { Even })(\text { Odd }) & =\text { Odd } \\
(\text { Odd })(\text { Odd }) & =\text { Even }
\end{aligned}
$$

These simple product properties can be used to simplify finding the Fourier coefficients of even and odd functions, as we now show.

THEOREM 2 FOURIER SERIES OF EVEN AND ODD FUNCTIONS

Suppose that $f$ is $2 p$-periodic and has the Fourier series representation (2). Then (i) $f$ is even if and only if $b_{n}=0$ for all $n$. In this case

$$
f(x)=a_{0}+\sum_{n=1}^{\infty} a_{n} \cos \frac{n \pi}{p} x
$$

where

$$
a_{0}=\frac{1}{p} \int_{0}^{p} f(x) d x, \quad \text { and } \quad a_{n}=\frac{2}{p} \int_{0}^{p} f(x) \cos \frac{n \pi}{p} x d x \quad(n=1,2, \ldots)
$$

(ii) $f$ is odd if and only if $a_{n}=0$ for all $n$. In this case

$$
f(x)=\sum_{n=1}^{\infty} b_{n} \sin \frac{n \pi}{p} x
$$

where

$$
b_{n}=\frac{2}{p} \int_{0}^{p} f(x) \sin \frac{n \pi}{p} x d x \quad(n=1,2, \ldots)
$$

Proof (i) If $f(x)=a_{0}+\sum_{n=1}^{\infty} a_{n} \cos \frac{n \pi}{p} x$, then clearly it is even. Conversely, suppose that $f$ is even. Use (10) and the fact that $f(x) \sin \frac{n \pi}{p} x$ is odd to get that $b_{n}=0$ for all $n$. Use (3), (4), (9) and the fact that $f(x) \cos \frac{n \pi}{p} x$ is even to get the formulas for the coefficients in (i). The proof of (ii) is similar and is left as an exercise.

![](./images/3daa498e-ff33-460f-afa4-7af2cd933f9d-26_385_535_490_108.jpg)
Figure 7 An even function.

![](./images/3daa498e-ff33-460f-afa4-7af2cd933f9d-26_371_533_1149_126.jpg)
Figure 8 Partial sums of the Fourier series in Example 4.

![](./images/3daa498e-ff33-460f-afa4-7af2cd933f9d-26_388_548_2061_124.jpg)

Figure 9 The odd function in Example 5.

## EXAMPLE 4 Fourier series of an even function

Find the Fourier series of the 2 -periodic function $f(x)=1-x^{2}$ if $-1<x<1$.
Solution The function $f$ is even (see Figure 7); hence $b_{n}=0$ for all $n$. To compute the $a_{n}$ 's, we use Theorem 2 with $p=1$ and get

$$
a_{0}=\int_{0}^{1}\left(1-x^{2}\right) d x=\frac{2}{3}
$$

and

$$
a_{n}=2 \int_{0}^{1}\left(1-x^{2}\right) \cos n \pi x d x=-2 \int_{0}^{1} x^{2} \cos n \pi x d x=\frac{-4(-1)^{n}}{\pi^{2} n^{2}}
$$

In computing the last integral we used the formula

$$
\int x^{2} \cos n \pi x d x=\frac{2 x \cos n \pi x}{\pi^{2} n^{2}}-\frac{2 \sin n \pi x}{\pi^{3} n^{3}}+\frac{x^{2} \sin n \pi x}{\pi n}
$$

which can be derived by two integrations by parts. Since $f$ is continuous and piecewise smooth, we get

$$
f(x)=\frac{2}{3}-\frac{4}{\pi^{2}} \sum_{n=1}^{\infty} \frac{(-1)^{n}}{n^{2}} \cos n \pi x,
$$

for all $x$. Since $f$ is continuous and piecewise smooth for all $x$, its Fourier series converges uniformly to $f(x)$, as illustrated in Figure 8.

## EXAMPLE 5 Fourier series of an odd function

The function $f(x)=x \cos x$, if $-\frac{\pi}{2}<x<\frac{\pi}{2}$, and $f(x+\pi)=f(x)$ otherwise, is shown in Figure 9. It is $\pi$-periodic and odd. From Theorem 2, its Fourier series is given by

$$
\sum_{n=1}^{\infty} b_{n} \sin 2 n x
$$

where

$$
b_{n}=\frac{4}{\pi} \int_{0}^{\pi / 2} x \cos x \sin 2 n x d x
$$

In evaluating this integral, we will need the addition formula

$$
\cos a \sin b=\frac{1}{2}(\sin (a+b)-\sin (a-b))
$$

and the integral formula

$$
\int u \sin u d u=\sin u-u \cos u+C
$$

![](./images/3daa498e-ff33-460f-afa4-7af2cd933f9d-27_362_454_895_56.jpg)
Figure 10 Graphs of $f(x)$, $s_{2}(x)$ and $s_{4}(x)$, in Example 5.

Computing with the help of these formulas, we find

$$
\begin{aligned}
b_{n}= & \frac{2}{\pi} \int_{0}^{\pi / 2} x(\sin (2 n+1) x+\sin (2 n-1) x) d x \\
= & \left.\frac{2}{\pi(2 n+1)^{2}}(\sin (2 n+1) x-(2 n+1) x \cos (2 n+1) x)\right|_{0} ^{\pi / 2} \\
& +\left.\frac{2}{\pi(2 n-1)^{2}}(\sin (2 n-1) x-(2 n-1) x \cos (2 n-1) x)\right|_{0} ^{\pi / 2} \\
= & \frac{2}{\pi(2 n+1)^{2}} \sin (2 n+1) \frac{\pi}{2}+\frac{2}{\pi(2 n-1)^{2}} \sin (2 n-1) \frac{\pi}{2} \\
= & \frac{2}{\pi}(-1)^{n}\left[\frac{1}{(2 n+1)^{2}}-\frac{1}{(2 n-1)^{2}}\right] \\
& \left(\text { since } \sin (2 n+1) \frac{\pi}{2}=(-1)^{n} \text { and } \sin (2 n-1) \frac{\pi}{2}=(-1)^{n+1}\right) \\
= & \frac{16}{\pi}(-1)^{n+1} \frac{n}{(2 n+1)^{2}(2 n-1)^{2}}
\end{aligned}
$$

Thus

$$
f(x)=\frac{16}{\pi}\left[\frac{1}{9} \sin 2 x-\frac{2}{225} \sin 4 x+\ldots\right]
$$

Figure 10 illustrates the uniform convergence of the Fourier series to $f(x)$. Along with $f(x)$, we have plotted the partial sums $s_{2}(x)$ and $s_{4}(x)$. The graphs of $s_{4}(x)$ and $f(x)$ can hardly be distinguished from one another, which suggests that the Fourier series converges very fast to $f(x)$.

In the next section we use Fourier series of even and odd functions to periodically extend functions that are defined on finite intervals. As we will see in Chapter 8, this process will be needed in solving partial differential equations by means of Fourier series.

## Exercises 7.3

In Exercises 1-10, a 2p-periodic function is given on an interval of length $2 p$ in the accompanying figure (Figures 11-20). (a) State whether the function is even, odd, or neither. (b) Derive the given Fourier series, and determine its values at the points of discontinuity. State if the series converges uniformly for all $x$. (Most of these Fourier series can be derived from earlier examples and exercises, as illustrated by Examples 3 and 4.)

![](./images/3daa498e-ff33-460f-afa4-7af2cd933f9d-27_240_444_2135_42.jpg)
Figure 11

1. 

$$
f(x)= \begin{cases}1 & \text { if } 0<x<p \\ -1 & \text { if }-p<x<0\end{cases}
$$

Fourier series: $\frac{4}{\pi} \sum_{k=0}^{\infty} \frac{1}{(2 k+1)} \sin \frac{(2 k+1) \pi}{p} x$.

![](./images/3daa498e-ff33-460f-afa4-7af2cd933f9d-28_252_547_191_62.jpg)
Figure 12

![](./images/3daa498e-ff33-460f-afa4-7af2cd933f9d-28_244_537_490_74.jpg)
Figure 13

![](./images/3daa498e-ff33-460f-afa4-7af2cd933f9d-28_238_550_814_76.jpg)
Figure 14

![](./images/3daa498e-ff33-460f-afa4-7af2cd933f9d-28_242_545_1167_85.jpg)
Figure 15

![](./images/3daa498e-ff33-460f-afa4-7af2cd933f9d-28_244_551_1517_85.jpg)
Figure 16

![](./images/3daa498e-ff33-460f-afa4-7af2cd933f9d-28_251_556_1884_87.jpg)
Figure 17

![](./images/3daa498e-ff33-460f-afa4-7af2cd933f9d-28_261_575_2298_78.jpg)
Figure 18

2. $f(x)=x$ if $-p<x<p$. [Hint: Exercise 13, Section 7.2.]

Fourier series: $\quad \frac{2 p}{\pi} \sum_{n=1}^{\infty} \frac{(-1)^{n+1}}{n} \sin \left(\frac{n \pi}{p} x\right)$.
3. $f(x)=a\left(1-\left(\frac{x}{p}\right)^{2}\right)$ if $-p \leq x \leq p,(a \neq 0)$.

Fourier series: $\quad \frac{2}{3} a+4 a \sum_{n=1}^{\infty} \frac{(-1)^{n+1}}{(n \pi)^{2}} \cos \left(\frac{n \pi}{p} x\right)$.
4. $f(x)=x^{2}$ if $-p \leq x \leq p$. [Hint: Use Exercise 3.]

Fourier series: $\frac{p^{2}}{3}-\frac{4 p^{2}}{\pi^{2}}\left[\cos \left(\frac{\pi}{p} x\right)-\frac{1}{2^{2}} \cos \left(\frac{2 \pi}{p} x\right)+\frac{1}{3^{2}} \cos \left(\frac{3 \pi}{p} x\right)-\ldots\right]$.
5.

$$
f(x)= \begin{cases}-\frac{2 c}{p}(x-p / 2) & \text { if } 0 \leq x \leq p \\ \frac{2 c}{p}(x+p / 2) & \text { if }-p \leq x \leq 0\end{cases}
$$

where $c \neq 0$ (in the picture $c>0$.)
Fourier series: $\quad \frac{8 c}{\pi^{2}} \sum_{k=0}^{\infty} \frac{1}{(2 k+1)^{2}} \cos \left((2 k+1) \frac{\pi}{p} x\right)$.
6.

$$
f(x)= \begin{cases}c & \text { if }|x|<d \\ 0 & \text { if } d<|x|<p\end{cases}
$$

where $0<d<p$.
Fourier series: $\frac{c d}{p}+\frac{2 c}{\pi} \sum_{n=0}^{\infty} \frac{\sin \left(\frac{d n \pi}{p}\right)}{n} \cos \left(\frac{n \pi}{p} x\right)$.
7.

$$
f(x)= \begin{cases}-\frac{2}{p}(x-p / 2) & \text { if } 0<x<p \\ -\frac{2}{p}(x+p / 2) & \text { if }-p<x<0\end{cases}
$$

Fourier series: $\frac{4}{\pi} \sum_{k=1}^{\infty} \frac{1}{2 k} \sin \left(\frac{2 k \pi}{p} x\right)$.
8.

$$
f(x)= \begin{cases}-\frac{c}{d}(x-d) & \text { if } 0 \leq x \leq d \\ 0 & \text { if } d \leq|x| \leq p \\ \frac{c}{d}(x+d) & \text { if }-d \leq x \leq 0\end{cases}
$$

where $0 \leq d \leq p$.
Fourier series: $\frac{c d}{2 p}+\frac{2 c p}{d \pi^{2}} \sum_{n=1}^{\infty} \frac{1}{n^{2}}\left(1-\cos \left(\frac{d n \pi}{p}\right)\right) \cos \left(\frac{n \pi}{p} x\right)$.
![](./images/3daa498e-ff33-460f-afa4-7af2cd933f9d-29_272_478_146_37.jpg)

Figure 19
9. $f(x)=e^{-c|x|}(c \neq 0)$ for $|x| \leq p$.

Fourier series: $\frac{1}{p c}\left(1-e^{-c p}\right)+2 c p \sum_{n=1}^{\infty} \frac{1}{c^{2} p^{2}+(n \pi)^{2}}\left(1-e^{-c p}(-1)^{n}\right) \cos \left(\frac{n \pi}{p} x\right)$.
10.

![](./images/3daa498e-ff33-460f-afa4-7af2cd933f9d-29_264_478_495_36.jpg)
Figure 20

$$
f(x)= \begin{cases}-\frac{1}{p-c}(x-p) & \text { if } c<x<p, \\ 1 & \text { if }|x|<c, \\ \frac{1}{p-c}(x+p) & \text { if }-p<x<-c,\end{cases}
$$

where $0<c<p$.
Fourier series: $\quad \frac{p+c}{2 p}+\frac{2 p}{(c-p) \pi^{2}} \sum_{n=1}^{\infty} \frac{1}{n^{2}}\left((-1)^{n}-\cos \left(\frac{c n \pi}{p}\right)\right) \cos \left(\frac{n \pi}{p} x\right)$.
11. (a) Find the Fourier series of the $2 \pi$-periodic function given on the interval $-\pi<x<\pi$ by $f(x)=x \sin x$.
(b) Plot several partial sums to illustrate the convergence of the Fourier series.
12. (a) Find the Fourier series of the $2 \pi$-periodic function given on the interval $-\pi<x<\pi$ by $f(x)=(\pi-x) \sin x$. [Hint: Exercise 11.]
(b) Plot several partial sums to illustrate the convergence of the Fourier series.

In Exercises 13-14 a function is given over one period by a figure (Figures 21-22).
(a) Find its Fourier series. [Hint: Use Exercise 1.]
(b) Plot several partial sums to illustrate the convergence of the Fourier series.

## 13.

![](./images/3daa498e-ff33-460f-afa4-7af2cd933f9d-29_299_571_1452_618.jpg)
Figure 21

14. 

![](./images/3daa498e-ff33-460f-afa4-7af2cd933f9d-29_297_577_1452_1310.jpg)
Figure 22

15. Obtain the Fourier series of Example 2, Section 7.2, from Example 2 of this section.
16. (a) Illustrate graphically the answer in Exercise 6 by taking $p=1, c=1, d=\frac{1}{2}$ and by plotting several partial sums of the Fourier series.
(b) What happens to the Fourier coefficients as $d$ approaches $p$ ? Justify your answer.
17. Use the result of Exercise 4 to derive the formulas
(a) $\frac{\pi^{2}}{12}=1-\frac{1}{2^{2}}+\frac{1}{3^{2}}-\frac{1}{4^{2}}+\cdots$
(b) $\frac{\pi^{2}}{8}=1+\frac{1}{3^{2}}+\frac{1}{5^{2}}+\frac{1}{7^{2}}+\cdots$ [Hint: Use (a) also.]
18. Derive (4) and (5) of Theorem 1. [Hint: Study the proof of Theorem 1.]
19. Prove part (ii) of Theorem 2.

Project Problem: Decomposition into even and odd parts. Do Exercise 20 and any one of 21-24. You will discover how an arbitrary function can be decom-
posed into the sum of an even and odd function.
20. Let $f$ be an arbitrary function defined for all real numbers. Consider the functions

$$
f_{\mathrm{e}}(x)=\frac{f(x)+f(-x)}{2} \text { and } f_{\mathrm{o}}(x)=\frac{f(x)-f(-x)}{2}
$$

(a) Show that $f_{\mathrm{e}}$ is even and $f_{\mathrm{o}}$ is odd.
(b) Show that $f=f_{\mathrm{e}}+f_{\mathrm{o}}$. Hence every function is the sum of an even function and an odd function. Moreover, show that this decomposition is unique.
(c) In the remainder of this exercise, we suppose that $f$ is $2 p$-periodic. Show that $f_{\mathrm{e}}$ and $f_{\mathrm{o}}$ are both $2 p$-periodic.
(d) Let $a_{0}, a_{1}, a_{2}, \ldots, b_{1}, b_{2}, \ldots$ denote the Fourier coefficients of $f$. Show that the Fourier series of $f_{\mathrm{e}}$ is $a_{0}+\sum_{n=1}^{\infty} a_{n} \cos \frac{n \pi}{p} x$, and the Fourier series of $f_{\mathrm{o}}$ is $\sum_{n=1}^{\infty} b_{n} \sin \frac{n \pi}{p} x$.
In Exercises 21-24, a 2 -periodic function is given by its graph over the interval $[-1,1]$ (Figures 23-26). In each case, (a) determine and plot $f_{\mathrm{e}}$ and $f_{\mathrm{o}}$ (see Exercise 20).
(b) Find the Fourier series of $f_{e}$ and $f_{o}$, and then deduce the Fourier series of $f$.
21.

![](./images/3daa498e-ff33-460f-afa4-7af2cd933f9d-30_277_559_1096_714.jpg)
Figure 23

23. 

![](./images/3daa498e-ff33-460f-afa4-7af2cd933f9d-30_286_553_1493_728.jpg)
Figure 25

22. 

![](./images/3daa498e-ff33-460f-afa4-7af2cd933f9d-30_283_612_1082_1383.jpg)
Figure 24

24. 

![](./images/3daa498e-ff33-460f-afa4-7af2cd933f9d-30_281_609_1493_1395.jpg)
Figure 26

Project Problem: Differentiation of Fourier series. Can a Fourier series be differentiated term by term? The answer is no, in general. Do Exercises 25, 26, and any one of 27-30, and you will learn when you can safely use this process.
25. Fourier series and derivatives. Suppose that $f$ is a $2 p$-periodic, piecewise smooth and continuous function such that $f^{\prime}$ is also piecewise smooth. Let $a_{n}, b_{n}$ denote the Fourier coefficients of $f$ and $a_{n}^{\prime}, b_{n}^{\prime}$ those of $f^{\prime}$. Show that

$$
a_{0}^{\prime}=0, \quad a_{n}^{\prime}=b_{n} \frac{n \pi}{p}, \quad \text { and } \quad b_{n}^{\prime}=-a_{n} \frac{n \pi}{p}
$$

[Hint: To compute the Fourier coefficients of $f^{\prime}$, evaluate the integrals by parts and use $f(p)=f(-p)$.]
26. Term-by-term differentiation of Fourier series. Suppose that $f$ is a $2 p$ periodic piecewise smooth and continuous function such that $f^{\prime}$ is also piecewise

![](./images/3daa498e-ff33-460f-afa4-7af2cd933f9d-31_224_448_1096_54.jpg)
Figure 27 for Exercise 29.

![](./images/3daa498e-ff33-460f-afa4-7af2cd933f9d-31_228_454_1463_56.jpg)
Figure 28 for Exercise 30.

smooth. Show that the Fourier series of $f^{\prime}$ is obtained from the Fourier series of $f$ by differentiating term by term. That is, under the stated conditions, if

$$
f(x)=a_{0}+\sum_{n=1}^{\infty}\left(a_{n} \cos \frac{n \pi}{p} x+b_{n} \sin \frac{n \pi}{p} x\right),
$$

then

$$
f^{\prime}(x)=\sum_{n=1}^{\infty}\left(-n a_{n} \frac{\pi}{p} \sin \frac{n \pi}{p} x+n b_{n} \frac{\pi}{p} \cos \frac{n \pi}{p} x\right)
$$

[Hint: Since $f^{\prime}$ satisfies the hypothesis of Theorem 1 it has a Fourier series expansion. Use Exercise 25 to compute the Fourier coefficients. Compare with the differentiated Fourier series of $f$.]

In most cases in this book, $f$ and $f^{\prime}$ are piecewise smooth. Thus, according to Exercise 26, to differentiate term by term the Fourier series in these cases, it is enough to check that $f$ is continuous. It is important to note that if $f$ fails to satisfy some of the assumptions of Exercise 26, then we cannot in general differentiate the series term by term. See Exercises 31-32.
27. Derive the Fourier series in Exercise 1 by differentiating term by term the Fourier series in Exercise 5. Justify your work.
28. Derive the Fourier series in Exercise 2 by differentiating term by term the Fourier series in Exercise 4. Justify your work.
29. Use the Fourier series of Exercise 8 to find the Fourier series of the $2 p$-periodic function in the Figure 27.
30. Use the Fourier series of Exercise 10 to find the Fourier series of the $2 p$-periodic function in the Figure 28.
Project Problem: Failure of term-by-term differentiation. Do Exercises 31-32 to show that the Fourier series of the sawtooth function (a piecewise smooth function) cannot be differentiated term by term.
31. Show that the series $\sum_{n=1}^{\infty} \cos n x$ is divergent for all $x$. [Hint: Apply the $n$th term test and Exercise 8, Section 4.1.]
32. Failure of term-by-term differentiation. Consider the Fourier series of the sawtooth function $\sum_{n=1}^{\infty} \frac{\sin n x}{n}$.
(a) Show that the function represented by this Fourier series satisfies all the hypotheses of Exercise 26, except that it fails to be continuous.
(b) Show that the series cannot be differentiated term by term. [Hint: Exercise 31.]
33. Project Problem: Term-by-term integration of Fourier series. Let $f$ be as in Theorem 1, and define an antiderivative of $f$ by

$$
F(x)=\int_{0}^{x} f(t) d t
$$

From Exercises 15-16, Section 7.1, we know that $F$ is $2 p$-periodic if and only if $\int_{0}^{2 p} f(t) d t=0$. Show that, in this case, the Fourier series of $F$ is

$$
F(x)=A_{0}+\sum_{n=1}^{\infty}\left(\frac{p}{n \pi} a_{n} \sin \frac{n \pi}{p} x-\frac{p}{n \pi} b_{n} \cos \frac{n \pi}{p} x\right),
$$

where $A_{0}=\frac{p}{\pi} \sum_{n=1}^{\infty} \frac{b_{n}}{n}$. Hence, as long as $F$ is periodic, with no further assumptions on $f$ other than piecewise smoothness, we can get the Fourier series of $F$ by integrating term by term the Fourier series of $f$. [Hint: Apply the result of Exercise 25 to $F(x)$ and use $F^{\prime}(x)=f(x)$. To compute $A_{0}$, use $F(0)=0$ (why?).]
34. Use Exercise 33 to derive the Fourier series of Exercise 4 from that of Exercise 2.

### 7.4 Half-Range Expansions: The Cosine and Sine Series

In many applications we are interested in representing by a Fourier series a function $f(x)$ that is defined only in a finite interval, say $0<x<p$. Since $f$ is clearly not periodic, the results of the previous sections are not readily applicable. Our goal in this section is to show how we can represent $f$ by a Fourier series, after extending it to a periodic function.

THEOREM 1 HALF-RANGE EXPANSIONS

Suppose that $f(x)$ is a piecewise smooth function defined on an interval $0<x<p$. Then $f$ has a cosine series expansion
(1)

$$
a_{0}+\sum_{n=1}^{\infty} a_{n} \cos \frac{n \pi}{p} x \quad(0<x<p),
$$

where

$$
a_{0}=\frac{1}{p} \int_{0}^{p} f(x) d x ; \quad a_{n}=\frac{2}{p} \int_{0}^{p} f(x) \cos \frac{n \pi}{p} x d x \quad(n \geq 1)
$$

Also, $f$ has a sine series expansion

$$
\sum_{n=1}^{\infty} b_{n} \sin \frac{n \pi}{p} x \quad(0<x<p)
$$

where
(4)

$$
b_{n}=\frac{2}{p} \int_{0}^{p} f(x) \sin \frac{n \pi}{p} x d x \quad(n \geq 1)
$$

On the interval $0<x<p$, the series (1) and (3) converge to $f(x)$ if $f$ is continuous at $x$ and to $\frac{f(x+)+f(x-)}{2}$ otherwise.

The series (1) and (3) are commonly referred to as the half-range expansions of $f$. They are two different series representations of the same function on the interval $0<x<p$. Theorem 1 will be derived by appealing to the Fourier series representation of even and odd functions (Theorem 2, Section 7.3). For this purpose, we introduce the following notions.

Define the even periodic extension of $f$ by $f_{1}(x)=f(x)$ if $0<x<p$, $f_{1}(x)=f(-x)$ if $-p<x<0$, and $f_{1}(x)=f_{1}(x+2 p)$ otherwise. Define the odd periodic extension of $f$ by $f_{2}(x)=f(x)$ if $0<x<p, f_{2}(x)= -f(-x)$ if $-p<x<0$, and $f_{2}(x)=f_{2}(x+2 p)$ otherwise. (In view of the
remark following Theorem 1 of Section 7.2, we will not worry about the definition of the extensions at the points $0, \pm p, \pm 2 p, \ldots$.)

![](./images/3daa498e-ff33-460f-afa4-7af2cd933f9d-33_424_571_317_68.jpg)
Figure 1 (a) $f(x), 0<x<p$.

![](./images/3daa498e-ff33-460f-afa4-7af2cd933f9d-33_424_620_327_710.jpg)
(b) Even $2 p$-periodic extension, $f_{1}$.

![](./images/3daa498e-ff33-460f-afa4-7af2cd933f9d-33_428_621_323_1397.jpg)
(c) Odd $2 p$-periodic extension, $f_{2}$.

By the way they are constructed, the function $f_{1}$ is even and $2 p$-periodic, and the function $f_{2}$ is odd and $2 p$-periodic. Both functions agree with $f$ on the interval $0<x<p$ which justifies calling them extensions of $f$ (Figure 1). Since $f$ is piecewise smooth, it follows that $f_{1}$ and $f_{2}$ are both piecewise smooth. Applying Theorem 2 of Section 7.3, we find that $f_{1}$ has a cosine series expansion given by (1) with the coefficients (2). Now $f(x)=f_{1}(x)$ for all $0<x<p$, and so the cosine series (1) represents $f$ on this interval. Similar reasoning using $f_{2}$ yields the sine series expansion of $f$.

## EXAMPLE 1 Half-range expansions

Find the half-range expansions of the function $f(x)=x$ for $0<x<1$.
Solution The graphs of the even and odd extensions are shown in Figure 2.

![](./images/3daa498e-ff33-460f-afa4-7af2cd933f9d-33_284_405_1481_164.jpg)
Figure 2 (a) $f(x)=x, 0<x<1$.

![](./images/3daa498e-ff33-460f-afa4-7af2cd933f9d-33_276_646_1481_694.jpg)
(b) Even extension of $f$, period 2.

![](./images/3daa498e-ff33-460f-afa4-7af2cd933f9d-33_276_647_1487_1383.jpg)
(c) Odd extension of $f$, period 2 .

The even extension is a special case of Example 1 of Section 7.3 with $p=1$. We have

$$
x=\frac{1}{2}-\frac{4}{\pi^{2}} \sum_{k=0}^{\infty} \frac{1}{(2 k+1)^{2}} \cos (2 k+1) \pi x, \quad \text { for all } 0 \leq x \leq 1 .
$$

The odd extension is a special case of Exercise 2 of Section 7.3, with $p=1$. However, to illustrate the formulas of Theorem 1, we will derive the sine coefficients using (4). We have

$$
b_{n}=\frac{2}{1} \int_{0}^{1} x \sin n \pi x d x=\frac{2(-1)^{n+1}}{n \pi}
$$

Hence

$$
x=\frac{2}{\pi} \sum_{n=1}^{\infty} \frac{(-1)^{n+1}}{n} \sin n \pi x, \quad 0 \leq x<1 .
$$

It is a remarkable fact that the cosine series and the sine series have the same values on the intervals $(0,1),(2,3),(-2,-1), \ldots$.

## EXAMPLE 2 Half-range expansions

Consider the function $f(x)=\sin x, 0 \leq x \leq \pi$. If we take its odd extension, we get the usual sine function, $f_{2}(x)=\sin x$ for all $x$. Thus, the sine series expansion is just $\sin x$.

![](./images/3daa498e-ff33-460f-afa4-7af2cd933f9d-34_302_554_569_151.jpg)
Figure 3 (a) $f(x)=\sin x, 0 \leq x \leq \pi$.

![](./images/3daa498e-ff33-460f-afa4-7af2cd933f9d-34_300_572_561_805.jpg)
(b) Odd extension of $f, \sin x$.

![](./images/3daa498e-ff33-460f-afa4-7af2cd933f9d-34_307_606_552_1454.jpg)
(c) Even extension of $f,|\sin x|$.

$$
\sin x=\frac{2}{\pi}-\frac{4}{\pi} \sum_{k=1}^{\infty} \frac{1}{(2 k)^{2}-1} \cos 2 k x, \quad 0 \leq x \leq \pi
$$

## Exercises 7.4

In Exercises 1-8, (a) find the half-range expansions of the given function. (Use as much as possible series that you have encountered earlier.)
(b) To illustrate the convergence of the cosine and sine series, plot several partial sums of each and comment on the graphs.

1. $f(x)=1$ if $0<x<1$.
2. $f(x)=\pi-x$ if $0 \leq x \leq \pi$.
3. $f(x)=x^{2}$ if $0<x<1$.
4. 

$$
f(x)= \begin{cases}0 & \text { if } 0 \leq x<1, \\ x-1 & \text { if } 1 \leq x<2 .\end{cases}
$$

5. 

$$
f(x)= \begin{cases}1 & \text { if } a<x<b \\ 0 & \text { if } 0<x<a \\ & \text { or } b<x<p\end{cases}
$$

where $0<a<b<p<\infty$. For (b), take $p=1, a=\frac{1}{4}, b=\frac{1}{2}$.
6. $f(x)=\cos x$ if $0<x<\pi$.
7. $f(x)=\cos x$ if $0 \leq x \leq \frac{\pi}{2}$.
8. $f(x)=x \sin x$ if $0<x<\pi$.

In Exercises 9-16, find the sine series expansion of the given function on the interval $0<x<1$.
9. $x(1-x)$.
10. $1-x^{2}$.
11. $\sin \pi x$.
12. $\sin \frac{\pi}{2} x$.
13. $\sin \pi x \cos \pi x$.
14. $(1+\cos \pi x) \sin \pi x$.
15. $e^{x}$.
16. $1-e^{x}$.

![](./images/3daa498e-ff33-460f-afa4-7af2cd933f9d-35_415_469_181_65.jpg)
Figure 4 for Exercise 17.

17. Triangular function. Let $f(x)$ denote the shape of a plucked string of length $p$ with endpoints fastened at $x=0$ and $x=p$, as shown in Figure 4.
(a) Using the data in the figure, derive the formula

$$
f(x)= \begin{cases}\frac{h}{a} x & \text { if } 0 \leq x \leq a \\ \frac{h}{a-p}(x-p) & \text { if } a \leq x \leq p\end{cases}
$$

(b) Obtain the sine series representation of $f$ :

$$
f(x)=\frac{2 h p^{2}}{a(-a+p) \pi^{2}} \sum_{n=1}^{\infty} \frac{\sin \frac{a n \pi}{p}}{n^{2}} \sin \frac{n \pi}{p} x
$$

(c) Verify this representation by taking $a=1 / 3, p=1, h=1 / 10$ and plotting the resulting function $f$ along with several partial sums of the Fourier series.

### 7.5 Complex Form of Fourier Series

In previous sections, we have used the formulas

$$
\cos u=\frac{e^{i u}+e^{-i u}}{2} \quad \text { and } \quad \sin u=\frac{e^{i u}-e^{-i u}}{2 i}
$$

several times with tools from complex analysis to compute Fourier series. In this section, we will consider a Fourier series

$$
f(x)=a_{0}+\sum_{n=1}^{\infty}\left(a_{n} \cos \frac{n \pi}{p} x+b_{n} \sin \frac{n \pi}{p} x\right)
$$

and then, using (2), we will replace the cosine and sine by their expressions in terms of the complex exponential and derive the complex form of the Fourier series, which is expressed as follows.

THEOREM 1 COMPLEX FORM OF FOURIER SERIES

Let $f$ be a $2 p$-periodic piecewise smooth function. The complex form of the Fourier series of $f$ is

$$
\sum_{n=-\infty}^{\infty} c_{n} e^{i \frac{n \pi}{p} x}
$$

where the Fourier coefficients $c_{n}$ are given by

$$
c_{n}=\frac{1}{2 p} \int_{-p}^{p} f(t) e^{-i \frac{n \pi}{p} t} d t \quad(n=0, \pm 1, \pm 2, \ldots)
$$

For all $x$, the Fourier series converges to $f(x)$ if $f$ is continuous at $x$, and to $\frac{f(x+)+f(x-)}{2}$ otherwise. Moreover, the Fourier series converges to $f(x)$ uniformly for all $x$ if and only if $f$ is continuous for all $x$ (and piecewise smooth).

The Fourier coefficients $c_{n}$ are also denoted by $\widehat{f}(n)$. The $N$ th partial sum of (3) is by definition the symmetric sum

$$
S_{N}(x)=\sum_{n=-N}^{N} c_{n} e^{i \frac{n \pi}{p} x}
$$

We will see in a moment that $S_{N}(x)$ is the same as the usual partial sum of the Fourier series

$$
s_{N}(x)=a_{0}+\sum_{n=1}^{N}\left(a_{n} \cos \frac{n \pi}{p} x+b_{n} \sin \frac{n \pi}{p} x\right)
$$

Proof of Theorem 1 It is enough to show that $S_{N}=s_{N}$, then the theorem will follow from Theorem 1, Section 7.3. We clearly have $c_{0}=a_{0}$. For $n>0$, using (1), we get

$$
\begin{aligned}
a_{n} \cos \frac{n \pi}{p} x+b_{n} \sin \frac{n \pi}{p} x & =a_{n} \frac{e^{i \frac{n \pi}{p} x}+e^{-i \frac{n \pi}{p} x}}{2}+b_{n} \frac{e^{i \frac{n \pi}{p} x}-e^{-i \frac{n \pi}{p} x}}{2 i} \\
& =\frac{1}{2}\left(a_{n}+\frac{1}{i} b_{n}\right) e^{i \frac{n \pi}{p} x}+\frac{1}{2}\left(a_{n}-\frac{1}{i} b_{n}\right) e^{-i \frac{n \pi}{p} x} \\
& =\frac{1}{2}\left(a_{n}-i b_{n}\right) e^{i \frac{n \pi}{p} x}+\frac{1}{2}\left(a_{n}+i b_{n}\right) e^{-i \frac{n \pi}{p} x}
\end{aligned}
$$

Using the formulas for $a_{n}$ and $b_{n}$ (Theorem 1, Section 7.3) and (4), we have

$$
\begin{aligned}
\frac{1}{2}\left(a_{n}-i b_{n}\right) & =\frac{1}{2} \frac{1}{p} \int_{-p}^{p} f(t) \cos \frac{n \pi}{p} t d t-\frac{i}{2} \frac{1}{p} \int_{-p}^{p} f(t) \sin \frac{n \pi}{p} t d t \\
& =\frac{1}{2 p} \int_{-p}^{p} f(t)\left(\cos \frac{n \pi}{p} t-i \sin \frac{n \pi}{p} t\right) d t \\
& =\frac{1}{2 p} \int_{-p}^{p} f(t) e^{-i \frac{n \pi}{p} t} d t=c_{n}
\end{aligned}
$$

To simplify the middle integral, we used the identity $e^{-i \theta}=\cos \theta-i \sin \theta$. A similar argument shows that $c_{-n}=\frac{1}{2}\left(a_{n}+i b_{n}\right)$. Thus, for $n \geq 1$,

$$
a_{n} \cos \frac{n \pi}{p} x+b_{n} \sin \frac{n \pi}{p} x=c_{n} e^{i \frac{n \pi}{p} x}+c_{-n} e^{-i \frac{n \pi}{p} x}
$$

and so

$$
s_{N}(x)=a_{0}+\sum_{n=1}^{N}\left(a_{n} \cos \frac{n \pi}{p} x+b_{n} \sin \frac{n \pi}{p} x\right)=c_{0}+\sum_{n=1}^{N} c_{n} e^{i \frac{n \pi}{p} x}+\sum_{n=1}^{N} c_{-n} e^{-i \frac{n \pi}{p} x}
$$

Changing $n$ to $-n$ in the second series on the right and combining, we get that $s_{N}(x)=S_{N}(x)$, and the theorem follows.

![](./images/3daa498e-ff33-460f-afa4-7af2cd933f9d-37_483_491_1353_60.jpg)
Figure $1 \mathrm{~A} 2 \pi$-periodic function, $e^{a x}, a>0,-\pi<x<$ 7

## We can extract the following useful identities from the previous proof.

$$
\begin{aligned}
c_{0} & =a_{0} \\
c_{n}=\frac{1}{2}\left(a_{n}-i b_{n}\right), \quad c_{-n} & =\frac{1}{2}\left(a_{n}+i b_{n}\right) \quad(n>0) \\
a_{n}=c_{n}+c_{-n}, \quad b_{n} & =i\left(c_{n}-c_{-n}\right) \quad(n>0) \\
S_{N}(x) & =s_{N}(x)
\end{aligned}
$$

If $f$ is real-valued, so that $a_{n}$ and $b_{n}$ are both real, then (6) shows that $c_{-n}$ is the complex conjugate of $c_{n}$. In symbols,

$$
c_{-n}=\bar{c}_{n} .
$$

This identity fails in general if $f$ is not real-valued. Consider $f(x)=e^{i x}$. From the orthogonality relations of the complex exponential functions (Exercise 12, Section 3.2), it follows that $c_{1}=1$ and $c_{n}=0$ for all $n \neq 1$ (Exercise 9). Hence, $c_{-1} \neq \bar{c}_{1}$.

The complex form of the Fourier series is particularly useful when dealing with exponential functions, as we now illustrate.

## EXAMPLE 1 A complex Fourier series

Find the complex form of the Fourier series of the $2 \pi$-periodic function $f(x)=e^{a x}$ for $-\pi<x<\pi$, where $a \neq 0, \pm i, \pm 2 i, \pm 3 i, \ldots$. Determine the values of the Fourier series at $x= \pm \pi$.

Solution From (4), we have

$$
c_{n}=\frac{1}{2 \pi} \int_{-\pi}^{\pi} e^{a x} e^{-i n x} d x=\frac{1}{2 \pi}\left[\frac{e^{(a-i n) x}}{a-i n}\right]_{-\pi}^{\pi}=\frac{(-1)^{n}}{a-i n} \frac{\sinh \pi a}{\pi},
$$

where we have used $e^{ \pm i n \pi}=(-1)^{n}$ and $\sinh \pi a=\frac{e^{\pi a}-e^{-\pi a}}{2}$. Plugging these coefficients into (3) and simplifying, we obtain the complex form of the Fourier series of $f$

$$
\frac{\sinh \pi a}{\pi} \sum_{n=-\infty}^{\infty} \frac{(-1)^{n}}{a-i n} e^{i n x}=\frac{\sinh \pi a}{\pi} \sum_{n=-\infty}^{\infty} \frac{(-1)^{n}}{a^{2}+n^{2}}(a+i n) e^{i n x} .
$$

(We remind you that here and throughout the section the doubly infinite Fourier series represents the limit of the symmetric partial sums, $\sum_{n=-N}^{N}$.) Applying Theorem 1 to $f(x)$, we obtain the Fourier series representation

$$
e^{a x}=\frac{\sinh \pi a}{\pi} \sum_{n=-\infty}^{\infty} \frac{(-1)^{n}}{a^{2}+n^{2}}(a+i n) e^{i n x} \quad(-\pi<x<\pi) .
$$

According to Theorem 1, the values of the Fourier series at the points of discontinuity, and in particular at $x= \pm \pi$, are given by the average of the function at
these points. With the help of Figure 1, we see that this average is

$$
\frac{e^{a \pi}+e^{-a \pi}}{2}=\cosh a \pi
$$

As a specific illustration, if you take $x=\pi$ in the Fourier series, you obtain the interesting identity

$$
\cosh a \pi=\frac{\sinh \pi a}{\pi} \sum_{n=-\infty}^{\infty} \frac{a+i n}{a^{2}+n^{2}}, \quad a \neq 0, \pm i, \pm 2 i, \pm 3 i, \ldots .
$$

We have used $e^{i n \pi}=(-1)^{n}$ and $(-1)^{n}(-1)^{n}=1$ to simplify the series. (See Exercises 12 and 13 for related results.) Finally, let us note that if $a= \pm i n$, then $f(x)=e^{ \pm i n x}$, and hence $f$ is its own Fourier series.

EXAMPLE 2 The (usual) Fourier series from the complex form
Obtain the usual Fourier series of the function in Example 1 from its complex form. Take $a$ to be a real number $\neq 0$.
Solution The point here is not to use the Euler formulas of Section 7.2 to compute the Fourier series. Instead, we will use Example 1 and appropriate formulas relating the Fourier coefficients $a_{n}$ and $b_{n}$ to the complex Fourier coefficients $c_{n}$. From (5) and (10), we obtain

$$
a_{0}=c_{0}=\frac{1}{a} \frac{\sinh \pi a}{\pi}
$$

From (7) and (10), we have

$$
a_{n}=(-1)^{n} \frac{\sinh \pi a}{\pi}\left(\frac{1}{a-i n}+\frac{1}{a+i n}\right)=(-1)^{n} \frac{\sinh \pi a}{\pi} \frac{2 a}{a^{2}+n^{2}}
$$

and

$$
b_{n}=i(-1)^{n} \frac{\sinh \pi a}{\pi}\left(\frac{1}{a-i n}-\frac{1}{a+i n}\right)=-(-1)^{n} \frac{\sinh \pi a}{\pi} \frac{2 n}{a^{2}+n^{2}}
$$

![](./images/3daa498e-ff33-460f-afa4-7af2cd933f9d-38_516_528_1843_81.jpg)

Thus, the Fourier series of $f$ is

$$
\frac{1}{a} \frac{\sinh \pi a}{\pi}+\frac{\sinh \pi a}{\pi} \sum_{n=1}^{\infty} \frac{(-1)^{n}}{a^{2}+n^{2}}(2 a \cos n x-2 n \sin n x)
$$

In particular, for $-\pi<x<\pi$ and $a \neq 0$, we have

$$
e^{a x}=\frac{1}{a} \frac{\sinh \pi a}{\pi}+\frac{\sinh \pi a}{\pi} \sum_{n=1}^{\infty} \frac{(-1)^{n}}{a^{2}+n^{2}}(2 a \cos n x-2 n \sin n x)
$$

Figure 2 Partial sums of the Fourier series of the $2 \pi$ periodic function $f(x)=e^{x}$, $-\pi<x<\pi$.

Our next example illustrates the use of methods from complex analysis in computing Fourier series. The ideas are similar to those we used in

![](./images/3daa498e-ff33-460f-afa4-7af2cd933f9d-39_521_482_262_62.jpg)
Figure 3 The disk $|z|<|a| (|a|>1)$ contains the circle $|z|=1$.

![](./images/3daa498e-ff33-460f-afa4-7af2cd933f9d-39_528_485_979_55.jpg)
Figure 4 In this figure:

$\operatorname{Re}\left(\frac{1}{2+e^{i \theta}}\right)=\frac{2+\cos \theta}{5+4 \cos \theta} ; s_{2}(\theta)=\frac{1}{2}\left(1-\frac{\cos \theta}{2}+\frac{\cos 2 \theta}{4}\right)$.
![](./images/3daa498e-ff33-460f-afa4-7af2cd933f9d-39_606_468_1781_55.jpg)

Figure 5 In this figure:
$\operatorname{Im}\left(\frac{1}{2+e^{2 \theta}}\right)=\frac{-\sin \theta}{5+4 \cos \theta} ;$
$\delta_{2}(\theta)=-\frac{1}{2}\left(\frac{\sin \theta}{2}-\frac{\sin 2 \theta}{4}\right)$.

Section 7.2 and are based on the applications of Laurent series. The example that we present leads to power series, which are special cases of Laurent series.

## EXAMPLE 3 Using complex power series to compute Fourier series

Let $a$ be a real number with $|a|>1$. The complex-valued function

$$
f(\theta)=\frac{1}{a+e^{i \theta}} \quad(\theta \text { real })
$$

is $2 \pi$-periodic, and because $|a|>1$ and $\left|e^{i \theta}\right|=1$ for all $\theta$, the denominator does not vanish, and so $f$ is smooth. The function $f(\theta)$ is the restriction to the unit circle $\left(z=e^{i \theta}\right)$ of the function $\frac{1}{a+z}$, where $z$ is the variable. Since $|a|>1$, it follows that $\frac{1}{a+z}$ is analytic in the disk $|z|<|a|$, and so it has a power series expansion in $|z|<|a|$, which can be obtained from the geometric series as follows:

$$
\frac{1}{a+z}=\frac{1}{a} \frac{1}{1-\left(-\frac{z}{a}\right)}=\frac{1}{a} \sum_{n=0}^{\infty}(-1)^{n}\left(\frac{z}{a}\right)^{n} \quad(|z|<|a|) .
$$

Since the unit circle $|z|=1$ is contained in the disk $|z|<|a|$, the power series expansion is valid for all $z=e^{i \theta}$ (Figure 3). Substituting $z=e^{i \theta}$, then using $z^{n}=e^{i n \theta}$ and simplifying, we get

$$
f(\theta)=\frac{1}{a+e^{i \theta}}=\frac{1}{a} \sum_{n=0}^{\infty} \frac{(-1)^{n}}{a^{n}} e^{i n \theta},
$$

which is the complex form of the Fourier series of $f(\theta)$. Out of this expansion, we can derive two interesting real Fourier series, by taking the real and imaginary parts of $f(\theta)$. We have (here we will use the fact that $a$ is real)

$$
f(\theta)=\frac{1}{a+e^{i \theta}}=\frac{a+e^{-i \theta}}{\left(a+e^{i \theta}\right)\left(a+e^{-i \theta}\right)}=\frac{a+\cos \theta}{1+a^{2}+2 a \cos \theta}-\frac{i \sin \theta}{1+a^{2}+2 a \cos \theta} .
$$

Substitute this into (11), use $e^{i n \theta}=\cos n \theta+i \sin n \theta$, then equate real and imaginary parts, and get the two Fourier series

$$
\frac{a+\cos \theta}{1+a^{2}+2 a \cos \theta}=\frac{1}{a}\left[1-\frac{\cos \theta}{a}+\frac{\cos 2 \theta}{a^{2}}-\frac{\cos 3 \theta}{a^{3}}+\cdots\right],
$$

and

$$
\frac{-\sin \theta}{1+a^{2}+2 a \cos \theta}=-\frac{1}{a}\left[\frac{\sin \theta}{a}-\frac{\sin 2 \theta}{a^{2}}+\frac{\sin 3 \theta}{a^{3}}+\cdots\right],
$$

which are valid for all $\theta$. In Figures 4 and 5, we plotted the real and imaginary parts of $f$ in the case $a=2$, along with partial sums of their Fourier series. $\square$

The Fourier series (11) is very special, in the sense that all the $c_{n}$ 's with $n<0$ are zero. Such a Fourier series is called analytic, because, as we saw
in Example 3, it is the restriction of an analytic function to the circle. Note that the functions $f(\theta)$ in Example 3 is complex-valued. Is it possible to have a real-valued analytic Fourier series? It is not hard to show that the only real-valued analytic functions are the constant functions (Exercise 10(b)).

## Convolution of Periodic Functions

One of the most important operations in Fourier analysis is the convolution. To define it, consider a pair of $2 p$-periodic functions $f$ and $g$. The convolution of $f$ and $g$, denoted by $f * g(x)$, is defined by

$$
f * g(x)=\frac{1}{2 p} \int_{-p}^{p} f(t) g(x-t) d t
$$

From its mere definition, it is difficult to explain what the convolution does to a pair of functions. In a moment, we will be able to clearly explain its effect in terms of the complex Fourier coefficients. For now, let us observe that if $f$ and $g$ are piecewise continuous and $2 p$-periodic, then, for fixed $x$, the function $f(t) g(x-t)$ is also piecewise continuous and $2 p$-periodic. Its integral can be evaluated over any interval of length $2 p$, without affecting its value (Theorem 1, Section 7.1). So

$$
f * g(x)=\frac{1}{2 p} \int_{-p}^{p} f(t) g(x-t) d t=\frac{1}{2 p} \int_{a}^{a+2 p} f(t) g(x-t) d t
$$

where $a$ is an arbitrary real number. Also, if $f$ and $g$ are continuous with continuous derivatives, we can differentiate under the integral sign (Theorem 5, Section 3.5) and conclude that

$$
\begin{aligned}
\frac{d}{d x} f * g(x) & =\frac{1}{2 p} \int_{-p}^{p} \frac{d}{d x}(f(t) g(x-t)) d t \\
& =\frac{1}{2 p} \int_{-p}^{p} f(t) g^{\prime}(x-t) d t=f * g^{\prime}(x)
\end{aligned}
$$

Similarly, we have $\frac{d}{d x} f * g(x)=f^{\prime} * g(x)$, and so

$$
\frac{d}{d x} f * g(x)=f * g^{\prime}(x)=f^{\prime} * g(x)
$$

If $f$ and $g$ are merely piecewise smooth, we can write the convolution integral as a sum of integrals over intervals on which $f$ and $g$ are continuous with continuous derivatives, and then differentiate under the integral sign. So, in general, the convolution is piecewise smooth.

Convolutions are important because they correspond to multiplication of the Fourier coefficients. To express this property, it will be convenient to use the notation $\widehat{f}(n)$ for the complex Fourier coefficients instead of $c_{n}$.

THEOREM 2 FOURIER COEFFICIENTS OF CONVOLUTIONS

COROLLARY 1 CONTINUITY OF CONVOLUTIONS

Let $f$ and $g$ be $2 p$-periodic, piecewise smooth functions. Then

$$
\widehat{f * g}(n)=\widehat{f}(n) \widehat{g}(n) \quad n=0, \pm 1, \pm 2, \ldots .
$$

Proof We have

$$
\begin{aligned}
\widehat{f * g}(n) & =\frac{1}{2 p} \int_{-p}^{p} f * g(x) e^{-i \frac{n \pi}{p} x} d x \\
& =\frac{1}{2 p} \int_{-p}^{p} \frac{1}{2 p} \int_{-p}^{p} f(t) g(x-t) d t e^{-i \frac{n \pi}{p} x} d x \\
& =\frac{1}{2 p} \int_{-p}^{p} \frac{1}{2 p} \int_{-p}^{p} g(x-t) e^{-i \frac{n \pi}{p} x} d x f(t) d t
\end{aligned}
$$

Making the change of variables $y=x-t$ in the inner integral and using the fact that the integral does not change over an interval of length $2 p$ (Theorem 1, Section 7.1), we obtain

$$
\begin{aligned}
\widehat{f * g}(n) & =\frac{1}{2 p} \int_{-p}^{p} \frac{1}{2 p} \int_{-p}^{p} g(y) e^{-i \frac{n \pi}{p} y} e^{-i \frac{n \pi}{p} t} d y f(t) d t \\
& =\frac{1}{2 p} \int_{-p}^{p} g(y) e^{-i \frac{n \pi}{p} y} d y \frac{1}{2 p} \int_{-p}^{p} f(t) e^{-i \frac{n \pi}{p} t} d t \\
& =\widehat{g}(n) \widehat{f}(n)=\widehat{f}(n) \widehat{g}(n)
\end{aligned}
$$

We will derive several interesting consequences of Theorem 2.
Let $f$ and $g$ be $2 p$-periodic, piecewise smooth functions. Then $f * g$ is continuous and piecewise smooth.

Proof We have already showed that $f * g$ is piecewise smooth with derivative given by (14) at all but finitely many points in $[-p, p]$. To show that it is continuous, we note that if $|f|$ and $\left|f^{\prime}\right|$ are bounded, say by $M$, then $|\widehat{f}(n)| \leq \frac{4 M}{n}$, which follows by integrating by parts in (4). The details are left as an exercise. So $|\widehat{f * g}(n)|=|\widehat{f}(n)||\widehat{g}(n)| \leq A \frac{1}{n} \frac{1}{n}=\frac{A}{n^{2}}$, where $A$ is a constant. We now apply the Weierstrass $M$-test to the Fourier series of $f * g(x)$, which is $\sum_{-\infty}^{\infty} \widehat{f}(n) \widehat{g}(n) e^{i \frac{n \pi}{p}}$, and conclude that the series converges uniformly for all $x$, implying that $f * g(x)$ is continuous, by Theorem 1.

The next result states that convolution is commutative. It can be checked directly by using the definition of convolution. We give a different proof based on Theorem 2.

COROLLARY 2

Let $f$ and $g$ be piecewise smooth $2 p$-periodic functions. Then $f * g(x)= g * f(x)$.

Proof The functions $f * g$ and $g * f$ are piecewise smooth and continuous. Moreover,
they have the same Fourier coefficients, because

$$
\widehat{f * g}(n)=\hat{f}(n) \hat{g}(n)=\hat{g}(n) \hat{f}(n)=\widehat{g * f}(n) .
$$

Since the Fourier series are the same and converge (uniformly) everywhere to the functions, we conclude that $f * g=g * f$.

## COROLLARY 3 PARSEVAL'S IDENTITY

![](./images/3daa498e-ff33-460f-afa4-7af2cd933f9d-42_430_535_1821_94.jpg)
Figure 6 Sawtooth function in Example 4 has the Fourier series $\sum_{n=1}^{\infty} \frac{\sin n x}{n}$.

Let $f$ be a real-valued $2 p$-periodic piecewise smooth function on $[-p, p]$. Let $a_{n}, b_{n}$, and $c_{n}$ denote, respectively, the cosine, the sine, and the complex Fourier coefficients of $f$. Then

$$
\frac{1}{2 p} \int_{-p}^{p} f(x)^{2} d x=\sum_{n=-\infty}^{\infty}\left|c_{n}\right|^{2}=a_{0}^{2}+\sum_{n=1}^{\infty}\left(a_{n}^{2}+b_{n}^{2}\right)
$$

Proof Let $g(t)=f(-t)$. Then

$$
\begin{aligned}
\widehat{g}(n) & =\frac{1}{2 p} \int_{-p}^{p} f(-t) e^{-i \frac{n \pi}{p} t} d t=\frac{1}{2 p} \int_{-p}^{p} f(t) e^{i \frac{n \pi}{p} t} d t \\
& =\frac{1}{2 p} \int_{-p}^{p} f(t) e^{-i \frac{(-n) \pi}{p} t} d t=c_{-n}=\overline{c_{n}}
\end{aligned}
$$

where the last equality follows from (9). From the Fourier series representation, we have

$$
\begin{aligned}
f * g(x) & =\sum_{n=-\infty}^{\infty} \hat{f}(n) \hat{g}(n) e^{i \frac{n \pi}{p} x} \\
& =\sum_{n=-\infty}^{\infty} c_{n} c_{-n} e^{i \frac{n \pi}{p} x}=\sum_{n=-\infty}^{\infty}\left|c_{n}\right|^{2} e^{i \frac{n \pi}{p} x}
\end{aligned}
$$

Evaluating both sides at $x=0$, we obtain the first of the Parseval's identities, since $f * g(0)=\frac{1}{2 p} \int_{-p}^{p} f(t) g(-t) d t=\frac{1}{2 p} \int_{-p}^{p} f(t) f(t) d t=\frac{1}{2 p} \int_{-p}^{p} f^{2}(t) d t$. The second identity follows from the first one by using the relationships between the Fourier coefficients (5)-(7). The details are left as an exercise.

In the following example of a convolution, we will avoid computing directly from the definition. Instead we will compute the Fourier coefficients of the convolution and then identify the convolution function from its Fourier coefficients.

## EXAMPLE 4 Computing convolutions

Find $f * f(x)$, where $f(x)$ denotes the $2 \pi$-periodic sawtooth function, defined on $(0,2 \pi)$ by $f(x)=\frac{1}{2}(\pi-x)$ (Figure 6).
Solution Let us first compute $c_{n}=\widehat{f}(n)$. We can use the definition of the Fourier coefficients or, better yet, since we know the Fourier cosine and sine coefficients, $a_{n}=0$ and $b_{n}=\frac{1}{n}$, we can compute $c_{n}$ by using (6). We have $c_{n}=\frac{1}{2}\left(a_{n}-i b_{n}\right)=$

![](./images/3daa498e-ff33-460f-afa4-7af2cd933f9d-43_389_446_565_53.jpg)
Figure 7 The convolution of the sawtooth function with itself is a continuous function, given on $[0,2 \pi]$ by

$$
\frac{1}{8}\left(\frac{\pi^{2}}{3}-(x-\pi)^{2}\right)
$$

$-\frac{i}{2 n}$. From this and Theorem 2, we conclude that $\widehat{f * f}(n)=\left(-\frac{i}{2 n}\right)^{2}=-\frac{1}{4 n^{2}}$. Computing the cosine and sine Fourier coefficients of $f * f$ from (7), we find that the Fourier sine coefficients are 0 , while the Fourier cosine coefficients are $-\frac{1}{2 n^{2}}$. We now ask: Which function has these Fourier coefficients? Consider the function from Exercise 9, Section 7.2. Call this function $h$. Replace $x$ by $x-\pi$ in the Fourier series and get

$$
h(x-\pi)=\frac{\pi^{2}}{3}+4 \sum_{n=1}^{\infty} \frac{(-1)^{n}}{n^{2}} \cos n(x-\pi)=\frac{\pi^{2}}{3}+4 \sum_{n=1}^{\infty} \frac{1}{n^{2}} \cos n x
$$

where we have used $\cos n(x-\pi)=(-1)^{n} \cos n x$. Subtract $\frac{\pi^{2}}{3}$ and divide by -8 to get

$$
-\frac{1}{8}\left(h(x-\pi)-\frac{\pi^{2}}{3}\right)=-\frac{1}{2} \sum_{n=1}^{\infty} \frac{1}{n^{2}} \cos n x
$$

which is the desired function. Since this function has the same Fourier coefficients as $f * f(x)$, it is thus equal to $f * f(x)$. Using the formula for $h$, we find that on the interval $(0,2 \pi)$

$$
f * f(x)=-\frac{1}{8}\left((x-\pi)^{2}-\frac{\pi^{2}}{3}\right)=\frac{1}{8}\left(\frac{\pi^{2}}{3}-(x-\pi)^{2}\right)
$$

The graph of $f * f$ is shown in Figure 7. It is continuous and piecewise smooth, even though $f$ is not continuous for all $x$.

The final result of this section is an interesting application of Parseval's identity, which implies that the Fourier series of a continuous piecewise smooth function is uniformly and absolutely convergent. We stated this result in Theorem 2, Section 7.2, and proved it under the further assumption that $f^{\prime}$ is piecewise smooth.

## THEOREM 3

Suppose that $f$ is continuous with piecewise continuous derivative $f^{\prime}$. Then the Fourier series of $f$ converges uniformly and absolutely for all $x$.
Proof Denote the Fourier coefficients of $f$ by $a_{n}$ and $b_{n}$ and those of $f^{\prime}$ by $a_{n}^{\prime}$ and $b_{n}^{\prime}$. It is enough to show that $\sum_{n=1}^{\infty}\left(\left|a_{n}\right|+\left|b_{n}\right|\right)<\infty$. We will prove that $\sum_{n=1}^{\infty}\left|a_{n}\right|<\infty$, since the sum with the $b_{n}$ is handled similarly. From the proof of Theorem 2, Section 7.2, we have

$$
a_{n}=-\frac{1}{n} b_{n}^{\prime} \quad \text { and } \quad b_{n}=\frac{1}{n} a_{n}^{\prime}
$$

So by the Cauchy-Schwarz inequality (Exercise 41, Section 1.2), we have

$$
\sum_{n=1}^{N}\left|a_{n}\right|=\sum_{n=1}^{N}\left|b_{n}^{\prime}\right| \frac{1}{n} \leq\left(\sum_{n=1}^{N}\left|b_{n}^{\prime}\right|^{2}\right)^{\frac{1}{2}}\left(\sum_{n=1}^{N} \frac{1}{n^{2}}\right)^{\frac{1}{2}} .
$$

Letting $N \rightarrow \infty$ and using the fact that $\sum_{n=1}^{\infty}\left|b_{n}^{\prime}\right|^{2}<\infty$, by Parseval's identity applied to $f^{\prime}$, it follows that

$$
\sum_{n=1}^{\infty}\left|a_{n}\right| \leq\left(\sum_{n=1}^{\infty}\left|b_{n}^{\prime}\right|^{2}\right)^{\frac{1}{2}}\left(\sum_{n=1}^{\infty} \frac{1}{n^{2}}\right)^{\frac{1}{2}}<\infty
$$

## Exercises 7.5

In Exercises 1-6, find the complex form of the Fourier series of the given $2 \pi$-periodic function.

1. $f(x)=\cosh a x$ if $-\pi<x<\pi(a \neq 0, \pm i, \pm 2 i, \pm 3 i, \ldots)$.
[Hint: Example 1.]
2. $f(x)=\sinh a x$ if $-\pi<x<\pi(a \neq 0, \pm i, \pm 2 i, \pm 3 i, \ldots)$.
[Hint: Example 1.]
3. $f(x)=\cos a x$ if $-\pi<x<\pi$ ( $a$ is not an integer). [Hint:
(1) and Example 1.]
4. $f(x)=\sin a x$ if $-\pi<x<\pi$ ( $a$ is not an integer). [Hint:
(1) and Example 1.]
5. $f(x)=\cos 2 x+2 \cos 3 x$. [Hint: Use (1).]
6. $f(x)=\sin 3 x$.
[Hint: Use (1).]
In Exercises 7-8, find the Fourier series of the given function by using (5) and (7) or by manipulating the complex form of the Fourier series.
7. $f(x)$ is as in Exercise 3.
8. $f(x)$ is as in Exercise 4.
9. (a) Use the orthogonality relations of the complex exponential system (Exercise 12 , Section 3.2 ) to show that the $2 \pi$-periodic function $e^{i n x}$ is its own Fourier series.
(b) Let $m \leq n$ be arbitrary integers and $c_{k}$ be arbitrary complex numbers. What is the Fourier series of the $2 \pi$-periodic function $f(x)=\sum_{k=m}^{n} c_{k} e^{i k x}$ ?
10. (a) Derive (7) from (6).
(b) Show that if $f$ is real-valued, $2 p$-periodic, and piecewise smooth, and all the Fourier coefficients $c_{n}$ with $n<0$ are zero, then $f$ is constant. [Hint: Use (9).]
11. For any real number $a \neq 0$, obtain the expansion

$$
\frac{\pi}{a \sinh \pi a}=\sum_{n=-\infty}^{\infty} \frac{(-1)^{n}}{a^{2}+n^{2}}
$$

[Hint: Take $x=0$ in Example 1.]
12. For any real number $a \neq 0$ and all $-\pi<x<\pi$, obtain the expansion

$$
e^{a x}=\frac{\sinh \pi a}{\pi} \sum_{n=-\infty}^{\infty} \frac{(-1)^{n}}{a^{2}+n^{2}}(a \cos n x-n \sin n x)
$$

[Hint: Equate real parts in the Fourier series of Example 1.]
13. (a) Let $a \neq 0$ be a real number. Use Parseval's identity and Exercise 1 to derive the identity

$$
\sum_{n=-\infty}^{\infty} \frac{1}{\left(a^{2}+n^{2}\right)^{2}}=\frac{\pi}{2 a^{2} \sinh ^{2}(\pi a)}\left[\pi+\frac{\sinh (2 \pi a)}{2 a}\right]
$$

(b) With the help of Exercise 2, derive the identity

$$
\sum_{n=-\infty}^{\infty} \frac{n^{2}}{\left(a^{2}+n^{2}\right)^{2}}=\frac{\pi}{2 \sinh ^{2}(\pi a)}\left[\frac{\sinh (2 \pi a)}{2 a}-\pi\right]
$$

14. (a) Use Parseval's identity and the Fourier series expansion $\frac{x}{2}=\sum_{n=1}^{\infty} \frac{(-1)^{n+1}}{n} \sin n x$ for $-\pi<x<\pi$, to obtain $\sum_{n=1}^{\infty} \frac{1}{n^{2}}=\frac{\pi^{2}}{6}$.
(b) From (a), obtain that $\sum_{k=1}^{\infty} \frac{1}{(2 k)^{2}}=\frac{\pi^{2}}{24}$.
(c) Combine (a) and (b) to derive the identity $\sum_{k=0}^{\infty} \frac{1}{(2 k+1)^{2}}=\frac{\pi^{2}}{8}$.

In Exercises 15-16, find the Fourier series of the given function using Taylor or Laurent series expansions.
15. $f(\theta)=\frac{e^{i \theta}}{2+e^{2 i \theta}}$.
16. $f(\theta)=\frac{1}{3+e^{1 \theta}+e^{-1 \theta}}$.
17. $f(\theta)=e^{e^{i \theta}}$.
18. $f(\theta)=\cos \left(e^{i \theta}\right)$.
19. Which real Fourier series do you get by taking real and imaginary parts in the Fourier series of Exercise 15?
20. (a) Which real Fourier series do you get by taking real and imaginary parts in the Fourier series of Exercise 17?
(b) Answer (a) with the Fourier series of Exercise 18.

In Exercises $21-24$, you are given two $2 \pi$-periodic functions $f$ and $g$ on an interval of length $2 \pi$. (a) Compute the Fourier coefficients of $f * g$. (b) Find $f * g$ by matching its Fourier coefficients with those of a known function (as we did in Example 4).
21. For $-\pi<x<\pi, f(x)=g(x)=x$.
22. For $-\pi<x<\pi, f(x)=x$; and $g(x)=-1$ if $-\pi<x<0$ and $g(x)=1$ if $0<x<\pi$.
23. For $-\pi<x<\pi, f(x)=e^{i x}+e^{-i x}$, and $g(x)$ is an arbitrary piecewise smooth function.
24. For $-\pi<x<\pi, f(x)=\sum_{n=-N}^{N} e^{-i n x}$, and $g(x)$ is an arbitrary piecewise smooth function.
Project Problem: Cotangent expansion, Bernoulli numbers, and Fourier series. In Exercises 25-27, we explore a connection between Fourier series and some important complex series expansions, and derive interesting identities.
25. Consider the $2 \pi$-periodic function of Example 2, which is defined on the interval $(-\pi, \pi)$ by $f(x)=e^{a x}$, where $a \neq 0$ is an arbitrary real number.
(a) Evaluate the Fourier series in Example 2 at $x=\pi$ and obtain for $a \neq 0$

$$
\cosh a \pi=\frac{\sinh a \pi}{a \pi}+\frac{\sinh a \pi}{\pi} \sum_{n=1}^{\infty} \frac{2 a}{a^{2}+n^{2}} .
$$

[Hint: See Example 1.]
(b) Conclude that for any real number $a \neq 0$,

$$
a \pi \operatorname{coth} a \pi=1+\sum_{n=1}^{\infty} \frac{2 a^{2}}{a^{2}+n^{2}} .
$$

26. Euler's expansion of the cotangent. Let $\Omega$ consists of the entire complex plane minus the points $z \neq \pm i, \pm 2 i, \ldots$. For $z$ in $\Omega$, consider

$$
\phi(z)=1+\sum_{n=1}^{\infty} \frac{2 z^{2}}{z^{2}+n^{2}} .
$$

(a) Complete the details of the following argument showing that $\phi$ is analytic in $\Omega$. It is enough to show that the series converges uniformly on every closed and bounded subset of $\Omega$ (Corollary 2, Section 4.2). Let $A \subset \Omega$ be closed and bounded. Let $M>0$ be an integer such that $|z|<M$ for all $z$ in $A$. Then for all $n>M+1$ and all $z$ in $A$, we have $\left|\frac{2 z 2}{z^{2}+n^{2}}\right| \leq \frac{2 M^{2}}{n^{2}-M^{2}}$. So the series converges uniformly on $A$ by the Weierstrass $M$-test, since $\sum_{n=M+1}^{\infty} \frac{2 M^{2}}{n^{2}-M^{2}}<\infty$.
(b) Show that the function $\psi(z)=\pi z \operatorname{coth}(\pi z)$ is analytic for all $z \neq \pm i, \pm 2 i$,
(c) By Exercise 25(b), $\phi(z)=\psi(z)$ for all real $z \neq 0$. Using the identity principle (Section 4.6), conclude that $\phi(z)=\psi(z)$ for all $z$ in $\Omega$. Hence

$$
\pi z \operatorname{coth}(\pi z)=1+\sum_{n=1}^{\infty} \frac{2 z^{2}}{z^{2}+n^{2}} \quad(z \neq \pm i, \pm 2 i, \ldots) .
$$

(d) Replace $z$ by $i z$ in (c) and obtain Euler's expansion of the cotangent

$$
\pi z \cot (\pi z)=1+\sum_{n=1}^{\infty} \frac{2 z^{2}}{z^{2}-n^{2}} \quad(z \neq \pm, \pm 2, \ldots)
$$

27. Bernoulli numbers. (a) Using Exercise 26(d) and the expansion of the cotangent from Exercise 31, Section 4.4, obtain

$$
\sum_{n=1}^{\infty} \frac{2 z^{2}}{z^{2}-n^{2}}=\sum_{n=1}^{\infty}(-1)^{n} \frac{2^{2 n} B_{2 n} \pi^{2 n}}{(2 n)!} z^{2 n}, \quad|z|<1,
$$

where $B_{2 n}$ are the Bernoulli numbers (see Example 4, Section 4.4).
(b) Use the Weierstrass double series theorem (Exercise 39, Section 4.4) to show that for $|z|<1$,

$$
\sum_{n=1}^{\infty} \frac{2 z^{2}}{z^{2}-n^{2}}=\sum_{n=1}^{\infty}\left(\sum_{k=1}^{\infty} \frac{-2}{k^{2 n}}\right) z^{2 n}
$$

[Hint: For each $n=1,2, \ldots$, expand $\frac{2 z^{2}}{z^{2}-n^{2}}=-2 \sum_{k=1}^{\infty}\left(\frac{z}{n}\right)^{2 k},|z|<1$.]
(c) Equating the coefficients in the power series expansions in (a) and (b), conclude that for $n=1,2, \ldots$,

$$
\sum_{k=1}^{\infty} \frac{1}{k^{2 n}}=(-1)^{n-1} \frac{2^{2 n-1} B_{2 n} \pi^{2 n}}{(2 n)!}
$$

(d) Using the values of the Bernoulli numbers from Table 1, Section 4.4, derive the entries in Table 1, which follows.

| $n$ | 1 | 2 | 3 | 4 | 5 | 6 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $\sum_{k=1}^{\infty} \frac{1}{k^{2 n}}$ | $\frac{\pi^{2}}{6}$ | $\frac{\pi^{4}}{90}$ | $\frac{\pi^{6}}{945}$ | $\frac{\pi^{8}}{9450}$ | $\frac{\pi^{10}}{93555}$ | $\frac{691 \pi^{12}}{638512875}$ |

Table 1. Sums of reciprocals of even powers of integers.

### 7.6 Proof of the

![](./images/3daa498e-ff33-460f-afa4-7af2cd933f9d-47_506_437_592_45.jpg)
Figure 1 The $N$ th Dirichlet kernel, $D_{N}(\theta)$, for $N=$ 1,2,5. We have $D_{N}(0)= 2 \mathrm{~N}+1$.

## LEMMA 1 <br> DIRICHLET KERNEL AND FOURIER SERIES


#### Abstract

In this section, we prove Theorem 1, Section 7.2. The proof that we present is based on three preliminary results that are interesting in their own right. We start with the first one, which is an integral representation of the partial sums of Fourier


series involving the Dirichlet kernel (see Exercise 40, Section 1.5).

Let $N$ be a positive integer, and consider the $N$ th partial sum of the Fourier series of a function $f(x): s_{N}(x)=a_{0}+\sum_{n=1}^{N}\left(a_{n} \cos n x+b_{n} \sin n x\right)$. If we use the Euler formulas to write the Fourier coefficients in terms of $f$, we see that

$$
\begin{aligned}
s_{N}(x)= & \frac{1}{2 \pi} \int_{-\pi}^{\pi} f(t) d t \\
& +\frac{1}{\pi} \sum_{n=1}^{N}\left(\cos n x \int_{-\pi}^{\pi} f(t) \cos n t d t+\sin n x \int_{-\pi}^{\pi} f(t) \sin n t d t\right) \\
= & \frac{1}{2 \pi} \int_{-\pi}^{\pi} f(t) d t+\frac{1}{\pi} \int_{-\pi}^{\pi}\left\{f(t) \sum_{n=1}^{N}(\cos n x \cos n t+\sin n x \sin n t)\right\} d t \\
= & \frac{1}{2 \pi} \int_{-\pi}^{\pi} f(t)\left(1+2 \sum_{n=1}^{N} \cos n(x-t)\right) d t
\end{aligned}
$$

where we have combined the integrals and used $\cos n x \cos n t+\sin n x \sin n t= \cos (n-t) x$. The sum inside the big parentheses is the Dirichlet kernel evaluated at $x-t$. Thus according to Exercise 40(d), Section 1.5, we have

$$
1+2 \sum_{n=1}^{N} \cos n(x-t)=\frac{\sin \left[\left(N+\frac{1}{2}\right)(x-t)\right]}{\sin \frac{x-t}{2}}=D_{N}(x-t),
$$

where we let $D_{N}(\theta)$ denote the $N$ th Dirichlet kernel (Figure 1):

$$
D_{N}(\theta)=1+2 \sum_{n=1}^{N} \cos n \theta=\frac{\sin \left[\left(N+\frac{1}{2}\right) \theta\right]}{\sin \frac{\theta}{2}}
$$

The formula seems to have a problem at $\theta=2 k \pi$, since for those values $\sin \frac{\theta}{2}=0$. However, for $\theta=2 k \pi$, we have $\cos \theta=1$, and so $D_{N}(2 k \pi)=1+2 \sum_{n=1}^{N} 1=1+2 N$, which is also equal to $\lim _{\theta \rightarrow 2 k \pi} \frac{\sin \left[\left(N+\frac{1}{2}\right) \theta\right]}{\sin \frac{\theta}{2}}$, as you can verify by using l'Hospital's rule. So (1) is true for all $\theta$ if we interpret it in the limit at the points $\theta=2 k \pi$. Substituting (1) in the expression for $s_{N}(x)$, we obtain the first half of the following integral representation of the partial sums of Fourier series.
If $f$ is a $2 \pi$-periodic piecewise continuous function, and $N \geq 1$, then

$$
s_{N}(x)=\frac{1}{2 \pi} \int_{-\pi}^{\pi} f(t) D_{N}(x-t) d t=\frac{1}{2 \pi} \int_{-\pi}^{\pi} f(x-t) D_{N}(t) d t
$$

where $D_{N}$ is the $N$ th Dirichlet kernel (1).
Proof The second equality follows from the fact that convolution is a commutative operation. To give a direct proof, start with the first equality and use the change
![](./images/3daa498e-ff33-460f-afa4-7af2cd933f9d-48_333_491_134_122.jpg)
![](./images/3daa498e-ff33-460f-afa4-7af2cd933f9d-48_318_497_495_132.jpg)

Figure 2 The function $h(x)$ is piecewise linear. Its discontinuities are the same as those of $f(x)$. They are built in order to cancel the discontinuities of $f(x)$ by adding $-h(x)$.

LEMMA 2 LINEAR CORRECTION

LEMMA 3 RIEMANN-LEBESGUE LEMMA
of variables $T=x-t, d T=-d t$. Then

$$
\begin{aligned}
s_{N}(x) & =\frac{1}{2 \pi} \int_{-\pi}^{\pi} f(t) D_{N}(x-t) d t=-\frac{1}{2 \pi} \int_{x+\pi}^{x-\pi} f(x-T) D_{N}(T) d T \\
& =\frac{1}{2 \pi} \int_{x-\pi}^{x+\pi} f(x-T) D_{N}(T) d T=\frac{1}{2 \pi} \int_{-\pi}^{\pi} f(x-T) D_{N}(T) d T
\end{aligned}
$$

where the last equality follows because we are integrating a $2 \pi$-periodic function over an interval of length $2 \pi$ (Theorem 1, Section 7.1).

In what follows we will be concerned with piecewise continuous $2 \pi$-periodic functions, which may be considered as functions on $[-\pi, \pi]$. The proofs are greatly simplified if we assume further that the functions are continuous on $[-\pi, \pi]$; because functions that are continuous on closed and bounded intervals are in fact uniformly continuous. To reduce a proof from a piecewise continuous function to a continuous function, we can add a piecewise linear correction term, which can be handled separately. This useful process will be clarified in the proofs; for now let us describe our linear correction term.
Suppose that $f$ is a $2 \pi$-periodic piecewise continuous function. Then there is a piecewise linear function $h(x)$ with finitely many discontinuities in $[-\pi, \pi]$, such that the function $g(x)=f(x)-h(x)$ is $2 \pi$-periodic and continuous for all $x$.
Proof The construction of $h$ is best described by a figure (see Figure 2). It is enough to define $h$ on the interval $[-\pi, \pi]$. Since $f$ is piecewise continuous, it has at most a finite number of discontinuities in $[-\pi, \pi]$, say, $-\pi=x_{0}<x_{1}<\cdots<x_{n}=\pi$. Define $h(x)$ on each subinterval $\left(x_{j}, x_{j+1}\right)$ by $h\left(x_{j}+\right)=f\left(x_{j}+\right)$ and $h\left(x_{j+1}-\right)= f\left(x_{j+1}-\right)$. Then $g(x)=f(x)-h(x)$ is clearly continuous for all $x \neq x_{j}$. For $x=x_{j}$, we have $g\left(x_{j}+\right)=f\left(x_{j}+\right)-h\left(x_{j}+\right)=0$ and $g\left(x_{j}-\right)=f\left(x_{j}-\right)-h\left(x_{j}-\right)=0$. Hence $g$ is also continuous at $x_{j}$ and so $g$ is continuous for all $x$.

Our next result states that the Fourier coefficients of a piecewise continuous function tend to 0 as $n \rightarrow \infty$.
Suppose that $f$ is a $2 \pi$-periodic piecewise continuous function. Then
(2) $\lim _{n \rightarrow \infty} \int_{-\pi}^{\pi} f(x) \cos n x d x=0$ and $\lim _{n \rightarrow \infty} \int_{-\pi}^{\pi} f(x) \sin n x d x=0$.

More generally, if $\alpha$ is any fixed real number, then
(3)

$$
\lim _{n \rightarrow \infty} \int_{-\pi}^{\pi} f(x) \cos [(n+\alpha) x] d x=0 \text { and } \lim _{n \rightarrow \infty} \int_{-\pi}^{\pi} f(x) \sin [(n+\alpha) x] d x=0
$$

Proof We will only establish the first limit in (2); the second one follows similarly. We start by verifying the limit for functions that are piecewise linear. Using
integration by parts, we have

$$
\begin{aligned}
\int_{a}^{b}(c x+d) \cos n x d x & =\left.(c x+d) \frac{\sin n x}{n}\right|_{a} ^{b}-c \int_{a}^{b} \frac{\sin n x}{n} d x \\
& =\frac{(c b+d) \sin n b-(c a+d) \sin n a}{n}+c \frac{\cos n b-\cos n a}{n^{2}} \rightarrow 0
\end{aligned}
$$

as $n \rightarrow \infty$. If $f$ is piecewise linear, the first integral in (2) is a finite sum of integrals of the form $\int_{a}^{b}(c x+d) \cos n x d x$, each of which tends to 0 as $n \rightarrow \infty$, and so the integral itself tends to 0 as $n \rightarrow \infty$. This shows that the first limit in (2) is true if $f$ is piecewise linear. Next we consider the case of a continuous function $f$. From the identity $\cos a=-\cos (a+\pi)$, we get $\cos n x=-\cos \left(n\left(x+\frac{\pi}{n}\right)\right)$. Using the substitution $X=x+\frac{\pi}{n}$, we have

$$
\begin{aligned}
\int_{-\pi}^{\pi} f(x) \cos n x d x & =-\int_{-\pi}^{\pi} f(x) \cos \left(n\left(x+\frac{\pi}{n}\right)\right) d x \\
& =-\int_{-\pi+\frac{\pi}{n}}^{\pi+\frac{\pi}{n}} f\left(x-\frac{\pi}{n}\right) \cos n x d x \\
& =-\int_{-\pi}^{\pi} f\left(x-\frac{\pi}{n}\right) \cos n x d x
\end{aligned}
$$

where the last equality follows from Theorem 1, Section 7.1, since all functions are $2 \pi$-periodic. So

$$
2 \int_{-\pi}^{\pi} f(x) \cos n x d x=\int_{-\pi}^{\pi}\left(f(x)-f\left(x-\frac{\pi}{n}\right)\right) \cos n x d x
$$

and hence by the inequality for integrals,

$$
\left|\int_{-\pi}^{\pi} f(x) \cos n x d x\right| \leq \frac{1}{2}\left|\int_{-\pi}^{\pi}\left(f(x)-f\left(x-\frac{\pi}{n}\right)\right) \cos n x d x\right| \leq \frac{1}{2}(2 \pi) M_{n},
$$

where $M_{n}=\max \left|\left(f(x)-f\left(x-\frac{\pi}{n}\right)\right) \cos n x\right|=\max \left|f(x)-f\left(x-\frac{\pi}{n}\right)\right|$ for $x$ in $[-\pi, \pi]$. Since $f$ is continuous on the closed interval $[-\pi, \pi]$, it is uniformly continuous; hence the difference $\left|f(x)-f\left(x-\frac{\pi}{n}\right)\right|$ tends to 0 uniformly for all $x$ in $[-\pi, \pi]$, as $\frac{\pi}{n} \rightarrow 0$. So as $n \rightarrow \infty, M_{n} \rightarrow 0$, implying that $\left|\int_{-\pi}^{\pi} f(x) \cos n x d x\right| \rightarrow 0$, and thus completing the proof in the case $f$ is continuous. Finally, if $f$ is piecewise continuous, we apply Lemma 2 and write $f(x)=g(x)+h(x)$, where $g$ is continuous and $h$ is piecewise linear. Then $\int_{-\pi}^{\pi} f(x) \cos n x d x=\int_{-\pi}^{\pi} g(x) \cos n x d x+ \int_{-\pi}^{\pi} h(x) \cos n x d x \rightarrow 0$ as $n \rightarrow \infty$, by the previous two cases.

To prove (3), use the addition formula for the sine and cosine and apply (2). For example, using $\cos [(n+\alpha) x]=\cos (n x) \cos (\alpha x)-\sin (n x) \sin (\alpha x)$, we get

$$
\begin{aligned}
& \int_{-\pi}^{\pi} f(x) \cos [(n+\alpha) x] d x \\
& =\int_{-\pi}^{\pi}[f(x) \cos (\alpha x)] \cos n x d x-\int_{-\pi}^{\pi}[f(x) \sin (\alpha x)] \sin n x d x
\end{aligned}
$$

![](./images/3daa498e-ff33-460f-afa4-7af2cd933f9d-50_651_490_1249_130.jpg)
Figure 3 The piecewise linear function $h(x)$ has slope equal to $f^{\prime}\left(x_{0}-\right)$ to the left of $x_{0}$ and $f^{\prime}\left(x_{0}+\right)$ to the right of $x_{0}$. The discontinuity of its derivative and its own discontinuity at $x_{0}$ are built to cancel those of $f$ and $f^{\prime}$ in order to make $f$ and $f^{\prime}$ continuous (and $=0$ ) at $x_{0}$.

Applying (2) to the functions $f(x) \cos (\alpha x)$ and $f(x) \sin (\alpha x)$, it follows that both terms on the right of the displayed equation tend to 0 as $n \rightarrow \infty$. $\square$

We are now ready to prove the Fourier representation theorem (Theorem 1, Section 7.2). By assumption, $f$ and $f^{\prime}$ are piecewise continuous. Thus, $f^{\prime}$ may have at most a finite number of discontinuities in $[-\pi, \pi]$, otherwise it exists and is continuous. We will prove that $s_{N}(x)$ converges to $f(x)$ at all points $x$ where $f^{\prime}(x)$ exists. At the points where $f^{\prime}$ does not exist, we can add a correction term, as we did in the proof of Lemma 3, and reduce to the case of points where $f^{\prime}$ does exist. The details are left to the exercises.

Using the fact that $\int_{-\pi}^{\pi} \cos n t d t=0$ for all $n \geq 1$, and $\frac{1}{2 \pi} \int_{-\pi}^{\pi} d t=1$, it follows from (1) that

$$
\frac{1}{2 \pi} \int_{-\pi}^{\pi} D_{N}(t) d t=1, \quad \text { for all } N \geq 1
$$

Using this and Lemma 1, we have

$$
\begin{aligned}
\left|s_{N}(x)-f(x)\right| & =\left|\frac{1}{2 \pi} \int_{-\pi}^{\pi} f(x-t) D_{N}(t) d t-f(x)\right| \\
& =\left|\frac{1}{2 \pi} \int_{-\pi}^{\pi}(f(x-t)-f(x)) D_{N}(t) d t\right| \\
& =\left|\frac{1}{2 \pi} \int_{-\pi}^{\pi} \frac{f(x-t)-f(x)}{\sin \frac{t}{2}} \sin \left[\left(N+\frac{1}{2}\right) t\right] d t\right|
\end{aligned}
$$

To show that this expression tends to 0 as $N \rightarrow \infty$, we use a clever trick. For fixed $x$, consider the function $g(t)=\frac{f(x-t)-f(x)}{\sin \frac{t}{2}}$, for $t \neq 0$ in $[-\pi, \pi]$, and $g(0)=2 f^{\prime}(x)$. This function is clearly piecewise continuous for all $t \neq 0$, and

$$
\lim _{t \rightarrow 0} g(t)=\lim _{t \rightarrow 0} \frac{f(x-t)-f(x)}{\sin \frac{t}{2}}=\lim _{t \rightarrow 0} \frac{f(x-t)-f(x)}{t} \lim _{t \rightarrow 0} \frac{t}{\sin \frac{t}{2}}=2 f^{\prime}(x)=g(0),
$$

where we have used the fact that $f^{\prime}(x)$ exists and $\lim _{t \rightarrow 0} \frac{t}{\sin \frac{t}{2}}=2$. So the function $g(t)$ is continuous at $t=0$, and hence it is piecewise continuous on the entire interval $[-\pi, \pi]$. Applying (3) from the Riemann-Lebesgue lemma, we see that $\lim _{N \rightarrow \infty} \int_{-\pi}^{\pi} g(t) \sin \left[\left(N+\frac{1}{2}\right) t\right] d t=0$, and it follows from (5) that $\lim _{N \rightarrow \infty} \mid s_{N}(x)- f(x) \mid=0$, completing the proof.

## Exercises 7.6

1. The correction term. Suppose that $f$ and $f^{\prime}$ are piecewise continuous in $[-\pi, \pi]$ and that $f^{\prime}$ does not exist at some point $x_{0}$ in $[-\pi, \pi]$. Assume without loss of generality that $x_{0}$ is in ( $-\pi, \pi$ ); otherwise work on a different interval of length $2 \pi$. Show that there is a piecewise linear function $h(x)$ such that $g(x)=f(x)-h(x)$ is piecewise continuous in $(-\pi, \pi)$ and $g^{\prime}\left(x_{0}\right)$ exists. (Note: The function $g(x)$ may not be continuous on all of $[-\pi, \pi]$, as was the case in Lemma 2.) [Hint: Using the fact that $f$ and $f^{\prime}$ are piecewise continuous, define the values of $h$ around $x_{0}$ by $h\left(x_{0}-\right)=f\left(x_{0}-\right), h\left(x_{0}+\right)=f\left(x_{0}+\right)$, and the slopes of lines by $h^{\prime}\left(x_{0}-\right)=f^{\prime}\left(x_{0}-\right)$, $h^{\prime}\left(x_{0}+\right)=f^{\prime}\left(x_{0}+\right)$. See Figure 3.]
(b) Obtain the equation of $h$ :

$$
h(x)= \begin{cases}f^{\prime}\left(x_{0}-\right)\left(x-x_{0}\right)+f\left(x_{0}-\right) & \text { if }-\pi<x<x_{0}, \\ f^{\prime}\left(x_{0}+\right)\left(x-x_{0}\right)+f\left(x_{0}+\right) & \text { if } x_{0}<x<\pi .\end{cases}
$$

2. Fourier series of the correction term. We have already established that the Fourier series of a piecewise smooth function converges to the function at points where the derivative exists. This shows that the Fourier series of $h(x)$ in Exercise 1 converges to $h(x)$, except at $x=x_{0}$ and $x= \pm \pi$. In this exercise, we will evaluate the Fourier series at $x_{0}$ and show that it converges to $\frac{h\left(x_{0}+\right)+h\left(x_{0}-\right)}{2}=\frac{f\left(x_{0}+\right)+f\left(x_{0}-\right)}{2}$.
(a) Replacing $x$ by $x-x_{0}$, we may assume from here on that $x_{0}=0$. Let $H(x)=h(x)-\frac{h(0+)+h(0-)}{2}$. Note that the Fourier series of $H$ is the same as the Fourier series of $h$ minus the constant $\frac{h(0+)+h(0-)}{2}$. Show that

$$
H(x)= \begin{cases}f^{\prime}(0-) x+\frac{h(0-)-h(0+)}{2} & \text { if }-\pi<x<0 \\ f^{\prime}(0+) x+\frac{h(0+)-h(0-)}{2} & \text { if } 0<x<\pi\end{cases}
$$

(b) Derive the following Fourier coefficients of $H$ :

$$
a_{0}=\frac{\pi}{4}\left(f^{\prime}(0+)-f^{\prime}(0-)\right) ; \quad a_{n}=\frac{\left((-1)^{n}-1\right)\left(f^{\prime}(0+)-f^{\prime}(0-)\right)}{\pi n^{2}}, n \geq 1 .
$$

(We will not need the $b_{n}$ 's in the proofs.) (c) Using residues (or other methods of your choice)-more specifically, the results of Exercises 17 and 18, Section 5.6, show that $\sum_{n=1}^{\infty} \frac{(-1)^{n}-1}{\pi n^{2}}=-\frac{\pi}{4}$.
(d) Evaluate the Fourier series of $H$ at 0 and use (c) to show that it converges to 0 . Conclude that the Fourier series of $h$ converges to $\frac{h(0+)+h(0-)}{2}$ at $x_{0}=0$.
3. Fourier series at points of discontinuity. Let $f$ be as in Exercise 1 and suppose that $f$ is not continuous at $x_{0}$. Add a correction term $h(x)$ as in Exercise 1 so that $g(x)=f(x)-h(x)$ becomes continuous and differentiable at $x_{0}$. By construction, we have $g\left(x_{0}\right)=0$. Let $s_{N}(g, x)$ denote the partial sums of the Fourier series of $g$, and define similarly the partial sums of the Fourier series of $f$ and $h$. By the linearity of Fourier series, we have $s_{N}(g, x)=s_{N}(f, x)-s_{N}(h, x)$. Since $g^{\prime}\left(x_{0}\right)$ exists, we have $s_{N}\left(g, x_{0}\right) \rightarrow g\left(x_{0}\right)=0$ (this is the case of the Fourier series representation theorem that we proved in this section). By Exercise 2, we have $s_{N}\left(h, x_{0}\right) \rightarrow \frac{h\left(x_{0}+\right)+h\left(x_{0}-\right)}{2}=\frac{f\left(x_{0}+\right)+f\left(x_{0}-\right)}{2}$, where the second equality follows from the way we defined $h$. Thus $s_{N}(f, x) \rightarrow \frac{f\left(x_{0}+\right)+f\left(x_{0}-\right)}{2}$, which completes the proof.

