
# Editorial records

Reading note: 18.3 The Finite Difference Method for Laplace's Equation.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!equation|933cc6a7-5662-5579-a1a8-dd5c8a9c42d3.local at=b29b3ea2-f5b9-5f74-858b-2fe2edf8d504] Five-Point Finite-Difference Laplace Equation on a Uniform Square Grid
> Let $U_{ij}$ approximate a harmonic function $u$ on a square grid $(ih,jh)$ of spacing $h>0$. The centered finite-difference Laplace equation at an interior gridpoint is
>
> $$
> \frac{U_{i+1,j}+U_{i-1,j}+U_{i,j+1}+U_{i,j-1}-4U_{ij}}{h^2}=0,
> $$
>
> or equivalently
>
> $$
> U_{ij}=\frac14(U_{i+1,j}+U_{i-1,j}+U_{i,j+1}+U_{i,j-1}).
> $$
>
> Each interior value is the average of its four nearest grid neighbors. Boundary values must be supplied to determine the discrete Dirichlet solution.
````
### After

````text
> [!equation|933cc6a7-5662-5579-a1a8-dd5c8a9c42d3.local at=b29b3ea2-f5b9-5f74-858b-2fe2edf8d504] Discretization of Laplace's Equation
> For Laplace's equation on a square grid of spacing $h>0$, let $u_{ij}$ denote the discrete approximations, with prescribed boundary values. Then
> $$
> u_{ij}=\frac14\left(u_{i+1,j}+u_{i-1,j}+u_{i,j+1}+u_{i,j-1}\right).
> $$
````

## 2. Restore source wording; retain only the actual correction.

### Before

````text
The working below retains the source notation $u_{ij}$ for these discrete approximations (Figure 3). Henceforth the grid spacings are equal.
````
### After

````text
Henceforth the grid spacings are equal.
````

## 3. Restore source wording; retain only the actual correction.

### Before

````text
For numerical work, one can solve the sparse linear system without explicitly forming its dense inverse. The inverses above illustrate the algebra. If one does form the dense inverse,
````
### After

````text
Even if you use a computer to invert the matrix $A$,
````

## Additional source comparison

## 1. Move the remaining editorial notice into the separate record.

### Before

````text
[Source corrections: the Poisson table on printed page 539 has entries $-0.57$ and $-0.013$; symmetry and direct recomputation give $-0.057$ and $-0.043$, respectively. The zero boundary condition applies to all four sides.]
````
### After

````text

````
