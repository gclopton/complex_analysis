
# Editorial records

Reading note: 6.4 The Schwarz-Christoffel Transformation.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Callout 240: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Schwarz–Christoffel Map from a Half-Plane to a Polygon
> Let $\Omega$ be a region bounded by a simple closed polygonal path $P$ with $n$ vertices with vertices at $w_j$ (counted consecutively) and corresponding exterior angles $\theta_j$. Then there is a one-to-one conformal mapping $f(z)$ of the upper half-plane onto $\Omega$, such that
>
> $$
> f^{\prime}(z)=A\left(z-x_1\right)^{-\frac{\theta_1}{\pi}}\left(z-x_2\right)^{-\frac{\theta_2}{\pi}} \cdots\left(z-x_{n-1}\right)^{-\frac{\theta_{n-1}}{\pi}},
> $$
>
> where the $x_j$ 's are real, $x_1<x_2<\cdots<x_{n-1}, f\left(x_j\right)=w_j, \lim _{z \rightarrow \infty} f(z)= w_n, A\neq0$ is a constant, and principal branches are used to define the powers.
````
### After

````text
> [!theorem] Schwarz-Christoffel Transformation
> Let $\Omega$ be a region bounded by a simple closed polygonal path $P$ with $n$ vertices with vertices at $w_j$ (counted consecutively) and corresponding exterior angles $\theta_j$. Then there is a one-to-one conformal mapping $f(z)$ of the upper half-plane onto $\Omega$, such that
>
> $$
> f^{\prime}(z)=A\left(z-x_1\right)^{-\frac{\theta_1}{\pi}}\left(z-x_2\right)^{-\frac{\theta_2}{\pi}} \cdots\left(z-x_{n-1}\right)^{-\frac{\theta_{n-1}}{\pi}},
> $$
>
> where the $x_j$ 's are real, $x_1<x_2<\cdots<x_{n-1}, f\left(x_j\right)=w_j, \lim _{z \rightarrow \infty} f(z)= w_n, A\neq0$ is a constant, and principal branches are used to define the powers.
````

## 2. Callout 241: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!proposition] Transport of Level Curves Under a Conformal Change of Variables
> Let $f:\Omega\to D$ be a one-to-one conformal map, let $U:D\to\mathbb R$, and put $u=U\circ f$. Then the image under $w=f(z)$ of the level curve $u(z)=C$ is a level curve $U(w)=C$. Thus, if $\gamma(t)$ parametrizes an isotherm of $u$, then $f(\gamma(t))$ parametrizes a corresponding isotherm of $U$.
````
### After

````text
> [!proposition] Image of Level Curves
> Let $f:\Omega\to D$ be a one-to-one conformal map, let $U:D\to\mathbb R$, and put $u=U\circ f$. Then the image under $w=f(z)$ of the level curve $u(z)=C$ is a level curve $U(w)=C$. Thus, if $\gamma(t)$ parametrizes an isotherm of $u$, then $f(\gamma(t))$ parametrizes a corresponding isotherm of $U$.
````

## Source-to-current comparison

Source: /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 06 Conformal Mappings/6.4 The Schwarz-Christoffel Transformation.md

This exact comparison preserves the full change evidence, including formatting, OCR corrections, restored source wording, and required standalone context. The entries above explain the recovery edits. The comparison is not a claim that every difference is a correction; component serialization, callout wrapping, and printed labels outside callouts are formatting.

