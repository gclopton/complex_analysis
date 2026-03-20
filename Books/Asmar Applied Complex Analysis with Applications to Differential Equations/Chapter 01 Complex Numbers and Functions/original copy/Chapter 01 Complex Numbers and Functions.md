Topics to Review
This chapter requires basic knowledge from calculus. Most functions that you will encounter here are named after the functions that they generalize from calculus. For example, the complex exponential $e^{z}$ generalizes the real exponential function $e^{x}$. The same is true for many other complex functions such as $\cos z$, $\sin z, \tan z, \log z$. Thus a good knowledge of these elementary functions and their properties is helpful in studying their complex counterparts.

## Looking Ahead

The results of this chapter will be used throughout the rest of the book. A good knowledge of the properties of complex numbers, as presented in Sections 1.11.3 is essential to all that follows. In particular, you should familiarize yourself with the triangle inequality and understand its meaning and geometric interpretation. Section 1.5 introduces the most important function in complex analysis: the complex exponential function $e^{z}$. Its relationship to trigonometric functions, as illustrated by Euler's identity

$$
e^{i \theta}=\cos \theta+i \sin \theta
$$

makes complex analysis a powerful tool for studying Fourier series, solving differential equations, and important problems in other areas of applied mathematics. Mapping properties of complex functions are presented in Section, 1.4 and discussed with each function as it is introduced. These properties will be needed in solving boundary value problems, starting in Section 2.5.

## 1

## COMPLEX NUMBERS AND FUNCTIONS

