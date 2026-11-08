
# Editorial records

Reading note: 14.1 Orthogonal Functions.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Restore source wording; retain only the actual correction.

### Before

````text
In defining the inner product of two vectors, we summed products of components. For functions, integration plays the corresponding role. We require square integrability; on an unbounded interval, piecewise continuity alone does not ensure that the integrals are finite.
````
### After

````text
In defining the inner product of two vectors, we summed the products of their components. To define the inner product of two functions, we will integrate their product as follows.
````

## 2. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!definition] Inner Product and Norm of Square-Integrable Functions
> Let $I=(a,b)$, allowing infinite endpoints. For real or complex functions $f,g\in L^2(I)$, define
>
> $$
> (f,g)=\int_a^b f(x)\overline{g(x)}\,dx,
> \qquad \|f\|_2=\left(\int_a^b |f(x)|^2\,dx\right)^{1/2}.
> $$
>
> For real functions the conjugate can be omitted. The inner product is linear in its first argument. Functions equal almost everywhere represent the same element of $L^2(I)$.
````
### After

````text
> [!definition] Inner Product and Norm of Square-Integrable Functions
> Let $f$ and $g$ be real-valued, square integrable functions defined on an interval $(a,b)$ (the interval may be infinite). The inner product of $f$ and $g$, denoted $(f,g)$, is the number
> $$
> (f,g)=\int_a^b f(x)g(x)\,dx.
> $$
> If $f$ and $g$ are complex-valued, then define
> $$
> (f,g)=\int_a^b f(x)\overline{g(x)}\,dx.
> $$
> We define the norm of $f$, denoted $\|f\|$, by
> $$
> \|f\|=\sqrt{(f,f)}=\left(\int_a^b|f(x)|^2\,dx\right)^{1/2}.
> $$
> If $\|f\|<\infty$, we also say that $f$ is square integrable on $(a,b)$.
````

## 3. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!definition] Orthogonal and Orthonormal Systems of Functions
> In $L^2(I)$ with inner product $(f,g)=\int_I f(x)\overline{g(x)}\,dx$, two functions are orthogonal when $(f,g)=0$. A system $\{f_n\}$ is orthogonal when $\|f_n\|_2>0$ for every $n$ and $(f_n,f_m)=0$ whenever $n\ne m$. It is orthonormal when, in addition, $\|f_n\|_2=1$ for every $n$. Dividing each member of an orthogonal system by its norm produces an orthonormal system.
````
### After

````text
> [!definition] Orthogonal Functions
> The functions $f$ and $g$ are called orthogonal on the interval $(a,b)$ if $(f,g)=0$.
>
> A set of functions $\left\{f_{1}, f_{2}, f_{3}, \ldots\right\}$ defined on the interval ( $a, b$ ) is called an orthogonal set if $\left\|f_{n}\right\| \neq 0$ for all $n$, and each distinct pair of functions from the set is orthogonal, that is, $\left(f_{n}, f_{m}\right)=$ 0 for $n \neq m$. If, in addition, the norm of each $f_{n}$ is 1 , the set is called an orthonormal set. Hence, if we divide each function in an orthogonal set by its norm we obtain an orthonormal set.
>
> Here $(f,g)=\int_a^b f(x)\overline{g(x)}\,dx$ and $\|f\|^2=(f,f)$.
````

## 4. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem] Coefficients of an Orthogonal Function Expansion
> Let $\{f_j\}_{j\ge1}$ be a nonzero orthogonal system in $L^2(I)$, with $(f,g)=\int_I f\overline g\,dx$. If $f=\sum_{j=1}^\infty a_jf_j$ with convergence in $L^2(I)$, then
>
> $$
> a_j=\frac{(f,f_j)}{\|f_j\|_2^2},
> \qquad f=\sum_{j=1}^\infty\frac{(f,f_j)}{\|f_j\|_2^2}f_j.
> $$
>
> The latter series is the generalized Fourier series of $f$ in this orthogonal system.
````
### After

