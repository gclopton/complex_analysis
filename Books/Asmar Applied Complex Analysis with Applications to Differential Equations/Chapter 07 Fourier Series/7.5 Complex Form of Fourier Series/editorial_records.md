
# Editorial records

Reading note: 7.5 Complex Form of Fourier Series.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Callout 266: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem|655a1864-1618-519a-aa4a-65896981c6cf.local at=e6249e7b-f9ca-5ac6-aef3-f9bbd75ecc6b] Complex Exponential Fourier Series for an Arbitrary Period
> Let $p>0$. The bilateral Fourier series is summed symmetrically as $\lim_{N\to\infty}\sum_{n=-N}^{N}$.
>
> Let $f$ be a $2 p$-periodic piecewise smooth function. The complex form of the Fourier series of $f$ is
>
> $$
> \sum_{n=-\infty}^{\infty} c_n e^{i \frac{n \pi}{p} x},
> $$
>
> where the Fourier coefficients $c_n$ are given by
>
> $$
> c_n=\frac{1}{2 p} \int_{-p}^p f(t) e^{-i \frac{n \pi}{p} t} d t \quad(n=0, \pm 1, \pm 2, \ldots) .
> $$
>
> For all $x$, the Fourier series converges to $f(x)$ if $f$ is continuous at $x$, and to $\frac{f(x+)+f(x-)}{2}$ otherwise. Moreover, the Fourier series converges to $f(x)$ uniformly for all $x$ if and only if $f$ is continuous for all $x$ (and piecewise smooth).
````
### After

````text
> [!theorem|655a1864-1618-519a-aa4a-65896981c6cf.local at=e6249e7b-f9ca-5ac6-aef3-f9bbd75ecc6b] Complex Form of Fourier Series
> Let $p>0$. The bilateral Fourier series is summed symmetrically as $\lim_{N\to\infty}\sum_{n=-N}^{N}$.
>
> Let $f$ be a $2 p$-periodic piecewise smooth function. The complex form of the Fourier series of $f$ is
>
> $$
> \sum_{n=-\infty}^{\infty} c_n e^{i \frac{n \pi}{p} x},
> $$
>
> where the Fourier coefficients $c_n$ are given by
>
> $$
> c_n=\frac{1}{2 p} \int_{-p}^p f(t) e^{-i \frac{n \pi}{p} t} d t \quad(n=0, \pm 1, \pm 2, \ldots) .
> $$
>
> For all $x$, the Fourier series converges to $f(x)$ if $f$ is continuous at $x$, and to $\frac{f(x+)+f(x-)}{2}$ otherwise. Moreover, the Fourier series converges to $f(x)$ uniformly for all $x$ if and only if $f$ is continuous for all $x$ (and piecewise smooth).
````

## 2. Callout 268: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem|2aabf1a7-be36-53ee-8acb-62dca5a31fea.local at=8eacc40f-716c-56b7-af51-833a069efc00] Fourier Coefficients of Normalized Periodic Convolution
> For a periodic function $h$, write $\widehat h(n)=(2p)^{-1}\int_{-p}^{p}h(t)e^{-in\pi t/p}\,dt$.
>
> Let $p>0$. The normalized periodic convolution is $(f*g)(x)=(2p)^{-1}\int_{-p}^{p}f(t)g(x-t)\,dt$.
>
> Let $f$ and $g$ be $2 p$-periodic, piecewise smooth functions. Then
>
> $$
> \widehat{f * g}(n)=\widehat{f}(n) \widehat{g}(n) \quad n=0, \pm 1, \pm 2, \ldots .
> $$
````
### After

````text
> [!theorem|2aabf1a7-be36-53ee-8acb-62dca5a31fea.local at=8eacc40f-716c-56b7-af51-833a069efc00] Fourier Coefficients of Convolutions
> For a periodic function $h$, write $\widehat h(n)=(2p)^{-1}\int_{-p}^{p}h(t)e^{-in\pi t/p}\,dt$.
>
> Let $p>0$. The normalized periodic convolution is $(f*g)(x)=(2p)^{-1}\int_{-p}^{p}f(t)g(x-t)\,dt$.
>
> Let $f$ and $g$ be $2 p$-periodic, piecewise smooth functions. Then
>
> $$
> \widehat{f * g}(n)=\widehat{f}(n) \widehat{g}(n) \quad n=0, \pm 1, \pm 2, \ldots .
> $$
````

