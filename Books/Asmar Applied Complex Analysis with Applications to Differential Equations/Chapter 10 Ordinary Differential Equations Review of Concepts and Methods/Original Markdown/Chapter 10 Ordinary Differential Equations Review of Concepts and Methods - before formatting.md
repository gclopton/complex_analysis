<!-- Page 1 -->

Left margin note (page 1)

Topics to Review
This appendix is self-contained and requires basic knowledge of differential and integral calculus.

Looking Ahead...
This appendix presents standard techniques for solving linear ordinary differential equations. They are needed throughout this book. Our primary use of the power series and Frobenius methods of Sections A.4, A.5, and A. 6 will be to establish the basic properties of Bessel functions (Chapter 4) and Legendre polynomials (Chapter 5).

Right margin note (page 1)

ations entary S LIE he deartial differiques ntials differerties est of linear is not rence

++++

APPENDIX A

ORDINARY
DIFFERENTIAL
EQUATIONS: REVIEW
OF CONCEPTS
AND METHODS

Among all the mathematical disciplines the theory of differential equ is the most important. It furnishes the explanation of all those elem manifestations of nature which involve time.
-SOPHU,

A basic knowledge of ordinary differential equations is essential for th velopment of the main topics of this book. For example, solving a differential equation by standard methods leads naturally to ordinary ential equations. In this appendix we provide a review of the basic techr that will be useful in this book. Our brief presentation covers the esse of linear ordinary differential equations as taught in a first course on ential equations. In the first section we present the fundamental prop of existence. uniqueness, and linear independence of solutions. The the chapter is devoted to the treatment of the basic tools for solving ordinary differential equations, including series methods. This chapter intended as a comprehensive treatment, but rather as a convenient refe for topics that are needed in the book.

---

<!-- Page 2 -->

Left margin note (page 2)

A2
Appendix A
A. 1 Linear

THEC SOLUTION FIRST

I
DIFFERI
EQU

The expression $\int p$ resents an antide $p(x)$. and so it is to a constant $C$. I (2). you should tak value of $C$ in both of $\int p(x) d x$. Us most convenient ch 0 . (See Example 1.

Right margin note (page 2)

known feren-
e given lat the 2 times (1) is

1s. We of the

1en any
oth oc-
grating
itten as desired or all $x$,
ution is

++++

Ordinary Differential Equations: Review of Concepts and Methods
Ordinary Differential Equations

An ordinary differential equation is an equation that involves an un function $y$ and its derivatives $y^{(j)}$ of order $j$. A linear ordinary dit tial equation in standard form is an equation
$$
y^{(n)}+p_{n-1}(x) y^{(n-1)}+\cdots+p_{1}(x) y^{\prime}+p_{0}(x) y=g(. x)
$$
where $n$ is called the order of the equation and $p_{j}(x)$ and $g(x)$ ar functions of $x$. The expression standard form refers to the fact tl leading coefficient is 1 . A solution of (1) on an interval $I$ is any $r$ differentiable function $y=y(x)$ satisfying (1) on $I$. The equation homogeneous if $g(x) \equiv 0$, otherwise it is nonhomogeneous.

The first- and second-order equations are of particular interest to 1 can describe completely the solution of the first one, while discussion second will occupy the rest of this appendix.

OREM 1 OF THE ORDER LINEAR ENTIAL JATION

Suppose that $p(x)$ and $g(x)$ are continuous on the interval $I$. Tl solution of the first-order linear differential equation
$$
y^{\prime}+p(x) y=g(x), \quad x \text { in } I,
$$
is of the form
$$
y=e^{-\int p(x) d x}\left[C+\int g(x) e^{\int p(x) d x} d x\right],
$$
where $\int p(x) d x$ represents the same antiderivative of $p(x)$ in b curences.
$(x) d x$ reprivative of defined up n applying e the same occurences ually, the oice is $C=$

Proof Suppose $y$ is a solution. Multiply the equation through by the intes factor $\mu(x)=e^{\int p(x) d x}$ and get
$$
\mu(x)\left[y^{\prime}+p(x) y\right]=g(x) \mu(x) .
$$

Since $\mu^{\prime}(x)=p(x) \mu(x)$, by the product rule, the equation can be rewr $[\mu(x) y]^{\prime}=g(x) \mu(x)$. Integrating both sides and dividing by $\mu(x)$ yields the solution. (Note that, since $\mu(x)$ is an exponential function, it is nomzero f and so we may divide by it.)

EXAMPLE 1 A first-order differential equation
Using Theorem 1, we find all solutions of the differential equation
$$
y^{\prime}-y=2 \text {. }
$$

The integrating factor is $\mu(x)=e^{-\int d x}=e^{-x}$ and hence the general sol $y=e^{x}\left[C-2 e^{-x}\right]=C e^{x}-2$, where $C$ is an arbitrary constant.

---

<!-- Page 3 -->

Left margin note (page 3)

THE WRONSKIAN

Right margin note (page 3)

A3

t, in there at we tions ssion
l $I$.
ential given
sim-
skian

Their
ns of

++++

Section A. 1 Linear Ordinary Differential Equations

In treating higher-order equations we are not so fortunate, in the general, we do not have a closed form for the solutions. However, are fundamental results concerning the general form of the solutions the discuss in the remainder of this section. Important cases where solu are given explicitly are presented in Sections A. 2 and A.3. Our discu focuses first on the homogeneous equation
$$
y^{(n)}+p_{n-1}(x) y^{(n-1)}+\cdots+p_{1}(x) y^{\prime}+p_{0}(x) y=0,
$$
where all the coefficient functions are continuous on some fixed interva
We begin with a definition that is central to our treatment.

Let $y_{1}, y_{2}, \ldots, y_{n}$ be any $n$ solutions to the homogeneous linear differ equation (3). The Wronskian $W\left(y_{1}, y_{2}, \ldots, y_{n}\right)$ of these solutions is by the following $n \times n$ determinant:
$$
W\left(y_{1}, y_{2}, \ldots, y_{n}\right)=\left|\begin{array}{cccc}
y_{1} & y_{2} & \ldots & y_{n} \\
y_{1}^{\prime} & y_{2}^{\prime} & \ldots & y_{n}^{\prime} \\
\vdots & \vdots & \vdots & \vdots \\
y_{1}^{(n-1)} & y_{2}^{(n-1)} & \ldots & y_{n}^{(n-1)}
\end{array}\right| .
$$

We will sometimes use the alternative notation $W\left(y_{1}, y_{2}, \ldots, y_{n}\right)(x)$, or ply $W(x)$, to emphasize that the Wronskian is a function of $x$.

EXAMPLE 2 Computing Wronskians
(a) The equation $y^{\prime \prime}-y=0$ has solutions $y_{1}=e^{x}$ and $y_{2}=e^{-x}$. Their Wron is
$$
W\left(e^{x}, e^{-x}\right)=\left|\begin{array}{cc}
e^{x} & e^{-x} \\
e^{x} & -e^{-x}
\end{array}\right|=e^{x}\left(-e^{-x}\right)-e^{x}\left(e^{-x}\right)=-2 .
$$
(b) The equation $y^{\prime \prime}+y=0$ has solutions $y_{1}=\cos x$ and $y_{2}=\sin x$. Wronskian is
$$
W(\cos x, \sin x)=\left|\begin{array}{cc}
\cos x & \sin x \\
-\sin x & \cos x
\end{array}\right|=\cos ^{2} x+\sin ^{2} x=1 .
$$

The next theorem gives an explicit form of the Wronskian in tern the coefficient functions in (3).

---

<!-- Page 4 -->

Left margin note (page 4)

A4
Appendix A

THEO
ABEL'S FOP
FC
WRON

Since the key issue II vanishes or not, divide by W' to sepe ables. An appeal to 1 is necossary.

THEC
EXISTEN
FUNDAM
SETS OF SOLU

Right margin note (page 4)

erential
erential

1e $x$ in $n=3$ ensions ation is lutions,
conse-
d form
differ-
$1 I$, has crinore, $c_{2} y_{2}+$ blutions set of
f order Note et. If nbinaion.

++++

Ordinary Differential Equations: Review of C'oncepts and Methods

REM 2
RMULA
R THE
SKIAN
is whether we cannot arate variTheorem

REM 3 NCE OF ENTAL JTIONS

Let $y_{1}, y_{2}, \ldots, y_{n}$ be any $n$ solutions to the homogeneous linear diff equation (3). Then the Wronskian $W(x)$ satisfies the first-order diff equation
$$
W^{\prime}(x)+p_{n-1}(x) W(x)=0, \quad \text { for } x \text { in } I,
$$
and hence
(4)
$$
W(x)=C e^{-\int p_{n-1}(x) d x} .
$$

Consequently, either $W(x) \neq 0$ for all $x$ in $I$, or $W(x) \equiv 0$ on $I$.
The point of this theorem is that determining that $W(x) \neq 0$ for son $I$ allows us to conclude that $W(x) \neq 0$ for all $x$ in $I$.
Proof For clarity's sake, we give a proof only for $n=2$. (The case is treated in Exercise 31.) The same approach generalizes to higher dim but requires a greater knowledge of linear algebra. For $n=2$, the equa $y^{\prime \prime}+p_{1}(x) y^{\prime}+p_{0}(x) y=0$, and $W(x)=y_{1} y_{2}^{\prime}-y_{1}^{\prime} y_{2}$. Since $y_{1}$ and $y_{2}$ are so we have
$$
\begin{aligned}
W^{\prime}(x) & =y_{1} y_{2}^{\prime \prime}-y_{1}^{\prime \prime} y_{2} \\
& =y_{1}\left[-p_{1}(x) y_{2}^{\prime}-p_{0}(x) y_{2}\right]-\left[-p_{1}(x) y_{1}^{\prime}-p_{0}(x) y_{1}\right] y_{2} \\
& =-p_{1}(x) W(x)
\end{aligned}
$$

This is a first-order differential equation for $W(x)$. and (4) is an immediate quence of (2) in Theorem 1.

It is crucial in applying Theorem 2 to put the equation in standar and verify the continuity of the coefficients. See Exercise 23.

We can now state a fundamental result in the theory of ordinary ential equations.

The homogeneous equation (3)
$$
y^{(n)}+p_{n-1}(x) y^{(n-1)}+\cdots+p_{1}(x) y^{\prime}+p_{0}(x) y=0 .
$$
where the coefficient functions $p_{j}(x)$ are all continuous on an interva $n$ solutions $y_{1}, y_{2}, \ldots, y_{n}$ with nonvanishing Wronskian on 1 . Furth given any such set $y_{1}, y_{2}, \ldots y_{n}$ and any solution $y$, then $y=c_{1} y_{1}+ \cdots+c_{n} y_{n}$ for a unique choice of constants $c_{1}, c_{2}, \ldots, c_{n}$. The set of so $y_{1}, y_{2}, \ldots, y_{n}$ with nonvanishing Wronskian is called a fundamental solutions.

Theorem 3 asserts that any linear homogeneous differential equation o $n$ has $n$. solutions that span the set of all solutions of the equation. that the theorem does not assert the uniqueness of a fundamental s $y_{1}, y_{2}, \ldots, y_{n}$ is a fundamental set of solutions, then the linear con tion $y=c_{1} y_{1}+c_{2} y_{2}+\cdots+c_{n} y_{n}$ is referred to as the general solut

---

<!-- Page 5 -->

Left margin note (page 5)

SNOILVAOO' -NON HO NOILATOS TV\&ANGS ๕ ΝεθΟΊ.

GTAIONIHd NOILISO d HGd Đ NGHOTHL

Right margin note (page 5)

A5

on of imple aling
ration nation
huous ation that is $y_{1}$, on of oy $y_{p}$ ution ff the $y_{p}=$ of the as the d the
neous n any
ect to are pecify order itions

++++

Section A. 1 Linear Ordinary Differential Equations

We have been using without verification that a linear combinati solutions of a homogeneous linear equation is again a solution. This s fact. called the superposition principle, can be checked directly by appe to (3). We state it here for ease of reference.

Suppose that $u(x)$ and $v(x)$ are solutions of the linear homogeneous eqr (3) and let $c$ and $d$ be any two numbers. Then the linear combit $c u(x)+d v(x)$ is also a solution of (3).

Nonhomogeneous Differential Equations
Let us recall from (1) the general nonhomogeneous equation
$$
y^{(n)}+p_{n-1}(. r) y^{(n 1)}+\cdots+p_{1}(x) y^{\prime}+p_{0}(x) y=g(x),
$$
where the coefficient functions and $g(x)$ are all assumed to be contin on some interval $I$. If $g(x)$ is replaced by 0 , we call the resulting equ the associated homogeneous equation. We know from Theorem 3 the associated homogeneous equation has a fundamental set of solutio $y_{2}, \ldots, y_{n}$. We will show in Section A.2, using the method of variati parameters, that (5) has at least one solution that we will denote and call a particular solution. Now suppose that $y$ is any other sol of (5). It is a simple exercise to check that $y-y_{p}$ is a solution o associated homogeneous equation. By Theorem 3 we must have $y$ $c_{1} y_{1}+c_{2} y_{2}+\cdots+c_{n} y_{n}$. Thus, if $y_{h}$ denotes the general solution $c^{3}$ associated homogeneous equation, it follows that $y=y_{h}+y_{p}$ (known a general solution of the nonhomogeneous equation). We have prove following important result.

Let $y_{h}$ and $y_{p}$ denote, respectively, the general solution of the homoge equation associated with (5) and a particular solution of (5). The solution $y$ of (5) has the form
$$
y=y_{h}+y_{p} .
$$

Often in applications we have to solve differential equations subje certain conditions; for example,
$$
y^{\prime \prime}+y=c^{r^{\prime}}, \quad y(0)=0, y^{\prime}(0)=1 .
$$

Such a problem is called an initial value problem, and the condition called initial conditions. Typically we impose enough conditions to s a unique solution of the problem. Since the general solution of an $n$th linear differential equation has $n$ arbitrary constants, we expect $n$ cond to suffice.

---

<!-- Page 6 -->

Left margin note (page 6)

A6
Appendix A

THEO EXISTENC UNIQUENES INITIAL PRO]

![](./images/66923605-2b3e-4154-b144-3e182be82ea5-06_398_466_793_63.jpg)

Figure 1 Various from Example 3.

![](./images/66923605-2b3e-4154-b144-3e182be82ea5-06_421_468_1396_63.jpg)

Figure 2 Solution tial value problem ple 3 and its tange $x=0$. It is the o among those in Fig goes through the p and that has slope equal to $y^{\prime}(0)=2$.

Right margin note (page 6)

1 equa-
en this
mental
ve take
e $2 \times 2$
( $x_{0}$ )
( $x_{0}$ )
system follows of the lution.
1. Let initial and $b$. er that
+3 as a $2 y=0$ g these olution

olution

++++

Ordinary Differential Equations: Review of Concepts and Methods

REM 6
E AND
SS FOR
VALUE
BLEMS

Consider the initial value problem consisting of the linear differentia tion (5) and the initial conditions
$$
y\left(x_{0}\right)=y_{0}, y^{\prime}\left(x_{0}\right)=y_{0}^{\prime}, \ldots, y^{(n-1)}\left(x_{0}\right)=y_{0}^{(n-1)},
$$
where $x_{0}$ is in $I$ and $y_{0}, y_{0}^{\prime}, \ldots, y_{0}^{(n-1)}$ are prescribed values. Th problem has a unique solution $y$ on the interval $I$.

