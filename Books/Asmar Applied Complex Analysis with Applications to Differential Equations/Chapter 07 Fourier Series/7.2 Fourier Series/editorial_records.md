
# Editorial records

Reading note: 7.2 Fourier Series.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Callout 255: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!equation|e35fe69d-eabe-5bfb-bbd4-c2908be0901d.local at=090841af-4f87-5e1c-8852-9e8cfddea8d4] Real Fourier Coefficients on the Symmetric Period Interval
> The Fourier coefficients of an integrable $2\pi$-periodic function $f$ are given by
>
> $$
> a_0=\frac{1}{2 \pi} \int_{-\pi}^\pi f(x) d x,
> $$
>
> $$
> a_n=\frac{1}{\pi} \int_{-\pi}^\pi f(x) \cos n x d x \quad(n=1,2, \ldots),
> $$
>
> $$
> b_n=\frac{1}{\pi} \int_{-\pi}^\pi f(x) \sin n x d x \quad(n=1,2, \ldots)
> $$
````
### After

````text
> [!equation|e35fe69d-eabe-5bfb-bbd4-c2908be0901d.local at=090841af-4f87-5e1c-8852-9e8cfddea8d4] Euler Formulas for the Fourier Coefficients
> The Fourier coefficients of an integrable $2\pi$-periodic function $f$ are given by
>
> $$
> a_0=\frac{1}{2 \pi} \int_{-\pi}^\pi f(x) d x,
> $$
>
> $$
> a_n=\frac{1}{\pi} \int_{-\pi}^\pi f(x) \cos n x d x \quad(n=1,2, \ldots),
> $$
>
> $$
> b_n=\frac{1}{\pi} \int_{-\pi}^\pi f(x) \sin n x d x \quad(n=1,2, \ldots)
> $$
````

## 2. Callout 257: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!equation|74d94a23-240c-50f8-b220-622990d197fb.local at=976188cb-e75d-5df7-8eb5-700c2d19fc99] Real Fourier Coefficients on a Full Positive Period Interval
> For an integrable $2\pi$-periodic function $f$, with constant coefficient $a_0$ rather than $a_0/2$ in the Fourier series,
>
> $$
> a_0=\frac{1}{2 \pi} \int_0^{2 \pi} f(x) d x
> $$
>
> $$
> a_n=\frac{1}{\pi} \int_0^{2 \pi} f(x) \cos n x d x, \text { and } b_n=\frac{1}{\pi} \int_0^{2 \pi} f(x) \sin n x d x, n \geq 1 .
> $$
````
### After

````text
> [!equation|74d94a23-240c-50f8-b220-622990d197fb.local at=976188cb-e75d-5df7-8eb5-700c2d19fc99] Alternative Euler Formulas
> For an integrable $2\pi$-periodic function $f$, with constant coefficient $a_0$ rather than $a_0/2$ in the Fourier series,
>
> $$
> a_0=\frac{1}{2 \pi} \int_0^{2 \pi} f(x) d x
> $$
>
> $$
> a_n=\frac{1}{\pi} \int_0^{2 \pi} f(x) \cos n x d x, \text { and } b_n=\frac{1}{\pi} \int_0^{2 \pi} f(x) \sin n x d x, n \geq 1 .
> $$
````

## 3. Callout 258: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem|8bc02eb9-f2cf-5e29-981e-5e93fbe73ad9.local at=ee1bf1be-a960-5b42-bd43-24305539e2d7] Pointwise Convergence of a Piecewise Smooth Fourier Series
> Write $f(x+)$ and $f(x-)$ for the right and left limits.
>
> Suppose that $f$ is a $2 \pi$-periodic piecewise smooth function. Then for all $x$ we have
>
> $$
> \frac{f(x+)+f(x-)}{2}=a_0+\sum_{n=1}^{\infty}\left(a_n \cos n x+b_n \sin n x\right),
> $$
>
> where the Fourier coefficients are $a_0=(2\pi)^{-1}\int_{-\pi}^{\pi}f(t)\,dt$, $a_n=\pi^{-1}\int_{-\pi}^{\pi}f(t)\cos(nt)\,dt$, and $b_n=\pi^{-1}\int_{-\pi}^{\pi}f(t)\sin(nt)\,dt$ for $n\geq1$. In particular, if $f$ is piecewise smooth and continuous at $x$, then
>
> $$
> f(x)=a_0+\sum_{n=1}^{\infty}\left(a_n \cos n x+b_n \sin n x\right)
> $$
````
### After

````text
> [!theorem|8bc02eb9-f2cf-5e29-981e-5e93fbe73ad9.local at=ee1bf1be-a960-5b42-bd43-24305539e2d7] Fourier Series Representation
> Write $f(x+)$ and $f(x-)$ for the right and left limits.
>
> Suppose that $f$ is a $2 \pi$-periodic piecewise smooth function. Then for all $x$ we have
>
> $$
> \frac{f(x+)+f(x-)}{2}=a_0+\sum_{n=1}^{\infty}\left(a_n \cos n x+b_n \sin n x\right),
> $$
>
> where the Fourier coefficients are $a_0=(2\pi)^{-1}\int_{-\pi}^{\pi}f(t)\,dt$, $a_n=\pi^{-1}\int_{-\pi}^{\pi}f(t)\cos(nt)\,dt$, and $b_n=\pi^{-1}\int_{-\pi}^{\pi}f(t)\sin(nt)\,dt$ for $n\geq1$. In particular, if $f$ is piecewise smooth and continuous at $x$, then
>
> $$
> f(x)=a_0+\sum_{n=1}^{\infty}\left(a_n \cos n x+b_n \sin n x\right)
> $$
````

## 4. Callout 259: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!corollary|4b2b0a41-0cc6-5959-8abd-036e2a16f028.local at=c916d5c4-f347-539c-b9ca-bf8238ffd65c] Uniqueness of Piecewise Smooth Fourier Series Representations
> Suppose that $f$ and $g$ are $2 \pi$-periodic piecewise smooth functions. If $f$ and $g$ have the same Fourier coefficients, then $f(x)=g(x)$ for all $x$, except possibly at the points where $f$ or $g$ are discontinuous. Consequently, if $f$ and $g$ are continuous and have the same Fourier coefficients, then they are equal everywhere.
````
### After

````text
> [!corollary|4b2b0a41-0cc6-5959-8abd-036e2a16f028.local at=c916d5c4-f347-539c-b9ca-bf8238ffd65c] Uniqueness of Fourier Series Representation
> Suppose that $f$ and $g$ are $2 \pi$-periodic piecewise smooth functions. If $f$ and $g$ have the same Fourier coefficients, then $f(x)=g(x)$ for all $x$, except possibly at the points where $f$ or $g$ are discontinuous. Consequently, if $f$ and $g$ are continuous and have the same Fourier coefficients, then they are equal everywhere.
````

