
# Editorial records

Reading note: 2.2 Limits and Continuity.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Callout 44: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!definition] Limit of a Complex-Valued Function
> We say that a complex-valued function $f(z)$ has a limit $L$ as $z$ approaches $z_{0}$, and we write
>
> $$
> \lim _{z \rightarrow z_{0}} f(z)=L \quad \text { or } \quad f(z) \rightarrow L \text { as } z \rightarrow z_{0},
> $$
>
> if given any $\epsilon>0$, there exists a $\delta>0$ such that
>
> $$
> |f(z)-L|<\epsilon \quad \text { whenever } 0<\left|z-z_{0}\right|<\delta .
> $$
````
### After

````text
> [!definition] limit of a complex-valued function
> We say that a complex-valued function $f(z)$ has a limit $L$ as $z$ approaches $z_{0}$, and we write
>
> $$
> \lim _{z \rightarrow z_{0}} f(z)=L \quad \text { or } \quad f(z) \rightarrow L \text { as } z \rightarrow z_{0},
> $$
>
> if given any $\epsilon>0$, there exists a $\delta>0$ such that
>
> $$
> |f(z)-L|<\epsilon \quad \text { whenever } 0<\left|z-z_{0}\right|<\delta .
> $$
````

## 2. Callout 45: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Algebra and Composition Laws for Complex Limits
> Suppose $\lim _{z \rightarrow z_{0}} f(z)$ and $\lim _{z \rightarrow z_{0}} g(z)$ both exist and $c_{1}, c_{2}$ are complex constants. Then
>
> $$
> \lim _{z \rightarrow z_{0}}\left[c_{1} f(z)+c_{2} g(z)\right]=c_{1} \lim _{z \rightarrow z_{0}} f(z)+c_{2} \lim _{z \rightarrow z_{0}} g(z), 
> $$
>
> $$
> \lim _{z \rightarrow z_{0}}[f(z) g(z)]=\lim _{z \rightarrow z_{0}} f(z)\,\lim _{z \rightarrow z_{0}} g(z), 
> $$
>
> $\lim _{z \rightarrow z_{0}}\left[\frac{f(z)}{g(z)}\right]=\frac{\lim _{z \rightarrow z_{0}} f(z)}{\lim _{z \rightarrow z_{0}} g(z)}$, provided $\lim _{z \rightarrow z_{0}} g(z) \neq 0$.
>
> If $g(z)\to w_0$ as $z\to z_0$ and $f$ is continuous at $w_0$, then, writing $A=f(w_0)$,
>
> $$
> \lim _{z \rightarrow z_{0}} f(g(z))=A=f\left(\lim _{z \rightarrow z_{0}} g(z)\right) 
> $$
````
### After

````text
> [!theorem] Operations with Limits
> Suppose $\lim _{z \rightarrow z_{0}} f(z)$ and $\lim _{z \rightarrow z_{0}} g(z)$ both exist and $c_{1}, c_{2}$ are complex constants. Then
>
> $$
> \lim _{z \rightarrow z_{0}}\left[c_{1} f(z)+c_{2} g(z)\right]=c_{1} \lim _{z \rightarrow z_{0}} f(z)+c_{2} \lim _{z \rightarrow z_{0}} g(z), 
> $$
>
> $$
> \lim _{z \rightarrow z_{0}}[f(z) g(z)]=\lim _{z \rightarrow z_{0}} f(z)\,\lim _{z \rightarrow z_{0}} g(z), 
> $$
>
> $\lim _{z \rightarrow z_{0}}\left[\frac{f(z)}{g(z)}\right]=\frac{\lim _{z \rightarrow z_{0}} f(z)}{\lim _{z \rightarrow z_{0}} g(z)}$, provided $\lim _{z \rightarrow z_{0}} g(z) \neq 0$.
>
> If $g(z)\to w_0$ as $z\to z_0$ and $f$ is continuous at $w_0$, then, writing $A=f(w_0)$,
>
> $$
> \lim _{z \rightarrow z_{0}} f(g(z))=A=f\left(\lim _{z \rightarrow z_{0}} g(z)\right) 
> $$
````

