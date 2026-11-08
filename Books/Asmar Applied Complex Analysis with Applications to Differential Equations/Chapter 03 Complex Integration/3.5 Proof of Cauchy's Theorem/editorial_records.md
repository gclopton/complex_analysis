
# Editorial records

Reading note: 3.5 Proof of Cauchy's Theorem.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Callout 109: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Cauchy’s Integral Theorem in a Star-Shaped Region
> Suppose that $f$ is analytic on a star region $\Omega$. Then
>
> $$\int_{\Gamma} f(z) d z=0$$
>
> for all closed paths $\Gamma$ in $\Omega$.
````
### After

````text
> [!theorem] Cauchy's Integral Theorem for Star Regions
> Suppose that $f$ is analytic on a star region $\Omega$. Then
>
> $$\int_{\Gamma} f(z) d z=0$$
>
> for all closed paths $\Gamma$ in $\Omega$.
````

## 2. Callout 110: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Fubini's Theorem for Complex Path Integrals
> Suppose that $f(z, \zeta)$ is continuous for $z$ on a path $\gamma_{1}$ and $\zeta$ on a path $\gamma_{2}$. Then
>
> $$
> \int_{\gamma_{1}} \int_{\gamma_{2}} f(z, \zeta) d \zeta d z=\int_{\gamma_{2}} \int_{\gamma_{1}} f(z, \zeta) d z d \zeta
> $$
````
### After

````text
> [!theorem] Fubini's Theorem for Path Integrals
> Suppose that $f(z, \zeta)$ is continuous for $z$ on a path $\gamma_{1}$ and $\zeta$ on a path $\gamma_{2}$. Then
>
> $$
> \int_{\gamma_{1}} \int_{\gamma_{2}} f(z, \zeta) d \zeta d z=\int_{\gamma_{2}} \int_{\gamma_{1}} f(z, \zeta) d z d \zeta
> $$
````

## 3. Callout 111: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Continuity of Parameter-Dependent Complex Path Integrals
> Suppose that $f(z, \zeta)$ is continuous for $z$ in a region $\Omega$ and $\zeta$ on a path $\gamma$. For $z$ in $\Omega$, consider
>
> $$
> \phi(z)=\int_{\gamma} f(z, \zeta) d \zeta
> $$
>
> Then $\phi$ is a continuous function of $z$ in $\Omega$.
````
### After

````text
> [!theorem] Continuity of Path Integrals
> Suppose that $f(z, \zeta)$ is continuous for $z$ in a region $\Omega$ and $\zeta$ on a path $\gamma$. For $z$ in $\Omega$, consider
>
> $$
> \phi(z)=\int_{\gamma} f(z, \zeta) d \zeta
> $$
>
> Then $\phi$ is a continuous function of $z$ in $\Omega$.
````

## 4. Callout 112: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Differentiation Under a Complex Path Integral
> Suppose that $f(z, \zeta)$ is a complex-valued function, defined for $z$ in a region $\Omega$ and $\zeta$ on a path $\gamma$. If both $f(z, \zeta)$ and $\frac{d}{d z} f(z, \zeta)$ are continuous functions of $(z, \zeta)$ (hence, for fixed $\zeta, f(z, \zeta)$ is analytic in $z)$, then the function
>
> $$
> F(z)=\int_{\gamma} f(z, \zeta) d \zeta
> $$
>
> is analytic on $\Omega$ and
>
> $$
> F^{\prime}(z)=\int_{\gamma} \frac{d}{d z} f(z, \zeta) d \zeta
> $$
````
### After

````text
> [!theorem] Differentiation of Path Integrals
> Suppose that $f(z, \zeta)$ is a complex-valued function, defined for $z$ in a region $\Omega$ and $\zeta$ on a path $\gamma$. If both $f(z, \zeta)$ and $\frac{d}{d z} f(z, \zeta)$ are continuous functions of $(z, \zeta)$ (hence, for fixed $\zeta, f(z, \zeta)$ is analytic in $z)$, then the function
>
> $$
> F(z)=\int_{\gamma} f(z, \zeta) d \zeta
> $$
>
> is analytic on $\Omega$ and
>
> $$
> F^{\prime}(z)=\int_{\gamma} \frac{d}{d z} f(z, \zeta) d \zeta
> $$
````

## 5. Callout 113: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Continuity and Differentiation Under a Real-Parameter Integral
> (i) Let $u$ be a continuous complex-valued function on the rectangle $R=[a, b] \times [c, d]$. For $c \leq y \leq d$, define
>
> $$
> \phi(y)=\int_{a}^{b} u(x, y) d x
> $$
>
> Then $\phi(y)$ is continuous on $[c, d]$. 
>
> (ii) If $u$ is real-valued and continuous on $R$ and $\frac{\partial u}{\partial y}$ is also continuous on $R$, then $\phi(y)$ is differentiable on $(c, d)$ with
>
> $$
> \phi^{\prime}(y)=\frac{d}{d y} \int_{a}^{b} u(x, y) d x=\int_{a}^{b} \frac{\partial u}{\partial y}(x, y) d x \quad(c<y<d)
> $$
````
### After

````text
> [!theorem] Continuity and Differentiation of Integrals
> (i) Let $u$ be a continuous complex-valued function on the rectangle $R=[a, b] \times [c, d]$. For $c \leq y \leq d$, define
>
> $$
> \phi(y)=\int_{a}^{b} u(x, y) d x
> $$
>
> Then $\phi(y)$ is continuous on $[c, d]$. 
>
> (ii) If $u$ is real-valued and continuous on $R$ and $\frac{\partial u}{\partial y}$ is also continuous on $R$, then $\phi(y)$ is differentiable on $(c, d)$ with
>
> $$
> \phi^{\prime}(y)=\frac{d}{d y} \int_{a}^{b} u(x, y) d x=\int_{a}^{b} \frac{\partial u}{\partial y}(x, y) d x \quad(c<y<d)
> $$
````
