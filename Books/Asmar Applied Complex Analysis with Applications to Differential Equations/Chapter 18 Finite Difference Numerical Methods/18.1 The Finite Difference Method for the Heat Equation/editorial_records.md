
# Editorial records

Reading note: 18.1 The Finite Difference Method for the Heat Equation.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!equation|8be3d570-9f65-54d8-8ad4-5bd3d976df08.local at=cc1356ee-b017-5db7-8a9a-4b6f9d19b50a] Forward Difference Approximation of a First Time Derivative
> For a sufficiently smooth function $u(x,t)$ sampled on the uniform grid $(ih,jk)$, $k>0$, put $u_{ij}=u(ih,jk)$. Then
>
> $$
> u_t(ih,jk)\approx\frac{u_{i,j+1}-u_{ij}}{k}.
> $$
>
> The local derivative error is $O(k)$ if $u_{tt}$ is bounded near the sample.
````
### After

````text
> [!equation|8be3d570-9f65-54d8-8ad4-5bd3d976df08.local at=cc1356ee-b017-5db7-8a9a-4b6f9d19b50a] Discretization of First Derivative
> For a smooth function $u(x,t)$, let $u_{ij}=u(ih,jk)$ on a uniform grid with $h,k>0$. Then
>
> $$
> \begin{aligned}
> u_{t}(i h, j k) & \approx \frac{u(i h, j k+k)-u(i h, j k)}{k} \\
> & \approx \frac{1}{k}\left(u_{i, j+1}-u_{i j}\right)
> \end{aligned}
> $$
````

## 2. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!equation|8de3a8f9-9e94-5b61-91ca-4ae204cd2319.local at=3be280a4-58ca-5492-82c5-b9ac2e3cc78b] Centered Second Difference Approximation of a Spatial Second Derivative
> For a sufficiently smooth function $u(x,t)$ sampled on the uniform grid $(ih,jk)$, $h>0$, put $u_{ij}=u(ih,jk)$. Then
>
> $$
> u_{xx}(ih,jk)\approx\frac{u_{i+1,j}-2u_{ij}+u_{i-1,j}}{h^2}.
> $$
>
> The local derivative error is $O(h^2)$ if the fourth spatial derivative is bounded near the sample.
````
### After

````text
> [!equation|8de3a8f9-9e94-5b61-91ca-4ae204cd2319.local at=3be280a4-58ca-5492-82c5-b9ac2e3cc78b] Discretization of Second Derivative
> For a smooth function $u(x,t)$, let $u_{ij}=u(ih,jk)$ on a uniform grid with $h,k>0$. Then
>
> $$
> u_{x x}(i h, j k) \approx \frac{1}{h^{2}}\left(u_{i+1, j}-2 u_{i j}+u_{i-1, j}\right) .
> $$
````

## 3. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!equation|e650f2d0-28fd-5ccc-bcca-8fb1cddee1e1.local at=b41cfc86-b4d2-5447-8c65-fa44ba1fdd40] Explicit Forward-Time Centered-Space Scheme for the One-Dimensional Heat Equation
> For $u_t=c^2u_{xx}$, $c>0$, use spatial step $h>0$, time step $k>0$, and approximations $U_i^j\approx u(ih,jk)$. The explicit finite-difference update is
>
> $$
> U_i^{j+1}=(1-2s)U_i^j+s(U_{i+1}^j+U_{i-1}^j),\qquad s=\frac{c^2k}{h^2}.
> $$
>
> Supply initial samples and the prescribed boundary values at each step. The usual grid-independent stability restriction is $0<s\le\tfrac12$. For smooth solutions the differential-equation truncation error is $O(k+h^2)$.
````
### After

````text
> [!equation|e650f2d0-28fd-5ccc-bcca-8fb1cddee1e1.local at=b41cfc86-b4d2-5447-8c65-fa44ba1fdd40] Explicit Forward-Time Centered-Space Scheme for the One-Dimensional Heat Equation
> For the heat equation $u_t=c^2u_{xx}$, let $u_{ij}$ denote the approximation on the grid $(ih,jk)$, $h,k,c>0$. The update is
>
> $$
> u_{i, j+1}=(1-2 s) u_{i j}+s\left(u_{i+1, j}+u_{i-1,j}\right),
> $$
>
> where
>
> $$
> s=\frac{c^{2} k}{h^{2}}
> $$ Initial and boundary values are prescribed; stability requires $0<s\le1/2$.
````

## 4. Restore source wording; retain only the actual correction.

### Before

````text
Here $U$ distinguishes computed grid values from exact samples; the following working retains the source notation $u_{ij}$ for computed values.
````
### After

````text

````

## 5. Restore source wording; retain only the actual correction.

### Before

````text
The choice $s=1/2$ simplifies the formula. The usual stability restriction is $0<s\le1/2$; $s>1/2$ is unstable under mesh refinement. Stability controls error amplification, but accuracy still depends on the mesh, data regularity, and initialization. Reducing $s$ at fixed $h$ reduces the time step but does not universally guarantee a smaller total error.

[Source clarification: the printed discussion describes smaller positive $s$ as always more accurate. That conclusion is specific to the comparison below, not a general consequence of stability.]
````
### After

````text
It may appear that $s=1 / 2$ is the natural choice, since it simplifies the formula. Smaller positive values of $s$ can yield better approximations to the exact solution, as in the comparison below. In fact, it can be shown that the finite difference scheme (11) for the heat equation is unstable if $s>1 / 2$. The scheme is stable if $0<s \leq 1 / 2$, although accuracy also depends on the mesh and data.
````

## Source-to-current comparison

Source: /Users/gradyclopton/ObsidianVaults/complex_analysis/Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 18 Finite Difference Numerical Methods/.reference_mdzip/reference.md

This exact comparison preserves the full change evidence, including formatting, OCR corrections, restored source wording, and required standalone context. The entries above explain the recovery edits. The comparison is not a claim that every difference is a correction; component serialization, callout wrapping, and printed labels outside callouts are formatting.

