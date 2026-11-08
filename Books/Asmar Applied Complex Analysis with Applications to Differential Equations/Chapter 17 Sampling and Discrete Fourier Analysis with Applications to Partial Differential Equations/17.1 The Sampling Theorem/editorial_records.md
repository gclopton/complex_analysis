
# Editorial records

Reading note: 17.1 The Sampling Theorem.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!definition|94784048-1192-5e9e-b02c-2d7eaca6456a.local at=f9ae5be4-de0f-5a32-a04e-92d01c8c3b79] Band-Limited Function and Angular-Frequency Bandwidth
> Use the unitary angular-frequency Fourier transform $\widehat f(\omega)=(2\pi)^{-1/2}\int_{\mathbb R}f(x)e^{-i\omega x}\,dx$, interpreted by its $L^2$ extension when necessary. A function $f\in L^2(\mathbb R)$ is band-limited if $\widehat f=0$ almost everywhere outside a bounded interval. Any $W>0$ such that $\widehat f(\omega)=0$ for almost every $|\omega|>W$ is a bandwidth in this centered angular-frequency convention. For sampling, use the continuous representative given by Fourier inversion.
````
### After

````text
> [!definition|94784048-1192-5e9e-b02c-2d7eaca6456a.local at=f9ae5be4-de0f-5a32-a04e-92d01c8c3b79] Band Limited Functions
> A square integrable function $f(x)$ is called band limited if its Fourier transform $\widehat{f}$ vanishes almost everywhere outside a finite interval. In this case, there is a positive number $W$ such that $\widehat{f}(\omega)=0$ for almost all $|\omega|>W$. Any such number $W$ is called a band width of $f$.
>
> Use $\hat f(\omega)=(2\pi)^{-1/2}\int_{\mathbb R}f(x)e^{-i\omega x}\,dx$, interpreted by mean-square extension for $f\in L^2$. Sample the continuous inverse-Fourier representative of a band-limited function.
````

## 2. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|93e36581-6bd4-580b-893f-5867d2ff424e.local at=f9baee9f-8a8a-50e7-8fd6-9f6fc239de92] Bandwidth under Linear Combination, Translation, and Convolution
> Use the unitary angular-frequency Fourier transform $\widehat f(\omega)=(2\pi)^{-1/2}\int_{\mathbb R}f(x)e^{-i\omega x}\,dx$, interpreted by its $L^2$ extension when necessary.
>
> Let $f,g\in L^2(\mathbb R)$ be band-limited with bandwidths $W_1,W_2$ and let $a,b\in\mathbb C$.
>
> (a) $af+bg$ has bandwidth at most $\max(W_1,W_2)$.
> (b) For real $c$, $f(x-c)$ has the same admissible bandwidth $W_1$.
> (c) If $f$ has bandwidth $W_1$ and $g\in L^1(\mathbb R)$, their normalized convolution
>
> $$
> (f*g)(x)=\frac1{\sqrt{2\pi}}\int_{\mathbb R}f(x-t)g(t)\,dt
> $$
>
> belongs to $L^2$ and has bandwidth at most $W_1$. The analogous statement holds with the two factors interchanged.
````
### After

````text
> [!theorem|93e36581-6bd4-580b-893f-5867d2ff424e.local at=f9baee9f-8a8a-50e7-8fd6-9f6fc239de92] Properties of Band Limited Functions
> Suppose that $a, b$ are constants and $f, g$ are functions.
> (a) If $f$ and $g$ are band limited with band widths $W_{1}$ and $W_{2}$, respectively, then $a f+b g$ is band limited with band width $W$ smaller than or equal to the larger of $W_{1}$ and $W_{2}$.
> (b) If $f$ is band limited with band width $W$, then the translate of $f$ by $a$, $f(x-a)$, is also band limited with band width $W$.
> (c) If either $f$ or $g$ is band limited with band width $W$, and the other factor is integrable, then the convolution $f * g$ is also band limited with band width $W$.
>
> Use $\hat f(\omega)=(2\pi)^{-1/2}\int_{\mathbb R}f(x)e^{-i\omega x}\,dx$, interpreted by mean-square extension for $f\in L^2$. Sample the continuous inverse-Fourier representative of a band-limited function. The band-limited factors are square integrable, and $(f*g)(x)=(2\pi)^{-1/2}\int f(x-t)g(t)\,dt$.
````

## 3. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|4c40236c-e418-5e99-be39-e1e862ca0aef.local at=611d5282-f241-5d09-a91b-d1153d1fb2c6] Shannon Sampling Theorem for Square-Integrable Band-Limited Functions
> Use the unitary angular-frequency Fourier transform $\widehat f(\omega)=(2\pi)^{-1/2}\int_{\mathbb R}f(x)e^{-i\omega x}\,dx$, interpreted by its $L^2$ extension when necessary.
>
> Let $W>0$ and let $f\in L^2(\mathbb R)$ have Fourier transform supported almost everywhere in $[-W,W]$. Take its continuous inverse-Fourier representative. Then
>
> $$
> f(x)=\sum_{n\in\mathbb Z}f\left(\frac{n\pi}{W}\right)\frac{\sin(Wx-n\pi)}{Wx-n\pi},\qquad x\in\mathbb R,
> $$
>
> where $\sin t/t$ is assigned its limiting value one at $t=0$. Symmetric partial sums converge in $L^2(\mathbb R)$ and uniformly on $\mathbb R$. Thus the samples at spacing $\pi/W$ determine $f$ uniquely in this class.
````
### After

````text
> [!theorem|4c40236c-e418-5e99-be39-e1e862ca0aef.local at=611d5282-f241-5d09-a91b-d1153d1fb2c6] Sampling Theorem for Band Limited Functions
> Suppose that $f\in L^2(\mathbb R)$ is band limited with band width $W>0$. Then for all $x$ we have
>
> $$
> f(x)=\sum_{n\in\mathbb Z}f\left(\frac{n\pi}{W}\right)\frac{\sin(Wx-n\pi)}{Wx-n\pi},\qquad x\in\mathbb R,
> $$
>
> Thus $f$ can be constructed completely from its sample values $f(n\pi/W)$, $n=0,\pm1,\pm2,\ldots$.
>
> Use $\hat f(\omega)=(2\pi)^{-1/2}\int_{\mathbb R}f(x)e^{-i\omega x}\,dx$, interpreted by mean-square extension for $f\in L^2$. Sample the continuous inverse-Fourier representative of a band-limited function. Removable sinc quotients take their limiting value one.
````

## 4. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|0ba04e44-1ab8-5055-833d-981e6b78ac38.local at=fd80a014-c3b6-5572-820f-05ea40b5203e] Sinc Reconstruction of the Fourier Transform of a Time-Limited Function
> Use the unitary angular-frequency Fourier transform $\widehat f(\omega)=(2\pi)^{-1/2}\int_{\mathbb R}f(x)e^{-i\omega x}\,dx$, interpreted by its $L^2$ extension when necessary.
>
> If $T>0$ and $f\in L^2(\mathbb R)$ vanishes almost everywhere outside $[-T,T]$, then its continuous Fourier transform satisfies
>
> $$
> \widehat f(\omega)=\sum_{n\in\mathbb Z}\widehat f\left(\frac{n\pi}{T}\right)\frac{\sin(T\omega-n\pi)}{T\omega-n\pi}.
> $$
>
> Use the limiting value one for each removable sinc quotient. Symmetric partial sums converge in $L^2$ and uniformly; samples at spacing $\pi/T$ determine the transform.
````
### After

````text
> [!theorem|0ba04e44-1ab8-5055-833d-981e6b78ac38.local at=fd80a014-c3b6-5572-820f-05ea40b5203e] Sinc Reconstruction of the Fourier Transform of a Time-Limited Function
> For $T>0$ and $f\in L^2(\mathbb R)$, suppose that $f(t)=0$ for all $|t|>T$. Then for all $\omega$ we have
>
> $$
> \hat{f}(\omega)=\sum_{n=-\infty}^{\infty} \hat{f}\left(\frac{n \pi}{T}\right) \frac{\sin (T \omega-n \pi)}{(T \omega-n \pi)} .
> $$
>
> Thus $\widehat{f}$ is completely determined by sampling at the points $\frac{n \pi}{T} . n= 0, \pm 1, \pm 2, \ldots$.
>
> Use $\hat f(\omega)=(2\pi)^{-1/2}\int_{\mathbb R}f(x)e^{-i\omega x}\,dx$, interpreted by mean-square extension for $f\in L^2$. Sample the continuous inverse-Fourier representative of a band-limited function.
````

