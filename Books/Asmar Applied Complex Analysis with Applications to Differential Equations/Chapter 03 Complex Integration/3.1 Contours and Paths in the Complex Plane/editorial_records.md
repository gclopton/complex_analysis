
# Editorial records

Reading note: 3.1 Contours and Paths in the Complex Plane.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Callout 76: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!definition] Piecewise Continuous and Piecewise Smooth Complex-Valued Functions
> A complex-valued function $f$ of a real variable is piecewise continuous on $[a,b]$ if it is continuous except at finitely many points of $(a,b)$, has finite one-sided limits $\lim_{t\to c^-}f(t)$ and $\lim_{t\to c^+}f(t)$ at each interior discontinuity, and has finite endpoint limits $\lim_{t\to a^+}f(t)$ and $\lim_{t\to b^-}f(t)$.
>
> It is piecewise smooth if $f$ and its derivative on the smooth pieces are both piecewise continuous.
````
### After

````text
> [!definition] Piecewise Continuous and Piecewise Smooth Functions
> A complex-valued function of a real variable $f(t)$ is said to be piecewise continuous on $[a, b]$ if the following hold:
> (i) $f(t)$ exists and is continuous for all but finitely many points in $(a, b)$.
> (ii) At any point $c$ in $(a, b)$ where $f$ fails to be continuous, both the left limit $\lim_{t\to c^-}f(t)$ and the right limit $\lim_{t\to c^+}f(t)$ exist and are finite.
> (iii) At the endpoints, the right limit $\lim_{t\to a^+} f(t)$ and the left limit $\lim_{t\to b^-} f(t)$ exist and are finite.
> The function $f(t)$ is said to be piecewise smooth on $[a, b]$ if $f$ and $f^{\prime}$ are both piecewise continuous on $[a, b]$.
````

## 2. Callout 77: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!definition] Complex Path or Contour
> By a path or a contour we mean a continuous piecewise smooth curve $\gamma(t)$ over a closed interval $[a, b]$.
````
### After

````text
> [!definition] Path or Contour
> By a path or a contour we mean a continuous piecewise smooth curve $\gamma(t)$ over a closed interval $[a, b]$.
````

## 3. Move editorial commentary out of the reading note.

### Before

````text
*Editorial note: Restored missing one-sided limit directions and corrected OCR punctuation.*
````
### After

````text

````

## Source-to-current comparison

Source: /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 03 Complex Integration/3.1 Contours and Paths in the Complex Plane.md

This exact comparison preserves the full change evidence, including formatting, OCR corrections, restored source wording, and required standalone context. The entries above explain the recovery edits. The comparison is not a claim that every difference is a correction; component serialization, callout wrapping, and printed labels outside callouts are formatting.

`````diff
--- /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 03 Complex Integration/3.1 Contours and Paths in the Complex Plane.md
+++ /Users/gradyclopton/ObsidianVaults/complex_analysis/Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/3.1 Contours and Paths in the Complex Plane.md
@@ -132,7 +132,7 @@
 ##### problem 2(c)
 
 
-![](Pasted%20image%2020260426012132.png)
+![](Books/Asmar%20Applied%20Complex%20Analysis%20with%20Applications%20to%20Differential%20Equations/Chapter%2003%20Complex%20Integration/images/Pasted%20image%2020260426012132.png)
 
 
 ```python title:""
@@ -160,7 +160,7 @@
 ##### problem 2(d)
 
 
-![](Pasted%20image%2020260426012541.png)
+![](Books/Asmar%20Applied%20Complex%20Analysis%20with%20Applications%20to%20Differential%20Equations/Chapter%2003%20Complex%20Integration/images/Pasted%20image%2020260426012541.png)
 
 
 
@@ -178,7 +178,7 @@
 
 
 
-![](Pasted%20image%2020260426013602.png)
+![](Books/Asmar%20Applied%20Complex%20Analysis%20with%20Applications%20to%20Differential%20Equations/Chapter%2003%20Complex%20Integration/images/Pasted%20image%2020260426013602.png)
 
 
 
@@ -431,10 +431,18 @@
 
 
 
-> [!figure] Figure 1
-> 
-> ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-002_458_527_332_74.jpg)
-> Figure 1
+```scientific-figure
+id: c2992f62-8a01-4c58-a270-2facc6b90afc
+numbered: false
+title: ""
+caption: "**Figure 1.**"
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-002_458_527_332_74.jpg
+    caption: ""
+```
 
 
 
@@ -442,11 +450,18 @@
 
 
 
-> [!figure] Figure 2
-> 
-> ![500](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-002_466_1102_860_730.jpg)
-> 
-> Figure 2 A parametric interval mapping to a curve.
+```scientific-figure
+id: db693f96-c196-488d-90f0-b5f611bd69a8
+numbered: false
+title: ""
+caption: "**Figure 2.** A parametric interval mapping to a curve."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-002_466_1102_860_730.jpg
+    caption: ""
+```
 
 
 
@@ -455,10 +470,18 @@
 Let $\gamma(t), a \leq t \leq b$, be a parametrization of a curve. As $t$ varies from $a$ to $b$ the point $\gamma(t)$ traces the curve in a specific direction, starting with $\gamma(a)$, the initial point of $\gamma$, and ending at $\gamma(b)$, the terminal point of $\gamma$. For continuous curves, this direction is usually denoted by an arrow on the curve. A curve is closed if $\gamma(a)=\gamma(b)$. For circles and circular arcs, if the arrow points in the counterclockwise direction, we will say that the curve has positive orientation. Curves traversed in the clockwise direction have negative orientation (see _Figure 3_).
 
 
