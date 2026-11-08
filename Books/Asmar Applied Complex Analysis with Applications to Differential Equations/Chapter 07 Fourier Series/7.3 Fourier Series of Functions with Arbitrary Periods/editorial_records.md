
# Editorial records

Reading note: 7.3 Fourier Series of Functions with Arbitrary Periods.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Callout 261: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Fourier Series Representation for an Arbitrary Period
> Let $p>0$; $f(x\pm)$ denote one-sided limits.
>
> Suppose that $f$ is a $2 p$-periodic piecewise smooth function. Then $f$ has a unique Fourier series representation
>
> $$
> \frac{f(x-)+f(x+)}{2}=a_0+\sum_{n=1}^{\infty}\left(a_n \cos \frac{n \pi}{p} x+b_n \sin \frac{n \pi}{p} x\right),
> $$
>
> where the Fourier coefficients are given by
>
> $$
> a_0=\frac{1}{2 p} \int_{-p}^p f(x) d x
> $$
>
> $$
> a_n=\frac{1}{p} \int_{-p}^p f(x) \cos \frac{n \pi}{p} x d x \quad(n=1,2, \ldots),
> $$
>
> $$
> b_n=\frac{1}{p} \int_{-p}^p f(x) \sin \frac{n \pi}{p} x d x \quad(n=1,2, \ldots)
> $$
>
> If $f$ is continuous at $x$, then the Fourier series converges to $f(x)$. The series converges uniformly for all $x$ if and only if $f$ is continuous for all $x$.
````
### After

````text
> [!theorem] Fourier Series Representation: Arbitrary Period
> Let $p>0$; $f(x\pm)$ denote one-sided limits.
>
> Suppose that $f$ is a $2 p$-periodic piecewise smooth function. Then $f$ has a unique Fourier series representation
>
> $$
> \frac{f(x-)+f(x+)}{2}=a_0+\sum_{n=1}^{\infty}\left(a_n \cos \frac{n \pi}{p} x+b_n \sin \frac{n \pi}{p} x\right),
> $$
>
> where the Fourier coefficients are given by
>
> $$
> a_0=\frac{1}{2 p} \int_{-p}^p f(x) d x
> $$
>
> $$
> a_n=\frac{1}{p} \int_{-p}^p f(x) \cos \frac{n \pi}{p} x d x \quad(n=1,2, \ldots),
> $$
>
> $$
> b_n=\frac{1}{p} \int_{-p}^p f(x) \sin \frac{n \pi}{p} x d x \quad(n=1,2, \ldots)
> $$
>
> If $f$ is continuous at $x$, then the Fourier series converges to $f(x)$. The series converges uniformly for all $x$ if and only if $f$ is continuous for all $x$.
````

## 2. Callout 263: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!property] Parity of Products of Even and Odd Functions
> On a domain symmetric about zero, the pointwise product of two even functions is even; the product of an even and an odd function is odd; and the product of two odd functions is even.
````
### After

````text
> [!property] Parity of Products of Even and Odd Functions
> For pointwise products of functions on a domain symmetric about zero,
>
> $$
> \begin{aligned}
> (\text { Even })(\text { Even }) & =\text { Even } \\
> (\text { Even })(\text { Odd }) & =\text { Odd } \\
> (\text { Odd })(\text { Odd }) & =\text { Even }
> \end{aligned}
> $$
````

## 3. Callout 264: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Cosine and Sine Fourier Series of Even and Odd Periodic Functions
> Let $p>0$. Suppose $f$ is $2p$-periodic and has a convergent Fourier representation $f(x)=a_0+\sum_{n=1}^{\infty}(a_n\cos(n\pi x/p)+b_n\sin(n\pi x/p))$ at every $x$, with its Fourier coefficients. Then (i) $f$ is even if and only if $b_n=0$ for all $n$. In this case
>
> $$
> f(x)=a_0+\sum_{n=1}^{\infty} a_n \cos \frac{n \pi}{p} x,
> $$
>
> where
>
> $$
> a_0=\frac{1}{p} \int_0^p f(x) d x, \quad \text { and } \quad a_n=\frac{2}{p} \int_0^p f(x) \cos \frac{n \pi}{p} x d x \quad(n=1,2, \ldots)
> $$
>
> (ii) $f$ is odd if and only if $a_n=0$ for all $n\geq0$. In this case
>
> $$
> f(x)=\sum_{n=1}^{\infty} b_n \sin \frac{n \pi}{p} x
> $$
>
> where
>
> $$
> b_n=\frac{2}{p} \int_0^p f(x) \sin \frac{n \pi}{p} x d x \quad(n=1,2, \ldots)
> $$
````
### After

````text
> [!theorem] Fourier Series of Even and Odd Functions
> Let $p>0$. Suppose $f$ is $2p$-periodic and has a convergent Fourier representation $f(x)=a_0+\sum_{n=1}^{\infty}(a_n\cos(n\pi x/p)+b_n\sin(n\pi x/p))$ at every $x$, with its Fourier coefficients. Then (i) $f$ is even if and only if $b_n=0$ for all $n$. In this case
>
> $$
> f(x)=a_0+\sum_{n=1}^{\infty} a_n \cos \frac{n \pi}{p} x,
> $$
>
> where
>
> $$
> a_0=\frac{1}{p} \int_0^p f(x) d x, \quad \text { and } \quad a_n=\frac{2}{p} \int_0^p f(x) \cos \frac{n \pi}{p} x d x \quad(n=1,2, \ldots)
> $$
>
> (ii) $f$ is odd if and only if $a_n=0$ for all $n\geq0$. In this case
>
> $$
> f(x)=\sum_{n=1}^{\infty} b_n \sin \frac{n \pi}{p} x
> $$
>
> where
>
> $$
> b_n=\frac{2}{p} \int_0^p f(x) \sin \frac{n \pi}{p} x d x \quad(n=1,2, \ldots)
> $$
````

## 4. Move editorial commentary out of the reading note.

### Before

````text
*Editorial corrections to source details: The sum in Exercise 6 begins at $n=1$; Exercise 8 requires $d>0$. In Example 3 the scaling factor is $2c/\pi$. Exercise 26’s differentiated series equals $f^{\prime}$ at continuity points of the derivative and its one-sided average at derivative jumps.*
````
### After

````text

````
