
# Editorial records

Reading note: 4.1 Sequences and Series of Complex Numbers.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Callout 145: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!definition] Limit of a Complex Sequence
> We say that a sequence $\left\{a_{n}\right\}$ converges to a complex number $L$ or has limit $L$ as $n$ tends to infinity and write
>
> $$
> \lim _{n \rightarrow \infty} a_{n}=L
> $$
>
> if given any $\epsilon>0$ there is an integer $N$ such that
>
> $$
> \left|a_{n}-L\right|<\epsilon \quad \text { for all } n \geq N .
> $$
>
> If the sequence $\left\{a_{n}\right\}$ does not converge, then we say that it diverges.
````
### After

````text
> [!definition] Limit of a Sequence
> We say that a sequence $\left\{a_{n}\right\}$ converges to a complex number $L$ or has limit $L$ as $n$ tends to infinity and write
>
> $$
> \lim _{n \rightarrow \infty} a_{n}=L
> $$
>
> if given any $\epsilon>0$ there is an integer $N$ such that
>
> $$
> \left|a_{n}-L\right|<\epsilon \quad \text { for all } n \geq N .
> $$
>
> If the sequence $\left\{a_{n}\right\}$ does not converge, then we say that it diverges.
````

## 2. Callout 146: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Algebraic Limit Laws for Complex Sequences
> If $\left\{a_{n}\right\}$ and $\left\{b_{n}\right\}$ are convergent sequences of complex numbers and $\alpha$ and $\beta$ are complex numbers, then
>
> $$
> \begin{aligned}
> & \lim _{n \rightarrow \infty}\left(\alpha a_{n}+\beta b_{n}\right)=\alpha \lim _{n \rightarrow \infty} a_{n}+\beta \lim _{n \rightarrow \infty} b_{n} ; \\
> & \lim _{n \rightarrow \infty}\left(a_{n} b_{n}\right)=\lim _{n \rightarrow \infty} a_{n} \lim _{n \rightarrow \infty} b_{n} ; \\
> & \lim _{n \rightarrow \infty} \frac{a_{n}}{b_{n}}=\frac{\lim _{n \rightarrow \infty} a_{n}}{\lim _{n \rightarrow \infty} b_{n}} \text { if } \lim _{n \rightarrow \infty} b_{n} \neq 0 .
> \end{aligned}
> $$
````
### After

````text
> [!theorem] Limit Laws for Sequences
> If $\left\{a_{n}\right\}$ and $\left\{b_{n}\right\}$ are convergent sequences of complex numbers and $\alpha$ and $\beta$ are complex numbers, then
>
> $$
> \begin{aligned}
> & \lim _{n \rightarrow \infty}\left(\alpha a_{n}+\beta b_{n}\right)=\alpha \lim _{n \rightarrow \infty} a_{n}+\beta \lim _{n \rightarrow \infty} b_{n} ; \\
> & \lim _{n \rightarrow \infty}\left(a_{n} b_{n}\right)=\lim _{n \rightarrow \infty} a_{n} \lim _{n \rightarrow \infty} b_{n} ; \\
> & \lim _{n \rightarrow \infty} \frac{a_{n}}{b_{n}}=\frac{\lim _{n \rightarrow \infty} a_{n}}{\lim _{n \rightarrow \infty} b_{n}} \text { if } \lim _{n \rightarrow \infty} b_{n} \neq 0 .
> \end{aligned}
> $$
````

## 3. Callout 147: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Continuous Functions Preserve Limits of Complex Sequences
> Let $(a_n)$ be a complex sequence in the domain of $f$.
>
> If $\lim _{n \rightarrow \infty} a_{n}=L$ and $f$ is continuous at $L$, then
>
> $$
> \lim _{n \rightarrow \infty} f\left(a_{n}\right)=f(L)
> $$
````
### After

