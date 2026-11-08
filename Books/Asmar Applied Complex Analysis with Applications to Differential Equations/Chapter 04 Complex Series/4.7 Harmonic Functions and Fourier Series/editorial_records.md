
# Editorial records

Reading note: 4.7 Harmonic Functions and Fourier Series.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Callout 200: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!lemma] Fourier Series of the Poisson Kernel for a Disk
> Let $R>0$ and define the disk Poisson kernel by $P(r,\theta)=(R^2-r^2)/(R^2-2rR\cos\theta+r^2)$.
>
> For $0 \leq r<R$ and all $\theta$, we have
>
> $$
> P(r, \theta)=\operatorname{Re}\left(\frac{R+r e^{i \theta}}{R-r e^{i \theta}}\right)=1+2 \sum_{n=1}^{\infty}\left(\frac{r}{R}\right)^{n} \cos n \theta .
> $$
````
### After

````text
> [!lemma] Series Form of the Poisson Kernel
> Let $R>0$ and define the disk Poisson kernel by $P(r,\theta)=(R^2-r^2)/(R^2-2rR\cos\theta+r^2)$.
>
> For $0 \leq r<R$ and all $\theta$, we have
>
> $$
> P(r, \theta)=\operatorname{Re}\left(\frac{R+r e^{i \theta}}{R-r e^{i \theta}}\right)=1+2 \sum_{n=1}^{\infty}\left(\frac{r}{R}\right)^{n} \cos n \theta .
> $$
````

## 2. Callout 201: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Fourier Series Representation of the Poisson Extension on a Disk
> Let $R>0$ and let $f$ be real-valued, $2\pi$-periodic, and piecewise continuous. Its Poisson extension is harmonic in $|z|<R$, approaches $f(\theta)$ radially at continuity points, and is given by
> $\quad u(r, \theta)=a_{0}+\sum_{n=1}^{\infty}\left(\frac{r}{R}\right)^{n}\left(a_{n} \cos n \theta+b_{n} \sin n \theta\right), \quad 0 \leq r<R$,
> where $a_{0}, a_{n}$, and $b_{n}$ are the Fourier coefficients of $f$, given by the following:
>
> $$a_0=\frac{1}{2 \pi} \int_0^{2 \pi} f(\theta) d \theta; $$
> $$
> a_n=\frac{1}{\pi} \int_0^{2 \pi} f(\theta) \cos n \theta d \theta \quad(n=1,2, \ldots); 
> $$
>
> $$
> b_n=\frac{1}{\pi} \int_0^{2 \pi} f(\theta) \sin n \theta d \theta \quad(n=1,2, \ldots). 
> $$
````
### After

````text
> [!theorem] Fourier Series Form of the Poisson Integral Formula
> Let $R>0$ and let $f$ be real-valued, $2\pi$-periodic, and piecewise continuous. Its Poisson extension is harmonic in $|z|<R$, approaches $f(\theta)$ radially at continuity points, and is given by
> $\quad u(r, \theta)=a_{0}+\sum_{n=1}^{\infty}\left(\frac{r}{R}\right)^{n}\left(a_{n} \cos n \theta+b_{n} \sin n \theta\right), \quad 0 \leq r<R$,
> where $a_{0}, a_{n}$, and $b_{n}$ are the Fourier coefficients of $f$, given by the following:
>
> $$a_0=\frac{1}{2 \pi} \int_0^{2 \pi} f(\theta) d \theta; $$
> $$
> a_n=\frac{1}{\pi} \int_0^{2 \pi} f(\theta) \cos n \theta d \theta \quad(n=1,2, \ldots); 
> $$
>
> $$
> b_n=\frac{1}{\pi} \int_0^{2 \pi} f(\theta) \sin n \theta d \theta \quad(n=1,2, \ldots). 
> $$
````

## Source-to-current comparison

Source: /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 04 Complex Series/4.7 Harmonic Functions and Fourier Series.md

This exact comparison preserves the full change evidence, including formatting, OCR corrections, restored source wording, and required standalone context. The entries above explain the recovery edits. The comparison is not a claim that every difference is a correction; component serialization, callout wrapping, and printed labels outside callouts are formatting.