-> [!figure] Figure 3
-> 
-> ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-002_476_542_1601_74.jpg)
-> Figure 3 Negative and positive orientation.
+```scientific-figure
+id: 2657fe35-5530-4924-874f-d9dab0ccac6f
+numbered: false
+title: ""
+caption: "**Figure 3.** Negative and positive orientation."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-002_476_542_1601_74.jpg
+    caption: ""
+```
 
 
 Since $z=x+i y$, it makes sense to adopt the notation $z(t)=x(t)+i y(t)$. In particular, we can write the parametric form of a curve $\gamma$ using complex notation as
@@ -495,11 +518,21 @@
 
 The initial point is $\gamma\!\left(\frac{\pi}{6}\right)=e^{i\pi/6}$, and the terminal point is $\gamma\!\left(\frac{2\pi}{3}\right)=e^{i2\pi/3}$.
 
-> [!figure] Python figure for Problem 1
-> 
-> ![](./images/exercise1_problem1_python.png)
-> 
-> The Python rendering is intentionally minimal: it shows the geometry and the counterclockwise direction without trying to duplicate every annotation from the text.
+```scientific-figure
+id: b9ad092a-9951-482e-a4c0-1c4d64a6b708
+numbered: false
+title: ""
+caption: |-
+  Python figure for Problem 1
+
+  The Python rendering is intentionally minimal: it shows the geometry and the counterclockwise direction without trying to duplicate every annotation from the text.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/exercise1_problem1_python.png
+    caption: ""
+```
 
 A Mathematica plot of this arc, with an arrow showing the positive orientation, is:
 
@@ -662,11 +695,21 @@
 v(t)=-3+4\sin t.
 $$
 
-> [!figure] Python figure for Problem 2
-> 
-> ![](./images/exercise1_problem2_python.png)
-> 
-> The Python rendering keeps only the center, one distinguished point, and the orientation.
+```scientific-figure
+id: bb502a6f-ac7e-45eb-9515-274f0f3ed3f3
+numbered: false
+title: ""
+caption: |-
+  Python figure for Problem 2
+
+  The Python rendering keeps only the center, one distinguished point, and the orientation.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/exercise1_problem2_python.png
+    caption: ""
+```
 
 A Mathematica plot of this circle is:
 
@@ -731,11 +774,21 @@
 
 This has the standard form $\gamma(t)=z_0+Re^{it}$ with $z_0=-1+i$ and $R=3$. Therefore the curve is the positively oriented circle centered at $-1+i$ with radius $3$.
 
-> [!figure] Python figure for Problem 3
-> 
-> ![](./images/exercise1_problem3_python.png)
-> 
-> The Python rendering is stripped down to the center and the direction of traversal.
+```scientific-figure
+id: 541fe892-3700-4bff-a01b-dae7db6867c8
+numbered: false
+title: ""
+caption: |-
+  Python figure for Problem 3
+
+  The Python rendering is stripped down to the center and the direction of traversal.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/exercise1_problem3_python.png
+    caption: ""
+```
 
 A Mathematica plot of this circle is:
 
@@ -813,11 +866,21 @@
 
 The initial point is $\gamma(0)=1+i=z_1$, and the terminal point is $\gamma(1)=4-2i=z_2$.
 
-> [!figure] Python figure for Problem 4
-> 
-> ![](./images/exercise1_problem4_python.png)
-> 
-> The Python rendering keeps the segment itself and its direction, with only the endpoint labels retained.
+```scientific-figure
+id: b4eb1fdd-9a54-46fe-8925-1ee7bcf199e2
+numbered: false
+title: ""
+caption: |-
+  Python figure for Problem 4
+
+  The Python rendering keeps the segment itself and its direction, with only the endpoint labels retained.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/exercise1_problem4_python.png
+    caption: ""
+```
 
 A Mathematica plot of this directed line segment is:
 
@@ -875,11 +938,21 @@
 
 
 
-> [!figure] Figure 4a
-> 
-> ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-003_484_487_172_58.jpg)
-> 
-> Figure 4(a) A positively oriented arc with initial point $e^{i \alpha}$ and terminal point $e^{i \beta}$.
+```scientific-figure
+id: 4edc7600-f5a6-4812-8fc4-f5ac5d20553f
+numbered: false
+title: ""
+caption: |-
+  **Figure 4.** a
+
+  (a) A positively oriented arc with initial point $e^{i \alpha}$ and terminal point $e^{i \beta}$.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-003_484_487_172_58.jpg
+    caption: ""
+```
 
 
 
@@ -892,12 +965,21 @@
 The circle is a closed curve with initial point $\gamma(0)=1$ and terminal point $\gamma(2 \pi)=1$. 
 
 
-> [!figure] Figure 4b
-> 
-> 
-> ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-003_485_489_813_52.jpg)
-> 
-> Figure 4(b) A positively oriented circle.
+```scientific-figure
+id: b96e15f8-384b-4ffb-8411-cc85ed93a197
+numbered: false
+title: ""
+caption: |-
+  **Figure 4.** b
+
+  (b) A positively oriented circle.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-003_485_489_813_52.jpg
+    caption: ""
+```
 
 
 (c) The circle in _Figure 4(c)_ is centered at $z_{0}$ with radius $R>0$. We obtain its parametrization by dilating and then translating the equation in (b). This gives
