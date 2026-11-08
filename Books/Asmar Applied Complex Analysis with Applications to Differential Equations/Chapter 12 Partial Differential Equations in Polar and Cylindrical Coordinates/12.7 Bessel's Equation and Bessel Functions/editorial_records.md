
# Editorial records

Reading note: 12.7 Bessel's Equation and Bessel Functions.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!equation|3f367ba5-7274-57c5-9f48-982e8ed1dfc3.local at=299d01d5-9a3e-50af-8a46-629dbeb9d5ed] General solution of Bessel’s differential equation on the positive axis
> For a fixed real order $p\ge0$, the general solution of
> $$
> x^2y''+xy'+(x^2-p^2)y=0,\qquad x>0,
> $$
> is
> $$
> y(x)=c_1J_p(x)+c_2Y_p(x),
> $$
> where $c_1,c_2$ are arbitrary constants and $J_p,Y_p$ are the Bessel functions of the first and second kinds. If $p$ is not an integer, an alternative fundamental pair is $J_p,J_{-p}$:
> $$
> y(x)=c_1J_p(x)+c_2J_{-p}(x).
> $$
````
### After

````text
> [!equation|3f367ba5-7274-57c5-9f48-982e8ed1dfc3.local at=299d01d5-9a3e-50af-8a46-629dbeb9d5ed] General Solution of Bessel's Equation
> Let $p\geq0$.
>
> The general solution of Bessel's equation $x^2y''+xy'+(x^2-p^2)y=0$, $x>0$, of order $p$ is
>
> $$
> y(x)=c_{1} J_{p}(x)+c_{2} Y_{p}(x)
> $$
>
> where $J_p$ and $Y_p$ are the Bessel functions of the first and second kinds. When $p$ is not an integer, a general solution is also given by
>
> $$
> y(x)=c_{1} J_{p}(x)+c_{2} J_{-p}(x),
> $$
>
> where $J_p$ and $J_{-p}$ are Bessel functions of the first kind.
````

## 2. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!definition|3eb52e35-d2a0-5902-ab98-9f125f2a5d2a.local at=b2fd50e8-8398-5a9d-9334-bc1f95265c68] Bessel function of the second kind
> For $x>0$ and noninteger real order $p\ge0$, define
> $$
> Y_p(x)=\frac{J_p(x)\cos(\pi p)-J_{-p}(x)}{\sin(\pi p)},
> $$
> where $J_\nu$ is the Bessel function of the first kind. For a nonnegative integer $n$, define
> $$
> Y_n(x)=\lim_{\nu\to n}Y_\nu(x).
> $$
> The limit exists. These are the Bessel functions of the second kind; $J_p$ and $Y_p$ are linearly independent solutions of Bessel's equation on $(0,\infty)$.
````
### After

````text
> [!definition|3eb52e35-d2a0-5902-ab98-9f125f2a5d2a.local at=b2fd50e8-8398-5a9d-9334-bc1f95265c68] Bessel function of the second kind
> For $x>0$ and real $p\geq0$, let $J_p$ denote the Bessel function of the first kind.
>
> $$
> Y_{p}(x)=\frac{J_{p}(x) \cos p \pi-J_{-p}(x)}{\sin p \pi} \quad(p \text { not an integer }) .
> $$
>
> Since $J_{p}$ and $J_{-p}$ are in this case linearly independent solutions of Bessel's equation, it follows from this formula that $Y_{p}$ is also a solution of Bessel's equation that is linearly independent of $J_{p}$. The function $Y_{p}$ is called a Bessel function of the second kind of order $p$. For integer $p$, this function is constructed by a limiting process from the noninteger values as follows:
>
> $$
> Y_{p}=\lim _{\nu \rightarrow p} Y_{\nu}
> $$
````

## 3. Move correction/commentary into the separate editorial record; keep the actual correction in the reading text.

### Before

````text
[Corrected: the printed result has an extra factor of $2$; the formula above gives the length of both loops.]
````
### After

````text

````

## 4. Move correction/commentary into the separate editorial record; keep the actual correction in the reading text.

### Before

````text
[Corrected: the printed formula omits the factor $1/2$ in the logarithm; the standard normalization of $Y_0$ requires $\ln(x/2)$.]
````
### After

````text

````
