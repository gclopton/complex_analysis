
# Editorial records

Reading note: 6.3 Solving Dirichlet Problems with Conformal Mappings.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Callout 239: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Poisson Integral Solution in the Upper Half-Plane
> Let $f(x)$ be a bounded piecewise smooth function on the real line. A solution of the Dirichlet problem $\Delta u(x+i y)=0$ for $x+i y$ in the upper half-plane $(y>0)$ with boundary limit $u(x+iy)\to f(x)$ as $y\downarrow0$ at every continuity point of the real-valued function $f$ is given by the Poisson integral formula
>
> $$
> u(x+i y)=\frac{y}{\pi} \int_{-\infty}^{\infty} \frac{f(s)}{(x-s)^2+y^2} d s=\frac{y}{\pi} \int_{-\infty}^{\infty} \frac{f(x-s)}{s^2+y^2} d s
> $$
````
### After

````text
> [!theorem] Poisson Integral Formula in the Upper Half-Plane
> Let $f(x)$ be a bounded piecewise smooth function on the real line. A solution of the Dirichlet problem $\Delta u(x+i y)=0$ for $x+i y$ in the upper half-plane $(y>0)$ with boundary limit $u(x+iy)\to f(x)$ as $y\downarrow0$ at every continuity point of the real-valued function $f$ is given by the Poisson integral formula
>
> $$
> u(x+i y)=\frac{y}{\pi} \int_{-\infty}^{\infty} \frac{f(s)}{(x-s)^2+y^2} d s=\frac{y}{\pi} \int_{-\infty}^{\infty} \frac{f(x-s)}{s^2+y^2} d s
> $$
````

## 2. Move editorial commentary out of the reading note.

### Before

````text
*Editorial note: [clarified] Boundary values of piecewise smooth data are attained at continuity points; a jump cannot be prescribed as an arbitrary pointwise limit.*
````
### After

````text

````

## Source-to-current comparison

Source: /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 06 Conformal Mappings/6.3 Solving Dirichlet Problems with Conformal Mappings.md

This exact comparison preserves the full change evidence, including formatting, OCR corrections, restored source wording, and required standalone context. The entries above explain the recovery edits. The comparison is not a claim that every difference is a correction; component serialization, callout wrapping, and printed labels outside callouts are formatting.

