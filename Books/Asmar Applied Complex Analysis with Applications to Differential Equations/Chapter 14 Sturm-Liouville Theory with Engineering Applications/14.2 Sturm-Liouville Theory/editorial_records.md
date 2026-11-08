
# Editorial records

Reading note: 14.2 Sturm-Liouville Theory.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!definition|805bda36-235a-5169-9a2a-98b17eeb0c50.local at=8918ebfe-774e-5419-b917-6a9b41241c57] Regular Sturm–Liouville Problem with Separated Boundary Conditions
> Let $a<b$ be finite, $p\in C^1[a,b]$, and $q,r\in C[a,b]$ be real, with $p>0$ and $r>0$. Consider
>
> $$
> (py')'+(q+\lambda r)y=0,\qquad
> c_1y(a)+c_2y'(a)=0,\quad d_1y(b)+d_2y'(b)=0,
> $$
>
> where the boundary coefficients are real, $(c_1,c_2)\ne(0,0)$, and $(d_1,d_2)\ne(0,0)$.
>
> This boundary value problem is a regular Sturm–Liouville problem. A value of $\lambda$ admitting a nonzero solution is an eigenvalue, and such a solution is an eigenfunction.
````
### After

````text
> [!definition|805bda36-235a-5169-9a2a-98b17eeb0c50.local at=8918ebfe-774e-5419-b917-6a9b41241c57] Regular Sturm-Liouville Problem
> A regular Sturm-Liouville problem is a boundary value problem on a closed finite interval $[a, b]$ of the form
>
> $$
> \begin{aligned}
> & {\left[p(x) y^{\prime}\right]^{\prime}+[q(x)+\lambda r(x)] y=0, \quad a<x<b} \\
> & \text { (a) }\left\{\begin{array}{c}
> c_{1} y(a)+c_{2} y^{\prime}(a)=0 \\
> d_{1} y(b)+d_{2} y^{\prime}(b)=0
> \end{array}\right.
> \end{aligned}
> $$
>
> where all coefficients are real, at least one of $c_{1}$ and $c_{2}$ and at least one of $d_{1}$ and $d_{2}$ are nonzero, and $\lambda$ is a parameter. The differential equation is said to be in Sturm-Liouville form. We further assume the regularity conditions: $p(x), p^{\prime}(x), q(x)$, and $r(x)$ are continuous on the closed interval $a \leq x \leq b$, with $p(x)>0$ and $r(x)>0$ for $a \leq x \leq b$.
````

## 2. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!definition|56de0eb2-bd59-5c60-bcac-93664c7073f9.local at=f989c2af-ea26-5bc3-9ccf-f756a65490e0] Singular Sturm–Liouville Problem
> Consider $(py')'+(q+\lambda r)y=0$ on an interval $(a,b)$, with real coefficients, $p\in C^1(a,b)$, $q,r\in C(a,b)$, and $p,r>0$ in the interior. The problem is singular if an endpoint is infinite or the regular endpoint conditions on the coefficients fail. Appropriate boundary or endpoint admissibility conditions, such as boundedness, are part of the problem and depend on the singular endpoint.
````
### After

````text
> [!definition|56de0eb2-bd59-5c60-bcac-93664c7073f9.local at=f989c2af-ea26-5bc3-9ccf-f756a65490e0] Singular Sturm–Liouville Problem
> A singular Sturm-Liouville problem is a boundary value problem consisting of $(py')'+(q+\lambda r)y=0$ either on a finite interval where at least one of the regularity properties fails or on an infinite interval. In this case the boundary conditions are not always described by sets of equations like $c_1y(a)+c_2y'(a)=0$ and $d_1y(b)+d_2y'(b)=0$. Typically, a Sturm-Liouville problem is singular either because it occurs on an infinite interval, or because one or more of the coefficients goes to 0 or $\infty$ at an endpoint of the interval, or both. Indeed, it is convenient to require that $p(x), p^{\prime}(x), q(x)$, and $r(x)$ are continuous on the open interval $a<x<b$, with $p(x)>0$ and $r(x)>0$ for $a<x<b$.
````

## 3. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|61c35791-6311-5925-97b4-7fa5400e592a.local at=f895caa3-0a82-5476-a777-7964874444e1] Real Discrete Spectrum of a Regular Separated Sturm–Liouville Problem
> Let $a<b$ be finite, $p\in C^1[a,b]$, and $q,r\in C[a,b]$ be real, with $p>0$ and $r>0$. Consider
>
> $$
> (py')'+(q+\lambda r)y=0,\qquad
> c_1y(a)+c_2y'(a)=0,\quad d_1y(b)+d_2y'(b)=0,
> $$
>
> where the boundary coefficients are real, $(c_1,c_2)\ne(0,0)$, and $(d_1,d_2)\ne(0,0)$.
>
> Its eigenvalues are real and can be ordered as a strictly increasing sequence $\lambda_1<\lambda_2<\cdots$ with $\lambda_j\to+\infty$.
````
### After

````text
> [!theorem|61c35791-6311-5925-97b4-7fa5400e592a.local at=f895caa3-0a82-5476-a777-7964874444e1] Eigenvalues of Regular Sturm-Liouville Problems
> Let $a<b$ be finite, with real $p\in C^1[a,b]$, $q,r\in C[a,b]$, and $p,r>0$. The regular Sturm–Liouville problem is $(py')'+(q+\lambda r)y=0$, with real separated boundary conditions $c_1y(a)+c_2y'(a)=0$, $d_1y(b)+d_2y'(b)=0$, where neither coefficient pair is zero.
>
> The eigenvalues of a regular Sturm-Liouville problem are all real and form an increasing sequence
>
> $$
> \lambda_{1}<\lambda_{2}<\lambda_{3}<\cdots
> $$
>
> where $\lambda_{j} \rightarrow \infty$ as $j \rightarrow \infty$.
````

## 4. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!property|9d63ccb8-773a-5f08-9aac-aef50c8976b2.local at=abc50dbe-ec5f-50e5-b5c6-79eeb9d6d04e] Vanishing Boundary Form and Sturm–Liouville Orthogonality
> Let real functions $y_1,y_2$ solve $(py_j')'+(q+\lambda_jr)y_j=0$ on $(a,b)$ for distinct real parameters $\lambda_1,\lambda_2$, where $p\in C^1$, $q,r$ are continuous and real, and $p,r>0$ in the interior. Assume $y_1,y_2\in L^2((a,b),r\,dx)$ and the endpoint limits below exist. If
>
> $$
> \lim_{x\uparrow b}p(x)(y_1y_2'-y_2y_1')
> -\lim_{x\downarrow a}p(x)(y_1y_2'-y_2y_1')=0,
> $$
>
> then $\int_a^b y_1(x)y_2(x)r(x)\,dx=0$.
````
### After

````text
> [!property|9d63ccb8-773a-5f08-9aac-aef50c8976b2.local at=abc50dbe-ec5f-50e5-b5c6-79eeb9d6d04e] Condition for Orthogonality in Singular Sturm-Liouville Problems
> Let real functions $y_1,y_2$ solve $(py_j')'+(q+\lambda_jr)y_j=0$ on $(a,b)$ for distinct real parameters $\lambda_1,\lambda_2$, where $p\in C^1$, $q,r$ are continuous and real, and $p,r>0$ in the interior. Assume $y_1,y_2\in L^2((a,b),r\,dx)$ and the endpoint limits below exist. If
>
> $$
> \lim_{x\uparrow b}p(x)(y_1y_2'-y_2y_1')
> -\lim_{x\downarrow a}p(x)(y_1y_2'-y_2y_1')=0,
> $$
>
> then $\int_a^b y_1(x)y_2(x)r(x)\,dx=0$.
````

## 5. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|d47be7bf-422c-5bf2-adb7-8da618a5954a.local at=6572f4b5-3e07-592c-be0b-5f9a7b965356] Simplicity and Orthogonality for Regular Separated Sturm–Liouville Problems
> Let $a<b$ be finite, $p\in C^1[a,b]$, and $q,r\in C[a,b]$ be real, with $p>0$ and $r>0$. Consider
>
> $$
> (py')'+(q+\lambda r)y=0,\qquad
> c_1y(a)+c_2y'(a)=0,\quad d_1y(b)+d_2y'(b)=0,
> $$
>
> where the boundary coefficients are real, $(c_1,c_2)\ne(0,0)$, and $(d_1,d_2)\ne(0,0)$.
>
> Each eigenvalue has a one-dimensional eigenspace. Eigenfunctions for distinct eigenvalues are orthogonal in $L^2((a,b),r\,dx)$:
>
> $$
> \int_a^b y_j(x)\overline{y_k(x)}r(x)\,dx=0\qquad(\lambda_j\ne\lambda_k).
> $$
````
### After

````text
> [!theorem|d47be7bf-422c-5bf2-adb7-8da618a5954a.local at=6572f4b5-3e07-592c-be0b-5f9a7b965356] Simplicity and Orthogonality for Regular Separated Sturm–Liouville Problems
> Let $a<b$ be finite, with real $p\in C^1[a,b]$, $q,r\in C[a,b]$, and $p,r>0$. The regular Sturm–Liouville problem is $(py')'+(q+\lambda r)y=0$, with real separated boundary conditions $c_1y(a)+c_2y'(a)=0$, $d_1y(b)+d_2y'(b)=0$, where neither coefficient pair is zero.
>
> (a) Each eigenvalue of a regular Sturm-Liouville problem has just one linearly independent eigenfunction corresponding to it.
> (b) Eigenfunctions corresponding to different eigenvalues of a regular Sturm-Liouville problem are orthogonal with respect to the weight function $r(x)$. This assertion is also valid for singular Sturm-Liouville problems when the endpoint boundary form $[p(y_1y_2^{\prime}-y_2y_1^{\prime})]_a^b$ vanishes and the weighted inner product exists.
````

## 6. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|9fd91445-18fe-55d1-9aaa-1205e1e63c0d.local at=3a24cf97-788d-544f-8042-dca7da7b4f8f] Eigenfunction Expansion for a Regular Separated Sturm–Liouville Problem
> Let $a<b$ be finite, $p\in C^1[a,b]$, and $q,r\in C[a,b]$ be real, with $p>0$ and $r>0$. Consider
>
> $$
> (py')'+(q+\lambda r)y=0,\qquad
> c_1y(a)+c_2y'(a)=0,\quad d_1y(b)+d_2y'(b)=0,
> $$
>
> where the boundary coefficients are real, $(c_1,c_2)\ne(0,0)$, and $(d_1,d_2)\ne(0,0)$.
>
> Choose one real nonzero eigenfunction $y_j$ for each eigenvalue, in increasing eigenvalue order. These eigenfunctions form a complete orthogonal system in $L^2((a,b),r\,dx)$. For $f$ in that space, its expansion converges in the weighted $L^2$ norm and has coefficients
>
> $$
> f=\sum_{j=1}^\infty A_jy_j,\qquad
> A_j=\frac{\int_a^b f(x)y_j(x)r(x)\,dx}{\int_a^b y_j(x)^2r(x)\,dx}.
> $$
>
> If $f$ is piecewise smooth on $[a,b]$, the series converges at each interior point to $[f(x+)+f(x-)]/2$, and hence to $f(x)$ at every interior point of continuity.
````
### After

````text
> [!theorem|9fd91445-18fe-55d1-9aaa-1205e1e63c0d.local at=3a24cf97-788d-544f-8042-dca7da7b4f8f] Eigenfunction Expansions
> Let $a<b$ be finite, with real $p\in C^1[a,b]$, $q,r\in C[a,b]$, and $p,r>0$. The regular Sturm–Liouville problem is $(py')'+(q+\lambda r)y=0$, with real separated boundary conditions $c_1y(a)+c_2y'(a)=0$, $d_1y(b)+d_2y'(b)=0$, where neither coefficient pair is zero.
>
> Let $y_{1}, y_{2}, y_{3}, \ldots$ be the collection of eigenfunctions for a regular Sturm-Liouville problem on an interval $[a, b]$. If $f$ is piecewise smooth on the interval $[a, b]$, then we have $f(x)=\sum_{j=1}^{\infty} A_{j} y_{j}(x)$, where
>
> $$
> A_{j}=\frac{\left(f, y_{j}\right)}{\left\|y_{j}\right\|^{2}}=\int_{a}^{b} f(x) y_{j}(x) r(x) d x / \int_{a}^{b} y_{j}^{2}(x) r(x) d x
> $$
>
> For $a<x<b$, the series converges to $f(x)$ if $f$ is continuous at $x$, and to $\frac{f(x+)+f(x-)}{2}$ otherwise.
````

## 7. Preserve the source limitation/correction history in the editorial record only.

### Before

````text
[Source corrections: Exercise 32 needs the stated $n=0$ exception. In Exercise 36, the arguments of $h$ and the omitted factor $\lambda$ in part (c) are corrected to agree with its definition.]
````
### After

````text

````
