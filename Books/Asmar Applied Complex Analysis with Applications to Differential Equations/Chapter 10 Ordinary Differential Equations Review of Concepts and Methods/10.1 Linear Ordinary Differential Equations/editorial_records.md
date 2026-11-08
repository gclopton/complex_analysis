
# Editorial records

Reading note: 10.1 Linear Ordinary Differential Equations.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|cb200824-c353-579a-9ff0-cd179f9d6e12.local at=7d6b0cc2-3654-54e2-9af8-eac5712a0bcd] Superposition of Homogeneous Linear ODE Solutions
> On an interval $I$, consider $L[y]=y^{(n)}+p_{n-1}(x)y^{(n-1)}+\cdots+p_1(x)y^{\prime}+p_0(x)y$, where $n\geq1$ and every coefficient $p_j$ is continuous.
>
> If $L[u]=L[v]=0$, then $L[cu+dv]=0$ for arbitrary constants $c,d$.
````
### After

````text
> [!theorem|cb200824-c353-579a-9ff0-cd179f9d6e12.local at=7d6b0cc2-3654-54e2-9af8-eac5712a0bcd] Superposition Principle
> On an interval $I$, let $L[y]=y^{(n)}+p_{n-1}(x)y^{(n-1)}+\cdots+p_1(x)y^{\prime}+p_0(x)y$, where $n\geq1$ and the coefficients are continuous.
>
> Suppose that $u(x)$ and $v(x)$ are solutions of $L[y]=0$ and let $c$ and $d$ be any two numbers. Then the linear combination $c u(x)+d v(x)$ is also a solution of $L[y]=0$.
````

## 2. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|c4e81fe4-f52b-5477-83a1-df188c8bcf6a.local at=fd3850cc-d23a-5891-a840-635cb32dfc87] General Solution of a Nonhomogeneous Linear ODE
> On an interval $I$, consider $L[y]=y^{(n)}+p_{n-1}(x)y^{(n-1)}+\cdots+p_1(x)y^{\prime}+p_0(x)y$, where $n\geq1$ and every coefficient $p_j$ is continuous.
>
> Let $g$ be continuous on $I$ and let $y_p$ be any particular solution of $L[y]=g$. Every solution has the form $y=y_h+y_p$, where $y_h$ is a solution of $L[y_h]=0$. If $y_1,\ldots,y_n$ is a fundamental set for the homogeneous equation, then $y=\sum_{j=1}^n c_jy_j+y_p$ with arbitrary constants $c_j$.
````
### After

````text
> [!theorem|c4e81fe4-f52b-5477-83a1-df188c8bcf6a.local at=fd3850cc-d23a-5891-a840-635cb32dfc87] General Solution of Nonhomogeneous Equations
> On an interval $I$, let $L[y]=y^{(n)}+p_{n-1}(x)y^{(n-1)}+\cdots+p_1(x)y^{\prime}+p_0(x)y$, where $n\geq1$ and the coefficients are continuous.
>
> Let $g$ be continuous on $I$.
>
> Let $y_{h}$ and $y_{p}$ denote, respectively, the general solution of the homogeneous equation associated with $L[y]=g$ and a particular solution of $L[y]=g$. Then any solution $y$ of $L[y]=g$ has the form
>
> $$
> y=y_{h}+y_{p}
> $$
````

## 3. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|12d47e51-786c-53e9-a14b-1272ed834ece.local at=f9afdc7a-c723-5527-b50e-5a177b36c12a] Existence and Uniqueness for Linear ODE Initial Value Problems
> On an interval $I$, consider $L[y]=y^{(n)}+p_{n-1}(x)y^{(n-1)}+\cdots+p_1(x)y^{\prime}+p_0(x)y$, where $n\geq1$ and every coefficient $p_j$ is continuous.
>
> If $g$ is continuous on $I$, $x_0\in I$, and $b_0,\ldots,b_{n-1}$ are prescribed constants, then $L[y]=g$ has exactly one solution on $I$ satisfying $y^{(j)}(x_0)=b_j$ for $j=0,\ldots,n-1$.
````
### After

````text
> [!theorem|12d47e51-786c-53e9-a14b-1272ed834ece.local at=f9afdc7a-c723-5527-b50e-5a177b36c12a] Existence and Uniqueness for Initial Value Problems
> On an interval $I$, let $L[y]=y^{(n)}+p_{n-1}(x)y^{(n-1)}+\cdots+p_1(x)y^{\prime}+p_0(x)y$, where $n\geq1$ and the coefficients are continuous.
>
> Let $g$ be continuous on $I$.
>
> Consider the initial value problem consisting of the linear differential equation $L[y]=g$ and the initial conditions
>
> $$
> y\left(x_{0}\right)=y_{0}, y^{\prime}\left(x_{0}\right)=y_{0}^{\prime}, \ldots, y^{(n-1)}\left(x_{0}\right)=y_{0}^{(n-1)},
> $$
>
> where $x_{0}$ is in $I$ and $y_{0}, y_{0}^{\prime}, \ldots, y_{0}^{(n-1)}$ are prescribed values. Then this problem has a unique solution $y$ on the interval $I$.
````

## 4. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!definition|18a292cd-fb05-5a7f-8487-87369bb7350e.local at=f610b10d-92a0-5cb5-9fd7-22daf3013e0b] Wronskian of a Finite Family of Functions
> Let $y_{1}, y_{2}, \ldots, y_{n}$ be $n$ functions with derivatives through order $n-1$ on an interval. The Wronskian $W\left(y_{1}, y_{2}, \ldots, y_{n}\right)$ of these functions is given by the following $n \times n$ determinant:
>
> $$
> W\left(y_{1}, y_{2}, \ldots, y_{n}\right)=\left|\begin{array}{cccc}
> y_{1} & y_{2} & \ldots & y_{n} \\
> y_{1}^{\prime} & y_{2}^{\prime} & \ldots & y_{n}^{\prime} \\
> \vdots & \vdots & \vdots & \vdots \\
> y_{1}^{(n-1)} & y_{2}^{(n-1)} & \ldots & y_{n}^{(n-1)}
> \end{array}\right| .
> $$
````
### After

````text
> [!definition|18a292cd-fb05-5a7f-8487-87369bb7350e.local at=f610b10d-92a0-5cb5-9fd7-22daf3013e0b] The Wronskian
> On an interval $I$, let $L[y]=y^{(n)}+p_{n-1}(x)y^{(n-1)}+\cdots+p_1(x)y^{\prime}+p_0(x)y$, where $n\geq1$ and the coefficients are continuous.
>
> Let $y_{1}, y_{2}, \ldots, y_{n}$ be any $n$ solutions to the homogeneous linear differential equation $L[y]=0$. The Wronskian $W\left(y_{1}, y_{2}, \ldots, y_{n}\right)$ of these solutions is given by the following $n \times n$ determinant:
>
> $$
> W\left(y_{1}, y_{2}, \ldots, y_{n}\right)=\left|\begin{array}{cccc}
> y_{1} & y_{2} & \ldots & y_{n} \\
> y_{1}^{\prime} & y_{2}^{\prime} & \ldots & y_{n}^{\prime} \\
> \vdots & \vdots & \vdots & \vdots \\
> y_{1}^{(n-1)} & y_{2}^{(n-1)} & \ldots & y_{n}^{(n-1)}
> \end{array}\right| .
> $$
````

## 5. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|1fd50e80-c6dd-5663-b76f-62cb76946c6f.local at=fa13fb7f-b377-52f0-b6cd-4b7416cd4085] Integrating-Factor Formula for a First-Order Linear ODE
> Suppose that $p(x)$ and $g(x)$ are continuous on the interval $I$. Then any solution of the first-order linear differential equation
>
> $$
> y^{\prime}+p(x) y=g(x), \quad x \text { in } I,
> $$
>
> is of the form
>
> $$
> y=e^{-\int p(x) d x}\left[C+\int g(x) e^{\int p(x) d x} d x\right]
> $$
>
> where $\int p(x) d x$ represents the same antiderivative of $p(x)$ in both occurrences.
````
### After

````text
> [!theorem|1fd50e80-c6dd-5663-b76f-62cb76946c6f.local at=fa13fb7f-b377-52f0-b6cd-4b7416cd4085] Solution of the First Order Linear Differential Equation
> Suppose that $p(x)$ and $g(x)$ are continuous on the interval $I$. Then any solution of the first-order linear differential equation
>
> $$
> y^{\prime}+p(x) y=g(x), \quad x \text { in } I,
> $$
>
> is of the form
>
> $$
> y=e^{-\int p(x) d x}\left[C+\int g(x) e^{\int p(x) d x} d x\right]
> $$
>
> where $\int p(x) d x$ represents the same antiderivative of $p(x)$ in both occurrences.
````

## 6. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|58d36e0f-23d5-5fc2-a7af-d48845743392.local at=ae61bbfd-6cf0-5838-a0b1-c687acef90cc] Abel’s Formula for the Wronskian of Linear ODE Solutions
> On an interval $I$, consider $L[y]=y^{(n)}+p_{n-1}(x)y^{(n-1)}+\cdots+p_1(x)y^{\prime}+p_0(x)y$, where $n\geq1$ and every coefficient $p_j$ is continuous.
>
> Let $y_{1}, y_{2}, \ldots, y_{n}$ be any $n$ solutions to $L[y]=0$. Then the Wronskian $W(x)$ satisfies the first-order differential equation
>
> $$
> W^{\prime}(x)+p_{n-1}(x) W(x)=0 . \quad \text { for } x \text { in } I,
> $$
>
> and hence
>
> $$
> W(x)=C e^{-\int p_{n-1}(x) d x}
> $$
>
> Consequently, either $W(x) \neq 0$ for all $x$ in $I$, or $W(x) \equiv 0$ on $I$.
````
### After

