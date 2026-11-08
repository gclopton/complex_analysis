
# Editorial records

Reading note: 2.6 Differentiation of Functions of Several Variables.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Callout 70: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!definition] Total Differentiability of a Real Function of Two Variables
> We call a real-valued function $u(x, y)$ differentiable at $z_{0}=\left(x_{0}, y_{0}\right)$ if it can be written in the form
>
> $$
> u(z)=u\left(z_{0}\right)+A\left(x-x_{0}\right)+B\left(y-y_{0}\right)+\epsilon(z)\left|z-z_{0}\right|
> $$
>
> where $A$ and $B$ are (real) constants and $\epsilon(z) \rightarrow 0$ as $z \rightarrow z_{0}$.
````
### After

````text
> [!definition] Differentiability of Real-Valued Functions of Two Variables
> We call a real-valued function $u(x, y)$ differentiable at $z_{0}=\left(x_{0}, y_{0}\right)$ if it can be written in the form
>
> $$
> u(z)=u\left(z_{0}\right)+A\left(x-x_{0}\right)+B\left(y-y_{0}\right)+\epsilon(z)\left|z-z_{0}\right|
> $$
>
> where $A$ and $B$ are (real) constants and $\epsilon(z) \rightarrow 0$ as $z \rightarrow z_{0}$.
````

## 2. Callout 72: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Differentiability from Partial Derivatives and One Continuous Partial
> Let $u$ be a real-valued function defined on a neighborhood of $z_{0}$. If
> (i) $u_{x}\left(z_{0}\right)$ and $u_{y}\left(z_{0}\right)$ exist, and
> (ii) at least one of $u_x$ and $u_y$ exists in a neighborhood of $z_0$ and is continuous at $z_0$,
> then $u$ is differentiable at $z_{0}$, its differential is $du=u_x(x_0,y_0)\,dx+u_y(x_0,y_0)\,dy$.
````
### After

````text
> [!theorem] Sufficient Conditions for Differentiability
> Let $u$ be a real-valued function defined on a neighborhood of $z_{0}$. If
> (i) $u_{x}\left(z_{0}\right)$ and $u_{y}\left(z_{0}\right)$ exist, and
> (ii) either $u_{x}(z)$ or $u_{y}(z)$ is continuous at $z_{0}$,
> then $u$ is differentiable at $z_{0}$, and $u(z)=u(z_0)+A(x-x_0)+B(y-y_0)+o(|z-z_0|)$ with $A=u_{x}\left(x_{0}, y_{0}\right), B= u_{y}\left(x_{0}, y_{0}\right)$.
````

## 3. Callout 73: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Continuous Cauchy–Riemann Partials Imply Analyticity
> Let $f(z)=u(x, y)+i v(x, y)$ be a complex-valued function, defined in an open set $S$. If $u_{x}, u_{y}, v_{x}$, and $v_{y}$ are continuous and satisfy the Cauchy–Riemann equations in $S$, then $f(z)$ is analytic on $S$.
````
### After

````text
> [!theorem] The Chain Rule
> Let $f(z)=u(x, y)+i v(x, y)$ be a complex-valued function, defined in an open set $S$. If $u_{x}, u_{y}, v_{x}$, and $v_{y}$ are continuous and satisfy the Cauchy–Riemann equations in $S$, then $f(z)$ is analytic on $S$.
````

## 4. Callout 74: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Chain Rule along a Differentiable Plane Curve
> Assume the curve $(x(t),y(t))$ lies in $S$.
>
> Suppose that $u(x, y)$ is a differentiable function of $(x, y)$ in an open set $S$, where $x=x(t)$ and $y=y(t)$ are both differentiable functions of $t$. Then the function $U(t)=u(x(t), y(t))$ is a differentiable function of $t$ and
>
> $$
> \frac{d U}{d t}=\frac{\partial u}{\partial x} \frac{d x}{d t}+\frac{\partial u}{\partial y} \frac{d y}{d t}
> $$
````
### After

