
# Editorial records

Reading note: 5.4 Improper Integrals of Products of Rational and Trigonometric Functions.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Callout 211: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!lemma] Jordan's Lemma for Upper-Half-Plane Circular Arcs
> Let $f(z)$ be a continuous complex-valued function defined on the circular $\operatorname{arcs} \sigma_{R}$ consisting of all $z=R e^{i \theta}$, where $R \geq R_{0}$ ( $R_{0}$ fixed) and $0 \leq \theta_{1} \leq \theta \leq \theta_{2} \leq \pi$, and let $M(R)$ denote the maximum value of $|f(z)|$ for $z$ on $\sigma_{R}$. If $\lim _{R \rightarrow \infty} M(R)=0$, then for all $s>0$
>
> $$
> \lim _{R \rightarrow \infty} \int_{\sigma_{R}} e^{i s z} f(z) d z=0
> $$
````
### After

````text
> [!lemma] Jordan's Lemma
> Let $f(z)$ be a continuous complex-valued function defined on the circular $\operatorname{arcs} \sigma_{R}$ consisting of all $z=R e^{i \theta}$, where $R \geq R_{0}$ ( $R_{0}$ fixed) and $0 \leq \theta_{1} \leq \theta \leq \theta_{2} \leq \pi$, and let $M(R)$ denote the maximum value of $|f(z)|$ for $z$ on $\sigma_{R}$. If $\lim _{R \rightarrow \infty} M(R)=0$, then for all $s>0$
>
> $$
> \lim _{R \rightarrow \infty} \int_{\sigma_{R}} e^{i s z} f(z) d z=0
> $$
````

## 2. Callout 213: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!lemma] Shrinking Circular Arc Limit for a Cauchy-Type Integral
> Suppose that $f(z)$ is a continuous complex-valued function on a closed disk $S_{r_{0}}\left(z_{0}\right)$ with center at $z_{0}$ and radius $r_{0}$. For $0<r \leq r_{0}$, let $\sigma_{r}$ denote the positively oriented circular arc at angle $\alpha$, consisting of all $z=z_{0}+r e^{i \theta}$, where $\theta_{0} \leq \theta \leq \theta_{0}+\alpha, \theta_{0}$ and $\alpha$ are fixed, and $\alpha>0$. Then
>
> $$
> \lim _{r \rightarrow 0^{+}} \frac{1}{i \alpha} \int_{\sigma_{r}} \frac{f(z)}{z-z_{0}} d z=f\left(z_{0}\right)
> $$
````
### After

````text
> [!lemma] Shrinking Path Lemma
> Suppose that $f(z)$ is a continuous complex-valued function on a closed disk $S_{r_{0}}\left(z_{0}\right)$ with center at $z_{0}$ and radius $r_{0}$. For $0<r \leq r_{0}$, let $\sigma_{r}$ denote the positively oriented circular arc at angle $\alpha$, consisting of all $z=z_{0}+r e^{i \theta}$, where $\theta_{0} \leq \theta \leq \theta_{0}+\alpha, \theta_{0}$ and $\alpha$ are fixed, and $\alpha>0$. Then
>
> $$
> \lim _{r \rightarrow 0^{+}} \frac{1}{i \alpha} \int_{\sigma_{r}} \frac{f(z)}{z-z_{0}} d z=f\left(z_{0}\right)
> $$
````

## Source-to-current comparison

Source: /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 05 Residue Theory/5.4 Improper Integrals of Products of Rational and Trigonometric Functions.md

This exact comparison preserves the full change evidence, including formatting, OCR corrections, restored source wording, and required standalone context. The entries above explain the recovery edits. The comparison is not a claim that every difference is a correction; component serialization, callout wrapping, and printed labels outside callouts are formatting.

