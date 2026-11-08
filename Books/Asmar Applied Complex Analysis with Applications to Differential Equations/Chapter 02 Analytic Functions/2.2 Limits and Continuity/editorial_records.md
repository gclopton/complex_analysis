
# Editorial records

Reading note: 2.2 Limits and Continuity.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Callout 44: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!definition] Limit of a Complex-Valued Function
> We say that a complex-valued function $f(z)$ has a limit $L$ as $z$ approaches $z_{0}$, and we write
>
> $$
> \lim _{z \rightarrow z_{0}} f(z)=L \quad \text { or } \quad f(z) \rightarrow L \text { as } z \rightarrow z_{0},
> $$
>
> if given any $\epsilon>0$, there exists a $\delta>0$ such that
>
> $$
> |f(z)-L|<\epsilon \quad \text { whenever } 0<\left|z-z_{0}\right|<\delta .
> $$
````
### After

````text
> [!definition] limit of a complex-valued function
> We say that a complex-valued function $f(z)$ has a limit $L$ as $z$ approaches $z_{0}$, and we write
>
> $$
> \lim _{z \rightarrow z_{0}} f(z)=L \quad \text { or } \quad f(z) \rightarrow L \text { as } z \rightarrow z_{0},
> $$
>
> if given any $\epsilon>0$, there exists a $\delta>0$ such that
>
> $$
> |f(z)-L|<\epsilon \quad \text { whenever } 0<\left|z-z_{0}\right|<\delta .
> $$
````

## 2. Callout 45: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Algebra and Composition Laws for Complex Limits
> Suppose $\lim _{z \rightarrow z_{0}} f(z)$ and $\lim _{z \rightarrow z_{0}} g(z)$ both exist and $c_{1}, c_{2}$ are complex constants. Then
>
> $$
> \lim _{z \rightarrow z_{0}}\left[c_{1} f(z)+c_{2} g(z)\right]=c_{1} \lim _{z \rightarrow z_{0}} f(z)+c_{2} \lim _{z \rightarrow z_{0}} g(z), 
> $$
>
> $$
> \lim _{z \rightarrow z_{0}}[f(z) g(z)]=\lim _{z \rightarrow z_{0}} f(z)\,\lim _{z \rightarrow z_{0}} g(z), 
> $$
>
> $\lim _{z \rightarrow z_{0}}\left[\frac{f(z)}{g(z)}\right]=\frac{\lim _{z \rightarrow z_{0}} f(z)}{\lim _{z \rightarrow z_{0}} g(z)}$, provided $\lim _{z \rightarrow z_{0}} g(z) \neq 0$.
>
> If $g(z)\to w_0$ as $z\to z_0$ and $f$ is continuous at $w_0$, then, writing $A=f(w_0)$,
>
> $$
> \lim _{z \rightarrow z_{0}} f(g(z))=A=f\left(\lim _{z \rightarrow z_{0}} g(z)\right) 
> $$
````
### After

````text
> [!theorem] Operations with Limits
> Suppose $\lim _{z \rightarrow z_{0}} f(z)$ and $\lim _{z \rightarrow z_{0}} g(z)$ both exist and $c_{1}, c_{2}$ are complex constants. Then
>
> $$
> \lim _{z \rightarrow z_{0}}\left[c_{1} f(z)+c_{2} g(z)\right]=c_{1} \lim _{z \rightarrow z_{0}} f(z)+c_{2} \lim _{z \rightarrow z_{0}} g(z), 
> $$
>
> $$
> \lim _{z \rightarrow z_{0}}[f(z) g(z)]=\lim _{z \rightarrow z_{0}} f(z)\,\lim _{z \rightarrow z_{0}} g(z), 
> $$
>
> $\lim _{z \rightarrow z_{0}}\left[\frac{f(z)}{g(z)}\right]=\frac{\lim _{z \rightarrow z_{0}} f(z)}{\lim _{z \rightarrow z_{0}} g(z)}$, provided $\lim _{z \rightarrow z_{0}} g(z) \neq 0$.
>
> If $g(z)\to w_0$ as $z\to z_0$ and $f$ is continuous at $w_0$, then, writing $A=f(w_0)$,
>
> $$
> \lim _{z \rightarrow z_{0}} f(g(z))=A=f\left(\lim _{z \rightarrow z_{0}} g(z)\right) 
> $$
````

