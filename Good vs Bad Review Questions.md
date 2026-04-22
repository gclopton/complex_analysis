
# Example 1: The mean value theorem for functions of several variables





> [!review] Bad Review Question
> 1. Let $U \subset \mathbb{R}^n$ be open, let $f: U \rightarrow \mathbb{R}$ be differentiable, and let $\mathbf{a}, \mathbf{b} \in U$ be points such that the segment $[\mathbf{a}, \mathbf{b}]$ is contained in $U$. Formulate the analogue of the one-variable mean value theorem in this setting, and prove it.
> 2. Let $U \subset \mathbb{R}^n$ be open, let $f: U \rightarrow \mathbb{R}$ be differentiable, and let $\mathbf{a}, \mathbf{b} \in U$ be points such that the segment $[\mathbf{a}, \mathbf{b}]$ is contained in $U$. Bound $|f(\mathbf{b})-f(\mathbf{a})|$ above in terms of $|\mathbf{b}-\mathbf{a}|$ and the derivative of $f$, and prove your answer.
> 3. Let $U \subset \mathbb{R}^n$ be open, let $f: U \rightarrow \mathbb{R}$ be differentiable, and let $\mathbf{a}, \mathbf{b} \in U$ be points such that the segment $[\mathbf{a}, \mathbf{b}]$ is contained in $U$. The multivariable mean value theorem produces a specific intermediate point $\mathbf{c}_0 \in(\mathbf{a}, \mathbf{b})$ for which $|f(\mathbf{b})-f(\mathbf{a})| \leq \left|\left[\mathbf{D} f\left(\mathbf{c}_0\right)\right]\right| \cdot|\mathbf{b}-\mathbf{a}|$. What advantage does the bound $|f(\mathbf{b})-f(\mathbf{a})| \leq \left(\sup _{\mathbf{c} \in[\mathbf{a}, \mathbf{b}]}|[\mathbf{D} f(\mathbf{c})]|\right) \cdot|\mathbf{b}-\mathbf{a}|$ have over this?



> [!review] Good Example
> 4. Can the total finite change in a multivariable function be represented by an instantaneous rate of change at some intermediate point? Prove your answer.
> 5. If I know how large the derivative can be, how much can the function value change between two points? Prove your answer.





The derivative measures the difference of the values of functions at different points. For functions of one variable, the mean value theorem (Theorem 1.6.13) says that if $f:[a, b] \rightarrow \mathbb{R}$ is continuous, and $f$ is differentiable on $(a, b)$, then there exists $c \in(a, b)$ such that

$$
f(b)-f(a)=f^{\prime}(c)(b-a) .
$$


The analogous statement in several variables is the following.



> [!theorem] -Theorem 1.9.1 (Mean value theorem for functions of several variables). 
> Let $U \subset \mathbb{R}^n$ be open, let $f: U \rightarrow \mathbb{R}$ be differentiable, and let the segment $[\mathrm{a}, \mathrm{b}]$ joining a to b be contained in $U$. Then there exists $\mathbf{c}_0 \in(\mathbf{a}, \mathbf{b})$ such that
> 
> $$
> f(\mathbf{b})-f(\mathbf{a})=\left[\mathbf{D} f\left(\mathbf{c}_0\right)\right](\mathbf{b}-\mathbf{a}) .
> $$



> [!NOTE]
> Theorem 1.9.1: The segment [a, b] is the image of the map
> 
> $$
> t \mapsto(1-t) \mathbf{a}+t \mathbf{b} .
> $$
> 
> for $0 \leq t \leq 1$.



> [!corollary] -Corollary 1.9.2. 
> If $f$ is a function as defined in Theorem 1.9.1, then
> 
> $$
> |f(\mathbf{b})-f(\mathbf{a})| \leq\left(\sup _{\mathbf{c} \in[\mathbf{a}, \mathbf{b}]}|[\mathbf{D} f(\mathbf{c})]|\right)|\mathbf{b}-\mathbf{a}| . \tag{1.9.3}
> $$
> 
> 
> 



