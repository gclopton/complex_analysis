
# Editorial records

Reading note: 3.4 Cauchy's Integral Theorem.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Callout 99: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Straight-Line Homotopies in Convex Plane Regions
> Let $\Omega\subset\mathbb{C}$ be a convex region and let $\gamma_0,\gamma_1:[0,1]\to\Omega$ be paths. The straight-line homotopy
>
> $$
> H(t,s)=(1-s)\gamma_0(t)+s\gamma_1(t),\qquad 0\le t,s\le1,
> $$
>
> stays in $\Omega$. If the paths have the same endpoints, this homotopy fixes those endpoints. If both paths are closed, every intermediate path is closed. In particular, taking $\gamma_1(t)=z_1$ for a fixed $z_1\in\Omega$ contracts any closed path to a point.
````
### After

````text
> [!theorem] Deformation of Paths in Convex Sets
> Suppose that $\Omega$ is a convex region. (i) Any two paths $\gamma_{0}$ and $\gamma_{1}$ in $\Omega$, joining two points $\alpha$ and $\beta$ in $\Omega$, are mutually continuously deformable relative to $\Omega$. The continuous mapping $H$ that deforms $\gamma_{0}$ into $\gamma_{1}$ is given by $H(t,s)=(1-s)\gamma_0(t)+s\gamma_1(t)$, $0\le t,s\le1$.
> (ii) Any two closed paths $\gamma_{0}$ and $\gamma_{1}$ in $\Omega$ are mutually continuously deformable relative to $\Omega$. The continuous mapping $H$ that deforms $\gamma_{0}$ into $\gamma_{1}$ is given by $H(t,s)=(1-s)\gamma_0(t)+s\gamma_1(t)$, $0\le t,s\le1$.
> (iii) Any closed path $\gamma_{0}$ in $\Omega$ is continuously deformable into a point in $\Omega$. The continuous mapping $H$ that deforms a closed path $\gamma_{0}$ into a point $z_{1}$ in $\Omega$ is given by $H(t,s)=(1-s)\gamma_0(t)+s\gamma_1(t)$, $0\le t,s\le1$, where $\gamma_{1}(t)=z_{1}$ is constant for all $t$ in $[0,1]$.
````

## 2. Callout 100: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Cauchy’s Integral Theorem for Homotopic Paths
> Let $f$ be a function analytic in a region $\Omega$. (i) If $\gamma_{0}$ and $\gamma_{1}$ are two paths joining $\alpha$ to $\beta$ in $\Omega$, and if $\gamma_{0}$ is continuously deformable into $\gamma_{1}$ relative to $\Omega$, then
>
> $$
> \int_{\gamma_{0}} f(z) d z=\int_{\gamma_{1}} f(z) d z
> $$
>
> (ii) If $\gamma_{0}$ and $\gamma_{1}$ are closed paths in $\Omega$ and $\gamma_{0}$ is continuously deformable into $\gamma_{1}$ relative to $\Omega$, then
>
> $$
> \int_{\gamma_{0}} f(z) d z=\int_{\gamma_{1}} f(z) d z
> $$
>
> In particular, if $\gamma_{0}$ is a closed path in $\Omega$ that is continuously deformable into a point in $\Omega$, then
>
> $$
> \int_{\gamma_{0}} f(z) d z=0
> $$
````
### After

````text
> [!theorem] Cauchy's Integral Theorem for Deformable Paths
> Let $f$ be a function analytic in a region $\Omega$. (i) If $\gamma_{0}$ and $\gamma_{1}$ are two paths joining $\alpha$ to $\beta$ in $\Omega$, and if $\gamma_{0}$ is continuously deformable into $\gamma_{1}$ relative to $\Omega$, then
>
> $$
> \int_{\gamma_{0}} f(z) d z=\int_{\gamma_{1}} f(z) d z
> $$
>
> (ii) If $\gamma_{0}$ and $\gamma_{1}$ are closed paths in $\Omega$ and $\gamma_{0}$ is continuously deformable into $\gamma_{1}$ relative to $\Omega$, then
>
> $$
> \int_{\gamma_{0}} f(z) d z=\int_{\gamma_{1}} f(z) d z
> $$
>
> In particular, if $\gamma_{0}$ is a closed path in $\Omega$ that is continuously deformable into a point in $\Omega$, then
>
> $$
> \int_{\gamma_{0}} f(z) d z=0
> $$
````

## 3. Callout 101: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!corollary] Vanishing Closed-Path Integrals of Functions Analytic on a Disk
> Suppose that $\gamma$ is a closed path and $f$ is analytic on an open disk containing $\gamma$. Then
>
> $$
> \int_{\gamma} f(z) d z=0
> $$
>
> In particular, if $f$ is entire then the displayed integral is zero for any closed path $\gamma$.
````
### After

````text
> [!corollary] Path Integrals of Functions Analytic on Disks
> Suppose that $\gamma$ is a closed path and $f$ is analytic on an open disk containing $\gamma$. Then
>
> $$
> \int_{\gamma} f(z) d z=0
> $$
>
> In particular, if $f$ is entire then the displayed integral is zero for any closed path $\gamma$.
````

## 4. Callout 103: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!definition] Simply Connected and Multiply Connected Plane Regions
> A region $\Omega$ is called **simply connected** if, for every pair $\alpha,\beta\in\Omega$, all paths joining $\alpha$ to $\beta$ in $\Omega$ are mutually continuously deformable relative to $\Omega$. If a region is not simply connected, then it is called **multiply connected**.
````
### After

````text
> [!definition] Simply Connected Region, Multiply Connected Region
> A region $\Omega$ is called **simply connected** if, for every pair $\alpha,\beta\in\Omega$, all paths joining $\alpha$ to $\beta$ in $\Omega$ are mutually continuously deformable relative to $\Omega$. If a region is not simply connected, then it is called **multiply connected**.
````

## 5. Callout 104: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Cauchy’s Integral Theorem in a Simply Connected Region
> Suppose that $\Omega$ is a simply connected region and that $f$ is analytic in $\Omega$. (i) If $\gamma_{0}$ and $\gamma_{1}$ are two paths joining $\alpha$ to $\beta$ in $\Omega$, then
>
> $$
> \int_{\gamma_{0}} f(z) d z=\int_{\gamma_{1}} f(z) d z
> $$
>
> (ii) If $\gamma$ is a closed path in $\Omega$, then
>
> $$
> \int_{\gamma} f(z) d z=0
> $$
````
### After

````text
> [!theorem] Cauchy's Theorem for Simply Connected Regions
> Suppose that $\Omega$ is a simply connected region and that $f$ is analytic in $\Omega$. (i) If $\gamma_{0}$ and $\gamma_{1}$ are two paths joining $\alpha$ to $\beta$ in $\Omega$, then
>
> $$
> \int_{\gamma_{0}} f(z) d z=\int_{\gamma_{1}} f(z) d z
> $$
>
> (ii) If $\gamma$ is a closed path in $\Omega$, then
>
> $$
> \int_{\gamma} f(z) d z=0
> $$
````

