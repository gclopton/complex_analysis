
# Editorial records

Reading note: 2.3 Analytic Functions.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Callout 54: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!definition] Analytic and Entire Complex Functions
> A function $f(z)$ defined on an open set $S$ is said to be analytic on $S$ if $f^{\prime}(z)$ exists and is continuous for all $z$ in $S$. We say $f(z)$ is analytic at a point if $f(z)$ is analytic on some open set containing that point. We say $f(z)$ is entire if $f(z)$ is analytic on $\mathbb{C}$.
````
### After

````text
> [!definition] Analytic Function
> A function $f(z)$ defined on an open set $S$ is said to be analytic on $S$ if $f^{\prime}(z)$ exists and is continuous for all $z$ in $S$. We say $f(z)$ is analytic at a point if $f(z)$ is analytic on some open set containing that point. We say $f(z)$ is entire if $f(z)$ is analytic on $\mathbb{C}$.
````

## 2. Callout 55: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Complex Differentiability Implies Continuity
> Suppose $f(z)$ is differentiable at $z_{0}$. Then $f(z)$ is continuous at $z_{0}$.
````
### After

````text
> [!theorem] Differentiable Implies Continuous
> Suppose $f(z)$ is differentiable at $z_{0}$. Then $f(z)$ is continuous at $z_{0}$.
````

## 3. Callout 56: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Sum, Product, Quotient, and Chain Rules for Analytic Functions
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
> (f \circ g)^{\prime}\left(z_{0}\right)=f^{\prime}\left(g\left(z_{0}\right)\right) g^{\prime}\left(z_{0}\right) .
> $$
````
### After

````text
> [!theorem] Properties of Analytic Functions
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
> (f \circ g)^{\prime}\left(z_{0}\right)=f^{\prime}\left(g\left(z_{0}\right)\right) g^{\prime}\left(z_{0}\right) .
> $$
````

## 4. Callout 57: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Analyticity and Derivatives of Complex Polynomials and Rational Functions
> Let $n$ be a nonnegative integer. A polynomial of degree $n, p(z)=a_{n} z^{n}+ a_{n-1} z^{n-1}+\cdots+a_{1} z+a_{0}$, is entire. Its derivative is given by
>
> $$
> p^{\prime}(z)=n a_{n} z^{n-1}+(n-1) a_{n-1} z^{n-1}+\cdots+a_{1} .
> $$
>
> A rational function $f(z)=p(z) / q(z)$, where $p(z)$ and $q(z)$ are polynomials, is analytic at all points $z$ where $q(z) \neq 0$. Its derivative is given by
>
> $$
> f^{\prime}(z)=\frac{p^{\prime}(z) q(z)-p(z) q^{\prime}(z)}{q(z)^{2}}
> $$
````
### After

````text
> [!theorem] Polynomials and Rational Functions
> Let $n$ be a nonnegative integer. A polynomial of degree $n, p(z)=a_{n} z^{n}+ a_{n-1} z^{n-1}+\cdots+a_{1} z+a_{0}$, is entire. Its derivative is given by
>
> $$
> p^{\prime}(z)=n a_{n} z^{n-1}+(n-1) a_{n-1} z^{n-1}+\cdots+a_{1} .
> $$
>
> A rational function $f(z)=p(z) / q(z)$, where $p(z)$ and $q(z)$ are polynomials, is analytic at all points $z$ where $q(z) \neq 0$. Its derivative is given by
>
> $$
> f^{\prime}(z)=\frac{p^{\prime}(z) q(z)-p(z) q^{\prime}(z)}{q(z)^{2}}
> $$
````

## 5. Callout 58: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Analyticity of an Inner Function under a Locally Invertible Analytic Map
> Suppose that $h(z)=f(g(z))$ is analytic on a region $\Omega$, and $f$ is analytic at $g(z)$ with $f^{\prime}(g(z)) \neq 0$ for all $z$ in $\Omega$. Suppose further that $g(z)$ is continuous on $\Omega$. Then $g$ is analytic on $\Omega$ and
>
> $$
> g^{\prime}(z)=\frac{h^{\prime}(z)}{f^{\prime}(g(z))}
> $$
````
### After

