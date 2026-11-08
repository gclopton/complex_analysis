
# Editorial records

Reading note: 4.5 Laurent Series.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Callout 185: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Laurent Expansion on a Complex Annulus
> Write $A_{R_1,R_2}(z_0)=\{z\in\mathbb C:R_1<|z-z_0|<R_2\}$.
>
> Suppose that $f$ is analytic in the annulus $A_{R_{1}, R_{2}}\left(z_{0}\right)$ where $0 \leq R_{1}<R_{2} \leq \infty$. Then $f$ has a unique Laurent series representation
>
> $$
> f(z)=\sum_{n=0}^{\infty} a_{n}\left(z-z_{0}\right)^{n}+\sum_{n=1}^{\infty} \frac{a_{-n}}{\left(z-z_{0}\right)^{n}}, \quad R_{1}<\left|z-z_{0}\right|<R_{2},
> $$
>
> where the Laurent coefficients are given by
>
> $$
> a_{n}=\frac{1}{2 \pi i} \int_{C_{R}\left(z_{0}\right)} \frac{f(\zeta)}{\left(\zeta-z_{0}\right)^{n+1}} d \zeta \quad(n=0, \pm 1, \pm 2, \ldots)
> $$
>
> with $R_{1}<R<R_{2}$ and $C_{R}\left(z_{0}\right)$ is any positively oriented circle centered at $z_{0}$ and contained in $A_{R_{1}, R_{2}}\left(z_{0}\right)$. The Laurent series converges absolutely for all $z$ in $A_{R_{1}, R_{2}}\left(z_{0}\right)$ and uniformly on any closed subannulus $R_{1}<\rho_{1} \leq \left|z-z_{0}\right| \leq \rho_{2}<R_{2}$.
````
### After

````text
> [!theorem] Laurent Series
> Write $A_{R_1,R_2}(z_0)=\{z\in\mathbb C:R_1<|z-z_0|<R_2\}$.
>
> Suppose that $f$ is analytic in the annulus $A_{R_{1}, R_{2}}\left(z_{0}\right)$ where $0 \leq R_{1}<R_{2} \leq \infty$. Then $f$ has a unique Laurent series representation
>
> $$
> f(z)=\sum_{n=0}^{\infty} a_{n}\left(z-z_{0}\right)^{n}+\sum_{n=1}^{\infty} \frac{a_{-n}}{\left(z-z_{0}\right)^{n}}, \quad R_{1}<\left|z-z_{0}\right|<R_{2},
> $$
>
> where the Laurent coefficients are given by
>
> $$
> a_{n}=\frac{1}{2 \pi i} \int_{C_{R}\left(z_{0}\right)} \frac{f(\zeta)}{\left(\zeta-z_{0}\right)^{n+1}} d \zeta \quad(n=0, \pm 1, \pm 2, \ldots)
> $$
>
> with $R_{1}<R<R_{2}$ and $C_{R}\left(z_{0}\right)$ is any positively oriented circle centered at $z_{0}$ and contained in $A_{R_{1}, R_{2}}\left(z_{0}\right)$. The Laurent series converges absolutely for all $z$ in $A_{R_{1}, R_{2}}\left(z_{0}\right)$ and uniformly on any closed subannulus $R_{1}<\rho_{1} \leq \left|z-z_{0}\right| \leq \rho_{2}<R_{2}$.
````

## Source-to-current comparison

Source: /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 04 Complex Series/4.5 Laurent Series.md

This exact comparison preserves the full change evidence, including formatting, OCR corrections, restored source wording, and required standalone context. The entries above explain the recovery edits. The comparison is not a claim that every difference is a correction; component serialization, callout wrapping, and printed labels outside callouts are formatting.