````text
> [!theorem] Generalized Fourier Series
> If $f_{1}, f_{2}, f_{3}, \ldots$ is a set of orthogonal functions on $(a, b)$ and if $f$ can be represented as a series $f=\sum_{j=1}^\infty a_jf_j$ convergent in mean square, then
>
> $$
> f(x)=\sum_{j=1}^{\infty} \frac{\left(f, f_{j}\right)}{\left\|f_{j}\right\|^{2}} f_{j}(x)
> $$
>
> Here $(f,g)=\int_a^b f(x)\overline{g(x)}\,dx$ and $\|f\|^2=(f,f)$.
````

## 5. Restore source wording; retain only the actual correction.

### Before

````text
We now turn to the first question. Infinite-dimensional expansions require a specified notion of convergence. The natural setting for these inner products is mean-square convergence in $L^2$.
````
### After

````text
We now turn to the first question. Again, we take a hint from the three-dimensional real vector space.
````

## 6. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!definition] Completeness of an Orthogonal System in a Hilbert Space
> An orthogonal system $\{f_j\}$ in a Hilbert space $H$ is complete if the only element orthogonal to every $f_j$ is the zero element. Equivalently, the closure of its linear span is $H$. For $H=L^2(I)$, the zero element means a function that vanishes almost everywhere.
````
### After

````text
> [!definition] Completeness of an Orthogonal System in a Hilbert Space
> A set of orthogonal square integrable functions $f_1,f_2,f_3,\ldots$ forms a complete set in the following sense: If $f$ is orthogonal to every $f_j$, $j=1,2,3,\ldots$, then $f$ must be zero almost everywhere.
>
> Here $(f,g)=\int_a^b f(x)\overline{g(x)}\,dx$ and $\|f\|^2=(f,f)$.
````

## 7. Restore source wording; retain only the actual correction.

### Before

````text
For the trigonometric system on $[-\pi,\pi]$, completeness means that a square-integrable function with all Fourier coefficients zero is zero almost everywhere. For a piecewise smooth function, the pointwise Fourier theorem yields zero at every point of continuity and zero for the average of the one-sided limits at each jump. Values assigned at isolated points do not change the Fourier coefficients. A continuous function with all coefficients zero is identically zero.
````
### After

````text
In the case of Fourier series on the interval $[-\pi, \pi]$, the functions $1, \cos x$, $\cos 2 x, \cos 3 x, \ldots, \cos n x, \ldots, \sin x, \sin 2 x, \sin 3 x, \ldots, \sin n x, \ldots$ form an orthogonal set of functions on $[-\pi, \pi]$. By the Fourier series representation theorem, this set also generates the class $A$ of $2 \pi$-periodic, piecewise smooth functions. What does completeness mean in this case? It means that if all the Fourier coefficients of a function $f$ are zero, then $f$ must be zero at every point of continuity. This fact follows from the Fourier series representation theorem, since

if we set all the coefficients of $f$ equal to 0 , then the Fourier series of $f$ is identically 0 . But the Fourier series converges to $f$ at points of continuity, and so $f$ must be zero there.
````

## 8. Restore source wording; retain only the actual correction.

### Before

````text
These notions extend to weighted inner products, as in Bessel expansions. The weights used here are nonnegative and piecewise continuous, and are not identically zero on any subinterval.
````
### After

````text
What we have presented thus far can be extended to functions that are orthogonal with respect to a weight function. We have encountered such situations in the study of Bessel series.
````

## 9. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!definition] Weighted Inner Product, Norm, and Orthogonality of Functions
> Let $w\ge0$ be a measurable weight on an interval $I$, and consider functions with $\int_I|f|^2w\,dx<\infty$. In $L^2(I,w\,dx)$, functions equal almost everywhere with respect to the measure $w\,dx$ are identified. Define
>
> $$
> (f,g)_w=\int_I f(x)\overline{g(x)}w(x)\,dx,
> \qquad \|f\|_w=\left(\int_I|f(x)|^2w(x)\,dx\right)^{1/2}.
> $$
>
> Functions $f,g$ are orthogonal with respect to $w$ if $(f,g)_w=0$. An orthogonal system has nonzero norm for each member and mutually orthogonal distinct members. It is orthonormal if every member has norm one.
````
### After