````text
> [!theorem] Analyticity of Composed Functions
> Suppose that $h(z)=f(g(z))$ is analytic on a region $\Omega$, and $f$ is analytic at $g(z)$ with $f^{\prime}(g(z)) \neq 0$ for all $z$ in $\Omega$. Suppose further that $g(z)$ is continuous on $\Omega$. Then $g$ is analytic on $\Omega$ and
>
> $$
> g^{\prime}(z)=\frac{h^{\prime}(z)}{f^{\prime}(g(z))}
> $$
````

## 6. Callout 59: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Linear Approximation Characterization of Complex Differentiability
> A function $f(z)$ is differentiable at $z_{0}$ if and only if it can be written in the form
>
> $$
> f(z)=f\left(z_{0}\right)+A\left(z-z_{0}\right)+\epsilon(z)\left(z-z_{0}\right)
> $$
>
> where $A=f^{\prime}\left(z_{0}\right)$ and $\epsilon(z) \rightarrow 0$ as $z \rightarrow z_{0}$.
````
### After

````text
> [!theorem] Differentiability
> A function $f(z)$ is differentiable at $z_{0}$ if and only if it can be written in the form
>
> $$
> f(z)=f\left(z_{0}\right)+A\left(z-z_{0}\right)+\epsilon(z)\left(z-z_{0}\right)
> $$
>
> where $A=f^{\prime}\left(z_{0}\right)$ and $\epsilon(z) \rightarrow 0$ as $z \rightarrow z_{0}$.
````

## 7. Move editorial commentary out of the reading note.

### Before

````text
*Editorial note: Corrected the final derivative term: the derivative of $a_1z$ is $a_1$.*
````
### After

````text

````

## Source-to-current comparison

Source: /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 02 Analytic Functions/2.3 Analytic Functions.md

This exact comparison preserves the full change evidence, including formatting, OCR corrections, restored source wording, and required standalone context. The entries above explain the recovery edits. The comparison is not a claim that every difference is a correction; component serialization, callout wrapping, and printed labels outside callouts are formatting.

