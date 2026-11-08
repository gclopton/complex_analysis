
# Editorial records

Reading note: 8.4 The Heat Equation and Gauss's Kernel.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem] Gaussian Convolution Solution of the Heat Equation on the Real Line
> The normalized convolution is $(f*g)(x)=(2\pi)^{-1/2}\int_{\mathbb R}f(x-t)g(t)\,dt$. Let $c>0$, $t>0$, and let the initial data $f$ be bounded and piecewise continuous. For $u_t=c^2u_{xx}$ on $\mathbb R$, the formula below gives a bounded solution tending to $f(x)$ at its continuity points as $t\downarrow0$.
>
> The solution with initial temperature distribution $f$ is the convolution of $f$ with the heat kernel. More explicitly,
>
> $$
> u(x, t)=\frac{1}{c \sqrt{2 t}} e^{-x^{2} / 4 c^{2} t} * f=\frac{1}{2 c \sqrt{\pi t}} \int_{-\infty}^{\infty} f(s) e^{-(x-s)^{2} / 4 c^{2} t} d s
> $$
````
### After

````text
> [!theorem] Gaussian Convolution Solution of the Heat Equation on the Real Line
> The normalized convolution is $(f*g)(x)=(2\pi)^{-1/2}\int_{\mathbb R}f(x-t)g(t)\,dt$. Let $c>0$, $t>0$, and let the initial data $f$ be bounded and piecewise continuous. For $u_t=c^2u_{xx}$ on $\mathbb R$, the formula below gives a bounded solution tending to $f(x)$ at its continuity points as $t\downarrow0$.
>
> The solution with initial temperature distribution $f$ is the convolution of $f$ with the heat kernel. More explicitly,
>
> $$
> u(x, t)=\frac{1}{c \sqrt{2 t}} e^{-x^{2} / 4 c^{2} t} * f=\frac{1}{2 c \sqrt{\pi t}} \int_{-\infty}^{\infty} f(s) e^{-(x-s)^{2} / 4 c^{2} t} d s
> $$
````
