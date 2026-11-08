
# Editorial records

Reading note: 7.5 Complex Form of Fourier Series.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Callout 266: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem|655a1864-1618-519a-aa4a-65896981c6cf.local at=e6249e7b-f9ca-5ac6-aef3-f9bbd75ecc6b] Complex Exponential Fourier Series for an Arbitrary Period
> Let $p>0$. The bilateral Fourier series is summed symmetrically as $\lim_{N\to\infty}\sum_{n=-N}^{N}$.
>
> Let $f$ be a $2 p$-periodic piecewise smooth function. The complex form of the Fourier series of $f$ is
>
> $$
> \sum_{n=-\infty}^{\infty} c_n e^{i \frac{n \pi}{p} x},
> $$
>
> where the Fourier coefficients $c_n$ are given by
>
> $$
> c_n=\frac{1}{2 p} \int_{-p}^p f(t) e^{-i \frac{n \pi}{p} t} d t \quad(n=0, \pm 1, \pm 2, \ldots) .
> $$
>
> For all $x$, the Fourier series converges to $f(x)$ if $f$ is continuous at $x$, and to $\frac{f(x+)+f(x-)}{2}$ otherwise. Moreover, the Fourier series converges to $f(x)$ uniformly for all $x$ if and only if $f$ is continuous for all $x$ (and piecewise smooth).
````
### After

````text
> [!theorem|655a1864-1618-519a-aa4a-65896981c6cf.local at=e6249e7b-f9ca-5ac6-aef3-f9bbd75ecc6b] Complex Form of Fourier Series
> Let $p>0$. The bilateral Fourier series is summed symmetrically as $\lim_{N\to\infty}\sum_{n=-N}^{N}$.
>
> Let $f$ be a $2 p$-periodic piecewise smooth function. The complex form of the Fourier series of $f$ is
>
> $$
> \sum_{n=-\infty}^{\infty} c_n e^{i \frac{n \pi}{p} x},
> $$
>
> where the Fourier coefficients $c_n$ are given by
>
> $$
> c_n=\frac{1}{2 p} \int_{-p}^p f(t) e^{-i \frac{n \pi}{p} t} d t \quad(n=0, \pm 1, \pm 2, \ldots) .
> $$
>
> For all $x$, the Fourier series converges to $f(x)$ if $f$ is continuous at $x$, and to $\frac{f(x+)+f(x-)}{2}$ otherwise. Moreover, the Fourier series converges to $f(x)$ uniformly for all $x$ if and only if $f$ is continuous for all $x$ (and piecewise smooth).
````

## 2. Callout 268: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem|2aabf1a7-be36-53ee-8acb-62dca5a31fea.local at=8eacc40f-716c-56b7-af51-833a069efc00] Fourier Coefficients of Normalized Periodic Convolution
> For a periodic function $h$, write $\widehat h(n)=(2p)^{-1}\int_{-p}^{p}h(t)e^{-in\pi t/p}\,dt$.
>
> Let $p>0$. The normalized periodic convolution is $(f*g)(x)=(2p)^{-1}\int_{-p}^{p}f(t)g(x-t)\,dt$.
>
> Let $f$ and $g$ be $2 p$-periodic, piecewise smooth functions. Then
>
> $$
> \widehat{f * g}(n)=\widehat{f}(n) \widehat{g}(n) \quad n=0, \pm 1, \pm 2, \ldots .
> $$
````
### After

````text
> [!theorem|2aabf1a7-be36-53ee-8acb-62dca5a31fea.local at=8eacc40f-716c-56b7-af51-833a069efc00] Fourier Coefficients of Convolutions
> For a periodic function $h$, write $\widehat h(n)=(2p)^{-1}\int_{-p}^{p}h(t)e^{-in\pi t/p}\,dt$.
>
> Let $p>0$. The normalized periodic convolution is $(f*g)(x)=(2p)^{-1}\int_{-p}^{p}f(t)g(x-t)\,dt$.
>
> Let $f$ and $g$ be $2 p$-periodic, piecewise smooth functions. Then
>
> $$
> \widehat{f * g}(n)=\widehat{f}(n) \widehat{g}(n) \quad n=0, \pm 1, \pm 2, \ldots .
> $$
````

## 3. Callout 269: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!corollary|ece2da0d-3242-50eb-a13d-c1e81021250f.local at=443c5414-02af-5205-aa76-974b9cef5f3a] Continuity and Piecewise Smoothness of Periodic Convolution
> Let $p>0$. The normalized periodic convolution is $(f*g)(x)=(2p)^{-1}\int_{-p}^{p}f(t)g(x-t)\,dt$.
>
> Let $f$ and $g$ be $2 p$-periodic, piecewise smooth functions. Then $f * g$ is continuous and piecewise smooth.
````
### After

````text
> [!corollary|ece2da0d-3242-50eb-a13d-c1e81021250f.local at=443c5414-02af-5205-aa76-974b9cef5f3a] Continuity of Convolutions
> Let $p>0$. The normalized periodic convolution is $(f*g)(x)=(2p)^{-1}\int_{-p}^{p}f(t)g(x-t)\,dt$.
>
> Let $f$ and $g$ be $2 p$-periodic, piecewise smooth functions. Then $f * g$ is continuous and piecewise smooth.
````

## 4. Callout 271: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!corollary|f6679090-fcb0-5028-8824-c4579a5fba52.local at=62251ac9-da98-50d9-a85d-6d67e14caea1] Parseval's Identity for Real Periodic Functions
> Let $p>0$ and let $f$ be an integrable $2p$-periodic function. Use coefficients
>
> $$
> a_0=\frac1{2p}\int_{-p}^{p}f(t)\,dt,\qquad a_n=\frac1p\int_{-p}^{p}f(t)\cos\frac{n\pi t}{p}\,dt,\qquad b_n=\frac1p\int_{-p}^{p}f(t)\sin\frac{n\pi t}{p}\,dt\quad(n\geq1),
> $$
>
> and $c_n=(2p)^{-1}\int_{-p}^{p}f(t)e^{-in\pi t/p}\,dt$ for integer $n$.
>
> Let $f$ be a real-valued $2 p$-periodic piecewise smooth function on $[-p, p]$. Let $a_n, b_n$, and $c_n$ denote, respectively, the cosine, the sine, and the complex Fourier coefficients of $f$. Then
>
> $$
> \frac{1}{2 p} \int_{-p}^p f(x)^2 d x=\sum_{n=-\infty}^{\infty}\left|c_n\right|^2=a_0^2+\frac12\sum_{n=1}^{\infty}\left(a_n^2+b_n^2\right)
> $$
````
### After

````text
> [!corollary|f6679090-fcb0-5028-8824-c4579a5fba52.local at=62251ac9-da98-50d9-a85d-6d67e14caea1] Parseval's Identity
> Let $p>0$ and let $f$ be an integrable $2p$-periodic function. Use coefficients
>
> $$
> a_0=\frac1{2p}\int_{-p}^{p}f(t)\,dt,\qquad a_n=\frac1p\int_{-p}^{p}f(t)\cos\frac{n\pi t}{p}\,dt,\qquad b_n=\frac1p\int_{-p}^{p}f(t)\sin\frac{n\pi t}{p}\,dt\quad(n\geq1),
> $$
>
> and $c_n=(2p)^{-1}\int_{-p}^{p}f(t)e^{-in\pi t/p}\,dt$ for integer $n$.
>
> Let $f$ be a real-valued $2 p$-periodic piecewise smooth function on $[-p, p]$. Let $a_n, b_n$, and $c_n$ denote, respectively, the cosine, the sine, and the complex Fourier coefficients of $f$. Then
>
> $$
> \frac{1}{2 p} \int_{-p}^p f(x)^2 d x=\sum_{n=-\infty}^{\infty}\left|c_n\right|^2=a_0^2+\frac12\sum_{n=1}^{\infty}\left(a_n^2+b_n^2\right)
> $$
````

