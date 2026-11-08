
# Editorial records

Reading note: 17.4 The Fourier and Discrete Fourier Transforms.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!procedure] Approximate a Continuous Fourier Transform Using a Unitary IDFT
> Use the continuous transform $\widehat f(\omega)=(2\pi)^{-1/2}\int_{\mathbb R}f(x)e^{-i\omega x}\,dx$. Suppose $f$ is integrable and sufficiently regular for the sampled quadrature below.
>
> 1. Choose a window length $M>0$ so the tails outside $[-M/2,M/2]$ are acceptably small, and an even sample count $N$. A power of two is convenient for a radix-two FFT. Set $h=M/N$.
> 2. Form the wrapped samples $a_j=f(jh)$ for $0\le j<N/2$ and $a_j=f(jh-M)$ for $N/2\le j<N$.
> 3. Compute the negative-exponent unitary transform
>
> $$
> b_k=\frac1{\sqrt N}\sum_{j=0}^{N-1}a_j e^{-2\pi ijk/N},\qquad k=0,\ldots,N-1.
> $$
>
> 4. Set $q_k=k$ for $0\le k<N/2$ and $q_k=k-N$ for $N/2\le k<N$. Then use
>
> $$
> \widehat f\left(\frac{2\pi q_k}{M}\right)\approx\frac{M}{\sqrt{2\pi N}}b_k.
> $$
>
> The Nyquist bin is assigned to the negative endpoint here; it is one bin, not two independent endpoint values.
> 5. Check convergence by enlarging the window and reducing the sample spacing. Increasing $M$ at fixed $N$ also coarsens the samples, so it need not improve the total error. Control both truncation and quadrature/aliasing errors.
````
### After

````text
> [!procedure] DFT Approximation of the Fourier Transform
> Step 1: Choose and fix $M$ and $N$ with $M>0$ and $N$ even. It is customary to choose $N$ to be a power of 2 .
> Step 2: Form the function $g$ by $g(x)=f(x)$ for $0\le x<M/2$, $g(x)=f(x-M)$ for $M/2\le x<M$, and $g(x)=0$ otherwise. On the $\omega$-axis, mark the points
>
> $$
> \omega=\frac{2 \pi k}{M}, \quad k=0, \pm 1, \ldots, \pm N / 2 .
> $$
>
> Step 3: To approximate the Fourier transform at the points $\omega$ corresponding to $k=0,1, \ldots, N / 2$, use $\hat f(2\pi k/M)\approx M\mathcal F_N^{-1}(g(jM/N))(k)/\sqrt{2N\pi}$.
> Step 4: To approximate the Fourier transform at the points $\omega$ corresponding to $k=-1, \ldots,-\frac{N}{2}+1$, use the periodicity of the DFT in the following form: For $k=1,2,\ldots,N/2-1$,
>
> $$
> \widehat{f}\left(-\frac{2 \pi k}{M}\right) \approx \frac{M}{\sqrt{2 N \pi}} \mathcal{F}_{N}^{-1}\left(g\left(j \frac{M}{N}\right)\right)(N-k) .
> $$
>
> Step 5: For better results, repeat Steps $1-4$ with larger values of $M$ and $N$.
>
> Here $N\ge1$, $(\mathcal F_Nx)(k)=N^{-1/2}\sum_{j=0}^{N-1}x(j)e^{2\pi ijk/N}$ and $(\mathcal F_N^{-1}X)(k)=N^{-1/2}\sum_{j=0}^{N-1}X(j)e^{-2\pi ijk/N}$. Use $\hat f(\omega)=(2\pi)^{-1/2}\int_{\mathbb R}f(x)e^{-i\omega x}\,dx$, interpreted by mean-square extension for $f\in L^2$. Sample the continuous inverse-Fourier representative of a band-limited function. The window must control omitted tails, and $M/N$ must be small enough to control quadrature error. The two Nyquist endpoints share a single bin.
````

## 2. Move correction/commentary into the separate editorial record; keep the actual correction in the reading text.

### Before

````text
[Source clarification: the printed Exercise 5(b) implicitly identifies a function with periodically extended samples. The equality applies to that periodic extension; for a general function on the real line, the wraparound contribution must be controlled. Bold sequences and the index $m-j$ are restored here.]
````
### After

````text

````

## Source-to-current comparison

Source: /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 17 Sampling and Discrete Fourier Analysis with Applications to Partial Differential Equations/17.4 The Fourier and Discrete Fourier Transforms.md

This exact comparison preserves the full change evidence, including formatting, OCR corrections, restored source wording, and required standalone context. The entries above explain the recovery edits. The comparison is not a claim that every difference is a correction; component serialization, callout wrapping, and printed labels outside callouts are formatting.

