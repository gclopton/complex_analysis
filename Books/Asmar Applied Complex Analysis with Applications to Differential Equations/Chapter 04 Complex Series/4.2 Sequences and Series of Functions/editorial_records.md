
# Editorial records

Reading note: 4.2 Sequences and Series of Functions.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Callout 165: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!definition] Uniform Convergence of Complex-Valued Functions
> Let $E\subseteq\mathbb C$ and $f_n,f:E\to\mathbb C$.
>
> We say that $f_{n}$ converges uniformly to $f$ on $E$, and we write $\lim _{n \rightarrow \infty} f_{n}= f$ uniformly on $E$, if given $\epsilon>0$, we can find $N>0$ such that for all $n \geq N$ and all $z$ in $E$, we have $\left|f(z)-f_{n}(z)\right|<\epsilon$.
````
### After

````text
> [!definition] Uniform Convergence
> Let $E\subseteq\mathbb C$ and $f_n,f:E\to\mathbb C$.
>
> We say that $f_{n}$ converges uniformly to $f$ on $E$, and we write $\lim _{n \rightarrow \infty} f_{n}= f$ uniformly on $E$, if given $\epsilon>0$, we can find $N>0$ such that for all $n \geq N$ and all $z$ in $E$, we have $\left|f(z)-f_{n}(z)\right|<\epsilon$.
````

## 2. Callout 166: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Continuity of Uniform Limits and Uniformly Convergent Function Series
> Let $E\subseteq\mathbb C$ and let all functions below be complex-valued on $E$.
>
> (i) Suppose that $f_{n} \rightarrow f$ uniformly on $E$ and $f_{n}$ is continuous on $E$ for every $n$. Then $f$ is continuous on $E$.
> (ii) Suppose $u(z)=\sum_{n=1}^{\infty} u_{n}(z)$ converges uniformly on $E$ and $u_{n}$ is continuous on $E$ for every $n$. Then $u$ is continuous on $E$.
````
### After

````text
> [!theorem] Continuity and Uniform Convergence
> Let $E\subseteq\mathbb C$ and let all functions below be complex-valued on $E$.
>
> (i) Suppose that $f_{n} \rightarrow f$ uniformly on $E$ and $f_{n}$ is continuous on $E$ for every $n$. Then $f$ is continuous on $E$.
> (ii) Suppose $u(z)=\sum_{n=1}^{\infty} u_{n}(z)$ converges uniformly on $E$ and $u_{n}$ is continuous on $E$ for every $n$. Then $u$ is continuous on $E$.
````

## 3. Callout 167: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Interchanging Uniform Limits and Complex Path Integrals
> Let $\left\{f_{n}\right\}$ be a sequence of continuous functions on a region $\Omega$ and let $\gamma$ be a path in $\Omega$. If $f_{n} \rightarrow f$ uniformly on $\gamma$, then
>
> $$
> \lim _{n \rightarrow \infty} \int_{\gamma} f_{n}(z) d z=\int_{\gamma} f(z) d z
> $$
````
### After

````text
> [!theorem] Sequential Limits and Integrals
> Let $\left\{f_{n}\right\}$ be a sequence of continuous functions on a region $\Omega$ and let $\gamma$ be a path in $\Omega$. If $f_{n} \rightarrow f$ uniformly on $\gamma$, then
>
> $$
> \lim _{n \rightarrow \infty} \int_{\gamma} f_{n}(z) d z=\int_{\gamma} f(z) d z
> $$
````

## 4. Callout 168: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!corollary] Termwise Complex Path Integration of a Uniformly Convergent Series
> Suppose that $\left\{u_{n}\right\}$ is a sequence of continuous functions on a region $\Omega$ and let $\gamma$ be a path in $\Omega$. Suppose that $u(z)=\sum_{n=1}^{\infty} u_{n}(z)$ converges uniformly on $\gamma$. Then
>
> $$
> \int_{\gamma} u(z) d z=\sum_{n=1}^{\infty}\left(\int_{\gamma} u_{n}(z) d z\right)
> $$
````
### After

