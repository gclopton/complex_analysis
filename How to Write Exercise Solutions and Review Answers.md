# How to Write Exercise Solutions and Review Answers

This note records the house style for writing solutions to exercises and answers to review blocks in this vault. The purpose is not merely to produce correct mathematics. The purpose is to write solutions that are pedagogically useful, visually consistent across the notes, and safe to insert into the source files without disturbing surrounding material.

The central principle is simple: never write a compressed answer when the mathematical value of the solution lies in seeing the argument unfold. A correct answer that skips the manipulations, substitutions, branch choices, or sign checks is not enough for this project.

## Insertion discipline

When inserting a solution into an existing note, replace only the exact `CODEX-INSERT-...` target. Do not rewrite surrounding material, do not "clean up" nearby text unless there is a local rendering error that must be fixed, and do not move headings or figures around the target unless the user explicitly asks for restructuring.

If the file already contains established notation, terminology, or section structure, preserve it. Do not introduce a new naming scheme, a new organizational pattern, or a new notational convention merely because it is mathematically equivalent.

## The basic writing standard

Solutions should read like natural mathematical exposition, not like terse answer keys and not like AI-produced summaries. The prose should flow normally, but the mathematics should still be explicit. Do not announce that you are "using derivation mode" inside the solution. The writing should simply do it.

Condensed answers are not allowed for exercises in these notes, even when the problem is long or has many parts. If the problem asks for verification, show the verification. If the problem asks for a formula, show how it is obtained. If the problem asks for a plot, derive the plotted curves and then include the plotting material.

When a problem naturally breaks into stages, the prose may explain what is being done, but the explanation should serve the mathematics rather than replace it. Avoid vague transitions such as "using algebra," "after simplification," "it follows," or "one finds" when the omitted work is exactly what the student should see.

## Header format for exercises

For a standard exercise solution block, begin with

```text
##### solution
```

If the exercise has only one question and no labeled subparts, write the solution directly under `##### solution`.

If the exercise has multiple numbered parts, then after `##### solution` use separate fifth-level headers of the form

```text
##### problem 1
##### problem 2
##### problem 3
```

If the exercise is already labeled by the textbook with a specific problem number, preserve that number:

```text
##### problem 17
##### problem 31
```

If the exercise has lettered subparts, preserve those labels exactly:

```text
##### problem 17(a)
##### problem 17(b)
##### problem 23(a)
##### problem 23(b)
```

If a multi-part exercise contains both an exercise number and separately numbered internal problems, mirror the visible structure of the textbook rather than inventing a new one.

Do not collapse several parts into one header. Do not answer several parts in a single compressed paragraph. If the source problem is broken into pieces, the solution block should visibly reflect that structure.

## Header format for review answers

For a review block with a single question, use

```text
##### solution
```

and answer the review question directly underneath it.

For a review block with multiple numbered prompts, use

```text
##### solution
##### problem 1
##### problem 2
...
```

If the review itself is lettered rather than numbered, preserve the lettering in the headers. The structure of the answer should mirror the structure of the review prompt.

A review answer should still be a real explanation. It may be shorter than a full exercise solution, but it must not become a one-line conclusion when the value lies in the reasoning.

## What derivation-style writing actually means here

Whenever the mathematics depends on algebraic manipulation, symbolic simplification, differentiation, substitution, factoring, cancellation, or comparison of branches or signs, write the steps as an explicit chain rather than jumping from the beginning to the end.

This means that if you start with an expression such as

$$
\sin^2 x \cosh^2 y+\cos^2 x \sinh^2 y,
$$

you should not jump immediately to

$$
\sin^2 x+\sinh^2 y.
$$

You should write the intermediate expansions:

$$
\sin^2 x \cosh^2 y+\cos^2 x \sinh^2 y
=
\sin^2 x(1+\sinh^2 y)+\cos^2 x \sinh^2 y
$$

$$
=
\sin^2 x+\sin^2 x \sinh^2 y+\cos^2 x \sinh^2 y
$$

$$
=
\sin^2 x+(\sin^2 x+\cos^2 x)\sinh^2 y
$$

$$
=
\sin^2 x+\sinh^2 y.
$$

The same standard applies everywhere else. If you use a trigonometric identity, first isolate the terms to which it applies. If you combine fractions, show the common denominator. If you apply the quadratic formula, simplify the discriminant in stages. If you reject a branch, show the sign comparison that rules it out. If you invoke linearity of Laplace's equation or of a sum of harmonic functions, write the sum and show the operator passing through it.

The general rule is this: if a student reading the solution might reasonably ask "wait, how did that become this?" then the missing line belongs in the solution.

## Places where compression is especially harmful

Compression is especially damaging in the following situations.

First, when verifying that a function is harmonic. Product-rule, quotient-rule, and chain-rule steps should be written out, especially when the cancellations are the point.