> [!NOTE]
> Why do we write inequality 1.9 .3 with the sup, rather than
> 
> $$
> |f(\mathbf{b})-f(\mathbf{a})| \leq|[\mathbf{D} f(\mathbf{c})]||\mathbf{b}-\mathbf{a}|,
> $$
> 
> which of course is also true? Using the sup means that we do not need to know the value of c in order to relate how fast $f$ is changing to its derivative; we can run through all $\mathbf{c} \in[\mathbf{a}, \mathbf{b}]$ and choose the one where the derivative is greatest. This will be useful in Section 2.8 when we discuss Lipschitz ratios.



> [!exercise] Proof of Corollary 1.9.2.


This follows immediately from Theorem 1.9.1 and Proposition 1.4.11.


++++



> [!exercise] Proof of Theorem 1.9.1.


As $t$ varies from 0 to 1 , the point $(1-t) \mathbf{a}+t \mathbf{b}$ moves from $\mathbf{a}$ to $\mathbf{b}$. Consider the mapping $g(t)=f((1-t) \mathbf{a}+t \mathbf{b})$. By the chain rule, $g$ is differentiable, and by the one-variable mean value theorem, there exists $t_0 \in(0,1)$ such that

$$
g(1)-g(0)=g^{\prime}\left(t_0\right)(1-0)=g^{\prime}\left(t_0\right) .
$$


Set $\mathbf{c}_0=\left(1-t_0\right) \mathbf{a}+t_0 \mathbf{b}$, so $\mathbf{c}_0$ is in $(\mathbf{a}, \mathbf{b})$. By Proposition 1.7.14, we can express $g^{\prime}\left(t_0\right)$ in terms of the derivative of $f$ :

$$
\begin{aligned}
g^{\prime}\left(t_0\right) & =\lim _{s \rightarrow 0} \frac{g\left(t_0+s\right)-g\left(t_0\right)}{s} \\
& =\lim _{s \rightarrow 0} \frac{f\left(\mathbf{c}_0+s((\mathbf{b}-\mathbf{a}))-f\left(\mathbf{c}_0\right)\right.}{s}=\left[\mathbf{D} f\left(\mathbf{c}_0\right)\right](\overrightarrow{\mathbf{b}-\mathbf{a}}) .
\end{aligned}
$$


So equation 1.9.4 reads

$$
f(\mathbf{b})-f(\mathbf{a})=\left[\mathbf{D} f\left(\mathbf{c}_0\right)\right](\mathbf{b}-\mathbf{a}) .
$$



# Example 2: Cauchy's Integral Formula



> [!review] Bad Example
> 1. Let $f$ be analytic on and inside a simple closed positively oriented path $C$, and let $z_0$ be a point inside $C$. Can $f\left(z_0\right)$ be determined from the values of $f$ on $C$ alone, and if so, how? Prove your answer.
> 2. Let $f$ be analytic on and inside a simple closed positively oriented path $C$, and let $z_0$ be a point outside $C$. What can be said about $\frac{1}{2 \pi i} \int_C \frac{f(z)}{z-z_0} d z$ ? Prove your answer.


> [!review] Good Example
> 1. If a function is analytic on and inside a closed curve, can its value at an interior point be recovered exactly from its values on the enclosing curve alone? Prove your answer.
> 2. If the reconstruction integral from Cauchy's formula is evaluated at a point outside the curve instead of inside, what value does it take, and why? Prove your answer.






Recall: The closed disk of radius $R$ centered at $z_{0}$ is defined as $S_{R}\left(z_{0}\right)=\{z: \mid z- \left.2_{0} \mid \leq R\right\}$. This set includes its boundary.

In this section we develop one of the most important consequences of Cauchy's integral theorem. It is the Cauchy integral formula, which will enable us to compute many interesting integrals, and more importantly, we will use it to derive fundamental properties of analytic functions.


> [!theorem] Theorem 1: Cauchy's Integral Formula
> Suppose that $f$ is analytic inside and on a simple closed path $C$ with positive orientation. If $z$ is any point inside $C$, then
> 
> $$
> f(z)=\frac{1}{2 \pi i} \int_{C} \frac{f(\zeta)}{\zeta-z} d \zeta
> $$
> 

**Proof** Given $z$ inside $C$, let $R>0$ be such that the closed disk $S_{R}(z)$ is contained in the region inside $C$. The function $\zeta \mapsto \frac{f(\zeta)}{\zeta-z}$ is analytic in the region inside $C$ and outside the circle $C_{r}(z)$, where $0<r \leq R$ (see _Figure 1_). 


> [!figure] Figure 1
> 
> ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-067_485_462_1175_36.jpg)
> Figure 1 The path $C$ can be continuously deformed into the circle $C_{r}(z)$, which explains the equality (2).



