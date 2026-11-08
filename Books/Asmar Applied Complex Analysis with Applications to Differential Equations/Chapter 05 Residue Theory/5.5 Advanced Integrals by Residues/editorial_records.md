
# Editorial records

Reading note: 5.5 Advanced Integrals by Residues.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

No recovery content changes were needed in this note. Existing genuine corrections and formatting were retained.

## Source-to-current comparison

Source: /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 05 Residue Theory/5.5 Advanced Integrals by Residues.md

This exact comparison preserves the full change evidence, including formatting, OCR corrections, restored source wording, and required standalone context. The entries above explain the recovery edits. The comparison is not a claim that every difference is a correction; component serialization, callout wrapping, and printed labels outside callouts are formatting.

`````diff
--- /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 05 Residue Theory/5.5 Advanced Integrals by Residues.md
+++ /Users/gradyclopton/ObsidianVaults/complex_analysis/Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 05 Residue Theory/5.5 Advanced Integrals by Residues.md
@@ -63,10 +63,18 @@
 
 
 
-> [!figure] Figure 1
-> ![300](Pasted%20image%2020260421183500.png)
-> 
-> Figure 1 The rectangular contour for Example 1.
+```scientific-figure
+id: 8aa8e118-aae5-4491-b3f7-991114d34077
+numbered: false
+title: ""
+caption: "**Figure 1.** The rectangular contour for Example 1."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 05 Residue Theory/images/Pasted image 20260421183500.png
+    caption: ""
+```
 
 
 
@@ -149,14 +157,24 @@
 
 
 
-**Solution** For the given integrands, it is natural to consider the function $f(z)= \frac{e^{\mathrm{i} 2}}{z^{\mathrm{a}}}$. The only trouble is that $z^\alpha$ is multiple-valued and so we need to specify a single-valued branch of $z^\alpha$. The choice of this branch is usually affected by the choice of the contour of integration. In this case, we will use the contour $\gamma$ in Figure 2, and choose a branch of $z^\alpha=e^{\alpha \log z}$ that equals the real-numbered power $x^\alpha$ on the $x$-axis and is analytic on the contour. 
-
-
-
-> [!figure] Figure 2
-> ![](Pasted%20image%2020260421183702.png)
-> 
-> Figure 2 The contour for Example 1.
+##### solution
+
+For the given integrands, it is natural to consider the function $f(z)= \frac{e^{iz}}{z^{\alpha}}$. The only trouble is that $z^\alpha$ is multiple-valued and so we need to specify a single-valued branch of $z^\alpha$. The choice of this branch is usually affected by the choice of the contour of integration. In this case, we will use the contour $\gamma$ in Figure 2, and choose a branch of $z^\alpha=e^{\alpha \log z}$ that equals the real-numbered power $x^\alpha$ on the $x$-axis and is analytic on the contour. 
+
+
+
+```scientific-figure
+id: 1f60bf76-b3f0-4bb7-a6b7-440081a1dc07
+numbered: false
+title: ""
+caption: "**Figure 2.** The contour for Example 1."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 05 Residue Theory/images/Pasted image 20260421183702.png
+    caption: ""
+```
 
 
 
@@ -247,10 +265,18 @@
 named after the French mathematician and physicist Augustin Fresnel (17881827), one of the founders of the wave theory of light. The cosine integral and its convergence are illustrated in Figure 3. 
 
 
-> [!figure] Figure 3
-> 
-> ![](Pasted%20image%2020260421183820.png)
-> Figure 3 An illustration of the Fresnel cosine integral.
+```scientific-figure
+id: e6b19c12-ff40-47d8-bda0-c92688f25d50
+numbered: false
+title: ""
+caption: "**Figure 3.** An illustration of the Fresnel cosine integral."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 05 Residue Theory/images/Pasted image 20260421183820.png
+    caption: ""
+```
 
 
 
@@ -274,22 +300,24 @@
 
 
 
-**Solution** We will integrate branches of $f_1(z)=\frac{1}{z^\alpha(z+1)}$ on the contours $\Gamma_1= \left(\gamma_1, \gamma_3, \gamma_5, \gamma_7\right)$ and $\Gamma_2=\left(\gamma_2, \gamma_4, \gamma_6, \gamma_8\right)$, shown in Figures 4, 5, and 6. 
+##### solution
+
+We will integrate branches of $f_1(z)=\frac{1}{z^\alpha(z+1)}$ on the contours $\Gamma_1= \left(\gamma_1, \gamma_3, \gamma_5, \gamma_7\right)$ and $\Gamma_2=\left(\gamma_2, \gamma_4, \gamma_6, \gamma_8\right)$, shown in Figures 4, 5, and 6. 
 
 
 
 ```hblock
 
