
# Editorial records

Reading note: 13.6 Legendre Polynomials and Legendre Series Expansions.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!identity|fb2e5281-924b-5151-a932-01eef37eb124.local at=b9818235-2688-508c-bd89-af0c22d81da8] Rodrigues’ formula for Legendre polynomials
> For every nonnegative integer $n$, the Legendre polynomial normalized by $P_n(1)=1$ satisfies
> $$
> P_n(x)=\frac1{2^n n!}\frac{d^n}{dx^n}(x^2-1)^n.
> $$
````
### After

````text
> [!identity|fb2e5281-924b-5151-a932-01eef37eb124.local at=b9818235-2688-508c-bd89-af0c22d81da8] Rodrigues' Formula
> For $n=0,1,2, \ldots$, we have
>
> $$
> P_{n}(x)=\frac{1}{2^{n} n!} \frac{d^{n}}{d x^{n}}\left(x^{2}-1\right)^{n}
> $$
>
> Here $P_n$ is the Legendre polynomial normalized by $P_n(1)=1$.
````

## 2. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!identity|3812d1e6-7ecb-530a-a502-6d0f0a70d31f.local at=dbe9fd0e-5c32-5aa3-a0b2-b81c57582e0a] Bonnet’s three-term recurrence for Legendre polynomials
> For integers $n\ge1$, the Legendre polynomials normalized by $P_k(1)=1$ satisfy
> $$
> (n+1)P_{n+1}(x)+nP_{n-1}(x)=(2n+1)xP_n(x).
> $$
````
### After

````text
> [!identity|3812d1e6-7ecb-530a-a502-6d0f0a70d31f.local at=dbe9fd0e-5c32-5aa3-a0b2-b81c57582e0a] Bonnet's Recurrence Relation
> For $n=1,2, \ldots$ we have
>
> $$
> (n+1) P_{n+1}(x)+n P_{n-1}(x)=(2 n+1) x P_{n}(x)
> $$
>
> Here $P_n$ is the Legendre polynomial normalized by $P_n(1)=1$.
````

## 3. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|f402a21f-6687-5549-88bf-1527db76b6fc.local at=50b109e5-0896-5f49-b976-0d98ef1a9fe0] Orthogonality and squared norms of Legendre polynomials
> For nonnegative integers $m,n$, let $P_m,P_n$ be the Legendre polynomials normalized by $P_k(1)=1$. Then
> $$
> \int_{-1}^1P_m(x)P_n(x)\,dx=
> \begin{cases}0,&m\ne n,\\[2pt]\dfrac2{2n+1},&m=n.\end{cases}
> $$
````
### After

````text
> [!theorem|f402a21f-6687-5549-88bf-1527db76b6fc.local at=50b109e5-0896-5f49-b976-0d98ef1a9fe0] Orthogonality of Legendre Polynomials
> Let $P_n$ denote the Legendre polynomial normalized by $P_n(1)=1$, for nonnegative integers $n$.
>
> (i) If $m \neq n$, then
>
> $$
> \int_{-1}^{1} P_{m}(x) P_{n}(x) d x=0
> $$
>
> (ii) For each $n$, we have
>
> $$
> \int_{-1}^{1} P_{n}^{2}(x) d x=\frac{2}{2 n+1}
> $$
````

## 4. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|5a845fe2-5dc9-55dd-b849-8dd528c0aef7.local at=0ce2435d-4e30-5b6a-9f67-51d5d3ec6ed2] Pointwise convergence and coefficients of a Legendre series
> Let $f$ be piecewise smooth on $[-1,1]$, with finitely many continuously differentiable pieces and finite one-sided limits of $f$ and $f'$ at their endpoints. For the Legendre polynomials $P_j$ normalized by $P_j(1)=1$, set
> $$
> A_j=\frac{2j+1}{2}\int_{-1}^1f(t)P_j(t)\,dt.
> $$
> At each $-1<x<1$,
> $$
> \sum_{j=0}^{\infty}A_jP_j(x)=\frac{f(x+)+f(x-)}2.
> $$
> At continuity points this equals $f(x)$. This statement makes no endpoint-convergence assertion.
````
### After

````text
> [!theorem|5a845fe2-5dc9-55dd-b849-8dd528c0aef7.local at=0ce2435d-4e30-5b6a-9f67-51d5d3ec6ed2] Legendre Series
> Suppose that $f$ is a piecewise smooth function on the interval $-1 \leq x \leq 1$. Then $f$ has the Legendre series expansion
>
> $$
> f(x)=\sum_{j=0}^{\infty} A_{j} P_{j}(x)
> $$
>
> where
>
> $$
> A_{j}=\frac{2 j+1}{2} \int_{-1}^{1} f(x) P_{j}(x) d x
> $$
>
> For $x$ in the (open) interval ( $-1,1$ ), the Legendre series converges to $f(x)$ if $f$ is continuous at $x$, and to $(f(x+)+f(x-)) / 2$ otherwise.
>
> Here $P_n$ is the Legendre polynomial normalized by $P_n(1)=1$.
````

## 5. Restore source wording; retain only the actual correction.

### Before

````text
The nonnegativity is the Fejér inequality. [Corrected: the printed upper bound $1/(1-x)$ fails already when $n=0$ and $x<0$. The valid upper bound $2/(1-x)$ suffices for the following convergence tests.] For the upper bound, use Laplace’s integral formula and the finite geometric sum: with $z=x+i\sqrt{1-x^2}\cos\theta$, one has $|z|\le1$ and $|1-z|\ge1-x$, so $|\sum_{k=0}^n z^k|\le2/(1-x)$.
````
### After

````text
The nonnegativity is the Fejér inequality.
````

## 6. Move editorial commentary to this record.

### Before

````text
*Editorial reference repair: the original hints cite source §§2.7–2.8, which are not present in this vault’s Fourier-series chapter. The relevant convergence arguments are named locally instead.*
````
### After

````text

````

## Source-to-current comparison

Source: /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 13 Partial Differential Equations in Spherical Coordinates/13.6 Legendre Polynomials and Legendre Series Expansions.md

This exact comparison preserves the full change evidence, including formatting, OCR corrections, restored source wording, and required standalone context. The entries above explain the recovery edits. The comparison is not a claim that every difference is a correction; component serialization, callout wrapping, and printed labels outside callouts are formatting.

