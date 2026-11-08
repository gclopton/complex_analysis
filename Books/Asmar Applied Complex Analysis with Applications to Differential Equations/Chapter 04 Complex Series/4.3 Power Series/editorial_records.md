
# Editorial records

Reading note: 4.3 Power Series.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Callout 173: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Convergence Trichotomy for a Complex Power Series
> The coefficients and variable are complex.
>
> Given a power series $\sum_{n=0}^{\infty} c_{n}\left(z-z_{0}\right)^{n}$, there are only three possibilities:
> (i) The series converges absolutely for all $z$.
> (ii) The series converges only at $z=z_{0}$.
> (iii) There is a number $R>0$ such that the series converges absolutely if $\left|z-z_{0}\right|<R$ and diverges if $\left|z-z_{0}\right|>R$.
````
### After

````text
> [!theorem] Convergence of Power Series
> The coefficients and variable are complex.
>
> Given a power series $\sum_{n=0}^{\infty} c_{n}\left(z-z_{0}\right)^{n}$, there are only three possibilities:
> (i) The series converges absolutely for all $z$.
> (ii) The series converges only at $z=z_{0}$.
> (iii) There is a number $R>0$ such that the series converges absolutely if $\left|z-z_{0}\right|<R$ and diverges if $\left|z-z_{0}\right|>R$.
````

## 2. Callout 174: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Uniform Convergence of Complex Power Series on Closed Subdisks
> Suppose that the power series $\sum_{n=0}^{\infty} c_{n}\left(z-z_{0}\right)^{n}$ has radius of convergence $R>0$. Then the power series converges absolutely and uniformly on any closed subdisk $\left|z-z_{0}\right| \leq r$, where $0<r<R$. Consequently, the power series converges uniformly on any closed and bounded subset of its disk of convergence.
````
### After

````text
> [!theorem] Uniform Convergence of Subdisks
> Suppose that the power series $\sum_{n=0}^{\infty} c_{n}\left(z-z_{0}\right)^{n}$ has radius of convergence $R>0$. Then the power series converges absolutely and uniformly on any closed subdisk $\left|z-z_{0}\right| \leq r$, where $0<r<R$. Consequently, the power series converges uniformly on any closed and bounded subset of its disk of convergence.
````

## 3. Callout 175: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Termwise Complex Path Integration of a Power Series
> Let $R>0$ denote the radius of convergence of the power series $\sum_{n=0}^{\infty} c_{n}\left(z-z_{0}\right)^{n}$. Let $\gamma$ be any path in the disk of convergence $\left|z-z_{0}\right|<R$. Then
> $$
> \int_{\gamma}\left(\sum_{n=0}^{\infty} c_{n}\left(z-z_{0}\right)^{n}\right) d z=\sum_{n=0}^{\infty} c_{n} \int_{\gamma}\left(z-z_{0}\right)^{n} d z
> $$
> That is, the power series may be integrated term by term within its radius of convergence.
````
### After

````text
> [!theorem] Term-by-Term Integration
> Let $R>0$ denote the radius of convergence of the power series $\sum_{n=0}^{\infty} c_{n}\left(z-z_{0}\right)^{n}$. Let $\gamma$ be any path in the disk of convergence $\left|z-z_{0}\right|<R$. Then
> $$
> \int_{\gamma}\left(\sum_{n=0}^{\infty} c_{n}\left(z-z_{0}\right)^{n}\right) d z=\sum_{n=0}^{\infty} c_{n} \int_{\gamma}\left(z-z_{0}\right)^{n} d z
> $$
> That is, the power series may be integrated term by term within its radius of convergence.
````

## 4. Callout 176: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Analyticity and Termwise Differentiation of Complex Power Series
> Suppose that $f(z)=\sum_{n=0}^{\infty} c_{n}\left(z-z_{0}\right)^{n}$ is a power series with radius of convergence $R>0$. Then $f$ is analytic on the disk of convergence $\left|z-z_{0}\right|< R$. Moreover, for any integer $k \geq 1$, the power series may be differentiated $k$ times term by term within its radius of convergence to yield, for $\left|z-z_{0}\right|<R$,
>
> $$
> f^{(k)}(z)=\sum_{n=k}^{\infty} n(n-1) \cdots(n-k+1) c_{n}\left(z-z_{0}\right)^{n-k}
> $$
>
> with radius of convergence $R$.
````
### After

