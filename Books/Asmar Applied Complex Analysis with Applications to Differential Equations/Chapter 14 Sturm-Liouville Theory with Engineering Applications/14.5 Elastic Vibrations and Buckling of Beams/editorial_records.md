
# Editorial records

Reading note: 14.5 Elastic Vibrations and Buckling of Beams.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Move correction/commentary into the separate editorial record; keep the actual correction in the reading text.

### Before

````text
[Source clarification: the diagram labels $y(L)=\delta$ but omits the zero transverse-force condition needed to determine the cantilever buckling eigenvalues. Here $\lambda=P/(EI)$.]
````
### After

````text

````

## Additional source comparison

## 1. Restore the author’s buckling-load explanation; retain the missing free-end force boundary condition below.

### Before

````text
For a uniform column with flexural rigidity $EI$, the critical buckling load is

$$
P_1=EI\lambda_1,
$$

where $\lambda_1$ is the smallest positive buckling eigenvalue, $E$ is Young's modulus, and $I$ is the second moment of the cross-sectional area about the bending axis. Its eigenfunction describes the initial buckling shape.
````
### After

````text
From the theory of strength of materials, the critical buckling load $P_1$ is related to the first eigenvalue of (21) with appropriate boundary conditions by
$$
P_1=EI\lambda_1,
$$
where $E=$ Young's constant and $I=$ moment of inertia of a cross section of the column with respect to an axis through its center of mass and perpendicular to the $(x,y)$-plane. The eigenfunction corresponding to $\lambda_1$ gives an indication of the deformation of the column as it begins to buckle.
````

## Source-to-current comparison

Source: /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 14 Sturm-Liouville Theory with Engineering Applications/14.5 Elastic Vibrations and Buckling of Beams.md

This exact comparison preserves the full change evidence, including formatting, OCR corrections, restored source wording, and required standalone context. The entries above explain the recovery edits. The comparison is not a claim that every difference is a correction; component serialization, callout wrapping, and printed labels outside callouts are formatting.