## 3. Callout 269: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!corollary|ece2da0d-3242-50eb-a13d-c1e81021250f.local at=443c5414-02af-5205-aa76-974b9cef5f3a] Continuity and Piecewise Smoothness of Periodic Convolution
> Let $p>0$. The normalized periodic convolution is $(f*g)(x)=(2p)^{-1}\int_{-p}^{p}f(t)g(x-t)\,dt$.
>
> Let $f$ and $g$ be $2 p$-periodic, piecewise smooth functions. Then $f * g$ is continuous and piecewise smooth.
````
### After

````text
> [!corollary|ece2da0d-3242-50eb-a13d-c1e81021250f.local at=443c5414-02af-5205-aa76-974b9cef5f3a] Continuity of Convolutions
> Let $p>0$. The normalized periodic convolution is $(f*g)(x)=(2p)^{-1}\int_{-p}^{p}f(t)g(x-t)\,dt$.
>
> Let $f$ and $g$ be $2 p$-periodic, piecewise smooth functions. Then $f * g$ is continuous and piecewise smooth.
````

## 4. Callout 271: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!corollary|f6679090-fcb0-5028-8824-c4579a5fba52.local at=62251ac9-da98-50d9-a85d-6d67e14caea1] Parseval's Identity for Real Periodic Functions
> Let $p>0$ and let $f$ be an integrable $2p$-periodic function. Use coefficients
>
> $$
> a_0=\frac1{2p}\int_{-p}^{p}f(t)\,dt,\qquad a_n=\frac1p\int_{-p}^{p}f(t)\cos\frac{n\pi t}{p}\,dt,\qquad b_n=\frac1p\int_{-p}^{p}f(t)\sin\frac{n\pi t}{p}\,dt\quad(n\geq1),
> $$
>
> and $c_n=(2p)^{-1}\int_{-p}^{p}f(t)e^{-in\pi t/p}\,dt$ for integer $n$.
>
> Let $f$ be a real-valued $2 p$-periodic piecewise smooth function on $[-p, p]$. Let $a_n, b_n$, and $c_n$ denote, respectively, the cosine, the sine, and the complex Fourier coefficients of $f$. Then
>
> $$
> \frac{1}{2 p} \int_{-p}^p f(x)^2 d x=\sum_{n=-\infty}^{\infty}\left|c_n\right|^2=a_0^2+\frac12\sum_{n=1}^{\infty}\left(a_n^2+b_n^2\right)
> $$
````
### After

````text
> [!corollary|f6679090-fcb0-5028-8824-c4579a5fba52.local at=62251ac9-da98-50d9-a85d-6d67e14caea1] Parseval's Identity
> Let $p>0$ and let $f$ be an integrable $2p$-periodic function. Use coefficients
>
> $$
> a_0=\frac1{2p}\int_{-p}^{p}f(t)\,dt,\qquad a_n=\frac1p\int_{-p}^{p}f(t)\cos\frac{n\pi t}{p}\,dt,\qquad b_n=\frac1p\int_{-p}^{p}f(t)\sin\frac{n\pi t}{p}\,dt\quad(n\geq1),
> $$
>
> and $c_n=(2p)^{-1}\int_{-p}^{p}f(t)e^{-in\pi t/p}\,dt$ for integer $n$.
>
> Let $f$ be a real-valued $2 p$-periodic piecewise smooth function on $[-p, p]$. Let $a_n, b_n$, and $c_n$ denote, respectively, the cosine, the sine, and the complex Fourier coefficients of $f$. Then
>
> $$
> \frac{1}{2 p} \int_{-p}^p f(x)^2 d x=\sum_{n=-\infty}^{\infty}\left|c_n\right|^2=a_0^2+\frac12\sum_{n=1}^{\infty}\left(a_n^2+b_n^2\right)
> $$
````

## 5. Move editorial commentary out of the reading note.

### Before

