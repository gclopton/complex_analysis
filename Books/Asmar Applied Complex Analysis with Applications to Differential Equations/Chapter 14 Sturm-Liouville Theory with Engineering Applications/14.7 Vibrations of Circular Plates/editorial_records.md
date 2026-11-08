
# Editorial records

Reading note: 14.7 Vibrations of Circular Plates.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!proposition] Radial Scaling of Solutions of the Laplace Eigenvalue Equation
> Suppose $\phi(r,\theta)$ satisfies $\nabla^2\phi=\lambda\phi$ on a planar domain. For a positive real dilation $\alpha$ and a nonzero constant $A$, define $\psi(r,\theta)=A\phi(\alpha r,\theta)$ on the correspondingly rescaled domain. Then $\nabla^2\psi=\alpha^2\lambda\psi$. This is a statement about the differential equation; boundary conditions must also be rescaled.
>
> The same algebra applies to a complex value of $\alpha$ when the radial factor has an analytic continuation to the required complex arguments, as for integer-order Bessel functions.
````
### After

````text
> [!proposition] Dilation of Eigenfunctions
> Suppose that $\phi(r, \theta)$ satisfies $\nabla^{2} \phi=\lambda \phi(\lambda \neq 0)$, and let $\psi(r, \theta)=A \phi(\alpha r, \theta)$, where $A$ and $\alpha$ are nonzero constants. Then $\nabla^{2} \psi=\alpha^{2} \lambda \psi$. The domain is rescaled accordingly. Complex $\alpha$ requires analytic continuation of the radial factor to the arguments used.
````

## 2. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem] Clamped Circular-Plate Eigenfunctions from Bessel Functions
> Let $a>0$. For each integer $m\ge0$, let $k_{mn}$, $n=1,2,\ldots$, be the positive roots in increasing order of
>
> $$
> J_m(ka)I_m'(ka)-I_m(ka)J_m'(ka)=0,
> $$
>
> where $J_m$ and $I_m$ are the Bessel and modified Bessel functions of order $m$, and primes denote derivatives of their arguments. Define
>
> $$
> R_{mn}(r)=I_m(k_{mn}a)J_m(k_{mn}r)-J_m(k_{mn}a)I_m(k_{mn}r).
> $$
>
> The nonzero modes $R_{mn}(r)\cos(m\theta)$ for $m\ge0$, and $R_{mn}(r)\sin(m\theta)$ for $m\ge1$, are smooth at the center and satisfy
>
> $$
> \nabla^4\phi=k_{mn}^4\phi\quad(r<a),\qquad
> \phi(a,\theta)=\phi_r(a,\theta)=0.
> $$
````
### After

````text
> [!theorem] Eigenfunctions of the Biharmonic Operator
> For $m=0,1,2, \ldots, n=1,2, \ldots$, consider the function $\phi_{m n}(r, \theta)$ given by
>
> $$
> \left[I_{m}\left(k_{m n} a\right) J_{m}\left(k_{m n} r\right)-J_{m}\left(k_{m n} a\right) I_{m}\left(k_{m n} r\right)\right] \cos m \theta
> $$
>
> or, for $m\ge1$,
>
> $$
> \left[I_{m}\left(k_{m n} a\right) J_{m}\left(k_{m n} r\right)-J_{m}\left(k_{m n} a\right) I_m\left(k_{m n} r\right)\right] \sin m \theta
> $$
>
> where $k_{m n}$ is a positive root of
>
> $$
> J_{m}(k a) I_{m}^{\prime}(k a)-I_{m}(k a) \cdot J_{m}^{\prime}(k a)=0
> $$
>
> Then $\nabla^{4} \phi_{m n}=k_{m n}^{4} \phi_{m n}$ and $\phi_{m n}$ satisfies the boundary conditions $\phi_{mn}(a,\theta)=\partial_r\phi_{mn}(a,\theta)=0$. Here $a>0$, $J_m$ and $I_m$ are the Bessel and modified Bessel functions, and $k_{mn}$ denotes the $n$th positive root.
````

## 3. Restore source wording; retain only the actual correction.

### Before

````text
The radial case $m=0$ below illustrates the coefficient calculation.
````
### After

````text
We will prove these facts when $m=0$ in the second part of this section.
````

## 4. Preserve the source limitation/correction history in the editorial record only.

### Before

````text
[Source corrections: the signs and factors in Exercises 2 and 6, the order restriction in Exercise 7, and the $y_2$ definition and derivative sum in Exercise 12 are corrected. The sequence is restored to Exercises 1–22.]
````
### After

````text

````

## 5. Move correction/commentary into the separate editorial record; keep the actual correction in the reading text.

### Before

````text
[Source correction: the printed real-axis asymptotic formula for $J_0$ does not by itself justify substituting an imaginary argument. Exercise 22 now uses the preceding integral representation to establish the stated result.]
````
### After

````text

````

## Source-to-current comparison

Source: /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 14 Sturm-Liouville Theory with Engineering Applications/14.7 Vibrations of Circular Plates.md

This exact comparison preserves the full change evidence, including formatting, OCR corrections, restored source wording, and required standalone context. The entries above explain the recovery edits. The comparison is not a claim that every difference is a correction; component serialization, callout wrapping, and printed labels outside callouts are formatting.

