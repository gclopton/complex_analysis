
# Editorial records

Reading note: 7.4 Half-Range Expansions- The Cosine and Sine Series.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Callout 265: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Half-Range Cosine and Sine Expansions
> Let $p>0$, and assume finite one-sided endpoint limits for $f$ and its piecewise continuous derivative.
>
> Suppose that $f(x)$ is a piecewise smooth function defined on an interval $0<x<p$. Then $f$ has a cosine series expansion
>
> $$
> a_0+\sum_{n=1}^{\infty} a_n \cos \frac{n \pi}{p} x \quad(0<x<p),
> $$
>
> where
>
> $$
> a_0=\frac{1}{p} \int_0^p f(x) d x ; \quad a_n=\frac{2}{p} \int_0^p f(x) \cos \frac{n \pi}{p} x d x \quad(n \geq 1) .
> $$
>
> Also, $f$ has a sine series expansion
>
> $$
> \sum_{n=1}^{\infty} b_n \sin \frac{n \pi}{p} x \quad(0<x<p),
> $$
>
> where
>
> $$
> b_n=\frac{2}{p} \int_0^p f(x) \sin \frac{n \pi}{p} x d x \quad(n \geq 1)
> $$
>
> On the interval $0<x<p$, both series converge to $f(x)$ if $f$ is continuous at $x$ and to $\frac{f(x+)+f(x-)}{2}$ otherwise.
````
### After

````text
> [!theorem] Half-Range Expansions
> Let $p>0$, and assume finite one-sided endpoint limits for $f$ and its piecewise continuous derivative.
>
> Suppose that $f(x)$ is a piecewise smooth function defined on an interval $0<x<p$. Then $f$ has a cosine series expansion
>
> $$
> a_0+\sum_{n=1}^{\infty} a_n \cos \frac{n \pi}{p} x \quad(0<x<p),
> $$
>
> where
>
> $$
> a_0=\frac{1}{p} \int_0^p f(x) d x ; \quad a_n=\frac{2}{p} \int_0^p f(x) \cos \frac{n \pi}{p} x d x \quad(n \geq 1) .
> $$
>
> Also, $f$ has a sine series expansion
>
> $$
> \sum_{n=1}^{\infty} b_n \sin \frac{n \pi}{p} x \quad(0<x<p),
> $$
>
> where
>
> $$
> b_n=\frac{2}{p} \int_0^p f(x) \sin \frac{n \pi}{p} x d x \quad(n \geq 1)
> $$
>
> On the interval $0<x<p$, both series converge to $f(x)$ if $f$ is continuous at $x$ and to $\frac{f(x+)+f(x-)}{2}$ otherwise.
````

## Source-to-current comparison

Source: /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 07 Fourier Series/7.4 Half-Range Expansions- The Cosine and Sine Series.md

This exact comparison preserves the full change evidence, including formatting, OCR corrections, restored source wording, and required standalone context. The entries above explain the recovery edits. The comparison is not a claim that every difference is a correction; component serialization, callout wrapping, and printed labels outside callouts are formatting.

