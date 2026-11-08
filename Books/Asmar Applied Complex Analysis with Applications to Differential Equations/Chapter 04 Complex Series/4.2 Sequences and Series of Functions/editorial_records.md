
# Editorial records

Reading note: 4.2 Sequences and Series of Functions.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Callout 165: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!definition] Uniform Convergence of Complex-Valued Functions
> Let $E\subseteq\mathbb C$ and $f_n,f:E\to\mathbb C$.
>
> We say that $f_{n}$ converges uniformly to $f$ on $E$, and we write $\lim _{n \rightarrow \infty} f_{n}= f$ uniformly on $E$, if given $\epsilon>0$, we can find $N>0$ such that for all $n \geq N$ and all $z$ in $E$, we have $\left|f(z)-f_{n}(z)\right|<\epsilon$.
````
### After

````text
> [!definition] Uniform Convergence
> Let $E\subseteq\mathbb C$ and $f_n,f:E\to\mathbb C$.
>
> We say that $f_{n}$ converges uniformly to $f$ on $E$, and we write $\lim _{n \rightarrow \infty} f_{n}= f$ uniformly on $E$, if given $\epsilon>0$, we can find $N>0$ such that for all $n \geq N$ and all $z$ in $E$, we have $\left|f(z)-f_{n}(z)\right|<\epsilon$.
````

## 2. Callout 166: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Continuity of Uniform Limits and Uniformly Convergent Function Series
> Let $E\subseteq\mathbb C$ and let all functions below be complex-valued on $E$.
>
> (i) Suppose that $f_{n} \rightarrow f$ uniformly on $E$ and $f_{n}$ is continuous on $E$ for every $n$. Then $f$ is continuous on $E$.
> (ii) Suppose $u(z)=\sum_{n=1}^{\infty} u_{n}(z)$ converges uniformly on $E$ and $u_{n}$ is continuous on $E$ for every $n$. Then $u$ is continuous on $E$.
````
### After

````text
> [!theorem] Continuity and Uniform Convergence
> Let $E\subseteq\mathbb C$ and let all functions below be complex-valued on $E$.
>
> (i) Suppose that $f_{n} \rightarrow f$ uniformly on $E$ and $f_{n}$ is continuous on $E$ for every $n$. Then $f$ is continuous on $E$.
> (ii) Suppose $u(z)=\sum_{n=1}^{\infty} u_{n}(z)$ converges uniformly on $E$ and $u_{n}$ is continuous on $E$ for every $n$. Then $u$ is continuous on $E$.
````

## 3. Callout 167: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Interchanging Uniform Limits and Complex Path Integrals
> Let $\left\{f_{n}\right\}$ be a sequence of continuous functions on a region $\Omega$ and let $\gamma$ be a path in $\Omega$. If $f_{n} \rightarrow f$ uniformly on $\gamma$, then
>
> $$
> \lim _{n \rightarrow \infty} \int_{\gamma} f_{n}(z) d z=\int_{\gamma} f(z) d z
> $$
````
### After

````text
> [!theorem] Sequential Limits and Integrals
> Let $\left\{f_{n}\right\}$ be a sequence of continuous functions on a region $\Omega$ and let $\gamma$ be a path in $\Omega$. If $f_{n} \rightarrow f$ uniformly on $\gamma$, then
>
> $$
> \lim _{n \rightarrow \infty} \int_{\gamma} f_{n}(z) d z=\int_{\gamma} f(z) d z
> $$
````

## 4. Callout 168: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!corollary] Termwise Complex Path Integration of a Uniformly Convergent Series
> Suppose that $\left\{u_{n}\right\}$ is a sequence of continuous functions on a region $\Omega$ and let $\gamma$ be a path in $\Omega$. Suppose that $u(z)=\sum_{n=1}^{\infty} u_{n}(z)$ converges uniformly on $\gamma$. Then
>
> $$
> \int_{\gamma} u(z) d z=\sum_{n=1}^{\infty}\left(\int_{\gamma} u_{n}(z) d z\right)
> $$
````
### After

````text
> [!corollary] Term-by-Term Integration of Series
> Suppose that $\left\{u_{n}\right\}$ is a sequence of continuous functions on a region $\Omega$ and let $\gamma$ be a path in $\Omega$. Suppose that $u(z)=\sum_{n=1}^{\infty} u_{n}(z)$ converges uniformly on $\gamma$. Then
>
> $$
> \int_{\gamma} u(z) d z=\sum_{n=1}^{\infty}\left(\int_{\gamma} u_{n}(z) d z\right)
> $$
````

