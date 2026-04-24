


**How to write a proof sketch.**

A proof sketch in this style is a procedural walkthrough of the argument, not a prose summary written after the fact and not a full proof with every computation. The goal is to let the reader follow the moves of the proof in order — what is set up, what is constructed, what is invoked — with just enough commentary that the reason behind each move is visible. It sits between a recap and a formal proof.

1. Break the proof into its natural stages, cases, or subgoals, and give each one a short header describing what that stage is responsible for. If the proof is case-based, state the defining hypothesis of each case in the header so the reader does not have to hunt for it. If the proof is linear — for instance, a direct derivation, an induction, or a construction followed by a verification — a single numbered list under one header is fine. For inductions, the base case and the inductive step should each get their own block.
    
2. Within each stage, use a numbered list of steps. Each step should correspond to an actual move in the proof — introducing an object, invoking a definition or theorem, performing a key estimate or manipulation, discharging a subgoal — not to a line of computation. If two steps amount to the same move written twice, merge them. If a step is really two distinct moves bolted together, split them.
    
3. Attach reasoning to the steps where the reason is non-obvious or where the step depends on a constraint the reader should notice (why a particular auxiliary object is chosen, why a particular theorem applies, why a quantity is nonzero or has a given sign). Do not attach reasoning to purely mechanical steps, and do not start every step with "because" — the reasoning should flow naturally as a second clause or a follow-on sentence.
    
4. Write verbally by default. Describe objects, relations, and conditions in words rather than symbols when the wording is unambiguous. Use mathematical notation only when it is either the genuine content of the step (a defining equation, a key inequality, a parameterization, a change of variables) or when verbal language would be vaguer than the symbols. Aim for sentences a reader could follow aloud.
    
5. Control the level of detail. A sketch should name each move but not execute every routine computation — expansions, cancellations, algebraic rearrangements, standard substitutions. If a computation carries the load of the argument (a non-obvious cancellation, a critical sign or bound, the precise application of a named result), keep it. If it is mechanical, state the result and move on.
    
6. Use precise mathematical terminology appropriate to the subject. Write the established names — associativity, continuity, compactness, exactness, linearity, whatever the proof actually uses — rather than informal paraphrases. Avoid casual proof vocabulary ("clearly," "trivially," "we notice," colloquial coinages) and avoid pet metaphors dressed up as terms.
    
7. Close with a brief combining step that states how the cases or stages fit together to give the full conclusion. It is usually one or two sentences and does not need to be numbered.
    

Several patterns recur across proofs in different areas and are worth handling consistently.

When introducing an auxiliary quantity chosen to satisfy several constraints simultaneously, name those constraints in the same step where the quantity is introduced, so the reader sees why the specific choice — a minimum, a maximum, a generic element, a particular index — is the right one.

When two or more parallel constructions appear in the same stage, give them parallel numbered steps rather than merging them; the symmetry is easier to read when the structure of the sketch mirrors it.

When invoking a previously established result, a definition, or a prior part of the problem, state what the result or definition says rather than citing it only by label. The sketch should remain intelligible without a second document open.

When an argument proceeds by a standard technique — induction, contradiction, contrapositive, cases, a deformation or continuity argument, passage to a limit — flag the technique at the start of the stage so the reader knows the shape of what follows.

Let me know if you want anything trimmed or reorganized before you save it.


# Example