`````diff
--- /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 17 Sampling and Discrete Fourier Analysis with Applications to Partial Differential Equations/17.4 The Fourier and Discrete Fourier Transforms.md
+++ /Users/gradyclopton/ObsidianVaults/complex_analysis/Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 17 Sampling and Discrete Fourier Analysis with Applications to Partial Differential Equations/17.4 The Fourier and Discrete Fourier Transforms.md
@@ -1,9 +1,11 @@
+
 ### 17.4 The Fourier and Discrete Fourier Transforms
 
 In this section we show how the Fourier transform can be approximated by the discrete Fourier transform. This will enable us to use the fast Fourier transform to approximate Fourier transforms numerically. The connection that we explore is based on a Riemann sum approximation of the integral defining the Fourier transform
 
 $$
 \widehat{f}(\omega)=\frac{1}{\sqrt{2 \pi}} \int_{-\infty}^{\infty} f(x) e^{-i \omega x} d x, \quad-\infty<\omega<\infty
+\tag{1}
 $$
 
 To simplify the presentation, we start with a special case.
@@ -11,15 +13,17 @@
 
 $$
 \hat{f}(\omega)=\frac{1}{\sqrt{2 \pi}} \int_{0}^{\infty} f(x) e^{-i \omega x} d x, \quad-\infty<\omega<\infty
+\tag{2}
 $$
 
 Now suppose that the improper integral can be approximated by a definite integral over a finite range as follows:
 
 $$
-\hat{f}(\omega) \approx \frac{1}{\sqrt{2 \pi}} \int_{0}^{M} f(x) r^{-i \omega x} d x, \quad-\infty \cdot \omega<\infty
-$$
-
-where $M$ is a fixed large number. The larger the value of $M$, the better the approximation of $\widehat{f}$. We now approximate the definite integral by a leftendpoint Riemann sum, with increments $\Delta x=\frac{M}{N}$, where $N$ is the number of subdivisions of the interval $[0, M]$, and get
+\hat{f}(\omega) \approx \frac{1}{\sqrt{2 \pi}} \int_{0}^{M} f(x) e^{-i \omega x} d x, \quad-\infty<\omega<\infty
+\tag{3}
+$$
+
+where $M$ is a fixed large number. For $f\in L^1$, the omitted-tail bound tends to zero as $M\to\infty$. The later quadrature error must be controlled separately by the sample spacing. We now approximate the definite integral by a left-endpoint Riemann sum, with increments $\Delta x=\frac{M}{N}$, where $N$ is the number of subdivisions of the interval $[0, M]$, and get
 
 $$
 \begin{aligned}
@@ -31,16 +35,17 @@
 Evaluating $\widehat{f}$ at $\omega=\frac{2 \pi k}{M}$, for $k=0,1, \ldots, N-1$, we get
 
 $$
-\widehat{f}\left(\frac{2 \pi k}{M}\right) \approx \frac{M}{\sqrt{2 N} \pi} \overbrace{\frac{1}{\sqrt{N}} \sum_{j=1}^{N-1} f\left(j \frac{M}{N}\right) e^{-i \frac{2 \pi k}{N} j}}^{\text {IDFT of }\left(f\left(j \frac{M}{N}\right)\right)_{j=0}^{N-1}}
-$$
-
-Comparing this with the definition of the IDFT ((2), Section 17.3), we find that the values of $\widehat{f}\left(\frac{2 \pi k}{M}\right)$ are given by a scalar multiple of the inverse discrete Fourier transform of the sequence $\left(f\left(j \frac{M}{N}\right)\right)_{j-0}^{N-1}$. In symbols, we have
+\widehat{f}\left(\frac{2 \pi k}{M}\right) \approx \frac{M}{\sqrt{2N\pi}} \overbrace{\frac{1}{\sqrt{N}} \sum_{j=0}^{N-1} f\left(j \frac{M}{N}\right) e^{-i \frac{2 \pi k}{N} j}}^{\text {IDFT of }\left(f\left(j \frac{M}{N}\right)\right)_{j=0}^{N-1}}
+$$
+
+Comparing this with the definition of the IDFT ((2), Section 17.3), we find that the values of $\widehat{f}\left(\frac{2 \pi k}{M}\right)$ are given by a scalar multiple of the inverse discrete Fourier transform of the sequence $\left(f\left(j \frac{M}{N}\right)\right)_{j=0}^{N-1}$. In symbols, we have
 (4) $\quad \hat{f}\left(\frac{2 \pi k}{M}\right) \approx \frac{M}{\sqrt{2 N \pi}} \mathcal{F}_{N}^{-1}\left(f\left(j \frac{M}{N}\right)\right)(k), \quad k=0,1, \ldots, N-1$.
 
 Evaluating $\widehat{f}$ at negative values and using a similar argument, we get
 
 $$
 \widehat{f}\left(-\frac{2 \pi k}{M}\right) \approx \frac{M}{\sqrt{2 N \pi}} \mathcal{F}_{N}\left(f\left(j \frac{M}{N}\right)\right)(k), \quad k=0,1, \ldots, N-1
+\tag{5}
 $$
 
 Case II: $f$ is an arbitrary function defined for all $x$. We go back to (1) and choose a very large value of $M$ so that
@@ -68,14 +73,16 @@
 \widehat{f}\left(\frac{2 \pi k}{M}\right) \approx & \frac{1}{\sqrt{2 \pi}} \int_{M / 2}^{M} f(x-M) e^{-i \frac{2 \pi k}{M} x} d x \\
 & +\frac{1}{\sqrt{2 \pi}} \int_{0}^{M / 2} f(x) e^{-i \frac{2 \pi k}{M} x} d x
 \end{aligned}
-$$
-
-Caution: This approximation is good only for $k= 0.1, \ldots, N / 2$. See the discussion following Example 1 below, and particularly (12).
+\tag{6}
+$$
+
+Caution: after discretization, the frequency bins are periodic. For even $N$, interpret bins $k>N/2$ as negative frequencies, as discussed after Example 1. The preceding integral identity itself is valid for every integer $k$.
 
 Now define a function $g$ by
 
 $$
-g(x)= \begin{cases}0 & \text { if } x<0, \\ f(x) & \text { if } 0 \leq x \leq \frac{M}{2}, \\ f(x-M) & \text { if } \frac{M}{2} \leq x \leq M, \\ 0 & \text { if } x>M .\end{cases}
+g(x)= \begin{cases}0 & \text { if } x<0, \\ f(x) & \text { if } 0 \leq x < \frac{M}{2}, \\ f(x-M) & \text { if } \frac{M}{2} \leq x < M, \\ 0 & \text { if } x\ge M .\end{cases}
+\tag{7}
 $$
 
 Note that $g$ fits Case I. It is constructed by cutting off $f$ outside $[-M / 2, M / 2]$ and translating the portion over $[-M / 2,0]$ to $[M / 2, M]$. Using (7), we can rewrite the right side of (6) in terms of $g$, as follows:
@@ -83,7 +90,7 @@
 $$
 \begin{aligned}
 \widehat{f}\left(\frac{2 \pi k}{M}\right) & \approx \frac{1}{\sqrt{2 \pi}} \int_{0}^{M} g(x) e^{-i \frac{2 \pi k}{M} x} d x \\
-& =\frac{1}{\sqrt{2 \pi}} \int_{-\infty}^{\infty} g(x) e^{-i \frac{2 \pi k}{M} x} d x=\tilde{g}\left(\frac{2 \pi k}{M}\right)
+& =\frac{1}{\sqrt{2 \pi}} \int_{-\infty}^{\infty} g(x) e^{-i \frac{2 \pi k}{M} x} d x=\widehat g\left(\frac{2 \pi k}{M}\right)
 \end{aligned}
 $$
 
@@ -91,13 +98,19 @@
 
 $$
 \hat{f}\left(\frac{2 \pi k}{M}\right) \approx \frac{M}{\sqrt{2 N \pi}} \mathcal{F}_{N}^{-1}\left(g\left(j \frac{M}{N}\right)\right)(k), \quad k=0,1, \ldots, N-1
-$$
-
-This is the formula that we are aiming for. It expresses the Fourier transform of $f$ in terms of an inverse discrete Fourier transform. Notice that the IDFT is really a discrete Fourier transform evaluated at $-k$ for $k=0,1,2, \ldots, N$ 1. There are several important comments to be made about the relative sizes of $M, N$, and $k$. These remarks will be more meaningful as we look at some numerical examples.
+\tag{8}
+$$
+
+This is the formula that we are aiming for. It expresses the Fourier transform of $f$ in terms of an inverse discrete Fourier transform. Notice that the IDFT is really a discrete Fourier transform evaluated at $-k$ for $k=0,1,2, \ldots, N-1$. There are several important comments to be made about the relative sizes of $M, N$, and $k$. These remarks will be more meaningful as we look at some numerical examples.
 
 In the following example, we use a well-known Fourier transform to test the validity and accuracy of the formulas that we have derived thus far.
 
-## EXAMPLE 1 Approximation of the Fourier transform
+> [!exercise] EXAMPLE 1 Approximation of the Fourier transform
+> Approximate the unitary Fourier transform of $f(x)=1$ for $-1<x<1$ and zero otherwise using $M=10$ and $N=64$. Compare the result with the exact transform and explain how the DFT bins represent negative frequencies.
+
+
+
+##### solution
 
 Consider the function $f(x)=1$ if $-1<x<1$ and 0 otherwise (Figure 1). We have, from the table of Fourier transforms,
 
@@ -105,101 +118,243 @@
 \widehat{f}(\omega)=\sqrt{\frac{2}{\pi}} \frac{\sin \omega}{\omega}, \quad-\infty<\omega<\infty .
 $$
 
-![](./images/e0b9cf26-d77c-487a-ae6f-e9bad0026586-25_361_395_186_574.jpg)
-Figure 1 Graph of $f(x)$.
-
-![](./images/e0b9cf26-d77c-487a-ae6f-e9bad0026586-25_433_507_119_1223.jpg)
-Figure 2 Graph of $\hat{f}(\omega)$.
-
-![](./images/e0b9cf26-d77c-487a-ae6f-e9bad0026586-25_356_465_595_84.jpg)
-Figure 3 Graph of $g(x)$.
+```scientific-figure
+id: 8f59a699-1bdd-4e98-b17d-cce8e433eca9
+numbered: false
+title: ""
+caption: Figure 1 Graph of $f(x)$.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 17 Sampling and Discrete Fourier Analysis with Applications to Partial Differential Equations/images/e0b9cf26-d77c-487a-ae6f-e9bad0026586-25_361_395_186_574.jpg
+    caption: ""
+```
+
+
+```scientific-figure
+id: bf8b0cd3-c017-4075-b8e8-51199c22de1c
+numbered: false
+title: ""
+caption: Figure 2 Graph of $\hat{f}(\omega)$.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 17 Sampling and Discrete Fourier Analysis with Applications to Partial Differential Equations/images/e0b9cf26-d77c-487a-ae6f-e9bad0026586-25_433_507_119_1223.jpg
+    caption: ""
+```
+
+
+```scientific-figure
+id: 78cd0d1e-22f4-4820-8bac-ce1067327adc
+numbered: false
+title: ""
+caption: Figure 3 Graph of $g(x)$.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 17 Sampling and Discrete Fourier Analysis with Applications to Partial Differential Equations/images/e0b9cf26-d77c-487a-ae6f-e9bad0026586-25_356_465_595_84.jpg
+    caption: ""
+```
+
 
 The graph of this transform is shown in Figure 2. Our goal is to use a discrete Fourier transform to approximate $\widehat{f}$. For this purpose, we apply (8) with $N=2^{6}$; $M=10$, and compute the IDFT of the sequence
 
 $$
-x=\left(g\left(j \frac{10}{2^{\mathrm{G}}}\right)\right)_{j=0}^{2^{\mathrm{G}}-1},
+x=\left(g\left(j \frac{10}{2^6}\right)\right)_{j=0}^{2^6-1},
+\tag{9}
 $$
 
 where $g(x)$ is given by (7). (The graph of $g$ is shown in Figure 3.) This will generate approximate values of the Fourier transform at the points
 
 $$
 \omega=\frac{2 \pi k}{10} \quad k=0,1,2, \ldots, 2^{6}-1 .
+\tag{10}
 $$
 
 The resulting values are plotted in Figure 4 and connected by line segments to form a continuous graph. As $k$ ranges from 0 to $2^{6}-1$, the values of $\omega$ vary from 0 to $\frac{2 \pi(63)}{10} \approx 40$. In Figure 5, we superposed the graphs of the Fourier transform and the one in Figure 4, for comparison's sake. Notice that the two graphs are pretty close near 0 , but as we get beyond 20 the approximation gets worse. There is an important reason for this phenomenon. Recall that the IDFT is periodic with period $N$, but the Fourier transform is not. So, in general, it is impossible to get a good approximation past the points $k= \pm N / 2$. Indeed, because of periodicity, we have
 
 $$
 \operatorname{IDFT}(x)(-k)=\operatorname{IDFT}(x)(N-k) .
-$$
-
-![](./images/e0b9cf26-d77c-487a-ae6f-e9bad0026586-25_399_616_1652_578.jpg)
-Figure 4 Graph of the IDFT.
-
-![](./images/e0b9cf26-d77c-487a-ae6f-e9bad0026586-25_404_609_1651_1220.jpg)
-Figure 5 Comparison of the IDFT and the Fourier transform.
-
-Thus, we expect the points corresponding to $k=N / 2, N / 2+1, \ldots, N-1$ to yield a good approximation of the Fourier transform at $\omega=\frac{-2 \pi(N-k)}{10}$. This is illustrated in Figure 6, where the portion of the graph in Figure 4, corresponding to the second half of the $\omega$-interval (those values of $\omega$ between 20 and 40), is translated over to the negative $\omega$-axis. In Figure 7 we combined the graphs in Figure 6 and the first half in Figure 5 to form our approximation of the Fourier transform on the interval ( 20,20 ). Finally, in Figure 8 we compared the Fourier transform to our approximation in Figure 7. As you can see, the approximation is quite good over the entire interval. You can obtain better results by increasing $N$ (try $N=2^{10}$ ).
-
-![](./images/e0b9cf26-d77c-487a-ae6f-e9bad0026586-26_419_471_613_0.jpg)
-Figure 6
-
-![](./images/e0b9cf26-d77c-487a-ae6f-e9bad0026586-26_395_705_633_435.jpg)
-Figure 7
-
-![](./images/e0b9cf26-d77c-487a-ae6f-e9bad0026586-26_401_665_631_1146.jpg)
-Figure 8
+\tag{11}
+$$
+
+```scientific-figure
+id: 0e6809b0-8a9a-4ca0-8d29-5c319a5d7d9f
+numbered: false
+title: ""
+caption: Figure 4 Graph of the IDFT.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 17 Sampling and Discrete Fourier Analysis with Applications to Partial Differential Equations/images/e0b9cf26-d77c-487a-ae6f-e9bad0026586-25_399_616_1652_578.jpg
+    caption: ""
+```
+
+
+```scientific-figure
+id: b9e40682-4ae1-4567-b7f7-047ed51e810c
+numbered: false
+title: ""
+caption: Figure 5 Comparison of the IDFT and the Fourier transform.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 17 Sampling and Discrete Fourier Analysis with Applications to Partial Differential Equations/images/e0b9cf26-d77c-487a-ae6f-e9bad0026586-25_404_609_1651_1220.jpg
+    caption: ""
+```
+
+
+Thus, we expect the points corresponding to $k=N / 2, N / 2+1, \ldots, N-1$ to yield a good approximation of the Fourier transform at $\omega=\frac{-2 \pi(N-k)}{10}$. This is illustrated in Figure 6, where the portion of the graph in Figure 4, corresponding to the second half of the $\omega$-interval (those values of $\omega$ between 20 and 40), is translated over to the negative $\omega$-axis. In Figure 7 we combined the graphs in Figure 6 and the first half in Figure 5 to form our approximation of the Fourier transform on the interval $(-20,20)$. Finally, in Figure 8 we compared the Fourier transform to our approximation in Figure 7. As you can see, the approximation is quite good over the entire interval. You can obtain better results by increasing $N$ (try $N=2^{10}$ ).
+
+```scientific-figure
+id: b2eb125b-9fc1-4cd5-9776-b77beb10c7bc
+numbered: false
+title: ""
+caption: Figure 6
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 17 Sampling and Discrete Fourier Analysis with Applications to Partial Differential Equations/images/e0b9cf26-d77c-487a-ae6f-e9bad0026586-26_419_471_613_0.jpg
+    caption: ""
+```
+
+
+```scientific-figure
+id: dc7b6659-45d5-4371-a01d-5353b40e3070
+numbered: false
+title: ""
+caption: Figure 7
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 17 Sampling and Discrete Fourier Analysis with Applications to Partial Differential Equations/images/e0b9cf26-d77c-487a-ae6f-e9bad0026586-26_395_705_633_435.jpg
+    caption: ""
+```
+
+
+```scientific-figure
+id: 30594a1b-4b30-4d8f-8809-dd900d0cbc9a
+numbered: false
+title: ""
+caption: Figure 8
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 17 Sampling and Discrete Fourier Analysis with Applications to Partial Differential Equations/images/e0b9cf26-d77c-487a-ae6f-e9bad0026586-26_401_665_631_1146.jpg
+    caption: ""
+```
+
 
 Let us now outline a method for approximating the Fourier transform by the IDFT, following the steps in Example 1.
 
-## DFT Approximation of the Fourier Transform
-
-Step 1: Choose and fix $M I$ and $N$ to prepare for the application of (8). It is customary to choose $V$ to be a power of 2 .
-Step 2: Form the function $g$ as described by (7). On the $\omega$-axis, mark the points
-
-$$
-\omega=\frac{2 \pi k}{M}, \quad k=0, \pm 1, \ldots, \pm N / 2 .
-$$
-
-Step 3: To approximate the Fourier transform at the points $\omega$ corresponding to $k=0,1, \ldots, N / 2$, use ( 8 ).
-Step 4: To approximate the Fourier transform at the points $\omega$ corresponding to $k=-1, \ldots,-\frac{N}{2}+1$, use (11). This amounts to using (8) in the following form: For $k=1,2, \ldots, N / 2$,
-
-$$
-\widehat{f}\left(-\frac{2 \pi k}{M}\right) \approx \frac{M}{\sqrt{2 N \pi}} \mathcal{F}_{N}^{1}\left(g\left(j \frac{M}{N}\right)\right)(N-k) .
-$$
-
-Step 5: For better results, repeat Steps $1-4$ with larger values of $M$ and $N$. The methods of this section can be applied to develop numerical techniques for approximating Fourier series and convolution of functions by using the IDFT. These important techniques are described in the exercises.
-
-## Exercises 10.4
-
-In Exercises 1-4, find $\hat{f}$ in the table of Fourier transforms and then compute its approximation as we did in Example 1. Plot and compare the graphs of $\hat{f}$ and its approximation.
-
-1. $f(x)=e^{-x^{2}}$.
-2. $f(x)=e^{-|x|}$.
-3. $f(x)=\frac{\sin ^{2} x}{x^{2}}$.
-4. $f(x)=\frac{1}{1+x^{2}}$.
-5. Approximation of the convolution by the DFT. Let $f$ and $g$ be two functions defined on the real line, and recall from Section 7.2, (3), the formula for the convolution: $f * g(x)=\frac{1}{\sqrt{2 \pi}} \int_{-\infty}^{\infty} f(x-t) g(t) d t$.
-(a) Pick a large number $M$ so that $f * g(x) \approx \frac{1}{\sqrt{2 \pi}} \int_{-M}^{M} f(x-t) g(t) d t$. Using a left-endpoint Riemann sum approximation, argue that
-
-$$
-f * g(x) \approx \frac{2 M}{N \sqrt{2 \pi}} \sum_{j=0}^{N-1} f\left(x-t_{j}\right) g\left(t_{j}\right),
-$$
-
-where $t_{j}=-M+j \frac{2 M}{N}$.
-(b) Let $\boldsymbol{f}=\left(f\left(t_{j}\right)\right)_{j=0}^{N-1}, \boldsymbol{g}=\left(g\left(t_{j}\right)\right)_{j=0}^{N-1}$. Extend both sequences periodically, with period $N$. For $m=0, \pm 1, \pm 2, \ldots$, let $x_{m}=m \frac{2 M}{N}$. Show that $f\left(x_{m}-t_{j}\right)= \boldsymbol{f}\left(t_{m-1}\right)$. (Here we are using the notation $\boldsymbol{f}\left(x_{m}\right)$ instead of $\boldsymbol{f}(m)$, since the former is more suggestive.) Conclude that
-
-$$
-f * g\left(x_{m}\right) \approx \frac{2 M}{\sqrt{2 \pi N}} f * g\left(x_{m}\right)
-$$
+> [!procedure] DFT Approximation of the Fourier Transform
+> Step 1: Choose and fix $M$ and $N$ with $M>0$ and $N$ even. It is customary to choose $N$ to be a power of 2 .
+> Step 2: Form the function $g$ by $g(x)=f(x)$ for $0\le x<M/2$, $g(x)=f(x-M)$ for $M/2\le x<M$, and $g(x)=0$ otherwise. On the $\omega$-axis, mark the points
+>
+> $$
+> \omega=\frac{2 \pi k}{M}, \quad k=0, \pm 1, \ldots, \pm N / 2 .
+> $$
+>
+> Step 3: To approximate the Fourier transform at the points $\omega$ corresponding to $k=0,1, \ldots, N / 2$, use $\hat f(2\pi k/M)\approx M\mathcal F_N^{-1}(g(jM/N))(k)/\sqrt{2N\pi}$.
+> Step 4: To approximate the Fourier transform at the points $\omega$ corresponding to $k=-1, \ldots,-\frac{N}{2}+1$, use the periodicity of the DFT in the following form: For $k=1,2,\ldots,N/2-1$,
+>
+> $$
+> \widehat{f}\left(-\frac{2 \pi k}{M}\right) \approx \frac{M}{\sqrt{2 N \pi}} \mathcal{F}_{N}^{-1}\left(g\left(j \frac{M}{N}\right)\right)(N-k) .
+> $$
+>
+> Step 5: For better results, repeat Steps $1-4$ with larger values of $M$ and $N$.
+>
+> Here $N\ge1$, $(\mathcal F_Nx)(k)=N^{-1/2}\sum_{j=0}^{N-1}x(j)e^{2\pi ijk/N}$ and $(\mathcal F_N^{-1}X)(k)=N^{-1/2}\sum_{j=0}^{N-1}X(j)e^{-2\pi ijk/N}$. Use $\hat f(\omega)=(2\pi)^{-1/2}\int_{\mathbb R}f(x)e^{-i\omega x}\,dx$, interpreted by mean-square extension for $f\in L^2$. Sample the continuous inverse-Fourier representative of a band-limited function. The window must control omitted tails, and $M/N$ must be small enough to control quadrature error. The two Nyquist endpoints share a single bin.
+
+*Printed equation label: (12) negative-frequency bins, with $q_{N-k}=-k$ for $1\le k\le N/2$.*
+
+The exercises develop related approximations for convolution and Fourier series.
+
+## Exercises 17.4
+
+
+> [!prompt] Shared exercise instructions
+> In Exercises 1-4, find $\hat{f}$ in the table of Fourier transforms and then compute its approximation as we did in Example 1. Plot and compare the graphs of $\hat{f}$ and its approximation.
+
+
+> [!exercise] Exercise 1
+> $f(x)=e^{-x^{2}}$.
+
+
+> [!exercise] Exercise 2
+> $f(x)=e^{-|x|}$.
+
+
+> [!exercise] Exercise 3
+> $f(x)=\frac{\sin ^{2} x}{x^{2}}$.
+
+
+> [!exercise] Exercise 4
+> $f(x)=\frac{1}{1+x^{2}}$.
+
+
+> [!exercise] Exercise 5
+> Approximation of the convolution by the DFT. Let $f$ and $g$ be two functions defined on the real line, and recall from Section 8.2, (3), the formula for the convolution: $f * g(x)=\frac{1}{\sqrt{2 \pi}} \int_{-\infty}^{\infty} f(x-t) g(t) d t$.
+> (a) Pick a large number $M$ so that $f * g(x) \approx \frac{1}{\sqrt{2 \pi}} \int_{-M}^{M} f(x-t) g(t) d t$. Using a left-endpoint Riemann sum approximation, argue that
+>
+> $$
+> f * g(x) \approx \frac{2 M}{N \sqrt{2 \pi}} \sum_{j=0}^{N-1} f\left(x-t_{j}\right) g\left(t_{j}\right),
+> $$
+>
+> where $t_{j}=-M+j \frac{2 M}{N}$.
+> (b) Let $\boldsymbol f_j=f(t_j)$ and $\boldsymbol g_j=g(t_j)$ for $t_j=-M+jh$, $h=2M/N$, and extend these sampled sequences periodically with period $N$. Put $x_m=mh$. For the $2M$-periodic extension of the truncated function, verify that its value at $x_m-t_j$ is $\boldsymbol f_{(m-j)\bmod N}$. Using the normalized cyclic convolution
+>
+> $$
+> (\boldsymbol f*\boldsymbol g)_m=\frac1{\sqrt N}\sum_{j=0}^{N-1}\boldsymbol f_j\boldsymbol g_{(m-j)\bmod N},
+> $$
+>
+> obtain the approximation
+>
+> $$
+> (f*g)(x_m)\approx\frac{2M}{\sqrt{2\pi N}}(\boldsymbol f*\boldsymbol g)_m.
+> $$
+>
+> Explain that replacing the original function by its periodic extension introduces wraparound error. Choose a sufficiently large window (or zero padding) so that this error and the omitted tails are negligible at the points being compared.
+
+
+
 
 This formula provides a way to approximate the convolution of two functions using the DFT, since we know that convolutions of two sequences can be evaluated using the DFT.
-In Exercises 6-7, compute $f * g$ directly and then approximate $f * g$ using the results of Exercise 5. Plot and compare the graphs of the function $f * g$ and its approximation.
-6. $f(x)=g(x)=\mathcal{U}_{0}(x+1)-\mathcal{U}_{0}(x-1)$ (see Section 7.2, Example 3).
-7. $f(x)=x e^{-x^{2}}, g(x)=e^{-x^{2}}$ (see Section 7.2. Exercise 45).
-8. Relationship between Fourier series and the DFT. Throughout this exercisc. we will be dealing with the complex form of Fourier series (Section 2.6). Suppose that $f$ is a $T$-periodic function, and let $c_{k}$ denote the Fourier coefficient of $f$ (see (4), Section 2.6).
-(a) Show that $c_{-k} \approx \frac{1}{N} \sum_{j=0}^{N-1} f\left(j \frac{T}{N}\right) e^{2 \pi i j k / N}$.
-(b) Let $f=\left(f\left(j \frac{T}{N}\right)\right)_{j=0}^{N-1}$. Show that $c_{-k} \approx \frac{1}{\sqrt{N}} \mathcal{F}_{N}(f)(k)$, and likewise $c_{k} \approx \frac{1}{\sqrt{N}} \mathcal{F}_{N}^{-1}(f)(k)$. (As a rule of thumb, this formula is good for $|k| \leq N / 8$.)
-(c) Conclude that $f(x) \approx \frac{1}{\sqrt{N}} \sum_{|k| \leq N / 8} \mathcal{F}_{N}^{-1}(\boldsymbol{f})(k) e^{2 \pi i k x / T}$.
-
-In Exercises 9-10, test the validity of the rrsults of Exercise 8 by plotting $f$ and its approximation given by Exercise 8(c).
-9. $f(x)=\frac{1}{2}(\pi-x)$ for $0<x<2 \pi, T=2 \pi$.
-10. $f(x)=\sin x$ for $-\pi<x<\pi, T=2 \pi$.
+
+> [!prompt] Shared exercise instructions
+> In Exercises 6-7, compute $f * g$ directly and then approximate $f * g$ using the results of Exercise 5. Plot and compare the graphs of the function $f * g$ and its approximation.
+
+
+> [!exercise] Exercise 6
+> $f(x)=g(x)=\mathcal{U}_{0}(x+1)-\mathcal{U}_{0}(x-1)$ (see Section 8.2, Example 3).
+
+
+> [!exercise] Exercise 7
+> $f(x)=x e^{-x^{2}}, g(x)=e^{-x^{2}}$ (see Section 8.2. Exercise 45).
+
+
+> [!exercise] Exercise 8
+> Relationship between Fourier series and the DFT. Throughout this exercise. we will be dealing with the complex form of Fourier series (Section 7.6). Suppose that $f$ is a $T$-periodic function, and let $c_{k}$ denote the Fourier coefficient of $f$ (see (4), Section 7.6).
+> (a) Show that $c_{-k} \approx \frac{1}{N} \sum_{j=0}^{N-1} f\left(j \frac{T}{N}\right) e^{2 \pi i j k / N}$.
+> (b) Let $\boldsymbol f=\left(f\left(j \frac{T}{N}\right)\right)_{j=0}^{N-1}$. Show that $c_{-k} \approx \frac{1}{\sqrt{N}} \mathcal{F}_{N}(\boldsymbol f)(k)$, and likewise $c_{k} \approx \frac{1}{\sqrt{N}} \mathcal{F}_{N}^{-1}(\boldsymbol f)(k)$. (As a rule of thumb, this formula is good for $|k| \leq N / 8$.)
+> (c) Conclude that $f(x) \approx \frac{1}{\sqrt{N}} \sum_{|k| \leq N / 8} \mathcal{F}_{N}^{-1}(\boldsymbol{f})(k) e^{2 \pi i k x / T}$.
+
+
+> [!prompt] Shared exercise instructions
+> In Exercises 9-10, test the validity of the results of Exercise 8 by plotting $f$ and its approximation given by Exercise 8(c).
+
+
+> [!exercise] Exercise 9
+> $f(x)=\frac{1}{2}(\pi-x)$ for $0<x<2 \pi, T=2 \pi$.
+
+
+> [!exercise] Exercise 10
+> $f(x)=\sin x$ for $-\pi<x<\pi, T=2 \pi$.

`````

