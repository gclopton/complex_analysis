
# Editorial records

Reading note: 2.5 Harmonic Functions and Laplace's Equation.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Callout 64: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem|85415a80-67bf-5079-8636-7064ce1f10bd.local at=34247b14-e17d-54b0-913f-1c2999b59ba0] Real and Imaginary Parts of Analytic Functions Are Harmonic
> Suppose that $f=u+i v$ is analytic on an open set $S$. Then its real and imaginary parts $u(x, y)$ and $v(x, y)$ are harmonic on $S$.
````
### After

````text
> [!theorem|85415a80-67bf-5079-8636-7064ce1f10bd.local at=34247b14-e17d-54b0-913f-1c2999b59ba0] Analytic and Harmonic Functions
> Suppose that $f=u+i v$ is analytic on an open set $S$. Then its real and imaginary parts $u(x, y)$ and $v(x, y)$ are harmonic on $S$.
````

## 2. Callout 65: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!proposition|b0be787d-715a-5b55-b91e-9a9426bb5e67.local at=64b35c27-03c0-5fba-9a6c-8fe7acbdd5de] Real Linear Combinations of Harmonic Functions
> Suppose that $u$ and $v$ are harmonic on an open set $S$, and $a, b$ are real constants. Then $a u(x, y)+b v(x, y)$ is harmonic on $S$.
````
### After

````text
> [!proposition|b0be787d-715a-5b55-b91e-9a9426bb5e67.local at=64b35c27-03c0-5fba-9a6c-8fe7acbdd5de] Linearity
> Suppose that $u$ and $v$ are harmonic on an open set $S$, and $a, b$ are real constants. Then $a u(x, y)+b v(x, y)$ is harmonic on $S$.
````

## 3. Callout 68: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem|192c37f1-0b24-5836-91b4-767ea387e566.local at=281f9cdb-f49d-5b46-9803-5fa64585da04] Orthogonality of Harmonic-Conjugate Level Curves
> Suppose that $u$ is a harmonic function in a region $\Omega$ and let $v$ be a harmonic conjugate of $u$ in $\Omega$, so that $f=u+i v$ is analytic in $\Omega$. Then, the two families of level curves, $u(x, y)=C_{1}$ and $v(x, y)=C_{2}$, are orthogonal at every point where $f^{\prime}(z) \neq 0$.
````
### After

````text
> [!theorem|192c37f1-0b24-5836-91b4-767ea387e566.local at=281f9cdb-f49d-5b46-9803-5fa64585da04] Orthogonality of Level Curves
> Suppose that $u$ is a harmonic function in a region $\Omega$ and let $v$ be a harmonic conjugate of $u$ in $\Omega$, so that $f=u+i v$ is analytic in $\Omega$. Then, the two families of level curves, $u(x, y)=C_{1}$ and $v(x, y)=C_{2}$, are orthogonal at every point where $f^{\prime}(z) \neq 0$.
````

## 4. Callout 69: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem|833a8d0a-1ab5-5611-ad92-735684872993.local at=259a7183-1ac0-5a8e-ac46-9a85dd73ede5] Harmonicity under Analytic Change of Variables
> Suppose that $f$ is an analytic mapping of $\Omega$ into $\Omega^{\prime}$ and $U$ is a harmonic function on $\Omega^{\prime}$. Then $U \circ f$ is harmonic in $\Omega$. Thus, if $U$ satisfies $\Delta U=0$ on $\Omega^{\prime}$, then $u=U \circ f$ satisfies $\Delta u=0$ on $\Omega$.
````
### After

````text
> [!theorem|833a8d0a-1ab5-5611-ad92-735684872993.local at=259a7183-1ac0-5a8e-ac46-9a85dd73ede5] Invariance of Laplace's Equation
> Suppose that $f$ is an analytic mapping of $\Omega$ into $\Omega^{\prime}$ and $U$ is a harmonic function on $\Omega^{\prime}$. Then $U \circ f$ is harmonic in $\Omega$. Thus, if $U$ satisfies $\Delta U=0$ on $\Omega^{\prime}$, then $u=U \circ f$ satisfies $\Delta u=0$ on $\Omega$.
````

## Source-to-current comparison

Source: /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 02 Analytic Functions/2.5 Harmonic Functions and Laplace's Equation.md

This exact comparison preserves the full change evidence, including formatting, OCR corrections, restored source wording, and required standalone context. The entries above explain the recovery edits. The comparison is not a claim that every difference is a correction; component serialization, callout wrapping, and printed labels outside callouts are formatting.

