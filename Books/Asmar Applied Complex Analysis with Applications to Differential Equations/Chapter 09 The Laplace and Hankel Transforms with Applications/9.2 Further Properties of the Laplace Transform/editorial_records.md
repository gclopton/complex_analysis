
# Editorial records

Reading note: 9.2 Further Properties of the Laplace Transform.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|63bfac33-dcc2-5db8-8768-4c1b04c5fcd5.local at=02ea2f7f-2e27-57f8-9be9-30593f719031] Causal Time Delay in the One-Sided Laplace Transform
> Write $\mathcal Lf(s)=\int_0^\infty f(t)e^{-st}\,dt$ for the one-sided Laplace transform.
>
> Let $a>0$, let $\mathcal U_0(t)=0$ for $t<0$ and $1$ for $t\geq0$, and suppose $F(s)=\mathcal Lf(s)$ converges. Define the delayed function to be zero for $t<a$. Then
>
> $$
> \mathcal L\!\left(\mathcal U_0(t-a)f(t-a)\right)(s)=e^{-as}F(s).
> $$
````
### After

````text
> [!theorem|63bfac33-dcc2-5db8-8768-4c1b04c5fcd5.local at=02ea2f7f-2e27-57f8-9be9-30593f719031] Shifting on the $t$-Axis
> Write $\mathcal Lf(s)=\int_0^\infty f(t)e^{-st}\,dt$.
>
> Let $\mathcal U_0(t)$ be zero for $t<0$ and one for $t\geq0$. Suppose $F(s)$ converges; define the delayed function to be zero for $t<a$.
>
> If $a$ is a positive real number, then
>
> $$
> \mathcal{L}\left(\mathcal{U}_{0}(t-a) f(t-a)\right)(s)=e^{-a s} F(s)
> $$
>
> where $F(s)=\mathcal{L}(f(t))(s)$.
````

## 2. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!definition|8f9d61fa-5533-5e73-9f56-a19583ce2300.local at=25d71684-89c7-59ba-a2fb-af40888316c9] Causal Convolution on the Positive Half-Line
> For piecewise continuous functions $f,g:[0,\infty)\to\mathbb C$, their causal convolution is
>
> $$
> (f*g)(t)=\int_0^t f(t-\tau)g(\tau)\,d\tau,\qquad t\geq0.
> $$
````
### After

````text
> [!definition|8f9d61fa-5533-5e73-9f56-a19583ce2300.local at=25d71684-89c7-59ba-a2fb-af40888316c9] Causal Convolution on the Positive Half-Line
> Given two functions $f$ and $g$, piecewise continuous for $t\geq0$, we define their convolution $f * g(t)$ by
>
> $$
> f * g(t)=\int_{0}^{t} f(t-\tau) g(\tau) d \tau \quad \text { for all } t \geq 0
> $$
````

## 3. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|a8a05283-149f-5ec1-b9df-f1a4eb92aee1.local at=616ada6f-378a-5753-8ddf-a2f3fca4f1e6] Laplace Transform of a Causal Convolution
> Write $\mathcal Lf(s)=\int_0^\infty f(t)e^{-st}\,dt$ for the one-sided Laplace transform.
>
> Let $f,g$ be piecewise continuous on bounded intervals, with exponential bounds $|f(t)|\leq M_fe^{at}$ and $|g(t)|\leq M_ge^{bt}$. For $s>\max(a,b)$ and $(f*g)(t)=\int_0^t f(t-\tau)g(\tau)\,d\tau$,
>
> $$
> \mathcal L(f*g)(s)=\mathcal Lf(s)\,\mathcal Lg(s).
> $$
````
### After

````text
> [!theorem|a8a05283-149f-5ec1-b9df-f1a4eb92aee1.local at=616ada6f-378a-5753-8ddf-a2f3fca4f1e6] Transforms of Convolutions
> Write $\mathcal Lf(s)=\int_0^\infty f(t)e^{-st}\,dt$.
>
> Here $(f*g)(t)=\int_0^t f(t-\tau)g(\tau)\,d\tau$; take $s$ greater than the exponential growth rates of both functions.
>
> Suppose that $f$ and $g$ are piecewise continuous and of exponential order; then
>
> $$
> \mathcal{L}(f * g)=\mathcal{L}(f) \mathcal{L}(g)
> $$
````

## Source-to-current comparison

Source: /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 09 The Laplace and Hankel Transforms with Applications/9.2 Further Properties of the Laplace Transform.md

This exact comparison preserves the full change evidence, including formatting, OCR corrections, restored source wording, and required standalone context. The entries above explain the recovery edits. The comparison is not a claim that every difference is a correction; component serialization, callout wrapping, and printed labels outside callouts are formatting.

