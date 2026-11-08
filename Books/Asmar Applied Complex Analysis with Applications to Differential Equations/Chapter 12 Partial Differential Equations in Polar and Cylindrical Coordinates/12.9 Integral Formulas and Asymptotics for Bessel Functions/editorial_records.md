
# Editorial records

Reading note: 12.9 Integral Formulas and Asymptotics for Bessel Functions.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem] Integral representation of integer-order Bessel functions of the first kind
> For every integer $n$ and every real $x$, the Bessel function $J_n$ of the first kind satisfies
> $$
> J_n(x)=\frac1\pi\int_0^\pi\cos(n\theta-x\sin\theta)\,d\theta.
> $$
````
### After

````text
> [!theorem] Integral Representation
> Here $J_n$ is the Bessel function of the first kind.
>
> Let $n=0, \pm 1, \pm 2, \ldots$. Then for all real $x$, we have
>
> $$
> J_{n}(x)=\frac{1}{\pi} \int_{0}^{\pi} \cos (n \theta-x \sin \theta) d \theta
> $$
````

## 2. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem] Jacobi–Anger Fourier expansion of a sinusoidal complex exponential
> For real $x$ and $\theta$,
> $$
> e^{ix\sin\theta}=\sum_{n=-\infty}^{\infty}J_n(x)e^{in\theta},
> $$
> where $J_n$ denotes the Bessel function of the first kind of integer order $n$. For each fixed $x$, the series converges absolutely and uniformly in $\theta$.
````
### After

````text
> [!theorem] Fourier Series Generating Bessel Functions
> Here $J_n$ is the Bessel function of the first kind.
>
> For all real $x$ and all real $\theta$, we have
>
> $$
> e^{i x \sin \theta}=\sum_{n=-\infty}^{\infty} J_{n}(x) e^{i n \theta}
> $$
````

## 3. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem] Large-argument asymptotic expansion of integer-order Bessel functions
> For each fixed nonnegative integer $n$, as $x\to+\infty$,
> $$
> J_n(x)=\sqrt{\frac2{\pi x}}\cos\left(x-\frac\pi4-\frac{n\pi}2\right)+O(x^{-3/2}),
> $$
> where $J_n$ is the Bessel function of the first kind. Thus a constant $C_n$ bounds the absolute error by $C_nx^{-3/2}$ for all sufficiently large positive $x$. The error is additive; no ratio limit is asserted at the zeros of the oscillatory leading term.
````
### After

````text
> [!theorem] Asymptotic Formula
> Here $J_n$ is the Bessel function of the first kind, and $x\to+\infty$.
>
> Let $n \geq 0$ be an integer. Then for all large $x$, we have
>
> $$
> J_{n}(x) = \sqrt{\frac{2}{\pi x}} \cos \left(x-\frac{\pi}{4}-\frac{n \pi}{2}\right)+\mathcal{O}\left(\frac{1}{x^{3 / 2}}\right)
> $$
>
> where the big oh notation means that the approximation is of the order $\frac{1}{x^{3 / 2}}$.
````

## 4. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!lemma] Stationary-phase approximation at a single nondegenerate interior critical point
> Let $a<b$, and let $f$ be real-valued and smooth on $[a,b]$, with a Taylor expansion near $t_0\in(a,b)$. Suppose $f'(t_0)=0$, $f''(t_0)\ne0$, and $f'(t)\ne0$ for $t\ne t_0$ in $[a,b]$. Let $g$ be a smooth complex-valued function on $[a,b]$. As $x\to+\infty$,
> $$
> \int_a^b e^{ixf(t)}g(t)\,dt=
> \sqrt{\frac{2\pi}{x}}\,\frac{g(t_0)}{\sqrt{|f''(t_0)|}}
>  e^{i\left(xf(t_0)+\frac\pi4\operatorname{sgn}f''(t_0)\right)}+O(x^{-1}).
> $$
> The phase shift is $+\pi/4$ when $f''(t_0)>0$ and $-\pi/4$ when $f''(t_0)<0$. If $g(t_0)\ne0$, the displayed leading term is an asymptotic equivalent. If $g(t_0)=0$, further terms and endpoint contributions must be examined to obtain the first nonzero approximation.
````
### After

````text
> [!lemma] Method of Stationary Phase
> Suppose that $f(t)$ is a smooth real-valued function on $[a,b]$ with a Taylor series centered at $t_0$ in the open interval $(a,b)$, such that $f^{\prime}\left(t_{0}\right)=0, f^{\prime}(t) \neq 0$ for all $t \neq t_{0}$, and $f^{\prime \prime}\left(t_{0}\right) \neq 0$. Let $g(t)$ be an arbitrary smooth complex-valued function on $[a,b]$ with $g(t_0)\ne0$. Then for large positive $x$
> $$
> \int_{a}^{b} e^{i x f(t)} g(t) d t \sim \sqrt{\frac{2 \pi}{x}} g\left(t_{0}\right) \frac{e^{i\left(x f\left(t_{0}\right) \pm \frac{\pi}{4}\right)}}{\sqrt{\left|f^{\prime \prime}\left(t_{0}\right)\right|}}
> $$
>
> where we use the plus sign if $f^{\prime \prime}\left(t_{0}\right)>0$ and the minus sign if $f^{\prime \prime}\left(t_{0}\right)<0$.
````

## 5. Move correction/commentary into the separate editorial record; keep the actual correction in the reading text.

### Before

````text
[Corrected: the printed statement omits the restriction to even $n$; the claim is false in general for odd $n$.]
````
### After

````text

````

## 6. Move correction/commentary into the separate editorial record; keep the actual correction in the reading text.

### Before

````text
[Corrected: the sine series starts at $n=0$; the printed lower limit omits its first term.]
````
### After

````text

````

