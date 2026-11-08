
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
