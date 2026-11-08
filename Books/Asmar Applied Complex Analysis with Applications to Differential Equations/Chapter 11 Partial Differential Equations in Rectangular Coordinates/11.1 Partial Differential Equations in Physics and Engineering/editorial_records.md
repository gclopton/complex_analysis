
# Editorial records

Reading note: 11.1 Partial Differential Equations in Physics and Engineering.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!definition] Laplacian in Euclidean coordinates
> For a twice continuously differentiable scalar function $u$ on an open subset of $\mathbb R^n$, its Laplacian is
> $$
> \Delta u=\nabla^2u=\sum_{j=1}^{n}\frac{\partial^2u}{\partial x_j^2}.
> $$
````
### After

````text
> [!definition] Laplacian in Euclidean coordinates
> The expression $\frac{\partial^{2} u}{\partial x^{2}}+\frac{\partial^{2} u}{\partial y^{2}}$ and its higher dimensional analogs are known as the Laplacian of $u$ and are denoted by $\Delta u$ or $\nabla^{2} u$.
````

## 2. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!definition] Order and linearity of a partial differential equation
> The order of a partial differential equation is the highest derivative order appearing in it. A PDE is linear if the unknown function and its partial derivatives occur only to the first degree, with at most one such factor in each term; their coefficients may depend on the independent variables but not on the unknown function. Otherwise the equation is nonlinear.
````
### After

````text
> [!definition] Order and linearity of a partial differential equation
> The order of the partial differential equation is the highest order of derivative that appears. The equation is called linear if the unknown function and the partial derivatives are of the first degree and at most one of these appears in any given term, otherwise, the equation is called nonlinear.
````

## 3. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem] Superposition principle for homogeneous linear partial differential equations
> If $u_1$ and $u_2$ solve the same homogeneous linear partial differential equation on a common domain, then $c_1u_1+c_2u_2$ also solves it for any constants $c_1,c_2$. If both solutions satisfy the same homogeneous linear boundary or initial condition, their linear combination satisfies that condition as well.
````
### After

````text
> [!theorem] Superposition Principle
> If $u_{1}$ and $u_{2}$ are solutions of a linear homogeneous partial differential equation, then any linear combination $u=c_{1} u_{1}+c_{2} u_{2}$, where $c_{1}$ and $c_{2}$ are constants, is also a solution. If in addition $u_{1}$ and $u_{2}$ satisfy a linear homogeneous boundary condition, then so will $u=c_{1} u_{1}+c_{2} u_{2}$.
````

## 4. Retain necessary local-solution qualification without the added derivation.

### Before

````text
This construction is local: writing $\xi=x(0)$, the characteristic map $x=\xi+tA(\phi(\xi))$ must be invertible. For differentiable data this holds locally where $1+tA'(\phi(\xi))\phi'(\xi)\ne0$, before characteristics intersect.
````
### After

````text
The construction applies locally before characteristics intersect.
````
