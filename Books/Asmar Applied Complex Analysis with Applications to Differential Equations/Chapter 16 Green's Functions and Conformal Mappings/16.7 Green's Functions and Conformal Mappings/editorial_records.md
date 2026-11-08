
# Editorial records

Reading note: 16.7 Green's Functions and Conformal Mappings.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem] Möbius Automorphisms of the Unit Disk
> Let $z_{0}$ be a complex number in $D=\{z\in\mathbb C:|z|<1\}$ (thus $|z_0|<1$ ). Consider the linear fractional transformation
>
> $$
> f_{z_{0}}(z)=\frac{z-z_{0}}{1-\overline{z_{0}} z} .
> $$
>
> Then (i) $f_{z_{0}}$ is analytic on $D$;
> (ii) $f_{z_{0}}$ maps $D$ one-to-one onto $D$;
> (iii) $f_{z_{0}}$ maps the unit circle onto the unit circle;
> (iv) $f_{z_{0}}\left(z_{0}\right)=0$. Every conformal bijection of the unit disk onto itself has the form $e^{i\theta}f_{z_0}(z)$ for some real $\theta$ and some $z_0\in D$.
````
### After

````text
> [!theorem] Möbius Automorphisms of the Unit Disk
> Let $z_{0}$ be a complex number in $D=\{z\in\mathbb C:|z|<1\}$ (thus $|z_0|<1$ ). Consider the linear fractional transformation
>
> $$
> f_{z_{0}}(z)=\frac{z-z_{0}}{1-\overline{z_{0}} z} .
> $$
>
> Then (i) $f_{z_{0}}$ is analytic on $D$;
> (ii) $f_{z_{0}}$ maps $D$ one-to-one onto $D$;
> (iii) $f_{z_{0}}$ maps the unit circle onto the unit circle;
> (iv) $f_{z_{0}}\left(z_{0}\right)=0$.
````

## 2. Restore the source half-plane map symbol while preserving the corrected distinction from its disk composition.

### Before

````text
Let $q(z)=z^2$, which maps the first quadrant conformally onto the upper half-plane. Composing with the Cayley map gives $\Phi(z)=(i-z^2)/(i+z^2)$, a conformal bijection onto the disk. Applying the disk formula and simplifying as in the preceding example gives

$$
\begin{aligned}
G(z,z_0)
&=\log\left|\frac{\Phi(z)-\Phi(z_0)}{1-\overline{\Phi(z_0)}\Phi(z)}\right|\\
&=\log\left|\frac{q(z)-q(z_0)}{q(z)-\overline{q(z_0)}}\right|
=\log\left|\frac{z^2-z_0^2}{z^2-\overline{z_0}^{\,2}}\right|.
\end{aligned}
$$

*Printed equation labels: (9) disk-map expression; (10) equivalent half-plane expression and its square-map specialization.*

[Notation clarification: $q$ denotes the map to the half-plane, while $\Phi$ denotes its composition with the Cayley map to the disk.]
````
### After

````text
Let $\phi(z)=z^2$, which maps the first quadrant conformally onto the upper half-plane. Composing with the Cayley map gives $\Phi(z)=(i-z^2)/(i+z^2)$, a conformal bijection onto the disk. Applying the disk formula and simplifying as in the preceding example gives

$$
\begin{aligned}
G(z,z_0)
&=\log\left|\frac{\Phi(z)-\Phi(z_0)}{1-\overline{\Phi(z_0)}\Phi(z)}\right|\\
&=\log\left|\frac{\phi(z)-\phi(z_0)}{\phi(z)-\overline{\phi(z_0)}}\right|
=\log\left|\frac{z^2-z_0^2}{z^2-\overline{z_0}^{\,2}}\right|.
\end{aligned}
$$

*Printed equation labels: (9) disk-map expression; (10) equivalent half-plane expression and its square-map specialization.*

[Notation clarification: $\phi$ denotes the map to the half-plane, while $\Phi$ denotes its composition with the Cayley map to the disk.]
````

