
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

## Additional source comparison

## 1. Restore the source conformal-mapping statement and its notation; retain required map domain/normalization.

### Before

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
### After

````text
> [!theorem] Conformal Mapping Formula for Green's Function
> Suppose that $\Omega$ is a simply connected region with (nonempty) boundary $\Gamma$. Let $\phi$ be a one-to-one conformal mapping of $\Omega$ onto the upper half-plane, taking $\Gamma$ into the real line. Then Green's function for $\Omega$ is
>
> $$
> G\left(x, y, x_{0}, y_{0}\right)=\ln \left|\frac{\phi(z)-\phi\left(z_{0}\right)}{\phi(z)-\overline{\phi\left(z_{0}\right)}}\right|,
> $$
>
> where $z=x+i y$ and $z_{0}=x_{0}+i y_{0}$ are in $\Omega$.
>
> Use $G(z,z_0)=\log|z-z_0|+$ a function harmonic at $z_0$, with zero boundary values. The formulas apply for $z\ne z_0$.
````

## 2. Restore the source conformal-mapping statement and its notation; retain required map domain/normalization.

### Before

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
### After

````text
> [!theorem] Conformal Mapping Formula for Green's Function
> Suppose that $\Omega$ is a simply connected region with (nonempty) boundary $\Gamma$. Let $\phi$ be a one-to-one conformal mapping of $\Omega$ onto the unit disk. Let $z=x+iy$ and $z_0=x_0+iy_0$ be in $\Omega$. Then Green's function for $\Omega$ is
>
> $$
> G\left(x, y, x_{0}, y_{0}\right)=\ln \left|\frac{\phi(z)-\phi\left(z_0\right)}{1-\overline{\phi\left(z_0\right)} \phi(z)}\right| .
> $$
>
> Use $G(z,z_0)=\log|z-z_0|+$ a function harmonic at $z_0$, with zero boundary values. The formulas apply for $z\ne z_0$.
````

## 3. Restore the source conformal-mapping statement and its notation; retain required map domain/normalization.

### Before

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
### After

````text
> [!theorem] Conformal Mapping Formula for Green's Function
> Suppose that $\Omega$ is a simply connected region with (nonempty) boundary $\Gamma$. Let $z=x+i y$ and $z_{0}=x_{0}+i y_{0}$ be in $\Omega$, and let $\phi\left(z, z_{0}\right)$ be the conformal mapping onto the unit disk, with $\phi(z_0,z_0)=0$ and the boundary correspondence $|\phi|=1$. Then the Green's function on $\Omega$ is
>
> $$
> G\left(x, y, x_{0}, y_{0}\right)=\ln \left|\phi\left(z,z_0\right)\right| .
> $$
>
> Use $G(z,z_0)=\log|z-z_0|+$ a function harmonic at $z_0$, with zero boundary values. The formulas apply for $z\ne z_0$.
````

## 4. Restore source wording; retain only the actual correction.

### Before

````text
> [!theorem] Composition of Green's Functions and Conformal Mappings
> Let $\Omega,\Omega'\subsetneq\mathbb C$ be simply connected regions and $\phi:\Omega\to\Omega'$ a conformal bijection with the required boundary correspondence. Suppose $g(w,w_0)$ is the Dirichlet Green function on $\Omega'$ normalized by $g(w,w_0)=\log|w-w_0|+$ a function harmonic at $w_0$. Then the Green function on $\Omega$ with the same normalization is
>
> $$
> G(z,z_0)=g\bigl(\phi(z),\phi(z_0)\bigr),\qquad z,z_0\in\Omega,\ z\ne z_0.
> $$
````
### After

````text
> [!theorem] Composition of Green's Functions and Conformal Mappings
> Suppose that $\Omega$ and $\Omega^{\prime}$ are simply connected regions with (nonempty) boundaries $\Gamma$ and $\Gamma^{\prime}$, respectively. Suppose that $\phi$ is a one-to-one conformal mapping of $\Omega$ onto $\Omega^{\prime}$, such that $\phi[\Gamma]$ is contained in $\Gamma^{\prime}$. Let $g\left(x, y, x_{0}, y_{0}\right)=g\left(x+i y, x_{0}+i y_{0}\right)$ denote the Green's function for $\Omega^{\prime}$. Then Green's function for $\Omega$ is
>
> $$
> G\left(x, y, x_{0}, y_{0}\right)=g\left(\phi(x+i y), \phi\left(x_{0}+i y_{0}\right)\right)
> $$
>
> Use $G(z,z_0)=\log|z-z_0|+$ a function harmonic at $z_0$, with zero boundary values. The formulas apply for $z\ne z_0$.
````

## Source-to-current comparison

Source: /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 16 Green's Functions and Conformal Mappings/16.7 Green's Functions and Conformal Mappings.md

This exact comparison preserves the full change evidence, including formatting, OCR corrections, restored source wording, and required standalone context. The entries above explain the recovery edits. The comparison is not a claim that every difference is a correction; component serialization, callout wrapping, and printed labels outside callouts are formatting.

