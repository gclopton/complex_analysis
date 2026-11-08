
# Editorial records

Reading note: 8.5 The Poisson Integral and the Hilbert Transform.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|c9653b03-a8be-50a6-8d4a-fc679e8eb1b3.local at=cdae0e75-8f1f-5a0b-bf07-c56fdcc3c8d8] Harmonicity of the Poisson and Conjugate Poisson Kernels
> The Poisson kernel $P_{y}(x)=\sqrt{\frac{2}{\pi}} \frac{y}{x^{2}+y^{2}}$ is harmonic for all $(x, y) \neq(\mathbf{0}, \mathbf{0})$. Moreover, it has a harmonic conjugate (called the conjugate Poisson kernel) given by
> $$
> Q_{y}(x)=\sqrt{\frac{2}{\pi}} \frac{x}{x^{2}+y^{2}}, \quad(x, y) \neq(0,0)
> $$
````
### After

````text
> [!theorem|c9653b03-a8be-50a6-8d4a-fc679e8eb1b3.local at=cdae0e75-8f1f-5a0b-bf07-c56fdcc3c8d8] Harmonicity of the Poisson kernel
> The Poisson kernel $P_{y}(x)=\sqrt{\frac{2}{\pi}} \frac{y}{x^{2}+y^{2}}$ is harmonic for all $(x, y) \neq(\mathbf{0}, \mathbf{0})$. Moreover, it has a harmonic conjugate (called the conjugate Poisson kernel) given by
> $$
> Q_{y}(x)=\sqrt{\frac{2}{\pi}} \frac{x}{x^{2}+y^{2}}, \quad(x, y) \neq(0,0)
> $$
````

## 2. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|4e77a596-e099-541d-9212-2bc5c7d7313d.local at=ba61bf31-c7d4-5f99-96a2-5c6548fd787e] Harmonic Conjugate from the Conjugate Poisson Integral
> The normalized convolution is $(f*g)(x)=(2\pi)^{-1/2}\int_{\mathbb R}f(x-t)g(t)\,dt$. Let $f\in L^1(\mathbb R)$ be real-valued, $y>0$, $P_y(x)=\sqrt{2/\pi}\,y/(x^2+y^2)$, and $Q_y(x)=\sqrt{2/\pi}\,x/(x^2+y^2)$.
>
> Let $u(x, y)=P_{y} * f(x)$ denote the Poisson extension in the upper half-plane. Then a harmonic conjugate of $u(x, y)$ is given by
>
> $$
> v(x, y)=Q_{y} * f(x)=\frac{1}{\pi} \int_{-\infty}^{\infty} f(x-s) \frac{s}{s^{2}+y^{2}} d s \quad(y>0)
> $$
>
> where $Q_{y}$ is the conjugate Poisson kernel.
````
### After

````text
> [!theorem|4e77a596-e099-541d-9212-2bc5c7d7313d.local at=ba61bf31-c7d4-5f99-96a2-5c6548fd787e] Harmonic conjugate
> The normalized convolution is $(f*g)(x)=(2\pi)^{-1/2}\int_{\mathbb R}f(x-t)g(t)\,dt$. Let $f\in L^1(\mathbb R)$ be real-valued, $y>0$, $P_y(x)=\sqrt{2/\pi}\,y/(x^2+y^2)$, and $Q_y(x)=\sqrt{2/\pi}\,x/(x^2+y^2)$.
>
> Let $u(x, y)=P_{y} * f(x)$ denote the Poisson extension in the upper half-plane. Then a harmonic conjugate of $u(x, y)$ is given by
>
> $$
> v(x, y)=Q_{y} * f(x)=\frac{1}{\pi} \int_{-\infty}^{\infty} f(x-s) \frac{s}{s^{2}+y^{2}} d s \quad(y>0)
> $$
>
> where $Q_{y}$ is the conjugate Poisson kernel.
````