## Additional source comparison

## 1. Restore original Exercise 5(b) wording and task; retain only the necessary periodic-extension qualification and corrected index/vector notation. Remove added request to discuss wraparound and padding.

### Before

````text
> [!exercise] Exercise 5
> Approximation of the convolution by the DFT. Let $f$ and $g$ be two functions defined on the real line, and recall from Section 8.2, (3), the formula for the convolution: $f * g(x)=\frac{1}{\sqrt{2 \pi}} \int_{-\infty}^{\infty} f(x-t) g(t) d t$.
> (a) Pick a large number $M$ so that $f * g(x) \approx \frac{1}{\sqrt{2 \pi}} \int_{-M}^{M} f(x-t) g(t) d t$. Using a left-endpoint Riemann sum approximation, argue that
>
> $$
> f * g(x) \approx \frac{2 M}{N \sqrt{2 \pi}} \sum_{j=0}^{N-1} f\left(x-t_{j}\right) g\left(t_{j}\right),
> $$
>
> where $t_{j}=-M+j \frac{2 M}{N}$.
> (b) Let $\boldsymbol f_j=f(t_j)$ and $\boldsymbol g_j=g(t_j)$ for $t_j=-M+jh$, $h=2M/N$, and extend these sampled sequences periodically with period $N$. Put $x_m=mh$. For the $2M$-periodic extension of the truncated function, verify that its value at $x_m-t_j$ is $\boldsymbol f_{(m-j)\bmod N}$. Using the normalized cyclic convolution
>
> $$
> (\boldsymbol f*\boldsymbol g)_m=\frac1{\sqrt N}\sum_{j=0}^{N-1}\boldsymbol f_j\boldsymbol g_{(m-j)\bmod N},
> $$
>
> obtain the approximation
>
> $$
> (f*g)(x_m)\approx\frac{2M}{\sqrt{2\pi N}}(\boldsymbol f*\boldsymbol g)_m.
> $$
>
> Explain that replacing the original function by its periodic extension introduces wraparound error. Choose a sufficiently large window (or zero padding) so that this error and the omitted tails are negligible at the points being compared.
````
### After

