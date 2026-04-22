# How to Write Review Questions

## Purpose

Review questions should test whether the reader understands the material beyond surface-level regurgitation. They are "forest for the trees" questions — they probe the *why* behind definitions, the *role* of hypotheses, and the *motivation* for results, not just whether someone can repeat what they read.

## Principles

### Don't give away the answer in the prompt

A question like "Why is an interval $(a,b) \subset \mathbb{R}$ not a region, even though it is open in $\mathbb{R}$ and connected?" is better suited as an exercise. The phrasing already reveals the key tension. A review question should require the student to identify what matters, not just confirm it.

### For theorems, lemmas, and corollaries, ask the question the result answers

Every theorem exists because someone asked a question. The review should pose that question so the student has to reconstruct the theorem's answer. For example, if a theorem states that a function with zero partial derivatives on a region is constant, the review question is: "Does the one-dimensional result — that a function with zero derivative is constant — still hold for functions of two variables, and if so, under what conditions?" This forces the student to understand why the theorem exists, not just what it says.

### Probe the role of hypotheses

Ask why specific conditions in a definition or theorem are necessary. If a definition requires a set to be open, ask why openness is needed. If a proposition requires both subsets in a decomposition to be open, ask why that matters. These questions test whether the reader understands the structure of the result or just memorized its statement.

### Keep questions concise

Questions should be short and direct. Avoid elaborate setups, hints, or multi-part scaffolding. A well-written review question trusts the reader to engage with the material.

### Separate examples and computations into exercises

If a question asks the reader to determine whether specific sets are regions, or to verify a definition against particular examples, it belongs in an exercise section, not the review. Review questions target conceptual understanding; exercises target application.

### Write questions that stand on their own, away from the text

The student answering a review question will not have the section open in front of them. A review is not a reading-comprehension check. Never phrase a question in a way that refers to "the three definitions in this section," "the inequalities used in the proof above," "the replacements made in the $\varepsilon$–$\delta$ statement," or any other construction that only makes sense if the reader is simultaneously looking at the passage. A well-written review question should read the same whether the student has just finished the section or is coming back to it months later from memory.

Concretely, this means:

- Do not reference "the definition above," "the theorem on this page," "the inequality (15)," etc.
- Do not ask "why does the proof use X" — instead, ask the conceptual question that X was introduced to answer.
- Do not ask the student to locate or identify features of the presentation (where a quantifier appears, which inequality gets used, which line of the proof does what).
- Ask the student to reproduce, motivate, or justify the mathematical content itself, as if no text were available.

#### Example: bad vs. good

**Bad (assumes the text is in front of the student):**

> In the three definitions of limits involving infinity, where does the quantifier "for any $M > 0$" (or "for any $\varepsilon > 0$") appear, and what would be lost if it were weakened to "for some sufficiently large $M$"?

This question only makes sense if the reader can look at "the three definitions" on the page. It is asking the student to inspect the text, not to reconstruct the mathematics.

**Good (stands on its own):**

> What does it mean for a complex-valued function to have limit $\infty$ at a point, to have a finite limit as its input goes to $\infty$, or to have limit $\infty$ as its input goes to $\infty$? Give a precise definition of each.

This version forces the student to produce the definitions themselves from memory and understanding, with no dependence on the surrounding text.

## Question patterns that work well

- "What does it mean for X, and why is [specific detail in the definition] important?"
- "Why is it necessary that [hypothesis] in order to [conclusion]?"
- "What two properties define X, and why is each one needed independently?"
- "[Motivating question that a theorem answers]?"
- "How can you [accomplish goal] without [the obvious but harder approach]?"

## Question patterns to avoid

- True/false questions
- "State the definition of X" (pure recall)
- Questions with hints or justifications embedded in the prompt
- Questions that ask the reader to compare two things without a clear conceptual target
- Questions whose answer is a single word or yes/no



# Example




We have avoided thus far dealing with limits that involve $\infty$. What do we mean by statements such as $\lim _{z \rightarrow z_{0}} f(z)=\infty$ or $\lim _{z \rightarrow \infty} f(z)=L$ or even $\lim _{z \rightarrow \infty} f(z)=\infty$ ? We answer these questions and complete our discussion of limits by introducing the following definitions.

> [!definition] Limits Involving Infinity
> (i) We write $\lim _{z \rightarrow z_{0}} f(z)=\infty$ to mean that for any $M>0$ there is a $\delta>0$ such that $\left|z-z_{0}\right|<\delta \Rightarrow|f(z)|>M$.
> (ii) We write $\lim _{z \rightarrow \infty} f(z)=L$ to mean that for any $\epsilon>0$ there is an $R>0$ such that $|z|>R \Rightarrow|f(z)-L|<\epsilon$.
> (iii) We write $\lim _{z \rightarrow \infty} f(z)=\infty$ to mean that for any $M>0$ there is an $R>0$ such that $|z|>R \Rightarrow|f(z)|>M$.

