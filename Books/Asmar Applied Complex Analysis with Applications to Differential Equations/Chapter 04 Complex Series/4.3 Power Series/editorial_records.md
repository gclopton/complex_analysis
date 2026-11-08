
# Editorial records

Reading note: 4.3 Power Series.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Callout 173: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Convergence Trichotomy for a Complex Power Series
> The coefficients and variable are complex.
>
> Given a power series $\sum_{n=0}^{\infty} c_{n}\left(z-z_{0}\right)^{n}$, there are only three possibilities:
> (i) The series converges absolutely for all $z$.
> (ii) The series converges only at $z=z_{0}$.
> (iii) There is a number $R>0$ such that the series converges absolutely if $\left|z-z_{0}\right|<R$ and diverges if $\left|z-z_{0}\right|>R$.
````
### After

````text
> [!theorem] Convergence of Power Series
> The coefficients and variable are complex.
>
> Given a power series $\sum_{n=0}^{\infty} c_{n}\left(z-z_{0}\right)^{n}$, there are only three possibilities:
> (i) The series converges absolutely for all $z$.
> (ii) The series converges only at $z=z_{0}$.
> (iii) There is a number $R>0$ such that the series converges absolutely if $\left|z-z_{0}\right|<R$ and diverges if $\left|z-z_{0}\right|>R$.
````

## 2. Callout 174: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Uniform Convergence of Complex Power Series on Closed Subdisks
> Suppose that the power series $\sum_{n=0}^{\infty} c_{n}\left(z-z_{0}\right)^{n}$ has radius of convergence $R>0$. Then the power series converges absolutely and uniformly on any closed subdisk $\left|z-z_{0}\right| \leq r$, where $0<r<R$. Consequently, the power series converges uniformly on any closed and bounded subset of its disk of convergence.
````
### After

````text
> [!theorem] Uniform Convergence of Subdisks
> Suppose that the power series $\sum_{n=0}^{\infty} c_{n}\left(z-z_{0}\right)^{n}$ has radius of convergence $R>0$. Then the power series converges absolutely and uniformly on any closed subdisk $\left|z-z_{0}\right| \leq r$, where $0<r<R$. Consequently, the power series converges uniformly on any closed and bounded subset of its disk of convergence.
````

## 3. Callout 175: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Termwise Complex Path Integration of a Power Series
> Let $R>0$ denote the radius of convergence of the power series $\sum_{n=0}^{\infty} c_{n}\left(z-z_{0}\right)^{n}$. Let $\gamma$ be any path in the disk of convergence $\left|z-z_{0}\right|<R$. Then
> $$
> \int_{\gamma}\left(\sum_{n=0}^{\infty} c_{n}\left(z-z_{0}\right)^{n}\right) d z=\sum_{n=0}^{\infty} c_{n} \int_{\gamma}\left(z-z_{0}\right)^{n} d z
> $$
> That is, the power series may be integrated term by term within its radius of convergence.
````
### After

````text
> [!theorem] Term-by-Term Integration
> Let $R>0$ denote the radius of convergence of the power series $\sum_{n=0}^{\infty} c_{n}\left(z-z_{0}\right)^{n}$. Let $\gamma$ be any path in the disk of convergence $\left|z-z_{0}\right|<R$. Then
> $$
> \int_{\gamma}\left(\sum_{n=0}^{\infty} c_{n}\left(z-z_{0}\right)^{n}\right) d z=\sum_{n=0}^{\infty} c_{n} \int_{\gamma}\left(z-z_{0}\right)^{n} d z
> $$
> That is, the power series may be integrated term by term within its radius of convergence.
````

