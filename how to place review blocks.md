# How to Place Review Blocks

## Purpose

A review block is a `[!review]` callout that holds the review questions for a block of content. Deciding where review blocks go is a step that happens *before* writing the questions themselves. The goal is to carve a section into coherent content blocks and place one review callout at the top of each, so that a student reading top-to-bottom always encounters the review questions for a piece of content before the content itself.

## Core principle

Every review block sits at the beginning of the block of content it covers. A review block is not a summary of what the student just read; it is a preview of the material that follows it in the note. If a question in a review block cannot be answered from the content that comes after the block and before the next review block, either the block is wrongly placed or the question belongs elsewhere.

## Step 1: Map the section into content blocks

Read through the section and identify the natural content blocks. A content block is a single coherent piece of mathematical development — typically one theorem (or a tight family of closely related theorems) together with its motivation, proof, and immediate applications.

Block boundaries usually sit at one of the following signals:

- A major new theorem is introduced, and its motivation is independent of the preceding theorem's motivation.
- The text pivots from "here is the formula and how to compute with it" to "here are the theoretical consequences."
- A basic result is extended to a generalized version, and that generalization carries its own derivation and its own examples.
- A transitional sentence introduces the next major idea — phrases like "X has many important applications to Y," "Two observations concerning X deserve mentioning," or "The following is a converse of sorts to X."
- The section itself has an internal sub-heading or a visibly different tone (for example, an appendix block at the end).

Do not mistake "a new theorem appears" for "a new block starts." A corollary that is a direct consequence of the preceding theorem usually lives in the *same* content block as that theorem. A new block requires a genuine shift in subject or character, not just the next numbered result.

## Step 2: Decide how many review blocks the section needs

One review block is enough when the whole section covers a single theorem or a tightly unified family of results, all of the same character (for example, all computational or all theoretical), and a natural review of the material comes out to roughly four to seven questions.

Split into multiple review blocks when any of the following is true:

- A single review over the whole section would balloon past eight or nine questions.
- The content shifts in character across the section — computational to theoretical, basic to generalized, concrete to abstract.
- Two or more theorems are developed with independent motivations rather than as a connected chain.
- The section contains material that could stand alone as its own mini-section (an appendix, a separate proof of a separately-stated result, a follow-up block of corollaries with their own flavor).

The target density is around four to seven questions per review block. A block whose natural review would be ten or more questions is a signal that the block should be split, not that the questions should be crammed together.

## Step 3: Find the fault line, not the halfway point

Never divide a section by line count, word count, or "roughly in the middle." Divisions must follow the conceptual structure of the text. The right place to split is wherever the text itself pivots — the sentence that introduces the next big idea, the paragraph just before a new theorem that opens a fresh topic, the pivot from "what this is" to "what this is good for," or the pivot from proof machinery to downstream consequences.

Place the review block on the line immediately before the first content of the new block. That usually means just above the transitional sentence, not buried in the closing remarks of the previous block.

## Step 4: Record the placement unambiguously

When proposing a placement, always give two things: the line number in the current file, and the exact opening phrase of the content that starts the new block. Line numbers drift as the file is edited, but an opening phrase is stable.

For example: "Place Review 2 at line 161. Section starts with: *Two observations concerning Cauchy's formula (1) deserve mentioning.*"

Prefer the actual opening words of the paragraph as the anchor. Avoid anchors like "just before Theorem 2" — theorem numbers can shift, and the phrasing is less precise about whether the review goes above the statement, above its motivation, or above its proof.

## Step 5: Sanity-check the divisions

Before committing to a division, verify each block:

- Every question in its review can be answered using only the material between this review block and the next one.
- Every theorem, corollary, and in-text example inside the block is covered by at least one question in the review (unless the item is a pure exercise that belongs in the Exercises section instead).
- The block is neither too short to be worth reviewing nor too long to be reviewed with four to seven questions.
- The first review block in the section begins at the top of the section, not after the first theorem. The opening material — motivation, recalls, definitions — belongs under the first review.

If any check fails, redraw the block boundaries.

## Worked example: 3.6 Cauchy's Integral Formula

The section mixes three kinds of material: the basic Cauchy integral formula with direct computational examples, the generalized formula for higher derivatives with its own computational examples, and a block of theoretical consequences (Corollary 1 and 2, Morera's theorem, the removable-singularity construction). This is the canonical three-block situation.

Review 1 goes at the very top of the section and covers Theorem 1 (basic Cauchy integral formula), the extension giving zero when $z$ is outside $C$, the combined piecewise formula, and the two computational examples that apply the formula directly or via multiply connected regions.

Review 2 goes at the line that begins *"Two observations concerning Cauchy's formula (1) deserve mentioning."* This is the pivot from the basic formula to the bootstrap that produces derivatives of all orders. The block covers the two observations, the inductive differentiation-under-the-integral derivation, Theorem 2 (Generalized Cauchy Integral Formula), and its two computational examples.

Review 3 goes at the line that begins *"Cauchy's formula has many important applications to analytic functions, which in turn will be used to derive properties of harmonic functions..."* This is the pivot from computation to theoretical consequences. The block covers Corollary 1, Corollary 2, Morera's theorem, Theorem 4 (the removable-singularity builder), and the extension of $\sin z / z$ to an entire function.

Merging Reviews 1 and 2 would wrongly combine "what the basic formula is" with "why we can differentiate under the integral sign arbitrarily often" — two genuinely separate motivations. Merging Reviews 2 and 3 would wrongly combine computational applications with purely theoretical consequences. The three-way split follows the fault lines the text itself draws.

## Common mistakes to avoid

Placing a review block in the middle of a content block rather than at its start. Reviews are previews, not summaries.

Writing a single review block for an entire long section. If the natural review runs past eight or nine questions, the section has more than one content block and should be split.

Dividing on line count rather than on conceptual fault lines. Blocks of unequal length are fine if they follow the structure of the material.

Placing a review block between a theorem statement and its proof. The review belongs before the theorem, because a well-written review poses the question the theorem answers — putting it after the statement defeats the purpose.

Using a unique numbered reference (like "before Theorem 2") as the placement anchor. Prefer the actual opening words of the paragraph, since those survive renumbering and edits.

Forgetting that an in-text example with no callout still needs a question in whichever review block it lives under. When you draw the block boundaries, make sure every piece of mathematical content — including buried examples in prose — falls under some review.
