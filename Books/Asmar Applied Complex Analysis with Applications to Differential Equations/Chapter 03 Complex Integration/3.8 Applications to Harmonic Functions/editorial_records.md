
# Editorial records

Reading note: 3.8 Applications to Harmonic Functions.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Callout 130: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!lemma] Analyticity of the Conjugate Gradient of a Harmonic Function
> Suppose that $u$ is harmonic on a region $\Omega$. Let $\phi=u_{x}-i u_{y}$. Then $\phi$ is analytic on $\Omega$. The function $\phi$ is called the conjugate gradient of $u$.
````
### After

````text
> [!lemma] Conjugate gradient
> Suppose that $u$ is harmonic on a region $\Omega$. Let $\phi=u_{x}-i u_{y}$. Then $\phi$ is analytic on $\Omega$. The function $\phi$ is called the conjugate gradient of $u$.
````

## 2. Callout 132: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Harmonic Conjugates on Simply Connected Regions
> Suppose that $u$ is harmonic on a simply connected region $\Omega$. Then $u$ has a harmonic conjugate in $\Omega$ given up to an additive constant by
>
> $$
> v(z)=\int_{z_{0}}^{z}-u_{y} d x+u_{x} d y \quad\left(z_{0} \text { fixed in } \Omega\right)
> $$
>
> where the integral is independent of path.
````
### After

````text
> [!theorem] Harmonic Conjugate
> Suppose that $u$ is harmonic on a simply connected region $\Omega$. Then $u$ has a harmonic conjugate in $\Omega$ given up to an additive constant by
>
> $$
> v(z)=\int_{z_{0}}^{z}-u_{y} d x+u_{x} d y \quad\left(z_{0} \text { fixed in } \Omega\right)
> $$
>
> where the integral is independent of path.
````

## 3. Callout 134: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!corollary] Gauss's Circular Mean Value Property for Harmonic Functions
> Suppose that $u$ is harmonic on a region $\Omega$, then $u$ satisfies the mean value property, in the following sense. If $z$ is in $\Omega$, and the closed disk $S_{r}(z)$ ( $r>0$ ) is contained in $\Omega$, then
>
> $$
> u(z)=\frac{1}{2 \pi} \int_{0}^{2 \pi} u\left(z+r e^{i t}\right) d t
> $$
````
### After

````text
> [!corollary] 3: Gauss's Mean Value Property
> Suppose that $u$ is harmonic on a region $\Omega$, then $u$ satisfies the mean value property, in the following sense. If $z$ is in $\Omega$, and the closed disk $S_{r}(z)$ ( $r>0$ ) is contained in $\Omega$, then
>
> $$
> u(z)=\frac{1}{2 \pi} \int_{0}^{2 \pi} u\left(z+r e^{i t}\right) d t
> $$
````

## 4. Callout 135: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Maximum and Minimum Principles for Harmonic Functions
> Suppose that $u$ is a harmonic function on a region $\Omega$. If $u$ attains a maximum
> or a minimum in $\Omega$, then $u$ is constant in $\Omega$.
````
### After

````text
> [!theorem] Maximum-Minimum Principle
> Suppose that $u$ is a harmonic function on a region $\Omega$. If $u$ attains a maximum
> or a minimum in $\Omega$, then $u$ is constant in $\Omega$.
````

## 5. Callout 139: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!proposition] Harmonic Extension of Trigonometric Polynomial Boundary Data on a Disk
> Let $R>0$, let $N$ be a nonnegative integer, and let $a_0,a_n,b_n$ be real coefficients. The unique harmonic function in $|z|<R$, continuous on the closed disk, with boundary values $u(R,\theta)=a_0+\sum_{n=1}^{N}(a_n\cos n\theta+b_n\sin n\theta)$ is, for $0\leq r\leq R$,
>
> $$
> u(r, \theta)=a_{0}+\sum_{n=1}^{N}\left(\frac{r}{R}\right)^{n}\left(a_{n} \cos n \theta+b_{n} \sin n \theta\right)
> $$
````
### After

````text
> [!proposition] A Dirichlet Problem on the Disk
> Let $R>0$, let $N$ be a nonnegative integer, and let $a_0,a_n,b_n$ be real coefficients. The unique harmonic function in $|z|<R$, continuous on the closed disk, with boundary values $u(R,\theta)=a_0+\sum_{n=1}^{N}(a_n\cos n\theta+b_n\sin n\theta)$ is, for $0\leq r\leq R$,
>
> $$
> u(r, \theta)=a_{0}+\sum_{n=1}^{N}\left(\frac{r}{R}\right)^{n}\left(a_{n} \cos n \theta+b_{n} \sin n \theta\right)
> $$
````

## 6. Callout 141: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Poisson Solution of the Dirichlet Problem on a Disk
> Let $R>0$ and let $f$ be a real-valued, $2\pi$-periodic, piecewise continuous function. Its harmonic extension to the disk $|z|<R$ is given by the Poisson integral
>  $$u(r, \theta)=\frac{R^{2}-r^{2}}{2 \pi} \int_{0}^{2 \pi} \frac{f(\phi)}{R^{2}-2 r R \cos (\theta-\phi)+r^{2}} d \phi \quad(0 \leq r<R). $$
>
> More precisely, $u(r, \theta)$ is harmonic in the open disk $|z|<R$ and tends to $f(\theta)$ as $r \uparrow R$ at all points of continuity of $f$.
````
### After

````text
> [!theorem] Poisson Integral Formula
> Let $R>0$ and let $f$ be a real-valued, $2\pi$-periodic, piecewise continuous function. Its harmonic extension to the disk $|z|<R$ is given by the Poisson integral
>  $$u(r, \theta)=\frac{R^{2}-r^{2}}{2 \pi} \int_{0}^{2 \pi} \frac{f(\phi)}{R^{2}-2 r R \cos (\theta-\phi)+r^{2}} d \phi \quad(0 \leq r<R). $$
>
> More precisely, $u(r, \theta)$ is harmonic in the open disk $|z|<R$ and tends to $f(\theta)$ as $r \uparrow R$ at all points of continuity of $f$.
````

## 7. Callout 142: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!corollary] Value at the Center of a Disk of a Poisson Extension
> Let $R>0$ and let $f$ be real-valued, $2\pi$-periodic, and piecewise continuous. For its Poisson extension
>
> $$
> u(re^{i\theta})=\frac{R^2-r^2}{2\pi}\int_0^{2\pi}\frac{f(\phi)}{R^2-2rR\cos(\theta-\phi)+r^2}\,d\phi,\qquad 0\leq r<R,
> $$
>
> the value at the center is the boundary average:
>
> $$
> u(0)=\frac{1}{2\pi}\int_0^{2\pi}f(\phi)\,d\phi.
> $$
````
### After

````text
> [!corollary] Mean Value Property
> Let $R>0$, and let $u$ be the Poisson extension of the $2\pi$-periodic boundary function $f$. Suppose that $u\left(r e^{i \phi}\right)$ is harmonic for $0 \leq r<R$ and $0 \leq \phi \leq 2 \pi$, and $u\left(R e^{i \phi}\right)=f(\phi)$, where $f$ is piecewise continuous on the boundary. Then
>
> $$
> u(0)=\frac{1}{2 \pi} \int_{0}^{2 \pi} f(\phi) d \phi
> $$
````

## 8. Move editorial commentary out of the reading note.

### Before

````text
*Editorial note: [clarified] This corollary concerns the Poisson extension from the preceding theorem. Merely assigning piecewise continuous boundary values to an arbitrary interior harmonic function does not imply this formula.*
````
### After

````text

````
