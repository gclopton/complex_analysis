
# Editorial records

Reading note: 8.2 Operational Properties.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|919c9527-2e40-5f7d-ba42-5547a0c14265.local at=b3c9a3ae-fac1-52da-a9b6-b751b60879ca] Fourier Transforms of Derivatives
> Use the symmetric Fourier transform $\widehat f(\omega)=(2\pi)^{-1/2}\int_{\mathbb R}f(x)e^{-i\omega x}\,dx$. For each stated derivative order, assume the lower derivatives are locally absolutely continuous, so integration by parts applies. In the general formula also assume $f(x)\to0$ at both infinities.
>
> (i) Suppose $f(x)$ and $f^{\prime}(x)$ are integrable and $f(x) \rightarrow 0$ as $|x| \rightarrow \infty$; then
>
> $$
> \mathcal{F}\left(f^{\prime}\right)=i \omega \mathcal{F}(f) .
> $$
>
> (ii) If, in addition, $f^{\prime \prime}(x)$ is integrable and $f^{\prime}(x) \rightarrow 0$ as $|x| \rightarrow \infty$, then
>
> $$
> \mathcal{F}\left(f^{\prime \prime}\right)=i \omega \mathcal{F}\left(f^{\prime}\right)=-\omega^{2} \mathcal{F}(f) .
> $$
>
> (iii) In general, if $f^{(k)}(x) \rightarrow 0(k=1,2, \ldots, n-1)$ as $|x| \rightarrow \infty$, and $f$ and its derivatives of order up to $n$ are integrable, then
>
> $$
> \mathcal{F}\left(f^{(n)}\right)=(i \omega)^{n} \mathcal{F}(f) .
> $$
````
### After

````text
> [!theorem|919c9527-2e40-5f7d-ba42-5547a0c14265.local at=b3c9a3ae-fac1-52da-a9b6-b751b60879ca] Fourier transforms of derivatives
> Use the symmetric Fourier transform $\widehat f(\omega)=(2\pi)^{-1/2}\int_{\mathbb R}f(x)e^{-i\omega x}\,dx$. For each stated derivative order, assume the lower derivatives are locally absolutely continuous, so integration by parts applies. In the general formula also assume $f(x)\to0$ at both infinities.
>
> (i) Suppose $f(x)$ and $f^{\prime}(x)$ are integrable and $f(x) \rightarrow 0$ as $|x| \rightarrow \infty$; then
>
> $$
> \mathcal{F}\left(f^{\prime}\right)=i \omega \mathcal{F}(f) .
> $$
>
> (ii) If, in addition, $f^{\prime \prime}(x)$ is integrable and $f^{\prime}(x) \rightarrow 0$ as $|x| \rightarrow \infty$, then
>
> $$
> \mathcal{F}\left(f^{\prime \prime}\right)=i \omega \mathcal{F}\left(f^{\prime}\right)=-\omega^{2} \mathcal{F}(f) .
> $$
>
> (iii) In general, if $f^{(k)}(x) \rightarrow 0(k=1,2, \ldots, n-1)$ as $|x| \rightarrow \infty$, and $f$ and its derivatives of order up to $n$ are integrable, then
>
> $$
> \mathcal{F}\left(f^{(n)}\right)=(i \omega)^{n} \mathcal{F}(f) .
> $$
````

## 2. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|4a7c260a-75bb-5fd4-a015-fab7b9a6dd83.local at=b1010265-7403-51b5-ae36-f6dc2845b989] Differentiation of the Fourier Transform by Multiplication in Position
> Use the symmetric Fourier transform $\widehat f(\omega)=(2\pi)^{-1/2}\int_{\mathbb R}f(x)e^{-i\omega x}\,dx$. Integrability means absolute integrability on $\mathbb R$; $n$ is a positive integer.
>
> (i) Suppose $f(x)$ and $x f(x)$ are integrable, then
>
> $$
> \mathcal{F}(x f(x))(\omega)=i[\hat{f}]^{\prime}(\omega)=i \frac{d}{d \omega} \mathcal{F}(f)(\omega)
> $$
>
> (ii) In general, if $f(x)$ and $x^{n} f(x)$ are integrable, then
>
> $$
> \mathcal{F}\left(x^{n} f(x)\right)=i^{n}[\hat{f}]^{(n)}(\omega)
> $$
````
### After

