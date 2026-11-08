
# Editorial records

Reading note: 15.3 Heisenberg's Uncertainty Principle.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|1027638f-2ec8-5470-94a9-e130f8e0b80a.local at=f265bf63-621d-5060-9c20-6f8ecb1f4f1a] Parseval Identity for the Unitary Fourier Transform
> Use the unitary angular-frequency Fourier transform $\widehat f(\omega)=(2\pi)^{-1/2}\int_{\mathbb R}e^{-i\omega x}f(x)\,dx$, extended from integrable square-integrable functions to all of $L^2(\mathbb R)$ by $L^2$ limits.
>
> For $f,g\in L^2(\mathbb R)$,
>
> $$
> \int_{\mathbb R}f(x)\overline{g(x)}\,dx
> =\int_{\mathbb R}\widehat f(\omega)\overline{\widehat g(\omega)}\,d\omega.
> $$
````
### After

````text
> [!theorem|1027638f-2ec8-5470-94a9-e130f8e0b80a.local at=f265bf63-621d-5060-9c20-6f8ecb1f4f1a] Parseval's Theorem
> Suppose that $f$ and $g$ are square integrable functions on the real line. Then
>
> $$
> \int_{-\infty}^{\infty} f(t) \overline{g(t)} d t=\int_{-\infty}^{\infty} \hat{f}(\omega) \overline{\hat{g}(\omega)} d \omega
> $$
>
> Here $\hat f(\omega)=(2\pi)^{-1/2}\int_{-\infty}^{\infty}e^{-i\omega x}f(x)\,dx$, extended to square integrable functions by mean-square limits.
````

## 2. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|53a7cbce-e8ac-580f-adec-f211d6ebcd85.local at=751cc718-f630-584d-b54b-90e3afaf91fa] Plancherel Norm Identity for the Unitary Fourier Transform
> Use the unitary angular-frequency Fourier transform $\widehat f(\omega)=(2\pi)^{-1/2}\int_{\mathbb R}e^{-i\omega x}f(x)\,dx$, extended from integrable square-integrable functions to all of $L^2(\mathbb R)$ by $L^2$ limits.
>
> Every $f\in L^2(\mathbb R)$ satisfies
>
> $$
> \int_{\mathbb R}|f(x)|^2\,dx=\int_{\mathbb R}|\widehat f(\omega)|^2\,d\omega.
> $$
````
### After

````text
> [!theorem|53a7cbce-e8ac-580f-adec-f211d6ebcd85.local at=751cc718-f630-584d-b54b-90e3afaf91fa] Plancherel's Theorem
> Suppose that $f$ is a square integrable function on the real line. Then
>
> $$
> \int_{-\infty}^{\infty}|f(t)|^{2} d t=\int_{-\infty}^{\infty}|\hat{f}(\omega)|^{2} d \omega
> $$
>
> Here $\hat f(\omega)=(2\pi)^{-1/2}\int_{-\infty}^{\infty}e^{-i\omega x}f(x)\,dx$, extended to square integrable functions by mean-square limits.
````

## 3. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!definition|ed5fa2e1-80e1-5e31-a743-ccf855acdb28.local at=b0d75f5e-b823-50cd-b9ea-1d50e814fd40] Mean-Square Spread of a Square-Integrable Function About a Point
> For a nonzero $f\in L^2(\mathbb R)$ and $a\in\mathbb R$, define
>
> $$
> \Delta_af=\frac{\int_{\mathbb R}(x-a)^2|f(x)|^2\,dx}{\int_{\mathbb R}|f(x)|^2\,dx}.
> $$
>
> This quantity can be infinite. When $a$ is the mean of the normalized density $|f|^2/\|f\|_2^2$, it is the variance; its square root is the standard deviation. The symbol $\Delta_a$ here denotes mean-square spread, not standard deviation.
````
### After

````text
> [!definition|ed5fa2e1-80e1-5e31-a743-ccf855acdb28.local at=b0d75f5e-b823-50cd-b9ea-1d50e814fd40] Mean-Square Spread of a Square-Integrable Function About a Point
> We now introduce the notion of uncertainty of a nonzero square integrable function $f$ about a point $a$ as
>
> $$
> \Delta_{a} f=\int_{-\infty}^{\infty}(x-a)^{2}|f(x)|^{2} d x / \int_{-\infty}^{\infty}|f(x)|^{2} d x
> $$
````

## 4. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|b2853fb2-4b61-5ff1-ae4b-2f9b2f1f032d.local at=a8920430-5d02-57d7-9ac0-111b097ee555] Heisenberg Uncertainty Inequality for the Unitary Fourier Transform
> Use the unitary angular-frequency Fourier transform $\widehat f(\omega)=(2\pi)^{-1/2}\int_{\mathbb R}e^{-i\omega x}f(x)\,dx$, extended from integrable square-integrable functions to all of $L^2(\mathbb R)$ by $L^2$ limits.
>
> Let $f\ne0$ in $L^2(\mathbb R)$ and $a,\alpha\in\mathbb R$. Define
>
> $$
> \Delta_af=\frac{\int_{\mathbb R}(x-a)^2|f(x)|^2\,dx}{\|f\|_2^2},\qquad
> \Delta_\alpha\widehat f=\frac{\int_{\mathbb R}(\omega-\alpha)^2|\widehat f(\omega)|^2\,d\omega}{\|\widehat f\|_2^2}.
> $$
>
> If both moments are finite, then $\Delta_af\,\Delta_\alpha\widehat f\ge1/4$. If either is infinite, the inequality holds in the extended sense. At the respective means this is the standard-deviation inequality $\sigma_x\sigma_\omega\ge1/2$.
````
### After

````text
> [!theorem|b2853fb2-4b61-5ff1-ae4b-2f9b2f1f032d.local at=a8920430-5d02-57d7-9ac0-111b097ee555] Heisenberg's Inequality
> Suppose that $f(x)$ is a square integrable function on the real line that is not identically 0. Then
> $$
> \Delta_{a} f \Delta_{\alpha} \hat{f} \geq \frac{1}{4}
> $$
>
> for all $a$ on the $x$-axis and all $\alpha$ on the $\omega$-axis.
>
> Here $\hat f(\omega)=(2\pi)^{-1/2}\int_{-\infty}^{\infty}e^{-i\omega x}f(x)\,dx$, extended to square integrable functions by mean-square limits. The quantities are $\Delta_af=\int(x-a)^2|f(x)|^2\,dx/\int|f(x)|^2\,dx$ and $\Delta_\alpha\hat f=\int(\omega-\alpha)^2|\hat f(\omega)|^2\,d\omega/\int|\hat f(\omega)|^2\,d\omega$, allowing infinite values.
````
