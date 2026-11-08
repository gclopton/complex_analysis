
# Editorial records

Reading note: 1.4 Complex Function.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Callout 21: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!definition] Möbius (Linear Fractional) Transformation
> For complex constants $a,b,c,d$ with $ad-bc\ne0$, a Möbius transformation is the map below, defined at finite $z$ for which $cz+d\ne0$:
>
> $$
> w=\frac{a z+b}{c z+d} \quad(a d \neq b c)
> $$
````
### After

````text
> [!definition] Linear Fractional Transformation (Bilinear Transformation, Möbius Transformation)
> For complex constants $a,b,c,d$ with $ad-bc\ne0$, a Möbius transformation is the map below, defined at finite $z$ for which $cz+d\ne0$:
>
> $$
> w=\frac{a z+b}{c z+d} \quad(a d \neq b c)
> $$
````

## Source-to-current comparison

Source: /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 01 Complex Numbers and Functions/1.4 Complex Function.md

This exact comparison preserves the full change evidence, including formatting, OCR corrections, restored source wording, and required standalone context. The entries above explain the recovery edits. The comparison is not a claim that every difference is a correction; component serialization, callout wrapping, and printed labels outside callouts are formatting.

`````diff
--- /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 01 Complex Numbers and Functions/1.4 Complex Function.md
+++ /Users/gradyclopton/ObsidianVaults/complex_analysis/Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 01 Complex Numbers and Functions/1.4 Complex Function.md
@@ -123,12 +123,18 @@
 Back in calculus, a real-valued function $y=g(x)$ of a real variable $x$ was represented as a graph in the $x y$-plane. The graph contains vital information about the function and allows us to easily visualize and deduce properties of $g(x)$. In the complex case, we are not as fortunate. To visualize a complex-valued function $f(z)$ requires four dimensions: two dimensions for the variable $z$ and two for the values $w=f(z)$. Since a four-dimensional picture is not practical, instead we will use two planes, the $z$-plane and the $w$-plane, and visualize the function as a mapping from a subset of one plane to the other (see Figure 1). 
 
 
-> [!figure] Figure 1
-> 
-> ![](./images/13d4bcc6-f973-445e-ad7d-b22a7a43507d-38_507_1299_643_762.jpg)
-> 
-> 
-> Figure 1 To visualize a mapping by a complex-valued function $w=f(z)$, we use two planes: the $z$ - or $x y$-plane for the domain of definition and the $w$ - or $u v$-plane for the image.
+```scientific-figure
+id: 9446cf41-27cd-4b82-b65e-48177a6e4e0f
+numbered: false
+title: ""
+caption: "**Figure 1.** To visualize a mapping by a complex-valued function $w=f(z)$, we use two planes: the $z$ - or $x y$-plane for the domain of definition and the $w$ - or $u v$-plane for the image."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 01 Complex Numbers and Functions/images/13d4bcc6-f973-445e-ad7d-b22a7a43507d-38_507_1299_643_762.jpg
+    caption: ""
+```
 
 
 
@@ -193,7 +199,7 @@
 
 
 
-![](Pasted%20image%2020260411024044.png)
+![](Books/Asmar%20Applied%20Complex%20Analysis%20with%20Applications%20to%20Differential%20Equations/Chapter%2001%20Complex%20Numbers%20and%20Functions/images/Pasted%20image%2020260411024044.png)
 
 
 
@@ -281,11 +287,18 @@
 
 
 
-> [!figure] Figure 2
-> 
-> ![](./images/13d4bcc6-f973-445e-ad7d-b22a7a43507d-38_424_1093_1727_797.jpg)
-> 
-> Figure 2 A ==translation== is a mapping of the form $f(z)= z+b$, where $b$ is a complex number. In Example 1, $b= 2+i$.
+```scientific-figure
+id: ca53a211-63e3-4b58-bbeb-0ee8883a1ae5
+numbered: false
+title: ""
+caption: "**Figure 2.** A ==translation== is a mapping of the form $f(z)= z+b$, where $b$ is a complex number. In Example 1, $b= 2+i$."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 01 Complex Numbers and Functions/images/13d4bcc6-f973-445e-ad7d-b22a7a43507d-38_424_1093_1727_797.jpg
+    caption: ""
+```
 
 
 
@@ -405,7 +418,7 @@
 $$
 
 
-![](Pasted%20image%2020260411025109.png)
+![](Books/Asmar%20Applied%20Complex%20Analysis%20with%20Applications%20to%20Differential%20Equations/Chapter%2001%20Complex%20Numbers%20and%20Functions/images/Pasted%20image%2020260411025109.png)
 
 
 ```mathematica title:""
@@ -500,22 +513,30 @@
 
 
 
