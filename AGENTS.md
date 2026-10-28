# AGENTS.md

This file contains persistent instructions for work inside `/Users/gradyclopton/ObsidianVaults/complex_analysis`.

## Primary style reference

For exercise solutions and review answers, follow:

`/Users/gradyclopton/ObsidianVaults/complex_analysis/How to Write Exercise Solutions and Review Answers.md`

That document is the main house style guide for inserted mathematical solutions in this vault.

## Display-math discipline

Do not put single symbols, short values, isolated terms, short equalities, endpoint labels, radii, centers, or one-step facts in display math unless there is a genuine visual reason.

Keep items such as `3`, `-1+i`, `R=4`, `z_1=1+i`, `\gamma(0)=1+i`, `\gamma(1)=4-2i`, and similar short expressions inline by default.

Use display math only for:

1. full formulas that are being presented as formulas,
2. multi-step derivations or aligned computations,
3. substitutions that are substantial enough to benefit from being displayed,
4. equations that genuinely need visual separation for readability.

“Show every step” does not mean “put every step in display mode.” It means write every logical and algebraic step explicitly while still preserving natural prose.

When revising or inserting math exposition, prefer prose with inline math unless a displayed line materially improves readability.

## Reusing earlier results

When a later solution uses a result already derived earlier, do not use brittle references such as “by Exercise 12(b)” or “from Problem 7 above.”

Instead, state the result itself locally at the point of use, usually as a short equation callout. In the simplest cases only, a brief inline note such as `u=...`, `du=...`, `v=...`, or `dv=...` is acceptable.

Even when reusing a previously derived formula, still show the substitutions into that formula and any remaining algebraic manipulations.

## Insertion safety

Never insert a solution unless there is an explicit `CODEX-INSERT-...` marker at the target location.

If the user asks for a solution and there is no insertion marker, stop and remind the user to add one before making any edit.

Do not infer a blank region as an insertion point, and do not overwrite surrounding text merely because a solution slot seems obvious. Replace only the exact marker.

## Code block folding

Always add a `title:"..."` attribute to fenced code blocks so they can be folded in the note interface.

An empty title such as `title:""` is acceptable when there is no useful label to add. If a descriptive title would help, use one.

## Plot separation

When adding plots to multi-part exercises, do not combine multiple problems or subproblems into one shared figure or one shared Mathematica/Python plotting block unless the user explicitly asks for that. Each plotted problem or subproblem should have its own embedded image above its own Mathematica and Python code blocks.
