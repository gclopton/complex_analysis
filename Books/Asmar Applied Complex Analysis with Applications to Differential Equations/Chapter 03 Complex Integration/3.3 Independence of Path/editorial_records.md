
# Editorial records

Reading note: 3.3 Independence of Path.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Callout 96: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Path Independence and Analytic Antiderivatives
> Let $f$ be a continuous complex-valued function on a region $\Omega$, let $z_{1}, z_{2}$ be two points in $\Omega$, and let
>
> $$
> I=\int_{\gamma} f(z) d z
> $$
>
> where $\gamma$ is a path in $\Omega$ joining $z_{1}$ to $z_{2}$. Then $I$ is independent of the path $\gamma$ if and only if $f(z)=F^{\prime}(z)$ for some analytic function $F$ on $\Omega$. In this case, we write
>
> $$
> I=\int_{\gamma} f(z) d z=\int_{z_{1}}^{z_{2}} f(z) d z=F\left(z_{2}\right)-F\left(z_{1}\right)
> $$
````
### After

````text
> [!theorem] Independence of Path
> Let $f$ be a continuous complex-valued function on a region $\Omega$, let $z_{1}, z_{2}$ be two points in $\Omega$, and let
>
> $$
> I=\int_{\gamma} f(z) d z
> $$
>
> where $\gamma$ is a path in $\Omega$ joining $z_{1}$ to $z_{2}$. Then $I$ is independent of the path $\gamma$ if and only if $f(z)=F^{\prime}(z)$ for some analytic function $F$ on $\Omega$. In this case, we write
>
> $$
> I=\int_{\gamma} f(z) d z=\int_{z_{1}}^{z_{2}} f(z) d z=F\left(z_{2}\right)-F\left(z_{1}\right)
> $$
````

## Source-to-current comparison

Source: /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 03 Complex Integration/3.3 Independence of Path.md

This exact comparison preserves the full change evidence, including formatting, OCR corrections, restored source wording, and required standalone context. The entries above explain the recovery edits. The comparison is not a claim that every difference is a correction; component serialization, callout wrapping, and printed labels outside callouts are formatting.