> [!sketch]
> 
> **Case 1:** $z$ lies on the circle, i.e., at distance exactly $r$ from $z_0$. We show $z$ is a boundary point.
> 1. Fix an arbitrary $\varepsilon>0$ and set $\eta=\min \{\varepsilon / 2, r / 2\}$. The first constraint keeps the nudge length below $\varepsilon$, and the second keeps it below $r$, so that moving inward from the circle stays inside the ball.
> 2. Work on the radial line through $z_0$ and $z$, parameterized as $z_0+t\left(z-z_0\right)$. The distance from $z_0$ to such a point is $t \cdot r$, which lets us place points at any prescribed distance from $z_0$ by choosing $t$ accordingly.
> 3. Slide inward by choosing $t=1-\eta / r$ to produce $w_1$, which sits at distance $r-\eta$ from $z_0$ and at distance $\eta$ from $z$. The first fact places $w_1$ inside the ball; the second places it inside the $\varepsilon$-neighborhood of $z$.
> 4. Slide outward by choosing $t=1+\eta / r$ to produce $w_2$, which sits at distance $r+\eta$ from $z_0$ and again at distance $\eta$ from $z$. This places $w_2$ outside the ball and still inside the $\varepsilon$ neighborhood of $z$.
> 5. Since $\varepsilon$ was arbitrary and both constructions used the same $\eta$, every $\varepsilon$-neighborhood of $z$ contains a point in the ball and a point outside it. Hence $z$ is a boundary point.
> 
> **Case 2:** $z$ is strictly inside the ball, i.e., at distance less than $r$ from $z_0$. By part (a), $z$ is an interior point of the ball, and an interior point has a neighborhood contained entirely inside the ball, which rules out being a boundary point.
> 
> **Case 3:** $z$ is strictly outside the ball, i.e., at distance greater than $r$ from $z_0$.
> 6. Let $\rho=\left|z-z_0\right|-r$, which is positive because $z$ lies outside the circle.
> 7. For any $w$ in $B_\rho(z)$, the reverse triangle inequality gives $\left|w-z_0\right| \geq\left|z-z_0\right|-\mid w- z\left|>\left|z-z_0\right|-\rho=r\right.$, so $w$ lies outside the ball.
> 8. Therefore $B_\rho(z)$ is disjoint from the ball, so $z$ has a neighborhood containing no points of the ball and cannot be a boundary point.
> 
> **Combining the cases:** every point of the plane falls into exactly one case, and only Case 1 produces boundary points. So the boundary of the ball is exactly the circle of points at distance $r$ from $z_0$.
> 







