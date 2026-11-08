
# Editorial records

Reading note: 4.1 Sequences and Series of Complex Numbers.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Callout 145: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!definition] Limit of a Complex Sequence
> We say that a sequence $\left\{a_{n}\right\}$ converges to a complex number $L$ or has limit $L$ as $n$ tends to infinity and write
>
> $$
> \lim _{n \rightarrow \infty} a_{n}=L
> $$
>
> if given any $\epsilon>0$ there is an integer $N$ such that
>
> $$
> \left|a_{n}-L\right|<\epsilon \quad \text { for all } n \geq N .
> $$
>
> If the sequence $\left\{a_{n}\right\}$ does not converge, then we say that it diverges.
````
### After

````text
> [!definition] Limit of a Sequence
> We say that a sequence $\left\{a_{n}\right\}$ converges to a complex number $L$ or has limit $L$ as $n$ tends to infinity and write
>
> $$
> \lim _{n \rightarrow \infty} a_{n}=L
> $$
>
> if given any $\epsilon>0$ there is an integer $N$ such that
>
> $$
> \left|a_{n}-L\right|<\epsilon \quad \text { for all } n \geq N .
> $$
>
> If the sequence $\left\{a_{n}\right\}$ does not converge, then we say that it diverges.
````

## 2. Callout 146: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Algebraic Limit Laws for Complex Sequences
> If $\left\{a_{n}\right\}$ and $\left\{b_{n}\right\}$ are convergent sequences of complex numbers and $\alpha$ and $\beta$ are complex numbers, then
>
> $$
> \begin{aligned}
> & \lim _{n \rightarrow \infty}\left(\alpha a_{n}+\beta b_{n}\right)=\alpha \lim _{n \rightarrow \infty} a_{n}+\beta \lim _{n \rightarrow \infty} b_{n} ; \\
> & \lim _{n \rightarrow \infty}\left(a_{n} b_{n}\right)=\lim _{n \rightarrow \infty} a_{n} \lim _{n \rightarrow \infty} b_{n} ; \\
> & \lim _{n \rightarrow \infty} \frac{a_{n}}{b_{n}}=\frac{\lim _{n \rightarrow \infty} a_{n}}{\lim _{n \rightarrow \infty} b_{n}} \text { if } \lim _{n \rightarrow \infty} b_{n} \neq 0 .
> \end{aligned}
> $$
````
### After

````text
> [!theorem] Limit Laws for Sequences
> If $\left\{a_{n}\right\}$ and $\left\{b_{n}\right\}$ are convergent sequences of complex numbers and $\alpha$ and $\beta$ are complex numbers, then
>
> $$
> \begin{aligned}
> & \lim _{n \rightarrow \infty}\left(\alpha a_{n}+\beta b_{n}\right)=\alpha \lim _{n \rightarrow \infty} a_{n}+\beta \lim _{n \rightarrow \infty} b_{n} ; \\
> & \lim _{n \rightarrow \infty}\left(a_{n} b_{n}\right)=\lim _{n \rightarrow \infty} a_{n} \lim _{n \rightarrow \infty} b_{n} ; \\
> & \lim _{n \rightarrow \infty} \frac{a_{n}}{b_{n}}=\frac{\lim _{n \rightarrow \infty} a_{n}}{\lim _{n \rightarrow \infty} b_{n}} \text { if } \lim _{n \rightarrow \infty} b_{n} \neq 0 .
> \end{aligned}
> $$
````

## 3. Callout 147: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Continuous Functions Preserve Limits of Complex Sequences
> Let $(a_n)$ be a complex sequence in the domain of $f$.
>
> If $\lim _{n \rightarrow \infty} a_{n}=L$ and $f$ is continuous at $L$, then
>
> $$
> \lim _{n \rightarrow \infty} f\left(a_{n}\right)=f(L)
> $$
````
### After

````text
> [!theorem] Substitution Law
> Let $(a_n)$ be a complex sequence in the domain of $f$.
>
> If $\lim _{n \rightarrow \infty} a_{n}=L$ and $f$ is continuous at $L$, then
>
> $$
> \lim _{n \rightarrow \infty} f\left(a_{n}\right)=f(L)
> $$
````

## 4. Callout 149: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Boundedness of Convergent Complex Sequences
> A convergent complex sequence is bounded. That is, if $\left\{a_{n}\right\}$ is a convergent complex sequence, then there is a positive real number $M>0$ such that $\left|a_{n}\right| \leq M$ for all $n$.
````
### After

````text
> [!theorem] Boundedness
> A convergent complex sequence is bounded. That is, if $\left\{a_{n}\right\}$ is a convergent complex sequence, then there is a positive real number $M>0$ such that $\left|a_{n}\right| \leq M$ for all $n$.
````

## 5. Callout 150: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Squeeze and Bounded-Factor Limits for Complex Sequences
> Let $(a_n)$ and $(b_n)$ be complex sequences.
>
> (i) Suppose that $\lim _{n \rightarrow \infty} a_{n}=0$ and $\left|b_{n}\right| \leq\left|a_{n}\right|$ for all $n \geq n_{0}$. Then $\lim _{n \rightarrow \infty} b_{n}=0$.
> (ii) Suppose that $\lim _{n \rightarrow \infty} a_{n}=0$ and $\left\{b_{n}\right\}$ is a bounded sequence, then $\lim _{n \rightarrow \infty} a_{n} b_{n}=0$.
````
### After

````text
> [!theorem] Squeeze Theorem
> Let $(a_n)$ and $(b_n)$ be complex sequences.
>
> (i) Suppose that $\lim _{n \rightarrow \infty} a_{n}=0$ and $\left|b_{n}\right| \leq\left|a_{n}\right|$ for all $n \geq n_{0}$. Then $\lim _{n \rightarrow \infty} b_{n}=0$.
> (ii) Suppose that $\lim _{n \rightarrow \infty} a_{n}=0$ and $\left\{b_{n}\right\}$ is a bounded sequence, then $\lim _{n \rightarrow \infty} a_{n} b_{n}=0$.
````

## 6. Callout 151: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Componentwise Convergence of Complex Sequences
> Suppose that $\left\{a_{n}\right\}$ is a sequence of complex numbers and write $a_{n}=x_{n}+i y_{n}$, where $x_{n}=\operatorname{Re} a_{n}$ and $y_{n}=\operatorname{Im} a_{n}$. Then
>
> $$
> \lim _{n \rightarrow \infty} a_{n}=L=\alpha+i \beta \Leftrightarrow \lim _{n \rightarrow \infty} x_{n}=\alpha \text { and } \lim _{n \rightarrow \infty} y_{n}=\beta .
> $$
````
### After