Applying Cauchy's theorem for multiply connected regions, Theorem 6, Section 3.4 (with the variable of integration being $\zeta$ and the integrand being $\frac{f(\zeta)}{\zeta-z}$ ), we obtain

$$
\frac{1}{2 \pi i} \int_{C} \frac{f(\zeta)}{\zeta-z} d \zeta=\frac{1}{2 \pi i} \int_{C_{r}(z)} \frac{f(\zeta)}{\zeta-z} d \zeta
$$

where $C$ and $C_{r}(z)$ are positively oriented. Since this equality holds for all $0<r \leq R$, taking limits on both sides, we get

$$
\frac{1}{2 \pi i} \int_{C} \frac{f(\zeta)}{\zeta-z} d \zeta=\lim _{r \rightarrow 0^{+}} \frac{1}{2 \pi i} \int_{C_{r}(z)} \frac{f(\zeta)}{\zeta-z} d \zeta
$$

To finish off the proof, we must show that the limit is $f(z)$. Parametrize $C_{r}(z)$ by $\gamma(t)=z+r e^{i t}, 0 \leq t \leq 2 \pi, \gamma^{\prime}(t)=i r e^{i t} d t$. Then

$$
\frac{1}{2 \pi i} \int_{C_{r}(z)} \frac{f(\zeta)}{\zeta-z} d \zeta=\frac{1}{2 \pi i} \int_{0}^{2 \pi} \frac{f\left(z+r e^{i t}\right)}{r e^{i t}} i r e^{i t} d t=\frac{1}{2 \pi} \int_{0}^{2 \pi} f\left(z+r e^{i t}\right) d t
$$

For fixed $z$, the function $t \mapsto f\left(z+r e^{i t}\right)$ is a continuous complex-valued function of $t$ and $r$ in $[0,2 \pi] \times[0, R]$. So by Theorem 5(i), Section 3.5, if we integrate it with respect to $t$, we get a continuous function of $r: \phi(r)=\frac{1}{2 \pi} \int_{0}^{2 \pi} f\left(z+r e^{i t}\right) d t$. Thus, $\lim _{r \rightarrow 0^{+}} \phi(r)=\phi(0)=\frac{1}{2 \pi} \int_{0}^{2 \pi} f(z) d t=f(z)$, as required. $\square$



Before we move to the applications of (1), let us note that if in Cauchy's formula $z$ is any point outside $C$, then

$$
\frac{1}{2 \pi i} \int_{C} \frac{f(\zeta)}{\zeta-z} d \zeta=0
$$

This is an immediate consequence of Cauchy's theorem for simple paths (Theorem 5, Section 3.4), since in this case the integrand $\zeta \mapsto \frac{f(\zeta)}{\zeta-z}$ is analytic
on and inside $C$, and so its integral along $C$ is zero. We combine (1) and (4) in one convenient formula in which the variable of integration is denoted $z$ :

$$
\frac{1}{2 \pi i} \int_{C} \frac{f(z)}{z-z_{0}} d z= \begin{cases}f\left(z_{0}\right) & \text { if } z_{0} \text { is inside } C \\ 0 & \text { if } z_{0} \text { is outside } C\end{cases}
$$

(It is traditional to change the variables of integration from $\zeta$ to $z$ when applying Theorem 1.)


> [!exercise] Exercise 1: Cauchy's integral formula
> 
> Let $C_{R}\left(z_{0}\right)$ denote the positively oriented circle with center at $z_{0}$ and radius $R>0$. Compute the following integrals.
> (a) $\quad \int_{C_{2}(0)} \frac{e^{z}}{z+1} d z$,
> (b) $\quad \int_{C_{2}(1)} \frac{z^{2}+3 z-1}{(z+3)(z-2)} d z$,

##### problem 1(a)