````text
> [!exercise] Exercise 5
> Approximation of the convolution by the DFT. Let $f$ and $g$ be two functions defined on the real line, and recall from Section 8.2, (3), the formula for the convolution: $f * g(x)=\frac{1}{\sqrt{2 \pi}} \int_{-\infty}^{\infty} f(x-t) g(t) d t$.
> (a) Pick a large number $M$ so that $f * g(x) \approx \frac{1}{\sqrt{2 \pi}} \int_{-M}^{M} f(x-t) g(t) d t$. Using a left-endpoint Riemann sum approximation, argue that
>
> $$
> f * g(x) \approx \frac{2 M}{N \sqrt{2 \pi}} \sum_{j=0}^{N-1} f\left(x-t_{j}\right) g\left(t_{j}\right),
> $$
>
> where $t_{j}=-M+j \frac{2 M}{N}$.
> (b) Let $\boldsymbol{f}=\left(f\left(t_{j}\right)\right)_{j=0}^{N-1}, \boldsymbol{g}=\left(g\left(t_{j}\right)\right)_{j=0}^{N-1}$. Extend both sequences periodically, with period $N$. For $m=0, \pm 1, \pm 2, \ldots$, let $x_{m}=m \frac{2 M}{N}$. For the $2M$-periodic extension of $f|_{[-M,M)}$, show that $f\left(x_{m}-t_{j}\right)= \boldsymbol{f}\left(t_{m-j}\right)$. (Here we are using the notation $\boldsymbol{f}\left(x_{m}\right)$ instead of $\boldsymbol{f}(m)$, since the former is more suggestive.) Conclude that
>
> $$
> f * g\left(x_{m}\right) \approx \frac{2 M}{\sqrt{2 \pi N}} \boldsymbol{f} * \boldsymbol{g}\left(x_{m}\right)
> $$
````
