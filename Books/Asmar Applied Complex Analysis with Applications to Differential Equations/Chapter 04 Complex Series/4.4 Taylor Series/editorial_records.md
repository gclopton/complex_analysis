
# Editorial records

Reading note: 4.4 Taylor Series.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Callout 181: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Taylor Expansion of a Complex Analytic Function
> Suppose that $f$ is analytic in a region $\Omega$ and $z_{0}$ is in $\Omega$. Let $B_{R}\left(z_{0}\right)$ be the largest open disk centered at $z_{0}$ and contained in $\Omega$. Then $f$ has a unique Taylor series expansion around $z_{0}$ given by
>
> $$
> f(z)=\sum_{n=0}^{\infty} \frac{f^{(n)}\left(z_{0}\right)}{n!}\left(z-z_{0}\right)^{n}, \quad\left|z-z_{0}\right|<R
> $$
>
> The coefficient $\frac{f^{(n)}\left(z_{0}\right)}{n!}$ is called the $n$th Taylor coefficient of $f$.
````
### After

````text
> [!theorem] Taylor Series
> Suppose that $f$ is analytic in a region $\Omega$ and $z_{0}$ is in $\Omega$. Let $B_{R}\left(z_{0}\right)$ be the largest open disk centered at $z_{0}$ and contained in $\Omega$. Then $f$ has a unique Taylor series expansion around $z_{0}$ given by
>
> $$
> f(z)=\sum_{n=0}^{\infty} \frac{f^{(n)}\left(z_{0}\right)}{n!}\left(z-z_{0}\right)^{n}, \quad\left|z-z_{0}\right|<R
> $$
>
> The coefficient $\frac{f^{(n)}\left(z_{0}\right)}{n!}$ is called the $n$th Taylor coefficient of $f$.
````

## 2. Callout 183: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!proposition] Parity and Taylor Coefficients of Analytic Functions
> Suppose that $f$ is analytic on $|z|<R$ and write $f(z)=\sum_{n=0}^{\infty} c_{n} z^{n},|z|<R$. $R>0$. Then
> (i) $f$ is even if and only if $c_{2 n+1}=0$ for all $n=0,1,2, \ldots$.
> (ii) $f$ is odd if and only if $c_{2 n}=0$ for all $n=0,1,2, \ldots$.
````
### After

````text
> [!proposition] Even and Odd Functions
> Suppose that $f$ is analytic on $|z|<R$ and write $f(z)=\sum_{n=0}^{\infty} c_{n} z^{n},|z|<R$. $R>0$. Then
> (i) $f$ is even if and only if $c_{2 n+1}=0$ for all $n=0,1,2, \ldots$.
> (ii) $f$ is odd if and only if $c_{2 n}=0$ for all $n=0,1,2, \ldots$.
````

## Source-to-current comparison

Source: /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 04 Complex Series/4.4 Taylor Series.md

This exact comparison preserves the full change evidence, including formatting, OCR corrections, restored source wording, and required standalone context. The entries above explain the recovery edits. The comparison is not a claim that every difference is a correction; component serialization, callout wrapping, and printed labels outside callouts are formatting.