## 3. Callout 46: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Squeeze and Bounded-Factor Theorems for Complex Limits
> (i) Suppose that $f(z) \rightarrow 0$ as $z \rightarrow z_0$ and $|g(z)| \leq|f(z)|$ in a deleted neighborhood of $z_0$. Then $g(z) \rightarrow 0$ as $z \rightarrow z_0$.
> (ii) Suppose that $f(z) \rightarrow 0$ as $z \rightarrow z_0$ and $g(z)$ is bounded in a deleted neighborhood of $z_0$. Then $f(z) g(z) \rightarrow 0$ as $z \rightarrow z_0$.
````
### After

````text
> [!theorem] The Squeeze Theorem
> (i) Suppose that $f(z) \rightarrow 0$ as $z \rightarrow z_0$ and $|g(z)| \leq|f(z)|$ in a deleted neighborhood of $z_0$. Then $g(z) \rightarrow 0$ as $z \rightarrow z_0$.
> (ii) Suppose that $f(z) \rightarrow 0$ as $z \rightarrow z_0$ and $g(z)$ is bounded in a deleted neighborhood of $z_0$. Then $f(z) g(z) \rightarrow 0$ as $z \rightarrow z_0$.
````

## 4. Callout 47: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Complex Limits via Real and Imaginary Parts
> Given a complex-valued function $f(z)=u(x, y)+i v(x, y)$ and a complex number $L=a+i b$, then
> $\lim _{z \rightarrow z_{0}} f(z)=L \Longleftrightarrow \lim _{z \rightarrow z_{0}} u(x, y)=a$ and $\lim _{z \rightarrow z_{0}} v(x, y)=b$.
````
### After

````text
> [!theorem] REAL AND IMAGINARY PARTS OF LIMITS
> Given a complex-valued function $f(z)=u(x, y)+i v(x, y)$ and a complex number $L=a+i b$, then
> $\lim _{z \rightarrow z_{0}} f(z)=L \Longleftrightarrow \lim _{z \rightarrow z_{0}} u(x, y)=a$ and $\lim _{z \rightarrow z_{0}} v(x, y)=b$.
````

## 5. Callout 48: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!definition] Infinite Limits and Limits at Infinity for Complex Functions
> (i) We write $\lim _{z \rightarrow z_{0}} f(z)=\infty$ to mean that for any $M>0$ there is a $\delta>0$ such that $0<\left|z-z_{0}\right|<\delta \Rightarrow|f(z)|>M$.
> (ii) We write $\lim _{z \rightarrow \infty} f(z)=L$ to mean that for any $\epsilon>0$ there is an $R>0$ such that $|z|>R \Rightarrow|f(z)-L|<\epsilon$.
> (iii) We write $\lim _{z \rightarrow \infty} f(z)=\infty$ to mean that for any $M>0$ there is an $R>0$ such that $|z|>R \Rightarrow|f(z)|>M$.
````
### After

````text
> [!definition] Limits Involving Infinity
> (i) We write $\lim _{z \rightarrow z_{0}} f(z)=\infty$ to mean that for any $M>0$ there is a $\delta>0$ such that $0<\left|z-z_{0}\right|<\delta \Rightarrow|f(z)|>M$.
> (ii) We write $\lim _{z \rightarrow \infty} f(z)=L$ to mean that for any $\epsilon>0$ there is an $R>0$ such that $|z|>R \Rightarrow|f(z)-L|<\epsilon$.
> (iii) We write $\lim _{z \rightarrow \infty} f(z)=\infty$ to mean that for any $M>0$ there is an $R>0$ such that $|z|>R \Rightarrow|f(z)|>M$.
````

## 6. Callout 49: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!definition] Continuity of a Complex-Valued Function
> Suppose $f(z)$ is defined on a neighborhood of $z_{0}$. We say that $f(z)$ is continuous at the point $z_{0}$ if $\lim _{z \rightarrow z_{0}} f(z)$ exists and equals $f\left(z_{0}\right)$. We say $f$ is continuous on a set $S$ if it is continuous at every point in $S$.
````
### After

