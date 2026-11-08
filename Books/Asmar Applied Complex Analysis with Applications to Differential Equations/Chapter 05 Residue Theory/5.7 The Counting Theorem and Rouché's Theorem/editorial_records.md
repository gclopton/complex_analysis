
# Editorial records

Reading note: 5.7 The Counting Theorem and Rouché's Theorem.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Callout 218: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Argument Principle for Counting Zeros of an Analytic Function
> Suppose that $C$ is a simple closed positively oriented path, $\Omega$ is the region inside $C$, and $f$ is analytic inside and on $C$ and nonvanishing on $C$. Let $N(f)$ denote the number of zeros of $f$ inside $\Omega$, counted according to multiplicity. Then $N(f)$ is finite and
>
> $$
> N(f)=\frac{1}{2 \pi i} \int_C \frac{f^{\prime}(z)}{f(z)} d z
> $$
````
### After

````text
> [!theorem] Counting Theorem
> Suppose that $C$ is a simple closed positively oriented path, $\Omega$ is the region inside $C$, and $f$ is analytic inside and on $C$ and nonvanishing on $C$. Let $N(f)$ denote the number of zeros of $f$ inside $\Omega$, counted according to multiplicity. Then $N(f)$ is finite and
>
> $$
> N(f)=\frac{1}{2 \pi i} \int_C \frac{f^{\prime}(z)}{f(z)} d z
> $$
````

## 2. Callout 219: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Argument Principle for Zeros and Poles of a Meromorphic Function
> Suppose that $C$ is a simple closed positively oriented path, $\Omega$ is the region inside $C$, and $f$ is meromorphic on $\Omega$, analytic and nonvanishing on $C$. Let $N(f)$ denote the number of zeros of $f$ inside $\Omega$ and $P(f)$ denote the number of poles of $f$ inside $\Omega$, counted according to multiplicity. Then $N(f)$ and $P(f)$ are finite and
>
> $$
> N(f)-P(f)=\frac{1}{2 \pi i} \int_C \frac{f^{\prime}(z)}{f(z)} d z .
> $$
````
### After

````text
> [!theorem] Meromorphic Counting Theorem
> Suppose that $C$ is a simple closed positively oriented path, $\Omega$ is the region inside $C$, and $f$ is meromorphic on $\Omega$, analytic and nonvanishing on $C$. Let $N(f)$ denote the number of zeros of $f$ inside $\Omega$ and $P(f)$ denote the number of poles of $f$ inside $\Omega$, counted according to multiplicity. Then $N(f)$ and $P(f)$ are finite and
>
> $$
> N(f)-P(f)=\frac{1}{2 \pi i} \int_C \frac{f^{\prime}(z)}{f(z)} d z .
> $$
````

## 3. Callout 220: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Weighted Argument Principle for Meromorphic Functions
> Let $C$ be a simple closed positively oriented path with interior $\Omega$. Let $f$ be meromorphic inside and on $C$, with no zeros or poles on $C$, and let $g$ be analytic inside and on $C$. Let $z_1, z_2, \ldots, z_{n_1}$ denote the zeros of $f$ in $\Omega$ and $p_1, p_2, \ldots, p_{n_2}$ denote the poles of $f$ in $\Omega$. Let $m\left(z_j\right)$ and $m\left(p_j\right)$ denote the orders of the roots and poles. Then
>
> $$
> \frac{1}{2 \pi i} \int_C g(z) \frac{f^{\prime}(z)}{f(z)} d z=\sum_{j=1}^{n_1} m\left(z_j\right) g\left(z_j\right)-\sum_{j=1}^{n_2} m\left(p_j\right) g\left(p_j\right)
> $$
````
### After