`````diff
--- /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 16 Green's Functions and Conformal Mappings/16.7 Green's Functions and Conformal Mappings.md
+++ /Users/gradyclopton/ObsidianVaults/complex_analysis/Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 16 Green's Functions and Conformal Mappings/16.7 Green's Functions and Conformal Mappings.md
@@ -1,59 +1,84 @@
+
 ### 16.7 Green's Functions and Conformal Mappings
 
-In this section we present useful formulas for Green's function on a simply connected region $\Omega$ in terms of conformal mappings of $\Omega$ onto the unit disk or the upper half-plane. We then calculate these formulas explicitely for regions such as disks, half-planes, sectors, and strips (semi-infinite and infinite). Wo begin by setting the notation: $D$ denotes the open unit disk, $C$ the unit circle, and $\Omega$ a simply connected region other than the entire plane, with boundary $\Gamma$. Thus $\Omega$ is open, connected, with no holes in it, and its boundary is nonempty. For $z_{0}$ in $\Omega$, let $\phi\left(z, z_{0}\right)$ denote a one-to-one conformal mapping of $\Omega$ onto $D$, such that $\phi$ maps the boundary $\Gamma$ into $C$ and $\phi\left(z_{0}, z_{0}\right)=0$ (Figure 1). Thus
+In this section we present useful formulas for Green's function on a simply connected region $\Omega$ in terms of conformal mappings of $\Omega$ onto the unit disk or the upper half-plane. We then calculate these formulas explicitly for regions such as disks, half-planes, sectors, and strips (semi-infinite and infinite). We begin by setting the notation: $D$ denotes the open unit disk, $C$ the unit circle, and $\Omega$ a simply connected region other than the entire plane, with boundary $\Gamma$. Thus $\Omega$ is open, connected, with no holes in it, and its boundary is nonempty. For $z_{0}$ in $\Omega$, let $\phi\left(z, z_{0}\right)$ denote a one-to-one conformal mapping of $\Omega$ onto $D$, such that $\phi$ maps the boundary $\Gamma$ into $C$ and $\phi\left(z_{0}, z_{0}\right)=0$ (Figure 1). Thus
 
 $$
 \left|\phi\left(z, z_{0}\right)\right|=1 \text { for all } z \text { on } \Gamma .
-$$
-
-## THEOREM 1 CONFORMAL MAPPING FORMULA FOR GREEN'S FUNCTION
-
-Figure 1 Because $\phi\left(z, z_{0}\right)$ belongs to the unit circle if $z$ is on $\Gamma$, we have $\left|\phi\left(z, z_{0}\right)\right|=1$ for $z$ on $\Gamma$. Moreover, since $\phi$ is one-to-one, $z_{0}$ is the only complex number in $\Omega$ such that $\phi\left(z, z_{0}\right)=0$.
-![](./images/7ce1063d-f13d-4631-8956-8a97e0eaf48a-64_433_992_804_648.jpg)
-
-Write $z=x+i y$ and $z_{0}=x_{0}+i y_{0}$, and think of $\phi\left(s, z_{0}\right)$ as a function of $x$, $y, x_{0}$, and $y_{0}$, in the obvious way. Here is the main result of the section.
-
-Suppose that $\Omega$ is a simply connected region with (nonempty) boundary $\Gamma$. Let $z=x+i y$ and $z_{0}=x_{0}+i y_{0}$ be in $\Omega$, and let $\phi\left(z, z_{0}\right)$ be the conformal mapping as described above. Then the Green's function on $\Omega$ is
-
-$$
-G\left(x, y, x_{0}, y_{0}\right)=\ln \left|\phi\left(z, x_{0}\right)\right| .
-$$
+\tag{1}
+$$
+
+
+```scientific-figure
+id: 5f78424c-ddd6-44a0-912b-ab61fbbbcca8
+numbered: false
+title: ""
+caption: Figure 1 Because $\phi\left(z, z_{0}\right)$ belongs to the unit circle if $z$ is on $\Gamma$, we have $\left|\phi\left(z, z_{0}\right)\right|=1$ for $z$ on $\Gamma$. Moreover, since $\phi$ is one-to-one, $z_{0}$ is the only complex number in $\Omega$ such that $\phi\left(z, z_{0}\right)=0$.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 16 Green's Functions and Conformal Mappings/images/7ce1063d-f13d-4631-8956-8a97e0eaf48a-64_433_992_804_648.jpg
+    caption: ""
+```
+
+
+Write $z=x+i y$ and $z_{0}=x_{0}+i y_{0}$, and think of $\phi(z,z_0)$ as a function of $x$, $y, x_{0}$, and $y_{0}$, in the obvious way. Here is the main result of the section.
+
+> [!theorem] Conformal Mapping Formula for Green's Function
+> Suppose that $\Omega$ is a simply connected region with (nonempty) boundary $\Gamma$. Let $z=x+i y$ and $z_{0}=x_{0}+i y_{0}$ be in $\Omega$, and let $\phi\left(z, z_{0}\right)$ be the conformal mapping onto the unit disk, with $\phi(z_0,z_0)=0$ and the boundary correspondence $|\phi|=1$. Then the Green's function on $\Omega$ is
+>
+> $$
+> G\left(x, y, x_{0}, y_{0}\right)=\ln \left|\phi\left(z,z_0\right)\right| .
+> $$
+>
+> Use $G(z,z_0)=\log|z-z_0|+$ a function harmonic at $z_0$, with zero boundary values. The formulas apply for $z\ne z_0$.
+
+*Printed equation label: (2).*
 
 It is instructive at this point to verify some of the characteristic properties of Green's function that we stated in Theorem 3, Section 16.3, using properties of the conformal mapping $\phi$. We postpone the full proof of the theorem until the end of this section.
 
 - The function $\ln \left|\phi\left(z, z_{0}\right)\right|$ is the composition of $\phi\left(z, z_{0}\right)$ and $\ln |z|$. The function $\phi$ is analytic on $\Omega$ and is nonzero for all $z \neq z_{0}$, because only $z_{0}$ is mapped to 0 in $D$. The function $\ln |z|=\frac{1}{2} \ln \left(x^{2}+y^{2}\right)$ is harmonic for all $z \neq 0$. Consequently, by Theorem 1, Section 16.6, $\ln \left|\phi\left(z, z_{0}\right)\right|$ is harmonic for all $z \neq z_{0}$ in $\Omega$. Thus property (i) of Theorem 3, Section 16.3, is verified.
 - Recall that $\phi\left(z, z_{0}\right)$ belongs to the unit circle $C$ if $z$ is on $\Gamma$; hence, for $z$ on $\Gamma,\left|\phi\left(z, z_{0}\right)\right|=1$, and so $\ln \left|\phi\left(z, z_{0}\right)\right|=\ln 1=0$. Thus property (ii) of Theorem 3, Section 16.3, is verified.
 - Recall that $\phi\left(z, z_{0}\right)$ belongs to $D$, for all $z$ in $\Omega$. So $\left|\phi\left(z, z_{0}\right)\right| \leq 1$, and so $\ln \left|\phi\left(z, z_{0}\right)\right| \leq 0$, for all $z$ in $\Omega$. Thus property (iii) of Theorem 3, Section 16.3, is verified.
-- The symmetry property of $\phi\left(z, z_{0}\right)$ will become more evident as soon as we investigate the conformal mapping $\phi$ (see Theorem 3 of this section).
+- The symmetry of the Green function $\log|\phi(z,z_0)|$ will become more evident as soon as we investigate the conformal mapping $\phi$ (see Theorem 3 of this section).
 
 We make a few additional points regarding Theorem 1.
 
 - According to Theorem 1, we have to construct a conformal mapping of $\Omega$ onto $D$ for each $z_{0}$ in $\Omega$. While this is true, you will shortly see that in fact all we need is just one conformal mapping of $\Omega$ onto $D$.
 - The existence of a conformal mapping of $\Omega$ onto $D$ is guaranteed by a famous theorem, called the Riemann mapping theorem, that states that if $\Omega$ is any simply connected region in the complex plane other than the complex plane itself, then there is a one-to-one analytic function $f$ that maps $\Omega$ onto the unit disk $D$. The mapping $f$ is unique if we specify that $f\left(z_{0}\right)=0$ and $f^{\prime}\left(z_{0}\right)>0$, for some $z_{0}$ in $\Omega$.
-- While the Riemann mapping theorem does not tells us how to construct the conformal mapping, it does guarantee its existence. Combining this with Theorem 1, we conclude that Green's function exists on any simply connected region. (When $\Omega$ is the entire plane, we take $\left.G\left(z, z_{0}\right)=\ln \left|z-z_{0}\right|.\right)$
+- While the Riemann mapping theorem does not tell us how to construct the conformal mapping, it does guarantee its existence. Combining this with Theorem 1, we conclude that the Green function exists on any proper simply connected plane region. On the entire plane, $\log|z-z_0|$ is a fundamental solution with the same singularity, but it is not a nonpositive Dirichlet Green function with boundary normalization. Boundary extension of a Riemann map requires its own hypotheses; it is not part of the Riemann mapping theorem.
 
 Next, we describe all the conformal mappings of the unit disk onto itself. In addition to being interesting in its own right, this result has two purposes for us: We will use it to rederive Green's function on the disk and to simplify the construction of the conformal mapping in Theorem 1.
 
 ## Linear Fractional Transformations
 
-Let $a, b, c$, and $d$ be complex numbers with $a d-b c \neq 0$. The function
-
-$$
-f(z)=\frac{a z+b}{c z+d}
-$$
-
-is called a linear fractional transformation or Möbius transformation. If $c=0, f$ is a linear function and hence it is entire. If $c \neq 0, f(z)$ is a rational function. It is analytic for all $z \neq-\frac{d}{c}$, where the denominator vanishes. The following properties are straightforward to check.
-
-PROPOSITION 1 LINEAR FRACTIONAL TRANSFORMATIONS
-
-THEOREM 2 CONFORMAL MAPPINGS OF THE DISK ONTO ITSELF
-(i) A linear fractional transformation is one-to-one.
-(ii) The composition of any two linear fractional transformations is another linear fractional transformation.
-(iii) The inverse of the linear fractional transformation (3) is the linear fractional transformation
-
-$$
-f^{-1}(z)=\frac{d z-b}{-c z+a}
-$$
+> [!definition] Linear Fractional (Möbius) Transformation
+> Let $a, b, c$, and $d$ be complex numbers with $a d-b c \neq 0$. The function
+>
+> $$
+> f(z)=\frac{a z+b}{c z+d}
+> $$
+>
+> is called a linear fractional transformation or Möbius transformation. It acts on the extended complex plane $\widehat{\mathbb C}$, assigning the pole to $\infty$ and using the limiting value at $\infty$.
+
+*Printed equation label: (3).*
+
+If $c=0, f$ is a linear function and hence it is entire. If $c \neq 0, f(z)$ is a rational function. It is analytic for all $z \neq-\frac{d}{c}$, where the denominator vanishes. The following properties are straightforward to check.
+
+
+> [!proposition] Linear Fractional Transformations
+> Let $f(z)=(az+b)/(cz+d)$ with complex coefficients satisfying $ad-bc\ne0$, regarded as a map of the extended complex plane.
+>
+> (i) A linear fractional transformation is one-to-one.
+> (ii) The composition of any two linear fractional transformations is another linear fractional transformation.
+> (iii) The inverse of the linear fractional transformation $f$ is the linear fractional transformation
+>
+> $$
+> f^{-1}(z)=\frac{d z-b}{-c z+a}
+> $$
+
+*Printed equation label: (4).*
 
 Proof We prove (i) and (iii) and leave (ii) as an exercise. We start with (iii). We have to check that $f \circ f^{-1}(z)=f^{-1} \circ f(z)=z$. We have
 
@@ -68,30 +93,34 @@
 
 The next theorem deals with a particular family of linear fractional transformations.
 
-Let $z_{0}$ be a complex number in $D$ (thus $\left.\right|_{0} \mid<1$ ). Consider the linear fractional transformation
-
-$$
-f_{z_{0}}(z)=\frac{z-z_{0}}{1-\overline{z_{0}} z} .
-$$
-
-Then (i) $f_{z_{0}}$ is analytic on $D$;
-(ii) $f_{z_{0}}$ maps $D$ one-to-one onto $D$;
-(iii) $f_{z_{0}}$ maps the unit circle onto the unit circle;
-(iv) $f_{z_{0}}\left(z_{0}\right)=0$.
-
-Proof Part (iv) is clear. From Proposition 1, we know that $f_{z_{0}}$ is one-to-one. It is also analytic for all $z \neq \frac{1}{\frac{1}{20}^{\circ}}$. But
+> [!theorem] Conformal Mappings of the Disk onto Itself
+> Let $z_{0}$ be a complex number in $D=\{z\in\mathbb C:|z|<1\}$ (thus $|z_0|<1$ ). Consider the linear fractional transformation
+>
+> $$
+> f_{z_{0}}(z)=\frac{z-z_{0}}{1-\overline{z_{0}} z} .
+> $$
+>
+> Then (i) $f_{z_{0}}$ is analytic on $D$;
+> (ii) $f_{z_{0}}$ maps $D$ one-to-one onto $D$;
+> (iii) $f_{z_{0}}$ maps the unit circle onto the unit circle;
+> (iv) $f_{z_{0}}\left(z_{0}\right)=0$.
+
+*Printed equation label: (5).*
+
+Proof Part (iv) is clear. From Proposition 1, we know that $f_{z_{0}}$ is one-to-one. When $z_0=0$, it is the identity map. When $z_0\ne0$, its only finite pole is $1/\overline{z_0}$. But
 
 $$
 \left|\frac{1}{\bar{z}_{0}}\right|=\frac{1}{\left|\overline{z_{0}}\right|}=\frac{1}{\left|z_{0}\right|}>1,
 $$
 
-because $\left|z_{0}\right|<1$. So the point where $f_{z_{0}}$ is not analytic, $\left(\overline{z_{0}}\right)^{-1}$, is not in $D$, which proves (i). Parts (ii) and (iii) are more interesting. For (iii), let $\varepsilon^{i \theta}$ denote a complex number with modulus 1 . We want to show that $\left|f_{z_{0}}\left(e^{i \theta}\right)\right|=1$. We use tricks with the absolute value and complex conjugation:
-
-$$
-\begin{aligned}
-&\left|f_{z_{0}}\left(e^{i \theta}\right)\right|=\frac{\left|e^{i \theta}-z_{0}\right|}{\left|1-\overline{z_{0}} e^{i \theta}\right|}=\frac{\left|e^{i \theta}-z_{0}\right|}{\left|e^{i \theta}\left(e^{-i \theta}-\overline{z_{0}}\right)\right|}=\frac{\left|e^{i \theta}-z_{0}\right|}{\left|e^{i \theta}\right| \cdot\left|e^{-i \theta}-\overline{z_{0}}\right|} \\
-& \left.=\frac{\left|e^{i \theta}-z_{0}\right|}{\left|e^{-i \theta}-\overline{z_{0}}\right|}=\frac{\left|e^{i \theta}-z_{0}\right|}{\mid \overline{e^{i \theta}}-z_{0}} \right\rvert\, \\
-& \left\lvert\, \frac{\left|e^{i \theta}-z_{0}\right|}{\left|e^{i \theta}-z_{0}\right|}=1 .\right.
+because $\left|z_{0}\right|<1$. So the point where $f_{z_{0}}$ is not analytic, $\left(\overline{z_{0}}\right)^{-1}$, is not in $D$, which proves (i). Parts (ii) and (iii) are more interesting. For (iii), let $e^{i\theta}$ denote a complex number with modulus 1 . We want to show that $\left|f_{z_{0}}\left(e^{i \theta}\right)\right|=1$. We use tricks with the absolute value and complex conjugation:
+
+$$
+\begin{aligned}
+|f_{z_0}(e^{i\theta})|
+&=\frac{|e^{i\theta}-z_0|}{|1-\overline{z_0}e^{i\theta}|}
+=\frac{|e^{i\theta}-z_0|}{|e^{i\theta}|\,|e^{-i\theta}-\overline{z_0}|}\\
+&=\frac{|e^{i\theta}-z_0|}{|\overline{e^{i\theta}-z_0}|}=1.
 \end{aligned}
 $$
 
@@ -99,28 +128,36 @@
 
 Using properties of analytic functions, it can be shown that, up to a constant factor of modulus 1 , any one-to-one conformal mapping of the unit disk onto itself is of the form (5) (see [1], Section 6.2). Thus Theorem 2 characterizes all the conformal mappings of the unit disk onto itself. We now combine Theorems 1 and 2 to obtain the Green's function for the unit disk.
 
-## EXAMPLE 1 Green's function for the unit disk
-
-Let $z$ and $z_{0}$ be in $D$. By Theorem 2, $f_{z_{0}}(z)=\frac{z-z_{0}}{1-\overline{z_{0}} z}$ is a one-to-one conformal mapping of the unit clisk onto itself that maps $z_{0}$ to 0 . By Theorem 1 Green's function for the unit disk is
+> [!exercise] EXAMPLE 1 Green's function for the unit disk
+> Use a disk automorphism to derive the Green function for the unit disk with pole $z_0$, normalized by a positive logarithmic singularity.
+
+##### solution
+
+Let $z$ and $z_{0}$ be in $D$. By Theorem 2, $f_{z_{0}}(z)=\frac{z-z_{0}}{1-\overline{z_{0}} z}$ is a one-to-one conformal mapping of the unit disk onto itself that maps $z_{0}$ to 0 . By Theorem 1 Green's function for the unit disk is
 
 $$
 G\left(z, z_{0}\right)=\ln \left|\frac{z-z_{0}}{1-\overline{z_{0}} z}\right| .
+\tag{6}
 $$
 
 To compare with the formula that we found in Section 16.4 , substitute $z=x+i y$ and $z_{0}=x_{0}+i y_{0}$ (Exercise 13).
 
 Our second application of Theorem 2 is to simplify the construction of the mappings in Theorem 1. We have the following version of Green's formula.
 
-THEOREM 3 CONFORMAL MAPPING FORMULA FOR GREEN'S FUNCTION
-
-Suppose that $\Omega$ is a simply connected region with (nonempty) boundary $\Gamma$. Let $\phi$ be a one-to-one conformal mapping of $\Omega$ onto the unit disk. Let $\approx=x+i y$ and $\varepsilon_{0}=x_{0}+i y_{0}$ be in $\Omega$. Then Green's function for $\Omega$ is
-
-$$
-G\left(x, y, x_{0}, y_{0}\right)=\ln \left|\frac{\phi(z)-\phi\left(\sigma_{0}\right)}{1-\overline{\phi\left(\sigma_{0}\right)} \phi(z)}\right| .
-$$
-
-It is immediate from (7) that Greens function is symmetric (Thcorem 3 (v). Section 16.3); that is, $G\left(z, z_{0}\right)=G\left(z_{0}, z\right)$.
-Proof Note that the function insicle the absolute value in (7) is $f_{\phi\left(z_{0}\right)} \circ \phi(z)$, where $f_{\phi\left(z_{0}\right)}$ is a linear fractional transformation of the form (5), with $z_{0}$ replaced by $\phi\left(z_{0}\right)$. Since $\phi$ is a one-to-one conformal mapping of $\Omega$ onto $D$ and $f_{\phi\left(z_{0}\right)}$ is a one-to-one conformal mapping of $D$ onto $D$. it follows that $f_{\phi\left(z_{0}\right)} \circ \phi(z)$ is a one-to-one conformal mapping of $\Omega$ onto $D$. Clearly, $f_{\phi\left(z_{0}\right)} \circ \phi\left(z_{0}\right)=0$; hence the mapping $f_{\phi\left(z_{0}\right)} \circ \phi(z)$ has all the properties of the mapping $\phi\left(z . z_{0}\right)$ in Theorem 1, and so Theorem 3 follows now from Theorem 1.
+
+> [!theorem] Conformal Mapping Formula for Green's Function
+> Suppose that $\Omega$ is a simply connected region with (nonempty) boundary $\Gamma$. Let $\phi$ be a one-to-one conformal mapping of $\Omega$ onto the unit disk. Let $z=x+iy$ and $z_0=x_0+iy_0$ be in $\Omega$. Then Green's function for $\Omega$ is
+>
+> $$
+> G\left(x, y, x_{0}, y_{0}\right)=\ln \left|\frac{\phi(z)-\phi\left(z_0\right)}{1-\overline{\phi\left(z_0\right)} \phi(z)}\right| .
+> $$
+>
+> Use $G(z,z_0)=\log|z-z_0|+$ a function harmonic at $z_0$, with zero boundary values. The formulas apply for $z\ne z_0$.
+
+*Printed equation label: (7).*
+
+It is immediate from (7) that Green’s function is symmetric (Theorem 3 (v). Section 16.3); that is, $G\left(z, z_{0}\right)=G\left(z_{0}, z\right)$.
+Proof Note that the function inside the absolute value in (7) is $f_{\phi\left(z_{0}\right)} \circ \phi(z)$, where $f_{\phi\left(z_{0}\right)}$ is a linear fractional transformation of the form (5), with $z_{0}$ replaced by $\phi\left(z_{0}\right)$. Since $\phi$ is a one-to-one conformal mapping of $\Omega$ onto $D$ and $f_{\phi\left(z_{0}\right)}$ is a one-to-one conformal mapping of $D$ onto $D$. it follows that $f_{\phi\left(z_{0}\right)} \circ \phi(z)$ is a one-to-one conformal mapping of $\Omega$ onto $D$. Clearly, $f_{\phi\left(z_{0}\right)} \circ \phi\left(z_{0}\right)=0$; hence the mapping $f_{\phi\left(z_{0}\right)} \circ \phi(z)$ has all the properties of the mapping $\phi(z,z_0)$ in Theorem 1, and so Theorem 3 follows now from Theorem 1.
 
 From this point, the scope of the applications is unlimited. For example, given a simply connected region $\Omega$, (a) find a one-to-one conformal mapping of $\Omega$ onto the unit $D$. (b) Use Theorem 3 to get the Green's function for $\Omega$. (c) Use results, such as the ones of Section 16.3, to derive formulas for the solutions of Dirichlet problems and Poisson equations on $\Omega$.
 
@@ -130,79 +167,113 @@
 
 To construct the desired conformal mapping, we use a linear fractional transformation and the following properties:
 
-- A linear fractional transformation is uniquely determined by the images of three points.
+- A linear fractional transformation is uniquely determined by the images of three distinct points on the extended complex plane (with three distinct target points).
 - The image of a circle by a linear fractional transformation is another circle or a line, and the image of a line is also a circle or a line.
 
-The first property follows because we may assume that one of the coefficients in the linear fractional transformation is 1 . Then the other three coefficients are uniquely determined by three equations with three unknowns. One way to prove the second property is to verify it first in the case of a linear mapping. Next, verify it for the inversion mapping, $f(z)=\frac{1}{z}$. Then because an arbitrary linear fractional transformation is the composition of linear mappings and inversions, it follows that the property holds for lincar fractional transformations.
-
-## EXAMPLE 2 Mappings between the upper half-plane and the unit disk
-
-(a) Show that the linear fractional transformation
-
-$$
-\phi(z)=i \frac{1-z}{1+z}
-$$
-
-maps the unit disk onto the upper half-plane.
-(b) Show that the linear fractional transformation
-
-$$
-\psi(z)=\frac{i-z}{i+z}
-$$
-
-maps the upper half-plane onto the unit disk.
-Solution (a) Our goal is to show that the unit circle $C$ is mapped to the real axis. Because the image of a circle is either a line or a circle and because three points determine either a line or a circle, it suffices to check the images of three points on the unit circle. We have
+The first property follows because we may assume that one of the coefficients in the linear fractional transformation is 1 . Then the other three coefficients are uniquely determined by three equations with three unknowns. One way to prove the second property is to verify it first in the case of a linear mapping. Next, verify it for the inversion mapping, $f(z)=\frac{1}{z}$. Then because an arbitrary linear fractional transformation is the composition of linear mappings and inversions, it follows that the property holds for linear fractional transformations.
+
+> [!exercise] EXAMPLE 2 Mappings between the upper half-plane and the unit disk
+> (a) Show that the linear fractional transformation
+>
+> $$
+> \phi(z)=i \frac{1-z}{1+z}
+> $$
+>
+> maps the unit disk onto the upper half-plane.
+> (b) Show that the linear fractional transformation
+>
+> $$
+> \psi(z)=\frac{i-z}{i+z}
+> $$
+>
+> maps the upper half-plane onto the unit disk.
+
+##### solution
+
+(a) Our goal is to show that the unit circle $C$ is mapped to the real axis. Because the image of a circle is either a line or a circle and because three points determine either a line or a circle, it suffices to check the images of three points on the unit circle. We have
 
 $$
 \phi(1)=0 ; \quad \phi(i)=i \frac{1-i}{1+i}=1 ; \quad \phi(-i)=i \frac{1+i}{1-i}=-1 .
 $$
 
-Thus $\phi(1), \phi(i)$, and $\phi(-i)$ lie on the $u$-axis (the real axis in the $u$-planc), and so the image of $C$ is the $u$-axis. Because $\phi$ is one-to-one, it maps the boundary $C$ onto the boundary of the image of the unit disk. Thus the image of the unit disk is either the upper half-plane or the lower half-plane. Checking $\phi(0)=i$ (a point in the upper half-plane), we conclude that $\phi$ maps the unit disk one-to-one onto the upper half-plane (see Figure 2).
-
-Figure 2 One-fo one conformal mappings between the unit disk and the upper halfplane.
-![](./images/7ce1063d-f13d-4631-8956-8a97e0eaf48a-69_427_992_245_634.jpg)
-
-(b) We can do this part in at least two ways. One way is to use Proposition 1(iii) and notice that $\psi$ is the inverse of $\phi$. Another way is to check the image by $\psi$ of the boundary and one interior point. We leave it as an exercise to verify that $\psi(0)=1$, $\psi(1)=i$, and $\psi(-1)=-i$. Since the images of the three points are not collinear. we conclude that the real axis is mapped onto the circle that goes through the points $1, i$, and $-i$, which is clearly the unit circle. (Here again, we are using the fact that three points determine a circle.) Also, $v(i)=0$; hence $i$ - maps the upper half-plane onto the unit disk.
+Thus $\phi(1), \phi(i)$, and $\phi(-i)$ lie on the $u$-axis (the real axis in the $u$-plane), and so the image of $C$ is the extended real axis, with $z=-1$ mapped to infinity. Because $\phi$ is one-to-one, it maps the boundary $C$ onto the boundary of the image of the unit disk. Thus the image of the unit disk is either the upper half-plane or the lower half-plane. Checking $\phi(0)=i$ (a point in the upper half-plane), we conclude that $\phi$ maps the unit disk one-to-one onto the upper half-plane (see Figure 2).
+
+```scientific-figure
+id: 2e9ed9f6-dc08-4710-832d-edeac6e94de5
+numbered: false
+title: ""
+caption: Figure 2 One-to-one conformal mappings between the unit disk and the upper half-plane.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 16 Green's Functions and Conformal Mappings/images/7ce1063d-f13d-4631-8956-8a97e0eaf48a-69_427_992_245_634.jpg
+    caption: ""
+```
+
+
+(b) We can do this part in at least two ways. One way is to use Proposition 1(iii) and notice that $\psi$ is the inverse of $\phi$. Another way is to check the image by $\psi$ of the boundary and one interior point. We leave it as an exercise to verify that $\psi(0)=1$, $\psi(1)=i$, and $\psi(-1)=-i$. Since the images of the three points are not collinear. we conclude that the real axis is mapped onto the circle that goes through the points $1, i$, and $-i$, which is clearly the unit circle. (Here again, we are using the fact that three points determine a circle.) Also, $\psi(i)=0$; hence $\psi$ maps the upper half-plane onto the unit disk.
 
 Example 2(b) and Theorem 3 combine to give us Green's function for the upper half-plane. The formula was derived in Section 16.4 by the method of images.
 
-## EXAMPLE 3 Green's function for the upper half-plane
+> [!exercise] EXAMPLE 3 Green's function for the upper half-plane
+> Derive the upper-half-plane Green function by composing the disk formula with a Cayley map. Use the positive logarithmic normalization.
+
+##### solution
 
 Let $z$ and $z_{0}$ be in the upper half-plane. Then Green's function for the upper half-plane is
 
 $$
-G\left(\therefore z_{0}\right)=\ln \left|\frac{z-z_{0}}{z-\overline{z_{0}}}\right|=\frac{1}{2} \ln \frac{\left(x-x_{0}\right)^{2}+\left(y-y_{0}\right)^{2}}{\left(x-x_{0}\right)^{2}+\left(y+y_{0}\right)^{2}} .
+G(z,z_0)=\ln \left|\frac{z-z_{0}}{z-\overline{z_{0}}}\right|=\frac{1}{2} \ln \frac{\left(x-x_{0}\right)^{2}+\left(y-y_{0}\right)^{2}}{\left(x-x_{0}\right)^{2}+\left(y+y_{0}\right)^{2}} .
+\tag{8}
 $$
 
 To derive the formula, we use (7) and the conformal mapping in Example 2(b):
 
 $$
 \begin{aligned}
-G\left(c, z_{0}\right) & =\ln \left|\frac{\frac{i-z}{i+z}-\frac{i-z_{0}}{i+z_{0}}}{1-\overline{\left(\frac{i-z_{0}}{i+z_{0}}\right)} \frac{i-z}{i+z}}\right|=\ln \left|\frac{\frac{(i-z)\left(i+z_{0}\right)-\left(i-z_{0}\right)(i+z)}{(i+z)\left(i+z_{0}\right)}}{1-\frac{-i-\overline{z_{0}}}{-i+z_{0}} \frac{i-z}{i+z}}\right| \\
-& =\ln \left|\frac{\frac{2 i\left(z_{0}-z\right)}{(i+z)\left(i+z_{0}\right)}}{\frac{2 i\left(\overline{z_{0}}-z\right)}{(i+z)\left(-i+\overline{z_{0}}\right)}}\right|=\ln \left|\frac{z-z_{0}}{z-\overline{z_{0}}} \frac{-i+\overline{z_{0}}}{i+\overline{z_{0}}}\right|=\ln \left(\left|\frac{z-z_{0}}{z-\overline{z_{0}}}\right|\left|\frac{-i+\overline{z_{0}}}{i+z_{0}}\right|\right) .
-\end{aligned}
-$$
-
-But $-i+\overline{z_{0}}$ is the complex conjugate of $i+z_{0}$, so $\left|\frac{\overline{-i+\bar{z}_{0}}}{i+z_{0}}\right|=1$, and the formula follows. $\square$
+G(z,z_0) & =\ln \left|\frac{\frac{i-z}{i+z}-\frac{i-z_{0}}{i+z_{0}}}{1-\overline{\left(\frac{i-z_{0}}{i+z_{0}}\right)} \frac{i-z}{i+z}}\right|=\ln \left|\frac{\frac{(i-z)\left(i+z_{0}\right)-\left(i-z_{0}\right)(i+z)}{(i+z)\left(i+z_{0}\right)}}{1-\frac{-i-\overline{z_0}}{-i+\overline{z_0}} \frac{i-z}{i+z}}\right| \\
+& =\ln \left|\frac{\frac{2 i\left(z_{0}-z\right)}{(i+z)\left(i+z_{0}\right)}}{\frac{2 i\left(\overline{z_{0}}-z\right)}{(i+z)\left(-i+\overline{z_{0}}\right)}}\right|=\ln \left|\frac{z-z_{0}}{z-\overline{z_{0}}} \frac{-i+\overline{z_0}}{i+z_0}\right|=\ln \left(\left|\frac{z-z_{0}}{z-\overline{z_{0}}}\right|\left|\frac{-i+\overline{z_{0}}}{i+z_{0}}\right|\right) .
+\end{aligned}
+$$
+
+But $-i+\overline{z_{0}}$ is the complex conjugate of $i+z_{0}$, so $\left|\frac{-i+\overline{z_0}}{i+z_0}\right|=1$, and the formula follows. $\square$
 
 We now add a new Green's function to our list.
 
-![](./images/7ce1063d-f13d-4631-8956-8a97e0eaf48a-70_456_466_1595_65.jpg)
-Figure 3 A general Dirichlet problem in the first quadrant.
-
-## EXAMPLE 4 Green's function for the first quadrant
-
-Let us start by constructing a one-to-one conformal mapping of the first quadrant onto the unit disk by mapping the first quadrant onto the upper half-plane and then using the mapping in Example 2(b). Thus $\phi(z)=\frac{i-z^{2}}{i+z^{2}}$ is a one-to-one conformal mapping of the first quadrant onto the unit disk. For $z$ and $z_{0}$ in the first quadrant, use Theorem 3 to get the Green's function for the first quadrant in the form
-
-$$
-G\left(z, z_{0}\right)=\ln \left|\frac{\frac{i-\phi(z)}{i+\phi(z)}-\frac{i-\phi\left(z_{0}\right)}{i+\phi\left(z_{0}\right)}}{1-\overline{\left(\frac{i-\phi\left(z_{0}\right)}{i+\phi\left(z_{0}\right)}\right)} \overline{i-\phi(z)} \overline{i+\phi(z)}}\right| .
-$$
-
-This is the same expression as what we had in the previous example, except that $z$ and $z_{0}$ are now replaced by $\phi(z)$ and $o\left(i_{0}\right)$. Using the result of the previous example, we find:
-
-$$
-G\left(z, z_{0}\right)=\ln \left|\frac{\phi(z)-\phi\left(z_{0}\right)}{\phi(z)-\overline{\phi\left(z_{0}\right)}}\right|=\ln \left|\frac{z^{2}-z_{0}^{2}}{z^{2}-{\overline{z_{0}}}^{2}}\right| .
-$$
+```scientific-figure
+id: aaeb38cf-e3a2-497a-b3b5-edc87a01cc1a
+numbered: false
+title: ""
+caption: Figure 3 A general Dirichlet problem in the first quadrant.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 16 Green's Functions and Conformal Mappings/images/7ce1063d-f13d-4631-8956-8a97e0eaf48a-70_456_466_1595_65.jpg
+    caption: ""
+```
+
+
+> [!exercise] EXAMPLE 4 Green's function for the first quadrant
+> Derive the positive-logarithmic Green function of the first quadrant $\Omega=\{x+iy:x>0,y>0\}$ and express it in Cartesian coordinates.
+
+##### solution
+
+Let $\phi(z)=z^2$, which maps the first quadrant conformally onto the upper half-plane. Composing with the Cayley map gives $\Phi(z)=(i-z^2)/(i+z^2)$, a conformal bijection onto the disk. Applying the disk formula and simplifying as in the preceding example gives
+
+$$
+\begin{aligned}
+G(z,z_0)
+&=\log\left|\frac{\Phi(z)-\Phi(z_0)}{1-\overline{\Phi(z_0)}\Phi(z)}\right|\\
+&=\log\left|\frac{\phi(z)-\phi(z_0)}{\phi(z)-\overline{\phi(z_0)}}\right|
+=\log\left|\frac{z^2-z_0^2}{z^2-\overline{z_0}^{\,2}}\right|.
+\end{aligned}
+$$
+
+*Printed equation labels: (9) disk-map expression; (10) equivalent half-plane expression and its square-map specialization.*
+
+
 
 To express $G$ in terms of $x, y, x_{0}$, and $y_{0}$, we proceed as follows:
 
@@ -218,26 +289,27 @@
 
 In the following example, we use Green's function to derive a Poisson integral formula for the first quadrant.
 
-## EXAMPLE 5 Poisson integral formula for the first quadrant
-
-Consider the Dirichlet problem in the first quadrant $\Omega$, shown in Figure 3: $\nabla^{2} u(x, y)=$ 0 for all $(x, y)$ in $\Omega ; u(x, 0)=f(x)$ for all $x>0, u(0, y)=g(y)$ for all $y>0$. Show that the solution is given by the Poisson integral formula:
-
-$$
-\begin{aligned}
-u(x, y)= & \frac{y}{\pi} \int_{0}^{\infty} f(s)\left(\frac{1}{(x-s)^{2}+y^{2}}-\frac{1}{(x+s)^{2}+y^{2}}\right) d s \\
-& +\frac{x}{\pi} \int_{0}^{\infty} g(t)\left(\frac{1}{x^{2}+(y-t)^{2}}-\frac{1}{x^{2}+(y+t)^{2}}\right) d t
-\end{aligned}
-$$
-
-Solution According to Theorem 2, Section 16.3,
+> [!exercise] EXAMPLE 5 Poisson integral formula for the first quadrant
+> Consider the Dirichlet problem in the first quadrant $\Omega$, shown in Figure 3: $\nabla^{2} u(x, y)=$ 0 for all $(x, y)$ in $\Omega ; u(x, 0)=f(x)$ for all $x>0, u(0, y)=g(y)$ for all $y>0$. Assume $f,g$ are bounded and continuous on their open rays. Show that the bounded harmonic solution is given by the Poisson integral formula:
+>
+> $$
+> \begin{aligned}
+> u(x, y)= & \frac{y}{\pi} \int_{0}^{\infty} f(s)\left(\frac{1}{(x-s)^{2}+y^{2}}-\frac{1}{(x+s)^{2}+y^{2}}\right) d s \\
+> & +\frac{x}{\pi} \int_{0}^{\infty} g(t)\left(\frac{1}{x^{2}+(y-t)^{2}}-\frac{1}{x^{2}+(y+t)^{2}}\right) d t
+> \end{aligned}
+> $$
+
+##### solution
+
+According to Theorem 2, Section 16.3,
 
 $$
 u\left(x_{0}, y_{0}\right)=\frac{1}{2 \pi} \int_{\Gamma} u(x, y) \frac{\partial G}{\partial n}\left(x, y, x_{0}, y_{0}\right) d s
+\tag{11}
 $$
 
 where $G$ is the Green's function for the first quadrant, and $\Gamma$ is the boundary of the first quadrant. On the nonnegative $x$-axis, we have $d s=d x$ and $\frac{\partial G}{\partial n}=-\left.\frac{\partial G}{\partial y}\right|_{y=0}$.
 
-THEOREM 4 CONFORMAL MAPPING FORMULA FOR GREEN'S FUNCTION
 
 On the nonnegative $y$-axis, we have $d s=d y$ and $\frac{\partial G}{\partial n}=-\left.\frac{\partial G}{\partial x}\right|_{x=0}$. Using the explicit formula for $G$ from Example 4, we compute:
 
@@ -254,8 +326,8 @@
 
 $$
 \begin{aligned}
-\frac{\partial G}{\partial n} & =\frac{y_{0}}{\left(x-x_{0}\right)^{2}+y^{2}}-\frac{y_{0}}{\left(x+x_{0}\right)^{2}+y_{0}^{2}}+\frac{y_{0}}{\left(x-x_{0}\right)^{2}+y_{0}^{2}}-\frac{y_{0}}{\left(x+x_{0}\right)^{2}+y_{0}^{2}} \\
-& =\frac{2 y_{0}}{\left(x-x_{0}\right)^{2}+y^{2}}-\frac{2 y_{0}}{\left(x+x_{0}\right)^{2}+y_{0}^{2}} .
+\frac{\partial G}{\partial n} & =\frac{y_{0}}{\left(x-x_{0}\right)^{2}+y_0^2}-\frac{y_{0}}{\left(x+x_{0}\right)^{2}+y_{0}^{2}}+\frac{y_{0}}{\left(x-x_{0}\right)^{2}+y_{0}^{2}}-\frac{y_{0}}{\left(x+x_{0}\right)^{2}+y_{0}^{2}} \\
+& =\frac{2 y_{0}}{\left(x-x_{0}\right)^{2}+y_0^2}-\frac{2 y_{0}}{\left(x+x_{0}\right)^{2}+y_{0}^{2}} .
 \end{aligned}
 $$
 
@@ -269,32 +341,47 @@
 
 The steps that we took to go from (9) to (10) in Example 4 can be applied with any conformal mapping. This yields the following variation on Theorem 3, which may be more useful in computations.
 
-Suppose that $\Omega$ is a simply connected region with (nonempty) boundary $\Gamma$. Let $\phi$ be a one-to-one conformal mapping of $\Omega$ onto the upper half-plane. taking $\Gamma$ into the real line. Then Green's function for $\Omega$ is
-
-$$
-G\left(x, y, x_{0}, y_{0}\right)=\ln \left|\frac{\phi(z)-\phi\left(z_{0}\right)}{\phi(z)-\overline{\phi\left(z_{0}\right)}}\right|,
-$$
-
-where $z=x+i y$ and $z_{0}=x_{0}+i y_{0}$ are in $\Omega$.
+> [!theorem] Conformal Mapping Formula for Green's Function
+> Suppose that $\Omega$ is a simply connected region with (nonempty) boundary $\Gamma$. Let $\phi$ be a one-to-one conformal mapping of $\Omega$ onto the upper half-plane, taking $\Gamma$ into the real line. Then Green's function for $\Omega$ is
+>
+> $$
+> G\left(x, y, x_{0}, y_{0}\right)=\ln \left|\frac{\phi(z)-\phi\left(z_{0}\right)}{\phi(z)-\overline{\phi\left(z_{0}\right)}}\right|,
+> $$
+>
+> where $z=x+i y$ and $z_{0}=x_{0}+i y_{0}$ are in $\Omega$.
+>
+> Use $G(z,z_0)=\log|z-z_0|+$ a function harmonic at $z_0$, with zero boundary values. The formulas apply for $z\ne z_0$.
+
+*Printed equation label: (12).*
+
 Here is an interesting application.
-EXAMPLE 6 Green's function for a semi-infinite vertical strip
-Let $\Omega$ be the semi-infinite vertical strip $\left\{z=x+i y:-\frac{\pi}{2} \leq x \leq \frac{\pi}{2}, y \geq 0\right\}$. The function $\phi(z)=\sin z$ is a one-to-one conformal mapping of $\Omega$ onto the upper half-plane. (See Example 3, Section 16.6.) Thus by Theorem 4, Green's function for $\Omega$ is
+> [!exercise] EXAMPLE 6 Green's function for a semi-infinite vertical strip
+> Derive the positive-logarithmic Green function for $\Omega=\{x+iy:-\pi/2<x<\pi/2,\ y>0\}$ using the sine map.
+
+##### solution
+
+Let $\Omega$ be the semi-infinite vertical strip $\left\{z=x+i y:-\frac{\pi}{2}<x<\frac{\pi}{2},y>0\right\}$. The function $\phi(z)=\sin z$ is a one-to-one conformal mapping of $\Omega$ onto the upper half-plane. (See Example 3, Section 16.6.) Thus by Theorem 4, Green's function for $\Omega$ is
 
 $$
 G\left(z, z_{0}\right)=\ln \left|\frac{\sin z-\sin z_{0}}{\sin z-\overline{\sin z_{0}}}\right|=\ln \left|\sin z-\sin z_{0}\right|-\ln \left|\sin z-\overline{\sin z_{0}}\right|
-$$
-
-## THEOREM 5 COMPOSITION OF GREEN'S FUNCTIONS AND CONFORMAL MAPPINGS
+\tag{13}
+$$
+
 
 To express $G$ in terms of $x, y, x_{0}$, and $y_{0}$, you can use the formula for $\sin z$ in terms of these variables. We leave the details to the exercises.
 
 The following theorem describes yet another way to construct new Green's functions by composing known Green's functions with one-to-one conformal mappings. The proof of the theorem is very much like the proof of Theorem 1 and will be left to the exercises.
 
-Suppose that $\Omega$ and $\Omega^{\prime}$ are simply connected regions with (nonempty) boundaries $\Gamma$ and $\Gamma^{\prime}$, respectively. Suppose that $\phi$ is a one-to-one conformal mapping of $\Omega$ onto $\Omega^{\prime}$, such that $\phi[\Gamma]$ is contained in $\Gamma^{\prime}$. Let $g\left(x, y, x_{0}, y_{0}\right)=g\left(x+i y, x_{0}+i y_{0}\right)$ denote the Green's function for $\Omega^{\prime}$. Then Green's function for $\Omega$ is
-
-$$
-G\left(x, y, x_{0}, y_{0}\right)=g\left(\phi(x+i y), \phi\left(x_{0}+i y_{0}\right)\right)
-$$
+> [!theorem] Composition of Green's Functions and Conformal Mappings
+> Suppose that $\Omega$ and $\Omega^{\prime}$ are simply connected regions with (nonempty) boundaries $\Gamma$ and $\Gamma^{\prime}$, respectively. Suppose that $\phi$ is a one-to-one conformal mapping of $\Omega$ onto $\Omega^{\prime}$, such that $\phi[\Gamma]$ is contained in $\Gamma^{\prime}$. Let $g\left(x, y, x_{0}, y_{0}\right)=g\left(x+i y, x_{0}+i y_{0}\right)$ denote the Green's function for $\Omega^{\prime}$. Then Green's function for $\Omega$ is
+>
+> $$
+> G\left(x, y, x_{0}, y_{0}\right)=g\left(\phi(x+i y), \phi\left(x_{0}+i y_{0}\right)\right)
+> $$
+>
+> Use $G(z,z_0)=\log|z-z_0|+$ a function harmonic at $z_0$, with zero boundary values. The formulas apply for $z\ne z_0$.
+
+*Printed equation label: (14).*
 
 As an illustration, write Green's function for the upper half-plane in the form $g\left(x, y, x_{0}, y_{0}\right)=\ln \left|z-z_{0}\right|-\ln \left|z-\bar{z}_{0}\right|$ (Example 3). Let $\phi(z)$ denote a one-to-one conformal mapping of a region $\Omega$ onto the upper half-plane, taking $\Gamma$ into the real line. Then Green's function for $\Omega$ is
 
@@ -304,20 +391,19 @@
 
 which is the formula in Theorem 4.
 We close this section by completing the proof of Theorem 1. The proof requires some properties of analytic functions that are recalled where needed.
-Proof of Theorem 1. Suppose that $\Omega$ is a simply connected region with (nonempty) boundary $\Gamma . z=x+i y$ and $z_{0}=x_{0}+i y_{0}$ are in $\Omega$, and $\phi\left(z, z_{0}\right)$ is a one-to-one conformal mapping of $\Omega$ onto the unit disk. We want to show that Green's function for $\Omega$ is given by (2): $G\left(z, z_{0}\right)=\ln \left|\phi\left(z, z_{0}\right)\right|$. We have already proved that the function $\ln \left|\infty\left(z, z_{0}\right)\right|$ is harmonic on $\Omega$, except at $z=z_{0}$, and that it vanishes on the boundary of $\Omega$. To prove that it is the Green's function for $\Omega$, by (2), Section 16.3, we must show that, for $z \neq z_{0}$,
+Proof of Theorem 1. Suppose that $\Omega$ is a simply connected region with (nonempty) boundary $\Gamma . z=x+i y$ and $z_{0}=x_{0}+i y_{0}$ are in $\Omega$, and $\phi\left(z, z_{0}\right)$ is a one-to-one conformal mapping of $\Omega$ onto the unit disk. We want to show that Green's function for $\Omega$ is given by (2): $G\left(z, z_{0}\right)=\ln \left|\phi\left(z, z_{0}\right)\right|$. We have already proved that the function $\ln|\phi(z,z_0)|$ is harmonic on $\Omega$, except at $z=z_{0}$, and that it vanishes on the boundary of $\Omega$. To prove that it is the Green's function for $\Omega$, by (2), Section 16.3, we must show that, for $z \neq z_{0}$,
 
 $$
 \ln \left|\phi\left(z, z_{0}\right)\right|=\frac{1}{2} \ln \left(\left(x-x_{0}\right)^{2}+\left(y-y_{0}\right)^{2}\right)+h\left(z, z_{0}\right)=\ln \left|z-z_{0}\right|+h\left(z, z_{0}\right)
+\tag{15}
 $$
 
 where $h$ is harmonic for all $z$ in $\Omega$. We need the following fact about analytic functions. Suppose that $f(z)$ is analytic in a disk containing $z_{0}$, but not at $z_{0}$. Then $z_{0}$ is called an isolated singularity. It is a fact that if $z_{0}$ is an isolated singularity and $\lim _{z \rightarrow z_{0}} f(z)=A$ exists, then $z_{0}$ is a removable singularity. That is, if we define $f\left(z_{0}\right)=A$, then $f$ becomes analytic at $z_{0}$ (see [1], Section 4.6). With this property in mind. consider the function $f(z)=\frac{\phi\left(z, z_{0}\right)}{z-z_{0}}\left(z \neq z_{0}\right.$ in $\left.\Omega\right)$, where, as in Theorem 1. $\phi\left(z, z_{0}\right)$ is analytic on $\Omega$ and $\phi\left(z_{0}, z_{0}\right)=0$. It is clear that $f$ is analytic on $\Omega$ except at $z_{0}$. Thus $z_{0}$ is an isolated singularity of $f$. Also,
 
 $$
-\lim _{z \rightarrow 0} f(z)=\lim _{z \rightarrow z_{0}} \frac{\phi\left(z, z_{0}\right)}{z-z_{0}}=\lim _{z \rightarrow z_{0}} \frac{\phi\left(z, z_{0}\right)-\overbrace{\phi\left(z_{0}, z_{0}\right)}^{=0}}{z-z_{0}}=\left.\frac{d}{d z} \phi\left(z, z_{0}\right)\right|_{z=z_{0}},
-$$
-
-![](./images/7ce1063d-f13d-4631-8956-8a97e0eaf48a-73_325_462_1384_52.jpg)
-Figure 4 A general Dirichlet problem on a horizontal strip (Exercises 9 and 10).
+\lim_{z\to z_0}f(z)=\lim _{z \rightarrow z_{0}} \frac{\phi\left(z, z_{0}\right)}{z-z_{0}}=\lim _{z \rightarrow z_{0}} \frac{\phi\left(z, z_{0}\right)-\overbrace{\phi\left(z_{0}, z_{0}\right)}^{=0}}{z-z_{0}}=\left.\frac{d}{d z} \phi\left(z, z_{0}\right)\right|_{z=z_{0}},
+$$
+
 
 by definition of the derivative. Hence $z_{0}$ is a removable singularity of $f(z)$. Define
 
@@ -325,32 +411,93 @@
 f(z)= \begin{cases}\frac{\phi\left(z, z_{0}\right)}{z-z_{0}} & \text { if } z \neq z_{0} \\ \left.\phi^{\prime}\left(z, z_{0}\right)\right|_{z=z_{0}} & \text { if } z=z_{0}\end{cases}
 $$
 
-Then $f$ is analytic on $\Omega$. Also, $f(z) \neq 0$ for all $z$ in $\Omega$. This last assertion is clear for $z \neq z_{0}$, since $\phi$ is onc-to-one and $\phi\left(z_{0}, z_{0}\right)=0$. For $z=z_{0}$, we use the fact that $\phi$ is one-to-one to infer that $\phi^{\prime}\left(z, z_{0}\right) \neq 0$ for all $z$ in $\Omega$; in particular, $\left.\phi^{\prime}\left(z, z_{0}\right)\right|_{z=z_{0}} \neq 0$. Now, set $h\left(z, z_{0}\right)=\ln |f(z)|$. Then $h$ is harmonic on $\Omega$, by Theorem 1, Section 16.6, because it is the composition of the analytic function $f$ and the harmonic function $\ln |z|(z \neq 0)$. For $z \neq z_{0}$, using the definition of $f(z)$, we see that
-
-$$
-\begin{aligned}
-\ln \left|z-z_{0}\right|+h\left(z, z_{0}\right) & =\ln \left|z-z_{0}\right|+\ln |f(z)| \\
-& \left.=\ln \left|z-z_{0}\right|+\ln \left|\phi\left(z, z_{0}\right)\right|-\ln \mid z-z_{0}\right)|=\ln | \phi\left(z, z_{0}\right) \mid .
+Then $f$ is analytic on $\Omega$. Also, $f(z) \neq 0$ for all $z$ in $\Omega$. This last assertion is clear for $z \neq z_{0}$, since $\phi$ is one-to-one and $\phi\left(z_{0}, z_{0}\right)=0$. For $z=z_{0}$, we use the fact that $\phi$ is one-to-one to infer that $\phi^{\prime}\left(z, z_{0}\right) \neq 0$ for all $z$ in $\Omega$; in particular, $\left.\phi^{\prime}\left(z, z_{0}\right)\right|_{z=z_{0}} \neq 0$. Now, set $h\left(z, z_{0}\right)=\ln |f(z)|$. Then $h$ is harmonic on $\Omega$, by Theorem 1, Section 16.6, because it is the composition of the analytic function $f$ and the harmonic function $\ln |z|(z \neq 0)$. For $z \neq z_{0}$, using the definition of $f(z)$, we see that
+
+$$
+\begin{aligned}
+\log|z-z_0|+h(z,z_0)
+&=\log|z-z_0|+\log|f(z)|\\
+&=\log|z-z_0|+\log|\phi(z,z_0)|-\log|z-z_0|\\
+&=\log|\phi(z,z_0)|.
 \end{aligned}
 $$
 
 Thus (15) holds.
 
-## Exercises 12.7
-
-In Exercises 1-8, find Green's function for the region $\Omega$.
-
-1. $\Omega$ is the open disk of radius 1 and center at $(1,0)$.
-2. $\Omega$ is the open disk of radius 2 and center at $(4,4)$.
-3. $\Omega$ is the half-plane above the line $y=x$.
-4. $\Omega$ is the half-plane to the right of the line $x=1$.
-5. $\Omega$ is the infinite horizontal strip bounded by the lines $y=0$ and $y=\pi$.
-6. $\Omega$ is the infinite horizontal strip bounded by the lines $y=0$ and $y=\frac{\pi}{2}$.
-7. $\Omega$ is the infinite sector bounded by the rays through the origin at angles 0 and $\frac{\pi}{4}$.
-8. $\Omega$ is the infinite sector bounded by the rays through the origin at angles 0 and $\frac{3 \pi}{4}$.
-9. Derive a Poisson integral formula that solves the Dirichlet problem on the horizontal strip in Figure 4 for the case when $f(x)=0$ and $g(x)$ is arbitrary.
-10. Derive a Poisson integral formula that solves the Dirichlet problem on the horizontal strip in Figure 4 when both $f(x)$ and $g(x)$ are arbitrary
-11. Solve the Dirichlet problem in the first quadrant in Figure 3, given that $f(x)=x$ if $0<x<1$ and 0 otherwise, and $g(y)=0$ for all $y>0$.
-12. Derive a Poisson integral formula for the semi-infinite strip in Example 6.
-13. Show that the formula that we found in Example 1 for Green's function for a disk is identical with the formula that we have in Section 16.4.
-14. Study the proof of Theorem 1 and then prove Theorem 5.
+## Exercises 16.7
+
+
+> [!prompt] Shared exercise instructions
+> Use the positive-logarithmic normalization throughout. For the Dirichlet problems on unbounded regions, assume bounded continuous boundary data on the open boundary pieces and seek bounded harmonic solutions.
+
+
+> [!prompt] Shared exercise instructions
+> In Exercises 1–8, find Green's function for the region $\Omega$.
+
+
+> [!exercise] Exercise 1
+> $\Omega$ is the open disk of radius 1 and center at $(1,0)$.
+
+
+> [!exercise] Exercise 2
+> $\Omega$ is the open disk of radius 2 and center at $(4,4)$.
+
+
+> [!exercise] Exercise 3
+> $\Omega$ is the half-plane above the line $y=x$.
+
+
+> [!exercise] Exercise 4
+> $\Omega$ is the half-plane to the right of the line $x=1$.
+
+
+> [!exercise] Exercise 5
+> $\Omega$ is the infinite horizontal strip bounded by the lines $y=0$ and $y=\pi$.
+
+
+> [!exercise] Exercise 6
+> $\Omega$ is the infinite horizontal strip bounded by the lines $y=0$ and $y=\frac{\pi}{2}$.
+
+
+> [!exercise] Exercise 7
+> $\Omega$ is the infinite sector bounded by the rays through the origin at angles 0 and $\frac{\pi}{4}$.
+
+
+> [!exercise] Exercise 8
+> $\Omega$ is the infinite sector bounded by the rays through the origin at angles 0 and $\frac{3 \pi}{4}$.
+
+
+```scientific-figure
+id: 066395fe-ad42-4ce5-9261-9dca67520e80
+numbered: false
+title: ""
+caption: Figure 4 A general Dirichlet problem on a horizontal strip (Exercises 9 and 10).
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 16 Green's Functions and Conformal Mappings/images/7ce1063d-f13d-4631-8956-8a97e0eaf48a-73_325_462_1384_52.jpg
+    caption: ""
+```
+> [!exercise] Exercise 9
+> Derive a Poisson integral formula that solves the Dirichlet problem on the horizontal strip in Figure 4 for the case when $f(x)=0$ and $g(x)$ is arbitrary.
+
+
+> [!exercise] Exercise 10
+> Derive a Poisson integral formula that solves the Dirichlet problem on the horizontal strip in Figure 4 when both $f(x)$ and $g(x)$ are arbitrary
+
+
+> [!exercise] Exercise 11
+> Solve the Dirichlet problem in the first quadrant in Figure 3, given that $f(x)=x$ if $0<x<1$ and 0 otherwise, and $g(y)=0$ for all $y>0$.
+
+
+> [!exercise] Exercise 12
+> Derive a Poisson integral formula for the semi-infinite strip in Example 6.
+
+
+> [!exercise] Exercise 13
+> Show that the formula that we found in Example 1 for Green's function for a disk is identical with the formula that we have in Section 16.4.
+
+
+> [!exercise] Exercise 14
+> Study the proof of Theorem 1 and then prove Theorem 5.

`````

