
# Editorial records

Reading note: 11.5 The One Dimensional Heat Equation.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Restore source glossary wording outside display math.

### Before

````text
Here $u(x,t)$ is temperature; $e(x,t)$ is thermal energy per unit volume; $\phi(x,t)$ is heat flux, positive in the positive $x$ direction (energy per unit area per unit time); and $Q(x,t)$ is heat generation per unit volume per unit time. The specific heat $s(x)$ is the energy needed to raise one unit of mass by one unit of temperature, and $\rho(x)$ is mass per unit volume. Both $s$ and $\rho$ are assumed independent of temperature and time.
````
### After

````text
$u(x,t)$ = temperature at $x$ at time $t$.

$e(x,t)$ = thermal energy density (heat energy per unit volume).

$\phi(x,t)$ = heat flux (amount of heat energy per unit time flowing in the positive direction across a unit surface).

$Q(x,t)$ = heat source (heat energy per unit volume per unit time).

$s(x)$ = specific heat (heat energy required to raise the temperature of one unit mass by one unit of temperature, assumed here to depend only on the position $x$ along the bar).

$\rho(x)$ = mass density (mass per unit volume).
````

## 2. Move editorial commentary to this record.

### Before

````text
*Editorial reference repair: the source’s unavailable uniform-convergence section is replaced by the relevant convergence condition in the text.*
````
### After

````text

````

## Source-to-current comparison

Source: /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 11 Partial Differential Equations in Rectangular Coordinates/11.5 The One Dimensional Heat Equation.md

This exact comparison preserves the full change evidence, including formatting, OCR corrections, restored source wording, and required standalone context. The entries above explain the recovery edits. The comparison is not a claim that every difference is a correction; component serialization, callout wrapping, and printed labels outside callouts are formatting.

