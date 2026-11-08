
# Editorial records

Reading note: 5.7 The Counting Theorem and Rouché's Theorem.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Callout 218: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Argument Principle for Counting Zeros of an Analytic Function
> Suppose that $C$ is a simple closed positively oriented path, $\Omega$ is the region inside $C$, and $f$ is analytic inside and on $C$ and nonvanishing on $C$. Let $N(f)$ denote the number of zeros of $f$ inside $\Omega$, counted according to multiplicity. Then $N(f)$ is finite and
>
> $$
> N(f)=\frac{1}{2 \pi i} \int_C \frac{f^{\prime}(z)}{f(z)} d z
> $$
````
### After

````text
> [!theorem] Counting Theorem
> Suppose that $C$ is a simple closed positively oriented path, $\Omega$ is the region inside $C$, and $f$ is analytic inside and on $C$ and nonvanishing on $C$. Let $N(f)$ denote the number of zeros of $f$ inside $\Omega$, counted according to multiplicity. Then $N(f)$ is finite and
>
> $$
> N(f)=\frac{1}{2 \pi i} \int_C \frac{f^{\prime}(z)}{f(z)} d z
> $$
````

## 2. Callout 219: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Argument Principle for Zeros and Poles of a Meromorphic Function
> Suppose that $C$ is a simple closed positively oriented path, $\Omega$ is the region inside $C$, and $f$ is meromorphic on $\Omega$, analytic and nonvanishing on $C$. Let $N(f)$ denote the number of zeros of $f$ inside $\Omega$ and $P(f)$ denote the number of poles of $f$ inside $\Omega$, counted according to multiplicity. Then $N(f)$ and $P(f)$ are finite and
>
> $$
> N(f)-P(f)=\frac{1}{2 \pi i} \int_C \frac{f^{\prime}(z)}{f(z)} d z .
> $$
````
### After

````text
> [!theorem] Meromorphic Counting Theorem
> Suppose that $C$ is a simple closed positively oriented path, $\Omega$ is the region inside $C$, and $f$ is meromorphic on $\Omega$, analytic and nonvanishing on $C$. Let $N(f)$ denote the number of zeros of $f$ inside $\Omega$ and $P(f)$ denote the number of poles of $f$ inside $\Omega$, counted according to multiplicity. Then $N(f)$ and $P(f)$ are finite and
>
> $$
> N(f)-P(f)=\frac{1}{2 \pi i} \int_C \frac{f^{\prime}(z)}{f(z)} d z .
> $$
````

## 3. Callout 220: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Weighted Argument Principle for Meromorphic Functions
> Let $C$ be a simple closed positively oriented path with interior $\Omega$. Let $f$ be meromorphic inside and on $C$, with no zeros or poles on $C$, and let $g$ be analytic inside and on $C$. Let $z_1, z_2, \ldots, z_{n_1}$ denote the zeros of $f$ in $\Omega$ and $p_1, p_2, \ldots, p_{n_2}$ denote the poles of $f$ in $\Omega$. Let $m\left(z_j\right)$ and $m\left(p_j\right)$ denote the orders of the roots and poles. Then
>
> $$
> \frac{1}{2 \pi i} \int_C g(z) \frac{f^{\prime}(z)}{f(z)} d z=\sum_{j=1}^{n_1} m\left(z_j\right) g\left(z_j\right)-\sum_{j=1}^{n_2} m\left(p_j\right) g\left(p_j\right)
> $$
````
### After

````text
> [!theorem] Variant of the Counting Theorem
> Let $C$ be a simple closed positively oriented path with interior $\Omega$. Let $f$ be meromorphic inside and on $C$, with no zeros or poles on $C$, and let $g$ be analytic inside and on $C$. Let $z_1, z_2, \ldots, z_{n_1}$ denote the zeros of $f$ in $\Omega$ and $p_1, p_2, \ldots, p_{n_2}$ denote the poles of $f$ in $\Omega$. Let $m\left(z_j\right)$ and $m\left(p_j\right)$ denote the orders of the roots and poles. Then
>
> $$
> \frac{1}{2 \pi i} \int_C g(z) \frac{f^{\prime}(z)}{f(z)} d z=\sum_{j=1}^{n_1} m\left(z_j\right) g\left(z_j\right)-\sum_{j=1}^{n_2} m\left(p_j\right) g\left(p_j\right)
> $$
````

