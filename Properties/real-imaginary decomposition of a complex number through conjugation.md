
Both the real and complex parts of a complex number can each be expressed in terms of the complex number and its conjugate.

**Proof:**
We know that $z = a + ib$ so $\operatorname{Re} z = a$, and $\operatorname{Im}z = b$. Also, $\bar{z}=a - ib$. So we have


$$\begin{aligned} z+\bar{z} & =a+i b+(a-i b) \\ & =2 a \\ & =2 \operatorname{Re} z\end{aligned}$$
Dividing both sides by 2, we obtain:

$$\frac{z + \bar{z}}{2} = \frac{2\operatorname{Re}z}{2}=\operatorname{2}.$$

Similarly
$$
z-\bar{z}=a+i b-(a-i b)=2 i b=2 i \operatorname{Im} z
$$

upon dividing both sides by $2 i$, we have:

$$z - \bar{z} = \operatorname{Im}z$$


**_Facts:_**
- These formulas show that the real part and imaginary part are linear operators on the complex numbers.
- These formulas make it clear that $\operatorname{Re}z$ and $\operatorname{Im}z$ are projections of $z$ in the plane, definable without coordinates.
- These identities are useful for splitting functions into real and imaginary parts. You will see this in the context of complex integration and Fourier analysis.
- **Abstract algebra / Galois theory:** The map $z \mapsto \bar{z}$ is a nontrivial automorphism of $\mathbb{C}$ over $\mathbb{R}$. These formulas describe how the fixed field $\mathbb{R}$ and the imaginary direction are recovered from $z$ and $\bar{z}$.
