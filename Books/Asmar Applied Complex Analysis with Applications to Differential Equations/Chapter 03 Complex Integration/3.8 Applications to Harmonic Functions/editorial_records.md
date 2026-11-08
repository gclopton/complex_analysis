
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

## Source-to-current comparison

Source: /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 03 Complex Integration/3.8 Applications to Harmonic Functions.md

This exact comparison preserves the full change evidence, including formatting, OCR corrections, restored source wording, and required standalone context. The entries above explain the recovery edits. The comparison is not a claim that every difference is a correction; component serialization, callout wrapping, and printed labels outside callouts are formatting.

`````diff
--- /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 03 Complex Integration/3.8 Applications to Harmonic Functions.md
+++ /Users/gradyclopton/ObsidianVaults/complex_analysis/Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/3.8 Applications to Harmonic Functions.md
@@ -28,7 +28,8 @@
 
 
 
-> [!lemma] Lemma 1: Conjugate gradient
+<!-- Source label: Lemma 1: Conjugate gradient -->
+> [!lemma] Conjugate gradient
 > Suppose that $u$ is harmonic on a region $\Omega$. Let $\phi=u_{x}-i u_{y}$. Then $\phi$ is analytic on $\Omega$. The function $\phi$ is called the conjugate gradient of $u$.
 
 
@@ -62,10 +63,18 @@
 $$
 
 
-> [!figure] Figure 1
-> 
-> ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-088_398_501_1387_103.jpg)
-> Figure 1
+```scientific-figure
+id: 9724ad0a-444e-4d2e-8dbd-bb8a1fd7745b
+numbered: false
+title: ""
+caption: "**Figure 1.**"
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-088_398_501_1387_103.jpg
+    caption: ""
+```
 
 
 From this, it is easy to see that $u$ is the real part of the function
@@ -101,7 +110,8 @@
 
 Using the conjugate gradient $\phi=u_{x}-i u_{y}$, we can express any partial derivative of $u$ as the real or imaginary part of an analytic function, namely a derivative of $\phi$. For example, to get $u_{x x x}$, differentiate $\phi$ with respect to $x$ twice and get $\phi^{\prime \prime}=u_{x x x}-i u_{y x x}$. (Note that since the derivatives of $\phi$ exist, we can obtain them by differentiating with respect to any one of the variables $x, y$, or $z$. This was done in the proof of the CauchyRiemann equations.) Since $\phi$ is analytic, all its higher-order derivatives are analytic (Corollary 1, Section 3.6), and so $u_{x x x}$ and $u_{y x x}$ are both harmonic by Theorem 1, Section 2.5. We can carry these ideas further and arrive at the following useful result.
 
-> [!corollary] Corollary 1
+<!-- Source label: Corollary 1 -->
+> [!corollary] Infinite Differentiability of Harmonic Functions
 > Suppose that $u$ is harmonic on a region $\Omega$. Then $u$ has continuous partial derivatives of all order in $\Omega$.
 
 
@@ -112,10 +122,18 @@
 
 
 
-> [!figure] Figure 2
-> 
-> ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-089_477_520_1120_56.jpg)
-> Figure 2
+```scientific-figure
+id: 54e16fe6-8e77-485b-960c-65a9020ff930
+numbered: false
+title: ""
+caption: "**Figure 2.**"
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-089_477_520_1120_56.jpg
+    caption: ""
+```
 
 
 Our next result guarantees the existence of a harmonic conjugate if the region is simply connected.
@@ -123,13 +141,14 @@
 
 
 
-> [!theorem] Theorem 1: Harmonic Conjugate
+<!-- Source label: Theorem 1: Harmonic Conjugate -->
+> [!theorem] Harmonic Conjugate
 > Suppose that $u$ is harmonic on a simply connected region $\Omega$. Then $u$ has a harmonic conjugate in $\Omega$ given up to an additive constant by
-> 
+>
 > $$
 > v(z)=\int_{z_{0}}^{z}-u_{y} d x+u_{x} d y \quad\left(z_{0} \text { fixed in } \Omega\right)
 > $$
-> 
+>
 > where the integral is independent of path.
 
 
@@ -167,27 +186,35 @@
 Keeping in mind the example of the harmonic function $\ln |z|$ with no harmonic conjugate in the punctured plane $\mathbb{C} \backslash\{0\}$, we see that simple connectedness is a crucial property in Theorem 1, and the result is not true on arbitrary regions. What can we say on arbitrary regions? Suppose that $u$ is harmonic on a region $\Omega$ and let $z_{0}$ be in $\Omega$. Since $\Omega$ is open, we can find an open disk $B_{R}\left(z_{0}\right)$ in $\Omega$. Since $B_{R}\left(z_{0}\right)$ is simply connected, $u$ has a harmonic conjugate in $B_{R}\left(z_{0}\right)$. This means that Theorem 1 holds locally in $\Omega$ (_Figure 3_). This is a very useful fact that we record separately.
 
 
-> [!figure] Figure 3
-> 
-> ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-090_547_519_760_94.jpg)
-> Figure 3 Local existence of the harmonic conjugate.
-
-
-
-
-> [!corollary] Corollary 2
+```scientific-figure
+id: 1f344ac4-9398-4a27-bddf-fe100648f23e
+numbered: false
+title: ""
+caption: "**Figure 3.** Local existence of the harmonic conjugate."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-090_547_519_760_94.jpg
+    caption: ""
+```
+
+
+
+
+<!-- Source label: Corollary 2 -->
+> [!corollary] Local Existence of Harmonic Conjugates
 > Suppose that $u$ is harmonic on a region $\Omega$. Then $u$ admits a harmonic conjugate locally in $\Omega$.
 
 Using the local existence of a harmonic conjugate, we obtain the mean value property of harmonic functions from the corresponding property for analytic functions.
 
+<!-- Source label: 3: Gauss's Mean Value Property -->
 > [!corollary] 3: Gauss's Mean Value Property
 > Suppose that $u$ is harmonic on a region $\Omega$, then $u$ satisfies the mean value property, in the following sense. If $z$ is in $\Omega$, and the closed disk $S_{r}(z)$ ( $r>0$ ) is contained in $\Omega$, then
-> 
+>
 > $$
 > u(z)=\frac{1}{2 \pi} \int_{0}^{2 \pi} u\left(z+r e^{i t}\right) d t
 > $$
-> 
-> 
 
 
 **Proof** Let $B$ be an open disk in $\Omega$ containing the closed disk $S_{r}\left(z_{0}\right)$. Since $B$ is simply connected, $u$ admits a harmonic conjugate $v$ in $B$. So $f=u+i v$ is analytic in $B$. By the mean value property of analytic functions ((4), Section 3.7), we have
@@ -214,7 +241,8 @@
 
 
 
-> [!theorem] Theorem 2: Maximum-Minimum Principle
+<!-- Source label: Theorem 2: Maximum-Minimum Principle -->
+> [!theorem] Maximum-Minimum Principle
 > Suppose that $u$ is a harmonic function on a region $\Omega$. If $u$ attains a maximum
 > or a minimum in $\Omega$, then $u$ is constant in $\Omega$.
 
@@ -230,10 +258,18 @@
 
 
 
-> [!figure] Figure 4
-> 
-> ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-091_450_419_1097_53.jpg)
-> Figure 4
+```scientific-figure
+id: d1abcd1b-336d-48ef-80ce-d00fe831f77b
+numbered: false
+title: ""
+caption: "**Figure 4.**"
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-091_450_419_1097_53.jpg
+    caption: ""
+```
 
 
 
@@ -247,18 +283,21 @@
 
 The following corollaries of Theorem 2 are similar to results that we proved regarding the modulus of an analytic function. We relegate their proofs to the exercises.
 
-> [!corollary] Corollary 4
-> Suppose $\Omega$ is a bounded region, and $u$ is harmonic on $\Omega$ and continuous on the boundary of $\Omega$. Then
+<!-- Source label: Corollary 4 -->
+> [!corollary] Boundary Extrema of Harmonic Functions on Bounded Regions
+> Suppose $\Omega$ is a bounded region, and $u$ is harmonic on $\Omega$ and continuous on the closure $\overline{\Omega}$. Then
 > (i) $u$ attains its maximum $M$ and minimum $m$ on the boundary of $\Omega$, and
 > (ii) either $u$ is constant or $m<u<M$ for all points in $\Omega$.
 
 
-> [!corollary] Corollary 5
-> Suppose $\Omega$ is a bounded region, and $u$ is harmonic on $\Omega$ and continuous on the boundary of $\Omega$. If $u$ is constant on the boundary of $\Omega$, then $u$ is constant in $\Omega$.
-
-
-> [!corollary] Corollary 6
-> Suppose $\Omega$ is a bounded region, and $u_{1}$ and $u_{2}$ are harmonic on $\Omega$ and continuous on the boundary of $\Omega$. If $u_{1}=u_{2}$ on the boundary of $\Omega$, then $u_{1}=u_{2}$ in $\Omega$.
+<!-- Source label: Corollary 5 -->
+> [!corollary] Constant Boundary Values Determine a Constant Harmonic Function
+> Suppose $\Omega$ is a bounded region, and $u$ is harmonic on $\Omega$ and continuous on the closure $\overline{\Omega}$. If $u$ is constant on the boundary of $\Omega$, then $u$ is constant in $\Omega$.
+
+
+<!-- Source label: Corollary 6 -->
+> [!corollary] Uniqueness of the Harmonic Dirichlet Problem on a Bounded Region
+> Suppose $\Omega$ is a bounded region, and $u_{1}$ and $u_{2}$ are harmonic on $\Omega$ and continuous on the closure $\overline{\Omega}$. If $u_{1}=u_{2}$ on the boundary of $\Omega$, then $u_{1}=u_{2}$ in $\Omega$.
 
 
 
@@ -278,10 +317,18 @@
 We focus now on some applications of the theory of harmonic functions to the solution of Dirichlet problems on a disk. To simplify the presentation, we will work on a disk centered at the origin with radius $R>0$. In polar coordinates, the problem is stated as follows. Suppose we are given a piecewise continuous function $f(\theta), 0<\theta \leq 2 \pi$ that represents boundary data on the points $R e^{i \theta}$ (_Figure 5_). 
 
 
-> [!figure] Figure 5
-> 
-> ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-092_467_521_730_88.jpg)
-> Figure 5 $f(\theta)$ gives the boundary data: $f(\theta)= u(R, \theta)$.
+```scientific-figure
+id: 9dc3fd3e-6b39-4b1e-9c83-879627c1d2b8
+numbered: false
+title: ""
+caption: "**Figure 5.** $f(\\theta)$ gives the boundary data: $f(\\theta)= u(R, \\theta)$."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-092_467_521_730_88.jpg
+    caption: ""
+```
 
 
 
@@ -299,10 +346,18 @@
 
 
 
-> [!figure] Figure 6
-> 
-> ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-092_525_525_1456_90.jpg)
-> Figure 6 A Dirichlet problem on a disk.
+```scientific-figure
+id: d55c0076-27dd-4f36-9a6c-0197ec2cc450
+numbered: false
+title: ""
+caption: "**Figure 6.** A Dirichlet problem on a disk."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-092_525_525_1456_90.jpg
+    caption: ""
+```
 
 
 
@@ -321,13 +376,13 @@
 This is a linear combination of functions from the $2 \pi$-periodic trigonometric system: $1, \cos x, \cos 2 x, \ldots, \sin x, \sin 2 x, \ldots$.
 
 
-> [!proposition] Proposition 1: A Dirichlet Problem on the Disk
-> The solution of the Dirichlet problem on the disk $|z| \leq R$ with boundary condition (6) is
-> 
+<!-- Source label: Proposition 1: A Dirichlet Problem on the Disk -->
+> [!proposition] A Dirichlet Problem on the Disk
+> Let $R>0$, let $N$ be a nonnegative integer, and let $a_0,a_n,b_n$ be real coefficients. The unique harmonic function in $|z|<R$, continuous on the closed disk, with boundary values $u(R,\theta)=a_0+\sum_{n=1}^{N}(a_n\cos n\theta+b_n\sin n\theta)$ is, for $0\leq r\leq R$,
+>
 > $$
 > u(r, \theta)=a_{0}+\sum_{n=1}^{N}\left(\frac{r}{R}\right)^{n}\left(a_{n} \cos n \theta+b_{n} \sin n \theta\right)
 > $$
-> 
 
 **Proof** For $|z|<R$, write $z=r e^{i \theta}=r(\cos \theta+i \sin \theta)$. The function $f(z)=z^{n}= r^{n}(\cos n \theta+i \sin n \theta)$ is analytic on the disk $|z| \leq R$. Hence its real and imaginary parts are harmonic (Theorem 1, Section 2.5). This shows that the functions $1, r \cos \theta, r^{2} \cos 2 \theta, \ldots, r \sin \theta, r^{2} \sin 2 \theta, \ldots$ are harmonic on the disk $|z| \leq R$. B $y$ Proposition 1, Section 2.5, any linear combination of such functions is also harmonic on the unit disk, and so (7) is harmonic. Setting $r=R$ in (7), we see that $u(R, \theta)=f(\theta)$, where $f$ is as in (6). Hence (7) is the solution of the Dirichlet problem with boundary data (6).
 
@@ -336,10 +391,18 @@
 
 Each term in the finite sum (7) is a constant multiple of the harmonic functions $1, r \cos \theta, r^{2} \cos 2 \theta, \ldots, r \sin \theta, r^{2} \sin 2 \theta, \ldots$ With the exception of the constant function 1 , the graphs of these functions over the disk $|z|<R$ are saddle-shaped. This confirms our expectation that the maxima and minima of these functions must occur on the boundary (see _Figure 7_).
 
-> [!figure] Figure 7
-> 
-> ![700](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-093_663_1998_890_64.jpg)
-> Figure 7 The saddle-shaped graphs of the harmonic functions $r \cos \theta, r^{2} \cos 2 \theta, r^{3} \cos 3 \theta, r^{4} \cos 4 \theta$ seem to confirm the important property that the maximum and minimum of a harmonic function occur on the boundary of the (bounded) region.
+```scientific-figure
+id: e801df77-718c-47b4-a5d1-c622e9db2eb7
+numbered: false
+title: ""
+caption: "**Figure 7.** The saddle-shaped graphs of the harmonic functions $r \\cos \\theta, r^{2} \\cos 2 \\theta, r^{3} \\cos 3 \\theta, r^{4} \\cos 4 \\theta$ seem to confirm the important property that the maximum and minimum of a harmonic function occur on the boundary of the (bounded) region."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-093_663_1998_890_64.jpg
+    caption: ""
+```
 
 
 
@@ -350,30 +413,56 @@
 > (b) Describe the isotherms and lines of heat flow.
 > 
 > 
-> > [!figure] Figure 8
-> > 
-> > ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-093_498_542_1746_68.jpg)
-> > Figure 8 The boundary function, as a function of $\theta$.
-> 
-> 
-
-**Solution** (a) To find the steady-state temperature, we must solve the Dirichlet problem with boundary data given by $f(\theta)$. According to (7), the solution is $u(r, \theta)=50-50 r \cos \theta, 0 \leq r<1$. This is a harmonic function, which is equal to $f(\theta)$ when $r=1$ (_Figure 9_).
-
-
-> [!figure] Figure 9
-> 
-> ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-094_587_487_552_640.jpg)
-> Figure 9
+> ```scientific-figure
+> id: e7513d80-91fb-49bd-bf98-9944fb71b168
+> numbered: false
+> title: ""
+> caption: "**Figure 8.** The boundary function, as a function of $\\theta$."
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-093_498_542_1746_68.jpg
+>     caption: ""
+> ```
+> 
+> 
+
+##### solution
+
+(a) To find the steady-state temperature, we must solve the Dirichlet problem with boundary data given by $f(\theta)$. According to (7), the solution is $u(r, \theta)=50-50 r \cos \theta, 0 \leq r<1$. This is a harmonic function, which is equal to $f(\theta)$ when $r=1$ (_Figure 9_).
+
+
+```scientific-figure
+id: 4dd082d4-fdc4-42f3-be25-988b34522a25
+numbered: false
+title: ""
+caption: "**Figure 9.**"
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-094_587_487_552_640.jpg
+    caption: ""
+```
 
 
 (b) Since the temperature on the boundary varies between 0 and 100 , by the maximum-minimum principle for harmonic functions, the temperature inside the plate will vary between these two limits. To find the isotherms, let $0<T<100$ and solve the equation $u(r, \theta)=T$ or $50-50 r \cos \theta=T$. Using $x=r \cos \theta$, the equation
 
 In _Figure 9_, we show the solution of the Dirichlet problem. Note how on the boundary the values of this solution coincide with the values of the boundary function. In _Figure 10_, we illustrate the isotherms and lines of heat flow. The orthogonality of these two families of curves is obvious in this case.
 
-> [!figure] Figure 10
-> 
-> ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-094_396_404_741_1338.jpg)
-> Figure 10
+```scientific-figure
+id: de01d847-1902-40a7-9001-0f7848fa903a
+numbered: false
+title: ""
+caption: "**Figure 10.**"
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-094_396_404_741_1338.jpg
+    caption: ""
+```
 
 becomes $50-50 x=T$ or $x=\frac{50-T}{50}$. Thus the isotherms are the intersections with the unit disk of the vertical lines $x=\frac{50-T}{50}$. The isotherms vary between $x=1$ and $x=-1$ as $T$ varies between 0 and 100 . We know from Section 2.5 that heat flows along the curves that are orthogonal to the isotherms. In this case, it is easy to sox that heat flows inside the unit disk in the direction of the horizontal lines $y=b$ (_Figure 10_).
 
@@ -456,22 +545,24 @@
 
 and so from (10) (with the variable $s$ replaced by $\phi$ ) we obtain the alternative Poisson integral formula
 
-> [!equation]
-> 
+<!-- Source label:  -->
+> [!equation] Poisson Integral Representation of a Harmonic Function on a Disk
+> Let $R>0$ and let $u$ be harmonic in $|z|<R$ and continuous on the closed disk. For $0\leq r<R$,
+>
 > $$
 > u\left(r e^{i \theta}\right)=\frac{R^{2}-r^{2}}{2 \pi} \int_{0}^{2 \pi} \frac{u\left(R e^{i \phi}\right)}{R^{2}-2 r R \cos (\theta-\phi)+r^{2}} d \phi
 > $$
-> 
 
 In deriving (11), we were given a harmonic function $u(z)$ in a region containing $S_{R}(0)$. The importance of (11) is that it can be used to construct $u(z)$ inside the disk $B_{R}(0)$, when only its (piecewise continuous) values on the circle $C_{R}(0)$ are known. More precisely, we have the following result.
 
 
 
 
-> [!theorem] Theorem 3: Poisson Integral Formula
-> Consider the Dirichlet problem (4) on the disk $|z| \leq R$, with boundary conditions (5), where $f(\theta)$ is piecewise continuous for $\theta$ in $[0,2 \pi]$. Then the solution exists and is given by the Poisson integral formula
->  $$u(r, \theta)=\frac{R^{2}-r^{2}}{2 \pi} \int_{0}^{2 \pi} \frac{f(\phi)}{R^{2}-2 r R \cos (\theta-\phi)+r^{2}} d \phi \quad(0 \leq r<R). \tag{12}$$
-> 
+<!-- Source label: Theorem 3: Poisson Integral Formula -->
+> [!theorem] Poisson Integral Formula
+> Let $R>0$ and let $f$ be a real-valued, $2\pi$-periodic, piecewise continuous function. Its harmonic extension to the disk $|z|<R$ is given by the Poisson integral
+>  $$u(r, \theta)=\frac{R^{2}-r^{2}}{2 \pi} \int_{0}^{2 \pi} \frac{f(\phi)}{R^{2}-2 r R \cos (\theta-\phi)+r^{2}} d \phi \quad(0 \leq r<R). $$
+>
 > More precisely, $u(r, \theta)$ is harmonic in the open disk $|z|<R$ and tends to $f(\theta)$ as $r \uparrow R$ at all points of continuity of $f$.
 
 
@@ -491,14 +582,14 @@
 
 
 
-> [!corollary] Corollary 7: Mean Value Propery
-> Suppose that $u\left(r e^{i \phi}\right)$ is harmonic for $0 \leq r<R$ and $0 \leq \phi \leq 2 \pi$, and $u\left(R e^{i \phi}\right)=f(\phi)$, where $f$ is piecewise continuous on the boundary. Then
-> 
+<!-- Source label: Corollary 7: Mean Value Propery -->
+> [!corollary] Mean Value Property
+> Let $R>0$, and let $u$ be the Poisson extension of the $2\pi$-periodic boundary function $f$. Suppose that $u\left(r e^{i \phi}\right)$ is harmonic for $0 \leq r<R$ and $0 \leq \phi \leq 2 \pi$, and $u\left(R e^{i \phi}\right)=f(\phi)$, where $f$ is piecewise continuous on the boundary. Then
+>
 > $$
 > u(0)=\frac{1}{2 \pi} \int_{0}^{2 \pi} f(\phi) d \phi
 > $$
-> 
-> 
+
 
 # Exercises 3.8
 
@@ -558,10 +649,18 @@
 > In problems 13-16, solve the Dirichlet problem (4)-(5) for the given boundary function $f(\theta)$ on the disk with center at the origin and given radius $R>0$ (_Figure 11_).
 > 
 > 
-> > [!figure] Figure 11
-> > 
-> > ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-097_523_542_1851_47.jpg)
-> > Figure 11 For Exercises 1316.
+> ```scientific-figure
+> id: f07689a9-9a21-4be9-890a-7a30f497afa8
+> numbered: false
+> title: ""
+> caption: "**Figure 11.** For Exercises 1316."
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-097_523_542_1851_47.jpg
+>     caption: ""
+> ```
 > 
 > 
 > 13. $f(\theta)=1-\cos \theta+\sin 2 \theta, R=1$.
@@ -770,4 +869,4 @@
 > As $r \uparrow R$, the last integral tends to 0 (Exercise 23(a). Since $\epsilon$ is arbitrary, it follows that $|u(r, \theta)-f(\theta)|$ tends to 0 independently of $\theta$, as $r \uparrow R$.
 > 
 > We have effectively shown that $u(r, \theta)$, the Poisson integral of $f$, converges uniformly to $f(\theta)$ as $r \uparrow R$, if (and only if) $f$ is continuous. The concept of uniform convergence is extremely important in the theory of analytic and harmonic functions. We will study it in great detail in the following chapter.
-> +> 

`````
