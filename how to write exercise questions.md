# How to Write Exercise Questions

## Purpose

Exercise questions are computational and applicational. They ask the reader to *apply* the material — parametrize a specific curve, compute a specific integral, verify a definition against a particular object — rather than to reconstruct or motivate the underlying concept. The companion documents on review questions cover the conceptual side; this document covers everything that gets routed out of the review and into the exercises section.

## Where exercise questions come from

When processing a section, there are two sources of exercise questions to scan, plus a third decision to make for any labeled callout whose content is already covered elsewhere.

### 1. In-text examples not yet covered by an existing exercise

Some examples in the text are labeled (`EXAMPLE 1`, `EXAMPLE 2`, etc.) and some are buried in motivation prose with no label at all. A single sentence like *"the semicircle $y = \sqrt{1-x^2}$ can be parametrized by $\cos t, \sin t$"* is just as much an in-text example as a fully displayed worked one — and is the kind that is easiest to miss because the text never uses the word "example."

Scan deliberately for both kinds. A labeled `EXAMPLE` block that is already paralleled by an existing Exercise block (the standard `EXAMPLE 1 ↔ Exercise 1` pattern, with specific parameter values plugged into the exercise) is already represented; do not duplicate it. The aim is to surface examples that are *not* yet captured anywhere, which in practice almost always means the unlabeled ones sitting in motivating prose.

### 2. Labeled exercise callouts with no formulated question

Sometimes the vault contains a `[!exercise]` callout that has a worked solution but no question above it — the body jumps straight into a "Solution," a computation, or a `**Proof**` heading with no problem statement. The question for that callout still needs to be written. A callout whose body opens with solution material and has no preceding prompt is the signal. The output for these is a question phrased to fit the existing solution, with a header that points at the specific callout it belongs to.

### 3. Callouts that should be eliminated rather than prompted

Sometimes a labeled `[!exercise]` or `[!example]` callout is redundant — its content is already covered either by another exercise (the same task on the same object, or a generalization that subsumes it) or by a review question (the underlying conceptual content). In that case, the right action is **not** to formulate a prompt; the callout should be eliminated from the vault.

When inventorying a block, every `[!exercise]` / `[!example]` callout has three possible fates:

- **Formulate a prompt** for it — the default when the callout has no question stated.
- **Lift into a more general in-text exercise** — rare; only when the callout's specific case is captured better by a broader exercise written from prose.
- **Eliminate as redundant** — when its content is already covered elsewhere.

A silently skipped callout — neither prompted nor flagged — looks like an oversight. The reader assumes one decision per callout, so an unmarked one causes a round trip ("did you miss this?"). Always name a fate.

In the chat deliverable, list eliminations as a short `### Eliminate` group at the end, after the formulated exercises:

> ### Eliminate
> - **2.1.X**: redundant with Exercise 2.1.Y (same row reduction on the same matrix).
> - **Y.Y.Z**: covered by review question N — no separate exercise needed.

One bullet per eliminated callout. The reason is brief but specific — name the other exercise or review question that supersedes it. Omit the `### Eliminate` heading entirely when there are no eliminations.

## Output format

Each exercise question is delivered in its own labeled block, *separate from any other exercise*. Do not combine multiple exercises into a single numbered list, even if there are only two — that makes them look like parts of the same problem. The header on each block tells me where the question belongs in the vault.

### Header convention

Two grouping conventions, used to distinguish the two sources.

**Never start a bold header with the word "Exercise".** Obsidian's `[!exercise]` callout renders an `Exercise N:` prefix automatically, and including the word "Exercise" in the header text produces an "Exercise N: Exercise ..." duplication that has to be erased by hand. Write only the title content.

**For exercises lifted from in-text examples** (no corresponding callout exists yet), gather them under a single section heading

`# In-text exercises`

placed once, above the entire group. Each individual exercise then gets its own bold sub-header of the form

`**<short descriptor>**`

where the descriptor is specific enough that the relevant prose can be found — usually the topic of the example, e.g. `**parametrization of the upper semicircle**`. Do **not** include the phrase "in-text example" or the word "Exercise" in the bold sub-header itself; the `# In-text exercises` section heading above the group already marks every question in the group as such, and repeating the phrase in each title creates clutter that has to be erased after OCR.