## 5. Move editorial commentary out of the reading note.

### Before

````text
*Editorial clarifications: Exercise 10(b) allows isolated changes of values unless continuity is assumed. The final theorem’s proof is explicitly reduced to period $2\pi$ and uses Bessel’s inequality for $f^{\prime}$, whose derivative need not exist. Other source corrections include the missing Parseval factor and the removable value at the origin in Exercise 26.*
````
### After

````text

````

## 6. Move editorial commentary out of the reading note.

### Before

````text
*Editorial note: [source typo corrected] Inserted the missing factor 1/2 on the sum of squared real Fourier coefficients, required by the displayed coefficient normalization.*
````
### After

````text

````

## 7. Move editorial commentary out of the reading note.

### Before

````text
*Editorial correction: the bound includes all jumps; the printed constant $4M$ need not cover an arbitrary number of discontinuities.*
````
### After

````text

````

## 8. Move editorial commentary out of the reading note.

### Before

````text
*Editorial correction: the source’s extension of the differentiation formula to discontinuous factors omits these jump terms.*
````
### After

````text

````

## Additional source comparison

## 1. Restore source proof wording and method while retaining the correction for jump terms and coefficient bounds.

### Before

````text
If $f$ and $g$ are merely piecewise smooth, split the integral at their breakpoints and include the moving-boundary terms when differentiating. Write $g'_\mathrm{reg}$ for the ordinary derivative on the smooth pieces and $\Delta g(t_j)=g(t_j+)-g(t_j-)$ for the jumps in one period (including the periodic endpoint if necessary). Away from the finitely many translated breakpoints,

$$
(f*g)'(x)=(f*g'_\mathrm{reg})(x)+\frac1{2p}\sum_j\Delta g(t_j)f(x-t_j).
$$

The integral term is continuous and the finite sum is piecewise continuous, so the convolution is piecewise smooth. The formula without jump terms applies when the differentiated factor is continuous.
````
### After

````text
If $f$ and $g$ are merely piecewise smooth, we can write the convolution integral as a sum of integrals over intervals on which $f$ and $g$ are continuous with continuous derivatives, and then differentiate under the integral sign, including the endpoint terms from the moving breakpoints. So, in general, the convolution is piecewise smooth.
````

## 2. Restore source proof wording and method while retaining the correction for jump terms and coefficient bounds.

### Before

````text
**Proof** Piecewise smoothness follows from the corrected differentiation formula above. Continuity also follows directly: if $x_k\to x$, then $g(x_k-t)\to g(x-t)$ except at finitely many $t$ modulo the period, while $|f(t)g(x_k-t)|\leq\|g\|_\infty|f(t)|$. Dominated convergence therefore gives $(f*g)(x_k)\to(f*g)(x)$.

For the source’s Fourier-series argument, integration by parts on each smooth piece, retaining its endpoint and jump terms, gives $|\widehat f(n)|\leq C_f/|n|$ and $|\widehat g(n)|\leq C_g/|n|$ for $n\ne0$, where the constants depend on the functions and the period. Consequently $|\widehat{f*g}(n)|\leq C_fC_g/n^2$. The Weierstrass $M$-test gives uniform convergence of $\sum_{n=-\infty}^{\infty}\widehat f(n)\widehat g(n)e^{in\pi x/p}$.


---
````
### After

````text
**Proof** We have already showed that $f * g$ is piecewise smooth with the endpoint terms from moving breakpoints included when differentiating at all but finitely many points in $[-p, p]$. To show that it is continuous, we note that if $|f|$ and $\left|f^{\prime}\right|$ are bounded, say by $M$, then $|\widehat{f}(n)|\leq C/|n|$ for $n\ne0$, where $C$ includes the finitely many jumps, which follows by integrating by parts on each smooth interval in (4). The details are left as an exercise. So $|\widehat{f * g}(n)|=|\widehat{f}(n)||\widehat{g}(n)| \leq A \frac{1}{n} \frac{1}{n}=\frac{A}{n^{2}}$, where $A$ is a constant. We now apply the Weierstrass $M$-test to the Fourier series of $f * g(x)$, which is $\sum_{-\infty}^{\infty} \widehat{f}(n) \widehat{g}(n) e^{i \frac{n \pi}{p}x}$, and conclude that the series converges uniformly for all $x$, implying that $f * g(x)$ is continuous, by Theorem 1.
````

## Source-to-current comparison

Source: /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 07 Fourier Series/7.5 Complex Form of Fourier Series.md

This exact comparison preserves the full change evidence, including formatting, OCR corrections, restored source wording, and required standalone context. The entries above explain the recovery edits. The comparison is not a claim that every difference is a correction; component serialization, callout wrapping, and printed labels outside callouts are formatting.