````text
*Editorial clarifications: Exercise 10(b) allows isolated changes of values unless continuity is assumed. The final theorem’s proof is explicitly reduced to period $2\pi$ and uses Bessel’s inequality for $f^{\prime}$, whose derivative need not exist. Other source corrections include the missing Parseval factor and the removable value at the origin in Exercise 26.*
````
### After

````text

````

## 6. Move editorial commentary out of the reading note.

### Before

````text
*Editorial note: [source typo corrected] Inserted the missing factor 1/2 on the sum of squared real Fourier coefficients, required by the displayed coefficient normalization.*
````
### After

````text

````

## 7. Move editorial commentary out of the reading note.

### Before

````text
*Editorial correction: the bound includes all jumps; the printed constant $4M$ need not cover an arbitrary number of discontinuities.*
````
### After

````text

````

## 8. Move editorial commentary out of the reading note.

### Before

````text
*Editorial correction: the source’s extension of the differentiation formula to discontinuous factors omits these jump terms.*
````
### After

````text

````

## Additional source comparison

## 1. Restore source proof wording and method while retaining the correction for jump terms and coefficient bounds.

### Before

````text
If $f$ and $g$ are merely piecewise smooth, split the integral at their breakpoints and include the moving-boundary terms when differentiating. Write $g'_\mathrm{reg}$ for the ordinary derivative on the smooth pieces and $\Delta g(t_j)=g(t_j+)-g(t_j-)$ for the jumps in one period (including the periodic endpoint if necessary). Away from the finitely many translated breakpoints,

$$
(f*g)'(x)=(f*g'_\mathrm{reg})(x)+\frac1{2p}\sum_j\Delta g(t_j)f(x-t_j).
$$

The integral term is continuous and the finite sum is piecewise continuous, so the convolution is piecewise smooth. The formula without jump terms applies when the differentiated factor is continuous.
````
### After

````text
If $f$ and $g$ are merely piecewise smooth, we can write the convolution integral as a sum of integrals over intervals on which $f$ and $g$ are continuous with continuous derivatives, and then differentiate under the integral sign, including the endpoint terms from the moving breakpoints. So, in general, the convolution is piecewise smooth.
````

## 2. Restore source proof wording and method while retaining the correction for jump terms and coefficient bounds.

### Before

````text
**Proof** Piecewise smoothness follows from the corrected differentiation formula above. Continuity also follows directly: if $x_k\to x$, then $g(x_k-t)\to g(x-t)$ except at finitely many $t$ modulo the period, while $|f(t)g(x_k-t)|\leq\|g\|_\infty|f(t)|$. Dominated convergence therefore gives $(f*g)(x_k)\to(f*g)(x)$.

For the source’s Fourier-series argument, integration by parts on each smooth piece, retaining its endpoint and jump terms, gives $|\widehat f(n)|\leq C_f/|n|$ and $|\widehat g(n)|\leq C_g/|n|$ for $n\ne0$, where the constants depend on the functions and the period. Consequently $|\widehat{f*g}(n)|\leq C_fC_g/n^2$. The Weierstrass $M$-test gives uniform convergence of $\sum_{n=-\infty}^{\infty}\widehat f(n)\widehat g(n)e^{in\pi x/p}$.


---
````
### After

````text
**Proof** We have already showed that $f * g$ is piecewise smooth with the endpoint terms from moving breakpoints included when differentiating at all but finitely many points in $[-p, p]$. To show that it is continuous, we note that if $|f|$ and $\left|f^{\prime}\right|$ are bounded, say by $M$, then $|\widehat{f}(n)|\leq C/|n|$ for $n\ne0$, where $C$ includes the finitely many jumps, which follows by integrating by parts on each smooth interval in (4). The details are left as an exercise. So $|\widehat{f * g}(n)|=|\widehat{f}(n)||\widehat{g}(n)| \leq A \frac{1}{n} \frac{1}{n}=\frac{A}{n^{2}}$, where $A$ is a constant. We now apply the Weierstrass $M$-test to the Fourier series of $f * g(x)$, which is $\sum_{-\infty}^{\infty} \widehat{f}(n) \widehat{g}(n) e^{i \frac{n \pi}{p}x}$, and conclude that the series converges uniformly for all $x$, implying that $f * g(x)$ is continuous, by Theorem 1.
````