`````diff
--- /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 02 Analytic Functions/2.3 Analytic Functions.md
+++ /Users/gradyclopton/ObsidianVaults/complex_analysis/Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 02 Analytic Functions/2.3 Analytic Functions.md
@@ -50,19 +50,20 @@
 
 
 
+<!-- Source label: Complex Derivative -->
 > [!definition] Complex Derivative
 > Let $f(z)$ be defined on a neighborhood of $z_{0}$. If
-> 
+>
 > $$
 > \lim _{z \rightarrow z_{0}} \frac{f(z)-f\left(z_{0}\right)}{z-z_{0}}
 > $$
-> 
+>
 > exists, then $f$ is said to be differentiable at the point $z_{0}$, and the number
-> 
+>
 > $$
 > f^{\prime}\left(z_{0}\right)=\lim _{z \rightarrow z_{0}} \frac{f(z)-f\left(z_{0}\right)}{z-z_{0}}
 > $$
-> 
+>
 > is called the derivative of $f$ at $z_{0}$.
 
 
@@ -78,6 +79,7 @@
 We now introduce a fundamental definition in the theory of complex variables.
 
 
+<!-- Source label: Analytic Function -->
 > [!definition] Analytic Function
 > A function $f(z)$ defined on an open set $S$ is said to be analytic on $S$ if $f^{\prime}(z)$ exists and is continuous for all $z$ in $S$. We say $f(z)$ is analytic at a point if $f(z)$ is analytic on some open set containing that point. We say $f(z)$ is entire if $f(z)$ is analytic on $\mathbb{C}$.
 
@@ -413,7 +415,8 @@
 
 
 
-> [!theorem] Theorem 1: Differentiable Implies Continuous
+<!-- Source label: Theorem 1: Differentiable Implies Continuous -->
+> [!theorem] Differentiable Implies Continuous
 > Suppose $f(z)$ is differentiable at $z_{0}$. Then $f(z)$ is continuous at $z_{0}$.
 
 
@@ -426,28 +429,28 @@
 
 
 
-> [!theorem] Theorem 2: Properties of Analytic Functions
+<!-- Source label: Theorem 2: Properties of Analytic Functions -->
+> [!theorem] Properties of Analytic Functions
 > Suppose that $f$ and $g$ are analytic on an open set $S$ and $c_{1}, c_{2}$ are complex constants. Then $c_{1} f+c_{2} g$ and $f g$ are analytic on $S$ with
-> 
+>
 > $$
 > \begin{aligned}
 > \left(c_{1} f+c_{2} g\right)^{\prime}(z) & =c_{1} f^{\prime}(z)+c_{2} g^{\prime}(z) \text { and } \\
 > (f g)^{\prime}(z) & =f^{\prime}(z) g(z)+f(z) g^{\prime}(z) .
 > \end{aligned}
 > $$
-> 
+>
 > Also, $\frac{f}{g}$ is analytic on $S$ minus the points where $g=0$, and
-> 
+>
 > $$
 > \left(\frac{f}{g}\right)^{\prime}(z)=\frac{f^{\prime}(z) g(z)-f(z) g^{\prime}(z)}{(g(z))^{2}} \quad(g(z) \neq 0) .
 > $$
-> 
+>
 > If $g$ is analytic at $z_{0}$ and $f$ is analytic at $g\left(z_{0}\right)$, then the composition $(f \circ g)(z)$ is analytic at $z_{0}$ and we have the chain rule
-> 
+>
 > $$
 > (f \circ g)^{\prime}\left(z_{0}\right)=f^{\prime}\left(g\left(z_{0}\right)\right) g^{\prime}\left(z_{0}\right) .
 > $$
-> 
 
 
 **Proof** 
@@ -466,7 +469,9 @@
 > Conclude that $f(z)=z^{n}$ is entire.
 
 
-**Solution:** We prove by induction on $n$ that
+##### solution
+
+We prove by induction on $n$ that
 $$
 \frac{d}{dz}z^n=nz^{n-1}.
 $$
@@ -538,7 +543,9 @@
 > and determine where $f(z)$ is analytic.
 
 
-**Solution:** Let
+##### solution
+
+Let
 $$
 f(z)=\frac{(z+1)(z+i)^2}{z+1-3i}.
 $$
@@ -705,19 +712,19 @@
 
 
 
-> [!theorem] Theorem 3 Polynomials and Rational Functions
+<!-- Source label: Theorem 3 Polynomials and Rational Functions -->
+> [!theorem] Polynomials and Rational Functions
 > Let $n$ be a nonnegative integer. A polynomial of degree $n, p(z)=a_{n} z^{n}+ a_{n-1} z^{n-1}+\cdots+a_{1} z+a_{0}$, is entire. Its derivative is given by
-> 
+>
 > $$
-> p^{\prime}(z)=n a_{n} z^{n-1}+(n-1) a_{n-1} z^{n-1}+\cdots+a_{1} z .
+> p^{\prime}(z)=n a_{n} z^{n-1}+(n-1) a_{n-1} z^{n-1}+\cdots+a_{1} .
 > $$
-> 
+>
 > A rational function $f(z)=p(z) / q(z)$, where $p(z)$ and $q(z)$ are polynomials, is analytic at all points $z$ where $q(z) \neq 0$. Its derivative is given by
-> 
+>
 > $$
 > f^{\prime}(z)=\frac{p^{\prime}(z) q(z)-p(z) q^{\prime}(z)}{q(z)^{2}}
 > $$
-> 
 
 
 Typically, any function that algebraically manipulates $z$ will be differentiable; however, not every complex-valued function is analytic. Functions like $\operatorname{Re} z, \operatorname{Im} z, \bar{z}$, and $|z|$ will have at best limited differentiability.
@@ -738,7 +745,9 @@
 ##### problem 4.a
 
 
-**Solution:** Let
+##### solution
+
+Let
 $$
 f(z)=\bar z.
 $$
@@ -805,17 +814,27 @@
 Because $z_0$ was arbitrary, $\bar z$ is not differentiable at any point of $\mathbb{C}$. Hence $f(z)=\bar z$ is nowhere analytic.
 
 
-> [!figure] Figure 1
-> 
-> ![](./images/af4f9593-dec7-4bc0-8d78-d25500419ec9-23_463_509_480_116.jpg)
-> Figure 1 On $C, \Delta z=\Delta x$. On $C^{\prime}, \Delta z=i \Delta y$.
+```scientific-figure
+id: ac05455b-f69c-43db-962f-0e698efa1b79
+numbered: false
+title: ""
+caption: "**Figure 1.** On $C, \\Delta z=\\Delta x$. On $C^{\\prime}, \\Delta z=i \\Delta y$."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 02 Analytic Functions/images/af4f9593-dec7-4bc0-8d78-d25500419ec9-23_463_509_480_116.jpg
+    caption: ""
+```
 
 
 
 ##### problem 4.b
 
 
-**Solution:** Let
+##### solution
+
+Let
 $$
 f(z)=\operatorname{Re} z.
 $$
@@ -957,21 +976,28 @@
 
 
 
-> [!figure] Figure 2
-> 
-> ![](./images/af4f9593-dec7-4bc0-8d78-d25500419ec9-24_544_1431_1357_676.jpg)
-> 
-> Figure 2 Unlike the chain rule, where we suppose that $f$ and $g$ are analytic and conclude that $h=g \circ f$ is analytic, in Theorem 4, we suppose that $g$ is continuous, and $f$ and the composed function $h$ are analytic, and then we conclude that $g$ is analytic.
-
-
-
-> [!theorem] Theorem 4: Analyticity of Composed Functions
-> Suppose that $h(z)=f(g(z))$ is analytic on a region $\Omega$, and $f$ is analytic at $g(z)$ with $f^{\prime}(g(z)) \neq 0$ for all $z$ in $\Omega$. Suppose further that $g(z)$ is continuous on $\Omega$ (Figure 2). Then $g$ is analytic on $\Omega$ and
-> 
+```scientific-figure
+id: 62596e89-33c6-4791-97da-13838197c7e4
+numbered: false
+title: ""
+caption: "**Figure 2.** Unlike the chain rule, where we suppose that $f$ and $g$ are analytic and conclude that $h=g \\circ f$ is analytic, in Theorem 4, we suppose that $g$ is continuous, and $f$ and the composed function $h$ are analytic, and then we conclude that $g$ is analytic."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 02 Analytic Functions/images/af4f9593-dec7-4bc0-8d78-d25500419ec9-24_544_1431_1357_676.jpg
+    caption: ""
+```
+
+
+
+<!-- Source label: Theorem 4: Analyticity of Composed Functions -->
+> [!theorem] Analyticity of Composed Functions
+> Suppose that $h(z)=f(g(z))$ is analytic on a region $\Omega$, and $f$ is analytic at $g(z)$ with $f^{\prime}(g(z)) \neq 0$ for all $z$ in $\Omega$. Suppose further that $g(z)$ is continuous on $\Omega$. Then $g$ is analytic on $\Omega$ and
+>
 > $$
 > g^{\prime}(z)=\frac{h^{\prime}(z)}{f^{\prime}(g(z))}
 > $$
-> 
 
 As in the case of the chain rule, the proof of this theorem will be greatly simplified by using the formalisms presented in the appendix. We postpone the proof and give instead an application.
 
@@ -988,7 +1014,9 @@
 
 
 
-**Solution:** Let
+##### solution
+
+Let
 $$
 g(z)=z^{1/n}
 $$
@@ -1102,10 +1130,18 @@
 $$
 
 
-> [!figure] Figure 3
-> 
-> ![400](Pasted%20image%2020260412041440.png)
-> Figure 3 Branch cut of $\log z$.
+```scientific-figure
+id: fcff5520-b007-45f7-9b66-59d90e696ac0
+numbered: false
+title: ""
+caption: "**Figure 3.** Branch cut of $\\log z$."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 02 Analytic Functions/images/Pasted image 20260412041440.png
+    caption: ""
+```
 
 
 
@@ -1166,7 +1202,9 @@
 > Show how a function can be locally approximated by an affine linear function at a point if it is differentiable at that point. Show whether or not the converse is true.
 
 
-**Solution:** Suppose first that $f$ is differentiable at $z_0$. Then
+##### solution
+
+Suppose first that $f$ is differentiable at $z_0$. Then
 $$
 f'(z_0)=\lim_{z\to z_0}\frac{f(z)-f(z_0)}{z-z_0}.
 $$
@@ -1260,13 +1298,14 @@
 
 
 
-> [!theorem] Theorem 5: Differentiability
+<!-- Source label: Theorem 5: Differentiability -->
+> [!theorem] Differentiability
 > A function $f(z)$ is differentiable at $z_{0}$ if and only if it can be written in the form
-> 
+>
 > $$
 > f(z)=f\left(z_{0}\right)+A\left(z-z_{0}\right)+\epsilon(z)\left(z-z_{0}\right)
 > $$
-> 
+>
 > where $A=f^{\prime}\left(z_{0}\right)$ and $\epsilon(z) \rightarrow 0$ as $z \rightarrow z_{0}$.
 
 
@@ -1285,7 +1324,9 @@
 
 
 
-**Solution:** Since $g$ is analytic at $z_0$ and $f$ is analytic at $g(z_0)$, both derivatives
+##### solution
+
+Since $g$ is analytic at $z_0$ and $f$ is analytic at $g(z_0)$, both derivatives
 $$
 g'(z_0)
 \qquad\text{and}\qquad
@@ -1380,7 +1421,9 @@
 > $$
 
 
-**Solution:** We are given that
+##### solution
+
+We are given that
 $$
 h(z)=f(g(z))
 $$
@@ -1527,7 +1570,7 @@
 
 
 
-**Solution:**
+##### solution
 
 ##### problem 1
 
@@ -2435,7 +2478,7 @@
 
 
 
-**Solution:**
+##### solution
 
 ##### problem 13
 
@@ -2679,7 +2722,9 @@
 
 
 
-**Solution:** We consider the two pieces separately and then examine what happens on the boundary
+##### solution
+
+We consider the two pieces separately and then examine what happens on the boundary
 $$
 |z|=1.
 $$
@@ -2881,7 +2926,7 @@
 
 
 
-**Solution:**
+##### solution
 
 ##### problem 18.a
 
@@ -3097,7 +3142,9 @@
 
 
 
-**Solution:** Let
+##### solution
+
+Let
 $$
 f(z)=|z|.
 $$
@@ -3513,7 +3560,9 @@
 
 
 
-**Solution:** Let
+##### solution
+
+Let
 $$
 g(z)=z^{p/q},
 $$
@@ -3672,7 +3721,9 @@
 
 
 
-**Solution:** Let
+##### solution
+
+Let
 $$
 h(z)=c_1f(z)+c_2g(z).
 $$
@@ -3760,7 +3811,7 @@
 
 
 
-**Solution:**
+##### solution
 
 ##### problem 23.a
 

`````
