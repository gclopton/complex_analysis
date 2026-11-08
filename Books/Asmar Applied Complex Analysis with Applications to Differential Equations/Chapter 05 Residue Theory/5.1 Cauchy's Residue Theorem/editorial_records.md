
# Editorial records

Reading note: 5.1 Cauchy's Residue Theorem.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Callout 204: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!proposition] Residue Formulas at Simple Poles
> (i) If $f(z)$ has a simple pole at $z_{0}$, then
>
> $$
> \operatorname{Res}\left(f, z_{0}\right)=\lim _{z \rightarrow z_{0}}\left(z-z_{0}\right) f(z)
> $$
>
> (ii) If $f(z)=\frac{p(z)}{q(z)}$, where $p$ and $q$ are analytic at $z_{0}, p\left(z_{0}\right) \neq 0$, and $q(z)$ has a simple zero at $z_{0}$, then
>
> $$
> \operatorname{Res}\left(\frac{p(z)}{q(z)}, z_{0}\right)=\frac{p\left(z_{0}\right)}{q^{\prime}\left(z_{0}\right)}
> $$
>
> (iii) If $f(z)$ has a simple pole at $z_{0}$ and $g$ is analytic at $z_{0}$,
>
> $$
> \operatorname{Res}\left(f(z) g(z), z_{0}\right)=g\left(z_{0}\right) \operatorname{Res}\left(f(z), z_{0}\right)
> $$
>
> (iv) If $g$ is analytic at $z_{0}$, then
>
> $$
> \operatorname{Res}\left(\frac{g(z)}{z-z_{0}}, z_{0}\right)=g\left(z_{0}\right)
> $$
````
### After

````text
> [!proposition] Residue at a Simple Monopole
> (i) If $f(z)$ has a simple pole at $z_{0}$, then
>
> $$
> \operatorname{Res}\left(f, z_{0}\right)=\lim _{z \rightarrow z_{0}}\left(z-z_{0}\right) f(z)
> $$
>
> (ii) If $f(z)=\frac{p(z)}{q(z)}$, where $p$ and $q$ are analytic at $z_{0}, p\left(z_{0}\right) \neq 0$, and $q(z)$ has a simple zero at $z_{0}$, then
>
> $$
> \operatorname{Res}\left(\frac{p(z)}{q(z)}, z_{0}\right)=\frac{p\left(z_{0}\right)}{q^{\prime}\left(z_{0}\right)}
> $$
>
> (iii) If $f(z)$ has a simple pole at $z_{0}$ and $g$ is analytic at $z_{0}$,
>
> $$
> \operatorname{Res}\left(f(z) g(z), z_{0}\right)=g\left(z_{0}\right) \operatorname{Res}\left(f(z), z_{0}\right)
> $$
>
> (iv) If $g$ is analytic at $z_{0}$, then
>
> $$
> \operatorname{Res}\left(\frac{g(z)}{z-z_{0}}, z_{0}\right)=g\left(z_{0}\right)
> $$
````

## 2. Callout 205: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Residue Formula at a Pole of Arbitrary Order
> Suppose that $z_{0}$ is a pole of order $m \geq 1$ of $f$. Then the residue of $f$ at $z_{0}$ is
>
> $$
> \operatorname{Res}\left(f, z_{0}\right)=\lim _{z \rightarrow z_{0}} \frac{1}{(m-1)!} \frac{d^{m-1}}{d z^{m-1}}\left[\left(z-z_{0}\right)^{m} f(z)\right]
> $$
>
> where as usual the derivative of order 0 of a function is the function itself.
````
### After

````text
> [!theorem] Residue at a Pole of Order $m$
> Suppose that $z_{0}$ is a pole of order $m \geq 1$ of $f$. Then the residue of $f$ at $z_{0}$ is
>
> $$
> \operatorname{Res}\left(f, z_{0}\right)=\lim _{z \rightarrow z_{0}} \frac{1}{(m-1)!} \frac{d^{m-1}}{d z^{m-1}}\left[\left(z-z_{0}\right)^{m} f(z)\right]
> $$
>
> where as usual the derivative of order 0 of a function is the function itself.
````

