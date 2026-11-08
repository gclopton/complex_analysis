
# Editorial records

Reading note: 18.1 The Finite Difference Method for the Heat Equation.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!equation|8be3d570-9f65-54d8-8ad4-5bd3d976df08.local at=cc1356ee-b017-5db7-8a9a-4b6f9d19b50a] Forward Difference Approximation of a First Time Derivative
> For a sufficiently smooth function $u(x,t)$ sampled on the uniform grid $(ih,jk)$, $k>0$, put $u_{ij}=u(ih,jk)$. Then
>
> $$
> u_t(ih,jk)\approx\frac{u_{i,j+1}-u_{ij}}{k}.
> $$
>
> The local derivative error is $O(k)$ if $u_{tt}$ is bounded near the sample.
````
### After

````text
> [!equation|8be3d570-9f65-54d8-8ad4-5bd3d976df08.local at=cc1356ee-b017-5db7-8a9a-4b6f9d19b50a] Discretization of First Derivative
> For a smooth function $u(x,t)$, let $u_{ij}=u(ih,jk)$ on a uniform grid with $h,k>0$. Then
>
> $$
> \begin{aligned}
> u_{t}(i h, j k) & \approx \frac{u(i h, j k+k)-u(i h, j k)}{k} \\
> & \approx \frac{1}{k}\left(u_{i, j+1}-u_{i j}\right)
> \end{aligned}
> $$
````

## 2. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!equation|8de3a8f9-9e94-5b61-91ca-4ae204cd2319.local at=3be280a4-58ca-5492-82c5-b9ac2e3cc78b] Centered Second Difference Approximation of a Spatial Second Derivative
> For a sufficiently smooth function $u(x,t)$ sampled on the uniform grid $(ih,jk)$, $h>0$, put $u_{ij}=u(ih,jk)$. Then
>
> $$
> u_{xx}(ih,jk)\approx\frac{u_{i+1,j}-2u_{ij}+u_{i-1,j}}{h^2}.
> $$
>
> The local derivative error is $O(h^2)$ if the fourth spatial derivative is bounded near the sample.
````
### After

````text
> [!equation|8de3a8f9-9e94-5b61-91ca-4ae204cd2319.local at=3be280a4-58ca-5492-82c5-b9ac2e3cc78b] Discretization of Second Derivative
> For a smooth function $u(x,t)$, let $u_{ij}=u(ih,jk)$ on a uniform grid with $h,k>0$. Then
>
> $$
> u_{x x}(i h, j k) \approx \frac{1}{h^{2}}\left(u_{i+1, j}-2 u_{i j}+u_{i-1, j}\right) .
> $$
````

## 3. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!equation|e650f2d0-28fd-5ccc-bcca-8fb1cddee1e1.local at=b41cfc86-b4d2-5447-8c65-fa44ba1fdd40] Explicit Forward-Time Centered-Space Scheme for the One-Dimensional Heat Equation
> For $u_t=c^2u_{xx}$, $c>0$, use spatial step $h>0$, time step $k>0$, and approximations $U_i^j\approx u(ih,jk)$. The explicit finite-difference update is
>
> $$
> U_i^{j+1}=(1-2s)U_i^j+s(U_{i+1}^j+U_{i-1}^j),\qquad s=\frac{c^2k}{h^2}.
> $$
>
> Supply initial samples and the prescribed boundary values at each step. The usual grid-independent stability restriction is $0<s\le\tfrac12$. For smooth solutions the differential-equation truncation error is $O(k+h^2)$.
````
### After

````text
> [!equation|e650f2d0-28fd-5ccc-bcca-8fb1cddee1e1.local at=b41cfc86-b4d2-5447-8c65-fa44ba1fdd40] Explicit Forward-Time Centered-Space Scheme for the One-Dimensional Heat Equation
> For the heat equation $u_t=c^2u_{xx}$, let $u_{ij}$ denote the approximation on the grid $(ih,jk)$, $h,k,c>0$. The update is
>
> $$
> u_{i, j+1}=(1-2 s) u_{i j}+s\left(u_{i+1, j}+u_{i-1,j}\right),
> $$
>
> where
>
> $$
> s=\frac{c^{2} k}{h^{2}}
> $$ Initial and boundary values are prescribed; stability requires $0<s\le1/2$.
````

## 4. Restore source wording; retain only the actual correction.

### Before

````text
Here $U$ distinguishes computed grid values from exact samples; the following working retains the source notation $u_{ij}$ for computed values.
````
### After

````text

````

## 5. Restore source wording; retain only the actual correction.

### Before

````text
The choice $s=1/2$ simplifies the formula. The usual stability restriction is $0<s\le1/2$; $s>1/2$ is unstable under mesh refinement. Stability controls error amplification, but accuracy still depends on the mesh, data regularity, and initialization. Reducing $s$ at fixed $h$ reduces the time step but does not universally guarantee a smaller total error.

[Source clarification: the printed discussion describes smaller positive $s$ as always more accurate. That conclusion is specific to the comparison below, not a general consequence of stability.]
````
### After

````text
It may appear that $s=1 / 2$ is the natural choice, since it simplifies the formula. Smaller positive values of $s$ can yield better approximations to the exact solution, as in the comparison below. In fact, it can be shown that the finite difference scheme (11) for the heat equation is unstable if $s>1 / 2$. The scheme is stable if $0<s \leq 1 / 2$, although accuracy also depends on the mesh and data.
````