`````diff
--- /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 07 Fourier Series/7.4 Half-Range Expansions- The Cosine and Sine Series.md
+++ /Users/gradyclopton/ObsidianVaults/complex_analysis/Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 07 Fourier Series/7.4 Half-Range Expansions- The Cosine and Sine Series.md
@@ -3,38 +3,35 @@
 In many applications we are interested in representing by a Fourier series a function $f(x)$ that is defined only in a finite interval, say $0<x<p$. Since $f$ is clearly not periodic, the results of the previous sections are not readily applicable. Our goal in this section is to show how we can represent $f$ by a Fourier series, after extending it to a periodic function.
 
 
-
+<!-- Source label: Half-Range Expansions -->
 > [!theorem] Half-Range Expansions
+> Let $p>0$, and assume finite one-sided endpoint limits for $f$ and its piecewise continuous derivative.
+>
 > Suppose that $f(x)$ is a piecewise smooth function defined on an interval $0<x<p$. Then $f$ has a cosine series expansion
-> (1)
-> 
+>
 > $$
 > a_0+\sum_{n=1}^{\infty} a_n \cos \frac{n \pi}{p} x \quad(0<x<p),
 > $$
-> 
+>
 > where
-> 
+>
 > $$
 > a_0=\frac{1}{p} \int_0^p f(x) d x ; \quad a_n=\frac{2}{p} \int_0^p f(x) \cos \frac{n \pi}{p} x d x \quad(n \geq 1) .
 > $$
-> 
-> 
+>
 > Also, $f$ has a sine series expansion
-> 
+>
 > $$
 > \sum_{n=1}^{\infty} b_n \sin \frac{n \pi}{p} x \quad(0<x<p),
 > $$
-> 
+>
 > where
-> 
+>
 > $$
 > b_n=\frac{2}{p} \int_0^p f(x) \sin \frac{n \pi}{p} x d x \quad(n \geq 1)
 > $$
-> 
-> 
-> On the interval $0<x<p$, the series (1) and (3) converge to $f(x)$ if $f$ is continuous at $x$ and to $\frac{f(x+)+f(x-)}{2}$ otherwise.
-
-
+>
+> On the interval $0<x<p$, both series converge to $f(x)$ if $f$ is continuous at $x$ and to $\frac{f(x+)+f(x-)}{2}$ otherwise.
 
 
 The series (1) and (3) are commonly referred to as the half-range expansions of $f$. They are two different series representations of the same function on the interval $0<x<p$. Theorem 1 will be derived by appealing to the Fourier series representation of even and odd functions (Theorem 2, Section 7.3). For this purpose, we introduce the following notions.
@@ -48,17 +45,23 @@
 By the way they are constructed, the function $f_1$ is even and $2 p$-periodic, and the function $f_2$ is odd and $2 p$-periodic. Both functions agree with $f$ on the interval $0<x<p$ which justifies calling them extensions of $f$ (Figure 1). 
 
 
-
-> [!figure]
-> ![](Pasted%20image%2020260422012635.png)
-> 
-> 
+```scientific-figure
+id: 5b4b00e3-45ae-4b10-89d8-9e6b11c6c4fb
+numbered: false
+title: ""
+caption: ""
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 07 Fourier Series/images/Pasted image 20260422012635.png
+    caption: ""
+```
 
 
 Since $f$ is piecewise smooth, it follows that $f_1$ and $f_2$ are both piecewise smooth. Applying Theorem 2 of Section 7.3, we find that $f_1$ has a cosine series expansion given by (1) with the coefficients (2). Now $f(x)=f_1(x)$ for all $0<x<p$, and so the cosine series (1) represents $f$ on this interval. Similar reasoning using $f_2$ yields the sine series expansion of $f$.
 
 
-
 > [!exercise] EXAMPLE 1 Half-range expansions
 > 
 > Find the half-range expansions of the function $f(x)=x$ for $0<x<1$.
@@ -66,15 +69,23 @@
 > 
 
 
-
-**Solution** The graphs of the even and odd extensions are shown in Figure 2.
-
-
-
-> [!figure] Figure 2
-> ![](Pasted%20image%2020260422012559.png)
-> 
-> 
+##### solution
+
+The graphs of the even and odd extensions are shown in Figure 2.
+
+
+```scientific-figure
+id: f695495f-3716-48e6-8fb8-62adc6a96038
+numbered: false
+title: ""
+caption: "**Figure 2.**"
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 07 Fourier Series/images/Pasted image 20260422012559.png
+    caption: ""
+```
 
 
 The even extension is a special case of Example 1 of Section 7.3 with $p=1$. We have
@@ -101,18 +112,11 @@
 It is a remarkable fact that the cosine series and the sine series have the same values on the intervals $(0,1),(2,3),(-2,-1), \ldots$.
 
 
-++++
-
-
-
-> [!exercise]
-> EXAMPLE 2 Half-range expansions
-> <span style="color:#ff0000; font-weight:bold">Need to formulate problem statement</span>
-> 
-> 
-
-
-
+---
+> [!exercise] EXAMPLE 2 Half-range expansions
+> Find the half-range cosine and sine expansions of $f(x)=\sin x$ on $0<x<\pi$, and identify its even and odd periodic extensions.
+
+##### solution
 
 Consider the function $f(x)=\sin x, 0 \leq x \leq \pi$. If we take its odd extension, we get the usual sine function, $f_2(x)=\sin x$ for all $x$. Thus, the sine series expansion is just $\sin x$.
 
@@ -123,17 +127,22 @@
 \sin x=\frac{2}{\pi}-\frac{4}{\pi} \sum_{k=1}^{\infty} \frac{1}{(2 k)^2-1} \cos 2 k x, \quad 0 \leq x \leq \pi
 $$
 
-> [!figure] Figure 3
-> ![](Pasted%20image%2020260422013103.png)
-> 
-
-
-++++
-
-
-
+```scientific-figure
+id: 84014d8a-5fd9-4442-8e4e-416088142700
+numbered: false
+title: ""
+caption: "**Figure 3.**"
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 07 Fourier Series/images/Pasted image 20260422013103.png
+    caption: ""
+```
+
+
+---
 # Exercises 7.4
-
 
 
 > [!exercise]
@@ -157,38 +166,44 @@
 > $$
 > 
 > where $0<a<b<p<\infty$. For (b), take $p=1, a=\frac{1}{4}, b=\frac{1}{2}$.
-> 4. $f(x)=\cos x$ if $0<x<\pi$.
-> 5. $f(x)=\cos x$ if $0 \leq x \leq \frac{\pi}{2}$.
-> 6. $f(x)=x \sin x$ if $0<x<\pi$.
-> 
-> 
-
+> 6. $f(x)=\cos x$ if $0<x<\pi$.
+> 7. $f(x)=\cos x$ if $0 \leq x \leq \frac{\pi}{2}$.
+> 8. $f(x)=x \sin x$ if $0<x<\pi$.
+> 
+> 
 
 
 > [!exercise]
 > In Exercises 9-16, find the sine series expansion of the given function on the interval $0<x<1$.
-> 7. $x(1-x)$.
-> 8. $1-x^2$.
-> 9. $\sin \pi x$.
-> 10. $\sin \frac{\pi}{2} x$.
-> 11. $\sin \pi x \cos \pi x$.
-> 12. $(1+\cos \pi x) \sin \pi x$.
-> 13. $e^x$.
-> 14. $1-e^x$.
-> 
-> 
-
+> 9. $x(1-x)$.
+> 10. $1-x^2$.
+> 11. $\sin \pi x$.
+> 12. $\sin \frac{\pi}{2} x$.
+> 13. $\sin \pi x \cos \pi x$.
+> 14. $(1+\cos \pi x) \sin \pi x$.
+> 15. $e^x$.
+> 16. $1-e^x$.
+> 
+> 
 
 
 > [!exercise]
-> 15. Triangular function. Let $f(x)$ denote the shape of a plucked string of length $p$ with endpoints fastened at $x=0$ and $x=p$, as shown in Figure 4.
-> 
-> 
-> 
-> > [!figure]
-> > 
-> > ![](Pasted%20image%2020260422013203.png)
-> > 
+> 17. Triangular function. Let $f(x)$ denote the shape of a plucked string of length $p$ with endpoints fastened at $x=0$ and $x=p$, as shown in Figure 4.
+> 
+> 
+> 
+> ```scientific-figure
+> id: 74d67092-3aa1-4144-b44e-ee18738d9400
+> numbered: false
+> title: ""
+> caption: ""
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 07 Fourier Series/images/Pasted image 20260422013203.png
+>     caption: ""
+> ```
 > 
 > 
 > (a) Using the data in the figure, derive the formula
@@ -208,47 +223,3 @@
 > 
 
 
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
-
-
-
-
-

`````