## 4. Callout 221: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!lemma] Constancy of Continuous Integer-Valued Functions on a Region
> Suppose that $\phi$ is continuous on a region $\Omega$ and $\phi(z)$ is an integer for all $z$ in $\Omega$ (in other words, $\phi$ is integer-valued). Then $\phi$ is constant on $\Omega$.
````
### After

````text
> [!lemma] Integer-Valued Functions
> Suppose that $\phi$ is continuous on a region $\Omega$ and $\phi(z)$ is an integer for all $z$ in $\Omega$ (in other words, $\phi$ is integer-valued). Then $\phi$ is constant on $\Omega$.
````

## 5. Callout 222: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Rouché's Theorem for Counting Complex Zeros
> Suppose that $C$ is a simple closed path, $\Omega$ is the region inside $C, f$ and $g$ are analytic inside and on $C$. If $|g(z)|<|f(z)|$ for all $z$ on $C$, then $N(f+g)=N(f)$; that is, $f+g$ and $f$ have the same number of zeros in $\Omega$, counted with multiplicity.
````
### After

````text
> [!theorem] Rouché's Theorem
> Suppose that $C$ is a simple closed path, $\Omega$ is the region inside $C, f$ and $g$ are analytic inside and on $C$. If $|g(z)|<|f(z)|$ for all $z$ on $C$, then $N(f+g)=N(f)$; that is, $f+g$ and $f$ have the same number of zeros in $\Omega$, counted with multiplicity.
````

## 6. Callout 223: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Local Multiplicity of a Nonconstant Analytic Mapping
> Let $f$ be a nonconstant analytic function in a neighborhood of $z_0$. Let $w_0=f\left(z_0\right)$ and $n$ be the order of the zero of $f(z)-f(z_0)$ at $z_0$. There exists $R>0$ and $\rho>0$ such that every $w \neq w_0$ in $B_\rho\left(w_0\right)$ is attained by $f$ at precisely $n$ distinct points in $B_R\left(z_0\right)$.
````
### After

````text
> [!theorem] Local Mapping Theorem
> Let $f$ be a nonconstant analytic function in a neighborhood of $z_0$. Let $w_0=f\left(z_0\right)$ and $n$ be the order of the zero of $f(z)-f(z_0)$ at $z_0$. There exists $R>0$ and $\rho>0$ such that every $w \neq w_0$ in $B_\rho\left(w_0\right)$ is attained by $f$ at precisely $n$ distinct points in $B_R\left(z_0\right)$.
````

## 7. Callout 224: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Local Injectivity and the Nonvanishing Complex Derivative
> Suppose that $f$ is analytic on a region $\Omega$ and $z_0$ is in $\Omega$. Then $f$ is one-to-one on some neighborhood $B_r\left(z_0\right)$ if and only if $f^{\prime}\left(z_0\right) \neq 0$.
````
### After

````text
> [!theorem] Inverse Function Theorem
> Suppose that $f$ is analytic on a region $\Omega$ and $z_0$ is in $\Omega$. Then $f$ is one-to-one on some neighborhood $B_r\left(z_0\right)$ if and only if $f^{\prime}\left(z_0\right) \neq 0$.
````

## 8. Callout 225: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!corollary] Open Mapping Theorem for Nonconstant Analytic Functions
> Let $f$ be analytic and nonconstant on a region $\Omega$; the open sets considered are subsets of $\Omega$.
>
> A nonconstant analytic function $f$ maps open sets into open sets. A function with this property is said to be open.
````
### After

````text
> [!corollary] Open Mapping Property
> Let $f$ be analytic and nonconstant on a region $\Omega$; the open sets considered are subsets of $\Omega$.
>
> A nonconstant analytic function $f$ maps open sets into open sets. A function with this property is said to be open.
````

## 9. Callout 226: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!corollary] Images of Regions Under Nonconstant Analytic Functions
> If $\Omega$ is a nonempty region (open and connected set) and $f$ is a nonconstant analytic function on $\Omega$, then $f[\Omega]$ is a region.
````
### After

````text
> [!corollary] Mapping of Regions
> If $\Omega$ is a nonempty region (open and connected set) and $f$ is a nonconstant analytic function on $\Omega$, then $f[\Omega]$ is a region.
````