## 5. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|28e15c10-8e5e-5408-9023-68331e83e99d.local at=4cab5303-52d5-57aa-9fab-a568e58418c6] Fourier Transform from Uniform Samples of a Band-Limited Function
> Use the unitary angular-frequency Fourier transform $\widehat f(\omega)=(2\pi)^{-1/2}\int_{\mathbb R}f(x)e^{-i\omega x}\,dx$, interpreted by its $L^2$ extension when necessary. Let $f\in L^2(\mathbb R)$ have spectrum supported in $[-W,W]$, $W>0$, and take its continuous representative. Let $\chi_{[-W,W]}$ denote the indicator of that frequency interval; endpoint values do not affect the $L^2$ transform.
>
> $$
> \widehat f(\omega)=\frac1W\sqrt{\frac\pi2}\,\chi_{[-W,W]}(\omega)\sum_{n\in\mathbb Z}f\left(\frac{n\pi}{W}\right)e^{-in\pi\omega/W}.
> $$
>
> The series converges in $L^2([-W,W])$. Additional regularity supplies the usual pointwise Fourier-series conclusions.
````
### After

````text
> [!theorem|28e15c10-8e5e-5408-9023-68331e83e99d.local at=4cab5303-52d5-57aa-9fab-a568e58418c6] Fourier Transform Using Sampling
> Suppose that $f\in L^2(\mathbb R)$ is band limited with band width $W>0$. Then
>
> $$
> \widehat f(\omega)=\frac1W\sqrt{\frac\pi2}\,\left(\mathcal U_0(\omega+W)-\mathcal U_0(\omega-W)\right)\sum_{n\in\mathbb Z}f\left(\frac{n\pi}{W}\right)e^{-in\pi\omega/W}.
> $$
>
> Use $\hat f(\omega)=(2\pi)^{-1/2}\int_{\mathbb R}f(x)e^{-i\omega x}\,dx$, interpreted by mean-square extension for $f\in L^2$. Sample the continuous inverse-Fourier representative of a band-limited function. Here $\mathcal U_0(\omega)=1$ for $\omega>0$ and zero otherwise. The series equality is in mean square; endpoint values do not affect the transform.
````

## 6. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|7cd918f2-1c69-5f69-b560-22cbaa862aba.local at=0b2c5c7b-2101-5733-961a-862277cca5ae] Cosine-Series Reconstruction of the Fourier Transform from Even Band-Limited Samples
> Use the unitary angular-frequency Fourier transform $\widehat f(\omega)=(2\pi)^{-1/2}\int_{\mathbb R}f(x)e^{-i\omega x}\,dx$, interpreted by its $L^2$ extension when necessary. Let $f\in L^2(\mathbb R)$ have spectrum supported in $[-W,W]$, $W>0$, and take its continuous representative. Let $\chi_{[-W,W]}$ denote the indicator of that frequency interval; endpoint values do not affect the $L^2$ transform. Assume also that $f(-x)=f(x)$. Then, with convergence in $L^2([-W,W])$,
>
> $$
> \widehat f(\omega)=\frac1W\sqrt{\frac\pi2}\,\chi_{[-W,W]}(\omega)\left[f(0)+2\sum_{n=1}^\infty f\left(\frac{n\pi}{W}\right)\cos\left(\frac{n\pi\omega}{W}\right)\right].
> $$
````
### After

````text
> [!theorem|7cd918f2-1c69-5f69-b560-22cbaa862aba.local at=0b2c5c7b-2101-5733-961a-862277cca5ae] Fourier Transforms of Even Functions Using Sampling
> Suppose that $f\in L^2(\mathbb R)$ is even and band limited with band width $W>0$. Then
>
> $$
> \widehat f(\omega)=\frac1W\sqrt{\frac\pi2}\,\left(\mathcal U_0(\omega+W)-\mathcal U_0(\omega-W)\right)\left[f(0)+2\sum_{n=1}^\infty f\left(\frac{n\pi}{W}\right)\cos\left(\frac{n\pi\omega}{W}\right)\right].
> $$
>
> Use $\hat f(\omega)=(2\pi)^{-1/2}\int_{\mathbb R}f(x)e^{-i\omega x}\,dx$, interpreted by mean-square extension for $f\in L^2$. Sample the continuous inverse-Fourier representative of a band-limited function. Here $\mathcal U_0(\omega)=1$ for $\omega>0$ and zero otherwise. The series equality is in mean square; endpoint values do not affect the transform.
````

## 7. Move correction/commentary into the separate editorial record; keep the actual correction in the reading text.

### Before

````text
[Source correction: the ± signs in the Exercise 3 sample headings are inconsistent with its translated function. The listed values match the positive sample points only; the headings below are corrected.]
````
### After

````text

````

## Source-to-current comparison

Source: /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 17 Sampling and Discrete Fourier Analysis with Applications to Partial Differential Equations/17.1 The Sampling Theorem.md

This exact comparison preserves the full change evidence, including formatting, OCR corrections, restored source wording, and required standalone context. The entries above explain the recovery edits. The comparison is not a claim that every difference is a correction; component serialization, callout wrapping, and printed labels outside callouts are formatting.