@@ -917,11 +999,21 @@
 
 
 
-> [!figure] Figure 4c
-> 
-> ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-003_481_477_1388_48.jpg)
-> 
-> Figure 4(c) Dilating and then translating a circle.
+```scientific-figure
+id: 1b919e38-77bd-4bc1-b0d4-03d6f46f8e6a
+numbered: false
+title: ""
+caption: |-
+  **Figure 4.** c
+
+  (c) Dilating and then translating a circle.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-003_481_477_1388_48.jpg
+    caption: ""
+```
 
 
 
@@ -996,11 +1088,21 @@
 $x(t)=8\cos t+5\cos 4t$ and
 $y(t)=8\sin t-5\sin 4t$.
 
-> [!figure] Python figure for Exercise 2
-> 
-> ![](./images/exercise2_hypotrochoid_python.png)
-> 
-> This Python rendering uses $a=8$, $b=5$, and equal scaling in the horizontal and vertical directions so the curve is not distorted.
+```scientific-figure
+id: 077aa764-0db7-4998-9d52-bb12dbdf6320
+numbered: false
+title: ""
+caption: |-
+  Python figure for Exercise 2
+
+  This Python rendering uses $a=8$, $b=5$, and equal scaling in the horizontal and vertical directions so the curve is not distorted.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/exercise2_hypotrochoid_python.png
+    caption: ""
+```
 
 A Mathematica plot of this hypotrochoid is:
 
@@ -1123,10 +1225,21 @@
 
 
 
-> [!figure] Figure 5: For exercise 2
-> 
-> ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-003_493_481_1967_36.jpg)
-> Figure 5 A hypotrochoid.
+```scientific-figure
+id: f21b727c-9253-44a8-b402-06a72482cf48
+numbered: false
+title: ""
+caption: |-
+  **Figure 5.** For exercise 2
+
+  A hypotrochoid.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-003_493_481_1967_36.jpg
+    caption: ""
+```
 
 
 
@@ -1667,12 +1780,18 @@
 Having stated properties of the derivative of a real-valued function that hold for complex-valued functions of a real variable, we should caution you that not all properties of derivatives that hold in the real case hold in the complex case. Most notably, the mean value property does not hold for complex-valued functions. In the real case, the mean value property states that if $f$ is continuous on $[a, b]$ and differentiable on $(a, b)$, then $f(b)-f(a)= f^{\prime}(c)(b-a)$ for some $c$ in $(a, b)$. This property does not hold for complexvalued functions. To see this, consider $f(x)=e^{i x}$ for $x$ in $[0,2 \pi]$. Then $f$ is continuous on $[0,2 \pi]$ and has a derivative $f^{\prime}(x)=i e^{i x}$ on $(0,2 \pi)$. Also, $f(2 \pi)-f(0)=1-1=0$, but $f^{\prime}(x)$ never vanishes since $\left|f^{\prime}(x)\right|=\left|i e^{i x}\right|= \left|e^{i x}\right|=1$. Hence there is no number $c$ in $(0,2 \pi)$ such that $f(2 \pi)-f(0)= (2 \pi-0) f^{\prime}(c)$, and so the mean value property does not hold (_Figure 6_).
 
 
-> [!figure] Figure 6
-> 
-> 
-> ![[Pasted image 20260401051005.png|500]]
-> 
-> Figure $6 f(2 \pi)-f(0)=0$, but $f^{\prime}(x) \neq 0$ for all $x$ in ( $0,2 \pi$ ) showing that the mean value property fails for complex-valued functions.
+```scientific-figure
+id: a24f3483-c2bc-4a52-98be-62e7fe465dd2
+numbered: false
+title: ""
+caption: "**Figure 6.** Figure $6 f(2 \\pi)-f(0)=0$, but $f^{\\prime}(x) \\neq 0$ for all $x$ in ( $0,2 \\pi$ ) showing that the mean value property fails for complex-valued functions."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Pasted image 20260401051005.png
+    caption: ""
+```
 
 
 
@@ -1747,11 +1866,21 @@
 
 So $\gamma$ is a continuous piecewise-smooth curve over the closed interval $[-2,2]$. Therefore $\gamma$ is a path in the sense of Definition 2.
 
-> [!figure] Python figure for Exercise 5
-> 
-> ![](./images/exercise5_path_python.png)
-> 
-> The figure uses equal scaling, so the middle piece is a true upper semicircle rather than a stretched arc.
+```scientific-figure
+id: 736920eb-beeb-426d-abad-bc13e2f5dc84
+numbered: false
+title: ""
+caption: |-
+  Python figure for Exercise 5
+
+  The figure uses equal scaling, so the middle piece is a true upper semicircle rather than a stretched arc.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/exercise5_path_python.png
+    caption: ""
+```
 
 A Mathematica plot of this path is:
 
@@ -1932,22 +2061,22 @@
 Returning to our discussion of complex-valued functions of a real variable. we introduce the following useful definitions.
 
 