````text
> [!theorem] Analyticity and Termwise Differentiation of Power Series
> Suppose that $f(z)=\sum_{n=0}^{\infty} c_{n}\left(z-z_{0}\right)^{n}$ is a power series with radius of convergence $R>0$. Then $f$ is analytic on the disk of convergence $\left|z-z_{0}\right|< R$. Moreover, for any integer $k \geq 1$, the power series may be differentiated $k$ times term by term within its radius of convergence to yield, for $\left|z-z_{0}\right|<R$,
>
> $$
> f^{(k)}(z)=\sum_{n=k}^{\infty} n(n-1) \cdots(n-k+1) c_{n}\left(z-z_{0}\right)^{n-k}
> $$
>
> with radius of convergence $R$.
````

## 5. Callout 177: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!corollary] Taylor Coefficients of a Complex Power Series
> If $f(z)=\sum_{n=0}^{\infty} c_{n}\left(z-z_{0}\right)^{n}$ is a power series with radius of convergence $R>0$, then the coefficients $c_{n}$ are given by the Taylor formula
>
> $$
> c_{n}=\frac{f^{(n)}\left(z_{0}\right)}{n!} \quad(n=0,1,2, \ldots)
> $$
>
> with the usual convention: $f^{(0)}(z)=f(z)$ and $0!=1$.
````
### After

````text
> [!corollary] Taylor Coefficients
> If $f(z)=\sum_{n=0}^{\infty} c_{n}\left(z-z_{0}\right)^{n}$ is a power series with radius of convergence $R>0$, then the coefficients $c_{n}$ are given by the Taylor formula
>
> $$
> c_{n}=\frac{f^{(n)}\left(z_{0}\right)}{n!} \quad(n=0,1,2, \ldots)
> $$
>
> with the usual convention: $f^{(0)}(z)=f(z)$ and $0!=1$.
````

## 6. Callout 178: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Uniqueness of Complex Power Series Coefficients
> Let $R>0$. If two complex power series satisfy
>
> $$
> \sum_{n=0}^{\infty}a_n(z-z_0)^n=f(z)=\sum_{n=0}^{\infty}b_n(z-z_0)^n,\qquad |z-z_0|<R,
> $$
>
> then $a_n=b_n$ for every $n\geq0$. In particular, a power series $f(z)=\sum_{n=0}^{\infty}c_n(z-z_0)^n$ is identically zero on this disk if and only if every coefficient $c_n$ is zero.
````
### After

````text
> [!theorem] Uniqueness
> If $\sum_{n=0}^{\infty} a_{n}\left(z-z_{0}\right)^{n}=f(z)=\sum_{n=0}^{\infty} b_{n}\left(z-z_{0}\right)^{n}$ for all $\left|z-z_{0}\right|<R$ where $R>0$, then $a_{n}=b_{n}$ for all $n$. In particular, if $f(z)=\sum_{n=0}^{\infty} c_{n}\left(z-z_{0}\right)^{n}$ for all $\left|z-z_{0}\right|<R$, then $f(z)$ is identically 0 for all $\left|z-z_{0}\right|<R$ if and only if $c_{n}=0$ for all $n$.
````

## 7. Callout 180: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Cauchy–Hadamard Formula for the Radius of Convergence
> The radius of convergence $R$ of the series $\sum_{n=0}^{\infty} c_{n}\left(z-z_{0}\right)^{n}$ is given by
>
> $$
> \frac{1}{R}=\limsup_{n\to\infty} \sqrt[n]{\left|c_{n}\right|}
> $$
>
> with the convention $\frac{1}{0}=\infty$ and $\frac{1}{\infty}=0$.
````
### After

````text
> [!theorem] Cauchy-Hadamard Formula
> The radius of convergence $R$ of the series $\sum_{n=0}^{\infty} c_{n}\left(z-z_{0}\right)^{n}$ is given by
>
> $$
> \frac{1}{R}=\limsup_{n\to\infty} \sqrt[n]{\left|c_{n}\right|}
> $$
>
> with the convention $\frac{1}{0}=\infty$ and $\frac{1}{\infty}=0$.
````

## 8. Move editorial commentary out of the reading note.

### Before

````text
*Editorial note: [typo fixed] Restored the exponent n in both power series.*
````
### After

````text

````

## 9. Move editorial commentary out of the reading note.

### Before

````text
*Editorial note: [typo fixed] Repaired garbled “where R>0” and “for all” in the transcription.*
````
### After

````text

````
