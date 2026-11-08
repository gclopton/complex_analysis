
# Editorial records

Reading note: 10.3 Linear Ordinary Differential Equations with Nonconstant Coefficients.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!rule|f272087c-bbd0-5309-a2f3-ce52cf655a7a.local at=ca9cb3db-25df-58e8-b879-5ec5e7e621a5] Reduction of Order for a Second-Order Homogeneous Linear ODE
> Let $p,q$ be continuous on an interval $I$ and let $y_1$ be a solution of $y^{\prime\prime}+p(x)y^{\prime}+q(x)y=0$ that has no zeros on $I$. A linearly independent second solution is
>
> $$
> y_2(x)=y_1(x)\int\frac{e^{-\int p(x)\,dx}}{y_1(x)^2}\,dx.
> $$
>
> Use a fixed antiderivative in the exponential. The formula applies on intervals where $y_1
> e0$; extension across a zero requires a separate argument.
````
### After

````text
> [!rule|f272087c-bbd0-5309-a2f3-ce52cf655a7a.local at=ca9cb3db-25df-58e8-b879-5ec5e7e621a5] Reduction of Order Formula
> Let $p,q$ be continuous on an interval where the known solution $y_1$ of $y^{\prime\prime}+p(x)y^{\prime}+q(x)y=0$ does not vanish.
>
> A second linearly independent solution of $y^{\prime\prime}+p(x)y^{\prime}+q(x)y=0$ given $y_{1}$ is
>
> $$
> y_{2}=y_{1} \int \frac{e^{-\int p(x) d x}}{y_{1}^{2}} d x .
> $$
>
> Before you apply this formula, be sure that your equation is in standard form.
````

## 2. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!rule|8581a96b-e43e-5712-883a-446d14e9edc5.local at=79e898a5-d4a0-5a18-9dc1-7ffbb0360372] Variation of Parameters for a Second-Order Linear ODE
> Assume $p,q,g$ are continuous on an interval $I$, and take a fundamental pair $y_1,y_2$ of the associated homogeneous equation, so their Wronskian is nowhere zero on $I$.
>
> A particular solution of $y^{\prime\prime}+p(x)y^{\prime}+q(x)y=g(x)$ is given by
>
> $$
> y_{p}=y_{1} \int \frac{-y_{2} g(x)}{W\left(y_{1}, y_{2}\right)} d x+y_{2} \int \frac{y_{1} g(x)}{W\left(y_{1}, y_{2}\right)} d x
> $$
>
> where $y_{1}$ and $y_{2}$ are linearly independent solutions of $y^{\prime\prime}+p(x)y^{\prime}+q(x)y=0$, and $W\left(y_{1}, y_{2}\right)= y_{1} y_{2}^{\prime}-y_{1}^{\prime} y_{2}$ is the Wronskian of $y_{1}$ and $y_{2}$.
````
### After

````text
> [!rule|8581a96b-e43e-5712-883a-446d14e9edc5.local at=79e898a5-d4a0-5a18-9dc1-7ffbb0360372] Variation of Parameters Formula
> Assume $p,q,g$ are continuous on an interval $I$, and take a fundamental pair $y_1,y_2$ of the associated homogeneous equation, so their Wronskian is nowhere zero on $I$.
>
> A particular solution of $y^{\prime\prime}+p(x)y^{\prime}+q(x)y=g(x)$ is given by
>
> $$
> y_{p}=y_{1} \int \frac{-y_{2} g(x)}{W\left(y_{1}, y_{2}\right)} d x+y_{2} \int \frac{y_{1} g(x)}{W\left(y_{1}, y_{2}\right)} d x
> $$
>
> where $y_{1}$ and $y_{2}$ are linearly independent solutions of $y^{\prime\prime}+p(x)y^{\prime}+q(x)y=0$, and $W\left(y_{1}, y_{2}\right)= y_{1} y_{2}^{\prime}-y_{1}^{\prime} y_{2}$ is the Wronskian of $y_{1}$ and $y_{2}$.
````

## 3. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!rule|ddb62b20-b6b9-5464-af10-4b6d045eb481.local at=eb679021-cd50-5280-861b-e10948fd15ec] General Solutions of the Second-Order Cauchy–Euler Equation
> Work on a connected interval contained in $x>0$ or $x<0$. Constants on the two sides of zero are independent.
>
> Consider $x^2y^{\prime\prime}+\alpha xy^{\prime}+\beta y=0$ with real constants $\alpha,\beta$ and its indicial equation, which we write as
>
> $$
> r^{2}+(\alpha-1) r+\beta=0
> $$
>
> Let $r_{1}$ and $r_{2}$ denote the indicial roots. The general solution $y$ of this equation is given by the following cases.
> Case I If $r_{1}$ and $r_{2}$ are distinct real roots, then
>
> $$
> y=c_{1}|x|^{r_{1}}+c_{2}|x|^{r_{2}}
> $$
>
> Case II If $r_{1}=r_{2}$, then
>
> $$
> y=\left(c_{1}+c_{2} \ln |x|\right)|x|^{r_{1}}
> $$
>
> Case III If $r_{1}$ and $r_{2}$ are complex conjugate roots with $r_{1}=a+i b$, then
>
> $$
> y=|x|^{a}\left[c_{1} \cos (b \ln |x|)+c_{2} \sin (b \ln |x|)\right]
> $$
>
> Clearly when $x>0$ we may drop the absolute values.
````
### After

````text
> [!rule|ddb62b20-b6b9-5464-af10-4b6d045eb481.local at=eb679021-cd50-5280-861b-e10948fd15ec] General Solution of Euler's Equation
> Work on a connected interval contained in $x>0$ or $x<0$. Constants on the two sides of zero are independent.
>
> Consider $x^2y^{\prime\prime}+\alpha xy^{\prime}+\beta y=0$ with real constants $\alpha,\beta$ and its indicial equation, which we write as
>
> $$
> r^{2}+(\alpha-1) r+\beta=0
> $$
>
> Let $r_{1}$ and $r_{2}$ denote the indicial roots. The general solution $y$ of this equation is given by the following cases.
> Case I If $r_{1}$ and $r_{2}$ are distinct real roots, then
>
> $$
> y=c_{1}|x|^{r_{1}}+c_{2}|x|^{r_{2}}
> $$
>
> Case II If $r_{1}=r_{2}$, then
>
> $$
> y=\left(c_{1}+c_{2} \ln |x|\right)|x|^{r_{1}}
> $$
>
> Case III If $r_{1}$ and $r_{2}$ are complex conjugate roots with $r_{1}=a+i b$, then
>
> $$
> y=|x|^{a}\left[c_{1} \cos (b \ln |x|)+c_{2} \sin (b \ln |x|)\right]
> $$
>
> Clearly when $x>0$ we may drop the absolute values.
````

## 4. Move correction/commentary into the separate editorial record; keep the actual correction in the reading text.

### Before

````text
[Corrected: the source drops a factor of $2$ in part (a) and inserts an extra $dx$ inside the outer integral in part (b).]
````
### After

````text

````

## 5. Move correction/commentary into the separate editorial record; keep the actual correction in the reading text.

### Before

````text
[Corrected: the printed Wronskian omits the factor $b$.]
````
### After

````text

````