Second, when deriving level curves, isotherms, or heat-flow curves. These problems often hide the real mathematical work inside substitutions and simplifications. Do not skip the route from the original temperature function to the final geometric equation.

Third, when pulling back a known curve under a conformal map. The substitutions for the real and imaginary parts of the image variable should be shown explicitly, followed by the algebra needed to obtain the final equation in the original coordinates.

Fourth, when solving for constants from boundary conditions. Show the substitutions into the general candidate solution and solve the resulting system line by line.

Fifth, when justifying approximation schemes, superposition arguments, and Riemann-sum limits. Do not write "by linearity" or "this approaches the integral" as if that alone were enough. Show the terms being added, show the operator acting term-by-term, and show how the discrete expression matches the form of the limiting integral.

## What may be compressed

Very little should be compressed in these solution blocks, but a few things may be kept concise when they are not carrying the mathematical burden.

Routine prose transitions may stay short. Repetition of an already-established notational definition may be omitted if the symbol has just been introduced and there is no ambiguity. A standard theorem may be cited without reproving it, provided the solution then shows clearly how the theorem applies in the present setting.

Even in those cases, do not compress the actual application of the theorem if that application itself requires computation or a nontrivial check.

## Reusing previously derived results

When a later exercise genuinely depends on a result that has already been derived, it is usually better to reuse that result than to rederive it from scratch. This should be done sparingly. The point is to avoid useless repetition, not to hide new work.

Do not write brittle references such as "by Exercise 12(b)" or "from Problem 7 above." The numbering in these notes may change later, and such references are easy to break.

Instead, when a previously derived result is being used, state the result itself at the point of use. There are three acceptable ways to do this.

First, in the simplest cases only, place a short inline comment directly beside the relevant line of an equality chain. This is appropriate for tiny substitutions or one-line facts such as a change of variables, a branch choice, a previously derived one-line identity, or the setup data for standard maneuvers such as $u$-substitution or integration by parts. Typical acceptable inline notes are things like $u=\cdots$, $du=\cdots$, $v=\cdots$, $dv=\cdots$, or a one-line formula being inserted into the current chain.

Second, and more commonly, insert a short equation callout containing the formula being applied. This is the preferred method when the reused result is more than a tiny substitution but still short enough to quote cleanly.

Third, if the reused result is already a named theorem whose statement is standard and stable, it may be cited by name, but the present solution must still show the substitutions into that theorem and any algebra that follows from applying it.

In every case, once the formula is stated, the current solution must still show the actual use of that formula. That means showing substitutions into the reused result and then showing any remaining algebraic or analytic manipulations. Do not replace the application with phrases such as "applying the previous formula" or "using the identity above" when the substituted form still requires work.

The governing rule is simple: do not rederive old work unnecessarily, but do make the dependency explicit in the local solution so the argument still reads cleanly even if exercise numbering later changes.

## Tone and presentation

Write the solution as mathematics, not as meta-commentary about the solution. Do not say "now I will use derivation mode," "here is the compressed version," or "I will not skip steps." Just write the steps.

Do not put mathematics into code blocks when ordinary KaTeX display math is what is wanted. Use ordinary display equations and aligned derivations so the browser can render them normally.

Avoid turning a mathematical solution into a bullet-list outline unless the problem itself is inherently procedural. In most cases, the right form is ordinary prose interleaved with displayed mathematics.

## Plots and computer evaluation

If a problem asks for a plot, use Mathematica for the plot. The mathematical derivation of the plotted curves should appear in the solution before the Mathematica code block.

If a static rendered image is being added to the notes, place the image in the appropriate `images` directory, embed the image in the solution block near the discussion it illustrates, and place the Python code that generated the static image below the Mathematica block when that static rendering is part of the workflow.

If a multi-part exercise has several plotted subproblems, do not combine those subproblems into one shared composite figure or one shared plotting-code block unless the user explicitly asks for that layout. Each plotted problem or subproblem should have its own independently embedded figure, its own Mathematica code block, and its own Python code block. The embedded image should appear above the corresponding Mathematica and Python blocks for that same problem or subproblem.

If any numerical value is obtained by computer evaluation, include the Python code used to produce it in the solution block. Do not report computer-generated sample values without also including the code that generated them.

If a plot represents physical flow, such as heat-flow curves, include arrows when the physical direction matters. Isotherms do not need arrows, but flow lines usually do if the figure is meant to convey direction rather than mere orthogonality.

## Reviews versus exercises

A review answer may be shorter than an exercise solution, but it is not allowed to become a mere slogan. If the review asks for a conceptual explanation, answer in full sentences and support the explanation with the relevant equations when appropriate.

An exercise solution is expected to be fuller than a review answer. In particular, multi-part exercises should be written part-by-part, and any nontrivial algebra or calculus in those parts should be displayed rather than hidden behind summary phrases.

## Final checklist

Before considering a solution complete, check the following.

The inserted text replaces only the intended target marker.