````text
> [!theorem] Substitution Law
> Let $(a_n)$ be a complex sequence in the domain of $f$.
>
> If $\lim _{n \rightarrow \infty} a_{n}=L$ and $f$ is continuous at $L$, then
>
> $$
> \lim _{n \rightarrow \infty} f\left(a_{n}\right)=f(L)
> $$
````

## 4. Callout 149: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Boundedness of Convergent Complex Sequences
> A convergent complex sequence is bounded. That is, if $\left\{a_{n}\right\}$ is a convergent complex sequence, then there is a positive real number $M>0$ such that $\left|a_{n}\right| \leq M$ for all $n$.
````
### After

````text
> [!theorem] Boundedness
> A convergent complex sequence is bounded. That is, if $\left\{a_{n}\right\}$ is a convergent complex sequence, then there is a positive real number $M>0$ such that $\left|a_{n}\right| \leq M$ for all $n$.
````

## 5. Callout 150: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Squeeze and Bounded-Factor Limits for Complex Sequences
> Let $(a_n)$ and $(b_n)$ be complex sequences.
>
> (i) Suppose that $\lim _{n \rightarrow \infty} a_{n}=0$ and $\left|b_{n}\right| \leq\left|a_{n}\right|$ for all $n \geq n_{0}$. Then $\lim _{n \rightarrow \infty} b_{n}=0$.
> (ii) Suppose that $\lim _{n \rightarrow \infty} a_{n}=0$ and $\left\{b_{n}\right\}$ is a bounded sequence, then $\lim _{n \rightarrow \infty} a_{n} b_{n}=0$.
````
### After

````text
> [!theorem] Squeeze Theorem
> Let $(a_n)$ and $(b_n)$ be complex sequences.
>
> (i) Suppose that $\lim _{n \rightarrow \infty} a_{n}=0$ and $\left|b_{n}\right| \leq\left|a_{n}\right|$ for all $n \geq n_{0}$. Then $\lim _{n \rightarrow \infty} b_{n}=0$.
> (ii) Suppose that $\lim _{n \rightarrow \infty} a_{n}=0$ and $\left\{b_{n}\right\}$ is a bounded sequence, then $\lim _{n \rightarrow \infty} a_{n} b_{n}=0$.
````

## 6. Callout 151: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Componentwise Convergence of Complex Sequences
> Suppose that $\left\{a_{n}\right\}$ is a sequence of complex numbers and write $a_{n}=x_{n}+i y_{n}$, where $x_{n}=\operatorname{Re} a_{n}$ and $y_{n}=\operatorname{Im} a_{n}$. Then
>
> $$
> \lim _{n \rightarrow \infty} a_{n}=L=\alpha+i \beta \Leftrightarrow \lim _{n \rightarrow \infty} x_{n}=\alpha \text { and } \lim _{n \rightarrow \infty} y_{n}=\beta .
> $$
````
### After

````text
> [!theorem] Real and Imaginary Parts of Sequences
> Suppose that $\left\{a_{n}\right\}$ is a sequence of complex numbers and write $a_{n}=x_{n}+i y_{n}$, where $x_{n}=\operatorname{Re} a_{n}$ and $y_{n}=\operatorname{Im} a_{n}$. Then
>
> $$
> \lim _{n \rightarrow \infty} a_{n}=L=\alpha+i \beta \Leftrightarrow \lim _{n \rightarrow \infty} x_{n}=\alpha \text { and } \lim _{n \rightarrow \infty} y_{n}=\beta .
> $$
````

## 7. Callout 152: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!definition] Cauchy Sequence of Complex Numbers
> A complex sequence $\left\{a_{n}\right\}$ is said to be a Cauchy sequence if given any $\epsilon>0$ there is an integer $N$ such that
>
> $$
> \left|a_{n}-a_{m}\right|<\epsilon \quad \text { for all } m, n \geq N
> $$
````
### After

````text
> [!definition] Cauchy Sequence
> A complex sequence $\left\{a_{n}\right\}$ is said to be a Cauchy sequence if given any $\epsilon>0$ there is an integer $N$ such that
>
> $$
> \left|a_{n}-a_{m}\right|<\epsilon \quad \text { for all } m, n \geq N
> $$
````