Proof Let $y_{p}$ be a particular solution to (5) and let $y_{1}, y_{2}, \ldots, y_{n}$ be a funda set of solutions to the associated homogeneous equation. For clarity's sake 1 $n=2$, although the proof generalizes for arbitrary $n$. We need to solve the system
$$
\left\{\begin{array} { l } 
{ c _ { 1 } y _ { 1 } ( x _ { 0 } ) + c _ { 2 } y _ { 2 } ( x _ { 0 } ) + y _ { p } ( x _ { 0 } ) = y _ { 0 } } \\
{ c _ { 1 } y _ { 1 } ^ { \prime } ( x _ { 0 } ) + c _ { 2 } y _ { 2 } ^ { \prime } ( x _ { 0 } ) + y _ { p } ^ { \prime } ( x _ { 0 } ) = y _ { 0 } ^ { \prime } }
\end{array} \Leftrightarrow \left\{\begin{array}{l}
c_{1} y_{1}\left(x_{0}\right)+c_{2} y_{2}\left(x_{0}\right)=y_{0}-y_{p} \\
c_{1} y_{1}^{\prime}\left(x_{0}\right)+c_{2} y_{2}^{\prime}\left(x_{0}\right)=y_{0}^{\prime}-y_{p}^{\prime}
\end{array}\right.\right.
$$
for the unknowns $c_{1}$ and $c_{2}$. Since the determinant of the matrix of this is precisely the Wronskian and is nonzero by definition (see Theorem 3), it that the system has a unique solution pair $c_{1}, c_{2}$. This proves the existence solution of the initial value problem. To establish the uniqueness of the se suppose that $u(x)$ and $v(x)$ are two solutions to the initial value probler $w=u-v$. Then $w$ satisfies the associated homogencous equation with 0 values. We know from Theorem 3 that $w=a y_{1}+b y_{2}$ for some choice of $a$ Now using the initial values of $w$ and the fact that $W\left(y_{1}, y_{2}\right)\left(x_{0}\right) \neq 0$, we int $a=b=0$ and hence $w \equiv 0$ implying that $u \equiv v$.

EXAMPLE 3 An initial value problem
You can (and should) check that the equation $y^{\prime \prime}-3 y^{\prime}+2 y=4 x$ has $y_{p}=2 x$ particular solution and that the associated homogeneous equation $y^{\prime \prime}-3 y^{\prime}+$ has general solution $y_{h}=c_{1} e^{x}+c_{2} e^{2 x}$. (General techniques for derivin solutions will be developed in the next two sections.) Hence the generals of the nonhomogeneous equation is
$$
y=y_{h}+y_{p}=c_{1} e^{x}+c_{2} e^{2 x}+2 x+3
$$
(see Figure 1). Now suppose that we want to solve the initial value probler
$$
y^{\prime \prime}-3 y^{\prime}+2 y=4 x, \quad y(0)=4, y^{\prime}(0)=2 .
$$

Using the initial conditions, we get
$$
\begin{array}{l}
y(0)=4 \Rightarrow c_{1}+c_{2}=1 \\
y^{\prime}(0)=2 \Rightarrow c_{1}+2 c_{2}=0
\end{array}
$$

This system has a unique solution $c_{1}=2$ and $c_{2}=-1$. Hence the (unique) s of the initial value problem is $y=2 e^{x}-e^{2 x}+2 x+3$ (Figure 2).

---

<!-- Page 7 -->

Left margin note (page 7)

મ. \&VANIT HOA NOIHGLIHO NVIYSNOUM $\angle$ WGYOAHL

Right margin note (page 7)

A 7

ions
be ,..., densaid ce is folence
ontial g are
defi⇒ (i). that sion the $n$ iscly nant roof that $=0$. not (for lues,
$/\left(e^{x}\right.$, ntial ation

For ions.

++++

Section A. 1 Linear Ordinary Differential Equations

We next present a brief discussion of linear independence of solut and its connection to fundamental sets.

The functions $f_{1}, f_{2}, \ldots, f_{n}$ defined on an interval $[a, b]$ are said $t$ linearly independent on $[a, b]$ if the only choice of the constants $c_{1}, c_{2} c_{n}$ for which the linear combination $c_{1} f_{1}+c_{2} f_{2}+\cdots+c_{n} f_{n}$ vanishes i tically on $[a, b]$ is $c_{1}=c_{2}=\cdots=c_{n}=0$. Otherwise, the functions are to be linearly dependent. When $n=2$, we note that linear dependen equivalent to one function being a constant multiple of the other. The lowing result shows a connection between the notion of linear independ and fundamental sets.

Let $y_{1}, y_{2}, \ldots y_{n}$ be any $n$ solutions to the homogeneous linear differ equation (3) with coefficients continuous on an interval $I$. The followin equivalent:
(i) $y_{1}, y_{2}, \ldots, y_{n}$ are linearly independent on $I$;
(ii) $y_{1}, y_{2}, \ldots, y_{n}$ form a fundamental set of solutions of (3);
(iii) $W\left(y_{1}, y_{2}, \ldots, y_{n}\right)\left(x_{0}\right) \neq 0$ for some $x_{0}$ in $I$;
(iv) $W\left(y_{1}, y_{2}, \ldots, y_{n}\right)(x) \neq 0$ for all $x$ in $I$.

Proof Clearly (ii) ⇔ (iii) ⇔ (iv) follow from Theorems 2 and 3 and the nition of a fundamental set. We conclude by proving (i) ⇒ (iii) and (iii) $=$ We start with (iii) ⇒ (i). Suppose that $y_{1}, y_{2}, \ldots, y_{n}$ are any $n$ solutions such $c_{1} y_{1}+c_{2} y_{2}+\cdots+c_{n} y_{n}=0$. By differentiating this equation $n-1$ times in succe and then setting $x=x_{0}$, we get a system of $n$ linear homogeneous equations in unknowns $c_{1}, c_{2}, \ldots, c_{n}$. The determinant of the matrix of this system is prec $W\left(x_{0}\right)$, which is nonzero by assumption. The nonvanishing of this determi implies that $c_{1}=c_{2}=\cdots=c_{n}=0$, proving (iii) ⇒ (i). To complete the it is enough to show (i) ⇒ (iii). The proof is by contradiction. We assume $y_{1}, y_{2}, \ldots, y_{n}$ are linearly independent on $I$ and that $W\left(y_{1}, y_{2}, \ldots, y_{n}\right)\left(x_{0}\right)$ The vanishing of the Wronskian implies that there are constants $c_{1}, c_{2}, \ldots, c_{n}$ all zero. such that all the initial values of $y=c_{1} y_{1}+c_{2} y_{2}+\cdots+c_{n} y_{n}$ are 0 at $x_{0} n=2$, this fact is clear). However, the solution $w \equiv 0$ has the same initial va and so by the uniqueness part of Theorem $6, w \equiv y \equiv 0$, implying that $c_{1}=c_{2}= =c_{n}=0$ by the definition of linear independence, which is a contradiction.

EXAMPLE 4 Fundamental sets of solutions, linear independence We saw in Example 2 that $e^{x}$ and $e^{-x}$ are solutions of $y^{\prime \prime}-y=0$ and that $U \left.e^{-x}\right)=-2 \neq 0$. Thus, by Theorem 7. the general solution of the differe equation is of the form $y=c_{1} e^{x}+c_{2} e^{-x}$; and so any solution is a linear combin of the functions, $r^{x}$ and $e^{-x}$, which form a fundamental set of solutions.

It is worthwhile to note that the fundamental set of solutions is not unique the equation at hand, you can casily check that $\cosh x$ and $\sinh x$ are also solut Their Wronskian is
$$
W(\cosh x, \sinh x)=\left|\begin{array}{ll}
\cosh x & \sinh x \\
\sinh x & \cosh x
\end{array}\right|=\cosh ^{2} x-\sinh ^{2} x=1
$$

---

<!-- Page 8 -->

Left margin note (page 8)

A8
Appendix A
Ordinary

Right margin note (page 8)

of the
of the t order This we will linear
amental $\sinh x$.
inctions
swer by

++++

Differential Equations: Review of Concepts and Methods

Thus, by Theorem 7, the general solution of the differential equation is als form $y=c_{1} \cosh x+c_{2} \sinh x$.

Thus far we have developed an understanding of the general form solutions of linear differential equations. However, aside from the firs case, we have not developed techniques for finding explicit solutions will occupy us throughout the remainder of this appendix, where develop methods for solving certain important classes of higher order differential equations.

Exercises A. 1
In Exercises 1-10, solve the given first order differential equation.
1. $y^{\prime}+y=1$.
2. $y^{\prime}+2 x y=x$.
3. $y^{\prime}=-.5 y$.
4. $y^{\prime}=2 y+x$.
5. $y^{\prime}-y=\sin x$.
6. $y^{\prime}-2 x y=x^{3}$.
7. $x y^{\prime}+y=\cos x$.
8. $y^{\prime}-\frac{2}{x} y=x^{2}$.
9. $y^{\prime}+\tan x y=\cos x$.
10. $y^{\prime}+\tan x y=\sec ^{2} x$.

In Exercises 11-20, solve the given initial value problem.
11. $y^{\prime}=y, y(0)=1$.
13. $y^{\prime}+x y=x, y(0)=0$.
15. $x y^{\prime}+2 y=1, \quad y(-1)=-2$.
17. $y^{\prime}+y \tan x=\tan x, y(0)=1$.
19. $y^{\prime}+e^{x} y=e^{x}, \quad y(0)=2$.
12. $y^{\prime}+2 y=1, y(0)=2$.
14. $y^{\prime}+\frac{y}{x}=\frac{\sin x}{x}, y(\pi)=1$.
16. $x y^{\prime}-2 y=\frac{1}{x}, \quad y(1)=0$.
18. $y^{\prime}+y \tan x=\tan x, y(0)=2$
20. $y^{\prime}+y=e^{x}, \quad y(3)=0$.
21. (a) Check that the functions
$$
e^{x}, e^{-x}, \cosh x, \sinh x
$$
are solutions of
$$
y^{\prime \prime}-y=0 .
$$
(b) We know from Example 4 that $\left\{e^{x}, e^{-x}\right\}$ and $\{\cosh x, \sinh x\}$ are fund sets of solutions. Express $e^{x}$ as a linear combination of the functions $\cosh x$
(c) Can you think of other fundamental sets of solutions?
22. Check that the functions $e^{x}, e^{-x}, \cosh x$ are solutions of
$$
y^{\prime \prime \prime}-y^{\prime}=0 .
$$
(b) Show directly that $W\left(e^{x}, e^{-x}, \cosh x\right) \equiv 0$ and conclude that these ft do not form a fundamental set.
(c) Find a fundamental set of solutions by inspection. Justify your an computing the Wronskian.
23. (a) Check that the functions $x, x^{2}$ are solutions of
$$
x^{2} y^{\prime \prime}-2 x y^{\prime}+2 y=0 .
$$

---

<!-- Page 9 -->

Right margin note (page 9)

A. 9

rem 2?
es this inearly
l equa-

2(s--1).
he pre-
ntiable

++++

Section A. 1 Lincar Ordinary Differential Equation
(b) Compute the Wronskian of the solutions.
(c) Note that the Wronskian vanishes at $x=0$. Does this contradict Theo
24. (a) Check that the functions $e^{, r}, 1+x$ are solutions of
$$
r y^{\prime \prime}-(1+x) y^{\prime}+y=0 .
$$
(b) Check that both of these functions satisfy $y(0)=1$ and $y^{\prime}(0)=1$. contradict the uniqueness part in Theorem 6?
(c) Compute the Wronskian of the solutions and conclude that they are l independent on $(0, \infty)$.

In Exercises 25-30, solve the initial value problem consisting of the differentio tion in Example 3.
25. $y(0)=0, y^{\prime}(0)=0$.
26. $y(0)=1, y^{\prime}(0)=-1$.
27. $y(1)=0, y^{\prime}(1)=2$.
28. $y(1)=1, y^{\prime}(1)=-1$.
[Hint: In Exercises 27 and 28, it is easier to work with $y_{h}=c_{1} e^{(x-1)}+c_{2}$ o Why is this possible?]
29. $y(2)=0, y^{\prime}(2)=1$.
30. $y(3)=3, y^{\prime}(3)=3$.
[Hint: In Exercises 29-30, use a $y_{h}$ that simplifies the computations as in th vious exercises.]
31. Project Problem: Abel's formula for $n=3$.
(a) Let $y_{1}, y_{2}, y_{3}$ be any three solutions of the third order equation
$$
y^{\prime \prime \prime}+p_{2}(x) y^{\prime \prime}+p_{1}(x) y^{\prime}+p_{0}(x) y=0 .
$$

Derive the formulas for the Wronskian
$$
W\left(y_{1}, y_{2}, y_{3}\right)=\left(y_{2} y_{3}^{\prime}-y_{2}^{\prime} y_{3}\right) y_{1}^{\prime \prime}-\left(y_{1} y_{3}^{\prime}-y_{1}^{\prime} y_{3}\right) y_{2}^{\prime \prime}+\left(y_{1} y_{2}^{\prime}-y_{1}^{\prime} y_{2}\right) y_{3}^{\prime \prime}
$$
and
$$
W^{\prime}\left(y_{1} \cdot y_{2}, y_{3}\right)=\left(y_{2} y_{3}^{\prime}-y_{2}^{\prime} y_{3}\right) y_{1}^{\prime \prime \prime}-\left(y_{1} y_{3}^{\prime}-y_{1}^{\prime} y_{3}\right) y_{2}^{\prime \prime \prime}+\left(y_{1} y_{2}^{\prime}-y_{1}^{\prime} y_{2}\right) y_{3}^{\prime \prime \prime}
$$
(b) Follow the proof of Theorem 2 to show that
$$
W^{\prime}=-p_{2}(x) W .
$$
(c) Derive Abel's formula for $n=3$.
32. (a) Show that $W\left(x^{3} \cdot\left|x^{3}\right|\right)=0$ for all $x$. (The function $\left|x^{3}\right|$ is differe for all $x$. ('an you see why?)
(b) Show. however, that $x^{3} \cdot\left|x^{3}\right|$ are linearly independent on the real line.
(c) Does this contradict Theorem 7? Justify your answer.

---

<!-- Page 10 -->

Left margin note (page 10)

A10
Appendix A
A. 2 Linear

Right margin note (page 10)

ents ential
ndard ortant will
eristic
future
$\lambda_{1}, \lambda_{2}$,

, , ,

++++

Ordinary Differential Equations: Review of Concepts and Methods

Ordinary Differential Equations with Constant Coeffici The general form of the $\boldsymbol{n}$ th order homogeneous linear differ equation with constant coefficients is
$$
a_{n} y^{(n)}+a_{n-1} y^{(n-1)}+\cdots+a_{1} y^{\prime}+a_{0} y=0,
$$
where each $a_{j}$ is a constant and $a_{n} \neq 0$. The equation can be put in sta form by dividing through by the leading coefficient $a_{n}$. This imp class of equations is needed throughout this book. Our presentatic emphasize the second-order case, which is by far the most useful.

The simple first-order case of (1) suggests that we try
$$
y=e^{\lambda x}
$$
in solving the general case. Since
$$
y^{\prime}=\lambda e^{\lambda x}, y^{\prime \prime}=\lambda^{2} e^{\lambda x}, \ldots, y^{(n-1)}=\lambda^{n-1} e^{\lambda x}, y^{(n)} \cdots \lambda^{n} e^{\lambda x},
$$
substituting these into (1), we get
$$
\left(a_{n} \lambda^{n}+a_{n-1} \lambda^{n-1}+\cdots+a_{1} \lambda+a_{0}\right) e^{\lambda x}=0 .
$$

Thus $y=e^{\lambda x}$ is a solution to (1) if $\lambda$ is any root of the characte equation
$$
a_{n} \lambda^{n}+a_{n-1} \lambda^{n-1}+\cdots+a_{1} \lambda+a_{0}=0 .
$$

The roots of this equation are called the characteristic roots. For use, we define the characteristic polynomial
$$
p(\lambda)=a_{n} \lambda^{n}+a_{n-1} \lambda^{n-1}+\cdots+a_{1} \lambda+a_{0} .
$$

In the case when this polynomial has $n$ distinct characteristic roots $\ldots, \lambda_{n}$, the general solution of (1) is
$$
y=c_{1} e^{\lambda_{1} x}+c_{2} e^{\lambda_{2} x}+\cdots+c_{n} e^{\lambda_{n} x} .
$$

Equivalently, a fundamental set of solutions is given by
$$
e^{\lambda_{1} x}, e^{\lambda_{2} x}, \ldots, e^{\lambda_{\mu} x} .
$$

This follows from the nonvanishing of the Wronskian $W\left(e^{\lambda_{1} x}, e^{\lambda_{2}}\right. e^{\lambda_{n} x}$ ). See Exercise 77.

---

<!-- Page 11 -->

Left margin note (page 11)

![](./images/66923605-2b3e-4154-b144-3e182be82ea5-11_418_447_364_43.jpg)

Figure 1 The hyperbolic cosine and sine (with $\mu>0$ ): $\cosh \mu x$ is even and $\cosh \mu x \geq$ 1 for all $x$.
$\sinh \mu x$ is odd and $\sinh \mu x=0$ if and only if $x=0$.

![](./images/66923605-2b3e-4154-b144-3e182be82ea5-11_408_412_1608_45.jpg)

Figure 2 The complex number $\mu=\alpha+i \beta$ and its conjugate $\bar{\mu}=\alpha-i \beta$.

Right margin note (page 11)

A11
ristic

ations 1 , the er set rbolic
of sod also
$\neq 0$.
nh $\mu x$ ential $x$ and
roots ation set of
used is are have any ts its this

++++

Section A. 2 Linear Ordinary Differential Equations with Constant Coefficients

EXAMPLE 1 Hyperbolic functions
The equation $y^{\prime \prime}-\mu^{2} y=0(\mu>0)$ occurs frequently in this book. Its characte equation is
$$
\lambda^{2}-\mu^{2}=0 .
$$
with characteristic roots $\lambda_{1}=\mu$ and $\lambda_{2}=-\mu$. Thus a fundamental set of solu is $\left\{e^{\mu x}, e^{-\mu x}\right\}$. As we observed following Example 4 of the previous section fundamental set of solutions is not unique. In fact, we now describe anoth that is more convenient in some applications. Recall the definition of the hype functions
$$
\cosh \mu x=\frac{e^{\mu x}+e^{-\mu x}}{2} \quad \text { and } \quad \sinh \mu x=\frac{e^{\mu x}-e^{-\mu x}}{2} .
$$

Since these are linear combinations of functions from the fundamental set lutions, they are themselves solutions of the differential equation. You could verify the last assertion directly by using the derivative formulas
$$
\frac{d}{d x} \cosh \mu x=\mu \sinh \mu x \quad \text { and } \quad \frac{d}{d x} \sinh \mu x=\mu \cosh \mu x .
$$

Computing the Wronskian of $\cosh \mu x$ and $\sinh \mu x$. we find
$$
W(\cosh \mu x, \sinh \mu x)=\left|\begin{array}{cc}
\cosh \mu x & \sinh \mu x \\
\mu \sinh \mu x & \mu \cosh \mu x
\end{array}\right|=\mu \overbrace{\left(\cosh ^{2} \mu x-\sinh ^{2} \mu x\right)}^{=1}=\mu
$$

By Theorem 7 of Appendix A. 1 (with $n=2$ ), we conclude that $\cosh \mu x$ and si form a fundamental set of solutions and so the general solution of the differ equation is of the form $y=c_{1} \cosh \mu x+c_{2} \sinh \mu x$. Basic properties of cosli $\mu$ sinh $\mu x$ are illustrated by the graphs shown in Figure 1.

EXAMPLE 2 Characteristic equation with distinct real roots
The third-order equation $y^{\prime \prime \prime}-y^{\prime \prime}-6 y^{\prime}=0$ has characteristic equation
$$
\lambda^{3}-\lambda^{2}-6 \lambda=0 .
$$

Since this equation factors as $\lambda(\lambda-3)(\lambda+2)=0$, we get the characteristic $\lambda_{1}=0, \lambda_{2}=3 . \lambda_{3}=-2$. Thus the general solution of the differential equ is $y=c_{1}+c_{2} \epsilon^{3 x}+c_{3}{ }^{2 x}$. Observe that $\left\{1, e^{3 x}, e^{-2 x}\right\}$ is a fundamental solutions. You should check that $W\left(1, e^{3 x}, e^{-2 x}\right) \neq 0$.

In the case of $n$ distinct roots, the functions in (2) can still be as a fundamental set even when some or all of the characteristic root complex numbers. However, for practical purposes, it is preferable to real-valued functions. This can be done by using the fact that for nonreal root $\mu=\alpha+i \beta(\beta \neq 0)$ of a polynomial with real coefficien complex conjugate $\bar{\mu}=\alpha-i \beta$ is also a root (Figure 2). We illustrat technique with a simple but very important example.

---

<!-- Page 12 -->

Left margin note (page 12)

A12
Appendix A
Ordina

Right margin note (page 12)

set of ff realucting Euler's ormed ons:
at you ds the endent 0 ) is
ginary h the re real
$i$ and tal set Euler's
these $x$ and
$n x)$

Note mental

++++

Differential Equations: Review of Concepts and Methods

EXAMPLE 3 Trigonometric functions
The characteristic equation of $y^{\prime \prime}+k^{2} y \quad 0(k>0)$ is
$$
\lambda^{2}+k^{2}=0
$$

Its characteristic roots are $\lambda_{1}=i k$ and $\lambda_{2}=-i k$. Thus a fundamental solutions is $\left\{c^{i k x}, c^{-i k x}\right\}$. We now describe an alternative fundamental set valued solutions. The construction is similar to the one we used in constr the hyperbolic cosine and sine solutions in the previous example. Recall I identity: $e^{i k x}=\cos k x+i \sin k x$. Consider the following solution, which is 1 by taking a particular linear combination from the fundamental set of soluti
$$
\begin{aligned}
y_{1} & =\frac{e^{i k x}+e^{-i k x}}{2}=\frac{1}{2}(\cos k x+i \sin k x+\cos k x-i \sin k x) \\
& =\cos k x
\end{aligned}
$$

Thus $y_{1}=\cos k x$ is a solution of the differential equation, which is a fact th can verify directly. Similarly, the linear combination $\left(e^{i k x}-e^{-i k x}\right) / 2 i$ yiel solution $y_{2}=\sin k x$. Clearly, $y_{1}$ and $y_{2}$ are real-valued and linearly indep (check their Wronskian). Thus the general solution of $y^{\prime \prime}+k^{2} y=0(k> y=c_{1} \cos k x+c_{2} \sin k x$.

In the previous example, the characteristic roots were purely imag (their real parts $=0$ ). The next example illustrate's a case in whic characteristic roots have nonzero real parts. The solutions will involy exponential functions, along with cosines and sines.

EXAMPLE 4 Complex characteristic roots
The characteristic roots of the equation $y^{\prime \prime}-4 y^{\prime}+5 y=0$ are $\lambda_{1}=2+ \lambda_{2}=2-i$. From (2), the functions $e^{(2+i) x}$ and $e^{(2-i) x}$ form a fundamen of solutions. We next show how to obtain real-valued solutions. Using identity, $e^{i \theta}=\cos \theta+i \sin \theta$, we have
$$
e^{(2+i) x}=e^{2 x} e^{i x}=e^{2 x}(\cos x+i \sin x)
$$

Similarly, $e^{(2-i) x}=e^{2 x}(\cos x-i \sin x)$. By taking sums and differences o solutions, we arrive at the solutions $2 e^{2 x} \cos x$ and $2 i e^{2 x} \sin x$. Thus $e^{2 x} \cos e^{2 x} \sin x$ are two real-valued solutions. We have
$$
\begin{aligned}
W\left(e^{2 x} \cos x, e^{2 x} \sin x\right) & =\left|\begin{array}{cc}
e^{2 x} \cos x & e^{2 x} \sin x \\
e^{2 x}(2 \cos x-\sin x) & e^{2 x}(2 \sin x+\cos x)
\end{array}\right| \\
& =e^{4 x}((2 \sin x+\cos x) \cos x-(2 \cos x-\sin x) \operatorname{si} \\
& =e^{4 x}\left(\cos ^{2} x+\sin ^{2} x\right)=e^{4 x} \neq 0
\end{aligned}
$$

We conclude that $e^{2 x} \cos x$ and $e^{2 x} \sin x$ form a fundamental set of solutions. that in the case of two solutions, we could have verified that the set is fundat by simply observing that one is not a constant multiple of the other.

---

<!-- Page 13 -->

Left margin note (page 13)

![](./images/66923605-2b3e-4154-b144-3e182be82ea5-13_390_454_1497_49.jpg)

Figure 3 Solutions from Example 6(a).

Right margin note (page 13)

A13
come
ained
e the
ponds
d the
1, $y_{2}$,
f the e get ental
$+1)^{2}$, ${ }^{-x}$. A ential form iction btain
omial ration ccond

++++

Section A. 2 Linear Ordinary Differential Equations with Constant Cuefficients

In general, when we have complex characteristic roots, these roots in conjugate pairs. A fundamental set of real-valued solutions is obt by replacing the pair of functions $e^{\mu x}, e^{\bar{\mu} x}$ in (2) by
$$
e^{\alpha x} \cos \beta x, e^{\alpha x} \sin \beta x
$$
for each nonreal pair of characteristic roots $\mu=\alpha \pm i \beta$. Let us illustrat pairing of complex roots with one more example.

EXAMPLE 5 Pairing complex characteristic roots
Find a fundamental set of solutions of $y^{\prime \prime \prime}-y=0$.
Solution Let us find the characteristic roots:
$$
\begin{aligned}
\lambda^{3}-1=0 & \Rightarrow(\lambda-1)\left(\lambda^{2}+\lambda+1\right)=0 \\
& \Rightarrow \lambda_{1}=1, \lambda_{2}=-\frac{1}{2}+i \frac{\sqrt{3}}{2}, \quad \lambda_{3}=-\frac{1}{2}-i \frac{\sqrt{3}}{2} .
\end{aligned}
$$

We have one real root and two complex conjugate roots. To the real root corres the solution $y_{1}=e^{x}$, and to the pair of complex conjugate roots correspon two solutions $y_{2}=e^{-x / 2} \cos \left(\frac{\sqrt{3}}{2} x\right)$ and $y_{3}=e^{-x / 2} \sin \left(\frac{\sqrt{3}}{2} x\right)$. The functions $y$ and $y_{3}$ form a fundamental set of solutions.

Thus far we have not dealt with the case of a repeated root $\mu$ o characteristic polynomial of multiplicity $m>1$. If we try to use (2), the function $e^{\mu x}$ repeated $m$ times, and hence we do not obtain a fundam set. The following example illustrates how to resolve this problem.

EXAMPLE 6 Repeated roots of the characteristic polynomial
(a) The second-order equation $y^{\prime \prime}+2 y^{\prime}+y=0$ has characteristic polynomial ( $\lambda$ which has -1 as a root of multiplicity two. One solution of the equation is $e$ simple verification shows that the function $x e^{-x}$ is also a solution of the differ equation, which is also independent of $e^{-x}$. We conclude that $c^{-x}$ and $x e^{-x}$ a fundamental set of solutions (Figure 3). (We note that the method of redu of order, presented in the next section, provides a straightforward way to the second solution $x e^{-x}$.)
(b) The third-order equation $y^{\prime \prime \prime}-6 y^{\prime \prime}+12 y^{\prime}-8 y=0$ has characteristic polyn $(\lambda-2)^{3}$, which has 2 as a root of multiplicity three. One solution of the equ is $e^{2 x}$. Taking a hint from the previous example, we try $y=x e^{2 x}$ for a s solution. We have
$$
y^{\prime}=e^{2 x}(1+2 x), \quad y^{\prime \prime}=4 e^{2 x}(1+x), \quad y^{\prime \prime \prime}=4 e^{2 x}(3+2 x) .
$$

Plugging into the equation, we obtain
$$
4 e^{2 x}(3+2 x)-24 e^{2 x}(1+x)+12 e^{2 x}(1+2 x)-8 x e^{2 x}=0 .
$$

---

<!-- Page 14 -->

Left margin note (page 14)

A14
Appendix A

Note that there are $r$ independent solutio sponding to repeate order $m$.

Right margin note (page 14)

on, we
check
),
$x^{2} e^{2 x}$
of the
undat $\mu$ be rences
for city $m$
multine the roots
of our view a

++++

Ordinary Differential Equations: Review of Concepts and Methods

Thus $y=x e^{2 x}$ is a solution. For a third solution of the differential equati modify the first solution by multiplying by $x^{2}$, and try $y=x^{2} e^{2 x}$. You can that
$$
y^{\prime}=2 x e^{2 x}(1+x), \quad y^{\prime \prime}=2 e^{2 x}\left(1+4 x+2 x^{2}\right), \quad y^{\prime \prime \prime}=4 e^{2 x}\left(3+6 x+2 x^{2}\right.
$$
and that $x^{2} \epsilon^{2 x}$ is a solution. It is easy to check that the solutions $\varepsilon^{2 x}, x e^{2 x}$ are linearly independent, and hence they form a fundamental set of solutions differential equation.

This example motivates the following prescription for obtaining a mental set of solutions of (1) in the case when multiple roots occur. Le a repeated root having multiplicity $m$. In (2), we replace the $m$ occur of $e^{\mu x}$ by the following $m$ functions:

$n$ linearly
ns corre-
d roots of
$$
e^{\mu x}, x t^{\mu x}, \ldots, x^{m-1} e^{\mu x} .
$$

To obtain a fundamental set of solutions of (1), make this replaceme each repeated characteristic root. (Keep in mind that the multiplic may vary from one root to another.)

Finally, if $\mu=\alpha+i \beta$ is a nonreal repeated characteristic root of plicity $m$, to get a fundamental set of real-valued solutions we combi previous methods and find that the $2 m$ functions associated with the $\mu$ and $\bar{\mu}$ are
$$
\begin{array}{l}
e^{\alpha x} \cos \beta x, x e^{\alpha x} \cos \beta x, \ldots, x^{m-1} e^{\alpha x} \cos 3 x \\
e^{\alpha x} \sin \beta x, x e^{\alpha x} \sin \beta x, \ldots, x^{n-1} e^{\alpha x} \sin 3 x
\end{array}
$$

For ease of reference, we restate in the following box the results discussion in terms of general solutions of (1). For convenience we nonrepeated characteristic root as a root of multiplicity $m=1$.

---

<!-- Page 15 -->

Left margin note (page 15)

GENERAL SOLUTION OF THE $n$ th-ORDER LINEAR HOMOGENEOUS EQUATION WITH CONSTANT COEFFICIENTS

![](./images/66923605-2b3e-4154-b144-3e182be82ea5-15_412_469_1484_52.jpg)

Figure 4 Various solutions from Example 7(b).

Right margin note (page 15)

A15
ling to
linear
jugate of the
roots
dingly,
nt val-
lution in the

++++

Section A. 2 Linear Ordinary Differential Equations with Constant Coefficients

Consider the equation
$$
a_{n} y^{(n)}+a_{n-1} y^{(n-1)}+\cdots+a_{1} y^{\prime}+a_{0} y=0
$$
with characteristic equation
$$
a_{n} \lambda^{n}+a_{n-1} \lambda^{n-1}+\cdots+a_{1} \lambda+a_{0}=0
$$

The general solution of the differential equation is constructed accore the nature of the roots of the characteristic equation as follows.

Case I For each real root $\mu$ of multiplicity $m \geq 1$, we include a combination of the form
$$
c_{1} e^{\mu x}+c_{2} x e^{\mu x}+\cdots+c_{m} x^{m-1} e^{\mu x}
$$

Case II For each nonreal root $\mu=\alpha+i \beta$ and its complex cor $\bar{\mu}=\alpha-i \beta$ of multiplicity $m \geq 1$, we include a linear combination form
$$
\begin{array}{l}
c_{1} e^{\alpha x} \cos \beta x+c_{2} x e^{\alpha x} \cos \beta x+\cdots+c_{m} x^{m-1} e^{\alpha x} \cos \beta x \\
\quad+d_{1} e^{\alpha x} \sin \beta x+d_{2} x e^{\alpha x} \sin \beta x+\cdots+d_{m} x^{m-1} e^{\alpha x} \sin \beta x
\end{array}
$$

EXAMPLE 7 Fourth-order equations
Find the general solution of the following equations:
(a) $y^{(4)}-16 y=0$;
(b) $y^{(4)}+2 y^{\prime \prime}+y=0$.

Solution (a) The characteristic equation is $\lambda^{4}-16=0$, with characteristic $\pm 2$ and $\pm 2 i$. Thus, the general solution is
$$
y=c_{1} e^{2 x}+c_{2} e^{-2 x}+d_{1} \cos 2 x+d_{2} \sin 2 x
$$
(b) The characteristic equation is
$$
\left(\lambda^{2}+1\right)^{2}=0 \quad \text { or } \quad(\lambda-i)^{2}(\lambda+i)^{2}=0 .
$$

Thus the characteristic roots are $i$ and $-i$ with multiplicity 2 each. Accor the general solution is
$$
y=c_{1} \cos x+c_{2} x \cos x+d_{1} \sin x+d_{2} x \sin x
$$

![](./images/66923605-2b3e-4154-b144-3e182be82ea5-15_412_469_1484_52.jpg)
Figure 4 shows some specific solutions that are obtained by assigning differe ues to the constants $c_{1}, c_{2}, d_{1}, d_{2}$.

In the second-order case, we have a simpler form of the general so which we now describe. You will be asked to verify these solutions exercises.

---

<!-- Page 16 -->

Left margin note (page 16)

A16
Appendix A

GEN SOLUTION O SECOND-O

LI
HOMOGEN
EQUATION CONS COEFFIC

Right margin note (page 16)

of this then ations ready gh by ing $y_{p}$ form This strate od of leters,

++++

Ordinary Differential Equations: Review of ('uncepts and Methods
JERAL
F THE
RDER
NEAR
NEOUS
WITH
TANT
IENTS

Consider the equation
$$
a y^{\prime \prime}+b y^{\prime}+c y=0
$$
with characteristic equation
$$
a \lambda^{2}+b \lambda+c=0 .
$$

Let $\lambda_{1}$ and $\lambda_{2}$ denote the characteristic roots. The general solution $y$ differential equation is given by one of the following cases.
Case I If $\lambda_{1}$ and $\lambda_{2}$ are distinct real roots, then
$$
y=c_{1} e^{\lambda_{1} x}+c_{2} e^{\lambda_{2} x} .
$$

Equivalently, write $\lambda_{1}=\frac{-b}{2 a}+\frac{\sqrt{b^{2}-4 a c}}{2 a}=\alpha+\beta$ and $\lambda_{2}=\alpha-\beta$, then
$$
y=e^{\alpha x}\left(c_{1} \cosh \beta x+c_{2} \sinh \beta x\right) .
$$

Case II If $\lambda_{1}=\lambda_{2}$, then
$$
y=c_{1} e^{\lambda_{1} x}+c_{2} x e^{\lambda_{1} x}
$$

Case III If $\lambda_{1}$ and $\lambda_{2}$ are complex conjugate roots with $\lambda_{1}=\alpha+i$ p
$$
y=c_{1} e^{\alpha x} \cos \beta x+c_{2} e^{\alpha x} \sin \beta x .
$$

We now turn our attention to nonhomogencous second-order equ with constant coefficients.

The Method of Undetermined Coefficients
The study of various physical systems often leads to the equation
$$
a y^{\prime \prime}+b y^{\prime}+c y=g(x) .
$$

The general solution of the associated homogeneous equation $y_{h}$ has al been given explicitly. Thus, to find the general solution of (7), it is enou Theorem 5 of the previous section to find a particular solution $y_{p}$. Find depends on the nonhomogeneous term $g$. In many interesting cases, the of $g$ allows us to guess the form of $y_{p}$ up to a set of unknown coefficients. method is called the method of undetermined coefficients. We illu it with examples. We also note that in other cases where the meth undetermined coefficients does not work, we can use variation of param as described in the next section.

---

<!-- Page 17 -->

Left margin note (page 17)

THE METHOD OF UNDETERMINED COEFFICIENTS

Right margin note (page 17)

A17

We nains $A e^{x}$, that is the
$$
y_{h}=
$$
th of
$$
{ }^{2} e^{-x} .
$$
$$
=\frac{1}{2} .
$$
neral ciated ot. ferent form

++++

Section A. 2 Linear Ordinary Differential Equations with Constant Coefficients

EXAMPLE 8 A simple undetermined coefficients problem
Find the general solution of the given nonhomogeneous equation.
(a) $y^{\prime \prime}-4 y^{\prime}+5 y=e^{x}$.
(b) $y^{\prime \prime}+2 y^{\prime}+y=e^{-x}$.

Solution (a) The associated homogeneous equation is solved in Example 4 have $y_{h}=c_{1} e^{2 x} \cos x+c_{2} e^{2 x} \sin x$. To determine the general solution, it rel to find $y_{p}$. Since the right side of the equation is $e^{x}$ it makes sense to try $y_{p}=$ where $A$ is an unknown constant yet to be determined. A computation shows $y_{p}^{\prime \prime}-4 y_{p}^{\prime}+5 y_{p}=2 A e^{x}$. J'or $y_{p}$ to be a solution we must set $A=\frac{1}{2}$. Thu general solution is $y=c_{1} e^{2 x} \cos x+c_{2} e^{2 x} \sin x+\frac{1}{2} e^{x}$.
(b) The associated homogeneous equation is solved in Example 6. We have $c_{1} e^{-x}+c_{2} x e^{-x}$. To find $y_{i}$, it is pointless to try $A e^{-x}$ or $A x e^{-x}$ since bo these solve the homogencous equation. We modify our guess to $y_{p}=A x$ Differentiating $y_{p}$, we find
$$
y_{p}^{\prime}=2 A x e^{-x}-A x^{2} e^{-x}, \quad y_{p}^{\prime \prime}=2 A e^{-x}-4 A x e^{-x}+A x^{2} e^{-x}
$$

Hence $y_{p}^{\prime \prime}+2 y_{p}^{\prime}+y_{p}=2 A e^{-x}$. For $y_{p}$ to be a solution we must choose $A$ Thus the general solution is $y=c_{1} e^{-x}+c_{2} x e^{-x}+\frac{1}{2} x^{2} e^{-x}$.

The procedure we have used above is covered by the following ge rules.

To find a particular solution of (7) when
$$
g(x)=\left(a_{n} x^{n}+a_{n-1} x^{n-1}+\cdots+a_{0}\right) e^{\alpha x}\left\{\begin{array}{l}
\cos \beta x \\
\sin \beta x
\end{array}\right.
$$
we use
$$
\begin{aligned}
y_{p}= & \left(A_{n} x^{n}+A_{n-1} x^{n-1}+\cdots+A_{0}\right) e^{\alpha x} \cos \beta x \\
& +\left(B_{n} x^{n}+B_{n-1} x^{n-1}+\cdots+B_{0}\right) e^{\alpha x} \sin \beta x
\end{aligned}
$$
provided that no term in the expression of $y_{p}$ is a solution of the asso homogeneous equation. If not, we modify this expression by multi] by $x$ or $x^{2}$. We use $x$ if the characteristic polynomial of the asso homogeneous equation has distinct roots, and $x^{2}$ if it has a double ro Superposition rule If the right side of (7) is a sum of several dif functions of the form (8), we use a corresponding sum of terms of the (9).

---

<!-- Page 18 -->

Left margin note (page 18)

A18
Appendix A
Ordinary

Right margin note (page 18)

we see in the
$$
\begin{array}{l}
x+D) \\
y+2 D .
\end{array}
$$
ither of eed for $\cos x-$
this we

expres-
troduce

++++

Differential Equations: Review of Concepts and Methods

EXAMPLE 9 The method of undetermined coefficients
Use the method of undetermined coeflicients to find the general solution of
$$
y^{\prime \prime}-3 y^{\prime}+2 y=x^{3} .
$$

Solution It is straightforward to see that $y_{h}=c_{1} e^{x}+c_{2} e^{2 x}$. From (9), that $y_{p}=A x^{3}+B x^{2}+C x+D$. Note that none of these terms appears expression of $y_{h}$. We have
$$
\begin{aligned}
y_{p}^{\prime \prime}-3 y_{p}^{\prime}+2 y_{p} & =6 A x+2 B-3\left(3 A x^{2}+2 B x+C\right)+2\left(A x^{3}+B x^{2}+C\right. \\
& =2 A x^{3}+(-9 A+2 B) x^{2}+(6 A-6 B+2 C) x+2 B-3 C
\end{aligned}
$$

For $y_{p}$ to be a solution, $A, B, C$, and $D$ must satisfy
$$
\begin{aligned}
2 A & =1 \\
-9 A+2 B & =0 \\
6 A-6 B+2 C & =0 \\
2 B-3 C+2 D & =0
\end{aligned}
$$

The solution of this linear system is $A=\frac{1}{2}, B=\frac{9}{4}, C=\frac{21}{4}, D=\frac{45}{8}$. Thus
$$
y_{p}=\frac{1}{2} x^{3}+\frac{9}{4} x^{2}+\frac{21}{4} x+\frac{45}{8},
$$
and the general solution is obtained by adding on $y_{h}$.

EXAMPLE 10 The method of undetermined coefficients
Use the method of undetermined coefficients to find the general solution of
$$
y^{\prime \prime}-3 y^{\prime}+2 y=e^{x} \cos x
$$

Solution According to (9), we take $y_{p}=A e^{x} \cos x+B e^{x} \sin x$. Since ne these terms appears in the expression of $y_{h}$ (see Example 9), there is no n modification. Now $y_{p}^{\prime}=(A+B) e^{x} \cos x+(-A+B) e^{x} \sin x$ and $y_{p}^{\prime \prime}=2 B e^{x} 2 A e^{x} \sin x$, and hence
$$
y_{p}^{\prime \prime}-3 y_{p}^{\prime}+2 y_{p}=-(A+B) e^{x} \cos x+(A-B) e^{x} \sin x .
$$

For $y_{p}$ to be a solution, we must solve $A+B=-1$ and $A-B=0$. From get $y_{p}=-\frac{1}{2} e^{x} \cos x-\frac{1}{2} e^{x} \sin x$ and hence the general solution is
$$
y=c_{1} e^{x}+c_{2} e^{2 x}-\frac{1}{2} e^{x}(\cos x+\sin x) .
$$

EXAMPLE 11 Using the superposition rule
Consider the equation $y^{\prime \prime}+4 y=e^{-2 x}+3 \sin 2 x$. It is easy to see that
$$
y_{h}=c_{1} \cos 2 x+c_{2} \sin 2 x .
$$

The term $e^{-2 x}$ requires a term $A e^{-2 x}$ in $y_{p}$. The term $3 \sin 2 x$ suggests the sion $B \cos 2 x+C \sin 2 x$. but because these terms appear in $y_{h}$ we must in

---

<!-- Page 19 -->

Right margin note (page 19)

A19
ce we
ation have terms
0.
0.
D.
0.
nethod
$n$ and e sure

++++

Section A. 2 Linear Ordinary Differential Equations with Constant Coefficients
an extra factor of $x$ (the characteristic polynomial has distinct roots). take
$$
y_{p}=A, \quad 2 x+B x \cos 2 x+C x \sin 2 x .
$$

Solving for $A, B$, and $C$ as before, we find $y_{p}=\frac{1}{8} e^{-2 x}-\frac{3}{4} x \cos 2 x$.
Note that even though the nonhomogeneous term $g(x)$ in the equ of Example 11 has no cosine term in it, the particular solution does one. This emphasizes the necessity of including both cosine and sine in $y_{p}$ even when only one of these appears in $g(x)$.

Exercises A. 2
In Excreises 1-24, find the general solution of the given equation.
1. $y^{\prime \prime}-4 y^{\prime}+3 y=0$.
2. $y^{\prime \prime}-y^{\prime}-6 y=0$.
3. $y^{\prime \prime}-5 y^{\prime}+6 y=0$.
4. $2 y^{\prime \prime}-3 y^{\prime}+y=0$.
$5 y^{\prime \prime}+2 y^{\prime}+y=0$.
6. $4 y^{\prime \prime}-13 y^{\prime}+9 y=$
7. $4 y^{\prime \prime}-4 y^{\prime}+y=0$.
8. $4 y^{\prime \prime}-12 y^{\prime}+9 y=0$.
9. $y^{\prime \prime}+y=0$.
10. $9 y^{\prime \prime}+4 y=0$.
11. $y^{\prime \prime}-4 y=0$.
12. $y^{\prime \prime}+3 y^{\prime}+3 y=0$
13. $y^{\prime \prime}+4 y^{\prime}+5 y=0$.
14. $y^{\prime \prime}-2 y^{\prime}+5 y=0$.
15. $y^{\prime \prime}+6 y^{\prime}+13 y=$
16. $2 y^{\prime \prime}-6 y^{\prime}+5 y=0$.
17. $y^{\prime \prime \prime}-2 y^{\prime \prime}+y^{\prime}=0$.
18. $y^{\prime \prime \prime}-3 y^{\prime \prime}+2 y=$
19. $y^{(4)}-2 y^{\prime \prime}+y=0$.
20. $y^{(4)}-y=0$.
21. $y^{\prime \prime \prime}-3 y^{\prime \prime}+3 y^{\prime}-y=0$.
22. $y^{\prime \prime \prime}+y=0$.
23. $y^{(4)}-6 y^{\prime \prime}+8 y^{\prime}-3 y=0$.
24. $y^{(4)}+4 y^{\prime \prime \prime}+6 y^{\prime \prime}+4 y^{\prime}+y=$

In Exercises 25-44, find the general solution of the given equation using the 1 , of undetermined coefficients.
25. $y^{\prime \prime}-4 y^{\prime}+3 y=e^{2 x}$.
26. $y^{\prime \prime}-y^{\prime}-6 y=e^{x}$.
27. $y^{\prime \prime}-5 y^{\prime}+6 y=e^{x}+x$.
28. $2 y^{\prime \prime}-3 y^{\prime}+y=e^{2 x}+\sin x$.
29. $y^{\prime \prime}-4 y^{\prime}+3 y=x e^{-x}$.
30. $y^{\prime \prime}-4 y=\cosh x$.
31. $y^{\prime \prime}+4 y=\sin ^{2} x$.
32. $y^{\prime \prime}+4 y=x \sin 2 x$.
33. $y^{\prime \prime}+y=\cos ^{2} x$.
34. $y^{\prime \prime}+2 y^{\prime}+2 y=e^{-x} \cos x$.
35. $y^{\prime \prime}+2 y^{\prime}+y=e^{-x}$.
36. $y^{\prime \prime}+2 y^{\prime}+y=x e^{-x}+6$.
37. $y^{\prime \prime}-y^{\prime}-2 y=x^{2}-4$.
38. $y^{\prime \prime}+y^{\prime}-2 y=2 x^{2}+x e^{x}$.
39. $y^{\prime}+2 y=2 x+\sin x$.
40. $y^{\prime}+2 y=\sin x$.
41. $2 y^{\prime}-y=e^{2 x}$.
42. $y^{\prime}-7 y=e^{\prime x}+\cos x$.
43. $y^{\prime \prime}+9 y=\sum_{n=1}^{6} \frac{\sin n \cdot r}{n}$.
44. $y^{\prime \prime}+y=\sum_{n=1}^{6} \frac{\sin 2 n x}{\prime \prime}$.

In Exercises 45-54, find the solution of the associated homogeneous equatic state the form of a particular solution. Do not solve for the coefficients. to modify by $x$ or $x^{2}$ as appropriate.
45. $y^{\prime \prime}-4 y^{\prime}+3 y=e^{2 x} \sinh x$.
46. $y^{\prime \prime}-4 y^{\prime}+3 y=e^{x} \sinh 2 x$.
47. $y^{\prime \prime}+2 y^{\prime}+2 y=\cos x+6 x^{2}-e^{-x} \sin x$.

---

<!-- Page 20 -->

Left margin note (page 20)

A20
Appendix A
O

Right margin note (page 20)

arbi-
ses.
$$
g(x) d x
$$
mant
e that
ct (see
$\left.\lambda_{n} x\right) \neq$

++++

rdinary Differential Equations: Review of Concepts and Methods
48. $y^{(1)}-y=\cosh x+\cosh 2 x$.
49. $y^{\prime \prime}-3 y^{\prime}+2 y=3 x^{1} c^{r}+x e^{-2 x} \cos 3 x$.
50. $y^{\prime \prime}-3 y^{\prime}+2 y=x^{4},{ }^{s}+7 x^{2},{ }^{2 x}$.
51. $y^{\prime \prime}+4 y=e^{2 x}(\sin 2 x+2 \cos 2 x)$.
52. $y^{\prime \prime}+4 y=x \sin 2 x+2 e^{2 x} \cos 2 x$.
53. $y^{\prime \prime}-2 y^{\prime \prime}+y=6 x-e^{x}$.
54. $y^{\prime \prime}-3 y^{\prime}+2 y=\epsilon^{x}+3 e^{-2 x}$.

In Exercises 55-60, find the general solution of the given equation. Since a trary parumeter appears in the equation, you have to distinguish separate ca
55. $y^{\prime \prime}-4 y^{\prime}+3 y=e^{\alpha x}$.
56. $y^{\prime \prime}-4 y^{\prime}+4 y=e^{\alpha x}$.
57. $y^{\prime \prime}+4 y=\cos \omega x$.
58. $y^{\prime \prime}+9 y=\sin \omega x$.
59. $y^{\prime \prime}+\omega^{2} y=\sin 2 x$.
60. $y^{\prime \prime}+b y^{\prime}+y=\sin x$.

In Exercises 61-70, solve the given initial value problem.
61. $y^{\prime \prime}-4 y=0, \quad y(0)=0, y^{\prime}(0)=3$.
62. $y^{\prime \prime}+2 y^{\prime}+y=0, \quad y(0)=2, y^{\prime}(0)=-1$.
63. $4 y^{\prime \prime}-4 y^{\prime}+y=0, \quad y(0)=-1, y^{\prime}(0)=1$.
64. $y^{\prime \prime}+y=0, \quad y(\pi)=1, y^{\prime}(\pi)=0$.
65. $y^{\prime \prime}-5 y^{\prime}+6 y=e^{x}, \quad y(0)=0, y^{\prime}(0)=0$.
66. $2 y^{\prime \prime}-3 y^{\prime}+y=\sin x, \quad y(0)=0, y^{\prime}(0)=0$.
67. $y^{\prime \prime}-4 y^{\prime}+3 y=x e^{-x}, \quad y(0)=0, y^{\prime}(0)=1$.
68. $y^{\prime \prime}-4 y=\cosh x, \quad y(0)=1, y^{\prime}(0)=0$.
69. $y^{\prime \prime}+4 y=\cos 2 x, \quad y(\pi / 2)=1, y^{\prime}(\pi / 2)=0$.
70. $y^{\prime \prime}+9 y=\sum_{n=1}^{6} \frac{\sin n x}{n}, \quad y(0)=0, y^{\prime}(0)=2$.

Integrals via undetermined coefficients. In Exercises 71-74, compute $\int$ by solving $y^{\prime}=g(x)$ using the method of undetermined coefficients.
71. $g(x)=e^{x} \sin x$.
72. $e^{x} \cos 2 x$.
73. $g(x)=e^{a x} \cos b x$.
74. $e^{a x} \sin b x$.

Given $n$ numbers $\lambda_{1}, \lambda_{2}, \ldots, \lambda_{n}$, we define the Vandermonde detern $V\left(\lambda_{1}, \lambda_{2}, \ldots, \lambda_{n}\right)$ to be
$$
\left|\begin{array}{cccc}
1 & 1 & \ldots & 1 \\
\lambda_{1} & \lambda_{2} & \ldots & \lambda_{n} \\
\vdots & \vdots & \vdots & \vdots \\
\lambda_{1}^{n-1} & \lambda_{2}^{n-1} & \ldots & \lambda_{n}^{n-1}
\end{array}\right| .
$$
75. Compute $V\left(\lambda_{1}, \lambda_{2}\right)$ and show that it is nonzero if and only if $\lambda_{1} \neq \lambda_{2}$.
76. Show that $V\left(\lambda_{1}, \lambda_{2}, \lambda_{3}\right)=\left(\lambda_{3}-\lambda_{2}\right)\left(\lambda_{3}-\lambda_{1}\right)\left(\lambda_{2}-\lambda_{1}\right)$ and conclud $V\left(\lambda_{1}, \lambda_{2}, \lambda_{3}\right) \neq 0$ if and only if all the $\lambda$ 's are distinct.
77. It is a fact that $V\left(\lambda_{1}, \lambda_{2}, \ldots, \lambda_{n}\right) \neq 0$ if and only if all the $\lambda$ 's are distin Exercise 78). Use this fact to prove that the Wronskian $W\left(e^{\lambda_{1} x}, \epsilon^{\lambda_{2} x}, \ldots, e\right.$ 0 if all the $\lambda$ 's are distinct.

---

<!-- Page 21 -->

Left margin note (page 21)

A. 3 Linear with No

Note that the equat standard form. Tha leading coefficient is

REDUCTI ORDER FOR

Before you apply this be sure that your eq in standard form.

Right margin note (page 21)

A21
your stinct. condiated ained s are neral The an be e the equaod of nd $y_{2}$
fixed e will
nearly that

++++

Section A. 3 Linear Ordinary Differential Fiquations with Nonconstant Coefficients
78. (a) Based on Exercise 76, guess the formula for $V\left(\lambda_{1}, \lambda_{2}, \ldots, \lambda_{n}\right)$. Verify guess for $n=2,3,4$.
(b) Using (a), show that $V\left(\lambda_{1}, \lambda_{2}, \ldots, \lambda_{n}\right) \neq 0$ if and only if all the $\lambda$ 's are dis

Ordinary Differential Equations nconstant Coefficients

In the previous two sections we saw that the general solution of the se order linear differential equation
$$
y^{\prime \prime}+p(x) y^{\prime}+q(x) y=g(x)
$$
is of the form $y=y_{h}+y_{p}$, where $y_{h}$ is the general solution of the assoc homogeneous equation and $y_{p}$ is any particular solution of (1). We obt a complete description of the solution when the coefficient function constants and $g$ is of a special form. In this section we present two ge methods for handling the cases not covered by the previous section. first one is usually applied when solving for $y_{h}$, and the second one cand used to find $y_{p}$. We end the section by applying these methods to solv important class of Euler equations.

Reduction of Order
For second-order linear differential equations, we know that
$$
y_{h}=c_{1} y_{1}+c_{2} y_{2},
$$
where $y_{1}$ and $y_{2}$ are linearly independent solutions of the homogeneous tion
ion is in t is, the 1.

ON OF MULA
formula, nation is
$$
y^{\prime \prime}+p(x) y^{\prime}+q(: r) y=0 .
$$

Suppose that we know one nontrivial solution to (2), say $y_{1}$. The meth reduction of order allows us to find a second solution $y_{2}$ such that $y_{1}$ a are independent.

A second linearly independent solution of (2) given $y_{1}$ is
$$
y_{2}=y_{1} \int \frac{e^{-\int p(x) d x}}{y_{1}^{2}} d x .
$$

Since we are sccking only one independent solution, we can assign any values to the constants of integration appearing in this formula. W often neglect these constants.

Proof We know that $c y_{1}$ is a solution of (2). But of course this solution is li dependent with $y_{1}$. The idca is to find a nonconstant function $\eta(x)$ such

---

<!-- Page 22 -->

Left margin note (page 22)

A22 Appendix A

![](./images/66923605-2b3e-4154-b144-3e182be82ea5-22_418_477_1169_58.jpg)

Figure 1 Solutions ple 1.
$$
\begin{array}{l}
\int x e^{-x} d x \\
\quad=-x e^{-x}-e
\end{array}
$$

Right margin note (page 22)

$y_{1}{ }^{v}$
1) $v$
(2), $v$
(hence
erested
The
n. See
□
st
endent.
□

We
scond
order
endent
form.

++++

Ordinary Differential Equations: Review of Concepts and Methods

$v(x) y_{1}$ is a solution. Substituting $y=v(x) y_{1}$ into (2), we get
$$
\begin{aligned}
y^{\prime \prime}+p(x) y^{\prime}+q(x) y & =\left(y_{1} v^{\prime \prime}+2 y_{1}^{\prime} v^{\prime}+y_{1}^{\prime \prime} v\right)+p(x)\left(y_{1} v^{\prime}+y_{1}^{\prime} v\right)+q(x) \\
& \left.=y_{1} v^{\prime \prime}+\left(2 y_{1}^{\prime}\right) p(x) y_{1}\right) v^{\prime}+\left(y_{1}^{\prime \prime}+p(x) y_{1}^{\prime}+q(x) y\right. \\
& =y_{1} v^{\prime \prime}+\left(2 y_{1}^{\prime}+p(x) y_{1}\right) v^{\prime}
\end{aligned}
$$
because $y_{1}^{\prime \prime}+p(x) y_{1}^{\prime}+q(x) y_{1}=0$. Hence, for $y=v y_{1}$ to be a solution to must satisfy $y_{1} v^{\prime \prime}+\left(2 y_{1}^{\prime}+p(x) y_{1}\right) v^{\prime}=0$. This is a first-order equation in $v^{\prime}$ the name reduction of order). Equivalently,
$$
v^{\prime \prime}+\left(2 \frac{y_{1}^{\prime}}{y_{1}}+p(x)\right) v^{\prime} \cdots 0,
$$
and thus by Theorem 1, Section A.1, we find
$$
v^{\prime}(x)=\frac{e^{-\int p(x) d x}}{y_{1}^{2}} .
$$
(We have taken the constant in this theorem to be 1 , since we are only int in one solution.) Hence (3) follows by integrating and multiplying by $y_{1}$ linear independence of $y_{1}$ and $y_{2}$ can be checked by computing the Wronskia Exercise 41.

EXAMPLE 1 Reduction of order in the presence of a double roc
Given that $y_{1}=e^{x}$ is a solution to $y^{\prime \prime}-2 y^{\prime}+y=0$, a second linearly indep
solution is obtained from (3), as follows (Figure 1):
$$
y_{2}=e^{x} \int \frac{e^{2 x}}{\left(e^{x}\right)^{2}} d x=x e^{x}
$$

The characteristic equation in Example 1 has 1 as a double root could have used the methods of the previous section to write down thes solution. However, the point of Example 1 is to show how reduction of can be used to derive such solutions.

EXAMPLE 2 Applying the reduction of order formula
Given that $c^{r}$ is a solution of $x y^{\prime \prime}-(1+x) y^{\prime}+y=0$, a second linearly indep solution is obtained by appealing to (3). We have
$$
y_{2}=e^{x} \int \frac{e^{\rho\left(\frac{1}{i}+1\right) d x}}{\left(e^{x}\right)^{2}} d x=e^{x} \int \frac{x^{x}}{\left(e^{x}\right)^{2}} d x=e^{x} \int x e^{x} d x
$$

Observe that before evaluating (3), we must put the equation in standare Integrating by parts, we find
$$
y_{2}=e^{x}\left(-x e^{-x}-e^{-x}\right)=-x-1 .
$$

At this point, we may use $y_{2}=x+1$.

---

<!-- Page 23 -->

Left margin note (page 23)

VARIATION OF PARAMETERS FORMULA

Right margin note (page 23)

A23

mogeicular
$$
\left., y_{2}\right)=
$$

inte-

ope is of the
uation As you
) $y_{2}$ )
$y_{2}^{\prime}$.
$y_{1}$ and

++++

Section A. 3 Linear Ordinary Differential Equations with Nonconstant Coefficients

Variation of Parameters
In this part, we suppose that we know the solution of the associated ho neous equation (2) and describe a general method for generating a part solution of (1). This method is called variation of parameters.

A particular solution of (1) is given by
$$
y_{p}=y_{1} \int \frac{-y_{2} g(x)}{W\left(y_{1}, y_{2}\right)} d x+y_{2} \int \frac{y_{1} g(x)}{W\left(y_{1}, y_{2}\right)} d x
$$
where $y_{1}$ and $y_{2}$ are linearly independent solutions of (2), and $W\left(y_{1}\right. y_{1} y_{2}^{\prime}-y_{1}^{\prime} y_{2}$ is the Wronskian of $y_{1}$ and $y_{2}$.

As in the reduction of order method, we can neglect the constants of gration.
Proof Since $c_{1} y_{1}+c_{2} y_{2}$ is a solution of the homogencous equation, our 1 that by allowing functions instead of constants we can generate a solution nonhomogeneous equation. We thus try
$$
y=u_{1}(x) y_{1}+u_{2}(x) y_{2}
$$
and solve for $u_{1}$ and $u_{2}$. Since we have two unknown functions and only one eq to satisfy, we are free to impose one additional relation between $u_{1}$ and $u_{2}$. will see, the following condition simplifies the computation:
$$
u_{1}^{\prime}(x) y_{1}+u_{2}^{\prime}(x) y_{2}=0
$$

We now compute using (5) and (6):
$$
y^{\prime}=u_{1}(x) y_{1}^{\prime}+u_{2}(x) y_{2}^{\prime} ; \quad y^{\prime \prime}=u_{1}(x) y_{1}^{\prime \prime}+u_{2}(x) y_{2}^{\prime \prime}+u_{1}^{\prime}(x) y_{1}^{\prime}+u_{2}^{\prime}(x) y_{2}^{\prime}
$$

Substituting these and (5) in the left side of (1) we get
$$
\begin{aligned}
y^{\prime \prime}+p(x) y^{\prime}+q(x) y= & \left(u_{1}(x) y_{1}^{\prime \prime}+u_{2}(x) y_{2}^{\prime \prime}+u_{1}^{\prime}(x) y_{1}^{\prime}+u_{2}^{\prime}(x) y_{2}^{\prime}\right) \\
& +p(x)\left(u_{1}(x) y_{1}^{\prime}+u_{2}(x) y_{2}^{\prime}\right)+q(x)\left(u_{1}(x) y_{1}+u_{2}(x)\right. \\
= & u_{1}(x) \underbrace{\left(y_{1}^{\prime \prime}+p(x) y_{1}^{\prime}+q(x) y_{1}\right)}_{=0} \\
& +u_{2}(x) \underbrace{\left(y_{2}^{\prime \prime}+p(x) y_{2}^{\prime}+q(x) y_{2}\right)}_{=0}+u_{1}^{\prime}(x) y_{1}^{\prime}+u_{2}^{\prime}(x)
\end{aligned}
$$

Therefore, recalling (6), we will have a solution if $u_{1}$ and $u_{2}$ satisfy
$$
\left\{\begin{array}{l}
y_{1} u_{1}^{\prime}(x)+y_{2} u_{2}^{\prime}(x)=0 \\
y_{1}^{\prime} u_{1}^{\prime}(x)+y_{2}^{\prime} u_{2}^{\prime}(x)=g(x) .
\end{array}\right.
$$

The determinant of this system is precisely $W\left(y_{1}, y_{2}\right)$, which is nonzero since $y_{2}$ are linearly independent. Solving this system, we get the unique solution
$$
u_{1}^{\prime}=\frac{-y_{2} g(x)}{W\left(y_{1}, y_{2}\right)} \quad \text { and } \quad u_{2}^{\prime}=\frac{y_{1} g(x)}{W\left(y_{1}, y_{2}\right)}
$$

---

<!-- Page 24 -->

Left margin note (page 24)

A24 Appendix A Ordinary

Right margin note (page 24)

icular
tions simstant first${ }^{\alpha}$, we
st be ey to ey to tions ts. cients the most ss, in cases

++++

Differential Equations: Review of Concepts and Methods

Integrating and substituting in (5) yields (4).

EXAMPLE 3 Variation of parameters
Given that $y_{1}=x$ and $y_{2}=x^{4}$ are solutions of $x^{2} y^{\prime \prime}-4 x y^{\prime}+4 y=0$, find a part solution of
$$
x^{2} y^{\prime \prime}-4 x y^{\prime}+4 y=3 x^{2}
$$

Solution We have
$$
W\left(y_{1}, y_{2}\right)=W\left(x, x^{4}\right)=3 x^{4}
$$

We put the equation in standard form, apply (4), and get
$$
y_{p}=x \int \frac{-3 x^{4}}{3 x^{4}} d x+x^{4} \int \frac{3 x}{3 x^{4}} d x=-x^{2}-\frac{1}{2} x^{2}=-\frac{3}{2} x^{2}
$$

We end this section with a discussion of a class of differential equa with important applications.

Euler Equations
The differential equation
$$
x^{2} y^{\prime \prime}+\alpha x y^{\prime}+\beta y=0
$$
where $\alpha$ and $\beta$ are constants, is known as Euler's equation. It is the plest example of a second-order linear differential equation with noncon coefficients for which we have an explicit solution. Motivated by the order version of this equation, $x y^{\prime}+\alpha y=0$, which has solution $y=x^{-}$ try
$$
y=x^{r}
$$
as a solution of (7). Plugging $x^{r}$ into the equation, it follows that $r$ mu a root of
$$
r(r-1)+\alpha r+\beta=0
$$

This quadratic equation, known as the indicial equation, is the k solving (7), in the same way that the characteristic equation is the $k$ solving an equation with constant coefficients. As expected, the solu will depend on the nature of the roots, referred to as the indicial roo

If we put the general Euler's equation in standard form, the coeffic of $y^{\prime}$ and $y$ are not defined at $x=0$. Because of this problem at cases $x>0$ and $x<0$ are to be treated separately. In fact, in applications we are only interested in the case $x>0$. For completene the following box we present the solution of Euler's equation in both using the absolute value.

---

<!-- Page 25 -->

Left margin note (page 25)

GEN
SOLUTIC
EULER'S EQUA

Right margin note (page 25)

A25
te as
equa-
then
and d via
$r_{1}+$
blying
mally
oceed
orevi-teriseft as
and ge of with

++++

Section A. 3 Lincar Ordinary Differential Equations with Nonconstant Coefficients
ERAL

Consider Euler's equation (7) with indicial equation (9), which we wri

N OF
TION
$$
r^{2}+(\alpha-1) r+\beta=0
$$

Let $r_{1}$ and $r_{2}$ denote the indicial roots. The general solution $y$ of this tion is given by the following cases.
Case I If $r_{1}$ and $r_{2}$ are distinct real roots, then
$$
y=c_{1}|x|^{r_{1}}+c_{2}|x|^{r_{2}}
$$

Case II If $r_{1}=r_{2}$, then
$$
y=\left(c_{1}+c_{2} \ln |x|\right)|x|^{r_{1}}
$$

Case III If $r_{1}$ and $r_{2}$ are complex conjugate roots with $r_{1}=a+i b$,
$$
y=|x|^{a}\left[c_{1} \cos (b \ln |x|)+c_{2} \sin (b \ln |x|)\right]
$$

Clearly when $x>0$ we may drop the absolute values.
Proof For clarity's sake, we take $x>0$. Case I follows immediately from (8 the fact that $W\left(x^{r_{1}}, x^{r_{2}}\right)=\left(r_{2}-r_{1}\right) x^{r_{1}+r_{2}-1} \neq 0$ for $x>0$. Case II is derive reduction of order. Using $y_{1}=x^{r_{1}}$ in (3), we get
$$
y_{2}=x^{r_{1}} \int \frac{e^{-\int \frac{\alpha}{x} d x}}{x^{2 r_{1}}} d x=x^{r_{1}} \int x^{-\alpha-2 r_{1}} d x
$$

But because $r_{1}$ is a double root of the indicial equation (10), we have $2 r_{1}= r_{2}=-(\alpha-1)$. So $x^{-\alpha-2 r_{1}}=x^{-1}$, and the integral evaluates to $\ln x$, imp $y=x^{r_{1}} \ln x$.

In Case III, two linearly independent complex-valued solutions are for given by $x^{a+i b}$ and $x^{a-i b}$. We interpret these as $e^{\ln x(a+i b)}$ and $e^{\ln x(a-i b)}$ and pr to derive real-valued solutions. From Euler's identity, we have
$$
e^{\ln x(a+i b)}=e^{a \ln x} e^{i b \ln x}=x^{a}[\cos (b \ln x)+i \sin (b \ln x)]
$$
and, similarly,
$$
e^{\ln x(a-i b)}=x^{a}[\cos (b \ln x)-i \sin (b \ln x)]
$$

Taking linear combinations, we arrive at the desired real solutions as we did ously when dealing with constant coefficient equations having complex charac tic roots. Linear independence follows by computing the Wronskian and is 1 Exercise 42.

There is a close similarity between the solution to Euler's equation the solution to the constant coefficient equation. Indeed, the chan variables $t=\ln x$ in Euler's equation transforms it to an equation

---

<!-- Page 26 -->

Left margin note (page 26)

A26
Appendix A

![](./images/66923605-2b3e-4154-b144-3e182be82ea5-26_470_470_331_63.jpg)

Figure 2 Solutions ple 4. Notice that defined at $x=0$ : not differentiable a These solutions are $x>0$, where the equation is defined.

Right margin note (page 26)

general
indicial indicial $\frac{2}{2}$. The
ruation.

++++

Ordinary Differential Equations: Review of Concepts and Methods

constant coefficients. This provides an alternative derivation of the $\varepsilon$ solution of Euler's equation. See Exercise 43.

EXAMPLE 4 Euler's equation
Solve $2 x^{2} y^{\prime \prime}+5 x y^{\prime}-2 y=0$ for $x>0$.
Solution We rewrite the equation as $x^{2} y^{\prime \prime}+\frac{5}{2} x y^{\prime}-y=0$. From (10), the equation is $r^{2}+\frac{3}{2} r-1=0$, which factors as $\left(r-\frac{1}{2}\right)(r+2)=0$. We get the roots $r_{1}=\frac{1}{2}, r_{2}=-2$. Thus by Case I, the general solution is $y=c_{1} \sqrt{x}+\frac{c}{x}$ general solution is illustrated in Figure 2.
in Exam$\frac{1}{x^{2}}$ is not and $\sqrt{x}$ is t $x=0$. valid for lifferential

Note that when $x<0$, the solution in Example 4 becomes
$$
y=c_{1} \sqrt{-x}+\frac{c_{2}}{x^{2}} .
$$

Exercises A. 3
In Exercises 1-20, verify that the given function is a solution of the given eq and then find the general solution using the reduction of order formula.
1. $y^{\prime \prime}+2 y^{\prime}-3 y=0, \quad y_{1}=e^{x}$.
2. $y^{\prime \prime}-5 \cdot y^{\prime}+6 y=0, \quad y_{1}=e^{3 x}$.
3. $x y^{\prime \prime}-(3+x) y^{\prime}+3 y=0, \quad y_{1}=e^{x}$.
4. $x y^{\prime \prime}-(2-x) y^{\prime}-2 y=0, \quad y_{1}=e^{-x}$.
5. $y^{\prime \prime}+4 y=0, \quad y_{1}=\cos 2 x$.
6. $y^{\prime \prime}+9 y=0, \quad y_{1}=\sin 3 x$.
7. $y^{\prime \prime}-y=0, \quad y_{1}=\cosh x$.
8. $y^{\prime \prime}+2 y^{\prime}+y=0, \quad y_{1}=e^{-x}$.
9. $\left(1-x^{2}\right) y^{\prime \prime}-2 x y^{\prime}+2 y=0, \quad y_{1}=x$.
10. $\left(1-x^{2}\right) y^{\prime \prime}-2 x y^{\prime}=0, \quad y_{1}=1$.
11. $x^{2} y^{\prime \prime}+x y^{\prime}-y=0, \quad y_{1}=x$.
12. $x^{2} y^{\prime \prime}-x y^{\prime}+y=0, \quad y_{1}=x$.
13. $x^{2} y^{\prime \prime}+x y^{\prime}+y=0, \quad y_{1}=\cos (\ln x)$.
14. $x^{2} y^{\prime \prime}+2 x y^{\prime}+\frac{1}{4} y=0, \quad y_{1}=1 / \sqrt{x}$.
15. $x y^{\prime \prime}+2 y^{\prime}+4 x y=0, \quad y_{1}=\frac{\sin 2 x}{x}$.
16. $x y^{\prime \prime}+2 y^{\prime}-x y=0, \quad y_{1}-\frac{e^{x}}{x}$.
17. $x y^{\prime \prime}+2(1-x) y^{\prime}+(x-2) y=0, \quad y_{1}=e^{x}$.
18. $(x-1)^{2} y^{\prime \prime}-3(x-1) y^{\prime}+4 y=0, \quad y_{1}=(x-1)^{2}$.
19. $x^{2} y^{\prime \prime}-2 x y^{\prime}+2 y=0, \quad y_{1}=x^{2}$.
20. $\left(x^{2}-2 x\right) y^{\prime \prime}-\left(x^{2}-2\right) y^{\prime}+2(x-1) y=0, \quad y_{1}=e^{x}$.

---

<!-- Page 27 -->

Right margin note (page 27)

A27
nethod
erwise

ion of that $x>0$. uation ad the Euler's uation
ise we eneous given aram-

++++

Section A. 3 Linear Ordinary Differential Equations with Nonconstant Cocfficients

In Exercises 21-30, find the general solution of the given equation using the $n$ of variation of parameters. Take $x>0$.
21. $y^{\prime \prime}-4 y^{\prime}+3 y=e^{-x}$.
22. $y^{\prime \prime}-15 y^{\prime}+56 y=c^{7 x}+12 x$.
23. $3 y^{\prime \prime}+13 y^{\prime}+10 y=\sin x$.
24. $y^{\prime \prime}+3 y=x$.
25. $y^{\prime \prime}+y=\sec x$.
26. $y^{\prime \prime}+y=\sin x+\cos x$.
27. $x y^{\prime \prime}-(1+x) y^{\prime}+y=x^{3}$.
28. $x y^{\prime \prime}-(1+x) y^{\prime}+y=x^{4} e^{\prime \prime}$.
[Hint: $y_{1}=1+x, y_{2}=e^{x}$.]
[Hint: Exercise 27.]
29. $x^{2} y^{\prime \prime}+3 x y^{\prime}+y=\sqrt{x}$.
30. $x^{2} y^{\prime \prime}+x y^{\prime}+y=x$.

In Exercises 31-40, solve the given Euler equation. Take $x>0$, unless oth stated.
31. $x^{2} y^{\prime \prime}+4 x y^{\prime}+2 y=0$.
32. $x^{2} y^{\prime \prime}+x y^{\prime}-4 y=0$.
33. $x^{2} y^{\prime \prime}+3 x y^{\prime}+y=0$.
34. $4 x^{2} y^{\prime \prime}+8 x y^{\prime}+y=0$.
35. $x^{2} y^{\prime \prime}+x y^{\prime}+4 y=0$.
36. $4 x^{2} y^{\prime \prime}+4 x y^{\prime}+y=0$.
37. $x^{2} y^{\prime \prime}+7 x y^{\prime}+13 y=0$.
38. $x^{2} y^{\prime \prime}-x y^{\prime}+5 y=0$.
39. $(x-2)^{2} y^{\prime \prime}+3(x-2) y^{\prime}+y=0$
40. $(x+1)^{2} y^{\prime \prime}+(x+1) y^{\prime}+y=0$
$(x>2)$.
$(x>-1)$.
[Hint: Let $t=x-2$.]
[Hint: Let $t=x+1$.]
41. Compute $W\left(y_{1}, y_{2}\right)$ with $y_{2}$ given by (3) and conclude that the reduct order formula yields a second linearly independent solution.
42. Let $y_{1}$ and $y_{2}$ be the solutions of Euler's equation in Case III. Shov $W\left(y_{1}, y_{2}\right)=x^{2 a-1}$ and conclude that $y_{1}$ and $y_{2}$ are linearly independent for
43 Show that the change of variables $t=\ln x(x>0)$ transforms Euler's eq (7) to the equation
$$
\frac{d^{2} y}{d t^{2}}+(\alpha-1) \frac{d y}{d t}+\beta y=0
$$
with constant coefficients.
44. An alternative solution of Euler's equation. Using Exercise 43 ar solution of (6), Section A.2, derive the three cases of the general solution of equation.
45. Reduction of order formula from Abel's formula.
(a) Use Abel's formula (Theorem 2, Section A.1) to conclude that
$$
y_{1} y_{2}^{\prime}-y_{1}^{\prime} y_{2}=C e^{-\int p(x) d x}
$$
where $y_{1}$ and $y_{2}$ are any two solution of (2).
(b) Given $y_{1}$, set $C=1$ in (a) and solve the resulting first-order differential eq in $y_{2}$, thereby deriving (3).
46. Reduction of order for nonhomogeneous equations. In this exerc demonstrate that the method of reduction of order also applies to nonhomog equations given a solution $y_{1}$ to the associated homogeneous equation. Thus, $y_{1}$, we may solve (1) directly without recourse to the method of variation of p eters.

---

<!-- Page 28 -->

Left margin note (page 28)

A28
Appendix A
A. 4 The Po

Right margin note (page 28)

rive at eneral tive of ng the at you uding such basic eeded
aid to mpler
is the uch $x$ esents

++++

Ordinary Differential Equations: Review of Concepts and Methods
(a) Show that if we want to solve (1) and carry out the proof of (3) we ar the equation
$$
v^{\prime \prime}+\left(\frac{y_{1}^{\prime}}{y_{1}}+p(x)\right) v^{\prime}=\frac{g(x)}{y_{1}} .
$$
(b) Solve the equation using Theorem 1, Section A.1, and conclude that the g solution of (1) is
$$
\begin{aligned}
y= & c_{1} y_{1}+c_{2} y_{1} \int \frac{e^{-\int p(x) d x}}{y_{1}^{2}} d x \\
& +y_{1} \int \frac{e^{-\int p(x) d x}}{y_{1}^{2}} d x\left(\int y_{1} e^{\int p(x) d x} g(x) d x\right) d x
\end{aligned}
$$
where the last two occurrences of $\int p(x) d x$ represent the same antideriva $p(x)$.

In Exercises 47-50, find the general solution of the given equation by usi method of Exerrise 46. To get a good feel for Exercise 46, we suggest th repeat its proof with at least one of the following exercises.
47. $y^{\prime \prime}-4 y^{\prime}+3 y=e^{x}, \quad y_{1}=e^{x}$.
48. $x^{2} y^{\prime \prime}+3 x y^{\prime}+y=\sqrt{x}, \quad y_{1}=\frac{1}{x}$.
49. $3 y^{\prime \prime}+13 y^{\prime}+10 y=\sin x, \quad y_{1}=e^{-x}$.
50. $x y^{\prime \prime}-(1+x) y^{\prime}+y=x^{3}, \quad y_{1}=e^{x}$.
wer Series Method, Part I
Power series will be used to solve ordinary differential equations, incl many important differential equations with nonconstant coefficients. as the Legendre and Bessel equations. In this section we review the properties of power series, and present some techniques that will be $n$ in the next sections.

A power series is a series of the form
$$
\sum_{m=0}^{\infty} a_{m}(x-a)^{m}=a_{0}+a_{1}(x-a)+a_{2}(x-a)^{2}+\cdots,
$$
where $a, a_{0}, a_{1}, a_{2}, \ldots$ are constants and $x$ is a variable. The series is s be centered at $a$. If the series is centered at $a=0$, it takes on the si form
$$
\sum_{m=0}^{\infty} a_{m} x^{m}=a_{0}+a_{1} x+a_{2} x^{2}+\cdots
$$

Given the power series (1), we define a function $f(x)$ whose domain set of all $x$ for which the series converges, and whose value at every s is the sum of the series for that $x$. We say that the power series repr the function $f(x)$.

---

<!-- Page 29 -->

Left margin note (page 29)

Series converges for $|x-a|<R$.

![](./images/66923605-2b3e-4154-b144-3e182be82ea5-29_172_465_1523_49.jpg)

Figure 1 The interval of convergence of a power series centered at the point $x=a$. The series may converge or diverge at the endpoints $x=a \pm R$.

Right margin note (page 29)

A29
esen-
⋯ .
ts are
$f(a)$
ons of
series

all $x$.
values ce. If adius which re 1). series
terval ibe a

++++

Section A. 4 The Power Series Method, Part I

Recall from calculus that certain functions have a Taylor series repr tation centered at $x=a$ of the form
$$
f(x)=f(0)+\frac{f^{\prime}(a)}{1!}(x-a)+\frac{f^{\prime \prime}(a)}{2!}(x-a)^{2}+\cdots+\frac{f^{(k)}(a)}{k!}(x-a)+
$$

Thus a Taylor series is an example of a power series where the coefficien uniquely determined by $f(x)$ and its derivatives. In fact, we have $a_{0}$ and $a_{k}=f^{(k)}(a) / k!$. The following list gives Taylor series representatic some elementary functions, together with the domains for which the expansions are valid. All the series are centered at 0 .
$$
\begin{aligned}
\frac{1}{1-x} & =\sum_{m=0}^{\infty} x^{m}=1+x+x^{2}+x^{3}+\cdots, & & |x|<1 \\
\epsilon^{r} & =\sum_{m=0}^{\infty} \frac{x^{m}}{m!}=1+x+\frac{x^{2}}{2!}+\frac{x^{3}}{3!}+\cdots, & & -\infty<x<\infty \\
\sin x & =\sum_{m=0}^{\infty} \frac{(-1)^{m} x^{2 m+1}}{(2 m+1)!}=x-\frac{x^{3}}{3!}+\frac{x^{5}}{5!}-\cdots, & & -\infty<x<\infty \\
\cos x & =\sum_{m=0}^{\infty} \frac{(-1)^{m} x^{2 m}}{(2 m)!}=1-\frac{x^{2}}{2!}+\frac{x^{4}}{4!}-\cdots, & & -\propto<x<\infty \\
\ln (1+x) & =\sum_{m=1}^{\infty} \frac{(-1)^{m+1} x^{m}}{m}=x-\frac{x^{2}}{2}+\frac{x^{3}}{3}-\cdots, & & |x|<1 \\
\tan ^{-1} x & =\sum_{m=0}^{\infty} \frac{(-1)^{m} x^{2 m+1}}{2 m+1}=x-\frac{x^{3}}{3}+\frac{x^{5}}{5}-\cdots, & & |x| \div 1 \\
\sinh x & =\sum_{m=0}^{\infty} \frac{x^{2 m+1}}{(2 m+1)!}=x+\frac{x^{3}}{3!}+\frac{x^{5}}{5!}+\cdots, & & -\infty<x<\infty \\
\cosh x & =\sum_{m=0}^{\infty} \frac{x^{2 m}}{(2 m)!}=1+\frac{x^{2}}{2!}+\frac{x^{4}}{4!}+\cdots, & & -\infty<x<\infty
\end{aligned}
$$

As the preceding list indicates, a power series need not converge for We recall the following facts about the convergence of power series.
- The power series (1) always converges at its center $x=a$.
- If the series converges for values of $x$ other than $a$, then these form an interval centered at $a$, called the interval of convergen the interval is finite, then there is a number $R>0$, called the $\mathbf{r}$ : of convergence, such that the series converges at all $x$ for $|x-a|<R$, and diverges at all $x$ for which $|x-a|>R$ (Figu If the series converges only at $x=a$, we set $R=0$, and if the converges for all $x$, we set $R=\infty$.

A function defined by a power series is said to be analytic on the in of convergence. (In Section 12.5 we used the term analytic to descr

---

<!-- Page 30 -->

Left margin note (page 30)

A30
Appendix A
Ordinary

Right margin note (page 30)

ne. A valent n this is the e root
rgence rgence ned by $= \pm 2$. ollows: es to a
$\infty$, and

++++

Differential Equations: Review of Concepts and Methods
complex function that is differentiable in an open subset of the pla basic result from complex analysis tells us that this property is equi to having a power series expansion. So the usage of the term analytic section is consistent with our previous usage in Section 12.5.)

A useful test for finding the radius of convergence of a power series ratio test, as illustrated by the following examples. (In some cases th test may be more convenient.)

EXAMPLE 1 Radius and interval of convergence
Consider the power series
$$
\sum_{m=1}^{\infty} \frac{(-1)^{m} m}{4^{m}} x^{2 m}=-\frac{1}{4} x^{2}+\frac{1}{8} x^{4}-\frac{3}{64} x^{6}+\cdots
$$

Using the ratio test, we have that the series converges whenever the limit
$$
\lim _{m \rightarrow \infty}\left|\frac{(m+1)}{4^{m+1}} x^{2(m+1)} / \frac{m}{4^{m}} x^{2 m}\right|=\lim _{m \rightarrow \infty}\left(\frac{m+1}{4 m}\right) x^{2}=\frac{x^{2}}{4}
$$
is less than 1. That is, $x^{2} / 4<1$ or $x^{2}<4$. Thus, the interval of conve is $|x|<2$, or $(-2,2)$. Since the series is centered at 0 , the radius of conve is 2 . The behavior of the series at the endpoints, $x= \pm 2$, is not determit the ratio test. In this example, you can check that the series diverges at $x$ Thus we can define a function for all $x$ in $(-2,2)$ by the power series, as $f f(x)=\sum_{m=1}^{\infty} \frac{(-1)^{m} m}{4^{m}} x^{2 m}$. For each value of $x$ in $(-2,2)$, the series converg real number, which is $f(x)$.

EXAMPLE 2 A power series that converges for all $x$
Find the radius of convergence of the series
$$
\sum_{m=1}^{\infty} \frac{(-1)^{m+1}}{2^{m}(m!)^{2}} x^{m}=\frac{x}{2}-\frac{x^{2}}{16}+\frac{x^{3}}{288}-\cdots
$$

Solution Evaluating the limit obtained from the ratio test, we find
$$
\lim _{m \rightarrow \infty}\left|\frac{x^{m+1}}{2^{m+1}[(m+1)!]^{2}} / \frac{x^{m}}{2^{m}(m!)^{2}}\right|=\lim _{m \rightarrow \infty}\left(\frac{|x|}{2(m+1)^{2}}\right)=0
$$
for all $x$. Thus the series converges for all $x$. The radius of convergence is the interval of convergence is $(-\infty, \infty)$.

EXAMPLE 3 A power series that converges only at its center For the power series
$$
\sum_{m=1}^{\infty} m^{m}(x-1)^{m}=(x-1)+4(x-1)^{2}+27(x-1)^{3}+256(x-1)^{4}+\cdots
$$

---

<!-- Page 31 -->

Right margin note (page 31)

A31

rgent
mials term.
epre-
$$
>0,
$$
$x$ and
for
$$
+\cdots)
$$
⋯
$$
f \cdot g
$$

++++

Section A. 4 The Power Series Method, Part I

we use the root test and get
$$
\lim _{m \rightarrow \infty} \sqrt[m]{\left|m^{m}(x-1)^{m}\right|}=\lim _{m \rightarrow \infty} m|x-1|=\infty
$$
for all $x \neq 1$. Thus the series diverges for all $x \neq 1$. The series is clearly conve when $x=1$. The radius of convergence is 0 .

Operations on Power Series
Power series are like polynomials of "infinite degree," and like polyno they can be added, multiplied, differentiated, and integrated term-byWe now recall how these operations apply.

Linear Combinations and Products. Consider the power series sentations
$$
f(x)=\sum_{m=0}^{\infty} a_{m}(x-a)^{m} \quad \text { and } \quad g(x)=\sum_{m=0}^{\infty} b_{m}(x-a)^{\prime \prime \prime},
$$
with common center at $a$ and radii of convergence $R_{1}>0$ and $R_{2}$ respectively. Then it is not difficult to show that for any real numbers 3 , we have
$$
\alpha f(x)+\beta g(x)=\sum_{m=0}^{\infty}\left(\alpha a_{m}+\beta b_{m}\right)(x-a)^{m} .
$$

The multiplication of power series is done in much the same way polynomials:
$$
\begin{aligned}
f & (x) \cdot g(x) \\
& =\left(a_{0}+a_{1}(x-a)+a_{2}(x-a)^{2}+\cdots\right) \cdot\left(b_{0}+b_{1}(x-a)+b_{2}(x-a)^{2}\right. \\
& =a_{0}+b_{0}+\left(a_{0} b_{1}+a_{1} b_{0}\right)(x-a)+\left(a_{0} b_{2}+a_{1} b_{1}+a_{2} b_{0}\right)(x-a)^{2}+ \\
& =\sum_{m=0}^{\infty}\left(a_{0} b_{m}+a_{1} b_{m-1}+\cdots+a_{m} b_{0}\right)(x-a)^{m} .
\end{aligned}
$$

The power series of the linear combination $\alpha f+\beta g$ and the product have radii of convergence at least as large as the smaller of $R_{1}$ and $R_{2}$

Differentiation and Integration of Power Series. A power series
$$
f(x)=\sum_{m=0}^{\infty} a_{m}(x-a)^{m} \quad(|x-a|<R, R>0)
$$
can be differentiated term-by-term to yield
$$
f^{\prime}(x)=\sum_{m=1}^{\infty} m a_{m}(x-a)^{m-1} \quad(|x-a|<R) .
$$

---

<!-- Page 32 -->

Left margin note (page 32)

A32
Appendix A Ordinary

Right margin note (page 32)

e. The ergence ntiated to the in, and
$R$ ).
of $f(x)$ :
ence is al, you actions,
ed and $b, c]$ be

fulness
r series

++++

Differential Equations: Review of Concepts and Methods

Moreover, the series (4) and (5) have the same interval of convergenc proof is sketched in the exercises; it uses the notion of uniform conve and results about series of functions from Section 2.9. Since the differe series (5) is itself a power series with interval of convergence equal interval of convergence of the series (4), we can differentiate it aga again, and conclude that $f$ is infinitely differentiable.

If we differentiate the power series $k$ times, we find
$$
f^{(k)}(x)=\sum_{m=k}^{\infty} m(m-1) \cdots(m-k+1) a_{m}(x-a)^{m-k} \quad(|x-a|<
$$

Setting $x=a$, all the terms cancel, except for $m=k$, and we get
$$
f^{(k)}(a)=\overbrace{k(k-1) \cdots(k-k+1)}^{=k!} a_{k} \quad \Rightarrow \quad a_{k}=\frac{f^{(k)}(a)}{k!} .
$$

Substituting back into (4), we obtain the Taylor series expansion
$$
f(x)=\sum_{m=1}^{\infty} \frac{f^{(k)}(a)}{m!}(x-a)^{m} \quad(|x-a|<R) .
$$

This shows that every power series with a positive radius of converg the Taylor series of the function $f(x)$ that it represents. (In gener may not be able to express $f(x)$ in terms of familiar elementary fur as shown in the list at the outset of the section.)

The power series (4) can be integrated term-by-term on any clos bounded subintervals of the interval of convergence, as follows. Let a closed interval in the interval of convergence: then
$$
\begin{aligned}
\int_{b}^{c} f(t) d t & =\sum_{m=0}^{\infty} a_{m} \int_{b}^{c}(t-a)^{m} \\
& =\sum_{m=0}^{\infty} \frac{a_{m}}{m+1}\left[(c-a)^{m+1}-(b-a)^{m+1}\right]
\end{aligned}
$$

In particular, if $x$ is in the interval of convergence, then
$$
\int_{a}^{x} f(t) d t=\sum_{m=0}^{\infty} \frac{a_{m}}{m+1}(x-a)^{m+1}
$$
because
$$
\int_{a}^{x}(t-a)^{m} d t=\left.\frac{1}{m+1}(t-a)^{m+1}\right|_{a} ^{x}=\frac{1}{m+1}(x-a)^{m+1}
$$

The proof is also sketched in the exercises. Let us illustrate the use of term-by-term differentiation and integration by deriving new powe from known ones, without performing excessive computations.

---

<!-- Page 33 -->

Right margin note (page 33)

A33

ve the riginal
riginal $m=0$
nterval placing of the
series nd the that ons of esult.
$(x)=$ nce. If $m$. In
in the ratives then same

++++

Section A. 4 The Power Series Method, Part I

EXAMPLE 4 Differentiation and integration term-by-term
(a) Start with the geometric series
$$
\frac{1}{1-x}=1+x+x^{2}+x^{3}+\cdots=\sum_{m=0}^{\infty} x^{m} \quad(-1<x<1) .
$$

Differentiate both sides of the the first equality:
$$
\frac{1}{(1-x)^{2}}=0+1+2 x+3 x^{2}+\cdots=\sum_{m=1}^{\infty} m x^{m-1} \quad(-1<x<1) .
$$

This gives the power series expansion of the function $1 /(1-x)^{2}$. Obser following two facts:
- The differentiated series has the same radius of convergence as the series.
- The index in the differentiated series starts at $m=1$, whereas in the series it starts at $m=0$. This is clear since the term corresponding to in the differentiated series is 0 .
(b) Start with the geometric series in (a). For $x$ in ( $-1,1$ ), we have
$$
\begin{aligned}
\int_{0}^{x} \frac{1}{1-t} d t & =\int_{0}^{x}\left(1+t+t^{2}+t^{3}+\cdots\right) d t \\
-\left.\ln (1-t)\right|_{0} ^{x} & =\left.\left(t+\frac{t^{2}}{2}+\frac{t^{3}}{3}+\frac{t^{4}}{4}+\cdots\right)\right|_{0} ^{x} \\
-\ln (1 \cdots r) & =x+\frac{x^{2}}{2}+\frac{x^{3}}{3}+\frac{x^{4}}{4}+\cdots
\end{aligned}
$$

This gives the power series representation of $\ln (1-x)$, which is valid in the $i -1<x<1$. Note that we could have obtained this representation by re $x$ by $-x$ in the expansion of $\ln (1+x)$ from the list given at the beginning section.

In the preceding examples, we used various operations on known to derive new power series expansions. Thus we claimed to have four power series expansions of $1 /(1-x)^{2}$ and $\ln (1-x)$. The questio comes to mind is whether there are other power series representati these functions. The answer is provided by the following important r

The Identity Principle. Suppose $f(x)=\sum_{m=0}^{\infty} a_{m}(x-a)^{m}$ and $s^{-} \sum_{m=0}^{\infty} b_{m}(x-a)^{m}$, where both series have positive radii of converge $f(x)=g(x)$ for all $x$ in an interval containing $a$, then $a_{m}=b_{m}$ for all other words, a power series representation is unique.

This is an immediate consequence of the fact that the coefficients power series are determined from the values of the function and its deriv at $x=a$ (Taylor's formula). So if $f=g$ in an interval containing $a f^{(m)}(a)=g^{(m)}(a)$ for all $m$, which implies that the coefficients are the in both power series.

---

<!-- Page 34 -->

Left margin note (page 34)

A34
Appendix A
Ordina

Right margin note (page 34)

of a
strate.
anishes
equal
bout 0 Thus
ing the and so
( $x$ ) is $(x)$ ) is ble by $\mathrm{d} g(x)$ power
nalytic aed by For obtain

++++

Differential Equations: Review of Concepts and Methods

We will often use the identity principle to determine the coefficien power series that appears in an equation, as the following examples illus

EXAMPLE 5 The identity principle
Determine $a_{m}$ if for all $x$ in the interval $(1,1)$, we have
$$
\sum_{m=0}^{\grave{n}}\left(u_{m}-2 m\right) r^{m}=0 .
$$

Solution By the identity principle, there is only one power series that va identically on ( $-1,1$ ), and this is the power series whose coefficients are al to 0 . Thus $a_{m}-2 m=0$ for all $m$, and so $a_{m}=2 m$.

EXAMPLE 6 Equation involving a power series
Determine $a_{m}$ if for all $x$ in the interval $(-1,1)$, we have
$$
\sum_{m=0}^{\infty} a_{m} x^{m}+\sum_{m=0}^{\infty} m a_{m} x^{m}=\frac{1}{1-x}
$$

Solution Combining the two series on the left, the equation becomes
$$
\sum_{m=0}^{\infty}(1+m) a_{m}: x^{m}=\frac{1}{1-x}
$$

To be able to proceed from this point, we express $1 /(1-x)$ in a power series a and use the identity principle to equate the corresponding coefficients of $x^{m}$
$$
\sum_{m=0}^{\infty}(1+m) a_{m} x^{m}=\sum_{m 0}^{\infty} r^{\prime m} \Rightarrow \quad(1+m) a_{m}=1 \text { for all } m,
$$
because all the coefficients in the expansion of $1 /(1-x)$ are equal to 1 . Solv last equation, we find $a_{m}=1 /(1+m)$. Thus $a_{0}=1, a_{1}=1 / 2, a_{2}=1 / 3$, on.

Composition of Power Series. We know from calculus that if $f$ differentiable at $x=a$ and $g(x)$ is differentiable at $f(a)$, then $g(f$ differentiable at $a$. This fact remains valid if we replace differentia analytic; that is, if $f(x)$ has a power series expansion centered at $a$ an has a power series expansion centered at $f(a)$, then $g(f(x))$ has a series expansion centered at $a$.

As an illustration, suppose that $f(x)=(x-a)^{m}$ and $g(x)$ is ar at $0(=f(a))$. Then the power series of $g(f(x))$ about $a$ is obtain substituting $(x-a)^{m}$ in the power series expansion of $g(x)$ about $($ example, substituting $x$ by $x^{2}$ in the Taylor series expansion of $e^{x}$, we the Taylor series of $\epsilon^{x^{2}}$,
$$
e^{x^{2}}=\sum_{m=0}^{\infty} \frac{r^{2 m}}{m!}=1+x^{2}+\frac{x^{4}}{2!}+\frac{x^{6}}{3!}+\cdots \quad(-\infty<x<\infty) .
$$

---

<!-- Page 35 -->

Right margin note (page 35)

A35 tic at h the Exer$1 / g$ ), tions used 1e the oo the stant,
$$
3 \mid<1
$$

++++

Section A. 4 The Power Series Method, Part I

Quotients of Analytic Functions. Suppose that $f$ and $g$ are analy $a$ and $g(a) \neq 0$. Then the quotient $f / g$ is also analytic at $a$.

To see this, we view the function $1 / g$ as the composition of $g$ wit function $1 / x$. The latter being analytic everywhere except at $x=0$ ( cise 25), it follows that $1 / g$ is analytic at $a$ if $g(a) \neq 0$. Now $f / g=f \cdot($ and the desired conclusion follows since the product of two analytic func is again analytic.

The following examples illustrate some useful techniques that can be when computing a power series of a rational function.

EXAMPLE 7 Power series of rational functions
Find the power series expansion at $a=0$ of the given function, and determin radius of convergence.
(a) $\frac{1}{3+2 x}$.
(b) $\frac{4 x^{2}+8 x-4}{3+2 x}$.

Solution (a) To find the power expansion, we try to relate the function geometric series, which we recall in the following form:
$$
\sum_{m=0}^{\infty} u^{m}=\frac{1}{1-u} \quad(|u|<1) .
$$

If we can write $L /(3+2 x)$ in the form $A /(1-u)$ for some $u$, where $A$ is a con then we will be done. For this purpose, we proceed as follows:
$$
\frac{1}{3+2 x}=\frac{1}{3} \frac{1}{1-\left(-\frac{2 x}{3}\right)}=\frac{1}{3} \frac{1}{1-u},
$$
where $u=-2 x / 3$. Thus
$$
\frac{1}{3+2 x}=\frac{1}{3} \sum_{m=0}^{\infty}\left(-\frac{2 x}{3}\right)^{m}=\sum_{m=0}^{\infty}(-1)^{m} \frac{2^{m} x^{m}}{3^{m+1}} .
$$

Furthermore. the scries converges if and only if $|u|<1$; equivalently, $\mid-2 x /$; or $|x|<3 / 2$. Hence the series has radius of convergence equal to $3 / 2$.
(b) Dividing the numerator by the denominator, we obtain
$$
\frac{4 x^{2}+8 x-4}{3+2 x}=2 x+1-\frac{7}{3+2 x} .
$$

Using the power series expansion from (a), we find
$$
\begin{aligned}
\frac{4 x^{2}+8 x-4}{3+2 x} & =1+2 x-7 \sum_{m=0}^{\infty}(-1)^{m} \frac{2^{m} x^{m}}{3^{m+1}} \\
& =1-\frac{7}{3}+x\left(2+\frac{14}{9}\right)-7\left(\frac{4}{27} x^{2}-\frac{8}{243} x^{3}+\cdots\right) \\
& =-\frac{4}{3}+\frac{32}{9} x-7 \sum_{m=2}^{\infty}(-1)^{m} \frac{2^{m} x^{n}}{3^{m+1}} .
\end{aligned}
$$

---

<!-- Page 36 -->

Left margin note (page 36)

A36
Appendix A
Ordinary

Right margin note (page 36)

solve series ne the annot has a nation, $n$. As nes
power nits as
in the of the
in the of the

++++

Differential Equations: Review of Concepts and Methods

The power series has the same radius of convergence as the one in part (a). Shifting the Index in a Power Series. When using power series to differential equations, we are often required to combine several power into a single one, as we did in Example 6. Suppose you want to combi expression
$$
\sum_{m=0}^{\infty} x^{m+1}+\sum_{m-0}^{\infty}(m+1) x^{m}
$$
into one power series. Unlike what we did in Example 6, here we simply add terms with corresponding indices, because the variable $x$ different power in the general term of each series. To deal with this situ we can rewrite the first series in terms of $x^{m}$, as follows. Let $m+1= m$ varies from 0 to $\infty, n$ varies from 1 to $\infty$ and the first series becon
$$
\sum_{m=0}^{\infty} x^{m+1}=\sum_{n=1}^{\infty} x^{n} .
$$

Now rewrite the index $n$ as $m$, and you have
$$
\sum_{m=0}^{n} x^{m-1}=\sum_{m}^{\infty} x^{m} .
$$

So we were able to shift the index of the terms without changing the series. In general, the index $m$ in a power series can be shifted by $k \mathrm{u}$ follows:
$$
\sum_{m=s}^{\infty} a_{m}(x-a)^{m+k}=\sum_{m=s+k}^{\infty} a_{m-k}(x-a)^{m} .
$$

Thus, if we shift the index of summation by changing $m$ to $m-k$ general term of the series, then we must increase the starting point summation by $k$. We also have
$$
\sum_{m=s}^{\infty} a_{m}(x-a)^{m}=\sum_{m=s-k}^{\infty} a_{m+k}(x-a)^{m+k} .
$$

Thus, if we shift the index of summation by changing m to $n+k$ general term of the series, then we must decrease the starting point summation by $k$.

EXAMPLE 8 Shifting indices
Write the following sum as a single power series
$$
\sum_{m=1}^{\infty} m x^{m-1}+\sum_{m=0}^{\infty} 2 x^{m+1} .
$$

---

<!-- Page 37 -->

Right margin note (page 37)

A37
nge $m$
$m$. In
ecome

d one
ower
$$
R>0 .
$$
ius of
$$
m=0
$$

++++

Section A. 4 The Power Series Method, Part 1

Solution Let us express both series in terms of $x^{m}$. That means we must cha to $m+1$ in the first series, so that the exponent of $x$ becomes $(m+1)-1=$ the second series we must change $m$ to $m-1$. With this in mind, the serics b
$$
\sum_{m=0}^{\infty}(m+1) x^{m}+\sum_{m=1}^{\infty} 2 x^{m} .
$$

We can now combine the two series as
$$
(0+1) x^{0}+\sum_{m=1}^{\infty}(m+1) x^{m}+\sum_{m=1}^{\infty} 2 x^{m}=1+\sum_{m=1}^{\infty}(m+3) x^{m} .
$$

Note how we split off the $m=0$ term from the first series. since the secon starts at $m-1$.

The following two examples illustrate some of the basic steps in the series method of the next section.

EXAMPLE 9 Combining power series and their derivatives
Suppose that $y=\sum_{m=0}^{\infty} a_{m} x^{m}$ is a power series with radius of convergence Find a power series representation for the expression
$$
(1+x) y^{\prime}-2 y .
$$

Solution A power series can be differentiated term-by-term within its rad convergence. So for $|x|<R$, we have
$$
y^{\prime}=\sum_{m=1}^{\infty} a_{m} m x^{m-1} .
$$

Using that $x \sum_{m=1}^{\infty} a_{m} m x^{m-1}=\sum_{m=1}^{\infty} a_{m} m x^{\prime \prime}$, we obtain
$$
\begin{aligned}
(1+x) y^{\prime} & =(1+x) \sum_{m=1}^{\infty} a_{m} m x^{m-1}=\sum_{m=1}^{\infty} a_{m} m x^{m-1}+\sum_{m=1}^{\infty} a_{m} m x^{m} \\
& =\sum_{m=0}^{\infty} a_{m+1}(m+1) x^{m}+\sum_{m=1}^{\infty} a_{m} m x^{m} .
\end{aligned}
$$

The second series can be started at $m=0$, since the term corresponding to is 0 . So
$$
\begin{aligned}
(1+x) y^{\prime} & =\sum_{m=0}^{\infty}\left[(m+1) a_{m+1}+m a_{m}\right] x^{m} ; \\
(1+x) y^{\prime}-2 y & =\sum_{m=0}^{\infty}\left[(m+1) a_{m+1}+m a_{m}\right] x^{m}-2 \sum_{m=0}^{\infty} a_{m} x^{m} \\
& =\sum_{m=0}^{\infty}\left[(m+1) a_{m+1}+(m-2) a_{m}\right] x^{m} .
\end{aligned}
$$

---

<!-- Page 38 -->

Left margin note (page 38)

A38

Appendix A Ordinary

Right margin note (page 38)

and 1
$$
\left.a_{m}\right] x^{m}
$$
eries.
$$
\text { 3) } x^{m}
$$

Taylor us and
- 1).

++++

Differential Equations: Review of Concepts and Methods

EXAMPLE 10 Combining power series and their derivatives Continuing the previous example, find a power series representation of
$$
x^{2} y^{\prime \prime}+(1+x) y^{\prime}-2 y .
$$

Solution Differentiating the power series of $y$ twice, we obtain
$$
y^{\prime \prime}=\sum_{m=2}^{\infty} a_{m} m(m-1) x^{m-2} \Rightarrow x^{2} y^{\prime \prime}=\sum_{m-2}^{\infty} a_{m} m(m-1) x^{m} .
$$

We now appeal to the result of the previous exercise and get
$$
\begin{array}{l}
x^{2} y^{\prime \prime}+(1+x) y^{\prime}-2 y \\
\quad=\sum_{m=2}^{\infty} a_{m} m(m-1) x^{m}+\sum_{m=0}^{\infty}\left[(m+1) a_{m+1}+(m-2) a_{m}\right] x^{m}
\end{array}
$$

To combine the two series, we split off the terms corresponding to $m$ from the second series and get
$$
\begin{aligned}
x^{2} y^{\prime \prime} & +(x+1) y^{\prime}-2 y \\
& =\left(a_{1}-2 a_{0}\right)+\left(2 a_{2}-a_{1}\right)+\sum_{m=2}^{\infty}\left[a_{m} m(m-1)+(m+1) a_{m+1}+(m-2\right. \\
& =2\left(a_{2}-a_{0}\right)+\sum_{m=2}^{\infty}\left[(m+1) a_{m+1}+a_{m}\left(m^{2}-2\right)\right] x^{m} .
\end{aligned}
$$

Exercises A. 4
In Exercises 1-12, find the radius and interval of convergence of the given $s$
1. $\sum_{m=0}^{\infty} \frac{x^{m}}{5 m+1}$.
2. $\sum_{m=0}^{\infty} \frac{3^{m} x^{m}}{m!}$.
3. $\sum_{m=0}^{\infty} \frac{(-1)^{m} x^{m+2}}{2^{m}}$.
4. $\sum_{m=0}^{\infty}(x-2)^{m}$.
5. $\sum_{m=1}^{\infty} \frac{m^{m} x^{m}}{m!}$.
6. $\sum_{m=1}^{\infty} \frac{(m-1)(m+\text {; }}{m}$
7. $\sum_{m=2}^{\infty} \frac{x^{m}}{\ln m}$.
8. $\sum_{m=1}^{\infty} \frac{(x+1)^{m}}{m^{2}}$.
9. $\sum_{m=1}^{\infty} \frac{[10(x+1)]^{2 m}}{(m!)^{2}}$.
10. $\sum_{m=0}^{\infty} \frac{(9 x)^{2 m}}{(n!)^{2}}$.
11. $\sum_{m=0}^{\infty} \frac{2^{m}(x-2)^{m}}{10^{m}}$.
12. $\sum_{m-0}^{\infty} \frac{m!(x-2)^{m}}{10^{m}}$.

In Exercises 13-20, use a Taylor series found in this section to derive the series expansion of the given function at 0 . In each case, specify the rad interval of convergence.
13. $\frac{3-x}{1+x}$.
14. $\frac{x}{(1+x)^{2}}$.
15. $\frac{x}{\left(1+r^{2}\right)^{2}}$.
16. $\frac{x+2}{1-x^{2}}$.
17. $e^{3 x^{2}+1}$.
18. $x \ln (1+x)$.
19. $x \sin x \cos x$.
20. $x \sin (x$

---

<!-- Page 39 -->

Right margin note (page 39)

A39
ion of
pence.
$\overline{2}$
that
at, 0 .
C.
ively.
ctions
vith a
ssibly
a pos-
given

++++

Section A. 4 The Power Series Method, Part I

In Errrises 21-24, use the geometric series to derive the Taylor series expans the given function at 0 . In each case, specify the radius and interval of conver
21. $\frac{1}{2-3 x}$.
22. $\frac{1+x}{2-3 x}$.
23. $3 \frac{x+x^{3}}{2+3 x^{2}}$.
24. $\frac{1}{x^{2}-2 x+}$
25. Let $a$ be any real number $\neq 0$. Use ideas found in Example 7(a) to show
$$
\frac{1}{x}=\frac{1}{a} \sum_{m-0}^{\infty}(-1)^{n} \frac{(x-a)^{n}}{a^{n}},
$$
with radius of convergence $R=|a|$. Thus $1 / x$ is analytic everywhere except
26. Let
$$
f(x)=\sum_{k=0}^{\infty} \frac{(-1)^{k} x^{2 k}}{(k!)^{2} 2^{2 k}} \quad \text { and } \quad g(x)=\sum_{k=0}^{\infty} \frac{(-1)^{k} x^{2 k+1}}{k!(k+1)!2^{2 k \cdot 1}} .
$$

Prove the following assertions. (a) Both power series converge for all $x$.
(b) $f^{\prime}(x)=-g(x)$.
(c) $\int g(x) d x=f(x)+C$.
(d) $\int x f(x) d x=x g(x)+$
(The functions $f$ and $g$ are known as Bessel functions or order 0 and 1 , respect They are usually clenoted by $J_{0}(x)$ (for $f(x)$ ) and $J_{1}(x)$ (for $g(x)$ ). Bessel fun are studied in detail in Chapter 4.)
27. Let $f(x)$ be as in Exercise 26. (a) Find $f(0), f^{\prime}(0), f^{\prime \prime}(0)$.
(b) More generally, find $f^{(k)}(0)$, for $k=0,1.2, \ldots$.
(c) Integrate term-by-term to find $\int_{0}^{1} f(x) d x$, then estimate the integral calculator.
28. Let $f(x)=\frac{1+x}{1-x}$. Find $f(0), f^{\prime}(0)$, and $f^{(100)}(0)$.

In Exercises 29-32, write the given expression as a single power series (and po some lower power terms, as in Example 8).
29. $\sum_{m=1}^{\infty} \frac{x^{m}}{m}-2 \sum_{m=0}^{\infty} m x^{m+1}$.
30. $\sum_{m=1}^{\infty} \frac{x^{m+1}}{m!}+\sum_{m=3}^{\infty}(m-1) x^{m-1}$.
31. $2 x \sum_{m=2}^{\infty} 2 \sqrt{m+2} x^{m}+\sum_{m=2}^{\infty} \frac{x^{m-1}}{m+6}$.
32. $(x+1) \sum_{m=2}^{\infty} 2 x^{m-1}$.

In Exercises 33-40, suppose that $y=\sum_{m=0}^{\infty} a_{m} x^{m}$ is a power series with itive radius of convergence, and find a power series representation for the expression.
33. $y^{\prime}+y$.
34. $y^{\prime}+x^{2} y$.
35. $\left(1-x^{2}\right) y^{\prime \prime}+2 x y^{\prime}$.
36. $(2+x) y^{\prime}+x^{3} y$.
37. $x^{2} y^{\prime \prime}+y$.
38. $y^{\prime \prime}+y^{\prime}+x y$.
39. $x y^{\prime}+y-e^{x}$.
40. $(1 \cdots r) y^{\prime \prime}+\sin x$.

---

<!-- Page 40 -->

Left margin note (page 40)

A40
Appendix A
A. 5 The Po

Right margin note (page 40)

1, and
$|x|<1$
if and
number c series
$\rho, \rho]$.
rem 5 ,
$x^{m}$ has
all $m$.
to con-
$=0 a_{m} x^{m}$
of con-
Then
can be
id then
$R$ ) is
$+a$ ).]
nsions.
The nd the ration.
l-order solved series series. series. ation.

++++

Ordinary Differential Equations: Review of Concepts and Methods
41. Geometric series. Fix a real (or complex) number $x$ such that $|x|<$ let $n$ be a positive integer. (a) Show that
$$
1+x+x^{2}+\cdots+x^{n}=\frac{1-x^{n+1}}{1-x}
$$
(b) Conclude that the geometric series $\sum_{m=0}^{\infty} x^{m}$ converges to $1 /(1-x)$ if and diverges otherwise. [Hint: What are the partial sums? Also, $x^{n+1} \rightarrow 0$ only if $|x|<1$.]
42. Uniform convergence of the geometric series. (a) Let $\rho$ bc any such that $0<\rho<1$. Use the Weierstrass $M$-test to show that the goometri $\sum_{m=0}^{\infty} x^{m}$ converges uniformly for all $x$ in $[-\rho, \rho]$.
(b) Show that the differentiated series $\sum_{m=1}^{\infty} m x^{m-1}$ converges uniformly on
(c) Justify term-by-term differentiation of the geometric sories. (See Theo Section 2.9.)
43. Uniform convergence of power series. Suppose that $\sum_{m=0}^{\infty} a_{m}$ radius of convergence $R>0$. Let $r$ be any real number such that $0<r<F$
(a) Show that $a_{m} r^{m} \rightarrow 0$. Conclude that $\left|a_{m} r^{m}\right| \leq M$ for some $M>0$ and [Hint: Apply the $n$th term test to a convergent series.]
(b) For $x$ such that $|x| \leq r$, we have
$$
\left|a_{m} x^{m}\right|=\left|a_{m}\right| r^{m}(|x| / r)^{m} \leq M(|x| / r)^{m} .
$$

Use these inequalities, the fact that $|x| / r<1$, and the Weierstrass $M$-test clude that $\sum_{m=0}^{\infty} a_{m} x^{m}$ converges uniformly on $[-r, r]$.
44. Term-by-term differentiation of power series. (a) Show that if $\sum_{m}^{\infty}$ has radius of convergence $R>0$, then $\sum_{m=1}^{\infty} m a_{m} x^{m-1}$ has the same radius vergence. [Hint: Given $0 \leq|x|<R$, let $r$ be such that $|x|<r<R$. $\left|m a_{m} x^{m-1}\right| \leq m(|x| / r)^{m-1}\left|a_{m}\right| r^{m-1}$. Use the fact that the geometric series differentiated term-by-term (so $\sum m(|x| / r)^{m-1}$ is convergent); also prove an use that $\left|a_{m}\right| r^{\prime \prime \prime}-1 \leq M$ for some $M$.]
(b) Show that the derivative of $\sum_{m=0}^{\infty} a_{m} x^{m}$ is $\sum_{m=1}^{\infty} m a_{m} x^{m-1}$.
(c) Show that the derivative of $f(x)=\sum_{m=0}^{\infty} a_{m}(x-a)^{m}$ (for $|x-a|< f^{\prime}(x)=\sum_{m=1}^{\infty} m a_{m}(x-a)^{m-1}$ (for $|x-a|<R$ ). [Hint: Define $g(x)=f(x$
wer Series Method, Part II
The solutions of many differential equations have power series expar For example, the solution of $y^{\prime}-y=0$ is $y=C e^{x}$ or $y=C \sum_{m=0}^{\infty} \frac{x^{\prime}}{n}$ power series method, that we present in this section, allows us to fi power series solution (when it exists) directly from the differential eqn This method is very useful in solving a wide class of important second linear differential equations with variable coefficients that cannot be by the methods that we discussed in previous sections. The power method works as follows. First, assume that the solution is a power Second, write each term in the given differential equation as a power Third, equate coefficients of the resulting series on both sides of the eqr

---

<!-- Page 41 -->

Left margin note (page 41)

To combine the series, we need to have the same powers of $x$ : appearing in both. For this purpose, we reindex the first series by changing $m$ to $m+1$. The index of summation has to be lowered by 1 , and so the first series will have to start at 0 .

Right margin note (page 41)

A41 of the $y=0$. ansion $y^{\prime}=$ uation
…,
encral
like a hange ist be series
eding lation et $a_{1}$, lation

++++

Section A. 5 The Power Series Method, Part II

Finally, solve for the unknown coefficients in the series representation assumed solution.

Let us illustrate this by deriving the power series solution of $y^{\prime}-$

EXAMPLE 1 A first-order equation
Assuming that you know that the solution of $y^{\prime}-y=0$ has a power series $\exp$ about 0 , find this solution.
Solution Write $y=\sum_{m=0}^{\infty} a_{m} x^{m}$. Differentiating term-by-term we have $\sum_{m=1}^{\infty} m a_{m} x^{m-1}$. If we substitute the power series of $y$ and $y^{\prime}$ into the eq and combine the series, we obtain
$$
\begin{array}{c}
\sum_{m=1}^{\infty} m a_{m} x^{m-1}-\sum_{m=0}^{\infty} a_{m} x^{m}=0 \\
\sum_{m=0}^{\infty}(m+1) a_{m+1} x^{m}-\sum_{n=0}^{\infty} a_{m} x^{m}=0 \\
\sum_{m=0}^{\infty}\left[(m+1) a_{m+1}-a_{m}\right] x^{m}=0
\end{array}
$$

By the identity principle, $(m+1) a_{m+1}-a_{m}=0$ for all $m$, and so
$$
a_{m+1}=\frac{a_{m}}{m+1} .
$$

Thus,
$$
a_{1}=a_{0} . \quad a_{2}=\frac{a_{1}}{2}=\frac{a_{0}}{1 \cdot 2}, \quad a_{3}=\frac{a_{2}}{3}=\frac{a_{0}}{1 \cdot 2 \cdot 3}, \quad a_{4}=\frac{a_{3}}{4}=\frac{a_{0}}{1 \cdot 2 \cdot 3 \cdot 4},
$$
and in general $a_{m}=a_{0} / m!$. Hence the solution is
$$
y=a_{0}\left(1+\frac{x}{1!}+\frac{x^{2}}{2!}+\frac{x^{3}}{3!}+\cdots\right)=a_{0} e^{x},
$$
where $a_{0}$ accounts for the arbitrary constant that we would expect in the solution of a first-order linear differential equation.

Recall from the previous section that reindexing a series works change of variables in an integral. If $k$ is a positive integer and you c $m$ to $m+k$ inside the series, then the starting point of the series m lowered by $k$. If you change $m$ to $m-k$, then the starting point of the must be raised by $k$.

An expression like (1) that gives each coefficient in terms of pred ones is called a recurrence relation. In Example 1 the recurrence re determines the coefficients in steps of one. That is, from $a_{0}$ we g from $a_{1}$ we get $a_{2}$, and so on. In the next example, the recurrence re determines the coefficients in steps of two.

---

<!-- Page 42 -->

Left margin note (page 42)

A42
Appendix A

Change $m$ to $m+2$ ir series. and start the 1 at 0 .

Right margin note (page 42)

$+y=$
s have
power
Ition
$a_{4}$ and
c even
blution

++++

Ordinary Differential Equations: Review of Concepts and Methods

EXAMPLE 2 A familiar second-order equation
We know that two linearly independent solutions of the differential equation $y^{\prime \prime}$ 0 are $y_{1}=\cos x$ and $y_{2}=\sin x$. We also know that both of these solution power series expansions about 0 . Derive the power series solutions using the series method.

Solution If we assume that the differential equation has a power series solu
$$
y=\sum_{m=0}^{\infty} a_{m} x^{m}=a_{0}+a_{1} x+a_{2} x^{2}+a_{3} x^{3}+\cdots,
$$
then the derivatives of $y$ are obtained by term-by-term differentiation:
$$
\begin{array}{c}
y^{\prime}=\sum_{m=1}^{\infty} m a_{m} x^{m-1}=a_{1}+2 a_{2} x+3 a_{3} x^{2}+\cdots \\
y^{\prime \prime}=\sum_{m=2}^{\infty} m(m-1) a_{m} x^{m-2}=2 a_{2}+2 \cdot 3 a_{3} x+3 \cdot 4 a_{4} x^{2}+\cdots
\end{array}
$$

Substituting $y$ and $y^{\prime \prime}$ into the equation, we obtain

the first
new series
$$
\begin{aligned}
\sum_{m}^{\infty} m(m-1) a_{m} x^{m-2}+\sum_{m=0}^{\infty} a_{m} x^{m} & =0 \\
\sum_{m=0}^{\infty}(m+2)(m+1) a_{m} \cdot 2 x^{m}+\sum_{m 0}^{\infty} a_{m} x^{\prime \prime \prime} & =0 \\
\sum_{m=0}^{\infty}\left[(m+2)(m+1) a_{m \cdot 2}+a_{m}\right] x^{m} & =0
\end{aligned}
$$

Thus
$$
a_{m+2}=-\frac{1}{(m+2)(m+1)} a_{m} .
$$

It is clear from this relation that $a_{0}$ determines $a_{2}$, which in turn determines so on. Similarly, $a_{1}$ determines $a_{3}$. which determines $a_{5}$, and so on. Thus th coefficients are determined from $a_{0}$ and the odd coefficients from $a_{1}$ :
$$
\begin{array}{ll}
a_{2}=-\frac{1}{2!} a_{0}, & a_{3}=-\frac{1}{3!} a_{1} \\
a_{4}=-\frac{1}{4 \cdot 3} a_{2}=\frac{1}{4!} a_{0}, & a_{5}=-\frac{a_{3}}{5 \cdot 4}=\frac{1}{5!} a_{1} \\
a_{6}=-\frac{1}{6 \cdot 5} a_{4}=-\frac{1}{6!} a_{0}, & a_{7}=-\frac{a_{5}}{7 \cdot 6}=-\frac{1}{7!} a_{1}
\end{array}
$$

The pattern we see gives
$$
a_{2 k}=(-1)^{k} \frac{a_{0}}{(2 k)!}, \quad a_{2 k+1}=(-1)^{k} \frac{a_{1}}{(2 k+1)!} .
$$

Writing the even-indexed and the odd-indexed terms separately, we get the sc
$$
y=a_{0} \sum_{k=0}^{\infty}(-1)^{k} \frac{x^{2 k}}{(2 k)!}+a_{1} \sum_{k=0}^{\infty}(-1)^{k} \frac{x^{2 k+1}}{(2 k+1)!} .
$$

---

<!-- Page 43 -->

Left margin note (page 43)

SNOILATOS
SAIHAS ΗθMOA
I NGYOAHL

Right margin note (page 43)

A43
as we
at we were er, is ations loes a silme series
nplies which $? / x$ is c A.1, $/ x) \dagger$ s is to annot es exgives nsions ressed
s large
adius or the

++++

Section A. 5 The Power Series Method. Part. II

We recognize these series as the Taylor series for the sine and cosine; thus. already observed, $y=a_{0} \cos x-a_{1} \sin x$.

Note that $a_{0}$ and $a_{1}$ account for the two arbitrary constants th expect in the general solution to a second-order differential equation.

In Examples 1 and 2 the solutions of the differential equations familiar functions. The usefulness of the power series method, howev more appreciated when we use it to find solutions that are not combina of elementary functions. To apply the method, we need to know when solution have a power series expansion. Consider what happens if we as that the solution of the differential equation $x y^{\prime}+y=0$ has a power expansion at 0 . Setting $y=\sum_{m=0}^{\infty} a_{m} x^{m}$, then
$$
x y^{\prime}+y=x \sum_{m=0}^{\infty} m a_{m} x^{m-1}+\sum_{m=0}^{\infty} a_{m} x^{m}=\sum_{m=0}^{\infty}(1+m) a_{m} x^{m} .
$$

So $x y^{\prime}+y=0$ implies that $\sum_{m=0}^{\infty}(1+m) a_{m} x^{\prime \prime \prime}=0$, which in turn in that $(1+m) a_{m}=0$ for all $m$. Since $1+m \neq 0$, it follows that $a_{m}=0$, implies that the solution is $y=0$. But you can easily verify that $y=0$ a solution (you can derive the solution by using Theorem 1, Appendi> or by simply guessing it). Indeed, $y^{\prime}=-C / x^{2}$ and so $x y^{\prime}+y=(-C (C / x)=0$. So the power series method did not work in this case. This be expected since the solution is not even defined at $x=0$ and so it c possibly have a power series centered at 0 .

Thus we cannot always assume that the solution has a power seri pansion centered at a given point. The following theorem of Fuchs sufficient conditions that justify using the power series method.

Suppose that the functions $p(x), q(x)$, and $g(x)$ have power series expa at $x=a$; then any solution of
$$
y^{\prime \prime}+p(x) y^{\prime}+q(x) y=g(x)
$$
has a power series expansion at $x=a$. Thus any solution $y$ can be exp as a power series centered at $a$,
$$
y=\sum_{m=0}^{\infty} a_{m}(x-a)^{m} .
$$

Moreover, the radius of convergence of this power series is at least a as the minimum of the radii of convergence of $p, q$, and $g$.

When $p(x), q(x)$, and $g(x)$ have power series expansions with positive , of convergence at $x=a$, the point $a$ is called an ordinary point for equation (2).

---

<!-- Page 44 -->

Left margin note (page 44)

A44
Appendix A

Note how the index o tion in the first sum by 2 .

Right margin note (page 44)

em 3, stence 1, see Gianem 1, $x y=$ gence

Since elves), series icients es and 1. For

++++

Ordinary Differential Equations: Review of Concepts and Methods

Since the existence of the solutions of (2) is guaranteed by Theor Appendix A.1, the real purpose of Theorem 1 is to address the exis of power series expansions of the solutions. For a proof of Theorem Chapter 3 of Ordinary Differential Equations. by Garrett Birkhoff and Carlo Rota, 2nd ed., Wiley, 1969. To appreciate the power of Theor note that it asserts that a complicated equation such as $y^{\prime \prime}+e^{x} y^{\prime}+\cos 1 /\left(1+x^{2}\right)$ has a power series solution about $x=0$ with radius of conver at least 1 .

EXAMPLE 3 A second-order initial value problem
Solve the initial value problem
$$
y^{\prime \prime}+r y^{\prime}+y=0, \quad y(0): \quad 0, \quad y^{\prime}(0)=1 .
$$

Solution Using the notation of Theorem 1, we let $p(x)=x$ and $q(x)=1$. both functions have power series expansions at 0 (given by the functions thems we can assume a solution of the form
$$
y=\sum_{m=0}^{\infty} a_{m} x^{m}=a_{0}+a_{1} x+a_{2} x^{2}+\cdots
$$

At the outset, we may use the initial conditions to find $a_{0}$ and $a_{1}$. We have
$$
\begin{array}{c}
y(0)=a_{0}+a_{1} 0+a_{2} 0^{2}+\cdots=a_{0} \\
y^{\prime}(0)=a_{1}+2 a_{2} 0+3 a_{3} 0^{2}+\cdots=a_{1}
\end{array}
$$
and so the initial conditions imply that $a_{0}=0$ and $a_{1}=1$. Substituting the for $y$ and its derivatives into the differential equation yields
$$
\sum_{m=2}^{\infty} m(m-1) a_{m} x^{m-2}+\sum_{m=1}^{\infty} m a_{m} x^{m}+\sum_{m=0}^{\infty} a_{m} x^{m}=0 .
$$

Shifting the index of summation in the first series yields
f summadropped
$$
\begin{array}{l}
\sum_{m-0}^{\infty}(m+2)(m+1) a_{m+2} x^{m}+\sum_{m=1}^{\infty} m a_{m} x^{m}+\sum_{m=0}^{\infty} a_{m} x^{m}=0 \\
\left(2 a_{2}+a_{0}\right)+\sum_{m=1}^{\infty}\left[(m+2)(m+1) a_{m+2}+m a_{m}+a_{m}\right] x^{m}=0
\end{array}
$$

Equating the constant term to zero gives $a_{2}=-a_{0} / 2$ and equating the coeff of the series to wro yields the recurrence relation
$$
a_{m+2}=\frac{-1}{m+2} a_{m}
$$

As in the preceding example, $a_{0}$ determines the coefficients with even indic $a_{1}$ those with odd indices. Since $a_{0}=0$, we get $a_{2}=0, a_{4}=0$, and so or

---

<!-- Page 45 -->

Left margin note (page 45)

![](./images/66923605-2b3e-4154-b144-3e182be82ea5-45_299_458_892_59.jpg)

Figure 1 Polynomial (degree $2 n$ 1) approximation of the solution in Example 3.

Right margin note (page 45)

A45
given
hed in s on a ions. ее Ex-
ns for terms nation initial $g(x)=$ for all dius of

++++

Section A. 5 The Power Series Method, Part 11

the coefficients with odd indices. the recurrence relation gives
$$
\begin{array}{l}
a_{1}=1 \\
a_{3}=-\frac{1}{3} a_{1}=-\frac{1}{3} \\
a_{5}=-\frac{1}{5} a_{3}=\frac{1}{5 \cdot 3} \\
a_{7}=-\frac{1}{7} a_{5}=-\frac{1}{7 \cdot 5 \cdot 3} .
\end{array}
$$

The pattern that emerges is
$$
a_{2 k+1}=\frac{(-1)^{k}}{1 \cdot 3 \cdot 5 \cdots(2 k+1)} .
$$

Substituting these values for the coefficients into $y$, we get the solution to the initial value problem
$$
y=x-\frac{1}{3} x^{3}+\frac{1}{15} x^{5}-\frac{1}{105} x^{7}+\cdots+\frac{(-1)^{k}}{1 \cdot 3 \cdot 5 \cdots(2 k+1)} x^{2 k+1}+\cdots
$$

This solution can be expressed in a more compact form (sce Exercise 23).

Polynomial approximations of the solution of Example 3 are grapl Figure 1. The more terms we include, the better the approximation i larger interval. Note that all the polynomials satisfy the initial condit

It is useful to remark that when solving initial value problems lik ample 3, using the power series method, we always have
$$
y(0)=a_{0} \quad \text { and } \quad y^{\prime}(0)=a_{1} .
$$

As should be expected, it is not always possible to find simple patter the coefficients in the solution. In such cases we can determine as many of the series as we wish in order to obtain a Taylor polynomial approxin of the solution.

EXAMPLE 4 Approximation by a Taylor polynomial
Find a fourth degree Taylor polynomial approximation of the solution of the value problem
$$
y^{\prime \prime}+e^{x} y=\cos x, \quad y(0)=1, \quad y^{\prime}(0)=0 .
$$

Solution In the notation of Theorem 1, we have $p(x)=0, q(x)=e^{x}$, and $\cos x$, and each of these functions has a power series expansion at 0 , valid $x$. Hence we have a power series solution, centered at 0 with an infinite ra convergence. Let us write this series as a Taylor series in the form
$$
y=\sum_{m=0}^{\infty} \frac{y^{(m)}(0)}{m!} x^{m} .
$$

---

<!-- Page 46 -->

Left margin note (page 46)

A46
Appendix A

![](./images/66923605-2b3e-4154-b144-3e182be82ea5-46_334_468_1019_63.jpg)

Figure 2 Polynomi $n$ ) approximation o tion.

Right margin note (page 46)

obtain
on and 0 ) $=0$, om the
c,

Taylor
Here is
ee 4 is This mial of to get
fy lin-
3. the

2, in
$y_{2}$ by
initial
1.
e's difted in pplica-

++++

Ordinary Differential Equations: Review of Concepts and Methods

Our goal is to determine the first five coefficients, $a_{0}, a_{1}, \ldots, a_{5}$, in order to a Taylor polynomial approximation
$$
P_{4}(x)=y(0)+y^{\prime}(0) x+\frac{y^{\prime \prime}(0)}{2!} x^{2}+\frac{y^{\prime \prime \prime}(0)}{3!} x^{3}+\frac{y^{(4)}(0)}{4!} x^{4} .
$$

Instead of using the power series method, we will use the differential equati the initial conditions directly. Indeed the initial conditions, $y(0)=1$ and $y^{\prime}($ give us immediately the first two coefficients of the Taylor polynomial. Fr differential equation, we have
$$
\begin{aligned}
y^{\prime \prime} & =-e^{x} y+\cos x \\
y^{\prime \prime}(0) & =-e^{0} y(0)+\cos (0)=(-1)(1)+1=0 ; \\
y^{\prime \prime \prime} & =\left[-e^{x} y+\cos x\right]^{\prime}=-e^{x} y-e^{x} y^{\prime}-\sin x, \\
y^{\prime \prime \prime}(0) & =-e^{0} y(0)-e^{0} y^{\prime}(0)-\sin (0)=-1 ; \\
y^{(4)} & =\left[-e^{x}\left(y+y^{\prime}\right)-\sin x\right]^{\prime}=-e^{x}\left(y+y^{\prime}\right)-e^{x}\left(y^{\prime}+y^{\prime \prime}\right)-\cos ; \\
y^{(4)}(0) & =-1-1=-2 .
\end{aligned}
$$

Thus $P_{4}(x)=1-(1 / 3!) x^{3}-(2 / 4!) x^{4}=1-x^{3} / 6-x^{4} / 12$ is the fourth-degree polynomial approximation of the solution.

We can continue this procedure and find as many terms as we please. the seventh-degree Taylor polynomial approximation
$$
P_{7}(x)=1-\frac{1}{6} x^{3}-\frac{1}{12} x^{4}+\frac{1}{120} x^{6}+\frac{19}{5,040} x^{7} .
$$

On the interval $[-1,1]$, the graph of the approximating polynomial of deg indistinguishable from the graph of the polynomial of degree 7 (Figure 2) suggests that on this interval we have a good approximation with a polyno degree 4. However, as we move away from the center, more terms are needed a good approximation.

In second-order homogeneous problems, it is instructive to ident, early independent solutions $y_{1}$ and $y_{2}$. As we saw in Examples 2 and recurrence relations allowed us to solve for the coefficients $a_{m}, m \geq$ terms of $a_{0}$ and $a_{1}$. We can define $y_{1}$ by taking $a_{0}=1, a_{1}=0$ and taking $a_{0}=0, a_{1}=1$. Then the general solution can be written as
$$
y=c_{1} y_{1}+c_{2} y_{2} .
$$

In terms of initial value problems, it is casily seen that $y_{1}$ satisfies the values $y_{1}(a)=1, y_{1}^{\prime}(a)=0$. Similarly, $y_{2}$ satisfies $y_{2}(a)=0, y_{2}^{\prime}(a)=$

The following example deals with a particular case of a Legendr ferential equation. A detailed treatment of these equations is preser Sections 5.5 and 5.6. This treatment is one of the most important a tions of the power series method in this book.

---

<!-- Page 47 -->

Section A. 5 The Power Series Method, Part II

EXAMPLE 5 A Legendre's differential equation
Solve the initial value problem
$$
\left(1-x^{2}\right) y^{\prime \prime}-2 x y^{\prime}+12 y=0, \quad y(0)=0, \quad y^{\prime}(0)=1 .
$$

Solution Put the equation in standard form:
$$
y^{\prime \prime}-\frac{2 x}{1-x^{2}} y^{\prime}+\frac{12}{1-x^{2}} y=0 .
$$

In the notation of Theorem 1, we have $p(x)=-2 x /\left(1-x^{2}\right)$ and $q(x)=12 /(1-$ From the geometric series, $\sum_{m=0}^{\infty} x^{m}=1 /(1-x)$, which is valid for $|x|<1$, obtain
$$
\frac{1}{1-x^{2}}=\sum_{m=0}^{\infty} x^{2 m} \quad \text { and } \quad \frac{x}{1-x^{2}}=\sum_{m=0}^{\infty} x^{2 m+1},
$$
where both swries converge for all $\left|x^{2}\right|<1$ or $|x|<1$. From this it follows $p(x)$ and $q(x)$ have power series expansions about 0 with radius of converge equal to 1 . Theorem 1 guarantees that the solution has a power series expan at 0 with radius of convergence at least equal to 1 . To find this solution, $y=\sum_{m=0}^{\infty} a_{m} x^{m}$ and its first and second derivatives into the equation and get
$$
\begin{array}{c}
\left(1-x^{2}\right) \sum_{m=2}^{\infty} m(m-1) a_{m} x^{m-2}-2 x \sum_{m=1}^{\infty} m a_{m}, x^{m-1}+12 \sum_{m=0}^{\infty} a_{m} x^{m}=0 ; \\
\sum_{m=2}^{\infty} m(m-1) a_{m} x^{m-2}-\sum_{m=2}^{\infty} m(m-1) a_{m} x^{m} \\
-\sum_{m=1}^{\infty} 2 m a_{m} x^{m}+12 \sum_{m=0}^{\infty} a_{m} x^{m}=0 .
\end{array}
$$

Changing $m$ to $m+2$ in the first series in the second equation and simplifying
$$
\begin{array}{c}
\sum_{m=0}^{\infty}(m+2)(m+1) a_{m+2} x^{m}-\sum_{m=1}^{\infty} m(m-1) a_{m} x^{m} \\
-\sum_{m=1}^{\infty} 2 m a_{m} x^{m}+12 \sum_{m=0}^{\infty} a_{m} x^{m}=0 ; \\
2 a_{2}+12 a_{0}+\sum_{m=1}^{\infty}[(m+2)(m+1) a_{m+2}+a_{m}(\overbrace{-m(m-1)-2 m+12}^{(m-3)(m+4)})] x^{m},
\end{array}
$$
where we have split off the $m=0$ terms from the series in order to start all of th at $m=1$. Setting the coefficients in the series equal to 0 and simplifying, we ob the relations
$$
2 a_{2}+12 a_{0}=0 ; \quad a_{m+2}=a_{m} \frac{(m-3)(m+4)}{(m+2)(m+1)} \quad(m \geq 1) .
$$

The initial conditions determine $a_{0}$ and $a_{1}$. Indeed, $a_{0}=y(0)=0$ and $a_{1}=y^{\prime}(0$ 1. The two step-recurrence relation determines the remaining coefficients. F

---

<!-- Page 48 -->

Left margin note (page 48)

A48
Appendix A
Ordina

Right margin note (page 48)

$\because \geq 0$. on, we and so on is a
will adii of $p(x)$ cadius 3 ; in
on

To find hat we 3)(4) $=$
$y_{2}$ has
lution appen $y=0$ Many 5 and

++++

ry Differential Equations: Review of Concepts and Methods

$a_{0}=0$, we get that $a_{2}=0, a_{4}=0$, and, more generally, $a_{2 k}=0$ for all We now turn to the odd indices. Taking $m=1$ in the recurrence relatio obtain: $a_{3}=a_{1}(-10) / 6=-5 / 3$. Next, we take $m=3$ and find $a_{5}=0$, $a_{7}=0, a_{9}=0$, and, more generally, $a_{2 k+1}=0$ for all $k \geq 1$. Thus the soluti polynomial:
$$
y=a_{1} x+a_{3} x^{3}=x-\frac{5}{3} x^{3}
$$

This can be verified directly from the equation: $y^{\prime}=1-5 x^{2}, y^{\prime \prime}=-10 x$, so
$$
\left(1-x^{2}\right) y^{\prime \prime}-2 x y^{\prime}+12 y=\left(1-x^{2}\right)(-10 x)-2 x\left(1-5 x^{2}\right)+12\left(x-\frac{5}{3} x^{3}\right)=
$$

The initial conditions are obviously verified.
Recall that Theorem 1 guarantees that the power series solutio have a radius of convergence at least as large as the smallest of the ra convergence of the power series expansions of the coefficient function and $q(x)$. Keep in mind, though, that the solution may have a larger 1 of convergence. In Example 5 one solution is a polynomial of degree particular, its radius of convergence is infinite.

We next derive the general solution of the equation in Example 5.

EXAMPLE 6 General solution of a Legendre's differential equat
Find two linearly independent solutions of Legendre's equation
$$
\left(1-x^{2}\right) y^{\prime \prime}-2 x y^{\prime}+12 y=0
$$

Solution In Example 5 we found one particular solution, $y_{1}=x-(5 / 3) \cdot x^{3}$. a second linearly independent solution, we return to the recurrence relation $t$ found in the previous solution and let $a_{0}$ be arbitrary. This gives $a_{2}=a_{0} \frac{(-:}{(2} -6 a_{0} . a_{4}=a_{2} \frac{(-1)(6)}{(4)(3)}=3 a_{0}, a_{6}=a_{4} \frac{(1)(8)}{(6)(5)}=\frac{4}{5} a_{0}$, and so on. Thus,
$$
y_{2}=a_{0}\left(1-6 x^{2}+3 x^{4}+\frac{4}{5} x^{6}+\cdots\right)
$$

The solution is an infinite power series in even powers of $x$. Unlike $y_{1}$, infinitely many nonzero terms.

The fact that Legendre's equation in Example 5 has a polynomial so and an infinite series solution is not a coincidence. Indeed this will ha every time the equation can be put in the form $\left(1 \quad x^{2}\right) y^{\prime \prime}-2 x y^{\prime}+n(n+1)$ for some nonnegative integer $n$. (In Example 5, we have $n=3$.) interesting facts about Legendre's equation can be found in Sections 5. 5.6.

---

<!-- Page 49 -->

Right margin note (page 49)

A 19
ver se-
on for
series

is dif-
on the a first second
on the
ered at n. (b) pproxlowest aterval
tion of

++++

Section A. 5 The Power Series Method, Part II

Exercises A. 5
In Exercises 1 12, show that 0 is an ordinary point, and then find the pou ries solutions cuntered at 0 . In each case, write down the recurrence relati the coefficients, and compute at least three nonzero terms from each power solution.
1. $y^{\prime}+2 x y=0$.
2. $y^{\prime}+y=0$.
3. $y^{\prime}+y=x$.
4. $y^{\prime}+(\cos x) y=0$.
5. $y^{\prime \prime}-y=0$.
6. $y^{\prime \prime}-y=x$.
7. $y^{\prime \prime}-x y^{\prime}+y=0$.
8. $y^{\prime \prime}+2 y^{\prime}+2 y=0$.
9. $y^{\prime \prime}+2 x y^{\prime}+y=0$.
10. $y^{\prime \prime}+x y^{\prime}+y=0$.
11. $y^{\prime \prime}-2 y^{\prime}+y=0, \quad y(0)=0, y^{\prime}(0)=1$.
12. $y^{\prime \prime}-2 y^{\prime}+y=x, \quad y(0)=2, y^{\prime}(0)=1$.

In Exercises 13-16, use the power series method to solve the given Logendr ferential equation.
13. $\left(1-x^{2}\right) y^{\prime \prime}-2 x y^{\prime}+2 y=0, y(0)=0, y^{\prime}(0)=3$.
14. $\left(1-x^{2}\right) y^{\prime \prime}-2 x y^{\prime}+6 y=0, \quad y(0)=1, \quad y^{\prime}(0)=1$.
15. $\left(1-x^{2}\right) y^{\prime \prime}-2 x y^{\prime}+12 y=0, \quad y(0)=1, \quad y^{\prime}(0)=0$.
16. $\left(1-x^{2}\right) y^{\prime \prime}-2 x y^{\prime}+2 y=0, y(0)=1, y^{\prime}(0)=0$.
17. Find two linearly independent solutions of $\left(1-x^{2}\right) y^{\prime \prime}-2 x y^{\prime}+2 y=0$ interval $-1<x<1$. [Hint: From the power series method, one solution is degree polynomial. You may use the reduction of order formula to find a linearly independent solution.]
18. Find two linearly independent solutions of $\left(1-x^{2}\right) y^{\prime \prime}-2 x y^{\prime}+6 y=0$ interval $-1<x<1$.
In Exercises 19-22, (a) justify the existence of a power series solution cent 0, and then find a fifth-degree Taylor polynomial approximation of the solutic With the help of a computer, find higher-degree Taylor polynomials that a imate the solution. Plot them on the interval $[-2,2]$, and then decide the degree needed in order to obtain a good approximation of the solution on the ir $[-1,1]$.
19. $y^{\prime \prime}-y^{\prime}+2 y=e^{x}, \quad y(0)=0, \quad y^{\prime}(0)=1$.
20. $y^{\prime \prime}+(\sin x) y=x, y(0)=0, y^{\prime}(0)=1$.
21. $y^{\prime \prime}+e^{x} y=0, \quad y(0)=1, y^{\prime}(0)=0$.
22. $y^{\prime \prime}+x y=\cosh x, y(0)=0, y^{\prime}(0)=1$.
23. Show that the solution in Example 3 is
$$
y=\sum_{k=0}^{\infty} \frac{(-1)^{k} 2^{k} k!}{(2 k+1)!} x^{2 k+1}
$$
24. Airy's differential equation. In this exercise, we find a series solut Airy's equation
$$
y^{\prime \prime}-x y=0
$$

---

<!-- Page 50 -->

Left margin note (page 50)

A50
Appendix A
Ordi

Right margin note (page 50)

utions
ee-step
and $y_{2}$.
$x$, and
rential
rential
rential
cosine
linear
[Hint:
${ }_{2} C(x)$.

++++

nary Differential Equations: Review of Concepts and Methods
(a) State why the solutions of the differential equation have power series so with infinite radius of convergence.
(b) Assume that $y=\sum_{m=0}^{\sim} a_{m} x^{m}$. Show that $a_{2}=0$ and derive the thr recurrence relation
$$
(m+2)(m+1) a_{m+2}=a_{m-1}, \quad m=1,2,3, \ldots .
$$
(c) Show that the general solution is
$$
\begin{aligned}
y= & a_{0}\left[1+\sum_{n=1}^{\infty} \frac{x^{3 n}}{(3 n)(3 n-1)(3 n-3) \ldots 3 \cdot 2}\right] \\
& +a_{1}\left[x+\sum_{n=1}^{\infty} \frac{x^{3 n+1}}{(3 n+1)(3 n)(3 n-2) \ldots 4 \cdot 3}\right] .
\end{aligned}
$$
(d) Write $y=a_{0} y_{1}+a_{1} y_{2}$ and plot several polynomial approximations of $y_{1}$ Note that for negative values of $x$ the graphs look like those of $\sin x$ and $\cos$ for positive values of $x$ the graphs look like those of $e^{x}$. Examine the differe equation and give a reason for these observations.
25. Solve the following initial value problem for Airy's equation:
$$
y^{\prime \prime}-x y=0, \quad y(0)=1, y^{\prime}(0)=0 .
$$
26. The sine and cosine functions. In this exercise, we show how a differ equation can be used to derive properties of its solutions. We refer to the diffe equation of Example 2 with the two linearly independent solutions
$$
C(x)=\sum_{k=0}^{\infty}(-1)^{k} \frac{1}{(2 k)!} x^{2 k} \quad \text { and } \quad S(x)=\sum_{k=0}^{\infty}(-1)^{k} \frac{1}{(2 k+1)!} x^{2 k+1} .
$$

We pretend for now that we do not recognize these functions as the sine and functions, and we derive their basic properties from the differential equatior
(a) Show that $C^{\prime}(x)=-S(x)$ and $S^{\prime}(x)=C(x)$.
(b) Using Abel's form of the Wronskian, show that $C^{2}(x)+S^{2}(x)=1$.
(c) Using the fact that any solution of the differential equation $y^{\prime \prime}+y=0$ is a combination of $C(x)$ and $S(x)$, show that $S(x+a)=S(x) C(a)+C(x) S(a)$.
Show that $S(x+a)$ is a solution and conclude that $S(x+a)=c_{1} S(x)+c$ Determine the constants by evaluating at $x=0$.]
(d) Establish the identity
$$
C(x+a)=C(x) C(a)-S(x) S(a) .
$$
(e) Which trigonometric identities are implied by (c) and (d)?

---

<!-- Page 51 -->

Left margin note (page 51)

A. 6 The Method

Right margin note (page 51)

A51

rhaps there od by point. ns, it ns at scries
have If $a$ ection point is our ls
have a ation. $y=$ ceeded

++++

Section A. 6 The Method of Frobenius

of Frobenius
While the method of power series is useful in many situations, and pe the most widely applicable method that we have developed thus far, are still important differential equations that cannot be fully understo this method. For example, consider Bessel's equation
$$
x^{2} y^{\prime \prime}+x y^{\prime}+\left(x^{2}-p^{2}\right) y=0 .
$$

Putting it in standard form, we see that $x=0$ is not an ordinary Hence, Theorem 1 of Appendix A. 5 does not apply. For applicatio is of particular importance to understand the behavior of the solutio $x=0$. To this end, we will develop a generalization of the power method, known as the method of Frobenius.

Consider the homogeneous differential equation
$$
y^{\prime \prime}+p(x) y^{\prime}+q(x) y=0 .
$$

Recall that $a$ is an ordinary point of the differential equation if $p$ and $q$ power series expansions at $a$. Otherwise, $a$ is called a singular point is an ordinary point, then we know from our work in the preceding se that the solutions of this equation have power series expansions at the $x=a$. If $a$ is a singular point, then the method of power series fails, 2 next example shows.

EXAMPLE 1 An equation for which the power series method fai Consider the differential equation $x y^{\prime \prime}+2 y^{\prime}+x y=0$.
(a) Determine whether $x=0$ is an ordinary or singular point.
(b) Apply the method of power series at $x=0$ to the differential equation.

Solution (a) We have $p(x)=2 / x$, and $q(x)=1$. Since $p(x)$ does not 1 power series expansion at $x=0$, the point $x=0$ is a singular point of the equ
(b) We assume that $y$ has a power series representation centered at $x= \sum_{m=0}^{\infty} a_{m} x^{m}$. Substituting into the differential equation and reindexing as gives
$$
\begin{array}{c}
\sum_{m=2}^{\infty} m(m-1) a_{m} x^{m-1}+\sum_{m=1}^{\infty} 2 m a_{m} x^{m-1}+\sum_{m=0}^{\infty} a_{m} x^{m+1}=0 ; \\
\sum_{m=1}^{\infty}(m+1) m a_{m+1} x^{m}+\sum_{m=0}^{\infty} 2(m+1) a_{m+1} x^{m}+\sum_{m=1}^{\infty} a_{m-1} x^{m}=0 ; \\
2 a_{1}+\sum_{m=1}^{\infty}\left[m(m+1) a_{m+1}+2(m+1) a_{m+1}+a_{m-1}\right] \cdot r^{m}=0
\end{array}
$$

Equating coefficients, we find that $a_{1}=0$ and
$$
m(m+1) a_{m+1}+2(m+1) a_{m+1}+a_{m-1}=0, \quad \text { for all } m,
$$

---

<!-- Page 52 -->

Left margin note (page 52)

A52
Appendix A Ordinary

![](./images/66923605-2b3e-4154-b144-3e182be82ea5-52_317_462_514_59.jpg)

Figure 1 Graph of $y=\frac{\sin x}{x}$.

Right margin note (page 52)

adexed
$\frac{\sin x}{x}$
iverges nearly on and endent should
nearly not a
turns bad" hat is, rest r only series
oth of (This

++++

Differential Equations: Review of Concepts and Methods
from which we get the two-step recurrence relation
$$
a_{m+1}=-\frac{1}{(m+2)(m+1)} a_{m-1} .
$$

Since $a_{1}=0$, it follows that $a_{3}=a_{5}=a_{7}=\cdots=0$. For the even it coefficients we have
$$
\begin{array}{l}
a_{2}=-\frac{1}{3 \cdot 2} a_{0}=-\frac{1}{3!} a_{0} \\
a_{4}=-\frac{1}{5 \cdot 4} a_{2}=\frac{1}{5!} a_{0} \\
a_{6}=-\frac{1}{7 \cdot 6} a_{4}=-\frac{1}{7!} a_{0}
\end{array}
$$

It is clear how this sequence continues. Thus one solution is
$$
y=a_{0}\left(1-\frac{x^{2}}{3!}+\frac{x^{4}}{5!}-\frac{x^{6}}{7!}+\cdots\right)=\frac{a_{0}}{x}\left(x-\frac{x^{3}}{3!}+\frac{x^{5}}{5!}-\frac{x^{7}}{7!}+\cdots\right)=a_{0}
$$
(Figure 1).
(Note that the function $\frac{\sin x}{x}$ has a power series expansion at $x=0$ that con for all $x$.) Since the differential equation is of second order, we need two 1 independent solutions. The method of power series yielded only one solutic hence failed to give the general solution. To get a second linearly indep solution, we can use the method of reduction of order, which gives (you check this)
$$
y=\frac{\cos x}{x} .
$$
(See also Exercise 29.)
Put simply, the method of power series failed to generate both li independent solutions in Example 1 because one of those solutions is power series. To see why, we write
$$
\frac{\cos x}{x}=x^{-1}\left(1-\frac{x^{2}}{2!}+\frac{x^{4}}{4!}-\frac{x^{6}}{6!}+\cdots\right) .
$$

This is not a power series, since it contains a negative power of $x$. It out that if the singular point of a differential equation is not "very then the solutions follow a pattern similar to that of Example 1. T at least one solution is a power series multiplied by $x^{r}$. We devote th of this section to making this idea precise. For simplicity, we conside series expansions about $x=0$, although analogous methods apply for expanded about an arbitrary $x=a$.

Suppose that $x=0$ is a singular point of the equation
$$
y^{\prime \prime}+p(x) y^{\prime}+q(x) y=0 .
$$

We say that $x=0$ is a regular singular point of the equation if $b$ the functions $x p(x)$ and $x^{2} q(x)$ have power series expansions at $x=0$.

---

<!-- Page 53 -->

Right margin note (page 53)

A53

penius 0 is a to the to the ple 1 ,
scries.
cxpo-
$x p(x)$

++++

Section A. 6 The Method of Frobenius

is what we mean by a singularity that is not "very bad.") The Frob method that we now describe applies to equations for which $x=$ regular singular point. For clarity's sake, we restrict our attention case $x>0$. The case $x<0$ is handled similarly (or can be reduced case $x>0$ by the change of variables $t=-x$ ). Motivated by Exam we try a series solution of the form
$$
y=x^{r}\left(a_{0}+a_{1} x+a_{2} x^{2}+\cdots\right)=\sum_{m=0}^{\infty} a_{m} x^{r+m}
$$
with $a_{0} \neq 0$. Such a series is called a Frobenius series. We have
$$
y^{\prime}=\sum_{m=0}^{\infty} a_{m}(r+m) x^{r+m-1}
$$
and
$$
y^{\prime \prime}=\sum_{m=0}^{\infty} a_{m}(r+m)(r+m-1) x^{r+m-2} .
$$
(Observe that the index of summation begins at 0 in both these Why?) Thus (2) becomes
$$
\begin{array}{l}
\sum_{m=0}^{\infty} a_{m}(r+m)(r+m-1) x^{r+m-2} \\
\quad+p(x) \sum_{m=0}^{\infty} a_{m}(r+m) x^{r+m-1}+q(x) \sum_{m=0}^{\infty} a_{m} x^{r+m}=0 .
\end{array}
$$

We factor $x$ from the second series and $x^{2}$ from the third to make all nents the same and get
$$
\begin{array}{l}
\sum_{m-0}^{\infty} a_{m}(r+m)(r+m-1) x^{r+m-2} \\
\quad+x p(x) \sum_{m=0}^{\infty} a_{m}(r+m) x^{r+m-2}+x^{2} q(x) \sum_{m=0}^{\infty} a_{m} x^{r+m-2}=0 .
\end{array}
$$

Since by assumption $x=0$ is a regular singular point, the functions and $x^{2} q(x)$ have power series expansions about 0 , say
$$
x p(x)=p_{0}+p_{1} x+p_{2} x^{2}+\cdots
$$
and
$$
x^{2} q(x)=q_{0}+q_{1} x+q_{2} x^{2}+\cdots
$$

---

<!-- Page 54 -->

Left margin note (page 54)

A54
Appendix A

THEO
FROB
METHOD
SOL

Right margin note (page 54)

ration pears $a_{0}=$ dicial ed by Note s) and $r_{1}$ in power p, we
hat $r_{1}$

EquaIt can nverge

This The

++++

Ordinary Differential Equations: Review of Concepts and Methods

Substituting these into (4) gives
$$
\begin{array}{l}
\sum_{m=0}^{\infty} a_{m}(r+m)(r+m-1) x^{r+m-2} \\
\quad+\left(p_{0}+p_{1} x+p_{2} x^{2}+\cdots\right) \sum_{m=0}^{\infty} a_{m}(r+m) r^{r+m-2} \\
\quad+\left(q_{0}+q_{1} x+q_{2} x^{2}+\cdots\right) \sum_{m=0}^{\infty} a_{m} x^{r+m-2}=0 .
\end{array}
$$

The total coefficient of each power of $x$ on the left side of this eqr must be 0 , since the right side is 0 . The lowest power of $x$ that ar in the equation is $x^{r-2}$. Its coefficient is $a_{0} r(r-1)+p_{0} a_{0} r+q_{0} a_{0}\left[r(r-1)+p_{0} r+q_{0}\right]=0$. Since $a_{0} \neq 0, r$ must be a root of the in equation
$$
r(r-1)+p_{0} r+q_{0}=0 .
$$

The roots of this equation are called the indicial roots and are denot $r_{1}$ and $r_{2}$ with the convention that $r_{1} \geq r_{2}$ whenever they are real. that $p_{0}$ and $q_{0}$ are easily determined, since they are the values of $x p(x) x^{2} q(x)$ at $x=0$. Once we have determined $r_{1}$ and $r_{2}$, we substitute (4) and solve for the unknown coefficients $a_{n}$ as we would do with the series method. This will determine a first solution of (2). Summing 1 have the following important result.

REM 1 ENIUS FIRST UTION

If $x=0$ is a regular singular point of the equation
$$
y^{\prime \prime}+p(x) y^{\prime}+q(x) y=0 .
$$
then one solution is of the form
$$
y_{1}=|x|^{r_{1}}\left(a_{0}+a_{1} x+a_{2} x^{2}+\cdots\right), \quad a_{0} \neq 0,
$$
where $r_{1}$ is a root of the indicial equation (5), with the convention is the larger of the two roots when both roots are real.

For a proof of this theorem, see Chapter 9 of Ordinary Differential tions by Garrett Birkhoff and Gian-Carlo Rota, 2nd ed., Wiley, 1969. be shown that if $x p(x)$ and $x^{2} q(x)$ have power series expansions that col for $|x|<R$, then the series solution will converge for $0<|x|<R$.

Note that Theorem 1 says nothing about a second solution of (2). solution may have one of three forms, as described in the following box proofs are presented in an appendix at the end of this section.

---

<!-- Page 55 -->

Right margin note (page 55)

A55
ation

on has
).
'ase 1
Frobe-
olve a
$l_{0}=1$
ng the
nd $y_{2}$.
power
puation
nteger, p is to

++++

Section A. 6 The Method of Frobenius

Suppose that $x=0$ is a regular singular point of the differential eque
$$
y^{\prime \prime}+p(x) y^{\prime}+q(x) y=0 .
$$
and let $r_{1}$ and $r_{2}$ denote the indicial roots. The differential equati two linearly independent solutions $y_{1}$ and $y_{2}$, as we now describe.
Case 1. If $r_{1}-r_{2}$ is not an integer, then
$$
y_{1}=|x|^{r_{1}} \sum_{m=0}^{\infty} a_{m} x^{m}, \quad y_{2}=|x|^{r_{2}} \sum_{m=0}^{\infty} b_{m} x^{m}, \quad a_{0} \neq 0 \text { and } b_{0} \neq
$$

Case 2. If $r=r_{1}=r_{2}$, then
$$
y_{1}=|x|^{r} \sum_{m=0}^{\infty} a_{m} x^{m}, \quad y_{2}=y_{1} \ln |x|+|x|^{r} \sum_{m=1}^{\infty} b_{m} \cdot x^{m}, \quad a_{0} \neq 0 .
$$

Case 3. If $r_{1}-r_{2}$ is a positive integer, with $r_{1} \geq r_{2}$, then
$$
y_{1}=|x|^{r_{1}} \sum_{m=0}^{\infty} a_{m} x^{m}, \quad y_{2}=k y_{1} \ln |x|+|x|^{r_{2}} \sum_{m=0}^{\infty} b_{m} x^{m} .
$$
where $a_{0} \neq 0, b_{0} \neq 0$ ( $k$ may or may not be 0 ).
Thus we find two linearly independent Frobenius series solutions in and also in Case 3 when $k=0$. Otherwise we can find only one nius series solution, and any linearly independent solution must inv logarithmic term. In computing $y_{1}$ and $y_{2}$ it is convenient to take ( and $b_{0}=1$; then the two arbitrary constants will appear when writi general solution in the form of an arbitrary linear combination of $y_{1}$ a

EXAMPLE 2 Frobenius method: $r_{1}-r_{2}$ is not an integer
Solve the differential equation
$$
y^{\prime \prime}+\frac{1}{2 x} y^{\prime}-\frac{1}{4 x} y=0, \quad x>0 .
$$

Solution Theorem 1 applies, since both $x p(x)=\frac{1}{2}$ and $x^{2} q(x)=-\frac{1}{4} x$ have series expansions at $x=0$. Morcover, $p_{0}=\frac{1}{2}$ and $q_{0}=0$, so the indicial eo and indicial roots are
$$
\begin{array}{c}
r(r-1)+\frac{1}{2} r=0 \\
r^{2}-\frac{1}{2} r=0 \\
r_{1}=\frac{1}{2} \text { and } r_{2}=0
\end{array}
$$
(Following our convention, we choose $r_{1} \geq r_{2}$.) Since $r_{1}-r_{2}$ is not an i the solutions are given by Case I of the Frobenius method. The next ste

---

<!-- Page 56 -->

Left margin note (page 56)

A56
Appendix A Ordinary

Right margin note (page 56)

enient
of $x$.)
$$
0+r-1
$$
$\frac{1}{2}$, the
$=1$ is

++++

Differential Equations: Review of Concepts and Methods
determine the unknown coefficients in the series solutions. It is more conv to work with the differential equation if we multiply both sides by $4 x$ :
$$
4 x y^{\prime \prime}+2 y^{\prime}-y=0 .
$$

Substituting $y=\sum_{m=0}^{\infty} a_{m} x^{m+r}$ into the equation gives
$$
\begin{aligned}
\sum_{m=0}^{\infty} 4 a_{m}(m+r)(m+r-1) x^{m+r-1} & \\
+\sum_{m=0}^{\infty} 2 a_{m}(m+r) x^{m+r-1}-\sum_{m=1}^{\infty} a_{m-1} x^{m+r-1} & =0
\end{aligned}
$$
(We have shifted the index in the third series to match all the exponents Adding the terms corresponding to $m=0$ and setting the coefficient of $x$ equal to 0 gives us the indicial equation
$$
\begin{array}{l}
4 a_{0} r(r-1)+2 a_{0} r=0 \\
r^{2}-\frac{1}{2} r=0 \quad\left(\text { since } a_{0} \neq 0\right)
\end{array}
$$

Setting the sum of the coefficients of $x^{m+r-1}$ equal to 0 gives us
$$
4 a_{m}(m+r)(m+r-1)+2 a_{m}(m+r)-a_{m-1}=0 .
$$

At this point, we treat separately the case $r_{1}=\frac{1}{2}$ and $r_{2}=0$. When $r=$ recurrence relation (6) becomes
$$
\begin{array}{l}
4 a_{m}\left(m+\frac{1}{2}\right)\left(m+\frac{1}{2}-1\right)+2 a_{m}\left(m+\frac{1}{2}\right)-a_{m-1}=0 \\
a_{m}=\frac{1}{2 m(2 m+1)} a_{m-1} .
\end{array}
$$

From this recurrence relation we get the pattern
$$
\begin{array}{rlrl}
a_{1} & =\frac{1}{2 \cdot 3} a_{0} & =\frac{1}{3!} a_{0}, & a_{4} \\
a_{2} & =\frac{1}{4 \cdot 5} a_{1} & =\frac{1}{5!} a_{3}=\frac{1}{9!} a_{0} \\
a_{3} & =\frac{1}{6 \cdot 7} a_{2}= & \frac{1}{7!} a_{0} & =\frac{1}{10 \cdot 11} a_{4}=\frac{1}{11!} a_{0}
\end{array}
$$

Thus $a_{m}=\frac{1}{(2 m+1)!} a_{0}$, and hence the solution corresponding to $r=\frac{1}{2}$ and $a_{0}$
$$
y_{1}=\sum_{m=0}^{\infty} \frac{1}{(2 m+1)!} x^{m+\frac{1}{2}}
$$

For $r=0$ we get the recurrence relation (6):
$$
\begin{array}{l}
4 a_{m} m(m-1)+2 a_{m} m-a_{m-1}=0 \\
a_{m}=\frac{1}{2 m(2 m-1)} a_{m-1}
\end{array}
$$

---

<!-- Page 57 -->

Left margin note (page 57)

![](./images/66923605-2b3e-4154-b144-3e182be82ea5-57_348_426_592_49.jpg)

Figure 2 Solutions and partial sum approximation from Example 2.

![](./images/66923605-2b3e-4154-b144-3e182be82ea5-57_378_463_1585_56.jpg)

Figure 3 Approximation of $y_{1}$ near 0 . Notice the blow-up due to the term $\frac{1}{x}$.

Right margin note (page 57)

A57
0 and
$$
\text { ere } c_{1}
$$
lity of gure 2 how of a
tion is Let ons as
nfinite ing to

++++

Section A. 6 The Method of Frobenius

This gives the following pattern for the coefficients:
$$
\begin{array}{rlrl}
a_{1} & =\frac{1}{2 \cdot 1} a_{0} & =\frac{1}{2!} a_{0}, & a_{4}=\frac{1}{8 \cdot 7} a_{3}=\frac{1}{8!} a_{0} \\
a_{2} & =\frac{1}{4 \cdot 3} a_{1}= & \frac{1}{4!} a_{0}, & a_{5}=\frac{1}{10 \cdot 9} a_{4}=\frac{1}{10!} a_{0} \\
a_{3} & =\frac{1}{6 \cdot 5} a_{2}= & \frac{1}{6!} a_{0},
\end{array}
$$

It is clear that $a_{m}=\frac{1}{(2 m)!} a_{0}$, and hence the solution corresponding to $r= a_{0}=1$ is
$$
y_{2}=\sum_{m=0}^{\infty} \frac{1}{(2 m)!} x^{m} .
$$

Thus the general solution of the differential equation is $y=c_{1} y_{1}+c_{2} y_{2}$, wh and $c_{2}$ are arbitrary constants.

The solutions in Example 2 can be simplified as
$$
y_{1}=\sinh \sqrt{x} \quad \text { and } \quad y_{2}=\cosh \sqrt{x}, \quad x>0 .
$$

Do you see why? [Hint: Write $x^{m}$ as $(\sqrt{x})^{2 m}$.] We can verify the valic these solutions by plugging them into the differential equation. In Fig we compare the graphs $\cosh \sqrt{x}$ and the partial sums of $y_{2}$. Notic the partial sums of $y_{2}$ approximate the real solution. With the aic computer system, you can do the same for $y_{1}$.

EXAMPLE 3 Case of a double root $r=r_{1}=r_{2}$
Solve the differential equation
$$
x^{2} y^{\prime \prime}+3 x y^{\prime}+(1-x) y=0, \quad x>0 .
$$

Solution We easily verify that $p_{0}=3, q_{0}=1$, and so the indicial equa $r^{2}+2 r+1=0$. We have a double root $r=-1$, and so we are in Case 2 $y_{1}=\sum_{m=0}^{\infty} a_{m} x^{m-1}$ with $a_{0} \neq 0$. Substituting in (7), after some computati in Example 2, we arrive at the recurrence relation
$$
a_{m+1}=\frac{a_{m}}{(m+1)^{2}}
$$

Taking $a_{0}=1$, we get the first solution
$$
y_{1}=\sum_{m=0}^{\infty} \frac{1}{(m!)^{2}} x^{m-1}=\frac{1}{x}\left(1+x+\frac{x^{2}}{4}+\frac{x^{3}}{36}+\frac{x^{4}}{576}+\cdots\right) .
$$
(An approximation of $y_{1}$ is shown in Figure 3, using a partial sum of the i series. The details of the derivation of $y_{1}$ are left to Exercise 30.) Accord Case 2, we try for a second solution
$$
y=y_{1} \ln x+\sum_{m=1}^{\infty} b_{m} x^{m-1} .
$$

---

<!-- Page 58 -->

Left margin note (page 58)

A58
Appendix A Ordinary

Right margin note (page 58)

series
rive at
ugh it rst five
...).

++++

Differential Equations: Review of Concepts and Methods

Substituting in (7) and simplifying, we get
$$
\begin{array}{l}
{[\overbrace{x^{2} y_{1}^{\prime \prime}+3 x y_{1}^{\prime}+(1-x) y_{1}}^{=0}] \ln x+\left(2 x y_{1}^{\prime}+2 y_{1}\right)} \\
\quad+\sum_{m=1}^{x} b_{m}(m-1)(m-2) x^{m-1}+\sum_{m=1}^{\infty} 3 b_{m}(m-1) x^{\prime \prime \prime-1} \\
\quad+\sum_{m=1}^{\infty} b_{m} x^{m-1}-\sum_{m=2}^{\infty} b_{m-1} x^{m-1}=0
\end{array}
$$

The coefficient of $\ln x$ in (8) is 0 , since $y_{1}$ is a solution of (7). From the representation of $y_{1}$ we see that
$$
\begin{aligned}
2 x y_{1}^{\prime}+2 y_{1} & =2\left[\sum_{m=0}^{\infty} \frac{m-1}{(m!)^{2}} x^{m-1}+\sum_{m=0}^{\infty} \frac{1}{(m!)^{2}} x^{m-1}\right] \\
& =\sum_{m=0}^{\infty} \frac{2 m}{(m!)^{2}} x^{m-1}=\sum_{m=1}^{\infty} \frac{2}{(m-1)!m!} x^{m-1}
\end{aligned}
$$

After substituting this into (8) and combining terms with like powers, we ar the equation
$$
\left(2+b_{1}\right)+\sum_{m=2}^{\infty}\left(\frac{2}{(m-1)!m!}+m^{2} b_{m}-b_{m-1}\right) x^{m-1}=0 .
$$

Thus $b_{1}=-2$, and the recurrence relation for the $b_{m}$ 's is
$$
b_{m}=\frac{1}{m^{2}}\left(b_{m-1}-\frac{2}{(m-1)!m!}\right)
$$

From this relation we can calculate as many coefficients as we wish, althe would be difficult to find a closed formula for $b_{m}$ in terms of $m$. Using the $f$ coefficients, we have
$$
y_{2}=\ln x \sum_{m=0}^{\infty} \frac{1}{(n!)^{2}} x^{m-1}-\left(2+\frac{3}{4} x+\frac{11}{108} x^{2}+\frac{25}{3,456} x^{3}+\frac{137}{432,000} x^{4}+\right.
$$

Hence the general solution of (7) is
$$
\begin{aligned}
y= & c_{1} y_{1}+c_{2} y_{2} \\
= & \left(c_{1}+c_{2} \ln x\right) \sum_{m=0} \frac{1}{(m!)^{2}} x^{m-1} \\
& -c_{2}\left(2+\frac{3}{4} x+\frac{11}{108} x^{2}+\frac{25}{3.456} x^{3}+\frac{137}{432,000} x^{4}+\cdots\right),
\end{aligned}
$$
where $c_{1}$ and $c_{2}$ are arbitrary constants.

---

<!-- Page 59 -->

Right margin note (page 59)

A59
$3=0$.
lution
icients
e form
that
in the
obtain

++++

Section A. 6 The Method of Frobenius

EXAMPLE 4 Case $r_{1}-r_{2}$ is an integer
Solve the differential equation
$$
x^{2} y^{\prime \prime}-x y^{\prime}+(x-3) y=0, \quad x>0 .
$$

Solution We have $p_{0}=-1, q_{0}=-3$, and so the indicial equation is $r^{2}-2 r-$ The indicial roots are $r_{1}=3$ and $r_{2}=-1$. We are in Case 3. For a first so we try $y_{1}=\sum_{m=0}^{\infty} a_{m} x^{m+3}$. Substituting in (9) and solving for the coeff $a_{m}$, we arrive at the recurrence relation
$$
a_{m}=\frac{-1}{m^{2}+4 m} a_{m-1},
$$
from which we get
$$
y_{1}=a_{0} x^{3}\left(1-\frac{1}{5} x+\frac{1}{60} x^{2}-\frac{1}{1,260} x^{3}+\frac{1}{40,320} x^{4}-\cdots\right) .
$$

The details are left as an exercise (Exercise 31). The second solution is of th
$$
y=k y_{1} \ln x+\sum_{m=0}^{\infty} b_{m} x^{m-1},
$$
where $k$ may or may not be 0 . We substitute this in (9), simplify, use the fac $y_{1}$ is a solution, and get
$$
\begin{array}{l}
{[\overbrace{x^{2} y_{1}^{\prime \prime}-x y_{1}^{\prime}+(x-3) y_{1}}^{=0}] \ln x+2 k\left(x y_{1}^{\prime}-y_{1}\right)} \\
\quad+\sum_{m=0}^{\infty} b_{m}(m-1)(m-2) x^{m-1}-\sum_{m=0}^{\infty} b_{m}(m-1) x^{m-1} \\
\quad-\sum_{m=0}^{\infty} 3 b_{m} x^{m-1}+\sum_{m=1}^{\infty} b_{m-1} x^{m-1}=0
\end{array}
$$

The lowest power of $x$ appearing in the term $2 k\left(x y_{1}^{\prime}-y_{1}\right)$ is $x^{3}$, so we obta following equation upon simplification:
$$
\begin{array}{c}
\left(b_{0}-3 b_{1}\right)+\left(b_{1}-4 b_{2}\right) x+\left(b_{2}-3 b_{3}\right) x^{2}+2 k\left(x y_{1}^{\prime}-y_{1}\right) \\
+\sum_{m=4}^{\alpha}\left[b_{m}\left(m^{2}-4 m\right)+b_{m-1}\right] x^{m-1}=0
\end{array}
$$

Taking $b_{0}=1$, setting the first three coefficients equal to 0 , and solving, we
$$
b_{1}=\frac{1}{3}, \quad b_{2}=\frac{1}{12}, \quad b_{3}=\frac{1}{36} .
$$

Now from (10) it follows that
$$
2 k\left(x y_{1}^{\prime}-y_{1}\right)=2 k\left(2 x^{3}-\frac{3}{5} x^{4}+\frac{1}{15} x^{5}-\frac{1}{252} x^{6}+\cdots\right),
$$

---

<!-- Page 60 -->

Left margin note (page 60)

A60
$\Lambda$ ppendix A
Ordinary

Right margin note (page 60)

of the n turn choose
thmic hand, ppen. 0 and ation,
using ion of
m by in the with
$$
=-1 .
$$
outset

++++

Differential Equations: Review of Concepts and Methods
and so, setting the coefficient of $x^{3}$ in (11) equal to 0 , we get
$$
4 k+b_{3}=0 .
$$

Thus $k=-\frac{1}{4} b_{3}=-\frac{1}{144}$. We can now continue to use (11) to find as many coefficients $b_{4}, b_{5}, \ldots$ as we wish, by setting the coefficients of $x^{4}, x^{5}, \ldots$ i equal to zero. Omitting the details, we find that $b_{4}$ is arbitrary (so we $b_{4}=1$ ), and so $b_{5}=-\frac{121}{600}$. Hence
$$
y_{2}=-\frac{1}{144} y_{1} \ln x+x^{-1}\left(1+\frac{1}{3} x+\frac{1}{12} x^{2}+\frac{1}{36} x^{3}+x^{4}-\frac{121}{600} x^{5}+\cdots\right)
$$

So the general solution of (9) is
$$
\begin{aligned}
y= & c_{1} y_{1}+c_{2} y_{2} \\
= & x^{3}\left(c_{1}-c_{2} \frac{\ln x}{144}\right)\left(1-\frac{1}{5} x+\frac{1}{60} x^{2}-\frac{1}{1,260} x^{3}+\frac{1}{4,032} x^{4}-\cdots\right. \\
& +c_{2} x^{-1}\left(1+\frac{1}{3} x+\frac{1}{12} x^{2}+\frac{1}{36} x^{3}+x^{1}-\frac{121}{600} x^{5}+\cdots\right),
\end{aligned}
$$
where $c_{1}$ and $c_{2}$ are arbitrary constants.
In the preceding example the second solution $y_{2}$ contained a logari term, since the constant $k$ turned out to be nonzero. On the other Example 1 deals with a Case 3 equation in which this does not ha Indeed, the indicial equation is $r(r-1)+2 r=0$ with roots $r_{1}= r_{2}=-1$ that differ by a positive integer, and the solutions of the equ $y_{1}=\frac{\sin x}{x}$ and $y_{2}=\frac{\cos x}{x}$, do not contain a logarithmic term.
Use of the Reduction of Order Formula
In all three cases of the Frobenius method, once we have found $y_{1}$ Theorem 1), a second solution can be derived by using the reduct order formula:
$$
y_{2}(x)=y_{1}(x) \int \frac{e^{-\int p(x) d x}}{y_{1}^{2}(x)} d x
$$

To get the series for $y_{2}$, we expand the integrand and integrate ter term. This process is illustrated by our next example and is justified appendix of this section. The task of expanding is greatly simplific the help of a computer.

EXAMPLE 5 The reduction of order formula
Find the general solution of the differential equation
$$
x^{2} y^{\prime \prime}+x y^{\prime}+\left(x^{2}-1\right) y=0, \quad x>0 .
$$

Solution The indicial equation is $r^{2}-1=0$ with indicial roots $r_{1}=1$ and $r_{2}$ (Note that the indicial roots differ by an integer, so we cannot assume at the

---

<!-- Page 61 -->

Right margin note (page 61)

A61 of the on and of the
d.r.
$-\cdots)$
$+\cdots)$.
pol for
thod
plution ct our
serics

++++

Section A. 6 The Method of Frobenius

that the solutions are both of the form (3).) By Theorem 1, one solution is form $y_{1}=x^{r_{1}} \sum_{m=0}^{\infty} a_{m} x^{m}$ with $r_{1}=1$. Plugging in the differential equati solving for the coefficients as in the previous examples, we find
$$
y_{1}=x\left(1-\frac{x^{2}}{8}+\frac{x^{4}}{192}-\frac{x^{6}}{9,216}+\frac{x^{8}}{737,280}-\frac{r^{10}}{88,473,600}+\cdots\right)
$$
(Exercise 32). We find a second linearly independent solution with the help reduction of order formula. Putting $y_{1}$ in (12) we get
$$
\begin{aligned}
y_{2}(x)= & y_{1} \int \frac{e^{-\int 1 / x d x}}{y_{1}^{2}} d x \quad\left(e^{-\int 1 / x d x}=\frac{1}{x}\right) \\
= & y_{1} \int \frac{1}{x^{3}\left(1-\frac{x^{2}}{8}+\frac{x^{4}}{192}-\frac{x^{6}}{9,216}+\frac{x^{8}}{737,280}-\frac{x^{10}}{88,473,600}+\cdots\right)^{2}} d x \\
= & y_{1} \int \frac{1}{x^{3}\left(1-\frac{x^{2}}{4}+\frac{5 x^{4}}{192}-\frac{7 x^{6}}{4,608}+\frac{7 x^{8}}{122,880}-\frac{11 x^{10}}{7,372,800}+\cdots\right)} d x \\
& \quad \text { (Squaring) } \\
= & y_{1} \int\left(\frac{1}{x^{3}}+\frac{1}{4 x}+\frac{7 x}{192}+\frac{19 x^{3}}{4.608}+\frac{149 x^{5}}{368,640}+\frac{803 x^{7}}{22,118,400}+\cdots\right) \\
& \quad \text { (Series expansion or long division) } \\
= & y_{1}\left(\frac{-1}{2 x^{2}}+\frac{1}{4} \ln x+\frac{7 x^{2}}{384}+\frac{19 x^{4}}{18,432}+\frac{149 x^{6}}{2,211,840}+\frac{803 x^{8}}{176,947,200}-\right. \\
& \quad \text { (Integrate term by term) } \\
= & y_{1} \frac{\ln x}{4}+y_{1}\left(\frac{-1}{2 x^{2}}+\frac{7 x^{2}}{384}+\frac{19 x^{4}}{18,432}+\frac{149 x^{6}}{2,211,840}+\frac{803 x^{8}}{176,947,200}\right.
\end{aligned}
$$

This determines a second linearly independent solution.

Example 5 shows that the reduction of order formula is a handy to checking for the presence of a logarithmic term in the solution.

Appendix: Further Proofs Related to the Frobenius Me In this appendix we use the reduction of order formula to derive the second s in the Frobenius problems. given the first one by Theorem 1. We restri attention to the case $x>0$.

Recall that $x p(x)$ has a power series at $x=0$. Thus we have
$$
\begin{aligned}
x p(x) & =p_{0}+p_{1} x+p_{2} x^{2}+\cdots \\
p(x) & =\frac{p_{0}}{x}+p_{1}+p_{2} x+\cdots
\end{aligned}
$$

We denote the function $p_{1}+p_{2} x+\cdots$ by $a(x)$ (note that $a(x)$ has a power expansion at $x=0$ ), and so
$$
p(x)=\frac{p_{0}}{x}+a(x) .
$$

Integrating and taking the exponential, we get
$$
e^{-\int p(r) d x}=x^{-p_{0}} G(x),
$$

---

<!-- Page 62 -->

Left margin note (page 62)

A62
Appendix A
Ordinary

Right margin note (page 62)

$G$ has
power
that
are the
occurs
$r_{1}-r_{2}$
hence
since
have
nt. In
ermine
onzero

++++

Differential Equations: Review of Concepts and Methods
where $G$ is the function $e^{-\int a(x) d x}$, and, in particular, $G(0) \neq 0$. (Note that a power series expansion at $x=0$.) Now, using Theorem 1, we can write
$$
\frac{1}{y_{1}^{2}}=\frac{1}{x^{2 r_{1}}} H(x),
$$
where $H(x)=1 /\left(\sum_{m=0}^{\infty} a_{m} x^{m}\right)^{2}$. Since $a_{0} \neq 0$, the function $H(x)$ has a series expansion at 0 and $H(0) \neq 0$. Combining (12), (13), and (14), we fin
$$
y_{2}=y_{1} \int x^{-p_{0}-2 r_{1}} K(x) d x
$$
where $K(x)$ has a power series expansion about 0 , and $K(0) \neq 0$. We write
$$
K(x)=k_{0}+k_{1} x+k_{2} x^{2}+\cdots, \quad k_{0} \neq 0 .
$$

At this point, we establish a connection between $r_{1}, r_{2}, p_{0}$. Since $r_{1}$ and $r_{2}$ roots of equation (5), we have $r_{1}+r_{2}=1-p_{0}$. Thus (15) becomes
$$
y_{2}=y_{1} \int x^{-\left(r_{1}-r_{2}+1\right)}\left(k_{0}+k_{1} x+k_{2} x^{2}+\cdots\right) d x, \quad k_{0} \neq 0 .
$$

Note that a logarithmic term in $y_{2}$ will appear if and only if a term in $x^{-1}$ in the integrand (after multiplying through by $x^{-\left(r_{1}-r_{2}+1\right)}$ ). This is why $r$ determines the nature of the second solution.
Case 1: If $r_{1}-r_{2}$ is not an integer, clearly there can be no tcrm in $x^{-1}$, and no logarithmic term in $y_{2}$.
Case 2: If $r_{1}=r_{2}$, then the very first term yields the logarithmic term in $y_{2} k_{0} \neq 0$.
Case 3: If $r_{1}-r_{2}$ is a positive integer, say $r_{1}-r_{2}=n$, we may or may no a logarithmic term, depending on whether $k_{n}$ is 0 .

Exercises A. 5
In Exercises 1-6, decide whether $x=0$ is an ordinary point or a singular poi case it is a singular point, determine if it is a regular singular point.
1. $y^{\prime \prime}+\left(1-x^{2}\right) y^{\prime}+x y=0$.
2. $x y^{\prime \prime}+\sin x y^{\prime}+\frac{1}{x} y=0$.
3. $x^{3} y^{\prime \prime}+x^{2} y^{\prime}+y=0$.
4. $\sin x y^{\prime \prime}+y^{\prime}+\frac{1}{x} y=0$.
5. $x^{2} y^{\prime \prime}+\left(1-e^{x}\right) y^{\prime}+x y=0$.
6. $3 x y^{\prime \prime}+2 y^{\prime}-\frac{1}{3 x} y=0$.

In Exercises 7-22, (a) check that $x=0$ is a regular singular point. (b) Det which case of the Frobenius method applies. (c) Determine at least three $n$ terms in each of two linearly independent scries solutions. Take $x>0$.
7. $4 x y^{\prime \prime}+6 y^{\prime}+y=0$.
8. $4 x y^{\prime \prime}+6 y^{\prime}-y=0$.
9. $4 x^{2} y^{\prime \prime}-14 x y^{\prime}+(20-x) y=0$.
10. $4 x y^{\prime \prime}+2 y^{\prime}+y=0$.
11. $2 x y^{\prime \prime}+(1+x) y^{\prime}+y=0$.
12. $y^{\prime \prime}-\frac{1}{2 x} y^{\prime}+\frac{1}{x} y=0$.
13. $x y^{\prime \prime}+(1-x) y^{\prime}+y=0$.
14. $x y^{\prime \prime}+2 y^{\prime}-x y=0$.
15. $x y^{\prime \prime}+2(1+x) y^{\prime}+(x+2) y=0$.
16. $x^{2} y^{\prime \prime}+x y^{\prime}+\left(x^{2}-\frac{1}{4}\right) y=0$.

---

<!-- Page 63 -->

Right margin note (page 63)

A63

0 .
d then iple 5.
ample.
of the ngular ad two
on
od apof the ge can to an
near 0

++++

Section A. 6 The Method of Frobenius
17. $x^{2} y^{\prime \prime}+4 x y^{\prime}+\left(2-x^{2}\right) y=0$.
19. $x y^{\prime \prime}+3 y^{\prime}+\frac{1+x}{x} y=0$.
21. $x y^{\prime \prime}+y^{\prime}-\frac{1+x}{x} y=0$.
18. $x y^{\prime \prime}+(x+2) y^{\prime}+(x+1) y=$
20. $x^{2} y^{\prime \prime}+4 x y^{\prime}+\left(2+x^{2}\right) y=0$.
22. $4 x y^{\prime \prime}+2 y^{\prime}+x y=0$.

In Exercises 23-28, determine which case of the Frobenius method applies. an solve the equation using Theorem 1 and reduction of order as we did in Exan Does your second solution contain a logarithmic term?
23. $4 x^{2} y^{\prime \prime}-14 x y^{\prime}+(20+x) y=0, \quad x>0$.
24. $y^{\prime \prime}-\frac{1+x^{2}}{2 x} y^{\prime}+\frac{1}{2 x^{2}} y=0, \quad x>0$.
25. $y^{\prime \prime}+\frac{1}{x} y^{\prime}+\frac{1}{y^{2}} y=0, \quad x>0$.
26. $y^{\prime \prime}-\frac{1+x}{2 x} y^{\prime}+\frac{1+2 x}{2 x^{2}} y=0, x>0$.
27. $x(1-x) y^{\prime \prime}+(1-3 x) y^{\prime}-y=0, \quad 0<x<1$.
28. $x(1-x) y^{\prime \prime}-\frac{1}{4} y=0, \quad 0<x<1$.
29. (a) Make the change of variables $u=x y$ in the differential equation of Ex 1 and show that it becomes $u^{\prime \prime}+u=0$.
(b) Use (a) to derive the solutions $y_{1}=\frac{\sin x}{x}$ and $y_{2}=\frac{\cos x}{x}$.
30. Derive the first solution in Example 3.
31. Supply the details leading to the first solution in Example 4.
32. Supply the details leading to the first solution in Example 5.

Euler's equation can be used to illustrate the solutions in all thro cases Frobenius method. In Exercises 33-36, (a) show that $x=0$ is a regular si point, and determine which case of the Frobenius method applies. (b) Fix linearly independent solutions, using the methods of Section. A.3.
33. $y^{\prime \prime}+\frac{1}{x} y^{\prime}-\frac{2}{x^{2}} y=0$.
34. $y^{\prime \prime}+\frac{2}{x} y^{\prime}-\frac{3}{x^{2}} y=0$.
35. $y^{\prime \prime}+\frac{1}{x} y^{\prime}+\frac{1}{9 x^{2}} y=0$.
36. $y^{\prime \prime}+\frac{1}{2 x} y^{\prime}+\frac{1}{2 x^{2}} y=0$.
37. (a) Show that $x=0$ is a regular singular point of the differential equati
$$
(\sin x)^{2} y^{\prime \prime}+\tan x y^{\prime}+(\cos x)^{2} y=0
$$
(b) Find the indicial roots and determine which case of the Frobenius meth plies.
(c) Verify that $\left.y_{1}=\sin (\ln (\sin x))\right)$ and $\left.y_{2}=\cos (\ln (\sin x))\right)$ are solutions differential equation for $0<x<R$, where $R$ is a positive number. How lar $R$ be?
(d) Make a change of variables $u=\sin x$ and transform the given equation Euler rquation. Then derive the solutions given in (c).
(e) Plot the graphs of the solutions. Explain the behavior of the graphs and $\pi$.

---

<!-- Page 64 -->

Left margin note (page 64)

A64 Appendix A Ordinary

Right margin note (page 64)

and od. onding
benius / 2 can ary.]
and od. onding
can be ary.]

++++

Differential Equations: Review of Concepts and Methods
38. Consider the equation
$$
x y^{\prime \prime}-(2+x) y^{\prime}+2 y=0, \quad x>0 .
$$
(a) Show that $x=0$ is a regular singular point. Find the indicial equatic the indicial roots. and conclude that we are in Case 3 of the Frobenius meth
(b) Use the method of Frobenius to find a Frobenius series solution correspe to the larger root $r_{1}$.
(c) Identify the solution in (b) as $3!\left(c^{r}-1-x-\frac{s^{2}}{2}\right)$.
(d) Even though the roots differ by an integer, there exists a sccond Fro series solution. Using the method of Frobenius, show that $e^{x}$ or $1+x+x^{2}$ be taken as a second solution. [Hint: Argue that the coefficient $b_{3}$ is arbitr
39. Consider the equation
$$
x y^{\prime \prime}-(n+x) y^{\prime}+n y=0, \quad x>0,
$$
where $n$ is a nonnegative integer.
(a) Show that $x=0$ is a regular singular point. Find the indicial equatic the indicial roots, and conclude that we are in Case 3 of the Frobenius meth
(b) Use the method of Frobenius to find a Frobenius series solution corresper to the larger root $r_{1}$.
(c) Identify the solution in (b) as
$$
(n+1)!\left(e^{r}-1-x-\frac{x^{2}}{2}-\cdots-\frac{x^{n}}{n!}\right) .
$$
(d) Using the method of Frobenius, show that $e^{x}$ or $1+x+x^{2} / 2+\cdots+\frac{x^{n}}{n!}$ taken as a second solution. [Hint: Argue that the coefficient $b_{n+1}$ is arbitra