````text
> [!theorem|4a7c260a-75bb-5fd4-a015-fab7b9a6dd83.local at=b1010265-7403-51b5-ae36-f6dc2845b989] Derivatives of Fourier transforms
> Use the symmetric Fourier transform $\widehat f(\omega)=(2\pi)^{-1/2}\int_{\mathbb R}f(x)e^{-i\omega x}\,dx$. Integrability means absolute integrability on $\mathbb R$; $n$ is a positive integer.
>
> (i) Suppose $f(x)$ and $x f(x)$ are integrable, then
>
> $$
> \mathcal{F}(x f(x))(\omega)=i[\hat{f}]^{\prime}(\omega)=i \frac{d}{d \omega} \mathcal{F}(f)(\omega)
> $$
>
> (ii) In general, if $f(x)$ and $x^{n} f(x)$ are integrable, then
>
> $$
> \mathcal{F}\left(x^{n} f(x)\right)=i^{n}[\hat{f}]^{(n)}(\omega)
> $$
````

## 3. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|85044e8d-43b2-51c9-aee8-d04f90d3bc7a.local at=bb222b73-e8e9-5a43-9877-468d1d7a46a1] Fourier Translation and Modulation Laws
> Use the symmetric Fourier transform $\widehat f(\omega)=(2\pi)^{-1/2}\int_{\mathbb R}f(x)e^{-i\omega x}\,dx$. Assume $f\in L^1(\mathbb R)$ and $\alpha\in\mathbb R$.
>
> (i) Shifting on the $x$-axis: Let $\alpha$ be arbitrary, then
>
> $$
> \mathcal{F}(f(x-\alpha))(\omega)=e^{-i \alpha \omega} \widehat{f}(\omega)
> $$
>
> (ii) Shifting on the $\omega$-axis:
>
> $$
> \mathcal{F}\left(e^{i \alpha x} f(x)\right)(\omega)=\widehat{f}(\omega-\alpha)
> $$
````
### After

````text
> [!theorem|85044e8d-43b2-51c9-aee8-d04f90d3bc7a.local at=bb222b73-e8e9-5a43-9877-468d1d7a46a1] Shifting and Fourier transforms
> Use the symmetric Fourier transform $\widehat f(\omega)=(2\pi)^{-1/2}\int_{\mathbb R}f(x)e^{-i\omega x}\,dx$. Assume $f\in L^1(\mathbb R)$ and $\alpha\in\mathbb R$.
>
> (i) Shifting on the $x$-axis: Let $\alpha$ be arbitrary, then
>
> $$
> \mathcal{F}(f(x-\alpha))(\omega)=e^{-i \alpha \omega} \widehat{f}(\omega)
> $$
>
> (ii) Shifting on the $\omega$-axis:
>
> $$
> \mathcal{F}\left(e^{i \alpha x} f(x)\right)(\omega)=\widehat{f}(\omega-\alpha)
> $$
````

## 4. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|5ba4babe-0c07-5fea-9706-d4fe75d4b43d.local at=0f47916c-7204-54dd-a8df-0279e735f670] Fourier Transform of Normalized Convolution
> Use the symmetric Fourier transform $\widehat f(\omega)=(2\pi)^{-1/2}\int_{\mathbb R}f(x)e^{-i\omega x}\,dx$. The normalized convolution is $(f*g)(x)=(2\pi)^{-1/2}\int_{\mathbb R}f(x-t)g(t)\,dt$.
>
> Suppose that $f$ and $g$ are integrable, then
>
> $$
> \mathcal{F}(f * g)=\mathcal{F}(f) \mathcal{F}(g)
> $$
````
### After