`````diff
--- /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 03 Complex Integration/3.3 Independence of Path.md
+++ /Users/gradyclopton/ObsidianVaults/complex_analysis/Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/3.3 Independence of Path.md
@@ -267,11 +267,21 @@
 
 The Python rendering below uses this choice $\alpha=0$, so the deleted ray is the positive real axis and the negative real axis remains in $\Omega_0$.
 
-> [!figure] Python figure for Exercise 1
-> 
-> ![](./images/exercise1_branch_cut_python.png)
-> 
-> Figure 1. A plot of $\Omega_0=\mathbb{C}\setminus [0,\infty)$.
+```scientific-figure
+id: a2098988-4b68-4523-8452-402d7fde2a0d
+numbered: false
+title: ""
+caption: |-
+  **Figure 1.** Python figure for Exercise 1
+
+  A plot of $\Omega_0=\mathbb{C}\setminus [0,\infty)$.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/exercise1_branch_cut_python.png
+    caption: ""
+```
 
 A Mathematica plot of this branch-cut geometry is:
 
@@ -409,9 +419,18 @@
 
 
 
-> [!figure] Figure 1
-> ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-029_510_456_1877_58.jpg)
-> Figure $1 \log _{\alpha} z$ and its branch cut at angle $\alpha$.
+```scientific-figure
+id: 65ca0763-4c75-422d-b7c2-4740054d3e3a
+numbered: false
+title: ""
+caption: "**Figure 1.** Figure $1 \\log _{\\alpha} z$ and its branch cut at angle $\\alpha$."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-029_510_456_1877_58.jpg
+    caption: ""
+```
 
 
 As we now show, independence of path for integrals can be used to characterize functions with antiderivatives.
@@ -420,20 +439,19 @@
 
 
 
-> [!theorem] Theorem 1: Independence of Path
-> 
+<!-- Source label: Theorem 1: Independence of Path -->
+> [!theorem] Independence of Path
 > Let $f$ be a continuous complex-valued function on a region $\Omega$, let $z_{1}, z_{2}$ be two points in $\Omega$, and let
-> 
+>
 > $$
 > I=\int_{\gamma} f(z) d z
 > $$
-> 
+>
 > where $\gamma$ is a path in $\Omega$ joining $z_{1}$ to $z_{2}$. Then $I$ is independent of the path $\gamma$ if and only if $f(z)=F^{\prime}(z)$ for some analytic function $F$ on $\Omega$. In this case, we write
-> 
+>
 > $$
 > I=\int_{\gamma} f(z) d z=\int_{z_{1}}^{z_{2}} f(z) d z=F\left(z_{2}\right)-F\left(z_{1}\right)
 > $$
-> 
 
 We will prove that if $f$ has an antiderivative, then $\int_{\gamma} f(z) d z$ is independent of path, and we will postpone the other direction until the end of the section. 
 
@@ -467,29 +485,54 @@
 > Evaluate
 > (a) $\int_{\gamma}^{z} d z$, where $\gamma$ is the semi-circle $\gamma(t)=e^{i t}, 0 \leq t \leq \pi$ (_Figure 2(a)_).
 > 
-> > [!figure] Figure 2(a)
-> > 
-> > ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-030_535_532_2099_81.jpg)
-> > Figure 2(a)
+> ```scientific-figure
+> id: 5fe32783-0866-408a-912c-d00d0e9bcc74
+> numbered: false
+> title: ""
+> caption: "**Figure 2.** (a)"
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-030_535_532_2099_81.jpg
+>     caption: ""
+> ```
 > 
 > (b) $\int_{\left[z_{1}, z_{2}, z_{3}, z_{1}\right]}\left(z^{3}+z^{2}-2\right) d z$, where $\left[z_{1}, z_{2}, z_{3}, z_{1}\right]$ is the closed directed line segment with $z_{1}=-1, z_{2}=1, z_{3}=i$ (_Figure 2(b)_).
 > 
 > 
-> > [!figure] Figure 2(b)
-> > 
-> > ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-031_507_479_137_62.jpg)
-> > 
-> > Figure 2(b) A closed triangle path
+> ```scientific-figure
+> id: b9c3462d-ad76-4c3e-bd17-19ebe4194519
+> numbered: false
+> title: ""
+> caption: |-
+>   **Figure 2.** (b)
+> 
+>   (b) A closed triangle path
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-031_507_479_137_62.jpg
+>     caption: ""
+> ```
 > 
 > 
 > (c) $\int_{\gamma} z e^{z^{2}} d z$, where $\gamma$ is the semi-circle $\gamma(t)=-\frac{i}{2}+\frac{1}{2} e^{i t},-\frac{\pi}{2} \leq t \leq \frac{\pi}{2}$ (_Figure 2(c)_).
 > 
 > 
-> > [!figure] Figure 2(c)
-> > 
-> > ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-031_522_489_778_43.jpg)
-> > 
-> > Figure 2(c)
+> ```scientific-figure
+> id: 3b5d3c2e-8375-42d5-ab61-c1366232c177
+> numbered: false
+> title: ""
+> caption: "**Figure 2.** (c)"
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-031_522_489_778_43.jpg
+>     caption: ""
+> ```
 > 
 > 
 > 
@@ -568,11 +611,21 @@
 \int_\gamma e^z\,dz=e^{-1}-e=-2\sinh(1).
 $$
 
-> [!figure] Python figure for Exercise 2(a)
-> 
-> ![](./images/exercise2_problem_a_python.png)
-> 
-> Figure 2(a). The upper semicircular path from $1$ to $-1$.
+```scientific-figure
+id: 44110f8e-25be-4292-9127-540f0ebe62e6
+numbered: false
+title: ""
+caption: |-
+  **Figure 2.** Python figure for Exercise 2(a)
+
+  (a). The upper semicircular path from $1$ to $-1$.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/exercise2_problem_a_python.png
+    caption: ""
+```
 
 A Mathematica plot of the path in part (a) is:
 
@@ -720,11 +773,21 @@
 \int_{\left[z_1,z_2,z_3,z_1\right]} (z^3+z^2-2)\,dz=0.
 $$
 
-> [!figure] Python figure for Exercise 2(b)
-> 
-> ![](./images/exercise2_problem_b_python.png)
-> 
-> Figure 2(b). The closed triangular path through $z_1=-1$, $z_2=1$, and $z_3=i$.
+```scientific-figure
+id: df634248-daff-44c4-8ad5-fba01c1385ee
+numbered: false
+title: ""
+caption: |-
+  **Figure 2.** Python figure for Exercise 2(b)
+
+  (b). The closed triangular path through $z_1=-1$, $z_2=1$, and $z_3=i$.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/exercise2_problem_b_python.png
+    caption: ""
+```
 
 A Mathematica plot of the path in part (b) is:
 
@@ -934,11 +997,21 @@
 \int_\gamma ze^{z^2}\,dz=\frac{1}{2}(1-e^{-1}).
 $$
 
-> [!figure] Python figure for Exercise 2(c)
-> 
-> ![](./images/exercise2_problem_c_python.png)
-> 
-> Figure 2(c). The semicircular path centered at $-\frac{i}{2}$ from $-i$ to $0$.
+```scientific-figure
+id: 5e7613ae-fb75-46e5-b594-c2654bee0c2a
+numbered: false
+title: ""
+caption: |-
+  **Figure 2.** Python figure for Exercise 2(c)
+
+  (c). The semicircular path centered at $-\frac{i}{2}$ from $-i$ to $0$.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/exercise2_problem_c_python.png
+    caption: ""
+```
 
 A Mathematica plot of the path in part (c) is:
 
@@ -1068,9 +1141,18 @@
 > Evaluate $\int_{\left[z_{1}, z_{2}, z_{3}\right]} \frac{1}{z} d z$, where $\left[z_{1}, z_{2}, z_{3}\right]$ is the directed line segment with $z_{1}=1$, $z_{2}=2+i, z_{3}=3$ (_Figure 3_).
 > 
 > 
-> > [!figure] Figure 3
-> > ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-031_511_485_1344_43.jpg)
-> > Figure 3 for Example 3.
+> ```scientific-figure
+> id: 27ebdea5-8a89-4f53-8dcd-d1fec1290b2b
+> numbered: false
+> title: ""
+> caption: "**Figure 3.** for Example 3."
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-031_511_485_1344_43.jpg
+>     caption: ""
+> ```
 > 
 > 
 
@@ -1205,11 +1287,21 @@
 \boxed{\int_{\left[z_1,z_2,z_3\right]} \frac{1}{z}\,dz=\ln 3.}
 $$
 
-> [!figure] Python figure for Exercise 3
-> 
-> ![](./images/exercise3_path_python.png)
-> 
-> Figure 3. The polygonal path from $1$ to $2+i$ to $3$ lies entirely in $\mathbb{C}\setminus(-\infty,0]$.
+```scientific-figure
+id: 1c2cdaad-4379-4e94-8a64-7f6871d8ed83
+numbered: false
+title: ""
+caption: |-
+  **Figure 3.** Python figure for Exercise 3
+
+  The polygonal path from $1$ to $2+i$ to $3$ lies entirely in $\mathbb{C}\setminus(-\infty,0]$.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/exercise3_path_python.png
+    caption: ""
+```
 
 A Mathematica plot of this path is:
 
@@ -1311,7 +1403,9 @@
 
 
 
-**Solution** The function $f(z)=\frac{1}{z}$ is continuous in $\mathbb{C} \backslash\{0\}$. An antiderivative of $\frac{1}{z}$ is $\log z$ in the region $\Omega=\mathbb{C} \backslash(-\infty, 0]$. Since the path $\left[z_{1}, z_{2}, z_{3}\right]$ lies entirely in $\Omega$, we may apply Theorem 1 and get
+##### solution
+
+The function $f(z)=\frac{1}{z}$ is continuous in $\mathbb{C} \backslash\{0\}$. An antiderivative of $\frac{1}{z}$ is $\log z$ in the region $\Omega=\mathbb{C} \backslash(-\infty, 0]$. Since the path $\left[z_{1}, z_{2}, z_{3}\right]$ lies entirely in $\Omega$, we may apply Theorem 1 and get
 
 $$
 \int_{\left[z_{1}, z_{2}, z_{3}\right]} \frac{1}{z} d z=\left.\log z\right|_{1} ^{3}=\log 3-\log 1=\ln 3
@@ -1323,9 +1417,18 @@
 > 
 > 
 > 
-> > [!figure] Figure 4
-> > ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-031_535_476_1972_34.jpg)
-> > Figure 4 for Example 4.
+> ```scientific-figure
+> id: 965e90e8-deae-4b26-91e2-cc9739b02f31
+> numbered: false
+> title: ""
+> caption: "**Figure 4.** for Example 4."
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-031_535_476_1972_34.jpg
+>     caption: ""
+> ```
 > 
 > 
 
@@ -1533,11 +1636,21 @@
 \boxed{\int_{\left[z_1,z_2,z_3\right]} \frac{1}{z}\,dz=\frac{5}{2}\ln 2+i\frac{\pi}{4}.}
 $$
 
-> [!figure] Python figure for Exercise 4
-> 
-> ![](./images/exercise4_path_python.png)
-> 
-> Figure 4. The path lies in $\Omega_0=\mathbb{C}\setminus[0,\infty)$, so the branch $\log_0 z$ is valid along the whole path.
+```scientific-figure
+id: 28c3b797-d9fd-4844-bef5-0dcb4a4448b6
+numbered: false
+title: ""
+caption: |-
+  **Figure 4.** Python figure for Exercise 4
+
+  The path lies in $\Omega_0=\mathbb{C}\setminus[0,\infty)$, so the branch $\log_0 z$ is valid along the whole path.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/exercise4_path_python.png
+    caption: ""
+```
 
 A Mathematica plt of this path and branch-cut choice is:
 
@@ -1650,7 +1763,9 @@
 
 
 
-**Solution** In order to apply Theorem 1, we must find an antiderivative of $\frac{1}{z}$ that is analytic in a region that contains the path $\left[z_{1}, z_{2}, z_{3}\right]$. We cannot use $\log z$ as antiderivative, because it is not analytic in any region that contains the path $\left[z_{1}, z_{2}, z_{3}\right]$. Instead, we will use a different branch of the logarithm. We know from Example 1(d) that $\log _{\alpha} z$ is an antiderivative of $\frac{1}{z}$ in the region $\Omega_{\alpha}$ (the plane minus the ray at angle $\alpha$ ). We can apply Theorem 1 if we choose $\alpha$ in such a way that
+##### solution
+
+In order to apply Theorem 1, we must find an antiderivative of $\frac{1}{z}$ that is analytic in a region that contains the path $\left[z_{1}, z_{2}, z_{3}\right]$. We cannot use $\log z$ as antiderivative, because it is not analytic in any region that contains the path $\left[z_{1}, z_{2}, z_{3}\right]$. Instead, we will use a different branch of the logarithm. We know from Example 1(d) that $\log _{\alpha} z$ is an antiderivative of $\frac{1}{z}$ in the region $\Omega_{\alpha}$ (the plane minus the ray at angle $\alpha$ ). We can apply Theorem 1 if we choose $\alpha$ in such a way that
 the branch cut of $\log _{\alpha} z$ does not intersect the path $\left[z_{1}, z_{2}, z_{3}\right]$. Take, for example, $\alpha=0$; then $\log _{0} z=\ln |z|+i \arg _{0} z$, where $0<\arg _{0} z \leq 2 \pi$. By Theorem 1,
 
 
@@ -2243,10 +2358,18 @@
 $$
 
 
-> [!figure] Figure 5
-> 
-> ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-032_472_514_268_84.jpg)
-> Figure 5 A closed path starting and ending at $z_{1}$.
+```scientific-figure
+id: 7b10148d-e925-4307-957b-912b61fb8603
+numbered: false
+title: ""
+caption: "**Figure 5.** A closed path starting and ending at $z_{1}$."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-032_472_514_268_84.jpg
+    caption: ""
+```
 
 
 
@@ -2259,10 +2382,18 @@
 implying that $\int_{\gamma_{1}} f(z) d z=\int_{\gamma_{2}} f(z) d z$. Thus, the integral of $f$ is independent of path.
 
 
-> [!figure] Figure 6
-> 
-> ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-032_468_521_975_92.jpg)
-> Figure $6 \gamma_{1}$ followed by $\gamma_{2}$ yields the closed path $\Gamma$.
+```scientific-figure
+id: 3e1cd860-84cf-4582-a3d2-3ed2964590c0
+numbered: false
+title: ""
+caption: "**Figure 6.** Figure $6 \\gamma_{1}$ followed by $\\gamma_{2}$ yields the closed path $\\Gamma$."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-032_468_521_975_92.jpg
+    caption: ""
+```
 
 
 Combining this discussion with Theorem 1, we have the following useful theorem.
@@ -2270,7 +2401,8 @@
 
 
 
-> [!theorem] Theorem 2
+<!-- Source label: Theorem 2 -->
+> [!theorem] Equivalent Criteria for Path Independence of Complex Integrals
 > Let $f(z)$ be a continuous function defined in a region $\Omega$. Then the following are equivalent.
 > (i) $f(z)$ has an analytic antiderivative $F(z)$ in $\Omega$.
 > (ii) The integral of $f$ is independent of path.
@@ -2338,11 +2470,21 @@
 
 But Theorem 2 says that if a continuous function has an antiderivative on a region, then its integral is independent of path on that region. Hence $\overline{z}$ does not possess an antiderivative on any region that contains both paths $\left[z_1,z_2,z_3\right]$ and $\left[z_1,z_3\right]$.
 
-> [!figure] Python figure for Exercise 5(1)
-> 
-> ![](./images/exercise5_problem_a_python.png)
-> 
-> Figure 5(a). The polygonal path $\left[z_1,z_2,z_3\right]$ and the direct segment $\left[z_1,z_3\right]$ have the same endpoints.
+```scientific-figure
+id: 29bca6d9-4b2a-4105-9b79-154bb0f6ec64
+numbered: false
+title: ""
+caption: |-
+  **Figure 5.** Python figure for Exercise 5(1)
+
+  (a). The polygonal path $\left[z_1,z_2,z_3\right]$ and the direct segment $\left[z_1,z_3\right]$ have the same endpoints.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/exercise5_problem_a_python.png
+    caption: ""
+```
 
 A Mathematica plot for part (1) is:
 
@@ -2514,11 +2656,21 @@
 
 Therefore $\overline{z}$ does not possess an antiderivative on any region of $\mathbb{C}$.
 
-> [!figure] Python figure for Exercise 5(2)
-> 
-> ![](./images/exercise5_problem_b_python.png)
-> 
-> Figure 5(b). The same two paths have the same endpoints, but $\int \overline{z}\,dz$ takes different values on them.
+```scientific-figure
+id: e1045793-d65d-4f69-b5f7-947cccfb9a89
+numbered: false
+title: ""
+caption: |-
+  **Figure 5.** Python figure for Exercise 5(2)
+
+  (b). The same two paths have the same endpoints, but $\int \overline{z}\,dz$ takes different values on them.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/exercise5_problem_b_python.png
+    caption: ""
+```
 
 A Mathematica plot for part (2) is:
 
@@ -2932,10 +3084,18 @@
 because $\log (1+z)$ is an antiderivative of $\frac{1}{z+1}$ in the region $\mathbb{C} \backslash(-\infty,-1]$, which contains $C_{\frac{1}{2}}(0)$ (see _Figure 7_).
 
 
-> [!figure] Figure 7
-> 
-> ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-033_512_456_1048_32.jpg)
-> Figure 7 The branch cut of $\log (z+1)$ is obtained by translating to the left by one mit the branch cut of $\log z$.
+```scientific-figure
+id: f889f3d2-ecb6-4782-b94d-6d241c5e41e0
+numbered: false
+title: ""
+caption: "**Figure 7.** The branch cut of $\\log (z+1)$ is obtained by translating to the left by one mit the branch cut of $\\log z$."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-033_512_456_1048_32.jpg
+    caption: ""
+```
 
 
 (d) Let $z_{0}$ be a fixed point in the plane, $\gamma$ be a closed path in a region that does not go through $z_{0}$, and $n \geq 2$ be an integer. Then by Theorem 2,
@@ -2962,13 +3122,13 @@
 
 
 
-> [!lemma] Lemma 1
+<!-- Source label: Lemma 1 -->
+> [!lemma] Local Average of a Complex Function along a Shrinking Line Segment
 > Suppose $f(z)$ is continuous in a region $\Omega, z$ and $z+\Delta z$ are in $\Omega$, and the closed line segment $[z, z+\Delta z]$ is also in $\Omega$. Then
-> 
+>
 > $$
 > \lim _{\Delta z \rightarrow 0} \frac{1}{\Delta z} \int_{[z, z+\Delta z]} f(\zeta) d \zeta=f(z)
 > $$
-> 
 
 
 **Proof:** Parametrize $[z, z+\Delta z]$ by $\gamma(t)=(1-t) z+t(z+\Delta z)=z+t \Delta z$, where $0 \leq t \leq 1$. Then $\gamma^{\prime}(t)=\Delta z$ and hence $\int_{[z, z+\Delta z]} d \zeta=\int_{0}^{1} \Delta z d t=\Delta z$. So $\frac{1}{\Delta z} \int_{[z, z+\Delta z]} f(z) d \zeta=f(z)$, and
@@ -3014,9 +3174,18 @@
 $$
 
 
-> [!figure] Figure 8
-> ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-034_477_526_1664_95.jpg)
-> Figure 8
+```scientific-figure
+id: f64fa4e2-ebc7-41b0-9c3d-7615d3ef9a65
+numbered: false
+title: ""
+caption: "**Figure 8.**"
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-034_477_526_1664_95.jpg
+    caption: ""
+```
 
 
 For very small $\Delta z, z$ and $z+\Delta z$ are in $\Omega$, because $\Omega$ is open. So we can choose the path joining $z$ to $z+\Delta z$ to be the line segment $[z, z+\Delta z]$,
@@ -3084,11 +3253,21 @@
 \Omega=\mathbb{C}.
 $$
 
-> [!figure] Python figure for Exercise 7(1)
-> 
-> ![](./images/exercise7_problem1_python.svg)
-> 
-> Figure 7(1). The valid region is the whole plane $\Omega=\mathbb{C}$.
+```scientific-figure
+id: 2a304358-d6d2-484b-a5d4-bf2b7218a812
+numbered: false
+title: ""
+caption: |-
+  **Figure 7.** Python figure for Exercise 7(1)
+
+  (1). The valid region is the whole plane $\Omega=\mathbb{C}$.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/exercise7_problem1_python.svg
+    caption: ""
+```
 
 A Mathematica plot for problem (1) is:
 
@@ -3173,11 +3352,21 @@
 \Omega=\mathbb{C}.
 $$
 
-> [!figure] Python figure for Exercise 7(2)
-> 
-> ![](./images/exercise7_problem2_python.svg)
-> 
-> Figure 7(2). The valid region is again the whole plane $\Omega=\mathbb{C}$.
+```scientific-figure
+id: 1f6bd9b1-b677-4a22-8ed5-05478ded9d80
+numbered: false
+title: ""
+caption: |-
+  **Figure 7.** Python figure for Exercise 7(2)
+
+  (2). The valid region is again the whole plane $\Omega=\mathbb{C}$.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/exercise7_problem2_python.svg
+    caption: ""
+```
 
 A Mathematica plot for problem (2) is:
 
@@ -3254,11 +3443,21 @@
 \Omega=\mathbb{C}\setminus(-\infty,0].
 $$
 
-> [!figure] Python figure for Exercise 7(3)
-> 
-> ![](./images/exercise7_problem3_python.svg)
-> 
-> Figure 7(3). The principal-branch cut removes the nonpositive real axis.
+```scientific-figure
+id: 689a20b5-1478-4cdb-be82-e65481db6c75
+numbered: false
+title: ""
+caption: |-
+  **Figure 7.** Python figure for Exercise 7(3)
+
+  (3). The principal-branch cut removes the nonpositive real axis.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/exercise7_problem3_python.svg
+    caption: ""
+```
 
 A Mathematica plot for problem (3) is:
 
@@ -3336,11 +3535,21 @@
 \Omega=\mathbb{C}\setminus(-\infty,1].
 $$
 
-> [!figure] Python figure for Exercise 7(4)
-> 
-> ![](./images/exercise7_problem4_python.svg)
-> 
-> Figure 7(4). The principal-branch cut for $\log(z-1)$ is the ray $(-\infty,1]$.
+```scientific-figure
+id: e5101497-506f-4e07-841f-01b089c8f96d
+numbered: false
+title: ""
+caption: |-
+  **Figure 7.** Python figure for Exercise 7(4)
+
+  (4). The principal-branch cut for $\log(z-1)$ is the ray $(-\infty,1]$.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/exercise7_problem4_python.svg
+    caption: ""
+```
 
 A Mathematica plot for problem (4) is:
 
@@ -3481,11 +3690,21 @@
 \Omega=\mathbb{C}\setminus(-\infty,1].
 $$
 
-> [!figure] Python figure for Exercise 7(5)
-> 
-> ![](./images/exercise7_problem5_python.svg)
-> 
-> Figure 7(5). The same shifted branch cut $(-\infty,1]$ works for both logarithms in the antiderivative.
+```scientific-figure
+id: 395a3210-8d8c-46aa-bb3f-7625db54f5b6
+numbered: false
+title: ""
+caption: |-
+  **Figure 7.** Python figure for Exercise 7(5)
+
+  (5). The same shifted branch cut $(-\infty,1]$ works for both logarithms in the antiderivative.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/exercise7_problem5_python.svg
+    caption: ""
+```
 
 A Mathematica plot for problem (5) is:
 
@@ -3562,11 +3781,21 @@
 
 On this strip, $\cos z\ne 0$, so $\tan z$ is analytic there. Therefore $\tan z$ is an antiderivative of $\sec^2 z$ on this region.
 
-> [!figure] Python figure for Exercise 7(6)
-> 
-> ![](./images/exercise7_problem6_python.svg)
-> 
-> Figure 7(6). One convenient connected region is the strip $-\frac{\pi}{2}<\operatorname{Re}z<\frac{\pi}{2}$.
+```scientific-figure
+id: 4fcf92d8-5954-443b-964a-dd7cc4d24df3
+numbered: false
+title: ""
+caption: |-
+  **Figure 7.** Python figure for Exercise 7(6)
+
+  (6). One convenient connected region is the strip $-\frac{\pi}{2}<\operatorname{Re}z<\frac{\pi}{2}$.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/exercise7_problem6_python.svg
+    caption: ""
+```
 
 A Mathematica plot for problem (6) is:
 
@@ -3645,11 +3874,21 @@
 \Omega=\mathbb{C}.
 $$
 
-> [!figure] Python figure for Exercise 7(7)
-> 
-> ![](./images/exercise7_problem7_python.svg)
-> 
-> Figure 7(7). The valid region is the whole plane $\Omega=\mathbb{C}$.
+```scientific-figure
+id: 327dbe1b-5836-4a63-8ba1-843273b09bfc
+numbered: false
+title: ""
+caption: |-
+  **Figure 7.** Python figure for Exercise 7(7)
+
+  (7). The valid region is the whole plane $\Omega=\mathbb{C}$.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/exercise7_problem7_python.svg
+    caption: ""
+```
 
 A Mathematica plot for problem (7) is:
 
@@ -3729,11 +3968,21 @@
 \Omega=\mathbb{C}\setminus(-\infty,0].
 $$
 
-> [!figure] Python figure for Exercise 7(8)
-> 
-> ![](./images/exercise7_problem8_python.svg)
-> 
-> Figure 7(8). The logarithm term forces the principal-branch cut $(-\infty,0]$.
+```scientific-figure
+id: e29b6b6f-e1b6-458d-ad1d-87b6b17e4f8f
+numbered: false
+title: ""
+caption: |-
+  **Figure 7.** Python figure for Exercise 7(8)
+
+  (8). The logarithm term forces the principal-branch cut $(-\infty,0]$.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/exercise7_problem8_python.svg
+    caption: ""
+```
 
 A Mathematica plot for problem (8) is:
 
@@ -3808,11 +4057,21 @@
 \Omega=\mathbb{C}.
 $$
 
-> [!figure] Python figure for Exercise 7(9)
-> 
-> ![](./images/exercise7_problem9_python.svg)
-> 
-> Figure 7(9). The valid region is the whole plane $\Omega=\mathbb{C}$.
+```scientific-figure
+id: d1cc46c7-d1e6-4d27-80cd-0cf3cfe4c03a
+numbered: false
+title: ""
+caption: |-
+  **Figure 7.** Python figure for Exercise 7(9)
+
+  (9). The valid region is the whole plane $\Omega=\mathbb{C}$.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/exercise7_problem9_python.svg
+    caption: ""
+```
 
 A Mathematica plot for problem (9) is:
 
@@ -3895,11 +4154,21 @@
 \Omega=\mathbb{C}.
 $$
 
-> [!figure] Python figure for Exercise 7(10)
-> 
-> ![](./images/exercise7_problem10_python.svg)
-> 
-> Figure 7(10). The valid region is the whole plane $\Omega=\mathbb{C}$.
+```scientific-figure
+id: e4757be4-a4c8-4eb3-8091-ed3e6cebd008
+numbered: false
+title: ""
+caption: |-
+  **Figure 7.** Python figure for Exercise 7(10)
+
+  (10). The valid region is the whole plane $\Omega=\mathbb{C}$.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/exercise7_problem10_python.svg
+    caption: ""
+```
 
 A Mathematica plot for problem (10) is:
 
@@ -3986,11 +4255,21 @@
 \Omega=\mathbb{C}\setminus(-\infty,0].
 $$
 
-> [!figure] Python figure for Exercise 7(11)
-> 
-> ![](./images/exercise7_problem11_python.svg)
-> 
-> Figure 7(11). The logarithm term again forces the principal-branch cut $(-\infty,0]$.
+```scientific-figure
+id: 3e277d4e-e920-42a5-bf80-a3a69be13fe6
+numbered: false
+title: ""
+caption: |-
+  **Figure 7.** Python figure for Exercise 7(11)
+
+  (11). The logarithm term again forces the principal-branch cut $(-\infty,0]$.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/exercise7_problem11_python.svg
+    caption: ""
+```
 
 A Mathematica plot for problem (11) is:
 
@@ -4079,11 +4358,21 @@
 \Omega=\Omega_\alpha.
 $$
 
-> [!figure] Python figure for Exercise 7(12)
-> 
-> ![](./images/exercise7_problem12_python.svg)
-> 
-> Figure 7(12). An illustrative branch cut for $\Omega_\alpha$, shown here with the sample choice $\alpha=\pi/4$.
+```scientific-figure
+id: 614423bc-484b-49ac-aa3f-43b34b6b32c6
+numbered: false
+title: ""
+caption: |-
+  **Figure 7.** Python figure for Exercise 7(12)
+
+  (12). An illustrative branch cut for $\Omega_\alpha$, shown here with the sample choice $\alpha=\pi/4$.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/exercise7_problem12_python.svg
+    caption: ""
+```
 
 A Mathematica plot for problem (12) is:
 
@@ -4204,11 +4493,21 @@
 \Omega=\Omega_0\cap \Omega_{\pi/2}.
 $$
 
-> [!figure] Python figure for Exercise 7(13)
-> 
-> ![](./images/exercise7_problem13_python.svg)
-> 
-> Figure 7(13). The common region removes both the positive real axis and the positive imaginary axis.
+```scientific-figure
+id: 64b1dff8-df36-4182-9c8e-31dfb21e8a79
+numbered: false
+title: ""
+caption: |-
+  **Figure 7.** Python figure for Exercise 7(13)
+
+  (13). The common region removes both the positive real axis and the positive imaginary axis.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/exercise7_problem13_python.svg
+    caption: ""
+```
 
 A Mathematica plot for problem (13) is:
 
@@ -4264,11 +4563,21 @@
 \Omega=\mathbb{C}\setminus(-\infty,0].
 $$
 
-> [!figure] Python figure for Exercise 7(14)
-> 
-> ![](./images/exercise7_problem14_python.svg)
-> 
-> Figure 7(14). The principal branch of $z^{1/5}$ uses the same branch cut $(-\infty,0]$.
+```scientific-figure
+id: b579649a-f3a2-43fa-a41e-3deaf8f0652c
+numbered: false
+title: ""
+caption: |-
+  **Figure 7.** Python figure for Exercise 7(14)
+
+  (14). The principal branch of $z^{1/5}$ uses the same branch cut $(-\infty,0]$.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/exercise7_problem14_python.svg
+    caption: ""
+```
 
 A Mathematica plot for problem (14) is:
 

`````
