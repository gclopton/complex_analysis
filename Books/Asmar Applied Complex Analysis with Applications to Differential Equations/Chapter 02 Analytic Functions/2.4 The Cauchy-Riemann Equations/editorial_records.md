
# Editorial records

Reading note: 2.4 The Cauchy-Riemann Equations.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Callout 60: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!equation] Cauchy–Riemann Equations
> For $f(x+iy)=u(x,y)+iv(x,y)$ with real-valued $u,v$, the Cauchy–Riemann equations are
>
> $$
> \frac{\partial u}{\partial x}=\frac{\partial v}{\partial y} \quad \text { and } \quad \frac{\partial u}{\partial y}=-\frac{\partial v}{\partial x}
> $$
````
### After

````text
> [!equation] The Cauchy-Reimann Equations
> For $f(x+iy)=u(x,y)+iv(x,y)$ with real-valued $u,v$, the Cauchy–Riemann equations are
>
> $$
> \frac{\partial u}{\partial x}=\frac{\partial v}{\partial y} \quad \text { and } \quad \frac{\partial u}{\partial y}=-\frac{\partial v}{\partial x}
> $$
````

## 2. Callout 61: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Cauchy–Riemann Criterion for Analyticity
> The function $f(z)=u(x, y)+i v(x, y)$ is analytic in an open set $S$ if and only if the partial derivatives of $u$ and $v$ are continuous and satisfy the Cauchy-Riemann equations
>
> $$
> u_{x}=v_{y} \quad \text { and } \quad u_{y}=-v_{x} .
> $$
>
> The derivative $f^{\prime}(z)$ is given as either of
>
> $$
> f^{\prime}(z)=u_{x}(x, y)+i v_{x}(x, y) \text { or } f^{\prime}(z)=v_{y}(x, y)-i u_{y}(x, y) .
> $$
````
### After

````text
> [!theorem] The Cauchy-Reimann Equations
> The function $f(z)=u(x, y)+i v(x, y)$ is analytic in an open set $S$ if and only if the partial derivatives of $u$ and $v$ are continuous and satisfy the Cauchy-Riemann equations
>
> $$
> u_{x}=v_{y} \quad \text { and } \quad u_{y}=-v_{x} .
> $$
>
> The derivative $f^{\prime}(z)$ is given as either of
>
> $$
> f^{\prime}(z)=u_{x}(x, y)+i v_{x}(x, y) \text { or } f^{\prime}(z)=v_{y}(x, y)-i u_{y}(x, y) .
> $$
````

## Source-to-current comparison

Source: /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 02 Analytic Functions/2.4 The Cauchy-Riemann Equations.md

This exact comparison preserves the full change evidence, including formatting, OCR corrections, restored source wording, and required standalone context. The entries above explain the recovery edits. The comparison is not a claim that every difference is a correction; component serialization, callout wrapping, and printed labels outside callouts are formatting.