## 8. Callout 153: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Cauchy Criterion for Convergence in the Complex Plane
> A sequence of complex numbers $\left\{a_{n}\right\}$ converges if and only if it is a Cauchy sequence.
````
### After

````text
> [!theorem] Cauchy Sequences
> A sequence of complex numbers $\left\{a_{n}\right\}$ converges if and only if it is a Cauchy sequence.
````

## 9. Callout 154: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!definition] Convergence and Sum of a Complex Series
> For complex terms $a_n$, define the partial sums $s_n=\sum_{k=1}^{n}a_k$.
>
> We say that a series $\sum_{n=1}^{\infty} a_{n}$ converges or is convergent to a complex number $s$ and we write
>
> $$
> s=\sum_{n=1}^{\infty} a_{n}
> $$
>
> if the sequence of partial sums $\left\{s_{n}\right\}$ converges to $s: \lim _{n \rightarrow \infty} s_{n}=s$. Otherwise, we say that the series $\sum_{n=1}^{\infty} a_{n}$ diverges or is divergent.
````
### After

````text
> [!definition] Limit of a Series
> For complex terms $a_n$, define the partial sums $s_n=\sum_{k=1}^{n}a_k$.
>
> We say that a series $\sum_{n=1}^{\infty} a_{n}$ converges or is convergent to a complex number $s$ and we write
>
> $$
> s=\sum_{n=1}^{\infty} a_{n}
> $$
>
> if the sequence of partial sums $\left\{s_{n}\right\}$ converges to $s: \lim _{n \rightarrow \infty} s_{n}=s$. Otherwise, we say that the series $\sum_{n=1}^{\infty} a_{n}$ diverges or is divergent.
````

## 10. Callout 155: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Linearity, Conjugation, and Components of Convergent Complex Series
> Let the series terms be complex numbers.
>
> If $\sum_{n=1}^{\infty} a_{n}$ and $\sum_{n=1}^{\infty} b_{n}$ are convergent series and $\alpha$ and $\beta$ are complex numbers, then
> (i) $\sum_{n=1}^{\infty}\left(\alpha a_{n}+\beta b_{n}\right)=\alpha \sum_{n=1}^{\infty} a_{n}+\beta \sum_{n=1}^{\infty} b_{n}$;
> (ii) $\overline{\sum_{n=1}^{\infty} a_{n}}=\sum_{n=1}^{\infty} \overline{a_{n}}$;
> (iii) $\operatorname{Re}\left(\sum_{n=1}^{\infty} a_{n}\right)=\sum_{n=1}^{\infty} \operatorname{Re}\left(a_{n}\right)$ and $\operatorname{Im}\left(\sum_{n=1}^{\infty} a_{n}\right)=\sum_{n=1}^{\infty} \operatorname{Im}\left(a_{n}\right)$.
````
### After

````text
> [!theorem] Linearity, Conjugation, Real and Imaginary Parts
> Let the series terms be complex numbers.
>
> If $\sum_{n=1}^{\infty} a_{n}$ and $\sum_{n=1}^{\infty} b_{n}$ are convergent series and $\alpha$ and $\beta$ are complex numbers, then
> (i) $\sum_{n=1}^{\infty}\left(\alpha a_{n}+\beta b_{n}\right)=\alpha \sum_{n=1}^{\infty} a_{n}+\beta \sum_{n=1}^{\infty} b_{n}$;
> (ii) $\overline{\sum_{n=1}^{\infty} a_{n}}=\sum_{n=1}^{\infty} \overline{a_{n}}$;
> (iii) $\operatorname{Re}\left(\sum_{n=1}^{\infty} a_{n}\right)=\sum_{n=1}^{\infty} \operatorname{Re}\left(a_{n}\right)$ and $\operatorname{Im}\left(\sum_{n=1}^{\infty} a_{n}\right)=\sum_{n=1}^{\infty} \operatorname{Im}\left(a_{n}\right)$.
````