`````diff
--- /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 04 Complex Series/4.5 Laurent Series.md
+++ /Users/gradyclopton/ObsidianVaults/complex_analysis/Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 04 Complex Series/4.5 Laurent Series.md
@@ -16,10 +16,18 @@
 See _Figure 1_ for an illustration where $R_{1}$ and $R_{2}$ are nonzero and finite. 
 
 
-> [!figure] Figure 1
-> 
-> ![300](./images/5443c314-b89d-4dd1-b950-bb21550520a5-49_451_382_1761_42.jpg)
-> Figure 1 The annulus $A_{\mathrm{P}_{1}, \mathrm{R}_{2}}\left(z_{0}\right)$ centered at $z_{0}$ with inner radius $R_{1}$ and outer radius $R_{2}$.
+```scientific-figure
+id: 753df087-bfd5-4f88-8fc9-b7425792584c
+numbered: false
+title: ""
+caption: "**Figure 1.** The annulus $A_{\\mathrm{P}_{1}, \\mathrm{R}_{2}}\\left(z_{0}\\right)$ centered at $z_{0}$ with inner radius $R_{1}$ and outer radius $R_{2}$."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 04 Complex Series/images/5443c314-b89d-4dd1-b950-bb21550520a5-49_451_382_1761_42.jpg
+    caption: ""
+```
 
 
 Note that the annulus $A_{R_{1}, R_{2}}\left(z_{0}\right)$ can degenerate into a punctured disk with $z_{0}$ removed $\left(R_{1}=0\right.$ and $\left.R_{2}<\infty\right)$, a punctured plane with $z_{0}$ removed $\left(R_{1}=0\right.$, $R_{2}=\infty$ ), or a plane with a disk centered at $z_{0}$ cut out of it ( $0<R_{1}$ and $R_{2}=\infty$ ). These sets still count as annuli by our definition.
@@ -27,29 +35,40 @@
 
 
 
-> [!theorem] Theorem 1: Laurent Series
+<!-- Source label: Theorem 1: Laurent Series -->
+> [!theorem] Laurent Series
+> Write $A_{R_1,R_2}(z_0)=\{z\in\mathbb C:R_1<|z-z_0|<R_2\}$.
+>
 > Suppose that $f$ is analytic in the annulus $A_{R_{1}, R_{2}}\left(z_{0}\right)$ where $0 \leq R_{1}<R_{2} \leq \infty$. Then $f$ has a unique Laurent series representation
-> 
+>
 > $$
 > f(z)=\sum_{n=0}^{\infty} a_{n}\left(z-z_{0}\right)^{n}+\sum_{n=1}^{\infty} \frac{a_{-n}}{\left(z-z_{0}\right)^{n}}, \quad R_{1}<\left|z-z_{0}\right|<R_{2},
 > $$
-> 
+>
 > where the Laurent coefficients are given by
-> 
+>
 > $$
 > a_{n}=\frac{1}{2 \pi i} \int_{C_{R}\left(z_{0}\right)} \frac{f(\zeta)}{\left(\zeta-z_{0}\right)^{n+1}} d \zeta \quad(n=0, \pm 1, \pm 2, \ldots)
 > $$
-> 
+>
 > with $R_{1}<R<R_{2}$ and $C_{R}\left(z_{0}\right)$ is any positively oriented circle centered at $z_{0}$ and contained in $A_{R_{1}, R_{2}}\left(z_{0}\right)$. The Laurent series converges absolutely for all $z$ in $A_{R_{1}, R_{2}}\left(z_{0}\right)$ and uniformly on any closed subannulus $R_{1}<\rho_{1} \leq \left|z-z_{0}\right| \leq \rho_{2}<R_{2}$.
 
 Proof Given $z$ in the annulus $A_{R_{1}, R_{2}}\left(z_{0}\right)$, we can find $r_{1}, r_{2}$ and $\rho$ so that $R_{1}< r_{1}<r_{2}<R_{2}$ and $C_{\rho}(z)$ is contained in $A_{r_{1}, r_{2}}\left(z_{0}\right)$ (see _Figure 2_). 
 
 
 
-> [!figure] Figure 2
-> 
-> ![300](./images/5443c314-b89d-4dd1-b950-bb21550520a5-50_488_533_1335_107.jpg)
-> Figure 2 The function $\zeta \mapsto \frac{f(\zeta)}{\zeta-z}$ is analytic inside and on the boundary of the shaded area.
+```scientific-figure
+id: 5be856cc-d032-408c-bfc7-8fe3bac036a6
+numbered: false
+title: ""
+caption: "**Figure 2.** The function $\\zeta \\mapsto \\frac{f(\\zeta)}{\\zeta-z}$ is analytic inside and on the boundary of the shaded area."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 04 Complex Series/images/5443c314-b89d-4dd1-b950-bb21550520a5-50_488_533_1335_107.jpg
+    caption: ""
+```
 
 
 The function $\zeta \mapsto \frac{f(\zeta)}{\zeta-z}$ is analytic inside and on the boundary of the region outside $C_{\rho}(z)$ and inside $A_{r_{1}, r_{2}}\left(z_{0}\right)$. So by Cauchy's theorem for multiply connected regions (Theorem 6, Section 3.4), we have
@@ -105,7 +124,9 @@
 
 
 
-**Solution** (a) Start with the exponential series $e^{z}=\sum_{n=0}^{\infty} \frac{z^{n}}{n!}$, which is valid for all $z$. In particular, if $z \neq 0$, putting $\frac{1}{z}$ into this series, we obtain
+##### solution
+
+(a) Start with the exponential series $e^{z}=\sum_{n=0}^{\infty} \frac{z^{n}}{n!}$, which is valid for all $z$. In particular, if $z \neq 0$, putting $\frac{1}{z}$ into this series, we obtain
 
 $$
 e^{\frac{1}{n}}=\sum_{n=0}^{\infty} \frac{1}{n!z^{n}}=1+\sum_{n=1}^{\infty} \frac{1}{n!z^{n}}=1+\frac{1}{1!z}+\frac{1}{2!z^{2}}+\frac{1}{3!z^{3}}+\cdots
@@ -130,12 +151,13 @@
 
 Combining Example 1(b) with the geometric series, we obtain the following useful identities:
 
-> [!equation]
-> 
+<!-- Source label:  -->
+> [!identity] Geometric Series Expansions Inside and Outside the Unit Circle
+> For $w\in\mathbb C$ with $|w|\neq1$,
+>
 > $$
 > \frac{1}{1-w}= \begin{cases}\sum_{n=0}^{\infty} w^{n} & \text { if }|w|<1, \\ -\sum_{n=1}^{\infty} \frac{1}{w^{n}} & \text { if } 1<|w| .\end{cases}
 > $$
-> 
 
 Here is an application.
 
@@ -146,15 +168,25 @@
 > 
 > 
 > 
-> > [!figure] Figure 3
-> > 
-> > ![300](./images/5443c314-b89d-4dd1-b950-bb21550520a5-52_415_428_1233_116.jpg)
-> > Figure 3 The function $f(z)=\frac{1}{z-6}$ is analytic in the annulus $2<|z-4|$ and so has a Laurent series expansion there.
-> 
-> 
-> 
-
-**Solution** Since we are expanding around 4, we need to see the expression $(z-4)$ in the denominator of $f$. For this purpose, and in order to apply (5), let us write
+> ```scientific-figure
+> id: b4b733fa-f631-417c-9348-677c6d87eff0
+> numbered: false
+> title: ""
+> caption: "**Figure 3.** The function $f(z)=\\frac{1}{z-6}$ is analytic in the annulus $2<|z-4|$ and so has a Laurent series expansion there."
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 04 Complex Series/images/5443c314-b89d-4dd1-b950-bb21550520a5-52_415_428_1233_116.jpg
+>     caption: ""
+> ```
+> 
+> 
+> 
+
+##### solution
+
+Since we are expanding around 4, we need to see the expression $(z-4)$ in the denominator of $f$. For this purpose, and in order to apply (5), let us write
 
 $$
 \frac{1}{z-6}=\frac{1}{(z-4)-2}=-\frac{1}{2} \frac{1}{1-\frac{z-4}{2}}=-\frac{1}{2} \frac{1}{1-w}
@@ -178,7 +210,9 @@
 > Find the Laurent series expansion of $f(z)=\frac{3 z^{2}-2 z+4}{z-6}$ in the annulus $2<|z-4|$ of the previous example.
 
 
-**Solution** Since the degree of the numerator is larger than the degree of the denominator, the first step is to divide the numerator by the denominator:
+##### solution
+
+Since the degree of the numerator is larger than the degree of the denominator, the first step is to divide the numerator by the denominator:
 
 $$
 \frac{3 z^{2}-2 z+4}{z-6}=3 z+16+\frac{100}{z-6}
@@ -212,13 +246,23 @@
 > Find all the Laurent series expansions of $f(z)=\frac{3}{(1+z)(2-z)}$ around $z_{0}=0$.
 
 
-**Solution** This problem has two parts. First we must determine how many different Laurent series expansions $f$ has around 0 . Then we must find these Laurent series. To answer the first question, we ask ourselves, what are the largest disjoint annular regions around $z_{0}=0$ on which $f$ is analytic? The function $f$ is analytic at all points except at $z=-1$ and $z=2$. So the desired regions around 0 on which $f$ is analytic are $|z|<1 ; 1<|z|<2$; and $2<|z|$ (_Figure 4_).
-
-
-> [!figure] Figure 4
-> 
-> ![300](./images/5443c314-b89d-4dd1-b950-bb21550520a5-53_531_481_1215_48.jpg)
-> Figure 4 The function $f(z)=\frac{3}{(1+z)(2-z)}$ is not analytic at $z=-1$ and $z=2$. It has three Laurent series expansions around 0 .
+##### solution
+
+This problem has two parts. First we must determine how many different Laurent series expansions $f$ has around 0 . Then we must find these Laurent series. To answer the first question, we ask ourselves, what are the largest disjoint annular regions around $z_{0}=0$ on which $f$ is analytic? The function $f$ is analytic at all points except at $z=-1$ and $z=2$. So the desired regions around 0 on which $f$ is analytic are $|z|<1 ; 1<|z|<2$; and $2<|z|$ (_Figure 4_).
+
+
+```scientific-figure
+id: c55dc3a0-33b8-4788-b30d-2153b0d9ca54
+numbered: false
+title: ""
+caption: "**Figure 4.** The function $f(z)=\\frac{3}{(1+z)(2-z)}$ is not analytic at $z=-1$ and $z=2$. It has three Laurent series expansions around 0 ."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 04 Complex Series/images/5443c314-b89d-4dd1-b950-bb21550520a5-53_531_481_1215_48.jpg
+    caption: ""
+```
 
 
 
@@ -291,14 +335,24 @@
 > Determine the largest annulus around $z_{0}=i$ of the form $R_{1}<|z-i|<R_{2}$ on which the function $f(z)=\frac{1}{1+z^{2}}$ has a Laurent series and then find the Laurent series.
 
 
-**Solution** The function $\frac{1}{1+z^{2}}$ is analytic at all $z$ except $z= \pm i$. It has a Laurent series in the largest annulus around $i$ on which it is analytic. In order to avoid the singularity at $-i$, we take the annulus $0<|z-i|<2$ (_Figure 5_). 
-
-
-
-> [!figure] Figure 5
-> 
-> ![300](./images/5443c314-b89d-4dd1-b950-bb21550520a5-54_412_483_1768_85.jpg)
-> Figure 5 The largest annulus around $i$ on which $f(z)= \frac{1}{1+z^{2}}$ has a Laurent series expansion.
+##### solution
+
+The function $\frac{1}{1+z^{2}}$ is analytic at all $z$ except $z= \pm i$. It has a Laurent series in the largest annulus around $i$ on which it is analytic. In order to avoid the singularity at $-i$, we take the annulus $0<|z-i|<2$ (_Figure 5_). 
+
+
+
+```scientific-figure
+id: c61cfe29-7bfc-481e-bdb3-e740043eedf7
+numbered: false
+title: ""
+caption: "**Figure 5.** The largest annulus around $i$ on which $f(z)= \\frac{1}{1+z^{2}}$ has a Laurent series expansion."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 04 Complex Series/images/5443c314-b89d-4dd1-b950-bb21550520a5-54_412_483_1768_85.jpg
+    caption: ""
+```
 
 
 We have $\frac{1}{1+z^{2}}=\frac{1}{z-7} \frac{1}{x+1}$. Since we are expanding in terms of $(z-i)$, the factor $\frac{1}{z-1}$ is already in a desirable form, and so we keep it as is and work on the factor $\frac{1}{z+i}$. To make $(z-i)$ appear in the latter factor, we add and subtract $i$ from the denominator. Thus
@@ -343,15 +397,25 @@
 > Find the Laurent series for $f(z)=\frac{1}{(1-z)^{3}}$ in the annulus $1<|z|$ (_Figure 6_).
 > 
 > 
-> > [!figure] Figure 6
-> > 
-> > ![300](./images/5443c314-b89d-4dd1-b950-bb21550520a5-55_459_467_1960_43.jpg)
-> > Figure 6 The annulus $1<|z|$ in Example 6.
-> 
-> 
-> 
-
-**Solution** Starting with the Laurent series
+> ```scientific-figure
+> id: 75cb19d8-06f6-468f-8130-2eafaf7de076
+> numbered: false
+> title: ""
+> caption: "**Figure 6.** The annulus $1<|z|$ in Example 6."
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 04 Complex Series/images/5443c314-b89d-4dd1-b950-bb21550520a5-55_459_467_1960_43.jpg
+>     caption: ""
+> ```
+> 
+> 
+> 
+
+##### solution
+
+Starting with the Laurent series
 
 $$
 \frac{1}{1-z}=-\sum_{n=1}^{\infty} \frac{1}{z^{n}}, \quad 1<|z|
@@ -381,7 +445,9 @@
 > (a) $\int_{C_{1}(0)} \frac{e^{\frac{1}{z}}}{z} d z$,
 > (b) $\int_{C_{1}(0)} e^{z+\frac{1}{z}} d z$.
 
-**Solution** Note that the integrands are continuous on the path of integration. So the integrals do exist; however, they cannot be computed using Cauchy's theorem because of the problem at $z=0$, which lies inside the path. The idea is to expand the integrand (or part of the integrand) in a Laurent series in an annulus that contains the path, and then integrate term by term.
+##### solution
+
+Note that the integrands are continuous on the path of integration. So the integrals do exist; however, they cannot be computed using Cauchy's theorem because of the problem at $z=0$, which lies inside the path. The idea is to expand the integrand (or part of the integrand) in a Laurent series in an annulus that contains the path, and then integrate term by term.
 (a) In the annulus $0<|z|$, we have
 
 $$
@@ -565,10 +631,18 @@
 > 
 > 
 > 
-> > [!figure] Figure 7
-> > 
-> > ![300](./images/5443c314-b89d-4dd1-b950-bb21550520a5-59_442_480_1211_64.jpg)
-> > Figure 7 Bessel functions $J_{n}(x)$, for $n=0,1,2$.
-> 
-> 
-> +> ```scientific-figure
+> id: e4dedea1-3cf0-4b36-8f9c-97a7e82c53ba
+> numbered: false
+> title: ""
+> caption: "**Figure 7.** Bessel functions $J_{n}(x)$, for $n=0,1,2$."
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 04 Complex Series/images/5443c314-b89d-4dd1-b950-bb21550520a5-59_442_480_1211_64.jpg
+>     caption: ""
+> ```
+> 
+> 
+> 

`````

## Additional source comparison

## 1. Repair Markdown display boundary: place closing display delimiter on its own line and end-of-proof square in following paragraph. No mathematical content or author wording changed.

### Before

````text
$$ $\square$
````
### After

````text
$$

$\square$
````