````text
> [!theorem|58d36e0f-23d5-5fc2-a7af-d48845743392.local at=ae61bbfd-6cf0-5838-a0b1-c687acef90cc] Abel's Formula
> On an interval $I$, consider $L[y]=y^{(n)}+p_{n-1}(x)y^{(n-1)}+\cdots+p_1(x)y^{\prime}+p_0(x)y$, where $n\geq1$ and every coefficient $p_j$ is continuous.
>
> Let $y_{1}, y_{2}, \ldots, y_{n}$ be any $n$ solutions to $L[y]=0$. Then the Wronskian $W(x)$ satisfies the first-order differential equation
>
> $$
> W^{\prime}(x)+p_{n-1}(x) W(x)=0 . \quad \text { for } x \text { in } I,
> $$
>
> and hence
>
> $$
> W(x)=C e^{-\int p_{n-1}(x) d x}
> $$
>
> Consequently, either $W(x) \neq 0$ for all $x$ in $I$, or $W(x) \equiv 0$ on $I$.
````

## 7. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|db15dfe7-346c-58c1-8951-18bd923b981e.local at=82d9c1c5-dacf-5fa9-9199-7e7854129d88] Fundamental Solution Sets for Homogeneous Linear ODEs
> The homogeneous equation
>
> $$
> y^{(n)}+p_{n-1}(x) y^{(n-1)}+\cdots+p_{1}(x) y^{\prime}+p_{0}(x) y=0 .
> $$
>
> where the coefficient functions $p_{j}(x)$ are all continuous on an interval $I$, has $n$ solutions $y_{1}, y_{2}, \ldots, y_{n}$ with nonvanishing Wronskian on $I$. Furthermore, given any such set $y_{1}, y_{2}, \ldots y_{n}$ and any solution $y$, then $y=c_{1} y_{1}+c_{2} y_{2}+ \cdots+c_{n} y_{n}$ for a unique choice of constants $c_{1}, c_{2}, \ldots \ldots c_{n}$. The set of solutions $y_{1}, y_{2}, \ldots, y_{n}$ with nonvanishing Wronskian is called a fundamental set of solutions.
````
### After

````text
> [!theorem|db15dfe7-346c-58c1-8951-18bd923b981e.local at=82d9c1c5-dacf-5fa9-9199-7e7854129d88] Existence of a Fundamental Set
> The homogeneous equation
>
> $$
> y^{(n)}+p_{n-1}(x) y^{(n-1)}+\cdots+p_{1}(x) y^{\prime}+p_{0}(x) y=0 .
> $$
>
> where the coefficient functions $p_{j}(x)$ are all continuous on an interval $I$, has $n$ solutions $y_{1}, y_{2}, \ldots, y_{n}$ with nonvanishing Wronskian on $I$. Furthermore, given any such set $y_{1}, y_{2}, \ldots y_{n}$ and any solution $y$, then $y=c_{1} y_{1}+c_{2} y_{2}+ \cdots+c_{n} y_{n}$ for a unique choice of constants $c_{1}, c_{2}, \ldots \ldots c_{n}$. The set of solutions $y_{1}, y_{2}, \ldots, y_{n}$ with nonvanishing Wronskian is called a fundamental set of solutions.
````

## 8. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|e9b1c9b6-7a98-5fe0-a9b9-a4669d1e18ef.local at=a97cae01-9f6e-56a3-bfed-06e078e1c08f] Wronskian Criterion for a Fundamental Set of Linear ODE Solutions
> On an interval $I$, consider $L[y]=y^{(n)}+p_{n-1}(x)y^{(n-1)}+\cdots+p_1(x)y^{\prime}+p_0(x)y$, where $n\geq1$ and every coefficient $p_j$ is continuous.
>
> Let $y_{1}, y_{2}, \ldots y_{n}$ be any $n$ solutions to $L[y]=0$ with coefficients continuous on an interval $I$. The following are equivalent:
> (i) $y_{1}, y_{2}, \ldots, y_{n}$ are linearly independent on $I$;
> (ii) $y_{1}, y_{2}, \ldots y_{n}$ form a fundamental set of solutions of $L[y]=0$:
> (iii) $W\left(y_{1}, y_{2}, \ldots, y_{n}\right)\left(x_{0}\right) \neq 0$ for some $x_{0}$ in $I$;
> (iv) $W\left(y_{1}, y_{2}, \ldots, y_{n}\right)(x) \neq 0$ for all $x$ in $I$.
````
### After

````text
> [!theorem|e9b1c9b6-7a98-5fe0-a9b9-a4669d1e18ef.local at=a97cae01-9f6e-56a3-bfed-06e078e1c08f] Wronskian Criterion for Linear Independence
> On an interval $I$, consider $L[y]=y^{(n)}+p_{n-1}(x)y^{(n-1)}+\cdots+p_1(x)y^{\prime}+p_0(x)y$, where $n\geq1$ and every coefficient $p_j$ is continuous.
>
> Let $y_{1}, y_{2}, \ldots y_{n}$ be any $n$ solutions to $L[y]=0$ with coefficients continuous on an interval $I$. The following are equivalent:
> (i) $y_{1}, y_{2}, \ldots, y_{n}$ are linearly independent on $I$;
> (ii) $y_{1}, y_{2}, \ldots y_{n}$ form a fundamental set of solutions of $L[y]=0$:
> (iii) $W\left(y_{1}, y_{2}, \ldots, y_{n}\right)\left(x_{0}\right) \neq 0$ for some $x_{0}$ in $I$;
> (iv) $W\left(y_{1}, y_{2}, \ldots, y_{n}\right)(x) \neq 0$ for all $x$ in $I$.
````

## Additional source comparison

## 1. Restore the exact descriptive source title without its numbering.

### Before

````text
> [!theorem|58d36e0f-23d5-5fc2-a7af-d48845743392.local at=ae61bbfd-6cf0-5838-a0b1-c687acef90cc] Abel's Formula
````
### After

````text
> [!theorem|58d36e0f-23d5-5fc2-a7af-d48845743392.local at=ae61bbfd-6cf0-5838-a0b1-c687acef90cc] Abel's Formula for the Wronskian
````

## 2. Restore the exact descriptive source title without its numbering.

### Before

````text
> [!theorem|db15dfe7-346c-58c1-8951-18bd923b981e.local at=82d9c1c5-dacf-5fa9-9199-7e7854129d88] Existence of a Fundamental Set
````
### After

````text
> [!theorem|db15dfe7-346c-58c1-8951-18bd923b981e.local at=82d9c1c5-dacf-5fa9-9199-7e7854129d88] Existence of Fundamental Sets of Solutions
````

## Source-to-current comparison

Source: /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 10 Ordinary Differential Equations Review of Concepts and Methods/10.1 Linear Ordinary Differential Equations.md

This exact comparison preserves the full change evidence, including formatting, OCR corrections, restored source wording, and required standalone context. The entries above explain the recovery edits. The comparison is not a claim that every difference is a correction; component serialization, callout wrapping, and printed labels outside callouts are formatting.

