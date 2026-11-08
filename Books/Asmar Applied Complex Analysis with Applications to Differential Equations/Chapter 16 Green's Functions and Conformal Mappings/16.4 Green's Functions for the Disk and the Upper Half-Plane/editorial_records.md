
# Editorial records

Reading note: 16.4 Green's Functions for the Disk and the Upper Half-Plane.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!proposition|7112982e-ecb6-51c2-8bb5-2b1e4132df24.local at=cf51912a-e210-5bfc-9215-22d31a88f591] Distance Ratio for Inversion in a Circle
> Let $R>0$ and $A\in\mathbb R^2$ satisfy $0<|A|<R$. Its inverse in the circle $|P|=R$ is $A^*=R^2A/|A|^2$, lying on the same ray from the origin. For every $P$ on that circle,
>
> $$
> |A-P|=\frac{|A|}{R}|A^*-P|.
> $$
>
> Thus the proportionality constant is $k=|A|/R$.
````
### After

````text
> [!proposition|7112982e-ecb6-51c2-8bb5-2b1e4132df24.local at=cf51912a-e210-5bfc-9215-22d31a88f591] Distance Ratio for Inversion in a Circle
> Let $A=\left(x_{0}, y_{0}\right)$ be a fixed point in $D_{R}$ minus its center and let $A^{*}= \left(x_{0}^{*}, y_{0}^{*}\right)$ be its image by the Steiner inversion. For any point $P=(x, y)$ on $C_{R}$, we have
> $$
> |A-P|=\frac{|A|}{R}\left|A^{*}-P\right|=k \cdot\left|A^{*}-P\right|,
> $$
>
> where $k=\frac{|A|}{R}=\frac{\sqrt{x_{0}^{2}+y_{0}^{2}}}{R}$. Here $D_R=\{P:|P|<R\}$, $C_R=\partial D_R$, $R>0$, and $A^*=R^2A/|A|^2$.
````

## 2. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|7824230a-489f-518c-90b8-6dd44c9aee12.local at=d3d55a19-d8a9-5aa3-a991-c3c51a850555] Poisson Equation on a Disk with Zero Dirichlet Boundary Data
> Let $D_R=\{(x,y):x^2+y^2<R^2\}$ with $R>0$. If $u\in C^2$ near $\overline{D_R}$ satisfies $\Delta u=f$ in $D_R$ and $u=0$ on its boundary, then at $0\le r_0<R$,
>
> $$
> u(r_0,\phi)=\frac1{4\pi}\int_0^{2\pi}\int_0^R f(r,\theta)\log\left[R^2\frac{r^2+r_0^2-2rr_0\cos(\theta-\phi)}{r^2r_0^2+R^4-2rr_0R^2\cos(\theta-\phi)}\right]r\,dr\,d\theta.
> $$
>
> The integral uses polar area measure; the logarithmic singularity at the evaluation point is integrable.
````
### After

````text
> [!theorem|7824230a-489f-518c-90b8-6dd44c9aee12.local at=d3d55a19-d8a9-5aa3-a991-c3c51a850555] Poisson Equation on a Disk with Zero Dirichlet Boundary Data
> Let $f(r, \theta)$ be a smooth function on the disk $D_{R}$. The solution of
>
> $$
> \nabla^{2} u(r, \theta)=f(r, \theta), \quad 0 \leq r<R, 0 \leq \theta \leq 2 \pi,
> $$
>
> with boundary values $u=0$ on $C_{R}$, is
>
> $$
> u\left(r_{0}, \phi\right)=\frac{1}{4 \pi} \int_{0}^{2 \pi} \int_{0}^{R} f(r, \theta) \ln \left[R^{2} \frac{r^{2}+r_{0}^{2}-2 r r_{0} \cos (\theta-\phi)}{r^{2} r_{0}^{2}+R^{4}-2 r r_{0} R^{2} \cos (\theta-\phi)}\right] r d r d \theta
> $$
>
> where $0 \leq r_{0}<R$ and $0 \leq \phi \leq 2 \pi$. Here $D_R$ is the disk of radius $R>0$ centered at the origin and $C_R$ is its boundary.
````

## 3. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|085c8b9c-2da6-5374-b4d0-8218f2dab441.local at=a48455fd-1410-59da-9551-f52b6081645b] Poisson Integral Formula for the Dirichlet Problem on a Disk
> Let $R>0$ and let $f$ be a continuous $2\pi$-periodic real function. The unique function harmonic on $D_R=\{x^2+y^2<R^2\}$ and continuous on $\overline{D_R}$ with boundary values $u(R,\theta)=f(\theta)$ is
>
> $$
> u(r,\phi)=\frac{R^2-r^2}{2\pi}\int_0^{2\pi}\frac{f(\theta)}{R^2+r^2-2rR\cos(\theta-\phi)}\,d\theta,\qquad0\le r<R.
> $$
````
### After