## 4. Callout 176: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Analyticity and Termwise Differentiation of Complex Power Series
> Suppose that $f(z)=\sum_{n=0}^{\infty} c_{n}\left(z-z_{0}\right)^{n}$ is a power series with radius of convergence $R>0$. Then $f$ is analytic on the disk of convergence $\left|z-z_{0}\right|< R$. Moreover, for any integer $k \geq 1$, the power series may be differentiated $k$ times term by term within its radius of convergence to yield, for $\left|z-z_{0}\right|<R$,
>
> $$
> f^{(k)}(z)=\sum_{n=k}^{\infty} n(n-1) \cdots(n-k+1) c_{n}\left(z-z_{0}\right)^{n-k}
> $$
>
> with radius of convergence $R$.
````
### After

````text
> [!theorem] Analyticity and Termwise Differentiation of Power Series
> Suppose that $f(z)=\sum_{n=0}^{\infty} c_{n}\left(z-z_{0}\right)^{n}$ is a power series with radius of convergence $R>0$. Then $f$ is analytic on the disk of convergence $\left|z-z_{0}\right|< R$. Moreover, for any integer $k \geq 1$, the power series may be differentiated $k$ times term by term within its radius of convergence to yield, for $\left|z-z_{0}\right|<R$,
>
> $$
> f^{(k)}(z)=\sum_{n=k}^{\infty} n(n-1) \cdots(n-k+1) c_{n}\left(z-z_{0}\right)^{n-k}
> $$
>
> with radius of convergence $R$.
````

## 5. Callout 177: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!corollary] Taylor Coefficients of a Complex Power Series
> If $f(z)=\sum_{n=0}^{\infty} c_{n}\left(z-z_{0}\right)^{n}$ is a power series with radius of convergence $R>0$, then the coefficients $c_{n}$ are given by the Taylor formula
>
> $$
> c_{n}=\frac{f^{(n)}\left(z_{0}\right)}{n!} \quad(n=0,1,2, \ldots)
> $$
>
> with the usual convention: $f^{(0)}(z)=f(z)$ and $0!=1$.
````
### After

````text
> [!corollary] Taylor Coefficients
> If $f(z)=\sum_{n=0}^{\infty} c_{n}\left(z-z_{0}\right)^{n}$ is a power series with radius of convergence $R>0$, then the coefficients $c_{n}$ are given by the Taylor formula
>
> $$
> c_{n}=\frac{f^{(n)}\left(z_{0}\right)}{n!} \quad(n=0,1,2, \ldots)
> $$
>
> with the usual convention: $f^{(0)}(z)=f(z)$ and $0!=1$.
````

## 6. Callout 178: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Uniqueness of Complex Power Series Coefficients
> Let $R>0$. If two complex power series satisfy
>
> $$
> \sum_{n=0}^{\infty}a_n(z-z_0)^n=f(z)=\sum_{n=0}^{\infty}b_n(z-z_0)^n,\qquad |z-z_0|<R,
> $$
>
> then $a_n=b_n$ for every $n\geq0$. In particular, a power series $f(z)=\sum_{n=0}^{\infty}c_n(z-z_0)^n$ is identically zero on this disk if and only if every coefficient $c_n$ is zero.
````
### After

````text
> [!theorem] Uniqueness
> If $\sum_{n=0}^{\infty} a_{n}\left(z-z_{0}\right)^{n}=f(z)=\sum_{n=0}^{\infty} b_{n}\left(z-z_{0}\right)^{n}$ for all $\left|z-z_{0}\right|<R$ where $R>0$, then $a_{n}=b_{n}$ for all $n$. In particular, if $f(z)=\sum_{n=0}^{\infty} c_{n}\left(z-z_{0}\right)^{n}$ for all $\left|z-z_{0}\right|<R$, then $f(z)$ is identically 0 for all $\left|z-z_{0}\right|<R$ if and only if $c_{n}=0$ for all $n$.
````

## 7. Callout 180: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Cauchy–Hadamard Formula for the Radius of Convergence
> The radius of convergence $R$ of the series $\sum_{n=0}^{\infty} c_{n}\left(z-z_{0}\right)^{n}$ is given by
>
> $$
> \frac{1}{R}=\limsup_{n\to\infty} \sqrt[n]{\left|c_{n}\right|}
> $$
>
> with the convention $\frac{1}{0}=\infty$ and $\frac{1}{\infty}=0$.
````
### After

