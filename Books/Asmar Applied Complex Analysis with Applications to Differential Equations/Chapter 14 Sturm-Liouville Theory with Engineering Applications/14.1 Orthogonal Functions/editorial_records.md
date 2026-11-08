
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

## Additional source comparison

## 1. Restore omitted author explanation outside the reusable definitions; qualify the finite-interval integrability example.

### Before

````text

````
### After

````text
This terminology is the same as for the inner product of vectors because the function ( $\cdot, \cdot$ ) defined in (3) satisfies the same properties as the inner product of vectors (see Exercise 21). We will assume that the functions are real-valued and nice enough that all integrals of the form (3) exist. This is for example the case on a finite interval if the functions are piecewise continuous and bounded.

If $f$ is real-valued, then $|f(x)|^2$ is simply $f^2(x)$. But if $f$ is complex-valued, then $|f(x)|^2=f(x)\overline{f(x)}$. Note how both definitions, orthogonality and norm, are based on the notion of inner products as they were in the finite-dimensional case. (Compare with (2).)
````

## Source-to-current comparison

Source: /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 14 Sturm-Liouville Theory with Engineering Applications/14.1 Orthogonal Functions.md

This exact comparison preserves the full change evidence, including formatting, OCR corrections, restored source wording, and required standalone context. The entries above explain the recovery edits. The comparison is not a claim that every difference is a correction; component serialization, callout wrapping, and printed labels outside callouts are formatting.