## 11. Callout 156: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Term Test for Divergence of a Complex Series
> Let the series terms be complex numbers.
>
> If $\sum_{n=1}^{\infty} a_{n}$ is convergent, then $\lim _{n \rightarrow \infty} a_{n}=0$. Equivalently, if either $\lim _{n \rightarrow \infty} a_{n} \neq 0$ or $\lim _{n \rightarrow \infty} a_{n}$ does not exist, then $\sum_{n=1}^{\infty} a_{n}$ diverges.
````
### After

````text
> [!theorem] The nth Term Test for Divergence
> Let the series terms be complex numbers.
>
> If $\sum_{n=1}^{\infty} a_{n}$ is convergent, then $\lim _{n \rightarrow \infty} a_{n}=0$. Equivalently, if either $\lim _{n \rightarrow \infty} a_{n} \neq 0$ or $\lim _{n \rightarrow \infty} a_{n}$ does not exist, then $\sum_{n=1}^{\infty} a_{n}$ diverges.
````

## 12. Callout 157: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!proposition] Vanishing Tails of a Convergent Complex Series
> Let the series terms be complex numbers.
>
> If $\sum_{n=1}^{\infty} a_{n}$ is convergent, then $\lim _{m \rightarrow \infty} \sum_{n=m+1}^{\infty} a_{n}=0$. Hence if a series converges, its tail must go to 0 .
````
### After

````text
> [!proposition] Tail of Series
> Let the series terms be complex numbers.
>
> If $\sum_{n=1}^{\infty} a_{n}$ is convergent, then $\lim _{m \rightarrow \infty} \sum_{n=m+1}^{\infty} a_{n}=0$. Hence if a series converges, its tail must go to 0 .
````

## 13. Callout 158: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Absolute Convergence Implies Convergence of a Complex Series
> Let the series terms be complex numbers.
>
> If $\sum_{n=1}^{\infty} a_{n}$ is absolutely convergent, then it is convergent. In symbols,
>
> $$
> \sum_{n=1}^{\infty}\left|a_{n}\right|<\infty \Rightarrow \sum_{n=1}^{\infty} a_{n} \text { converges. }
> $$
````
### After

````text
> [!theorem] Absolute Convergence Implies Convergence
> Let the series terms be complex numbers.
>
> If $\sum_{n=1}^{\infty} a_{n}$ is absolutely convergent, then it is convergent. In symbols,
>
> $$
> \sum_{n=1}^{\infty}\left|a_{n}\right|<\infty \Rightarrow \sum_{n=1}^{\infty} a_{n} \text { converges. }
> $$
````

## 14. Callout 159: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Comparison Test for Absolute Convergence of a Complex Series
> Suppose that $a_{n}$ are complex numbers, $b_{n}$ are real numbers, $\left|a_{n}\right| \leq b_{n}$ for all $n \geq n_{0}$, and $\sum_{n=1}^{\infty} b_{n}$ is convergent. Then $\sum_{n=1}^{\infty} a_{n}$ is absolutely convergent.
````
### After

````text
> [!theorem] Comparison Test
> Suppose that $a_{n}$ are complex numbers, $b_{n}$ are real numbers, $\left|a_{n}\right| \leq b_{n}$ for all $n \geq n_{0}$, and $\sum_{n=1}^{\infty} b_{n}$ is convergent. Then $\sum_{n=1}^{\infty} a_{n}$ is absolutely convergent.
````

## 15. Callout 160: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Ratio Test for a Complex Series
> Suppose that
>
> $$
> \rho=\lim _{n \rightarrow \infty}\left|\frac{a_{n+1}}{a_{n}}\right|
> $$
>
> exists or is infinite. Then the complex series $\sum_{n=1}^{\infty} a_{n}$ of nonzero terms converges absolutely if $\rho<1$ and diverges if $\rho>1$. If $\rho=1$ the test is inconclusive.
````
### After