Looking at these definitions, we see that $z \rightarrow \infty$ means that the real quantity $|z| \rightarrow \infty$, and similarly $f(z) \rightarrow \infty$ means that $|f(z)| \rightarrow \infty$. Hence

$$
\lim _{z \rightarrow z_{0}} f(z)=\infty \quad \Leftrightarrow \quad \lim _{z \rightarrow z_{0}}|f(z)|=\infty ;
$$

$$
\lim _{z \rightarrow \infty} f(z)=L \Leftrightarrow \lim _{z \rightarrow \infty}|f(z)-L|=0 ;
$$

$$
\lim _{z \rightarrow \infty} f(z)=\infty \quad \Leftrightarrow \quad \lim _{z \rightarrow \infty}|f(z)|=\infty .
$$

Limits at infinity can also be reduced to limits at $z_{0}=0$ by means of the inversion $1 / z$. The idea is that taking the limit as $z \rightarrow \infty$ of $f(z)$ is the same thing as taking the limit as $z \rightarrow 0$ of $f\left(\frac{1}{z}\right)$. So you can check that

$$
\lim _{z \rightarrow \infty} f(z)=L \quad \Leftrightarrow \quad \lim _{z \rightarrow 0} f\left(\frac{1}{z}\right)=L
$$

and

$$
\lim _{z \rightarrow \infty} f(z)=\infty \quad \Leftrightarrow \quad \lim _{z \rightarrow 0} f\left(\frac{1}{z}\right)=\infty .
$$

These equivalent statements are sometimes useful. For example, appealing to (15), we have

$$
\lim _{z \rightarrow \infty} \frac{1}{z}=\lim _{z \rightarrow 0} \frac{1}{1 / z}=\lim _{z \rightarrow 0} z=0
$$

Similarly, for any constant $c$ and positive integer $n$, we have

$$
\lim _{z \rightarrow \infty} \frac{c}{z^{n}}=\lim _{z \rightarrow 0} \frac{c}{1 / z^{n}}=\lim _{z \rightarrow 0} c z^{n}=0
$$



## Bad Example of Review questions for this section


1. In real analysis, " $x \rightarrow \infty$ " and " $f(x) \rightarrow \infty$ " are distinguished from ordinary limits by using sign ( $+\infty$ vs. $-\infty$ ) and unboundedness. Why can't the complex case simply carry these definitions over unchanged, and what does the complex definition of "approaching $\infty$ " end up capturing instead?
2. The three definitions in this section replace one of the quantities in an ordinary $\varepsilon-\delta$ statement with something of the form $|z|>R$ or $|f(z)|>M$. What does each of these replacements mean geometrically, and why is a single "point at infinity" the right object to attach these statements to rather than a collection of directional infinities?
3. How can a question about a limit at $\infty$ be converted into a question about a limit at a finite point, and why is it legitimate to treat the behavior of $f(z)$ as $z \rightarrow \infty$ and the behavior of $f(1 / z)$ as $z \rightarrow 0$ as interchangeable?
4. Why are the equivalences $\lim _{z \rightarrow z_0} f(z)=\infty \Leftrightarrow \lim _{z \rightarrow z_0}|f(z)|=\infty$ (and its analogues) useful, given that the left-hand sides are already defined directly? What do they let you borrow from real analysis that the original definitions do not?
5. In the three definitions of limits involving infinity, where does the quantifier "for any $M>0$ " (or "for any $\varepsilon>0$ ") appear, and what would be lost if it were weakened to "for some sufficiently large $M^{\prime \prime}$ ?


## Good Example of Review Questions for the same section

1. What does it mean for a complex-valued function to have limit $\infty$ at a point, to have a finite limit as its input goes to $\infty$, or to have limit $\infty$ as its input goes to $\infty$ ? Give a precise definition of each.
2. In the real line, "going to infinity" splits into $+\infty$ and $-\infty$. What is the analogous notion for the complex plane, and why does it collapse to a single object rather than a family of directional infinities?
3. How can a limit as $z \rightarrow \infty$ be rephrased as a limit at a finite point, and why is that rephrasing valid?
4. Once limits involving $\infty$ are defined for complex-valued functions, how can they be reduced to limits of real-valued (nonnegative) quantities, and why is that reduction useful?
5. Compute $\lim _{z \rightarrow \infty} c / z^n$ for a constant $c$ and a positive integer $n$, using the reduction from a limit at $\infty$ to a limit at 0 .



