
# Editorial records

Reading note: 7.3 Fourier Series of Functions with Arbitrary Periods.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Callout 261: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Fourier Series Representation for an Arbitrary Period
> Let $p>0$; $f(x\pm)$ denote one-sided limits.
>
> Suppose that $f$ is a $2 p$-periodic piecewise smooth function. Then $f$ has a unique Fourier series representation
>
> $$
> \frac{f(x-)+f(x+)}{2}=a_0+\sum_{n=1}^{\infty}\left(a_n \cos \frac{n \pi}{p} x+b_n \sin \frac{n \pi}{p} x\right),
> $$
>
> where the Fourier coefficients are given by
>
> $$
> a_0=\frac{1}{2 p} \int_{-p}^p f(x) d x
> $$
>
> $$
> a_n=\frac{1}{p} \int_{-p}^p f(x) \cos \frac{n \pi}{p} x d x \quad(n=1,2, \ldots),
> $$
>
> $$
> b_n=\frac{1}{p} \int_{-p}^p f(x) \sin \frac{n \pi}{p} x d x \quad(n=1,2, \ldots)
> $$
>
> If $f$ is continuous at $x$, then the Fourier series converges to $f(x)$. The series converges uniformly for all $x$ if and only if $f$ is continuous for all $x$.
````
### After

````text
> [!theorem] Fourier Series Representation: Arbitrary Period
> Let $p>0$; $f(x\pm)$ denote one-sided limits.
>
> Suppose that $f$ is a $2 p$-periodic piecewise smooth function. Then $f$ has a unique Fourier series representation
>
> $$
> \frac{f(x-)+f(x+)}{2}=a_0+\sum_{n=1}^{\infty}\left(a_n \cos \frac{n \pi}{p} x+b_n \sin \frac{n \pi}{p} x\right),
> $$
>
> where the Fourier coefficients are given by
>
> $$
> a_0=\frac{1}{2 p} \int_{-p}^p f(x) d x
> $$
>
> $$
> a_n=\frac{1}{p} \int_{-p}^p f(x) \cos \frac{n \pi}{p} x d x \quad(n=1,2, \ldots),
> $$
>
> $$
> b_n=\frac{1}{p} \int_{-p}^p f(x) \sin \frac{n \pi}{p} x d x \quad(n=1,2, \ldots)
> $$
>
> If $f$ is continuous at $x$, then the Fourier series converges to $f(x)$. The series converges uniformly for all $x$ if and only if $f$ is continuous for all $x$.
````

## 2. Callout 263: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!property] Parity of Products of Even and Odd Functions
> On a domain symmetric about zero, the pointwise product of two even functions is even; the product of an even and an odd function is odd; and the product of two odd functions is even.
````
### After

````text
> [!property] Parity of Products of Even and Odd Functions
> For pointwise products of functions on a domain symmetric about zero,
>
> $$
> \begin{aligned}
> (\text { Even })(\text { Even }) & =\text { Even } \\
> (\text { Even })(\text { Odd }) & =\text { Odd } \\
> (\text { Odd })(\text { Odd }) & =\text { Even }
> \end{aligned}
> $$
````

## 3. Callout 264: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Cosine and Sine Fourier Series of Even and Odd Periodic Functions
> Let $p>0$. Suppose $f$ is $2p$-periodic and has a convergent Fourier representation $f(x)=a_0+\sum_{n=1}^{\infty}(a_n\cos(n\pi x/p)+b_n\sin(n\pi x/p))$ at every $x$, with its Fourier coefficients. Then (i) $f$ is even if and only if $b_n=0$ for all $n$. In this case
>
> $$
> f(x)=a_0+\sum_{n=1}^{\infty} a_n \cos \frac{n \pi}{p} x,
> $$
>
> where
>
> $$
> a_0=\frac{1}{p} \int_0^p f(x) d x, \quad \text { and } \quad a_n=\frac{2}{p} \int_0^p f(x) \cos \frac{n \pi}{p} x d x \quad(n=1,2, \ldots)
> $$
>
> (ii) $f$ is odd if and only if $a_n=0$ for all $n\geq0$. In this case
>
> $$
> f(x)=\sum_{n=1}^{\infty} b_n \sin \frac{n \pi}{p} x
> $$
>
> where
>
> $$
> b_n=\frac{2}{p} \int_0^p f(x) \sin \frac{n \pi}{p} x d x \quad(n=1,2, \ldots)
> $$
````
### After

````text
> [!theorem] Fourier Series of Even and Odd Functions
> Let $p>0$. Suppose $f$ is $2p$-periodic and has a convergent Fourier representation $f(x)=a_0+\sum_{n=1}^{\infty}(a_n\cos(n\pi x/p)+b_n\sin(n\pi x/p))$ at every $x$, with its Fourier coefficients. Then (i) $f$ is even if and only if $b_n=0$ for all $n$. In this case
>
> $$
> f(x)=a_0+\sum_{n=1}^{\infty} a_n \cos \frac{n \pi}{p} x,
> $$
>
> where
>
> $$
> a_0=\frac{1}{p} \int_0^p f(x) d x, \quad \text { and } \quad a_n=\frac{2}{p} \int_0^p f(x) \cos \frac{n \pi}{p} x d x \quad(n=1,2, \ldots)
> $$
>
> (ii) $f$ is odd if and only if $a_n=0$ for all $n\geq0$. In this case
>
> $$
> f(x)=\sum_{n=1}^{\infty} b_n \sin \frac{n \pi}{p} x
> $$
>
> where
>
> $$
> b_n=\frac{2}{p} \int_0^p f(x) \sin \frac{n \pi}{p} x d x \quad(n=1,2, \ldots)
> $$
````

