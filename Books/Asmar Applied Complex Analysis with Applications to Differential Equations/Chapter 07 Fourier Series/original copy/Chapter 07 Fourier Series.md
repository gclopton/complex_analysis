<!-- Page 1 -->

Left margin note (page 1)

Topics to Review
The core material in Sect 7.4 is independent from vious chapters and requ a basic knowledge of Methods from complex will be used in applicat to develop tools for co Fourier series. These t usually included at the e tions and can be omitt out affecting the continu course. Complex num the complex exponential are required in Section 7 fine the complex form o series.

Looking Ahead
Fourier series, as pres Sections 7.1-7.4, are for all that follows a not be omitted. The convergence of Fourier Section 7.6 is optional tions 7.2 and 7.5 contal cations based on tools fr plex analysis, such as Ta Laurent series, and inte residues. These applicati you deeper in the compu Fourier series. You are aged to cover at least them, since these method used again in later cha expand the scope of the and derive important pr of special functions.

++++

7
FOURIER SERIES

Mathematics compares the most diverse phenomena and discovers the secret analogies that unite them.
-Joseph Fourier

Like the familiar Taylor series, Fourier series are special types of expansions of functions. With a Taylor series, the expansion is in terms of the special set of functions $1, x, x^{2}, x^{3}, \ldots$. With a Fourier series, we are interested in expanding a function in terms of the special set of functions $1, \cos x, \cos 2 x, \cos 3 x, \ldots, \sin x, \sin 2 x, \sin 3 x, \ldots$. Thus, a Fourier series expansion of a function $f$ is an expression of the form
$$
f(x)=a_{0}+\sum_{n=1}^{\infty}\left(a_{n} \cos n x+b_{n} \sin n x\right)
$$
where $a_{0}, a_{n}$, and $b_{n}$ are the Fourier coefficients. Fourier series arose naturally when solving Dirichlet problems on the disk in Section 4.7. As we will see in the remaining chapters, Fourier series are fundamental tools for the implementation of important methods for solving boundary value problems, such as the separation of variables method and the eigenfunction expansions method. Also the theory of Fourier series will serve as a model for theories involving other special functions such as Bessel functions and Legendre polynomials. The latter are the tools of choice for solving boundary value problems involving Laplace's equation on disks, cylinders and spheres.

In this chapter, we will present basic properties of Fourier series that will be used throughout the rest of the book.

---

<!-- Page 2 -->

Left margin note (page 2)

458
Chapter 7
7.1 Period

![](./images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-02_469_505_312_110.jpg)

Figure 1 The bo tion $f(\theta)$ in a Di lem on a disk cer origin is $2 \pi$-perio

![](./images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-02_334_520_1173_120.jpg)

Figure 2 A $T-$ tion.

![](./images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-02_412_528_1843_120.jpg)

Figure 3 The 2 tion in Example

Right margin note (page 2)

tions rigin. e the Using of the the $f$ is aly in over
re 2). e the sitive $\sin 2 x$ is $\pi$.

In are the ained As a t over many
$\_\_\_\_$
ht line

++++

Fourier Series

ic Functions
One of the problems that we have discussed at length in previous sec was the Dirichlet problem on a disk of radius $R>0$, centered at the o
$, \theta)=f(\theta)$
undary funcrichlet probtered at the dic.
periodic func-
periodic func1.
In such a problem, we are supposed to solve Laplace's equation insid disk, given the values of the function on the boundary of the disk. polar coordinates, the boundary data was given by a function $f(\boldsymbol{\theta})$ polar angle $\theta$. Because $\theta$ and $\theta+2 \pi$ correspond to the same point unit circle, we have $f(\theta)=f(\theta+2 \pi)$. In other words, the function $2 \pi$-periodic (Figure 1). Periodic functions will arise naturally not on boundary value problems on a disk but also in wave and heat problems a finite interval. A function $f$ satisfying the identity
$$
f(x)=f(x+T) \text { for all } x,
$$
where $T>0$, is called periodic or, more specifically, $T$-periodic (Figu The number $T$ is called a period of $f$. If $f$ is nonconstant, we defin fundamental period, or simply, the period of $f$ to be the smallest po number $T$ for which (1) holds. For example, the functions $3 \sin x$, s are all $2 \pi$-periodic. The period of $\sin x$ is $2 \pi$, while the period of $\sin 2 x$

Using (1) repeatedly, we get
$$
f(x)=f(x+T)=f(x+2 T)=\cdots=f(x+n T) .
$$

Hence if $T$ is a period, then $n T$ is also a period for any integer $n>$ the case of the sine function, this amounts to saying that $2 \pi, 4 \pi, 6 \pi,$. all periods of $\sin x$, but only $2 \pi$ is the fundamental period. Becaus values of a $T$-periodic function repeat every $T$ units, its graph is obt by repeating the portion over any interval of length $T$ (Figure 2). consequence, to define a $T$-periodic function, it is enough to describe i an interval of length $T$. Obviously, the interval can be chosen in different ways. The following example illustrates these ideas.

EXAMPLE 1 Describing a periodic function
Describe the 2-periodic function $f$ in Figure 3 in two different ways:
(a) by considering its values on the interval $0 \leq x<2$;
(b) by considering its values on the interval $-1 \leq x<1$.

Solution (a) On the interval $0 \leq x<2$ the graph is a portion of the straig $y=-x+1$. Thus
$$
f(x)=-x+1 \text { if } 0 \leq x<2 .
$$

Now the relation $f(x+2)=f(x)$ describes $f$ for all other values of $x$.

---

<!-- Page 3 -->

Left margin note (page 3)

![](./images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-03_430_455_197_63.jpg)

Figure 4 Areas over on riod are equal.

THEORE
INTEGRAL OV
ONE PER]

++++

Section 7.1 Periodic Functions
459
(b) On the interval $-1 \leq x<1$, the graph consists of two straight lines (Figure 3). We have
$$
f(x)=\left\{\begin{array}{ll}
-x-1 & \text { if }-1 \leq x<0 \\
-x+1 & \text { if } 0 \leq x<1
\end{array}\right.
$$

As in part (a), the relation $f(x+2)=f(x)$ describes $f$ for all values of $x$ outside the interval $[-1,1)$.

Although the formulas in Example 1(a) and (b) are different, they describe the same periodic function. In practice, we use common sense in choosing the most convenient formula. Before we illustrate with an example, we introduce a very useful theorem whose content is intuitively clear. It says that the definite integral of a $T$-periodic function is the same over any interval of length $T$ (Figure 4).

M 1
TER
[OD

Suppose that $f$ is $T$-periodic. Then, for any real number $a$, we have
$$
\int_{0}^{T} f(x) d x=\int_{a}^{a+T} f(x) d x
$$

Proof Define
$$
F(a)=\int_{a}^{a+T} f(x) d x
$$

By the fundamental theorem of calculus, we have $F^{\prime}(a)=f(a+T)-f(a)=0$, because $f$ is periodic with period $T$. Hence $F(a)$ is constant for all $a$, and so $F(0)=F(a)$, which implies the theorem.

EXAMPLE 2 Integrating periodic functions
Let $f$ be the 2-periodic function in Example 1. Use Theorem 1 to compute
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

---

<!-- Page 4 -->

Left margin note (page 4)

460
Chapter 7 Fourier Series

Right margin note (page 4)

odic)

1 the Sec-
s):
ise 12, ve the

++++

The most important periodic functions are those in the ( $2 \pi$-peri trigonometric system
$$
\begin{array}{c}
1, \cos x, \cos 2 x, \cos 3 x, \ldots, \cos m x, \ldots, \\
\sin x, \sin 2 x, \sin 3 x, \ldots, \sin n x, \ldots
\end{array}
$$

They are $2 \pi$-periodic, and orthogonal on the interval $[0,2 \pi]$. Recal orthogonality properties of the trigonometric system from Exercise 12 tion 3.2 (in what follows, the indices $m$ and $n$ are nonnegative integer
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

To prove these, we can use the complex integral, as suggested in Exerc Section 3.2, or just use trigonometric identities. For example, to pro first one, use
$$
\cos m x \cos n x=\frac{1}{2}(\cos (m+n) x+\cos (m-n) x) .
$$

Since $m \pm n \neq 0$, we get
$$
\begin{aligned}
\int_{-\pi}^{\pi} & \cos m x \cos n x d x \\
\quad= & \frac{1}{2}\left[\frac{1}{m+n} \sin (m+n) x+\frac{1}{m-n} \sin (m-n) x\right]_{-\pi}^{\pi}=0 .
\end{aligned}
$$

Exercises 7.1
In Exercises 1-2, find a period of the given function and sketch its graph.
1. (a) $\cos x$,
(b) $\cos \pi x$,
(c) $\cos \frac{2}{3} x$,
(d) $\cos x+\cos 2 x$.
2. (a) $\sin 7 \pi x$,
(b) $\sin n \pi x$,
(c) $\cos m x$,
(d) $\sin x+\cos x$,
(e) $\sin ^{2} 2 x$.

---

<!-- Page 5 -->

Left margin note (page 5)

$\_\_\_\_$

Right margin note (page 5)

461
ying

odic how it is $x+$ The rest dic t 0) ax) lic),

os $x$
$h \pi$.

++++

Section 7.1 Periodic Functions

In Exercises 3-6, find a formula that describes the function in the accompan figure (Figures 5-8).
3.

![](./images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-39_606_468_1781_55.jpg)
Figure 5
5.

![](./images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-43_389_446_565_53.jpg)
Figure 7
4.

![](./images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-42_430_535_1821_94.jpg)
Figure 6
6.