`````diff
--- /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 17 Sampling and Discrete Fourier Analysis with Applications to Partial Differential Equations/17.1 The Sampling Theorem.md
+++ /Users/gradyclopton/ObsidianVaults/complex_analysis/Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 17 Sampling and Discrete Fourier Analysis with Applications to Partial Differential Equations/17.1 The Sampling Theorem.md
@@ -1,6 +1,7 @@
+
 ## Topics to Review
 
-This chapter contains numerical techniques for computing the Fourier transform and Fourier series, and for solving boundary value problems. Sections 17.1 and 17.2 deal with the sampling theorem and some of its applications. They are not required for the rest of the chapter. In Section 17.3 we present the discrete and fast Fourier transforms. In stadying this section, it will help to keep in mind the basic properties of the Fourier transform as presented in Section 7.2. Similar properties will be established for the discrete Fourier transform. In Section 17.4 we show a connection between the Fourier transform and the discrete Fourier transform. To appreciate this connection, you need to do the exercises of Section 17.4 which deal with the topies of Sections 7.4 and 7.5.
+This chapter contains numerical techniques for computing the Fourier transform and Fourier series, and for solving boundary value problems. Sections 17.1 and 17.2 deal with the sampling theorem and some of its applications. They are not required for the rest of the chapter. In Section 17.3 we present the discrete and fast Fourier transforms. In studying this section, it will help to keep in mind the basic properties of the Fourier transform as presented in Section 8.2. Similar properties will be established for the discrete Fourier transform. In Section 17.4 we show a connection between the Fourier transform and the discrete Fourier transform. To appreciate this connection, you need to do the exercises of Section 17.4 which deal with the topics of Sections 8.4 and 8.5.
 
 ## Looking Ahead...
 
@@ -15,7 +16,7 @@
 
 By now it is clear that the Fourier transform and Fourier series are essential tools in applications. To analyze a function with these tools requires knowledge of the function over a whole interval. In real-world applications, functions are measured over discrete sets of values, and hence they are usually given as sequences of values. To analyze these discrete functions, we will introduce and use the discrete Fourier transform. Among other important applications of the discrete Fourier transform, we will show how we can use it to approximate Fourier transforms and solve boundary value problems.
 
-The discrete Fourier transform became widely used in the 1960s after the discovery of a numerical algorithm that gives a fast and efficient method for computing it. This algorithm is known as the fast Fourier transform. The ideas behind it date back to Gauss. But it was Cooley and Tukey who emphasized its significance to computerbased Fourier analysis.
+The discrete Fourier transform became widely used in the 1960s after the discovery of a numerical algorithm that gives a fast and efficient method for computing it. This algorithm is known as the fast Fourier transform. The ideas behind it date back to Gauss. But it was Cooley and Tukey who emphasized its significance to computer-based Fourier analysis.
 
 Another topic covered in this chapter is the sampling theorem. This important result was discovered by the American engineer Claude Shannon in the 1940s. It has numerous applications to transmission and information theory.
 
@@ -24,22 +25,29 @@
 The sampling theorem is a striking result that states that certain functions can be reconstructed completely from a discrete set of measurements or samples taken at equal intervals. This very important result has many interesting applications, some of which will be discussed in the following section. Let us recall the definition of the Fourier transform
 
 $$
-\widehat{f}(\omega)=\frac{1}{\sqrt{2 \pi}} \int_{-\infty}^{x} f(x) e^{-i \omega x} d x, \quad-\infty<\omega<\infty
+\widehat{f}(\omega)=\frac{1}{\sqrt{2 \pi}} \int_{-\infty}^{\infty}f(x) e^{-i \omega x} d x, \quad-\infty<\omega<\infty
+\tag{1}
 $$
 
 We now define a class of functions by a property of the Fourier transform.
 
-BAND LIMITED FUNCTIONS
-
-It is important to note that only $\widehat{f}$ is required to vanish outside a finite interval and not $f$. Indeed, it can be shown that $f$ and $\widehat{f}$ cannot both vanish off a finite interval.
-
-A function $f(x)$ is called band limited if its Fourier transform $\widehat{f}$ vanishes outside a finite interval. In this case, there is a positive number $W$ such that $\widehat{f}(\omega)=0$ for all $|\omega|>W$. Any such number $W$ is called a band width of $f$.
+It is important to note that only $\widehat{f}$ is required to vanish outside a finite interval and not $f$. For a nonzero square-integrable function, $f$ and $\widehat f$ cannot both vanish outside finite intervals.
+
+> [!definition|94784048-1192-5e9e-b02c-2d7eaca6456a.local at=f9ae5be4-de0f-5a32-a04e-92d01c8c3b79] Band Limited Functions
+> A square integrable function $f(x)$ is called band limited if its Fourier transform $\widehat{f}$ vanishes almost everywhere outside a finite interval. In this case, there is a positive number $W$ such that $\widehat{f}(\omega)=0$ for almost all $|\omega|>W$. Any such number $W$ is called a band width of $f$.
+>
+> Use $\hat f(\omega)=(2\pi)^{-1/2}\int_{\mathbb R}f(x)e^{-i\omega x}\,dx$, interpreted by mean-square extension for $f\in L^2$. Sample the continuous inverse-Fourier representative of a band-limited function.
 
 Although "most" functions are not band limited, we can show that at least all the functions that we have dealt with in this text can be approximated as closely as we want by band limited functions (see Exercises 7 and 8). This makes the class of band limited functions very useful in applications.
 
 We have encountered many band limited functions before. Here is a simple example that will play an important role in our development.
 
-## EXAMPLE 1 A band limited function
+> [!exercise|22544709-2901-5577-9d5b-809e236ac15b.local at=376a06dd-7ef2-5024-9e80-e9432713502f] EXAMPLE 1 A band limited function
+> Find the Fourier transforms and bandwidths of (a) $s(x)=\sin x/x$ and (b) $s_W(x)=\sin(Wx)/(Wx)$ for $W>0$, defining both functions to equal one at the origin.
+
+
+
+##### solution
 
 (a) The function $s(x)=\frac{\sin x}{x}$ is shown in Figure 1. From the table of Fourier transforms, we find that
 
@@ -49,87 +57,170 @@
 
 Since $\widehat{s}$ vanishes for all $|\omega|>1$, we conclude that $s$ is band limited with band width 1 (see Figure 2).
 
-![](./images/e0b9cf26-d77c-487a-ae6f-e9bad0026586-02_409_597_1683_509.jpg)
-Figure 1 The function $\frac{\sin x}{x}$ is band limited with band width 1.
-
-![](./images/e0b9cf26-d77c-487a-ae6f-e9bad0026586-02_415_622_1682_1147.jpg)
-Figure 2 The Fourier transform of $\frac{\sin x}{x}$ vanishes for all $|\omega|>1$.
+```scientific-figure
+id: a4b9e3b9-bd90-44c1-8c38-8c69de3d90e8
+numbered: false
+title: ""
+caption: Figure 1 The function $\frac{\sin x}{x}$ is band limited with band width 1.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 17 Sampling and Discrete Fourier Analysis with Applications to Partial Differential Equations/images/e0b9cf26-d77c-487a-ae6f-e9bad0026586-02_409_597_1683_509.jpg
+    caption: ""
+```
+
+
+```scientific-figure
+id: f155ee32-b6c8-4d9b-bb3b-38366443c4f1
+numbered: false
+title: ""
+caption: Figure 2 The Fourier transform of $\frac{\sin x}{x}$ vanishes for all $|\omega|>1$.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 17 Sampling and Discrete Fourier Analysis with Applications to Partial Differential Equations/images/e0b9cf26-d77c-487a-ae6f-e9bad0026586-02_415_622_1682_1147.jpg
+    caption: ""
+```
+
 
 As $W$ increases, the frequency of $\sin W x$ increases, and this causes the graph of $\frac{\sin W x}{W x}$ to be more wavy and more squished toward the origin (Figure 3). On the Fourier transform side, increasing $W$ has the opposite effect of spreading or stretching the graph.
 
-THEOREM 1
-PROPERTIES OF BAND LIMITED FUNCTIONS
-
-![](./images/e0b9cf26-d77c-487a-ae6f-e9bad0026586-03_465_580_701_597.jpg)
-Figure 3
-
-![](./images/e0b9cf26-d77c-487a-ae6f-e9bad0026586-03_417_644_749_1190.jpg)
-Figure 4
-
-(b) Let $W>0$ and consider the function $s_{W}(x)=\frac{\sin W x}{W x}$, which is shown in Figure 3 for various values of $W$. Wo have $s_{W}(x)=s(W x)$, hence $s_{W}$ is a dilate of the function $s$. Again, from the table of Fourier transforms, we find that
-
-$$
-\widehat{S_{W}}\left(\omega^{\prime}\right)= \begin{cases}\sqrt{\frac{\pi}{2}} \frac{1}{W} & \text { if }|\omega|<W \\ \frac{1}{2 W} \sqrt{\frac{\pi}{2}} & \text { if } \omega= \pm W \\ 0 & \text { if }|\omega|>W\end{cases}
-$$
-
-Since $\widehat{s_{W}}$ vanishes for all $|\omega|>W$, we conclude that $s_{W}$ is band limited with band width W (see Figure 1).
+```scientific-figure
+id: 2a8cfedc-7999-4f10-b384-0277cfaae827
+numbered: false
+title: ""
+caption: Figure 3
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 17 Sampling and Discrete Fourier Analysis with Applications to Partial Differential Equations/images/e0b9cf26-d77c-487a-ae6f-e9bad0026586-03_465_580_701_597.jpg
+    caption: ""
+```
+
+
+```scientific-figure
+id: 5aa3d911-2ae1-4cae-b230-89bf3f466379
+numbered: false
+title: ""
+caption: Figure 4
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 17 Sampling and Discrete Fourier Analysis with Applications to Partial Differential Equations/images/e0b9cf26-d77c-487a-ae6f-e9bad0026586-03_417_644_749_1190.jpg
+    caption: ""
+```
+
+
+(b) Let $W>0$ and consider the function $s_{W}(x)=\frac{\sin W x}{W x}$, which is shown in Figure 3 for various values of $W$. We have $s_{W}(x)=s(W x)$, hence $s_{W}$ is a dilate of the function $s$. Again, from the table of Fourier transforms, we find that
+
+$$
+\widehat{s_W}(\omega)= \begin{cases}\sqrt{\frac{\pi}{2}} \frac{1}{W} & \text { if }|\omega|<W \\ \frac{1}{2 W} \sqrt{\frac{\pi}{2}} & \text { if } \omega= \pm W \\ 0 & \text { if }|\omega|>W\end{cases}
+$$
+
+Since $\widehat{s_{W}}$ vanishes for all $|\omega|>W$, we conclude that $s_{W}$ is band limited with band width $W$ (see Figure 4).
 
 We now list some basic properties of band limited functions that will be useful in building more interesting examples.
 
-Suppose that $a, b$ are constants and $f, g$ are functions.
-(a) If $f$ and $g$ are band limited with band widths $W_{1}$ and $W_{2}$, respectively, then $a f+b y$ is band limited with band width $W$ smaller than or equal to the larger of $W_{1}$ and $W_{2}$.
-(b) If $f$ is band limited with band width $W$, then the translate of $f$ by $a$, $f(x-a)$, is also band limited with band width $W$.
-(c) If either $f$ or $g$ is band limited with band width W , then the convolution $f * g$ is also band limited with band width $W$.
+> [!theorem|93e36581-6bd4-580b-893f-5867d2ff424e.local at=f9baee9f-8a8a-50e7-8fd6-9f6fc239de92] Properties of Band Limited Functions
+> Suppose that $a, b$ are constants and $f, g$ are functions.
+> (a) If $f$ and $g$ are band limited with band widths $W_{1}$ and $W_{2}$, respectively, then $a f+b g$ is band limited with band width $W$ smaller than or equal to the larger of $W_{1}$ and $W_{2}$.
+> (b) If $f$ is band limited with band width $W$, then the translate of $f$ by $a$, $f(x-a)$, is also band limited with band width $W$.
+> (c) If either $f$ or $g$ is band limited with band width $W$, and the other factor is integrable, then the convolution $f * g$ is also band limited with band width $W$.
+>
+> Use $\hat f(\omega)=(2\pi)^{-1/2}\int_{\mathbb R}f(x)e^{-i\omega x}\,dx$, interpreted by mean-square extension for $f\in L^2$. Sample the continuous inverse-Fourier representative of a band-limited function. The band-limited factors are square integrable, and $(f*g)(x)=(2\pi)^{-1/2}\int f(x-t)g(t)\,dt$.
+
 Proof Part (a) is straightforward and is left as an exercise. To prove (b), we simply recall that
 
 $$
 \mathcal{F}(f(x-a))(\omega)=e^{-i a \omega} \widehat{f}(\omega)
 $$
 
-So, if $\hat{f}$ vanishes for $|\omega|>W$, then clearly the Fourier transform of $f(x-a)$ vanishes for $|\omega|>W$. Finally, (c) is an immediate consequence of the fact that $\widehat{f * g}=\widehat{f g}$.
+So, if $\hat{f}$ vanishes for $|\omega|>W$, then clearly the Fourier transform of $f(x-a)$ vanishes for $|\omega|>W$. Finally, (c) is an immediate consequence of the fact that $\widehat{f*g}=\widehat f\,\widehat g$.
 
 Recall that the function $s_{W}$ of Example 1 (b) is band limited with band
 width $W$. Shifting this function by $n \pi / W$ yields
 
 $$
 s_{W}\left(x-\frac{n \pi}{W}\right)=\frac{\sin (W x-n \pi)}{(W x-n \pi)} .
+\tag{2}
 $$
 
 which is also band limited with band width $W$, by Theorem 1(b). Also, by Theorem 1(a), any linear combination of functions of the form (2) is also band limited with band width $W$. The powerful result that we are about to state tells us that a converse of sorts is also true. That is, every band limited function with band width $W$ can be written as an infinite sum of functions of the form (2). Moreover, the coefficients in this sum are precisely the values of the function at an evenly spaced discrete set of sample points.
 
-THEOREM 2 SAMPLING THEOREM FOR BAND LIMITED FUNCTIONS
-
-Suppose that $f$ is band limited with band width $W$. Then for all $x$ we have
-
-Thus $f$ can be constructed completely from its sample values $f\left(\frac{n \pi}{W}\right), n= 0 . \pm 1 . \pm 2, \ldots$.
-
-If $W$ and $W^{\prime}$ are two band widths of $f$ with $W^{\prime}>W$, then the series corresponding to $W^{\prime}$ requires more sample points per unit length than the one for $W$, since $\frac{\pi}{W^{\prime}}>\frac{\pi}{W^{\prime}}$. The least number of sample points per unit length that is required for (3) to hold is called the Nyquist sampling rate and corresponds to the least band width of $f$.
+> [!theorem|4c40236c-e418-5e99-be39-e1e862ca0aef.local at=611d5282-f241-5d09-a91b-d1153d1fb2c6] Sampling Theorem for Band Limited Functions
+> Suppose that $f\in L^2(\mathbb R)$ is band limited with band width $W>0$. Then for all $x$ we have
+>
+> $$
+> f(x)=\sum_{n\in\mathbb Z}f\left(\frac{n\pi}{W}\right)\frac{\sin(Wx-n\pi)}{Wx-n\pi},\qquad x\in\mathbb R,
+> $$
+>
+> Thus $f$ can be constructed completely from its sample values $f(n\pi/W)$, $n=0,\pm1,\pm2,\ldots$.
+>
+> Use $\hat f(\omega)=(2\pi)^{-1/2}\int_{\mathbb R}f(x)e^{-i\omega x}\,dx$, interpreted by mean-square extension for $f\in L^2$. Sample the continuous inverse-Fourier representative of a band-limited function. Removable sinc quotients take their limiting value one.
+
+*Printed equation label: (3).*
+
+If $W$ and $W^{\prime}$ are two band widths of $f$ with $W^{\prime}>W$, then the series corresponding to $W^{\prime}$ requires more sample points per unit length than the one for $W$, since $\frac{\pi}{W}>\frac{\pi}{W^{\prime}}$. The least number of sample points per unit length that is required for (3) to hold is called the Nyquist sampling rate and corresponds to the least bandwidth of $f$: $W/\pi$ samples per unit length, when angular frequencies lie in $[-W,W]$.
 
 The proof of Theorem 2 is presented in the appendix at the end of this section. By reversing the roles of the function and its Fourier transform in the sampling theorem, we obtain a sampling theorem for time-limited functions. These are functions vanishing outside a finite interval. The precise statement follows. The proof can be reconstructed from that of the sampling theorem by interchanging $f$ and $\widehat{f}$.
 
-Suppose that $f(t)=0$ for all $|t|>T$. Then for all $\omega$ we have
-
-$$
-\hat{f}(\omega)=\sum_{n=-\infty}^{\infty} \hat{f}\left(\frac{n \pi}{T}\right) \frac{\sin (T \omega-n \pi)}{(T \omega-n \pi)} .
-$$
-
-Thus $\widehat{f}$ is completely determined by sampling at the points $\frac{n \pi}{T} . n= 0, \pm 1, \pm 2, \ldots$.
+> [!theorem|0ba04e44-1ab8-5055-833d-981e6b78ac38.local at=fd80a014-c3b6-5572-820f-05ea40b5203e] Sinc Reconstruction of the Fourier Transform of a Time-Limited Function
+> For $T>0$ and $f\in L^2(\mathbb R)$, suppose that $f(t)=0$ for all $|t|>T$. Then for all $\omega$ we have
+>
+> $$
+> \hat{f}(\omega)=\sum_{n=-\infty}^{\infty} \hat{f}\left(\frac{n \pi}{T}\right) \frac{\sin (T \omega-n \pi)}{(T \omega-n \pi)} .
+> $$
+>
+> Thus $\widehat{f}$ is completely determined by sampling at the points $\frac{n \pi}{T} . n= 0, \pm 1, \pm 2, \ldots$.
+>
+> Use $\hat f(\omega)=(2\pi)^{-1/2}\int_{\mathbb R}f(x)e^{-i\omega x}\,dx$, interpreted by mean-square extension for $f\in L^2$. Sample the continuous inverse-Fourier representative of a band-limited function.
+
+*Printed equation label: (4).*
 
 In the following example we show how to approximate a band limited function using the sampling theorem.
 
-## EXAMPLE 2 Sampling of a band limited function
-
-The initial temperature distribution of a bar, $f(x)(-\infty<x<\infty)$, has band width $W=2$. Some of its values are shown in Table 1.
-
-| $x$ | 0 | $\pi / 2$ | $\pi$ | $3 \pi / 2$ | $2 \pi$ | $5 \pi / 2$ |
-| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
-| $f(x)$ | .001765 | .382839 | .792567 | .266685 | .0014741 | .03319 |
-
-Table 1
-
-Using the sampling theorem, approximate the initial heat distribution at the points .1, .2, . 8 .
-
-Solution Since $f(x)$ is band limited with band width 2 , we can reconstruct it using (3), by sampling at the points $x=\frac{n \pi}{2}$. Using the values in Table 1, we obtain
+> [!exercise|cfd5e501-4dae-54b5-8502-4046ada0af4b.local at=88a6117d-0f10-568e-845c-3ec4643e4002] EXAMPLE 2 Sampling of a band limited function
+> The initial temperature distribution of a bar, $f(x)(-\infty<x<\infty)$, has band width $W=2$. Some of its values are shown in Table 1.
+>
+>
+>
+>
+> Using the sampling theorem, approximate the initial heat distribution at the points .1, .2, and .8 .
+
+```scientific-table
+id: de3c20ab-7700-47de-862b-bc69ce5cbe40
+numbered: false
+title: ""
+caption: Table 1
+captionVisible: true
+captionPosition: below
+rows:
+  - - text: $x$
+    - text: "0"
+    - text: $\pi / 2$
+    - text: $\pi$
+    - text: $3 \pi / 2$
+    - text: $2 \pi$
+    - text: $5 \pi / 2$
+  - - text: $f(x)$
+    - text: ".001765"
+    - text: ".382839"
+    - text: ".792567"
+    - text: ".266685"
+    - text: ".0014741"
+    - text: ".03319"
+headerRows: 1
+rowHeaders: true
+style: scientific
+```
+
+##### solution
+
+Since $f(x)$ is band limited with band width 2 , we can reconstruct it using (3), by sampling at the points $x=\frac{n \pi}{2}$. Using the values in Table 1, we obtain
 
 $$
 \begin{aligned}
@@ -147,21 +238,42 @@
 
 The graph of $f^{*}$, the partial sum approximation of $f$, is shown in Figure 5. For comparison's sake, we have also plotted the function $f$ which was used to generate the values in Table 1. (Of course, in real-life applications $f$ is unknown, except for its sampled values.)
 
-Figure 5 Approximation of a band limited function using sample points. We have a better approximation over the interval where the sample points were chosen.
-![](./images/e0b9cf26-d77c-487a-ae6f-e9bad0026586-05_511_602_1385_608.jpg)
-
-![](./images/e0b9cf26-d77c-487a-ae6f-e9bad0026586-05_515_595_1385_1241.jpg)
+```scientific-figure
+id: a6c15382-d042-4a5a-b70d-f1314b427640
+numbered: false
+title: ""
+caption: Figure 5 Approximation of a band limited function using sample points. We have a better approximation over the interval where the sample points were chosen.
+captionVisible: true
+captionPosition: below
+columns: 2
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 17 Sampling and Discrete Fourier Analysis with Applications to Partial Differential Equations/images/e0b9cf26-d77c-487a-ae6f-e9bad0026586-05_511_602_1385_608.jpg
+    caption: ""
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 17 Sampling and Discrete Fourier Analysis with Applications to Partial Differential Equations/images/e0b9cf26-d77c-487a-ae6f-e9bad0026586-05_515_595_1385_1241.jpg
+    caption: ""
+```
+
+
 
 Figure 5(b) shows that the approximation of $f$ by its partial sum is much better on the interval $x>0$ compared to the interval $x<0$. This is to be expected, since all the sample points were chosen from the interval $x \geq 0$.
 
-In the remainder of this section we apply the sampling theorem to compute Fourier transforms of band limited functions, by using only sampled
-
-![](./images/e0b9cf26-d77c-487a-ae6f-e9bad0026586-06_375_452_234_33.jpg)
-Figure 6
-
-# THEOREM 4 FOURIER TRANSFORM USING SAMPLING 
-
-values. Before we state the theorem, we recall the Heaviside step function
+In the remainder of this section we apply the sampling theorem to compute Fourier transforms of band limited functions, by using only sampled values.
+
+```scientific-figure
+id: 9fdeb021-5ae3-47f7-878c-9fc7910d3b74
+numbered: false
+title: ""
+caption: Figure 6
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 17 Sampling and Discrete Fourier Analysis with Applications to Partial Differential Equations/images/e0b9cf26-d77c-487a-ae6f-e9bad0026586-06_375_452_234_33.jpg
+    caption: ""
+```
+
+
+Before we state the theorem, we recall the Heaviside step function
 
 $$
 \mathcal{U}_{0}(\omega)= \begin{cases}1 & \text { if } \omega>0, \\ 0 & \text { otherwise } .\end{cases}
@@ -176,16 +288,23 @@
 and the step function in Figure 6, which is given by
 
 $$
-\mathcal{U}_{0}(\omega+W)-\mathcal{U}_{0}(\omega-W)= \begin{cases}1 & \text { if }-W<\omega<W, \\ 0 & \text { otherwise } .\end{cases}
-$$
-
-□
-Suppose that $f$ is band limited with band width $W$. Then
-(5) $\quad \hat{f}(\omega)=\frac{1}{W} \sqrt{\frac{\pi}{2}}\left(\mathcal{U}_{0}(\omega+W)-\mathcal{U}_{0}(\omega-W)\right) \sum_{n=-\infty}^{\infty} f\left(\frac{n \pi}{W}\right) e^{-i n \frac{\pi}{W} \omega}$.
-
-Thus to compute the Fourier transform of a band limited function with band width $W$, we only need to sample the function on a discrete set of points, at a sampling rate of $\pi / W$. In the expression on the right side of (5) the factor $\mathcal{U}_{0}(\omega+W)-\mathcal{U}_{0}(\omega-W)$ vanishes for all $|\omega|>W$, which has the effect of truncating the whole expression on the right side for all $|\omega|>W$.
-
-Proof The idea is to use the sampling theorem to write $f$ as specified by (3), then use (1) to compute the Fourier transform. We have
+\mathcal{U}_{0}(\omega+W)-\mathcal{U}_{0}(\omega-W)= \begin{cases}1 & \text { if }-W<\omega\le W, \\ 0 & \text { otherwise } .\end{cases}
+$$
+
+> [!theorem|28e15c10-8e5e-5408-9023-68331e83e99d.local at=4cab5303-52d5-57aa-9fab-a568e58418c6] Fourier Transform Using Sampling
+> Suppose that $f\in L^2(\mathbb R)$ is band limited with band width $W>0$. Then
+>
+> $$
+> \widehat f(\omega)=\frac1W\sqrt{\frac\pi2}\,\left(\mathcal U_0(\omega+W)-\mathcal U_0(\omega-W)\right)\sum_{n\in\mathbb Z}f\left(\frac{n\pi}{W}\right)e^{-in\pi\omega/W}.
+> $$
+>
+> Use $\hat f(\omega)=(2\pi)^{-1/2}\int_{\mathbb R}f(x)e^{-i\omega x}\,dx$, interpreted by mean-square extension for $f\in L^2$. Sample the continuous inverse-Fourier representative of a band-limited function. Here $\mathcal U_0(\omega)=1$ for $\omega>0$ and zero otherwise. The series equality is in mean square; endpoint values do not affect the transform.
+
+*Printed equation label: (5).*
+
+Thus to compute the Fourier transform of a band limited function with band width $W$, we only need to sample the function on a discrete set of points, at a sampling spacing of $\pi/W$ (rate $W/\pi$). In the expression on the right side of (5) the factor $\mathcal{U}_{0}(\omega+W)-\mathcal{U}_{0}(\omega-W)$ vanishes for all $|\omega|>W$, which has the effect of truncating the whole expression on the right side for all $|\omega|>W$.
+
+Proof The series/integral interchange below is interpreted by taking partial sums and passing to the limit in $L^2$. The idea is to use the sampling theorem to write $f$ as specified by (3), then use (1) to compute the Fourier transform. We have
 
 $$
 \begin{aligned}
@@ -201,15 +320,21 @@
 \frac{1}{W} \sqrt{\frac{\pi}{2}}\left(\mathcal{U}_{0}(\omega+W)-\mathcal{U}_{0}(\omega-W)\right) e^{-i n \frac{\pi}{W} \omega}= \begin{cases}\frac{1}{W} \sqrt{\frac{\pi}{2}} e^{-i n \frac{\pi}{W} \omega} & \text { if }|\omega|<W, \\ 0 & \text { otherwise }\end{cases}
 $$
 
-(see Exercise 5). $\square$
-
-THEOREM 5 FOURIER TRANSFORMS OF EVEN FUNCTIONS USING SAMPLING
+(see Exercise 5; the endpoint values are immaterial in $L^2$). $\square$
 
 Interesting applications of Theorem 4 to boundary value problems are presented in the following section.
 
 The following special case of Theorem 4 is worth noting.
-Suppose that $f$ is even and band limited with band width $I I$. Then
-(6) $\hat{f}(\omega)=\frac{1}{W} \sqrt{\frac{\pi}{2}}\left(\mathcal{U}_{0}(\omega+W)-\mathcal{U}_{0}(\omega-W)\right)\left[f(0)+2 \sum_{n=1}^{n} f\left(\frac{n \pi}{W}\right) \cos \left(\frac{n \pi}{W}{ }^{\prime}\right)\right]$.
+> [!theorem|7cd918f2-1c69-5f69-b560-22cbaa862aba.local at=0b2c5c7b-2101-5733-961a-862277cca5ae] Fourier Transforms of Even Functions Using Sampling
+> Suppose that $f\in L^2(\mathbb R)$ is even and band limited with band width $W>0$. Then
+>
+> $$
+> \widehat f(\omega)=\frac1W\sqrt{\frac\pi2}\,\left(\mathcal U_0(\omega+W)-\mathcal U_0(\omega-W)\right)\left[f(0)+2\sum_{n=1}^\infty f\left(\frac{n\pi}{W}\right)\cos\left(\frac{n\pi\omega}{W}\right)\right].
+> $$
+>
+> Use $\hat f(\omega)=(2\pi)^{-1/2}\int_{\mathbb R}f(x)e^{-i\omega x}\,dx$, interpreted by mean-square extension for $f\in L^2$. Sample the continuous inverse-Fourier representative of a band-limited function. Here $\mathcal U_0(\omega)=1$ for $\omega>0$ and zero otherwise. The series equality is in mean square; endpoint values do not affect the transform.
+
+*Printed equation label: (6).*
 
 Proof Consider the symmetric partial sums in (5), and add together the terms corresponding to $n$ and $-n$. Simplify, using $f\left(-\frac{n \pi}{W}\right)=f\left(\frac{n \pi}{W}\right)$ and
 
@@ -219,14 +344,40 @@
 
 We illustrate the last two theorems with a numerical example.
 
-![](./images/e0b9cf26-d77c-487a-ae6f-e9bad0026586-07_414_396_946_75.jpg)
-Figure 7
-
-![](./images/e0b9cf26-d77c-487a-ae6f-e9bad0026586-07_355_442_1433_77.jpg)
-
-Figure 8 Approximation of $\widehat{k}$ using three nonzero terms of the sampled series.
-
-## EXAMPLE 3 Computing a Fourier transform using sampling
+```scientific-figure
+id: 17b77254-0590-495c-b882-d8e676b5502e
+numbered: false
+title: ""
+caption: Figure 7
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 17 Sampling and Discrete Fourier Analysis with Applications to Partial Differential Equations/images/e0b9cf26-d77c-487a-ae6f-e9bad0026586-07_414_396_946_75.jpg
+    caption: ""
+```
+
+
+```scientific-figure
+id: 18f47472-5160-4bae-adc0-76627231d4f2
+numbered: false
+title: ""
+caption: Figure 8 Approximation of $\widehat{k}$ using three nonzero terms of the sampled series.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 17 Sampling and Discrete Fourier Analysis with Applications to Partial Differential Equations/images/e0b9cf26-d77c-487a-ae6f-e9bad0026586-07_355_442_1433_77.jpg
+    caption: ""
+```
+
+
+> [!exercise|a8622ae6-d0cd-5fca-958d-bb7b245c7b7d.local at=078851b6-3571-598c-b22f-924c53caacbf] EXAMPLE 3 Computing a Fourier transform using sampling
+> Use even-function sampling to reconstruct the Fourier transform of $k(x)=(\sin x/x)^2$, with $k(0)=1$, and approximate the transform using three nonzero cosine-series terms.
+
+
+
+##### solution
 
 Let
 
@@ -240,32 +391,35 @@
 \widehat{k}(\omega)= \begin{cases}\sqrt{\frac{\pi}{2}}\left(1-\frac{|\omega|}{2}\right) & \text { if }|\omega| \leq 2 \\ 0 & \text { otherwise }\end{cases}
 $$
 
-As illustrated in Figure 7, $\widehat{k}$ vanishes outsicle $[-2,2]$, and so $k$ is band limited with band width $W=2$. We will verify the assertion of Theorem 5 by reconstructing the Fourier transform from sample values of $f$. Applying (6),
-
-$$
-\widehat{h}(\omega)=\frac{1}{2} \sqrt{\frac{\pi}{2}}\left(\mathcal{U}_{0}(\omega+2)-\mathcal{U}_{0}(\omega-2)\right)\left[1+2 \sum_{n=1}^{\infty} \frac{\sin ^{2}\left(\frac{n \pi}{2}\right)}{\left(\frac{n \pi}{2}\right)^{2}} \cos \left(\frac{n \pi}{2} \omega\right)\right] .
-$$
-
-Note that all the terms for even $n$ are zero, except for $n=0$. A pretty good approximation of $\widehat{f}$ is obtained by taking only three nonzero terms from the sum. This partial sum approximation of $\widehat{f}$ is shown in Figure 8. Thus, if we did not know the Fourier transform, we would obtain a pretty good approximation of $\widehat{f}$ by sampling the function at six points: $x=\frac{n \pi}{2}, n=1,2, \ldots, 6$.
+As illustrated in Figure 7, $\widehat{k}$ vanishes outside $[-2,2]$, and so $k$ is band limited with band width $W=2$. We will verify the assertion of Theorem 5 by reconstructing the Fourier transform from sample values of $k$. Applying (6),
+
+$$
+\widehat{k}(\omega)=\frac{1}{2} \sqrt{\frac{\pi}{2}}\left(\mathcal{U}_{0}(\omega+2)-\mathcal{U}_{0}(\omega-2)\right)\left[1+2 \sum_{n=1}^{\infty} \frac{\sin ^{2}\left(\frac{n \pi}{2}\right)}{\left(\frac{n \pi}{2}\right)^{2}} \cos \left(\frac{n \pi}{2} \omega\right)\right] .
+$$
+
+Note that all the terms for even $n$ are zero, except for $n=0$. A pretty good approximation of $\widehat{k}$ is obtained by taking only three nonzero terms from the sum. This partial sum approximation of $\widehat{k}$ is shown in Figure 8. Thus, if we did not know the Fourier transform, we would obtain a pretty good approximation of $\widehat{k}$ by sampling the function using the known central value $k(0)=1$ and sampling at six positive points: $x=\frac{n \pi}{2}, n=1,2, \ldots, 6$.
 
 ## Appendix: Proof of the Sampling Theorem
 
-Since $\hat{f}$ vanishes outside $[-W, W]$, we have by Fourier inversion (Section 7.2, (2))
-
-$$
-f(x)=\frac{1}{\sqrt{2 \pi}} \int_{-W}^{W} f(\omega) e^{i \cdots r} d \omega
-$$
-
-Also, since $\widehat{f}$ vanishes outside $[-W, W]$, we can extend $\widehat{f}$ periodically (with period $2 W$ ) on the $\omega$-axis and then use a Fourier series (Section 2.6, (3)) to represent it as
+Since $\hat{f}$ vanishes outside $[-W, W]$, we have by Fourier inversion (Section 8.2, (2))
+
+$$
+f(x)=\frac{1}{\sqrt{2 \pi}} \int_{-W}^W\widehat f(\omega)e^{i\omega x} d \omega
+\tag{7}
+$$
+
+Also, since $\widehat{f}$ vanishes outside $[-W, W]$, we can extend $\widehat{f}$ periodically (with period $2 W$ ) on the $\omega$-axis and then use a Fourier series (Section 7.6, (3)) to represent it as
 
 $$
 \widehat{f}(\omega)=\sum_{n=-\infty}^{\infty} c_{n} e^{i \frac{n \pi}{W} \omega}=\sum_{n=-\infty}^{\infty} c_{-n} e^{-i \frac{n \pi}{W} \omega} \quad(|\omega|<W) .
-$$
-
-Using the definition of the Fourier coefficients (Section 2.6, (4)) and (7), we get
+\tag{8}
+$$
+
+Using the definition of the Fourier coefficients (Section 7.6, (4)) and (7), we get
 
 $$
 c_{-n}=\frac{1}{2 W} \int_{-W}^{W} \widehat{f}(\omega) e^{i \frac{n \pi}{W} \omega} d \omega=\frac{\sqrt{2 \pi}}{2 W} f\left(\frac{n \pi}{W}\right)
+\tag{9}
 $$
 
 Before we finish off the proof, we evaluate one more integral. Keeping in mind Euler's identity ( $e^{i \theta}=\cos \theta+i \sin \theta$ ) and the fact that the integral of an odd function over a symmetric interval about zero is zero, we have
@@ -276,98 +430,224 @@
 & =\frac{1}{2 W} \int_{-W}^{W} \cos \left(\frac{W x-n \pi}{W} \omega\right) d \omega \\
 & =\frac{\sin (W x-n \pi)}{W x-n \pi}
 \end{aligned}
-$$
-
-We can now establish (3) as follows:
+\tag{10}
+$$
+
+Substitute the Fourier series (in $L^2[-W,W]$) into the inversion integral and pass to the limit from finite partial sums:
 
 $$
 \begin{aligned}
-f(x) & =\frac{1}{\sqrt{2 \pi}} \int_{-W}^{W} \overbrace{\sum_{n=-\infty}^{\infty} c_{-n} e^{-i \frac{n \pi}{W} \omega}}^{\hat{f}(\omega)} e^{i \omega x} d \omega \quad \text { (by (7) and (8)) } \\
-& =\frac{1}{\sqrt{2 \pi}} \int_{-W}^{W} \overbrace{n=-\infty}^{\infty} \overbrace{\frac{\sqrt{2 \pi}}{2 W} f\left(\frac{n \pi}{W}\right)}^{c_{-n}}) e^{-i \frac{n \pi}{W} \omega} e^{i \omega x} d \omega \quad \text { (by (9)) } \\
-& =\sum_{n=-\infty}^{\infty} f\left(\frac{n \pi}{W}\right) \frac{1}{2 W} \int_{-W}^{W} e^{-i \frac{n \pi}{W} \omega} e^{i \omega x} d \omega \\
-& =\sum_{n=-\infty}^{\infty} f\left(\frac{n \pi}{W}\right) \frac{\sin (W x-n \pi)}{W x-n \pi} \quad \text { (by (10)). }
+f(x)&=\frac1{\sqrt{2\pi}}\int_{-W}^W\sum_{n\in\mathbb Z}c_{-n}e^{-in\pi\omega/W}e^{i\omega x}\,d\omega\\
+&=\frac1{\sqrt{2\pi}}\int_{-W}^W\sum_{n\in\mathbb Z}\frac{\sqrt{2\pi}}{2W}f\left(\frac{n\pi}{W}\right)e^{-in\pi\omega/W}e^{i\omega x}\,d\omega\\
+&=\sum_{n\in\mathbb Z}f\left(\frac{n\pi}{W}\right)\frac1{2W}\int_{-W}^We^{i\omega(x-n\pi/W)}\,d\omega\\
+&=\sum_{n\in\mathbb Z}f\left(\frac{n\pi}{W}\right)\frac{\sin(Wx-n\pi)}{Wx-n\pi}.
 \end{aligned}
 $$
 
-## Exercises 10.1
-
-1. Prove Theorem 1, (a) and (c).
-2. Use the table of Fourier transforms to decide which of the following functions are band limited. For such functions, determine a band width.
-(a) $f(x)=\frac{\sin 2 x}{x}$.
-(b) $f(x)=\frac{1-\cos x}{x^{2}}$.
-(c) $f(x)=\mathcal{U}_{0}(1-|x|)$.
-(d) $f(x)=\frac{\sin ^{4} x}{x^{4}}$.
-
-In Exercises 3-4, you are given the sampled values of a band limited function $f(x)$ and its band width $W$. (a) Use the sampling theorem to construct an approximation of $f(x)$ (see Example 2).
-(b) To verify the sumpling theorem, in this part you are also given the function $f(x)$. Plot and compare $f(x)$ and your approximating function that you obtained in (a).
-3. (a) $W=4$,
-
-| $x$ | 0 | $\pm \pi / 4$ | $\pm \pi / 2$ | $\pm 3 \pi / 4$ | $\pm \pi$ |
-| :---: | :---: | :---: | :---: | :---: | :---: |
-| $f(x)$ | -0.05068 | -0.24400 | 1.73064 | 1.92217 | -0.15555 |
-
-(b) $f(x)=\sqrt{\frac{2}{\pi}} \frac{\sin ^{2}(2(x-2))-\sin ^{2}(x-2)}{(x-2)^{2}}$.
-4. (a) $W=6$,
-
-| $x$ | 0 | $\pi / 6$ | $\pi / 3$ | $\pi / 2$ | $2 \pi / 3$ | $5 \pi / 6$ | $\pi$ | $7 \pi / 6$ | $4 \pi / 3$ | $3 \pi / 2$ | $5 \pi / 3$ |
-| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
-| $f(x)$ | 3.59 | 0.97 | -0.18 | 0.11 | 0 | 0.04 | -0.05 | 0.02 | 0 | 0.01 | -0.02 |
-
-(b) $f(x)=\frac{4}{3 \sqrt{2 \pi}} \frac{\sin ^{2}(3 x)-\sin ^{2}\left(\frac{3}{2} x\right)}{x^{2}}$.
-5. Compute the Fourier transform of $\frac{\sin (W x-n \pi)}{W x-n \pi}$.
-6. The table below contains a set of samples of a function $f$ with band width 1 .
-
-| $x$ | $-4 \pi$ | $-3 \pi$ | $-2 \pi$ | $-\pi$ | 0 | $\pi$ | $2 \pi$ | $3 \pi$ | $4 \pi$ |
-| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
-| $f(x)$ | 0 | 1 | 0 | -1 | 0 | -1 | 0 | 1 | 0 |
-
-Approximate $\widehat{f}$ at the points $\omega=0 . \pm .5, \pm .75, \pm 2$.
-Project Problem: Approximation by band limited functions. We mentioned in this section that band limited functions can be used to approximate arbitrary functions as closely as we want. Do Exercises 7 and 8 to justify this result. Exercises 9 and 10 describe alternative proofs.
-7. Fejér's kernel. For $n=1,2,3, \ldots$ define
-
-$$
-k_{n}(x)=\frac{1}{\sqrt{2 \pi}} n\left(\frac{\sin \left(\frac{1}{2} n x\right)}{\frac{1}{2} n x}\right)^{2}=\frac{4}{\sqrt{2 \pi}} \frac{\sin ^{2}\left(\frac{1}{2} n x\right)}{n x^{2}} .
-$$
-
-The function $k_{n}(x)$ is known as a Fejér kernel.
-(a) Use the table of Fourier transforms to show that
-
-$$
-\hat{k}_{n}(\omega)=\left(1-\frac{|\omega|}{n}\right) \mathcal{U}_{0}(n-|\omega|) .
-$$
-
-(b) Plot the graphs of $k_{n}$ for various values of $n$, and describe the behavior of these graphs near 0 , as $n$ increases.
-(c) Show that $\lim _{n} . \hat{k}_{n}(\omega)=1$ for all $\omega$.
-(d) Plot several graphs to illustrate the result in (c).
-8. In this exercise, we suppose that all functions that we are dealing with are defined on the real line and have Fourier transforms.
-(a) Let $k_{n}$ be as in Exercise 7. Show that $f * k_{n}$ is band limited.
-(b) Use Exercise 7(c) to justify the fact that $\lim _{n \rightarrow \infty} f * k_{n}(x)=f(x)$. Thus $f$ may be approximated by the band limited functions $f * k_{n}$.
-9. Abel's kernel For $n=1,2, \ldots$ define
-
-$$
-h_{n}(t)=\sqrt{\frac{2}{\pi}} \frac{n}{1+n^{2} t^{2}}
-$$
-
-The function $h_{n}$ is known as Abel kernel.
-(a) Show that $\hat{h}_{n}(\omega)=e^{-\frac{|\omega|}{n}}$.
-(b) Illustrate graphically the fact that as $n \rightarrow \infty$, the graphs of $h_{n}(t)$ are more and more concentrated around the origin, while the graphs of $\widehat{h}_{n}(\omega)$ spread out.
-(c) Show that $\lim _{n \rightarrow \infty} \widehat{h}_{n}(\omega)=1$. Based on this result, explain why $\lim _{n \rightarrow \infty} h_{n} * f(x)=f(x)$.
-10. De la Vallée Poussin kernel. For $n=1,2, \ldots$ define the de la Vallée Poussin kernel by $v_{n}(t)=2 k_{2 n}(t)-k_{n}(t)$, where $k_{n}$ is Fejér's kernel (Exercise 7). Show the following.
-(a) $v_{n}(t)$ is band limited with band width $2 n$.
-(b)
-
-$$
-\hat{v}_{n}(\omega)= \begin{cases}1 & \text { if }|\omega|<n \\ 0 & \text { if }|\omega|>2 n \\ (-\omega+2 n) / n & \text { if } n \leq \omega \leq 2 n \\ (\omega+2 n) / n & \text { if }-2 n \leq \omega \leq-n\end{cases}
-$$
-
-Plot $\widehat{v}_{n}(\omega)$ for $n=1.2, \ldots, 5$. Can you justify calling $\widehat{v}_{n}(\omega)$ a tent function? (c) Obtain the explicit formulas for the de la Vallée Poussin kernel and its Fourier transform
-
-$$
-\begin{gathered}
-v_{n}(t)=\frac{4}{\sqrt{2 \pi}} \frac{\sin ^{2}(n t)-\sin ^{2}\left(\frac{1}{2} n t\right)}{n t^{2}}, \\
-\widehat{v}_{n}(\omega)=(|2 n+\omega|+|2 n-\omega|-|n+\omega|-|n-\omega|) / 2 n
-\end{gathered}
-$$
-
-(d) Plot the tents $\widehat{v}_{1}(\omega), \widehat{v}_{2}(\omega), \widehat{v}_{4}(\omega)$.
-(1) How can you approximate a function by band limited functions using the de la Vallée Poussin kernel? Justify your answer.
+## Exercises 17.1
+
+
+> [!exercise|f2a89db8-0d2a-5293-bd7c-ef367d956c41.local at=15e8c66a-7127-5a64-933b-bd681ba055b8] Exercise 1
+> Prove Theorem 1, (a) and (c).
+
+
+> [!exercise|525e3245-e31b-5198-920b-527204d31688.local at=b6ecadd0-9a21-5bc5-9be7-7a2558199e45] Exercise 2
+> Use the table of Fourier transforms to decide which of the following functions are band limited. For such functions, determine a band width.
+> (a) $f(x)=\frac{\sin 2 x}{x}$.
+> (b) $f(x)=\frac{1-\cos x}{x^{2}}$.
+> (c) $f(x)=\mathcal{U}_{0}(1-|x|)$.
+> (d) $f(x)=\frac{\sin ^{4} x}{x^{4}}$.
+
+
+> [!prompt|9e9e6bb1-146b-50b8-9dca-3844f51aafdf.local at=2b16daf5-ccb4-58fb-8065-81e6fe4794d3] Shared exercise instructions
+> In Exercises 3-4, you are given the sampled values of a band limited function $f(x)$ and its band width $W$. (a) Use the sampling theorem to construct an approximation of $f(x)$ (see Example 2).
+> (b) To verify the sampling theorem, in this part you are also given the function $f(x)$. Plot and compare $f(x)$ and your approximating function that you obtained in (a).
+
+
+
+
+> [!exercise|629dabf7-6014-5754-bdb5-75888d51ebd4.local at=ce86f679-7647-574e-93d0-d098803cfa28] Exercise 3
+> (a) $W=4$,
+>
+> (b) $f(x)=\sqrt{\frac{2}{\pi}} \frac{\sin ^{2}(2(x-2))-\sin ^{2}(x-2)}{(x-2)^{2}}$.
+
+
+```scientific-table
+id: 4891e00d-62b2-4351-a2f7-9aa92ee9788f
+numbered: false
+title: ""
+caption: ""
+captionVisible: true
+captionPosition: below
+rows:
+  - - text: $x$
+    - text: "0"
+    - text: $\pi/4$
+    - text: $\pi/2$
+    - text: $3\pi/4$
+    - text: $\pi$
+  - - text: $f(x)$
+    - text: "-0.05068"
+    - text: "-0.24400"
+    - text: "1.73064"
+    - text: "1.92217"
+    - text: "-0.15555"
+headerRows: 1
+rowHeaders: true
+style: scientific
+```
+
+
+
+> [!exercise|3c31a5ec-8388-5f7c-be0e-f90bcc11995e.local at=64fdd6a9-ad16-5fd1-9532-29d695e57e8b] Exercise 4
+> (a) $W=6$,
+>
+> (b) $f(x)=\frac{4}{3 \sqrt{2 \pi}} \frac{\sin ^{2}(3 x)-\sin ^{2}\left(\frac{3}{2} x\right)}{x^{2}}$.
+
+
+```scientific-table
+id: c92d6926-52ae-4050-aa53-c50a08d64a7b
+numbered: false
+title: ""
+caption: ""
+captionVisible: true
+captionPosition: below
+rows:
+  - - text: $x$
+    - text: "0"
+    - text: $\pi / 6$
+    - text: $\pi / 3$
+    - text: $\pi / 2$
+    - text: $2 \pi / 3$
+    - text: $5 \pi / 6$
+    - text: $\pi$
+    - text: $7 \pi / 6$
+    - text: $4 \pi / 3$
+    - text: $3 \pi / 2$
+    - text: $5 \pi / 3$
+  - - text: $f(x)$
+    - text: "3.59"
+    - text: "0.97"
+    - text: "-0.18"
+    - text: "0.11"
+    - text: "0"
+    - text: "0.04"
+    - text: "-0.05"
+    - text: "0.02"
+    - text: "0"
+    - text: "0.01"
+    - text: "-0.02"
+headerRows: 1
+rowHeaders: true
+style: scientific
+```
+
+
+
+> [!exercise|2a1e9c17-5f0f-5f60-8b69-ddd5b10a8c01.local at=679dedf6-ac84-5b8c-ae57-ab0f7b26b656] Exercise 5
+> Compute the Fourier transform of $\frac{\sin (W x-n \pi)}{W x-n \pi}$.
+
+
+> [!exercise|5488e3c0-b94a-5f80-acd8-ce2faadcd30f.local at=aefbd577-d33d-5624-9771-474e715fae61] Exercise 6
+> The table below contains a set of samples of a function $f$ with band width 1 .
+>
+> Approximate $\widehat{f}$ at the points $\omega=0 . \pm .5, \pm .75, \pm 2$.
+
+
+```scientific-table
+id: 58df3a63-39e3-450b-80a5-49b12cf812f7
+numbered: false
+title: ""
+caption: ""
+captionVisible: true
+captionPosition: below
+rows:
+  - - text: $x$
+    - text: $-4 \pi$
+    - text: $-3 \pi$
+    - text: $-2 \pi$
+    - text: $-\pi$
+    - text: "0"
+    - text: $\pi$
+    - text: $2 \pi$
+    - text: $3 \pi$
+    - text: $4 \pi$
+  - - text: $f(x)$
+    - text: "0"
+    - text: "1"
+    - text: "0"
+    - text: "-1"
+    - text: "0"
+    - text: "-1"
+    - text: "0"
+    - text: "1"
+    - text: "0"
+headerRows: 1
+rowHeaders: true
+style: scientific
+```
+
+
+
+> [!prompt|2228ac07-f7cc-547b-8a9a-fbbb942a7fa7.local at=5f71de3a-d003-525a-b667-c8d7394b9915] Shared exercise instructions
+> Project Problem: Approximation by band limited functions. We mentioned in this section that band limited functions can be used to approximate arbitrary functions as closely as we want. Do Exercises 7 and 8 to justify this result. Exercises 9 and 10 describe alternative proofs.
+
+
+> [!exercise|40a25c14-63ce-54a2-93bd-cec02c2a4637.local at=bb000d79-a3b6-53a5-992a-cf4c8646ec2b] Exercise 7
+> Fejér's kernel. For $n=1,2,3, \ldots$ define
+>
+> $$
+> k_{n}(x)=\frac{1}{\sqrt{2 \pi}} n\left(\frac{\sin \left(\frac{1}{2} n x\right)}{\frac{1}{2} n x}\right)^{2}=\frac{4}{\sqrt{2 \pi}} \frac{\sin ^{2}\left(\frac{1}{2} n x\right)}{n x^{2}} .
+> $$
+>
+> The function $k_{n}(x)$ is known as a Fejér kernel.
+> (a) Use the table of Fourier transforms to show that
+>
+> $$
+> \hat{k}_{n}(\omega)=\left(1-\frac{|\omega|}{n}\right) \mathcal{U}_{0}(n-|\omega|) .
+> $$
+>
+> (b) Plot the graphs of $k_{n}$ for various values of $n$, and describe the behavior of these graphs near 0 , as $n$ increases.
+> (c) Show that $\lim_{n\to\infty}\hat{k}_n(\omega)=1$ for all $\omega$.
+> (d) Plot several graphs to illustrate the result in (c).
+
+
+> [!exercise|23a6859d-8de6-5fe4-813e-44a51ae52328.local at=3242bd9a-e5d3-5cc4-8c84-9877ceebd58b] Exercise 8
+> Assume $f\in L^2(\mathbb R)$ and use the normalized convolution $(f*g)(x)=(2\pi)^{-1/2}\int f(x-t)g(t)\,dt$.
+> (a) Let $k_{n}$ be as in Exercise 7. Show that $f * k_{n}$ is band limited.
+> (b) Use Exercise 7(c) to justify $f*k_n\to f$ in $L^2$ (and pointwise at continuity points when $f$ is also bounded and continuous). Thus $f$ may be approximated by the band limited functions $f * k_{n}$.
+
+
+> [!exercise|82f18500-0a15-5517-986a-442ee8a90031.local at=5e307f1a-516b-5fb9-ae68-812480f4f6e1] Exercise 9
+> Abel's kernel For $n=1,2, \ldots$ define
+>
+> $$
+> h_{n}(t)=\sqrt{\frac{2}{\pi}} \frac{n}{1+n^{2} t^{2}}
+> $$
+>
+> The function $h_{n}$ is known as Abel kernel.
+> (a) Show that $\hat{h}_{n}(\omega)=e^{-\frac{|\omega|}{n}}$.
+> (b) Illustrate graphically the fact that as $n \rightarrow \infty$, the graphs of $h_{n}(t)$ are more and more concentrated around the origin, while the graphs of $\widehat{h}_{n}(\omega)$ spread out.
+> (c) Show that $\lim _{n \rightarrow \infty} \widehat{h}_{n}(\omega)=1$. Based on this result, explain why $h_n*f\to f$ in $L^2$ for $f\in L^2(\mathbb R)$. For bounded continuous $f$, also discuss pointwise convergence.
+
+
+> [!exercise|1fa1be91-5e8e-5a22-9c2c-979e7ba087cf.local at=66c59e69-c237-5fbd-b249-24008c7bca4b] Exercise 10
+> De la Vallée Poussin kernel. For $n=1,2, \ldots$ define the de la Vallée Poussin kernel by $v_{n}(t)=2 k_{2 n}(t)-k_{n}(t)$, where $k_{n}$ is Fejér's kernel (Exercise 7). Show the following.
+> (a) $v_{n}(t)$ is band limited with band width $2 n$.
+> (b)
+>
+> $$
+> \hat{v}_{n}(\omega)= \begin{cases}1 & \text { if }|\omega|<n \\ 0 & \text { if }|\omega|>2 n \\ (-\omega+2 n) / n & \text { if } n \leq \omega \leq 2 n \\ (\omega+2 n) / n & \text { if }-2 n \leq \omega \leq-n\end{cases}
+> $$
+>
+> Plot $\widehat{v}_{n}(\omega)$ for $n=1,2, \ldots, 5$. Can you justify calling $\widehat{v}_{n}(\omega)$ a tent function? (c) Obtain the explicit formulas for the de la Vallée Poussin kernel and its Fourier transform
+>
+> $$
+> \begin{gathered}
+> v_{n}(t)=\frac{4}{\sqrt{2 \pi}} \frac{\sin ^{2}(n t)-\sin ^{2}\left(\frac{1}{2} n t\right)}{n t^{2}}, \\
+> \widehat{v}_{n}(\omega)=(|2 n+\omega|+|2 n-\omega|-|n+\omega|-|n-\omega|) / 2 n
+> \end{gathered}
+> $$
+>
+> (d) Plot the tents $\widehat{v}_{1}(\omega), \widehat{v}_{2}(\omega), \widehat{v}_{4}(\omega)$.
+> (e) How can you approximate a function by band limited functions using the de la Vallée Poussin kernel? Justify your answer.

`````
