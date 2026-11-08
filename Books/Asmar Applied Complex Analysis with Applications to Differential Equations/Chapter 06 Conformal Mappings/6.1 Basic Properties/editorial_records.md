
# Editorial records

Reading note: 6.1 Basic Properties.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Callout 230: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Conformality at a Point with Nonzero Complex Derivative
> Suppose that $f$ is analytic at $z_0$ and $f^{\prime}\left(z_0\right) \neq 0$, then $f$ preserves angles and their orientation at $z_0$ (that is, it is conformal there).
````
### After

````text
> [!theorem] Conformal Property
> Suppose that $f$ is analytic at $z_0$ and $f^{\prime}\left(z_0\right) \neq 0$, then $f$ is conformal at $z_0$.
````

## 2. Callout 231: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Boundary Cluster Behavior of a One-to-One Analytic Mapping
> Let $f$ be analytic and one-to-one on a region $\Omega$, and put $D=f(\Omega)$. Boundaries in this statement are taken in the extended complex plane $\widehat{\mathbb C}$.
>
> If $z_n\in\Omega$, $z_n\to\alpha\in\partial\Omega$, and $f(z_n)\to\beta$ in $\widehat{\mathbb C}$, then $\beta\in\partial D$. Conversely, every $\beta\in\partial D$ is obtained as such a boundary cluster value for some $\alpha\in\partial\Omega$ and some sequence in $\Omega$.
````
### After

````text
> [!theorem] Boundary Behavior
> Suppose that $f$ is analytic and one-to-one in a region $\Omega$. With boundary values understood as cluster values in the extended complex plane, $f$ maps the boundary of $\Omega$ to the boundary of $f[\Omega]$, and this map is onto.
````

## 3. Callout 233: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Normalized Riemann Mapping Theorem
> Let $\Omega$ be a simply connected region in the complex plane other than the complex plane itself. Then there is a one-to-one analytic function $f$ that maps $\Omega$ onto the unit disk $|w|<1$. The mapping $f$ is unique if we specify that $f\left(z_0\right)=0$ and $f^{\prime}\left(z_0\right)>0$, for some $z_0$ in $\Omega$.
````
### After

````text
> [!theorem] Riemann Mapping Theorem
> Let $\Omega$ be a simply connected region in the complex plane other than the complex plane itself. Then there is a one-to-one analytic function $f$ that maps $\Omega$ onto the unit disk $|w|<1$. The mapping $f$ is unique if we specify that $f\left(z_0\right)=0$ and $f^{\prime}\left(z_0\right)>0$, for some $z_0$ in $\Omega$.
````

## 4. Move editorial commentary out of the reading note.

### Before

````text
*Editorial corrections: the boundary segment mapped into the interior has open endpoints; the sine preimage argument includes both alternatives.*
````
### After

````text

````

## 5. Move editorial commentary out of the reading note.

### Before

````text
*Editorial note: [clarified] The source’s “maps the boundary onto the boundary” is a statement about boundary limits, not an assertion that every univalent map has a single-valued continuous extension to its boundary. Infinity is included for unbounded regions.*
````
### After

````text

````

## Source-to-current comparison

Source: /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 06 Conformal Mappings/6.1 Basic Properties.md

This exact comparison preserves the full change evidence, including formatting, OCR corrections, restored source wording, and required standalone context. The entries above explain the recovery edits. The comparison is not a claim that every difference is a correction; component serialization, callout wrapping, and printed labels outside callouts are formatting.