## Source-to-current comparison

Source: /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 12 Partial Differential Equations in Polar and Cylindrical Coordinates/12.9 Integral Formulas and Asymptotics for Bessel Functions.md

This exact comparison preserves the full change evidence, including formatting, OCR corrections, restored source wording, and required standalone context. The entries above explain the recovery edits. The comparison is not a claim that every difference is a correction; component serialization, callout wrapping, and printed labels outside callouts are formatting.

`````diff
--- /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 12 Partial Differential Equations in Polar and Cylindrical Coordinates/12.9 Integral Formulas and Asymptotics for Bessel Functions.md
+++ /Users/gradyclopton/ObsidianVaults/complex_analysis/Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 12 Partial Differential Equations in Polar and Cylindrical Coordinates/12.9 Integral Formulas and Asymptotics for Bessel Functions.md
@@ -1,14 +1,18 @@
+
 ### 12.9 Integral Formulas and Asymptotics for Bessel Functions
 
 Bessel functions are widely used in mathematics, engineering, and physics, because they are at the heart of so many important applications. It is thus essential to get familiarized with their basic properties. To gain insight into the theory of Bessel functions we will represent them by formulas and integrals involving more familiar functions, such as the cosine and sine functions. Let us start by deriving an important integral representation for Bessel functions and then use it to show a surprising connection with Fourier series.
 
-## THEOREM 1 INTEGRAL REPRESENTATION
-
- □Let $n=0, \pm 1, \pm 2, \ldots$. Then for all $x$, we have
-
-$$
-J_{n}(x)=\frac{1}{\pi} \int_{0}^{\pi} \cos (n \theta-x \sin \theta) d \theta
-$$
+> [!theorem] Integral Representation
+> Here $J_n$ is the Bessel function of the first kind.
+>
+> Let $n=0, \pm 1, \pm 2, \ldots$. Then for all real $x$, we have
+>
+> $$
+> J_{n}(x)=\frac{1}{\pi} \int_{0}^{\pi} \cos (n \theta-x \sin \theta) d \theta
+> $$
+
+*Printed equation label: (1).*
 
 Proof We do the case $n \geq 0$, and in the exercises you can show that this case implies the formula when $n<0$. Let $x$ and $\theta$ be real numbers and set $\zeta=e^{i \theta}$. For all $\theta$, we have $|\zeta|=\left|e^{i \theta}\right|=1$. So $\zeta$ lies on the unit circle. The function $e^{-\frac{x}{2 \zeta}}$ has a series expansion about 0 in $-\frac{x}{2 \zeta}$, which is obtained by plugging $-\frac{x}{2 \zeta}$ in place of $z$ in the series expansion of $e^{z}=\sum_{k=0}^{\infty} \frac{z^{k}}{k!}$. Thus
 
@@ -16,10 +20,11 @@
 e^{\frac{x}{2}\left(\zeta-\frac{1}{\zeta}\right)}=e^{\frac{x}{2} \zeta} e^{-\frac{x}{2 \zeta}}=e^{\frac{x}{2} \zeta} \sum_{k=0}^{\infty} \frac{1}{k!}\left(-\frac{x}{2 \zeta}\right)^{k}=\sum_{k=0}^{\infty} \frac{(-1)^{k}}{k!2^{k}} x^{k} \frac{e^{\frac{x}{2} \zeta}}{\zeta^{k}} .
 $$
 
-For fixed $x$, the series is absolutely convergent for all $\theta$ (remember, $\zeta=e^{i \theta}$ ). So we can multiply both sides by $\zeta^{-n}$, integrate term by term, and get
+For fixed $x$, the series is absolutely and uniformly convergent for $0\le\theta\le2\pi$ (remember, $\zeta=e^{i \theta}$ ). So we can multiply both sides by $\zeta^{-n}$, integrate term by term, and get
 
 $$
 \frac{1}{2 \pi} \int_{0}^{2 \pi} e^{\frac{x}{2}\left(\zeta-\frac{1}{\zeta}\right)} \zeta^{-n} d \theta=\sum_{k=0}^{\infty} \frac{(-1)^{k}}{k!2^{k}} x^{k} \frac{1}{2 \pi} \int_{0}^{2 \pi} \frac{e^{\frac{x}{2} \zeta}}{\zeta^{k+n}} d \theta
+\tag{2}
 $$
 
 We claim that, for $n \geq 0$, the left side is equal to $\frac{1}{\pi} \int_{0}^{\pi} \cos (n \theta-x \sin \theta) d \theta$, and the right side is equal to $J_{n}(x)$. Obviously, we will be done once we prove these claims. We need the identities
@@ -34,7 +39,7 @@
 e^{\frac{x}{2}\left(\zeta-\frac{1}{\zeta}\right)} \zeta^{-n}=e^{i(x \sin \theta-n \theta)}=\cos (x \sin \theta-n \theta)+i \sin (x \sin \theta-n \theta) .
 $$
 
-The terms on the right side are $2 \pi$-periodic functions of $\theta$; moreover, the first one is even and the second one is odd. Using Theorem 1, Section 2.1, we obtain
+The terms on the right side are $2 \pi$-periodic functions of $\theta$; moreover, the first one is even and the second one is odd. Using Theorem 1, Section 7.1, we obtain
 
 $$
 \begin{aligned}
@@ -48,6 +53,7 @@
 
 $$
 \frac{1}{2 \pi} \int_{0}^{2 \pi} \frac{e^{\frac{x}{2} \zeta}}{\zeta^{k+n}} d \theta=\left(\frac{x}{2}\right)^{k+n} \frac{1}{(k+n)!}
+\tag{3}
 $$
 
 Then substituting this value of the integral into the right side of (2), we obtain the series expansion for $J_{n}(x)$ (see the formula following (7), Section 12.7), which would complete the proof. To prove (3), we use the Taylor series expansion of $e^{z}$, as we did before, and integrate term by term (recall $\zeta=e^{i \theta}$ ):
@@ -60,12 +66,14 @@
 \end{aligned}
 $$
 
-But $\frac{1}{2 \pi} \int_{0}^{2 \pi} e^{i(j-k-n) \theta} d \theta=0$ if $j-k-n \neq 0$ and 1 if $j=k+n$ (see Section 2.6); so only one term of the series is nonzero (when $j=k+n$ ) and (3) follows.
-
-## EXAMPLE $1 \quad J_{0}$ is bounded by 1
-
-Show that for all $x,\left|J_{0}(x)\right| \leq 1$. (Since $J_{0}(0)=1$, this inequality is best possible.)
-Solution Using (1) with $n=0$, we have
+But $\frac{1}{2 \pi} \int_{0}^{2 \pi} e^{i(j-k-n) \theta} d \theta=0$ if $j-k-n \neq 0$ and 1 if $j=k+n$ (see Section 7.6); so only one term of the series is nonzero (when $j=k+n$ ) and (3) follows.
+
+> [!exercise] EXAMPLE 1 $J_{0}$ is bounded by 1
+> Show that for all $x,\left|J_{0}(x)\right| \leq 1$. (Since $J_{0}(0)=1$, this inequality is best possible.)
+
+##### solution
+
+Using (1) with $n=0$, we have
 
 $$
 \left|J_{0}(x)\right|=\frac{1}{\pi}\left|\int_{0}^{\pi} \cos (x \sin \theta) d \theta\right| \leq \frac{1}{\pi} \int_{0}^{\pi} \overbrace{|\cos (x \sin \theta)|}^{\leq 1} d \theta \leq \frac{1}{\pi} \int_{0}^{\pi} d \theta=1
@@ -89,32 +97,48 @@
 J_{n}(x)=\frac{1}{2 \pi} \int_{0}^{2 \pi} f(\theta) e^{-i n \theta} d \theta=c_{n}
 $$
 
-Substituting into the Fourier series representation of $f(\theta)=\sum_{n=-\infty}^{\infty} c_{n} e^{i n \theta}$ (Theorem 1, Section 2.6), we obtain the following interesting result, which provides a Fourier series generating the Bessel functions.
-
-THEOREM 2 FOURIER SERIES GENERATING BESSEL FUNCTIONS
-
-For all $x$ and all $\theta$, we have
-
-$$
-e^{i x \sin \theta}=\sum_{n=-\infty}^{\infty} J_{n}(x) e^{i n \theta}
-$$
+Substituting into the Fourier series representation of $f(\theta)=\sum_{n=-\infty}^{\infty} c_{n} e^{i n \theta}$ (Theorem 1, Section 7.6), we obtain the following interesting result, which provides a Fourier series generating the Bessel functions.
+
+> [!theorem] Fourier Series Generating Bessel Functions
+> Here $J_n$ is the Bessel function of the first kind.
+>
+> For all real $x$ and all real $\theta$, we have
+>
+> $$
+> e^{i x \sin \theta}=\sum_{n=-\infty}^{\infty} J_{n}(x) e^{i n \theta}
+> $$
+
+*Printed equation label: (4).*
 
 Formula (4) has many interesting consequences that follow by simply evaluating the series at particular values of $\theta$ (see the exercises). We illustrate with an example.
 
-![](./images/1c611338-958a-44f7-9d79-2dde87e6ac2a-72_329_470_622_63.jpg)
-Figure 1 Approximation of $\cos x$ by the partial sum $J_{0}(x)+2\left(-J_{2}(x)+J_{4}(x)-\right. J_{6}(x)$ ). The graphs are almost indistinguishable on the interval $[-2 \pi, 2 \pi]$.
-
-EXAMPLE 2 Bessel functions related to $\cos x$ and $\sin x$
-Derive the following identities: For all $x$,
-
-$$
-\begin{gathered}
-\cos x=J_{0}(x)+2 \sum_{n=1}^{\infty}(-1)^{n} J_{2 n}(x) \\
-\sin x=2 \sum_{n=0}^{\infty}(-1)^{n} J_{2 n+1}(x)
-\end{gathered}
-$$
-
-Solution Put $\theta=\frac{\pi}{2}$ in (4). Then for all $x$,
+```scientific-figure
+id: 97d7d37f-0a62-4a08-9e84-aa1e867f8bf3
+numbered: false
+title: ""
+caption: Figure 1 Approximation of $\cos x$ by the partial sum $J_0(x)+2[-J_2(x)+J_4(x)-J_6(x)]$. The graphs are almost indistinguishable on the interval $[-2 \pi, 2 \pi]$.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 12 Partial Differential Equations in Polar and Cylindrical Coordinates/images/1c611338-958a-44f7-9d79-2dde87e6ac2a-72_329_470_622_63.jpg
+    caption: ""
+```
+
+
+> [!exercise] EXAMPLE 2 Bessel functions related to $\cos x$ and $\sin x$
+> Derive the following identities: For all $x$,
+>
+> $$
+> \begin{gathered}
+> \cos x=J_{0}(x)+2 \sum_{n=1}^{\infty}(-1)^{n} J_{2 n}(x) \\
+> \sin x=2 \sum_{n=0}^{\infty}(-1)^{n} J_{2 n+1}(x)
+> \end{gathered}
+> $$
+
+##### solution
+
+Put $\theta=\frac{\pi}{2}$ in (4). Then for all $x$,
 
 $$
 \begin{aligned}
@@ -128,7 +152,7 @@
 $$
 \begin{aligned}
 \cos x & =\sum_{n=-\infty}^{\infty} \cos \left(\frac{n \pi}{2}\right) J_{n}(x) \\
-& =J_{0}(x)+\sum_{n=1}^{\infty}(-1)^{n} J_{2 n}(x)+\sum_{n=-1}^{-\infty}(-1)^{n} J_{2 n}(x) \\
+& =J_{0}(x)+\sum_{n=1}^{\infty}(-1)^{n} J_{2 n}(x)+\sum_{n=-\infty}^{-1}(-1)^{n} J_{2 n}(x) \\
 & =J_{0}(x)+\sum_{n=1}^{\infty}(-1)^{n}\left(J_{2 n}(x)+J_{-2 n}(x)\right)=J_{0}(x)+2 \sum_{n=1}^{\infty}(-1)^{n} J_{2 n}(x) .
 \end{aligned}
 $$
@@ -137,47 +161,68 @@
 
 ## Asymptotics for Bessel Functions
 
-Looking at the graph of a Bessel function, say $J_{0}(x)$, we notice two features: As $x$ tends to $\infty$, the graph oscillates like a cosine or sine wave and its amplitude decays like a negative power of $x$. In Figure 2, we show the graphs of $J_{0}(x)$ and $\sqrt{\frac{2}{\pi x}} \cos \left(x-\frac{\pi}{4}\right)$. The graphs are almost identical for large $x$. In fact, a more delicate analysis reveals that the difference between them is tending to 0 at the same rate as $1 / x^{3 / 2}$. We write $J_{0}(x) \sim \sqrt{\frac{2}{\pi x}} \cos \left(x-\frac{\pi}{4}\right)$ or, more precisely,
-
-$$
-J_{0}(x) \sim \sqrt{\frac{2}{\pi x}} \cos \left(x-\frac{\pi}{4}\right)+\mathcal{O}\left(\frac{1}{x^{3 / 2}}\right),
-$$
-
-and say that $J_{0}(x)$ is asymptotic to $\sqrt{\frac{2}{\pi x}} \cos \left(x-\frac{\pi}{4}\right)$ plus a big oh of $1 / x^{3 / 2}$. The expression "big on of $1 / x^{3 / 2}$ " means that there is a constant $C>0$ such
-
-THEOREM 3 ASYMPTOTIC FORMULA
-
-## LEMMA 1 METHOD OF STATIONARY PHASE
-
-that $\left|J_{0}(x)-\sqrt{\frac{2}{\pi x}} \cos \left(x-\frac{\pi}{4}\right)\right| \leq C / x^{3 / 2}$ for all large $x$. Thus the error in the approximation tends to zero like $1 / x^{3 / 2}$. This asymptotic formula has many important consequences. For example, it follows immediately from it that $J_{0}(x)$ has infinitely many zeros and that these zeros are approximately the same as the zeros of $\cos \left(x-\frac{\pi}{4}\right)$ (Figure 2).
-
-Figure 2 The asymptotic formula says that $J_{0}(x) \sim \sqrt{\frac{2}{\pi x}} \cos \left(x-\frac{\pi}{4}\right)$ with an error of the order $1 / x^{3 / 2}$. See how well the zeros of $J_{0}(x)$ are approximated by the zeros of $\cos \left(x-\frac{\pi}{4}\right)$, which are $\frac{3 \pi}{4} \approx 2.35619, \frac{7 \pi}{4} \approx 5.49779$, $\frac{11 \pi}{4} \approx 8.63938, \ldots$. Compare with the table of zeros of $J_{0}(x)$ in the previous section.
-![](./images/1c611338-958a-44f7-9d79-2dde87e6ac2a-73_480_865_504_625.jpg)
-
-In general, we have the following asymptotic formula.
-Let $n \geq 0$ be an integer. Then for all large $x$, we have
-
-$$
-J_{n}(x) \sim \sqrt{\frac{2}{\pi x}} \cos \left(x-\frac{\pi}{4}-\frac{n \pi}{2}\right)+\mathcal{O}\left(\frac{1}{x^{3 / 2}}\right)
-$$
-
-where the big oh notation means that the approximation is of the order $\frac{1}{x^{3 / 2}}$.
+Looking at the graph of a Bessel function, say $J_{0}(x)$, we notice two features: As $x$ tends to $\infty$, the graph oscillates like a cosine or sine wave and its amplitude decays like a negative power of $x$. In Figure 2, we show the graphs of $J_{0}(x)$ and $\sqrt{\frac{2}{\pi x}} \cos \left(x-\frac{\pi}{4}\right)$. The graphs are almost identical for large $x$. In fact, a more delicate analysis reveals that the difference between them is tending to 0 at the same rate as $1 / x^{3 / 2}$. The leading approximation is $J_{0}(x) \approx \sqrt{\frac{2}{\pi x}} \cos \left(x-\frac{\pi}{4}\right)$ or, more precisely,
+
+$$
+J_{0}(x) = \sqrt{\frac{2}{\pi x}} \cos \left(x-\frac{\pi}{4}\right)+\mathcal{O}\left(\frac{1}{x^{3 / 2}}\right),
+$$
+
+and describe this as the leading oscillatory approximation $\sqrt{\frac{2}{\pi x}} \cos \left(x-\frac{\pi}{4}\right)$ plus a big oh of $1 / x^{3 / 2}$. The expression "big oh of $1 / x^{3 / 2}$ " means that there is a constant $C>0$ such that $\left|J_{0}(x)-\sqrt{\frac{2}{\pi x}} \cos \left(x-\frac{\pi}{4}\right)\right| \leq C / x^{3 / 2}$ for all large $x$. Thus the error in the approximation tends to zero like $1 / x^{3 / 2}$. This asymptotic formula has many important consequences. For example, it follows immediately from it that $J_{0}(x)$ has infinitely many zeros and that these zeros are approximately the same as the zeros of $\cos \left(x-\frac{\pi}{4}\right)$ (Figure 2).
+
+```scientific-figure
+id: eb0d6207-d7aa-4c9e-9cd0-bf5e9fb0d94b
+numbered: false
+title: ""
+caption: Figure 2 The asymptotic formula says that $J_{0}(x) \approx \sqrt{\frac{2}{\pi x}} \cos \left(x-\frac{\pi}{4}\right)$ with an error of the order $1 / x^{3 / 2}$. See how well the zeros of $J_{0}(x)$ are approximated by the zeros of $\cos \left(x-\frac{\pi}{4}\right)$, which are $\frac{3 \pi}{4} \approx 2.35619, \frac{7 \pi}{4} \approx 5.49779$, $\frac{11 \pi}{4} \approx 8.63938, \ldots$. Compare with the table of zeros of $J_{0}(x)$ in the previous section.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 12 Partial Differential Equations in Polar and Cylindrical Coordinates/images/1c611338-958a-44f7-9d79-2dde87e6ac2a-73_480_865_504_625.jpg
+    caption: ""
+```
+
+
+> [!theorem] Asymptotic Formula
+> Here $J_n$ is the Bessel function of the first kind, and $x\to+\infty$.
+>
+> Let $n \geq 0$ be an integer. Then for all large $x$, we have
+>
+> $$
+> J_{n}(x) = \sqrt{\frac{2}{\pi x}} \cos \left(x-\frac{\pi}{4}-\frac{n \pi}{2}\right)+\mathcal{O}\left(\frac{1}{x^{3 / 2}}\right)
+> $$
+>
+> where the big oh notation means that the approximation is of the order $\frac{1}{x^{3 / 2}}$.
+
+*Printed equation label: (5).*
+
 Asymptotic formulas can be derived using the method of stationary phase, from which we quote the following result.
 
-Suppose that $f(t)$ is a real-valued function with a Taylor series centered at $t_{0}$ in the interval $[a, b]$, such that $f^{\prime}\left(t_{0}\right)=0, f^{\prime}(t) \neq 0$ for all $t \neq t_{0}$, and $f^{\prime \prime}\left(t_{0}\right) \neq 0$. Let $g(t)$ be an arbitrary smooth complex-valued function on $[a, b]$. Then for large $x$
-(6)
-
-$$
-\int_{a}^{b} e^{i x f(t)} g(t) d t \sim \sqrt{\frac{2 \pi}{x}} g\left(t_{0}\right) \frac{e^{i\left(x f\left(t_{0}\right) \pm \frac{\pi}{4}\right)}}{\sqrt{\left|f^{\prime \prime}\left(t_{0}\right)\right|}}
-$$
-
-where we use the plus sign if $f^{\prime \prime}\left(t_{0}\right)>0$ and the minus sign if $f^{\prime \prime}\left(t_{0}\right)<0$.
-The function $f(t)$ is called a phase function and the point $t_{0}$ is called a stationary point. The lemma states that most of the contribution to the integral comes from the part of the function near the stationary point. To understand the reason behind this, look at the graph in Figure 3, where we have plotted the function $e^{t} \cos \left(40(t-1 / 2)^{2}\right)$, which is the real part of
-
-![](./images/1c611338-958a-44f7-9d79-2dde87e6ac2a-74_389_430_370_59.jpg)
-Figure 3 Concentration of area around the stationary point $t=1 / 2$.
-
-the function $e^{t} e^{40 i(t-1 / 2)^{2}}$. The phase function is in this case $(t-1 / 2)^{2}$. Its derivative vanishes at $t=1 / 2$, which is the stationary point. The area bounded by the graph and the $t$-axis over any interval $[a, b]$ that contains $t_{0}=1 / 2$ is equal to the integral $\int_{a}^{b} e^{t} \cos \left(40(t-1 / 2)^{2}\right) d t$. It is clear from Figure 3 that the area is concentrated around the stationary point $t=1 / 2$. Away from the stationary point, the graph oscillates and the areas cancel out. This is basically what the lemma is saying, only it is about the complex exponential and not the cosine function. However, because the phase function $f(t)$ is real-valued, $e^{i x f(t)}$ is the sum of a cosine and a sine, and so its integral is the sum of two integrals like the one we just described.
+> [!lemma] Method of Stationary Phase
+> Suppose that $f(t)$ is a smooth real-valued function on $[a,b]$ with a Taylor series centered at $t_0$ in the open interval $(a,b)$, such that $f^{\prime}\left(t_{0}\right)=0, f^{\prime}(t) \neq 0$ for all $t \neq t_{0}$, and $f^{\prime \prime}\left(t_{0}\right) \neq 0$. Let $g(t)$ be an arbitrary smooth complex-valued function on $[a,b]$ with $g(t_0)\ne0$. Then for large positive $x$
+> $$
+> \int_{a}^{b} e^{i x f(t)} g(t) d t \sim \sqrt{\frac{2 \pi}{x}} g\left(t_{0}\right) \frac{e^{i\left(x f\left(t_{0}\right) \pm \frac{\pi}{4}\right)}}{\sqrt{\left|f^{\prime \prime}\left(t_{0}\right)\right|}}
+> $$
+>
+> where we use the plus sign if $f^{\prime \prime}\left(t_{0}\right)>0$ and the minus sign if $f^{\prime \prime}\left(t_{0}\right)<0$.
+
+*Printed equation label: (6).*
+
+The function $f(t)$ is called a phase function and the point $t_{0}$ is called a stationary point. The lemma states that most of the contribution to the integral comes from the part of the function near the stationary point. To understand the reason behind this, look at the graph in Figure 3, where we have plotted the function $e^{t} \cos \left(40(t-1 / 2)^{2}\right)$, which is the real part of the function $e^{t} e^{40 i(t-1 / 2)^{2}}$. The phase function is in this case $(t-1 / 2)^{2}$. Its derivative vanishes at $t=1 / 2$, which is the stationary point. The area bounded by the graph and the $t$-axis over any interval $[a, b]$ that contains $t_{0}=1 / 2$ is equal to the integral $\int_{a}^{b} e^{t} \cos \left(40(t-1 / 2)^{2}\right) d t$. It is clear from Figure 3 that the area is concentrated around the stationary point $t=1 / 2$. Away from the stationary point, the graph oscillates and the areas cancel out. This is basically what the lemma is saying, only it is about the complex exponential and not the cosine function. However, because the phase function $f(t)$ is real-valued, $e^{i x f(t)}$ is the sum of a cosine and a sine, and so its integral is the sum of two integrals like the one we just described.
+
+```scientific-figure
+id: 00681c80-0fd6-4a32-8107-94924a32c498
+numbered: false
+title: ""
+caption: Figure 3 Concentration of area around the stationary point $t=1 / 2$.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 12 Partial Differential Equations in Polar and Cylindrical Coordinates/images/1c611338-958a-44f7-9d79-2dde87e6ac2a-74_389_430_370_59.jpg
+    caption: ""
+```
+
 
 We will sketch the proof of the lemma, but before we do so, let us see how the lemma applies toward the proof of Theorem 3.
 
@@ -209,11 +254,13 @@
 \frac{1}{2 \pi} \int_{0}^{\pi} e^{-i x \sin \theta} e^{i n \theta} d \theta \sim \frac{1}{2} \sqrt{\frac{2}{\pi x}} e^{-i\left(x-\frac{\pi}{4}-n \frac{\pi}{2}\right)}
 $$
 
-and (5) follows upon adding the two asymptotics and simplifying with the help of the identity
+The leading term in the Bessel asymptotic formula follows upon adding the two asymptotics and simplifying with the help of the identity
 
 $$
 e^{i\left(x-\frac{\pi}{4}-n \frac{\pi}{2}\right)}+e^{-i\left(x-\frac{\pi}{4}-n \frac{\pi}{2}\right)}=2 \cos \left(x-\frac{\pi}{4}-n \frac{\pi}{2}\right)
 $$
+
+The quoted leading-order stationary-phase formula alone does not establish the sharper $O(x^{-3/2})$ remainder. That bound requires the next-order stationary-phase estimate and cancellation of the endpoint terms in the combined integral.
 
 Sketch of proof of Lemma 1. Let $I$ denote the integral on the left side of (6), and suppose that $f^{\prime \prime}\left(t_{0}\right)>0$. Expand the function $f(t)$ in a Taylor series about $t_{0}$ :
 
@@ -239,57 +286,99 @@
 
 The last displayed integrals are known as the Fresnel integrals. See [1] for their evaluation. This justifies the asymptotic formula (6) in the case $f^{\prime \prime}\left(t_{0}\right)>0$. The case $f^{\prime \prime}\left(t_{0}\right)<0$ is handled similarly.
 
-## Exercises 4.9
-
-1. Use the integral representation (1) to show that $J_{0}(0)=1$ and $J_{n}(0)=0$ for all integers $n \neq 0$.
-2. Use the integral representation (1) to show that $\left|J_{n}(x)\right| \leq 1$ for all integers $n$ and all $x$. (A better bound for $n \neq 0$ is given in Exercise 5.)
-3. Derive the series expansion for $\sin x$ in Example 2.
-4. (a) Show that $\left|e^{i x \sin \theta}\right|=1$ for all real $x$ and $\theta$.
-(b) Use Parseval's identity (Section 2.6) and the Fourier series (4) to prove that for all $x$
-
-$$
-1=\left|J_{0}(x)\right|^{2}+2 \sum_{n=1}^{\infty}\left|J_{n}(x)\right|^{2}
-$$
-
-(c) For any fixed $x$, show that $\lim _{n \rightarrow \infty} J_{n}(x)=0$.
-5. Use Exercise 4(b) to show that, for all $x,\left|J_{0}(x)\right| \leq 1$ and $\left|J_{n}(x)\right| \leq \frac{1}{\sqrt{2}}$.
-6. Take real and imaginary parts on both sides of (4) and show that, for all $x$ and all $\theta$,
-
-$$
-\begin{aligned}
-& \cos (x \sin \theta)=J_{0}(x)+2 \sum_{n=1}^{\infty} J_{2 n}(x) \cos (2 n \theta) \\
-& \sin (x \sin \theta)=2 \sum_{n=1}^{\infty} J_{2 n+1}(x) \sin (2 n+1) \theta
-\end{aligned}
-$$
-
-7. A useful fact. Suppose that $f(t)$ and $g(t)$ are continuous functions for $0 \leq t \leq \pi$, such that $f(t)=f(\pi-t)$ ( $f$ is symmetric with respect to the line $x=\frac{\pi}{2}$ ), and
-$g(t)=-g(\pi-t)$ ( $g$ is symmetric with respect to the point $\left.\left(\frac{\pi}{2}, 0\right)\right)$. Show that
-
-$$
-\int_{0}^{\pi} f(t) g(t) d t=0
-$$
-
-[Hint: Break up the integral over $\left[0, \frac{\pi}{2}\right]$ plus over $\left[\frac{\pi}{2}, \pi\right]$.]
-8. Apply the result of Exercise 7 to show that
-(a) $\int_{0}^{\pi} \cos \theta \cos (x \sin \theta) d \theta=0$;
-(b) $\int_{0}^{\pi} \sin (n \theta) \sin (x \sin \theta) d \theta=0$.
-9. Use the integral representation (1) to show that $\frac{d}{d x} J_{0}(x)=-J_{1}(x)$. [Hint: Differentiate under the integral sign. The result of Exercise 8(a) is also useful.]
-10. Completing the proof of Theorem 1. Let $\mathcal{I}_{n}(x)$ denote the right side of
-(1). We proved in the section that for $n \geq 0, \mathcal{I}_{n}(x)=J_{n}(x)$. We have defined $J_{-n}(x)$ to be $(-1)^{n} J_{n}(x)$. Thus in order to show that (1) holds for $n<0$, it is enough to show that $\mathcal{I}_{-n}(x)=(-1)^{n} \mathcal{I}_{n}(x)$.
-(a) Show that $\mathcal{I}_{-n}(x)=\frac{1}{\pi} \int_{0}^{\pi} \cos (n \theta+x \sin \theta) d \theta$.
-(b) Use the addition formula for the cosine to expand the integrands in $\mathcal{I}_{n}$ and $\mathcal{I}_{-n}$. Then apply the result of Exercise 7 to conclude that $\mathcal{I}_{n}=(-1)^{n} \mathcal{I}_{n}$.
-In Exercises 11-12, find an asymptotic formula for the given function as $x \rightarrow \infty$. If the interval of integration contains more than one stationary point, write your integral as a sum of integrals over intervals that contain one stationary point each.
-11. $\int_{-1}^{1} e^{i x^{2} \cos t} d t$.
-12. $\int_{-10}^{10} e^{i x \cos t} \sin ^{2} t d t$.
-13. Project Problem: Zeros of Bessel functions. The asymptotic formula (5) says that there is a constant $C$ such that, for all large $x$,
-
-$$
-\left|J_{n}(x)-\sqrt{\frac{2}{\pi x}} \cos \left(x-\frac{\pi}{4}-\frac{n \pi}{2}\right)\right| \leq \frac{C}{x^{3 / 2}}
-$$
-
-(a) Show that, for all large $x,\left|\sqrt{x} J_{n}(x)-\sqrt{\frac{2}{\pi}} \cos \left(x-\frac{\pi}{4}-\frac{n \pi}{2}\right)\right| \leq \frac{C}{x}$.
-(b) Show that the function $\cos \left(x-\frac{\pi}{4}-\frac{n \pi}{2}\right)$ equals to $\pm 1$ for $x=k \pi+\frac{\pi}{4}+\frac{n \pi}{2}$, $k=0,1,2, \ldots$.
-(c) Show that for large values of $x$, the function $\sqrt{x} J_{n}(x)$ has at least one zero in the interval $I_{k}=\left[k \pi+\frac{\pi}{4}+\frac{n \pi}{2},(k+1) \pi+\frac{\pi}{4}+\frac{n \pi}{2}\right]$. Conclude that $J_{n}(x)$ has infinitely many zeros; at least one in each interval $I_{k}$, for $k$ sufficiently large.
-(d) Show that the function $\cos \left(x-\frac{\pi}{4}-\frac{n \pi}{2}\right)$ is equal to 0 for $x=\alpha_{k}=\frac{\pi}{4}+\frac{(n+1) \pi}{2}+k \pi$, $k=0,1,2, \ldots$. You can actually show that the zeros of $J_{n}(x)$ are approximated by the $\alpha_{k} \mathrm{~s}$. Thus, for large $x$, the zeros of $J_{n}(x)$ are approximately $\alpha_{k}= \frac{\pi}{4}+\frac{(n+1) \pi}{2}+k \pi, k=0,1,2, \ldots$.
-(e) Test the last assertion by computing the first ten zeros of $J_{0}(x), J_{1}(x)$, and $J_{2}(x)$, and then comparing them with the sequences $\frac{\pi}{4}+\frac{(n+1) \pi}{2}+k \pi k=0,1,2, \ldots$, for $n=0,1,2$.
-(f) Use the result in (d) to show that if $\lambda_{n, j}<\lambda_{n, j+1}$ are two consecutive positive zeros of $J_{n}$, then $\lim _{j \rightarrow \infty}\left(\lambda_{n, j+1}-\lambda_{n, j}\right)=\pi$.
+## Exercises 12.9
+
+
+> [!exercise] Exercise 1
+> Use the integral representation (1) to show that $J_{0}(0)=1$ and $J_{n}(0)=0$ for all integers $n \neq 0$.
+
+
+> [!exercise] Exercise 2
+> Use the integral representation (1) to show that $\left|J_{n}(x)\right| \leq 1$ for all integers $n$ and all $x$. (A better bound for $n \neq 0$ is given in Exercise 5.)
+
+
+> [!exercise] Exercise 3
+> Derive the series expansion for $\sin x$ in Example 2.
+
+
+> [!exercise] Exercise 4
+> (a) Show that $\left|e^{i x \sin \theta}\right|=1$ for all real $x$ and $\theta$.
+> (b) Use Parseval's identity (Section 7.6) and the Fourier series (4) to prove that for all $x$
+>
+> $$
+> 1=\left|J_{0}(x)\right|^{2}+2 \sum_{n=1}^{\infty}\left|J_{n}(x)\right|^{2}
+> $$
+>
+> (c) For any fixed $x$, show that $\lim _{n \rightarrow \infty} J_{n}(x)=0$.
+
+
+> [!exercise] Exercise 5
+> Use Exercise 4(b) to show that, for all $x,\left|J_{0}(x)\right| \leq 1$ and $\left|J_n(x)\right|\le1/\sqrt2$ for nonzero integers $n$.
+
+
+> [!exercise] Exercise 6
+> Take real and imaginary parts on both sides of (4) and show that, for all $x$ and all $\theta$,
+>
+> $$
+> \begin{aligned}
+> & \cos (x \sin \theta)=J_{0}(x)+2 \sum_{n=1}^{\infty} J_{2 n}(x) \cos (2 n \theta) \\
+> & \sin (x \sin \theta)=2 \sum_{n=0}^{\infty} J_{2 n+1}(x) \sin (2 n+1) \theta
+> \end{aligned}
+> $$
+>
+> 
+
+
+> [!exercise] Exercise 7
+> A useful fact. Suppose that $f(t)$ and $g(t)$ are continuous functions for $0 \leq t \leq \pi$, such that $f(t)=f(\pi-t)$ ( $f$ is symmetric with respect to the line $x=\frac{\pi}{2}$ ), and
+> $g(t)=-g(\pi-t)$ ( $g$ is symmetric with respect to the point $\left(\frac{\pi}{2},0\right)$. Show that
+>
+> $$
+> \int_{0}^{\pi} f(t) g(t) d t=0
+> $$
+>
+> [Hint: Break up the integral over $\left[0, \frac{\pi}{2}\right]$ plus over $\left[\frac{\pi}{2}, \pi\right]$.]
+
+
+> [!exercise] Exercise 8
+> Apply the result of Exercise 7 to show that
+> (a) $\int_{0}^{\pi} \cos \theta \cos (x \sin \theta) d \theta=0$;
+> (b) For even integers $n$, show that $\int_0^\pi\sin(n\theta)\sin(x\sin\theta)\,d\theta=0$. 
+
+
+> [!exercise] Exercise 9
+> Use the integral representation (1) to show that $\frac{d}{d x} J_{0}(x)=-J_{1}(x)$. [Hint: Differentiate under the integral sign. The result of Exercise 8(a) is also useful.]
+
+
+> [!exercise] Exercise 10
+> Completing the proof of Theorem 1. Let $\mathcal{I}_{n}(x)$ denote the right side of
+> (1). We proved in the section that for $n \geq 0, \mathcal{I}_{n}(x)=J_{n}(x)$. We have defined $J_{-n}(x)$ to be $(-1)^{n} J_{n}(x)$. Thus in order to show that (1) holds for $n<0$, it is enough to show that $\mathcal{I}_{-n}(x)=(-1)^{n} \mathcal{I}_{n}(x)$.
+> (a) Show that $\mathcal{I}_{-n}(x)=\frac{1}{\pi} \int_{0}^{\pi} \cos (n \theta+x \sin \theta) d \theta$.
+> (b) Use the addition formula for the cosine to expand the integrands in $\mathcal{I}_{n}$ and $\mathcal{I}_{-n}$. Then apply the result of Exercise 7 to conclude that $\mathcal{I}_{-n}=(-1)^n\mathcal{I}_n$.
+
+
+> [!prompt] Shared exercise instructions
+> In Exercises 11-12, find an asymptotic formula for the given function as $x \rightarrow \infty$. If the interval of integration contains more than one stationary point, write your integral as a sum of integrals over intervals that contain one stationary point each.
+
+
+> [!exercise] Exercise 11
+> $\int_{-1}^{1} e^{i x^{2} \cos t} d t$.
+
+
+> [!exercise] Exercise 12
+> $\int_{-10}^{10} e^{i x \cos t} \sin ^{2} t d t$.
+
+
+> [!exercise] Exercise 13
+> Project Problem: Zeros of Bessel functions. The asymptotic formula (5) says that there is a constant $C$ such that, for all large $x$,
+>
+> $$
+> \left|J_{n}(x)-\sqrt{\frac{2}{\pi x}} \cos \left(x-\frac{\pi}{4}-\frac{n \pi}{2}\right)\right| \leq \frac{C}{x^{3 / 2}}
+> $$
+>
+> (a) Show that, for all large $x,\left|\sqrt{x} J_{n}(x)-\sqrt{\frac{2}{\pi}} \cos \left(x-\frac{\pi}{4}-\frac{n \pi}{2}\right)\right| \leq \frac{C}{x}$.
+> (b) Show that the function $\cos \left(x-\frac{\pi}{4}-\frac{n \pi}{2}\right)$ equals to $\pm 1$ for $x=k \pi+\frac{\pi}{4}+\frac{n \pi}{2}$, $k=0,1,2, \ldots$.
+> (c) Show that for large values of $x$, the function $\sqrt{x} J_{n}(x)$ has at least one zero in the interval $I_{k}=\left[k \pi+\frac{\pi}{4}+\frac{n \pi}{2},(k+1) \pi+\frac{\pi}{4}+\frac{n \pi}{2}\right]$. Conclude that $J_{n}(x)$ has infinitely many zeros; at least one in each interval $I_{k}$, for $k$ sufficiently large.
+> (d) Show that the function $\cos \left(x-\frac{\pi}{4}-\frac{n \pi}{2}\right)$ is equal to 0 for $x=\alpha_{k}=\frac{\pi}{4}+\frac{(n+1) \pi}{2}+k \pi$, $k=0,1,2, \ldots$. You can actually show that the zeros of $J_{n}(x)$ are approximated by the $\alpha_{k} \mathrm{~s}$. Thus, for large $x$, the zeros of $J_{n}(x)$ are approximately $\alpha_{k}= \frac{\pi}{4}+\frac{(n+1) \pi}{2}+k \pi, k=0,1,2, \ldots$.
+> (e) Test the last assertion by computing the first ten zeros of $J_{0}(x), J_{1}(x)$, and $J_{2}(x)$, and then comparing them with the sequences $\frac{\pi}{4}+\frac{(n+1) \pi}{2}+k \pi k=0,1,2, \ldots$, for $n=0,1,2$.
+> (f) Use the result in (d) to show that if $\lambda_{n, j}<\lambda_{n, j+1}$ are two consecutive positive zeros of $J_{n}$, then $\lim _{j \rightarrow \infty}\left(\lambda_{n, j+1}-\lambda_{n, j}\right)=\pi$.

`````