````text
> [!theorem|5ba4babe-0c07-5fea-9706-d4fe75d4b43d.local at=0f47916c-7204-54dd-a8df-0279e735f670] Fourier transforms of convolutions
> Use the symmetric Fourier transform $\widehat f(\omega)=(2\pi)^{-1/2}\int_{\mathbb R}f(x)e^{-i\omega x}\,dx$. The normalized convolution is $(f*g)(x)=(2\pi)^{-1/2}\int_{\mathbb R}f(x-t)g(t)\,dt$.
>
> Suppose that $f$ and $g$ are integrable, then
>
> $$
> \mathcal{F}(f * g)=\mathcal{F}(f) \mathcal{F}(g)
> $$
````

## 5. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|e0b81521-076b-50b7-bd89-d9e140d49885.local at=0df90327-94ea-5e96-92d5-eaa81476caa3] Differentiation of Normalized Convolution
> The normalized convolution is $(f*g)(x)=(2\pi)^{-1/2}\int_{\mathbb R}f(x-t)g(t)\,dt$. Assume the derivatives used below are absolutely integrable, the lower derivatives are locally absolutely continuous, and the boundary terms vanish at infinity.
>
> Let $n, \alpha$ and $\beta$ denote nonnegative integers, such that $n=\alpha+\beta$. Then
>
> $$
> \frac{d^{n}}{d x^{n}}(f * g)=\frac{d^{\alpha} f}{d x^{\alpha}} * \frac{d^{\beta} g}{d x^{\beta}}
> $$
>
> In particular, taking $\alpha=n$ and $\beta=0$, then $\alpha=0$ and $\beta=n$, we obtain
>
> $$
> \frac{d^{n}}{d x^{n}}(f * g)=\frac{d^{n} f}{d x^{n}} * g=f * \frac{d^{n} g}{d x^{n}}
> $$
````
### After

````text
> [!theorem|e0b81521-076b-50b7-bd89-d9e140d49885.local at=0df90327-94ea-5e96-92d5-eaa81476caa3] Convolutions and derivatives
> The normalized convolution is $(f*g)(x)=(2\pi)^{-1/2}\int_{\mathbb R}f(x-t)g(t)\,dt$. Assume the derivatives used below are absolutely integrable, the lower derivatives are locally absolutely continuous, and the boundary terms vanish at infinity.
>
> Let $n, \alpha$ and $\beta$ denote nonnegative integers, such that $n=\alpha+\beta$. Then
>
> $$
> \frac{d^{n}}{d x^{n}}(f * g)=\frac{d^{\alpha} f}{d x^{\alpha}} * \frac{d^{\beta} g}{d x^{\beta}}
> $$
>
> In particular, taking $\alpha=n$ and $\beta=0$, then $\alpha=0$ and $\beta=n$, we obtain
>
> $$
> \frac{d^{n}}{d x^{n}}(f * g)=\frac{d^{n} f}{d x^{n}} * g=f * \frac{d^{n} g}{d x^{n}}
> $$
````

## 6. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|5db59350-e816-5761-afd3-ebfd705154a9.local at=c5f01410-f1d2-58c8-bacb-57ebd0e73de1] Parseval Inner-Product Identity for the Symmetric Fourier Transform
> Use the symmetric Fourier transform $\widehat f(\omega)=(2\pi)^{-1/2}\int_{\mathbb R}f(x)e^{-i\omega x}\,dx$. For general $L^2(\mathbb R)$ functions, use the continuous $L^2$ extension of this transform.
>
> Suppose that $f$ and $g$ are square integrable functions on the real line. Then
>
> $$
> \int_{-\infty}^{\infty} f(x) \overline{g(x)} d x=\int_{-\infty}^{\infty} \hat{f}(\omega) \overline{\widehat{g}(\omega)} d \omega
> $$
````
### After

````text
> [!theorem|5db59350-e816-5761-afd3-ebfd705154a9.local at=c5f01410-f1d2-58c8-bacb-57ebd0e73de1] Parseval's theorem
> Use the symmetric Fourier transform $\widehat f(\omega)=(2\pi)^{-1/2}\int_{\mathbb R}f(x)e^{-i\omega x}\,dx$. For general $L^2(\mathbb R)$ functions, use the continuous $L^2$ extension of this transform.
>
> Suppose that $f$ and $g$ are square integrable functions on the real line. Then
>
> $$
> \int_{-\infty}^{\infty} f(x) \overline{g(x)} d x=\int_{-\infty}^{\infty} \hat{f}(\omega) \overline{\widehat{g}(\omega)} d \omega
> $$
````

