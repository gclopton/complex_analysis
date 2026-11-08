
# Editorial records

Reading note: 11.10 Neumann and Robin Conditions.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!definition|a4e32151-7186-55cb-85c7-7222899d6f7b.local at=235d7f1f-5602-5e71-8a86-808ae828807c] Dirichlet, Neumann, and Robin boundary conditions
> For a scalar field $u$ and the outward unit normal $n$ to a boundary:
>
> A Dirichlet condition specifies $u=h$.
>
> A Neumann condition specifies $\partial u/\partial n=h$.
>
> A generalized Robin condition specifies $\alpha u+\beta\,\partial u/\partial n=h$, with prescribed coefficients $\alpha,\beta$ not both zero. It includes the Dirichlet case $\beta=0$ and the Neumann case $\alpha=0$. When $\beta\ne0$, it can be normalized to $\partial u/\partial n+(\alpha/\beta)u=h/\beta$.
>
> For a rectangle, the outward normal derivatives on the left, right, bottom, and top sides are respectively $-u_x$, $u_x$, $-u_y$, and $u_y$.
````
### After

````text
> [!definition|a4e32151-7186-55cb-85c7-7222899d6f7b.local at=235d7f1f-5602-5e71-8a86-808ae828807c] Dirichlet, Neumann, and Robin boundary conditions
> In a boundary value problem, we will call a Dirichlet condition any condition that specifies the values of the solution $u$ on the boundary, and a Neumann condition any condition that specifies the normal derivative $\frac{\partial u}{\partial n}$ on the boundary. A Robin condition is any condition that specifies $\beta\frac{\partial u}{\partial n}+\alpha u$ on the boundary, where $\alpha$ and $\beta$ are prescribed functions of $x$ and $y$, not both zero. Thus Dirichlet and Neumann conditions are special cases of Robin conditions. In a rectangular region, the normal derivative on the boundary is a derivative in the positive or negative direction of the $x$ - or $y$-axes. Thus a Robin condition is a condition that specifies the values of $\beta u_x+\alpha u$ or $\beta u_y+\alpha u$, with the normal orientation included in $\beta$, on the boundary of the rectangle.
````