`````diff
--- /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 02 Analytic Functions/2.5 Harmonic Functions and Laplace's Equation.md
+++ /Users/gradyclopton/ObsidianVaults/complex_analysis/Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 02 Analytic Functions/2.5 Harmonic Functions and Laplace's Equation.md
@@ -8,7 +8,7 @@
 
 
 
-> [!review]
+> [!review|7354709e-575d-5ff7-b702-a15fe6a84b0a.local at=756dfe1a-89c1-50a5-98f8-73880e3e3020]
 > 1. A homogeneous plate with insulated lateral surfaces has its boundary held at a fixed temperature distribution $b(x, y)$ that does not vary in time. What happens to the temperature inside the plate over time, and what partial differential equation is satisfied by this long-term temperature distribution?
 > 2. Define the Laplacian $\Delta u$ of a twice-differentiable real-valued function $u(x, y)$.
 > 3. What does the Laplacian of a function $u$ measure about $u$ 's behavior near a point, and what does this imply about a function whose Laplacian is zero?
@@ -95,7 +95,7 @@
 
 
 
-> [!exercise]
+> [!exercise|43e84031-6917-5ea3-86ae-a93a06f6968b.local at=382e26c7-34ef-5286-92c3-ebe600216a48]
 > Verify that constants and the functions $u(x, y)=x, u(x, y)=y, u(x, y)=x y$ are each harmonic on $\mathbb{R}^2$.
 
 
@@ -216,10 +216,18 @@
 Consider a two-dimensional plate of homogeneous material, with instlated lateral surfaces. We represent this plate by a region $\Omega$ in the complex plane (see _Figure 1_). Suppose that the temperature of the points on the boundary of the plate is given by a function of position $b(x, y)$ that does not change with time. It is a fact from thermodynamics that the temperature inside the plate will eventually reach and remain at an equilibrium
 
 
-> [!figure] Figure 1
-> 
-> ![](./images/af4f9593-dec7-4bc0-8d78-d25500419ec9-37_459_508_201_110.jpg)
-> Figure 1 The steady-state temperature distribution satisfies Laplace's equation.
+```scientific-figure
+id: 0ebfbe94-ea97-4a62-9d4c-eb1267d1a323
+numbered: false
+title: ""
+caption: "**Figure 1.** The steady-state temperature distribution satisfies Laplace's equation."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 02 Analytic Functions/images/af4f9593-dec7-4bc0-8d78-d25500419ec9-37_459_508_201_110.jpg
+    caption: ""
+```
 
 
 
@@ -241,7 +249,7 @@
 
 
 
-> [!review]
+> [!review|f39a595f-27af-5cf8-99bb-4d51e95c0f8a.local at=8ffc26ca-eb02-5c28-8a84-648d53998161]
 > How can analytic functions be used to produce harmonic functions? Prove your answer.
 
 
@@ -366,15 +374,16 @@
 second partial derivatives are continuous. One of the major results that we will develop in the following chapter guarantees that the real and imaginary parts of an analytic function have continuous partial derivatives of all orders. Thus, the steps that we used above are justified and $u$ and $v$ are harmonic.
 
 
-> [!theorem] Theorem 1: Analytic and Harmonic Functions
-> Suppose that $f=u+i v$ is analytic on an open set $S$. Then its real and inaginary parts $u(x, y)$ and $v(x, y)$ are harmonic on $S$.
+<!-- Source label: Theorem 1: Analytic and Harmonic Functions -->
+> [!theorem|85415a80-67bf-5079-8636-7064ce1f10bd.local at=34247b14-e17d-54b0-913f-1c2999b59ba0] Analytic and Harmonic Functions
+> Suppose that $f=u+i v$ is analytic on an open set $S$. Then its real and imaginary parts $u(x, y)$ and $v(x, y)$ are harmonic on $S$.
 
 
 What this result effectively does for us is provide us with many examples of harmonic functions; simply take the real or imaginary part of any analytic function.
 
 
 
-> [!exercise] Exercise 1: Harmonic functions
+> [!exercise|62c55853-5c38-5a80-b2c8-841183c0d36f.local at=e65c3cfb-8314-552d-8c17-b2db92b47d42] Exercise 1: Harmonic functions
 > Show that the following are harmonic functions in the stated region.
 > (a) $u(x, y)=x^{2}-y^{2}$ on $\mathbb{C}$.
 > (b) $u(x, y)=e^{x} \sin y$ on $\mathbb{C}$.
@@ -645,7 +654,7 @@
 
 
 
-> [!review]
+> [!review|a96684a0-c638-5012-be60-407f141eb1e4.local at=1e4ee029-6130-5a65-b2a6-5d360f64411d]
 > 1. Under what conditions is a linear combination $a u+b v$ of two functions $u, v$ harmonic on an open set $S$ ? Prove your answer.
 > 2. What can be said about the pointwise product $u v$ of two harmonic functions $u, v$ on an open set $S$ ? Justify your answer.
 
@@ -767,7 +776,7 @@
 +++++
 
 
-> [!exercise]
+> [!exercise|08e85a4d-7e7e-57f7-9ad8-1cc158c071a2.local at=8bda7511-3e83-54ce-98ae-a53bba186e40]
 > 1. Show that $\phi(x, y)=2\left(x^2-y^2\right)+7$ is harmonic on $\mathbb{R}^2$.
 > 2. Show that $\phi(x, y)=(a x+b)(c y+d)$ is harmonic on $\mathbb{R}^2$ for any real constants $a, b, c, d$ .
 > 3. Show that $u(x, y)=x^2$ is not harmonic on $\mathbb{R}^2$.
@@ -893,8 +902,9 @@
 
 
 
-> [!proposition] Proposition 1: Linearity
-> Suppose that $u$ and $v$ are harmonic on an open set $S$, and $a, b$ are resed constants. Then $a u(x, y)+b v(x, y)$ is harmonic on $S$.
+<!-- Source label: Proposition 1: Linearity -->
+> [!proposition|b0be787d-715a-5b55-b91e-9a9426bb5e67.local at=64b35c27-03c0-5fba-9a6c-8fe7acbdd5de] Linearity
+> Suppose that $u$ and $v$ are harmonic on an open set $S$, and $a, b$ are real constants. Then $a u(x, y)+b v(x, y)$ is harmonic on $S$.
 
 
 
@@ -909,7 +919,7 @@
 # 2.5.3 Harmonic Conjugates
 
 
-> [!review]
+> [!review|61da94b2-a015-59dc-8489-1796253db62b.local at=6ef3cb73-ac12-5746-882e-653daa048ea5]
 > Given a harmonic function $u$ on a region $\Omega$, what additional function must be supplied to produce an analytic function $f$ on $\Omega$ with $\operatorname{Re}(f)=u$, and what properties must it satisfy? Is the required function always guaranteed to exist on $\Omega$ ?
 
 
@@ -968,7 +978,7 @@
 
 
 
-> [!exercise] Exercise 2: Finding harmonic conjugates
+> [!exercise|8aef26a8-9953-5687-a8ba-81095271b539.local at=c0aeb1a5-2c5c-5fe4-a174-4845b296b594] Exercise 2: Finding harmonic conjugates
 > Show that $u(x, y)=x^{2}-y^{2}+x$ is harmonic in the entire plane and find a harmonic conjugate.
 
 
@@ -1131,7 +1141,7 @@
 ++++
 
 
-> [!review]
+> [!review|9cd45d05-b7e4-5dd0-9daf-40ac75de43fb.local at=daf5c968-8467-58e8-bdd1-67bc1e5072de]
 > Given that $v$ is a harmonic conjugate of a harmonic function $u$, how can a harmonic conjugate of $v$ be expressed in terms of $u$ ? Prove your answer.
 
 
@@ -1218,7 +1228,8 @@
 
 So, from Example 2, a harmonic conjugate of $u(x, y)=x^{2}-y^{2}+x$ is $v(x, y)=2 x y+y$. What is a harmonic conjugate of $v(x, y)=2 x y+y$ ? Surely it is related to $u$. Indeed, you can check that a conjugate of $v$ is $-u(x, y)=-x^{2}+y^{2}-x$. More generally, we have the following useful result.
 
-> [!proposition] Proposition 2
+<!-- Source label: Proposition 2 -->
+> [!proposition|cb29896b-dde2-5942-a716-3549752f1c6b.local at=bd687f57-ed46-583c-be3d-8c6a9ccd0250] Reversing a Harmonic Conjugate Pair
 > Suppose that $u$ is harmonic and that $v$ is a harmonic conjugate of $u$. Then $-u$ is a harmonic conjugate of $v$.
 
 
@@ -1229,7 +1240,7 @@
 
 
 
-> [!review]
+> [!review|7f015a0b-46d7-5f33-ac4d-04b060ab3489.local at=004c7d5b-9205-5f31-9cc9-7f3b3a0ea3e4]
 > 1. If $v_1$ and $v_2$ are both harmonic conjugates of the same harmonic function $u$ on a region $\Omega$, how must $v_1$ and $v_2$ be related? Prove your answer.
 > 2. If $v$ is a harmonic conjugate of a harmonic function $u$ on a region $\Omega$, determine whether $v$ is also a harmonic conjugate of $u+c$ for every real constant $c$. Prove your answer.
 > 3. What does it mean for two curves in the plane to be orthogonal at a point of intersection, and what does it mean for two families of curves to be orthogonal?
@@ -1495,7 +1506,8 @@
 In Example 2, we found the harmonic conjugate of $u$ up to an arbitrary additive real constant. In fact, the following properties of the harmonic conjugate are not hard to prove (Exercise 18).
 
 
-> [!proposition] Proposition 3
+<!-- Source label: Proposition 3 -->
+> [!proposition|2fd5db90-d2cc-56c6-b6cc-0d56328e8461.local at=72e6f416-8697-5ecc-b2cf-b051a23078b7] Uniqueness and Additive Constants for Harmonic Conjugates
 > Suppose that $u$ is a harmonic function in a region $\Omega$. Then
 > (i) if $v_{1}$ and $v_{2}$ are harmonic conjugates of $u$ in $\Omega$, then $v_{1}$ and $v_{2}$ must differ by a real constant.
 > (ii) If $v$ is a harmonic conjugate of $u$, then $v$ is also a harmonic conjugate of $u+c$ where $c$ is any real constant.
@@ -1507,11 +1519,18 @@
 
 
 
-> [!figure] Figure 2
-> 
-> 
-> ![](./images/af4f9593-dec7-4bc0-8d78-d25500419ec9-40_480_528_1485_142.jpg)
-> Figure 2 The curves $C_{1}$ and $C_{2}$ are orthogonal at $A$ if the tangent lines $L_{1}$ and $L_{2}$ (at $A$ ) are orthogonal.
+```scientific-figure
+id: 053964c8-b603-407d-9247-b31c42be0aa7
+numbered: false
+title: ""
+caption: "**Figure 2.** The curves $C_{1}$ and $C_{2}$ are orthogonal at $A$ if the tangent lines $L_{1}$ and $L_{2}$ (at $A$ ) are orthogonal."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 02 Analytic Functions/images/af4f9593-dec7-4bc0-8d78-d25500419ec9-40_480_528_1485_142.jpg
+    caption: ""
+```
 
 
 
@@ -1555,9 +1574,9 @@
 
 since by the Cauchy-Riemann equations, $\partial v / \partial x=-\partial u / \partial y$ and $\partial v / \partial y= \partial u / \partial x$. Comparing (6) and (7), we see that the slopes of the tangent lines satisfy the orthogonality relation (3), and hence the level curves of $u$ are orthogonal to the level curves of $v$. This orthogonality relation also holds when the tangents are horizontal and vertical. We thus have the following result.
 
-> [!theorem] Theorem 2: Orthogonality of Level Curves
+<!-- Source label: Theorem 2: Orthogonality of Level Curves -->
+> [!theorem|192c37f1-0b24-5836-91b4-767ea387e566.local at=281f9cdb-f49d-5b46-9803-5fa64585da04] Orthogonality of Level Curves
 > Suppose that $u$ is a harmonic function in a region $\Omega$ and let $v$ be a harmonic conjugate of $u$ in $\Omega$, so that $f=u+i v$ is analytic in $\Omega$. Then, the two families of level curves, $u(x, y)=C_{1}$ and $v(x, y)=C_{2}$, are orthogonal at every point where $f^{\prime}(z) \neq 0$.
-> 
 
 
 As an illustration, we show in _Figure 3(a) and (b)_ the level curves of the harmonic function $u=x^{2}-y^{2}+x$ and its conjugate $v(x, y)=2 x y+y$ (see Exercise 2). The graphs of the two families are superposed in Figure 3(c) to illustrate their orthogonality.
@@ -1567,34 +1586,25 @@
 
 
 
-> [!figure] FIgure 3
-> 
-> ```horizontal
-> 
-> ![](./images/af4f9593-dec7-4bc0-8d78-d25500419ec9-42_421_423_278_686.jpg)
-> (a)
-> ---
-> 
-> 
-> 
-> ![](./images/af4f9593-dec7-4bc0-8d78-d25500419ec9-42_419_417_278_1164.jpg)
-> (b)
-> 
-> ---
-> 
-> 
-> 
-> ![](./images/af4f9593-dec7-4bc0-8d78-d25500419ec9-42_415_406_278_1639.jpg)
-> (c)
-> 
-> ```
-> 
-> 
-> Figure 3 (a) Level curves of $u(x, y)=x^{2}-y^{2}+x$.
-> (b) Level curves of $v(x, y)=2 x y+y$.
-> (c) The level curves of $u$ and $v$ are orthogonal.
-> 
-> 
+```scientific-figure
+id: 17cebb25-1467-44c5-bf6c-3b5d23fd8891
+numbered: false
+title: ""
+caption: |-
+  Figure 3 (a) Level curves of $u(x, y)=x^{2}-y^{2}+x$.
+  (b) Level curves of $v(x, y)=2 x y+y$.
+  (c) The level curves of $u$ and $v$ are orthogonal.
+captionVisible: true
+captionPosition: below
+columns: 3
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 02 Analytic Functions/images/af4f9593-dec7-4bc0-8d78-d25500419ec9-42_421_423_278_686.jpg
+    caption: ""
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 02 Analytic Functions/images/af4f9593-dec7-4bc0-8d78-d25500419ec9-42_419_417_278_1164.jpg
+    caption: ""
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 02 Analytic Functions/images/af4f9593-dec7-4bc0-8d78-d25500419ec9-42_415_406_278_1639.jpg
+    caption: ""
+```
 
 
 
@@ -1602,7 +1612,7 @@
 # 2.5.4 Solving and Interpreting Dirichlet Problems
 
 
-> [!review]
+> [!review|bb8c31bf-846d-5b2b-83f9-6b05e50ff4bd.local at=5cccb303-8d3c-5343-b0f7-8ea2663cb7b1]
 > 1. What characterizes the harmonic functions (on appropriate subdomains of $\mathbb{C}$ ) that are constant on rays from the origin? For what class of Dirichlet problems are such functions natural candidate solutions?
 > 2. What characterizes the harmonic functions on $\mathbb{R}^2$ that are independent of $y$ ? Prove your answer. For what class of Dirichlet problems are such functions natural candidate solutions?
 
@@ -1725,7 +1735,7 @@
 +++++
 
 
-> [!exercise]
+> [!exercise|e05f2d20-4266-5d79-b352-964ad61d71ef.local at=164e38da-4784-52ee-9676-a05a2f41d6c1]
 > Let $u=a \operatorname{Arg} z+b$. Show that $u(x, y)=a \operatorname{Arg} z+b$ (for real constants $a, b$ ) is harmonic on $\mathbb{C} \backslash(-\infty, 0]$ and is constant on rays from the origin.
 
 
@@ -1817,7 +1827,7 @@
 
 
 
-> [!exercise]
+> [!exercise|48d8d9fc-d29f-5a9b-ae1a-ac569b1b8e8c.local at=7d9c789f-632b-532e-a60b-c0d63822b904]
 > Let $u=a \ln |z|+b$. Show that $u(z)=a \ln |z|+b$ (for real constants $a, b$ ) is harmonic on $\mathbb{C} \backslash\{0\}$ and depends only on $|z|$.
 
 
@@ -1896,16 +1906,22 @@
 We now return to our main topic: that of solving Dirichlet problems. Let us first mention an interesting example of a harmonic function, $u(x, y)= a \operatorname{Arg} z+b$, which is harmonic by Example 1(c) and Proposition 1. Because $\operatorname{Arg} z$ is constant on rays (independent of $r$ ), it follows that $u=a \operatorname{Arg} z+b$ is also constant on rays. (In fact, this is the only harmonic function with such a property. See Exercise 49.) Thus $u$ is a good candidate for a solution of Dirichlet problems in which the boundary data is constant on rays or independent of $r$. We illustrate these ideas with an example.
 
 
-> [!exercise] Exercise 3: A Dirichlet problem in a quadrant
+> [!exercise|167de579-b968-5a30-9e84-f03d02a3ec96.local at=0d6f8654-aee7-50c1-871c-e3f379ac77fb] Exercise 3: A Dirichlet problem in a quadrant
 > 
 > Find the steady-state temperature $u(x, y)$ in a large sheet of metal occupying a quadrant of the plane, whose boundary is held at the constant temperatures $100^{\circ}$ on the bottom edge and $50^{\circ}$ on the left edge.
 > 
-> > [!figure]
-> > 
-> > ![300](./images/af4f9593-dec7-4bc0-8d78-d25500419ec9-42_485_542_1401_100.jpg)
-> > Dirichlet problem
-> > 
-> > 
+> ```scientific-figure
+> id: aa4f33fe-3eb8-4299-b397-35bf4bed86f7
+> numbered: false
+> title: ""
+> caption: Dirichlet problem
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 02 Analytic Functions/images/af4f9593-dec7-4bc0-8d78-d25500419ec9-42_485_542_1401_100.jpg
+>     caption: ""
+> ```
 > 
 > 
 
@@ -2055,10 +2071,18 @@
 
 
 
-> [!figure] Figure 5: For Exercise 3
-> 
-> ![300](./images/af4f9593-dec7-4bc0-8d78-d25500419ec9-43_452_470_196_132.jpg)
-> Figure 5
+```scientific-figure
+id: c764ea47-edc8-4e1a-bd21-4ae45302b709
+numbered: false
+title: ""
+caption: "**Figure 5.** For Exercise 3"
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 02 Analytic Functions/images/af4f9593-dec7-4bc0-8d78-d25500419ec9-43_452_470_196_132.jpg
+    caption: ""
+```
 
 
 
@@ -2070,13 +2094,24 @@
 
 
 
-> [!exercise] Exercise 4: Dirichlet problem in an infinite strip
+> [!exercise|b2b09fc2-e44f-53bd-bda8-31d776aba347.local at=ea20ecf2-de0e-5976-aeab-48ef53486a7c] Exercise 4: Dirichlet problem in an infinite strip
 > Solve the Dirichlet problem on the infinite strip $\{(x, y): 0<y<1\}$ with boundary conditions $u=0^{\circ}$ on $y=0$ and $u=100^{\circ}$ on $y=1$.
 > 
-> > [!figure] Figure 6: For Exercise 4
-> > 
-> > ![300](./images/af4f9593-dec7-4bc0-8d78-d25500419ec9-43_469_503_1047_101.jpg)
-> > Figure 6 Dirichlet problem in Example 4.
+> ```scientific-figure
+> id: 82a8e8bd-ad5e-4a41-8d38-0b2b3d4f8e0d
+> numbered: false
+> title: ""
+> caption: |-
+>   **Figure 6.** For Exercise 4
+> 
+>   Dirichlet problem in Example 4.
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 02 Analytic Functions/images/af4f9593-dec7-4bc0-8d78-d25500419ec9-43_469_503_1047_101.jpg
+>     caption: ""
+> ```
 > 
 > 
 > 
@@ -2242,7 +2277,7 @@
 # 2.5.5 Harmonic Conjugates, Isotherms, and Heat Flow
 
 
-> [!review]
+> [!review|4ce59daa-ce7c-5148-a017-84104cc5558a.local at=0b051725-dfb6-5582-bf45-bbd74bd683dc]
 > 1.) What are isotherms in a steady-state heat distribution on a plate, and in terms of the temperature function $u(x, y)$, what curves do they correspond to?
 > 2.) Why are the curves of heat flow in a steady-state temperature distribution orthogonal to the isotherms?
 > 3.) How can a harmonic conjugate $v$ of a steady-state temperature distribution $u$ be used to determine the curves of heat flow on the plate, and why does this method work?
@@ -2338,16 +2373,26 @@
 
 
 
-> [!exercise] Exercise 5: Isotherms
+> [!exercise|017361bf-360a-5807-91d5-8497a0d4d51f.local at=0378a913-a0f7-5913-afc1-82ebcc0f9d1a] Exercise 5: Isotherms
 > 
 > Find the isotherms in Exercise 3.
 > 
 > 
-> > [!figure] Figure 7: For Exercise 5
-> > 
-> > ![](./images/af4f9593-dec7-4bc0-8d78-d25500419ec9-44_487_543_244_106.jpg)
-> > 
-> > Figure 7 Isotherms in Example 5.
+> ```scientific-figure
+> id: af8246e6-a74e-4003-8099-ffdc6410e70b
+> numbered: false
+> title: ""
+> caption: |-
+>   **Figure 7.** For Exercise 5
+> 
+>   Isotherms in Example 5.
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 02 Analytic Functions/images/af4f9593-dec7-4bc0-8d78-d25500419ec9-44_487_543_244_106.jpg
+>     caption: ""
+> ```
 > 
 > 
 > 
@@ -2444,16 +2489,27 @@
 So to find the curves of heat flow in a plate, it is enough to find a harmonic conjugate $v(x, y)$ of the steady-state temperature distribution $u(x, y)$, since by Theorem 2 the level curves of $v$ are orthogonal to the level curves of $u$ We illustrate this process with an example.
 
 
-> [!exercise] Exercise 6: Curves of Heat Flow
+> [!exercise|d2201a76-9140-5bf9-90ec-149b9cccbeeb.local at=0ec8a942-a1e0-5e9e-a54e-9b656f5526fc] Exercise 6: Curves of Heat Flow
 > 
 > 
 > Find the curves of heat flow in Example 3.
 > 
 > 
-> > [!figure] Figure 8: For Exercise 6
-> > 
-> > ![300](./images/af4f9593-dec7-4bc0-8d78-d25500419ec9-45_477_510_300_76.jpg)
-> > Figure 8 Curves of heat flow in Example 6, along with the isotherms.
+> ```scientific-figure
+> id: 6d4bfeae-ead5-455f-8884-f33714e59363
+> numbered: false
+> title: ""
+> caption: |-
+>   **Figure 8.** For Exercise 6
+> 
+>   Curves of heat flow in Example 6, along with the isotherms.
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 02 Analytic Functions/images/af4f9593-dec7-4bc0-8d78-d25500419ec9-45_477_510_300_76.jpg
+>     caption: ""
+> ```
 > 
 > 
 > 
@@ -2552,7 +2608,7 @@
 
 
 
-> [!review]
+> [!review|a721ec92-2d19-59f7-ae4a-c36308b75c08.local at=43c81044-dfc9-581f-8fa8-1280a42c899a]
 > 1.) What strategic idea underlies the method of conformal mappings for solving Dirichlet problems?
 > 2.) What does it mean for a mapping $w=f(z)$ to be a conformal mapping of a region $\Omega$, and what geometric properties does such a mapping have that make it suitable for transforming a Dirichlet problem on $\Omega$ into one posed on the image region?
 > 3.) If $U$ is a harmonic function on a region $\Omega^{\prime}$ and we pull it back to a region $\Omega$ via a mapping $w=f(z)$ (forming $u(z)=U(f(z))$ ), under what hypotheses on $f$ is $u$ guaranteed to be harmonic on $\Omega$ ? Prove your answer.
@@ -2573,14 +2629,15 @@
 
 
 
-> [!NOTE]
+> [!note|c708512a-9e19-57b0-8cac-c0815ac14864.local at=42ad3861-0af6-58a7-bf50-1a333123ec7e]
 > To understand the meaning of $U \circ f(z)$ where $f$ is complexvalued and $U$ is a function of two variables, write $U \circ f(z)=U(\operatorname{Re} f(z), \operatorname{Im} f(z))$. For example, if $f(z)= e^{z}=e^{x} \cos y+i e^{x} \sin y$ and $U(s, t)=s t$, then $U \circ f(z)= e^{2 x} \cos y \sin y$.
 
 
 
 
 
-> [!Theorem] Theorem 3: Invariance of Laplace's Equation
+<!-- Source label: Theorem 3: Invariance of Laplace's Equation -->
+> [!theorem|833a8d0a-1ab5-5611-ad92-735684872993.local at=259a7183-1ac0-5a8e-ac46-9a85dd73ede5] Invariance of Laplace's Equation
 > Suppose that $f$ is an analytic mapping of $\Omega$ into $\Omega^{\prime}$ and $U$ is a harmonic function on $\Omega^{\prime}$. Then $U \circ f$ is harmonic in $\Omega$. Thus, if $U$ satisfies $\Delta U=0$ on $\Omega^{\prime}$, then $u=U \circ f$ satisfies $\Delta u=0$ on $\Omega$.
 
 **Proof** 
@@ -2588,7 +2645,7 @@
 
 
 
-> [!review]
+> [!review|926466ac-e590-5264-b2c8-857322749971.local at=df8249e8-a57a-5e9e-a015-6617592da1af]
 > Given a Dirichlet problem on a region $\Omega$ (Laplace's equation with prescribed boundary data $b$ on $\Gamma$ ), and an analytic mapping $w=f(z)$ that is one-to-one on $\Omega$ and its boundary, how can $f$ be used to transform the problem into a Dirichlet problem posed on the image region, and how does a solution of the transformed problem then yield a solution of the original? Prove your answer.
 
 
@@ -2708,11 +2765,21 @@
 Now suppose that you want to use a conformal mapping $w=f(z)$ to solve the Dirichlet problem $\Delta u=0$ in $\Omega$ and $u(z)=b(z)$ on the boundary $\Gamma$ of $\Omega$. Suppose also that $f$ is one-to-one on $\Omega$ and its boundary $\Gamma$. Here is how the method works (see _Figure 9_ as you read through the steps).
 
 
-> [!figure] Figure 9: For Proof to Theorem 3
-> 
-> ![](./images/af4f9593-dec7-4bc0-8d78-d25500419ec9-46_519_1162_1082_766.jpg)
-> 
-> The conformal mapping method. If $f(z)$ is analytic and one-to-one on $\Omega$ and its boundary $\Gamma$, then $\Omega^{\prime}= f[\Omega]$ is a region with boundary $\Gamma^{\prime}=f[\Gamma]$. The boundary function $b(z)$ ( $z$ on $\Gamma$ ) is used to define a boundary function $b \circ f^{-1}(w)$ for all $w$ on $\Gamma$, where $f^{-1}$ is the inverse of $f$.
+```scientific-figure
+id: 3cb3a543-055e-49e4-8210-f5c438cae207
+numbered: false
+title: ""
+caption: |-
+  **Figure 9.** For Proof to Theorem 3
+
+  The conformal mapping method. If $f(z)$ is analytic and one-to-one on $\Omega$ and its boundary $\Gamma$, then $\Omega^{\prime}= f[\Omega]$ is a region with boundary $\Gamma^{\prime}=f[\Gamma]$. The boundary function $b(z)$ ( $z$ on $\Gamma$ ) is used to define a boundary function $b \circ f^{-1}(w)$ for all $w$ on $\Gamma$, where $f^{-1}$ is the inverse of $f$.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 02 Analytic Functions/images/af4f9593-dec7-4bc0-8d78-d25500419ec9-46_519_1162_1082_766.jpg
+    caption: ""
+```
 
 
 
@@ -2726,15 +2793,23 @@
 
 
 
-> [!exercise] Exercise 7
+> [!exercise|0f7f0954-b85c-5e83-9239-d7a3a15aadbf.local at=fc435832-deba-5a6b-8bb7-28280256372c] Exercise 7
 > (a) Solve the Dirichlet problem in the semi-infinite strip $\Omega$ shown in _Figure 10_.
 > (b) Discuss the isotherms and lines of heat flow of the solution.
 > 
 > 
-> > [!figure] Figure 10
-> > 
-> > ![300](./images/af4f9593-dec7-4bc0-8d78-d25500419ec9-47_468_498_188_96.jpg)
-> > Dirichlet problem in Exercise 7.
+> ```scientific-figure
+> id: b86f8b49-4190-4b4a-b698-4478f7528531
+> numbered: false
+> title: ""
+> caption: "**Figure 10.** Dirichlet problem in Exercise 7."
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 02 Analytic Functions/images/af4f9593-dec7-4bc0-8d78-d25500419ec9-47_468_498_188_96.jpg
+>     caption: ""
+> ```
 > 
 > 
 
@@ -2963,11 +3038,21 @@
 The following static plot shows a representative family of isotherms and curves of heat flow in the strip.
 
 
-> [!figure] Python rendering for Exercise 7
-> 
-> ![700](./images/exercise7_isotherms_heatflow_python_static.png)
-> 
-> Static Python rendering of the isotherms $u(x, y)=T$ and heat-flow curves $\sin ^{2} x+\sinh ^{2} y=R^{2}$ for Exercise 7.
+```scientific-figure
+id: 30cb408e-60f3-4ca8-b7d6-604a89015b24
+numbered: false
+title: ""
+caption: |-
+  Python rendering for Exercise 7
+
+  Static Python rendering of the isotherms $u(x, y)=T$ and heat-flow curves $\sin ^{2} x+\sinh ^{2} y=R^{2}$ for Exercise 7.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 02 Analytic Functions/images/exercise7_isotherms_heatflow_python_static.png
+    caption: ""
+```
 
 
 ```Mathematica title:""