## 5. Callout 260: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem|5c662c09-67e6-5224-afad-068e094a800e.local at=d8453e12-9618-5b91-9a78-b048346d5e32] Uniform Convergence of Fourier Series of Piecewise Smooth Functions
> The coefficient convention is $a_0=(2\pi)^{-1}\int_{-\pi}^{\pi}f(t)\,dt$, $a_n=\pi^{-1}\int_{-\pi}^{\pi}f(t)\cos(nt)\,dt$, and $b_n=\pi^{-1}\int_{-\pi}^{\pi}f(t)\sin(nt)\,dt$ for $n\geq1$.
>
> Suppose that $f$ is a $2 \pi$-periodic piecewise smooth function. Then the Fourier series of $f$ converges uniformly for all $x$ to $f(x)$ if and only if $f$ is continuous for all $x$. Thus, if $f$ is continuous and piecewise smooth, then
>
> $$
> f(x)=a_0+\sum_{n=1}^{\infty}\left(a_n \cos n x+b_n \sin n x\right),
> $$
>
> where the Fourier series converges uniformly for all $x$.
````
### After

````text
> [!theorem|5c662c09-67e6-5224-afad-068e094a800e.local at=d8453e12-9618-5b91-9a78-b048346d5e32] Uniform Convergence of Fourier Series
> The coefficient convention is $a_0=(2\pi)^{-1}\int_{-\pi}^{\pi}f(t)\,dt$, $a_n=\pi^{-1}\int_{-\pi}^{\pi}f(t)\cos(nt)\,dt$, and $b_n=\pi^{-1}\int_{-\pi}^{\pi}f(t)\sin(nt)\,dt$ for $n\geq1$.
>
> Suppose that $f$ is a $2 \pi$-periodic piecewise smooth function. Then the Fourier series of $f$ converges uniformly for all $x$ to $f(x)$ if and only if $f$ is continuous for all $x$. Thus, if $f$ is continuous and piecewise smooth, then
>
> $$
> f(x)=a_0+\sum_{n=1}^{\infty}\left(a_n \cos n x+b_n \sin n x\right),
> $$
>
> where the Fourier series converges uniformly for all $x$.
````

## 6. Move editorial commentary out of the reading note.

### Before

````text
*Editorial corrections to source details: The coefficient-decay comparison uses absolute values. In Exercise 16, the requested illustration $c=d=\pi/2$ is the limiting case $c+d=\pi$, rather than a case satisfying the printed strict inequality.*
````
### After

````text

````

## Source-to-current comparison

Source: /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 07 Fourier Series/7.2 Fourier Series.md

This exact comparison preserves the full change evidence, including formatting, OCR corrections, restored source wording, and required standalone context. The entries above explain the recovery edits. The comparison is not a claim that every difference is a correction; component serialization, callout wrapping, and printed labels outside callouts are formatting.