````text
> [!theorem] Real and Imaginary Parts of Sequences
> Suppose that $\left\{a_{n}\right\}$ is a sequence of complex numbers and write $a_{n}=x_{n}+i y_{n}$, where $x_{n}=\operatorname{Re} a_{n}$ and $y_{n}=\operatorname{Im} a_{n}$. Then
>
> $$
> \lim _{n \rightarrow \infty} a_{n}=L=\alpha+i \beta \Leftrightarrow \lim _{n \rightarrow \infty} x_{n}=\alpha \text { and } \lim _{n \rightarrow \infty} y_{n}=\beta .
> $$
````

## 7. Callout 152: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!definition] Cauchy Sequence of Complex Numbers
> A complex sequence $\left\{a_{n}\right\}$ is said to be a Cauchy sequence if given any $\epsilon>0$ there is an integer $N$ such that
>
> $$
> \left|a_{n}-a_{m}\right|<\epsilon \quad \text { for all } m, n \geq N
> $$
````
### After

````text
> [!definition] Cauchy Sequence
> A complex sequence $\left\{a_{n}\right\}$ is said to be a Cauchy sequence if given any $\epsilon>0$ there is an integer $N$ such that
>
> $$
> \left|a_{n}-a_{m}\right|<\epsilon \quad \text { for all } m, n \geq N
> $$
````

## 8. Callout 153: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Cauchy Criterion for Convergence in the Complex Plane
> A sequence of complex numbers $\left\{a_{n}\right\}$ converges if and only if it is a Cauchy sequence.
````
### After

````text
> [!theorem] Cauchy Sequences
> A sequence of complex numbers $\left\{a_{n}\right\}$ converges if and only if it is a Cauchy sequence.
````

## 9. Callout 154: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!definition] Convergence and Sum of a Complex Series
> For complex terms $a_n$, define the partial sums $s_n=\sum_{k=1}^{n}a_k$.
>
> We say that a series $\sum_{n=1}^{\infty} a_{n}$ converges or is convergent to a complex number $s$ and we write
>
> $$
> s=\sum_{n=1}^{\infty} a_{n}
> $$
>
> if the sequence of partial sums $\left\{s_{n}\right\}$ converges to $s: \lim _{n \rightarrow \infty} s_{n}=s$. Otherwise, we say that the series $\sum_{n=1}^{\infty} a_{n}$ diverges or is divergent.
````
### After

````text
> [!definition] Limit of a Series
> For complex terms $a_n$, define the partial sums $s_n=\sum_{k=1}^{n}a_k$.
>
> We say that a series $\sum_{n=1}^{\infty} a_{n}$ converges or is convergent to a complex number $s$ and we write
>
> $$
> s=\sum_{n=1}^{\infty} a_{n}
> $$
>
> if the sequence of partial sums $\left\{s_{n}\right\}$ converges to $s: \lim _{n \rightarrow \infty} s_{n}=s$. Otherwise, we say that the series $\sum_{n=1}^{\infty} a_{n}$ diverges or is divergent.
````

## 10. Callout 155: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Linearity, Conjugation, and Components of Convergent Complex Series
> Let the series terms be complex numbers.
>
> If $\sum_{n=1}^{\infty} a_{n}$ and $\sum_{n=1}^{\infty} b_{n}$ are convergent series and $\alpha$ and $\beta$ are complex numbers, then
> (i) $\sum_{n=1}^{\infty}\left(\alpha a_{n}+\beta b_{n}\right)=\alpha \sum_{n=1}^{\infty} a_{n}+\beta \sum_{n=1}^{\infty} b_{n}$;
> (ii) $\overline{\sum_{n=1}^{\infty} a_{n}}=\sum_{n=1}^{\infty} \overline{a_{n}}$;
> (iii) $\operatorname{Re}\left(\sum_{n=1}^{\infty} a_{n}\right)=\sum_{n=1}^{\infty} \operatorname{Re}\left(a_{n}\right)$ and $\operatorname{Im}\left(\sum_{n=1}^{\infty} a_{n}\right)=\sum_{n=1}^{\infty} \operatorname{Im}\left(a_{n}\right)$.
````
### After

````text
> [!theorem] Linearity, Conjugation, Real and Imaginary Parts
> Let the series terms be complex numbers.
>
> If $\sum_{n=1}^{\infty} a_{n}$ and $\sum_{n=1}^{\infty} b_{n}$ are convergent series and $\alpha$ and $\beta$ are complex numbers, then
> (i) $\sum_{n=1}^{\infty}\left(\alpha a_{n}+\beta b_{n}\right)=\alpha \sum_{n=1}^{\infty} a_{n}+\beta \sum_{n=1}^{\infty} b_{n}$;
> (ii) $\overline{\sum_{n=1}^{\infty} a_{n}}=\sum_{n=1}^{\infty} \overline{a_{n}}$;
> (iii) $\operatorname{Re}\left(\sum_{n=1}^{\infty} a_{n}\right)=\sum_{n=1}^{\infty} \operatorname{Re}\left(a_{n}\right)$ and $\operatorname{Im}\left(\sum_{n=1}^{\infty} a_{n}\right)=\sum_{n=1}^{\infty} \operatorname{Im}\left(a_{n}\right)$.
````

## 11. Callout 156: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Term Test for Divergence of a Complex Series
> Let the series terms be complex numbers.
>
> If $\sum_{n=1}^{\infty} a_{n}$ is convergent, then $\lim _{n \rightarrow \infty} a_{n}=0$. Equivalently, if either $\lim _{n \rightarrow \infty} a_{n} \neq 0$ or $\lim _{n \rightarrow \infty} a_{n}$ does not exist, then $\sum_{n=1}^{\infty} a_{n}$ diverges.
````
### After

````text
> [!theorem] The nth Term Test for Divergence
> Let the series terms be complex numbers.
>
> If $\sum_{n=1}^{\infty} a_{n}$ is convergent, then $\lim _{n \rightarrow \infty} a_{n}=0$. Equivalently, if either $\lim _{n \rightarrow \infty} a_{n} \neq 0$ or $\lim _{n \rightarrow \infty} a_{n}$ does not exist, then $\sum_{n=1}^{\infty} a_{n}$ diverges.
````

## 12. Callout 157: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!proposition] Vanishing Tails of a Convergent Complex Series
> Let the series terms be complex numbers.
>
> If $\sum_{n=1}^{\infty} a_{n}$ is convergent, then $\lim _{m \rightarrow \infty} \sum_{n=m+1}^{\infty} a_{n}=0$. Hence if a series converges, its tail must go to 0 .
````
### After

