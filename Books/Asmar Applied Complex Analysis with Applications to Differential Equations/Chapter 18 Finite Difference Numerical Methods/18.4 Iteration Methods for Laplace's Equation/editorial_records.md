
# Editorial records

Reading note: 18.4 Iteration Methods for Laplace's Equation.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!algorithm|002ac32b-92bb-57fe-abc4-77f42e3fed38.local at=c7086cd6-d3bf-5a51-89ad-4b8565f4bce5] Jacobi Iteration for the Five-Point Discrete Dirichlet Problem
> On a finite rectangular square grid, hold all prescribed boundary values fixed and initialize the interior values $U_{ij}^{0}$. For each sweep $r=0,1,\ldots$, update every interior gridpoint using only the preceding sweep:
>
> $$
> U_{ij}^{r+1}=\frac14\left(U_{i+1,j}^{r}+U_{i-1,j}^{r}+U_{i,j+1}^{r}+U_{i,j-1}^{r}\right).
> $$
>
> Use a separate array for the new sweep. The iterates converge to the unique discrete Dirichlet solution. Monitor the residual $4U_{ij}-U_{i+1,j}-U_{i-1,j}-U_{i,j+1}-U_{i,j-1}$ against a chosen tolerance; a small change between sweeps alone is not an error bound for the continuous PDE.
````
### After

````text
> [!algorithm|002ac32b-92bb-57fe-abc4-77f42e3fed38.local at=c7086cd6-d3bf-5a51-89ad-4b8565f4bce5] Jacobi Iteration for the Five-Point Discrete Dirichlet Problem
> On a rectangular square grid with fixed Dirichlet boundary data, start with interior values $U_{ij}^0$.
>
> $$
> U_{i j}^{k+1}=\frac{1}{4}\left(U_{i+1, j}^{k}+U_{i-1, j}^{k}+U_{i, j+1}^{k}+U_{i, j-1}^{k}\right)
> $$
>
> for $k=0,1,2, \ldots$. We stop our iteration when we feel that the new set of values $U_{i j}^{k+1}$ agrees closely with the previous set $U_{i j}^{k}$.
````

## 2. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!algorithm|6ec9c20f-5bbe-5a87-86db-c80b32aa6f90.local at=11278057-f5f0-5f3e-bf1e-a0ed52b858dd] Gauss–Seidel Iteration for the Five-Point Discrete Dirichlet Problem
> On a finite rectangular square grid, hold prescribed boundary values fixed. Starting from an interior guess, sweep rows from bottom to top and within each row from left to right. At sweep $r+1$, set
>
> $$
> U_{ij}^{r+1}=\frac14\left(U_{i+1,j}^{r}+U_{i-1,j}^{r+1}+U_{i,j+1}^{r}+U_{i,j-1}^{r+1}\right).
> $$
>
> Thus the left and lower neighbors use their newly updated values, and the right and upper neighbors use their preceding-sweep values. These iterates converge to the discrete Dirichlet solution. Check the discrete residual against the chosen stopping tolerance.
````
### After

````text
> [!algorithm|6ec9c20f-5bbe-5a87-86db-c80b32aa6f90.local at=11278057-f5f0-5f3e-bf1e-a0ed52b858dd] Gauss–Seidel Iteration for the Five-Point Discrete Dirichlet Problem
> On a rectangular square grid with fixed Dirichlet boundary data, start with interior values $U_{ij}^0$. Sweep rows bottom to top and entries left to right.
>
> $$
> U_{i j}^{k+1}=\frac{1}{4}\left(U_{i+1, j}^{k}+U_{i-1, j}^{k+1}+U_{i, j+1}^{k}+U_{i,j-1}^{k+1}\right) .
> $$
>
> Here the only difference from Jacobi iteration is the appearance of $k+1$ as a superscript on the two terms on the right corresponding to the points below or to the left of the central point.
````

## 3. Restore source wording; retain only the actual correction.

### Before