`````diff
--- /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 13 Partial Differential Equations in Spherical Coordinates/13.6 Legendre Polynomials and Legendre Series Expansions.md
+++ /Users/gradyclopton/ObsidianVaults/complex_analysis/Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 13 Partial Differential Equations in Spherical Coordinates/13.6 Legendre Polynomials and Legendre Series Expansions.md
@@ -1,14 +1,18 @@
+
 ### 13.6 Legendre Polynomials and Legendre Series Expansions
 
 Our goal in this section is to establish the orthogonality of the Legendre polynomials, and show how they can be used to expand functions in series in terms of Legendre polynomials. We start with a useful formula.
 
-## RODRIGUES' FORMULA
-
-For $n=0,1,2, \ldots$, we have
-
-$$
-P_{n}(x)=\frac{1}{2^{n} n!} \frac{d^{n}}{d x^{n}}\left(x^{2}-1\right)^{n}
-$$
+> [!identity|fb2e5281-924b-5151-a932-01eef37eb124.local at=b9818235-2688-508c-bd89-af0c22d81da8] Rodrigues' Formula
+> For $n=0,1,2, \ldots$, we have
+>
+> $$
+> P_{n}(x)=\frac{1}{2^{n} n!} \frac{d^{n}}{d x^{n}}\left(x^{2}-1\right)^{n}
+> $$
+>
+> Here $P_n$ is the Legendre polynomial normalized by $P_n(1)=1$.
+
+*Printed equation label: (1).*
 
 This concise formula could be used as the definition of the Legendre polynomials. It is apparent from this formula that the Legendre polynomials are polynomials of degree $n$. Formulas of this type will be used in defining other useful functions (see Section 13.7).
 
@@ -16,6 +20,7 @@
 
 $$
 P_{n}(x)=\frac{1}{2^{n}} \sum_{m=0}^{M}(-1)^{m} \frac{(2 n-2 m)!}{m!(n-m)!(n-2 m)!} x^{n-2 m}
+\tag{2}
 $$
 
 where $M=n / 2$ if $n$ is even or $(n-1) / 2$ if $n$ is odd. For each $0 \leq m \leq M$, we have
@@ -30,50 +35,57 @@
 \frac{d^{n}}{d x^{n}} x^{2 n-2 m}=0
 $$
 
+So we can write (2) as
+
+$$
+P_{n}(x)=\frac{1}{2^{n} n!} \sum_{m=0}^{n}(-1)^{m} \frac{n!}{m!(n-m)!} \frac{d^{n}}{d x^{n}} x^{2 n-2 m}
+$$
+
+and because differentiation is a linear operation, we get
+
+$$
+P_{n}(x)=\frac{1}{2^{n} n!} \frac{d^{n}}{d x^{n}} \sum_{m=0}^{n}(-1)^{m} \frac{n!}{m!(n-m)!}\left(x^{2}\right)^{n-m}=\frac{1}{2^{n} n!} \frac{d^{n}}{d x^{n}}\left(x^{2}-1\right)^{n}
+$$
+
+where the last equality follows from the binomial formula.
+
 Binomial formula:
 
 $$
-=\sum_{m=0}^{n} \frac{n!}{m!(n-m)!} a^{n-m} b^{m} .
-$$
-
-## BONNET'S RECURRENCE RELATION
-
-So we can write (2) as
-
-$$
-P_{n}(x)=\frac{1}{2^{n} n!} \sum_{m=0}^{n}(-1)^{m} \frac{n!}{m!(n-m)!} \frac{d^{n}}{d x^{n}} x^{2 n-2 m}
-$$
-
-and because differentiation is a linear operation, we get
-
-$$
-P_{n}(x)=\frac{1}{2^{n} n!} \frac{d^{n}}{d x^{n}} \sum_{m=0}^{n}(-1)^{m} \frac{n!}{m!(n-m)!}\left(x^{2}\right)^{n-m}=\frac{1}{2^{n} n!} \frac{d^{n}}{d x^{n}}\left(x^{2}-1\right)^{n}
-$$
-
-where the last equality follows from the binomial formula.
+(a+b)^n=\sum_{m=0}^{n} \frac{n!}{m!(n-m)!} a^{n-m} b^{m} .
+$$
+
+
 A judicious use of Rodrigues' formula yields the following important identity which relates different Legendre polynomials.
 
-## For $n=1,2, \ldots$ we have
-
-$$
-(n+1) P_{n+1}(x)+n P_{n-1}(x)=(2 n+1) x P_{n}(x)
-$$
+> [!identity|3812d1e6-7ecb-530a-a502-6d0f0a70d31f.local at=dbe9fd0e-5c32-5aa3-a0b2-b81c57582e0a] Bonnet's Recurrence Relation
+> For $n=1,2, \ldots$ we have
+>
+> $$
+> (n+1) P_{n+1}(x)+n P_{n-1}(x)=(2 n+1) x P_{n}(x)
+> $$
+>
+> Here $P_n$ is the Legendre polynomial normalized by $P_n(1)=1$.
+
+*Printed equation label: (3).*
 
 Bonnet's relation has several applications. For example, we can use it to generate as many Legendre polynomials as we wish by just knowing $P_{0}$ and $P_{1}$. (See Exercise 1.) The following related formula is also useful:
 
 $$
 P_{n+1}^{\prime}(x)=P_{n-1}^{\prime}(x)+(2 n+1) P_{n}(x)
+\tag{4}
 $$
 
 The proofs of (3) and (4) are presented in the appendix to this section.
 
-## EXAMPLE 1 An application of Bonnet's relation
-
-Show that for all $n=0,1,2, \ldots$, we have
-(a) $P_{n}(1)=1$;
-(b) $P_{n}(-1)=(-1)^{n}$.
-
-Solution (a) We use a two-step induction. Recall that $P_{0}(x)=1$ and $P_{1}(x)=x$, and so the assertion is clear for $n=0$ and $n=1$. Now assume that the assertion is true for $(n-1)$ and $n$; that is, assume that $P_{n-1}(1)=1$ and $P_{n}(1)=1$. Then, Bonnet's recurrence relation gives
+> [!exercise|5f722d8b-51f5-5375-8922-a0333062dbe3.local at=3db4bfc5-a20f-5258-9d1f-805100a29830] EXAMPLE 1 An application of Bonnet's relation
+> Show that for all $n=0,1,2, \ldots$, we have
+> (a) $P_{n}(1)=1$;
+> (b) $P_{n}(-1)=(-1)^{n}$.
+
+##### solution
+
+(a) We use a two-step induction. Recall that $P_{0}(x)=1$ and $P_{1}(x)=x$, and so the assertion is clear for $n=0$ and $n=1$. Now assume that the assertion is true for $(n-1)$ and $n$; that is, assume that $P_{n-1}(1)=1$ and $P_{n}(1)=1$. Then, Bonnet's recurrence relation gives
 
 $$
 (n+1) P_{n+1}(1)+n P_{n-1}(1)=(2 n+1) P_{n}(1)
@@ -83,22 +95,23 @@
 
 To prove (b), we recall that $P_{n}(x)$ is an even function when $n$ is even, and odd when $n$ is odd. Thus $P_{n}(-1)=P_{n}(1)=1$ if $n$ is even, $P_{n}(-1)=-P_{n}(1)=-1$ if $n$ is odd. Equivalently, $P_{n}(-1)=(-1)^{n}$.
 
-THEOREM 1 ORTHOGONALITY OF LEGENDRE POLYNOMIALS
-
 ## Orthogonality of Legendre Polynomials
 
-We can now establish the orthogonality of the Legendre polynomials. As with Bessel functions, this property is a consequence of a general theory of Sturm and Liouville (Chapter 6). We present here an independent account to illustrate further the general theory.
-(i) If $m \neq n$, then
-
-$$
-\int_{-1}^{1} P_{m}(x) P_{n}(x) d x=0
-$$
-
-(ii) For each $n$, we have
-
-$$
-\int_{-1}^{1} P_{n}^{2}(x) d x=\frac{2}{2 n+1}
-$$
+We can now establish the orthogonality of the Legendre polynomials. As with Bessel functions, this property is a consequence of a general theory of Sturm and Liouville (Chapter 14). We present here an independent account to illustrate further the general theory.
+> [!theorem|f402a21f-6687-5549-88bf-1527db76b6fc.local at=50b109e5-0896-5f49-b976-0d98ef1a9fe0] Orthogonality of Legendre Polynomials
+> Let $P_n$ denote the Legendre polynomial normalized by $P_n(1)=1$, for nonnegative integers $n$.
+>
+> (i) If $m \neq n$, then
+>
+> $$
+> \int_{-1}^{1} P_{m}(x) P_{n}(x) d x=0
+> $$
+>
+> (ii) For each $n$, we have
+>
+> $$
+> \int_{-1}^{1} P_{n}^{2}(x) d x=\frac{2}{2 n+1}
+> $$
 
 In particular, taking $m=0$ in (i), we obtain
 
@@ -113,7 +126,6 @@
 $$
 
 and rewrite it as
-You should compare this proof with that of the orthogonality of Bessel functions and note the use of the special form of the differential equations in both cases.
 
 $$
 \left[\left(1-x^{2}\right) y^{\prime}\right]^{\prime}=-\lambda(\lambda+1) y
@@ -142,11 +154,13 @@
 $$
 \begin{aligned}
 & \left(\lambda_{m}-\lambda_{n}\right) \int_{-1}^{1} P_{m}(x) P_{n}(x) d x \\
-& \quad=\left[\left.\left(1-x^{2}\left(P_{m}(x) P_{n}^{\prime}(x)-P_{m}^{\prime}(x) P_{n}(x)\right)\right]\right|_{x=-1} ^{x=1}=0\right.
+&\quad=\left[(1-x^2)\bigl(P_m(x)P_n^{\prime}(x)-P_m^{\prime}(x)P_n(x)\bigr)\right]_{x=-1}^{x=1}=0
 \end{aligned}
 $$
 
 and since $\lambda_{m} \neq \lambda_{n}$, (i) follows.
+You should compare this proof with that of the orthogonality of Bessel functions and note the use of the special form of the differential equations in both cases.
+
 (ii) Bonnet's recurrence relations for $n$ and $n-1$ give
 
 $$
@@ -181,6 +195,7 @@
 
 $$
 \int_{-1}^{1} P_{n}^{2}(x) d x=\frac{2 n-1}{2 n+1} \int_{-1}^{1} P_{n-1}^{2}(x) d x
+\tag{5}
 $$
 
 Now recall that $P_{0}(x)=1$, and so $\int_{-1}^{1} P_{0}^{2}(x) d x=2$. Repeated applications of (5) give
@@ -197,42 +212,56 @@
 
 $$
 f(x)=\sum_{j=0}^{\infty} A_{j} P_{j}(x)
-$$
-
-called the Legendre series expansion of $f$. The coefficient $A_{j}$ is called the $j$ th Legendre coefficient of $f$. The following theorem, which you are asked to apply in the exercises, gives sufficient conditions for a function to have a Legendre series and provides a formula for the $j$ th Legendre coefficient. Note the similarity between the hypotheses of this theorem and those for Fourier and Bessel expansions. For the definition of piecewise smooth, refer to Section 2.2.
-
-THEOREM 2
-
-## LEGENDRE SERIES
-
-![](./images/122e2a0e-ba5b-4934-9af1-dcd4ea360903-44_331_475_1625_63.jpg)
-Figure 1 Function in Example 2.
-
-Suppose that $f$ is a piecewise smooth function on the interval $-1 \leq x \leq 1$. Then $f$ has the Legendre series expansion
-
-$$
-f(x)=\sum_{j=0}^{\infty} A_{j} P_{j}(x)
-$$
-
-where
-
-$$
-A_{j}=\frac{2 j+1}{2} \int_{-1}^{1} f(x) P_{j}(x) d x
-$$
-
-For $x$ in the (open) interval ( $-1,1$ ), the Legendre series converges to $f(x)$ if $f$ is continuous at $x$, and to $(f(x+)+f(x-)) / 2$ otherwise.
-
-## EXAMPLE 2 A Legendre series
-
-(a) Find the first eight Legendre coefficients $A_{0}, A_{1}, \ldots, A_{7}$ of the function in Figure 1:
-
-$$
-f(x)= \begin{cases}0 & \text { if }-1 \leq x<0, \\ 1 & \text { if } 0 \leq x \leq 1 .\end{cases}
-$$
-
-(b) On the same coordinate axes, sketch the graphs of $f$ and the partial sums $s_{n}(x)=\sum_{j=0}^{n} A_{j} P_{j}(x)$ for $n=0,1,3,7$. Describe the behavior of the partial sums over the interval $[-1,1]$.
-
-Solution (a) We use (7) to compute the Legendre coefficients and note that $\int_{-1}^{1} f(x) P_{j}(x) d x=\int_{0}^{1} P_{j}(x) d x$. Using the list of Legendre polynomials found in
+\tag{6}
+$$
+
+called the Legendre series expansion of $f$. The coefficient $A_{j}$ is called the $j$ th Legendre coefficient of $f$. The following theorem, which you are asked to apply in the exercises, gives sufficient conditions for a function to have a Legendre series and provides a formula for the $j$ th Legendre coefficient. Note the similarity between the hypotheses of this theorem and those for Fourier and Bessel expansions. For the definition of piecewise smooth, refer to Section 7.2.
+
+> [!theorem|5a845fe2-5dc9-55dd-b849-8dd528c0aef7.local at=0ce2435d-4e30-5b6a-9f67-51d5d3ec6ed2] Legendre Series
+> Suppose that $f$ is a piecewise smooth function on the interval $-1 \leq x \leq 1$. Then $f$ has the Legendre series expansion
+>
+> $$
+> f(x)=\sum_{j=0}^{\infty} A_{j} P_{j}(x)
+> $$
+>
+> where
+>
+> $$
+> A_{j}=\frac{2 j+1}{2} \int_{-1}^{1} f(x) P_{j}(x) d x
+> $$
+>
+> For $x$ in the (open) interval ( $-1,1$ ), the Legendre series converges to $f(x)$ if $f$ is continuous at $x$, and to $(f(x+)+f(x-)) / 2$ otherwise.
+>
+> Here $P_n$ is the Legendre polynomial normalized by $P_n(1)=1$.
+
+*Printed equation label: (7).*
+
+```scientific-figure
+id: 47d5bcff-d3fc-4536-9861-afe6c8ab8994
+numbered: false
+title: ""
+caption: Figure 1 Function in Example 2.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 13 Partial Differential Equations in Spherical Coordinates/images/122e2a0e-ba5b-4934-9af1-dcd4ea360903-44_331_475_1625_63.jpg
+    caption: ""
+```
+
+
+> [!exercise|1642d7bb-e25a-5f52-ae41-c92b56f8bcfa.local at=090fcd2f-a7aa-5e16-9e5f-2df22cb3f9ab] EXAMPLE 2 A Legendre series
+> (a) Find the first eight Legendre coefficients $A_{0}, A_{1}, \ldots, A_{7}$ of the function in Figure 1:
+>
+> $$
+> f(x)= \begin{cases}0 & \text { if }-1 \leq x<0, \\ 1 & \text { if } 0 \leq x \leq 1 .\end{cases}
+> $$
+>
+> (b) On the same coordinate axes, sketch the graphs of $f$ and the partial sums $s_{n}(x)=\sum_{j=0}^{n} A_{j} P_{j}(x)$ for $n=0,1,3,7$. Describe the behavior of the partial sums over the interval $[-1,1]$.
+
+##### solution
+
+(a) We use (7) to compute the Legendre coefficients and note that $\int_{-1}^{1} f(x) P_{j}(x) d x=\int_{0}^{1} P_{j}(x) d x$. Using the list of Legendre polynomials found in
 
 Section 13.5, we get
 
@@ -268,13 +297,19 @@
 
 The graphs of $f$ together with these partial sums are shown in Figure 2. As the number of terms in a partial sum increases, the graph of the partial sum gets closer to the graph of $f$. Note that all the graphs of the partial sums have $y$ intercept $\frac{1}{2}$. This confirms the assertion of Theorem 2 concerning the limit of the Legendre series at points of discontinuity, since 0 is a point of discontinuity and $(f(0+)+f(0-)) / 2=\frac{1}{2}$.
 
-Figure 2 The partial sums of the Legendre series converge to $f(x)$ for all $0<x<1$, except at the point of discontinuity $x=0$. There, the series converges to
-
-$$
-\frac{f(0+)+f(0-)}{2}=\frac{1}{2} .
-$$
-
-![](./images/122e2a0e-ba5b-4934-9af1-dcd4ea360903-46_554_941_148_673.jpg)
+```scientific-figure
+id: 06c60e27-7653-4bdc-8c2e-7158b9c9fe34
+numbered: false
+title: ""
+caption: Figure 2 Partial sums of the Legendre series. For $-1<x<1$ they converge to $f(x)$ at continuity points and to $(f(0+)+f(0-))/2=1/2$ at the jump $x=0$.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 13 Partial Differential Equations in Spherical Coordinates/images/122e2a0e-ba5b-4934-9af1-dcd4ea360903-46_554_941_148_673.jpg
+    caption: ""
+```
+
 
 In Exercise 26 you are asked to find a closed form for the Legendre coefficients in Example 2 and to further study the behavior of the partial sums. You will see that Legendre series exhibit a Gibbs phenomenon near a point of discontinuity.
 
@@ -298,15 +333,17 @@
 D^{n+1}\left(u^{n+1}\right) & =D^{n-1} D^{2}\left(u^{n+1}\right) \\
 & =4 n(n+1) D^{n-1} u^{n-1}+2(n+1)(2 n+1) D^{n-1} u^{n}
 \end{aligned}
+\tag{8}
 $$
 
 Write Rodrigues' formula (1) as $P_{n}(x)=\frac{1}{2^{n} n!} D^{n} u^{n}$. Now (8) gives
 
 $$
 P_{n+1}(x)=\frac{1}{2^{n+1}(n+1)!} D^{n-1} D^{2}\left(u^{n+1}\right)=P_{n-1}(x)+\frac{(2 n+1)}{2^{n} n!} D^{n-1} u^{n} .
-$$
-
-## Recall the Leibniz product rule for differentiation:
+\tag{9}
+$$
+
+Recall the Leibniz product rule for differentiation:
 
 $$
 \frac{d^{n}}{d x^{n}}(f \cdot g)=\sum_{m=0}^{n} \frac{n!}{m!(n-m)!} \frac{d^{m} f}{d x^{m}} \frac{d^{n-m} g}{d x^{n-m}}
@@ -320,6 +357,7 @@
 & =\frac{1}{2^{n} n!} D^{n}\left[x u^{n}\right]=\frac{1}{2^{n} n!}\left[x D^{n} u^{n}+n D^{n-1} u^{n}\right] \\
 & =x P_{n}(x)+\frac{n}{2^{n} n!} D^{n-1} u^{n}
 \end{aligned}
+\tag{10}
 $$
 
 Now if we solve for $\frac{1}{2^{n} n!} D^{n-1} u^{n}$ in (9) and (10), equate the results, and simplify, we get Bonnet's recurrence relation (3). It remains to establish (4). To this end, differentiate both sides of (9):
@@ -336,167 +374,322 @@
 
 which is precisely what we want.
 
-## Exercises 5.6
-
-1. Use Bonnet's recurrence relation to find $P_{2}(x), P_{3}(x)$, and $P_{4}(x)$ given that $P_{0}(x)=1, P_{1}(x)=x$.
-2. Use Bonnet's recurrence relation to compute $P_{2}(0), P_{3}(0)$, and $P_{4}(0)$ given that $P_{0}(0)=1, P_{1}(0)=0$.
-
-Evaluate the following integrals using Bonnet's relation and orthogonality.
-3. $\int_{-1}^{1} x P_{7}(x) d x$.
-4. $\int_{-1}^{1} P_{2}(x) P_{7}(x) d x$.
-5. $\int_{-1}^{1} x P_{2}(x) P_{3}(x) d x$.
-6. $\int_{-1}^{1} x^{2} P_{4}(x) d x$.
-7. $\int_{-1}^{1} x^{2} P_{7}(x) d x$.
-8. $\int_{-1}^{1} x^{2} P_{6}(x) P_{7}(x) d x$.
-9. (a) Use (4) to prove that for $n=1,2, \ldots$
-
-$$
-\int_{x}^{1} P_{n}(t) d t=\frac{1}{2 n+1}\left[P_{n-1}(x)-P_{n+1}(x)\right]
-$$
-
-(b) Deduce that $\int_{-1}^{1} P_{n}(t) d t=0$ for $n=1,2, \ldots$.
-(c) Use (a) and (b) to prove that for $n=1,2, \ldots$.
-
-$$
-\int_{-1}^{x} P_{n}(t) d t=\frac{1}{2 n+1}\left[P_{n+1}(x)-P_{n-1}(x)\right]
-$$
-
-10. Use Exercise 9 to derive the following identities.
-
-$$
-\begin{gathered}
-\int_{0}^{1} P_{2 n}(t) d t=0, \quad n=1,2, \ldots \\
-\int_{0}^{1} P_{2 n+1}(t) d t=\frac{(-1)^{n}(2 n)!}{2^{2 n+1}(n!)^{2}(n+1)}, \quad n=0,1,2, \ldots
-\end{gathered}
-$$
-
-[Hint: Exercise 3, Section 13.5.]
-11. Derive the following identities. For (b) and (c), use Bonnet's relation and Exercise 10.
-(a)
-
-$$
-\int_{0}^{1} x P_{0}(x) d x=\frac{1}{2} ; \quad \int_{0}^{1} x P_{1}(x) d x=\frac{1}{3}
-$$
-
-(b)
-
-$$
-\int_{0}^{1} x P_{2 n}(x) d x=\frac{(-1)^{n+1}(2 n-2)!}{2^{2 n}((n-1)!)^{2} n(n+1)}, \quad n=1,2, \ldots
-$$
-
-$$
-\int_{0}^{1} x P_{2 n+1}(x) d x=0, \quad n=1,2, \ldots
-$$
-
-12. Use Rodrigues' formula and integration by parts to show that
-
-$$
-\int_{-1}^{1} f(x) P_{n}(x) d x=\frac{(-1)^{n}}{2^{n} n!} \int_{-1}^{1} f^{(n)}(x)\left(x^{2}-1\right)^{n} d x, \quad n=0,1,2, \ldots
-$$
-
-(As a convention, $f^{(0)}(x)=f(x)$.)
-In Exercises 13-24, evaluate the integral using Exercise 12. Take $n=0,1,2, \ldots$.
-13. $\int_{-1}^{1}\left(1-x^{2}\right) P_{13}(x) d x$.
-14. $\int_{-1}^{1} x^{4} P_{3}(x) d x$.
-15. $\int_{-1}^{1} x^{n} P_{n}(x) d x$.
-16. $\int_{-1}^{1} x^{n+1} P_{n}(x) d x$.
-[Hint: In Exercises 15 and 16, use Wallis's formulas, Section 4.7.]
-17. $\int_{-1}^{1} \ln (1-x) P_{2}(x) d x$.
-18. $\int_{-1}^{1} \ln (1+x) P_{4}(x) d x$.
-19. $\int_{-1}^{1} \ln (1-x) x P_{2}(x) d x$.
-20. $\int_{-1}^{1} \ln (1+x) x P_{2}(x) d x$.
-[Hint: In Exercises 19 and 20, use Bonnet's relation (3).]
-21. $\int_{-1}^{1} \ln (1-x) P_{n}(x) d x$.
-22. $\int_{-1}^{1} \ln (1+x) P_{n}(x) d x$.
-23. $\int_{-1}^{1} \ln (1-x) x P_{n}(x) d x$.
-24. $\int_{-1}^{1} \ln (1+x) x P_{n}(x) d x$.
-25. Use Rodrigues' formula to show that $P_{n}(1)=1, n=0,1,2, \ldots$. [Hint: Write $\left(x^{2}-1\right)^{n}=(x-1)^{n}(x+1)^{n}$, and use the Leibniz rule.]
-26. (a) Consider the function in Example 2. Derive the Legendre series expansion
-
-$$
-f(x)=\frac{1}{2}+\sum_{n=0}^{\infty}(-1)^{n}\left(\frac{4 n+3}{4 n+4}\right) \frac{(2 n)!}{2^{2 n}(n!)^{2}} P_{2 n+1}(x) .
-$$
-
-[Hint: Exercise 10.]
-(b) Plot several partial sums of the series and note that near $x=0$, a point of discontinuity of the function, the partial sums overshoot the graph of the function. Do the overshoots disappear with larger partial sums? State a property or a principle concerning the convergence of partial sums of Legendre series near points of discontinuity.
-27. Let $f(x)=|x|,-1 \leq x \leq 1$. (a) Compute the first three nonzero Legendre coefficients of $f$.
-(b) Derive the Legendre coefficients $A_{0}=\frac{1}{2}, A_{2 n+1}=0$ for all $n$, and
-
-$$
-A_{2 n}=(-1)^{n+1} \frac{n(2 n-2)!}{2^{2 n}(n!)^{2}}\left(\frac{4 n+1}{n+1}\right), \quad n=1,2, \ldots
-$$
-
-[Hint: Exercise 11.]
-(c) Plot the function and the partial sums of the Legendre series $\sum_{j=0}^{n} A_{j} P_{j}(x)$ for $n=1,2,5$, and 20 .
-(d) If $f(x)$ is to be approximated by its Legendre series to within 0.05 on the entire interval $-1 \leq x \leq 1$, how large should $n$ be?
-28. (a) Find the first eight Legendre coefficients $A_{0}, A_{1}, \ldots, A_{7}$ of the function
-
-$$
-f(x)= \begin{cases}0 & \text { if }-1 \leq x<0 \\ x & \text { if } 0 \leq x \leq 1\end{cases}
-$$
-
-(b) Illustrate Theorem 2 by plotting on the same coordinate axes the graphs of $f$ and the partial sums
-
-$$
-\sum_{j=0}^{3} A_{j} P_{j}(x), \quad \sum_{j=0}^{5} A_{j} P_{j}(x), \quad \sum_{j=0}^{7} A_{j} P_{j}(x) .
-$$
-
-29. Derive the Legendre series of the function in Exercise 28. [Hint: Consider the function $\frac{1}{2}\left(|x|+P_{1}(x)\right)$ and use Exercise 27.]
-30. (a) Obtain the Legendre series expansion
-
-$$
-\ln (1-x)=\ln 2-1-\sum_{n=1}^{\infty} \frac{2 n+1}{n(n+1)} P_{n}(x), \quad-1<x<1
-$$
-
-[Hint: Exercise 21.]
-(b) Plot several partial sums to illustrate the convergence of the Legendre series.
-(Note that the function does not satisfy the hypothesis of Theorem 2, because of its behavior at the endpoint $x=1$, yet the Legendre series does converge. You can establish the convergence of this Legendre series using a different test; see Exercise 39 below.)
-31. (a) Make a suitable change of variables in the series expansion of Exercise 30 to derive the Legendre series of $f(x)=\ln (1+x), \quad-1<x<1$.
-(b) Plot several partial sums to illustrate the convergence of the Legendre series.
-32. Expand the Legendre function of the second kind $Q_{0}(x)$ in a Legendre series. The explicit formula for $Q_{0}$ is given in Exercise 23, Section 13.5. [Hint: Exercises 30 and 31.]
-(b) Plot several partial sums to illustrate the convergence of the Legendre series.
-
-In Exercises 33 and 34, (a) compute at least eight terms of the Legendre series expansion of the given function. (b) On the same graph, plot the function and several partial sums to illustrate the convergence of the Legendre series. (c) If the function is to be approximated by its Legendre series to within .1 on the entire interval $-1<x<1$, how many terms of the series should you take?
-33. $f(x)=\cos \frac{\pi}{2} x,-1<x<1$.
-34. $f(x)=\sin x,-1<x<1$.
-
-Project Problem: Dirichlet test for Legendre series. Do Exercises 35-37, and either 38 or 39.
-35. Plot several partial sums $\sum_{k=0}^{n} P_{k}(x)$ and the function $1 /(1-x)$ over the
-interval $[-1,1]$. This should illustrate the inequality
-
-$$
-0 \leq \sum_{k=0}^{n} P_{k}(x) \leq \frac{1}{1-x}, \quad-1<x<1 .
-$$
-
-This nontrivial inequality is due to the Hungarian mathematician Leopoldo Fejér.
-36. Test for uniform convergence of Legendre series with decreasing coefficients. Prove the following test. Suppose that $\left(A_{k}\right)_{k=0}^{\infty}$ is a sequence of positive numbers decreasing to zero. Let $E$ be any closed interval contained in $(-1,1)$. Then the series $\sum_{k=0}^{\infty} A_{k} P_{k}(x)$ is uniformly convergent on $E$. [Hint: Use Exercise 35 of this section, and Theorem 1, Section 2.8.]
-37. Test for pointwise convergence of Legendre series with decreasing coefficients. Prove the following test. Suppose that $\left(A_{k}\right)_{k=0}^{\infty}$ is a sequence of positive numbers decreasing to zero. Then the series $\sum_{k=0}^{\infty} A_{k} P_{k}(x)$ converges pointwise for all $x$ in $(-1,1)$. [Hint: Use Exercise 36 and proceed as in the proof of part (b) of Theorem 2, Section 2.8.]
-38. Determine the values of $x$ from the interval $[-1,1]$ for which the series is convergent. Justify your answer, and be sure to check the endpoints.
-(a) $\quad \sum_{k=0}^{\infty} \frac{P_{k}(x)}{\sqrt{k+1}}$.
-(b) $\quad \sum_{k=1}^{\infty} \frac{P_{k}(x)}{k}$.
-39. Discuss the uniform convergence and pointwise convergence of the Legendre series in Exercise 30, based on the tests for convergence in Exercises 36 and 37. Be sure to discuss the behavior of the series at the endpoints.
-40. (a) Find the Legendre series of the function $f(x)=x \ln (1-x),-1<x<1$. [Hint: Exercise 23.]
-(b) Find the Legendre series of the function $f(x)=x \ln (1+x),-1<x<1$. [Hint: Change variables in (a).]
-41. Find the Legendre series of the Legendre function of the second kind $Q_{1}(x)$. For the explicit formula of $Q_{1}(x)$ see Exercise 24, Section 13.5. [Hint: Exercise 40.]
-42. Orthogonality of $\boldsymbol{P}_{\boldsymbol{n}}^{\prime}(\boldsymbol{x})$. (a) Verify that for $m=0,1,2, \ldots$ we have
-
-$$
-\left[\left(1-x^{2}\right) P_{m}^{\prime}(x)\right]^{\prime}=-m(m+1) P_{m}(x) .
-$$
-
-[Hint: Use the differential equation for $P_{m}(x)$.]
-(b) Show that if $m$ and $n$ are positive integers with $m \neq n$, then
-
-$$
-\int_{-1}^{1} P_{n}^{\prime}(x) P_{m}^{\prime}(x)\left(1-x^{2}\right) d x=0
-$$
-
-This states that the functions $P_{n}^{\prime}(x)(n=1,2, \ldots)$ are orthogonal on the interval $-1 \leq x \leq 1$ with respect to the weight function ( $1-x^{2}$ ). This result is a special case of Theorem 1, Section 13.7. [Hint: Integrate by parts and use (a).]
-43. The $j$ th Legendre coefficient. In this exercise we justify (7). Multiply both sides of (6) by $P_{j}(x)$ and then integrate from -1 to 1 . Assume that term-by-term integration is allowed and derive (7) using Theorem 1.
-44. Legendre series of polynomials. (a) Use Exercise 12 to show that if $p(x)$ is a polynomial of degree $n$, then $\int_{-1}^{1} p(x) P_{m}(x) d x=0$ for all $m>n$.
-(b) Conclude that if $p(x)$ is a polynomial of degree $n$, then the Legendre series of $p(x)$ has only finitely many terms.
-In Exercises 45-48, find the Legendre series of the given polynomial. [Hint: Write the polynomial as a linear combination of the Legendre polynomials, and then determine the coefficients.]
-45. $p(x)=x^{2}+2 x+1$.
-46. $p(x)=63 x^{5}-7 x^{3}+15 x$.
-47. $p(x)=x^{4}+2 x^{3}+x^{2}+x$.
-48. $p(x)=x^{6}$.
+## Exercises 13.6
+
+
+> [!exercise|1472fdfa-7cdf-5f14-970f-4f648333e1db.local at=53217baf-9de1-5c8b-9c86-30e364be7bb7] Exercise 1
+> Use Bonnet's recurrence relation to find $P_{2}(x), P_{3}(x)$, and $P_{4}(x)$ given that $P_{0}(x)=1, P_{1}(x)=x$.
+
+
+> [!exercise|9716bec5-5533-5cbb-a497-11c02285b098.local at=212278c7-03a1-5241-8a63-63ac42a10afd] Exercise 2
+> Use Bonnet's recurrence relation to compute $P_{2}(0), P_{3}(0)$, and $P_{4}(0)$ given that $P_{0}(0)=1, P_{1}(0)=0$.
+
+
+> [!prompt|61bd9e71-ca3f-5e15-99d3-95f4b2eff23b.local at=5870e61a-b484-53e1-bf4b-9f8e761330af] Shared exercise instructions
+> Evaluate the following integrals using Bonnet's relation and orthogonality.
+
+
+> [!exercise|4fa7b4ff-9af1-5e2e-8103-72e087d5d429.local at=60e28408-46fe-534c-9594-620b26c68c4f] Exercise 3
+> $\int_{-1}^{1} x P_{7}(x) d x$.
+
+
+> [!exercise|f36fe8a2-d33c-5410-a989-e6e50c8b85ab.local at=252bb359-67d6-50ea-80bb-cabd27a96542] Exercise 4
+> $\int_{-1}^{1} P_{2}(x) P_{7}(x) d x$.
+
+
+> [!exercise|b25123e7-5396-56ea-a2ec-b8041e03e876.local at=bad56627-0720-5c67-99b5-cca65345d901] Exercise 5
+> $\int_{-1}^{1} x P_{2}(x) P_{3}(x) d x$.
+
+
+> [!exercise|8f868ac1-486e-52b3-84e7-e9116cfdfc9b.local at=1c3c85b7-cbec-54c2-9900-b83767e0088f] Exercise 6
+> $\int_{-1}^{1} x^{2} P_{4}(x) d x$.
+
+
+> [!exercise|617d2efa-a523-5cba-a395-d3c0e85ba137.local at=83351e8d-985e-5720-a26a-b6fa93758f5d] Exercise 7
+> $\int_{-1}^{1} x^{2} P_{7}(x) d x$.
+
+
+> [!exercise|ec9bc5a0-586c-59c0-a323-aedc4cc92f48.local at=55931bf5-0c0a-5473-b2c0-946f29f60492] Exercise 8
+> $\int_{-1}^{1} x^{2} P_{6}(x) P_{7}(x) d x$.
+
+
+> [!exercise|46e9138a-144d-5a0e-ae3d-c3779250ca02.local at=c6841f6d-001b-5d4f-8480-894d360f45cd] Exercise 9
+> (a) Use (4) to prove that for $n=1,2, \ldots$
+>
+> $$
+> \int_{x}^{1} P_{n}(t) d t=\frac{1}{2 n+1}\left[P_{n-1}(x)-P_{n+1}(x)\right]
+> $$
+>
+> (b) Deduce that $\int_{-1}^{1} P_{n}(t) d t=0$ for $n=1,2, \ldots$.
+> (c) Use (a) and (b) to prove that for $n=1,2, \ldots$.
+>
+> $$
+> \int_{-1}^{x} P_{n}(t) d t=\frac{1}{2 n+1}\left[P_{n+1}(x)-P_{n-1}(x)\right]
+> $$
+
+
+> [!exercise|ada8070a-dc10-5bd3-8d20-9c7011ac51a3.local at=f87fb38a-ef57-5284-b0ad-8545081be4b1] Exercise 10
+> Use Exercise 9 to derive the following identities.
+>
+> $$
+> \begin{gathered}
+> \int_{0}^{1} P_{2 n}(t) d t=0, \quad n=1,2, \ldots \\
+> \int_{0}^{1} P_{2 n+1}(t) d t=\frac{(-1)^{n}(2 n)!}{2^{2 n+1}(n!)^{2}(n+1)}, \quad n=0,1,2, \ldots
+> \end{gathered}
+> $$
+>
+> [Hint: Exercise 3, Section 13.5.]
+
+
+> [!exercise|5afebcc6-2041-54f8-ae6d-4f616bcb83f0.local at=e8b085a7-f607-5fa7-ae11-7f1a034e430d] Exercise 11
+> Derive the following identities. For (b) and (c), use Bonnet's relation and Exercise 10.
+> (a)
+>
+> $$
+> \int_{0}^{1} x P_{0}(x) d x=\frac{1}{2} ; \quad \int_{0}^{1} x P_{1}(x) d x=\frac{1}{3}
+> $$
+>
+> (b)
+>
+> $$
+> \int_{0}^{1} x P_{2 n}(x) d x=\frac{(-1)^{n+1}(2 n-2)!}{2^{2 n}((n-1)!)^{2} n(n+1)}, \quad n=1,2, \ldots
+> $$
+>
+> (c)
+>
+> $$
+> \int_{0}^{1} x P_{2 n+1}(x) d x=0, \quad n=1,2, \ldots
+> $$
+
+
+> [!exercise|6763946e-5349-5210-be68-5da71b9317cb.local at=93fab341-8cdf-52c9-bd9e-42bb853a35e9] Exercise 12
+> For $f\in C^n([-1,1])$, use Rodrigues' formula and integration by parts to show that
+>
+> $$
+> \int_{-1}^{1} f(x) P_{n}(x) d x=\frac{(-1)^{n}}{2^{n} n!} \int_{-1}^{1} f^{(n)}(x)\left(x^{2}-1\right)^{n} d x, \quad n=0,1,2, \ldots
+> $$
+>
+> (As a convention, $f^{(0)}(x)=f(x)$.)
+
+
+> [!prompt|12ef23a8-0842-550f-b619-3e2b3a5c166c.local at=338595d3-5a1c-5025-a2f5-9252b3bbce16] Shared exercise instructions
+> In Exercises 13-24, evaluate the integral using Exercise 12. Take $n=0,1,2,\ldots$. For logarithmic endpoint singularities, interpret the integrals as improper and justify the endpoint limits in integration by parts.
+
+
+> [!exercise|3e38882a-9fea-55d4-87db-1cd2d1179ae9.local at=1bd0a0ca-b9c0-5b5b-9b7a-151bf84b1305] Exercise 13
+> $\int_{-1}^{1}\left(1-x^{2}\right) P_{13}(x) d x$.
+
+
+> [!exercise|eb3bfe60-52bc-590f-ab6f-995ae75a9624.local at=9b753213-0a01-5faf-99f5-0566f68c74bf] Exercise 14
+> $\int_{-1}^{1} x^{4} P_{3}(x) d x$.
+
+
+> [!exercise|ec371b33-8279-55f1-9f4d-63f1bf96e126.local at=5b85d166-2bc7-5dbc-a76a-d4f3e0b1a293] Exercise 15
+> $\int_{-1}^{1} x^{n} P_{n}(x) d x$.
+
+
+> [!exercise|be63ce7f-5b7b-54c3-ba20-7292aa4af571.local at=95dae3e0-fc11-5997-add7-a7cf80bea2cd] Exercise 16
+> $\int_{-1}^{1} x^{n+1} P_{n}(x) d x$.
+> [Hint: In Exercises 15 and 16, use Wallis's formulas, Section 12.7.]
+
+
+> [!exercise|02b4ccb5-16c1-5072-a0d2-f25fdb8588a6.local at=cc1f474b-0a27-5fd6-8473-37dd619117e2] Exercise 17
+> $\int_{-1}^{1} \ln (1-x) P_{2}(x) d x$.
+
+
+> [!exercise|e9b34071-cb58-5a43-b422-de7102adc2c0.local at=be270b58-1df2-5188-9ae9-2c0ecbf2e93e] Exercise 18
+> $\int_{-1}^{1} \ln (1+x) P_{4}(x) d x$.
+
+
+> [!exercise|9a6f1d10-b2b7-5274-a02c-95f35c781998.local at=f3c6352f-788e-51aa-85e8-a05937babd0b] Exercise 19
+> $\int_{-1}^{1} \ln (1-x) x P_{2}(x) d x$.
+
+
+> [!exercise|89b86bf5-602f-575e-9a61-05ab5643f317.local at=2e610747-bc82-56a0-9593-20d169c7f17d] Exercise 20
+> $\int_{-1}^{1} \ln (1+x) x P_{2}(x) d x$.
+> [Hint: In Exercises 19 and 20, use Bonnet's relation (3).]
+
+
+> [!exercise|55e1fe22-ce08-5fee-b132-98c716cdce93.local at=eb177a14-b027-5bb6-9f94-d8f1cec7942c] Exercise 21
+> $\int_{-1}^{1} \ln (1-x) P_{n}(x) d x$.
+
+
+> [!exercise|584f2bc5-9e2a-5cea-bccb-edadc6500014.local at=2d51aafd-8b04-580b-9e26-2ffd6989cbbe] Exercise 22
+> $\int_{-1}^{1} \ln (1+x) P_{n}(x) d x$.
+
+
+> [!exercise|31d2d57c-313a-5aa1-a272-dbf19c5c53dc.local at=07cb609b-4a19-5f45-8f08-5e1b2932fa20] Exercise 23
+> $\int_{-1}^{1} \ln (1-x) x P_{n}(x) d x$.
+
+
+> [!exercise|756c101c-aeb3-5170-ab04-538ee39e9733.local at=70a16a1a-41c7-58d9-9623-d74c67496b21] Exercise 24
+> $\int_{-1}^{1} \ln (1+x) x P_{n}(x) d x$.
+
+
+> [!exercise|0e643123-0b0f-562c-84d2-722d5510ebbd.local at=dbc80396-b173-5293-919b-3e08c3cc1c3e] Exercise 25
+> Use Rodrigues' formula to show that $P_{n}(1)=1, n=0,1,2, \ldots$. [Hint: Write $\left(x^{2}-1\right)^{n}=(x-1)^{n}(x+1)^{n}$, and use the Leibniz rule.]
+
+
+> [!exercise|b1f8e5c7-dd53-5606-9605-c6bb22c6cc7c.local at=6501398e-fcfc-56a2-ad5d-70bc830e18f6] Exercise 26
+> (a) Consider the function in Example 2. Derive the Legendre series expansion
+>
+> $$
+> f(x)=\frac{1}{2}+\sum_{n=0}^{\infty}(-1)^{n}\left(\frac{4 n+3}{4 n+4}\right) \frac{(2 n)!}{2^{2 n}(n!)^{2}} P_{2 n+1}(x) .
+> $$
+>
+> [Hint: Exercise 10.]
+> (b) Plot several partial sums of the series and note that near $x=0$, a point of discontinuity of the function, the partial sums overshoot the graph of the function. Do the overshoots disappear with larger partial sums? State a property or a principle concerning the convergence of partial sums of Legendre series near points of discontinuity.
+
+
+> [!exercise|87b15d1f-55d5-5d9b-a343-5873fc6f43d4.local at=68f074f9-1b5f-5655-9980-1cbac549832e] Exercise 27
+> Let $f(x)=|x|,-1 \leq x \leq 1$. (a) Compute the first three nonzero Legendre coefficients of $f$.
+> (b) Derive the Legendre coefficients $A_{0}=\frac{1}{2}, A_{2 n+1}=0$ for all $n$, and
+>
+> $$
+> A_{2 n}=(-1)^{n+1} \frac{n(2 n-2)!}{2^{2 n}(n!)^{2}}\left(\frac{4 n+1}{n+1}\right), \quad n=1,2, \ldots
+> $$
+>
+> [Hint: Exercise 11.]
+> (c) Plot the function and the partial sums of the Legendre series $\sum_{j=0}^{n} A_{j} P_{j}(x)$ for $n=1,2,5$, and 20 .
+> (d) If $f(x)$ is to be approximated by its Legendre series to within 0.05 on the entire interval $-1 \leq x \leq 1$, how large should $n$ be?
+
+
+> [!exercise|1db6dd37-2f11-507a-aabb-14853dedb4e1.local at=42b156bd-f7da-5c34-9c55-f55750b0b718] Exercise 28
+> (a) Find the first eight Legendre coefficients $A_{0}, A_{1}, \ldots, A_{7}$ of the function
+>
+> $$
+> f(x)= \begin{cases}0 & \text { if }-1 \leq x<0 \\ x & \text { if } 0 \leq x \leq 1\end{cases}
+> $$
+>
+> (b) Illustrate Theorem 2 by plotting on the same coordinate axes the graphs of $f$ and the partial sums
+>
+> $$
+> \sum_{j=0}^{3} A_{j} P_{j}(x), \quad \sum_{j=0}^{5} A_{j} P_{j}(x), \quad \sum_{j=0}^{7} A_{j} P_{j}(x) .
+> $$
+
+
+> [!exercise|ca6e9eb6-089d-5607-bb01-3cb196fdc50d.local at=49591eaa-18d5-5a8c-801a-f219967cadfb] Exercise 29
+> Derive the Legendre series of the function in Exercise 28. [Hint: Consider the function $\frac{1}{2}\left(|x|+P_{1}(x)\right)$ and use Exercise 27.]
+
+
+> [!exercise|08b9970f-f8c3-5a5c-9a37-4426866e8310.local at=2735632a-bd21-5573-b96a-2a75beb6838a] Exercise 30
+> (a) Obtain the Legendre series expansion
+>
+> $$
+> \ln (1-x)=\ln 2-1-\sum_{n=1}^{\infty} \frac{2 n+1}{n(n+1)} P_{n}(x), \quad-1<x<1
+> $$
+>
+> [Hint: Exercise 21.]
+> (b) Plot several partial sums to illustrate the convergence of the Legendre series.
+> (Note that the function does not satisfy the hypothesis of Theorem 2, because of its behavior at the endpoint $x=1$, yet the Legendre series does converge. You can establish the convergence of this Legendre series using a different test; see Exercise 39 below.)
+
+
+> [!exercise|86eb8016-07a8-5290-ac1f-03b6534f4986.local at=fa2e0ef8-9f43-5bf5-932c-a91eae1d2606] Exercise 31
+> (a) Make a suitable change of variables in the series expansion of Exercise 30 to derive the Legendre series of $f(x)=\ln (1+x), \quad-1<x<1$.
+> (b) Plot several partial sums to illustrate the convergence of the Legendre series.
+
+
+> [!exercise|20057768-c4e6-5fb5-9cda-2064d88cbe97.local at=61725973-5db0-5118-912a-0828c9586e7d] Exercise 32
+> (a) Expand the Legendre function of the second kind $Q_{0}(x)$ in a Legendre series. The explicit formula for $Q_{0}$ is given in Exercise 23, Section 13.5. [Hint: Exercises 30 and 31.]
+> (b) Plot several partial sums to illustrate the convergence of the Legendre series.
+
+
+> [!prompt|5b8d41ca-e138-5217-ab73-cc8ce825e2c9.local at=b542f6e9-e547-5b98-a3d8-04c4d966b3eb] Shared exercise instructions
+> In Exercises 33 and 34, (a) compute at least eight terms of the Legendre series expansion of the given function. (b) On the same graph, plot the function and several partial sums to illustrate the convergence of the Legendre series. (c) If the function is to be approximated by its Legendre series to within .1 on the entire interval $-1<x<1$, how many terms of the series should you take?
+
+
+> [!exercise|c615516b-a6b1-57f6-8b6e-8aa2b059da8c.local at=cc200909-82b1-5e71-a00f-1b9f4a09c5f4] Exercise 33
+> $f(x)=\cos \frac{\pi}{2} x,-1<x<1$.
+
+
+> [!exercise|5678a947-fd14-52e2-981b-faa44da2e66e.local at=ff575b49-da30-56bb-a6a6-e61ff207123d] Exercise 34
+> $f(x)=\sin x,-1<x<1$.
+
+
+> [!prompt|c367e50b-2a32-5534-8247-a9b045a889a2.local at=c0befc46-8c88-573f-b0d6-77fa6b5f7b7b] Shared exercise instructions
+> Project Problem: Dirichlet test for Legendre series. Do Exercises 35-37, and either 38 or 39.
+
+
+> [!exercise|c8319aa2-6116-5bba-9c97-fd148f63d519.local at=bc50eda0-6256-5c32-80c0-b46f8051d07d] Exercise 35
+> Plot several partial sums $\sum_{k=0}^{n} P_{k}(x)$ and the function $2/(1-x)$ over the
+> interval $[-1,1]$. This should illustrate the inequality
+>
+> $$
+> 0 \leq \sum_{k=0}^{n} P_{k}(x) \leq \frac{2}{1-x}, \quad-1<x<1 .
+> $$
+>
+> The nonnegativity is the Fejér inequality.
+
+
+> [!exercise|bde4c3c8-193d-563e-aa1f-b8161baf6d1c.local at=c3eb79cc-942c-58ae-987a-e0beace5b1a8] Exercise 36
+> Test for uniform convergence of Legendre series with decreasing coefficients. Prove the following test. Suppose that $\left(A_{k}\right)_{k=0}^{\infty}$ is a sequence of positive numbers decreasing to zero. Let $E$ be any closed interval contained in $(-1,1)$. Then the series $\sum_{k=0}^{\infty} A_{k} P_{k}(x)$ is uniformly convergent on $E$. [Hint: Use Exercise 35 and the uniform Dirichlet test: uniformly bounded partial sums of the functions, multiplied by a decreasing scalar sequence tending to zero, give a uniformly convergent series.]
+
+
+> [!exercise|e75d6f00-364a-5caf-8dbe-4446da0a3714.local at=a01a6074-c8fd-53d1-8686-1ef1b16a3335] Exercise 37
+> Test for pointwise convergence of Legendre series with decreasing coefficients. Prove the following test. Suppose that $\left(A_{k}\right)_{k=0}^{\infty}$ is a sequence of positive numbers decreasing to zero. Then the series $\sum_{k=0}^{\infty} A_{k} P_{k}(x)$ converges pointwise for all $x$ in $(-1,1)$. [Hint: Use Exercise 36 on a closed subinterval of $(-1,1)$ containing the point under consideration.]
+
+
+> [!exercise|aa171a0a-b49f-53ca-83d9-4a8f12b563b5.local at=89de7e83-c51f-5563-a564-591a2571d55b] Exercise 38
+> Determine the values of $x$ from the interval $[-1,1]$ for which the series is convergent. Justify your answer, and be sure to check the endpoints.
+> (a) $\quad \sum_{k=0}^{\infty} \frac{P_{k}(x)}{\sqrt{k+1}}$.
+> (b) $\quad \sum_{k=1}^{\infty} \frac{P_{k}(x)}{k}$.
+
+
+> [!exercise|6f120fbd-b833-51e1-953d-7e6669abe09b.local at=922c9a7f-e860-529f-83ce-b4c303610cc3] Exercise 39
+> Discuss the uniform convergence and pointwise convergence of the Legendre series in Exercise 30, based on the tests for convergence in Exercises 36 and 37. Be sure to discuss the behavior of the series at the endpoints.
+
+
+> [!exercise|4b3eccd8-0b77-5140-a541-96dc008194b5.local at=02a831b4-195f-53ca-ad96-67247162cdf8] Exercise 40
+> (a) Find the Legendre series of the function $f(x)=x \ln (1-x),-1<x<1$. [Hint: Exercise 23.]
+> (b) Find the Legendre series of the function $f(x)=x \ln (1+x),-1<x<1$. [Hint: Change variables in (a).]
+
+
+> [!exercise|74a1eedf-ca7c-55ac-aa0f-f6611e34eabc.local at=5f1d221f-cd8d-55a6-a94b-08c763e8a36b] Exercise 41
+> Find the Legendre series of the Legendre function of the second kind $Q_{1}(x)$. For the explicit formula of $Q_{1}(x)$ see Exercise 24, Section 13.5. [Hint: Exercise 40.]
+
+
+> [!exercise|ef64f3cd-3c4f-52a8-8e87-739fe97dd4f0.local at=fcb84280-8e0f-5efb-a489-3e8884df0272] Exercise 42
+> Orthogonality of $\boldsymbol{P}_{\boldsymbol{n}}^{\prime}(\boldsymbol{x})$. (a) Verify that for $m=0,1,2, \ldots$ we have
+>
+> $$
+> \left[\left(1-x^{2}\right) P_{m}^{\prime}(x)\right]^{\prime}=-m(m+1) P_{m}(x) .
+> $$
+>
+> [Hint: Use the differential equation for $P_{m}(x)$.]
+> (b) Show that if $m$ and $n$ are positive integers with $m \neq n$, then
+>
+> $$
+> \int_{-1}^{1} P_{n}^{\prime}(x) P_{m}^{\prime}(x)\left(1-x^{2}\right) d x=0
+> $$
+>
+> This states that the functions $P_{n}^{\prime}(x)(n=1,2, \ldots)$ are orthogonal on the interval $-1 \leq x \leq 1$ with respect to the weight function ( $1-x^{2}$ ). This result is a special case of Theorem 1, Section 13.7. [Hint: Integrate by parts and use (a).]
+
+
+> [!exercise|1f6063bb-b50e-5099-a105-6eabc3e97269.local at=c097617d-29b6-5419-bf82-ec225d0a9389] Exercise 43
+> The $j$ th Legendre coefficient. In this exercise we justify (7). Multiply both sides of (6) by $P_{j}(x)$ and then integrate from -1 to 1 . Assume that term-by-term integration is allowed and derive (7) using Theorem 1.
+
+
+> [!exercise|37d846fa-1172-569f-9542-7dc365051f8c.local at=b1da8103-92ff-5a0c-81b5-738aa7f30475] Exercise 44
+> Legendre series of polynomials. (a) Use Exercise 12 to show that if $p(x)$ is a polynomial of degree $n$, then $\int_{-1}^{1} p(x) P_{m}(x) d x=0$ for all $m>n$.
+> (b) Conclude that if $p(x)$ is a polynomial of degree $n$, then the Legendre series of $p(x)$ has only finitely many terms.
+
+
+> [!prompt|5191ce98-b746-5bae-b95a-c4e2024667af.local at=550f52f6-5cad-57cb-bbb8-27d32dd3a77f] Shared exercise instructions
+> In Exercises 45-48, find the Legendre series of the given polynomial. [Hint: Write the polynomial as a linear combination of the Legendre polynomials, and then determine the coefficients.]
+
+
+> [!exercise|1da02788-4421-5da7-b408-212923763ab6.local at=c56bdb1a-548d-53f2-8620-d0f2535b703b] Exercise 45
+> $p(x)=x^{2}+2 x+1$.
+
+
+> [!exercise|1eb3a2c6-949e-513b-9582-503fdc2888e2.local at=ff150b75-704f-5983-a42a-7335ffaa58c7] Exercise 46
+> $p(x)=63 x^{5}-7 x^{3}+15 x$.
+
+
+> [!exercise|f5a89e84-f39a-5a72-9718-a11b0411aaf2.local at=e6ea68c9-cfb7-5647-8d19-22f2c88900d8] Exercise 47
+> $p(x)=x^{4}+2 x^{3}+x^{2}+x$.
+
+
+> [!exercise|6f8e21fd-4f9e-5379-8db8-39ba49423bd9.local at=d7663a12-a42e-59aa-a65e-76a7c6cafb7f] Exercise 48
+> $p(x)=x^{6}$.
+

`````
