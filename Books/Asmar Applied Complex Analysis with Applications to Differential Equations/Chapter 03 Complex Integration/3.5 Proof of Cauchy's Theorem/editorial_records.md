
# Editorial records

Reading note: 3.5 Proof of Cauchy's Theorem.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Callout 109: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Cauchy’s Integral Theorem in a Star-Shaped Region
> Suppose that $f$ is analytic on a star region $\Omega$. Then
>
> $$\int_{\Gamma} f(z) d z=0$$
>
> for all closed paths $\Gamma$ in $\Omega$.
````
### After

````text
> [!theorem] Cauchy's Integral Theorem for Star Regions
> Suppose that $f$ is analytic on a star region $\Omega$. Then
>
> $$\int_{\Gamma} f(z) d z=0$$
>
> for all closed paths $\Gamma$ in $\Omega$.
````

## 2. Callout 110: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Fubini's Theorem for Complex Path Integrals
> Suppose that $f(z, \zeta)$ is continuous for $z$ on a path $\gamma_{1}$ and $\zeta$ on a path $\gamma_{2}$. Then
>
> $$
> \int_{\gamma_{1}} \int_{\gamma_{2}} f(z, \zeta) d \zeta d z=\int_{\gamma_{2}} \int_{\gamma_{1}} f(z, \zeta) d z d \zeta
> $$
````
### After

````text
> [!theorem] Fubini's Theorem for Path Integrals
> Suppose that $f(z, \zeta)$ is continuous for $z$ on a path $\gamma_{1}$ and $\zeta$ on a path $\gamma_{2}$. Then
>
> $$
> \int_{\gamma_{1}} \int_{\gamma_{2}} f(z, \zeta) d \zeta d z=\int_{\gamma_{2}} \int_{\gamma_{1}} f(z, \zeta) d z d \zeta
> $$
````

## 3. Callout 111: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Continuity of Parameter-Dependent Complex Path Integrals
> Suppose that $f(z, \zeta)$ is continuous for $z$ in a region $\Omega$ and $\zeta$ on a path $\gamma$. For $z$ in $\Omega$, consider
>
> $$
> \phi(z)=\int_{\gamma} f(z, \zeta) d \zeta
> $$
>
> Then $\phi$ is a continuous function of $z$ in $\Omega$.
````
### After

````text
> [!theorem] Continuity of Path Integrals
> Suppose that $f(z, \zeta)$ is continuous for $z$ in a region $\Omega$ and $\zeta$ on a path $\gamma$. For $z$ in $\Omega$, consider
>
> $$
> \phi(z)=\int_{\gamma} f(z, \zeta) d \zeta
> $$
>
> Then $\phi$ is a continuous function of $z$ in $\Omega$.
````

## 4. Callout 112: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Differentiation Under a Complex Path Integral
> Suppose that $f(z, \zeta)$ is a complex-valued function, defined for $z$ in a region $\Omega$ and $\zeta$ on a path $\gamma$. If both $f(z, \zeta)$ and $\frac{d}{d z} f(z, \zeta)$ are continuous functions of $(z, \zeta)$ (hence, for fixed $\zeta, f(z, \zeta)$ is analytic in $z)$, then the function
>
> $$
> F(z)=\int_{\gamma} f(z, \zeta) d \zeta
> $$
>
> is analytic on $\Omega$ and
>
> $$
> F^{\prime}(z)=\int_{\gamma} \frac{d}{d z} f(z, \zeta) d \zeta
> $$
````
### After

````text
> [!theorem] Differentiation of Path Integrals
> Suppose that $f(z, \zeta)$ is a complex-valued function, defined for $z$ in a region $\Omega$ and $\zeta$ on a path $\gamma$. If both $f(z, \zeta)$ and $\frac{d}{d z} f(z, \zeta)$ are continuous functions of $(z, \zeta)$ (hence, for fixed $\zeta, f(z, \zeta)$ is analytic in $z)$, then the function
>
> $$
> F(z)=\int_{\gamma} f(z, \zeta) d \zeta
> $$
>
> is analytic on $\Omega$ and
>
> $$
> F^{\prime}(z)=\int_{\gamma} \frac{d}{d z} f(z, \zeta) d \zeta
> $$
````

