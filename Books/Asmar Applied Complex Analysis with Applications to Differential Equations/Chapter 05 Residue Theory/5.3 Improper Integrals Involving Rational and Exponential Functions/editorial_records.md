
# Editorial records

Reading note: 5.3 Improper Integrals Involving Rational and Exponential Functions.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Callout 209: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!proposition] Absolute Convergence and Comparison for Improper Integrals
> Let $\int_{A}^{B} f(x) d x$ represent an improper integral of a locally integrable complex-valued function, where $A=-\infty$ or $B=\infty$.
> (i) If $\int_{A}^{B}|f(x)| d x$ is convergent, then $\int_{A}^{B} f(x) d x$ is convergent and we have $\left|\int_{A}^{B} f(x) d x\right| \leq \int_{A}^{B}|f(x)| d x$.
> (ii) If $|f(x)| \leq g(x)$ for all $A<x<B$ and $\int_{A}^{B} g(x) d x$ is convergent, then $\int_{A}^{B} f(x) d x$ is convergent and we have $\left|\int_{A}^{B} f(x) d x\right| \leq \int_{A}^{B} g(x) d x$.
````
### After

````text
> [!proposition] Inequalities for Improper Integrals
> Let $\int_{A}^{B} f(x) d x$ represent an improper integral of a locally integrable complex-valued function, where $A=-\infty$ or $B=\infty$.
> (i) If $\int_{A}^{B}|f(x)| d x$ is convergent, then $\int_{A}^{B} f(x) d x$ is convergent and we have $\left|\int_{A}^{B} f(x) d x\right| \leq \int_{A}^{B}|f(x)| d x$.
> (ii) If $|f(x)| \leq g(x)$ for all $A<x<B$ and $\int_{A}^{B} g(x) d x$ is convergent, then $\int_{A}^{B} f(x) d x$ is convergent and we have $\left|\int_{A}^{B} f(x) d x\right| \leq \int_{A}^{B} g(x) d x$.
````

## 2. Callout 210: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!proposition] Rational Integrals by Upper-Half-Plane Residues
> Let $f(x)=\frac{p(x)}{q(x)}$ be a rational function with degree $q(x) \geq 2+$ degree $p(x)$, and let $\sigma_{R}$ denote an arc of the circle centered at 0 with radius $R>0$. Then
>
> $$
> \lim _{R \rightarrow \infty}\left|\int_{\sigma_{R}} \frac{p(z)}{q(z)} d z\right|=0
> $$
>
> Moreover, if $q(x)$ has no real roots and $z_{1}, z_{2}, \ldots, z_{N}$ denote all the poles of $\frac{p(z)}{q(z)}$ in the upper half-plane, then
>
> $$
> \int_{-\infty}^{\infty} \frac{p(x)}{q(x)} d x=2 \pi i \sum_{j=1}^{N} \operatorname{Res}\left(\frac{p(z)}{q(z)}, z_{j}\right)
> $$
````
### After

````text
> [!proposition] Integrals of Rational Functions
> Let $f(x)=\frac{p(x)}{q(x)}$ be a rational function with degree $q(x) \geq 2+$ degree $p(x)$, and let $\sigma_{R}$ denote an arc of the circle centered at 0 with radius $R>0$. Then
>
> $$
> \lim _{R \rightarrow \infty}\left|\int_{\sigma_{R}} \frac{p(z)}{q(z)} d z\right|=0
> $$
>
> Moreover, if $q(x)$ has no real roots and $z_{1}, z_{2}, \ldots, z_{N}$ denote all the poles of $\frac{p(z)}{q(z)}$ in the upper half-plane, then
>
> $$
> \int_{-\infty}^{\infty} \frac{p(x)}{q(x)} d x=2 \pi i \sum_{j=1}^{N} \operatorname{Res}\left(\frac{p(z)}{q(z)}, z_{j}\right)
> $$
````

## Source-to-current comparison

Source: /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 05 Residue Theory/5.3 Improper Integrals Involving Rational and Exponential Functions.md