## 3. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem] Planar Green Function from a Disk Map Sending Its Pole to the Origin
> Let $\Omega\subsetneq\mathbb C$ be simply connected and let $z_0\in\Omega$. Suppose $\phi(\cdot,z_0)$ is a conformal bijection onto the unit disk with $\phi(z_0,z_0)=0$. Assume the boundary correspondence used here extends to the relevant boundary points with $|\phi|=1$. Use the planar Dirichlet Green function normalized by $G(z,z_0)=\log|z-z_0|+h(z,z_0)$, with $h(\cdot,z_0)$ harmonic and $G=0$ on the boundary; this corresponds to $\Delta_zG=2\pi\delta_{z_0}$.
>
> Then, for $z\in\Omega\setminus\{z_0\}$,
>
> $$
> G(z,z_0)=\log|\phi(z,z_0)|.
> $$
````
### After

````text
> [!theorem] Conformal Mapping Formula for Green's Function
> Let $\Omega\subsetneq\mathbb C$ be simply connected and let $z_0\in\Omega$. Suppose $\phi(\cdot,z_0)$ is a conformal bijection onto the unit disk with $\phi(z_0,z_0)=0$. Assume the boundary correspondence used here extends to the relevant boundary points with $|\phi|=1$. Use the planar Dirichlet Green function normalized by $G(z,z_0)=\log|z-z_0|+h(z,z_0)$, with $h(\cdot,z_0)$ harmonic and $G=0$ on the boundary; this corresponds to $\Delta_zG=2\pi\delta_{z_0}$.
>
> Then, for $z\in\Omega\setminus\{z_0\}$,
>
> $$
> G(z,z_0)=\log|\phi(z,z_0)|.
> $$
````

## 4. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!proposition] Injectivity, Composition, and Inverse of Möbius Transformations
> Let $f(z)=(az+b)/(cz+d)$ with complex coefficients satisfying $ad-bc\ne0$, regarded as a map of the extended complex plane.
>
> (i) A linear fractional transformation is one-to-one.
> (ii) The composition of any two linear fractional transformations is another linear fractional transformation.
> (iii) The inverse of the linear fractional transformation $f$ is the linear fractional transformation
>
> $$
> f^{-1}(z)=\frac{d z-b}{-c z+a}
> $$
````
### After

````text
> [!proposition] Linear Fractional Transformations
> Let $f(z)=(az+b)/(cz+d)$ with complex coefficients satisfying $ad-bc\ne0$, regarded as a map of the extended complex plane.
>
> (i) A linear fractional transformation is one-to-one.
> (ii) The composition of any two linear fractional transformations is another linear fractional transformation.
> (iii) The inverse of the linear fractional transformation $f$ is the linear fractional transformation
>
> $$
> f^{-1}(z)=\frac{d z-b}{-c z+a}
> $$
````

## 5. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem] Möbius Automorphisms of the Unit Disk
> Let $z_{0}$ be a complex number in $D=\{z\in\mathbb C:|z|<1\}$ (thus $|z_0|<1$ ). Consider the linear fractional transformation
>
> $$
> f_{z_{0}}(z)=\frac{z-z_{0}}{1-\overline{z_{0}} z} .
> $$
>
> Then (i) $f_{z_{0}}$ is analytic on $D$;
> (ii) $f_{z_{0}}$ maps $D$ one-to-one onto $D$;
> (iii) $f_{z_{0}}$ maps the unit circle onto the unit circle;
> (iv) $f_{z_{0}}\left(z_{0}\right)=0$.
````
### After

````text
> [!theorem] Conformal Mappings of the Disk onto Itself
> Let $z_{0}$ be a complex number in $D=\{z\in\mathbb C:|z|<1\}$ (thus $|z_0|<1$ ). Consider the linear fractional transformation
>
> $$
> f_{z_{0}}(z)=\frac{z-z_{0}}{1-\overline{z_{0}} z} .
> $$
>
> Then (i) $f_{z_{0}}$ is analytic on $D$;
> (ii) $f_{z_{0}}$ maps $D$ one-to-one onto $D$;
> (iii) $f_{z_{0}}$ maps the unit circle onto the unit circle;
> (iv) $f_{z_{0}}\left(z_{0}\right)=0$.
````

## 6. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem] Planar Green Function from an Arbitrary Conformal Map to the Unit Disk
> Let $\Omega\subsetneq\mathbb C$ be simply connected and $\phi:\Omega\to D$ a conformal bijection onto the unit disk, with the assumed boundary correspondence. Use the planar Dirichlet Green function normalized by $G(z,z_0)=\log|z-z_0|+h(z,z_0)$, with $h(\cdot,z_0)$ harmonic and $G=0$ on the boundary; this corresponds to $\Delta_zG=2\pi\delta_{z_0}$.
>
> For distinct $z,z_0\in\Omega$,
>
> $$
> G(z,z_0)=\log\left|\frac{\phi(z)-\phi(z_0)}{1-\overline{\phi(z_0)}\phi(z)}\right|.
> $$
````
### After