`````diff
--- /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 06 Conformal Mappings/6.4 The Schwarz-Christoffel Transformation.md
+++ /Users/gradyclopton/ObsidianVaults/complex_analysis/Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 06 Conformal Mappings/6.4 The Schwarz-Christoffel Transformation.md
@@ -5,10 +5,18 @@
 Suppose that $\Omega$ is a region in the $w$-plane, bounded by a positively oriented polygonal path $P$ with $n$ sides. Let $w_1, w_2, \ldots, w_n$ denote the vertices of $P$, counted consecutively as we trace the path through its positive orientation (see _Figure 1_, where $n=5$ ). If $P$ is bounded, then the point $w_n$ is taken to be the initial and terminal point of the closed path $P$. 
 
 
-> [!figure] Figure 1
-> 
-> ![[Screenshot 2026-04-04 at 8.36.31 PM.png]]
-> Figure 1 Positively oriented polygonal boundary with corner angles measured from the outside.
+```scientific-figure
+id: 362a0d12-72f1-402f-9a87-5b329b159e2f
+numbered: false
+title: ""
+caption: "**Figure 1.** Positively oriented polygonal boundary with corner angles measured from the outside."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 06 Conformal Mappings/images/Screenshot 2026-04-04 at 8.36.31 PM.png
+    caption: ""
+```
 
 
 
@@ -17,24 +25,33 @@
 
 
 
-> [!figure] Figure 2
-> 
-> ![[Screenshot 2026-04-04 at 8.36.54 PM.png]]
-> Figure 2 Unbounded polygonal region with $n$ sides ( $n=4$ ) and $n-1$ vertices.
+```scientific-figure
+id: 4520a157-6e38-4c61-ad3f-45376f2ad746
+numbered: false
+title: ""
+caption: "**Figure 2.** Unbounded polygonal region with $n$ sides ( $n=4$ ) and $n-1$ vertices."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 06 Conformal Mappings/images/Screenshot 2026-04-04 at 8.36.54 PM.png
+    caption: ""
+```
 
 
 It will be convenient to measure the exterior angle at a vertex, and so we let $\theta_j$ denote the angle that we make as we turn the corner of the polygon at $w_j$. We choose $0<\left|\theta_j\right|<\pi(j=1, \ldots, n)$; a positive value corresponds to a left turn and a negative value corresponds to a right turn. In _Figure 1_, $\theta_2$ is negative while all other $\theta_j$ are positive.
 
 
 
+<!-- Source label: Schwarz-Christoffel Transformation -->
 > [!theorem] Schwarz-Christoffel Transformation
-> Let $\Omega$ be a region bounded by a polygonal path $P$ with vertices at $w_j$ (counted consecutively) and corresponding exterior angles $\theta_j$. Then there is a one-to-one conformal mapping $f(z)$ of the upper half-plane onto $\Omega$, such that
-> 
+> Let $\Omega$ be a region bounded by a simple closed polygonal path $P$ with $n$ vertices with vertices at $w_j$ (counted consecutively) and corresponding exterior angles $\theta_j$. Then there is a one-to-one conformal mapping $f(z)$ of the upper half-plane onto $\Omega$, such that
+>
 > $$
 > f^{\prime}(z)=A\left(z-x_1\right)^{-\frac{\theta_1}{\pi}}\left(z-x_2\right)^{-\frac{\theta_2}{\pi}} \cdots\left(z-x_{n-1}\right)^{-\frac{\theta_{n-1}}{\pi}},
 > $$
-> 
-> where the $x_j$ 's are real, $x_1<x_2<\cdots<x_{n-1}, f\left(x_j\right)=w_j, \lim _{z \rightarrow \infty} f(z)= w_n, A$ is a constant, and principal branches are used to define the powers.
+>
+> where the $x_j$ 's are real, $x_1<x_2<\cdots<x_{n-1}, f\left(x_j\right)=w_j, \lim _{z \rightarrow \infty} f(z)= w_n, A\neq0$ is a constant, and principal branches are used to define the powers.
 
 
 The points $x_j(j=1, \ldots, n-1)$ on the $x$-axis are the pre-images of the vertices of the polygonal path $P$ in the $w$-plane. Two of the $x_j$ 's may be chosen arbitrarily, so long as they are arranged in ascending order. We can express the fact that $\lim _{z \rightarrow \infty} f(z)=w_n$ by writing $f(\infty)=w_n$. In the case of an unbounded polygon $P$, we have $f(\infty)=\infty$.
@@ -71,11 +88,18 @@
 Thus if $w_n=f(\infty)$, then all the points in the interval $\left(-\infty, x_1\right)$ are mapped onto a line segment starting with $w_n$ and ending with $w_1=f\left(x_1\right)$ and at an angle given by (4) (_Figure 3_). 
 
 
-> [!figure] Figure 3
-> 
-> ![[Screenshot 2026-04-04 at 8.41.11 PM.png]]
-> 
-> Figure 3 Arguments of the line segments of the polygon $P$.
+```scientific-figure
+id: d64ba9b6-8f47-4e42-bf91-3e74c5068ce1
+numbered: false
+title: ""
+caption: "**Figure 3.** Arguments of the line segments of the polygon $P$."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 06 Conformal Mappings/images/Screenshot 2026-04-04 at 8.41.11 PM.png
+    caption: ""
+```
 
 
 
@@ -94,10 +118,18 @@
 
 
 
-> [!figure] Figure 4
-> 
-> ![[Screenshot 2026-04-04 at 8.42.40 PM.png]]
-> Figure 4 As $x$ crosses $x_j$ from left to right, $\arg f^{\prime}(x)$ changes abruptly by $\theta_j$ then remains constant until it crosses $x_{j+1}$.
+```scientific-figure
+id: 2df90008-fb53-4089-81a9-dd567c3c9536
+numbered: false
+title: ""
+caption: "**Figure 4.** As $x$ crosses $x_j$ from left to right, $\\arg f^{\\prime}(x)$ changes abruptly by $\\theta_j$ then remains constant until it crosses $x_{j+1}$."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 06 Conformal Mappings/images/Screenshot 2026-04-04 at 8.42.40 PM.png
+    caption: ""
+```
 
 
 We continue in this fashion, and finally we find that after an abrupt change in the argument, the points in the interval ( $x_{n-1}, \infty$ ) are mapped onto a line segment with initial point $w_{n-1}$, and at angle $\arg f^{\prime}(z)=\arg A$. In the case of a bounded polygon, this line segment will connect back to $w_n$ (Exercise 11). The polygon is then closed; after turning the last corner we have gone through an angle $\theta_1+\theta_2+\cdots+\theta_n=2 \pi$. Thus we have shown that the mapping whose derivative is given by (1) takes the real line onto a polygon with vertices $w_j=f\left(x_j\right)$ and exterior angles $\theta_j$. Since the upper half-plane is to our left as we traverse the real line rightward, conformality ensures that the image region is to our left as we trace $P$ in the positive sense (that is, $f$ maps the upper half-plane onto the interior of $P$ ). The converse of these statements is also true, although we will not prove it. That is, given a polygonal path $P$ with vertices $w_j$ and exterior angles $\theta_j$, it can be shown that we can find ordered real numbers $x_1, \ldots, x_{n-1}$, and complex numbers $A$ and $B$ such that the mapping given by (2) whose derivative is given by (1), takes the real line onto $P$. Moreover, two of the $x_j$ 's can be chosen arbitrarily.
@@ -109,16 +141,26 @@
 > 
 > Find a Schwarz-Christoffel transformation that maps the upper half-plane onto the sector at angle $0<\alpha<\pi$ in _Figure 5_.
 > 
-> > [!figure] Figure 5
-> > 
-> > ![[Screenshot 2026-04-04 at 8.43.05 PM.png]]
-> > _Figure 5_ for Example 1.
-> 
-> 
-
-
-
-**Solution** Obviously one answer is $f(z)=z^{\frac{\alpha}{\pi}}$, but let us see how this answer comes out of (2). Since the region has two sides, we have $n=2$. From _Figure 5_, the exterior angle at $w_1=0$ is $\pi-\alpha$. In the $z$-plane, choose $x_1=0$, then (2) yields
+> ```scientific-figure
+> id: ae2d54fe-0859-4fe1-843c-71c7715df359
+> numbered: false
+> title: ""
+> caption: "**Figure 5.** for Example 1."
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 06 Conformal Mappings/images/Screenshot 2026-04-04 at 8.43.05 PM.png
+>     caption: ""
+> ```
+> 
+> 
+
+
+
+##### solution
+
+Obviously one answer is $f(z)=z^{\frac{\alpha}{\pi}}$, but let us see how this answer comes out of (2). Since the region has two sides, we have $n=2$. From _Figure 5_, the exterior angle at $w_1=0$ is $\pi-\alpha$. In the $z$-plane, choose $x_1=0$, then (2) yields
 
 $$
 f(z)=A \int z^{-\frac{\pi-\alpha}{\pi}} d z+B=A \int z^{-1+\alpha / \pi} d z+B=A \frac{\pi}{\alpha} z^{\frac{\alpha}{\pi}}+B,
@@ -143,15 +185,25 @@
 
 Find a Schwarz-Christoffel transformation that maps the upper half-plane onto the the semi-infinite vertical strip in _Figure 6_.
 
-> [!figure] Figure 6
-> 
-> ![[Screenshot 2026-04-04 at 8.44.40 PM.png]]
-> Figure 6 A semi-infinite vertical strip with positively orianted boundary.
-
-
-
-
-**Solution** We know that $\sin z$ maps the infinite strip in _Figure 6_ onto the upper half-plane. So the mapping that we are looking for is the inverse of $\sin z$. Let us see how this comes out of (2). In the $w$-plane, take $w_1=-\frac{\pi}{2}, w_2=\frac{\pi}{2}$, with exterior angles $\theta_1=\theta_2=\frac{\pi}{2}$. In the $z$-plane, take $x_1=-1$ and $x_2=1$. Then (2) yields
+```scientific-figure
+id: 2beabb84-8cd0-4351-b1aa-d09688708fc6
+numbered: false
+title: ""
+caption: "**Figure 6.** A semi-infinite vertical strip with positively orianted boundary."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 06 Conformal Mappings/images/Screenshot 2026-04-04 at 8.44.40 PM.png
+    caption: ""
+```
+
+
+
+
+##### solution
+
+We know that $\sin z$ maps the infinite strip in _Figure 6_ onto the upper half-plane. So the mapping that we are looking for is the inverse of $\sin z$. Let us see how this comes out of (2). In the $w$-plane, take $w_1=-\frac{\pi}{2}, w_2=\frac{\pi}{2}$, with exterior angles $\theta_1=\theta_2=\frac{\pi}{2}$. In the $z$-plane, take $x_1=-1$ and $x_2=1$. Then (2) yields
 
 $$
 f(z)=A \int(z+1)^{-\frac{1}{2}}(z-1)^{-\frac{1}{2}} d z+B
@@ -196,15 +248,25 @@
 > 
 > Find a Schwarz-Christoffel transformation that maps the upper half-plane onto the right isosceles triangle in _Figure 7_.
 > 
-> > [!figure] Figure 7
-> > ![[Screenshot 2026-04-04 at 8.46.14 PM.png]]
-> > 
-> > _Figure 7_ Positively oriented isosceles triangle.
-> 
-> 
-
-
-**Solution** It is clear that the triangle is determined by two consecutive vertices and their corresponding angles. In the $w$-plane, take $w_1=-1, w_2=1$, with exterior angles $\theta_1=\theta_2=\frac{3 \pi}{4}$. In the $z$-plane, we freely choose the points $x_1=-1$ and $x_2=1$. Then (2) yields
+> ```scientific-figure
+> id: ad4a6ced-6b28-461f-82c9-edfc9a027bb9
+> numbered: false
+> title: ""
+> caption: "**Figure 7.** Positively oriented isosceles triangle."
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 06 Conformal Mappings/images/Screenshot 2026-04-04 at 8.46.14 PM.png
+>     caption: ""
+> ```
+> 
+> 
+
+
+##### solution
+
+It is clear that the triangle is determined by two consecutive vertices and their corresponding angles. In the $w$-plane, take $w_1=-1, w_2=1$, with exterior angles $\theta_1=\theta_2=\frac{3 \pi}{4}$. In the $z$-plane, we freely choose the points $x_1=-1$ and $x_2=1$. Then (2) yields
 
 $$
 f(z)=A \int_0^z(\zeta+1)^{-\frac{3}{4}}(\zeta-1)^{-\frac{4}{4}} d \zeta+B=A \int_0^z \frac{d \zeta}{(-1)^{\frac{3}{4}}\left(1-\zeta^2\right)^{\frac{3}{4}}}+B,
@@ -253,24 +315,42 @@
 > 
 > Find a Schwarz-Christoffel transformation that maps the upper half-plane onto the $L$-shaped region in _Figure 8_.
 > 
-> > [!figure] Figure 8
-> > 
-> > ![[Screenshot 2026-04-04 at 8.47.18 PM.png]]
-> > Figure 8
-> 
-> 
-
-
-
-
-**Solution** To determine the orientation of the boundary in such a way that the region becomes interior to a positively oriented boundary, we think of the region as a limit of a region with vertices at $w_1=0, w_2>0$, and $w_3=1+i$, and corresponding exterior angles $\theta_1=\frac{\pi}{2}, \theta_2=\alpha$, and $\theta_3=\beta$ (_Figure 9_).
-
-
-
-> [!figure] Figure 9
-> 
-> ![[Screenshot 2026-04-04 at 8.47.42 PM.png]]
-> Figure 9
+> ```scientific-figure
+> id: bfb51e5e-c92a-4476-aef7-6894244a28bf
+> numbered: false
+> title: ""
+> caption: "**Figure 8.**"
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 06 Conformal Mappings/images/Screenshot 2026-04-04 at 8.47.18 PM.png
+>     caption: ""
+> ```
+> 
+> 
+
+
+
+
+##### solution
+
+To determine the orientation of the boundary in such a way that the region becomes interior to a positively oriented boundary, we think of the region as a limit of a region with vertices at $w_1=0, w_2>0$, and $w_3=1+i$, and corresponding exterior angles $\theta_1=\frac{\pi}{2}, \theta_2=\alpha$, and $\theta_3=\beta$ (_Figure 9_).
+
+
+
+```scientific-figure
+id: 55fc0225-719f-4767-aa78-35fe28dbc331
+numbered: false
+title: ""
+caption: "**Figure 9.**"
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 06 Conformal Mappings/images/Screenshot 2026-04-04 at 8.47.42 PM.png
+    caption: ""
+```
 
 
 As $w_2 \rightarrow \infty, \theta_2 \rightarrow \pi$, and $\theta_3 \rightarrow-\frac{\pi}{2}$. Thus, we may think of our region as having a vertex at infinity with exterior angle $\theta_2=\pi$ and a vertex at $w_3=1+i$ with exterior angle $-\frac{\pi}{2}$. In fact, setting $\theta_j=\pi$ will force $f\left(x_j\right)=\infty$. Now we may only choose two of the three $x_j$ 's arbitrarily, but in fact a solution can be found in $x_1=-1$, $x_2=0$, and $x_3=1$. Other choices of the three $x_j$ 's will typically result in $L$-shaped regions where the angle $\phi$ in _Figure 8_ is not $\pi / 4$. From (2) and (7)
@@ -314,26 +394,40 @@
 > 
 > 
 > 
-> > [!figure] Figure 10
-> > 
-> > ![[Screenshot 2026-04-04 at 8.51.48 PM.png]]
-> > 
-> > _Figure 10_ A doubly slit plane with a positively oriented boundary consisting of four sides.
-> 
-> 
-
-**Solution** To define the region as the interior of a positively oriented boundary requires four sides as shown in _Figure 10_. We think of the region as a limit of a region with vertices at $w_1=i, w_2=t$ (where $t<0$ ) and $w_3=-i$, and corresponding exterior angles $\theta_1=\alpha, \theta_2=\beta$, and $\theta_3=\gamma$ (_Figure 11_). 
-
-
-
-
-> [!figure] Figure 11
-> 
-> ![[Screenshot 2026-04-04 at 8.53.13 PM.png]]
-> 
-> Figure 11
-> 
-> 
+> ```scientific-figure
+> id: bfbf7972-010b-4873-9fb3-6565001b2635
+> numbered: false
+> title: ""
+> caption: "**Figure 10.** A doubly slit plane with a positively oriented boundary consisting of four sides."
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 06 Conformal Mappings/images/Screenshot 2026-04-04 at 8.51.48 PM.png
+>     caption: ""
+> ```
+> 
+> 
+
+##### solution
+
+To define the region as the interior of a positively oriented boundary requires four sides as shown in _Figure 10_. We think of the region as a limit of a region with vertices at $w_1=i, w_2=t$ (where $t<0$ ) and $w_3=-i$, and corresponding exterior angles $\theta_1=\alpha, \theta_2=\beta$, and $\theta_3=\gamma$ (_Figure 11_). 
+
+
+
+
+```scientific-figure
+id: 486f2adf-b123-4ac3-a652-033accca383d
+numbered: false
+title: ""
+caption: "**Figure 11.**"
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 06 Conformal Mappings/images/Screenshot 2026-04-04 at 8.53.13 PM.png
+    caption: ""
+```
 
 
 
@@ -371,8 +465,9 @@
 Suppose that $f(z)$ is a Schwarz-Christoffel transformation taking the upper half-plane onto a region $\Omega$ in the $w$-plane. If we want to solve a Dirichlet problem $\Delta U(w)=0$, the technique is to map the problem to a corresponding problem in the upper half of the $z$-plane, where a solution $u(z)$ of Laplace's equation $\Delta u(z)=0$ with boundary conditions can be obtained more easily. The solution in the $w$-plane is then $U(w)=u\left(f^{-1}(w)\right)$. However, the Schwarz-Christoffel transformation gives us $f$, not $f^{-1}$, and it is not always possible or easy to invert $f(z)$ in closed form (try Examples 3, 4 , and 5 ). Nevertheless, the conformal map $f(z)$ is still very useful: It allows us to find isotherms of $U(w)$ without actually knowing $U(w)$. As we now show, this is because the image under $f$ of an isotherm $u(z)=C$ (where $C$ is a constant) is an isotherm $U(w)=C$ in the region $\Omega$.
 
 
+<!-- Source label: Image of Level Curves -->
 > [!proposition] Image of Level Curves
-> With the preceding notation, the image under $w=f(z)$ of the level curve $u(z)=C$ is a level curve $U(w)=C$. Thus, if $\gamma(t)$ parametrizes an isotherm of $u$, then $f(\gamma(t))$ parametrizes a corresponding isotherm of $U$.
+> Let $f:\Omega\to D$ be a one-to-one conformal map, let $U:D\to\mathbb R$, and put $u=U\circ f$. Then the image under $w=f(z)$ of the level curve $u(z)=C$ is a level curve $U(w)=C$. Thus, if $\gamma(t)$ parametrizes an isotherm of $u$, then $f(\gamma(t))$ parametrizes a corresponding isotherm of $U$.
 
 
 **Proof** Since $\gamma(t)$ is a level curve of $u, u(\gamma(t))=C$. Since $U(w)=u\left(f^{-1}(w)\right)$, we conclude that $U(f(\gamma(t)))=u(\gamma(t))=C$, and hence $f(\gamma(t))$ is a level curve of $U$.
@@ -387,16 +482,26 @@
 > 
 > Find the isotherms of the Dirichlet problem $\Delta U(w)=0$ in _Figure 12_.
 > 
-> > [!figure] Figure 12
-> > 
-> > ![[Screenshot 2026-04-04 at 8.56.30 PM.png]]
-> > _Figure 12_ for Example 6.
-> 
-> 
-
-
-
-**Solution** From Example 4, we know that the Schwarz-Christoffel transformation $f(z)=\frac{1}{\pi}\left(\sin ^{-1} z+i \sin ^{-1} \frac{1}{z}\right)+\frac{1+i}{2}$ will map the upper half-plane onto the $L$ shaped region. Since the boundary data switches from 0 to 100 at $f(1)=1+i$, the corresponding Dirichlet problem in the upper half-plane is $\Delta u(z)=0, u(x)=0$ for $x<1$, and $u(x)=100$ for $x>1$. We immediately write down the solution using the argument function:
+> ```scientific-figure
+> id: bfd8bd40-13d8-4300-aca8-f828db756015
+> numbered: false
+> title: ""
+> caption: "**Figure 12.** for Example 6."
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 06 Conformal Mappings/images/Screenshot 2026-04-04 at 8.56.30 PM.png
+>     caption: ""
+> ```
+> 
+> 
+
+
+
+##### solution
+
+From Example 4, we know that the Schwarz-Christoffel transformation $f(z)=\frac{1}{\pi}\left(\sin ^{-1} z+i \sin ^{-1} \frac{1}{z}\right)+\frac{1+i}{2}$ will map the upper half-plane onto the $L$ shaped region. Since the boundary data switches from 0 to 100 at $f(1)=1+i$, the corresponding Dirichlet problem in the upper half-plane is $\Delta u(z)=0, u(x)=0$ for $x<1$, and $u(x)=100$ for $x>1$. We immediately write down the solution using the argument function:
 
 $$
 u(z)=100-\frac{100}{\pi} \operatorname{Arg}(z-1) .
@@ -415,10 +520,18 @@
 
 
 
-> [!figure] Figure 13
-> 
-> ![[Screenshot 2026-04-04 at 8.57.19 PM.png]]
-> Figure 13 Isotherms in Example 6.
+```scientific-figure
+id: aeb0f5a1-cbc3-4036-a4eb-e1ca52322410
+numbered: false
+title: ""
+caption: "**Figure 13.** Isotherms in Example 6."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 06 Conformal Mappings/images/Screenshot 2026-04-04 at 8.57.19 PM.png
+    caption: ""
+```
 
 
 
@@ -459,10 +572,18 @@
 For a simple example of a complex potential, we consider a uniform rightward flow in the upper half-plane with complex potential $\Phi(z)=z= x+i y$ (_Figure 14_). 
 
 
-> [!figure] Figure 14
-> 
-> ![[Screenshot 2026-04-04 at 9.01.06 PM.png]]
-> Figure 14 Streamlines in a uniform rightward flow in the upper half-plane.
+```scientific-figure
+id: dcd5996d-9661-4f84-a31f-9a7ff5a869ca
+numbered: false
+title: ""
+caption: "**Figure 14.** Streamlines in a uniform rightward flow in the upper half-plane."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 06 Conformal Mappings/images/Screenshot 2026-04-04 at 9.01.06 PM.png
+    caption: ""
+```
 
 
 
@@ -480,16 +601,25 @@
 > 
 > 
 > 
-> > [!figure] Figure 15
-> > 
-> > ![[Screenshot 2026-04-04 at 8.58.40 PM.png]]
-> > 
-> > _Figure 15_ Streamlines in a sector
-> 
-> 
-
-
-**Solution** From Example 1, the Schwarz-Christoffel transformation $f(z)=z^{\frac{1}{4}}$ maps the upper half-plane to the given sector. We will use the simple stream function in the upper half-plane, $\psi(z)=y$, to generate a solution. Streamlines in the $z$-plane are parametrized as $\gamma(x)=x+i y_0$ for fixed $y_0$. Streamlines in the $w$ plane are images of these under $f$; we have $f(\gamma(x))=\left(x+i y_0\right)^{\frac{1}{4}}$. As the parameter $x$ increases, the streamlines are traced in the manner shown in _Figure 15_. Fluid comes in along $\operatorname{Arg} w=\frac{\pi}{4}$ and out along $\operatorname{Arg} w=0$.
+> ```scientific-figure
+> id: aa6a1500-4ee5-460a-ac81-acfeebcb08c2
+> numbered: false
+> title: ""
+> caption: "**Figure 15.** Streamlines in a sector"
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 06 Conformal Mappings/images/Screenshot 2026-04-04 at 8.58.40 PM.png
+>     caption: ""
+> ```
+> 
+> 
+
+
+##### solution
+
+From Example 1, the Schwarz-Christoffel transformation $f(z)=z^{\frac{1}{4}}$ maps the upper half-plane to the given sector. We will use the simple stream function in the upper half-plane, $\psi(z)=y$, to generate a solution. Streamlines in the $z$-plane are parametrized as $\gamma(x)=x+i y_0$ for fixed $y_0$. Streamlines in the $w$ plane are images of these under $f$; we have $f(\gamma(x))=\left(x+i y_0\right)^{\frac{1}{4}}$. As the parameter $x$ increases, the streamlines are traced in the manner shown in _Figure 15_. Fluid comes in along $\operatorname{Arg} w=\frac{\pi}{4}$ and out along $\operatorname{Arg} w=0$.
 
 
 > [!exercise] EXAMPLE 8 Fluid flow in the doubly slit plane
@@ -498,15 +628,25 @@
 > 
 > 
 > 
-> > [!figure] Figure 16
-> > 
-> > ![[Screenshot 2026-04-04 at 9.00.24 PM.png]]
-> > _Figure 16_ Streamlines in a doubly slit plane.
-> 
-> 
-
-
-**Solution** In Example 5, we found that $f(z)=-\frac{1}{\pi} z^2+\frac{2}{\pi} \log z+\frac{1}{\pi}-i$ is a conformal mapping of the upper half-plane onto the doubly slit plane $\Omega$. Taking $\psi(z)=y$ to be the stream function for the upper half-plane, for each $y_0 \geq 0$ we have a streamline parametrized by $\gamma(x)=x+i y_0,-\infty<x<\infty$. By Proposition 1, the images $f(\gamma(x))$ are streamlines in the doubly slit plane. They are
+> ```scientific-figure
+> id: df7a2017-eaf7-46e6-b707-d97940ebb51f
+> numbered: false
+> title: ""
+> caption: "**Figure 16.** Streamlines in a doubly slit plane."
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 06 Conformal Mappings/images/Screenshot 2026-04-04 at 9.00.24 PM.png
+>     caption: ""
+> ```
+> 
+> 
+
+
+##### solution
+
+In Example 5, we found that $f(z)=-\frac{1}{\pi} z^2+\frac{2}{\pi} \log z+\frac{1}{\pi}-i$ is a conformal mapping of the upper half-plane onto the doubly slit plane $\Omega$. Taking $\psi(z)=y$ to be the stream function for the upper half-plane, for each $y_0 \geq 0$ we have a streamline parametrized by $\gamma(x)=x+i y_0,-\infty<x<\infty$. By Proposition 1, the images $f(\gamma(x))$ are streamlines in the doubly slit plane. They are
 
 $$
 f\left(x+i y_0\right)=-\frac{1}{\pi}\left(x+i y_0\right)^2+\frac{2}{\pi} \log \left(x+i y_0\right)+\frac{1}{\pi}-i \quad(-\infty<x<\infty) .
@@ -530,20 +670,36 @@
 > In problems 1 - 6, find the Schwarz-Christoffel transformation of the upper half-plane onto the given region. Use the labeled points to set-up the integral (2).
 > 1. See _Figure 17_. **(Hint: Use (7) and integrate.)**
 > 
-> > [!figure] Figure 17
-> > 
-> > ![[Screenshot 2026-04-04 at 9.04.31 PM.png]]
-> > Figure 17
+> ```scientific-figure
+> id: 2e781877-2e9a-4a64-ba2d-e4452e496964
+> numbered: false
+> title: ""
+> caption: "**Figure 17.**"
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 06 Conformal Mappings/images/Screenshot 2026-04-04 at 9.04.31 PM.png
+>     caption: ""
+> ```
 > 
 > 
 > 
 > 2. See _Figure 18_. **(Hint: $\frac{z+1}{(z-1)^{\frac{1}{2}}}=\frac{z-1+2}{(z-1)^{\frac{1}{2}}}=(z-1)^{\frac{1}{2}}+\frac{2}{(z-1)^{\frac{1}{2}}}$.)**
 > 
 > 
-> > [!figure] Figure 18
-> > 
-> > ![[Screenshot 2026-04-04 at 9.04.47 PM.png]]
-> > Figure 18
+> ```scientific-figure
+> id: 7972481f-b382-4216-ac88-871aa682dc53
+> numbered: false
+> title: ""
+> caption: "**Figure 18.**"
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 06 Conformal Mappings/images/Screenshot 2026-04-04 at 9.04.47 PM.png
+>     caption: ""
+> ```
 > 
 > 
 > 
@@ -551,28 +707,52 @@
 > 
 > 3. See _Figure 19_. **(Hint: $\frac{(z+1)^{\frac{1}{2}}}{(z-1)^{\frac{1}{2}}}=\frac{z+1}{i\left(1-z^2\right)^{\frac{1}{2}}}=\frac{z}{i\left(1-z^2\right)^{\frac{1}{2}}}+\frac{1}{i\left(1-z^2\right)^{\frac{1}{2}}}$.)**
 > 
-> > [!figure] Figure 19
-> > 
-> > ![[Screenshot 2026-04-04 at 9.05.11 PM.png]]
-> > Figure 19
+> ```scientific-figure
+> id: 767956d8-d51f-46d3-8441-ea22dcf8b1a1
+> numbered: false
+> title: ""
+> caption: "**Figure 19.**"
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 06 Conformal Mappings/images/Screenshot 2026-04-04 at 9.05.11 PM.png
+>     caption: ""
+> ```
 > 
 > 
 > 4. See _Figure 20_. **(Hint: $\frac{(z-1)^{\frac{1}{2}}}{(z+1)^{\frac{1}{2}}}=\frac{z-1}{i\left(1-z^2\right)^{\frac{1}{2}}}=\frac{z}{i\left(1-z^2\right)^{\frac{1}{2}}}-\frac{1}{i\left(1-z^2\right)^{\frac{1}{2}}}$.)**
 > 
-> > [!figure] Figure 20
-> > 
-> > ![[Screenshot 2026-04-04 at 9.05.34 PM.png]]
-> > Figure 20
+> ```scientific-figure
+> id: 2d432de7-96b4-4254-979a-53905116eca0
+> numbered: false
+> title: ""
+> caption: "**Figure 20.**"
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 06 Conformal Mappings/images/Screenshot 2026-04-04 at 9.05.34 PM.png
+>     caption: ""
+> ```
 > 
 > 
 > 
 > 5. See _Figure 21_. **(Hint: Let $z=\sin \zeta$, where $-\frac{\pi}{2} \leq \operatorname{Re} \zeta \leq \frac{\pi}{2}$ and $\operatorname{Im} \zeta \geq 0$. Then $\left(1-z^2\right)^{\frac{1}{2}}=\cos \zeta$. Use $\cos ^2 \zeta=\frac{1+\cos 2 \zeta}{2}$, integrate, then use $\sin 2 \zeta=2 \sin \zeta \cos \zeta$.)**
 > 
 > 
-> > [!figure] Figure 21
-> > 
-> > ![[Screenshot 2026-04-04 at 9.06.00 PM.png]]
-> > Figure 21
+> ```scientific-figure
+> id: fb1043dc-8f7c-48fa-bcb1-7162c41c0c47
+> numbered: false
+> title: ""
+> caption: "**Figure 21.**"
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 06 Conformal Mappings/images/Screenshot 2026-04-04 at 9.06.00 PM.png
+>     caption: ""
+> ```
 > 
 > 
 > 
@@ -582,10 +762,18 @@
 > 6. See _Figure 22_, $\left[\right.$ Hints: $\frac{(z-1)^{\frac{1}{2}}}{z+1}=\frac{1}{(z-1)^{\frac{1}{2}}} \frac{z-1}{z+1}=\frac{1}{(z-1)^{\frac{1}{2}}}-\frac{2}{(z-1)^{\frac{1}{2}}} \frac{1}{z+1}$. In the second term, use $\frac{1}{z+1}=\frac{1}{2 \sqrt{2}}\left(\frac{1}{\sqrt{z-1}+i \sqrt{2}}-\frac{1}{\sqrt{z-1}-i \sqrt{2}}\right)$, and change variables $u= \sqrt{z-1}-i \sqrt{2}$ and $v=\sqrt{z-1}-i \sqrt{2}$. You cannot find $A$ and $B$ just from $f(1)=0$. Instead, first argue that $\operatorname{Arg} A=-\frac{\pi}{2}$ (look at the angle of the final line segment; see the proof of Theorem 1) and thus $A=-i|A|$. Now get $B=i \pi \sqrt{2}|A|$ from $f(1)=0$. To get $|A|$, either use $\operatorname{Im} f(x)=1$ for $x<1$, or use the channel width formula (16) $\left.1=|s|=\pi|A|\left|x_2-x_1\right|^{-\frac{g_2}{\pi}} \right\rvert\,$
 > 
 > 
-> > [!figure] Figure 22
-> > 
-> > ![[Screenshot 2026-04-04 at 9.06.22 PM.png]]
-> > Figure 22
+> ```scientific-figure
+> id: 2b413615-d3c2-41c6-836f-369ed1495ff6
+> numbered: false
+> title: ""
+> caption: "**Figure 22.**"
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 06 Conformal Mappings/images/Screenshot 2026-04-04 at 9.06.22 PM.png
+>     caption: ""
+> ```
 > 
 > 
 > 
@@ -696,10 +884,18 @@
 > where again $\left|x_{j_0}-x_{j_0}\right|$ is skipped.
 > 
 > 
-> > [!figure] Figure 23
-> > 
-> > ![[Screenshot 2026-04-04 at 9.06.42 PM.png]]
-> > Figure 23
+> ```scientific-figure
+> id: ea6f582f-3fdc-4a87-82f9-c78a3a450fc6
+> numbered: false
+> title: ""
+> caption: "**Figure 23.**"
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 06 Conformal Mappings/images/Screenshot 2026-04-04 at 9.06.42 PM.png
+>     caption: ""
+> ```
 > 
 > 
 > (c) Verify the channel width formula for the $L$-shaped region of Example 4 and the doubly slit plane of Example 5.

`````