`````diff
--- /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 04 Complex Series/4.7 Harmonic Functions and Fourier Series.md
+++ /Users/gradyclopton/ObsidianVaults/complex_analysis/Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 04 Complex Series/4.7 Harmonic Functions and Fourier Series.md
@@ -21,10 +21,18 @@
 
 
 
-> [!figure] Figure 1
-> 
-> ![300](./images/5443c314-b89d-4dd1-b950-bb21550520a5-73_492_487_681_69.jpg)
-> Figure 1 A Dirichlet problem on a disk with radius $R>0$ and center at the origin.
+```scientific-figure
+id: 28f96847-8798-4627-9476-9496b6950738
+numbered: false
+title: ""
+caption: "**Figure 1.** A Dirichlet problem on a disk with radius $R>0$ and center at the origin."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 04 Complex Series/images/5443c314-b89d-4dd1-b950-bb21550520a5-73_492_487_681_69.jpg
+    caption: ""
+```
 
 
 
@@ -42,14 +50,15 @@
 
 
 
-> [!lemma] Lemma 1 Series Form of the Poisson Kernel
+<!-- Source label: Lemma 1 Series Form of the Poisson Kernel -->
+> [!lemma] Series Form of the Poisson Kernel
+> Let $R>0$ and define the disk Poisson kernel by $P(r,\theta)=(R^2-r^2)/(R^2-2rR\cos\theta+r^2)$.
+>
 > For $0 \leq r<R$ and all $\theta$, we have
-> (5)
-> 
+>
 > $$
 > P(r, \theta)=\operatorname{Re}\left(\frac{R+r e^{i \theta}}{R-r e^{i \theta}}\right)=1+2 \sum_{n=1}^{\infty}\left(\frac{r}{R}\right)^{n} \cos n \theta .
 > $$
-> 
 
 **proof** Using $\overline{R-r e^{i \theta}}=R-r e^{-i \theta}$, we obtain
 
@@ -96,21 +105,20 @@
 THEOREM 1 FOURIER SERIES FORM OF THE POISSON INTEGRAL FORMULA
 
 
-> [!theorem] Theorem 1: Fourier Series Form of the Poisson Integral Formula
-> Consider the Dirichlet problem (1)-(2) with piecewise continuous boundary data $f$. Then the **solution** is given by
-> (9) $\quad u(r, \theta)=a_{0}+\sum_{n=1}^{\infty}\left(\frac{r}{R}\right)^{n}\left(a_{n} \cos n \theta+b_{n} \sin n \theta\right), \quad 0 \leq r<R$,
+<!-- Source label: Theorem 1: Fourier Series Form of the Poisson Integral Formula -->
+> [!theorem] Fourier Series Form of the Poisson Integral Formula
+> Let $R>0$ and let $f$ be real-valued, $2\pi$-periodic, and piecewise continuous. Its Poisson extension is harmonic in $|z|<R$, approaches $f(\theta)$ radially at continuity points, and is given by
+> $\quad u(r, \theta)=a_{0}+\sum_{n=1}^{\infty}\left(\frac{r}{R}\right)^{n}\left(a_{n} \cos n \theta+b_{n} \sin n \theta\right), \quad 0 \leq r<R$,
 > where $a_{0}, a_{n}$, and $b_{n}$ are the Fourier coefficients of $f$, given by the following:
-> 
-> $$a_0=\frac{1}{2 \pi} \int_0^{2 \pi} f(\theta) d \theta; \tag{6}$$
-> $$
-> a_n=\frac{1}{\pi} \int_0^{2 \pi} f(\theta) \cos n \theta d \theta \quad(n=1,2, \ldots); \tag{7}
-> $$
-> 
-> $$
-> b_n=\frac{1}{\pi} \int_0^{2 \pi} f(\theta) \sin n \theta d \theta \quad(n=1,2, \ldots). \tag{8}
-> $$
-> 
-> 
+>
+> $$a_0=\frac{1}{2 \pi} \int_0^{2 \pi} f(\theta) d \theta; $$
+> $$
+> a_n=\frac{1}{\pi} \int_0^{2 \pi} f(\theta) \cos n \theta d \theta \quad(n=1,2, \ldots); 
+> $$
+>
+> $$
+> b_n=\frac{1}{\pi} \int_0^{2 \pi} f(\theta) \sin n \theta d \theta \quad(n=1,2, \ldots). 
+> $$
 
 
 **proof** Starting with the **solution** (3), we expand the Poisson integral in a series by using (5) (replace $\theta$ by $\theta-\phi$ in (5)) and get
@@ -157,15 +165,25 @@
 > (b) Show that all the points inside the plate on the $x$-axis have the same temperature. What is this temperature?
 
 
-> [!figure] Figure 2
-> 
-> ![300](./images/5443c314-b89d-4dd1-b950-bb21550520a5-75_555_464_1699_57.jpg)
-> Figure 2 Dirichlet problem in Example 1.
-
-
-
-
-**solution** (a) According to (9), the **solution** inside the disk is given by
+```scientific-figure
+id: 0ce75df1-18e4-413c-b12c-0d790fb3a26c
+numbered: false
+title: ""
+caption: "**Figure 2.** Dirichlet problem in Example 1."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 04 Complex Series/images/5443c314-b89d-4dd1-b950-bb21550520a5-75_555_464_1699_57.jpg
+    caption: ""
+```
+
+
+
+
+##### solution
+
+(a) According to (9), the **solution** inside the disk is given by
 
 $$
 u(r, \theta)=a_{0}+\sum_{n=1}^{\infty}\left(\frac{r}{2}\right)^{n}\left(a_{n} \cos n \theta+b_{n} \sin n \theta\right), \quad 0 \leq r<2
@@ -212,13 +230,11 @@
 Suppose for a moment that we can take the limit inside the infinite sum. Then because $\lim _{r \uparrow R}\left(\frac{r}{R}\right)^{n}=1$ for all $n$, we get
 
 
-> [!equation]
-> 
+<!-- Source label:  -->
+> [!equation] Formal Fourier Expansion from Boundary Values of a Poisson Integral
 > $$
 > f(\theta)=a_{0}+\sum_{n=1}^{\infty}\left(a_{n} \cos n \theta+b_{n} \sin n \theta\right)
 > $$
-> 
-> 
 
 
 
@@ -246,10 +262,18 @@
 The boundary function in Example 1 is plotted in _Figure 3_. 
 
 
-> [!figure] Figure 3
-> 
-> ![300](./images/5443c314-b89d-4dd1-b950-bb21550520a5-77_384_473_1214_68.jpg)
-> Figure 3 The boundary function in Example 1, as a $2 \pi$ periodic function of $\theta$.
+```scientific-figure
+id: f177c6e3-2aa6-4e44-9d2e-5daa4f746e7c
+numbered: false
+title: ""
+caption: "**Figure 3.** The boundary function in Example 1, as a $2 \\pi$ periodic function of $\\theta$."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 04 Complex Series/images/5443c314-b89d-4dd1-b950-bb21550520a5-77_384_473_1214_68.jpg
+    caption: ""
+```
 
 
 
@@ -282,10 +306,18 @@
 
 
 
-> [!figure] Figure 4
-> 
-> ![300](./images/5443c314-b89d-4dd1-b950-bb21550520a5-78_575_1434_172_643.jpg)
-> Figure 4. Partial sums of the Fourier series: $s_{n}(\theta)= 50+\frac{200}{\pi} \sum_{k=0}^{n} \frac{\sin (2 k+1) \theta}{2 k+1}$, for $n=1,3,10$. As $n$ increases, the frequencies of the sine terms increase, causing the graphs of the higher partial sums to be more wiggly.
+```scientific-figure
+id: c9b3d545-d68f-4e08-af85-09b3b2d7553b
+numbered: false
+title: ""
+caption: "**Figure 4.** Partial sums of the Fourier series: $s_{n}(\\theta)= 50+\\frac{200}{\\pi} \\sum_{k=0}^{n} \\frac{\\sin (2 k+1) \\theta}{2 k+1}$, for $n=1,3,10$. As $n$ increases, the frequencies of the sine terms increase, causing the graphs of the higher partial sums to be more wiggly."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 04 Complex Series/images/5443c314-b89d-4dd1-b950-bb21550520a5-78_575_1434_172_643.jpg
+    caption: ""
+```
 
 
 
@@ -306,10 +338,18 @@
 
 
 
-> [!figure] Figure 5
-> 
-> ![300](./images/5443c314-b89d-4dd1-b950-bb21550520a5-78_365_557_1127_105.jpg)
-> Figure 5 Graph of the Fourier series of a piecewise smooth function in Example 2. It agrees with the function at all the points where $f(\theta)$ is continuous.
+```scientific-figure
+id: 6081d052-7989-4d06-8b69-e22eb32a4148
+numbered: false
+title: ""
+caption: "**Figure 5.** Graph of the Fourier series of a piecewise smooth function in Example 2. It agrees with the function at all the points where $f(\\theta)$ is continuous."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 04 Complex Series/images/5443c314-b89d-4dd1-b950-bb21550520a5-78_365_557_1127_105.jpg
+    caption: ""
+```
 
 
 

`````
