
# Editorial records

Reading note: 3.9 Goursat's Theorem.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Callout 143: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Goursat's Theorem on Continuity of the Complex Derivative
> Let $f$ be a complex-valued function on an open set $\Omega$. If $f$ is differentiable on $\Omega$; that is, if the derivative
>
> $$
> f^{\prime}\left(z_{0}\right)=\lim _{z \rightarrow z_{0}} \frac{f(z)-f\left(z_{0}\right)}{z-z_{0}}
> $$
>
> exists for all $z_{0}$ in $\Omega$, then $f$ is analytic on $\Omega$ (that is, $f^{\prime}$ is continuous on $\Omega$ ).
````
### After

````text
> [!theorem] Goursat's Theorem
> Let $f$ be a complex-valued function on an open set $\Omega$. If $f$ is differentiable on $\Omega$; that is, if the derivative
>
> $$
> f^{\prime}\left(z_{0}\right)=\lim _{z \rightarrow z_{0}} \frac{f(z)-f\left(z_{0}\right)}{z-z_{0}}
> $$
>
> exists for all $z_{0}$ in $\Omega$, then $f$ is analytic on $\Omega$ (that is, $f^{\prime}$ is continuous on $\Omega$ ).
````

## 2. Callout 144: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Analyticity and Complex Differentiability on an Open Set
> Let $f$ be a complex-valued function on an open set $\Omega$. Then $f$ is analytic on $\Omega$ if and only if
>
> $$
> f^{\prime}\left(z_{0}\right)=\lim _{z \rightarrow z_{0}} \frac{f(z)-f\left(z_{0}\right)}{z-z_{0}}
> $$
>
> exists for all $z_{0}$ in $\Omega$.
````
### After

````text
> [!theorem] Analytic Functions
> Let $f$ be a complex-valued function on an open set $\Omega$. Then $f$ is analytic on $\Omega$ if and only if
>
> $$
> f^{\prime}\left(z_{0}\right)=\lim _{z \rightarrow z_{0}} \frac{f(z)-f\left(z_{0}\right)}{z-z_{0}}
> $$
>
> exists for all $z_{0}$ in $\Omega$.
````

## Source-to-current comparison

Source: /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 03 Complex Integration/3.9 Goursat's Theorem.md

This exact comparison preserves the full change evidence, including formatting, OCR corrections, restored source wording, and required standalone context. The entries above explain the recovery edits. The comparison is not a claim that every difference is a correction; component serialization, callout wrapping, and printed labels outside callouts are formatting.

