
# Editorial records

Reading note: 10.2 Linear Ordinary Differential Equations with Constant Coefficients.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!rule|d20db426-76e0-56ae-a30c-c4dd6a5f292d.local at=dec31ecc-135b-5e87-983e-541fa27dba48] Characteristic-Root Construction for Constant-Coefficient Homogeneous Linear ODEs
> Let all coefficients $a_j$ be real constants, with $a_n\ne0$. Multiplicities are algebraic multiplicities, and constants in different root contributions are independent.
>
> Consider the equation
>
> $$
> a_{n} y^{(n)}+a_{n-1} y^{(n-1)}+\cdots+a_{1} y^{\prime}+a_{0} y=0
> $$
>
> with characteristic equation
>
> $$
> a_{n} \lambda^{n}+a_{n-1} \lambda^{n-1}+\cdots+a_{1} \lambda+a_{0}=0
> $$
>
> The general real solution of the differential equation is constructed according to the nature of the roots of the characteristic equation as follows.
>
> Case I For each real root $\mu$ of multiplicity $m \geq 1$, we include a linear combination of the form
>
> $$
> c_{1} e^{\mu x}+c_{2} x e^{\mu x}+\cdots+c_{m} x^{m-1}e^{\mu x}
> $$
>
> Case II For each nonreal root $\mu=\alpha+i \beta$ and its complex conjugate $\bar{\mu}=\alpha-i \beta$ of multiplicity $m \geq 1$, we include a linear combination of the form
>
> $$
> \begin{aligned}
> & c_{1} e^{\alpha x} \cos \beta x+c_{2} x e^{\alpha x} \cos \beta x+\cdots+c_{m} x^{m-1} e^{\alpha x} \cos \beta x \\
> & \quad+d_{1} e^{\alpha x} \sin \beta x+d_{2} x e^{\alpha x} \sin \beta x+\cdots+d_{m} x^{m-1} e^{\alpha x} \sin \beta x
> \end{aligned}
> $$
````
### After

````text
> [!rule|d20db426-76e0-56ae-a30c-c4dd6a5f292d.local at=dec31ecc-135b-5e87-983e-541fa27dba48] General Solution of the $n$th-Order Homogeneous Equation
> Let all coefficients $a_j$ be real constants, with $a_n\ne0$. Multiplicities are algebraic multiplicities, and constants in different root contributions are independent.
>
> Consider the equation
>
> $$
> a_{n} y^{(n)}+a_{n-1} y^{(n-1)}+\cdots+a_{1} y^{\prime}+a_{0} y=0
> $$
>
> with characteristic equation
>
> $$
> a_{n} \lambda^{n}+a_{n-1} \lambda^{n-1}+\cdots+a_{1} \lambda+a_{0}=0
> $$
>
> The general real solution of the differential equation is constructed according to the nature of the roots of the characteristic equation as follows.
>
> Case I For each real root $\mu$ of multiplicity $m \geq 1$, we include a linear combination of the form
>
> $$
> c_{1} e^{\mu x}+c_{2} x e^{\mu x}+\cdots+c_{m} x^{m-1}e^{\mu x}
> $$
>
> Case II For each nonreal root $\mu=\alpha+i \beta$ and its complex conjugate $\bar{\mu}=\alpha-i \beta$ of multiplicity $m \geq 1$, we include a linear combination of the form
>
> $$
> \begin{aligned}
> & c_{1} e^{\alpha x} \cos \beta x+c_{2} x e^{\alpha x} \cos \beta x+\cdots+c_{m} x^{m-1} e^{\alpha x} \cos \beta x \\
> & \quad+d_{1} e^{\alpha x} \sin \beta x+d_{2} x e^{\alpha x} \sin \beta x+\cdots+d_{m} x^{m-1} e^{\alpha x} \sin \beta x
> \end{aligned}
> $$
````

