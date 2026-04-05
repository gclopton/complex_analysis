<!-- Page 1 -->

Left margin note (page 1)

Topics to Review
Strictly speaking, the numerical techniques of this chapter do not require previous knowledge of partial differential equations. However, to appreciate these techniques, a familiarity with the boundary value problems of Chapter 3 is required. In particular, the analytical solutions that we developed in Sections 3.3, 3.5, 3.7, and 3.8 are useful in treating their numerical counterparts. This chapter can be covered right after Chapter 3.

Looking Ahead...
In Section 9.1 we present the finite difference method and apply it to the heat equation. Section 9.1 is essential to the rest of the chapter. In Section 9.2 we apply the finite difference method for the wave equation, and in Section 9.3 we apply this method to Laplace's equation. Section 9.4 expands on the ideas of Section 9.3. For the sake of clarity, we chose simple problems to illustrate the numerical methods. However, you should keep in mind that these methods work equally well with more complicated problems and are very well suited for real-world applications.

Right margin note (page 1)

ZAC
you oints me $t$ s for tical ,$\left.t_{k}\right)$. the crete lytiwill tizaor a ation after erate
cornthe ence e adsome $r$ the with apter sepaates, ions. can

++++

9

FINITE DIFFERENCE NUMERICAL METHODS

Numbers are intellectual witnesses that belong only to mankind.
-HONORÉ DE BAL
Suppose that you are studying a concrete heat problem and that want to know the temperature at times $t_{1}, t_{2}, \ldots, t_{n}$ of certain $p x_{1}, x_{2}, \ldots, x_{m}$ in a bar. If $u(x, t)$ denotes the temperature at ti of the point $x$, then what you are looking for is a table of value $u\left(r_{j}, t_{k}\right)$, where $1 \leq j \leq m$ and $1 \leq k \leq n$. When an analy solution is available, you may be able to use it to compute $u\left(x_{j}\right.$ However, in many practical problems, it is impossible to comput analytical solutions, since the data is known only on a set of dis points.

To remedy this situation, we may forgo the search for an and cal solution in favor of a numerical solution. In this chapter you study numerical methods that are based on the principle of discre tion. By discretizing a problem, you come up with an algorithm formula that can be used to generate numerical values of the solu at a discrete set of points. For example, in the heat problem, discretizing, you arrive at a formula which can be iterated to gene a numerical solution.

With ubiquity of computers capable of carrying out numerical putations to a very high degree of accuracy, at a minimum cost to user, the numerical methods are gaining more and more promin in the world of engineering and science. Moreover, they enjoy the vantage of being applicable with few constraints, as compared to s of the analytical methods. For example, the numerical scheme fo heat equation (Section 9.1) applies with equal ease to problems a variety of boundary conditions. As you may recall from Che 3 , with the analytical methods we had to treat these problems s rately. Also, in solving Dirichlet problems in rectangular coordin with the analytical methods we had to restrict to rectangular reg You will see in Sections 9.3 and 9.4 that the numerical methods be applied to less regular regions.

---

<!-- Page 2 -->

Left margin note (page 2)

516
Chapter 9
F
9.1 The Fir

![](./images/3d691698-445f-4a4d-96f7-0cb184e4b380-02_690_1074_1118_561.jpg)

Figure 1 Gridpoin $x t$-plane. To march time, we increase the $t_{j}$.

Right margin note (page 2)

olving e heat of the of the lytical with and a grid of t $n-1 h, 2 h$, values that that

++++

inite Difference Numerical Methods

iite Difference Method for the Heat Equation
To gain some insight and understanding of numerical techniques for s partial differential equations, we start by considering the case of th equation for a finite bar. This example will illustrate the key ideas finite difference method and will allow us to measure the success numerical methods, by comparing their results with those of the ana solution of Section 3.5.

Let us recall the heat boundary value problem for an insulated ba ends held at temperature 0 ,
$$
\begin{aligned}
u_{t} & =c^{2} u_{x x}, & & 0<x<L, t>0, \\
u(0, t) & =0, & & u(L, t)=0, t>0, \\
u(x, 0) & =f(x), & & 0 \leq x \leq L .
\end{aligned}
$$

Discretizing the Heat Problem
The idea is to discretize the problem by choosing a stepsize $h$ in $x$ stepsize $k$ in $t$ and trying to approximate the temperature $u$ on a points in the $x t$-plane. Say we want to approximate the values of $u$ a equally spaced points between 0 and $L$.

Take
$$
h=L / n
$$
and divide the interval from 0 to $L$ into $n$ parts by choosing $x= \ldots,(n-1) h$. Similarly, we pick a $k$ and consider only the time $t=0, k, 2 k, 3 k, \ldots$. Thus, we want to develop a numerical schen

---

<!-- Page 3 -->

Right margin note (page 3)

517
Fig-
leter-
$\iota-1$ )
wing
with
wice)

++++

Section 9.1 The Finite Difference Method for the Heat Equation
yields approximations for the values
$$
u_{i j}=u(i h, j k), \quad \text { where } 0<i<n \text { and } j \geq 0 .
$$

That is, $u_{i j}$ will represent the value of $u$ at the gridpoint $(i h, j k)$ (see ure 1).

At this point we would like to formulate a rule, based on (1), for $d$ mining the values $u_{i j}$ for a certain time from the values $u_{i, j-1}(1 \leq i \leq r$ one time step back. To arrive at this rule we take a hint from the follo limits:
$$
\lim _{k \rightarrow 0} \frac{u(x, t+k)-u(x, t)}{k}=\frac{\partial u}{\partial t}(x, t),
$$
and
$$
\lim _{h \rightarrow 0} \frac{u(x+h, t)-2 u(x, t)+u(x-h, t)}{h^{2}}=\frac{\partial^{2} u}{\partial x^{2}}(x, t) .
$$

The first of these is just the definition of the partial derivative of $u$ respect to $t$. The second one may be verified using L'Hospital's rule (t as follows:
$$
\begin{aligned}
\lim _{h \rightarrow 0} & \frac{u(x+h, t)-2 u(x, t)+u(x-h, t)}{h^{2}} \\
& =\lim _{h \rightarrow 0} \frac{u_{x}(x+h, t)-u_{x}(x-h, t)}{2 h} \\
& =\lim _{h \rightarrow 0} \frac{u_{x x}(x+h, t)+u_{x x}(x-h, t)}{2}=\frac{\partial^{2} u}{\partial x^{2}}(x, t)
\end{aligned}
$$

Thus, if $k$ is sufficiently small, we have
$$
u_{t}(x, t) \approx \frac{u(x, t+k)-u(x, t)}{k},
$$
and, if $h$ is sufficiently small, we have
$$
u_{x x}(x, t) \approx \frac{u(x+h, t)-2 u(x, t)+u(x-h, t)}{h^{2}} .
$$

Hence, at our gridpoints $(i h, j k)$ we have the approximations

---

<!-- Page 4 -->

Left margin note (page 4)

518
Chapter 9
Finite Differe

DISCRETIZATION OF FIRST DERIVATIVE

DISCRETIZATION OF SECOND DERIVATIVE

DISCRETIZATION OF THE HEAT EQUATION

Right margin note (page 4)

ation
alled a takes ashion 1), we
ation.
+ 1)th
$x, 0)=$

++++

ace Numerical Methods
(9)
$$
\begin{aligned}
u_{t}(i h, j k) & \approx \frac{u(i h, j k+k)-u(i h, j k)}{k} \\
& \approx \frac{1}{k}\left(u_{i, j+1}-u_{i j}\right)
\end{aligned}
$$
and, similarly, using (8),
$$
u_{x x}(i h, j k) \approx \frac{1}{h^{2}}\left(u_{i+1, j}-2 u_{i j}+u_{i-1, j}\right)
$$

