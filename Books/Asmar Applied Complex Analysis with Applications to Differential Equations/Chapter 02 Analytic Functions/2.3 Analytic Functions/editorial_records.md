
# Editorial records

Reading note: 2.3 Analytic Functions.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Callout 54: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!definition] Analytic and Entire Complex Functions
> A function $f(z)$ defined on an open set $S$ is said to be analytic on $S$ if $f^{\prime}(z)$ exists and is continuous for all $z$ in $S$. We say $f(z)$ is analytic at a point if $f(z)$ is analytic on some open set containing that point. We say $f(z)$ is entire if $f(z)$ is analytic on $\mathbb{C}$.
````
### After

````text
> [!definition] Analytic Function
> A function $f(z)$ defined on an open set $S$ is said to be analytic on $S$ if $f^{\prime}(z)$ exists and is continuous for all $z$ in $S$. We say $f(z)$ is analytic at a point if $f(z)$ is analytic on some open set containing that point. We say $f(z)$ is entire if $f(z)$ is analytic on $\mathbb{C}$.
````

## 2. Callout 55: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Complex Differentiability Implies Continuity
> Suppose $f(z)$ is differentiable at $z_{0}$. Then $f(z)$ is continuous at $z_{0}$.
````
### After

````text
> [!theorem] Differentiable Implies Continuous
> Suppose $f(z)$ is differentiable at $z_{0}$. Then $f(z)$ is continuous at $z_{0}$.
````

## 3. Callout 56: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Sum, Product, Quotient, and Chain Rules for Analytic Functions
> Suppose that $f$ and $g$ are analytic on an open set $S$ and $c_{1}, c_{2}$ are complex constants. Then $c_{1} f+c_{2} g$ and $f g$ are analytic on $S$ with
>
> $$
> \begin{aligned}
> \left(c_{1} f+c_{2} g\right)^{\prime}(z) & =c_{1} f^{\prime}(z)+c_{2} g^{\prime}(z) \text { and } \\
> (f g)^{\prime}(z) & =f^{\prime}(z) g(z)+f(z) g^{\prime}(z) .
> \end{aligned}
> $$
>
> Also, $\frac{f}{g}$ is analytic on $S$ minus the points where $g=0$, and
>
> $$
> \left(\frac{f}{g}\right)^{\prime}(z)=\frac{f^{\prime}(z) g(z)-f(z) g^{\prime}(z)}{(g(z))^{2}} \quad(g(z) \neq 0) .
> $$
>
> If $g$ is analytic at $z_{0}$ and $f$ is analytic at $g\left(z_{0}\right)$, then the composition $(f \circ g)(z)$ is analytic at $z_{0}$ and we have the chain rule
>
> $$
> (f \circ g)^{\prime}\left(z_{0}\right)=f^{\prime}\left(g\left(z_{0}\right)\right) g^{\prime}\left(z_{0}\right) .
> $$
````
### After

````text
> [!theorem] Properties of Analytic Functions
> Suppose that $f$ and $g$ are analytic on an open set $S$ and $c_{1}, c_{2}$ are complex constants. Then $c_{1} f+c_{2} g$ and $f g$ are analytic on $S$ with
>
> $$
> \begin{aligned}
> \left(c_{1} f+c_{2} g\right)^{\prime}(z) & =c_{1} f^{\prime}(z)+c_{2} g^{\prime}(z) \text { and } \\
> (f g)^{\prime}(z) & =f^{\prime}(z) g(z)+f(z) g^{\prime}(z) .
> \end{aligned}
> $$
>
> Also, $\frac{f}{g}$ is analytic on $S$ minus the points where $g=0$, and
>
> $$
> \left(\frac{f}{g}\right)^{\prime}(z)=\frac{f^{\prime}(z) g(z)-f(z) g^{\prime}(z)}{(g(z))^{2}} \quad(g(z) \neq 0) .
> $$
>
> If $g$ is analytic at $z_{0}$ and $f$ is analytic at $g\left(z_{0}\right)$, then the composition $(f \circ g)(z)$ is analytic at $z_{0}$ and we have the chain rule
>
> $$
> (f \circ g)^{\prime}\left(z_{0}\right)=f^{\prime}\left(g\left(z_{0}\right)\right) g^{\prime}\left(z_{0}\right) .
> $$
````