> [!verbalization]
> First let $z$ satisfy the equation that the distance from $z$ to $z_0$ equals $r$ - that is, $z$ lies exactly on the circle of radius $r$ around $z_0$. We show that $z$ is a boundary point of $B_r\left(z_0\right)$. Let $\varepsilon$ be an arbitrary positive number; our goal is to find a point of $B_r\left(z_0\right)$ and a point outside $B_r\left(z_0\right)$, both within distance $\varepsilon$ of $z$. Choose $\eta$ to be the smaller of $\varepsilon / 2$ and $r / 2$; this ensures $\eta$ is positive, strictly less than $r$, and at most $\varepsilon / 2$. The idea is now geometric: $z$ sits on the circle, and we will nudge it slightly inward along the radial line through $z_0$ and $z$ to produce a point $w_1$ inside the ball, and slightly outward along the same line to produce a point $w_2$ outside the ball, each at distance exactly $\eta$ from $z$.
> 
> To construct $w_1$, we parameterize points on the radial line as $z_0+t\left(z-z_0\right)$, where $t$ is a scalar. When $t$ is zero, we are at $z_0$; when $t$ is one, we are at $z$; and for $t$ between zero and one, we are somewhere along the segment, at distance $t \cdot r$ from $z_0$. We want $w_1$ to sit at distance $r-\eta$ from $z_0$ - that is, $\eta$ units short of the boundary - so we need $t \cdot r$ to equal $r-\eta$, which gives $t$ equal to $1-\eta / r$. Accordingly, define $w_1$ as $z_0$ plus $(1-\eta / r)$ times the vector from $z_0$ to $z$. This scaling factor is positive because $\eta$ is less than $r$. Then the distance from $w_1$ to $z_0$ is $(1-\eta / r)$ times the distance from $z$ to $z_0$, which is $(1-\eta / r) \cdot r$, or $r-\eta$, which is strictly less than $r$. Hence $w_1$ lies in $B_r\left(z_0\right)$. The distance from $w_1$ to $z$ is $\eta / r$ times the distance from $z$ to $z_0$, which equals $\eta$, which is at most $\varepsilon / 2$ and therefore strictly less than $\varepsilon$. Thus every neighborhood of $z$ contains a point of $B_r\left(z_0\right)$.
> 
> The construction of $w_2$ follows the same logic, but now we want to travel past $z$ by $\eta$ units along the same radial direction, landing at distance $r+\eta$ from $z_0$. Setting $t \cdot r$ equal to $r+\eta$ gives $t$ equal to $1+\eta / r$. Accordingly, define $w_2$ as $z_0$ plus $(1+\eta / r)$ times the vector from $z_0$ to $z$. The distance from $w_2$ to $z_0$ is $(1+\eta / r) \cdot r$, which equals $r+\eta$, strictly greater than $r$, so $w_2$ does not lie in $B_r\left(z_0\right)$. The distance from $w_2$ to $z$ is again $\eta$, which is strictly less than $\varepsilon$. Hence every neighborhood of $z$ contains both a point in $B_r\left(z_0\right)$ and a point not in $B_r\left(z_0\right)$, so $z$ is a boundary point. 
> 
> Conversely, suppose $z$ is not on the circle. If the distance from $z$ to $z_0$ is strictly less than $r$, then by part (a), $z$ is an interior point of $B_r\left(z_0\right)$, and in particular it is not a boundary point. If the distance from $z$ to $z_0$ is strictly greater than $r$, set $\rho$ equal to that distance minus $r$, which is positive. We claim that the open ball of radius $\rho$ around $z$ lies entirely outside $B_r\left(z_0\right)$. Indeed, for any $w$ in $B_\rho(z)$, the reverse triangle inequality says that the distance from $w$ to $z_0$ is at least the absolute difference between the distance from $z$ to $z_0$ and the distance from $w$ to $z$; since the latter is less than $\rho$, this lower bound is strictly greater than the distance from $z$ to $z_0$ minus $\rho$, which by the definition of $\rho$ equals $r$. Hence $w$ lies outside $B_r\left(z_0\right)$. Therefore $z$ has a neighborhood containing no points of $B_r\left(z_0\right)$, so $z$ cannot be a boundary point. Combining the three cases, the boundary of $B_r\left(z_0\right)$ is exactly the circle where the distance from $z$ to $z_0$ equals $r$.


First let $z$ satisfy

$$
\left|z-z_0\right|=r
$$


We show that $z$ is a boundary point of $B_r\left(z_0\right)$. Let $\varepsilon>0$. Choose

$$
\eta=\min \left\{\frac{\varepsilon}{2}, \frac{r}{2}\right\} .
$$


Then $0<\eta<r$ and $\eta \leq \varepsilon / 2$.
Consider points on the radial line through $z_0$ and $z$, which can be written in the form

$$
z_0+t\left(z-z_0\right)
$$

where $t$ is a real scalar. When $t=0$, this gives $z_0$; when $t=1$, this gives $z$; and when $0<t<1$, the point lies between $z_0$ and $z$.

We first construct a point inside $B_r\left(z_0\right)$ that lies within distance $\varepsilon$ of $z$. We want a point on this line whose distance from $z_0$ is $r-\eta$. Since

$$
\left|z_0+t\left(z-z_0\right)-z_0\right|=\left|t\left(z-z_0\right)\right|=t\left|z-z_0\right|=t r
$$

we need $t r=r-\eta$, so


$$
t=1-\frac{\eta}{r}
$$


Thus define

$$
w_1=z_0+\left(1-\frac{\eta}{r}\right)\left(z-z_0\right)
$$


Then