`````diff
--- /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 14 Sturm-Liouville Theory with Engineering Applications/14.1 Orthogonal Functions.md
+++ /Users/gradyclopton/ObsidianVaults/complex_analysis/Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 14 Sturm-Liouville Theory with Engineering Applications/14.1 Orthogonal Functions.md
@@ -1,10 +1,11 @@
+
 ## Topics to Review
 
-In studying this chapter, it will help to keep in mind some specific examples of orthogonal functions and their associated expansion theory. For example, you might use Fourier series or Bessel expansions as your basis for comparison. Sections 6.1, 6.2, and 6.4 are self-contained. Sections 14.1 and 14.2 develop the general subject of Sturn-Liouville theory for boundary value problems associated with second order linear ordinary differential equations. Section 14.4 develops a corresponding theory for certain fourth-order problems. In Sections 14.3 and 14.5 we look at specific classical applications of the second and fourth-order theories, respectively.
+In studying this chapter, it will help to keep in mind some specific examples of orthogonal functions and their associated expansion theory. For example, you might use Fourier series or Bessel expansions as your basis for comparison. Sections 14.1, 14.2, and 14.4 are self-contained. Sections 14.1 and 14.2 develop the general subject of Sturm-Liouville theory for boundary value problems associated with second order linear ordinary differential equations. Section 14.4 develops a corresponding theory for certain fourth-order problems. In Sections 14.3 and 14.5 we look at specific classical applications of the second and fourth-order theories, respectively.
 
 ## Looking Ahead...
 
-The applications in this chapter are some of the most beautiful in physics and engineering. They put together different theories and use almost all our knowledge of special series expansions. Even though these applications are all classical, they are presented in a way that invites the use of computers. For example, in the hanging chain problem (Section 14.3), the solution is carried out to a point where it can be fed into a computer to generate pictures that simulate the motion of the hanging chain. The computer can be used in a similar way to illustrate the new expansion results arising in SturmLiouville theory, especially the complicated fourth-order expansions and their related applications to the elastic vibrations of beams (Sections 6.4, 6.5).
+The applications in this chapter are some of the most beautiful in physics and engineering. They put together different theories and use almost all our knowledge of special series expansions. Even though these applications are all classical, they are presented in a way that invites the use of computers. For example, in the hanging chain problem (Section 14.3), the solution is carried out to a point where it can be fed into a computer to generate pictures that simulate the motion of the hanging chain. The computer can be used in a similar way to illustrate the new expansion results arising in Sturm-Liouville theory, especially the complicated fourth-order expansions and their related applications to the elastic vibrations of beams (Sections 14.4, 14.5).
 
 ## 14
 
@@ -21,12 +22,13 @@
 
 ### 14.1 Orthogonal Functions
 
-You may recall from your first course in differential equations how certain notions from linear algebra were crucial in studying solutions of differential equations. For example, to check whether two solutions of a second order linear differential equation yield the general solution, it is enough to show that the determinant of a certain matrix (the Wronskian) is nonzero (see Appendix A.1). These and other notions, such as linear independence and basis, contributed in an essential way to our understanding of solutions of differential equations. Similarly, our development of the theory of Sturm-Liouville in this chapter will require notions from linear algebra that are somewhat abstract but simple to explain in the context of a finite-dimensional vector space. For this reason, we start our discussion by reviewing some basic concepts from linear algebra, specialized to vectors in three dimensions.
+You may recall from your first course in differential equations how certain notions from linear algebra were crucial in studying solutions of differential equations. For example, to check whether two solutions of a second order linear differential equation yield the general solution, it is enough to show that the determinant of a certain matrix (the Wronskian) is nonzero (see Section 10.1). These and other notions, such as linear independence and basis, contributed in an essential way to our understanding of solutions of differential equations. Similarly, our development of the theory of Sturm-Liouville in this chapter will require notions from linear algebra that are somewhat abstract but simple to explain in the context of a finite-dimensional vector space. For this reason, we start our discussion by reviewing some basic concepts from linear algebra, specialized to vectors in three dimensions.
 
 Recall that the inner product of two vectors $\boldsymbol{x}=\left(x_{1}, x_{2}, x_{3}\right)$ and $\boldsymbol{y}=\left(y_{1}, y_{2}, y_{3}\right)$ is the number $\boldsymbol{x} \cdot \boldsymbol{y}=(\boldsymbol{x}, \boldsymbol{y})=x_{1} y_{1}+x_{2} y_{2}+x_{3} y_{3}$. Two nonzero vectors $\boldsymbol{x}$ and $\boldsymbol{y}$ are said to be orthogonal if $\boldsymbol{x} \cdot \boldsymbol{y}=0$. A set of nonzero vectors is said to be orthogonal if any two distinct vectors from this set are orthogonal. A simple example of an orthogonal set consists of the vectors $\boldsymbol{e}_{1}=(1,0,0), \boldsymbol{e}_{2}=(0,1,0)$, and $\boldsymbol{e}_{3}=(0,0,1)$. The inner product is also used to define the norm of a vector $\boldsymbol{v}$ by
 
 $$
 \|\boldsymbol{v}\|=\sqrt{(\boldsymbol{v}, \boldsymbol{v})}=\left(\sum_{j=1}^{3} v_{j}^{2}\right)^{1 / 2} .
+\tag{1}
 $$
 
 Here are two properties of the set $\left\{\boldsymbol{e}_{1}, \boldsymbol{e}_{2}, \boldsymbol{e}_{3}\right\}$ that we wish to investigate for sets of functions:
@@ -36,47 +38,47 @@
 
 $$
 v=\sum_{j=1}^{3}\left(v, e_{j}\right) e_{j}
+\tag{2}
 $$
 
 ## Inner Products and Orthogonality of Functions
 
-In defining the inner product of two vectors, we summed the products of their components. To define the inner product of two functions, we will integrate their product as follows. Let $f$ and $g$ be real-valued functions defined on an interval $(a, b)$ (the interval may be infinite). The inner product of $f$ and $g$, denoted $(f, g)$, is the number
-
-If $f$ and $g$ are complex-valued, then define
-
-$$
-(f, g)=\int_{a}^{b} f(x) \overline{g(x)} d x
-$$
-
-ORTHOGONAL FUNCTIONS
-
-In the definitions of orthogonality and norm, you should use the appropriate definition of ( $f, g$ ) for complex-valued functions.
-
-$$
-(f, g)=\int_{a}^{b} f(x) g(x) d x
-$$
-
-This terminology is the same as for the inner product of vectors because the function ( $\cdot, \cdot$ ) defined in (3) satisfies the same properties as the inner product of vectors (see Exercise 21). We will assume that the functions are real-valued and nice enough that all integrals of the form (3) exist. This is for example the case, if the functions are piecewise continuous.
-
-$$
-\begin{aligned}
-& \text { The functions } f \text { and } g \text { are called orthogonal on the interval }(a, b) \text { if } \\
-& \qquad(f, g)=\int_{a}^{b} f(x) g(x) d x=0
-\end{aligned}
-$$
-
-We define the norm of $f$, denoted $\|f\|$, by
-
-$$
-\|f\|=\sqrt{(f, f)}=\left(\int_{a}^{b}|f(x)|^{2} d x\right)^{1 / 2}
-$$
-
-If $\|f\|<\infty$, we also say that $f$ is square integrable on $(a, b)$. If $f$ is real-valued, then $|f(x)|^{2}$ is simply $f^{2}(x)$. But if $f$ is complex-valued, then $|f(x)|^{2}=f(x) \overline{f(x)}$. Note how both definitions, orthogonality and norm, are based on the notion of inner products as they were in the finite-dimensional case. (Compare with (2).) A set of functions $\left\{f_{1}, f_{2}, f_{3}, \ldots\right\}$ defined on the interval ( $a, b$ ) is called an orthogonal set if $\left\|f_{n}\right\| \neq 0$ for all $n$, and each distinct pair of functions from the set is orthogonal, that is, $\left(f_{n}, f_{m}\right)=$ 0 for $n \neq m$. If, in addition, the norm of each $f_{n}$ is 1 , the set is called an orthonormal set. Hence, if we divide each function in an orthogonal set by its norm we obtain an orthonormal set.
-
-## EXAMPLE 1 Orthogonal functions
-
-Show that the set of functions $f_{n}(x)=\sin n x(n=1,2, \ldots)$ is orthogonal on the interval $[-\pi, \pi]$ and obtain the corresponding orthonormal set.
-Solution We need to show that $\|\sin n x\| \neq 0$ and each distinct pair of functions in the given set is orthogonal. We have
+In defining the inner product of two vectors, we summed the products of their components. To define the inner product of two functions, we will integrate their product as follows.
+
+> [!definition] Inner Product and Norm of Square-Integrable Functions
+> Let $f$ and $g$ be real-valued, square integrable functions defined on an interval $(a,b)$ (the interval may be infinite). The inner product of $f$ and $g$, denoted $(f,g)$, is the number
+> $$
+> (f,g)=\int_a^b f(x)g(x)\,dx.
+> $$
+> If $f$ and $g$ are complex-valued, then define
+> $$
+> (f,g)=\int_a^b f(x)\overline{g(x)}\,dx.
+> $$
+> We define the norm of $f$, denoted $\|f\|$, by
+> $$
+> \|f\|=\sqrt{(f,f)}=\left(\int_a^b|f(x)|^2\,dx\right)^{1/2}.
+> $$
+> If $\|f\|<\infty$, we also say that $f$ is square integrable on $(a,b)$.
+
+*Printed equation label: (3) inner product (the printed formula is for real-valued functions).*
+
+This terminology is the same as for the inner product of vectors because the function ( $\cdot, \cdot$ ) defined in (3) satisfies the same properties as the inner product of vectors (see Exercise 21). We will assume that the functions are real-valued and nice enough that all integrals of the form (3) exist. This is for example the case on a finite interval if the functions are piecewise continuous and bounded.
+
+If $f$ is real-valued, then $|f(x)|^2$ is simply $f^2(x)$. But if $f$ is complex-valued, then $|f(x)|^2=f(x)\overline{f(x)}$. Note how both definitions, orthogonality and norm, are based on the notion of inner products as they were in the finite-dimensional case. (Compare with (2).)
+
+> [!definition] Orthogonal Functions
+> The functions $f$ and $g$ are called orthogonal on the interval $(a,b)$ if $(f,g)=0$.
+>
+> A set of functions $\left\{f_{1}, f_{2}, f_{3}, \ldots\right\}$ defined on the interval ( $a, b$ ) is called an orthogonal set if $\left\|f_{n}\right\| \neq 0$ for all $n$, and each distinct pair of functions from the set is orthogonal, that is, $\left(f_{n}, f_{m}\right)=$ 0 for $n \neq m$. If, in addition, the norm of each $f_{n}$ is 1 , the set is called an orthonormal set. Hence, if we divide each function in an orthogonal set by its norm we obtain an orthonormal set.
+>
+> Here $(f,g)=\int_a^b f(x)\overline{g(x)}\,dx$ and $\|f\|^2=(f,f)$.
+
+> [!exercise] EXAMPLE 1 Orthogonal functions
+> Show that the set of functions $f_{n}(x)=\sin n x(n=1,2, \ldots)$ is orthogonal on the interval $[-\pi, \pi]$ and obtain the corresponding orthonormal set.
+
+##### solution
+
+We need to show that $\|\sin n x\| \neq 0$ and each distinct pair of functions in the given set is orthogonal. We have
 
 $$
 \|\sin n x\|^{2}=\int_{-\pi}^{\pi} \sin ^{2} n x d x=\int_{-\pi}^{\pi} \frac{1-\cos 2 n x}{2} d x=\pi
@@ -96,7 +98,10 @@
 
 The next example deals with the trigonometric system from Fourier series. Note that this set has the set from Example 1 as a subset.
 
-## EXAMPLE 2 The trigonometric system
+> [!exercise] EXAMPLE 2 The trigonometric system
+> Obtain the orthonormal system associated with $1,\sin x,\cos x,\sin 2x,\cos 2x,\ldots$ on $[-\pi,\pi]$.
+
+##### solution
 
 The set of functions
 
@@ -104,15 +109,18 @@
 1, \sin x, \cos x, \sin 2 x, \cos 2 x, \sin 3 x, \cos 3 x, \ldots
 $$
 
-is orthogonal on the interval $[-\pi, \pi]$ (see Section 2.1). To obtain the corresponding orthonormal set, we compute $\|\cos n x\|=\|\sin n x\|=\sqrt{\pi} \neq 0$, for $n=1,2, \ldots$. Also, the norm of the function identically 1 over the interval $[-\pi, \pi]$ is equal to $\sqrt{2 \pi}$. Thus the orthonormal set is
+is orthogonal on the interval $[-\pi, \pi]$ (see Section 7.1). To obtain the corresponding orthonormal set, we compute $\|\cos n x\|=\|\sin n x\|=\sqrt{\pi} \neq 0$, for $n=1,2, \ldots$. Also, the norm of the function identically 1 over the interval $[-\pi, \pi]$ is equal to $\sqrt{2 \pi}$. Thus the orthonormal set is
 
 $$
 \frac{1}{\sqrt{2 \pi}}, \frac{\sin x}{\sqrt{\pi}}, \frac{\cos x}{\sqrt{\pi}}, \frac{\sin 2 x}{\sqrt{\pi}}, \frac{\cos 2 x}{\sqrt{\pi}}, \frac{\sin 3 x}{\sqrt{\pi}}, \frac{\cos 3 x}{\sqrt{\pi}}, \ldots
 $$
 
-## EXAMPLE 3 Legendre polynomials
-
-It was shown in Section 5.6 that the Legendre polynomials satisfy
+> [!exercise] EXAMPLE 3 Legendre polynomials
+> Use the norm and orthogonality formulas for Legendre polynomials to verify that $\{P_n\}_{n\ge0}$ is an orthogonal system on $[-1,1]$.
+
+##### solution
+
+It was shown in Section 13.6 that the Legendre polynomials satisfy
 
 $$
 \int_{-1}^{1} P_{n}^{2}(x) d x=\frac{2}{2 n+1} \quad \text { and } \quad \int_{-1}^{1} P_{m}(x) P_{n}(x) d x=0 \quad \text { for } m \neq n
@@ -128,13 +136,14 @@
 
 $$
 f(x)=\sum_{j=1}^{\infty} a_{j} f_{j}(x)
+\tag{4}
 $$
 
 where the $a_{j}$ 's are real or complex numbers?
 2. If the representation (4) is possible, how do we find the coefficients $a_{j}$ ?
 
 A complete treatment of these questions requires machinery that is beyond the scope of this text. Without going far into the theory of orthogonal functions, we will try to motivate the answers to these fundamental questions
-through examples. Starting with the second question, and taking a hint from (1), our guess is that the coefficients in (4) should be given in terms of the inner products of $f$ with $f_{1}, f_{2}, f_{3}, \ldots$. To see this, we proceed as we have done before with Fourier series. We multiply both sides of (4) by $f_{k}$ and integrate term by term on the interval $(a, b)$. This gives
+through examples. Starting with the second question, and taking a hint from (1), our guess is that the coefficients in (4) should be given in terms of the inner products of $f$ with $f_{1}, f_{2}, f_{3}, \ldots$. To see this, we proceed as we have done before with Fourier series. For real-valued functions, we multiply the expansion by $f_k$ and integrate term by term (justified by $L^2$ convergence) on the interval $(a, b)$. This gives
 
 $$
 \int_{a}^{b} f(x) f_{k}(x) d x=\sum_{j=1}^{\infty} a_{j} \int_{a}^{b} f_{j}(x) f_{k}(x) d x
@@ -150,124 +159,213 @@
 
 $$
 a_{k}=\frac{\left(f, f_{k}\right)}{\left\|f_{k}\right\|^{2}}=\frac{1}{\left\|f_{k}\right\|^{2}} \int_{a}^{b} f(x) f_{k}(x) d x
+\tag{5}
 $$
 
 This motivates the following answer to the second question.
 
-THEOREM 1 GENERALIZED FOURIER SERIES
-
-If $f_{1}, f_{2}, f_{3}, \ldots$ is a set of orthogonal functions on $(a, b)$ and if $f$ can be represented as a series in the form (4), then
-
-$$
-f(x)=\sum_{j=1}^{\infty} \frac{\left(f, f_{j}\right)}{\left\|f_{j}\right\|^{2}} f_{j}(x)
-$$
-
-The series (6) is called a generalized Fourier series. Examples of such series include Fourier, Legendre, and Bessel series of the previous chapters.
-
-We now turn to the first question. Again, we take a hint from the three-dimensional real vector space. For the classes of functions that we will consider in this book, a set of orthogonal functions $f_{1}, f_{2}, f_{3}, \ldots$ in $A$ generates $A$ if and only if the the orthogonal functions $f_{1} ; f_{2}, f_{3}, \ldots$ form a complete set of function in the following sense: If $f$ is orthogonal to every $f_{j}, j=1,2,3, \ldots$, then $f$ must be identically 0 .
-
-In the case of Fourier series on the interval $[-\pi, \pi]$, the functions $1, \cos x$, $\cos 2 x, \cos 3 x, \ldots, \cos n x, \ldots, \sin x, \sin 2 x, \sin 3 x, \ldots, \sin n x, \ldots$ form an orthogonal set of functions on $[-\pi, \pi]$. By the Fourier series representation theorem, this set also generates the class $A$ of $2 \pi$-periodic, piecewise smooth functions. What does completeness mean in this case? It means that if all the Fourier coefficients of a function $f$ are zero, then $f$ must be identically zero. This fact follows from the Fourier series representation theorem, since
-
-ORTHOGONALITY WITH RESPECT TO A WEIGHT
-if we set all the coefficients of $f$ equal to 0 , then the Fourier series of $f$ is identically 0 . But the Fourier series converges to $f$, and so $f$ must be zero.
+> [!theorem] Generalized Fourier Series
+> If $f_{1}, f_{2}, f_{3}, \ldots$ is a set of orthogonal functions on $(a, b)$ and if $f$ can be represented as a series $f=\sum_{j=1}^\infty a_jf_j$ convergent in mean square, then
+>
+> $$
+> f(x)=\sum_{j=1}^{\infty} \frac{\left(f, f_{j}\right)}{\left\|f_{j}\right\|^{2}} f_{j}(x)
+> $$
+>
+> Here $(f,g)=\int_a^b f(x)\overline{g(x)}\,dx$ and $\|f\|^2=(f,f)$.
+
+*Printed equation label: (6) orthogonal expansion.*
+
+This expansion is called a generalized Fourier series. Examples of such series include Fourier, Legendre, and Bessel series of the previous chapters.
+
+We now turn to the first question. Again, we take a hint from the three-dimensional real vector space.
+
+> [!definition] Completeness of an Orthogonal System in a Hilbert Space
+> A set of orthogonal square integrable functions $f_1,f_2,f_3,\ldots$ forms a complete set in the following sense: If $f$ is orthogonal to every $f_j$, $j=1,2,3,\ldots$, then $f$ must be zero almost everywhere.
+>
+> Here $(f,g)=\int_a^b f(x)\overline{g(x)}\,dx$ and $\|f\|^2=(f,f)$.
+
+In the case of Fourier series on the interval $[-\pi, \pi]$, the functions $1, \cos x$, $\cos 2 x, \cos 3 x, \ldots, \cos n x, \ldots, \sin x, \sin 2 x, \sin 3 x, \ldots, \sin n x, \ldots$ form an orthogonal set of functions on $[-\pi, \pi]$. By the Fourier series representation theorem, this set also generates the class $A$ of $2 \pi$-periodic, piecewise smooth functions. What does completeness mean in this case? It means that if all the Fourier coefficients of a function $f$ are zero, then $f$ must be zero at every point of continuity. This fact follows from the Fourier series representation theorem, since
+
+if we set all the coefficients of $f$ equal to 0 , then the Fourier series of $f$ is identically 0 . But the Fourier series converges to $f$ at points of continuity, and so $f$ must be zero there.
 
 To establish the completeness of a set of functions is difficult in general. The good news is that most orthogonal sets of functions that we will encounter arise from solutions of ordinary differential equations that fit the so-called Sturm-Liouville theory form. The completeness property of these sets of functions is a consequence of general results from the Sturm-Liouville theory. (See Theorem 3, Section 14.2.)
 
 ## Orthogonality with Respect to a Weight
 
-What we have presented thus far can be extended to functions that are orthogonal with respect to a weight function. We have encountered such situations in the study of Bessel series. In general, if $f$ and $g$ are real-valued functions on $(a, b)$, we define their inner product with respect to the weight $\boldsymbol{w}$ to be the number
-
-$$
-(f, g)=\int_{a}^{b} f(x) g(x) w(x) d x
-$$
-
-We assume that $w(x)$ is a nonnegative piecewise continuous function on $[a, b]$ that is not identically 0 on any subinterval of $[a, b]$. The corresponding definition of orthogonality is as follows.
-
-The functions $f$ and $g$ are orthogonal with respect to the weight function $w$ on the interval $[a, b]$ if
-
-$$
-\int_{a}^{b} f(x) g(x) w(x) d x=0
-$$
-
-The norm of $f$ with respect to the weight function $w$ is
-
-$$
-\|f\|=\left(\int_{a}^{b}|f(x)|^{2} w(x) d x\right)^{1 / 2}
-$$
-
-## EXAMPLE 4 Orthogonality with respect to a weight
+What we have presented thus far can be extended to functions that are orthogonal with respect to a weight function. We have encountered such situations in the study of Bessel series.
+
+> [!definition] Orthogonality with Respect to a Weight
+> In general, if $f$ and $g$ are real-valued square integrable functions with respect to $w$ on $(a, b)$, we define their inner product with respect to the weight $\boldsymbol{w}$ to be the number
+>
+> $$
+> (f, g)=\int_{a}^{b} f(x) g(x) w(x) d x
+> $$
+>
+> We assume that $w(x)$ is a nonnegative piecewise continuous function on $[a, b]$ that is not identically 0 on any subinterval of $[a, b]$. The corresponding definition of orthogonality is as follows.
+>
+> The functions $f$ and $g$ are orthogonal with respect to the weight function $w$ on the interval $[a, b]$ if
+>
+> $$
+> \int_{a}^{b} f(x) g(x) w(x) d x=0
+> $$
+>
+> The norm of $f$ with respect to the weight function $w$ is
+>
+> $$
+> \|f\|=\left(\int_{a}^{b}|f(x)|^{2} w(x) d x\right)^{1 / 2}
+> $$
+
+*Printed equation label: (7).*
+
+> [!exercise] EXAMPLE 4 Orthogonality with respect to a weight
+> Identify the weights and verify orthogonality for these systems:
+>
+> (a) $\cos(nx)$, $n\ge1$, on $(-\pi,\pi)$.
+>
+> (b) $J_0(\alpha_nx)$, $n\ge1$, on $(0,1)$, where $\alpha_n$ are the positive zeros of $J_0$.
+
+##### solution
 
 (a) The functions $f_{n}(x)=\cos n x(n=1,2, \ldots)$ satisfy $\int_{-\pi}^{\pi} f_{m}(x) f_{n}(x) d x=0$ for $m \neq n$. So these functions form an orthogonal set with weight function $w(x)=1$ on the interval $(-\pi, \pi)$.
-(b) Let $\alpha_{1}, \alpha_{2}, \alpha_{3}, \ldots$ denote the positive zeros of the Bessel function $J_{0}$. From Theorem 1, Section 4.8, we have $\int_{0}^{1} J_{0}\left(\alpha_{m} x\right) J_{0}\left(\alpha_{n} x\right) x d x=0$ for $m \neq n$. Thus the functions $J_{0}\left(\alpha_{n} x\right), n=1,2, \ldots$ form an orthogonal set with respect to the weight function $w(x)=x$ on the interval $(0,1)$.
+(b) Let $\alpha_{1}, \alpha_{2}, \alpha_{3}, \ldots$ denote the positive zeros of the Bessel function $J_{0}$. From Theorem 1, Section 12.8, we have $\int_{0}^{1} J_{0}\left(\alpha_{m} x\right) J_{0}\left(\alpha_{n} x\right) x d x=0$ for $m \neq n$. Thus the functions $J_{0}\left(\alpha_{n} x\right), n=1,2, \ldots$ form an orthogonal set with respect to the weight function $w(x)=x$ on the interval $(0,1)$.
 
 The following is the analog of Theorem 1 for expansions in series with respect to functions that are orthogonal with respect to a weight.
 
-THEOREM 2 GENERALIZED FOURIER SERIES
-
-Although (8) looks identical to (6), you should keep in mind that computing the inner products and norms in (8) involves a weight function.
-
-If $f_{1}, f_{2}, f_{3}, \ldots$ is a set of orthogonal functions with respect to the weight $w$ on $[a, b]$ and if $f$ can be represented as a series in the form (4), then
-
-$$
-f(x)=\sum_{j=1}^{\infty} \frac{\left(f, f_{j}\right)}{\left\|f_{j}\right\|^{2}} f_{j}(x)
-$$
-
-In Example 4(b) we observed that the functions $J_{0}\left(\alpha_{n} x\right)$ are orthogonal with weight $w(x)=x$ on the interval $(0,1)$. In Example 1 of Section 4.8 we derived the series expansion of the function $f(x)=1$ in terms of this orthogonal series. You should check that the series obtained there is the same as that in (8).
+> [!theorem] Generalized Fourier Series
+> If $f_{1}, f_{2}, f_{3}, \ldots$ is a set of orthogonal functions with respect to the weight $w$ on $[a, b]$ and if $f$ can be represented as a series $f=\sum_{j=1}^\infty a_jf_j$ convergent in weighted mean square, then
+>
+> $$
+> f(x)=\sum_{j=1}^{\infty} \frac{\left(f, f_{j}\right)}{\left\|f_{j}\right\|^{2}} f_{j}(x)
+> $$
+>
+> Here $(f,g)=\int_a^b f(x)\overline{g(x)}w(x)\,dx$ and $\|f\|^2=(f,f)$, with a nonnegative piecewise continuous weight $w$ that is not identically zero on any subinterval.
+
+*Printed equation label: (8) weighted orthogonal expansion.*
+
+In Example 4(b) we observed that the functions $J_{0}\left(\alpha_{n} x\right)$ are orthogonal with weight $w(x)=x$ on the interval $(0,1)$. In Example 1 of Section 12.8 we derived the series expansion of the function $f(x)=1$ in terms of this orthogonal series. You should check that the series obtained there is the same as that in (8).
 
 We end this section with a statement of Parseval's identity for complete orthogonal systems.
 
-THEOREM 3 PARSEVAL'S IDENTITY
-
-Let $f_{1}, f_{2}, f_{3}, \ldots$ be a complete set of orthogonal functions with respect to the weight $w$ on $[a, b]$ and let $f$ be such that its norm as given by (7) is finite. (That is, $f$ is square integrable with respect to the weight $w$.) Then
-
-$$
-\int_{a}^{b}|f(x)|^{2} w(x) d x=\sum_{j=1}^{\infty} \frac{\left|\left(f, f_{j}\right)\right|^{2}}{\left\|f_{j}\right\|^{2}}
-$$
-
-As we have seen in Section 2.5 with Fourier series, Parseval's identity has many important applications. We can motivate it as follows. Since the functions $f_{1}, f_{2}, f_{3}, \ldots$ form a complete orthogonal set of functions with respect to the weight $w$ on $[a, b]$, the function $f$ can be represented in a generalized series as in (8). If $f$ is real-valued, multiply both sides of (8) by $f(x) w(x)$, and integrate over the interval $[a, b]$. Assuming that we can integrate the series term by term and using the definition of the inner product with respect to the weight $w$, we get (9). If $f$ is complex-valued, we multiply both sides of (8) by $\overline{f(x)} w(x)$ and repeat the same proof.
-
-## Exercises 6.1
-
-In Exercises 1-8, show that the given set of functions is orthogonal with respect to the given weight on the prescribed interval.
-
-1. $1, \sin \pi x, \cos \pi x, \sin 2 \pi x, \cos 2 \pi x, \sin 3 \pi x, \cos 3 \pi x, \ldots ; w(x)=1$ on $[0,2]$.
-2. $f(x)$ is an even function, $g(x)$ is an odd function; $w(x)=1$ on any symmetric interval about 0 .
-3. $1, x,-1+2 x^{2} ; w(x)=\frac{1}{\sqrt{1-x^{2}}}$ on $[-1,1]$. (These are examples of Chebyshev polynomials of the first kind. See Exercises 6.2 for further details.)
-4. $-3 x+4 x^{3}, 1-8 x^{2}+8 x^{4} ; w(x)=\frac{1}{\sqrt{1-x^{2}}}$ on $[-1,1]$.
-5. $1,2 x,-1+4 x^{2} ; w(x)=\sqrt{1-x^{2}}$ on $[-1,1]$. (These are examples of Chebyshev polynomials of the second kind.)
-6. $1,1-x,\left(2-4 x+x^{2}\right) / 2 ; w(x)=e^{-x}$ on $[0, \infty)$. (These are examples of Laguerre polynomials.)
-7. $1,2 x,-2+4 x^{2} ; w(x)=e^{-x^{2}}$ on $(-\infty, \infty)$. (These are examples of Hermite polynomials. [Hint: Exercise 33 (a), Section 4.7.]
-8. $\left(2-4 x+x^{2}\right) / 2,-12 x+8 x^{3} ; w(x)=e^{-x}$ on $[0, \infty)$.
-9. Determine the constants $a$ and $b$ so that the functions $1, x$, and $a+b x+x^{2}$ become orthogonal on the interval $[-1,1]$.
-10. If the functions $f(x)$ and $g(x)$ are orthogonal with respect to a weight $w(x)$ on $[0, L]$, what can be said about the functions $f(a x)$ and $g(a x)$ where $a>0$ ?
-11. Compute the norms of the functions in Exercise 1.
-12. Compute the norms of the functions in Exercise 5.
-13. What is the orthonormal set corresponding to the Legendre polynomials on the interval $[-1,1]$ ?
-14. Show that if $f$ and $g$ are continuous functions on $[a, b]$ that are orthogonal with respect to the weight function 1 , then either $f$ or $g$ must vanish somewhere in $(a, b)$.
-15. Show that if $f_{1}(x), f_{2}(x), \ldots$ are orthogonal on $[0,1]$ with respect to the weight $x$, then $f_{1}(\sqrt{x}), f_{2}(\sqrt{x}), \ldots$ are orthogonal on $[0,1]$ with respect to the weight function 1.
-16. Parseval's identity for Fourier series. Specialize (9) to the trigonometric system (of period $2 p$ ) to obtain (6) of Section 2.5.
-17. Parseval's identity for Legendre series. Use (9) to derive the identity
-
-$$
-\int_{-1}^{1} f(x)^{2} d x=\sum_{n=0}^{\infty} \frac{2 A_{n}^{2}}{2 n+1}
-$$
-
-where $A_{n}$ is the $n$th Legendre coefficient of $f$. (See Section 5.6.)
-18. Parseval's identity for Bessel series. Use (9) to derive the identity
-
-$$
-\int_{0}^{R} f(x)^{2} x d x=\sum_{j=1}^{\infty} \frac{R^{2} J_{p+1}^{2}\left(\alpha_{p j}\right)}{2} A_{j}^{2}
-$$
-
-where $A_{j}$ is the $j$ th coefficient of the Bessel series expansion of $f$ of order $p$, and $\alpha_{p j}$ is the $j$ th positive zero of $J_{p}$. (See Section 4.8.)
-19. Sums of reciprocals of squares of zeros of Bessel functions. Derive the following interesting formula: $\frac{1}{4(p+1)}=\sum_{j=1}^{\infty} \frac{1}{\alpha_{p j}^{2}}$. [Hint: Apply Exercise 18 with $R=1$ to the Bessel series expansion found in Exercise 20, Section 4.8.]
-20. By specializing Exercise 19 to the case $p=\frac{1}{2}$, derive the identity
-
-$$
-\frac{\pi^{2}}{6}=\sum_{j=1}^{\infty} \frac{1}{j^{2}}
-$$
-
-21. Show that the inner product satisfies the following properties:
-(a) $(a f, g)=a(f, g)$ for any number $a$,
-(b) $(f+g, h)=(f, h)+(g, h)$,
-(c) $(f, f) \geq 0$ for any function $f$.
+> [!theorem] Parseval's Identity
+> Let $f_{1}, f_{2}, f_{3}, \ldots$ be a complete set of orthogonal functions with respect to the weight $w$ on $[a, b]$ and let $f$ be such that its norm with respect to $w$ is finite. (That is, $f$ is square integrable with respect to the weight $w$.) Then
+>
+> $$
+> \int_{a}^{b}|f(x)|^{2} w(x) d x=\sum_{j=1}^{\infty} \frac{\left|\left(f, f_{j}\right)\right|^{2}}{\left\|f_{j}\right\|^{2}}
+> $$
+>
+> Here $(f,g)=\int_a^b f(x)\overline{g(x)}w(x)\,dx$ and $\|f\|^2=(f,f)$, with a nonnegative piecewise continuous weight $w$ that is not identically zero on any subinterval.
+
+*Printed equation label: (9).*
+
+As we have seen in Section 7.5 with Fourier series, Parseval's identity has many important applications. We can motivate it as follows. Since the functions $f_{1}, f_{2}, f_{3}, \ldots$ form a complete orthogonal set of functions with respect to the weight $w$ on $[a, b]$, the function $f$ can be represented in a generalized series as in (8). If $f$ is real-valued, multiply both sides of (8) by $f(x) w(x)$, and integrate over the interval $[a, b]$. Assuming that we can integrate the series term by term and using the definition of the inner product with respect to the weight $w$, we get (9). If $f$ is complex-valued, we multiply both sides of (8) by $\overline{f(x)} w(x)$ and repeat the same proof.
+
+## Exercises 14.1
+
+
+> [!prompt] Shared exercise instructions
+> In Exercises 1–7, show that the given set of functions is orthogonal with respect to the given weight on the prescribed interval.
+
+
+> [!exercise] Exercise 1
+> $1, \sin \pi x, \cos \pi x, \sin 2 \pi x, \cos 2 \pi x, \sin 3 \pi x, \cos 3 \pi x, \ldots ; w(x)=1$ on $[0,2]$.
+
+
+> [!exercise] Exercise 2
+> $f(x)$ is an even function, $g(x)$ is an odd function; $w(x)=1$ on any symmetric interval about 0 .
+
+
+> [!exercise] Exercise 3
+> $1, x,-1+2 x^{2} ; w(x)=\frac{1}{\sqrt{1-x^{2}}}$ on $[-1,1]$. (These are examples of Chebyshev polynomials of the first kind. See Exercises 14.2 for further details.)
+
+
+> [!exercise] Exercise 4
+> $-3 x+4 x^{3}, 1-8 x^{2}+8 x^{4} ; w(x)=\frac{1}{\sqrt{1-x^{2}}}$ on $[-1,1]$.
+
+
+> [!exercise] Exercise 5
+> $1,2 x,-1+4 x^{2} ; w(x)=\sqrt{1-x^{2}}$ on $[-1,1]$. (These are examples of Chebyshev polynomials of the second kind.)
+
+
+> [!exercise] Exercise 6
+> $1,1-x,\left(2-4 x+x^{2}\right) / 2 ; w(x)=e^{-x}$ on $[0, \infty)$. (These are examples of Laguerre polynomials.)
+
+
+> [!exercise] Exercise 7
+> $1,2 x,-2+4 x^{2} ; w(x)=e^{-x^{2}}$ on $(-\infty, \infty)$. (These are examples of Hermite polynomials. [Hint: Exercise 33 (a), Section 12.7.])
+
+
+> [!exercise] Exercise 8
+> Check whether the following pair is orthogonal: $\left(2-4 x+x^{2}\right) / 2,-12 x+8 x^{3} ; w(x)=e^{-x}$ on $[0, \infty)$.
+
+
+
+
+> [!exercise] Exercise 9
+> Determine the constants $a$ and $b$ so that the functions $1, x$, and $a+b x+x^{2}$ become orthogonal on the interval $[-1,1]$.
+
+
+> [!exercise] Exercise 10
+> If the functions $f(x)$ and $g(x)$ are orthogonal with respect to a weight $w(x)$ on $[0, L]$, what can be said about the functions $f(a x)$ and $g(a x)$ where $a>0$ ?
+
+
+> [!exercise] Exercise 11
+> Compute the norms of the functions in Exercise 1.
+
+
+> [!exercise] Exercise 12
+> Compute the norms of the functions in Exercise 5.
+
+
+> [!exercise] Exercise 13
+> What is the orthonormal set corresponding to the Legendre polynomials on the interval $[-1,1]$ ?
+
+
+> [!exercise] Exercise 14
+> Show that if $f$ and $g$ are real-valued continuous functions on $[a, b]$ that are orthogonal with respect to the weight function 1 , then either $f$ or $g$ must vanish somewhere in $(a, b)$.
+
+
+> [!exercise] Exercise 15
+> Show that if $f_{1}(x), f_{2}(x), \ldots$ are orthogonal on $[0,1]$ with respect to the weight $x$, then $f_{1}(\sqrt{x}), f_{2}(\sqrt{x}), \ldots$ are orthogonal on $[0,1]$ with respect to the weight function 1.
+
+
+> [!exercise] Exercise 16
+> Parseval's identity for Fourier series. Specialize (9) to the trigonometric system (of period $2 p$ ) to obtain (6) of Section 7.5.
+
+
+> [!exercise] Exercise 17
+> Parseval's identity for Legendre series. For a real function $f\in L^2(-1,1)$, use Parseval's identity to derive the identity
+>
+> $$
+> \int_{-1}^{1} f(x)^{2} d x=\sum_{n=0}^{\infty} \frac{2 A_{n}^{2}}{2 n+1}
+> $$
+>
+> where $A_{n}$ is the $n$th Legendre coefficient of $f$. (See Section 13.6.)
+
+
+> [!exercise] Exercise 18
+> Parseval's identity for Bessel series. For $R>0$, $p\ge0$, and real $f\in L^2((0,R),x\,dx)$, use Parseval's identity to derive the identity
+>
+> $$
+> \int_{0}^{R} f(x)^{2} x d x=\sum_{j=1}^{\infty} \frac{R^{2} J_{p+1}^{2}\left(\alpha_{p j}\right)}{2} A_{j}^{2}
+> $$
+>
+> where $A_{j}$ is the $j$ th coefficient of the Bessel series expansion of $f$ of order $p$, and $\alpha_{p j}$ is the $j$ th positive zero of $J_{p}$. (See Section 12.8.)
+
+
+> [!exercise] Exercise 19
+> Sums of reciprocals of squares of zeros of Bessel functions. For $p\ge0$, derive the following formula: $\frac{1}{4(p+1)}=\sum_{j=1}^{\infty} \frac{1}{\alpha_{p j}^{2}}$. [Hint: Apply Exercise 18 with $R=1$ to the Bessel series expansion found in Exercise 20, Section 12.8.]
+
+
+> [!exercise] Exercise 20
+> By specializing Exercise 19 to the case $p=\frac{1}{2}$, derive the identity
+>
+> $$
+> \frac{\pi^{2}}{6}=\sum_{j=1}^{\infty} \frac{1}{j^{2}}
+> $$
+
+
+> [!exercise] Exercise 21
+> Show that the inner product satisfies the following properties:
+> (a) $(a f, g)=a(f, g)$ for any number $a$,
+> (b) $(f+g, h)=(f, h)+(g, h)$,
+> (c) $(f, f) \geq 0$ for any function $f$.

`````
