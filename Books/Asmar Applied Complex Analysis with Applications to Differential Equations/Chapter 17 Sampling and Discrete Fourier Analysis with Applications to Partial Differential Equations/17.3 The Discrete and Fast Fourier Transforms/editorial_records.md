
# Editorial records

Reading note: 17.3 The Discrete and Fast Fourier Transforms.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!definition] Unitary Discrete Fourier Transform with Positive Exponential Convention
> Let $N\ge1$ be an integer and $x=(x(0),\ldots,x(N-1))\in\mathbb C^N$. The unitary discrete Fourier transform with positive exponential convention is the sequence $X=\mathcal F_Nx$ defined by
>
> $$
> X(k)=\frac1{\sqrt N}\sum_{j=0}^{N-1}x(j)e^{2\pi ijk/N},\qquad k=0,\ldots,N-1.
> $$
>
> The sign and normalization are part of this convention.
````
### After

````text
> [!definition] Discrete Fourier Transform
> Given an $N$-sequence $x=(x(0), x(1), \ldots, x(N-1))$, we define the $N$-point discrete Fourier transform of $x$, abbreviated DFT, by
> $\quad X(k)=\frac{1}{\sqrt{N}} \sum_{j=0}^{N-1} x(j) e^{2 \pi i j \frac{k}{N}}, \quad k=0,1, \ldots, N-1$.
>
> Thus the DFT of an $N$-sequence $x$ is another $N$-sequence of complex numbers $X=(X(0), X(1) \ldots X(N-1))$. We will also use the notation $X=\mathcal{F}_{N}(x)$.
````

## 2. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!definition] Inverse of the Unitary Positive-Exponent Discrete Fourier Transform
> For an integer $N\ge1$ and $X\in\mathbb C^N$, define
>
> $$
> (\mathcal F_N^{-1}X)(k)=\frac1{\sqrt N}\sum_{j=0}^{N-1}X(j)e^{-2\pi ijk/N},\qquad k=0,\ldots,N-1.
> $$
>
> This is the negative-exponent unitary transform, inverse to $(\mathcal F_Nx)(k)=N^{-1/2}\sum_{j=0}^{N-1}x(j)e^{2\pi ijk/N}$.
````
### After

````text
> [!definition] Inverse Discrete Fourier Transform
> Like other transforms that we have encountered previously, the DFT has an inverse, known as the inverse discrete Fourier transform (IDFT), given by
> $\quad \mathcal{F}_{N}^{-1}(X)(k)=\frac{1}{\sqrt{N}} \sum_{j=0}^{N-1} X(j) e^{-2 \pi i j \frac{k}{N}}, \quad k=0,1, \ldots N-1$.
>
> Here $N\ge1$, $(\mathcal F_Nx)(k)=N^{-1/2}\sum_{j=0}^{N-1}x(j)e^{2\pi ijk/N}$ and $(\mathcal F_N^{-1}X)(k)=N^{-1/2}\sum_{j=0}^{N-1}X(j)e^{-2\pi ijk/N}$.
````

## 3. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem] Inversion and Uniqueness of the Unitary Discrete Fourier Transform
> For an integer $N\ge1$, define $(\mathcal F_Nx)(k)=N^{-1/2}\sum_{j=0}^{N-1}x(j)e^{2\pi ijk/N}$ and $(\mathcal F_N^{-1}X)(k)=N^{-1/2}\sum_{j=0}^{N-1}X(j)e^{-2\pi ijk/N}$ for $k=0,\ldots,N-1$. Then every $x\in\mathbb C^N$ satisfies
>
> $$
> \mathcal F_N^{-1}(\mathcal F_Nx)=x.
> $$
>
> Consequently, $\mathcal F_Nx=\mathcal F_Ny$ implies $x=y$.
````
### After

````text
> [!theorem] Inversion of the DFT
> For any $N$-sequence $x$ we have
>
> $$
> \mathcal{F}_{N}^{-1}\left(\mathcal{F}_{N}(x)\right)(k)=x(k), \quad k=0,1, \ldots, N-1
> $$
>
> As an immediate consequence we get the uniqueness property of the DFT, which states that if $x$ and $y$ are two $N$-sequences such that $X=Y$, then $x=y$.
>
> Here $N\ge1$, $(\mathcal F_Nx)(k)=N^{-1/2}\sum_{j=0}^{N-1}x(j)e^{2\pi ijk/N}$ and $(\mathcal F_N^{-1}X)(k)=N^{-1/2}\sum_{j=0}^{N-1}X(j)e^{-2\pi ijk/N}$.
````

## 4. Restore source wording; retain only the actual correction.

### Before

````text
The source’s inversion theorem is proved in the appendix below.
````
### After

````text
The proof is presented in the appendix at the end of the section.
````

## 5. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!definition] Normalized Cyclic Convolution of Finite Complex Sequences
> Let $N\ge1$ be an integer and $x,y\in\mathbb C^N$, extended to all integer indices with period $N$. Their normalized cyclic convolution is
>
> $$
> (x*y)(k)=\frac1{\sqrt N}\sum_{j=0}^{N-1}x(j)y(k-j),\qquad k=0,\ldots,N-1.
> $$
>
> The index $k-j$ is taken modulo $N$.
````
### After

````text
> [!definition] Normalized Cyclic Convolution of Finite Complex Sequences
> Given two $N$-sequences $x$ and $y$, with both viewed as $N$-periodic sequences on the integers, we can define their convolution by
>
> $$
> (x*y)(k)=\frac{1}{\sqrt{N}} \sum_{j=0}^{N-1} x(j) y(k-j) . \quad k=0,1, \ldots N-1
> $$
````

## 6. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem] Convolution Theorem for the Unitary Positive-Exponent Discrete Fourier Transform
> For an integer $N\ge1$, let $x,y\in\mathbb C^N$ have $N$-periodic extensions, define
>
> $$
> (\mathcal F_Nx)(k)=\frac1{\sqrt N}\sum_{j=0}^{N-1}x(j)e^{2\pi ijk/N},\qquad
> (x*y)(k)=\frac1{\sqrt N}\sum_{j=0}^{N-1}x(j)y(k-j),
> $$
>
> and put $X=\mathcal F_Nx$, $Y=\mathcal F_Ny$. Then
>
> $$
> \mathcal F_N(x*y)=XY,\qquad \mathcal F_N^{-1}(XY)=x*y,
> $$
>
> where $XY$ is pointwise multiplication and $(\mathcal F_N^{-1}Z)(k)=N^{-1/2}\sum_{j=0}^{N-1}Z(j)e^{-2\pi ijk/N}$.
````
### After

````text
> [!theorem] Transforms of Convolutions
> For any two $N$-sequences $x$ and $y$ we have
>
> $$
> \mathcal{F}_{N}(x * y)=\mathcal{F}_{N}(x) \mathcal{F}_{N}(y),
> $$
>
> and
>
> $$
> \mathcal{F}_{N}^{-1}(X Y)=x * y
> $$
>
> Here $N\ge1$, $(\mathcal F_Nx)(k)=N^{-1/2}\sum_{j=0}^{N-1}x(j)e^{2\pi ijk/N}$ and $(\mathcal F_N^{-1}X)(k)=N^{-1/2}\sum_{j=0}^{N-1}X(j)e^{-2\pi ijk/N}$. Here $X=\mathcal F_Nx$, $Y=\mathcal F_Ny$, and $(x*y)(k)=N^{-1/2}\sum_{j=0}^{N-1}x(j)y(k-j)$ uses periodic indices.
````