## Additional source comparison

## 1. Restore author construction and wording in Example 4; correct the inconsistent conformal-map symbol and OCR denominator, retaining the printed equation labels.

### Before

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
````
### After

````text
Let us start by constructing a one-to-one conformal mapping of the first quadrant onto the unit disk by mapping the first quadrant onto the upper half-plane and then using the mapping in Example 2(b). Put $\phi(z)=z^2$. Thus $\frac{i-\phi(z)}{i+\phi(z)}$ is a one-to-one conformal mapping of the first quadrant onto the unit disk. For $z$ and $z_{0}$ in the first quadrant, use Theorem 3 to get the Green's function for the first quadrant in the form

$$
G\left(z, z_{0}\right)=\ln \left|\frac{\frac{i-\phi(z)}{i+\phi(z)}-\frac{i-\phi\left(z_{0}\right)}{i+\phi\left(z_{0}\right)}}{1-\overline{\left(\frac{i-\phi\left(z_{0}\right)}{i+\phi\left(z_{0}\right)}\right)} \frac{i-\phi(z)}{i+\phi(z)}}\right| .
\tag{9}
$$

This is the same expression as what we had in the previous example, except that $z$ and $z_{0}$ are now replaced by $\phi(z)$ and $\phi(z_0)$. Using the result of the previous example, we find:

$$
G\left(z, z_{0}\right)=\ln \left|\frac{\phi(z)-\phi\left(z_{0}\right)}{\phi(z)-\overline{\phi\left(z_{0}\right)}}\right|=\ln \left|\frac{z^{2}-z_{0}^{2}}{z^{2}-{\overline{z_{0}}}^{2}}\right| .
\tag{10}
$$
````