````text
> [!proposition] Tail of Series
> Let the series terms be complex numbers.
>
> If $\sum_{n=1}^{\infty} a_{n}$ is convergent, then $\lim _{m \rightarrow \infty} \sum_{n=m+1}^{\infty} a_{n}=0$. Hence if a series converges, its tail must go to 0 .
````

## 13. Callout 158: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Absolute Convergence Implies Convergence of a Complex Series
> Let the series terms be complex numbers.
>
> If $\sum_{n=1}^{\infty} a_{n}$ is absolutely convergent, then it is convergent. In symbols,
>
> $$
> \sum_{n=1}^{\infty}\left|a_{n}\right|<\infty \Rightarrow \sum_{n=1}^{\infty} a_{n} \text { converges. }
> $$
````
### After

````text
> [!theorem] Absolute Convergence Implies Convergence
> Let the series terms be complex numbers.
>
> If $\sum_{n=1}^{\infty} a_{n}$ is absolutely convergent, then it is convergent. In symbols,
>
> $$
> \sum_{n=1}^{\infty}\left|a_{n}\right|<\infty \Rightarrow \sum_{n=1}^{\infty} a_{n} \text { converges. }
> $$
````

## 14. Callout 159: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Comparison Test for Absolute Convergence of a Complex Series
> Suppose that $a_{n}$ are complex numbers, $b_{n}$ are real numbers, $\left|a_{n}\right| \leq b_{n}$ for all $n \geq n_{0}$, and $\sum_{n=1}^{\infty} b_{n}$ is convergent. Then $\sum_{n=1}^{\infty} a_{n}$ is absolutely convergent.
````
### After

````text
> [!theorem] Comparison Test
> Suppose that $a_{n}$ are complex numbers, $b_{n}$ are real numbers, $\left|a_{n}\right| \leq b_{n}$ for all $n \geq n_{0}$, and $\sum_{n=1}^{\infty} b_{n}$ is convergent. Then $\sum_{n=1}^{\infty} a_{n}$ is absolutely convergent.
````

## 15. Callout 160: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Ratio Test for a Complex Series
> Suppose that
>
> $$
> \rho=\lim _{n \rightarrow \infty}\left|\frac{a_{n+1}}{a_{n}}\right|
> $$
>
> exists or is infinite. Then the complex series $\sum_{n=1}^{\infty} a_{n}$ of nonzero terms converges absolutely if $\rho<1$ and diverges if $\rho>1$. If $\rho=1$ the test is inconclusive.
````
### After

````text
> [!theorem] Ratio Test
> Suppose that
>
> $$
> \rho=\lim _{n \rightarrow \infty}\left|\frac{a_{n+1}}{a_{n}}\right|
> $$
>
> exists or is infinite. Then the complex series $\sum_{n=1}^{\infty} a_{n}$ of nonzero terms converges absolutely if $\rho<1$ and diverges if $\rho>1$. If $\rho=1$ the test is inconclusive.
````

## 16. Callout 161: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Root Test for a Complex Series: Limit Form
> Suppose that
>
> $$
> \rho=\lim _{n \rightarrow \infty}\left|a_{n}\right|^{1 / n} 
> $$
>
> either exists or is infinite. Then the complex series $\sum_{n=1}^{\infty} a_{n}$ converges absolutely if $\rho<1$ and diverges if $\rho>1$. If $\rho=1$ the test is inconclusive.
````
### After

````text
> [!theorem] Root Test
> Suppose that
>
> $$
> \rho=\lim _{n \rightarrow \infty}\left|a_{n}\right|^{1 / n} 
> $$
>
> either exists or is infinite. Then the complex series $\sum_{n=1}^{\infty} a_{n}$ converges absolutely if $\rho<1$ and diverges if $\rho>1$. If $\rho=1$ the test is inconclusive.
````

## 17. Callout 162: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Bounded Absolute Partial Sums and Absolute Convergence
> Let the series terms be complex numbers.
>
> Suppose that there is a positive number $M>0$ such that $\sum_{n=1}^{N}\left|a_{n}\right| \leq M$ for all $N$. Then the series $\sum_{n=1}^{\infty} a_{n}$ is absolutely convergent.
````
### After

````text
> [!theorem] Bounded Partial Sums
> Let the series terms be complex numbers.
>
> Suppose that there is a positive number $M>0$ such that $\sum_{n=1}^{N}\left|a_{n}\right| \leq M$ for all $N$. Then the series $\sum_{n=1}^{\infty} a_{n}$ is absolutely convergent.
````

## 18. Callout 163: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Rearrangement Invariance of Absolutely Convergent Complex Series
> Let the series terms be complex numbers.
>
> If $\sum_{n=1}^{\infty} a_{n}$ is absolutely convergent, then every rearrangement is absolutely convergent and converges to the same limit.
````
### After

````text
> [!theorem] Rearrangements
> Let the series terms be complex numbers.
>
> If $\sum_{n=1}^{\infty} a_{n}$ is absolutely convergent, then every rearrangement is absolutely convergent and converges to the same limit.
````

## 19. Callout 164: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Cauchy Products of Absolutely Convergent Complex Series
> Let the series terms be complex numbers.
>
> Suppose that $\sum_{n=0}^{\infty} a_{n}$ and $\sum_{n=0}^{\infty} b_{n}$ are absolutely convergent. Then their Cauchy product $\sum_{n=0}^{\infty} c_{n}$, where $c_n=\sum_{k=0}^{n}a_k b_{n-k}$, is absolutely convergent and we have
>
> $$
> \sum_{n=0}^{\infty} c_{n}=\left(\sum_{n=0}^{\infty} a_{n}\right)\left(\sum_{n=0}^{\infty} b_{n}\right) .
> $$
````
### After

````text
> [!theorem] Cauchy Products
> Let the series terms be complex numbers.
>
> Suppose that $\sum_{n=0}^{\infty} a_{n}$ and $\sum_{n=0}^{\infty} b_{n}$ are absolutely convergent. Then their Cauchy product $\sum_{n=0}^{\infty} c_{n}$, where $c_n=\sum_{k=0}^{n}a_k b_{n-k}$, is absolutely convergent and we have
>
> $$
> \sum_{n=0}^{\infty} c_{n}=\left(\sum_{n=0}^{\infty} a_{n}\right)\left(\sum_{n=0}^{\infty} b_{n}\right) .
> $$
````

## Source-to-current comparison

Source: /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 04 Complex Series/4.1 Sequences and Series of Complex Numbers.md

This exact comparison preserves the full change evidence, including formatting, OCR corrections, restored source wording, and required standalone context. The entries above explain the recovery edits. The comparison is not a claim that every difference is a correction; component serialization, callout wrapping, and printed labels outside callouts are formatting.