`````diff
--- /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 09 The Laplace and Hankel Transforms with Applications/9.2 Further Properties of the Laplace Transform.md
+++ /Users/gradyclopton/ObsidianVaults/complex_analysis/Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 09 The Laplace and Hankel Transforms with Applications/9.2 Further Properties of the Laplace Transform.md
@@ -1,12 +1,28 @@
-### 9.2 Further Properties of the Laplace Transform
+
+# 9.2 Further Properties of the Laplace Transform
 
 We continue our study of the Laplace transform and start by computing the transform of special functions that arise naturally in studying operational properties of the transform. Recall the Heaviside unit step function
 
 $$
 \mathcal{U}_{a}(t)=\mathcal{U}_{0}(t-a)= \begin{cases}0 & \text { if } t<a \\ 1 & \text { if } t \geq a\end{cases}
-$$
-
-(Figure 1). Given a function $f(t)$, consider the product $\mathcal{U}_{0}(t-a) f(t-a)$. Written explicitly, we have
+\tag{1}
+$$
+
+```scientific-figure
+id: a177756c-e3cb-4999-b712-63fd4a044bc8
+numbered: false
+title: ""
+caption: Figure 1 The Heaviside unit step delayed by $a$.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 09 The Laplace and Hankel Transforms with Applications/images/asmar-9-2-figure-1-restored.png
+    caption: ""
+```
+
+
+Given a function $f(t)$, consider the product $\mathcal{U}_{0}(t-a) f(t-a)$. Written explicitly, we have
 
 $$
 \mathcal{U}_{0}(t-a) f(t-a)= \begin{cases}0 & \text { if } t<a \\ f(t-a) & \text { if } t \geq a\end{cases}
@@ -14,20 +30,19 @@
 
 Thus, if $f(t)$ represents, say a message, then $\mathcal{U}_{0}(t-a) f(t-a)$ represents the same message, but delayed by $a$ units of time.
 
-THEOREM 1 SHIFTING ON THE $\boldsymbol{t}$-AXIS
-
-![](./images/68332ba3-9551-434a-a491-ce53af60160e-13_327_441_1665_24.jpg)
-gure 2 The function in Ex-
-
-ample 1.
-
-If $a$ is a positive real number, then
-
-$$
-\mathcal{L}\left(\mathcal{U}_{0}(t-a) f(t-a)\right)(s)=e^{-a s} F(s)
-$$
-
-where $F(s)=\mathcal{L}(f(t))(s)$.
+> [!theorem|63bfac33-dcc2-5db8-8768-4c1b04c5fcd5.local at=02ea2f7f-2e27-57f8-9be9-30593f719031] Shifting on the $t$-Axis
+> Write $\mathcal Lf(s)=\int_0^\infty f(t)e^{-st}\,dt$.
+>
+> Let $\mathcal U_0(t)$ be zero for $t<0$ and one for $t\geq0$. Suppose $F(s)$ converges; define the delayed function to be zero for $t<a$.
+>
+> If $a$ is a positive real number, then
+>
+> $$
+> \mathcal{L}\left(\mathcal{U}_{0}(t-a) f(t-a)\right)(s)=e^{-a s} F(s)
+> $$
+>
+> where $F(s)=\mathcal{L}(f(t))(s)$.
+
 Proof We have
 
 $$
@@ -38,17 +53,36 @@
 \end{aligned}
 $$
 
-## EXAMPLE 1 Transforms involving unit step functions
-
-(a) Evaluate $\mathcal{L}\left(\mathcal{U}_{0}(t-a)\right)$.
-(b) Evaluate $\mathcal{L}(f(t))$, where
-
-$$
-f(t)= \begin{cases}2 & \text { if } 1 \leq t<4 \\ 0 & \text { otherwise }\end{cases}
-$$
-
-(see Figure 2).
-Solution (a) Using Theorem 1 with $f(t)=1$, and Example 1 of the previous section, we find
+> [!exercise|b6935a08-7860-51ce-9572-112a761f49c1.local at=24fdd5fe-32cc-5563-a014-7ba9fbac4984] EXAMPLE 1 Transforms involving unit step functions
+> (a) Evaluate $\mathcal{L}\left(\mathcal{U}_{0}(t-a)\right)$.
+> (b) Evaluate $\mathcal{L}(f(t))$, where
+>
+> $$
+> f(t)= \begin{cases}2 & \text { if } 1 \leq t<4 \\ 0 & \text { otherwise }\end{cases}
+> $$
+>
+> (see Figure 2).
+
+
+
+
+
+```scientific-figure
+id: 1b0330f4-4454-4a84-ace2-da8b9448234f
+numbered: false
+title: ""
+caption: Figure 2 The function in Example 1.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 09 The Laplace and Hankel Transforms with Applications/images/68332ba3-9551-434a-a491-ce53af60160e-13_327_441_1665_24.jpg
+    caption: ""
+```
+
+##### solution
+
+(a) Using Theorem 1 with $f(t)=1$, and Example 1 of the previous section, we find
 
 $$
 \mathcal{L}\left(\mathcal{U}_{0}(t-a)\right)=\frac{e^{-a s}}{s}, \quad s>0
@@ -60,16 +94,40 @@
 \mathcal{L}(f(t))=2\left(\mathcal{L}\left(\mathcal{U}_{0}(t-1)\right)-\mathcal{L}\left(\mathcal{U}_{0}(t-4)\right)\right)=\frac{2}{s}\left(e^{-s}-e^{-4 s}\right), \quad s>0
 $$
 
-![](./images/68332ba3-9551-434a-a491-ce53af60160e-14_366_473_243_87.jpg)
-Figure 3 A ramp function.
-
-![](./images/68332ba3-9551-434a-a491-ce53af60160e-14_339_514_1363_91.jpg)
-Figure 4 Solution in Example 3.
-
-## EXAMPLE 2 A ramp function
-
-Evaluate the Laplace transform of the ramp function shown in Figure 3.
-Solution For $t>1$, we have $f(t)=\mathcal{U}_{0}(t-1)$, and for $0 \leq t \leq 1$, we have $f(t)=t\left(\mathcal{U}_{0}(t)-\mathcal{U}_{0}(t-1)\right)$. We can combine these two formulas and simply write
+```scientific-figure
+id: 8f1b422a-c9cd-4e6b-97f0-47686adc2bb5
+numbered: false
+title: ""
+caption: Figure 3 A ramp function.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 09 The Laplace and Hankel Transforms with Applications/images/68332ba3-9551-434a-a491-ce53af60160e-14_366_473_243_87.jpg
+    caption: ""
+```
+
+
+```scientific-figure
+id: f5083f29-e7a3-4b6e-aca7-6bafdfa31baf
+numbered: false
+title: ""
+caption: Figure 4 Solution in Example 3.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 09 The Laplace and Hankel Transforms with Applications/images/68332ba3-9551-434a-a491-ce53af60160e-14_339_514_1363_91.jpg
+    caption: ""
+```
+
+
+> [!exercise|2ce2aed5-1bef-56a2-967d-bdffb28db459.local at=4b1cbf23-7ef7-5617-bb4e-8fa460b621bc] EXAMPLE 2 A ramp function
+> Evaluate the Laplace transform of the ramp function shown in Figure 3.
+
+##### solution
+
+For $t>1$, we have $f(t)=\mathcal{U}_{0}(t-1)$, and for $0 \leq t \leq 1$, we have $f(t)=t\left(\mathcal{U}_{0}(t)-\mathcal{U}_{0}(t-1)\right)$. We can combine these two formulas and simply write
 
 $$
 f(t)=t\left(\mathcal{U}_{0}(t)-\mathcal{U}_{0}(t-1)\right)+\mathcal{U}_{0}(t-1) .
@@ -85,14 +143,17 @@
 
 $$
 \mathcal{L}(f(t))=-\frac{e^{-s}}{s^{2}}+\frac{1}{s^{2}}
-$$ $\square$
-
+$$
+
+$\square$
 In the next example we solve a nonhomogeneous differential equation involving a ramp function.
 
-## EXAMPLE 3 A nonhomogeneous differential equation
-
-Solve $y^{\prime \prime}+y=f(t), y(0)=0, y^{\prime}(0)=0$, where $f(t)$ is as in Example 2.
-Solution Taking the Laplace transform of both sides of the equation and using the result of Example 2, we find
+> [!exercise|89c57ea1-2ea3-57df-a9be-5cac702e1a0a.local at=27397207-5159-586d-b4a5-4debf62dd8b7] EXAMPLE 3 A nonhomogeneous differential equation
+> Solve $y^{\prime \prime}+y=f(t), y(0)=0, y^{\prime}(0)=0$, where $f(t)$ is as in Example 2.
+
+##### solution
+
+Taking the Laplace transform of both sides of the equation and using the result of Example 2, we find
 
 $$
 \begin{aligned}
@@ -126,22 +187,45 @@
 
 Our next example involves a differential equation with a discontinuous term.
 
-## EXAMPLE 4 Discontinuous forcing term
-
-Solve $y^{\prime \prime}+4 y=f(t), y(0)=1, y^{\prime}(0)=0$, where the forcing term $f(t)$ is as in Figure 5.
-Solution The forcing term can be expressed as
+> [!exercise|d28c0485-1de4-5af1-9251-1636903e15f2.local at=4ed8e528-2378-5846-82bd-2457805eaaf7] EXAMPLE 4 Discontinuous forcing term
+> Solve $y^{\prime \prime}+4 y=f(t), y(0)=1, y^{\prime}(0)=0$, where the forcing term $f(t)$ is as in Figure 5.
+
+##### solution
+
+The forcing term can be expressed as
 
 $$
 f(t)=1-\mathcal{U}_{0}(t-1)
 $$
 
 Taking the Laplace transform of both sides of the equation, we get
-![](./images/68332ba3-9551-434a-a491-ce53af60160e-15_307_341_701_17.jpg)
-
-Figure $5 f(t)$ in Example 4.
-
-![](./images/68332ba3-9551-434a-a491-ce53af60160e-15_327_378_1189_18.jpg)
-Figure 6 Solution in Exampie 4.
+```scientific-figure
+id: 409941ce-5575-43d3-90bb-e14cedb5064a
+numbered: false
+title: ""
+caption: Figure 5 $f(t)$ in Example 4.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 09 The Laplace and Hankel Transforms with Applications/images/68332ba3-9551-434a-a491-ce53af60160e-15_307_341_701_17.jpg
+    caption: ""
+```
+
+
+```scientific-figure
+id: 770e4d66-9d35-4fe0-9269-cfda8286ef62
+numbered: false
+title: ""
+caption: Figure 6 Solution in Example 4.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 09 The Laplace and Hankel Transforms with Applications/images/68332ba3-9551-434a-a491-ce53af60160e-15_327_378_1189_18.jpg
+    caption: ""
+```
+
 
 $$
 \begin{aligned}
@@ -165,32 +249,38 @@
 \end{aligned}
 $$
 
-(Figure 6). Note that even though the forcing term is discontinuous at $t=1$, the solution is continuous everywhere. A discontinuity at $t=1$ will appear in the graph of the second derivative of the solution, since $y^{\prime \prime}=f(t)-y$.
+(Figure 6). Note that even though the forcing term is discontinuous at $t=1$, the solution is continuous everywhere. A discontinuity at $t=1$ will appear in the graph of the second derivative of the solution, since $y^{\prime \prime}=f(t)-4y$.
 
 ## Convolutions and Laplace Transforms
 
-Given two functions $f$ and $g$, defined for all $t \geq 0$, we define their convolution $f * g(t)$ by
-
-$$
-f * g(t)=\int_{0}^{t} f(t-\tau) g(\tau) d \tau \quad \text { for all } t \geq 0
-$$
-
-Clearly this definition is related to the definition of convolutions that we presented in Section 11.2. In fact, if we think of $f$ and $g$ as being defined for all $t$ with values 0 for $t<0$, then (2) becomes $\int_{-\infty}^{\infty} f(t-\tau) g(\tau) d \tau$, which differs by a constant multiple from the convolution that we introduced in Section 11.2. It should be clear from the context which convolution we are talking about, and so there is no risk of confusion in using the same
-
-THEOREM 2 TRANSFORMS OF CONVOLUTIONS
-notation for the two different operations. In particular, all our discussion in this section concerns the convolution (2) and not the one in Section 11.2.
+> [!definition|8f9d61fa-5533-5e73-9f56-a19583ce2300.local at=25d71684-89c7-59ba-a2fb-af40888316c9] Causal Convolution on the Positive Half-Line
+> Given two functions $f$ and $g$, piecewise continuous for $t\geq0$, we define their convolution $f * g(t)$ by
+>
+> $$
+> f * g(t)=\int_{0}^{t} f(t-\tau) g(\tau) d \tau \quad \text { for all } t \geq 0
+> $$
+
+*Printed equation label: (2).*
+
+Clearly this definition is related to the definition of convolutions that we presented in Section 8.2. In fact, if we think of $f$ and $g$ as being defined for all $t$ with values 0 for $t<0$, then (2) becomes $\int_{-\infty}^{\infty} f(t-\tau) g(\tau) d \tau$, which differs by a constant multiple from the convolution that we introduced in Section 8.2. It should be clear from the context which convolution we are talking about, and so there is no risk of confusion in using the same notation for the two different operations. In particular, all our discussion in this section concerns the convolution (2) and not the one in Section 8.2.
 
 Note that since the convolution is defined by an integral over a finite interval, there is no problem in computing $f * g(t)$ if, say, $f$ and $g$ are piecewise continuous functions, no matter how fast they grow at infinity.
-Suppose that $f$ and $g$ are piecewise continuous and of exponential order; then
-
-$$
-\mathcal{L}(f * g)=\mathcal{L}(f) \mathcal{L}(g)
-$$
+> [!theorem|a8a05283-149f-5ec1-b9df-f1a4eb92aee1.local at=616ada6f-378a-5753-8ddf-a2f3fca4f1e6] Transforms of Convolutions
+> Write $\mathcal Lf(s)=\int_0^\infty f(t)e^{-st}\,dt$.
+>
+> Here $(f*g)(t)=\int_0^t f(t-\tau)g(\tau)\,d\tau$; take $s$ greater than the exponential growth rates of both functions.
+>
+> Suppose that $f$ and $g$ are piecewise continuous and of exponential order; then
+>
+> $$
+> \mathcal{L}(f * g)=\mathcal{L}(f) \mathcal{L}(g)
+> $$
 
 Proof If we extend the functions $f$ and $g$ to be zero for $t<0$, then the integral in (2) is the same as
 
 $$
 \int_{0}^{\infty} f(t-\tau) g(\tau) d \tau
+\tag{3}
 $$
 
 Thus, throughout this proof, we assume that $f$ and $g$ are extended to the whole line with $f(t)=0$ and $g(t)=0$, for all $t<0$. We have
@@ -204,12 +294,13 @@
 \end{aligned}
 $$
 
-## EXAMPLE 5 Transforms involving convolutions
-
-(a) Evaluate $\mathcal{L}\left(\int_{0}^{t}(t-\tau) \sin (\tau) d \tau\right)$.
-(b) Evaluate $\mathcal{L}^{-1}\left(\frac{1}{s^{2}\left(s^{2}+4 s+5\right)}\right)$ using convolutions.
-
-Solution (a) From Theorem 2, we have
+> [!exercise|d0cacade-1800-5d0c-84d0-0fd09f655155.local at=27de366c-f5ce-59ef-840e-a0c447b6ed0d] EXAMPLE 5 Transforms involving convolutions
+> (a) Evaluate $\mathcal{L}\left(\int_{0}^{t}(t-\tau) \sin (\tau) d \tau\right)$.
+> (b) Evaluate $\mathcal{L}^{-1}\left(\frac{1}{s^{2}\left(s^{2}+4 s+5\right)}\right)$ using convolutions.
+
+##### solution
+
+(a) From Theorem 2, we have
 
 $$
 \mathcal{L}\left(\int_{0}^{t}(t-\tau) \sin \tau d \tau\right)=\mathcal{L}(t) \mathcal{L}(\sin t)=\frac{1}{s^{2}} \frac{1}{s^{2}+1}
@@ -224,7 +315,7 @@
 and
 
 $$
-\mathcal{L}^{-1}\left(\frac{1}{s^{2}+4 s+5}\right)=\mathcal{L}^{-1}\left(\frac{1}{\left.(s+2)^{2}+1\right)}\right)=e^{-2 t} \sin t
+\mathcal{L}^{-1}\left(\frac{1}{s^{2}+4 s+5}\right)=\mathcal{L}^{-1}\left(\frac{1}{(s+2)^{2}+1}\right)=e^{-2 t} \sin t
 $$
 
 it follows that
@@ -239,16 +330,18 @@
 \mathcal{L}^{-1}\left(\frac{1}{s^{2}\left(s^{2}+4 s+5\right)}\right)=\frac{1}{25}(5 t-4)+\frac{4}{25} e^{-2 t} \cos t+\frac{3}{25} e^{-2 t} \sin t
 $$
 
-## EXAMPLE 6 Solving differential equations with convolutions
-
-Express the solution of the initial value problem
-
-$$
-y^{\prime \prime}-2 y^{\prime}+5 y=f(t), \quad y(0)=0, y^{\prime}(0)=0
-$$
-
-as a convolution.
-Solution Transforming the equation and then solving for $Y$, we find
+> [!exercise|d5861255-54eb-5f96-aaa7-d1965f8e9da2.local at=e8c74b2e-18c6-5363-b80d-5ada6484cc71] EXAMPLE 6 Solving differential equations with convolutions
+> Express the solution of the initial value problem
+>
+> $$
+> y^{\prime \prime}-2 y^{\prime}+5 y=f(t), \quad y(0)=0, y^{\prime}(0)=0
+> $$
+>
+> as a convolution.
+
+##### solution
+
+Transforming the equation and then solving for $Y$, we find
 
 $$
 Y=\frac{F(s)}{s^{2}-2 s+5}
@@ -272,18 +365,24 @@
 y=\frac{1}{2} e^{t} \sin 2 t * f(t)=\frac{1}{2} \int_{0}^{t} e^{t-\tau} \sin 2(t-\tau) f(\tau) d \tau
 $$
 
-Example 6 shows that in solving the differential equation with zero initial data all nonhomogeneous terms are treated equally: we simply integrate $f(t)$ against $\frac{1}{2} e^{t-\tau} \sin 2(t-\tau)$ on the interval 0 to $t$. Note that the latter function is a translate of the inverse Laplace transform of $1 /\left(s^{2}-2 s+5\right)$, where the differential equation determines the denominator as follows: $y^{\prime \prime}$ corresponds to $s^{2},-2 y^{\prime}$ corresponds to $-2 s$, and $5 y$ corresponds to 5 . In other words, the response of the system to the input function (nonhomogeneous term) $f(t)$ is always related to that function via convolution with a "response function" that is determined solely by the associated homogeneous differential equation. It is clear that this remark applies for any linear nonhomogeneous differential equation, and it is therefore a general principle governing all such equations.
-
-We close the section with examples that involve the Dirac delta function and its translates. Recall from Section 11.2 the effect of integrating against
+Example 6 shows that in solving the differential equation with zero initial data all nonhomogeneous terms are treated equally: we simply integrate $f(t)$ against $\frac{1}{2} e^{t-\tau} \sin 2(t-\tau)$ on the interval 0 to $t$. Note that the latter function is a translate of the inverse Laplace transform of $1 /\left(s^{2}-2 s+5\right)$, where the differential equation determines the denominator as follows: $y^{\prime \prime}$ corresponds to $s^{2},-2 y^{\prime}$ corresponds to $-2 s$, and $5 y$ corresponds to 5 . In other words, the response of the system to the input function (nonhomogeneous term) $f(t)$ is always related to that function via convolution with a "response function" that is determined solely by the associated homogeneous differential equation. It is clear that this remark applies for any constant-coefficient linear ordinary differential equation with zero initial data, and it is therefore a general principle governing all such equations.
+
+We close the section with examples that involve the Dirac delta function and its translates. Recall from Section 8.2 the effect of integrating against
 a Dirac delta is given by
 
 $$
 \int_{a}^{b} f(t) \delta_{0}\left(t-t_{0}\right) d t= \begin{cases}f\left(t_{0}\right) & \text { if } t_{0} \text { is in }[a, b] \\ 0 & \text { if } t_{0} \text { is not in }[a, b]\end{cases}
-$$
+\tag{4}
+$$
+
+Here integration over a closed interval includes an endpoint Dirac mass with full weight. This convention also gives $\mathcal L\delta_0=1$ in the causal transform.
 
 With this formula in hand, we can compute Laplace transforms involving the Dirac delta function. We illustrate with a basic example.
 
-## EXAMPLE 7 Laplace transform of the Dirac delta function
+> [!exercise|db8f5b47-0926-51d4-8b40-35b238bfd56c.local at=2e4f2646-63fc-5018-b3de-975f8d0ecb17] EXAMPLE 7 Laplace transform of the Dirac delta function
+> For $a\geq0$, compute the one-sided Laplace transform of the Dirac mass at $t=a$, using the convention that an endpoint mass has full weight.
+
+##### solution
 
 Let $a \geq 0$. From the definition of the Laplace transform, we have
 
@@ -307,15 +406,26 @@
 
 Our final example is a differential equation involving the delta function.
 
-## EXAMPLE 8 Effect of impulse functions
-
-Solve $y^{\prime \prime}+4 y=\delta_{0}(t-2), y(0)=0, y^{\prime}(0)=0$. (This represents an oscillator, initially at rest, which receives a unit impulse at time $t=2$.)
-Solution Taking the Laplace transform of both sides of the equation, we get
-
-![](./images/68332ba3-9551-434a-a491-ce53af60160e-18_311_467_1982_78.jpg)
-Figure 7 Solution in Exam-
-
-ple 8.
+> [!exercise|75c6fe63-3181-5bff-9ff4-3420db2e15a7.local at=a2ffdcd1-dcf9-5982-8c50-597478c1f1f2] EXAMPLE 8 Effect of impulse functions
+> Solve $y^{\prime \prime}+4 y=\delta_{0}(t-2), y(0)=0, y^{\prime}(0)=0$. (This represents an oscillator, initially at rest, which receives a unit impulse at time $t=2$.)
+
+##### solution
+
+Taking the Laplace transform of both sides of the equation, we get
+
+```scientific-figure
+id: 1a393712-fa76-4ba9-b47f-91701f030e68
+numbered: false
+title: ""
+caption: Figure 7 Solution in Example 8.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 09 The Laplace and Hankel Transforms with Applications/images/68332ba3-9551-434a-a491-ce53af60160e-18_311_467_1982_78.jpg
+    caption: ""
+```
+
 
 $$
 \begin{aligned}
@@ -332,142 +442,379 @@
 
 The graph in Figure 7 shows that the solution is identically 0 up to time $t=2$, which corresponds to the fact that the oscillator started at rest and no forces acted upon it until that time. For $t>2$, the solution oscillates periodically.
 
-## Section 9.2 Further Properties of the Laplace Transform 777
-
-## Exercises 12.2
-
-In Exercises 1-6, evaluate the Laplace transform of the given function.
-
-1. $f(t)=\mathcal{U}_{0}(t-1)-t+1$.
-2. $f(t)=(t-1) \mathcal{U}_{0}(t-1)$.
-3. $f(t)=e^{2 t} \mathcal{U}_{0}(t-2)$.
-4. $f(t)=t \mathcal{U}_{0}(t-\pi)$.
-5. $f(t)=\mathcal{U}_{0}(t-\pi) \sin t$.
-6. $f(t)=\mathcal{U}_{0}(t-\pi) \cos t \sin t$.
-
-In Exercises 7-14, (a) plot the given function. (b) Express it using unit step functions. (c) Evaluate its Laplace transform.
-7. $f(x)= \begin{cases}1 & \text { if } 0<t<2, \\ 0 & \text { if } t>2 .\end{cases}$
-8. $f(x)= \begin{cases}t & \text { if } 0 \leq t \leq 1, \\ 2-t & \text { if } 1 \leq t \leq 2, \\ 0 & \text { if } t>2 .\end{cases}$
-9. $f(x)= \begin{cases}2 & \text { if } 2 \leq t \leq 3, \\ 0 & \text { otherwise. }\end{cases}$
-10. $f(x)= \begin{cases}t & \text { if } 0 \leq t \leq 1, \\ 0 & \text { otherwise. }\end{cases}$
-11. $f(x)= \begin{cases}t-1 & \text { if } 1 \leq t \leq 2, \\ 0 & \text { otherwise. }\end{cases}$
-12. $f(x)= \begin{cases}-\sin t & \text { if } \pi \leq t \leq 2 \pi, \\ 0 & \text { otherwise. }\end{cases}$
-13. $f(x)= \begin{cases}1 & \text { if } 1 \leq t \leq 4, \\ t-5 & \text { if } 4 \leq t \leq 5, \\ 0 & \text { otherwise. }\end{cases}$
-14. $f(x)= \begin{cases}t & \text { if } 0 \leq t \leq 1, \\ 1 & \text { if } 1 \leq t \leq 3, \\ 4-t & \text { if } 3<t \leq 4, \\ 0 & \text { otherwise. }\end{cases}$
-
-In Exercises 15-22, evaluate the inverse Laplace transform of the given function.
-15. $F(s)=\frac{e^{-s}}{s^{2}}$.
-16. $F(s)=\frac{e^{-\pi s}}{s^{2}-2}$.
-17. $F(s)=\frac{e^{-s}}{s^{2}+1}$.
-18. $F(s)=\frac{e^{-s}}{(s-1)^{2}-1}$.
-19. $F(s)=\frac{s-3}{1+(s-3)^{2}}$.
-20. $F(s)=\frac{e^{-3 s}}{(s-1)(s+1)}$.
-21. $F(s)=\frac{e^{-s}}{s^{3 / 2}}$.
-22. $F(s)=\frac{e^{-s}}{(s-2)^{3 / 2}}$.
-
-In Exercises 23-28, evaluate the given convolution.
-23. $1 * t$.
-24. $e^{t} * e^{-t}$.
-25. $t * t$.
-26. $t * \sin t$.
-27. $\sin t * \sin t$.
-28. $e^{t} * \delta_{0}(t)$.
-
-In Exercises 29-32, express the inverse Laplace transform of the given function as a convolution. Evaluate the integral in your answer.
-29. $F(s)=\frac{1}{s\left(s^{2}+1\right)}$.
-30. $F(s)=\frac{1}{s^{2}\left(s^{2}+1\right)}$.
-31. $F(s)=\frac{1}{\left(s^{2}+1\right)\left(s^{2}+1\right)}$.
-32. $F(s)=\frac{s}{\left(s^{2}-1\right)\left(s^{2}-1\right)}$.
-
-In Exercises 33-38, solve the given initial value problem.
-33. $y^{\prime \prime}+y=\delta_{0}(t-1), \quad y(0)=0, \quad y^{\prime}(0)=0$.
-34. $y^{\prime \prime}-y=(t-2) \mathcal{U}_{0}(t-2), \quad y(0)=0, y^{\prime}(0)=0$.
-35. $y^{\prime \prime}+2 y^{\prime}+y=3 \delta_{0}(t-2), \quad y(0)=1, y^{\prime}(0)=0$.
-36. $y^{\prime \prime}-y=t * \cos t, \quad y(0)=-1, y^{\prime}(0)=0$.
-37. $y^{\prime \prime}+4 y=\mathcal{U}_{0}(t-1) e^{t-1}, \quad y(0)=0, y^{\prime}(0)=0$.
-38. $y^{\prime \prime}+y^{\prime}+y=\delta_{0}(t-\pi), \quad y(0)=0, y^{\prime}(0)=0$.
-
-In Exercises 39-42, express the solution of the given initial value problem as a convolution.
-39. $y^{\prime \prime}+y=f(t), \quad y(0)=0, y^{\prime}(0)=0$.
-40. $y^{\prime \prime}+y^{\prime}+y=f(t), \quad y(0)=0, y^{\prime}(0)=0$.
-41. $y^{\prime \prime}+4 y=\cos t, \quad y(0)=0, y^{\prime}(0)=0$.
-42. $4 y^{\prime \prime}+4 y^{\prime}+17 y=t, \quad y(0)=0, y^{\prime}(0)=0$.
-
-Project Problem: Periodic functions. As you know, in computing Fourier series all we need is knowledge of the function on an interval of length equal to one period. In Exercise 43 you are asked to derive a formula for the Laplace transform of a periodic function, which enables you to compute the transform from just knowing the function over one period. As a project, do Exercise 43 and any one of Exercises 44-47.
-43. Suppose that $f(t+T)=f(t)$ for all $t>0$; that is, $f$ is $T$-periodic.
-(a) Show that
-
-$$
-\mathcal{L}(f(t))=\sum_{k=0}^{\infty} \int_{k T}^{(k+1) T} e^{-s t} f(t) d t
-$$
-
-(b) Make a change of variables $\tau=t-k T$ and conclude that
-
-$$
-\mathcal{L}(f(t))=\int_{0}^{T} e^{-s t} f(t) d t \sum_{k=0}^{\infty} e^{-k s T}
-$$
-
-(c) Sum the (geometric) series and conclude that
-
-$$
-\mathcal{L}(f(t))=\frac{\int_{0}^{T} e^{-s t} f(t) d t}{1-e^{-s T}}
-$$
-
-In Exercises 44-47, compute the Laplace transform of the given function using the result of Exercise 43.
-44.
-![](./images/68332ba3-9551-434a-a491-ce53af60160e-20_385_583_2230_644.jpg)
-45.
-![](./images/68332ba3-9551-434a-a491-ce53af60160e-20_375_587_2234_1336.jpg)
-46.
-![](./images/68332ba3-9551-434a-a491-ce53af60160e-21_332_600_324_457.jpg)
-47.
-![](./images/68332ba3-9551-434a-a491-ce53af60160e-21_324_603_326_1175.jpg)
-48. A function is given by its power series expansion, $f(t)=\sum_{k=0}^{\infty} a_{k} t^{k}$ for all $t$. Show that
-
-$$
-\mathcal{L}(f(t))=\sum_{k=0}^{\infty} a_{k} \frac{k!}{s^{k+1}}
-$$
-
-49. Use the result of Exercise 48 to show that $\mathcal{L}\left(\frac{\sin t}{t}\right)=\tan ^{-1}\left(\frac{1}{s}\right)$. (For an alternative derivation, see Exercise 56.)
-50. Laplace transform of $J_{0}$. Recall from Section 4.3 that
-
-$$
-J_{0}(t)=\sum_{k=0}^{\infty} \frac{(-1)^{k} t^{2 k}}{2^{2 k}(k!)^{2}}
-$$
-
-(a) Use the binomial theorem to show that
-
-$$
-\frac{1}{\sqrt{1+s^{2}}}=\frac{1}{s}\left(1+\frac{1}{s^{2}}\right)^{-1 / 2}=\sum_{k=0}^{\infty} \frac{(-1)^{k}(2 k)!}{2^{2 k}(k!)^{2} s^{2 k+1}}, \quad s>1 .
-$$
-
-(b) Use the result of Exercise 48 and (a) to show that
-
-$$
-\mathcal{L}\left(J_{0}(t)\right)=\frac{1}{\sqrt{1+s^{2}}}
-$$
-
-(For an alternative derivation using residues, see Exercise 37, Section 5.1.)
-51. Proceed as in Exercise 50 to show that $\mathcal{L}\left(J_{0}(\sqrt{t})\right)=\frac{e^{-1 / 4 s}}{s}$.
-52. The error function. Use the Definition of the Laplace transform to show that
-
-$$
-\mathcal{L}(\operatorname{erf}(t))=\frac{2}{s \sqrt{\pi}} e^{\frac{s^{2}}{4}} \int_{s / 2}^{\infty} e^{-u^{2}} d u=\frac{1}{s} e^{\frac{s^{2}}{4}} \operatorname{erfc}\left(\frac{s}{2}\right)
-$$
-
-For the definition of the functions erf and erfc, see Section 11.4, (5) and Exercise 16.
-[Hint: After setting up the integrals, interchange the order of integration.]
-53. A Gaussian function. Use the definitions of the Laplace transform and the complementary error function to show that
-
-$$
-\mathcal{L}\left(\frac{1}{a \sqrt{\pi}} e^{-t^{2} / 4 a^{2}}\right)=e^{a^{2} s^{2}} \operatorname{erfc}(a s)
-$$
-
-54. Derive entry 37 in the table of Laplace transforms, Appendix B.4.
-55. Let $F(s)$ denote the Laplace transform of $f(t)$. Establish the identity
-
-$$
-\mathcal{L}\left(\frac{f(t)}{t}\right)=\int_{s}^{\infty} F(u) d u
-$$
-
-56. Derive the Laplace transform in Exercise 49 using the result of Exercise 55.
+## Exercises 9.2
+
+
+> [!prompt|4cdc30b5-1e9f-5a8d-adcb-55a2f0f37886.local at=917a6e8b-f15f-5cec-b1ff-c2753b0aecaa] Shared exercise instructions
+> In Exercises 1-6, evaluate the Laplace transform of the given function.
+
+
+
+> [!exercise|14a6c761-dafe-5607-965e-a3c8cc9fca6f.local at=127f0029-a70b-5626-b362-bba6f575b245] Exercise 1
+> $f(t)=\mathcal{U}_{0}(t-1)-t+1$.
+
+
+> [!exercise|31b2f064-5a0d-5b40-8bd7-b4b17e93b981.local at=55cec142-884b-557a-a9b2-ab4b676a1805] Exercise 2
+> $f(t)=(t-1) \mathcal{U}_{0}(t-1)$.
+
+
+> [!exercise|2100f96f-6dde-5f7b-9a5b-79befdaaaa66.local at=a5cd5d04-d177-5a56-a8dc-f889e5da4b3f] Exercise 3
+> $f(t)=e^{2 t} \mathcal{U}_{0}(t-2)$.
+
+
+> [!exercise|386515d1-93e9-5992-81c9-f48f6cfc5b78.local at=4603fb8f-2c66-539d-9393-b655d6233275] Exercise 4
+> $f(t)=t \mathcal{U}_{0}(t-\pi)$.
+
+
+> [!exercise|2140b944-a57a-5a85-aa12-4ee979413611.local at=f9699507-9463-5496-a641-1b0d31b13fa5] Exercise 5
+> $f(t)=\mathcal{U}_{0}(t-\pi) \sin t$.
+
+
+> [!exercise|8f428e34-5418-5ffc-a798-812129136e69.local at=a6f15d1b-b1b2-5799-ba8b-4be6d1e59887] Exercise 6
+> $f(t)=\mathcal{U}_{0}(t-\pi) \cos t \sin t$.
+
+
+> [!prompt|4cc38c9f-c6d8-5198-9e79-4cee28381ac0.local at=f3e1cae8-671c-5065-bc59-20b3ebf1989b] Shared exercise instructions
+> In Exercises 7-14, (a) plot the given function. (b) Express it using unit step functions. (c) Evaluate its Laplace transform.
+
+
+
+> [!exercise|fa1c7a8b-6461-5228-9405-17178398cda7.local at=a3fd85b7-d9d7-5e2d-9c00-469f1f75801b] Exercise 7
+> $f(t)= \begin{cases}1 & \text { if } 0<t<2, \\ 0 & \text { if } t>2 .\end{cases}$
+
+
+> [!exercise|c8419972-16a5-5f33-b948-b9714b063cd1.local at=af22b166-c1c0-5f90-8ee8-522364c62ac6] Exercise 8
+> $f(t)= \begin{cases}t & \text { if } 0 \leq t \leq 1, \\ 2-t & \text { if } 1 \leq t \leq 2, \\ 0 & \text { if } t>2 .\end{cases}$
+
+
+> [!exercise|aec8dcc8-4c5a-5867-8f0a-66a46be59ed9.local at=02f18372-8882-5ff2-98e2-385a05184c65] Exercise 9
+> $f(t)= \begin{cases}2 & \text { if } 2 \leq t \leq 3, \\ 0 & \text { otherwise. }\end{cases}$
+
+
+> [!exercise|4c11cef6-908c-58ae-9de0-230e734f39db.local at=d67f2857-c751-52be-bf20-76be3742f36b] Exercise 10
+> $f(t)= \begin{cases}t & \text { if } 0 \leq t \leq 1, \\ 0 & \text { otherwise. }\end{cases}$
+
+
+> [!exercise|42a4eb42-d6b7-5513-ae45-ef97725ef244.local at=4402727f-6a64-55c3-b3e4-2d148c6ebff2] Exercise 11
+> $f(t)= \begin{cases}t-1 & \text { if } 1 \leq t \leq 2, \\ 0 & \text { otherwise. }\end{cases}$
+
+
+> [!exercise|a6e8266e-2524-5ba0-a1c4-4be28b186ed1.local at=fc2d03ff-dbcc-5438-8d24-f4ddcde800de] Exercise 12
+> $f(t)= \begin{cases}-\sin t & \text { if } \pi \leq t \leq 2 \pi, \\ 0 & \text { otherwise. }\end{cases}$
+
+
+> [!exercise|16a06abf-b71a-5ead-a7a9-905607d33b0e.local at=5159ec4d-061c-5b2c-9f5f-8999af215274] Exercise 13
+> $f(t)= \begin{cases}1 & \text { if } 1 \leq t < 4, \\ t-5 & \text { if } 4 \leq t \leq 5, \\ 0 & \text { otherwise. }\end{cases}$
+
+
+> [!exercise|59b1efac-289a-51d4-a361-9a47add07843.local at=4ca65394-4016-5b73-bf48-fa2405fcb80b] Exercise 14
+> $f(t)= \begin{cases}t & \text { if } 0 \leq t \leq 1, \\ 1 & \text { if } 1 \leq t \leq 3, \\ 4-t & \text { if } 3<t \leq 4, \\ 0 & \text { otherwise. }\end{cases}$
+
+
+> [!prompt|21f82d1a-8ae8-5f97-a749-994a457eff03.local at=54976b37-18c2-5422-97f5-dc25533c54fa] Shared exercise instructions
+> In Exercises 15-22, evaluate the inverse Laplace transform of the given function.
+
+
+
+> [!exercise|268ca5cc-6c22-5342-ab7c-71fc33ec21e2.local at=bb4a8b7d-3a3b-55ee-b4c3-a9f34bac7600] Exercise 15
+> $F(s)=\frac{e^{-s}}{s^{2}}$.
+
+
+> [!exercise|26d46fc8-caad-5130-9f38-abaf77dc1aad.local at=6b5e6a48-004d-55b5-8675-f9972dd0e746] Exercise 16
+> $F(s)=\frac{e^{-\pi s}}{s^{2}-2}$.
+
+
+> [!exercise|2a5c4ac3-c0df-5d1d-a55d-ddde66d41a88.local at=41b8766a-7fac-57bc-8325-7ccc9a7c6204] Exercise 17
+> $F(s)=\frac{e^{-s}}{s^{2}+1}$.
+
+
+> [!exercise|0a43c8c1-6a03-51fc-b17f-27bdce2fb628.local at=c24b3f0e-71bf-58af-9b7e-3036fec55b20] Exercise 18
+> $F(s)=\frac{e^{-s}}{(s-1)^{2}-1}$.
+
+
+> [!exercise|0eeb3dd6-9228-512d-bd43-2caab488d46e.local at=e04e47f8-879c-5fcb-95d9-dee1aa809899] Exercise 19
+> $F(s)=\frac{s-3}{1+(s-3)^{2}}$.
+
+
+> [!exercise|47952a31-5c46-58b5-9aa7-1a76107cdba6.local at=52a29a67-0237-5740-983e-6458a1fcd143] Exercise 20
+> $F(s)=\frac{e^{-3 s}}{(s-1)(s+1)}$.
+
+
+> [!exercise|9b5644d4-2804-56c2-9c2c-32d2c2785c3d.local at=42aabbc2-030b-592e-9a9a-1b7cb6ddd8fc] Exercise 21
+> $F(s)=\frac{e^{-s}}{s^{3 / 2}}$.
+
+
+> [!exercise|ae0a681c-d966-59bd-81f2-90ef93ec6321.local at=0dd3fae1-7171-5fda-ac4f-75d43539608a] Exercise 22
+> $F(s)=\frac{e^{-s}}{(s-2)^{3 / 2}}$.
+
+
+> [!prompt|54358960-301d-5bb4-9c71-a580cd0f96a8.local at=5b04dd91-8d5f-531f-9ae5-bf9c01135bb8] Shared exercise instructions
+> In Exercises 23-28, evaluate the given convolution.
+
+
+
+> [!exercise|3a31c656-f9bd-5599-9854-f48715faaeb5.local at=899eed57-da41-5869-be63-f6baf999fc23] Exercise 23
+> $1 * t$.
+
+
+> [!exercise|60d02f82-95b9-56a6-9228-779b0a6d5a6d.local at=a498977c-0e82-505b-be6e-ee95261a7e24] Exercise 24
+> $e^{t} * e^{-t}$.
+
+
+> [!exercise|fbd2933f-ac66-504f-a44f-9aaa8c8248c0.local at=fd42a1e4-0267-5e96-b4a3-082e557aa696] Exercise 25
+> $t * t$.
+
+
+> [!exercise|31838210-1e08-5101-9cc4-6db7a28503ab.local at=515c167f-e3a2-5aa5-8629-f88b3c2e2eb9] Exercise 26
+> $t * \sin t$.
+
+
+> [!exercise|89bd773d-c7af-565c-b04b-be5e310646e1.local at=bad1579a-48f5-5601-982f-72750621f526] Exercise 27
+> $\sin t * \sin t$.
+
+
+> [!exercise|35f500c4-c19c-5f8e-b3da-307cd6bb7a73.local at=370502f1-f278-568b-b42c-ec001d26190a] Exercise 28
+> $e^{t} * \delta_{0}(t)$.
+
+
+> [!prompt|fe01b38d-0b60-56a5-b515-4b381887cd0f.local at=49bf516a-824e-570a-8642-0bf3d28eed4b] Shared exercise instructions
+> In Exercises 29-32, express the inverse Laplace transform of the given function as a convolution. Evaluate the integral in your answer.
+
+
+
+> [!exercise|a25c0edc-bb80-5d9c-a79c-f594f2ac01c5.local at=1ba6ec65-dbd2-55ef-8877-e51fee91acf0] Exercise 29
+> $F(s)=\frac{1}{s\left(s^{2}+1\right)}$.
+
+
+> [!exercise|5852b763-c787-5778-a837-502e2d94811d.local at=ea20669b-5f7c-5b11-bd31-f2d17c032c6f] Exercise 30
+> $F(s)=\frac{1}{s^{2}\left(s^{2}+1\right)}$.
+
+
+> [!exercise|3f9212e7-2e84-5c0a-9131-93c8613c4104.local at=0821e795-0994-58de-8dbc-1ddeb3aa507b] Exercise 31
+> $F(s)=\frac{1}{\left(s^{2}+1\right)\left(s^{2}+1\right)}$.
+
+
+> [!exercise|912c481e-35d8-5e60-a3aa-6e1ff7ffb940.local at=bffe23d8-1a59-508c-aded-3223ed575459] Exercise 32
+> $F(s)=\frac{s}{\left(s^{2}-1\right)\left(s^{2}-1\right)}$.
+
+
+> [!prompt|694f2de9-9034-5c3f-a67a-87df12b72d27.local at=c36564f3-61f8-58ec-aaf5-c9f29f368d79] Shared exercise instructions
+> In Exercises 33-38, solve the given initial value problem.
+
+
+
+> [!exercise|3d5e8fda-245f-5292-996a-535e65e4670c.local at=38df2c1a-f5fb-5894-85d1-aa751e7fe1c8] Exercise 33
+> $y^{\prime \prime}+y=\delta_{0}(t-1), \quad y(0)=0, \quad y^{\prime}(0)=0$.
+
+
+> [!exercise|033b9995-d6f6-56ae-aff3-7c390a157f75.local at=d8b6cb2c-4109-5fd5-821e-26f01482caef] Exercise 34
+> $y^{\prime \prime}-y=(t-2) \mathcal{U}_{0}(t-2), \quad y(0)=0, y^{\prime}(0)=0$.
+
+
+> [!exercise|e585b6bd-a1c5-5b34-b67c-4806608a9485.local at=d126f5ba-3e5e-5538-a930-0efa4fbe2919] Exercise 35
+> $y^{\prime \prime}+2 y^{\prime}+y=3 \delta_{0}(t-2), \quad y(0)=1, y^{\prime}(0)=0$.
+
+
+> [!exercise|f7759d36-f5b0-5e22-b6d2-a354483a923e.local at=9b47031d-85fc-5a6a-88b4-e90688beaec0] Exercise 36
+> $y^{\prime \prime}-y=t * \cos t, \quad y(0)=-1, y^{\prime}(0)=0$.
+
+
+> [!exercise|61e26ae7-7d36-5546-823e-e0835c2c9282.local at=932f90d4-855d-521b-9614-440593251c2d] Exercise 37
+> $y^{\prime \prime}+4 y=\mathcal{U}_{0}(t-1) e^{t-1}, \quad y(0)=0, y^{\prime}(0)=0$.
+
+
+> [!exercise|ee019527-5bfc-583c-aaa1-e61b9d4d71b2.local at=4d48b490-b502-51d8-a484-263df9834ba2] Exercise 38
+> $y^{\prime \prime}+y^{\prime}+y=\delta_{0}(t-\pi), \quad y(0)=0, y^{\prime}(0)=0$.
+
+
+> [!prompt|2474dd20-4ff7-5b3c-9681-286b6593be22.local at=08fd9392-6e4a-5bb5-90af-367ddf932bf2] Shared exercise instructions
+> In Exercises 39-42, express the solution of the given initial value problem as a convolution.
+
+
+
+> [!exercise|d91745b4-ce17-5d51-bbdd-366e481c4bfc.local at=33c2228c-09fb-5267-9057-333d324e43f2] Exercise 39
+> $y^{\prime \prime}+y=f(t), \quad y(0)=0, y^{\prime}(0)=0$.
+
+
+> [!exercise|52542cc7-71bb-5f7f-a1c5-dd059bdee7aa.local at=9649eeed-871c-5ceb-b857-47899531e5b0] Exercise 40
+> $y^{\prime \prime}+y^{\prime}+y=f(t), \quad y(0)=0, y^{\prime}(0)=0$.
+
+
+> [!exercise|81d6a80d-7e2d-559c-b15f-867c4f98a0bf.local at=cd5f590f-fc72-501a-aae9-028b5984d9ae] Exercise 41
+> $y^{\prime \prime}+4 y=\cos t, \quad y(0)=0, y^{\prime}(0)=0$.
+
+
+> [!exercise|f48c43e7-fe2a-5525-a5d5-2c19c98bb8c9.local at=7d0dc8d1-79cc-50ca-894f-72215fb83e7f] Exercise 42
+> $4 y^{\prime \prime}+4 y^{\prime}+17 y=t, \quad y(0)=0, y^{\prime}(0)=0$.
+
+
+> [!prompt|a571cf37-b70c-507d-8731-9ddbfeca72d5.local at=1334b86d-b2e1-537c-afb6-557f9cdba4d1] Shared exercise instructions
+> Project Problem: Periodic functions. As you know, in computing Fourier series all we need is knowledge of the function on an interval of length equal to one period. In Exercise 43 you are asked to derive a formula for the Laplace transform of a periodic function, which enables you to compute the transform from just knowing the function over one period. As a project, do Exercise 43 and any one of Exercises 44-47.
+
+
+
+> [!exercise|da33cf41-cb37-5b88-9321-2ccec58f054e.local at=f9e8ad3b-4744-57be-ba9b-20ed771413bc] Exercise 43
+> Suppose that $f(t+T)=f(t)$ for all $t>0$; that is, $f$ is $T$-periodic.
+> (a) Show that
+>
+> $$
+> \mathcal{L}(f(t))=\sum_{k=0}^{\infty} \int_{k T}^{(k+1) T} e^{-s t} f(t) d t
+> $$
+>
+> (b) Make a change of variables $\tau=t-k T$ and conclude that
+>
+> $$
+> \mathcal{L}(f(t))=\int_{0}^{T} e^{-s t} f(t) d t \sum_{k=0}^{\infty} e^{-k s T}
+> $$
+>
+> (c) Sum the (geometric) series and conclude that
+>
+> $$
+> \mathcal{L}(f(t))=\frac{\int_{0}^{T} e^{-s t} f(t) d t}{1-e^{-s T}}
+> $$
+
+
+> [!prompt|b89c6053-857a-58b8-973b-5e7627760b77.local at=1a13196f-4642-5dfb-9b3e-c04d6c53076a] Shared exercise instructions
+> In Exercises 44-47, compute the Laplace transform of the given function using the result of Exercise 43.
+
+
+
+> [!exercise|021f1238-fbf0-5f73-a87a-9f2302c1805c.local at=53660fdb-2ac0-5f8c-95a6-b4b58a90e449] Exercise 44
+> Use the accompanying figure and the shared instructions.
+
+
+```scientific-figure
+id: 56faa407-43a7-436a-8cdd-b9469d9801dc
+numbered: false
+title: ""
+caption: Given function for Exercise 44.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 09 The Laplace and Hankel Transforms with Applications/images/68332ba3-9551-434a-a491-ce53af60160e-20_385_583_2230_644.jpg
+    caption: ""
+```
+
+> [!exercise|f1dcf65c-06b5-5c1c-8f74-c6f803a79ad8.local at=0e2f6be7-41e1-570f-8d47-6d95cad97e05] Exercise 45
+> Use the accompanying figure and the shared instructions.
+
+
+```scientific-figure
+id: 4cb29c9a-d203-4803-b416-affd36368401
+numbered: false
+title: ""
+caption: Given function for Exercise 45.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 09 The Laplace and Hankel Transforms with Applications/images/68332ba3-9551-434a-a491-ce53af60160e-20_375_587_2234_1336.jpg
+    caption: ""
+```
+
+> [!exercise|6e0335f8-84e4-589f-a0c7-3fa174faf0b2.local at=5f1633aa-f7a3-55c9-a156-844a318e9699] Exercise 46
+> Use the accompanying figure and the shared instructions.
+
+
+```scientific-figure
+id: 4238227f-24d3-48ea-916e-8aa805cb3220
+numbered: false
+title: ""
+caption: Given function for Exercise 46.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 09 The Laplace and Hankel Transforms with Applications/images/68332ba3-9551-434a-a491-ce53af60160e-21_332_600_324_457.jpg
+    caption: ""
+```
+
+> [!exercise|585ade27-54bc-57f5-bcf3-b0345bd33b93.local at=44df0e22-1c58-56e8-bdb4-b53f9499e2cf] Exercise 47
+> Use the accompanying figure and the shared instructions.
+
+
+```scientific-figure
+id: a4193f47-3b2e-4b69-a229-3c6e2fc8b576
+numbered: false
+title: ""
+caption: Given function for Exercise 47.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 09 The Laplace and Hankel Transforms with Applications/images/68332ba3-9551-434a-a491-ce53af60160e-21_324_603_326_1175.jpg
+    caption: ""
+```
+
+> [!exercise|1a12ae04-8ba4-5e08-8c13-a4f5cdc16ee4.local at=12436879-7590-5b1e-a83c-6cc2e94bbb89] Exercise 48
+> A function is given by its power series expansion, $f(t)=\sum_{k=0}^{\infty} a_{k} t^{k}$ for all $t$. For $s>0$ such that $\sum_{k=0}^{\infty}|a_k|k!/s^{k+1}<\infty$, justify termwise integration and show that
+>
+> $$
+> \mathcal{L}(f(t))=\sum_{k=0}^{\infty} a_{k} \frac{k!}{s^{k+1}}
+> $$
+
+
+> [!exercise|8394d2f6-e622-5737-8dfe-75803b91923d.local at=a06f15f7-c012-53b4-b7b4-25f829ef55e4] Exercise 49
+> First for $s>1$, use the result of Exercise 48 to show that $\mathcal{L}\left(\frac{\sin t}{t}\right)=\tan ^{-1}\left(\frac{1}{s}\right)$. Extend the result to $s>0$ by analytic continuation, or use Exercise 56 for a direct derivation.
+
+
+> [!exercise|61ec8b6e-f9e4-5ef6-915a-ca9c6b45f37f.local at=291bde8c-6cf2-51cf-b61e-01f4b24b39b1] Exercise 50
+> Laplace transform of $J_{0}$. Recall from Section 4.3 that
+>
+> $$
+> J_{0}(t)=\sum_{k=0}^{\infty} \frac{(-1)^{k} t^{2 k}}{2^{2 k}(k!)^{2}}
+> $$
+>
+> (a) Use the binomial theorem to show that
+>
+> $$
+> \frac{1}{\sqrt{1+s^{2}}}=\frac{1}{s}\left(1+\frac{1}{s^{2}}\right)^{-1 / 2}=\sum_{k=0}^{\infty} \frac{(-1)^{k}(2 k)!}{2^{2 k}(k!)^{2} s^{2 k+1}}, \quad s>1 .
+> $$
+>
+> (b) First for $s>1$, use the result of Exercise 48 and (a) to show that
+>
+> $$
+> \mathcal{L}\left(J_{0}(t)\right)=\frac{1}{\sqrt{1+s^{2}}}
+> $$
+>
+> Extend the identity to $s>0$ by analyticity. (For an alternative derivation using residues, see Exercise 37, Section 5.1.)
+
+
+> [!exercise|2d599d0a-ad1d-5243-b7d7-10be4abe3269.local at=929d9c01-1167-527d-a760-897db065981b] Exercise 51
+> Proceed as in Exercise 50 to show that $\mathcal{L}\left(J_{0}(\sqrt{t})\right)=\frac{e^{-1 / 4 s}}{s}$.
+
+
+> [!exercise|49b03961-fe87-5b5f-a8c9-0ce98e1fe44e.local at=7ef048e5-aefc-57a4-a37a-353f7b0ad86d] Exercise 52
+> The error function. Use the Definition of the Laplace transform to show that
+>
+> $$
+> \mathcal{L}(\operatorname{erf}(t))=\frac{2}{s \sqrt{\pi}} e^{\frac{s^{2}}{4}} \int_{s / 2}^{\infty} e^{-u^{2}} d u=\frac{1}{s} e^{\frac{s^{2}}{4}} \operatorname{erfc}\left(\frac{s}{2}\right)
+> $$
+>
+> For the definition of the functions erf and erfc, see Section 8.4, (5) and Exercise 16.
+> [Hint: After setting up the integrals, interchange the order of integration.]
+
+
+> [!exercise|9dd6ed61-09da-5b2c-af91-73ff626846d5.local at=899c03e5-af4b-5b50-9bf8-99c939870cfe] Exercise 53
+> A Gaussian function. Let $a>0$. Use the definitions of the Laplace transform and the complementary error function to show that
+>
+> $$
+> \mathcal{L}\left(\frac{1}{a \sqrt{\pi}} e^{-t^{2} / 4 a^{2}}\right)=e^{a^{2} s^{2}} \operatorname{erfc}(a s)
+> $$
+
+
+> [!exercise|218668e3-7c91-55ef-a0a1-58bc0f6fd50e.local at=72329828-9e43-5c85-9eba-1a47afbb0a51] Exercise 54
+> Derive entry 37 in the table of Laplace transforms, Appendix B.4.
+
+
+> [!exercise|1cda18b5-079f-5e3b-872f-6e09a8babfbf.local at=7aec7642-17f8-5efc-9bdc-280da8273007] Exercise 55
+> Let $F(s)$ denote the Laplace transform of $f(t)$. Assume $\int_0^\infty |f(t)|e^{-st}/t\,dt<\infty$. Establish the identity
+>
+> $$
+> \mathcal{L}\left(\frac{f(t)}{t}\right)=\int_{s}^{\infty} F(u) d u
+> $$
+
+
+> [!exercise|d1d1db01-2a8a-5356-a871-d0fe54b4807e.local at=134079a6-9166-5558-b38f-154fe6bf7aa0] Exercise 56
+> Derive the Laplace transform in Exercise 49 using the result of Exercise 55.

`````