## 5. Callout 169: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Weierstrass M-Test for Complex Function Series
> Let $\left\{u_{n}\right\}$ be a sequence of functions on $E \subset \mathbb{C}$ and $\left\{M_{n}\right\}$ be a sequence of nonnegative numbers such that for all $n$
> (i) $\left|u_{n}(z)\right| \leq M_{n}$ for all $z$ in $E$; and
> (ii) $\sum_{n=1}^{\infty} M_{n}<\infty$.
>
> Then $\sum_{n=1}^{\infty} u_{n}(z)$ converges uniformly and absolutely on $E$.
````
### After

````text
> [!theorem] Weierstrass M-Test
> Let $\left\{u_{n}\right\}$ be a sequence of functions on $E \subset \mathbb{C}$ and $\left\{M_{n}\right\}$ be a sequence of nonnegative numbers such that for all $n$
> (i) $\left|u_{n}(z)\right| \leq M_{n}$ for all $z$ in $E$; and
> (ii) $\sum_{n=1}^{\infty} M_{n}<\infty$.
>
> Then $\sum_{n=1}^{\infty} u_{n}(z)$ converges uniformly and absolutely on $E$.
````

## 6. Callout 170: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Analyticity and Derivatives of Locally Uniform Limits
> Suppose that $\left\{f_{n}\right\}$ is a sequence of analytic functions on a region $\Omega$ such that $f_{n} \rightarrow f$ uniformly on every closed disk contained in $\Omega$. Then
> (i) $f$ is analytic on $\Omega$, and
> (ii) for any integer $k \geq 1, f_{n}^{(k)}(z) \rightarrow f^{(k)}(z)$ for all $z$ in $\Omega$. Thus, the limit of the $k$ th derivative is the $k$ th derivative of the limit.
````
### After

````text
> [!theorem] Sequential Limits and Derivatives
> Suppose that $\left\{f_{n}\right\}$ is a sequence of analytic functions on a region $\Omega$ such that $f_{n} \rightarrow f$ uniformly on every closed disk contained in $\Omega$. Then
> (i) $f$ is analytic on $\Omega$, and
> (ii) for any integer $k \geq 1, f_{n}^{(k)}(z) \rightarrow f^{(k)}(z)$ for all $z$ in $\Omega$. Thus, the limit of the $k$ th derivative is the $k$ th derivative of the limit.
````

## 7. Callout 172: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!corollary] Termwise Differentiation of Locally Uniformly Convergent Analytic Series
> Suppose that $\left\{u_{n}\right\}$ is a sequence of analytic functions on a region $\Omega$ and that $u(z)=\sum_{n=1}^{\infty} u_{n}(z)$ converges uniformly on every closed disk in $\Omega$. Then $u$ is analytic on $\Omega$; and for any integer $k \geq 1$, the series may be differentiated term by term $k$ times to yield
>
> $$
> u^{(k)}(z)=\sum_{n=1}^{\infty} u_{n}^{(k)}(z) \quad \text { for all } z \text { in } \Omega
> $$
````
### After

````text
> [!corollary] Term-by-Term Differentiation of Series
> Suppose that $\left\{u_{n}\right\}$ is a sequence of analytic functions on a region $\Omega$ and that $u(z)=\sum_{n=1}^{\infty} u_{n}(z)$ converges uniformly on every closed disk in $\Omega$. Then $u$ is analytic on $\Omega$; and for any integer $k \geq 1$, the series may be differentiated term by term $k$ times to yield
>
> $$
> u^{(k)}(z)=\sum_{n=1}^{\infty} u_{n}^{(k)}(z) \quad \text { for all } z \text { in } \Omega
> $$
````

## Source-to-current comparison

Source: /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 04 Complex Series/4.2 Sequences and Series of Functions.md

This exact comparison preserves the full change evidence, including formatting, OCR corrections, restored source wording, and required standalone context. The entries above explain the recovery edits. The comparison is not a claim that every difference is a correction; component serialization, callout wrapping, and printed labels outside callouts are formatting.