`````diff
--- /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 04 Complex Series/4.4 Taylor Series.md
+++ /Users/gradyclopton/ObsidianVaults/complex_analysis/Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 04 Complex Series/4.4 Taylor Series.md
@@ -13,13 +13,14 @@
 
 
 
-> [!theorem] Theorem 1: Taylor Series
+<!-- Source label: Theorem 1: Taylor Series -->
+> [!theorem] Taylor Series
 > Suppose that $f$ is analytic in a region $\Omega$ and $z_{0}$ is in $\Omega$. Let $B_{R}\left(z_{0}\right)$ be the largest open disk centered at $z_{0}$ and contained in $\Omega$. Then $f$ has a unique Taylor series expansion around $z_{0}$ given by
-> 
+>
 > $$
 > f(z)=\sum_{n=0}^{\infty} \frac{f^{(n)}\left(z_{0}\right)}{n!}\left(z-z_{0}\right)^{n}, \quad\left|z-z_{0}\right|<R
 > $$
-> 
+>
 > The coefficient $\frac{f^{(n)}\left(z_{0}\right)}{n!}$ is called the $n$th Taylor coefficient of $f$.
 
 
@@ -52,10 +53,18 @@
 which is the Taylor series expansion of $f(z)$ around 0 . The advantage of Theorem 1 is that it gives us the radius of convergence without knowing the coefficients in the Taylor series. For example, Theorem 1 tells us that the Taylor series of $f(z)=\frac{1}{1-z}$ around $z_{0}=i$ has radius of convergence $R=\sqrt{2}$ (_Figure 1_).
 
 
-> [!figure] Figure 1
-> 
-> ![300](./images/5443c314-b89d-4dd1-b950-bb21550520a5-37_352_506_1017_50.jpg)
-> Figure 1 (Disk of convergence centered at $i$): The function $f(z)= \frac{1}{1-2}$ has a serious problem at $z=1$. If we expand it around $z_{0}=i$, the power series will converge in the largest disk around $i$ that does not contain 1. This disk has radius $\sqrt{2}$.
+```scientific-figure
+id: c22166ba-1bea-4baa-bbcd-fcad1fc8864d
+numbered: false
+title: ""
+caption: "**Figure 1.** (Disk of convergence centered at $i$): The function $f(z)= \\frac{1}{1-2}$ has a serious problem at $z=1$. If we expand it around $z_{0}=i$, the power series will converge in the largest disk around $i$ that does not contain 1. This disk has radius $\\sqrt{2}$."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 04 Complex Series/images/5443c314-b89d-4dd1-b950-bb21550520a5-37_352_506_1017_50.jpg
+    caption: ""
+```
 representation of the $n$th derivative
 
 
@@ -66,7 +75,9 @@
 
 
 
-**Solution** Let us first note that all three functions are entire, so the Maclaurin series will converge for all $z$; that is, $R=\infty$ in all three cases.
+##### solution
+
+Let us first note that all three functions are entire, so the Maclaurin series will converge for all $z$; that is, $R=\infty$ in all three cases.
 (a) Recall that we defined the exponential function by a power series: $e^{z}= \sum_{n=0}^{\infty} \frac{z^{n}}{n!}$ for all $z$. So this is the Maclaurin series expansion of $e^{z}$. Let us reconfirm this using Theorem 1. If $f(z)=e^{z}$, then $f^{(n)}(z)=e^{z}$, so $f^{(n)}(0)=1$ for all $n$. Therefore, as expected, the Maclaurin series is
 
 $$
@@ -120,7 +131,10 @@
 
 
 
-> [!proposition] Proposition 1
+<!-- Source label: Proposition 1 -->
+> [!proposition] Complex Analytic Extension of a Real Taylor Series
+> Let $R>0$, and let $x$ denote a real variable and $z$ a complex variable.
+>
 > Suppose that $f(x)=\sum_{n=0}^{\infty} c_{n} x^{n}$ is a Taylor series that converges for all $|x|<R$. Suppose that $g(z)$ is analytic on $|z|<R$ and $g(x)=f(x)$ for all $|x|<R$. Then the Taylor series of $g$ is $g(z)=\sum_{n=0}^{\infty} c_{n} z^{n}$ for all $|z|<R$.
 
 
@@ -132,7 +146,9 @@
 > (a) $f(z)=z e^{z^{2}}$,
 > (b) $f(z)=\frac{1}{1+z^{2}}$.
 
-**Solution** (a) Since $e^{z}=\sum_{n=0}^{\infty} \frac{z^{n}}{n!}$ is valid for all $z$, replacing $z$ by $z^{2}$, we obtain
+##### solution
+
+(a) Since $e^{z}=\sum_{n=0}^{\infty} \frac{z^{n}}{n!}$ is valid for all $z$, replacing $z$ by $z^{2}$, we obtain
 
 $$
 e^{z^{2}}=\sum_{n=0}^{\infty} \frac{\left(z^{2}\right)^{n}}{n!}=\sum_{n=0}^{\infty} \frac{z^{2 n}}{n!}, \quad \text { for all } z
@@ -161,7 +177,9 @@
 > Find the Maclaurin series expansion of $g(z)=\frac{\sin z}{z}(z \neq 0), g(0)=1$, and determine its radius of convergence.
 
 
-**Solution** The function $g$ is entire (Example 5, Section 3.6), so its Maclaurin series converges for all $z$. To find this series, start with $\sin z=\sum_{n=0}^{\infty}(-1)^{n} \frac{z^{2 n+1}}{(2 n+1)!}$, which converges for all $z$. For a given $z \neq 0$, we can multiply the series by $\frac{1}{z}$, and conclude that
+##### solution
+
+The function $g$ is entire (Example 5, Section 3.6), so its Maclaurin series converges for all $z$. To find this series, start with $\sin z=\sum_{n=0}^{\infty}(-1)^{n} \frac{z^{2 n+1}}{(2 n+1)!}$, which converges for all $z$. For a given $z \neq 0$, we can multiply the series by $\frac{1}{z}$, and conclude that
 
 $$
 \begin{aligned}
@@ -185,7 +203,8 @@
 Recall that a function $f$ is even if $f(-z)=f(z)$, and it is odd if $f(-z)= -f(z)$. The following useful property of Taylor series is obvious. You should verify it with the previous examples of this section.
 
 
-> [!proposition] Proposition 2: Even and Odd Functions
+<!-- Source label: Proposition 2: Even and Odd Functions -->
+> [!proposition] Even and Odd Functions
 > Suppose that $f$ is analytic on $|z|<R$ and write $f(z)=\sum_{n=0}^{\infty} c_{n} z^{n},|z|<R$. $R>0$. Then
 > (i) $f$ is even if and only if $c_{2 n+1}=0$ for all $n=0,1,2, \ldots$.
 > (ii) $f$ is odd if and only if $c_{2 n}=0$ for all $n=0,1,2, \ldots$.
@@ -205,23 +224,30 @@
 
 
 
-> [!lemma] Lemma 1
-> Let $z_{0}, z_{1}, z_{2}$ be distinct complex numbers such that $\left|z_{1}-z_{0}\right|<\left|z_{2}-z_{0}\right|$ (_Figure 2_). 
-> 
+<!-- Source label: Lemma 1 -->
+> [!lemma] Geometric Expansion of the Cauchy Kernel About a Complex Center
+> Let $z_{0}, z_{1}, z_{2}$ be distinct complex numbers such that $\left|z_{1}-z_{0}\right|<\left|z_{2}-z_{0}\right|$. 
+>
 > Then
-> 
-> 
-> $$
-> \frac{1}{z_{2}-z_{1}}=\sum_{n=0}^{\infty} \frac{\left(z_{1}-z_{0}\right)^{n}}{\left(z_{2}-z_{0}\right)^{n+1}} \tag{4}
-> $$
-> 
-
-
-
-> [!figure] Figure 2
-> 
-> ![300](./images/5443c314-b89d-4dd1-b950-bb21550520a5-40_410_543_1630_118.jpg)
-> Figure 2
+>
+> $$
+> \frac{1}{z_{2}-z_{1}}=\sum_{n=0}^{\infty} \frac{\left(z_{1}-z_{0}\right)^{n}}{\left(z_{2}-z_{0}\right)^{n+1}} 
+> $$
+
+
+
+```scientific-figure
+id: f66ed6f5-844c-43bc-9f24-7a22e772a974
+numbered: false
+title: ""
+caption: "**Figure 2.**"
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 04 Complex Series/images/5443c314-b89d-4dd1-b950-bb21550520a5-40_410_543_1630_118.jpg
+    caption: ""
+```
 
 
 
@@ -249,10 +275,18 @@
 (See _Figure 3_.) 
 
 
-> [!figure] Figure 3
-> 
-> ![300](./images/5443c314-b89d-4dd1-b950-bb21550520a5-41_487_459_466_60.jpg)
-> Figure 3 The picture around $z_0$ : We have $\left|z-z_0\right|<r=\left|\zeta-z_0\right|$ for all $\zeta$ on $C_r\left(z_0\right)$ and $z$ inside $B_r\left(z_0\right)$.
+```scientific-figure
+id: 106e6206-804a-4d4c-a9c8-f4592307dd14
+numbered: false
+title: ""
+caption: "**Figure 3.** The picture around $z_0$ : We have $\\left|z-z_0\\right|<r=\\left|\\zeta-z_0\\right|$ for all $\\zeta$ on $C_r\\left(z_0\\right)$ and $z$ inside $B_r\\left(z_0\\right)$."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 04 Complex Series/images/5443c314-b89d-4dd1-b950-bb21550520a5-41_487_459_466_60.jpg
+    caption: ""
+```
 
 
 
@@ -300,10 +334,18 @@
 > (a) Show that $f$ is analytic at 0 .
 > 
 > 
-> > [!figure] Figure 4
-> > 
-> > ![300](./images/5443c314-b89d-4dd1-b950-bb21550520a5-42_499_528_246_98.jpg)
-> > Figure 4 Having shown that $f(z)=\frac{z}{c^{z}-1}$ is analytic at $z=0$, its only problems are at $z=2 k \pi i$ ( $k$ integer $\neq 0$ ), which are the nonzero roots of $e^{z}-1$. Thus its Taylor series will converge in the disk $|z|<2 \pi$.
+> ```scientific-figure
+> id: e60d6493-05e3-49f5-8696-9669aed460a0
+> numbered: false
+> title: ""
+> caption: "**Figure 4.** Having shown that $f(z)=\\frac{z}{c^{z}-1}$ is analytic at $z=0$, its only problems are at $z=2 k \\pi i$ ( $k$ integer $\\neq 0$ ), which are the nonzero roots of $e^{z}-1$. Thus its Taylor series will converge in the disk $|z|<2 \\pi$."
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 04 Complex Series/images/5443c314-b89d-4dd1-b950-bb21550520a5-42_499_528_246_98.jpg
+>     caption: ""
+> ```
 > 
 > 
 > 
@@ -324,7 +366,9 @@
 > (d) Find $B_{0}, B_{1}, B_{2}, \ldots, B_{12}$, with the help of the recursion formula and a calculator.
 > (e) Show that $B_{2 n+1}=0$ for $n \geq 1$.
 
-**Solution** (a) Consider $g(z)=\frac{1}{f(z)}=\frac{e^{z}-1}{z}$ for $z \neq 0$, and $g(0)=1$. By Theorem 4, Section 3.6, $g$ is analytic at 0 . Since $g(0) \neq 0, \frac{1}{g(z)}=f(z)$ is therefore analytic at $z=0$.
+##### solution
+
+(a) Consider $g(z)=\frac{1}{f(z)}=\frac{e^{z}-1}{z}$ for $z \neq 0$, and $g(0)=1$. By Theorem 4, Section 3.6, $g$ is analytic at 0 . Since $g(0) \neq 0, \frac{1}{g(z)}=f(z)$ is therefore analytic at $z=0$.
 (b) The Maclaurin series of $f$ converges in the largest disk around $z_{0}=0$ on which $f$ is defined and analytic. For $z \neq 0, f(z)$ is analytic except when $e^{z}-\mathbf{1}=0$, where $f$ becomes unbounded. Since $e^{z}=1$ precisely when $z$ is an integer multiple of $2 \pi i$, we see that the Maclaurin series converges for all $|z|<2 \pi$, and the radius of convergence is $2 \pi$.
 (c) Multiplying both sides of the Maclaurin series expansion of $\frac{z}{e^{z}-1}$ by $e^{z}-1$ and using the Maclaurin series $e^{z}-1=z+\frac{z^{2}}{2!}+\frac{z^{3}}{3!}+\cdots=\sum_{n=1}^{\infty} \frac{z^{n}}{n!}$, we obtain
 
@@ -711,10 +755,18 @@
 > 
 > 
 > 
-> > [!figure] Figure 5
-> > 
-> > ![300](./images/5443c314-b89d-4dd1-b950-bb21550520a5-49_397_450_585_53.jpg)
-> > Figure 5 The Taylor series expansion of $\log z$ around $-1+i$ has radius of convergence $\sqrt{2}$.
+> ```scientific-figure
+> id: e62d1ebb-050a-4c3c-8938-d5c9d9f8d95c
+> numbered: false
+> title: ""
+> caption: "**Figure 5.** The Taylor series expansion of $\\log z$ around $-1+i$ has radius of convergence $\\sqrt{2}$."
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 04 Complex Series/images/5443c314-b89d-4dd1-b950-bb21550520a5-49_397_450_585_53.jpg
+>     caption: ""
+> ```
 > 
 > 
 > 

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