`````diff
--- /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 03 Complex Integration/3.9 Goursat's Theorem.md
+++ /Users/gradyclopton/ObsidianVaults/complex_analysis/Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/3.9 Goursat's Theorem.md
@@ -13,26 +13,28 @@
 
 
 
-> [!theorem] Theorem 1: Goursat's Theorem
+<!-- Source label: Theorem 1: Goursat's Theorem -->
+> [!theorem] Goursat's Theorem
 > Let $f$ be a complex-valued function on an open set $\Omega$. If $f$ is differentiable on $\Omega$; that is, if the derivative
-> 
+>
 > $$
 > f^{\prime}\left(z_{0}\right)=\lim _{z \rightarrow z_{0}} \frac{f(z)-f\left(z_{0}\right)}{z-z_{0}}
 > $$
-> 
+>
 > exists for all $z_{0}$ in $\Omega$, then $f$ is analytic on $\Omega$ (that is, $f^{\prime}$ is continuous on $\Omega$ ).
 
 Before we prove the theorem, let us make some additional remarks. Let us record the following important improvement to the definition of analytic functions.
 
 
 
-> [!theorem] Theorem 2: Analytic Functions
+<!-- Source label: Theorem 2: Analytic Functions -->
+> [!theorem] Analytic Functions
 > Let $f$ be a complex-valued function on an open set $\Omega$. Then $f$ is analytic on $\Omega$ if and only if
-> 
+>
 > $$
 > f^{\prime}\left(z_{0}\right)=\lim _{z \rightarrow z_{0}} \frac{f(z)-f\left(z_{0}\right)}{z-z_{0}}
 > $$
-> 
+>
 > exists for all $z_{0}$ in $\Omega$.
 
 
@@ -61,19 +63,20 @@
 
 
 
-> [!figure] Figure 1
-> 
-> ```horizontal
-> 
-> ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-102_373_522_876_63.jpg)
-> 
-> ---
-> 
-> ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-102_377_493_494_70.jpg)
-> 
-> ```
-> 
-> Figure 1 The function $f(x)$ is defined on the real line and has derivative $f^{\prime}(x)$ that exists everywhere, but $f^{\prime}(x)$ is not continuous at $x=$ 0 . Goursat's theorem tells us that nothing like this happens with functions defined on regions $\Omega$ in $\mathbb{C}$. If $f^{\prime}$ exists on $\Omega$, then it must be continuous on $\Omega$.
+```scientific-figure
+id: 78b52de8-1b79-40d5-9cff-12ffb302d0d8
+numbered: false
+title: ""
+caption: Figure 1 The function $f(x)$ is defined on the real line and has derivative $f^{\prime}(x)$ that exists everywhere, but $f^{\prime}(x)$ is not continuous at $x=$ 0 . Goursat's theorem tells us that nothing like this happens with functions defined on regions $\Omega$ in $\mathbb{C}$. If $f^{\prime}$ exists on $\Omega$, then it must be continuous on $\Omega$.
+captionVisible: true
+captionPosition: below
+columns: 2
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-102_373_522_876_63.jpg
+    caption: ""
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-102_377_493_494_70.jpg
+    caption: ""
+```
 
 
 
@@ -85,23 +88,22 @@
 **Proof of Theorem 1** We will apply the strong version of Morera's theorem (Exercise 37, Section 3.6). Let $\Delta$ be an arbitrary triangle lying in some disk in $\Omega$ and let $\gamma$ denote the boundary of $\Delta$. Subdivide $\Delta$ into four congruent subtriangles by taking the midpoints of the sides and connecting them with line segments. Call the subtriangles $\Delta_{1}^{j}, j=1,2,3,4$ and let $\gamma_{1}^{j}$ denote the boundary of $\Delta_{1}^{j}$, with the same orientation as $\gamma$ (say positive; see _Figure 2_). 
 
 
-> [!figure] Figure 2
-> 
-> ```horizontal
-> 
-> ![303](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-102_531_497_2114_507.jpg)
-> 
-> ---
-> 
-> ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-102_521_504_2116_1514.jpg)
-> 
-> ---
-> 
-> ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-103_496_480_286_72.jpg)
-> 
-> ```
-> 
-> Figure 2 This figure illustrates the case when $\left|I_{1}^{3}\right|$ is larger than $\left|I_{1}^{j}\right|$ for $j=1,2,3,4$. In this case, we pick the triangle $\Delta_{1}^{3}$ and set $\Delta_{2}= \Delta_{1}^{3}$. Next, we subdivide $\Delta_{2}$ into four congruent triangles and proceed as before to determine $\Delta_{3}$. Continue ad infinitum.
+```scientific-figure
+id: b0d58740-8b16-44b4-a167-80df642b959c
+numbered: false
+title: ""
+caption: Figure 2 This figure illustrates the case when $\left|I_{1}^{3}\right|$ is larger than $\left|I_{1}^{j}\right|$ for $j=1,2,3,4$. In this case, we pick the triangle $\Delta_{1}^{3}$ and set $\Delta_{2}= \Delta_{1}^{3}$. Next, we subdivide $\Delta_{2}$ into four congruent triangles and proceed as before to determine $\Delta_{3}$. Continue ad infinitum.
+captionVisible: true
+captionPosition: below
+columns: 2
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-102_531_497_2114_507.jpg
+    caption: ""
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-102_521_504_2116_1514.jpg
+    caption: ""
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-103_496_480_286_72.jpg
+    caption: ""
+```
 
 
 Let
@@ -140,10 +142,18 @@
 The triangles $\Delta_{n}$ form a sequence of nested closed sets with diameters tending to 0 . By Cantor's intersection theorem, there is exactly one point, say $z_{0}$, that belongs to all $\Delta_{n}$ (_Figure 3_). 
 
 
-> [!figure] Figure 3
-> 
-> ![[Screenshot 2026-04-02 at 8.10.27 AM.png]]
-> Figure 3 Cantor's intersection theorem applied to the sequence of nested triangles with diameters shrinking to 0 yields the point $z_0$ that belongs to all the triangles in this sequence.
+```scientific-figure
+id: 65d5427f-ffef-4c24-a8a7-2b303615f3f8
+numbered: false
+title: ""
+caption: "**Figure 3.** Cantor's intersection theorem applied to the sequence of nested triangles with diameters shrinking to 0 yields the point $z_0$ that belongs to all the triangles in this sequence."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Screenshot 2026-04-02 at 8.10.27 AM.png
+    caption: ""
+```
 
 
 
@@ -178,10 +188,18 @@
 and it follows from (1) that $|I|=0$, completing the proof.
 
 
-> [!figure] Figure 4
-> 
-> ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-103_584_556_1326_36.jpg)
-> Figure 4 The inequality $z-z_{0} \mid \leq l\left(\gamma_{n}\right)$ for $z$ on $\gamma_{n}$ and $z_{0}$ inside $\gamma_{n}$, illustrated with $n=3$.
+```scientific-figure
+id: c1a17821-90dc-4a84-a316-ec8688d9cd3c
+numbered: false
+title: ""
+caption: "**Figure 4.** The inequality $z-z_{0} \\mid \\leq l\\left(\\gamma_{n}\\right)$ for $z$ on $\\gamma_{n}$ and $z_{0}$ inside $\\gamma_{n}$, illustrated with $n=3$."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-103_584_556_1326_36.jpg
+    caption: ""
+```
 
 
 Goursat's theorem will be needed at crucial stages in proofs of results in the following chapter.

`````
