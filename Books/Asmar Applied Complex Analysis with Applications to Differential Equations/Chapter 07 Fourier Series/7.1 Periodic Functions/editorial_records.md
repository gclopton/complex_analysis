
# Editorial records

Reading note: 7.1 Periodic Functions.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Callout 252: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Translation Invariance of the Integral over One Period
> Suppose that $T>0$ and $f$ is a locally integrable $T$-periodic function. Then, for any real number $a$, we have
>
> $$
> \int_0^T f(x) d x=\int_a^{a+T} f(x) d x
> $$
````
### After

````text
> [!theorem] Integral over One Period
> Suppose that $T>0$ and $f$ is a locally integrable $T$-periodic function. Then, for any real number $a$, we have
>
> $$
> \int_0^T f(x) d x=\int_a^{a+T} f(x) d x
> $$
````

## 2. Move editorial commentary out of the reading note.

### Before

````text
*Editorial corrections to source details: The fundamental period is defined when a least positive period exists; the integral proof states the almost-everywhere derivative required for locally integrable functions.*
````
### After

````text

````

## Source-to-current comparison

Source: /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 07 Fourier Series/7.1 Periodic Functions.md

This exact comparison preserves the full change evidence, including formatting, OCR corrections, restored source wording, and required standalone context. The entries above explain the recovery edits. The comparison is not a claim that every difference is a correction; component serialization, callout wrapping, and printed labels outside callouts are formatting.