## 3. Move editorial commentary out of the reading note.

### Before

````text
*Editorial note: [typo fixed] Corrected the last singularity subscript to n and made the residue’s function explicit.*
````
### After

````text

````

## Source-to-current comparison

Source: /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 05 Residue Theory/5.1 Cauchy's Residue Theorem.md

This exact comparison preserves the full change evidence, including formatting, OCR corrections, restored source wording, and required standalone context. The entries above explain the recovery edits. The comparison is not a claim that every difference is a correction; component serialization, callout wrapping, and printed labels outside callouts are formatting.

`````diff
--- /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 05 Residue Theory/5.1 Cauchy's Residue Theorem.md
+++ /Users/gradyclopton/ObsidianVaults/complex_analysis/Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 05 Residue Theory/5.1 Cauchy's Residue Theorem.md
@@ -47,22 +47,30 @@
 
 
 
-> [!theorem] Theorem 1: Cauchy's Residue Theorem
-> Let $C$ be a simple closed positively oriented path. Suppose that $f$ is analytic inside and on $C$, except at finitely many isolated singularities $z_{1}, z_{2}, \ldots, z_{1}$ inside C. Then
-> 
-> $$
-> \int_{C} f(z) d z=2 \pi i \sum_{j=1}^{n} \operatorname{Res}\left(z_{j}\right)
-> $$
-> 
-> 
+<!-- Source label: Theorem 1: Cauchy's Residue Theorem -->
+> [!theorem] Cauchy's Residue Theorem
+> Let $C$ be a simple closed positively oriented path. Suppose that $f$ is analytic inside and on $C$, except at finitely many isolated singularities $z_{1}, z_{2}, \ldots, z_{n}$ inside C. Then
+>
+> $$
+> \int_{C} f(z) d z=2 \pi i \sum_{j=1}^{n} \operatorname{Res}\left(f,z_{j}\right)
+> $$
+
 
 **proof** Take amall circles $C_{r_{j}}\left(z_{j}\right)(j=1,2, \ldots, n)$ that do not intersect each other and are contained in the interior of $C$ (_Figure 1_). 
 
 
-> [!figure] Figure 1
-> 
-> ![300](./images/b1ad9866-c636-4d3b-85cb-e1f2bdb2e560-02_487_536_1536_125.jpg)
-> Figure 1 To compute the integral around a path $C$ of a function with multiple isolated singularities in the interior of $C$, we first carve out the singularities using non overlapping circles inside $C$, then use Cauchy's theorem for multiply connected regions.
+```scientific-figure
+id: 01b0459f-c546-40f7-b0bc-6f2619efc85c
+numbered: false
+title: ""
+caption: "**Figure 1.** To compute the integral around a path $C$ of a function with multiple isolated singularities in the interior of $C$, we first carve out the singularities using non overlapping circles inside $C$, then use Cauchy's theorem for multiply connected regions."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 05 Residue Theory/images/b1ad9866-c636-4d3b-85cb-e1f2bdb2e560-02_487_536_1536_125.jpg
+    caption: ""
+```
 
 
 
@@ -91,10 +99,18 @@
 > 
 > 
 > 
-> > [!figure] Figure 2
-> > 
-> > ![300](./images/b1ad9866-c636-4d3b-85cb-e1f2bdb2e560-03_488_467_592_37.jpg)
-> > Figure 2 The path $C$ and the puss of $f(z)$ in Example 1.
+> ```scientific-figure
+> id: 3f1ff7ca-5ecb-4381-8e00-761fb02f9813
+> numbered: false
+> title: ""
+> caption: "**Figure 2.** The path $C$ and the poles of $f(z)$ in Example 1."
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 05 Residue Theory/images/b1ad9866-c636-4d3b-85cb-e1f2bdb2e560-03_488_467_592_37.jpg
+>     caption: ""
+> ```
 > 
 > 
 > Find
@@ -105,13 +121,15 @@
 > 
 > 
 
-**solution** The function $f(z)=\frac{1}{z^{x^{2}}-1}$ has isolated singularities at $z= \pm 1$ and $\pm t$. Three of these are inside $C$, and according to (2) we have
+##### solution
+
+The function $f(z)=\frac{1}{z^{4}-1}$ has isolated singularities at $z= \pm 1$ and $\pm i$. Three of these are inside $C$, and according to (2) we have
 
 $$
 \int_{C} \frac{d z}{z^{4}-1}=2 \pi i(\operatorname{Res}(1)+\operatorname{Res}(i)+\operatorname{Res}(-i))
 $$
 
-To compute the residues, we will find the Laurent series of $f(z)$ around each isolated singularity and obtain the residue as the coefficient $a_{-1}$ in each case. We have $z^{4}-1=(z-1)(z+1)(z-i)(z+i)$, so $\pm 1$ and $\pm i$ are simple roots of the polynomial $z^{4}-1=0$. Hence $f(z)=\frac{1}{z^{x^{2}}-1}$ has simple poles at $\pm 1$ and $\pm i$ (Theorem 7(v), Section 4.6). Let $z_{0}$ denote any one of the points $1, \pm i$. Because $z_{0}$ is a simple pole, $f$ has a Laurent series expansion around $z_{0}$ of the form
+To compute the residues, we will find the Laurent series of $f(z)$ around each isolated singularity and obtain the residue as the coefficient $a_{-1}$ in each case. We have $z^{4}-1=(z-1)(z+1)(z-i)(z+i)$, so $\pm 1$ and $\pm i$ are simple roots of the polynomial $z^{4}-1=0$. Hence $f(z)=\frac{1}{z^{4}-1}$ has simple poles at $\pm 1$ and $\pm i$ (Theorem 7(v), Section 4.6). Let $z_{0}$ denote any one of the points $1, \pm i$. Because $z_{0}$ is a simple pole, $f$ has a Laurent series expansion around $z_{0}$ of the form
 
 $$
 f(z)=\frac{a_{-1}}{z-z_{0}}+a_{0}+a_{1}\left(z-z_{0}\right)+a_{2}\left(z-z_{0}\right)^{2}+\cdots
@@ -147,7 +165,7 @@
 and at $z=-i$,
 
 $$
-\operatorname{Res}(-i)=\lim _{z \rightarrow-1}(z+i) \frac{1}{z^{4}-1}=\left.\frac{1}{(z-1)(z+1)(z-i)}\right|_{z=-i}=-\frac{i}{4}
+\operatorname{Res}(-i)=\lim _{z \rightarrow-i}(z+i) \frac{1}{z^{4}-1}=\left.\frac{1}{(z-1)(z+1)(z-i)}\right|_{z=-i}=-\frac{i}{4}
 $$
 
 Plugging these values into (3), we obtain
@@ -165,33 +183,31 @@
 
 
 
-> [!proposition] Proposition 1: Residue at a Simple Monopole
-> 
+<!-- Source label: Proposition 1: Residue at a Simple Monopole -->
+> [!proposition] Residue at a Simple Monopole
 > (i) If $f(z)$ has a simple pole at $z_{0}$, then
-> 
+>
 > $$
 > \operatorname{Res}\left(f, z_{0}\right)=\lim _{z \rightarrow z_{0}}\left(z-z_{0}\right) f(z)
 > $$
-> 
+>
 > (ii) If $f(z)=\frac{p(z)}{q(z)}$, where $p$ and $q$ are analytic at $z_{0}, p\left(z_{0}\right) \neq 0$, and $q(z)$ has a simple zero at $z_{0}$, then
-> 
+>
 > $$
 > \operatorname{Res}\left(\frac{p(z)}{q(z)}, z_{0}\right)=\frac{p\left(z_{0}\right)}{q^{\prime}\left(z_{0}\right)}
 > $$
-> 
+>
 > (iii) If $f(z)$ has a simple pole at $z_{0}$ and $g$ is analytic at $z_{0}$,
-> 
+>
 > $$
 > \operatorname{Res}\left(f(z) g(z), z_{0}\right)=g\left(z_{0}\right) \operatorname{Res}\left(f(z), z_{0}\right)
 > $$
-> 
+>
 > (iv) If $g$ is analytic at $z_{0}$, then
-> 
+>
 > $$
 > \operatorname{Res}\left(\frac{g(z)}{z-z_{0}}, z_{0}\right)=g\left(z_{0}\right)
 > $$
-> 
-> 
 
 
 
@@ -209,13 +225,14 @@
 For poles of higher order the situation is more complicated.
 
 
-> [!theorem] Theorem 2: Residue at a Pole of Order $m$
+<!-- Source label: Theorem 2: Residue at a Pole of Order $m$ -->
+> [!theorem] Residue at a Pole of Order $m$
 > Suppose that $z_{0}$ is a pole of order $m \geq 1$ of $f$. Then the residue of $f$ at $z_{0}$ is
-> 
+>
 > $$
 > \operatorname{Res}\left(f, z_{0}\right)=\lim _{z \rightarrow z_{0}} \frac{1}{(m-1)!} \frac{d^{m-1}}{d z^{m-1}}\left[\left(z-z_{0}\right)^{m} f(z)\right]
 > $$
-> 
+>
 > where as usual the derivative of order 0 of a function is the function itself.
 
 
@@ -254,10 +271,18 @@
 > 
 > 
 > 
-> > [!figure] Figure 3
-> > 
-> > ![300](./images/b1ad9866-c636-4d3b-85cb-e1f2bdb2e560-05_486_474_988_66.jpg)
-> > Figure 3 The path $C$ and the poles of $f(z)$ in Example 2.
+> ```scientific-figure
+> id: bec32243-6bf8-4843-9877-0f2311dc106b
+> numbered: false
+> title: ""
+> caption: "**Figure 3.** The path $C$ and the poles of $f(z)$ in Example 2."
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 05 Residue Theory/images/b1ad9866-c636-4d3b-85cb-e1f2bdb2e560-05_486_474_988_66.jpg
+>     caption: ""
+> ```
 > 
 > 
 > 
@@ -270,7 +295,9 @@
 > 
 
 
-**solution** (a) Three steps are involved in answering this question.
+##### solution
+
+(a) Three steps are involved in answering this question.
 Step 1: Determine the singularities of $f$ inside $C$. The function $f(z)=\frac{z^{2}}{\left(z^{2}+\pi^{2}\right)^{2} \sin z}$ is analytic except where $z^{2}+\pi^{2}=0$ or $\sin z=0$. Thus $f$ has isolated singularities at $\pm i \pi$ and at $k \pi$ where $k$ is an integer. Only 0 and $i \pi$ are inside $C$.
 Step 2: Determine the type of the singularities of $f$ inside $C$. Let us start with the singularity at 0 . Using $\lim _{z \rightarrow 0} \frac{\sin z}{z}=1$, it follows that $\lim _{z \rightarrow 0} \frac{z}{\sin z}=1$, and so
 
@@ -317,7 +344,9 @@
 > Let $f(z)=\frac{(z+1)^{3}}{(z-1)^{2}}$. Find $\operatorname{Res}(f(z), 1)$.
 
 
-**solution** We can rewrite the numerator in terms of $z-1$ and write $f(z)$ as its own Laurent series expansion. We have
+##### solution
+
+We can rewrite the numerator in terms of $z-1$ and write $f(z)$ as its own Laurent series expansion. We have
 
 $$
 \begin{aligned}
@@ -352,14 +381,24 @@
 > where $C$ is the positively oriented rectangular path shown in _Figure 4_.
 > 
 > 
-> > [!figure] Figure 4
-> > 
-> > ![300](./images/b1ad9866-c636-4d3b-85cb-e1f2bdb2e560-06_477_539_1696_97.jpg)
-> > Figure 4 The path $C$ and the poles of $f(z) \cot (\pi z)$ in Example $4(c)$.
-> 
-> 
-
-**solution** (a) We know that the zeros of $\sin (\pi z)$ are precisely the integers. Also, it is immediate from Theorem 1, Section 4.6, that all the zeros of $\sin (\pi z)$ are simple zeros. Hence $\cot (\pi z)=\frac{\cos (\pi z)}{\sin (\pi z)}$ has simple poles at the integers. To find the residue at $k$, we can apply (9) with $m=1$ or, better yet, use Proposition 1(ii). We have
+> ```scientific-figure
+> id: e8419cb6-cccf-40a1-925a-fc07628e27a8
+> numbered: false
+> title: ""
+> caption: "**Figure 4.** The path $C$ and the poles of $f(z) \\cot (\\pi z)$ in Example $4(c)$."
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 05 Residue Theory/images/b1ad9866-c636-4d3b-85cb-e1f2bdb2e560-06_477_539_1696_97.jpg
+>     caption: ""
+> ```
+> 
+> 
+
+##### solution
+
+(a) We know that the zeros of $\sin (\pi z)$ are precisely the integers. Also, it is immediate from Theorem 1, Section 4.6, that all the zeros of $\sin (\pi z)$ are simple zeros. Hence $\cot (\pi z)=\frac{\cos (\pi z)}{\sin (\pi z)}$ has simple poles at the integers. To find the residue at $k$, we can apply (9) with $m=1$ or, better yet, use Proposition 1(ii). We have
 
 $$
 \operatorname{Res}(\cot (\pi z), k)=\operatorname{Res}\left(\frac{\cos (\pi z)}{\sin (\pi z)}, k\right)=\frac{\cos (k \pi)}{\left.\frac{d}{d z} \sin (\pi z)\right|_{z=k}}=\frac{1}{\pi}
@@ -390,7 +429,9 @@
 > 
 > (b) Compute $\operatorname{Res}\left(e^{-\frac{1}{z^{2}}} \cos \frac{1}{z}, 0\right)$.
 
-**solution** (a) We proved in Proposition 2, Section 4.4, that if $f(z)$ is even and analytic at 0 , then the Taylor coefficients corresponding to the odd powers of $z$ are zero. The same **proof** applies to Laurent series around 0 and shows that $f$ is even if and only if $a_{2 n+1}$ and $a_{-2 n+1}$ are zero for all integers $n$. In particular, if $f$ is even then $a_{-1}=0$, and so $\operatorname{Res}(f, 0)=0$.
+##### solution
+
+(a) We proved in Proposition 2, Section 4.4, that if $f(z)$ is even and analytic at 0 , then the Taylor coefficients corresponding to the odd powers of $z$ are zero. The same **proof** applies to Laurent series around 0 and shows that $f$ is even if and only if $a_{2 n+1}$ and $a_{-2 n+1}$ are zero for all integers $n$. In particular, if $f$ is even then $a_{-1}=0$, and so $\operatorname{Res}(f, 0)=0$.
 (b) The function $e^{-\frac{1}{z^{2}}} \cos \frac{1}{z}$ is even and has an essential singularity at 0 . By (a), its residue at 0 is 0 . $\square$
 
 
@@ -406,7 +447,9 @@
 
 
 
-**solution** From the Laurent series
+##### solution
+
+From the Laurent series
 
 $$
 \sin \frac{1}{z}=\frac{1}{z}-\frac{1}{3!} \frac{1}{z^{3}}+\frac{1}{5!} \frac{1}{z^{5}}-\cdots,
@@ -431,7 +474,9 @@
 > Find the residue of $\frac{e^{\frac{1}{2}}}{z^{2}+1}$ at $z=0$.
 
 
-**solution** The given function has an essential singularity at $z=0$. To compute the coefficient $a_{-1}$ in its Laurent series around 0 , we use two familiar Taylor and Laurent series as follows. We have, for $0<|z|<1$,
+##### solution
+
+The given function has an essential singularity at $z=0$. To compute the coefficient $a_{-1}$ in its Laurent series around 0 , we use two familiar Taylor and Laurent series as follows. We have, for $0<|z|<1$,
 
 $$
 \frac{e^{\frac{1}{t}}}{z^{2}+1}=\frac{1}{z^{2}+1} e^{\frac{1}{z}}=\left(1-z^{2}+z^{4}-\cdots\right)\left(1+\frac{1}{z}+\frac{1}{2!} \frac{1}{z^{2}}+\frac{1}{3!} \frac{1}{z^{3}}+\cdots\right)
@@ -466,10 +511,18 @@
 In problems 13-26, evaluate the given path integral. The path $R$ in problems 15 and 20 is shown in _Figure 5_.
 
 
-> [!figure] Figure 5
-> 
-> ![300](./images/b1ad9866-c636-4d3b-85cb-e1f2bdb2e560-08_486_536_1349_108.jpg)
-> Figure 5 The path $R$ for problems 15 and 20.
+```scientific-figure
+id: 56a44dd1-1702-47ac-b428-a9671f6e4401
+numbered: false
+title: ""
+caption: "**Figure 5.** The path $R$ for problems 15 and 20."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 05 Residue Theory/images/b1ad9866-c636-4d3b-85cb-e1f2bdb2e560-08_486_536_1349_108.jpg
+    caption: ""
+```
 
 
 

`````