````text
> [!theorem] Ratio Test
> Suppose that
>
> $$
> \rho=\lim _{n \rightarrow \infty}\left|\frac{a_{n+1}}{a_{n}}\right|
> $$
>
> exists or is infinite. Then the complex series $\sum_{n=1}^{\infty} a_{n}$ of nonzero terms converges absolutely if $\rho<1$ and diverges if $\rho>1$. If $\rho=1$ the test is inconclusive.
````

## 16. Callout 161: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Root Test for a Complex Series: Limit Form
> Suppose that
>
> $$
> \rho=\lim _{n \rightarrow \infty}\left|a_{n}\right|^{1 / n} 
> $$
>
> either exists or is infinite. Then the complex series $\sum_{n=1}^{\infty} a_{n}$ converges absolutely if $\rho<1$ and diverges if $\rho>1$. If $\rho=1$ the test is inconclusive.
````
### After

````text
> [!theorem] Root Test
> Suppose that
>
> $$
> \rho=\lim _{n \rightarrow \infty}\left|a_{n}\right|^{1 / n} 
> $$
>
> either exists or is infinite. Then the complex series $\sum_{n=1}^{\infty} a_{n}$ converges absolutely if $\rho<1$ and diverges if $\rho>1$. If $\rho=1$ the test is inconclusive.
````

## 17. Callout 162: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Bounded Absolute Partial Sums and Absolute Convergence
> Let the series terms be complex numbers.
>
> Suppose that there is a positive number $M>0$ such that $\sum_{n=1}^{N}\left|a_{n}\right| \leq M$ for all $N$. Then the series $\sum_{n=1}^{\infty} a_{n}$ is absolutely convergent.
````
### After

````text
> [!theorem] Bounded Partial Sums
> Let the series terms be complex numbers.
>
> Suppose that there is a positive number $M>0$ such that $\sum_{n=1}^{N}\left|a_{n}\right| \leq M$ for all $N$. Then the series $\sum_{n=1}^{\infty} a_{n}$ is absolutely convergent.
````

## 18. Callout 163: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Rearrangement Invariance of Absolutely Convergent Complex Series
> Let the series terms be complex numbers.
>
> If $\sum_{n=1}^{\infty} a_{n}$ is absolutely convergent, then every rearrangement is absolutely convergent and converges to the same limit.
````
### After

````text
> [!theorem] Rearrangements
> Let the series terms be complex numbers.
>
> If $\sum_{n=1}^{\infty} a_{n}$ is absolutely convergent, then every rearrangement is absolutely convergent and converges to the same limit.
````

## 19. Callout 164: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!theorem] Cauchy Products of Absolutely Convergent Complex Series
> Let the series terms be complex numbers.
>
> Suppose that $\sum_{n=0}^{\infty} a_{n}$ and $\sum_{n=0}^{\infty} b_{n}$ are absolutely convergent. Then their Cauchy product $\sum_{n=0}^{\infty} c_{n}$, where $c_n=\sum_{k=0}^{n}a_k b_{n-k}$, is absolutely convergent and we have
>
> $$
> \sum_{n=0}^{\infty} c_{n}=\left(\sum_{n=0}^{\infty} a_{n}\right)\left(\sum_{n=0}^{\infty} b_{n}\right) .
> $$
````
### After

````text
> [!theorem] Cauchy Products
> Let the series terms be complex numbers.
>
> Suppose that $\sum_{n=0}^{\infty} a_{n}$ and $\sum_{n=0}^{\infty} b_{n}$ are absolutely convergent. Then their Cauchy product $\sum_{n=0}^{\infty} c_{n}$, where $c_n=\sum_{k=0}^{n}a_k b_{n-k}$, is absolutely convergent and we have
>
> $$
> \sum_{n=0}^{\infty} c_{n}=\left(\sum_{n=0}^{\infty} a_{n}\right)\left(\sum_{n=0}^{\infty} b_{n}\right) .
> $$
````
