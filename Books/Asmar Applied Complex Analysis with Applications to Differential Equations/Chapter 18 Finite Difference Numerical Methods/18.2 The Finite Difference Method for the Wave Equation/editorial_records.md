
# Editorial records

Reading note: 18.2 The Finite Difference Method for the Wave Equation.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!equation] Centered Finite-Difference Scheme for the One-Dimensional Wave Equation
> For $u_{tt}=c^2u_{xx}$ with $c>0$, spatial step $h>0$, and time step $k>0$, let $U_i^j\approx u(ih,jk)$ and $s=(ck/h)^2$. The centered update is
>
> $$
> U_i^{j+1}=2(1-s)U_i^j+s(U_{i+1}^j+U_{i-1}^j)-U_i^{j-1}.
> $$
>
> For initial displacement $f$ and velocity $g$, initialize the interior grid by
>
> $$
> U_i^0=f(ih),\qquad U_i^1=f(ih)+kg(ih)+\frac s2\bigl(f((i+1)h)-2f(ih)+f((i-1)h)\bigr).
> $$
>
> Enforce the prescribed boundary data at every time level. The usual mesh-independent CFL condition is $0<ck/h\le1$; for smooth solutions and compatible initial/boundary data this centered scheme is second-order accurate in space and time.
````
### After

````text
> [!equation] Discretization of the Wave Equation
> For $u_{tt}=c^2u_{xx}$, let $u_{ij}$ be the approximation on the grid $(ih,jk)$, $h,k,c>0$. The update is
>
> $$
> u_{i, j+1}=2(1-s) u_{i j}+s\left(u_{i+1, j}+u_{i-1, j}\right)-u_{i, j-1},
> $$
>
> where
>
> $$
> s=c^{2} \frac{k^{2}}{h^{2}}
> $$ Supply initial displacement and velocity and boundary values, with $0<ck/h\le1$.
````

## 2. Restore source wording; retain only the actual correction.

### Before

````text
The source working below writes the computed grid values as $u_{ij}$ and uses $s=(ck/h)^2$.
````
### After

````text

````