## 3. Callout 46: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Squeeze and Bounded-Factor Theorems for Complex Limits
> (i) Suppose that $f(z) \rightarrow 0$ as $z \rightarrow z_0$ and $|g(z)| \leq|f(z)|$ in a deleted neighborhood of $z_0$. Then $g(z) \rightarrow 0$ as $z \rightarrow z_0$.
> (ii) Suppose that $f(z) \rightarrow 0$ as $z \rightarrow z_0$ and $g(z)$ is bounded in a deleted neighborhood of $z_0$. Then $f(z) g(z) \rightarrow 0$ as $z \rightarrow z_0$.
````
### After

````text
> [!theorem] The Squeeze Theorem
> (i) Suppose that $f(z) \rightarrow 0$ as $z \rightarrow z_0$ and $|g(z)| \leq|f(z)|$ in a deleted neighborhood of $z_0$. Then $g(z) \rightarrow 0$ as $z \rightarrow z_0$.
> (ii) Suppose that $f(z) \rightarrow 0$ as $z \rightarrow z_0$ and $g(z)$ is bounded in a deleted neighborhood of $z_0$. Then $f(z) g(z) \rightarrow 0$ as $z \rightarrow z_0$.
````

## 4. Callout 47: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Complex Limits via Real and Imaginary Parts
> Given a complex-valued function $f(z)=u(x, y)+i v(x, y)$ and a complex number $L=a+i b$, then
> $\lim _{z \rightarrow z_{0}} f(z)=L \Longleftrightarrow \lim _{z \rightarrow z_{0}} u(x, y)=a$ and $\lim _{z \rightarrow z_{0}} v(x, y)=b$.
````
### After

````text
> [!theorem] REAL AND IMAGINARY PARTS OF LIMITS
> Given a complex-valued function $f(z)=u(x, y)+i v(x, y)$ and a complex number $L=a+i b$, then
> $\lim _{z \rightarrow z_{0}} f(z)=L \Longleftrightarrow \lim _{z \rightarrow z_{0}} u(x, y)=a$ and $\lim _{z \rightarrow z_{0}} v(x, y)=b$.
````

## 5. Callout 48: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!definition] Infinite Limits and Limits at Infinity for Complex Functions
> (i) We write $\lim _{z \rightarrow z_{0}} f(z)=\infty$ to mean that for any $M>0$ there is a $\delta>0$ such that $0<\left|z-z_{0}\right|<\delta \Rightarrow|f(z)|>M$.
> (ii) We write $\lim _{z \rightarrow \infty} f(z)=L$ to mean that for any $\epsilon>0$ there is an $R>0$ such that $|z|>R \Rightarrow|f(z)-L|<\epsilon$.
> (iii) We write $\lim _{z \rightarrow \infty} f(z)=\infty$ to mean that for any $M>0$ there is an $R>0$ such that $|z|>R \Rightarrow|f(z)|>M$.
````
### After

````text
> [!definition] Limits Involving Infinity
> (i) We write $\lim _{z \rightarrow z_{0}} f(z)=\infty$ to mean that for any $M>0$ there is a $\delta>0$ such that $0<\left|z-z_{0}\right|<\delta \Rightarrow|f(z)|>M$.
> (ii) We write $\lim _{z \rightarrow \infty} f(z)=L$ to mean that for any $\epsilon>0$ there is an $R>0$ such that $|z|>R \Rightarrow|f(z)-L|<\epsilon$.
> (iii) We write $\lim _{z \rightarrow \infty} f(z)=\infty$ to mean that for any $M>0$ there is an $R>0$ such that $|z|>R \Rightarrow|f(z)|>M$.
````

## 6. Callout 49: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!definition] Continuity of a Complex-Valued Function
> Suppose $f(z)$ is defined on a neighborhood of $z_{0}$. We say that $f(z)$ is continuous at the point $z_{0}$ if $\lim _{z \rightarrow z_{0}} f(z)$ exists and equals $f\left(z_{0}\right)$. We say $f$ is continuous on a set $S$ if it is continuous at every point in $S$.
````
### After