````text
> [!definition] Continuous Function
> Suppose $f(z)$ is defined on a neighborhood of $z_{0}$. We say that $f(z)$ is continuous at the point $z_{0}$ if $\lim _{z \rightarrow z_{0}} f(z)$ exists and equals $f\left(z_{0}\right)$. We say $f$ is continuous on a set $S$ if it is continuous at every point in $S$.
````

## 7. Callout 50: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Algebra and Composition Laws for Continuous Complex Functions
> (i) If $f(z)$ and $g(z)$ are continuous at $z_{0}$, and $c_{1}, c_{2}$ are complex constants, then the following functions are continuous at $z_{0}$ :
>
> $$
> c_{1} f(z)+c_{2} g(z), \quad f(z) g(z), \quad \frac{f(z)}{g(z)}\left(\text { provided } g\left(z_{0}\right) \neq 0\right)
> $$
>
> (ii) If $g$ is continuous at $z_{0}$ and $f$ is continuous at $g\left(z_{0}\right)$, then the composition $h(z)=f(g(z))$ is continuous at $z_{0}$.
> (iii) If $g(z)$ is real-valued and continuous at $z_{0}$ and $f(x)$ is continuous at $x_{0}=g\left(z_{0}\right)$, then the composition $h(z)=f(g(z))$ is continuous at $z_{0}$.
> (iv) The function $f(z)=u(z)+i v(z)$ is continuous if and only if $u$ and $v$ are continuous.
````
### After

````text
> [!theorem] Properties of Continuous Functions
> (i) If $f(z)$ and $g(z)$ are continuous at $z_{0}$, and $c_{1}, c_{2}$ are complex constants, then the following functions are continuous at $z_{0}$ :
>
> $$
> c_{1} f(z)+c_{2} g(z), \quad f(z) g(z), \quad \frac{f(z)}{g(z)}\left(\text { provided } g\left(z_{0}\right) \neq 0\right)
> $$
>
> (ii) If $g$ is continuous at $z_{0}$ and $f$ is continuous at $g\left(z_{0}\right)$, then the composition $h(z)=f(g(z))$ is continuous at $z_{0}$.
> (iii) If $g(z)$ is real-valued and continuous at $z_{0}$ and $f(x)$ is continuous at $x_{0}=g\left(z_{0}\right)$, then the composition $h(z)=f(g(z))$ is continuous at $z_{0}$.
> (iv) The function $f(z)=u(z)+i v(z)$ is continuous if and only if $u$ and $v$ are continuous.
````

## 8. Callout 52: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Continuity and Branch Cut of the Principal Complex Logarithm
> The principal branch of the logarithm
>
> $$
> \log (z)=\ln |z|+i \operatorname{Arg}(z), \quad-\pi<\operatorname{Arg} z \leq \pi \quad(z \neq 0),
> $$
>
> is continuous for all $z$ in $\mathbb{C} \backslash(-\infty, 0]$. The jump across the negative real axis cannot be removed by redefining values there, and the singularity at $z=0$ is not removable.
````
### After

````text
> [!theorem] CONTINUITY OF THE LOGARITHM
> The principal branch of the logarithm
>
> $$
> \log (z)=\ln |z|+i \operatorname{Arg}(z), \quad-\pi<\operatorname{Arg} z \leq \pi \quad(z \neq 0),
> $$
>
> is continuous for all $z$ in $\mathbb{C} \backslash(-\infty, 0]$. For $z$ in $(-\infty, 0)$, the discontinuities of $\log z$ are not removable.
````

## 9. Move editorial commentary out of the reading note.

### Before

````text
*Editorial note: Restored the punctured-neighborhood condition for a limit at a finite point.*
````
### After

````text

````

## 10. Move editorial commentary out of the reading note.

### Before