-> [!definition] Definition 1: Piecewise Continuous and Piecewise Smooth Functions
+<!-- Source label: Definition 1: Piecewise Continuous and Piecewise Smooth Functions -->
+> [!definition] Piecewise Continuous and Piecewise Smooth Functions
 > A complex-valued function of a real variable $f(t)$ is said to be piecewise continuous on $[a, b]$ if the following hold:
 > (i) $f(t)$ exists and is continuous for all but finitely many points in $(a, b)$.
-> (ii) At any point $c$ in $(a, b)$ where $f$ fails to be continuous. both the left limit $\lim f(t)$ and the right limit $\lim f(t)$ exist and are finite.
-> (iii) At the endpoints, the right limit $\lim _{t, a} f(t)$ and the left limit $\lim _{t \mid b} f(t)$ exist and are finite.
+> (ii) At any point $c$ in $(a, b)$ where $f$ fails to be continuous, both the left limit $\lim_{t\to c^-}f(t)$ and the right limit $\lim_{t\to c^+}f(t)$ exist and are finite.
+> (iii) At the endpoints, the right limit $\lim_{t\to a^+} f(t)$ and the left limit $\lim_{t\to b^-} f(t)$ exist and are finite.
 > The function $f(t)$ is said to be piecewise smooth on $[a, b]$ if $f$ and $f^{\prime}$ are both piecewise continuous on $[a, b]$.
 
 
-
-
 If $f$ and $f^{\prime}$ are both continuous on $[a, b]$ we will say that $f$ is smooth or continuously differentiable on $[a, b]$.
 
 We are now in a position to introduce the notion of path, which is fundamental to our development of the theory of integration. Recall that we have referred to a curve by its parametrization $\gamma(t)$. In addition, we will attribute to the curve the analytical properties of the function $\gamma(t)$, such as continuity and differentiability. Thus, when we talk about a continuous curve or a differentiable curve, we have in mind a specific parametrization with these properties.
 
 
-> [!definition] Definition 2: Path or Contour
+<!-- Source label: Definition 2: Path or Contour -->
+> [!definition] Path or Contour
 > By a path or a contour we mean a continuous piecewise smooth curve $\gamma(t)$ over a closed interval $[a, b]$.
 
 A path $\gamma$ is continuously differentiable or smooth on $[a, b]$ if $\gamma(t)$ and $\gamma^{\prime}(t)$ are continuous on $[a, b]$. Thus, according to Definition 2, a path or a contour $\gamma$ is a finite sequence of continuously differentiable curves, $\gamma_{1}, \gamma_{2}, \ldots, \gamma_{n}$, joined together end-to-end. In this case, it is sometimes convenient to write $\gamma=\left(\gamma_{1}, \gamma_{2}, \ldots, \gamma_{n}\right)$. The path is closed if the initial point of $\gamma_{1}$ is joined to the terminal point of $\gamma_{n}$.
@@ -2018,11 +2147,21 @@
 
 
 
-> [!figure] Python figure for Exercise 5
-> 
-> ![](./images/exercise5_path_python.png)
-> 
-> The figure uses equal scaling, so the middle piece is a true upper semicircle.
+```scientific-figure
+id: a68d9fbf-29a2-4540-bfae-0192bb8f9452
+numbered: false
+title: ""
+caption: |-
+  Python figure for Exercise 5
+
+  The figure uses equal scaling, so the middle piece is a true upper semicircle.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/exercise5_path_python.png
+    caption: ""
+```
 
 A Mathematica plot of this path is:
 
@@ -2156,9 +2295,21 @@
 
 
 
-> [!figure] Figure 7: For exercise 5
-> ![](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-007_469_463_1111_48.jpg)
-> Figure 7 for Example 5.
+```scientific-figure
+id: a1e6783a-c4d3-4188-a277-0e79ca219040
+numbered: false
+title: ""
+caption: |-
+  **Figure 7.** For exercise 5
+
+  for Example 5.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-007_469_463_1111_48.jpg
+    caption: ""
+```
 
 
 
@@ -2262,11 +2413,21 @@
 
 Each piece is a line segment, hence smooth on its own subinterval. Therefore $\gamma$ is continuous and piecewise smooth on $[0,1]$, so it is a path in the sense of Definition 2.
 
-> [!figure] Python figure for Exercise 6
-> 
-> ![](./images/exercise6_polygonal_path_python.png)
-> 
-> The figure uses equal scaling, so the polygonal path is not distorted.
+```scientific-figure
+id: e6093939-083e-401d-a205-90db348c413c
+numbered: false
+title: ""
+caption: |-
+  Python figure for Exercise 6
+
+  The figure uses equal scaling, so the polygonal path is not distorted.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/exercise6_polygonal_path_python.png
+    caption: ""
+```
 
 A Mathematica plot of this closed polygonal path is:
 
