
# Editorial records

Reading note: 16.5 Analytic Functions.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!definition|88c531a0-86d5-5f63-ac74-4b12f49c99bf.local at=6f435288-03a3-5ea8-a345-b33c2c859469] Entire Function
> A function $f:\mathbb C\to\mathbb C$ is entire if it is analytic at every point of the complex plane.
````
### After

````text
> [!definition|88c531a0-86d5-5f63-ac74-4b12f49c99bf.local at=6f435288-03a3-5ea8-a345-b33c2c859469] Entire Function
> Functions that are analytic for all $z$ are called entire.
````

## 2. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!definition|715fe8a9-cd33-5925-878f-de84255bbee7.local at=11b37645-96d6-5666-b4b8-bef8bba1ed00] Harmonic Conjugate of a Real Harmonic Function
> Let $\Omega\subset\mathbb C$ be open and let $u:\Omega\to\mathbb R$ be harmonic. A real harmonic function $v$ on $\Omega$ is a harmonic conjugate of $u$ if $f=u+iv$ is analytic on $\Omega$; equivalently, $u_x=v_y$ and $u_y=-v_x$.
````
### After

````text
> [!definition|715fe8a9-cd33-5925-878f-de84255bbee7.local at=11b37645-96d6-5666-b4b8-bef8bba1ed00] Harmonic Conjugate of a Real Harmonic Function
> If a harmonic function $v$ exists such that $u+iv$ is analytic on the region where $u$ is harmonic, it is called a harmonic conjugate of $u$.
````

## 3. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|d0d34a97-7afe-5050-b4d6-aa73417469ef.local at=9952bf75-89e2-556b-83d0-c2a3b533e215] Simply Connected Plane Regions and Global Harmonic Conjugates
> For an open connected set $\Omega\subset\mathbb C$, every real harmonic function $u$ on $\Omega$ has a single-valued harmonic conjugate on $\Omega$ if and only if $\Omega$ is simply connected. The assertion concerns every harmonic function; a particular one may have a conjugate on a multiply connected region.
````
### After

````text
> [!theorem|d0d34a97-7afe-5050-b4d6-aa73417469ef.local at=9952bf75-89e2-556b-83d0-c2a3b533e215] Simply Connected Plane Regions and Global Harmonic Conjugates
> Suppose that $\Omega$ is a region (open and connected). Then every harmonic function $u$ on $\Omega$ has a harmonic conjugate $v$ on $\Omega$ if and only if $\Omega$ is simply connected.
````

## 4. Restore source wording; retain only the actual correction.

### Before

````text
The author calls the angle $\alpha(x,y)$ the harmonic measure of $(a,b)$. In the usual normalized convention, the harmonic measure is $\alpha(x,y)/\pi$, which takes values between zero and one.
````
### After

````text
The function $\alpha(x,y)/\pi$ is called the harmonic measure of the interval $(a,b)$.
````

## 5. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|144da62d-4427-57b4-ac3a-8afa8fc7b053.local at=0803b93e-4117-5d9d-9123-298a06c10d2d] Cauchy–Riemann Characterization and Derivative of an Analytic Function
> The function $f(z)=u(x, y)+i v(x, y)$ is analytic in an open set $S$ if and only if the partial derivatives of $u$ and $v$ are continuous and satisfy the Cauchy-Riemann equations
>
> $$
> u_{x}=v_{y} \quad \text { and } \quad u_{y}=-v_{x} .
> $$
>
> Furthermore, if $f$ is analytic, then the derivative $f^{\prime}(z)$ is given as either of
>
> $$
> f^{\prime}(z)=u_{x}(x, y)+i v_{x}(x, y) \text { or } f^{\prime}(z)=v_{y}(x, y)-i u_{y}(x, y) .
> $$
````
### After

````text
> [!theorem|144da62d-4427-57b4-ac3a-8afa8fc7b053.local at=0803b93e-4117-5d9d-9123-298a06c10d2d] Cauchy-Riemann Equations
> The function $f(z)=u(x, y)+i v(x, y)$ is analytic in an open set $S$ if and only if the partial derivatives of $u$ and $v$ are continuous and satisfy the Cauchy-Riemann equations
>
> $$
> u_{x}=v_{y} \quad \text { and } \quad u_{y}=-v_{x} .
> $$
>
> Furthermore, if $f$ is analytic, then the derivative $f^{\prime}(z)$ is given as either of
>
> $$
> f^{\prime}(z)=u_{x}(x, y)+i v_{x}(x, y) \text { or } f^{\prime}(z)=v_{y}(x, y)-i u_{y}(x, y) .
> $$
````