## 5. Callout 113: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Continuity and Differentiation Under a Real-Parameter Integral
> (i) Let $u$ be a continuous complex-valued function on the rectangle $R=[a, b] \times [c, d]$. For $c \leq y \leq d$, define
>
> $$
> \phi(y)=\int_{a}^{b} u(x, y) d x
> $$
>
> Then $\phi(y)$ is continuous on $[c, d]$. 
>
> (ii) If $u$ is real-valued and continuous on $R$ and $\frac{\partial u}{\partial y}$ is also continuous on $R$, then $\phi(y)$ is differentiable on $(c, d)$ with
>
> $$
> \phi^{\prime}(y)=\frac{d}{d y} \int_{a}^{b} u(x, y) d x=\int_{a}^{b} \frac{\partial u}{\partial y}(x, y) d x \quad(c<y<d)
> $$
````
### After

````text
> [!theorem] Continuity and Differentiation of Integrals
> (i) Let $u$ be a continuous complex-valued function on the rectangle $R=[a, b] \times [c, d]$. For $c \leq y \leq d$, define
>
> $$
> \phi(y)=\int_{a}^{b} u(x, y) d x
> $$
>
> Then $\phi(y)$ is continuous on $[c, d]$. 
>
> (ii) If $u$ is real-valued and continuous on $R$ and $\frac{\partial u}{\partial y}$ is also continuous on $R$, then $\phi(y)$ is differentiable on $(c, d)$ with
>
> $$
> \phi^{\prime}(y)=\frac{d}{d y} \int_{a}^{b} u(x, y) d x=\int_{a}^{b} \frac{\partial u}{\partial y}(x, y) d x \quad(c<y<d)
> $$
````

## Source-to-current comparison

Source: /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 03 Complex Integration/3.5 Proof of Cauchy's Theorem.md

This exact comparison preserves the full change evidence, including formatting, OCR corrections, restored source wording, and required standalone context. The entries above explain the recovery edits. The comparison is not a claim that every difference is a correction; component serialization, callout wrapping, and printed labels outside callouts are formatting.