## 4. Move editorial commentary out of the reading note.

### Before

````text
*Editorial corrections to source details: The sum in Exercise 6 begins at $n=1$; Exercise 8 requires $d>0$. In Example 3 the scaling factor is $2c/\pi$. Exercise 26’s differentiated series equals $f^{\prime}$ at continuity points of the derivative and its one-sided average at derivative jumps.*
````
### After

````text

````

## Source-to-current comparison

Source: /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 07 Fourier Series/7.3 Fourier Series of Functions with Arbitrary Periods.md

This exact comparison preserves the full change evidence, including formatting, OCR corrections, restored source wording, and required standalone context. The entries above explain the recovery edits. The comparison is not a claim that every difference is a correction; component serialization, callout wrapping, and printed labels outside callouts are formatting.

`````diff
--- /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 07 Fourier Series/7.3 Fourier Series of Functions with Arbitrary Periods.md
+++ /Users/gradyclopton/ObsidianVaults/complex_analysis/Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 07 Fourier Series/7.3 Fourier Series of Functions with Arbitrary Periods.md
@@ -18,50 +18,51 @@
 Hence $g$ is $2 \pi$-periodic. This reduction enables us to extend the main results of Section 7.2 to functions of arbitrary period.
 
 
-
-> [!figure] Figure 1
-> 
-> ![](Pasted%20image%2020260422003938.png)
-> Figure 1 A $2 p$-periodic function.
-
-
-
-
+```scientific-figure
+id: 70484e01-00b2-4d40-882c-e22c60a219c3
+numbered: false
+title: ""
+caption: "**Figure 1.** A $2 p$-periodic function."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 07 Fourier Series/images/Pasted image 20260422003938.png
+    caption: ""
+```
+
+
+<!-- Source label: Fourier Series Representation: Arbitrary Period -->
 > [!theorem] Fourier Series Representation: Arbitrary Period
+> Let $p>0$; $f(x\pm)$ denote one-sided limits.
+>
 > Suppose that $f$ is a $2 p$-periodic piecewise smooth function. Then $f$ has a unique Fourier series representation
-> 
+>
 > $$
 > \frac{f(x-)+f(x+)}{2}=a_0+\sum_{n=1}^{\infty}\left(a_n \cos \frac{n \pi}{p} x+b_n \sin \frac{n \pi}{p} x\right),
 > $$
-> 
+>
 > where the Fourier coefficients are given by
-> 
+>
 > $$
 > a_0=\frac{1}{2 p} \int_{-p}^p f(x) d x
 > $$
-> 
-> (4)
-> 
+>
 > $$
 > a_n=\frac{1}{p} \int_{-p}^p f(x) \cos \frac{n \pi}{p} x d x \quad(n=1,2, \ldots),
 > $$
-> 
-> 
+>
 > $$
 > b_n=\frac{1}{p} \int_{-p}^p f(x) \sin \frac{n \pi}{p} x d x \quad(n=1,2, \ldots)
 > $$
-> 
-> 
+>
 > If $f$ is continuous at $x$, then the Fourier series converges to $f(x)$. The series converges uniformly for all $x$ if and only if $f$ is continuous for all $x$.
-
 
 
 > [!NOTE]
 > By Theorem 1, Section 7.1, all the integrals $\int_{-p}^p$ can be replaced by $\int_0^{2 p}$ without changing the values of the coefficients.
 
 
-
-
 **Proof** Since $f$ is piecewise smooth, it follows that the $2 \pi$-periodic function $g$ defined by (1) is also piecewise smooth. By Theorem 1 of Section 7.2 we have
 
 $$
@@ -91,29 +92,34 @@
 Formulas (4) and (5) are derived in a similar way. The details are left to the exercises. The uniqueness and the uniform convergence in the theorem follow from the corresponding results for $2 \pi$-periodic functions (Corollary 1 and Theorem 2, Section 7.2).
 
 
-+++
-
-
+---
 > [!exercise] EXAMPLE 1 A Fourier series with arbitrary period
 > 
 > Find the Fourier series of the $2 p$-periodic function given by $f(x)=|x|$ if $-p \leq x \leq p$ (Figure 2).
 > 
 
 
-
-**Solution** We compute the Fourier coefficients using Theorem 1. The area under the graph of $f$ in Figure 2 gives
+##### solution
+
+We compute the Fourier coefficients using Theorem 1. The area under the graph of $f$ in Figure 2 gives
 
 $$
 a_0=\frac{1}{2 p} \int_{-p}^p f(x) d x=\frac{p}{2}
 $$
 
 
-> [!figure] Figure 2
-> 
-> ![](Pasted%20image%2020260422004124.png)
-> Figure 2 Triangular wave with period $2 p$.
-> 
-
+```scientific-figure
+id: 355f3736-0941-4c54-98a5-cb5a7312c1cc
+numbered: false
+title: ""
+caption: "**Figure 2.** Triangular wave with period $2 p$."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 07 Fourier Series/images/Pasted image 20260422004124.png
+    caption: ""
+```
 
 
 To compute $a_n$ we take advantage of the fact that $f(x) \cos \frac{n \pi}{p} x$ is an even function and write
@@ -135,27 +141,24 @@
 Because $f$ is continuous and piecewise smooth, Theorem 1 implies that the Fourier series converges uniformly to $f(x)$ for all $x$, as can be seen in Figure 3.
 
 
-
-
-> [!figure] Figure 3
-> 
-> ![](Pasted%20image%2020260422004645.png)
-> Figure 3 Partial sums of the Fourier series $(p=1)$, in Example 1.
-
-
-
-
-
-
-++++
-
-
-
+```scientific-figure
+id: 7346198e-9019-4e1e-bec1-f88761a582a6
+numbered: false
+title: ""
+caption: "**Figure 3.** Partial sums of the Fourier series $(p=1)$, in Example 1."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 07 Fourier Series/images/Pasted image 20260422004645.png
+    caption: ""
+```
+
+
+---
 Sometimes we can derive a new Fourier series from a known one without performing many additional computations. The following examples illustrate this process.
 
 
-
-
 > [!exercise] EXAMPLE 2 Triangular wave with arbitrary period and amplitude
 > 
 > Find the Fourier series of the $2 p$-periodic function given by
@@ -166,16 +169,23 @@
 > 
 
 
-
-**Solution** Comparing Figures 4 and 2 shows that we can obtain the graph of $g$ by reflecting the graph of $f$ in the $x$-axis, translating it upward by $p$ units, and then scaling it by a factor of $\frac{a}{p}$. 
-
-
-
-> [!figure] Figure 4
-> 
-> ![](Pasted%20image%2020260422004509.png)
-> Figure 4 A $2 p$-periodic triangular wave.
-
+##### solution
+
+Comparing Figures 4 and 2 shows that we can obtain the graph of $g$ by reflecting the graph of $f$ in the $x$-axis, translating it upward by $p$ units, and then scaling it by a factor of $\frac{a}{p}$. 
+
+
+```scientific-figure
+id: 56d17617-06b5-48c0-bfcb-3ca8bde69112
+numbered: false
+title: ""
+caption: "**Figure 4.** A $2 p$-periodic triangular wave."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 07 Fourier Series/images/Pasted image 20260422004509.png
+    caption: ""
+```
 
 
 This is expressed by writing
@@ -203,13 +213,10 @@
 
 (You should check that the special case with $p=a=\pi$ yields the Fourier series of Example 2 of the previous section.)
 
-++++
-
-
+---
 Changing variables as we did at the outset of the section can be very useful in deriving new Fourier series from known ones.
 
 
-
 > [!exercise] EXAMPLE 3 Varying the period in a Fourier series
 > 
 > Find the Fourier series of the function in Figure 5.
@@ -217,28 +224,38 @@
 > 
 > 
 > 
-> > [!figure] Figure 5
-> > 
-> > ![](Pasted%20image%2020260422004302.png)
-> > Figure 5 A $2 p$-periodic sawlooth function.
-> 
-> 
-
-
-**Solution** Let us start by defining the function in Figure 5. On the interval $0<x<2 p$, we have $f(x)=c\left(1-\frac{\pi}{p}\right)$. Now, from Example 1, Section 7.2, we have the Fourier series expansion
+> ```scientific-figure
+> id: 2c4fa2ef-4a56-459b-ae7d-fc2da850abd2
+> numbered: false
+> title: ""
+> caption: "**Figure 5.** A $2 p$-periodic sawlooth function."
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 07 Fourier Series/images/Pasted image 20260422004302.png
+>     caption: ""
+> ```
+> 
+> 
+
+
+##### solution
+
+Let us start by defining the function in Figure 5. On the interval $0<x<2 p$, we have $f(x)=c\left(1-\frac{x}{p}\right)$. Now, from Example 1, Section 7.2, we have the Fourier series expansion
 
 $$
 \frac{1}{2}(\pi-x)=\sum_{n=1}^{\infty} \frac{\sin n x}{n}, \text { for } 0<x<2 \pi
 $$
 
-Replacing $x$ by $\frac{t}{p} x$ in the formula and the interval for $x$, we get
+Replacing $x$ by $\frac{\pi}{p} x$ in the formula and the interval for $x$, we get
 
 $$
 \frac{1}{2}\left(\pi-\frac{\pi}{p} x\right)=\sum_{n=1}^{\infty} \frac{\sin \frac{n \pi}{p} x}{n}, \text { for } 0<\frac{\pi}{p} x<2 \pi \text {. }
 $$
 
 
-Simplifying and multiplying both sides by $c$ to match the formula for $f$, we get
+Simplifying and multiplying both sides by $2c/\pi$ to match the formula for $f$, we get
 
 $$
 c\left(1-\frac{x}{p}\right)=\frac{2 c}{\pi} \sum_{n=1}^{\infty} \frac{\sin \frac{n \pi}{p} x}{n}, \text { for } 0<x<2 p
@@ -247,21 +264,17 @@
 which yields the Fourier series of $f$.
 
 
-++++
-
-
+---
 # Even and Odd Functions
 As we noticed already, geometric considerations are helpful in computing Fourier coefficients. This is particularly the case when dealing with even and odd functions. Recall the following definitions:
 
 
-
-> [!equation]
+<!-- Source label:  -->
+> [!definition] Even and Odd Functions
+> Let the domain of $f$ be symmetric about zero.
+>
 > A function $f$ is even if $f(-x)=f(x)$ for all $x$.
 > A function $f$ is odd if $f(-x)=-f(x)$ for all $x$.
-> 
-
-
-
 
 
 It is clear from the graphs in Figure 6 (or by a simple change of variables) that if $f$ is even, then
@@ -279,22 +292,27 @@
 $$
 
 
-
-> [!figure] Figure 6
-> 
-> ![](Pasted%20image%2020260422004844.png)
-> Figure 6 (a) Even function: The graph is symmetric with respect to the $y$-axis. (b) Odd function: The graph is symmetric with respect to the origin.
-
-
-
+```scientific-figure
+id: 0096fa0e-e549-4990-ae61-24d364b9b31d
+numbered: false
+title: ""
+caption: "**Figure 6.** (a) Even function: The graph is symmetric with respect to the $y$-axis. (b) Odd function: The graph is symmetric with respect to the origin."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 07 Fourier Series/images/Pasted image 20260422004844.png
+    caption: ""
+```
 
 
 The following useful properties concerning the products of these functions are easily verified.
 
 
-
-> [!equation]
-> 
+<!-- Source label:  -->
+> [!property] Parity of Products of Even and Odd Functions
+> For pointwise products of functions on a domain symmetric about zero,
+>
 > $$
 > \begin{aligned}
 > (\text { Even })(\text { Even }) & =\text { Even } \\
@@ -302,63 +320,68 @@
 > (\text { Odd })(\text { Odd }) & =\text { Even }
 > \end{aligned}
 > $$
-> 
-
 
 
 These simple product properties can be used to simplify finding the Fourier coefficients of even and odd functions, as we now show.
 
 
-
-
-
+<!-- Source label: Fourier Series of Even and Odd Functions -->
 > [!theorem] Fourier Series of Even and Odd Functions
-> Suppose that $f$ is $2 p$-periodic and has the Fourier series representation (2). Then (i) $f$ is even if and only if $b_n=0$ for all $n$. In this case
-> 
+> Let $p>0$. Suppose $f$ is $2p$-periodic and has a convergent Fourier representation $f(x)=a_0+\sum_{n=1}^{\infty}(a_n\cos(n\pi x/p)+b_n\sin(n\pi x/p))$ at every $x$, with its Fourier coefficients. Then (i) $f$ is even if and only if $b_n=0$ for all $n$. In this case
+>
 > $$
 > f(x)=a_0+\sum_{n=1}^{\infty} a_n \cos \frac{n \pi}{p} x,
 > $$
-> 
+>
 > where
-> 
+>
 > $$
 > a_0=\frac{1}{p} \int_0^p f(x) d x, \quad \text { and } \quad a_n=\frac{2}{p} \int_0^p f(x) \cos \frac{n \pi}{p} x d x \quad(n=1,2, \ldots)
 > $$
-> 
-> (ii) $f$ is odd if and only if $a_n=0$ for all $n$. In this case
-> 
+>
+> (ii) $f$ is odd if and only if $a_n=0$ for all $n\geq0$. In this case
+>
 > $$
 > f(x)=\sum_{n=1}^{\infty} b_n \sin \frac{n \pi}{p} x
 > $$
-> 
+>
 > where
-> 
+>
 > $$
 > b_n=\frac{2}{p} \int_0^p f(x) \sin \frac{n \pi}{p} x d x \quad(n=1,2, \ldots)
 > $$
-> 
-> 
 
 
 **Proof** (i) If $f(x)=a_0+\sum_{n=1}^{\infty} a_n \cos \frac{n \pi}{p} x$, then clearly it is even. Conversely, suppose that $f$ is even. Use (10) and the fact that $f(x) \sin \frac{n \pi}{p} x$ is odd to get that $b_n=0$ for all $n$. Use (3), (4), (9) and the fact that $f(x) \cos \frac{n \pi}{p} x$ is even to get the formulas for the coefficients in (i). The proof of (ii) is similar and is left as an exercise.
 
 
-+++
-
-
-
-
+---
 > [!exercise] EXAMPLE 4 Fourier series of an even function
 > 
 > Find the Fourier series of the 2 -periodic function $f(x)=1-x^2$ if $-1<x<1$.
 
 
-**Solution** The function $f$ is even (see Figure 7); hence $b_n=0$ for all $n$. compute the $a_n$ 's, we use Theorem 2 with $p=1$ and get
+##### solution
+
+The function $f$ is even (see Figure 7); hence $b_n=0$ for all $n$. To compute the $a_n$ 's, we use Theorem 2 with $p=1$ and get
 
 $$
 a_0=\int_0^1\left(1-x^2\right) d x=\frac{2}{3}
 $$
 
+```scientific-figure
+id: 8728aaee-1320-4e69-afe3-460a4378fded
+numbered: false
+title: ""
+caption: "**Figure 7.** An even function."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 07 Fourier Series/images/18b4a275-332c-4c46-b6df-2b0f8cb200e4-26_385_535_490_108.jpg
+    caption: ""
+```
+
 and
 
 $$
@@ -381,34 +404,41 @@
 for all $x$. Since $f$ is continuous and piecewise smooth for all $x$, its Fourier series converges uniformly to $f(x)$, as illustrated in Figure 8.
 
 
-
-> [!figure] Figure 8
-> 
-> ![](Pasted%20image%2020260422005101.png)
-> Figure 8 Partial sums of the Fourier series in Example 4.
-
-
-
-++++
-
-
-
-> [!exercise]
-> EXAMPLE 5 Fourier series of an odd function
-> <span style="color:#ff0000; font-weight:bold">Need exercise statement</span>
-
+```scientific-figure
+id: 5154a75a-699d-45c2-bf06-c53bc8fb9bb5
+numbered: false
+title: ""
+caption: "**Figure 8.** Partial sums of the Fourier series in Example 4."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 07 Fourier Series/images/Pasted image 20260422005101.png
+    caption: ""
+```
+
+
+---
+> [!exercise] EXAMPLE 5 Fourier series of an odd function
+> Find the Fourier series of the $\pi$-periodic function defined by $f(x)=x\cos x$ for $-\pi/2<x<\pi/2$.
+
+##### solution
 
 The function $f(x)=x \cos x$, if $-\frac{\pi}{2}<x<\frac{\pi}{2}$, and $f(x+\pi)=f(x)$ otherwise, is shown in Figure 9. 
 
 
-
-
-> [!figure] Figure 5
-> 
-> ![](Pasted%20image%2020260422005207.png)
-> Figure 9 The odd function in Example 5.
-
-
+```scientific-figure
+id: 96afce5b-ef28-4d85-9c2f-9cc79f185ed0
+numbered: false
+title: ""
+caption: "**Figure 9.** The odd function in Example 5."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 07 Fourier Series/images/Pasted image 20260422005207.png
+    caption: ""
+```
 
 
 It is $\pi$-periodic and odd. From Theorem 2, its Fourier series is given by
@@ -432,12 +462,9 @@
 
 and the integral formula
 
-in
-
 $$
 \int u \sin u d u=\sin u-u \cos u+C .
 $$
-
 
 
 Computing with the help of these formulas, we find
@@ -465,23 +492,78 @@
 Figure 10 illustrates the uniform convergence of the Fourier series to $f(x)$. Along with $f(x)$, we have plotted the partial sums $s_2(x)$ and $s_4(x)$. The graphs of $s_4(x)$ and $f(x)$ can hardly be distinguished from one another, which suggests that the Fourier series converges very fast to $f(x)$.
 
 
-
-> [!figure] Figure 10
-> 
-> ![](Pasted%20image%2020260422005410.png)
-> Figure 10 Graphs of $f(x)$, $s_2(x)$ and $s_4(x)$, in Example 5.
-
-
-
-++++
-
-
+```scientific-figure
+id: 00fd1b17-285e-4cd7-a7cc-d972e01b90f3
+numbered: false
+title: ""
+caption: "**Figure 10.** Graphs of $f(x)$, $s_2(x)$ and $s_4(x)$, in Example 5."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 07 Fourier Series/images/Pasted image 20260422005410.png
+    caption: ""
+```
+
+
+---
 # Exercises 7.3
 
 
-
 > [!exercise]
 > In Exercises 1-10, a 2p-periodic function is given on an interval of length $2 p$ in the accompanying figure (Figures 11-20). (a) State whether the function is even, odd, or neither. (b) Derive the given Fourier series, and determine its values at the points of discontinuity. State if the series converges uniformly for all $x$. (Most of these Fourier series can be derived from earlier examples and exercises, as illustrated by Examples 3 and 4.)
+> ```horizontal
+> 
+> ![](Books/Asmar%20Applied%20Complex%20Analysis%20with%20Applications%20to%20Differential%20Equations/Chapter%2007%20Fourier%20Series/images/Pasted%20image%2020260422005821.png)
+> 
+> ---
+> 
+> ![](Books/Asmar%20Applied%20Complex%20Analysis%20with%20Applications%20to%20Differential%20Equations/Chapter%2007%20Fourier%20Series/images/Pasted%20image%2020260422010039.png)
+> 
+> ---
+> 
+> ![](Books/Asmar%20Applied%20Complex%20Analysis%20with%20Applications%20to%20Differential%20Equations/Chapter%2007%20Fourier%20Series/images/Pasted%20image%2020260422010049.png)
+> 
+> ---
+> 
+> ![](Books/Asmar%20Applied%20Complex%20Analysis%20with%20Applications%20to%20Differential%20Equations/Chapter%2007%20Fourier%20Series/images/Pasted%20image%2020260422010103.png)
+> 
+> ```
+> 
+> 
+> 
+> ```horizontal
+> 
+> ![](Books/Asmar%20Applied%20Complex%20Analysis%20with%20Applications%20to%20Differential%20Equations/Chapter%2007%20Fourier%20Series/images/Pasted%20image%2020260422010145.png)
+> 
+> ---
+> 
+> ![](Books/Asmar%20Applied%20Complex%20Analysis%20with%20Applications%20to%20Differential%20Equations/Chapter%2007%20Fourier%20Series/images/Pasted%20image%2020260422010154.png)
+> 
+> ---
+> 
+> ![](Books/Asmar%20Applied%20Complex%20Analysis%20with%20Applications%20to%20Differential%20Equations/Chapter%2007%20Fourier%20Series/images/Pasted%20image%2020260422010204.png)
+> 
+> ---
+> 
+> ![](Books/Asmar%20Applied%20Complex%20Analysis%20with%20Applications%20to%20Differential%20Equations/Chapter%2007%20Fourier%20Series/images/Pasted%20image%2020260422010215.png)
+> 
+> ```
+> 
+> 
+> 
+> ```horizontal
+> 
+> ![](Books/Asmar%20Applied%20Complex%20Analysis%20with%20Applications%20to%20Differential%20Equations/Chapter%2007%20Fourier%20Series/images/Pasted%20image%2020260422010252.png)
+> 
+> ---
+> 
+> ![](Books/Asmar%20Applied%20Complex%20Analysis%20with%20Applications%20to%20Differential%20Equations/Chapter%2007%20Fourier%20Series/images/Pasted%20image%2020260422010302.png)
+> 
+> ```
+> 
+> 
+> 
 > 1.
 > 
 > $$
@@ -491,73 +573,10 @@
 > 
 > Fourier series: $\quad \frac{4}{\pi} \sum_{k=0}^{\infty} \frac{1}{(2 k+1)} \sin \frac{(2 k+1) \pi}{p} x$.
 > 
-> 
-> 
-> ```horizontal
-> 
-> ![](Pasted%20image%2020260422005821.png)
-> 
-> ---
-> 
-> ![](Pasted%20image%2020260422010039.png)
-> 
-> ---
-> 
-> ![](Pasted%20image%2020260422010049.png)
-> 
-> ---
-> 
-> ![](Pasted%20image%2020260422010103.png)
-> 
-> ```
-> 
-> 
-> 
-> ```horizontal
-> 
-> ![](Pasted%20image%2020260422010145.png)
-> 
-> ---
-> 
-> ![](Pasted%20image%2020260422010154.png)
-> 
-> ---
-> 
-> ![](Pasted%20image%2020260422010204.png)
-> 
-> ---
-> 
-> ![](Pasted%20image%2020260422010215.png)
-> 
-> ```
-> 
-> 
-> 
-> ```horizontal
-> 
-> ![](Pasted%20image%2020260422010252.png)
-> 
-> ---
-> 
-> ![](Pasted%20image%2020260422010302.png)
-> 
-> ```
-> 
-> 
-> 
-> 1.
-> 
-> $$
-> f(x)= \begin{cases}1 & \text { if } 0<x<p, \\ -1 & \text { if }-p<x<0 .\end{cases}
-> $$
-> 
-> 
-> Fourier series: $\quad \frac{4}{\pi} \sum_{k=0}^{\infty} \frac{1}{(2 k+1)} \sin \frac{(2 k+1) \pi}{p} x$.
-> 
 > 2. $f(x)=x$ if $-p<x<p$. [Hint: Exercise 13, Section 7.2.]
 > 
 > Fourier series: $\quad \frac{2 p}{\pi} \sum_{n=1}^{\infty} \frac{(-1)^{n+1}}{n} \sin \left(\frac{n \pi}{p} x\right)$.
-> 3. $f(x)=a\left(1-\left(\frac{z}{p}\right)^2\right)$ if $-p \leq x \leq p,(a \neq 0)$.
+> 3. $f(x)=a\left(1-\left(\frac{x}{p}\right)^2\right)$ if $-p \leq x \leq p,(a \neq 0)$.
 > 
 > Fourier series: $\quad \frac{2}{3} a+4 a \sum_{n=1}^{\infty} \frac{(-1)^{n+1}}{(n \pi)^2} \cos \left(\frac{n \pi}{p} x\right)$.
 > 4. $f(x)=x^2$ if $-p \leq x \leq p$. [Hint: Use Exercise 3.]
@@ -578,7 +597,7 @@
 > $$
 > 
 > where $0<d<p$.
-> Fourier series: $\frac{c d}{p}+\frac{2 c}{\pi} \sum_{n=0}^{\infty} \frac{\sin \left(\frac{d n \pi}{p}\right)}{n} \cos \left(\frac{n \pi}{p} x\right)$.
+> Fourier series: $\frac{c d}{p}+\frac{2 c}{\pi} \sum_{n=1}^{\infty} \frac{\sin \left(\frac{d n \pi}{p}\right)}{n} \cos \left(\frac{n \pi}{p} x\right)$.
 > 7.
 > 
 > $$
@@ -593,11 +612,11 @@
 > f(x)= \begin{cases}-\frac{c}{d}(x-d) & \text { if } 0 \leq x \leq d, \\ 0 & \text { if } d \leq|x| \leq p, \\ \frac{c}{d}(x+d) & \text { if }-d \leq x \leq 0 .\end{cases}
 > $$
 > 
-> where $0 \leq d \leq p$.
+> where $0<d\leq p$.
 > Fourier series: $\quad \frac{c d}{2 p}+\frac{2 c p}{d \pi^2} \sum_{n=1}^{\infty} \frac{1}{n^2}\left(1-\cos \left(\frac{d n \pi}{p}\right)\right) \cos \left(\frac{n \pi}{p} x\right)$.
 > 
 > 
-> 5. $f(x)=e^{-c|x|}(c \neq 0)$ for $|x| \leq p$.
+> 9. $f(x)=e^{-c|x|}(c \neq 0)$ for $|x| \leq p$.
 > 
 > Fourier series: $\frac{1}{p c}\left(1-e^{-c p}\right)+2 c p \sum_{n=1}^{\infty} \frac{1}{c^2 p^2+(n \pi)^2}\left(1-e^{-c p}(-1)^n\right) \cos \left(\frac{n \pi}{p} x\right)$.
 > 10.
@@ -611,8 +630,6 @@
 > 
 > 
 > 
-
-
 
 
 > [!exercise]
@@ -624,9 +641,6 @@
 > 
 
 
-
-
-
 > [!exercise]
 > In Exercises 13-14 a function is given over one period by a figure (Figures 21-22).
 > (a) Find its Fourier series. [Hint: Use Exercise 1.]
@@ -634,14 +648,20 @@
 > 
 > 
 > 
-> > [!figure]
-> > ![](Pasted%20image%2020260422010625.png)
-> > 
-> > 
-> 
-> 
-
-
+> ```scientific-figure
+> id: 64da4c7c-b3ea-4e70-aba2-075490211c6d
+> numbered: false
+> title: ""
+> caption: ""
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 07 Fourier Series/images/Pasted image 20260422010625.png
+>     caption: ""
+> ```
+> 
+> 
 
 
 > [!exercise]
@@ -654,8 +674,6 @@
 > (b) What happens to the Fourier coefficients as $d$ approaches $p$ ? Justify your answer.
 > 
 > 
-
-
 
 
 > [!exercise]
@@ -666,9 +684,6 @@
 > 
 
 
-
-
-
 > [!exercise]
 > 18. Derive (4) and (5) of Theorem 1. **(Hint: Study the proof of Theorem 1.)**
 > 19. Prove part (ii) of Theorem 2.
@@ -676,18 +691,12 @@
 > 
 
 
-
-
-
-> [!exercise]
-> Project Problem: Decomposition into even and odd parts. Do Exercise 20 and any one of 21-24. You will discover how an arbitrary function can be decom-
-> 
-> 
-> posed into the sum of an even and odd function.
+> [!exercise]
+> Project Problem: Decomposition into even and odd parts. Do Exercise 20 and any one of 21-24. You will discover how an arbitrary function can be decomposed into the sum of an even and odd function.
 > 20. Let $f$ be an arbitrary function defined for all real numbers. Consider the functions
 > 
 > $$
-> f_{\mathrm{e}}(x)=\frac{f(x)+f(-x)}{2} \text { and } f_0(x)=\frac{f(x)-f(-x)}{2}
+> f_{\mathrm{e}}(x)=\frac{f(x)+f(-x)}{2} \text { and } f_{\mathrm{o}}(x)=\frac{f(x)-f(-x)}{2}
 > $$
 > 
 > (a) Show that $f_{\mathrm{e}}$ is even and $f_{\mathrm{o}}$ is odd.
@@ -698,25 +707,29 @@
 > 
 
 
-
 > [!exercise]
 > In Exercises 21-24, a 2-periodic function is given by its graph over the interval $[-1,1]$ (Figures 23-
 > 26). In each case, 
-> (a) determine and plot $f_0$ and $f_0$ (see Exercise 20).
+> (a) determine and plot $f_{\mathrm{e}}$ and $f_{\mathrm{o}}$ (see Exercise 20).
 > (b) Find the Fourier series of $f_e$ and $f_o$, and then deduce the Fourier series of $f$.
 > 
 > 
 > 
-> > [!figure]
-> > 
-> > ![](Pasted%20image%2020260422011141.png)
-> > 
-> > 
-> 
-> 
-> 
-
-
+> ```scientific-figure
+> id: d472eaca-82ee-4dde-8d8c-10babeb158a3
+> numbered: false
+> title: ""
+> caption: ""
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 07 Fourier Series/images/Pasted image 20260422011141.png
+>     caption: ""
+> ```
+> 
+> 
+> 
 
 
 > [!exercise]
@@ -742,7 +755,7 @@
 > f(x)=a_0+\sum_{n=1}^{\infty}\left(a_n \cos \frac{n \pi}{p} x+b_n \sin \frac{n \pi}{p} x\right),
 > $$
 > 
-> then
+> then, at every continuity point of $f^{\prime}$ (and with the one-sided average on the left at a jump),
 > 
 > $$
 > f^{\prime}(x)=\sum_{n=1}^{\infty}\left(-n a_n \frac{\pi}{p} \sin \frac{n \pi}{p} x+n b_n \frac{\pi}{p} \cos \frac{n \pi}{p} x\right) .
@@ -753,7 +766,6 @@
 > In most cases in this book, $f$ and $f^{\prime}$ are piecewise smooth. Thus, according to Exercise 26, to differentiate term by term the Fourier series in these cases, it is enough to check that $f$ is continuous. It is important to note that if $f$ fails to satisfy some of the assumptions of Exercise 26, then we cannot in general differentiate the series term by term. See Exercises 31-32.
 > 
 > 
-
 
 
 > [!exercise]
@@ -763,25 +775,39 @@
 > 
 
 
-
-> [!exercise]
-> 27. Use the Fourier series of Exercise 8 to find the Fourier series of the $2 p$-periodic function in the Figure 27.
-> 
-> 
-> > [!figure]
-> > ![](Pasted%20image%2020260422011732.png)
-> > 
-> 
-> 
-> 28. Use the Fourier series of Exercise 10 to find the Fourier series of the $2 p$-periodic function in the Figure 28.
-> 
-> > [!figure]
-> > ![](Pasted%20image%2020260422011750.png)
-> > 
-> > 
-> 
-
-
+> [!exercise]
+> 29. Use the Fourier series of Exercise 8 to find the Fourier series of the $2 p$-periodic function in the Figure 27.
+> 
+> 
+> ```scientific-figure
+> id: a3d784e3-8bfb-4733-a436-9a1b1780b42b
+> numbered: false
+> title: ""
+> caption: ""
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 07 Fourier Series/images/Pasted image 20260422011732.png
+>     caption: ""
+> ```
+> 
+> 
+> 30. Use the Fourier series of Exercise 10 to find the Fourier series of the $2 p$-periodic function in the Figure 28.
+> 
+> ```scientific-figure
+> id: 79850974-aa6b-4d40-aaa3-ddcaa4705fdb
+> numbered: false
+> title: ""
+> caption: ""
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 07 Fourier Series/images/Pasted image 20260422011750.png
+>     caption: ""
+> ```
+> 
 
 
 > [!exercise]
@@ -795,10 +821,6 @@
 > 
 
 
-
-
-
-
 > [!exercise]
 > 33. Project Problem: Term-by-term integration of Fourier series. Let $f$ be as in Theorem 1, and define an antiderivative of $f$ by
 > 
@@ -813,45 +835,11 @@
 > F(x)=A_0+\sum_{n=1}^{\infty}\left(\frac{p}{n \pi} a_n \sin \frac{n \pi}{p} x-\frac{p}{n \pi} b_n \cos \frac{n \pi}{p} x\right),
 > $$
 > 
-> where $A_0=\frac{2}{\pi} \sum_{n=1}^{\infty} \frac{b_n}{n}$. Hence, as long as $F$ is periodic, with no further assumptions on $f$ other than piecewise smoothness, we can get the Fourier series of $F$ by integrating term by term the Fourier series of $f$. **(Hint: Apply the result of Exercise 25 to $F(x)$ and use $F^{\prime}(x)=f(x)$. To compute $A_0$, use $F(0)=0$ (why?).)**
-> 
-> 
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
-
-
+> where $A_0=\frac{p}{\pi} \sum_{n=1}^{\infty} \frac{b_n}{n}$. Hence, as long as $F$ is periodic, with no further assumptions on $f$ other than piecewise smoothness, we can get the Fourier series of $F$ by integrating term by term the Fourier series of $f$. **(Hint: Apply the result of Exercise 25 to $F(x)$ and use $F^{\prime}(x)=f(x)$. To compute $A_0$, use $F(0)=0$ (why?).)**
+> 
+> 
+
+
+> [!exercise] Exercise 7.3.34
+> Use Exercise 33 to derive the Fourier series of Exercise 4 from that of Exercise 2.
+

`````

## 2026-11-09 — Native identity initialization recovery

Restored 3 printed exercise-number lines exactly from the pre-admission baseline after native initialization changed them. All native component identities were retained. No exercise wording, mathematics or admissible primitive was changed. Case 020; exact preimage and line receipt: `/Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-repair-20261108/admission/number-drift/7.3-f6ab6421063d.json`.