@@ -2423,11 +2584,21 @@
 We can now use these equations to parametrize $\gamma$ over a closed interval, say $[0,1$. This can be done by reparanetrizing $\gamma_{1}$ over $\left[0, \frac{1}{3}\right], \gamma_{2}$ over $\left[\frac{1}{3}, \frac{2}{3}\right], \gamma_{3}$ over $\left[\frac{2}{3}, 1\right]$, and
 
 
-> [!figure] Figure 8: For Exercise 6
-> 
-> ![](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-007_483_453_1782_40.jpg)
-> 
-> Eigure 8 for Example 6.
+```scientific-figure
+id: b4ac275f-e82b-40fb-818b-b88fd59577b8
+numbered: false
+title: ""
+caption: |-
+  **Figure 8.** For Exercise 6
+
+  Eigure 8 for Example 6.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-007_483_453_1782_40.jpg
+    caption: ""
+```
 
 
 
@@ -2436,10 +2607,18 @@
 then pasting the three equations to form the path $\gamma$ (_Figure 9_). 
 
 
-> [!figure] Figure 9
-> 
-> ![](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-008_470_510_325_124.jpg)
-> Figure 9 for Example 6.
+```scientific-figure
+id: add08f4a-3d94-4cdf-8bc6-81486c9b109e
+numbered: false
+title: ""
+caption: "**Figure 9.** for Example 6."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-008_470_510_325_124.jpg
+    caption: ""
+```
 
 
 To parametrize $\gamma_{1}$ over $\left[0, \frac{1}{3}\right]$, it suffices to change $t$ to $3 t$. This yields
@@ -2551,10 +2730,21 @@
 
 
 
-> [!figure] Figure 10: For Example 7a
-> 
-> ![](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-008_429_487_1069_155.jpg)
-> Figure 10 A path that degenerates to a point.
+```scientific-figure
+id: f053bad2-6296-42c3-ab33-e6abf5a478cd
+numbered: false
+title: ""
+caption: |-
+  **Figure 10.** For Example 7a
+
+  A path that degenerates to a point.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-008_429_487_1069_155.jpg
+    caption: ""
+```
 
 
 (b) Points on the path $\gamma_{2}(t)$ are on the circle of radius $R$, centered at the origin.
@@ -2563,11 +2753,21 @@
 
 
 
-> [!figure] Figure 11: For Example 7b
-> 
-> 
-> ![](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-008_474_534_1737_112.jpg)
-> Figure 11 A doubly traced circle.
+```scientific-figure
+id: abf0d347-a507-470f-82bd-48711fdc3b7a
+numbered: false
+title: ""
+caption: |-
+  **Figure 11.** For Example 7b
+
+  A doubly traced circle.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-008_474_534_1737_112.jpg
+    caption: ""
+```
 
 
 The path $\gamma_{1}(t)$ traces around the circle only once. The two paths are not the same but have the same graphs. $\square$
@@ -2731,10 +2931,18 @@
 
 
 
-> [!figure] Figure 12
-> 
-> ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-009_690_471_185_51.jpg)
-> Figure $12 f(t)$ is continuous and even differentiable, but its graph is not a path.
+```scientific-figure
+id: 750b7671-5177-473f-8fa9-18c8c5c0708e
+numbered: false
+title: ""
+caption: "**Figure 12.** Figure $12 f(t)$ is continuous and even differentiable, but its graph is not a path."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-009_690_471_185_51.jpg
+    caption: ""
+```
 
 
 
@@ -2761,30 +2969,52 @@
 > 9. The contour in Figure 13.
 > 
 > 
-> > [!figure] Figure 13
-> > 
-> > ![](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-009_472_465_1150_43.jpg)
-> > Figure 13 Arc of a circle with center at $-3+2 i$ and radius 5 .
+> ```scientific-figure
+> id: d68f733a-a6a1-4545-81fc-30382c2bdbaf
+> numbered: false
+> title: ""
+> caption: "**Figure 13.** Arc of a circle with center at $-3+2 i$ and radius 5 ."
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-009_472_465_1150_43.jpg
+>     caption: ""
+> ```
 > 
 > 
 > 10. The contour in _Figure 14_.
 > 
 > 
-> > [!figure] Figure 14
-> > 
-> > 
-> > ![](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-009_482_457_1759_37.jpg)
-> > Figure 14 Arc of a circle with center at 0 and radius 2 .
+> ```scientific-figure
+> id: 1c556725-c230-4402-a0bb-f2f1c4e72f85
+> numbered: false
+> title: ""
+> caption: "**Figure 14.** Arc of a circle with center at 0 and radius 2 ."
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-009_482_457_1759_37.jpg
+>     caption: ""
+> ```
 > 
 > 
 > 
 > 11. The contour in _Figure 15_.
 > 
-> > [!figure] Figure 15
-> > 
-> > ![[Screenshot 2026-04-01 at 5.42.59 AM.png]]
-> > 
-> > Figure 15 Arc of a parabola for Exercise 11.
+> ```scientific-figure
+> id: 137fd414-4c48-4a6f-856d-d6d58820a848
+> numbered: false
+> title: ""
+> caption: "**Figure 15.** Arc of a parabola for Exercise 11."
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Screenshot 2026-04-01 at 5.42.59 AM.png
+>     caption: ""
+> ```
 > 
 > 
 > 
@@ -2820,11 +3050,21 @@
 0\le t\le 1.
 $$
 