`````diff
--- /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 03 Complex Integration/3.5 Proof of Cauchy's Theorem.md
+++ /Users/gradyclopton/ObsidianVaults/complex_analysis/Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/3.5 Proof of Cauchy's Theorem.md
@@ -20,30 +20,47 @@
 A region $\Omega$ is called a star region if it contains a point $z_{0}$ such that any other point $z$ in $\Omega$ can be connected to $z_{0}$ by a line segment wholly contained in $\Omega$. Thus $\left[z_{0}, z\right]$ is contained in $\Omega$ for any $z$ in $\Omega$. _Figure 1_ depicts several examples of star regions along with suitable points to serve as $z_{0}$.
 
 
-> [!figure] Figure 1
-> 
-> ![700](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-058_528_1554_670_500.jpg)
-> Figure 1 Star regions.
+```scientific-figure
+id: 36c8e467-ab98-4433-9f6d-6d9c9cacf61c
+numbered: false
+title: ""
+caption: "**Figure 1.** Star regions."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-058_528_1554_670_500.jpg
+    caption: ""
+```
 
 The proof of Cauchy's theorem on star regions is a simple consequence of Theorem 2, Section 3.3, and a general result on differentiation of path integrals, which we state and prove at the end of the section.
 
 
 
 
+<!-- Source label: Cauchy's Integral Theorem for Star Regions -->
 > [!theorem] Cauchy's Integral Theorem for Star Regions
 > Suppose that $f$ is analytic on a star region $\Omega$. Then
-> 
+>
 > $$\int_{\Gamma} f(z) d z=0$$
-> 
+>
 > for all closed paths $\Gamma$ in $\Omega$.
 
 **Proof** According to Theorem 2, Section 3.3, it is enough to construct an antiderivative of $f$ in $\Omega$. Let $z_{0}$ be a point in $\Omega$ that connects to all other points in $\Omega$ via line segments (see _Figure 2_). 
 
 
-> [!figure] Figure 2
-> 
-> ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-058_503_533_1771_102.jpg)
-> Figure 2
+```scientific-figure
+id: a969465e-4df4-49ed-b212-f1b5f78a5b31
+numbered: false
+title: ""
+caption: "**Figure 2.**"
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-058_503_533_1771_102.jpg
+    caption: ""
+```
 
 
 
@@ -105,10 +122,18 @@
 For our next result, we define the notion of distance between two sets. If $K$ and $S$ are two nonempty sets, the distance between $K$ and $S$ is defined to be the smallest value of $|z-w|$ where $z$ is in $K$ and $w$ is in $S$ (_Figure 3_). 
 
 
-> [!figure] Figure 3
-> 
-> ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-060_504_529_446_80.jpg)
-> Figure 3 Distance between sets.
+```scientific-figure
+id: 90a7ad71-0e16-4cb4-a81f-7f7bf52b1204
+numbered: false
+title: ""
+caption: "**Figure 3.** Distance between sets."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-060_504_529_446_80.jpg
+    caption: ""
+```
 
 
 
@@ -138,10 +163,18 @@
 Having chosen $n$, construct a grid over $Q$ by subdividing the sides into $n$ equal subintervals (_Figure 4_). 
 
 
-> [!figure] Figure 4
-> 
-> ![700](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-061_699_1483_302_574.jpg)
-> Figure 4 A simplicial network on the square $Q$ with a sample smplicial square with one corner at $p_{32}$. The simplicial sques are so small that the imare of each is contained in a dive in $\Omega$ of radius $\delta>0$, where $\delta$ is the distance between thic boundary of $\Omega, \partial \Omega$, and the closed and bounded set $H[Q]$.
+```scientific-figure
+id: ba117d6f-ddcf-4e45-a87d-4e337b5b6b26
+numbered: false
+title: ""
+caption: "**Figure 4.** A simplicial network on the square $Q$ with a sample smplicial square with one corner at $p_{32}$. The simplicial sques are so small that the imare of each is contained in a dive in $\\Omega$ of radius $\\delta>0$, where $\\delta$ is the distance between thic boundary of $\\Omega, \\partial \\Omega$, and the closed and bounded set $H[Q]$."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-061_699_1483_302_574.jpg
+    caption: ""
+```
 
 
 
@@ -179,19 +212,35 @@
 
 
 
-> [!figure] Figure 5
-> 
-> ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-061_703_690_1624_550.jpg)
-> Figure 5
+```scientific-figure
+id: 97e84316-77fa-4bbf-beb7-5a38fa0cef92
+numbered: false
+title: ""
+caption: "**Figure 5.**"
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-061_703_690_1624_550.jpg
+    caption: ""
+```
 
 
 
 By construction, these polygonal paths are contained in disks of radius $\delta$ in ? In _Figure 6_, after summing all the path integrals and canceling those that are traversed ${ }^{\text {in }}$ opposite direction, the only ones that remain are those that correspond to the boundary of $Q$.
 
-> [!figure] Figure 6
-> 
-> ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-061_695_688_1624_1303.jpg)
-> Figure 6
+```scientific-figure
+id: f57d8f3b-abba-49ac-a607-304b73b9f5c7
+numbered: false
+title: ""
+caption: "**Figure 6.**"
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-061_695_688_1624_1303.jpg
+    caption: ""
+```
 
 Adding the integrals over all the $\sigma_{j k}$ 's, we note the following. The integrals over the segments that correspond to internal sides of the simplicial squares cancel, since each internal segment is traversed twice in opposite directions. Thus the only noncanceling integrals are those over line segments that correspond to external sides of the simplicial squares, that is, the boundary of $Q$.
 
@@ -266,14 +315,13 @@
 
 
 
-> [!theorem] Theorem 2: Fubini's Theorem for Path Integrals
+<!-- Source label: Theorem 2: Fubini's Theorem for Path Integrals -->
+> [!theorem] Fubini's Theorem for Path Integrals
 > Suppose that $f(z, \zeta)$ is continuous for $z$ on a path $\gamma_{1}$ and $\zeta$ on a path $\gamma_{2}$. Then
-> 
+>
 > $$
 > \int_{\gamma_{1}} \int_{\gamma_{2}} f(z, \zeta) d \zeta d z=\int_{\gamma_{2}} \int_{\gamma_{1}} f(z, \zeta) d z d \zeta
 > $$
-> 
-> 
 
 **Proof** Parametrize $\gamma_{1}$ by $[a, b]$ and $\gamma_{2}$ by $[c, d]$. Then (11) is equivalent to
 
@@ -289,13 +337,14 @@
 
 
 
-> [!theorem] Theorem 3: Continuity of Path Integrals
+<!-- Source label: Theorem 3: Continuity of Path Integrals -->
+> [!theorem] Continuity of Path Integrals
 > Suppose that $f(z, \zeta)$ is continuous for $z$ in a region $\Omega$ and $\zeta$ on a path $\gamma$. For $z$ in $\Omega$, consider
-> 
+>
 > $$
 > \phi(z)=\int_{\gamma} f(z, \zeta) d \zeta
 > $$
-> 
+>
 > Then $\phi$ is a continuous function of $z$ in $\Omega$.
 
 
@@ -312,27 +361,35 @@
 
 
 
-> [!figure] Figure 7
-> 
-> ![700](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-064_531_1075_189_803.jpg)
-> Figure 7 Picturing a continuous function $f$ of two variables $z$ and $\zeta$.
+```scientific-figure
+id: 3ee5a502-a571-46de-a682-5a7436dc9f2b
+numbered: false
+title: ""
+caption: "**Figure 7.** Picturing a continuous function $f$ of two variables $z$ and $\\zeta$."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-064_531_1075_189_803.jpg
+    caption: ""
+```
 
 
 We are now ready to state and prove a general result that justifies differentiation under the integral sign for path integrals.
 
-> [!theorem] Theorem 4: Differentiation of Path Integrals
+<!-- Source label: Theorem 4: Differentiation of Path Integrals -->
+> [!theorem] Differentiation of Path Integrals
 > Suppose that $f(z, \zeta)$ is a complex-valued function, defined for $z$ in a region $\Omega$ and $\zeta$ on a path $\gamma$. If both $f(z, \zeta)$ and $\frac{d}{d z} f(z, \zeta)$ are continuous functions of $(z, \zeta)$ (hence, for fixed $\zeta, f(z, \zeta)$ is analytic in $z)$, then the function
-> 
+>
 > $$
 > F(z)=\int_{\gamma} f(z, \zeta) d \zeta
 > $$
-> 
+>
 > is analytic on $\Omega$ and
-> 
+>
 > $$
 > F^{\prime}(z)=\int_{\gamma} \frac{d}{d z} f(z, \zeta) d \zeta
 > $$
-> 
 
 **Proof** Let $z_{0}$ be in $\Omega$ and $\Delta z$ be so small that $z_{0}+\Delta z$ is also in $\Omega$. To compute $F^{\prime}\left(z_{0}\right)$, we must find the limit as $\Delta z \rightarrow 0$ of
 
@@ -382,30 +439,34 @@
 
 
 
-> [!theorem] Theorem 5: Continuity and Differentiation of Integrals
+<!-- Source label: Theorem 5: Continuity and Differentiation of Integrals -->
+> [!theorem] Continuity and Differentiation of Integrals
 > (i) Let $u$ be a continuous complex-valued function on the rectangle $R=[a, b] \times [c, d]$. For $c \leq y \leq d$, define
-> 
+>
 > $$
 > \phi(y)=\int_{a}^{b} u(x, y) d x
 > $$
-> 
-> Then $\phi(y)$ is continuous on $[c, d]$ (_Figure 8_). 
-> 
-> 
-> > [!figure] Figure 8
-> > 
-> > ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-065_459_524_1001_52.jpg)
-> > Figure 8 Visualizing the continuity of $\phi(y)$, when $u$ is real and $\geq 0$. For a given $y, \phi(y)$ is the area of the cross section above the $x y$-plane, under the surface $z=u(x, y)$, $a \leq x \leq b$. To say that $\phi$ is continuous at $y_{0}$ means that the area $\phi(y)$ tends to the area $\phi\left(y_{0}\right)$ as $y \rightarrow y_{0}$.
-> 
-> 
-> 
+>
+> Then $\phi(y)$ is continuous on $[c, d]$. 
+>
 > (ii) If $u$ is real-valued and continuous on $R$ and $\frac{\partial u}{\partial y}$ is also continuous on $R$, then $\phi(y)$ is differentiable on $(c, d)$ with
-> 
+>
 > $$
 > \phi^{\prime}(y)=\frac{d}{d y} \int_{a}^{b} u(x, y) d x=\int_{a}^{b} \frac{\partial u}{\partial y}(x, y) d x \quad(c<y<d)
 > $$
-> 
-> 
+
+```scientific-figure
+id: 01a6928c-c6c1-464d-9b3f-72b3d076504e
+numbered: false
+title: ""
+caption: "**Figure 8.** Visualizing the continuity of $\\phi(y)$, when $u$ is real and $\\geq 0$. For a given $y, \\phi(y)$ is the area of the cross section above the $x y$-plane, under the surface $z=u(x, y)$, $a \\leq x \\leq b$. To say that $\\phi$ is continuous at $y_{0}$ means that the area $\\phi(y)$ tends to the area $\\phi\\left(y_{0}\\right)$ as $y \\rightarrow y_{0}$."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-065_459_524_1001_52.jpg
+    caption: ""
+```
 
 
 
@@ -478,10 +539,18 @@
 > $$
 > 
 > 
-> > [!figure] Figure 9
-> > 
-> > ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-066_464_523_1284_97.jpg)
-> > Figure 9
+> ```scientific-figure
+> id: ba8e3b97-e906-46af-8378-ac3b96600818
+> numbered: false
+> title: ""
+> caption: "**Figure 9.**"
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-066_464_523_1284_97.jpg
+>     caption: ""
+> ```
 > 
 > 
 > (a) Write $F=U+i V$. Using (18), show that

`````
