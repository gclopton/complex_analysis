
# Editorial records

Reading note: 4.7 Harmonic Functions and Fourier Series.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Callout 200: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!lemma] Fourier Series of the Poisson Kernel for a Disk
> Let $R>0$ and define the disk Poisson kernel by $P(r,\theta)=(R^2-r^2)/(R^2-2rR\cos\theta+r^2)$.
>
> For $0 \leq r<R$ and all $\theta$, we have
>
> $$
> P(r, \theta)=\operatorname{Re}\left(\frac{R+r e^{i \theta}}{R-r e^{i \theta}}\right)=1+2 \sum_{n=1}^{\infty}\left(\frac{r}{R}\right)^{n} \cos n \theta .
> $$
````
### After

````text
> [!lemma] Series Form of the Poisson Kernel
> Let $R>0$ and define the disk Poisson kernel by $P(r,\theta)=(R^2-r^2)/(R^2-2rR\cos\theta+r^2)$.
>
> For $0 \leq r<R$ and all $\theta$, we have
>
> $$
> P(r, \theta)=\operatorname{Re}\left(\frac{R+r e^{i \theta}}{R-r e^{i \theta}}\right)=1+2 \sum_{n=1}^{\infty}\left(\frac{r}{R}\right)^{n} \cos n \theta .
> $$
````

## 2. Callout 201: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Fourier Series Representation of the Poisson Extension on a Disk
> Let $R>0$ and let $f$ be real-valued, $2\pi$-periodic, and piecewise continuous. Its Poisson extension is harmonic in $|z|<R$, approaches $f(\theta)$ radially at continuity points, and is given by
> $\quad u(r, \theta)=a_{0}+\sum_{n=1}^{\infty}\left(\frac{r}{R}\right)^{n}\left(a_{n} \cos n \theta+b_{n} \sin n \theta\right), \quad 0 \leq r<R$,
> where $a_{0}, a_{n}$, and $b_{n}$ are the Fourier coefficients of $f$, given by the following:
>
> $$a_0=\frac{1}{2 \pi} \int_0^{2 \pi} f(\theta) d \theta; $$
> $$
> a_n=\frac{1}{\pi} \int_0^{2 \pi} f(\theta) \cos n \theta d \theta \quad(n=1,2, \ldots); 
> $$
>
> $$
> b_n=\frac{1}{\pi} \int_0^{2 \pi} f(\theta) \sin n \theta d \theta \quad(n=1,2, \ldots). 
> $$
````
### After

````text
> [!theorem] Fourier Series Form of the Poisson Integral Formula
> Let $R>0$ and let $f$ be real-valued, $2\pi$-periodic, and piecewise continuous. Its Poisson extension is harmonic in $|z|<R$, approaches $f(\theta)$ radially at continuity points, and is given by
> $\quad u(r, \theta)=a_{0}+\sum_{n=1}^{\infty}\left(\frac{r}{R}\right)^{n}\left(a_{n} \cos n \theta+b_{n} \sin n \theta\right), \quad 0 \leq r<R$,
> where $a_{0}, a_{n}$, and $b_{n}$ are the Fourier coefficients of $f$, given by the following:
>
> $$a_0=\frac{1}{2 \pi} \int_0^{2 \pi} f(\theta) d \theta; $$
> $$
> a_n=\frac{1}{\pi} \int_0^{2 \pi} f(\theta) \cos n \theta d \theta \quad(n=1,2, \ldots); 
> $$
>
> $$
> b_n=\frac{1}{\pi} \int_0^{2 \pi} f(\theta) \sin n \theta d \theta \quad(n=1,2, \ldots). 
> $$
````
