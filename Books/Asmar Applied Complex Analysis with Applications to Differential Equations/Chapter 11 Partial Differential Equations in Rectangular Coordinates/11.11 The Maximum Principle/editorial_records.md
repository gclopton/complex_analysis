
# Editorial records

Reading note: 11.11 The Maximum Principle.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|e3151e58-4abe-51b8-994f-5bf8715928e5.local at=3ed9a45d-0de1-5b88-855b-c847ceddd982] Maximum–minimum principle for the one-dimensional heat equation
> Let $L,c,T>0$ and let $u$ be continuous on $[0,L]\times[0,T]$, with $u_t,u_x,u_{xx}$ continuous where $0<x<L$ and $0<t\le T$. Suppose $u_t=c^2u_{xx}$ there. If constants $m,M$ bound the initial and endpoint data,
> $$
> m\le u(x,0)\le M,\qquad m\le u(0,t),u(L,t)\le M,
> $$
> for $0\le x\le L$ and $0\le t\le T$, then
> $$
> m\le u(x,t)\le M\qquad(0\le x\le L,\ 0\le t\le T).
> $$
> If the same hypotheses and bounds hold on every finite time interval, the conclusion holds for all $t\ge0$.
````
### After

````text
> [!theorem|e3151e58-4abe-51b8-994f-5bf8715928e5.local at=3ed9a45d-0de1-5b88-855b-c847ceddd982] The Maximum Principle for the Heat Equation
> Let $L,c>0$. Assume the solution is continuous on each closed finite-time rectangle and satisfies the heat equation classically in its spatial interior.
>
> Consider the heat boundary value problem with nonconstant boundary conditions
>
> $$
> \begin{gathered}
> u_{t}=c^{2} u_{x x}, \quad 0<x<L, \quad t>0 \\
> u(0, t)=g_{1}(t), \quad u(L, t)=g_{2}(t), \quad t \geq 0 \\
> u(x, 0)=f(x), \quad 0<x<L
> \end{gathered}
> $$
>
> Suppose that $f, g_{1}, g_{2}$ are bounded. Thus, there are constants $m$ and $M$ such that for all $0 \leq x \leq L$, and all $t \geq 0$, we have
> $\quad m \leq f(x) \leq M ; \quad m \leq g_{1}(t) \leq M ; \quad m \leq g_{2}(t) \leq M$.
>
> Then the solution of this boundary value problem satisfies the inequalities
>
> $$
> m \leq u(x, t) \leq M ; \quad 0 \leq x \leq L ; \quad t \geq 0
> $$
````

## 2. Remove added commentary; source notation is restored in the theorem.

### Before

````text
In the notation below the initial data are $f(x)=u(x,0)$ and the endpoint data are $g_1(t)=u(0,t)$, $g_2(t)=u(L,t)$. The bounded heat solutions with corner jumps used in the examples obey the same bounds by approximation; continuity at an incompatible initial corner is not claimed.
````
### After

````text

````

## 3. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|886b3dfe-9e5b-5024-a65a-175b637d5e91.local at=103584d6-0646-5778-bbb8-550810cc13e5] Maximum–minimum principle for harmonic functions on a rectangle
> Let $a,b>0$, $R=(0,a)\times(0,b)$, and let $u\in C^2(R)\cap C(\overline R)$ satisfy $u_{xx}+u_{yy}=0$ in $R$. If $m\le u\le M$ on the boundary $\partial R$, then $m\le u\le M$ throughout $\overline R$.
````
### After

````text
> [!theorem|886b3dfe-9e5b-5024-a65a-175b637d5e91.local at=103584d6-0646-5778-bbb8-550810cc13e5] The Maximum Principle for Laplace's Equation
> Let $a,b>0$, and let $u$ solve $u_{xx}+u_{yy}=0$ on $0<x<a$, $0<y<b$, continuously up to the boundary, with $u(x,0)=f_1(x)$, $u(x,b)=f_2(x)$, $u(0,y)=g_1(y)$, $u(a,y)=g_2(y)$.
>
> Suppose that $f_{1}, f_{2}, g_{1}, g_{2}$ are bounded. Thus, there are constants $m$ and $M$ such that for all $0 \leq x \leq a$, and all $0 \leq y \leq b$, we have
>
> $$
> m \leq f_{1}(x), f_{2}(x) \leq M ; \quad m \leq g_{1}(y), g_{2}(y) \leq M .
> $$
>
> Then the solution of this Dirichlet problem satisfies the inequalities
>
> $$
> m \leq u(x, y) \leq M ; \quad 0 \leq x \leq a ; \quad 0 \leq y \leq b .
> $$
````

## 4. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!lemma|6bb9824e-3ee6-5902-8dab-a1b393dc42ed.local at=e415ff92-81fa-5027-802b-2b56f8bd944e] Quadratic perturbation for the heat-equation maximum principle
> Let $L,c,T>0$ and $R_T=[0,L]\times[0,T]$. Let $u$ be continuous on $R_T$, solve $u_t=c^2u_{xx}$ classically for $0<x<L$, $0<t\le T$, and satisfy $u\le M$ on $x=0$, $x=L$ and $t=0$. For any positive integer $n$, set $v(x,t)=u(x,t)+x^2/n$. Then:
>
> (i) $v_t<c^2v_{xx}$ for $0<x<L$, $0<t\le T$.
>
> (ii) The maximum of $v$ on $R_T$ occurs on the initial or lateral boundary.
>
> (iii) $v(x,t)\le M+L^2/n$ everywhere on $R_T$.
````
### After

````text
> [!lemma|6bb9824e-3ee6-5902-8dab-a1b393dc42ed.local at=e415ff92-81fa-5027-802b-2b56f8bd944e] Quadratic perturbation for the heat-equation maximum principle
> Let $L,c,T>0$ and $R_T=[0,L]\times[0,T]$. Let $u$ be continuous on $R_T$, solve $u_t=c^2u_{xx}$ classically for $0<x<L$, $0<t\le T$, and satisfy $u\le M$ on $x=0$, $x=L$ and $t=0$. For any positive integer $n$, set $v(x,t)=u(x,t)+x^2/n$. 
>
> Then
> (i) $v_{t}(x, t)<c^{2} v_{x x}(x, t)$ for all $(x, t)$ inside $R_{T}$ and on its upper side.
> (ii) The maximum value of $v$ over the rectangle $R_{T}$ occurs somewhere on the three sides $x=0, x=L$, or $t=0$.
> (iii) For all $(x, t)$ in $R_{T}$, we have $v(x, t) \leq M+\frac{L^{2}}{n}$.
````
