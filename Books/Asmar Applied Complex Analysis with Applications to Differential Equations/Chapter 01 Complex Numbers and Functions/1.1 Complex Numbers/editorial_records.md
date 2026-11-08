
# Editorial records

Reading note: 1.1 Complex Numbers.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Callout 0: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!definition] Imaginary Unit
> The imaginary unit $i$ satisfies $i^2=-1$; the principal square root of $-1$ is denoted by $i$.
````
### After

````text
> [!definition] Imaginary Unit
> $$
> i=\sqrt{-1}, \text { or equivalently, } i^{2}=-1
> $$
````

## 2. Callout 1: restore source title/wording without book numbering; retain actual corrections and necessary source context.

### Before

````text
> [!definition] Complex Numbers and Their Real and Imaginary Parts
> A **complex number** $z$ is an expression of the form $z=a+i b$, where $a$ and $b$ are **real numbers** and $i^{2}=-1$. The number $a$ is called the **real part of $z$** and denoted Re $z$. The number $b$ is called the **imaginary part of $z$** and denoted $\operatorname{Im} z$.
````
### After

````text
> [!definition] Definition of Complex Numbers
> A **complex number** $z$ is an expression of the form $z=a+i b$, where $a$ and $b$ are **real numbers** and $i^{2}=-1$. The number $a$ is called the **real part of $z$** and denoted Re $z$. The number $b$ is called the **imaginary part of $z$** and denoted $\operatorname{Im} z$.
````

## Source-to-current comparison

Source: /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 01 Complex Numbers and Functions/1.1 Complex Numbers.md

This exact comparison preserves the full change evidence, including formatting, OCR corrections, restored source wording, and required standalone context. The entries above explain the recovery edits. The comparison is not a claim that every difference is a correction; component serialization, callout wrapping, and printed labels outside callouts are formatting.

`````diff
--- /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 01 Complex Numbers and Functions/1.1 Complex Numbers.md
+++ /Users/gradyclopton/ObsidianVaults/complex_analysis/Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 01 Complex Numbers and Functions/1.1 Complex Numbers.md
@@ -1,3 +1,4 @@
+
 **Topics to Review**
 This chapter requires basic knowledge from calculus. Most functions that you will encounter here are named after the functions that they generalize from calculus. For example, the complex exponential $e^{z}$ generalizes the real exponential function $e^{x}$. The same is true for many other complex functions such as $\cos z$, $\sin z, \tan z, \log z$. Thus a good knowledge of these elementary functions and their properties is helpful in studying their complex counterparts.
 
@@ -161,21 +162,23 @@
 
 Two centuries later, the Swiss mathematician Leonhard Euler (17071783) introduced the symbol $i$ by setting
 
+<!-- Source label: Imaginary Unit -->
 > [!definition] Imaginary Unit
 > $$
 > i=\sqrt{-1}, \text { or equivalently, } i^{2}=-1
 > $$
-> 
 
 Though Euler used numbers of the form $a+i b$ routinely in computations, he was skeptical about their meaning and referred to them as imaginary numbers. It took the authority of the great German mathematician Karl Friedrich Gauss (1777-1855) to definitively recognize the importance of these numbers, introducing for the first time the term that we now use-complex numbers.
 
 
 
+<!-- Source label: Definition of Complex Numbers -->
 > [!definition] Definition of Complex Numbers
 > A **complex number** $z$ is an expression of the form $z=a+i b$, where $a$ and $b$ are **real numbers** and $i^{2}=-1$. The number $a$ is called the **real part of $z$** and denoted Re $z$. The number $b$ is called the **imaginary part of $z$** and denoted $\operatorname{Im} z$.
 
 
 
+<!-- Source label: Equality of Complex Numbers -->
 > [!property] Equality of Complex Numbers
 > Two complex numbers are equal if they have the same real and imaginary parts. That is, $z_{1}=z_{2}$ if and only if $\operatorname{Re} z_{1}=\operatorname{Re} z_{2}$ and $\operatorname{Im} z_{1}=\operatorname{Im} z_{2}$.
 

`````