`````diff
--- /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 10 Ordinary Differential Equations Review of Concepts and Methods/10.1 Linear Ordinary Differential Equations.md
+++ /Users/gradyclopton/ObsidianVaults/complex_analysis/Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 10 Ordinary Differential Equations Review of Concepts and Methods/10.1 Linear Ordinary Differential Equations.md
@@ -1,3 +1,4 @@
+
 ## APPENDIX A
 
 ## Topics to Review
@@ -6,59 +7,67 @@
 
 ## Looking Ahead...
 
-This appendix presents standard techniques for solving linear ordinary differential equations. They are needed throughout this book. Our primary use of the power series and Frobenius methods of Sections A.4, A.5, and A. 6 will be to establish the basic properties of Bessel functions (Chapter 4) and Legendre polynomials (Chapter 5).
+This appendix presents standard techniques for solving linear ordinary differential equations. They are needed throughout this book. Our primary use of the power series and Frobenius methods of Sections 10.4, 10.5, and 10.6 will be to establish the basic properties of Bessel functions (Chapter 12) and Legendre polynomials (Chapter 13).
 
 ## ORDINARY DIFFERENTIAL EQUATIONS: REVIEW OF CONCEPTS AND METHODS
 
 
 #### Abstract
 
-Among all the mathematical disciplines the theory of differential equations is the most important. It furnishes the explanation of all those elementary manifestations of nature which imolve time.
+Among all the mathematical disciplines the theory of differential equations is the most important. It furnishes the explanation of all those elementary manifestations of nature which involve time.
 
 
 -SOPHUS LIE
 
-A basic knowledge of ordinary differential equations is exsential for the development of the main topics of this book. For example solving a partial differential equation by standard methods leads naturally to ordinary differential equations. In this appendix we provide a review of the basic techniques that will be useful in this book. Our brief presentation covers the essentials of linear ordinary differential equations as taught in a first course on differential equations. In the first section we present the fundamental properties of existence uniqueness, and linear independence of solutions. The rest of the chapter is devoted to the treatment of the basic tools for solving linear ordinary differential equations, including series methods. This chapter is not intended as a comprehensive treatment, but rather as a convenient reference for topics that are needed in the book.
-
-## 10.1 Linear Ordinary Differential Equations
-
-## THEOREM 1 SOLUTION OF THE FIRST ORDER LINEAR DIFFERENTIAL EQUATION
-
-The expression $\int p(x) d x$ represents an antiderivative of $p(a)$. and so it is defined up to a constant $C$. In applying (2). you should take the same value of $C$ in both occurences of $\int p(x) d x$ Usually, the most convenient choice is $C=$ 0. (See Example 1.)
-
-An ordinary differential equation is an equation that involves an unknown function $y$ and its derivatives $y^{(j)}$ of order $j$. A linear ordinary differential equation in standard form is an equation
-
-$$
-y^{(n)}+p_{n-1}(x) y^{(n-1)}+\cdots+p_{1}(x) y^{\prime}+p_{0}(x) y=g(r)
-$$
-
-where $n$ is called the order of the equation and $p_{j}\left(x^{\prime}\right)$ and $g(r)$ are given functions of $x$. The expression standard form refers to the fact that the leading coefficient is 1 . A solution of (1) on an interval $I$ is any $n$ times differentiable function $y=y(x)$ satisfying (1) on 1 . The equation (1) is homogeneous if $g(x) \equiv 0$, otherwise it is nonhomogeneous.
+A basic knowledge of ordinary differential equations is essential for the development of the main topics of this book. For example solving a partial differential equation by standard methods leads naturally to ordinary differential equations. In this appendix we provide a review of the basic techniques that will be useful in this book. Our brief presentation covers the essentials of linear ordinary differential equations as taught in a first course on differential equations. In the first section we present the fundamental properties of existence uniqueness, and linear independence of solutions. The rest of the chapter is devoted to the treatment of the basic tools for solving linear ordinary differential equations, including series methods. This chapter is not intended as a comprehensive treatment, but rather as a convenient reference for topics that are needed in the book.
+
+# 10.1 Linear Ordinary Differential Equations
+
+> [!definition|7db2073f-ab58-5437-aca4-16c500070e9a.local at=2f81238a-9d7d-51d8-8141-31dc3cf7aefe] Linear Ordinary Differential Equation in Standard Form
+> An ordinary differential equation is an equation that involves an unknown function $y$ and its derivatives $y^{(j)}$ of order $j$. A linear ordinary differential equation in standard form is an equation
+>
+> $$
+> y^{(n)}+p_{n-1}(x) y^{(n-1)}+\cdots+p_{1}(x) y^{\prime}+p_{0}(x) y=g(x)
+> $$
+>
+> where $n$ is called the order of the equation and $p_j(x)$ and $g(x)$ are given functions of $x$. The expression standard form refers to the fact that the leading coefficient is 1 . A solution of this equation on an interval $I$ is any $n$ times differentiable function $y=y(x)$ satisfying the equation on $I$. The equation is homogeneous if $g(x) \equiv 0$, otherwise it is nonhomogeneous.
+
+*Printed equation label: (1).*
 
 The first- and second-order equations are of particular interest to us. We can describe completely the solution of the first one, while discussion of the second will occupy the rest of this appendix.
 
-Suppose that $p(x)$ and $g(x)$ are continuous on the interval $I$. Then any solution of the first-order linear differential equation
-
-$$
-y^{\prime}+p(x) y=g(x), \quad x \text { in } l,
-$$
-
-is of the form
-
-$$
-y=e^{-\int p(x) d x}\left[C+\int g(x) e^{\int p(x) d x} d x\right]
-$$
-
-where $\int p(x) d x$ represents the same antiderivative of $p(x)$ in both occurcuces.
-
-Proof Suppose $y$ is a solution. Multiply the equation throngh by the integrating factor $\mu(x)=e^{\int p(x) d x}$ and get
+> [!theorem|1fd50e80-c6dd-5663-b76f-62cb76946c6f.local at=fa13fb7f-b377-52f0-b6cd-4b7416cd4085] Solution of the First Order Linear Differential Equation
+> Suppose that $p(x)$ and $g(x)$ are continuous on the interval $I$. Then any solution of the first-order linear differential equation
+>
+> $$
+> y^{\prime}+p(x) y=g(x), \quad x \text { in } I,
+> $$
+>
+> is of the form
+>
+> $$
+> y=e^{-\int p(x) d x}\left[C+\int g(x) e^{\int p(x) d x} d x\right]
+> $$
+>
+> where $\int p(x) d x$ represents the same antiderivative of $p(x)$ in both occurrences.
+
+*Printed equation label: (2).*
+
+The expression $\int p(x) d x$ represents an antiderivative of $p(x)$, and so it is defined up to a constant $C$. In applying (2). you should take the same value of $C$ in both occurrences of $\int p(x) d x$ Usually, the most convenient choice is $C=$ 0. (See Example 1.)
+
+
+Proof Suppose $y$ is a solution. Multiply the equation through by the integrating factor $\mu(x)=e^{\int p(x) d x}$ and get
 
 $$
 \mu(x)\left[y^{\prime}+p(x) y\right]=g(x) \mu(x) .
 $$
 
-Since $\mu^{\prime}(x)=p(x) \mu(x)$, by the product rule, the equation can be rewritten as $[\mu(x) y]^{\prime}=g(x) \mu(x)$. Integrating both sides and dividing by $\mu(x)$ yields the desired solution. Note that, since $\mu(x)$ is an exponential function, it is nonzero for all $x$. and so we may divide by it.) $\square$
-
-## EXAMPLE 1 A first-order differential equation
+Since $\mu^{\prime}(x)=p(x) \mu(x)$, by the product rule, the equation can be rewritten as $[\mu(x) y]^{\prime}=g(x) \mu(x)$. Integrating both sides and dividing by $\mu(x)$ yields the desired solution. Note that, since $\mu(x)$ is an exponential function, it is nonzero for all $x$, and so we may divide by it.) $\square$
+
+> [!exercise|d6de4eb0-7159-5dd3-8f9d-e89059b4c60c.local at=8ddba0d2-9429-568a-bf56-3aecc750da70] EXAMPLE 1 A first-order differential equation
+> Solve $y^{\prime}-y=2$ by an integrating factor.
+
+##### solution
 
 Using Theorem 1, we find all solutions of the differential equation
 
@@ -72,26 +81,32 @@
 
 $$
 y^{(n)}+p_{n-1}(x) y^{(n-1)}+\cdots+p_{1}(x) y^{\prime}+p_{0}(x) y=0,
+\tag{3}
 $$
 
 where all the coefficient functions are continuous on some fixed interval $I$.
 We begin with a definition that is central to our treatment.
 
-THE WRONSKIAN
-Let $y_{1}, y_{2}, \ldots, y_{n}$ be any $n$ solutions to the homogeneous linear differential equation (3). The Wronskian $W\left(y_{1}, y_{2}, \ldots, y_{n}\right)$ of these solutions is given by the following $n \times n$ determinant:
-
-$$
-W\left(y_{1}, y_{2}, \ldots, y_{n}\right)=\left|\begin{array}{cccc}
-y_{1} & y_{2} & \ldots & y_{n} \\
-y_{1}^{\prime} & y_{2}^{\prime} & \ldots & y_{n}^{\prime} \\
-\vdots & \vdots & \vdots & \vdots \\
-y_{1}^{(n-1)} & y_{2}^{(n-1)} & \ldots & y_{n}^{(n-1)}
-\end{array}\right| .
-$$
+> [!definition|18a292cd-fb05-5a7f-8487-87369bb7350e.local at=f610b10d-92a0-5cb5-9fd7-22daf3013e0b] The Wronskian
+> On an interval $I$, let $L[y]=y^{(n)}+p_{n-1}(x)y^{(n-1)}+\cdots+p_1(x)y^{\prime}+p_0(x)y$, where $n\geq1$ and the coefficients are continuous.
+>
+> Let $y_{1}, y_{2}, \ldots, y_{n}$ be any $n$ solutions to the homogeneous linear differential equation $L[y]=0$. The Wronskian $W\left(y_{1}, y_{2}, \ldots, y_{n}\right)$ of these solutions is given by the following $n \times n$ determinant:
+>
+> $$
+> W\left(y_{1}, y_{2}, \ldots, y_{n}\right)=\left|\begin{array}{cccc}
+> y_{1} & y_{2} & \ldots & y_{n} \\
+> y_{1}^{\prime} & y_{2}^{\prime} & \ldots & y_{n}^{\prime} \\
+> \vdots & \vdots & \vdots & \vdots \\
+> y_{1}^{(n-1)} & y_{2}^{(n-1)} & \ldots & y_{n}^{(n-1)}
+> \end{array}\right| .
+> $$
 
 We will sometimes use the alternative notation $W\left(y_{1}, y_{2}, \ldots, y_{n}\right)(x)$, or simply $W(x)$, to emphasize that the Wronskian is a function of $x$.
 
-## EXAMPLE 2 Computing Wronskians
+> [!exercise|1a23ccdd-4412-5819-bac5-383ee0614952.local at=42f04268-1d65-5edd-b6c4-696399870151] EXAMPLE 2 Computing Wronskians
+> Compute the Wronskians (a) $W(e^x,e^{-x})$ and (b) $W(\cos x,\sin x)$.
+
+##### solution
 
 (a) The equation $y^{\prime \prime}-y=0$ has solutions $y_{1}=e^{x}$ and $y_{2}=e^{-x}$. Their Wronskian is
 
@@ -113,24 +128,25 @@
 
 The next theorem gives an explicit form of the Wronskian in terms of the coefficient functions in (3).
 
-THEOREM 2 ABEL'S FORMULA FOR THE WRONSKIAN
-
-Since the key issue is whether If vanishes or not, we cannot divide by $W$ to separate variables. An appeal to Theorem 1 is necossary.
-
-Let $y_{1}, y_{2}, \ldots, y_{n}$ be any $n$ solutions to the homogeneous linear differential equation (3). Then the Wronskian $W(x)$ satisfies the first-order differential equation
-
-$$
-W^{\prime}(x)+p_{n-1}(x) W(x)=0 . \quad \text { for } x \text { in } l,
-$$
-
-and hence
-(1)
-
-$$
-W(x)=C e^{-\int p_{n-1}(x) d x}
-$$
-
-Consequently, either $W(x) \neq 0$ for all $x$ in $I$, or $W(x) \equiv 0$ on $I$.
+> [!theorem|58d36e0f-23d5-5fc2-a7af-d48845743392.local at=ae61bbfd-6cf0-5838-a0b1-c687acef90cc] Abel's Formula for the Wronskian
+> On an interval $I$, consider $L[y]=y^{(n)}+p_{n-1}(x)y^{(n-1)}+\cdots+p_1(x)y^{\prime}+p_0(x)y$, where $n\geq1$ and every coefficient $p_j$ is continuous.
+>
+> Let $y_{1}, y_{2}, \ldots, y_{n}$ be any $n$ solutions to $L[y]=0$. Then the Wronskian $W(x)$ satisfies the first-order differential equation
+>
+> $$
+> W^{\prime}(x)+p_{n-1}(x) W(x)=0 . \quad \text { for } x \text { in } I,
+> $$
+>
+> and hence
+>
+> $$
+> W(x)=C e^{-\int p_{n-1}(x) d x}
+> $$
+>
+> Consequently, either $W(x) \neq 0$ for all $x$ in $I$, or $W(x) \equiv 0$ on $I$.
+
+*Printed equation label: (4).*
+
 The point of this theorem is that determining that $W(x) \neq 0$ for some $x$ in $I$ allows us to conclude that $W(x) \neq 0$ for all $x$ in $I$.
 Proof For clarity's sake, we give a proof only for $n=2$. (The case $n=3$ is treated in Exercise 31.) The same approach generalizes to higher dimensions but requires a greater knowledge of linear algebra. For $n=2$, the equation is $y^{\prime \prime}+p_{1}(x) y^{\prime}+p_{0}(x) y=0$, and $W(x)=y_{1} y_{2}^{\prime}-y_{1}^{\prime} y_{2}$. Since $y_{1}$ and $y_{2}$ are solutions, we have
 
@@ -142,93 +158,126 @@
 \end{aligned}
 $$
 
-This is a first-order differential equation for $W(x)$ and (4) is an immediate consequence of (2) in Theorem 1.
+This is a first-order differential equation for $W(x)$. We do not divide by $W$, since it may vanish. The integrating-factor formula (4) is an immediate consequence of (2) in Theorem 1.
 
 It is crucial in applying Theorem 2 to put the equation in standard form and verify the continuity of the coefficients. See Exercise 23.
 
 We can now state a fundamental result in the theory of ordinary differential equations.
 
-THEOREM 3 EXISTENCE OF FUNDAMENTAL SETS OF SOLUTIONS
-
-The homogeneous equation (3)
-
-$$
-y^{(n)}+p_{n-1}(x) y^{(n-1)}+\cdots+p_{1}(x) y^{\prime}+p_{0}(x) y=0 .
-$$
-
-where the coefficient functions $p_{j}(x)$ are all continuous on an interval $I$, has $n$ solutions $y_{1}, y_{2}, \ldots, y_{n}$ with nonvanishing Wronskian on $I$. Furthermore, given any such set $y_{1}, y_{2}, \ldots y_{n}$ and any solution $y$, then $y=c_{1} y_{1}+c_{2} y_{2}+ \cdots+c_{n} y_{n}$ for a unique choice of constants $c_{1}, c_{2}, \ldots \ldots c_{n}$. The set of solutions $y_{1}, y_{2}, \ldots, y_{n}$ with nonvanishing Wronskian is called a fundamental set of solutions.
+> [!theorem|db15dfe7-346c-58c1-8951-18bd923b981e.local at=82d9c1c5-dacf-5fa9-9199-7e7854129d88] Existence of Fundamental Sets of Solutions
+> The homogeneous equation
+>
+> $$
+> y^{(n)}+p_{n-1}(x) y^{(n-1)}+\cdots+p_{1}(x) y^{\prime}+p_{0}(x) y=0 .
+> $$
+>
+> where the coefficient functions $p_{j}(x)$ are all continuous on an interval $I$, has $n$ solutions $y_{1}, y_{2}, \ldots, y_{n}$ with nonvanishing Wronskian on $I$. Furthermore, given any such set $y_{1}, y_{2}, \ldots y_{n}$ and any solution $y$, then $y=c_{1} y_{1}+c_{2} y_{2}+ \cdots+c_{n} y_{n}$ for a unique choice of constants $c_{1}, c_{2}, \ldots \ldots c_{n}$. The set of solutions $y_{1}, y_{2}, \ldots, y_{n}$ with nonvanishing Wronskian is called a fundamental set of solutions.
 
 Theorem 3 asserts that any linear homogeneous differential equation of order $n$ has $n$ solutions that span the set of all solutions of the equation. Note that the theorem does not assert the uniqueness of a fundamental set. If $y_{1}, y_{2}, \ldots, y_{n}$ is a fundamental set of solutions, then the linear combination $y=c_{1} y_{1}+c_{2} y_{2}+\cdots+c_{n} y_{n}$ is referred to as the general solution.
 
-## THEOREM 4 SUPERPOSITION PRINCIPLE
-
-THEOREM 5 GENERAL
-SOLUTION OF NONHOMOGENEOUS EQUATIONS
-
 We have been using without verification that a linear combination of solutions of a homogeneous linear equation is again a solution. This simple fact. called the superposition principle, can be checked directly by appealing to (3). We state it here for ease of reference.
 
-Suppose that $u(x)$ and $v(x)$ are solutions of the linear homogeneous equation (3) and let $c$ and $d$ be any two numbers. Then the linear combination $c u(x)+d v(x)$ is also a solution of (3).
+> [!theorem|cb200824-c353-579a-9ff0-cd179f9d6e12.local at=7d6b0cc2-3654-54e2-9af8-eac5712a0bcd] Superposition Principle
+> On an interval $I$, let $L[y]=y^{(n)}+p_{n-1}(x)y^{(n-1)}+\cdots+p_1(x)y^{\prime}+p_0(x)y$, where $n\geq1$ and the coefficients are continuous.
+>
+> Suppose that $u(x)$ and $v(x)$ are solutions of $L[y]=0$ and let $c$ and $d$ be any two numbers. Then the linear combination $c u(x)+d v(x)$ is also a solution of $L[y]=0$.
 
 ## Nonhomogeneous Differential Equations
 
 Let us recall from (1) the general nonhomogeneous equation
 
 $$
-y^{(n)}+p_{n-1}(r) y^{(n 1)}+\cdots+p_{1}(x) y^{\prime}+p_{0}(x) y=g(x),
-$$
-
-where the coefficient functions and $g(x)$ are all assumed to be continuous on some interval $I$. If $g(x)$ is replaced by 0 , we call the resulting equation the associated homogeneous equation. We know from Theorem 3 that the associated homogeneous equation has a fundamental set of solutions $y_{1}$, $y_{2}, \ldots, y_{n}$. We will show in Section 10.2, using the method of variation of parameters, that (5) has at least one solution that we will denote by $y_{p}$ and call a particular solution. Now suppose that $y$ is any other solution of (5). It is a simple exercise to check that $y-y_{p}$ is a solution of the associated homogeneous equation. By Theorem 3 we must have $y-y_{p}= c_{1} y_{1}+c_{2} y_{2}+\cdots+c_{n} y_{n}$. Thus, if $y_{h}$ denotes the general solution of the associated homogeneous equation, it follows that $y=y_{h}+y_{p}$ (known as the general solution of the nonhomogeneous equation). We have proved the following important result.
-
-Let $y_{h}$ and $y_{p}$ denote, respectively, the general solution of the homogeneous equation associated with (5) and a particular solution of (5). Then any solution $y$ of (5) has the form
-
-$$
-y=y_{h}+y_{p}
-$$
+y^{(n)}+p_{n-1}(x)y^{(n-1)}+\cdots+p_{1}(x) y^{\prime}+p_{0}(x) y=g(x),
+\tag{5}
+$$
+
+where the coefficient functions and $g(x)$ are all assumed to be continuous on some interval $I$. If $g(x)$ is replaced by 0 , we call the resulting equation the associated homogeneous equation. We know from Theorem 3 that the associated homogeneous equation has a fundamental set of solutions $y_{1}$, $y_{2}, \ldots, y_{n}$. We will show in Section 10.3, using the method of variation of parameters, that (5) has at least one solution that we will denote by $y_{p}$ and call a particular solution. Now suppose that $y$ is any other solution of (5). It is a simple exercise to check that $y-y_{p}$ is a solution of the associated homogeneous equation. By Theorem 3 we must have $y-y_{p}= c_{1} y_{1}+c_{2} y_{2}+\cdots+c_{n} y_{n}$. Thus, if $y_{h}$ denotes the general solution of the associated homogeneous equation, it follows that $y=y_{h}+y_{p}$ (known as the general solution of the nonhomogeneous equation). We have proved the following important result.
+
+> [!theorem|c4e81fe4-f52b-5477-83a1-df188c8bcf6a.local at=fd3850cc-d23a-5891-a840-635cb32dfc87] General Solution of Nonhomogeneous Equations
+> On an interval $I$, let $L[y]=y^{(n)}+p_{n-1}(x)y^{(n-1)}+\cdots+p_1(x)y^{\prime}+p_0(x)y$, where $n\geq1$ and the coefficients are continuous.
+>
+> Let $g$ be continuous on $I$.
+>
+> Let $y_{h}$ and $y_{p}$ denote, respectively, the general solution of the homogeneous equation associated with $L[y]=g$ and a particular solution of $L[y]=g$. Then any solution $y$ of $L[y]=g$ has the form
+>
+> $$
+> y=y_{h}+y_{p}
+> $$
 
 Often in applications we have to solve differential equations subject to certain conditions; for example,
 
 $$
-y^{\prime \prime}+y=c^{x}, \quad y(0)=0, y^{\prime}(0)=1 .
+y^{\prime \prime}+y=e^{x}, \quad y(0)=0, y^{\prime}(0)=1 .
 $$
 
 Such a problem is called an initial value problem, and the conditions are called initial conditions. Typically we impose enough conditions to specify a unique solution of the problem. Since the general solution of an $n$th order linear differential equation has $n$ arbitrary constants, we expect $n$ conditions to suffice.
 
-THEOREM 6 EXISTENCE AND UNIQUENESS FOR INITIAL VALUE PROBLEMS
-
-![](./images/ecab6dba-4966-4870-8bb0-6c1f9a8f866d-06_398_466_793_63.jpg)
-Figure 1 Various solutions from Example 3.
-
-![](./images/ecab6dba-4966-4870-8bb0-6c1f9a8f866d-06_421_468_1396_63.jpg)
-Figure 2 Solution of the initial value problem in Example 3 and its tangent line at $x=0$. It is the only curve among those in Figure 1 that goes through the point $(0,4)$ and that has slope at $x=0$ equal to $y^{\prime}(0)=2$.
-
-Consider the initial value problem consisting of the linear differential equation (5) and the initial conditions
-
-$$
-y\left(x_{0}\right)=y_{0}, y^{\prime}\left(x_{0}\right)=y_{0}^{\prime}, \ldots, y^{(n-1)}\left(x_{0}\right)=y_{0}^{(n-1)},
-$$
-
-where $x_{0}$ is in $I$ and $y_{0}, y_{0}^{\prime}, \ldots, y_{0}^{(n-1)}$ are prescribed values. Then this problem has a unique solution $y$ on the interval $I$.
+> [!theorem|12d47e51-786c-53e9-a14b-1272ed834ece.local at=f9afdc7a-c723-5527-b50e-5a177b36c12a] Existence and Uniqueness for Initial Value Problems
+> On an interval $I$, let $L[y]=y^{(n)}+p_{n-1}(x)y^{(n-1)}+\cdots+p_1(x)y^{\prime}+p_0(x)y$, where $n\geq1$ and the coefficients are continuous.
+>
+> Let $g$ be continuous on $I$.
+>
+> Consider the initial value problem consisting of the linear differential equation $L[y]=g$ and the initial conditions
+>
+> $$
+> y\left(x_{0}\right)=y_{0}, y^{\prime}\left(x_{0}\right)=y_{0}^{\prime}, \ldots, y^{(n-1)}\left(x_{0}\right)=y_{0}^{(n-1)},
+> $$
+>
+> where $x_{0}$ is in $I$ and $y_{0}, y_{0}^{\prime}, \ldots, y_{0}^{(n-1)}$ are prescribed values. Then this problem has a unique solution $y$ on the interval $I$.
 
 Proof Let $y_{p}$ be a particular solution to (5) and let $y_{1}, y_{2}, \ldots, y_{n}$ be a fundamental set of solutions to the associated homogeneous equation. For clarity's sake we take $n=2$, although the proof generalizes for arbitrary $n$. We need to solve the $2 \times 2$ system
 
 $$
-\left\{\begin{array} { l } 
-{ c _ { 1 } y _ { 1 } ( x _ { 0 } ) + c _ { 2 } y _ { 2 } ( x _ { 0 } ) + y _ { p } ( x _ { 0 } ) = y _ { 0 } } \\
-{ c _ { 1 } y _ { 1 } ^ { \prime } ( x _ { 0 } ) + c _ { 2 } y _ { 2 } ^ { \prime } ( x _ { 0 } ) + y _ { p } ^ { \prime } ( x _ { 0 } ) = y _ { 0 } ^ { \prime } }
-\end{array} \Leftrightarrow \left\{\begin{array}{l}
-c_{1} y_{1}\left(x_{0}\right)+c_{2} y_{2}\left(x_{0}\right)=y_{0}-y_{p}\left(x_{0}\right) \\
-c_{1} y_{1}^{\prime}\left(x_{0}\right)+c_{2} y_{2}^{\prime}\left(x_{0}\right)=y_{0}^{\prime}-y_{p}^{\prime}\left(x_{0}\right)
-\end{array}\right.\right.
-$$
-
-for the unknowns $c_{1}$ and $c_{2}$. Since the determinant of the matrix of this system is precisely the Wronskian and is nonzero by definition (see Theorem 3), it follows that the system has a unique solution pair $c_{1}, c_{2}$. This proves the existence of the solution of the initial value problem. To establish the uniqueness of the solution. suppose that $u(x)$ and $v(x)$ are two solutions to the initial value problem. Let $w=u-v$. Then $w$ satisfies the associated homogencons equation with 0 initial values. We know from Theorem 3 that $w=a y_{1}+b y_{2}$ for some choice of $a$ and $b$. Now using the initial values of $w$ and the fact that $W\left(y_{1}, y_{2}\right)\left(x_{0}\right) \neq 0$, we infer that $a=b=0$ and hence $w \equiv 0$ implying that $u \equiv v$.
-
-## EXAMPLE 3 An initial value problem
+\begin{cases}
+c_1y_1(x_0)+c_2y_2(x_0)+y_p(x_0)=y_0,\\
+c_1y_1^{\prime}(x_0)+c_2y_2^{\prime}(x_0)+y_p^{\prime}(x_0)=y_0^{\prime}
+\end{cases}
+\quad\Longleftrightarrow\quad
+\begin{cases}
+c_1y_1(x_0)+c_2y_2(x_0)=y_0-y_p(x_0),\\
+c_1y_1^{\prime}(x_0)+c_2y_2^{\prime}(x_0)=y_0^{\prime}-y_p^{\prime}(x_0).
+\end{cases}
+$$
+
+for the unknowns $c_{1}$ and $c_{2}$. Since the determinant of the matrix of this system is precisely the Wronskian and is nonzero by definition (see Theorem 3), it follows that the system has a unique solution pair $c_{1}, c_{2}$. This proves the existence of the solution of the initial value problem. To establish the uniqueness of the solution. suppose that $u(x)$ and $v(x)$ are two solutions to the initial value problem. Let $w=u-v$. Then $w$ satisfies the associated homogeneous equation with 0 initial values. We know from Theorem 3 that $w=a y_{1}+b y_{2}$ for some choice of $a$ and $b$. Now using the initial values of $w$ and the fact that $W\left(y_{1}, y_{2}\right)\left(x_{0}\right) \neq 0$, we infer that $a=b=0$ and hence $w \equiv 0$ implying that $u \equiv v$.
+
+```scientific-figure
+id: ff2a4568-f74f-423c-a51c-67b8b417e9f2
+numbered: false
+title: ""
+caption: Figure 1 Various solutions from Example 3.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 10 Ordinary Differential Equations Review of Concepts and Methods/images/ecab6dba-4966-4870-8bb0-6c1f9a8f866d-06_398_466_793_63.jpg
+    caption: ""
+```
+
+
+```scientific-figure
+id: 4970a62d-7abf-46ce-a0fc-7f39c688b03b
+numbered: false
+title: ""
+caption: Figure 2 Solution of the initial value problem in Example 3 and its tangent line at $x=0$. It is the only curve among those in Figure 1 that goes through the point $(0,4)$ and that has slope at $x=0$ equal to $y^{\prime}(0)=2$.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 10 Ordinary Differential Equations Review of Concepts and Methods/images/ecab6dba-4966-4870-8bb0-6c1f9a8f866d-06_421_468_1396_63.jpg
+    caption: ""
+```
+
+
+> [!exercise|ba2e44c0-bec3-5a0d-bd4a-64ae0cff2dd4.local at=eb2995c0-57db-578e-956b-4105c9a2c629] EXAMPLE 3 An initial value problem
+> Given a particular solution $y_p=2x+3$ and homogeneous basis $e^x,e^{2x}$, solve $y^{\prime\prime}-3y^{\prime}+2y=4x$ with $y(0)=4$, $y^{\prime}(0)=2$.
+
+##### solution
 
 You can (and should) check that the equation $y^{\prime \prime}-3 y^{\prime}+2 y=4 x$ has $y_{p}=2 x+3$ as a particular solution and that the associated homogeneous equation $y^{\prime \prime}-3 y^{\prime}+2 y=0$ has general solution $y_{h}=c_{1} e^{x}+c_{2} e^{2 x}$. (General techniques for deriving these solutions will be developed in the next two sections.) Hence the general solution of the nonhomogeneous equation is
 
 $$
-y=y_{n}+y_{p}=c_{1} e^{x}+c_{2} e^{2 x}+2 x+3
+y=y_h+y_p=c_{1} e^{x}+c_{2} e^{2 x}+2 x+3
 $$
 
 (see Figure 1). Now suppose that we want to solve the initial value problem
@@ -248,25 +297,32 @@
 
 This system has a unique solution $c_{1}=2$ and $c_{2}=-1$. Hence the (unique) solution of the initial value problem is $y=2 e^{x}-e^{2 x}+2 x+3$ (Figure 2).
 
-## THEOREM 7 WRONSKIAN CRITERION FOR LINEAR INDEPENDENCE
-
 We next present a brief discussion of linear independence of solutions and its connection to fundamental sets.
 
-The functions $f_{1}, f_{2}, \ldots, f_{n}$ defined on an interval $[a, b]$ are said to be linearly independent on $[a, b]$ if the only choice of the constants $c_{1}, c_{2}, \ldots$, $c_{n}$ for which the linear combination $c_{1} f_{1}+c_{2} f_{2}+\cdots+c_{n} f_{n}$ vanishes identically on $[a, b]$ is $c_{1}=c_{2}=\cdots=c_{n}=0$. Otherwise, the functions are said to be linearly dependent. When $n=2$, we note that linear dependence is equivalent to one function being a constant multiple of the other. The following result shows a connection between the notion of linear independence and fundamental sets.
-
-Let $y_{1}, y_{2}, \ldots y_{n}$ be any $n$ solutions to the homogeneons linear differential equation (3) with coefficients continuous on an interval $I$. The following are equivalent:
-(i) $y_{1}, y_{2}, \ldots, y_{n}$ are linearly independent on $I$;
-(ii) $y_{1}, y_{2}, \ldots y_{n}$ form a fundamental set of solutions of (3):
-(iii) $W\left(y_{1}, y_{2}, \ldots, y_{n}\right)\left(x_{0}\right) \neq 0$ for some $x_{0}$ in $I$;
-(iv) $W\left(y_{1}, y_{2}, \ldots, y_{n}\right)(x) \neq 0$ for all $x$ in $I$.
-
-Proof Clearly (ii) ⇔ (iii) ⇔ (iv) follow from Theorems 2 and 3 and the definition of a fundamental set. We conclude by proving (i) ⇒ (iii) and (iii) ⇒ (i). We start with (iii) ⇒ (i). Suppose that $y_{1}, y_{2}, \ldots, y_{n}$ are any $n$ solutions such that $c_{1} y_{1}+c_{2} y_{2}+\cdots+c_{n} y_{n}=0$. By differentiating this equation $n-1$ times in succession and then setting $x=x_{0}$, we get a system of $n$ linear homogeneous equations in the $n$ unknowns $c_{1}, c_{2}, \ldots, c_{n}$. The determinant of the matrix of this system is precisely $W\left(x_{0}\right)$, which is nonzero by assumption. The nonvanishing of this determinant implies that $c_{1}=c_{2}=\cdots=c_{n}=0$, proving (iii) ⇒ (i). To complete the proof it is enough to show (i) ⇒ (iii). The proof is by contradiction. We assume that $y_{1}, y_{2}, \ldots, y_{n}$ are linearly independent on $I$ and that $W\left(y_{1}, y_{2}, \ldots, y_{n}\right)\left(x_{0}\right)=0$. The vanishing of the Wronskian implies that there are constants $c_{1}, c_{2}, \ldots, c_{n}$. not all zero, such that all the initial values of $y=c_{1} y_{1}+c_{2} y_{2}+\cdots+c_{n} y_{n}$ are 0 at $x_{0}$ (for $n=2$, this fact is clear). However, the solution $w \equiv 0$ has the same intital values, and so by the uniqueness part of Theorem 6, $w \equiv y \equiv 0$, implying that $c_{1}=c_{2}=\cdots =c_{n}=0$ by the definition of linear independence, which is a contradiction.
-
-## EXAMPLE 4 Fundamental sets of solutions, linear independence
-
-We saw in Example 2 that $e^{x}$ and $e^{-x}$ are solutions of $y^{\prime \prime}-y=0$ and that $W\left(e^{x}\right.$, $\left.e^{-x}\right)=-2 \neq 0$. Thus, by Theorem 7. the general solution of the differential equation is of the form $y=c_{1} e^{x}+c_{2} e^{-x}$; and so any solution is a linear combination of the functions $r^{r}$ and $e^{-x}$, which form a fundamental set of solutions.
-
-It is worthwhile to note that the fundamental set of solutions is not unique. For the equation at hand, you can casily check that cosh $x$ and $\sinh x$ are also solutions. Their Wronskian is
+> [!definition|30633ae5-b6c2-5e89-a843-405b3ac75152.local at=9d6c51b1-76b0-5769-85b1-b8cd19af9c8b] Linear Independence of Functions on an Interval
+> The functions $f_{1}, f_{2}, \ldots, f_{n}$ defined on an interval $[a, b]$ are said to be linearly independent on $[a, b]$ if the only choice of the constants $c_{1}, c_{2}, \ldots$, $c_{n}$ for which the linear combination $c_{1} f_{1}+c_{2} f_{2}+\cdots+c_{n} f_{n}$ vanishes identically on $[a, b]$ is $c_{1}=c_{2}=\cdots=c_{n}=0$. Otherwise, the functions are said to be linearly dependent.
+
+When $n=2$, we note that linear dependence is equivalent to one function being a constant multiple of the other. The following result shows a connection between the notion of linear independence and fundamental sets.
+
+> [!theorem|e9b1c9b6-7a98-5fe0-a9b9-a4669d1e18ef.local at=a97cae01-9f6e-56a3-bfed-06e078e1c08f] Wronskian Criterion for Linear Independence
+> On an interval $I$, consider $L[y]=y^{(n)}+p_{n-1}(x)y^{(n-1)}+\cdots+p_1(x)y^{\prime}+p_0(x)y$, where $n\geq1$ and every coefficient $p_j$ is continuous.
+>
+> Let $y_{1}, y_{2}, \ldots y_{n}$ be any $n$ solutions to $L[y]=0$ with coefficients continuous on an interval $I$. The following are equivalent:
+> (i) $y_{1}, y_{2}, \ldots, y_{n}$ are linearly independent on $I$;
+> (ii) $y_{1}, y_{2}, \ldots y_{n}$ form a fundamental set of solutions of $L[y]=0$:
+> (iii) $W\left(y_{1}, y_{2}, \ldots, y_{n}\right)\left(x_{0}\right) \neq 0$ for some $x_{0}$ in $I$;
+> (iv) $W\left(y_{1}, y_{2}, \ldots, y_{n}\right)(x) \neq 0$ for all $x$ in $I$.
+
+Proof Clearly (ii) ⇔ (iii) ⇔ (iv) follow from Theorems 2 and 3 and the definition of a fundamental set. We conclude by proving (i) ⇒ (iii) and (iii) ⇒ (i). We start with (iii) ⇒ (i). Suppose that $y_{1}, y_{2}, \ldots, y_{n}$ are any $n$ solutions such that $c_{1} y_{1}+c_{2} y_{2}+\cdots+c_{n} y_{n}=0$. By differentiating this equation $n-1$ times in succession and then setting $x=x_{0}$, we get a system of $n$ linear homogeneous equations in the $n$ unknowns $c_{1}, c_{2}, \ldots, c_{n}$. The determinant of the matrix of this system is precisely $W\left(x_{0}\right)$, which is nonzero by assumption. The nonvanishing of this determinant implies that $c_{1}=c_{2}=\cdots=c_{n}=0$, proving (iii) ⇒ (i). To complete the proof it is enough to show (i) ⇒ (iii). The proof is by contradiction. We assume that $y_{1}, y_{2}, \ldots, y_{n}$ are linearly independent on $I$ and that $W\left(y_{1}, y_{2}, \ldots, y_{n}\right)\left(x_{0}\right)=0$. The vanishing of the Wronskian implies that there are constants $c_{1}, c_{2}, \ldots, c_{n}$. not all zero, such that all the initial values of $y=c_{1} y_{1}+c_{2} y_{2}+\cdots+c_{n} y_{n}$ are 0 at $x_{0}$ (for $n=2$, this fact is clear). However, the solution $w \equiv 0$ has the same initial values, and so by the uniqueness part of Theorem 6, $w \equiv y \equiv 0$, implying that $c_{1}=c_{2}=\cdots =c_{n}=0$ by the definition of linear independence, which is a contradiction.
+
+> [!exercise|a8782957-ca1e-54f5-b773-94a4a9f820a4.local at=aff8bb93-5ec4-5e2b-b3fd-e95a56ae0c76] EXAMPLE 4 Fundamental sets of solutions, linear independence
+> For $y^{\prime\prime}-y=0$, verify that both $\{e^x,e^{-x}\}$ and $\{\cosh x,\sinh x\}$ are fundamental solution sets, and express the general solution in each basis.
+
+##### solution
+
+We saw in Example 2 that $e^{x}$ and $e^{-x}$ are solutions of $y^{\prime \prime}-y=0$ and that $W(e^x,e^{-x})=-2\ne0$. Thus, by Theorem 7. the general solution of the differential equation is of the form $y=c_{1} e^{x}+c_{2} e^{-x}$; and so any solution is a linear combination of the functions $e^x$ and $e^{-x}$, which form a fundamental set of solutions.
+
+It is worthwhile to note that the fundamental set of solutions is not unique. For the equation at hand, you can easily check that $\cosh x$ and $\sinh x$ are also solutions. Their Wronskian is
 
 $$
 W(\cosh x, \sinh x)=\left|\begin{array}{ll}
@@ -279,108 +335,211 @@
 
 Thus far we have developed an understanding of the general form of the solutions of linear differential equations. However, aside from the first order case, we have not developed techniques for finding explicit solutions. This will occupy us throughout the remainder of this appendix, where we will develop methods for solving certain important classes of higher order linear differential equations.
 
-## Exercises A. 1
-
-In Exercises 1-10, solve the given first order differential equation.
-
-1. $y^{\prime}+y=1$.
-2. $y^{\prime}+2 x y=x$.
-3. $y^{\prime}=-.5 y$.
-4. $y^{\prime}=2 y+x$.
-5. $y^{\prime}-y=\sin x$.
-6. $y^{\prime}-2 x y=x^{3}$.
-7. $x y^{\prime}+y=\cos x$.
-8. $y^{\prime}-\frac{2}{x} y=x^{2}$.
-9. $y^{\prime}+\tan x y=\cos x$.
-10. $y^{\prime}+\tan x y=\sec ^{2} x$.
-
-In Exercises 11-20, solve the given initial value problem.
-11. $y^{\prime}=y, y(0)=1$.
-12. $y^{\prime}+2 y=1, y(0)=2$.
-13. $y^{\prime}+x y=x, y(0)=0$.
-14. $y^{\prime}+\frac{y}{x}=\frac{\sin x}{x}, \quad y(\pi)=1$.
-15. $x y^{\prime}+2 y=1, \quad y(-1)=-2$.
-16. $x y^{\prime}-2 y=\frac{1}{x}, y(1)=0$.
-17. $y^{\prime}+y \tan x=\tan x, y(0)=1$.
-18. $y^{\prime}+y \tan x=\tan x, y(0)=2$.
-19. $y^{\prime}+e^{x} y=e^{x}, y(0)=2$.
-20. $y^{\prime}+y=e^{x}, \quad y(3)=0$.
-21. (a) Check that the functions
-
-$$
-e^{x}, e^{-x}, \cosh x, \sinh x
-$$
-
-are solutions of
-
-$$
-y^{\prime \prime}-y=0
-$$
-
-(b) We know from Example 4 that $\left\{e^{x}, e^{-x}\right\}$ and $\{\cosh x, \sinh x\}$ are fundamental sets of solutions. Express $e^{x}$ as a linear combination of the functions $\cosh x, \sinh x$.
-(c) Can you think of other fundamental sets of solutions?
-22. Check that the functions $e^{x}, e^{-x}, \cosh x$ are solutions of
-
-$$
-y^{\prime \prime \prime}-y^{\prime}=0
-$$
-
-(b) Show directly that $W\left(e^{x}, e^{-x}, \cosh x\right) \equiv 0$ and conclude that these functions do not form a fundamental set.
-(c) Find a fundamental set of solutions by inspection. Justify your answer by computing the Wronskian.
-23. (a) Check that the functions $x, x^{2}$ are solutions of
-
-$$
-x^{2} y^{\prime \prime}-2 x y^{\prime}+2 y=0
-$$
-
-(b) Compute the Wronskian of the solutions.
-(c) Note that the Wronskian vanishes at $x=0$. Does this contradict Theorem 2?
-24. (a) Check that the functions $r^{r}, 1+x$ are solutions of
-
-$$
-r y^{\prime \prime}-(1+x) y^{\prime}+y=0
-$$
-
-(b) Check that both of these functions satisfy $y(0)=1$ and $y^{\prime}(0)=1$. Does this contradict the uniqueness part in Theorem 6?
-(c) Compute the Wronskian of the solutions and conclude that they are linearly independent on ( $0, \infty$ ).
-
-In Exercises 25-30, solve the initial value problem consisting of the differential equation in Example 3.
-25. $y(0)=0, y^{\prime}(0)=0$.
-26. $y(0)=1, y^{\prime}(0)=-1$.
-27. $y(1)=0, y^{\prime}(1)=2$.
-28. $y(1)=1, y^{\prime}(1)=-1$.
-[Hint: In Exercises 27 and 28, it is easier to work with $y_{h}=c_{1} e^{(x-1)}+c_{2} c^{2(r-1)}$. Why is this possible?]
-29. $y(2)=0, y^{\prime}(2)=1$.
-30. $y(3)=3, y^{\prime}(3)=3$.
-[Hint: In Exercises 29-30, use a $y_{h}$ that simplifies the computations as in the previous exercises.]
-
-## 31. Project Problem: Abel's formula for $n=3$.
-
-(a) Let $y_{1}, y_{2}, y_{3}$ be any three solutions of the third order equation
-
-$$
-y^{\prime \prime \prime}+p_{2}(x) y^{\prime \prime}+p_{1}(x) y^{\prime}+p_{0}(x) y=0 .
-$$
-
-Derive the formulas for the Wronskian
-
-$$
-W\left(y_{1}, y_{2}, y_{3}\right)=\left(y_{2} y_{3}^{\prime}-y_{2}^{\prime} y_{3}\right) y_{1}^{\prime \prime}-\left(y_{1} y_{3}^{\prime}-y_{1}^{\prime} y_{3}\right) y_{2}^{\prime \prime}+\left(y_{1} y_{2}^{\prime}-y_{1}^{\prime} y_{2}\right) y_{3}^{\prime \prime}
-$$
-
-and
-
-$$
-W^{\prime}\left(y_{1} \cdot y_{2}, y_{3}\right)=\left(y_{2} y_{3}^{\prime}-y_{2}^{\prime} y_{3}\right) y_{1}^{\prime \prime \prime}-\left(y_{1} y_{3}^{\prime}-y_{1}^{\prime} y_{3}\right) y_{2}^{\prime \prime \prime}+\left(y_{1} y_{2}^{\prime}-y_{1}^{\prime} y_{2}\right) y_{3}^{\prime \prime \prime}
-$$
-
-(b) Follow the proof of Theorem 2 to show that
-
-$$
-W^{\prime}=-p_{2}(x) W .
-$$
-
-(c) Derive Abel's formula for $n-3$.
-32. (a) Show that $W\left(x^{3} \cdot\left|x^{3}\right|\right)=0$ for all $x$. (The function $\left|x^{3}\right|$ is differentiable for all $x$. ('an you sed why?)
-(b) Show however, that $x^{3} \cdot\left|x^{3}\right|$ are linearly independent on the real line.
-(c) Does this contradict Theorem 7? Justify your answer.
+## Exercises 10.1
+
+
+> [!prompt|da8bc37e-a2a8-50e9-9261-86ab7fa342cc.local at=3c05692e-8284-59b5-9645-bddb8f783d9d] Shared exercise instructions
+> In Exercises 1-10, solve the given first order differential equation.
+
+
+
+> [!exercise|6dca2e6e-4b94-503b-9b04-24c09deae63d.local at=c7907c60-018c-52c2-9d6e-c6162e67206c] Exercise 1
+> $y^{\prime}+y=1$.
+
+
+> [!exercise|20f9c1da-3e6f-5542-847a-71975d0a5cdd.local at=c0adcc68-bcd1-5a87-96e9-563244cc15e0] Exercise 2
+> $y^{\prime}+2 x y=x$.
+
+
+> [!exercise|2dc9987a-bb0f-53a5-810f-3c2b44621a5d.local at=f81aab5b-d5f6-5573-9306-df9b45a32f75] Exercise 3
+> $y^{\prime}=-.5 y$.
+
+
+> [!exercise|a770aeba-9a8d-5580-8177-4510b3934d2f.local at=6c1b2b28-33a2-5410-8151-2020b26daea4] Exercise 4
+> $y^{\prime}=2 y+x$.
+
+
+> [!exercise|66dc1d30-74de-5651-a1dc-74f7fec3cbdf.local at=82cc061f-ac3e-54e3-879c-c941775396da] Exercise 5
+> $y^{\prime}-y=\sin x$.
+
+
+> [!exercise|e3b37fe5-96c3-5cf9-8f26-7fbc0500c4a5.local at=9637f706-e4ea-5f36-93e8-5e9a05a11e22] Exercise 6
+> $y^{\prime}-2 x y=x^{3}$.
+
+
+> [!exercise|33e2eee4-1ba7-58b4-925a-965babeeb3a8.local at=28df287f-f797-51c2-a5d5-ffb7644acf6b] Exercise 7
+> $x y^{\prime}+y=\cos x$.
+
+
+> [!exercise|5b00492f-1edd-5075-8018-e96379689e21.local at=9d898a41-e583-5d77-b40b-53a98ceb227e] Exercise 8
+> $y^{\prime}-\frac{2}{x} y=x^{2}$.
+
+
+> [!exercise|2cdba820-2afc-56c5-b92c-a0830164cd03.local at=9c5dc521-1bcb-503a-92c0-2d2e977034d3] Exercise 9
+> $y^{\prime}+\tan x y=\cos x$.
+
+
+> [!exercise|2a71f77f-7df4-5680-bee1-6263ad461af4.local at=44d7e716-5687-5bf8-ace8-9df861338b2e] Exercise 10
+> $y^{\prime}+\tan x y=\sec ^{2} x$.
+
+
+> [!prompt|45e3417c-93c9-5bc0-b7a4-c34081efb930.local at=d7ffff46-24b0-55d7-a6d4-b3cf43aff720] Shared exercise instructions
+> In Exercises 11-20, solve the given initial value problem.
+
+
+
+> [!exercise|c1e54998-acb4-5472-968b-a1dca798ba64.local at=64a39c88-0ec4-5c24-9005-39cda3fa6271] Exercise 11
+> $y^{\prime}=y, y(0)=1$.
+
+
+> [!exercise|8d38d9c6-d99b-58ac-82c3-27a3ef7b77a1.local at=2f9ccc63-e72a-5a89-b5dc-2e41654e67de] Exercise 12
+> $y^{\prime}+2 y=1, y(0)=2$.
+
+
+> [!exercise|3da67f54-f440-5484-a70b-82d4c86dce7d.local at=d5e41dc6-d847-504c-a24a-f0a3a2494965] Exercise 13
+> $y^{\prime}+x y=x, y(0)=0$.
+
+
+> [!exercise|856470bb-8282-5cab-a4a8-481257ce97df.local at=822bc4d4-061e-5ee2-a66b-f859568c8b65] Exercise 14
+> $y^{\prime}+\frac{y}{x}=\frac{\sin x}{x}, \quad y(\pi)=1$.
+
+
+> [!exercise|4501ce9b-063b-5f6d-8148-4fe63d53e7ed.local at=cdbdbec8-4720-5d4d-8ccb-319e2c542787] Exercise 15
+> $x y^{\prime}+2 y=1, \quad y(-1)=-2$.
+
+
+> [!exercise|2527aed7-77b2-5657-85f7-2cd9e3696971.local at=48368aee-76ce-5f7d-89e2-25105595ce5c] Exercise 16
+> $x y^{\prime}-2 y=\frac{1}{x}, y(1)=0$.
+
+
+> [!exercise|c28ec70c-74d0-5dd0-904d-ecc1266c9377.local at=7fd90e07-31e6-5384-96d7-63e9372d221e] Exercise 17
+> $y^{\prime}+y \tan x=\tan x, y(0)=1$.
+
+
+> [!exercise|7ff63757-3227-5abf-b17c-4c41ce5a6b94.local at=609734ab-5319-5008-a331-4774ae7686cd] Exercise 18
+> $y^{\prime}+y \tan x=\tan x, y(0)=2$.
+
+
+> [!exercise|7e7ab4cd-7857-55e1-a72e-e921c361643f.local at=aab04f5d-a295-5377-8914-4595c4297613] Exercise 19
+> $y^{\prime}+e^{x} y=e^{x}, y(0)=2$.
+
+
+> [!exercise|d40194f9-9538-5bdb-8bbf-28c56cda2243.local at=62696896-25ae-5889-b8a8-54913ff74af8] Exercise 20
+> $y^{\prime}+y=e^{x}, \quad y(3)=0$.
+
+
+> [!exercise|b228fc75-6b16-5d81-ab48-699e1861dc0c.local at=f6b3aa9c-601d-58d9-b035-bc2ccb370842] Exercise 21
+> (a) Check that the functions
+>
+> $$
+> e^{x}, e^{-x}, \cosh x, \sinh x
+> $$
+>
+> are solutions of
+>
+> $$
+> y^{\prime \prime}-y=0
+> $$
+>
+> (b) We know from Example 4 that $\left\{e^{x}, e^{-x}\right\}$ and $\{\cosh x, \sinh x\}$ are fundamental sets of solutions. Express $e^{x}$ as a linear combination of the functions $\cosh x, \sinh x$.
+> (c) Can you think of other fundamental sets of solutions?
+
+
+> [!exercise|e5dbe3ca-e4ee-5560-8cea-e1859b39f64c.local at=cc9bc4f0-e967-5dc6-8101-ebd68f1cc521] Exercise 22
+> (a) Check that the functions $e^{x}, e^{-x}, \cosh x$ are solutions of
+>
+> $$
+> y^{\prime \prime \prime}-y^{\prime}=0
+> $$
+>
+> (b) Show directly that $W\left(e^{x}, e^{-x}, \cosh x\right) \equiv 0$ and conclude that these functions do not form a fundamental set.
+> (c) Find a fundamental set of solutions by inspection. Justify your answer by computing the Wronskian.
+
+
+> [!exercise|158a8fbb-f213-5438-ae8f-05ab80ccc5b0.local at=ac13110a-35ff-5bd5-abfb-f7e46e94ad70] Exercise 23
+> (a) Check that the functions $x, x^{2}$ are solutions of
+>
+> $$
+> x^{2} y^{\prime \prime}-2 x y^{\prime}+2 y=0
+> $$
+>
+> (b) Compute the Wronskian of the solutions.
+> (c) Note that the Wronskian vanishes at $x=0$. Does this contradict Theorem 2?
+
+
+> [!exercise|ef2938af-ffbd-5ca1-8f79-4e0fb44632fa.local at=d0b2b124-ac59-5bee-a8cc-10fd46a9a0d9] Exercise 24
+> (a) Check that the functions $e^x,1+x$ are solutions of
+>
+> $$
+> x y^{\prime \prime}-(1+x) y^{\prime}+y=0
+> $$
+>
+> (b) Check that both of these functions satisfy $y(0)=1$ and $y^{\prime}(0)=1$. Does this contradict the uniqueness part in Theorem 6?
+> (c) Compute the Wronskian of the solutions and conclude that they are linearly independent on ( $0, \infty$ ).
+
+
+> [!prompt|407e9a17-ebe6-5309-8cec-cc36cb85ed9e.local at=8bad2726-38bf-541b-a118-06ff51c014a1] Shared exercise instructions
+> In Exercises 25-30, solve the initial value problem consisting of the differential equation in Example 3.
+
+
+
+> [!exercise|be7a0f51-d9f4-5201-8e01-b0d8dcc669da.local at=37a999c2-abfc-52ed-b0cd-4469f341024b] Exercise 25
+> $y(0)=0, y^{\prime}(0)=0$.
+
+
+> [!exercise|0f54a395-2e66-56cc-94f0-df9986b6ddfc.local at=d5f8ac9a-ab44-5f27-9b8c-6e92237caa18] Exercise 26
+> $y(0)=1, y^{\prime}(0)=-1$.
+
+
+> [!exercise|ba0fb33a-fd53-553d-b495-016f80484fc6.local at=272fe7a7-cbb4-5107-867b-3cf04064ab8c] Exercise 27
+> $y(1)=0, y^{\prime}(1)=2$.
+
+
+> [!exercise|b19a3344-182f-5edc-b82c-915339e4195b.local at=2ff70c2c-1056-5b46-b02d-7258d7312c5d] Exercise 28
+> $y(1)=1, y^{\prime}(1)=-1$.
+> [Hint: In Exercises 27 and 28, it is easier to work with $y_{h}=c_{1} e^{(x-1)}+c_2e^{2(x-1)}$. Why is this possible?]
+
+
+> [!exercise|c4b781db-ca0a-503c-b2b9-1dafc1c7d6e1.local at=6694c228-2f3b-52c1-85eb-5ef109ba7157] Exercise 29
+> $y(2)=0, y^{\prime}(2)=1$.
+
+
+> [!exercise|47c7c614-d3cc-5f07-acfe-5d9ba7328184.local at=44b55002-8815-5e58-8da5-653bc5f5335b] Exercise 30
+> $y(3)=3, y^{\prime}(3)=3$.
+> [Hint: In Exercises 29-30, use a $y_{h}$ that simplifies the computations as in the previous exercises.]
+
+
+> [!exercise|af45bd1d-ce87-5141-a17c-59883301543f.local at=cd6eb15f-2330-5f81-b6b9-a5553b039156] Exercise 31
+> Project Problem: Abel's formula for $n=3$.
+>
+> (a) Let $y_{1}, y_{2}, y_{3}$ be any three solutions of the third order equation
+>
+> $$
+> y^{\prime \prime \prime}+p_{2}(x) y^{\prime \prime}+p_{1}(x) y^{\prime}+p_{0}(x) y=0 .
+> $$
+>
+> Derive the formulas for the Wronskian
+>
+> $$
+> W\left(y_{1}, y_{2}, y_{3}\right)=\left(y_{2} y_{3}^{\prime}-y_{2}^{\prime} y_{3}\right) y_{1}^{\prime \prime}-\left(y_{1} y_{3}^{\prime}-y_{1}^{\prime} y_{3}\right) y_{2}^{\prime \prime}+\left(y_{1} y_{2}^{\prime}-y_{1}^{\prime} y_{2}\right) y_{3}^{\prime \prime}
+> $$
+>
+> and
+>
+> $$
+> W^{\prime}\left(y_1,y_2,y_3\right)=\left(y_{2} y_{3}^{\prime}-y_{2}^{\prime} y_{3}\right) y_{1}^{\prime \prime \prime}-\left(y_{1} y_{3}^{\prime}-y_{1}^{\prime} y_{3}\right) y_{2}^{\prime \prime \prime}+\left(y_{1} y_{2}^{\prime}-y_{1}^{\prime} y_{2}\right) y_{3}^{\prime \prime \prime}
+> $$
+>
+> (b) Follow the proof of Theorem 2 to show that
+>
+> $$
+> W^{\prime}=-p_{2}(x) W .
+> $$
+>
+> (c) Derive Abel's formula for $n=3$.
+
+
+> [!exercise|0ed88607-03de-5c9b-a393-2cc028c4b33c.local at=8ea0ae74-2214-5cfe-b13b-5ebcf6e0c51c] Exercise 32
+> (a) Show that $W\left(x^3,|x^3|\right)=0$ for all $x$. (The function $\left|x^{3}\right|$ is differentiable for all $x$. (Can you see why?))
+> (b) Show however, that $x^3$ and $|x^3|$ are linearly independent on the real line.
+> (c) Does this contradict Theorem 7? Justify your answer.

`````