`````diff
--- /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 02 Analytic Functions/2.4 The Cauchy-Riemann Equations.md
+++ /Users/gradyclopton/ObsidianVaults/complex_analysis/Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 02 Analytic Functions/2.4 The Cauchy-Riemann Equations.md
@@ -208,10 +208,18 @@
 
 
 
-> [!figure] Figure 1
-> 
-> ![](./images/af4f9593-dec7-4bc0-8d78-d25500419ec9-28_512_557_1699_86.jpg)
-> Figure 1 For $z$ approaching $z_{0}$ in the direction of the $x$ axis, $\Delta z=\Delta x$.
+```scientific-figure
+id: 92915684-9dc1-471e-9e2c-9aab71314290
+numbered: false
+title: ""
+caption: "**Figure 1.** For $z$ approaching $z_{0}$ in the direction of the $x$ axis, $\\Delta z=\\Delta x$."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 02 Analytic Functions/images/af4f9593-dec7-4bc0-8d78-d25500419ec9-28_512_557_1699_86.jpg
+    caption: ""
+```
 
 
 
@@ -230,10 +238,18 @@
 where in the last step we have used $1 / i=-i$ and rearranged the terms. 
 
 
-> [!figure] Figure 2
-> 
-> ![](./images/af4f9593-dec7-4bc0-8d78-d25500419ec9-29_492_505_394_101.jpg)
-> Figure 2 For $z$ approaching $z_{0}$ in the direction of the $y$ axis, $\Delta z=i \Delta y$.
+```scientific-figure
+id: 6daad326-2745-4297-9b39-1310bad76f93
+numbered: false
+title: ""
+caption: "**Figure 2.** For $z$ approaching $z_{0}$ in the direction of the $y$ axis, $\\Delta z=i \\Delta y$."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 02 Analytic Functions/images/af4f9593-dec7-4bc0-8d78-d25500419ec9-29_492_505_394_101.jpg
+    caption: ""
+```
 
 
 
@@ -245,12 +261,13 @@
 
 which is this time an expression of the derivative of $f$ in terms of the partial derivatives with respect to $y$ of $u$ and $v$. Now comes the startling result. Equate real and imaginary parts in (3) and (5) and get
 
+<!-- Source label: The Cauchy-Reimann Equations -->
 > [!equation] The Cauchy-Reimann Equations
-> 
+> For $f(x+iy)=u(x,y)+iv(x,y)$ with real-valued $u,v$, the Cauchy–Riemann equations are
+>
 > $$
 > \frac{\partial u}{\partial x}=\frac{\partial v}{\partial y} \quad \text { and } \quad \frac{\partial u}{\partial y}=-\frac{\partial v}{\partial x}
 > $$
-> 
 
 Thus, in order for $f$ to be analytic, $u$ and $v$ must satisfy the Cauchy-Riemann equations. Moreover, since $f$ is analytic, $f^{\prime}$ is continuous, and it follows from (3) and (5) and Theorem 4(iv), Section 2.2, that $\frac{\partial u}{\partial x}, \frac{\partial v}{\partial x}, \frac{\partial u}{\partial y}$, and $\frac{\partial v}{\partial y}$ are all continuous. The converse of these statements is also true. In applications, we will need the converse, since to establish the analyticity of a function, it is often easier to check the Cauchy-Riemann equations and the continuity of the partial derivatives. Because the proof of the converse requires advanced topics from calculus of several variables, we postpone it until Section 2.6, where it will be treated in detail. Let us now summarize our discussion
 and proceed with the applications. To simplify the notation, we will denote partial derivatives with subscripts, $\frac{\partial u}{\partial x}=u_{x}, \frac{\partial u}{\partial y}=u_{y}$, and so on.
@@ -326,20 +343,19 @@
 
 
 
-> [!theorem] Theorem 1: The Cauchy-Reimann Equations
+<!-- Source label: Theorem 1: The Cauchy-Reimann Equations -->
+> [!theorem] The Cauchy-Reimann Equations
 > The function $f(z)=u(x, y)+i v(x, y)$ is analytic in an open set $S$ if and only if the partial derivatives of $u$ and $v$ are continuous and satisfy the Cauchy-Riemann equations
-> (7)
-> 
+>
 > $$
 > u_{x}=v_{y} \quad \text { and } \quad u_{y}=-v_{x} .
 > $$
-> 
+>
 > The derivative $f^{\prime}(z)$ is given as either of
-> 
+>
 > $$
 > f^{\prime}(z)=u_{x}(x, y)+i v_{x}(x, y) \text { or } f^{\prime}(z)=v_{y}(x, y)-i u_{y}(x, y) .
 > $$
-> 
 
 The Cauchy-Riemann equations appeared in 1821 in the early work of Cauchy on integrals of complex-valued functions. Their connection to the existence of the derivative, as stated in Theorem 1, appeared in 1851 in the doctoral dissertation of the great German mathematician, Bernhard Riemann (1826-1866). As it should be obvious to any one who has studied calculus, Riemann's work shaped the development of modern calculus. His study of complex functions was motivated by his work in hydrodynamics, fluid flow and other applied problems. Some of these applications and their connection to the Cauchy-Riemann equations will be explored in the following section and Chapter 6.
 
@@ -1286,7 +1302,8 @@
 The final applications show how the Cauchy-Riemann equations can be used to derive important results of theoretical nature.
 
 
-> [!theorem] Theorem 2
+<!-- Source label: Theorem 2 -->
+> [!theorem] Zero Complex Derivative Implies Constancy on a Region
 > Suppose that $f(z)=u(x, y)+i v(x, y)$ is analytic in a region (open and connected) $\Omega$ and $f^{\prime}(z)=0$ for all $z$ in $\Omega$. Then $f$ is constant in $\Omega$.
 
 
@@ -1304,14 +1321,23 @@
 
 
 
-> [!figure] Figure 3
-> 
-> ![](./images/af4f9593-dec7-4bc0-8d78-d25500419ec9-33_492_505_1222_112.jpg)
-> Figure 3 A nonconstant function with zero derivative. Its domain of definition is the nonconnected shaded area.
-
-
-
-> [!corollary] Corollary 3 
+```scientific-figure
+id: a6870bad-89a9-4727-8f69-ecf8b5568b5e
+numbered: false
+title: ""
+caption: "**Figure 3.** A nonconstant function with zero derivative. Its domain of definition is the nonconnected shaded area."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 02 Analytic Functions/images/af4f9593-dec7-4bc0-8d78-d25500419ec9-33_492_505_1222_112.jpg
+    caption: ""
+```
+
+
+
+<!-- Source label: Corollary 3  -->
+> [!corollary] Analytic Functions with Equal Real or Imaginary Parts Differ by a Constant
 > Suppose that $f$ and $g$ are analytic in a region $\Omega$. If either $\operatorname{Re} f=\operatorname{Re} g$ on $\Omega$ or $\operatorname{Im} f=\operatorname{Im} g$ on $\Omega$, then $f(z)=g(z)+c$ on $\Omega$, where $c$ is a constant.
 
 

`````
