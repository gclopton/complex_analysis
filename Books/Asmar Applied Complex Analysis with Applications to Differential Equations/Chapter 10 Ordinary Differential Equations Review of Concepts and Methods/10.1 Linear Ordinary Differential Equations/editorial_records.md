
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