````text
> [!theorem] Conformal Mapping Formula for Green's Function
> Let $\Omega\subsetneq\mathbb C$ be simply connected and $\phi:\Omega\to D$ a conformal bijection onto the unit disk, with the assumed boundary correspondence. Use the planar Dirichlet Green function normalized by $G(z,z_0)=\log|z-z_0|+h(z,z_0)$, with $h(\cdot,z_0)$ harmonic and $G=0$ on the boundary; this corresponds to $\Delta_zG=2\pi\delta_{z_0}$.
>
> For distinct $z,z_0\in\Omega$,
>
> $$
> G(z,z_0)=\log\left|\frac{\phi(z)-\phi(z_0)}{1-\overline{\phi(z_0)}\phi(z)}\right|.
> $$
````

## 7. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem] Planar Green Function from a Conformal Map to the Upper Half-Plane
> Let $\Omega\subsetneq\mathbb C$ be simply connected and $\phi:\Omega\to\{w:\operatorname{Im}w>0\}$ a conformal bijection, with boundary correspondence to the extended real axis. Use the planar Dirichlet Green function normalized by $G(z,z_0)=\log|z-z_0|+h(z,z_0)$, with $h(\cdot,z_0)$ harmonic and $G=0$ on the boundary; this corresponds to $\Delta_zG=2\pi\delta_{z_0}$.
>
> For distinct $z,z_0\in\Omega$,
>
> $$
> G(z,z_0)=\log\left|\frac{\phi(z)-\phi(z_0)}{\phi(z)-\overline{\phi(z_0)}}\right|.
> $$
````
### After

````text
> [!theorem] Conformal Mapping Formula for Green's Function
> Let $\Omega\subsetneq\mathbb C$ be simply connected and $\phi:\Omega\to\{w:\operatorname{Im}w>0\}$ a conformal bijection, with boundary correspondence to the extended real axis. Use the planar Dirichlet Green function normalized by $G(z,z_0)=\log|z-z_0|+h(z,z_0)$, with $h(\cdot,z_0)$ harmonic and $G=0$ on the boundary; this corresponds to $\Delta_zG=2\pi\delta_{z_0}$.
>
> For distinct $z,z_0\in\Omega$,
>
> $$
> G(z,z_0)=\log\left|\frac{\phi(z)-\phi(z_0)}{\phi(z)-\overline{\phi(z_0)}}\right|.
> $$
````

## 8. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem] Conformal Invariance of the Planar Dirichlet Green Function
> Let $\Omega,\Omega'\subsetneq\mathbb C$ be simply connected regions and $\phi:\Omega\to\Omega'$ a conformal bijection with the required boundary correspondence. Suppose $g(w,w_0)$ is the Dirichlet Green function on $\Omega'$ normalized by $g(w,w_0)=\log|w-w_0|+$ a function harmonic at $w_0$. Then the Green function on $\Omega$ with the same normalization is
>
> $$
> G(z,z_0)=g\bigl(\phi(z),\phi(z_0)\bigr),\qquad z,z_0\in\Omega,\ z\ne z_0.
> $$
````
### After

````text
> [!theorem] Composition of Green's Functions and Conformal Mappings
> Let $\Omega,\Omega'\subsetneq\mathbb C$ be simply connected regions and $\phi:\Omega\to\Omega'$ a conformal bijection with the required boundary correspondence. Suppose $g(w,w_0)$ is the Dirichlet Green function on $\Omega'$ normalized by $g(w,w_0)=\log|w-w_0|+$ a function harmonic at $w_0$. Then the Green function on $\Omega$ with the same normalization is
>
> $$
> G(z,z_0)=g\bigl(\phi(z),\phi(z_0)\bigr),\qquad z,z_0\in\Omega,\ z\ne z_0.
> $$
````

## 9. Move correction/commentary into the separate editorial record; keep the actual correction in the reading text.

### Before

````text
[Notation clarification: $\phi$ denotes the map to the half-plane, while $\Phi$ denotes its composition with the Cayley map to the disk.]
````
### After

````text

````