## 3. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|5b01e8f8-1d6e-5c6e-9e53-9cd1284d08ae.local at=f16eb417-cc12-518f-badd-0c4bd357cf56] Hilbert Transform as a Fourier Multiplier
> Use the symmetric Fourier transform $\widehat f(\omega)=(2\pi)^{-1/2}\int_{\mathbb R}f(x)e^{-i\omega x}\,dx$. Use $Hf(x)=\pi^{-1}\operatorname{pv}\int_{\mathbb R}f(x-s)/s\,ds$. For $f\in L^2(\mathbb R)$ this is interpreted as the $L^2$ Hilbert transform.
>
> Let $f\in L^1(\mathbb R)\cap L^2(\mathbb R)$, and let $H(f)(x)$ denote its Hilbert transform. Then
>
> $$
> \widehat{H f}(\omega)=-i \operatorname{sgn}(\omega) \widehat{f}(\omega) \quad\text{for almost every }\omega .
> $$
````
### After

````text
> [!theorem|5b01e8f8-1d6e-5c6e-9e53-9cd1284d08ae.local at=f16eb417-cc12-518f-badd-0c4bd357cf56] Fourier transform of the Hilbert transform
> Use the symmetric Fourier transform $\widehat f(\omega)=(2\pi)^{-1/2}\int_{\mathbb R}f(x)e^{-i\omega x}\,dx$. Use $Hf(x)=\pi^{-1}\operatorname{pv}\int_{\mathbb R}f(x-s)/s\,ds$. For $f\in L^2(\mathbb R)$ this is interpreted as the $L^2$ Hilbert transform.
>
> Let $f\in L^1(\mathbb R)\cap L^2(\mathbb R)$, and let $H(f)(x)$ denote its Hilbert transform. Then
>
> $$
> \widehat{H f}(\omega)=-i \operatorname{sgn}(\omega) \widehat{f}(\omega) \quad\text{for almost every }\omega .
> $$
````

## 4. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|d08bc374-420b-5e61-a58f-9304451f71a5.local at=e5aa6ccd-bc7d-52a0-b7b3-ed4c4c0fca0a] Poisson Extension of a Hilbert Transform
> The normalized convolution is $(f*g)(x)=(2\pi)^{-1/2}\int_{\mathbb R}f(x-t)g(t)\,dt$. Use $Hf(x)=\pi^{-1}\operatorname{pv}\int_{\mathbb R}f(x-s)/s\,ds$. For $f\in L^2(\mathbb R)$ this is interpreted as the $L^2$ Hilbert transform. For $y>0$, write $P_y(x)=\sqrt{2/\pi}\,y/(x^2+y^2)$ and $Q_y(x)=\sqrt{2/\pi}\,x/(x^2+y^2)$.
>
> Let $f\in L^1(\mathbb R)\cap L^2(\mathbb R)$, and let $H(f)(x)$ denote its Hilbert transform. Then
>
> $$
> v(x, y)=Q_{y} * f(x)=P_{y} *(H f)(x) .
> $$
````
### After

````text
> [!theorem|d08bc374-420b-5e61-a58f-9304451f71a5.local at=e5aa6ccd-bc7d-52a0-b7b3-ed4c4c0fca0a] Hilbert transform and conjugate Poisson integral
> The normalized convolution is $(f*g)(x)=(2\pi)^{-1/2}\int_{\mathbb R}f(x-t)g(t)\,dt$. Use $Hf(x)=\pi^{-1}\operatorname{pv}\int_{\mathbb R}f(x-s)/s\,ds$. For $f\in L^2(\mathbb R)$ this is interpreted as the $L^2$ Hilbert transform. For $y>0$, write $P_y(x)=\sqrt{2/\pi}\,y/(x^2+y^2)$ and $Q_y(x)=\sqrt{2/\pi}\,x/(x^2+y^2)$.
>
> Let $f\in L^1(\mathbb R)\cap L^2(\mathbb R)$, and let $H(f)(x)$ denote its Hilbert transform. Then
>
> $$
> v(x, y)=Q_{y} * f(x)=P_{y} *(H f)(x) .
> $$
````