`````diff
--- /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 06 Conformal Mappings/6.3 Solving Dirichlet Problems with Conformal Mappings.md
+++ /Users/gradyclopton/ObsidianVaults/complex_analysis/Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 06 Conformal Mappings/6.3 Solving Dirichlet Problems with Conformal Mappings.md
@@ -12,14 +12,26 @@
 > Solution To answer this question, we must solve $\Delta u=0$ inside the unit disk with boundary values $u=100$ on the upper semi-circle and $u=0$ on the lower semicircle. While the geometry of the circle makes it difficult to understand the effect of the boundary conditions on the solution inside the unit disk, the corresponding boundary value problem in the upper half-plane has a simple 
 > 
 
-**solution.** To transform the given problem into a problem in the upper half-plane, we use the linear fractional transformation $\phi(z)=i \frac{1-z}{1+z}$ from Example 1(ii), Section 6.2. It is easy to verify that $\phi(z)$ takes the upper semi-circle onto the positive real axis, and the lower semicircle onto the negative real axis. Thus $\phi$ transforms the given Dirichlet problem into a Dirichlet problem in the upper half-plane with boundary values shown in _Figure 1(b)_.
-
-
-> [!figure] Figures 1(a) and 1(b)
-> 
-> ![[Screenshot 2026-04-04 at 7.56.10 PM.png]]
-> 
-> Figures 1(a) and (b) Transforming the Dirichlet problem in _Figure 1(a)_ into an easier Dirichlet problem in _Figure 1(b)_, by using a linear fractional transformation
+##### solution
+
+To transform the given problem into a problem in the upper half-plane, we use the linear fractional transformation $\phi(z)=i \frac{1-z}{1+z}$ from Example 1(ii), Section 6.2. It is easy to verify that $\phi(z)$ takes the upper semi-circle onto the positive real axis, and the lower semicircle onto the negative real axis. Thus $\phi$ transforms the given Dirichlet problem into a Dirichlet problem in the upper half-plane with boundary values shown in _Figure 1(b)_.
+
+
+```scientific-figure
+id: 381adb71-831c-46ed-b438-6c8bb146c5b5
+numbered: false
+title: ""
+caption: |-
+  Figures 1(a) and 1(b)
+
+  Figures 1(a) and (b) Transforming the Dirichlet problem in _Figure 1(a)_ into an easier Dirichlet problem in _Figure 1(b)_, by using a linear fractional transformation
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 06 Conformal Mappings/images/Screenshot 2026-04-04 at 7.56.10 PM.png
+    caption: ""
+```
 
 $$
 \phi(z)=i \frac{1-z}{1+z} .
@@ -46,17 +58,19 @@
 2(a)_, with boundary values $u=100$ on the upper circular arc and $u=0$ on the lower circular arc.
 
 
-> [!figure] 
+<!-- Removed empty figure template. -->
 s 2(a) and 2(b)
 > 
-> ![[Screenshot 2026-04-04 at 7.57.20 PM.png]]
+> ![[Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 06 Conformal Mappings/images/Screenshot 2026-04-04 at 7.57.20 PM.png]]
 > 
 > Figures 2(a) and (b) Using a linear fractional transformation to transform a Dirich${ }^{\text {let }}$ problem in a lens (_Figure 2(a)_) into a Dirichlet problem in the first quadrant (_Figure 2(b)_). While the problem in the lens is difficult to solve, the problem in the first quadtant has a very simple solution $U^U(w)=\frac{2000}{\pi} \operatorname{Arg} w$.
 
 
 
 
-**Solution** The region $\Omega$ was discussed in Example 3, Section 6.2, from which we recall the linear fractional transformation $\phi(z)=\frac{2+i}{2-i} \frac{2+z}{2-z}$. It is straightforward to check that $\phi$ maps the lower boundary of $\Omega$ onto the positive real axis, and the upper boundary of $\Omega$ onto the positive imaginary axis. By checking the image of one point in $\Omega$, say $z=0$, we find $\phi(0)=\frac{2+i}{2-i}=\frac{1}{5}(3+4 i)$, which is a point in the first quadrant. Thus $\phi$ maps the region $\Omega$ onto the first quadrant and transforms the given problem into a Dirichlet problem in the first quadrant of the $w$-plane, with boundary conditions as shown in _Figure 2(b)_.
+##### solution
+
+The region $\Omega$ was discussed in Example 3, Section 6.2, from which we recall the linear fractional transformation $\phi(z)=\frac{2+i}{2-i} \frac{2+z}{2-z}$. It is straightforward to check that $\phi$ maps the lower boundary of $\Omega$ onto the positive real axis, and the upper boundary of $\Omega$ onto the positive imaginary axis. By checking the image of one point in $\Omega$, say $z=0$, we find $\phi(0)=\frac{2+i}{2-i}=\frac{1}{5}(3+4 i)$, which is a point in the first quadrant. Thus $\phi$ maps the region $\Omega$ onto the first quadrant and transforms the given problem into a Dirichlet problem in the first quadrant of the $w$-plane, with boundary conditions as shown in _Figure 2(b)_.
 
 It is clear that the solution in the $u$-plane is $U(w)=\frac{200}{\pi} \operatorname{Arg} w$. Thus the solution of the Dirichlet problem on $\Omega$ is
 
@@ -81,10 +95,18 @@
 $$
 
 
-> [!figure] Figure 3
-> 
-> ![[Screenshot 2026-04-04 at 7.58.23 PM.png]]
-> Figure 3 Dirichlet problem in an annulus.
+```scientific-figure
+id: 1ffc4333-1bee-4746-a4f1-ace600f15ae6
+numbered: false
+title: ""
+caption: "**Figure 3.** Dirichlet problem in an annulus."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Images/Screenshot 2026-04-04 at 7.58.23 PM.png
+    caption: ""
+```
 
 
 
@@ -92,18 +114,28 @@
 EXAMPLE 3 A problem on a region between nonconcentric circles Find a harmonic function $u$ in the nonregular annular region $\Omega$ in _Figure 4_ (a), such that $u=50$ on the inner circle $C_1$ and $u=100$ on the outer unit circle $C_2$.
 
 
-> [!figure] Figure 4(a) and 4(b)
-> 
-> ![[Screenshot 2026-04-04 at 7.59.19 PM.png]]
-> 
-> Figures 4(a) and (b) A Dirichlet problem in a nonregular annulus (_Figure 4(a)_) is greatly simplified by first transforming the region into a regular annulus (_Figure 4(b)_), using a linear fractional transformation.
-> 
-> 
-
-
-
-
-**Solution** We transform the problem into a Dirichlet problem on an annulus using the linear fractional transformation of Example 4, Section 6.2,
+```scientific-figure
+id: 85312a0d-5210-422c-9271-6749432e0bb6
+numbered: false
+title: ""
+caption: |-
+  **Figure 4.** (a) and 4(b)
+
+  Figures 4(a) and (b) A Dirichlet problem in a nonregular annulus (_Figure 4(a)_) is greatly simplified by first transforming the region into a regular annulus (_Figure 4(b)_), using a linear fractional transformation.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 06 Conformal Mappings/images/Screenshot 2026-04-04 at 7.59.19 PM.png
+    caption: ""
+```
+
+
+
+
+##### solution
+
+We transform the problem into a Dirichlet problem on an annulus using the linear fractional transformation of Example 4, Section 6.2,
 
 $$
 w=\phi(z)=\frac{3 z-1}{3-z}
@@ -141,13 +173,13 @@
 
 
 
+<!-- Source label: Poisson Integral Formula in the Upper Half-Plane -->
 > [!theorem] Poisson Integral Formula in the Upper Half-Plane
-> Let $f(x)$ be a bounded piecewise smooth function on the real line. A solution of the Dirichlet problem $\Delta u(x+i y)=0$ for $x+i y$ in the upper half-plane $(y>0)$ with boundary condition $u(x)=f(x)$ for all $-\infty<x<\infty$ is given by the Poisson integral formula
-> 
+> Let $f(x)$ be a bounded piecewise smooth function on the real line. A solution of the Dirichlet problem $\Delta u(x+i y)=0$ for $x+i y$ in the upper half-plane $(y>0)$ with boundary limit $u(x+iy)\to f(x)$ as $y\downarrow0$ at every continuity point of the real-valued function $f$ is given by the Poisson integral formula
+>
 > $$
 > u(x+i y)=\frac{y}{\pi} \int_{-\infty}^{\infty} \frac{f(s)}{(x-s)^2+y^2} d s=\frac{y}{\pi} \int_{-\infty}^{\infty} \frac{f(x-s)}{s^2+y^2} d s
 > $$
-> 
 
 
 For $y>0$, the function $P_y(x)=\sqrt{ } \frac{2}{\pi} \frac{y}{x^2+y^2} \quad(-\infty<x<\infty)$ is called the Poisson kernel on the real line. (The constant $\sqrt{\frac{2}{\pi}}$ is a normalizing constant.) We can write (3) in terms of the Poisson kernel as
@@ -162,10 +194,18 @@
 
 
 
-> [!figure] Figure 5
-> 
-> ![[Screenshot 2026-04-04 at 8.07.36 PM.png]]
-> Figure 5 How the boundary values in a Dirichlet problem are transformed, after using a linear fractional transformation that takes boundary to boundary.
+```scientific-figure
+id: 3a53a0ff-0182-4e62-9999-edcaca32c287
+numbered: false
+title: ""
+caption: "**Figure 5.** How the boundary values in a Dirichlet problem are transformed, after using a linear fractional transformation that takes boundary to boundary."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 06 Conformal Mappings/images/Screenshot 2026-04-04 at 8.07.36 PM.png
+    caption: ""
+```
 
 
 As illustrated in Figure 5, the boundary data that we get for the problem on the unit disk is given by $U\left(e^{i \phi}\right)=f\left(\psi^{-1}\left(e^{i \phi}\right)\right)$, for all $e^{i \phi}$ on the unit circle. The solution of the Dirichlet problem in the unit disk $(|w|<1)$ with this boundary data is obtained from the Poisson integral formula, which we recall from (10), Section 3.8:
@@ -228,7 +268,9 @@
 
 
 
-**Solution** We apply the first formula in (3) and get for $-\infty<x<\infty, y>0$,
+##### solution
+
+We apply the first formula in (3) and get for $-\infty<x<\infty, y>0$,
 
 $$
 u(x+i y)=\frac{y}{\pi} \int_{-\infty}^{\infty} \frac{f(s)}{(x-s)^2+y^2} d s=\frac{y}{\pi} \int_a^b \frac{C}{(x-s)^2+y^2} d s
@@ -250,11 +292,18 @@
 
 
 
-> [!figure] FIgure 6
-> 
-> ![[Screenshot 2026-04-04 at 8.10.44 PM.png]]
-> 
-> Figure 6 For a given interval $(a, b)$, the angle at $x+i y$ subtended by $(a, b)$ is a harmonic function $\alpha(x+i y)$ called the harmonic measure of $(a, b)$.
+```scientific-figure
+id: af23e444-67f0-4648-9945-47215b93b8f4
+numbered: false
+title: ""
+caption: "**Figure 6.** For a given interval $(a, b)$, the angle at $x+i y$ subtended by $(a, b)$ is a harmonic function $\\alpha(x+i y)$ called the harmonic measure of $(a, b)$."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 06 Conformal Mappings/images/Screenshot 2026-04-04 at 8.10.44 PM.png
+    caption: ""
+```
 
 
 
@@ -269,7 +318,9 @@
 > Let ( $a_1, b_1$ ) and ( $a_2, b_2$ ) be two disjoint intervals on the real line, and let $T_1$ and $T_2$ be two complex numbers. Solve the Dirichlet problem in the upper half-plane with boundary data on the real line given by $f(x)=T_1$ if $x$ is in $\left(a_1, b_1\right), T_2$ if $x$ is in ( $a_2, b_2$ ) and 0 otherwise.
 
 
-**Solution** For $j=1,2$, let $f_j(x)=T_j$ if $x$ is in $\left(a_j, b_j\right), 0$ otherwise. Clearly, $f(x)=f_1(x)+f-2(x)$. From Example 4, the solution of the Dirichlet problem
+##### solution
+
+For $j=1,2$, let $f_j(x)=T_j$ if $x$ is in $\left(a_j, b_j\right), 0$ otherwise. Clearly, $f(x)=f_1(x)+f-2(x)$. From Example 4, the solution of the Dirichlet problem
 
 in the upper half-plane with boundary values on the real line given by $f_j(x)$ is $u_j(z)=\frac{T_j}{\pi}\left[\tan ^{-1}\left(\frac{b_j-x}{y}\right)-\tan ^{-1}\left(\frac{a_j-x}{y}\right)\right]$. Thus the solution to our original problem is $u(z)=u_1(z)+u_2(z)$.
 
@@ -284,17 +335,26 @@
 
 
 
-> [!figure] Figure 7
-> 
-> ![[Screenshot 2026-04-04 at 8.19.23 PM.png]]
-> 
-> Figure 7 for Example 6.
-
-
-
-
-
-**Solution** We transform the problem into a problem in the upper half-plane by using the Joukowski mapping $w=J(z)=\frac{1}{2}\left(z+\frac{1}{z}\right)$. As shown in Example 3, Section 6.1, $J(z)$ takes the upper-unit circle onto $[-1,1]$, and the semi-infinite intervals $(-\infty,-1]$ and $[1, \infty)$ onto themselves. Thus the boundary conditions in the transformed Dirichlet problem in the upper half-plane are given by $f(w)=100$ for real $-1<w<1$ and $f(w)=0$ for real $w$ outside this interval. According to Example 4 , the solution in the upper half of the $w$-plane is given by
+```scientific-figure
+id: 98d30c1d-6f30-4384-82da-3bb2398ce96f
+numbered: false
+title: ""
+caption: "**Figure 7.** for Example 6."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 06 Conformal Mappings/images/Screenshot 2026-04-04 at 8.19.23 PM.png
+    caption: ""
+```
+
+
+
+
+
+##### solution
+
+We transform the problem into a problem in the upper half-plane by using the Joukowski mapping $w=J(z)=\frac{1}{2}\left(z+\frac{1}{z}\right)$. As shown in Example 3, Section 6.1, $J(z)$ takes the upper-unit circle onto $[-1,1]$, and the semi-infinite intervals $(-\infty,-1]$ and $[1, \infty)$ onto themselves. Thus the boundary conditions in the transformed Dirichlet problem in the upper half-plane are given by $f(w)=100$ for real $-1<w<1$ and $f(w)=0$ for real $w$ outside this interval. According to Example 4 , the solution in the upper half of the $w$-plane is given by
 
 $$
 \frac{100}{\pi}\left[\tan ^{-1}\left(\frac{1-\operatorname{Re} w}{\operatorname{Im} w}\right)+\tan ^{-1}\left(\frac{1+\operatorname{Re} w}{\operatorname{Im} w}\right)\right]
@@ -329,9 +389,18 @@
 > $$
 > 
 > 
-> > [!figure] Figure 8
-> > ![[Screenshot 2026-04-04 at 8.21.15 PM.png]]
-> > 
+> ```scientific-figure
+> id: 8e4d57d6-8f8c-412c-8c45-878e11b0aaba
+> numbered: false
+> title: ""
+> caption: "**Figure 8.**"
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 06 Conformal Mappings/images/Screenshot 2026-04-04 at 8.21.15 PM.png
+>     caption: ""
+> ```
 > 
 > 
 
@@ -347,15 +416,23 @@
 $$
 
 
-> [!figure] Figure 9
-> 
-> ![[Screenshot 2026-04-04 at 8.22.33 PM.png]]
-> 
-> Figure 9 The Poisson kernel $P_y(x)$ for various values of $y>$ 0 . Properties to note on the graphs of $P_y(x)$ as a function of $x$ :
-> $P_y(x)>0$ for all $x ;$
-> $P_y(x)$ is even;
-> $P_y(x)$ is a bell-shaped curve;
-> $\lim _{y \mid 0} P_y(0)=\infty$.
+```scientific-figure
+id: 2f254a6b-25b1-4c53-852a-39c30a58d288
+numbered: false
+title: ""
+caption: |-
+  **Figure 9.** The Poisson kernel $P_y(x)$ for various values of $y>$ 0 . Properties to note on the graphs of $P_y(x)$ as a function of $x$ :
+  $P_y(x)>0$ for all $x ;$
+  $P_y(x)$ is even;
+  $P_y(x)$ is a bell-shaped curve;
+  $\lim _{y \mid 0} P_y(0)=\infty$.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 06 Conformal Mappings/images/Screenshot 2026-04-04 at 8.22.33 PM.png
+    caption: ""
+```
 
 
 We evaluate the last integral using the residue method of Section 5.3, by completing the contour with a semicircle in the upper half-plane. The function $h(z)= \frac{1}{\left(z^2+a^2\right)\left((x-z)^2+y^2\right)}$ has two simple poles in the upper half-plane, at $z=i a$ and at $z=x+i y$. We compute the residues at these points using Proposition 1, Section 5.1(iii). We have
@@ -394,15 +471,34 @@
 > In Exercises 1-15, (a) solve the Dirichlet problem described by the accompanying figure (Figures 10-24), using the methods of this section. Examples 4 and 5 and superposition of solutions are useful.
 > (b) Evaluate your answer at various points inside the region and comment on your data, as we did in Example 3.
 > 
-> > [!figure] Figure 10 - 12
-> > 
-> > ![[Screenshot 2026-04-04 at 8.23.56 PM.png]]
-> 
-> 
-> 
-> 
-> > [!figure] Figures 13 - 24
-> > ![[Screenshot 2026-04-04 at 8.24.46 PM.png]]
+> ```scientific-figure
+> id: bb0e0730-de2e-4ece-bb85-92db438e65b7
+> numbered: false
+> title: ""
+> caption: "**Figure 10 - 12.**"
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 06 Conformal Mappings/images/Screenshot 2026-04-04 at 8.23.56 PM.png
+>     caption: ""
+> ```
+> 
+> 
+> 
+> 
+> ```scientific-figure
+> id: ee2aa24d-9098-4ee4-b6dc-50996b7d56b2
+> numbered: false
+> title: ""
+> caption: Figures 13 - 24
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 06 Conformal Mappings/images/Screenshot 2026-04-04 at 8.24.46 PM.png
+>     caption: ""
+> ```
 > 
 > 
 
@@ -437,11 +533,21 @@
 > 17. (a) Solve the Dirichlet Problem in Figure 25(a) by using the Poisson integral formula.
 > 
 > 
-> > [!figure] Figures 12(a) and (b)
-> > 
-> > ![[Screenshot 2026-04-04 at 8.27.01 PM.png]]
-> > 
-> > Figures 25(a) and (b) for Exercise 17.
+> ```scientific-figure
+> id: c3bad313-677e-4341-b602-f698d0da9fce
+> numbered: false
+> title: ""
+> caption: |-
+>   Figures 12(a) and (b)
+> 
+>   Figures 25(a) and (b) for Exercise 17.
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 06 Conformal Mappings/images/Screenshot 2026-04-04 at 8.27.01 PM.png
+>     caption: ""
+> ```
 > 
 > 
 > (b) Solve the Dirichlet problem in Figure 25(b) by using the conformal map $w= \sin z$ and the result in part (a).
@@ -510,10 +616,10 @@
 > Solve the Dirichlet problem depicted in the figure (Figures 26-31) by transforming it into a Dirichlet problem in the upper half-plane. To solve in the upper halfplane, use the Arg function in Exercises 30-32, and the Poisson integral formula in Exercises 33-35. Leave your answer in Exercise 35 in the form of an integral involving the Chebyshev polynomials. Compute the integral when $n=2$.
 > 
 > 
-> ![[Screenshot 2026-04-04 at 8.32.22 PM.png]]
-
-
-
-
-
-
+> ![[Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 06 Conformal Mappings/images/Screenshot 2026-04-04 at 8.32.22 PM.png]]
+
+
+
+
+
+

`````
