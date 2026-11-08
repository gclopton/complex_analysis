
# Editorial records

Reading note: 9.4 The Hankel Transform with Applications.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!property|2169c6d6-8158-5aea-bb2e-9d3208b02910.local at=f2b86664-9a3f-5ec0-be6d-aa9e60b84377] Self-Inversion of the Hankel Transform
> For $\nu\geq0$, the transform $\mathcal H_\nu f(s)=\int_0^\infty f(x)J_\nu(sx)x\,dx$ extends to a unitary involution on $L^2((0,\infty),x\,dx)$:
>
> $$
> \mathcal H_\nu(\mathcal H_\nu f)=f.
> $$
>
> The equality is in the weighted $L^2$ sense; pointwise use of the iterated integrals requires additional convergence hypotheses.
````
### After

````text
> [!property|2169c6d6-8158-5aea-bb2e-9d3208b02910.local at=f2b86664-9a3f-5ec0-be6d-aa9e60b84377] Self-Inversion of the Hankel Transform
> For $\nu\geq0$, write $\mathcal H_\nu f(s)=\int_0^\infty f(x)J_\nu(sx)x\,dx$. A sufficient condition below is that $f$ be smooth with compact support in $(0,\infty)$.
>
> Under certain conditions on $f$ (which we are going to assume hold) one can prove the inversion formula
>
> $$
> \mathcal{H}_{\nu} \mathcal{H}_{\nu} f=f .
> $$
````

## 2. Move correction/commentary into the separate editorial record; keep the actual correction in the reading text.

### Before

````text
[Source limitation: after $x=z^2$, the ordinary Hankel integral of $f(z^2)=z^{-2}$ diverges logarithmically at zero. The stated data do not yield a solution by the ordinary-transform formula; a separate regularization would have to be specified.]
````
### After

````text

````

## 3. Move correction/commentary into the separate editorial record; keep the actual correction in the reading text.

### Before

````text
[Corrected: the boundary term in this integration by parts contains $J_1$, not the printed $J_0$. The appropriate endpoint conditions for each identity are stated above.]
````
### After

````text

````

## Source-to-current comparison

Source: /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 09 The Laplace and Hankel Transforms with Applications/9.4 The Hankel Transform with Applications.md

This exact comparison preserves the full change evidence, including formatting, OCR corrections, restored source wording, and required standalone context. The entries above explain the recovery edits. The comparison is not a claim that every difference is a correction; component serialization, callout wrapping, and printed labels outside callouts are formatting.