## 6. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|52a6a037-84b9-5823-bda1-5ba137365ab9.local at=f28a0cb1-e92f-5908-b201-1cad8e00aa98] Linear Combination, Product, Quotient, and Chain Rules for Analytic Functions
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
> (f \circ g)^{\prime}\left(z_{0}\right)=f^{\prime}\left(g\left(z_{0}\right)\right) g^{\prime}\left(z_0\right)
> $$
````
### After

````text
> [!theorem|52a6a037-84b9-5823-bda1-5ba137365ab9.local at=f28a0cb1-e92f-5908-b201-1cad8e00aa98] Properties of Analytic Functions
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
> (f \circ g)^{\prime}\left(z_{0}\right)=f^{\prime}\left(g\left(z_{0}\right)\right) g^{\prime}\left(z_0\right)
> $$
````

## 7. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|b7a06797-f906-50ff-8bce-f74fe316c00c.local at=23d4e2e9-dc45-5f38-a0ef-c7277625cf49] Real and Imaginary Parts of an Analytic Function Are Harmonic
> Suppose that $f=u+i v$ is analytic on an open set $S$. Then its real and imaginary parts, $u(x, y)$ and $v(x, y)$, are harmonic on $S$; that is, $u$ and $v$ satisfy Laplace's equation $\nabla^{2} \phi=0$ on $S$.
````
### After

````text
> [!theorem|b7a06797-f906-50ff-8bce-f74fe316c00c.local at=23d4e2e9-dc45-5f38-a0ef-c7277625cf49] Analytic Functions and Laplace's Equation
> Suppose that $f=u+i v$ is analytic on an open set $S$. Then its real and imaginary parts, $u(x, y)$ and $v(x, y)$, are harmonic on $S$; that is, $u$ and $v$ satisfy Laplace's equation $\nabla^{2} \phi=0$ on $S$.
````

## 8. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|d0d34a97-7afe-5050-b4d6-aa73417469ef.local at=9952bf75-89e2-556b-83d0-c2a3b533e215] Simply Connected Plane Regions and Global Harmonic Conjugates
> Suppose that $\Omega$ is a region (open and connected). Then every harmonic function $u$ on $\Omega$ has a harmonic conjugate $v$ on $\Omega$ if and only if $\Omega$ is simply connected.
````
### After

````text
> [!theorem|d0d34a97-7afe-5050-b4d6-aa73417469ef.local at=9952bf75-89e2-556b-83d0-c2a3b533e215] Harmonic Conjugate
> Suppose that $\Omega$ is a region (open and connected). Then every harmonic function $u$ on $\Omega$ has a harmonic conjugate $v$ on $\Omega$ if and only if $\Omega$ is simply connected.
````

## 9. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|504a572f-b3e7-5934-a665-bc458cbe57bb.local at=cae4b1cb-c767-50df-aeee-fa994f060043] Orthogonality of Regular Level Curves of Harmonic Conjugates
> Let $u+iv$ be analytic on an open subset of $\mathbb C$. At every point where its complex derivative is nonzero, the level curves of $u$ and $v$ through that point are regular and meet at right angles. Equivalently, $\nabla u\cdot\nabla v=0$ and $|\nabla u|=|\nabla v|>0$ there. Critical points require separate treatment.
````
### After

````text
> [!theorem|504a572f-b3e7-5934-a665-bc458cbe57bb.local at=cae4b1cb-c767-50df-aeee-fa994f060043] Orthogonal Trajectories
> Let $u+iv$ be analytic on an open subset of $\mathbb C$. At every point where its complex derivative is nonzero, the level curves of $u$ and $v$ through that point are regular and meet at right angles. Equivalently, $\nabla u\cdot\nabla v=0$ and $|\nabla u|=|\nabla v|>0$ there. Critical points require separate treatment.
````

## 10. Move correction/commentary into the separate editorial record; keep the actual correction in the reading text.

### Before

````text
[Source correction: the electric field uses the negative gradient.]
````
### After

````text

````