The headers match the established format of the vault.

The structure of the solution mirrors the structure of the problem.

No crucial algebraic, analytic, or geometric step has been compressed into a phrase such as "after simplification" or "it follows."

Any numerical computation includes the Python code used to obtain it.

Any requested plot includes Mathematica code, and the mathematical derivation of the plotted curves appears before the plotting code.

Each plotted problem or subproblem has its own figure and its own Mathematica/Python plotting blocks, unless the user explicitly asked for a combined figure.

The prose reads naturally and mathematically, without announcing the method as a mode.

If the solution still feels like an answer key rather than a worked solution, it is not finished.

# Example of a Good Solution

The following example uses a problem of the same type that came up repeatedly in the recent conformal-mapping exercises. The point of the example is to show the difference between a mathematically correct but overly compressed answer and the kind of worked solution this vault actually requires.

## Problem Statement

In the $w$-plane, suppose the isotherm corresponding to the temperature $T$ is

$$
\xi^2+\left(\eta-\cot\frac{\pi T}{100}\right)^2=\csc^2\frac{\pi T}{100},
\qquad 0<T<100,
$$

where

$$
w=\xi+i\eta.
$$

Under the conformal map

$$
w=z^2,
\qquad z=x+iy,
$$

determine the equation of the isotherms in the $z$-plane.

## Compressed Answer

Since

$$
w=z^2=(x+iy)^2=x^2-y^2+i(2xy),
$$

we have

$$
\xi=x^2-y^2,
\qquad
\eta=2xy.
$$

Substituting into the isotherm equation gives

$$
(x^2-y^2)^2+\left(2xy-\cot\frac{\pi T}{100}\right)^2=\csc^2\frac{\pi T}{100}.
$$

Expanding and simplifying,

$$
(x^2+y^2)^2-4xy\cot\frac{\pi T}{100}=1.
$$

So the isotherms are

$$
\boxed{
(x^2+y^2)^2-4xy\cot\frac{\pi T}{100}=1.
}
$$

This answer is too compressed for the house style because the real work is hidden inside the phrase "expanding and simplifying."

## Properly Written Solution

Under the map

$$
w=z^2,
\qquad z=x+iy,
$$

we compute

$$
w=(x+iy)^2=x^2+2ixy+i^2y^2=x^2+2ixy-y^2.
$$

Therefore

$$
w=(x^2-y^2)+i(2xy).
$$

Comparing this with

$$
w=\xi+i\eta,
$$

we obtain

$$
\xi=x^2-y^2,
\qquad
\eta=2xy.
$$

Now substitute these expressions into the isotherm equation in the $w$-plane:

$$
\xi^2+\left(\eta-\cot\frac{\pi T}{100}\right)^2=\csc^2\frac{\pi T}{100}.
$$

This gives

$$
(x^2-y^2)^2+\left(2xy-\cot\frac{\pi T}{100}\right)^2=\csc^2\frac{\pi T}{100}.
$$

Now expand each square explicitly:

$$
\begin{aligned}
(x^2-y^2)^2+\left(2xy-\cot\frac{\pi T}{100}\right)^2
&=
\left(x^4-2x^2y^2+y^4\right)
+\left(4x^2y^2-4xy\cot\frac{\pi T}{100}+\cot^2\frac{\pi T}{100}\right)\\
&=
x^4-2x^2y^2+y^4+4x^2y^2-4xy\cot\frac{\pi T}{100}+\cot^2\frac{\pi T}{100}\\
&=
x^4+2x^2y^2+y^4-4xy\cot\frac{\pi T}{100}+\cot^2\frac{\pi T}{100}\\
&=
\left(x^2+y^2\right)^2-4xy\cot\frac{\pi T}{100}+\cot^2\frac{\pi T}{100}.
\end{aligned}
$$

So the equation becomes

$$
\left(x^2+y^2\right)^2-4xy\cot\frac{\pi T}{100}+\cot^2\frac{\pi T}{100}
=\csc^2\frac{\pi T}{100}.
$$

Subtract

$$
\cot^2\frac{\pi T}{100}
$$

from both sides:

$$
\left(x^2+y^2\right)^2-4xy\cot\frac{\pi T}{100}
=
\csc^2\frac{\pi T}{100}-\cot^2\frac{\pi T}{100}.
$$

Now use the identity

$$
\csc^2\theta-\cot^2\theta=1.
$$

Therefore

$$
\left(x^2+y^2\right)^2-4xy\cot\frac{\pi T}{100}=1.
$$

Hence the isotherms in the $z$-plane are

$$
\boxed{
\left(x^2+y^2\right)^2-4xy\cot\frac{\pi T}{100}=1,
\qquad 0<T<100.
}
$$

This is the standard to aim for. The reader can see the substitution, the expansion, the regrouping, the identity, and the final conclusion without having to guess what happened between the first displayed equation and the last one.
