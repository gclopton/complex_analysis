
# Editorial records

Reading note: 10.4 The Power Series Method, Part I.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!exercise|1639fcc1-f740-5efa-975f-564c3c82c478.local at=5dadc83e-6e7a-592d-9755-be3144675a5a] Exercise 43
> Uniform convergence of power series. Suppose that $\sum_{m=0}^{\infty}a_mx^m$ has radius of convergence $R>0$. Fix $0<r<R$ and choose $\rho$ with $r<\rho<R$.
> (a) Show that $a_m\rho^m\to0$, and hence $|a_m|\rho^m\leq M$ for some $M>0$ and all $m$.
> (b) For $|x|\leq r$, establish $|a_mx^m|\leq M(r/\rho)^m$. Use the Weierstrass $M$-test to conclude uniform convergence on $[-r,r]$.
````
### After

````text
> [!exercise|1639fcc1-f740-5efa-975f-564c3c82c478.local at=5dadc83e-6e7a-592d-9755-be3144675a5a] Exercise 43
> Uniform convergence of power series. Suppose that $\sum_{m=0}^{\infty} a_{m} x^{m}$ has radius of convergence $R>0$. Let $r$ be any real number such that $0<r<R$, and choose $\rho$ with $r<\rho<R$.
> (a) Show that $a_m\rho^m \rightarrow 0$. Conclude that $\left|a_m\rho^m\right| \leq M$ for some $M>0$ and all $m$.
> [Hint: Apply the $n$th term test to a convergent series.]
> (b) For $x$ such that $|x| \leq r$, we have
>
> $$
> \left|a_{m} x^{m}\right|=\left|a_m\right|\rho^m(|x|/\rho)^m \leq M(r/\rho)^m .
> $$
>
> Use these inequalities, the fact that $r/\rho<1$, and the Weierstrass $M$-test to conclude that $\sum_{m=0}^{\infty} a_{m} x^{m}$ converges uniformly on $[-r, r]$.
````

## 2. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!property|55d973e6-e5a8-5f66-9ddd-46efc46e43f7.local at=ff821645-d23f-5da1-a423-585c58853692] Uniqueness of Coefficients in a Convergent Power Series
> Suppose $f(x)=\sum_{m=0}^{\infty} a_{m}(x-a)^{m}$ and $g(x)= \sum_{m=0}^{\infty} b_{m}(x-a)^{m}$, where both series have positive radii of convergence. If $f(x)=g(x)$ for all $x$ in an open interval containing $a$, then $a_{m}=b_{m}$ for all $m$. In other words, a power series representation is unique.
````
### After

````text
> [!property|55d973e6-e5a8-5f66-9ddd-46efc46e43f7.local at=ff821645-d23f-5da1-a423-585c58853692] The Identity Principle
> Suppose $f(x)=\sum_{m=0}^{\infty} a_{m}(x-a)^{m}$ and $g(x)= \sum_{m=0}^{\infty} b_{m}(x-a)^{m}$, where both series have positive radii of convergence. If $f(x)=g(x)$ for all $x$ in an open interval containing $a$, then $a_{m}=b_{m}$ for all $m$. In other words, a power series representation is unique.
````

## 3. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!property|1604b309-c377-522d-bce7-1a378a2a99fe.local at=ddf5b4d0-7c15-57e4-b5ef-414bfc5932db] Quotients of Real Analytic Functions with Nonzero Denominator
> Suppose that $f$ and $g$ are analytic at $a$ and $g(a) \neq 0$. Then the quotient $f / g$ is also analytic at $a$.
````
### After

````text
> [!property|1604b309-c377-522d-bce7-1a378a2a99fe.local at=ddf5b4d0-7c15-57e4-b5ef-414bfc5932db] Quotients of Analytic Functions
> Suppose that $f$ and $g$ are analytic at $a$ and $g(a) \neq 0$. Then the quotient $f / g$ is also analytic at $a$.
````

## 4. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!property|f3a33803-a80f-5388-85fa-9b47a1cf80aa.local at=ec80d941-813c-53a4-a67e-cb433b51a3c6] Linear Combinations of Power Series with a Common Center
> Consider the power series representations
>
> $$
> f(x)=\sum_{m=0}^{\infty} a_{m}(x-a)^{m} \quad \text { and } \quad g(x)=\sum_{m=0}^{\infty} b_{m}(x-a)^{m},
> $$
>
> with common center at $a$ and radii of convergence $R_{1}>0$ and $R_{2}>0$, respectively. Then it is not difficult to show that for any real numbers $\alpha$ and $\beta$, we have
>
> $$
> \alpha f(x)+\beta g(x)=\sum_{m=0}^{\infty}\left(\alpha a_{m}+\beta b_{m}\right)(x-a)^{m}
> $$
>
>
>
> The equality holds for $|x-a|<\min(R_1,R_2)$.
````
### After

````text
> [!property|f3a33803-a80f-5388-85fa-9b47a1cf80aa.local at=ec80d941-813c-53a4-a67e-cb433b51a3c6] Linear Combinations and Products
> Consider the power series representations
>
> $$
> f(x)=\sum_{m=0}^{\infty} a_{m}(x-a)^{m} \quad \text { and } \quad g(x)=\sum_{m=0}^{\infty} b_{m}(x-a)^{m},
> $$
>
> with common center at $a$ and radii of convergence $R_{1}>0$ and $R_{2}>0$, respectively. Then it is not difficult to show that for any real numbers $\alpha$ and $\beta$, we have
>
> $$
> \alpha f(x)+\beta g(x)=\sum_{m=0}^{\infty}\left(\alpha a_{m}+\beta b_{m}\right)(x-a)^{m}
> $$
>
> The equality holds for $|x-a|<\min(R_1,R_2)$.
````

## 5. Move correction/commentary into the separate editorial record; keep the actual correction in the reading text.

### Before

````text
[Corrected: the source’s bound $M(|x|/r)^m$ has ratio one at the endpoints and does not establish uniform convergence on the claimed closed interval.]
````
### After

````text

````

## 6. Move correction/commentary into the separate editorial record; keep the actual correction in the reading text.

### Before

````text
[Corrected: the final calculation retains the $x$ multiplying its linear coefficient; the constant and linear terms cannot be combined.]
````
### After

````text

````