`````diff
--- /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 06 Conformal Mappings/6.1 Basic Properties.md
+++ /Users/gradyclopton/ObsidianVaults/complex_analysis/Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 06 Conformal Mappings/6.1 Basic Properties.md
@@ -27,10 +27,18 @@
 Suppose that $\gamma$ is a smooth path parametrized by $z(t)=x(t)+i y(t)$, $a \leq t \leq b$. Write $\frac{d z}{d t}=z^{\prime}(t)=x^{\prime}(t)+i y^{\prime}(t)$. Let us also assume that $z^{\prime}(t) \neq 0$, as this will guarantee the existence of a tangent. The tangent line to the curve at $z(t)$ points in the direction of $z^{\prime}(t)$; we can characterize this direction by specifying $\arg z^{\prime}(t)$ (see _Figure 1_). 
 
 
-> [!figure] Figure 1
-> 
-> ![[Screenshot 2026-04-04 at 5.47.05 PM.png]]
-> Figure 1 The direction of the tangent line at $z(t)$ is given by $\arg z^{\prime}(t)$.
+```scientific-figure
+id: fa27a371-ec45-4aed-8756-fcaae80c1f45
+numbered: false
+title: ""
+caption: "**Figure 1.** The direction of the tangent line at $z(t)$ is given by $\\arg z^{\\prime}(t)$."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 06 Conformal Mappings/images/Screenshot 2026-04-04 at 5.47.05 PM.png
+    caption: ""
+```
 
 
 
@@ -40,10 +48,18 @@
 
 
 
-> [!figure] Figure 2
-> 
-> ![[Screenshot 2026-04-04 at 5.47.15 PM.png]]
-> Figure 2 The curves $\gamma_1$ and $\gamma_2$ intersect at angle $\alpha$.
+```scientific-figure
+id: d0f173d7-d0a5-4308-a43a-3d07814e9dc7
+numbered: false
+title: ""
+caption: "**Figure 2.** The curves $\\gamma_1$ and $\\gamma_2$ intersect at angle $\\alpha$."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 06 Conformal Mappings/images/Screenshot 2026-04-04 at 5.47.15 PM.png
+    caption: ""
+```
 
 
 
@@ -54,10 +70,18 @@
 
 
 
-> [!figure] Figure 3
-> 
-> ![[Screenshot 2026-04-04 at 5.47.23 PM.png]]
-> Figure 3 A linear mapping $f(z)=a z+b(a \neq 0)$ rotates by an angle arg $a$, dilates by a factor $|a|$, and translates by b. In particular, it preserves angles between curves.
+```scientific-figure
+id: 559b8ab6-2f24-43eb-bcdc-26638fd49cb6
+numbered: false
+title: ""
+caption: "**Figure 3.** A linear mapping $f(z)=a z+b(a \\neq 0)$ rotates by an angle arg $a$, dilates by a factor $|a|$, and translates by b. In particular, it preserves angles between curves."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 06 Conformal Mappings/images/Screenshot 2026-04-04 at 5.47.23 PM.png
+    caption: ""
+```
 
 
 
@@ -73,6 +97,7 @@
 
 
 
+<!-- Source label: Conformal Property -->
 > [!theorem] Conformal Property
 > Suppose that $f$ is analytic at $z_0$ and $f^{\prime}\left(z_0\right) \neq 0$, then $f$ is conformal at $z_0$.
 
@@ -96,12 +121,9 @@
 
 
 > [!exercise] EXAMPLE 1 Boundary points mapped to interior points
-> 
-> <span style="color:#ff0000; font-weight:bold">Exercise statement needed.</span>
-> 
-> 
-
-
+> For $f(z)=z^2$ on $\Omega=\{re^{i\theta}:1/2<r<1,-\pi<\theta<\pi\}$, determine $f(\Omega)$ and show that conformality in $\Omega$ does not force every boundary point to map to a boundary point.
+
+##### solution
 
 Consider $f(z)=z^2$ and $\Omega=\left\{z=r e^{i \theta}: \frac{1}{2}<r<1,-\pi<\theta<\pi\right\}$. Then $f$ is analytic and $f^{\prime}(z)=2 z \neq 0$ for all $z$ in $\Omega$. Hence $f(z)$ is conformal at each $z$ in $\Omega$.
 Since $z^2=r^2 e^{2 i \theta}$ it is easy to see that $f[\Omega]$ is the annulus
@@ -111,15 +133,22 @@
 $$
 
 
-It is also easy to see that the boundary points $z=x,-1 \leq x \leq-\frac{1}{2}$ are mapped to the interior points $w=u, \frac{1}{4} \leq u \leq 1$ (see _Figure 4_). Thus $f$ does not map the boundary of $\Omega$ to the boundary of $f[\Omega]$.
-
-
-
-> [!figure] Figure 4
-> 
-> ![[Screenshot 2026-04-04 at 5.52.56 PM.png]]
-> 
-> Figure 4 The function $f(z)= z^2$ is conformal in $\Omega$. It takes the interval $\left(-1,-\frac{1}{2}\right)$ on the boundary of $\Omega$ to the interval $\left(\frac{1}{4}, 1\right)$ in the interior of $f[\Omega]$. Thus $f$ does not map boundary points to boundary points.
+It is also easy to see that the boundary points $z=x,-1<x<-\frac{1}{2}$ are mapped to the interior points $w=u,\frac14<u<1$ (see _Figure 4_). Thus $f$ does not map the boundary of $\Omega$ to the boundary of $f[\Omega]$.
+
+
+
+```scientific-figure
+id: 441f9de2-b225-4174-a911-323ee7eba5c2
+numbered: false
+title: ""
+caption: "**Figure 4.** The function $f(z)= z^2$ is conformal in $\\Omega$. It takes the interval $\\left(-1,-\\frac{1}{2}\\right)$ on the boundary of $\\Omega$ to the interval $\\left(\\frac{1}{4}, 1\\right)$ in the interior of $f[\\Omega]$. Thus $f$ does not map boundary points to boundary points."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 06 Conformal Mappings/images/Screenshot 2026-04-04 at 5.52.56 PM.png
+    caption: ""
+```
 
 
 
@@ -128,8 +157,9 @@
 
 
 
+<!-- Source label: Boundary Behavior -->
 > [!theorem] Boundary Behavior
-> Suppose that $f$ is analytic and one-to-one in a region $\Omega$. Then $f$ maps the boundary of $\Omega$ to the boundary of $f[\Omega]$, and this map is onto.
+> Suppose that $f$ is analytic and one-to-one in a region $\Omega$. With boundary values understood as cluster values in the extended complex plane, $f$ maps the boundary of $\Omega$ to the boundary of $f[\Omega]$, and this map is onto.
 
 
 **Proof** We will prove that $f$ maps the boundary of $\Omega$ to the boundary of $f[\Omega]$. leaving the "onto" part for Exercise 20. Let $\left\{z_n\right\}$ be a sequence in $\Omega$ such that $f\left(z_n\right) \rightarrow \beta$, where $\beta$ is an interior point of $f[\Omega]$. Since $f$ is analytic and one-to-one. $f^{-1}$ exists and is analytic, and hence continuous. Thus
@@ -146,8 +176,9 @@
 If the conformal mapping can be extended to a continuous function on the boundary, the following version of Theorem 2 will be useful.
 
 
-> [!corollary]
-> Suppose that $f$ is analytic and one-to-one in a region $\Omega$. Let $\alpha$ be any point of the boundary of $\Omega$ such that $f$ is continuous at $\alpha$. Then $f(\alpha)$ is a point on the boundary of $f[\Omega]$.
+<!-- Source label:  -->
+> [!corollary] Boundary Images Under a Continuous Extension of a Univalent Map
+> Suppose that $f$ is analytic and one-to-one in a region $\Omega$. Let $\alpha$ be any point of the boundary of $\Omega$ such that $f$ has a finite continuous extension to $\alpha$ from $\Omega$. Then $f(\alpha)$ is a point on the boundary of $f[\Omega]$.
 
 
 **Proof** Let $\left\{z_n\right\}$ be a sequence in $\Omega$ converging to $\alpha$ on the boundary of $\Omega$. Since $f$ is continuous at $\alpha, f\left(z_n\right)$ converges to $f(\alpha)$. By Theorem $2, f(\alpha)$ is a boundary point of $f[\Omega]$.
@@ -158,16 +189,25 @@
 
 
 > [!exercise] EXAMPLE 2 Mapping of regions
-> 
-> <span style="color:#ff0000; font-weight:bold">Exercise statement needed</span>
-
-Let $f(z)=\sin z$ and $\Omega=\left\{z=x+i y:-\frac{\pi}{2}<x<\frac{\pi}{2}, y>0\right\}$. Thus $\Omega$ is the semi-infinite vertical strip shown in _Figure 5_. Since $\sin z_1=\sin z_2$ if and only if $z_1=z_2+2 k \pi$ ( $k$ an integer), we see that $f$ is one-to-one on $\Omega$. Also, $f$ is continuous on the boundary of $\Omega$.
-
-
-> [!figure] Figure 5
-> 
-> ![[Screenshot 2026-04-04 at 5.57.07 PM.png]]
-> Figure 5 The fact that the boundary of $f[\Omega]$ is the $u$ axis implies that $f[\Omega]$ is either the upper or lower halfplane. We decide which half it is by checking the image of one point. Note how the right angles at $z= \pm \frac{\pi}{2}$ got flattened by $f$ in the $w$-plane. The function $f$ is still conformal in $\Omega$, even though $f$ is not conformal at two points on the boundary.
+> Determine the image of $\Omega=\{x+iy:-\pi/2<x<\pi/2,\ y>0\}$ under $f(z)=\sin z$, using its boundary behavior and the image of an interior point.
+
+##### solution
+
+Let $f(z)=\sin z$ and $\Omega=\left\{z=x+i y:-\frac{\pi}{2}<x<\frac{\pi}{2}, y>0\right\}$. Thus $\Omega$ is the semi-infinite vertical strip shown in _Figure 5_. The equality $\sin z_1=\sin z_2$ holds exactly when $z_1=z_2+2k\pi$ or $z_1=\pi-z_2+2k\pi$, for an integer $k$. The strip’s width excludes the first possibility unless $k=0$, and positivity of both imaginary parts excludes the second. Thus $f$ is one-to-one on $\Omega$. Also, $f$ is continuous on the boundary of $\Omega$.
+
+
+```scientific-figure
+id: cbee1de4-c40b-4123-8b01-a5aff6166f50
+numbered: false
+title: ""
+caption: "**Figure 5.** The fact that the boundary of $f[\\Omega]$ is the $u$ axis implies that $f[\\Omega]$ is either the upper or lower halfplane. We decide which half it is by checking the image of one point. Note how the right angles at $z= \\pm \\frac{\\pi}{2}$ got flattened by $f$ in the $w$-plane. The function $f$ is still conformal in $\\Omega$, even though $f$ is not conformal at two points on the boundary."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 06 Conformal Mappings/images/Screenshot 2026-04-04 at 5.57.07 PM.png
+    caption: ""
+```
 
 
 We start by determining the image of the boundary. For $z=x$ real, we have $f(z)=\sin x$, and so $f$ maps the interval $-\frac{\pi}{2} \leq x \leq \frac{\pi}{2}$ onto the interval $[-1,1]$. For $z=\frac{\pi}{2}+i y$, we have $f(z)=\sin \left(\frac{\pi}{2}+i y\right)=\cosh y$, a real number (see (16), Section 1.6). So $f$ maps the vertical semi-infinite line $z=\frac{\pi}{2}+i y(y \geq 0)$ onto the semiinfinite interval $[1, \infty)$. For $z=-\frac{\pi}{2}+i y$, we have $f(z)=\sin \left(-\frac{\pi}{2}+i y\right)=-\cosh y$ (see (16), Section1.6). So $f$ maps the vertical semi-infinite line $z=-\frac{\pi}{2}+i y(y \geq 0)$ onto the semi-infinite interval $(-\infty,-1]$. Thus, $f$ maps the boundary of $\Omega$ to the real axis. According to Theorem 2, the image of the vertical strip has boundary the $u$-axis, so it is either the upper or the lower half-plane. Checking the value of $f$ at one point in $\Omega$, say $z=i$, we find $f(i)=\sin (i)=i \sinh (1)$, which is a point in the upper half. Thus the image of $\Omega$ is the upper half-plane.
@@ -189,10 +229,18 @@
 > (a) Show that $J(z)$ maps the upper unit semicircle $\sigma=\left\{z: z=e^{i \theta}, 0 \leq \theta \leq \pi\right\}$ onto the real interval $J|\sigma|=\mid-1,1]$, and the semi-infinite intervals $[1, \infty)$ and $(-\infty,-1]$ onto themselves.
 > (b) Show that the Joukowski function maps the set $\Omega=\left\{z:|z| \geq 1,0 \leq \operatorname{Arg}_{z \leq}\right. \pi\}$ onto the upper half-plane $\{w=u+i v: v \geq 0\}$ (see _Figure 6_). A more precise description of the Joukowski mapping is outlined in Exercise 17.
 > 
-> > [!figure] Figure 6
-> > 
-> > ![[Screenshot 2026-04-04 at 5.59.32 PM.png]]
-> > _Figure 6_ The Joukowski function maps the region $\Omega$ one-to-one onto the upper half-plane. It also maps the upper semi-circle of radius $R>1, x^2+y^2=R^2, y \geq 0$, to the upper semi-ellipse $\frac{(\mathrm{Rew})^2}{\left[\frac{1}{2}(R+\hbar)\right]^2}+\frac{(\operatorname{lm} w)^2}{\left[\frac{1}{2}(R-\hbar)\right]^2}=1$, Im $w \geq 0$. (See Exercise 17.)
+> ```scientific-figure
+> id: fd1edb8d-246a-4491-898c-24b72f2ae5eb
+> numbered: false
+> title: ""
+> caption: "**Figure 6.** The Joukowski function maps the region $\\Omega$ one-to-one onto the upper half-plane. It also maps the upper semi-circle of radius $R>1, x^2+y^2=R^2, y \\geq 0$, to the upper semi-ellipse $\\frac{(\\mathrm{Rew})^2}{\\left[\\frac{1}{2}(R+\\hbar)\\right]^2}+\\frac{(\\operatorname{lm} w)^2}{\\left[\\frac{1}{2}(R-\\hbar)\\right]^2}=1$, Im $w \\geq 0$. (See Exercise 17.)"
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 06 Conformal Mappings/images/Screenshot 2026-04-04 at 5.59.32 PM.png
+>     caption: ""
+> ```
 > 
 > 
 
@@ -232,6 +280,7 @@
 The following famous theorem of Riemann tells us that any simply connected region of the complex plane other than the plane itself is conformally equivalent to the open unit disk.
 
 
+<!-- Source label: Riemann Mapping Theorem -->
 > [!theorem] Riemann Mapping Theorem
 > Let $\Omega$ be a simply connected region in the complex plane other than the complex plane itself. Then there is a one-to-one analytic function $f$ that maps $\Omega$ onto the unit disk $|w|<1$. The mapping $f$ is unique if we specify that $f\left(z_0\right)=0$ and $f^{\prime}\left(z_0\right)>0$, for some $z_0$ in $\Omega$.
 
@@ -242,10 +291,18 @@
 Combined with the Poisson integral formula, which solves the Dirichlet problem with arbitrary boundary data on the disk, the Riemann mapping theorem implies that we can at least theoretically solve the Dirichlet problem on any simply connected region $\Omega$. As illustrated in _Figure 7_, it suffices to conformally map $\Omega$ in a one-to-one way onto the unit disk. This gives rise to a new boundary value problem on the disk, which can be solved using the Poisson formula. 
 
 
-> [!figure] Figure 7
-> 
-> ![[Screenshot 2026-04-04 at 6.02.22 PM.png]]
-> Figure 7 A one-to-one conformal mapping $f$ of $\Omega$ onto the unit disk $D=f[\Omega]$ takes boundary to boundary and preserves Laplace's equation. It transforms a Dirichlet problem on $\Omega$ into a Dirichlet problem on $D$, which can be solved using the Poisson forunula. The solution in $\Omega$ is then $u(z)=U(f(z))$.
+```scientific-figure
+id: 2c5ad821-cf2e-42be-99fa-1ff3700983f3
+numbered: false
+title: ""
+caption: "**Figure 7.** A one-to-one conformal mapping $f$ of $\\Omega$ onto the unit disk $D=f[\\Omega]$ takes boundary to boundary and preserves Laplace's equation. It transforms a Dirichlet problem on $\\Omega$ into a Dirichlet problem on $D$, which can be solved using the Poisson forunula. The solution in $\\Omega$ is then $u(z)=U(f(z))$."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 06 Conformal Mappings/images/Screenshot 2026-04-04 at 6.02.22 PM.png
+    caption: ""
+```
 
 
 The solution of the original problem is then obtained by composing the solution on the disk with the conformal mapping. As simple and elegant as it is, this approach has its limitations. Even though we have several powerful tools, such as Fourier series and techniques for evaluating integrals using residues, our experience with the Poisson formula tells us that this formula is not easy to compute in general. Even more difficult is the actual construction of the conformal mapping from $\Omega$ onto the unit disk. While the Riemann mapping guarantees its existence, it gives no clue as to how to construct it.
@@ -327,3 +384,4 @@
 > [!exercise]
 > 21. Let $\Omega$ be the slit plane, $\mathbb{C} \backslash\{z: z \leq 0\}$, and $f(z)=\log z$. Show that the sequence $z_n=-1+i \frac{(-1)^n}{n}(n=1,2, \ldots)$ converges to -1 on the boundary of $\Omega$ and yet $f\left(z_n\right)$ does not converge.
 
+

`````