**For a labeled exercise callout missing a question**, gather these under their own section heading

`# Labeled Exercises`

placed once, above the group. Each individual exercise then gets its own bold sub-header carrying the callout's number and title (still no leading "Exercise") so the prompt can be matched to the right callout without hunting:

`**3: Cauchy's formula on a deformed contour**`

If a callout has only a number and no title, use just the number: `**3**`. If only a title and no number, use the title.

**Omit a section heading entirely if it has no entries.** If the block has no in-text examples to lift, do not include an empty `# In-text exercises` section. If the block has no labeled callouts needing prompts, do not include an empty `# Labeled Exercises` section. The two section headings exist to group entries, not as required scaffolding.

### Body

Below the header, write the question(s) as a numbered list.

**The prompt must be self-contained.** It must include all the information needed to solve the exercise — every specific object (matrices, systems of equations, integrals, functions, sequences, series), every parameter or condition, and every piece of context required to interpret the question. Do not write *"For each of the following matrices..."* or *"Solve the system above..."* without showing the matrices or the system. When the prompt is pasted into an `[!exercise]` callout in the vault, the surrounding text is not necessarily visible to the student, so anything the prompt depends on must be inlined.

Practical inlining formats:

- Matrices: KaTeX `\begin{bmatrix} ... \end{bmatrix}` blocks, separated by `\quad` when several appear together.
- Systems of equations: `\begin{aligned} ... \end{aligned}` (using `&=` to align).
- Integrals, functions, sequences, series: include the actual expression, not a name (e.g. *"Compute $\int_0^1 x^2 e^x \, dx$"* not *"Compute the integral above"*).
- Conditions and parameters (domains of variables, ranges of indices, hypotheses on functions): state them in the prompt.

The only acceptable reference to an unstated object is to one the student themselves has produced earlier in the same exercise — e.g. *"using the matrix from part (a)"*. Cross-references to an external object (a matrix in a different example, a result from a different theorem) must inline whatever they refer to.

If a single exercise has multiple parts (a), (b), (c), they go in the same block under one header — they are parts of one problem. If two exercises are independent — even if conceptually related — they each get their own header and their own block.

## Delivery rules carry over from review questions

The Mathpix OCR rules are the same:

- No triple-backtick code fences around the questions.
- KaTeX math delimiters: `$...$` for inline, `$$...$$` for display, with standard LaTeX commands inside.
- No `> [!exercise]` callout wrapper around the question. The header line is plain bold text. The callout is added by hand in the vault, or already exists when the destination is a labeled exercise.

## Worked example of formatted output

Suppose a section contains the semicircle parametrization in its motivation prose, the multiple-parametrizations-of-$[0,1]$ illustration also in prose, and a labeled `[!exercise]` callout titled "Exercise 2: A hypotrochoid in complex notation" whose body has only a solution, with no question stated. The output looks like this:

# In-text exercises

**parametrization of the upper semicircle**

1. Find a parametrization of the upper semicircle $y = \sqrt{1-x^2}$, $-1 \leq x \leq 1$, in complex notation. Identify the initial point, terminal point, and orientation.

**multiple parametrizations of $[0,1]$**

1. Verify that $\gamma_1(t) = t$ and $\gamma_2(t) = t^2$, both for $0 \leq t \leq 1$, parametrize the same directed segment $[0,1] \subset \mathbb{R}$. Identify the initial and terminal points of each, and describe in what sense the two parametrizations differ even though they represent the same curve.

# Labeled Exercises

**2: A hypotrochoid in complex notation**

1. Express the hypotrochoid given by $x(t) = a\cos t + b\cos\!\left(\tfrac{at}{2}\right)$, $y(t) = a\sin t - b\sin\!\left(\tfrac{at}{2}\right)$ as a single equation $\gamma(t)$ in complex notation.

Three exercises split across two sections. The first two sit under `# In-text exercises` because they were lifted from prose with no existing callout. The third sits under `# Labeled Exercises` because its bold sub-header carries the existing callout's identifying number and title (without the word "Exercise", which the callout renders automatically). If the block had only in-text examples and no labeled callouts needing prompts, the `# Labeled Exercises` section would be omitted entirely, and vice versa.
