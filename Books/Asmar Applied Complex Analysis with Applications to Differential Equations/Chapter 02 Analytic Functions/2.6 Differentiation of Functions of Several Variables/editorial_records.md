
# Editorial records

Reading note: 2.6 Differentiation of Functions of Several Variables.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Callout 70: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!definition] Total Differentiability of a Real Function of Two Variables
> We call a real-valued function $u(x, y)$ differentiable at $z_{0}=\left(x_{0}, y_{0}\right)$ if it can be written in the form
>
> $$
> u(z)=u\left(z_{0}\right)+A\left(x-x_{0}\right)+B\left(y-y_{0}\right)+\epsilon(z)\left|z-z_{0}\right|
> $$
>
> where $A$ and $B$ are (real) constants and $\epsilon(z) \rightarrow 0$ as $z \rightarrow z_{0}$.
````
### After

````text
> [!definition] Differentiability of Real-Valued Functions of Two Variables
> We call a real-valued function $u(x, y)$ differentiable at $z_{0}=\left(x_{0}, y_{0}\right)$ if it can be written in the form
>
> $$
> u(z)=u\left(z_{0}\right)+A\left(x-x_{0}\right)+B\left(y-y_{0}\right)+\epsilon(z)\left|z-z_{0}\right|
> $$
>
> where $A$ and $B$ are (real) constants and $\epsilon(z) \rightarrow 0$ as $z \rightarrow z_{0}$.
````

## 2. Callout 72: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Differentiability from Partial Derivatives and One Continuous Partial
> Let $u$ be a real-valued function defined on a neighborhood of $z_{0}$. If
> (i) $u_{x}\left(z_{0}\right)$ and $u_{y}\left(z_{0}\right)$ exist, and
> (ii) at least one of $u_x$ and $u_y$ exists in a neighborhood of $z_0$ and is continuous at $z_0$,
> then $u$ is differentiable at $z_{0}$, its differential is $du=u_x(x_0,y_0)\,dx+u_y(x_0,y_0)\,dy$.
````
### After

````text
> [!theorem] Sufficient Conditions for Differentiability
> Let $u$ be a real-valued function defined on a neighborhood of $z_{0}$. If
> (i) $u_{x}\left(z_{0}\right)$ and $u_{y}\left(z_{0}\right)$ exist, and
> (ii) either $u_{x}(z)$ or $u_{y}(z)$ is continuous at $z_{0}$,
> then $u$ is differentiable at $z_{0}$, and $u(z)=u(z_0)+A(x-x_0)+B(y-y_0)+o(|z-z_0|)$ with $A=u_{x}\left(x_{0}, y_{0}\right), B= u_{y}\left(x_{0}, y_{0}\right)$.
````

## 3. Callout 73: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Continuous Cauchy–Riemann Partials Imply Analyticity
> Let $f(z)=u(x, y)+i v(x, y)$ be a complex-valued function, defined in an open set $S$. If $u_{x}, u_{y}, v_{x}$, and $v_{y}$ are continuous and satisfy the Cauchy–Riemann equations in $S$, then $f(z)$ is analytic on $S$.
````
### After

````text
> [!theorem] The Chain Rule
> Let $f(z)=u(x, y)+i v(x, y)$ be a complex-valued function, defined in an open set $S$. If $u_{x}, u_{y}, v_{x}$, and $v_{y}$ are continuous and satisfy the Cauchy–Riemann equations in $S$, then $f(z)$ is analytic on $S$.
````

## 4. Callout 74: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Chain Rule along a Differentiable Plane Curve
> Assume the curve $(x(t),y(t))$ lies in $S$.
>
> Suppose that $u(x, y)$ is a differentiable function of $(x, y)$ in an open set $S$, where $x=x(t)$ and $y=y(t)$ are both differentiable functions of $t$. Then the function $U(t)=u(x(t), y(t))$ is a differentiable function of $t$ and
>
> $$
> \frac{d U}{d t}=\frac{\partial u}{\partial x} \frac{d x}{d t}+\frac{\partial u}{\partial y} \frac{d y}{d t}
> $$
````
### After

````text
> [!theorem] The Chain Rule
> Assume the curve $(x(t),y(t))$ lies in $S$.
>
> Suppose that $u(x, y)$ is a differentiable function of $(x, y)$ in an open set $S$, where $x=x(t)$ and $y=y(t)$ are both differentiable functions of $t$. Then the function $U(t)=u(x(t), y(t))$ is a differentiable function of $t$ and
>
> $$
> \frac{d U}{d t}=\frac{\partial u}{\partial x} \frac{d x}{d t}+\frac{\partial u}{\partial y} \frac{d y}{d t}
> $$
````

## 5. Callout 75: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Mean Value Theorem along a Line Segment in the Plane
> Suppose $u(x, y)$ is a differentiable real-valued function of ( $x, y$ ) in an open set $S$. Suppose that the line segment $\left[z_1, z_2\right]$ joining $z_1=\left(x_1, y_1\right)$ to $z_2=\left(x_2, y_2\right)$ lies entirely in $S$. Then there exists a point $\zeta$ on $\left[z_1, z_2\right]$ such that
>
> $$
> u\left(z_2\right)-u\left(z_1\right)=u_x(\zeta)\left(x_2-x_1\right)+u_y(\zeta)\left(y_2-y_1\right)
> $$
````
### After

````text
> [!theorem] The Mean Value Theorem in Two Dimensions
> Suppose $u(x, y)$ is a differentiable real-valued function of ( $x, y$ ) in an open set $S$. Suppose that the line segment $\left[z_1, z_2\right]$ joining $z_1=\left(x_1, y_1\right)$ to $z_2=\left(x_2, y_2\right)$ lies entirely in $S$. Then there exists a point $\zeta$ on $\left[z_1, z_2\right]$ such that
>
> $$
> u\left(z_2\right)-u\left(z_1\right)=u_x(\zeta)\left(x_2-x_1\right)+u_y(\zeta)\left(y_2-y_1\right)
> $$
````