````text
> [!theorem|085c8b9c-2da6-5374-b4d0-8218f2dab441.local at=a48455fd-1410-59da-9551-f52b6081645b] Poisson Integral Formula for the Dirichlet Problem on a Disk
> Suppose that $u$ is harmonic in $D_{R}$ , continuous on $\overline{D_R}$, and $u(R, \theta)=f(\theta)$ on the boundary $C_{R}$. Then
>
> $$
> u(r, \phi)=\frac{R^{2}-r^{2}}{2 \pi} \int_{0}^{2 \pi} \frac{f(\theta)}{R^{2}+r^{2}-2 r R \cos (\theta-\phi)} d \theta
> $$
>
> where $0 \leq r<R$ and $0 \leq \phi \leq 2 \pi$. Here $D_R$ is the disk of radius $R>0$ centered at the origin and $C_R$ is its boundary.
````

## 4. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|1be9f76d-35f8-5d7b-a140-6dc2ab962fd5.local at=9542d3ef-da00-5ce7-9529-328e4ee86e35] Green Potential for the Poisson Equation in the Upper Half-Plane
> Let $H=\{(x,y):y>0\}$ and let $f$ be Hölder continuous with compact support in $H$. The bounded solution of $\Delta u=f$ in $H$ with continuous zero boundary values on $y=0$ is
>
> $$
> u(x_0,y_0)=\frac1{4\pi}\int_0^\infty\int_{-\infty}^\infty f(x,y)\log\frac{(x-x_0)^2+(y-y_0)^2}{(x-x_0)^2+(y+y_0)^2}\,dx\,dy,\qquad y_0>0.
> $$
>
> It tends to zero at infinity. Without a boundedness or growth condition, zero boundary values alone do not guarantee uniqueness on this unbounded domain.
````
### After

````text
> [!theorem|1be9f76d-35f8-5d7b-a140-6dc2ab962fd5.local at=9542d3ef-da00-5ce7-9529-328e4ee86e35] Green Potential for the Poisson Equation in the Upper Half-Plane
> Let $f(x, y)$ be a Hölder continuous function of compact support defined on the upper half-plane. The bounded solution of
>
> $$
> \nabla^{2} u(x,y)=f(x, y), \quad-\infty<x<\infty, 0<y .
> $$
>
> with boundary values $u=0$ on the $x$-axis $(y=0)$, is
>
> $$
> u\left(x_{0}, y_{0}\right)=\frac{1}{4 \pi} \int_{0}^{\infty} \int_{-\infty}^{\infty} f(x, y) \ln \frac{\left(x-x_{0}\right)^{2}+\left(y-y_{0}\right)^{2}}{\left(x-x_{0}\right)^{2}+\left(y+y_{0}\right)^{2}} d x d y
> $$
````

## 5. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|80e9f0c0-0701-5904-a9df-a6cb291067a3.local at=394f2488-c1fc-59a1-9c13-a06dacf708fe] Poisson Integral Formula for Bounded Harmonic Functions in the Upper Half-Plane
> If $f:\mathbb R\to\mathbb R$ is bounded and continuous, the unique bounded harmonic function on $H=\{(x,y):y>0\}$ that extends continuously to $u(x,0)=f(x)$ is
>
> $$
> u(x_0,y)=\frac y\pi\int_{-\infty}^\infty\frac{f(x)}{(x-x_0)^2+y^2}\,dx,\qquad x_0\in\mathbb R,\ y>0.
> $$
````
### After

````text
> [!theorem|80e9f0c0-0701-5904-a9df-a6cb291067a3.local at=394f2488-c1fc-59a1-9c13-a06dacf708fe] Poisson Integral Formula for Bounded Harmonic Functions in the Upper Half-Plane
> Suppose that $u$ is bounded and harmonic in the upper half-plane and extends continuously to $u(x,0)=f(x)$ on the boundary. Then
>
> $$
> u\left(x_{0}, y\right)=\frac{y}{\pi} \int_{-\infty}^{\infty} \frac{f(x)}{\left(x-x_{0}\right)^{2}+y^{2}} d x
> $$
>
> where $-\infty<x_{0}<\infty$ and $0<y$.
````