`````diff
--- /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 09 The Laplace and Hankel Transforms with Applications/9.4 The Hankel Transform with Applications.md
+++ /Users/gradyclopton/ObsidianVaults/complex_analysis/Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 09 The Laplace and Hankel Transforms with Applications/9.4 The Hankel Transform with Applications.md
@@ -1,40 +1,56 @@
-### 9.4 The Hankel Transform with Applications
-
-As we saw in Chapter 9, Bessel functions and Bessel series are instrumental in solving problems in polar coordinates. It should not surprise you, then, to see Bessel functions arising in the treatment of similar problems over unbounded regions. Instead of Bessel series, here we will need a transform, defined in terms of Bessel functions as follows.
-
-Suppose that $f(x)$ is defined for all $x \geq 0$. The Hankel transform of order $\nu \geq 0$ of $f(x)$ is given by
-
-$$
-\mathcal{H}_{\nu}(f)(s)=\int_{0}^{\infty} f(x) J_{\nu}(s x) x d x, \quad s \geq 0
-$$
-
-where $J_{\nu}$ is Bessel's function of order $\nu$ (see Section 9.6 for background on Bessel functions). Under certain conditions on $f$ (which we are going to assume hold) one can prove the inversion formula
-
-$$
-\mathcal{H}_{\nu} \mathcal{H}_{\nu} f=f .
-$$
-
-Thus the Hankel transform is its own inverse. This property is also shared by the cosine and sine transforms (see Exercise 21, Section 11.6). Indeed, there is a close connection between these transforms and the Hankel transform of order $\nu=\frac{1}{2}$ (see Exercise 16).
+
+# 9.4 The Hankel Transform with Applications
+
+As we saw in Chapter 12, Bessel functions and Bessel series are instrumental in solving problems in polar coordinates. It should not surprise you, then, to see Bessel functions arising in the treatment of similar problems over unbounded regions. Instead of Bessel series, here we will need a transform, defined in terms of Bessel functions as follows.
+
+> [!definition|b48a9f4a-3400-57df-8ff2-3eeb92b83146.local at=ee41df9f-d485-5be9-8726-a8ea110b03e7] Hankel Transform of Nonnegative Order
+> Suppose that $f(x)$ is defined for all $x \geq 0$. The Hankel transform of order $\nu \geq 0$ of $f(x)$ is given by
+>
+> $$
+> \mathcal{H}_{\nu}(f)(s)=\int_{0}^{\infty} f(x) J_{\nu}(s x) x d x, \quad s \geq 0
+> $$
+>
+> where $J_{\nu}$ is the Bessel function of the first kind of order $\nu$. 
+>
+> The integral is understood wherever it converges.
+
+*Printed equation label: (1).*
+
+> [!property|2169c6d6-8158-5aea-bb2e-9d3208b02910.local at=f2b86664-9a3f-5ec0-be6d-aa9e60b84377] Self-Inversion of the Hankel Transform
+> For $\nu\geq0$, write $\mathcal H_\nu f(s)=\int_0^\infty f(x)J_\nu(sx)x\,dx$. A sufficient condition below is that $f$ be smooth with compact support in $(0,\infty)$.
+>
+> Under certain conditions on $f$ (which we are going to assume hold) one can prove the inversion formula
+>
+> $$
+> \mathcal{H}_{\nu} \mathcal{H}_{\nu} f=f .
+> $$
+
+*Printed equation label: (2).*
+
+Thus the Hankel transform is its own inverse. This property is also shared by the cosine and sine transforms (see Exercise 21, Section 8.6). Indeed, there is a close connection between these transforms and the Hankel transform of order $\nu=\frac{1}{2}$ (see Exercise 16).
 
 The following operational properties are needed in the applications of this section:
 
-OPERATIONAL PROPERTIES
-
-$$
-\begin{aligned}
--s \mathcal{H}_{0}(f)(s) & =\mathcal{H}_{1}\left(f^{\prime}\right)(s) \\
-\mathcal{H}_{0}\left(f^{\prime}+\frac{1}{x} f\right)(s) & =s \mathcal{H}_{1}(f)(s) \\
-\mathcal{H}_{0}\left(f^{\prime \prime}+\frac{1}{x} f^{\prime}\right)(s) & =-s^{2} \mathcal{H}_{0}(f)(s)
-\end{aligned}
-$$
-
-For the proofs, we will need the following properties of Bessel functions from Section 9.7:
+> [!property|47710a13-e85e-55f2-9bad-b11d1a5c74c7.local at=f7827811-0a71-51e2-9ae5-721560f0f038] Hankel Transforms of First Derivatives and the Radial Laplacian
+> Write $\mathcal H_\nu f(s)=\int_0^\infty f(x)J_\nu(sx)x\,dx$. For $s>0$, assume the displayed integrals converge and integration by parts is valid. The boundary terms $xf(x)J_1(sx)$ vanish at both endpoints for the first formula; $xf(x)J_0(sx)$ vanish for the second; and $xf\,J_1(sx)$ and $xf^{\prime}(x)J_0(sx)$ vanish for the third. For example, smooth functions compactly supported inside $(0,\infty)$ satisfy these requirements.
+>
+> $$
+> \begin{aligned}
+> -s \mathcal{H}_{0}(f)(s) & =\mathcal{H}_{1}\left(f^{\prime}\right)(s) \\
+> \mathcal{H}_{0}\left(f^{\prime}+\frac{1}{x} f\right)(s) & =s \mathcal{H}_{1}(f)(s) \\
+> \mathcal{H}_{0}\left(f^{\prime \prime}+\frac{1}{x} f^{\prime}\right)(s) & =-s^{2} \mathcal{H}_{0}(f)(s)
+> \end{aligned}
+> $$
+
+*Printed equation labels: (3) transform $\mathcal H_1(f')$; (4) transform $\mathcal H_0(f'+f/x)$; (5) transform of the radial Laplacian.*
+
+For the proofs, we will need the following properties of Bessel functions from Section 12.7:
 
 $$
 \frac{d}{d x}\left(J_{0}(s x)\right)=-s J_{1}(s x) \quad \text { and } \quad \int J_{0}(s x) x d x=\frac{1}{s} x J_{1}(s x)+C
 $$
 
-We also assume the following conditions on $f$ : For any $s$,
+We also assume the following conditions on $f$ : For the second identity, require the following endpoint conditions. For the first and third identities use the corresponding $J_1$ and derivative conditions in the callout above. For any $s>0$,
 
 $$
 \lim _{x \rightarrow 0} f(x) J_{0}(s x) x=0 \quad \text { and } \quad \lim _{x \rightarrow \infty} f(x) J_{0}(s x) x=0 .
@@ -49,11 +65,11 @@
 & \mathcal{H}_{0}(f)(s)=\int_{0}^{\infty} f(x) J_{0}(s x) x d x \\
 & \left(u=f(x), d u=f^{\prime}(x) d x,\right. \\
 & \left.d v=J_{0}(s x) x d x, v=\frac{1}{s} x J_{1}(s x)\right) \\
-& =\left.\frac{1}{s} f(x) J_{0}(s x) x\right|_{0} ^{\infty}-\frac{1}{s} \underbrace{\int_{0}^{\infty} f^{\prime}(x) J_{1}(s x) x d x}_{\mathcal{H}_{1}\left(f^{\prime}\right)} .
+& =\left.\frac{1}{s} f(x) J_{1}(s x) x\right|_{0} ^{\infty}-\frac{1}{s} \underbrace{\int_{0}^{\infty} f^{\prime}(x) J_{1}(s x) x d x}_{\mathcal{H}_{1}\left(f^{\prime}\right)} .
 \end{aligned}
 $$
 
-By our assumption on $f$ the first term is zero, and (3) follows. The proof of $(4)$ is similar. First let us note that
+ With that boundary term zero, and (3) follows. The proof of $(4)$ is similar. First let us note that
 
 $$
 f^{\prime}+\frac{1}{x} f=\frac{1}{x} \frac{d}{d x}[x f(x)]
@@ -85,26 +101,46 @@
 
 The proof is simple and is left as an exercise. We are now in a position to treat some applications. We start with a hanging chain problem.
 
-## EXAMPLE 1 Oscillations of an infinitely long hanging chain
-
-The oscillations of a very long heavy chain can be modeled by assuming the chain is semi-infinite, with the fastened end sent to infinity. We will further assume that the transverse vibrations take place in one vertical plane. We place the chain on
-
-![](./images/68332ba3-9551-434a-a491-ce53af60160e-31_477_450_184_87.jpg)
-Figure 1 An infinite hanging chain, end fastened at $\infty$.
-
-![](./images/68332ba3-9551-434a-a491-ce53af60160e-31_394_476_1798_96.jpg)
-Figure 2 A heated large body.
-
-the $x$-axis, which we assume directed vertically and pointing upward (Figure 1). The boundary value problem governing the free motion of the chain becomes
-
-$$
-\begin{aligned}
-\frac{\partial^{2} u}{\partial t^{2}} & =g\left[x \frac{\partial^{2} u}{\partial x^{2}}+\frac{\partial u}{\partial x}\right], & & 0<x<\infty, \quad t>0 \\
-u(x, 0) & =f(x), & & u_{t}(x, 0)=v(x), x>0
-\end{aligned}
-$$
-
-Here $g$ is the gravitational acceleration, $f(x)$ is the initial displacement of the chain, and $v(x)$ is its initial velocity. To proceed with the solution, we make the change of variables $z^{2}=x, 2 z d z=d x$, and transform the equations into
+> [!exercise|dd5670df-bb96-5d13-92f1-2312a30bbdbd.local at=8047c9ea-b7a8-5b0d-84a8-c43b545588e4] EXAMPLE 1 Oscillations of an infinitely long hanging chain
+> The oscillations of a very long heavy chain can be modeled by assuming the chain is semi-infinite, with the fastened end sent to infinity. We will further assume that the transverse vibrations take place in one vertical plane. We place the chain on the $x$-axis, directed vertically and pointing upward (Figure 1).
+>
+>
+>
+> The boundary value problem governing the free motion of the chain becomes
+>
+> $$
+> \begin{aligned}
+> \frac{\partial^{2} u}{\partial t^{2}} & =g\left[x \frac{\partial^{2} u}{\partial x^{2}}+\frac{\partial u}{\partial x}\right], & & 0<x<\infty, \quad t>0 \\
+> u(x, 0) & =f(x), & & u_{t}(x, 0)=v(x), x>0
+> \end{aligned}
+> $$
+>
+> Here $g$ is the gravitational acceleration, $f(x)$ is the initial displacement of the chain, and $v(x)$ is its initial velocity. Find the transverse displacement $u(x,t)$ using the Hankel transform.
+
+*Printed equation label: (6).*
+
+
+
+
+
+```scientific-figure
+id: 54d443e3-b60e-4a7f-a634-0901f6516f8b
+numbered: false
+title: ""
+caption: Figure 1 An infinite hanging chain, end fastened at $\infty$.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 09 The Laplace and Hankel Transforms with Applications/images/68332ba3-9551-434a-a491-ce53af60160e-31_477_450_184_87.jpg
+    caption: ""
+```
+
+
+
+##### solution
+
+To proceed with the solution, we make the change of variables $z^{2}=x, 2 z d z=d x$, and transform the equations into
 
 $$
 \begin{aligned}
@@ -146,22 +182,37 @@
 u(x, t)=\int_{0}^{\infty}\left[A(s) \cos \left(\frac{\sqrt{g}}{2} s t\right)+B(s) \sin \left(\frac{\sqrt{g}}{2} s t\right)\right] J_{0}(\sqrt{x} s) s d s
 $$
 
-Numerical illustrations for the hanging chain problem are presented in the exercises. Our next example is a Dirichlet problem in the upper half-space.
-
-## EXAMPLE 2 Steady-state temperature in a large body
-
-Solve the boundary value problem in cylindrical coordinates
-
-$$
-\begin{aligned}
-(\Delta u=) u_{r r}+\frac{1}{r} u_{r}+u_{z z} & =0, \quad r>0, z>0 \\
--c^{2} u_{z}(r, 0) & = \begin{cases}k & \text { if } 0<r<R \\
-0 & \text { if } r>R\end{cases}
-\end{aligned}
-$$
-
-This boundary value problem models the steady-state temperature distribution in a very large body in the upper half-space, with one of its sides placed on the plane $z=0$ (Figure 2). Heat is introduced in the body at a constant rate $k$ per unit area per unit time through a circular area of radius $R$, centered at the origin, in the plane $z=0$, and the rest of this plane is unheated. Because of circular symmetry, the steady-state temperature at a point in the upper half-space is a function of $r$ and $z$ only.
-Solution We write $U(s, z)$ for the Hankel transform of order 0 of $u(r, z)$ with respect to $r$. Transforming the equations, using (5) and the first entry of Table 1 below, we get
+Numerical illustrations for the hanging chain problem are presented in the exercises. Our next example is a Neumann problem in the upper half-space.
+
+> [!exercise|31d146d8-eccd-5b4f-b73e-18555fa7d282.local at=52912bec-7477-503f-8adb-528d112651f4] EXAMPLE 2 Steady-state temperature in a large body
+> Find the solution regular at the axis and tending to zero at spatial infinity of the boundary value problem in cylindrical coordinates
+>
+> $$
+> \begin{aligned}
+> (\Delta u=) u_{r r}+\frac{1}{r} u_{r}+u_{z z} & =0, \quad r>0, z>0 \\
+> -c^{2} u_{z}(r, 0) & = \begin{cases}k & \text { if } 0<r<R \\
+> 0 & \text { if } r>R\end{cases}
+> \end{aligned}
+> $$
+>
+> This boundary value problem models the steady-state temperature distribution in a very large body in the upper half-space, with one of its sides placed on the plane $z=0$ (Figure 2). Heat is introduced in the body at a constant rate $k$ per unit area per unit time through a circular area of radius $R$, centered at the origin, in the plane $z=0$, and the rest of this plane is unheated. Because of circular symmetry, the steady-state temperature at a point in the upper half-space is a function of $r$ and $z$ only.
+
+```scientific-figure
+id: 3acb8ebf-2abf-44be-acd6-2d6572625c63
+numbered: false
+title: ""
+caption: Figure 2 A heated large body.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 09 The Laplace and Hankel Transforms with Applications/images/68332ba3-9551-434a-a491-ce53af60160e-31_394_476_1798_96.jpg
+    caption: ""
+```
+
+##### solution
+
+We write $U(s, z)$ for the Hankel transform of order 0 of $u(r, z)$ with respect to $r$. Transforming the equations, using (5) and the first entry of Table 1 below, we get
 
 $$
 \begin{gathered}
@@ -176,7 +227,7 @@
 U(s, z)=A(s) e^{-s z}+B(s) e^{s z}
 $$
 
-Expecting the transform to remain bounded, we take $U(s, z)=A(s) e^{-s z}$. To determine $A(s)$, we use the transformed boundary condition and get
+For $s>0$, requiring the transformed solution to decay as $z\to\infty$, we take $U(s, z)=A(s) e^{-s z}$. To determine $A(s)$, we use the transformed boundary condition and get
 
 $$
 \begin{aligned}
@@ -198,87 +249,161 @@
 \mathcal{H}_{0}\left(\frac{a}{x} J_{1}(a x)\right)=\mathcal{U}_{0}(a-s) .
 $$
 
-Note the interesting fact that the function $e^{-x^{2} / 2}$ is its own Hankel transform. (Compare with Example 5, Section 11.1.)
-
-|  | $f(x), \quad x \geq 0$ | $\mathcal{H}_{0}(f)(s)=\int_{0}^{\infty} f(x) J_{0}(s x) x d x, \quad s \geq 0$ |
-| :--- | :--- | :--- |
-| 1. | $\mathcal{U}_{0}(a-x), a>0$ | $\frac{a}{s} J_{1}(a s)$ |
-| 2. | $x^{2 N} \mathcal{U}_{0}(a-x), a>0$ | $\sum_{n=0}^{N}(-1)^{n} 2^{n} a^{2 N-n+1} \frac{N!}{(N-n)!} \frac{J_{n+1}(a s)}{s^{n+1}}$ |
-| 3. | $\frac{1}{x}$ | $\frac{1}{s}$ |
-| 4. | $e^{-a x}, a>0$ | $\frac{a}{\sqrt{\left(s^{2}+a^{2}\right)^{3}}}$ |
-| 5. | $\frac{1}{x} e^{-a x}, a>0$ | $\frac{1}{\sqrt{s^{2}+a^{2}}}$ |
-| 6. | $e^{-a^{2} x^{2}}, a>0$ | $\frac{1}{2 a^{2}} e^{-s^{2} / 4 a^{2}}$ |
-| 7. | $\frac{1}{x} \sin a x, a>0$ | $\frac{U_{0}(a-s)}{\sqrt{a^{2}-s^{2}}}$ |
-
-Table 1 Hankel Transforms of order 0.
-
-## Exercises 12.4
-
-1. Let $z^{2}=x$, and let $\tilde{u}(z, t)=u\left(z^{2}, t\right)=u(x, t)$.
-(a) Use the chain rule to obtain
-
-$$
-u_{x}=\frac{1}{2 z} \tilde{u}_{z} ; \quad u_{x x}=\frac{1}{4 z^{2}} \tilde{u}_{z z}-\frac{1}{4 z^{3}} \tilde{u}_{z}
-$$
-
-(b) Refer to Example 1 and justify the derivation of the new differential equation from (6).
-
-In Exercises 2-3, use (1) and various properties of Bessel functions found in Sections 9.6 and 9.7 to establish the following identities. Take $\nu \geq 0$ and $a>0$.
-2. $\mathcal{H}_{\nu}(f(a x))(s)=\frac{1}{a^{2}} \mathcal{H}_{\nu}(f(x))\left(\frac{s}{a}\right)$.
-3. $\mathcal{H}_{\nu}\left[\frac{1}{x} f\right](s)=\frac{s}{2 \nu}\left[\mathcal{H}_{\nu+1}(f)(s)+\mathcal{H}_{\nu-1}(f)(s)\right]$
-4. (a) Use properties of Bessel functions to prove that, for $a>0$,
-
-$$
-\mathcal{H}_{\nu}\left[x^{\nu} \mathcal{U}_{0}(a-x)\right]=\frac{a^{\nu+1}}{s} J_{\nu+1}(a s) .
-$$
-
-(b) Deduce entry 1 of Table 1.
-5. Use Exercise 9 of Section 9.3 to derive entry 2 of Table 1.
-6. (a) Show that $\mathcal{H}_{0}\left(\frac{1}{x} e^{-a x}\right)=\mathcal{L}\left(J_{0}(a x)\right)(s)$.
-(b) Obtain entry 5 of Table 1 from the table of Laplace transforms.
-7. Justify entry 3 of Table 1 by letting $a \rightarrow 0$ in entry 5 .
-8. In this exercise we outline a proof of entry 6 of Table 1.
-(a) Use the series expansion of $J_{0}$ and obtain that
-
-$$
-\mathcal{H}_{0}\left(e^{-a^{2} x^{2}}\right)(s)=\frac{1}{2 a^{2}} \sum_{n=0}^{\infty}\left[\frac{(-1)^{n}}{(n!)^{2}}\left(\frac{s^{2}}{4 a^{2}}\right)^{n} \int_{0}^{\infty} t^{n} e^{-t} d t\right]
-$$
-
-(b) Use the gamma function to show that the integral in the sum is $n$ !,
-(c) Complete the proof by comparing the series with the Taylor series expansion of $\frac{1}{2 a^{2}} e^{-s^{2} / 4 a^{2}}$.
-9. (a) Refer to Example 1 and describe the physical phenomenon corresponding to the data $g=9.8, f(x)=0, v(x)=\frac{1}{\sqrt{x}}$.
-(b) Write down the solution in the form of an integral.
-(c) Take $x=1$ and approximate the solution when $t=.1, .2, .3$.
-10. Repeat Exercise 9 for the data $g=9.8, f(x)=\frac{1}{x}, v(x)=0$.
-11. Approximate the steady state temperature $u(1,1)$ in Example 2, given the numerical data: $R=2, k=.5, c=.8$.
-12. Transverse vibrations of a large sheet of metal. A very large sheet of metal vibrates under the action of radially symmetric pressure exerted at its surface. The boundary value problem in polar coordinates is described as follows
-
-$$
-\begin{aligned}
-u_{t t} & =c^{2}\left(u_{r r}+\frac{1}{r} u_{r}\right)+p(r, t), & & r>0, t>0 \\
-u(r, 0) & =f(r), \quad u_{t}(r, 0)=g(r), & & r>0
-\end{aligned}
-$$
-
-where $p(r, t)$ corresponds to the outside pressure divided by the surface mass density of the sheet, $f$ is the radially symmetric initial shape of the sheet, and $g$ its radially symmetric initial velocity.
-
-Show that the Hankel transform of order 0 (with respect to $r$ ) of the solution, $U(s, t)$, satisfies
-
-$$
-\begin{aligned}
-U_{t t} & =-c^{2} s^{2} U+P(s, t) \\
-U(s, 0) & =F(s), \quad U_{t}(s, 0)=G(s)
-\end{aligned}
-$$
-
-13. Refer to Exercise 12. Show that if the pressure is 0 , then the Hankel transform of the solution is
-
-$$
-U(s, t)=F(s) \cos (c s t)+\frac{1}{c s} G(s) \sin (c s t)
-$$
-
-14. Do Exercise 12 with $c=1, p \equiv 0, f(r)=\left(1-r^{2}\right) \mathcal{U}_{0}(1-r), g(r)=0$.
-15. (a) Do Exercise 12 with $c=1, p \equiv 0, f(r)=\sqrt{1-r^{2}} u_{0}(1-r), g(r)=0$.
-(b) Plot the initial shape of the membrane at various values of $t$.
-(c) Discuss the motion of the point at the origin.
-16. Recalling from Section 9.6 that $J_{1 / 2}(x)=\sqrt{\frac{2}{\pi x}} \sin x$, show that $\mathcal{H}_{1 / 2}(f)= \frac{1}{\sqrt{s}} \mathcal{F}_{s}(f(x) \sqrt{x})$, where $\mathcal{F}_{s}$ is the Fourier sine transform. Argue from the fact that $\mathcal{F}_{s}$ is its own inverse transform that $\mathcal{H}_{1 / 2}$ is its own inverse transform.
+Note the interesting fact that the function $e^{-x^{2} / 2}$ is its own Hankel transform. (Compare with Example 5, Section 8.1.)
+
+```scientific-table
+id: df449b5c-dab5-455e-ae70-a82191fd23b7
+numbered: false
+title: ""
+caption: Table 1. Hankel transforms of order zero. Take $N$ to be a nonnegative integer and $s>0$ for rows containing $1/s$, with limits at zero where finite. In row 7 the value is $1/\sqrt{a^2-s^2}$ for $0\leq s<a$ and zero for $s>a$; $s=a$ is excluded. Discontinuous inverse data take midpoint values at jumps.
+captionVisible: true
+captionPosition: below
+rows:
+  - - text: ""
+    - text: $f(x), \quad x \geq 0$
+    - text: $\mathcal{H}_{0}(f)(s)=\int_{0}^{\infty} f(x) J_{0}(s x) x d x, \quad s \geq 0$
+  - - text: "1."
+    - text: $\mathcal{U}_{0}(a-x), a>0$
+    - text: $\frac{a}{s} J_{1}(a s)$
+  - - text: "2."
+    - text: $x^{2 N} \mathcal{U}_{0}(a-x), a>0$
+    - text: $\sum_{n=0}^{N}(-1)^{n} 2^{n} a^{2 N-n+1} \frac{N!}{(N-n)!} \frac{J_{n+1}(a s)}{s^{n+1}}$
+  - - text: "3."
+    - text: $\frac{1}{x}$
+    - text: $\frac{1}{s}$
+  - - text: "4."
+    - text: $e^{-a x}, a>0$
+    - text: $\frac{a}{\sqrt{\left(s^{2}+a^{2}\right)^{3}}}$
+  - - text: "5."
+    - text: $\frac{1}{x} e^{-a x}, a>0$
+    - text: $\frac{1}{\sqrt{s^{2}+a^{2}}}$
+  - - text: "6."
+    - text: $e^{-a^{2} x^{2}}, a>0$
+    - text: $\frac{1}{2 a^{2}} e^{-s^{2} / 4 a^{2}}$
+  - - text: "7."
+    - text: $\frac{1}{x} \sin a x, a>0$
+    - text: $\frac{U_{0}(a-s)}{\sqrt{a^{2}-s^{2}}}$
+headerRows: 1
+rowHeaders: true
+style: scientific
+```
+
+
+## Exercises 9.4
+
+
+> [!exercise|19f4dd2e-6a35-5d9f-8395-3db0b94bce45.local at=60659655-2933-5157-98ab-4bfcd27ed77a] Exercise 1
+> Let $z^{2}=x$, and let $\tilde{u}(z, t)=u\left(z^{2}, t\right)=u(x, t)$.
+> (a) Use the chain rule to obtain
+>
+> $$
+> u_{x}=\frac{1}{2 z} \tilde{u}_{z} ; \quad u_{x x}=\frac{1}{4 z^{2}} \tilde{u}_{z z}-\frac{1}{4 z^{3}} \tilde{u}_{z}
+> $$
+>
+> (b) Refer to Example 1 and justify the derivation of the new differential equation from (6).
+
+
+> [!prompt|899ffbaa-c1ca-5a8f-aa2e-9af1186233cc.local at=42106886-0228-54ec-a32d-2afc98503ec1] Shared exercise instructions
+> In Exercises 2-3, use (1) and various properties of Bessel functions found in Sections 12.6 and 12.7 to establish the following identities. Take $a>0$, $\nu\geq0$ in Exercise 2, and $\nu>0$ in Exercise 3. Assume convergence of the relevant transforms.
+
+
+
+> [!exercise|5ea42c42-e694-54ad-bb53-c54c62fdab1d.local at=f84d856f-6d64-538b-b9a7-b8f261f42e8c] Exercise 2
+> $\mathcal{H}_{\nu}(f(a x))(s)=\frac{1}{a^{2}} \mathcal{H}_{\nu}(f(x))\left(\frac{s}{a}\right)$.
+
+
+> [!exercise|3c9d81de-271d-5e2f-8f8d-004fc98b272a.local at=ec70c770-661c-5c8b-9615-c00fc0efaa71] Exercise 3
+> $\mathcal{H}_{\nu}\left[\frac{1}{x} f\right](s)=\frac{s}{2 \nu}\left[\mathcal{H}_{\nu+1}(f)(s)+\mathcal{H}_{\nu-1}(f)(s)\right]$
+
+
+> [!exercise|2eaa07d9-342a-5ed2-8739-c8f9c93c6e4e.local at=8d6740ca-970c-57e3-9514-11af5340a9b3] Exercise 4
+> (a) Use properties of Bessel functions to prove that, for $a>0$,
+>
+> $$
+> \mathcal{H}_{\nu}\left[x^{\nu} \mathcal{U}_{0}(a-x)\right]=\frac{a^{\nu+1}}{s} J_{\nu+1}(a s) .
+> $$
+>
+> (b) Deduce entry 1 of Table 1.
+
+
+> [!exercise|c8740961-321b-57ac-bade-b62109482c37.local at=562e2310-ee89-5641-905c-cd080d82906d] Exercise 5
+> Use Exercise 9 of Section 12.3 to derive entry 2 of Table 1.
+
+
+> [!exercise|debd43e6-79a7-55e9-9fe0-05e3f18f2a0a.local at=d5bc9f52-70b4-5a17-bc28-4ccdc178784b] Exercise 6
+> (a) Show that $\mathcal{H}_{0}\left(\frac{1}{x} e^{-a x}\right)=\mathcal{L}\left(J_{0}(a x)\right)(s)$.
+> (b) Obtain entry 5 of Table 1 from the table of Laplace transforms.
+
+
+> [!exercise|40d7a861-bdfd-5b5b-9691-5476e73ae28b.local at=104b24ca-0283-5f9c-8fd0-c64a4a9ae93a] Exercise 7
+> Justify entry 3 of Table 1 by letting $a \rightarrow 0$ in entry 5 .
+
+
+> [!exercise|3e5a987a-3d5f-56e8-a2fa-0e20a275decf.local at=1c283319-bc33-5ead-8b63-20e98e3ad45b] Exercise 8
+> In this exercise we outline a proof of entry 6 of Table 1.
+> (a) Use the series expansion of $J_{0}$ and obtain that
+>
+> $$
+> \mathcal{H}_{0}\left(e^{-a^{2} x^{2}}\right)(s)=\frac{1}{2 a^{2}} \sum_{n=0}^{\infty}\left[\frac{(-1)^{n}}{(n!)^{2}}\left(\frac{s^{2}}{4 a^{2}}\right)^{n} \int_{0}^{\infty} t^{n} e^{-t} d t\right]
+> $$
+>
+> (b) Use the gamma function to show that the integral in the sum is $n$ !,
+> (c) Complete the proof by comparing the series with the Taylor series expansion of $\frac{1}{2 a^{2}} e^{-s^{2} / 4 a^{2}}$.
+
+
+> [!exercise|6e249f84-10a3-5900-b0ba-7b45c378115b.local at=5074c357-8067-5e81-b1ce-923b1e19ee61] Exercise 9
+> (a) Refer to Example 1 and describe the physical phenomenon corresponding to the data $g=9.8, f(x)=0, v(x)=\frac{1}{\sqrt{x}}$.
+> (b) Write down the solution in the form of an integral.
+> (c) Take $x=1$ and approximate the solution when $t=.1, .2, .3$.
+
+
+> [!exercise|db21e2ab-b8c6-5f27-891f-5edf5fb1f1cd.local at=d999a123-d49b-5b77-8bd2-1631ca0a4210] Exercise 10
+> Repeat Exercise 9 for the data $g=9.8, f(x)=\frac{1}{x}, v(x)=0$. 
+
+
+> [!exercise|b395428c-7adb-5a28-bf82-af8abfe07af0.local at=595c272e-9dc6-5575-a127-b2b2865e52e0] Exercise 11
+> Approximate the steady state temperature $u(1,1)$ in Example 2, given the numerical data: $R=2, k=.5, c=.8$.
+
+
+> [!exercise|e8681890-3a12-57d0-9345-b83ff393c391.local at=d16eae94-b20b-5db1-ac67-6627d48fe145] Exercise 12
+> Transverse vibrations of a large sheet of metal. A very large sheet of metal vibrates under the action of radially symmetric pressure exerted at its surface. The boundary value problem in polar coordinates is described as follows
+>
+> $$
+> \begin{aligned}
+> u_{t t} & =c^{2}\left(u_{r r}+\frac{1}{r} u_{r}\right)+p(r, t), & & r>0, t>0 \\
+> u(r, 0) & =f(r), \quad u_{t}(r, 0)=g(r), & & r>0
+> \end{aligned}
+> $$
+>
+> where $p(r, t)$ corresponds to the outside pressure divided by the surface mass density of the sheet, $f$ is the radially symmetric initial shape of the sheet, and $g$ its radially symmetric initial velocity.
+>
+> Show that the Hankel transform of order 0 (with respect to $r$ ) of the solution, $U(s, t)$, satisfies
+>
+> $$
+> \begin{aligned}
+> U_{t t} & =-c^{2} s^{2} U+P(s, t) \\
+> U(s, 0) & =F(s), \quad U_{t}(s, 0)=G(s)
+> \end{aligned}
+> $$
+
+
+> [!exercise|5898185f-17ec-596c-8cad-fcd6a348283f.local at=80f4aac2-a187-5d77-a367-e5934945399e] Exercise 13
+> Refer to Exercise 12. Show that if the pressure is 0 , then the Hankel transform of the solution is
+>
+> $$
+> U(s, t)=F(s) \cos (c s t)+\frac{1}{c s} G(s) \sin (c s t)
+> $$
+
+
+> [!exercise|0901d27e-e543-5858-bb37-6fab08a63c72.local at=907b4243-f47d-5f8e-a2a7-e3486f7f74e0] Exercise 14
+> Do Exercise 12 with $c=1, p \equiv 0, f(r)=\left(1-r^{2}\right) \mathcal{U}_{0}(1-r), g(r)=0$.
+
+
+> [!exercise|6beadd6b-d02e-5b4b-82e0-ea8c3d333ba1.local at=ca7137ca-8e18-56f8-9e50-cb125b6c3035] Exercise 15
+> (a) Do Exercise 12 with $c=1$, $p\equiv0$, $g(r)=0$, and $f(r)=\sqrt{1-r^2}$ for $0\leq r\leq1$, zero for $r>1$.
+> (b) Plot the shape of the membrane at various values of $t$.
+> (c) Discuss the motion of the point at the origin.
+
+
+> [!exercise|4302caea-c879-5408-ba8f-39b367a3ed5f.local at=7d73eb75-d627-5a78-b6c4-1f95ba926884] Exercise 16
+> Recalling from Section 12.7 that $J_{1 / 2}(x)=\sqrt{\frac{2}{\pi x}} \sin x$, show that $\mathcal{H}_{1 / 2}(f)= \frac{1}{\sqrt{s}} \mathcal{F}_{s}(f(x) \sqrt{x})$, where $\mathcal{F}_{s}$ is the Fourier sine transform. Argue from the fact that $\mathcal{F}_{s}$ is its own inverse transform that $\mathcal{H}_{1 / 2}$ is its own inverse transform.

`````