## 7. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|3f25af67-aeed-5cdf-bee7-fc7c23b552f2.local at=6b543933-5925-5d1e-a8c6-8bfc8fad1be2] Plancherel Norm Identity for the Symmetric Fourier Transform
> Use the symmetric Fourier transform $\widehat f(\omega)=(2\pi)^{-1/2}\int_{\mathbb R}f(x)e^{-i\omega x}\,dx$. For general $L^2(\mathbb R)$ functions, use the continuous $L^2$ extension of this transform.
>
> Suppose that $f$ is a square integrable function on the real line. Then
>
> $$
> \int_{-\infty}^{\infty}|f(x)|^{2} d x=\int_{-\infty}^{\infty}|\hat{f}(\omega)|^{2} d \omega
> $$
````
### After

````text
> [!theorem|3f25af67-aeed-5cdf-bee7-fc7c23b552f2.local at=6b543933-5925-5d1e-a8c6-8bfc8fad1be2] Plancherel's theorem
> Use the symmetric Fourier transform $\widehat f(\omega)=(2\pi)^{-1/2}\int_{\mathbb R}f(x)e^{-i\omega x}\,dx$. For general $L^2(\mathbb R)$ functions, use the continuous $L^2$ extension of this transform.
>
> Suppose that $f$ is a square integrable function on the real line. Then
>
> $$
> \int_{-\infty}^{\infty}|f(x)|^{2} d x=\int_{-\infty}^{\infty}|\hat{f}(\omega)|^{2} d \omega
> $$
````

## 8. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!definition|ce251f7e-b24d-5894-8522-2dcb7d623bb8.local at=d28aeba4-2e47-537e-b4af-cb188e55c241] Normalized Convolution on the Real Line
> For $f,g\in L^1(\mathbb R)$, their normalized convolution, defined for almost every $x$, is
>
> $$
> (f*g)(x)=\frac1{\sqrt{2\pi}}\int_{\mathbb R}f(x-t)g(t)\,dt.
> $$
````
### After

````text
> [!definition|ce251f7e-b24d-5894-8522-2dcb7d623bb8.local at=d28aeba4-2e47-537e-b4af-cb188e55c241] Normalized Convolution on the Real Line
> The convolution of two integrable functions $f$ and $g$ is defined, almost everywhere, by
> $$
> f * g(x)=\frac{1}{\sqrt{2 \pi}} \int_{-\infty}^{\infty} f(x-t) g(t) d t
> $$
````

## 9. Restore source wording; retain only the actual correction.

### Before

````text
These are distributional derivatives: the derivative of a unit jump at $x=\alpha$ is the unit point mass $\delta_\alpha$. No infinite pointwise derivative is being assigned. This interpretation extends differentiation to piecewise smooth functions.
````
### After

````text
We can give some meaning to these identities: The Heaviside is constant so its slope (derivative) is 0, except at $x=\alpha$, where the values of $\mathcal{U}_{\alpha}$ jump from 0 to 1. In the sense of generalized functions, this jump contributes $\delta_\alpha$ to the derivative.
````

## 10. Move correction/commentary into the separate editorial record; keep the actual correction in the reading text.

### Before

````text
[Corrected: the normalization factor in the printed delta-convolution formula must be $(2\pi)^{-(n-1)/2}$.]
````
### After

````text

````

## 11. Move correction/commentary into the separate editorial record; keep the actual correction in the reading text.

### Before

````text
[Corrected: $L^1*L^1$ is integrable, but continuity requires additional hypotheses, such as both factors belonging to $L^2$.]
````
### After

````text

````

## 12. Move correction/commentary into the separate editorial record; keep the actual correction in the reading text.

### Before

````text
[Corrected: the printed Heaviside-transform formulas omit the delta term and the principal-value interpretation.]
````
### After

````text

````