`````diff
--- /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 07 Fourier Series/7.1 Periodic Functions.md
+++ /Users/gradyclopton/ObsidianVaults/complex_analysis/Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 07 Fourier Series/7.1 Periodic Functions.md
@@ -15,14 +15,20 @@
 In this chapter, we will present basic properties of Fourier series that will be used throughout the rest of the book.
 
 
-
 One of the problems that we have discussed at length in previous sections was the Dirichlet problem on a disk of radius $R>0$, centered at the origin. In such a problem, we are supposed to solve Laplace's equation inside the disk, given the values of the function on the boundary of the disk. Using polar coordinates, the boundary data was given by a function $f(\theta)$ of the polar angle $\theta$. Because $\theta$ and $\theta+2 \pi$ correspond to the same point on the unit circle, we have $f(\theta)=f(\theta+2 \pi)$. In other words, the function $f$ is $2 \pi$-periodic (Figure 1). 
 
-> [!figure] Figure 1
-> 
-> ![](Screenshot%202026-04-21%20at%2011.30.40%20PM.png)
-> Figure 1 The boundary function $f(\theta)$ in a Dirichlet problem on a disk centered at the origin is $2 \pi$-periodic.
-
+```scientific-figure
+id: 5885ab5a-8a5f-47e1-9659-c7d4b7336aff
+numbered: false
+title: ""
+caption: "**Figure 1.** The boundary function $f(\\theta)$ in a Dirichlet problem on a disk centered at the origin is $2 \\pi$-periodic."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 07 Fourier Series/images/Screenshot 2026-04-21 at 11.30.40 PM.png
+    caption: ""
+```
 
 
 Periodic functions will arise naturally not only in boundary value problems on a disk but also in wave and heat problems over a finite interval. A function $f$ satisfying the identity
@@ -34,14 +40,21 @@
 where $T>0$, is called periodic or, more specifically, $T$-periodic (Figure 2). 
 
 
-
-> [!figure] Figure 2
-> 
-> ![](Screenshot%202026-04-21%20at%2011.31.06%20PM.png)
-> Figure 2 A $T$-periodic function.
-
-
-The number $T$ is called a period of $f$. If $f$ is nonconstant, we define the fundamental period, or simply, the period of $f$ to be the smallest positive number $T$ for which (1) holds. For example, the functions $3, \sin x, \sin 2 x$ are all $2 \pi$-periodic. The period of $\sin x$ is $2 \pi$, while the period of $\sin 2 x$ is $\pi$.
+```scientific-figure
+id: cd736488-243f-4c5f-b317-0142e57646e2
+numbered: false
+title: ""
+caption: "**Figure 2.** A $T$-periodic function."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 07 Fourier Series/images/Screenshot 2026-04-21 at 11.31.06 PM.png
+    caption: ""
+```
+
+
+The number $T$ is called a period of $f$. When a smallest positive period exists, we define the fundamental period, or simply, the period of $f$ to be the smallest positive number $T$ for which (1) holds. For example, the functions $3, \sin x, \sin 2 x$ are all $2 \pi$-periodic. The period of $\sin x$ is $2 \pi$, while the period of $\sin 2 x$ is $\pi$.
 
 Using (1) repeatedly, we get
 
@@ -51,7 +64,6 @@
 
 
 Hence if $T$ is a period, then $n T$ is also a period for any integer $n>0$. In the case of the sine function, this amounts to saying that $2 \pi, 4 \pi, 6 \pi, \ldots$ are all periods of $\sin x$, but only $2 \pi$ is the fundamental period. Because the values of a $T$-periodic function repeat every $T$ units, its graph is obtained by repeating the portion over any interval of length $T$ (Figure 2). As a consequence, to define a $T$-periodic function, it is enough to describe it over an interval of length $T$. Obviously, the interval can be chosen in many different ways. The following example illustrates these ideas.
-
 
 
 > [!exercise] EXAMPLE 1 Describing a periodic function
@@ -60,15 +72,25 @@
 > (a) by considering its values on the interval $0 \leq x<2$;
 > (b) by considering its values on the interval $-1 \leq x<1$.
 > 
-> > [!figure] Figure 3
-> > 
-> > ![](Screenshot%202026-04-21%20at%2011.31.59%20PM.png)
-> > Figure 3 The 2-periodic function in Example 1.
-> 
-> 
-
-
-**Solution** (a) On the interval $0 \leq x<2$ the graph is a portion of the straight line $y=-x+1$. Thus
+> ```scientific-figure
+> id: b28c3f87-296e-44e9-88f6-1861f62df165
+> numbered: false
+> title: ""
+> caption: "**Figure 3.** The 2-periodic function in Example 1."
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 07 Fourier Series/images/Screenshot 2026-04-21 at 11.31.59 PM.png
+>     caption: ""
+> ```
+> 
+> 
+
+
+##### solution
+
+(a) On the interval $0 \leq x<2$ the graph is a portion of the straight line $y=-x+1$. Thus
 
 $$
 f(x)=-x+1 \text { if } 0 \leq x<2 \text {. }
@@ -88,26 +110,31 @@
 As in part (a), the relation $f(x+2)=f(x)$ describes $f$ for all values of $x$ outside the interval $[-1,1)$.
 
 
-++++
-
-
+---
 Although the formulas in Example 1(a) and (b) are different, they describe the same periodic function. In practice, we use common sense in choosing the most convenient formula. Before we illustrate with an example, we introduce a very useful theorem whose content is intuitively clear. It says that the definite integral of a $T$-periodic function is the same over any interval of length $T$ (Figure 4).
 
 
-> [!figure] Figure 4
-> 
-> ![](Pasted%20image%2020260421233503.png)
-> Figure 4 Areas over one period are equal.
-
-
-
+```scientific-figure
+id: 38b40590-e30d-4d9c-9511-c1acb0e70c61
+numbered: false
+title: ""
+caption: "**Figure 4.** Areas over one period are equal."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 07 Fourier Series/images/Pasted image 20260421233503.png
+    caption: ""
+```
+
+
+<!-- Source label: Integral over One Period -->
 > [!theorem] Integral over One Period
-> Suppose that $f$ is $T$-periodic. Then, for any real number $a$, we have
-> 
+> Suppose that $T>0$ and $f$ is a locally integrable $T$-periodic function. Then, for any real number $a$, we have
+>
 > $$
 > \int_0^T f(x) d x=\int_a^{a+T} f(x) d x
 > $$
-> 
 
 
 **Proof** Define
@@ -117,13 +144,10 @@
 $$
 
 
-By the fundamental theorem of calculus, we have $F^{\prime}(a)=f(a+T)-f(a)=0$, because $f$ is periodic with period $T$. Hence $F(a)$ is constant for all $a$, and so $F(0)=F(a)$, which implies the theorem.
-
-
-+++
-
-
-
+The function $F$ is locally absolutely continuous. By the fundamental theorem of calculus, $F^{\prime}(a)=f(a+T)-f(a)=0$ for almost every $a$, because $f$ is periodic with period $T$. Hence $F(a)$ is constant for all $a$, and so $F(0)=F(a)$, which implies the theorem.
+
+
+---
 > [!exercise] EXAMPLE 2 Integrating periodic functions
 > 
 > Let $f$ be the 2 -periodic function in Example 1. Use Theorem 1 to compute
@@ -131,8 +155,9 @@
 > (b) $\int_{-N}^N f^2(x) d x, N$ a positive integer.
 
 
-
-**Solution** (a) Observe that $f^2(x)$ is also 2 -periodic. Thus, by Theorem 1, to compute the integral in (a) we may choose any interval of length 2 . Using the formula from Example 1 (a), we have
+##### solution
+
+(a) Observe that $f^2(x)$ is also 2 -periodic. Thus, by Theorem 1, to compute the integral in (a) we may choose any interval of length 2 . Using the formula from Example 1 (a), we have
 
 $$
 \int_{-1}^1 f^2(x) d x=\int_0^2 f^2(x) d x=\int_0^2(-x+1)^2 d x=-\left.\frac{1}{3}(-x+1)^3\right|_0 ^2=\frac{2}{3}
@@ -148,10 +173,7 @@
 Since $f^2(x)$ is 2 -periodic, by Theorem 1, each integral on the right side is equal to $\int_{-1}^1 f^2(x) d x=\frac{2}{3}$, by (a). Hence the desired integral is $N \frac{2}{3}=\frac{2 N}{3}$.
 
 
-++++
-
-
-
+---
 The most important periodic functions are those in the ( $2 \pi$-periodic) trigonometric system
 
 $$
@@ -165,8 +187,10 @@
 They are $2 \pi$-periodic, and orthogonal on the interval $[0,2 \pi]$. Recall the orthogonality properties of the trigonometric system from Exercise 12, Section 3.2 (in what follows, the indices $m$ and $n$ are nonnegative integers):
 
 
-> [!equation]
-> 
+<!-- Source label:  -->
+> [!equation] Orthogonality of Integer-Frequency Sines and Cosines
+> Let $m,n$ be nonnegative integers.
+>
 > $$
 > \begin{array}{ll}
 > \int_{-\pi}^\pi \cos m x \cos n x d x=0 & \text { if } m \neq n \\
@@ -174,20 +198,18 @@
 > \int_{-\pi}^\pi \sin m x \sin n x d x=0 & \text { if } m \neq n
 > \end{array}
 > $$
-> 
-> 
 
 
 We also have the useful identities:
 
 
-> [!equation]
-> 
+<!-- Source label:  -->
+> [!equation] Squared Norms of Nonconstant Integer-Frequency Sines and Cosines
+> Let $m$ be a nonzero integer.
+>
 > $$
 > \int_{-\pi}^\pi \cos ^2 m x d x=\int_{-\pi}^\pi \sin ^2 m x d x=\pi \quad \text { for all } m \neq 0
 > $$
-> 
-
 
 
 To prove these, we can use the complex integral, as suggested in Exercise 12. Section 3.2, or just use trigonometric identities. For example, to prove the first one, use
@@ -208,8 +230,6 @@
 
 
 # Exercises 7.1
-
-
 
 
 > [!exercise]
@@ -226,12 +246,10 @@
 > 
 
 
-
 > [!exercise]
 > In Exercises 3-6, find a formula that describes the function in the accompanying figure (Figures 5-8).
 > 
-> ![](Screenshot%202026-04-21%20at%2011.37.09%20PM.png)
-
+> ![](Books/Asmar%20Applied%20Complex%20Analysis%20with%20Applications%20to%20Differential%20Equations/Chapter%2007%20Fourier%20Series/original%20copy/images/Screenshot%202026-04-21%20at%2011.37.09%20PM.png)
 
 
 > [!exercise]
@@ -244,7 +262,6 @@
 > 8. Sums of periodic functions need not be periodic. Let $f(x)=\cos x+ \cos \pi x$. (a) Show that the equation $f(x)=2$ has a unique solution.
 > (b) Conclude from (a) that $f$ is not periodic. Does this contradict Exercise 7? The function $f$ is called almost periodic. These functions are of considerable interest and have many useful applications.
 > 
-
 
 
 > [!exercise]
@@ -260,8 +277,6 @@
 > 
 
 
-
-
 > [!exercise]
 > In Exercises 11-14, a $\pi$-periodic function is described over an interval of length $\pi$. In each case plot the graph over three periods and compute the integral
 > 
@@ -275,9 +290,6 @@
 > 14. $f(x)=x^2, \quad-\frac{\pi}{2} \leq x<\frac{\pi}{2}$.
 
 
-
-
-
 > [!exercise]
 > 15. Antiderivatives of periodic functions. Suppose that $f$ is $2 \pi$-periodic and let $a$ be a fixed real number. Define
 > 
@@ -304,3 +316,4 @@
 > (b) Plot $F$ over the interval $[-4,4]$.
 > 
 
+

`````