## 6. Callout 105: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Analytic Antiderivatives in a Simply Connected Region
> Suppose that $\Omega$ is a simply connected region and that $f$ is analytic in $\Omega$. Then there is an analytic function $F$ in $\Omega$ such that $F^{\prime}=f$. In other words, every analytic function in $\Omega$ has an antiderivative in $\Omega$. Up to an arbitrary additive constant, we have
>
> $$
> F(z)=\int_{z_{0}}^{z} f(\zeta) d \zeta
> $$
>
> where $z_{0}$ is a fixed point in $\Omega$ and the integral is taken over any path in $\Omega$ joining $z_{0}$ to $z$.
````
### After

````text
> [!theorem] Existence of Antiderivatives
> Suppose that $\Omega$ is a simply connected region and that $f$ is analytic in $\Omega$. Then there is an analytic function $F$ in $\Omega$ such that $F^{\prime}=f$. In other words, every analytic function in $\Omega$ has an antiderivative in $\Omega$. Up to an arbitrary additive constant, we have
>
> $$
> F(z)=\int_{z_{0}}^{z} f(\zeta) d \zeta
> $$
>
> where $z_{0}$ is a fixed point in $\Omega$ and the integral is taken over any path in $\Omega$ joining $z_{0}$ to $z$.
````

## 7. Callout 106: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!definition] Simple Closed Path in the Complex Plane
> A closed path $\gamma$ is called simple or a simple curve if $\gamma$ intersects itself only at the endpoints. That is, if $\gamma(t), a \leq t \leq b$, is a parametrization of $\gamma$, and $a \leq t_{1}<t_{2} \leq b$, then $\gamma\left(t_{1}\right)=\gamma\left(t_{2}\right) \Leftrightarrow t_{1}=a$ and $t_{2}=b$.
````
### After

````text
> [!definition] Simple Path
> A closed path $\gamma$ is called simple or a simple curve if $\gamma$ intersects itself only at the endpoints. That is, if $\gamma(t), a \leq t \leq b$, is a parametrization of $\gamma$, and $a \leq t_{1}<t_{2} \leq b$, then $\gamma\left(t_{1}\right)=\gamma\left(t_{2}\right) \Leftrightarrow t_{1}=a$ and $t_{2}=b$.
````

## 8. Callout 107: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Cauchy’s Integral Theorem inside a Simple Closed Path
> Suppose that $f$ is analytic on a simple closed path $C$ and its interior.
> (i) We have
>
> $$
> \int_{C} f(z) d z=0
> $$
>
> (ii) If $\gamma$ is a closed path (not necessarily simple) contained in the interior of $C$, then
>
> $$
> \int_{\gamma} f(z) d z=0
> $$
````
### After

````text
> [!theorem] Cauchy's Theorem for Simple Paths
> Suppose that $f$ is analytic on a simple closed path $C$ and its interior.
> (i) We have
>
> $$
> \int_{C} f(z) d z=0
> $$
>
> (ii) If $\gamma$ is a closed path (not necessarily simple) contained in the interior of $C$, then
>
> $$
> \int_{\gamma} f(z) d z=0
> $$
````

## 9. Callout 108: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Cauchy’s Integral Theorem for a Region with Multiple Boundary Curves
> Let $C,C_1,\ldots,C_n$ be positively oriented simple closed paths. Suppose the $C_j$ lie inside $C$, their interiors are pairwise disjoint, and their boundaries are disjoint from one another and from $C$. If $f$ is analytic on an open set containing the boundaries and the closed region inside $C$ and outside all the $C_j$, then
>
> $$
> \int_C f(z)\,dz=\sum_{j=1}^n\int_{C_j}f(z)\,dz.
> $$
````
### After

````text
> [!theorem] Cauchy's Theorem for Multiply Connected Regions
> Suppose that $f$ is analytic on a region $\Omega$ with simple paths $C$ and $C_{j}(j= 1,2, \ldots, n)$ positively oriented and contained in $\Omega$, where the $C_j$ are inside $C$ with pairwise disjoint interiors and boundaries, and the closed region inside $C$ and outside the $C_j$ is contained in $\Omega$. Then
>
> $$
> \int_{C} f(z) d z=\sum_{j=1}^{n} \int_{C_{j}} f(z) d z
> $$
````

## Source-to-current comparison

Source: /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 03 Complex Integration/3.4 Cauchy's Integral Theorem.md

This exact comparison preserves the full change evidence, including formatting, OCR corrections, restored source wording, and required standalone context. The entries above explain the recovery edits. The comparison is not a claim that every difference is a correction; component serialization, callout wrapping, and printed labels outside callouts are formatting.