$$
\begin{aligned}
\left|w_1-z_0\right| & =\left|\left(1-\frac{\eta}{r}\right)\left(z-z_0\right)\right| \\
& =\left(1-\frac{\eta}{r}\right)\left|z-z_0\right| \\
& =\left(1-\frac{\eta}{r}\right) r \\
& =r-\eta \\
& <r
\end{aligned}
$$


so $w_1 \in B_r\left(z_0\right)$. Also,

$$
\begin{aligned}
w_1-z & =z_0+\left(1-\frac{\eta}{r}\right)\left(z-z_0\right)-z \\
& =\left(1-\frac{\eta}{r}\right)\left(z-z_0\right)-\left(z-z_0\right) \\
& =-\frac{\eta}{r}\left(z-z_0\right)
\end{aligned}
$$

hence

$$
\begin{aligned}
\left|w_1-z\right| & =\frac{\eta}{r}\left|z-z_0\right| \\
& =\frac{\eta}{r} r \\
& =\eta \\
& \leq \frac{\varepsilon}{2} \\
& <\varepsilon
\end{aligned}
$$


Thus every neighborhood of $z$ contains a point of $B_r\left(z_0\right)$.


Now we construct a point outside $B_r\left(z_0\right)$ that also lies within distance $\varepsilon$ of $z$. We want a point on the same radial line whose distance from $z_0$ is $r+\eta$. Again writing points on the line as $z_0+t\left(z-z_0\right)$, we need $t r=r+\eta$, so

$$
t=1+\frac{\eta}{r} .
$$


Thus define

$$
w_2=z_0+\left(1+\frac{\eta}{r}\right)\left(z-z_0\right) .
$$


Then

$$
\begin{aligned}
\left|w_2-z_0\right| & =\left|\left(1+\frac{\eta}{r}\right)\left(z-z_0\right)\right| \\
& =\left(1+\frac{\eta}{r}\right)\left|z-z_0\right| \\
& =\left(1+\frac{\eta}{r}\right) r \\
& =r+\eta \\
& >r
\end{aligned}
$$

so $w_2 \notin B_r\left(z_0\right)$. Also,

$$
\begin{aligned}
w_2-z & =z_0+\left(1+\frac{\eta}{r}\right)\left(z-z_0\right)-z \\
& =\left(1+\frac{\eta}{r}\right)\left(z-z_0\right)-\left(z-z_0\right) \\
& =\frac{\eta}{r}\left(z-z_0\right)
\end{aligned}
$$

and therefore

$$
\begin{aligned}
\left|w_2-z\right| & =\frac{\eta}{r}\left|z-z_0\right| \\
& =\frac{\eta}{r} r \\
& =\eta \\
& \leq \frac{\varepsilon}{2} \\
& <\varepsilon
\end{aligned}
$$


Hence every neighborhood of $z$ contains a point in $B_r\left(z_0\right)$ and a point not in $B_r\left(z_0\right)$, so $z$ is a boundary point.

Conversely, if $\left|z-z_0\right|<r$, then part (a) shows that $z$ is an interior point of $B_r\left(z_0\right)$, so $z$ is not a boundary point. If $\left|z-z_0\right|>r$, set

$$
\rho=\left|z-z_0\right|-r>0 .
$$


We claim that $B_\rho(z)$ lies entirely outside $B_r\left(z_0\right)$. Indeed, if $w \in B_\rho(z)$, then $\mid w- z \mid<\rho$, so by the reverse triangle inequality,

$$
\begin{aligned}
\left|w-z_0\right| & \geq| | z-z_0|-|w-z|| \\
& >\left|z-z_0\right|-\rho \\
& =\left|z-z_0\right|-\left(\left|z-z_0\right|-r\right) \\
& =r .
\end{aligned}
$$


So $w \notin B_r\left(z_0\right)$. Thus $z$ has a neighborhood containing no points of $B_r\left(z_0\right)$, so $z$ cannot be a boundary point.

Therefore the boundary of $B_r\left(z_0\right)$ is exactly the circle

$$
\left|z-z_0\right|=r .
$$


