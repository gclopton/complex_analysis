
# Editorial records

Reading note: 5.6 Summing Series by Residues.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Callout 215: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!lemma] Cotangent Bounds on Half-Integer Square Contours
> Let $N$ be a positive integer and $\Gamma_N$ be the positively oriented boundary of the square $|\operatorname{Re}z|\leq N+\tfrac12$, $|\operatorname{Im}z|\leq N+\tfrac12$. For all $z$ on $\Gamma_N$, we have
>
> $$
> |\cot (\pi z)| \leq 2 .
> $$
>
> Moreover, if $f(z)=\frac{p(z)}{q(z)}$ is a rational function with degree $q(z) \geq 2+$ degree $p(z)$, then
>
> $$
> \lim _{N \rightarrow \infty}\left|\int_{\Gamma_N} \frac{p(z)}{q(z)} \cot (\pi z) d z\right|=0 .
> $$
````
### After

````text
> [!lemma] Bounds for the Cotangent
> Let $N$ be a positive integer and $\Gamma_N$ be the positively oriented boundary of the square $|\operatorname{Re}z|\leq N+\tfrac12$, $|\operatorname{Im}z|\leq N+\tfrac12$. For all $z$ on $\Gamma_N$, we have
>
> $$
> |\cot (\pi z)| \leq 2 .
> $$
>
> Moreover, if $f(z)=\frac{p(z)}{q(z)}$ is a rational function with degree $q(z) \geq 2+$ degree $p(z)$, then
>
> $$
> \lim _{N \rightarrow \infty}\left|\int_{\Gamma_N} \frac{p(z)}{q(z)} \cot (\pi z) d z\right|=0 .
> $$
````

## 2. Callout 216: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!proposition] Summation of Rational Series by Cotangent Residues
> Suppose that $f(z)=\frac{p(z)}{q(z)}$ is a rational function with degree $q(z) \geq 2+$ degree $p(z)$. Suppose further that $f$ has no poles at the integers. Then
>
> $$
> \sum_{k=-\infty}^{\infty} f(k)=-\pi \sum_j \operatorname{Res}\left(f(z) \cot (\pi z), z_j\right)
> $$
>
> where the (finite) sum on the right runs over all the poles $z_j$ of $f(z)$.
````
### After

````text
> [!proposition] Summing Infinite Series by Residues
> Suppose that $f(z)=\frac{p(z)}{q(z)}$ is a rational function with degree $q(z) \geq 2+$ degree $p(z)$. Suppose further that $f$ has no poles at the integers. Then
>
> $$
> \sum_{k=-\infty}^{\infty} f(k)=-\pi \sum_j \operatorname{Res}\left(f(z) \cot (\pi z), z_j\right)
> $$
>
> where the (finite) sum on the right runs over all the poles $z_j$ of $f(z)$.
````

## Source-to-current comparison

Source: /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 05 Residue Theory/5.6 Summing Series by Residues.md

This exact comparison preserves the full change evidence, including formatting, OCR corrections, restored source wording, and required standalone context. The entries above explain the recovery edits. The comparison is not a claim that every difference is a correction; component serialization, callout wrapping, and printed labels outside callouts are formatting.

`````diff
--- /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 05 Residue Theory/5.6 Summing Series by Residues.md
+++ /Users/gradyclopton/ObsidianVaults/complex_analysis/Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 05 Residue Theory/5.6 Summing Series by Residues.md
@@ -22,31 +22,34 @@
 
 
 
-> [!figure]
-> 
-> ![](Pasted%20image%2020260421190328.png)
-> Figure 1 Square contour $\Gamma_N$ for integers $N \geq 1$.
-
-
-
-> [!lemma] Lemma 1: Bounds for the Cotangent
-> 
-> Let $N$ be a positive integer and $\Gamma_N$ be as in Figure 1. For all $z$ on $\Gamma_N$, we have
-> (2)
-> 
+```scientific-figure
+id: fc9525d1-0415-4f47-b268-bbd89131d737
+numbered: false
+title: ""
+caption: "**Figure 1.** Square contour $\\Gamma_N$ for integers $N \\geq 1$."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 05 Residue Theory/images/Pasted image 20260421190328.png
+    caption: ""
+```
+
+
+
+<!-- Source label: Lemma 1: Bounds for the Cotangent -->
+> [!lemma] Bounds for the Cotangent
+> Let $N$ be a positive integer and $\Gamma_N$ be the positively oriented boundary of the square $|\operatorname{Re}z|\leq N+\tfrac12$, $|\operatorname{Im}z|\leq N+\tfrac12$. For all $z$ on $\Gamma_N$, we have
+>
 > $$
 > |\cot (\pi z)| \leq 2 .
 > $$
-> 
-> 
+>
 > Moreover, if $f(z)=\frac{p(z)}{q(z)}$ is a rational function with degree $q(z) \geq 2+$ degree $p(z)$, then
-> (3)
-> 
+>
 > $$
 > \lim _{N \rightarrow \infty}\left|\int_{\Gamma_N} \frac{p(z)}{q(z)} \cot (\pi z) d z\right|=0 .
 > $$
-> 
-> 
 
 
 
@@ -87,15 +90,14 @@
 
 
 
-> [!proposition] Proposition 1: Summing Infinite Series by Residues
-> 
+<!-- Source label: Proposition 1: Summing Infinite Series by Residues -->
+> [!proposition] Summing Infinite Series by Residues
 > Suppose that $f(z)=\frac{p(z)}{q(z)}$ is a rational function with degree $q(z) \geq 2+$ degree $p(z)$. Suppose further that $f$ has no poles at the integers. Then
-> (4)
-> 
+>
 > $$
 > \sum_{k=-\infty}^{\infty} f(k)=-\pi \sum_j \operatorname{Res}\left(f(z) \cot (\pi z), z_j\right)
 > $$
-> 
+>
 > where the (finite) sum on the right runs over all the poles $z_j$ of $f(z)$.
 
 
@@ -120,7 +122,9 @@
 
 
 
-**Solution** We apply (4) with $f(z)=\frac{1}{z^2+1}$ and find
+##### solution
+
+We apply (4) with $f(z)=\frac{1}{z^2+1}$ and find
 
 $$
 \sum_{k=-\infty}^{\infty} \frac{1}{k^2+1}=-\pi \sum_j \operatorname{Res}\left(\frac{1}{z^2+1} \cot (\pi z), z_j\right)

`````