## 6. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!proposition|7112982e-ecb6-51c2-8bb5-2b1e4132df24.local at=cf51912a-e210-5bfc-9215-22d31a88f591] Distance Ratio for Inversion in a Circle
> Let $A=\left(x_{0}, y_{0}\right)$ be a fixed point in $D_{R}$ minus its center and let $A^{*}= \left(x_{0}^{*}, y_{0}^{*}\right)$ be its image by the Steiner inversion. For any point $P=(x, y)$ on $C_{R}$, we have
> $$
> |A-P|=\frac{|A|}{R}\left|A^{*}-P\right|=k \cdot\left|A^{*}-P\right|,
> $$
>
> where $k=\frac{|A|}{R}=\frac{\sqrt{x_{0}^{2}+y_{0}^{2}}}{R}$. Here $D_R=\{P:|P|<R\}$, $C_R=\partial D_R$, $R>0$, and $A^*=R^2A/|A|^2$.
````
### After

````text
> [!proposition|7112982e-ecb6-51c2-8bb5-2b1e4132df24.local at=cf51912a-e210-5bfc-9215-22d31a88f591] Steiner Inversion
> Let $A=\left(x_{0}, y_{0}\right)$ be a fixed point in $D_{R}$ minus its center and let $A^{*}= \left(x_{0}^{*}, y_{0}^{*}\right)$ be its image by the Steiner inversion. For any point $P=(x, y)$ on $C_{R}$, we have
> $$
> |A-P|=\frac{|A|}{R}\left|A^{*}-P\right|=k \cdot\left|A^{*}-P\right|,
> $$
>
> where $k=\frac{|A|}{R}=\frac{\sqrt{x_{0}^{2}+y_{0}^{2}}}{R}$. Here $D_R=\{P:|P|<R\}$, $C_R=\partial D_R$, $R>0$, and $A^*=R^2A/|A|^2$.
````

## 7. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|7824230a-489f-518c-90b8-6dd44c9aee12.local at=d3d55a19-d8a9-5aa3-a991-c3c51a850555] Poisson Equation on a Disk with Zero Dirichlet Boundary Data
> Let $f(r, \theta)$ be a smooth function on the disk $D_{R}$. The solution of
>
> $$
> \nabla^{2} u(r, \theta)=f(r, \theta), \quad 0 \leq r<R, 0 \leq \theta \leq 2 \pi,
> $$
>
> with boundary values $u=0$ on $C_{R}$, is
>
> $$
> u\left(r_{0}, \phi\right)=\frac{1}{4 \pi} \int_{0}^{2 \pi} \int_{0}^{R} f(r, \theta) \ln \left[R^{2} \frac{r^{2}+r_{0}^{2}-2 r r_{0} \cos (\theta-\phi)}{r^{2} r_{0}^{2}+R^{4}-2 r r_{0} R^{2} \cos (\theta-\phi)}\right] r d r d \theta
> $$
>
> where $0 \leq r_{0}<R$ and $0 \leq \phi \leq 2 \pi$. Here $D_R$ is the disk of radius $R>0$ centered at the origin and $C_R$ is its boundary.
````
### After

````text
> [!theorem|7824230a-489f-518c-90b8-6dd44c9aee12.local at=d3d55a19-d8a9-5aa3-a991-c3c51a850555] Solution of Poisson's Equation on the Disk
> Let $f(r, \theta)$ be a smooth function on the disk $D_{R}$. The solution of
>
> $$
> \nabla^{2} u(r, \theta)=f(r, \theta), \quad 0 \leq r<R, 0 \leq \theta \leq 2 \pi,
> $$
>
> with boundary values $u=0$ on $C_{R}$, is
>
> $$
> u\left(r_{0}, \phi\right)=\frac{1}{4 \pi} \int_{0}^{2 \pi} \int_{0}^{R} f(r, \theta) \ln \left[R^{2} \frac{r^{2}+r_{0}^{2}-2 r r_{0} \cos (\theta-\phi)}{r^{2} r_{0}^{2}+R^{4}-2 r r_{0} R^{2} \cos (\theta-\phi)}\right] r d r d \theta
> $$
>
> where $0 \leq r_{0}<R$ and $0 \leq \phi \leq 2 \pi$. Here $D_R$ is the disk of radius $R>0$ centered at the origin and $C_R$ is its boundary.
````

## 8. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|085c8b9c-2da6-5374-b4d0-8218f2dab441.local at=a48455fd-1410-59da-9551-f52b6081645b] Poisson Integral Formula for the Dirichlet Problem on a Disk
> Suppose that $u$ is harmonic in $D_{R}$ , continuous on $\overline{D_R}$, and $u(R, \theta)=f(\theta)$ on the boundary $C_{R}$. Then
>
> $$
> u(r, \phi)=\frac{R^{2}-r^{2}}{2 \pi} \int_{0}^{2 \pi} \frac{f(\theta)}{R^{2}+r^{2}-2 r R \cos (\theta-\phi)} d \theta
> $$
>
> where $0 \leq r<R$ and $0 \leq \phi \leq 2 \pi$. Here $D_R$ is the disk of radius $R>0$ centered at the origin and $C_R$ is its boundary.
````
### After