`````diff
--- /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 05 Residue Theory/5.4 Improper Integrals of Products of Rational and Trigonometric Functions.md
+++ /Users/gradyclopton/ObsidianVaults/complex_analysis/Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 05 Residue Theory/5.4 Improper Integrals of Products of Rational and Trigonometric Functions.md
@@ -19,10 +19,18 @@
 where $a$ and $b$ are real and $\frac{p(x)}{q(x)}$ is a rational function of $x$. The method is similar to the one we used previously. We will even use the expanding closed semi-circles $\gamma_{R}$ in _Figure 1_, as we did in Section 5.3. 
 
 
-> [!figure] Figure 1
-> 
-> ![300](./images/b1ad9866-c636-4d3b-85cb-e1f2bdb2e560-25_499_454_1861_36.jpg)
-> Figure 1 An expanding closed semi-circle with radius $R \rightarrow \infty$.
+```scientific-figure
+id: 48cc922f-7567-489d-8896-81db7027ac3b
+numbered: false
+title: ""
+caption: "**Figure 1.** An expanding closed semi-circle with radius $R \\rightarrow \\infty$."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 05 Residue Theory/images/b1ad9866-c636-4d3b-85cb-e1f2bdb2e560-25_499_454_1861_36.jpg
+    caption: ""
+```
 
 
 
@@ -64,7 +72,9 @@
 > $$
 > 
 
-**solution** Step 1: Show that the improper integral is convergent. We have $\left|\frac{\cos s x}{x^{2}+a^{2}}\right| \leq \frac{1}{x^{2}+a^{2}}$, and since $\int_{-\infty}^{\infty} \frac{d x}{x^{2}+a^{2}}$ is convergent, our integral converges by Proposition 1, Section 5.3.
+##### solution
+
+Step 1: Show that the improper integral is convergent. We have $\left|\frac{\cos s x}{x^{2}+a^{2}}\right| \leq \frac{1}{x^{2}+a^{2}}$, and since $\int_{-\infty}^{\infty} \frac{d x}{x^{2}+a^{2}}$ is convergent, our integral converges by Proposition 1, Section 5.3.
 Step 2: Set up and evaluate the contour integral. Since
 (4) $\int_{-\infty}^{\infty} \frac{\cos s x}{x^{2}+a^{2}} d x=\int_{-\infty}^{\infty} \operatorname{Re}\left(\frac{e^{i s x}}{x^{2}+a^{2}}\right) d x=\operatorname{Re}\left(\int_{-\infty}^{\infty} \frac{e^{i s x}}{x^{2}+a^{2}} d x\right)$,
 we will consider the contour integral
@@ -77,10 +87,18 @@
 
 
 
-> [!figure] Figure 2
-> 
-> ![300](./images/b1ad9866-c636-4d3b-85cb-e1f2bdb2e560-26_489_523_931_120.jpg)
-> Figure 2 The path and poles for the contour integral in Example 1.
+```scientific-figure
+id: e712dd1d-0284-4b84-bf36-4a53d72904f6
+numbered: false
+title: ""
+caption: "**Figure 2.** The path and poles for the contour integral in Example 1."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 05 Residue Theory/images/b1ad9866-c636-4d3b-85cb-e1f2bdb2e560-26_489_523_931_120.jpg
+    caption: ""
+```
 
 
 
@@ -143,19 +161,27 @@
 
 
 
+<!-- Source label: Jordan's Lemma -->
 > [!lemma] Jordan's Lemma
-> Let $f(z)$ be a continuous complex-valued function defined on the circular $\operatorname{arcs} \sigma_{R}$ consisting of all $z=R e^{i \theta}$, where $R \geq R_{0}$ ( $R_{0}$ fixed) and $0 \leq \theta_{1} \leq \theta \leq \theta_{2} \leq \pi$ (_Figure 3_), and let $M(R)$ denote the maximum value of $|f(z)|$ for $z$ on $\sigma_{R}$. If $\lim _{R \rightarrow \infty} M(R)=0$, then for all $s>0$
-> 
+> Let $f(z)$ be a continuous complex-valued function defined on the circular $\operatorname{arcs} \sigma_{R}$ consisting of all $z=R e^{i \theta}$, where $R \geq R_{0}$ ( $R_{0}$ fixed) and $0 \leq \theta_{1} \leq \theta \leq \theta_{2} \leq \pi$, and let $M(R)$ denote the maximum value of $|f(z)|$ for $z$ on $\sigma_{R}$. If $\lim _{R \rightarrow \infty} M(R)=0$, then for all $s>0$
+>
 > $$
 > \lim _{R \rightarrow \infty} \int_{\sigma_{R}} e^{i s z} f(z) d z=0
 > $$
-> 
-
-
-> [!figure] Figure 3
-> 
-> ![300](./images/b1ad9866-c636-4d3b-85cb-e1f2bdb2e560-27_482_488_1706_28.jpg)
-> Figure 3
+
+
+```scientific-figure
+id: 56b824cc-7fb6-48f2-9449-3e055723e9da
+numbered: false
+title: ""
+caption: "**Figure 3.**"
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 05 Residue Theory/images/b1ad9866-c636-4d3b-85cb-e1f2bdb2e560-27_482_488_1706_28.jpg
+    caption: ""
+```
 
 
 
@@ -187,10 +213,18 @@
 
 
 
-> [!figure] Figure 4
-> 
-> ![300](./images/b1ad9866-c636-4d3b-85cb-e1f2bdb2e560-28_477_503_712_127.jpg)
-> Figure 4
+```scientific-figure
+id: 16747dfc-5e75-4dd2-8ee6-caffa98bad4a
+numbered: false
+title: ""
+caption: "**Figure 4.**"
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 05 Residue Theory/images/b1ad9866-c636-4d3b-85cb-e1f2bdb2e560-28_477_503_712_127.jpg
+    caption: ""
+```
 
 
 
@@ -218,7 +252,8 @@
 
 
 
-> [!corollary]
+<!-- Source label:  -->
+> [!corollary] Vanishing Exponential–Rational Integrals on Large Semicircles
 > Let $f(z)=\frac{p(z)}{q(z)}$, where degree $q(z) \geq 1+\operatorname{degree} p(z)$, Let $\sigma_{R}$ denote the semi-circular arc consisting of all $z=R e^{i \theta}$, where $0 \leq \theta \leq \pi$. Then $\lim _{R \rightarrow \infty} \int_{\sigma_{R}} e^{i s z} f(z) d z=0$, for all $s>0$.
 
 **proof** Let $M(R)$ denote the maximum of $|p(z) / q(z)|$ for $z$ on $\sigma_{R}$. Since degree $q(z) \geq 1+$ degree $p(z), M(R) \rightarrow 0$ as $R \rightarrow \infty$. Now apply Jordan's lemma. $\square$
@@ -252,7 +287,9 @@
 > $$
 > 
 
-**solution** Consider the contour integral over the closed semi-circle $\gamma_{R}$
+##### solution
+
+Consider the contour integral over the closed semi-circle $\gamma_{R}$
 
 $$
 I_{\gamma_{R}}=\int_{\sigma_{R}} \frac{z}{z^{2}+a^{2}} e^{i z} d z+\int_{-R}^{R} \frac{x}{x^{2}+a^{2}} e^{i x} d x=I_{\sigma_{R}}+I_{R}
@@ -263,10 +300,18 @@
 
 
 
-> [!figure] Figure 5
-> 
-> ![300](./images/b1ad9866-c636-4d3b-85cb-e1f2bdb2e560-29_517_463_354_64.jpg)
-> Figure 5 The path and poles for the contour integral in Example 2.
+```scientific-figure
+id: 102580e2-d2dd-494e-9bf2-6eb98776cc7a
+numbered: false
+title: ""
+caption: "**Figure 5.** The path and poles for the contour integral in Example 2."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 05 Residue Theory/images/b1ad9866-c636-4d3b-85cb-e1f2bdb2e560-29_517_463_354_64.jpg
+    caption: ""
+```
 
 
 
@@ -317,10 +362,18 @@
 
 
 
-> [!figure] Figure 6
-> 
-> ![300](./images/b1ad9866-c636-4d3b-85cb-e1f2bdb2e560-30_705_1429_190_678.jpg)
-> Figure 6 Splitting an improper integral.
+```scientific-figure
+id: 49cbaafc-f184-43a3-95c3-3a3375b617d5
+numbered: false
+title: ""
+caption: "**Figure 6.** Splitting an improper integral."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 05 Residue Theory/images/b1ad9866-c636-4d3b-85cb-e1f2bdb2e560-30_705_1429_190_678.jpg
+    caption: ""
+```
 
 
 
@@ -334,10 +387,18 @@
 
 
 
-> [!figure] Figure 7
-> 
-> ![300](./images/b1ad9866-c636-4d3b-85cb-e1f2bdb2e560-30_500_548_1216_128.jpg)
-> Figure 7 The Cauchy principal value.
+```scientific-figure
+id: 7b35e8ca-2c13-4807-81b9-8ca54cae814e
+numbered: false
+title: ""
+caption: "**Figure 7.** The Cauchy principal value."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 05 Residue Theory/images/b1ad9866-c636-4d3b-85cb-e1f2bdb2e560-30_500_548_1216_128.jpg
+    caption: ""
+```
 
 
 
@@ -363,7 +424,9 @@
 > Write down P.V. $\int_{-\infty}^{\infty} \frac{1}{x-1} d x$ in terms of limits of integrals on finite intervals.
 
 
-**solution** The integral is improper because it extends over the infinite real line and because the integrand is singular at $x=1$. Accordingly, the principal value involves two limits; it is
+##### solution
+
+The integral is improper because it extends over the infinite real line and because the integrand is singular at $x=1$. Accordingly, the principal value involves two limits; it is
 
 $$
 \text { P.V. } \begin{aligned}
@@ -400,10 +463,18 @@
 
 
 
-> [!figure] Figure 8
-> 
-> ![300](./images/b1ad9866-c636-4d3b-85cb-e1f2bdb2e560-31_472_491_268_53.jpg)
-> Figure 8 The principal value of the integral in Example 3.
+```scientific-figure
+id: 0ec8cbed-8c31-44ed-88c4-db2eb25e913b
+numbered: false
+title: ""
+caption: "**Figure 8.** The principal value of the integral in Example 3."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 05 Residue Theory/images/b1ad9866-c636-4d3b-85cb-e1f2bdb2e560-31_472_491_268_53.jpg
+    caption: ""
+```
 
 
 ---
@@ -421,27 +492,42 @@
 
 
 
-> [!figure] Figure 9
-> 
-> ![300](./images/b1ad9866-c636-4d3b-85cb-e1f2bdb2e560-31_462_504_1755_46.jpg)
-> Figure 9 Bypassing the point $\theta$ with the contour $\gamma_{r, R}$.
-
-
-
-
+```scientific-figure
+id: 026aa84a-f3f1-4ff0-9e0c-1146a060b109
+numbered: false
+title: ""
+caption: "**Figure 9.** Bypassing the point $\\theta$ with the contour $\\gamma_{r, R}$."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 05 Residue Theory/images/b1ad9866-c636-4d3b-85cb-e1f2bdb2e560-31_462_504_1755_46.jpg
+    caption: ""
+```
+
+
+
+
+<!-- Source label: Shrinking Path Lemma -->
 > [!lemma] Shrinking Path Lemma
-> Suppose that $f(z)$ is a continuous complex-valued function on a closed disk $S_{r_{0}}\left(z_{0}\right)$ with center at $z_{0}$ and radius $r_{0}$. For $0<r \leq r_{0}$, let $\sigma_{r}$ denote the positively oriented circular arc at angle $\alpha$ (_Figure 10_), consisting of all $z=z_{0}+r e^{i \theta}$, where $\theta_{0} \leq \theta \leq \theta_{0}+\alpha, \theta_{0}$ and $\alpha$ are fixed, and $\alpha \neq 0$. Then
-> 
+> Suppose that $f(z)$ is a continuous complex-valued function on a closed disk $S_{r_{0}}\left(z_{0}\right)$ with center at $z_{0}$ and radius $r_{0}$. For $0<r \leq r_{0}$, let $\sigma_{r}$ denote the positively oriented circular arc at angle $\alpha$, consisting of all $z=z_{0}+r e^{i \theta}$, where $\theta_{0} \leq \theta \leq \theta_{0}+\alpha, \theta_{0}$ and $\alpha$ are fixed, and $\alpha>0$. Then
+>
 > $$
 > \lim _{r \rightarrow 0^{+}} \frac{1}{i \alpha} \int_{\sigma_{r}} \frac{f(z)}{z-z_{0}} d z=f\left(z_{0}\right)
 > $$
-> 
-> > [!figure] Figure 10
-> > 
-> > ![300](./images/b1ad9866-c636-4d3b-85cb-e1f2bdb2e560-32_474_533_494_107.jpg)
-> > Figure 10 Circular arc at angle $\alpha$.
-> 
-> 
+
+```scientific-figure
+id: cdb4997b-0242-4259-b495-7089be43f56f
+numbered: false
+title: ""
+caption: "**Figure 10.** Circular arc at angle $\\alpha$."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 05 Residue Theory/images/b1ad9866-c636-4d3b-85cb-e1f2bdb2e560-32_474_533_494_107.jpg
+    caption: ""
+```
 
 
 
@@ -466,14 +552,13 @@
 
 
 
-> [!corollary]
-> Suppose that $g(z)$ has a simple pole at $z_{0}$ and for $0<r \leq r_{0}$, let $\sigma_{r}$ denote the circular arc at angle $\alpha$ (_Figure 10_). Then
-> 
-> $$
-> \lim _{r \rightarrow 0^{+}} \int_{\sigma_{r}} g(z) d z=i \alpha \operatorname{Res}\left(g(z), z_{0}\right) \tag{16}
-> $$
-> 
-> 
+<!-- Source label:  -->
+> [!corollary] Shrinking Circular Arc Integral at a Simple Pole
+> Suppose that $g(z)$ has a simple pole at $z_{0}$ and for $0<r \leq r_{0}$, let $\sigma_{r}$ denote the counterclockwise arc $z=z_0+re^{i\theta}$, $\theta_0\leq\theta\leq\theta_0+\alpha$, where $\theta_0$ and $\alpha>0$ are fixed and $r_0>0$ is small enough that the punctured disk contains no other singularities. Then
+>
+> $$
+> \lim _{r \rightarrow 0^{+}} \int_{\sigma_{r}} g(z) d z=i \alpha \operatorname{Res}\left(g(z), z_{0}\right) 
+> $$
 
 **proof** Let $f(z)=\left(z-z_{0}\right) g(z)$ for $z \neq z_{0}$ and define $f\left(z_{0}\right)=\lim _{z \rightarrow z_{0}}\left(z-z_{0}\right) g(z)= \operatorname{Res}\left(g(z), z_{0}\right)$. Since $g(z)$ has a simple pole at $z_{0}$, it follows from Theorem 7. Section 4.6, that $f(z)$ is analytic at $z_{0}$. Now apply Lemma 2 to $f(z)$ and (16) follows from (15), since for $z \neq z_{0}, f(z) /\left(z-z_{0}\right)=g(z)$.
 
@@ -491,7 +576,9 @@
 > In particular, when $a=0$, the first integral yields $\int_{-\infty}^{\infty} \frac{\sin x}{x} d x=\pi$.
 
 
-**solution** The integrals are improper because the interval of integration is infinite
+##### solution
+
+The integrals are improper because the interval of integration is infinite
 
 
 
@@ -509,10 +596,18 @@
 
 
 
-> [!figure] Figure 11
-> 
-> ![300](./images/b1ad9866-c636-4d3b-85cb-e1f2bdb2e560-32_505_547_1914_103.jpg)
-> Figure 11 Principal value integral.
+```scientific-figure
+id: 7f41a494-703f-45c4-917d-f930580a9562
+numbered: false
+title: ""
+caption: "**Figure 11.** Principal value integral."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 05 Residue Theory/images/b1ad9866-c636-4d3b-85cb-e1f2bdb2e560-32_505_547_1914_103.jpg
+    caption: ""
+```
 
 
 
@@ -520,10 +615,18 @@
 
 
 
-> [!figure] Figure 12
-> 
-> ![300](./images/b1ad9866-c636-4d3b-85cb-e1f2bdb2e560-33_495_486_622_44.jpg)
-> Figure 12 Indenting a contour around $a$.
+```scientific-figure
+id: 7b55c25e-57a5-4222-b362-0b337fda5190
+numbered: false
+title: ""
+caption: "**Figure 12.** Indenting a contour around $a$."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 05 Residue Theory/images/b1ad9866-c636-4d3b-85cb-e1f2bdb2e560-33_495_486_622_44.jpg
+    caption: ""
+```
 
 
 The larger semi-circle $\sigma_{R}$ has radius $R$ and positive orientation. The smaller semi-circle has radius $r$; it is negatively oriented and we shall call it $-\sigma_{r}$. Since $f(z)$ is analytic on and inside $\gamma_{r, R}$, Cauchy's theorem implies that
@@ -650,10 +753,18 @@
 > (a) Let $f(z)=\frac{e^{(\pi+i w) z}}{e^{2 \pi z}+1}$ and let $\gamma_{\epsilon, R}$ denote the indented contour in _Figure 13_. 
 > 
 > 
-> > [!figure] Figure 13
-> > 
-> > ![300](./images/b1ad9866-c636-4d3b-85cb-e1f2bdb2e560-35_443_435_444_58.jpg)
-> > Figure 13 Indented contour for problem 24.
+> ```scientific-figure
+> id: 455dc405-6283-4ffc-b1e9-738b4dbdff8a
+> numbered: false
+> title: ""
+> caption: "**Figure 13.** Indented contour for problem 24."
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 05 Residue Theory/images/b1ad9866-c636-4d3b-85cb-e1f2bdb2e560-35_443_435_444_58.jpg
+>     caption: ""
+> ```
 > 
 > 
 > 
@@ -699,10 +810,18 @@
 > 
 > 
 > 
-> > [!figure] Figure 14
-> > 
-> > ![300](./images/b1ad9866-c636-4d3b-85cb-e1f2bdb2e560-35_452_427_1684_46.jpg)
-> > Figure 14 Indented contour for problem 25.
+> ```scientific-figure
+> id: 671979d2-72ee-4e08-ac8b-cd155487d95e
+> numbered: false
+> title: ""
+> caption: "**Figure 14.** Indented contour for problem 25."
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 05 Residue Theory/images/b1ad9866-c636-4d3b-85cb-e1f2bdb2e560-35_452_427_1684_46.jpg
+>     caption: ""
+> ```
 > 
 > 
 > 
@@ -725,4 +844,4 @@
 > $$
 > 
 > (The diligent reader can justify the interchange of the sum and the integral.)
-> +> 

`````