@@ -3196,20 +3281,41 @@
 ##### problem 7.a
 
 
-> [!figure] Figure 11: For problem 7.a
-> 
-> ![](./images/af4f9593-dec7-4bc0-8d78-d25500419ec9-47_424_1237_1573_689.jpg)
-> 
-> Mapping the semiinfinite vertical strip onto the upper half-plane. Note the boundary correspondence.
-
-
-
-
-
-> [!figure] Figure 12: For Problem 7.a
-> 
-> ![](./images/af4f9593-dec7-4bc0-8d78-d25500419ec9-48_307_553_372_104.jpg)
-> Figure 12 The inverse cotangent takes its values in $(0, \pi)$.
+```scientific-figure
+id: 16dd6af4-1238-445f-8d29-2c8963dd9dbf
+numbered: false
+title: ""
+caption: |-
+  **Figure 11.** For problem 7.a
+
+  Mapping the semiinfinite vertical strip onto the upper half-plane. Note the boundary correspondence.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 02 Analytic Functions/images/af4f9593-dec7-4bc0-8d78-d25500419ec9-47_424_1237_1573_689.jpg
+    caption: ""
+```
+
+
+
+
+
+```scientific-figure
+id: 2e92666c-ec34-4858-ac1b-ec3374c76efc
+numbered: false
+title: ""
+caption: |-
+  **Figure 12.** For Problem 7.a
+
+  The inverse cotangent takes its values in $(0, \pi)$.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 02 Analytic Functions/images/af4f9593-dec7-4bc0-8d78-d25500419ec9-48_307_553_372_104.jpg
+    caption: ""
+```
 
 
 
