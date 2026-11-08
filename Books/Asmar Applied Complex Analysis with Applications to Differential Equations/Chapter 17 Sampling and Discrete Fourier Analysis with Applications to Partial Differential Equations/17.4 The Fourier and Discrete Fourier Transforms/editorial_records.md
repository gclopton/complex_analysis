
# Editorial records

Reading note: 17.4 The Fourier and Discrete Fourier Transforms.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!procedure] Approximate a Continuous Fourier Transform Using a Unitary IDFT
> Use the continuous transform $\widehat f(\omega)=(2\pi)^{-1/2}\int_{\mathbb R}f(x)e^{-i\omega x}\,dx$. Suppose $f$ is integrable and sufficiently regular for the sampled quadrature below.
>
> 1. Choose a window length $M>0$ so the tails outside $[-M/2,M/2]$ are acceptably small, and an even sample count $N$. A power of two is convenient for a radix-two FFT. Set $h=M/N$.
> 2. Form the wrapped samples $a_j=f(jh)$ for $0\le j<N/2$ and $a_j=f(jh-M)$ for $N/2\le j<N$.
> 3. Compute the negative-exponent unitary transform
>
> $$
> b_k=\frac1{\sqrt N}\sum_{j=0}^{N-1}a_j e^{-2\pi ijk/N},\qquad k=0,\ldots,N-1.
> $$
>
> 4. Set $q_k=k$ for $0\le k<N/2$ and $q_k=k-N$ for $N/2\le k<N$. Then use
>
> $$
> \widehat f\left(\frac{2\pi q_k}{M}\right)\approx\frac{M}{\sqrt{2\pi N}}b_k.
> $$
>
> The Nyquist bin is assigned to the negative endpoint here; it is one bin, not two independent endpoint values.
> 5. Check convergence by enlarging the window and reducing the sample spacing. Increasing $M$ at fixed $N$ also coarsens the samples, so it need not improve the total error. Control both truncation and quadrature/aliasing errors.
````
### After

````text
> [!procedure] DFT Approximation of the Fourier Transform
> Step 1: Choose and fix $M$ and $N$ with $M>0$ and $N$ even. It is customary to choose $N$ to be a power of 2 .
> Step 2: Form the function $g$ by $g(x)=f(x)$ for $0\le x<M/2$, $g(x)=f(x-M)$ for $M/2\le x<M$, and $g(x)=0$ otherwise. On the $\omega$-axis, mark the points
>
> $$
> \omega=\frac{2 \pi k}{M}, \quad k=0, \pm 1, \ldots, \pm N / 2 .
> $$
>
> Step 3: To approximate the Fourier transform at the points $\omega$ corresponding to $k=0,1, \ldots, N / 2$, use $\hat f(2\pi k/M)\approx M\mathcal F_N^{-1}(g(jM/N))(k)/\sqrt{2N\pi}$.
> Step 4: To approximate the Fourier transform at the points $\omega$ corresponding to $k=-1, \ldots,-\frac{N}{2}+1$, use the periodicity of the DFT in the following form: For $k=1,2,\ldots,N/2-1$,
>
> $$
> \widehat{f}\left(-\frac{2 \pi k}{M}\right) \approx \frac{M}{\sqrt{2 N \pi}} \mathcal{F}_{N}^{-1}\left(g\left(j \frac{M}{N}\right)\right)(N-k) .
> $$
>
> Step 5: For better results, repeat Steps $1-4$ with larger values of $M$ and $N$.
>
> Here $N\ge1$, $(\mathcal F_Nx)(k)=N^{-1/2}\sum_{j=0}^{N-1}x(j)e^{2\pi ijk/N}$ and $(\mathcal F_N^{-1}X)(k)=N^{-1/2}\sum_{j=0}^{N-1}X(j)e^{-2\pi ijk/N}$. Use $\hat f(\omega)=(2\pi)^{-1/2}\int_{\mathbb R}f(x)e^{-i\omega x}\,dx$, interpreted by mean-square extension for $f\in L^2$. Sample the continuous inverse-Fourier representative of a band-limited function. The window must control omitted tails, and $M/N$ must be small enough to control quadrature error. The two Nyquist endpoints share a single bin.
````

## 2. Move correction/commentary into the separate editorial record; keep the actual correction in the reading text.

### Before

````text
[Source clarification: the printed Exercise 5(b) implicitly identifies a function with periodically extended samples. The equality applies to that periodic extension; for a general function on the real line, the wraparound contribution must be controlled. Bold sequences and the index $m-j$ are restored here.]
````
### After

````text

````
