
# Editorial records

Reading note: 13.5 Legendre's Differential Equation.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!definition|e429f6d7-0540-5e28-9e61-221696326ae9.local at=41c415fa-9568-515f-b55a-fd8b0d556215] Legendre polynomial with the normalization at one
> For a nonnegative integer $n$, the Legendre polynomial $P_n$ is the degree-$n$ polynomial solution of
> $$
> (1-x^2)y''-2xy'+n(n+1)y=0
> $$
> normalized by $P_n(1)=1$. Equivalently, its leading coefficient is $(2n)!/[2^n(n!)^2]$, and
> $$
> P_n(x)=\frac1{2^n}\sum_{m=0}^{\lfloor n/2\rfloor}(-1)^m\frac{(2n-2m)!}{m!(n-m)!(n-2m)!}x^{n-2m}.
> $$
````
### After

````text
> [!definition|e429f6d7-0540-5e28-9e61-221696326ae9.local at=41c415fa-9568-515f-b55a-fd8b0d556215] Legendre polynomial with the normalization at one
> For a nonnegative integer $n$, the polynomial solution of $(1-x^2)y^{\prime\prime}-2xy^{\prime}+n(n+1)y=0$, normalized by $P_n(1)=1$, is called the Legendre polynomial of degree $n$ and is denoted by $P_{n}(x)$. Setting $M=n / 2$ if $n$ is even or $(n-1) / 2$ if $n$ is odd, the $n$th Legendre polynomial becomes
>
> $$
> P_{n}(x)=\frac{1}{2^{n}} \sum_{m=0}^{M}(-1)^{m} \frac{(2 n-2 m)!}{m!(n-m)!(n-2 m)!} x^{n-2 m} .
> $$
````

## 2. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!equation|b18296d0-620e-5825-a4de-838c8ec5f642.local at=ab1df737-5909-567a-863a-e8af3166a93f] General solution of Legendre’s equation of integer degree
> For a fixed integer $n\ge0$, the general solution of
> $$
> (1-x^2)y''-2xy'+n(n+1)y=0,\qquad -1<x<1,
> $$
> is
> $$
> y(x)=c_1P_n(x)+c_2Q_n(x),
> $$
> where $P_n$ is the Legendre polynomial normalized by $P_n(1)=1$, $Q_n$ is the real Legendre function of the second kind on $(-1,1)$, and $c_1,c_2$ are arbitrary constants. The function $P_n$ is bounded at both endpoints, whereas $Q_n$ is unbounded there.
````
### After

````text
> [!equation|b18296d0-620e-5825-a4de-838c8ec5f642.local at=ab1df737-5909-567a-863a-e8af3166a93f] General solution of Legendre’s equation of integer degree
> Hence the general solution of Legendre's equation $(1-x^2)y^{\prime\prime}-2xy^{\prime}+n(n+1)y=0$ of order $n\ge0$ on $-1<x<1$ is
>
> $$
> y(x)=c_{1} P_{n}(x)+c_{2} Q_{n}(x)
> $$
>
> where $c_{1}$ and $c_{2}$ are arbitrary constants.
>
> Here $P_n$ is the Legendre polynomial normalized by $P_n(1)=1$. The function $Q_n$ is the Legendre function of the second kind.
````

## 3. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!property|82caf074-b664-5cfc-ae3f-b233b751fd0d.local at=0a04882c-d6f2-52b0-93ba-d9f678235427] Parity, endpoint values, bounds and zeros of Legendre polynomials
> For integers $n\ge0$, let $P_n$ be the Legendre polynomial normalized by $P_n(1)=1$. Then
> $$
> P_n(-x)=(-1)^nP_n(x),\qquad P_n(-1)=(-1)^n,
> $$
> and $|P_n(x)|\le1$ for $-1\le x\le1$. For $n\ge1$, $P_n$ has exactly $n$ distinct zeros in $(-1,1)$, and all its relative extrema lie in $[-1,1]$. The constant polynomial $P_0=1$ is excluded from the extrema-location assertion.
````
### After

````text
> [!property|82caf074-b664-5cfc-ae3f-b233b751fd0d.local at=0a04882c-d6f2-52b0-93ba-d9f678235427] Further Properties of Legendre Polynomials
> $P_{n}$ is even if $n$ is even and odd if $n$ is odd. $P_{n}(1)=1$ and $P_{n}(-1)=(-1)^{n}$ for all $n$.
> $\left|P_{n}(x)\right| \leq 1$ for all $n$ and all $x$ in $[-1,1]$. $P_{n}(x)$ has $n$ distinct zeros in $[-1,1]$. For $n\ge1$, all relative maxima and minima of $P_{n}$ occur in $[-1,1]$.
>
> Here $P_n$ is the Legendre polynomial normalized by $P_n(1)=1$.
````

## 4. Restore source wording; retain only the actual correction.

### Before

````text
The conventional gravitational potential is the negative of this function.
````
### After

````text

````

## 5. Restore source wording; retain only the actual correction.

### Before

````text
[Numbering corrected: the source repeats Exercise 31.]
````
### After

````text

````

## 6. Restore source wording; retain only the actual correction.

### Before

````text
with radii of convergence at least 1 (the zero function $q$ when $\mu=0$ has infinite radius)
````
### After

````text
with radii of convergence at least 1
````

## Source-to-current comparison

Source: /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 13 Partial Differential Equations in Spherical Coordinates/13.5 Legendre's Differential Equation.md

This exact comparison preserves the full change evidence, including formatting, OCR corrections, restored source wording, and required standalone context. The entries above explain the recovery edits. The comparison is not a claim that every difference is a correction; component serialization, callout wrapping, and printed labels outside callouts are formatting.