`````diff
--- /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 04 Complex Series/4.2 Sequences and Series of Functions.md
+++ /Users/gradyclopton/ObsidianVaults/complex_analysis/Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 04 Complex Series/4.2 Sequences and Series of Functions.md
@@ -14,7 +14,10 @@
 
 
 
-> [!definition] Definition 1: Uniform Convergence
+<!-- Source label: Definition 1: Uniform Convergence -->
+> [!definition] Uniform Convergence
+> Let $E\subseteq\mathbb C$ and $f_n,f:E\to\mathbb C$.
+>
 > We say that $f_{n}$ converges uniformly to $f$ on $E$, and we write $\lim _{n \rightarrow \infty} f_{n}= f$ uniformly on $E$, if given $\epsilon>0$, we can find $N>0$ such that for all $n \geq N$ and all $z$ in $E$, we have $\left|f(z)-f_{n}(z)\right|<\epsilon$.
 
 
@@ -41,7 +44,9 @@
 > (b) Does it converge uniformly on $[0,1]$ ?
 > (c) Does it converge uniformly on $[0.1,1]$ ?
 
-**solution** (a) We have $f_{n}(0)=0$ for all $n$, and so $f_{n}(x) \rightarrow 0$ if $x=0$. For any $x \neq 0$, we have
+##### solution
+
+(a) We have $f_{n}(0)=0$ for all $n$, and so $f_{n}(x) \rightarrow 0$ if $x=0$. For any $x \neq 0$, we have
 
 $$
 \lim _{n \rightarrow \infty} f_{n}(x)=\lim _{n \rightarrow \infty} \frac{2 n x}{1+n^{2} x^{2}}=\lim _{n \rightarrow \infty} \frac{1}{n} \frac{2 x}{x^{2}+\frac{1}{n^{2}}}=0
@@ -53,10 +58,18 @@
 
 
 
-> [!figure] Figure 1
-> 
-> ![](./images/5443c314-b89d-4dd1-b950-bb21550520a5-16_418_405_1016_96.jpg)
-> Figure 1 Graphs of $f_{n}(x)$ for $n=1,5,10,100 . f_{n}(x)$ has a maximum at $x=\frac{1}{n}$ in the interval $[0,1]$, and $f_{n}\left(\frac{1}{n}\right)=1$.
+```scientific-figure
+id: 0ee66157-b8d2-4b2d-a167-8f7070d5e593
+numbered: false
+title: ""
+caption: "**Figure 1.** Graphs of $f_{n}(x)$ for $n=1,5,10,100 . f_{n}(x)$ has a maximum at $x=\\frac{1}{n}$ in the interval $[0,1]$, and $f_{n}\\left(\\frac{1}{n}\\right)=1$."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 04 Complex Series/images/5443c314-b89d-4dd1-b950-bb21550520a5-16_418_405_1016_96.jpg
+    caption: ""
+```
 
 
 To confirm this, let us see how large $\left|f_{n}(x)\right|$ can get on the interval $[0,1]$. For this purpose, we compute the derivative
@@ -79,10 +92,18 @@
 (c) The situation now is much different than in (b). For $n>10$, we have $\frac{1}{n}<0.1$, and so the maximum value of $f_{n}(x)$, which we found to be 1 in (b), is not attained in the interval $[0.1,1]$; it is attained at $\frac{1}{n}$ outside this interval. So how large is $f_{n}(x)$ for $x$ in $[0.1,1]$ ? Since $f_{n}^{\prime}(x) \leq 0$ on $\left[\frac{1}{n}, 1\right], f_{n}(x)$ is decreasing on $\left[\frac{1}{n}, 1\right]$ and so the maximum of $f_{n}(x)$ for $x$ in the interval $[0.1,1]$ occurs at the left endpoint, $x=\frac{1}{10}$ (_Figure 2_). 
 
 
-> [!figure] Figure 2
-> 
-> ![](./images/5443c314-b89d-4dd1-b950-bb21550520a5-17_336_347_376_40.jpg)
-> Figure 2 Graphs of $f_{n}(x)$ for $n=1,50,100$. Note how $f_{n}(x)$ attains its maximum value in $[0.1,1]$ at $x=$ 0.1.
+```scientific-figure
+id: e4cbdc75-2a52-4e55-bd0f-267821ba2163
+numbered: false
+title: ""
+caption: "**Figure 2.** Graphs of $f_{n}(x)$ for $n=1,50,100$. Note how $f_{n}(x)$ attains its maximum value in $[0.1,1]$ at $x=$ 0.1."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 04 Complex Series/images/5443c314-b89d-4dd1-b950-bb21550520a5-17_336_347_376_40.jpg
+    caption: ""
+```
 
 
 We have $M_{n}=f_{n}\left(\frac{1}{10}\right)$ and we know that $f_{n}\left(\frac{1}{10}\right) \rightarrow 0$ as $n \rightarrow \infty$ from part (a). Thus $M_{n} \rightarrow 0$, implying that $f_{n} \rightarrow 0$ uniformly on $[0.1,1]$.
@@ -105,7 +126,10 @@
 We now look at continuity and integrability in the context of uniform limits of functions. This first part of our study does not require analyticity.
 
 
-> [!theorem] Theorem 1: Continuity and Uniform Convergence
+<!-- Source label: Theorem 1: Continuity and Uniform Convergence -->
+> [!theorem] Continuity and Uniform Convergence
+> Let $E\subseteq\mathbb C$ and let all functions below be complex-valued on $E$.
+>
 > (i) Suppose that $f_{n} \rightarrow f$ uniformly on $E$ and $f_{n}$ is continuous on $E$ for every $n$. Then $f$ is continuous on $E$.
 > (ii) Suppose $u(z)=\sum_{n=1}^{\infty} u_{n}(z)$ converges uniformly on $E$ and $u_{n}$ is continuous on $E$ for every $n$. Then $u$ is continuous on $E$.
 
@@ -140,14 +164,24 @@
 > 
 > Does the sequence converge uniformly on $|z| \leq 1$ ?
 
-**solution** The function $f_{n}(z)$ with $n=5$ is depicted in _Figure 3_. 
-
-
-
-> [!figure] Figure 3
-> 
-> ![[Screenshot 2026-04-02 at 11.01.50 PM.png]]
-> Figure 3 Graph of $f_n(z)$ (with $n=5$ ) in Example 2.
+##### solution
+
+The function $f_{n}(z)$ with $n=5$ is depicted in _Figure 3_. 
+
+
+
+```scientific-figure
+id: 2533ce84-16e3-489e-9cd9-c4e648ba4c5c
+numbered: false
+title: ""
+caption: "**Figure 3.** Graph of $f_n(z)$ (with $n=5$ ) in Example 2."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 04 Complex Series/images/Screenshot 2026-04-02 at 11.01.50 PM.png
+    caption: ""
+```
 
 
 
@@ -169,13 +203,13 @@
 
 
 
-> [!Theorem] Theorem 2: Sequential Limits and Integrals
+<!-- Source label: Theorem 2: Sequential Limits and Integrals -->
+> [!theorem] Sequential Limits and Integrals
 > Let $\left\{f_{n}\right\}$ be a sequence of continuous functions on a region $\Omega$ and let $\gamma$ be a path in $\Omega$. If $f_{n} \rightarrow f$ uniformly on $\gamma$, then
-> 
+>
 > $$
 > \lim _{n \rightarrow \infty} \int_{\gamma} f_{n}(z) d z=\int_{\gamma} f(z) d z
 > $$
-> 
 
 **Proof** Let $M_{n}=\max _{z \in \gamma}\left|f_{n}(z)-f(z)\right|$; then $M_{n} \rightarrow 0$. Using the integral inequality, Theorem 2, Section 3.2,
 
@@ -191,13 +225,13 @@
 Applying Theorem 2 to the partial sums of a uniformly convergent series, we obtain the following important corollary.
 
 
-> [!corollary] Corollary 1: Term-by-Term Integration of Series
+<!-- Source label: Corollary 1: Term-by-Term Integration of Series -->
+> [!corollary] Term-by-Term Integration of Series
 > Suppose that $\left\{u_{n}\right\}$ is a sequence of continuous functions on a region $\Omega$ and let $\gamma$ be a path in $\Omega$. Suppose that $u(z)=\sum_{n=1}^{\infty} u_{n}(z)$ converges uniformly on $\gamma$. Then
-> 
+>
 > $$
 > \int_{\gamma} u(z) d z=\sum_{n=1}^{\infty}\left(\int_{\gamma} u_{n}(z) d z\right)
 > $$
-> 
 
 
 
@@ -212,11 +246,12 @@
 
 
 
-> [!theorem] Theorem 3: Weierstrass M-Test
+<!-- Source label: Theorem 3: Weierstrass M-Test -->
+> [!theorem] Weierstrass M-Test
 > Let $\left\{u_{n}\right\}$ be a sequence of functions on $E \subset \mathbb{C}$ and $\left\{M_{n}\right\}$ be a sequence of nonnegative numbers such that for all $n$
 > (i) $\left|u_{n}(z)\right| \leq M_{n}$ for all $z$ in $E$; and
 > (ii) $\sum_{n=1}^{\infty} M_{n}<\infty$.
-> 
+>
 > Then $\sum_{n=1}^{\infty} u_{n}(z)$ converges uniformly and absolutely on $E$.
 
 
@@ -238,7 +273,9 @@
 > (c) $\sum_{n=1}^{\infty}\left(\frac{z}{2}\right)^{n},|z| \leq 1.9$.
 > (d) $\sum_{n=1}^{\infty} \frac{1}{(1-z)^{n}}, 1.01 \leq|1-z|$.
 
-**solution** We will use the notation of the Weierstrass $M$-test. For (a), $E= (-\infty, \infty), u_{n}(x)=\frac{e^{i n x}}{n^{2}}$. For all $x$ in $E$, we have
+##### solution
+
+We will use the notation of the Weierstrass $M$-test. For (a), $E= (-\infty, \infty), u_{n}(x)=\frac{e^{i n x}}{n^{2}}$. For all $x$ in $E$, we have
 
 $$
 \left|u_{n}(x)\right|=\left|\frac{e^{i n x}}{n^{2}}\right|=\frac{1}{n^{2}}=M_{n}
@@ -279,7 +316,9 @@
 
 
 
-**solution** (a) We refer to Example 3, Section 4.1, for results about the geometric series. To establish the uniform convergence of the series for $|z| \leq r<1$, we will apply the Weierstrass $M$-test. We have $\left|u_{n}(z)\right|=\left|z^{n}\right| \leq r^{n}=M_{n}$ for all $|z| \leq r$. Since $\sum_{n=0}^{\infty} M_{n}=\sum_{n=0}^{\infty} r^{n}$ is convergent if $0 \leq r<1$, we conclude that the series $\sum_{n=0}^{\infty} z^{n}$ converges uniformly for $|z| \leq r$.
+##### solution
+
+(a) We refer to Example 3, Section 4.1, for results about the geometric series. To establish the uniform convergence of the series for $|z| \leq r<1$, we will apply the Weierstrass $M$-test. We have $\left|u_{n}(z)\right|=\left|z^{n}\right| \leq r^{n}=M_{n}$ for all $|z| \leq r$. Since $\sum_{n=0}^{\infty} M_{n}=\sum_{n=0}^{\infty} r^{n}$ is convergent if $0 \leq r<1$, we conclude that the series $\sum_{n=0}^{\infty} z^{n}$ converges uniformly for $|z| \leq r$.
 (b) We now show that uniform convergence is lost when we consider the whole open disk $|z|<1$. The $n$th partial sum is $s_{n}(z)=\frac{1-z^{n+1}}{1-z}$. Let $M_{n}=\max _{|z|<1} \mid s_{n}(z)- \left.\frac{1}{1-z} \right\rvert\,$. By (1), it is enough to show that $M_{n}$ does not converge to 0 as $n \rightarrow \infty$. Indeed, for $z=r e^{i \theta}$ with $0 \leq r<1$, we have $|1-z| \leq 1+|z|=1+r, \frac{1}{|1-z|} \geq \frac{1}{1+r}$, and so
 
 $$
@@ -307,7 +346,8 @@
 
 
 
-> [!theorem] Theorem 4: Sequential Limits and Derivatives
+<!-- Source label: Theorem 4: Sequential Limits and Derivatives -->
+> [!theorem] Sequential Limits and Derivatives
 > Suppose that $\left\{f_{n}\right\}$ is a sequence of analytic functions on a region $\Omega$ such that $f_{n} \rightarrow f$ uniformly on every closed disk contained in $\Omega$. Then
 > (i) $f$ is analytic on $\Omega$, and
 > (ii) for any integer $k \geq 1, f_{n}^{(k)}(z) \rightarrow f^{(k)}(z)$ for all $z$ in $\Omega$. Thus, the limit of the $k$ th derivative is the $k$ th derivative of the limit.
@@ -316,7 +356,10 @@
 
 
 
-> [!lemma] Lemma 1
+<!-- Source label: Lemma 1 -->
+> [!lemma] Preservation of Uniform Convergence Under Multiplication by a Continuous Function
+> All functions below are complex-valued on $E\subseteq\mathbb C$.
+>
 > (i) Suppose that $f_{n} \rightarrow f$ uniformly on a closed and bounded set $E$, and $g$ is a continuous function on $E$. Then $f_{n} g \rightarrow f g$ uniformly on $E$.
 > (ii) Suppose that the series $u(z)=\sum u_{n}(z)$ converges uniformly on a closed and bounded set $E$, and $g$ is a continuous function on $E$. Then the series $g(z) u(z)=\sum g(z) u_{n}(z)$ converges uniformly on $E$.
 
@@ -355,13 +398,13 @@
 ---
 
 
-> [!corollary] Corollary 2: Term-by-Term Differentiation of Series 
+<!-- Source label: Corollary 2: Term-by-Term Differentiation of Series  -->
+> [!corollary] Term-by-Term Differentiation of Series
 > Suppose that $\left\{u_{n}\right\}$ is a sequence of analytic functions on a region $\Omega$ and that $u(z)=\sum_{n=1}^{\infty} u_{n}(z)$ converges uniformly on every closed disk in $\Omega$. Then $u$ is analytic on $\Omega$; and for any integer $k \geq 1$, the series may be differentiated term by term $k$ times to yield
-> 
+>
 > $$
 > u^{(k)}(z)=\sum_{n=1}^{\infty} u_{n}^{(k)}(z) \quad \text { for all } z \text { in } \Omega
 > $$
-> 
 
 **Proof** Apply Theorem 4 to the sequence of partial sums.
 
@@ -369,8 +412,9 @@
 
 
 > [!exercise] Exercise 6: Term-by-term differentiation of the geometric series
-> 
-> <span style="color:#ff0000; font-weight:bold">Exercise statement needed</span>
+> Use term-by-term differentiation of the geometric series to obtain a series for $1/(1-z)^2$, and justify the domain on which the differentiation is valid.
+
+##### solution
 
 The geometric series $\sum_{n=0}^{\infty} z^{n}$ converges uniformly to $\frac{1}{1-z}$ on any disk $|z| \leq r<1$, by Example 4. It will then converge uniformly on any closed disk contained in the open disk $|z|<1$. Applying Corollary 2, we may differentiate term by term in the open disk $|z|<1$ and get
 
@@ -393,7 +437,9 @@
 > (c) Let $C_{R}(0)$ denote a circle of radius $R>0$ centered at 0 , with positive orientation. Evaluate $\int_{C_{R}(0)} u(z) d z$.
 
 
-**solution** (a) For $|z| \geq \rho$, we have $\left|\frac{1}{z^{n}}\right| \leq \frac{1}{\rho^{n}}$, and so
+##### solution
+
+(a) For $|z| \geq \rho$, we have $\left|\frac{1}{z^{n}}\right| \leq \frac{1}{\rho^{n}}$, and so
 
 $$
 \left|\frac{1}{n!z^{n}}\right| \leq \frac{1}{n!\rho^{n}} \quad \text { for all } \rho \leq|z|
@@ -413,10 +459,18 @@
 
 
 
-> [!figure] Figure 4
-> 
-> ![](./images/5443c314-b89d-4dd1-b950-bb21550520a5-23_562_467_339_34.jpg)
-> Figure 4 Since $S$ is closed and 0 is not in $S$, then we can find $\rho>0$ so that $S$ is contained in the annulus $|z| \geq \rho$.
+```scientific-figure
+id: 79bcd8b2-1d0a-4fc3-a18f-1a7beefda06c
+numbered: false
+title: ""
+caption: "**Figure 4.** Since $S$ is closed and 0 is not in $S$, then we can find $\\rho>0$ so that $S$ is contained in the annulus $|z| \\geq \\rho$."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 04 Complex Series/images/5443c314-b89d-4dd1-b950-bb21550520a5-23_562_467_339_34.jpg
+    caption: ""
+```
 
 
 

`````