-> [!figure] Figure 3
-> 
-> ![](./images/13d4bcc6-f973-445e-ad7d-b22a7a43507d-39_388_1047_1265_763.jpg)
-> 
-> Figure 3 Images of the corners are computed explicitly using the formula for $f$
-> 
-> $$
-> \begin{aligned}
-> & f(1+i)=3+3 i \\
-> & f(1-i)=3-3 i \\
-> & f(3+i)=9+3 i \\
-> & f(3-i)=9-3 i
-> \end{aligned}
-> $$
-> 
-> They form the corners of the image.
+```scientific-figure
+id: 31eae23c-a75d-43d9-b215-5243241b0b99
+numbered: false
+title: ""
+caption: |-
+  **Figure 3.** Images of the corners are computed explicitly using the formula for $f$
+
+  $$
+  \begin{aligned}
+  & f(1+i)=3+3 i \\
+  & f(1-i)=3-3 i \\
+  & f(3+i)=9+3 i \\
+  & f(3-i)=9-3 i
+  \end{aligned}
+  $$
+
+  They form the corners of the image.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 01 Complex Numbers and Functions/images/13d4bcc6-f973-445e-ad7d-b22a7a43507d-39_388_1047_1265_763.jpg
+    caption: ""
+```
 
 
 
@@ -663,13 +684,20 @@
 ]
 ```
 
-> [!figure] Figure 4
-> 
-> ![](./images/13d4bcc6-f973-445e-ad7d-b22a7a43507d-39_394_931_1943_753.jpg)
-> 
->
->Figure 5 The inversion
-> Figure 4 The mapping $g(z)=2 i z$ is a composition of two mappings: a dilation by a factor of 2 , followed by a counterclockwise rotation by an angle of $\pi / 2$. The angle of rotation is the argument of $2 i$.
+```scientific-figure
+id: 8d622e21-1746-4858-b0d9-cc09e8e4fd9d
+numbered: false
+title: ""
+caption: |-
+  **Figure 4.** Figure 5 The inversion
+  Figure 4 The mapping $g(z)=2 i z$ is a composition of two mappings: a dilation by a factor of 2 , followed by a counterclockwise rotation by an angle of $\pi / 2$. The angle of rotation is the argument of $2 i$.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 01 Complex Numbers and Functions/images/13d4bcc6-f973-445e-ad7d-b22a7a43507d-39_394_931_1943_753.jpg
+    caption: ""
+```
 
 
 ++++
@@ -781,7 +809,7 @@
 $$
 
 
-![](Pasted%20image%2020260411025923.png)
+![](Books/Asmar%20Applied%20Complex%20Analysis%20with%20Applications%20to%20Differential%20Equations/Chapter%2001%20Complex%20Numbers%20and%20Functions/images/Pasted%20image%2020260411025923.png)
 
 
 ```mathematica title:""
@@ -896,7 +924,7 @@
 $$
 
 
-![](Pasted%20image%2020260411030138.png)
+![](Books/Asmar%20Applied%20Complex%20Analysis%20with%20Applications%20to%20Differential%20Equations/Chapter%2001%20Complex%20Numbers%20and%20Functions/images/Pasted%20image%2020260411030138.png)
 
 
 
@@ -995,37 +1023,53 @@
 $$
 
 
-> [!figure] Figure 5
-> 
-> ![](./images/13d4bcc6-f973-445e-ad7d-b22a7a43507d-40_380_981_1841_810.jpg)
-> 
-> $$
-> w=\frac{1}{z}
-> $$
-> 
-> has the effect of inverting the modulus and changing the sign of the argument:
-> 
-> $$
-> \begin{aligned}
-> & |w|=\frac{1}{|z|} \\
-> & \operatorname{Arg} w=-\operatorname{Arg} z .
-> \end{aligned}
-> $$
-> 
+```scientific-figure
+id: 52b4c236-972d-46df-8091-863b08ad618f
+numbered: false
+title: ""
+caption: |-
+  **Figure 5.** $$
+  w=\frac{1}{z}
+  $$
+
+  has the effect of inverting the modulus and changing the sign of the argument:
+
+  $$
+  \begin{aligned}
+  & |w|=\frac{1}{|z|} \\
+  & \operatorname{Arg} w=-\operatorname{Arg} z .
+  \end{aligned}
+  $$
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 01 Complex Numbers and Functions/images/13d4bcc6-f973-445e-ad7d-b22a7a43507d-40_380_981_1841_810.jpg
+    caption: ""
+```
 
 
 (b) As the modulus of $z$ increases from 2 up to infinity, the modulus of $1 / z$ decreases from $1 / 2$ down to zero (but never equals zero). As the argument of $z$ goes from 0 up to $\pi$, the argument of $1 / z$ goes from 0 down to $-\pi$. Hence $f[S]$ is the set of points in the lower half-plane, including the real axis, with $0<|w|<1 / 2$ (see Figure 6): $f[S]=\{w: 0<|w|<1 / 2,-\pi \leq \arg z \leq 0\}$.
 