````text
This is the Gauss–Seidel method, also called Liebmann’s method in this setting. Its asymptotic convergence is faster here than Jacobi’s, although a particular initial error and finite stopping tolerance can affect iteration counts.
````
### After

````text
This is known as the Gauss-Seidel method (also as Liebmann's method). It is an improvement of the Jacobi method that in general will yield faster convergence to the finite difference method solution.
````

## 4. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!algorithm|e9513713-9e35-5148-9699-d188ed5ec318.local at=f99704ca-8ed0-58fc-9dfc-69cfd82438bc] Successive Overrelaxation for the Five-Point Discrete Dirichlet Problem
> On a finite rectangular square grid with fixed Dirichlet boundary data, choose $0<\omega<2$ and an initial guess for the interior values. Sweep rows bottom to top and entries left to right, updating by
>
> $$
> U_{ij}^{r+1}=(1-\omega)U_{ij}^{r}+\frac\omega4\left(U_{i+1,j}^{r}+U_{i-1,j}^{r+1}+U_{i,j+1}^{r}+U_{i,j-1}^{r+1}\right).
> $$
>
> This iteration converges to the discrete Dirichlet solution. The case $\omega=1$ is Gauss–Seidel; $1<\omega<2$ is overrelaxation and $0<\omega<1$ is underrelaxation. Equivalently, write $s=\omega/4$, so $0<s<1/2$. Select the parameter and stopping tolerance with reference to the residual and convergence behavior.
````
### After

````text
> [!algorithm|e9513713-9e35-5148-9699-d188ed5ec318.local at=f99704ca-8ed0-58fc-9dfc-69cfd82438bc] Successive Overrelaxation for the Five-Point Discrete Dirichlet Problem
> On a rectangular square grid with fixed Dirichlet boundary data, start with interior values $U_{ij}^0$. Sweep rows bottom to top and entries left to right.
>
> $$
> U_{i j}^{k+1}=U_{i j}^{k}+s\left(U_{i+1, j}^{k}+U_{i-1, j}^{k+1}+U_{i, j+1}^{k}+U_{i, j-1}^{k+1}-4 U_{i j}^{k}\right)
> $$ Here $0<s<1/2$; $s=1/4$ gives the Gauss-Seidel method.
````

## 5. Restore source wording; retain only the actual correction.

### Before

````text
The source writes the parameter as $s=\Delta_t c^2/h^2$ and motivates the update by heat relaxation, then uses newly computed neighbors as in Gauss–Seidel. That change produces a stationary linear-system iteration; it should not be confused with the ordinary explicit two-dimensional heat scheme, whose stability limit is $\Delta_t c^2/h^2\le1/4$.

[Source correction: printed page 544 includes the endpoint $s=1/2$ in its stability discussion. Convergence of this SOR iteration requires the strict bound $0<s<1/2$ (equivalently $0<\omega<2$); the endpoint does not in general converge. A parameter in this range is not automatically faster than Jacobi or Gauss–Seidel.]
````
### After

````text
where we have set $s=\Delta_{t} c^{2} / h^{2}$. Note that the update, which has a very specific interpretation in terms of heat values at a discrete set of times, can be reinterpreted rather as an iterative scheme. Each new time step represents a new set of data calculated from previous data, and the process is not fundamentally different from our earlier iteration procedures. Indeed, this method is just a generalization of the Gauss-Seidel method; and taking $s=1 / 4$ will reduce the update to the Gauss-Seidel update.

Since the values generated by the update correspond to the finite difference approximations to the heat equation, we expect that as $t \rightarrow \infty$ (that is, as $k \rightarrow \infty$ ) these values should approach the steady-state solution for the corresponding heat equation. Thus, so long as these schemes are stable, the heat equation leads us quite naturally to an iterative procedure for solving the Dirichlet problem. It turns out that a stability analysis of the update gives the range $0<s<1/2$. The scheme given by the update is known as the method of successive overrelaxation. With a value of $s$ in the range $0<s<1 / 2$, in most cases it can be the best of the iterative schemes developed in this section.
````