## 10. Callout 227: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!corollary] Maximum Modulus Principle for Analytic Functions
> If $f$ is analytic on a region $\Omega$, such that $|f|$ attains a maximum at some point in $\Omega$, then $f$ is constant in $\Omega$.
````
### After

````text
> [!corollary] Maximum Modulus Principle
> If $f$ is analytic on a region $\Omega$, such that $|f|$ attains a maximum at some point in $\Omega$, then $f$ is constant in $\Omega$.
````

## 11. Callout 228: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Contour Integral Formula for a Local Analytic Inverse
> Write $w_0=f(z_0)$. Choose $R>0$ small enough that $f$ is analytic and one-to-one on a neighborhood of the closed disk $|z-z_0|\leq R$, and choose $\rho>0$ such that $B_\rho(w_0)$ lies inside its image. The circle $C_R(z_0)$ has positive orientation.
>
> Suppose that $f(z)$ is analytic at $z_0$ and $f^{\prime}\left(z_0\right) \neq 0$. Then $f$ has an inverse function $z=g(w)$ in a neighborhood $B_\rho\left(w_0\right)$ of $w_0$ given by
>
> $$
> g(w)=\frac{1}{2 \pi i} \int_{C_R\left(z_0\right)} z \frac{f^{\prime}(z)}{f(z)-w} d z
> $$
>
> Furthermore, $g(w)$ is analytic on $B_\rho\left(w_0\right)$.
````
### After

````text
> [!theorem] Inverse Function Formula
> Write $w_0=f(z_0)$. Choose $R>0$ small enough that $f$ is analytic and one-to-one on a neighborhood of the closed disk $|z-z_0|\leq R$, and choose $\rho>0$ such that $B_\rho(w_0)$ lies inside its image. The circle $C_R(z_0)$ has positive orientation.
>
> Suppose that $f(z)$ is analytic at $z_0$ and $f^{\prime}\left(z_0\right) \neq 0$. Then $f$ has an inverse function $z=g(w)$ in a neighborhood $B_\rho\left(w_0\right)$ of $w_0$ given by
>
> $$
> g(w)=\frac{1}{2 \pi i} \int_{C_R\left(z_0\right)} z \frac{f^{\prime}(z)}{f(z)-w} d z
> $$
>
> Furthermore, $g(w)$ is analytic on $B_\rho\left(w_0\right)$.
````

## 12. Callout 229: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!corollary] Analyticity and Derivative of a Global Complex Inverse
> Suppose that $f$ is analytic and one-to-one on a region $\Omega$. Then its inverse function $f^{-1}$ exists and is analytic on the region $f[\Omega]$. Moreover,
>
> $$
> \frac{d}{d w} f^{-1}(w)=\frac{1}{f^{\prime}(z)}, \quad \text { where } w=f(z)
> $$
````
### After

````text
> [!corollary] A Global Inverse Function
> Suppose that $f$ is analytic and one-to-one on a region $\Omega$. Then its inverse function $f^{-1}$ exists and is analytic on the region $f[\Omega]$. Moreover,
>
> $$
> \frac{d}{d w} f^{-1}(w)=\frac{1}{f^{\prime}(z)}, \quad \text { where } w=f(z)
> $$
````

## 13. Move editorial commentary out of the reading note.

### Before

````text
*Editorial note: [corrected] The logarithmic-derivative statement allows poles, so its common hypothesis is meromorphic, not analytic throughout the region.*
````
### After

````text

````

## Source-to-current comparison

Source: /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 05 Residue Theory/5.7 The Counting Theorem and Rouché's Theorem.md

This exact comparison preserves the full change evidence, including formatting, OCR corrections, restored source wording, and required standalone context. The entries above explain the recovery edits. The comparison is not a claim that every difference is a correction; component serialization, callout wrapping, and printed labels outside callouts are formatting.