`````diff
--- /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 11 Partial Differential Equations in Rectangular Coordinates/11.5 The One Dimensional Heat Equation.md
+++ /Users/gradyclopton/ObsidianVaults/complex_analysis/Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 11 Partial Differential Equations in Rectangular Coordinates/11.5 The One Dimensional Heat Equation.md
@@ -1,28 +1,39 @@
+
 ### 11.5 The One Dimensional Heat Equation
 
-In this and the following section we study the temperature distribution in a uniform bar of length $L$ with insulated lateral surface and no internal sources of heat, subject to certain boundary and initial conditions. To describe the problem, let $u(x, t)(0<x<L, t>0)$ represent the temperature
-
-![](./images/e7203df9-f76c-453b-be1e-147d5ba42d96-33_384_443_1103_35.jpg)
-Figure 1 Insulated bar with ends kept at $0^{\circ}$.
+In this and the following section we study the temperature distribution in a uniform bar of length $L$ with insulated lateral surface and no internal sources of heat, subject to certain boundary and initial conditions. To describe the problem, let $u(x, t)(0<x<L, t>0)$ represent the temperature of the point $x$ of the bar at time $t$ (Figure 1). Given that the initial temperature distribution of the bar is $u(x, 0)=f(x)$, and given that the ends of the bar are held at constant temperature 0 , we ask, What is $u(x, t)$ for $0<x<L, t>0$ ? As you would expect, to answer this question, we must solve a boundary value problem. We will show in the appendix at the end of this section that $u$ satisfies the one dimensional heat equation
+
+$$
+\frac{\partial u}{\partial t}=c^{2} \frac{\partial^{2} u}{\partial x^{2}}, \quad 0<x<L, \quad t>0 .
+$$
+
+In addition, $u$ satisfies the boundary conditions
+
+$$
+u(0, t)=0 \quad \text { and } \quad u(L, t)=0 \quad \text { for all } t>0
+$$
+
+and the initial condition
+
+$$
+u(x, 0)=f(x) \quad \text { for } 0<x<L .
+$$
+
+```scientific-figure
+id: 46258457-a4c6-4511-8831-5c873bd942a1
+numbered: false
+title: ""
+caption: Figure 1 Insulated bar with ends kept at $0^{\circ}$.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 11 Partial Differential Equations in Rectangular Coordinates/images/e7203df9-f76c-453b-be1e-147d5ba42d96-33_384_443_1103_35.jpg
+    caption: ""
+```
+
 
 Since the problem is first order in $t$, we only need one initial condition, unlike the wave problem where two conditions were needed.
-of the point $x$ of the bar at time $t$ (Figure 1). Given that the initial temperature distribution of the bar is $u(x, 0)=f(x)$, and given that the ends of the bar are held at constant temperature 0 , we ask, What is $u(x, t)$ for $0<x<L, t>0$ ? As you would expect, to answer this question, we must solve a boundary value problem. We will show in the appendix at the end of this section that $u$ satisfies the one dimensional heat equation
-
-$$
-\frac{\partial u}{\partial t}=c^{2} \frac{\partial^{2} u}{\partial x^{2}}, \quad 0<x<L, \quad t>0 .
-$$
-
-In addition, $u$ satisfies the boundary conditions
-
-$$
-u(0, t)=0 \quad \text { and } \quad u(L, t)=0 \quad \text { for all } t>0
-$$
-
-and the initial condition
-
-$$
-u(x, 0)=f(x) \quad \text { for } 0<x<L .
-$$
 
 We solve this problem using the method of separation of variables. After doing so, we will introduce the notion of steady-state temperature and use it to solve a related heat problem with nonzero boundary data. Interesting and important variations on these problems are presented in the following section.
 
@@ -100,7 +111,7 @@
 \lambda_{n}=c \frac{n \pi}{L}, \quad n=1,2, \ldots
 $$
 
-(see Theorem 1, Appendix A.1). We thus arrive at the product solution, or normal mode,
+(see Theorem 1, Section 10.1). We thus arrive at the product solution, or normal mode,
 
 $$
 u_{n}(x, t)=b_{n} e^{-\lambda_{n}^{2} t} \sin \frac{n \pi}{L} x, \quad n=1,2, \ldots .
@@ -122,7 +133,7 @@
 f(x)=u(x, 0)=\sum_{n=1}^{\infty} b_{n} \sin \frac{n \pi}{L} x .
 $$
 
-Recognizing this sum as the half-range sine series expansion of $f$, we get from (4), Section 2.4,
+Recognizing this sum as the half-range sine series expansion of $f$, we get from (4), Section 7.4,
 
 $$
 b_{n}=\frac{2}{L} \int_{0}^{L} f(x) \sin \frac{n \pi}{L} x d x \quad n=1,2, \ldots
@@ -130,39 +141,56 @@
 
 which completely determines the solution. We summarize our findings as follows.
 
-## SOLUTION OF THE ONE DIMENSIONAL HEAT EQUATION
-
-![](./images/e7203df9-f76c-453b-be1e-147d5ba42d96-36_421_453_1290_52.jpg)
-Figure 2 Partial sum of the sine Fourier series expansion of the initial temperature distribution (with $k$ up to 10) Section 2.3.)
-
-## The solution of the one dimensional heat boundary value problem
-
-$$
-\frac{\partial u}{\partial t}=c^{2} \frac{\partial^{2} u}{\partial x^{2}} \quad 0<x<L, \quad t>0,
-$$
-
-$$
-u(0, t)=0 \quad \text { and } \quad u(L, t)=0 \quad \text { for all } t>0,
-$$
-
-$$
-u(x, 0)=f(x) \quad \text { for } 0<x<L,
-$$
-
-is
-
-$$
-u(x, t)=\sum_{n=1}^{\infty} b_{n} e^{-\lambda_{n}^{2} t} \sin \frac{n \pi}{L} x
-$$
-
-where
-(5) $\quad b_{n}=\frac{2}{L} \int_{0}^{L} f(x) \sin \frac{n \pi}{L} x d x \quad$ and $\quad \lambda_{n}=c \frac{n \pi}{L}, \quad n=1,2, \ldots$
-
-## EXAMPLE 1 Temperature in a bar with ends held at $0^{\circ} \mathrm{C}$
-
-A thin bar of length $\pi$ units is placed in boiling water (temperature $100^{\circ} \mathrm{C}$ ). After reaching $100^{\circ} \mathrm{C}$ throughout, the bar is removed from the boiling water. With the lateral sides kept insulated, suddenly, at time $t=0$, the ends are immersed in a medium with constant freezing temperature $0^{\circ} \mathrm{C}$. Taking $c=1$, find the temperature $u(x, t)$ for $t>0$.
-
-Solution The boundary value problem that we need to solve is
+> [!equation|e4fe2eeb-5cb3-505e-b82b-6e6e72f16ad6.local at=67bcbebb-0f84-5694-a221-cdcce1200bc1] Fourier sine solution of the heat equation with zero endpoint temperatures
+> Let $c,L>0$ and let $f$ be piecewise smooth on $[0,L]$. The solution of the one dimensional heat boundary value problem
+>
+> $$
+> \frac{\partial u}{\partial t}=c^{2} \frac{\partial^{2} u}{\partial x^{2}} \quad 0<x<L, \quad t>0,
+> $$
+>
+> $$
+> u(0, t)=0 \quad \text { and } \quad u(L, t)=0 \quad \text { for all } t>0,
+> $$
+>
+> $$
+> u(x, 0)=f(x) \quad \text { for } 0<x<L,
+> $$
+>
+> is
+>
+> $$
+> u(x, t)=\sum_{n=1}^{\infty} b_{n} e^{-\lambda_{n}^{2} t} \sin \frac{n \pi}{L} x
+> $$
+>
+> where
+> $\quad b_{n}=\frac{2}{L} \int_{0}^{L} f(x) \sin \frac{n \pi}{L} x d x \quad$ and $\quad \lambda_{n}=c \frac{n \pi}{L}, \quad n=1,2, \ldots$
+>
+>
+>
+> For $t>0$ the series is smooth and satisfies the equation and endpoint conditions. As $t\downarrow0$ it approaches $f(x)$ at interior continuity points and the mean of the one-sided limits at jumps. Continuity at the initial corners additionally requires $f(0)=f(L)=0$.
+
+*Printed equation labels: (1) heat equation; (2) endpoint conditions; (3) initial condition; (4) sine-series solution; (5) Fourier coefficients and decay rates.*
+
+```scientific-figure
+id: 2d37fe31-5bc3-4df6-a794-32b5aee2c95e
+numbered: false
+title: ""
+caption: Figure 2 Partial sum of the sine Fourier series expansion of the initial temperature distribution (with $k$ up to 10). The full initial sine series is $100=\frac{400}{\pi}\sum_{k=0}^{\infty}\frac{\sin((2k+1)x)}{2k+1}$ for $0<x<\pi$.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 11 Partial Differential Equations in Rectangular Coordinates/images/e7203df9-f76c-453b-be1e-147d5ba42d96-36_421_453_1290_52.jpg
+    caption: ""
+```
+
+
+> [!exercise|1d9dbf52-a8b3-5938-b0d7-c1375d5cfb31.local at=d249faa7-6801-5cba-a8a7-153ce1bbbf91] EXAMPLE 1 Temperature in a bar with ends held at $0^{\circ} \mathrm{C}$
+> A thin bar of length $\pi$ units is placed in boiling water (temperature $100^{\circ} \mathrm{C}$ ). After reaching $100^{\circ} \mathrm{C}$ throughout, the bar is removed from the boiling water. With the lateral sides kept insulated, suddenly, at time $t=0$, the ends are immersed in a medium with constant freezing temperature $0^{\circ} \mathrm{C}$. Taking $c=1$, find the temperature $u(x, t)$ for $t>0$.
+
+##### solution
+
+The boundary value problem that we need to solve is
 
 $$
 \begin{array}{r}
@@ -187,33 +215,64 @@
 Substituting the values of $b_{n}$ and using the fact that $(1-\cos n \pi)=0$ if $n$ is even and 2 if $n$ is odd, we get
 
 $$
-u(x, t)=\frac{400}{\pi} \sum_{\substack{n=0 \\ n \text { Odd }}}^{\infty} \frac{e^{-n^{2} t}}{n} \sin n x=\frac{400}{\pi} \sum_{k=0}^{\infty} \frac{e^{-(2 k+1)^{2} t}}{2 k+1} \sin (2 k+1) x .
-$$
-
-If we plug a given value of $t$ into the series solution, we obtain a function of $x$ alone. This function gives the temperature distribution of the bar at the given time $t$. In
-
-![](./images/e7203df9-f76c-453b-be1e-147d5ba42d96-37_430_433_849_35.jpg)
-Figure 3 Approximation of the temperature by the first normal mode
-$u_{1}(x, t)=\frac{400}{\pi} e^{-t} \sin x$.
-
-particular, when $t=0, u(x, 0)$ yields the half-range sine series expansion of the initial temperature distribution $f(x)$, illustrated in Figure 2 and the first picture in Figure 4. In Figures 3 and 4, we have approximated the series solution by summing it through the terms with $k=0$ and $k=10$, respectively, and have shown the temperature distribution at various values of $t$. Notice the rapid exponential decay of the higher order terms of the series solution. The exponent of the second nonzero term is 9 times bigger and the third is 25 times bigger than the exponent of the first term. This shows that the higher order terms die exceedingly fast. Because of this fast fall off of the higher order terms, the Gibbs phenomenon, which is apparent in the first frame in Figure 4, disappears very quickly from the partial sums.
-
-![](./images/e7203df9-f76c-453b-be1e-147d5ba42d96-37_664_1288_624_513.jpg)
-Figure 4 Temperature distribution in a bar with ends held at $0^{\circ}$. The temperature decays to 0 as $t$ increases. Note that for large $t$, the shape of the graph is dominated by the first normal mode. Indeed, comparison with Figure 3 shows that the two curves are virtually indistinguishable for $t \geq 0.5$.
+u(x, t)=\frac{400}{\pi} \sum_{\substack{n=1 \\ n\text{ odd}}}^{\infty} \frac{e^{-n^{2} t}}{n} \sin n x=\frac{400}{\pi} \sum_{k=0}^{\infty} \frac{e^{-(2 k+1)^{2} t}}{2 k+1} \sin (2 k+1) x .
+$$
+
+If we plug a given value of $t$ into the series solution, we obtain a function of $x$ alone. This function gives the temperature distribution of the bar at the given time $t$. In particular, when $t=0, u(x, 0)$ yields the half-range sine series expansion of the initial temperature distribution $f(x)$, illustrated in Figure 2 and the first picture in Figure 4. In Figures 3 and 4, we have approximated the series solution by summing it through the terms with $k=0$ and $k=10$, respectively, and have shown the temperature distribution at various values of $t$. Notice the rapid exponential decay of the higher order terms of the series solution. The exponent of the second nonzero term is 9 times bigger and the third is 25 times bigger than the exponent of the first term. This shows that the higher order terms die exceedingly fast. Because of this fast fall off of the higher order terms, the Gibbs phenomenon, which is apparent in the first frame in Figure 4, disappears very quickly from the partial sums.
+
+```scientific-figure
+id: 660be31d-d6e5-4de5-9c50-59b59867aab4
+numbered: false
+title: ""
+caption: Figure 3 Approximation of the temperature by the first normal mode $u_1(x,t)=\frac{400}{\pi}e^{-t}\sin x$.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 11 Partial Differential Equations in Rectangular Coordinates/images/e7203df9-f76c-453b-be1e-147d5ba42d96-37_430_433_849_35.jpg
+    caption: ""
+```
+
+```scientific-figure
+id: 518f6412-955e-4bc9-9f15-fbb6107d4225
+numbered: false
+title: ""
+caption: Figure 4 Temperature distribution in a bar with ends held at $0^{\circ}$. The temperature decays to 0 as $t$ increases. Note that for large $t$, the shape of the graph is dominated by the first normal mode. Indeed, comparison with Figure 3 shows that the two curves are virtually indistinguishable for $t \geq 0.5$.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 11 Partial Differential Equations in Rectangular Coordinates/images/e7203df9-f76c-453b-be1e-147d5ba42d96-37_664_1288_624_513.jpg
+    caption: ""
+```
+
 
 ## Steady-State Temperature Distribution
 
-The graphs in Figure 4 show that the temperature in the bar tends to zero as $t$ increases. This is intuitively clear, since the ends of the bar are kept at $0^{\circ}$ and there is no internal source of heat. In general, the temperature distribution that we get as $t \rightarrow \infty$ is a function of $x$ alone called the steadystate solution (or time-independent solution). So, in Example 1, the steady-state solution is the function that is identically 0 .
+The graphs in Figure 4 show that the temperature in the bar tends to zero as $t$ increases. This is intuitively clear, since the ends of the bar are kept at $0^{\circ}$ and there is no internal source of heat. In general, the temperature distribution that we get as $t \rightarrow \infty$ is a function of $x$ alone called the steady-state solution (or time-independent solution). So, in Example 1, the steady-state solution is the function that is identically 0 .
 
 For general boundary conditions, since the steady-state solution is independent of $t$, we must have $\partial u / \partial t=0$. Substituting this in (1), we see that the steady-state distribution satisfies the differential equation $\frac{\partial^{2} u}{\partial x^{2}}=0$, or simply $\frac{d^{2} u}{d x^{2}}=0$, because $u$, the steady-state solution, is a function of $x$ only. The general solution of this simple differential equation is $u(x)=A x+B$, where $A$ and $B$ are constants that are determined using the boundary conditions. We illustrate with an example.
 
-![](./images/e7203df9-f76c-453b-be1e-147d5ba42d96-38_410_475_560_58.jpg)
-Figure 5 Steady-state or time-independent solution.
-
-## EXAMPLE 2 Steady-state solution
-
-Describe the steady-state solution in a bar of length $L$ with one end kept at temperature $T_{1}$ and the other at temperature $T_{2}$. Assume that the lateral surface is insulated and that there are no internal sources of heat.
-Solution We have $u(0)=T_{1}$ and $u(L)=T_{2}$. Hence, from the fact that $u(x)= A x+B$, it follows that $B=T_{1}$ and $A L+T_{1}=T_{2}$. Solving for $A$, we get $A=\frac{T_{2}-T_{1}}{L}$ and so
+```scientific-figure
+id: e10f4f1e-7403-45c5-9a1f-968e4b68a393
+numbered: false
+title: ""
+caption: Figure 5 Steady-state or time-independent solution.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 11 Partial Differential Equations in Rectangular Coordinates/images/e7203df9-f76c-453b-be1e-147d5ba42d96-38_410_475_560_58.jpg
+    caption: ""
+```
+
+
+> [!exercise|cc50bd54-d15a-5b83-b715-f05c5aa29627.local at=1e9f1768-2db0-51a6-ba9e-32bb5a3eb867] EXAMPLE 2 Steady-state solution
+> Describe the steady-state solution in a bar of length $L$ with one end kept at temperature $T_{1}$ and the other at temperature $T_{2}$. Assume that the lateral surface is insulated and that there are no internal sources of heat.
+
+##### solution
+
+We have $u(0)=T_{1}$ and $u(L)=T_{2}$. Hence, from the fact that $u(x)= A x+B$, it follows that $B=T_{1}$ and $A L+T_{1}=T_{2}$. Solving for $A$, we get $A=\frac{T_{2}-T_{1}}{L}$ and so
 
 $$
 u(x)=\frac{T_{2}-T_{1}}{L} x+T_{1} .
@@ -230,11 +289,11 @@
 Consider the heat boundary value problem
 
 $$
-\begin{gathered}
-\frac{\partial u}{\partial t}=c^{2} \frac{\partial^{2} u}{\partial x^{2}}, \quad 0<x<L, \quad t>0, \\
-u(0, t)=T_{1} \quad \text { and } \quad u(L, t)=T_{2}, \quad t>0, \\
-u(x, 0)=f(x), \quad 0<x<L .
-\end{gathered}
+\begin{gather}
+\frac{\partial u}{\partial t}=c^{2} \frac{\partial^{2} u}{\partial x^{2}}, \quad 0<x<L, \quad t>0, \tag{6} \\
+u(0, t)=T_{1} \quad \text { and } \quad u(L, t)=T_{2}, \quad t>0, \tag{7} \\
+u(x, 0)=f(x), \quad 0<x<L . \tag{8}
+\end{gather}
 $$
 
 The problem is nonhomogeneous when $T_{1}$ and $T_{2}$ are not both zero. If you try to solve it in this case using the method of separation of variables, you will encounter difficulties because of the boundary conditions. As we now show, the problem can be reduced to the zero-ends case by subtracting and then adding the steady-state solution.
@@ -243,44 +302,49 @@
 
 $$
 u_{1}(x)=\frac{T_{2}-T_{1}}{L} x+T_{1} .
+\tag{9}
 $$
 
 Subtract $u_{1}(x)$ from the initial temperature distribution in (8) and consider
 the resulting zero-ends (homogeneous) heat boundary value problem
 
 $$
-\begin{gathered}
-\frac{\partial u}{\partial t}=c^{2} \frac{\partial^{2} u}{\partial x^{2}}, \quad 0<x<L, \quad t>0, \\
-u(0, t)=0 \quad \text { and } \quad u(L, t)=0, \quad t>0, \\
-u(x, 0)=f(x)-u_{1}(x), \quad 0<x<L .
-\end{gathered}
+\begin{gather}
+\frac{\partial u}{\partial t}=c^{2} \frac{\partial^{2} u}{\partial x^{2}}, \quad 0<x<L, \quad t>0, \tag{10} \\
+u(0, t)=0 \quad \text { and } \quad u(L, t)=0, \quad t>0, \tag{11} \\
+u(x, 0)=f(x)-u_{1}(x), \quad 0<x<L . \tag{12}
+\end{gather}
 $$
 
 Let $u_{2}(x, t)$ be the solution of (10)-(12). According to (4) and (5), we have
 
 $$
 u_{2}(x, t)=\sum_{n=1}^{\infty} b_{n} e^{-\lambda_{n}^{2} t} \sin \frac{n \pi}{L} x
+\tag{13}
 $$
 
 where $\lambda_{n}=\frac{c n \pi}{L}$, and
 
 $$
 b_{n}=\frac{2}{L} \int_{0}^{L}(f(x)-\overbrace{\left(\frac{T_{2}-T_{1}}{L} x+T_{1}\right)}^{u_{1}(x)}) \sin \frac{n \pi}{L} x d x
+\tag{14}
 $$
 
 Now the solution of (6)-(8) is obtained by adding to $u_{2}(x, t)$ the steady-state solution $u_{1}(x)$ as follows:
 
 $$
 u(x, t)=u_{1}(x)+u_{2}(x, t) .
+\tag{15}
 $$
 
 This can be verified directly by plugging into the equations (6)-(8) and using the properties of $u_{1}$ and $u_{2}$ (see Exercise 10).
 
-## EXAMPLE 3 A nonhomogeneous boundary value problem
-
-Consider the experiment in Example 1. Find the solution if after bringing the temperature of the bar to $100^{\circ}$, the end at $x=0$ is frozen at $0^{\circ}$, while the end at $x=\pi$ is kept at $100^{\circ}$.
-
-Solution We have $T_{1}=0$ and $T_{2}=100$. Thus $u_{1}(x)=\frac{100}{\pi} x$, and the initial temperature distribution in (12) becomes $100-\frac{100}{\pi} x$. We now determine the coefficients in the series solution $u_{2}$ in (13). Using (14) and integration by parts, we get
+> [!exercise|e4ccf1d5-1e64-51da-8008-7cc4ee1c0eaa.local at=349d2a15-5615-5507-ae88-9f77579a532b] EXAMPLE 3 A nonhomogeneous boundary value problem
+> Consider the experiment in Example 1. Find the solution if after bringing the temperature of the bar to $100^{\circ}$, the end at $x=0$ is frozen at $0^{\circ}$, while the end at $x=\pi$ is kept at $100^{\circ}$.
+
+##### solution
+
+We have $T_{1}=0$ and $T_{2}=100$. Thus $u_{1}(x)=\frac{100}{\pi} x$, and the initial temperature distribution in (12) becomes $100-\frac{100}{\pi} x$. We now determine the coefficients in the series solution $u_{2}$ in (13). Using (14) and integration by parts, we get
 
 $$
 b_{n}=\frac{2}{\pi} \int_{0}^{\pi}\left(100-\frac{100}{\pi} x\right) \sin n x d x=\frac{200}{n \pi}
@@ -290,20 +354,16 @@
 
 $$
 u(x, t)=\frac{100}{\pi} x+\frac{200}{\pi} \sum_{n=1}^{\infty} \frac{\sin n x}{n} e^{-n^{2} t} .
-$$
-
-Two questions come to mind when we consider this solution: Does it yield the steady-state solution $u_{1}(x)$ when $t \rightarrow \infty$ ? and does it yield the initial temperature
-
-![](./images/e7203df9-f76c-453b-be1e-147d5ba42d96-40_426_466_158_51.jpg)
-Figure 6 As $t$ increases the graph of $u(x, t)$ approaches that of the steady-state solution $u_{1}(x)$. When $t=0$, the graph approximates the initial temperature distribution. Note the Gibbs phenomenon at the endpoints, causing the graph to overshoot the value 100.
-
-distribution 100 when $t=0$ ? We have $\lim _{t \rightarrow \infty} \frac{\sin n x}{n} e^{-n^{2} t}=0$. Thus each term in the series in (16) tends to 0 as $t \rightarrow \infty$, which leads us to conclude that
+\tag{16}
+$$
+
+Two questions come to mind when we consider this solution: Does it yield the steady-state solution $u_{1}(x)$ when $t \rightarrow \infty$ ? and does it yield the initial temperature distribution 100 when $t=0$ ? We have $\lim _{t \rightarrow \infty} \frac{\sin n x}{n} e^{-n^{2} t}=0$. Thus each term in the series in (16) tends to 0 as $t \rightarrow \infty$, which leads us to conclude that
 
 $$
 \lim _{t \rightarrow \infty} u(x, t)=\frac{100}{\pi} x=u_{1}(x) .
 $$
 
-This argument lacks rigor (in general, the limit of an infinite sum of functions is not equal to the sum of the limits of the functions). However, because the rate of convergence of the series is very fast, due to the terms $e^{-n^{2} t}$, this proof can be justified using properties of convergent series of functions similar to those presented in Section 2.7. Toward answering our second question, we set $t=0$ in (16) and get
+This argument lacks rigor (in general, the limit of an infinite sum of functions is not equal to the sum of the limits of the functions). However, because the rate of convergence of the series is very fast, due to the terms $e^{-n^{2} t}$, this proof can be justified using uniform convergence of the series for $t\ge t_0>0$. Toward answering our second question, we set $t=0$ in (16) and get
 
 $$
 u(x, 0)=\frac{100}{\pi} x+\frac{200}{\pi} \sum_{n=1}^{\infty} \frac{\sin n x}{n} .
@@ -317,35 +377,51 @@
 
 which yields an affirmative answer to our second question. The graphs in Figure 6 illustrate both answers. To plot $u(x, t)$ we used (16) and truncated the series after three terms. $\square$
 
+```scientific-figure
+id: 3679373a-38ac-417b-a975-818c5fe307a3
+numbered: false
+title: ""
+caption: Figure 6 As $t$ increases the graph of $u(x, t)$ approaches that of the steady-state solution $u_{1}(x)$. When $t=0$, the graph approximates the initial temperature distribution. Note the Gibbs phenomenon at the endpoints, causing the graph to overshoot the value 100.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 11 Partial Differential Equations in Rectangular Coordinates/images/e7203df9-f76c-453b-be1e-147d5ba42d96-40_426_466_158_51.jpg
+    caption: ""
+```
+
+
 From the last example, you could extract a method for solving problems with nonhomogeneous boundary conditions. By subtracting the steady-state solution, we were able to reduce to a problem with zero boundary conditions and then solve using the method of separation of variables. The success of this method depends in a crucial way on the fact that the heat equation is linear. These ideas are very important and will be used in later sections to solve more complicated nonhomogeneous higher dimensional problems.
 
 ## Appendix: Derivation of the one dimensional heat equation
 
-Consider a bar of length $L$ placed horizontally on the $x$-axis with ends at $x=0$ and $x=L$. We suppose that the cross sections of the bar are uniform and that the lateral sides of the bar are well insulated, so that heat inside the bar flows only in the $x$-direction. To derive the equation that governs the heat transfer inside the bar, we recall some definitions and laws from
-
-![](./images/e7203df9-f76c-453b-be1e-147d5ba42d96-41_394_468_645_35.jpg)
-Figure 7 Flow of heat into a small portion of the rod.
-
-physics. The following definitions will be needed:
-
-$$
-\begin{aligned}
-u(x, t)= & \text { temperature at } x \text { at time } t, \\
-e(x, t)= & \text { thermal energy density } \\
-& \text { (heat energy per unit volume) }, \\
-\phi(x, t)= & \text { heat flux (amount of heat energy per unit time flowing } \\
-& \text { in the positive direction across a unit surface), } \\
-Q(x, t)= & \text { heat source (heat energy per unit volume } \\
-& \text { per unit time), } \\
-s(x)= & \text { specific heat (heat energy required to raise the } \\
-& \text { temperature of one unit mass by one unit of temperature, } \\
-& \begin{array}{l}
-\text { assumed here to depend only on the position } x \\
-\text { along the bar), }
-\end{array} \\
-\rho(x)= & \text { mass density (mass per unit volume). }
-\end{aligned}
-$$
+Consider a bar of length $L$ placed horizontally on the $x$-axis with ends at $x=0$ and $x=L$. We suppose that the cross sections of the bar are uniform and that the lateral sides of the bar are well insulated, so that heat inside the bar flows only in the $x$-direction. To derive the equation that governs the heat transfer inside the bar, we recall some definitions and laws from physics. The following definitions will be needed:
+
+$u(x,t)$ = temperature at $x$ at time $t$.
+
+$e(x,t)$ = thermal energy density (heat energy per unit volume).
+
+$\phi(x,t)$ = heat flux (amount of heat energy per unit time flowing in the positive direction across a unit surface).
+
+$Q(x,t)$ = heat source (heat energy per unit volume per unit time).
+
+$s(x)$ = specific heat (heat energy required to raise the temperature of one unit mass by one unit of temperature, assumed here to depend only on the position $x$ along the bar).
+
+$\rho(x)$ = mass density (mass per unit volume).
+
+```scientific-figure
+id: 8e360c4d-451d-4f1a-baaf-67d6710c4436
+numbered: false
+title: ""
+caption: Figure 7 Flow of heat into a small portion of the rod.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 11 Partial Differential Equations in Rectangular Coordinates/images/e7203df9-f76c-453b-be1e-147d5ba42d96-41_394_468_645_35.jpg
+    caption: ""
+```
+
 
 Consider a thin vertical slice of the bar at $x$ with width $\Delta x$. Denote the area of the cross section by $A$ (Figure 7). The volume of the slice is $A \Delta x$, and its total thermal energy is therefore
 
@@ -363,21 +439,25 @@
 
 $$
 e(x, t)=s(x) u(x, t) \rho(x)
+\tag{17}
 $$
 
 The law of conservation of heat energy states that the rate of change of the heat energy is due to the heat energy flowing across the boundaries and internal sources of heat. Applied to the slice at $x$, the law states that
 
 $$
 \frac{\partial}{\partial t}[e(x, t) A \Delta x]=\phi(x, t) A-\phi(x+\Delta x, t) A+Q(x, t) A \Delta x
+\tag{18}
 $$
 
 (see Figure 7). The second law that we appeal to is Fourier's law of heat conduction, expressed by the equation
 
-$$
-\phi(x, t)=-K_{0} \frac{\partial u}{\partial x}
-$$
-
-where the positive constant $K_{0}$ is called the thermal conductivity. Fourier's law expresses in quantitative form the well-known fact that heat flows from
+> [!equation|d9a0dfd1-efe8-53fa-a318-6435d873e437.local at=4ffe94e8-ded7-5cc1-afc9-ea90f0eb0c1a] Fourier law of one-dimensional heat conduction
+> For temperature $u(x,t)$ and positive thermal conductivity $K_0$, the heat flux in the positive $x$ direction, measured as energy per unit area per unit time, is
+> $$
+> \phi(x,t)=-K_0\frac{\partial u}{\partial x}(x,t).
+> $$
+
+Fourier's law expresses in quantitative form the well-known fact that heat flows from
 hotter to cooler. (Thus if temperature increases as $x$ increases, the heat energy will flow to the left, explaining the minus sign in Fourier's law.)
 
 We now have all the necessary ingredients to derive the heat equation. Going back to (18), dividing by $A \Delta x$ and making $\Delta x \rightarrow 0$ on the right side of the equation, we get
@@ -412,51 +492,105 @@
 
 Letting $c^{2}=\frac{K_{0}}{s \rho}$, we get the heat equation treated in this section.
 
-## Exercises 3.5
-
-In Exercises 1-6, solve the boundary value heat problem (1)-(3) with the given data. In each case, give a brief physical explanation of the problem.
-
-1. $L=\pi, c=1, f(x)=78$.
-2. $L=\pi, c=1, f(x)=30 \sin x$.
-3. $L=\pi, c=1$,
-4. $L=\pi, c=1$,
-$f(x)= \begin{cases}33 x & \text { if } 0<x \leq \frac{\pi}{2}, \\ 33(\pi-x) & \text { if } \frac{\pi}{2}<x<\pi .\end{cases}$
-
-$$
-f(x)= \begin{cases}100 & \text { if } 0<x \leq \frac{\pi}{2} \\ 0 & \text { if } \quad \frac{\pi}{2}<x<\pi\end{cases}
-$$
-
-5. $L=1, c=1, f(x)=x$.
-6. $L=1, c=1, f(x)=e^{-x}$.
-7. (a) Plot the temperature distributions for various values of $t>0$ in Example 1, and approximate how long it will take for the maximum temperature to drop to $50^{\circ}$.
-(b) Plot the surface $z=u(x, t)(t>0)$ and explain what it represents. Be specific in your description of the surface as $t \rightarrow 0$ and $t \rightarrow \infty$.
-8. (a) Generalize Example 1 by solving the problem for arbitrary $c$.
-(b) Plot the solution at $t=1$, for $c=1,2,3$. Describe how a change in the value of $c$ affects the rate of heat transfer. Justify your answer by considering the solution given by (4) and (5).
-9. Determine the steady-state solution in a bar of length 1 with the given boundary conditions.
-(a) $u(0, t)=0, u(1, t)=100$.
-(b) $u(0, t)=100, u(1, t)=100$.
-10. (a) Verify that the solution of (6)-(8) is given by (15).
-(b) Show that, in terms of the Fourier coefficients of the initial temperature distribution $f(x)$ in (8), the coefficient in (14) is
-
-$$
-b_{n}=\frac{2}{L} \int_{0}^{L} f(x) \sin \frac{n \pi}{L} x d x-2 \frac{T_{1}+(-1)^{n+1} T_{2}}{n \pi}
-$$
-
-In Exercises 11-14, solve the nonhomogeneous boundary value problem (6)-(8) for the given data.
-11. $u(0, t)=100, u(1, t)=0, f(x)=30 \sin (\pi x), L=1, c=1$.
-12. $u(0, t)=100, u(1, t)=100, f(x)=50 x(1-x), L=1, c=1$.
-13. $u(0, t)=100, u(\pi, t)=50, f(x)$ as in Exercise $3, L=\pi, c=1$.
-14. $u(0, t)=0, u(\pi, t)=100, f(x)$ as in Exercise 4, $L=\pi, c=1$.
-15. What is the solution of (6)-(8) if the initial temperature distribution $f(x)$ is equal to the steady-state solution $u_{1}(x)$ ? Justify your answer on physical ground?
-16. Project Problem: A nonhomogeneous wave problem. Using the ideas behind the solution of the boundary value problem (6)-(8), solve the nonhomogeneous wave problem
-
-$$
-\begin{gathered}
-u_{t t}=c^{2} u_{x x}, \quad 0<x<L, \quad t>0 \\
-u(0, t)=A, \quad u(L, t)=B, \quad t>0 \\
-u(x, 0)=f(x), \quad u_{t}(x, 0)=g(x), \quad 0<x<L
-\end{gathered}
-$$
-
-where $A$ and $B$ are not both zero. (As you may verify, the time-independent solution is still $u_{1}(x)=\frac{B-A}{L} x+A$. Unlike the case of the heat equation, the solution of the wave equation does not have a limit in general as $t \rightarrow \infty$. Hence $u_{1}(x)$ is not the time-asymptotic form of the solution. However, $u_{1}$ is the solution about which the waves wiggle. For this reason, a physicist would still call $u_{1}$ the equilibrium solution.)
-17. Show that for fixed $t>0$, the solution of the heat equation (4) is uniformly convergent for $0 \leq x \leq L$. (Assume that $f(x)$ is bounded for $0 \leq x \leq L$.)
+## Exercises 11.5
+
+
+> [!prompt|db818d92-9490-5a27-8a5e-f5fd8f7818b6.local at=736a30df-8cac-56f8-8c25-a99de848f05f] Shared exercise instructions
+> In Exercises 1-6, solve the boundary value heat problem (1)-(3) with the given data. In each case, give a brief physical explanation of the problem.
+
+
+> [!exercise|f40ab9bb-4203-5b41-9154-3e6f03e96eac.local at=e8a429e1-3346-53b8-96f2-e1f2f374442d] Exercise 1
+> $L=\pi, c=1, f(x)=78$.
+
+
+> [!exercise|7474eb17-1e89-50fe-b367-6defc4ca04b2.local at=fdba799f-b73f-5c42-a529-afdb7cf221d9] Exercise 2
+> $L=\pi, c=1, f(x)=30 \sin x$.
+
+
+> [!exercise|5bfd6ea7-caff-551b-989b-3fb2754aecab.local at=6dce10f8-8b21-5663-acc7-9541211980c9] Exercise 3
+> $L=\pi, c=1$,
+> $f(x)= \begin{cases}33 x & \text { if } 0<x \leq \frac{\pi}{2}, \\ 33(\pi-x) & \text { if } \frac{\pi}{2}<x<\pi .\end{cases}$
+
+
+> [!exercise|85d5f43e-e87b-5eba-9c5e-a9547a8d10be.local at=8fb8b19d-a8b6-5b4e-9a90-51c2fe79a0ea] Exercise 4
+> $L=\pi,c=1$,
+>
+> $$
+> f(x)= \begin{cases}100 & \text { if } 0<x \leq \frac{\pi}{2} \\ 0 & \text { if } \quad \frac{\pi}{2}<x<\pi\end{cases}
+> $$
+
+
+> [!exercise|93d7d1b7-75d5-54a1-846c-7d4be460921d.local at=96a313b7-9c20-5fad-ae30-9d3198deddbe] Exercise 5
+> $L=1, c=1, f(x)=x$.
+
+
+> [!exercise|583e8a13-6b92-57e2-ab06-929b4e7508eb.local at=c89384f1-9195-5bca-bd4f-f694a219785a] Exercise 6
+> $L=1, c=1, f(x)=e^{-x}$.
+
+
+> [!exercise|1f1b44d2-5738-5c45-99a4-975d9c0cb73f.local at=43f3bbb9-0ae8-541b-b2b2-3c5b255faa09] Exercise 7
+> (a) Plot the temperature distributions for various values of $t>0$ in Example 1, and approximate how long it will take for the maximum temperature to drop to $50^{\circ}$.
+> (b) Plot the surface $z=u(x, t)(t>0)$ and explain what it represents. Be specific in your description of the surface as $t \rightarrow 0$ and $t \rightarrow \infty$.
+
+
+> [!exercise|47f50994-3121-51b5-8c08-c998d2b4a511.local at=37637156-7899-57a2-afb0-3175f5796306] Exercise 8
+> (a) Generalize Example 1 by solving the problem for arbitrary $c$.
+> (b) Plot the solution at $t=1$, for $c=1,2,3$. Describe how a change in the value of $c$ affects the rate of heat transfer. Justify your answer by considering the solution given by (4) and (5).
+
+
+> [!exercise|82383cdc-4635-5d46-926c-ae248629a217.local at=e87128d1-179a-5f85-b46a-9bbb00b75282] Exercise 9
+> Determine the steady-state solution in a bar of length 1 with the given boundary conditions.
+> (a) $u(0, t)=0, u(1, t)=100$.
+> (b) $u(0, t)=100, u(1, t)=100$.
+
+
+> [!exercise|8a89c213-05f9-5128-869e-35341ac84157.local at=4643d76b-3100-511f-a415-580c1a623f53] Exercise 10
+> (a) Verify that the solution of (6)-(8) is given by (15).
+> (b) Show that, in terms of the Fourier coefficients of the initial temperature distribution $f(x)$ in (8), the coefficient in (14) is
+>
+> $$
+> b_{n}=\frac{2}{L} \int_{0}^{L} f(x) \sin \frac{n \pi}{L} x d x-2 \frac{T_{1}+(-1)^{n+1} T_{2}}{n \pi}
+> $$
+
+
+> [!prompt|4eaf0153-881f-556b-a868-2cf6b2e1dbeb.local at=8dad63f0-5f9a-52c8-9283-bd55adf3b3aa] Shared exercise instructions
+> In Exercises 11-14, solve the nonhomogeneous boundary value problem (6)-(8) for the given data.
+
+
+> [!exercise|1bbd065d-cda8-5684-99ad-7a9310dc8378.local at=7c5ab610-0826-51bc-a705-4051dd13e3d2] Exercise 11
+> $u(0, t)=100, u(1, t)=0, f(x)=30 \sin (\pi x), L=1, c=1$.
+
+
+> [!exercise|6e40221d-b24c-5d86-ae7a-55fb43817eff.local at=c20ae38a-3c01-5e78-ace1-df29da1d950b] Exercise 12
+> $u(0, t)=100, u(1, t)=100, f(x)=50 x(1-x), L=1, c=1$.
+
+
+> [!exercise|c7a2fb92-0959-5a92-b050-81b30cea86a0.local at=94bd77d3-a0cc-5b18-8656-5422478ad023] Exercise 13
+> $u(0, t)=100, u(\pi, t)=50, f(x)$ as in Exercise $3, L=\pi, c=1$.
+
+
+> [!exercise|375797ac-db65-5abc-899d-ee5875291828.local at=5c99a142-1ae9-55ed-963c-2b3f3f65da4e] Exercise 14
+> $u(0, t)=0, u(\pi, t)=100, f(x)$ as in Exercise 4, $L=\pi, c=1$.
+
+
+> [!exercise|39b56592-67ba-5812-9c52-4041cd80379b.local at=afa52657-b4ab-561e-b6d5-ded4286986a5] Exercise 15
+> What is the solution of (6)-(8) if the initial temperature distribution $f(x)$ is equal to the steady-state solution $u_{1}(x)$ ? Justify your answer on physical ground?
+
+
+> [!exercise|4feb92f8-b675-5c60-8df6-01e905376d18.local at=7bcad258-79a8-559a-a1db-62ee22a451bd] Exercise 16
+> Project Problem: A nonhomogeneous wave problem. Using the ideas behind the solution of the boundary value problem (6)-(8), solve the nonhomogeneous wave problem
+>
+> $$
+> \begin{gathered}
+> u_{t t}=c^{2} u_{x x}, \quad 0<x<L, \quad t>0 \\
+> u(0, t)=A, \quad u(L, t)=B, \quad t>0 \\
+> u(x, 0)=f(x), \quad u_{t}(x, 0)=g(x), \quad 0<x<L
+> \end{gathered}
+> $$
+>
+> where $A$ and $B$ are not both zero. (As you may verify, the time-independent solution is still $u_{1}(x)=\frac{B-A}{L} x+A$. Unlike the case of the heat equation, the solution of the wave equation does not have a limit in general as $t \rightarrow \infty$. Hence $u_{1}(x)$ is not the time-asymptotic form of the solution. However, $u_{1}$ is the solution about which the waves wiggle. For this reason, a physicist would still call $u_{1}$ the equilibrium solution.)
+
+
+> [!exercise|b6849baa-283c-5067-8d69-205e00cf5025.local at=52dfd17c-fe9a-5109-836f-d6591ec1acfd] Exercise 17
+> Show that for fixed $t>0$, the solution of the heat equation (4) is uniformly convergent for $0 \leq x \leq L$. (Assume that $f(x)$ is bounded for $0 \leq x \leq L$.)
+

`````