![](./images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-26_371_533_1149_126.jpg)
Figure 8
7. Sums of periodic functions. Show that if $f_{1}, f_{2}, \ldots, f_{n}, \ldots$ are $T$-peri functions, then $a_{1} f_{1}+a_{2} f_{2}+\cdots+a_{n} f_{n}$ is also $T$-periodic. More generally, s that if the series $\sum_{n=1}^{\infty} a_{n} f_{n}(x)$ converges for all $x$ in $0<x \leq T$, then its lim a $T$-periodic function.
8. Sums of periodic functions need not be periodic. Let $f(x)=\cos \cos \pi x$. (a) Show that the equation $f(x)=2$ has a unique solution.
(b) Conclude from (a) that $f$ is not periodic. Does this contradict Exercise 7? function $f$ is called almost periodic. These functions are of considerable inte and have many useful applications.
9. Operations on periodic functions. (a) Let $f$ and $g$ be two $T$-peri functions. Show that the product $f(x) g(x)$ and the quotient $f(x) / g(x)(g(x)=$ are also $T$-periodic.
(b) Show that if $f$ has period $T$ and $a>0$, then $f\left(\frac{x}{a}\right)$ has period $a T$ and $f($ has period $\frac{T}{a}$.
(c) Show that if $f$ has period $T$ and $g$ is any function (not necessarily perioc then the composition $g \circ f$ has period $T$.
10. With the help of Exercise 9, determine the period of the given function.
(a) $\sin 2 x$
(b) $\cos \frac{1}{2} x+3 \sin 2 x$
(c) $\frac{1}{2+\sin x}$
(d) $e^{\mathrm{c}}$

In Exercises 11-14, a $\pi$-periodic function is described over an interval of lengt In each case plot the graph over three periods and compute the integral
$$
\int_{-\pi / 2}^{\pi / 2} f(x) d x
$$

---

<!-- Page 6 -->

Left margin note (page 6)

462
Chapter 7
Fo
7.2 Fourier

EULER FOF
FOR THE F COEFF

Right margin note (page 6)

and as r an chlet eriod its of series

++++

urier Series
11. $f(x)=\sin x, \quad 0 \leq x<\pi$.
12. $f(x)=\cos x, \quad 0 \leq x<\pi$.
13.
14. $f(x)=x^{2}, \quad-\frac{\pi}{2} \leq x<\frac{\pi}{2}$.
$$
f(x)=\left\{\begin{array}{ll}
1 & \text { if } 0 \leq x \leq \frac{\pi}{2} \\
0 & \text { if }-\frac{\pi}{2}<x<0
\end{array}\right.
$$
15. Antiderivatives of periodic functions. Suppose that $f$ is $2 \pi$-periodic let $a$ be a fixed real number. Define
$$
F(x)=\int_{a}^{x} f(t) d t, \text { for all } x
$$

Show that $F$ is $2 \pi$-periodic if and only if $\int_{0}^{2 \pi} f(t) d t=0$. [Hint: Theorem 1.]
16. Suppose that $f$ is $T$-periodic and let $F$ be an antiderivative of $f$, define in Exercise 15. Show that $F$ is $T$-periodic if and only if the integral of $f$ ove interval of length $T$ is 0 .
17. (a) Let $f$ be as in Example 1. Describe the function
$$
F(x)=\int_{0}^{x} f(t) d t
$$
[Hint: By Exercise 16, it is enough to consider $x$ in [0,2].]
(b) Plot $F$ over the interval $[-4,4]$.

Series
Fourier series arose naturally in Section 4.7 from our solution of the Diri problem in a disk centered at 0 . They are special expansions of $2 \pi$-p functions of the form
$$
f(x)=a_{0}+\sum_{n=1}^{\infty}\left(a_{n} \cos n x+b_{n} \sin n x\right)
$$
where the coefficients $a_{0}, a_{n}$, and $b_{n}$ are called the Fourier coefficien $f$ and are given by the following Euler formulas.

ZMULAS

The Fourier coefficients of of a function $f$ are given by

OURIER
ICIENTS
$$
\begin{array}{l}
a_{0}=\frac{1}{2 \pi} \int_{-\pi}^{\pi} f(x) d x \\
a_{n}=\frac{1}{\pi} \int_{-\pi}^{\pi} f(x) \cos n x d x \quad(n=1,2, \ldots) \\
b_{n}=\frac{1}{\pi} \int_{-\pi}^{\pi} f(x) \sin n x d x \quad(n=1,2, \ldots)
\end{array}
$$

For a positive integer $N$, we denote the $N$ th partial sum of the Fourier

---

<!-- Page 7 -->

Left margin note (page 7)

ALTERNA
EULER FORMU

++++

Section 7.2 Fourier Series

of $f$ by $s_{N}(x)$. Thus
$$
s_{N}(x)=a_{0}+\sum_{n=1}^{N}\left(a_{n} \cos n x+b_{n} \sin n x\right)
$$

Because all the integrands in (2)-(4) are $2 \pi$-periodic, we can use Theoren Section 7.1, to rewrite these formulas using integrals over the interval $[0$, (or any other interval of length $2 \pi$ ). Such alternative formulas are sometir useful.

TIVE
JAS
(5)
$$
a_{0}=\frac{1}{2 \pi} \int_{0}^{2 \pi} f(x) d x
$$
(6)
$$
a_{n}=\frac{1}{\pi} \int_{0}^{2 \pi} f(x) \cos n x d x, \text { and } b_{n}=\frac{1}{\pi} \int_{0}^{2 \pi} f(x) \sin n x d x, n \geq
$$

The Fourier coefficients were known to Euler before Fourier and for $t$ reason they bear Euler's name. Euler used them to derive particular Four series such as the one presented in Example 1 below.

Before we consider some examples of Fourier series, it is instructive motivate the Euler formulas by deriving them from the Fourier series, usi the orthogonality of the trigonometric system. For this purpose, we proce as Fourier himself did. We integrate both sides of (1) over the inter $[-\pi, \pi]$, assuming term-by-term integration is justified, and get
$$
\int_{-\pi}^{\pi} f(x) d x=\int_{-\pi}^{\pi} a_{0} d x+\sum_{n=1}^{\infty} \int_{-\pi}^{\pi}\left(a_{n} \cos n x+b_{n} \sin n x\right) d x
$$

But $\int_{-\pi}^{\pi} \cos n x d x=\int_{-\pi}^{\pi} \sin n x d x=0$ for $n=1,2, \ldots$, so
$$
\int_{-\pi}^{\pi} f(x) d x=\int_{-\pi}^{\pi} a_{0} d x=2 \pi a_{0} \quad \Rightarrow \quad a_{0}=\frac{1}{2 \pi} \int_{-\pi}^{\pi} f(x) d x
$$

Similarly, starting with (1), we multiply both sides by $\cos m x(m \geq$ integrate term by term, use the orthogonality of the trigonometric syst

---

<!-- Page 8 -->

Left margin note (page 8)

464
Chapter 7

![](./images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-08_432_535_1113_120.jpg)

Figure 1 Sawt

In evaluating $a$ formula $\int x \cos \frac{1}{n^{2}} \cos n x+\frac{x}{n} s$ obtained by i parts.

Right margin note (page 8)

$x d x$

Fourier
(x), and

++++

Fourier Series

(Section 7.1), and get
$$
\begin{aligned}
\int_{-\pi}^{\pi} f(x) \cos m x d x & =\overbrace{\int_{-\pi}^{\pi} a_{0} \cos m x d x}^{=0}+\sum_{n=1}^{\infty} \overbrace{\int_{-\pi}^{\pi} a_{n} \cos n x \cos m}^{=0 \text { for } m \neq n} \\
& +\sum_{n=1}^{\infty} \overbrace{\int_{-\pi}^{\pi} b_{n} \sin n x \cos m x d x}^{=0} \\
& =a_{m} \overbrace{\int_{-\pi}^{\pi} \cos ^{2} m x d x}^{=\pi}=\pi a_{m} .
\end{aligned}
$$

Solving for $a_{m}$, we obtain (3). By a similar procedure, we derive (4)
Our first example displays many of the peculiar properties of series.

EXAMPLE 1 Fourier series of the sawtooth function
poth function.
$n$, we use the $n x d x= \mathrm{n} n x$, which is ntegrating by

The sawtooth function, shown in Figure 1, is determined by the formulas
$$
f(x)=\left\{\begin{array}{ll}
\frac{1}{2}(\pi-x) & \text { if } 0<x \leq 2 \pi, \\
f(x+2 \pi) & \text { otherwise } .
\end{array}\right.
$$
(a) Find its Fourier series.
(b) With the help of a computer, plot the partial sums $s_{1}(x), s_{7}(x)$, and $s_{20}$ determine the graph of the Fourier series.
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
& =\frac{1}{2 \pi} \frac{2 \pi}{n}=\frac{1}{n}
\end{aligned}
$$

---

<!-- Page 9 -->

Left margin note (page 9)

![](./images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-09_384_459_876_49.jpg)

Figure 2 To distinguis graphs of the $n$th

p sums of the Fourier $s_{n}(x)=\sum_{k=1}^{n} \frac{s i n k x}{k}$, that as $n$ increases, th quencies of the sine tern crease. This causes the g of the higher partial sur be more wiggly. The ing graph is the graph whole Fourier series, sho Figure 3. It is identical t graph of the function, ev at points of discontinuity

![](./images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-09_475_453_1574_37.jpg)

Figure 3 The graph of Fourier series $\sum_{n=1}^{\infty} \frac{\sin n x}{n}$ incides with the graph o function, except at the p of the discontinuity. limits of a function at a p of discontinuity: $f(1+)= f(1-)=1$.

![](./images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-09_486_1345_309_549.jpg)

++++

Section 7.2 Fourier Series
465

h the artial eries, note freas inraphs ns to imitof the vn in o the xcept

the
co-
f the
oints
$\xrightarrow[\text { ght }]{x}$

Substituting these values for $a_{n}$ and $b_{n}$ into (1), we obtain $\sum_{n=1}^{\infty} \frac{\sin n x}{n}$ as the Fourier series of $f$.
(b) Figure 2 shows the first, seventh and twentieth partial sums of the Fourier series. We see clearly that the Fourier series of $f$ converges to $f(x)$ at each point $x$ where $f$ is continuous. In particular, for $0<x<2 \pi$, we have
$$
\sum_{n=1}^{\infty} \frac{\sin n x}{n}=\frac{1}{2}(\pi-x)
$$

At the points of discontinuity ( $x=2 k \pi, k=0, \pm 1, \pm 2, \ldots$ ), the series converges to 0 . The graph of the Fourier series $\sum_{n=1}^{\infty} \frac{\sin n x}{n}$ is shown in Figure 3. It agrees with the graph of the function, except at the points of discontinuity.

Two important facts are worth noting concerning the behavior of Fourier series near points of discontinuity. As we will see shortly, these observations are true in a very general sense.
Note 1: At the points of discontinuity ( $x=2 k \pi$ ) in Example 1, the Fourier series converges to 0 , which is the average value of the function from the left and the right at these points.
Note 2: Near the points of discontinuity, the Fourier series overshoots its limiting values. This is apparent in Figure 2, where humps form on the graphs of the partial sums near the points of discontinuity. This curious phenomenon is known as the Gibbs (or Wilbraham-Gibbs) phenomenon.
(See the paper [15] for an interesting historical account.)
Fourier Series Representation
To state our main result, we recall from Section 3.1 the definitions of piecewise continuous and piecewise smooth functions. We will write
$$
f(c-)=\lim _{x \rightarrow c^{-}} f(x)
$$
to denote the fact that $f$ approaches the number $f(c-)$ as $x$ approaches $c$ from below (Figure 4). Similarly, if the limit of $f$ exists as $x$ approaches $c$

---

<!-- Page 10 -->

Left margin note (page 10)

466
Chapter 7
F

![](./images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-10_484_530_303_85.jpg)

Figure 5 A con periodic function.

![](./images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-10_467_541_1065_93.jpg)

Figure 6 Averag $x=1$.

THE
FOURIEF
REPRESEN

Right margin note (page 10)

n the us on right if it is action e that points $c$ and on of low is nooth action One rage)
motion
iscontate a theo-
or all $x$
rticular,

++++

ourier Series

from above, we denote this limit $f(c+)$ and write
tinuous $2 p$ -
$$
+f(1+)) / 2=3 / 4
$$
$$
1+)=1 / 2
$$

e of $f(x)$ at
OREM 1
SERIES
JTATION
$$
f(c+)=\lim _{x \rightarrow c^{+}} f(x)
$$

A function $f$ is thus continuous at $c$ if and only if
$$
f(c-)=f(c+)=f(c) .
$$

In this notation, a function $f$ is said to be piecewise continuous o interval $[a, b]$ if $f(a+)$ and $f(b-)$ exist, and $f$ is defined and continuo $(a, b)$ except at a finite number of points in $(a, b)$ where the left and limits exist. A periodic function is said to be piecewise continuous piecewise continuous on every interval of the form $[a, b]$. A periodic fur is said to be continuous if it is continuous on the entire real line. Not continuity forces a certain behavior of the periodic function at the endp of any interval of length one period. For example, if $f$ is $2 p$-periodi continuous, then necessarily $f(-p)=f(p)$ (Figure 5). The functi Example 1 is piecewise continuous, while the function in Example 2 be continuous. Let us also recall that a function $f$ is said to be piecewise sn if $f$ and $f^{\prime}$ are piecewise continuous on $[a, b]$. Similarly, a periodic fur is piecewise smooth if it is piecewise smooth on every interval $[a, b]$ more item of terminology is needed. The average (or arithmetic ave of $f$ at $c$ is
$$
\frac{f(c-)+f(c+)}{2} .
$$

Clearly if $f$ is continuous at $c$, then its average at $c$ is $f(c)$. Thus the 1 of average will be of interest only at points of discontinuity.

As an illustration, consider the function in Figure 6. It has a d tinuity at $x=1$ and its average there is $\frac{1+\frac{1}{2}}{2}=\frac{3}{4}$. We can now $s$ fundamental result in the theory of Fourier series. The proof of this rem is presented in Section 7.6.
Suppose that $f$ is a $2 \pi$-periodic piecewise smooth function. Then f we have
$$
\frac{f(x+)+f(x-)}{2}=a_{0}+\sum_{n=1}^{\infty}\left(a_{n} \cos n x+b_{n} \sin n x\right),
$$
where the Fourier coefficients $a_{0}, a_{n}, b_{n}$ are given by (2)-(4). In par if $f$ is piecewise smooth and continuous at $x$, then
$$
f(x)=a_{0}+\sum_{n=1}^{\infty}\left(a_{n} \cos n x+b_{n} \sin n x\right)
$$

---

<!-- Page 11 -->

Left margin note (page 11)

(b) its Fourier series.

![](./images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-11_849_480_849_48.jpg)

Figure 7 At a point of d tinuity of a piecewise sn function, the Fourier converges to the average function at that point.

++++

Section 7.2 Fourier Series

Let us see what (7) is telling us. At a point of continuity of $f$, the Four series converges to $f(x)$. At a point of discontinuity, the Fourier series d its best to converge, and having no reason to favor one side over the oth it converges to the average of the left and right limits (see Figure 7). N that in (7) the value of the Fourier series of $f$ at a given point $x$ does depend on $f(x)$ but on the limit of $f$ from the left and right at $x$. For $t$ reason, we may define (or redefine) $f$ at isolated points without affect its Fourier series. This is illustrated by the behavior of the Fourier series Example 1, where, at the points of discontinuity, we could have assigned a values for the function without affecting the behavior of the Fourier seri If we redefine the function at points of discontinuity to be
$$
\frac{f(x+)+f(x-)}{2},
$$
we then have the equality
$$
f(x)=a_{0}+\sum_{n=1}^{\infty}\left(a_{n} \cos n x+b_{n} \sin n x\right)
$$
holding at all $x$. We will often assume such a modification at the poin of discontinuity and not worry about the more precise, but cumberson equality (7).

It is important to keep in mind that continuity of $f$ alone is not enous to ensure the convergence of its Fourier series. Although we will not e counter such functions, there are continuous functions with Fourier seri that diverge at an infinite number of points in $[0,2 \pi]$.

The problem of convergence for Fourier series was tackled by Fourie Cauchy, and many other prominent mathematicians, who tried but cou not establish the convergence for arbitrary $f$. We owe it to Peter Gusta Lejeune Dirichlet (1805-1859), who took a different approach to this proble by first formulating sufficient conditions on $f$ that ensure the convergen of its Fourier series representation. Dirichlet's theorem about Fourier seri is basically what we have stated in Theorem 1. Determining condition on $f$ that ensure the convergence of its Fourier series is an extremely han problem. The most general results in this direction were obtained in th 1960s by Lennart Carleson (University of Uppsala, Sweden, and Universi of California, Los Angeles) and Richard Hunt (University of Indiana). The spectacular results are far beyond the level of this book. For a moder account of this theory, see the book by Grafakos [14].

Let us note one more property of Fourier series, which is an immedia consequence of Theorem 1.

---

<!-- Page 12 -->

Left margin note (page 12)

468
Chapter 7
F

COROL UNIQUEN FOURIER REPRESEN?

![](./images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-12_431_529_1444_106.jpg)

Figure 8 Triang

Right margin note (page 12)

and
xcept
, if $f$
$y$ are
tion
ries.
ırier
n on
uous es to
d by
odd.
rem 1

++++

ourier Series

LARY 1
ESS OF
SERIES CATION

Suppose that $f$ and $g$ are $2 \pi$-periodic piecewise smooth functions. If $g$ have the same Fourier coefficients, then $f(x)=g(x)$ for all $x$, ee possibly at the points where $f$ or $g$ are discontinuous. Consequently and $g$ are continuous and have the same Fourier coefficients, then the equal everywhere.

Proof Since the Fourier series of a function converges to the value of the fund at the points of continuity, it follows that if $f$ and $g$ have the same Fourier then they must be equal at all the points of continuity.

For all practical purposes in analysis, if $f$ and $g$ have the same For series, then they are considered to be the same function.

EXAMPLE 2 Triangular wave
(a) Find the Fourier series of the $2 \pi$-periodic triangular function, which is give the interval $[-\pi, \pi]$ by
$$
f(x)=\left\{\begin{array}{ll}
\pi+x & \text { if }-\pi \leq x \leq 0, \\
\pi-x & \text { if } 0 \leq x \leq \pi .
\end{array}\right.
$$
(b) Plot some partial sums and the Fourier series.

Solution Figure 8 shows that the function is piecewise smooth and contin for all $x$. So, from the second part of Theorem 1, we expect the Fourier seri converge to $f(x)$ for all $x$. Using (2), we have
$$
a_{0}=\frac{1}{2 \pi} \int_{-\pi}^{\pi} f(x) d x=\frac{1}{2 \pi} \pi^{2}=\frac{1}{2} \pi
$$
(This is the area of the triangular region in Figure 8 with base $[-\pi, \pi]$ divide
$\pi-x$ lar wave. $2 \pi$.) Using (3), we have
$$
\begin{aligned}
a_{n} & =\frac{1}{\pi} \int_{-\pi}^{0}(\pi+x) \cos n x d x+\frac{1}{\pi} \int_{0}^{\pi}(\pi-x) \cos n x d x \\
& =\frac{2}{\pi} \int_{0}^{\pi}(\pi-x) \cos n x d x \quad \text { (change } x \text { to }-x \text { in the first integral } \\
& =\frac{2}{\pi}\left\{\frac{1}{n^{2}}-\frac{\cos n \pi}{n^{2}}\right\} \quad \text { (integration by parts). }
\end{aligned}
$$

Since $\cos n \pi=(-1)^{n}$, we see that $a_{n}=0$ if $n$ is even, and $a_{n}=\frac{4}{\pi n^{2}}$ if $n$ is Finally, using (4), we find
$$
b_{n}=\frac{1}{\pi} \int_{-\pi}^{\pi} \overbrace{f(x) \sin n x}^{\text {odd function }} d x=0
$$
since we are integrating an odd function over a symmetric interval. Now The implies that
$$
f(x)=\frac{1}{2} \pi+\sum_{n \text { odd }} \frac{4}{\pi n^{2}} \cos n x=\frac{1}{2} \pi+\frac{4}{\pi} \sum_{k=0}^{\infty} \frac{1}{(2 k+1)^{2}} \cos (2 k+1) x
$$

---

<!-- Page 13 -->

Left margin note (page 13)

The partial sums of Fourier series, illustrate Figure 9, are converging fast. much faster than the Example 1. This is due $t$ magnitudes of the Fourie efficients. In Example coefficients are of the $1 / n$, while in Example coefficients are of the $1 / n^{2}$.

THEOREN UNIFOF CONVERGENCE FOURIER SERI

![](./images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-13_433_659_361_536.jpg)
![](./images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-13_425_678_365_1259.jpg)

Right margin note (page 13)

క్ర
एक्व.
कै F
$\stackrel{7}{7}$

++++

Section 7.2 Fourier Series

for all $x$. Since the function and its Fourier series are equal at all points, the graphs coincide (compare Figures 8 and 10).
the
d in
very
ose in
o the
r co-
the
order
the
order
the
od in
very
ose in
o the
r co-
the
order
the
order

![](./images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-26_388_548_2061_124.jpg)
Figure 9 Partial sums of the Fourier series.

![](./images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-27_362_454_895_56.jpg)
Figure 10 The Fourier series.

In (9), letting $k$ run from 0 to 1,2 , and 5 , respectively, we generate the third, fift and eleventh partial sums of the Fourier series. These are plotted in Figure 9. No the fast convergence of the Fourier series.

![](./images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-26_388_548_2061_124.jpg)
Figure 9 suggests that the Fourier series in Example 2 converges un formly to the function. This is indeed true and follows from the followi important result.

42

Suppose that $f$ is a $2 \pi$-periodic piecewise smooth function. Then the Four

RM series of $f$ converges uniformly for all $x$ to $f(x)$ if and only if $f$ is continue

OF for all $x$. Thus, if $f$ is continuous and piecewise smooth, then

ES
$$
f(x)=a_{0}+\sum_{n=1}^{\infty}\left(a_{n} \cos n x+b_{n} \sin n x\right),
$$
where the Fourier series converges uniformly for all $x$.

Proof One direction is immediate from Theorem 1, Section 4.2, which asserts th the uniform limit of continuous functions is continuous. Since a partial sum of Fourier series is a finite linear combination of sines and cosines, it is clearly cont uous. So, if $s_{N}(x)$ converges uniformly to $f(x)$ for all $x$, then $f(x)$ is necessar continuous for all $x$. For the other direction, we know from Theorem 1 that $t$ Fourier series converges to $f(x)$ for all $x$. To prove that the convergence is $u$ form, we will show that there is a constant $M$ such that $\left|a_{n}\right| \leq \frac{M}{n^{2}}$ and $\left|b_{n}\right| \leq$ Then $\left|a_{n} \cos n x+b_{n} \sin n x\right| \leq \frac{2 M}{n^{2}}$, and the uniform convergence will follow fre the Weierstrass $M$-test (Theorem 3, Section 4.2) since $\sum \frac{2 . M}{n^{2}}<\infty$. To simpl the proof, we will further suppose that $f^{\prime}$ is piecewise smooth. (This condition satisfied in all the examples in this book, and indeed most applications. A pr that does not depend on it is presented in Section 7.5 and uses Parseval's theore

---

<!-- Page 14 -->

Left margin note (page 14)

470
Chapter 7
Fo

Right margin note (page 14)

fact
and Then
lx)
mber 1 m of nuous that ty for
tt one cosine The puted es.

++++

urier Series

Integrating by parts, we find that
$$
\begin{aligned}
a_{n} & =\frac{1}{\pi} \int_{-\pi}^{\pi} f(x) \cos n x d x=\left.\frac{1}{n \pi} f(x) \sin n x\right|_{-\pi} ^{\pi}-\frac{1}{n \pi} \int_{-\pi}^{\pi} f^{\prime}(x) \sin n x d \\
& =-\frac{1}{n \pi} \int_{-\pi}^{\pi} f^{\prime}(x) \sin n x d x
\end{aligned}
$$
because $\sin n \pi=\sin (-n \pi)=0$. Similarly, integrating by parts and using the that $f(\pi)=f(-\pi)$, we obtain that
$$
b_{n}=\frac{1}{\pi} \int_{-\pi}^{\pi} f(x) \sin n x d x=\frac{1}{n \pi} \int_{-\pi}^{\pi} f^{\prime}(x) \cos n x d x
$$

The function $f^{\prime}(x)$ has a piecewise continuous derivative $f^{\prime \prime}(x)$. So $\left|f^{\prime}(x)\right| \leq A \left|f^{\prime \prime}(x)\right| \leq B$ for all $x$. Let $(a, b)$ be an interval on which $f^{\prime \prime}$ is continuous. integrating by parts, we find that
$$
\frac{1}{n \pi} \int_{a}^{b} f^{\prime}(x) \sin n x d x=\frac{1}{n^{2} \pi}\left(\left(f^{\prime}(a) \cos n a-f^{\prime}(b) \cos n b\right)+\int_{a}^{b} f^{\prime \prime}(x) \cos n x\right.
$$

Hence, because $\left|f^{\prime}(a)\right| \leq A,\left|f^{\prime}(b)\right| \leq A$, and $\left|f^{\prime \prime}(x) \cos n x\right| \leq B$, we obtain
$$
\frac{1}{n \pi}\left|\int_{a}^{b} f^{\prime}(x) \sin n x d x\right| \leq \frac{1}{n^{2} \pi}(2 A+(b-a) B) \leq \frac{C}{n^{2}}
$$
where $C$ is a constant that does not depend on $n$. Since $f^{\prime \prime}$ has a finite nu of discontinuities, we can write the integral $\int_{-\pi}^{\pi} f^{\prime}(x) \sin n x d x$ as the finite su integrals of the form $\int_{a}^{b} f^{\prime}(x) \sin n x d x$ (say, $k$ of them), where $f^{\prime \prime}(x)$ is contir on each interval $(a, b)$. It follows from our estimate on the latter integral $\left|a_{n}\right| \leq \frac{k C}{n^{2}}=\frac{M}{n^{2}}$, where $M=k C$ is a constant independent of $n$. The inequali $b_{n}$ is obtained in a similar way.

Theorems 1 or 2 can be used to sum interesting series.

EXAMPLE 3 Using Fourier series to sum series
If we take $x=0$ on both sides of (9), we get
$$
\pi=f(0)=\frac{1}{2} \pi+\frac{4}{\pi} \sum_{k=0}^{\infty} \frac{1}{(2 k+1)^{2}}
$$

Subtracting $\frac{1}{2} \pi$ and then multiplying by $\frac{\pi}{4}$, we get the interesting identity
$$
\frac{\pi^{2}}{8}=1+\frac{1}{3^{2}}+\frac{1}{5^{2}}+\frac{1}{7^{2}}+\ldots
$$
which can be used to approximate $\pi^{2}$ (and hence also $\pi$ ).
The Fourier series in Examples 1 and 2 are special in the sense tha of them contains only sine terms, while the other one contains only terms. Fourier series of this type will be studied in the next section following Fourier series contains both sine and cosine terms. It is com using the previous examples and the linearity property of Fourier seri

---

<!-- Page 15 -->

Left margin note (page 15)

![](./images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-15_489_476_1787_39.jpg)

Figure 11 Note the phenomenon at the poi discontinuity $(x=2 k \pi)$. is due to the fact tha Fourier series consists of sine part that is conve very fast (Figure 9) and part that overshoots a points of discontinuity.

![](./images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-15_404_1450_943_558.jpg)

Figure 12 The functio Example 5 and the the pa surns of its Fourier series with $n=1$ and 2 .

Right margin note (page 15)

ぶ ||
1
प्त है दि ल ए
CR $\downarrow^{*}$
க்க்.
Sou.
I

++++

Section 7.2 Fourier Series

EXAMPLE 4 A Fourier series with cosine and sine terms
Adding the two functions of Examples 1 and 2 , we obtain a $2 \pi$-periodic func which is defined on the interval $[0,2 \pi]$ by
$$
f(x)=\left\{\begin{array}{ll}
\frac{3}{2}(\pi-x) & \text { if } 0<x<\pi \\
\frac{1}{2}(-\pi+x) & \text { if } \pi<x<2 \pi
\end{array}\right.
$$
(You should check this formula and plot the function.) To compute the Fou series, we can use the Euler formulas or, better yet, we can simply add the Fou series of Examples 1 and 2, thanks to the linearity of the Fourier coefficients Exercise 18). We thus obtain the Fourier series representation
$$
f(x)=\frac{1}{2} \pi+\sum_{n=1}^{\infty}\left\{\frac{2}{\pi}\left(\frac{1}{n^{2}}-\frac{\cos n \pi}{n^{2}}\right) \cos n x+\frac{\sin n x}{n}\right\}
$$

Gibbs
nts of
This
t the
a co-
rging
a sine
t the

As illustrated in Figure 11, at the points of discontinuity, the Fourier series cc verges to the average value $\pi$. At all other points, the Fourier series converges $f(x)$.

Complex Methods for Finding Fourier Series
Because of Euler's identity $e^{i n \theta}=\cos n \theta+i \sin n \theta$, which relates t) complex exponential to the trigonometric functions, we expect the comple exponential function and complex analysis in general to play a role in th theory of Fourier series. This will become clear at many stages in our deve opment of Fourier series and their applications. In what follows, we illustra the use of major tools from complex analysis, such as residues and Laure

(θ) series, in computing Fourier series.

EXAMPLE 5 Using residues to compute Fourier series Find the Fourier series of $f(\theta)=\frac{1}{2+\cos \theta}$.
Solution The function is $2 \pi$-periodic and even. We have $b_{n}=\frac{1}{\pi} \int_{-\pi}^{\pi} f(\theta) \sin n \theta d \theta$ 0 , because $f(\theta) \sin n \theta$ is an odd function so its integral over a symmetric interval 0 . In computing $a_{n}$ for $n \geq 0$, we will evaluate the integral
$$
I_{n}=\int_{0}^{2 \pi} \frac{\cos n \theta}{2+\cos \theta} d \theta \quad(n=0,1, \ldots)
$$

---

<!-- Page 16 -->

Left margin note (page 16)

472
Chapter 7 Fourier Series

Right margin note (page 16)

n 7.1,
n 5.2,
- As
ositive
$\left.-z_{2}\right)$,
2. But
n 1(i),
gure 12.
ae order
ates the
$\_\_\_\_$
$\theta$,

++++

using a slight variation on the methods of Section 5.2. By Theorem 1, Sectio
$$
\int_{0}^{2 \pi} \frac{\sin n \theta}{2+\cos \theta} d \theta=\int_{-\pi}^{\pi} \frac{\sin n \theta}{2+\cos \theta} d \theta=0
$$
because the integrand in the second integral is odd. So
$$
I_{n}=\int_{0}^{2 \pi} \frac{\cos n \theta}{2+\cos \theta} d \theta+i \int_{0}^{2 \pi} \frac{\sin n \theta}{2+\cos \theta} d \theta=\int_{0}^{2 \pi} \frac{e^{i n \theta}}{2+\cos \theta} d \theta,
$$
where we have used $e^{i n \theta}=\cos n \theta+i \sin n \theta$. We now use the method of Sectic as follows. Let $z=e^{i \theta}, d z=i e^{i \theta} d \theta$ or $d \theta=\frac{d z}{i z}, z^{n}=e^{i n \theta}$, and $\cos \theta=\frac{e^{e^{\theta}}+e^{-}}{2} \theta$ varies over the interval $[0,2 \pi], z$ traverses the unit circle $C_{1}(0)$, in the po direction. So
$$
\begin{aligned}
I_{n} & =\int_{0}^{2 \pi} \frac{e^{i n \theta}}{2+\cos \theta} d \theta=\int_{0}^{2 \pi} \frac{e^{i n \theta}}{2+\frac{e^{\mathrm{i} \theta}+e^{-\mathrm{i} \theta}}{2}} d \theta \\
& =\int_{C_{1}(0)} \frac{2 z^{n}}{4+z+\frac{1}{z}} \frac{d z}{i z}=-i \int_{C_{1}(0)} \frac{2 z^{n}}{z^{2}+4 z+1} d z
\end{aligned}
$$

We compute the last integral using residues. We have $z^{2}+4 z+1=\left(z-z_{1}\right)(z$ where $z_{1}=-2+\sqrt{3}$ and $z_{2}=-2-\sqrt{3}$. We have two simple poles at $z_{1}$ and $z$ since $\left|z_{1}\right| \approx .3$ and $\left|z_{2}\right| \approx 3.7$, only $z_{1}$ is inside the unit disk. By Propositio Section 5.1, we have
$$
I_{n}=\left.(-2 i) 2 \pi i \frac{z^{n}}{z-z_{2}}\right|_{z=z_{1}}=2 \pi \frac{(-2+\sqrt{3})^{n}}{\sqrt{3}} .
$$

Using the formula for $I_{n}$, we obtain
$$
a_{0}=\frac{1}{2 \pi} I_{0}=\frac{1}{\sqrt{3}} \quad \text { and } \quad a_{n}=\frac{1}{\pi} I_{n}=2 \frac{(-2+\sqrt{3})^{n}}{\sqrt{3}}, \quad n=1,2, \ldots
$$

Thus the Fourier series representation
$$
\frac{1}{2+\cos \theta}=\frac{1}{\sqrt{3}}+\frac{2}{\sqrt{3}} \sum_{n=1}^{\infty}(-2+\sqrt{3})^{n} \cos n \theta,
$$
which is valid for all $\theta$. Partial sums of the Fourier series are plotted in Fi, Note how fast the series is converging, because the coefficients are of th $(-2+\sqrt{3})^{n}=\left|z_{1}\right|^{n}$, where $0<\left|z_{1}\right| \approx .3<1$.

Our next example generalizes the result of Example 5 and illustr use of Laurent series in computing Fourier series.

EXAMPLE 6 Using Laurent series to compute Fourier series
Let $a>1$ be a real number. Derive the Fourier series representation
$$
f(\theta)=\frac{1}{a+\cos \theta}=\frac{1}{\sqrt{a^{2}-1}}+\frac{2}{\sqrt{a^{2}-1}} \sum_{n=1}^{\infty}\left(-a+\sqrt{a^{2}-1}\right)^{n} \cos n
$$

---

<!-- Page 17 -->

Left margin note (page 17)

![](./images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-17_487_440_887_54.jpg)

Figure 13 The annu convergence of the Laure ries in Example 6.

++++

Section 7.2 Fourier Series

which is valid for all $\theta$.
Solution The function is $2 \pi$-periodic and smooth. By Theorem 2, its For series converges uniformly for all $\theta$ to $f(\theta)$. To find the Fourier series, we will compute the Fourier coefficients directly; instead we will match the function the restriction of a rational function and use Laurent series. As a first step, u the substitution $\cos \theta=\frac{1}{2}\left(z+\frac{1}{z}\right)$, where $z=e^{i \theta}$, we write
$$
\frac{1}{a+\cos \theta}=\frac{1}{a+\frac{1}{2}\left(z+\frac{1}{z}\right)}=\frac{2 z}{z^{2}+2 a z+1}
$$

Next, we expand $\frac{2 z}{z^{2}+2 a z+1}$ in an annulus that contains the unit circle $|z|=1$. we will see in a moment, this will allow us to use the Laurent series with $z=$ and obtain the desired Fourier series.

The quadratic equation $z^{2}+2 a z+1=0$ has two real roots $z_{1}=-a-\sqrt{a^{2}}$ and $z_{2}=-a+\sqrt{a^{2}-1}$. Because $a>1$, we have $z_{1}<-1$ and $-1<z_{2}<0$ ( should check these assertions). By Theorem 1, Section 4.5, we have a Laurent se expansion in the annulus $\left|z_{2}\right|<|z|<\left|z_{1}\right|$ (Figure 13), and to find it we emp methods from Section 4.5. We have the partial fraction decomposition
$$
\begin{aligned}
\frac{2 z}{z^{2}+2 a z+1} & =\frac{A}{z-z_{1}}+\frac{B}{z-z_{2}}=\frac{A\left(z-z_{2}\right)+B\left(z-z_{1}\right)}{z^{2}+2 a z+1} \\
& =\frac{z(A+B)-\left(A z_{2}+B z_{1}\right)}{z^{2}+2 a z+1}
\end{aligned}
$$

Solving
$$
\left\{\begin{array}{ll}
A+B & =2 \\
A z_{2}+B z_{1} & =0
\end{array}\right.
$$
we find $A=\frac{2 z_{1}}{z_{1}-z_{2}}=-\frac{z_{1}}{\sqrt{a^{2}-1}}$ and $B=-\frac{2 z_{2}}{z_{1}-z_{2}}=\frac{z_{2}}{\sqrt{a^{2}-1}}$, where we have us $z_{2}-z_{1}=2 \sqrt{a^{2}-1}$. So we have the partial fraction decomposition
$$
\frac{2 z}{z^{2}+2 a z+1}=\frac{1}{\sqrt{a^{2}-1}}\left(-\frac{z_{1}}{z-z_{1}}+\frac{z_{2}}{z-z_{2}}\right) .
$$

In the annulus $\left|z_{2}\right|<|z|<\left|z_{1}\right|$, the first term inside the parentheses on the rig can be expanded in a power series and the second one in a Laurent series, usi the geometric series as follows. For $|z|<\left|z_{1}\right|$, we have $\left|z / z_{1}\right|<1$ and so
$$
-\frac{z_{1}}{z-z_{1}}=-\frac{z_{1}}{z_{1}\left(\frac{z}{z_{1}}-1\right)}=\frac{1}{1-\left(\frac{z}{z_{1}}\right)}=\sum_{n=0}^{\infty}\left(\frac{z}{z_{1}}\right)^{n}, \quad|z|<\left|z_{1}\right|
$$

For $\left|z_{2}\right|<|z|$, we have $\left|z_{2} / z\right|<1$ and so
$$
\frac{z_{2}}{z-z_{2}}=\frac{z_{2}}{z\left(1-\frac{z_{2}}{z}\right)}=\frac{z_{2}}{z} \sum_{n=0}^{\infty}\left(\frac{z_{2}}{z}\right)^{n}, \quad\left|z_{2}\right|<|z| .
$$

Plugging into (11) and simplifying with the help of the identity $z_{1} z_{2}=1$ or $z_{2}=$

---

<!-- Page 18 -->

Left margin note (page 18)

474 Chapter 7 Fourier Serie

Right margin note (page 18)

t side after

ге ac$, 3 \pi]$. $x$
$x$
nterval tch the iverges

Discuss at the

++++

es

we get the Laurent series expansion
$$
\begin{aligned}
\frac{2 z}{z^{2}+2 a z+1} & =\frac{1}{\sqrt{a^{2}-1}} \sum_{n=0}^{\infty}\left[\left(\frac{z}{z_{1}}\right)^{n}+\frac{z_{2}}{z}\left(\frac{z_{2}}{z}\right)^{n}\right] \\
& =\frac{1}{\sqrt{a^{2}-1}}\left\{1+\sum_{n=1}^{\infty}\left[\left(\frac{z}{z_{1}}\right)^{n}+\left(\frac{z_{2}}{z}\right)^{n}\right]\right\} \\
& =\frac{1}{\sqrt{a^{2}-1}}\left\{1+\sum_{n=1}^{\infty} z_{2}^{n}\left(z^{n}+\frac{1}{z^{n}}\right)\right\}
\end{aligned}
$$
which is valid in the annulus $\left|z_{2}\right|<|z|<\left|z_{1}\right|$. In particular, for $z=e^{i \theta}$ the lef becomes $\frac{1}{a+\cos \theta}$ and the right side reduces to $\frac{1}{\sqrt{a^{2}-1}}\left\{1+\sum_{n=1}^{\infty} 2 z_{2}^{n} \cos n \theta\right\}$, using the identity $z^{n}+\frac{1}{z^{n}}=2 \cos n \theta$, which completes the proof.

Exercises 7.2
In Exercises $1-4$, a $2 \pi$-periodic function is specified on the interval $[-\pi, \pi]$ in $t$ ] companying figure (Figures 14-17). (a) Plot the function on the interval $[-3 \pi$ (b) Plot its Fourier series (without computing it) on the interval $[-3 \pi, 3 \pi]$.
1.

![](./images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-28_238_550_814_76.jpg)
Figure 14
2.

![](./images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-28_242_545_1167_85.jpg)
Figure 15
3.

![](./images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-28_244_551_1517_85.jpg)
Figure 16
4.

![](./images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-28_251_556_1884_87.jpg)
Figure 17

In Exercises 5-16, the equation of a $2 \pi$-periodic function is given on an ir of length $2 \pi$. You are also given the Fourier series of the function. (a) Sket function and its Fourier series on $[-2 \pi, 2 \pi]$, and decide whether the series cor uniformly for all $x$. (b) Derive the given Fourier series.
(c) Plot the $N$ th partial sums of the Fourier series for $N=1,2, \ldots, 20$. the convergence of the partial sums by considering their graphs. Be specific points of discontinuity.
5. $f(x)=|x|$ if $-\pi \leq x<\pi$.

Fourier series: $\quad \frac{\pi}{2}-\frac{4}{\pi} \sum_{k=0}^{\infty} \frac{1}{(2 k+1)^{2}} \cos (2 k+1) x$.

---

<!-- Page 19 -->

Right margin note (page 19)

475
$$
\pi / 2
$$

++++

Section 7.2 Fourier Series
6. $f(x)=\left\{\begin{array}{lll}\frac{1}{\pi} x & \text { if } & 0 \leq x \leq \pi, \\ 0 & \text { if } & -\pi<x \leq 0 .\end{array}\right.$

Fourier series: $\quad \frac{1}{4}-\frac{1}{\pi^{2}} \sum_{n=1}^{\infty}\left\{\left(\frac{1}{n^{2}}-\frac{(-1)^{n}}{n^{2}}\right) \cos n x+\frac{\pi(-1)^{n}}{n} \sin n x\right\}$
7. $f(x)=|\sin x|$ if $-\pi \leq x<\pi$.

Fourier series: $\quad \frac{2}{\pi}-\frac{4}{\pi} \sum_{k=1}^{\infty} \frac{1}{(2 k)^{2}-1} \cos 2 k x$.
8. $f(x)=|\cos x|$ if $-\pi \leq x \leq \pi$.

Fourier series: $\quad \frac{2}{\pi}-\frac{4}{\pi} \sum_{k=1}^{\infty} \frac{(-1)^{k}}{(2 k)^{2}-1} \cos 2 k x$.
[Hint: You can compute directly, or, if you have done Exercise 7 , substitute $x$ for $x$.]
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
f(x)=\left\{\begin{array}{ll}
0 & \text { if }-\pi \leq x \leq-d, \\
\frac{c}{d}(x+d) & \text { if }-d \leq x \leq 0, \\
-\frac{c}{d}(x-d) & \text { if } 0 \leq x \leq d, \\
0 & \text { if } d \leq x \leq \pi,
\end{array}\right.
$$
where $c, d>0$ and $d<\pi$.
Fourier series: $\quad \frac{c d}{2 \pi}+\frac{4 c}{d \pi} \sum_{n=1}^{\infty} \frac{\sin ^{2}\left(\frac{d n}{2}\right)}{n^{2}} \cos n x$.
For part (c), take $c=d=\pi / 2$.
15. $f(x)=e^{-|x|}$ if $-\pi \leq x \leq \pi$.

Fourier series:
$$
\frac{e^{\pi}-1}{\pi e^{\pi}}+\frac{2}{\pi e^{\pi}} \sum_{n=1}^{\infty} \frac{1}{n^{2}+1}\left(e^{\pi}-(-1)^{n}\right) \cos n x
$$

---

<!-- Page 20 -->

Left margin note (page 20)

476
Chapter 7 Fourier Series

Right margin note (page 20)

any $1, b_{2}$, urier ig the urent ries of ables.
$\sin n \theta) ; \sin n \theta)$.

++++

16.
$$
f(x)=\left\{\begin{array}{ll}
1 /(2 c) & \text { if }|x-d|<c, \\
0 & \text { if } c<|x-d|<\pi,
\end{array}\right.
$$
where $c, d>0$, and $c+d<\pi$.
Fourier series: $\frac{1}{2 \pi}+\frac{1}{c \pi} \sum_{n=1}^{\infty}\left(\frac{\sin (n c) \cos (n d)}{n} \cos n x+\frac{\sin (n c) \sin (n d)}{n} \sin n x\right)$
For part (c), take $c=d=\pi / 2$.
17. (a) Use the Fourier series of Exercise 9 to obtain
$$
\frac{\pi^{2}}{6}=1+\frac{1}{2^{2}}+\frac{1}{3^{2}}+\frac{1}{4^{2}}+\ldots
$$
(b) Use the Fourier series of Exercise 13 to obtain
$$
\frac{\pi}{4}=1-\frac{1}{3}+\frac{1}{5}-\frac{1}{7}+\ldots
$$
18. Linearity of Fourier coefficients and Fourier series Let $\alpha$ and $\beta$ be real numbers. Show that if $f$ and $g$ have Fourier coefficients $a_{0}, a_{1}, a_{2}, \ldots, b \ldots$, respectively, $a_{0}^{*}, a_{1}^{*}, a_{2}^{*}, \ldots, b_{1}^{*}, b_{2}^{*}, \ldots$, then the function $\alpha f+\beta g$ has $F_{0}$ coefficients $\alpha a_{0}+\beta a_{0}^{*}, \alpha a_{1}+\beta a_{1}^{*}, \alpha a_{2}+\beta a_{2}^{*}, \ldots, \alpha b_{1}+\beta b_{1}^{*}, \alpha b_{2}+\beta b_{2}^{*}, \ldots$.
Methods from Complex Analysis
In Exercise 19-20, compute the Fourier series of the given function, followir method in Example 5. Verify your answer by using the result of Example 6.
19. $\frac{1}{3+2 \cos \theta}$.
20. $\frac{3 \sin \theta}{10-6 \cos \theta}$.

In Exercise 21-24, compute the Fourier series of the given function, using Lc series as we did in Example 6.
21. $\frac{1}{3+\cos \theta}$.
22. $e^{2 \cos \theta}$.
23. $\frac{1}{3+\cos \theta+\sin \theta}$.
24. $\quad e^{\cos \theta} \cos (\sin \theta)$.

In Exercise 25-26, derive the given Fourier series by using the Fourier se Example 6 and various manipulations, including appropriate changes of var
25. Let $a>1$ be a real number. Then
$$
\frac{1}{a-\cos \theta}=\frac{1}{\sqrt{a^{2}-1}}+\frac{2}{\sqrt{a^{2}-1}} \sum_{n=1}^{\infty}(-1)^{n}\left(-a+\sqrt{a^{2}-1}\right)^{n} \cos n \theta,
$$
which is valid for all $\theta$.
26. Let $a>1$ be a real number. Then for all $\theta$,
$$
\frac{1}{a+\sin \theta}=\frac{1}{\sqrt{a^{2}-1}}+\frac{2}{\sqrt{a^{2}-1}} \sum_{n=1}^{\infty}\left(-a+\sqrt{a^{2}-1}\right)^{n}\left(\cos \frac{n \pi}{2} \cos n \theta+\sin \frac{n \pi}{2}\right.
$$
and
$$
\frac{1}{a-\sin \theta}=\frac{1}{\sqrt{a^{2}-1}}+\frac{2}{\sqrt{a^{2}-1}} \sum_{n=1}^{\infty}\left(-a+\sqrt{a^{2}-1}\right)^{n}\left(\cos \frac{n \pi}{2} \cos n \theta-\sin \frac{n \pi}{2}\right.
$$

---

<!-- Page 21 -->

Left margin note (page 21)

7.3 Fourier

![](./images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-21_409_489_820_83.jpg)

Figure 1 A $2 p$-perio tion.

THEO
FOURIER S
REPRESENTA
ARBIT
Pl

By Theorem 1, Sect all the integrals $\int$ be replaced by $\int_{0}^{2 p}$ changing the values coefficients.

++++

Section 7.3 Fourier Series of Functions with Arbitrary Periods
477
27. Let $a>1$ be a real number. Use Example 6 and Exercise 25 to derive the following formulas: for $n \geq 1$,
$$
\begin{aligned}
\frac{1}{2 \pi} \int_{-\pi}^{\pi} \frac{d \theta}{a+\cos \theta} & =\frac{1}{\sqrt{a^{2}-1}} \\
\frac{1}{2 \pi} \int_{-\pi}^{\pi} \frac{\cos n \theta}{a+\cos \theta} d \theta & =\frac{1}{\sqrt{a^{2}-1}}\left(-a+\sqrt{a^{2}-1}\right)^{n} \\
\frac{1}{2 \pi} \int_{-\pi}^{\pi} \frac{\cos n \theta}{a-\cos \theta} d \theta & =\frac{(-1)^{n}}{\sqrt{a^{2}-1}}\left(-a+\sqrt{a^{2}-1}\right)^{n}
\end{aligned}
$$

Series of Functions with Arbitrary Periods
In the preceding section we worked with functions of period $2 \pi$. The choice of this period was merely for convenience. In this section, we show how to extend our results to functions with arbitrary period by using a simple
dic func-

REM 1
ERIES
TION:
RARY
ERIOD
ion 7.1,
${ }_{-p}^{p}$ can without of the
change of variables. Suppose that $f$ is a function with period $T=2 p>0$, and let
$$
g(x)=f\left(\frac{p}{\pi} x\right) .
$$

Since $f$ is $2 p$-periodic, we have
$$
g(x+2 \pi)=f\left(\frac{p}{\pi}(x+2 \pi)\right)=f\left(\frac{p}{\pi} x+2 p\right)=f\left(\frac{p}{\pi} x\right)=g(x) .
$$

Hence $g$ is $2 \pi$-periodic. This reduction enables us to extend the main results of Section 7.2 to functions of arbitrary period.

Suppose that $f$ is a $2 p$-periodic piecewise smooth function. Then $f$ has a unique Fourier series representation
$$
\frac{f(x-)+f(x+)}{2}=a_{0}+\sum_{n=1}^{\infty}\left(a_{n} \cos \frac{n \pi}{p} x+b_{n} \sin \frac{n \pi}{p} x\right),
$$
where the Fourier coefficients are given by
(3)
$$
a_{0}=\frac{1}{2 p} \int_{-p}^{p} f(x) d x
$$
(4)
$$
a_{n}=\frac{1}{p} \int_{-p}^{p} f(x) \cos \frac{n \pi}{p} x d x \quad(n=1,2, \ldots),
$$
(5)
$$
b_{n}=\frac{1}{p} \int_{-p}^{p} f(x) \sin \frac{n \pi}{p} x d x \quad(n=1,2, \ldots)
$$

If $f$ is continuous at $x$, then the Fourier series converges to $f(x)$. The series converges uniformly for all $x$ if and only if $f$ is continuous for all $x$.

---

<!-- Page 22 -->

Left margin note (page 22)

478
Chapter 7

![](./images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-22_373_523_1684_109.jpg)

Figure 2 Tria with period $2 p$.

Right margin note (page 22)

$d x$.
$f$ as cmula
o the from em 2,
$x \leq p$
under
netion
if $n$ is for all

++++

urier Series

Proof Since $f$ is piecewise smooth, it follows that the $2 \pi$-periodic funct defined by (1) is also piecewise smooth. By Theorem 1 of Section 7.2 we have
$$
\frac{g(x-)+g(x+)}{2}=a_{0}+\sum_{n=1}^{\infty}\left(a_{n} \cos n x+b_{n} \sin n x\right) \quad(\text { for all } x),
$$
where
$$
a_{0}=\frac{1}{2 \pi} \int_{-\pi}^{\pi} g(x) d x ; a_{n}=\frac{1}{\pi} \int_{-\pi}^{\pi} g(x) \cos n x d x ; b_{n}=\frac{1}{\pi} \int_{-\pi}^{\pi} g(x) \sin n x
$$

Replacing $x$ by $\frac{\pi}{p} x$ in (6) and using (1) gives
$$
\frac{f(x-)+f(x+)}{2}=a_{0}+\sum_{n=1}^{\infty}\left(a_{n} \cos \frac{n \pi}{p} x+b_{n} \sin \frac{n \pi}{p} x\right),
$$
where the coefficients are given by (7). To express the coefficients in terms of in (3)-(5), we use (1) again. For example, to obtain (3), start with the first for in (7), use (1), then use the change of variables $t=\frac{p}{\pi} x$, and get
$$
a_{0}=\frac{1}{2 \pi} \int_{-\pi}^{\pi} g(x) d x=\frac{1}{2 \pi} \int_{-\pi}^{\pi} f\left(\frac{p}{\pi} x\right) d x=\frac{1}{2 p} \int_{-p}^{p} f(t) d t
$$

Formulas (4) and (5) are derived in a similar way. The details are left exercises. The uniqueness and the uniform convergence in the theorem follow the corresponding results for $2 \pi$-periodic functions (Corollary 1 and Theor Section 7.2).

EXAMPLE 1 A Fourier series with arbitrary period
Find the Fourier series of the $2 p$-periodic function given by $f(x)=|x|$ if $-p \leq$ (Figure 2).
Solution We compute the Fourier coefficients using Theorem 1. The area the graph of $f$ in Figure 2 gives
$$
a_{0}=\frac{1}{2 p} \int_{-p}^{p} f(x) d x=\frac{p}{2}
$$

To compute $a_{n}$ we take advantage of the fact that $f(x) \cos \frac{n \pi}{p} x$ is an even fu and write
$$
\begin{aligned}
a_{n} & =\frac{1}{p} \int_{-p}^{p} f(x) \cos \frac{n \pi}{p} x d x=\frac{2}{p} \int_{0}^{p} f(x) \cos \frac{n \pi}{p} x d x \\
& =\frac{2}{p} \int_{0}^{p} x \cos \frac{n \pi}{p} x d x=\frac{-2 p}{\pi^{2} n^{2}}(1-\cos n \pi)
\end{aligned}
$$
where the last integral is evaluated by parts. Since $\cos n \pi=(-1)^{n}, a_{n}=0$ even, and $a_{n}=\frac{-4 p}{\pi^{2} n^{2}}$ if $n$ is odd. A similar computation shows that $b_{n}=0 n$ (since $f$ is even). We thus obtain the Fourier series
$$
f(x)=\frac{p}{2}-\frac{4 p}{\pi^{2}}\left(\cos \frac{\pi}{p} x+\frac{1}{3^{2}} \cos \frac{3 \pi}{p} x+\frac{1}{5^{2}} \cos \frac{5 \pi}{p} x+\ldots\right)
$$

---

<!-- Page 23 -->

Left margin note (page 23)

![](./images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-23_338_471_229_67.jpg)

Figure 3 Partial sums Fourier series $(p=1)$,
ample 1.

![](./images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-23_386_463_728_62.jpg)

Figure 4 A $2 p$-periodic gular wave.

![](./images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-23_399_458_1691_51.jpg)

Figure 5 A $2 p$-periodic tooth function.

++++

Section 7.3 Fourier Series of Functions with Arbitrary Periods
479

Because $f$ is continuous and piecewise smooth, Theorem 1 implies that the Fourier series converges uniformly to $f(x)$ for all $x$, as can be seen in Figure 3.

Sometimes we can derive a new Fourier series from a known one without performing many additional computations. The following examples illustrate this process.

EXAMPLE 2 Triangular wave with arbitrary period and amplitude
Find the Fourier series of the $2 p$-periodic function given by
$$
g(x)=\left\{\begin{array}{ll}
a\left(1+\frac{1}{p} x\right) & \text { if }-p \leq x \leq 0 \\
a\left(1-\frac{1}{p} x\right) & \text { if } 0 \leq x \leq p
\end{array}\right.
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

EXAMPLE 3 Varying the period in a Fourier series
Find the Fourier series of the function in Figure 5.
Solution Let us start by defining the function in Figure 5. On the interval $0<x<2 p$, we have $f(x)=c\left(1-\frac{x}{p}\right)$. Now, from Example 1, Section 7.2, we have the Fourier series expansion
$$
\frac{1}{2}(\pi-x)=\sum_{n=1}^{\infty} \frac{\sin n x}{n}, \text { for } 0<x<2 \pi
$$

---

<!-- Page 24 -->

Left margin note (page 24)

480
Chapter 7
F

![](./images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-24_449_635_1836_629.jpg)

Figure 6 (a) Ev
The graph is syn respect to the $y-\varepsilon$ function: The g metric with respe gin.

![](./images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-24_450_665_1830_1310.jpg)

Right margin note (page 24)

get
ed on ed as olving mula eries, s was
uting even
ables)

++++

ourier Series

Replacing $x$ by $\frac{\pi}{p} x$ in the formula and the interval for $x$, we get
$$
\frac{1}{2}\left(\pi-\frac{\pi}{p} x\right)=\sum_{n=1}^{\infty} \frac{\sin \frac{n \pi}{p} x}{n}, \text { for } 0<\frac{\pi}{p} x<2 \pi
$$

Simplifying and multiplying both sides by $c$ to match the formula for $f$, we
$$
c\left(1-\frac{x}{p}\right)=\frac{2 c}{\pi} \sum_{n=1}^{\infty} \frac{\sin \frac{n \pi}{p} x}{n}, \text { for } 0<x<2 p,
$$
which yields the Fourier series of $f$.
The ideas behind Examples 2 and 3 are quite simple. They are bas the fact that a Fourier series is really a function and can be manipulat such. As with any infinite series, when you manipulate a formula inve a Fourier series, you must keep in mind the interval on which this for is valid. In particular, when you perform an operation on a Fourier s it may affect the interval on which the resulting series is defined. Thi the case when we performed a change of variables in Example 3.
Even and Odd Functions
As we noticed already, geometric considerations are helpful in comp Fourier coefficients. This is particularly the case when dealing with and odd functions. Recall the following definitions:

A function $f$ is even if $f(-x)=f(x)$ for all $x$.
A function $f$ is odd if $f(-x)=-f(x)$ for all $x$.
en function: metric with xis. (b) Odd raph is symect to the ori-

(a) Even function

(b) Odd function

It is clear from the graphs in Figure 6 (or by a simple change of vari that if $f$ is even, then
$$
\int_{-p}^{p} f(x) d x=2 \int_{0}^{p} f(x) d x
$$

---

<!-- Page 25 -->

Left margin note (page 25)

THEOREI
FOURIER SERIES
EVEN AND O
FUNCTIO

++++

Section 7.3 Fourier Series of Functions with Arbitrary Periods
481

and if $f$ is odd, then
$$
\int_{-p}^{p} f(x) d x=0 .
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

M 2

Suppose that $f$ is $2 p$-periodic and has the Fourier series representation (2).

OF Then (i) $f$ is even if and only if $b_{n}=0$ for all $n$. In this case

DD
NS
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

---

<!-- Page 26 -->

Left margin note (page 26)

482
Chapter 7

![](./images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-26_385_535_490_108.jpg)

Figure 7 An eve

![](./images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-26_371_533_1149_126.jpg)

Figure 8 Partia Fourier series in

![](./images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-26_388_548_2061_124.jpg)

Figure 9 The o Example 5.

Right margin note (page 26)

< 1 .
n. To
ous and
er series
D
$\_\_\_\_$
rwise, is er series

++++

Fourier Series

EXAMPLE 4 Fourier series of an even function Find the Fourier series of the 2 -periodic function $f(x)=1-x^{2}$ if $-1<x$
Solution The function $f$ is even (see Figure 7); hence $b_{n}=0$ for all compute the $a_{n}$ 's, we use Theorem 2 with $p=1$ and get
$-x^{2}$
$\overbrace{1} \overbrace{x}$
n function.

1 sums of the
Example 4.
dd function in
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
which can be derived by two integrations by parts. Since $f$ is continu piecewise smooth, we get
$$
f(x)=\frac{2}{3}-\frac{4}{\pi^{2}} \sum_{n=1}^{\infty} \frac{(-1)^{n}}{n^{2}} \cos n \pi x
$$
for all $x$. Since $f$ is continuous and piecewise smooth for all $x$, its Fouri converges uniformly to $f(x)$, as illustrated in Figure 8.

EXAMPLE 5 Fourier series of an odd function
The function $f(x)=x \cos x$, if $-\frac{\pi}{2}<x<\frac{\pi}{2}$, and $f(x+\pi)=f(x)$ othe shown in Figure 9. It is $\pi$-periodic and odd. From Theorem 2, its Fouri is given by
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

---

<!-- Page 27 -->

Left margin note (page 27)

![](./images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-27_362_454_895_56.jpg)

Figure 10 Graphs of $s_{2}(x)$ and $s_{4}(x)$, in Exa 5.

![](./images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-27_240_444_2135_42.jpg)

Figure 11

++++

Section 7.3 Fourier Series of Functions with Arbitrary Periods
483

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

$x$
$\pi / 2$

Thus
$$
f(x)=\frac{16}{\pi}\left[\frac{1}{9} \sin 2 x-\frac{2}{225} \sin 4 x+\ldots\right]
$$

![](./images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-27_362_454_895_56.jpg)
Figure 10 illustrates the uniform convergence of the Fourier series to $f(x)$. Along with $f(x)$, we have plotted the partial sums $s_{2}(x)$ and $s_{4}(x)$. The graphs of $s_{4}(x)$ and $f(x)$ can hardly be distinguished from one another, which suggests that the Fourier series converges very fast to $f(x)$.

In the next section we use Fourier series of even and odd functions to periodically extend functions that are defined on finite intervals. As we will see in Chapter 8, this process will be needed in solving partial differential equations by means of Fourier series.
Exercises 7.3
In Exercises 1-10, a 2p-periodic function is given on an interval of length $2 p$ in the accompanying figure (Figures 11-20). (a) State whether the function is even, odd, or neither. (b) Derive the given Fourier series, and determine its values at the points of discontinuity. State if the series converges uniformly for all $x$. (Most of these Fourier series can be derived from earlier examples and exercises, as illustrated by Examples 3 and 4.)
1.
$$
f(x)=\left\{\begin{array}{ll}
1 & \text { if } 0<x<p \\
-1 & \text { if }-p<x<0
\end{array}\right.
$$

Fourier series: $\frac{4}{\pi} \sum_{k=0}^{\infty} \frac{1}{(2 k+1)} \sin \frac{(2 k+1) \pi}{p} x$.

---

<!-- Page 28 -->

Left margin note (page 28)

484
Chapter 7
F

![](./images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-28_252_547_191_62.jpg)

Figure 12

![](./images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-28_244_537_490_74.jpg)

Figure 13

![](./images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-28_238_550_814_76.jpg)

Figure 14

![](./images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-28_242_545_1167_85.jpg)

Figure 15

![](./images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-28_244_551_1517_85.jpg)

Figure 16

![](./images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-28_251_556_1884_87.jpg)

Figure 17

![](./images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-28_261_575_2298_78.jpg)

Figure 18

++++

ourier Series
2. $f(x)=x$ if $-p<x<p$. [Hint: Exercise 13, Section 7.2.]

Fourier series: $\quad \frac{2 p}{\pi} \sum_{n=1}^{\infty} \frac{(-1)^{n+1}}{n} \sin \left(\frac{n \pi}{p} x\right)$.
3. $f(x)=a\left(1-\left(\frac{x}{p}\right)^{2}\right)$ if $-p \leq x \leq p,(a \neq 0)$.

Fourier series: $\quad \frac{2}{3} a+4 a \sum_{n=1}^{\infty} \frac{(-1)^{n+1}}{(n \pi)^{2}} \cos \left(\frac{n \pi}{p} x\right)$.
4. $f(x)=x^{2}$ if $-p \leq x \leq p$. [Hint: Use Exercise 3.]

Fourier series: $\frac{p^{2}}{3}-\frac{4 p^{2}}{\pi^{2}}\left[\cos \left(\frac{\pi}{p} x\right)-\frac{1}{2^{2}} \cos \left(\frac{2 \pi}{p} x\right)+\frac{1}{3^{2}} \cos \left(\frac{3 \pi}{p} x\right)-\ldots\right]$
5.
$$
f(x)=\left\{\begin{array}{ll}
-\frac{2 c}{p}(x-p / 2) & \text { if } 0 \leq x \leq p, \\
\frac{2 c}{p}(x+p / 2) & \text { if }-p \leq x \leq 0,
\end{array}\right.
$$
where $c \neq 0$ (in the picture $c>0$.)
Fourier series: $\quad \frac{8 c}{\pi^{2}} \sum_{k=0}^{\infty} \frac{1}{(2 k+1)^{2}} \cos \left((2 k+1) \frac{\pi}{p} x\right)$.
6.
$$
f(x)=\left\{\begin{array}{ll}
c & \text { if }|x|<d \\
0 & \text { if } d<|x|<p
\end{array}\right.
$$
where $0<d<p$.
Fourier series: $\frac{c d}{p}+\frac{2 c}{\pi} \sum_{n=0}^{\infty} \frac{\sin \left(\frac{d n \pi}{p}\right)}{n} \cos \left(\frac{n \pi}{p} x\right)$.
7.
$$
f(x)=\left\{\begin{array}{ll}
-\frac{2}{p}(x-p / 2) & \text { if } 0<x<p, \\
-\frac{2}{p}(x+p / 2) & \text { if }-p<x<0 .
\end{array}\right.
$$

Fourier series: $\frac{4}{\pi} \sum_{k=1}^{\infty} \frac{1}{2 k} \sin \left(\frac{2 k \pi}{p} x\right)$.
8.
$$
f(x)=\left\{\begin{array}{ll}
-\frac{c}{d}(x-d) & \text { if } 0 \leq x \leq d, \\
0 & \text { if } d \leq|x| \leq p, \\
\frac{c}{d}(x+d) & \text { if }-d \leq x \leq 0,
\end{array}\right.
$$
where $0 \leq d \leq p$.
Fourier series: $\frac{c d}{2 p}+\frac{2 c p}{d \pi^{2}} \sum_{n=1}^{\infty} \frac{1}{n^{2}}\left(1-\cos \left(\frac{d n \pi}{p}\right)\right) \cos \left(\frac{n \pi}{p} x\right)$.

---

<!-- Page 29 -->

Left margin note (page 29)

![](./images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-29_272_478_146_37.jpg)

Figure 19

![](./images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-29_264_478_495_36.jpg)

Figure 20

![](./images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-29_299_571_1452_618.jpg)
![](./images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-29_297_577_1452_1310.jpg)

Right margin note (page 29)

ध्री

++++

Section 7.3 Fourier Series of Functions with Arbitrary Periods
$>0$
9. $f(x)=e^{-c|x|}(c \neq 0)$ for $|x| \leq p$.

$\vec{p}^{x}$

Fourier series: $\quad \frac{1}{p c}\left(1-e^{-c p}\right)+2 c p \sum_{n=1}^{\infty} \frac{1}{c^{2} p^{2}+(n \pi)^{2}}\left(1-e^{-c p}(-1)^{n}\right) \cos \left(\frac{n \pi}{p} x\right)$.
10.
$$
f(x)=\left\{\begin{array}{ll}
-\frac{1}{p-c}(x-p) & \text { if } c<x<p, \\
1 & \text { if }|x|<c, \\
\frac{1}{p-c}(x+p) & \text { if }-p<x<-c,
\end{array}\right.
$$
where $0<c<p$.
Fourier series: $\quad \frac{p+c}{2 p}+\frac{2 p}{(c-p) \pi^{2}} \sum_{n=1}^{\infty} \frac{1}{n^{2}}\left((-1)^{n}-\cos \left(\frac{c n \pi}{p}\right)\right) \cos \left(\frac{n \pi}{p} x\right)$.
11. (a) Find the Fourier series of the $2 \pi$-periodic function given on the inter $-\pi<x<\pi$ by $f(x)=x \sin x$.
(b) Plot several partial sums to illustrate the convergence of the Fourier series.
12. (a) Find the Fourier series of the $2 \pi$-periodic function given on the interv $-\pi<x<\pi$ by $f(x)=(\pi-x) \sin x$. [Hint: Exercise 11.]
(b) Plot several partial sums to illustrate the convergence of the Fourier series.

In Exercises 13-14 a function is given over one period by a figure (Figures 21-22
(a) Find its Fourier series. [Hint: Use Exercise 1.]
(b) Plot several partial sums to illustrate the convergence of the Fourier series.
13.

![](./images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-29_299_571_1452_618.jpg)
Figure 21
14.

![](./images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-29_297_577_1452_1310.jpg)
Figure 22
15. Obtain the Fourier series of Example 2, Section 7.2, from Example 2 of thi section.
16. (a) Illustrate graphically the answer in Exercise 6 by taking $p=1, c=1, d=$ and by plotting several partial sums of the Fourier series.
(b) What happens to the Fourier coefficients as $d$ approaches $p$ ? Justify you answer.
17. Use the result of Exercise 4 to derive the formulas
(a) $\frac{\pi^{2}}{12}=1-\frac{1}{2^{2}}+\frac{1}{3^{2}}-\frac{1}{4^{2}}+\cdots$
(b) $\frac{\pi^{2}}{8}=1+\frac{1}{3^{2}}+\frac{1}{5^{2}}+\frac{1}{7^{2}}+\cdots$
[Hint: Use (a) also.]
18. Derive (4) and (5) of Theorem 1.
[Hint: Study the proof of Theorem 1.]
19. Prove part (ii) of Theorem 2.

Project Problem: Decomposition into even and odd parts. Do Exercise 2 and any one of 21-24. You will discover how an arbitrary function can be decom

---

<!-- Page 30 -->

Left margin note (page 30)

486
Chapter 7

Right margin note (page 30)

the
ction that that $f_{0}$ is erval (see of $f$. $\boldsymbol{x} \xrightarrow{x}$ ies be 5, 26, s. ewise $a_{n}, b_{n}$ parts a $2 p$ ewise

++++

ourier Series

posed into the sum of an even and odd function.
20. Let $f$ be an arbitrary function defined for all real numbers. Conside functions
$$
f_{\mathrm{e}}(x)=\frac{f(x)+f(-x)}{2} \text { and } f_{\mathrm{o}}(x)=\frac{f(x)-f(-x)}{2}
$$
(a) Show that $f_{\mathrm{e}}$ is even and $f_{\mathrm{o}}$ is odd.
(b) Show that $f=f_{\mathrm{e}}+f_{\mathrm{o}}$. Hence every function is the sum of an even fun and an odd function. Moreover, show that this decomposition is unique.
(c) In the remainder of this exercise, we suppose that $f$ is $2 p$-periodic. Show $f_{\mathrm{e}}$ and $f_{\mathrm{o}}$ are both $2 p$-periodic.
(d) Let $a_{0}, a_{1}, a_{2}, \ldots, b_{1}, b_{2}, \ldots$ denote the Fourier coefficients of $f$. Show the Fourier series of $f_{\mathrm{e}}$ is $a_{0}+\sum_{n=1}^{\infty} a_{n} \cos \frac{n \pi}{p} x$, and the Fourier series of $\sum_{n=1}^{\infty} b_{n} \sin \frac{n \pi}{p} x$.
In Exercises 21-24, a 2 -periodic function is given by its graph over the int $[-1,1]$ (Figures 23-26). In each case, (a) determine and plot $f_{\mathrm{e}}$ and $f_{\mathrm{o}}$ Exercise 20).
(b) Find the Fourier series of $f_{e}$ and $f_{o}$, and then deduce the Fourier series
21.

![](./images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-30_277_559_1096_714.jpg)
Figure 23
22.

![](./images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-30_283_612_1082_1383.jpg)
Figure 24
23.

![](./images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-30_286_553_1493_728.jpg)
Figure 25
24.

![](./images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-30_281_609_1493_1395.jpg)
Figure 26

Project Problem: Differentiation of Fourier series. Can a Fourier ser differentiated term by term? The answer is no, in general. Do Exercises 2 and any one of 27-30, and you will learn when you can safely use this proces
25. Fourier series and derivatives. Suppose that $f$ is a $2 p$-periodic, piec smooth and continuous function such that $f^{\prime}$ is also piecewise smooth. Let denote the Fourier coefficients of $f$ and $a_{n}^{\prime}, b_{n}^{\prime}$ those of $f^{\prime}$. Show that
$$
a_{0}^{\prime}=0, \quad a_{n}^{\prime}=b_{n} \frac{n \pi}{p}, \quad \text { and } \quad b_{n}^{\prime}=-a_{n} \frac{n \pi}{p}
$$
[Hint: To compute the Fourier coefficients of $f^{\prime}$, evaluate the integrals by and use $f(p)=f(-p)$.]
26. Term-by-term differentiation of Fourier series. Suppose that $f$ is periodic piecewise smooth and continuous function such that $f^{\prime}$ is also piec

---

<!-- Page 31 -->

Left margin note (page 31)

![](./images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-31_224_448_1096_54.jpg)

Figure 27 for Exercise 29.

![](./images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-31_228_454_1463_56.jpg)

Figure 28 for Exercise 30.

++++

Section 7.3 Fourier Series of Functions with Arbitrary Periods
487

smooth. Show that the Fourier series of $f^{\prime}$ is obtained from the Fourier series of $f$ by differentiating term by term. That is, under the stated conditions, if
$$
f(x)=a_{0}+\sum_{n=1}^{\infty}\left(a_{n} \cos \frac{n \pi}{p} x+b_{n} \sin \frac{n \pi}{p} x\right)
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

---

<!-- Page 32 -->

Left margin note (page 32)

488
Chapter 7 Fou
7.4 Half-Ra

THEO
HALF-F
EXPAI

Right margin note (page 32)

mpof $F$ It of ?).] se 2.
es a nce dily y a
erval
$f$ is
exame ling m 2,
$<p$, efine c) = f the

++++

rier Series

where $A_{0}=\frac{p}{\pi} \sum_{n=1}^{\infty} \frac{\delta_{n}}{n}$. Hence, as long as $F$ is periodic, with no further assu tions on $f$ other than piecewise smoothness, we can get the Fourier series by integrating term by term the Fourier series of $f$. [Hint: Apply the resu Exercise 25 to $F(x)$ and use $F^{\prime}(x)=f(x)$. To compute $A_{0}$, use $F(0)=0$ (wh)
34. Use Exercise 33 to derive the Fourier series of Exercise 4 from that of Exerci
nge Expansions: The Cosine and Sine Series
In many applications we are interested in representing by a Fourier seri function $f(x)$ that is defined only in a finite interval, say $0<x<p$. Si $f$ is clearly not periodic, the results of the previous sections are not rea applicable. Our goal in this section is to show how we can represent $f$ t Fourier series, after extending it to a periodic function.

REM 1 RANGE JSIONS

Suppose that $f(x)$ is a piecewise smooth function defined on an int $0<x<p$. Then $f$ has a cosine series expansion
(1)
$$
a_{0}+\sum_{n=1}^{\infty} a_{n} \cos \frac{n \pi}{p} x \quad(0<x<p)
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
$$
b_{n}=\frac{2}{p} \int_{0}^{p} f(x) \sin \frac{n \pi}{p} x d x \quad(n \geq 1)
$$

On the interval $0<x<p$, the series (1) and (3) converge to $f(x)$ i continuous at $x$ and to $\frac{f(x+)+f(x-)}{2}$ otherwise.

The series (1) and (3) are commonly referred to as the half-range pansions of $f$. They are two different series representations of the $s$ function on the interval $0<x<p$. Theorem 1 will be derived by appea to the Fourier series representation of even and odd functions (Theore Section 7.3). For this purpose, we introduce the following notions.

Define the even periodic extension of $f$ by $f_{1}(x)=f(x)$ if $0<x f_{1}(x)=f(-x)$ if $-p<x<0$, and $f_{1}(x)=f_{1}(x+2 p)$ otherwise. D the odd periodic extension of $f$ by $f_{2}(x)=f(x)$ if $0<x<p, f_{2}$ ( $-f(-x)$ if $-p<x<0$, and $f_{2}(x)=f_{2}(x+2 p)$ otherwise. (In view

---

<!-- Page 33 -->

Left margin note (page 33)

![](./images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-33_424_569_317_70.jpg)

Figure 1 (a) $f(x), 0<$

![](./images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-33_424_620_327_710.jpg)

Figure 2 (a) $f(x)=x$,

![](./images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-33_428_621_323_1397.jpg)
![](./images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-33_284_405_1481_164.jpg)
![](./images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-33_276_646_1481_694.jpg)
![](./images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-33_276_647_1487_1383.jpg)

Right margin note (page 33)

489 the

$\stackrel{x}{\mapsto}$
$f_{2}$.
and
the
1).
vise
sine
(x)
val.
$\xrightarrow{x}$
We
ver,
sing

++++

Section 7.4 Half-Range Expansions: The Cosine and Sine Series

remark following Theorem 1 of Section 7.2 , we will not worry about definition of the extensions at the points $0, \pm p, \pm 2 p, \ldots$.)
$$
x<p .
$$
(b) Even $2 p$-periodic extension, $f_{1}$.

(c) Odd $2 p$-periodic extension,

By the way they are constructed, the function $f_{1}$ is even and $2 p$-periodic, the function $f_{2}$ is odd and $2 p$-periodic. Both functions agree with $f$ on interval $0<x<p$ which justifies calling them extensions of $f$ (Figure Since $f$ is piecewise smooth, it follows that $f_{1}$ and $f_{2}$ are both piecev smooth. Applying Theorem 2 of Section 7.3, we find that $f_{1}$ has a cos series expansion given by (1) with the coefficients (2). Now $f(x)=f_{1}$ for all $0<x<p$, and so the cosine series (1) represents $f$ on this inter Similar reasoning using $f_{2}$ yields the sine series expansion of $f$.

EXAMPLE 1 Half-range expansions
Find the half-range expansions of the function $f(x)=x$ for $0<x<1$.
Solution The graphs of the even and odd extensions are shown in Figure 2.

(b) Even extension of $f$, period 2.

(c) Odd extension of $f$, period 2

The even extension is a special case of Example 1 of Section 7.3 with $p=1$. have
$$
x=\frac{1}{2}-\frac{4}{\pi^{2}} \sum_{k=0}^{\infty} \frac{1}{(2 k+1)^{2}} \cos (2 k+1) \pi x, \quad \text { for all } 0 \leq x \leq 1 .
$$

The odd extension is a special case of Exercise 2 of Section 7.3, with $p=1$. Howe to illustrate the formulas of Theorem 1, we will derive the sine coefficients us (4). We have
$$
b_{n}=\frac{2}{1} \int_{0}^{1} x \sin n \pi x d x=\frac{2(-1)^{n+1}}{n \pi} .
$$

Hence
$$
x=\frac{2}{\pi} \sum_{n=1}^{\infty} \frac{(-1)^{n+1}}{n} \sin n \pi x, \quad 0 \leq x<1 .
$$

---

<!-- Page 34 -->

Left margin note (page 34)

490
Chapter 7
F

![](./images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-34_302_554_569_151.jpg)

Figure 3 (a) $f(x)$

![](./images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-34_300_572_561_805.jpg)
![](./images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-34_307_606_552_1454.jpg)

Right margin note (page 34)

on, we
ansion
$n x \mid$
$x$
$2 \pi$
$\mathrm{n} x \mid$.
series
cosine
(Use partial
$$
x \leq \frac{\pi}{2} .
$$
interval
$$
\frac{\pi}{2} x .
$$
$$
e^{x}
$$

++++

purier Series

It is a remarkable fact that the cosine series and the sine series have the same on the intervals $(0,1),(2,3),(-2,-1), \ldots$.

EXAMPLE 2 Half-range expansions
Consider the function $f(x)=\sin x, 0 \leq x \leq \pi$. If we take its odd extensic get the usual sine function, $f_{2}(x)=\sin x$ for all $x$. Thus, the sine series $\exp$ is just $\sin x$.
$=\sin x, 0 \leq x \leq \pi$.

(b) Odd extension of $f, \sin x$.

(c) Even extension of $f, \mid$ si

If we take the even extension of $f$, we get the function $|\sin x|$. The Fourier of this even function can be obtained from Exercise 7, Section 7.2. Thus the series (of $\sin x$ ) is
$$
\sin x=\frac{2}{\pi}-\frac{4}{\pi} \sum_{k=1}^{\infty} \frac{1}{(2 k)^{2}-1} \cos 2 k x, \quad 0 \leq x \leq \pi
$$

Exercises 7.4
In Exercises 1-8, (a) find the half-range expansions of the given function. as much as possible series that you have encountered earlier.)
(b) To illustrate the convergence of the cosine and sine series, plot several sums of each and comment on the graphs.
1. $f(x)=1$ if $0<x<1$.
2. $f(x)=\pi-x$ if $0 \leq x \leq \pi$.
3. $f(x)=x^{2}$ if $0<x<1$.
4.
$$
f(x)=\left\{\begin{array}{ll}
0 & \text { if } 0 \leq x<1, \\
x-1 & \text { if } 1 \leq x<2 .
\end{array}\right.
$$
5.
$$
f(x)=\left\{\begin{array}{ll}
1 & \text { if } a<x<b, \\
0 & \text { if } 0<x<a \\
& \text { or } b<x<p,
\end{array}\right.
$$
where $0<a<b<p<\infty$. For (b), take $p=1, a=\frac{1}{4}, b=\frac{1}{2}$.
6. $f(x)=\cos x$ if $0<x<\pi$.
7. $f(x)=\cos x$ if $0 \leq$
8. $f(x)=x \sin x$ if $0<x<\pi$.

In Exercises 9-16, find the sine series expansion of the given function on the $0<x<1$.
9. $x(1-x)$.
10. $1-x^{2}$.
11. $\sin \pi x$.
12. $\sin$
13. $\sin \pi x \cos \pi x$.
14. $(1+\cos \pi x) \sin \pi x$.
15. $e^{x}$.
16. $1-$

---

<!-- Page 35 -->

Left margin note (page 35)

![](./images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-35_415_469_181_65.jpg)

Figure 4 for Exercise 1
7.5 Complex

THEORE COMPLEX FORM FOURIER SER

++++

Section 7.5 Complex Form of Fourier Series
491
17. Triangular function. Let $f(x)$ denote the shape of a plucked string of length $p$ with endpoints fastened at $x=0$ and $x=p$, as shown in Figure 4.
(a) Using the data in the figure, derive the formula
$$
f(x)=\left\{\begin{array}{ll}
\frac{h}{a} x & \text { if } 0 \leq x \leq a, \\
\frac{h}{a-p}(x-p) & \text { if } a \leq x \leq p .
\end{array}\right.
$$
(b) Obtain the sine series representation of $f$ :
7.
$$
f(x)=\frac{2 h p^{2}}{a(-a+p) \pi^{2}} \sum_{n=1}^{\infty} \frac{\sin \frac{a n \pi}{p}}{n^{2}} \sin \frac{n \pi}{p} x .
$$
(c) Verify this representation by taking $a=1 / 3, p=1, h=1 / 10$ and plotting the resulting function $f$ along with several partial sums of the Fourier series.
Form of Fourier Series
In previous sections, we have used the formulas
$$
\cos u=\frac{e^{i u}+e^{-i u}}{2} \quad \text { and } \quad \sin u=\frac{e^{i u}-e^{-i u}}{2 i}
$$
several times with tools from complex analysis to compute Fourier series. In this section, we will consider a Fourier series
$$
f(x)=a_{0}+\sum_{n=1}^{\infty}\left(a_{n} \cos \frac{n \pi}{p} x+b_{n} \sin \frac{n \pi}{p} x\right),
$$
and then, using (2), we will replace the cosine and sine by their expressions in terms of the complex exponential and derive the complex form of the Fourier series, which is expressed as follows.

M 1

Let $f$ be a $2 p$-periodic piecewise smooth function. The complex form of

OF the Fourier series of $f$ is

IES
$$
\sum_{n=-\infty}^{\infty} c_{n} e^{i \frac{n \pi}{p} x}
$$
where the Fourier coefficients $c_{n}$ are given by
$$
c_{n}=\frac{1}{2 p} \int_{-p}^{p} f(t) e^{-i \frac{n \pi}{p} t} d t \quad(n=0, \pm 1, \pm 2, \ldots)
$$

For all $x$, the Fourier series converges to $f(x)$ if $f$ is continuous at $x$, and to $\frac{f(x+)+f(x-)}{2}$ otherwise. Moreover, the Fourier series converges to $f(x)$ uniformly for all $x$ if and only if $f$ is continuous for all $x$ (and piecewise smooth).

---

<!-- Page 36 -->

Left margin note (page 36)

492
Chapter 7 For

Right margin note (page 36)

of
will
sing
imilar
$-i \frac{n \pi}{p} x$.
that

++++

trier Series

The Fourier coefficients $c_{n}$ are also denoted by $\widehat{f}(n)$. The $N$ th partial s of (3) is by definition the symmetric sum
$$
S_{N}(x)=\sum_{n=-N}^{N} c_{n} e^{i \frac{n \pi}{p} x}
$$

We will see in a moment that $S_{N}(x)$ is the same as the usual partial sum the Fourier series
$$
s_{N}(x)=a_{0}+\sum_{n=1}^{N}\left(a_{n} \cos \frac{n \pi}{p} x+b_{n} \sin \frac{n \pi}{p} x\right)
$$

Proof of Theorem 1 It is enough to show that $S_{N}=s_{N}$, then the theorem follow from Theorem 1, Section 7.3. We clearly have $c_{0}=a_{0}$. For $n>0, \mathbf{u}$ (1), we get
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

To simplify the middle integral, we used the identity $e^{-i \theta}=\cos \theta-i \sin \theta$. A s argument shows that $c_{-n}=\frac{1}{2}\left(a_{n}+i b_{n}\right)$. Thus, for $n \geq 1$,
$$
a_{n} \cos \frac{n \pi}{p} x+b_{n} \sin \frac{n \pi}{p} x=c_{n} e^{i \frac{n \pi}{p} x}+c_{-n} e^{-i \frac{n \pi}{p} x}
$$
and so
$$
s_{N}(x)=a_{0}+\sum_{n=1}^{N}\left(a_{n} \cos \frac{n \pi}{p} x+b_{n} \sin \frac{n \pi}{p} x\right)=c_{0}+\sum_{n=1}^{N} c_{n} e^{i \frac{n \pi}{p} x}+\sum_{n=1}^{N} c_{-n} e
$$

Changing $n$ to $-n$ in the second series on the right and combining, we g $s_{N}(x)=S_{N}(x)$, and the theorem follows.

---

<!-- Page 37 -->

Left margin note (page 37)

![](./images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-37_483_491_1353_60.jpg)

Figure $1 \mathrm{~A} 2 \pi$-periodic function, $e^{a x}, a>0,-\pi<x<$

++++

Section 7.5 Complex Form of Fourier Series

We can extract the following useful identities from the previous proc
$$
\begin{array}{c}
c_{n}=\frac{1}{2}\left(a_{n}-i b_{n}\right), \quad c_{-n}=\frac{1}{2}\left(a_{n}+i b_{n}\right) \quad(n>0) \\
a_{n}=c_{n}+c_{-n}, \quad b_{n}=i\left(c_{n}-c_{-n}\right) \quad(n>0) \\
S_{N}(x)=s_{N}(x)
\end{array}
$$

If $f$ is real-valued, so that $a_{n}$ and $b_{n}$ are both real, then (6) shows that is the complex conjugate of $c_{n}$. In symbols,
$$
c_{-n}=\bar{c}_{n} .
$$

This identity fails in general if $f$ is not real-valued. Consider $f(x)=$ From the orthogonality relations of the complex exponential functions (I ercise 12, Section 3.2), it follows that $c_{1}=1$ and $c_{n}=0$ for all $n \neq$ (Exercise 9). Hence, $c_{-1} \neq \bar{c}_{1}$.

The complex form of the Fourier series is particularly useful when deal with exponential functions, as we now illustrate.

EXAMPLE 1 A complex Fourier series
Find the complex form of the Fourier series of the $2 \pi$-periodic function $f(x)=$ for $-\pi<x<\pi$, where $a \neq 0, \pm i, \pm 2 i, \pm 3 i, \ldots$. Determine the values of Fourier series at $x= \pm \pi$.

Solution From (4), we have
$$
c_{n}=\frac{1}{2 \pi} \int_{-\pi}^{\pi} e^{a x} e^{-i n x} d x=\frac{1}{2 \pi}\left[\frac{e^{(a-i n) x}}{a-i n}\right]_{-\pi}^{\pi}=\frac{(-1)^{n}}{a-i n} \frac{\sinh \pi a}{\pi},
$$
where we have used $e^{ \pm i n \pi}=(-1)^{n}$ and $\sinh \pi a=\frac{e^{\pi a}-e^{-\pi a}}{2}$. Plugging th coefficients into (3) and simplifying, we obtain the complex form of the Fou series of $f$
$$
\frac{\sinh \pi a}{\pi} \sum_{n=-\infty}^{\infty} \frac{(-1)^{n}}{a-i n} e^{i n x}=\frac{\sinh \pi a}{\pi} \sum_{n=-\infty}^{\infty} \frac{(-1)^{n}}{a^{2}+n^{2}}(a+i n) e^{i n x} .
$$
(We remind you that here and throughout the section the doubly infinite Fou series represents the limit of the symmetric partial sums, $\sum_{n=-N}^{N}$.) Applying T orem 1 to $f(x)$, we obtain the Fourier series representation
$$
e^{a x}=\frac{\sinh \pi a}{\pi} \sum_{n=-\infty}^{\infty} \frac{(-1)^{n}}{a^{2}+n^{2}}(a+i n) e^{i n x} \quad(-\pi<x<\pi) .
$$

According to Theorem 1, the values of the Fourier series at the points of disc tinuity, and in particular at $x= \pm \pi$, are given by the average of the function

---

<!-- Page 38 -->

Left margin note (page 38)

494
Chapter 7 Fou

![](./images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-38_516_528_1843_81.jpg)

Figure 2 Part the Fourier series periodic function $-\pi<x<\pi$.

Right margin note (page 38)

n the
(See then
form.
apute lating m (5)
gure 2. iverges
nalysis sed in

++++

rier Series

these points. With the help of Figure 1, we see that this average is
$$
\frac{e^{a \pi}+e^{-a \pi}}{2}=\cosh a \pi .
$$

As a specific illustration, if you take $x=\pi$ in the Fourier series, you obtai interesting identity
$$
\cosh a \pi=\frac{\sinh \pi a}{\pi} \sum_{n=-\infty}^{\infty} \frac{a+i n}{a^{2}+n^{2}}, \quad a \neq 0, \pm i, \pm 2 i, \pm 3 i, \ldots .
$$

We have used $e^{i n \pi}=(-1)^{n}$ and $(-1)^{n}(-1)^{n}=1$ to simplify the series. Exercises 12 and 13 for related results.) Finally, let us note that if $a= \pm i n$, $f(x)=e^{ \pm i n x}$, and hence $f$ is its own Fourier series.

EXAMPLE 2 The (usual) Fourier series from the complex form Obtain the usual Fourier series of the function in Example 1 from its complex Take $a$ to be a real number $\neq 0$.
Solution The point here is not to use the Euler formulas of Section 7.2 to con the Fourier series. Instead, we will use Example 1 and appropriate formulas re the Fourier coefficients $a_{n}$ and $b_{n}$ to the complex Fourier coefficients $c_{n}$. Fro and (10), we obtain
$$
a_{0}=c_{0}=\frac{1}{a} \frac{\sinh \pi a}{\pi}
$$

From (7) and (10), we have
$$
a_{n}=(-1)^{n} \frac{\sinh \pi a}{\pi}\left(\frac{1}{a-i n}+\frac{1}{a+i n}\right)=(-1)^{n} \frac{\sinh \pi a}{\pi} \frac{2 a}{a^{2}+n^{2}}
$$
and
$$
b_{n}=i(-1)^{n} \frac{\sinh \pi a}{\pi}\left(\frac{1}{a-i n}-\frac{1}{a+i n}\right)=-(-1)^{n} \frac{\sinh \pi a}{\pi} \frac{2 n}{a^{2}+n^{2}} .
$$

Thus, the Fourier series of $f$ is
$$
\frac{1}{a} \frac{\sinh \pi a}{\pi}+\frac{\sinh \pi a}{\pi} \sum_{n=1}^{\infty} \frac{(-1)^{n}}{a^{2}+n^{2}}(2 a \cos n x-2 n \sin n x)
$$

In particular, for $-\pi<x<\pi$ and $a \neq 0$, we have
$$
e^{a x}=\frac{1}{a} \frac{\sinh \pi a}{\pi}+\frac{\sinh \pi a}{\pi} \sum_{n=1}^{\infty} \frac{(-1)^{n}}{a^{2}+n^{2}}(2 a \cos n x-2 n \sin n x)
$$
al sums of of the $2 \pi$ -
$$
f(x)=e^{x}
$$

We took $a=1$ and illustrated the convergence of the Fourier series in Fi Note that because the sine coefficients are of the order $1 / n$, the series cor relatively slowly like the Fourier series of the sawtooth function.

Our next example illustrates the use of methods from complex ar in computing Fourier series. The ideas are similar to those we $u$

---

<!-- Page 39 -->

Left margin note (page 39)

![](./images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-39_521_482_262_62.jpg)

Figure 3 The disk $(|a|>1)$ contains the $|z|=1$.

![](./images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-39_528_485_979_55.jpg)

Figure 4 In this figure $\operatorname{Re}\left(\frac{1}{2+e^{i \theta}}\right)=\frac{2+\cos \theta}{5+4 \cos \theta} ; s_{2}(\theta)=\frac{1}{2}\left(1-\frac{\cos \theta}{2}+\frac{c c}{2}\right.$

![](./images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-39_606_468_1781_55.jpg)

Figure 5 In this figure:
$\operatorname{lm}\left(\frac{1}{2+e^{1 / \theta}}\right)=\frac{-\sin \theta}{5+4 \cos \theta}$;
$$
8_{2}(\theta)=-\frac{1}{2}\left(\frac{\sin \theta}{2}-\frac{\sin 2 \theta}{4}\right.
$$

Right margin note (page 39)

\#
Z
5
रु०
I'v. OV. O.C.
C
풀o⿱№
ট্রু

++++

Section 7.5 Complex Form of Fourier Series

Section 7.2 and are based on the applications of Laurent series. The exar that we present leads to power series, which are special cases of Lau series.

EXAMPLE 3 Using complex power series to compute Fourier seri
Let $a$ be a real number with $|a|>1$. The complex-valued function
$$
f(\theta)=\frac{1}{a+e^{i \theta}} \quad(\theta \text { real })
$$
is $2 \pi$-periodic, and because $|a|>1$ and $\left|e^{i \theta}\right|=1$ for all $\theta$, the denominator not vanish, and so $f$ is smooth. The function $f(\theta)$ is the restriction to the circle $\left(z=e^{i \theta}\right)$ of the function $\frac{1}{a+z}$, where $z$ is the variable. Since $|a|>1$, it foll that $\frac{1}{a+z}$ is analytic in the disk $|z|<|a|$, and so it has a power series expansio $|z|<|a|$, which can be obtained from the geometric series as follows:
$$
\frac{1}{a+z}=\frac{1}{a} \frac{1}{1-\left(-\frac{z}{a}\right)}=\frac{1}{a} \sum_{n=0}^{\infty}(-1)^{n}\left(\frac{z}{a}\right)^{n} \quad(|z|<|a|) .
$$

Since the unit circle $|z|=1$ is contained in the disk $|z|<|a|$, the power se expansion is valid for all $z=e^{i \theta}$ (Figure 3). Substituting $z=e^{i \theta}$, then us $z^{n}=e^{i n \theta}$ and simplifying, we get
$$
f(\theta)=\frac{1}{a+e^{i \theta}}=\frac{1}{a} \sum_{n=0}^{\infty} \frac{(-1)^{n}}{a^{n}} e^{i n \theta},
$$
which is the complex form of the Fourier series of $f(\theta)$. Out of this expansi we can derive two interesting real Fourier series, by taking the real and imagin parts of $f(\theta)$. We have (here we will use the fact that $a$ is real)
$$
f(\theta)=\frac{1}{a+e^{i \theta}}=\frac{a+e^{-i \theta}}{\left(a+e^{i \theta}\right)\left(a+e^{-i \theta}\right)}=\frac{a+\cos \theta}{1+a^{2}+2 a \cos \theta}-\frac{i \sin \theta}{1+a^{2}+2 a \cos \theta} .
$$

Substitute this into (11), use $e^{i n \theta}=\cos n \theta+i \sin n \theta$, then equate real and imagina parts, and get the two Fourier series
$$
\frac{a+\cos \theta}{1+a^{2}+2 a \cos \theta}=\frac{1}{a}\left[1-\frac{\cos \theta}{a}+\frac{\cos 2 \theta}{a^{2}}-\frac{\cos 3 \theta}{a^{3}}+\cdots\right],
$$
and
$$
\frac{-\sin \theta}{1+a^{2}+2 a \cos \theta}=-\frac{1}{a}\left[\frac{\sin \theta}{a}-\frac{\sin 2 \theta}{a^{2}}+\frac{\sin 3 \theta}{a^{3}}+\cdots\right],
$$
which are valid for all $\theta$. In Figures 4 and 5, we plotted the real and imagina parts of $f$ in the case $a=2$, along with partial sums of their Fourier series.

The Fourier series (11) is very special, in the sense that all the $c_{n}$ 's wi $n<0$ are zero. Such a Fourier series is called analytic, because, as we sa

---

<!-- Page 40 -->

Left margin note (page 40)

496
Chapter 7
Fo

Right margin note (page 40)

Note have only )).
nvoThe
does n its erve d $x$, Its cting
with Cheo-
tegral $s$ with So, in
cation ient to $c_{n}$.

++++

urier Series

in Example 3, it is the restriction of an analytic function to the circle. that the functions $f(\theta)$ in Example 3 is complex-valued. Is it possible to a real-valued analytic Fourier series? It is not hard to show that the real-valued analytic functions are the constant functions (Exercise $10(1$
Convolution of Periodic Functions
One of the most important operations in Fourier analysis is the co lution. To define it, consider a pair of $2 p$-periodic functions $f$ and $g$. convolution of $f$ and $g$, denoted by $f * g(x)$, is defined by
$$
f * g(x)=\frac{1}{2 p} \int_{-p}^{p} f(t) g(x-t) d t
$$

From its mere definition, it is difficult to explain what the convolution to a pair of functions. In a moment, we will be able to clearly explai effect in terms of the complex Fourier coefficients. For now, let us obs that if $f$ and $g$ are piecewise continuous and $2 p$-periodic, then, for fixe the function $f(t) g(x-t)$ is also piecewise continuous and $2 p$-periodic integral can be evaluated over any interval of length $2 p$, without affe its value (Theorem 1, Section 7.1). So
$$
f * g(x)=\frac{1}{2 p} \int_{-p}^{p} f(t) g(x-t) d t=\frac{1}{2 p} \int_{a}^{a+2 p} f(t) g(x-t) d t
$$
where $a$ is an arbitrary real number. Also, if $f$ and $g$ are continuous continuous derivatives, we can differentiate under the integral sign ( rem 5 , Section 3.5 ) and conclude that
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

If $f$ and $g$ are merely piecewise smooth, we can write the convolution in as a sum of integrals over intervals on which $f$ and $g$ are continuou continuous derivatives, and then differentiate under the integral sign. general, the convolution is piecewise smooth.

Convolutions are important because they correspond to multipli of the Fourier coefficients. To express this property, it will be conven use the notation $\widehat{f}(n)$ for the complex Fourier coefficients instead of

---

<!-- Page 41 -->

Left margin note (page 41)

THEORE
FOUR
COEFFICIENTS
CONVOLUTI

COROLLAR CONTINUITY CONVOLUTIO

COROLLARY

++++

Section 7.5 Complex Form of Fourier Series
497
M 2
IER
OF
ONS

Let $f$ and $g$ be $2 p$-periodic, piecewise smooth functions. Then
$$
\widehat{f * g}(n)=\widehat{f}(n) \widehat{g}(n) \quad n=0, \pm 1, \pm 2, \ldots
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
Y 1
OF
NS

Let $f$ and $g$ be $2 p$-periodic, piecewise smooth functions. Then $f * g$ is continuous and piecewise smooth.

Proof We have already showed that $f * g$ is piecewise smooth with derivative given by (14) at all but finitely many points in $[-p, p]$. To show that it is continuous, we note that if $|f|$ and $\left|f^{\prime}\right|$ are bounded, say by $M$, then $|\widehat{f}(n)| \leq \frac{4 M}{n}$, which follows by integrating by parts in (4). The details are left as an exercise. So $|\widehat{f * g}(n)|=|\widehat{f}(n)||\widehat{g}(n)| \leq A \frac{1}{n} \frac{1}{n}=\frac{A}{n^{2}}$, where $A$ is a constant. We now apply the Weierstrass $M$-test to the Fourier series of $f * g(x)$, which is $\sum_{-\infty}^{\infty} \widehat{f}(n) \widehat{g}(n) e^{i \frac{n \pi}{p}}$, and conclude that the series converges uniformly for all $x$, implying that $f * g(x)$ is continuous, by Theorem 1.

The next result states that convolution is commutative. It can be checked directly by using the definition of convolution. We give a different proof based on Theorem 2.

2

Let $f$ and $g$ be piecewise smooth $2 p$-periodic functions. Then $f * g(x)= g * f(x)$.

Proof The functions $f * g$ and $g * f$ are piecewise smooth and continuous. Moreover,

---

<!-- Page 42 -->

Left margin note (page 42)

498
Chapter 7 For

COROLI
PARSI
IDE

![](./images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-42_430_535_1821_94.jpg)

Figure 6 Sawte in Example 4 ha series $\sum_{n=1}^{\infty} \frac{\sin n}{n}$

Right margin note (page 42)

to the
□
p]. Let
mplex
on, we
since econd ourier
ng dints of ourier
ned on
ourier cients, $\left.i b_{n}\right)=$

++++

trier Series

they have the same Fourier coefficients, because
$$
\widehat{f * g}(n)=\hat{f}(n) \hat{g}(n)=\hat{g}(n) \hat{f}(n)=\widehat{g * f}(n) .
$$

Since the Fourier series are the same and converge (uniformly) everywhere functions, we conclude that $f * g=g * f$.
ARY 3
EVAL'S
NTITY

Let $f$ be a real-valued $2 p$-periodic piecewise smooth function on $[-p, 1 a_{n}, b_{n}$, and $c_{n}$ denote, respectively, the cosine, the sine, and the co Fourier coefficients of $f$. Then
$$
\frac{1}{2 p} \int_{-p}^{p} f(x)^{2} d x=\sum_{n=-\infty}^{\infty}\left|c_{n}\right|^{2}=a_{0}^{2}+\sum_{n=1}^{\infty}\left(a_{n}^{2}+b_{n}^{2}\right)
$$

Proof Let $g(t)=f(-t)$. Then
$$
\begin{aligned}
\hat{g}(n) & =\frac{1}{2 p} \int_{-p}^{p} f(-t) e^{-i \frac{n \pi}{p} t} d t=\frac{1}{2 p} \int_{-p}^{p} f(t) e^{i \frac{n \pi}{p} t} d t \\
& =\frac{1}{2 p} \int_{-p}^{p} f(t) e^{-i \frac{(-n) \pi}{p} t} d t=c_{-n}=\overline{c_{n}}
\end{aligned}
$$
where the last equality follows from (9). From the Fourier series representatic have
$$
\begin{aligned}
f * g(x) & =\sum_{n=-\infty}^{\infty} \hat{f}(n) \hat{g}(n) e^{i \frac{n \pi}{p} x} \\
& =\sum_{n=-\infty}^{\infty} c_{n} c_{-n} e^{i \frac{n \pi}{p} x}=\sum_{n=-\infty}^{\infty}\left|c_{n}\right|^{2} e^{i \frac{n \pi}{p} x}
\end{aligned}
$$

Evaluating both sides at $x=0$, we obtain the first of the Parseval's identities $f * g(0)=\frac{1}{2 p} \int_{-p}^{p} f(t) g(-t) d t=\frac{1}{2 p} \int_{-p}^{p} f(t) f(t) d t=\frac{1}{2 p} \int_{-p}^{p} f^{2}(t) d t$. The $s$ identity follows from the first one by using the relationships between the $\mathbf{F}$ coefficients (5)-(7). The details are left as an exercise.

In the following example of a convolution, we will avoid computi rectly from the definition. Instead we will compute the Fourier coefficie the convolution and then identify the convolution function from its $F$ coefficients.

EXAMPLE 4 Computing convolutions

function

Find $f * f(x)$, where $f(x)$ denotes the $2 \pi$-periodic sawtooth function, defin $(0,2 \pi)$ by $f(x)=\frac{1}{2}(\pi-x)$ (Figure 6).
Solution Let us first compute $c_{n}=\widehat{f}(n)$. We can use the definition of the F coefficients or, better yet, since we know the Fourier cosine and sine coeffi $a_{n}=0$ and $b_{n}=\frac{1}{n}$, we can compute $c_{n}$ by using (6). We have $c_{n}=\frac{1}{2}\left(a_{n}-\right.$

---

<!-- Page 43 -->

Left margin note (page 43)

![](./images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-43_389_446_565_53.jpg)

Figure 7 The convoluti the sawtooth function itself is a continuous func given on $[0,2 \pi]$ by
$$
\frac{1}{8}\left(\frac{\pi^{2}}{3}-(x-\pi)^{2}\right)
$$

THEOREM

++++

Section 7.5 Complex Form of Fourier Series
499

$-\frac{i}{2 n}$. From this and Theorem 2, we conclude that $\widehat{f * f}(n)=\left(-\frac{i}{2 n}\right)^{2}=-\frac{1}{4 n^{2}}$. Computing the cosine and sine Fourier coefficients of $f * f$ from (7), we find that the Fourier sine coefficients are 0 , while the Fourier cosine coefficients are $-\frac{1}{2 n^{2}}$. We now ask: Which function has these Fourier coefficients? Consider the function from Exercise 9, Section 7.2. Call this function $h$. Replace $x$ by $x-\pi$ in the Fourier series and get
$$
h(x-\pi)=\frac{\pi^{2}}{3}+4 \sum_{n=1}^{\infty} \frac{(-1)^{n}}{n^{2}} \cos n(x-\pi)=\frac{\pi^{2}}{3}+4 \sum_{n=1}^{\infty} \frac{1}{n^{2}} \cos n x,
$$
where we have used $\cos n(x-\pi)=(-1)^{n} \cos n x$. Subtract $\frac{\pi^{2}}{3}$ and divide by -8 to get
$$
-\frac{1}{8}\left(h(x-\pi)-\frac{\pi^{2}}{3}\right)=-\frac{1}{2} \sum_{n=1}^{\infty} \frac{1}{n^{2}} \cos n x,
$$
which is the desired function. Since this function has the same Fourier coefficients as $f * f(x)$, it is thus equal to $f * f(x)$. Using the formula for $h$, we find that on the interval $(0,2 \pi)$
$$
f * f(x)=-\frac{1}{8}\left((x-\pi)^{2}-\frac{\pi^{2}}{3}\right)=\frac{1}{8}\left(\frac{\pi^{2}}{3}-(x-\pi)^{2}\right)
$$

The graph of $f * f$ is shown in Figure 7. It is continuous and piecewise smooth, even though $f$ is not continuous for all $x$.

The final result of this section is an interesting application of Parseval's identity, which implies that the Fourier series of a continuous piecewise smooth function is uniformly and absolutely convergent. We stated this result in Theorem 2, Section 7.2, and proved it under the further assumption that $f^{\prime}$ is piecewise smooth.

43

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

---

<!-- Page 44 -->

Left margin note (page 44)

500
Chapter 7

Right margin note (page 44)

riodic
1.]
.]
e 1.]
e 1.]
nd (7)
(Exerourier

What
the
).]
ise 1 to

++++

Fourier Series
$$
\sum_{n=1}^{\infty}\left|a_{n}\right| \leq\left(\sum_{n=1}^{\infty}\left|b_{n}^{\prime}\right|^{2}\right)^{\frac{1}{2}}\left(\sum_{n=1}^{\infty} \frac{1}{n^{2}}\right)^{\frac{1}{2}}<\infty
$$

Exercises 7.5
In Exercises 1-6, find the complex form of the Fourier series of the given $2 \pi-p \epsilon$ function.
1. $f(x)=\cosh a x$ if $-\pi<x<\pi(a \neq 0, \pm i, \pm 2 i, \pm 3 i, \ldots)$.
[Hint: Example
2. $f(x)=\sinh a x$ if $-\pi<x<\pi(a \neq 0, \pm i, \pm 2 i, \pm 3 i, \ldots)$.
[Hint: Example
3. $f(x)=\cos a x$ if $-\pi<x<\pi$ ( $a$ is not an integer). [Hint:
(1) and Exampl
4. $f(x)=\sin a x$ if $-\pi<x<\pi$ ( $a$ is not an integer). [Hint:
(1) and Exampl
5. $f(x)=\cos 2 x+2 \cos 3 x$. [Hint: Use (1).]
6. $f(x)=\sin 3 x$. [Hint: Use (1).]

In Exercises 7-8, find the Fourier series of the given function by using (5) or by manipulating the complex form of the Fourier series.
7. $f(x)$ is as in Exercise 3.
8. $f(x)$ is as in Exercise 4.
9. (a) Use the orthogonality relations of the complex exponential system cise 12 , Section 3.2 ) to show that the $2 \pi$-periodic function $e^{i n x}$ is its own series.
(b) Let $m \leq n$ be arbitrary integers and $c_{k}$ be arbitrary complex numbers. is the Fourier series of the $2 \pi$-periodic function $f(x)=\sum_{k=m}^{n} c_{k} e^{i k x}$ ?
10. (a) Derive (7) from (6).
(b) Show that if $f$ is real-valued, $2 p$-periodic, and piecewise smooth, and Fourier coefficients $c_{n}$ with $n<0$ are zero, then $f$ is constant. [Hint: Use ( 9
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
13. (a) Let $a \neq 0$ be a real number. Use Parseval's identity and Exerc derive the identity
$$
\sum_{n=-\infty}^{\infty} \frac{1}{\left(a^{2}+n^{2}\right)^{2}}=\frac{\pi}{2 a^{2} \sinh ^{2}(\pi a)}\left[\pi+\frac{\sinh (2 \pi a)}{2 a}\right]
$$
(b) With the help of Exercise 2, derive the identity
$$
\sum_{n=-\infty}^{\infty} \frac{n^{2}}{\left(a^{2}+n^{2}\right)^{2}}=\frac{\pi}{2 \sinh ^{2}(\pi a)}\left[\frac{\sinh (2 \pi a)}{2 a}-\pi\right]
$$

---

<!-- Page 45 -->

Right margin note (page 45)

K

++++

Section 7.5 Complex Form of Fourier Series
501
14. (a) Use Parseval's identity and the Fourier series expansion $\frac{x}{2}=\sum_{n=1}^{\infty} \frac{(-1)^{n+1}}{n} \sin n x$ for $-\pi<x<\pi$, to obtain $\sum_{n=1}^{\infty} \frac{1}{n^{2}}=\frac{\pi^{2}}{6}$.
(b) From (a), obtain that $\sum_{k=1}^{\infty} \frac{1}{(2 k)^{2}}=\frac{\pi^{2}}{24}$.
(c) Combine (a) and (b) to derive the identity $\sum_{k=0}^{\infty} \frac{1}{(2 k+1)^{2}}=\frac{\pi^{2}}{8}$.

In Exercises 15-16, find the Fourier series of the given function using Taylor or Laurent series expansions.
15. $f(\theta)=\frac{e^{\prime \theta}}{2+e^{2 \pi \theta}}$.
16. $f(\theta)=\frac{1}{3+e^{1 \theta}+e^{-1 \theta}}$.
17. $f(\theta)=e^{e^{i \theta}}$.
18. $f(\theta)=\cos \left(e^{i \theta}\right)$.
19. Which real Fourier series do you get by taking real and imaginary parts in the Fourier series of Exercise 15?
20. (a) Which real Fourier series do you get by taking real and imaginary parts in the Fourier series of Exercise 17?
(b) Answer (a) with the Fourier series of Exercise 18.

In Exercises 21-24, you are given two $2 \pi$-periodic functions $f$ and $g$ on an interva of length $2 \pi$. (a) Compute the Fourier coefficients of $f * g$. (b) Find $f * g$ by matchin (b) its Fourier coefficients with those of a known function (as we did in Example 4).
21. For $-\pi<x<\pi, f(x)=g(x)=x$.
22. For $-\pi<x<\pi, f(x)=x$; and $g(x)=-1$ if $-\pi<x<0$ and $g(x)=1 0<x<\pi$.
23. For $-\pi<x<\pi, f(x)=e^{i x}+e^{-i x}$, and $g(x)$ is an arbitrary piecewise smoot function.
24. For $-\pi<x<\pi, f(x)=\sum_{n=-N}^{N} e^{-i n x}$, and $g(x)$ is an arbitrary piecewis smooth function.
Project Problem: Cotangent expansion, Bernoulli numbers, and Fourie series. In Exercises 25-27, we explore a connection between Fourier series and som important complex series expansions, and derive interesting identities.
25. Consider the $2 \pi$-periodic function of Example 2, which is defined on the in terval $(-\pi, \pi)$ by $f(x)=e^{a x}$, where $a \neq 0$ is an arbitrary real number.
(a) Evaluate the Fourier series in Example 2 at $x=\pi$ and obtain for $a \neq 0$
$$
\cosh a \pi=\frac{\sinh a \pi}{a \pi}+\frac{\sinh a \pi}{\pi} \sum_{n=1}^{\infty} \frac{2 a}{a^{2}+n^{2}} .
$$
[Hint: See Example 1.]
(b) Conclude that for any real number $a \neq 0$,
$$
a \pi \operatorname{coth} a \pi=1+\sum_{n=1}^{\infty} \frac{2 a^{2}}{a^{2}+n^{2}}
$$
26. Euler's expansion of the cotangent. Let $\Omega$ consists of the entire comple plane minus the points $z \neq \pm i, \pm 2 i, \ldots$. For $z$ in $\Omega$, consider
$$
\phi(z)=1+\sum_{n=1}^{\infty} \frac{2 z^{2}}{z^{2}+n^{2}}
$$

---

<!-- Page 46 -->

Left margin note (page 46)

502
Chapter 7
F

Right margin note (page 46)

ic in and ded.

$+1$
on $A$
ciple
the
show
clude
lerive

++++

purier Series
(a) Complete the details of the following argument showing that $\phi$ is analyt $\Omega$. It is enough to show that the series converges uniformly on every closed bounded subset of $\Omega$ (Corollary 2, Section 4.2). Let $A \subset \Omega$ be closed and boun Let $M>0$ be an integer such that $|z|<M$ for all $z$ in $A$. Then for all $n>M$ and all $z$ in $A$, we have $\left|\frac{2 z 2}{z^{2}+n^{2}}\right| \leq \frac{2 M^{2}}{n^{2}-M^{2}}$. So the series converges uniformly by the Weierstrass $M$-test, since $\sum_{n=M+1}^{\infty} \frac{2 M^{2}}{n^{2}-M^{2}}<\infty$.
(b) Show that the function $\psi(z)=\pi z \operatorname{coth}(\pi z)$ is analytic for all $z \neq \pm i, \pm 2 i$,
(c) By Exercise 25(b), $\phi(z)=\psi(z)$ for all real $z \neq 0$. Using the identity prin (Section 4.6), conclude that $\phi(z)=\psi(z)$ for all $z$ in $\Omega$. Hence
$$
\pi z \operatorname{coth}(\pi z)=1+\sum_{n=1}^{\infty} \frac{2 z^{2}}{z^{2}+n^{2}} \quad(z \neq \pm i, \pm 2 i, \ldots)
$$
(d) Replace $z$ by $i z$ in (c) and obtain Euler's expansion of the cotangent
$$
\pi z \cot (\pi z)=1+\sum_{n=1}^{\infty} \frac{2 z^{2}}{z^{2}-n^{2}} \quad(z \neq \pm, \pm 2, \ldots)
$$
27. Bernoulli numbers. (a) Using Exercise 26(d) and the expansion cotangent from Exercise 31, Section 4.4, obtain
$$
\sum_{n=1}^{\infty} \frac{2 z^{2}}{z^{2}-n^{2}}=\sum_{n=1}^{\infty}(-1)^{n} \frac{2^{2 n} B_{2 n} \pi^{2 n}}{(2 n)!} z^{2 n}, \quad|z|<1,
$$
where $B_{2 n}$ are the Bernoulli numbers (see Example 4, Section 4.4).
(b) Use the Weierstrass double series theorem (Exercise 39, Section 4.4) to that for $|z|<1$,
$$
\sum_{n=1}^{\infty} \frac{2 z^{2}}{z^{2}-n^{2}}=\sum_{n=1}^{\infty}\left(\sum_{k=1}^{\infty} \frac{-2}{k^{2 n}}\right) z^{2 n}
$$
[Hint: For each $n=1,2, \ldots$, expand $\frac{2 z^{2}}{z^{2}-n^{2}}=-2 \sum_{k=1}^{\infty}\left(\frac{z}{n}\right)^{2 k},|z|<1$.]
(c) Equating the coefficients in the power series expansions in (a) and (b), con that for $n=1,2, \ldots$,
$$
\sum_{k=1}^{\infty} \frac{1}{k^{2 n}}=(-1)^{n-1} \frac{2^{2 n-1} B_{2 n} \pi^{2 n}}{(2 n)!}
$$
(d) Using the values of the Bernoulli numbers from Table 1, Section 4.4, the entries in Table 1, which follows.

\begin{table}
| $n$ | 1 | 2 | 3 | 4 | 5 | 6 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $\sum_{k=1}^{\infty} \frac{1}{k^{2 n}}$ | $\frac{\pi^{2}}{6}$ | $\frac{\pi^{4}}{90}$ | $\frac{\pi^{6}}{945}$ | $\frac{\pi^{8}}{9450}$ | $\frac{\pi^{10}}{93555}$ | $\frac{691 \pi^{12}}{638512875}$ |
\captionsetup{labelformat=empty}
\caption{Table 1. Sums of reciprocals of even powers of integers.}
\end{table}

---

<!-- Page 47 -->

Left margin note (page 47)

7.6 Proof of th

![](./images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-47_506_437_592_45.jpg)

Figure 1 The $N$ th Dir let kernel, $D_{N}(\theta)$, for $N$ 1,2,5. We have $D_{N}(0) 2 \mathrm{~N}+1$.

LEMMA
DIRICHLET KERNE
ANI
FOURIER SERIE

++++

Section 7.6 Proof of the Fourier Representation Theorem
503

Fourier Representation Theorem
In this section, we prove Theorem 1, Section 7.2. The proof that we present is based on three preliminary results that are interesting in their own right. We start with the first one, which is an integral representation of the partial sums of Fourier series involving the Dirichlet kernel (see Exercise 40, Section 1.5).

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
1+2 \sum_{n=1}^{N} \cos n(x-t)=\frac{\sin \left[\left(N+\frac{1}{2}\right)(x-t)\right]}{\sin \frac{x-t}{2}}=D_{N}(x-t)
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

---

<!-- Page 48 -->

Left margin note (page 48)

504
Chapter 7

![](./images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-48_335_495_134_122.jpg)

Figure 2 The ft piecewise linear nuities are the of $f(x)$. They der to cancel ities of $f(x)$ by

LINEAR CC

RIEMAN

![](./images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-48_318_497_495_132.jpg)

Right margin note (page 48)

$T$,
unction
eriodic greatly oecause iformly tinuous handled lescribe
here is a $\boldsymbol{\pi}]$, such $x$.
enough at most $x_{n}=\pi$. $\left.{ }_{+1}-\right)= x=x_{j}$, Hence
ntinuous
$$
d x=0 .
$$
ows simiar. Using

++++

Fourier Series
c)
netion $h(x)$ is Its discontisame as those are built in orhe discontinuadding $-h(x)$.

LEMMA 2 RRECTION

LEMMA 3 N-LEBESGUE LEMMA
of variables $T=x-t, d T=-d t$. Then
$$
\begin{aligned}
s_{N}(x) & =\frac{1}{2 \pi} \int_{-\pi}^{\pi} f(t) D_{N}(x-t) d t=-\frac{1}{2 \pi} \int_{x+\pi}^{x-\pi} f(x-T) D_{N}(T) d T \\
& =\frac{1}{2 \pi} \int_{x-\pi}^{x+\pi} f(x-T) D_{N}(T) d T=\frac{1}{2 \pi} \int_{-\pi}^{\pi} f(x-T) D_{N}(T) d
\end{aligned}
$$
where the last equality follows because we are integrating a $2 \pi$-periodic f over an interval of length $2 \pi$ (Theorem 1, Section 7.1).

In what follows we will be concerned with piecewise continuous $2 \pi$ functions, which may be considered as functions on $[-\pi, \pi]$. The proofs are simplified if we assume further that the functions are continuous on $[-\pi, \pi]$; functions that are continuous on closed and bounded intervals are in fact un continuous. To reduce a proof from a piecewise continuous function to a con function, we can add a piecewise linear correction term, which can be separately. This useful process will be clarified in the proofs; for now let us our linear correction term.
Suppose that $f$ is a $2 \pi$-periodic piecewise continuous function. Then $\mathbf{t}$ ] piecewise linear function $h(x)$ with finitely many discontinuities in $[-\pi$, that the function $g(x)=f(x)-h(x)$ is $2 \pi$-periodic and continuous for all
Proof The construction of $h$ is best described by a figure (see Figure 2). It is to define $h$ on the interval $[-\pi, \pi]$. Since $f$ is piecewise continuous, it has a finite number of discontinuities in $[-\pi, \pi]$, say, $-\pi=x_{0}<x_{1}<\cdots<$ Define $h(x)$ on each subinterval $\left(x_{j}, x_{j+1}\right)$ by $h\left(x_{j}+\right)=f\left(x_{j}+\right)$ and $h\left(x_{j}\right. f\left(x_{j+1}-\right)$. Then $g(x)=f(x)-h(x)$ is clearly continuous for all $x \neq x_{j}$. For we have $g\left(x_{j}+\right)=f\left(x_{j}+\right)-h\left(x_{j}+\right)=0$ and $g\left(x_{j}-\right)=f\left(x_{j}-\right)-h\left(x_{j}-\right)=0 g$ is also continuous at $x_{j}$ and so $g$ is continuous for all $x$.

Our next result states that the Fourier coefficients of a piecewise co function tend to 0 as $n \rightarrow \infty$.
Suppose that $f$ is a $2 \pi$-periodic piecewise continuous function. Then
(2) $\lim _{n \rightarrow \infty} \int_{-\pi}^{\pi} f(x) \cos n x d x=0$ and $\lim _{n \rightarrow \infty} \int_{-\pi}^{\pi} f(x) \sin n x d x=0$.

More generally, if $\alpha$ is any fixed real number, then
(3)
$$
\lim _{n \rightarrow \infty} \int_{-\pi}^{\pi} f(x) \cos [(n+\alpha) x] d x=0 \text { and } \lim _{n \rightarrow \infty} \int_{-\pi}^{\pi} f(x) \sin [(n+\alpha) x]
$$

Proof We will only establish the first limit in (2); the second one foll larly. We start by verifying the limit for functions that are piecewise line

---

<!-- Page 49 -->

Right margin note (page 49)

505

0,
rals the e if om the
are
in
n-
in
0,
se
n-
+
).

++++

Section 7.6 Proof of the Fourier Representation Theorem

integration by parts, we have
$$
\begin{aligned}
\int_{a}^{b}(c x+d) \cos n x d x & =\left.(c x+d) \frac{\sin n x}{n}\right|_{a} ^{b}-c \int_{a}^{b} \frac{\sin n x}{n} d x \\
& =\frac{(c b+d) \sin n b-(c a+d) \sin n a}{n}+c \frac{\cos n b-\cos n a}{n^{2}}
\end{aligned}
$$
as $n \rightarrow \infty$. If $f$ is piecewise linear, the first integral in (2) is a finite sum of integ of the form $\int_{a}^{b}(c x+d) \cos n x d x$, each of which tends to 0 as $n \rightarrow \infty$, and so integral itself tends to 0 as $n \rightarrow \infty$. This shows that the first limit in (2) is tru $f$ is piecewise linear. Next we consider the case of a continuous function $f$. Fr the identity $\cos a=-\cos (a+\pi)$, we get $\cos n x=-\cos \left(n\left(x+\frac{\pi}{n}\right)\right)$. Using substitution $X=x+\frac{\pi}{n}$, we have
$$
\begin{aligned}
\int_{-\pi}^{\pi} f(x) \cos n x d x & =-\int_{-\pi}^{\pi} f(x) \cos \left(n\left(x+\frac{\pi}{n}\right)\right) d x \\
& =-\int_{-\pi+\frac{\pi}{n}}^{\pi+\frac{\pi}{n}} f\left(x-\frac{\pi}{n}\right) \cos n x d x \\
& =-\int_{-\pi}^{\pi} f\left(x-\frac{\pi}{n}\right) \cos n x d x
\end{aligned}
$$
where the last equality follows from Theorem 1, Section 7.1, since all functions $2 \pi$-periodic. So
$$
2 \int_{-\pi}^{\pi} f(x) \cos n x d x=\int_{-\pi}^{\pi}\left(f(x)-f\left(x-\frac{\pi}{n}\right)\right) \cos n x d x
$$
and hence by the inequality for integrals,
$$
\left|\int_{-\pi}^{\pi} f(x) \cos n x d x\right| \leq \frac{1}{2}\left|\int_{-\pi}^{\pi}\left(f(x)-f\left(x-\frac{\pi}{n}\right)\right) \cos n x d x\right| \leq \frac{1}{2}(2 \pi) M_{n}
$$
where $M_{n}=\max \left|\left(f(x)-f\left(x-\frac{\pi}{n}\right)\right) \cos n x\right|=\max \left|f(x)-f\left(x-\frac{\pi}{n}\right)\right|$ for $x [-\pi, \pi]$. Since $f$ is continuous on the closed interval $[-\pi, \pi]$, it is uniformly $\operatorname{co}$ tinuous; hence the difference $\left|f(x)-f\left(x-\frac{\pi}{n}\right)\right|$ tends to 0 uniformly for all $x [-\pi, \pi]$, as $\frac{\pi}{n} \rightarrow 0$. So as $n \rightarrow \infty, M_{n} \rightarrow 0$, implying that $\left|\int_{-\pi}^{\pi} f(x) \cos n x d x\right| \rightarrow$ and thus completing the proof in the case $f$ is continuous. Finally, if $f$ is piecewi continuous, we apply Lemma 2 and write $f(x)=g(x)+h(x)$, where $g$ is co tinuous and $h$ is piecewise linear. Then $\int_{-\pi}^{\pi} f(x) \cos n x d x=\int_{-\pi}^{\pi} g(x) \cos n x d x \int_{-\pi}^{\pi} h(x) \cos n x d x \rightarrow 0$ as $n \rightarrow \infty$, by the previous two cases.

To prove (3), use the addition formula for the sine and cosine and apply (2 For example, using $\cos [(n+\alpha) x]=\cos (n x) \cos (\alpha x)-\sin (n x) \sin (\alpha x)$, we get
$$
\begin{array}{l}
\int_{-\pi}^{\pi} f(x) \cos [(n+\alpha) x] d x \\
=\int_{-\pi}^{\pi}[f(x) \cos (\alpha x)] \cos n x d x-\int_{-\pi}^{\pi}[f(x) \sin (\alpha x)] \sin n x d x
\end{array}
$$

---

<!-- Page 50 -->

Left margin note (page 50)

506
Chapter 7

![](./images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-50_651_490_1249_130.jpg)

Figure 3 The pi function $h(x)$ he to $f^{\prime}\left(x_{0}-\right)$ to t and $f^{\prime}\left(x_{0}+\right)$ to $x_{0}$. The discon derivative and it tinuity at $x_{0}$ are cel those of $f$ an to make $f$ and $($ and $=0)$ at $x_{0}$.

Right margin note (page 50)

at both
orem 1, $f^{\prime}$ may s and is e $f^{\prime}(x)$ , as we s exist.
follows or fixed $2 f^{\prime}(x)$. $=g(0)$, function e entire see that $s_{N}(x)-$
nuous in out loss of length $x)-h(x)$ (x) may Jsing the ad $x_{0}$ by $f^{\prime}\left(x_{0}-\right)$,

++++

ourier Series

Applying (2) to the functions $f(x) \cos (\alpha x)$ and $f(x) \sin (\alpha x)$, it follows th terms on the right of the displayed equation tend to 0 as $n \rightarrow \infty$.

We are now ready to prove the Fourier representation theorem (The Section 7.2). By assumption, $f$ and $f^{\prime}$ are piecewise continuous. Thus, have at most a finite number of discontinuities in $[-\pi, \pi]$, otherwise it exist continuous. We will prove that $s_{N}(x)$ converges to $f(x)$ at all points $x$ whe exists. At the points where $f^{\prime}$ does not exist, we can add a correction term did in the proof of Lemma 3, and reduce to the case of points where $f^{\prime}$ doe The details are left to the exercises.

Using the fact that $\int_{-\pi}^{\pi} \cos n t d t=0$ for all $n \geq 1$, and $\frac{1}{2 \pi} \int_{-\pi}^{\pi} d t=1$, it from (1) that
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

To show that this expression tends to 0 as $N \rightarrow \infty$, we use a clever trick. F $x$, consider the function $g(t)=\frac{f(x-t)-f(x)}{\sin \frac{t}{2}}$, for $t \neq 0$ in $[-\pi, \pi]$, and $g(0)=$ This function is clearly piecewise continuous for all $t \neq 0$, and
$$
\lim _{t \rightarrow 0} g(t)=\lim _{t \rightarrow 0} \frac{f(x-t)-f(x)}{\sin \frac{t}{2}}=\lim _{t \rightarrow 0} \frac{f(x-t)-f(x)}{t} \lim _{t \rightarrow 0} \frac{t}{\sin \frac{t}{2}}=2 f^{\prime}(x)=
$$
where we have used the fact that $f^{\prime}(x)$ exists and $\lim _{t \rightarrow 0} \frac{t}{\sin \frac{t}{2}}=2$. So the $g(t)$ is continuous at $t=0$, and hence it is piecewise continuous on th interval $[-\pi, \pi]$. Applying (3) from the Riemann-Lebesgue lemma, we $\lim _{N \rightarrow \infty} \int_{-\pi}^{\pi} g(t) \sin \left[\left(N+\frac{1}{2}\right) t\right] d t=0$, and it follows from (5) that $\lim _{N \rightarrow \infty} f(x) \mid=0$, completing the proof.
Exercises 7.6
1. The correction term. Suppose that $f$ and $f^{\prime}$ are piecewise contin $[-\pi, \pi]$ and that $f^{\prime}$ does not exist at some point $x_{0}$ in $[-\pi, \pi]$. Assume witl of generality that $x_{0}$ is in $(-\pi, \pi)$; otherwise work on a different interval $2 \pi$. Show that there is a piecewise linear function $h(x)$ such that $g(x)=f($ is piecewise continuous in $(-\pi, \pi)$ and $g^{\prime}\left(x_{0}\right)$ exists. (Note: The function $g$ not be continuous on all of $[-\pi, \pi]$, as was the case in Lemma 2.) [Hint: L fact that $f$ and $f^{\prime}$ are piecewise continuous, define the values of $h$ arou $h\left(x_{0}-\right)=f\left(x_{0}-\right), h\left(x_{0}+\right)=f\left(x_{0}+\right)$, and the slopes of lines by $h^{\prime}\left(x_{0}-\right)= h^{\prime}\left(x_{0}+\right)=f^{\prime}\left(x_{0}+\right)$. See Figure 3.]

---

<!-- Page 51 -->

Right margin note (page 51)

good

++++

Section 7.6 Proof of the Fourier Representation Theorem
(b) Obtain the equation of $h$ :
$$
h(x)=\left\{\begin{array}{ll}
f^{\prime}\left(x_{0}-\right)\left(x-x_{0}\right)+f\left(x_{0}-\right) & \text { if }-\pi<x<x_{0} \\
f^{\prime}\left(x_{0}+\right)\left(x-x_{0}\right)+f\left(x_{0}+\right) & \text { if } x_{0}<x<\pi
\end{array}\right.
$$
2. Fourier series of the correction term. We have already established t the Fourier series of a piecewise smooth function converges to the function points where the derivative exists. This shows that the Fourier series of $h$ in Exercise 1 converges to $h(x)$, except at $x=x_{0}$ and $x= \pm \pi$. In this ercise, we will evaluate the Fourier series at $x_{0}$ and show that it converges $\frac{h\left(x_{0}+\right)+h\left(x_{0}-\right)}{2}=\frac{f\left(x_{0}+\right)+f\left(x_{0}-\right)}{2}$.
(a) Replacing $x$ by $x-x_{0}$, we may assume from here on that $x_{0}=0$. $H(x)=h(x)-\frac{h(0+)+h(0-)}{2}$. Note that the Fourier series of $H$ is the same the Fourier series of $h$ minus the constant $\frac{h(0+)+h(0-)}{2}$. Show that
$$
H(x)=\left\{\begin{array}{ll}
f^{\prime}(0-) x+\frac{h(0-)-h(0+)}{2} & \text { if }-\pi<x<0 \\
f^{\prime}(0+) x+\frac{h(0+)-h(0-)}{2} & \text { if } 0<x<\pi
\end{array}\right.
$$
(b) Derive the following Fourier coefficients of $H$ :
$$
a_{0}=\frac{\pi}{4}\left(f^{\prime}(0+)-f^{\prime}(0-)\right) ; \quad a_{n}=\frac{\left((-1)^{n}-1\right)\left(f^{\prime}(0+)-f^{\prime}(0-)\right)}{\pi n^{2}}, n \geq 1
$$
(We will not need the $b_{n}$ 's in the proofs.) (c) Using residues (or other methods your choice)-more specifically, the results of Exercises 17 and 18, Section 5.6, sh that $\sum_{n=1}^{\infty} \frac{(-1)^{n}-1}{\pi n^{2}}=-\frac{\pi}{4}$.
(d) Evaluate the Fourier series of $H$ at 0 and use (c) to show that it converges 0 . Conclude that the Fourier series of $h$ converges to $\frac{h(0+)+h(0-)}{2}$ at $x_{0}=0$.
3. Fourier series at points of discontinuity. Let $f$ be as in Exercise 1 a suppose that $f$ is not continuous at $x_{0}$. Add a correction term $h(x)$ as in E ercise 1 so that $g(x)=f(x)-h(x)$ becomes continuous and differentiable at By construction, we have $g\left(x_{0}\right)=0$. Let $s_{N}(g, x)$ denote the partial sums of $t$ Fourier series of $g$, and define similarly the partial sums of the Fourier series of and $h$. By the linearity of Fourier series, we have $s_{N}(g, x)=s_{N}(f, x)-s_{N}(h, x$ Since $g^{\prime}\left(x_{0}\right)$ exists, we have $s_{N}\left(g, x_{0}\right) \rightarrow g\left(x_{0}\right)=0$ (this is the case of the Fouri series representation theorem that we proved in this section). By Exercise 2, have $s_{N}\left(h, x_{0}\right) \rightarrow \frac{h\left(x_{0}+\right)+h\left(x_{0}-\right)}{2}=\frac{f\left(x_{0}+\right)+f\left(x_{0}-\right)}{2}$, where the second equality $f^{\circ}$ lows from the way we defined $h$. Thus $s_{N}(f, x) \rightarrow \frac{f\left(x_{0}+\right)+f\left(x_{0}-\right)}{2}$, which complet the proof.