The approximation (9) is called a forward difference approxim for the first partial derivative $u_{t}$, while the approximation (10) is ca centered second difference approximation for $u_{x x}$. The latter account of the values of $u$ about the gridpoint $(i, j)$ in a symmetric f (see Figure 1). Substituting the approximations (8) and (9) into ( obtain
$$
u_{i, j+1}-u_{i j}=c^{2} \frac{k}{h^{2}}\left(u_{i+1, j}-2 u_{i j}+u_{i-1, j}\right),
$$
which is our finite difference approximation to the heat equ Combining like terms and solving for $u_{i, j+1}$, we get
$$
u_{i, j+1}=(1-2 s) u_{i j}+s\left(u_{i+1, j}+u_{i} \quad 1, j\right),
$$
where
$$
s=\frac{c^{2} k}{h^{2}}
$$

From this we can compute the values $u_{i, j+1}$ corresponding to the $(j$ time step from the values $u_{i j}$ at the $j$ th time step.

Let us now discretize the boundary and initial conditions. Since $u( f(x)$, we get

---

<!-- Page 5 -->

Left margin note (page 5)

DISCRETIZA
OF THE INI CONDI

DISCRETIZA OF THE BOUNE CONDIT

![](./images/3d691698-445f-4a4d-96f7-0cb184e4b380-05_343_414_867_31.jpg)

Figure 2 Stepping in time in the hoat equ

Right margin note (page 5)

519
(11)
hrce
the
$u$ On
the
dary

After a the d in (11), the and your
blem

++++

Section 9.1 The Finite Difference Method for the Heat Equation

TION
TIAL
TION

TION
ARY IONS

$\bullet_{i+1, j}$
forward
ration.
$$
u_{i 0}=u(i h, 0)=f(i h), \quad 0 \leq i \leq n .
$$

Also, the boundary conditions (2) lead to
$$
u_{0 j}=u(0, j k)=0, \quad j>0,
$$
and
$$
u_{n j}=u(n h, j k)=u(L, j k)=0, \quad j>0 .
$$

We will need these boundary values as we use our difference equation to step forward in time, since to compute $u_{i, j+1}$ we typically need the $t$ values $u_{i-1, j}, u_{i j}$, and $u_{i+1, j}$. Thus when $i=1$ or $n-1$, we will noed values $u_{0 j}$ and $u_{n j}$.

The method is illustrated in the diagram in Figure 2. The values of the $x$-axis are determined by the initial condition. The values of $u$ on vertical lines $x=0$ (the $t$-axis) and $x=L$ are determined by the boun conditions. All other values of $u$ on the grid are computed from (11).

EXAMPLE 1 Temperature in a bar with ends held at $0^{\circ}$
A thin bar of unit length is placed in boiling water (temperature $100^{\circ} \mathrm{C}$ ). reaching $100^{\circ} \mathrm{C}$ throughout, the bar is removed from the boiling water. Witl lateral sides kept insulated, suddenly, at time $t=0$, the ends are immerse a medium with constant temperature $0^{\circ} \mathrm{C}$. Use the finite difference scheme together with the boundary and initial conditions (13)-(15), to approximate solution to this problem at the times $t=0.2,0.4,0.6,0.8$. and 1. Take $c=1 / 2$ use stepsizes $h=0.1$ (hence $n=10$ ) and $k=0.01$ (hence $s=1 / 4$ ). Compare values with the values obtained using separation of variables.

Solution Substituting $s=1 / 4$ into (11), we find that the boundary value pro to be solved is
$$
u_{i, j+1}=\left(u_{i+1, j}+2 u_{i j}+u_{i-1, j}\right) / 4,
$$
together with the boundary conditions
$$
u_{0 j}=u(0,0.01 j)=0, \quad j>0,
$$
and
$$
u_{10, j}=u(1,0.01 j)=0, \quad j>0,
$$

---

<!-- Page 6 -->

Left margin note (page 6)

520 Chapter 9 Finite Differer

Right margin note (page 6)

nethod get the ain the obtain ta that

| 1 |
| :---: |
| 100 |
| 0 |
| 0 |
| 0 |
hod.
ial sum roblem

the
ues

++++

ce Numerical Methods

and the initial condition
$$
u_{i 0}=u(0.1 i, 0)=f(0.1 i)=100, \quad 0 \leq i \leq 10 .
$$

Having all the necessary ingredients, we can now apply the finite difference i to obtain approximations of the solution $u$. From the initial data, we can values of $u$ at time $t=0.01$. Having done so. we use these values to obt values of $u$ at time $t=0.02$. Repeating this process eighteen more times, we the desired values at time $t=0.2$, and so on. In Table 1 we show some da results from this process, which was generated with the help of a computer.

\begin{table}
| $t \backslash x$ | 0 | 0.1 | 0.2 | 0.3 | 0.4 | 0.5 | 0.6 | 0.7 | 0.8 | 0.9 |  |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 0 | 100 | 100 | 100 | 100 | 100 | 100 | 100 | 100 | 100 | 100 |  |
| 0.01 | 0 | 100 | 100 | 100 | 100 | 100 | 100 | 100 | 100 | 100 |  |
| 0.02 | 0 | 75 | 100 | 100 | 100 | 100 | 100 | 100 | 100 | 75 |  |
| 0.03 | 0 | 62 | 94 | 100 | 100 | 100 | 100 | 100 | 94 | 62 |  |
\captionsetup{labelformat=empty}
\caption{Table 1 Temperature in the bar, generated with the finite difference met}
\end{table}

In Table 2 we compare the numerical solution to the values from a part approximation to the exact solution. The exact analytical solution to this p can be found using separation of variables (see Section 3.5) and is
$$
u(x, t)=\frac{400}{\pi} \sum_{m=0}^{\infty} \frac{e^{-(2 m+1)^{2} \pi^{2} t / 4}}{2 m+1} \sin (2 m+1) \pi x .
$$

\begin{table}
| \multicolumn{12}{\|c\|}{Finite difference method versus the analytical solution} |  |  |  |  |  |  |  |  |  |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| $t \backslash x$ | 0 | 0.1 | 0.2 | 0.3 | 0.4 | 0.5 | 0.6 | 0.7 | 0.8 | 0.9 | 1 |
| 0.2 | 0 0 | 25 24 | 47 46 | 64 63 | 75 74 | 78 77 | 75 74 | 64 63 | 47 46 | 25 24 | 0 0 |
| 0.4 | 0 0 | 15 15 | 28 28 | 39 38 | 46 45 | 48 47 | 46 45 | 39 38 | 28 28 | 15 15 | 0 0 |
| 0.6 | 0 0 | 9 9 | 17 17 | 24 23 | 28 28 | 29 29 | 28 28 | 24 23 | 17 17 | 9 9 | 0 0 |
| 0.8 | 0 0 | 6 5 | 10 10 | 14 14 | 17 17 | 18 18 | 17 17 | 14 14 | 10 10 | 6 5 | 0 0 |
| 1 | 0 0 | 3 3 | 6 6 | 9 9 | 10 10 | 11 11 | 10 10 | 9 9 | 6 6 | 3 3 | 0 0 |
\captionsetup{labelformat=empty}
\caption{Table 2 Cells with two entries contain the values of " generated with numerical solution (top) and the analytical solution (bottom). All val were rounded to the nearest integer.}
\end{table}

---

<!-- Page 7 -->

Left margin note (page 7)

![](./images/3d691698-445f-4a4d-96f7-0cb184e4b380-07_391_510_197_35.jpg)

Figure 3(a) Tempera bution at time $t=0.2$ with the finite differen

![](./images/3d691698-445f-4a4d-96f7-0cb184e4b380-07_391_518_197_622.jpg)

Figure 4 Temperatur bution as $x$ and $t$ va structed from the nu data in Table 2.

![](./images/3d691698-445f-4a4d-96f7-0cb184e4b380-07_398_516_190_1214.jpg)
![](./images/3d691698-445f-4a4d-96f7-0cb184e4b380-07_673_766_1158_754.jpg)

Right margin note (page 7)

521
$$
=30 .
$$

otted
lines
3(c)

of the
ble 1.
To rence

++++

Section 9.1 The Finite Difference Method for the Heat Equation
ture distri, generated ce method.

![](./images/3d691698-445f-4a4d-96f7-0cb184e4b380-21_276_425_897_37.jpg)
Figure 3(b) Temperature distribution at time $t=0.2$, generated with a partial sum (with $m=30$ ) of the analytical solution.

![](./images/3d691698-445f-4a4d-96f7-0cb184e4b380-21_276_425_897_37.jpg)
Figure 3(c) Comparison of the analytical and numerical solutions.

In our approximation by the analytical solution, we took a partial sum up to $m$ In Figure 3(b) we plotted this partial sum at $t=1 / 5$. In Figure 3(a) we pl the points $u(0.1 i, 1 / 5)$, for $i=0,1, \ldots, 10$, and connected them by straight to get a graph that approximates the real solution at time $t=1 / 5$. In Figure we superposed both graphs for comparison's sake.
e distriry, conimerical

Finally, we used the data in Table 2 to generate a three-dimensional plot surface $:=u(x, t)$, for $0<x<1$, and $0<t<1$ (Figure 4).

An important question comes to mind as we work through Examp Was our choice of $s=1 / 4$ arbitrary, or is there a reason behind it? answer this question, we take up the topic of stability of the finite diffe method.

---

<!-- Page 8 -->

Left margin note (page 8)

522
Chapter 9
Finite Diffcrer

Right margin note (page 8)

os the yield n that 1/2. gives
erence arison, with
ite u"s $=1 / 2$, for the
$$
>1 / 2
$$
1. The

++++

ice Numerical Methods

A Stability Criterion
When $s=1 / 2$, formula (11) takes on a particularly simple form
$$
u_{i, j+1}=\frac{1}{2}\left(u_{i+1, j}+u_{i-1, j}\right) .
$$

It may appear that $s=1 / 2$ is the natural choice, since it simplifi formula. However, it can be shown that smaller positive values of better approximations to the exact solution. In fact, it can be show the finite difference scheme (11) for the heat equation is unstable if $s$ The scheme is stable if $0<s \leq 1 / 2$, which means that the methoc reasonable approximations to the exact solution when $0<s \leq 1 / 2$.

As an illustration, let us revisit Example 1 and apply the finite diff method with $s=1 / 2$ (corresponding to $h=0.1, k=0.02$ ). For comp we show the results in Table 3, along with the results of the metho $s=1 / 4$, and the values of the analytical solution.

\begin{table}
| \multicolumn{12}{\|c\|}{Varying $s$ in the finite difference method} |  |  |  |  |  |  |  |  |  |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| $t \backslash x$ | 0 | 0.1 | 0.2 | 0.3 | 0.4 | 0.5 | 0.6 | 0.7 | 0.8 | 0.9 | 1 |
| \multirow{3}{*}{0.2} | 0 | 25 | 47 | 64 | 75 | 78 | 75 | 64 | 47 | 25 | 0 |
|  | 0 | 24 | 46 | 63 | 74 | 77 | 74 | 63 | 46 | 24 | 0 |
|  | 0 | 24 | 49 | 63 | 78 | 78 | 78 | 63 | 49 | 24 | 0 |
| \multirow{3}{*}{0.4} | 0 | 15 | 28 | 39 | 46 | 48 | 46 | 39 | 28 | 15 | 0 |
|  | 0 | 15 | 28 | 38 | 45 | 47 | 45 | 38 | 28 | 15 | 0 |
|  | 0 | 15 | 29 | 38 | 47 | 47 | 47 | 38 | 29 | 15 | 0 |
| \multirow{3}{*}{0.6} | 0 | 9 | 17 | 24 | 28 | 29 | 28 | 24 | 17 | 9 | 0 |
|  | 0 | 9 | 17 | 23 | 28 | 29 | 28 | 23 | 17 | 9 | 0 |
|  | 0 | 9 | 18 | 23 | 29 | 29 | 29 | 23 | 18 | 9 | 0 |
| \multirow{3}{*}{0.8} | 0 | 6 | 10 | 14 | 17 | 18 | 17 | 14 | 10 | 6 | 0 |
|  | 0 | 5 | 10 | 14 | 17 | 18 | 17 | 14 | 10 | 5 | 0 |
|  | 0 | 5 | 11 | 14 | 17 | 17 | 17 | 14 | 11 | 5 | 0 |
| \multirow{3}{*}{1} | 0 | 3 | 6 | 9 | 10 | 11 | 10 | 9 | 6 | 3 | 0 |
|  | 0 | 3 | 6 | 9 | 10 | 11 | 10 | 9 | 6 | 3 | 0 |
|  | 0 | 3 | 7 | 9 | 11 | 11 | 11 | 9 | 7 | 3 | 0 |
\captionsetup{labelformat=empty}
\caption{Table 3 Cells with three entries contain the values of $u$ from the fir difference method with $s=1 / 4$ (top), $s=1 / 2$ (bottom), and the val from the analytical solution (center).}
\end{table}

Table 3 confirms that the method works with the limiting value $s$ but better results are obtained with $s<1 / 2$.

We next illustrate the instability of the finite difference method heat equation with $s>1 / 2$.

EXAMPLE 2 Instability of the finite difference method: Case Here we will simply repeat Example 1 with $h=0.1$ and $k=0.04$, hence $s=$ values generated from (11) are shown in Table 4.

---

<!-- Page 9 -->

Right margin note (page 9)

523

| 1 |
| :---: |
| 100 |
| 0 |
| 0 |
| 0 |
| 0 |
| 0 |
large ne is
ty of $1,0)$. r all what For y for efine
eous data
data
$(t)=$ finite using

++++

Section 9.1 The Finite Difference Method for the Heat Equation

| \multicolumn{11}{\|c\|}{Instability of the finite difference method: $s>1 / 2$} |  |  |  |  |  |  |  |  |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| $t \backslash x$ | 0 | 0.1 | 0.2 | 0.3 | 0.4 | 0.5 | 0.6 | 0.7 | 0.8 | 0.9 |
| 0 | 100 | 100 | 100 | 100 | 100 | 100 | 100 | 100 | 100 | 100 |
| 0.04 | 0 | 100 | 100 | 100 | 100 | 100 | 100 | 100 | 100 | 100 |
| 0.08 | 0 | 0 | 100 | 100 | 100 | 100 | 100 | 100 | 100 | 0 |
| 0.12 | 0 | 100 | 0 | 100 | 100 | 100 | 100 | 100 | 0 | 100 |
| 0.16 | 0 | -100 | 200 | 0 | 100 | 100 | 100 | 0 | 200 | -100 |
| 0.20 | 0 | 300 | -300 | 300 | 0 | 100 | 0 | 300 | -300 | 300 |

Table 4 Results of the finite difference method with $s=1$
Note the appearance of negative values for the temperature. Also note the oscillations in the values. These are obvious signs that the numerical scher unstable when $s=1$.

An issue that bears mention is our treatment of the incompatibili the boundary and initial data at the "corner points" $(x, t)=(0,0)$ and $($ In Example 1, we took $u_{00}=100=u_{10,0}$; that is, we applied (19) fo $0 \leq i \leq 10$ but applied (17) and (18) only for $j>0$. Other choices for to do with these corner points might be made with equal justification. example, we might choose to apply (17) and (18) for $j \geq 0$ and (19) onl $0<i<10$, or, perhaps even better, we could take the average and d $u_{00}=50=u_{10,0}$. These alternatives are explored in the exercises.
Nonhomogeneous Boundary Conditions
The finite difference method works equally well with nonhomogen boundary conditions. That is, we can consider equation (1) with initial (3) and boundary conditions given by
$$
u(0, t)=\phi(t) \quad \text { and } \quad u(L, t)=\psi(t), t>0
$$

Following the discretization method above (see (14) and (15)), this translates into
$$
u_{0 j}=\phi(j k) \quad \text { and } \quad u_{n j}=\eta(j k), j>0,
$$
where $n=L / h$.

EXAMPLE 3 Steady-state solution
Consider the heat problem (1), (3), (20), with $c=1 / 2, L=1, \phi(t)=0, \psi$ 100 , and $f(x)=0$. We approximate the solution to this problem using the difference scheme given by (11), (13), and (21); that is, we shall iterate (11) the boundary conditions
$$
u_{0 j}=0 \quad \text { and } \quad u_{n j}=100, j>0,
$$
and the initial condition
$$
u_{i 0}=0, \quad 0 \leq i \leq n .
$$

---

<!-- Page 10 -->

Left margin note (page 10)

524
Chapter 9
F

![](./images/3d691698-445f-4a4d-96f7-0cb184e4b380-10_341_457_268_74.jpg)

Figure 5

Right margin note (page 10)

igure 5 e times nd one $00 x$. is
riables break of the s with
< 1/3, $x<1$.
imple 1
a value
process
hit your
consist-
$x)=0$,
0.1 and
).2, 0.4,
tion
fference
on

++++

nite Difference Numerical Methods

We take $h=0.1$ and $k=0.01$, and hence $n=10$ and $s=1 / 4$. In F we present our numerical solution for the temperature distribution at the $t=0.1$ and $t=1$. These were obtained by iterating formula (11) ten a hundred times, respectively. Note that the steady-state solution, $u(x, t)=1$ approached closely already by time $t=1$.

It is worthwhile to recall that when we used the separation of va method to solve nonhomogeneous problems, in many cases we had to the problem into several subproblems. By contrast, one nice feature finite difference method is that it handles these nonhomogeneous case no additional complications.

Exercises 9.1
In Exercises 1-4, repeat Example 1 for the given initial data.
1.
$$
f(x)=\left\{\begin{array}{ll}
100 x & \text { if } 0<x<1 / 2, \\
100(1-x) & \text { if } 1 / 2<x<1 .
\end{array}\right.
$$
2.
$$
f(x)=\left\{\begin{array}{ll}
100 \sin ^{2} 3 \pi x & \text { if } 0<x \\
45(1 / 3-x) & \text { if } 1 / 3<
\end{array}\right.
$$
3. $f(x)=\sin \pi x$.
4. $f(x)=x(1-x)$.

In Exercises 5-8, take $h=0.1$ and $k=0.02$ (hence $s=1 / 2$ ) and repeat $E x$ for the given initial data.
5. Take $f$ as in Exercise 1.
6. Take $f$ as in Exercise 2.
7. Take $f$ as in Excrcise 3.
8. Take $f$ as in Exercise 4.
9. Verify the instability of (11) by repeating Exercise 1 with your choice of of $s>1 / 2$.

In Exercises 10-13, discretize the given equation. That is, carry out the analogous to that employed in the text in passing from (1) to (11). and exhi finite difference analog of (11).
10. $u_{t}=c^{2} u_{x x}+3 u$.
11. $u_{t}=c^{2} u_{x x}+2$.
12. $u_{t}=u_{x x}+u_{x}+1$.
13. $u_{t}=2 u_{x}$.
14. Use the results of Exercise 11 to solve the heat boundary value problem ing of the equation in Excrcise 11 and the following data: $L=1, c=1 / 2, f$ ( $u(0, t)=u(1, t)=0$. When applying the finite difference method, take $h= k=0.01$. Find the approximate temperature distribution at the times $t=0$ 0.6, 0.8, and 1 .
15. Use l'Hospital's rule to justify the backward difference approxima
$$
u_{t}(i h, j k) \approx \frac{1}{k}\left(u_{i, j}-u_{i, j-1}\right)
$$
to the first partial derivative $u_{t}$ at the gridpoint $(i, j)$. [Hint: Consider the di quotient $\frac{u(x, t)-u(x, t-k)}{k}$.]
16. Use l'Hospital's rule to justify the centered difference approximati
$$
u_{t}(i h, j k) \approx \frac{1}{2 k}\left(u_{i, j+1}-u_{i, j-1}\right)
$$

---

<!-- Page 11 -->

Left margin note (page 11)

9.2 The Finite

Right margin note (page 11)

525

liffer-

That $\iota_{00}=$
$u_{10,0}$. evant those
ation ple 3. ee the
mate y the n the n the ation on is buted
of you e can time time
ction

++++

Section 9.2 The Finite Difference Method for the Wave Equation

to the first partial derivative $u_{t}$ at the gridpoint $(i, j)$. [Hint: Consider the ence quotient $\left.\frac{u(x, t+k)-u(x, t-k)}{2 k}\right]$.
17. Repeat Example 1 letting the boundary values determine $u_{00}$ and $u_{10.0}$. is, take the values at the "corner points" as $u_{00}=0=u_{10,0}$, rather than $100=u_{10.0}$ (as was done in Exerrise 1).
18. Repeat Example 1, taking the values at the corner points as $u_{00}=50=$ Thus, we are determining the values at the corner points as averages of the rel boundary and initial data. In fact, your answers here should be the average of from Example 1 and Exercise 17 (the superposition principle!).
In Exercises 19-20, you are asked to approximate the solution to the heat equ with nonhomogeneous boundary conditions. Model your solution after Exam but use the given boundary and initial data. Go to large enough time to se steady-state solution.
19. $u(x, 0)=0, u(0, t)=60, u(1 . t)=20$.
20. $u(x, 0)=400 x(1-x), u(0, t)=0, u(1, t)=40$.

Difference Method for the Wave Equation
In the previous section we used the finite difference method to approxi the solution of the heat problem for a finite rod. In this section we appl same ideas to the wave equation for a finite string. When dealing wit, heat problem, the values at the $(j+1)$ th time step were determined fror values at the $j$ th time step. This is due to the fact that the heat equ is first order in time. Here you will see that, because the wave equati second order in time, the values at the $(j+1)$ th time step will be comp from the values at the $j$ th and $(j-1)$ th time steps.

Recall that in the wave problem for a string, you are given the valu $u$ and $u_{t}$ at time $t=0$. As we said. to start the finite difference scheme need the values of $u$ at two consecutive time steps. You will see that w use the initial data for $u_{t}$ to generate a set of values of $u$ at the next step. Once these are determined, we use them along with the values at $t=0$ to iterate the finite difference scheme.

Let us recall the boundary value problem for the finite string from Se
3.3. It consists of the wave equation
$$
u_{t t}=c^{2} u_{x x}, \quad 0<x<L, t>0
$$
the boundary conditions
$$
u(0, t)=0, \quad u(L, t)=0, t>0
$$
and the initial data
$$
u(x, 0)=f(x), \quad u_{t}(x, 0)=g(x), 0 \leq x \leq L .
$$

---

<!-- Page 12 -->

Left margin note (page 12)

526
Chapter 9
Finite Differer

![](./images/3d691698-445f-4a4d-96f7-0cb184e4b380-12_692_1059_871_668.jpg)

Figure 1 Gridpoints in the $x t$-plane.

Right margin note (page 12)

epsize points
ose to

proxi-

++++

ice Numerical Methods

Discretizing the Wave Equation
As in the previous section, we let $h$ denote our stepsize in $x$ and $k$ our st in $t$. We will approximate the displacement $u$ at a discrete set of grid in the $x t$-plane (see Figure 1). Let
$$
h=\frac{L}{n},
$$
where $n$ denotes the number of equal subintervals into which we cho subdivide the interval $(0, L)$, and let
$$
u_{i j}=u(i h, j k), \quad 0 \leq i \leq n, \quad j \geq 0 .
$$

Thus $u_{i j}$ represents the value of $u$ at the gridpoint $(i h, j k)$.

To discretize (1), we appeal to the centered second difference ap mation ((10), Section 9.1):
$$
u_{x x}(i h, j k) \approx \frac{1}{h^{2}}\left(u_{i+1, j}-2 u_{i j}+u_{i-1, j}\right),
$$
and
(6)
$$
u_{t t}(i h, j k) \approx \frac{1}{k^{2}}\left(u_{i, j+1}-2 u_{i j}+u_{i, j-1}\right) .
$$

Plugging into (1) and simplifying, we get

---

<!-- Page 13 -->

Left margin note (page 13)

DISCRETIZATION OF THE WAVE EQUATION

![](./images/3d691698-445f-4a4d-96f7-0cb184e4b380-13_525_276_553_185.jpg)

Figure 2 Stepping forward in time in the wave equation.

++++

Section 9.2 The Finite Difference Method for the Wave Equation
$$
u_{i, j+1}=2(1-s) u_{i j}+s\left(u_{i+1, j}+u_{i-1, j}\right)-u_{i, j-1},
$$
where
$$
s=c^{2} \frac{k^{2}}{h^{2}}
$$

This is our finite difference approximation to the wave equation. In a with our previous remarks, we see that the values at the $(j+1)$ th time are computed from the values at the $j$ th and the $(j-1)$ th time steps Figure 2).

Stability Criterion
As in the previous section, our numerical scheme is stable only fo ficiently small positive values of $s$. In this case, the finite difference sc (7) is unstable if $s>1$ and stable if $0<s \leq 1$. Thus the method reasonable approximations to the exact solution when $0<s \leq 1$. Exan below illustrates this criterion.

Here again, the critical value ( $s=1$ ) simplifies (7), yielding
$$
u_{i, j+1}=u_{i+1, j}+u_{i-1, j}-u_{i, j-1}
$$

Discretizing the Boundary and Initial Conditions
Let's first deal with the boundary conditions. From (2), we get
$$
u_{0 j}=u(0, j k)=0, \quad j>0
$$
and
$$
u_{n j}=u(n h, j k)=u(L, j k)=0, \quad j>0
$$

Also, the first initial condition yields
$$
u_{i 0}=u(i h, 0)=f(i h), \quad 0 \leq i \leq n
$$

We now use the initial data $f$ and $g$ to generate a second set of i values of $u$. For this purpose, it is best to use the centered first diffe approximation
$$
u_{t}(x, t) \approx \frac{u(x, t+k)-u(x, t-k)}{2 k}
$$

---

<!-- Page 14 -->

Left margin note (page 14)

528
Chapter 9
Finite Differen

![](./images/3d691698-445f-4a4d-96f7-0cb184e4b380-14_398_472_1650_59.jpg)

Figure 3 Initial slape of the string.

Right margin note (page 14)

ble to ce ap-correcalled a way to use her of is also ed (for cases, tes as n later
$L=6$;

orward
inction
string?

++++

ce Numerical Methods

(see Exercise 16, Section 9.1). Setting $t=0$, we find
$$
g(x)=u_{t}(x, 0) \approx \frac{u(x \cdot k)-u(x \cdot-k)}{2 k} .
$$

Evaluating at the points $x=i h$, we get
$$
u_{i 1}-u_{i,-1}=2 k g(i h) .
$$

From (7), with $j=0$, we find
$$
\begin{aligned}
u_{i, 1}+u_{t,-1} & =2(1-s) u_{i, 0}+s\left(u_{i+1,0}+u_{i-1,0}\right) \\
& =2 f(i h)+s(f((i+1) h)-2 f(i h)+f((i-1) h))
\end{aligned}
$$

Adding (13) and (14) and dividing by 2 , we get
$$
u_{i, l}=f(i h)+k g(i h)+\frac{s}{2}(f((i+1) h)-2 f(i h)+f((i-1) h))
$$

This is the second pice of initial data that we need in order to be a start iterating formula (7).

The trick that we used above in introducing the centered differen proximation to $u_{t}(x, 0)$ forced us to work briefly with the values $u_{i,-1}$, sponding to the gridpoints $(i,-1)$ (see (13) and (14)). Such points are ghost points. They helped us incorporate the initial data for $u_{t}$ in that is symmetric with respect to $t=0$. That is, by this device we got centered differences rather than forward or backward differences (neit which treats $t=0$ in a symmetric fashion). The use of ghost points desirable when dealing with boundary conditions in which $u_{x}$ is specifi example. in the heat problem for a bar with insulated ends). In these we would use gridpoints just beyond our normal range of $x$ coordina our ghost points. We shall see examples of this in the exercises and in sections.

EXAMPLE 1 Numerical solution for the wave equation
Approximate the solution to the problem (1)-(3) with the following data: $r=1$; the initial shape of the string is as shown in Figure 1 and given by
$$
f(x)=\left\{\begin{array}{ll}
2-2|x-2| & \text { if } 1<x<3, \\
0 & \text { otherwise; }
\end{array} \quad g(x)=0 .\right.
$$

Use (7) with $h=1$ and $k=1$ (hence $s=1$ and $n=6$ ). Carry your solution f in steps of 1 to $t=13$. What do you notice about the solution as a f of $t$ ? What happens to the disturbance when it reaches the ends of the

---

<!-- Page 15 -->

Right margin note (page 15)

529

on of
(9),
value band rule cids, nited ta by
wave ntext only $y$, no 13 is blein ytical $(x, t)$

++++

Section 9.2 The Finite Difference Method for the Wave Equation

Also, compare your solution to the analytical solution obtained via separati variables.

Solution Since $s=1$, the discretized problem that we need to solve is, from
$$
u_{i, j+1}=u_{i+1, j}+u_{i-1, j}-u_{i, j} \quad 1 .
$$

Using (12) and (15), we get our first two rows of data in Table 1.

\begin{table}
| $i$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $u_{i, 0}$ | 0 | 0 | 2 | 0 | 0 | 0 | 0 |
| $u_{i, 1}$ | 0 | 1 | 0 | 1 | 0 | 0 | 0 |
\captionsetup{labelformat=empty}
\caption{Table 1}
\end{table}

Now (16) tells us that to propagate our wave to the next time step for a given of $x$ we simply sum the values at the two adjacent positions at that time stee subtract the value at the given position at the previous time step. With this we are prepared to iterate our scheme indefinitely (recall that we have fixed so $u$ is always 0 at $i=0$ and 6). The results are shown in Table 2 and represe graphically in Figure 4. These graphs were constructed from the numerical da connecting consecutive data points by line segments.

\begin{table}
| $t . x$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 |
| 1 | 0 | 1 | 0 | 1 | 0 | 0 | 0 |
| 2 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| 3 | 0 | -1 | 0 | 0 | 0 | 1 | 0 |
| 4 | 0 | 0 | -1 | 0 | 0 | 0 | 0 |
| 5 | 0 | 0 | 0 | -1 | 0 | -1 | 0 |
| 6 | 0 | 0 | 0 | 0 | -2 | 0 | 0 |
| 7 | 0 | 0 | 0 | -1 | 0 | -1 | 0 |
| 8 | 0 | 0 | -1 | 0 | 0 | 0 | 0 |
| 9 | 0 | -1 | 0 | 0 | 0 | 1 | 0 |
| 10 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| 11 | 0 | 1 | 0 | 1 | 0 | 0 | 0 |
| 12 | 0 | 0 | 2 | 0 | 0 | 0 | 0 |
| 13 | 0 | 1 | 0 | 1 | 0 | 0 | 0 |
| 14 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
\captionsetup{labelformat=empty}
\caption{Table 2 Finite difference method with $s=1$.}
\end{table}

It appears from our numcrical values and the corresponding graphs that the motion repeats itself beginning from $t=12$. To prove this rigorously in the co of our discretized wave problem, we note that our iteration process requires two rows of discrete data, and it procceds from these in exactly the same wa matter what time we consider. Since Table 2 shows that the data at $t=12$ and identical to that at $t=0$ and 1 , this shows that the solution to the discrete pro repeats periodically with period 12 . Note that 12 is also the period of our anal solution (see Exercise 6, Section 3.4, where it is shown that the displacement is periodic in $t$ of period $2 L / c$ ).

---

<!-- Page 16 -->

Left margin note (page 16)

530
Chapter 9
Fi

![](./images/3d691698-445f-4a4d-96f7-0cb184e4b380-16_193_306_292_98.jpg)

Figure 4 Snapshots consecutive data poi

![](./images/3d691698-445f-4a4d-96f7-0cb184e4b380-16_188_312_296_417.jpg)
![](./images/3d691698-445f-4a4d-96f7-0cb184e4b380-16_188_309_297_742.jpg)
![](./images/3d691698-445f-4a4d-96f7-0cb184e4b380-16_185_309_297_1065.jpg)
![](./images/3d691698-445f-4a4d-96f7-0cb184e4b380-16_179_300_303_1391.jpg)
![](./images/3d691698-445f-4a4d-96f7-0cb184e4b380-16_184_304_629_100.jpg)
![](./images/3d691698-445f-4a4d-96f7-0cb184e4b380-16_181_312_631_417.jpg)
![](./images/3d691698-445f-4a4d-96f7-0cb184e4b380-16_184_308_629_742.jpg)
![](./images/3d691698-445f-4a4d-96f7-0cb184e4b380-16_184_309_629_1065.jpg)
![](./images/3d691698-445f-4a4d-96f7-0cb184e4b380-16_179_300_631_1391.jpg)
![](./images/3d691698-445f-4a4d-96f7-0cb184e4b380-16_204_311_941_95.jpg)
![](./images/3d691698-445f-4a4d-96f7-0cb184e4b380-16_195_327_946_412.jpg)
![](./images/3d691698-445f-4a4d-96f7-0cb184e4b380-16_194_317_946_747.jpg)
![](./images/3d691698-445f-4a4d-96f7-0cb184e4b380-16_194_304_946_1070.jpg)
![](./images/3d691698-445f-4a4d-96f7-0cb184e4b380-16_190_303_948_1392.jpg)

Right margin note (page 16)

g

values e good, ations. ecewise ecewise $h$ and tinuous course, in our oint of

++++

nite Difference Numerical Methods
of the string constructed from the finite difference solution data in Table 2 by connectin nts by line segments. Notice the periodicity of the motion $T=2 L / c=12$.

Using the results of Section 3.3, we find the analytical solution
$$
u(x, t)=\sum_{n=1}^{\infty} b_{n} \sin \frac{n \pi x}{6} \cos \frac{n \pi t}{6},
$$
where
$$
b_{n}=\frac{1}{3} \int_{0}^{6} f(x) \sin \frac{n \pi x}{6} d x=\frac{24}{n^{2} \pi^{2}}\left(2 \sin \frac{n \pi}{3}-\sin \frac{n \pi}{6}-\sin \frac{n \pi}{2}\right) .
$$

We have plotted the graph of the partial sum of the first 30 terms at various of $t$ in Figure 5. We note that, while the partial sum approximation is quit in this case the numerical solution is actually the better of the two approxim In fact, the numerical solution turns out to be exact (if we agree to the pi linear interpolation shown in Figure 1), partly because we began with a pi linear function. Other factors contributing to this are our choice of stepsizes $k$ and our use of the centered difference approximation in converting our con initial data into the initial data for our discretized problem. We could, of get better accuracy from our series solution simply by going to more terms partial sums. Finally, we could also develop an exact solution from the

---

<!-- Page 17 -->

Left margin note (page 17)

![](./images/3d691698-445f-4a4d-96f7-0cb184e4b380-17_202_309_384_65.jpg)

Figure 5 Snapshots the infinite series solut

![](./images/3d691698-445f-4a4d-96f7-0cb184e4b380-17_195_307_387_386.jpg)
![](./images/3d691698-445f-4a4d-96f7-0cb184e4b380-17_197_310_387_708.jpg)
![](./images/3d691698-445f-4a4d-96f7-0cb184e4b380-17_193_306_389_1033.jpg)
![](./images/3d691698-445f-4a4d-96f7-0cb184e4b380-17_187_305_394_1357.jpg)
![](./images/3d691698-445f-4a4d-96f7-0cb184e4b380-17_193_309_726_67.jpg)
![](./images/3d691698-445f-4a4d-96f7-0cb184e4b380-17_185_311_729_384.jpg)
![](./images/3d691698-445f-4a4d-96f7-0cb184e4b380-17_183_307_729_707.jpg)
![](./images/3d691698-445f-4a4d-96f7-0cb184e4b380-17_183_306_729_1033.jpg)
![](./images/3d691698-445f-4a4d-96f7-0cb184e4b380-17_183_306_729_1357.jpg)
![](./images/3d691698-445f-4a4d-96f7-0cb184e4b380-17_200_309_1047_67.jpg)
![](./images/3d691698-445f-4a4d-96f7-0cb184e4b380-17_200_317_1047_380.jpg)
![](./images/3d691698-445f-4a4d-96f7-0cb184e4b380-17_198_315_1047_705.jpg)
![](./images/3d691698-445f-4a4d-96f7-0cb184e4b380-17_198_315_1047_1029.jpg)
![](./images/3d691698-445f-4a4d-96f7-0cb184e4b380-17_194_308_1050_1355.jpg)

Right margin note (page 17)

531
on of
iffer-
ice a
$t(x$
$x, 0)$
side
ation
ng a
$u_{i, 1}$.
rox-
tion,

++++

Section 9.2 The Finite Difference Method for the Wave Equation

view of the d'Alembert solution to the wave equation, using the odd extensic our initial data (see Section 3.4).
of the string constructed from the analytical solution by using 30 -term partial sum of tion.

We close the section with a brief analysis of the error in our finite d ence scheme for the wave equation. Looking back at (15), you may not resemblance to a Taylor expansion for $u(x, t)$ along the second variable is fixed). That is,
$$
\begin{aligned}
u(x, k) & \approx u(x, 0)+u_{t}(x, 0) k+\frac{1}{2} u_{t t}(x, 0) k^{2} \\
& =f(x)+g(x) k+\frac{1}{2} c^{2} f^{\prime \prime}(x) k^{2}
\end{aligned}
$$
where in the last term we have used the wave equation to convert $u_{t t}($ into $c^{2} u_{x . x}(x, 0)=c^{2} f^{\prime \prime}(x)$. This last expression reduces to the right of (15) if we set $x=i h$, use the centered second difference approxima for $f^{\prime \prime}(i h)$, and recall that $s=c^{2} k^{2} / h^{2}$. Thus (15) amounts to usi discretized form of the second order Taylor polynomial to determine This is the advantage of equating $g(i h)$ to the centered difference app imation of $u_{t}(i h, 0)$. If we had used the forward difference approxima

---

<!-- Page 18 -->

Left margin note (page 18)

532
Chapter 9 Finite

Right margin note (page 18)

hat is. pproxwave e (15), roblem ee time
d. Use 13. Is ag. In te one, it ends atward. corre$x)=0$. 1, Sec-
ulated boundoduced rences, ate the points
bound-

++++

Difference Numerical Methods

we would have gotten the first order Taylor polynomial in (15). T $u_{i, 1} \approx f(i h)+k g(i h)$. It turns out that by using the more precise a imation given by (15), the errors made in our approximations to the equation, $u$, and $u_{t}$ are all of order at least $h^{2}$ or $k^{2}$. Hence if we us our errors will all be of second order or higher.

Exercises 9.2
In Exercises 1-4, data to the wave problem (1) -(3) is given. Discretize the 7 using $s=1$ and $n=5$, and compute the solution by hand for the first thr steps.
1. $L=c=1, g(x)=0, f(x)=\left\{\begin{array}{ll}2 x & \text { if } 0<x<1 / 2, \\ 2(1-x) & \text { if } 1 / 2<x<1 .\end{array}\right.$
2. $L=c=1, g(x)=0, f(x)=\left\{\begin{array}{ll}6 x & \text { if } 0<x<1 / 3, \\ 3(1-x) & \text { if } 1 / 3<x<1 .\end{array}\right.$
3. All data as in Exercise 1, except $g(x)=1$.
4. $L=c=1, f(x)=0, g(x)=x(1-x)$.
5. Consider the problem given in Example 1 but with $f$ and $g$ interchange $s=1$ and $n=6$ and compute the finite difference solution $u_{i}$, through $t=$ your solution periodic? Of what period?
6. Project Problem: Finite difference scheme for the infinite stri many ways the infinite stretched string is easier to deal with than the fini since in this case there are no boundary conditions to be imposed. Witho there are no reflections to complicate matters, and the data just propagate on
(a) Review the finite difference method for the finite string and formulate a sponding theory for the infinite string.
(b) Test your result in (a) with the following data: $c=1, f(x)=e^{-x^{2}}, g($ You should compare your solution with the d'Alembert solution (Exercise 2 tion 7.3).
(c) Repeat (b) with the data $c=1, f(x)=e^{-x^{2}} \cos 2 x, g(x)=0$.
7. Project Problem: Ghost points for the heat equation with ins ends. As we mentioned in the text, ghost points can also be used to handle ary conditions such as $u_{x}=0$ in a way that helps minimize the error intr by our difference approximation. That is, they allow us to use centered diffe rather than forward or backward differences, and thus allow us to incorpor boundary data in a more symmetric fashion. To illustrate the use of ghost in this setting, let's consider the problem of an insulated bar,
$$
\begin{aligned}
u_{t} & =c^{2} u_{x x}, \quad 0<x<L . t>0, \\
u_{x}(0, t)=0 & =u_{x}(L, t), \quad t>0, \\
u(x, 0) & =f(x), \quad 0 \ldots x<L .
\end{aligned}
$$
(a) Using centered differences (Exercise 16, Section 9.1) to approximate the ary conditions $u_{x}=0$, develop the iteration schemes
$$
u_{0, j+1}=(1-2 s) u_{0, j}+2 s u_{1, l},
$$

---

<!-- Page 19 -->

Left margin note (page 19)

The Finite

Right margin note (page 19)

533

ends
step find $1, j+1$ alues We hole
$i, j+1$ ified all $i +1$
ation itial pute
ol to from
blem r all ug"?

in
:hlet
nate sing lems ized 10), ions olem with n by

++++

Section 9.3 The Finite Difference Method for Laplace's Equation

and
$$
u_{n, j+1}=(1-2 s) u_{n_{j}}+2 s u_{n-1, j} .
$$

These formulas tell us how the temperature propagates forward in time at the of our bar. Note that they are stated without explicit mention of ghost points

Alternatively, starting with the data $u_{i j}$, for $-1 \leq i \leq n+1$ at a fixed time $j$, we could use the difference scheme for the heat equation ((7), Section 9.1) to the values $u_{i, j+1}$ at the next time step for $0 \leq i \leq n$, and then use $u_{-1, j+1}=u$. and $u_{n+1, j+1}=u_{n-1, j+1}$. With these last two equations we are supplying the ve at the two ghost points using the centered difference approximation to $\mathrm{u}_{x}=0$. then have the values $u_{i, j+1}$ at time step $j+1$ for $-1 \leq i \leq n+1$, and the $w$ process can be repeated.

Note that with the first method given we need only compute the values $u$ for $0 \leq i \leq n$ at each stage. but we must compute the end values using mod formulas. In the second method we get to use the same iteration scheme for from 0 to $n$, but we must also carry forward values of $u$ at $i=-1$ and $i=n$ via reflection from the values at 1 and $n-1$, respectively.
(b) Use the finite difference scheme developed in (a) to approximate the solu to the heat problem for a bar of length $L=4$ with insulated ends for the ir data $f(x)=25 x$. Assume $c=1$, take stepsizes $h=1$ and $k=0.5$, and com the numerical solution through 8 time steps.
(c) Identify the steady-state solution to the problem in part (b). (You may ned compute additional time steps.) Does your answer agree with what we know the analytical case (see Section 3.6)?
8. Using the method of the previous problem, rework the wave equation prol from Example 1, but with the boundary conditions $u_{x}(0, t)=0=u_{s}(L, t)$ fo $t>0$. What happens this time when a disturbance reaches an end of our "stri Is it reflected? In what sense?

Difference Method for Laplace's Equation
In this and the following section, we will consider Laplace's equatio two variables with given boundary data. That is, we consider the Diric problem
$$
\Delta u \equiv u_{x x}+u_{y y}=0 \quad \text { in a domain } R
$$
where $u$ is specificd on the boundary of $R$. We seek to find an approxir solution to this problem by discretizing it in the $x$ and $y$ variables and pas to a finite difference scheme, just as we did for the heat and wave prob. in previous sections. The partial differential equation (1) is easily discret using the centered second difference approximations for $u_{x x}$ and $u_{y y}$ ( Section 9.1). Our biggest problem will be to handle the boundary condit in the discretized setting. For the time being, we shall alleviate this prol by concentrating on rectangular domains. In the exercises we shall deal other domains.

We consider the Dirichlet problem over a rectangular domain $R$ give $0<x<a, 0<y<b$, with boundary data as shown in Figure 1.

---

<!-- Page 20 -->

Left margin note (page 20)

534
Chapter 9 Finite Differer

![](./images/3d691698-445f-4a4d-96f7-0cb184e4b380-20_435_466_719_65.jpg)

Figure 1 A Dirichlet problem in a rectangle $R$.

![](./images/3d691698-445f-4a4d-96f7-0cb184e4b380-20_403_1048_202_677.jpg)

Figure 2 A grid over $R$.

Right margin note (page 20)

2. We ximate t
le now on 9.1)
mation
four $x$ is to goes weight , since

++++

Numerical Methods

Discretizing Laplace's Equation
We will put a grid over the rectangular region $R$, as shown in Figure let $h$ denote our gridsize in $x$ and $k$ our gridsize in $y$. We will appro the displacement $u$ at a discrete set of gridpoints in the $x y$-plane. Le
$$
h=a / m, \quad k=b / n,
$$
and
$$
u_{i j}=u(i h, j k), \quad 0 \leq i \leq m, 0 \leq j \leq n .
$$

Thus $u_{i j}$ represents the value of $u$ at the gridpoint $(i h, j k)$. W appeal to the centered second difference approximation ((10), Sectic and write:
$$
u_{x x}(i h, j k) \approx \frac{1}{h^{2}}\left(u_{i+1, j}-2 u_{i j}+u_{i-1, j}\right),
$$
and
$$
u_{y y}(i h, j k) \approx \frac{1}{k^{2}}\left(u_{i, j+1}-2 u_{i j}+u_{i, j-1}\right) .
$$

Plugging into (1) and simplifying, we get our finite difference approxi to Laplace's equation:
$$
u_{i, j}=\frac{1}{2\left(h^{2}+k^{2}\right)}\left(k^{2}\left(u_{i+1, j}+u_{i-1, j}\right)+h^{2}\left(u_{i, j+1}+u_{i, j-1}\right)\right),
$$
which says that $u_{i j}$ is a weighted average of the values of $u$ at th neighboring gridpoints (see Figure 3). When $h<k$, the spacing less than that in $y$, and (5) tells us that the weight $k^{2} /\left(h^{2}+k^{2}\right)$ the with the gridpoints $((i+1) h, j k)$ and $((i-1) h, j k)$ is larger than the $h^{2} /\left(h^{2}+k^{2}\right)$ that goes with the other two points. This is expected these are the nearer of the four points.

---

<!-- Page 21 -->

Left margin note (page 21)

DISCRETIZA OF LAPL. EQUA

![](./images/3d691698-445f-4a4d-96f7-0cb184e4b380-21_210_80_670_185.jpg)

Figure 3 Averag property of a soluti Dirichlet problem.

![](./images/3d691698-445f-4a4d-96f7-0cb184e4b380-21_276_425_897_37.jpg)

Right margin note (page 21)

535

and
f the igure
gridhave ns in solvem of that rated
th all 1. As ently $n-1)$ lumn
oulr ocess
ndary re 1).
npare found
ample 1/4),

++++

Section 9.3 The Finite Difference Method for Laplace's Equation

In the important special case when $h=k$, the weights are all $1 / 4$ therefore (5) reduces to

TION
ACE'S
TION
$$
u_{i+1, j}^{\bullet}
$$
value on of a
$$
u_{i, j}=\frac{1}{4}\left(u_{i+1, j}+u_{i-1, j}+u_{i, j+1}+u_{i, j-1}\right),
$$
which has a very nice interpretation. In this case, $u_{i j}$ is the average 0 values of $u$ at the four neighboring points on the grid to $(i h, j k)$ (sce F $3)$. Henceforth we shall proceed under this simplifying assumption.

Equation (6) gives an expression for the value of $u$ at each interior point of our region $R$ in terms of its four nearest neighbors. Since we $(m-1)(n-1)$ interior gridpoints, (6) gives us $(m-1)(n-1)$ equatio the unknowns $u_{i j}, 1 \leq i \leq m-1,1 \leq j \leq n-1$. The problem of ing our discretized Dirichlet problem is now reduced to solving a syste $(m-1)(n-1)$ equations in the $(m-1)(n-1)$ unknowns $u_{i j}$. It turns out this system of equations always has a unique solution, as will be illust by examples below.

In listing the system of $(m-1)(n-1)$ equations we will run throug the indices $(i, j)$ row by row, starting from the bottom left of the gric you may recall from linear algebra, the system of equations is conveni represented in the form $A u=b$, where $A$ is the $(m-1)(n-1)$ by $(m-1)$ ( matrix of coefficients, $b$ is a column $(m-1)(n-1)$-vector, and $u$ is a co $(m-1)(n-1)$-vector that contains the $u_{i j}$ in the order chosen above.

Assuming that the square matrix $A$ has an inverse, the solution t problem will then be given by $u=A^{-1} b$. We illustrate the entire pr with a simple example.

EXAMPLE 1 A Dirichlet problem on a square
Approximate the solution to the problem (1) on a square of side 1 with bou data given as 100 along the upper side and 0 along the other three sides (Figu
(a) Use the finite difference scheme developed above with $m=n=3$.
(b) Use the finite difference scheme developed above with $m=n=4$, and cor the approximation you obtain for $u$ at the square's center with the value 25 analytically (see the end of Section 3.8).
(c) Compare the values you found in (b) to those of the analytical solution (Exa 2, Section 3.8). That is, use the analytical solution to find the 9 values $u(1 / 4$, $u(1 / 2,1 / 4), u(3 / 4,1 / 4), \ldots, u(3 / 4,3 / 4)$.

---

<!-- Page 22 -->

Left margin note (page 22)

536 Chapter 9 Finite Differer

![](./images/3d691698-445f-4a4d-96f7-0cb184e4b380-22_500_482_132_51.jpg)

Figure 4 Schematic representation of the discretized problem.

Right margin note (page 22)

1. By nations
n (that ations.
(2.2),
is is a trix is st says 1e sum such a

++++

ace Numerical Methods

Solution (a) Our discretized problem is represented schematically in Figure the averaging property (6) and using Figure 4. we can read off the four eqi (in our conventional order)
$$
\begin{array}{l}
u_{11}=\frac{1}{4}\left(u_{21}+u_{12}\right), \\
u_{21}=\frac{1}{4}\left(u_{11}+u_{22}\right), \\
u_{12}=\frac{1}{4}\left(u_{11}+u_{22}+100\right) . \\
u_{22}=\frac{1}{4}\left(u_{21}+u_{12}+100\right) .
\end{array}
$$

Note that here we do not need to worry about the corner points of the domai is, the values $u_{00}, u_{30}, u_{03}$, and $u_{33}$ ), since these never enter into our equ Again, choosing to run through the indices in the order $(1,1),(2,1),(1,2)$, we put our system in the form

| $4 u_{11}$ | $-u_{21}$ | $-u_{12}$ |  | $=0$ |
| :--- | :--- | :--- | :--- | :--- |
| $-u_{11}$ | $+4 u_{21}$ |  | $-u_{22}$ | $=0$ |
| $-u_{11}$ |  | $+4 u_{12}$ | $-u_{22}$ | $=100$ |
|  | $-u_{21}$ | $-u_{12}$ | $+4 u_{22}$ | $=100$. |

This system can be represented using matrices as $A u=b$, where
$$
A=\left[\begin{array}{cccc}
4 & -1 & -1 & 0 \\
-1 & 4 & 0 & -1 \\
-1 & 0 & 4 & -1 \\
0 & -1 & -1 & 4
\end{array}\right], \quad u=\left[\begin{array}{l}
u_{11} \\
u_{21} \\
u_{12} \\
u_{22}
\end{array}\right], \quad \text { and } \quad b=\left[\begin{array}{c}
0 \\
0 \\
100 \\
100
\end{array}\right] .
$$

We note that $A$ is a symmetric matrix with 1 s down its diagonal. consequence of the way we ordered our equations and variables.) This ma a special case of what is called a diagonally dominant matrix, which ju that in each row the diagonal element is larger (in absolute value) than th of the absolute values of all other entries from that row. It is known that matrix always has an inverse. In our case, we have
$$
A^{-1}=\frac{1}{24}\left[\begin{array}{llll}
7 & 2 & 2 & 1 \\
2 & 7 & 1 & 2 \\
2 & 1 & 7 & 2 \\
1 & 2 & 2 & 7
\end{array}\right]
$$

---

<!-- Page 23 -->

Left margin note (page 23)

![](./images/3d691698-445f-4a4d-96f7-0cb184e4b380-23_495_468_213_35.jpg)

Figure 5 Schematic sentation of the soluti
$$
u=A^{-1} b
$$

Right margin note (page 23)

537
erior
e the
ional
inted
n the
$]$.
blem
have
e the

++++

Soction 9.3 The Finite Difference Method for Laplace's Equation

Thus we have the solution
repreon.
$$
u=\left[\begin{array}{l}
u_{11} \\
u_{21} \\
u_{12} \\
u_{22}
\end{array}\right]=A^{-1} b=\frac{1}{24}\left[\begin{array}{llll}
7 & 2 & 2 & 1 \\
2 & 7 & 1 & 2 \\
2 & 1 & 7 & 2 \\
1 & 2 & 2 & 7
\end{array}\right]\left[\begin{array}{c}
0 \\
0 \\
100 \\
100
\end{array}\right]=\left[\begin{array}{c}
12.5 \\
12.5 \\
37.5 \\
37.5
\end{array}\right] .
$$

This solution is represented schematically in Figure 5. Note that every int value is the average of the values at its four nearest neighbors.

It is also worth noting that once we have computed $A^{-1}$, we can comput numerical solution for new choices of boundary data with very little addit effort. We need only compute $A^{-1} b$ for the new choices of $b$.
(b) Proceeding as in (a), we arrive at the 9 -by- 9 system of equations represi by $A u=b$, where
$$
A=\left[\begin{array}{ccccccccc}
4 & -1 & 0 & -1 & 0 & 0 & 0 & 0 & 0 \\
-1 & 4 & -1 & 0 & -1 & 0 & 0 & 0 & 0 \\
0 & -1 & 4 & 0 & 0 & -1 & 0 & 0 & 0 \\
-1 & 0 & 0 & 4 & -1 & 0 & -1 & 0 & 0 \\
0 & -1 & 0 & -1 & 4 & -1 & 0 & -1 & 0 \\
0 & 0 & -1 & 0 & -1 & 4 & 0 & 0 & -1 \\
0 & 0 & 0 & -1 & 0 & 0 & 4 & -1 & 0 \\
0 & 0 & 0 & 0 & -1 & 0 & -1 & 4 & -1 \\
0 & 0 & 0 & 0 & 0 & -1 & 0 & -1 & 4
\end{array}\right], u=\left[\begin{array}{c}
u_{11} \\
u_{21} \\
u_{31} \\
u_{12} \\
u_{22} \\
u_{32} \\
u_{13} \\
u_{23} \\
u_{33}
\end{array}\right], b=\left[\begin{array}{c}
0 \\
0 \\
0 \\
0 \\
0 \\
0 \\
100 \\
100 \\
100
\end{array}\right.
$$

With the help of a computer, we invert the matrix $A$ and obtain our solution i form
$$
=\frac{1}{224}\left[\begin{array}{ccccccccc}
67 & 22 & 7 & 22 & 14 & 6 & 7 & 6 & 3 \\
22 & 74 & 22 & 14 & 28 & 14 & 6 & 10 & 6 \\
7 & 22 & 67 & 6 & 14 & 22 & 3 & 6 & 7 \\
22 & 14 & 6 & 74 & 28 & 10 & 22 & 14 & 6 \\
14 & 28 & 14 & 28 & 84 & 28 & 14 & 28 & 14 \\
6 & 14 & 22 & 10 & 28 & 74 & 6 & 14 & 22 \\
7 & 6 & 3 & 22 & 14 & 6 & 67 & 22 & 7 \\
6 & 10 & 6 & 14 & 28 & 14 & 22 & 74 & 22 \\
3 & 6 & 7 & 6 & 14 & 22 & 7 & 22 & 67
\end{array}\right]\left[\begin{array}{c}
0 \\
0 \\
0 \\
0 \\
0 \\
0 \\
100 \\
100 \\
100
\end{array}\right]=\left[\begin{array}{c}
50 / 7 \\
275 / 28 \\
50 / 7 \\
75 / 4 \\
25 \\
75 / 4 \\
300 / 7 \\
1475 / 28 \\
300 / 7
\end{array}\right]=\left[\begin{array}{c}
7.14 \\
9.82 \\
7.14 \\
18.75 \\
25 \\
18.75 \\
12.86 \\
52.68 \\
42.86
\end{array}\right.
$$

The solution is represented in Table 1. Since in our discretization of the pro $u_{22}$ represents the value at the square's center (recall that $h=k=1 / 4$ ), we found the approximation 25 for the value $u(1 / 2,1 / 2)$, which also happens to b exact value.

---

<!-- Page 24 -->

Left margin note (page 24)

538
Chapter 9
Finite Differer

Right margin note (page 24)

results,
erence $A$ that indary change richlet e $A^{-1}$. lacian,

1e with s found
uation,

++++

ace Numerical Methods

| \multicolumn{3}{\|c\|}{Temperature at the gridpoints} |  |  |
| :--- | :--- | :--- |
| 42.86 | 52.68 | 42.86 |
| 43.20 | 54.05 | 43.20 |
| 18.75 | 25 | 18.75 |
| $u(1 / 4,1 / 2)$ | $u(1 / 2,1 / 2)$ | $u(3 / 4,1 / 2)$ |
| 18.20 | 25 | 18.20 |
| 7.14 | 9.82 | 7.14 |
| $u(1 / 4,1 / 4)$ | $u(1 / 2,1 / 4)$ | $u(3 / 4,1 / 4)$ |
| 6.80 | 9.54 | 6.80 |

Table 1 In each cell, the top values were generated with the finite differ method in (b). The bottom values were computed using the analy solution.
(c) We use a computer to evaluate the analytical solution
$$
u(x, y)=\frac{400}{\pi} \sum_{k=0}^{\infty} \frac{\sin (2 k+1) \pi x}{2 k+1} \frac{\sinh (2 k+1) \pi y}{\sinh (2 k+1) \pi}
$$
at the 9 given interior gridpoints (we use a partial sum up to $k=30$ ). The along with our numerical approximations from (b), are presented in Table 1

There is no doubt that most of the work in applying the finite dif method to a Dirichlet problem goes toward inverting the matrix arises in the problem. You should go over Example 1 with different bor conditions in mind and check that only the vector $b$ changes when we the boundary conditions. This means that we can solve a variety of D problems by the finite difference method, without having to recomput Indeed, the same remarks apply to some equations involving the Lap as we now illustrate.

EXAMPLE 2 A Poisson problem on a square
Approximate the solution to the Poisson problem
$$
\nabla^{2} u=1
$$
on a square of side 1 with 0 boundary data. Use the finite difference schen $m=n=4$, and compare the approximation you obtain for $u$ with the value analytically from Example 3, Section 3.9.

Solution We follow the notation of Example 1. To discretize Poisson's eq we use (3) and (4), with $h=k=\frac{1}{4}$, and get
$$
\frac{1}{h^{2}}\left(u_{i+1, j}+u_{i-1, j}+u_{i, j+1}+u_{i, j-1}-4 u_{i j}\right)=1 .
$$

Solving for $u_{i j}$, we get
$$
u_{i j}=\frac{1}{1}\left(u_{i+1, j}+u_{i-1, j}+u_{i, j+1}+u_{i, j-1}-\frac{1}{16}\right),
$$

---

<!-- Page 25 -->

Right margin note (page 25)

539

nine e we ut in s the n $\left.\begin{array}{l}3 \\ 5 \\ 3 \\ 5 \\ 0 \\ 5 \\ 3 \\ 5 \\ 3\end{array}\right]$.
of the series
c
with uped, vious finite must rvals ith a es. It have le 1).

++++

Section 9.3 The Finite Difference Method for Laplacr's Equation

which determines our finite difference scheme. The boundary values are
$$
u_{r, 0}=0 \quad \text { and } \quad u_{0, j}=0, \quad i, j>0 .
$$

Reading off the values of $u_{i j}$ from our finite difference scheme, we arrive at equations in the nine unknowns $u_{1,1}, u_{2,1} . u_{3,1}, u_{1,2}, \ldots, u_{3,3}$, where het followed the same order as in Example 1. The system of equations can be p the form $A u=b$. where $A$ is the same matrix as in Example 1(b), and $b$ i vector with entries identically cqual to $-h^{2}=-\frac{1}{16}$. Thus we have the solutio
$$
\frac{1}{224}\left[\begin{array}{ccccccccc}
67 & 22 & 7 & 22 & 11 & 6 & 7 & 6 & 3 \\
22 & 74 & 22 & 11 & 28 & 14 & 6 & 10 & 6 \\
7 & 22 & 67 & 6 & 14 & 22 & 3 & 6 & 7 \\
22 & 11 & 6 & 74 & 28 & 10 & 22 & 14 & 6 \\
14 & 28 & 14 & 28 & 81 & 28 & 14 & 28 & 14 \\
6 & 14 & 22 & 10 & 28 & 74 & 6 & 14 & 22 \\
7 & 6 & 3 & 22 & 14 & 6 & 67 & 22 & 7 \\
6 & 10 & 6 & 14 & 28 & 14 & 22 & 74 & 22 \\
3 & 6 & 7 & 6 & 14 & 22 & 7 & 22 & 67
\end{array}\right]\left[\begin{array}{l}
-1 / 16 \\
-1 / 16 \\
-1 / 16 \\
-1 / 16 \\
-1 / 16 \\
-1 / 16 \\
-1 / 16 \\
-1 / 16 \\
-1 / 16
\end{array}\right]=\left[\begin{array}{l}
-11 / 256 \\
-7 / 128 \\
-11 / 256 \\
-7 / 128 \\
-9 / 128 \\
-7 / 128 \\
-11 / 256 \\
-7 / 128 \\
-11 / 256
\end{array}\right]=\left[\begin{array}{l}
-0.04 \\
-0.05 \\
-0.04 \\
-0.05 \\
-0.07 \\
-0.05 \\
-0.04 \\
-0.05 \\
-0.04
\end{array}\right.
$$

In Table 2. we compare the results of the finite difference method to those analytical solution. For the analytical solution, we took 30 terms in the solution in Example 3, Section 3.9.

\begin{table}
| \multicolumn{3}{\|c\|}{Solution of Poisson's equation} |  |  |
| :--- | :--- | :--- |
| -0.043 | -0.055 | -0.043 |
| $u(1 / 4,3 / 4)$ | $u(1 / 2.3 / 4)$ | $u(3 / 4,3 / 4)$ |
| -0.045 | -0.057 | -0.045 |
| -0.055 | -0.070 | -0.055 |
| $u(1 / 4,1 / 2)$ | $u(1 / 2,1 / 2)$ | $u(3 / 4,1 / 2)$ |
| -0.57 | -0.073 | -0.057 |
| -0.043 | -0.055 | -0.043 |
| $u(1 / 4,1 / 4)$ | $u(1 / 2,1 / 4)$ | $u(3 / 4,1 / 4)$ |
| -0.045 | -0.057 | -0.045 |
\captionsetup{labelformat=empty}
\caption{Table 2 In each cell, the top values were generated with the finite differenc method. The bottom values were computed using the analytical solution.}
\end{table}

As you will see in the exercises, the method of this section applies equal ease to Dirichlet problems over less regular regions, such as L-sha triangular, and cross-shaped regions. Finally, let us mention an ob drawback to the method of this section. If you seek a solution by the difference method that is accurate to several decimal places, then you take a large number of gridpoints. Say, if you divide the $x$ - and $y$-into into 100 parts (not at all unreasonable), then you will be dealing w system of 10,000 equations, with a matrix $A$ having $100,000,000$ entric is a fact that, in Dirichlet problems, even though the matrix $A$ may many zero entries, its inverse, $A^{-1}$, has all nonzero entries (see Examp.

---

<!-- Page 26 -->

Left margin note (page 26)

540 Chapter 9 Finite D

Right margin note (page 26)

ly run a that nverse. n new olving
square
$$
n=3
$$
llowing
i.]
olution.
ct solu-
of side ompute.
$u+x$.
olve the he grid.

0

++++

ifference Numerical Methods

Even if you use a computer to invert the matrix $A$, you can quick into storage problems. There are methods in numerical linear algebr exploit the properties of the matrix $A$ to simplify computing its i Instead of taking this approach, we will present in the next sectio iteration methods that yield satisfactory results with problems in large numbers of gridpoints.

Exercises 9.3
In Exercises 1-4, approximate the solution to the Dirichlet problem (1) on a of side 1 , with the given boundary data. Discretize the problem, using $m=$ and compute the numerical solution by hand. [Hint: Read the remarks fo Example 1.]
1. $f_{1}(x)=0, f_{2}(x)=0, g_{1}(y)=100, g_{2}=0$.
2. $f_{1}(x)=100 x, f_{2}(x)=100, g_{1}=g_{2}=0$.
3. $f_{1}(x)=e^{x}, f_{2}(x)=1, g_{1}=g_{2}=0$.
4. $f_{2}(x)=\sin \pi x, f_{1}=g_{1}=g_{2}=0$.
[Compare your answer to the exact solution, which is $u(x, y)=\sin \pi x \frac{\sinh \pi y}{\sinh \pi}$
5. Repeat Exercise 4 with $m=n=5$. Compare your results with the exact so
6. Repeat Example 1 with $m=n=5$. Compare your results with the exa tion.

In Exercises 7-10, approximate the solution of the given equation on a square 1 with zero boundary data. Discretize the problem, using $m=n=3$ and 0 the numerical solution by hand. [Hint: Proceed as in Example 2.]
7. $\nabla^{2} u=x+y$.
8. $\nabla^{2} u=x y$.
9. $\nabla^{2} u=u+3$.
10. $\nabla^{2} u=$

In Exercises 11-14. a Dirichlet problem is described over a given region. S discretized problem by computing the values of $u$ at the interior points of $t$. You may want to use a computer to solve the insuing system of equations.
11. L shaped:
12. Cross shaped:

---

<!-- Page 27 -->

Left margin note (page 27)

9.4 Iteration M

Right margin note (page 27)

541
0
10
00
00
00
10
00
ated
the
(see
The
$u_{i j}$.
ints.
$u_{i j}$.
gree
bers
But
that
the
our
ount
ould
ge of
, we

++++

Section 9.4 Iteration Methods for Laplace's Equation
13. Isosceles right triangle:
14. A rectangular frame:
ethods for Laplace's Equation
We continue our study of Laplace's equation
$$
\nabla^{2} u=0
$$
over a rectangle $0<x<a, 0<y<b$, with boundary data as illustr in Figure 1, Section 9.3. As in the previous section, we put a grid over rectangle, letting $h$ denote our gridsize in $x$ and $k$ our gridsize in $y$ Figure 2, Section 9.3). We choose $h=k$ and let $m=a / h, n=b / h$. discretized version of (1) becomes
$$
u_{i j}=\frac{1}{4}\left(u_{i+1, j}+u_{i-1, j}+u_{i, j+1}+u_{i, j-1}\right)
$$
(see (6), Section 9.3). Our goal is to generate the approximate solution The idea is to take a guess as to what the solution may be on the gridpo Using this initial guess, we apply (2) to generate a new set of values of We repeat this process until we reach a point when the new values of $u_{i, j}$ a closely with the old ones; then we stop. The result is a sequence of num $u_{i j}$ that approximates the solution of the discretized Dirichlet problem. since the latter is an approximation to the exact solution, it follows the sequence generated by the iteration method is an approximation to exact solution.

Jacobi Iteration
Let us formalize the method that we just described. Let $U_{i j}^{0}$ denote initial guess to the solution. This initial guess is made by taking into acc the boundary values and keeping in mind that nearer boundary data sh matter more than data from far away. We may also use the averag the temperature of the boundary (see Example 1). Using (2) and $U_{i j}^{0}$

---

<!-- Page 28 -->

Left margin note (page 28)

542 Chapter 9 Finite Differer

Right margin note (page 28)

ration.
set of called on and
le l(b). ore. we left to that we
for our (corner erating
re quite rocess,

3
5
5
62
19
58
77
82
85
85
86
86
tion

++++

ce Numerical Methods

generate $U_{i j}^{1}$, which approximates the value of $u_{i j}$ after the first ite We iterate the process according to (2), thus obtaining
$$
U_{i j}^{k+1}=\frac{1}{4}\left(U_{i+1, j}^{k}+U_{i-1, j}^{k}+U_{i, j+1}^{k}+U_{i, j-1}^{k}\right)
$$
for $k=0,1,2, \ldots$. We stop our iteration when we feel that the new values $U_{i j}^{k+1}$ agrees closely with the previous set $U_{i j}^{k}$. This scheme is Jacobi iteration. We apply it to Example 1(b) of the previous secti compare results.

EXAMPLE 1 Jacobi iteration
Let us go back to the discretized version of the Dirichlet problem in Examp Section 9.3, and find an approximate solution using Jacobi iteration. As bef list the values at the gridpoints by starting with the bottom row first, fron right, and then working our way up. With this ordering, the list of values are trying to approximate with the Jacobi iteration is
$$
7.14,9.82,7.14,18.75,25,18.75,42.86,52.68,42.86
$$
(see Example 1(b), Section 9.3). To begin, we must make an initial gucss solution $U_{i j}^{0}$. Let us take the average of the values at the 12 boundary points points are excluded). This gives us $U_{i j}^{0}=300 / 12=25$ for all $i, j=1,2,3$. It once with the help of (3) with $k=0$, we obtain the list
$$
12.5,18.75,12.5,18.75,25 ., 18.75,37.5,43.75,37.5 .
$$

Comparing this list to the actual finite difference solution, we see that we a close at certain points. Now, with the help of a computer, we can iterate the by applying (3) repeatedly. The results are shown in Table 1.

\begin{table}
| \multicolumn{10}{\|c\|}{Jacobi iteration} |  |  |  |  |  |  |  |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| $k$ | $U_{1,1}^{k}$ | $U_{2,1}^{k}$ | $U_{3,1}^{k}$ | $U_{1,2}^{k}$ | $U_{2,2}^{k}$ | $U_{3,2}^{k}$ | $U_{1,3}^{k}$ | $U_{2,3}^{k}$ | $\bar{U}_{3}^{\prime}$ |
| 0 | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 2 |
| 1 | 12.5 | 18.75 | 12.5 | 18.75 | 25. | 18.75 | 37.5 | 43.75 | 37 |
| 2 | 9.375 | 12.5 | 9.375 | 18.75 | 25. | 18.75 | 40.62 | 50. | 40. |
| 3 | 7.812 | 10.94 | 7.812 | 18.75 | 25. | 18.75 | 42.19 | 51.56 | 42. |
| 4 | 7.422 | 10.16 | 7.422 | 18.75 | 25. | 18.75 | 42.58 | 52.34 | 42. |
| 5 | 7.227 | 9.961 | 7.227 | 18.75 | 25. | 18.75 | 42.77 | 52.54 | 42. |
| 6 | 7.178 | 9.863 | 7.178 | 18.75 | 25. | 18.75 | 42.82 | 52.64 | 42. |
| 7 | 7.153 | 9.839 | 7.153 | 18.75 | 25. | 18.75 | 42.85 | 52.66 | 42. |
| 8 | 7.147 | 9.827 | 7.117 | 18.75 | 25. | 18.75 | 42.85 | 52.67 | 42. |
| 9 | 7.144 | 9.824 | 7.144 | 18.75 | 25. | 18.75 | 42.86 | 52.68 | 42. |
| 10 | 7.143 | 9.822 | 7.143 | 18.75 | 25. | 18.75 | 42.86 | 52.68 | 42. |
\captionsetup{labelformat=empty}
\caption{Table 1 Starting with an initial guess (top row), we apply the Jacobi itera process to generate sets of data that converge to the finite difference solution}
\end{table}

---

<!-- Page 29 -->

Right margin note (page 29)

543
enth
our
iterwe 108s, ript left o as at in ion.
hod. and
k 28
the hod itial
ion cally the cing

++++

Section 9.4 Iteration Methods for Laplace's Equation

Note that there is little change after the ninth iteration, so we stop after the t iteration. Comparing with the actual finite difference solution, we see that results are satisfactory.

Gauss-Seidel Iteration
In general, we can improve the speed of convergence of the Jacobi ation process by taking into consideration the new sets of values that generate, as we apply formula (3). That is, after making our initial gi we iterate according to the formula
$$
U_{i j}^{k+1}=\frac{1}{4}\left(U_{i+1, j}^{k}+U_{i-1, j}^{k+1}+U_{i, j+1}^{k}+U_{i, j-1}^{k-1}\right) .
$$

Here the only difference from (3) is the appearance of $k+1$ as a superse on the two terms on the right corresponding to the points below or to the of the central point. This is known as the Gauss-Seidel method (als Liebmann's method). It is an improvement of the Jacobi method tha general will yield faster convergence to the finite difference method solut Let us illustrate with an example.

EXAMPLE 2 Gauss-Seidel iteration
For comparison's sake, we will repeat Example 1, using the Gauss-Seidel met We start with a different initial guess (see the text following this example) iterate according to (4). Our initial guess is
$$
\left(U_{1,1}^{0}, U_{2,1}^{0}, U_{3,1}^{0}, U_{1,2}^{0}, U_{2,2}^{0}, U_{3,2}^{0}, U_{1,3}^{0}, U_{2,3}^{0}, U_{3,3}^{0}\right)=(0,0,0,50,50,50,50,50,50
$$

After 16 iterations of the Gauss-Seidel formula, we arrive at the set of values
$$
(7.143,9.822,7.143,18.75,25 ., 18.75,42.86,52.68,42.86),
$$
which did not change by further iteration. With the Jacobi process, it too iterations to reach this set of values, starting with the same guess.

The relative effectiveness of a numerical method is quite sensitive to initial guess we use. For example, even though the Gauss-Seidel met is generally better than the Jacobi method, you can check that the in guess in Example 1 yields a faster convergence with the Jacobi method

Method of Successive Overrelaxation and the Heat Equat
We know that any steady-state solution to the heat equation is identic a solution to Laplace's equation. With this in mind, we can approach solution to a Dirichlet problem by modeling the heat equation and advan the time step in a procedure much like the above iteration methods.

---

<!-- Page 30 -->

Left margin note (page 30)

544 Chapter 9 Finite Differer

Right margin note (page 30)

and let barated he first ing our
specific can be resents is not ed, this taking
nce apt is, as he corole, the solving ves the thod of $1 / 2$, in in this
co use a in start tion) to lues are scheme. a good ll more guess, way to ver the

++++

acc Numerical Methods

The heat equation in two dimensions is
$$
u_{t}=c^{2}\left(u_{x x}+u_{y y}\right) .
$$

Let $h$ represent the length of the sides of the $x$ and $y$ gridsquares, $k$ now represent the time-step index. Successive time steps are se by a time $\Delta_{t}$ such that $t_{k}=k \Delta_{t}$. Using our discrete versions of $t$ derivative in $t$ and the second derivatives in $x$ and $y$, and modify results using the ideas of the Gauss-Seidel proccss, we arrive at
$$
U_{i j}^{k+1}=U_{i j}^{k}+s\left(U_{i+1, j}^{k}+U_{i-1, j}^{k+1}+U_{i, j+1}^{k}+U_{i, j-1}^{k+1}-4 U_{i j}^{k}\right),
$$
where we have set $s=\Delta_{t} c^{2} / h^{2}$. Note that (5), which has a very interpretation in terms of heat values at a cliscrete set of times. reinterpreted rather as an iterative scheme. Each new time step rep a new set of data calculated from previous data, and the process fundamentally different from our earlier iteration procedures. Inde method is just a generalization of the Gauss-Seidel method; and $s=1 / 4$ will reduce (5) to (4).

Since the values generated by (5) correspond to the finite differe proximations to the heat equation, we expect that as $t \rightarrow \infty$ (tha $k \rightarrow \infty$ ) these values should approach the steady-state solution for t responding heat equation. Thus, so long as these schemes are stal heat equation leads us quite naturally to an iterative procedure for the Dirichlet problem. It turns out that a stability analysis of (5) gi range $0<s \leq 1 / 2$. The scheme given by (5) is known as the me successive overrelaxation. With a value of $s$ in the range $0<s<$ most cases it should be the best of the iterative schemes devoloped section.

In practice, in solving a boundary value problem, it is often best combination of the methods of this and the previous section. You ca with a coarse grid and use matrix inversion (or Gaussian eliminat find approximate values of the solution at the gridpoints. If these va not sufficiently accurate, use a finer grid and switch to an iteratives Using the previously determined numerical values, you can construct guess for your initial approximation to begin your iterations. If sti accuracy is desired, you can halve your gridsize, refine your initia and continue to iterate. Each time you halve your gridsize, a good refine your solution is to average: for midpoints of gridlines average endpoints, and for centers of squares average over the four corners.

---

<!-- Page 31 -->

Right margin note (page 31)

545

1 ,
c 3,
rcise
rcise
rical
sign
your
rical
val-
tart-
tion, ion?
11,

12,
rcise
rcise

++++

Section 9.4 Iteration Methods for Laplace's Equation

Exercises 9.4
1. Use Jacobi iteration to solve the Dirichlet problem described in Exercis Section 9.3.
2. Use Jacobi iteration to solve the Dirichlet problem described in Exercis Section 9.3.
3. Use Gauss-Seidel iteration to solve the Dirichlet problem described in Exe 1, Section 9.3.
4. Use Gauss Scidel iteration to solve the Dirichlet problem described in Exe 3, Section 9.3.
5. (a) Solve Exercise 4, Section 9.3, with $m=n=10$. Compare your nume answer to the exact solution.
(b) Use Jacobi iteration to solve the Dirichlet problem. For an initial guess, as the value $1 / 4$ to all interior gridpoints. Iterate until you are within $10^{-2}$ of numerical answer in (a). How many iterations were required."
(c) Repeat (b) with a different initial guess of your choice (but not your nume answer from (a)). Take into account the boundary data.
6. Repeat Example 1(b) using Gauss-Seidel iteration, with the same starting ues. How does this method compare to Jacobi iteration?
7. Repeat Exercise 5(b) and (c) using Gauss-Seidel iteration, with the same s ing values. How does this method compare to Jacobi iteration?
8. Repcat Exercise 5(b) and (c) using the method of successive overrelaxa with the same starting values. How does this method compare to Jacobi iterat
9. Use Jacobi iteration to solve the Dirichlet problem described in Exercise Section 9.3.
10. Use Jacobi iteration to solve the Dirichlet problem described in Excrcis Section 9.3.
11. Use Gauss-Seidel iteration to solve the Dirichlet problem described in Exe 13, Section 9.3.
12. Use Gauss Seidel iteration to solve the Dirichlet problem described in Exe 14, Section 9.3.
