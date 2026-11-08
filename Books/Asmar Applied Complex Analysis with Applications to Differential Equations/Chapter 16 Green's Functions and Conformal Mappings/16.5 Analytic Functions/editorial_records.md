
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

## Additional source comparison

## 1. Restore the author’s orthogonal-trajectory derivation; retain only regular-point qualifications and the corrected derivative symbol.

### Before

````text
Suppose that a second family of regular level curves is given by $\psi(x,y)=C'$. Where the relevant denominators are nonzero, its slope is $m_2=-\psi_x/\psi_y$, so

$$
m_1m_2=-1\quad\Longleftrightarrow\quad
\frac{u_x}{u_y}\frac{\psi_x}{\psi_y}=-1
\quad\Longleftrightarrow\quad\frac{u_x}{u_y}=-\frac{\psi_y}{\psi_x}.
\tag{12}
$$

The division-free condition is $\nabla u\cdot\nabla\psi=0$, with both gradients nonzero to ensure regular level curves. For a harmonic conjugate $v$, the Cauchy–Riemann equations give $\nabla u\cdot\nabla v=u_xv_x+u_yv_y=0$.
````
### After

````text
Suppose that we have expressed the orthogonal trajectories in the form $\psi(x, y)=C^{\prime}$ for some function $\psi$. At regular points where the displayed denominators are nonzero, the slope of the tangent line at any point of the orthogonal curves is given by $m_{2}=\frac{d y}{d x}=-\frac{\psi_x}{\psi_y}$. Since the slopes of orthogonal curves are negative reciprocals, we have

$$
m_{1} \cdot m_{2}=-1 \Leftrightarrow \frac{u_{x}}{u_{y}} \cdot \frac{\psi_{x}}{\psi_{y}}=-1
$$

equivalently, the condition for two families to be mutually orthogonal is

$$
\frac{u_{x}}{u_{y}}=-\frac{\psi_{y}}{\psi_{x}}
$$


Now suppose that $u$ is a harmonic function with harmonic conjugate $v$, and let us consider the level curves $u(x, y)=C$ and $v(x, y)=C^{\prime}$. Since $u+i v$ is analytic, the Cauchy Riemann equations hold: $u_{x}=v_{y}$ and $u_{y}=-v_{x}$. At points where the complex derivative is nonzero, it follows that $u(x, y)=C$ and $v(x, y)=C^{\prime}$ are orthogonal families of curves. We thus have the following useful result.
````

## 2. Restore source wording; retain only the actual correction.

### Before

````text
> [!theorem|504a572f-b3e7-5934-a665-bc458cbe57bb.local at=cae4b1cb-c767-50df-aeee-fa994f060043] Orthogonal Trajectories
> Let $u+iv$ be analytic on an open subset of $\mathbb C$. At every point where its complex derivative is nonzero, the level curves of $u$ and $v$ through that point are regular and meet at right angles. Equivalently, $\nabla u\cdot\nabla v=0$ and $|\nabla u|=|\nabla v|>0$ there. Critical points require separate treatment.
````
### After

````text
> [!theorem|504a572f-b3e7-5934-a665-bc458cbe57bb.local at=cae4b1cb-c767-50df-aeee-fa994f060043] Orthogonal Trajectories
> If $u$ is harmonic and $v$ is a harmonic conjugate of $u$, then the level curves $u(x,y)=C$ and $v(x,y)=C^{\prime}$ are mutually orthogonal at points where $(u+iv)^{\prime}\ne0$.
````

## Source-to-current comparison

Source: /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 16 Green's Functions and Conformal Mappings/16.5 Analytic Functions.md

This exact comparison preserves the full change evidence, including formatting, OCR corrections, restored source wording, and required standalone context. The entries above explain the recovery edits. The comparison is not a claim that every difference is a correction; component serialization, callout wrapping, and printed labels outside callouts are formatting.