## Additional source comparison

## 1. Repair Markdown display boundary: place closing display delimiter on its own line and end-of-proof square in following paragraph. No mathematical content or author wording changed.

### Before

````text
$$ $\square$
````
### After

````text
$$

$\square$
````

## Additional source comparison

## 1. Correct OCR in chapter-opening margin text against the first page of the preserved chapter PDF.

### Before

````text
guimat series and Laurent corefferents from Section 4.5 are and to define residues in Secsin 31.
````
### After

````text
Laurent series and Laurent coefficients from Section 4.5 are used to define residues in Section 5.1.
````

## 2. Correct OCR in chapter-opening margin text against the first page of the preserved chapter PDF.

### Before

````text
Cauchy's theorem for gudiply connected regions (Theoem 6. Section 3.4) is the basis ha mast integrals
````
### After

````text
Cauchy's theorem for multiply connected regions (Theorem 6, Section 3.4) is the basis for most integrals
````

## 3. Correct OCR in chapter-opening margin text against the first page of the preserved chapter PDF.

### Before

````text
Theoren 2. Section 3.2. Sectim 5.6
````
### After

````text
Theorem 2, Section 3.2. Section 5.6
````

## 4. Correct OCR in chapter-opening margin text against the first page of the preserved chapter PDF.

### Before