`````diff
--- /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 04 Complex Series/4.1 Sequences and Series of Complex Numbers.md
+++ /Users/gradyclopton/ObsidianVaults/complex_analysis/Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 04 Complex Series/4.1 Sequences and Series of Complex Numbers.md
@@ -41,25 +41,35 @@
 
 
 
-> [!figure] Figure 1
-> ![300](./images/5443c314-b89d-4dd1-b950-bb21550520a5-02_519_502_1044_129.jpg)
-> Figure 1 The sequence $\left\{a_{n}\right\}$ converges to the complex number $L$.
-
-
-
-> [!definition] Definition 1: Limit of a Sequence
+```scientific-figure
+id: 0c1858e3-afe2-410f-add8-d5de11c15c83
+numbered: false
+title: ""
+caption: "**Figure 1.** The sequence $\\left\\{a_{n}\\right\\}$ converges to the complex number $L$."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 04 Complex Series/images/5443c314-b89d-4dd1-b950-bb21550520a5-02_519_502_1044_129.jpg
+    caption: ""
+```
+
+
+
+<!-- Source label: Definition 1: Limit of a Sequence -->
+> [!definition] Limit of a Sequence
 > We say that a sequence $\left\{a_{n}\right\}$ converges to a complex number $L$ or has limit $L$ as $n$ tends to infinity and write
-> 
+>
 > $$
 > \lim _{n \rightarrow \infty} a_{n}=L
 > $$
-> 
+>
 > if given any $\epsilon>0$ there is an integer $N$ such that
-> 
+>
 > $$
 > \left|a_{n}-L\right|<\epsilon \quad \text { for all } n \geq N .
 > $$
-> 
+>
 > If the sequence $\left\{a_{n}\right\}$ does not converge, then we say that it diverges.
 
 
@@ -86,10 +96,18 @@
 
 
 
-> [!figure] Figure 2
-> 
-> ![300](./images/5443c314-b89d-4dd1-b950-bb21550520a5-03_418_410_364_46.jpg)
-> Figure 2 The first five terms of the sequence $a_{n}=\frac{e^{\operatorname{tn} \frac{\pi}{4}}}{n}$, and the limit $L=0$. Note how the arguments of two successive terms differ by $\frac{\pi}{4}$. Do you see why?
+```scientific-figure
+id: 11f115ee-8c4b-46c1-9f58-ef31ca663b1a
+numbered: false
+title: ""
+caption: "**Figure 2.** The first five terms of the sequence $a_{n}=\\frac{e^{\\operatorname{tn} \\frac{\\pi}{4}}}{n}$, and the limit $L=0$. Note how the arguments of two successive terms differ by $\\frac{\\pi}{4}$. Do you see why?"
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 04 Complex Series/images/5443c314-b89d-4dd1-b950-bb21550520a5-03_418_410_364_46.jpg
+    caption: ""
+```
 
 
 
@@ -107,9 +125,10 @@
 Limits of sequences have properties similar to those of functions, because the definitions of limits are similar in both cases. We list some of these properties for ease of reference and omit most of the proofs that can be derived by using the same techniques as in Section 2.2.
 
 
-> [!theorem] Theorem 1: Limit Laws for Sequences
-> If $\left\{a_{n}\right\}$ and $\left\{b_{n}\right\}$ are convergent sequences and $\alpha$ and $\beta$ are complex numbers, then
-> 
+<!-- Source label: Theorem 1: Limit Laws for Sequences -->
+> [!theorem] Limit Laws for Sequences
+> If $\left\{a_{n}\right\}$ and $\left\{b_{n}\right\}$ are convergent sequences of complex numbers and $\alpha$ and $\beta$ are complex numbers, then
+>
 > $$
 > \begin{aligned}
 > & \lim _{n \rightarrow \infty}\left(\alpha a_{n}+\beta b_{n}\right)=\alpha \lim _{n \rightarrow \infty} a_{n}+\beta \lim _{n \rightarrow \infty} b_{n} ; \\
@@ -117,41 +136,46 @@
 > & \lim _{n \rightarrow \infty} \frac{a_{n}}{b_{n}}=\frac{\lim _{n \rightarrow \infty} a_{n}}{\lim _{n \rightarrow \infty} b_{n}} \text { if } \lim _{n \rightarrow \infty} b_{n} \neq 0 .
 > \end{aligned}
 > $$
-> 
 
 The following useful result is an immediate consequence of continuity.
 
 
-> [!theorem] Theorem 2: Substitution Law
+<!-- Source label: Theorem 2: Substitution Law -->
+> [!theorem] Substitution Law
+> Let $(a_n)$ be a complex sequence in the domain of $f$.
+>
 > If $\lim _{n \rightarrow \infty} a_{n}=L$ and $f$ is continuous at $L$, then
-> 
+>
 > $$
 > \lim _{n \rightarrow \infty} f\left(a_{n}\right)=f(L)
 > $$
-> 
 
 Applying Theorem 2 with the continuous functions $f(z)=\bar{z}$ and $g(z)=|z|$, we obtain the following.
 
 
-> [!corollary] Corollary 1
-> If $\left\{a_{n}\right\}$ is a convergent sequence with $L=\lim _{n \rightarrow \infty} a_{n}$, then
-> 
+<!-- Source label: Corollary 1 -->
+> [!corollary] Limits of Conjugates and Moduli of Complex Sequences
+> If $\left\{a_{n}\right\}$ is a convergent complex sequence with $L=\lim _{n \rightarrow \infty} a_{n}$, then
+>
 > $$
 > \lim _{n \rightarrow \infty} \overline{a_{n}}=\overline{\lim _{n \rightarrow \infty} a_{n}}=\bar{L}, \quad \text { and } \quad \lim _{n \rightarrow \infty}\left|a_{n}\right|=\left|\lim _{n \rightarrow \infty} a_{n}\right|=|L| .
 > $$
-> 
 
 In particular, if $\left\{a_{n}\right\}$ converges, then $\left\{\left|a_{n}\right|\right\}$ converges. The converse is not true, as illustrated by Example 1(a), where $\left|a_{n}\right|=1$ and so $\left\{\left|a_{n}\right|\right\}$ obviously converges to 1 , but $\left\{a_{n}\right\}$ is divergent.
 
 A sequence of complex numbers $\left\{a_{n}\right\}$ is said to be bounded if there is a positive number $M>0$ such that $\left|a_{n}\right| \leq M$ for all $n$. The following theorem states that all convergent sequences are bounded.
 
 
-> [!theorem] Theorem 3: Boundedness
-> A convergent sequence is bounded. That is, if $\left\{a_{n}\right\}$ is a convergent sequence, then there is a positive real number $M>0$ such that $\left|a_{n}\right| \leq M$ for all $n$.
+<!-- Source label: Theorem 3: Boundedness -->
+> [!theorem] Boundedness
+> A convergent complex sequence is bounded. That is, if $\left\{a_{n}\right\}$ is a convergent complex sequence, then there is a positive real number $M>0$ such that $\left|a_{n}\right| \leq M$ for all $n$.
 
 We also have a squeeze theorem, like the one from calculus.
 
-> [!theorem] Theorem 4: Squeeze Theorem
+<!-- Source label: Theorem 4: Squeeze Theorem -->
+> [!theorem] Squeeze Theorem
+> Let $(a_n)$ and $(b_n)$ be complex sequences.
+>
 > (i) Suppose that $\lim _{n \rightarrow \infty} a_{n}=0$ and $\left|b_{n}\right| \leq\left|a_{n}\right|$ for all $n \geq n_{0}$. Then $\lim _{n \rightarrow \infty} b_{n}=0$.
 > (ii) Suppose that $\lim _{n \rightarrow \infty} a_{n}=0$ and $\left\{b_{n}\right\}$ is a bounded sequence, then $\lim _{n \rightarrow \infty} a_{n} b_{n}=0$.
 
@@ -162,13 +186,13 @@
 The following result is useful in establishing properties of complex-valued sequences by using the corresponding ones for real-valued sequences.
 
 
-> [!theorem] Theorem 5: Real and Imaginary Parts of Sequences
+<!-- Source label: Theorem 5: Real and Imaginary Parts of Sequences -->
+> [!theorem] Real and Imaginary Parts of Sequences
 > Suppose that $\left\{a_{n}\right\}$ is a sequence of complex numbers and write $a_{n}=x_{n}+i y_{n}$, where $x_{n}=\operatorname{Re} a_{n}$ and $y_{n}=\operatorname{Im} a_{n}$. Then
-> 
+>
 > $$
 > \lim _{n \rightarrow \infty} a_{n}=L=\alpha+i \beta \Leftrightarrow \lim _{n \rightarrow \infty} x_{n}=\alpha \text { and } \lim _{n \rightarrow \infty} y_{n}=\beta .
 > $$
-> 
 
 Our next example shows how we can use the preceding theorems along with our knowledge of real-valued sequences to compute limits of complexvalued sequences.
 
@@ -184,7 +208,9 @@
 
 
 
-**Solution** Recall that for any real number $r \geq 0$, we have
+##### solution
+
+Recall that for any real number $r \geq 0$, we have
 
 $$
 \lim _{n \rightarrow \infty} r^{n}= \begin{cases}0 & \text { if } 0 \leq r<1, \\ 1 & \text { if } r=1, \\ \infty & \text { if } r>1 .\end{cases}
@@ -212,13 +238,13 @@
 
 
 
-> [!definition] Definition 2: Cauchy Sequence
-> A sequence $\left\{a_{n}\right\}$ is said to be a Cauchy sequence if given any $\epsilon>0$ there is an integer $N$ such that
-> 
+<!-- Source label: Definition 2: Cauchy Sequence -->
+> [!definition] Cauchy Sequence
+> A complex sequence $\left\{a_{n}\right\}$ is said to be a Cauchy sequence if given any $\epsilon>0$ there is an integer $N$ such that
+>
 > $$
 > \left|a_{n}-a_{m}\right|<\epsilon \quad \text { for all } m, n \geq N
 > $$
-> 
 
 
 
@@ -227,7 +253,8 @@
 
 
 
-> [!theorem] Theorem 6: Cauchy Sequences
+<!-- Source label: Theorem 6: Cauchy Sequences -->
+> [!theorem] Cauchy Sequences
 > A sequence of complex numbers $\left\{a_{n}\right\}$ converges if and only if it is a Cauchy sequence.
 
 **Proof** Suppose that $\left\{a_{n}\right\}$ converges to a limit $L$. Given $\epsilon>0$, let $N$ be such that $n \geq N \Rightarrow\left|a_{n}-L\right|<\frac{\epsilon}{2}$. For $m, n \geq N$, we have by the triangle inequality (_Figure 3_):
@@ -238,10 +265,18 @@
 
 
 
-> [!figure] Figure 3
-> 
-> ![300](./images/5443c314-b89d-4dd1-b950-bb21550520a5-05_359_435_1246_6.jpg)
-> Figure 3 For the proof of Theorem 6, the inequality $a_{m}-a_{n} \mid<\epsilon$ if $\left|a_{m}-L\right|<\frac{\epsilon}{2}$ and $\left|a_{n}-L\right|<\frac{\epsilon}{2}$.
+```scientific-figure
+id: 71749833-c5d4-4a1b-8435-c2e1f31501d6
+numbered: false
+title: ""
+caption: "**Figure 3.** For the proof of Theorem 6, the inequality $a_{m}-a_{n} \\mid<\\epsilon$ if $\\left|a_{m}-L\\right|<\\frac{\\epsilon}{2}$ and $\\left|a_{n}-L\\right|<\\frac{\\epsilon}{2}$."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 04 Complex Series/images/5443c314-b89d-4dd1-b950-bb21550520a5-05_359_435_1246_6.jpg
+    caption: ""
+```
 
 
 
@@ -272,14 +307,17 @@
 $$
 
 
-> [!definition] Definition 3: Limit of a Series
+<!-- Source label: Definition 3: Limit of a Series -->
+> [!definition] Limit of a Series
+> For complex terms $a_n$, define the partial sums $s_n=\sum_{k=1}^{n}a_k$.
+>
 > We say that a series $\sum_{n=1}^{\infty} a_{n}$ converges or is convergent to a complex number $s$ and we write
-> 
+>
 > $$
 > s=\sum_{n=1}^{\infty} a_{n}
 > $$
-> 
-> if the sequence of partial sums $\left\{s_{n}\right\}$ converges to $s: \lim _{n \rightarrow \infty} s_{n}=s$. Otherwise. we say that the series $\sum_{n=1}^{\infty} a_{n}$ diverges or is divergent.
+>
+> if the sequence of partial sums $\left\{s_{n}\right\}$ converges to $s: \lim _{n \rightarrow \infty} s_{n}=s$. Otherwise, we say that the series $\sum_{n=1}^{\infty} a_{n}$ diverges or is divergent.
 
 
 
@@ -297,7 +335,9 @@
 
 
 
-**Solution** Consider the partial sum (a typical case is shown in _Figure 4_):
+##### solution
+
+Consider the partial sum (a typical case is shown in _Figure 4_):
 
 $$
 s_{n}=1+z+z^{2}+\cdots+z^{n} .
@@ -305,10 +345,18 @@
 
 
 
-> [!figure] Figure 4
-> 
-> ![300](./images/5443c314-b89d-4dd1-b950-bb21550520a5-06_462_451_1262_201.jpg)
-> Figure 4 Terms in a convergent geometric series $(|z|<$ 1). To get a partial sum $s_{n}$, add the vectors $1, z, \ldots, z^{n}$ using the head-to-tail method.
+```scientific-figure
+id: 138ddf7d-c8e3-45a4-880f-f0143d1ab1a3
+numbered: false
+title: ""
+caption: "**Figure 4.** Terms in a convergent geometric series $(|z|<$ 1). To get a partial sum $s_{n}$, add the vectors $1, z, \\ldots, z^{n}$ using the head-to-tail method."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 04 Complex Series/images/5443c314-b89d-4dd1-b950-bb21550520a5-06_462_451_1262_201.jpg
+    caption: ""
+```
 
 
 If $z=1$ this partial sum is clearly equal to $n+1$ and hence the series diverges. For $z \neq 1$, we multiply and divide the right side of (6) by $1-z \neq 0$, simplify, and get
@@ -334,7 +382,9 @@
 > 
 > is convergent and find its sum.
 
-**Solution** The series is a geometric series of the form $\sum w^{n}$ where $w=\frac{1}{4+2 z}$. It converges to $\frac{1}{1-w}$ if and only if $|w|<1$. Expressing these results in terms of $z$, we find that the series converges to
+##### solution
+
+The series is a geometric series of the form $\sum w^{n}$ where $w=\frac{1}{4+2 z}$. It converges to $\frac{1}{1-w}$ if and only if $|w|<1$. Expressing these results in terms of $z$, we find that the series converges to
 
 $$
 \frac{1}{1-\frac{1}{4+2 z}}=\frac{4+2 z}{3+2 z}
@@ -356,10 +406,18 @@
 
 
 
-> [!figure] Figure 5
-> 
-> ![300](./images/5443c314-b89d-4dd1-b950-bb21550520a5-07_454_458_863_40.jpg)
-> Figure 5 The shaded region describes all $z$ such that $\frac{1}{2}< [z+2$ ]. These are the points where the series in Example 4 converges.
+```scientific-figure
+id: a69a343c-93c7-4abb-bfd5-5e794c25a1a3
+numbered: false
+title: ""
+caption: "**Figure 5.** The shaded region describes all $z$ such that $\\frac{1}{2}< [z+2$ ]. These are the points where the series in Example 4 converges."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 04 Complex Series/images/5443c314-b89d-4dd1-b950-bb21550520a5-07_454_458_863_40.jpg
+    caption: ""
+```
 
 
 # 4.1.1 Properties of Series and Tests of Convergence
@@ -370,7 +428,10 @@
 
 For geometric series we are lucky in that we are able to find a closed expression for the partial sums. In most cases, this will not be possible. We will have to rely on properties of series to establish the convergence or divergence of a given series. Because a series is really a sequence of partial sums, all of the results about sequences can be restated for series. For convenience and for ease of reference, we will state some of these results along with several tests of convergence that are similar to ones for real series. The proofs will be omitted in most cases.
 
-> [!theorem] Theorem 7: Linearity, Conjugation, Real and Imaginary Parts
+<!-- Source label: Theorem 7: Linearity, Conjugation, Real and Imaginary Parts -->
+> [!theorem] Linearity, Conjugation, Real and Imaginary Parts
+> Let the series terms be complex numbers.
+>
 > If $\sum_{n=1}^{\infty} a_{n}$ and $\sum_{n=1}^{\infty} b_{n}$ are convergent series and $\alpha$ and $\beta$ are complex numbers, then
 > (i) $\sum_{n=1}^{\infty}\left(\alpha a_{n}+\beta b_{n}\right)=\alpha \sum_{n=1}^{\infty} a_{n}+\beta \sum_{n=1}^{\infty} b_{n}$;
 > (ii) $\overline{\sum_{n=1}^{\infty} a_{n}}=\sum_{n=1}^{\infty} \overline{a_{n}}$;
@@ -387,7 +448,9 @@
 > Show that the series $\sum_{n=0}^{\infty} \frac{\cos n \theta}{2^{n}}$ is convergent for all $\theta$ and find its sum.
 
 
-**Solution** We immediately recognize $\cos n \theta$ as the real part of $e^{i n \theta}=\left(e^{i \theta}\right)^{n}$, and so the given series is the real part of the geometric series $\sum_{n=0}^{\infty} z^{n}$, where $z=\frac{e^{i f}}{2}$. From Example 3, since $\left|\frac{e^{i \theta}}{2}\right|=\frac{1}{2}<1$, we have
+##### solution
+
+We immediately recognize $\cos n \theta$ as the real part of $e^{i n \theta}=\left(e^{i \theta}\right)^{n}$, and so the given series is the real part of the geometric series $\sum_{n=0}^{\infty} z^{n}$, where $z=\frac{e^{i \theta}}{2}$. From Example 3, since $\left|\frac{e^{i \theta}}{2}\right|=\frac{1}{2}<1$, we have
 $\sum_{n=0}^{\infty}\left(\frac{e^{i \theta}}{2}\right)^{n}=\frac{1}{1-\frac{e^{i \theta}}{2}}=\frac{2}{2-e^{i \theta}}=\frac{2\left(2-e^{-i \theta}\right)}{\left(2-e^{i \theta}\right)\left(2-e^{-i \theta}\right)}=\frac{4-2 \cos \theta+2 i \sin \theta}{5-4 \cos \theta}$.
 Taking real parts and using Theorem 7(iii), we obtain
 
@@ -401,17 +464,28 @@
 
 
 
-> [!figure] Figure 6
-> 
-> ![300](./images/5443c314-b89d-4dd1-b950-bb21550520a5-08_468_500_318_131.jpg)
-> Figure 6 Graph of the series $\sum_{n=0}^{\infty} \frac{\cos n \theta}{2^{n}}$, which converges for all $\theta$ and equals the function $\frac{4-2 \cos \theta}{5-4 \cos \theta}$. (This is a $2 \pi$ periodic function.)
+```scientific-figure
+id: a9c93e76-a157-48db-ba0d-7543ed625cea
+numbered: false
+title: ""
+caption: "**Figure 6.** Graph of the series $\\sum_{n=0}^{\\infty} \\frac{\\cos n \\theta}{2^{n}}$, which converges for all $\\theta$ and equals the function $\\frac{4-2 \\cos \\theta}{5-4 \\cos \\theta}$. (This is a $2 \\pi$ periodic function.)"
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 04 Complex Series/images/5443c314-b89d-4dd1-b950-bb21550520a5-08_468_500_318_131.jpg
+    caption: ""
+```
 
 
 
 The following test of divergence is often useful. Its proof for real series works also with complex series.
 
 
-> [!theorem] Theorem 8: The nth Term Test for Divergence
+<!-- Source label: Theorem 8: The nth Term Test for Divergence -->
+> [!theorem] The nth Term Test for Divergence
+> Let the series terms be complex numbers.
+>
 > If $\sum_{n=1}^{\infty} a_{n}$ is convergent, then $\lim _{n \rightarrow \infty} a_{n}=0$. Equivalently, if either $\lim _{n \rightarrow \infty} a_{n} \neq 0$ or $\lim _{n \rightarrow \infty} a_{n}$ does not exist, then $\sum_{n=1}^{\infty} a_{n}$ diverges.
 
 **Proof** Let $s_{n}=\sum_{m=1}^{n} a_{m}$. If $s_{n} \rightarrow s$, then also $s_{n-1} \rightarrow s$, and so $s_{n}-s_{n-1} \rightarrow s-s=0$. But $s_{n}-s_{n-1}=a_{n}$, and so $a_{n} \rightarrow 0$.
@@ -424,7 +498,10 @@
 
 For $m \geq 1$, the expression $t_{m}=\sum_{n=m+1}^{\infty} a_{n}$ is called a tail of the series $\sum_{n=1}^{\infty} a_{n}$. For fixed $m$, the tail $t_{m}$ is itself a series, which differs from the original series by finitely many terms. So it is obvious that a series converges if and only if all its tails converge. As $m \rightarrow \infty$, we are dropping more and more terms from the tail series; as a result, we have the following useful fact.
 
-> [!proposition] Proposition 1: Tail of Series
+<!-- Source label: Proposition 1: Tail of Series -->
+> [!proposition] Tail of Series
+> Let the series terms be complex numbers.
+>
 > If $\sum_{n=1}^{\infty} a_{n}$ is convergent, then $\lim _{m \rightarrow \infty} \sum_{n=m+1}^{\infty} a_{n}=0$. Hence if a series converges, its tail must go to 0 .
 
 
@@ -442,13 +519,15 @@
 Recall that, for series with real terms, absolute convergence implies convergence. The same is true for complex series.
 
 
-> [!theorem] Theorem 9: Absolute Convergence Implies Convergence
+<!-- Source label: Theorem 9: Absolute Convergence Implies Convergence -->
+> [!theorem] Absolute Convergence Implies Convergence
+> Let the series terms be complex numbers.
+>
 > If $\sum_{n=1}^{\infty} a_{n}$ is absolutely convergent, then it is convergent. In symbols,
-> 
+>
 > $$
 > \sum_{n=1}^{\infty}\left|a_{n}\right|<\infty \Rightarrow \sum_{n=1}^{\infty} a_{n} \text { converges. }
 > $$
-> 
 
 **Proof** Let $s_{n}$ denote the $n$th partial sum of the series $\sum_{j=1}^{\infty} a_{j}$ and $v_{n}$ denote the $n$th partial sum of the convergent series $\sum_{j=1}^{\infty}\left|a_{j}\right|$. By Theorem 6, it is enough to show that the sequence of partial sums, $\left\{s_{n}\right\}$, is a Cauchy sequence. For $n>m \geq 1$, using the triangle inequality, we have
 
@@ -478,7 +557,8 @@
 
 
 
-> [!theorem] Theorem 10: Comparison Test
+<!-- Source label: Theorem 10: Comparison Test -->
+> [!theorem] Comparison Test
 > Suppose that $a_{n}$ are complex numbers, $b_{n}$ are real numbers, $\left|a_{n}\right| \leq b_{n}$ for all $n \geq n_{0}$, and $\sum_{n=1}^{\infty} b_{n}$ is convergent. Then $\sum_{n=1}^{\infty} a_{n}$ is absolutely convergent.
 
 **Proof** By the comparison test for real series, we have that $\sum_{n=1}^{\infty}\left|a_{n}\right|$ is convergent. By Theorem 9, it follows that $\sum_{n=1}^{1} a_{n}$ is convergent.
@@ -503,13 +583,14 @@
 
 
 
-> [!theorem] Theorem 11: Ratio Test
+<!-- Source label: Theorem 11: Ratio Test -->
+> [!theorem] Ratio Test
 > Suppose that
-> 
+>
 > $$
 > \rho=\lim _{n \rightarrow \infty}\left|\frac{a_{n+1}}{a_{n}}\right|
 > $$
-> 
+>
 > exists or is infinite. Then the complex series $\sum_{n=1}^{\infty} a_{n}$ of nonzero terms converges absolutely if $\rho<1$ and diverges if $\rho>1$. If $\rho=1$ the test is inconclusive.
 
 
@@ -530,14 +611,14 @@
 
 
 
-> [!theorem] Theorem 12: Root Test
+<!-- Source label: Theorem 12: Root Test -->
+> [!theorem] Root Test
 > Suppose that
-> 
-> 
-> $$
-> \rho=\lim _{n \rightarrow \infty}\left|a_{n}\right|^{1 / n} \tag{8}
-> $$
-> 
+>
+> $$
+> \rho=\lim _{n \rightarrow \infty}\left|a_{n}\right|^{1 / n} 
+> $$
+>
 > either exists or is infinite. Then the complex series $\sum_{n=1}^{\infty} a_{n}$ converges absolutely if $\rho<1$ and diverges if $\rho>1$. If $\rho=1$ the test is inconclusive.
 
 In general, the ratio test is easier to apply than the root test. But there are situations that call naturally for the root test. Here is an example.
@@ -548,7 +629,9 @@
 
 
 
-**Solution** The presence of the exponent $n$ in the terms suggests using the root test. We have
+##### solution
+
+The presence of the exponent $n$ in the terms suggests using the root test. We have
 
 $$
 \rho=\lim _{n \rightarrow \infty}\left|\frac{z^{n}}{(n+1)^{n}}\right|^{\frac{1}{n}}=\lim _{n \rightarrow \infty} \frac{|z|}{n+1}=0
@@ -562,7 +645,10 @@
 
 Another well-known consequence of the completeness property of real numbers is that every bounded monotonic sequence (increasing or decreasing) converges. Since the partial sums of a series with nonnegative terms are increasing, we conclude that if these partial sums are bounded, then the series is convergent. This leads to the following result, which is not particularly useful as a test of convergence but will be required in later proofs.
 
-> [!theorem] Theorem 13: Bounded Partial Sums
+<!-- Source label: Theorem 13: Bounded Partial Sums -->
+> [!theorem] Bounded Partial Sums
+> Let the series terms be complex numbers.
+>
 > Suppose that there is a positive number $M>0$ such that $\sum_{n=1}^{N}\left|a_{n}\right| \leq M$ for all $N$. Then the series $\sum_{n=1}^{\infty} a_{n}$ is absolutely convergent.
 
 
@@ -578,7 +664,10 @@
 A rearrangement of a given complex series $\sum_{n=1}^{\infty} a_{n}$ is a series of the form $\sum_{n=1}^{\infty} a_{\phi(n)}$, where $\phi$ is a one-to-one mapping of the indexing set $\{1,2,3, \ldots\}$ onto itself. For example, a rearrangement of $a_{1}+a_{2}+a_{3}+\cdots$ could be something like $a_{4}+a_{1}+a_{6}+\cdots$, where each $a_{n}$ must appear exactly once in the expression.
 
 
-> [!theorem] Theorem 14: Rearrangements
+<!-- Source label: Theorem 14: Rearrangements -->
+> [!theorem] Rearrangements
+> Let the series terms be complex numbers.
+>
 > If $\sum_{n=1}^{\infty} a_{n}$ is absolutely convergent, then every rearrangement is absolutely convergent and converges to the same limit.
 
 **Proof** For $m \geq 1$, we have $\sum_{n=1}^{m}\left|a_{\phi(n)}\right| \leq \sum_{n=1}^{\infty}\left|a_{n}\right|<\infty$. Hence the partial sums of the series $\sum_{n=0}^{m}\left|a_{\phi(n)}\right|$ are bounded and so they converge by Theorem 13. Thus any rearrangement converges absolutely. We next show that the rearranged series will still converge to $s=\sum_{n=1}^{\infty} a_{n}$. Let $\sigma(m)=\max _{n \leq m} \phi(n)$. Consider the expressions $\sum_{n=1}^{m} a_{\phi(n)}$ and $\sum_{n=1}^{\sigma(m)} a_{n}$. The first is a sum of the first $m$ terms of the rearranged series; the second is a sum of the first $\sigma(m)$ terms in the original series, which will include each term from the first expression. The difference between the expressions is a finite sum of terms that come in the rearranged series after the term $a_{\phi(m)}$. Thus we can derive
@@ -606,10 +695,18 @@
 The term $c_{n}$ in the Cauchy product is gotten by summing along the diagonal $j+k=n$ as shown in _Figure 7_. 
 
 
-> [!figure] Figure 7
-> 
-> ![300](./images/5443c314-b89d-4dd1-b950-bb21550520a5-12_454_716_511_773.jpg)
-> Figure 7 The $n$th term of a Cauchy product:
+```scientific-figure
+id: 471cdf15-6411-4a21-a2a2-d8ee4b25f8a0
+numbered: false
+title: ""
+caption: "**Figure 7.** The $n$th term of a Cauchy product:"
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 04 Complex Series/images/5443c314-b89d-4dd1-b950-bb21550520a5-12_454_716_511_773.jpg
+    caption: ""
+```
 $c_{n}=a_{0} b_{n}+a_{1} b_{n-1}+\cdots+ a_{n-1} b_{1}+a_{n} b_{0}=\sum_{j=0}^{n} a_{j} b_{n-j}$. By summing all the $c_{n}$ 's, you will pick up all the terms of form $a_{j} b_{k}$, but in a very special order: $a_{0} b_{0}+a_{1} b_{0}+a_{1} b_{1}+$ ... .
 
 
@@ -618,14 +715,15 @@
 
 
 
-> [!theorem] Theorem 15: Cauchy Products
-> Suppose that $\sum_{n=0}^{\infty} a_{n}$ and $\sum_{n=0}^{\infty} b_{n}$ are absolutely convergent. Then their Cauchy product $\sum_{n=0}^{\infty} c_{n}$, where $c_{n}$ is as in (9), is absolutely convergent and we have
-> (10)
-> 
+<!-- Source label: Theorem 15: Cauchy Products -->
+> [!theorem] Cauchy Products
+> Let the series terms be complex numbers.
+>
+> Suppose that $\sum_{n=0}^{\infty} a_{n}$ and $\sum_{n=0}^{\infty} b_{n}$ are absolutely convergent. Then their Cauchy product $\sum_{n=0}^{\infty} c_{n}$, where $c_n=\sum_{k=0}^{n}a_k b_{n-k}$, is absolutely convergent and we have
+>
 > $$
 > \sum_{n=0}^{\infty} c_{n}=\left(\sum_{n=0}^{\infty} a_{n}\right)\left(\sum_{n=0}^{\infty} b_{n}\right) .
 > $$
-> 
 
 **Proof** First we will show that the Cauchy product is absolutely convergent, then we will show that it converges to the right limit. For the first part, observe that
 
@@ -650,7 +748,9 @@
 > Show that $e^{z_{1}} e^{z_{2}}=e^{z_{1}+z_{2}}$.
 
 
-**Solution** We have $e^{z_{1}}=\sum_{n=0}^{\infty} \frac{z_{1}^{n}}{n!}$ and $e^{z_{2}}=\sum_{n=0}^{\infty} \frac{z_{2}^{n}}{n!}$, where both series converge absolutely by Example 7. By Theorem 15, we can form the Cauchy product of the two series and get $e^{z_{1}} e^{z_{2}}=\sum_{n=0}^{\infty} c_{n}$, where according to (9)
+##### solution
+
+We have $e^{z_{1}}=\sum_{n=0}^{\infty} \frac{z_{1}^{n}}{n!}$ and $e^{z_{2}}=\sum_{n=0}^{\infty} \frac{z_{2}^{n}}{n!}$, where both series converge absolutely by Example 7. By Theorem 15, we can form the Cauchy product of the two series and get $e^{z_{1}} e^{z_{2}}=\sum_{n=0}^{\infty} c_{n}$, where according to (9)
 
 $$
 c_{n}=\sum_{j=0}^{n} \frac{z_{1}^{j}}{j!} \frac{z_{2}^{n-j}}{(n-j)!}=\frac{1}{n!} \overbrace{\sum_{j=0}^{n} \frac{n!}{j!(n-j)!} z_{1}^{j} z_{2}^{n-j}}^{\left(z_{1}+z_{2}\right)^{n}}=\frac{\left(z_{1}+z_{2}\right)^{n}}{n!}

`````