`````diff
--- /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 16 Green's Functions and Conformal Mappings/16.5 Analytic Functions.md
+++ /Users/gradyclopton/ObsidianVaults/complex_analysis/Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 16 Green's Functions and Conformal Mappings/16.5 Analytic Functions.md
@@ -1,9 +1,21 @@
+
 ### 16.5 Analytic Functions
 
 In the remaining sections of this chapter we explore a connection between complex-valued functions and the solution of partial differential equations.
 
-![](./images/7ce1063d-f13d-4631-8956-8a97e0eaf48a-35_426_391_1313_38.jpg)
-Figure 1 Identifying a complex number $z$ with a point in the Cartesian plane; the complex conjugate $Z$; the norm $|z|$ of $z$.
+```scientific-figure
+id: afbe0a5d-5847-499f-af2a-3781fbf44cb8
+numbered: false
+title: ""
+caption: Figure 1 Identifying a complex number $z$ with a point in the Cartesian plane; the complex conjugate $\bar z$; the norm $|z|$ of $z$.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 16 Green's Functions and Conformal Mappings/images/7ce1063d-f13d-4631-8956-8a97e0eaf48a-35_426_391_1313_38.jpg
+    caption: ""
+```
+
 
 If $z=x+i y$, where $x$ and $y$ are real numbers, we call $x$ the real part of $z$ and $y$ its imaginary part, and set $x=\operatorname{Re} z$ and $y=\operatorname{Im} z$. We denote the set of all complex numbers by $\mathbb{C}$. We identify a complex number $z=x+i y$ with a point ( $x, y$ ) in the Cartesian plane (referred to as the complex plane), much like a real number is identified with a point on the real number line (Figure 1). We introduce the notion of distance between two complex numbers, using the distance formula from the Cartesian plane: If $z_{1}=x_{1}+i y_{1}$ and $z_{2}=x_{2}+i y_{2}$, then the distance between $z_{1}$ and $z_{2}$ is
 
@@ -17,15 +29,38 @@
 z \cdot \bar{z}=x^{2}+y^{2}
 $$
 
-![](./images/7ce1063d-f13d-4631-8956-8a97e0eaf48a-36_340_352_172_65.jpg)
-Figure 2 Distance between two complex numbers $z_{1}$ and $z_{2}$.
-
-![](./images/7ce1063d-f13d-4631-8956-8a97e0eaf48a-36_410_454_754_63.jpg)
-Figure 3 Polar representation $z=|z| e^{i \theta}, \theta$ is the argument of $z$.
+```scientific-figure
+id: abbd395a-c62c-4836-b21d-832c540f3d03
+numbered: false
+title: ""
+caption: Figure 2 Distance between two complex numbers $z_{1}$ and $z_{2}$.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 16 Green's Functions and Conformal Mappings/images/7ce1063d-f13d-4631-8956-8a97e0eaf48a-36_340_352_172_65.jpg
+    caption: ""
+```
+
+
 
 Thus $z \cdot \bar{z}$ is always a nonnegative real number and $z \cdot \bar{z}=0 \Leftrightarrow z=0$. In terms of the complex conjugate, we have $|z|=\sqrt{z \bar{z}}$.
 
-Using polar coordinates, we write a nonzero complex number in polar form, $z=r(\cos \theta+i \sin \theta)$, where $r=|z|=\sqrt{x^{2}+y^{2}}$ and $\theta$ is the polar angle in Figure 3. With the help of Euler's identity, $e^{i \theta}=\cos \theta+i \sin \theta$, we can also write $z=r e^{i \theta}$. The angle $\theta$ is called the argument of $z$ and is denoted $\arg z$. It is clear that $\arg z$ is not single-valued: If $\alpha$ is one value of the argument, then any value of the form $\alpha+2 k \pi$, where $k$ is an integer, is also the argument of $z$. The unique value of $\arg z$ in the interval $(-\pi, \pi]$ is called the principal value of the argument and is clenoted by $\operatorname{Arg} z$.
+```scientific-figure
+id: dcfcfb6f-e07a-4934-aaf1-67a7f9422579
+numbered: false
+title: ""
+caption: Figure 3 Polar representation $z=|z| e^{i \theta}, \theta$ is the argument of $z$.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 16 Green's Functions and Conformal Mappings/images/7ce1063d-f13d-4631-8956-8a97e0eaf48a-36_410_454_754_63.jpg
+    caption: ""
+```
+
+
+Using polar coordinates, we write a nonzero complex number in polar form, $z=r(\cos \theta+i \sin \theta)$, where $r=|z|=\sqrt{x^{2}+y^{2}}$ and $\theta$ is the polar angle in Figure 3. With the help of Euler's identity, $e^{i \theta}=\cos \theta+i \sin \theta$, we can also write $z=r e^{i \theta}$. The angle $\theta$ is called the argument of $z$ and is denoted $\arg z$. It is clear that $\arg z$ is not single-valued: If $\alpha$ is one value of the argument, then any value of the form $\alpha+2 k \pi$, where $k$ is an integer, is also the argument of $z$. The unique value of $\arg z$ in the interval $(-\pi, \pi]$ is called the principal value of the argument and is denoted by $\operatorname{Arg} z$.
 
 The polar representation can be used to describe geometrically the effect of multiplication. Given two complex numbers $z_{1}=r_{1} e^{i \theta_{1}}$ and $z_{2}=r_{2} e^{i \theta_{2}}$, we have
 
@@ -39,12 +74,26 @@
 
 A complex-valued function of a complex variable, or simply a complex function, is a mapping $w=f(z)$ whose domain is a subset of the complex $z$-plane and whose range is a subset of the complex $w$-plane. By taking real and imaginary parts. we can visualize such a function as a mapping from a subset of the Cartesian $x y$-plane into the Cartesian $u v$-plane. We have the relations, $f(z)=u(z)+i v(z)$ or $f(z)=u(x, y)+i v(x, y)$, where $u(x, y)=\operatorname{Re}(f(z))$ and $v(x, y)=\operatorname{Im}(f(z))$ (Figure 4).
 
-![](./images/7ce1063d-f13d-4631-8956-8a97e0eaf48a-36_439_1117_1445_641.jpg)
+```scientific-figure
+id: 93feaba6-cbb4-4413-afb7-1b5966b24a35
+numbered: false
+title: ""
+caption: Figure 4 A complex function as a map from the $xy$-plane to the $uv$-plane.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 16 Green's Functions and Conformal Mappings/images/7ce1063d-f13d-4631-8956-8a97e0eaf48a-36_439_1117_1445_641.jpg
+    caption: ""
+```
+
 The following examples illustrate these concepts.
 
-## EXAMPLE 1 Functions of a complex variable
-
-In each of the following examples, we express the function in the form $f(z)= u(x, y)+i v(x, y)$, where $z=x+i y$.
+> [!exercise|2eebbce3-dcf8-505e-8a13-8813376b2f8d.local at=873305b8-0cf1-5310-9a84-086628afac43] EXAMPLE 1 Functions of a complex variable
+> For $z=x+iy$, express each function as $u(x,y)+iv(x,y)$: (a) $\operatorname{Im}z$; (b) $\alpha z+\beta$, with $\alpha=a+ib$, $\beta=c+id$; (c) $e^z$; (d) $\sin z$; (e) $\cos z$; (f) the principal value $\log z$ for $z\ne0$. Use $\sin z=(e^{iz}-e^{-iz})/(2i)$, $\cos z=(e^{iz}+e^{-iz})/2$, and $\log z=\ln|z|+i\operatorname{Arg}z$.
+
+##### solution
+
 (a) The function $f(z)=\operatorname{Im} z$ is real-valued. We have $u(x, y)=y$ and $v(x, y)=0$.
 (b) A linear function is of the form $f(z)=\alpha z+\beta$, where $\alpha$ and $\beta$ are complex numbers. Write $\alpha=a+i b$ and $\beta=c+i d$ where $a, b, c$, and $d$ are real. Then
 
@@ -71,7 +120,7 @@
 $$
 \begin{aligned}
 \sin z & =\frac{e^{i(x+i y)}-e^{-i(x+i y)}}{2 i}=\frac{e^{i x} e^{-y}-e^{-i x} e^{y}}{2 i} \\
-& =\sin x \frac{e^{y}+e^{-y}}{2}+i \cos x \frac{e^{y}+e^{-y}}{2} \\
+& =\sin x \frac{e^{y}+e^{-y}}{2}+i\cos x\frac{e^y-e^{-y}}2 \\
 & =\sin x \cosh y+i \cos x \sinh y
 \end{aligned}
 $$
@@ -88,62 +137,102 @@
 \cos z=\cos x \cosh y-i \sin x \sinh y
 $$
 
-(f) The complex logarithm is trickier to define. There are many "branches" of the logarithm. The principal branch of the logarithm is defined for all $z \neq 0$ by
+(f) The complex logarithm is trickier to define. There are many "branches" of the logarithm. The principal value of the logarithm is defined for all $z\ne0$ by
 
 $$
 \log z=\ln |z|+i \operatorname{Arg} z
 $$
 
-where $\operatorname{Arg} z$ is the principal value of the argument. Taking real and imaginary parts of the function $\log z$, we find $u(x, y)=\ln |z|=\frac{1}{2} \ln \left(x^{2}+y^{2}\right)$ and $v(x, y)= \tan ^{-1}\left(\frac{y}{x}\right)$, where the value of the inverse tangent must be chosen in the interval ( $-\pi, \pi]$ (see (8)-(10) for explicit formulas for Arg $z$ in terms of $x$ and $y$ ). For any complex number $z \neq 0$, we have
+where $\operatorname{Arg}z\in(-\pi,\pi]$. Its restriction to $\mathbb C\setminus(-\infty,0]$ is the analytic principal branch. Taking real and imaginary parts of the function $\log z$, we find $u(x, y)=\ln |z|=\frac{1}{2} \ln \left(x^{2}+y^{2}\right)$ and $v(x,y)=\operatorname{Arg}(x+iy)$, with the quadrant chosen correctly; the ordinary inverse tangent $\arctan(y/x)$ alone is insufficient (see (8)-(10) for explicit formulas for Arg $z$ in terms of $x$ and $y$ ). For any complex number $z \neq 0$, we have
 
 $$
 e^{\log z}=e^{\ln |z|+i \operatorname{Arg} z}=e^{\ln |z|} e^{i \operatorname{Arg} z}=|z| e^{i \operatorname{Arg} z}=z
 $$
 
-where we have used the fact that $\ln x$ and $e^{r}$ are inverse functions (hence $e^{\ln |z|}= |z|$ ), and we have used the polar representation $z=|z| e^{i \operatorname{Arg} z}$. As a result, we see that $e^{\log z}=z$, which is analogous to the inverse function relationship between $e^{x}$ and $\operatorname{In} x$. Notice however that the identity $\log \left(e^{z}\right)=z$ does not always hold (Exercise 22).
-
-![](./images/7ce1063d-f13d-4631-8956-8a97e0eaf48a-38_435_466_218_65.jpg)
-Figure $5 \operatorname{Arg} z$ is not continuous when $z_{0}=x_{0} \leq 0$. Limit of $\operatorname{Arg} z$ along the curve $C$ is $\pi$, but the limit along the curve $C^{\prime}$ is $-\pi$
-
-![](./images/7ce1063d-f13d-4631-8956-8a97e0eaf48a-38_438_462_1026_67.jpg)
-Figure 6 Branch cut of $\log 2$, where the function fails to be continuous.
-
-A complex function $f(z)=u(x, y)+i v(x, y)$ is continuous if and only if both $u$ and $v$ are continuous. You can verify that the functions in Example 1(a)-(e) are continuous for all $z=x+i y$. The logarithmic function $\log z$ is not defined at $z=0$ and is not continuous at all $z$ on the negative real axis. To see this, let $z_{0}=x_{0}$ with $x_{0}<0$. By definition of the principal value, we have $\operatorname{Arg} z_{0}=\pi$. If $z$ approaches the point $z_{0}$ from the lower half-plane, then $\operatorname{Arg} z$ tends to $-\pi$ which is not equal to $\operatorname{Arg} z_{0}$. Thus $\lim _{z \rightarrow z_{0}} \operatorname{Arg} z \neq \operatorname{Arg} z_{0}$ and so $\operatorname{Arg} z$ is not continuous at the point $z_{0}$ (Figure 5). It follows that $\log z$ is not continuous at $\varepsilon_{0}$. The set of points $z=x$, where $x \leq 0$ is called a branch cut for $\log z$ (Figure 6). We just proved that $\log z$ is not continuous at all the points on its branch cut. At all other points in the plane, $\log z$ is continuous.
+where we have used the fact that $\ln x$ and $e^x$ are inverse functions (hence $e^{\ln |z|}= |z|$ ), and we have used the polar representation $z=|z| e^{i \operatorname{Arg} z}$. As a result, we see that $e^{\log z}=z$, which is analogous to the inverse function relationship between $e^{x}$ and $\ln x$. Notice however that the identity $\log \left(e^{z}\right)=z$ does not always hold (Exercise 22).
+
+```scientific-figure
+id: 2ec9b0d8-c3a7-4f2a-951b-66cdbcc7277c
+numbered: false
+title: ""
+caption: Figure 5 $\operatorname{Arg}z$ is not continuous when $z_0=x_0<0$. Limit of $\operatorname{Arg} z$ along the curve $C$ is $\pi$, but the limit along the curve $C^{\prime}$ is $-\pi$
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 16 Green's Functions and Conformal Mappings/images/7ce1063d-f13d-4631-8956-8a97e0eaf48a-38_435_466_218_65.jpg
+    caption: ""
+```
+
+
+```scientific-figure
+id: 397ba9ff-ec5d-4cbb-bb4c-87c49dbbc86d
+numbered: false
+title: ""
+caption: Figure 6 Branch cut of $\log z$, where the function fails to be continuous.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 16 Green's Functions and Conformal Mappings/images/7ce1063d-f13d-4631-8956-8a97e0eaf48a-38_438_462_1026_67.jpg
+    caption: ""
+```
+
+
+A complex function $f(z)=u(x, y)+i v(x, y)$ is continuous if and only if both $u$ and $v$ are continuous. You can verify that the functions in Example 1(a)-(e) are continuous for all $z=x+i y$. The logarithmic function $\log z$ is not defined at $z=0$ and is not continuous at all $z$ on the negative real axis. To see this, let $z_{0}=x_{0}$ with $x_{0}<0$. By definition of the principal value, we have $\operatorname{Arg} z_{0}=\pi$. If $z$ approaches the point $z_{0}$ from the lower half-plane, then $\operatorname{Arg} z$ tends to $-\pi$ which is not equal to $\operatorname{Arg} z_{0}$. Thus $\lim _{z \rightarrow z_{0}} \operatorname{Arg} z \neq \operatorname{Arg} z_{0}$ and so $\operatorname{Arg} z$ is not continuous at the point $z_{0}$ (Figure 5). It follows that $\log z$ is not continuous at $z_0$. The set of points $z=x$, where $x \leq 0$ is called a branch cut for $\log z$ (Figure 6). It is discontinuous at each negative real point and undefined at the origin. At all other points in the plane, $\log z$ is continuous.
 
 ## Analytic Functions, the Cauchy-Riemann Equations
 
-We say that $f(z)$ is differentiable at $z$ if its derivative $f^{\prime}(z)$, or $\frac{d}{d z} f(z)$, exists and is finite at $z$, where
-
-$$
-f^{\prime}(z)=\lim _{\zeta \rightarrow z} \frac{f(\zeta)-f(z)}{\zeta-z}
-$$
-
-If $S$ is an open set in the complex plane we say that $f$ is analytic on $S$ if $f$ is differentiable at all points $z$ in $S$. A function is analytic at one point $z_{0}$ if it is analytic on an open set that contains $z_{0}$. Definition (1) resembles the familiar definition of the derivative of a function of a real variable from calculus. So you should not hesitate to try techniques from calculus in computing the limit in (1), especially if $f$ is a polynomial or a rational function. For example, if $f(z)=z$, then
+> [!definition|7a3918ec-b8ce-5fb6-afb3-3fa188f9f22a.local at=a45fda6d-881f-5946-8622-f57e69eefd7e] Complex Differentiability and Analyticity
+> Let $f$ be defined on an open subset of $\mathbb C$. We say that $f(z)$ is differentiable at $z$ if its derivative $f^{\prime}(z)$, or $\frac{d}{d z} f(z)$, exists and is finite at $z$, where
+>
+> $$
+> f^{\prime}(z)=\lim _{\zeta \rightarrow z} \frac{f(\zeta)-f(z)}{\zeta-z}
+> $$
+>
+> If $S$ is an open set in the complex plane we say that $f$ is analytic on $S$ if $f$ is differentiable at all points $z$ in $S$. A function is analytic at one point $z_{0}$ if it is analytic on an open set that contains $z_{0}$.
+
+*Printed equation label: (1).*
+
+Definition (1) resembles the familiar definition of the derivative of a function of a real variable from calculus. So you should not hesitate to try techniques from calculus in computing the limit in (1), especially if $f$ is a polynomial or a rational function. For example, if $f(z)=z$, then
 
 $$
 f^{\prime}(z)=\lim _{\zeta \rightarrow z} \frac{f(\zeta)-f(z)}{\zeta-z}=\lim _{\zeta \rightarrow z} \frac{\zeta-z}{\zeta-z}=1
 $$
 
-as expected. However, keep in mind that unlike a real variable which can vary in only two directions, the complex variable $\zeta$ in (1) can approach $z$ in infinitely many ways, and to say that (1) exists we mean that it exists and is the same no matter how we approach $z$. This is clearly a stronger requirement than the existence of the derivative in the real variable case. For this reason analytic functions have distinctive properties that are not shared by differentiable functions of a real variable. One of these striking propertios is expressed by the following result.
-
-THEOREM 1 CAUCHY-RIEMANN EQUATIONS
-
-![](./images/7ce1063d-f13d-4631-8956-8a97e0eaf48a-39_429_452_1359_36.jpg)
-Figure 7 Evaluating the limit (1), as $\zeta$ approaches $z$ in two different (special) ways.
-
-The function $f(z)=u(x, y)+i v(x, y)$ is analytic in an open set $S$ if and only if the partial derivatives of $u$ and $v$ are continuous and satisfy the Cauchy-Riemann equations
-
-$$
-u_{x}=v_{y} \quad \text { and } \quad u_{y}=-v_{x} .
-$$
-
-Furthermore, if $f$ is analytic, then the derivative $f^{\prime}(z)$ is given as either of
-
-$$
-f^{\prime}(z)=u_{x}(x, y)+i v_{x}(x, y) \text { or } f^{\prime}(z)=v_{y}(x, y)-i u_{y}(x, y) .
-$$
+as expected. However, keep in mind that unlike a real variable which can vary in only two directions, the complex variable $\zeta$ in (1) can approach $z$ in infinitely many ways, and to say that (1) exists we mean that it exists and is the same no matter how we approach $z$. This is clearly a stronger requirement than the existence of the derivative in the real variable case. For this reason analytic functions have distinctive properties that are not shared by differentiable functions of a real variable. One of these striking properties is expressed by the following result.
+
+
+> [!theorem|144da62d-4427-57b4-ac3a-8afa8fc7b053.local at=0803b93e-4117-5d9d-9123-298a06c10d2d] Cauchy-Riemann Equations
+> The function $f(z)=u(x, y)+i v(x, y)$ is analytic in an open set $S$ if and only if the partial derivatives of $u$ and $v$ are continuous and satisfy the Cauchy-Riemann equations
+>
+> $$
+> u_{x}=v_{y} \quad \text { and } \quad u_{y}=-v_{x} .
+> $$
+>
+> Furthermore, if $f$ is analytic, then the derivative $f^{\prime}(z)$ is given as either of
+>
+> $$
+> f^{\prime}(z)=u_{x}(x, y)+i v_{x}(x, y) \text { or } f^{\prime}(z)=v_{y}(x, y)-i u_{y}(x, y) .
+> $$
+
+*Printed equation labels: (2) Cauchy–Riemann equations; (3) complex derivative formulas.*
 
 Thus the real and imaginary parts of an analytic function cannot be arbitrary of each other: They depend on each other in a precise manner described by the Cauchy-Riemann equations.
+```scientific-figure
+id: 98174ba5-6bc2-4c24-a7dc-b422da55c673
+numbered: false
+title: ""
+caption: Figure 7 Evaluating the limit (1), as $\zeta$ approaches $z$ in two different (special) ways.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 16 Green's Functions and Conformal Mappings/images/7ce1063d-f13d-4631-8956-8a97e0eaf48a-39_429_452_1359_36.jpg
+    caption: ""
+```
+
+
 Proof Here we shall prove only one direction in the theorem. (For the full proof see [1], Chapter 2.) Suppose that $f$ is analytic at $z=x+i y$ so that the limit (1) exists. To prove that the Cauchy Riemann equations and (3) hold, we compute the limit (1) in two different ways: once by taking $\zeta=z+\Delta x$ and once by taking $\zeta=z+i \Delta y$, where $\Delta x$ and $\Delta y$ are small increments in $x$ and $y$ (Figure 7). If $\zeta=z+\Delta x=x+\Delta x+i y, \zeta-z=\Delta x$, and (1) becomes
 
 $$
@@ -168,12 +257,14 @@
 
 The following examples illustrate how Theorem 1 can be used to establish analyticity and compute derivatives.
 
-## EXAMPLE 2 Applying the Cauchy-Riemann equations
-
-Refer to the functions in Example 1.
+> [!exercise|fcdf4cdc-ac40-55a2-afe7-56d5a3d9c715.local at=efb99aef-95d2-5e11-bdea-ceb8947e0bd6] EXAMPLE 2 Applying the Cauchy-Riemann equations
+> Use the Cauchy–Riemann equations to determine where (a) $\operatorname{Im}z$, (b) $\alpha z+\beta$, (c) $e^z$, (d) $\sin z$, (e) $\cos z$, and (f) the principal logarithm are analytic. Compute their complex derivatives wherever they are analytic.
+
+##### solution
+
 (a) The function $f(z)=\operatorname{Im} z=y$ has real part $u(x, y)=y$ and imaginary part $v(x, y)=0$. Computing partial derivatives, we find $u_{x}=0, u_{y}=1, v_{x}=v_{y}=0$. Thus the equality $u_{y}=-v_{x}$ holds nowhere, and so the Cauchy-Riemann equations do not hold for any $z=x+i y$. Consequently, the function is not analytic at any point in the complex plane.
 (b) Using the definition (1), it is straightforward to show that the derivative of the linear function $f(z)=\alpha z+\beta$ is $f^{\prime}(z)=\alpha$. Let us derive this result using Theorem 1 . Write $\alpha=a+i b$ and $\beta=c+i d, u(x, y)=a x-b y+c$ and $v(x, y)=b x+a y+d$. Then $u_{x}=a, u_{y}=-b, v_{x}=b$, and $v_{y}=a$. Thus $u_{x}=v_{y}$ and $u_{y}=-v_{x}$ for all $(x, y)$. Hence the Cauchy-Riemann equations hold and the partial derivatives are continuous at all points. It follows that the function is analytic for all $z$. Moreover, $f^{\prime}(z)=u_{x}+i v_{x}=a+i b=\alpha$.
-(c) If $f(z)=e^{z}$, then $u=e^{x} \cos y, v=e^{x} \sin y, u_{x}=e^{x} \cos y, u_{y}=-e^{x} \sin y$, $v_{x}=e^{x} \sin y$, and $v_{y}=e^{x} \cos y$. The partial derivatives are continuous and satisfy the Cauchy-Riemann equations: $u_{x}=v_{y}$ and $u_{y}=-v_{x}$ for all $(x, y)$. Consequently, $f(z)=e^{z}$ is analytic for all $z$ and $f^{\prime}(z)=u_{x}+i v_{x}=e^{x} \cos y+i \rho^{x} \sin y=e^{z}$.
+(c) If $f(z)=e^{z}$, then $u=e^{x} \cos y, v=e^{x} \sin y, u_{x}=e^{x} \cos y, u_{y}=-e^{x} \sin y$, $v_{x}=e^{x} \sin y$, and $v_{y}=e^{x} \cos y$. The partial derivatives are continuous and satisfy the Cauchy-Riemann equations: $u_{x}=v_{y}$ and $u_{y}=-v_{x}$ for all $(x, y)$. Consequently, $f(z)=e^{z}$ is analytic for all $z$ and $f^{\prime}(z)=u_{x}+i v_{x}=e^{x} \cos y+i e^x \sin y=e^{z}$.
 (d) It is a straightforward exercise to show that $\sin z$ is analytic for all $z$ and $\frac{d}{d z} \sin z=\cos z$ (Exercise 27(a)).
 (e) Similarly, $\cos z$ is analytic for all $z$ and $\frac{d}{d z} \cos z=-\sin z$ (Exercise 27(b)).
 (f) As in the real case, if $f(z)$ is analytic at a point $z$ then it is necessarily continuous at $z$. Thus $\log z$ is not analytic at the branch cut since it is not continuous there. For all other points in the complex plane, recall from Example 1(f) that $u(x, y)=\frac{1}{2} \ln \left(x^{2}+y^{2}\right)$. So
@@ -182,7 +273,7 @@
 u_{x}=\frac{x}{x^{2}+y^{2}} \quad \text { and } \quad u_{y}=\frac{y}{x^{2}+y^{2}} .
 $$
 
-In terms of the inverse tangent, the imaginary part of $\log z$ is $v(x, y)=\tan ^{-1} \underset{x}{y}+ k \pi$, where $k=0, \pm 1$, depending on the location of the point ( $x, y$ ) (see the discussion following Example 3, below). Using that $\frac{d}{d x} \tan ^{-1} x=\frac{1}{1+x^{2}}$ and the chain rule, it is straightforward to show that
+In terms of the inverse tangent, the imaginary part of $\log z$ is $v(x, y)=\tan^{-1}(y/x)+ k \pi$, where $k=0, \pm 1$, depending on the location of the point ( $x, y$ ) (see the discussion following Example 3, below). Using that $\frac{d}{d x} \tan ^{-1} x=\frac{1}{1+x^{2}}$ and the chain rule, it is straightforward to show that
 
 $$
 v_{x}=\frac{-y}{x^{2}+y^{2}} \quad \text { and } \quad v_{y}=\frac{x}{x^{2}+y^{2}}
@@ -196,56 +287,55 @@
 
 You should justify the last equality (Exercise 53). $\square$
 
-Functions that are analytic for all $z$ are called entire. Thus $\alpha z+\beta, e^{z}$, $\cos z$, and $\sin z$ are all entire functions, but $\log z$ is not entire.
+> [!definition|88c531a0-86d5-5f63-ac74-4b12f49c99bf.local at=6f435288-03a3-5ea8-a345-b33c2c859469] Entire Function
+> Functions that are analytic for all $z$ are called entire.
+
+Thus $\alpha z+\beta, e^{z}$, $\cos z$, and $\sin z$ are all entire functions, but $\log z$ is not entire.
 
 For ease of reference, we now state some properties of the derivative, which are similar to properties of the derivative of a function of a real variable.
 
-THEOREM 2 PROPERTIES OF ANALYTIC FUNCTIONS
-
-THEOREM 3 ANALYTIC FUNCTIONS AND LAPLACE'S EQUATION
-
-Suppose that $f$ and $g$ are analytic on an open set $S$ and $c_{1}, c_{2}$ are complex constants. Then $c_{1} f+c_{2} g$ and $f g$ are analytic on $S$ with
-
-$$
-\begin{aligned}
-\left(c_{1} f+c_{2} g\right)^{\prime}(z) & =c_{1} f^{\prime}(z)+c_{2} g^{\prime}(z) \text { and } \\
-(f g)^{\prime}(z) & =f^{\prime}(z) g(z)+f(z) g^{\prime}(z) .
-\end{aligned}
-$$
-
-Also, $\frac{f}{g}$ is analytic on $S$ minus the points where $g=0$, and
-
-$$
-\left(\frac{f}{g}\right)^{\prime}(z)=\frac{f^{\prime}(z) g(z)-f(z) g^{\prime}(z)}{(g(z))^{2}} \quad(g(z) \neq 0) .
-$$
-
-If $g$ is analytic at $z_{0}$ and $f$ is analytic at $g\left(z_{0}\right)$, then the composition $(f \circ g)(z)$ is analytic at $z_{0}$ and we have the chain rule
-
-$$
-(f \circ g)^{\prime}\left(z_{0}\right)=f^{\prime}\left(g\left(z_{0}\right)\right) g^{\prime}\left(\sigma_{0}\right)
-$$
+> [!theorem|52a6a037-84b9-5823-bda1-5ba137365ab9.local at=f28a0cb1-e92f-5908-b201-1cad8e00aa98] Properties of Analytic Functions
+> Suppose that $f$ and $g$ are analytic on an open set $S$ and $c_{1}, c_{2}$ are complex constants. Then $c_{1} f+c_{2} g$ and $f g$ are analytic on $S$ with
+>
+> $$
+> \begin{aligned}
+> \left(c_{1} f+c_{2} g\right)^{\prime}(z) & =c_{1} f^{\prime}(z)+c_{2} g^{\prime}(z) \text { and } \\
+> (f g)^{\prime}(z) & =f^{\prime}(z) g(z)+f(z) g^{\prime}(z) .
+> \end{aligned}
+> $$
+>
+> Also, $\frac{f}{g}$ is analytic on $S$ minus the points where $g=0$, and
+>
+> $$
+> \left(\frac{f}{g}\right)^{\prime}(z)=\frac{f^{\prime}(z) g(z)-f(z) g^{\prime}(z)}{(g(z))^{2}} \quad(g(z) \neq 0) .
+> $$
+>
+> If $g$ is analytic at $z_{0}$ and $f$ is analytic at $g\left(z_{0}\right)$, then the composition $(f \circ g)(z)$ is analytic at $z_{0}$ and we have the chain rule
+>
+> $$
+> (f \circ g)^{\prime}\left(z_{0}\right)=f^{\prime}\left(g\left(z_{0}\right)\right) g^{\prime}\left(z_0\right)
+> $$
+
+*Printed equation labels: (4) linear combination; (5) product; (6) quotient; (7) chain rule.*
 
 Using linear combinations of powers of $z$ and appealing to Theorem 2, we conclude that a polynomial $p(z)=a_{n} z^{n}+a_{n-1} z^{n-1}+\cdots+a_{1} z+a_{0}$ is an entire function. Appealing to the quotient rule, we see that a rational function $q(z)=\frac{f(z)}{g(z)}$, where $f$ and $g$ are polynomials, is analytic at all $z$ where $g(z) \neq 0$.
 
-Typically, any function that algebraically manipulates $z$ will be differentiable; however, as we saw in Example 2(a), analyticity can easily fail. Functions such as $\operatorname{Re} z, \operatorname{Im} z$, and $\bar{z}$ are not analytic at any point. (See Exercise 30.)
+Polynomial and rational expressions in $z$ are analytic wherever their denominators do not vanish; however, as we saw in Example 2(a), analyticity can easily fail. Functions such as $\operatorname{Re} z, \operatorname{Im} z$, and $\bar{z}$ are not analytic at any point. (See Exercise 30.)
 
 ## The Role of Analytic Functions
 
 Soon we will show powerful applications of analytic functions to partial differential equations. Indeed, the connection between these two fields can be established at this point using the Cauchy-Riemann equations. We have the following important result.
 
-Suppose that $f=u+i v$ is analytic on an open set $S$. Then its real and imaginary parts, $u(x, y)$ and $v(x, y)$, are harmonic on $S$; that is, $u$ and $v$ satisfy Laplace's equation $\nabla^{2} \phi=0$ on $S$.
-
-Proof By a well-know property of analytic functions, if $f$ is analytic then it has derivatives of all orders. This implies that if $f=u+i v$ is analytic then $u$ and $v$ have partial derivatives of all orders and these derivatives are continuous. Moreover, since $f$ is analytic, by the Cauchy-Riemann equations, we have
+> [!theorem|b7a06797-f906-50ff-8bce-f74fe316c00c.local at=23d4e2e9-dc45-5f38-a0ef-c7277625cf49] Analytic Functions and Laplace's Equation
+> Suppose that $f=u+i v$ is analytic on an open set $S$. Then its real and imaginary parts, $u(x, y)$ and $v(x, y)$, are harmonic on $S$; that is, $u$ and $v$ satisfy Laplace's equation $\nabla^{2} \phi=0$ on $S$.
+
+Proof By a well-known property of analytic functions, if $f$ is analytic then it has derivatives of all orders. This implies that if $f=u+i v$ is analytic then $u$ and $v$ have partial derivatives of all orders and these derivatives are continuous. Moreover, since $f$ is analytic, by the Cauchy-Riemann equations, we have
 
 $$
 u_{x}=v_{y} \quad \text { and } \quad u_{y}=-v_{x} .
 $$
 
-![](./images/7ce1063d-f13d-4631-8956-8a97e0eaf48a-42_332_465_987_61.jpg)
-Figure 8 The inverse tangent takes its values in $\left(\frac{-\pi}{2}, \frac{\pi}{2}\right)$.
-
-![](./images/7ce1063d-f13d-4631-8956-8a97e0eaf48a-42_366_469_1728_59.jpg)
-Figure 9 Computing $\operatorname{Arg} z$.
+
 
 Taking derivatives of second order, we find
 
@@ -260,16 +350,48 @@
 
 We can use Theorem 3 to generate many interesting examples of harmonic functions; simply take the real or imaginary part of any analytic function.
 
-## EXAMPLE 3 Harmonic functions
+> [!exercise|ecf8facc-3987-5418-a20c-628291c61007.local at=927f9027-32af-578d-b502-0aba6036634b] EXAMPLE 3 Harmonic functions
+> Use the real and imaginary parts of (a) $z^2$, (b) $e^z$, and (c) the principal logarithm to obtain harmonic functions and specify their domains.
+
+##### solution
 
 (a) The function $f(z)=z^{2}=x^{2}-y^{2}+2 i x y$ is entire. Thus $u(x, y)=x^{2}-y^{2}$ and $v(x, y)=x y$ are harmonic for all $(x, y)$, because $u=\operatorname{Re} f$ and $v=\frac{1}{2} \operatorname{Im} f$.
 (b) The function $f(z)=e^{z}=e^{x}(\cos y+i \sin y)$ is entire. Thus $u(x, y)=e^{x} \sin y$ and $v(x, y)=e^{x} \cos y$ are harmonic for all $(x, y)$.
-(c) The function $f(z)=\log z=\ln |z|+i \operatorname{Arg} z$ is analytic on $\mathbb{C}$ minus $(-\infty, 0]$. Thus $u(x, y)=\ln |z|=\frac{1}{2} \ln \left(x^{2}+y^{2}\right)$ and $v(x, y)=\operatorname{Arg} ;$ are harmonic on the region $\Omega=\mathbb{C} \backslash(-\infty, 0]$. (In fact, we know from Proposition 2. Section 16.2, that $\frac{1}{2} \ln \left(x^{2}+y^{2}\right)$ is harmonic for all $(x, y) \neq(0,0)$.)
-
-The function $\operatorname{Arg} z$ is harmonic for all $z$ except for $z=a$ : with $x \leq 0$. It is useful to have an expression of $\operatorname{Arg} z$ in terms of $x$ and $y$. Recall that the inverse tangent is a function that takes values in the interval $\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$ (Figure 8), thus the equality $\operatorname{Arg} z=\tan ^{-1}\left(\frac{y}{x}\right)$ holds only when $\operatorname{Arg} z$ is in the interval $\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$. If $\operatorname{Arg} z$ is not in this interval, we need to modify the value of the inverse tangent by adding $\pm \pi$. You can check that for $z=x+i y$ with $x \neq 0$,
+(c) The function $f(z)=\log z=\ln |z|+i \operatorname{Arg} z$ is analytic on $\mathbb{C}$ minus $(-\infty, 0]$. Thus $u(x, y)=\ln |z|=\frac{1}{2} \ln \left(x^{2}+y^{2}\right)$ and $v(x, y)=\operatorname{Arg} z$ are harmonic on the region $\Omega=\mathbb{C} \backslash(-\infty, 0]$. (In fact, we know from Proposition 2. Section 16.2, that $\frac{1}{2} \ln \left(x^{2}+y^{2}\right)$ is harmonic for all $(x, y) \neq(0,0)$.)
+
+```scientific-figure
+id: e24e7733-6035-42b8-992d-81cc53e84da9
+numbered: false
+title: ""
+caption: Figure 8 The inverse tangent takes its values in $\left(\frac{-\pi}{2}, \frac{\pi}{2}\right)$.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 16 Green's Functions and Conformal Mappings/images/7ce1063d-f13d-4631-8956-8a97e0eaf48a-42_332_465_987_61.jpg
+    caption: ""
+```
+
+
+```scientific-figure
+id: f8c2a35f-ff2a-42a1-a4f6-1c09d87d3893
+numbered: false
+title: ""
+caption: Figure 9 Computing $\operatorname{Arg} z$.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 16 Green's Functions and Conformal Mappings/images/7ce1063d-f13d-4631-8956-8a97e0eaf48a-42_366_469_1728_59.jpg
+    caption: ""
+```
+
+
+The function $\operatorname{Arg} z$ is harmonic for all $z$ except for $z=x$ with $x \leq 0$. It is useful to have an expression of $\operatorname{Arg} z$ in terms of $x$ and $y$. Recall that the inverse tangent is a function that takes values in the interval $\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$ (Figure 8), thus the equality $\operatorname{Arg} z=\tan ^{-1}\left(\frac{y}{x}\right)$ holds only when $\operatorname{Arg} z$ is in the interval $\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$. If $\operatorname{Arg} z$ is not in this interval, we need to modify the value of the inverse tangent by adding $\pm \pi$. You can check that for $z=x+i y$ with $x \neq 0$,
 
 $$
 \operatorname{Arg} z= \begin{cases}\tan ^{-1}\left(\frac{y}{x}\right) & \text { if } x>0 ; \\ \tan ^{-1}\left(\frac{y}{x}\right)+\pi & \text { if } x<0 \text { and } y \geq 0 ; \\ \tan ^{-1}\left(\frac{y}{x}\right)-\pi & \text { if } x<0 \text { and } y<0 .\end{cases}
+\tag{8}
 $$
 
 For example, in Figure 9, the point $z_{1}=2+3 i$ is in the first quadrant. Using a calculator, we find $\operatorname{Arg} z_{1}=\tan ^{-1} \frac{3}{2} \approx 0.983$. The point $z_{2}=-2-3 i$, is in the third quadrant, $\operatorname{Arg} z_{2}=\tan ^{-1} \frac{3}{2}-\pi \approx-2.159$. (We remind you that all angles are measured in radians.)
@@ -278,28 +400,42 @@
 
 $$
 \operatorname{Arg} z=\operatorname{Arg}(i y)= \begin{cases}\frac{\pi}{2} & \text { if } y>0 \\ -\frac{\pi}{2} & \text { if } y<0\end{cases}
-$$
-
-![](./images/7ce1063d-f13d-4631-8956-8a97e0eaf48a-43_311_456_347_49.jpg)
-Figure 10 The inverse cotangent takes its values in $(0, \pi)$.
-
-It is sometimes more convenient to use the inverse cotangent, especially for points in the upper half-plane. The inverse cotangent bakes its values in $(0, \pi)$ (Figure 10) and hence coincides with the values of $\operatorname{Arg} z$ if $\operatorname{Im} z>0$. We have
+\tag{9}
+$$
+
+```scientific-figure
+id: 2c3f14ea-89b2-4c0c-aa43-3b3adccc18b0
+numbered: false
+title: ""
+caption: Figure 10 The inverse cotangent takes its values in $(0, \pi)$.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 16 Green's Functions and Conformal Mappings/images/7ce1063d-f13d-4631-8956-8a97e0eaf48a-43_311_456_347_49.jpg
+    caption: ""
+```
+
+
+It is sometimes more convenient to use the inverse cotangent, especially for points in the upper half-plane. The inverse cotangent takes its values in $(0, \pi)$ (Figure 10) and hence coincides with the values of $\operatorname{Arg} z$ if $\operatorname{Im} z>0$. We have
 
 $$
 \operatorname{Arg} z=\cot ^{-1}\left(\frac{x}{y}\right) \text { if } y>0 .
+\tag{10}
 $$
 
 Notice that $\operatorname{Arg} z$ is constant on rays through the origin; more generally, the function $u(z)=a \operatorname{Arg} z+b$, where $a$ and $b$ are real numbers, is constant on rays through the origin. This characteristic property of the argument function helps us solve certain Dirichlet problems, as we now illustrate.
 
-## EXAMPLE 4 Using the argument function
-
-Solve the Dirichlet problem $\nabla^{2} u=0$ in the half-plane $y>0$, given the boundary values
-
-$$
-u(x, 0)= \begin{cases}100 & \text { if } x>0 \\ 50 & \text { if } x<0\end{cases}
-$$
-
-Solution Since the boundary condition is constant on the rays $x \geq 0$ and $x \leq 0$, it is reasonable to expect that the solution be constant on rays in the upper half-plane. Based on this expectation, we try for a solution the function $u(x, y)=a \operatorname{Arg} z+b$, where $a$ and $b$ are real numbers and $z=x+i y$. The function is harmonic in the upper half-plane. Its values on the boundary are $u(x, 0)=b$ if $x>0$ and $u(x, 0)=a \pi+b$ if $x<0$. Thus, to satisty the boundary conditions, take $b=100$ and $a \pi+100=50$, so $a=-\frac{50}{\pi}$. Hence
+> [!exercise|c3502efa-9a26-5b57-a30d-f3c73e924d28.local at=ef3f6410-92a0-5e7b-b0c4-b0901eb52ac6] EXAMPLE 4 Using the argument function
+> Find the bounded harmonic solution of the Dirichlet problem $\nabla^2u=0$ in the half-plane $y>0$, given the boundary values
+>
+> $$
+> u(x, 0)= \begin{cases}100 & \text { if } x>0 \\ 50 & \text { if } x<0\end{cases}
+> $$
+
+##### solution
+
+Since the boundary condition is constant on the rays $x \geq 0$ and $x \leq 0$, it is reasonable to expect that the solution be constant on rays in the upper half-plane. Based on this expectation, we try for a solution the function $u(x, y)=a \operatorname{Arg} z+b$, where $a$ and $b$ are real numbers and $z=x+i y$. The function is harmonic in the upper half-plane. Its values on the boundary are $u(x, 0)=b$ if $x>0$ and $u(x, 0)=a \pi+b$ if $x<0$. Thus, to satisfy the boundary conditions, take $b=100$ and $a \pi+100=50$, so $a=-\frac{50}{\pi}$. Hence
 
 $$
 u(x, y)=-\frac{50}{\pi} \operatorname{Arg} z+100 .
@@ -313,29 +449,52 @@
 
 As $y \rightarrow 0^{+}, \cot ^{-1}\left(\frac{x}{y}\right)$ tends to 0 if $x>0$ and $\pi$ if $x<0$, which shows that $u$ satisfies the boundary condition.
 
-If we translate the boundary condition in Example 4 and center it at some point $x_{0}$ other than the origin, then it is necessary to translate the candidate function and consider instead the function $u(z)=a \operatorname{Arg}\left(z-x_{0}\right)+b$, which is also a harmonic function in the upper half-plane. The boundary values in this case are constant on the half-lines $x>x_{0}$ and $x<x_{0}$. As our next example illustrates, we can gencralize this process further and solve an important type of Dirichlet problems, in which the boundary values are constant on intervals. Similar problems were considered in Section 7.5.
-
-![](./images/7ce1063d-f13d-4631-8956-8a97e0eaf48a-44_428_456_481_65.jpg)
-Figure 11 A Dirichlet problem in the upper half-plane.
-
-![](./images/7ce1063d-f13d-4631-8956-8a97e0eaf48a-44_341_454_1144_72.jpg)
-Figure 12 The angle $\alpha(x, y)$ tends to 0 if $(x, y)$ approaches a point on the $x$-axis outside the interval $(a, b)$ and it tends to $\pi$ if $(x, y)$ approaches a point on the $x$-axis inside the interval ( $a, b$ ).
-
-## EXAMPLE 5 Using translates of the argument function
-
-Given $a \therefore b$, solve the Dirichlet problem $\nabla^{2} u=0$ in the upper half-plane, with the boundary values (Figure 11)
-
-$$
-u(x, 0)= \begin{cases}0 & \text { if } x<a, \\ T & \text { if } a<x<b, \\ 0 & \text { if } b<x .\end{cases}
-$$
-
-Solution Due to the nature of the boundary values, we must involve the translates of $\operatorname{Arg} z$ by $a$ and $b$. We thus try for a solution the harmonic function $u(x, y)= \frac{a_{1}}{\pi} \operatorname{Arg}(z-a)+\frac{a_{2}}{\pi} \operatorname{Arg}(z-b)+a_{3}$, where $a_{j}(j=1,2,3)$ are real numbers to be determined. The function is harmonic in the upper half-plane. In order to determine its coefficients, we compute its boundary valucs. For any real number $w$, $\frac{a}{\pi} \operatorname{Arg} w=0$ if $w>0$ and $\frac{a}{\pi} \operatorname{Arg} w=a$ if $w<0$. So you can verify that
+If we translate the boundary condition in Example 4 and center it at some point $x_{0}$ other than the origin, then it is necessary to translate the candidate function and consider instead the function $u(z)=a \operatorname{Arg}\left(z-x_{0}\right)+b$, which is also a harmonic function in the upper half-plane. The boundary values in this case are constant on the half-lines $x>x_{0}$ and $x<x_{0}$. As our next example illustrates, we can generalize this process further and solve an important type of Dirichlet problems, in which the boundary values are constant on intervals. Similar problems were considered in Section 8.5.
+
+```scientific-figure
+id: b0eaac90-6f01-4ebc-8ca2-2c0df829c143
+numbered: false
+title: ""
+caption: Figure 11 A Dirichlet problem in the upper half-plane.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 16 Green's Functions and Conformal Mappings/images/7ce1063d-f13d-4631-8956-8a97e0eaf48a-44_428_456_481_65.jpg
+    caption: ""
+```
+
+
+```scientific-figure
+id: 97c55509-1241-46d9-9b20-f6b362d0f9c0
+numbered: false
+title: ""
+caption: Figure 12 The angle $\alpha(x, y)$ tends to 0 if $(x, y)$ approaches a point on the $x$-axis outside the interval $(a, b)$ and it tends to $\pi$ if $(x, y)$ approaches a point on the $x$-axis inside the interval ( $a, b$ ).
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 16 Green's Functions and Conformal Mappings/images/7ce1063d-f13d-4631-8956-8a97e0eaf48a-44_341_454_1144_72.jpg
+    caption: ""
+```
+
+
+> [!exercise|4ce0b408-5f98-55f4-b815-168e1a35e7cf.local at=340cdc54-2a60-59d6-b0f8-3653cd0e9062] EXAMPLE 5 Using translates of the argument function
+> Given $a<b$, find the bounded harmonic solution of the Dirichlet problem $\nabla^{2} u=0$ in the upper half-plane, with the boundary values (Figure 11)
+>
+> $$
+> u(x, 0)= \begin{cases}0 & \text { if } x<a, \\ T & \text { if } a<x<b, \\ 0 & \text { if } b<x .\end{cases}
+> $$
+
+##### solution
+
+Due to the nature of the boundary values, we must involve the translates of $\operatorname{Arg} z$ by $a$ and $b$. We thus try for a solution the harmonic function $u(x, y)= \frac{a_{1}}{\pi} \operatorname{Arg}(z-a)+\frac{a_{2}}{\pi} \operatorname{Arg}(z-b)+a_{3}$, where $a_{j}(j=1,2,3)$ are real numbers to be determined. The function is harmonic in the upper half-plane. In order to determine its coefficients, we compute its boundary values. For any real number $w$, $\frac{a}{\pi} \operatorname{Arg} w=0$ if $w>0$ and $\frac{a}{\pi} \operatorname{Arg} w=a$ if $w<0$. So you can verify that
 
 $$
 u(x, 0)=\left\{\begin{aligned}
 a_{1}+a_{2}+a_{3} & \text { if } x<a, \\
 a_{2}+a_{3} & \text { if } a<x<b, \\
-a_{3} & \text { if } b \cdot x .
+a_{3} & \text { if } b<x .
 \end{aligned}\right.
 $$
 
@@ -355,30 +514,36 @@
 u(x, y)=\frac{T}{\pi}\left[\cot ^{-1}\left(\frac{x-b}{y}\right)-\cot ^{-1}\left(\frac{x-a}{y}\right)\right] .
 $$
 
-In Figure 12, we have $\cot ^{-1}\left(\frac{x-b}{y}\right)=\alpha_{2}$ and $\cot ^{-1}\left(\frac{x-a}{y}\right)=\alpha_{1}$. Since the sum of the interior angles in a triangle is $\pi$, we obtain $\alpha_{1}+\left(\pi-\alpha_{2}\right)+\alpha(x, y)=\pi$, where $\alpha(x, y)$ is the angle at the point ( $x, y$ ) subtended by the interval ( $a, b$ ). Hence $\alpha(x, y)=\alpha_{2}-\alpha_{1}$, and so $u(x, y)$ is equal to a constant times $\alpha(x, y)$. In particular, $\alpha(x, y)$ is a harmonic function of ( $x, y$ ) in the upper half-plane, which tends to $\pi$ if we approach a boundary point in the interval $(a, b)$ and to 0 if we approach a boundary point outside the interval $(a, b)$. This is a useful fact that was observed in the exercises of Section 7.5. The function $\alpha(x, y)$ is called the harmonic measure of the interval ( $a, b$ ).
+In Figure 12, we have $\cot ^{-1}\left(\frac{x-b}{y}\right)=\alpha_{2}$ and $\cot ^{-1}\left(\frac{x-a}{y}\right)=\alpha_{1}$. Since the sum of the interior angles in a triangle is $\pi$, we obtain $\alpha_{1}+\left(\pi-\alpha_{2}\right)+\alpha(x, y)=\pi$, where $\alpha(x, y)$ is the angle at the point ( $x, y$ ) subtended by the interval ( $a, b$ ). Hence $\alpha(x, y)=\alpha_{2}-\alpha_{1}$, and so $u(x, y)$ is equal to a constant times $\alpha(x, y)$. In particular, $\alpha(x, y)$ is a harmonic function of ( $x, y$ ) in the upper half-plane, which tends to $\pi$ if we approach a boundary point in the interval $(a, b)$ and to 0 if we approach a boundary point outside the interval $(a, b)$. This is a useful fact that was observed in the exercises of Section 8.5. The function $\alpha(x,y)/\pi$ is called the harmonic measure of the interval $(a,b)$.
 
 ## The Harmonic Conjugate
 
-Theorem 3 tells us that the real and imaginary parts of an analytic function are harmonic. Is every harmonic function the real or imaginary part of an
-
-THEOREM 4 HARMONIC CONJUGATE
-analytic function? More specifically, given a harmonic function $u$ on a region $\Omega$, can we find another harmonic function $v$ on $\Omega$ such that $f=u+i v$ is analytic on $\Omega$ ? If such a function $v$ exists, it is called a harmonic conjugate of $u$. The following result answers our question.
-
-Suppose that $\Omega$ is a region (open and connected). Then every harmonic function $u$ on $\Omega$ has a harmonic conjugate $v$ on $\Omega$ if and only if $\Omega$ is simply connected (see Section 16.1 for the definition).
-
-The statement of the theorem may appear unusual since the condition for the existence of the harmonic conjugate of $u$ is placed on the region and not on $u$ itself. To understand this peculiarity, consider the function $\frac{1}{2} \ln \left(x^{2}+y^{2}\right)$, which is harmonic on the region $\Omega_{1}=\mathbb{C}$ minus ( 0,0 ). It can be shown that $\frac{1}{2} \ln \left(x^{2}+y^{2}\right)$ does not have a harmonic conjugate on $\Omega_{1}$. However, since $\log z=\frac{1}{2} \ln \left|\ln \left(x^{2}+y^{2}\right)\right|+i \operatorname{Arg} z$ is analytic in $\Omega_{2}=\mathbb{C}$ minus $(-\infty, 0]$, it follows that a harmonic conjugate of $\frac{1}{2} \ln \left(x^{2}+y^{2}\right)$ in $\Omega_{2}$ is $\operatorname{Arg} z$. This example shows that the underlying region is crucial for the existence of the harmonic conjugate.
+Theorem 3 tells us that the real and imaginary parts of an analytic function are harmonic. Is every harmonic function the real or imaginary part of an analytic function? More specifically, given a harmonic function $u$ on a region $\Omega$, can we find another harmonic function $v$ on $\Omega$ such that $f=u+i v$ is analytic on $\Omega$ ?
+
+> [!definition|715fe8a9-cd33-5925-878f-de84255bbee7.local at=11b37645-96d6-5666-b4b8-bef8bba1ed00] Harmonic Conjugate of a Real Harmonic Function
+> If a harmonic function $v$ exists such that $u+iv$ is analytic on the region where $u$ is harmonic, it is called a harmonic conjugate of $u$.
+
+The following result answers our question.
+
+> [!theorem|d0d34a97-7afe-5050-b4d6-aa73417469ef.local at=9952bf75-89e2-556b-83d0-c2a3b533e215] Harmonic Conjugate
+> Suppose that $\Omega$ is a region (open and connected). Then every harmonic function $u$ on $\Omega$ has a harmonic conjugate $v$ on $\Omega$ if and only if $\Omega$ is simply connected.
+
+The statement of the theorem may appear unusual since the condition for the existence of the harmonic conjugate of $u$ is placed on the region and not on $u$ itself. To understand this peculiarity, consider the function $\frac{1}{2} \ln \left(x^{2}+y^{2}\right)$, which is harmonic on the region $\Omega_{1}=\mathbb{C}$ minus ( 0,0 ). It can be shown that $\frac{1}{2} \ln \left(x^{2}+y^{2}\right)$ does not have a harmonic conjugate on $\Omega_{1}$. However, since $\log z=\frac12\ln(x^2+y^2)+i \operatorname{Arg} z$ is analytic in $\Omega_{2}=\mathbb{C}$ minus $(-\infty, 0]$, it follows that a harmonic conjugate of $\frac{1}{2} \ln \left(x^{2}+y^{2}\right)$ in $\Omega_{2}$ is $\operatorname{Arg} z$. This example shows that the underlying region is crucial for the existence of the harmonic conjugate.
 
 Theorem 4 guarantees the existence of a harmonic conjugate on any simply connected region such as the entire plane, a disk, a half-plane, a sector, or any other open and connected region with no holes in it. For an arbitrary region, we can always take a disk inside the region around any given point and then apply Theorem 4. As a result, we can say that any harmonic function is locally the real (or imaginary) part of an analytic function, where by "locally" we mean on any disk in the region where the function is harmonic.
 
 Finding the harmonic conjugate can be achieved with the help of the Cauchy-Riemann equations, as we now illustrate.
 
-## EXAMPLE 6 Finding harmonic conjugates
-
-Show that $u(x, y)=x^{2}-y^{2}+x$ is harmonic in the entire plane and find a harmonic conjugate.
-Solution We have $u_{x x}=2$ and $u_{y y}=-2$; hence $u_{x x}+u_{y y}=0$, and so $u$ is harmonic. To find a harmonic conjugate $v$, we use the Cauchy-Riemann equations as follows. We want $u+i v$ to be analytic. Hence $v$ must satisfy the Cauchy-Riemann equations
+> [!exercise|e7190f17-df75-5024-a965-4cc14f4131ac.local at=f1868278-9309-57b4-a3f4-65f0960d9406] EXAMPLE 6 Finding harmonic conjugates
+> Show that $u(x, y)=x^{2}-y^{2}+x$ is harmonic in the entire plane and find a harmonic conjugate.
+
+##### solution
+
+We have $u_{x x}=2$ and $u_{y y}=-2$; hence $u_{x x}+u_{y y}=0$, and so $u$ is harmonic. To find a harmonic conjugate $v$, we use the Cauchy-Riemann equations as follows. We want $u+i v$ to be analytic. Hence $v$ must satisfy the Cauchy-Riemann equations
 
 $$
 \frac{\partial u}{\partial x}=\frac{\partial v}{\partial y}, \quad \text { and } \quad \frac{\partial u}{\partial y}=-\frac{\partial v}{\partial x} .
+\tag{11}
 $$
 
 Since $\frac{\partial u}{\partial x}=2 x+1$, the first equation implies that
@@ -407,13 +572,13 @@
 - Is $v$ unique?
 - What is a harmonic conjugate of $v$ ?
 
-On any given simply connected region, $v$ is unique up to an additive constant. Also, if $v$ is a harmonic conjugate of $u$, then $-u$ is a harmonic conjugate of $v$ (Exercise 54).
+On any connected region where a harmonic conjugate exists, $v$ is unique up to an additive constant. Also, if $v$ is a harmonic conjugate of $u$, then $-u$ is a harmonic conjugate of $v$ (Exercise 54).
 
 ## Orthogonal Trajectories and Harmonic Conjugates
 
 So far we have defined the harmonic conjugate of a harmonic function $u$ as the imaginary part of an analytic function, $f=u+i v$, whose real part is $u$. We now interpret the harmonic conjugate in terms of orthogonal trajectories. This geometric interpretation gives the harmonic conjugate a concrete meaning.
 
-Given a function of two variables, $u(x, y)$, the level curves of $u$ are defined by the equation $u(x . y)=C$. where $C$ is a constant in the range of $u$. To compute the slope of the tangent line, $\frac{d y}{d x}$, at a point on a level curve, we use the chain rule in two dimensions and differentiate with respect to $x$ both sides of $u(x, y)=C$ and get
+Given a function of two variables, $u(x, y)$, the level curves of $u$ are defined by the equation $u(x,y)=C$. where $C$ is a constant in the range of $u$. To compute the slope of the tangent line, $\frac{d y}{d x}$, at a point on a level curve, we use the chain rule in two dimensions and differentiate with respect to $x$ both sides of $u(x, y)=C$ and get
 
 $$
 u_{x} \frac{d x}{d x}+u_{y} \frac{d y}{d x}=0
@@ -427,50 +592,62 @@
 
 The orthogonal trajectories to the level curves $u(x, y)=C$ is the family of curves that intersects the level curves $u(x, y)=C$ at right angle at each point. Clearly, the two families of curves are mutually orthogonal.
 
-Suppose that we have expressed the orthogonal trajectories in the form $\dot{\psi}(x, y)=C^{\prime}$ for some function $\psi$. As we just showed, the slope of the tangent line at any point of the orthogonal curves is given by $m_{2}=\frac{d y}{d x}=-\frac{v_{x}}{v_{y}}$. Since the slopes of orthogonal curves are negative reciprocals, we have
+Suppose that we have expressed the orthogonal trajectories in the form $\psi(x, y)=C^{\prime}$ for some function $\psi$. At regular points where the displayed denominators are nonzero, the slope of the tangent line at any point of the orthogonal curves is given by $m_{2}=\frac{d y}{d x}=-\frac{\psi_x}{\psi_y}$. Since the slopes of orthogonal curves are negative reciprocals, we have
+
+$$
+m_{1} \cdot m_{2}=-1 \Leftrightarrow \frac{u_{x}}{u_{y}} \cdot \frac{\psi_{x}}{\psi_{y}}=-1
+$$
+
 equivalently, the condition for two families to be mutually orthogonal is
 
-Now suppose that $u$ is a harmonic function with harmonic conjugate $v$, and let us consider the level curves $u(x, y)=C$ and $v(x, y)=C^{\prime}$. Since $u+i v$ is analytic, the Cauchy Riemann equations hold: $u_{x}=v_{y}$ and $u_{y}=-v_{x}$. By (12), it follows that $u(x, y)=C$ and $v(x, y)=C^{\prime}$ are orthogonal families of curves. We thus have the following useful result.
-
-Suppose that we have expressed the orthogonal trajectories in the form $\psi(x, y)=C^{\prime}$ for some function $\psi$. As we just showed, the slope of the tangent
-line at any point of the orthogonal curves is given by $m_{2}=\frac{d y}{d x}=-\frac{v_{x}}{v_{y}}$. Since
-the slopes of orthogonal curves are negative reciprocals, we have
-
-$$
-m_{1} \cdot m_{2}=-1 \Leftrightarrow \frac{u_{x}}{u_{y}} \cdot \frac{\psi_{x}}{\psi_{y}}=-1
-$$
-
-equivalently, the condition for two families to be mutually orthogonal is
-
 $$
 \frac{u_{x}}{u_{y}}=-\frac{\psi_{y}}{\psi_{x}}
 $$
 
-![](./images/7ce1063d-f13d-4631-8956-8a97e0eaf48a-47_50_1159_825_652.jpg)
-![](./images/7ce1063d-f13d-4631-8956-8a97e0eaf48a-47_45_58_782_1008.jpg)增 Now suppose that $u$ is a harmonic function with harmonic conjugate $v$, and
-let us consider the level curves $u(x, y)=C$ and $v(x, y)=C^{\prime}$. Since $u+i v$ is
-analytic, the Cauchy Riemann equations hold: $u_{x}=v_{y}$ and $u_{y}=-v_{x}$. By
-(12), it follows that $u(x, y)=C$ and $v(x, y)=C^{\prime}$ are orthogonal familics of
-curves. We thus have the following useful result. "
-
-## THEOREM 5 ORTHOGONAL TRAJECTORIES <br> THEOREM 5 ORTHOGONAL S
-
-If $u$ is harmonic and $v$ is a harmonic conjugate of $u$, then the level curves $u(x, y)=C$ and $v(x, y)=C^{\prime}$ are mutually orthogonal.
-
-We give two interpretations of a harmonic conjugate. In heat flow, we can think of $u(x, y)$ as the solution of a Dirichlet problem on a region $\Omega$. Then the level curves $u(. x . y)=C$ represent the isotherms or curves of constant temperature inside $\Omega$. The curves of heat flow inside $\Omega$ are the curves that give the direction along which heat is flowing inside $\Omega$. According to Fourier's law of heat conduction, heat flows from hot to cold in the direction in which the temperature difference is the greatest. If along the isotherms the temperature difference is 0 (the temperature is constant), then the temperature difference is largest along the curves that are orthogonal to the isotherms. (Recall that the gradient of $u, \nabla u=\left(u_{x}, u_{y}\right)$, points in the direction of greatest change in a function, and the gradient is perpendicular to the level curves of $u$.) Consequently, by Theorem 5, the curves of heat flow are given by the level curves of the harmonic conjugate $v$ of $u$.
-
-In electricity and magnetism, the force of attraction or repulsion between charged particles is the gradient of a harmonic function $u$, known as the electrostatic potential. The level curves, $u(x, y)=C$, represcut the equipotential lines. In this case, the level curves of a harmonic conjugate $v$ of $u$ give the direction of the electric force in the field and are known as the lines of force.
-
-![](./images/7ce1063d-f13d-4631-8956-8a97e0eaf48a-48_329_459_414_74.jpg)
-Figure 13 The isotherms are rays at angle $\frac{\pi}{50}(100-T)$.
-
-![](./images/7ce1063d-f13d-4631-8956-8a97e0eaf48a-48_336_463_1066_72.jpg)
-Figure 14 The isotherms and curves of heat flow are orthogonal.
-
-## EXAMPLE 7 Isotherms and curves of heat flow
-
-Determine the isotherms and curves of heat flow in Example 4.
-Solution The boundary values are 50 and 100 , so the temperature inside the region will vary between these two values. For $50<T<100$, the isotherms are given by the level curves $u(x, y)=T$, or
+
+Now suppose that $u$ is a harmonic function with harmonic conjugate $v$, and let us consider the level curves $u(x, y)=C$ and $v(x, y)=C^{\prime}$. Since $u+i v$ is analytic, the Cauchy Riemann equations hold: $u_{x}=v_{y}$ and $u_{y}=-v_{x}$. At points where the complex derivative is nonzero, it follows that $u(x, y)=C$ and $v(x, y)=C^{\prime}$ are orthogonal families of curves. We thus have the following useful result.
+
+> [!theorem|504a572f-b3e7-5934-a665-bc458cbe57bb.local at=cae4b1cb-c767-50df-aeee-fa994f060043] Orthogonal Trajectories
+> If $u$ is harmonic and $v$ is a harmonic conjugate of $u$, then the level curves $u(x,y)=C$ and $v(x,y)=C^{\prime}$ are mutually orthogonal at points where $(u+iv)^{\prime}\ne0$.
+
+We give two interpretations of a harmonic conjugate. In heat flow, we can think of $u(x, y)$ as the solution of a Dirichlet problem on a region $\Omega$. Then the level curves $u(x,y)=C$ represent the isotherms or curves of constant temperature inside $\Omega$. The curves of heat flow inside $\Omega$ are the curves that give the direction along which heat is flowing inside $\Omega$. According to Fourier's law of heat conduction, heat flows from hot to cold in the direction in which the temperature difference is the greatest. If along the isotherms the temperature difference is 0 (the temperature is constant), then the temperature difference is largest along the curves that are orthogonal to the isotherms. (Recall that the gradient of $u, \nabla u=\left(u_{x}, u_{y}\right)$, points in the direction of greatest change in a function, and the gradient is perpendicular to the level curves of $u$.) Consequently, by Theorem 5, the curves of heat flow are given by the level curves of the harmonic conjugate $v$ of $u$.
+
+In a charge-free region with uniform permittivity, an electrostatic potential $u$ is harmonic. The electric field is $-\nabla u$, and the force on a test charge $q$ is $-q\nabla u$.  The level curves, $u(x, y)=C$, represent the equipotential lines. In this case, the level curves of a harmonic conjugate $v$ of $u$ give the direction of the electric force in the field and are known as the lines of force.
+
+```scientific-figure
+id: 37dbb373-eb88-4a42-89ad-56638cbc04c4
+numbered: false
+title: ""
+caption: Figure 13 The isotherms are rays at angle $\frac{\pi}{50}(100-T)$.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 16 Green's Functions and Conformal Mappings/images/7ce1063d-f13d-4631-8956-8a97e0eaf48a-48_329_459_414_74.jpg
+    caption: ""
+```
+
+
+```scientific-figure
+id: 7137c013-c520-4467-b86b-9eff5d21007c
+numbered: false
+title: ""
+caption: Figure 14 The isotherms and curves of heat flow are orthogonal.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 16 Green's Functions and Conformal Mappings/images/7ce1063d-f13d-4631-8956-8a97e0eaf48a-48_336_463_1066_72.jpg
+    caption: ""
+```
+
+
+> [!exercise|78735aa3-8e75-51d6-b5b4-7e3955fe3514.local at=b4bcafbd-060e-50a9-bb1a-7f7f2597cda2] EXAMPLE 7 Isotherms and curves of heat flow
+> Determine the isotherms and curves of heat flow in Example 4.
+
+##### solution
+
+The boundary values are 50 and 100 , so the temperature inside the region will vary between these two values. For $50<T<100$, the isotherms are given by the level curves $u(x, y)=T$, or
 
 $$
 \begin{aligned}
@@ -480,235 +657,462 @@
 \end{aligned}
 $$
 
-Thus the isotherms are rays through the origin at angle $\frac{\pi}{50}(100-T)$, since the slope is $\tan \left[\frac{\pi}{50}(100-T)\right]$. As $T$ varies from 100 to 50 , this angle varies from 0 to $\pi$, which agrees with our expectation, given the boundary conditions. Some isotherms are shown in Figure 13.
+Thus the isotherms are rays through the origin at angle $\frac{\pi}{50}(100-T)$, with this slope except at $T=75$, where the isotherm is the vertical ray $x=0$, $y>0$. As $T$ varies from 100 to 50 , this angle varies from 0 to $\pi$, which agrees with our expectation, given the boundary conditions. Some isotherms are shown in Figure 13.
 
 The curves of heat flow are the level curves of a harmonic conjugate of $u$. From Example 4, $u=-\frac{50}{\pi} \operatorname{Arg} z+100$. Now, recall that $\log z=\ln |z|+i \operatorname{Arg} z$ is analytic in the upper half-plane. So Arg $z$ is a harmonic conjugate of $\ln |z|$; consequently, $-\ln |z|$ is a harmonic conjugate of $\operatorname{Arg} z$. Hence a harmonic conjugate of $u$ is $v=\frac{50}{\pi} \ln |z|$. (Here we have used that if $v$ is a harmonic conjugate of $u$, then $\alpha v$ is a harmonic conjugate of $\alpha u+\beta$, where $\alpha$ and $\beta$ are real constants.) In terms of $x$ and $y$, we have $v(x, y)=(25 / \pi) \ln \left(x^{2}+y^{2}\right)$, and so the curves of heat flow are given by the level curves $(25 / \pi) \ln \left(x^{2}+y^{2}\right)=C$. Multiplying by $\frac{\pi}{25}$ and then taking the exponential, we get $x^{2}+y^{2}=R$, where $R>0$. Thus the curves of heat flow are semi-circles centered at the origin. In Figure 14 we show some isotherms and curves of heat flow. Notice the orthogonality of these two families of curves. Figure 14 also illustrates Fourier's law that heat is flowing from hot to cold in the direction in which the temperature difference is the greatest .
 
 In the following section we explore another connection between analytic functions and harmonic functions, and develop the method of conformal mappings for solving Laplace's equation.
 
-## Exercises 12.5
-
-Exercises 1-20 are intended as reviow of basic topies in complex numbers and functions. In these exercises, take $n=0 \pm 1, \pm 2, \ldots$, and $z=x+i y$, unless otherwise specified.
-In Exercises 1-4, write the given complex number in the form $a+i b$, where $a$ and $b$ are real numbers.
-1.
-(a) $(3+2 i)(2-i)$.
-(b) $\quad(3-i) \overline{(2-i)}$.
-(c) $\frac{1+i}{1-i}$.
-2. (a) $\quad i(2-i)^{2}$.
-(b) $\overline{(3+i) \overline{(1-i)}}$.
-(c) $\frac{2-i}{i}$.
-3. (a) $\frac{1}{i}$.
-(b) $(i)^{n}$.
-(c) $(\bar{i})^{n}$.
-4. (a) $\overline{\left(\frac{3+i}{1-i}\right)}$.
-(b) $i^{2}+i^{20}+i^{200}+i^{202}$.
-(c) $\sum_{n=0}^{1001} i^{n}$.
-
-For the given complex number in Exercises 5-16, (a) find the principal value of the argument. (b) Compute the modulus. (c) Write the number in the form $r^{i \theta}$.
-5. $\quad i$.
-6. $-i$.
-7. $\pi$.
-8. $-\pi$.
-9. $1+i$.
-10. $1-i$.
-11. $-1+i$.
-12. $-1-i$.
-13. $(1+i)^{2}$.
-14. $\frac{1}{1+i}$.
-15. $\cos \alpha+i \sin \alpha$. 16. $\cos \alpha-i \sin \alpha$.
-
-In Exercises 17-20, evaluate the function and write your answer in the form $a+i b$, where $a$ and $b$ are real numbers.
-17.
-(a) $e^{2 i}$.
-(b) $\sin i$.
-(c) $\cos i$.
-(d) $\log i$.
-18.
-(a) $e^{1-\pi i}$.
-(b) $\sin (2+\pi i)$.
-(c) $\log (-7)$.
-(d) $\quad \log 1$.
-19.
-(a) $e^{-\frac{\pi}{2} i}$.
-(b) $e^{2-\frac{\pi}{2} i}$.
-(c) $\quad \log (1-i)$.
-(d) $\quad \log (1-i)^{2}$.
-20.
-(a) $e^{\log (1+5 \pi i)}$.
-(b) $\quad \log \left(e^{1+5 \pi i}\right)$.
-(c) $\log [(-1) \cdot i]$.
-(d) $\log (-1)+\log i$.
-21. Give an example to show that $\log \left(z_{1} \cdot z_{2}\right)$ is not always equal to $\log \left(z_{1}\right)+ \log \left(z_{2}\right)$.
-22. Give an example to show that $\log \left(e^{z}\right)$ is not always equal to $z$. Find a necessary and sufficient condition on $z$ for the equality $\log \left(e^{z}\right)=z$ to hold.
-
-In Exercises 23-26, derive the given identity. Take $z=x+i y$.
-23.
-(a) $\left|e^{z}\right|=e^{x}$.
-(b) $\left|e^{i z}\right|=e^{-y}$.
-24.
-(a) $|\sin z|=\sqrt{\sin ^{2} x+\sinh ^{2} y}$.
-(b) $|\cos z|=\sqrt{\cos ^{2} x+\sinh ^{2} y}$.
-25.
-(a) $\cos (i x)=\cosh x$.
-(b) $\quad \sin (i x)=i \sinh x$.
-26.
-(a) $\overline{e^{z}}=e^{\bar{z}}$.
-(b) $\overline{\sin z}=\sin \bar{z}$.
-
-In Exercises 27-30, use the Cauchy-Riemann equations to verify whether the given function is analytic. If it is, compute its derivative using either one of the identities in (9).
-27.
-(a) $\sin z$.
-(b) $\cos z$.
-28.
-(a) $e^{z}+z$.
-(b) $z^{2}$.
-29.
-(a) $\frac{x+i y}{x^{2}+y^{2}}$.
-(b) $\frac{x-i y}{x^{2}+y^{2}}$.
-30.
-(a) $\bar{z}$.
-(b) $\operatorname{Re} z$.
-
-In Exercises 31-34, verify that the given function is harmonic, and then find a harmonic conjugate using the technique of Example 6.
-31. $x^{2}-y^{2}+x y$.
-32. $x^{2}-y^{2}-2 x+1$.
-33. $e^{x} \cos y$.
-34. $\cos x \sinh y$.
-
-![](./images/7ce1063d-f13d-4631-8956-8a97e0eaf48a-50_428_464_1008_88.jpg)
-Figure 15 Dirichlet problem in Exercise 42.
-
-![](./images/7ce1063d-f13d-4631-8956-8a97e0eaf48a-50_426_460_1650_89.jpg)
-Figure 16 Dirichlet problem in Exercise 43.
-
-In Exercises 35-36, by guessing find an analytic function $f$ such that the given function is the real or imaginary part of $f$. Using Theorem 3, determine where the given function is harmonic.
-35. $\frac{y}{x^{2}+y^{2}}$.
-36. $e^{2 x} \cos (2 y)$.
-37. (a) Plot the level curves of the harmonic function $u(x, y)=\frac{y}{x^{2}+y^{2}}$.
-(b) Find and plot the orthogonal trajectories.
-38. (a) Plot the level curves of the harmonic function $u(x, y)=\ln \left(x^{2}+y^{2}\right)$.
-(b) Find and plot the orthogonal trajectories.
-39. (a) For any integer $n$, show that $u(r, \theta)=r^{n} \cos (n \theta)$ and $v(r, \theta)=r^{n} \sin (n \theta)$ are harmonic on $\mathbb{C}$ if $n \geq 0$ and on $\mathbb{C} \backslash\{0\}$ if $n<0$.
-(b) Find the harmonic conjugates of $u$ and $v$. [Hint: Consider $f(z)=z^{n}$ in polar coordinates.]
-40. Translating and dilating a harmonic function. Suppose that $u$ is harmonic. Show that the following functions are also harmonic:
-(a) $\quad u(x-\alpha, y-\beta)$, where $\alpha$ and $\beta$ are real numbers;
-(b) $u(\alpha x, \alpha y)$, where $\alpha \neq 0$ is a real number.
-41. Harmonic functions independent of $y$. Suppose that $u(x, y)$ is a harmonic function whose values depend only on $x$ and not on $y$. Using Laplace's equation, show that $u(x, y)=a x+b$, where $a$ and $b$ are real constants.
-
-42 (a) Use Exercise 41 to solve the Dirichlet problem in the infinite vertical strip in Figure 15.
-(b) Determine and plot the isotherms and curves of heat flow.
-43. Solve the Dirichlet problem in Figure 16.
-44. Solve the Dirichlet problem in Figure 17.
-45. Solve the Dirichlet problem in Figure 18.
-46. Determine and plot the isotherms and curves of heat flow in Exercise 42.
-
-![](./images/7ce1063d-f13d-4631-8956-8a97e0eaf48a-50_426_463_1646_740.jpg)
-Figure 17 Dirichlet problem in Exercise 44.
-
-![](./images/7ce1063d-f13d-4631-8956-8a97e0eaf48a-50_420_454_1652_1389.jpg)
-Figure 18 Dirichlet problem in Exercise 45.
-
-![](./images/7ce1063d-f13d-4631-8956-8a97e0eaf48a-51_427_456_416_49.jpg)
-Figure 19 Dirichlet problem for Exercise 48.
-
-![](./images/7ce1063d-f13d-4631-8956-8a97e0eaf48a-51_434_462_1571_45.jpg)
-Figure 20 Dirichlet problem for Exercise 49.
-
-47. Solve the Dirichlet problem in the upper half-plane with boundary data on the $r$-axis given by
-
-$$
-u(x, 0)= \begin{cases}T_{1} & \text { if } a<x<b \\ T_{2} & \text { otherwise }\end{cases}
-$$
-
-where $a<b$ are fixed real numbers.
-48. Project Problem: Harmonic measures of two disjoint intervals. In this exercise, we generalize the result of Example 5 by solving the Dirichlet problem in the upper half-plane with boundary data.
-
-$$
-u(x, 0)= \begin{cases}T_{1} & \text { if } a<x<b \\ T_{2} & \text { if } c<x<d \\ 0 & \text { otherwise }\end{cases}
-$$
-
-where $a<b \leq c<d$ (Figure 19).
-(a) Show that if $u_{1}$ is a solution of the Dirichlet problem in the upper half-plane with boundary conditions
-
-$$
-u_{1}(x, 0)= \begin{cases}T_{1} & \text { if } a<x<b \\ 0 & \text { otherwise }\end{cases}
-$$
-
-and $u_{2}$ is a solution of the Dirichlet problem in the upper half-plane with boundary conditions
-
-$$
-u_{2}(x, 0)= \begin{cases}T_{2} & \text { if } c<x<d . \\ 0 & \text { otherwise },\end{cases}
-$$
-
-then the solution of the Dirichle problem in the upper half-plane with boundary data $u(x, 0)$ is $u(x, y)=u_{1}(x, y)+u_{2}(x, y)$.
-(b) Show that $n(x, y)=\left(T_{1} / \pi\right) \alpha_{1}(x, y)+\left(T_{2} / \pi\right) \alpha_{2}(x, y)$ where $\alpha_{1}(x, y)$, respectively, $\alpha_{2}(x, y)$, is the angle at ( $x, y$ ) subtended by the interval ( $a, b$ ), respectively. (c, d).
-49. (a) Solve the Dirichlet problem in Figure 20.
-(b) Plot the isotherms.
-50. Project Problem: Harmonic measures of several disjoint intervals. Generalize the result of Exercise 48 as follows. Suppose that $I_{1}, I_{2}, \ldots, I_{n}$ are disjoint open intervals on the $r$-axis, and $T_{1}, T_{2}, \ldots, T_{n}$ are real numbers. Consider the Dirichlet problem in the upper half-plane with boundary condition
-
-$$
-u(x, 0)= \begin{cases}T_{j} & \text { if } x \text { in } I_{j} \\ 0 & \text { otherwise } .\end{cases}
-$$
-
-Show that the solution is
-
-$$
-u(x, y)=\frac{1}{\pi} \sum_{j=1}^{n} T_{j} \alpha_{j}(x, y),
-$$
-
-where $\omega_{j}(x, y)$ is the angle at ( $x, y$ ) subtended by the interval $I_{j}$.
-51. Project Problem: Approximation of steady-state solutions. Consider the Dirichlet problem in the upper half-plane with boundary values $u(x, 0)=f(x)$
-$(-\infty<x<\infty)$, where $f(x)$ is an arbitrary function that represents the temperature of the points on the $x$-axis. In this exercise, we will show how we can use the result of Exercise 50 to approximate the solution for a given $f(x)$. The approach that we take has merit, since it can be used to obtain approximate numerical values for the steady-state temperature. Moreover, we will use it in Exercise 52 to justify the Poisson integral formula in the upper half-plane.
-
-To be able to compare our numerical approximation with the exact solution, let us take $f(x)=\left(1+x^{2}\right)^{-1},-\infty<x<\infty$. In this case, using properties of the Poisson integral, we have the solution
-
-$$
-u(x, y)=\frac{1+y}{x^{2}+(1+y)^{2}}
-$$
-
-(see Exercise 6, Section 7.5).
-(a) Pretend that we do not know the exact solution and proceed to find an approximate solution. The idea is to approximate $f(x)$ by a function that takes on constant values on disjoint intervals. Take the interval $(-5,5)$ and subdivide it into 40 smaller intervals of equal length, $\left(x_{j}, x_{j+1}\right), j=1,2, \ldots, 40$. Approximate $f$ on $\left(x_{j}, x_{j+1}\right)$ by $f\left(x_{j}\right)$, and by 0 outside the interval $(-5,5)$. Thus the boundary valucs are now replaced by
-
-$$
-u(x, 0)= \begin{cases}\frac{1}{1+x_{j}^{2}} & \text { if } x_{j}<x<x_{j+1} \\ 0 & \text { otherwise }\end{cases}
-$$
-
-Show that the solution is
-
-$$
-u(x, y)=\frac{1}{\pi} \sum_{j=1}^{40} \frac{1}{1+x_{j}^{2}} \alpha_{j}(x, y)
-$$
-
-where $\alpha_{j}(x, y)$ is the angle at $(x, y)$ subtended by the interval $\left(x_{j}, x_{j+1}\right)$.
-(b) With the help of a computer, evaluate your approximate solution at various points, $\left(x_{0}, y_{0}\right)$, in the upper half-plane and compare with the exact solution (13).
-52. Project Problem: From the harmonic measure to the Poisson integral formula. Consider the Dirichlet problem in the upper half-plane with boundary values $u(x, 0)=f(x),-\infty<x<\infty$, whose solution is given by the Poisson integral formula
-
-$$
-u(s, y)=\frac{y}{\pi} \int_{-\infty}^{\infty} \frac{f(x)}{(s-x)^{2}+y^{2}} d x, \quad-\infty<s<\infty, y>0
-$$
-
-Our goal in this exercise is to obtain this formula by using the numerical scheme of Exercise 51.
-(a) Based on the approach in Exercise 51, explain how you would derive the approximate solution
-
-$$
-u_{\mathrm{app}}(s, y)=\frac{1}{\pi} \sum_{j=1}^{n} f\left(x_{j}\right) \alpha_{j}(s, y)
-$$
-
-where $x_{j}$ are equally spaced points on the $x$-axis and $\alpha_{j}(s, y)$ is the angle at the point $(s, y)$ subtended by the interval $\left(x_{j}, x_{j+1}\right)$.
-(b) Show that
-
-$$
-u_{\text {app }}(s, y)=\frac{1}{\pi} \sum_{j=1}^{n} f\left(x_{j}\right)\left(\operatorname{Arg}\left(z-x_{j+1}\right)-\operatorname{Arg}\left(z-x_{j}\right)\right),
-$$
-
-where $z=s+i y$.
-(c) Use the mean value theorem to show that there exists a $\xi_{j}$ in the interval $\left(x_{j}, x_{j+1}\right)$ such that $\operatorname{Arg}\left(z-x_{j+1}\right)-\operatorname{Arg}\left(z-x_{j}\right)=\frac{y}{\left(s-\xi_{j}\right)^{2}+y^{2}} \Delta x$, where $\Delta x= x_{j+1}-x_{j}$.
-(d) Thus the approximate solution
-
-$$
-u_{\mathrm{app}}(s, y)=\frac{y}{\pi} \sum_{j=1}^{n} \frac{f\left(x_{j}\right)}{\left(s-\xi_{j}\right)^{2}+y^{2}} \Delta x .
-$$
-
-Let $\Delta x \rightarrow 0$ and explain why $u_{\text {app }}(s, y)$ should approach the Poisson integral (14). Hint: Interpret $u_{\text {app }}(s, y)$ as a Riemann sum that approximates the Poisson integral (14).]
-53. Complete the details of Example 2(f) to show that $\log z$ is analytic off its branch cut and then show that its derivative is $\frac{1}{z}$.
-54. Show that if $v$ is the harmonic conjugate of $u$, then $-u$ is the harmonic conjugate of $v$. [Hint: If $f=u+i v$ is analytic, what can you say about $i f$ ?]
+## Exercises 16.5
+
+
+> [!prompt|a1b76574-78cd-5a89-9a58-2426225708f3.local at=5fc124ef-8977-5cec-b69b-fd52c19b88f7] Shared exercise instructions
+> For the Dirichlet problems on unbounded regions below, seek the bounded harmonic extension. At discontinuities in the prescribed boundary data, impose the data on the open boundary pieces rather than requiring a continuous extension through the jump.
+
+
+> [!prompt|0ed01887-d63d-57d6-b977-bb699873bb76.local at=a87ccf78-5f17-549d-ba67-5376a755e396] Shared exercise instructions
+> Exercises 1-20 are intended as review of basic topics in complex numbers and functions. In these exercises, take $n=0,\pm1, \pm 2, \ldots$, and $z=x+i y$, unless otherwise specified.
+
+
+> [!prompt|cc1cdae0-8c76-51c0-9d1f-c656874fcfa3.local at=bb984027-df56-5440-ac56-117f14e6e66b] Shared exercise instructions
+> In Exercises 1-4, write the given complex number in the form $a+i b$, where $a$ and $b$ are real numbers.
+
+
+> [!exercise|6d544447-aa63-52ef-9f83-2b0a449bf367.local at=c812642b-c443-543f-bf20-dbf991128606] Exercise 1
+> (a) $(3+2 i)(2-i)$.
+> (b) $\quad(3-i) \overline{(2-i)}$.
+> (c) $\frac{1+i}{1-i}$.
+
+
+> [!exercise|e38559a9-06ee-536c-b953-4938ed2692cf.local at=68606261-b7be-5177-8fa2-69c1c7ed4755] Exercise 2
+> (a) $\quad i(2-i)^{2}$.
+> (b) $\overline{(3+i) \overline{(1-i)}}$.
+> (c) $\frac{2-i}{i}$.
+
+
+> [!exercise|426feb13-4477-5b20-8d20-5f5cda3aec84.local at=92c7b47e-7ab2-5da7-911d-cbc15ab2aca9] Exercise 3
+> (a) $\frac{1}{i}$.
+> (b) $(i)^{n}$.
+> (c) $(\bar{i})^{n}$.
+
+
+> [!exercise|d47a17c0-1337-51e3-b855-c4c06e8b534d.local at=a3080f19-737e-585a-bc04-fb5144bd3cbb] Exercise 4
+> (a) $\overline{\left(\frac{3+i}{1-i}\right)}$.
+> (b) $i^{2}+i^{20}+i^{200}+i^{202}$.
+> (c) $\sum_{n=0}^{1001} i^{n}$.
+
+
+> [!prompt|64098fe2-b711-5ba9-b369-19c2c99d7239.local at=313c0405-2e08-58d7-808f-68ec1e5da8d3] Shared exercise instructions
+> For the given complex number in Exercises 5-16, (a) find the principal value of the argument. (b) Compute the modulus. (c) Write the number in the form $re^{i\theta}$.
+
+
+> [!exercise|fb124318-c696-584a-b018-41ee23671b0c.local at=133d663a-6405-55dd-9048-da5d67a397a7] Exercise 5
+> $\quad i$.
+
+
+> [!exercise|f0a67cfa-d203-5e11-9d8b-4c603adfb316.local at=a71ef690-8467-5b97-b743-b89645f3c4b8] Exercise 6
+> $-i$.
+
+
+> [!exercise|80ac4e84-e78a-58a2-8606-d786d2373122.local at=3f8a3bed-f17f-5fd6-a3af-8194755b7174] Exercise 7
+> $\pi$.
+
+
+> [!exercise|91662db7-3b52-5f55-95e4-d50713551695.local at=2d5af8b6-f79b-558b-b843-b32c1a4f75dd] Exercise 8
+> $-\pi$.
+
+
+> [!exercise|87f4399f-71d9-5306-9c27-525287a4f242.local at=1f6259f7-d6ae-518a-a700-66adfd0cad8e] Exercise 9
+> $1+i$.
+
+
+> [!exercise|92facf11-2bbf-567a-be26-930ca9ae3a57.local at=916111b5-e674-5777-9de6-3ba54d5bbf8e] Exercise 10
+> $1-i$.
+
+
+> [!exercise|7e571921-9472-5787-b7d5-bb732caedbbc.local at=548b70aa-3509-541d-b12b-999ef7b38e4a] Exercise 11
+> $-1+i$.
+
+
+> [!exercise|2c7bfab7-a178-5328-a3f6-45a228157dda.local at=7662dc62-0507-5a38-a3fd-924413e34957] Exercise 12
+> $-1-i$.
+
+
+> [!exercise|44e4d33c-cea4-59b9-a655-113e48dceaf4.local at=ead7fb1b-df71-50b1-9397-3f3a4e156b64] Exercise 13
+> $(1+i)^{2}$.
+
+
+> [!exercise|88caf024-8a7b-5321-9b79-90823181b885.local at=23301502-e7bc-52fd-8e93-52c4bfc168ae] Exercise 14
+> $\frac{1}{1+i}$.
+
+
+> [!exercise|fbe519b9-06fb-550b-9b8b-c3137f82652e.local at=d4986a15-66b3-5960-ad10-50c27eb1f7ea] Exercise 15
+> $\cos\alpha+i\sin\alpha$.
+
+
+> [!exercise|158e58e1-6645-5827-959a-1632e0e5fe6e.local at=cc5a9146-bff4-5405-b7d3-d1eb0b771dec] Exercise 16
+> $\cos \alpha-i \sin \alpha$.
+
+
+> [!prompt|ece1c1e6-68f5-592c-b072-594df1579b1f.local at=d5d6995c-a7db-51d6-be06-21c87ede53ad] Shared exercise instructions
+> In Exercises 17-20, evaluate the function and write your answer in the form $a+i b$, where $a$ and $b$ are real numbers.
+
+
+> [!exercise|231881a5-2daf-53c6-9e4d-cee0d6b6ac3b.local at=75a5bb46-0f7f-5bd0-bd0b-5c31f912a3a1] Exercise 17
+> (a) $e^{2 i}$.
+> (b) $\sin i$.
+> (c) $\cos i$.
+> (d) $\log i$.
+
+
+> [!exercise|9a07ce76-0b35-5f76-af7a-b1e401456131.local at=f5218399-dd13-5abb-885e-eb66cdbd58b0] Exercise 18
+> (a) $e^{1-\pi i}$.
+> (b) $\sin (2+\pi i)$.
+> (c) $\log (-7)$.
+> (d) $\quad \log 1$.
+
+
+> [!exercise|e46c1a08-d7b4-5a32-893c-1990086ab75a.local at=018b3a1c-ba3d-5cc2-b1b4-ee317ba3e7c4] Exercise 19
+> (a) $e^{-\frac{\pi}{2} i}$.
+> (b) $e^{2-\frac{\pi}{2} i}$.
+> (c) $\quad \log (1-i)$.
+> (d) $\quad \log (1-i)^{2}$.
+
+
+> [!exercise|cbe9e591-e046-5805-9248-08dd3b8b9061.local at=90507db4-2db3-536b-b50f-282a5aadc49e] Exercise 20
+> (a) $e^{\log (1+5 \pi i)}$.
+> (b) $\quad \log \left(e^{1+5 \pi i}\right)$.
+> (c) $\log [(-1) \cdot i]$.
+> (d) $\log (-1)+\log i$.
+
+
+> [!exercise|dfb0f0fa-8fae-55fb-ac57-d5fde53123cf.local at=42f25b49-83c1-52c3-af31-8895c31257ee] Exercise 21
+> Give an example to show that $\log \left(z_{1} \cdot z_{2}\right)$ is not always equal to $\log \left(z_{1}\right)+ \log \left(z_{2}\right)$.
+
+
+> [!exercise|1d8a7680-42c6-5670-9a08-8cac03c02dfa.local at=01106237-681b-58a8-b1f2-08cab32e89ca] Exercise 22
+> Give an example to show that $\log \left(e^{z}\right)$ is not always equal to $z$. Find a necessary and sufficient condition on $z$ for the equality $\log \left(e^{z}\right)=z$ to hold.
+
+
+> [!prompt|5c2f2df5-fde3-53dd-914f-a1ac401dcc13.local at=ee09eeb5-2fff-56f5-9683-e85876743e0f] Shared exercise instructions
+> In Exercises 23-26, derive the given identity. Take $z=x+i y$.
+
+
+> [!exercise|61c5ef2e-1c82-57a2-9402-340077c4f91c.local at=a5ba2813-a26a-5893-b0ea-2576c5d19a0c] Exercise 23
+> (a) $\left|e^{z}\right|=e^{x}$.
+> (b) $\left|e^{i z}\right|=e^{-y}$.
+
+
+> [!exercise|cce25aaa-76ca-53a9-8a24-4e83ae720153.local at=ac4b3b87-04f8-5886-8d4a-c1b62fa757f9] Exercise 24
+> (a) $|\sin z|=\sqrt{\sin ^{2} x+\sinh ^{2} y}$.
+> (b) $|\cos z|=\sqrt{\cos ^{2} x+\sinh ^{2} y}$.
+
+
+> [!exercise|9cb011bd-8bc1-53fe-97c9-54fa306105ab.local at=93b127c6-5535-56c0-b689-baec3a3edee9] Exercise 25
+> (a) $\cos (i x)=\cosh x$.
+> (b) $\quad \sin (i x)=i \sinh x$.
+
+
+> [!exercise|49799b28-bb35-59ba-8d7f-594120b35ce5.local at=5f0b3339-aa17-5348-ba4b-e5552a0ad5be] Exercise 26
+> (a) $\overline{e^{z}}=e^{\bar{z}}$.
+> (b) $\overline{\sin z}=\sin \bar{z}$.
+
+
+> [!prompt|2d4efafa-ca15-5a91-82e5-02ef550ca027.local at=d1776e69-ec93-5b2e-b6f3-3496a066a400] Shared exercise instructions
+> In Exercises 27-30, use the Cauchy-Riemann equations to verify whether the given function is analytic. If it is, compute its derivative using $f'(z)=u_x+iv_x=v_y-iu_y$.
+
+
+> [!exercise|ec5831e4-b70c-5661-8dd4-50fcff6c2e7e.local at=d58625ef-f021-5250-8d40-1f2afd81e84c] Exercise 27
+> (a) $\sin z$.
+> (b) $\cos z$.
+
+
+> [!exercise|9cfea72d-afb2-5696-baa0-e77f0c27b6e8.local at=9723a872-0892-55dd-8362-1ee339353775] Exercise 28
+> (a) $e^{z}+z$.
+> (b) $z^{2}$.
+
+
+> [!exercise|99301b33-36f4-574d-993d-943038dd1018.local at=327a9e93-47d8-5c19-9d1a-194d893f9462] Exercise 29
+> (a) $\frac{x+i y}{x^{2}+y^{2}}$.
+> (b) $\frac{x-i y}{x^{2}+y^{2}}$.
+
+
+> [!exercise|ca727723-2b0a-5c15-8b5f-f222c40b0d89.local at=39dfc97d-454b-593c-b8be-f6ac6b27c389] Exercise 30
+> (a) $\bar{z}$.
+> (b) $\operatorname{Re} z$.
+
+
+> [!prompt|c8281334-d480-504a-843d-214d58e06cea.local at=b65ccfc8-db22-53be-9647-6608f37c3359] Shared exercise instructions
+> In Exercises 31-34, verify that the given function is harmonic, and then find a harmonic conjugate using the technique of Example 6.
+
+
+> [!exercise|e2f59469-0402-58ef-ad63-737f7740025e.local at=759c1203-fdb7-556c-972c-2fdd03e6c848] Exercise 31
+> $x^{2}-y^{2}+x y$.
+
+
+> [!exercise|6143f19d-b0db-567f-9455-5f4709977ed5.local at=9b66f4bc-c0c1-5b52-a118-754132b419ff] Exercise 32
+> $x^{2}-y^{2}-2 x+1$.
+
+
+> [!exercise|4c013e44-bde3-56fb-abd4-096dae9c9183.local at=7cafe239-7bd1-5f2d-98fc-aeec7f9ced3d] Exercise 33
+> $e^{x} \cos y$.
+
+
+> [!exercise|2d41e421-730a-5364-9495-0d0932617275.local at=dad3f49e-e84d-5b40-8514-089e37ab4cbb] Exercise 34
+> $\cos x \sinh y$.
+
+
+> [!prompt|4d6038fa-57e1-5d86-9de7-b339b8e466fe.local at=01525ff6-66f6-55bb-bbbe-c5fd5a4ca0c9] Shared exercise instructions
+> In Exercises 35-36, by guessing find an analytic function $f$ such that the given function is the real or imaginary part of $f$. Using Theorem 3, determine where the given function is harmonic.
+
+
+> [!exercise|2628d82d-1712-555c-ab9e-cb854979a00b.local at=3a1afc2e-a8bf-5b83-bb26-b7d862e50ee8] Exercise 35
+> $\frac{y}{x^{2}+y^{2}}$.
+
+
+> [!exercise|813b147c-e1a2-5ef8-843a-53dd7e9988ff.local at=3498325f-6713-52ad-85bd-243fad3b8acb] Exercise 36
+> $e^{2 x} \cos (2 y)$.
+
+
+> [!exercise|7d4a583c-31ae-58c1-b66a-55cd55ac0c1e.local at=bc5e2eac-064e-5232-9681-33a4c2985025] Exercise 37
+> (a) Plot the level curves of the harmonic function $u(x, y)=\frac{y}{x^{2}+y^{2}}$.
+> (b) Find and plot the orthogonal trajectories.
+
+
+> [!exercise|4d63c683-9067-5dba-ad41-1b5b3f8bfcc6.local at=a9a646b7-e21e-5fa1-991f-22adb830fff3] Exercise 38
+> (a) Plot the level curves of the harmonic function $u(x, y)=\ln \left(x^{2}+y^{2}\right)$.
+> (b) Find and plot the orthogonal trajectories.
+
+
+> [!exercise|dbd804d9-787e-530c-ae2e-60c7b31c5de2.local at=7f88e8f7-47f4-54f6-b7e9-d9f1d3a10e88] Exercise 39
+> (a) For any integer $n$, show that $u(r, \theta)=r^{n} \cos (n \theta)$ and $v(r, \theta)=r^{n} \sin (n \theta)$ are harmonic on $\mathbb{C}$ if $n \geq 0$ and on $\mathbb{C} \backslash\{0\}$ if $n<0$.
+> (b) Find the harmonic conjugates of $u$ and $v$. [Hint: Consider $f(z)=z^{n}$ in polar coordinates.]
+
+
+> [!exercise|c16d2954-d050-5aed-b9cf-c4dfcbfd0223.local at=d5bafed8-62fe-5686-a95f-a0886907d55c] Exercise 40
+> Translating and dilating a harmonic function. Suppose that $u$ is harmonic. Show that the following functions are also harmonic:
+> (a) $\quad u(x-\alpha, y-\beta)$, where $\alpha$ and $\beta$ are real numbers;
+> (b) $u(\alpha x, \alpha y)$, where $\alpha \neq 0$ is a real number.
+
+
+> [!exercise|8bb89d05-5bb1-5317-922a-44e12217cad2.local at=1a085da2-78c4-51b4-9faa-845de044678c] Exercise 41
+> Harmonic functions independent of $y$. Suppose that $u(x, y)$ is a harmonic function whose values depend only on $x$ and not on $y$. Using Laplace's equation, show that $u(x, y)=a x+b$, where $a$ and $b$ are real constants.
+
+
+```scientific-figure
+id: 285609cc-4b17-4edf-bc8b-157aa0068139
+numbered: false
+title: ""
+caption: Figure 15 Dirichlet problem in Exercise 42.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 16 Green's Functions and Conformal Mappings/images/7ce1063d-f13d-4631-8956-8a97e0eaf48a-50_428_464_1008_88.jpg
+    caption: ""
+```
+> [!exercise|b4885dda-cf9d-559b-a030-d5ae565a0951.local at=b117e406-f33c-5535-86a0-d6038df810ce] Exercise 42
+> (a) Use Exercise 41 to solve the Dirichlet problem in the infinite vertical strip in Figure 15.
+> (b) Determine and plot the isotherms and curves of heat flow.
+
+
+```scientific-figure
+id: 75eed045-f3cd-4ea9-8338-b9edcb4ed4f6
+numbered: false
+title: ""
+caption: Figure 16 Dirichlet problem in Exercise 43.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 16 Green's Functions and Conformal Mappings/images/7ce1063d-f13d-4631-8956-8a97e0eaf48a-50_426_460_1650_89.jpg
+    caption: ""
+```
+> [!exercise|bbf286bd-9439-50ef-8bb1-0cd5ed419820.local at=9e8e77e1-9e35-505e-887a-b200c52a72ea] Exercise 43
+> Solve the Dirichlet problem in Figure 16.
+
+
+```scientific-figure
+id: 51e0907d-4c35-404d-9db2-04ba3e118ab1
+numbered: false
+title: ""
+caption: Figure 17 Dirichlet problem in Exercise 44.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 16 Green's Functions and Conformal Mappings/images/7ce1063d-f13d-4631-8956-8a97e0eaf48a-50_426_463_1646_740.jpg
+    caption: ""
+```
+> [!exercise|ae05e94c-6c05-5946-a0a6-a38eeeffb901.local at=8844f76e-6a89-5be8-8c49-beb04c064904] Exercise 44
+> Solve the Dirichlet problem in Figure 17.
+
+
+```scientific-figure
+id: 14f658b1-1cb3-4d1b-a810-04f0c975f7bd
+numbered: false
+title: ""
+caption: Figure 18 Dirichlet problem in Exercise 45.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 16 Green's Functions and Conformal Mappings/images/7ce1063d-f13d-4631-8956-8a97e0eaf48a-50_420_454_1652_1389.jpg
+    caption: ""
+```
+> [!exercise|2c3d8b73-a30f-51eb-ae2c-84b8a64acecc.local at=146296a9-47be-5b7e-9e0d-ec0ea9c80beb] Exercise 45
+> Solve the Dirichlet problem in Figure 18.
+
+
+> [!exercise|6dd030b9-c175-5f1d-9e8c-68a4858f6950.local at=0e4dc839-cf85-51e8-a810-9f42e8c3bb62] Exercise 46
+> Determine and plot the isotherms and curves of heat flow in Exercise 42.
+
+
+> [!exercise|bbc06560-70ee-55b2-9f47-b7e80fa69de5.local at=47101947-bfad-5643-b083-ac8cdb421fe5] Exercise 47
+> Solve the Dirichlet problem in the upper half-plane with boundary data on the $x$-axis given by
+>
+> $$
+> u(x, 0)= \begin{cases}T_{1} & \text { if } a<x<b \\ T_{2} & \text { otherwise }\end{cases}
+> $$
+>
+> where $a<b$ are fixed real numbers.
+
+
+```scientific-figure
+id: 60188dfa-4528-45fa-b82e-0e5453e4575d
+numbered: false
+title: ""
+caption: Figure 19 Dirichlet problem for Exercise 48.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 16 Green's Functions and Conformal Mappings/images/7ce1063d-f13d-4631-8956-8a97e0eaf48a-51_427_456_416_49.jpg
+    caption: ""
+```
+> [!exercise|5ab24cc6-57b0-5a27-b1b3-732c9993474b.local at=7e853fd4-13fa-5fae-b75f-7bd8cec7b3ba] Exercise 48
+> Project Problem: Harmonic measures of two disjoint intervals. In this exercise, we generalize the result of Example 5 by solving the Dirichlet problem in the upper half-plane with boundary data.
+>
+> $$
+> u(x, 0)= \begin{cases}T_{1} & \text { if } a<x<b \\ T_{2} & \text { if } c<x<d \\ 0 & \text { otherwise }\end{cases}
+> $$
+>
+> where $a<b \leq c<d$ (Figure 19).
+> (a) Show that if $u_{1}$ is a solution of the Dirichlet problem in the upper half-plane with boundary conditions
+>
+> $$
+> u_{1}(x, 0)= \begin{cases}T_{1} & \text { if } a<x<b \\ 0 & \text { otherwise }\end{cases}
+> $$
+>
+> and $u_{2}$ is a solution of the Dirichlet problem in the upper half-plane with boundary conditions
+>
+> $$
+> u_{2}(x, 0)= \begin{cases}T_{2} & \text { if } c<x<d . \\ 0 & \text { otherwise },\end{cases}
+> $$
+>
+> then the solution of the Dirichlet problem in the upper half-plane with boundary data $u(x, 0)$ is $u(x, y)=u_{1}(x, y)+u_{2}(x, y)$.
+> (b) Show that $u(x,y)=\left(T_{1} / \pi\right) \alpha_{1}(x, y)+\left(T_{2} / \pi\right) \alpha_{2}(x, y)$ where $\alpha_{1}(x, y)$, respectively, $\alpha_{2}(x, y)$, is the angle at ( $x, y$ ) subtended by the interval ( $a, b$ ), respectively. (c, d).
+
+
+```scientific-figure
+id: c80ce7ea-3c66-4b6e-8ab9-c3e4a6281b97
+numbered: false
+title: ""
+caption: Figure 20 Dirichlet problem for Exercise 49.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 16 Green's Functions and Conformal Mappings/images/7ce1063d-f13d-4631-8956-8a97e0eaf48a-51_434_462_1571_45.jpg
+    caption: ""
+```
+> [!exercise|37b04b56-b82b-5c9d-b50e-c4264c897693.local at=97e5d25f-cae2-592c-ac3e-85f19b474fd8] Exercise 49
+> (a) Solve the Dirichlet problem in Figure 20.
+> (b) Plot the isotherms.
+
+
+> [!exercise|b4ee9b5c-3a79-58ce-8215-45eef21ed7ce.local at=16109f4c-158e-510a-9ec6-2591af55c6c8] Exercise 50
+> Project Problem: Harmonic measures of several disjoint intervals. Generalize the result of Exercise 48 as follows. Suppose that $I_{1}, I_{2}, \ldots, I_{n}$ are disjoint open intervals on the $x$-axis, and $T_{1}, T_{2}, \ldots, T_{n}$ are real numbers. Consider the Dirichlet problem in the upper half-plane with boundary condition
+>
+> $$
+> u(x, 0)= \begin{cases}T_{j} & \text { if } x \text { in } I_{j} \\ 0 & \text { otherwise } .\end{cases}
+> $$
+>
+> Show that the solution is
+>
+> $$
+> u(x, y)=\frac{1}{\pi} \sum_{j=1}^{n} T_{j} \alpha_{j}(x, y),
+> $$
+>
+> where $\alpha_j(x,y)$ is the angle at ( $x, y$ ) subtended by the interval $I_{j}$.
+
+
+> [!exercise|2abddce0-f11f-5547-944f-4b9b042870bd.local at=cd93f38b-5795-5f8f-bf3e-6bc15f007c90] Exercise 51
+> Project Problem: Approximation of steady-state solutions. Consider the Dirichlet problem in the upper half-plane with boundary values $u(x, 0)=f(x)$
+> $(-\infty<x<\infty)$, where $f(x)$ is an arbitrary function that represents the temperature of the points on the $x$-axis. In this exercise, we will show how we can use the result of Exercise 50 to approximate the solution for a given $f(x)$. The approach that we take has merit, since it can be used to obtain approximate numerical values for the steady-state temperature. Moreover, we will use it in Exercise 52 to justify the Poisson integral formula in the upper half-plane.
+>
+> To be able to compare our numerical approximation with the exact solution, let us take $f(x)=\left(1+x^{2}\right)^{-1},-\infty<x<\infty$. In this case, using properties of the Poisson integral, we have the solution
+>
+> $$
+> u(x, y)=\frac{1+y}{x^{2}+(1+y)^{2}}
+> $$
+>
+> (see Exercise 6, Section 8.5).
+> (a) Pretend that we do not know the exact solution and proceed to find an approximate solution. The idea is to approximate $f(x)$ by a function that takes on constant values on disjoint intervals. Take the interval $(-5,5)$ and subdivide it into 40 smaller intervals of equal length, $\left(x_{j}, x_{j+1}\right), j=1,2, \ldots, 40$. Approximate $f$ on $\left(x_{j}, x_{j+1}\right)$ by $f\left(x_{j}\right)$, and by 0 outside the interval $(-5,5)$. Thus the boundary values are now replaced by
+>
+> $$
+> u(x, 0)= \begin{cases}\frac{1}{1+x_{j}^{2}} & \text { if } x_{j}<x<x_{j+1} \\ 0 & \text { otherwise }\end{cases}
+> $$
+>
+> Show that the solution is
+>
+> $$
+> u(x, y)=\frac{1}{\pi} \sum_{j=1}^{40} \frac{1}{1+x_{j}^{2}} \alpha_{j}(x, y)
+> $$
+>
+> where $\alpha_{j}(x, y)$ is the angle at $(x, y)$ subtended by the interval $\left(x_{j}, x_{j+1}\right)$.
+> (b) With the help of a computer, evaluate your approximate solution at various points, $\left(x_{0}, y_{0}\right)$, in the upper half-plane and compare with the exact solution (13).
+
+*Printed equation label: (13).*
+
+
+> [!exercise|6e7cfa2c-6d27-57a1-a14f-90ade04d3d0a.local at=71a700a6-624d-5e66-ac6b-04ef5591d218] Exercise 52
+> Project Problem: From the harmonic measure to the Poisson integral formula. Consider the Dirichlet problem in the upper half-plane with boundary values $u(x, 0)=f(x),-\infty<x<\infty$, where $f$ is bounded and continuous, whose bounded harmonic solution is given by the Poisson integral formula
+>
+> $$
+> u(s, y)=\frac{y}{\pi} \int_{-\infty}^{\infty} \frac{f(x)}{(s-x)^{2}+y^{2}} d x, \quad-\infty<s<\infty, y>0
+> $$
+>
+> Our goal in this exercise is to obtain this formula by using the numerical scheme of Exercise 51.
+> (a) Based on the approach in Exercise 51, explain how you would derive the approximate solution
+>
+> $$
+> u_{\mathrm{app}}(s, y)=\frac{1}{\pi} \sum_{j=1}^{n} f\left(x_{j}\right) \alpha_{j}(s, y)
+> $$
+>
+> where $x_{j}$ are equally spaced points on the $x$-axis and $\alpha_{j}(s, y)$ is the angle at the point $(s, y)$ subtended by the interval $\left(x_{j}, x_{j+1}\right)$.
+> (b) Show that
+>
+> $$
+> u_{\text {app }}(s, y)=\frac{1}{\pi} \sum_{j=1}^{n} f\left(x_{j}\right)\left(\operatorname{Arg}\left(z-x_{j+1}\right)-\operatorname{Arg}\left(z-x_{j}\right)\right),
+> $$
+>
+> where $z=s+i y$.
+> (c) Use the mean value theorem to show that there exists a $\xi_{j}$ in the interval $\left(x_{j}, x_{j+1}\right)$ such that $\operatorname{Arg}\left(z-x_{j+1}\right)-\operatorname{Arg}\left(z-x_{j}\right)=\frac{y}{\left(s-\xi_{j}\right)^{2}+y^{2}} \Delta x$, where $\Delta x= x_{j+1}-x_{j}$.
+> (d) Thus the approximate solution
+>
+> $$
+> u_{\mathrm{app}}(s, y)=\frac{y}{\pi} \sum_{j=1}^{n} \frac{f\left(x_{j}\right)}{\left(s-\xi_{j}\right)^{2}+y^{2}} \Delta x .
+> $$
+>
+> First refine the mesh on a fixed finite interval, then let its endpoints tend to $-\infty$ and $+\infty$. Explain why $u_{\text {app }}(s, y)$ should approach the Poisson integral (14). [Hint: Interpret $u_{\text {app }}(s, y)$ as a Riemann sum that approximates the Poisson integral (14).]
+
+*Printed equation label: (14).*
+
+
+> [!exercise|d23ebf31-c6f9-57be-acdd-fe9b9511b973.local at=55ddf230-8bf2-5a23-ac50-cc6af331d08e] Exercise 53
+> Complete the details of Example 2(f) to show that $\log z$ is analytic off its branch cut and then show that its derivative is $\frac{1}{z}$.
+
+
+> [!exercise|75b5f8d9-c47b-568a-8aa2-d74d7195ae5e.local at=7198044b-7495-5cd0-8f4a-f6a2c772067e] Exercise 54
+> Show that if $v$ is the harmonic conjugate of $u$, then $-u$ is the harmonic conjugate of $v$. [Hint: If $f=u+i v$ is analytic, what can you say about $i f$ ?]

`````