Dismissing mental tortures, and multiplying $5+\sqrt{-15}$ by $5-\sqrt{-15}$, we obtain $25-(-15)$. Therefore the product is $40 \ldots$ and thus far does arithmetical subtlety go, of which this, the extreme, is, as I have said, so subtle that it is useless.
-Girolamo Cardan
[First explicit use of complex numbers, which appeared around 1545 in Cardan's solution of the problem of finding two numbers whose sum is 10 and whose product is 40 .]

This chapter starts with the early discovery of complex numbers and their role in the solution of algebraic equations. From the expression $z=x+i y$, we will represent complex numbers as points or vectors ( $x, y$ ) in the plane and take advantage of our geometric intuition in working with complex numbers. We will see how complex numbers can be added and subtracted much like we add and subtract vectors in two dimensions. We also have a notion of distance between complex numbers that satisfies the familiar triangle inequality.

Complex numbers also have a polar form, based on polar coordinates $(r, \theta)$. This representation enables us to give a very concrete geometric meaning to multiplication and division of complex numbers.

The last four sections of this chapter are devoted to the study of complex-valued functions of a complex variable. The most important of these functions is the complex exponential $e^{z}$. We will introduce it in Section 1.5 and use it in Sections 1.6 and 1.7 to define the trigonometric and logarithmic functions. Since we cannot plot the graph of a complex-valued function (this would require four dimensions), we will visualize these functions as mappings from one complex plane, the $z$-plane, into another plane, the $w$-plane. Mapping properties will be explored in this chapter and will be used in later sections to solve interesting partial differential equations.

Every once in a while an application is presented to remind us that complex numbers are studied for the purpose of solving realworld problems. The applications in this chapter include finding real roots of algebraic equations, simplifying the computation of certain integrals, and finding the solutions of ordinary differential equations.

### 1.1 Complex Numbers

Complex numbers were discovered in the sixteenth century for the purpose of solving algebraic equations that do not have real solutions. As you know, the equation

$$
x^{2}+1=0
$$

has no real roots, because there is no real number $x$ such that $x^{2}=-1$; or equivalently, we cannot take the square root of -1 . The Italian mathematician Girolamo Cardano (1501-1576), better known as Cardan, stumbled upon and used the square roots of negative numbers in his work. While Cardan was reluctant to accept these "imaginary" numbers, he did realize their role in solving algebraic equations.

Two centuries later, the Swiss mathematician Leonhard Euler (17071783) introduced the symbol $i$ by setting

$$
i=\sqrt{-1}, \text { or equivalently, } i^{2}=-1
$$

Though Euler used numbers of the form $a+i b$ routinely in computations, he was skeptical about their meaning and referred to them as imaginary numbers. It took the authority of the great German mathematician Karl Friedrich Gauss (1777-1855) to definitively recognize the importance of these numbers, introducing for the first time the term that we now use-complex numbers.

DEFINITION OF COMPLEX NUMBERS

A complex number $z$ is an expression of the form $z=a+i b$, where $a$ and $b$ are real numbers and $i^{2}=-1$. The number $a$ is called the real part of $z$ and denoted Re $z$. The number $b$ is called the imaginary part of $z$ and denoted $\operatorname{Im} z$.
Two complex numbers are equal if they have the same real and imaginary parts. That is, $z_{1}=z_{2}$ if and only if $\operatorname{Re} z_{1}=\operatorname{Re} z_{2}$ and $\operatorname{Im} z_{1}=\operatorname{Im} z_{2}$.
For example, if $z=3+i$ then

$$
\operatorname{Re} z=\operatorname{Re}(3+i)=3 \quad \text { and } \quad \operatorname{Im} z=\operatorname{Im}(3+i)=1
$$

Note that the imaginary part of a complex number is itself a real number. The imaginary part of $a+i b$ is just $b$, not $i b$.

We do not distinguish between the forms $a+i b$ and $a+b i$; for example, $-2+i 4$ and $-2+4 i$ are the same complex number. When a complex number has a zero imaginary part like $a+i 0$ we simply write it as $a$. These are known as purely real numbers and are just new interpretations of real numbers. Sometimes we shall even abuse the language and say that $z$ is "real" when $z$ has a zero imaginary part. When a complex number has a zero real part like $0+i b$ we simply write it as $i b$. These numbers are called purely imaginary.

For example, $i, 2 i, \pi i,-\frac{2}{3} i$ are all purely imaginary numbers. The unique complex number with zero real and imaginary parts will be denoted simply as 0 , instead of $0+0 i$.

## Algebraic Properties

We define addition among complex numbers as if $i$ obeyed the same basic algebraic relations that real numbers do. To add complex numbers, add their real and imaginary parts:

$$
(a+i b)+(c+i d)=(a+c)+i(b+d)
$$

For example, $(3+2 i)+(-1-4 i)=(3-1)+i(2-4)=2-2 i$.
Subtraction is done the same way:

$$
(a+i b)-(c+i d)=(a-c)+i(b-d) .
$$

For example, $(3+2 i)-(-1+4 i)=(3-(-1))+i(2-4)=4-2 i$.
Multiplication is defined by treating a complex number $a+i b$ as a binomial expression and using the identity $i^{2}=-1$. So

$$
\begin{aligned}
(a+i b)(c+i d) & =a c+i a d+i b c+i^{2} b d \\
& =(a c-b d)+i(a d+b c)
\end{aligned}
$$

For example, $(-1+i)(2+i)=-2-i+2 i+i^{2}=-3+i$. Also, $-i(4+4 i)= -4 i-4(i)^{2}=-4 i+4=4-4 i$.

For $z=a+i b$ we define the complex conjugate $\bar{z}$ of $z$ by

$$
\bar{z}=\overline{a+i b}=a-i b .
$$

Conjugation changes the sign of the imaginary part of a complex number but leaves the real part the same. Thus

$$
\operatorname{Re} \bar{z}=\operatorname{Re} z \quad \text { and } \quad \operatorname{Im} \bar{z}=-\operatorname{Im} z .
$$

For any complex number $z$, we have

$$
z \bar{z}=(a+i b)(a-i b)=a^{2}+b^{2} \geq 0 .
$$

Hence $z \bar{z}$ is always a nonnegative real number. We can now introduce division and compute the quotient of two complex numbers $\frac{a+i b}{c+i d}$, where $c+i d \neq 0$. First observe that

$$
c+i d \neq 0 \Leftrightarrow c-i d \neq 0 \Leftrightarrow c^{2}+d^{2} \neq 0 .
$$

Now

$$
\begin{aligned}
\frac{a+i b}{c+i d} & =\frac{(a+i b)(c-i d)}{(c+i d)(c-i d)} \quad[\text { multiply and divide by } c-i d \neq 0] \\
& =\frac{(a c+b d)+(b c-a d) i}{c^{2}+d^{2}} \\
& =\frac{a c+b d}{c^{2}+d^{2}}+i \frac{b c-a d}{c^{2}+d^{2}}
\end{aligned}
$$

As an illustration, if $z=x+i y \neq 0$, then from (1)

$$
\frac{1}{z}=\frac{x}{x^{2}+y^{2}}-i \frac{y}{x^{2}+y^{2}}
$$

In particular, if $z=i$, then, since $x=0$ and $y=1$,

$$
\frac{1}{i}=-i .
$$

We can now define integer powers of complex numbers: $z^{1}=z, z^{2}=z \cdot z$, and for any positive integer $n$,

$$
z^{n}=\overbrace{z \cdot z \cdot \cdots z}^{n \text { of these }} .
$$

For nonzero $z, z^{0}$ is defined to be 1 . Also, $z^{-n}=\frac{1}{z^{n}}$. As a consequence of the definition, we have the familiar results for exponents such as $z^{m} z^{n}=z^{m+n}$, $\left(z^{m}\right)^{n}=z^{m n}$, and $(z w)^{m}=z^{m} w^{m}$.

## EXAMPLE 1 Basic operations

Express the given complex number in the form $a+i b$, where $a$ and $b$ are real numbers.
(a) $(2-7 i)+\overline{(3+i)}$.
(b) $(4-2 i)\left(\frac{3}{2}-\frac{7}{i}\right)$.
(c) $i^{n}, \quad n=0,1,2, \ldots$.
(d) $\frac{2-7 i}{\pi-i}$.
(e) $\frac{i}{7-i}$.
(f) $\frac{2+i}{3 i}$.

Solution (a) We have

$$
(2-7 i)+\overline{(3+i)}=(2-7 i)+(3-i)=5-8 i
$$

(b) Using (3), we have $\frac{3}{2}-\frac{7}{i}=\frac{3}{2}+7 i$, and so

$$
(4-2 i)\left(\frac{3}{2}-\frac{7}{i}\right)=(4-2 i)\left(\frac{3}{2}+7 i\right)=6+28 i-3 i-14 i^{2}=20+25 i
$$

(c) From the identities

$$
i^{0}=1, \quad i^{1}=i, \quad i^{2}=-1, \quad i^{3}=-i, \quad i^{4}=1, \quad i^{5}=i, \quad \ldots
$$

we conclude that for $n=0,1,2, \ldots$

$$
i^{n}= \begin{cases}1 & \text { if } n=4 k \\ i & \text { if } n=4 k+1 \\ -1 & \text { if } n=4 k+2 \\ -i & \text { if } n=4 k+3\end{cases}
$$

where $k=0,1,2, \ldots$. We say that the sequence of complex numbers $\left\{i^{n}\right\}$ is periodic with period 4 , since it repeats every four terms.
(d) In computing quotients, instead of appealing to (1), just remember to multiply and divide by the conjugate of the denominator to make it real. So

$$
\frac{2-7 i}{\pi-i}=\frac{(2-7 i)}{(\pi-i)} \frac{(\pi+i)}{(\pi+i)}=\frac{(2 \pi+7)+i(2-7 \pi)}{\left(\pi^{2}+1\right)}=\frac{7+2 \pi}{\pi^{2}+1}+i \frac{2-7 \pi}{\pi^{2}+1}
$$

For (e), we have

$$
\frac{i}{7-i}=\frac{i}{(7-i)} \frac{(7+i)}{(7+i)}=\frac{-1}{50}+i \frac{7}{50}
$$

For (f), we could multiply and divide by the conjugate of the denominator, $-3 i$, but $-i$ will do the trick:

$$
\frac{2+i}{3 i}=\frac{(2+i)}{(3 i)} \frac{(-i)}{(-i)}=\frac{1-2 i}{3}=\frac{1}{3}-i \frac{2}{3}
$$

Several useful properties of complex numbers can be established by manipulating definitions. The proofs are not difficult in some cases. However, it is important to write out the proof formally, recognizing those statements that are definitions or hypotheses and recognizing those statements whose validity is still in need of proof. We illustrate with some examples.

## EXAMPLE 2 Algebraic proofs

(a) Let $z_{1}, z_{2}$, and $z_{3}$ be complex numbers. Prove that $\operatorname{Im}\left(z_{1}+z_{2}+z_{3}\right)= \operatorname{Im} z_{1}+\operatorname{Im} z_{2}+\operatorname{Im} z_{3}$.
(b) Show that for any complex number $z$, we have $\overline{\bar{z}}=z$.
(c) For any complex number $z$, show that

$$
\operatorname{Re} z=\frac{z+\bar{z}}{2} \quad \text { and } \quad \operatorname{Im} z=\frac{z-\bar{z}}{2 i}
$$

Solution Write $z_{1}=x_{1}+i y_{1}, z_{2}=x_{2}+i y_{2}$, and $z_{3}=x_{3}+i y_{3}$. Then

$$
z_{1}+z_{2}+z_{3}=\left(x_{1}+x_{2}+x_{3}\right)+i\left(y_{1}+y_{2}+y_{3}\right)
$$

and so $\operatorname{Im}\left(z_{2}+z_{2}+z_{3}\right)=y_{1}+y_{2}+y_{3}$. But $\operatorname{Im} z_{1}=y_{1}, \operatorname{Im} z_{2}=y_{2}$, and $\operatorname{Im} z_{3}=y_{3}$, so

$$
\operatorname{Im} z_{1}+\operatorname{Im} z_{2}+\operatorname{Im} z_{3}=y_{1}+y_{2}+y_{3}=\operatorname{Im}\left(z_{2}+z_{2}+z_{3}\right)
$$

which proves (a). To prove (b) and (c), write $z=a+i b$. Conjugating once, we get $\bar{z}=a-i b$. Conjugating again, we get

$$
\overline{\bar{z}}=\overline{a-i b}=a+i b=z,
$$

which proves (b). Now

$$
z+\bar{z}=a+i b+(a-i b)=2 a=2 \operatorname{Re} z
$$

and the first identity in (c) follows upon dividing both sides by 2 . Also,

$$
z-\bar{z}=a+i b-(a-i b)=2 i b=2 i \operatorname{Im} z,
$$

and the second identity in (c) follows upon dividing both sides by $2 i$. $\square$

The complex number system, endowed with the binary operations of addition, subtraction, multiplication, and division, enjoys the same basic algebraic properties as the real numbers. These include the commutative and associative properties of addition and multiplication; the distributive property; the existence of additive inverses; and the existence of multiplicative inverses for nonzero complex numbers (see Exercises 24-26). Consequently, all the algebraic identities that are true for the real numbers remain true for the complex numbers. For example, if $z_{1}$ and $z_{2}$ are complex numbers, then

$$
\begin{aligned}
\left(z_{1}+z_{2}\right)^{2} & =z_{1}^{2}+2 z_{1} z_{2}+z_{2}^{2} \\
\left(z_{1}-z_{2}\right)^{2} & =z_{1}^{2}-2 z_{1} z_{2}+z_{2}^{2} \\
z_{1}^{2}-z_{2}^{2} & =\left(z_{1}-z_{2}\right)\left(z_{1}+z_{2}\right)
\end{aligned}
$$

and so on.

## Square Roots of Negative Numbers

We end this section by revisiting the topic of quadratic equations. As you know, solving such equations involves computing square roots. The problem arises when we attempt to take the square root of a negative number. In the complex number system, a negative number has two square roots. For example, the square roots of -7 are $i \sqrt{7}$ and $-i \sqrt{7}$, because $(i \sqrt{7})^{2}=i^{2} 7=$ -7 and also $(-i \sqrt{7})^{2}=i^{2} 7=-7$. We need a convention to distinguish between the two roots. Given $r>0$, when we write $\sqrt{-r}$ we will be referring to the principal value of the square root of $-r$, defined as $i \sqrt{r}$, with a positive imaginary part. When we write $-\sqrt{-r}$ we will be referring to the second root, $-i \sqrt{r}$.

As an application, let $a, b$, and $c$ be real coefficients and consider the quadratic equation

$$
a x^{2}+b x+c=0 \quad(a \neq 0)
$$

Dividing by $a \neq 0$ and completing the square, we get

$$
\begin{aligned}
x^{2}+\frac{b}{a} x+\left(\frac{b}{2 a}\right)^{2} & =\left(\frac{b}{2 a}\right)^{2}-\frac{c}{a} \\
\left(x+\frac{b}{2 a}\right)^{2} & =\left(\frac{b}{2 a}\right)^{2}-\frac{c}{a} \\
x+\frac{b}{2 a} & = \pm \sqrt{\left(\frac{b}{2 a}\right)^{2}-\frac{c}{a}}= \pm \frac{\sqrt{b^{2}-4 a c}}{2 a}
\end{aligned}
$$

and we arrive at the quadratic formulas

$$
x_{1}=\frac{-b+\sqrt{b^{2}-4 a c}}{2 a} \text { and } x_{2}=\frac{-b-\sqrt{b^{2}-4 a c}}{2 a}
$$

If the discriminant $b^{2}-4 a c>0$, then these formulas yield two distinct real solutions. If $b^{2}-4 a c=0$, then we have one double root. If $b^{2}-4 a c<0$, then $4 a c-b^{2}>0$ and the solutions are in this case

$$
x_{1}=\frac{-b+i \sqrt{4 a c-b^{2}}}{2 a} \text { and } x_{2}=\frac{-b-i \sqrt{4 a c-b^{2}}}{2 a}
$$

Note that the solutions are mutually conjugate. That is, $x_{1}=\overline{x_{2}}$.

## EXAMPLE 3 The quadratic formulas

What are the roots of $x^{2}+x+1=0$ ?
Solution Applying the quadratic formula for the first root, we find

$$
x_{1}=\frac{-1+\sqrt{-3}}{2}=\frac{-1+i \sqrt{3}}{2}
$$

Since the roots are conjugate, we immediately have the other root,

$$
x_{2}=\frac{-1-i \sqrt{3}}{2}
$$

Here we have discussed only the square roots of negative numbers for the purpose of solving the quadratic equation with real coefficients. You may wonder about the square roots of arbitrary complex numbers. Indeed, all complex numbers will have two square roots-these will be discussed in Exercises 31-32 and Section 1.3.

## Exercises 1.1

In Exercises 1-15, write the given complex expression in the form $a+i b$, where $a$ and $b$ are real numbers. Take $x$ and $y$ to be real when they occur.

1. $-i$.
2. $4(5+i)$.
3. $(2-i)(3+i)$.
4. $(2-i)^{2}$.
5. $(\overline{2-i})^{2}$.
6. $(3+2 i)-(e i-\pi)$.
7. $(x+i y)^{2}$.
8. $i \overline{(2+i)^{2}}$.
9. $\left(\frac{1}{2}+\frac{i}{7}\right)\left(\frac{3}{2}-i\right)$.
10. $\left(\frac{1}{2}+\frac{\sqrt{3}}{2} i\right)^{3}$.
11. $(2 i)^{5}$.
12. $i^{12}+i^{25}-7 i^{111}$.
13. $\frac{14+13 i}{2-i}$.
14. $\frac{x+i y}{x-i y}$.
15. $\frac{101+i}{100+i}$.
16. Verify the given property of complex conjugation. Take $z, z_{1}$, and $z_{2}$ to be complex numbers.
(a) $\overline{z_{1}+z_{2}}=\overline{z_{1}}+\overline{z_{2}}$.
(b) $\overline{z_{1}-z_{2}}=\overline{z_{1}}-\overline{z_{2}}$.
(c) $\overline{z_{1} z_{2}}=\overline{z_{1}} \overline{z_{2}}$.
(d) $\overline{\left(\frac{z_{1}}{z_{2}}\right)}=\frac{\overline{z_{1}}}{\overline{z_{2}}} \quad\left(z_{2} \neq 0\right)$.
(e) $\overline{\left(z^{n}\right)}=\bar{z}^{n}, n=1,2, \ldots$.
[Hint: Use induction.]
(f) $z=\bar{z} \Leftrightarrow z$ is purely real. (g) $z=-\bar{z} \Leftrightarrow z$ is purely imaginary.

In Exercises 17-22, solve the given equation. Express your answers in the form $a+i b$, where $a$ and $b$ are real.
17. $x^{2}+6=0$.
18. $x^{2}+2 x=1$.
19. $x^{2}+x+1=0$.
20. $3 x^{2}+x=-2$.
21. $x^{4}+2 x^{2}+1=0$.
22. $x^{4}+6 x^{2}+3=0$.
23. Find two numbers that sum to ten and whose product is 40 . (This problem is of some historical value. It is said that Cardan first stumbled upon complex numbers while solving it.)
24. Let $z_{1}, z_{2}, z_{3}$ be complex numbers. Prove, using the definition of complex numbers and the commutative, associative, and distributive properties of real numbers that
(a) $z_{1}+z_{2}=z_{2}+z_{1}$
(b) $z_{1} z_{2}=z_{2} z_{1}$
(c) $\left(z_{1}+z_{2}\right)+z_{3}=z_{1}+\left(z_{2}+z_{3}\right)$
(d) $\left(z_{1} z_{2}\right) z_{3}=z_{1}\left(z_{2} z_{3}\right)$ (commutativity of addition) (commutativity of multiplication) (associativity of addition)
(e) $z_{1}\left(z_{2}+z_{3}\right)=z_{1} z_{2}+z_{1} z_{3}$ (associativity of multiplication)
(distribution)
25. (a) Let $z=a+i b$ be any complex number. Find the additive inverse for $z$; that is, the complex number $w$ such that $z+w=0$.
(b) Let $e_{s}$ represent a complex number such that $z+e_{s}=z$ for all complex $z$. Show that $e_{s}=0$; that is, $\operatorname{Re}\left(e_{s}\right)=0$ and $\operatorname{Im}\left(e_{s}\right)=0$. Thus $e_{s}=0$ is the unique additive identity for complex numbers.
26. (a) Let $z=a+i b \neq 0$ be a complex number. Find $z^{-1}$ in terms of $a$ and $b$. By $z^{-1}$ we mean the multiplicative inverse of $z$, which satisfies $z z^{-1}=z^{-1} z=1$.
(b) Let $e_{m}$ represent a complex number such that $z e_{m}=e_{m} z=z$ for all complex $z$. Prove that $e_{m}=1$; that is $\operatorname{Re}\left(e_{m}\right)=1$ and $\operatorname{Im}\left(e_{m}\right)=0$. Thus $e_{m}=1$ is the unique multiplicative identity for complex numbers.
(c) Show that if $z_{1} z_{2}=0$, then either $z_{1}=0$ or $z_{2}=0$. [Hint: Suppose $z_{1} \neq 0$. Use (a).]
27. Prove that $c+i d \neq 0 \Leftrightarrow c-i d \neq 0 \Leftrightarrow c^{2}+d^{2} \neq 0$. [Hint: It is enough to prove $c+i d \neq 0 \Rightarrow c-i d \neq 0 \Rightarrow c^{2}+d^{2} \neq 0 \Rightarrow c+i d \neq 0$.]
28. (a) Show that $i^{-n}=i^{n}$ for $n$ even, and $i^{-n}=-i^{n}$ for $n$ odd. (b) Show that $\overline{i^{n}}=i^{-n}$ for all $n$.
29. (a) Let $z$ be a complex number and $n$ a positive integer. A polynomial of degree $n$ is an expression of the form $a_{n} z^{n}+a_{n-1} z^{n-1}+\cdots+a_{1} z+a_{0}$, where $a_{n} \neq 0$. The polynomial is said to have real coefficients if all the coefficients $a_{j}$ are
real. For such a polynomial, show that

$$
\overline{a_{n} z^{n}+a_{n-1} z^{n-1}+\cdots+a_{1} z+a_{0}}=a_{n}(\bar{z})^{n}+a_{n-1}(\bar{z})^{n-1}+\cdots+a_{1} \bar{z}+a_{0} .
$$

[Hint: Exercise 16(e).]
(b) Recall that $z_{0}$ is a root of a polynomial $p(z)$ if $p\left(z_{0}\right)=0$. Show that if $z_{0}$ is a root of a polynomial with real coefficients, then $\overline{z_{0}}$ is also a root. Thus the complex roots of polynomials with real coefficients always appear in conjugate pairs.
30. In each case, use the given roots to find other roots with the help of Exercise 29 . Then factor the polynomial and find all its roots.
(a) $z^{3}+z^{2}+z+1=0, \quad z=i$.
(b) $z^{3}+10 z^{2}+29 z+30=0, \quad z=-2+i$.
(c) $z^{4}+4=0, \quad z_{1}=1+i, z_{2}=-1+i$.
(d) $z^{4}-6 z^{3}+15 z^{2}-18 z+10=0, \quad z_{1}=1+i, z_{2}=2+i$.
31. Project Problem: Computing square roots. The problem of finding $n$th roots of complex numbers will be discussed later in this chapter. The case of square roots is particularly interesting and can be solved by reducing to two equations in two unknowns. In this exercise, you are asked to compute $\sqrt{1+i}$ to illustrate the process.
(a) Finding $\sqrt{1+i}$ is equivalent to solving $z^{2}=1+i$. Let $z=x+i y$ and obtain

$$
\left\{\begin{array}{l}
x^{2}-y^{2}=1 \\
2 x y=1
\end{array}\right.
$$

(b) Derive the equation in $x: 4 x^{4}-4 x^{2}-1=0$. This is essentially a quadratic equation in $x^{2}$.
(c) Keep in mind that $x^{2}$ is nonnegative and obtain that $x^{2}=\frac{1+\sqrt{2}}{2}$. Thus

$$
x= \pm \sqrt{\frac{1+\sqrt{2}}{2}} \text { and } y= \pm \frac{1}{\sqrt{2+2 \sqrt{2}}}
$$

(d) Conclude that the square roots of $1+i$ are

$$
\sqrt{\frac{1+\sqrt{2}}{2}}+\frac{i}{\sqrt{2+2 \sqrt{2}}} \text { and }-\sqrt{\frac{1+\sqrt{2}}{2}}-\frac{i}{\sqrt{2+2 \sqrt{2}}}
$$

32. Compute the given square roots.
(a) $\sqrt{i}$.
(b) $\sqrt{-2+i}$.
(c) $\sqrt{\frac{-1-i \sqrt{3}}{2}}$.
33. Project Problem: The cubic equation. In this exercise, we will derive the solution of the cubic equation

$$
x^{3}+a x^{2}+b x+c=0
$$

(a) Use the change of variables $x=y-\frac{a}{3}$ to transform the equation to the following reduced form

$$
y^{3}+p y+q=0,
$$

which does not contain a quadratic term in $y$, where $p=b-\frac{a^{2}}{3}$ and $q=\frac{2 a^{3}}{27}-\frac{a b}{3}+c$.
(This trick is due to the Italian mathematician Niccolò Tartaglia (1500-1557).)
(b) Let $y=u+v$, and show that $u^{3}+v^{3}+(3 u v+p)(u+v)+q=0$.
(c) Require that $3 u v+p=0$; then directly we have $u^{3} v^{3}=-\frac{p^{3}}{27}$, and from the equation in part (b) we have $u^{3}+v^{3}=-q$.
(d) Suppose that $U$ and $V$ are numbers satisfying $U+V=-\beta$ and $U V=\gamma$.

Show that $U$ and $V$ are solutions of the quadratic equation $X^{2}+\beta X+\gamma=0$.
(e) Use (c) and (d) to conclude that $u^{3}$ and $v^{3}$ are solutions of the quadratic equation $X^{2}+q X-\frac{p^{3}}{27}=0$. Thus,

$$
u=\sqrt[3]{-\frac{q}{2}+\sqrt{\left(\frac{q}{2}\right)^{2}+\left(\frac{p}{3}\right)^{3}}} \text { and } v=\sqrt[3]{-\frac{q}{2}-\sqrt{\left(\frac{q}{2}\right)^{2}+\left(\frac{p}{3}\right)^{3}}}
$$

(f) Derive a solution of (4),

$$
x=\sqrt[3]{-\frac{q}{2}+\sqrt{\left(\frac{q}{2}\right)^{2}+\left(\frac{p}{3}\right)^{3}}}+\sqrt[3]{-\frac{q}{2}-\sqrt{\left(\frac{q}{2}\right)^{2}+\left(\frac{p}{3}\right)^{3}}}-\frac{a}{3}
$$

This is Cardan's formula, named after him because he was the first one to publish it. In the case $\left(\frac{q}{2}\right)^{2}+\left(\frac{p}{3}\right)^{3} \geq 0$, the formula clearly yields one real root of (4). You can use this root to factor (4) down into a quadratic equation, which you can solve to find all the roots of (4). The case $\left(\frac{q}{2}\right)^{2}+\left(\frac{p}{3}\right)^{3}<0$ baffled the mathematicians of the sixteenth century. They knew that the cubic equation (4) must have at least one real root, yet the solution in this case involves square roots of negative numbers, which are imaginary numbers. It turns out in this case that $u$ and $v$ are complex conjugate numbers, hence their sum is a real number and the solution $x$ is real! This was discovered by the Italian mathematician Rafael Bombelli (1527-1572) (see Exercise 38).

Not only was Bombelli bold enough to work with complex numbers; by using them to generate real solutions, he demonstrated that complex numbers were not merely the product of our imagination but tools that are essential to derive real solutions. This theme will occur over and over again in this book when we will appeal to complex variable techniques to solve real-life problems calling for realvalued solutions.

For an interesting account of the history of complex numbers, we refer you to the book The History of Mathematics, An Introduction, 3rd edition, by David M. Burton (McGraw-Hill, 1997).
In Exercises 34-37, use Cardan's formula to find one real root of the given cubic equation. Then factor the cubic and find the remaining solutions (some roots may be repeated).
34. $x^{3}-x+6=0$.
35. $x^{3}+4 x^{2}+x+4=0$.
36. $x^{3}-2 x^{2}+x-12=0$.
37. $x^{3}-2 x^{2}+3=0$.
38. Bombelli's equation. A problem of historical interest is $x^{3}-15 x-4=0$, which was investigated by Bombelli.
(a) Show that, by applying Cardan's formula, we arrive at the solution

$$
x=u+v=\sqrt[3]{2+11 i}+\sqrt[3]{2-11 i}
$$

where $u$ is the first cube root and $v$ is the second.
(b) Bombelli had the incredible insight that $u$ and $v$ have to be conjugate for $u+v$ to be real. Set $u=a+i b$ and $v=a-i b$, where $a$ and $b$ are to be determined. Cube both sides of the equations and note that $a=2, b=1$ will work for both equations.
(c) What is the real solution, $x$, of Bombelli's equation? What are the other two solutions?

### 1.2 The Complex Plane

![](13d4bcc6-f973-445e-ad7d-b22a7a43507d-11_505_470_749_136.jpg)
Figure 1 The complex plane.

![](13d4bcc6-f973-445e-ad7d-b22a7a43507d-11_475_512_1707_129.jpg)
Figure 2 Complex numbers as points and vectors.

A useful way of visualizing complex numbers is to plot them as points in a plane. To do this, we associate to each complex number $z=x+i y$ the ordered pair $(x, y)$, then plot the ordered pair $(x, y)$ as a point $P=(x, y)$ in the Cartesian $x y$-plane. Since $x$ and $y$ uniquely determine $z$, we thus obtain a one-to-one correspondence between complex numbers $z=x+i y$ and points $(x, y)$ in the Cartesian plane. The horizontal axis will be called the real axis, since the abscissa of a complex number is its real part; and complex numbers lying on the horizontal axis are purely real. The vertical axis will be called the imaginary axis, since the ordinate of a complex number is its imaginary part; and complex numbers lying on the vertical axis are purely imaginary. The Cartesian plane will be referred to as the complex plane, also commonly called the $z$-plane. It is not unusual to denote a point ( $x, y$ ) in the complex plane by the corresponding complex number $x+i y$ (see Figure 1). We can also think of a complex number $z=x+i y$ as a two-dimensional vector in the complex plane, with its tail at the origin and its head at $P=(x, y)$.

Historically, the geometric representation of complex numbers is due to Gauss and two lesser known mathematicians: the Frenchman Jean Robert Argand (1768-1822) and a Norwegian surveyor Caspar Wessel (1745-1818). This relatively simple idea dispelled the mystery and skepticism surrounding complex numbers. Much as real numbers are represented as points on a line, complex numbers are represented as points in the plane. As you will soon see, our ability to visualize complex numbers will greatly enhance our understanding of facts concerning complex numbers, and in some cases greatly simplify their proofs.

## EXAMPLE 1 Points and vectors in the plane

Label the following points in the complex plane: $3,0, i, 2-i,-4+3 i$. Draw their associated vectors, emanating from the origin.

Solution The points and the vectors are depicted in Figure 2. The complex number 3, being purely real, lies on the horizontal axis; while $i$, being purely imaginary, lies on the vertical axis. Note that one cannot really draw a vector to represent 0 , whose point is at the origin.

## Geometric Interpretation of Algebraic Rules

The vector representation allows us to add complex numbers by adding their vectors in the plane, with the usual head-to-tail or parallelogram methods (see Figure 3).

![](13d4bcc6-f973-445e-ad7d-b22a7a43507d-12_388_427_650_96.jpg)
Figure 3 Vector addition of complex numbers: the head-to-tail method. Slide $z_{2}$ over so its tail lies atop $z_{1}$ 's head. The resultant vector is then $z_{1}+z_{2}$.

![](13d4bcc6-f973-445e-ad7d-b22a7a43507d-12_508_520_540_788.jpg)
Figure 4 Subtraction: We will find $z_{1}-z_{2}$. We could take $-z_{2}$, then add it to $z_{1}$. Or we could take the vector with its tail at $z_{2}$ 's head, and its head at $z_{1}$ 's head.

![](13d4bcc6-f973-445e-ad7d-b22a7a43507d-12_478_422_572_1459.jpg)
Figure 5 Complex conjugation reflects a point about the horizontal axis.

Multiplying a complex number by -1 has the effect of reflecting it about the origin. If $z=x+i y=(x, y)$, then $-z=-x-i y=(-x,-y)$. This will allow us to subtract complex numbers. The complex subtraction $z_{1}-z_{2}$ can be performed by first multiplying the $z_{2}$ vector by -1 , then adding the resultant to $z_{1}$. Alternatively, we can draw both vectors with their tails at the origin, and the difference will be the vector that points from the head of $z_{2}$ to the head of $z_{1}$ (see Figure 4).

Conjugation has an interesting interpretation in the complex plane. Since the conjugate of $z=x+i y=(x, y)$ is $\bar{z}=x-i y=(x,-y)$, conjugates are reflections of each other across the real axis (see Figure 5).

EXAMPLE 2 Vector addition and subtraction of complex numbers Let $z_{1}=2+i$ and $z_{2}=3-3 i$. Find graphically $z_{1}+z_{2}$ and $z_{1}-z_{2}$.

Solution First draw the points in the plane and their associated vectors (see Figure 3). Then take $z_{2}$ 's vector and slide it so its tail lies on $z_{1}$ 's head. This gives $z_{1}+z_{2}=5-2 i$.

Take $z_{2}$ and reflect it about the origin to get $-z_{2}$. Now add $-z_{2}$ to $z_{1}$ as vectors to get $z_{1}-z_{2}$. The result is $z_{1}-z_{2}=-1+4 i$ (see Figure 4).

![](13d4bcc6-f973-445e-ad7d-b22a7a43507d-13_462_510_238_134.jpg)
Figure 6 The distance from $z$ to the origin is $|z|$.

![](13d4bcc6-f973-445e-ad7d-b22a7a43507d-13_410_458_955_132.jpg)

Figure 7 The distance from $z_{1}$ to $z_{2}$ is $\left|z_{1}-z_{2}\right|$.

![](13d4bcc6-f973-445e-ad7d-b22a7a43507d-13_359_372_1643_131.jpg)
Figure 8

## The Absolute Value

We now discuss an important geometric aspect of complex numbers. For a complex number $z=x+i y$, we define the norm or modulus or absolute value of $z$ by

$$
|z|=\sqrt{x^{2}+y^{2}}
$$

If $z=x$ is real, then $|z|=\sqrt{x^{2}}=|x|$. Thus the absolute value of a complex number $z$ reduces to the familiar absolute value when $z$ is real. Just as the absolute value $|x|$ of a real number $x$ represents the distance from $x$ to the origin on the real line, the absolute value $|z|$ of a complex number $z$ represents the distance from the point $z$ to the origin in the complex plane (see Figure 6). It is easy to see from (1) or Figure 6 that

$$
|z|=0 \Leftrightarrow z=0 ;
$$

and

$$
|-z|=|z| .
$$

If $z_{1}=x_{1}+i y_{1}$ and $z_{2}=x_{2}+i y_{2}$, applying (1) to the complex number $z_{1}-z_{2}=\left(x_{1}-x_{2}\right)+i\left(y_{1}-y_{2}\right)$, we obtain

$$
\left|z_{1}-z_{2}\right|=\sqrt{\left(x_{1}-x_{2}\right)^{2}+\left(y_{1}-y_{2}\right)^{2}}
$$

which is the familiar formula for distance between the points ( $x_{1}, y_{1}$ ) and $\left(x_{2}, y_{2}\right)$. Thus $\left|z_{1}-z_{2}\right|$ has a concrete geometric interpretation as the distance between (the points) $z_{1}$ and $z_{2}$ (see Figure 7).

## EXAMPLE 3 The absolute value as a distance

(a) For $z_{1}=2+4 i$ and $z_{2}=5+i$, we have

$$
\left|z_{1}\right|=\sqrt{2^{2}+4^{2}}=2 \sqrt{5} \approx 4.472, \quad\left|z_{2}\right|=\sqrt{5^{2}+1^{2}}=\sqrt{26} \approx 5.099
$$

Thus we see that $\left|z_{1}\right|<\left|z_{2}\right|$. Geometrically, this means that $z_{2}$ lies farther from the origin in the complex plane (see Figure 8).
(b) The distance between $z_{1}$ and $z_{2}$ is given by

$$
\left|z_{1}-z_{2}\right|=\sqrt{(2-5)^{2}+(4-1)^{2}}=\sqrt{18}=3 \sqrt{2} \approx 4.24
$$

This distance is also the length of the vector $z_{1}-z_{2}$, as shown in Figure 8.
Note that in Example 3(a) we compared the sizes of $z_{1}$ and $z_{2}$ and not the numbers themselves. In general, it does not make sense to write an inequality such as $z_{1} \leq z_{2}$ or $z_{2} \leq z_{1}$, unless $z_{1}$ and $z_{2}$ are real. This is

![](13d4bcc6-f973-445e-ad7d-b22a7a43507d-14_390_484_994_92.jpg)
Figure 9
The circle in Example 4(a).

![](13d4bcc6-f973-445e-ad7d-b22a7a43507d-14_411_458_1675_92.jpg)
Figure 10

The ellipse in Example 4(c).
because the complex numbers do not have a linear ordering like the real numbers.

We can use the geometric interpretation of the absolute value to our advantage in describing subsets of the complex numbers as subsets of the plane.

## EXAMPLE 4 Circles, disks, and ellipses

(a) Find and plot the points $z$ satisfying

$$
|z+4-i|=2
$$

(b) Find and plot the points $z$ satisfying

$$
|z+4-i| \leq 2
$$

(c) Find and plot all complex numbers $z$ such that

$$
|z+2+2 i|+|z+1+i|=4
$$

Solution (a) In answering the questions, we will write an absolute value in the form $\left|z-z_{0}\right|$ and interpret it as a distance between $z$ and $z_{0}$. Thus (5) is equivalent to

$$
|z-(-4+i)|=2
$$

Reading the absolute value as a distance, the question becomes: What are the points $z$ whose distance to $-4+i$ is 2 ? The answer now is obvious:

$$
|z-(-4+i)|=2 \Leftrightarrow z \text { lies on the circle centered at }-4+i, \text { with radius } 2 .
$$

(See Figure 9.) As you know, the Cartesian equation of the circle is $(x+4)^{2}+(y- 1)^{2}=4$. To derive this equation, write $z=x+i y$ and use (4). Thus

$$
|z-(-4+i)|=2 \Leftrightarrow|(x+4)+i(y-1)|=2 \Leftrightarrow \sqrt{(x+4)^{2}+(y-1)^{2}}=2
$$

and the Cartesian equation of the circle follows upon squaring both sides.
(b) Reading the absolute value as a distance, we ask: What are the points $z$ whose distance to $-4+i$ is less than or equal to 2 ? The answer is clear:
$|z-(-4+i)| \leq 2 \Leftrightarrow z$ lies inside or on the circle centered at $-4+i$, with radius 2 .
In other words, $z$ lies in the disk centered at $-4+i$, with radius 2 (Figure 9).
(c) Write (7) in the form

$$
|z-(-2-2 i)|+|z-(-1-i)|=4
$$

This time we are looking for all points $z$ the sum of whose distances to the two points $z_{1}=-2-2 i$ and $z_{2}=-1-i$ is constant and equals 4 . From geometry, we know that the answer is the ellipse with foci (plural of focus) located at $z_{1}$ and $z_{2}$, and semi-major axis 2 . (See Figure 10.)

IDENTITIES INVOLVING THE ABSOLUTE VALUE
(10) states that the absolute value of a product is the product of the absolute values.
(13) states that the absolute value of a quotient is the quotient of the absolute values.

The absolute value of complex numbers enjoys many interesting properties, including all those of the usual absolute value of real numbers.

Let $z, z_{1}, z_{2}, \ldots$ be any complex numbers. We have

$$
|z|=\sqrt{z \bar{z}}, \quad \text { and also } \quad|z|^{2}=z \bar{z} .
$$

Furthermore

$$
|z|=|\bar{z}| .
$$

The absolute value of a product satisfies

$$
\begin{gathered}
\left|z_{1} z_{2}\right|=\left|z_{1}\right|\left|z_{2}\right| \\
\left|z_{1} z_{2} \cdots z_{n}\right|=\left|z_{1}\right|\left|z_{2}\right| \cdots\left|z_{n}\right| \\
\left|z^{n}\right|=|z|^{n} \quad(n=1,2, \ldots)
\end{gathered}
$$

The absolute value of a quotient satisfies

$$
\left|\frac{z_{1}}{z_{2}}\right|=\frac{\left|z_{1}\right|}{\left|z_{2}\right|} \quad\left(z_{2} \neq 0\right)
$$

Recall that, for any complex number $z, z \bar{z}$ is always a nonnegative real number. So there is no problem in taking the square root in (8).
Proof Write $z=x+i y$. Starting from (1), we have

$$
|z|=\sqrt{x^{2}+y^{2}}=\sqrt{\underbrace{(x+i y)}_{z} \underbrace{(x-i y)}_{\bar{z}}}=\sqrt{z \bar{z}},
$$

and (8) follows. Using (1) with $\bar{z}=x-i y$, we find

$$
|\bar{z}|=\sqrt{x^{2}+(-y)^{2}}=\sqrt{x^{2}+y^{2}}=|z| .
$$

Using (8) to compute $\left|z_{1} z_{2}\right|$, we find

$$
\left|z_{1} z_{2}\right|=\sqrt{\left(z_{1} z_{2}\right) \overline{\left(z_{1} z_{2}\right)}}=\sqrt{\left(z_{1} \overline{z_{1}}\right)\left(z_{2} \overline{z_{2}}\right)}=\sqrt{z_{1} \overline{z_{1}}} \sqrt{z_{2} \overline{z_{2}}}=\left|z_{1}\right|\left|z_{2}\right| .
$$

(For the second equality, we used $\overline{z_{1} z_{2}}=\overline{z_{1}} \overline{z_{2}}$ and the associativity of multiplication.) The proofs of (11) and (12) are straightforward and are left as an exercise. Replacing $z_{1}$ by $\frac{z_{1}}{z_{2}}\left(z_{2} \neq 0\right)$ in (10), we obtain

$$
\left|\frac{z_{1}}{z_{2}} z_{2}\right|=\left|\frac{z_{1}}{z_{2}}\right|\left|z_{2}\right| \Rightarrow\left|z_{1}\right|=\left|\frac{z_{1}}{z_{2}}\right|\left|z_{2}\right|,
$$

and (13) follows upon dividing by $\left|z_{2}\right| \neq 0$.

## EXAMPLE 5 Moduli of products and quotients

Compute the given absolute value. Take $n$ to be a positive integer.
(a) $|(1+i) \overline{(2-i)}|$.
(b) $\left|(1-i)^{4}(1+2 i)(1+\sqrt{2} i)\right|$.
(c) $\left|i^{n}\right|$.
(d) $\left|\frac{1+2 i}{1-i}\right|$.
(e) $\left|\frac{(3+4 i)^{2}(3-i)^{10}}{(3+i)^{9}}\right|$.

Solution We will use as much as possible the properties of the absolute value to avoid excessive computations.
(a) Using (10) and (9), we have

$$
|(1+i) \overline{(2-i)}|=|1+i||\overline{(2-i)}|=|1+i||2-i|=\sqrt{2} \sqrt{5}=\sqrt{10}
$$

(b) Using (11) and (12), we have

$$
\left|(1-i)^{4}(1+2 i)(1+\sqrt{2} i)\right|=\left|(1-i)^{4}\right| \overbrace{|1+2 i|}^{=\sqrt{5}} \overbrace{|1+\sqrt{2} i|}^{=\sqrt{3}}=\overbrace{|1-i|^{4}}^{=(\sqrt{2})^{4}} \sqrt{15}=4 \sqrt{15} .
$$

(c) From (12) and the fact that $|i|=1$, we have

$$
\left|i^{n}\right|=|i|^{n}=1
$$

(d) Using (13), we have

$$
\left|\frac{1+2 i}{1-i}\right|=\frac{|1+2 i|}{|1-i|}=\sqrt{\frac{5}{2}}
$$

(e) We have

$$
\left|\frac{(3+4 i)^{2}(3-i)^{10}}{(3+i)^{9}}\right|=\frac{\overbrace{|3+4 i|^{2}}^{=25}|3-i|^{10}}{|3+i|^{9}}=25|3-i|=25 \sqrt{10},
$$

because $|3+i|=|3-i|$ by (9).
In addition to the identities that we just proved, the absolute value satisfies fundamental inequalities, which are in some cases immediate consequences of elementary facts from geometry. Let us recall two facts and then list the inequalities that will be obtained as a consequence.

- In a right triangle, the hypotenuse is larger than either one of the other two sides.
- In any triangle, the sum of two sides is larger than the third side.

INEQUALITIES INVOLVING THE ABSOLUTE VALUE

![](13d4bcc6-f973-445e-ad7d-b22a7a43507d-17_407_422_896_125.jpg)
Figure 11
For inequalities (14) and (15).

![](13d4bcc6-f973-445e-ad7d-b22a7a43507d-17_358_362_1677_123.jpg)
Figure 12
For inequality (18).

Let $z, z_{1}, z_{2}, \ldots$ be complex numbers. We have

$$
\begin{gathered}
|\operatorname{Re} z| \leq|z|, \quad|\operatorname{Im} z| \leq|z| ; \\
|z| \leq|\operatorname{Re} z|+|\operatorname{Im} z| .
\end{gathered}
$$

The absolute value of a sum satisfies the fundamental inequality

$$
\left|z_{1}+z_{2}\right| \leq\left|z_{1}\right|+\left|z_{2}\right|
$$

known as the triangle inequality. More generally,

$$
\left|z_{1}+z_{2}+\cdots+z_{n}\right| \leq\left|z_{1}\right|+\left|z_{2}\right|+\cdots+\left|z_{n}\right| .
$$

The absolute value of a difference satisfies

$$
\left|z_{1}-z_{2}\right| \leq\left|z_{1}\right|+\left|z_{2}\right|
$$

A lower bound for $\left|z_{1} \pm z_{2}\right|$ is provided by

$$
\left|z_{1} \pm z_{2}\right| \geq\left|\left|z_{1}\right|-\right| z_{2} \|
$$

Proof Consider a nondegenerate right triangle with vertices at $0, z=(x, y)$, and $\operatorname{Re} z=x$, as shown in Figure 11. The sides of the triangle are $|\operatorname{Re} z|=|x|$, $|\operatorname{Im} z|=|y|$, and the hypothenuse is $|z|$. Since the hypothenuse is larger than either of the other two sides, we obtain (14). Since the sum of two sides in a triangle is larger than the third side, we obtain (15). Of course, (14) and (15) are also consequences of the inequalities

$$
|x| \leq \sqrt{x^{2}+y^{2}}, \quad|y| \leq \sqrt{x^{2}+y^{2}}, \text { and } \sqrt{x^{2}+y^{2}} \leq|x|+|y|
$$

which are straightforward to prove.
For the moment, we skip (16) and (17) and prove (18). Consider the triangle in Figure 12 with vertices at $0, z_{1}$, and $z_{2}$. The lengths of the sides in that triangle are $\left|z_{1}\right|,\left|z_{2}\right|$, and $\left|z_{1}-z_{2}\right|$. Because the sum of two sides is larger than the third side, we obtain (18). Replacing $z_{2}$ by $-z_{2}$ and noticing that $\left|-z_{2}\right|=\left|z_{2}\right|$, we obtain (16). Inequality (17) follows by repeated applications of (16).

Replacing $z_{1}$ by $z_{1}-z_{2}$ in (16), we obtain $\left|z_{1}\right| \leq\left|z_{1}-z_{2}\right|+\left|z_{2}\right|$, and so

$$
\left|z_{1}-z_{2}\right| \geq\left|z_{1}\right|-\left|z_{2}\right| .
$$

Reversing the roles of $z_{1}$ and $z_{2}$, and realizing that $\left|z_{2}-z_{1}\right|=\left|z_{1}-z_{2}\right|$, we also have

$$
\left|z_{1}-z_{2}\right| \geq\left|z_{2}\right|-\left|z_{1}\right| .
$$

Putting these two together, we conclude $\left|z_{1}-z_{2}\right| \geq\left|\left|z_{1}\right|-\left|z_{2}\right|\right|$, which proves the "minus-sign" inequality in (19). To get the inequality with a plus sign, namely, $\left|z_{1}+z_{2}\right| \geq\left|\left|z_{1}\right|-\left|z_{2}\right|\right|$, replace $z_{2}$ by $-z_{2}$.

Because the triangle inequality is fundamental in the development of complex analysis, we will also offer an algebraic proof. This will afford us the opportunity to practice some of the properties of complex numbers that we have already derived. Start by observing that

$$
\overline{z_{1} \overline{z_{2}}}=\overline{z_{1}} \overline{\overline{z_{2}}}=\overline{z_{1}} z_{2}
$$

Since for any complex number $w, w+\bar{w}=2 \operatorname{Re} w$, we obtain

$$
z_{1} \overline{z_{2}}+\overline{z_{1}} z_{2}=z_{1} \overline{z_{2}}+\overline{z_{1}} \overline{z_{2}}=2 \operatorname{Re}\left(z_{1} \overline{z_{2}}\right)
$$

Using this interesting identity, along with (8) and basic properties of complex conjugation, we obtain

$$
\begin{aligned}
\left|z_{1}+z_{2}\right|^{2} & =\left(z_{1}+z_{2}\right) \overline{\left(z_{1}+z_{2}\right)}=\left(z_{1}+z_{2}\right)\left(\overline{z_{1}}+\overline{z_{2}}\right) \\
& =z_{1} \overline{z_{1}}+z_{2} \overline{z_{2}}+z_{1} \overline{z_{2}}+\overline{z_{1}} z_{2}=\left|z_{1}\right|^{2}+\left|z_{2}\right|^{2}+z_{1} \overline{z_{2}}+\overline{z_{1}} z_{2} \\
& =\left|z_{1}\right|^{2}+\left|z_{2}\right|^{2}+2 \operatorname{Re}\left(z_{1} \overline{z_{2}}\right) \\
& \leq\left|z_{1}\right|^{2}+\left|z_{2}\right|^{2}+2\left|z_{1} \overline{z_{2}}\right| \\
& =\left|z_{1}\right|^{2}+\left|z_{2}\right|^{2}+2\left|z_{1}\right| \overline{z_{2}} \mid \\
& =\left|z_{1}\right|^{2}+\left|z_{2}\right|^{2}+2\left|z_{1}\right|\left|z_{2}\right| \quad\left([\text { by }(9)],\left|\overline{z_{2}}\right|=\left|z_{2}\right|\right) \\
& =\left(\left|z_{1}\right|+\left|z_{2}\right|\right)^{2}
\end{aligned}
$$

and (16) follows now upon taking square roots on both sides.
The triangle inequality will be used extensively in proofs to provide estimates on the sizes of complex-valued expressions. We next illustrate this type of applications with examples.

EXAMPLE 6 Estimating the size of an absolute value
What is an upper bound for $\left|z^{5}-4\right|$ if $|z| \leq 1$ ?
Solution Applying the triangle inequality, we get

$$
\left|z^{5}-4\right| \leq\left|z^{5}\right|+4=|z|^{5}+4 \leq 1+4=5,
$$

because $|z| \leq 1$. Hence if $|z| \leq 1$, an upper bound for $\left|z^{5}-4\right|$ is 5 .
Can we find a number smaller than 5 that is also an upper bound, or is 5 the least upper bound? It is easy to see that for $z=-1$, we have $\left|z^{5}-4\right|=\left|(-1)^{5}-4\right|= |-1-4|=5$. Thus, the upper bound 5 is best possible. You should be cautioned that, in general, the triangle inequality is considered as a crude inequality, which means that it will not yield least upper bound estimates as it did in this case. See Exercise 33 for an illustration.

## EXAMPLE 7 Inequalities

Show that for any complex numbers $z$ and $a$

$$
\frac{1}{|a|+|z|} \leq\left|\frac{1}{a+z}\right| \leq \frac{1}{\| a|-|z|}
$$

Solution The triangle inequality (16) tells us that $|a+z| \leq|a|+|z|$, while (19) implies that $||a|-|z|| \leq|a+z|$. Hence the inequalities

$$
\| a|-|z|| \leq|a+z| \leq|a|+|z| .
$$

Taking reciprocals reverses the inequalities and yields

$$
\frac{1}{||a|-|z||} \geq \frac{1}{|a+z|} \geq \frac{1}{|a|+|z|}
$$

which implies (20), since $\left|\frac{1}{a+z}\right|=\frac{1}{|a+z|}$ by (13).
Our final example illustrates a classical trick in dealing with inequalities. It consists of adding and subtracting a number in order to transform a given expression into a form that contains familiar terms.

## EXAMPLE 8 Tricks with the absolute value

(a) What is an upper bound for $|z-3|$ if $|z-i| \leq 1$ ?
(b) What is a lower bound for $|z-3|$ if $|z-i| \leq 1$ ?

Solution (a) We want to know some thing about $|z-3|$ given some information about $|z-i|$. The trick is to add and subtract $i$, then use the triangle inequality as follows:

$$
\begin{aligned}
|z-3| & =|z-i+i+3|=|(z-i)+(3+i)| \quad \text { (Add and subtract } i .) \\
& \leq|z-i|+\underbrace{|3+i|}_{=\sqrt{10}} \leq 1+\sqrt{10}, \quad \text { (triangle inequality) }
\end{aligned}
$$

since $|z-i| \leq 1$. Thus an upper bound is $1+\sqrt{10}$.
(b) In finding a lower bound, we will proceed as in (a) but use (19) instead of the triangle inequality. We have

$$
\begin{aligned}
|z-3| & =|(z-i)+(3+i)| \quad(\text { Add and subtract } i .) \\
& \geq| | z-i|-|3+i||=||z-i|-\sqrt{10}|
\end{aligned}
$$

by (19). Now since $|z-i|$ is at most 1 and $\sqrt{10}>1$, we see that

$$
||z-i|-\sqrt{10}| \geq \sqrt{10}-1
$$

Hence, $|z-3| \geq \sqrt{10}-1$ if $|z-i| \leq 1$.

## Exercises 1.2

In Exercises 1-6, plot the points $z,-z, \bar{z}$ and the associated vectors emanating from the origin. In each case, compute the modulus of $z$.

1. $1-i$.
2. $\quad \frac{\sqrt{2}}{2}+i \frac{\sqrt{2}}{2}$.
3. $3 i+5$.
4. $\quad i^{7}$.
5. $\overline{1-i}$.
6. $(1+i)^{2}$.
7. Let

$$
z_{1}=i, z_{2}=\frac{\sqrt{2}}{2}+i \frac{\sqrt{2}}{2}, z_{3}=\frac{\sqrt{2}}{2}-i \frac{\sqrt{2}}{2}, z_{4}=\frac{1}{2}+i \frac{3}{2} .
$$

(a) Plot $z_{2}, z_{3}$, and $z_{2}+z_{3}$ on the same complex plane. Explain in words how you constructed $z_{2}+z_{3}$.
(b) Plot the points $z_{1}, z_{2}, z_{3}, z_{4}$, compute their moduli, and decide which point or points are closest to the origin.
(c) Find graphically $z_{1}-z_{2}, z_{2}-z_{3}$, and $z_{3}-z_{4}$.
(d) Which one of the points $z_{2}$ or $z_{4}$ is closer to $z_{1}$ ?
8. Let $z_{1}=i, z_{2}=1+2 i$.
(a) On the same complex plane, plot $z_{1}, z_{2}, z_{1}+z_{2}, z_{1}-z_{2}, z_{2}-z_{1}$.
(b) How does vector $z_{1}-z_{2}$ compare with $z_{2}-z_{1}$ ?
(c) On the same complex plane, plot the vectors $z_{2}$ and $i z_{2}$. How do these vectors compare? Describe in general the vector $i z$ in comparison with vector $z$.
(d) Describe in general the vector $z / i$ in comparison with $z$.

In Exercises 9-14, compute the given modulus.
9. $|(1+i)(1-i)(1+3 i)|$.
10. $\left|\overline{(2+3 i)^{8}}\right|$.
11. $\left|\left(\frac{\sqrt{2}}{2}+i \frac{\sqrt{2}}{2}\right)^{27}\right|$.
12. $\left|\frac{1+i}{(1-i)(1+3 i)}\right|$.
13. $\left|\frac{i}{\overline{2-i}}\right|$.
14. $\left|\frac{(1+i)^{5}}{(-2+2 i)^{5}}\right|$.

In Exercises 15-20, describe and plot the set of points satisfying the given equation.
15. $|z-4|=3$.
16. $|z+2+i|=1$.
17. $|z-i|=-1$.
18. $|z+1|+|z-1|=4$.
19. $|z-i|+|z|=2$.
20. $|2 z|+|2 z-1|=4$.
21. Derive the equation of the ellipse in Exercise 20.
22. Derive the equation of the circle in Exercise 16.
23. Lines in the complex plane. (a) Show that the set of points $z$ in the complex plane with $\operatorname{Re} z=a$ ( $a$ real) is the vertical line $x=a$.
(b) Show that the set of points $z$ in the complex plane with $\operatorname{Im} z=b$ ( $b$ real) is the horizontal line $y=b$.
(c) Let $z_{1} \neq z_{2}$ be two points in the complex plane. Show that the set of points $z$ such that $z=z_{1}+t\left(z_{2}-z_{1}\right)$, where $t$ is real, is the line going through $z_{1}$ and $z_{2}$. Illustrate your answer graphically by plotting the vectors $z_{1}, z_{1}+z_{2}$, and $z_{1}+t\left(z_{2}-z_{1}\right)$ for several values of $t$.
24. Show that three distinct points $z_{1}, z_{2}$, and $z_{3}$ lie on the same line if and only if

$$
\frac{z_{1}-z_{2}}{z_{1}-z_{3}}=t
$$

where $t$ is real. (Compare with Exercise 23(c).)

![](13d4bcc6-f973-445e-ad7d-b22a7a43507d-21_383_366_749_108.jpg)
Figure 13 Triangle inequality, Exercise 28.

![](13d4bcc6-f973-445e-ad7d-b22a7a43507d-21_495_502_1294_106.jpg)
Figure 14 For Exercise 29.

![](13d4bcc6-f973-445e-ad7d-b22a7a43507d-21_373_475_2019_106.jpg)
Figure 15 Parallelogram identity, Exercise 32.

25. Parabolas. Recall from geometry that a parabola is the set of points in the plane that are equidistant from a fixed line (called the directrix) and a fixed point not on the line (called the focus).
(a) Using this description and the geometric interpretation of the absolute value, argue that the set of points $z$ satisfying

$$
|z-1-i|=\operatorname{Re}(z)+1
$$

is a parabola. Find its directrix and its focus and then plot it.
(b) More generally, describe the set of points $z$ such that

$$
\left|z-z_{0}\right|=\operatorname{Re}(z)-a,
$$

where $a$ is a real number.
26. (a) With the help of Exercise 25, describe the set of points $z$ such that

$$
|z-i|=\operatorname{Im}(z)+2 .
$$

(b) More generally, describe the set of points $z$ such that

$$
\left|z-z_{0}\right|=\operatorname{Im}(z)-a,
$$

where $a$ is a real number.
27. The multiplicative inverse. Show that if $z \neq 0$, then

$$
z^{-1}=\frac{\bar{z}}{|z|^{2}} .
$$

28. Use Figure 13 to argue a proof for (16).
29. Use Figure 14 to argue a proof for (19).
30. Equality in the triangle inequality. When do we have

$$
\left|z_{1}+z_{2}\right|=\left|z_{1}\right|+\left|z_{2}\right| ?
$$

To answer this question, review the algebraic proof of the triangle inequality and note that the string of equalities in the proof was broken when we replaced $2 \operatorname{Re}\left(z_{1} \overline{z_{2}}\right)$ by $2\left|z_{1}\right|\left|z_{2}\right|$. Thus we have an equality in the triangle inequality if and only if $\operatorname{Re}\left(z_{1} \overline{z_{2}}\right)=\left|z_{1}\right|\left|z_{2}\right|$. Show that this is the case if and only either $z_{1}$ or $z_{2}$ is zero or $z_{1}=\alpha z_{2}$, where $\alpha$ is a positive real number. Geometrically, this states that $z_{1}$ and $z_{2}$ are on the same side of the ray issued from the origin.
31. (a) Give an example to show that, in general, $z^{2} \neq|z|^{2}$.
(b) Show that $z^{2}=|z|^{2} \Leftrightarrow \operatorname{Im} z=0$.
32. Parallelogram identity. (a) Consider an arbitrary parallelogram as in Figure 15, with sides $a, b$, and diagonals $c$ and $d$. Prove the following identity:

$$
c^{2}+d^{2}=2\left(a^{2}+b^{2}\right) .
$$

(The identity states the well-known fact that, in a parallelogram, the sum of the squares of the diagonals is equal to the sum of the squares of the sides.) In your
proof, use the law of $\operatorname{cosines} r^{2}+s^{2}-2 r s \cos \alpha=a^{2}$, where $\alpha$ is the angle opposite the side $a$, and $r$ and $s$ are the other two sides.
(b) Let $u$ and $v$ be arbitrary complex numbers. Form the parallelogram with sides $u$ and $v$. Plot $u+v$ and $u-v$ as diagonals of this parallelogram.
(c) Using parts (a) and (b), show from geometric considerations that for any complex numbers $u$ and $v$

$$
|u+v|^{2}+|u-v|^{2}=2\left(|u|^{2}+|v|^{2}\right) .
$$

This is known as the parallelogram identity for complex numbers.
(d) Prove the parallelogram identity algebraically using (8).
33. The triangle inequality is crude. (a) Justify each step in the following estimate

$$
|\cos \theta+i \sin \theta| \leq|\cos \theta|+|i \sin \theta|=|\cos \theta|+|\sin \theta| \leq 2 .
$$

Thus, a straightforward application of the triangle inequality yields the estimate $|\cos \theta+i \sin \theta| \leq 2$.
(b) Use the definition of the absolute value to show $|\cos \theta+i \sin \theta|=1$. Hence the estimate in (a) is not the best possible estimate.
34. (a) Use the triangle inequality to show that $|z-1| \leq 2$ for $|z| \leq 1$.
(b) Explain your result in (a) geometrically.
(c) Is the upper bound in (a) best possible?
35. Find an upper bound for $|z-4|$ if $|z-3 i| \leq 1$.
36. Find a lower bound for $|z-4|$ if $|z-3 i| \leq 1$.
37. Find an upper bound for $\left|\frac{1}{z-4}\right|$ if $|z-1| \leq 1$. [Hint: Find a lower bound for $|z-4|$.]
38. Find an upper bound for $\left|\frac{1}{1-z}\right|$ if $|z-i| \leq \frac{1}{2}$.
39. Find an upper bound for $\left|\frac{1}{z^{2}+z+1}\right|$ if $|z| \leq \frac{1}{2}$.
40. Find a lower bound for $\left|\frac{1}{z^{2}+z+1}\right|$ if $|z| \leq \frac{1}{2}$.
41. Project Problem: Cauchy-Schwarz inequality. Suppose that $v_{1}, v_{2}$, $\ldots, v_{n}$ and $w_{1}, w_{2}, \ldots, w_{n}$ are arbitrary complex numbers. Our goal in this exercise is to prove the Cauchy-Schwarz inequality, which states that

$$
\left|\sum_{j=1}^{n} \overline{v_{j}} w_{j}\right| \leq \sqrt{\sum_{j=1}^{n}\left|v_{j}\right|^{2}} \sqrt{\sum_{j=1}^{n}\left|w_{j}\right|^{2}} .
$$

(a) Show that in order to prove (21) it is enough to prove

$$
\sum_{j=1}^{n}\left|v_{j}\right|\left|w_{j}\right| \leq \sqrt{\sum_{j=1}^{n}\left|v_{j}\right|^{2}} \sqrt{\sum_{j=1}^{n}\left|w_{j}\right|^{2}} .
$$

(b) Prove (22) in the case $\sum_{j=1}^{n}\left|v_{j}\right|^{2}=1$ and $\sum_{j=1}^{n}\left|w_{j}\right|^{2}=1$. [Hint: Start with the inequality $0 \leq \sum_{j=1}^{n}\left(\left|v_{j}\right|-\left|w_{j}\right|\right)^{2}$. Expand and simplify.]
![](13d4bcc6-f973-445e-ad7d-b22a7a43507d-23_241_1412_175_638.jpg)

### 1.3 Polar Form

In the previous section, we represented complex numbers as points in the plane and used Cartesian coordinates. In this section, we will use polar coordinates and obtain the so-called polar representation or polar form of

![](13d4bcc6-f973-445e-ad7d-b22a7a43507d-23_440_506_707_131.jpg)
Figure 1 Polar coordinates.

## POLAR FORM OF COMPLEX NUMBERS

complex numbers. The polar form will introduce trigonometry into the picture, enabling us to take fuller advantage of our geometric insight.

If $P=(x, y) \neq(0,0)$ is a point given in Cartesian coordinates, we will write it in polar coordinates as $P=(r, \theta)$, where $r$ is the distance from $P$ to the origin $O$, and $\theta$ is the angle between the polar axis (which points toward positive $x$ ) and the ray $O P$. As the usual convention for $\theta$, the counterclockwise direction is positive, while the clockwise direction is negative. We have the familiar change of coordinates formulas:

$$
x=r \cos \theta \quad \text { and } \quad y=r \sin \theta, \quad \text { where } r \geq 0 .
$$

Given a complex number $z=x+i y$, we think of $z$ as a point $(x, y)$ in the complex plane. Using polar coordinates. we obtain the following polar representation.
Let $z=x+i y$ be a complex number. We have the polar representation

$$
z=r(\cos \theta+i \sin \theta)
$$

where $r$ is the modulus of $z$ and $\theta$ is the is the argument of $z$. We have

$$
r=\sqrt{x^{2}+y^{2}} \geq 0
$$

and $\theta$ is any angle such that
(4) $\quad \cos \theta=\frac{x}{\sqrt{x^{2}+y^{2}}}=\frac{x}{r}, \quad \sin \theta=\frac{y}{\sqrt{x^{2}+y^{2}}}=\frac{y}{r} \quad(r \neq 0)$.

The argument of $z$ is not defined when $z=0$; equivalently, when $r=0$.
From Figure 1, we have

$$
\operatorname{Re} z=r \cos \theta, \quad \operatorname{Im} z=r \sin \theta
$$

and

$$
\tan \theta=\frac{y}{x} \quad(x \neq 0)
$$

From (3) in this section and (8) in Section 1.2,

$$
r=\sqrt{x^{2}+y^{2}}=|z|=\sqrt{z \bar{z}}
$$

It is easy to see that

$$
|z|=1 \Leftrightarrow r=1 \Leftrightarrow z=\cos \theta+i \sin \theta \text {, for some real } \theta \text {. }
$$

Any complex number $z$ such that $|z|=1$ is called unimodular. See Exercise 30 for basic properties of unimodular numbers.

We now shift our attention to the more delicate subject of the argument. If $\theta$ is any angle that satisfies (4), then $\theta+2 k \pi(k=0, \pm 1, \pm 2, \ldots)$ will also satisfy (4), because the cosine and sine are $2 \pi$-periodic functions. Thus, relations (4) do not determine a unique value of argument $z$. If we restrict the choice of $\theta$ to the interval $-\pi<\theta \leq \pi$, then there is a unique value of $\theta$ that satisfies (4). We call this value the principal value of the argument and denote it by $\operatorname{Arg} z$. Thus, by definition, if $z=x+i y$, then

$$
-\pi<\operatorname{Arg} z \leq \pi, \quad \cos (\operatorname{Arg} z)=\frac{x}{|z|}, \quad \sin (\operatorname{Arg} z)=\frac{y}{|z|}
$$

The set of all values of the argument will be denoted by

$$
\arg z=\{\theta+2 k \pi: k=0, \pm 1, \pm 2, \ldots\},
$$

where $\theta$ is any angle that satisfies (4). In particular, we have

$$
\arg z=\{\operatorname{Arg} z+2 k \pi: k=0, \pm 1, \pm 2, \ldots\} .
$$

Unlike $\operatorname{Arg} z$, which is $\operatorname{single}$-valued, $\arg z$ is multi-valued or set-valued. Sometimes we will abuse notation and write $\arg z=\theta+2 k \pi$ or simply $\arg z=\theta$ to denote a specific value of the argument from the set $\arg z$.

Table 1 contains some special values that will be useful in the examples and exercises.

| $\theta$ | 0 | $\frac{\pi}{6}$ | $\frac{\pi}{4}$ | $\frac{\pi}{3}$ | $\frac{\pi}{2}$ | $\frac{2 \pi}{3}$ | $\frac{3 \pi}{4}$ | $\frac{5 \pi}{6}$ | $\pi$ | $\frac{7 \pi}{6}$ | $\frac{5 \pi}{4}$ | $\frac{4 \pi}{3}$ | $\frac{3 \pi}{2}$ | $\frac{5 \pi}{3}$ | $\frac{7 \pi}{4}$ | $\frac{11 \pi}{6}$ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| $\cos \theta$ | 1 | $\frac{\sqrt{3}}{2}$ | $\frac{\sqrt{2}}{2}$ | $\frac{1}{2}$ | 0 | $-\frac{1}{2}$ | $-\frac{\sqrt{2}}{2}$ | $-\frac{\sqrt{3}}{2}$ | -1 | $-\frac{\sqrt{3}}{2}$ | $-\frac{\sqrt{2}}{2}$ | $-\frac{1}{2}$ | 0 | $\frac{1}{2}$ | $\frac{\sqrt{2}}{2}$ | $\frac{\sqrt{3}}{2}$ |
| $\sin \theta$ | 0 | $\frac{1}{2}$ | $\frac{\sqrt{2}}{2}$ | $\frac{\sqrt{3}}{2}$ | 1 | $\frac{\sqrt{3}}{2}$ | $\frac{\sqrt{2}}{2}$ | $\frac{1}{2}$ | 0 | $-\frac{1}{2}$ | $-\frac{\sqrt{2}}{2}$ | $-\frac{\sqrt{3}}{2}$ | -1 | $-\frac{\sqrt{3}}{2}$ | $-\frac{\sqrt{2}}{2}$ | $-\frac{1}{2}$ |
| $\tan \theta$ | 0 | $\frac{\sqrt{3}}{3}$ | 1 | $\sqrt{3}$ | not defined | $-\sqrt{3}$ | -1 | $-\frac{\sqrt{3}}{3}$ | 0 | $\frac{\sqrt{3}}{3}$ | 1 | $\sqrt{3}$ | not defined | $-\sqrt{3}$ | -1 | $-\frac{\sqrt{3}}{3}$ |

Table 1. Special trigonometric values.

![](13d4bcc6-f973-445e-ad7d-b22a7a43507d-25_465_487_238_121.jpg)
Figure 2 The points in Example 1.

Note that $r$ is always $\geq 0$ in the polar representation.

## EXAMPLE 1 Polar form

Find the modulus, argument, principal value of the argument, and polar form of the given complex number.
(a) $z_{1}=5$.
(b) $z_{2}=-3 i$.
(c) $z_{3}=\sqrt{3}+i$.
(d) $z_{4}=1+i$.
(e) $z_{5}=1-i$.
(f) $\quad z_{6}=-1-i$.

Solution Several parts of our answer are obvious from Figure 2, where we have plotted the given complex numbers.
(a) From (3), $r=\left|z_{1}\right|=5$. An argument of $z_{1}$ is clearly $\theta=0$. Thus, arg $z_{1}= \{2 k \pi: k=0, \pm 1, \pm 2, \ldots\}$. Since 0 is in the interval $(-\pi, \pi]$, we also have $\operatorname{Arg} z_{1}=$ 0 . The polar representation is

$$
5=5(\cos 0+i \sin 0)
$$

(b) Here $r=\left|z_{2}\right|=|-3 i|=3$, and, from Figure 2, $\arg z_{2}=\frac{3 \pi}{2}+2 k \pi$. To determine $\operatorname{Arg} z_{2}$, we must pick the unique value of $\arg z_{2}$ that lies in the interval ( $-\pi, \pi]$. From Figure 2, we clearly have $\operatorname{Arg} z_{2}=-\frac{\pi}{2}$. Thus, the polar representation

$$
-3 i=3\left(\cos \frac{3 \pi}{2}+i \sin \frac{3 \pi}{2}\right)=3\left(\cos \left(\frac{-\pi}{2}\right)+i \sin \left(\frac{-\pi}{2}\right)\right) .
$$

(c) Here the answers are not obvious from Figure 2, so we will supply all the details. We have $r=\left|z_{3}\right|=|\sqrt{3}+i|=\sqrt{3+1}=2$. So from (4), we have

$$
\cos \theta=\frac{x}{r}=\frac{\sqrt{3}}{2} \quad \text { and } \quad \sin \theta=\frac{y}{r}=\frac{1}{2}
$$

From Table 1 , we find that $\theta=\frac{\pi}{6}$. Thus, $\arg z_{3}=\frac{\pi}{6}+2 k \pi, \operatorname{Arg} z_{3}=\frac{\pi}{6}$, and the polar representation is

$$
\sqrt{3}+i=2\left(\cos \frac{\pi}{6}+i \sin \frac{\pi}{6}\right)
$$

(d) We will repeat the steps in (c), even though you may be able to guess the answers from Figure 2. We have $r=\left|z_{4}\right|=\sqrt{1+1}=\sqrt{2}$. Factoring the modulus of $1+i$, we obtain

$$
\begin{aligned}
1+i & =\sqrt{2}\left(\frac{1}{\sqrt{2}}+i \frac{1}{\sqrt{2}}\right)=\sqrt{2}\left(\frac{\sqrt{2}}{2}+i \frac{\sqrt{2}}{2}\right) \\
& =\sqrt{2}\left(\cos \frac{\pi}{4}+i \sin \frac{\pi}{4}\right) \quad(\text { from Table 1), }
\end{aligned}
$$

which is the polar form of $z_{4}$, with $\operatorname{Arg} z_{4}=\frac{\pi}{4}$.
(e) It is clear from Figure 2 that $z_{5}$ is the reflection of $z_{4}=1+i$ about the $x$ axis (equivalently, $z_{5}=\overline{z_{4}}$ ). Hence $z_{5}$ and $z_{4}$ have the same moduli and opposite arguments. So $r=\sqrt{2}$, $\arg z_{5}=-\frac{\pi}{4}, \operatorname{Arg} z_{5}=-\frac{\pi}{4}$, and the polar representation is

$$
1-i=\sqrt{2}\left(\cos \left(-\frac{\pi}{4}\right)+i \sin \left(-\frac{\pi}{4}\right)\right)
$$

![](13d4bcc6-f973-445e-ad7d-b22a7a43507d-26_359_546_759_117.jpg)
Figure 3 The inverse tangent takes its values in $\left(\frac{-\pi}{2}, \frac{\pi}{2}\right)$.

For $z=x+i y$ :
$x>0 \Leftrightarrow \quad z$ is in the first or fourth quadrants;
$x<0$ and $y>0 \Leftrightarrow z$ is in the second quadrant;
$x<0$ and $y<0 \Leftrightarrow z$ is in the third quadrant.

![](13d4bcc6-f973-445e-ad7d-b22a7a43507d-26_417_554_1995_130.jpg)
Figure 4 Computing $\operatorname{Arg} z$ using (14).

(f) Note that $z_{6}$ is the reflection of $z_{4}=1+i$ about the origin (equivalently, $z_{6}=-z_{4}$ ). Hence $z_{6}$ and $z_{4}$ have the same moduli and their arguments are related by the identity $\arg z_{6}=\arg z_{4}+\pi$. So, $r=\sqrt{2}$, $\arg z_{6}=\frac{\pi}{4}+\pi=\frac{5 \pi}{4}$, $\operatorname{Arg} z_{6}=-\frac{3 \pi}{4}$, and the polar representation is

$$
-1-i=\sqrt{2}\left(\cos \frac{5 \pi}{4}+i \sin \frac{5 \pi}{4}\right)
$$

The following properties of the argument were illustrated in Example 1(e) and (f) (for proofs, see Exercise 26):

$$
\begin{gathered}
\arg \bar{z}=-\arg z \\
\arg (-z)=\arg z+\pi
\end{gathered}
$$

It is tempting to compute the argument $\theta$ of a complex number $z=x+i y$ by taking the inverse tangent on both sides of (6) and writing $\theta=\tan ^{-1}\left(\frac{y}{x}\right)$. This formula is true only if $\theta$ is in the interval $\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$, because the inverse tangent takes its values in the interval $\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$ (see Figure 3); and so it will not yield values of $\theta$ that are outside this interval. For example, if $\theta=\frac{4 \pi}{3}$, from Table 1 we have $\tan \frac{4 \pi}{3}=\sqrt{3}$. However, $\tan ^{-1} \sqrt{3}=\frac{\pi}{3}$ and not $\frac{4 \pi}{3}$. To overcome this problem, recall that the tangent is $\pi$-periodic. That means, for all $\theta$,

$$
\tan \theta=\tan (\theta+k \pi) \quad(k=0, \pm 1, \pm 2, \ldots) .
$$

Also, since $\tan \theta=\frac{y}{x}$, we conclude that

$$
\theta=\tan ^{-1}\left(\frac{y}{x}\right)+k \pi \quad(x \neq 0),
$$

where the choice of $k$ depends on $z$. You can check that for $z=x+i y$ with $x \neq 0$,

$$
\operatorname{Arg} z= \begin{cases}\tan ^{-1}\left(\frac{y}{x}\right) & \text { if } x>0 \\ \tan ^{-1}\left(\frac{y}{x}\right)+\pi & \text { if } x<0 \text { and } y \geq 0 \\ \tan ^{-1}\left(\frac{y}{x}\right)-\pi & \text { if } x<0 \text { and } y<0\end{cases}
$$

For example, in Figure 4, the point $z_{1}=2+3 i$ is in the first quadrant. Using a calculator, we find $\operatorname{Arg} z_{1}=\tan ^{-1} \frac{3}{2} \approx 0.983$. The point $z_{2}=-2-3 i$, is in the third quadrant, $\operatorname{Arg} z_{2}=\tan ^{-1} \frac{3}{2}-\pi \approx-2.159$. (We remind you that all angles are measured in radians.)

When $x$ is zero, we cannot use (13). In this case,

$$
\operatorname{Arg} z=\operatorname{Arg}(i y)= \begin{cases}\frac{\pi}{2} & \text { if } y>0 \\ -\frac{\pi}{2} & \text { if } y<0\end{cases}
$$

![](13d4bcc6-f973-445e-ad7d-b22a7a43507d-27_497_509_1193_106.jpg)
Figure 5 To multiply in polar form, add the arguments and multiply the moduli.

## Multiplication, Inverses, and Division in Polar Form

The polar form of complex numbers gives us a new insight into multiplication and related operations on complex numbers. Let $z_{1}=r_{1}\left(\cos \theta_{1}+i \sin \theta_{1}\right)$ and $z_{2}=r_{2}\left(\cos \theta_{2}+i \sin \theta_{2}\right)$ be two nonzero complex numbers. We compute their product directly, using $i^{2}=-1$ :

$$
\begin{aligned}
z_{1} z_{2} & =r_{1}\left(\cos \theta_{1}+i \sin \theta_{1}\right) r_{2}\left(\cos \theta_{2}+i \sin \theta_{2}\right) \\
& =r_{1} r_{2}\left[\left(\cos \theta_{1} \cos \theta_{2}-\sin \theta_{1} \sin \theta_{2}\right)+i\left(\sin \theta_{1} \cos \theta_{2}+\cos \theta_{1} \sin \theta_{2}\right)\right]
\end{aligned}
$$

We recognize the trigonometric expressions as the sum angle formulas for the cosine and sine:

$$
\cos \left(\theta_{1}+\theta_{2}\right)=\cos \theta_{1} \cos \theta_{2}-\sin \theta_{1} \sin \theta_{2}
$$

and

$$
\sin \left(\theta_{1}+\theta_{2}\right)=\sin \theta_{1} \cos \theta_{2}+\cos \theta_{1} \sin \theta_{2} .
$$

Therefore, the polar form of the product

$$
z_{1} z_{2}=r_{1} r_{2}\left[\cos \left(\theta_{1}+\theta_{2}\right)+i \sin \left(\theta_{1}+\theta_{2}\right)\right] .
$$

By taking the modulus of both sides of (16), we have

$$
\left|z_{1} z_{2}\right|=\left|z_{1}\right|\left|z_{2}\right|
$$

which is a fact we already know from Section 1.2. By taking the argument of both sides of (16), we obtain

$$
\arg \left(z_{1} z_{2}\right)=\theta_{1}+\theta_{2}=\arg z_{1}+\arg z_{2} .
$$

More precisely,

$$
\arg \left(z_{1} z_{2}\right)=\left\{\theta_{1}+\theta_{2}+2 k \pi: k=0, \pm 1, \pm 2, \ldots\right\} .
$$

Identities (17) and (18) tell us that when we multiply two complex numbers in polar form, we multiply their moduli and add their arguments. See Figure 5.

Suppose that $z_{1} \neq 0$, and $z_{2}=z_{1}^{-1}$ in (16). Since $z_{1} z_{2}=z_{1} z_{1}^{-1}=1$, we obtain

$$
1=r_{1} r_{2}\left[\cos \left(\theta_{1}+\theta_{2}\right)+i \sin \left(\theta_{1}+\theta_{2}\right)\right] .
$$

Hence from (8), $r_{1} r_{2}=1$ and $\theta_{1}+\theta_{2}=0$, because the modulus of 1 is 1 and its argument is 0 . Hence $r_{2}=\frac{1}{r_{1}}$ and $\theta_{2}=-\theta_{1}$. So the polar form of the inverse of a complex number $z$ is given by

$$
z^{-1}=\frac{1}{r}(\cos (-\theta)+i \sin (-\theta))=\frac{1}{r}(\cos \theta-i \sin \theta) .
$$

![](13d4bcc6-f973-445e-ad7d-b22a7a43507d-28_490_559_239_101.jpg)
Figure 6 Division in polar form.

Consider now arbitrary $z_{1}$ and $z_{2} \neq 0$. Since $\frac{z_{1}}{z_{2}}=z_{1} z_{2}^{-1}$, then by (16) and (19), we obtain the polar form of a quotient

$$
\frac{z_{1}}{z_{2}}=\frac{r_{1}}{r_{2}}\left(\cos \left(\theta_{1}-\theta_{2}\right)+i \sin \left(\theta_{1}-\theta_{2}\right)\right)
$$

Thus to divide two complex numbers in polar form, we divide their moduli and subtract their arguments (Figure 6).

## EXAMPLE 2 Multiplication and division in polar form

(a) Let $z_{1}=3\left(\cos \frac{\pi}{4}+i \sin \frac{\pi}{4}\right)$ and $z_{2}=2\left(\cos \frac{5 \pi}{6}+i \sin \frac{5 \pi}{6}\right)$. Calculate $z_{1} z_{2}$.
(b) Let $z_{1}=5\left(\cos \frac{3 \pi}{4}+i \sin \frac{3 \pi}{4}\right)$ and $z_{2}=2 i$. Calculate $\frac{z_{1}}{z_{2}}$.

Solution (a) Reading off the values $r_{1}=3, \theta_{1}=\frac{\pi}{4}, r_{2}=2, \theta_{2}=\frac{5 \pi}{6}$, we use (16) and get

$$
\begin{aligned}
z_{1} z_{2} & =2 \cdot 3\left[\cos \left(\frac{\pi}{4}+\frac{5 \pi}{6}\right)+i \sin \left(\frac{\pi}{4}+\frac{5 \pi}{6}\right)\right] \\
& =6\left[\cos \frac{13 \pi}{12}+i \sin \frac{13 \pi}{12}\right]
\end{aligned}
$$

This is the multiplication shown in Figure 5.
(b) We write $z_{2}$ in polar form as $2 i=2\left(\cos \frac{\pi}{2}+i \sin \frac{\pi}{2}\right)$, then perform the division by dividing moduli and subtracting arguments:

$$
\begin{aligned}
\frac{z_{1}}{z_{2}} & =\frac{5}{2}\left[\cos \left(\frac{3 \pi}{4}-\frac{\pi}{2}\right)+i \sin \left(\frac{3 \pi}{4}-\frac{\pi}{2}\right)\right] \\
& =\frac{5}{2}\left(\cos \frac{\pi}{4}+i \sin \frac{\pi}{4}\right)=\frac{5}{2}\left(\frac{\sqrt{2}}{2}+i \frac{\sqrt{2}}{2}\right)
\end{aligned}
$$

This is the division shown in Figure 6.

## De Moivre's Identity

If we take the number $z=1(\cos \theta+i \sin \theta)$ and multiply it by itself, using (16), we get

$$
z z=(1 \cdot 1)[\cos (\theta+\theta)+i \sin (\theta+\theta)]=\cos 2 \theta+i \sin 2 \theta
$$

Computing successive powers of $z$, a pattern emerges:

$$
\begin{aligned}
z & =\cos \theta+i \sin \theta \\
z^{2} & =\cos 2 \theta+i \sin 2 \theta \\
z^{3} & =\cos 3 \theta+i \sin 3 \theta
\end{aligned}
$$

⋮

We have the following useful identity.

DE MOIVRE'S IDENTITY

For any positive integer $n$ and real number $\theta$,

$$
(\cos \theta+i \sin \theta)^{n}=\cos n \theta+i \sin n \theta .
$$

Proof We prove the statement by mathematical induction. For $n=1$, the statement is true, since we have trivially $(\cos \theta+i \sin \theta)^{1}=\cos 1 \cdot \theta+i \sin 1 \cdot \theta$. Now for the inductive step: We assume the statement is true for $n$, and prove that it is true for $n+1$. Let us compute

$$
\begin{aligned}
(\cos \theta+i \sin \theta)^{n+1} & =(\cos \theta+i \sin \theta)^{n}(\cos \theta+i \sin \theta) \\
& =(\cos n \theta+i \sin n \theta)(\cos \theta+i \sin \theta)
\end{aligned}
$$

[by induction hypothesis]

$$
=\cos (n+1) \theta+i \sin (n+1) \theta \quad[\text { by }(16)] .
$$

By induction, the statement holds for all positive integers $n$.
We can also use De Moivre's identity to calculate powers of complex numbers of arbitrary modulus $r \neq 0$. For if $z=r(\cos \theta+i \sin \theta)$, then

$$
\begin{aligned}
z^{n} & =[r(\cos \theta+i \sin \theta)]^{n} \\
& =r^{n}(\cos \theta+i \sin \theta)^{n} \\
& =r^{n}(\cos n \theta+i \sin n \theta)
\end{aligned}
$$

## EXAMPLE 3 Polar form and powers

Calculate $(2+2 i)^{11}$.
Solution We use De Moivre's identity for a quick calculation. First, write the number $2+2 i$ in polar form: $2+2 i=2^{3 / 2}\left(\cos \frac{\pi}{4}+i \sin \frac{\pi}{4}\right)$. Then, from (21) we obtain our answer in polar form:

$$
(2+2 i)^{11}=2^{33 / 2}\left(\cos \frac{11 \pi}{4}+i \sin \frac{11 \pi}{4}\right) .
$$

By subtracting a multiple of $2 \pi$ from the angle, we can simplify our answer and put it in Cartesian coordinates as follows:

$$
(2+2 i)^{11}=2^{16} \sqrt{2}\left(\cos \frac{3 \pi}{4}+i \sin \frac{3 \pi}{4}\right)=2^{16}(-1+i) .
$$

## EXAMPLE 4 Double-angle identities

Use De Moivre's identity with $n=2$ to recover the double-angle formulas for $\cos 2 \theta$ and $\sin 2 \theta$.

Solution From De Moivre's identity,

$$
\cos 2 \theta+i \sin 2 \theta=(\cos \theta+i \sin \theta)^{2}=\cos ^{2} \theta-\sin ^{2} \theta+i 2 \sin \theta \cos \theta .
$$

Equating real and imaginary parts, we get the double-angle formulas

$$
\cos 2 \theta=\cos ^{2} \theta-\sin ^{2} \theta \quad \text { and } \quad \sin 2 \theta=2 \sin \theta \cos \theta
$$

## Roots of Complex Numbers

We first define an $n$th root of a complex number.

## DEFINITION OF $n$th ROOT

## Let $w \neq 0$ be a given complex number and $n$ a positive integer. A number $z$ is called an $n$th root of $w$ if $z^{n}=w$.

Our goal is to find the roots of the given number $w$. De Moivre's formula for calculating powers can in essence be worked "backward" to find roots of complex numbers.

Write $w=\rho(\cos \phi+i \sin \phi)$ and $z=r(\cos \theta+i \sin \theta)$. The equation $z^{n}=w$ tells us (using (21)) that

$$
r^{n}(\cos n \theta+i \sin n \theta)=\rho(\cos \phi+i \sin \phi)
$$

Two complex numbers are equal only if their moduli are equal, so $r^{n}=\rho$. Thus, take $r=\rho^{1 / n}$ (meaning the real root of a real number). Also, when two complex numbers are equal, their arguments must differ by $2 k \pi$, where $k$ is an integer. So

$$
n \theta=\phi+2 k \pi, \quad \text { or } \quad \theta=\frac{\phi}{n}+\frac{2 k \pi}{n} .
$$

If we take the values $k=0,1, \ldots, n-1$, we will get $n$ values of $\theta$ that yield $n$ distinct roots of $w$. Any other value of $k$ will produce a root identical to one of these, since when $k$ increases by $n$, the argument of $z$ increases by $2 \pi$. Thus we have a formula for the $n$ roots of a complex number $w$.

## FORMULA FOR THE $\boldsymbol{n}$ th ROOTS

Let $w=\rho(\cos \phi+i \sin \phi) \neq 0$. The $n$th roots of $w$ are the solutions of the equation $z^{n}=w$. They are given by

$$
z_{k+1}=\rho^{1 / n}\left[\cos \left(\frac{\phi}{n}+\frac{2 k \pi}{n}\right)+i \sin \left(\frac{\phi}{n}+\frac{2 k \pi}{n}\right)\right]
$$

$k=0,1, \ldots, n-1$.
The unique number $z$ such that $z^{n}=w$ and $\operatorname{Arg} z=\frac{\operatorname{Arg} w}{n}$ is called the principal $n$th root of $w$. The principal root is obtained from (23) by taking $\phi=\operatorname{Arg} w$ and $k=0$.

![](13d4bcc6-f973-445e-ad7d-b22a7a43507d-31_466_508_454_118.jpg)
Figure 7 Sixth roots of unity.

![](13d4bcc6-f973-445e-ad7d-b22a7a43507d-31_474_505_1433_108.jpg)
Figure 8 Solutions in Example 6.

## EXAMPLE 5 Sixth roots of unity

Find and plot all numbers $z$ such that $z^{6}=1$. What is the principal sixth root of 1?

Solution The modulus of 1 is 1 and the argument of 1 is 0 . According to (23), the six roots have $r=1^{1 / 6}=1$ and $\theta=\frac{0}{6}+\frac{k \pi}{3}$, for $k=0,1,2,3,4$, and 5 . Hence the roots are

$$
z_{k+1}=\cos \frac{k \pi}{3}+i \sin \frac{k \pi}{3}, k=0,1, \ldots, 5 .
$$

The principal root is clearly $z_{1}=1$. We can list the roots explicitly, with the help of Table 1:

$$
\begin{aligned}
& z_{1}=1, \quad z_{2}=\frac{1}{2}+i \frac{\sqrt{3}}{2}, \quad z_{3}=-\frac{1}{2}+i \frac{\sqrt{3}}{2} \\
& z_{4}=-1, \quad z_{5}=-\frac{1}{2}-i \frac{\sqrt{3}}{2}, \quad z_{6}=\frac{1}{2}-i \frac{\sqrt{3}}{2}
\end{aligned}
$$

The six roots are displayed in Figure 7. Since they all have the same modulus, they all lie on the same circle centered at the origin. They have a common angular separation of $\pi / 3$. This particular set of roots is symmetric about the horizontal axis because we are finding the roots of a real number; the polynomial equation $z^{6}=1$ has real coefficients, and nonreal solutions come in conjugate pairs (see Section 1, Exercise 29).

## EXAMPLE 6 Finding roots of complex numbers

Find and plot all numbers $z$ such that $(z+1)^{3}=2+2 i$.
Solution Change variables to $w=z+1$. We must now solve $w^{3}=2+2 i$. The polar form of $2+2 i$ is $2+2 i=2^{3 / 2}\left(\cos \frac{\pi}{4}+i \sin \frac{\pi}{4}\right)$. Appealing to ( 23 ) with $n=3$, we find

$$
\begin{gathered}
w_{1}=\sqrt{2}\left(\cos \frac{\pi}{12}+i \sin \frac{\pi}{12}\right), \quad w_{2}=\sqrt{2}\left(\cos \frac{9 \pi}{12}+i \sin \frac{9 \pi}{12}\right) \\
w_{3}=\sqrt{2}\left(\cos \frac{17 \pi}{12}+i \sin \frac{17 \pi}{12}\right)
\end{gathered}
$$

Since $z=w-1$, we conclude that the solutions $z_{1}, z_{2}$, and $z_{3}$, of $(z+1)^{3}=2+2 i$, are

$$
\begin{gathered}
z_{1}=\sqrt{2} \cos \frac{\pi}{12}-1+i \sqrt{2} \sin \frac{\pi}{12}, \quad z_{2}=\sqrt{2} \cos \frac{9 \pi}{12}-1+i \sqrt{2} \sin \frac{9 \pi}{12} \\
z_{3}=\sqrt{2} \cos \frac{17 \pi}{12}-1+i \sqrt{2} \sin \frac{17 \pi}{12}
\end{gathered}
$$

The solutions are illustrated in Figure 8.
As a final application, we revisit the quadratic equation

$$
a z^{2}+b z+c=0 \quad(a \neq 0)
$$

where $a, b, c$ are now complex numbers. Following the algebraic manipulations in Section 1.1 for solving the equation with real coefficients, we arrive
at the solution

$$
z=\frac{-b \pm \sqrt{b^{2}-4 a c}}{2 a}
$$

where now $\pm \sqrt{b^{2}-4 a c}$ represents the two complex square roots of $b^{2}-4 a c$. These square roots can be computed by appealing to (23) with $n=2$, thus yielding the solutions of (24).

## EXAMPLE 7 Quadratic equation with complex coefficients

Solve $z^{2}-2 i z+3+i=0$.
Solution From (25), we have

$$
z=\frac{2 i \pm \sqrt{(-2 i)^{2}-4(3+i)}}{2}=i \pm \sqrt{-4-i} .
$$

We have

$$
-4-i=\sqrt{17}\left(-\frac{4}{\sqrt{17}}-\frac{i}{\sqrt{17}}\right)=\sqrt{17}(\cos \theta+i \sin \theta),
$$

where $\theta$ is the angle in the third quadrant (we may take $\pi<\theta<\frac{3 \pi}{2}$ ) such that

$$
\cos \theta=-\frac{4}{\sqrt{17}}, \quad \text { and } \quad \sin \theta=-\frac{1}{\sqrt{17}}
$$

Appealing to (23) to compute $w_{1}$ and $w_{2}$, the two square roots of $-4-i$, we find

$$
w_{1}=17^{1 / 4}\left(\cos \frac{\theta}{2}+i \sin \frac{\theta}{2}\right)
$$

and

$$
\begin{aligned}
w_{2} & =17^{1 / 4}\left(\cos \left(\frac{\theta}{2}+\pi\right)+i \sin \left(\frac{\theta}{2}+\pi\right)\right) \\
& =17^{1 / 4}\left(-\cos \frac{\theta}{2}-i \sin \frac{\theta}{2}\right)=-w_{1}
\end{aligned}
$$

as you would have expected $w_{2}$ to be related to $w_{1}$. Thus,

$$
z_{1}=i+w_{1} \quad \text { and } \quad z_{2}=i-w_{1} .
$$

To compute $z_{1}$ and $z_{2}$ explicitly, we must determine the values of $\cos \frac{\theta}{2}$ and $\sin \frac{\theta}{2}$ from the values of $\cos \theta$ and $\sin \theta$. This can be done with the help of the half-angle formulas:

$$
\cos ^{2} \frac{\theta}{2}=\frac{1+\cos \theta}{2} \text { and } \sin ^{2} \frac{\theta}{2}=\frac{1-\cos \theta}{2} .
$$

Since $\pi<\theta<\frac{3 \pi}{2}$, we have $\frac{\pi}{2}<\frac{\theta}{2}<\frac{3 \pi}{4}$; so $\cos \frac{\theta}{2}<0$ and $\sin \frac{\theta}{2}>0$. Hence from (26)

$$
\cos \frac{\theta}{2}=-\sqrt{\frac{1+\cos \theta}{2}} \text { and } \sin \frac{\theta}{2}=\sqrt{\frac{1-\cos \theta}{2}} .
$$

Using the explicit value of $\cos \theta$, we get

$$
\cos \frac{\theta}{2}=-\sqrt{\frac{\sqrt{17}-4}{2 \sqrt{17}}} \quad \text { and } \quad \sin \frac{\theta}{2}=\sqrt{\frac{\sqrt{17}+4}{2 \sqrt{17}}},
$$

and hence

$$
\begin{aligned}
& z_{1}=i+\frac{1}{\sqrt{2}}[-\sqrt{\sqrt{17}-4}+i \sqrt{\sqrt{17}+4}], \\
& z_{2}=i-\frac{1}{\sqrt{2}}[-\sqrt{\sqrt{17}-4}+i \sqrt{\sqrt{17}+4}] .
\end{aligned}
$$

Observe that the roots $z_{1}$ and $z_{2}$ are not complex conjugates. This is because the coefficients of the quadratic equation were not all real (see Exercise 29(b), Section 1.1).

## Exercises 1.3

In Exercises 1-4, draw the complex number, given in its polar form.

1. $3\left(\cos \frac{7 \pi}{12}+i \sin \frac{7 \pi}{12}\right)$.
2. $\quad \sqrt{2}\left(\cos \frac{-\pi}{2}+i \sin \frac{-\pi}{2}\right)$.
3. $\frac{1}{2}\left(\cos \frac{64 \pi}{3}+i \sin \frac{64 \pi}{3}\right)$.
4. $3\left(\cos \frac{-72 \pi}{11}+i \sin \frac{-72 \pi}{11}\right)$.

In Exercises 5-12, represent the given number in polar form.
5. $-3-3 i$.
6. $-\frac{\sqrt{3}}{2}+\frac{i}{2}$.
7. $-1-\sqrt{3} i$.
8. $1+i$.
9. $-\frac{i}{2}$.
10. $\frac{1+i}{1+\sqrt{3} i}$.
11. $\frac{1+i}{1-i}$.
12. $\frac{i}{10+10 i}$.

In Exercises 13-16, you are given a complex number $z$. Find $\operatorname{Arg} z$ with the help of (14) or (15); then find $\arg z$. If needed, use a calculator to compute $\tan ^{-1}$.
13. $13+2 i$.
14. $-3-32 i$.
15. $-1+\frac{1}{2} i$.
16. $-\frac{3 \pi}{2} i$.

In Exercises 17-20, find the polar form of the given number.
17. $(-\sqrt{3}+i)^{3}$.
18. $(-2-3 i)^{17}$.
19. $\left(\frac{1-i}{1+i}\right)^{10}$.
20. $\frac{i}{(1+2 \sqrt{3} i)^{5}}$.

In Exercises 21-24, find the real and imaginary parts of the given number.
21. $(1+i)^{30}$.
22. $\left(\cos \frac{2 \pi}{17}+i \sin \frac{2 \pi}{17}\right)^{170}$.
23. $\left(\frac{1-i}{1+i}\right)^{4}$.
24. $\frac{-i}{(1+i)^{5}}$.
25. What are the real and imaginary parts of $i^{n}$, where $n$ is an integer?
26. Prove (11) and (12).
27. Show that

$$
\left(\frac{1+i \tan \theta}{1-i \tan \theta}\right)^{n}=\frac{1+i \tan n \theta}{1-i \tan n \theta}
$$

28. Show that $\bar{z}$ and $z^{-1}$ are parallel, using their polar forms. Find the positive constant $\alpha$ such that $\bar{z}=\alpha z^{-1}$.
29. Suppose $z_{1}, z_{2}, \ldots, z_{n}$ are complex numbers with respective moduli $r_{1}, r_{2}$, $\ldots, r_{n}$ and arguments $\theta_{1}, \theta_{2}, \ldots, \theta_{n}$. Show that

$$
z_{1} z_{2} \cdots z_{n}=r_{1} r_{2} \cdots r_{n}\left[\cos \left(\theta_{1}+\theta_{2}+\cdots+\theta_{n}\right)+i \sin \left(\theta_{1}+\theta_{2}+\cdots+\theta_{n}\right)\right]
$$

30. (a) Show that if $z_{1}, z_{2}, \ldots, z_{n}$ are all unimodular, then so is $z_{1} z_{2} \cdots z_{n}$.
(b) Let $n$ be a positive integer and $z$ a nonzero complex number. Show that $z$ is unimodular if and only if all its $n$th roots are unimodular.
31. (a) Show that two nonzero complex numbers $z_{1}$ and $z_{2}$ represent perpendicular vectors only if $\arg \left(\frac{z_{1}}{z_{2}}\right)=\frac{\pi}{2}+k \pi$, where $k$ is an integer.
(b) Show that two nonzero complex numbers $z_{1}$ and $z_{2}$ represent parallel vectors only if $\arg \left(\frac{z_{1}}{z_{2}}\right)=2 k \pi$, where $k$ is an integer.
32. Suppose $z=r(\cos \theta+i \sin \theta)$. What become of its polar coordinates $r$ and $\theta$ if we multiply it by
(a) a positive real number $\alpha$ ?
(b) a negative real number $-\alpha$ ?
(c) a unimodular complex number $\cos \phi+i \sin \phi$ ?

In Exercises 33-38, solve the given equation and plot the solutions. In each case, determine the principal root.
33. $z^{4}=i$.
34. $z^{3}=1+i$.
35. $z^{6}=128$.
36. $z^{5}=-30$.
37. $z^{7}=-1$.
38. $z^{8}=-\frac{\pi}{2}$.

In Exercises 39-42, solve the given equation.
39. $(z+2)^{3}=3 i$.
40. $(z-i)^{4}=1$.
41. $(z-5)^{3}=-125$.
42. $(3 z-2)^{4}=11$.

In Exercises 43-46, solve the given equation.
43. $z^{2}-2(1+i) z+i=0$.
44. $2 z^{2}-z-1-i=0$.
45. $z^{2}+z+\frac{i}{4}=0$.
46. $z^{2}+i z+1=0$.

In Exercises 47-50, use De Moivre's identity to derive the given trigonometric identity. (More generally, see Exercise 56.)
47. $\cos (3 \theta)=\cos ^{3} \theta-3 \cos \theta \sin ^{2} \theta$.
48. $\sin (3 \theta)=3 \cos ^{2} \theta \sin \theta-\sin ^{3} \theta$.
49. $\cos (4 \theta)=\cos ^{4} \theta-6 \cos ^{2} \theta \sin ^{2} \theta+\sin ^{4} \theta$.
50. $\sin (4 \theta)=4 \cos ^{3} \theta \sin \theta-4 \cos \theta \sin ^{3} \theta$.
51. Roots of unity. Let $n$ be a positive integer. Solve $z^{n}=1$. These $n$ values of $z$ are called the $n$th roots of unity and are denoted by $\omega_{1}, \ldots, \omega_{n}$.
52. Use the fact that

$$
\cos \left(\frac{\phi}{n}+\frac{2 k \pi}{n}\right)+i \sin \left(\frac{\phi}{n}+\frac{2 k \pi}{n}\right)=\left[\cos \left(\frac{\phi}{n}\right)+i \sin \left(\frac{\phi}{n}\right)\right]\left[\cos \left(\frac{2 k \pi}{n}\right)+i \sin \left(\frac{2 k \pi}{n}\right)\right]
$$

to show that the roots of the equation $z^{n}=w$ are $w_{p}^{1 / n} \omega_{j}$ where $w_{p}^{1 / n}$ is the principal root of $w$ and $\omega_{j}$ is an $n$th root of unity, $j=1,2, \ldots, n$.
53. Summing roots of unity. Let $\omega_{1}, \omega_{2}, \ldots, \omega_{n}$ denote the $n$th roots of unity where $n \geq 2$; that is $\omega_{j}^{n}=1$ for $j=1,2, \ldots, n$. Pick and fix any root $\omega_{0} \neq 1$ from the set $\left(\omega_{j}\right)_{j=1}^{n}$.
(a) Show that $\omega_{0} \omega_{j}$ is an $n$th root of unity for $j=1,2, \ldots, n$. [Hint: Verify the equation $z^{n}=1$.]
(b) Show that $\omega_{0} \omega_{j} \neq \omega_{0} \omega_{k}$ if $j \neq k$. Conclude that the set $\left(\omega_{0} \omega_{j}\right)_{j=1}^{n}$ is the same as the set of all $n$ roots of unity.
(c) Show that the sum of the $n$ roots of unity is zero. That is, show that

$$
\omega_{1}+\omega_{2}+\cdots+\omega_{n}=0 .
$$

[Hint: $\omega_{1}+\omega_{2}+\cdots+\omega_{n}=\omega_{0} \omega_{1}+\omega_{0} \omega_{2}+\cdots+\omega_{0} \omega_{n}$; why? Factor $\omega_{0}$ and conclude that the sum has to be 0 .]
(d) Show directly that

$$
1+\omega_{0}+\omega_{0}^{2}+\cdots+\omega_{0}^{n-1}=0 .
$$

[Hint: Multiply the left side by $1-\omega_{0} \neq 0$.]
54. Project Problem. Our goal in this exercise is to solve the equation

$$
z^{n}=(z+1)^{n} .
$$

This polynomial equation is actually of order $n-1$, since upon expanding, the terms in $z^{n}$ will cancel.
(a) Divide both sides of (27) by $(z+1)^{n}$ (evidently, $z+1$ cannot be zero) and conclude that $\frac{z}{z+1}$ must be one of the $n$th roots of unity (see Exercise 51). Hence $z=(z+1) \omega_{k}$, where $\omega_{k}=\cos \left(\frac{2 k \pi}{n}\right)+i \sin \left(\frac{2 k \pi}{n}\right)$, for $k=1,2, \ldots, n-1$. We must throw out $k=0$ because $z=z+1$ cannot be correct.
(b) Write $z=x+i y$ and solve for $x$ and $y$ by equating real and imaginary parts in $z=(z+1) \omega_{k}$. Obtain the answers

$$
x=-\frac{1}{2} \quad \text { and } \quad y_{k}=\frac{\sin (2 k \pi / n)}{2(1-\cos (2 k \pi / n))}=\frac{1}{2} \cot (k \pi / n) .
$$

(c) Apply the result of (b) to solve $(z+1)^{7}=z^{7}$.

## Chebyshev Polynomials

In the remaining problems, we present a family of polynomials, known as the Chebyshev polynomials. These polynomials have useful applications in numerical analysis. Our presentation will use De Moivre's identity and the following well-known formula.
55. The binomial formula. Use mathematical induction to prove that for any complex numbers $a$ and $b$ and any positive integer $n$

$$
(a+b)^{n}=a^{n}+\binom{n}{1} a^{n-1} b^{1}+\binom{n}{2} a^{n-2} b^{2}+\cdots+\binom{n}{n-1} a^{1} b^{n-1}+b^{n},
$$

where for $0 \leq m \leq n$, the binomial coefficient $\binom{n}{m}$ (read it " $n$ choose $m$ ") is defined by

$$
\binom{n}{m}=\frac{n!}{(n-m)!m!},
$$

with $0!=1$ as a convention. Using the summation notation, the binomial formula becomes

$$
(a+b)^{n}=\sum_{m=0}^{n}\binom{n}{m} a^{n-m} b^{m}
$$

[Hint: You should come up with two sums. Shift the index on one summation so the summand looks like the other. Pull off the $a^{n+1}$ and $b^{n+1}$ terms. Then use the identity of Pascal's triangle,

$$
\left.\binom{n}{m-1}+\binom{n}{m}=\binom{n+1}{m} \cdot\right]
$$

56. (a) Use De Moivre's identity and the binomial formula to show that, for $n=1,2, \ldots$,

$$
\cos n \theta=\sum_{k=0}^{\left[\frac{n}{2}\right]}\binom{n}{2 k}(\cos \theta)^{n-2 k}(-1)^{k}(\sin \theta)^{2 k}
$$

and

$$
\sin n \theta=\sum_{k=0}^{\left[\frac{n-1}{2}\right]}\binom{n}{2 k+1}(\cos \theta)^{n-2 k-1}(-1)^{k}(\sin \theta)^{2 k+1},
$$

where, for a real number $s,[s]$ denotes the greatest integer not larger than $s$.
(b) Show that

$$
\cos n \theta=\sum_{k=0}^{\left[\frac{n}{2}\right]}\binom{n}{2 k}(\cos \theta)^{n-2 k}(-1)^{k}\left(1-\cos ^{2} \theta\right)^{k}
$$

(c) Derive the results of Exercises 47 and 48 from (a).

With the Roman alphabet, Chebyshev may be spelled a variety of ways, including Tchebichef. Hence $T_{n}$.
57. Chebyshev polynomials. It is clear from (31) that $\cos n \theta$ can be expressed as a polynomial of degree $n$ in $\cos \theta$. So, for $n=0,1,2, \ldots$, we define the $n$th Chebyshev polynomial $T_{n}$ by the formula

$$
T_{n}(\cos \theta)=\cos n \theta, \quad n=0,1,2, \ldots .
$$

(a) Obtain the formula

$$
T_{n}(x)=\sum_{k=0}^{\left[\frac{n}{2}\right]}\binom{n}{2 k}(-1)^{k} x^{n-2 k}\left(1-x^{2}\right)^{k}
$$

(b) Use (33) to derive the following list of Chebyshev polynomials:

$$
\begin{array}{lll}
T_{0}(x)=1, & T_{1}(x)=x, & T_{2}(x)=-1+2 x^{2} \\
T_{3}(x)=-3 x+4 x^{3}, & T_{4}(x)=1-8 x^{2}+8 x^{4}, & T_{5}(x)=5 x-20 x^{3}+16 x^{5}
\end{array}
$$

58. Properties of the Chebyshev polynomials. Derive the following properties of Chebyshev polynomials. These properties are characteristic of many other families of functions that we will encounter when solving important differential equations such as the Legendre, Laguerre, and Bessel differential equations.
(a) $\quad T_{n}(1)=1$ and $T_{n}(-1)=(-1)^{n}$.
(b) $T_{n}(0)=\cos \left(\frac{n \pi}{2}\right)=0$ if $n$ is odd and $(-1)^{k}$ if $n=2 k$.
(c) $\left|T_{n}(x)\right| \leq 1$ for all $x$ in $[-1,1]$.
(d) $T_{n}(x)$ is a polynomial of degree $n$. [Hint: Induction on $n$ and (33).]
(e) Derive the recurrence relation $T_{n+1}(x)+T_{n-1}(x)=2 x T_{n}(x)$. [Hint: Use the trigonometric identities $\cos (a \pm b)=\cos a \cos b \mp \sin a \sin b$ and (32).]
(f) Show that $T_{n}(x)$ has $n$ simple zeros in $[-1,1]$ at the points $\alpha_{k}=\cos \left(\frac{2 k-1}{2 n} \pi\right)$, $k=1,2, \ldots, n$.
(g) Show that $T_{n}(x)$ assumes its absolute extrema in $[-1,1]$ at the points $\beta_{k}= \cos \left(\frac{k}{n} \pi\right), k=0,1,2, \ldots, n$, with $T_{n}\left(\beta_{k}\right)=(-1)^{k}$.
(h) Illustrate graphically your answers in (f) and (g) by plotting the first ten Chebyshev polynomials.
(i) Show that for $m \neq n$

$$
\int_{-1}^{1} T_{m}(x) T_{n}(x) \frac{d x}{\sqrt{1-x^{2}}}=0
$$

[Hint: Change variables: $x=\cos \theta$.]
(j) Show that for $n=0,1,2, \ldots$,

$$
\int_{-1}^{1}\left[T_{n}(x)\right]^{2} \frac{d x}{\sqrt{1-x^{2}}}= \begin{cases}\pi & \text { if } n=0 \\ \frac{\pi}{2} & \text { if } n \geq 1\end{cases}
$$

### 1.4 Complex Functions

So far we have introduced complex numbers, both in Cartesian and polar forms, and we have studied their algebraic and geometric properties. We now move to the topic of functions of a complex variable.

A complex-valued function $f$ of a complex variable $z$ is a rule that assigns to each complex number $z$ in a set $S$ a complex number $f(z)$. The set $S$ is a subset of the complex numbers and is called the domain of definition of $f$. The complex number $f(z)$ is called the value of $f$ at $z$ and is sometimes written $w=f(z)$. For example the function $f(z)=z^{3}$ is a rule that assigns to each $z$ the complex number $w=z^{3}$. When a function is given by a formula and the domain is not specified, the domain is taken to be the largest set on which the formula makes sense. In the case $f(z)=z^{3}$, the domain is the set of all complex numbers $\mathbb{C}$.

Back in calculus, a real-valued function $y=g(x)$ of a real variable $x$ was represented as a graph in the $x y$-plane. The graph contains vital information about the function and allows us to easily visualize and deduce properties of $g(x)$. In the complex case, we are not as fortunate. To visualize a complex-valued function $f(z)$ requires four dimensions: two dimensions for the variable $z$ and two for the values $w=f(z)$. Since a four-dimensional

Figure 1 To visualize a mapping by a complex-valued function $w=f(z)$, we use two planes: the $z$ - or $x y$-plane for the domain of definition and the $w$ - or $u v$-plane for the image.

Figure 2 A translation is a mapping of the form $f(z)= z+b$, where $b$ is a complex number. In Example 1, $b= 2+i$.
picture is not practical, instead we will use two planes, the $z$-plane and the $w$-plane, and visualize the function as a mapping from a subset of one plane to the other (see Figure 1). As usual, we will write $z=x+i y$, and also write $w=u+i v$. Thus as a convention, the $z$-plane axes will be labeled by $x$ and $y$ and those of the $w$-plane by $u$ and $v$. The image $f[S]$ of a set S under a mapping $f$ is the set of all points $w$ such that $w=f(z)$ for some $z$ in $S$. We illustrate the mapping process with basic examples including some familiar geometric transformations.
![](13d4bcc6-f973-445e-ad7d-b22a7a43507d-38_507_1299_643_762.jpg)

## EXAMPLE 1 Translation

Let $S$ denote the disk

$$
S=\{z:|z| \leq 1\}
$$

Find the image of $S$ under the mapping $f(z)=z+2+i$.
Solution For any $z$ in $S$, the number $f(z)$ is found by adding $z$ to $2+i$ as vectors. Hence the function translates the point $z$ two units to the right and one unit up. The image of $S$, then, is the set $S$ translated two units to the right and one unit up (see Figure 2).
![](13d4bcc6-f973-445e-ad7d-b22a7a43507d-38_424_1093_1727_797.jpg)

Consequently, the image of the disk is a disk of the same radius, centered at $2+i$ (the image of the original center). Hence,

$$
f[S]=\{w:|w-2-i| \leq 1\} .
$$

Our next example deals with functions of the form $f(z)=a z$, where ${ }^{a}$ is a complex constant. To understand these mappings, recall that when we

Figure 3 Images of the corners are computed explicitly using the formula for $f$ :

$$
\begin{aligned}
& f(1+i)=3+3 i \\
& f(1-i)=3-3 i \\
& f(3+i)=9+3 i \\
& f(3-i)=9-3 i
\end{aligned}
$$

They form the corners of the image.

Figure 4 The mapping $g(z)=2 i z$ is a composition of two mappings: a dilation by a factor of 2 , followed by a counterclockwise rotation by an angle of $\pi / 2$. The angle of rotation is the argument of $2 i$.
multiply two complex numbers in polar form, we multiply their moduli and add their arguments. Writing $a$ in polar form as $a=r(\cos \theta+i \sin \theta)$, we see that the mapping $f(z)=r(\cos \theta+i \sin \theta) z$ has two effects: It multiplies the modulus of $z$ by $r>0$ (a dilation) and adds $\theta$ to the argument of $z$ (a rotation). Since multiplication is commutative, these operations of dilation and rotation may be applied in either order. When $r=1$, we obtain the mapping $f(z)=(\cos \theta+i \sin \theta) z$, which is a rotation by the angle $\theta$. Mappings of the form $f(z)=r z$, where $r>0$, are dilations by a factor $r$.

## EXAMPLE 2 Dilations and rotations

Let $S$ be the points lying inside and on the square of side length 2 centered at the point 2 on the real axis (Figure 3).
(a) What is the image of $S$ under the mapping $f(z)=3 z$ ?
(b) What is the image of $S$ under the mapping $g(z)=2 i z$ ?

Solution (a) For any $z$ in $S, f(z)=3 z$ has the effect of tripling the modulus and leaving the argument unchanged. Hence $f(z)$ lies on the ray extending from the origin to $z$, at three times the distance from the origin to $z$. In particular, the image of the square is a square whose corners are the images of the four original corners. It is easy to see from Figure 3 that the image of $S$ is a square of side length 6 , centered at the point 6 on the real axis.
![](13d4bcc6-f973-445e-ad7d-b22a7a43507d-39_388_1047_1265_763.jpg)
(b) In polar form, we have $i=\cos \frac{\pi}{2}+i \sin \frac{\pi}{2}$, and so $g(z)=2\left(\cos \frac{\pi}{2}+i \sin \frac{\pi}{2}\right) z$. Hence for any $z$ in $S, g(z)$ has the effect of doubling the modulus and adding $\frac{\pi}{2}$ to the argument. To determine $f[S]$, take the set $S$, dilate it by a factor of 2 , then rotate it counterclockwise by $\pi / 2$ (Figure 4).
![](13d4bcc6-f973-445e-ad7d-b22a7a43507d-39_394_931_1943_753.jpg)

Figure 5 The inversion

$$
w=\frac{1}{z}
$$

has the effect of inverting the modulus and changing the sign of the argument:

$$
\begin{aligned}
& |w|=\frac{1}{|z|} \\
& \operatorname{Arg} w=-\operatorname{Arg} z .
\end{aligned}
$$

Examples 1 and 2 deal with mappings of the type $f(z)=a z+b$, where $a$ and $b$ are complex constants and $a \neq 0$. These are called linear transformations and can always be thought of in terms of a dilation, a rotation, and a translation. These transformations map regions to geometrically similar regions. It is important that $a \neq 0$ because otherwise the transformation would be a constant. The transformation $f(z)=z$ is called the identity transformation for obvious reasons. The next transformation is not linear.

## EXAMPLE 3 Inversion

Find the image of the following sets under the mapping $f(z)=1 / z$.
(a) $S=\{z: 0<|z|<1,0 \leq \arg z \leq \pi / 2\}$.
(b) $S=\{z: 2 \leq|z|, 0 \leq \arg z \leq \pi\}$.

Solution (a) From (19) in Section 1.3, we know that for $z=r(\cos \theta+i \sin \theta) \neq$ 0 , we have

$$
\frac{1}{z}=\frac{1}{r}(\cos (-\theta)+i \sin (-\theta)) .
$$

According to this formula, the modulus of the number $f(z)$ is the reciprocal of the modulus of $z$ and the argument of $f(z)$ is the negative of the argument of $z$. Consequently, numbers inside the unit circle $(|z| \leq 1)$ get mapped to numbers outside the unit circle $\left(\frac{1}{|z|} \geq 1\right)$, and numbers in the upper half-plane get mapped to numbers in the lower half-plane. Looking at $S$, as the modulus of $z$ goes from 1 down to 0 , the modulus of $f(z)$ goes from 1 up to infinity. As the argument of $z$ goes from 0 up to $\pi / 2$, the argument of $1 / z$ goes from 0 down to $-\pi / 2$. Hence $f[S]$ is the set of all points in the fourth quadrant, including the border axes, that lie outside the unit circle (see Figure 5):

$$
f[S]=\{w: 1<|w|,-\pi / 2 \leq \arg z \leq 0\} .
$$

![](13d4bcc6-f973-445e-ad7d-b22a7a43507d-40_380_981_1841_810.jpg)
(b) As the modulus of $z$ increases from 2 up to infinity, the modulus of $1 / z$ decreases from $1 / 2$ down to zero (but never equals zero). As the argument of $z$ goes from 0 up to $\pi$, the argument of $1 / z$ goes from 0 down to $-\pi$. Hence $f[S]$ is the set of points in the lower half-plane, including the real axis, with $0<|w|<1 / 2$ (see Figure 6): $f[S]=\{w: 0<|w|<1 / 2,-\pi \leq \arg z \leq 0\}$.

Figure 6 Under the inversion

$$
f(z)=\frac{1}{z},
$$

points outside the circle of radius $2,|z| \geq 2$, get mapped to points inside the circle of radius $\frac{1}{2},|w| \leq \frac{1}{2}$.
![](13d4bcc6-f973-445e-ad7d-b22a7a43507d-41_414_1017_208_782.jpg)

The function $f(z)=\frac{1}{z}$ in Example 3 is a special case of a general type of mapping of the form

$$
w=\frac{a z+b}{c z+d} \quad(a d \neq b c)
$$

known as a linear fractional transformation, also known as a bilinear transformation or Möbius transformation. Here $a, b, c, d$ are complex numbers, and you can check that when $a d=b c, w$ is constant. Linear fractional transformations are studied extensively in Chapter 6. They have many important applications that will occur throughout the book.

## Real and Imaginary Parts of Functions

Given a complex function $f(z)$, let $u(z)=\operatorname{Re} f(z)$ and $v(z)=\operatorname{Im} f(z)$. The functions $u$ and $v$ are real-valued functions, and we may think of them as functions of two real variables. With a slight abuse of notation, we will sometime write $u(z)=u(x+i y)=u(x, y)$, and $v(z)=v(x+i y)=v(x, y)$. Thus

$$
f(z)=f(x+i y)=u(x, y)+i v(x, y) .
$$

For example, for $f(z)=z^{2}=(x+i y)^{2}=x^{2}-y^{2}+2 i x y$, we have

$$
u(x, y)=x^{2}-y^{2} \quad \text { and } \quad v(x, y)=2 x y .
$$

As we now illustrate, the functions $u(x, y)$ and $v(x, y)$ may be used to determine algebraically the image of a set when the answer is not geometrically obvious.

## EXAMPLE 4 Squaring

Let $S$ be the vertical strip

$$
S=\{z=x+i y: 1 \leq x \leq 2\} .
$$

Find the image of $S$ under the mapping $f(z)=z^{2}$.
Solution As before, write $f(z)=z^{2}=x^{2}-y^{2}+2 i x y$. Thus the real part of $f(z)$ is $u(x, y)=x^{2}-y^{2}$ and the imaginary part of $f(z)$ is $v(x, y)=2 x y$. Let us
fix $1 \leq x_{0} \leq 2$, and find the image of the vertical line $x=x_{0}$. A point $\left(x_{0}, y\right)$ on the line maps to the point $(u, v)$, where $u=x_{0}^{2}-y^{2}, v=2 x_{0} y$. To determine the equation of the curve that is traced by the point $(u, v)$ as $y$ varies from $-\infty$ to $\infty$, we will eliminate $y$ and get an algebraic relation between $u$ and $v$. From $v=2 x_{0 y}$, we obtain $y=\frac{v}{2 x_{0}}$. Plugging into the expression for $u$, we obtain

$$
u=x_{0}^{2}-\frac{v^{2}}{4 x_{0}^{2}}
$$

This gives $u$ as a quadratic function of $v$. Hence the graph is a leftward-facing parabola with a vertex at $(u, v)=\left(x_{0}^{2}, 0\right)$ and $v$-intercepts at $\left(0, \pm 2 x_{0}^{2}\right)$. As $x_{0}$ ranges from 1 up to 2 , the corresponding parabolas in the $w$-plane sweep out a parabolic region, which is described as follows (see Figure 7). Since all points lie to the right of the parabola, where $x_{0}=1$, and to the left of the parabola, where $x_{0}=2$, we have

$$
f[S]=\left\{w=u+i v: 1-\frac{v^{2}}{4} \leq u \leq 4-\frac{v^{2}}{16}\right\}
$$

Figure 7 For $1 \leq x_{0} \leq 2$, the image of a line $x=x_{0}$ under the mapping $f(z)=z^{2}$ is a parabola

$$
u=x_{0}^{2}-\frac{v^{2}}{4 x_{0}^{2}}
$$

As we vary $x_{0}$ from 1 to 2 , these parabolas sweep out a parabolic region, which determines $f[S]$.
![](13d4bcc6-f973-445e-ad7d-b22a7a43507d-42_502_1006_1082_789.jpg)

## Mappings in Polar Coordinates

Some complex functions and regions are more naturally suited to polar coordinates. Hence it may be to our advantage to write a function as

$$
f(z)=f\left(r e^{i \theta}\right)=u(r, \theta)+i v(r, \theta)
$$

We may even write $w=f(z)$ in polar coordinates as $w=\rho(\cos \phi+i \sin \phi)$. Then we may identify the polar coordinates of $w$ as functions of the polar coordinates of $z: \rho(r, \theta)=\left|f\left(r e^{i \theta}\right)\right|$ and $\phi(r, \theta)=\arg f\left(r e^{i \theta}\right)$. The next example uses such polar coordinates to track the mapping of circular sectors.

## EXAMPLE 5 Mapping sectors

Let $S$ be the sector

$$
S=\left\{z:|z| \leq \frac{3}{2}, 0 \leq \arg z \leq \frac{\pi}{4} .\right\}
$$

Find the image of $S$ under the mapping $f(z)=z^{3}$.

Figure 8 The mapping

$$
w=z^{3}
$$

has the effect of cubing the norm and tripling the argument:

$$
\begin{aligned}
& |w|=|z|^{3} \\
& \arg w=3 \operatorname{Arg} z
\end{aligned}
$$

Solution If we write $z=r(\cos \theta+i \sin \theta)$, then $z^{3}=r^{3}(\cos 3 \theta+i \sin 3 \theta)$. Hence the polar coordinates of $w=f(z)=\rho(\cos \phi+i \sin \phi)$ are $\rho=r^{3}$ and $\phi=3 \theta$. As $r$ increases from 0 up to $\frac{3}{2}, \rho$ increases from 0 up to $\frac{27}{8}$; and as $\theta$ goes from 0 up to $\frac{\pi}{4}, \phi$ goes from 0 up to $\frac{3 \pi}{4}$. Hence the image of $S$ is the set of all $w$ with modulus less than $\frac{27}{8}$ and arguments between 0 and $\frac{3 \pi}{4}$ (see Figure 8):

$$
f[S]=\left\{w:|w| \leq \frac{27}{8}, 0 \leq \arg w \leq \frac{3 \pi}{4}\right\} .
$$

![](13d4bcc6-f973-445e-ad7d-b22a7a43507d-43_383_857_567_771.jpg)

All the mappings considered in the examples have been one-to-one, in that distinct points $z_{1}$ and $z_{2}$ always map to distinct points $f\left(z_{1}\right)$ and $f\left(z_{2}\right)$. It is possible that more than one point on the $z$-plane will map to the same point on the $w$-plane. Such mappings are not one-to-one, and we are already familiar with some of them. For example, the function $f(z)=z^{2}$ with domain of definition $\mathbb{C}$ will map $z$ and $-z$ to the same point in the $w$-plane.

## Exercises 1.4

In Exercises 1-6, evaluate $w=f(z)$ for the given value of $z$.

1. $f(z)=z+i, z=3+4 i$.
2. $f(z)=3 i z, z=-5 i$.
3. $f(z)=\operatorname{Re}(z)-2 i \operatorname{Im} z, z=-4+i$.
4. $f(z)=z^{10}+\bar{z}, z=-\sqrt{3}+i$.
5. $f(z)=\left(z^{2}+2\right)^{\frac{1}{2}}$ (principal root), $z=1+i$.
6. $f(z)=\frac{z-1}{z+1}, z=i+1$.

In Exercises 7-12, express $f(z)$ in the form $u(x, y)+i v(x, y)$ where $u$ and $v$ are the real and imaginary parts of $f$.
7. $f(z)=i z+2-i$.
8. $f(z)=z^{2}+3 z+1+3 i$.
9. $f(z)=z^{3}$.
10. $f(z)=2 \bar{z}+\frac{1}{2+i}$.
11. $f(z)=\frac{1}{z+1}$.
12. $f(z)=|z|^{3}$.

In Exercises 13-18, find the largest subset of $\mathbb{C}$ on which the given formula makes sense and hence defines a function.
13. $f(z)=\frac{1}{z}$.
14. $f(z)=3+i z^{2}$.
15. $f(z)=\frac{1}{1+z^{2}}$.
16. $f(z)=2+i \operatorname{Arg} z$.
17. $f(z)=z^{\frac{1}{2}}$ (principal root).
18. $f(z)=\frac{z-2 i}{2 z+i}$.
19. Find a linear transformation $f(z)$ such that $f(1)=3+i$ and $f(3 i)=-2+6 i$.
20. Find a linear transformation $f(z)$ such that $f(2-i)=-3-3 i$ and $f(2)= -2-2 i$.
In Exercises 21-24, find the image $f[S]$ under the given linear transformation. Draw a picture of $S$ and $f[S]$, and depict arrows mapping select points.
21. $S=\{z:|z|<1\}, \quad f(z)=4 z$.
22. $S=\{z: \operatorname{Re} z>0\}, \quad f(z)=z+i$.
23. $S=\{z: \operatorname{Re} z>0, \operatorname{Im} z>0\}, f(z)=-z+2 i$.
24. $S=\left\{z:|z| \leq 2,0 \leq \operatorname{Arg} z \leq \frac{\pi}{2}\right\} \quad f(z)=i z+2$.
25. (a) Suppose that $f(z)=a z+b$ and $g(z)=c z+d$ are linear transformations. Show that $f(g(z))$ is also a linear transformation.
(b) Show that every linear transformation $f(z)=a z+b, a \neq 0$ can be written in the form $g_{1}\left(g_{2}\left(g_{3}(z)\right)\right)$, where $g_{1}$ is a translation, $g_{2}$ is a rotation, and $g_{3}$ is a dilation.
26. Construct a linear transformation that rotates all points in the plane an angle $\phi$ about a point $z_{0}$.
27. Let $f(z)=a z$ and $g(z)=z+b$. Show that $f(g(z))=g(f(z))$ for all $z$ if and only if $a=1$ or $b=0$.
28. Show that for each linear transformation $f(z)=a z+b$, there exists a linear transformation $g(z)$ such that $f(g(z))=g(f(z))=z$ for all complex $z$.
29. Find the image of the set $S=\{z: z$ is real $\}$ under the mapping $f(z)=\operatorname{Arg} z$.
30. Find the image of the set $S=\{z:|z| \leq 1\}$ under the mapping $f(z)=z+\bar{z}$. In Exercises 31-34, find the image $f[S]$ under the inversion $f(z)=\frac{1}{z}$. Draw a picture of $S$ and $f[S]$, and depict arrows mapping select points.
31. $S=\{z: 0<|z| \leq 1\}$.
32. $S=\{z:|z| \geq 1$,$\} .$
33. $S=\left\{z: 0<|z| \leq 3, \frac{\pi}{3} \leq \operatorname{Arg} z \leq \frac{2 \pi}{3}\right\}$.
34. $S=\left\{z: z \neq 0,0 \leq \operatorname{Arg} z \leq \frac{\pi}{2}\right\}$.
35. Let $f(z)=\frac{1}{z}$.
(a) Show that the image of the circle $|z|=a>0$ is the circle $|w|=\frac{1}{a}$.
(b) Show that the image of the ray $\operatorname{Arg} z=\alpha \quad(z \neq 0)$ is the ray $\operatorname{Arg} w=-\alpha (w \neq 0)$.
36. Show that for $f(z)=1 / z, f(z)=g(h(z))=h(g(z))$, where $g(z)=\bar{z}$ and $h(z)=\frac{z}{|z|^{2}}$.
37. (a) Show that $f(z)=\frac{1}{z}$ is never zero for any complex $z$.
(b) Let $S$ be any subset of the complex numbers that does not include zero. Show that $f[S]$ is a subset of the complex numbers that does not include zero.
(c) Show that $f(f(z))=z$ for all $z \neq 0$.
(d) Show that $f[f[S]]=S$.
38. Find a linear fractional transformation $f(z)=\frac{a z+b}{c z+d}$ such that $f(0)=-5+i$, $f(2)=-\frac{8}{5}-i \frac{11}{5}, f(-2 i)=5-2 i$. [Hint: In solving for $a, b, c, d$, keep in mind that these are not uniquely determined. Once you determine that a coefficient is not zero, say $a \neq 0$, you may set it equal to 1 .]
39. Find a linear fractional transformation $f(z)=\frac{a z+b}{c z+d}$ such that $f(0)=-2 i$, $f(9 i)=-\frac{i}{5}, f(4-i)=\frac{1}{2}$.
40. Find the function $f(z)=\frac{1}{c z+d}$ so that $f(1)=\frac{2-i}{5}$ and $f\left(-\frac{i}{2}\right)$ is not defined. A point $z_{0}$ is called a fixed point of a function $f(z)$ if $f\left(z_{0}\right)=z_{0}$. In Exercises 4144, determine the fixed points of the given function.
41. $f(z)=\frac{1}{z}$.
42. $f(z)=a z+b$. [Hint: Take two cases: $a=1$ and $a \neq 1$ ]
43. $f(z)=2\left(z+\frac{1}{z}\right)$.
44. $f(z)=\frac{-6 i+(2+3 i) z}{z}$.
45. Define the set of lattice points in the plane as

$$
L=\{z: z=m+i n, \quad m \text { and } n \text { integers }\} .
$$

Consider the mapping $f(z)=z^{2}$ and the image $f[L]$.
(a) Show that if $w$ is in $f[L],-w, \bar{w}$, and $-\operatorname{Re} w+i \operatorname{Im} w$ are in $f[L]$.
(b) Show that if $w$ is in $f[L], w$ is also in $L$.
(c) Show that if $w$ is in $f[L], f(w)$ is in $f[L]$.

### 1.5 The Complex Exponential

In this section, we introduce the complex exponential function $e^{z}$. Unlike in calculus, where $e^{x}$ was introduced separately from the trigonometric functions, here we will use the exponential function $e^{z}$ to define the trigonometric functions of a complex variable $z$. This makes $e^{z}$ one of the most important functions in this book.

As a first step toward defining $e^{z}$, ask yourself how you might compute $e^{x}$ for a given real number $x$. One way is to use the power series

$$
e^{x}=1+\frac{x}{1!}+\frac{x^{2}}{2!}+\frac{x^{3}}{3!}+\cdots \quad(-\infty<x<\infty) .
$$

In fact, we can take this series to be the definition of $e^{x}$ and use properties of power series to study $e^{x}$. Guided by this approach, we define the complex exponential function by a power series

$$
e^{z}=\sum_{n=0}^{\infty} \frac{z^{n}}{n!}=1+\frac{z}{1!}+\frac{z^{2}}{2!}+\frac{z^{3}}{3!}+\cdots, \quad \text { for all complex } z
$$

Sometimes the exponential function is written as $\exp (z)$. Of course, we have not yet defined what we mean by an infinite series of complex numbers. However, we are familiar with infinite sums of real numbers, and as you
will see in Chapter 4, the theory of series extends to complex numbers. As a consequence, we will show that the series in (1) converges for all $z$ and defines a function that enjoys some of the familiar properties of the exponential function. In particular, we will show that the rule

$$
e^{z_{1}+z_{2}}=e^{z_{1}} e^{z_{2}}
$$

holds for all complex numbers $z_{1}$ and $z_{2}$. Because we have used the exponential power series to define $e^{z}$, it is clear that $e^{z}$ reduces to the real exponential when $z=x$ is real.

Our next step will be to unlock the mystery of $e^{z}$ by expressing it in terms of familiar functions. Write $z=x+i y$, where $x$ and $y$ are real. By (2), we have

$$
e^{z}=e^{x+i y}=e^{x} e^{i y}
$$

The first factor, $e^{x}$, is the familiar real exponential function from calculus. To compute the second factor, we use (1) and get

$$
\begin{aligned}
e^{i y} & =1+i y+\frac{(i y)^{2}}{2!}+\frac{(i y)^{3}}{3!}+\frac{(i y)^{4}}{4!}+\frac{(i y)^{5}}{5!}+\cdots \\
& =1+i y-\frac{y^{2}}{2!}-i \frac{y^{3}}{3!}+\frac{y^{4}}{4!}+i \frac{y^{5}}{5!}+\cdots
\end{aligned}
$$

If we regroup the terms in the series, a step that will be justified in Chapter 4, we obtain

$$
\begin{aligned}
e^{i y} & =\left(1-\frac{y^{2}}{2!}+\frac{y^{4}}{4!}-\cdots\right)+i\left(y-\frac{y^{3}}{3!}+\frac{y^{5}}{5!}-\cdots\right) \\
& =\cos y+i \sin y
\end{aligned}
$$

where we have recognized the power series expansions for the cosine and sine functions (converging for all $y$ ),

$$
\cos y=\sum_{n=0}^{\infty} \frac{(-1)^{n} y^{2 n}}{(2 n)!} \text { and } \sin y=\sum_{n=0}^{\infty} \frac{(-1)^{n} y^{2 n+1}}{(2 n+1)!} .
$$

Thus the desired expression

$$
e^{z}=e^{x} e^{i y}=e^{x}(\cos y+i \sin y)
$$

Consequently,

$$
\operatorname{Re} e^{z}=e^{x} \cos y \quad \text { and } \quad \operatorname{Im} e^{z}=e^{x} \sin y
$$

THE COMPLEX EXPONENTIAL

![](13d4bcc6-f973-445e-ad7d-b22a7a43507d-47_461_508_1496_112.jpg)
Figure 1 For $z=x+i y$, $e^{z}$ has modulus $e^{x}$ and argument $y$ :
$$
\begin{aligned}
& \left|e^{z}\right|=e^{x} \\
& \arg \left(e^{z}\right)=y .
\end{aligned}
$$

We summarize these results for ease of reference.
The complex exponential $e^{z}$ is defined for all $z$ as in (1). For $z=x+i y$, we have
(4)

$$
e^{z}=e^{x}(\cos y+i \sin y)
$$

In particular, for $z=i \theta$, with $\theta$ real, we have the identity

$$
e^{i \theta}=\cos \theta+i \sin \theta,
$$

known as Euler's identity.

## EXAMPLE 1 Finding $e^{z}$

Compute $e^{z}$ for the given $z$.
(a) $2+i \pi$.
(b) $3-i \frac{\pi}{3}$.
(c) $-1+i \frac{\pi}{2}$.
(d) $\quad i \frac{5 \pi}{4}$.

Solution (a) From (4),

$$
e^{2+i \pi}=e^{2}(\cos \pi+i \sin \pi)=-e^{2} .
$$

This number is purely real and negative.
(b) From (4),

$$
e^{3-i \frac{\pi}{3}}=e^{3}\left(\cos \frac{\pi}{3}+i \sin \left(-\frac{\pi}{3}\right)\right)=e^{3}\left(\frac{1}{2}-i \frac{\sqrt{3}}{2}\right)
$$

(c) From (4),

$$
e^{-1+i \frac{\pi}{2}}=e^{-1}\left(\cos \frac{\pi}{2}+i \sin \frac{\pi}{2}\right)=\frac{i}{e}
$$

This number is purely imaginary.
(d) Here $z$ is purely imaginary; we may use Euler's identity. From (5),

$$
e^{i \frac{5 \pi}{4}}=\cos \frac{5 \pi}{4}+i \sin \frac{5 \pi}{4}=-\frac{\sqrt{2}}{2}-i \frac{\sqrt{2}}{2} .
$$

This number is unimodular.
Example 1 shows that the complex exponential function can take on negative real values and complex values. This is in sharp contrast with the real exponential function, which is always positive.

Looking back at (4), and recalling the well-known fact from calculus that $e^{x}>0$ for all $x$, it follows immediately that (4) is the polar form of $e^{z}$ (see (2), Section 1.3), where the modulus of $e^{z}$ is $e^{x}$ and its argument is $y+2 k \pi$,
where $k$ is an integer (see Figure 1). We have the following results.

Figure 2 To plot a point in exponential notation $z=r e^{i \theta}$, move a distance $r$ along the ray extending from the origin to $e^{i \theta}$.
![](13d4bcc6-f973-445e-ad7d-b22a7a43507d-48_525_557_1570_108.jpg)

MODULUS AND ARGUMENT OF THE COMPLEX EXPONENTIAL

The exponential notation, $z=r e^{i \theta}$, enables us to operate on complex numbers in a very convenient way, as we now show.
For $z=x+i y$, the modulus of $e^{z}$ is

$$
\left|e^{z}\right|=e^{x}>0 .
$$

Consequently, $e^{z}$ is never zero. The argument of $e^{z}$ is

$$
\arg \left(e^{z}\right)=y+2 k \pi \quad(z=x+i y),
$$

where $k$ is an integer.
Using the exponent rule (2) and the fact that $e^{0}=1$, we can write

$$
1=e^{z-z}=e^{z} e^{-z} .
$$

Thus, for any complex number $z$, the multiplicative inverse of $e^{z}$ is $e^{-z}$; equivalently,

$$
e^{-z}=\frac{1}{e^{z}}
$$

## Exponential and Polar Representations

Euler's identity (5) provides us with yet another convenient way of representing complex numbers. Indeed, if $z=r(\cos \theta+i \sin \theta)$ is a complex number in polar form, then since $e^{i \theta}=\cos \theta+i \sin \theta$, we obtain the exponential representation or polar form $z=r e^{i \theta}$.

From this representation it is clear that

$$
|z|=1 \Leftrightarrow r=1 \Leftrightarrow z=e^{i \theta},
$$

where $\theta$ is the argument of $z$. Thus the complex numbers $e^{i \theta}$ are the unimodular complex numbers. Because their distance to the origin always equals 1 , all the complex numbers $e^{i \theta}$ lie on the unit circle. All other nonzero complex numbers are positive multiples of some $e^{i \theta}$. This fact is illustrated geometrically in Figure 2, where the ray from the origin to $z=r e^{i \theta}$ intersects the unit circle at the point $e^{i \theta}$. To go from the origin to $z$, we move in the direction of $e^{i \theta}$ by a distance $r=|z|$.
where $\theta$ is the argument of $z$. Thus the complex numbers $e^{i \theta}$ are the unimod-
ular complex numbers. Because their distance to the origin always equals 1 ,
all the complex numbers $e^{i \theta}$ lie on the unit circle. All other nonzero complex
numbers are positive multiples of some $e^{i \theta}$. This fact is illustrated geomet-
rically in Figure 2 , where the ray from the origin to $z=r e^{i \theta}$ intersects the
unit circle at the point $e^{i \theta}$. To go from the origin to $z$, we move in the
direction of $e^{i \theta}$ by a distance $r=|z|$.
The exponential notation, $z=r e^{i \theta}$, enables us to operate on complex
numbers in a very convenient way, as we now show.

EXPONENTIAL REPRESENTATION

The exponential representation of $z=r(\cos \theta+i \sin \theta)$ is
(8) $\quad z=r e^{i \theta}, \quad|z|=r \quad$ and $\quad \arg z=\theta+2 k \pi$.

We have
(9) $\bar{z}=r e^{-i \theta}$;
(10)

$$
z^{-1}=\frac{1}{r} e^{-i \theta} \quad(z \neq 0)
$$

If $z_{1}=r_{1} e^{i \theta_{1}}$ and $z_{2}=r_{2} e^{i \theta_{2}}$, then

$$
\begin{aligned}
z_{1} z_{2} & =r_{1} r_{2} e^{i\left(\theta_{1}+\theta_{2}\right)} \\
\frac{z_{1}}{z_{2}} & =\frac{r_{1}}{r_{2}} e^{i\left(\theta_{1}-\theta_{2}\right)} \quad\left(z_{2} \neq 0\right)
\end{aligned}
$$

Proof As we remarked earlier, (8) is a consequence of Euler's identity (5). For (9), we have

$$
\bar{z}=\overline{r(\cos \theta+i \sin \theta)}=r(\cos \theta-i \sin \theta)=r(\cos (-\theta)+i \sin (-\theta))=r e^{-i \theta}
$$

To prove (10), write $z=r e^{i \theta}$ with $r \neq 0$. Then

$$
z \frac{1}{r} e^{-i \theta}=r e^{i \theta} \frac{1}{r} e^{-i \theta}=e^{i(\theta-\theta)}=e^{0}=1
$$

The proofs of (11) and (12) are immediate from (2) and (10). We leave the details to the exercises.

![](13d4bcc6-f973-445e-ad7d-b22a7a43507d-49_463_502_1461_107.jpg)
Figure 3 To multiply two unimodular numbers we add their arguments, and to divide them we subtract their arguments.

Multiplication and division of unimodular numbers are particularly easy to describe using the complex exponential. Indeed, if $z_{1}=e^{i \theta_{1}}$ and $z_{2}=e^{i \theta_{2}}$, then from (11) and (12) we get

$$
z_{1} z_{2}=e^{i \theta_{1}} e^{i \theta_{2}}=e^{i\left(\theta_{1}+\theta_{2}\right)}
$$

and

$$
\frac{z_{1}}{z_{2}}=\frac{e^{i \theta_{1}}}{e^{i \theta_{2}}}=e^{i\left(\theta_{1}-\theta_{2}\right)}
$$

Thus, to multiply two unimodular numbers we add their arguments, and to divide them we subtract their arguments. (See Figure 3.)

## EXAMPLE 2 Exponential representations

Let $z_{1}=-7 \sqrt{3}+7 i$ and $z_{2}=1+i$. Express the following complex expressions in exponential form. Also give your answer in Cartesian form in (d) and (e).
(a) $z_{1}$.
(b) $z_{2}$.
(c) $z_{1} z_{2}$.
(d) $\frac{1}{z_{2}}$.
(e) $\frac{z_{1}}{z_{2}}$.

Solution (a) We will use (8). We have $\left|z_{1}\right|=\sqrt{(-7 \sqrt{3})^{2}+7^{2}}=14$. To compute a value of $\arg z_{1}$, we appeal to (14), Section 1.3. Since $z_{1}$ is in the second quadrant, we have $\operatorname{Arg} z_{1}=\tan ^{-1}\left(\frac{7}{-7 \sqrt{3}}\right)+\pi=\frac{5 \pi}{6}$. Hence

$$
z_{1}=14\left(\cos \frac{5 \pi}{6}+i \sin \frac{5 \pi}{6}\right)=14 e^{i \frac{5 \pi}{6}}
$$

(b) Following the steps in (a), we find $\left|z_{2}\right|=\sqrt{1^{2}+1^{2}}=\sqrt{2}$ and $\operatorname{Arg} z_{2}= \tan ^{-1}(1)=\frac{\pi}{4}$. Hence

$$
z_{2}=\sqrt{2}\left(\cos \frac{\pi}{4}+i \sin \frac{\pi}{4}\right)=\sqrt{2} e^{i \frac{\pi}{4}}
$$

(c) We use (a), (b), and (11) and get

$$
z_{1} z_{2}=14 e^{i \frac{5 \pi}{6}} \sqrt{2} e^{i \frac{\pi}{4}}=14 \sqrt{2} e^{i\left(\frac{5 \pi}{6}+\frac{\pi}{4}\right)}=14 \sqrt{2} e^{i \frac{13 \pi}{12}}
$$

(d) We use (b) and (10) and get

$$
\frac{1}{z_{2}}=z_{2}^{-1}=\frac{1}{\sqrt{2}} e^{-i \frac{\pi}{4}}
$$

This is the polar form of $\frac{1}{z_{2}}$. To get the Cartesian form, we use Euler's identity:

$$
\frac{1}{z_{2}}=\frac{1}{\sqrt{2}}\left(\cos \frac{-\pi}{4}+i \sin \frac{-\pi}{4}\right)=\frac{1}{\sqrt{2}}\left(\frac{\sqrt{2}}{2}-i \frac{\sqrt{2}}{2}\right)=\frac{1}{2}-i \frac{1}{2}
$$

Checking our answer, we have

$$
z_{2} \frac{1}{z_{2}}=(1+i)\left(\frac{1}{2}-i \frac{1}{2}\right)=\left(\frac{1}{2}+\frac{1}{2}\right)+i\left(\frac{1}{2}-\frac{1}{2}\right)=1
$$

as it should be.
(e) We use (a) and (b) and (12) and get

$$
\frac{z_{1}}{z_{2}}=\frac{14}{\sqrt{2}} e^{i\left(\frac{5 \pi}{6}-\frac{\pi}{4}\right)}=7 \sqrt{2} e^{i \frac{7 \pi}{12}}
$$

To get the Cartesian form, we use Euler's identity:

$$
\begin{aligned}
\frac{z_{1}}{z_{2}} & =7 \sqrt{2}\left(\cos \frac{7 \pi}{12}+i \sin \frac{7 \pi}{12}\right) \\
& =7 \sqrt{2}\left(\frac{1-\sqrt{3}}{2 \sqrt{2}}+i \frac{1+\sqrt{3}}{2 \sqrt{2}}\right)=\frac{7}{2}((1-\sqrt{3})+i(1+\sqrt{3}))
\end{aligned}
$$

where we have used the subtraction formulas for the cosine and sine to compute the exact values of $\cos \frac{7 \pi}{12}$ and $\sin \frac{7 \pi}{12}$. For example,

$$
\begin{aligned}
\cos \frac{7 \pi}{12} & =\cos \left(\frac{5 \pi}{6}-\frac{\pi}{4}\right)=\cos \frac{5 \pi}{6} \cos \frac{\pi}{4}+\sin \frac{5 \pi}{6} \sin \frac{\pi}{4} \\
& =-\frac{\sqrt{3}}{2} \frac{\sqrt{2}}{2}+\frac{1}{2} \frac{\sqrt{2}}{2}=\frac{1-\sqrt{3}}{2 \sqrt{2}}
\end{aligned}
$$

The value of $\sin \frac{7 \pi}{12}=\frac{1+\sqrt{3}}{2 \sqrt{2}}$ can be derived similarly.

## The Exponential as a Mapping

It is important to explore how the exponential function maps complex numbers. The following result shows that the exponential function, unlike its real counterpart, is not one-to-one.

MAPPING PROPERTIES OF THE EXPONENTIAL

We have

$$
e^{z}=1 \quad \text { if and only if } \quad z=2 k \pi i, \text { for some integer } k .
$$

Also,

$$
e^{z_{1}}=e^{z_{2}} \quad \text { if and only if } \quad z_{1}=z_{2}+2 k \pi i, \text { for some integer } k .
$$

Proof Write $z=x+i y$, and suppose $e^{z}=1$. Then $e^{x} e^{i y}=1$. Thinking of this as the exponential representation of the complex number 1 , we see that $e^{x}=1$ and $y=2 k \pi$ for some integer $k$. But $e^{x}=1$ implies that $x=0$. Hence $z=i y=2 k \pi i$ for some integer $k$. Conversely, if $z=2 k \pi i$, then $e^{2 k \pi i}=\cos 2 k \pi+i \sin 2 k \pi=1$. We have proved (13). To prove (14), notice that $e^{z_{1}}=e^{z_{2}} \Leftrightarrow e^{z_{1}-z_{2}}=1$, which by (13) is if and only if $z_{1}-z_{2}=2 k \pi i$, or $z_{1}=z_{2}+2 k \pi i$.

A complex-valued function $f(z)$ is periodic with period $\tau \neq 0$ if for all $z$ in the domain of definition of $f$, we have $f(z+\tau)=f(z)$. From (14), it follows that, for all complex numbers $z$,

$$
e^{z}=e^{z+2 \pi i}
$$

Hence the exponential function $e^{z}$ is periodic with period $2 \pi i$.
Now we show an example of the exponential function mapping a specific region.

## EXAMPLE 3 An exponential mapping

Consider the rectangular area

$$
S=\{z=x+i y:-1 \leq x \leq 1,0 \leq y \leq \pi\} .
$$

Find the image of $S$ under the mapping $f(z)=e^{z}$.
Solution Fix $x_{0}$ in the interval $[-1,1]$ and consider $E F$, the vertical line segment $x=x_{0}$ inside $S$. Points on the segment $E F$ are of the form $z=x_{0}+i y$, where $0 \leq y \leq \pi$. For such $z$,

$$
f(z)=e^{z}=e^{x_{0}} e^{i y}=e^{x_{0}}(\cos y+i \sin y) .
$$

The point $w=e^{x_{0}} e^{i y}$ has modulus $e^{x_{0}}$ and argument $y$. In particular, $w$ lies on the circle of radius $e^{x_{0}}$ with center at 0 . As $y$ varies from 0 to $\pi$, the point $w$ traces the
upper semicircle. Thus the image of $E F$ by $f$ is the upper semicircle with center at 0 and radius $e^{x_{0}}$.

Figure 4 As usual, we denote the image of a point $P$ in the $x y$-plane by the point $P^{\prime}$ in the $u v$-plane. The mapping $w=e^{z}$ takes the vertical line segment $E F$ to a semicircle in the $u v$-plane with $u$-intercepts at $E^{\prime}$ and $F^{\prime}$.
![](13d4bcc6-f973-445e-ad7d-b22a7a43507d-52_501_1327_275_743.jpg)

Now, as we vary $x_{0}$ from -1 to $1, e^{x_{0}}$ varies from $e^{-1}$ to $e$. As a consequence, the corresponding semicircles increase in radius and fill the semiannular area between the semicircle of radius $e^{-1}$ with center at 0 and the semicircle of radius $e$ with center at 0 . (See Figure 4.)

You should check in Example 3 that the rectangular boundary of the area $S$ is mapped to the boundary of the semiannular area $f[S]$. The fact that $f$ maps boundary to boundary is an important property that will be investigated in Section 2.5 and the chapter on conformal mappings.

In Example 3, if we enlarge the rectangular region $S$ to become the infinite horizontal strip, where $-\infty<x<\infty$ and $0 \leq y<2 \pi$, the image of $S$ will cover the entire $w$-plane minus the origin. Since $e^{z}$ is never $0, e^{z}$ will map the entire $z$-plane onto the $w$-plane minus the origin. In fact, by periodicity, $e^{z}$ assumes every nonzero $w$ an infinite number of times; by (14), the solutions $z$ to $e^{z}=w$ must differ by integer multiples of $2 \pi i$.

## Trigonometric Functions via Euler's Identity

Let $\theta$ be an arbitrary real number. Euler's identity tells us that

$$
e^{i \theta}=\cos \theta+i \sin \theta
$$

and

$$
e^{-i \theta}=\cos \theta-i \sin \theta .
$$

Adding these two identities and dividing by 2 , we get

$$
\cos \theta=\frac{e^{i \theta}+e^{-i \theta}}{2} .
$$

Similarly, subtracting and dividing by $2 i$, we get

$$
\sin \theta=\frac{e^{i \theta}-e^{-i \theta}}{2 i} .
$$

These expressions enable us in certain cases to use to our advantage elementary properties of the exponential function in handling tricky problems
involving products of the cosine and sine functions. For example, suppose $p$ is a positive integer. You can express the product $\cos ^{m} \theta \sin ^{n} \theta$, where $m$ and $n$ are nonnegative integers such that $m+n=p$, as a linear combination of terms involving $\cos (j \theta)$ and $\sin (k \theta)$, where $1 \leq j, k \leq p$. This process is called linearization and has many useful applications in calculus. We illustrate with an example.

## EXAMPLE 4 Linearizing powers of the cosine

Linearize $\cos ^{3} \theta$.
Solution Appealing to (16), we have

$$
\begin{aligned}
\cos ^{3} \theta & =\left(\frac{e^{i \theta}+e^{-i \theta}}{2}\right)^{3}=\frac{1}{8}\left(e^{3 i \theta}+3 e^{2 i \theta} e^{-i \theta}+3 e^{i \theta} e^{-2 i \theta}+e^{-3 i \theta}\right) \\
& =\frac{1}{4}\left[\frac{e^{3 i \theta}+e^{-3 i \theta}}{2}+3 \frac{e^{i \theta}+e^{-i \theta}}{2}\right]=\frac{1}{4}(\cos 3 \theta+3 \cos \theta)
\end{aligned}
$$

As a typical application of linearization, we evaluate $\int \cos ^{3} \theta d \theta$. By using the result of Example 4, we have

$$
\int \cos ^{3} \theta d \theta=\frac{1}{4} \int(\cos 3 \theta+3 \cos \theta) d \theta=\frac{1}{12} \sin 3 \theta+\frac{3}{4} \sin \theta+C
$$

In the following section, we will use the expressions (16) and (17) for the cosine and sine in terms of the exponential to generalize trigonometric functions to complex variables. Finally, we mention that (16) and (17) are extremely useful in the theory of Fourier series, where they are used to relate the real form to the complex form of Fourier series. This is developed in Chapter 7 on Fourier series.

## Exercises 1.5

In Exercises 1-10, write the given complex number in the form $a+i b$.

1. $e^{i \pi}$.
2. $e^{2 i \pi}$.
3. $e^{200 i \pi}$.
4. $e^{201 i \pi}$.
5. $e^{i \frac{3 \pi}{4}}$.
6. $e^{2-i \frac{\pi}{4}}$.
7. $e^{-1-i \frac{\pi}{6}}$.
8. $-2 e^{i+\pi}$.
9. $3 e^{3+i \frac{\pi}{2}}$.
10. $e^{701 i \frac{\pi}{4}}$.

In Exercises 11-18, express the given complex number in the exponential form re $e^{i \theta}$. (You may notice that these are the same complex numbers as in Exercises 5-12 in Section 1.3.)
11. $-3-3 i$.
12. $-\frac{\sqrt{3}}{2}+\frac{i}{2}$.
13. $-1-\sqrt{3} i$.
14. $1+i$.
15. $-\frac{i}{2}$.
16. $\frac{1+i}{1+\sqrt{3} i}$.
17. $\frac{1+i}{1-i}$.
18. $\frac{i}{10+10 i}$.

In Exercises 19-24, write the given complex number in the form $a+i b$, where $a$ and $b$ are real.
19. $e^{i}$.
20. $e^{1+\sqrt{2} i \pi}$.
21. $\left|e^{-i \frac{\pi}{12}}\right|$.
22. $e^{-1-i} \overline{e^{1+2 i}}$.
23. $\frac{e^{3-i}}{e^{-1+2 i}}$.
24. $e^{1-60 i \pi}\left|e^{-1+200 i}\right|$.
25. Find the real and imaginary parts of the following functions.
(a) $e^{3 z}$.
(b) $e^{z^{2}}$.
(c) $e^{\bar{z}}$.
(d) $e^{i z}$.
26. (a) For all complex numbers $z$, show that $\left(e^{z}\right)^{n}=e^{n z}, n=0, \pm 1, \pm 2, \ldots$.
(b) Show that $\overline{e^{z}}=e^{\bar{z}}$.
(c) Show that $e^{z+i \pi}=-e^{z}$.

In Exercises 27-32, show that the shaded area $S$ in the $z$-plane is mapped to the shaded area in the $w$-plane by the given mapping $f(z)$.
27.

![](13d4bcc6-f973-445e-ad7d-b22a7a43507d-54_482_868_653_227.jpg)
Figure 5

29. 

![](13d4bcc6-f973-445e-ad7d-b22a7a43507d-54_501_906_1193_227.jpg)
Figure 7

31. 

![](13d4bcc6-f973-445e-ad7d-b22a7a43507d-54_503_912_1746_231.jpg)
Figure 9

28. 

![](13d4bcc6-f973-445e-ad7d-b22a7a43507d-54_490_860_643_1217.jpg)
Figure 6

30. 

![](13d4bcc6-f973-445e-ad7d-b22a7a43507d-54_494_872_1189_1219.jpg)
Figure 8

32. 

![](13d4bcc6-f973-445e-ad7d-b22a7a43507d-54_508_888_1739_1221.jpg)
Figure 10

In Exercises 33-36, (a) linearize the integrand; (b) evaluate the given integral.
33. $\quad \int \sin ^{4} \theta d \theta$. 34. $\quad \int \cos ^{5} \theta d \theta$. 35. $\quad \int \cos ^{6} \theta d \theta$. 36. $\quad \int \sin ^{3} \theta \cos ^{5} \theta d \theta$
37. Show that for all complex numbers $z,\left|e^{z}\right| \leq e^{|z|}$. When does equality hold?
38. Differences and similarities. In the text, we pointed out a few similarities and differences between $e^{z}$ and $e^{x}$. In what follows we consider some additional ones. For each part, either prove your answer or provide an example to show that the statement is false.
(a) The function $e^{x}$ is one to one. Is $e^{z}$ one to one?
(b) The function $e^{x}$ is increasing (if $x_{1}<x_{2}$ then $e^{x_{1}}<e^{x_{2}}$ ). If $\left|z_{1}\right|<\left|z_{2}\right|$ do we have $\left|e^{z_{1}}\right|<\left|e^{z_{2}}\right|$ ?
(c) The function $e^{x}$ never vanishes. Can $e^{z}$ vanish?
(d) The function $e^{x}$ is always positive. Is $e^{z}$ always real and positive?
(e) The modulus or absolute value of $e^{x}$ is $e^{x}$. What is the absolute value of $e^{z}$ ?
(f) We have $e^{x}=1 \Leftrightarrow x=0$. Do we have $e^{z}=1 \Leftrightarrow z=0$ ?
39. Show that $\left|e^{z}\right| \leq 1$ if and only if $\operatorname{Re} z \leq 0$. When does equality hold?
40. Project Problem: The Dirichlet kernel. (a) For $z \neq 1$ and $n= 1,2, \ldots$, show that

$$
1+z+z^{2}+\cdots+z^{n}=\frac{1-z^{n+1}}{1-z}
$$

(b) Take $z=e^{i \theta}$, where $\theta$ is a real number $\neq 2 k \pi$ ( $k$ an integer), and obtain

$$
1+e^{i \theta}+e^{2 i \theta}+\cdots+e^{i n \theta}=\frac{i}{2} \frac{\left(1-e^{i(n+1) \theta}\right) e^{-i \frac{\theta}{2}}}{\sin \frac{\theta}{2}}
$$

[Hint: After substituting $z=e^{i \theta}$, multiply and divide by $e^{-i \frac{\theta}{2}}$; then use (17).] (c) Take the real and imaginary parts of the identity in (b) to obtain

$$
1+\cos \theta+\cos 2 \theta+\cdots+\cos n \theta=\frac{1}{2}+\frac{\sin \left[\left(n+\frac{1}{2}\right) \theta\right]}{2 \sin \frac{\theta}{2}}
$$

and

$$
\sin \theta+\sin 2 \theta+\cdots+\sin n \theta=\frac{\cos \frac{\theta}{2}-\sin \left[(n+1) \frac{\theta}{2}\right]}{2 \sin \frac{\theta}{2}}
$$

(d) Derive the identity

$$
\frac{1}{2}+\cos \theta+\cos 2 \theta+\cdots+\cos n \theta=\frac{\sin \left[\left(n+\frac{1}{2}\right) \theta\right]}{2 \sin \frac{\theta}{2}}
$$

This finite sum of cosines is a constant multiple of the Dirichlet kernel (see Section 7.6). It plays an important role in the theory of Fourier series. The sum of sines in (c) is known as the conjugate Dirichlet kernel of order $n$ and is also useful in the theory of Fourier series.

### 1.6 Trigonometric and Hyperbolic Functions

In the previous section, we defined the complex exponential function $e^{z}$ as an extension of the real exponential function $e^{x}$. The function $e^{x}$ is one of the so-called elementary functions from calculus. Elementary functions comprise
among other functions the trigonometric functions, the hyperbolic functions, the logarithmic functions, and raising numbers to powers. Our goal in this and the following section is to extend some of the elementary functions to complex numbers and study their basic properties. These new functions will provide us with ample examples to test the theory of derivatives and integrals that will be presented in the following chapters.

## Trigonometric Functions

Let $\theta$ be any real number. Using Euler's identity, we showed in Section 1.5, (16) and (17), that
(1)

$$
\cos \theta=\frac{e^{i \theta}+e^{-i \theta}}{2} \text { and } \sin \theta=\frac{e^{i \theta}-e^{-i \theta}}{2 i} .
$$

Motivated by these identities, we define the complex cosine and sine functions for all complex numbers $z$ by the formulas

$$
\cos z=\frac{e^{i z}+e^{-i z}}{2}
$$

and

$$
\sin z=\frac{e^{i z}-e^{-i z}}{2 i}
$$

You should keep in mind that these are new functions, even though they are named after familiar functions. As you will soon see, they share similar properties with the usual cosine and sine functions, but they assume complex values and are not bounded in absolute value.

## EXAMPLE 1 Finding $\cos z$ and $\sin z$

(a) Compute $\cos (2+i \pi)$.
(b) Compute $\sin \left(i \frac{5 \pi}{4}\right)$.

Solution We use the definitions. For (a), we have from (2),

$$
\begin{aligned}
\cos (2+i \pi) & =\frac{1}{2}\left(e^{i(2+i \pi)}+e^{-i(2+i \pi)}\right) \\
& =\frac{1}{2}\left(e^{-\pi+2 i}+e^{\pi-2 i}\right)=\frac{1}{2}\left(e^{-\pi} e^{2 i}+e^{\pi} e^{-2 i}\right) \\
& =\frac{1}{2}\left(e^{-\pi}[\cos (2)+i \sin (2)]+e^{\pi}[\cos (2)-i \sin (2)]\right) \\
& =\cos (2) \frac{e^{\pi}+e^{-\pi}}{2}-i \sin (2) \frac{e^{\pi}-e^{-\pi}}{2} \\
& =\cos (2) \cosh \pi-i \sin (2) \sinh \pi
\end{aligned}
$$

where $\cosh \pi$ and $\sinh \pi$ are the real hyperbolic functions evaluated at $\pi$.

PROPERTIES OF TRIGONOMETRIC FUNCTIONS

For (b), we use (3) and proceed in a similar way:

$$
\begin{aligned}
\sin \left(i \frac{5 \pi}{4}\right) & =\frac{1}{2 i}\left(e^{i\left(i \frac{5 \pi}{4}\right)}-e^{-i\left(i \frac{5 \pi}{4}\right)}\right) \\
& =\frac{-i}{2}\left(e^{-\frac{5 \pi}{4}}-e^{\frac{5 \pi}{4}}\right)=i \sinh \left(\frac{5 \pi}{4}\right)
\end{aligned}
$$

The appearance of the hyperbolic functions in the expressions of the real and imaginary parts of the complex cosine and sine functions was not a coincidence. In fact, general formulas of this nature will be derived later in this section.

A function $f(z)$ is said to be even if $f(z)=f(-z)$ and odd if $f(-z)= -f(z)$, for all $z$ in the domain of definition of $f$. We can show from their definitions that the cosine is even while the sine is odd; also, both of them are $2 \pi$-periodic. In fact, the complex trigonometric functions satisfy many identities that we are familiar with for real trigonometric functions.

Let $z=x+i y$ be a complex number. Then

$$
\begin{array}{cc}
\cos (-z)=\cos z, & \sin (-z)=-\sin z \\
\cos (z+2 \pi)=\cos z & \sin (z+2 \pi)=\sin z \\
\sin \left(z+\frac{\pi}{2}\right)=\cos z \\
e^{i z}=\cos z+i \sin z \\
\cos ^{2} z+\sin ^{2} z=1
\end{array}
$$

Proof To prove the first identity in (4), we appeal to (2):

$$
\cos (-z)=\frac{e^{i(-z)}+e^{-i(-z)}}{2}=\frac{e^{-i z}+e^{i z}}{2}=\frac{e^{i z}+e^{-i z}}{2}=\cos z .
$$

The second identity in (4) is proved similarly by appealing to (3) (Exercise 25). In proving (5), we will use the fact that $e^{ \pm 2 \pi i}=1$. We have

$$
\cos (z+2 \pi)=\frac{e^{i(z+2 \pi)}+e^{-i(z+2 \pi)}}{2}=\frac{e^{i z} e^{2 \pi i}+e^{-i z} e^{-2 \pi i}}{2}=\frac{e^{i z}+e^{-i z}}{2}=\cos z
$$

This proves the first identity in (5). The proof of second the identity in (5) is similar (Exercise 26). To prove (6), we calculate

$$
\sin \left(z+\frac{\pi}{2}\right)=\frac{e^{i(z+\pi / 2)}-e^{-i(z+\pi / 2)}}{2 i}=\frac{i e^{i z}-(-i) e^{-i z}}{2 i}=\cos z
$$

You should recognize (7) as Euler's identity (5), Section 1.3, where we have replaced the real argument $\theta$ by a complex argument $z$. To prove (7), we simply multiply (2) by 2 and (3) by $2 i$ and add the resulting identities.

Identity (8) is the analog of the famous Pythagorean identity relating the real cosine and sine functions. We prove it with a trick based on the complex exponential function, which emphasizes the relationships between the trigonometric and
exponential functions. Using (7), we have

$$
1=e^{i z} e^{-i z}=\overbrace{(\cos z+i \sin z)}^{e^{i z}} \overbrace{(\cos z-i \sin z)}^{e^{-i z}}=\cos ^{2} z+\sin ^{2} z .
$$

The familiar angle-addition and half-angle formulas also apply to the complex cosine and sine.

## TRIGONOMETRIC IDENTITIES

Let $z, z_{1}, z_{2}$ be a complex numbers. Then

$$
\begin{gathered}
\cos \left(z_{1}+z_{2}\right)=\cos z_{1} \cos z_{2}-\sin z_{1} \sin z_{2} \\
\sin \left(z_{1}+z_{2}\right)=\sin z_{1} \cos z_{2}+\cos z_{1} \sin z_{2} \\
\cos ^{2} z=\frac{1+\cos (2 z)}{2} \\
\sin ^{2} z=\frac{1-\cos (2 z)}{2}
\end{gathered}
$$

Proof Expanding the right side of (9), it equals

$$
\frac{\left(e^{i z_{1}}+e^{-i z_{1}}\right)\left(e^{i z_{2}}+e^{-i z_{2}}\right)}{2^{2}}-\frac{\left(e^{i z_{1}}-e^{-i z_{1}}\right)\left(e^{i z_{2}}-e^{-i z_{2}}\right)}{(2 i)^{2}} .
$$

Expanding the numerators and adding the fractions, all terms in $e^{i\left(z_{1}-z_{2}\right)}$ and $e^{i\left(z_{2}-z_{1}\right)}$ cancel and we are left with $\frac{2 e^{i\left(z_{1}+z_{2}\right)}+2 e^{-i\left(z_{1}+z_{2}\right)}}{4}$, which is the same as $\cos \left(z_{1}+z_{2}\right)$. The proof of (10) is similar. Now, setting $z_{1}=z_{2}=z$ in (9) yields

$$
\cos 2 z=\cos ^{2} z-\sin ^{2} z .
$$

Replacing $\sin ^{2} z$ by $1-\cos ^{2} z$, we conclude (11). Replacing $\cos ^{2} z$ by $1-\sin ^{2} z$, we conclude (12). $\square$

Up to this point our statements about the complex trigonometric functions have been no different than those statements for real trigonometric functions. Now we show how they can behave differently. From (2), we have, for any real $y$,

$$
\cos (i y)=\frac{e^{i(i y)}+e^{-i(i y)}}{2}=\frac{e^{y}+e^{-y}}{2}=\cosh y
$$

and

$$
\sin (i y)=\frac{e^{i(i y)}-e^{-i(i y)}}{2 i}=i \frac{e^{y}-e^{-y}}{2}=i \sinh y,
$$

where $\cosh y$ and $\sinh y$ are the real hyperbolic functions from calculus. We are now in a position to express $\cos z$ and $\sin z$ in terms of their real and
imaginary parts, and also to compute their moduli.

REAL AND IMAGINARY PARTS AND MODULI OF TRIGONOMETRIC FUNCTIONS

Let $z=x+i y$ be a complex number. Then

$$
\begin{gathered}
\cos z=\cos x \cosh y-i \sin x \sinh y \\
\sin z=\sin x \cosh y+i \cos x \sinh y \\
|\cos z|=\sqrt{\cos ^{2} x+\sinh ^{2} y} \\
|\sin z|=\sqrt{\sin ^{2} x+\sinh ^{2} y}
\end{gathered}
$$

Proof To prove (15), we appeal to (9) and (13)-(14) and write

$$
\begin{aligned}
\cos z & =\cos (x+i y) \\
& =\cos x \cos (i y)-\sin x \sin (i y) \\
& =\cos x \cosh y-i \sin x \sinh y
\end{aligned}
$$

The proof of (16) is similar and is left to Exercise 21. To prove (17), we use (15) and the definition of the modulus of a complex number ((1), Section 1.2). We also use the identity $\cosh ^{2} y-\sinh ^{2} y=1$ for real hyperbolic functions. We get

$$
\begin{aligned}
|\cos z|^{2} & =\cos ^{2} x \cosh ^{2} y+\sin ^{2} x \sinh ^{2} y \\
& =\cos ^{2} x\left(1+\sinh ^{2} y\right)+\sin ^{2} x \sinh ^{2} y \\
& =\cos ^{2} x+\sinh ^{2} y\left(\cos ^{2} x+\sin ^{2} x\right) \\
& =\cos ^{2} x+\sinh ^{2} y
\end{aligned}
$$

The proof of (18) is similar and is left to Exercise 21.
The following example is intended to show you that, unlike $\cos x$ and $\sin x$, the complex functions $\cos z$ and $\sin z$ are not bounded.

EXAMPLE $2 \cos z$ and $\sin z$ are not bounded
Show that $\cos z$ and $\sin z$ are not bounded over the complex plane.
Solution For $z=x+i y$, using (17), we obtain $|\cos z|=\sqrt{\cos ^{2} x+\sinh ^{2} y} \geq \sqrt{\sinh ^{2} y}=|\sinh y|$. Similarly, using (18), we obtain $|\sin z|=\sqrt{\sin ^{2} x+\sinh ^{2} y} \geq \sqrt{\sinh ^{2} y}=|\sinh y|$. As $y \rightarrow \infty$, we have $\sinh y \rightarrow \infty$; and as $y \rightarrow-\infty$, we have $\sinh y \rightarrow-\infty$. Hence $|\cos z|$ and $|\sin z|$ blow up to infinity as $|\operatorname{Im} z|$ tends to infinity.

## EXAMPLE 3 Zeros of the sine and cosine

(a) Show that $\sin z=0 \Leftrightarrow z=k \pi$, for some integer $k$.
(b) Show $\cos z=0 \Leftrightarrow z=\frac{\pi}{2}+k \pi$, for some integer $k$.

Thus $\cos z$ and $\sin z$ have the same zeros as their real counterparts, $\cos x$ and $\sin x$.
Solution (a) Suppose that $z=x+i y$ is a point in the plane and that $\sin z=0$. We know then that $|\sin z|=0$, so by (18) we have $\sin x=0$ and $\sinh y=0$. The real function $\sinh y$ equals zero $\Leftrightarrow y=0$, and the real function $\sin x$ equals zero $\Leftrightarrow x=k \pi$ for some integer $k$. Hence (a) holds.
(b) Now that we have the zeros of the sine, we can easily find the zeros of the cosine using (6). We have

$$
\begin{aligned}
\cos z=0 & \Leftrightarrow \sin \left(z+\frac{\pi}{2}\right)=0 \\
& \Leftrightarrow z+\frac{\pi}{2}=k \pi, \text { for some integer } k \\
& \Leftrightarrow z=-\frac{\pi}{2}+k \pi, \text { for some integer } k
\end{aligned}
$$

Replacing $k$ by $k+1$, we obtain (b).
In our next example, we consider a mapping by the function $\sin z$.

## EXAMPLE 4 The mapping $w=\sin z$

Find the image under the mapping $f(z)=\sin z$ of the semi-infinite strip

$$
S=\left\{z=x+i y:-\frac{\pi}{2} \leq x \leq \frac{\pi}{2}, y \geq 0\right\}
$$

Solution As in previous examples of mappings, we will first find the image under $f$ of a simple curve in the domain of definition, often a line segment or line. Then we will sweep the domain of definition with this curve and keep track of the area that is swept by the image. Fix $0 \leq y_{0}<\infty$ and consider the horizontal line segment $E F$ defined by: $y=y_{0},-\frac{\pi}{2} \leq x \leq \frac{\pi}{2}$. Let $u+i v$ denote the image of a point $z=x+i y_{0}$ on $E F$. Using (16), we get

$$
u+i v=\sin \left(x+i y_{0}\right)=\sin x \cosh y_{0}+i \cos x \sinh y_{0}
$$

Hence

$$
u=\sin x \cosh y_{0} \quad \text { and } \quad v=\cos x \sinh y_{0}
$$

If $y_{0}=0$, we see that $v=0$ and $u=\sin x$, which shows that the image of the interval $-\frac{\pi}{2} \leq x \leq \frac{\pi}{2}$ under the mapping $\sin z$ is the interval $-1 \leq u \leq 1$. The case $y_{0}>0$ is more interesting. In this case, we have

$$
\frac{u}{\cosh y_{0}}=\sin x \quad \text { and } \quad \frac{v}{\sinh y_{0}}=\cos x
$$

Note that $v \geq 0$ because $\cos x \geq 0$ for $-\frac{\pi}{2} \leq x \leq \frac{\pi}{2}$. Squaring both equations in (19) then adding them, we get

$$
\left(\frac{u}{\cosh y_{0}}\right)^{2}+\left(\frac{v}{\sinh y_{0}}\right)^{2}=\sin ^{2} x+\cos ^{2} x=1
$$

Hence as $x$ varies in the interval $-\frac{\pi}{2} \leq x \leq \frac{\pi}{2}$, the point $(u, v)$ traces the upper semi-ellipse

$$
\left(\frac{u}{\cosh y_{0}}\right)^{2}+\left(\frac{v}{\sinh y_{0}}\right)^{2}=1, \quad v \geq 0
$$

The $u$-intercepts of the ellipse are at $u= \pm \cosh y_{0}$ and the $v$-intercept is at $v= \sinh y_{0}$. As $y_{0} \rightarrow \infty, \cosh y_{0}$ and $\sinh y_{0}$ tend to $\infty$. And as $y_{0} \rightarrow 0, \sinh y_{0} \rightarrow 0$ and $\cosh y_{0} \rightarrow 1$. So, as $y_{0}$ varies in the interval $0<y_{0}<\infty$, the upper semi-ellipses ${ }^{\text {fill }}$

Figure 1 The mapping $w= \sin z$ takes the horizontal line segment $y=y_{0}>0,-\frac{\pi}{2} \leq x \leq \frac{\pi}{2}$ onto the upper semiellipse

$$
\left(\frac{u}{\cosh y_{0}}\right)^{2}+\left(\frac{v}{\sinh y_{0}}\right)^{2}=1,
$$

$v \geq 0$.

OTHER TRIGONOMETRIC FUNCTIONS
the upper half $w$-plane $v \geq 0$, including the $u$-axis (Figure 1). You should verify (Exercise 23) that the boundary of $S$ gets mapped to the boundary of $f[S]$, namely, the $u$-axis. $\square$
![](13d4bcc6-f973-445e-ad7d-b22a7a43507d-61_411_1220_326_701.jpg)

The other trigonometric functions are defined for complex variables in terms of the cosine and sine in accordance with the real definitions.

With $\cos z=\frac{e^{i z}+e^{-i z}}{2}$ and $\sin z=\frac{e^{i z}-e^{-i z}}{2 i}$, the other trigonometric functions are defined by

$$
\begin{aligned}
& \tan z=\frac{\sin z}{\cos z}(\cos z \neq 0) \\
& \cot z=\frac{\cos z}{\sin z}(\sin z \neq 0)
\end{aligned}
$$

$$
\sec z=\frac{1}{\cos z}(\cos z \neq 0)
$$

$$
\csc z=\frac{1}{\sin z}(\sin z \neq 0)
$$

Like the complex cosine and sine functions, these functions share several properties with their real counterparts. The following is one illustration.

## EXAMPLE $5 \tan z$ is $\pi$-periodic

Show that $\tan z_{1}=\tan z_{2}$ if and only if $z_{1}=z_{2}+k \pi$, where $k$ is an integer.
Solution Note that $\tan z$ is not defined for $z=\frac{\pi}{2}+k \pi$. For $z_{1}, z_{2} \neq \frac{\pi}{2}+k \pi$, we have

$$
\begin{aligned}
\tan z_{1}=\tan z_{2} & \Leftrightarrow \frac{\sin z_{1}}{\cos z_{1}}=\frac{\sin z_{2}}{\cos z_{2}} \\
& \Leftrightarrow \sin z_{1} \cos z_{2}-\cos z_{1} \sin z_{2}=0 \\
& \Leftrightarrow \sin \left(z_{1}-z_{2}\right)=0 \quad \text { (use (10) with } z_{2} \text { replaced by }\left(-z_{2}\right) \text { ) } \\
& \Leftrightarrow z_{1}-z_{2}=k \pi \quad \Leftrightarrow \quad z_{1}=z_{2}+k \pi,
\end{aligned}
$$

where the step before last follows from Example 3(a).

## Hyperbolic Functions

We define the hyperbolic functions for complex variables exactly as we do for real variables:

$$
\cosh z=\frac{e^{z}+e^{-z}}{2} \quad \text { and } \quad \sinh z=\frac{e^{z}-e^{-z}}{2}
$$

The hyperbolic functions satisfy interesting identities. Some of them are extensions of familiar identities for the real hyperbolic functions, and some are new. We illustrate with a brief list.

PROPERTIES OF HYPERBOLIC FUNCTIONS

For any complex number $z=x+i y$, we have

$$
\begin{gathered}
\cosh i z=\cos z \\
\sinh i z=i \sin z \\
\cosh ^{2} z-\sinh ^{2} z=1 \\
=\cosh x \cos y+i \sinh x \sin y \\
=\sinh x \cos y+i \cosh x \sin y
\end{gathered}
$$

These and many more identities (Exercises 35-52) can be proved from the definitions (24). Finally, we define the other hyperbolic functions in terms of $\cosh z$ and $\sinh z$.

OTHER HYPERBOLIC FUNCTIONS

With $\cosh z=\frac{e^{z}+e^{-z}}{2}$ and $\sinh z=\frac{e^{z}-e^{-z}}{2}$, the other hyperbolic functions are defined by

$$
\tanh z=\frac{\sinh z}{\cosh z}(\cosh z \neq 0)
$$

$$
\operatorname{sech} z=\frac{1}{\cosh z}(\cosh z \neq 0)
$$

$$
\operatorname{csch} z=\frac{1}{\sinh z}(\sinh z \neq 0)
$$

$$
\operatorname{coth} z=\frac{\cosh z}{\sinh z}(\sinh z \neq 0)
$$

## Exercises 1.6

In Exercises 1-4, (a) evaluate $\cos z$ and $\sin z$ for the given $z$, using the definitions (2) and (3). (b) Verify that your answers satisfy (15) and (16).

1. $i$.
2. $-2 i$.
3. $\frac{\pi}{2}+2 i$.
4. $\pi-i$.

In Exercises 5-8, for the given $z$, (a) evaluate $\cos z$, $\sin z$, and $\tan z$, using (15) and (16). (b) Compute $|\cos z|$ and $|\sin z|$. (c) Plot the points $\cos z$, $\sin z$, and $\tan z$.
5. $1+i$.
6. $1-i$.
7. $\frac{3 \pi}{2}+i$.
8. $\frac{\pi}{6}-i$.

In Exercises 9-14, express the given function $f(z)$ in the form $f(z)=u(x, y)+ i v(x, y)$, where $u$ and $v$ are the real and imaginary parts of $f(z)$.
9. $\sin (2 z)$.
10. $\cos \left(z^{2}\right)$.
11. $\sin (z)+2 z$.
12. $z \cos z$.
13. $\tan z$.
14. $\sec z$.

In Exercises 15-20, show that the shaded area $S$ in the $z$-plane is mapped to the shaded area in the $w$-plane by the given mapping $f(z)$.
15.

![](13d4bcc6-f973-445e-ad7d-b22a7a43507d-63_419_850_564_195.jpg)
Figure 2

17. 

![](13d4bcc6-f973-445e-ad7d-b22a7a43507d-63_390_850_1056_195.jpg)
Figure 4

19. 

![](13d4bcc6-f973-445e-ad7d-b22a7a43507d-63_386_842_1517_201.jpg)
Figure 6

16. 

![](13d4bcc6-f973-445e-ad7d-b22a7a43507d-63_413_841_566_1140.jpg)
Figure 3

18. 

![](13d4bcc6-f973-445e-ad7d-b22a7a43507d-63_386_843_1054_1138.jpg)
Figure 5

20. 

![](13d4bcc6-f973-445e-ad7d-b22a7a43507d-63_392_845_1509_1134.jpg)
Figure 7

21. Establish (16) and (18).
22. Explain why $\cos z$ and $\sin z$ are not bounded in absolute value.
23. More on Example 4. In this exercise, we study further the mapping $f(z)=\sin z$ of Example 4.
(a) Show that the half-line $x=\frac{\pi}{2}, y \geq 0$, is mapped to the half-line $u \geq 1, v=0$.
(b) Show that the half-line $x=\frac{-\pi}{2}$ is mapped to the half-line $u \leq-1, v=0$.
(c) Conclude that the boundary of the set $S$ in Example 4 is mapped to the boundary of the set $f[S]$.
(d) Recall from your calculus course that an ellipse of the form $\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1$ with $0<b<a$ has its foci at $x= \pm \sqrt{a^{2}-b^{2}}$. Show that all the ellipses in Example 4 have the same foci located on the $u$-axis at $u= \pm 1$.
24. Zeros of hyperbolic functions. Show that

$$
\sinh z=0 \quad \Leftrightarrow \quad z=i k \pi, k \text { an integer; }
$$

and

$$
\cosh z=0 \quad \Leftrightarrow \quad z=i\left(k+\frac{1}{2}\right) \pi, k \text { an integer. }
$$

[Hint: $z$ is a zero of $\sin z \Leftrightarrow i z$ is a zero of the hyperbolic sine (why?). Reason the same way for the cosine.]
In Exercises 25-52, establish the given identity. In establishing an identity with hyperbolic functions, you may want to use the corresponding one for trigonometric functions and the identities (25) and (26).
25. $\sin (-z)=-\sin z$.
26. $\sin (z+2 \pi)=\sin z$.
27. $\cos (z+\pi)=-\cos z$.
28. $\sin (z+\pi)=-\sin z$.
29. $\sin \left(z_{1}+z_{2}\right)=\sin z_{1} \cos z_{2}+\cos z_{1} \sin z_{2}$.
30. $\cos 2 z=\cos ^{2} z-\sin ^{2} z=2 \cos ^{2} z-1=1-2 \sin ^{2} z$.
31. $\sin 2 z=2 \sin z \cos z$.
32. $2 \cos z_{1} \cos z_{2}=\cos \left(z_{1}-z_{2}\right)+\cos \left(z_{1}+z_{2}\right)$.
33. $2 \sin z_{1} \sin z_{2}=\cos \left(z_{1}-z_{2}\right)-\cos \left(z_{1}+z_{2}\right)$.
34. $2 \sin z_{1} \cos z_{2}=\sin \left(z_{1}+z_{2}\right)+\sin \left(z_{1}-z_{2}\right)$.
35. $\cosh (-z)=\cosh z$ and $\sinh (-z)=-\sinh z$.
36. $\cosh (z+2 \pi i)=\cosh z$ and $\sinh (z+2 \pi i)=\sinh z$.
37. $\cosh (z+\pi i)=-\cosh z$ and $\sinh (z+\pi i)=-\sinh z$.
38. $\sinh \left(z+\frac{i \pi}{2}\right)=i \cosh z$ and $\cosh \left(z+\frac{i \pi}{2}\right)=i \sinh z$.
39. $e^{z}=\cosh z+\sinh z$. 40. $\cosh ^{2} z-\sinh ^{2} z=1$.
41. $\cosh 2 z=\cosh ^{2} z+\sinh ^{2} z=2 \cosh ^{2} z-1=1+2 \sinh ^{2} z$.
42. $\sinh 2 z=2 \sinh z \cosh z$.
43. $\cosh ^{2} z=\frac{1+\cosh 2 z}{2}$.
44. $\sinh ^{2} z=\frac{-1+\cosh 2 z}{2}$.
45. $\cosh \left(z_{1}+z_{2}\right)=\cosh z_{1} \cosh z_{2}+\sinh z_{1} \sinh z_{2}$.
46. $\sinh \left(z_{1}+z_{2}\right)=\sinh z_{1} \cosh z_{2}+\cosh z_{1} \sinh z_{2}$.
47. $2 \cosh z_{1} \cosh z_{2}=\cosh \left(z_{1}+z_{2}\right)+\cosh \left(z_{1}-z_{2}\right)$.
48. $2 \sinh z_{1} \sinh z_{2}=\cosh \left(z_{1}+z_{2}\right)-\cosh \left(z_{1}-z_{2}\right)$.
49. $2 \sinh z_{1} \cosh z_{2}=\sinh \left(z_{1}+z_{2}\right)+\sinh \left(z_{1}-z_{2}\right)$.
50. $\cosh z=\cosh x \cos y+i \sinh x \sin y$, and $\sinh z=\sinh x \cos y+i \cosh x \sin y$.
51. $|\cosh z|=\sqrt{\sinh ^{2} x+\cos ^{2} y}$.
52. $|\sinh z|=\sqrt{\sinh ^{2} x+\sin ^{2} y}$.
53. Show that either $\tan z=i$ or $\tan z=-i$ has no solution. [Hint: Use (15) and (16).]

### 1.7 Logarithms and Powers

In this section we define the complex logarithms and define what it means to raise a complex number to a complex power. Thus we will be able to compute expressions like $\log i$ and $i^{i}$.

The logarithm was defined in elementary algebra as the inverse of the exponential function. We will follow this idea in defining the complex logarithm, $\log z$ for $z \neq 0$. Thus,

$$
w=\log z \quad \Leftrightarrow \quad e^{w}=z .
$$

To determine $w$ in terms of $z$, write $w=u+i v$ and $z=r e^{i \theta}$, with $|z|=r>0$ and $\theta=\arg z$. Then (1) becomes

$$
e^{u} e^{i v}=r e^{i \theta}
$$

and hence

$$
e^{u}=r \quad \text { and } \quad e^{i v}=e^{i \theta}
$$

The first equation gives $u=\ln r$, where here $\ln r$ denotes the usual natural logarithm of the positive number $r$. The second equation in (2) tells us that $v$ and $\theta$ differ by an integer multiple of $2 \pi$, because the complex exponential is $2 \pi i$ periodic. So $v=\theta+2 k \pi$, where $k$ is an integer, or simply $v=\arg z$. Putting this together, we obtain the formula for the complex logarithm:

$$
\log z=\ln |z|+i \arg z \quad(z \neq 0)
$$

Unlike the real logarithm, this formula defines a multiple-valued function, because $\arg z$ is multiple-valued. The complex logarithm is not a function in our usual sense of the word, since in our understanding a function is a rule that assigns to a given complex number $z$ a single number. We can make the function defined by (3) single-valued by specifying a single-valued $\arg z$. For example, we can use the principal value of the argument by specifying that $-\pi<\arg z \leq \pi$ (see (9), Section 1.3). The corresponding function that we obtain in (3) is called the principal value or principal branch of the logarithm and is denoted by $\log z$. Thus

$$
\log z=\ln |z|+i \operatorname{Arg} z \quad(z \neq 0)
$$

Recalling that $\arg z=\operatorname{Arg} z+2 k \pi$, where $k$ is an integer, we see from (3) and (4) that all the values of $\log z$ differ from the principal value by $2 k \pi i$. Thus

$$
\log z=\log z+2 k \pi i \quad(z \neq 0)
$$

## EXAMPLE 1 Evaluating logarithms

Find the following logarithms.
(a) $\log i$.
(b) $\quad \log i$.
(c) $\quad \log (1+i)$.
(d) $\quad \log (-2)$.

Solution (a) The polar form of $i$ is $i=e^{i \frac{\pi}{2}}$. So $|i|=1$ and $\arg i=\frac{\pi}{2}+2 k \pi$, where $k$ is an integer. Hence, by (3),

$$
\log i=\overbrace{\ln (1)}^{=0}+i\left(\frac{\pi}{2}+2 k \pi\right)=i\left(\frac{\pi}{2}+2 k \pi\right) .
$$

As expected, $\log i$ takes on an infinite number of values, all of which happen to be purely imaginary.
(b) The principal argument of $i$ is $\operatorname{Arg} i=\frac{\pi}{2}$. Thus, according to (4),

$$
\log i=\ln (1)+i \frac{\pi}{2}=i \frac{\pi}{2} .
$$

Note that $\log i$ is single-valued and equal to one of the values of $\log i$.
(c) We will apply (4) after putting $1+i$ in polar form. As you can easily check, $1+i=\sqrt{2} e^{i \frac{\pi}{4}}$, where $\frac{\pi}{4}$ is the principal argument of $1+i$. Applying (4), we get

$$
\log (1+i)=\ln (\sqrt{2})+i \frac{\pi}{4}=\frac{1}{2} \ln 2+i \frac{\pi}{4} .
$$

(d) You should have no problem evaluating Log (-2) by applying (4). Appreciate, however, that the complex logarithm, unlike its real counterpart, is defined for negative numbers. We have

$$
-2=2 e^{i \pi} \Rightarrow \log (-2)=\ln (2)+i \pi .
$$ $\square$

As you can imagine, we could have specified a different range of values of $\arg z$ in defining a logarithmic function out of (3). In fact, given any real number $\alpha$, we can specify that $\alpha<\arg z \leq \alpha+2 \pi$. This will assign a single value to $\arg z$, denoted by $\arg _{\alpha} z$. For $z \neq 0$, using $\arg _{\alpha} z$ in (3), we obtain the corresponding function, called a branch of the logarithm,

$$
\log _{\alpha} z=\ln |z|+i \arg _{\alpha} z, \quad \text { where } \alpha<\arg _{\alpha} z \leq \alpha+2 \pi .
$$

For example, for $\alpha=\frac{3 \pi}{4}$, we have $\frac{3 \pi}{4}<\arg _{\frac{3 \pi}{4}} z \leq \frac{3 \pi}{4}+2 \pi$. If we want to compute $\log _{\frac{3 \pi}{4}}(i)$, we first compute

$$
\arg _{\frac{3 \pi}{4}}(i)=\frac{5 \pi}{2} .
$$

Then from (6)

$$
\log _{\frac{3 \pi}{4}}(i)=\ln 1+i \frac{5 \pi}{2}=i \frac{5 \pi}{2} .
$$

Figure 1 For $\alpha$ real, the fundamental region $S_{\alpha}$ of $e^{z}$ is the infinite horizontal strip
$S_{\alpha}=\{z: \alpha<\operatorname{Im} z \leq \alpha+2 \pi\}$.
The upper boundary line, $\operatorname{Im} z=\alpha+2 \pi$, is included in $S_{\alpha}$, but the lower boundary line, $\operatorname{Im} z=\alpha$, is not. If we were to include the line $\operatorname{Im} z=\alpha$, then $e^{z}$ would cease to be one-to-one in the region.

To discuss the mapping properties of the logarithm, you should check that for any real $\alpha$, the exponential function maps the period strip or fundamental region

$$
S_{\alpha}=\{z=x+i y: \alpha<y \leq \alpha+2 \pi\}
$$

one-to-one onto the complex plane minus the origin, which we write as $\mathbb{C} \backslash \{0\}$. Thus the branch of the logarithm $\log _{\alpha} z$ maps the punctured plane $\mathbb{C} \backslash\{0\}$ back onto the fundamental region $S_{\alpha}$ (see Figure 1).
![](./images/13d4bcc6-f973-445e-ad7d-b22a7a43507d-67_486_1217_626_749.jpg)

## Complex Powers

In direct analogy with calculus, for a complex number $z \neq 0$, we define the complex power

$$
z^{a}=e^{a \log z} \quad(z \neq 0)
$$

where $\log z$ is the complex $\log$ arithm (3). Since $\log z$ is multiple-valued, it follows from (8) that $z^{a}$ is in general multiple-valued. By specifying a branch of the logarithm, we obtain a single-valued branch of the complex power function from (8). In particular, if we choose the principal logarithm (4), we obtain the principal value of $z^{a}$ :

$$
z^{a}=e^{a \log z} \quad(z \neq 0)
$$

## EXAMPLE 2 Evaluating complex powers

Compute $(-i)^{1+i}$ using (a) the principal branch of the logarithm; (b) the branch of the logarithm with a branch cut at angle $\alpha=0$.
Solution (a) Using (9), we find

$$
(-i)^{1+i}=e^{(1+i) \log (-i)}=e^{(1+i)\left(-\frac{i \pi}{2}\right)}=e^{\frac{\pi}{2}} e^{-\frac{i \pi}{2}}=-i e^{\frac{\pi}{2}} .
$$

(b) Using the logarithm with a branch cut at angle 0 in (8), we have

$$
(-i)^{1+i}=e^{(1+i) \log _{0}(-i)}=e^{(1+i) \frac{3 i \pi}{2}}=e^{-\frac{3 \pi}{2}} e^{3 \frac{i \pi}{2}}=-i e^{-\frac{3 \pi}{2}},
$$

which is a different value from the one we found in (a).
For $z \neq 0$, is the function $z^{a}$, defined by (8), always multiple-valued? $\mathrm{T}_{0}$ answer this question, let us use the formula for $\log z$ from (5) and write

$$
z^{a}=e^{a \log z}=e^{a(\log z+2 k \pi i)}=e^{a \log z} e^{2 k a \pi i}
$$

where $k$ is an integer. To determine the number of distinct values of $z^{a}$, we must determine the number of distinct values taken by $e^{2 k a \pi i}$ as $k$ varies over the integers. We distinguish three cases.

Case (i): $a$ is a (real) integer. Then $2 k a \pi i$ is an integer multiple of $2 \pi i$, and hence $e^{2 k a \pi i}=1$ for all integers $k$. The expression $z^{a}$ has only one value. This result is in concordance with our notion of $z^{n}, z^{-1}$, etc., as being single-valued functions.

Case (ii): $a$ is a (real) rational number. Write $a=\frac{p}{q}$, where $p$ and $q$ are integers and have no common factors. The quantity $e^{2 k a \pi i}=e^{2 \pi i \frac{p k}{q}}$ will have $q$ distinct values, for $k=0,1, \ldots, q-1$ (see Exercise 38). Thus, for each value of $k=0,1, \ldots, q-1$, we obtain a distinct power function

$$
z^{\frac{p}{q}}=e^{\frac{p}{q} \log z} e^{2 \pi i \frac{p k}{q}}
$$

called a branch of $z^{\frac{p}{q}}$. The branch for $k=0$ is called the principal branch of $z^{\frac{p}{q}}$. This result is in concordance with our notion of $n$th roots $z^{1 / n}$; there are $n$ of them. Note also that case (i) is just case (ii) with $q=1$.

Case (iii): $a$ is a complex number not of either of the preceding two types. This is the case when $a$ is an irrational real number or a complex number with a nonzero imaginary part. Then the quantities $e^{2 k a \pi i}$ are distinct for all integers $k$ (Exercise 39), and $z^{a}$ has an infinite number of values. As in case (ii), each value of $k$ determines a branch of $z^{a}$, except that here we have infinitely many distinct branches.

Note that our definition of a complex power is inconsistent with our definition of the complex exponential $e^{z}$. According to (8), we can take $e$ and raise it to the power $a$, resulting in

$$
e^{a}=e^{a \log e}=e^{a \ln e} e^{a 2 k \pi i}
$$

which is, in general, multiple-valued. We must distinguish this concept of "raising $e$ to the power $a$ " from our previous, single-valued definition of the "exponential function." As a convention, $e^{z}$ will always refer to the exponential function, unless otherwise stated.

The last example of this section deals with inverse trigonometric functions. These will be computed using complex powers and logarithms, and so they will be multiple-valued in general. For example, the inverse sine of $z$ is any complex number $w=\sin ^{-1} z \operatorname{such}$ that $\sin w=z$. As you will see, the solutions of the last equation form an infinite set, and so $\sin ^{-1} z$ is infinite-valued.

## EXAMPLE 3 Computing the inverse sine function

Show that

$$
\sin ^{-1} z=-i \log \left(i z+\left(1-z^{2}\right)^{\frac{1}{2}}\right)
$$

where the complex logarithm is given by (3). (For a given $z$, the square root takes two values in general, and the complex logarithm is infinite-valued. As a result the inverse sine is infinite-valued.)
Solution We want to solve $\sin w=z$. Recalling the definition of $\sin w$ from (3), Section 1.6, we have

$$
z=\frac{e^{i w}-e^{-i w}}{2 i},
$$

or, after multiplying both sides by $e^{i w}$ and simplifying,

$$
\left(e^{i w}\right)^{2}-2 i z e^{i w}-1=0
$$

This is a quadratic equation in $e^{i w}$, which we can solve by appealing to the quadratic formula (25), Section 1.3:

$$
e^{i w}=i z+\left(1-z^{2}\right)^{\frac{1}{2}}
$$

where the square root has two values in general. The desired identity (11) follows now upon taking logarithms.

Formulas for the inverses of the other trigonometric functions and hyperbolic functions can be derived with varying degrees of difficulty by using the logarithm. See the exercises for an extensive list of these functions.

## Exercises 1.7

In Exercises 1-4, evaluate $\log z$ for the given $z$.

1. $2 i$.
2. $-3-3 i$.
3. $5 e^{i \frac{\pi}{7}}$.
4. $e^{2+i \frac{2 \pi}{11}}$.

In Exercises 5-8, evaluate $\log z$ for the given $z$.
5. $3+i \sqrt{3}$.
6. $e^{3-i \frac{3 \pi}{2}}$.
7. $e^{i \frac{5 \pi}{7}} e^{i \frac{3 \pi}{7}}$.
8. $-\alpha$, where $\alpha>0$.

In Exercises 9-12, evaluate the given logarithm.
9. $\log _{\pi} 1$.
10. $\log _{\sqrt{3}}(1+i)$. 11. $\log _{5}(-i e)$.
12. $\log _{\frac{\pi}{2}} i$.

In Exercises 13-18, solve the given equation.
13. $e^{z}=3$.
14. $e^{-z}=1+i$.
15. $e^{z+3}=i$.
16. $e^{2 z}+3 e^{z}+2=0$.
17. $e^{2 z}+5=0$.
18. $e^{z}=\frac{1+i}{1-i}$.
19. (a) Compute $\log \left(e^{i \pi}\right), \log \left(e^{3 i \pi}\right)$, and $\log \left(e^{5 i \pi}\right)$.
(b) Show that $\log \left(e^{z}\right)=z$ if and only if $-\pi<\operatorname{Im} z \leq \pi$.
20. Show that $\log z=i \arg z$ if and only if $z$ is unimodular.
21. Compute $\log (-1), \log i$, and $\log (-i)$ and conclude that, unlike the identity for the usual real logarithm, in general, $\log \left(z_{1} z_{2}\right)$ is not equal to $\log z_{1}+ \log z_{2}$. The situation is not all that hopeless. See Project Problem 37.
22. For which $\alpha$ is $\log _{\alpha} 1=0$ ?

In Exercises 23-26, evaluate the principal value of the given power.
23. $5^{i}$.
24. $(1+i)^{3+i}$.
25. $(-5)^{1-i}$.
26. $\left(\frac{1+i}{1-i}\right)^{i}$.

In Exercises 27-30, state how many values the given power takes, and find them.
27. $(3 i)^{4}$.
28. $(1+i \sqrt{3})^{\frac{2}{7}}$.
29. $i^{i}$.
30. $(-e)^{\frac{i}{2}}$.
31. Find all solutions of $\cos z=\sin z$.
32. (a) Use the definition (2) from Section 1.6 to find the formula

$$
\cos ^{-1} z=-i \log \left(z+\left(z^{2}-1\right)^{\frac{1}{2}}\right)
$$

(b) Derive an expression for $\cos ^{-1} z$ more quickly using (6) from Section 1.6 and (11) from this section.
33. (a) Verify from the definition (20) in Section 1.6 that, for suitable $w$,

$$
1+i \tan w=\frac{2 e^{i w}}{e^{i w}+e^{-i w}}
$$

(b) Verify similarly that

$$
1-i \tan w=\frac{2 e^{-i w}}{e^{i w}+e^{-i w}}
$$

(c) Divide the quantities in parts (a) and (b) and conclude the formula

$$
\tan ^{-1} z=\frac{i}{2} \log \frac{1-i z}{1+i z} \quad(z \neq \pm i)
$$

34. Verify that

$$
\sinh ^{-1} z=\log \left(z+\left(z^{2}+1\right)^{\frac{1}{2}}\right)
$$

35. Verify that

$$
\cosh ^{-1} z=\log \left(z+\left(z^{2}-1\right)^{\frac{1}{2}}\right)
$$

36. Verify that

$$
\tanh ^{-1} z=\frac{1}{2} \log \frac{1+z}{1-z} \quad(z \neq \pm 1)
$$

[Hint: Consider $1+\tanh w$ and $1-\tanh w$.]
37. Project Problem: Set equations and $\log$ operations. In this problem we define what we mean by an equation like $\log \left(z_{1} z_{2}\right)=\log z_{1}+\log z_{2}$ and see when equations like this are true. For $z \neq 0$, recall that $\log z$ is multiple-valued. Let us denote the set of all values of $\log z$ using set notation, and so by (5)

$$
\log z=\{w: w=\log z+2 k \pi i \text { for some integer } k\} .
$$

Our first example is fully worked out, to help you get the idea. We define the sum of two sets $S_{1}$ and $S_{2}$ to be the set

$$
S_{1}+S_{2}=\left\{z: z=\zeta_{1}+\zeta_{2} \text { for some } \zeta_{1} \in S_{1}, \zeta_{2} \in S_{2}\right\}
$$

With this definition, we will show that

$$
\log \left(z_{1} z_{2}\right)=\log z_{1}+\log z_{2}
$$

Each side of the equation is a set; we must show that they have precisely the same elements. The left side is the set of all $\ln \left|z_{1} z_{2}\right|+i \arg \left(z_{1} z_{2}\right)$. From calculus we know that $\ln \left|z_{1} z_{2}\right|=\ln \left|z_{1}\right|+\ln \left|z_{2}\right|$, and since $\arg \left(z_{1} z_{2}\right)=\operatorname{Arg}\left(z_{1} z_{2}\right)+2 k \pi$, hence

$$
\log \left(z_{1} z_{2}\right)=\left\{z: z=\ln \left|z_{1}\right|+\ln \left|z_{2}\right|+i \operatorname{Arg}\left(z_{1} z_{2}\right)+2 k \pi i \text { for some integer } k\right\} .
$$

Using (18) to figure out the right side, we get

$$
\begin{aligned}
\log z_{1} & +\log z_{2}=\left\{z: z=\ln \left|z_{1}\right|+\ln \left|z_{2}\right|\right. \\
& \left.+i \operatorname{Arg} z_{1}+i \operatorname{Arg} z_{2}+2 k \pi i+2 j \pi i \text { for some integers } j, k\right\}
\end{aligned}
$$

Since $\operatorname{Arg}\left(z_{1} z_{2}\right)$ differs from $\operatorname{Arg} z_{1}+\operatorname{Arg} z_{2}$ by an integer multiple of $2 \pi$, we see that the sets $\log z_{1}+\log z_{2}$ and $\log \left(z_{1} z_{2}\right)$ are the same, and so (19) holds. Now you can apply this technique to the following problems.
(a) The negative of a set $S$ is the set

$$
-S=\{z:-z \in S\} .
$$

With this definition, show that

$$
\log \left(z^{-1}\right)=-\log z
$$

(b) The difference of two sets $S_{1}$ and $S_{2}$ is the set

$$
S_{1}-S_{2}=\left\{z: z=\zeta_{1}-\zeta_{2} \text { for some } \zeta_{1} \in S_{1}, \zeta_{2} \in S_{2}\right\}
$$

With this definition, show that

$$
\log \left(\frac{z_{1}}{z_{2}}\right)=\log z_{1}-\log z_{2}
$$

(c) The scalar product of a set $S$ with the complex number $a$ is the set

$$
a S=\{z: z=a \zeta \text { for some } \zeta \in S\} .
$$

We know from (19) that $\log \left(z^{2}\right)=\log z+\log z$. Show that it is not true that $\log \left(z^{2}\right)=2 \log z$. If we use $S_{1} \supset S_{2}$ to mean that $S_{2}$ is a subset of $S_{1}$, show that

$$
\log \left(z^{2}\right) \supset 2 \log z .
$$

38. Project Problem: Rational powers. In this problem we prove that for rational $a=\frac{p}{q}, p$ and $q$ having no common factors, the expression $z^{a}$ has exactly $q$ distinct values.
(a) Show that all values for $z^{a}$ are of the form $e^{(p / q) \log z} e^{2 k p \pi i / q}$.
(b) Define $E_{n}=e^{2 n p \pi i / q}$, for all integers $n$. Argue that $E_{n}=E_{n+q}$ for all $n$ and hence there can be at most $q$ distinct values for $z^{a}$. Without loss of generality we need only consider $0 \leq n \leq q-1$.

![](./images/13d4bcc6-f973-445e-ad7d-b22a7a43507d-72_475_536_846_93.jpg)
Figure 2 for Exercise 40.

(c) Suppose that $E_{j}=E_{l}$ for some $0 \leq j<l \leq q-1$. Use (14) from Section 1.5 to conclude that

$$
\frac{p(l-j)}{q}=k
$$

for some integer $k$.
(d) Argue that (26) is impossible; for $\frac{p(l-j)}{q}$ to be an integer, all the prime factors of $q$ must be canceled by terms in the numerator. However, $p$ has none of them, and $l-j$ cannot have all of them since $l-j<q$. Conclude that all $E_{n}$ are distinct for $0 \leq n \leq q-1$, and hence $z^{\frac{p}{q}}$ has $q$ distinct values.
39. Project Problem: Nonreal and irrational powers. In this problem we prove that if $\operatorname{Im} a \neq 0$ or $\operatorname{Re} a$ is irrational, $z^{a}$ has an infinite number of values.
(a) Write $a=\alpha+i \beta$ and show that all values for $z^{a}$ are of the form

$$
e^{a \log z} e^{-\beta 2 k \pi} e^{\alpha 2 k \pi i} .
$$

(b) Define $E_{n}=e^{\beta 2 n \pi} e^{\alpha 2 n \pi i}$ for all integers $n$. Argue that if $\beta \neq 0$, then $\left|E_{n}\right|$ are all distinct, and hence all values of $E_{n}$ are distinct. Thus $z^{a}$ has an infinite number of values.
(c) Otherwise, if $\beta=0$ and $\alpha$ is irrational, we have $E_{n}=e^{\alpha 2 n \pi i}$. Suppose $E_{j}=E_{l}$ for some $j<l$. Use (14), Section 1.5, to conclude that $\alpha(l-j)=k$ for some integer $k$. However, this is impossible because $\alpha$ is irrational. Hence all $E_{n}$ are distinct and $z^{a}$ has an infinite number of values.
40. Show that the formula for the inverse tangent (13) holds for real $z$, by using the geometric interpretation of the tangent function and Figure 2.