## 4. Callout 57: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Analyticity and Derivatives of Complex Polynomials and Rational Functions
> Let $n$ be a nonnegative integer. A polynomial of degree $n, p(z)=a_{n} z^{n}+ a_{n-1} z^{n-1}+\cdots+a_{1} z+a_{0}$, is entire. Its derivative is given by
>
> $$
> p^{\prime}(z)=n a_{n} z^{n-1}+(n-1) a_{n-1} z^{n-1}+\cdots+a_{1} .
> $$
>
> A rational function $f(z)=p(z) / q(z)$, where $p(z)$ and $q(z)$ are polynomials, is analytic at all points $z$ where $q(z) \neq 0$. Its derivative is given by
>
> $$
> f^{\prime}(z)=\frac{p^{\prime}(z) q(z)-p(z) q^{\prime}(z)}{q(z)^{2}}
> $$
````
### After

````text
> [!theorem] Polynomials and Rational Functions
> Let $n$ be a nonnegative integer. A polynomial of degree $n, p(z)=a_{n} z^{n}+ a_{n-1} z^{n-1}+\cdots+a_{1} z+a_{0}$, is entire. Its derivative is given by
>
> $$
> p^{\prime}(z)=n a_{n} z^{n-1}+(n-1) a_{n-1} z^{n-1}+\cdots+a_{1} .
> $$
>
> A rational function $f(z)=p(z) / q(z)$, where $p(z)$ and $q(z)$ are polynomials, is analytic at all points $z$ where $q(z) \neq 0$. Its derivative is given by
>
> $$
> f^{\prime}(z)=\frac{p^{\prime}(z) q(z)-p(z) q^{\prime}(z)}{q(z)^{2}}
> $$
````

## 5. Callout 58: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Analyticity of an Inner Function under a Locally Invertible Analytic Map
> Suppose that $h(z)=f(g(z))$ is analytic on a region $\Omega$, and $f$ is analytic at $g(z)$ with $f^{\prime}(g(z)) \neq 0$ for all $z$ in $\Omega$. Suppose further that $g(z)$ is continuous on $\Omega$. Then $g$ is analytic on $\Omega$ and
>
> $$
> g^{\prime}(z)=\frac{h^{\prime}(z)}{f^{\prime}(g(z))}
> $$
````
### After

````text
> [!theorem] Analyticity of Composed Functions
> Suppose that $h(z)=f(g(z))$ is analytic on a region $\Omega$, and $f$ is analytic at $g(z)$ with $f^{\prime}(g(z)) \neq 0$ for all $z$ in $\Omega$. Suppose further that $g(z)$ is continuous on $\Omega$. Then $g$ is analytic on $\Omega$ and
>
> $$
> g^{\prime}(z)=\frac{h^{\prime}(z)}{f^{\prime}(g(z))}
> $$
````

## 6. Callout 59: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Linear Approximation Characterization of Complex Differentiability
> A function $f(z)$ is differentiable at $z_{0}$ if and only if it can be written in the form
>
> $$
> f(z)=f\left(z_{0}\right)+A\left(z-z_{0}\right)+\epsilon(z)\left(z-z_{0}\right)
> $$
>
> where $A=f^{\prime}\left(z_{0}\right)$ and $\epsilon(z) \rightarrow 0$ as $z \rightarrow z_{0}$.
````
### After

````text
> [!theorem] Differentiability
> A function $f(z)$ is differentiable at $z_{0}$ if and only if it can be written in the form
>
> $$
> f(z)=f\left(z_{0}\right)+A\left(z-z_{0}\right)+\epsilon(z)\left(z-z_{0}\right)
> $$
>
> where $A=f^{\prime}\left(z_{0}\right)$ and $\epsilon(z) \rightarrow 0$ as $z \rightarrow z_{0}$.
````

## 7. Move editorial commentary out of the reading note.

### Before

````text
*Editorial note: Corrected the final derivative term: the derivative of $a_1z$ is $a_1$.*
````
### After

````text

````