````text
> [!theorem|085c8b9c-2da6-5374-b4d0-8218f2dab441.local at=a48455fd-1410-59da-9551-f52b6081645b] Solution of Dirichlet's Problem on the Disk
> Suppose that $u$ is harmonic in $D_{R}$ , continuous on $\overline{D_R}$, and $u(R, \theta)=f(\theta)$ on the boundary $C_{R}$. Then
>
> $$
> u(r, \phi)=\frac{R^{2}-r^{2}}{2 \pi} \int_{0}^{2 \pi} \frac{f(\theta)}{R^{2}+r^{2}-2 r R \cos (\theta-\phi)} d \theta
> $$
>
> where $0 \leq r<R$ and $0 \leq \phi \leq 2 \pi$. Here $D_R$ is the disk of radius $R>0$ centered at the origin and $C_R$ is its boundary.
````

## 9. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|1be9f76d-35f8-5d7b-a140-6dc2ab962fd5.local at=9542d3ef-da00-5ce7-9529-328e4ee86e35] Green Potential for the Poisson Equation in the Upper Half-Plane
> Let $f(x, y)$ be a Hölder continuous function of compact support defined on the upper half-plane. The bounded solution of
>
> $$
> \nabla^{2} u(x,y)=f(x, y), \quad-\infty<x<\infty, 0<y .
> $$
>
> with boundary values $u=0$ on the $x$-axis $(y=0)$, is
>
> $$
> u\left(x_{0}, y_{0}\right)=\frac{1}{4 \pi} \int_{0}^{\infty} \int_{-\infty}^{\infty} f(x, y) \ln \frac{\left(x-x_{0}\right)^{2}+\left(y-y_{0}\right)^{2}}{\left(x-x_{0}\right)^{2}+\left(y+y_{0}\right)^{2}} d x d y
> $$
````
### After

````text
> [!theorem|1be9f76d-35f8-5d7b-a140-6dc2ab962fd5.local at=9542d3ef-da00-5ce7-9529-328e4ee86e35] Solution of Poisson's Equation on the Upper Half-Plane
> Let $f(x, y)$ be a Hölder continuous function of compact support defined on the upper half-plane. The bounded solution of
>
> $$
> \nabla^{2} u(x,y)=f(x, y), \quad-\infty<x<\infty, 0<y .
> $$
>
> with boundary values $u=0$ on the $x$-axis $(y=0)$, is
>
> $$
> u\left(x_{0}, y_{0}\right)=\frac{1}{4 \pi} \int_{0}^{\infty} \int_{-\infty}^{\infty} f(x, y) \ln \frac{\left(x-x_{0}\right)^{2}+\left(y-y_{0}\right)^{2}}{\left(x-x_{0}\right)^{2}+\left(y+y_{0}\right)^{2}} d x d y
> $$
````

## 10. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|80e9f0c0-0701-5904-a9df-a6cb291067a3.local at=394f2488-c1fc-59a1-9c13-a06dacf708fe] Poisson Integral Formula for Bounded Harmonic Functions in the Upper Half-Plane
> Suppose that $u$ is bounded and harmonic in the upper half-plane and extends continuously to $u(x,0)=f(x)$ on the boundary. Then
>
> $$
> u\left(x_{0}, y\right)=\frac{y}{\pi} \int_{-\infty}^{\infty} \frac{f(x)}{\left(x-x_{0}\right)^{2}+y^{2}} d x
> $$
>
> where $-\infty<x_{0}<\infty$ and $0<y$.
````
### After

````text
> [!theorem|80e9f0c0-0701-5904-a9df-a6cb291067a3.local at=394f2488-c1fc-59a1-9c13-a06dacf708fe] Solution of Dirichlet's Problem on the Upper Half-Plane
> Suppose that $u$ is bounded and harmonic in the upper half-plane and extends continuously to $u(x,0)=f(x)$ on the boundary. Then
>
> $$
> u\left(x_{0}, y\right)=\frac{y}{\pi} \int_{-\infty}^{\infty} \frac{f(x)}{\left(x-x_{0}\right)^{2}+y^{2}} d x
> $$
>
> where $-\infty<x_{0}<\infty$ and $0<y$.
````