`````diff
--- /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 13 Partial Differential Equations in Spherical Coordinates/13.5 Legendre's Differential Equation.md
+++ /Users/gradyclopton/ObsidianVaults/complex_analysis/Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 13 Partial Differential Equations in Spherical Coordinates/13.5 Legendre's Differential Equation.md
@@ -1,11 +1,13 @@
+
 ### 13.5 Legendre's Differential Equation
 
-A through review of the methods that are used in this section is presented in Appendixes A. 4 and A.5. These sections are strongly recommended for readers who are not familiar with the power series method for solving ordinary differential equations.
+A thorough review of the methods that are used in this section is presented in Sections 10.4 and 10.5. These sections are strongly recommended for readers who are not familiar with the power series method for solving ordinary differential equations.
 
 ## Legendre's differential equation
 
 $$
 \left(1-x^{2}\right) y^{\prime \prime}-2 x y^{\prime}+\mu y=0, \quad-1<x<1,
+\tag{1}
 $$
 
 arose when solving Laplace's equation in spherical coordinates (see (13), Section 13.1). It is thus a very important differential equation. Legendre's differential equation is really a family of equations, one for each value of the parameter $\mu$. Upon dividing by $\left(1-x^{2}\right)$, the equation becomes
@@ -14,7 +16,7 @@
 y^{\prime \prime}-\frac{2 x}{1-x^{2}} y^{\prime}+\frac{\mu}{1-x^{2}} y=0
 $$
 
-Using the geometric series expansion, we can verify that the functions $p(x)= -\frac{2 x}{1-x^{2}}$ and $q(x)=\frac{\mu}{1-x^{2}}$ have power series expansions about 0 with both radii of convergence equal to 1. It follows from Theorem 1, Appendix A.5, that (1) has two linearly independent solutions given by power series that converge for $|x|<1$. To find these solutions we substitute $y=\sum_{m=0}^{\infty} a_{m} x^{m}$ and its derivatives into (1) and get
+Using the geometric series expansion, we can verify that the functions $p(x)= -\frac{2 x}{1-x^{2}}$ and $q(x)=\frac{\mu}{1-x^{2}}$ have power series expansions about 0 with radii of convergence at least 1. It follows from Theorem 1, Section 10.5, that (1) has two linearly independent solutions given by power series that converge for $|x|<1$. To find these solutions we substitute $y=\sum_{m=0}^{\infty} a_{m} x^{m}$ and its derivatives into (1) and get
 
 $$
 \left(1-x^{2}\right) \sum_{m=2}^{\infty} m(m-1) a_{m} x^{m-2}-2 x \sum_{m=1}^{\infty} m a_{m} x^{m-1}+\mu \sum_{m=0}^{\infty} a_{m} x^{m}=0 .
@@ -43,8 +45,19 @@
 
 Thus $a_{0}$ determines $a_{2}$, which determines $a_{4}, a_{6}, \ldots$, and $a_{1}$ determines $a_{3}$, which determines $a_{5}, a_{7}, \ldots$ Using these coefficients, we get the two series solutions, known as Legendre functions, one consisting of even powers of $x$ only and the other consisting of odd powers of $x$ only.
 
-![](./images/122e2a0e-ba5b-4934-9af1-dcd4ea360903-33_399_461_873_46.jpg)
-Figure 1 Legendre functions with $\mu=3 / 4$.
+```scientific-figure
+id: 11dccc95-7ec5-42a9-adca-0c2dd9e67082
+numbered: false
+title: ""
+caption: Figure 1 Legendre functions with $\mu=3 / 4$.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 13 Partial Differential Equations in Spherical Coordinates/images/122e2a0e-ba5b-4934-9af1-dcd4ea360903-33_399_461_873_46.jpg
+    caption: ""
+```
+
 
 ## Legendre Polynomials
 
@@ -58,17 +71,20 @@
 
 $$
 a_{m+2}=-\frac{(n-m)(n+m+1)}{(m+2)(m+1)} a_{m},
+\tag{2}
 $$
 
 from which we get
 
 $$
-\begin{gathered}
-a_{2}=-\frac{n(n+1)}{2!} a_{0} \\
-a_{4}=\frac{(n-2) n(n+1)(n+3)}{4!} a_{0} \quad a_{3}=-\frac{(n-1)(n+2)}{3!} a_{1} \\
-a_{6}=-\frac{(n-3)(n-1)(n+2)(n+4)}{5!} a_{1} \\
-a_{7}=-\frac{(n-5)(n-3)(n-1)(n+2)(n+4)(n+6)}{7!} a_{1} .
-\end{gathered}
+\begin{aligned}
+a_2&=-\frac{n(n+1)}{2!}a_0,&
+a_3&=-\frac{(n-1)(n+2)}{3!}a_1,\\
+a_4&=\frac{(n-2)n(n+1)(n+3)}{4!}a_0,&
+a_5&=\frac{(n-3)(n-1)(n+2)(n+4)}{5!}a_1,\\
+a_6&=-\frac{(n-4)(n-2)n(n+1)(n+3)(n+5)}{6!}a_0,&
+a_7&=-\frac{(n-5)(n-3)(n-1)(n+2)(n+4)(n+6)}{7!}a_1.
+\end{aligned}
 $$
 
 Hence, the general solution of (1) is
@@ -84,6 +100,7 @@
 y_{1}(x) & =1-\frac{n(n+1)}{2!} x^{2}+\frac{(n-2) n(n+1)(n+3)}{4!} x^{4} \\
 & -\frac{(n-4)(n-2) n(n+1)(n+3)(n+5)}{6!} x^{6}+\cdots
 \end{aligned}
+\tag{3}
 $$
 
 and
@@ -93,30 +110,35 @@
 y_{2}(x) & =x-\frac{(n-1)(n+2)}{3!} x^{3}+\frac{(n-3)(n-1)(n+2)(n+4)}{5!} x^{5} \\
 & -\frac{(n-5)(n-3)(n-1)(n+2)(n+4)(n+6)}{7!} x^{7}+\cdots
 \end{aligned}
+\tag{4}
 $$
 
 If $n$ is an even integer, then, from (2), we have that $a_{n+2}=0$, and hence $a_{n+4}=a_{n+6}=\cdots=0$. Thus (3) reduces to a polynomial of even degree $n$ containing only even powers of $x$ :
 
 $$
 y_{1}=a_{0}+a_{2} x^{2}+\cdots+a_{n} x^{n} \quad(n \text { even }) .
+\tag{5}
 $$
 
 Similarly, if $n$ is an odd integer, then (4) reduces to a polynomial of odd degree $n$ containing only odd powers of $x$ :
 
 $$
 y_{2}=a_{1} x+a_{3} x^{3}+\cdots+a_{n} x^{n} \quad(n \text { odd }) .
+\tag{6}
 $$
 
 Thus far the solutions are determined up to an arbitrary constant. It is customary to normalize the polynomial solution by taking
 
 $$
 a_{n}=\frac{(2 n)!}{2^{n}(n!)^{2}}
+\tag{7}
 $$
 
 To compute the remaining coefficients we need a backward recurrence relation that takes us from $a_{m}$ to $a_{m-2}$. For that purpose, express $a_{m}$ in terms of $a_{m+2}$ in (2), and then replace $m$ by $m-2$ to get
 
 $$
 a_{m-2}=-\frac{m(m-1)}{(n-m+2)(n+m-1)} a_{m} .
+\tag{8}
 $$
 
 We compute $a_{n-2}$ from $a_{n}$ using (7) and (8):
@@ -137,11 +159,14 @@
 a_{n-2 m}=(-1)^{m} \frac{(2 n-2 m)!}{2^{n} m!(n-m)!(n-2 m)!} .
 $$
 
-With these coefficients the polynomial solution is called the Legendre polynomial of degree $n$ and is denoted by $P_{n}(x)$. Setting $M=n / 2$ if $n$ is even or $(n-1) / 2$ if $n$ is odd, the $n$th Legendre polynomial becomes
-
-$$
-P_{n}(x)=\frac{1}{2^{n}} \sum_{m=0}^{M}(-1)^{m} \frac{(2 n-2 m)!}{m!(n-m)!(n-2 m)!} x^{n-2 m} .
-$$
+> [!definition|e429f6d7-0540-5e28-9e61-221696326ae9.local at=41c415fa-9568-515f-b55a-fd8b0d556215] Legendre polynomial with the normalization at one
+> For a nonnegative integer $n$, the polynomial solution of $(1-x^2)y^{\prime\prime}-2xy^{\prime}+n(n+1)y=0$, normalized by $P_n(1)=1$, is called the Legendre polynomial of degree $n$ and is denoted by $P_{n}(x)$. Setting $M=n / 2$ if $n$ is even or $(n-1) / 2$ if $n$ is odd, the $n$th Legendre polynomial becomes
+>
+> $$
+> P_{n}(x)=\frac{1}{2^{n}} \sum_{m=0}^{M}(-1)^{m} \frac{(2 n-2 m)!}{m!(n-m)!(n-2 m)!} x^{n-2 m} .
+> $$
+
+*Printed equation label: (9).*
 
 The first few Legendre polynomials are (see Figure 2)
 
@@ -154,10 +179,21 @@
 \end{array}
 $$
 
-Figure 2 Legendre polynomials.
-![](./images/122e2a0e-ba5b-4934-9af1-dcd4ea360903-35_480_551_998_587.jpg)
-
-![](./images/122e2a0e-ba5b-4934-9af1-dcd4ea360903-35_471_557_1005_1214.jpg)
+```scientific-figure
+id: 33a2ae0e-07f7-4f6f-8eda-8875ca0037b0
+numbered: false
+title: ""
+caption: Figure 2 Legendre polynomials.
+captionVisible: true
+captionPosition: below
+columns: 2
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 13 Partial Differential Equations in Spherical Coordinates/images/122e2a0e-ba5b-4934-9af1-dcd4ea360903-35_480_551_998_587.jpg
+    caption: ""
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 13 Partial Differential Equations in Spherical Coordinates/images/122e2a0e-ba5b-4934-9af1-dcd4ea360903-35_471_557_1005_1214.jpg
+    caption: ""
+```
+
 
 ## Summary and Further Properties
 
@@ -165,206 +201,356 @@
 
 $$
 \left(1-x^{2}\right) y^{\prime \prime}-2 x y^{\prime}+n(n+1) y=0, \quad-1<x<1,
+\tag{10}
 $$
 
 has two linearly independent solutions $y_{1}$ and $y_{2}$ given by (3) and (4). One of them is a polynomial of degree $n$ and the other one is an infinite series solution. If we normalize the polynomial solution by (7), we obtain the Legendre polynomial of degree $n, P_{n}(x)$, given by (9). The other solution of (10), when suitably normalized, is denoted by $Q_{n}(x)$ and is called a Legendre function of the second kind. It converges on the interval $-1<x<1$ and is not bounded in $[-1,1]$ (see Exercises 23-27). Since $P_{n}$ is not identically 0 and bounded in $[-1,1]$ and $Q_{n}$ is not bounded, it follows that $P_{n}$
-and $Q_{n}$ are linearly independent. Hence the general solution of Legendre's equation of order $n$ is
-
-$$
-y(x)=c_{1} P_{n}(x)+c_{2} Q_{n}(x)
-$$
-
-where $c_{1}$ and $c_{2}$ are arbitrary constants.
-
-## EXAMPLE 1 Solution of Legendre's differential equation
-
-Find the general solution of the differential equation
-
-$$
-\left(1-x^{2}\right) y^{\prime \prime}-2 x y^{\prime}+12 y=0 .
-$$
-
-Solution This is Legendre's equation with $n=3$. From (11) the general solution is $y(x)=c_{1} P_{3}(x)+c_{2} Q_{3}(x)$. Since $n$ is odd, the infinite series solution $Q_{3}(x)$ is thus given by ( 3 ), up to normalization. We have
-
-$$
-y=c_{1}\left(\frac{1}{2}\left[5 x^{3}-3 x\right]\right)+c_{2}\left(1-6 x^{2}+3 x^{4}+\frac{4}{5} x^{6}-\cdots\right)
-$$
-
-## EXAMPLE 2 An initial value problem
-
-Without deriving the solution, determine whether the initial value problem
-
-$$
-\left(1-x^{2}\right) y^{\prime \prime}-2 x y^{\prime}+6 y=0 ; \quad y(0)=1, y^{\prime}(0)=1
-$$
-
-has a bounded solution in the interval $[-1,1]$.
-Solution We recognize the differential equation as a Legendre's equation with $n=2$. The only way to get a bounded solution from the general solution (11) is to take $c_{2}=0$. In this case, the solution is a constant multiple of $P_{2}(x)$, and so it is of the form $y_{1}(x)=c_{1} P_{2}(x)=a_{0}+a_{2} x^{2}$. It is easy to see that the second initial condition cannot be satisfied by any polynomial of this form, since $y_{1}^{\prime}=2 a_{2} x$, and so $y_{1}^{\prime}(0)=0$. Hence the initial value problem does not have a bounded solution. The solution must be an infinite series. To find the coefficients of this series, start with $a_{0}=1$ and $a_{1}=1$, and generate the rest using (2) with $n=2$.
+and $Q_{n}$ are linearly independent.
+
+> [!equation|b18296d0-620e-5825-a4de-838c8ec5f642.local at=ab1df737-5909-567a-863a-e8af3166a93f] General solution of Legendre’s equation of integer degree
+> Hence the general solution of Legendre's equation $(1-x^2)y^{\prime\prime}-2xy^{\prime}+n(n+1)y=0$ of order $n\ge0$ on $-1<x<1$ is
+>
+> $$
+> y(x)=c_{1} P_{n}(x)+c_{2} Q_{n}(x)
+> $$
+>
+> where $c_{1}$ and $c_{2}$ are arbitrary constants.
+>
+> Here $P_n$ is the Legendre polynomial normalized by $P_n(1)=1$. The function $Q_n$ is the Legendre function of the second kind.
+
+*Printed equation label: (11).*
+
+> [!exercise|2128b88b-f5d8-5afe-9136-5c8c4265e0b7.local at=63527c58-58a8-5d7f-a05e-3bde5536a7a8] EXAMPLE 1 Solution of Legendre's differential equation
+> Find the general solution of the differential equation
+>
+> $$
+> \left(1-x^{2}\right) y^{\prime \prime}-2 x y^{\prime}+12 y=0 .
+> $$
+
+##### solution
+
+This is Legendre's equation with $n=3$. From (11) the general solution is $y(x)=c_{1} P_{3}(x)+c_{2} Q_{3}(x)$. Since $n$ is odd, the infinite series solution $Q_{3}(x)$ is thus given by ( 3 ), up to normalization. We have
+
+$$
+y=c_{1}\left(\frac{1}{2}\left[5 x^{3}-3 x\right]\right)+c_{2}\left(1-6 x^{2}+3 x^{4}+\frac{4}{5} x^{6}+\cdots\right)
+$$
+
+> [!exercise|efa13cb1-3b16-50f7-85a1-65f9c047f364.local at=0b2f04cc-e31f-5938-b1ac-f009e3b42686] EXAMPLE 2 An initial value problem
+> Without deriving the solution, determine whether the initial value problem
+>
+> $$
+> \left(1-x^{2}\right) y^{\prime \prime}-2 x y^{\prime}+6 y=0 ; \quad y(0)=1, y^{\prime}(0)=1
+> $$
+>
+> has a bounded solution in the interval $[-1,1]$.
+
+##### solution
+
+We recognize the differential equation as a Legendre's equation with $n=2$. The only way to get a bounded solution from the general solution (11) is to take $c_{2}=0$. In this case, the solution is a constant multiple of $P_{2}(x)$, and so it is of the form $y_{1}(x)=c_{1} P_{2}(x)=a_{0}+a_{2} x^{2}$. It is easy to see that the second initial condition cannot be satisfied by any polynomial of this form, since $y_{1}^{\prime}=2 a_{2} x$, and so $y_{1}^{\prime}(0)=0$. Hence the initial value problem does not have a bounded solution. The solution must be an infinite series. To find the coefficients of this series, start with $a_{0}=1$ and $a_{1}=1$, and generate the rest using (2) with $n=2$.
 
 The graphs in Figure 2 illustrate many interesting properties of the Legendre polynomials. We list some of them for ease of reference. Their proofs are left as exercises or provided in the next section.
 
-## FURTHER PROPERTIES OF LEGENDRE POLYNOMIALS
-
-$P_{n}$ is even if $n$ is even and odd if $n$ is odd. $P_{n}(1)=1$ and $P_{n}(-1)=(-1)^{n}$ for all $n$.
-$\left|P_{n}(x)\right| \leq 1$ for all $n$ and all $x$ in $[-1,1]$. $P_{n}(x)$ has $n$ distinct zeros in $[-1,1]$. All relative maxima and minima of $P_{n}$ occur in $[-1,1]$.
+> [!property|82caf074-b664-5cfc-ae3f-b233b751fd0d.local at=0a04882c-d6f2-52b0-93ba-d9f678235427] Further Properties of Legendre Polynomials
+> $P_{n}$ is even if $n$ is even and odd if $n$ is odd. $P_{n}(1)=1$ and $P_{n}(-1)=(-1)^{n}$ for all $n$.
+> $\left|P_{n}(x)\right| \leq 1$ for all $n$ and all $x$ in $[-1,1]$. $P_{n}(x)$ has $n$ distinct zeros in $[-1,1]$. For $n\ge1$, all relative maxima and minima of $P_{n}$ occur in $[-1,1]$.
+>
+> Here $P_n$ is the Legendre polynomial normalized by $P_n(1)=1$.
+
+*Printed equation labels: (12) parity; (13) endpoint values; (14) absolute-value bound; (15) distinct zeros; (16) location of extrema.*
 
 In a sense, these properties say that the interesting behavior of the polynomials $P_{n}$ occurs in the interval $[-1,1]$.
 
-## Exercises 5.5
-
-1. Use (9) to derive (a) $P_{0}(x), P_{1}(x), P_{2}(x)$;
-(b) $P_{3}(x), P_{4}(x)$
-2. Use (9) to prove the following: (a) establish (12);
-(b) $P_{2 n}(0)=(-1)^{n} \frac{(2 n)!}{2^{2 n}(n!)^{2}}$, and $P_{2 n+1}(0)=0$;
-(c) $P_{2 n}^{\prime}(0)=0$, and $P_{2 n+1}^{\prime}(0)=(2 n+1) P_{2 n}(0)$.
-3. Use Exercise 2(b) to obtain the following useful identity for $n=0,1,2, \ldots$ :
-
-$$
-P_{2 n}(0)-P_{2 n+2}(0)=(-1)^{n} \frac{(2 n)!(4 n+3)}{2^{2 n+1}(n!)^{2}(n+1)} .
-$$
-
-4. Verify the following assertions for the first three Legendre polynomials.
-(a) The Legendre polynomial of degree $n$ is a solution of Legendre's differential equation of order $n$.
-(b) $P_{n}(1)=1, P_{n}(-1)=(-1)^{n}$.
-
-Evaluate the following integrals.
-5. $\int_{-1}^{1} P_{3}(x) d x$.
-6. $\int_{-1}^{1} P_{2}(x) P_{3}(x) d x$.
-7. $\int_{0}^{1} P_{2}(x) d x$.
-8. $\int_{-1}^{1} P_{2}^{2}(x) d x$.
-
-In Exercises 9-12, find the general solution of the given differential equation. Write down at least two terms from the series expansions of each part of your answer.
-9. $\left(1-x^{2}\right) y^{\prime \prime}-2 x y^{\prime}+30 y=0$.
-10. $\left(1-x^{2}\right) y^{\prime \prime}-2 x y^{\prime}+42 y=0$.
-11. $\left(1-x^{2}\right) y^{\prime \prime}-2 x y^{\prime}=0$.
-12. $y^{\prime \prime}-\frac{2 x}{\left(1-x^{2}\right)} y^{\prime}+\frac{6}{\left(1-x^{2}\right)} y=0$.
-
-In Exercises 13-16, without solving, decide whether the initial value problem has a bounded solution in $[-1,1]$. Find the solution if it is bounded.
-13. $\left(1-x^{2}\right) y^{\prime \prime}-2 x y^{\prime}+6 y=0 ; y(0)=0, y^{\prime}(0)=1$.
-14. $\left(1-x^{2}\right) y^{\prime \prime}-2 x y^{\prime}+56 y=0 ; y(0)=0, y^{\prime}(0)=1$.
-15. $\left(1-x^{2}\right) y^{\prime \prime}-2 x y^{\prime}+56 y=0 ; y(0)=1, y^{\prime}(0)=0$.
-16. $\left(1-x^{2}\right) y^{\prime \prime}-2 x y^{\prime}+110 y=0 ; y(0)=1, y^{\prime}(0)=1$.
-
-In Exercises 17-20, with the help of (2), determine the first four nonzero terms of the series solution of the given initial value problem.
-17. $\left(1-x^{2}\right) y^{\prime \prime}-2 x y^{\prime}+\frac{3}{4} y=0 ; y(0)=1, y^{\prime}(0)=1$.
-18. $\left(1-x^{2}\right) y^{\prime \prime}-2 x y^{\prime}+2 y=0 ; y(0)=1, y^{\prime}(0)=0$.
-19. $\left(1-x^{2}\right) y^{\prime \prime}-2 x y^{\prime}+3 y=0 ; y(0)=0, y^{\prime}(0)=1$.
-20. $\left(1-x^{2}\right) y^{\prime \prime}-2 x y^{\prime}+2 y=0 ; y(0)=1, y^{\prime}(0)=1$.
-21. Consider a Legendre function (solution of Legendre's differential equation) that is not a polynomial. Use the ratio test and the recurrence formula for the coefficients to show that the radius of convergence of the Legendre function is 1 .
-
-![](./images/122e2a0e-ba5b-4934-9af1-dcd4ea360903-38_439_483_1073_61.jpg)
-Figure 3 Legendre functions $Q_{2}(x)$ and $Q_{3}(x)$.
-
-Project Problem: Legendre functions of the second kind. Do Exercise 22 and any one of 23 or 24 .
-22. (a) Use the reduction of order formula (Appendix A.3) to derive the following formula for the Legendre functions of the second kind:
-
-$$
-Q_{n}(x)=P_{n}(x) \int \frac{1}{\left[P_{n}(x)\right]^{2}\left(1-x^{2}\right)} d x \quad(n=0,1,2, \ldots)
-$$
-
-(The integral is defined up to an arbitrary constant.)
-(b) Compute the Wronskian $W\left(P_{n}(x), Q_{n}(x)\right)$ and show that it vanishes nowhere on $-1<x<1$. Conclude that the two solutions are linearly independent.
-
-Use the formula in Exercise 22 to derive the given expression for the Legendre function of the second kind.
-23. $Q_{0}(x)=\frac{1}{2} \ln \left(\frac{1+x}{1-x}\right)$.
-24. $Q_{1}(x)=-1+\frac{x}{2} \ln \left(\frac{1+x}{1-x}\right)$.
-25. Project Problem: Legendre functions of the second kind are not bounded. The purpose of this problem is to derive the following formula for the Legendre functions of the second kind: for $n=0,1,2, \ldots$,
-
-$$
-Q_{n}(x)=\frac{1}{2} P_{n}(x) \ln \left(\frac{1+x}{1-x}\right)+f_{n}(x)
-$$
-
-where $f_{n}(x)$ is a polynomial of degree $n-1$ for $n \geq 1$ and $f_{0}(x)=0$.
-(a) Before we derive the formula, use it to show that $\left|Q_{n}(x)\right| \rightarrow \infty$ if $x \rightarrow \pm 1$; and thus $Q_{n}(x)$ is not bounded in $[-1,1]$.
-(b) Verify the formula for $n=0$ and 1, using the results of Exercises 23 and 24.
-(c) For $n \geq 2$, let $u(x)=\frac{1}{2} \ln \left(\frac{1+x}{1-x}\right), v(x)=u(x) P_{n}(x)$, and $\alpha_{n}=n(n+1)$. Show that $\left(\left(1-x^{2}\right) u^{\prime}(x)\right)^{\prime}=0$; equivalently, $\left(1-x^{2}\right) u^{\prime \prime}(x)-2 x u^{\prime}(x)=0$.
-(d) Plug $v(x)=u(x) P_{n}(x)$ into Legendre's equation of order $n$ and show that
-
-$$
-\left(1-x^{2}\right) v^{\prime \prime}-2 x v^{\prime}+\alpha_{n} v=2 P_{n}^{\prime}(x)
-$$
-
-[Hint: Use (c) and the fact that $P_{n}$ is a solution of Legendre's equation of order $n$.]
-(e) Let $f_{n}(x)$ denote a particular solution of the differential equation
-
-$$
-\left(1-x^{2}\right) y^{\prime \prime}-2 x y^{\prime}+\alpha_{n} y=-2 P_{n}^{\prime}(x)
-$$
-
-Show that $f_{n}$ can be chosen to be a polynomial of degree $n-1$. [Hint: If $y$ is a polynomial of degree $n-1$, then $\left(1-x^{2}\right) y^{\prime \prime}-2 x y^{\prime}+\alpha_{n} y$ is also a polynomial of degree $n-1$.]
-(f) Use (d) and (e) to show that $v(x)+f_{n}(x)$ is a solution of Legendre's equation of order $n$.
-(g) Show that $v(x)+f_{n}(x)$ is not bounded on $[-1,1]$ and conclude that it is a second solution of Legendre's equation, which is independent of $P_{n}(x)$. We can take $Q_{n}(x)=v(x)+f_{n}(x)$.
-26. Follow the steps in Exercise 25 and derive the Legendre function (Figure 3)
-
-$$
-Q_{2}(x)=-\frac{3}{2} x+\frac{1}{4}\left(-1+3 x^{2}\right) \ln \left(\frac{1+x}{1-x}\right)
-$$
-
-27. Follow the steps in Exercise 25 and derive the Legendre function (Figure 3)
-
-$$
-Q_{3}(x)=\frac{1}{6}\left(4-15 x^{2}\right)+\frac{1}{4}\left(-3 x+5 x^{3}\right) \ln \left(\frac{1+x}{1-x}\right)
-$$
-
-The formula
-
-$$
-P_{n}(x)=\frac{1}{\pi} \int_{0}^{\pi}\left(x+i \sqrt{1-x^{2}} \cos \theta\right)^{n} d \theta \quad(n=0,1,2, \ldots)
-$$
-
-is known as Laplace's integral formula for the Legendre polynomials. Here $i$ denotes as usual the complex number such that $(i)^{2}=-1$. This formula has many interesting applications that we explore in the following exercises. For a proof, see [1], Section 10.5.
-28. Derive the first three Legendre polynomials using (17).
-29. (a) Show that for $|x| \leq 1$, we have
-
-$$
-\left|\left(x+i \sqrt{1-x^{2}} \cos \theta\right)^{n}\right| \leq 1 .
-$$
-
-[Hint: If $\alpha+i \beta$ is a complex number, then $|\alpha+i \beta|=\sqrt{\alpha^{2}+\beta^{2}}$.]
-(b) Use (17) and (a) to establish (14).
-30. (a) Use (17) to establish (13).
-(b) Use (17) and Exercise 42, Section 4.7 (Wallis's formulas) to compute $P_{n}(0)$.
-31. Project Problem: Generating function for the Legendre polynomials. Recall that if $\alpha$ is any real number and $k$ is a nonnegative integer, the $k$ th binomial coefficient is
-
-$$
-\binom{\alpha}{k}=\frac{\alpha(\alpha-1)(\alpha-2) \ldots(\alpha-k+1)}{k!} \quad \text { for } k \geq 1
-$$
-
-and $\binom{\alpha}{0}=1$. With this notation, the binomial theorem asserts that
-
-$$
-(1+x)^{\alpha}=\sum_{k=0}^{\infty}\binom{\alpha}{k} x^{k}, \quad-1<x<1 .
-$$
-
-(a) Set $\alpha=-\frac{1}{2}$, and obtain that
-
-$$
-\frac{1}{\sqrt{1+v}}=\sum_{k=0}^{\infty}(-1)^{k} \frac{(2 k)!}{2^{2 k}(k!)^{2}} v^{k}, \quad|v|<1
-$$
-
-(b) Conclude that
-
-$$
-\frac{1}{\sqrt{1-2 x u+u^{2}}}=\sum_{n=0}^{\infty} P_{n}(x) u^{n}, \quad|x| \leq 1,|u|<1
-$$
-
-This is called the generating function for the Legendre polynomials. To prove it, set $v=-2 x u+u^{2}$ in (a), expand, and collect like powers of $u$. Note that
-since $\left|P_{n}(x)\right| \leq 1$ for $|x| \leq 1$ (Exercise 29), the series is convergent for all the given values of $x$ and $u$.
-31. A three-mass problem. Consider three masses in a plane $m_{1}, m_{2}$, and $m_{3}$, located at the points $O, P$, and $Q$, respectively (Figure 4). According to Newton's law of gravitation, the magnitude of the attractive force between two masses is inversely proportional to their distance. Thus the magnitude of the force between $m_{1}$ and $m_{3}$ is $F_{1}=\frac{G m_{1} m_{3}}{r^{2}}$, where $G$ is the gravitational constant and $r=|O Q|$.
-
-![](./images/122e2a0e-ba5b-4934-9af1-dcd4ea360903-40_258_468_497_50.jpg)
-Figure 4 Three masses.
-
-The force between $m_{2}$ and $m_{3}$ has a similar expression in terms of $\rho$. To express this force as a function of $r$, use the law of cosines in a triangle to show that $\rho^{2}=1+r^{2}-2 r \cos \alpha$, and obtain
-
-$$
-F_{2}=\frac{G m_{2} m_{3}}{1+r^{2}-2 r \cos \alpha}
-$$
-
-In terms of potential function for the mass $m_{2}$, we find that the potential of $m_{2}$ is
-
-$$
-\frac{G m_{2}}{\rho}=\frac{G m_{2}}{\sqrt{1+r^{2}-2 r \cos \alpha}}
-$$
-
-Replacing $r$ by $u$ and letting $\cos \alpha=x$, we see that, up to a constant multiple, this potential is the generating function for the Legendre polynomials.
+## Exercises 13.5
+
+
+> [!exercise|a2a63b3f-105e-5cdb-9775-a1762a1b256f.local at=5c19da74-9009-5e36-80e8-a1951ec9da08] Exercise 1
+> Use (9) to derive (a) $P_{0}(x), P_{1}(x), P_{2}(x)$;
+> (b) $P_{3}(x), P_{4}(x)$
+
+
+> [!exercise|a0482386-9308-5f52-9776-e1a83de550b3.local at=fd2aabd4-c3ba-58fb-a552-261c3ac84df0] Exercise 2
+> Use (9) to prove the following: (a) establish (12);
+> (b) $P_{2 n}(0)=(-1)^{n} \frac{(2 n)!}{2^{2 n}(n!)^{2}}$, and $P_{2 n+1}(0)=0$;
+> (c) $P_{2 n}^{\prime}(0)=0$, and $P_{2 n+1}^{\prime}(0)=(2 n+1) P_{2 n}(0)$.
+
+
+> [!exercise|10e9d981-6ca2-5d85-bad3-462cfddbde61.local at=7e88f33e-0755-546e-89ea-4f77fb9325d5] Exercise 3
+> Use Exercise 2(b) to obtain the following useful identity for $n=0,1,2, \ldots$ :
+>
+> $$
+> P_{2 n}(0)-P_{2 n+2}(0)=(-1)^{n} \frac{(2 n)!(4 n+3)}{2^{2 n+1}(n!)^{2}(n+1)} .
+> $$
+
+
+> [!exercise|bd2441a7-f116-599f-9821-89b1a4ca2eec.local at=3d7eec05-17c3-50ec-95d4-9a87b2b2d6b4] Exercise 4
+> Verify the following assertions for the first three Legendre polynomials.
+> (a) The Legendre polynomial of degree $n$ is a solution of Legendre's differential equation of order $n$.
+> (b) $P_{n}(1)=1, P_{n}(-1)=(-1)^{n}$.
+
+
+> [!prompt|63ee292c-e9a3-5375-bc78-6f6a4d57e02d.local at=c3de49ee-d5ef-55cd-a64f-0c2a2fa037d8] Shared exercise instructions
+> Evaluate the following integrals.
+
+
+> [!exercise|976cbd84-989c-5435-bd9a-377fb8466b29.local at=89bf6d6b-ce9a-502f-b4d3-b620fe813a3f] Exercise 5
+> $\int_{-1}^{1} P_{3}(x) d x$.
+
+
+> [!exercise|47df815d-a5f8-5be8-b4f1-c521a16bc3fb.local at=df1d89f8-8ef4-577b-819a-9587c6c0bbe2] Exercise 6
+> $\int_{-1}^{1} P_{2}(x) P_{3}(x) d x$.
+
+
+> [!exercise|046cdcad-66e4-51b5-9798-af67dcc2cbc6.local at=d7363423-1b95-5686-92c5-8daa96abfabb] Exercise 7
+> $\int_{0}^{1} P_{2}(x) d x$.
+
+
+> [!exercise|5219e67f-83f1-5c32-a4cc-0253d8adc94a.local at=cf82b086-5e8b-54e1-aed1-a072e258daaf] Exercise 8
+> $\int_{-1}^{1} P_{2}^{2}(x) d x$.
+
+
+> [!prompt|af9dd184-932d-56c7-bbfa-e6696ebc16e7.local at=fcd7dfe8-0af1-55da-bd7f-d158f8b9ac06] Shared exercise instructions
+> In Exercises 9-12, find the general solution of the given differential equation. Write down at least two terms from the series expansions of each part of your answer.
+
+
+> [!exercise|b16b864c-6eac-54de-a53c-f2c60bc57bd0.local at=8f459ff8-70e6-5821-8f4e-d87a65892a52] Exercise 9
+> $\left(1-x^{2}\right) y^{\prime \prime}-2 x y^{\prime}+30 y=0$.
+
+
+> [!exercise|0f4ecf80-a971-5856-922e-e430bcadafcd.local at=24e74cb3-f00f-59c5-b661-8c746997c7be] Exercise 10
+> $\left(1-x^{2}\right) y^{\prime \prime}-2 x y^{\prime}+42 y=0$.
+
+
+> [!exercise|1820213f-204a-53de-88d2-9feee6df9bc9.local at=a4e07077-e723-5629-b209-6c1f77393865] Exercise 11
+> $\left(1-x^{2}\right) y^{\prime \prime}-2 x y^{\prime}=0$.
+
+
+> [!exercise|fc14556e-19d1-5081-a1d4-5d7b06e96bd3.local at=05a46eae-c704-5c07-b2e1-f3c050a162d5] Exercise 12
+> $y^{\prime \prime}-\frac{2 x}{\left(1-x^{2}\right)} y^{\prime}+\frac{6}{\left(1-x^{2}\right)} y=0$.
+
+
+> [!prompt|e76ac358-330b-5ffb-bad7-66183aacd8ff.local at=0185ab09-e319-5d2e-9590-35ec062b4800] Shared exercise instructions
+> In Exercises 13-16, without solving, decide whether the initial value problem has a bounded solution in $[-1,1]$. Find the solution if it is bounded.
+
+
+> [!exercise|00d1d830-4541-5940-a160-806f138a3612.local at=c7a5113d-0d2e-560e-b686-194e14863ddc] Exercise 13
+> $\left(1-x^{2}\right) y^{\prime \prime}-2 x y^{\prime}+6 y=0 ; y(0)=0, y^{\prime}(0)=1$.
+
+
+> [!exercise|4a1b2738-3cea-5143-93d4-a3d95688ccdd.local at=4abdee99-d5f9-5825-9297-0f0918f96d54] Exercise 14
+> $\left(1-x^{2}\right) y^{\prime \prime}-2 x y^{\prime}+56 y=0 ; y(0)=0, y^{\prime}(0)=1$.
+
+
+> [!exercise|64eb696c-2f2e-5a23-923a-d8c8510008ab.local at=c984464f-a97b-5092-841a-ccf92d7a4892] Exercise 15
+> $\left(1-x^{2}\right) y^{\prime \prime}-2 x y^{\prime}+56 y=0 ; y(0)=1, y^{\prime}(0)=0$.
+
+
+> [!exercise|626dbcbd-76d5-5675-83ba-b7aada4eb013.local at=e25723f9-6356-5fa9-a90d-5825331be123] Exercise 16
+> $\left(1-x^{2}\right) y^{\prime \prime}-2 x y^{\prime}+110 y=0 ; y(0)=1, y^{\prime}(0)=1$.
+
+
+> [!prompt|7cc85101-f58c-5a58-a15a-5b2fc96a12b1.local at=b9cc2749-8790-5bc9-b2cb-235cfc5d9e0c] Shared exercise instructions
+> In Exercises 17-20, with the help of (2), determine the first four nonzero terms of the series solution of the given initial value problem.
+
+
+> [!exercise|79df8f23-7c13-5223-8f98-68bc0b0e3b20.local at=c282be6f-7596-5eeb-9545-2980871520f3] Exercise 17
+> $\left(1-x^{2}\right) y^{\prime \prime}-2 x y^{\prime}+\frac{3}{4} y=0 ; y(0)=1, y^{\prime}(0)=1$.
+
+
+> [!exercise|22ee1c71-a16e-5a74-8172-eb8deb6c05f2.local at=04ae9815-903f-5cac-84df-863cfc1c1bcd] Exercise 18
+> $\left(1-x^{2}\right) y^{\prime \prime}-2 x y^{\prime}+2 y=0 ; y(0)=1, y^{\prime}(0)=0$.
+
+
+> [!exercise|e22328af-1d3e-51e0-a365-c2925412716c.local at=045f6c15-211a-52f4-a311-ad2015149e13] Exercise 19
+> $\left(1-x^{2}\right) y^{\prime \prime}-2 x y^{\prime}+3 y=0 ; y(0)=0, y^{\prime}(0)=1$.
+
+
+> [!exercise|efd88ec7-a836-5bad-8b50-fddb4cfab700.local at=9bdbbb1d-44fc-51d5-98ca-3890bc3107e9] Exercise 20
+> $\left(1-x^{2}\right) y^{\prime \prime}-2 x y^{\prime}+2 y=0 ; y(0)=1, y^{\prime}(0)=1$.
+
+
+> [!exercise|cdea774e-dc0d-5695-9e1e-0c6180d7faa4.local at=182ab903-ed15-5309-ac11-f8f8a3630353] Exercise 21
+> Consider a Legendre function (solution of Legendre's differential equation) that is not a polynomial. Use the ratio test and the recurrence formula for the coefficients to show that the radius of convergence of the Legendre function is 1 .
+
+
+> [!prompt|82ffe710-7be6-5a4d-9acd-642717c02f67.local at=741e9a49-b3af-58e3-a04a-d22fe50ddfad] Shared exercise instructions
+> Project Problem: Legendre functions of the second kind. Do Exercise 22 and any one of 23 or 24 .
+
+
+> [!exercise|f6002614-ac0f-5bfe-a52b-b4f5d8eb9994.local at=1c885873-4dc1-5c76-b151-f1a375157540] Exercise 22
+> (a) Use the reduction of order formula (Section 10.3) to derive the following formula for the Legendre functions of the second kind:
+>
+> $$
+> Q_{n}(x)=P_{n}(x) \int \frac{1}{\left[P_{n}(x)\right]^{2}\left(1-x^{2}\right)} d x \quad(n=0,1,2, \ldots)
+> $$
+>
+> (Initially use an interval where $P_n\ne0$ and then continue the solution across its zeros. The integration constant adds a multiple of $P_n$; the usual normalization fixes that freedom.)
+> (b) Compute the Wronskian $W\left(P_{n}(x), Q_{n}(x)\right)$ and show that it vanishes nowhere on $-1<x<1$. Conclude that the two solutions are linearly independent.
+
+
+> [!prompt|02de773f-8c23-5b20-a8b7-b14ce9be0044.local at=81b6998b-b83a-5fd5-98e4-7c0aead05b8f] Shared exercise instructions
+> Use the formula in Exercise 22 to derive the given expression for the Legendre function of the second kind.
+
+
+> [!exercise|183e850b-d365-5e96-a48d-66aaa8fef586.local at=5a94fedb-370f-5f1e-8ec9-0664a9f46358] Exercise 23
+> $Q_{0}(x)=\frac{1}{2} \ln \left(\frac{1+x}{1-x}\right)$.
+
+
+> [!exercise|2e65280a-0d41-5c20-bf1e-92cbb9e43ec1.local at=5fcaa541-63f0-557c-b5c6-4299eb727978] Exercise 24
+> $Q_{1}(x)=-1+\frac{x}{2} \ln \left(\frac{1+x}{1-x}\right)$.
+
+
+> [!exercise|8d03ad65-ca2c-5d18-9d7d-78e048dce508.local at=3fad53fb-b468-50ed-a85a-8203161a38b2] Exercise 25
+> Project Problem: Legendre functions of the second kind are not bounded. The purpose of this problem is to derive the following formula for the Legendre functions of the second kind: for $n=0,1,2, \ldots$,
+>
+> $$
+> Q_{n}(x)=\frac{1}{2} P_{n}(x) \ln \left(\frac{1+x}{1-x}\right)+f_{n}(x)
+> $$
+>
+> where $f_{n}(x)$ is a polynomial of degree $n-1$ for $n \geq 1$ and $f_{0}(x)=0$.
+> (a) Before we derive the formula, use it to show that $\left|Q_{n}(x)\right| \rightarrow \infty$ if $x \rightarrow \pm 1$; and thus $Q_{n}(x)$ is not bounded in $[-1,1]$.
+> (b) Verify the formula for $n=0$ and 1, using the results of Exercises 23 and 24.
+> (c) For $n \geq 2$, let $u(x)=\frac{1}{2} \ln \left(\frac{1+x}{1-x}\right), v(x)=u(x) P_{n}(x)$, and $\alpha_{n}=n(n+1)$. Show that $\left(\left(1-x^{2}\right) u^{\prime}(x)\right)^{\prime}=0$; equivalently, $\left(1-x^{2}\right) u^{\prime \prime}(x)-2 x u^{\prime}(x)=0$.
+> (d) Plug $v(x)=u(x) P_{n}(x)$ into Legendre's equation of order $n$ and show that
+>
+> $$
+> \left(1-x^{2}\right) v^{\prime \prime}-2 x v^{\prime}+\alpha_{n} v=2 P_{n}^{\prime}(x)
+> $$
+>
+> [Hint: Use (c) and the fact that $P_{n}$ is a solution of Legendre's equation of order $n$.]
+> (e) Let $f_{n}(x)$ denote a particular solution of the differential equation
+>
+> $$
+> \left(1-x^{2}\right) y^{\prime \prime}-2 x y^{\prime}+\alpha_{n} y=-2 P_{n}^{\prime}(x)
+> $$
+>
+> Show that $f_{n}$ can be chosen to be a polynomial of degree $n-1$. [Hint: If $y$ is a polynomial of degree $n-1$, then $\left(1-x^{2}\right) y^{\prime \prime}-2 x y^{\prime}+\alpha_{n} y$ is also a polynomial of degree $n-1$.]
+> (f) Use (d) and (e) to show that $v(x)+f_{n}(x)$ is a solution of Legendre's equation of order $n$.
+> (g) Show that $v(x)+f_{n}(x)$ is not bounded on $[-1,1]$ and conclude that it is a second solution of Legendre's equation, which is independent of $P_{n}(x)$. We can take $Q_{n}(x)=v(x)+f_{n}(x)$.
+
+
+> [!exercise|c653bd6e-77ee-5b3b-b5ee-4f74d4285548.local at=b8123445-31d8-57d4-ab20-02f19f098559] Exercise 26
+> Follow the steps in Exercise 25 and derive the Legendre function (Figure 3)
+>
+> $$
+> Q_{2}(x)=-\frac{3}{2} x+\frac{1}{4}\left(-1+3 x^{2}\right) \ln \left(\frac{1+x}{1-x}\right)
+> $$
+
+
+```scientific-figure
+id: 4f93e0d9-912b-408c-a5d6-9698a46b0dcd
+numbered: false
+title: ""
+caption: Figure 3 Legendre functions $Q_{2}(x)$ and $Q_{3}(x)$.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 13 Partial Differential Equations in Spherical Coordinates/images/122e2a0e-ba5b-4934-9af1-dcd4ea360903-38_439_483_1073_61.jpg
+    caption: ""
+```
+
+
+
+
+
+> [!exercise|dcd44d48-2420-59fe-b5ca-f451495bcffe.local at=bacd25bc-3a7f-53ee-9534-b68d28a08b77] Exercise 27
+> Follow the steps in Exercise 25 and derive the Legendre function (Figure 3)
+>
+> $$
+> Q_{3}(x)=\frac{1}{6}\left(4-15 x^{2}\right)+\frac{1}{4}\left(-3 x+5 x^{3}\right) \ln \left(\frac{1+x}{1-x}\right)
+> $$
+
+
+> [!prompt|9f3db64e-f248-576c-9699-7295904b9413.local at=a27dc0e8-e538-5d6b-8d24-cc0585710a37] Shared exercise instructions
+> The formula
+>
+> $$
+> P_{n}(x)=\frac{1}{\pi} \int_{0}^{\pi}\left(x+i \sqrt{1-x^{2}} \cos \theta\right)^{n} d \theta \quad(n=0,1,2, \ldots)
+> $$
+>
+> is known as Laplace's integral formula for the Legendre polynomials. Here $i$ denotes as usual the complex number such that $(i)^{2}=-1$. This formula has many interesting applications that we explore in the following exercises. For a proof, see [1], Section 10.5.
+
+*Printed equation label: (17).*
+
+
+> [!exercise|893fa892-c698-5fe7-bbff-ea6240a4fac5.local at=3071c49a-2d13-513d-ba60-0326d6b2f287] Exercise 28
+> Derive the first three Legendre polynomials using (17).
+
+
+> [!exercise|3a5fcf00-26ce-5f56-b3be-0ffece720f27.local at=85ac2482-a08c-52df-a0d7-27aad65feb15] Exercise 29
+> (a) Show that for $|x| \leq 1$, we have
+>
+> $$
+> \left|\left(x+i \sqrt{1-x^{2}} \cos \theta\right)^{n}\right| \leq 1 .
+> $$
+>
+> [Hint: If $\alpha+i \beta$ is a complex number, then $|\alpha+i \beta|=\sqrt{\alpha^{2}+\beta^{2}}$.]
+> (b) Use (17) and (a) to establish (14).
+
+
+> [!exercise|09efdcc7-6bbb-505c-b5aa-f5564dc5c55f.local at=0dad990c-0014-5613-820c-6e22f88a2569] Exercise 30
+> (a) Use (17) to establish (13).
+> (b) Use (17) and Exercise 42, Section 12.7 (Wallis's formulas) to compute $P_{n}(0)$.
+
+
+> [!exercise|6f3224c4-9f13-5013-8c65-2f1438007509.local at=2c518540-3c68-5ae9-8e94-41862e66fb4b] Exercise 31
+> Project Problem: Generating function for the Legendre polynomials. Recall that if $\alpha$ is any real number and $k$ is a nonnegative integer, the $k$ th binomial coefficient is
+>
+> $$
+> \binom{\alpha}{k}=\frac{\alpha(\alpha-1)(\alpha-2) \ldots(\alpha-k+1)}{k!} \quad \text { for } k \geq 1
+> $$
+>
+> and $\binom{\alpha}{0}=1$. With this notation, the binomial theorem asserts that
+>
+> $$
+> (1+x)^{\alpha}=\sum_{k=0}^{\infty}\binom{\alpha}{k} x^{k}, \quad-1<x<1 .
+> $$
+>
+> (a) Set $\alpha=-\frac{1}{2}$, and obtain that
+>
+> $$
+> \frac{1}{\sqrt{1+v}}=\sum_{k=0}^{\infty}(-1)^{k} \frac{(2 k)!}{2^{2 k}(k!)^{2}} v^{k}, \quad|v|<1
+> $$
+>
+> (b) Conclude that
+>
+> $$
+> \frac{1}{\sqrt{1-2 x u+u^{2}}}=\sum_{n=0}^{\infty} P_{n}(x) u^{n}, \quad|x| \leq 1,|u|<1
+> $$
+>
+> This is called the generating function for the Legendre polynomials. To prove it, set $v=-2 x u+u^{2}$ in (a), expand, and collect like powers of $u$. Note that
+> since $\left|P_{n}(x)\right| \leq 1$ for $|x| \leq 1$ (Exercise 29), the series is convergent for all the given values of $x$ and $u$.
+
+
+> [!exercise|636ff3ac-cda0-5ecb-80a7-2a576b481082.local at=9417c588-a13b-58c7-9e18-09e4ffde08d8] Exercise 32
+> A three-mass problem.  Consider three masses in a plane $m_{1}, m_{2}$, and $m_{3}$, located at the points $O, P$, and $Q$, respectively (Figure 4). According to Newton's law of gravitation, the magnitude of the attractive force between two masses is inversely proportional to the square of their distance. Thus the magnitude of the force between $m_{1}$ and $m_{3}$ is $F_{1}=\frac{G m_{1} m_{3}}{r^{2}}$, where $G$ is the gravitational constant and $r=|O Q|$.
+>
+> The force between $m_{2}$ and $m_{3}$ has a similar expression in terms of $\rho$. To express this force as a function of $r$, use the law of cosines in a triangle to show that $\rho^{2}=1+r^{2}-2 r \cos \alpha$, and obtain
+>
+> $$
+> F_{2}=\frac{G m_{2} m_{3}}{1+r^{2}-2 r \cos \alpha}
+> $$
+>
+> Using the positive potential function whose gradient gives the gravitational acceleration, the potential function for $m_2$ is
+>
+> $$
+> \frac{G m_{2}}{\rho}=\frac{G m_{2}}{\sqrt{1+r^{2}-2 r \cos \alpha}}
+> $$
+>
+> 
+>
+> Replacing $r$ by $u$ and letting $\cos \alpha=x$, we see that, up to a constant multiple, this potential is the generating function for the Legendre polynomials.
+
+
+```scientific-figure
+id: 3a532ca3-ce5a-4778-922b-0f84844fa3d1
+numbered: false
+title: ""
+caption: Figure 4 Three masses.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 13 Partial Differential Equations in Spherical Coordinates/images/122e2a0e-ba5b-4934-9af1-dcd4ea360903-40_258_468_497_50.jpg
+    caption: ""
+```

`````