````text
> [!definition] Orthogonality with Respect to a Weight
> In general, if $f$ and $g$ are real-valued square integrable functions with respect to $w$ on $(a, b)$, we define their inner product with respect to the weight $\boldsymbol{w}$ to be the number
>
> $$
> (f, g)=\int_{a}^{b} f(x) g(x) w(x) d x
> $$
>
> We assume that $w(x)$ is a nonnegative piecewise continuous function on $[a, b]$ that is not identically 0 on any subinterval of $[a, b]$. The corresponding definition of orthogonality is as follows.
>
> The functions $f$ and $g$ are orthogonal with respect to the weight function $w$ on the interval $[a, b]$ if
>
> $$
> \int_{a}^{b} f(x) g(x) w(x) d x=0
> $$
>
> The norm of $f$ with respect to the weight function $w$ is
>
> $$
> \|f\|=\left(\int_{a}^{b}|f(x)|^{2} w(x) d x\right)^{1 / 2}
> $$
````

## 10. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem] Coefficients of a Weighted Orthogonal Function Expansion
> Let $\{f_j\}_{j\ge1}$ be a nonzero orthogonal system in $L^2(I,w\,dx)$ for a nonnegative weight $w$. Write $(f,g)_w=\int_I f\overline g\,w\,dx$ and $\|f\|_w^2=(f,f)_w$. If $f=\sum_{j=1}^\infty a_jf_j$ with convergence in this weighted norm, then
>
> $$
> a_j=\frac{(f,f_j)_w}{\|f_j\|_w^2},
> \qquad f=\sum_{j=1}^\infty\frac{(f,f_j)_w}{\|f_j\|_w^2}f_j.
> $$
````
### After

````text
> [!theorem] Generalized Fourier Series
> If $f_{1}, f_{2}, f_{3}, \ldots$ is a set of orthogonal functions with respect to the weight $w$ on $[a, b]$ and if $f$ can be represented as a series $f=\sum_{j=1}^\infty a_jf_j$ convergent in weighted mean square, then
>
> $$
> f(x)=\sum_{j=1}^{\infty} \frac{\left(f, f_{j}\right)}{\left\|f_{j}\right\|^{2}} f_{j}(x)
> $$
>
> Here $(f,g)=\int_a^b f(x)\overline{g(x)}w(x)\,dx$ and $\|f\|^2=(f,f)$, with a nonnegative piecewise continuous weight $w$ that is not identically zero on any subinterval.
````

## 11. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem] Parseval Identity for a Complete Weighted Orthogonal System
> Let $\{f_j\}_{j\ge1}$ be a complete nonzero orthogonal system in $L^2(I,w\,dx)$, where $w\ge0$. With $(f,g)_w=\int_I f\overline g\,w\,dx$ and $\|f\|_w^2=(f,f)_w$, every $f\in L^2(I,w\,dx)$ satisfies
>
> $$
> \int_I|f(x)|^2w(x)\,dx
> =\sum_{j=1}^\infty\frac{|(f,f_j)_w|^2}{\|f_j\|_w^2}.
> $$
````
### After

````text
> [!theorem] Parseval's Identity
> Let $f_{1}, f_{2}, f_{3}, \ldots$ be a complete set of orthogonal functions with respect to the weight $w$ on $[a, b]$ and let $f$ be such that its norm with respect to $w$ is finite. (That is, $f$ is square integrable with respect to the weight $w$.) Then
>
> $$
> \int_{a}^{b}|f(x)|^{2} w(x) d x=\sum_{j=1}^{\infty} \frac{\left|\left(f, f_{j}\right)\right|^{2}}{\left\|f_{j}\right\|^{2}}
> $$
>
> Here $(f,g)=\int_a^b f(x)\overline{g(x)}w(x)\,dx$ and $\|f\|^2=(f,f)$, with a nonnegative piecewise continuous weight $w$ that is not identically zero on any subinterval.
````

## 12. Move correction/commentary into the separate editorial record; keep the actual correction in the reading text.

### Before

````text
[Source correction: Exercise 8 is not an orthogonal pair as printed. Its functions and weight are retained; the instruction is changed from proving orthogonality to checking it.]
````
### After

````text

````