-> [!figure] Figure 6
-> Figure 6 Under the inversion
-> 
-> $$
-> f(z)=\frac{1}{z},
-> $$
-> 
-> points outside the circle of radius $2,|z| \geq 2$, get mapped to points inside the circle of radius $\frac{1}{2},|w| \leq \frac{1}{2}$.
-> ![](./images/13d4bcc6-f973-445e-ad7d-b22a7a43507d-41_414_1017_208_782.jpg)
-> 
+```scientific-figure
+id: 97d87b02-1c6a-4f67-a131-19d1d243fb09
+numbered: false
+title: ""
+caption: |-
+  **Figure 6.** Under the inversion
+
+  $$
+  f(z)=\frac{1}{z},
+  $$
+
+  points outside the circle of radius $2,|z| \geq 2$, get mapped to points inside the circle of radius $\frac{1}{2},|w| \leq \frac{1}{2}$.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 01 Complex Numbers and Functions/images/13d4bcc6-f973-445e-ad7d-b22a7a43507d-41_414_1017_208_782.jpg
+    caption: ""
+```
 
 
 > [!review] Review 4
@@ -1070,7 +1114,10 @@
 
 The function $f(z)=\frac{1}{z}$ in Example 3 is a special case of a general type of mapping of the form
 
-> [!definition] Linear Fractional Transformation (Bilinear Transformation, Möbius Transformation) 
+<!-- Source label: Linear Fractional Transformation (Bilinear Transformation, Möbius Transformation)  -->
+> [!definition] Linear Fractional Transformation (Bilinear Transformation, Möbius Transformation)
+> For complex constants $a,b,c,d$ with $ad-bc\ne0$, a Möbius transformation is the map below, defined at finite $z$ for which $cz+d\ne0$:
+>
 > $$
 > w=\frac{a z+b}{c z+d} \quad(a d \neq b c)
 > $$
@@ -1259,7 +1306,7 @@
 
 
 
-![](Pasted%20image%2020260411032618.png)
+![](Books/Asmar%20Applied%20Complex%20Analysis%20with%20Applications%20to%20Differential%20Equations/Chapter%2001%20Complex%20Numbers%20and%20Functions/images/Pasted%20image%2020260411032618.png)
 
 
 ```mathematica title:""
@@ -1374,16 +1421,25 @@
 
 
 
-> [!figure] Figure 7
->  ![](./images/13d4bcc6-f973-445e-ad7d-b22a7a43507d-42_502_1006_1082_789.jpg)
-> 
-> Figure 7 For $1 \leq x_{0} \leq 2$, the image of a line $x=x_{0}$ under the mapping $f(z)=z^{2}$ is a parabola
-> 
-> $$
-> u=x_{0}^{2}-\frac{v^{2}}{4 x_{0}^{2}}
-> $$
-> 
-> As we vary $x_{0}$ from 1 to 2 , these parabolas sweep out a parabolic region, which determines $f[S]$.
+```scientific-figure
+id: f7b453c0-2678-46d1-96e4-06ec17988c47
+numbered: false
+title: ""
+caption: |-
+  **Figure 7.** For $1 \leq x_{0} \leq 2$, the image of a line $x=x_{0}$ under the mapping $f(z)=z^{2}$ is a parabola
+
+  $$
+  u=x_{0}^{2}-\frac{v^{2}}{4 x_{0}^{2}}
+  $$
+
+  As we vary $x_{0}$ from 1 to 2 , these parabolas sweep out a parabolic region, which determines $f[S]$.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 01 Complex Numbers and Functions/images/13d4bcc6-f973-445e-ad7d-b22a7a43507d-42_502_1006_1082_789.jpg
+    caption: ""
+```
 
 
 
@@ -1508,7 +1564,7 @@
 
 
 
-![](Pasted%20image%2020260411033329.png)
+![](Books/Asmar%20Applied%20Complex%20Analysis%20with%20Applications%20to%20Differential%20Equations/Chapter%2001%20Complex%20Numbers%20and%20Functions/images/Pasted%20image%2020260411033329.png)
 
 
 
@@ -1604,26 +1660,32 @@
 f[S]=\left\{w:|w| \leq \frac{27}{8}, 0 \leq \arg w \leq \frac{3 \pi}{4}\right\} .
 $$
 
-> [!figure] Figure 8
-> 
-> Figure 8 The mapping
-> 
-> $$
-> w=z^{3}
-> $$
-> 
-> has the effect of cubing the norm and tripling the argument:
-> 
-> $$
-> \begin{aligned}
-> & |w|=|z|^{3} \\
-> & \arg w=3 \operatorname{Arg} z
-> \end{aligned}
-> $$
-> 
-> 
-> ![](./images/13d4bcc6-f973-445e-ad7d-b22a7a43507d-43_383_857_567_771.jpg)
-> 
+```scientific-figure
+id: ab53b6ea-10f4-4433-813d-98396f8ef906
+numbered: false
+title: ""
+caption: |-
+  **Figure 8.** The mapping
+
+  $$
+  w=z^{3}
+  $$
+
+  has the effect of cubing the norm and tripling the argument:
+
+  $$
+  \begin{aligned}
+  & |w|=|z|^{3} \\
+  & \arg w=3 \operatorname{Arg} z
+  \end{aligned}
+  $$
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 01 Complex Numbers and Functions/images/13d4bcc6-f973-445e-ad7d-b22a7a43507d-43_383_857_567_771.jpg
+    caption: ""
+```
 
 All the mappings considered in the examples have been one-to-one, in that distinct points $z_{1}$ and $z_{2}$ always map to distinct points $f\left(z_{1}\right)$ and $f\left(z_{2}\right)$. It is possible that more than one point on the $z$-plane will map to the same point on the $w$-plane. Such mappings are not one-to-one, and we are already familiar with some of them. For example, the function $f(z)=z^{2}$ with domain of definition $\mathbb{C}$ will map $z$ and $-z$ to the same point in the $w$-plane.
 
@@ -2188,7 +2250,7 @@
 $$
 
 
-![[Pasted image 20260409005720.png]]
+![[Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 01 Complex Numbers and Functions/images/Pasted image 20260409005720.png]]
 
 
 
@@ -2374,7 +2436,7 @@
 
 So the right half-plane maps to itself.
 
-![](./images/exercise9-problem22.png)
+![](Books/Asmar%20Applied%20Complex%20Analysis%20with%20Applications%20to%20Differential%20Equations/Chapter%2001%20Complex%20Numbers%20and%20Functions/images/exercise9-problem22.png)
 
 ```python
 from pathlib import Path