## 2. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!rule|82e7bb10-ee1c-58b9-a1b4-179d76a3554d.local at=80cec4ea-5d4d-5671-b00d-2a975958e9e0] Real General Solutions of Second-Order Constant-Coefficient Homogeneous ODEs
> Let $a,b,c$ be real constants with $a\ne0$. The constants $c_1,c_2$ below are arbitrary.
>
> Consider the equation
>
> $$
> a y^{\prime \prime}+b y^{\prime}+c y=0
> $$
>
> with characteristic equation
>
> $$
> a \lambda^{2}+b \lambda+c=0
> $$
>
> Let $\lambda_{1}$ and $\lambda_{2}$ denote the characteristic roots. The general solution y of this differential equation is given by one of the following cases.
> Case I If $\lambda_{1}$ and $\lambda_{2}$ are distinct real roots, then
>
> $$
> y=c_{1} e^{\lambda_{1} x}+c_{2} e^{\lambda_{2} x}
> $$
>
> Equivalently, write $\lambda_{1}=\frac{-b}{2 a}+\frac{\sqrt{b^{2}-4 a c}}{2 a}=\alpha+\beta$ and $\lambda_{2}=\alpha-\beta$, then
>
> $$
> y=e^{\alpha x}\left(c_{1} \cosh \beta x+c_{2} \sinh \beta x\right) .
> $$
>
> Case II If $\lambda_{1}=\lambda_{2}$, then
>
> $$
> y=c_{1} e^{\lambda_{1} x}+c_{2} x e^{\lambda_{1} x}
> $$
>
> Case III If $\lambda_{1}$ and $\lambda_{2}$ are complex conjugate roots with $\lambda_{1}=\alpha+i \beta$, then
>
> $$
> y=c_{1} e^{\alpha x} \cos \beta x+c_{2} e^{\alpha x} \sin \beta x .
> $$
````
### After

````text
> [!rule|82e7bb10-ee1c-58b9-a1b4-179d76a3554d.local at=80cec4ea-5d4d-5671-b00d-2a975958e9e0] General Solution of the Second-Order Homogeneous Equation
> Let $a,b,c$ be real constants with $a\ne0$. The constants $c_1,c_2$ below are arbitrary.
>
> Consider the equation
>
> $$
> a y^{\prime \prime}+b y^{\prime}+c y=0
> $$
>
> with characteristic equation
>
> $$
> a \lambda^{2}+b \lambda+c=0
> $$
>
> Let $\lambda_{1}$ and $\lambda_{2}$ denote the characteristic roots. The general solution y of this differential equation is given by one of the following cases.
> Case I If $\lambda_{1}$ and $\lambda_{2}$ are distinct real roots, then
>
> $$
> y=c_{1} e^{\lambda_{1} x}+c_{2} e^{\lambda_{2} x}
> $$
>
> Equivalently, write $\lambda_{1}=\frac{-b}{2 a}+\frac{\sqrt{b^{2}-4 a c}}{2 a}=\alpha+\beta$ and $\lambda_{2}=\alpha-\beta$, then
>
> $$
> y=e^{\alpha x}\left(c_{1} \cosh \beta x+c_{2} \sinh \beta x\right) .
> $$
>
> Case II If $\lambda_{1}=\lambda_{2}$, then
>
> $$
> y=c_{1} e^{\lambda_{1} x}+c_{2} x e^{\lambda_{1} x}
> $$
>
> Case III If $\lambda_{1}$ and $\lambda_{2}$ are complex conjugate roots with $\lambda_{1}=\alpha+i \beta$, then
>
> $$
> y=c_{1} e^{\alpha x} \cos \beta x+c_{2} e^{\alpha x} \sin \beta x .
> $$
````