````text
> [!corollary] Term-by-Term Integration of Series
> Suppose that $\left\{u_{n}\right\}$ is a sequence of continuous functions on a region $\Omega$ and let $\gamma$ be a path in $\Omega$. Suppose that $u(z)=\sum_{n=1}^{\infty} u_{n}(z)$ converges uniformly on $\gamma$. Then
>
> $$
> \int_{\gamma} u(z) d z=\sum_{n=1}^{\infty}\left(\int_{\gamma} u_{n}(z) d z\right)
> $$
````

## 5. Callout 169: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Weierstrass M-Test for Complex Function Series
> Let $\left\{u_{n}\right\}$ be a sequence of functions on $E \subset \mathbb{C}$ and $\left\{M_{n}\right\}$ be a sequence of nonnegative numbers such that for all $n$
> (i) $\left|u_{n}(z)\right| \leq M_{n}$ for all $z$ in $E$; and
> (ii) $\sum_{n=1}^{\infty} M_{n}<\infty$.
>
> Then $\sum_{n=1}^{\infty} u_{n}(z)$ converges uniformly and absolutely on $E$.
````
### After

````text
> [!theorem] Weierstrass M-Test
> Let $\left\{u_{n}\right\}$ be a sequence of functions on $E \subset \mathbb{C}$ and $\left\{M_{n}\right\}$ be a sequence of nonnegative numbers such that for all $n$
> (i) $\left|u_{n}(z)\right| \leq M_{n}$ for all $z$ in $E$; and
> (ii) $\sum_{n=1}^{\infty} M_{n}<\infty$.
>
> Then $\sum_{n=1}^{\infty} u_{n}(z)$ converges uniformly and absolutely on $E$.
````

## 6. Callout 170: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Analyticity and Derivatives of Locally Uniform Limits
> Suppose that $\left\{f_{n}\right\}$ is a sequence of analytic functions on a region $\Omega$ such that $f_{n} \rightarrow f$ uniformly on every closed disk contained in $\Omega$. Then
> (i) $f$ is analytic on $\Omega$, and
> (ii) for any integer $k \geq 1, f_{n}^{(k)}(z) \rightarrow f^{(k)}(z)$ for all $z$ in $\Omega$. Thus, the limit of the $k$ th derivative is the $k$ th derivative of the limit.
````
### After

````text
> [!theorem] Sequential Limits and Derivatives
> Suppose that $\left\{f_{n}\right\}$ is a sequence of analytic functions on a region $\Omega$ such that $f_{n} \rightarrow f$ uniformly on every closed disk contained in $\Omega$. Then
> (i) $f$ is analytic on $\Omega$, and
> (ii) for any integer $k \geq 1, f_{n}^{(k)}(z) \rightarrow f^{(k)}(z)$ for all $z$ in $\Omega$. Thus, the limit of the $k$ th derivative is the $k$ th derivative of the limit.
````

## 7. Callout 172: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!corollary] Termwise Differentiation of Locally Uniformly Convergent Analytic Series
> Suppose that $\left\{u_{n}\right\}$ is a sequence of analytic functions on a region $\Omega$ and that $u(z)=\sum_{n=1}^{\infty} u_{n}(z)$ converges uniformly on every closed disk in $\Omega$. Then $u$ is analytic on $\Omega$; and for any integer $k \geq 1$, the series may be differentiated term by term $k$ times to yield
>
> $$
> u^{(k)}(z)=\sum_{n=1}^{\infty} u_{n}^{(k)}(z) \quad \text { for all } z \text { in } \Omega
> $$
````
### After

````text
> [!corollary] Term-by-Term Differentiation of Series
> Suppose that $\left\{u_{n}\right\}$ is a sequence of analytic functions on a region $\Omega$ and that $u(z)=\sum_{n=1}^{\infty} u_{n}(z)$ converges uniformly on every closed disk in $\Omega$. Then $u$ is analytic on $\Omega$; and for any integer $k \geq 1$, the series may be differentiated term by term $k$ times to yield
>
> $$
> u^{(k)}(z)=\sum_{n=1}^{\infty} u_{n}^{(k)}(z) \quad \text { for all } z \text { in } \Omega
> $$
````
