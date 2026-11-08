
# Editorial records

Reading note: 13.6 Legendre Polynomials and Legendre Series Expansions.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!identity|fb2e5281-924b-5151-a932-01eef37eb124.local at=b9818235-2688-508c-bd89-af0c22d81da8] Rodrigues’ formula for Legendre polynomials
> For every nonnegative integer $n$, the Legendre polynomial normalized by $P_n(1)=1$ satisfies
> $$
> P_n(x)=\frac1{2^n n!}\frac{d^n}{dx^n}(x^2-1)^n.
> $$
````
### After

````text
> [!identity|fb2e5281-924b-5151-a932-01eef37eb124.local at=b9818235-2688-508c-bd89-af0c22d81da8] Rodrigues' Formula
> For $n=0,1,2, \ldots$, we have
>
> $$
> P_{n}(x)=\frac{1}{2^{n} n!} \frac{d^{n}}{d x^{n}}\left(x^{2}-1\right)^{n}
> $$
>
> Here $P_n$ is the Legendre polynomial normalized by $P_n(1)=1$.
````

## 2. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!identity|3812d1e6-7ecb-530a-a502-6d0f0a70d31f.local at=dbe9fd0e-5c32-5aa3-a0b2-b81c57582e0a] Bonnet’s three-term recurrence for Legendre polynomials
> For integers $n\ge1$, the Legendre polynomials normalized by $P_k(1)=1$ satisfy
> $$
> (n+1)P_{n+1}(x)+nP_{n-1}(x)=(2n+1)xP_n(x).
> $$
````
### After

````text
> [!identity|3812d1e6-7ecb-530a-a502-6d0f0a70d31f.local at=dbe9fd0e-5c32-5aa3-a0b2-b81c57582e0a] Bonnet's Recurrence Relation
> For $n=1,2, \ldots$ we have
>
> $$
> (n+1) P_{n+1}(x)+n P_{n-1}(x)=(2 n+1) x P_{n}(x)
> $$
>
> Here $P_n$ is the Legendre polynomial normalized by $P_n(1)=1$.
````

## 3. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|f402a21f-6687-5549-88bf-1527db76b6fc.local at=50b109e5-0896-5f49-b976-0d98ef1a9fe0] Orthogonality and squared norms of Legendre polynomials
> For nonnegative integers $m,n$, let $P_m,P_n$ be the Legendre polynomials normalized by $P_k(1)=1$. Then
> $$
> \int_{-1}^1P_m(x)P_n(x)\,dx=
> \begin{cases}0,&m\ne n,\\[2pt]\dfrac2{2n+1},&m=n.\end{cases}
> $$
````
### After

````text
> [!theorem|f402a21f-6687-5549-88bf-1527db76b6fc.local at=50b109e5-0896-5f49-b976-0d98ef1a9fe0] Orthogonality of Legendre Polynomials
> Let $P_n$ denote the Legendre polynomial normalized by $P_n(1)=1$, for nonnegative integers $n$.
>
> (i) If $m \neq n$, then
>
> $$
> \int_{-1}^{1} P_{m}(x) P_{n}(x) d x=0
> $$
>
> (ii) For each $n$, we have
>
> $$
> \int_{-1}^{1} P_{n}^{2}(x) d x=\frac{2}{2 n+1}
> $$
````

## 4. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|5a845fe2-5dc9-55dd-b849-8dd528c0aef7.local at=0ce2435d-4e30-5b6a-9f67-51d5d3ec6ed2] Pointwise convergence and coefficients of a Legendre series
> Let $f$ be piecewise smooth on $[-1,1]$, with finitely many continuously differentiable pieces and finite one-sided limits of $f$ and $f'$ at their endpoints. For the Legendre polynomials $P_j$ normalized by $P_j(1)=1$, set
> $$
> A_j=\frac{2j+1}{2}\int_{-1}^1f(t)P_j(t)\,dt.
> $$
> At each $-1<x<1$,
> $$
> \sum_{j=0}^{\infty}A_jP_j(x)=\frac{f(x+)+f(x-)}2.
> $$
> At continuity points this equals $f(x)$. This statement makes no endpoint-convergence assertion.
````
### After

````text
> [!theorem|5a845fe2-5dc9-55dd-b849-8dd528c0aef7.local at=0ce2435d-4e30-5b6a-9f67-51d5d3ec6ed2] Legendre Series
> Suppose that $f$ is a piecewise smooth function on the interval $-1 \leq x \leq 1$. Then $f$ has the Legendre series expansion
>
> $$
> f(x)=\sum_{j=0}^{\infty} A_{j} P_{j}(x)
> $$
>
> where
>
> $$
> A_{j}=\frac{2 j+1}{2} \int_{-1}^{1} f(x) P_{j}(x) d x
> $$
>
> For $x$ in the (open) interval ( $-1,1$ ), the Legendre series converges to $f(x)$ if $f$ is continuous at $x$, and to $(f(x+)+f(x-)) / 2$ otherwise.
>
> Here $P_n$ is the Legendre polynomial normalized by $P_n(1)=1$.
````

## 5. Restore source wording; retain only the actual correction.

### Before

````text
The nonnegativity is the Fejér inequality. [Corrected: the printed upper bound $1/(1-x)$ fails already when $n=0$ and $x<0$. The valid upper bound $2/(1-x)$ suffices for the following convergence tests.] For the upper bound, use Laplace’s integral formula and the finite geometric sum: with $z=x+i\sqrt{1-x^2}\cos\theta$, one has $|z|\le1$ and $|1-z|\ge1-x$, so $|\sum_{k=0}^n z^k|\le2/(1-x)$.
````
### After

````text
The nonnegativity is the Fejér inequality.
````

## 6. Move editorial commentary to this record.

### Before

````text
*Editorial reference repair: the original hints cite source §§2.7–2.8, which are not present in this vault’s Fourier-series chapter. The relevant convergence arguments are named locally instead.*
````
### After

````text

````