@@ -2591,7 +2653,7 @@
 f[S]=\{w: \operatorname{Re} w<0,\ \operatorname{Im} w<2\} .
 $$
 
-![](./images/exercise9-problem23.png)
+![](Books/Asmar%20Applied%20Complex%20Analysis%20with%20Applications%20to%20Differential%20Equations/Chapter%2001%20Complex%20Numbers%20and%20Functions/images/exercise9-problem23.png)
 
 ```python
 from pathlib import Path
@@ -2817,7 +2879,7 @@
 This is the quarter-disk of radius $2$ centered at $2$, lying above and to the left of the center.
 
 
-![](Pasted%20image%2020260411022043.png)
+![](Books/Asmar%20Applied%20Complex%20Analysis%20with%20Applications%20to%20Differential%20Equations/Chapter%2001%20Complex%20Numbers%20and%20Functions/images/Pasted%20image%2020260411022043.png)
 
 
 
@@ -3312,7 +3374,7 @@
 f[S]=\{w:|w| \geq 1\} .
 $$
 
-![](./images/exercise12-problem31.png)
+![](Books/Asmar%20Applied%20Complex%20Analysis%20with%20Applications%20to%20Differential%20Equations/Chapter%2001%20Complex%20Numbers%20and%20Functions/images/exercise12-problem31.png)
 
 ```python
 from pathlib import Path
@@ -3505,7 +3567,7 @@
 f[S]=\{w: 0<|w| \leq 1\} .
 $$
 
-![](./images/exercise12-problem32.png)
+![](Books/Asmar%20Applied%20Complex%20Analysis%20with%20Applications%20to%20Differential%20Equations/Chapter%2001%20Complex%20Numbers%20and%20Functions/images/exercise12-problem32.png)
 
 ```python
 from pathlib import Path
@@ -3708,7 +3770,7 @@
 f[S]=\left\{w:|w| \geq \frac{1}{3},-\frac{2 \pi}{3} \leq \operatorname{Arg} w \leq-\frac{\pi}{3}\right\} .
 $$
 
-![](./images/exercise12-problem33.png)
+![](Books/Asmar%20Applied%20Complex%20Analysis%20with%20Applications%20to%20Differential%20Equations/Chapter%2001%20Complex%20Numbers%20and%20Functions/images/exercise12-problem33.png)
 
 ```python
 from pathlib import Path
@@ -3929,7 +3991,7 @@
 f[S]=\left\{w: w \neq 0,-\frac{\pi}{2} \leq \operatorname{Arg} w \leq 0\right\} .
 $$
 
-![](./images/exercise12-problem34.png)
+![](Books/Asmar%20Applied%20Complex%20Analysis%20with%20Applications%20to%20Differential%20Equations/Chapter%2001%20Complex%20Numbers%20and%20Functions/images/exercise12-problem34.png)
 
 
 

`````