`````diff
--- /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 14 Sturm-Liouville Theory with Engineering Applications/14.7 Vibrations of Circular Plates.md
+++ /Users/gradyclopton/ObsidianVaults/complex_analysis/Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 14 Sturm-Liouville Theory with Engineering Applications/14.7 Vibrations of Circular Plates.md
@@ -1,6 +1,7 @@
+
 ### 14.7 Vibrations of Circular Plates
 
-The vibrations of plates are governed by the two-dimensional analog of the equation for the vibrations of beams (Section 14.4):
+The vibrations of plates are governed by the two-dimensional analog of the equation for the vibrations of beams (Section 14.5):
 
 $$
 \frac{\partial^{2} u}{\partial t^{2}}+c^{2} \nabla^{4} u=0 .
@@ -10,40 +11,46 @@
 
 $$
 u_{t t}+c^{2} \nabla^{4} u=0, \quad 0 \leq r<a, 0 \leq \theta \leq 2 \pi, t>0 .
+\tag{1}
 $$
 
 The appropriate boundary conditions for a clamped plate are
 
 $$
 u(a, \theta, t)=0 \text { and } u_{r}(a, \theta, t)=0
+\tag{2}
 $$
 
 and the initial conditions are
 
 $$
 u(r, \theta, 0)=f(r, \theta), u_{t}(r, \theta, 0)=g(r, \theta), 0 \leq r<a, 0 \leq \theta \leq 2 \pi .
+\tag{3}
 $$
 
 We will also consider the nonhomogeneous equation
 
 $$
 u_{t t}+c^{2} \nabla^{4} u=F(r, \theta, t), \quad 0 \leq r<a, 0 \leq \theta \leq 2 \pi, t>0,
-$$
-
-supplied with similar boundary and initial conditions. As you can imagine, the task ahead of us is at least as complicated as the solution of the vibrating membrane problem from Sections 4.2-4.3. We will first determine the eigenvalues and eigenfunctions of the biharmonic operator on the disk, and then use the eigenfunction expansion method to solve the stated boundary value problems. The good news is that the eigenfunction problem will be reduced to the one that we solved in Section 4.6.
-
-Eigenfunctions of the Biharmonic Operator Consider the eigenvalue problem on a disk of radius $a$,
+\tag{4}
+$$
+
+supplied with similar boundary and initial conditions. As you can imagine, the task ahead of us is at least as complicated as the solution of the vibrating membrane problem from Sections 12.2–12.3. We will first determine the eigenvalues and eigenfunctions of the biharmonic operator on the disk, and then use the eigenfunction expansion method to solve the stated boundary value problems. The good news is that the eigenfunction problem will be reduced to the one that we solved in Section 12.6.
+
+## Eigenfunctions of the Biharmonic Operator
+
+Consider the eigenvalue problem on a disk of radius $a$,
 
 $$
 \nabla^{4} \phi(r, \theta)=k^{4} \phi(r, \theta), 0 \leq r<a, 0 \leq \theta \leq 2 \pi,
-$$
-
-## PROPOSITION 1 DILATION OF EIGENFUNCTIONS
+\tag{5}
+$$
 
 with the boundary conditions
 
 $$
 \phi(a, \theta)=0, \phi_{r}(a, \theta)=0, \quad 0 \leq \theta \leq 2 \pi .
+\tag{6}
 $$
 
 Here we have an additional condition on the normal derivative at the boundary, which we did not have with the Laplacian. Also, for the sake of convenience, we wrote the constant in (5) as $k^{4}$. The important fact is that the constant should be positive.
@@ -54,18 +61,22 @@
 \nabla^{4}(\phi)=\nabla^{2}\left(\nabla^{2} \phi\right)=\nabla^{2}\left( \pm k^{2} \phi\right)= \pm k^{2} \nabla^{2}(\phi)=k^{4} \phi
 $$
 
-So if $\phi$ is an eigenfunction of the Laplacian corresponding to the eigenvalue $\pm k^{2}$, then $\phi$ is an eigenfunction of the biharmonic operator corresponding to the eigenvalue $k^{4}$. With this in mind and without worrying about the boundary conditions for now, looking back at Section 4.6, we find that the functions
+So if $\phi$ is an eigenfunction of the Laplacian corresponding to the eigenvalue $\pm k^{2}$, then $\phi$ is an eigenfunction of the biharmonic operator corresponding to the eigenvalue $k^{4}$. With this in mind and without worrying about the boundary conditions for now, looking back at Section 12.6, we find that the functions
 
 $$
 \phi(r, \theta)=J_{m}(k r) \cos m \theta \text { or } J_{m}(k r) \sin m \theta \quad(m=0,1,2, \ldots)
+\tag{7}
 $$
 
 are solutions of $\nabla^{2} \phi=-k^{2} \phi$, and thus they satisfy the equation $\nabla^{4} u=k^{4} u$. We next ask, What are the nonzero solutions of $\nabla^{2} \phi=+k^{2} \phi$ ? Are they related to the solutions of $\nabla^{2} \phi=-k^{2} \phi$ ? To answer these questions, we first prove the following useful proposition.
 
-Suppose that $\phi(r, \theta)$ satisfies $\nabla^{2} \phi=\lambda \phi(\lambda \neq 0)$, and let $\psi(r, \theta)=A \phi(\alpha r, \theta)$, where $A$ and $\alpha$ are nonzero constants. Then $\nabla^{2} \psi=\alpha^{2} \lambda \psi$.
+> [!proposition] Dilation of Eigenfunctions
+> Suppose that $\phi(r, \theta)$ satisfies $\nabla^{2} \phi=\lambda \phi(\lambda \neq 0)$, and let $\psi(r, \theta)=A \phi(\alpha r, \theta)$, where $A$ and $\alpha$ are nonzero constants. Then $\nabla^{2} \psi=\alpha^{2} \lambda \psi$. The domain is rescaled accordingly. Complex $\alpha$ requires analytic continuation of the radial factor to the arguments used.
 
 In other words, the radial dilate of an eigenfunction by a factor $\alpha$ is an eigenfunction that corresponds to the same eigenvalue scaled by $\alpha^{2}$.
-Proof The equation $\nabla^{2} \phi=\lambda \phi$ tells us that
+### Proof
+
+The equation $\nabla^{2} \phi=\lambda \phi$ tells us that
 
 $$
 \phi_{r r}(r, \theta)+\frac{1}{r} \phi_{r}(r, \theta)+\frac{1}{r^{2}} \phi_{\theta \theta}(r, \theta)=\lambda \phi(r, \theta)
@@ -75,9 +86,10 @@
 
 $$
 \phi_{r r}(\rho, \theta)+\frac{1}{\rho} \phi_{r}(\rho, \theta)+\frac{1}{\rho^{2}} \phi_{\theta \theta}(\rho, \theta)=\lambda \phi(\rho, \theta)
-$$
-
-We now compute the Laplacian of $\psi$ using $\psi_{r}(\alpha r, \theta)=A \alpha \phi_{r}(\alpha r, \theta), \psi_{r r}(\alpha r, \theta)= A \alpha^{2} \phi_{r r}(\alpha r, \theta)$, and $\psi_{\theta \theta}(\alpha r, \theta)=A \phi_{\theta \theta}(\alpha r, \theta)$ :
+\tag{8}
+$$
+
+We now compute the Laplacian of $\psi$ using $\psi_{r}(r, \theta)=A \alpha \phi_{r}(\alpha r, \theta), \psi_{r r}(r, \theta)= A \alpha^{2} \phi_{r r}(\alpha r, \theta)$, and $\psi_{\theta \theta}(r, \theta)=A \phi_{\theta \theta}(\alpha r, \theta)$ :
 
 $$
 \begin{aligned}
@@ -89,10 +101,11 @@
 $$
 
 This shows that $\psi$ is an eigenfunction that corresponds to the eigenvalue $\alpha^{2} \lambda$.
-Recall the definition of the modified Bessel function of integer order $m$ (Section 4.7, Exercise 29): $I_{m}(r)=\frac{1}{i^{m}} J_{m}(i r)$. Let
+Recall the definition of the modified Bessel function of integer order $m$ (Section 12.7, Exercise 29): $I_{m}(r)=\frac{1}{i^{m}} J_{m}(i r)$. Let
 
 $$
 \psi(r, \theta)=I_{m}(k r) \cos m \theta \text { or } I_{m}(k r) \sin m \theta \quad(m=0,1,2, \ldots)
+\tag{9}
 $$
 
 We have $\psi(r, \theta)=\frac{1}{i^{m}} \phi(i r, \theta)$, where $\phi$ is as in (7). Since $\nabla^{2} \phi=-k^{2} \phi$, then, by Proposition 1,
@@ -103,28 +116,32 @@
 
 We now summarize our findings and give a formula for the eigenvalues.
 
-THEOREM 1 EIGENFUNCTIONS OF THE BIHARMONIC OPERATOR
-
-For $m=0,1,2, \ldots, n=1,2, \ldots$, consider the function $\phi_{m n}(r, \theta)$ given by
-
-$$
-\left[I_{m}\left(k_{m n} a\right) J_{m}\left(k_{m n} r\right)-J_{m}\left(k_{m n} a\right) I_{m}\left(k_{m n} r\right)\right] \cos m \theta
-$$
-
-or
-
-$$
-\left[I_{m}\left(k_{m n} a\right) J_{m}\left(k_{m n} r\right)-J_{m}\left(k_{m n} a\right) I_{m n}\left(k_{m n} r\right)\right] \sin m \theta
-$$
-
-where $k_{m n}$ is a positive root of
-
-$$
-J_{m}(k a) I_{m}^{\prime}(k a)-I_{m}(k a) \cdot J_{m}^{\prime}(k a)=0
-$$
-
-Then $\nabla^{4} \phi_{m n}=k_{m n}^{4} \phi_{m n}$ and $\phi_{m n}$ satisfies the boundary conditions (6).
-Proof We have already established that $J_{m}\left(k_{m n} r\right) \cos m \theta, \quad I_{m}\left(k_{m n} r\right) \cos m \theta$, $J_{m}\left(k_{m n} r\right) \sin m \theta$, and $I_{m}\left(k_{m n} r\right) \sin m \theta$ are all eigenfunctions satisfying $\nabla^{4} \phi=k^{A} \phi$. Consequently, any linear combination of these functions is also an eigenfunction corresponding to $k^{4}$, and, in particular, the functions in (10) and (11) are eigenfunctions corresponding to $k^{4}$. We now show that if $k_{m n}$ is a root of equation (12), then the functions in (10) and (11) also satisfy the boundary conditions (6). Take $\phi(r, \theta)=\left[I_{m}\left(k_{m n} a\right) J_{m}\left(k_{m n} r\right)-J_{m}\left(k_{m n} a\right) I_{m}\left(k_{m n} r\right)\right] \cos m \theta$. Then
+> [!theorem] Eigenfunctions of the Biharmonic Operator
+> For $m=0,1,2, \ldots, n=1,2, \ldots$, consider the function $\phi_{m n}(r, \theta)$ given by
+>
+> $$
+> \left[I_{m}\left(k_{m n} a\right) J_{m}\left(k_{m n} r\right)-J_{m}\left(k_{m n} a\right) I_{m}\left(k_{m n} r\right)\right] \cos m \theta
+> $$
+>
+> or, for $m\ge1$,
+>
+> $$
+> \left[I_{m}\left(k_{m n} a\right) J_{m}\left(k_{m n} r\right)-J_{m}\left(k_{m n} a\right) I_m\left(k_{m n} r\right)\right] \sin m \theta
+> $$
+>
+> where $k_{m n}$ is a positive root of
+>
+> $$
+> J_{m}(k a) I_{m}^{\prime}(k a)-I_{m}(k a) \cdot J_{m}^{\prime}(k a)=0
+> $$
+>
+> Then $\nabla^{4} \phi_{m n}=k_{m n}^{4} \phi_{m n}$ and $\phi_{m n}$ satisfies the boundary conditions $\phi_{mn}(a,\theta)=\partial_r\phi_{mn}(a,\theta)=0$. Here $a>0$, $J_m$ and $I_m$ are the Bessel and modified Bessel functions, and $k_{mn}$ denotes the $n$th positive root.
+
+*Printed equation labels: (10) cosine eigenmode; (11) sine eigenmode; (12) characteristic equation for the radial wavenumbers.*
+
+### Proof
+
+We have already established that $J_{m}\left(k_{m n} r\right) \cos m \theta, \quad I_{m}\left(k_{m n} r\right) \cos m \theta$, $J_{m}\left(k_{m n} r\right) \sin m \theta$, and $I_{m}\left(k_{m n} r\right) \sin m \theta$ are all eigenfunctions satisfying $\nabla^{4} \phi=k^4 \phi$. Consequently, any nonzero linear combination of these functions is also a solution of the eigenvalue equation corresponding to $k^{4}$, and, in particular, the functions in (10) and (11) are eigenfunctions corresponding to $k^{4}$. We now show that if $k_{m n}$ is a root of equation (12), then the functions in (10) and (11) also satisfy the boundary conditions (6). Take $\phi(r, \theta)=\left[I_{m}\left(k_{m n} a\right) J_{m}\left(k_{m n} r\right)-J_{m}\left(k_{m n} a\right) I_{m}\left(k_{m n} r\right)\right] \cos m \theta$. Then
 
 $$
 \phi(a, \theta)=\left[I_{m}\left(k_{m n} a\right) J_{m}\left(k_{m n} a\right)-I_{m}\left(k_{m n} a\right) J_{m}\left(k_{m n} a\right)\right] \cos m \theta=0
@@ -133,7 +150,7 @@
 and
 
 $$
-\phi_{T}(a, \theta)=k_{m n}\left[I_{m}\left(k_{m n} a\right) J_{m}^{\prime}\left(k_{m n} a\right)-J_{m}\left(k_{m n} a\right) I_{m}^{\prime}\left(k_{m n} a\right)\right] \cos m \theta=0
+\phi_r(a, \theta)=k_{m n}\left[I_{m}\left(k_{m n} a\right) J_{m}^{\prime}\left(k_{m n} a\right)-J_{m}\left(k_{m n} a\right) I_{m}^{\prime}\left(k_{m n} a\right)\right] \cos m \theta=0
 $$
 
 because $k_{m n}$ is a root of (12). The same is true if $\phi_{m n}$ is given by (11).
@@ -141,6 +158,7 @@
 
 $$
 \int_{0}^{2 \pi} \int_{0}^{a} \phi_{m n}(r, \theta) \phi_{m^{\prime} n^{\prime}}(r, \theta) r d r d \theta=0
+\tag{13}
 $$
 
 and any reasonably smooth function $f(r, \theta)$ on the disk has an eigenfunction expansion of the form
@@ -148,11 +166,12 @@
 $$
 \begin{aligned}
 f(r, \theta)= & \sum_{m=0}^{\infty} \sum_{n=1}^{\infty}\left[A_{m n}\left[I_{m}\left(k_{m n} a\right) J_{m}\left(k_{m n} r\right)-J_{m}\left(k_{m n} a\right) I_{m}\left(k_{m n} r\right)\right] \cos m \theta\right. \\
-& \left.+B_{m n}\left[I_{m}\left(k_{m n} a\right) J_{m}\left(k_{m n} r\right)-J_{m}\left(k_{m n} a\right) I_{m n}\left(k_{m n} r\right)\right] \sin m \theta\right]
+& \left.+B_{m n}\left[I_{m}\left(k_{m n} a\right) J_{m}\left(k_{m n} r\right)-J_{m}\left(k_{m n} a\right) I_m\left(k_{m n} r\right)\right] \sin m \theta\right]
 \end{aligned}
-$$
-
-where the coefficients are given by the inner product of $f$ against the eigenfunctions. We will prove these facts when $m=0$ in the second part of this section. The general case is similar, but the notation is much more cumbersome.
+\tag{14}
+$$
+
+Each coefficient is the inner product of $f$ with its mode divided by the squared norm of that mode, using area measure $r\,dr\,d\theta$. Omit the zero sine mode at $m=0$ (set $B_{0n}=0$). The expansion is understood in $L^2$; pointwise and boundary convergence require appropriate regularity and compatibility. We will prove these facts when $m=0$ in the second part of this section. The general case is similar, but the notation is much more cumbersome.
 
 To solve problems with the results that we have derived thus far requires knowledge of the eigenvalues, which can be obtained by estimating numerically the solutions of (12). To keep the presentation clear, we will consider radially symmetric problems only.
 
@@ -162,53 +181,135 @@
 
 $$
 f(r)=\sum_{n=1}^{\infty} A_{n}\left[I_{0}\left(k_{n}\right) J_{0}\left(k_{n} r\right)-J_{0}\left(k_{n}\right) I_{0}\left(k_{n} r\right)\right]
+\tag{15}
 $$
 
 where $k_{n}$ is the $n$th positive root of equation (12) with $a=1$ and $m=0$,
 
 $$
 J_{0}(k) I_{0}^{\prime}(k)-I_{0}(k) J_{0}^{\prime}(k)=0 .
-$$
-
-We know from Section 4.8 that $J_{0}^{\prime}(k)=-J_{1}(k)$ and, in a similar way, we can prove that $I_{0}^{\prime}(k)=I_{1}(k)$. Thus the equation for the eigenvalues becomes
+\tag{16}
+$$
+
+We know from Section 12.8 that $J_{0}^{\prime}(k)=-J_{1}(k)$ and, in a similar way, we can prove that $I_{0}^{\prime}(k)=I_{1}(k)$. Thus the equation for the eigenvalues becomes
 
 $$
 J_{0}(k) I_{1}(k)+I_{0}(k) J_{1}(k)=0 .
-$$
-
-![](./images/28f4ed6f-dce0-442f-8bed-abc918ef4e83-54_410_442_1708_63.jpg)
-Figure 1
-
-![](./images/28f4ed6f-dce0-442f-8bed-abc918ef4e83-54_408_439_1710_597.jpg)
-Figure 2
-
-![](./images/28f4ed6f-dce0-442f-8bed-abc918ef4e83-54_408_604_1710_1172.jpg)
-Figure 3
+\tag{17}
+$$
+
+```scientific-figure
+id: 9f3d45a8-11ce-4c3f-b1b7-0d429c50496e
+numbered: false
+title: ""
+caption: Figure 1
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 14 Sturm-Liouville Theory with Engineering Applications/images/28f4ed6f-dce0-442f-8bed-abc918ef4e83-54_410_442_1708_63.jpg
+    caption: ""
+```
+
+
+```scientific-figure
+id: b9df2835-7c5c-4430-92b2-9ae53a036975
+numbered: false
+title: ""
+caption: Figure 2
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 14 Sturm-Liouville Theory with Engineering Applications/images/28f4ed6f-dce0-442f-8bed-abc918ef4e83-54_408_439_1710_597.jpg
+    caption: ""
+```
+
+
+```scientific-figure
+id: 2ea9aace-054a-4b25-95a9-e75ba08fb4c3
+numbered: false
+title: ""
+caption: Figure 3
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 14 Sturm-Liouville Theory with Engineering Applications/images/28f4ed6f-dce0-442f-8bed-abc918ef4e83-54_408_604_1710_1172.jpg
+    caption: ""
+```
+
 
 The graphs of $J_{0}$ and $J_{1}$ oscillate and have infinitely many zeros (Figure 1), while the graphs of $I_{0}$ and $I_{1}$ are increasing and tend to infinity (Figure 2). It is thus conceivable that the graph of $J_{0}(k) I_{1}(k)+I_{0}(k) J_{1}(k)$ will oscillate and have infinitely many zeros (Figure 3). Table 1 shows numerical estimates of the first six roots. It is interesting to observe that the $n$th root is approximately $n \pi$.
 
-| $n$ | 1 | 2 | 3 | 4 | 5 | 6 |
-| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
-| $k_{n}$ | 3.1962 | 6.3064 | 9.4395 | 12.5771 | 15.7164 | 18.8565 |
-| $n \pi$ | 3.1416 | 6.2832 | 9.4248 | 12.5664 | 15.7080 | 18.8496 |
-
-Table 1. $k_{n}$, positive roots of $J_{0}(k) I_{1}(k)+I_{0}(k) J_{1}(k)=0$.
+```scientific-table
+id: 331fa46d-acf0-45ee-9e2f-44121d849efe
+numbered: false
+title: ""
+caption: Table 1. $k_{n}$, positive roots of $J_{0}(k) I_{1}(k)+I_{0}(k) J_{1}(k)=0$.
+captionVisible: true
+captionPosition: below
+rows:
+  - - text: $n$
+    - text: "1"
+    - text: "2"
+    - text: "3"
+    - text: "4"
+    - text: "5"
+    - text: "6"
+  - - text: $k_{n}$
+    - text: "3.1962"
+    - text: "6.3064"
+    - text: "9.4395"
+    - text: "12.5771"
+    - text: "15.7164"
+    - text: "18.8565"
+  - - text: $n \pi$
+    - text: "3.1416"
+    - text: "6.2832"
+    - text: "9.4248"
+    - text: "12.5664"
+    - text: "15.7080"
+    - text: "18.8496"
+headerRows: 1
+rowHeaders: true
+style: scientific
+```
+
 
 Let us now describe the generalized Fourier coefficients $A_{n}$ in (15). These are derived in the usual way, using the orthogonality of the eigenfunctions
 
 $$
 \phi_{n}(r)=I_{0}\left(k_{n}\right) J_{0}\left(k_{n} r\right)-J_{0}\left(k_{n}\right) I_{0}\left(k_{n} r\right)
+\tag{18}
 $$
 
 on the interval $(0,1)$, with respect to the weight $r$. Thus,
 
 $$
 A_{n}=\frac{1}{\int_{0}^{1} \phi_{n}(r)^{2} r d r} \int_{0}^{1} f(r) \phi_{n}(r) r d r
+\tag{19}
 $$
 
 To handle integrals involving $J_{0}$ and $I_{0}$ (in particular, to find an expression for $\int_{0}^{1} \phi_{n}(r)^{2} r d r$ ), we will appeal to various integral identities, such as
 
-## You can verify these identities by simply differentiating to undo the integrals.
+> [!identity] Integrals of Products of Order-Zero Bessel and Modified Bessel Functions
+> For a nonzero real constant $\lambda$, with $J_\nu$ and $I_\nu$ denoting Bessel and modified Bessel functions,
+>
+> $$
+> \begin{aligned}
+> \int xJ_0(\lambda x)^2\,dx
+> &=\frac{x^2}{2}\left[J_0(\lambda x)^2+J_1(\lambda x)^2\right]+C,\\
+> \int xI_0(\lambda x)^2\,dx
+> &=\frac{x^2}{2}\left[I_0(\lambda x)^2-I_1(\lambda x)^2\right]+C,\\
+> \int xI_0(\lambda x)J_0(\lambda x)\,dx
+> &=\frac{x}{2\lambda}\left[I_1(\lambda x)J_0(\lambda x)+I_0(\lambda x)J_1(\lambda x)\right]+C.
+> \end{aligned}
+> $$
+
+*Printed equation labels: (20) integral of $xJ_0(\lambda x)^2$; (21) integral of $xI_0(\lambda x)^2$; (22) integral of $xI_0(\lambda x)J_0(\lambda x)$.*
+
+You can verify these identities by simply differentiating to undo the integrals.
 
 You can also derive them by appealing to the differential equations for $I_{0}$ and $J_{0}$. Let us illustrate this important technique by proving (20).
 
@@ -226,7 +327,7 @@
 \end{array}
 $$
 
-Now $y^{\prime}=J_{0}^{\prime}(x)=J_{1}(x)$. So
+Now $y^{\prime}=J_{0}^{\prime}(x)=-J_{1}(x)$. So
 
 $$
 x^{2} J_{1}^{2}(x)+\int x^{2}\left(y^{2}\right)^{\prime} d x=C
@@ -254,14 +355,17 @@
 =\int_{0}^{1}\left[I_{0}\left(k_{n}\right) J_{0}\left(k_{n} r\right)-J_{0}\left(k_{n}\right) I_{0}\left(k_{n} r\right)\right]^{2} r d r \\
 =\left[I_{0}\left(k_{n}\right)\right]^{2}\left[J_{0}\left(k_{n}\right)\right]^{2}+\frac{1}{2}\left[I_{0}\left(k_{n}\right)\right]^{2}\left[J_{1}\left(k_{n}\right)\right]^{2}-\frac{1}{2}\left[J_{0}\left(k_{n}\right)\right]^{2}\left[I_{1}\left(k_{n}\right)\right]^{2}
 \end{gathered}
+\tag{23}
 $$
 
 We are now ready to compute a simple eigenfunction expansion, which will be needed later to solve a forced vibrations problem.
 
-## EXAMPLE 1 An eigenfunction expansion
-
-Expand the function $f(r)=1$ for $0 \leq r<1$ in terms of the eigenfunctions (18).
-Solution We have to evaluate the coefficients $A_{n}$ in the series (15). We have already computed the integral $\int_{0}^{1} \phi_{n}(r)^{2} r d r$ in (23). We now compute
+> [!exercise] EXAMPLE 1 An eigenfunction expansion
+> Expand the function $f(r)=1$ for $0 \leq r<1$ in terms of the eigenfunctions (18).
+
+##### solution
+
+We have to evaluate the coefficients $A_{n}$ in the series (15). We have already computed the integral $\int_{0}^{1} \phi_{n}(r)^{2} r d r$ in (23). We now compute
 
 $$
 \begin{aligned}
@@ -270,10 +374,21 @@
 \end{aligned}
 $$
 
-![](./images/28f4ed6f-dce0-442f-8bed-abc918ef4e83-57_412_463_856_24.jpg)
-Figure 4 Eigenfunction expansion of $f(r)=1$, $1<r<1$. Note the overshoot at the endpoints.
-
-The first integral on the right side is similar to one that we computed in Example 1, Section 4.8. We have
+```scientific-figure
+id: d79d1d61-bb33-4c4a-882c-7a6d30b68376
+numbered: false
+title: ""
+caption: Figure 4 Eigenfunction expansion of $f(r)=1$, $0\le r<1$. The plotted diameter extends the radial function evenly; the overshoot occurs near the disk edge.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 14 Sturm-Liouville Theory with Engineering Applications/images/28f4ed6f-dce0-442f-8bed-abc918ef4e83-57_412_463_856_24.jpg
+    caption: ""
+```
+
+
+The first integral on the right side is similar to one that we computed in Example 1, Section 12.8. We have
 
 $$
 \int_{0}^{1} J_{0}\left(k_{n} r\right) r d r=\frac{1}{k_{n}^{2}} \int_{0}^{k_{n}} J_{0}(r) r d r=\left.\frac{1}{k_{n}^{2}} J_{1}(r) r\right|_{0} ^{k_{n}}=\frac{1}{k_{n}} J_{1}\left(k_{n}\right) .
@@ -302,43 +417,69 @@
 
 Numerical values of the first six coefficients are shown in Table 2.
 
-| $n$ | 1 | 2 | 3 | 4 | 5 | 6 |
-| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
-| $A_{n}$ | 0.2812 | -0.0145 | 0.0007 | -0.00003 | 0.0 | 0.0 |
-
-Table 2. Numerical values of the generalized Fourier coefficients $A_{n}$.
+```scientific-table
+id: eed63047-3925-418c-bb9d-d29f9a497707
+numbered: false
+title: ""
+caption: Table 2. Numerical values of the generalized Fourier coefficients $A_{n}$. Entries displayed as 0.0 are rounded values, not exact zeros.
+captionVisible: true
+captionPosition: below
+rows:
+  - - text: $n$
+    - text: "1"
+    - text: "2"
+    - text: "3"
+    - text: "4"
+    - text: "5"
+    - text: "6"
+  - - text: $A_{n}$
+    - text: "0.2812"
+    - text: "-0.0145"
+    - text: "0.0007"
+    - text: "-0.00003"
+    - text: "0.0"
+    - text: "0.0"
+headerRows: 1
+rowHeaders: true
+style: scientific
+```
+
 
 The eigenfunction expansion is illustrated in Figure 4, where we have plotted the third, fifth, and tenth partial sums of the eigenfunction expansion (15).
 
 Next, we examine problems related to the vibrations of plates. We start with a radially symmetric version of the boundary value problem (1)-(3).
 
-## EXAMPLE 2 Vibrations of a plate
-
-Solve the equation
-
-$$
-u_{t t}+c^{2} \nabla^{4} u=0, \quad 0 \leq r<1,0 \leq \theta \leq 2 \pi, t>0,
-$$
-
-subject to the boundary conditions
-
-$$
-u(1, \theta, t)=0 \text { and } u_{r}(1, \theta, t)=0,
-$$
-
-and the radially symmetric initial conditions
-
-$$
-u(r, \theta, 0)=f(r), u_{t}(r, \theta, 0)=0,0 \leq r<a, 0 \leq \theta \leq 2 \pi .
-$$
-
-Solution We outline a step-by-step strategy.
+> [!exercise] EXAMPLE 2 Vibrations of a plate
+> Solve the equation
+>
+> $$
+> u_{t t}+c^{2} \nabla^{4} u=0, \quad 0 \leq r<1,0 \leq \theta \leq 2 \pi, t>0,
+> $$
+>
+> subject to the boundary conditions
+>
+> $$
+> u(1, \theta, t)=0 \text { and } u_{r}(1, \theta, t)=0,
+> $$
+>
+> and the radially symmetric initial conditions
+>
+> $$
+> u(r, \theta, 0)=f(r), u_{t}(r, \theta, 0)=0,0 \leq r<1, 0 \leq \theta \leq 2 \pi .
+> $$
+
+*Printed equation label: (24).*
+
+##### solution
+
+We outline a step-by-step strategy.
 Step 1. Use a radially symmetric solution, since the data is radially symmetric. Thus, $u(r, \theta, t)=u(r, t)$, and there is no dependence on $\theta$.
 
 Step 2. Assume that the solution has an eigenfunction expansion in terms of the functions in Theorem 1. Since there is no dependence on $\theta$, we only need the order 0 Bessel functions. Thus, following (15), we set
 
 $$
-u(r, t)=\sum_{n=1}^{\infty} A_{n}(t)\left[I_{0}\left(k_{n}\right) J_{0}\left(k_{n} r\right)-J_{0}\left(k_{n}\right) I_{0}\left(k_{n} r\right)\right]=\sum_{n=1}^{\infty} A_{n}(t) \dot{\phi}_{n}(r),
+u(r, t)=\sum_{n=1}^{\infty} A_{n}(t)\left[I_{0}\left(k_{n}\right) J_{0}\left(k_{n} r\right)-J_{0}\left(k_{n}\right) I_{0}\left(k_{n} r\right)\right]=\sum_{n=1}^{\infty} A_{n}(t) \phi_n(r),
+\tag{25}
 $$
 
 where here, unlike (15), we allow the coefficients $A_{n}$ to be functions of $t$. Note that because $\phi_{n}(1)=0$ and $\phi_{n}^{\prime}(1)=0$, the series (25) satisfies the boundary conditions. Now comes the crux of the method.
@@ -393,36 +534,40 @@
 
 In what follows, we consider a radially symmetric case of equation (4), in which the external force depends only on time and is decaying with time.
 
-## EXAMPLE 3 Forced vibrations of a plate
-
-Solve the equation
-
-$$
-u_{t t}+c^{2} \nabla^{4} u=e^{-t}, \quad 0 \leq r<1,0 \leq \theta \leq 2 \pi, t>0
-$$
-
-subject to the boundary conditions
-
-$$
-u(1, \theta, t)=0 \text { and } u_{r}(1, \theta, t)=0
-$$
-
-and the radially symmetric initial conditions
-
-$$
-u(r, \theta, 0)=0, u_{t}(r, \theta, 0)=0,0 \leq r<a, 0 \leq \theta \leq 2 \pi
-$$
-
-Solution Use a radially symmetric solution and allow the coefficients to be functions of $t$ :
+> [!exercise] EXAMPLE 3 Forced vibrations of a plate
+> Solve the equation
+>
+> $$
+> u_{t t}+c^{2} \nabla^{4} u=e^{-t}, \quad 0 \leq r<1,0 \leq \theta \leq 2 \pi, t>0
+> $$
+>
+> subject to the boundary conditions
+>
+> $$
+> u(1, \theta, t)=0 \text { and } u_{r}(1, \theta, t)=0
+> $$
+>
+> and the radially symmetric initial conditions
+>
+> $$
+> u(r, \theta, 0)=0, u_{t}(r, \theta, 0)=0,0 \leq r<1, 0 \leq \theta \leq 2 \pi
+> $$
+
+*Printed equation label: (26).*
+
+##### solution
+
+Use a radially symmetric solution and allow the coefficients to be functions of $t$ :
 
 $$
 u(r, t)=\sum_{n=1}^{\infty} a_{n}(t)\left[I_{0}\left(k_{n}\right) J_{0}\left(k_{n} r\right)-J_{0}\left(k_{n}\right) I_{0}\left(k_{n} r\right)\right]=\sum_{n=1}^{\infty} a_{n}(t) \phi_{n}(r)
+\tag{27}
 $$
 
 Plug this solution into equation (26), and use the fact that $\nabla^{4} \phi_{n}=k_{n}^{4} \phi_{n}$, as in the previous example. Then
 
 $$
-u_{t t}+c^{2} \nabla^{4} u=e^{-t} \Rightarrow \sum_{n=1}^{\infty}\left(a_{n}^{\prime \prime}(t)+k_{n}^{4} c^{2}\right) \phi_{n}(r)=e^{-t}
+u_{t t}+c^{2} \nabla^{4} u=e^{-t} \Rightarrow \sum_{n=1}^{\infty}\left(a_{n}^{\prime \prime}(t)+k_{n}^{4} c^{2}a_n(t)\right) \phi_{n}(r)=e^{-t}
 $$
 
 To go any further, we have to think of the right side as an eigenfunction expansion in $r$. Indeed, think of it as $e^{-t} \cdot 1$ and expand the constant function 1 in a series in terms of the $\phi_{n}(r)$. This is precisely the expansion that we computed in Example 1. Thus,
@@ -435,6 +580,7 @@
 
 $$
 a_{n}^{\prime \prime}(t)+k_{n}^{4} c^{2} a_{n}(t)=A_{n} e^{-t}
+\tag{28}
 $$
 
 A particular solution $b_{n}(t)$ of this equation can be found by setting $b_{n}(t)=C e^{-t}$. Plugging into the equation, we find
@@ -470,143 +616,206 @@
 and so $\beta_{n}=\frac{A_{n}}{k_{n}^{2} c\left(1+k_{n}^{4} c^{2}\right)}$, which leads us to the solution
 
 $$
-u(r, t)=\sum_{n=1}^{\infty}\left[-\cos k_{n}^{2} c t+\frac{1}{k_{n}^{2} c} \sin k_{n}^{2} c t+e^{-\iota}\right] \frac{A_{n}}{1+k_{n}^{4} c^{2}} \phi_{n}(r) .
+u(r, t)=\sum_{n=1}^{\infty}\left[-\cos k_{n}^{2} c t+\frac{1}{k_{n}^{2} c} \sin k_{n}^{2} c t+e^{-t}\right] \frac{A_{n}}{1+k_{n}^{4} c^{2}} \phi_{n}(r) .
 $$
 
 The validity of this solution can be checked without too much trouble.
 
-## Exercises 6.7
-
-In Exercises 1-10, we list properties of the modified Bessel functions. Prove each property by modifying the proof of the corresponding property for Bessel functions. Alternatively, you can use the corresponding property of the Bessel function and the definition of $I_{p}$ from Exercise 29, Section 4.7: $I_{p}(x)=\frac{1}{i^{p}} J_{p}(i x)$.
-
-1. $\left[x^{p} I_{p}(x)\right]^{\prime}=x^{p} I_{p-1}$.
-2. $\left[x^{-p} I_{p}(x)\right]^{\prime}=-x^{-p} I_{p+1}$.
-3. $x I_{p}^{\prime}(x)=x I_{p-1}(x)-p I_{p}(x)$.
-4. $x I_{p}^{\prime}(x)=x I_{p+1}(x)+p I_{p}(x)$.
-5. $2 I_{p}^{\prime}(x)=I_{p-1}(x)+I_{p+1}(x)$.
-6. $2 p I_{p}^{\prime}(x)=x\left[I_{p-1}(x)-I_{p+1}(x)\right]$.
-7. $I_{-p}(x)=I_{p}(x)$.
-$8 . \frac{d}{d x} I_{0}(x)=I_{1}(x)$.
-8. $\int x^{p+1} I_{p}(x) d x=x^{p+1} I_{p+1}(x)+C$.
-9. $\int x^{-p+1} I_{p}(x) d x=-x^{-p+1} I_{p-1}(x)+C$.
-10. Prove (21) by modifying the proof of (20). (Recall that the differential equation for the modified Bessel function of order 0 is $x^{2} y^{\prime \prime}+x y^{\prime}-x^{2} y=0$.)
-11. Project Problem: Proof of (22). Justify each step in the following proof of (22). Let $y_{1}=J_{0}(x)$ and $y_{2}=J_{1}(x)$. Then
-
-$$
-\begin{gathered}
-x\left(y_{1}+y_{2}\right)^{\prime \prime}+\left(y_{1}+y_{2}\right)^{\prime}+x\left(y_{1}-y_{2}\right)=0 \\
-{\left[x\left(y_{1}+y_{2}\right)^{\prime}\right]^{\prime}+x\left(y_{1}-y_{2}\right)=0} \\
-{\left[\left[x\left(y_{1}+y_{2}\right)^{\prime}\right]^{2}\right]^{\prime}+2 x^{2}\left(y_{1}-y_{2}\right)\left(y_{1}^{\prime}-y_{2}^{\prime}\right)=0} \\
-{\left[x\left(y_{1}+y_{2}\right)^{\prime}\right]^{2}=-2 \int x^{2}\left(y_{1}-y_{2}\right)\left(y_{1}^{\prime}-y_{2}^{\prime}\right) d x}
-\end{gathered}
-$$
-
-Finish off the proof of (22) by using $y_{1}^{\prime}=-J_{1}(x), y_{2}^{\prime}=I_{1}(x)$, and evaluating the integral by parts. You will also need (20) and (21).
-13. Prove (23) by using (20)-(22).
-14. Expand the function $f(r)=1-r^{2}$ for $0 \leq r<1$ in terms of the eigenfunctions (18).
-15. Solve equation (24) subject to the boundary conditions
-
-$$
-u(1, \theta, t)=0 \text { and } u_{r}(1, \theta, t)=0
-$$
-
-and the radially symmetric initial conditions
-
-$$
-u(r, \theta, 0)=0, u_{t}(r, \theta, 0)=g(r), 0 \leq r<a, 0 \leq \theta \leq 2 \pi
-$$
-
-16. Solve equation (24) subject to the boundary conditions
-
-$$
-u(1, \theta, t)=0 \text { and } u_{r}(1, \theta, t)=0
-$$
-
-and the radially symmetric initial conditions
-
-$$
-u(r, \theta, 0)=f(r), u_{t}(r, \theta, 0)=g(r), 0 \leq r<a, 0 \leq \theta \leq 2 \pi
-$$
-
-17. Solve equation (26) subject to the boundary conditions
-
-$$
-u(1, \theta, t)=0 \text { and } u_{r}(1, \theta, t)=0
-$$
-
-and the radially symmetric initial conditions
-
-$$
-u(r, \theta, 0)=f(r), u_{t}(r, \theta, 0)=0,0 \leq r<a, 0 \leq \theta \leq 2 \pi
-$$
-
-18. Solve the equation
-
-$$
-u_{t t}+c^{2} \nabla^{4} u=1-r^{2}, \quad 0 \leq r<1,0 \leq \theta \leq 2 \pi, t>0
-$$
-
-subject to the boundary conditions
-
-$$
-u(1, \theta, t)=0 \text { and } u_{r}(1, \theta, t)=0
-$$
-
-and the radially symmetric initial conditions
-
-$$
-u(r, \theta, 0)=0, u_{t}(r, \theta, 0)=0,0 \leq r<a, 0 \leq \theta \leq 2 \pi .
-$$
-
-19. Let $u=u(r, \theta, t)$. Solve the equation
-
-$$
-u_{t}+c^{2} \nabla^{4} u=0, \quad 0 \leq r<1,0 \leq \theta \leq 2 \pi, t>0,
-$$
-
-subject to the boundary conditions
-
-$$
-u(1, \theta, t)=0 \text { and } u_{r}(1, \theta, t)=0
-$$
-
-and the radially symmetric initial conditions
-
-$$
-u(r, \theta, 0)=100,0 \leq r<a, 0 \leq \theta \leq 2 \pi
-$$
-
-20. Let $u=u(r, \theta)$. Solve the equation
-
-$$
-\nabla^{4} u=100, \quad 0 \leq r<1,0 \leq \theta \leq 2 \pi
-$$
-
-subject to the boundary conditions
-
-$$
-u(1, \theta, t)=0 \text { and } u_{r}(1, \theta, t)=0
-$$
-
-21. Project Problem: Integral representation of $I_{0}(x)$. Recall the definition of $I_{0}$ from Exercise 29, Section 4.7: $I_{0}(x)=J_{0}(i x)$. Recall the integral representation
-
-$$
-J_{0}(x)=\frac{1}{2 \pi} \int_{-\pi}^{\pi} e^{i x \sin t} d t
-$$
-
-(see Section 4.9, Theorem 1 and its proof).
-(a) Even though we have not established the validity of the integral representation of $J_{0}$ with complex variables, use it with $i x$ in place of $x$ to obtain
-
-$$
-I_{0}(x)=\frac{1}{2 \pi} \int_{-\pi}^{\pi} e^{-x \sin t} d t
-$$
-
-(b) Confirm the formula by verifying that the function defined by the integral satisfies the modified Bessel equation of order 0: $x^{2} y^{\prime \prime}+x y^{\prime}+x^{2} y=0$.
-22. Project Problem: Asymptotics for $I_{0}(x)$. Starting from the asymptotic formula for $J_{0}(x)$ (Theorem 3, Section 4.9) and using the identity $\cos u=\frac{e^{i u}+e^{-i u}}{2}$, show that, as $x \rightarrow \infty$,
-
-$$
-I_{0}(x) \sim \frac{1}{\sqrt{2 \pi x}} e^{x}
-$$
-
-
-[^0]:    Proof (a) Suppose that $y_{1}$ and $y_{2}$ are two eigenfunctions corresponding to the eigenvalue $\lambda$. We will show that $y_{1}$ and $y_{2}$ are linearly dependent by proving that their Wronskian $W\left(y_{1}, y_{2}\right)$ is 0 . Recall that we need only prove that $W\left(y_{1}, y_{2}\right)=0$
+## Exercises 14.7
+
+
+> [!prompt] Shared exercise instructions
+> In Exercises 1-10, we list properties of the modified Bessel functions. Prove each property by modifying the proof of the corresponding property for Bessel functions. Alternatively, you can use the corresponding property of the Bessel function and the definition of $I_{p}$ from Exercise 29, Section 12.7: $I_{p}(x)=\frac{1}{i^{p}} J_{p}(i x)$.
+
+
+> [!exercise] Exercise 1
+> $\left[x^pI_p(x)\right]^\prime=x^pI_{p-1}(x)$.
+
+
+> [!exercise] Exercise 2
+> $\left[x^{-p}I_p(x)\right]^\prime=x^{-p}I_{p+1}(x)$.
+
+
+> [!exercise] Exercise 3
+> $x I_{p}^{\prime}(x)=x I_{p-1}(x)-p I_{p}(x)$.
+
+
+> [!exercise] Exercise 4
+> $x I_{p}^{\prime}(x)=x I_{p+1}(x)+p I_{p}(x)$.
+
+
+> [!exercise] Exercise 5
+> $2 I_{p}^{\prime}(x)=I_{p-1}(x)+I_{p+1}(x)$.
+
+
+> [!exercise] Exercise 6
+> $2 p I_{p}(x)=x\left[I_{p-1}(x)-I_{p+1}(x)\right]$.
+
+
+> [!exercise] Exercise 7
+> $I_{-p}(x)=I_p(x)$ for integer $p$.
+
+
+> [!exercise] Exercise 8
+> $\frac{d}{dx}I_0(x)=I_1(x)$.
+
+
+> [!exercise] Exercise 9
+> $\int x^{p+1} I_{p}(x) d x=x^{p+1} I_{p+1}(x)+C$.
+
+
+> [!exercise] Exercise 10
+> $\int x^{-p+1} I_{p}(x) d x=-x^{-p+1} I_{p-1}(x)+C$.
+
+
+> [!exercise] Exercise 11
+> Prove (21) by modifying the proof of (20). (Recall that the differential equation for the modified Bessel function of order 0 is $x^{2} y^{\prime \prime}+x y^{\prime}-x^{2} y=0$.)
+
+
+> [!exercise] Exercise 12
+> Project Problem: Proof of (22). Justify each step in the following proof of (22). Let $y_{1}=J_{0}(x)$ and $y_2=I_0(x)$. Then
+>
+> $$
+> \begin{gathered}
+> x\left(y_{1}+y_{2}\right)^{\prime \prime}+\left(y_{1}+y_{2}\right)^{\prime}+x\left(y_{1}-y_{2}\right)=0 \\
+> {\left[x\left(y_{1}+y_{2}\right)^{\prime}\right]^{\prime}+x\left(y_{1}-y_{2}\right)=0} \\
+> {\left[\left[x\left(y_{1}+y_{2}\right)^{\prime}\right]^{2}\right]^{\prime}+2 x^{2}\left(y_{1}-y_{2}\right)\left(y_1^{\prime}+y_2^{\prime}\right)=0} \\
+> {\left[x\left(y_{1}+y_{2}\right)^{\prime}\right]^{2}=-2 \int x^{2}\left(y_{1}-y_{2}\right)\left(y_1^{\prime}+y_2^{\prime}\right) d x+C}
+> \end{gathered}
+> $$
+>
+> Finish off the proof of (22) by using $y_{1}^{\prime}=-J_{1}(x), y_{2}^{\prime}=I_{1}(x)$, and evaluating the integral by parts. You will also need (20) and (21).
+
+
+> [!exercise] Exercise 13
+> Prove (23) by using (20)-(22).
+
+
+> [!exercise] Exercise 14
+> Expand the function $f(r)=1-r^{2}$ for $0 \leq r<1$ in terms of the eigenfunctions (18).
+
+
+> [!exercise] Exercise 15
+> Solve equation (24) subject to the boundary conditions
+>
+> $$
+> u(1, \theta, t)=0 \text { and } u_{r}(1, \theta, t)=0
+> $$
+>
+> and the radially symmetric initial conditions
+>
+> $$
+> u(r, \theta, 0)=0, u_{t}(r, \theta, 0)=g(r), 0 \leq r<1, 0 \leq \theta \leq 2 \pi
+> $$
+
+
+> [!exercise] Exercise 16
+> Solve equation (24) subject to the boundary conditions
+>
+> $$
+> u(1, \theta, t)=0 \text { and } u_{r}(1, \theta, t)=0
+> $$
+>
+> and the radially symmetric initial conditions
+>
+> $$
+> u(r, \theta, 0)=f(r), u_{t}(r, \theta, 0)=g(r), 0 \leq r<1, 0 \leq \theta \leq 2 \pi
+> $$
+
+
+> [!exercise] Exercise 17
+> Solve equation (26) subject to the boundary conditions
+>
+> $$
+> u(1, \theta, t)=0 \text { and } u_{r}(1, \theta, t)=0
+> $$
+>
+> and the radially symmetric initial conditions
+>
+> $$
+> u(r, \theta, 0)=f(r), u_{t}(r, \theta, 0)=0,0 \leq r<1, 0 \leq \theta \leq 2 \pi
+> $$
+
+
+> [!exercise] Exercise 18
+> Solve the equation
+>
+> $$
+> u_{t t}+c^{2} \nabla^{4} u=1-r^{2}, \quad 0 \leq r<1,0 \leq \theta \leq 2 \pi, t>0
+> $$
+>
+> subject to the boundary conditions
+>
+> $$
+> u(1, \theta, t)=0 \text { and } u_{r}(1, \theta, t)=0
+> $$
+>
+> and the radially symmetric initial conditions
+>
+> $$
+> u(r, \theta, 0)=0, u_{t}(r, \theta, 0)=0,0 \leq r<1, 0 \leq \theta \leq 2 \pi .
+> $$
+
+
+> [!exercise] Exercise 19
+> Let $u=u(r, \theta, t)$. Solve the equation
+>
+> $$
+> u_{t}+c^{2} \nabla^{4} u=0, \quad 0 \leq r<1,0 \leq \theta \leq 2 \pi, t>0,
+> $$
+>
+> subject to the boundary conditions
+>
+> $$
+> u(1, \theta, t)=0 \text { and } u_{r}(1, \theta, t)=0
+> $$
+>
+> and the radially symmetric initial conditions
+>
+> $$
+> u(r, \theta, 0)=100,0 \leq r<1, 0 \leq \theta \leq 2 \pi
+> $$
+
+
+> [!exercise] Exercise 20
+> Let $u=u(r, \theta)$. Solve the equation
+>
+> $$
+> \nabla^{4} u=100, \quad 0 \leq r<1,0 \leq \theta \leq 2 \pi
+> $$
+>
+> subject to the boundary conditions
+>
+> $$
+> u(1, \theta)=0 \text { and } u_{r}(1, \theta)=0
+> $$
+
+
+ 
+
+> [!exercise] Exercise 21
+> Project Problem: Integral representation of $I_{0}(x)$. Recall the definition of $I_{0}$ from Exercise 29, Section 12.7: $I_{0}(x)=J_{0}(i x)$. Recall the integral representation
+>
+> $$
+> J_{0}(x)=\frac{1}{2 \pi} \int_{-\pi}^{\pi} e^{i x \sin t} d t
+> $$
+>
+> (see Section 12.9, Theorem 1 and its proof).
+> (a) Even though we have not established the validity of the integral representation of $J_{0}$ with complex variables, use it with $i x$ in place of $x$ to obtain
+>
+> $$
+> I_{0}(x)=\frac{1}{2 \pi} \int_{-\pi}^{\pi} e^{-x \sin t} d t
+> $$
+>
+> (b) Confirm the formula by verifying that the function defined by the integral satisfies the modified Bessel equation of order 0: $x^2y^{\prime\prime}+xy^\prime-x^2y=0$. Also verify the regular initial values $y(0)=1$ and $y^\prime(0)=0$.
+
+
+> [!exercise] Exercise 22
+> Project Problem: Asymptotics for $I_0(x)$. Use the integral representation from Exercise 21 and Laplace's method near the maximum of $-\sin t$ to show that, as $x\to+\infty$,
+>
+> $$
+> I_{0}(x) \sim \frac{1}{\sqrt{2 \pi x}} e^{x}
+> $$
+
+
+

`````