`````diff
--- /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 03 Complex Integration/3.4 Cauchy's Integral Theorem.md
+++ /Users/gradyclopton/ObsidianVaults/complex_analysis/Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/3.4 Cauchy's Integral Theorem.md
@@ -23,29 +23,53 @@
 - Suppose that $\alpha$ and $\beta$ are points in a region $\Omega$, and $\gamma_{0}$ and $\gamma_{1}$ are paths in $\Omega$ joining $\alpha$ to $\beta$. We say that $\gamma_{0}$ is **continuously deformable into $\gamma_{1}$ relative to $\Omega$** if we can continuously move $\gamma_{0}$ over $\gamma_{1}$ while keeping the ends fixed at $\alpha$ and $\beta$ and without leaving $\Omega$ (_Figure 1_).
 
 
-> [!figure] Figure 1
-> 
-> ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-038_473_515_183_71.jpg)
-> Figure 1 Continuous deformation of $\gamma_{0}$ into $\gamma_{1}$.
+```scientific-figure
+id: e3992d37-f909-4712-9ffa-3a861f6c4062
+numbered: false
+title: ""
+caption: "**Figure 1.** Continuous deformation of $\\gamma_{0}$ into $\\gamma_{1}$."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-038_473_515_183_71.jpg
+    caption: ""
+```
 
 
 - If $\gamma_{0}$ and $\gamma_{1}$ are two closed paths in a region $\Omega$, we say that $\gamma_{0}$ is **continuously deformable into $\gamma_{1}$ relative to $\Omega$** if we can continuously move $\gamma_{0}$ without leaving $\Omega$, in such a way that it overlaps with $\gamma_{1}$ in position and direction (_Figure 2_).
 
 
-> [!figure] Figure 2
-> 
-> ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-038_471_519_766_81.jpg)
-> Figure 2 Continuous deformation of $\gamma_{0}$ into $\gamma_{1}$.
+```scientific-figure
+id: 28420516-8df1-49e5-9a6c-f9dcedf63862
+numbered: false
+title: ""
+caption: "**Figure 2.** Continuous deformation of $\\gamma_{0}$ into $\\gamma_{1}$."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-038_471_519_766_81.jpg
+    caption: ""
+```
 
 
 
 - If $\gamma_{0}$ is a closed path in a region $\Omega$, we say that $\gamma_{0}$ is **continuously deformable into a point relative to $\Omega$** if we can continuously shrink $\gamma_{0}$ into a point $z_{0}$ in $\Omega$ without leaving $\Omega$ (_Figure 3_). This is the same as the deformation of the closed path $\gamma_{0}$ into the closed path $\gamma_{1}$ where $\gamma_{1}$ is degenerated into a point. That is, $\gamma_{1}(t)$ is constant for all $t$.
 
 
-> [!figure] Figure 3
-> 
-> ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-038_475_525_1370_87.jpg)
-> Figure 3 Continuous deformation of $\gamma_{0}$ into a point $z_{0}$.
+```scientific-figure
+id: 01c20df0-37d8-4806-bb6e-f1bb6ca91c2c
+numbered: false
+title: ""
+caption: "**Figure 3.** Continuous deformation of $\\gamma_{0}$ into a point $z_{0}$."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-038_475_525_1370_87.jpg
+    caption: ""
+```
 
 
 It is intuitively clear that if we can continuously deform $\gamma_{0}$ into $\gamma_{1}$ in $\Omega$, then we can continuously deform $\gamma_{1}$ into $\gamma_{0}$ in $\Omega$. Hence, we will refer to the paths $\gamma_{0}$ and $\gamma_{1}$ as **mutually deformable in $\Omega$**.
@@ -77,53 +101,101 @@
 (a) Let $\Omega$ be the complex plane. In _Figure 4_, the upper semi-circle $\gamma_{0}(t)=e^{i t}, 0 \leq t \leq \pi$, is continuously deformable into the directed line segment joining 1 to -1 .
 
 
-> [!figure] Figure 4
-> 
-> ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-039_498_533_225_212.jpg)
-> Figure 4
+```scientific-figure
+id: 3f7d6e86-92a7-4d93-b026-6c96af7d7e94
+numbered: false
+title: ""
+caption: "**Figure 4.**"
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-039_498_533_225_212.jpg
+    caption: ""
+```
 
 
 (b) In the open unit disk $B_{1}(0)$, the path $\left[z_{1}, z_{2}, z_{3}\right]$ is continuously deformable into the directed line segment $\left[z_{1}, z_{3}\right]$ (_Figure 5_).
 
 
-> [!figure] Figure 5
-> 
-> ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-039_494_539_237_818.jpg)
-> Figure 5
+```scientific-figure
+id: 3a98dc90-4261-4eec-ba97-900e82d5a124
+numbered: false
+title: ""
+caption: "**Figure 5.**"
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-039_494_539_237_818.jpg
+    caption: ""
+```
 
 
 (c) In the open unit disk $B_{1}(0)$, the arc $\gamma_{0}$ is continuously deformable into the triangular path $\left[z_{1}, z_{2}, z_{3}\right]$ (_Figure 6_).
 
 
-> [!figure] Figure 6
-> 
-> ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-039_496_545_233_1428.jpg)
-> Figure 6
+```scientific-figure
+id: c17a7c34-143d-4eac-b16b-f880629cc3e4
+numbered: false
+title: ""
+caption: "**Figure 6.**"
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-039_496_545_233_1428.jpg
+    caption: ""
+```
 
 
 (d) In the annular region $\Omega$ in _Figure 7_, the circle $\gamma_{0}$ is continuously deformable into the circle $\gamma_{1}$ relative to $\Omega$.
 
-> [!figure] Figure 7
-> 
-> ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-039_488_531_820_204.jpg)
-> Figure 7
+```scientific-figure
+id: c6f27d60-8c34-4097-9946-1c1ccd1f3f93
+numbered: false
+title: ""
+caption: "**Figure 7.**"
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-039_488_531_820_204.jpg
+    caption: ""
+```
 
 (e) In the region $\Omega$ in _Figure 8_, the ellipse $\gamma_{0}$ is continuously deformable into a point relative to $\Omega$.
 
 
-> [!figure] Figure 8
-> 
-> ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-039_486_535_822_810.jpg)
-> Figure 8
+```scientific-figure
+id: 6f0afe98-a9e3-409a-b60a-370d014f0424
+numbered: false
+title: ""
+caption: "**Figure 8.**"
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-039_486_535_822_810.jpg
+    caption: ""
+```
 
 
 (f) In _Figure 9_, the region $\Omega$ consists of a disk minus the points $z_{1}, z_{2}, z_{3}$. In $\Omega$ the circle $\gamma_{0}$ is continuously deformable into the curve $\gamma_{1}$ consisting of three circles centered at $z_{1}, z_{2}, z_{3}$, and connected by line segments traversed in both directions, as shown in _Figure 9_.
 
 
-> [!figure] Figure 9
-> 
-> ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-039_486_542_822_1419.jpg)
-> Figure 9
+```scientific-figure
+id: a187e385-ded9-4b98-a243-93f83c5152ff
+numbered: false
+title: ""
+caption: "**Figure 9.**"
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-039_486_542_822_1419.jpg
+    caption: ""
+```
 
 
 
@@ -137,19 +209,35 @@
 
 
 
-> [!figure] Figure 10
-> 
-> ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-039_494_537_1690_630.jpg)
-> Figure 10
+```scientific-figure
+id: 17ed678f-3f64-431a-92fe-be8b5646b760
+numbered: false
+title: ""
+caption: "**Figure 10.**"
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-039_494_537_1690_630.jpg
+    caption: ""
+```
 
 
 To see how important it is to be precise about the region $\Omega$ when talking about deformation of paths, consider the situation depicted in _Figures 10 and 11_. 
 
 
-> [!figure] Figure 11
-> 
-> ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-039_490_544_1690_1411.jpg)
-> Figure 11
+```scientific-figure
+id: 6ec92b30-0e70-4ddc-b5ad-511f601d626a
+numbered: false
+title: ""
+caption: "**Figure 11.**"
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-039_490_544_1690_1411.jpg
+    caption: ""
+```
 
 
 The upper and lower semi-circles joining the points -1 to 1 in _Figure 10_ are mutually deformable in the disk of radius 2 but are not mutually
@@ -191,10 +279,18 @@
 To understand this definition, consider _Figure 12_. 
 
 
-> [!figure] Figure 12
-> 
-> ![500](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-040_381_790_1155_903.jpg)
-> Figure 12 The path $\gamma_{0}$ is continuously deformed into $\gamma_{1}$ relative to $\Omega$ if we can find a continuous mapping $H$ of the square $Q$ into $\Omega$, such that $H$ maps the lower side of $Q$ onto $\gamma_{0}$, its upper side onto $\gamma_{1}$, its left side onto the point $\alpha$, and its right side onto the point $\beta$. As a result, the horizontal line segments in $Q$ will be mapped to curves varying continuously between $\gamma_{0}$ and $\gamma_{1}$, while staying entirely in $\Omega$. 
+```scientific-figure
+id: 7b94d8bb-b3bf-47b7-bb34-efb4de6262df
+numbered: false
+title: ""
+caption: "**Figure 12.** The path $\\gamma_{0}$ is continuously deformed into $\\gamma_{1}$ relative to $\\Omega$ if we can find a continuous mapping $H$ of the square $Q$ into $\\Omega$, such that $H$ maps the lower side of $Q$ onto $\\gamma_{0}$, its upper side onto $\\gamma_{1}$, its left side onto the point $\\alpha$, and its right side onto the point $\\beta$. As a result, the horizontal line segments in $Q$ will be mapped to curves varying continuously between $\\gamma_{0}$ and $\\gamma_{1}$, while staying entirely in $\\Omega$."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-040_381_790_1155_903.jpg
+    caption: ""
+```
 
 
 
@@ -208,10 +304,18 @@
 
 This condition states that the initial point $H(0, s)$ and the terminal point $H(1, s)$ are the same. Thus the images of all horizontal sections of the square $Q$ are closed curves (_Figure 13_).
 
-> [!figure] Figure 13
-> 
-> ![500](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-041_396_820_315_37.jpg)
-> Figure 13 Deformation of closed paths.
+```scientific-figure
+id: 5e50c022-786b-4a1a-afa5-ca4156f25772
+numbered: false
+title: ""
+caption: "**Figure 13.** Deformation of closed paths."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-041_396_820_315_37.jpg
+    caption: ""
+```
 
 
 
@@ -219,10 +323,18 @@
 
 
 
-> [!figure] Figure 14
-> 
-> ![500](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-041_377_823_334_1069.jpg)
-> Figure 14 Deformation to one point.
+```scientific-figure
+id: 310f231f-1b6d-4311-8d9c-b58a48843811
+numbered: false
+title: ""
+caption: "**Figure 14.** Deformation to one point."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-041_377_823_334_1069.jpg
+    caption: ""
+```
 
 
 
@@ -248,10 +360,18 @@
 
 
 
-> [!figure] Figure 15
-> 
-> ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-041_472_524_1771_37.jpg)
-> Figure 15
+```scientific-figure
+id: 2eee0b16-45cf-4e24-9018-93bccf4e138f
+numbered: false
+title: ""
+caption: "**Figure 15.**"
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-041_472_524_1771_37.jpg
+    caption: ""
+```
 
 
 
@@ -304,10 +424,18 @@
 
 
 
-> [!figure] Figure 16
-> 
-> ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-042_507_835_677_886.jpg)
-> Figure 16 How the continuous deformation mapping $H$ works: $H$ maps the lower side of $Q$ onto the inner circle $C_{1}(0)$, the upper side onto $C_{2}(0)$, and all the in between horizontal segments in $Q$ are mapped to in between circles $C_{R}(0)$, where $1<R<2$.
+```scientific-figure
+id: 172826c8-cb5a-4416-a346-e731f11bff3e
+numbered: false
+title: ""
+caption: "**Figure 16.** How the continuous deformation mapping $H$ works: $H$ maps the lower side of $Q$ onto the inner circle $C_{1}(0)$, the upper side onto $C_{2}(0)$, and all the in between horizontal segments in $Q$ are mapped to in between circles $C_{R}(0)$, where $1<R<2$."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-042_507_835_677_886.jpg
+    caption: ""
+```
 
 
 
@@ -326,10 +454,18 @@
 are also in $S$. The complex plane is a convex set. Any disk is a convex set. Any rectangle is convex (_Figure 17_). 
 
 
-> [!figure] Figure 17
-> 
-> ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-042_415_522_2039_348.jpg)
-> Figure 17
+```scientific-figure
+id: 1b47316c-bcbb-4fb0-9f7d-43dd9a31ac77
+numbered: false
+title: ""
+caption: "**Figure 17.**"
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-042_415_522_2039_348.jpg
+    caption: ""
+```
 
 
 
@@ -337,20 +473,36 @@
 
 
 
-> [!figure] Figure 18
-> 
-> ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-042_465_489_1974_944.jpg)
-> Figure 18
+```scientific-figure
+id: d480ea9b-9fa2-432c-9d9a-c1146fb398c3
+numbered: false
+title: ""
+caption: "**Figure 18.**"
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-042_465_489_1974_944.jpg
+    caption: ""
+```
 
 
 
 The punctured disk in _Figure 19_ is not convex for the same reason.
 
 
-> [!figure] Figure 19
-> 
-> ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-042_489_522_1942_1504.jpg)
-> Figure 19
+```scientific-figure
+id: 5cb4adf7-7c3a-4528-b9a5-99843d2e25b2
+numbered: false
+title: ""
+caption: "**Figure 19.**"
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-042_489_522_1942_1504.jpg
+    caption: ""
+```
 
 
 
@@ -367,10 +519,11 @@
 
 
 
-> [!theorem] Theorem 1: Deformation of Paths in Convex Sets
-> Suppose that $\Omega$ is a convex region. (i) Any two paths $\gamma_{0}$ and $\gamma_{1}$ in $\Omega$, joining two points $\alpha$ and $\beta$ in $\Omega$, are mutually continuously deformable relative to $\Omega$. The continuous mapping $H$ that deforms $\gamma_{0}$ into $\gamma_{1}$ is given by (8).
-> (ii) Any two closed paths $\gamma_{0}$ and $\gamma_{1}$ in $\Omega$ are mutually continuously deformable relative to $\Omega$. The continuous mapping $H$ that deforms $\gamma_{0}$ into $\gamma_{1}$ is given by (8).
-> (iii) Any closed path $\gamma_{0}$ in $\Omega$ is continuously deformable into a point in $\Omega$. The continuous mapping $H$ that deforms a closed path $\gamma_{0}$ into a point $z_{1}$ in $\Omega$ is given by (8), where $\gamma_{1}(t)=z_{1}$ is constant for all $t$ in $[0,1]$.
+<!-- Source label: Theorem 1: Deformation of Paths in Convex Sets -->
+> [!theorem] Deformation of Paths in Convex Sets
+> Suppose that $\Omega$ is a convex region. (i) Any two paths $\gamma_{0}$ and $\gamma_{1}$ in $\Omega$, joining two points $\alpha$ and $\beta$ in $\Omega$, are mutually continuously deformable relative to $\Omega$. The continuous mapping $H$ that deforms $\gamma_{0}$ into $\gamma_{1}$ is given by $H(t,s)=(1-s)\gamma_0(t)+s\gamma_1(t)$, $0\le t,s\le1$.
+> (ii) Any two closed paths $\gamma_{0}$ and $\gamma_{1}$ in $\Omega$ are mutually continuously deformable relative to $\Omega$. The continuous mapping $H$ that deforms $\gamma_{0}$ into $\gamma_{1}$ is given by $H(t,s)=(1-s)\gamma_0(t)+s\gamma_1(t)$, $0\le t,s\le1$.
+> (iii) Any closed path $\gamma_{0}$ in $\Omega$ is continuously deformable into a point in $\Omega$. The continuous mapping $H$ that deforms a closed path $\gamma_{0}$ into a point $z_{1}$ in $\Omega$ is given by $H(t,s)=(1-s)\gamma_0(t)+s\gamma_1(t)$, $0\le t,s\le1$, where $\gamma_{1}(t)=z_{1}$ is constant for all $t$ in $[0,1]$.
 
 
 
@@ -399,10 +552,18 @@
 
 
 
-> [!figure] Figure 20
-> 
-> ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-043_498_520_1871_26.jpg)
-> Figure 20
+```scientific-figure
+id: fc9a99d2-e26c-4ec5-9d0d-6c8e6b900f20
+numbered: false
+title: ""
+caption: "**Figure 20.**"
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-043_498_520_1871_26.jpg
+    caption: ""
+```
 
 
 
@@ -431,38 +592,38 @@
 
 
 
-> [!theorem] Theorem 2: Cauchy's Integral Theorem for Deformable Paths
+<!-- Source label: Theorem 2: Cauchy's Integral Theorem for Deformable Paths -->
+> [!theorem] Cauchy's Integral Theorem for Deformable Paths
 > Let $f$ be a function analytic in a region $\Omega$. (i) If $\gamma_{0}$ and $\gamma_{1}$ are two paths joining $\alpha$ to $\beta$ in $\Omega$, and if $\gamma_{0}$ is continuously deformable into $\gamma_{1}$ relative to $\Omega$, then
-> 
+>
 > $$
 > \int_{\gamma_{0}} f(z) d z=\int_{\gamma_{1}} f(z) d z
 > $$
-> 
+>
 > (ii) If $\gamma_{0}$ and $\gamma_{1}$ are closed paths in $\Omega$ and $\gamma_{0}$ is continuously deformable into $\gamma_{1}$ relative to $\Omega$, then
-> 
+>
 > $$
 > \int_{\gamma_{0}} f(z) d z=\int_{\gamma_{1}} f(z) d z
 > $$
-> 
+>
 > In particular, if $\gamma_{0}$ is a closed path in $\Omega$ that is continuously deformable into a point in $\Omega$, then
-> 
+>
 > $$
 > \int_{\gamma_{0}} f(z) d z=0
 > $$
-> 
 
 The proof of this theorem is quite long and technical. We will present it in full detail in the following section. For now, let us continue with some important applications.
 
 
-> [!corollary] Corollary 1: Path Integrals of Functions Analytic on Disks
+<!-- Source label: Corollary 1: Path Integrals of Functions Analytic on Disks -->
+> [!corollary] Path Integrals of Functions Analytic on Disks
 > Suppose that $\gamma$ is a closed path and $f$ is analytic on an open disk containing $\gamma$. Then
-> 
+>
 > $$
 > \int_{\gamma} f(z) d z=0
 > $$
-> 
-> In particular, if $f$ is entire then (12) holds for any closed path $\gamma$.
-> 
+>
+> In particular, if $f$ is entire then the displayed integral is zero for any closed path $\gamma$.
 
 **Proof:** Any closed path $\gamma$ in a disk is continuously deformable to a point in that disk. This is intuitively clear and follows from Theorem 1(iii) because a disk is a convex set. So (12) follows from Theorem 2. The second part of the corollary clearly follows from the first: If $f$ is entire and $\gamma$ is a closed path, then we can always enclose $\gamma$ in an open disk on which $f$ is analytic. Alternatively, the second part follows from the fact that $\mathbb{C}$ itself is convex, and so any two closed paths are mutually deformable.
 
@@ -509,7 +670,8 @@
 With Cauchy's theorem in hand, our main task is now to identify paths that are mutually continuously deformable. Instead of dealing with this issue on a case-by-case basis, we will try to identify regions in which any two closed paths are mutually deformable. For such regions, we have the following.
 
 
-> [!proposition] Proposition 1
+<!-- Source label: Proposition 1 -->
+> [!proposition] Equivalent Homotopy Criteria for Simple Connectedness
 > Suppose that $\Omega$ is a region in $\mathbb{C}$. The following properties are equivalent.
 > (i) Any two paths $\gamma_{0}$ and $\gamma_{1}$ in $\Omega$ joining two points $\alpha$ and $\beta$ in $\Omega$ are mutually continuously deformable relative to $\Omega$.
 > (ii) Any two closed paths $\gamma_{0}$ and $\gamma_{1}$ in $\Omega$ are mutually continuously deformable relative to $\Omega$.
@@ -520,24 +682,41 @@
 A region $\Omega$ for which (i), and hence (ii) and (iii) of Proposition 1, hold has a special name.
 
 
-> [!definition] Definition 1: Simply Connected Region, Multiply Connected Region
-> A region $\Omega$ is called **simply connected** if all paths joining $\alpha$ to $\beta$ in $\Omega$ are mutually continuously deformable relative to $\Omega$. If a region is not simply connected, then it is called **multiply connected**.
+<!-- Source label: Definition 1: Simply Connected Region, Multiply Connected Region -->
+> [!definition] Simply Connected Region, Multiply Connected Region
+> A region $\Omega$ is called **simply connected** if, for every pair $\alpha,\beta\in\Omega$, all paths joining $\alpha$ to $\beta$ in $\Omega$ are mutually continuously deformable relative to $\Omega$. If a region is not simply connected, then it is called **multiply connected**.
 
 
 
 Geometrically, a region is simply connected if it has no holes in it. _Figure 21_ shows several simply connected regions. Theorem 1 proves that every convex set is simply connected; consequently, a disk and a rectangle are simply connected. (As you can imagine, a convex set cannot have holes in it. So this result agrees with our geometric intuition.) But, as clearly illustrated in the second and third regions in _Figure 21_, a region can be simply connected without being convex.
 
-> [!figure] Figure 21
-> 
-> ![500](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-045_501_1631_1811_244.jpg)
-> Figure 21
+```scientific-figure
+id: 0021ad36-1c15-4820-902b-228f457a8d62
+numbered: false
+title: ""
+caption: "**Figure 21.**"
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-045_501_1631_1811_244.jpg
+    caption: ""
+```
 
 _Figure 22_ shows several multiply connected regions. In each case, we show two paths that are not mutually deformable relative to the region.
 
-> [!figure] Figure 22
-> 
-> ![500](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-046_533_1540_184_386.jpg)
-> Figure 22
+```scientific-figure
+id: 21009736-21a0-4237-a2a2-9f529d766fbf
+numbered: false
+title: ""
+caption: "**Figure 22.**"
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-046_533_1540_184_386.jpg
+    caption: ""
+```
 
 The following fundamental theorem is an immediate consequence of Theorem 2 and the definition of simply connected regions.
 
@@ -545,19 +724,19 @@
 
 
 
-> [!theorem] Theorem 3: Cauchy's Theorem for Simply Connected Regions
+<!-- Source label: Theorem 3: Cauchy's Theorem for Simply Connected Regions -->
+> [!theorem] Cauchy's Theorem for Simply Connected Regions
 > Suppose that $\Omega$ is a simply connected region and that $f$ is analytic in $\Omega$. (i) If $\gamma_{0}$ and $\gamma_{1}$ are two paths joining $\alpha$ to $\beta$ in $\Omega$, then
-> 
+>
 > $$
 > \int_{\gamma_{0}} f(z) d z=\int_{\gamma_{1}} f(z) d z
 > $$
-> 
+>
 > (ii) If $\gamma$ is a closed path in $\Omega$, then
-> 
+>
 > $$
 > \int_{\gamma} f(z) d z=0
 > $$
-> 
 
 Consider the function $\frac{1}{z-z_{0}}$, which is analytic in any punctured disk centered at $z_{0}$. We have $\int_{C_{R}\left(z_{0}\right)} \frac{d z}{z-z_{0}}=2 \pi i \neq 0$ (see Example 4(a), Section 3.2); and so by Theorem 3(ii), the punctured disk is not simply connected. This confirms our geometric understanding of simply connected regions as being regions without holes.
 
@@ -565,13 +744,14 @@
 
 
 
-> [!theorem] Theorem 4: Existence of Antiderivatives
+<!-- Source label: Theorem 4: Existence of Antiderivatives -->
+> [!theorem] Existence of Antiderivatives
 > Suppose that $\Omega$ is a simply connected region and that $f$ is analytic in $\Omega$. Then there is an analytic function $F$ in $\Omega$ such that $F^{\prime}=f$. In other words, every analytic function in $\Omega$ has an antiderivative in $\Omega$. Up to an arbitrary additive constant, we have
-> 
+>
 > $$
 > F(z)=\int_{z_{0}}^{z} f(\zeta) d \zeta
 > $$
-> 
+>
 > where $z_{0}$ is a fixed point in $\Omega$ and the integral is taken over any path in $\Omega$ joining $z_{0}$ to $z$.
 
 
@@ -584,7 +764,8 @@
 Our next topic about paths is closely related to the notion of simply connected regions.
 
 
-> [!definition] Definition 2: Simple Path
+<!-- Source label: Definition 2: Simple Path -->
+> [!definition] Simple Path
 > A closed path $\gamma$ is called simple or a simple curve if $\gamma$ intersects itself only at the endpoints. That is, if $\gamma(t), a \leq t \leq b$, is a parametrization of $\gamma$, and $a \leq t_{1}<t_{2} \leq b$, then $\gamma\left(t_{1}\right)=\gamma\left(t_{2}\right) \Leftrightarrow t_{1}=a$ and $t_{2}=b$.
 
 
@@ -601,21 +782,20 @@
 
 When we combine these properties with Theorems 2 and 3, we obtain a very useful integral theorem for simple paths. First recall that $f$ is analytic at a point if it is analytic in a neighborhood of that point. So to say that $f$ is analytic on a curve $C$ and its interior means that $f$ is analytic in a region $\Omega$ containing $C$ and its interior.
 
-> [!theorem] Theorem 5: Cauchy's Theorem for Simple Paths
+<!-- Source label: Theorem 5: Cauchy's Theorem for Simple Paths -->
+> [!theorem] Cauchy's Theorem for Simple Paths
 > Suppose that $f$ is analytic on a simple closed path $C$ and its interior.
 > (i) We have
-> 
+>
 > $$
 > \int_{C} f(z) d z=0
 > $$
-> 
+>
 > (ii) If $\gamma$ is a closed path (not necessarily simple) contained in the interior of $C$, then
-> 
+>
 > $$
 > \int_{\gamma} f(z) d z=0
 > $$
-> 
-> 
 
 **Proof:** Since $f$ is analytic on a region $\Omega$ that contains $C$ and its interior, and since $C$ can be continuously deformed into a point relative to $\Omega$, (i) follows from Cauchy's Theorem 2. Part (ii) follows from Theorem 3, because the interior of $C$ is simply connected.
 
@@ -641,31 +821,47 @@
 
 
 
-> [!figure] Figure 23
-> 
-> ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-048_514_514_526_107.jpg)
-> Figure 23
-
-
-
-
-
-
-> [!theorem] Theorem 6: Cauchy's Theorem for Multiply Connected Regions
-> Suppose that $f$ is analytic on a region $\Omega$ with simple paths $C$ and $C_{j}(j= 1,2, \ldots, n)$ as described above. Then
-> 
+```scientific-figure
+id: 93afd49b-0d6e-43f0-8c20-54c2491da5a5
+numbered: false
+title: ""
+caption: "**Figure 23.**"
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-048_514_514_526_107.jpg
+    caption: ""
+```
+
+
+
+
+
+
+<!-- Source label: Theorem 6: Cauchy's Theorem for Multiply Connected Regions -->
+> [!theorem] Cauchy's Theorem for Multiply Connected Regions
+> Suppose that $f$ is analytic on a region $\Omega$ with simple paths $C$ and $C_{j}(j= 1,2, \ldots, n)$ positively oriented and contained in $\Omega$, where the $C_j$ are inside $C$ with pairwise disjoint interiors and boundaries, and the closed region inside $C$ and outside the $C_j$ is contained in $\Omega$. Then
+>
 > $$
 > \int_{C} f(z) d z=\sum_{j=1}^{n} \int_{C_{j}} f(z) d z
 > $$
-> 
 
 **Proof** Join the outer path $C$ to $C_{1}$ using a polygonal path $L_{1}$ traversed in two opposite directions. Join $C_{1}$ to $C_{2}$ by a similar polygonal path $L_{2}$. Continue in this fashion, joining the path $C_{j}$ to the path $C_{j+1}$ by a polygonal path $L_{j+1}$ traversed in two opposite directions, and finally join $C_{n}$ to $C$ by a polygonal path $L_{n+1}$ traversed in two opposite directions. This construction yields two simple closed paths $\Gamma_{1}$ and $\Gamma_{2}$, as illustrated in _Figure 24_. (Note that, along either $\Gamma_{1}$ or $\Gamma_{2}$, we traverse portions of the $C_{j}$ 's in a direction opposite to their original orientation.) 
 
 
-> [!figure] Figure 24
-> 
-> ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-048_519_538_1516_109.jpg)
-> Figure 24 Each polygonal path $L_{j}$ is traversed in both directions, so the integral over $L_{j}$ is 0 .
+```scientific-figure
+id: dca5e52a-7162-44dd-a213-69d50a478097
+numbered: false
+title: ""
+caption: "**Figure 24.** Each polygonal path $L_{j}$ is traversed in both directions, so the integral over $L_{j}$ is 0 ."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-048_519_538_1516_109.jpg
+    caption: ""
+```
 
 
 
@@ -714,7 +910,9 @@
 
 
 
-**Solution** If $z_{0}$ is in the exterior of $C$, then the function $f(z)=\frac{1}{z-z_{0}}$ is analytic on and inside $C$ and hence its integral along $C$ is 0 , by Theorem 5(i). For the second case, where $z_{0}$ is in the interior of $C$, we can no longer claim that the function $f(z)=\frac{1}{z-z_{0}}$ is analytic on and inside $C$, and so we cannot use Theorem 5. To deal with this case, let us recall that
+##### solution
+
+If $z_{0}$ is in the exterior of $C$, then the function $f(z)=\frac{1}{z-z_{0}}$ is analytic on and inside $C$ and hence its integral along $C$ is 0 , by Theorem 5(i). For the second case, where $z_{0}$ is in the interior of $C$, we can no longer claim that the function $f(z)=\frac{1}{z-z_{0}}$ is analytic on and inside $C$, and so we cannot use Theorem 5. To deal with this case, let us recall that
 
 $$
 \int_{C_{R}\left(z_{0}\right)} \frac{1}{z-z_{0}} d z=2 \pi i
@@ -755,7 +953,9 @@
 
 
 
-**Solution** We start by finding the partial fraction decomposition of the integrand,
+##### solution
+
+We start by finding the partial fraction decomposition of the integrand,
 
 $$
 \frac{1}{(z-1)(z+i)(z-i)}=\frac{a}{z-1}+\frac{b}{z+i}+\frac{c}{z-i}
@@ -837,24 +1037,42 @@
 > 
 > 
 > 
-> > [!figure] Figure 25
-> > 
-> > ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-051_486_531_659_552.jpg)
-> > Figure 25
+> ```scientific-figure
+> id: 289d4078-072b-41a1-be81-b916878af29d
+> numbered: false
+> title: ""
+> caption: "**Figure 25.**"
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-051_486_531_659_552.jpg
+>     caption: ""
+> ```
 > 
 > 
 > 
 > 
 > The path $C$ in _Figure 25_ is not simple because it intersects itself. To use Cauchy's integral theorem for simple paths, we break up $C$ into two simple paths, as shown in _Figure 26_.
 > 
-> > [!figure] Figure 26
-> > 
-> > ![[Screenshot 2026-04-02 at 5.59.48 AM.png]]
-> > Figure 26
-> 
-> 
-
-**Solution** We will first break the path into two simple closed paths, $C_{1}$ and $C_{2}$, shown in _Figure 26_. Note that the orientation of $C_{1}$ is negative, while the orientation of $C_{2}$ is positive. The integral (16) becomes
+> ```scientific-figure
+> id: d831643a-f0e5-4c34-a48d-68b8d27df906
+> numbered: false
+> title: ""
+> caption: "**Figure 26.**"
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/Screenshot 2026-04-02 at 5.59.48 AM.png
+>     caption: ""
+> ```
+> 
+> 
+
+##### solution
+
+We will first break the path into two simple closed paths, $C_{1}$ and $C_{2}$, shown in _Figure 26_. Note that the orientation of $C_{1}$ is negative, while the orientation of $C_{2}$ is positive. The integral (16) becomes
 
 $$
 \int_{C_{1}} \frac{z}{(z-i)(z-1)} d z+\int_{C_{2}} \frac{z}{(z-i)(z-1)} d z=I_{1}+I_{2}
@@ -895,50 +1113,98 @@
 > 
 > 1.
 > 
-> > [!figure] Figure 27
-> > 
-> > ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-052_512_521_744_380.jpg)
-> > Figure 27
+> ```scientific-figure
+> id: aee4ea46-f15a-4f28-ad04-ae7675178601
+> numbered: false
+> title: ""
+> caption: "**Figure 27.**"
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-052_512_521_744_380.jpg
+>     caption: ""
+> ```
 > 
 > 2. 
 > 
-> > [!figure] Figure 28
-> > 
-> > ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-052_510_512_737_940.jpg)
-> > Figure 28
+> ```scientific-figure
+> id: 4747b8aa-c17e-4bef-9912-c4e0c53288d6
+> numbered: false
+> title: ""
+> caption: "**Figure 28.**"
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-052_510_512_737_940.jpg
+>     caption: ""
+> ```
 > 
 > 3. 
 > 
-> > [!figure] Figure 29
-> > 
-> > ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-052_512_508_735_1524.jpg)
-> > Figure 29
+> ```scientific-figure
+> id: a777d881-bb7a-477c-8ece-9778c0b067b2
+> numbered: false
+> title: ""
+> caption: "**Figure 29.**"
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-052_512_508_735_1524.jpg
+>     caption: ""
+> ```
 > 
 > 
 > 4. 
 > 
-> > [!figure] Figure 30
-> > 
-> > ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-052_508_514_1385_397.jpg)
-> > Figure 30
+> ```scientific-figure
+> id: 121bb8c6-ed3b-4197-84c5-d0a3dd14c7f2
+> numbered: false
+> title: ""
+> caption: "**Figure 30.**"
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-052_508_514_1385_397.jpg
+>     caption: ""
+> ```
 > 
 > 
 > 
 > 5. 
 > 
-> > [!figure] Figure 31
-> > 
-> > ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-052_512_514_1381_953.jpg)
-> > Figure 31
+> ```scientific-figure
+> id: e7c7edc0-be00-4cac-8f66-65d2a112183a
+> numbered: false
+> title: ""
+> caption: "**Figure 31.**"
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-052_512_514_1381_953.jpg
+>     caption: ""
+> ```
 > 
 > 
 > 
 > 6. 
 > 
-> > [!figure] Figure 32
-> > 
-> > ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-052_516_508_1379_1539.jpg)
-> > Figure 32
+> ```scientific-figure
+> id: f6287754-653a-4d12-9941-38d827000a13
+> numbered: false
+> title: ""
+> caption: "**Figure 32.**"
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-052_516_508_1379_1539.jpg
+>     caption: ""
+> ```
 > 
 > 
 > 
@@ -949,10 +1215,18 @@
 > 
 > 7. Describe the mapping of the unit square into $\Omega$ that continuously deforms $\gamma_{0}$ into $\gamma_{1}$ relative to $\Omega$ in _Figure 33_.
 > 
-> > [!figure] Figure 33
-> > 
-> > ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-052_516_523_2074_410.jpg)
-> > Figure 33
+> ```scientific-figure
+> id: ef4e618e-5f84-4a26-aaac-b787fa1857c0
+> numbered: false
+> title: ""
+> caption: "**Figure 33.**"
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-052_516_523_2074_410.jpg
+>     caption: ""
+> ```
 > 
 > 
 > 
@@ -960,10 +1234,18 @@
 > 8. (a) Describe the mapping $H(t, s)$ of the unit square that continuously deforms $\gamma_{0}$ into $\gamma_{1}$ relative to $\Omega$ in _Figure 34_.
 > 
 > 
-> > [!figure] Figure 34
-> > 
-> > ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-052_516_523_2074_968.jpg)
-> > Figure 34
+> ```scientific-figure
+> id: 88de6bbe-47ce-4cc5-adea-f14148a9e105
+> numbered: false
+> title: ""
+> caption: "**Figure 34.**"
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-052_516_523_2074_968.jpg
+>     caption: ""
+> ```
 > 
 > 
 > (b) Illustrate the deformation process in (a) by drawing $\gamma_{0}$ and $\gamma_{1}$ and the graph of $H(t, s)$ as a function of $t$ alone, for various fixed values of $s$.
@@ -973,10 +1255,18 @@
 > 9. Describe the mapping of the unit square that continuously deforms the path $\gamma_{0}$ into a point relative to $\Omega$ in _Figure 35_. You may pick any point in $\Omega$.
 > 
 > 
-> > [!figure] Figure 35
-> > 
-> > ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-052_514_500_2076_1560.jpg)
-> > Figure 35
+> ```scientific-figure
+> id: 3d3cb5c7-dfc5-4735-be75-aff06d664b2c
+> numbered: false
+> title: ""
+> caption: "**Figure 35.**"
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-052_514_500_2076_1560.jpg
+>     caption: ""
+> ```
 > 
 > 
 
@@ -986,22 +1276,46 @@
 > 
 > 
 > 
-> > [!figure] Figure 36
-> > 
-> > ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-053_513_523_499_271.jpg)
-> > Figure 36
-> 
-> > [!figure] Figure 37
-> > 
-> > ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-053_510_511_512_839.jpg)
-> > Figure 37
-> 
-> 
-> 
-> > [!figure] Figure 38
-> > 
-> > ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-053_507_524_520_1424.jpg)
-> > Figure 38
+> ```scientific-figure
+> id: d02ee843-f65f-4846-ba30-764841da6404
+> numbered: false
+> title: ""
+> caption: "**Figure 36.**"
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-053_513_523_499_271.jpg
+>     caption: ""
+> ```
+> 
+> ```scientific-figure
+> id: dd038553-b1e1-4e82-8c25-a4f4ebf3cd04
+> numbered: false
+> title: ""
+> caption: "**Figure 37.**"
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-053_510_511_512_839.jpg
+>     caption: ""
+> ```
+> 
+> 
+> 
+> ```scientific-figure
+> id: 3d01406d-43c4-4af4-8300-beffe4e91b65
+> numbered: false
+> title: ""
+> caption: "**Figure 38.**"
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-053_507_524_520_1424.jpg
+>     caption: ""
+> ```
 > 
 > 
 > 
@@ -1016,36 +1330,84 @@
 > 
 > 
 > 
-> > [!figure] Figure 39
-> > 
-> > ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-053_515_521_1471_258.jpg)
-> > Figure 39
-> 
-> 
-> > [!figure] Figure 40
-> > 
-> > ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-053_511_522_1471_817.jpg)
-> > Figure 40
-> 
-> > [!figure] Figure 41
-> > 
-> > ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-053_509_524_1475_1411.jpg)
-> > Figure 41
-> 
-> > [!figure] Figure 42
-> > 
-> > ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-053_528_522_2074_247.jpg)
-> > Figure 42
-> 
-> > [!figure] Figure 43
-> > 
-> > ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-053_526_524_2069_808.jpg)
-> > Figure 43
-> 
-> > [!figure] Figure 44
-> > 
-> > ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-053_524_533_2078_1400.jpg)
-> > Figure 44
+> ```scientific-figure
+> id: 2b75b50c-8aa6-4f33-84d5-a65b30ac0fd1
+> numbered: false
+> title: ""
+> caption: "**Figure 39.**"
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-053_515_521_1471_258.jpg
+>     caption: ""
+> ```
+> 
+> 
+> ```scientific-figure
+> id: 76bdc11f-5a74-4952-9fc5-3a319d4e08a1
+> numbered: false
+> title: ""
+> caption: "**Figure 40.**"
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-053_511_522_1471_817.jpg
+>     caption: ""
+> ```
+> 
+> ```scientific-figure
+> id: 801c452b-a6a6-4f2d-b19a-2a708f054969
+> numbered: false
+> title: ""
+> caption: "**Figure 41.**"
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-053_509_524_1475_1411.jpg
+>     caption: ""
+> ```
+> 
+> ```scientific-figure
+> id: ce99ebbd-01a1-4715-91b6-b207be2b8ed8
+> numbered: false
+> title: ""
+> caption: "**Figure 42.**"
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-053_528_522_2074_247.jpg
+>     caption: ""
+> ```
+> 
+> ```scientific-figure
+> id: ba19ded4-09ac-4c0e-983b-aff5f705938f
+> numbered: false
+> title: ""
+> caption: "**Figure 43.**"
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-053_526_524_2069_808.jpg
+>     caption: ""
+> ```
+> 
+> ```scientific-figure
+> id: 6d9b659f-d2f4-42f0-8dde-2767582cb474
+> numbered: false
+> title: ""
+> caption: "**Figure 44.**"
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-053_524_533_2078_1400.jpg
+>     caption: ""
+> ```
 > 
 > 
 > 
@@ -1074,39 +1436,71 @@
 > 
 > 
 > 
-> > [!figure] Figure 45
-> > 
-> > ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-054_460_502_203_107.jpg)
-> > Figure 45
+> ```scientific-figure
+> id: 5cca3146-f092-4f61-9795-dd247710fb3a
+> numbered: false
+> title: ""
+> caption: "**Figure 45.**"
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-054_460_502_203_107.jpg
+>     caption: ""
+> ```
 > 
 > 
 > 
 > 29. $\int_{\gamma} \frac{1}{(z+1)^{2}\left(z^{2}+1\right)} d z$, where $\gamma$ is the path that consists of the two circles in _Figure 46_.
 > 
 > 
-> > [!figure] Figure 46
-> > 
-> > ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-054_454_518_716_107.jpg)
-> > Figure 46
+> ```scientific-figure
+> id: 5b157236-4243-4149-ac8d-ffec8eb87b9c
+> numbered: false
+> title: ""
+> caption: "**Figure 46.**"
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-054_454_518_716_107.jpg
+>     caption: ""
+> ```
 > 
 > 
 > 30. $\int_{\gamma} \frac{1}{z+1} d z$, where $\gamma$ is the path in _Figure 47_ .
 > 
 > 
-> > [!figure] Figure 47
-> > 
-> > ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-054_470_526_1223_107.jpg)
-> > Figure 47
+> ```scientific-figure
+> id: 99e19a55-9e9b-4c71-8136-13aa6c3a0896
+> numbered: false
+> title: ""
+> caption: "**Figure 47.**"
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-054_470_526_1223_107.jpg
+>     caption: ""
+> ```
 > 
 > 
 > 31. $\int_{\gamma} \frac{z+1}{z-i} d z$, where $\gamma$ is the path in _Figure 48_.
 > 
 > 
 > 
-> > [!figure] Figure 48
-> > 
-> > ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-054_483_529_1809_107.jpg)
-> > Figure 48
+> ```scientific-figure
+> id: 1bb50ea7-7299-4793-8125-1354c1685d67
+> numbered: false
+> title: ""
+> caption: "**Figure 48.**"
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-054_483_529_1809_107.jpg
+>     caption: ""
+> ```
 > 
 > 
 > 
@@ -1230,10 +1624,18 @@
 > 
 > 
 > 
-> > [!figure] Figure 49
-> > 
-> > ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-057_520_453_236_25.jpg)
-> > Figure 49
+> ```scientific-figure
+> id: ebf34ff6-b726-4364-b6d5-9945bc634845
+> numbered: false
+> title: ""
+> caption: "**Figure 49.**"
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-057_520_453_236_25.jpg
+>     caption: ""
+> ```
 > 
 > 
 
@@ -1277,10 +1679,18 @@
 > 
 > 
 > 
-> > [!figure] Figure 50
-> > 
-> > ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-057_509_438_1800_21.jpg)
-> > Figure 50
+> ```scientific-figure
+> id: efb843e7-c46e-4623-9f37-e06f124a9dae
+> numbered: false
+> title: ""
+> caption: "**Figure 50.**"
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-057_509_438_1800_21.jpg
+>     caption: ""
+> ```
 > 
 > 
 > Repeat this same type of reasoning for a larger $n$ (say, $n=5$ ) and a more complicated arrangement of $C_{j}$ 's. It will work, but the connecting pieces $L_{j}$ might be curved.

`````