`````diff
--- /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 07 Fourier Series/7.5 Complex Form of Fourier Series.md
+++ /Users/gradyclopton/ObsidianVaults/complex_analysis/Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 07 Fourier Series/7.5 Complex Form of Fourier Series.md
@@ -12,29 +12,26 @@
 f(x)=a_0+\sum_{n=1}^{\infty}\left(a_n \cos \frac{n \pi}{p} x+b_n \sin \frac{n \pi}{p} x\right),
 $$
 
-and then, using (2), we will replace the cosine and sine by their expressions in terms of the complex exponential and derive the complex form of the Fourier series, which is expressed as follows.
-
-
-
-
-> [!theorem] Complex Form of Fourier Series
+and then, using (1), we will replace the cosine and sine by their expressions in terms of the complex exponential and derive the complex form of the Fourier series, which is expressed as follows.
+
+
+<!-- Source label: Complex Form of Fourier Series -->
+> [!theorem|655a1864-1618-519a-aa4a-65896981c6cf.local at=e6249e7b-f9ca-5ac6-aef3-f9bbd75ecc6b] Complex Form of Fourier Series
+> Let $p>0$. The bilateral Fourier series is summed symmetrically as $\lim_{N\to\infty}\sum_{n=-N}^{N}$.
+>
 > Let $f$ be a $2 p$-periodic piecewise smooth function. The complex form of the Fourier series of $f$ is
-> (3)
-> 
+>
 > $$
 > \sum_{n=-\infty}^{\infty} c_n e^{i \frac{n \pi}{p} x},
 > $$
-> 
+>
 > where the Fourier coefficients $c_n$ are given by
-> (4)
-> 
+>
 > $$
 > c_n=\frac{1}{2 p} \int_{-p}^p f(t) e^{-i \frac{n \pi}{p} t} d t \quad(n=0, \pm 1, \pm 2, \ldots) .
 > $$
-> 
-> 
+>
 > For all $x$, the Fourier series converges to $f(x)$ if $f$ is continuous at $x$, and to $\frac{f(x+)+f(x-)}{2}$ otherwise. Moreover, the Fourier series converges to $f(x)$ uniformly for all $x$ if and only if $f$ is continuous for all $x$ (and piecewise smooth).
-> 
 
 
 The Fourier coefficients $c_n$ are also denoted by $\hat{f}(n)$. The $N$ th partial sum of (3) is by definition the symmetric sum
@@ -49,8 +46,6 @@
 $$
 s_N(x)=a_0+\sum_{n=1}^N\left(a_n \cos \frac{n \pi}{p} x+b_n \sin \frac{n \pi}{p} x\right) .
 $$
-
-
 
 
 **Proof of Theorem 1** It is enough to show that $S_N=s_N$, then the theorem will follow from Theorem 1, Section 7.3. We clearly have $c_0=a_0$. For $n>0$, using (1), we get
@@ -78,27 +73,34 @@
 To simplify the middle integral, we used the identity $e^{-i \theta}=\cos \theta-i \sin \theta$. A similar argument shows that $c_{-n}=\frac{1}{2}\left(a_n+i b_n\right)$. Thus, for $n \geq 1$,
 
 $$
-a_n \cos \frac{n \pi}{p} x+b_n \sin \frac{n \pi}{p} x=c_n e^{i \frac{n \pi}{p} \pi}+c_{-n} e^{-i \frac{n \pi}{p} x},
+a_n \cos \frac{n \pi}{p} x+b_n \sin \frac{n \pi}{p} x=c_n e^{i \frac{n \pi}{p} x}+c_{-n} e^{-i \frac{n \pi}{p} x},
 $$
 
 and so
 
 $$
-s_N(x)=a_0+\sum_{n=1}^N\left(a_n \cos \frac{n \pi}{p} x+b_n \sin \frac{n \pi}{p} x\right)=c_0+\sum_{n=1}^N c_n e^{i \frac{n \pi}{p} x}+\sum_{n=1}^N c_{-n} e^{-1 \frac{n \pi}{p} x} .
+s_N(x)=a_0+\sum_{n=1}^N\left(a_n \cos \frac{n \pi}{p} x+b_n \sin \frac{n \pi}{p} x\right)=c_0+\sum_{n=1}^N c_n e^{i \frac{n \pi}{p} x}+\sum_{n=1}^N c_{-n} e^{-i \frac{n \pi}{p} x} .
 $$
 
 
 Changing $n$ to $-n$ in the second series on the right and combining, we get that $s_N(x)=S_N(x)$, and the theorem follows.
 
-+++
-
-
-
+---
 We can extract the following useful identities from the previous proof.
 
 
-> [!equation]
-> 
+<!-- Source label:  -->
+> [!equation|18550eef-fb3d-5c77-9ab9-58ec1cc43083.local at=3bd3c22f-0697-51bd-85b2-ebb7725023ea] Conversion Between Real and Complex Fourier Coefficients
+> Let $p>0$ and let $f$ be an integrable $2p$-periodic function. Use coefficients
+>
+> $$
+> a_0=\frac1{2p}\int_{-p}^{p}f(t)\,dt,\qquad a_n=\frac1p\int_{-p}^{p}f(t)\cos\frac{n\pi t}{p}\,dt,\qquad b_n=\frac1p\int_{-p}^{p}f(t)\sin\frac{n\pi t}{p}\,dt\quad(n\geq1),
+> $$
+>
+> and $c_n=(2p)^{-1}\int_{-p}^{p}f(t)e^{-in\pi t/p}\,dt$ for integer $n$.
+>
+> Write $S_N(x)=\sum_{n=-N}^{N}c_ne^{in\pi x/p}$ and $s_N(x)=a_0+\sum_{n=1}^{N}(a_n\cos(n\pi x/p)+b_n\sin(n\pi x/p))$. Then
+>
 > $$
 > \begin{gathered}
 > c_0=a_0 \\
@@ -107,8 +109,6 @@
 > S_N(x)=s_N(x)
 > \end{gathered}
 > $$
-> 
-> 
 
 
 If $f$ is real-valued, so that $a_n$ and $b_n$ are both real, then (6) shows that $c_{-n}$ is the complex conjugate of $c_n$. In symbols,
@@ -123,20 +123,21 @@
 The complex form of the Fourier series is particularly useful when dealing with exponential functions, as we now illustrate.
 
 
-
-> [!exercise] EXAMPLE 1 A complex Fourier series
+> [!exercise|3c8b4465-d396-5d69-a5d5-a5adfae6e12a.local at=3263409f-3bd5-536b-9592-6199f4e39438] EXAMPLE 1 A complex Fourier series
 > 
 > Find the complex form of the Fourier series of the $2 \pi$-periodic function $f(x)=e^{a x}$ for $-\pi<x<\pi$, where $a \neq 0, \pm i, \pm 2 i, \pm 3 i, \ldots$. Determine the values of the Fourier series at $x= \pm \pi$.
 > 
 > 
 
-**Solution** From (4), we have
+##### solution
+
+From (4), we have
 
 $$
 c_n=\frac{1}{2 \pi} \int_{-\pi}^\pi e^{a x} e^{-i n x} d x=\frac{1}{2 \pi}\left[\frac{e^{(a-i n) x}}{a-i n}\right]_{-\pi}^\pi=\frac{(-1)^n}{a-i n} \frac{\sinh \pi a}{\pi},
 $$
 
-where we have used $e^{ \pm i n \pi}=(-1)^n$ and $\sinh \pi a=\frac{e^{* *}-e^{-* a}}{2}$. Plugging these coefficients into (3) and simplifying, we obtain the complex form of the Fourier series of $f$
+where we have used $e^{ \pm i n \pi}=(-1)^n$ and $\sinh \pi a=\frac{e^{\pi a}-e^{-\pi a}}{2}$. Plugging these coefficients into (3) and simplifying, we obtain the complex form of the Fourier series of $f$
 
 $$
 \frac{\sinh \pi a}{\pi} \sum_{n=-\infty}^{\infty} \frac{(-1)^n}{a-i n} e^{i n x}=\frac{\sinh \pi a}{\pi} \sum_{n=-\infty}^{\infty} \frac{(-1)^n}{a^2+n^2}(a+i n) e^{i n x}
@@ -159,14 +160,18 @@
 $$
 
 
-
-> [!figure] Figure 1
-> 
-> ![](Pasted%20image%2020260422014144.png)
-> Figure $1 \mathrm{~A} 2 \pi$-periodic function, $e^{a x}, a>0,-\pi<x< \pi$ 
-
-
-
+```scientific-figure
+id: 71afdacb-f02a-4102-a642-a59593a81a96
+numbered: false
+title: ""
+caption: "**Figure 1.** Figure $1 \\mathrm{~A} 2 \\pi$-periodic function, $e^{a x}, a>0,-\\pi<x< \\pi$"
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 07 Fourier Series/images/Pasted image 20260422014144.png
+    caption: ""
+```
 
 
 As a specific illustration, if you take $x=\pi$ in the Fourier series, you obtain the interesting identity
@@ -179,16 +184,15 @@
 We have used $e^{i n \pi}=(-1)^n$ and $(-1)^n(-1)^n=1$ to simplify the series. (See Exercises 12 and 13 for related results.) Finally, let us note that if $a= \pm i n$, then $f(x)=e^{ \pm \mathrm{in} x}$, and hence $f$ is its own Fourier series.
 
 
-++++
-
-
-
-> [!exercise] EXAMPLE 2 The (usual) Fourier series from the complex form
+---
+> [!exercise|4bea19f9-e15d-562c-a422-583c42155bef.local at=35f90a93-4fc0-5a3e-9412-1915b847cae8] EXAMPLE 2 The (usual) Fourier series from the complex form
 > 
 > Obtain the usual Fourier series of the function in Example 1 from its complex form. Take $a$ to be a real number $\neq 0$.
 
 
-**Solution** The point here is not to use the Euler formulas of Section 7.2 to compute the Fourier series. Instead, we will use Example 1 and appropriate formulas relating the Fourier coefficients $a_n$ and $b_n$ to the complex Fourier coefficients $c_n$. From (5) and (10), we obtain
+##### solution
+
+The point here is not to use the Euler formulas of Section 7.2 to compute the Fourier series. Instead, we will use Example 1 and appropriate formulas relating the Fourier coefficients $a_n$ and $b_n$ to the complex Fourier coefficients $c_n$. From (5) and (10), we obtain
 
 $$
 a_0=c_0=\frac{1}{a} \frac{\sinh \pi a}{\pi} .
@@ -221,42 +225,42 @@
 e^{a x}=\frac{1}{a} \frac{\sinh \pi a}{\pi}+\frac{\sinh \pi a}{\pi} \sum_{n=1}^{\infty} \frac{(-1)^n}{a^2+n^2}(2 a \cos n x-2 n \sin n x) .
 $$
 
-f We took $a=1$ and illustrated the convergence of the Fourier series in Figure 2.
-
-
-
-
-> [!figure]
-> 
-> ![](Pasted%20image%2020260422014416.png)
-> Figure 2 Partial sums of the Fourier series of the $2 \pi$ periodic function $f(x)=e^x$, $-\pi<x<\pi$.
-
+We took $a=1$ and illustrated the convergence of the Fourier series in Figure 2.
+
+
+```scientific-figure
+id: 286f06f9-9988-4f10-adcc-e429ac600c40
+numbered: false
+title: ""
+caption: "**Figure 2.** Partial sums of the Fourier series of the $2 \\pi$ periodic function $f(x)=e^x$, $-\\pi<x<\\pi$."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 07 Fourier Series/images/Pasted image 20260422014416.png
+    caption: ""
+```
 
 
 - Note that because the sine coefficients are of the order $1 / n$, the series converges relatively slowly like the Fourier series of the sawtooth function.
 
 
-++++
-
-
-
+---
 Our next example illustrates the use of methods from complex analysis in computing Fourier series. The ideas are similar to those we used in
 
 
 Section 7.2 and are based on the applications of Laurent series. The example that we present leads to power series, which are special cases of Laurent series.
 
 
-
-> [!exercise] EXAMPLE 3 Using complex power series to compute Fourier series
-> 
-> <span style="color:#ff0000; font-weight:bold">Need exercise statement</span>
-> 
-
+> [!exercise|eda21c16-ce47-5cbb-bd99-806d05d42636.local at=a86f2953-ddd5-519f-a31a-a29fbe498bad] EXAMPLE 3 Using complex power series to compute Fourier series
+> For real $a$ with $|a|>1$, use a complex power series to find the Fourier series of $f(\theta)=1/(a+e^{i\theta})$. Deduce Fourier series for its real and imaginary parts.
+
+##### solution
 
 Let $a$ be a real number with $|a|>1$. The complex-valued function
 
 $$
-f(\theta)=\frac{1}{a+e^{1 \theta}} \quad(\theta \text { real })
+f(\theta)=\frac{1}{a+e^{i \theta}} \quad(\theta \text { real })
 $$
 
 is $2 \pi$-periodic, and because $|a|>1$ and $\left|e^{i \theta}\right|=1$ for all $\theta$, the denominator does not vanish, and so $f$ is smooth. The function $f(\theta)$ is the restriction to the unit circle $\left(z=e^{i \theta}\right)$ of the function $\frac{1}{a+z}$, where $z$ is the variable. Since $|a|>1$, it follows that $\frac{1}{a+z}$ is analytic in the disk $|z|<|a|$, and so it has a power series expansion in $|z|<|a|$, which can be obtained from the geometric series as follows:
@@ -269,12 +273,18 @@
 Since the unit circle $|z|=1$ is contained in the disk $|z|<|a|$, the power series expansion is valid for all $z=e^{i \theta}$ (Figure 3). 
 
 
-> [!figure] Figure 3
-> 
-> ![](Pasted%20image%2020260422014627.png)
-> Figure 3 The disk $|z|<|a| (|a|>1)$ contains the circle $|z|=1$.
-
-
+```scientific-figure
+id: d64499e8-a54c-4dde-8e7e-e9cf887b8f22
+numbered: false
+title: ""
+caption: "**Figure 3.** The disk $|z|<|a| (|a|>1)$ contains the circle $|z|=1$."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 07 Fourier Series/images/Pasted image 20260422014627.png
+    caption: ""
+```
 
 
 Substituting $z=e^{i \theta}$, then using $z^n=e^{i n \theta}$ and simplifying, we get
@@ -305,50 +315,55 @@
 which are valid for all $\theta$. In Figures 4 and 5, we plotted the real and imaginary parts of $f$ in the case $a=2$, along with partial sums of their Fourier series.
 
 
-
-
-> [!figure] Figure 4
-> 
-> ![](Pasted%20image%2020260422014802.png)
-> Figure 4 In this figure:
-> 
-> $$
-> \begin{aligned}
-> & \operatorname{Re}\left(\frac{1}{2+e^\pi}\right)=\frac{2+\cos \theta}{5+4 \cos \theta} ; \\
-> & s_2(\theta)=\frac{1}{2}\left(1-\frac{\cos \theta}{2}+\frac{\cos 2 \theta}{4}\right) .
-> \end{aligned}
-> $$
-
-
-
-
-
-> [!figure] Figure 5
-> 
-> ![](Pasted%20image%2020260422014828.png)
-> Figure 5 In this figure:
-> 
-> $$
-> \begin{aligned}
-> & \ln \left(\frac{1}{2+e^{21}}\right)=\frac{-\sin \theta}{5+4 \cos \theta} ; \\
-> & \sin (\theta)=-\frac{1}{2}\left(\frac{\sin \theta}{2}-\frac{\sin 2 \theta}{4}\right) .
-> \end{aligned}
-> $$
-
-
-
-
-
-
-++++
-
-
+```scientific-figure
+id: 5524dc9c-a988-44ba-a400-84f23874db40
+numbered: false
+title: ""
+caption: |-
+  **Figure 4.** In this figure:
+
+  $$
+  \begin{aligned}
+  & \operatorname{Re}\left(\frac{1}{2+e^\pi}\right)=\frac{2+\cos \theta}{5+4 \cos \theta} ; \\
+  & s_2(\theta)=\frac{1}{2}\left(1-\frac{\cos \theta}{2}+\frac{\cos 2 \theta}{4}\right) .
+  \end{aligned}
+  $$
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 07 Fourier Series/images/Pasted image 20260422014802.png
+    caption: ""
+```
+
+
+```scientific-figure
+id: 7248b73a-c832-437d-97c5-2e99cc0a2773
+numbered: false
+title: ""
+caption: |-
+  **Figure 5.** In this figure:
+
+  $$
+  \begin{aligned}
+  & \ln \left(\frac{1}{2+e^{21}}\right)=\frac{-\sin \theta}{5+4 \cos \theta} ; \\
+  & \sin (\theta)=-\frac{1}{2}\left(\frac{\sin \theta}{2}-\frac{\sin 2 \theta}{4}\right) .
+  \end{aligned}
+  $$
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 07 Fourier Series/images/Pasted image 20260422014828.png
+    caption: ""
+```
+
+
+---
 The Fourier series (11) is very special, in the sense that all the $c_n$ 's with $n<0$ are zero. Such a Fourier series is called analytic, because, as we saw
 
 
-
-in Example 3, it is the restriction of an analytic function to the circle. Note that the functions $f(\theta)$ in Example 3 is complex-valued. Is it possible to have a real-valued analytic Fourier series? It is not hard to show that the only real-valued analytic functions are the constant functions (Exercise 10(b)).
-
+in Example 3, it is the restriction of an analytic function to the circle. Note that the functions $f(\theta)$ in Example 3 is complex-valued. Is it possible to have a real-valued analytic Fourier series? It is not hard to show that the only real-valued continuous functions with analytic Fourier series are constant (Exercise 10(b)).
 
 
 # Convolution of Periodic Functions
@@ -382,21 +397,22 @@
 $$
 
 
-If $f$ and $g$ are merely piecewise smooth, we can write the convolution integral as a sum of integrals over intervals on which $f$ and $g$ are continuous with continuous derivatives, and then differentiate under the integral sign. So, in general, the convolution is piecewise smooth.
+If $f$ and $g$ are merely piecewise smooth, we can write the convolution integral as a sum of integrals over intervals on which $f$ and $g$ are continuous with continuous derivatives, and then differentiate under the integral sign, including the endpoint terms from the moving breakpoints. So, in general, the convolution is piecewise smooth.
 
 Convolutions are important because they correspond to multiplication of the Fourier coefficients. To express this property, it will be convenient to use the notation $\widehat{f}(n)$ for the complex Fourier coefficients instead of $c_n$.
 
 
-
-
-> [!theorem] Fourier Coefficients of Convolutions
+<!-- Source label: Fourier Coefficients of Convolutions -->
+> [!theorem|2aabf1a7-be36-53ee-8acb-62dca5a31fea.local at=8eacc40f-716c-56b7-af51-833a069efc00] Fourier Coefficients of Convolutions
+> For a periodic function $h$, write $\widehat h(n)=(2p)^{-1}\int_{-p}^{p}h(t)e^{-in\pi t/p}\,dt$.
+>
+> Let $p>0$. The normalized periodic convolution is $(f*g)(x)=(2p)^{-1}\int_{-p}^{p}f(t)g(x-t)\,dt$.
+>
 > Let $f$ and $g$ be $2 p$-periodic, piecewise smooth functions. Then
-> 
+>
 > $$
 > \widehat{f * g}(n)=\widehat{f}(n) \widehat{g}(n) \quad n=0, \pm 1, \pm 2, \ldots .
 > $$
-> 
-> 
 
 Proof We have
 
@@ -413,36 +429,32 @@
 
 $$
 \begin{aligned}
-\widehat{f * g}(n) & =\frac{1}{2 p} \int_{-p}^p \frac{1}{2 p} \int_{-p}^p g(y) e^{-i \frac{2 \pi}{p} y} e^{-i \frac{n \pi}{p} t} d y f(t) d t \\
+\widehat{f * g}(n) & =\frac{1}{2 p} \int_{-p}^p \frac{1}{2 p} \int_{-p}^p g(y) e^{-i \frac{n \pi}{p} y} e^{-i \frac{n \pi}{p} t} d y f(t) d t \\
 & =\frac{1}{2 p} \int_{-p}^p g(y) e^{-i \frac{n \pi}{p} y} d y \frac{1}{2 p} \int_{-p}^p f(t) e^{-i \frac{n \pi}{p} t} d t \\
 & =\widehat{g}(n) \widehat{f}(n)=\widehat{f}(n) \widehat{g}(n) .
 \end{aligned}
 $$
 
-+++
-
-
-
+---
 We will derive several interesting consequences of Theorem 2.
 
 
-
-> [!corollary] Continuity of Convolutions
+<!-- Source label: Continuity of Convolutions -->
+> [!corollary|ece2da0d-3242-50eb-a13d-c1e81021250f.local at=443c5414-02af-5205-aa76-974b9cef5f3a] Continuity of Convolutions
+> Let $p>0$. The normalized periodic convolution is $(f*g)(x)=(2p)^{-1}\int_{-p}^{p}f(t)g(x-t)\,dt$.
+>
 > Let $f$ and $g$ be $2 p$-periodic, piecewise smooth functions. Then $f * g$ is continuous and piecewise smooth.
 
 
-
-**Proof** We have already showed that $f * g$ is piecewise smooth with derivative given by (14) at all but finitely many points in $[-p, p]$. To show that it is continuous, we note that if $|f|$ and $\left|f^{\prime}\right|$ are bounded, say by $M$, then $|\hat{f}(n)| \leq \frac{4 M}{n}$, which follows by integrating by parts in (4). The details are left as an exercise. So $|\widehat{f * g}(n)|=|\hat{f}(n)||\hat{g}(n)| \leq A \frac{1}{n} \frac{1}{n}=\frac{A}{n^2}$, where $A$ is a constant. We now apply the Weierstrass $M$-test to the Fourier series of $f * g(x)$, which is $\sum_{-\infty}^{\infty} \hat{f}(n) \hat{g}(n) e^{i \frac{n x}{p}}$, and conclude that the series converges uniformly for all $x$, implying that $f * g(x)$ is continuous, by Theorem 1.
-
-
-+++
-
+**Proof** We have already showed that $f * g$ is piecewise smooth with the endpoint terms from moving breakpoints included when differentiating at all but finitely many points in $[-p, p]$. To show that it is continuous, we note that if $|f|$ and $\left|f^{\prime}\right|$ are bounded, say by $M$, then $|\widehat{f}(n)|\leq C/|n|$ for $n\ne0$, where $C$ includes the finitely many jumps, which follows by integrating by parts on each smooth interval in (4). The details are left as an exercise. So $|\widehat{f * g}(n)|=|\widehat{f}(n)||\widehat{g}(n)| \leq A \frac{1}{n} \frac{1}{n}=\frac{A}{n^{2}}$, where $A$ is a constant. We now apply the Weierstrass $M$-test to the Fourier series of $f * g(x)$, which is $\sum_{-\infty}^{\infty} \widehat{f}(n) \widehat{g}(n) e^{i \frac{n \pi}{p}x}$, and conclude that the series converges uniformly for all $x$, implying that $f * g(x)$ is continuous, by Theorem 1.
 
 The next result states that convolution is commutative. It can be checked directly by using the definition of convolution. We give a different proof based on Theorem 2.
 
 
-
-> [!corollary]
+<!-- Source label:  -->
+> [!corollary|5cf7df4e-c4bf-5da3-8d8d-8a98db6dbd44.local at=f1848af6-3522-5210-9209-370bee065b3a] Commutativity of Normalized Periodic Convolution
+> Let $p>0$. The normalized periodic convolution is $(f*g)(x)=(2p)^{-1}\int_{-p}^{p}f(t)g(x-t)\,dt$.
+>
 > Let $f$ and $g$ be piecewise smooth $2 p$-periodic functions. Then $f * g(x)= g * f(x)$.
 
 
@@ -458,19 +470,22 @@
 
 Since the Fourier series are the same and converge (uniformly) everywhere to the functions, we conclude that $f * g=g * f$.
 
-+++
-
-
-
-> [!corollary] Parseval's Identity
+---
+<!-- Source label: Parseval's Identity -->
+> [!corollary|f6679090-fcb0-5028-8824-c4579a5fba52.local at=62251ac9-da98-50d9-a85d-6d67e14caea1] Parseval's Identity
+> Let $p>0$ and let $f$ be an integrable $2p$-periodic function. Use coefficients
+>
+> $$
+> a_0=\frac1{2p}\int_{-p}^{p}f(t)\,dt,\qquad a_n=\frac1p\int_{-p}^{p}f(t)\cos\frac{n\pi t}{p}\,dt,\qquad b_n=\frac1p\int_{-p}^{p}f(t)\sin\frac{n\pi t}{p}\,dt\quad(n\geq1),
+> $$
+>
+> and $c_n=(2p)^{-1}\int_{-p}^{p}f(t)e^{-in\pi t/p}\,dt$ for integer $n$.
+>
 > Let $f$ be a real-valued $2 p$-periodic piecewise smooth function on $[-p, p]$. Let $a_n, b_n$, and $c_n$ denote, respectively, the cosine, the sine, and the complex Fourier coefficients of $f$. Then
-> 
-> $$
-> \frac{1}{2 p} \int_{-p}^p f(x)^2 d x=\sum_{n=-\infty}^{\infty}\left|c_n\right|^2=a_0^2+\sum_{n=1}^{\infty}\left(a_n^2+b_n^2\right)
-> $$
-> 
-
-
+>
+> $$
+> \frac{1}{2 p} \int_{-p}^p f(x)^2 d x=\sum_{n=-\infty}^{\infty}\left|c_n\right|^2=a_0^2+\frac12\sum_{n=1}^{\infty}\left(a_n^2+b_n^2\right)
+> $$
 
 
 **Proof** Let $g(t)=f(-t)$. Then
@@ -495,35 +510,35 @@
 Evaluating both sides at $x=0$, we obtain the first of the Parseval's identities, since $f * g(0)=\frac{1}{2 p} \int_{-p}^p f(t) g(-t) d t=\frac{1}{2 p} \int_{-p}^p f(t) f(t) d t=\frac{1}{2 p} \int_{-p}^p f^2(t) d t$. The second identity follows from the first one by using the relationships between the Fourier coefficients (5)-(7). The details are left as an exercise.
 
 
-
-+++
-
-
-
-
-
+---
 In the following example of a convolution, we will avoid computing directly from the definition. Instead we will compute the Fourier coefficients of the convolution and then identify the convolution function from its Fourier coefficients.
 
 
-
-
-> [!exercise] EXAMPLE 4 Computing convolutions
+> [!exercise|35c8596b-954e-5319-8988-f502c38bd5bd.local at=9b1e9fc4-7b31-5945-92aa-c9985bafab74] EXAMPLE 4 Computing convolutions
 > 
 > Find $f * f(x)$, where $f(x)$ denotes the $2 \pi$-periodic sawtooth function, defined on $(0,2 \pi)$ by $f(x)=\frac{1}{2}(\pi-x)$ (Figure 6).
 
 
-
-> [!figure] Figure 6
-> 
-> ![](Pasted%20image%2020260422015913.png)
-> Figure 6 Sawtooth function in Example 4 has the Fourier series $\sum_{n=1}^{\infty} \frac{\sin n x}{n}$.
-
-
-
-**Solution** Let us first compute $c_n=\hat{f}(n)$. We can use the definition of the Fourier coefficients or, better yet, since we know the Fourier cosine and sine coefficients, $a_n=0$ and $b_n=\frac{1}{n}$, we can compute $c_n$ by using (6). We have $c_n=\frac{1}{2}\left(a_n-i b_n\right)=$
-
-
-$-\frac{i}{2 n}$. From this and Theorem 2, we conclude that $\widehat{f * f}(n)=\left(-\frac{1}{2 n}\right)^2=-\frac{1}{4 n^2}$. Computing the cosine and sine Fourier coefficients of $f * f$ from (7), we find that the Fourier sine coefficients are 0, while the Fourier cosine coefficients are $-\frac{1}{2 n^2}$. We now ask: Which function has these Fourier coefficients? Consider the function from Exercise 9, Section 7.2. Call this function $h$. Replace $x$ by $x-\pi$ in the Fourier series and get.
+```scientific-figure
+id: aee8e9c9-7ee5-418c-8778-5ed2d45ab178
+numbered: false
+title: ""
+caption: "**Figure 6.** Sawtooth function in Example 4 has the Fourier series $\\sum_{n=1}^{\\infty} \\frac{\\sin n x}{n}$."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 07 Fourier Series/images/Pasted image 20260422015913.png
+    caption: ""
+```
+
+
+##### solution
+
+Let us first compute $c_n=\hat{f}(n)$. We can use the definition of the Fourier coefficients or, better yet, since we know the Fourier cosine and sine coefficients, $a_n=0$ and $b_n=\frac{1}{n}$, we can compute $c_n$ by using (6). We have $c_n=\frac{1}{2}\left(a_n-i b_n\right)=$
+
+
+$-\frac{i}{2 n}$. From this and Theorem 2, we conclude that $\widehat{f * f}(n)=\left(-\frac{i}{2 n}\right)^2=-\frac{1}{4 n^2}$. Computing the cosine and sine Fourier coefficients of $f * f$ from (7), we find that the Fourier sine coefficients are 0, while the Fourier cosine coefficients are $-\frac{1}{2 n^2}$. We now ask: Which function has these Fourier coefficients? Consider the function from Exercise 9, Section 7.2. Call this function $h$. Replace $x$ by $x-\pi$ in the Fourier series and get.
 
 $$
 h(x-\pi)=\frac{\pi^2}{3}+4 \sum_{n=1}^{\infty} \frac{(-1)^n}{n^2} \cos n(x-\pi)=\frac{\pi^2}{3}+4 \sum_{n=1}^{\infty} \frac{1}{n^2} \cos n x
@@ -545,33 +560,37 @@
 The graph of $f * f$ is shown in Figure 7. It is continuous and piecewise smooth, even though $f$ is not continuous for all $x$.
 
 
-
-> [!figure] Figure 7
-> 
-> ![](Pasted%20image%2020260422020654.png)
-> Figure 7 The convolution of the sawtooth function with itself is a continuous function, given on $[0,2 \pi]$ by
-> 
-> $$
-> \frac{1}{8}\left(\frac{\pi^2}{3}-(x-\pi)^2\right) .
-> $$
-
-
-
-
-++++
-
-
-
+```scientific-figure
+id: b66e1004-d34a-4863-89b0-9920633582df
+numbered: false
+title: ""
+caption: |-
+  **Figure 7.** The convolution of the sawtooth function with itself is a continuous function, given on $[0,2 \pi]$ by
+
+  $$
+  \frac{1}{8}\left(\frac{\pi^2}{3}-(x-\pi)^2\right) .
+  $$
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 07 Fourier Series/images/Pasted image 20260422020654.png
+    caption: ""
+```
+
+
+---
 The final result of this section is an interesting application of Parseval's identity, which implies that the Fourier series of a continuous piecewise smooth function is uniformly and absolutely convergent. We stated this result in Theorem 2, Section 7.2, and proved it under the further assumption that $f^{\prime}$ is piecewise smooth.
 
 
-
-> [!theorem]
+<!-- Source label:  -->
+> [!theorem|f1e650f3-158b-5939-a4a8-920757dce201.local at=2f44e0d3-e6b5-5f3e-a29b-bd8fb6fc8b9a] Absolute and Uniform Fourier Convergence for a Continuous Piecewise Smooth Function
+> Let $p>0$ and let $f$ be a $2p$-periodic function.
+>
 > Suppose that $f$ is continuous with piecewise continuous derivative $f^{\prime}$. Then the Fourier series of $f$ converges uniformly and absolutely for all $x$.
 
 
-
-**Proof** Denote the Fourier coefficients of $f$ by $a_n$ and $b_n$ and those of $f^{\prime}$ by $a_n^{\prime}$ and $b_n^{\prime}$. It is enough to show that $\sum_{n=1}^{\infty}\left(\left|a_n\right|+\left|b_n\right|\right)<\infty$. We will prove that $\sum_{n=1}^{\infty}\left|a_n\right|<\infty$, since the sum with the $b_n$ is handled similarly. From the proof of Theorem 2, Section 7.2, we have
+**Proof** Rescale to period $2\pi$; absolute and uniform convergence are unchanged by this change of variable. Denote the Fourier coefficients of $f$ by $a_n$ and $b_n$ and those of $f^{\prime}$ by $a_n^{\prime}$ and $b_n^{\prime}$. It is enough to show that $\sum_{n=1}^{\infty}\left(\left|a_n\right|+\left|b_n\right|\right)<\infty$. We will prove that $\sum_{n=1}^{\infty}\left|a_n\right|<\infty$, since the sum with the $b_n$ is handled similarly. From the proof of Theorem 2, Section 7.2, we have
 
 $$
 a_n=-\frac{1}{n} b_n^{\prime} \quad \text { and } \quad b_n=\frac{1}{n} a_n^{\prime}
@@ -585,22 +604,17 @@
 $$
 
 
-Letting $N \rightarrow \infty$ and using the fact that $\sum_{n=1}^{\infty}\left|b_n^{\prime}\right|^2<\infty$, by Parseval's identity applied to $f^{\prime}$, it follows that
-
+Letting $N \rightarrow \infty$ and using the fact that $\sum_{n=1}^{\infty}\left|b_n^{\prime}\right|^2<\infty$, by Bessel’s inequality applied to the square-integrable function $f^{\prime}$, it follows that
 
 
 $$\sum_{n=1}^{\infty}\left|a_n\right| \leq\left(\sum_{n=1}^{\infty}\left|b_n^{\prime}\right|^2\right)^{\frac{1}{2}}\left(\sum_{n=1}^{\infty} \frac{1}{n^2}\right)^{\frac{1}{2}}<\infty.$$
 
 
-+++
-
-
-
+---
 # Exercises 7.5
 
 
-
-> [!exercise]
+> [!exercise|5877c5ff-5f39-58e1-a0b9-251982af922b.local at=f174a84f-1a08-58b4-8bcd-a77931a65bee]
 > In Exercises 1-6, find the complex form of the Fourier series of the given $2 \pi$-periodic function.
 > 1. $f(x)=\cosh a x$ if $-\pi<x<\pi(a \neq 0, \pm i, \pm 2 i, \pm 3 i, \ldots)$. **(Hint: Example 1.)**
 > 2. $f(x)=\sinh a x$ if $-\pi<x<\pi(a \neq 0, \pm i, \pm 2 i, \pm 3 i, \ldots)$. **(Hint: Example 1.)**
@@ -612,8 +626,7 @@
 > 
 
 
-
-> [!exercise]
+> [!exercise|7a1b3d26-e56e-525a-b348-83a43e23c0cd.local at=3a4b1558-d4ee-5688-a353-1499e821dd87]
 > In Exercises 7-8, find the Fourier series of the given function by using (5) and (7) or by manipulating the complex form of the Fourier series.
 > 7. $f(x)$ is as in Exercise 3.
 > 8. $f(x)$ is as in Exercise 4.
@@ -621,27 +634,19 @@
 > 
 
 
-
-
-> [!exercise]
+> [!exercise|776ec988-9f8f-5bd9-94ca-0b390c0c670b.local at=dc5e80ff-6ed2-5518-85f6-85f6c7180b1e]
 > 9. (a) Use the orthogonality relations of the complex exponential system (Exercise 12 , Section 3.2 ) to show that the $2 \pi$-periodic function $e^{i n x}$ is its own Fourier series.
 > (b) Let $m \leq n$ be arbitrary integers and $c_k$ be arbitrary complex numbers. What is the Fourier series of the $2 \pi$-periodic function $f(x)=\sum_{k=m}^n c_k e^{i k x}$ ?
 > 
 
 
-
-
-> [!exercise]
+> [!exercise|935dfecd-b80b-5ac0-be11-d6716398f056.local at=a3c5992c-007a-51e4-9fad-5e8375cceef3]
 > 10. (a) Derive (7) from (6).
-> (b) Show that if $f$ is real-valued, $2 p$-periodic, and piecewise smooth, and all the Fourier coefficients $c_n$ with $n<0$ are zero, then $f$ is constant. **(Hint: Use (9).)**
-> 
-
-
-
-
-
-
-> [!exercise]
+> (b) Show that if $f$ is real-valued, $2 p$-periodic, and piecewise smooth, and all the Fourier coefficients $c_n$ with $n<0$ are zero, then $f$ is constant at all continuity points (and everywhere if $f$ is continuous). **(Hint: Use (9).)**
+> 
+
+
+> [!exercise|fb656ca8-cad2-5ae9-a86a-1febecd6144b.local at=00c5ad6e-7e55-5caa-be65-201871c6fe06]
 > 11. For any real number $a \neq 0$, obtain the expansion
 > 
 > $$
@@ -659,13 +664,7 @@
 > 
 
 
-
-
-
-
-
-
-> [!exercise]
+> [!exercise|5b27d1d6-6732-5644-a5e4-03d32f8034c4.local at=d0fa6c7d-5589-5d9d-855a-6cbc6cbaf7c5]
 > 13. (a) Let $a \neq 0$ be a real number. Use Parseval's identity and Exercise 1 to derive the identity
 > 
 > $$
@@ -685,16 +684,11 @@
 > 
 
 
-
-
-
-
-
-> [!exercise]
-> In Exercises 15-16, find the Fourier series of the given function using Taylor or Laurent series expansions.
-> 15. $f(\theta)=\frac{r^{\prime \prime}}{2+r^{21 \%}}$.
-> 16. $f(\theta)=\frac{1}{3+e^{12}+e^{-2}}$.
-> 17. $f(\theta)=e^{e^{\prime \theta}}$.
+> [!exercise|c6599d33-f095-5963-a8b4-e34516eccc9d.local at=98bf9c5f-0264-5165-aab5-875e0e36f657]
+> In Exercises 15–18, find the Fourier series of the given function using Taylor or Laurent series expansions.
+> 15. $f(\theta)=\frac{e^{i\theta}}{2+e^{2i\theta}}$.
+> 16. $f(\theta)=\frac{1}{3+e^{i\theta}+e^{-i\theta}}$.
+> 17. $f(\theta)=e^{e^{i\theta}}$.
 > 18. $f(\theta)=\cos \left(e^{i \theta}\right)$.
 > 19. Which real Fourier series do you get by taking real and imaginary parts in the Fourier series of Exercise 15?
 > 20. (a) Which real Fourier series do you get by taking real and imaginary parts in the Fourier series of Exercise 17?
@@ -703,10 +697,8 @@
 > 
 
 
-
-
-> [!exercise]
-> In Exercises 21 24, you are given two $2 \pi$-periodic functions $f$ and $g$ on an interval of length $2 \pi$. (a) Compute the Fourier coefficients of $f * g$. (b) Find $f * g$ by matching its Fourier coefficients with those of a known function (as we did in Example 4).
+> [!exercise|b90eab66-dad1-5b26-8a8b-d1335697e170.local at=f45ed6af-5426-550c-bcf1-6887ed06091c]
+> In Exercises 21–24, you are given two $2 \pi$-periodic functions $f$ and $g$ on an interval of length $2 \pi$. (a) Compute the Fourier coefficients of $f * g$. (b) Find $f * g$ by matching its Fourier coefficients with those of a known function (as we did in Example 4).
 > 21. For $-\pi<x<\pi, f(x)=g(x)=x$.
 > 22. For $-\pi<x<\pi, f(x)=x$; and $g(x)=-1$ if $-\pi<x<0$ and $g(x)=1$ if $0<x<\pi$.
 > 23. For $-\pi<x<\pi, f(x)=e^{i x}+e^{-i x}$, and $g(x)$ is an arbitrary piecewise smooth function.
@@ -715,13 +707,8 @@
 > 
 
 
-
-
-
-
-
-> [!exercise]
-> Project Problem: Cotangent expansion, Bernoulli numbers, and Fourier series. In Exercises 25 27, we explore a connection between Fourier series and some important complex series expansions, and derive interesting identities.
+> [!exercise|35a93315-1766-586a-93fb-1cbd3bc1ee1f.local at=5d3ed632-73f0-5670-a4f7-ccc03595db5b]
+> Project Problem: Cotangent expansion, Bernoulli numbers, and Fourier series. In Exercises 25–27, we explore a connection between Fourier series and some important complex series expansions, and derive interesting identities.
 > 25. Consider the $2 \pi$-periodic function of Example 2, which is defined on the interval $(-\pi, \pi)$ by $f(x)=e^{a x}$, where $a \neq 0$ is an arbitrary real number.
 > (a) Evaluate the Fourier series in Example 2 at $x=\pi$ and obtain for $a \neq 0$
 > 
@@ -736,15 +723,15 @@
 > a \pi \operatorname{coth} a \pi=1+\sum_{n=1}^{\infty} \frac{2 a^2}{a^2+n^2}
 > $$
 > 
-> 26. Euler's expansion of the cotangent. Let $\Omega$ consists of the entire complex plane minus the points $z \neq \pm i, \pm 2 i, \ldots$. For $z$ in $\Omega$, consider
+> 26. Euler's expansion of the cotangent. Let $\Omega$ consists of the entire complex plane minus the points $z=\pm i,\pm2i,\ldots$. For $z$ in $\Omega$, consider
 > 
 > $$
 > \phi(z)=1+\sum_{n=1}^{\infty} \frac{2 z^2}{z^2+n^2} .
 > $$
 > 
 > 
-> (a) Complete the details of the following argument showing that $\phi$ is analytic in $\Omega$. It is enough to show that the series converges uniformly on every closed and bounded subset of $\Omega$ (Corollary 2, Section 4.2). Let $A \subset \Omega$ be closed and bounded. Let $M>0$ be an integer such that $|z|<M$ for all $z$ in $A$. Then for all $n>M+1$ and all $z$ in $A$, we have $\left|\frac{2 z 2}{z^2+n^2}\right| \leq \frac{2 M^2}{n^2-M^2}$. So the series converges uniformly on $A$ by the Weierstrass $M$-test, since $\sum_{n=M+1}^{\infty} \frac{2 M^2}{n^2-M^2}<\infty$.
-> (b) Show that the function $\psi(z)=\pi z \operatorname{coth}(\pi z)$ is analytic for all $z \neq \pm i, \pm 2 i, \ldots$.
+> (a) Complete the details of the following argument showing that $\phi$ is analytic in $\Omega$. It is enough to show that the series converges uniformly on every closed and bounded subset of $\Omega$ (Corollary 2, Section 4.2). Let $A \subset \Omega$ be closed and bounded. Let $M>0$ be an integer such that $|z|<M$ for all $z$ in $A$. Then for all $n>M+1$ and all $z$ in $A$, we have $\left|\frac{2 z^2}{z^2+n^2}\right| \leq \frac{2 M^2}{n^2-M^2}$. So the series converges uniformly on $A$ by the Weierstrass $M$-test, since $\sum_{n=M+1}^{\infty} \frac{2 M^2}{n^2-M^2}<\infty$.
+> (b) Show that the function $\psi(z)=\pi z \operatorname{coth}(\pi z)$, with the removable value $\psi(0)=1$, is analytic for all $z \neq \pm i, \pm 2 i, \ldots$.
 > (c) By Exercise 25(b), $\phi(z)=\psi(z)$ for all real $z \neq 0$. Using the identity principle (Section 4.6), conclude that $\phi(z)=\psi(z)$ for all $z$ in $\Omega$. Hence
 > 
 > $$
@@ -754,7 +741,7 @@
 > (d) Replace $z$ by $i z$ in (c) and obtain Euler's expansion of the cotangent
 > 
 > $$
-> \pi z \cot (\pi z)=1+\sum_{n=1}^{\infty} \frac{2 z^2}{z^2-n^2} \quad(z \neq \pm, \pm 2, \ldots)
+> \pi z \cot (\pi z)=1+\sum_{n=1}^{\infty} \frac{2 z^2}{z^2-n^2} \quad(z\neq\pm1,\pm2,\ldots)
 > $$
 > 
 > 27. Bernoulli numbers. (a) Using Exercise 26(d) and the expansion of the cotangent from Exercise 31, Section 4.4, obtain
@@ -783,20 +770,35 @@
 > 
 > 
 > 
-> > [!table] Table 1
-> > 
-> >
-> >
-> > |                   $n$                   |         1         |         2          |          3          |          4           |            5             |                6                 |
-> > | :-------------------------------------: | :---------------: | :----------------: | :-----------------: | :------------------: | :----------------------: | :------------------------------: |
-> > | $\sum_{k=1}^{\infty} \frac{1}{k^{2 n}}$ | $\frac{\pi^2}{6}$ | $\frac{\pi^4}{90}$ | $\frac{\pi^6}{945}$ | $\frac{\pi^8}{9450}$ | $\frac{\pi^{10}}{93555}$ | $\frac{691 \pi^{12}}{638512875}$ |
-> > Table 1. Sums of reciprocals of even powers of integers.
-> > 
-> 
-> 
-> 
-
-
-
-
-
+> ```scientific-table
+> id: 9f70cd8d-3bf5-4378-93ca-4d87724cae4d
+> numbered: false
+> title: ""
+> caption: "**Table 1.** Sums of reciprocals of even powers of positive integers."
+> captionVisible: true
+> captionPosition: below
+> rows:
+>   - - text: $n$
+>     - text: "1"
+>     - text: "2"
+>     - text: "3"
+>     - text: "4"
+>     - text: "5"
+>     - text: "6"
+>   - - text: $\sum_{k=1}^{\infty} \frac{1}{k^{2 n}}$
+>     - text: $\frac{\pi^2}{6}$
+>     - text: $\frac{\pi^4}{90}$
+>     - text: $\frac{\pi^6}{945}$
+>     - text: $\frac{\pi^8}{9450}$
+>     - text: $\frac{\pi^{10}}{93555}$
+>     - text: $\frac{691 \pi^{12}}{638512875}$
+> headerRows: 1
+> rowHeaders: false
+> style: scientific
+> ```
+> 
+> 
+> 
+
+
+

`````