Solution (a) Write the integral as $\int_{C_{2}(0)} \frac{e^{z}}{z-(-1)} d z$. Since -1 is inside the circle $C_{2}(0)$, Cauchy's integral formula (5) with $f(z)=e^{z}$ and $z_{0}=-1$ implies

$$
\int_{C_{2}(0)} \frac{e^{z}}{z-(-1)} d z=2 \pi i e^{-1}
$$

##### problem 2(b)

(b) In evaluating $\int_{C_{2}(1)} \frac{z^{2}+3 z-1}{(z+3)(z-2)} d z$, we first note that the integrand is not analytic at the points $z=-3$ and $z=2$. Only the point $z=2$ is inside the curve $C_{2}(0)$. So if we let $f(z)=\frac{z^{2}+3 z-1}{z+3}$ the integral takes the form

$$
\int_{C_{2}(1)} \frac{f(z)}{z-2} d z=2 \pi i f(2)=\frac{18 \pi}{5} i
$$

by Cauchy's integral formula, applied at $z_{0}=2$.

---



Some integrals require multiple applications of Cauchy's formula along with applications of Cauchy's theorem. We illustrate with one example.


> [!exercise] Exercise 2: Multiple applications of Cauchy's formula
> 
> Compute
> 
> $$
> \int_{C_{2}(0)} \frac{e^{\pi z}}{z^{2}+1} d z
> $$
> 
> 

**Solution** Since $z^{2}+1=(z+i)(z-i)$, the integral cannot be computed directly from Cauchy's formula, since the path contains both $\pm i$ in its interior. To overcome this difficulty, draw small nonintersecting circles inside $C_{2}(0)$ around $\pm i$, say $C_{1 / 4}(i)$ and $C_{1 / 4}(-i)$, as illustrated in _Figure 2_. 


> [!figure] Figure 2
> 
> ![300](./images/858d24a8-ffa3-45ac-9ebe-5fc1408bbf28-068_519_519_1705_79.jpg)
> 
> Figure 2 The mean value property of $f$ states that the value of $f$ at $z$ is equal to the average value of $f$ around any circle in $\Omega$ centered at $z$.
> 



Since $\frac{e^{\pi z}}{z^{2}+1}$ is analytic in a region containing the interior of $C_{2}(0)$ and the exterior of the smaller circles, by Cauchy's theorem for multiply connected regions (Theorem 6, Section 3.4), we have

$$
\int_{C_{2}(0)} \frac{e^{\pi z}}{z^{2}+1} d z=\int_{C_{1 / 4}(i)} \frac{e^{\pi z}}{z^{2}+1} d z+\int_{C_{1 / 4}(-i)} \frac{e^{\pi z}}{z^{2}+1} d z
$$

Now, the two integrals on the right can be evaluated with the help of Cauchy's integral formula (5). For the first one, we apply Cauchy's formula (5) with $^{\pi z}(z)= \frac{e^{\pi z}}{z+i}$ and $z_{0}=i$, and obtain

$$
\int_{C_{1 / 4}(i)} \frac{e^{\pi z}}{(z-i)(z+i)} d z=\int_{C_{1 / 4}(i)} \frac{f(z)}{z-i} d z=2 \pi i f(i)
$$

Since $f(i)=\frac{e^{i \pi}}{2 i}=\frac{-1}{2 i}=\frac{i}{2}$, we get

$$
\int_{C_{1 / 4}(i)} \frac{f(z)}{z-i} d z=-\pi
$$

For the second integral, we have

$$
\int_{C_{1 / 4}(-i)} \frac{e^{\pi z}}{(z-i)(z+i)} d z=\int_{C_{1 / 4}(-i)} \frac{g(z)}{z+i} d z=2 \pi i g(-i)
$$

where $g(z)=\frac{e^{\pi z}}{z-i}$, and so $g(-i)=\frac{e^{-i \pi}}{-2 i}=\frac{1}{2 i}=-\frac{i}{2}$. Hence

$$
\int_{C_{1 / 4}(-i)} \frac{g(z)}{z-i} d z=\pi
$$

Adding the two integrals together, we find that

$$
\int_{C_{2}(0)} \frac{e^{\pi z}}{(z-i)(z+i)} d z=0
$$