## 3. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!procedure|8ee66310-8c6c-5b69-87bb-fd2965628cac.local at=151d6798-685e-5922-8104-417e052e6120] Undetermined Coefficients for Second-Order Constant-Coefficient ODEs
> To find a particular solution of $ay^{\prime\prime}+by^{\prime}+cy=g(x)$, where $a,b,c$ are real constants and $a\ne0$, when
>
> $$
> g(x)=\left(a_{n} x^{n}+a_{n-1} x^{n-1}+\cdots+a_{0}\right) e^{\alpha x}\left\{\begin{array}{l}
> \cos \beta x \\
> \sin \beta x
> \end{array}\right.
> $$
>
> we use
>
> $$
> \begin{aligned}
> y_{p}= & \left(A_{n} x^{n}+A_{n-1} x^{n-1}+\cdots+A_{0}\right) e^{\alpha x} \cos \beta x \\
> & +\left(B_{n} x^{n}+B_{n-1} x^{n-1}+\cdots+B_{0}\right) e^{\alpha x} \sin \beta x
> \end{aligned}
> $$
>
> provided that no term in the expression of $y_{p}$ is a solution of the associated homogeneous equation. If not, we modify this expression by multiplying by $x$ or $x^{2}$. We use $x$ if the characteristic polynomial of the associated homogeneous equation has distinct roots, and $x^{2}$ if it has a double root.
> Superposition rule If the right side of $ay^{\prime\prime}+by^{\prime}+cy=g(x)$, where $a,b,c$ are real constants and $a\ne0$, is a sum of several different functions of the stated polynomial–exponential–trigonometric form, we use a corresponding sum of terms of the corresponding trial form.
````
### After

````text
> [!procedure|8ee66310-8c6c-5b69-87bb-fd2965628cac.local at=151d6798-685e-5922-8104-417e052e6120] The Method of Undetermined Coefficients
> To find a particular solution of $ay^{\prime\prime}+by^{\prime}+cy=g(x)$, where $a,b,c$ are real constants and $a\ne0$, when
>
> $$
> g(x)=\left(a_{n} x^{n}+a_{n-1} x^{n-1}+\cdots+a_{0}\right) e^{\alpha x}\left\{\begin{array}{l}
> \cos \beta x \\
> \sin \beta x
> \end{array}\right.
> $$
>
> we use
>
> $$
> \begin{aligned}
> y_{p}= & \left(A_{n} x^{n}+A_{n-1} x^{n-1}+\cdots+A_{0}\right) e^{\alpha x} \cos \beta x \\
> & +\left(B_{n} x^{n}+B_{n-1} x^{n-1}+\cdots+B_{0}\right) e^{\alpha x} \sin \beta x
> \end{aligned}
> $$
>
> provided that no term in the expression of $y_{p}$ is a solution of the associated homogeneous equation. If not, we modify this expression by multiplying by $x$ or $x^{2}$. We use $x$ if the characteristic polynomial of the associated homogeneous equation has distinct roots, and $x^{2}$ if it has a double root.
> Superposition rule If the right side of $ay^{\prime\prime}+by^{\prime}+cy=g(x)$, where $a,b,c$ are real constants and $a\ne0$, is a sum of several different functions of the stated polynomial–exponential–trigonometric form, we use a corresponding sum of terms of the corresponding trial form.
````

## Additional source comparison

## 1. Restore the exact descriptive source title without its numbering.

### Before

````text
> [!rule|d20db426-76e0-56ae-a30c-c4dd6a5f292d.local at=dec31ecc-135b-5e87-983e-541fa27dba48] General Solution of the $n$th-Order Homogeneous Equation
````
### After

````text
> [!rule|d20db426-76e0-56ae-a30c-c4dd6a5f292d.local at=dec31ecc-135b-5e87-983e-541fa27dba48] General Solution of the $n$th-Order Linear Homogeneous Equation with Constant Coefficients
````

## 2. Restore the exact descriptive source title without its numbering.

### Before

````text
> [!rule|82e7bb10-ee1c-58b9-a1b4-179d76a3554d.local at=80cec4ea-5d4d-5671-b00d-2a975958e9e0] General Solution of the Second-Order Homogeneous Equation
````
### After

````text
> [!rule|82e7bb10-ee1c-58b9-a1b4-179d76a3554d.local at=80cec4ea-5d4d-5671-b00d-2a975958e9e0] General Solution of the Second-Order Linear Homogeneous Equation with Constant Coefficients
````

## Additional source comparison

## 1. Move the remaining editorial notice into the separate record.

### Before

````text
[Source uncertainty: the derivative order in Exercise 48 is faint in the supplied PDF. The transcribed $y^{(1)}$ is retained here; verify this order against a clearer source before solving.]
````
### After

````text

````