`````diff
--- /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 07 Fourier Series/7.2 Fourier Series.md
+++ /Users/gradyclopton/ObsidianVaults/complex_analysis/Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 07 Fourier Series/7.2 Fourier Series.md
@@ -10,57 +10,48 @@
 where the coefficients $a_0, a_n$, and $b_n$ are called the Fourier coefficients of $f$ and are given by the following Euler formulas.
 
 
-
-> [!equation] Euler Formulas for the Fourier Coefficients
-> The Fourier coefficients of of a function $f$ are given by
-> (2)
-> 
+<!-- Source label: Euler Formulas for the Fourier Coefficients -->
+> [!equation|e35fe69d-eabe-5bfb-bbd4-c2908be0901d.local at=090841af-4f87-5e1c-8852-9e8cfddea8d4] Euler Formulas for the Fourier Coefficients
+> The Fourier coefficients of an integrable $2\pi$-periodic function $f$ are given by
+>
 > $$
 > a_0=\frac{1}{2 \pi} \int_{-\pi}^\pi f(x) d x,
 > $$
-> 
-> (3)
-> 
+>
 > $$
 > a_n=\frac{1}{\pi} \int_{-\pi}^\pi f(x) \cos n x d x \quad(n=1,2, \ldots),
 > $$
-> 
-> (4)
-> 
+>
 > $$
 > b_n=\frac{1}{\pi} \int_{-\pi}^\pi f(x) \sin n x d x \quad(n=1,2, \ldots)
 > $$
-> 
 
 For a positive integer $N$, we denote the $N$ th partial sum of the Fourier series of $f$ by $s_N(x)$. Thus
 
 
-> [!equation]
-> 
+<!-- Source label:  -->
+> [!equation|8dab8435-8e68-5a24-81f1-c9107931ff10.local at=190c77f6-c6ae-5d24-beaa-7a8c3f8080f0] Partial Sum of a Real Trigonometric Fourier Series
+> For an integrable $2\pi$-periodic function $f$, let $a_0=(2\pi)^{-1}\int_{-\pi}^{\pi}f(t)\,dt$, $a_n=\pi^{-1}\int_{-\pi}^{\pi}f(t)\cos(nt)\,dt$, and $b_n=\pi^{-1}\int_{-\pi}^{\pi}f(t)\sin(nt)\,dt$ for $n\geq1$. Its partial sum of order $N\geq0$ is
+>
 > $$
 > s_N(x)=a_0+\sum_{n=1}^N\left(a_n \cos n x+b_n \sin n x\right) .
 > $$
-> 
-
 
 
 Because all the integrands in (2)-(4) are $2 \pi$-periodic, we can use Theorem 1, Section 7.1, to rewrite these formulas using integrals over the interval $[0,2 \pi]$ (or any other interval of length $2 \pi$ ). Such alternative formulas are sometimes useful.
 
 
-> [!equation] Alternative Euler Formulas
-> (5)
-> 
+<!-- Source label: Alternative Euler Formulas -->
+> [!equation|74d94a23-240c-50f8-b220-622990d197fb.local at=976188cb-e75d-5df7-8eb5-700c2d19fc99] Alternative Euler Formulas
+> For an integrable $2\pi$-periodic function $f$, with constant coefficient $a_0$ rather than $a_0/2$ in the Fourier series,
+>
 > $$
 > a_0=\frac{1}{2 \pi} \int_0^{2 \pi} f(x) d x
 > $$
-> 
-> (6)
-> 
+>
 > $$
 > a_n=\frac{1}{\pi} \int_0^{2 \pi} f(x) \cos n x d x, \text { and } b_n=\frac{1}{\pi} \int_0^{2 \pi} f(x) \sin n x d x, n \geq 1 .
 > $$
-> 
-
 
 
 The Fourier coefficients were known to Euler before Fourier and for this reason they bear Euler's name. Euler used them to derive particular Fourier series such as the one presented in Example 1 below.
@@ -94,8 +85,7 @@
 Our first example displays many of the peculiar properties of Fourier series.
 
 
-
-> [!exercise] EXAMPLE 1 Fourier series of the sawtooth function
+> [!exercise|dd9d7446-1d61-546f-9931-066325c5cc34.local at=47e8bda4-3062-5e57-930d-aa43f9541314] EXAMPLE 1 Fourier series of the sawtooth function
 > 
 > The sawtooth function, shown in Figure 1, is determined by the formulas
 > 
@@ -107,15 +97,24 @@
 > (b) With the help of a computer, plot the partial sums $s_1(x), s_7(x)$, and $s_{20}(x)$, and determine the graph of the Fourier series.
 
 
-> [!figure]
-> 
-> ![](Pasted%20image%2020260421235007.png)
-> Figure 1 Sawtooth function.
-
-
-
-
-**Solution** (a) Using (5) and (6), we have
+<!-- Migrated source callout: [!figure|0ca46a0e-ae78-5469-b7ee-e696be2e2cfd.local at=f604f91c-c0db-5efa-9f23-1706986fde43] -->
+```scientific-figure
+id: 0ca46a0e-ae78-5469-b7ee-e696be2e2cfd
+numbered: false
+title: ""
+caption: "**Figure 1.** Sawtooth function."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 07 Fourier Series/images/Pasted image 20260421235007.png
+    caption: ""
+```
+
+
+##### solution
+
+(a) Using (5) and (6), we have
 
 $$
 \begin{aligned}
@@ -124,7 +123,7 @@
 & =\frac{1}{2 \pi}\left\{\int_0^{2 \pi} \pi \cos n x d x-\int_0^{2 \pi} x \cos n x d x\right\}=0 \\
 b_n= & \frac{1}{\pi} \int_0^{2 \pi} \frac{1}{2}(\pi-x) \sin n x d x \\
 = & \frac{1}{2 \pi}\left\{\int_0^{2 \pi} \pi \sin n x d x-\int_0^{2 \pi} x \sin n x d x\right\} \\
-= & \frac{1}{2 \pi}\left\{\frac{-1}{n^2} \sin n x+\left.\frac{x}{n} \cos n x\right|_0 ^{2 \pi} \quad\right. \text { (integration by parts) } \\
+= & \frac{1}{2 \pi}\left[\frac{-1}{n^2} \sin n x+\frac{x}{n} \cos n x\right]_0 ^{2 \pi} \quad \text { (integration by parts) } \\
 = & \frac{1}{2 \pi} \frac{2 \pi}{n}=\frac{1}{n}
 \end{aligned}
 $$
@@ -134,23 +133,34 @@
 (b) Figure 2 shows the first, seventh and twentieth partial sums of the Fourier series. 
 
 
-
-
-> [!figure] Figure 2
-> 
-> ![](Pasted%20image%2020260421235116.png)
-> Figure 2 To distinguish the graphs of the $n$th partial sums of the Fourier series, $s_0(x)=\sum_{k=1}^n \frac{\text { sink } z}{k}$, note that as $n$ increases, the frequencies of the sine terms increase. This causes the graphs of the higher partial sums to be more wiggly. The limiting graph is the graph of the whole Fourier series, shown in Figure 3. It is identical to the graph of the function, except at points of discontinuity.
-> 
-
-
-
-
-> [!figure]
-> 
-> ![](Pasted%20image%2020260421235241.png)
-> Figure 3 The graph of the Fourier series $\sum_{n=1}^{\infty} \frac{\sin n x}{n}$ coincides with the graph of the function, except at the points of the discontinuity.
-
-
+<!-- Migrated source callout: [!figure|e9b5e8e9-5bff-58e4-a95d-e6f716b5c9a2.local at=0a7050d1-7020-5609-8fa4-9c7b64cad1eb] -->
+```scientific-figure
+id: e9b5e8e9-5bff-58e4-a95d-e6f716b5c9a2
+numbered: false
+title: ""
+caption: "**Figure 2.** To distinguish the graphs of the $n$th partial sums of the Fourier series, $s_n(x)=\\sum_{k=1}^n \\frac{\\sin(kx)}{k}$, note that as $n$ increases, the frequencies of the sine terms increase. This causes the graphs of the higher partial sums to be more wiggly. The limiting graph is the graph of the whole Fourier series, shown in Figure 3. It is identical to the graph of the function, except at points of discontinuity."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 07 Fourier Series/images/Pasted image 20260421235116.png
+    caption: ""
+```
+
+
+<!-- Migrated source callout: [!figure|e35db7eb-0f23-5174-b19d-b0609ba82e8c.local at=b5db3fd5-f965-520a-9fbc-66127b231905] -->
+```scientific-figure
+id: e35db7eb-0f23-5174-b19d-b0609ba82e8c
+numbered: false
+title: ""
+caption: "**Figure 3.** The graph of the Fourier series $\\sum_{n=1}^{\\infty} \\frac{\\sin n x}{n}$ coincides with the graph of the function, except at the points of the discontinuity."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 07 Fourier Series/images/Pasted image 20260421235241.png
+    caption: ""
+```
 
 
 We see clearly that the Fourier series of $f$ converges to $f(x)$ at each point $x$ where $f$ is continuous. In particular, for $0<x<2 \pi$, we have
@@ -163,17 +173,13 @@
 At the points of discontinuity ( $x=2 k \pi, k=0, \pm 1, \pm 2, \ldots$ ), the series converges to 0 . The graph of the Fourier series $\sum_{n=1}^{\infty} \frac{\sin n x}{n}$ is shown in Figure 3. It agrees with the graph of the function, except at the points of discontinuity.
 
 
-++++
-
-
-
+---
 Two important facts are worth noting concerning the behavior of Fourier series near points of discontinuity. As we will see shortly, these observations are true in a very general sense.
 Note 1: At the points of discontinuity ( $x=2 k \pi$ ) in Example 1, the Fourier series converges to 0 , which is the average value of the function from the left and the right at these points.
 Note 2: Near the points of discontinuity, the Fourier series overshoots its limiting values. This is apparent in Figure 2, where humps form on the graphs of the partial sums near the points of discontinuity. This curious phenomenon is known as the Gibbs (or Wilbraham-Gibbs) phenomenon.
 (See the paper [15] for an interesting historical account.)
 
 
-
 # Fourier Series Representation
 To state our main result, we recall from Section 3.1 the definitions of piecewise continuous and piecewise smooth functions. We will write
 
@@ -184,14 +190,19 @@
 to denote the fact that $f$ approaches the number $f(c-)$ as $x$ approaches $c$ from below (Figure 4). 
 
 
-
-
-> [!figure] Figure 4
-> 
-> ![](Pasted%20image%2020260421235340.png)
-> Figure 4 Left and right linits of a function at a point of discontinuity: $f(1+)=\frac{1}{2}$, $f(1-)=1$.
-> 
-
+<!-- Migrated source callout: [!figure|b29807f9-a308-5ea1-8cf6-dcb3c6fb5545.local at=093a3b18-0e07-55d1-9f2d-902f4c03fc5d] -->
+```scientific-figure
+id: b29807f9-a308-5ea1-8cf6-dcb3c6fb5545
+numbered: false
+title: ""
+caption: "**Figure 4.** Left and right limits of a function at a point of discontinuity: $f(1+)=\\frac{1}{2}$, $f(1-)=1$."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 07 Fourier Series/images/Pasted image 20260421235340.png
+    caption: ""
+```
 
 
 Similarly, if the limit of $f$ exists as $x$ approaches $c$
@@ -214,12 +225,19 @@
 In this notation, a function $f$ is said to be piecewise continuous on the interval $[a, b]$ if $f(a+)$ and $f(b-)$ exist, and $f$ is defined and continuous on $(a, b)$ except at a finite number of points in $(a, b)$ where the left and right limits exist. A periodic function is said to be piecewise continuous if it is piecewise continuous on every interval of the form $[a, b]$. A periodic function is said to be continuous if it is continuous on the entire real line. Note that continuity forces a certain behavior of the periodic function at the endpoints of any interval of length one period. For example, if $f$ is $2 p$-periodic and continuous, then necessarily $f(-p)=f(p)$ (Figure 5). 
 
 
-
-> [!figure] Figure 5
-> 
-> ![](Pasted%20image%2020260421235728.png)
-> Figure 5 A continuous $2 p$ periodic function.
-
+<!-- Migrated source callout: [!figure|d8173493-4e92-5c0a-bab1-dbeac428d278.local at=42456c29-3248-5465-952a-49ec0bfd5ea7] -->
+```scientific-figure
+id: d8173493-4e92-5c0a-bab1-dbeac428d278
+numbered: false
+title: ""
+caption: "**Figure 5.** A continuous $2 p$ periodic function."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 07 Fourier Series/images/Pasted image 20260421235728.png
+    caption: ""
+```
 
 
 The function of Example 1 is piecewise continuous, while the function in Example 2 below is continuous. Let us also recall that a function $f$ is said to be piecewise smooth if $f$ and $f^{\prime}$ are piecewise continuous on $[a, b]$. Similarly, a periodic function is piecewise smooth if it is piecewise smooth on every interval $[a, b]$. One more item of terminology is needed. The average (or arithmetic average) of $f$ at $c$ is
@@ -234,48 +252,57 @@
 As an illustration, consider the function in Figure 6. 
 
 
-
-> [!figure] Figure 6
-> 
-> ![](Pasted%20image%2020260421235849.png)
-> Figure 6 Average of $f(x)$ at $x=1$.
-
+<!-- Migrated source callout: [!figure|4f7a4dab-104b-5415-a90f-6d2fb47ba8c4.local at=2dc36f06-a682-53e3-9ccc-3bad37534ed9] -->
+```scientific-figure
+id: 4f7a4dab-104b-5415-a90f-6d2fb47ba8c4
+numbered: false
+title: ""
+caption: "**Figure 6.** Average of $f(x)$ at $x=1$."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 07 Fourier Series/images/Pasted image 20260421235849.png
+    caption: ""
+```
 
 
 It has a discontinuity at $x=1$ and its average there is $\frac{1+\frac{1}{2}}{2}=\frac{3}{4}$. We can now state a fundamental result in the theory of Fourier series. The proof of this theorem is presented in Section 7.6.
 
 
-
-
-> [!theorem] Fourier Series Representation
+<!-- Source label: Fourier Series Representation -->
+> [!theorem|8bc02eb9-f2cf-5e29-981e-5e93fbe73ad9.local at=ee1bf1be-a960-5b42-bd43-24305539e2d7] Fourier Series Representation
+> Write $f(x+)$ and $f(x-)$ for the right and left limits.
+>
 > Suppose that $f$ is a $2 \pi$-periodic piecewise smooth function. Then for all $x$ we have
-> 
+>
 > $$
 > \frac{f(x+)+f(x-)}{2}=a_0+\sum_{n=1}^{\infty}\left(a_n \cos n x+b_n \sin n x\right),
 > $$
-> 
-> where the Fourier coefficients $a_0, a_n, b_n$ are given by (2)-(4). In particular. if $f$ is piecewise smooth and continuous at $x$, then
-> 
+>
+> where the Fourier coefficients are $a_0=(2\pi)^{-1}\int_{-\pi}^{\pi}f(t)\,dt$, $a_n=\pi^{-1}\int_{-\pi}^{\pi}f(t)\cos(nt)\,dt$, and $b_n=\pi^{-1}\int_{-\pi}^{\pi}f(t)\sin(nt)\,dt$ for $n\geq1$. In particular, if $f$ is piecewise smooth and continuous at $x$, then
+>
 > $$
 > f(x)=a_0+\sum_{n=1}^{\infty}\left(a_n \cos n x+b_n \sin n x\right)
 > $$
-> 
-> 
 
 
 Let us see what (7) is telling us. At a point of continuity of $f$, the Fourier series converges to $f(x)$. At a point of discontinuity, the Fourier series does its best to converge, and having no reason to favor one side over the other. it converges to the average of the left and right limits (see Figure 7). 
 
 
-
-
-> [!figure] Figure 7
-> 
-> ![](Pasted%20image%2020260422000312.png)
-> Figure 7 At a point of discontinuity of a piecewise smooth function, the Fourier series converges to the average of the function at that point.
-
-
-
-
+<!-- Migrated source callout: [!figure|0b6b0351-f4a7-58fd-8ffb-d80b5d041009.local at=2bfef916-c1f7-583d-932d-171a162bb3bc] -->
+```scientific-figure
+id: 0b6b0351-f4a7-58fd-8ffb-d80b5d041009
+numbered: false
+title: ""
+caption: "**Figure 7.** At a point of discontinuity of a piecewise smooth function, the Fourier series converges to the average of the function at that point."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 07 Fourier Series/images/Pasted image 20260422000312.png
+    caption: ""
+```
 
 
 Note that in (7) the value of the Fourier series of $f$ at a given point $x$ does not depend on $f(x)$ but on the limit of $f$ from the left and right at $x$. For this reason, we may define (or redefine) $f$ at isolated points without affecting its Fourier series. This is illustrated by the behavior of the Fourier series in Example 1, where, at the points of discontinuity, we could have assigned any values for the function without affecting the behavior of the Fourier series. If we redefine the function at points of discontinuity to be
@@ -299,24 +326,19 @@
 Let us note one more property of Fourier series, which is an immediate consequence of Theorem 1.
 
 
-
-
-> [!corollary] Uniqueness of Fourier Series Representation 
+<!-- Source label: Uniqueness of Fourier Series Representation  -->
+> [!corollary|4b2b0a41-0cc6-5959-8abd-036e2a16f028.local at=c916d5c4-f347-539c-b9ca-bf8238ffd65c] Uniqueness of Fourier Series Representation
 > Suppose that $f$ and $g$ are $2 \pi$-periodic piecewise smooth functions. If $f$ and $g$ have the same Fourier coefficients, then $f(x)=g(x)$ for all $x$, except possibly at the points where $f$ or $g$ are discontinuous. Consequently, if $f$ and $g$ are continuous and have the same Fourier coefficients, then they are equal everywhere.
 
 
-
-**Proof** Since the Fourier scries of a function converges to the value of the function at the points of continuity, it follows that if $f$ and $g$ have the same Fourier series. then they must be equal at all the points of continuity.
-
-
-+++
-
-
+**Proof** Since the Fourier series of a function converges to the value of the function at the points of continuity, it follows that if $f$ and $g$ have the same Fourier series. then they must be equal at all the points of continuity.
+
+
+---
 For all practical purposes in analysis, if $f$ and $g$ have the same Fourier series, then they are considered to be the same function.
 
 
-
-> [!exercise] EXAMPLE 2 Triangular wave
+> [!exercise|8a2210c1-3462-5ca1-898f-3455b63b59a8.local at=e1f04b0a-fcfd-5bef-bea2-122d8b41c25f] EXAMPLE 2 Triangular wave
 > 
 > (a) Find the Fourier series of the $2 \pi$-periodic triangular function, which is given on the interval $[-\pi, \pi]$ by
 > 
@@ -327,17 +349,24 @@
 > (b) Plot some partial sums and the Fourier series.
 
 
-
-**Solution** Figure 8 shows that the function is piecewise smooth and continuous for all $x$. So, from the second part of Theorem 1, we expect the Fourier series to converge to $f(x)$ for all $x$. 
-
-
-
-> [!figure] Figure 8
-> 
-> ![](Pasted%20image%2020260422000549.png)
-> Figure 8 Triangular wave.
-
-
+##### solution
+
+Figure 8 shows that the function is piecewise smooth and continuous for all $x$. So, from the second part of Theorem 1, we expect the Fourier series to converge to $f(x)$ for all $x$. 
+
+
+<!-- Migrated source callout: [!figure|bbc58e75-011e-5265-a052-214b3ee315d9.local at=3bd32e52-79f6-5b4d-9409-a6054653c375] -->
+```scientific-figure
+id: bbc58e75-011e-5265-a052-214b3ee315d9
+numbered: false
+title: ""
+caption: "**Figure 8.** Triangular wave."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 07 Fourier Series/images/Pasted image 20260422000549.png
+    caption: ""
+```
 
 
 Using (2), we have
@@ -372,49 +401,57 @@
 for all $x$. Since the function and its Fourier series are equal at all points, their graphs coincide (compare Figures 8 and 10).
 
 
-
-
-> [!figure] Figure 10
-> 
-> ![](Pasted%20image%2020260422000703.png)
-> Figure 10 The Fourier series.
-
+<!-- Migrated source callout: [!figure|e24ac383-cd13-599c-a134-8aa95c9d5692.local at=b03be9f4-ba7c-55f5-b786-7015367ab9fa] -->
+```scientific-figure
+id: e24ac383-cd13-599c-a134-8aa95c9d5692
+numbered: false
+title: ""
+caption: "**Figure 10.** The Fourier series."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 07 Fourier Series/images/Pasted image 20260422000703.png
+    caption: ""
+```
 
 
 In (9), letting $k$ run from 0 to 1,2 , and 5 , respectively, we generate the third, fifth. and eleventh partial sums of the Fourier series. These are plotted in Figure 9. Note the fast convergence of the Fourier series.
 
 
-
-> [!figure] Figure 9
-> 
-> ![](Pasted%20image%2020260422000742.png)
-> Figure 9 Partial sums of the Fourier series. The partial sums of the Fourier series, illustrated in Figure 9, are converging very fast. much faster than those in Example 1. This is due to the magnitudes of the Fourier coefficients. In Example 1 the coefficients are of the order 1/n, while in Example 2 the coefficients are of the order $1 / n^2$.
-
-
-
-++++
-
-
-
-
+<!-- Migrated source callout: [!figure|f9d7e35f-78c4-59d8-929e-a06377b44b19.local at=364d4fc3-ce5c-5f7c-be4a-3b0316f9e602] -->
+```scientific-figure
+id: f9d7e35f-78c4-59d8-929e-a06377b44b19
+numbered: false
+title: ""
+caption: "**Figure 9.** Partial sums of the Fourier series. The partial sums of the Fourier series, illustrated in Figure 9, are converging very fast. much faster than those in Example 1. This is due to the magnitudes of the Fourier coefficients. In Example 1 the coefficients are of the order 1/n, while in Example 2 the coefficients are of the order $1 / n^2$."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 07 Fourier Series/images/Pasted image 20260422000742.png
+    caption: ""
+```
+
+
+---
 Figure 9 suggests that the Fourier series in Example 2 converges uniformly to the function. This is indeed true and follows from the following important result.
 
 
-
-
-> [!theorem] Uniform Convergence of Fourier Series
+<!-- Source label: Uniform Convergence of Fourier Series -->
+> [!theorem|5c662c09-67e6-5224-afad-068e094a800e.local at=d8453e12-9618-5b91-9a78-b048346d5e32] Uniform Convergence of Fourier Series
+> The coefficient convention is $a_0=(2\pi)^{-1}\int_{-\pi}^{\pi}f(t)\,dt$, $a_n=\pi^{-1}\int_{-\pi}^{\pi}f(t)\cos(nt)\,dt$, and $b_n=\pi^{-1}\int_{-\pi}^{\pi}f(t)\sin(nt)\,dt$ for $n\geq1$.
+>
 > Suppose that $f$ is a $2 \pi$-periodic piecewise smooth function. Then the Fourier series of $f$ converges uniformly for all $x$ to $f(x)$ if and only if $f$ is continuous for all $x$. Thus, if $f$ is continuous and piecewise smooth, then
-> 
+>
 > $$
 > f(x)=a_0+\sum_{n=1}^{\infty}\left(a_n \cos n x+b_n \sin n x\right),
 > $$
-> 
+>
 > where the Fourier series converges uniformly for all $x$.
 
 
-
-
-**Proof** One direction is imnediate from Theorem 1, Section 4.2, which asserts that the uniform limit of continuous functions is continuous. Since a partial sum of a Fourier series is a finite linear combination of sines and cosines, it is clearly continnous. So, if $s_N(x)$ converges uniformly to $f(x)$ for all $x$, then $f(x)$ is necessarily continuous for all $x$. For the other direction, we know from Theorem 1 that the Fourier series converges to $f(x)$ for all $x$. To prove that the convergence is uniform, we will show that there is a constant $M$ such that $\left|a_n\right| \leq \frac{M}{n^2}$ and $\left|b_n\right| \leq \frac{M}{n^2}$. Then $\left|a_n \cos n x+b_n \sin n x\right| \leq \frac{2 M}{n^2}$, and the uniform convergence will follow from the Weierstrass $M$-test (Theorem 3, Section 4.2) since $\sum \frac{2 . M}{n^2}<\infty$. To simplify the proof, we will further suppose that $f^{\prime}$ is piecewise smooth. (This condition is satisfied in all the examples in this book, and indeed most applications. A proof that does not depend on it is presented in Section 7.5 and uses Parseval's theorem.)
+**Proof** One direction is immediate from Theorem 1, Section 4.2, which asserts that the uniform limit of continuous functions is continuous. Since a partial sum of a Fourier series is a finite linear combination of sines and cosines, it is clearly continuous. So, if $s_N(x)$ converges uniformly to $f(x)$ for all $x$, then $f(x)$ is necessarily continuous for all $x$. For the other direction, we know from Theorem 1 that the Fourier series converges to $f(x)$ for all $x$. To prove that the convergence is uniform, we will show that there is a constant $M$ such that $\left|a_n\right| \leq \frac{M}{n^2}$ and $\left|b_n\right| \leq \frac{M}{n^2}$. Then $\left|a_n \cos n x+b_n \sin n x\right| \leq \frac{2 M}{n^2}$, and the uniform convergence will follow from the Weierstrass $M$-test (Theorem 3, Section 4.2) since $\sum \frac{2M}{n^2}<\infty$. To simplify the proof, we will further suppose that $f^{\prime}$ is piecewise smooth. (This condition is satisfied in all the examples in this book, and indeed most applications. A proof that does not depend on it is presented in Section 7.5 and uses Parseval's theorem.)
 
 
 Integrating by parts, we find that
@@ -449,20 +486,14 @@
 where $C$ is a constant that does not depend on $n$. Since $f^{\prime \prime}$ has a finite number of discontinuities, we can write the integral $\int_{-\pi}^\pi f^{\prime}(x) \sin n x d x$ as the finite sum of integrals of the form $\int_a^b f^{\prime}(x) \sin n x d x$ (say, $k$ of them), where $f^{\prime \prime}(x)$ is continuous on each interval $(a, b)$. It follows from our estimate on the latter integral that $\left|a_n\right| \leq \frac{k C}{n^2}=\frac{M}{n^2}$, where $M=k C$ is a constant independent of $n$. The inequality for $b_n$ is obtained in a similar way.
 
 
-+++
-
-
-
+---
 Theorems 1 or 2 can be used to sum interesting series.
 
 
-
-> [!exercise] EXAMPLE 3 Using Fourier series to sum series
-> 
-> <span style="color:#ff0000; font-weight:bold">Exercise statement needed</span>
-> 
-
-
+> [!exercise|775915eb-cc9a-54ef-87c1-2d1fbf6d1c43.local at=0b4dea5b-065d-5184-8db0-cc64e7215787] EXAMPLE 3 Using Fourier series to sum series
+> Use the Fourier series of the triangular wave in Example 2 to evaluate $\sum_{k=0}^{\infty}(2k+1)^{-2}$.
+
+##### solution
 
 If we take $x=0$ on both sides of (9), we get
 
@@ -480,20 +511,14 @@
 which can be used to approximate $\pi^2$ (and hence also $\pi$ ).
 
 
-++++
-
-
-
+---
 The Fourier series in Examples 1 and 2 are special in the sense that one of them contains only sine terms, while the other one contains only cosine terms. Fourier series of this type will be studied in the next section. The following Fourier series contains both sine and cosine terms. It is computed using the previous examples and the linearity property of Fourier series.
 
 
-
-
-> [!exercise] EXAMPLE 4 A Fourier series with cosine and sine terms
-> 
-> <span style="color:#ff0000; font-weight:bold">Exercise statement needed</span>
-> 
-
+> [!exercise|66ad14cf-c539-5254-a055-3cacf8b779fd.local at=132568d1-2b64-5c27-b824-492627ab11df] EXAMPLE 4 A Fourier series with cosine and sine terms
+> Find the Fourier series of the $2\pi$-periodic sum of the sawtooth function in Example 1 and the triangular wave in Example 2. Plot the function and describe the series at its discontinuities.
+
+##### solution
 
 Adding the two functions of Examples 1 and 2 , we obtain a $2 \pi$-periodic function which is defined on the interval $[0,2 \pi]$ by
 
@@ -509,30 +534,36 @@
 
 
 
-Figure 11 Note the Gibbs phenomenon at the points of discontinuity $(x=2 k \pi)$. This is due to the fact that the Fourier series consists of a cosine part that is converging very fast (Figure 9) and a sine part that overshoots at the points of discontinuity.
-
-
-> [!figure] Figure 11
-> 
-> ![](Pasted%20image%2020260422001418.png)
-> Figure 11 Note the Gibbs phenomenon at the points of discontinuity $(x=2 k \pi)$. This is due to the fact that the Fourier series consists of a cosine part that is converging very fast (Figure 9) and a sine part that overshoots at the points of discontinuity.
-> 
-
-
-
-
+
+<!-- Migrated source callout: [!figure|b31a57bd-2938-59d2-9e55-5ede9af963b7.local at=75466066-8e7e-5afb-af67-a4be387cba19] -->
+```scientific-figure
+id: b31a57bd-2938-59d2-9e55-5ede9af963b7
+numbered: false
+title: ""
+caption: "**Figure 11.** Note the Gibbs phenomenon at the points of discontinuity $(x=2 k \\pi)$. This is due to the fact that the Fourier series consists of a cosine part that is converging very fast (Figure 9) and a sine part that overshoots at the points of discontinuity."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 07 Fourier Series/images/Pasted image 20260422001418.png
+    caption: ""
+```
+
+
+As illustrated in Figure 11, at the points of discontinuity the Fourier series converges to the average value $\pi$. At all other points, it converges to $f(x)$.
 
 # Complex Methods for Finding Fourier Series
 Because of Euler's identity $e^{i n \theta}=\cos n \theta+i \sin n \theta$, which relates the complex exponential to the trigonometric functions, we expect the complex exponential function and complex analysis in general to play a role in the theory of Fourier series. This will become clear at many stages in our development of Fourier series and their applications. In what follows, we illustrate the use of major tools from complex analysis, such as residues and Laurent series, in computing Fourier series.
 
 
-
-> [!exercise] EXAMPLE 5 Using residues to compute Fourier series
+> [!exercise|98c96581-2b4e-50a6-91b5-2356299fd4b6.local at=7b32faf3-c765-513b-94ce-ad3a17787986] EXAMPLE 5 Using residues to compute Fourier series
 > 
 > Find the Fourier series of $f(\theta)=\frac{1}{2+\cos \theta}$.
 
 
-**Solution** The function is $2 \pi$-periodic and even. We have $b_n=\frac{1}{\pi} \int_{-\pi}^\pi f(\theta) \sin n \theta d \theta=$ 0 , because $f(\theta) \sin n \theta$ is an odd function so its integral over a symmetric interval is 0 . In computing $a_n$ for $n \geq 0$, we will evaluate the integral
+##### solution
+
+The function is $2 \pi$-periodic and even. We have $b_n=\frac{1}{\pi} \int_{-\pi}^\pi f(\theta) \sin n \theta d \theta=$ 0 , because $f(\theta) \sin n \theta$ is an odd function so its integral over a symmetric interval is 0 . In computing $a_n$ for $n \geq 0$, we will evaluate the integral
 
 $$
 I_n=\int_0^{2 \pi} \frac{\cos n \theta}{2+\cos \theta} d \theta \quad(n=0,1, \ldots)
@@ -551,11 +582,11 @@
 I_n=\int_0^{2 \pi} \frac{\cos n \theta}{2+\cos \theta} d \theta+i \int_0^{2 \pi} \frac{\sin n \theta}{2+\cos \theta} d \theta=\int_0^{2 \pi} \frac{e^{i n \theta}}{2+\cos \theta} d \theta
 $$
 
-where we have used $e^{i n \theta}=\cos n \theta+i \sin n \theta$. We now use the method of Section 5.2, as follows. Let $z=e^{i \theta}, d z=i e^{i \theta} d \theta$ or $d \theta=\frac{d z}{i z}, z^n=e^{i n \theta}$, and $\cos \theta=\frac{e^{4 \theta}+e^{-i \theta}}{2}$. As $\theta$ varies over the interval $[0,2 \pi], z$ traverses the unit circle $C_1(0)$, in the positive direction. So
+where we have used $e^{i n \theta}=\cos n \theta+i \sin n \theta$. We now use the method of Section 5.2, as follows. Let $z=e^{i \theta}, d z=i e^{i \theta} d \theta$ or $d \theta=\frac{d z}{i z}, z^n=e^{i n \theta}$, and $\cos \theta=\frac{e^{i \theta}+e^{-i \theta}}{2}$. As $\theta$ varies over the interval $[0,2 \pi], z$ traverses the unit circle $C_1(0)$, in the positive direction. So
 
 $$
 \begin{aligned}
-I_n & =\int_0^{2 \pi} \frac{e^{i n \theta}}{2+\cos \theta} d \theta=\int_0^{2 \pi} \frac{e^{i n \theta}}{2+\frac{e^{i \cdot \theta}+e^{-1 \theta}}{2}} d \theta \\
+I_n & =\int_0^{2 \pi} \frac{e^{i n \theta}}{2+\cos \theta} d \theta=\int_0^{2 \pi} \frac{e^{i n \theta}}{2+\frac{e^{i \theta}+e^{-i \theta}}{2}} d \theta \\
 & =\int_{C_1(0)} \frac{2 z^n}{4+z+\frac{1}{z}} \frac{d z}{i z}=-i \int_{C_1(0)} \frac{2 z^n}{z^2+4 z+1} d z
 \end{aligned}
 $$
@@ -581,19 +612,27 @@
 \frac{1}{2+\cos \theta}=\frac{1}{\sqrt{3}}+\frac{2}{\sqrt{3}} \sum_{n=1}^{\infty}(-2+\sqrt{3})^n \cos n \theta
 $$
 
-which is valid for all $\theta$. Partial sums of the Fourier series are plotted in Figure 12. Note how fast the series is converging, because the coefficients are of the order $(-2+\sqrt{3})^n=\left|z_1\right|^n$, where $0<\left|z_1\right| \approx .3<1$.
-
-
-++++
-
+which is valid for all $\theta$. Partial sums of the Fourier series are plotted in Figure 12. Note how fast the series is converging, because the coefficients are of the order $|{-2+\sqrt{3}}|^n=\left|z_1\right|^n$, where $0<\left|z_1\right| \approx .3<1$.
+
+
+---
+```scientific-figure
+id: ea6de23a-9fcb-4be9-ab8a-5c0335280997
+numbered: false
+title: ""
+caption: "**Figure 12.** The function in Example 5 and the partial sums $s_n(\\theta)$ of its Fourier series for $n=1,2$."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 07 Fourier Series/images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-15_489_476_1787_39.jpg
+    caption: ""
+```
 
 Our next example generalizes the result of Example 5 and illustrates the use of Laurent series in computing Fourier series.
 
 
-
-
-
-> [!exercise] EXAMPLE 6 Using Laurent series to compute Fourier series
+> [!exercise|87d913f7-2551-530f-b2e9-8d9c53ad3dd1.local at=4236866d-5744-5eaf-a322-5373e1f5a255] EXAMPLE 6 Using Laurent series to compute Fourier series
 > 
 > Let $a>1$ be a real number. Derive the Fourier series representation
 > 
@@ -604,15 +643,29 @@
 > which is valid for all $\theta$.
 
 
-
-**Solution** The function is $2 \pi$-periodic and smooth. By Theorem 2, its Fourier series converges uniformly for all $\theta$ to $f(\theta)$. To find the Fourier series, we will not compute the Fourier coefficients directly; instead we will match the function with the restriction of a rational function and use Laurent series. As a first step, using the substitution $\cos \theta=\frac{1}{2}\left(z+\frac{1}{z}\right)$, where $z=e^{i \theta}$, we write
-
-$$
-\frac{1}{a+\cos \theta}=\frac{1}{a+\frac{1}{2}\left(z+\frac{1}{2}\right)}=\frac{2 z}{z^2+2 a z+1}
+##### solution
+
+The function is $2 \pi$-periodic and smooth. By Theorem 2, its Fourier series converges uniformly for all $\theta$ to $f(\theta)$. To find the Fourier series, we will not compute the Fourier coefficients directly; instead we will match the function with the restriction of a rational function and use Laurent series. As a first step, using the substitution $\cos \theta=\frac{1}{2}\left(z+\frac{1}{z}\right)$, where $z=e^{i \theta}$, we write
+
+$$
+\frac{1}{a+\cos \theta}=\frac{1}{a+\frac{1}{2}\left(z+\frac{1}{z}\right)}=\frac{2 z}{z^2+2 a z+1}
 $$
 
 
 Next, we expand $\frac{2 z}{z^2+2 a z+1}$ in an annulus that contains the unit circle $|z|=1$. As we will see in a moment, this will allow us to use the Laurent series with $z=e^{i \theta}$ and obtain the desired Fourier series.
+
+```scientific-figure
+id: 03c24675-6536-4907-ad0c-cb9b8ac0bf83
+numbered: false
+title: ""
+caption: "**Figure 13.** The annulus of convergence of the Laurent series in Example 6."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 07 Fourier Series/images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-17_487_440_887_54.jpg
+    caption: ""
+```
 
 The quadratic equation $z^2+2 a z+1=0$ has two real roots $z_1=-a-\sqrt{a^2-1}$ and $z_2=-a+\sqrt{a^2-1}$. Because $a>1$, we have $z_1<-1$ and $-1<z_2<0$ (you should check these assertions). By Theorem 1, Section 4.5, we have a Laurent series expansion in the annulus $\left|z_2\right|<|z|<\left|z_1\right|$ (Figure 13), and to find it we employ methods from Section 4.5. We have the partial fraction decomposition
 
@@ -630,7 +683,7 @@
 \begin{cases}A+B & =2 \\ A z_2+B z_1 & =0\end{cases}
 $$
 
-we find $A=\frac{2 z_1}{z_1-z_2}=-\frac{3}{\sqrt{a^2-1}}$ and $B=-\frac{2 z_2}{z_1-z_2}=\frac{z_2}{\sqrt{a^2-1}}$, where we have used $z_2-z_1=2 \sqrt{a^2-1}$. So we have the partial fraction decomposition
+we find $A=\frac{2 z_1}{z_1-z_2}=-\frac{z_1}{\sqrt{a^2-1}}$ and $B=-\frac{2 z_2}{z_1-z_2}=\frac{z_2}{\sqrt{a^2-1}}$, where we have used $z_2-z_1=2 \sqrt{a^2-1}$. So we have the partial fraction decomposition
 
 $$
 \frac{2 z}{z^2+2 a z+1}=\frac{1}{\sqrt{a^2-1}}\left(-\frac{z_1}{z-z_1}+\frac{z_2}{z-z_2}\right) .
@@ -667,27 +720,21 @@
 which is valid in the annulus $\left|z_2\right|<|z|<\left|z_1\right|$. In particular, for $z=e^{i \theta}$ the left side becomes $\frac{1}{a+\cos \theta}$ and the right side reduces to $\frac{1}{\sqrt{a^2-1}}\left\{1+\sum_{n=1}^{\infty} 2 z_2^n \cos n \theta\right\}$, after using the identity $z^n+\frac{1}{z^n}=2 \cos n \theta$, which completes the proof.
 
 
-
-++++
-
-
-
+---
 # Exercises 7.2
 
 
-
-> [!exercise]
+> [!exercise|699331b3-6b12-52e6-909b-5023ed91db6c.local at=1a24ded3-89ec-5d60-a47c-04ee7aafa743]
 > In Exercises 1-4, a $2 \pi$-periodic function is specified on the interval $[-\pi, \pi]$ in the accompanying figure (Figures 14-17). (a) Plot the function on the interval $[-3 \pi, 3 \pi]$.
 > (b) Plot its Fourier series (without computing it) on the interval $[-3 \pi, 3 \pi]$.
 > 
 > 
-> ![](Pasted%20image%2020260422002422.png)
-> 
-> 
-
-
-
-> [!exercise]
+> ![](Books/Asmar%20Applied%20Complex%20Analysis%20with%20Applications%20to%20Differential%20Equations/Chapter%2007%20Fourier%20Series/images/Pasted%20image%2020260422002422.png)
+> 
+> 
+
+
+> [!exercise|b968c3ae-a971-5d85-9c38-27a969dcd086.local at=28271cf6-2166-59ec-b5bd-603e888b0642]
 > In Exercises 5-16, the equation of a $2 \pi$-periodic function is given on an interval of length $2 \pi$. You are also given the Fourier series of the function. 
 > (a) Sketch the function and its Fourier series on $[-2 \pi, 2 \pi]$, and decide whether the series converges uniformly for all $x$. 
 > (b) Derive the given Fourier series.
@@ -737,7 +784,7 @@
 > 
 > 
 > For part (c), take $c=d=\pi / 2$.
-> 14. $f(x)=e^{-|x|}$ if $-\pi \leq x \leq \pi$.
+> 15. $f(x)=e^{-|x|}$ if $-\pi \leq x \leq \pi$.
 > 
 > Fourier series: $\quad \frac{e^\pi-1}{\pi e^\pi}+\frac{2}{\pi e^\pi} \sum_{n=1}^{\infty} \frac{1}{n^2+1}\left(e^\pi-(-1)^n\right) \cos n x$.
 > 
@@ -753,8 +800,7 @@
 > For part (c), take $c=d=\pi / 2$.
 
 
-
-> [!exercise]
+> [!exercise|73abe204-ebdf-5bc6-ba12-785d955e8e44.local at=f827e4cc-fec7-5540-926c-5c2e5d052d3c]
 > 17. (a) Use the Fourier series of Exercise 9 to obtain
 > 
 > $$
@@ -770,9 +816,7 @@
 > 
 
 
-
-
-> [!exercise]
+> [!exercise|a703add7-5b59-5497-ab48-22c096373257.local at=c4152d69-a76f-5159-96e0-e7172a6add49]
 > 18. Linearity of Fourier coefficients and Fourier series Let $\alpha$ and $\beta$ be any real numbers. Show that if $f$ and $g$ have Fourier coefficients $a_0, a_1, a_2, \ldots, b_1, b_2$, $\ldots$, respectively, $a_0^*, a_1^*, a_2^*, \ldots, b_1^*, b_2^*, \ldots$, then the function $\alpha f+\beta g$ has Fourier coefficients $\alpha a_0+\beta a_0^*, \alpha a_1+\beta a_1^*, \alpha a_2+\beta a_2^*, \ldots, \alpha b_1+\beta b_1^*, \alpha b_2+\beta b_2^*, \ldots$.
 > 
 > 
@@ -781,11 +825,7 @@
 ## Methods from Complex Analysis
 
 
-
-
-
-
-> [!exercise]
+> [!exercise|dff3ffa2-a891-558c-93f5-01d2fcbe5f43.local at=11b496af-a624-5973-9a5a-006f39400dea]
 > In Exercise 19-20, compute the Fourier series of the given function, following the method in Example 5. Verify your answer by using the result of Example 6.
 > 19. $\frac{1}{3+2 \cos \theta}$.
 > 20. $\frac{3 \sin \theta}{10-6 \cos \theta}$.
@@ -793,10 +833,7 @@
 > 
 
 
-
-
-
-> [!exercise]
+> [!exercise|dd58194c-d776-5a57-84b3-3aa106248705.local at=b77e2db7-9408-56e6-ab29-9c9ed9319931]
 > In Exercise 21-24, compute the Fourier series of the given function, using Laurent series as we did in Example 6.
 > 21. $\frac{1}{3+\cos \theta}$.
 > 22. $e^{2 \cos \theta}$.
@@ -806,8 +843,7 @@
 > 
 
 
-
-> [!exercise]
+> [!exercise|055c6b98-d113-50bc-bed3-52bc27e0fb04.local at=f21cf2bf-d1eb-533a-ac31-b49d5d00e28d]
 > In Exercise 25-26, derive the given Fourier series by using the Fourier series of Example 6 and various manipulations, including appropriate changes of variables.
 > 25. Let $a>1$ be a real number. Then
 > 
@@ -831,9 +867,7 @@
 > 
 
 
-
-
-> [!exercise]
+> [!exercise|771bda5a-9407-5660-bda8-dce5f5d36b4e.local at=6744d43b-c825-541b-beaa-f7fc467a8708]
 > 27. Let $a>1$ be a real number. Use Example 6 and Exercise 25 to derive the following formulas: for $n \geq 1$.
 > 
 > $$
@@ -849,40 +883,3 @@
 
 
 
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-

`````
