
# Editorial records

Reading note: 3.6 Cauchy's Integral Formula.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Callout 115: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem|d4998f2f-de78-5688-8967-d64dd99a8254.local at=ef0b4aed-f9b4-5d8e-b563-77d8affad9d1] Cauchy's Integral Formula for Higher Derivatives
> Suppose that $f$ is analytic on and inside a simple closed path $C$ with positive orientation, and let $n=0,1,2, \ldots$. Then $f$ has derivatives of all order at all points $z$ in the region inside $C$ given by
>
> $$
> f^{(n)}(z)=\frac{n!}{2 \pi i} \int_{C} \frac{f(\zeta)}{(\zeta-z)^{n+1}} d \zeta
> $$
>
> (For $n=0$, we take by definition $f^{(0)}=f$ and $0!=1$.)
````
### After

````text
> [!theorem|d4998f2f-de78-5688-8967-d64dd99a8254.local at=ef0b4aed-f9b4-5d8e-b563-77d8affad9d1] Generalized Cauchy Integral Formula
> Suppose that $f$ is analytic on and inside a simple closed path $C$ with positive orientation, and let $n=0,1,2, \ldots$. Then $f$ has derivatives of all order at all points $z$ in the region inside $C$ given by
>
> $$
> f^{(n)}(z)=\frac{n!}{2 \pi i} \int_{C} \frac{f(\zeta)}{(\zeta-z)^{n+1}} d \zeta
> $$
>
> (For $n=0$, we take by definition $f^{(0)}=f$ and $0!=1$.)
````

## 2. Callout 118: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem|70e2b56b-0382-5393-b403-9cd77ee040f1.local at=a7759aeb-464a-57e3-918b-4baeceda5e84] Morera's Theorem for Complex Analyticity
> Let $f$ be a continuous complex-valued function on a region $\Omega$. If
>
> $$
> \int_{\gamma} f(z) d z=0
> $$
>
> for all closed paths $\gamma$ in $\Omega$, then $f$ is analytic on $\Omega$.
````
### After

````text
> [!theorem|70e2b56b-0382-5393-b403-9cd77ee040f1.local at=a7759aeb-464a-57e3-918b-4baeceda5e84] Morera's Theorem
> Let $f$ be a continuous complex-valued function on a region $\Omega$. If
>
> $$
> \int_{\gamma} f(z) d z=0
> $$
>
> for all closed paths $\gamma$ in $\Omega$, then $f$ is analytic on $\Omega$.
````

## Source-to-current comparison

Source: /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 03 Complex Integration/3.6 Cauchy's Integral Formula.md

This exact comparison preserves the full change evidence, including formatting, OCR corrections, restored source wording, and required standalone context. The entries above explain the recovery edits. The comparison is not a claim that every difference is a correction; component serialization, callout wrapping, and printed labels outside callouts are formatting.