````text
> [!theorem] Cauchy-Hadamard Formula
> The radius of convergence $R$ of the series $\sum_{n=0}^{\infty} c_{n}\left(z-z_{0}\right)^{n}$ is given by
>
> $$
> \frac{1}{R}=\limsup_{n\to\infty} \sqrt[n]{\left|c_{n}\right|}
> $$
>
> with the convention $\frac{1}{0}=\infty$ and $\frac{1}{\infty}=0$.
````

## 8. Move editorial commentary out of the reading note.

### Before

````text
*Editorial note: [typo fixed] Restored the exponent n in both power series.*
````
### After

````text

````

## 9. Move editorial commentary out of the reading note.

### Before

````text
*Editorial note: [typo fixed] Repaired garbled “where R>0” and “for all” in the transcription.*
````
### After

````text

````

## Source-to-current comparison

Source: /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 04 Complex Series/4.3 Power Series.md

This exact comparison preserves the full change evidence, including formatting, OCR corrections, restored source wording, and required standalone context. The entries above explain the recovery edits. The comparison is not a claim that every difference is a correction; component serialization, callout wrapping, and printed labels outside callouts are formatting.

`````diff
--- /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 04 Complex Series/4.3 Power Series.md
+++ /Users/gradyclopton/ObsidianVaults/complex_analysis/Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 04 Complex Series/4.3 Power Series.md
@@ -19,7 +19,10 @@
 
 
 
-> [!theorem] Theorem 1: Convergence of Power Series
+<!-- Source label: Theorem 1: Convergence of Power Series -->
+> [!theorem] Convergence of Power Series
+> The coefficients and variable are complex.
+>
 > Given a power series $\sum_{n=0}^{\infty} c_{n}\left(z-z_{0}\right)^{n}$, there are only three possibilities:
 > (i) The series converges absolutely for all $z$.
 > (ii) The series converges only at $z=z_{0}$.
@@ -32,10 +35,18 @@
 
 
 
-> [!figure] Figure 1
-> 
-> ![300](./images/5443c314-b89d-4dd1-b950-bb21550520a5-26_412_489_1711_92.jpg)
-> Figure 1 The disk of convergence is open and centered at the center of the power series. The power series converges absolutely inside the disk, diverges outside the disk, and may converge or diverge at points on the circle of convergence.
+```scientific-figure
+id: 96714f98-8b03-44f9-bc29-2da504608015
+numbered: false
+title: ""
+caption: "**Figure 1.** The disk of convergence is open and centered at the center of the power series. The power series converges absolutely inside the disk, diverges outside the disk, and may converge or diverge at points on the circle of convergence."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 04 Complex Series/images/5443c314-b89d-4dd1-b950-bb21550520a5-26_412_489_1711_92.jpg
+    caption: ""
+```
 
 
 
@@ -48,7 +59,9 @@
 > 
 
 
-**solution** (a) We apply the ratio test. For $z \neq 1-i$, we have
+##### solution
+
+(a) We apply the ratio test. For $z \neq 1-i$, we have
 
 $$
 \rho=\lim _{n \rightarrow \infty}\left|\frac{(z-1+i)^{n+1}(n!)^{2}}{(z-1+i)^{n}((n+1)!)^{2}}\right|=\lim _{n \rightarrow \infty} \frac{|z-1+i|(n!)^{2}}{(n+1)^{2}(n!)^{2}}=\lim _{n \rightarrow \infty} \frac{|z-1+i|}{(n+1)^{2}}=0
@@ -81,7 +94,8 @@
 
 
 
-> [!theorem] Theorem 2: Uniform Convergence of Subdisks
+<!-- Source label: Theorem 2: Uniform Convergence of Subdisks -->
+> [!theorem] Uniform Convergence of Subdisks
 > Suppose that the power series $\sum_{n=0}^{\infty} c_{n}\left(z-z_{0}\right)^{n}$ has radius of convergence $R>0$. Then the power series converges absolutely and uniformly on any closed subdisk $\left|z-z_{0}\right| \leq r$, where $0<r<R$. Consequently, the power series converges uniformly on any closed and bounded subset of its disk of convergence.
 
 
@@ -100,10 +114,18 @@
 
 
 
-> [!figure] Figure 2
-> 
-> ![300](./images/5443c314-b89d-4dd1-b950-bb21550520a5-28_437_429_163_94.jpg)
-> Figure 2 If $S$ is a closed subset of the open disk of convergence $B_{R}\left(z_{0}\right)$, we can find a closed disk $S_{r}\left(z_{0}\right)$ such that $S \subset S_{r}\left(z_{0}\right) \subset B_{R}\left(z_{0}\right)$.
+```scientific-figure
+id: b34a6a21-8fdd-4d11-9362-359725f30dd6
+numbered: false
+title: ""
+caption: "**Figure 2.** If $S$ is a closed subset of the open disk of convergence $B_{R}\\left(z_{0}\\right)$, we can find a closed disk $S_{r}\\left(z_{0}\\right)$ such that $S \\subset S_{r}\\left(z_{0}\\right) \\subset B_{R}\\left(z_{0}\\right)$."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 04 Complex Series/images/5443c314-b89d-4dd1-b950-bb21550520a5-28_437_429_163_94.jpg
+    caption: ""
+```
 
 
 
@@ -116,8 +138,9 @@
 Theorem 2 opens the door for the applications of the powerful results of the previous section. Each term in a power series is a polynomial of the form $c_{n}\left(z-z_{0}\right)^{n}$ and is continuous on $\mathbb{C}$. By Theorem 2, the power series converges uniformly on subdisks $\left|z-z_{0}\right| \leq r<R$, and by Theorem 1, Section 4.2, the series is continuous on these subdisks. Letting $r$ tend up to $R$, the series is continuous on the whole open disk $\left|z-z_{0}\right|<R$. Applying Theorem 1, Section 4.2, we get the following.
 
 
-> [!theorem] Theorem 3: Term-by-Term Integration
-> Let $R>0$ denote the radius of convergence of the power series $\sum_{n=0}^{\infty} c_{n}(z- \left.z_{0}\right)^{n}$. Let $\gamma$ be any path in the disk of convergence $\left|z-z_{0}\right|<R$. Then
+<!-- Source label: Theorem 3: Term-by-Term Integration -->
+> [!theorem] Term-by-Term Integration
+> Let $R>0$ denote the radius of convergence of the power series $\sum_{n=0}^{\infty} c_{n}\left(z-z_{0}\right)^{n}$. Let $\gamma$ be any path in the disk of convergence $\left|z-z_{0}\right|<R$. Then
 > $$
 > \int_{\gamma}\left(\sum_{n=0}^{\infty} c_{n}\left(z-z_{0}\right)^{n}\right) d z=\sum_{n=0}^{\infty} c_{n} \int_{\gamma}\left(z-z_{0}\right)^{n} d z
 > $$
@@ -168,13 +191,14 @@
 
 
 
-> [!theorem] Theorem 4: Analyticity and Termwise Differentiation of Power Series
+<!-- Source label: Theorem 4: Analyticity and Termwise Differentiation of Power Series -->
+> [!theorem] Analyticity and Termwise Differentiation of Power Series
 > Suppose that $f(z)=\sum_{n=0}^{\infty} c_{n}\left(z-z_{0}\right)^{n}$ is a power series with radius of convergence $R>0$. Then $f$ is analytic on the disk of convergence $\left|z-z_{0}\right|< R$. Moreover, for any integer $k \geq 1$, the power series may be differentiated $k$ times term by term within its radius of convergence to yield, for $\left|z-z_{0}\right|<R$,
-> 
+>
 > $$
 > f^{(k)}(z)=\sum_{n=k}^{\infty} n(n-1) \cdots(n-k+1) c_{n}\left(z-z_{0}\right)^{n-k}
 > $$
-> 
+>
 > with radius of convergence $R$.
 
 
@@ -190,7 +214,9 @@
 > Find the sum $\sum_{n=1}^{\infty} n z^{n}$, and determine its radius of convergence.
 
 
-**solution** Let us go straight to the point: The series looks like the derivative of the geometric series. Indeed, term-by-term differentiating the geometric series
+##### solution
+
+Let us go straight to the point: The series looks like the derivative of the geometric series. Indeed, term-by-term differentiating the geometric series
 
 $$
 \frac{1}{1-z}=\sum_{n=0}^{\infty} z^{n}, \quad|z|<1
@@ -219,7 +245,9 @@
 
 
 
-**solution** The factorial in the denominator of the coefficients suggests looking at the exponential series:
+##### solution
+
+The factorial in the denominator of the coefficients suggests looking at the exponential series:
 
 $$
 e^{z}=\sum_{n=0}^{\infty} \frac{z^{n}}{n!}, \quad \text { for all } z
@@ -266,7 +294,9 @@
 > (b) Verify the identity $\frac{d}{d z}\left[z^{n} J_{n}(z)\right]=z^{n} J_{n-1}(z)$.
 > (c) Prove the recurrence relation: $z J_{n}^{\prime}(z)+n J_{n}(z)=z J_{n-1}(z)$.
 
-**Solution** (a) Since $J_n(z)$ is defined by a power series, to prove that it is entire, it suffices by Theorem 4 to show that the power series converges for all $z$. Using the ratio test, we have for $z \neq 0$
+##### solution
+
+(a) Since $J_n(z)$ is defined by a power series, to prove that it is entire, it suffices by Theorem 4 to show that the power series converges for all $z$. Using the ratio test, we have for $z \neq 0$
 
 $$
 \begin{aligned}
@@ -314,14 +344,14 @@
 
 
 
-> [!corollary] Corollary 1: Taylor Coefficients
+<!-- Source label: Corollary 1: Taylor Coefficients -->
+> [!corollary] Taylor Coefficients
 > If $f(z)=\sum_{n=0}^{\infty} c_{n}\left(z-z_{0}\right)^{n}$ is a power series with radius of convergence $R>0$, then the coefficients $c_{n}$ are given by the Taylor formula
-> (3)
-> 
+>
 > $$
 > c_{n}=\frac{f^{(n)}\left(z_{0}\right)}{n!} \quad(n=0,1,2, \ldots)
 > $$
-> 
+>
 > with the usual convention: $f^{(0)}(z)=f(z)$ and $0!=1$.
 
 
@@ -334,8 +364,9 @@
 
 
 
-> [!theorem] Theorem 5: Uniqueness
-> If $\sum_{n=0}^{\infty} a_{n}\left(z-z_{0}\right)^{n}=f(z)=\sum_{n=0}^{\infty} b_{n}\left(z-z_{0}\right)^{n}$ for all $\left|z-z_{0}\right|<R$ whene $_{\text {Re }} R>0$, then $a_{n}=b_{n}$ for all $n$. In particular, if $f(z)=\sum_{n=0}^{\infty} c_{n}\left(z-z_{0}\right)^{n} f_{n}$ all $\left|z-z_{0}\right|<R$, then $f(z)$ is identically 0 for all $\left|z-z_{0}\right|<R$ if and only if $c_{n}=0$ for all $n$.
+<!-- Source label: Theorem 5: Uniqueness -->
+> [!theorem] Uniqueness
+> If $\sum_{n=0}^{\infty} a_{n}\left(z-z_{0}\right)^{n}=f(z)=\sum_{n=0}^{\infty} b_{n}\left(z-z_{0}\right)^{n}$ for all $\left|z-z_{0}\right|<R$ where $R>0$, then $a_{n}=b_{n}$ for all $n$. In particular, if $f(z)=\sum_{n=0}^{\infty} c_{n}\left(z-z_{0}\right)^{n}$ for all $\left|z-z_{0}\right|<R$, then $f(z)$ is identically 0 for all $\left|z-z_{0}\right|<R$ if and only if $c_{n}=0$ for all $n$.
 
 
 **proof** By Corollary 1, $a_{n}=\frac{L^{(n)}\left(z_{0}\right)}{n!}=b_{n}$. Now the second part follows from the first part, which guarantees the uniqueness of the coefficients.
@@ -349,10 +380,10 @@
 
 
 
-> [!lemma] Lemma 1
-> (i) If a power series $\sum_{n=0}^{\infty} c_{n}\left(z-z_{0}\right)$ converges for some $z_{1} \neq z_{0}$ then it converges for all $z$ such that $\left|z-z_{0}\right|<\left|z_{1}-z_{0}\right|$.
-> (ii) If a power series $\sum_{n=0}^{\infty} c_{n}\left(z-z_{0}\right)$ diverges for some $z_{2}$ then it diverges for all $z$ such that $\left|z-z_{0}\right|>\left|z_{2}-z_{0}\right|$.
-
+<!-- Source label: Lemma 1 -->
+> [!lemma] Radial Propagation of Power Series Convergence and Divergence
+> (i) If a power series $\sum_{n=0}^{\infty} c_{n}\left(z-z_{0}\right)^n$ converges for some $z_{1} \neq z_{0}$ then it converges for all $z$ such that $\left|z-z_{0}\right|<\left|z_{1}-z_{0}\right|$.
+> (ii) If a power series $\sum_{n=0}^{\infty} c_{n}\left(z-z_{0}\right)^n$ diverges for some $z_{2}$ then it diverges for all $z$ such that $\left|z-z_{0}\right|>\left|z_{2}-z_{0}\right|$.
 
 
 **proof** We will use an argument similar to the one we used in the **proof** of Theorem 2. (i) Suppose that $\sum_{n=0}^{\infty} c_{n}\left(z-z_{0}\right)$ converges; then the sequence $\left\{c_{n}\left(z_{1}-z_{0}\right)^{n}\right\}$ is bounded. So there is an $M>0$ such that $\left|c_{n}\left(z_{1}-z_{0}\right)^{n}\right| \leq M$ for all $n \geq 0$. For $\left|z-z_{0}\right|<\left|z_{1}-z_{0}\right|$, we have $\left|\frac{z-z_{0}}{z_{1}-z_{0}}\right|=\rho<1$. Hence $\left|c_{n}\left(z-z_{0}\right)^{n}\right|=\left|c_{n}\left(z_{1}-z_{0}\right)^{n}\right|\left|\frac{c_{n}\left(z-z_{0}\right)^{n}}{c_{n}\left(z_{1}-z_{0}\right)^{n}}\right| \leq M \rho^{n}$, and the series $\sum_{n=0}^{\infty} c_{n}\left(z-z_{0}\right)$ is absolutely convergent by comparison to the convergent series $\sum M \rho^{n}$. Part (ii) follows from (i), because if the series converges for some $z$ such that $\left|z-z_{0}\right|>\left|z_{2}-z_{0}\right|$, then it will converge for $z_{2}$ by (i).
@@ -380,13 +411,14 @@
 
 
 
-> [!theorem] Theorem 6: Cauchy-Hadamard Formula
+<!-- Source label: Theorem 6: Cauchy-Hadamard Formula -->
+> [!theorem] Cauchy-Hadamard Formula
 > The radius of convergence $R$ of the series $\sum_{n=0}^{\infty} c_{n}\left(z-z_{0}\right)^{n}$ is given by
-> 
-> $$
-> \frac{1}{R}=\limsup \sqrt[n]{\left|c_{n}\right|}
-> $$
-> 
+>
+> $$
+> \frac{1}{R}=\limsup_{n\to\infty} \sqrt[n]{\left|c_{n}\right|}
+> $$
+>
 > with the convention $\frac{1}{0}=\infty$ and $\frac{1}{\infty}=0$.
 
 

`````