@@ -3219,11 +3325,21 @@
 
 
 
-> [!figure] Figure 13: For Problem 7.b
-> 
-> ![300](./images/af4f9593-dec7-4bc0-8d78-d25500419ec9-48_609_553_1350_112.jpg)
-> 
-> Isotherms and curves of heat flow in Example 7. Note the orthogonality of the curves.
+```scientific-figure
+id: 2a3102f9-f152-467e-b73c-e835cf0b917f
+numbered: false
+title: ""
+caption: |-
+  **Figure 13.** For Problem 7.b
+
+  Isotherms and curves of heat flow in Example 7. Note the orthogonality of the curves.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 02 Analytic Functions/images/af4f9593-dec7-4bc0-8d78-d25500419ec9-48_609_553_1350_112.jpg
+    caption: ""
+```
 
 
 
@@ -3236,7 +3352,7 @@
 
 
 
-> [!review]
+> [!review|2dcbf852-abb5-5962-8b88-2821fbefd6c7.local at=088e02e0-4552-514f-b3c3-5e0afce75d68]
 > Why might the boundary data of a Dirichlet problem fail to determine a unique solution, and what additional condition on the solution restores uniqueness?
 
 
@@ -3276,7 +3392,7 @@
 +++++
 
 
-> [!exercise]
+> [!exercise|361e27a2-2bd7-5e34-9201-b37db7ad9477.local at=362008f4-ce61-5dff-ada3-24eee6d4eb37]
 > Show that if $u(x, y)$ is the solution to the Dirichlet problem of Example 3 (Laplace's equation on the first quadrant with $u=100$ on the positive $x$-axis and $u=50$ on the positive $y$-axis), then $\psi(x, y)=u(x, y)+x y$ is also a solution.
 
 
@@ -3376,7 +3492,7 @@
 
 # Exercises 2.5
 
-> [!exercise] Exercise 8
+> [!exercise|567f7ad6-e973-58be-b9ca-172be37c01e1.local at=95eba983-32ae-51d7-86d6-16770d270e6d] Exercise 8
 > In problemss 1-12, determine the set on which the given function is harmonic. You may verify Laplace's equation (1) directly or use Theorem 1.
 > 
 > 1. $x^{2}-y^{2}+2 x-y$.
@@ -4047,7 +4163,7 @@
 
 
 
-> [!exercise] Exercise 9
+> [!exercise|60571686-d008-5478-91d5-d7f36dfb589c.local at=644b376b-4cf2-566c-adba-e68b8dcc54e6] Exercise 9
 > In Problems 13-16, find a harmonic conjugate $v(x, y)$ of the given harmonic function $u(x, y)$ by using the method of Example 2 . Check your answer by verifying the Cauchy-Riemann equations.
 > 13. $x+2 y$.
 > 14. $x^{2}-y^{2}-x y$.
@@ -4828,7 +4944,7 @@
 ++++
 
 
-> [!exercise] Exercise 10
+> [!exercise|808a9cb7-3c4a-59a7-991e-4ac57d2e4aae.local at=91271a04-c83f-5bbf-944f-13a51f133412] Exercise 10
 > 17. Let $n$ be any integer. (a) Show that $u(r, \theta)=r^{n} \cos (n \theta)$ and $v(r, \theta)= r^{n} \sin (n \theta)$ are harmonic on $\mathbb{C}$ if $n \geq 0$ and on $\mathbb{C} \backslash\{0\}$ if $n<0$. (b) Find their respective harmonic conjugates. **(Hint: Consider $f(z)=z^{n}$ in polar coordinates.)**
 
 
@@ -5246,7 +5362,7 @@
 
 
 
-> [!exercise] Exercise 11
+> [!exercise|eb868cd0-7ba3-5763-9d8d-0eeebc6792df.local at=33c97c4c-3794-5240-b9a7-101e9dea5639] Exercise 11
 > 18. (a) Prove Proposition 1.
 > (b) Prove Proposition 3.
 
@@ -5527,7 +5643,7 @@
 ++++
 
 
-> [!exercise] Exercise 12
+> [!exercise|432afe2d-e828-5fc5-b8fb-aece170ed329.local at=cac88705-7e94-5a2d-87c5-11ab751b2fb4] Exercise 12
 > 19. Show that if $u$ and $u^{2}$ are both harmonic in a region $\Omega$, then $u$ must be constant. **(Hint: Plug $u^{2}$ into Laplace's equation and show that $u_{x}=u_{y}=0$.)**
 > 20. Show that if $u, v$, and $u^{2}+v^{2}$ are harmonic in a region $\Omega$, then $u$ and $v$ must be constant. **(Hint: Plug $u^{2}+v^{2}$ into Laplace's equation and show that $u_{x}=u_{y}=0$ and $v_{x}=v_{y}=0$.)**
 > 21. Suppose that $u$ is harmonic and $v$ is a harmonic conjugate of $u$. Show that $u^{2}-v^{2}$ and $u v$ are both harmonic. **(Hint: Consider $(u+i v)^{2}$.)**
@@ -5826,7 +5942,7 @@
 
 
 
-> [!exercise] Exercise 13
+> [!exercise|4950ca80-6891-5835-861d-1f7e62412d28.local at=d9ba4489-9fa7-57ae-80e4-759a8311de71] Exercise 13
 > 22. Use Exercises 20 and 21 to show that if $f$ is analytic in a region $\Omega$ and $|f|$ is constant in $\Omega$, then $f$ must be constant in $\Omega$. (A different proof was outlined in Exercise 38, Section 2.4.)
 
 
@@ -5909,7 +6025,7 @@
 ++++
 
 
-> [!exercise] Exercise 14
+> [!exercise|1ef29593-48bc-5451-9939-058078c8c816.local at=5599ff24-86e3-5e39-b02f-47b11c314afb] Exercise 14
 > 23. **Translating and dilating a harmonic function.** Suppose that $u$ is harmonic. Show that the following functions are also harmonic:
 > (a) $\quad u(x-\alpha, y-\beta)$, where $\alpha$ and $\beta$ are real numbers;
 > (b) $u(\alpha x, \alpha y)$, where $\alpha \neq 0$ is a real number.
@@ -6137,7 +6253,7 @@
 
 
 
-> [!exercise] Exercise 15
+> [!exercise|6455aca6-6273-5025-9867-89e4eff73c85.local at=20bbdf6c-1843-5ac1-aa52-ec8d65d69cbf] Exercise 15
 > 24. (a) Suppose that $u(x, y)$ is harmonic. Show that $u(x,-y)$ is also harmonic.
 > 
 > (b) Suppose that $u(x, y)$ is harmonic. Show that $u\left(\frac{x}{x^{2}+y^{2}}, \frac{y}{x^{2}+y^{2}}\right)$ is harmonic.
@@ -6383,7 +6499,7 @@
 
 
 
-> [!exercise] Exercise 16
+> [!exercise|28749d0c-711d-5afc-9d6c-434af655a38c.local at=12629119-a9ad-51c1-90fb-6806e1639537] Exercise 16
 > 
 > 
 > 25. **Harmonic functions independent of $y$.** 
@@ -6391,9 +6507,18 @@
 > (b) Consider the Dirichlet problem in the infinite vertical strip in _Figure 14_. Because the boundary values do not depend on $y$, it is plausible to try for a solution a harmonic function whose values do not depend on $y$. Solve the problem, using (a).
 > 
 > 
-> > [!figure] Figure 14
-> > ![300](./images/af4f9593-dec7-4bc0-8d78-d25500419ec9-50_493_558_342_84.jpg)
-> > Dirichlet problem in problem 25.
+> ```scientific-figure
+> id: 4d539050-1a8e-4dac-90b9-7e3c1d431a86
+> numbered: false
+> title: ""
+> caption: "**Figure 14.** Dirichlet problem in problem 25."
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 02 Analytic Functions/images/af4f9593-dec7-4bc0-8d78-d25500419ec9-50_493_558_342_84.jpg
+>     caption: ""
+> ```
 > 
 > 
 > (c) Determine and plot the isotherms and curves of heat flow.
@@ -6784,7 +6909,7 @@
 
 
 
-![|center|400](Pasted%20image%2020260425005540.png)
+![|center|400](Books/Asmar%20Applied%20Complex%20Analysis%20with%20Applications%20to%20Differential%20Equations/Chapter%2002%20Analytic%20Functions/images/Pasted%20image%2020260425005540.png)
 
 
 
@@ -6830,15 +6955,23 @@
 
 
 
-> [!exercise] Exercise 17
+> [!exercise|6c0ec3e9-90da-5347-9fb5-b436df8323c9.local at=ea2e50ac-1f0e-5a71-8094-bd2db1c7ff15] Exercise 17
 > 
 > 26. **A Dirichlet problem in an infinite vertical strip.** 
 > (a) Solve the Dirichlet problem in _Figure 15_.
 > 
-> > [!figure] Figure 15
-> > 
-> > ![[Pasted image 20260401005538.png|300]]
-> > Dirichlet problem in Problem 26.
+> ```scientific-figure
+> id: de324408-5f1c-48a9-a457-55328a61efca
+> numbered: false
+> title: ""
+> caption: "**Figure 15.** Dirichlet problem in Problem 26."
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Pasted image 20260401005538.png
+>     caption: ""
+> ```
 > 
 > 
 > (b) Determine and plot the isotherms and curves of heat flow.
@@ -7128,7 +7261,7 @@
 
 
 
-![|center|400](Pasted%20image%2020260425005632.png)
+![|center|400](Books/Asmar%20Applied%20Complex%20Analysis%20with%20Applications%20to%20Differential%20Equations/Chapter%2002%20Analytic%20Functions/images/Pasted%20image%2020260425005632.png)
 
 
 
@@ -7175,16 +7308,24 @@
 
 
 
-> [!exercise] Exercise 18
+> [!exercise|48f95fd9-0220-5ba4-889f-c1a9413e333c.local at=11f42499-83f8-58cf-be9c-89c02e00ecc7] Exercise 18
 > 
 > 27. Harmonic functions independent of $r$. 
 > (a) Solve the Dirichlet problem in _Figure 16_. Because the boundary values do not depend on $r$, you should try for a solution a harmonic function whose values do not depend on $r$.
 > 
 > 
-> > [!figure] Figure 16
-> > 
-> > ![300](./images/af4f9593-dec7-4bc0-8d78-d25500419ec9-50_495_535_1109_852.jpg)
-> > Dirichlet problem in Exercise 27.
+> ```scientific-figure
+> id: 9ffe9f50-9dff-4179-b11b-94bfcba66d48
+> numbered: false
+> title: ""
+> caption: "**Figure 16.** Dirichlet problem in Exercise 27."
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 02 Analytic Functions/images/af4f9593-dec7-4bc0-8d78-d25500419ec9-50_495_535_1109_852.jpg
+>     caption: ""
+> ```
 > 
 > 
 > (b) Determine and plot the isotherms and curves of heat flow.
@@ -7510,7 +7651,7 @@
 
 
 
-![|center|500](Pasted%20image%2020260425010715.png)
+![|center|500](Books/Asmar%20Applied%20Complex%20Analysis%20with%20Applications%20to%20Differential%20Equations/Chapter%2002%20Analytic%20Functions/images/Pasted%20image%2020260425010715.png)
 
 
 
@@ -7566,14 +7707,23 @@
 
 
 
-> [!exercise] Exercise 19
+> [!exercise|3b4448e1-a2a8-5729-8b7f-1234cc721717.local at=5895c4a7-7682-5eee-a388-dc813add7d10] Exercise 19
 > 
 > 
 > 28. A Dirichlet problem in a wedge. 
 > (a) Solve the Dirichlet problem in _Figure 17_.
-> > [!figure] Figure 17
-> > ![300](./images/af4f9593-dec7-4bc0-8d78-d25500419ec9-50_498_503_1097_1592.jpg)
-> > Dirichlet problem in Exercise 28.
+> ```scientific-figure
+> id: 8d08afa7-175b-4e94-84c1-0df46a47e529
+> numbered: false
+> title: ""
+> caption: "**Figure 17.** Dirichlet problem in Exercise 28."
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 02 Analytic Functions/images/af4f9593-dec7-4bc0-8d78-d25500419ec9-50_498_503_1097_1592.jpg
+>     caption: ""
+> ```
 > 
 > (b) Determine and plot the isotherms and curves of heat flow.
 
@@ -7960,7 +8110,7 @@
 
 
 
-![|center|500](Pasted%20image%2020260425011022.png)
+![|center|500](Books/Asmar%20Applied%20Complex%20Analysis%20with%20Applications%20to%20Differential%20Equations/Chapter%2002%20Analytic%20Functions/images/Pasted%20image%2020260425011022.png)
 
 
 
@@ -8015,7 +8165,7 @@
 
 
 
-> [!exercise] Exercise 20
+> [!exercise|aad41b26-606e-5e1b-b863-b41be0a8829a.local at=f9f81ae9-cac5-53c0-8400-51ba47f39588] Exercise 20
 > 29. Harmonic functions independent of $\theta$. Suppose that $u(r, \theta)$ is a harmonic function, in polar coordinates.
 > (a) Suppose that $u$ depends only on $r$ and not $\theta$; hence $u(r, \theta)=u(r)$. Using the polar form of the Laplacian (12) in Exercise 47, show that $u(r)$ satisfies the (ordinary) differential equation in $r$
 > 
@@ -8027,10 +8177,18 @@
 > (b) Multiply the Euler equation by the integrating factor $r$ and notice that the need two linearly independent solutions. left side is now exact. Integrate to conclude $r u_{r}=c_{1}$, where $c_{1}$ is the constant of
 > 
 > 
-> > [!figure] Figure 21
-> > 
-> > ![300](./images/af4f9593-dec7-4bc0-8d78-d25500419ec9-51_470_496_1775_89.jpg)
-> > Figure 21 Dirichlet problem for problem 35.
+> ```scientific-figure
+> id: bad541c3-1ee3-4cf0-b2de-54a415a7be61
+> numbered: false
+> title: ""
+> caption: "**Figure 21.** Dirichlet problem for problem 35."
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 02 Analytic Functions/images/af4f9593-dec7-4bc0-8d78-d25500419ec9-51_470_496_1775_89.jpg
+>     caption: ""
+> ```
 > 
 > integration. Integrate again and find the general solution
 > 
@@ -8187,15 +8345,23 @@
 
 
 
-> [!exercise] Exercise 21
+> [!exercise|85240bb8-37eb-5e21-abb3-7de38090d2f9.local at=cf8c09d6-2f9f-53cc-859a-5a51d3dc5e40] Exercise 21
 > 
 > 30. Dirichlet problems in annular regions. The annular region $A_{R_{1}, R_{2}}$ in _Figure 18_ is centered at the origin with inner radius $R_{1}$ and outer radius $R_{2}$. Consider the Dirichlet problem in $A_{R_{1}, R_{2}}$ with constant boundary conditions $u\left(R_{1}, \theta\right)= T_{1}$ and $u\left(R_{2}, \theta\right)=T_{2}$ for all $\theta$. Show that the solution of the problem is
 > 
 > 
-> > [!figure] Figure 18
-> > 
-> > ![300](./images/af4f9593-dec7-4bc0-8d78-d25500419ec9-51_461_492_971_97.jpg)
-> > Figure 18 Dirichlet problem in problem 30.
+> ```scientific-figure
+> id: 2b8ea57d-a3cb-40d2-97f8-519b4607195c
+> numbered: false
+> title: ""
+> caption: "**Figure 18.** Dirichlet problem in problem 30."
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 02 Analytic Functions/images/af4f9593-dec7-4bc0-8d78-d25500419ec9-51_461_492_971_97.jpg
+>     caption: ""
+> ```
 > 
 > 
 > $$
@@ -8389,7 +8555,7 @@
 
 
 
-> [!exercise] Exercise 22
+> [!exercise|1351845b-db5a-50f4-91ff-3f4e803bdb1e.local at=285ee181-a510-5095-9af0-3f29d9a4e460] Exercise 22
 > 
 > 
 > Problems 31-32 are Dirichlet problems described by the corresponding figures. In each case, (a) solve the Dirichlet problem.
@@ -8397,20 +8563,34 @@
 > (c) Determine the curves of heat flow. (d) Plot the isotherms and curves of heat flow.
 > 
 > 
-> > [!figure] Figure 19
-> > 
-> > ![300](./images/af4f9593-dec7-4bc0-8d78-d25500419ec9-51_457_500_979_802.jpg)
-> > 
-> > Dirichlet problem in problem 31.
-> 
-> 
-> 
-> 
-> > [!figure] Figure 20
-> > 
-> > ![300](./images/af4f9593-dec7-4bc0-8d78-d25500419ec9-51_461_508_981_1511.jpg)
-> > 
-> > Dirichlet problem in problem 32.
+> ```scientific-figure
+> id: a7aa3c34-db72-4955-8dbe-e8cddd805132
+> numbered: false
+> title: ""
+> caption: "**Figure 19.** Dirichlet problem in problem 31."
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 02 Analytic Functions/images/af4f9593-dec7-4bc0-8d78-d25500419ec9-51_457_500_979_802.jpg
+>     caption: ""
+> ```
+> 
+> 
+> 
+> 
+> ```scientific-figure
+> id: 7da06801-ba2b-4f97-a71b-7fc01b11e281
+> numbered: false
+> title: ""
+> caption: "**Figure 20.** Dirichlet problem in problem 32."
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 02 Analytic Functions/images/af4f9593-dec7-4bc0-8d78-d25500419ec9-51_461_508_981_1511.jpg
+>     caption: ""
+> ```
 > 
 > 
 > 
@@ -8642,7 +8822,7 @@
 
 
 
-![|center|500](Pasted%20image%2020260425030210.png)
+![|center|500](Books/Asmar%20Applied%20Complex%20Analysis%20with%20Applications%20to%20Differential%20Equations/Chapter%2002%20Analytic%20Functions/images/Pasted%20image%2020260425030210.png)
 
 
 
@@ -8908,7 +9088,7 @@
 
 
 
-![|center|500](Pasted%20image%2020260425030256.png)
+![|center|500](Books/Asmar%20Applied%20Complex%20Analysis%20with%20Applications%20to%20Differential%20Equations/Chapter%2002%20Analytic%20Functions/images/Pasted%20image%2020260425030256.png)
 
 
 
@@ -8952,7 +9132,7 @@
 
 
 
-> [!exercise] Exercise 23
+> [!exercise|a91ab7b2-1c03-5fbe-a357-f44d2005127f.local at=2dd297b4-b6e0-5e49-aa4c-c11021ea246c] Exercise 23
 > 33. Nonexistence of a harmonic conjugate. In Example 1(d), we showed that $\ln |z|$ is harmonic in $\mathbb{C} \backslash\{0\}$. We also know that $\ln |z|$ has a harmonic conjugate in $\mathbb{C} \backslash(-\infty, 0]$. In fact, since $\ln |z|$ is the real part of the analytic function $\log _{\alpha} z$, it has a harmonic conjugate in the complex plane minus the ray emanating from the origin at angle $\alpha$. In this exercise, we will show that $\ln |z|$ does not have a harmonic conjugate in $\mathbb{C} \backslash\{0\}$.
 > (a) Suppose that $\phi(z)$ is a harmonic conjugate of $\ln |z|$ in $\mathbb{C} \backslash\{0\}$. Show that $\phi(z)=\operatorname{Arg}(z)+c$ for all $z$ in $\mathbb{C} \backslash(-\infty, 0]$. **(Hint: The functions $\ln |z|+i \phi(z)$ and $\log z$ are analytic in the region $\mathbb{C} \backslash(-\infty, 0]$ and have the same real parts. Use Corollary 1, Section 2.4.])**
 > (b) Argue that, since $\phi(z)$ is harmonic in $\mathbb{C} \backslash\{0\}, \phi(z)$ is continuous on $(-\infty, 0)$. Obtain a contradiction using (a) and the fact that the discontinuities of $\operatorname{Arg} z$ are not removable on the negative $x$-axis (Example 7, Section 2.2).
@@ -9153,7 +9333,7 @@
 
 ++++
 
-> [!exercise] Exercise 24
+> [!exercise|530ca380-09e6-50b3-b09c-efc92d67486c.local at=75f10aef-af06-5593-b19c-63f5596e7bac] Exercise 24
 > 34. (a) Suppose that $f$ is analytic on $\Omega, U$ is harmonic on $f[\Omega]$, and $u=U \circ f$. Then $u$ is harmonic in $\Omega$ by Theorem 3. Suppose that $V$ is a harmonic conjugate of $U$. Show that $V \circ f$ is a harmonic conjugate of $u$.
 > (b) Derive the isotherms and curves of heat flow in Exercise 7.
 
@@ -9500,7 +9680,7 @@
 
 
 
-> [!exercise] Exercise 25
+> [!exercise|ce10a4b1-06de-5af3-9ae5-d0005642ec71.local at=7663e7b5-20bf-5792-bad4-8077288eda89] Exercise 25
 > 
 > 35. Harmonic measure of an interval. A very important Dirichlet problem is described in the upper half-plane with boundary data on the $x$-axis given by
 > 
@@ -9511,18 +9691,25 @@
 > where $a<b$ are fixed real numbers (see Figure 21). We will outline a solution of this problem using basic geometry and properties of harmonic functions.
 > (a) For $z$ in the upper half-plane, let $\alpha(z)$ denote the angle at $z$ subtended by the interval $[a, b]$ (_Figure 22_). Show that $\alpha(z)=\operatorname{Arg}(z-b)-\operatorname{Arg}(z-a)$. The function $\alpha(z)$ is called the harmonic measure of the interval $(a, b)$. **(Hint: We have $\alpha_{1}=\operatorname{Arg}(z-b), \alpha_{2}=\operatorname{Arg}(z-a)$, and $\alpha(z)=\alpha_{1}-\alpha_{2}$ _(Figure 22)_.)**
 > 
-> > [!figure] Figure 22
-> > 
-> > ![300](./images/af4f9593-dec7-4bc0-8d78-d25500419ec9-52_489_547_289_83.jpg)
-> > 
-> > Figure 22 The harmonic measure of an interval is the difference of two translated arguments:
-> > 
-> > $$
-> > \begin{aligned}
-> > \alpha(z)=\operatorname{Arg} & (z-b) -\operatorname{Arg}(z-a)
-> > \end{aligned}
-> > $$
-> > 
+> ```scientific-figure
+> id: 300c9a52-49e0-4ab8-be4e-2862ceef6955
+> numbered: false
+> title: ""
+> caption: |-
+>   **Figure 22.** The harmonic measure of an interval is the difference of two translated arguments:
+> 
+>   $$
+>   \begin{aligned}
+>   \alpha(z)=\operatorname{Arg} & (z-b) -\operatorname{Arg}(z-a)
+>   \end{aligned}
+>   $$
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 02 Analytic Functions/images/af4f9593-dec7-4bc0-8d78-d25500419ec9-52_489_547_289_83.jpg
+>     caption: ""
+> ```
 > 
 > 
 > (b) Show that $\alpha(z)$ is harmonic. **(Hint: problem 23(a).)**
@@ -9835,16 +10022,24 @@
 
 
 
-> [!exercise] Exercise 26
+> [!exercise|0f6a8f98-dc99-58df-9a1a-09516d076f36.local at=80bd7020-34b9-55c4-a1ea-de55f489f810] Exercise 26
 > 
 > 
 > 36. (a) Solve the Dirichlet problem in _Figure 23_.
 > 
 > 
-> > [!figure] Figure 23
-> > 
-> > ![300](./images/af4f9593-dec7-4bc0-8d78-d25500419ec9-52_497_553_1152_91.jpg)
-> > Figure 23 Dirichlet problem for problem 36.
+> ```scientific-figure
+> id: 493c0feb-3a66-4439-b44a-4956e74409c7
+> numbered: false
+> title: ""
+> caption: "**Figure 23.** Dirichlet problem for problem 36."
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 02 Analytic Functions/images/af4f9593-dec7-4bc0-8d78-d25500419ec9-52_497_553_1152_91.jpg
+>     caption: ""
+> ```
 > 
 > 
 > 
@@ -10355,7 +10550,7 @@
 ##### problem 36(d)
 
 
-![|center](Pasted%20image%2020260425030800.png)
+![|center](Books/Asmar%20Applied%20Complex%20Analysis%20with%20Applications%20to%20Differential%20Equations/Chapter%2002%20Analytic%20Functions/images/Pasted%20image%2020260425030800.png)
 
 
 
@@ -10447,7 +10642,7 @@
 
 
 
-> [!exercise] Exercise 27
+> [!exercise|799b5a09-b6f2-5944-a1cc-11c951a7f852.local at=b5041888-bad6-56cc-9082-dc134f949c6d] Exercise 27
 > 37. Solve the Dirichlet problem in the upper half-plane with boundary data on the $x$-axis given by
 > 
 > $$
@@ -10626,7 +10821,7 @@
 
 
 
-> [!exercise] Exercise 28
+> [!exercise|9f7adfef-c779-5774-bef4-30fcc3a7b35a.local at=6bb6045d-4c9b-51af-8854-7d649582ac6f] Exercise 28
 > 
 > 
 > 38. **Project Problem:** Harmonic measures of two disjoint intervals. In this exercise, we generalize the result of Exercise 35 by solving the Dirichlet problem in the upper half-plane with boundary data
@@ -10638,10 +10833,18 @@
 > where $a<b \leq c<d$ (_Figure 24_).
 > 
 > 
-> > [!figure] Figure 24
-> > 
-> > ![300](./images/af4f9593-dec7-4bc0-8d78-d25500419ec9-52_514_544_1860_102.jpg)
-> > Figure 24 Dirichlet problem for problem 38.
+> ```scientific-figure
+> id: da747857-95f1-4e06-bcb1-9533cebcbe7b
+> numbered: false
+> title: ""
+> caption: "**Figure 24.** Dirichlet problem for problem 38."
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 02 Analytic Functions/images/af4f9593-dec7-4bc0-8d78-d25500419ec9-52_514_544_1860_102.jpg
+>     caption: ""
+> ```
 > 
 > 
 > 
@@ -10860,16 +11063,24 @@
 
 
 
-> [!exercise] Exercise 29
+> [!exercise|f7771213-8419-5232-bd4b-7e32249be332.local at=fd063790-0c2a-5392-ad19-19b97f7b4942] Exercise 29
 > 
 > 
 > 39. (a) Solve the Dirichlet problem in _Figure 25_.
 > 
 > 
-> > [!figure] Figure 25
-> > 
-> > ![300](./images/af4f9593-dec7-4bc0-8d78-d25500419ec9-53_474_503_734_104.jpg)
-> > Figure 25 Dirichlet problem for problem 39.
+> ```scientific-figure
+> id: a39b5f44-a22f-4f5e-9117-50d4e282a3a3
+> numbered: false
+> title: ""
+> caption: "**Figure 25.** Dirichlet problem for problem 39."
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 02 Analytic Functions/images/af4f9593-dec7-4bc0-8d78-d25500419ec9-53_474_503_734_104.jpg
+>     caption: ""
+> ```
 > 
 > 
 > (b) Plot the isotherms.
@@ -11152,7 +11363,7 @@
 
 
 
-> [!exercise] Exercise 30
+> [!exercise|34a567cf-147f-5bd5-a718-99efc42688c2.local at=56acb5b7-15e8-5965-98d8-07a1688b7703] Exercise 30
 > 
 > 40. **Project Problem:** Harmonic measures of several disjoint intervals. Generalize the result of Exercise 38 as follows. Suppose that $I_{1}, I_{2}, \ldots, I_{n}$ are disjoint open intervals on the $x$-axis, and $T_{1}, T_{2}, \ldots, T_{n}$ are real numbers. Consider the Dirichlet problem in the upper half-plane with boundary condition
 > 
@@ -11405,7 +11616,7 @@
 
 
 
-> [!exercise] Exercise 31
+> [!exercise|3c495c69-ca91-5a53-83bb-89fcfba239c2.local at=18c605c6-ba02-5d76-a749-dffe5959f90e] Exercise 31
 > 
 > 41. **Project Problem:** Approximation of steady-state solutions. Consider the Dirichlet problem in the upper half-plane with boundary values $u(x, 0)= f(x)(-\infty<x<\infty)$, where $f(x)$ is an arbitrary function that represents the temperature of the points on the $x$-axis. Such a temperature distribution will be bounded and piecewise continuous. There is an analytical solution of the Dirichlet problem, given by an integral involving $f(x)$, known as the Poisson integral of $f$ (see Exercise 42). In this exercise, we will show how we can use the result of Exercise 40 to approximate the solution for a given $f(x)$. The approach that we take has some merit, since it can be used to obtain approximate numerical values for the steady-state temperature. Moreover, we will use it in Exercise 42 to justify the Poisson integral formula. The rigorous derivation of this formula will be given in a later chapter.
 > 
@@ -12200,7 +12411,7 @@
 
 
 
-> [!exercise] Exercise 32
+> [!exercise|595bb8a5-267a-5167-915c-83a41bb30078.local at=e7097ffe-2a4b-50b4-9231-6936738b5079] Exercise 32
 > 
 > 
 > 42. **Project Problem:** Justifying the Poisson integral formula. Consider the Dirichlet problem in the upper half-plane with boundary values $u(x, 0)=f(x)$, $-\infty<x<\infty$. One of the major results that we will derive in this book gives the solution as
@@ -12242,7 +12453,7 @@
 > Let $\Delta x \rightarrow 0$ and explain why $u_{\mathrm{app}}(s, y)$ should approach the Poisson integral (11). **(Hint: Interpret $u_{\mathrm{app}}(s, y)$ as a Riemann sum that approximates the Poisson integral (11).)**
 > 
 > 
-> > [!NOTE]
+> > [!note|3a68d960-1368-5771-b84d-63f354923bc6.local at=6eac4e63-2c80-5790-be33-6793b7a7dbd9]
 > > What we have done in problem 42 is not exactly a proof of the Poisson integral formula, since Riemann sums are defined for functions on finite intervals and we have used them on the interval $(-\infty, \infty)$. However, if we know that $f(x)$ is continuous and equal to zero outside an interval $[a, b]$ (no matter how large the interval is), then the preceding proof works, giving you a simple proof of an important result in applied mathematics for the class of continuous functions vanishing outside a bounded interval. Often in analysis, knowing that a result is true for this class of continuous functions is a good indication that the result is also true for a larger class of functions. In particular, to extend the Poisson integral formula to a larger class of functions $f(x)$ satisfying some general integrability conditions, we use standard techniques from analysis to approximate $f(x)$ by continuous functions that vanish outside a bounded interval, and then use this approximation to establish the Poisson integral formula for $f$.
 > 
 > 
@@ -12789,7 +13000,7 @@
 
 
 
-> [!exercise] Exercise 33
+> [!exercise|4ff6e9b3-f699-56a8-8ab5-a239959e05c5.local at=3a47fb5d-0c98-592a-8f81-3394b39ddd7e] Exercise 33
 > 
 > Project Problems: Conformal mapping method. Exercises 43-46 are Dirichlet problems described by the corresponding figures. In each case, 
 > (a) solve the problem by following the four steps, as we did in Exercise 7.
@@ -12797,31 +13008,63 @@
 > 
 > 
 > 
-> > [!figure] Figure 26
-> > 
-> > ![300](./images/af4f9593-dec7-4bc0-8d78-d25500419ec9-55_491_517_1272_690.jpg)
-> > Dirichlet problem in problem 43.
-> 
-> 
-> 
-> > [!figure] Figure 27
-> > 
-> > ![300](./images/af4f9593-dec7-4bc0-8d78-d25500419ec9-55_495_516_1272_1280.jpg)
-> > Dirichlet problem in problem 44.
-> 
-> 
-> 
-> > [!figure] Figure 28
-> > 
-> > ![300](./images/af4f9593-dec7-4bc0-8d78-d25500419ec9-55_508_520_1892_680.jpg)
-> > Dirichlet problem in problem 45.
-> 
-> 
-> 
-> > [!figure] Figure 29
-> > 
-> > ![300](./images/af4f9593-dec7-4bc0-8d78-d25500419ec9-55_508_516_1890_1278.jpg)
-> > Dirichlet problem in problem 46.
+> ```scientific-figure
+> id: 40b8e693-7492-4ac5-ac65-bdb6b05ca6a1
+> numbered: false
+> title: ""
+> caption: "**Figure 26.** Dirichlet problem in problem 43."
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 02 Analytic Functions/images/af4f9593-dec7-4bc0-8d78-d25500419ec9-55_491_517_1272_690.jpg
+>     caption: ""
+> ```
+> 
+> 
+> 
+> ```scientific-figure
+> id: 9b574519-eea7-46b5-964f-ad862a5d3497
+> numbered: false
+> title: ""
+> caption: "**Figure 27.** Dirichlet problem in problem 44."
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 02 Analytic Functions/images/af4f9593-dec7-4bc0-8d78-d25500419ec9-55_495_516_1272_1280.jpg
+>     caption: ""
+> ```
+> 
+> 
+> 
+> ```scientific-figure
+> id: d5d333c3-28b6-432e-9a90-ec3bef04a5b4
+> numbered: false
+> title: ""
+> caption: "**Figure 28.** Dirichlet problem in problem 45."
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 02 Analytic Functions/images/af4f9593-dec7-4bc0-8d78-d25500419ec9-55_508_520_1892_680.jpg
+>     caption: ""
+> ```
+> 
+> 
+> 
+> ```scientific-figure
+> id: 0d64f7ce-d267-4fc7-ba50-c45581cbdf58
+> numbered: false
+> title: ""
+> caption: "**Figure 29.** Dirichlet problem in problem 46."
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 02 Analytic Functions/images/af4f9593-dec7-4bc0-8d78-d25500419ec9-55_508_516_1890_1278.jpg
+>     caption: ""
+> ```
 > 
 > 
 
@@ -14058,7 +14301,7 @@
 
 
 
-![|center|500](Pasted%20image%2020260425041724.png)
+![|center|500](Books/Asmar%20Applied%20Complex%20Analysis%20with%20Applications%20to%20Differential%20Equations/Chapter%2002%20Analytic%20Functions/images/Pasted%20image%2020260425041724.png)
 
 
 
@@ -14477,7 +14720,7 @@
 
 
 
-![|center|500](Pasted%20image%2020260425041832.png)
+![|center|500](Books/Asmar%20Applied%20Complex%20Analysis%20with%20Applications%20to%20Differential%20Equations/Chapter%2002%20Analytic%20Functions/images/Pasted%20image%2020260425041832.png)
 
 
 
@@ -14530,7 +14773,7 @@
 
 
 
-> [!exercise] Exercise 34
+> [!exercise|69c3090d-9b25-5461-964d-e9d47729b838.local at=90d65383-18f9-522e-8d71-ae99afe91f56] Exercise 34
 > 
 > 43. **Project Problem:** Laplacian in polar coordinates. In this exercise, you are asked to derive the polar form of the Laplacian
 > 
@@ -15042,7 +15285,7 @@
 
 
 
-> [!exercise] Exercise 35
+> [!exercise|a8c97e56-995a-55c7-afcc-af76dba39b33.local at=7740974c-9823-5eb5-a5b7-6804c9e7028f] Exercise 35
 > 44. (a) Use (12) to give a direct proof of the result of problem 17(a).
 > (b) Use (12) to give a direct proof that $\log |z|$ is harmonic for all $z \neq 0$.
 
@@ -15548,7 +15791,7 @@
 
 
 
-> [!exercise] Exercise 36
+> [!exercise|c1344b6f-939f-52d8-8369-248775e3b617.local at=4fc500a0-23fd-5352-b187-3d062c205650] Exercise 36
 > 45. Show that if $u$ is harmonic and independent of $r$, then $u_{\theta \theta}=0$. Conclude that $u=a \theta+b$; equivalently, $u=a \arg _{\alpha} z+b$, where $\arg _{\alpha} z$ is a branch of the argument.
 
 

`````