`````diff
--- /Users/gradyclopton/ObsidianVaults/complex_analysis/Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 18 Finite Difference Numerical Methods/.reference_mdzip/reference.md
+++ /Users/gradyclopton/ObsidianVaults/complex_analysis/Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 18 Finite Difference Numerical Methods/18.1 The Finite Difference Method for the Heat Equation.md
@@ -1,24 +1,7 @@
-## Topics to Review
-
-Strictly speaking, the numerical techniques of this chapter do not require previous knowledge of partial differential equations. However, to appreciate these techniques, a familiarity with the boundary value problems of Chapter 3 is required. In particular, the analytical solutions that we developed in Sections 3.3, 3.5, 3.7, and 3.8 are useful in treating their numerical counterparts. This chapter can be covered right after Chapter 3.
-
-## Looking Ahead...
-
-In Section 9.1 we present the finite difference method and apply it to the heat equation. Section 9.1 is essential to the rest of the chapter. In Section 9.2 we apply the finite difference method for the wave equation, and in Section 9.3 we apply this method to Laplace's equation. Section 9.4 expands on the ideas of Section 9.3. For the sake of clarity, we chose simple problems to illustrate the numerical methods. However, you should keep in mind that these methods work equally well with more complicated problems and are very well suited for real-world applications.
-
-## FINITE DIFFERENCE NUMERICAL METHODS
-
-Numbers are intellectual witnesses that belong only to mankind.
--HONORÉ DE BALZAC
-Suppose that you are studying a concrete heat problem and that you want to know the temperature at times $t_{1}, t_{2}, \ldots, t_{n}$ of certain points $x_{1}, x_{2}, \ldots, x_{m}$ in a bar. If $u(x, t)$ denotes the temperature at time $t$ of the point $x$, then what you are looking for is a table of values for $u\left(x_{j}, t_{k}\right)$, where $1 \leq j \leq m$ and $1 \leq k \leq n$. When an analytical solution is available, you may be able to use it to compute $u\left(x_{j}, t_{k}\right)$. However, in many practical problems, it is impossible to compute the analytical solutions, since the data is known only on a set of discrete points.
-
-To remedy this situation, we may forgo the search for an analytical solution in favor of a numerical solution. In this chapter you will study numerical methods that are based on the principle of discretization. By discretizing a problem, you come up with an algorithm or a formula that can be used to generate numerical values of the solution at a discrete set of points. For example, in the heat problem, after discretizing, you arrive at a formula which can be iterated to generate a numerical solution.
-
-With ubiquity of computers capable of carrying out numerical computations to a very high degree of accuracy, at a minimum cost to the user, the numerical methods are gaining more and more prominence in the world of engineering and science. Moreover, they enjoy the advantage of being applicable with few constraints, as compared to some of the analytical methods. For example, the numerical scheme for the heat equation (Section 9.1) applies with equal ease to problems with a variety of boundary conditions. As you may recall from Chapter 3, with the analytical methods we had to treat these problems separately. Also, in solving Dirichlet problems in rectangular coordinates, with the analytical methods we had to restrict to rectangular regions. You will see in Sections 9.3 and 9.4 that the numerical methods can be applied to less regular regions.
-
-### 9.1 The Finite Difference Method for the Heat Equation
-
-To gain some insight and understanding of numerical techniques for solving partial differential equations, we start by considering the case of the heat equation for a finite bar. This example will illustrate the key ideas of the finite difference method and will allow us to measure the success of the numerical methods, by comparing their results with those of the analytical solution of Section 3.5.
+
+### 18.1 The Finite Difference Method for the Heat Equation
+
+To gain some insight and understanding of numerical techniques for solving partial differential equations, we start by considering the case of the heat equation for a finite bar. This example will illustrate the key ideas of the finite difference method and will allow us to measure the success of the numerical methods, by comparing their results with those of the analytical solution of Section 11.5.
 
 Let us recall the heat boundary value problem for an insulated bar with ends held at temperature 0 ,
 
@@ -30,12 +13,25 @@
 \end{aligned}
 $$
 
+*Printed equation labels: (1) heat equation; (2) endpoint conditions; (3) initial condition.*
+
 ## Discretizing the Heat Problem
 
 The idea is to discretize the problem by choosing a stepsize $h$ in $x$ and a stepsize $k$ in $t$ and trying to approximate the temperature $u$ on a grid of points in the $x t$-plane. Say we want to approximate the values of $u$ at $n-1$ equally spaced points between 0 and $L$.
 
-Figure 1 Gridpoints in the $x t$-plane. To march forward in time, we increase the value of $t_{j}$.
-![](./images/3d691698-445f-4a4d-96f7-0cb184e4b380-02_690_1074_1118_561.jpg)
+```scientific-figure
+id: a1bc41b1-703d-4e9b-abf6-14ef8b44589d
+numbered: false
+title: ""
+caption: Figure 1 Gridpoints in the $x t$-plane. To march forward in time, we increase the value of $t_{j}$.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 18 Finite Difference Numerical Methods/images/3d691698-445f-4a4d-96f7-0cb184e4b380-02_690_1074_1118_561.jpg
+    caption: ""
+```
+
 
 Take
 
@@ -48,20 +44,23 @@
 
 $$
 u_{i j}=u(i h, j k), \quad \text { where } 0<i<n \text { and } j \geq 0 .
+\tag{4}
 $$
 
 That is, $u_{i j}$ will represent the value of $u$ at the gridpoint $(i h, j k)$ (see Figure 1).
 
-At this point we would like to formulate a rule, based on (1), for determining the values $u_{i j}$ for a certain time from the values $u_{i, j \cdot l}(1 \leq i \leq n-1)$ one time step back. To arrive at this rule we take a hint from the following limits:
+At this point we would like to formulate a rule, based on (1), for determining the values $u_{i j}$ for a certain time from the values $u_{i,j-1}(1 \leq i \leq n-1)$ one time step back. To arrive at this rule we take a hint from the following limits:
 
 $$
 \lim _{k \rightarrow 0} \frac{u(x, t+k)-u(x, t)}{k}=\frac{\partial u}{\partial t}(x, t),
+\tag{5}
 $$
 
 and
 
 $$
 \lim _{h \rightarrow 0} \frac{u(x+h, t)-2 u(x, t)+u(x-h, t)}{h^{2}}=\frac{\partial^{2} u}{\partial x^{2}}(x, t) .
+\tag{6}
 $$
 
 The first of these is just the definition of the partial derivative of $u$ with respect to $t$. The second one may be verified using L'Hospital's rule (twice) as follows:
@@ -78,35 +77,40 @@
 
 $$
 u_{t}(x, t) \approx \frac{u(x, t+k)-u(x, t)}{k}
+\tag{7}
 $$
 
 and, if $h$ is sufficiently small, we have
 
 $$
 u_{x x}(x, t) \approx \frac{u(x+h, t)-2 u(x, t)+u(x-h, t)}{h^{2}} .
+\tag{8}
 $$
 
 Hence, at our gridpoints ( $i h, j k$ ) we have the approximations
 
-## DISCRETIZATION OF FIRST DERIVATIVE
-
-## \section*{DISCRETIZATION OF SECOND DERIVATIVE <br> <br> DISCRETIZATION DERIVATIVE}
-
-$$
-\begin{aligned}
-u_{t}(i h, j k) & \approx \frac{u(i h, j k+k)-u(i h, j k)}{k} \\
-& \approx \frac{1}{k}\left(u_{i, j+1}-u_{i j}\right)
-\end{aligned}
-$$
-
-and, similarly, using ( 8 ),
-□
-
-$$
-u_{x x}(i h, j k) \approx \frac{1}{h^{2}}\left(u_{i+1, j}-2 u_{i j}+u_{i-1, j}\right) .
-$$
-
-The approximation (9) is called a forward difference approximation for the first partial derivative $u_{t}$, while the approximation (10) is called a centered second difference approximation for $u_{x x}$. The latter takes account of the values of $u$ about the gridpoint $(i, j)$ in a symmetric fashion (see Figure 1). Substituting the approximations (8) and (9) into (1), we obtain
+> [!equation|8be3d570-9f65-54d8-8ad4-5bd3d976df08.local at=cc1356ee-b017-5db7-8a9a-4b6f9d19b50a] Discretization of First Derivative
+> For a smooth function $u(x,t)$, let $u_{ij}=u(ih,jk)$ on a uniform grid with $h,k>0$. Then
+>
+> $$
+> \begin{aligned}
+> u_{t}(i h, j k) & \approx \frac{u(i h, j k+k)-u(i h, j k)}{k} \\
+> & \approx \frac{1}{k}\left(u_{i, j+1}-u_{i j}\right)
+> \end{aligned}
+> $$
+
+*Printed equation label: (9).*
+
+> [!equation|8de3a8f9-9e94-5b61-91ca-4ae204cd2319.local at=3be280a4-58ca-5492-82c5-b9ac2e3cc78b] Discretization of Second Derivative
+> For a smooth function $u(x,t)$, let $u_{ij}=u(ih,jk)$ on a uniform grid with $h,k>0$. Then
+>
+> $$
+> u_{x x}(i h, j k) \approx \frac{1}{h^{2}}\left(u_{i+1, j}-2 u_{i j}+u_{i-1, j}\right) .
+> $$
+
+*Printed equation label: (10).*
+
+The approximation (9) is called a forward difference approximation for the first partial derivative $u_{t}$, while the approximation (10) is called a centered second difference approximation for $u_{x x}$. The latter takes account of the values of $u$ about the gridpoint $(i, j)$ in a symmetric fashion (see Figure 1). Substituting the forward time difference and centered spatial second difference into the heat equation, we obtain
 
 $$
 u_{i, j+1}-u_{i j}=c^{2} \frac{k}{h^{2}}\left(u_{i+1, j}-2 u_{i j}+u_{i-1, j}\right),
@@ -114,123 +118,468 @@
 
 which is our finite difference approximation to the heat equation. Combining like terms and solving for $u_{i, j+1}$, we get
 
-$$
-u_{i, j+1}=(1-2 s) u_{i j}+s\left(u_{i+1, j}+u_{i} \quad 1, j\right),
-$$
-
-where
-
-$$
-s=\frac{c^{2} k}{h^{2}}
-$$
+> [!equation|e650f2d0-28fd-5ccc-bcca-8fb1cddee1e1.local at=b41cfc86-b4d2-5447-8c65-fa44ba1fdd40] Explicit Forward-Time Centered-Space Scheme for the One-Dimensional Heat Equation
+> For the heat equation $u_t=c^2u_{xx}$, let $u_{ij}$ denote the approximation on the grid $(ih,jk)$, $h,k,c>0$. The update is
+>
+> $$
+> u_{i, j+1}=(1-2 s) u_{i j}+s\left(u_{i+1, j}+u_{i-1,j}\right),
+> $$
+>
+> where
+>
+> $$
+> s=\frac{c^{2} k}{h^{2}}
+> $$ Initial and boundary values are prescribed; stability requires $0<s\le1/2$.
+
+*Printed equation labels: (11) update formula; (12) mesh ratio $s=c^2k/h^2$.*
+
+
 
 From this we can compute the values $u_{i, j+1}$ corresponding to the $(j+1)$ th time step from the values $u_{i j}$ at the $j$ th time step.
 
 Let us now discretize the boundary and initial conditions. Since $u(x, 0)= f(x)$, we get
 
-DISCRETIZATION OF THE INITIAL CONDITION
-
-## DISCRETIZATION OF THE BOUNDARY CONDITIONS
-
-![](./images/3d691698-445f-4a4d-96f7-0cb184e4b380-05_343_414_867_31.jpg)
-Figure 2 Stepping forward in time in the hat equation.
+```scientific-figure
+id: 793e57a8-e5eb-406d-9ca5-3219cf991947
+numbered: false
+title: ""
+caption: Figure 2 Stepping forward in time in the heat equation.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 18 Finite Difference Numerical Methods/images/3d691698-445f-4a4d-96f7-0cb184e4b380-05_343_414_867_31.jpg
+    caption: ""
+```
+
 
 $$
 u_{i 0}=u(i h, 0)=f(i h), \quad 0 \leq i \leq n .
+\tag{13}
 $$
 
 Also, the boundary conditions (2) lead to
 
 $$
 u_{0 j}=u(0, j k)=0, \quad j>0,
+\tag{14}
 $$
 
 and
 
 $$
 u_{n j}=u(n h, j k)=u(L, j k)=0, \quad j>0 .
-$$
-
-We will need these boundary values as we use our difference equation (11) to step forward in time, since to compute $u_{i, j+1}$ we typically need the three values $u_{i-1, j}, u_{i j}$, and $u_{i+1, j}$. Thus when $i=1$ or $n-1$, we will noed the values $u_{0 j}$ and $u_{n j}$.
+\tag{15}
+$$
+
+We will need these boundary values as we use our difference equation (11) to step forward in time, since to compute $u_{i, j+1}$ we typically need the three values $u_{i-1, j}, u_{i j}$, and $u_{i+1, j}$. Thus when $i=1$ or $n-1$, we will need the values $u_{0 j}$ and $u_{n j}$.
 
 The method is illustrated in the diagram in Figure 2. The values of $u$ on the $x$-axis are determined by the initial condition. The values of $u$ on the vertical lines $x=0$ (the $t$-axis) and $x=L$ are determined by the boundary conditions. All other values of $u$ on the grid are computed from (11).
 
-## EXAMPLE 1 Temperature in a bar with ends held at $0^{\circ}$
-
-A thin bar of unit length is placed in boiling water (temperature $100^{\circ} \mathrm{C}$ ). After reaching $100^{\circ} \mathrm{C}$ throughout, the bar is removed from the boiling water. With the lateral sides kept insulated, suddenly, at time $t=0$, the ends are immersed in a medium with constant temperature $0^{\circ} \mathrm{C}$. Use the finite difference scheme (11), together with the boundary and initial conditions (13)-(15), to approximate the solution to this problem at the times $t=0.2,0.4,0.6,0.8$. and 1 . Take $c=1 / 2$, and use stepsizes $h=0.1$ (hence $n=10$ ) and $k=0.01$ (hence $s=1 / 4$ ). Compare your values with the values obtained using separation of variables.
-
-Solution Substituting $s=1 / 4$ into (11), we find that the boundary value problem to be solved is
+> [!exercise|c8d0b6e9-cd73-5d33-97fb-40e17c08a985.local at=0a5e64d0-425e-511a-b79f-e64084154134] EXAMPLE 1 Temperature in a bar with ends held at $0^{\circ}$
+> A thin bar of unit length is placed in boiling water (temperature $100^{\circ} \mathrm{C}$ ). After reaching $100^{\circ} \mathrm{C}$ throughout, the bar is removed from the boiling water. With the lateral sides kept insulated, suddenly, at time $t=0$, the ends are immersed in a medium with constant temperature $0^{\circ} \mathrm{C}$. Use the finite difference scheme (11), together with the boundary and initial conditions (13)-(15), to approximate the solution to this problem at the times $t=0.2,0.4,0.6,0.8$. and 1 . Take $c=1 / 2$, and use stepsizes $h=0.1$ (hence $n=10$ ) and $k=0.01$ (hence $s=1 / 4$ ). Compare your values with the values obtained using separation of variables.
+
+
+
+##### solution
+
+Substituting $s=1 / 4$ into (11), we find that the boundary value problem to be solved is
 
 $$
 u_{i, j+1}=\left(u_{i+1, j}+2 u_{i j}+u_{i-1, j}\right) / 4,
+\tag{16}
 $$
 
 together with the boundary conditions
 
 $$
 u_{0 j}=u(0,0.01 j)=0, \quad j>0,
+\tag{17}
 $$
 
 and
 
 $$
 u_{10, j}=u(1,0.01 j)=0, \quad j>0,
+\tag{18}
 $$
 
 and the initial condition
 
 $$
 u_{i 0}=u(0.1 i, 0)=f(0.1 i)=100, \quad 0 \leq i \leq 10 .
+\tag{19}
 $$
 
 Having all the necessary ingredients, we can now apply the finite difference method to obtain approximations of the solution $u$. From the initial data, we can get the values of $u$ at time $t=0.01$. Having done so. we use these values to obtain the values of $u$ at time $t=0.02$. Repeating this process eighteen more times, we obtain the desired values at time $t=0.2$, and so on. In Table 1 we show some data that results from this process, which was generated with the help of a computer.
 
-| $t \backslash x$ | 0 | 0.1 | 0.2 | 0.3 | 0.4 | 0.5 | 0.6 | 0.7 | 0.8 | 0.9 | 1 |
-| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
-| 0 | 100 | 100 | 100 | 100 | 100 | 100 | 100 | 100 | 100 | 100 | 100 |
-| 0.01 | 0 | 100 | 100 | 100 | 100 | 100 | 100 | 100 | 100 | 100 | 0 |
-| 0.02 | 0 | 75 | 100 | 100 | 100 | 100 | 100 | 100 | 100 | 75 | 0 |
-| 0.03 | 0 | 62 | 94 | 100 | 100 | 100 | 100 | 100 | 94 | 62 | 0 |
-
-Table 1 Temperature in the bar, generated with the finite difference method.
-
-In Table 2 we compare the numerical solution to the values from a partial sum approximation to the exact solution. The exact analytical solution to this problem can be found using separation of variables (see Section 3.5) and is
+```scientific-table
+id: 73f48937-5064-4167-9048-ae86083d47ed
+numbered: false
+title: ""
+caption: Table 1 Temperature in the bar, generated with the finite difference method.
+captionVisible: true
+captionPosition: below
+rows:
+  - - text: $t \backslash x$
+    - text: "0"
+    - text: "0.1"
+    - text: "0.2"
+    - text: "0.3"
+    - text: "0.4"
+    - text: "0.5"
+    - text: "0.6"
+    - text: "0.7"
+    - text: "0.8"
+    - text: "0.9"
+    - text: "1"
+  - - text: "0"
+    - text: "100"
+    - text: "100"
+    - text: "100"
+    - text: "100"
+    - text: "100"
+    - text: "100"
+    - text: "100"
+    - text: "100"
+    - text: "100"
+    - text: "100"
+    - text: "100"
+  - - text: "0.01"
+    - text: "0"
+    - text: "100"
+    - text: "100"
+    - text: "100"
+    - text: "100"
+    - text: "100"
+    - text: "100"
+    - text: "100"
+    - text: "100"
+    - text: "100"
+    - text: "0"
+  - - text: "0.02"
+    - text: "0"
+    - text: "75"
+    - text: "100"
+    - text: "100"
+    - text: "100"
+    - text: "100"
+    - text: "100"
+    - text: "100"
+    - text: "100"
+    - text: "75"
+    - text: "0"
+  - - text: "0.03"
+    - text: "0"
+    - text: "62"
+    - text: "94"
+    - text: "100"
+    - text: "100"
+    - text: "100"
+    - text: "100"
+    - text: "100"
+    - text: "94"
+    - text: "62"
+    - text: "0"
+headerRows: 1
+rowHeaders: true
+style: scientific
+```
+
+
+In Table 2 we compare the numerical solution to the values from a partial sum approximation to the exact solution. The exact analytical solution to this problem can be found using separation of variables (see Section 11.5) and is
 
 $$
 u(x, t)=\frac{400}{\pi} \sum_{m=0}^{\infty} \frac{e^{-(2 m+1)^{2} \pi^{2} t / 4}}{2 m+1} \sin (2 m+1) \pi x .
 $$
 
-| Finite difference method versus the analytical solution |  |  |  |  |  |  |  |  |  |  |  |
-| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
-| $t \backslash x$ | 0 | 0.1 | 0.2 | 0.3 | 0.4 | 0.5 | 0.6 | 0.7 | 0.8 | 0.9 | 1 |
-| 0.2 | 0 | 25 | 47 | 64 | 75 | 78 | 75 | 64 | 47 | 25 | 0 |
-|  | 0 | 24 | 46 | 63 | 74 | 77 | 74 | 63 | 46 | 24 | 0 |
-| 0.4 | 0 | 15 | 28 | 39 | 16 | 48 | 46 | 39 | 28 | 15 | 0 |
-|  | 0 | 15 | 28 | 38 | 45 | 47 | 45 | 38 | 28 | 15 | 0 |
-| 0.6 | 0 | 9 | 17 | 24 | 28 | 29 | 28 | 24 | 17 | 9 | 0 |
-|  | 0 | 9 | 17 | 23 | 28 | 29 | 28 | 23 | 17 | 9 | 0 |
-| 0.8 | 0 | 6 | 10 | 14 | 17 | 18 | 17 | 14 | 10 | 6 | 0 |
-|  | 0 | 5 | 10 | 14 | 17 | 18 | 17 | 14 | 10 | 5 | 0 |
-| 1 | 0 | 3 | 6 | 9 | 10 | 11 | 10 | 9 | 6 | 3 | 0 |
-|  | 0 | 3 | 6 | 9 | 10 | 11 | 10 | 9 | 6 | 3 | 0 |
-
-Table 2 Cells with two entries contain the values of 11 generated with the numerical solution (top) and the analytical solution (bottom). All values were rounded to the nearest integer.
-
-![](./images/3d691698-445f-4a4d-96f7-0cb184e4b380-07_391_510_197_35.jpg)
-Figure 3(a) Temperature distribution at time $t=0.2$, generated with the finite difference method.
-
-![](./images/3d691698-445f-4a4d-96f7-0cb184e4b380-07_391_518_197_622.jpg)
-Figure 3(b) Temperature distribution at time $t=0.2$, generated with a partial sum (with $m=30$ ) of the analytical solution.
-
-![](./images/3d691698-445f-4a4d-96f7-0cb184e4b380-07_398_516_190_1214.jpg)
-Figure 3(c) Comparison of the analytical and numerical solutions.
+```scientific-table
+id: e4b43f31-4f4c-4171-826a-de1c8bcc8382
+numbered: false
+title: Finite difference method versus the analytical solution
+caption: Table 2 Cells with two entries contain the values of $u$ generated with the numerical solution (top) and the analytical solution (bottom). All values were rounded to the nearest integer.
+captionVisible: true
+captionPosition: below
+rows:
+  - - text: $t \backslash x$
+    - text: "0"
+    - text: "0.1"
+    - text: "0.2"
+    - text: "0.3"
+    - text: "0.4"
+    - text: "0.5"
+    - text: "0.6"
+    - text: "0.7"
+    - text: "0.8"
+    - text: "0.9"
+    - text: "1"
+  - - text: "0.2"
+    - text: |-
+        0
+
+        0
+    - text: |-
+        25
+
+        24
+    - text: |-
+        47
+
+        46
+    - text: |-
+        64
+
+        63
+    - text: |-
+        75
+
+        74
+    - text: |-
+        78
+
+        77
+    - text: |-
+        75
+
+        74
+    - text: |-
+        64
+
+        63
+    - text: |-
+        47
+
+        46
+    - text: |-
+        25
+
+        24
+    - text: |-
+        0
+
+        0
+  - - text: "0.4"
+    - text: |-
+        0
+
+        0
+    - text: |-
+        15
+
+        15
+    - text: |-
+        28
+
+        28
+    - text: |-
+        39
+
+        38
+    - text: |-
+        46
+
+        45
+    - text: |-
+        48
+
+        47
+    - text: |-
+        46
+
+        45
+    - text: |-
+        39
+
+        38
+    - text: |-
+        28
+
+        28
+    - text: |-
+        15
+
+        15
+    - text: |-
+        0
+
+        0
+  - - text: "0.6"
+    - text: |-
+        0
+
+        0
+    - text: |-
+        9
+
+        9
+    - text: |-
+        17
+
+        17
+    - text: |-
+        24
+
+        23
+    - text: |-
+        28
+
+        28
+    - text: |-
+        29
+
+        29
+    - text: |-
+        28
+
+        28
+    - text: |-
+        24
+
+        23
+    - text: |-
+        17
+
+        17
+    - text: |-
+        9
+
+        9
+    - text: |-
+        0
+
+        0
+  - - text: "0.8"
+    - text: |-
+        0
+
+        0
+    - text: |-
+        6
+
+        5
+    - text: |-
+        10
+
+        10
+    - text: |-
+        14
+
+        14
+    - text: |-
+        17
+
+        17
+    - text: |-
+        18
+
+        18
+    - text: |-
+        17
+
+        17
+    - text: |-
+        14
+
+        14
+    - text: |-
+        10
+
+        10
+    - text: |-
+        6
+
+        5
+    - text: |-
+        0
+
+        0
+  - - text: "1"
+    - text: |-
+        0
+
+        0
+    - text: |-
+        3
+
+        3
+    - text: |-
+        6
+
+        6
+    - text: |-
+        9
+
+        9
+    - text: |-
+        10
+
+        10
+    - text: |-
+        11
+
+        11
+    - text: |-
+        10
+
+        10
+    - text: |-
+        9
+
+        9
+    - text: |-
+        6
+
+        6
+    - text: |-
+        3
+
+        3
+    - text: |-
+        0
+
+        0
+headerRows: 1
+rowHeaders: true
+style: scientific
+```
+
+
+```scientific-figure
+id: 17cd8436-1790-43a2-baa0-759c8819ac27
+numbered: false
+title: ""
+caption: "Figure 3 Temperature distributions at $t=0.2$: (a) finite-difference result; (b) analytical partial sum through $m=30$; (c) comparison."
+captionVisible: true
+captionPosition: below
+columns: 3
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 18 Finite Difference Numerical Methods/images/3d691698-445f-4a4d-96f7-0cb184e4b380-07_391_510_197_35.jpg
+    caption: ""
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 18 Finite Difference Numerical Methods/images/3d691698-445f-4a4d-96f7-0cb184e4b380-07_391_518_197_622.jpg
+    caption: ""
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 18 Finite Difference Numerical Methods/images/3d691698-445f-4a4d-96f7-0cb184e4b380-07_398_516_190_1214.jpg
+    caption: ""
+```
+
+
 
 In our approximation by the analytical solution, we took a partial sum up to $m=30$. In Figure 3(b) we plotted this partial sum at $t=1 / 5$. In Figure 3(a) we plotted the points $u(0.1 i, 1 / 5)$, for $i=0,1, \ldots, 10$, and connected them by straight lines to get a graph that approximates the real solution at time $t=1 / 5$. In Figure 3(c) we superposed both graphs for comparison's sake.
 
-Figure 4 Temperature distribution as $x$ and $t$ vary, constructed from the numerical data in Table 2.
-![](./images/3d691698-445f-4a4d-96f7-0cb184e4b380-07_673_766_1158_754.jpg)
-
-Finally, we used the data in Table 2 to generate a three-dimensional plot of the surface $:=v(x, t)$, for $0<x<1$, and $0<t<1$ (Figure 4).
+```scientific-figure
+id: 953d0300-4068-45cc-aafa-f0fa1934e6b2
+numbered: false
+title: ""
+caption: Figure 4 Temperature distribution as $x$ and $t$ vary, constructed from the numerical data in Table 2.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 18 Finite Difference Numerical Methods/images/3d691698-445f-4a4d-96f7-0cb184e4b380-07_673_766_1158_754.jpg
+    caption: ""
+```
+
+
+Finally, we used the data in Table 2 to generate a three-dimensional plot of the surface $z=u(x,t)$, for $0<x<1$, and $0<t<1$ (Figure 4).
 
 An important question comes to mind as we work through Example 1. Was our choice of $s=1 / 4$ arbitrary, or is there a reason behind it? To answer this question, we take up the topic of stability of the finite difference method.
 
@@ -242,48 +591,481 @@
 u_{i, j+1}=\frac{1}{2}\left(u_{i+1, j}+u_{i-1, j}\right) .
 $$
 
-It may appear that $s=1 / 2$ is the natural choice, since it simplifies the formula. However, it can be shown that smaller positive values of $s$ yield better approximations to the exact solution. In fact, it can be shown that the finite difference scheme (11) for the heat equation is unstable if $s>1 / 2$. The scheme is stable if $0<s \leq 1 / 2$, which means that the method gives reasonable approximations to the exact solution when $0<s \leq 1 / 2$.
+It may appear that $s=1 / 2$ is the natural choice, since it simplifies the formula. Smaller positive values of $s$ can yield better approximations to the exact solution, as in the comparison below. In fact, it can be shown that the finite difference scheme (11) for the heat equation is unstable if $s>1 / 2$. The scheme is stable if $0<s \leq 1 / 2$, although accuracy also depends on the mesh and data.
 
 As an illustration, let us revisit Example 1 and apply the finite difference method with $s=1 / 2$ (corresponding to $h=0.1, k=0.02$ ). For comparison, we show the results in Table 3, along with the results of the method with $s=1 / 4$, and the values of the analytical solution.
 
-| Varying $s$ in the finite difference method |  |  |  |  |  |  |  |  |  |  |  |
-| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
-| $t \backslash x$ | 0 | 0.1 | 0.2 | 0.3 | 0.4 | 0.5 | 0.6 | 0.7 | 0.8 | 0.9 | 1 |
-| 0.2 | 0 | 25 | 47 | 64 | 75 | 78 | 75 | 64 | 47 | 25 | 0 |
-|  | 0 | 24 | 46 | 63 | 74 | 77 | 74 | 63 | 46 | 24 | 0 |
-|  | 0 | 24 | 49 | 63 | 78 | 78 | 78 | 63 | 49 | 24 | 0 |
-| 0.4 | 0 | 15 | 28 | 39 | 46 | 48 | 46 | 39 | 28 | 15 | 0 |
-|  | 0 | 15 | 28 | 38 | 45 | 47 | 45 | 38 | 28 | 15 | 0 |
-|  | 0 | 15 | 29 | 38 | 47 | 47 | 47 | 38 | 29 | 15 | 0 |
-| 0.6 | 0 | 9 | 17 | 24 | 28 | 29 | 28 | 24 | 17 | 9 | 0 |
-|  | 0 | 9 | 17 | 23 | 28 | 29 | 28 | 23 | 17 | 9 | 0 |
-|  | 0 | 9 | 18 | 23 | 29 | 29 | 29 | 23 | 18 | 9 | 0 |
-| 0.8 | 0 | 6 | 10 | 14 | 17 | 18 | 17 | 14 | 10 | 6 | 0 |
-|  | 0 | 5 | 10 | 14 | 17 | 18 | 17 | 14 | 10 | 5 | 0 |
-|  | 0 | 5 | 11 | 14 | 17 | 17 | 17 | 14 | 11 | 5 | 0 |
-| 1 | 0 | 3 | 6 | 9 | 10 | 11 | 10 | 9 | 6 | 3 | 0 |
-|  | 0 | 3 | 6 | 9 | 10 | 11 | 10 | 9 | 6 | 3 | 0 |
-|  | 0 | 3 | 7 | 9 | 11 | 11 | 11 | 9 | 7 | 3 | 0 |
-
-Table 3 Cells with three entries contain the values of $u$ from the finite difference method with $s=1 / 4$ (top), $s=1 / 2$ (bottom), and the values from the analytical solution (center).
-
-Table 3 confirms that the method works with the limiting value $s=1 / 2$, but better results are obtained with $s<1 / 2$.
+```scientific-table
+id: 7db2f108-1b47-4452-9bec-a046929ae763
+numbered: false
+title: Varying $s$ in the finite difference method
+caption: Table 3 Cells with three entries contain the values of $u$ from the finite difference method with $s=1 / 4$ (top), $s=1 / 2$ (bottom), and the values from the analytical solution (center).
+captionVisible: true
+captionPosition: below
+rows:
+  - - text: $t \backslash x$
+    - text: "0"
+    - text: "0.1"
+    - text: "0.2"
+    - text: "0.3"
+    - text: "0.4"
+    - text: "0.5"
+    - text: "0.6"
+    - text: "0.7"
+    - text: "0.8"
+    - text: "0.9"
+    - text: "1"
+  - - text: "0.2"
+    - text: |-
+        0
+
+        0
+
+        0
+    - text: |-
+        25
+
+        24
+
+        24
+    - text: |-
+        47
+
+        46
+
+        49
+    - text: |-
+        64
+
+        63
+
+        63
+    - text: |-
+        75
+
+        74
+
+        78
+    - text: |-
+        78
+
+        77
+
+        78
+    - text: |-
+        75
+
+        74
+
+        78
+    - text: |-
+        64
+
+        63
+
+        63
+    - text: |-
+        47
+
+        46
+
+        49
+    - text: |-
+        25
+
+        24
+
+        24
+    - text: |-
+        0
+
+        0
+
+        0
+  - - text: "0.4"
+    - text: |-
+        0
+
+        0
+
+        0
+    - text: |-
+        15
+
+        15
+
+        15
+    - text: |-
+        28
+
+        28
+
+        29
+    - text: |-
+        39
+
+        38
+
+        38
+    - text: |-
+        46
+
+        45
+
+        47
+    - text: |-
+        48
+
+        47
+
+        47
+    - text: |-
+        46
+
+        45
+
+        47
+    - text: |-
+        39
+
+        38
+
+        38
+    - text: |-
+        28
+
+        28
+
+        29
+    - text: |-
+        15
+
+        15
+
+        15
+    - text: |-
+        0
+
+        0
+
+        0
+  - - text: "0.6"
+    - text: |-
+        0
+
+        0
+
+        0
+    - text: |-
+        9
+
+        9
+
+        9
+    - text: |-
+        17
+
+        17
+
+        18
+    - text: |-
+        24
+
+        23
+
+        23
+    - text: |-
+        28
+
+        28
+
+        29
+    - text: |-
+        29
+
+        29
+
+        29
+    - text: |-
+        28
+
+        28
+
+        29
+    - text: |-
+        24
+
+        23
+
+        23
+    - text: |-
+        17
+
+        17
+
+        18
+    - text: |-
+        9
+
+        9
+
+        9
+    - text: |-
+        0
+
+        0
+
+        0
+  - - text: "0.8"
+    - text: |-
+        0
+
+        0
+
+        0
+    - text: |-
+        6
+
+        5
+
+        5
+    - text: |-
+        10
+
+        10
+
+        11
+    - text: |-
+        14
+
+        14
+
+        14
+    - text: |-
+        17
+
+        17
+
+        17
+    - text: |-
+        18
+
+        18
+
+        17
+    - text: |-
+        17
+
+        17
+
+        17
+    - text: |-
+        14
+
+        14
+
+        14
+    - text: |-
+        10
+
+        10
+
+        11
+    - text: |-
+        6
+
+        5
+
+        5
+    - text: |-
+        0
+
+        0
+
+        0
+  - - text: "1"
+    - text: |-
+        0
+
+        0
+
+        0
+    - text: |-
+        3
+
+        3
+
+        3
+    - text: |-
+        6
+
+        6
+
+        7
+    - text: |-
+        9
+
+        9
+
+        9
+    - text: |-
+        10
+
+        10
+
+        11
+    - text: |-
+        11
+
+        11
+
+        11
+    - text: |-
+        10
+
+        10
+
+        11
+    - text: |-
+        9
+
+        9
+
+        9
+    - text: |-
+        6
+
+        6
+
+        7
+    - text: |-
+        3
+
+        3
+
+        3
+    - text: |-
+        0
+
+        0
+
+        0
+headerRows: 1
+rowHeaders: true
+style: scientific
+```
+
+
+Table 3 illustrates stable computations with $s=1/2$ and improved agreement for the particular $s=1/4$ comparison.
 
 We next illustrate the instability of the finite difference method for the heat equation with $s>1 / 2$.
 
-EXAMPLE 2 Instability of the finite difference method: Case $s>1 / 2$ Here we will simply repeat Example 1 with $h=0.1$ and $k=0.04$, hence $s=1$. The values generated from (11) are shown in Table 4.
-
-| Instability of the finite difference method: $s>1 / 2$ |  |  |  |  |  |  |  |  |  |  |  |
-| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
-| $t \backslash x$ | 0 | 0.1 | 0.2 | 0.3 | 0.4 | 0.5 | 0.6 | 0.7 | 0.8 | 0.9 | 1 |
-| 0 | 100 | 100 | 100 | 100 | 100 | 100 | 100 | 100 | 100 | 100 | 100 |
-| 0.04 | 0 | 100 | 100 | 100 | 100 | 100 | 100 | 100 | 100 | 100 | 0 |
-| 0.08 | 0 | 0 | 100 | 100 | 100 | 100 | 100 | 100 | 100 | 0 | 0 |
-| 0.12 | 0 | 100 | 0 | 100 | 100 | 100 | 100 | 100 | 0 | 100 | 0 |
-| 0.16 | 0 | -100 | 200 | 0 | 100 | 100 | 100 | 0 | 200 | -100 | 0 |
-| 0.20 | 0 | 300 | -300 | 300 | 0 | 100 | 0 | 300 | -300 | 300 | 0 |
-
-Table 4 Results of the finite difference method with $s=1$
+> [!exercise|697748ca-018c-53f5-8bab-6b8f27d059a6.local at=3a7a6bdd-65dd-5321-9c2e-b482e87fe3ca] EXAMPLE 2 Instability of the finite difference method: Case $s>1/2$
+> Repeat the heated-bar computation of Example 1 with $h=0.1$ and $k=0.04$, hence $s=1$, and examine the computed temperatures for instability.
+
+
+
+##### solution
+
+The values generated by the explicit heat scheme are shown in Table 4.
+
+```scientific-table
+id: 8065e254-030a-4b7a-8d13-dba288556ca8
+numbered: false
+title: "Instability of the finite difference method: $s>1 / 2$"
+caption: Table 4 Results of the finite difference method with $s=1$
+captionVisible: true
+captionPosition: below
+rows:
+  - - text: $t \backslash x$
+    - text: "0"
+    - text: "0.1"
+    - text: "0.2"
+    - text: "0.3"
+    - text: "0.4"
+    - text: "0.5"
+    - text: "0.6"
+    - text: "0.7"
+    - text: "0.8"
+    - text: "0.9"
+    - text: "1"
+  - - text: "0"
+    - text: "100"
+    - text: "100"
+    - text: "100"
+    - text: "100"
+    - text: "100"
+    - text: "100"
+    - text: "100"
+    - text: "100"
+    - text: "100"
+    - text: "100"
+    - text: "100"
+  - - text: "0.04"
+    - text: "0"
+    - text: "100"
+    - text: "100"
+    - text: "100"
+    - text: "100"
+    - text: "100"
+    - text: "100"
+    - text: "100"
+    - text: "100"
+    - text: "100"
+    - text: "0"
+  - - text: "0.08"
+    - text: "0"
+    - text: "0"
+    - text: "100"
+    - text: "100"
+    - text: "100"
+    - text: "100"
+    - text: "100"
+    - text: "100"
+    - text: "100"
+    - text: "0"
+    - text: "0"
+  - - text: "0.12"
+    - text: "0"
+    - text: "100"
+    - text: "0"
+    - text: "100"
+    - text: "100"
+    - text: "100"
+    - text: "100"
+    - text: "100"
+    - text: "0"
+    - text: "100"
+    - text: "0"
+  - - text: "0.16"
+    - text: "0"
+    - text: "-100"
+    - text: "200"
+    - text: "0"
+    - text: "100"
+    - text: "100"
+    - text: "100"
+    - text: "0"
+    - text: "200"
+    - text: "-100"
+    - text: "0"
+  - - text: "0.20"
+    - text: "0"
+    - text: "300"
+    - text: "-300"
+    - text: "300"
+    - text: "0"
+    - text: "100"
+    - text: "0"
+    - text: "300"
+    - text: "-300"
+    - text: "300"
+    - text: "0"
+headerRows: 1
+rowHeaders: true
+style: scientific
+```
+
 
 Note the appearance of negative values for the temperature. Also note the large oscillations in the values. These are obvious signs that the numerical scheme is unstable when $s=1$.
 
@@ -295,78 +1077,163 @@
 
 $$
 u(0, t)=\phi(t) \quad \text { and } \quad u(L, t)=\psi(t), t>0
+\tag{20}
 $$
 
 Following the discretization method above (see (14) and (15)), this data translates into
 
 $$
-u_{0 j}=\phi(j k) \quad \text { and } \quad u_{n j}=u(j k), j>0,
+u_{0 j}=\phi(j k) \quad \text { and } \quad u_{n j}=\psi(jk), j>0,
+\tag{21}
 $$
 
 where $n=L / h$.
 
-## EXAMPLE 3 Steady-state solution
+> [!exercise|1f09f958-5eb4-530f-8ee3-8313d6ca1749.local at=6c238903-60ce-571e-9fa1-086ce2c4df49] EXAMPLE 3 Steady-state solution
+> Approximate the heat evolution in a unit bar with $c=1/2$, initially at zero temperature, with its left end held at zero and its right end held at $100$ for $t>0$. Use $h=0.1$, $k=0.01$, and compare the profiles at $t=0.1$ and $t=1$ with the steady state.
+
+
+
+##### solution
 
 Consider the heat problem (1), (3), (20), with $c=1 / 2, L=1, \phi(t)=0, \psi(t)=$ 100 , and $f(x)=0$. We approximate the solution to this problem using the finite difference scheme given by (11), (13), and (21); that is, we shall iterate (11) using the boundary conditions
 
 $$
 u_{0 j}=0 \quad \text { and } \quad u_{n j}=100, j>0,
+\tag{22}
 $$
 
 and the initial condition
 
 $$
 u_{i 0}=0, \quad 0 \leq i \leq n .
-$$
-
-We take $h=0.1$ and $k=0.01$, and hence $n=10$ and $s=1 / 4$. In Figure 5 we present our numerical solution for the temperature distribution at the times $t=0.1$ and $t=1$. These were obtained by iterating formula (11) ten and one
-
-![](./images/3d691698-445f-4a4d-96f7-0cb184e4b380-10_341_457_268_74.jpg)
-Figure 5
+\tag{23}
+$$
+
+We take $h=0.1$ and $k=0.01$, and hence $n=10$ and $s=1 / 4$. In Figure 5 we present our numerical solution for the temperature distribution at the times $t=0.1$ and $t=1$. These were obtained by iterating the explicit heat formula ten and one hundred times, respectively. Note that the steady-state solution, $u(x,t)=100x$, is approached closely already by time $t=1$.
+
+```scientific-figure
+id: 10addddd-9c6f-4113-82c3-e11f63926892
+numbered: false
+title: ""
+caption: Figure 5
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 18 Finite Difference Numerical Methods/images/3d691698-445f-4a4d-96f7-0cb184e4b380-10_341_457_268_74.jpg
+    caption: ""
+```
+
 
 It is worthwhile to recall that when we used the separation of variables method to solve nonhomogeneous problems, in many cases we had to break the problem into several subproblems. By contrast, one nice feature of the finite difference method is that it handles these nonhomogeneous cases with no additional complications.
 
-## Exercises 9.1
-
-In Exercises 1-4, repeat Example 1 for the given initial data.
-1.
-$f(x)= \begin{cases}100 x & \text { if } 0<x<1 / 2, \\ 100(1-x) & \text { if } 1 / 2<x<1 .\end{cases}$
-3. $f(x)=\sin \pi x$.
-2.
-$f(x)= \begin{cases}100 \sin ^{2} 3 \pi x & \text { if } 0<x<1 / 3, \\ 45(1 / 3-x) & \text { if } 1 / 3<x<1 .\end{cases}$
-4. $f(x)=x(1-x)$.
-
-In Exercises 5-8, take $h=0.1$ and $k=0.02$ (hence $s=1 / 2$ ) and repeat Example 1 for the given initial data.
-5. Take $f$ as in Exercise 1.
-6. Take $f$ as in Exercise 2.
-7. Take $f$ as in Excrcise 3.
-8. Take $f$ as in Exercise 4.
-9. Verify the instability of (11) by repeating Exercise 1 with your choice of a value of $s>1 / 2$.
-
-In Exercises 10-13, discretize the given equation. That is, carry out the process analogous to that employed in the text in passing from (1) to (11), and exhibit your finite difference analog of (11).
-10. $u_{t}=c^{2} u_{x x}+3 u$.
-11. $u_{t}=c^{2} u_{x x}+2$.
-12. $u_{t}=u_{x x}+u_{x}+1$.
-13. $u_{t}=2 u_{x}$.
-14. Use the results of Exercise 11 to solve the heat boundary value problem consisting of the equation in Excrcise 11 and the following data: $L=1, c=1 / 2, f(x)=0$, $u(0, t)=u(1, t)=0$. When applying the finite difference method, take $h=0.1$ and $k=0.01$. Find the approximate temperature distribution at the times $t=0.2,0.4$, 0.6, 0.8 , and 1 .
-15. Use l'Hospital's rule to justify the backward difference approximation
-
-$$
-u_{t}\left(i h_{,} j k\right) \approx \frac{1}{k}\left(u_{i, j}-u_{i, j-1}\right)
-$$
-
-to the first partial derivative $u_{,}$at the gridpoint $(i, j)$. [Hint: Consider the difference quotient $\frac{u(x, t)-u(x, t-k)}{k}$.]
-16. Use l'Hospital's rule to justify the centered difference approximation
-
-$$
-u_{t}(i h, j k:) \approx \frac{1}{2 k}\left(u_{i, j+1}-u_{i, j-1}\right)
-$$
-
-to the first partial derivative $u_{t}$ at the gridpoint $(i, j)$. [Hint: Consider the difference quotient $\frac{n(x, t+k)-u(x, t-k)}{2 k}$ ].
-17. Repeat Example 1 letting the boundary values determine $u_{00}$ and $u_{10,0}$. That is, take the values at the "corner points" as $u_{00}=0=u_{10.0}$, wather than $u_{00}= 100=u_{10,0}$ (as was done in Exercise 1).
-18. Repeat Example 1, taking the values at the corner points as $u_{00}=50=u_{10,0}$. Thus, we are determining the valuos at the corner points as averages of the relevant boundary and initial data. In fact, your answers here should be the average of those from Example 1 and Exercise 17 (the superposition principle!).
-□
-In Exercises 19-20, you are asked to approximate the solution to the heat equation with nonhomogeneous boundary conditions. Model your solution after Example 3. but use the given boundary and initial data. Go to large enough time to see the steady-state solution.
-19. $u(x, 0)=0, u(0, t)=60, u(1, t)=20$.
-20. $u(x, 0)=400 x(1-x), u(0, t)=0, u(1, t)=40$.
-
+## Exercises 18.1
+
+
+> [!prompt|9190714a-c406-5668-a1fa-4ef37ca22688.local at=59a5288b-4159-5248-a3da-83c9fa1a568d] Shared exercise instructions
+> In Exercises 1-4, repeat Example 1 for the given initial data.
+
+
+> [!exercise|f2bf8a63-c4e8-5d05-b1fb-59706a268eb3.local at=459e7abf-416d-52f0-b082-112f30e1c33b] Exercise 1
+> $f(x)= \begin{cases}100 x & \text { if } 0<x<1 / 2, \\ 100(1-x) & \text { if } 1 / 2<x<1 .\end{cases}$
+
+
+> [!exercise|1302f90e-bc47-5e4a-91a5-150f4973ae21.local at=57b41615-56e0-5f61-86b4-766139cd3c69] Exercise 2
+> $f(x)= \begin{cases}100 \sin ^{2} 3 \pi x & \text { if } 0<x<1 / 3, \\ 45(1 / 3-x) & \text { if } 1 / 3<x<1 .\end{cases}$
+
+
+> [!exercise|79262495-c99b-5847-ac76-65feffa93b4c.local at=44a89626-d85b-563e-add2-d8e812cbd4f2] Exercise 3
+> $f(x)=\sin \pi x$.
+
+
+> [!exercise|4c2287dc-ba40-5b09-ad6e-ccc1773b0334.local at=e34e43cf-2f69-5543-8822-e90c39f164b4] Exercise 4
+> $f(x)=x(1-x)$.
+
+
+> [!prompt|9e14acc9-0a48-56aa-8e02-c8f92c787f9f.local at=e115d09e-bad3-50fd-a2ff-5058f283a9fe] Shared exercise instructions
+> In Exercises 5-8, take $h=0.1$ and $k=0.02$ (hence $s=1 / 2$ ) and repeat Example 1 for the given initial data.
+
+
+> [!exercise|fec6bffb-62f7-5d62-8021-6f1224b10e66.local at=44bee50e-62a7-5907-9feb-2b4a63bdc143] Exercise 5
+> Take $f$ as in Exercise 1.
+
+
+> [!exercise|3a060077-f1a3-504e-bca5-907c619fc28e.local at=890a058f-66c6-5ab9-9a6f-af9988071500] Exercise 6
+> Take $f$ as in Exercise 2.
+
+
+> [!exercise|1325ce5d-2cb1-58e8-92e2-bcb324d7c912.local at=946e7a9f-26c7-5792-ac19-0ccec96ead7a] Exercise 7
+> Take $f$ as in Exercise 3.
+
+
+> [!exercise|9855fbbb-433f-5574-87a1-15581dd649d0.local at=5410f6af-236a-5618-9942-f654c980d02f] Exercise 8
+> Take $f$ as in Exercise 4.
+
+
+> [!exercise|b7447690-b021-5f7c-ab8d-28fc96502e55.local at=205388e7-d205-5821-9544-458c91ded009] Exercise 9
+> Verify the instability of (11) by repeating Exercise 1 with your choice of a value of $s>1 / 2$.
+
+
+> [!prompt|cc86a9af-de6d-5143-8af1-cc3c00879eba.local at=8afbae71-e070-575c-b8f1-ea7953d635e1] Shared exercise instructions
+> In Exercises 10-13, discretize the given equation. That is, carry out the process analogous to that employed in the text in passing from (1) to (11), and exhibit your finite difference analog of (11).
+
+
+> [!exercise|90d120ab-7e78-5a30-bf40-f02ad2211284.local at=d5d69507-90bb-52f9-8de0-6ded23bc9c8c] Exercise 10
+> $u_{t}=c^{2} u_{x x}+3 u$.
+
+
+> [!exercise|54079e21-10c8-5309-949f-8c3069786600.local at=a7c0d62c-5097-5a3b-b7e8-5418e6ecdb6a] Exercise 11
+> $u_{t}=c^{2} u_{x x}+2$.
+
+
+> [!exercise|2e62a99f-8582-5d0c-918a-99b3f8336b92.local at=6464eaeb-cb56-5ecb-aaba-9851af3951b1] Exercise 12
+> $u_{t}=u_{x x}+u_{x}+1$.
+
+
+> [!exercise|c3dc5fee-1423-5676-a464-9b56c4fa69fc.local at=7fd6cd24-95f2-5c5a-81b3-cd1bdaa49325] Exercise 13
+> $u_{t}=2 u_{x}$.
+
+
+> [!exercise|7c01defb-c676-5643-a2b7-271ecd639425.local at=9d3c69d6-57a7-5e3a-8cd7-a6b216d661c0] Exercise 14
+> Use the results of Exercise 11 to solve the heat boundary value problem consisting of the equation in Exercise 11 and the following data: $L=1, c=1 / 2, f(x)=0$, $u(0, t)=u(1, t)=0$. When applying the finite difference method, take $h=0.1$ and $k=0.01$. Find the approximate temperature distribution at the times $t=0.2,0.4$, 0.6, 0.8 , and 1 .
+
+
+> [!exercise|691361dc-b621-5c44-bbd8-6ba7cb4822f8.local at=3bc10f94-add0-5628-a54e-d94107db4f92] Exercise 15
+> Use l'Hospital's rule to justify the backward difference approximation
+>
+> $$
+> u_{t}\left(ih,jk\right) \approx \frac{1}{k}\left(u_{i, j}-u_{i, j-1}\right)
+> $$
+>
+> to the first partial derivative $u_t$ at the gridpoint $(i, j)$. [Hint: Consider the difference quotient $\frac{u(x, t)-u(x, t-k)}{k}$.]
+
+
+> [!exercise|da883702-2d53-56e8-995c-a886b4562e9c.local at=69ef5650-c286-53f3-bcb3-35e95f6f6d45] Exercise 16
+> Use l'Hospital's rule to justify the centered difference approximation
+>
+> $$
+> u_{t}(i h, jk) \approx \frac{1}{2 k}\left(u_{i, j+1}-u_{i, j-1}\right)
+> $$
+>
+> to the first partial derivative $u_{t}$ at the gridpoint $(i, j)$. [Hint: Consider the difference quotient $\frac{u(x,t+k)-u(x, t-k)}{2 k}$ ].
+
+
+> [!exercise|022abfe7-8f99-5404-9e86-e23447c25991.local at=250c6044-e93c-577f-a9cc-6de8a844131d] Exercise 17
+> Repeat Example 1 letting the boundary values determine $u_{00}$ and $u_{10,0}$. That is, take the values at the "corner points" as $u_{00}=0=u_{10,0}$, rather than $u_{00}= 100=u_{10,0}$ (as was done in Exercise 1).
+
+
+> [!exercise|7d6ed5c1-d916-5725-a390-9705124cd8df.local at=d53d5ead-a351-599b-87cc-a4b17dc1c86a] Exercise 18
+> Repeat Example 1, taking the values at the corner points as $u_{00}=50=u_{10,0}$. Thus, we are determining the values at the corner points as averages of the relevant boundary and initial data. In fact, your answers here should be the average of those from Example 1 and Exercise 17 (the superposition principle!).
+
+
+> [!prompt|de4b51f9-125e-5732-871a-6340b9e860d3.local at=5c927185-0e66-53d8-a39e-662db54af385] Shared exercise instructions
+> In Exercises 19-20, you are asked to approximate the solution to the heat equation with nonhomogeneous boundary conditions. Model your solution after Example 3. but use the given boundary and initial data. Go to large enough time to see the steady-state solution.
+
+
+> [!exercise|33b55347-4c4e-5bbd-90c4-c83b47f97bd4.local at=05c15c56-f69a-54cd-bc13-92d3ead03aa8] Exercise 19
+> $u(x, 0)=0, u(0, t)=60, u(1, t)=20$.
+
+
+> [!exercise|3411acb3-da2a-5cd8-86f3-23d4ade8bd2d.local at=59c1c997-ed8c-5f6f-9458-b8845c5f7841] Exercise 20
+> $u(x, 0)=400 x(1-x), u(0, t)=0, u(1, t)=40$.

`````