````text
> [!definition] Continuous Function
> Suppose $f(z)$ is defined on a neighborhood of $z_{0}$. We say that $f(z)$ is continuous at the point $z_{0}$ if $\lim _{z \rightarrow z_{0}} f(z)$ exists and equals $f\left(z_{0}\right)$. We say $f$ is continuous on a set $S$ if it is continuous at every point in $S$.
````

## 7. Callout 50: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Algebra and Composition Laws for Continuous Complex Functions
> (i) If $f(z)$ and $g(z)$ are continuous at $z_{0}$, and $c_{1}, c_{2}$ are complex constants, then the following functions are continuous at $z_{0}$ :
>
> $$
> c_{1} f(z)+c_{2} g(z), \quad f(z) g(z), \quad \frac{f(z)}{g(z)}\left(\text { provided } g\left(z_{0}\right) \neq 0\right)
> $$
>
> (ii) If $g$ is continuous at $z_{0}$ and $f$ is continuous at $g\left(z_{0}\right)$, then the composition $h(z)=f(g(z))$ is continuous at $z_{0}$.
> (iii) If $g(z)$ is real-valued and continuous at $z_{0}$ and $f(x)$ is continuous at $x_{0}=g\left(z_{0}\right)$, then the composition $h(z)=f(g(z))$ is continuous at $z_{0}$.
> (iv) The function $f(z)=u(z)+i v(z)$ is continuous if and only if $u$ and $v$ are continuous.
````
### After

````text
> [!theorem] Properties of Continuous Functions
> (i) If $f(z)$ and $g(z)$ are continuous at $z_{0}$, and $c_{1}, c_{2}$ are complex constants, then the following functions are continuous at $z_{0}$ :
>
> $$
> c_{1} f(z)+c_{2} g(z), \quad f(z) g(z), \quad \frac{f(z)}{g(z)}\left(\text { provided } g\left(z_{0}\right) \neq 0\right)
> $$
>
> (ii) If $g$ is continuous at $z_{0}$ and $f$ is continuous at $g\left(z_{0}\right)$, then the composition $h(z)=f(g(z))$ is continuous at $z_{0}$.
> (iii) If $g(z)$ is real-valued and continuous at $z_{0}$ and $f(x)$ is continuous at $x_{0}=g\left(z_{0}\right)$, then the composition $h(z)=f(g(z))$ is continuous at $z_{0}$.
> (iv) The function $f(z)=u(z)+i v(z)$ is continuous if and only if $u$ and $v$ are continuous.
````

## 8. Callout 52: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Continuity and Branch Cut of the Principal Complex Logarithm
> The principal branch of the logarithm
>
> $$
> \log (z)=\ln |z|+i \operatorname{Arg}(z), \quad-\pi<\operatorname{Arg} z \leq \pi \quad(z \neq 0),
> $$
>
> is continuous for all $z$ in $\mathbb{C} \backslash(-\infty, 0]$. The jump across the negative real axis cannot be removed by redefining values there, and the singularity at $z=0$ is not removable.
````
### After

````text
> [!theorem] CONTINUITY OF THE LOGARITHM
> The principal branch of the logarithm
>
> $$
> \log (z)=\ln |z|+i \operatorname{Arg}(z), \quad-\pi<\operatorname{Arg} z \leq \pi \quad(z \neq 0),
> $$
>
> is continuous for all $z$ in $\mathbb{C} \backslash(-\infty, 0]$. For $z$ in $(-\infty, 0)$, the discontinuities of $\log z$ are not removable.
````

## 9. Move editorial commentary out of the reading note.

### Before

````text
*Editorial note: Restored the punctured-neighborhood condition for a limit at a finite point.*
````
### After

````text

````

## 10. Move editorial commentary out of the reading note.

### Before

````text
*Editorial note: Corrected the OCR comma between factors. Made continuity of the outer function explicit for the displayed composition formula with $f(w_0)$; a deleted limit alone does not justify that equality.*
````
### After

````text

````