This exact comparison preserves the full change evidence, including formatting, OCR corrections, restored source wording, and required standalone context. The entries above explain the recovery edits. The comparison is not a claim that every difference is a correction; component serialization, callout wrapping, and printed labels outside callouts are formatting.

`````diff
--- /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 05 Residue Theory/5.3 Improper Integrals Involving Rational and Exponential Functions.md
+++ /Users/gradyclopton/ObsidianVaults/complex_analysis/Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 05 Residue Theory/5.3 Improper Integrals Involving Rational and Exponential Functions.md
@@ -31,10 +31,18 @@
 
 
 
-> [!figure] Figure 1
-> 
-> ![[Pasted image 20260403153659.png]]
-> Figure 1 Splitting an improper integral over the line.
+```scientific-figure
+id: 7c1e30b3-6d2d-4d1f-9bb8-f8ff0ffc5a76
+numbered: false
+title: ""
+caption: "**Figure 1.** Splitting an improper integral over the line."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Pasted image 20260403153659.png
+    caption: ""
+```
 
 
 
@@ -47,11 +55,18 @@
 
 
 
-> [!figure]
-> 
-> ![300](./images/b1ad9866-c636-4d3b-85cb-e1f2bdb2e560-16_466_544_1444_124.jpg)
-> 
-> _Figure 2_ The Cauchy principal value of the integral.
+```scientific-figure
+id: 4818f00b-8c21-40f6-9c0f-fe10b57442d3
+numbered: false
+title: ""
+caption: "**Figure 2.** The Cauchy principal value of the integral."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 05 Residue Theory/images/b1ad9866-c636-4d3b-85cb-e1f2bdb2e560-16_466_544_1444_124.jpg
+    caption: ""
+```
 
 
 
@@ -80,8 +95,9 @@
 How can we know if an integral is convergent? We can use the following comparison test.
 
 
+<!-- Source label: Inequalities for Improper Integrals -->
 > [!proposition] Inequalities for Improper Integrals
-> Let $\int_{A}^{B} f(x) d x$ represent an improper integral as in (1), where $A=-\infty$ or $B=\infty$.
+> Let $\int_{A}^{B} f(x) d x$ represent an improper integral of a locally integrable complex-valued function, where $A=-\infty$ or $B=\infty$.
 > (i) If $\int_{A}^{B}|f(x)| d x$ is convergent, then $\int_{A}^{B} f(x) d x$ is convergent and we have $\left|\int_{A}^{B} f(x) d x\right| \leq \int_{A}^{B}|f(x)| d x$.
 > (ii) If $|f(x)| \leq g(x)$ for all $A<x<B$ and $\int_{A}^{B} g(x) d x$ is convergent, then $\int_{A}^{B} f(x) d x$ is convergent and we have $\left|\int_{A}^{B} f(x) d x\right| \leq \int_{A}^{B} g(x) d x$.
 
@@ -109,7 +125,9 @@
 > 
 > 
 
-**solution** To highlight the main ideas, we present the **solution** in basic steps.
+##### solution
+
+To highlight the main ideas, we present the **solution** in basic steps.
 Step 1: Show that the improper integral is convergent. Because the integrand is continuous on the real line, it is enough to show that the integral outside a
 
 
@@ -130,10 +148,18 @@
 
 
 
-> [!figure] Figure 3
-> 
-> ![300](./images/b1ad9866-c636-4d3b-85cb-e1f2bdb2e560-18_488_538_920_117.jpg)
-> Figure 3 The path and poles for the contour integral in Example 1.
+```scientific-figure
+id: 60b04aef-9ca2-40e4-9307-6e9b31dbbbab
+numbered: false
+title: ""
+caption: "**Figure 3.** The path and poles for the contour integral in Example 1."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 05 Residue Theory/images/b1ad9866-c636-4d3b-85cb-e1f2bdb2e560-18_488_538_920_117.jpg
+    caption: ""
+```
 
 
 
@@ -197,10 +223,18 @@
 In Example 1, we could have used the contour $\gamma_R^{\prime}$ in the lower half-plane in _Figure 4_. In this case, it is easiest to take the orientation of $\gamma_R^{\prime}$ to be negative in order to coincide with the orientation of the interval $[-R, R]$.
 
 
-> [!figure] Figure 4
-> 
-> ![300](./images/b1ad9866-c636-4d3b-85cb-e1f2bdb2e560-19_446_364_921_9.jpg)
-> Figure 4 An alternative path the integral in Example 1.
+```scientific-figure
+id: 5d461d4e-9fce-49a9-a4c0-46e5fcb16fc6
+numbered: false
+title: ""
+caption: "**Figure 4.** An alternative path the integral in Example 1."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 05 Residue Theory/images/b1ad9866-c636-4d3b-85cb-e1f2bdb2e560-19_446_364_921_9.jpg
+    caption: ""
+```
 
 
 The five steps that we used in the **solution** of Example 1 are applicable in a general situation described as follows.
@@ -209,20 +243,19 @@
 
 
 
+<!-- Source label: Integrals of Rational Functions -->
 > [!proposition] Integrals of Rational Functions
 > Let $f(x)=\frac{p(x)}{q(x)}$ be a rational function with degree $q(x) \geq 2+$ degree $p(x)$, and let $\sigma_{R}$ denote an arc of the circle centered at 0 with radius $R>0$. Then
-> 
+>
 > $$
 > \lim _{R \rightarrow \infty}\left|\int_{\sigma_{R}} \frac{p(z)}{q(z)} d z\right|=0
 > $$
-> 
+>
 > Moreover, if $q(x)$ has no real roots and $z_{1}, z_{2}, \ldots, z_{N}$ denote all the poles of $\frac{p(z)}{q(z)}$ in the upper half-plane, then
-> 
+>
 > $$
 > \int_{-\infty}^{\infty} \frac{p(x)}{q(x)} d x=2 \pi i \sum_{j=1}^{N} \operatorname{Res}\left(\frac{p(z)}{q(z)}, z_{j}\right)
 > $$
-> 
-> 
 
 The proof of the proposition is very similar to the **solution** of Example 1. We will relegate it to the exercises. Here is a straightforward application.
 
@@ -236,7 +269,9 @@
 > 
 > 
 
-**solution** The integrand satisfies the two conditions of Proposition 2: degree $q(x)= 4 \geq 2+$ degree $p(x)=2$, and the denominator $q(x)=\left(x^{2}+1\right)\left(x^{2}+4\right)$ has no real roots. So we may apply (8). We have
+##### solution
+
+The integrand satisfies the two conditions of Proposition 2: degree $q(x)= 4 \geq 2+$ degree $p(x)=2$, and the denominator $q(x)=\left(x^{2}+1\right)\left(x^{2}+4\right)$ has no real roots. So we may apply (8). We have
 
 $$
 \left(z^{2}+1\right)\left(z^{2}+4\right)=(z+i)(z-i)(z+2 i)(z-2 i)
@@ -246,10 +281,18 @@
 
 
 
-> [!figure] Figure 5
-> 
-> ![300](./images/b1ad9866-c636-4d3b-85cb-e1f2bdb2e560-20_489_539_285_100.jpg)
-> Figure 5 The path and poles for the contour integral in Example 2.
+```scientific-figure
+id: 272ad173-d7f4-467a-8fa2-2e1b6552299e
+numbered: false
+title: ""
+caption: "**Figure 5.** The path and poles for the contour integral in Example 2."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 05 Residue Theory/images/b1ad9866-c636-4d3b-85cb-e1f2bdb2e560-20_489_539_285_100.jpg
+    caption: ""
+```
 
 
 
@@ -305,7 +348,9 @@
 
 
 
-**solution** Step 1: Show that the integral converges. The integrand is continuous, so it is enough to show that it has a convergent integral on $[1, \infty)$. We have $\frac{1}{x^{\alpha}+1} \leq \frac{1}{x^{\alpha}}$, where the latter has a convergent integral over $[1, \infty)$.
+##### solution
+
+Step 1: Show that the integral converges. The integrand is continuous, so it is enough to show that it has a convergent integral on $[1, \infty)$. We have $\frac{1}{x^{\alpha}+1} \leq \frac{1}{x^{\alpha}}$, where the latter has a convergent integral over $[1, \infty)$.
 Step 2: Apply the substitution $x=e^{t}$. Let $x=e^{t}, d x=e^{t} d t$, and note that as $x$ varies from 0 to $\infty, t$ varies from $-\infty$ to $\infty$, and so
 
 $$
@@ -322,10 +367,18 @@
 
 
 
-> [!figure] Figure 6
-> 
-> ![300](./images/b1ad9866-c636-4d3b-85cb-e1f2bdb2e560-21_485_469_1018_57.jpg)
-> Figure 6 The path and poles for the contour integral in Example 3.
+```scientific-figure
+id: 6ae23719-6475-40c7-9a75-5d0d406c2f95
+numbered: false
+title: ""
+caption: "**Figure 6.** The path and poles for the contour integral in Example 3."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 05 Residue Theory/images/b1ad9866-c636-4d3b-85cb-e1f2bdb2e560-21_485_469_1018_57.jpg
+    caption: ""
+```
 
 
 
@@ -420,10 +473,18 @@
 
 
 
-> [!figure] Figure 7
-> 
-> ![300](./images/b1ad9866-c636-4d3b-85cb-e1f2bdb2e560-22_495_520_1498_141.jpg)
-> Figure 7 Splitting an improper integral.
+```scientific-figure
+id: a299de3a-8fd6-4467-9927-3354f8a4a3d2
+numbered: false
+title: ""
+caption: "**Figure 7.** Splitting an improper integral."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 05 Residue Theory/images/b1ad9866-c636-4d3b-85cb-e1f2bdb2e560-22_495_520_1498_141.jpg
+    caption: ""
+```
 
 
 
@@ -441,7 +502,9 @@
 > $$
 > 
 
-**solution** Let $x=e^{t}, \ln x=t, d x=e^{t} d t$. This transforms the integral into
+##### solution
+
+Let $x=e^{t}, \ln x=t, d x=e^{t} d t$. This transforms the integral into
 
 $$
 \int_{-\infty}^{\infty} \frac{t}{e^{4 t}+1} e^{t} d t=\int_{-\infty}^{\infty} \frac{x e^{x}}{e^{4 x}+1} d x
@@ -451,10 +514,18 @@
 
 
 
-> [!figure] Figure 8
-> 
-> ![300](./images/b1ad9866-c636-4d3b-85cb-e1f2bdb2e560-23_482_465_246_37.jpg)
-> Figure 8 The path and poles for the contour integral in Example 4.
+```scientific-figure
+id: 3224a74d-281b-47fb-9c6b-ba36650875e6
+numbered: false
+title: ""
+caption: "**Figure 8.** The path and poles for the contour integral in Example 4."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 05 Residue Theory/images/b1ad9866-c636-4d3b-85cb-e1f2bdb2e560-23_482_465_246_37.jpg
+    caption: ""
+```
 
 
 
@@ -567,10 +638,18 @@
 > **(Hint: $I_{\gamma_{R}}=I_{1}+I_{2}+I_{3} ; I_{3}=-e^{i \frac{2 \pi}{3}} I_{1} ;$ and $I_{2} \rightarrow 0$ as $R \rightarrow \infty$.)**
 > 
 > 
-> > [!figure] Figure 9
-> > 
-> > ![300](./images/b1ad9866-c636-4d3b-85cb-e1f2bdb2e560-25_510_466_311_40.jpg)
-> > Figure 9 The path and poles for the contour integral in problem 21.
+> ```scientific-figure
+> id: 6815078a-76da-477b-9617-45b96d52a436
+> numbered: false
+> title: ""
+> caption: "**Figure 9.** The path and poles for the contour integral in problem 21."
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 05 Residue Theory/images/b1ad9866-c636-4d3b-85cb-e1f2bdb2e560-25_510_466_311_40.jpg
+>     caption: ""
+> ```
 > 
 > 
 

`````
