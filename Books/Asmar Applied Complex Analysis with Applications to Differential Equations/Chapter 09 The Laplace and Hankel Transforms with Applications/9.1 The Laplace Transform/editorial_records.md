
# Editorial records

Reading note: 9.1 The Laplace Transform.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!definition|b9229dbe-41fd-56e8-be6f-4f260e3f4008.local at=6daf84c8-5a7e-5cae-afd2-aa1343710d2b] One-Sided Laplace Transform
> For a locally integrable function $f:[0,\infty)\to\mathbb C$, its one-sided Laplace transform is
>
> $$
> F(s)=\mathcal Lf(s)=\int_0^\infty f(t)e^{-st}\,dt
> $$
>
> where the improper integral converges. The parameter $s$ may be real or complex; absolute convergence holds in the right half-plane specified by an exponential growth bound.
````
### After

````text
> [!definition|b9229dbe-41fd-56e8-be6f-4f260e3f4008.local at=6daf84c8-5a7e-5cae-afd2-aa1343710d2b] One-Sided Laplace Transform
> Suppose that $f(t)$ is defined for all $t \geq 0$. The Laplace transform of $f$ is the function
> As a convention, functions $f, g, \ldots$ are defined for $t \geq 0$ and their transforms $F, G, \ldots$ are defined on the $s$-axis.
>
> $$
> \mathcal{L}(f)(s)=\int_{0}^{\infty} f(t) e^{-s t} d t
> $$
>
> Another commonly used notation for $\mathcal{L}(f)(s)$ is $F(s)$.
````

## 2. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!definition|9f1b84c9-6029-5529-bca1-cb463addb25a.local at=abe4fc0d-2f18-5027-9c50-28ca06c1962a] Global Exponential Bound on the Positive Half-Line
> A function $f:[0,\infty)\to\mathbb C$ satisfies a global exponential bound if there are constants $M>0$ and $a>0$ such that $|f(t)|\leq Me^{at}$ for every $t\geq0$.
````
### After

````text
> [!definition|9f1b84c9-6029-5529-bca1-cb463addb25a.local at=abe4fc0d-2f18-5027-9c50-28ca06c1962a] Exponential Order
> We say that $f$ is of exponential order if there exist positive numbers $a$ and $M$ such that
>
> $$
> |f(t)| \leq M e^{a t} \text { for all } t \geq 0
> $$
````

## 3. Remove assistant commentary comparing conventions; restore the author’s actual definition.

### Before

````text
The text calls this global bound “of exponential order.” It is stronger near zero than the convention that imposes the bound only for sufficiently large $t$.
````
### After

````text

````

## 4. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|e4f15047-1a89-56ba-a366-4da977816f96.local at=6abac71b-f0a9-5637-9140-8754976c1d5d] Existence of the Laplace Transform under an Exponential Bound
> Write $\mathcal Lf(s)=\int_0^\infty f(t)e^{-st}\,dt$ for the one-sided Laplace transform.
>
> If $f$ is piecewise continuous on every bounded subinterval of $[0,\infty)$ and $|f(t)|\leq Me^{at}$ for constants $M>0$ and real $a$, then $\mathcal Lf(s)$ converges absolutely for every complex $s$ with $\operatorname{Re}s>a$.
````
### After

````text
> [!theorem|e4f15047-1a89-56ba-a366-4da977816f96.local at=6abac71b-f0a9-5637-9140-8754976c1d5d] Existence of the Laplace Transform
> Write $\mathcal Lf(s)=\int_0^\infty f(t)e^{-st}\,dt$.
>
> Suppose that $f$ is piecewise continuous on the interval $[0, \infty)$ and of exponential order with $|f(t)| \leq M e^{a t}$ for all $t \geq 0$. Then $\mathcal{L}(f)(s)$ exists for all $s>a$.
````

## 5. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|c06973b1-0111-5f40-ac1e-b83269e28a8a.local at=a6e0737b-3255-5f46-aa18-76c15ffbea45] Linearity of the One-Sided Laplace Transform
> Write $\mathcal Lf(s)=\int_0^\infty f(t)e^{-st}\,dt$ for the one-sided Laplace transform.
>
> For constants $\alpha,\beta\in\mathbb C$ and functions $f,g$ whose transforms converge at $s$,
>
> $$
> \mathcal L(\alpha f+\beta g)(s)=\alpha\mathcal Lf(s)+\beta\mathcal Lg(s).
> $$
````
### After

````text
> [!theorem|c06973b1-0111-5f40-ac1e-b83269e28a8a.local at=a6e0737b-3255-5f46-aa18-76c15ffbea45] Linearity
> Write $\mathcal Lf(s)=\int_0^\infty f(t)e^{-st}\,dt$.
>
> Assume the transforms exist at the value of $s$ considered.
>
> $$
> \begin{aligned}
> & \text { If } f \text { and } g \text { are functions and } \alpha \text { and } \beta \text { are numbers, then } \\
> & \qquad \mathcal{L}(\alpha f+\beta g)=\alpha \mathcal{L}(f)+\beta \mathcal{L}(g)
> \end{aligned}
> $$
````

## 6. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|675e2821-a2b3-5efe-92ec-83d7bd866f90.local at=92279ffe-1f63-5248-a326-a14e135421db] Exponential Multiplication and Frequency Shifts of the Laplace Transform
> Write $\mathcal Lf(s)=\int_0^\infty f(t)e^{-st}\,dt$ for the one-sided Laplace transform.
>
> Let $f$ be piecewise continuous on bounded intervals of $[0,\infty)$, with $|f(t)|\leq Me^{at}$. For real $\alpha$ and $s>a+\alpha$,
>
> $$
> \mathcal L(e^{\alpha t}f(t))(s)=F(s-\alpha),\qquad F(s)=\mathcal Lf(s).
> $$
````
### After

````text
> [!theorem|675e2821-a2b3-5efe-92ec-83d7bd866f90.local at=92279ffe-1f63-5248-a326-a14e135421db] Shifting on the $s$-Axis
> Write $\mathcal Lf(s)=\int_0^\infty f(t)e^{-st}\,dt$.
>
> Suppose that $f$ is piecewise continuous and of exponential order. Let $\alpha$ be a real number and $a$ be such that $|f(t)|\leq Me^{at}$ for $t\geq0$ and some $M>0$. For $s>a+\alpha$, we have
>
> $$
> \mathcal{L}\left(e^{\alpha t} f(t)\right)(s)=F(s-\alpha)
> $$
>
> where $F(s)=\mathcal{L}(f(t))(s)$.
````

## 7. Move correction/commentary into the separate editorial record; keep the actual correction in the reading text.

### Before

````text
[Corrected: the printed inversion formulas have $e^{-zt}$; inversion requires $e^{zt}$.]
````
### After

````text

````