-![](Pasted%20image%2020260421184040.png)
+![](Books/Asmar%20Applied%20Complex%20Analysis%20with%20Applications%20to%20Differential%20Equations/Chapter%2005%20Residue%20Theory/images/Pasted%20image%2020260421184040.png)
 Figure 4 The contour $\Gamma_1$ and the branch cut of $f_1(z)$.
 ---
 
-![](Pasted%20image%2020260421184116.png)
+![](Books/Asmar%20Applied%20Complex%20Analysis%20with%20Applications%20to%20Differential%20Equations/Chapter%2005%20Residue%20Theory/images/Pasted%20image%2020260421184116.png)
 Figure 5 The contour $\Gamma_2$ and the branch cut of $f_2(z)$.
 
 ---
 
-![](Pasted%20image%2020260421184150.png)
+![](Books/Asmar%20Applied%20Complex%20Analysis%20with%20Applications%20to%20Differential%20Equations/Chapter%2005%20Residue%20Theory/images/Pasted%20image%2020260421184150.png)
 Figure 6 The contours
 
 $$
@@ -388,10 +416,18 @@
 where we use the $\log _0$ branch of the square root, so that the branch cut of $h(z)$ is on the part of the positive $x$-axis $x>a$. Explicitly, $h(z)=$ $|z-a|^{\frac{1}{2}} e^{\frac{1}{2} \arg _0(z-a)}$, where $0<\arg _0(z-a) \leq 2 \pi$. We will use this function and allow it to take different values on the branch cut, depending on how we approach the branch cut. For example, if $z$ approaches the part of the $x$ axis $x>a$ from the upper half-plane (Figure 7), then $\arg (z-a)$ approaches 0 and so the values of the function to the right of $a$ and above the $x$-axis are $\sqrt{z-a}=\sqrt{|x-a|}=\sqrt{x-a}$. 
 
 
-> [!figure] Figure 7
-> 
-> ![](Pasted%20image%2020260421184312.png)
-> Figure 7 Defining $\sqrt{z-a}$ as $z$ approaches the branch cut from above.
+```scientific-figure
+id: c682e2d3-1a8a-4b63-b89c-e6e66f151ef5
+numbered: false
+title: ""
+caption: "**Figure 7.** Defining $\\sqrt{z-a}$ as $z$ approaches the branch cut from above."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 05 Residue Theory/images/Pasted image 20260421184312.png
+    caption: ""
+```
 
 
 
@@ -400,10 +436,18 @@
 If $z$ approaches the part of the $x$-axis $x>a$ from the lower half-plane (Figure 8), then $\arg (z-a)$ approaches $2 \pi$ and so the values of the function to the right of $a$ and below the $x$-axis are taken to be $\sqrt{z-a}=e^{i \frac{1}{2}(2 \pi)} \sqrt{|x-a|}=-\sqrt{x-a}$. 
 
 
-> [!figure] Figure 8
-> 
-> ![](Pasted%20image%2020260421184349.png)
-> Figure 8 Defining $\sqrt{z-a}$ as $z$ approaches the branch cut from below.
+```scientific-figure
+id: 01745697-097b-4a8b-ad4f-da8d51f5fa59
+numbered: false
+title: ""
+caption: "**Figure 8.** Defining $\\sqrt{z-a}$ as $z$ approaches the branch cut from below."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 05 Residue Theory/images/Pasted image 20260421184349.png
+    caption: ""
+```
 
 
 
@@ -412,10 +456,18 @@
 
 
 
-> [!figure] Figure 9
-> 
-> ![](Pasted%20image%2020260421184424.png)
-> Figure 9 The mapping $w=\sqrt{z-a}$ maps the upper half of the branch cut to the right half of the real axis and the lower half of the branch cut to the left half of the real axis.
+```scientific-figure
+id: 2e1ef6e6-039c-4346-b180-a4f28168e95f
+numbered: false
+title: ""
+caption: "**Figure 9.** The mapping $w=\\sqrt{z-a}$ maps the upper half of the branch cut to the right half of the real axis and the lower half of the branch cut to the left half of the real axis."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 05 Residue Theory/images/Pasted image 20260421184424.png
+    caption: ""
+```
 
 
 
@@ -438,7 +490,9 @@
 
 
 
-**Solution** Consider the function
+##### solution
+
+Consider the function
 
 $$
 f(z)=\frac{1}{\sqrt{(z-a)} \sqrt{(z-b)} \sqrt{(z-c)}}
@@ -453,10 +507,18 @@
 
 
 