````text
> [!theorem] The Chain Rule
> Assume the curve $(x(t),y(t))$ lies in $S$.
>
> Suppose that $u(x, y)$ is a differentiable function of $(x, y)$ in an open set $S$, where $x=x(t)$ and $y=y(t)$ are both differentiable functions of $t$. Then the function $U(t)=u(x(t), y(t))$ is a differentiable function of $t$ and
>
> $$
> \frac{d U}{d t}=\frac{\partial u}{\partial x} \frac{d x}{d t}+\frac{\partial u}{\partial y} \frac{d y}{d t}
> $$
````

## 5. Callout 75: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Mean Value Theorem along a Line Segment in the Plane
> Suppose $u(x, y)$ is a differentiable real-valued function of ( $x, y$ ) in an open set $S$. Suppose that the line segment $\left[z_1, z_2\right]$ joining $z_1=\left(x_1, y_1\right)$ to $z_2=\left(x_2, y_2\right)$ lies entirely in $S$. Then there exists a point $\zeta$ on $\left[z_1, z_2\right]$ such that
>
> $$
> u\left(z_2\right)-u\left(z_1\right)=u_x(\zeta)\left(x_2-x_1\right)+u_y(\zeta)\left(y_2-y_1\right)
> $$
````
### After

````text
> [!theorem] The Mean Value Theorem in Two Dimensions
> Suppose $u(x, y)$ is a differentiable real-valued function of ( $x, y$ ) in an open set $S$. Suppose that the line segment $\left[z_1, z_2\right]$ joining $z_1=\left(x_1, y_1\right)$ to $z_2=\left(x_2, y_2\right)$ lies entirely in $S$. Then there exists a point $\zeta$ on $\left[z_1, z_2\right]$ such that
>
> $$
> u\left(z_2\right)-u\left(z_1\right)=u_x(\zeta)\left(x_2-x_1\right)+u_y(\zeta)\left(y_2-y_1\right)
> $$
````

## Source-to-current comparison

Source: /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 02 Analytic Functions/2.6 Differentiation of Functions of Several Variables.md

This exact comparison preserves the full change evidence, including formatting, OCR corrections, restored source wording, and required standalone context. The entries above explain the recovery edits. The comparison is not a claim that every difference is a correction; component serialization, callout wrapping, and printed labels outside callouts are formatting.