-> [!figure] Python figure for Problem 1
-> 
-> ![](./images/exercise9_problem1_python.png)
-> 
-> Equal scaling is used, so the line segment is not distorted.
+```scientific-figure
+id: 160e16a1-8e0a-4a90-bfc5-4cc06b7b7601
+numbered: false
+title: ""
+caption: |-
+  Python figure for Problem 1
+
+  Equal scaling is used, so the line segment is not distorted.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/exercise9_problem1_python.png
+    caption: ""
+```
 
 ```Mathematica title:"Problem 1: Mathematica plot"
 ParametricPlot[
@@ -2904,11 +3144,21 @@
 0\le t\le 1.
 $$
 
-> [!figure] Python figure for Problem 2
-> 
-> ![](./images/exercise9_problem2_python.png)
-> 
-> Equal scaling is used, so the segment has the correct slope.
+```scientific-figure
+id: 9a506100-1c55-4974-b9df-4a03f3d8d646
+numbered: false
+title: ""
+caption: |-
+  Python figure for Problem 2
+
+  Equal scaling is used, so the segment has the correct slope.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/exercise9_problem2_python.png
+    caption: ""
+```
 
 ```Mathematica title:"Problem 2: Mathematica plot"
 ParametricPlot[
@@ -2987,11 +3237,21 @@
 0\le t\le 2\pi.
 $$
 
-> [!figure] Python figure for Problem 3
-> 
-> ![](./images/exercise9_problem3_python.png)
-> 
-> Equal scaling is used, so the circle is not stretched.
+```scientific-figure
+id: 4e6d8283-c7b7-4f78-b03e-ee642728aa01
+numbered: false
+title: ""
+caption: |-
+  Python figure for Problem 3
+
+  Equal scaling is used, so the circle is not stretched.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/exercise9_problem3_python.png
+    caption: ""
+```
 
 ```Mathematica title:"Problem 3: Mathematica plot"
 Graphics[
@@ -3072,11 +3332,21 @@
 0\le t\le 2\pi.
 $$
 
-> [!figure] Python figure for Problem 4
-> 
-> ![](./images/exercise9_problem4_python.png)
-> 
-> Equal scaling is used, so the circle is not stretched.
+```scientific-figure
+id: 23d8e346-2ad1-4320-86be-0ec2100d38c4
+numbered: false
+title: ""
+caption: |-
+  Python figure for Problem 4
+
+  Equal scaling is used, so the circle is not stretched.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/exercise9_problem4_python.png
+    caption: ""
+```
 
 ```Mathematica title:"Problem 4: Mathematica plot"
 Graphics[
@@ -3150,11 +3420,21 @@
 -\frac{\pi}{4}\le t\le \frac{\pi}{4}.
 $$
 
-> [!figure] Python figure for Problem 5
-> 
-> ![](./images/exercise9_problem5_python.png)
-> 
-> Equal scaling is used, so the unit-circle arc is not distorted.
+```scientific-figure
+id: d685a817-151a-4fc1-b75f-9d77a405e12f
+numbered: false
+title: ""
+caption: |-
+  Python figure for Problem 5
+
+  Equal scaling is used, so the unit-circle arc is not distorted.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/exercise9_problem5_python.png
+    caption: ""
+```
 
 ```Mathematica title:"Problem 5: Mathematica plot"
 Graphics[
@@ -3225,11 +3505,21 @@
 
 This traces the same geometric arc, but in the clockwise direction.
 
-> [!figure] Python figure for Problem 6
-> 
-> ![](./images/exercise9_problem6_python.png)
-> 
-> Equal scaling is used, so the unit-circle arc is not distorted.
+```scientific-figure
+id: 3a80b374-eb27-4425-9385-e918e5b26773
+numbered: false
+title: ""
+caption: |-
+  Python figure for Problem 6
+
+  Equal scaling is used, so the unit-circle arc is not distorted.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/exercise9_problem6_python.png
+    caption: ""
+```
 
 ```Mathematica title:"Problem 6: Mathematica plot"
 Graphics[
@@ -3340,11 +3630,21 @@
 \end{cases}
 $$
 
-> [!figure] Python figure for Problem 7
-> 
-> ![](./images/exercise9_problem7_python.png)
-> 
-> Equal scaling is used, so the polygonal path is not distorted.
+```scientific-figure
+id: 15622867-9101-451c-a1a0-ff229fc43b8a
+numbered: false
+title: ""
+caption: |-
+  Python figure for Problem 7
+
+  Equal scaling is used, so the polygonal path is not distorted.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/exercise9_problem7_python.png
+    caption: ""
+```
 
 ```Mathematica title:"Problem 7: Mathematica plot"
 Graphics[
@@ -3462,11 +3762,21 @@
 \end{cases}
 $$
 
-> [!figure] Python figure for Problem 8
-> 
-> ![](./images/exercise9_problem8_python.png)
-> 
-> Equal scaling is used, so the polygonal path is not distorted.
+```scientific-figure
+id: 90114423-7156-4e19-9040-83a4d5b57cc7
+numbered: false
+title: ""
+caption: |-
+  Python figure for Problem 8
+
+  Equal scaling is used, so the polygonal path is not distorted.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/exercise9_problem8_python.png
+    caption: ""
+```
 
 ```Mathematica title:"Problem 8: Mathematica plot"
 Graphics[
@@ -3553,11 +3863,21 @@
 -\frac{\pi}{2}\le t\le 0.
 $$
 
-> [!figure] Python figure for Problem 9
-> 
-> ![](./images/exercise9_problem9_python.png)
-> 
-> Equal scaling is used, so the circular arc is not distorted.
+```scientific-figure
+id: ac4cb828-478f-4d0f-922a-ec067802aa40
+numbered: false
+title: ""
+caption: |-
+  Python figure for Problem 9
+
+  Equal scaling is used, so the circular arc is not distorted.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/exercise9_problem9_python.png
+    caption: ""
+```
 
 ```Mathematica title:"Problem 9: Mathematica plot"
 Graphics[
@@ -3628,11 +3948,21 @@
 \frac{\pi}{2}\le t\le 2\pi.
 $$
 
-> [!figure] Python figure for Problem 10
-> 
-> ![](./images/exercise9_problem10_python.png)
-> 
-> Equal scaling is used, so the circular arc is not distorted.
+```scientific-figure
+id: 02dbe9ad-d764-4769-9fa5-fce03935e76f
+numbered: false
+title: ""
+caption: |-
+  Python figure for Problem 10
+
+  Equal scaling is used, so the circular arc is not distorted.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/exercise9_problem10_python.png
+    caption: ""
+```
 
 ```Mathematica title:"Problem 10: Mathematica plot"
 Graphics[
@@ -3708,11 +4038,21 @@
 -1\le t\le 1.
 $$
 
-> [!figure] Python figure for Problem 11
-> 
-> ![](./images/exercise9_problem11_python.png)
-> 
-> Equal scaling is used, so the parabola arc is not distorted.
+```scientific-figure
+id: 30650bf7-8d41-4eb8-b694-7dec0f762605
+numbered: false
+title: ""
+caption: |-
+  Python figure for Problem 11
+
+  Equal scaling is used, so the parabola arc is not distorted.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/exercise9_problem11_python.png
+    caption: ""
+```
 
 ```Mathematica title:"Problem 11: Mathematica plot"
 Graphics[
@@ -3791,11 +4131,21 @@
 0\le t\le \frac{\pi}{2}.
 $$
 
-> [!figure] Python figure for Problem 12
-> 
-> ![](./images/exercise9_problem12_python.png)
-> 
-> Equal scaling is used, so the circular arc is not distorted.
+```scientific-figure
+id: ba8a7a51-81fa-4102-acfd-5a12bc6427b8
+numbered: false
+title: ""
+caption: |-
+  Python figure for Problem 12
+
+  Equal scaling is used, so the circular arc is not distorted.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/exercise9_problem12_python.png
+    caption: ""
+```
 
 ```Mathematica title:"Problem 12: Mathematica plot"
 Graphics[
@@ -3866,11 +4216,21 @@
 0\le t\le \frac{3\pi}{2}.
 $$
 
-> [!figure] Python figure for Problem 13
-> 
-> ![](./images/exercise9_problem13_python.png)
-> 
-> Equal scaling is used, so the circular arc is not distorted.
+```scientific-figure
+id: e022c60e-fcea-456f-abc8-9f81ba2c7518
+numbered: false
+title: ""
+caption: |-
+  Python figure for Problem 13
+
+  Equal scaling is used, so the circular arc is not distorted.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/exercise9_problem13_python.png
+    caption: ""
+```
 
 ```Mathematica title:"Problem 13: Mathematica plot"
 Graphics[
@@ -3952,11 +4312,21 @@
 
 
 
-> [!figure] Python figure for Problem 14
-> 
-> ![](./images/exercise9_problem14_python.png)
-> 
-> Equal scaling is used, so the parabola arc is not distorted.
+```scientific-figure
+id: db1a2c44-1bef-45a4-aab1-e578a14e6738
+numbered: false
+title: ""
+caption: |-
+  Python figure for Problem 14
+
+  Equal scaling is used, so the parabola arc is not distorted.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/exercise9_problem14_python.png
+    caption: ""
+```
 
 ```Mathematica title:"Problem 14: Mathematica plot"
 Graphics[
@@ -4043,11 +4413,21 @@
 
 Write $\gamma(t)=x(t)+iy(t)$ with $x(t)=t\cos t$ and $y(t)=-t\sin t$. This is easiest to understand in polar form: $\gamma(t)=te^{-it}$, so the radius is $r=t$ and the angle is $\theta=-t$. As $t$ increases from $0$ to $2\pi$, the radius increases from $0$ to $2\pi$ while the angle decreases by $2\pi$. Therefore the path is a clockwise spiral that starts at the origin and winds outward once, ending at $2\pi$ on the positive real axis.
 
-> [!figure] Python figure for Problem 15
-> 
-> ![](./images/exercise10_problem15_python.svg)
-> 
-> Equal scaling is used, so the spiral is not distorted.
+```scientific-figure
+id: d89fa362-3440-4abc-b700-7ccc1c48138b
+numbered: false
+title: ""
+caption: |-
+  Python figure for Problem 15
+
+  Equal scaling is used, so the spiral is not distorted.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/exercise10_problem15_python.svg
+    caption: ""
+```
 
 ```Mathematica title:"Problem 15: Mathematica plot"
 Graphics[
@@ -4140,11 +4520,21 @@
 
 Here $\gamma(t)=2\cos t+i\sin t$, so $x=2\cos t$ and $y=\sin t$. Eliminating $t$ gives $\left(\frac{x}{2}\right)^2+y^2=\cos^2 t+\sin^2 t=1$, so the graph is the ellipse $\frac{x^2}{4}+y^2=1$. It is centered at the origin, with semimajor axis $2$ on the $x$-axis and semiminor axis $1$ on the $y$-axis. At $t=0$ the point is $(2,0)$, and for small positive $t$ the value of $y=\sin t$ is positive, so the path moves upward from $(2,0)$. Therefore the ellipse is traced once counterclockwise.
 
-> [!figure] Python figure for Problem 16
-> 
-> ![](./images/exercise10_problem16_python.svg)
-> 
-> Equal scaling is used, so the ellipse is not distorted.
+```scientific-figure
+id: b6f74292-1863-4f5a-a138-61205570a343
+numbered: false
+title: ""
+caption: |-
+  Python figure for Problem 16
+
+  Equal scaling is used, so the ellipse is not distorted.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/exercise10_problem16_python.svg
+    caption: ""
+```
 
 ```Mathematica title:"Problem 16: Mathematica plot"
 Graphics[
@@ -4237,11 +4627,21 @@
 
 Since $\gamma(t)=t+i\sin(\pi t)$, we have $x=t$ and $y=\sin(\pi t)$. Because $x=t$, we may replace $t$ by $x$ and write the curve as $y=\sin(\pi x)$ for $0\le x\le 1$. So the path is the graph of one sine arch over the interval $[0,1]$. It starts at $(0,0)$, rises to $(\frac12,1)$, and returns to $(1,0)$ as $t$ increases from $0$ to $1$.
 
-> [!figure] Python figure for Problem 17
-> 
-> ![](./images/exercise10_problem17_python.svg)
-> 
-> Equal scaling is used, so the graph is not distorted.
+```scientific-figure
+id: fe467d57-415b-4e4e-82e8-36f11b27a16e
+numbered: false
+title: ""
+caption: |-
+  Python figure for Problem 17
+
+  Equal scaling is used, so the graph is not distorted.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/exercise10_problem17_python.svg
+    caption: ""
+```
 
 ```Mathematica title:"Problem 17: Mathematica plot"
 Graphics[
@@ -4334,11 +4734,21 @@
 
 For $\gamma(t)=t^2+it$, we have $x=t^2$ and $y=t$. Eliminating $t$ gives $x=y^2$, so the path is the parabola opening to the right. Since $t=y$, the parameter increases from $-3$ to $3$, so the curve is traced upward: it starts at $(9,-3)$, passes through $(0,0)$ when $t=0$, and ends at $(9,3)$.
 
-> [!figure] Python figure for Problem 18
-> 
-> ![](./images/exercise10_problem18_python.svg)
-> 
-> Equal scaling is used, so the parabola is not distorted.
+```scientific-figure
+id: 6fbfae71-5a46-4c0a-be1d-7d332d08da2d
+numbered: false
+title: ""
+caption: |-
+  Python figure for Problem 18
+
+  Equal scaling is used, so the parabola is not distorted.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/exercise10_problem18_python.svg
+    caption: ""
+```
 
 ```Mathematica title:"Problem 18: Mathematica plot"
 Graphics[
@@ -5211,11 +5621,21 @@
 0\le t\le 2\pi.
 $$
 
-> [!figure] Python figure for Problem 31
-> 
-> ![](./images/exercise14_problem31_python_v2.svg)
-> 
-> The plot uses $a=4$, $b=1$, and equal scaling.
+```scientific-figure
+id: c235ccd5-1d84-49d4-91b4-53cb3ec3b2d4
+numbered: false
+title: ""
+caption: |-
+  Python figure for Problem 31
+
+  The plot uses $a=4$, $b=1$, and equal scaling.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/exercise14_problem31_python_v2.svg
+    caption: ""
+```
 
 
 
@@ -5337,11 +5757,21 @@
 0\le t\le 2\pi.
 $$
 
-> [!figure] Python figure for Problem 32
-> 
-> ![](./images/exercise14_problem32_python.svg)
-> 
-> The plot uses $a=4$, $b=1$, and equal scaling.
+```scientific-figure
+id: ef339c94-9014-4ebb-9fd8-ef43168522c8
+numbered: false
+title: ""
+caption: |-
+  Python figure for Problem 32
+
+  The plot uses $a=4$, $b=1$, and equal scaling.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/exercise14_problem32_python.svg
+    caption: ""
+```
 
 ```Mathematica title:"Problem 32: Mathematica plot"
 Graphics[
@@ -5460,11 +5890,21 @@
 0\le t\le 2\pi.
 $$
 
-> [!figure] Python figure for Problem 33
-> 
-> ![](./images/exercise14_problem33_python.svg)
-> 
-> The plot uses $a=3$, $b=1$, and equal scaling.
+```scientific-figure
+id: c57eca69-69a0-4bea-8ce1-630f34cc7694
+numbered: false
+title: ""
+caption: |-
+  Python figure for Problem 33
+
+  The plot uses $a=3$, $b=1$, and equal scaling.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/exercise14_problem33_python.svg
+    caption: ""
+```
 
 ```Mathematica title:"Problem 33: Mathematica plot"
 Graphics[
@@ -5593,11 +6033,21 @@
 0\le t\le 2\pi.
 $$
 
-> [!figure] Python figure for Problem 34
-> 
-> ![](./images/exercise14_problem34_python.svg)
-> 
-> The plot uses $a=1$, $b=1$, and equal scaling.
+```scientific-figure
+id: aae0331c-2526-4124-a805-816419ba7fd9
+numbered: false
+title: ""
+caption: |-
+  Python figure for Problem 34
+
+  The plot uses $a=1$, $b=1$, and equal scaling.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/images/exercise14_problem34_python.svg
+    caption: ""
+```
 
 ```Mathematica title:"Problem 34: Mathematica plot"
 Graphics[

`````