`````diff
--- /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 14 Sturm-Liouville Theory with Engineering Applications/14.5 Elastic Vibrations and Buckling of Beams.md
+++ /Users/gradyclopton/ObsidianVaults/complex_analysis/Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 14 Sturm-Liouville Theory with Engineering Applications/14.5 Elastic Vibrations and Buckling of Beams.md
@@ -1,8 +1,9 @@
+
 ### 14.5 Elastic Vibrations and Buckling of Beams
 
 The applications that we consider in this section lead to partial differential equations that are fourth order in the space variables. We consider the transverse vibrations of an elastic homogeneous beam with various supports at its ends. We also consider the problem of determining the critical buckling load of a vertical column.
 
-The modeling of these problems can be carried out in a way similar to the problems considered in Section 3.2. Because beams and columns present resistance to bending, the derivations of their equations are more complicated and, in particular, involve the fourth derivative of the displacement with respect to $x$.
+The modeling of these problems can be carried out in a way similar to the problems considered in Section 11.2. Because beams and columns present resistance to bending, the derivations of their equations are more complicated and, in particular, involve the fourth derivative of the displacement with respect to $x$.
 
 ## Transverse Vibrations of a Beam: Simply Supported Case
 
@@ -10,30 +11,43 @@
 
 $$
 u_{t t}=-c^{2} u_{x x x x}
+\tag{1}
 $$
 
 where $c^{2}=\frac{E I}{\rho A}, E=$ Young's constant (determined by the constitutive material of the beam), $I=$ moment of inertia of a cross section of the beam with respect to an axis through its center of mass and perpendicular to the ( $x, u$ )-plane, $\rho=$ density (mass per unit volume), and $A=$ area of cross section. It is assumed that the beam is of uniform density throughout, that the cross sections are constant, and that in its equilibrium position the centers of mass of the cross sections lie on the $x$-axis (see Figure 1). The variable $u(x, t)$ represents the displacement of the point on the beam corresponding to position $x$ at time $t$.
 
-It is customary in engineering to show a simple beam resting on a pin and a roller and not, say, on two pins. In this manner, the beam is said to be statically determinate. If the beam were to have two pins as supports, it would become statically indeterminate and develop horizontal reactions,
-
-Figure 1 A simply supported beam is pinned at one end and roller supported at the other. The ends can rotate freely but do not move vertically.
-which is still acceptable; however, it would not constitute the simplest possible beam. As far as the boundary conditions are concerned, both prevent vertical translation (completely) and both allow rotation (unlike a fixed or clamped support, which locks also rotation). The only difference between a pin and a roller is that a pin prevents horizontal movement, whereas a roller does not (it can roll horizontally). However, both allow rotation and both prevent vertical translation as we said.
+It is customary in engineering to show a simple beam resting on a pin and a roller and not, say, on two pins. In this manner, the beam is said to be statically determinate. If the beam were to have two pins as supports, it would become statically indeterminate and develop horizontal reactions, which is still acceptable; however, it would not constitute the simplest possible beam. As far as the boundary conditions are concerned, both prevent vertical translation (completely) and both allow rotation (unlike a fixed or clamped support, which locks also rotation). The only difference between a pin and a roller is that a pin prevents horizontal movement, whereas a roller does not (it can roll horizontally). However, both allow rotation and both prevent vertical translation as we said.
 
 A structure in equilibrium must also be stable. A simply supported beam is the simplest structure that is also stable. If the supports were to be two rollers, the beam would be unstable (it would not resist any perturbation in the horizontal direction). On the other hand, if it is to rest on two pins, it would have one additional reaction in excess of being a stable structure. Therefore, a pin and a roller are the simplest possible supports for a beam to be both in equilibrium and stable.
-![](./images/28f4ed6f-dce0-442f-8bed-abc918ef4e83-35_299_817_853_578.jpg)
+```scientific-figure
+id: 0f871911-82c6-476f-b3d5-1c32d0cc0cf7
+numbered: false
+title: ""
+caption: Figure 1 A simply supported beam is pinned at one end and roller supported at the other. The ends can rotate freely but do not move vertically.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 14 Sturm-Liouville Theory with Engineering Applications/images/28f4ed6f-dce0-442f-8bed-abc918ef4e83-35_299_817_853_578.jpg
+    caption: ""
+```
+
+
 
 The boundary conditions that accompany equation (1) depend on the end supports of the beam. The case under consideration, that of simply supported ends, is described by
 
 $$
 u(0, t)=0, \quad u(L, t)=0, \quad u_{x x}(0, t)=0, \quad u_{x x}(L, t)=0 .
-$$
-
-The fact that the beam is prevented from translating vertically at its supports is expressed by the first two equations in (2). To understand the remaining equations in (2), recall that $u_{x x}(x, t)$ represents the curvature or concavity of the beam at any $x$. It is a fact from the theory of strength of materials that curvature is proportional to bending moment for an elastic beam. The last two equations in (2) state that the moments at the supports are zero, as is the case for a simply supported beam, since the beam can rotate at its ends.
+\tag{2}
+$$
+
+The fact that the beam is prevented from translating vertically at its supports is expressed by the first two equations in (2). To understand the remaining equations in (2), recall that $u_{xx}(x,t)$ approximates the curvature when slopes are small. It is a fact from the theory of strength of materials that curvature is proportional to bending moment for an elastic beam. The last two equations in (2) state that the moments at the supports are zero, as is the case for a simply supported beam, since the beam can rotate at its ends.
 
 To complete the description of the initial value problem, we specify the initial conditions
 
 $$
 u(x, 0)=f(x), u_{t}(x, 0)=g(x), \quad 0<x<L,
+\tag{3}
 $$
 
 which give the initial displacement and velocity of the beam.
@@ -41,9 +55,10 @@
 
 $$
 \frac{X^{(4)}}{X}=-\frac{T^{\prime \prime}}{c^{2} T}=\alpha^{4} .
-$$
-
-We have chosen the separation constant to be positive because we expect periodic behavior in $t$, and for reasons that will become apparent momentarily it is convenient to denote this constant by $\alpha^{4}$. For the sake of completeness, we note that it can be shown that the boundary value problem $X^{(4)}-\lambda X=0$ together with the boundary conditions implied by (2) has nontrivial solutions only for positive choices of the separation constant $\lambda$ (see Example 2 (a), Section 14.4).
+\tag{4}
+$$
+
+We have chosen the separation constant to be positive because we expect periodic behavior in $t$, and for reasons that will become apparent momentarily it is convenient to denote this constant by $\alpha^{4}$. For the sake of completeness, we note that it can be shown that the boundary value problem $X^{(4)}-\lambda X=0$ together with the boundary conditions implied by (2) has nontrivial solutions only for positive choices of the separation constant $\lambda$ (see Example 2(b), Section 14.4).
 
 We begin by considering the boundary value problem for $X$ :
 
@@ -52,9 +67,10 @@
 X^{(4)}-\alpha^{4} X=0 \\
 X(0)=0, \quad X(L)=0, \quad X^{\prime \prime}(0)=0, X^{\prime \prime}(L)=0
 \end{gathered}
-$$
-
-Note that this is a fourth-order Sturm-Liouville problem of the type described in the previous section, with $\lambda=\alpha^{4}, p(x)=1, q(x)=0$, and $r(x)=1$. Since (5) is a linear equation with constant coefficients, we solve it by passing to the characteristic equation in the familiar way (Appendix A.2). We find
+\tag{5}
+$$
+
+Note that this is a fourth-order Sturm-Liouville problem of the type described in the previous section, with $\lambda=\alpha^{4}, p(x)=1, q(x)=0$, and $r(x)=1$. Since (5) is a linear equation with constant coefficients, we solve it by passing to the characteristic equation in the familiar way (Section 10.2). We find
 
 $$
 r^{4}-\alpha^{4}=0 \Rightarrow r= \pm \alpha, \quad \text { and } \quad r= \pm i \alpha
@@ -95,7 +111,6 @@
 
 Note that in this case it is easy to verify that the eigenfunctions $X_{n}$ are orthogonal on the interval $0<x<L$ as guaranteed by Theorem 1 of Section 14.4.
 
-Figure 2 A beam with two clamped ends.
 
 Going back to (4) and solving for $T$ with $\alpha=\alpha_{n}$, we obtain the corresponding solutions
 
@@ -107,6 +122,7 @@
 
 $$
 u(x, t)=\sum_{n=1}^{\infty} \sin \frac{n \pi}{L} x\left(A_{n} \cos c \alpha_{n}^{2} t+A_{n}^{*} \sin c \alpha_{n}^{2} t\right) .
+\tag{6}
 $$
 
 Using the initial conditions (3), we get
@@ -121,7 +137,7 @@
 g(x)=\sum_{n=1}^{\infty} A_{n}^{*} c \alpha_{n}^{2} \sin \frac{n \pi}{L} x .
 $$
 
-Since these should just be the sine expansions of $f$ and $g$ on the interval $0<x<L$, it follows directly from Section 2.4 that
+Since these should just be the sine expansions of $f$ and $g$ on the interval $0<x<L$, it follows directly from Section 7.4 that
 
 $$
 \begin{gathered}
@@ -130,6 +146,8 @@
 \end{gathered}
 $$
 
+*Printed equation labels: (7) displacement coefficients; (8) velocity coefficients.*
+
 The solution of (1)-(3) is thus given by the series (6) with the coefficients determined by (7) and (8).
 
 ## Transverse Vibrations of a Beam: Clamped Case
@@ -138,15 +156,30 @@
 
 $$
 u(0, t)=0, u(L, t)=0, \quad u_{x}(0, t)=0, u_{x}(L, t)=0
+\tag{9}
 $$
 
 for all $t>0$. While the first two conditions in (9) are the same as those for the simply supported case, the last two impose a restraint against end rotation, since the beam does resist moments at its ends. The initial conditions remain
 
 $$
 u(x, 0)=f(x), u_{t}(x, 0)=g(x), \quad 0<x<L .
-$$
-
-![](./images/28f4ed6f-dce0-442f-8bed-abc918ef4e83-37_274_736_1936_680.jpg)
+\tag{10}
+$$
+
+```scientific-figure
+id: 0e78fcc6-90fc-4b7f-bf88-d5012cc02644
+numbered: false
+title: ""
+caption: Figure 2 A beam with two clamped ends.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 14 Sturm-Liouville Theory with Engineering Applications/images/28f4ed6f-dce0-442f-8bed-abc918ef4e83-37_274_736_1936_680.jpg
+    caption: ""
+```
+
+
 
 We solve the boundary value problem (1), (9), (10), in much the same way as in the previous example. After separating the variables, we arrive at the fourth order Sturm-Liouville problem
 
@@ -155,6 +188,7 @@
 X^{(4)}-\lambda X=0, \\
 X(0)=0, \quad X(L)=0, \quad X^{\prime}(0)=0, \quad X^{\prime}(L)=0 .
 \end{gathered}
+\tag{11}
 $$
 
 This is precisely the problem solved in Examples 1 and 2 of the previous section, where we found that $\lambda=\lambda_{n}=\alpha_{n}^{4}$, and
@@ -167,6 +201,7 @@
 
 $$
 \cosh \alpha L \cos \alpha L=1, \quad \text { or } \quad \cos \alpha L=\frac{1}{\cosh \alpha L}
+\tag{12}
 $$
 
 Using the solution for $T$ from the previous example and superposing product solutions, we arrive at
@@ -177,12 +212,14 @@
 & \left.\quad-\frac{\cosh \alpha_{n} L-\cos \alpha_{n} L}{\sinh \alpha_{n} L-\sin \alpha_{n} L}\left(\sinh \alpha_{n} x-\sin \alpha_{n} x\right)\right\} \\
 & \quad \times\left\{A_{n} \cos \alpha_{n}^{2} c t+A_{n}^{*} \sin \alpha_{n}^{2} c t\right\}
 \end{aligned}
+\tag{13}
 $$
 
 We now determine the coefficients by using the initial conditions and appealing to Theorem 2 of Section 14.4. We get
 
 $$
 A_{n}=\frac{1}{\kappa_{n}} \int_{0}^{L} f(x) X_{n}(x) d x, \quad A_{n}^{*}=\frac{1}{\alpha_{n}^{2} c \kappa_{n}} \int_{0}^{L} g(x) X_{n}(x) d x
+\tag{14}
 $$
 
 where
@@ -193,13 +230,16 @@
 
 and the $\alpha_{n}$ 's are the positive roots of (12). We illustrate this problem numerically.
 
-## EXAMPLE 1 Vibrating elastic beam: clamped case
-
-Consider the boundary value problem (1), (9), (10), with
-
-$$
-L=1, c=1, f(x)=\sin ^{2} \pi x, g(x)=0 .
-$$
+> [!exercise] EXAMPLE 1 Vibrating elastic beam: clamped case
+> Consider the boundary value problem (1), (9), (10), with
+>
+> $$
+> L=1, c=1, f(x)=\sin ^{2} \pi x, g(x)=0 .
+> $$
+>
+> Find the motion of the beam and illustrate it using the first five modes.
+
+##### solution
 
 The solution of this problem is given by (13), where $A_{n}$ and $A_{n}^{*}$ are given by (14), and $\alpha_{n}$ is the $n$th positive root of (12), with $L=1$. The eigenfunctions are
 
@@ -209,13 +249,43 @@
 
 Since $g$ is identically zero, we have $A_{n}^{*}=0$. In Table 1, we recall from Example 1 of the previous section the coefficients $A_{n}$ and the numerical values of the $\alpha_{n}$ 's, for $n=1,2, \ldots, 5$. We also compute the values of $\alpha_{n}^{2}$.
 
-| $n$ | 1 | 2 | 3 | 4 | 5 |
-| :---: | :---: | :---: | :---: | :---: | :---: |
-| $\alpha_{n}$ | 4.7300 | 7.8532 | 10.9956 | 14.1372 | 17.2788 |
-| $\alpha_{n}^{2}$ | 22.3729 | 61.6727 | 120.9032 | 199.8604 | 298.5569 |
-| $A_{n}$ | .612 | 0 | -.022 | 0 | -.002 |
-
-Table 1 Numerical data for Example 1.
+```scientific-table
+id: d5ac01b0-2c61-4c76-a388-e39b4bee9b43
+numbered: false
+title: ""
+caption: Table 1 Numerical data for Example 1.
+captionVisible: true
+captionPosition: below
+rows:
+  - - text: $n$
+    - text: "1"
+    - text: "2"
+    - text: "3"
+    - text: "4"
+    - text: "5"
+  - - text: $\alpha_{n}$
+    - text: "4.7300"
+    - text: "7.8532"
+    - text: "10.9956"
+    - text: "14.1372"
+    - text: "17.2788"
+  - - text: $\alpha_{n}^{2}$
+    - text: "22.3729"
+    - text: "61.6727"
+    - text: "120.9032"
+    - text: "199.8604"
+    - text: "298.5569"
+  - - text: $A_{n}$
+    - text: ".612"
+    - text: "0"
+    - text: "-.022"
+    - text: "0"
+    - text: "-.002"
+headerRows: 1
+rowHeaders: true
+style: scientific
+```
+
 
 Using the data from Table 1, we find
 
@@ -229,11 +299,33 @@
 u(x, t) \approx .612 X_{1}(x) \cos \alpha_{1}^{2} t-.022 X_{3}(x) \cos \alpha_{3}^{2} t-.002 X_{5}(x) \cos \alpha_{5}^{2} t
 $$
 
-![](./images/28f4ed6f-dce0-442f-8bed-abc918ef4e83-39_443_814_1206_31.jpg)
-Figure 3 Eigenfunctions for the clamped beam.
-
-![](./images/28f4ed6f-dce0-442f-8bed-abc918ef4e83-39_422_744_1227_969.jpg)
-Figure 4 Snapshots of the vibrating clamped beam.
+```scientific-figure
+id: f5fe2ea7-d343-418b-b654-8dbff940d7cc
+numbered: false
+title: ""
+caption: Figure 3 Eigenfunctions for the clamped beam.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 14 Sturm-Liouville Theory with Engineering Applications/images/28f4ed6f-dce0-442f-8bed-abc918ef4e83-39_443_814_1206_31.jpg
+    caption: ""
+```
+
+
+```scientific-figure
+id: 2baa9132-ff2c-47dd-8805-3fb542952ab3
+numbered: false
+title: ""
+caption: Figure 4 Snapshots of the vibrating clamped beam.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 14 Sturm-Liouville Theory with Engineering Applications/images/28f4ed6f-dce0-442f-8bed-abc918ef4e83-39_422_744_1227_969.jpg
+    caption: ""
+```
+
 
 ## Transverse Vibrations of a Beam: Clamped-Free Case
 
@@ -241,16 +333,29 @@
 
 $$
 u(0, t)=0, u_{x}(0, t)=0, u_{x x}(L, t)=0, u_{x x x}(L, t)=0
+\tag{15}
 $$
 
 and the initial conditions
 
 $$
 u(x, 0)=f(x), u_{t}(x, 0)=g(x), \quad 0<x<L .
-$$
-
-Figure 5 A cantelivered beam is fixed at one end and free at the other.
-![](./images/28f4ed6f-dce0-442f-8bed-abc918ef4e83-40_281_734_183_645.jpg)
+\tag{16}
+$$
+
+```scientific-figure
+id: 08bca0a9-6a1f-44de-a67e-0e7818459d1d
+numbered: false
+title: ""
+caption: Figure 5 A cantilevered beam is fixed at one end and free at the other.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 14 Sturm-Liouville Theory with Engineering Applications/images/28f4ed6f-dce0-442f-8bed-abc918ef4e83-40_281_734_183_645.jpg
+    caption: ""
+```
+
 
 We separate the variables and arrive at the fourth order Sturm-Liouville problem
 
@@ -259,6 +364,7 @@
 X^{(4)}-\lambda X=0 \\
 X(0)=0, X^{\prime}(0)=0, X^{\prime \prime}(L)=0, X^{\prime \prime \prime}(L)=0
 \end{gathered}
+\tag{17}
 $$
 
 The solution of this problem is outlined in Exercise 14, Section 14.4. We have
@@ -280,6 +386,7 @@
 
 $$
 \cosh \alpha L \cos \alpha L=-1
+\tag{18}
 $$
 
 Using the solution for $T$ from the previous example and superposing product solutions, we arrive at
@@ -290,12 +397,14 @@
 & \left.-\frac{\cosh \alpha_{n} L+\cos \alpha_{n} L}{\sinh \alpha_{n} L+\sin \alpha_{n} L}\left(\sin \alpha_{n} x-\sinh \alpha_{n} x\right)\right\} \\
 & \times\left\{A_{n} \cos \alpha_{n}^{2} c t+A_{n}^{*} \sin \alpha_{n}^{2} c t\right\}
 \end{aligned}
+\tag{19}
 $$
 
 To determine the coefficients, we use the initial conditions and appeal to Theorem 2, Section 14.4, and get
 
 $$
 A_{n}=\frac{1}{\kappa_{n}} \int_{0}^{L} f(x) X_{n}(x) d x, \quad A_{n}^{*}=\frac{1}{\alpha_{n}^{2} c \kappa_{n}} \int_{0}^{L} g(x) X_{n}(x) d x
+\tag{20}
 $$
 
 where
@@ -306,21 +415,44 @@
 
 and the $\alpha_{n}$ 's are the positive roots of (18).
 
-## EXAMPLE 2 Vibrating elastic beam: clamped-free case
-
-Solve the boundary value problem (1), (15), (16), with
-
-$$
-L=1, f(x)=x^{2}, g(x)=0, c=1 .
-$$
-
-Solution Here the solution is given by (19) and (20), with $A_{n}^{*}=0$, and the $\alpha_{n}$ 's are determined from the equation
-
-![](./images/28f4ed6f-dce0-442f-8bed-abc918ef4e83-41_340_405_495_42.jpg)
-Figure 6
-
-![](./images/28f4ed6f-dce0-442f-8bed-abc918ef4e83-41_373_700_1782_149.jpg)
-Figure 7 Eigenfunctions for the cantilevered beam.
+> [!exercise] EXAMPLE 2 Vibrating elastic beam: clamped-free case
+> Solve the boundary value problem (1), (15), (16), with
+>
+> $$
+> L=1, f(x)=x^{2}, g(x)=0, c=1 .
+> $$
+
+##### solution
+
+Here the solution is given by (19) and (20), with $A_{n}^{*}=0$, and the $\alpha_{n}$ 's are determined from the equation
+
+```scientific-figure
+id: 05c9f30e-cfeb-47f9-b613-6d6d50d71849
+numbered: false
+title: ""
+caption: Figure 6
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 14 Sturm-Liouville Theory with Engineering Applications/images/28f4ed6f-dce0-442f-8bed-abc918ef4e83-41_340_405_495_42.jpg
+    caption: ""
+```
+
+
+```scientific-figure
+id: 51658425-da28-4daa-b6bc-5508d35bcdf6
+numbered: false
+title: ""
+caption: Figure 7 Eigenfunctions for the cantilevered beam.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 14 Sturm-Liouville Theory with Engineering Applications/images/28f4ed6f-dce0-442f-8bed-abc918ef4e83-41_373_700_1782_149.jpg
+    caption: ""
+```
+
 
 $$
 \cos \alpha=-\frac{1}{\cosh \alpha} .
@@ -328,11 +460,31 @@
 
 As shown in Figure 6, this equation has infinitely many positive real roots. With the help of a computer, we approximated the numerical values of the first five positive roots and included them in Table 2.
 
-| $n$ | 1 | 2 | 3 | 4 | 5 |
-| :--- | :---: | :---: | :---: | :---: | :---: |
-| $\alpha_{n}$ | 1.875 | 4.694 | 7.855 | 10.995 | 14.137 |
-
-Table 2 Numerical data for Example 2.
+```scientific-table
+id: 263d1e25-4e31-44b9-8c85-4b82a8e34165
+numbered: false
+title: ""
+caption: Table 2 Numerical data for Example 2.
+captionVisible: true
+captionPosition: below
+rows:
+  - - text: $n$
+    - text: "1"
+    - text: "2"
+    - text: "3"
+    - text: "4"
+    - text: "5"
+  - - text: $\alpha_{n}$
+    - text: "1.875"
+    - text: "4.694"
+    - text: "7.855"
+    - text: "10.995"
+    - text: "14.137"
+headerRows: 1
+rowHeaders: true
+style: scientific
+```
+
 
 Note that in Table 2, starting with $n=2$, the values are close to those in Table 1 (starting with $n=1$ ). This is because $1 / \cosh \alpha$ goes to zero very rapidly with increasing $\alpha$. Hence the intersection points in Figure 6 above and Figure 1, Section 14.4, have very nearly equal $\alpha$ coordinates, which in turn are very nearly equal to $(n+1 / 2) \pi$. To determine the coefficients $A_{n}$ in the series solution (19), according to (20), we must compute the inner products of $f$ with the eigenfunctions
 
@@ -351,65 +503,113 @@
 
 Figure 7 shows the graphs of the first four eigenfunctions of this problem. Figure 8 shows the position of the beam at various values of $t$. Here also, we used the fifth partial sum to approximate $u$.
 
-![](./images/28f4ed6f-dce0-442f-8bed-abc918ef4e83-41_334_759_1805_908.jpg)
-Figure 8 Snapshots of the vibrating cantilevered beam.
-
-![](./images/28f4ed6f-dce0-442f-8bed-abc918ef4e83-42_479_313_363_65.jpg)
-Figure 9 Vertical column with axial loading.
+```scientific-figure
+id: 51bfbe27-92be-4afa-8e34-9052a9efb9f5
+numbered: false
+title: ""
+caption: Figure 8 Snapshots of the vibrating cantilevered beam.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 14 Sturm-Liouville Theory with Engineering Applications/images/28f4ed6f-dce0-442f-8bed-abc918ef4e83-41_334_759_1805_908.jpg
+    caption: ""
+```
+
+
+```scientific-figure
+id: 3524d005-07b8-44bf-99fd-ccb238f17f78
+numbered: false
+title: ""
+caption: Figure 9 Vertical column with axial loading.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 14 Sturm-Liouville Theory with Engineering Applications/images/28f4ed6f-dce0-442f-8bed-abc918ef4e83-42_479_313_363_65.jpg
+    caption: ""
+```
+
 
 ## Buckling of Columns under Axial Loading
 
-Consider a vertical column of length $L$ of constant density and cross- sectional shape with a load $P$ at its top, as shown in Figure 9. We are interested in finding the largest load $P$ that the column can withstand before buckling. This critical value $P_{1}$ is known as the Euler load. It turns out that $P_{1}$ is determined by the first eigenvalue of the following fourth-order equation:
+Consider a vertical column of length $L$ of constant density and cross-sectional shape with a load $P$ at its top, as shown in Figure 9. We are interested in finding the largest load $P$ that the column can withstand before buckling. This critical value $P_{1}$ is known as the Euler load. It turns out that $P_{1}$ is determined by the first eigenvalue of the following fourth-order equation:
 
 $$
 y^{(4)}+\lambda y^{\prime \prime}=0,
+\tag{21}
 $$
 
 with boundary conditions corresponding to the manner in which the column is fastened at its ends. Typical boundary conditions are shown in Figure 10.
 
-From the theory of strength of materials, the critical buckling load $P_{1}$ is related to the first eigenvalue of (21) with appropriate boundary conditions
-
-![](./images/28f4ed6f-dce0-442f-8bed-abc918ef4e83-42_494_308_1243_719.jpg)
-(b) Clamped-clamped case:
-
-$$
-\begin{aligned}
-& y(0)=0, y^{\prime}(0)=0 \\
-& y(L)=0, y^{\prime}(L)=0
-\end{aligned}
-$$
-
-by
-
-$$
-P_{1}=E I \lambda_{1},
-$$
-
-where $E=$ Young's constant and $I=$ moment of inertia of a cross section of
-
-![](./images/28f4ed6f-dce0-442f-8bed-abc918ef4e83-42_422_137_1315_1336.jpg)
-(c) Simply supported case:
-
-$y(0)=0, y^{\prime \prime}(0)=0$,
-$y(L)=0, y^{\prime \prime}(L)=0$.
-the column with respect to an axis through its center of mass and perpendicular to the ( $x, y$ )-plane. The eigenfunction corresponding to $\lambda_{1}$ gives an indication of the deformation of the column as it begins to buckle. In the following examples, we solve for the Euler load in the second and third cases in Figure 10. We begin with the third case.
-
-![](./images/28f4ed6f-dce0-442f-8bed-abc918ef4e83-42_471_313_1266_95.jpg)
-(a) Clamped-free case:
-
-$$
-\begin{aligned}
-& y(0)=0, y^{\prime}(0)=0 \\
-& y(L)=\delta, y^{\prime \prime}(L)=0
-\end{aligned}
-$$
-
-Figure 10 Boundary conditions for a vertical column with axial loading.
-
-EXAMPLE 3 Buckling of a column: simply supported case To solve for the critical load (Euler load) of a hinged-hinged column, we consider the equation
+From the theory of strength of materials, the critical buckling load $P_1$ is related to the first eigenvalue of (21) with appropriate boundary conditions by
+$$
+P_1=EI\lambda_1,
+$$
+where $E=$ Young's constant and $I=$ moment of inertia of a cross section of the column with respect to an axis through its center of mass and perpendicular to the $(x,y)$-plane. The eigenfunction corresponding to $\lambda_1$ gives an indication of the deformation of the column as it begins to buckle.
+
+Figure 10 illustrates three end constraints. For a clamped-free column, the free-end displacement $\delta=y(L)$ is an unknown amplitude, not a prescribed homogeneous eigenvalue condition. The complete small-deflection buckling conditions are
+
+$$
+y(0)=y'(0)=0,\qquad y''(L)=0,\qquad y^{(3)}(L)+\lambda y'(L)=0.
+$$
+
+
+
+```scientific-figure
+id: c29c92de-a754-41c2-b939-8e5a218cc799
+numbered: false
+title: ""
+caption: Figure 10(a) Clamped-free column; $y(L)=\delta$ denotes its unknown tip deflection.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 14 Sturm-Liouville Theory with Engineering Applications/images/28f4ed6f-dce0-442f-8bed-abc918ef4e83-42_471_313_1266_95.jpg
+    caption: ""
+```
+
+
+```scientific-figure
+id: c76214de-2043-4ac0-9f9c-82facc17105f
+numbered: false
+title: ""
+caption: "Figure 10(b) Clamped-clamped column: $y(0)=y'(0)=y(L)=y'(L)=0$."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 14 Sturm-Liouville Theory with Engineering Applications/images/28f4ed6f-dce0-442f-8bed-abc918ef4e83-42_494_308_1243_719.jpg
+    caption: ""
+```
+
+
+```scientific-figure
+id: 97e9dbb3-0817-4a3c-a2ae-780123951c37
+numbered: false
+title: ""
+caption: "Figure 10(c) Simply supported column: $y(0)=y''(0)=y(L)=y''(L)=0$."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 14 Sturm-Liouville Theory with Engineering Applications/images/28f4ed6f-dce0-442f-8bed-abc918ef4e83-42_422_137_1315_1336.jpg
+    caption: ""
+```
+
+
+In the following examples, we solve for the Euler load in the simply supported and clamped-clamped cases.
+
+> [!exercise] EXAMPLE 3 Buckling of a column: simply supported case
+> Find the critical Euler buckling load and the first buckling mode for a uniform column of length $L$ and flexural rigidity $EI$, with both ends simply supported.
+
+##### solution
+
+To solve for the critical load (Euler load) of a hinged-hinged column, we consider the equation
 
 $$
 y^{(4)}+\lambda y^{\prime \prime}=0,
+\tag{22}
 $$
 
 together with the boundary conditions
@@ -418,7 +618,7 @@
 y(0)=0, y^{\prime \prime}(0)=0, y(L)=0, y^{\prime \prime}(L)=0 .
 $$
 
-It can be shown that nonpositive values of $\lambda$ lead only to the trivial solution $y=0$ (see Exercise 9). Therefore, we concentrate on the case $\lambda>0$, and hence it is convenient to set $\lambda=\alpha^{2}$ with $\alpha>0$. The characteristic equation of (22) is
+It can be shown that nonpositive values of $\lambda$ lead only to the trivial solution $y=0$ (see Exercise 8). Therefore, we concentrate on the case $\lambda>0$, and hence it is convenient to set $\lambda=\alpha^{2}$ with $\alpha>0$. The characteristic equation of (22) is
 
 $$
 r^{4}+\alpha^{2} r^{2}=r^{2}\left(r^{2}+\alpha^{2}\right)=0
@@ -450,7 +650,10 @@
 
 and gives the shape of the deflection when the column first begins to buckle. In conclusion, we find that the Euler load for this column is $E I \frac{\pi^{2}}{L^{2}}$.
 
-## EXAMPLE 4 Buckling of a column: clamped-clamped case
+> [!exercise] EXAMPLE 4 Buckling of a column: clamped-clamped case
+> Find the critical Euler buckling load and the first buckling mode for a uniform column of length $L$ and flexural rigidity $EI$, clamped at both ends.
+
+##### solution
 
 For this case, we must solve equation (22) with the boundary conditions
 
@@ -458,7 +661,7 @@
 y(0)=0, y^{\prime}(0)=0, y(L)=0, y^{\prime}(L)=0 .
 $$
 
-It can be shown that nonpositive values of $\lambda$ lead only to the trivial solution $y=0$ (see Exercise 10). We therefore concentrate on the case $\lambda=\alpha^{2}$ with $\alpha>0$. From Example 3, we have
+It can be shown that nonpositive values of $\lambda$ lead only to the trivial solution $y=0$ (see Exercise 9). We therefore concentrate on the case $\lambda=\alpha^{2}$ with $\alpha>0$. From Example 3, we have
 
 $$
 y=A+B x+C \cos \alpha x+D \sin \alpha x .
@@ -473,6 +676,7 @@
 & A+B L+C \cos \alpha L+D \sin \alpha L=0 \\
 & B-\alpha C \sin \alpha L+\alpha D \cos \alpha L=0
 \end{aligned}
+\tag{23}
 $$
 
 Using the first and second of these equations in the third and fourth, we get
@@ -482,9 +686,8 @@
 (1-\cos \alpha L) C+(\alpha L-\sin \alpha L) D=0 \\
 \sin \alpha L C+(1-\cos \alpha L) D=0
 \end{array}\right.
-$$
-
-$\left(k \pi+\frac{\pi}{2},(k+1) \pi+\frac{\pi}{2}\right)$, $k=0,1,2, \ldots$.
+\tag{24}
+$$
 
 If this system of equations has a nonzero determinant, then its only solutions are $C=D=0$. This leads to a trivial solution for $y$. Hence, to get nontrivial solutions, we must set the determinant equal to 0 . We get
 
@@ -516,13 +719,24 @@
 \tan \frac{\alpha L}{2}=\frac{\alpha L}{2} .
 $$
 
-Figure 11 The transcendental equation $\tan x=x$ has infinitely many positive roots; one in each interval
-![](./images/28f4ed6f-dce0-442f-8bed-abc918ef4e83-44_507_1019_1105_685.jpg)
-
-The roots of this transcendental equation cannot be found explicitly, but as we have done before, we can use a computer system to approximate them. As Figure 11 shows, the first positive root is certainly larger than $2 \pi / L$. Hence $\alpha_{1}=2 \pi / L$, and the Euler load is
-
-$$
-P_{1}=\frac{4 \pi^{2}}{L^{2}} E l
+```scientific-figure
+id: 63212471-b559-4cd3-bbf2-9662af82e208
+numbered: false
+title: ""
+caption: Figure 11 The equation $\tan x=x$ has one positive root in each interval $(k\pi,k\pi+\pi/2)$, $k=1,2,\ldots$.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 14 Sturm-Liouville Theory with Engineering Applications/images/28f4ed6f-dce0-442f-8bed-abc918ef4e83-44_507_1019_1105_685.jpg
+    caption: ""
+```
+
+
+The roots of this transcendental equation cannot be found explicitly, but as we have done before, we can use a computer system to approximate them. Writing $z=\alpha L/2$, the first positive solution of $\tan z=z$ lies in $(\pi,3\pi/2)$; hence its corresponding $\alpha$ is greater than $2\pi/L$. Hence $\alpha_{1}=2 \pi / L$, and the Euler load is
+
+$$
+P_{1}=\frac{4 \pi^{2}}{L^{2}} E I
 $$
 
 Note that the critical load is four times greater than its value in the simply supported case. Finally, if we are interested in the shape of the column as it buckles, we have to compute the eigenfunction corresponding to $\alpha_{1}$. With $\alpha_{1}=\frac{2 \pi}{L}$, the first equation in (24) implies that $D=0$, and hence $B=0$. The coefficients $A$ and $C$ are related by $A=-C$. Taking $A=1$, we get the eigenfunction
@@ -537,21 +751,53 @@
 y_{1}=2 \sin ^{2} \frac{\pi}{L} x .
 $$
 
-## Exercises 6.5
-
-In Exercises 1-2, solve the boundary value problem (1), (2), (3) subject to the given conditions.
-
-1. $f(x)=x \sin \pi x, g(x)=0, c=\pi, L=1$.
-2. $f(x)=x(1-x), g(x)=0, c=\pi, L=1$.
-
-In Exercises 3-4, solve the boundary value problem (1), (9), (10) subject to the given conditions.
-3. $f(x)=x(1-x), \quad g(x)=x, c=1, L=1$.
-4. $f(x)=1-\cos 4 \pi x, \quad g(x)=\sin 2 \pi x, c=1, L=1$.
-
-In Exercises 5-6, solve the boundary value problem (1), (15), (16) subject to the given conditions.
-5. $f(x)=x^{3}, g(x)=0, c=\pi, L=1$.
-6. $f(x)=x^{2} \cos \pi x, g(x)=0, \quad c=\pi, L=1$.
-7. (a) Determine the eigenvalues of the problem in Figure 10(a).
-(b) Determine the critical buckling load for a clamped-free column.
-8. Show that the eigenvalues in Example 3 are positive.
-9. Show that the eigenvalues in Example 4 are positive.
+## Exercises 14.5
+
+
+> [!prompt] Shared exercise instructions
+> In Exercises 1-2, solve the boundary value problem (1), (2), (3) subject to the given conditions.
+
+
+> [!exercise] Exercise 1
+> $f(x)=x \sin \pi x, g(x)=0, c=\pi, L=1$.
+
+
+> [!exercise] Exercise 2
+> $f(x)=x(1-x), g(x)=0, c=\pi, L=1$.
+
+
+> [!prompt] Shared exercise instructions
+> In Exercises 3-4, solve the boundary value problem (1), (9), (10) subject to the given conditions.
+
+
+> [!exercise] Exercise 3
+> $f(x)=x(1-x), \quad g(x)=x, c=1, L=1$.
+
+
+> [!exercise] Exercise 4
+> $f(x)=1-\cos 4 \pi x, \quad g(x)=\sin 2 \pi x, c=1, L=1$.
+
+
+> [!prompt] Shared exercise instructions
+> In Exercises 5-6, solve the boundary value problem (1), (15), (16) subject to the given conditions.
+
+
+> [!exercise] Exercise 5
+> $f(x)=x^{3}, g(x)=0, c=\pi, L=1$.
+
+
+> [!exercise] Exercise 6
+> $f(x)=x^{2} \cos \pi x, g(x)=0, \quad c=\pi, L=1$.
+
+
+> [!exercise] Exercise 7
+> (a) Determine the eigenvalues of the problem in Figure 10(a).
+> (b) Determine the critical buckling load for a clamped-free column.
+
+
+> [!exercise] Exercise 8
+> Show that the eigenvalues in Example 3 are positive.
+
+
+> [!exercise] Exercise 9
+> Show that the eigenvalues in Example 4 are positive.

`````