-> [!figure] Figure 10
-> 
-> ![](Pasted%20image%2020260421184618.png)
-> Figure 10 The contour in Example 4 and its twelve components.
+```scientific-figure
+id: c902f23a-2a18-4d90-b7ff-2bfa927b9b03
+numbered: false
+title: ""
+caption: "**Figure 10.** The contour in Example 4 and its twelve components."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 05 Residue Theory/images/Pasted image 20260421184618.png
+    caption: ""
+```
 
 
 
@@ -482,10 +544,18 @@
 $$
 
 
-> [!figure] Figure 11
-> 
-> ![](Pasted%20image%2020260421184708.png)
-> Figure 11 The limiting values of $\sqrt{z-a}, \sqrt{z-b}$, and $\sqrt{z-c}$.
+```scientific-figure
+id: 406d48b1-1416-4f75-a741-0ae0c97786ef
+numbered: false
+title: ""
+caption: "**Figure 11.** The limiting values of $\\sqrt{z-a}, \\sqrt{z-b}$, and $\\sqrt{z-c}$."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 05 Residue Theory/images/Pasted image 20260421184708.png
+    caption: ""
+```
 
 
 
@@ -521,10 +591,18 @@
 > 
 > 
 > 
-> > [!figure] Figure 12
-> > 
-> > ![](Pasted%20image%2020260421185106.png)
-> > Figure 12 The inequality $\cos 2 x \geq 1-\frac{4}{\pi} x, 0 \leq x \leq \frac{\pi}{4}$.
+> ```scientific-figure
+> id: 9aecb2ff-ccf1-49c9-8c98-78707dfb7c0e
+> numbered: false
+> title: ""
+> caption: "**Figure 12.** The inequality $\\cos 2 x \\geq 1-\\frac{4}{\\pi} x, 0 \\leq x \\leq \\frac{\\pi}{4}$."
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 05 Residue Theory/images/Pasted image 20260421185106.png
+>     caption: ""
+> ```
 > 
 > 
 > Since the graph concaves down, it is above the chord that joins any two points on the graph. Explain how this implies the inequality
@@ -537,10 +615,18 @@
 > Let $I_j(j=1,2,3)$ denote the integral of $f(z)=e^{-z^2}$ on the closed contour in Figure 13. 
 > 
 > 
-> > [!figure] Figure 13
-> > 
-> > ![](Pasted%20image%2020260421185143.png)
-> > 
+> ```scientific-figure
+> id: a0b082b9-a592-4935-aad0-dec7c7ac1cf9
+> numbered: false
+> title: ""
+> caption: "**Figure 13.**"
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 05 Residue Theory/images/Pasted image 20260421185143.png
+>     caption: ""
+> ```
 > 
 > 
 > Prove the following.
@@ -582,9 +668,18 @@
 > 
 > 
 > 
-> > [!figure]
-> > ![](Pasted%20image%2020260421185232.png)
-> > 
+> ```scientific-figure
+> id: aeee8a7f-0a1b-4ac0-8b43-7a03f263947d
+> numbered: false
+> title: ""
+> caption: ""
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 05 Residue Theory/images/Pasted image 20260421185232.png
+>     caption: ""
+> ```
 > 
 > 
 > (b) Prove that
@@ -603,9 +698,18 @@
 > $$
 > 
 > 
-> > [!figure] Figure 15
-> > ![](Pasted%20image%2020260421185254.png)
-> > 
+> ```scientific-figure
+> id: 8ff3fda9-9326-40d1-ae5d-72ae08f88008
+> numbered: false
+> title: ""
+> caption: "**Figure 15.**"
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 05 Residue Theory/images/Pasted image 20260421185254.png
+>     caption: ""
+> ```
 > 
 > 
 > 
@@ -617,9 +721,18 @@
 > 
 > 
 > 
-> > [!figure] Figure 16
-> > ![](Pasted%20image%2020260421185325.png)
-> > 
+> ```scientific-figure
+> id: 8ce7813e-8f34-433c-bc07-0da99711c21f
+> numbered: false
+> title: ""
+> caption: "**Figure 16.**"
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 05 Residue Theory/images/Pasted image 20260421185325.png
+>     caption: ""
+> ```
 > 
 > 
 > 
@@ -636,9 +749,18 @@
 > $$
 > 
 > 
-> > [!figure] Figure 17
-> > ![](Pasted%20image%2020260421185354.png)
-> > 
+> ```scientific-figure
+> id: 7f08f1bb-ccb4-45cd-9edc-a31bcbbb8de0
+> numbered: false
+> title: ""
+> caption: "**Figure 17.**"
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 05 Residue Theory/images/Pasted image 20260421185354.png
+>     caption: ""
+> ```
 > 
 > 
 > 
@@ -649,9 +771,18 @@
 > $$
 > 
 > 
