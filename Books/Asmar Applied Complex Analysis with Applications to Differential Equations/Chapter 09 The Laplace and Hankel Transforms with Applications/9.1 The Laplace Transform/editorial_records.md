
# Editorial records

Reading note: 9.1 The Laplace Transform.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!definition|b9229dbe-41fd-56e8-be6f-4f260e3f4008.local at=6daf84c8-5a7e-5cae-afd2-aa1343710d2b] One-Sided Laplace Transform
> For a locally integrable function $f:[0,\infty)\to\mathbb C$, its one-sided Laplace transform is
>
> $$
> F(s)=\mathcal Lf(s)=\int_0^\infty f(t)e^{-st}\,dt
> $$
>
> where the improper integral converges. The parameter $s$ may be real or complex; absolute convergence holds in the right half-plane specified by an exponential growth bound.
````
### After

````text
> [!definition|b9229dbe-41fd-56e8-be6f-4f260e3f4008.local at=6daf84c8-5a7e-5cae-afd2-aa1343710d2b] One-Sided Laplace Transform
> Suppose that $f(t)$ is defined for all $t \geq 0$. The Laplace transform of $f$ is the function
> As a convention, functions $f, g, \ldots$ are defined for $t \geq 0$ and their transforms $F, G, \ldots$ are defined on the $s$-axis.
>
> $$
> \mathcal{L}(f)(s)=\int_{0}^{\infty} f(t) e^{-s t} d t
> $$
>
> Another commonly used notation for $\mathcal{L}(f)(s)$ is $F(s)$.
````

## 2. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!definition|9f1b84c9-6029-5529-bca1-cb463addb25a.local at=abe4fc0d-2f18-5027-9c50-28ca06c1962a] Global Exponential Bound on the Positive Half-Line
> A function $f:[0,\infty)\to\mathbb C$ satisfies a global exponential bound if there are constants $M>0$ and $a>0$ such that $|f(t)|\leq Me^{at}$ for every $t\geq0$.
````
### After

````text
> [!definition|9f1b84c9-6029-5529-bca1-cb463addb25a.local at=abe4fc0d-2f18-5027-9c50-28ca06c1962a] Exponential Order
> We say that $f$ is of exponential order if there exist positive numbers $a$ and $M$ such that
>
> $$
> |f(t)| \leq M e^{a t} \text { for all } t \geq 0
> $$
````

## 3. Remove assistant commentary comparing conventions; restore the author’s actual definition.

### Before

````text
The text calls this global bound “of exponential order.” It is stronger near zero than the convention that imposes the bound only for sufficiently large $t$.
````
### After

````text

````

## 4. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|e4f15047-1a89-56ba-a366-4da977816f96.local at=6abac71b-f0a9-5637-9140-8754976c1d5d] Existence of the Laplace Transform under an Exponential Bound
> Write $\mathcal Lf(s)=\int_0^\infty f(t)e^{-st}\,dt$ for the one-sided Laplace transform.
>
> If $f$ is piecewise continuous on every bounded subinterval of $[0,\infty)$ and $|f(t)|\leq Me^{at}$ for constants $M>0$ and real $a$, then $\mathcal Lf(s)$ converges absolutely for every complex $s$ with $\operatorname{Re}s>a$.
````
### After

````text
> [!theorem|e4f15047-1a89-56ba-a366-4da977816f96.local at=6abac71b-f0a9-5637-9140-8754976c1d5d] Existence of the Laplace Transform
> Write $\mathcal Lf(s)=\int_0^\infty f(t)e^{-st}\,dt$.
>
> Suppose that $f$ is piecewise continuous on the interval $[0, \infty)$ and of exponential order with $|f(t)| \leq M e^{a t}$ for all $t \geq 0$. Then $\mathcal{L}(f)(s)$ exists for all $s>a$.
````

## 5. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|c06973b1-0111-5f40-ac1e-b83269e28a8a.local at=a6e0737b-3255-5f46-aa18-76c15ffbea45] Linearity of the One-Sided Laplace Transform
> Write $\mathcal Lf(s)=\int_0^\infty f(t)e^{-st}\,dt$ for the one-sided Laplace transform.
>
> For constants $\alpha,\beta\in\mathbb C$ and functions $f,g$ whose transforms converge at $s$,
>
> $$
> \mathcal L(\alpha f+\beta g)(s)=\alpha\mathcal Lf(s)+\beta\mathcal Lg(s).
> $$
````
### After

````text
> [!theorem|c06973b1-0111-5f40-ac1e-b83269e28a8a.local at=a6e0737b-3255-5f46-aa18-76c15ffbea45] Linearity
> Write $\mathcal Lf(s)=\int_0^\infty f(t)e^{-st}\,dt$.
>
> Assume the transforms exist at the value of $s$ considered.
>
> $$
> \begin{aligned}
> & \text { If } f \text { and } g \text { are functions and } \alpha \text { and } \beta \text { are numbers, then } \\
> & \qquad \mathcal{L}(\alpha f+\beta g)=\alpha \mathcal{L}(f)+\beta \mathcal{L}(g)
> \end{aligned}
> $$
````

## 6. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|675e2821-a2b3-5efe-92ec-83d7bd866f90.local at=92279ffe-1f63-5248-a326-a14e135421db] Exponential Multiplication and Frequency Shifts of the Laplace Transform
> Write $\mathcal Lf(s)=\int_0^\infty f(t)e^{-st}\,dt$ for the one-sided Laplace transform.
>
> Let $f$ be piecewise continuous on bounded intervals of $[0,\infty)$, with $|f(t)|\leq Me^{at}$. For real $\alpha$ and $s>a+\alpha$,
>
> $$
> \mathcal L(e^{\alpha t}f(t))(s)=F(s-\alpha),\qquad F(s)=\mathcal Lf(s).
> $$
````
### After

````text
> [!theorem|675e2821-a2b3-5efe-92ec-83d7bd866f90.local at=92279ffe-1f63-5248-a326-a14e135421db] Shifting on the $s$-Axis
> Write $\mathcal Lf(s)=\int_0^\infty f(t)e^{-st}\,dt$.
>
> Suppose that $f$ is piecewise continuous and of exponential order. Let $\alpha$ be a real number and $a$ be such that $|f(t)|\leq Me^{at}$ for $t\geq0$ and some $M>0$. For $s>a+\alpha$, we have
>
> $$
> \mathcal{L}\left(e^{\alpha t} f(t)\right)(s)=F(s-\alpha)
> $$
>
> where $F(s)=\mathcal{L}(f(t))(s)$.
````

## 7. Move correction/commentary into the separate editorial record; keep the actual correction in the reading text.

### Before

````text
[Corrected: the printed inversion formulas have $e^{-zt}$; inversion requires $e^{zt}$.]
````
### After

````text

````

## Source-to-current comparison

Source: /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 09 The Laplace and Hankel Transforms with Applications/9.1 The Laplace Transform.md

This exact comparison preserves the full change evidence, including formatting, OCR corrections, restored source wording, and required standalone context. The entries above explain the recovery edits. The comparison is not a claim that every difference is a correction; component serialization, callout wrapping, and printed labels outside callouts are formatting.