````text
> [!theorem] Variant of the Counting Theorem
> Let $C$ be a simple closed positively oriented path with interior $\Omega$. Let $f$ be meromorphic inside and on $C$, with no zeros or poles on $C$, and let $g$ be analytic inside and on $C$. Let $z_1, z_2, \ldots, z_{n_1}$ denote the zeros of $f$ in $\Omega$ and $p_1, p_2, \ldots, p_{n_2}$ denote the poles of $f$ in $\Omega$. Let $m\left(z_j\right)$ and $m\left(p_j\right)$ denote the orders of the roots and poles. Then
>
> $$
> \frac{1}{2 \pi i} \int_C g(z) \frac{f^{\prime}(z)}{f(z)} d z=\sum_{j=1}^{n_1} m\left(z_j\right) g\left(z_j\right)-\sum_{j=1}^{n_2} m\left(p_j\right) g\left(p_j\right)
> $$
````

## 4. Callout 221: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!lemma] Constancy of Continuous Integer-Valued Functions on a Region
> Suppose that $\phi$ is continuous on a region $\Omega$ and $\phi(z)$ is an integer for all $z$ in $\Omega$ (in other words, $\phi$ is integer-valued). Then $\phi$ is constant on $\Omega$.
````
### After

````text
> [!lemma] Integer-Valued Functions
> Suppose that $\phi$ is continuous on a region $\Omega$ and $\phi(z)$ is an integer for all $z$ in $\Omega$ (in other words, $\phi$ is integer-valued). Then $\phi$ is constant on $\Omega$.
````

## 5. Callout 222: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Rouché's Theorem for Counting Complex Zeros
> Suppose that $C$ is a simple closed path, $\Omega$ is the region inside $C, f$ and $g$ are analytic inside and on $C$. If $|g(z)|<|f(z)|$ for all $z$ on $C$, then $N(f+g)=N(f)$; that is, $f+g$ and $f$ have the same number of zeros in $\Omega$, counted with multiplicity.
````
### After

````text
> [!theorem] Rouché's Theorem
> Suppose that $C$ is a simple closed path, $\Omega$ is the region inside $C, f$ and $g$ are analytic inside and on $C$. If $|g(z)|<|f(z)|$ for all $z$ on $C$, then $N(f+g)=N(f)$; that is, $f+g$ and $f$ have the same number of zeros in $\Omega$, counted with multiplicity.
````

## 6. Callout 223: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Local Multiplicity of a Nonconstant Analytic Mapping
> Let $f$ be a nonconstant analytic function in a neighborhood of $z_0$. Let $w_0=f\left(z_0\right)$ and $n$ be the order of the zero of $f(z)-f(z_0)$ at $z_0$. There exists $R>0$ and $\rho>0$ such that every $w \neq w_0$ in $B_\rho\left(w_0\right)$ is attained by $f$ at precisely $n$ distinct points in $B_R\left(z_0\right)$.
````
### After

````text
> [!theorem] Local Mapping Theorem
> Let $f$ be a nonconstant analytic function in a neighborhood of $z_0$. Let $w_0=f\left(z_0\right)$ and $n$ be the order of the zero of $f(z)-f(z_0)$ at $z_0$. There exists $R>0$ and $\rho>0$ such that every $w \neq w_0$ in $B_\rho\left(w_0\right)$ is attained by $f$ at precisely $n$ distinct points in $B_R\left(z_0\right)$.
````

## 7. Callout 224: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Local Injectivity and the Nonvanishing Complex Derivative
> Suppose that $f$ is analytic on a region $\Omega$ and $z_0$ is in $\Omega$. Then $f$ is one-to-one on some neighborhood $B_r\left(z_0\right)$ if and only if $f^{\prime}\left(z_0\right) \neq 0$.
````
### After

````text
> [!theorem] Inverse Function Theorem
> Suppose that $f$ is analytic on a region $\Omega$ and $z_0$ is in $\Omega$. Then $f$ is one-to-one on some neighborhood $B_r\left(z_0\right)$ if and only if $f^{\prime}\left(z_0\right) \neq 0$.
````

## 8. Callout 225: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!corollary] Open Mapping Theorem for Nonconstant Analytic Functions
> Let $f$ be analytic and nonconstant on a region $\Omega$; the open sets considered are subsets of $\Omega$.
>
> A nonconstant analytic function $f$ maps open sets into open sets. A function with this property is said to be open.
````
### After