````text
colangent, which are presmited
````
### After

````text
cotangent, which are presented
````

## 5. Correct OCR in chapter-opening margin text against the first page of the preserved chapter PDF.

### Before

````text
baric applications
````
### After

````text
basic applications
````

## 6. Correct OCR in chapter-opening margin text against the first page of the preserved chapter PDF.

### Before

````text
simplet ones
````
### After

````text
simpler ones
````

## 7. Correct OCR in chapter-opening margin text against the first page of the preserved chapter PDF.

### Before

````text
afferting
````
### After

````text
affecting
````

## 8. Correct OCR in chapter-opening margin text against the first page of the preserved chapter PDF.

### Before

````text
conLains
````
### After

````text
contains
````

## 9. Correct OCR in chapter-opening margin text against the first page of the preserved chapter PDF.

### Before

````text
at sunc stage
````
### After

````text
at some stage
````

## 10. Correct OCR in chapter-opening margin text against the first page of the preserved chapter PDF.

### Before

````text
this sertion
````
### After

````text
this section
````

## 11. Correct OCR in chapter-opening margin text against the first page of the preserved chapter PDF.

### Before

````text
a cource
````
### After

````text
a course
````

## 12. Correct OCR in chapter-opening margin text against the first page of the preserved chapter PDF.

### Before

````text
mathematical profis
````
### After

````text
mathematical proofs
````

## 13. Correct OCR in chapter-opening margin text against the first page of the preserved chapter PDF.

### Before

````text
that sartion
````
### After

````text
that section
````