`````diff
--- /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 03 Complex Integration/3.6 Cauchy's Integral Formula.md
+++ /Users/gradyclopton/ObsidianVaults/complex_analysis/Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/3.6 Cauchy's Integral Formula.md
@@ -1,7 +1,7 @@
 
 
 
-> [!review]
+> [!review|9ae928ca-8153-530e-9bf1-3b3c25f9a4de.local at=3a1b8d96-3367-5b0a-ac27-3cc3f9dd55ff]
 > 1. If a function is analytic on and inside a closed curve, can its value at an interior point be recovered exactly from its values on the enclosing curve alone? Prove your answer.
 > 2. If the reconstruction integral from Cauchy's formula is evaluated at a point outside the curve instead of inside, what value does it take, and why? Prove your answer.
 
@@ -12,21 +12,29 @@
 In this section we develop one of the most important consequences of Cauchy's integral theorem. It is the Cauchy integral formula, which will enable us to compute many interesting integrals, and more importantly, we will use it to derive fundamental properties of analytic functions.
 
 
-> [!theorem] Theorem 1: Cauchy's Integral Formula
+<!-- Source label: Theorem 1: Cauchy's Integral Formula -->
+> [!theorem|3d522871-a1b2-5132-8af1-b8e5eae0fb1d.local at=60eb9868-52de-5cab-92e2-8589c720f009] Cauchy's Integral Formula
 > Suppose that $f$ is analytic inside and on a simple closed path $C$ with positive orientation. If $z$ is any point inside $C$, then
-> 
+>
 > $$
 > f(z)=\frac{1}{2 \pi i} \int_{C} \frac{f(\zeta)}{\zeta-z} d \zeta
 > $$
-> 
 
 **Proof** Given $z$ inside $C$, let $R>0$ be such that the closed disk $S_{R}(z)$ is contained in the region inside $C$. The function $\zeta \mapsto \frac{f(\zeta)}{\zeta-z}$ is analytic in the region inside $C$ and outside the circle $C_{r}(z)$, where $0<r \leq R$ (see _Figure 1_). 
 
 
-> [!figure] Figure 1
-> 
-> ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-067_485_462_1175_36.jpg)
-> Figure 1 The path $C$ can be continuously deformed into the circle $C_{r}(z)$, which explains the equality (2).
+```scientific-figure
+id: 850f373f-2aab-4133-9f18-e1805ad293dc
+numbered: false
+title: ""
+caption: "**Figure 1.** The path $C$ can be continuously deformed into the circle $C_{r}(z)$, which explains the equality (2)."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-067_485_462_1175_36.jpg
+    caption: ""
+```
 
 
 
@@ -68,7 +76,7 @@
 (It is traditional to change the variables of integration from $\zeta$ to $z$ when applying Theorem 1.)
 
 
-> [!exercise] Exercise 1: Cauchy's integral formula
+> [!exercise|d260b275-820b-57ec-a8b3-3f7301465f67.local at=5c47902b-7a6a-500f-9819-a478203c5e9a] Exercise 1: Cauchy's integral formula
 > 
 > Let $C_{R}\left(z_{0}\right)$ denote the positively oriented circle with center at $z_{0}$ and radius $R>0$. Compute the following integrals.
 > (a) $\quad \int_{C_{2}(0)} \frac{e^{z}}{z+1} d z$,
@@ -99,7 +107,7 @@
 Some integrals require multiple applications of Cauchy's formula along with applications of Cauchy's theorem. We illustrate with one example.
 
 
-> [!exercise] Exercise 2: Multiple applications of Cauchy's formula
+> [!exercise|87cab3ac-f65a-5821-8fc1-9f99aa0f9012.local at=e588ff2a-4738-52cb-b6e5-0b656bd9a800] Exercise 2: Multiple applications of Cauchy's formula
 > 
 > Compute
 > 
@@ -109,15 +117,23 @@
 > 
 > 
 
-**Solution** Since $z^{2}+1=(z+i)(z-i)$, the integral cannot be computed directly from Cauchy's formula, since the path contains both $\pm i$ in its interior. To overcome this difficulty, draw small nonintersecting circles inside $C_{2}(0)$ around $\pm i$, say $C_{1 / 4}(i)$ and $C_{1 / 4}(-i)$, as illustrated in _Figure 2_. 
-
-
-> [!figure] Figure 2
-> 
-> ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-068_519_519_1705_79.jpg)
-> 
-> Figure 2 The mean value property of $f$ states that the value of $f$ at $z$ is equal to the average value of $f$ around any circle in $\Omega$ centered at $z$.
-> 
+##### solution
+
+Since $z^{2}+1=(z+i)(z-i)$, the integral cannot be computed directly from Cauchy's formula, since the path contains both $\pm i$ in its interior. To overcome this difficulty, draw small nonintersecting circles inside $C_{2}(0)$ around $\pm i$, say $C_{1 / 4}(i)$ and $C_{1 / 4}(-i)$, as illustrated in _Figure 2_. 
+
+
+```scientific-figure
+id: 88424214-53a5-4427-b11d-29fdf0f17504
+numbered: false
+title: ""
+caption: "**Figure 2.** The mean value property of $f$ states that the value of $f$ at $z$ is equal to the average value of $f$ around any circle in $\\Omega$ centered at $z$."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-068_519_519_1705_79.jpg
+    caption: ""
+```
 
 
 
@@ -160,7 +176,7 @@
 
 
 
-> [!review]
+> [!review|d9cea8af-1df4-5fe1-a01f-28359c914585.local at=99cf444a-4b32-51d1-ab0d-97e888e8c9d3]
 > 1. Cauchy's formula shows that the values of an analytic function inside an enclosing curve are determined by its values on the curve. What additional information about the function do those same boundary values also determine, and by what mechanism is it extracted? Prove your answer.
 > 2. If the point at which the generalized Cauchy integral formula is evaluated lies outside the enclosing curve instead of inside, what value does the integral take, and why? Prove your answer.
 
@@ -192,13 +208,14 @@
 
 
 
-> [!theorem] Theorem 2: Generalized Cauchy Integral Formula
+<!-- Source label: Theorem 2: Generalized Cauchy Integral Formula -->
+> [!theorem|d4998f2f-de78-5688-8967-d64dd99a8254.local at=ef0b4aed-f9b4-5d8e-b563-77d8affad9d1] Generalized Cauchy Integral Formula
 > Suppose that $f$ is analytic on and inside a simple closed path $C$ with positive orientation, and let $n=0,1,2, \ldots$. Then $f$ has derivatives of all order at all points $z$ in the region inside $C$ given by
-> 
+>
 > $$
 > f^{(n)}(z)=\frac{n!}{2 \pi i} \int_{C} \frac{f(\zeta)}{(\zeta-z)^{n+1}} d \zeta
 > $$
-> 
+>
 > (For $n=0$, we take by definition $f^{(0)}=f$ and $0!=1$.)
 
 
@@ -209,7 +226,7 @@
 
 
 
-> [!exercise] Exercise 3: Generalized Cauchy integral formula
+> [!exercise|105a7c13-ac00-5a01-9d87-a08e521323cc.local at=5bec7534-1fcd-5b7e-bb80-ce36108a1879] Exercise 3: Generalized Cauchy integral formula
 > 
 > Compute the following integrals:
 > (a) $\frac{1}{2 \pi i} \int_{C_{2}(0)} \frac{z^{10}}{(z-1)^{11}} d z$,
@@ -218,15 +235,25 @@
 
 
 
-> [!figure] Figure 3
-> 
-> ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-070_452_512_1156_83.jpg)
-> Figure 3 Ellipse in Example 3.
-
-
-
-
-**Solution** (a) By (6), we have
+```scientific-figure
+id: 74bb3550-20ca-496f-92f5-fffe026c9c42
+numbered: false
+title: ""
+caption: "**Figure 3.** Ellipse in Example 3."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-070_452_512_1156_83.jpg
+    caption: ""
+```
+
+
+
+
+##### solution
+
+(a) By (6), we have
 
 $$
 \frac{10!}{2 \pi i} \int_{C_{2}(0)} \frac{z^{10}}{(z-1)^{11}} d z=\left.\frac{d^{10}}{d z^{10}} z^{10}\right|_{z=1}=10!
@@ -253,7 +280,7 @@
 
 
 
-> [!exercise] Exercise 4: A path that intersects itself
+> [!exercise|4fb400eb-ae11-5d66-8358-25cee229f02e.local at=59afabaf-884a-5153-8c1e-e03818a8f314] Exercise 4: A path that intersects itself
 > 
 > Compute
 > 
@@ -265,19 +292,35 @@
 > where $\Gamma$ is the figure-eight in _Figure 4_.
 
 
-> [!figure] Figure 4
-> 
-> ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-070_490_540_1848_63.jpg)
-> Figure 4 The figure-eight path $\Gamma$ is not a simple path.
+```scientific-figure
+id: ae436efe-183d-4f5b-a1ce-18a9a55abe12
+numbered: false
+title: ""
+caption: "**Figure 4.** The figure-eight path $\\Gamma$ is not a simple path."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-070_490_540_1848_63.jpg
+    caption: ""
+```
 
 
 Solution Because the path intersects itself, it is not simple. So we cannot appeal to Cauchy's formulas directly. We will first decompose the path $\Gamma$ into two simple paths $\Gamma_{1}$ and $\Gamma_{2}$, as shown in _Figure 5_. 
 
 
-> [!figure] Figure 5
-> 
-> ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-071_495_483_566_55.jpg)
-> Figue 5 Decomposition of a figure-eight into two simple paths.
+```scientific-figure
+id: 8ad69a9f-930a-46c4-9265-9dbc0f23466f
+numbered: false
+title: ""
+caption: "**Figure 5.** Figue 5 Decomposition of a figure-eight into two simple paths."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-071_495_483_566_55.jpg
+    caption: ""
+```
 
 
 
@@ -307,7 +350,7 @@
 
 
 
-> [!review]
+> [!review|5b05a56e-ba5d-5220-9336-30d7c9c0e918.local at=6fa53112-d34f-52ad-abae-07762b1f71ac]
 > 1. In real analysis, a function can be once differentiable without being twice differentiable. Does the same situation occur for analytic functions, or does something stronger hold? Prove your answer.
 > 2. If $f=u+i v$ is analytic on an open set $\Omega$, what can be said about the partial derivatives of $u$ and $v$ ?
 > 3. If a continuous complex-valued function on a region has the property that its integral around every closed path in the region equals zero, what can be said about the function itself? Prove your answer.
@@ -325,7 +368,8 @@
 
 
 
-> [!corollary] Corollary 1
+<!-- Source label: Corollary 1 -->
+> [!corollary|fa7d1ab9-2709-5641-9169-f95432466198.local at=874a7f64-a487-5752-ac15-69f797a526b4] Analyticity of All Higher Complex Derivatives
 > Suppose that $f$ is analytic in an open set $\Omega$. Then $f$ has derivatives of all order, $f^{\prime}, f^{\prime \prime}, f^{\prime \prime \prime}, \ldots$, which are analytic in $\Omega$.
 
 
@@ -341,9 +385,9 @@
 
 
 
-> [!corollary] Corollary 2
+<!-- Source label: Corollary 2 -->
+> [!corollary|203ef65d-19ef-5768-8bb0-51b3de85bfb4.local at=349da879-2050-5ca7-855a-bf0a41bea677] Harmonicity of Partial Derivatives of Analytic Functions
 > Suppose that $f=u+i v$ is analytic in an open set $\Omega$. Then all the partial derivatives of $u$ and $v$ exist and are harmonic in $\Omega$.
-> 
 
 **Proof** From Corollary 1, we know that $f$ has analytic derivatives of all orders. Since the derivatives of $f$ exist, we can obtain them by partial differentiation with respect to either $x$ or $y$ (recall the Cauchy-Riemann equations, (8), Section 2.4). This shows that the partial derivatives of $u$ and $v$ exist and are the real or imaginary parts of analytic functions, and hence they are harmonic. For example, differentiating $f=u+i v$ with respect to $x$ yields $f^{\prime}(z)=u_{x}(z)+i v_{x}(z)$. Since $f^{\prime}$ is analytic, we see that $u_{x}$ and $v_{x}$ are harmonic. Differentiating with respect to $y$, we obtain $f^{\prime \prime}(z)=v_{x y}(z)-i u_{x y}(z)$, showing that $v_{x y}$ and $u_{x y}$ are harmonic, and so forth. Since all $f^{(n)}(z)$ are continuously differentiable, any partial derivative of $u$ or $v$ will have continuous second-order partials; these partial derivatives commute, and the conditions for harmonicity in Section 2.5 are now clearly established.
 
@@ -352,13 +396,14 @@
 
 
 
-> [!theorem] Theorem 3: Morera's Theorem
+<!-- Source label: Theorem 3: Morera's Theorem -->
+> [!theorem|70e2b56b-0382-5393-b403-9cd77ee040f1.local at=a7759aeb-464a-57e3-918b-4baeceda5e84] Morera's Theorem
 > Let $f$ be a continuous complex-valued function on a region $\Omega$. If
-> 
+>
 > $$
 > \int_{\gamma} f(z) d z=0
 > $$
-> 
+>
 > for all closed paths $\gamma$ in $\Omega$, then $f$ is analytic on $\Omega$.
 
 
@@ -371,13 +416,14 @@
 
 
 
-> [!theorem] Theorem 4
+<!-- Source label: Theorem 4 -->
+> [!theorem|c82dfabe-3f4e-5f08-a4a9-07f3f3024dad.local at=5b618e22-5659-5434-b64e-5ba9628c230b] Analytic Extension of a Complex Difference Quotient
 > Suppose that $f$ is analytic on a region $\Omega$ and let $z_{0}$ be in $\Omega$. Define
-> 
+>
 > $$
 > g(z)= \begin{cases}\frac{f(z)-f\left(z_{0}\right)}{z-z_{0}} & \text { if } z \neq z_{0} \\ f^{\prime}\left(z_{0}\right) & \text { if } z=z_{0}\end{cases}
 > $$
-> 
+>
 > Then $g$ is analytic in $\Omega$.
 
 
@@ -399,7 +445,7 @@
 
 
 
-> [!exercise] Exercise 5: Extending $\frac{\sin z}{z}$ to an entire function
+> [!exercise|d684947f-1241-5660-8966-4aea851d2dec.local at=f084258c-cb3c-5ea4-9834-2d95c626e13d] Exercise 5: Extending $\frac{\sin z}{z}$ to an entire function
 > 
 > Show that the function $\sin z / z$, which is defined for all $z \neq 0$, can be extended to an entire function. Determine the value that must be assigned at $z=0$, and justify that the resulting extension is entire.
 
@@ -432,7 +478,7 @@
 
 
 
-> [!exercise] Exercise 6
+> [!exercise|4be6e7c9-20d0-54c7-a268-00db49442244.local at=a983fe8e-3b60-50f9-ba00-488299e14aad] Exercise 6
 > In problems 1-20, evaluate the given integral. State clearly which version of Cauchy's theorem you are using and justify its application. It would help to plot the path in each case and describe exactly the points of interest in each problem. As usual, $C_{R}\left(z_{0}\right)$ denotes the positively oriented circle with center at $z_{0}$ and radius $R>0$.
 > 
 > 1. $\int_{C_{1}(0)} \frac{\cos z}{z} d z$.
@@ -448,38 +494,70 @@
 > 11. $\int_{\gamma} \frac{e^{z} \sin z}{z^{2}(z-\pi)} d z$, where $\gamma$ is as in _Figure 6_.
 > 
 > 
-> > [!figure] Figure 6
-> > 
-> > ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-074_494_513_272_81.jpg)
-> > Figure 6
+> ```scientific-figure
+> id: 3ea05539-5ab9-493e-93c8-ea4ccd583b70
+> numbered: false
+> title: ""
+> caption: "**Figure 6.**"
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-074_494_513_272_81.jpg
+>     caption: ""
+> ```
 > 
 > 
 > 
 > 12. $\int_{\gamma} \frac{d z}{z^{2}(z-1)^{3}(z+3)}$, where $\gamma$ is as in _Figure 7_.
 > 
 > 
-> > [!figure] Figure 7
-> > 
-> > ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-074_486_523_838_85.jpg)
-> > Figure 7
+> ```scientific-figure
+> id: 9d4b2201-2115-4c8e-8f43-05505e3fe472
+> numbered: false
+> title: ""
+> caption: "**Figure 7.**"
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-074_486_523_838_85.jpg
+>     caption: ""
+> ```
 > 
 > 
 > 13. $\int_{\gamma} \frac{z+\cos (\pi z)}{z\left(z^{2}+1\right)} d z$, where $\gamma$ is as in _Figure 8_.
 > 
 > 
-> > [!figure] Figure 8
-> > 
-> > ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-074_502_527_1373_87.jpg)
-> > Figure 8 (negative orientation).
+> ```scientific-figure
+> id: f92f8207-5a28-419c-9c9a-58e7f8f64be9
+> numbered: false
+> title: ""
+> caption: "**Figure 8.** (negative orientation)."
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-074_502_527_1373_87.jpg
+>     caption: ""
+> ```
 > 
 > 
 > 14. $\int_{\gamma} \frac{1}{z(z-1)^{2}\left(z^{2}-1\right)} d z$, where $\gamma$ is as in _Figure 9_.
 > 
 > 
-> > [!figure] Figure 9
-> > 
-> > ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-074_526_533_1956_85.jpg)
-> > Figure 9
+> ```scientific-figure
+> id: f8ff3f05-4cb7-47c0-80f7-3615455b922b
+> numbered: false
+> title: ""
+> caption: "**Figure 9.**"
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-074_526_533_1956_85.jpg
+>     caption: ""
+> ```
 > 
 > 
 > 15. $\int_{C_{2}(0)} \frac{z^{2}+z+1}{z^{2}-1} d z$.
@@ -492,36 +570,36 @@
 
 
 
-> [!exercise] Exercise 7
+> [!exercise|d588a438-538d-5aec-a9a4-bb3abfd6160a.local at=1b092896-9c88-57c4-808d-668422bbeb0b] Exercise 7
 > 21. For $|z|<1$, let $f(z)=\frac{1}{2 \pi} \int_{0}^{2 \pi} \frac{e^{i t}}{e^{i t}-z} d t$.
 > (a) Show that $f$ is analytic in the unit disk. **(Hint: Theorem 4, Section 3.5.)**
 > (b) Express the integral as a path integral and conclude that $f(z)=1$ for all $|z|<1$. **(Hint: Let $e^{i t}=\zeta, d t=\frac{d \zeta}{i \zeta}$.)**
 
 
 
-> [!exercise] Exercise 8
+> [!exercise|5523af86-33a9-56eb-af50-5e39de85fb51.local at=68a60eb6-3000-524c-ad84-fa0f426ab251] Exercise 8
 > 22. Compute $\frac{1}{2 \pi} \int_{0}^{2 \pi} \frac{1}{2+e^{i t}} d t$. (See the hint in Exercise 21.)
 
 
 
-> [!exercise] Exercise 9
+> [!exercise|22ab10fb-5878-58f8-85a6-1e2356c673ba.local at=009af738-87b1-5e05-ad77-e0e46d765a25] Exercise 9
 > 23. Show that $\frac{1}{2 \pi} \int_{0}^{2 \pi} e^{e^{i n t}} d t=1$ for $n= \pm 1, \pm 2, \ldots$.
 > 24. Show that $\frac{1}{2 \pi} \int_{0}^{2 \pi} \cos \left(e^{i t}\right) d t=1$ and $\frac{1}{2 \pi} \int_{0}^{2 \pi} \sin \left(e^{i t}\right) d t=0$.
 
 
-> [!exercise] Exercise 10
+> [!exercise|92a65c52-178a-51e1-8c92-b7bde37f16ec.local at=87826973-6ea7-59d7-8e65-8b3e838672ff] Exercise 10
 > 25. Define $f(z)=\int_{0}^{1} \cos (z t) d t$. Explain why $f$ is entire and then find $f$.
 > 26. Define $f(z)=\int_{0}^{1} e^{z^{2} t} d t$. Explain why $f$ is entire and then find $f$.
 
 
 
-> [!exercise] Exercise 11
+> [!exercise|84a36d5f-a70c-551b-84b0-8cb856098ef1.local at=e5463122-a01e-558d-ac83-cd13da7d5b29] Exercise 11
 > 27. Define the following functions at $z=0$ in order that they become entire:
 > (a) $\frac{1-e^{z}}{2 z}$ and (b) $\frac{\cos z-1}{z^{2}}$. Justify your answers using Theorem 4.
 
 
 
-> [!exercise] Exercise 12
+> [!exercise|cf8b7a0e-e920-5c17-954a-3ec3b728b4c6.local at=50d207d7-9620-5164-9ccb-0e355ffe3e37] Exercise 12
 > 28. 
 > (a) Compute $\frac{1}{2 \pi i} \int_{C_{1}(0)} \frac{e^{z}}{z} d z$.
 > (b) Use your answer in (a) to show that $\int_{0}^{\pi} e^{\cos t} \cos (\sin t) d t=\pi$. **(Hint: Parametrize $C_{1}(0)$ by the interval $[-\pi, \pi]$.)**
@@ -530,11 +608,11 @@
 
 
 
-> [!exercise] Exercise 13
+> [!exercise|f897841b-3f89-5855-b8b7-81dbe26d8356.local at=42501d31-614e-5d33-806e-9c09cb8d0e89] Exercise 13
 > 29. Suppose that $f$ and $g$ are analytic inside and on a simple path $C$. Suppose that $f=g$ on $C$. Show that $f=g$ inside $C$.
 
 
-> [!exercise] Exercise 14
+> [!exercise|188230c0-04f4-5852-ad80-7b9be1eaadca.local at=85cd974f-518e-5bea-9626-7f7da2e4e1a1] Exercise 14
 > 30. Suppose that $f$ is analytic inside and on $C_{1}(0)$. For $|z|<1$, show that
 > 
 > $$
@@ -553,7 +631,7 @@
 
 
 
-> [!exercise] Exercise 15
+> [!exercise|ce5bf16e-a04d-5c8a-803f-a9b359f69f7e.local at=65ebfa55-caac-55c1-8908-413d58314e3b] Exercise 15
 > 32. Project Problem: Approximation of the derivative. (a) Suppose that $f$ is analytic on a region $\Omega$. Let $S_{R}\left(z_{0}\right)$ be a closed disk in $\Omega$. For $z$ in $S_{R}\left(z_{0}\right)$, show that
 > 
 > $$
@@ -578,7 +656,7 @@
 
 
 
-> [!exercise] Exercise 16
+> [!exercise|a17056e6-812b-5374-ae79-687755ee5f1e.local at=e4a02557-578a-5ce6-b90c-432b723e5e3d] Exercise 16
 > 33. Project Problem: Differentiation under the integral sign. Theorem 4, Section 3.5, is a very useful tool. We used it to prove Cauchy's theorem and many other results. In this exercise, we will offer a new proof based on Exercise 32. Even though this proof cannot replace the one that we presented in Section 3.5, since it is based on results that use differentiation under the integral sign, it does offer yet another justification based on Cauchy's formula.
 > (a) In the notation of Theorem 4, Section 3.5, fix $S_{R}\left(z_{0}\right)$ in $\Omega$ and take $M$ to be the maximum value of $|f(z, \zeta)|$ for $z$ in $S_{R}\left(z_{0}\right)$ and $\zeta$ on the graph of $\gamma$. Using Exercise 32, show that for $0<\left|z-z_{0}\right|<\frac{R}{2}$,
 > 
@@ -594,7 +672,7 @@
 
 
 
-> [!exercise] Exercise 17
+> [!exercise|e8c6f835-5387-5187-a550-5cc5bc9392d7.local at=1e97f7f8-076c-5aee-9013-086a337dab3d] Exercise 17
 > 34. **Project Problem:** Wallis's formulas. (a) If $n$ is an integer, recall or prove once more the useful identity
 > 
 > $$
@@ -618,7 +696,7 @@
 
 
 
-> [!exercise] Exercise 18
+> [!exercise|252068c2-7b04-51f8-8150-20d4d630a0ea.local at=2e518ad1-0438-54d7-8085-e71b22cedb7b] Exercise 18
 > 35. Show that for $k=0,1,2, \ldots$,
 > 
 > $$
@@ -630,7 +708,7 @@
 
 
 
-> [!exercise] Exercise 19
+> [!exercise|b52761ba-1a0c-57b2-b37e-0768279379bc.local at=df1f37a3-36ba-59ad-a3bb-7c3aac8b2e59] Exercise 19
 > 36. **Project Problem:** Logarithms of functions. Suppose that $f(z)$ is analytic and nonvanishing on a simply connected region $\Omega$. By a branch of the logarithm of $f(z)$ we mean any continuous function $g(z)$ on $\Omega$ satisfying $e^{g(z)}=f(z)$ for all $z$ in $\Omega$. Such a function will be denoted by $\log f(z)$.
 > (a) Prove that if $g$ exists, then $g$ is in fact analytic and $g^{\prime}(z)=\frac{f^{\prime}(z)}{f(z)}$. Thus $g$ is an antiderivative of $\frac{f^{\prime}(z)}{f(z)}$. **(Hint: Theorem 4, Section 2.3.)**
 > (b) Show that if $g(z)$ is an antiderivative of $\frac{f^{\prime}(z)}{f(z)}$, and if $e^{g\left(z_{0}\right)}=f\left(z_{0}\right)$ at a point in $\Omega$, then in fact $g(z)$ is a branch of the logarithm of $f(z)$. **(Hint: To show that $e^{g(z)}=f(z)$, let $h(z)=\frac{e^{g(z)}}{f(z)}$. Show that $h^{\prime}(z)=0$ for all $z$ in $\Omega$.)**
@@ -638,7 +716,7 @@
 
 
 
-> [!exercise] Exercise 20
+> [!exercise|f6b4caea-e462-5571-916e-94889335630b.local at=ac0e204d-5c7c-5cbd-a86a-706f61e65f09] Exercise 20
 > 37. A stronger Morera's theorem. Follow the outlined steps to show that in Morera's theorem it is sufficient to restrict the path $\gamma$ to triangular paths lying in arbitrarily small disks in $\Omega$.
 > (a) Argue that it is enough to show that $f$ has an analytic antiderivative in every disk $B_{R}\left(z_{0}\right)$ contained in $\Omega$.
 > (b) For $z$ in $B_{R}\left(z_{0}\right)$, define $F(z)=\int_{\left[z_{0}, z\right]} f(\zeta) d \zeta$. Use the fact that the integral of $f$ over a closed triangular path is 0 to show that $\frac{F(z+\Delta z)-F(z)}{\Delta z}=\frac{1}{\Delta z} \int_{[z, z+\Delta z]} f(\zeta) d \zeta$. (c) Use Lemma 1, Section 3.3, to compute the limit in (b) as $\Delta z \rightarrow 0$, and conclude that $F^{\prime}(z)=f(z)$, as desired.
@@ -646,7 +724,7 @@
 
 
 
-> [!exercise] Exercise 21
+> [!exercise|9dc6bce0-1abf-52a1-ac66-e7dad5a95c3b.local at=cfc14902-d273-50e6-a5fd-65254767325a] Exercise 21
 > 38. Cauchy's formula for multiply connected regions. Use Cauchy's integral theorem for multiply connected regions (Theorem 6, Section 3.4) to obtain the following version of Cauchy's formula.
 > 
 > Suppose that $f$ is analytic on a region $\Omega$ containing the region interior to the outer simple path $C$ and exterior to the inner simple paths $C_{j}$ 's $(j=1,2, \ldots, n)$, as well as the paths themselves. Suppose that the paths all share the same orientation (_Figure 10_). Let $z$ be any point interior to $C$ and exterior to all $C_{j}$. Then
@@ -663,18 +741,26 @@
 > 
 > 
 > 
-> > [!figure] Figure 10
-> > 
-> > ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-077_483_460_496_45.jpg)
-> > Figure 10
-> 
-> 
-> 
-
-
-
-
-> [!exercise] Exercise 22
+> ```scientific-figure
+> id: 30875ac7-8967-4c01-904c-6eea5da88bad
+> numbered: false
+> title: ""
+> caption: "**Figure 10.**"
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-077_483_460_496_45.jpg
+>     caption: ""
+> ```
+> 
+> 
+> 
+
+
+
+
+> [!exercise|9e0825ad-c9bd-5b81-a9d0-e7ca21e6cb42.local at=0461c78d-f163-576c-9249-8fe3ad3fce96] Exercise 22
 > 39. Suppose $f(z)$ is analytic in a region $\Omega$ and $C$ is a simple closed positively oriented curve in $\Omega$ with its terminal point (initial and final) at $\alpha$. Let $z_{0}$ be a point inside $C$.
 > (a) Use integration by parts to show that
 > 
@@ -696,7 +782,7 @@
 
 
 
-> [!exercise] Exercise 23
+> [!exercise|db3cb854-afe7-5b39-b51a-60298fea05f7.local at=8e4914c6-306b-5835-9fb1-c3b7cc89a94d] Exercise 23
 > 40. Project Problem: Factoring zeros of analytic functions. This exercise contains useful facts about zeros of analytic functions, which will be derived again in Chapter 4 using power series. We include them at this early stage as interesting applications of Theorem 4, and we use them to derive a useful version of l'Hospital's rule. Throughout this problem, $f$ is analytic at a point $z_{0}$.
 > (a) Suppose that $f\left(z_{0}\right)=0$, that is, $z_{0}$ is a zero of $f$. Use Theorem 4 to show that $f(z)=\left(z-z_{0}\right) g(z)$, where $g(z)$ is analytic at $z_{0}$.
 > (b) Recall the Leibniz product rule for differentiation: If $f$ and $g$ are differentiable functions, then
@@ -712,7 +798,7 @@
 
 
 
-> [!exercise] Exercise 24
+> [!exercise|e923e360-7fb4-5af2-bb13-e2d919e49ec4.local at=75eef62c-ac5e-5f42-ac51-e41c05541075] Exercise 24
 > 41. Generalized l'Hospital's rule. Suppose that $f$ and $g$ are analytic at $z_{0}$ such that $f\left(z_{0}\right)=f^{\prime}\left(z_{0}\right)=\cdots=f^{(m-1)}\left(z_{0}\right)=0$ and $g\left(z_{0}\right)=g^{\prime}\left(z_{0}\right)=\cdots= g^{(m-1)}\left(z_{0}\right)=0$, but $g^{(m)}\left(z_{0}\right) \neq 0$. Then $\lim _{z \rightarrow z_{0}} \frac{f(z)}{g(z)}=\frac{f^{(m)}\left(z_{0}\right)}{g^{(m)}\left(z_{0}\right)}$.
 > **(Hint: Use Exercise 40.)**
 > 42. Use the generalized l'Hospital's rule to compute $\lim _{z \rightarrow 0} \frac{e^{z}\left(\left(1+e^{z}\right) z-2 e^{z}+2\right)}{\left(e^{z}-1\right)^{3}}$.

`````