`````diff
--- /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 05 Residue Theory/5.7 The Counting Theorem and Rouché's Theorem.md
+++ /Users/gradyclopton/ObsidianVaults/complex_analysis/Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 05 Residue Theory/5.7 The Counting Theorem and Rouché's Theorem.md
@@ -4,8 +4,9 @@
 In this section, we apply Cauchy's residue theorem to prove several important properties of analytic functions with fruitful applications. We start with a simple but very useful lemma.
 
 
-> [!lemma]
-> Suppose that $f$ is analytic and not identically zero in a region $\Omega$.
+<!-- Source label:  -->
+> [!lemma] Residues of a Logarithmic Derivative at Zeros and Poles
+> Suppose that $f$ is meromorphic and not identically zero in a region $\Omega$.
 > (i) If $z_0$ is a zero of $f$ of order $m \geq 1$, then $\frac{f^{\prime}(z)}{f(z)}$ has a simple pole at $z_0$ and the residue there is $m$.
 > (ii) If $z_0$ is a pole of $f$ of order $m \geq 1$, then $\frac{f^{\prime}(z)}{f(z)}$ has a simple pole at $z_0$ and the residue there is $-m$.
 
@@ -36,24 +37,31 @@
 
 
 
-> [!figure] Figure 1
-> 
-> ![](Pasted%20image%2020260421191043.png)
-> Figure 1 The number of zeros inside the circle according to multiplicity is 3 .
-
-
-
-
-
-
+```scientific-figure
+id: ceac5096-6d5c-46f0-9601-677a51193b61
+numbered: false
+title: ""
+caption: "**Figure 1.** The number of zeros inside the circle according to multiplicity is 3 ."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 05 Residue Theory/images/Pasted image 20260421191043.png
+    caption: ""
+```
+
+
+
+
+
+
+<!-- Source label: Counting Theorem -->
 > [!theorem] Counting Theorem
 > Suppose that $C$ is a simple closed positively oriented path, $\Omega$ is the region inside $C$, and $f$ is analytic inside and on $C$ and nonvanishing on $C$. Let $N(f)$ denote the number of zeros of $f$ inside $\Omega$, counted according to multiplicity. Then $N(f)$ is finite and
-> 
+>
 > $$
 > N(f)=\frac{1}{2 \pi i} \int_C \frac{f^{\prime}(z)}{f(z)} d z
 > $$
-> 
-> 
 
 
 **Proof** If $f$ has no zeros in $\Omega$ (hence $N(f)=0$ ), then $\frac{f^{\prime}(z)}{f(z)}$ is analytic on $\Omega$ and (3) follows from Cauchy's theorem. Note that $f$ cannot have infinitely many zeros in $\Omega$, by Corollary 2, Section 4.6. Let $z_1, z_2, \ldots, z_n$ denote the zeros of $f$ inside $\Omega$. By Lemma $1, \frac{f^{\prime}(z)}{f(z)}$ has simple poles in $\Omega$ located at $z_j$ and the residue at $z_j$ is the order of the zero at $z_j$. Thus (3) follows at once from the residue theorem.
@@ -65,14 +73,13 @@
 
 
 
+<!-- Source label: Meromorphic Counting Theorem -->
 > [!theorem] Meromorphic Counting Theorem
 > Suppose that $C$ is a simple closed positively oriented path, $\Omega$ is the region inside $C$, and $f$ is meromorphic on $\Omega$, analytic and nonvanishing on $C$. Let $N(f)$ denote the number of zeros of $f$ inside $\Omega$ and $P(f)$ denote the number of poles of $f$ inside $\Omega$, counted according to multiplicity. Then $N(f)$ and $P(f)$ are finite and
-> 
+>
 > $$
 > N(f)-P(f)=\frac{1}{2 \pi i} \int_C \frac{f^{\prime}(z)}{f(z)} d z .
 > $$
-> 
-> 
 
 
 **Proof** That $N(f)$ and $P(f)$ are finite follows as in the proof of Theorem 1. Apply the residue theorem and use Lemma 1 to see that (4) holds.
@@ -89,10 +96,18 @@
 
 
 
-> [!figure]
-> 
-> ![](Pasted%20image%2020260421192624.png)
-> Figure 2 The image $f\left[\gamma_1\right]$ is contained in a simply connected region not containing the origin. We can define the branch $\arg _1 z$ on this region.
+```scientific-figure
+id: 7997f0b0-b5f3-4aa7-8773-a28c4fd15d76
+numbered: false
+title: ""
+caption: "**Figure 2.** The image $f\\left[\\gamma_1\\right]$ is contained in a simply connected region not containing the origin. We can define the branch $\\arg _1 z$ on this region."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 05 Residue Theory/images/Pasted image 20260421192624.png
+    caption: ""
+```
 
 
 
@@ -100,10 +115,18 @@
 
 
 
-> [!figure]
-> 
-> ![](Pasted%20image%2020260421192549.png)
-> Figure 3 The point $f(z)$ travels twice around the origin and $\Delta_C \arg f=4 \pi$.
+```scientific-figure
+id: b0190545-c01c-40ad-8c23-79cbf4a9c2f7
+numbered: false
+title: ""
+caption: "**Figure 3.** The point $f(z)$ travels twice around the origin and $\\Delta_C \\arg f=4 \\pi$."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 05 Residue Theory/images/Pasted image 20260421192549.png
+    caption: ""
+```
 
 
 
@@ -135,14 +158,24 @@
 
 
 
-**Solution** We will apply the argument principle, which in this case is expressed by $\frac{1}{2 \pi} \Delta_C \arg f=N(f)$ since $f$ has no poles. The contour $C$ will be a closed quarter of a circle of radius $R>0$, as shown in Figure 4. 
-
-
-
-> [!figure]
-> 
-> ![](Pasted%20image%2020260421192511.png)
-> Figure 4 The closed quarter circle $C$ of radius $R>0$.
+##### solution
+
+We will apply the argument principle, which in this case is expressed by $\frac{1}{2 \pi} \Delta_C \arg f=N(f)$ since $f$ has no poles. The contour $C$ will be a closed quarter of a circle of radius $R>0$, as shown in Figure 4. 
+
+
+
+```scientific-figure
+id: 1a1f66ec-0f9a-4b74-b9d6-8d5f4375d8a9
+numbered: false
+title: ""
+caption: "**Figure 4.** The closed quarter circle $C$ of radius $R>0$."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 05 Residue Theory/images/Pasted image 20260421192511.png
+    caption: ""
+```
 
 
 
@@ -161,10 +194,18 @@
 
 
 
-> [!figure]
-> 
-> ![](Pasted%20image%2020260421192441.png)
-> Figure 5 The path $f[C]$ (pictured for $R=2$ ) goes around the origin once.
+```scientific-figure
+id: b7817a18-0405-4e4f-b918-3db4c9c30cee
+numbered: false
+title: ""
+caption: "**Figure 5.** The path $f[C]$ (pictured for $R=2$ ) goes around the origin once."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 05 Residue Theory/images/Pasted image 20260421192441.png
+    caption: ""
+```
 
 
 
@@ -179,13 +220,13 @@
 We give one more variant of the counting theorem.
 
 
+<!-- Source label: Variant of the Counting Theorem -->
 > [!theorem] Variant of the Counting Theorem
-> Let $C, \Omega$, and $f$ be as in Theorem 2, let $g$ be analytic inside and on $C$. Let $z_1, z_2, \ldots, z_{n_1}$ denote the zeros of $f$ in $\Omega$ and $p_1, p_2, \ldots, p_{n_2}$ denote the poles of $f$ in $\Omega$. Let $m\left(z_j\right)$ and $m\left(p_j\right)$ denote the orders of the roots and poles. Then
-> 
+> Let $C$ be a simple closed positively oriented path with interior $\Omega$. Let $f$ be meromorphic inside and on $C$, with no zeros or poles on $C$, and let $g$ be analytic inside and on $C$. Let $z_1, z_2, \ldots, z_{n_1}$ denote the zeros of $f$ in $\Omega$ and $p_1, p_2, \ldots, p_{n_2}$ denote the poles of $f$ in $\Omega$. Let $m\left(z_j\right)$ and $m\left(p_j\right)$ denote the orders of the roots and poles. Then
+>
 > $$
 > \frac{1}{2 \pi i} \int_C g(z) \frac{f^{\prime}(z)}{f(z)} d z=\sum_{j=1}^{n_1} m\left(z_j\right) g\left(z_j\right)-\sum_{j=1}^{n_2} m\left(p_j\right) g\left(p_j\right)
 > $$
-> 
 
 
 
@@ -220,7 +261,9 @@
 
 
 
-**Solution** The function $f(z)=e^z-1$ has a zero at $z=0$ and, because $f^{\prime}(0)=1 \neq$ 0 , this zero is simple. Also, using the $2 \pi i$-periodicity of $e^z$ (see(13), Section 1.5 ), it is easy to see that $e^z=1$ inside the unit disk $|z|<1$ only at $z=0$. From (6) applied with $f(z)=e^z-1$ and $g(z)=\cos z$, it follows immediately that
+##### solution
+
+The function $f(z)=e^z-1$ has a zero at $z=0$ and, because $f^{\prime}(0)=1 \neq$ 0 , this zero is simple. Also, using the $2 \pi i$-periodicity of $e^z$ (see(13), Section 1.5 ), it is easy to see that $e^z=1$ inside the unit disk $|z|<1$ only at $z=0$. From (6) applied with $f(z)=e^z-1$ and $g(z)=\cos z$, it follows immediately that
 
 $$
 \int_{C_1(0)} \frac{e^z \cos z}{e^z-1} d z=2 \pi i \cos 0=2 \pi i
@@ -233,6 +276,7 @@
 As an application of the counting principle we will prove a famous result known as Rouché's theorem, named after the French mathematician and educator Eugène Rouché (1832-1910). We need a simple lemma.
 
 
+<!-- Source label: Integer-Valued Functions -->
 > [!lemma] Integer-Valued Functions
 > Suppose that $\phi$ is continuous on a region $\Omega$ and $\phi(z)$ is an integer for all $z$ in $\Omega$ (in other words, $\phi$ is integer-valued). Then $\phi$ is constant on $\Omega$.
 
@@ -245,8 +289,9 @@
 
 
 
+<!-- Source label: Rouché's Theorem -->
 > [!theorem] Rouché's Theorem
-> Suppose that $C$ is a simple closed path, $\Omega$ is the region inside $C, f$ and $g$ are analytic inside and on $C$. If $|g(z)|<|f(z)|$ for all $z$ on $C$, then $N(f+g)=N(f)$; that is, $f+g$ and $f$ have the same number of zeros on $\Omega$.
+> Suppose that $C$ is a simple closed path, $\Omega$ is the region inside $C, f$ and $g$ are analytic inside and on $C$. If $|g(z)|<|f(z)|$ for all $z$ on $C$, then $N(f+g)=N(f)$; that is, $f+g$ and $f$ have the same number of zeros in $\Omega$, counted with multiplicity.
 
 
 
@@ -273,10 +318,18 @@
 
 
 
-> [!figure] Figure 6
-> 
-> ![](Pasted%20image%2020260421192351.png)
-> Figure 6 Since $|g(z)|< |f(z)|$, the point $f(z)+g(z)$ goes around the origin the same number of times as $f(z)$.
+```scientific-figure
+id: 9feb3ee0-60d3-4309-bb57-ebf80f53f173
+numbered: false
+title: ""
+caption: "**Figure 6.** Since $|g(z)|< |f(z)|$, the point $f(z)+g(z)$ goes around the origin the same number of times as $f(z)$."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 05 Residue Theory/images/Pasted image 20260421192351.png
+    caption: ""
+```
 
 
 
@@ -291,7 +344,9 @@
 
 
 
-**Solution** (a) Since $p$ is a polynomial of degree 4, it is enough to show that $N(p)=$ 4 inside the circle $|z|=2$. Take $f(z)=z^4$ and $g(z)=6 z+3$ and note that $f(z)+g(z)=p(z)$. For $|z|=2$, we have $|f(z)|=2^4=32$ and $|g(z)| \leq|6 z|+3=15$. Hence $|g(z)|<|f(z)|$ for all $z$ on the circle $|z|=2$, and so by Roucheé's theorem $N(f)=N(f+g)=N(p)$. Clearly $f$ has one zero with multiplicity 4 at $z=0$. Thus $N(f)=4$ and so $N(p)=4$, as desired.
+##### solution
+
+(a) Since $p$ is a polynomial of degree 4, it is enough to show that $N(p)=$ 4 inside the circle $|z|=2$. Take $f(z)=z^4$ and $g(z)=6 z+3$ and note that $f(z)+g(z)=p(z)$. For $|z|=2$, we have $|f(z)|=2^4=32$ and $|g(z)| \leq|6 z|+3=15$. Hence $|g(z)|<|f(z)|$ for all $z$ on the circle $|z|=2$, and so by Roucheé's theorem $N(f)=N(f+g)=N(p)$. Clearly $f$ has one zero with multiplicity 4 at $z=0$. Thus $N(f)=4$ and so $N(p)=4$, as desired.
 (b) Take $f(z)=a z^n$ and $g(z)=-e^z$. Counted according to multiplicity, $f$ has $n$ zeros in $|z|<1$ and so $N(f)=n$. For $|z|=1,|f(z)|=\left|a z^n\right|=a$ and
 
 $$
@@ -315,7 +370,9 @@
 
 
 
-**Solution** Take $f(z)=a_n z^n$. Then $f$ has a zero of multiplicity $n$ at $z=0$. Also, for $|z|=R$, we have $|f(z)|=\left|a_n\right| R^n$, which is a polynomial of degree $n$ in $R$. Now let $g(z)=a_{n-1} z^{n-1}+\cdots+a_1 z+a_0$, then $|g(z)| \leq\left|a_{n-1}\right|\left|z^{n-1}\right|+\cdots+\left|a_1\right||z|+\left|a_0\right|$, and so for $|z|=R,|g(z)| \leq\left|a_{n-1}\right| R^{n-1}+\cdots+\left|a_1\right| R+\left|a_0\right|$. Since the modulus of $f$ grows at a faster rate than the modulus of $g$, in the sense that
+##### solution
+
+Take $f(z)=a_n z^n$. Then $f$ has a zero of multiplicity $n$ at $z=0$. Also, for $|z|=R$, we have $|f(z)|=\left|a_n\right| R^n$, which is a polynomial of degree $n$ in $R$. Now let $g(z)=a_{n-1} z^{n-1}+\cdots+a_1 z+a_0$, then $|g(z)| \leq\left|a_{n-1}\right|\left|z^{n-1}\right|+\cdots+\left|a_1\right||z|+\left|a_0\right|$, and so for $|z|=R,|g(z)| \leq\left|a_{n-1}\right| R^{n-1}+\cdots+\left|a_1\right| R+\left|a_0\right|$. Since the modulus of $f$ grows at a faster rate than the modulus of $g$, in the sense that
 
 $$
 \lim _{R \rightarrow \infty} \frac{1}{\left|a_n\right| R^n}\left(\left|a_{n-1}\right| R^{n-1}+\cdots+\left|a_1\right| R+\left|a_0\right|\right)=0,
@@ -333,8 +390,9 @@
 
 
 
+<!-- Source label: Local Mapping Theorem -->
 > [!theorem] Local Mapping Theorem
-> Let $f$ be a nonconstant analytic function in a neighborhood of $z_0$. Let $w_0=f\left(z_0\right)$ and $n$ be the order of $f$ at $z_0$. There exists $R>0$ and $\rho>0$ such that every $w \neq w_0$ in $B_\rho\left(w_0\right)$ is attained by $f$ at precisely $n$ distinct points in $B_R\left(z_0\right)$,
+> Let $f$ be a nonconstant analytic function in a neighborhood of $z_0$. Let $w_0=f\left(z_0\right)$ and $n$ be the order of the zero of $f(z)-f(z_0)$ at $z_0$. There exists $R>0$ and $\rho>0$ such that every $w \neq w_0$ in $B_\rho\left(w_0\right)$ is attained by $f$ at precisely $n$ distinct points in $B_R\left(z_0\right)$.
 
 
 **Proof** Since $f(z)-w_0$ has a zero of order $n \geq 1$, write $f(z)-w_0=a_n\left(z-z_0\right)^n+$
@@ -365,6 +423,7 @@
 The case $n=1$ of the theorem deserves a separate statement.
 
 
+<!-- Source label: Inverse Function Theorem -->
 > [!theorem] Inverse Function Theorem
 > Suppose that $f$ is analytic on a region $\Omega$ and $z_0$ is in $\Omega$. Then $f$ is one-to-one on some neighborhood $B_r\left(z_0\right)$ if and only if $f^{\prime}\left(z_0\right) \neq 0$.
 
@@ -403,7 +462,10 @@
 The following two corollaries describe important properties of analytic functions, which are direct applications of the local mapping theorem.
 
 
+<!-- Source label: Open Mapping Property -->
 > [!corollary] Open Mapping Property
+> Let $f$ be analytic and nonconstant on a region $\Omega$; the open sets considered are subsets of $\Omega$.
+>
 > A nonconstant analytic function $f$ maps open sets into open sets. A function with this property is said to be open.
 
 
@@ -414,6 +476,7 @@
 
 
 
+<!-- Source label: Mapping of Regions -->
 > [!corollary] Mapping of Regions
 > If $\Omega$ is a nonempty region (open and connected set) and $f$ is a nonconstant analytic function on $\Omega$, then $f[\Omega]$ is a region.
 
@@ -428,6 +491,7 @@
 
 
 
+<!-- Source label: Maximum Modulus Principle -->
 > [!corollary] Maximum Modulus Principle
 > If $f$ is analytic on a region $\Omega$, such that $|f|$ attains a maximum at some point in $\Omega$, then $f$ is constant in $\Omega$.
 
@@ -436,9 +500,18 @@
 
 
 
-> [!figure] Figure 7
-> ![](Pasted%20image%2020260421193319.png)
-> 
+```scientific-figure
+id: e87a2c22-0d43-4e2d-956a-b355230c722b
+numbered: false
+title: ""
+caption: "**Figure 7.**"
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 05 Residue Theory/images/Pasted image 20260421193319.png
+    caption: ""
+```
 
 
 +++
@@ -449,14 +522,16 @@
 
 
 
+<!-- Source label: Inverse Function Formula -->
 > [!theorem] Inverse Function Formula
+> Write $w_0=f(z_0)$. Choose $R>0$ small enough that $f$ is analytic and one-to-one on a neighborhood of the closed disk $|z-z_0|\leq R$, and choose $\rho>0$ such that $B_\rho(w_0)$ lies inside its image. The circle $C_R(z_0)$ has positive orientation.
+>
 > Suppose that $f(z)$ is analytic at $z_0$ and $f^{\prime}\left(z_0\right) \neq 0$. Then $f$ has an inverse function $z=g(w)$ in a neighborhood $B_\rho\left(w_0\right)$ of $w_0$ given by
-> 
+>
 > $$
 > g(w)=\frac{1}{2 \pi i} \int_{C_R\left(z_0\right)} z \frac{f^{\prime}(z)}{f(z)-w} d z
 > $$
-> 
-> 
+>
 > Furthermore, $g(w)$ is analytic on $B_\rho\left(w_0\right)$.
 
 
@@ -473,14 +548,13 @@
 
 
 
+<!-- Source label: A Global Inverse Function -->
 > [!corollary] A Global Inverse Function
 > Suppose that $f$ is analytic and one-to-one on a region $\Omega$. Then its inverse function $f^{-1}$ exists and is analytic on the region $f[\Omega]$. Moreover,
-> 
+>
 > $$
 > \frac{d}{d w} f^{-1}(w)=\frac{1}{f^{\prime}(z)}, \quad \text { where } w=f(z)
 > $$
-> 
-> 
 
 **Proof** By Theorem 7, $f^{-1}$ is analytic in a neighborhood of each point in $\Omega$, and hence it is analytic on $\Omega$. Also, since $f$ is one-to-one, Theorem 6 implies that $f^{\prime}(z) \neq 0$ for all $z$ in $\Omega$. Differentiating both sides of the identity $z=f^{-1}(f(z))$, we obtain $1=\frac{d}{d w} f^{-1}(w) f^{\prime}(z)$, which is equivalent to (11).
 
@@ -525,9 +599,18 @@
 > [!exercise]
 > 7. Show that the equation $3-z+2 e^{-z}=0$ has exactly one root in the right half-plane $\operatorname{Re} z>0$. **(Hint: Use Rouché's theorem and contours such as the one in Figure 8.)**
 > 
-> > [!figure]
-> > ![](Pasted%20image%2020260421193822.png)
-> > 
+> ```scientific-figure
+> id: 73299342-34a7-4cf4-9610-eb84a353cca7
+> numbered: false
+> title: ""
+> caption: ""
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 05 Residue Theory/images/Pasted image 20260421193822.png
+>     caption: ""
+> ```
 > 
 
 

`````
