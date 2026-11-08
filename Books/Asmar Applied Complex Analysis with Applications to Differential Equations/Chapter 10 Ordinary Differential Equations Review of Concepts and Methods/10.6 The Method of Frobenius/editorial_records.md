
# Editorial records

Reading note: 10.6 The Method of Frobenius.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!definition|fe802857-e36c-5f71-a6c2-6811da025301.local at=2f51e866-9c22-53d2-abfd-ab33ef363c92] Frobenius Series about the Origin
> For $x>0$ and exponent $r$,
>
> $$
> y=x^{r}\left(a_{0}+a_{1} x+a_{2} x^{2}+\cdots\right)=\sum_{m=0}^{\infty} a_{m} x^{r+m}
> $$
>
> with $a_{0} \neq 0$. The analytic power-series factor is required to have positive radius of convergence.
````
### After

````text
> [!definition|fe802857-e36c-5f71-a6c2-6811da025301.local at=2f51e866-9c22-53d2-abfd-ab33ef363c92] Frobenius Series about the Origin
> For $x>0$ and exponent $r$,
>
> $$
> y=x^{r}\left(a_{0}+a_{1} x+a_{2} x^{2}+\cdots\right)=\sum_{m=0}^{\infty} a_{m} x^{r+m}
> $$
>
> with $a_{0} \neq 0$. Such a series is called a Frobenius series. The power series is assumed to have positive radius of convergence.
````

## 2. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|4c10f688-34c5-5087-9fb3-d3a4eb8115f3.local at=0df8f924-a00e-566d-b7a8-9531941750cf] First Frobenius Solution at a Regular Singular Point
> Let $P(x)=xp(x)$ and $Q(x)=x^2q(x)$ extend analytically to $x=0$, with power series converging for $|x|<R$, $R>0$. Write $p_0=P(0)$ and $q_0=Q(0)$. Treat the intervals $0<x<R$ and $-R<x<0$ separately; for complex exponents use $|x|^r=e^{r\ln|x|}$.
>
> If $x=0$ is a regular singular point of the equation
>
> $$
> y^{\prime \prime}+p(x) y^{\prime}+q(x) y=0 .
> $$
>
> then one solution is of the form
>
> $$
> y_{1}=|x|^{r_{1}}\left(a_{0}+a_{1} x+a_{2} x^{2}+\cdots\right) . \quad a_{0} \neq 0
> $$
>
> where $r_{1}$ is a root of $r(r-1)+p_0r+q_0=0$. with the convention that $r_{1}$ is the larger of the two roots when both roots are real.
>
>
>
> The analytic factor converges for $|x|<R$.
````
### After

````text
> [!theorem|4c10f688-34c5-5087-9fb3-d3a4eb8115f3.local at=0df8f924-a00e-566d-b7a8-9531941750cf] Frobenius Method First Solution
> Let $P(x)=xp(x)$ and $Q(x)=x^2q(x)$ extend analytically to $x=0$, with power series converging for $|x|<R$, $R>0$. Write $p_0=P(0)$ and $q_0=Q(0)$. Treat the intervals $0<x<R$ and $-R<x<0$ separately; for complex exponents use $|x|^r=e^{r\ln|x|}$.
>
> If $x=0$ is a regular singular point of the equation
>
> $$
> y^{\prime \prime}+p(x) y^{\prime}+q(x) y=0 .
> $$
>
> then one solution is of the form
>
> $$
> y_{1}=|x|^{r_{1}}\left(a_{0}+a_{1} x+a_{2} x^{2}+\cdots\right) . \quad a_{0} \neq 0
> $$
>
> where $r_{1}$ is a root of $r(r-1)+p_0r+q_0=0$. with the convention that $r_{1}$ is the larger of the two roots when both roots are real.
>
> The analytic factor converges for $|x|<R$.
````

