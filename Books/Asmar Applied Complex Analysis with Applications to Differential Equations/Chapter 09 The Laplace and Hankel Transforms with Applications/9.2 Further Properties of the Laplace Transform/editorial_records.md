
# Editorial records

Reading note: 9.2 Further Properties of the Laplace Transform.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|63bfac33-dcc2-5db8-8768-4c1b04c5fcd5.local at=02ea2f7f-2e27-57f8-9be9-30593f719031] Causal Time Delay in the One-Sided Laplace Transform
> Write $\mathcal Lf(s)=\int_0^\infty f(t)e^{-st}\,dt$ for the one-sided Laplace transform.
>
> Let $a>0$, let $\mathcal U_0(t)=0$ for $t<0$ and $1$ for $t\geq0$, and suppose $F(s)=\mathcal Lf(s)$ converges. Define the delayed function to be zero for $t<a$. Then
>
> $$
> \mathcal L\!\left(\mathcal U_0(t-a)f(t-a)\right)(s)=e^{-as}F(s).
> $$
````
### After

````text
> [!theorem|63bfac33-dcc2-5db8-8768-4c1b04c5fcd5.local at=02ea2f7f-2e27-57f8-9be9-30593f719031] Shifting on the $t$-Axis
> Write $\mathcal Lf(s)=\int_0^\infty f(t)e^{-st}\,dt$.
>
> Let $\mathcal U_0(t)$ be zero for $t<0$ and one for $t\geq0$. Suppose $F(s)$ converges; define the delayed function to be zero for $t<a$.
>
> If $a$ is a positive real number, then
>
> $$
> \mathcal{L}\left(\mathcal{U}_{0}(t-a) f(t-a)\right)(s)=e^{-a s} F(s)
> $$
>
> where $F(s)=\mathcal{L}(f(t))(s)$.
````

## 2. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!definition|8f9d61fa-5533-5e73-9f56-a19583ce2300.local at=25d71684-89c7-59ba-a2fb-af40888316c9] Causal Convolution on the Positive Half-Line
> For piecewise continuous functions $f,g:[0,\infty)\to\mathbb C$, their causal convolution is
>
> $$
> (f*g)(t)=\int_0^t f(t-\tau)g(\tau)\,d\tau,\qquad t\geq0.
> $$
````
### After

````text
> [!definition|8f9d61fa-5533-5e73-9f56-a19583ce2300.local at=25d71684-89c7-59ba-a2fb-af40888316c9] Causal Convolution on the Positive Half-Line
> Given two functions $f$ and $g$, piecewise continuous for $t\geq0$, we define their convolution $f * g(t)$ by
>
> $$
> f * g(t)=\int_{0}^{t} f(t-\tau) g(\tau) d \tau \quad \text { for all } t \geq 0
> $$
````

## 3. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|a8a05283-149f-5ec1-b9df-f1a4eb92aee1.local at=616ada6f-378a-5753-8ddf-a2f3fca4f1e6] Laplace Transform of a Causal Convolution
> Write $\mathcal Lf(s)=\int_0^\infty f(t)e^{-st}\,dt$ for the one-sided Laplace transform.
>
> Let $f,g$ be piecewise continuous on bounded intervals, with exponential bounds $|f(t)|\leq M_fe^{at}$ and $|g(t)|\leq M_ge^{bt}$. For $s>\max(a,b)$ and $(f*g)(t)=\int_0^t f(t-\tau)g(\tau)\,d\tau$,
>
> $$
> \mathcal L(f*g)(s)=\mathcal Lf(s)\,\mathcal Lg(s).
> $$
````
### After

````text
> [!theorem|a8a05283-149f-5ec1-b9df-f1a4eb92aee1.local at=616ada6f-378a-5753-8ddf-a2f3fca4f1e6] Transforms of Convolutions
> Write $\mathcal Lf(s)=\int_0^\infty f(t)e^{-st}\,dt$.
>
> Here $(f*g)(t)=\int_0^t f(t-\tau)g(\tau)\,d\tau$; take $s$ greater than the exponential growth rates of both functions.
>
> Suppose that $f$ and $g$ are piecewise continuous and of exponential order; then
>
> $$
> \mathcal{L}(f * g)=\mathcal{L}(f) \mathcal{L}(g)
> $$
````