`````diff
--- /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 02 Analytic Functions/2.6 Differentiation of Functions of Several Variables.md
+++ /Users/gradyclopton/ObsidianVaults/complex_analysis/Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 02 Analytic Functions/2.6 Differentiation of Functions of Several Variables.md
@@ -349,23 +349,32 @@
 This expresses the well-known geometric fact that, near a point $x=x_{0}$ where the function $\phi(x)$ is differentiable with derivative $\phi^{\prime}\left(x_{0}\right)$, the tangent line approximates the graph of the function with an error that tends to 0 faster than $\left|x-x_{0}\right|$ (_Figure 1_).
 
 
-> [!figure] Figure 1
-> 
-> ![300](./images/af4f9593-dec7-4bc0-8d78-d25500419ec9-57_461_497_1149_109.jpg)
-> Figure 1 Approximation of a differentiable function by the tangent line.
+```scientific-figure
+id: f12e4e04-50ee-49ae-bae3-77c5c40e40ed
+numbered: false
+title: ""
+caption: "**Figure 1.** Approximation of a differentiable function by the tangent line."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 02 Analytic Functions/images/af4f9593-dec7-4bc0-8d78-d25500419ec9-57_461_497_1149_109.jpg
+    caption: ""
+```
 
 
 
 
 With (1) in mind, we introduce the notion of differentiability for realvalued functions of two variables. To simplify the notation, we will sometimes denote a point $(x, y)$ by the complex number $z$.
 
+<!-- Source label: Differentiability of Real-Valued Functions of Two Variables -->
 > [!definition] Differentiability of Real-Valued Functions of Two Variables
 > We call a real-valued function $u(x, y)$ differentiable at $z_{0}=\left(x_{0}, y_{0}\right)$ if it can be written in the form
-> 
+>
 > $$
 > u(z)=u\left(z_{0}\right)+A\left(x-x_{0}\right)+B\left(y-y_{0}\right)+\epsilon(z)\left|z-z_{0}\right|
 > $$
-> 
+>
 > where $A$ and $B$ are (real) constants and $\epsilon(z) \rightarrow 0$ as $z \rightarrow z_{0}$.
 
 
@@ -386,8 +395,9 @@
 
 
 
-> [!Theorem] Theorem 1
-> Suppose $u(x, y)$ is differentiable at $z_{0}=x_{0}+i y_{0}$, so that (2) holds. Then 
+<!-- Source label: Theorem 1 -->
+> [!theorem] Continuity and Partial Derivatives of a Totally Differentiable Function
+> Suppose $u(x, y)$ is differentiable at $z_{0}=x_{0}+i y_{0}$, with linear approximation $u(z)=u(z_0)+A(x-x_0)+B(y-y_0)+o(|z-z_0|)$. Then 
 > (i) $u(x, y)$ is continuous at $z_{0}$; and
 > (ii) $u_{x}, u_{y}$ exist at $z_{0}$ and $u_{x}\left(z_{0}\right)=A, u_{y}\left(z_{0}\right)=B$.
 
@@ -868,11 +878,21 @@
 
 A helpful plot is the following. The surface is drawn on the punctured plane, and the red point marks the separately defined value $u(0,0)=0$.
 
-> [!figure] Plot of $u(x,y)=\dfrac{xy}{x^2+y^2}$
->
-> ![](Pasted%20image%2020260425053032.png)
->
-> The punctured surface approaches different values along different paths, while the origin itself is defined to be $0$.
+```scientific-figure
+id: c08b980e-55b7-437d-a52b-d4954c8a1c55
+numbered: false
+title: ""
+caption: |-
+  Plot of $u(x,y)=\dfrac{xy}{x^2+y^2}$
+
+  The punctured surface approaches different values along different paths, while the origin itself is defined to be $0$.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 02 Analytic Functions/images/Pasted image 20260425053032.png
+    caption: ""
+```
 
 The following Mathematica code produces a corresponding plot.
 
@@ -984,31 +1004,51 @@
 
 
 
-> [!figure] Figure 2
-> 
-> ![300](./images/af4f9593-dec7-4bc0-8d78-d25500419ec9-58_426_543_1783_113.jpg)
-> Figure 2 A discontinuous function with partial derivatives at $(0,0)$. The function is not differentiable at $(0,0)$.
+```scientific-figure
+id: 4bb9968d-0297-4469-8c96-80dbce213a52
+numbered: false
+title: ""
+caption: "**Figure 2.** A discontinuous function with partial derivatives at $(0,0)$. The function is not differentiable at $(0,0)$."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 02 Analytic Functions/images/af4f9593-dec7-4bc0-8d78-d25500419ec9-58_426_543_1783_113.jpg
+    caption: ""
+```
 
 
 $u(x, y)-u\left(x, y_{0}\right)$, think of $x$ as fixed, and apply the mean value theorem in the second variable.
 
 To obtain differentiability at a point, more is needed than the existence of the partial derivatives. We have the following interesting result.
 
-> [!Theorem] Theorem 2: Sufficient Conditions for Differentiability
+<!-- Source label: Theorem 2: Sufficient Conditions for Differentiability -->
+> [!theorem] Sufficient Conditions for Differentiability
 > Let $u$ be a real-valued function defined on a neighborhood of $z_{0}$. If
 > (i) $u_{x}\left(z_{0}\right)$ and $u_{y}\left(z_{0}\right)$ exist, and
 > (ii) either $u_{x}(z)$ or $u_{y}(z)$ is continuous at $z_{0}$,
-> then $u$ is differentiable at $z_{0}$, and (2) holds with $A=u_{x}\left(x_{0}, y_{0}\right), B= u_{y}\left(x_{0}, y_{0}\right)$.
+> then $u$ is differentiable at $z_{0}$, and $u(z)=u(z_0)+A(x-x_0)+B(y-y_0)+o(|z-z_0|)$ with $A=u_{x}\left(x_{0}, y_{0}\right), B= u_{y}\left(x_{0}, y_{0}\right)$.
 
 
 **Proof** 
 
 
 
-> [!figure] Figure 3: For Proof to Theorem 3
-> 
-> ![](./images/af4f9593-dec7-4bc0-8d78-d25500419ec9-59_465_484_1527_122.jpg)
-> Figure 3 In the expression
+```scientific-figure
+id: b52131eb-4b45-47d5-976d-66ca6d842c3d
+numbered: false
+title: ""
+caption: |-
+  **Figure 3.** For Proof to Theorem 3
+
+  In the expression
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 02 Analytic Functions/images/af4f9593-dec7-4bc0-8d78-d25500419ec9-59_465_484_1527_122.jpg
+    caption: ""
+```
 
 
 
@@ -1020,8 +1060,9 @@
 We are now in a position to complete the proof of the Cauchy-Riemann equations theorem.
 
 
-> [!theorem] Theorem 4: The Chain Rule
-> Let $f(z)=u(x, y)+i v(x, y)$ be a complex-valued function, defined in an open set $S$. If $u_{x}, u_{y}, v_{x}$, and $v_{y}$ are continuous and satisfy the CauchyRiemann equations in $S$, then $f(z)$ is analytic on $S$.
+<!-- Source label: Theorem 4: The Chain Rule -->
+> [!theorem] The Chain Rule
+> Let $f(z)=u(x, y)+i v(x, y)$ be a complex-valued function, defined in an open set $S$. If $u_{x}, u_{y}, v_{x}$, and $v_{y}$ are continuous and satisfy the Cauchy–Riemann equations in $S$, then $f(z)$ is analytic on $S$.
 
 
 **Proof** 
@@ -1421,13 +1462,15 @@
 We can use Definition 1 and basic properties of differentiability to give simple proofs of the chain rule and the mean value theorem in two dimensions. These fundamental results were already used in this chapter and will be used again.
 
 
-> [!theorem] Theorem 4: The Chain Rule
+<!-- Source label: Theorem 4: The Chain Rule -->
+> [!theorem] The Chain Rule
+> Assume the curve $(x(t),y(t))$ lies in $S$.
+>
 > Suppose that $u(x, y)$ is a differentiable function of $(x, y)$ in an open set $S$, where $x=x(t)$ and $y=y(t)$ are both differentiable functions of $t$. Then the function $U(t)=u(x(t), y(t))$ is a differentiable function of $t$ and
-> 
+>
 > $$
 > \frac{d U}{d t}=\frac{\partial u}{\partial x} \frac{d x}{d t}+\frac{\partial u}{\partial y} \frac{d y}{d t}
 > $$
-> 
 
 
 
@@ -1471,23 +1514,29 @@
 
 
 
-> [!theorem] Theorem 5: The Mean Value Theorem in Two Dimensions
-> 
-> 
-> Suppose $u(x, y)$ is a differentiable real-valued function of ( $x, y$ ) in an open set $S$. Suppose that the line segment $\left[z_1, z_2\right]$ joining $z_1=\left(x_1, y_1\right)$ to $z_2=\left(x_2, y_2\right)$ lies entirely in $S$. Then there exists a point $\zeta$ on $\left[z_1, z_2\right]$ (see _Figure 4_) such that
-> 
+<!-- Source label: Theorem 5: The Mean Value Theorem in Two Dimensions -->
+> [!theorem] The Mean Value Theorem in Two Dimensions
+> Suppose $u(x, y)$ is a differentiable real-valued function of ( $x, y$ ) in an open set $S$. Suppose that the line segment $\left[z_1, z_2\right]$ joining $z_1=\left(x_1, y_1\right)$ to $z_2=\left(x_2, y_2\right)$ lies entirely in $S$. Then there exists a point $\zeta$ on $\left[z_1, z_2\right]$ such that
+>
 > $$
 > u\left(z_2\right)-u\left(z_1\right)=u_x(\zeta)\left(x_2-x_1\right)+u_y(\zeta)\left(y_2-y_1\right)
 > $$
-> 
-> > [!figure] Figure 4: For Theorem 5
-> > 
-> > ![300](./images/af4f9593-dec7-4bc0-8d78-d25500419ec9-62_500_557_272_99.jpg)
-> > Figure 4 Mean value theorem in two dimensions.
-> 
-> 
-> 
-> 
+
+```scientific-figure
+id: 09aa0709-a77c-4c45-be72-0ed233114794
+numbered: false
+title: ""
+caption: |-
+  **Figure 4.** For Theorem 5
+
+  Mean value theorem in two dimensions.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 02 Analytic Functions/images/af4f9593-dec7-4bc0-8d78-d25500419ec9-62_500_557_272_99.jpg
+    caption: ""
+```
 
 **Proof:** 
 

`````