## 3. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|a6cbc45d-0dc2-5f2c-abd7-3b407939e739.local at=006d8e52-423a-5e14-afc1-429cb581b13c] Frobenius Fundamental Solutions and Logarithmic Resonance
> Let $P(x)=xp(x)$ and $Q(x)=x^2q(x)$ be analytic for $|x|<R$, with $R>0$. Set $p_0=P(0)$, $q_0=Q(0)$, and let $r_1,r_2$ solve $r(r-1)+p_0r+q_0=0$, ordered $r_1\geq r_2$ if real. Work separately on either side of zero; interpret complex powers as $|x|^r=e^{r\ln|x|}$. All analytic series factors below converge for $|x|<R$.
>
> Suppose that $x=0$ is a regular singular point of the differential equation
>
> $$
> y^{\prime \prime}+p(x) y^{\prime}+q(x) y=0 .
> $$
>
> and let $r_{1}$ and $r_{2}$ denote the indicial roots. The differential equation has two linearly independent solutions $y_{1}$ and $y_{2}$, as we now describe.
> Case 1. If $r_{1}-r_{2}$ is not an integer. then
>
> $$
> y_{1}=|x|^{r_{1}} \sum_{m=0}^{\infty} a_{m} x^{m} . \quad y_{2}=|x|^{r_{2}} \sum_{m=0}^{\infty} b_{m} x^{m} . \quad a_{0} \neq 0 \text { and } b_{0} \neq 0 .
> $$
>
> Case 2. If $r=r_{1}=r_{2}$, then
>
> $$
> y_{1}=|x|^{r} \sum_{m=0}^{\infty} a_{m} x^{m}, \quad y_{2}=y_{1} \ln |x|+|x|^{r} \sum_{m=1}^{\infty} b_{m} x^{m} . \quad a_{0} \neq 0 .
> $$
>
> Case 3. If $r_{1}-r_{2}$ is a positive integer, with $r_{1} \geq r_{2}$, then
>
> $$
> y_{1}=|x|^{r_{1}} \sum_{m=0}^{\infty} a_{m} x^{m}, \quad y_{2}=k y_{1} \ln |x|+|x|^{r_{2}} \sum_{m=0}^{\infty} b_{m} x^{m} .
> $$
>
> where $a_{0} \neq 0, b_{0} \neq 0$ ( $k$ may or may not be 0 ).
````
### After

````text
> [!theorem|a6cbc45d-0dc2-5f2c-abd7-3b407939e739.local at=006d8e52-423a-5e14-afc1-429cb581b13c] The Frobenius Method
> Let $P(x)=xp(x)$ and $Q(x)=x^2q(x)$ be analytic for $|x|<R$, with $R>0$. Set $p_0=P(0)$, $q_0=Q(0)$, and let $r_1,r_2$ solve $r(r-1)+p_0r+q_0=0$, ordered $r_1\geq r_2$ if real. Work separately on either side of zero; interpret complex powers as $|x|^r=e^{r\ln|x|}$. All analytic series factors below converge for $|x|<R$.
>
> Suppose that $x=0$ is a regular singular point of the differential equation
>
> $$
> y^{\prime \prime}+p(x) y^{\prime}+q(x) y=0 .
> $$
>
> and let $r_{1}$ and $r_{2}$ denote the indicial roots. The differential equation has two linearly independent solutions $y_{1}$ and $y_{2}$, as we now describe.
> Case 1. If $r_{1}-r_{2}$ is not an integer. then
>
> $$
> y_{1}=|x|^{r_{1}} \sum_{m=0}^{\infty} a_{m} x^{m} . \quad y_{2}=|x|^{r_{2}} \sum_{m=0}^{\infty} b_{m} x^{m} . \quad a_{0} \neq 0 \text { and } b_{0} \neq 0 .
> $$
>
> Case 2. If $r=r_{1}=r_{2}$, then
>
> $$
> y_{1}=|x|^{r} \sum_{m=0}^{\infty} a_{m} x^{m}, \quad y_{2}=y_{1} \ln |x|+|x|^{r} \sum_{m=1}^{\infty} b_{m} x^{m} . \quad a_{0} \neq 0 .
> $$
>
> Case 3. If $r_{1}-r_{2}$ is a positive integer, with $r_{1} \geq r_{2}$, then
>
> $$
> y_{1}=|x|^{r_{1}} \sum_{m=0}^{\infty} a_{m} x^{m}, \quad y_{2}=k y_{1} \ln |x|+|x|^{r_{2}} \sum_{m=0}^{\infty} b_{m} x^{m} .
> $$
>
> where $a_{0} \neq 0, b_{0} \neq 0$ ( $k$ may or may not be 0 ).
````

## 4. Move correction/commentary into the separate editorial record; keep the actual correction in the reading text.

### Before

````text
[Clarified: for $n=0$, division by $x$ yields $y^{\prime\prime}-y^{\prime}=0$, which has an ordinary point at zero; the requested regular-singular classification applies to $n\geq1$.]
````
### After

````text

````
