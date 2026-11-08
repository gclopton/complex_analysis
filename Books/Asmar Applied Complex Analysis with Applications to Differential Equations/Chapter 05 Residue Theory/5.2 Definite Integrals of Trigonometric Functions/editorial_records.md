
# Editorial records

Reading note: 5.2 Definite Integrals of Trigonometric Functions.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

No recovery content changes were needed in this note. Existing genuine corrections and formatting were retained.

## Source-to-current comparison

Source: /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 05 Residue Theory/5.2 Definite Integrals of Trigonometric Functions.md

This exact comparison preserves the full change evidence, including formatting, OCR corrections, restored source wording, and required standalone context. The entries above explain the recovery edits. The comparison is not a claim that every difference is a correction; component serialization, callout wrapping, and printed labels outside callouts are formatting.

`````diff
--- /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 05 Residue Theory/5.2 Definite Integrals of Trigonometric Functions.md
+++ /Users/gradyclopton/ObsidianVaults/complex_analysis/Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 05 Residue Theory/5.2 Definite Integrals of Trigonometric Functions.md
@@ -39,31 +39,41 @@
 
 As $\theta$ varies in the interval $[0,2 \pi]$, the complex number $z=e^{i \theta}$ traces $C_{1}(0)$,
 
-> [!equation] 
-> 
+<!-- Source label:  -->
+> [!equation] Sine and Cosine Under the Unit-Circle Substitution
+> Under the parametrization $z=e^{i\theta}$, with real $\theta$,
+>
 > $$
 > \cos \theta=\frac{1}{2}\left(z+\frac{1}{z}\right), \quad \text { and } \quad \sin \theta=\frac{1}{2 i}\left(z-\frac{1}{z}\right)
 > $$
-> 
 
 This is represented graphically in _Figure 1_. 
 
 
-> [!figure] Figure 1
-> 
-> ![300](./images/b1ad9866-c636-4d3b-85cb-e1f2bdb2e560-11_499_476_1849_43.jpg)
-> Figure 1 Constructing $\cos \theta$ and $\sin \theta$.
+```scientific-figure
+id: e78cb27f-cd12-423a-a46f-abf78b9fc0f3
+numbered: false
+title: ""
+caption: "**Figure 1.** Constructing $\\cos \\theta$ and $\\sin \\theta$."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 05 Residue Theory/images/b1ad9866-c636-4d3b-85cb-e1f2bdb2e560-11_499_476_1849_43.jpg
+    caption: ""
+```
 
 
 
 Also, from $z=e^{i \theta}$, we have $d z=i e^{i \theta} d \theta=i z d \theta$ or
 
-> [!equation]
-> 
+<!-- Source label:  -->
+> [!equation] Differential Under the Unit-Circle Substitution
+> Under the parametrization $z=e^{i\theta}$, with real $\theta$,
+>
 > $$
 > -i \frac{d z}{z}=d \theta
 > $$
-> 
 
 With (3) and (4) in hand, we can now consider some examples.
 
@@ -78,15 +88,25 @@
 
 
 
-> [!figure] Figure 2
-> 
-> ![300](./images/b1ad9866-c636-4d3b-85cb-e1f2bdb2e560-12_502_530_353_72.jpg)
-> Figure 2 The definite integral in Example 1.
-
-
-
-
-**Solution** Let $z=e^{i \theta}$. As $\theta$ varies from 0 to $2 \pi, z$ traces $C_{1}(0)$, the unit circle in the positive direction. Using the substitutions (3) and (4), we transform the given integral into a path integral as follows
+```scientific-figure
+id: 85ca414b-0e54-4e08-93f7-7637c3826722
+numbered: false
+title: ""
+caption: "**Figure 2.** The definite integral in Example 1."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 05 Residue Theory/images/b1ad9866-c636-4d3b-85cb-e1f2bdb2e560-12_502_530_353_72.jpg
+    caption: ""
+```
+
+
+
+
+##### solution
+
+Let $z=e^{i \theta}$. As $\theta$ varies from 0 to $2 \pi, z$ traces $C_{1}(0)$, the unit circle in the positive direction. Using the substitutions (3) and (4), we transform the given integral into a path integral as follows
 
 $$
 \int_{0}^{2 \pi} \frac{d \theta}{10+8 \cos \theta}=\int_{C_{1}(0)} \frac{-i \frac{d z}{z}}{10+\frac{8}{2}\left(z+\frac{1}{z}\right)}=-i \int_{C_{1}(0)} \frac{d z}{4 z^{2}+10 z+4}
@@ -101,10 +121,18 @@
 and get $z=-2$ and $z=-\frac{1}{2}$ (see _Figure 3_). So the only singularity inside the unit disk is a simple pole at $-\frac{1}{2}$. 
 
 
-> [!figure] Figure 3
-> 
-> ![300](./images/b1ad9866-c636-4d3b-85cb-e1f2bdb2e560-12_493_540_1314_76.jpg)
-> Figure 3 The path and poles for the contour integral in Example 1.
+```scientific-figure
+id: 9b469e13-171f-4991-b255-39d60e287f14
+numbered: false
+title: ""
+caption: "**Figure 3.** The path and poles for the contour integral in Example 1."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 05 Residue Theory/images/b1ad9866-c636-4d3b-85cb-e1f2bdb2e560-12_493_540_1314_76.jpg
+    caption: ""
+```
 
 
 
@@ -150,12 +178,13 @@
 So
 
 
-> [!equation]
-> 
-> $$
-> \cos n \theta=\frac{1}{2}\left(z^{n}+\frac{1}{z^{n}}\right) \text { and } \sin n \theta=\frac{1}{2 i}\left(z^{n}-\frac{1}{z^{n}}\right) \tag{3}
-> $$
-> 
+<!-- Source label:  -->
+> [!equation] Trigonometric Multiples Under the Unit-Circle Substitution
+> Let $z=e^{i\theta}$ with real $\theta$ and integer $n$.
+>
+> $$
+> \cos n \theta=\frac{1}{2}\left(z^{n}+\frac{1}{z^{n}}\right) \text { and } \sin n \theta=\frac{1}{2 i}\left(z^{n}-\frac{1}{z^{n}}\right) 
+> $$
 
 As we now illustrate, these formulas are useful when evaluating integrals involving $\cos n \theta$ and $\sin n \theta$.
 
@@ -173,16 +202,26 @@
 > $$
 > 
 > 
-> > [!figure] Figure 4
-> > 
-> > ![300](./images/b1ad9866-c636-4d3b-85cb-e1f2bdb2e560-13_506_463_270_68.jpg)
-> > Figure 4 The definite integral in Example 2.
-> 
-> 
-
-
-
-**Solution** Use (3), (4), and (5) with $n=2$, and get
+> ```scientific-figure
+> id: 851510f5-d8e0-430f-b9ce-c710b1935a9a
+> numbered: false
+> title: ""
+> caption: "**Figure 4.** The definite integral in Example 2."
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 05 Residue Theory/images/b1ad9866-c636-4d3b-85cb-e1f2bdb2e560-13_506_463_270_68.jpg
+>     caption: ""
+> ```
+> 
+> 
+
+
+
+##### solution
+
+Use (3), (4), and (5) with $n=2$, and get
 
 $$
 \int_{0}^{2 \pi} \frac{\cos 2 \theta}{2+\cos \theta} d \theta=-i \int_{C_{1}(0)} \frac{\frac{1}{2}\left(z^{2}+\frac{1}{z^{2}}\right)}{2+\frac{1}{2}\left(z+\frac{1}{z}\right)} \frac{d z}{z}=-i \int_{C_{1}(0)} \frac{z^{4}+1}{z^{2}\left(z^{2}+4 z+1\right)} d z
@@ -201,10 +240,18 @@
 
 
 
-> [!figure] Figure 5
-> 
-> ![300](./images/b1ad9866-c636-4d3b-85cb-e1f2bdb2e560-13_514_473_1087_62.jpg)
-> Figure 5 The path and poles for the contour integral in Example 2.
+```scientific-figure
+id: 0208e716-d968-458f-be71-ef757155c5fa
+numbered: false
+title: ""
+caption: "**Figure 5.** The path and poles for the contour integral in Example 2."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 05 Residue Theory/images/b1ad9866-c636-4d3b-85cb-e1f2bdb2e560-13_514_473_1087_62.jpg
+    caption: ""
+```
 
 
 
@@ -264,15 +311,25 @@
 
 
 
-> [!figure] Figure 6
-> 
-> ![300](./images/b1ad9866-c636-4d3b-85cb-e1f2bdb2e560-14_498_510_413_92.jpg)
-> Figure 6 The definite integral in Example 3.
-
-
-
-
-**Solution** First, use the double angle identity $2 \cos ^{2} \theta=1+\cos 2 \theta$, then the change of variables $\theta^{\prime}=2 \theta$, and get (for convenience, rename $\theta^{\prime}$ by $\theta$ )
+```scientific-figure
+id: ebf8409e-587e-4f95-9f81-540c9207f18b
+numbered: false
+title: ""
+caption: "**Figure 6.** The definite integral in Example 3."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 05 Residue Theory/images/b1ad9866-c636-4d3b-85cb-e1f2bdb2e560-14_498_510_413_92.jpg
+    caption: ""
+```
+
+
+
+
+##### solution
+
+First, use the double angle identity $2 \cos ^{2} \theta=1+\cos 2 \theta$, then the change of variables $\theta^{\prime}=2 \theta$, and get (for convenience, rename $\theta^{\prime}$ by $\theta$ )
 
 $$
 I=\int_{0}^{\frac{\pi}{2}} \frac{\cos 2 \theta}{2+\cos 2 \theta} d \theta=\frac{1}{2} \int_{0}^{\pi} \frac{\cos \theta}{2+\cos \theta} d \theta
@@ -303,10 +360,18 @@
 
 
 
-> [!figure] Figure 7
-> 
-> ![300](./images/b1ad9866-c636-4d3b-85cb-e1f2bdb2e560-14_490_527_1342_106.jpg)
-> Figure 7 The path and poles for the contour integral in Example 3.
+```scientific-figure
+id: 9ec46749-5cd3-47e3-951b-a3f2021834a9
+numbered: false
+title: ""
+caption: "**Figure 7.** The path and poles for the contour integral in Example 3."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 05 Residue Theory/images/b1ad9866-c636-4d3b-85cb-e1f2bdb2e560-14_490_527_1342_106.jpg
+    caption: ""
+```
 
 
 

`````