`````diff
--- /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 09 The Laplace and Hankel Transforms with Applications/9.1 The Laplace Transform.md
+++ /Users/gradyclopton/ObsidianVaults/complex_analysis/Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 09 The Laplace and Hankel Transforms with Applications/9.1 The Laplace Transform.md
@@ -1,8 +1,9 @@
+
 Topics to Review
-Soctions 12.1 and 12.2 contain the hasic properties of the Laplace ransform and are self-contained. The applications of the Laplace transform to partial differential equations are presented in Section 9.3 and assume a familiarity with related boundary value problems for the heat and wave equations that have been treated earlier in the book. Section 9.4 develops the Hankel transform and requires some knowledge of the basic properties of Bessel functions from Sections 9.6 and 9.7 The applications in this section are also related to boundary value problems treated previously.
+Sections 9.1 and 9.2 contain the basic properties of the Laplace transform and are self-contained. The applications of the Laplace transform to partial differential equations are presented in Section 9.3 and assume a familiarity with related boundary value problems for the heat and wave equations that have been treated earlier in the book. Section 9.4 develops the Hankel transform and requires some knowledge of the basic properties of Bessel functions from Sections 12.6 and 12.7 The applications in this section are also related to boundary value problems treated previously.
 
 Looking Ahead
-This chapter adds to the diversity of problems and applications that we have treated thus far. With it we complete the treatment of the standard boundary malue problems that arise in the classical areas of heat conduction and wave motion. The reader who has encountered the Laplace transform in a course in ordinary differential equations will see it bere fulfilling, next to the Fourier transform, a major role in the solution of boundary value problems for partial differential equalions. And those of you who lave enjoyed Bessel functions will see them again here at the heart of the definition of yet another mportant transform, the Hankel transform.
+This chapter adds to the diversity of problems and applications that we have treated thus far. With it we complete the treatment of the standard boundary value problems that arise in the classical areas of heat conduction and wave motion. The reader who has encountered the Laplace transform in a course in ordinary differential equations will see it here fulfilling, next to the Fourier transform, a major role in the solution of boundary value problems for partial differential equations. And those of you who have enjoyed Bessel functions will see them again here at the heart of the definition of yet another important transform, the Hankel transform.
 
 ## 9
 
@@ -14,33 +15,44 @@
 
 In the previous chapter we introduced the Fourier transform and the Fourier sine and cosine transforms and showed their utility in solving various boundary value problems for partial differential equations on unbounded domains. The problems to which these transforms applied were typically treated in Cartesian coordinates. Another transform that can frequently be applied with success is the Laplace transform, our first topic in this chapter. If one of the variables occurring in a problem ranges over a half-line $[0, \infty)$, we can often make progress by performing a Laplace transform with respect to this variable, in much the same way that we did with the sine and cosine transforms. Because of the importance of this transform in other settings, we present a self-contained treatment, including the solution of initial value problems for ordinary differential equations. For problems with other than Cartesian geometry, there are yet other transforms that are more natural and therefore more useful. For example, in unbounded problems with radial symmetry in either the plane or the space, so that the appropriate coordinates are polar, cylindrical, or spherical, the natural transform for the radial variable ( $r$ or $\rho$ ) involves Bessel functions. This transform, which depends on the order $\nu$ of the Bessel function involved, is known as the Hankel transform of order $\nu$.
 
-### 9.1 The Laplace Transform
+# 9.1 The Laplace Transform
 
 In this section we present the definition and basic properties of the Laplace transform. As a warm-up for the applications with partial differential equations, we will use it to solve some simple ordinary differential equations.
 
-Suppose that $f(t)$ is defined for all $t \geq 0$. The Laplace transform of $f$ is the function
-As a convention, functions $f, g, \ldots$ are defined for $t \geq 0$ and their transforms $F, G, \ldots$ are defined on the $s$-axis.
-
-$$
-\mathcal{L}(f)(s)=\int_{0}^{\infty} f(t) e^{-s t} d t
-$$
-
-Another commonly used notation for $\mathcal{L}(f)(s)$ is $F(s)$. For the integral to exist $f$ cannot grow faster than an exponential. This motivates the following definition. We say that $f$ is of exponential order if there exist positive numbers $a$ and $M$ such that
-
-$$
-|f(t)| \leq M e^{a t} \text { for all } t \geq 0
-$$
+> [!definition|b9229dbe-41fd-56e8-be6f-4f260e3f4008.local at=6daf84c8-5a7e-5cae-afd2-aa1343710d2b] One-Sided Laplace Transform
+> Suppose that $f(t)$ is defined for all $t \geq 0$. The Laplace transform of $f$ is the function
+> As a convention, functions $f, g, \ldots$ are defined for $t \geq 0$ and their transforms $F, G, \ldots$ are defined on the $s$-axis.
+>
+> $$
+> \mathcal{L}(f)(s)=\int_{0}^{\infty} f(t) e^{-s t} d t
+> $$
+>
+> Another commonly used notation for $\mathcal{L}(f)(s)$ is $F(s)$.
+
+*Printed equation label: (1).*
+
+> [!definition|9f1b84c9-6029-5529-bca1-cb463addb25a.local at=abe4fc0d-2f18-5027-9c50-28ca06c1962a] Exponential Order
+> We say that $f$ is of exponential order if there exist positive numbers $a$ and $M$ such that
+>
+> $$
+> |f(t)| \leq M e^{a t} \text { for all } t \geq 0
+> $$
+
+*Printed equation label: (2).*
+
+
 
 For example, the functions $1,4 \cos 2 t, 5 t \sin 2 t, e^{3 t}$ are all of exponential order. We can now give a sufficient condition for the existence of the Laplace transform.
 
-THEOREM 1 EXISTENCE OF THE LAPLACE TRANSFORM
-
-Suppose that $f$ is piecewise continuous on the interval $[0, \infty)$ and of exponential order with $|f(t)| \leq M e^{a t}$ for all $t \geq 0$. Then $\mathcal{L}(f)(s)$ exists for all $s>a$.
+> [!theorem|e4f15047-1a89-56ba-a366-4da977816f96.local at=6abac71b-f0a9-5637-9140-8754976c1d5d] Existence of the Laplace Transform
+> Write $\mathcal Lf(s)=\int_0^\infty f(t)e^{-st}\,dt$.
+>
+> Suppose that $f$ is piecewise continuous on the interval $[0, \infty)$ and of exponential order with $|f(t)| \leq M e^{a t}$ for all $t \geq 0$. Then $\mathcal{L}(f)(s)$ exists for all $s>a$.
 
 Proof We have to show that for $s>a$
 
 $$
-\mathcal{L}(f)(s)=\int_{0}^{\infty} f(t) e^{-s t} d t<\infty
+\int_{0}^{\infty} |f(t)| e^{-s t} d t<\infty
 $$
 
 With $M$ and $a$ as before, we have
@@ -54,7 +66,11 @@
 
 Note that the function $\frac{1}{\sqrt{t}}$ is not of exponential order, because of its behavior at $t=0$. However, we will show in Example 2 that its Laplace transform $\mathcal{L}\left(\frac{1}{\sqrt{t}}\right)(s)$ exists for all $s>0$. Thus Theorem 1 provides sufficient but not necessary conditions for the existence of the Laplace transform.
 
-EXAMPLE $1 \mathcal{L}(1), \mathcal{L}(t)$, and $\mathcal{L}\left(e^{\alpha t}\right)$
+> [!exercise|b517e4a9-44c3-57ee-8783-a7c7f20a5df1.local at=8c1bb7e4-7b26-57e8-ab06-79554821febb] EXAMPLE 1 $\mathcal{L}(1), \mathcal{L}(t)$, and $\mathcal{L}\left(e^{\alpha t}\right)$
+> Compute $\mathcal L(1)$, $\mathcal L(t)$, and $\mathcal L(e^{\alpha t})$ directly from the defining integral, and give their domains.
+
+##### solution
+
 We compute these transforms using (1). We have
 
 $$
@@ -73,12 +89,14 @@
 Note that $\mathcal{L}\left(e^{\alpha t}\right)(s)$ is not defined for $s \leq \alpha$.
 In computing $\mathcal{L}(t)$ we had to integrate by parts once. Similarly, we could compute $\mathcal{L}\left(t^{n}\right)$ ( $n$ a positive integer) by integrating by parts $n$ times. Rather than doing this, we shall take advantage of an interesting connection between the Laplace transform and the gamma function.
 
-EXAMPLE $2 \mathcal{L}\left(t^{a}\right)$ via the gamma function
-(a) Evaluate $\mathcal{L}\left(t^{a}\right)(s)$ when $a>-1$ and $s>0$.
-(b) Derive from (a) the transforms $\mathcal{L}(t), \mathcal{L}\left(t^{2}\right)$, and, more generally $\mathcal{L}\left(t^{n}\right)$, where $n$ is a positive integer.
-(c) What is $\mathcal{L}\left(\frac{1}{\sqrt{t}}\right)$ ?
-
-Solution (a) From (1) we have
+> [!exercise|417cc5e3-4643-544e-9015-c74de100d288.local at=7d6e3f64-88ae-5981-9bbf-ef89eb040aa5] EXAMPLE 2 $\mathcal{L}\left(t^{a}\right)$ via the gamma function
+> (a) Evaluate $\mathcal{L}\left(t^{a}\right)(s)$ when $a>-1$ and $s>0$.
+> (b) Derive from (a) the transforms $\mathcal{L}(t), \mathcal{L}\left(t^{2}\right)$, and, more generally $\mathcal{L}\left(t^{n}\right)$, where $n$ is a positive integer.
+> (c) What is $\mathcal{L}\left(\frac{1}{\sqrt{t}}\right)$ ?
+
+##### solution
+
+(a) From (1) we have
 
 $$
 \mathcal{L}\left(t^{a}\right)(s)=\int_{0}^{\infty} t^{a} e^{-s t} d t
@@ -118,18 +136,25 @@
 
 We will derive in the rest of this section properties of the Laplace transform that will assist us in solving differential equations. We are particularly interested in those formulas involving a function, its transform, and the transform of its derivatives. These formulas are similar to the operational properties of the Fourier transform. Because the Laplace transform is defined by an integral over the interval $[0, \infty)$, some of the formulas will involve the values of the function and its derivatives at 0 .
 
-## THEOREM 2 LINEARITY
-
-$$
-\begin{aligned}
-& \text { If } f \text { and } g \text { are functions and } \alpha \text { and } \beta \text { are numbers, then } \\
-& \qquad \mathcal{L}(\alpha f+\beta g)=\alpha \mathcal{L}(f)+\beta \mathcal{L}(g)
-\end{aligned}
-$$
+> [!theorem|c06973b1-0111-5f40-ac1e-b83269e28a8a.local at=a6e0737b-3255-5f46-aa18-76c15ffbea45] Linearity
+> Write $\mathcal Lf(s)=\int_0^\infty f(t)e^{-st}\,dt$.
+>
+> Assume the transforms exist at the value of $s$ considered.
+>
+> $$
+> \begin{aligned}
+> & \text { If } f \text { and } g \text { are functions and } \alpha \text { and } \beta \text { are numbers, then } \\
+> & \qquad \mathcal{L}(\alpha f+\beta g)=\alpha \mathcal{L}(f)+\beta \mathcal{L}(g)
+> \end{aligned}
+> $$
 
 The proof is left as an exercise. You should also think about the domain of definition of $\mathcal{L}(\alpha f+\beta g)$ in terms of the domains of definition of $\mathcal{L}(f)$ and $\mathcal{L}(g)$.
 
-EXAMPLE $3 \mathcal{L}(\cos k t)$ and $\mathcal{L}(\sin k t)$
+> [!exercise|194d120e-96a1-59b0-b06c-55fbc87a7210.local at=af10696a-c897-58f1-93ba-b3c0365c4e93] EXAMPLE 3 $\mathcal{L}(\cos k t)$ and $\mathcal{L}(\sin k t)$
+> Compute $\mathcal L(\cos kt)$ and $\mathcal L(\sin kt)$ for real $k$ and $s>0$ using Euler’s identity.
+
+##### solution
+
 These transforms can be evaluated directly by using (1). Our derivation will be based on Euler's identity $e^{i k t}=\cos k t+i \sin k t$ and the linearity of the Laplace transform. We have
 
 $$
@@ -148,21 +173,24 @@
 
 The next result is very useful. It states that the Laplace transform takes derivatives into powers of $s$.
 
-THEOREM 3
-LAPLACE TRANSFORMS OF DERIVATIVES
-(i) Suppose that $f$ is continuous on $[0, \infty)$ and of exponential order as in (2). Suppose further that $f^{\prime}$ is piecewise continuous on $[0, \infty)$ and of exponential order. Then
-(3)
-
-$$
-\mathcal{L}\left(f^{\prime}\right)=s \mathcal{L}(f)-f(0)
-$$
-
-(ii) More generally, if $f, f^{\prime}, \ldots, f^{(n-1)}$ are continuous on $[0, \infty)$ and of exponential order as in (2), and $f^{(n)}$ is piecewise continuous on $[0, \infty)$ and of exponential order, then
-(4)
-
-$$
-\mathcal{L}\left(f^{(n)}\right)=s^{n} \mathcal{L}(f)-s^{n-1} f(0)-s^{n-2} f^{\prime}(0)-\cdots-f^{(n-1)}(0)
-$$
+> [!theorem|f525c8b5-a9ac-5106-9edb-4c1f124074f4.local at=fe4d9a46-eb30-5c99-a5a8-0f69a8cfa2eb] Laplace Transforms of Ordinary Derivatives
+> Write $\mathcal Lf(s)=\int_0^\infty f(t)e^{-st}\,dt$ for the one-sided Laplace transform.
+>
+> Let $n\geq1$ be an integer. Evaluate all transforms at real $s$ larger than the exponential growth rates of the functions involved. Derivatives at zero are right derivatives.
+>
+> (i) Suppose that $f$ is continuous on $[0, \infty)$ and of exponential order with a common bound $Me^{at}$. Suppose further that $f^{\prime}$ is piecewise continuous on $[0, \infty)$ and of exponential order. Then
+>
+> $$
+> \mathcal{L}\left(f^{\prime}\right)=s \mathcal{L}(f)-f(0)
+> $$
+>
+> (ii) More generally, if $f, f^{\prime}, \ldots, f^{(n-1)}$ are continuous on $[0, \infty)$ and of exponential order with a common bound $Me^{at}$, and $f^{(n)}$ is piecewise continuous on $[0, \infty)$ and of exponential order, then
+>
+> $$
+> \mathcal{L}\left(f^{(n)}\right)=s^{n} \mathcal{L}(f)-s^{n-1} f(0)-s^{n-2} f^{\prime}(0)-\cdots-f^{(n-1)}(0)
+> $$
+
+*Printed equation labels: (3) first derivative; (4) general derivative.*
 
 Proof Since $f$ is of exponential order, then (2) holds for some positive constants $a$ and $M$. The transform $\mathcal{L}\left(f^{\prime}\right)(s)$ is to be computed for $s>a$. Before we start the computation, note that for $s>a$
 
@@ -185,38 +213,46 @@
 
 $$
 \mathcal{L}\left(f^{\prime \prime}\right)=s^{2} \mathcal{L}(f)-s f(0)-f^{\prime}(0)
+\tag{5}
 $$
 
 The following is a counterpart of Theorem 3 showing that the Laplace transform takes powers of $t$ into derivatives.
-(i) Suppose $f(t)$ is piecewise continuous and of exponential order. Then
-(6)
-
-$$
-\mathcal{L}(t f(t))(s)=-\frac{d}{d s} \mathcal{L}(f)(s)
-$$
-
-(ii) In general, if $f(t)$ is piecewise continuous and of exponential order, then
-
-$$
-\mathcal{L}\left(t^{n} f(t)\right)=(-1)^{n} \frac{d^{n}}{d s^{n}} \mathcal{L}(f)(s)
-$$
+> [!theorem|13aabdbc-dba9-531a-9b23-053cce0dc9ce.local at=9480f161-e76f-52eb-911c-1531dd405b21] Differentiating a Laplace Transform by Multiplying by Powers of Time
+> Write $\mathcal Lf(s)=\int_0^\infty f(t)e^{-st}\,dt$ for the one-sided Laplace transform.
+>
+> Assume $|f(t)|\leq Me^{at}$ on $[0,\infty)$, take $s>a$, and let $n$ be a nonnegative integer.
+>
+> (i) Suppose $f(t)$ is piecewise continuous and of exponential order. Then
+>
+> $$
+> \mathcal{L}(t f(t))(s)=-\frac{d}{d s} \mathcal{L}(f)(s)
+> $$
+>
+> (ii) In general, if $f(t)$ is piecewise continuous and of exponential order, then
+>
+> $$
+> \mathcal{L}\left(t^{n} f(t)\right)=(-1)^{n} \frac{d^{n}}{d s^{n}} \mathcal{L}(f)(s)
+> $$
+
+*Printed equation labels: (6) multiplication by $t$; (7) multiplication by $t^n$.*
 
 Proof Differentiation under the integral sign gives
 
 $$
 \begin{aligned}
-|\mathcal{L}(f)|^{\prime}(s) & =\frac{d}{d s} \int_{0}^{\infty} f(t) e^{-s t} d t=\int_{0}^{\infty} f(t) \frac{d}{d s} e^{-s t} d t \\
+[\mathcal{L}(f)]^{\prime}(s) & =\frac{d}{d s} \int_{0}^{\infty} f(t) e^{-s t} d t=\int_{0}^{\infty} f(t) \frac{d}{d s} e^{-s t} d t \\
 & =-\int_{0}^{\infty} t f(t) e^{-s t} d t=-\mathcal{L}(t f(t))(s)
 \end{aligned}
 $$
 
 and (i) follows upon multiplying both sides by -1 . Part (ii) is obtained by repeated applications of (i). $\square$
 
-## EXAMPLE 4 Derivatives of transforms
-
-(a) Evaluate $\mathcal{L}(t \sin 2 t)$. (b) Evaluate $\mathcal{L}\left(t^{2} \sin t\right)$.
-
-Solution (a) Using (6) and Example 3, we find
+> [!exercise|ee78bea7-6d72-5ac3-98da-ddad3fe7d13c.local at=195eea38-7936-572b-9968-431b4b58b14d] EXAMPLE 4 Derivatives of transforms
+> (a) Evaluate $\mathcal{L}(t \sin 2 t)$. (b) Evaluate $\mathcal{L}\left(t^{2} \sin t\right)$.
+
+##### solution
+
+(a) Using (6) and Example 3, we find
 
 $$
 \mathcal{L}(t \sin 2 t)=-\frac{d}{d s} \frac{2}{s^{2}+4}=\frac{4 s}{\left(s^{2}+4\right)^{2}}
@@ -226,25 +262,29 @@
 
 $$
 \mathcal{L}\left(t^{2} \sin t\right)=\frac{d^{2}}{d s^{2}} \frac{1}{s^{2}+1}=\frac{2\left(-1+3 s^{2}\right)}{\left(s^{2}+1\right)^{3}}
-$$ $\square$
-
+$$
+
+$\square$
 The following theorem states that multiplication of a function by $e^{\alpha t}$ causes the transform to be shifted by $\alpha$ units on the $s$-axis. This very important property has a counterpart which involves a shift on the $t$-axis (see Theorem 1, Section 9.2).
 
-THEOREM 5 SHIFTING ON THE $\boldsymbol{s}$-AXIS
-
-Suppose that $f$ is of exponential order. Let $\alpha$ be a real number and $a$ be as in (2). For $s>a+\alpha$, we have
-
-$$
-\mathcal{L}\left(e^{\alpha t} f(t)\right)(s)=F(s-\alpha)
-$$
-
-where $F(s)=\mathcal{L}(f(t))(s)$.
-Proof Note that $e^{a t} f(t)$ is also of exponential order and (2) holds with $a$ replaced by $a+\alpha$. Thus Theorem 1 guarantees the existence of $\mathcal{L}\left(e^{\alpha t} f(t)\right.$ for $s>a+\alpha$. We have
+> [!theorem|675e2821-a2b3-5efe-92ec-83d7bd866f90.local at=92279ffe-1f63-5248-a326-a14e135421db] Shifting on the $s$-Axis
+> Write $\mathcal Lf(s)=\int_0^\infty f(t)e^{-st}\,dt$.
+>
+> Suppose that $f$ is piecewise continuous and of exponential order. Let $\alpha$ be a real number and $a$ be such that $|f(t)|\leq Me^{at}$ for $t\geq0$ and some $M>0$. For $s>a+\alpha$, we have
+>
+> $$
+> \mathcal{L}\left(e^{\alpha t} f(t)\right)(s)=F(s-\alpha)
+> $$
+>
+> where $F(s)=\mathcal{L}(f(t))(s)$.
+
+Proof Note that $e^{\alpha t} f(t)$ is also of exponential order and (2) holds with $a$ replaced by $a+\alpha$. Thus Theorem 1 guarantees the existence of $\mathcal{L}\left(e^{\alpha t} f(t)\right)$ for $s>a+\alpha$. We have
 
 $$
 \mathcal{L}\left(e^{\alpha t} f(t)\right)(s)=\int_{0}^{\infty} f(t) e^{\alpha t} e^{-s t} d t=\int_{0}^{\infty} f(t) e^{-(s-\alpha) t} d t=F(s-\alpha)
-$$ $\square$
-
+$$
+
+$\square$
 Taking $f=1$ in Theorem 5, we obtain the third transform in Example 1, $\mathcal{L}\left(e^{\alpha t}\right)=\frac{1}{s-\alpha}$, since $\mathcal{L}(1)=\frac{1}{s}$.
 
 ## The Inverse Laplace Transform
@@ -261,11 +301,13 @@
 \mathcal{L}^{-1}(\alpha F+\beta G)=\alpha \mathcal{L}^{-1}(F)+\beta \mathcal{L}^{-1}(G)
 $$
 
-EXAMPLE 5 Inverse Laplace transforms
-(a) Evaluate $\mathcal{L}^{-1}\left(\frac{2}{4+(s-1)^{2}}\right)$.
-(b) Evaluate $\mathcal{L}^{-1}\left(\frac{1}{s^{2}+2 s+3}\right)$.
-
-Solution (a) From the table of Laplace transforms, Appendix B. 4 (or by using Example 3 and Theorem 5), we find that
+> [!exercise|18f731a8-aa87-5438-a83f-6530a0c9b8ed.local at=3b3ca888-a317-5648-8db8-de1fb61f40e3] EXAMPLE 5 Inverse Laplace transforms
+> (a) Evaluate $\mathcal{L}^{-1}\left(\frac{2}{4+(s-1)^{2}}\right)$.
+> (b) Evaluate $\mathcal{L}^{-1}\left(\frac{1}{s^{2}+2 s+3}\right)$.
+
+##### solution
+
+(a) From the table of Laplace transforms, Appendix B. 4 (or by using Example 3 and Theorem 5), we find that
 
 $$
 \mathcal{L}\left(e^{a t} \sin k t\right)=\frac{k}{(s-a)^{2}+k^{2}}
@@ -295,10 +337,12 @@
 \mathcal{L}^{-1}\left(\frac{1}{s^{2}+2 s+3}\right)=\frac{1}{\sqrt{2}} \mathcal{L}^{-1}\left(\frac{\sqrt{2}}{(s+1)^{2}+(\sqrt{2})^{2}}\right)=\frac{1}{\sqrt{2}} e^{-t} \sin \sqrt{2} t
 $$
 
-## EXAMPLE 6 Partial fractions
-
-Evaluate $\mathcal{L}^{-1}\left(\frac{1}{s^{2}+2 s-3}\right)$.
-Solution First Method We can compute as we did in Example 5(b). First, write
+> [!exercise|96778785-3464-542f-9437-4a0c73f98ee6.local at=24806261-8764-5c37-8c60-27415c1c465d] EXAMPLE 6 Partial fractions
+> Evaluate $\mathcal{L}^{-1}\left(\frac{1}{s^{2}+2 s-3}\right)$.
+
+##### solution
+
+First Method We can compute as we did in Example 5(b). First, write
 
 $$
 \frac{1}{s^{2}+2 s-3}=\frac{1}{(s+1)^{2}-2^{2}}=\frac{1}{2} \frac{2}{(s+1)^{2}-2^{2}}
@@ -340,8 +384,12 @@
 
 The key to solving differential equations via the Laplace transform method is to use the operational properties, particularly those related to differentiation. We begin with a simple initial value problem. In what follows, we will denote the Laplace transform of $y(t)$ by $Y(s)$.
 
-EXAMPLE 7 Solving a differential equation with the Laplace transform: Solve $y^{\prime \prime}+y=2, \quad y(0)=0, y^{\prime}(0)=1$.
-Solution Taking the Laplace transform of both sides of the equation and using Theorem 3, we find
+> [!exercise|83feec4e-e672-5b3c-9514-f972ff0ac864.local at=ab1d48f5-ccf6-54f6-8549-c5d009b2901f] EXAMPLE 7 Solving a differential equation with the Laplace transform
+> Solve $y^{\prime \prime}+y=2, \quad y(0)=0, y^{\prime}(0)=1$.
+
+##### solution
+
+Taking the Laplace transform of both sides of the equation and using Theorem 3, we find
 
 $$
 s^{2} Y-s y(0)-y^{\prime}(0)+Y=\mathcal{L}(2)=\frac{2}{s}
@@ -370,9 +418,12 @@
 
 This example is a typical illustration of the Laplace transform method. Starting from a linear ordinary differential equation with constant coefficients in $y$, the Laplace transform produces an algebraic equation that can be solved for $Y$. The solution $y$ is then found by taking the inverse Laplace transform of $Y$. The Laplace transform method is most compatible with initial value problems where the initial data is given at $t=0$, due to the way the transform acts on derivatives. If the initial data is given at some other value $t_{0}$, the Laplace transform still applies: We simply make the change of variables $\tau=t-t_{0}$. The next example illustrates this process.
 
-EXAMPLE 8 Shifting the time variable
-Solve $y^{\prime \prime}+2 y^{\prime}+y=t, \quad y(1)=0, y^{\prime}(1)=0$.
-Solution Making the change of variables $\tau=t-1$, we arrive at the initial value problem
+> [!exercise|96fa5658-dd37-5e59-8273-df3c96598b14.local at=bf20d56d-2032-5d4f-9850-56bb8af4e468] EXAMPLE 8 Shifting the time variable
+> Solve $y^{\prime \prime}+2 y^{\prime}+y=t, \quad y(1)=0, y^{\prime}(1)=0$.
+
+##### solution
+
+Making the change of variables $\tau=t-1$, we arrive at the initial value problem
 
 $$
 y^{\prime \prime}+2 y^{\prime}+y=\tau+1, \quad y(0)=0, y^{\prime}(0)=0
@@ -400,13 +451,27 @@
 $$
 
 Hence the solution is $y(t)=e^{1-t}+t-2$.
-Recall from Section 11.2 an interesting way to compute the Fourier transform of $e^{-a x^{2}}$ was to take an indirect approach and consider a differential equation that is satisfied by $e^{-a x^{2}}$. These ideas work also with the Laplace transform, as we now illustrate by giving a simple derivation of the Laplace transform of $\cos k x$.
-
-![](./images/68332ba3-9551-434a-a491-ce53af60160e-10_545_508_1363_81.jpg)
-Figure 1 Since $K$ is closed and bounded and disjoint from the line $\operatorname{Re} z=a$, its distance to this line is $\delta>0$. For all $z$ in $K, \operatorname{Re} z>a+\delta$; so
-$\left|f(z) e^{-z t}\right| \leq M e^{a t} e^{-t \operatorname{Re} z} \leq M e^{-\delta t}$.
-
-EXAMPLE 9 Using differential equations to compute transforms
+Recall from Section 8.2 an interesting way to compute the Fourier transform of $e^{-a x^{2}}$ was to take an indirect approach and consider a differential equation that is satisfied by $e^{-a x^{2}}$. These ideas work also with the Laplace transform, as we now illustrate by giving a simple derivation of the Laplace transform of $\cos k x$.
+
+```scientific-figure
+id: 9b047eea-147c-498f-a698-3571f7ab2244
+numbered: false
+title: ""
+caption: Figure 1 Since $K$ is closed and bounded and disjoint from the line $\operatorname{Re} z=a$, its distance to this line is $\delta>0$. For all $z$ in $K, \operatorname{Re} z\geq a+\delta$; so $\left|f(t) e^{-z t}\right| \leq M e^{a t} e^{-t \operatorname{Re} z} \leq M e^{-\delta t}$.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 09 The Laplace and Hankel Transforms with Applications/images/68332ba3-9551-434a-a491-ce53af60160e-10_545_508_1363_81.jpg
+    caption: ""
+```
+
+
+> [!exercise|3bd9f79e-8e63-5381-8a63-43e860e7c430.local at=5b8d21e0-4c10-576b-a312-1e3920be2626] EXAMPLE 9 Using differential equations to compute transforms
+> Compute the Laplace transforms of $\cos kx$ and $\sin kx$ for real $k$ by transforming differential equations satisfied by these functions.
+
+##### solution
+
 The function $y=\cos k x$ is the unique solution of the initial value problem
 
 $$
@@ -435,6 +500,7 @@
 
 $$
 \mathcal{L}(f)(z)=\int_{0}^{\infty} f(t) e^{-z t} d t
+\tag{8}
 $$
 
 When $z$ is real, this definition reduces to (1). Also, for $\operatorname{Re} z>a$ (say $\operatorname{Re} z=a+\epsilon, \epsilon>0$ ) and all $t \geq 0$, we have
@@ -447,6 +513,7 @@
 
 $$
 \mathcal{L}(f)(z)=\int_{0}^{\infty} f(t) e^{-z t} d t=\sum_{n=0}^{\infty} \int_{n}^{n+1} f(t) e^{-z t} d t
+\tag{9}
 $$
 
 Each term in the sum is analytic, by Theorem 4, Section 3.5 (differentiation under the integral sign). Moreover, if $K$ is a closed and bounded subset of the half-plane $\operatorname{Re} z>a$, then there is a $\delta>0$ such that $\left|f(t) e^{-z t}\right| \leq M e^{-\delta t}$ for all $z$ in $K$ and all $t$ (see Figure 1). Hence, for all $z$ in $K$ and all $t$,
@@ -457,94 +524,266 @@
 
 Since $\sum_{n=0}^{\infty} M_{n}<\infty$, it follows from the Weierstrass $M$-test that the series in (9) converges uniformly for all $z$ in $K$. From Corollary 2, Section 4.2, we conclude that $\mathcal{L}(f)(z)$ is analytic in the half-plane $\operatorname{Re} z>a$.
 
-We now proceed to invert the Laplace transform by appealing to the inverse Fourier transform. Pick $b>a$, and define $g(t)=e^{-b t} f(t)$ if $t \geq 0$ and $g(t)=0$ if $t<0$. Then because $f$ is piecewise smooth and of exponential order with $a<b$, it follows that $g$ is integrable and piecewise smooth on the real line, and so we may apply the inverse Fourier transform (Theorem 1, Section 11.1). Using $g(t)=0$ for $t<0$, we have the Fourier transform
+We now proceed to invert the Laplace transform by appealing to the inverse Fourier transform. Pick $b>a$, and define $g(t)=e^{-b t} f(t)$ if $t \geq 0$ and $g(t)=0$ if $t<0$. Then because $f$ is piecewise smooth and of exponential order with $a<b$, it follows that $g$ is integrable and piecewise smooth on the real line, and so we may apply the inverse Fourier transform (Theorem 1, Section 8.1). Using $g(t)=0$ for $t<0$, we have the Fourier transform
 
 $$
 \widehat{g}(\omega)=\frac{1}{\sqrt{2 \pi}} \int_{0}^{\infty} e^{-b t} f(t) e^{-i \omega t} d t=\frac{1}{\sqrt{2 \pi}} \mathcal{L}(f)(b+i \omega)
+\tag{10}
 $$
 
 and the inverse Fourier transform
 
 $$
 g(t)=\lim _{R \rightarrow \infty} \frac{1}{\sqrt{2 \pi}} \int_{-R}^{R} \widehat{g}(\omega) e^{i \omega t} d \omega=\lim _{R \rightarrow \infty} \frac{1}{2 \pi} \int_{-R}^{R} \mathcal{L}(f)(b+i \omega) e^{i \omega t} d \omega,
+\tag{11}
 $$
 
 where the left side in (11) should be interpreted as the average of $g$ at the points of discontinuity. Making the change of variables $z=b+i \omega, d z=i d \omega$, and recalling that $g(t)=e^{-b t} f(t)$, we get
 
-![](./images/68332ba3-9551-434a-a491-ce53af60160e-11_453_473_1125_4.jpg)
-Figure 2
-
-$$
-e^{-b t} f(t)=\lim _{R \rightarrow \infty} \frac{e^{-b t}}{2 \pi i} \int_{b-i R}^{b+i R} \mathcal{L}(f)(z) e^{-z t} d z
+```scientific-figure
+id: df89e503-1421-4ad0-bc8d-790873b3b038
+numbered: false
+title: ""
+caption: Figure 2 Rectangular contour joining two vertical Laplace inversion paths.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 09 The Laplace and Hankel Transforms with Applications/images/68332ba3-9551-434a-a491-ce53af60160e-11_453_473_1125_4.jpg
+    caption: ""
+```
+
+
+$$
+e^{-b t} f(t)=\lim _{R \rightarrow \infty} \frac{e^{-b t}}{2 \pi i} \int_{b-i R}^{b+i R} \mathcal{L}(f)(z) e^{z t} d z
+\tag{12}
 $$
 
 where the integral is over the vertical line segment from $b-i R$ to $b+ i R$. Simplifying, and replacing $f$ by its average to account for the possible discontinuities, we obtain the inversion formula for the Laplace transform:
 
-$$
-\frac{f(t+)+f(t-)}{2}=\lim _{R \rightarrow \infty} \frac{1}{2 \pi i} \int_{b-i R}^{b+i R} \mathcal{L}(f)(z) e^{-z t} d z
-$$
+> [!equation|4c56c8f4-d1a7-5497-b916-2b44976dad76.local at=63100233-c082-54d0-a352-0c7721ac3cf8] Bromwich Inversion Formula for the One-Sided Laplace Transform
+> Let $f$ be piecewise smooth on bounded subintervals of $[0,\infty)$ and satisfy $|f(t)|\leq Me^{at}$. Define $\mathcal Lf(z)=\int_0^\infty f(t)e^{-zt}\,dt$ for $\operatorname{Re}z>a$. For $t>0$ and any real $b>a$,
+>
+> $$
+> \frac{f(t+)+f(t-)}{2}=\lim _{R \rightarrow \infty} \frac{1}{2 \pi i} \int_{b-i R}^{b+i R} \mathcal{L}(f)(z) e^{z t} d z
+> $$
+
+*Printed equation label: (13).*
+
+
+
+
 
 Note that the integral is independent of the choice of $b$ as long as $b>a$. To see this, given any two vertical line segments, we can close the contour as in Figure 2. The integral over the closed contour is 0 by Cauchy's theorem. A straightforward estimate on the integrand shows that the integrals over the horizontal sides tend to zero as $R \rightarrow \infty$. This implies that
 
 $$
-\lim _{R \rightarrow \infty} \frac{1}{2 \pi i} \int_{b-i R}^{b+i R} \mathcal{L}(f)(z) e^{-z t} d z=\lim _{R \rightarrow \infty} \frac{1}{2 \pi i} \int_{b^{\prime}-i R}^{b^{\prime}+i R} \mathcal{L}(f)(z) e^{-z t} d z
-$$
-
-as claimed. One important consequence of (13) is the uniqueness of the inverse Laplace transform. Since this inverse is given by an integral, any two inverses must be equal to the integral and thus must be the same.
-
-## Exercises 12.1
-
-In Erencises 1-6, show that the given function is of exponential order by establishing (2) with an appropriate choice of the numbers $a$ and $M$.
-
-1. $f(t)=11 \cos 3 t$.
-2. $f(t)=\sin 2 t+3 \cos t$.
-3. $f(t)=5 e^{3 t}$.
-4. $f(t)=t^{n}$.
-5. $f(t)=\sinh 3 t$.
-6. $f(t)=e^{5 t} \sinh t$.
-
-In Exercises $7-24$, evaluate the Laplace transform of the given function using appropriate theorems and examples from this section.
-7. $f(t)=2 t+3$.
-8. $f(t)=t^{2}+3 t^{4}$.
-9. $f(t)=\sqrt{t}+\frac{1}{\sqrt{t}}$.
-10. $f(t)=t^{2}+3 t+t^{3 / 2}$.
-11. $f(t)=t^{2} e^{3 t}$.
-12. $f(t)=t^{4} e^{-3 t}+e^{t}$.
-13. $f(t)=t \sin 4 t$.
-14. $f(t)=t^{2} \cos 2 t$.
-15. $f(t)=\sin ^{2} t$.
-16. $f(t)=\cos t \sin t$.
-17. $f(t)=e^{2 t} \sin 3 t$.
-18. $f(t)=t \sinh 3 t$.
-19. $f(t)=t e^{-t} \sin t$.
-20. $f(t)=e^{t+1} \cos t$.
-21. $f(t)=(t+2)^{2} \cos t$.
-22. $f(t)=e^{\alpha t} t^{3 / 2}$.
-23. $f(t)=e^{\alpha t} \sin \beta t$.
-24. $f(t)=e^{\alpha t} \cos \beta t$.
-
-In Exercises 25-38, evaluate the inverse Laplace transform of the given function.
-25. $F(s)=\frac{1}{s^{2}}$.
-26. $F(s)=\frac{1}{s^{2}-2}$.
-27. $F(s)=\frac{4}{3 s^{2}+1}$.
-28. $F(s)=\frac{1}{(s-1)^{2}-2}$.
-29. $F(s)=\frac{1}{(s-3)^{5}}+\frac{s-3}{1+(s-3)^{2}}$.
-30. $F(s)=\frac{1}{(s-1)(s+1)}$.
-31. $F(s)=\frac{s}{s^{2}+2 s+1}$.
-32. $F(s)=\frac{3 s+1}{s^{2}-2 s}$.
-33. $F(s)=\frac{2 s-1}{s^{2}-s-2}$.
-34. $F(s)=\frac{s-1}{(s+1)\left(s^{2}+1\right)}$.
-35. $F(s)=\frac{5 s^{2}+2 s-4}{2 s\left(s^{2}+s-2\right)}$.
-36. $F(s)=\frac{s^{2}+s+3}{(s+2)\left(s^{2}+1\right)}$.
-37. $F(s)=\frac{1}{s^{2}+3 s+2}$.
-38. $F(s)=\frac{s}{s^{2}+3 s+2}$.
-
-In Exercises 39-46, solve the given initial value problem with the Laplace transform.
-39. $y^{\prime}+y=\cos 2 t, \quad y(0)=-2$.
-40. $y^{\prime}+2 y=6 e^{\alpha t}, \quad y(0)=1, \alpha$ is a constant.
-41. $y^{\prime \prime}+y=\cos t, \quad y(\pi)=0, y^{\prime}(\pi)=0$.
-42. $y^{\prime \prime}-y=1+t^{2}, \quad y(1)=0, y^{\prime}(1)=1$.
-43. $y^{\prime \prime}+2 y^{\prime}+y=t e^{-2 t}, \quad y(0)=1, y^{\prime}(0)=1$.
-44. $y^{\prime \prime}+y^{\prime}+4 y=0, \quad y(0)=1, y^{\prime}(0)=1$.
-45. $y^{\prime \prime}-y^{\prime}-6 y=e^{t} \cos t, \quad y(0)=0, y^{\prime}(0)=1$.
-46. $y^{\prime \prime}+4 y^{\prime}+5 y=t^{2}, \quad y(0)=0, y^{\prime}(0)=1$.
+\lim _{R \rightarrow \infty} \frac{1}{2 \pi i} \int_{b-i R}^{b+i R} \mathcal{L}(f)(z) e^{z t} d z=\lim _{R \rightarrow \infty} \frac{1}{2 \pi i} \int_{b^{\prime}-i R}^{b^{\prime}+i R} \mathcal{L}(f)(z) e^{z t} d z
+$$
+
+as claimed. One important consequence of (13) is the uniqueness of the inverse Laplace transform. For piecewise smooth functions this determines the average of the one-sided limits, and hence determines the function almost everywhere. Two continuous inverses agree at every point; changing isolated function values does not change a Laplace transform.
+
+## Exercises 9.1
+
+
+> [!prompt|7d348de2-19be-5eb4-b5b7-56815c6c0e45.local at=75adb412-7bc2-5b28-8d87-4227a64fca45] Shared exercise instructions
+> In Exercises 1-6, show that the given function is of exponential order by establishing (2) with an appropriate choice of the numbers $a$ and $M$.
+
+
+
+> [!exercise|37132a44-907f-5a19-8afe-d61660da16b9.local at=dd4628fc-b920-54cc-a351-c831314bfd0d] Exercise 1
+> $f(t)=11 \cos 3 t$.
+
+
+> [!exercise|89c9b6a4-8033-5292-9da6-25bb4f856de2.local at=4f56e71d-92e3-53d1-94f7-57d1f7ec9f2b] Exercise 2
+> $f(t)=\sin 2 t+3 \cos t$.
+
+
+> [!exercise|715ab805-0c50-577d-b944-44b6e3624635.local at=159f1cb7-467f-5b81-a749-e8faf77b09ca] Exercise 3
+> $f(t)=5 e^{3 t}$.
+
+
+> [!exercise|a7b414cf-f6ca-5ce6-8eb7-a00abf5ec065.local at=6a13f64c-9f0e-585f-b2b9-ae2c19559ab9] Exercise 4
+> $f(t)=t^{n}$.
+
+
+> [!exercise|7fbb6db2-02c4-5e21-a022-6ae891a1eb59.local at=dd286212-2782-5033-84e6-3624c59bb070] Exercise 5
+> $f(t)=\sinh 3 t$.
+
+
+> [!exercise|c03a8711-afd3-5cc4-a5ea-fd53d1525325.local at=4cd5f156-d20e-553e-96fb-8bda75d7703f] Exercise 6
+> $f(t)=e^{5 t} \sinh t$.
+
+
+> [!prompt|c59cb457-228b-5418-929a-19bfcf4a1c68.local at=36e63b27-2d5f-5fd8-ae1b-c184dc661ccb] Shared exercise instructions
+> In Exercises $7-24$, evaluate the Laplace transform of the given function using appropriate theorems and examples from this section.
+
+
+
+> [!exercise|bee9b8b1-bdd7-530a-b68d-43a5605216af.local at=7e4df3eb-09b9-5fcf-9569-7c527c5fbca9] Exercise 7
+> $f(t)=2 t+3$.
+
+
+> [!exercise|3fa766c3-a1f0-5470-9567-60451fdaa425.local at=dd2fb6e3-b31a-5d97-a4c4-8b3e07867ca4] Exercise 8
+> $f(t)=t^{2}+3 t^{4}$.
+
+
+> [!exercise|1912a81a-e87e-543f-9c2b-81620c6e1862.local at=4fc7b2a9-f3ae-5265-9138-e5f69ee3e3e4] Exercise 9
+> $f(t)=\sqrt{t}+\frac{1}{\sqrt{t}}$.
+
+
+> [!exercise|d180cede-f962-5924-92a5-0129cf3824c7.local at=1727fb22-c471-5490-972a-d4a2465109be] Exercise 10
+> $f(t)=t^{2}+3 t+t^{3 / 2}$.
+
+
+> [!exercise|7dde0de0-9f17-5169-9638-0ce5099b4cb0.local at=ae2454d7-4a21-5e46-bb43-bba08718ada6] Exercise 11
+> $f(t)=t^{2} e^{3 t}$.
+
+
+> [!exercise|c1370a14-f320-571d-99b7-0f5bb0a82008.local at=48db4f59-3756-5e9d-9485-30fa48a326cd] Exercise 12
+> $f(t)=t^{4} e^{-3 t}+e^{t}$.
+
+
+> [!exercise|1bc68ad7-b91c-5392-8e8f-2e1565adddfc.local at=d8e95c33-58cf-5e2b-b564-9185d898a65e] Exercise 13
+> $f(t)=t \sin 4 t$.
+
+
+> [!exercise|cab61a7b-1854-5f87-bbb7-97d046fffdeb.local at=7daf2e47-24cb-5fa8-b9e2-7c8bed0fb1c2] Exercise 14
+> $f(t)=t^{2} \cos 2 t$.
+
+
+> [!exercise|e0f03877-b1da-5153-b0c7-af850c24ab41.local at=d5d22c3c-47eb-51ce-a4ca-9c9c83d61d19] Exercise 15
+> $f(t)=\sin ^{2} t$.
+
+
+> [!exercise|99419e9f-799c-5966-9fb1-3ac1ca23d72b.local at=6fad17aa-3018-545e-a870-2c3c42caa83d] Exercise 16
+> $f(t)=\cos t \sin t$.
+
+
+> [!exercise|09c9b9cc-1e35-51a9-ab73-0287bbf243b8.local at=21c8b8ba-a472-5bdc-bb56-1f2b7bfbe4ed] Exercise 17
+> $f(t)=e^{2 t} \sin 3 t$.
+
+
+> [!exercise|1a7c4133-d55f-51ee-82b8-e9e3772739b4.local at=c6977e77-b300-52ad-9751-1e70bf19bbb1] Exercise 18
+> $f(t)=t \sinh 3 t$.
+
+
+> [!exercise|8b746742-60c7-5313-bebe-3ad9c9ade872.local at=498ee93e-d85b-5b65-8706-2001272a2026] Exercise 19
+> $f(t)=t e^{-t} \sin t$.
+
+
+> [!exercise|2ddd182a-6038-5f8c-b4c5-4c2e9af56a42.local at=652c4618-5f20-5370-8b84-354a3f11deaf] Exercise 20
+> $f(t)=e^{t+1} \cos t$.
+
+
+> [!exercise|eef6a3e6-8c22-5b62-af12-3c1258d67f3f.local at=a612a7ef-7fe9-54ca-86e1-f3098afa365a] Exercise 21
+> $f(t)=(t+2)^{2} \cos t$.
+
+
+> [!exercise|035bba93-0e79-598c-86ba-fa6e55dc6cd9.local at=5517bc82-6368-5b8a-b239-4cf2766cb0e0] Exercise 22
+> $f(t)=e^{\alpha t} t^{3 / 2}$.
+
+
+> [!exercise|788483f1-10ac-595c-9cb2-c3beb362392a.local at=4240dba6-97e0-5d9e-99c1-d3cb699e3034] Exercise 23
+> $f(t)=e^{\alpha t} \sin \beta t$.
+
+
+> [!exercise|080f1990-f445-5341-92d6-0ce58edef4d0.local at=b0819f47-7218-5f47-af85-8bd2948a0400] Exercise 24
+> $f(t)=e^{\alpha t} \cos \beta t$.
+
+
+> [!prompt|4e3450e3-80f8-5d90-8de6-0ad2af987658.local at=52178a85-523c-5602-90f9-6d0c8b5c7527] Shared exercise instructions
+> In Exercises 25-38, evaluate the inverse Laplace transform of the given function.
+
+
+
+> [!exercise|e5d66214-8834-5485-8d22-19c4bbcc9402.local at=1fd1ab4b-c929-5cc7-a3de-a80fff7661e5] Exercise 25
+> $F(s)=\frac{1}{s^{2}}$.
+
+
+> [!exercise|0d8659a9-e063-559b-891b-399c2873b203.local at=61cc6844-6c19-584a-a8e4-c4cb51c6fcde] Exercise 26
+> $F(s)=\frac{1}{s^{2}-2}$.
+
+
+> [!exercise|7fab6157-9035-574f-8562-ddf1a50ed726.local at=fcf12e19-bae4-578f-a292-66d51eda788c] Exercise 27
+> $F(s)=\frac{4}{3 s^{2}+1}$.
+
+
+> [!exercise|9e28b6b3-e51a-5a58-a62f-d8c161258de7.local at=af7b0731-e9d1-572a-b892-b1e5ba52e38c] Exercise 28
+> $F(s)=\frac{1}{(s-1)^{2}-2}$.
+
+
+> [!exercise|cb05d7cb-45d0-51cd-9403-e52b004a5c23.local at=f8ff2f0a-ba89-5f30-92bb-8fbb4ea2833b] Exercise 29
+> $F(s)=\frac{1}{(s-3)^{5}}+\frac{s-3}{1+(s-3)^{2}}$.
+
+
+> [!exercise|c1b5a261-a249-5e05-aed7-9e390d1f029f.local at=6ffcbada-5bc8-5fc5-be90-cc97e713ecac] Exercise 30
+> $F(s)=\frac{1}{(s-1)(s+1)}$.
+
+
+> [!exercise|9256e9a7-488b-57ec-b374-55ca08a360e1.local at=37080173-8990-5398-bd17-352f8715040c] Exercise 31
+> $F(s)=\frac{s}{s^{2}+2 s+1}$.
+
+
+> [!exercise|86ab6b88-96f7-52e4-ab78-959a6bb621db.local at=5ead0511-20a0-57e4-8449-93d4c704ee12] Exercise 32
+> $F(s)=\frac{3 s+1}{s^{2}-2 s}$.
+
+
+> [!exercise|c8af3af9-0479-559b-8d4f-5636bf60c5de.local at=becda241-28c6-5ac5-ae38-67983cf28eee] Exercise 33
+> $F(s)=\frac{2 s-1}{s^{2}-s-2}$.
+
+
+> [!exercise|539ef9e2-ad87-512c-9dd6-20323c557571.local at=0ee1c0e3-a9e8-5040-859b-d124ba8fc076] Exercise 34
+> $F(s)=\frac{s-1}{(s+1)\left(s^{2}+1\right)}$.
+
+
+> [!exercise|e6fba0f0-ad34-5f5e-804c-a1c327582ed6.local at=5c8eb7bf-34c9-5f04-b57a-91b9c632416a] Exercise 35
+> $F(s)=\frac{5 s^{2}+2 s-4}{2 s\left(s^{2}+s-2\right)}$.
+
+
+> [!exercise|02d7a3a7-ae64-5802-b5ad-1f183c8f7bbd.local at=a6c9d17a-a96f-5249-8794-4f13cc8c0de6] Exercise 36
+> $F(s)=\frac{s^{2}+s+3}{(s+2)\left(s^{2}+1\right)}$.
+
+
+> [!exercise|2f54dc45-8d99-5c9b-b428-f7fbca40b7e6.local at=1b6d4a8c-39dd-5496-8723-baf1159b2ab7] Exercise 37
+> $F(s)=\frac{1}{s^{2}+3 s+2}$.
+
+
+> [!exercise|ace43345-98c3-5bed-8ecd-ef6e77eecb51.local at=1deffd94-bda7-59a9-8f2c-6bbfe1a01486] Exercise 38
+> $F(s)=\frac{s}{s^{2}+3 s+2}$.
+
+
+> [!prompt|ddab6aeb-8cfd-5ebc-bca7-8b469a50fe30.local at=3ce67502-498a-5724-822c-9249b12f7d75] Shared exercise instructions
+> In Exercises 39-46, solve the given initial value problem with the Laplace transform.
+
+
+
+> [!exercise|21500628-de95-5fc1-a261-49afc97ac995.local at=c4c5ff45-49d2-5669-8e8b-5a71f47196a5] Exercise 39
+> $y^{\prime}+y=\cos 2 t, \quad y(0)=-2$.
+
+
+> [!exercise|c9771299-4bad-51de-b104-0a153e756a3c.local at=f8e201a9-0eb1-5b31-9f18-80d07dfd1a37] Exercise 40
+> $y^{\prime}+2 y=6 e^{\alpha t}, \quad y(0)=1, \alpha$ is a constant.
+
+
+> [!exercise|42cdc5d2-8811-524d-9a5a-220cbdb6e8cb.local at=5f8f1b0a-c57b-5125-a55a-d4656943ca21] Exercise 41
+> $y^{\prime \prime}+y=\cos t, \quad y(\pi)=0, y^{\prime}(\pi)=0$.
+
+
+> [!exercise|2ccdc8fb-6175-5533-8946-dc61ff894aec.local at=ec424ce7-c336-5666-ab44-934bdee0e756] Exercise 42
+> $y^{\prime \prime}-y=1+t^{2}, \quad y(1)=0, y^{\prime}(1)=1$.
+
+
+> [!exercise|c4bef097-39e1-52fd-9884-2a2b1a5c03a0.local at=8b527dcd-1ebb-57ea-af54-6129340802f3] Exercise 43
+> $y^{\prime \prime}+2 y^{\prime}+y=t e^{-2 t}, \quad y(0)=1, y^{\prime}(0)=1$.
+
+
+> [!exercise|1a96017c-aa5f-5a84-9777-bc39a0ccc653.local at=1cc8c53c-4dc1-556c-a00b-840e3189fec8] Exercise 44
+> $y^{\prime \prime}+y^{\prime}+4 y=0, \quad y(0)=1, y^{\prime}(0)=1$.
+
+
+> [!exercise|77a1c7eb-fb13-52c7-a0fb-336e95ff7479.local at=42c6a11f-a664-594d-8c78-f8b1fcaf60af] Exercise 45
+> $y^{\prime \prime}-y^{\prime}-6 y=e^{t} \cos t, \quad y(0)=0, y^{\prime}(0)=1$.
+
+
+> [!exercise|6c0d940d-8137-54cf-a5ce-8c204b272d4a.local at=2899ae7e-1b5c-5960-b6bb-5e8a01d1fec4] Exercise 46
+> $y^{\prime \prime}+4 y^{\prime}+5 y=t^{2}, \quad y(0)=0, y^{\prime}(0)=1$.

`````