-> > [!figure] Figure 18
-> > ![](Pasted%20image%2020260421185419.png)
-> > 
+> ```scientific-figure
+> id: 1e26517d-fc1c-4a23-88dc-75c0c0636398
+> numbered: false
+> title: ""
+> caption: "**Figure 18.**"
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 05 Residue Theory/images/Pasted image 20260421185419.png
+>     caption: ""
+> ```
 > 
 > 
 > 
@@ -662,9 +793,18 @@
 > $$
 > 
 > 
-> > [!figure] Figure 19
-> > ![](Pasted%20image%2020260421185444.png)
-> > 
+> ```scientific-figure
+> id: df581741-c1c7-4809-a7c7-4c3112330979
+> numbered: false
+> title: ""
+> caption: "**Figure 19.**"
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 05 Residue Theory/images/Pasted image 20260421185444.png
+>     caption: ""
+> ```
 > 
 > 
 > 
@@ -706,9 +846,18 @@
 > 
 > 
 > 
-> > [!figure] Figure 20
-> > ![](Pasted%20image%2020260421185511.png)
-> > 
+> ```scientific-figure
+> id: 19a395eb-c422-4aba-94c6-d3127c8f6f40
+> numbered: false
+> title: ""
+> caption: "**Figure 20.**"
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 05 Residue Theory/images/Pasted image 20260421185511.png
+>     caption: ""
+> ```
 > 
 > 
 > 
@@ -744,9 +893,18 @@
 > (b) Consider the contour in Figure 21. Argue that for fixed $\alpha$ and $\beta$, there exists $\epsilon>0$ such that for large enough $R, \gamma_2$ lies below the ray $\theta=\frac{\pi}{4}-\epsilon$ in the right half-plane, and $\gamma_4$ lies above the ray $\theta=-\frac{3 \pi}{4}-\epsilon$ in the left half-plane.
 > 
 > 
-> > [!figure] Figure 21
-> > ![](Pasted%20image%2020260421185547.png)
-> > 
+> ```scientific-figure
+> id: 12d8e832-1e6c-41ce-aa6f-8cea61dccaac
+> numbered: false
+> title: ""
+> caption: "**Figure 21.**"
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 05 Residue Theory/images/Pasted image 20260421185547.png
+>     caption: ""
+> ```
 > 
 > 
 > (c) Letting $I_j$ denote the integral of $e^{-z^2}$ on $\gamma_j$, show that $I_2 \rightarrow 0$ and $I_4 \rightarrow 0$ as $R \rightarrow \infty$.
@@ -763,9 +921,18 @@
 > 22. Another look at Example 3. Derive (7) by considering the $\log _0$ branch of $z^\alpha$ for $f(z)=\frac{1}{z^\alpha(z+1)}$. Use the contour in Figure 22, and treat $f(z)$ to have different values on the upper and lower sides of the real axis, as in the text following Example 3.
 > 
 > 
-> > [!figure] Figure 22
-> > ![](Pasted%20image%2020260421185617.png)
-> > 
+> ```scientific-figure
+> id: 7829a9b9-cfd1-40e6-a13c-eb424ca025c4
+> numbered: false
+> title: ""
+> caption: "**Figure 22.**"
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 05 Residue Theory/images/Pasted image 20260421185617.png
+>     caption: ""
+> ```
 > 
 > 
 
@@ -781,10 +948,18 @@
 > 
 > 
 > 
-> > [!figure] Figure 11
-> > 
-> > ![](Pasted%20image%2020260421184708.png)
-> > Figure 11 The limiting values of $\sqrt{z-a}, \sqrt{z-b}$, and $\sqrt{z-c}$.
+> ```scientific-figure
+> id: 8e0e2e66-4a31-47a1-ac7d-47d8fc63f6d3
+> numbered: false
+> title: ""
+> caption: "**Figure 11.** The limiting values of $\\sqrt{z-a}, \\sqrt{z-b}$, and $\\sqrt{z-c}$."
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 05 Residue Theory/images/Pasted image 20260421184708.png
+>     caption: ""
+> ```
 > 
 > 
 > 
@@ -796,101 +971,109 @@
 > 
 > 
 > 
-> > [!figure] Figure 23
-> > ![](Pasted%20image%2020260421185715.png)
-> > 
-> > 
-> 
-> 
-> 
-> 
-> 
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
+> ```scientific-figure
+> id: bf645a83-5c04-4d76-abfd-5e82866b76a8
+> numbered: false
+> title: ""
+> caption: "**Figure 23.**"
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 05 Residue Theory/images/Pasted image 20260421185715.png
+>     caption: ""
+> ```
+> 
+> 
+> 
+> 
+> 
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+

`````