````text
> [!corollary] Open Mapping Property
> Let $f$ be analytic and nonconstant on a region $\Omega$; the open sets considered are subsets of $\Omega$.
>
> A nonconstant analytic function $f$ maps open sets into open sets. A function with this property is said to be open.
````

## 9. Callout 226: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!corollary] Images of Regions Under Nonconstant Analytic Functions
> If $\Omega$ is a nonempty region (open and connected set) and $f$ is a nonconstant analytic function on $\Omega$, then $f[\Omega]$ is a region.
````
### After

````text
> [!corollary] Mapping of Regions
> If $\Omega$ is a nonempty region (open and connected set) and $f$ is a nonconstant analytic function on $\Omega$, then $f[\Omega]$ is a region.
````

## 10. Callout 227: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!corollary] Maximum Modulus Principle for Analytic Functions
> If $f$ is analytic on a region $\Omega$, such that $|f|$ attains a maximum at some point in $\Omega$, then $f$ is constant in $\Omega$.
````
### After

````text
> [!corollary] Maximum Modulus Principle
> If $f$ is analytic on a region $\Omega$, such that $|f|$ attains a maximum at some point in $\Omega$, then $f$ is constant in $\Omega$.
````

## 11. Callout 228: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Contour Integral Formula for a Local Analytic Inverse
> Write $w_0=f(z_0)$. Choose $R>0$ small enough that $f$ is analytic and one-to-one on a neighborhood of the closed disk $|z-z_0|\leq R$, and choose $\rho>0$ such that $B_\rho(w_0)$ lies inside its image. The circle $C_R(z_0)$ has positive orientation.
>
> Suppose that $f(z)$ is analytic at $z_0$ and $f^{\prime}\left(z_0\right) \neq 0$. Then $f$ has an inverse function $z=g(w)$ in a neighborhood $B_\rho\left(w_0\right)$ of $w_0$ given by
>
> $$
> g(w)=\frac{1}{2 \pi i} \int_{C_R\left(z_0\right)} z \frac{f^{\prime}(z)}{f(z)-w} d z
> $$
>
> Furthermore, $g(w)$ is analytic on $B_\rho\left(w_0\right)$.
````
### After

````text
> [!theorem] Inverse Function Formula
> Write $w_0=f(z_0)$. Choose $R>0$ small enough that $f$ is analytic and one-to-one on a neighborhood of the closed disk $|z-z_0|\leq R$, and choose $\rho>0$ such that $B_\rho(w_0)$ lies inside its image. The circle $C_R(z_0)$ has positive orientation.
>
> Suppose that $f(z)$ is analytic at $z_0$ and $f^{\prime}\left(z_0\right) \neq 0$. Then $f$ has an inverse function $z=g(w)$ in a neighborhood $B_\rho\left(w_0\right)$ of $w_0$ given by
>
> $$
> g(w)=\frac{1}{2 \pi i} \int_{C_R\left(z_0\right)} z \frac{f^{\prime}(z)}{f(z)-w} d z
> $$
>
> Furthermore, $g(w)$ is analytic on $B_\rho\left(w_0\right)$.
````

## 12. Callout 229: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!corollary] Analyticity and Derivative of a Global Complex Inverse
> Suppose that $f$ is analytic and one-to-one on a region $\Omega$. Then its inverse function $f^{-1}$ exists and is analytic on the region $f[\Omega]$. Moreover,
>
> $$
> \frac{d}{d w} f^{-1}(w)=\frac{1}{f^{\prime}(z)}, \quad \text { where } w=f(z)
> $$
````
### After

````text
> [!corollary] A Global Inverse Function
> Suppose that $f$ is analytic and one-to-one on a region $\Omega$. Then its inverse function $f^{-1}$ exists and is analytic on the region $f[\Omega]$. Moreover,
>
> $$
> \frac{d}{d w} f^{-1}(w)=\frac{1}{f^{\prime}(z)}, \quad \text { where } w=f(z)
> $$
````

## 13. Move editorial commentary out of the reading note.

### Before

````text
*Editorial note: [corrected] The logarithmic-derivative statement allows poles, so its common hypothesis is meromorphic, not analytic throughout the region.*
````
### After

````text

````