````text
*Editorial note: Corrected the OCR comma between factors. Made continuity of the outer function explicit for the displayed composition formula with $f(w_0)$; a deleted limit alone does not justify that equality.*
````
### After

````text

````

## Source-to-current comparison

Source: /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 02 Analytic Functions/2.2 Limits and Continuity.md

This exact comparison preserves the full change evidence, including formatting, OCR corrections, restored source wording, and required standalone context. The entries above explain the recovery edits. The comparison is not a claim that every difference is a correction; component serialization, callout wrapping, and printed labels outside callouts are formatting.

`````diff
--- /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 02 Analytic Functions/2.2 Limits and Continuity.md
+++ /Users/gradyclopton/ObsidianVaults/complex_analysis/Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 02 Analytic Functions/2.2 Limits and Continuity.md
@@ -214,29 +214,36 @@
 
 
 
+<!-- Source label: limit of a complex-valued function -->
 > [!definition] limit of a complex-valued function
 > We say that a complex-valued function $f(z)$ has a limit $L$ as $z$ approaches $z_{0}$, and we write
-> 
+>
 > $$
 > \lim _{z \rightarrow z_{0}} f(z)=L \quad \text { or } \quad f(z) \rightarrow L \text { as } z \rightarrow z_{0},
 > $$
-> 
+>
 > if given any $\epsilon>0$, there exists a $\delta>0$ such that
-> 
+>
 > $$
 > |f(z)-L|<\epsilon \quad \text { whenever } 0<\left|z-z_{0}\right|<\delta .
 > $$
-> 
 
 
 If the limit of a function exists at a point, then it is unique (Exercise 27). This is referred to as the uniqueness property of limits.
 
 
-> [!figure] Figure 1
-> 
-> ![](./images/af4f9593-dec7-4bc0-8d78-d25500419ec9-09_461_1109_1442_746.jpg)
-> 
-> To say that $f(z) \rightarrow L$ as $z \rightarrow z_{0}$ is a strong assertion; it states that no matter how $z$ approaches $z_{0}$ (and there are many possible ways in the plane), the distance from $f(z)$ to $L$ will tend to zero. By contrast, for limits of functions on the real line, a point $x$ can approach $x_{0}$ from only two directions.
+```scientific-figure
+id: 46ffb6d7-0a57-4930-95f4-749140c56890
+numbered: false
+title: ""
+caption: "**Figure 1.** To say that $f(z) \\rightarrow L$ as $z \\rightarrow z_{0}$ is a strong assertion; it states that no matter how $z$ approaches $z_{0}$ (and there are many possible ways in the plane), the distance from $f(z)$ to $L$ will tend to zero. By contrast, for limits of functions on the real line, a point $x$ can approach $x_{0}$ from only two directions."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 02 Analytic Functions/images/af4f9593-dec7-4bc0-8d78-d25500419ec9-09_461_1109_1442_746.jpg
+    caption: ""
+```
 
 
 Geometrically, interpreting the absolute value $|f(z)-L|$ as the distance between $f(z)$ and $L$, we see from (1) that the function $f(z)$ has limit $L$ as $z \rightarrow z_{0}$ if and only if the distance from $f(z)$ to $L$ tends to zero as $z$ tends to $z_{0}$. Thus, $\lim _{z \rightarrow z_{0}} f(z)=L$ if and only if
@@ -499,34 +506,31 @@
 Computing more complicated limits by recourse to the $\epsilon \delta$-definition (1) is not always easy. To simplify this task, we will use properties of limits.
 
 
-> [!theorem] Theorem 1: Operations with Limits
-> Suppose $\lim _{z \rightarrow z_{0}} f(z)$ and $\lim _{z \rightarrow z_{0}} g(z)$ both exist and $c_{1}, c_{2}$ are complex constants, Then
-> 
-> 
+<!-- Source label: Theorem 1: Operations with Limits -->
+> [!theorem] Operations with Limits
+> Suppose $\lim _{z \rightarrow z_{0}} f(z)$ and $\lim _{z \rightarrow z_{0}} g(z)$ both exist and $c_{1}, c_{2}$ are complex constants. Then
+>
 > $$
-> \lim _{z \rightarrow z_{0}}\left[c_{1} f(z)+c_{2} g(z)\right]=c_{1} \lim _{z \rightarrow z_{0}} f(z)+c_{2} \lim _{z \rightarrow z_{0}} g(z), \tag{3}
+> \lim _{z \rightarrow z_{0}}\left[c_{1} f(z)+c_{2} g(z)\right]=c_{1} \lim _{z \rightarrow z_{0}} f(z)+c_{2} \lim _{z \rightarrow z_{0}} g(z), 
 > $$
-> 
+>
 > $$
-> \lim _{z \rightarrow z_{0}}[f(z) g(z)]=\lim _{z \rightarrow z_{0}} f(z), \lim _{z \rightarrow z_{0}} g(z), \tag{4}
+> \lim _{z \rightarrow z_{0}}[f(z) g(z)]=\lim _{z \rightarrow z_{0}} f(z)\,\lim _{z \rightarrow z_{0}} g(z), 
 > $$
-> 
-> (5) $\lim _{z \rightarrow z_{0}}\left[\frac{f(z)}{g(z)}\right]=\frac{\lim _{z \rightarrow z_{0}} f(z)}{\lim _{z \rightarrow z_{0}} g(z)}$, provided $\lim _{z \rightarrow z_{0}} g(z) \neq 0$.
-> 
-> If $\lim _{z \rightarrow z_{0}} g(z)=w_{0}$ and $\lim _{w \rightarrow w_{0}} f(w)=A$, then
-> 
-> 
+>
+> $\lim _{z \rightarrow z_{0}}\left[\frac{f(z)}{g(z)}\right]=\frac{\lim _{z \rightarrow z_{0}} f(z)}{\lim _{z \rightarrow z_{0}} g(z)}$, provided $\lim _{z \rightarrow z_{0}} g(z) \neq 0$.
+>
+> If $g(z)\to w_0$ as $z\to z_0$ and $f$ is continuous at $w_0$, then, writing $A=f(w_0)$,
+>
 > $$
-> \lim _{z \rightarrow z_{0}} f(g(z))=A=f\left(\lim _{z \rightarrow z_{0}} g(z)\right) \tag{6}
+> \lim _{z \rightarrow z_{0}} f(g(z))=A=f\left(\lim _{z \rightarrow z_{0}} g(z)\right) 
 > $$
-> 
-> 
-
 
 
 The function $f(g(z))$ is called the composition of $f$ and $g$ and is also denoted $(f \circ g)(z)$. The proofs of (3)-(6) are similar to the proofs of the corresponding results from calculus. They are left to the exercises. Next, we illustrate these properties with some applications.
 
-> [!theorem] Theorem 2: The Squeeze Theorem
+<!-- Source label: Theorem 2: The Squeeze Theorem -->
+> [!theorem] The Squeeze Theorem
 > (i) Suppose that $f(z) \rightarrow 0$ as $z \rightarrow z_0$ and $|g(z)| \leq|f(z)|$ in a deleted neighborhood of $z_0$. Then $g(z) \rightarrow 0$ as $z \rightarrow z_0$.
 > (ii) Suppose that $f(z) \rightarrow 0$ as $z \rightarrow z_0$ and $g(z)$ is bounded in a deleted neighborhood of $z_0$. Then $f(z) g(z) \rightarrow 0$ as $z \rightarrow z_0$.
 
@@ -807,9 +811,10 @@
 
 
 
-> [!theorem] Theorem 3: REAL AND IMAGINARY PARTS OF LIMITS
+<!-- Source label: Theorem 3: REAL AND IMAGINARY PARTS OF LIMITS -->
+> [!theorem] REAL AND IMAGINARY PARTS OF LIMITS
 > Given a complex-valued function $f(z)=u(x, y)+i v(x, y)$ and a complex number $L=a+i b$, then
-> (8) $\lim _{z \rightarrow z_{0}} f(z)=L \Longleftrightarrow \lim _{z \rightarrow z_{0}} u(x, y)=a$ and $\lim _{z \rightarrow z_{0}} v(x, y)=b$.
+> $\lim _{z \rightarrow z_{0}} f(z)=L \Longleftrightarrow \lim _{z \rightarrow z_{0}} u(x, y)=a$ and $\lim _{z \rightarrow z_{0}} v(x, y)=b$.
 
 
 
@@ -1012,10 +1017,12 @@
 
 We have avoided thus far dealing with limits that involve $\infty$. What do we mean by statements such as $\lim _{z \rightarrow z_{0}} f(z)=\infty$ or $\lim _{z \rightarrow \infty} f(z)=L$ or even $\lim _{z \rightarrow \infty} f(z)=\infty$ ? We answer these questions and complete our discussion of limits by introducing the following definitions.
 
+<!-- Source label: Limits Involving Infinity -->
 > [!definition] Limits Involving Infinity
-> (i) We write $\lim _{z \rightarrow z_{0}} f(z)=\infty$ to mean that for any $M>0$ there is a $\delta>0$ such that $\left|z-z_{0}\right|<\delta \Rightarrow|f(z)|>M$.
+> (i) We write $\lim _{z \rightarrow z_{0}} f(z)=\infty$ to mean that for any $M>0$ there is a $\delta>0$ such that $0<\left|z-z_{0}\right|<\delta \Rightarrow|f(z)|>M$.
 > (ii) We write $\lim _{z \rightarrow \infty} f(z)=L$ to mean that for any $\epsilon>0$ there is an $R>0$ such that $|z|>R \Rightarrow|f(z)-L|<\epsilon$.
 > (iii) We write $\lim _{z \rightarrow \infty} f(z)=\infty$ to mean that for any $M>0$ there is an $R>0$ such that $|z|>R \Rightarrow|f(z)|>M$.
+
 
 Looking at these definitions, we see that $z \rightarrow \infty$ means that the real quantity $|z| \rightarrow \infty$, and similarly $f(z) \rightarrow \infty$ means that $|f(z)| \rightarrow \infty$. Hence
 
@@ -1278,19 +1285,21 @@
 
 Often, the limit of $f(z)$ as $z$ approaches $z_{0}$ will equal $f\left(z_{0}\right)$. Functions that satisfy this requirement are said to be continuous.
 
+<!-- Source label: Continuous Function -->
 > [!definition] Continuous Function
 > Suppose $f(z)$ is defined on a neighborhood of $z_{0}$. We say that $f(z)$ is continuous at the point $z_{0}$ if $\lim _{z \rightarrow z_{0}} f(z)$ exists and equals $f\left(z_{0}\right)$. We say $f$ is continuous on a set $S$ if it is continuous at every point in $S$.
 
 We see from Example 1 that the functions $f(z)=z$ and $f(z)=c$ are continuous at all points in the plane. To check the continuity of more complicated functions, we can appeal to the properties of limits. Since continuity is defined in terms of limits, many properties of limits extend to continuous functions.
 
 
-> [!theorem] Theorem 4 Properties of Continuous Functions
+<!-- Source label: Theorem 4 Properties of Continuous Functions -->
+> [!theorem] Properties of Continuous Functions
 > (i) If $f(z)$ and $g(z)$ are continuous at $z_{0}$, and $c_{1}, c_{2}$ are complex constants, then the following functions are continuous at $z_{0}$ :
-> 
+>
 > $$
 > c_{1} f(z)+c_{2} g(z), \quad f(z) g(z), \quad \frac{f(z)}{g(z)}\left(\text { provided } g\left(z_{0}\right) \neq 0\right)
 > $$
-> 
+>
 > (ii) If $g$ is continuous at $z_{0}$ and $f$ is continuous at $g\left(z_{0}\right)$, then the composition $h(z)=f(g(z))$ is continuous at $z_{0}$.
 > (iii) If $g(z)$ is real-valued and continuous at $z_{0}$ and $f(x)$ is continuous at $x_{0}=g\left(z_{0}\right)$, then the composition $h(z)=f(g(z))$ is continuous at $z_{0}$.
 > (iv) The function $f(z)=u(z)+i v(z)$ is continuous if and only if $u$ and $v$ are continuous.
@@ -1560,10 +1569,18 @@
 Our next example involves a function with infinitely many nonremovable discontinuities. In the example, we will use the uniqueness property of limits to show that a limit fails to exist. The method works as follows. If you can show that $f(z) \rightarrow L$ as $z$ approaches $z_{0}$ on curve $C$ _(Figure 2)_, but $f(z) \rightarrow L^{\prime}$ as $z$ approaches $z_{0}$ on curve $C^{\prime}$, and $L \neq L^{\prime}$, then, by the uniqueness of limits, we conclude that $\lim _{z \rightarrow z_{0}} f(z)$ does not exist.
 
 
-> [!figure] Figure 2
-> 
-> ![](./images/af4f9593-dec7-4bc0-8d78-d25500419ec9-15_463_496_1517_102.jpg)
-> If $L \neq L^{\prime}$, then the limit at $z_{0}$ cannot exist.
+```scientific-figure
+id: e67e6737-45f6-41ba-b369-644e9c78a41c
+numbered: false
+title: ""
+caption: "**Figure 2.** If $L \\neq L^{\\prime}$, then the limit at $z_{0}$ cannot exist."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 02 Analytic Functions/images/af4f9593-dec7-4bc0-8d78-d25500419ec9-15_463_496_1517_102.jpg
+    caption: ""
+```
 
 
 
@@ -1655,10 +1672,18 @@
 Also, for a point on the negative $x$-axis, $z_{0}=x_{0}<0$, we have $\operatorname{Arg} z_{0}=\pi$. If $z$ approaches $z_{0}$ from the second quadrant, say along curve $C$ in _Figure 3_, we have $\lim _{z \rightarrow z_{0}} \operatorname{Arg} z=\pi=\operatorname{Arg} z_{0}$. But if $z$ approaches $z_{0}$ from the third quadrant, say along curve $C^{\prime}$ in _Figure 3_, we have $\lim _{z \rightarrow z_{0}} \operatorname{Arg} z=-\pi$. Hence $\operatorname{Arg} z$ is not continuous at $z_{0}$ and the discontinuity is not removable, because $\lim _{z \rightarrow z_{0}} \operatorname{Arg} z$ does not exist for such $z_{0}$.
 
 
-> [!figure] Figure 3
-> 
-> ![](./images/af4f9593-dec7-4bc0-8d78-d25500419ec9-16_476_537_281_116.jpg)
-> Figure $3 \operatorname{Arg} z$ has nonremovable discontinuities at $z=$ 0 and at all negative real $z$. For all other $z, \operatorname{Arg} z$ is continuous.
+```scientific-figure
+id: 8ce1a5bb-c30e-4c75-ac6f-45d76fd41e8f
+numbered: false
+title: ""
+caption: "**Figure 3.** Figure $3 \\operatorname{Arg} z$ has nonremovable discontinuities at $z=$ 0 and at all negative real $z$. For all other $z, \\operatorname{Arg} z$ is continuous."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 02 Analytic Functions/images/af4f9593-dec7-4bc0-8d78-d25500419ec9-16_476_537_281_116.jpg
+    caption: ""
+```
 
 
 
@@ -1798,7 +1823,8 @@
 
 Many important functions of several variables are made up of products, quotients and linear combinations of functions of a single variable. For example, the function $u(x, y)=e^{x} \cos y$ is the product of two functions of a single variable each; namely, $e^{x}$ and $\cos y$. The exponential function $e^{z}=e^{x}(\cos y+i \sin y)$ is a linear combination of two products of functions of a single variable. In establishing the continuity of such functions, the following simple observations are very useful.
 
-> [!proposition] Proposition 1
+<!-- Source label: Proposition 1 -->
+> [!proposition] Continuity of a Function Depending on One Cartesian Coordinate
 > Suppose that $\phi(x)$ is a continuous function of a single variable $x$ over an interval $(a, b)$. Then the function of two variables $f(x, y)=\phi(x)$ is continuous at $\left(x_{0}, y_{0}\right)$ whenever $x_{0}$ is in $(a, b)$. Similarly, $g(x, y)=\phi(y)$ is continuous, at $\left(x_{0}, y_{0}\right)$ whenever $y_{0}$ is in $(a, b)$.
 
 
@@ -1902,7 +1928,9 @@
 > Show that the absolute value $|z|$ is continuous.
 
 
-**Solution:** Let $z_0\in\mathbb{C}$ be fixed. We show that
+##### solution
+
+Let $z_0\in\mathbb{C}$ be fixed. We show that
 $$
 \lim_{z\to z_0}|z|=|z_0|.
 $$
@@ -2256,22 +2284,31 @@
 Understanding the behavior of the logarithm is crucial to certain applications. We will prove the following important result, which should not surprise you in view of what we already know about $\operatorname{Arg} z$ and $|z|$.
 
 
-> [!theorem] Theorem 5: THEOREM 5 CONTINUITY OF THE LOGARITHM
+<!-- Source label: Theorem 5: THEOREM 5 CONTINUITY OF THE LOGARITHM -->
+> [!theorem] CONTINUITY OF THE LOGARITHM
 > The principal branch of the logarithm
-> 
+>
 > $$
 > \log (z)=\ln |z|+i \operatorname{Arg}(z), \quad-\pi<\operatorname{Arg} z \leq \pi \quad(z \neq 0),
 > $$
-> 
-> is continuous for all $z$ in $\mathbb{C} \backslash(-\infty, 0]$. For $z$ in $(-\infty, 0]$, the discontinuities of $\log z$ are not removable _(Figure 4)_.
-
-
-
-
-> [!figure] Figure 4
-> 
-> ![](./images/af4f9593-dec7-4bc0-8d78-d25500419ec9-17_465_517_903_94.jpg)
-> Figure $4 \log z$ has nonremovable discontinuities at $z=$ 0 and at all negative real $z$. For all other $z, \log z$ is continuous.
+>
+> is continuous for all $z$ in $\mathbb{C} \backslash(-\infty, 0]$. For $z$ in $(-\infty, 0)$, the discontinuities of $\log z$ are not removable.
+
+
+
+
+```scientific-figure
+id: 25a683de-98de-4de8-8546-83913647f8b1
+numbered: false
+title: ""
+caption: "**Figure 4.** Figure $4 \\log z$ has nonremovable discontinuities at $z=$ 0 and at all negative real $z$. For all other $z, \\log z$ is continuous."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 02 Analytic Functions/images/af4f9593-dec7-4bc0-8d78-d25500419ec9-17_465_517_903_94.jpg
+    caption: ""
+```
 
 
 **Proof** 
@@ -2283,10 +2320,18 @@
 
 
 
-> [!figure] Figure 5
-> 
-> ![](./images/af4f9593-dec7-4bc0-8d78-d25500419ec9-17_461_507_1586_104.jpg)
-> Figure 5 The branch cut of $\log _{\alpha} z$ is the ray at angle $\alpha$. The branch cut is the set of nonremovable discontinuities of $\log _{\alpha} z$.
+```scientific-figure
+id: 1e0ba2fd-1c09-4f9e-b209-4e5c54b87253
+numbered: false
+title: ""
+caption: "**Figure 5.** The branch cut of $\\log _{\\alpha} z$ is the ray at angle $\\alpha$. The branch cut is the set of nonremovable discontinuities of $\\log _{\\alpha} z$."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 02 Analytic Functions/images/af4f9593-dec7-4bc0-8d78-d25500419ec9-17_461_507_1586_104.jpg
+    caption: ""
+```
 
 
 

`````
