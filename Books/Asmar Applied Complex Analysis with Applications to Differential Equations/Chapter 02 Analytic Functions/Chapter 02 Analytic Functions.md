## Topics to Review

In this chapter we will present the fundamental definition of a derivative of a function of a complex variable. Like the definition from calculus, here the derivative will be defined as the limit of a difference quotient (although its existence will have consequences that have no analog in calculus). So it is helpful to review the basic definitions from calculus of limits, continuity, and derivatives.

## Looking Ahead

Complex analysis is about the study of analytic functions. These are functions that have a derivative in an open set. This fundamental notion of analyticity is presented in Section 2.3. Sections 2.1 and 2.2 pave the way for Section 2.3. So you may want to go over them relatively quickly. Section 2.4 contains the Cauchy-Riemann equations, which are fundamental both in theory and applications. Section 2.5 presents some interesting applications of complex analysis to the solution of boundary value problems, more precisely, Dirichlet problems. It is a mixture of theoretical results about analytic and harmonic functions and their applications to the solution of Dirichlet problems. Section 2.5 sets the stage for the applications that will follow in the book and justifies the need for the development of complex analysis. You should at least read through it and try some applications. Section 2.6 contains a proof related to the Cauchy-Riemann equations. It can be skipped without affecting the continuity of the course.

## 2

## ANALYTIC FUNCTIONS

I get up at 4 o'clock each morning and I am busy from then on ... Today I drew the plans for forges that I am to have built in granite. I am also constructing two lighthouses, one on each of the two piers that are located at the entrance of the harbor. I do not get tired of working; on the contrary, it invigorates me and I am in perfect health...
-Augustin Louis Cauchy
In the previous chapter, we introduced complex numbers and complex functions. In this chapter, we begin our analysis of complex functions, which will occupy us through Chapter 6. Most of what we will present is due to Cauchy and was prepared for a course that he taught at the Institut de France in 1814 and later at the Ecole Polytechnique. Cauchy single-handedly defined the derivative and integral of complex functions and developed one of the most fruitful theories of mathematics. As Cauchy developed his theory, he defined for the first time the notion of limit for functions and gave rigorous definitions of continuity and differentiability for real-valued functions, as we now know them in calculus. He also developed on solid foundation the theory of definite integrals and series. With Cauchy began a new age in mathematics, an age of rigor and insistence on mathematical proof.

So who was Cauchy? Augustin Louis Cauchy was born on August 21, 1789 in Paris. He received his early education from his father, Louis-François Cauchy, a master of classical studies. Cauchy entered the Ecole Polytechnique in Paris in 1805 and continued his education as a civil engineer at the Ecole des Ponts et Chaussées. He began his career as a military engineer, working in Napoleon's administration from 1810 to 1813 . His mathematical talents were soon discovered by leading mathematicians, among them was Joseph Louis Lagrange, who persuaded Cauchy to leave his career as an engineer and devote himself to mathematics. Cauchy's mathematical output was phenomenal. He is considered to be one of the greatest mathematicians. His contributions cover many areas of pure and applied mathematics, including the theory of heat, the theory of light, the mathematical theory of elasticity, and fluid dynamics. Cauchy's contributions to modern calculus are so fundamental that he "has come to be regarded as the creator of calculus in the modern sense," from The History of Mathematics, An Introduction, 3rd edition, by David M. Burton (McGraw-Hill, 1997).

### 2.1 Regions of the Complex Plane

In the previous chapter, we defined some elementary functions of a complex variable. An important part of a function is its domain of definition. In calculus, functions were usually defined over intervals. In dealing with functions of a complex variable, intervals will be replaced by subsets of the complex plane. The picture is no longer as simple as the one on the real line. For this reason, it is necessary to understand basic properties of subsets of the complex plane, which will assist us in our analytical study of functions of a complex variable.

## DEFINITION 1 NEIGHBORHOOD

![](af4f9593-dec7-4bc0-8d78-d25500419ec9-02_486_557_1188_109.jpg)
Figure 1 An $r$-neighborhood $B_{r}\left(z_{0}\right)$ does not include the points on the circle

$\left|z-z_{0}\right|=r$.

DEFINITION 2 INTERIOR AND BOUNDARY POINTS

## Open Sets

One very useful definition in this book is that of a neighborhood of a point. It is the analog of an open interval in one dimension.
Let $r>0$ be a positive real number and $z_{0}$ a point in the plane. The $r$-neighborhood of $z_{0}$ is the set of all complex numbers $z$ satisfying

$$
\left|z-z_{0}\right|<r .
$$

We denote this set by $B_{r}\left(z_{0}\right)$.
By interpreting the absolute value as a distance, we see from (1) that $B_{r}\left(z_{0}\right)$ is the disk centered at $z_{0}$ with radius $r>0$. The fact that the inequality in (1) is strict tells us that we should not include the points on the circle $\left|z-z_{0}\right|=r$ as part of the $r$-neighborhood of $z_{0}$. This is indicated in Figure 1, where we used a dashed line to plot the circle $\left|z-z_{0}\right|=r$.

Sometimes we will not specify the value of $r$ and will simply refer to $B_{r}\left(z_{0}\right)$ as a neighborhood of $z_{0}$.

A neighborhood of $z_{0}$ from which we have deleted the center $z_{0}$ is called a deleted neighborhood or punctured neighborhood of $z_{0}$ and is sometimes denoted by $B_{r}^{\prime}\left(z_{0}\right)$. Thus

$$
B_{r}^{\prime}\left(z_{0}\right)=\left\{z: 0<\left|z-z_{0}\right|<r\right\} .
$$

Let $S$ be a subset of the complex numbers. A point $z_{0}$ in $S$ is called an interior point of $S$ if we can find a neighborhood of $z_{0}$ that is wholly contained in $S$. A point $z$ in the complex plane is called a boundary point of $S$ if every neighborhood of $z$ contains at least one point in $S$ and at least one point not in $S$. The set of all boundary points of $S$ is called the boundary of $S$.

From the definitions, every point in $S$ is either an interior point or a boundary point. If a point is an interior point of $S$, then it cannot be a boundary point of $S$. Also, while an interior point of $S$ is necessarily a point in $S$, a boundary point of $S$ need not be in $S$.

![](af4f9593-dec7-4bc0-8d78-d25500419ec9-03_461_506_637_125.jpg)
Figure 2 The point $z$ is an interior point of $B_{r}\left(z_{0}\right)$, while $z_{1}$ is a boundary point.

## DEFINITION 3 OPEN SETS

The geometric concepts in Definition 2 are intuitively clear; however, dealing with them often requires delicate handling of the absolute value.

## EXAMPLE 1 Interior and boundary points

Consider an $r$-neighborhood $B_{r}\left(z_{0}\right)$, where $r>0$.
(a) Show that every point $z$ of $B_{r}\left(z_{0}\right)$ is an interior point.
(b) Show that the boundary of $B_{r}\left(z_{0}\right)$ is the circle $\left|z-z_{0}\right|=r$.

Solution (a) Pick a point $z$ in $B_{r}\left(z_{0}\right)$. It is clear from Figure 2 that we can find a disk centered at $z$, which lies wholly in $B_{r}\left(z_{0}\right)$. Hence $z$ is an interior point of $B_{r}\left(z_{0}\right)$.

If we want to give an analytic proof of this simple geometric argument, here is one way to proceed. Let $\delta=\left|z-z_{0}\right|$. By definition of $B_{r}\left(z_{0}\right)$, we have $0 \leq \delta<r$. Let $\delta^{\prime}=r-\delta$. For any $w$ in the neighborhood $B_{\delta^{\prime}}(z)$, we have $|w-z|<\delta^{\prime}$ and so, by the triangle inequality,

$$
\left|w-z_{0}\right| \leq|w-z|+\left|z-z_{0}\right|<\delta^{\prime}+\delta=r .
$$

Hence $w$ belongs to $B_{r}\left(z_{0}\right)$, and since this is true of every $w$ in $B_{\delta^{\prime}}(z)$, we conclude that $B_{\delta^{\prime}}(z)$ is contained in $B_{r}\left(z_{0}\right)$
(b) Pick a point $z_{1}$ on the circle $\left|z-z_{0}\right|=r$. It is clear from Figure 2 that every disk centered at $z_{1}$ will contain (infinitely many) points in $B_{r}\left(z_{0}\right)$ and (infinitely many) points not in $B_{r}\left(z_{0}\right)$. Hence every point on the circle $\left|z-z_{0}\right|$ is a boundary point of $B_{r}\left(z_{0}\right)$.

We now show that no other points are boundary points. Since points inside the circle are interior points, they cannot be boundary points. Also, given a point outside the circle we can enclose it in a disk that does not intersect the disk $B_{r}\left(z_{0}\right)$. Hence such a point is not a boundary point.

Note that in this example, none of the boundary points of $B_{r}\left(z_{0}\right)$ belong to $B_{r}\left(z_{0}\right)$.

We come now to an important definition.
A subset $S$ of the complex numbers is called open if every point in $S$ is an interior point of $S$.

Thus $S$ is open if around each point $z$ in $S$ you can find a neighborhood $B_{r}(z)$ that is wholly contained in $S$. The radius of $B_{r}(z)$ depends on $z$. Here are some useful examples to keep in mind.

- The empty set, denoted as usual by $\emptyset$, is open. Because there are no points in $\emptyset$, the definition of open sets is vacuously satisfied.
- The set of all complex numbers $\mathbb{C}$ is open.
- Any $r$-neighborhood, $B_{r}\left(z_{0}\right)$, is open. We just verified in Example 1(a) that every point in $B_{r}\left(z_{0}\right)$ is an interior point.
- The set of all $z$ such that $\left|z-z_{0}\right|>r$ is open. This set is called a neighborhood of $\infty$. To justify this terminology, see Exercise 23.
![](af4f9593-dec7-4bc0-8d78-d25500419ec9-04_520_523_270_86.jpg)

Figure 3 A closed disk includes its boundary, the circle $\left|z-z_{0}\right|=r$.

![](af4f9593-dec7-4bc0-8d78-d25500419ec9-04_529_529_1006_89.jpg)
Figure 4 A set that is neither open nor closed.

An $r$-neighborhood, $B_{r}\left(z_{0}\right)$, is more commonly called an open disk of radius $r$, centered at $z_{0}$.

You can show that a set is open if and only if it contains none of its boundary points (Exercise 18). Sets that contain all of their boundary points are called closed. The complex plane $\mathbb{C}$ and the empty set $\emptyset$ are closed since they trivially contain their empty sets of boundary points. The disk

$$
\left\{z:\left|z-z_{0}\right| \leq r\right\}
$$

is closed because it contains all its boundary points consisting of the circle $\left|z-z_{0}\right|=r$ (Figure 3). We will refer to such a disk as the closed disk of radius $r$, centered at $z_{0}$.

Some sets are neither open nor closed. For example, the set

$$
\left\{z:\left|z-z_{0}\right| \leq r ; \operatorname{Im} z>0\right\}
$$

contains the boundary points on the upper semicircle, but it does not contain the points on the $x$-axis. Hence, this set is neither open nor closed (Figure 4).

For our next topic and for use throughout this book, it will be convenient to introduce some set notation. If a point $z$ is in a set $S$, we say that $z$ is an element of $S$ and write $z \in S$. If $z$ does not belong to $S$, we will write $z \notin S$. Let $A$ and $B$ be two sets of complex numbers. The union of $A$ and $B$, denoted $A \cup B$, is the set

$$
A \cup B=\{z: z \in A \text { or } z \in B\} .
$$

The intersection of $A$ and $B$, denoted $A \cap B$, is the set

$$
A \cap B=\{z: z \in A \text { and } z \in B\} .
$$

Two sets $A$ and $B$ are disjoint if $A \cap B=\emptyset$. The set difference between $A$ and $B$ is the set

$$
A \backslash B=\{z: z \in A \text { and } z \notin B\} .
$$

We will say that $A$ is a subset of $B$ or that $B$ contains $A$ and write $A \subset B$ or $B \supset A$ if every element of $A$ is also an element of $B: z \in A \Rightarrow z \in B$.

## Connected Sets

A basic result from calculus states that if $f^{\prime}(x)=0$ for all $x$ in $(a, b)$, then $f$ is a constant. This result is not true if the domain of definition of the function is not connected. For example, consider the function

$$
f(x)= \begin{cases}1 & \text { if } 0<x<1 \\ -1 & \text { if } 2<x<3\end{cases}
$$

DEFINITION 4 POLYGONALLY CONNECTED SETS

DEFINITION 5 REGIONS

PROPOSITION 1 CHARACTERIZATION OF REGIONS

![](af4f9593-dec7-4bc0-8d78-d25500419ec9-05_455_500_1415_104.jpg)
Figure 5 An open annulus $A_{r_{1}, r_{2}}\left(z_{0}\right)$ is a region. Note how two arbitrary points $A$ and $B$ in $A_{r_{1}, r_{2}}\left(z_{0}\right)$ can be joined by a polygonal line contained in the annulus.

whose domain of definition is $(0,1) \cup(2,3)$. We have $f^{\prime}(x)=0$ for all $x$ in $(0,1) \cup(2,3)$, but clearly $f$ is not constant. This example shows you how crucial connectedness is in calculus. For subsets of the plane, one way to define connectedness is as follows.

A subset $S$ of the complex plane is called polygonally connected or connected if any two points in $S$ can be joined by a polygonal line consisting of a finite number of line segments joined end to end and wholly contained in $S$ (Figure 6).

The following definition combines two important properties.
A nonempty subset $S$ of the complex plane is called a region (or domain) if it is open and connected.

Caution: Some authors use the term domain instead of region and use the term region to denote a subset of the complex plane that may be open or closed. In this book, it is important to keep in mind that regions are always open. The term domain will be used only in connection with its usual meaning as in "domain of definition" of a function.

Connected open sets or regions have the following useful characterization, which is intuitively clear. Its proof is left as an exercise.
A nonempty open subset $S$ of the complex plane is a region if and only if it cannot be written as the disjoint union of two nonempty open subsets. Equivalently, if $S$ is a region (nonempty connected open subset of $\mathbb{C}$ ) and $S=A \cup B$, where $A$ and $B$ are open and disjoint, then either $A=\emptyset$ or $B=\emptyset$.

Here are some useful examples of regions.

- An open disk $B_{r}\left(z_{0}\right)$ is a region.
- A punctured disk centered at $z_{0}, B_{r}^{\prime}\left(z_{0}\right)=\left\{z: 0<\left|z-z_{0}\right|<r\right\}$, is a region.
- An open annulus centered at $z_{0}$,

$$
A_{r_{1}, r_{2}}\left(z_{0}\right)=\left\{z: r_{1}<\left|z-z_{0}\right|<r_{2}\right\}
$$

is a region (Figure 5).

- The open upper half-plane $\{z: \operatorname{Im} z>0\}$ is a region.
- The complex plane is a region.

Here are sets that are not regions.

- A closed disk is not a region because it is not open.
- The union of two disjoint open disks (for example, $B_{1}(0) \cup B_{\frac{1}{2}}(2 i)$ ) is not a region because it is not connected.
- An interval $(a, b)$ is not a region because it is not an open subset of the complex plane.
We end the section with an application of connectedness to functions of two variables. This is our generalization to two dimensions of the fact that a function with zero derivative is constant.

Suppose that $u(x, y)$ is a real-valued function of $(x, y)$ defined on a nonempty open set $\Omega$. If we fix $y$, we can think of $u$ as a function of $x$

The limit in (2) involves the values of $u$ at the point ( $x+ h, y)$. You should convince yourself that this point belongs to $\Omega$ if $h$ is sufficiently small, because $\Omega$ is open. It is in this sense that we will interpret expressions involving limits.

## THEOREM 1

![](af4f9593-dec7-4bc0-8d78-d25500419ec9-06_508_562_1818_97.jpg)
Figure 6 Joining two points in a connected region by a polygonal line.

$$
\frac{\partial u}{\partial x}=\lim _{h \rightarrow 0} \frac{u(x+h, y)-u(x, y)}{h} .
$$

Similarly, we can fix $x$, think of $u(x, y)$ as a function of $y$, and take its partial derivative with respect to $y$. Thus

$$
\frac{\partial u}{\partial y}=\lim _{h \rightarrow 0} \frac{u(x, y+h)-u(x, y)}{h} .
$$

Suppose that $u$ is a real-valued function defined over a region $\Omega$ such that $u_{x}(x, y)=0$ and $u_{y}(x, y)=0$ for all $(x, y)$ in $\Omega$. Then $u(x, y)$ is constant for all $(x, y)$ in $\Omega$.
Proof As a motivation, let us first recall the proof of the corresponding one dimensional result: If $f^{\prime}(x)=0$ for all $x$ in $(a, b)$, then $f(x)=c$ for all $x$ in $(a, b)$. Fix a point $x_{0}$ in $(a, b)$. Let $x$ be in $(a, b)$, and say $a<x<x_{0}<b$. The mean value theorem asserts that there is a point $x_{1}$ in ( $x, x_{0}$ ) such that

$$
f\left(x_{0}\right)-f(x)=f^{\prime}\left(x_{1}\right)\left(x_{0}-x\right)
$$

Since $f^{\prime}$ is identically zero in $\left(x, x_{0}\right)$, we conclude that $f\left(x_{0}\right)-f(x)=0$ or $f(x)= f\left(x_{0}\right)$. The case $x<x_{0}<b$ is treated similarly, and we obtain that $f(x)=f\left(x_{0}\right)$ for all $x$ in ( $a, b$ ). In other words, $f$ is constant in ( $a, b$ ).

This simple proof can be repeated in higher dimensions. What we need is a mean value theorem in higher dimensions. One form of this theorem is proved in Section 2.6, Theorem 5. According to that theorem, if $A=\left(x_{1}, y_{1}\right)$ and $B=$ ( $x_{2}, y_{2}$ ) are two points in $\Omega$ such that the line segment $A B$ is also in $\Omega$, then there exists a point $C=\left(x_{3}, y_{3}\right)$ on the line segment $A B$ such that

$$
u\left(x_{2}, y_{2}\right)-u\left(x_{1}, y_{1}\right)=u_{x}\left(x_{3}, y_{3}\right)\left(x_{2}-x_{1}\right)+u_{y}\left(x_{3}, y_{3}\right)\left(y_{2}-y_{1}\right)
$$

It is now easy to prove Theorem 1. Fix a point $\left(x_{0}, y_{0}\right)$ in $\Omega$. Given a point $(x, y)$ in $\Omega$, connect $\left(x_{0}, y_{0}\right)$ to $(x, y)$ by a finite number of line segments joined end to end and wholly contained in $\Omega$. (Here we have used the fact that $\Omega$ is a region.) Let $\left(x_{j}, y_{j}\right), j=0,1, \ldots, n$ denote the endpoints of the consecutive line segments, starting with $\left(x_{0}, y_{0}\right)$ and ending with $\left(x_{n}, y_{n}\right)=(x, y)$ (see Figure 6). Apply (4) to each line segment and use the fact that the partial derivatives are zero to conclude that $u\left(x_{j-1}, y_{j-1}\right)=u\left(x_{j}, y_{j}\right)$, and hence that $u\left(x_{0}, y_{0}\right)=u(x, y)$. $\square$

![](af4f9593-dec7-4bc0-8d78-d25500419ec9-07_469_509_1748_88.jpg)
Figure 7 For Exercise 22.

## Exercises 2.1

In Exercises 1-4, identify the interior points and boundary points of the given set.

1. $\{z:|z| \leq 1\}$.
2. $\{z: 0<|z| \leq 1\}$.
3. $\{z=x+i y: 0<x<1, y=0\}$.
4. $\{z: 1<|z-i| \leq 2\}$.

In Exercises 5-12, draw the given set of points. Is the set open? closed? connected? a region? Justify your answers.
5. $\{z: \operatorname{Re} z>0\}$.
6. $\{z: \operatorname{Im} z \leq 1\}$.
7. $B_{1}(i) \cup B_{1}(0)$.
8. $\left\{z: z \neq 0,|\operatorname{Arg} z|<\frac{\pi}{4}\right\}$.
9. $\left\{z: z \neq 0,|\operatorname{Arg} z|<\frac{\pi}{4}\right\} \cup\{0\}$.
10. $\{z:|z+5+i|<1\}$.
11. $\{z:|\operatorname{Re}(z+3+i)|>1\}$.
12. $\{z:|z-3 i|>1\}$.

In Exercises 13-16, construct an example to illustrate the given statement.
13. The union of two connected sets need not be connected.
14. A set with an infinite number of points need not have interior points.
15. If $A$ is a subset of $B$, then the boundary of $A$ need not be contained in the boundary of $B$.
16. The boundary of a region could be empty.
17. Prove that a set $S$ is open if and only if its complement, $\mathbb{C} \backslash S$, is closed.
18. Show that a set $S$ is open if and only if it contains none of its boundary points.
19. Suppose that $A_{1}, A_{2}, \ldots$ are open sets. Show that their union

$$
\bigcup_{n=1}^{\infty} A_{n}=\left\{z: z \in A_{n} \text { for some } n\right\}
$$

is also open.
20. (a) Suppose that $A_{1}, A_{2}, \ldots$, are open sets. Show that a finite intersection

$$
\bigcap_{n=1}^{N} A_{n}=\left\{z: z \in A_{n} \text { for all } 1 \leq n \leq N\right\}
$$

is also open. [Hint: Pick a neighborhood that is contained in all the $A_{n}$ 's.]
(b) Show that the infinite intersection

$$
\bigcap_{n=1}^{\infty} A_{n}=\left\{z: z \in A_{n} \text { for all } n\right\}
$$

need not be open. [Hint: Consider $A_{n}=\left\{z:|z|<\frac{1}{n}\right\}$.]
21. Suppose that $A$ and $B$ are two regions with nonempty intersection. Show that $A \cup B$ is also a region.
22. Project Problem: Is it true that if $u_{y}(x, y)=0$ for all $(x, y)$ in a region $\Omega$, then $u(x, y)=\phi(x)$; that is, $u$ depends only on $x$ ? The answer is no in general, as the following counterexamples show.
(a) For $(x, y)$ in the region $\Omega$ shown in Figure 7, consider the function

$$
u(x, y)= \begin{cases}0 & \text { if } x>0, \\ \operatorname{sgn} y & \text { if } x \leq 0,\end{cases}
$$

![](af4f9593-dec7-4bc0-8d78-d25500419ec9-08_296_545_830_103.jpg)

![](af4f9593-dec7-4bc0-8d78-d25500419ec9-08_292_541_1164_105.jpg)
Figure 8 Stereographic projection and the Riemann sphere. For $|z|>1$, the point $z^{*}$ is in the northern hemisphere. For $|z|<1$, the point $z^{*}$ is in the southern hemisphere. For $|z|=1$, the points $z$ and $z^{*}$ are coincident.

where the signum function is defined by $\operatorname{sgn} y=-1,0,1$, according as $y<0$, $y=0$, or $y>0$. Show that $u_{y}(x, y)=0$ for all $(x, y)$ in $\Omega$ but that $u$ is not a function of $x$ alone.
(b) Note that in the previous example $u_{x}$ does not exist for $x=0$. We now construct a function over the same region $\Omega$ for which the partials exist, $u_{y}=0$, and $u$ is not a function of $x$ alone. Show that these properties hold for

$$
u(x, y)= \begin{cases}0 & \text { if } x>0, \\ e^{-1 / x^{2}} \operatorname{sgn} y & \text { if } x \leq 0 .\end{cases}
$$

(c) Come up with a general condition on $\Omega$ that guarantees that whenever $u_{y}=0$ on $\Omega$ then $u$ depends only on $x$. [Hint: Use the mean value theorem as applied to vertical line segments in $\Omega$.]
23. Project Problem: Stereographic projection. Suppose that a sphere of radius one, called a Riemann sphere, is positioned on the complex plane with its equator coinciding with the unit circle (Figure 8). Let $N$ be the north pole of the sphere and let $z$ be any point in the complex plane. The line from $N$ to $z$ intersects the sphere at one other point $z^{\star}$. Conversely, if $z^{\star}$ is any point of the sphere other than the north pole, then the line from $N$ to $z^{\star}$ will intersect the plane at a single point $z$. It is not difficult to convince yourself that the mapping $P$ that takes $z^{\star}$ to $z$ is one-to-one from the sphere minus the north pole onto the complex plane. This mapping, known as the stereographic projection, was introduced by the German mathematician Bernhard Riemann (1826-1866). It enables us to represent points in the complex plane by points on the sphere, and vice versa. This also suggests that we introduce the point at infinity, $z=\infty$, as the image of the north pole by the stereographic projection. Thus $P(N)=\infty$. The complex plane together with this point at infinity is called the extended complex plane and written $\mathbb{C} \cup\{\infty\}$. It is in one-to-one correspondence with the whole sphere. As you will now discover, several issues concerning $\infty$ can be clarified by thinking in terms of the sphere and its projections. Answer parts (a)-(e) by using geometric reasoning with the help of Figure 8.
(a) Consider a circle $C$ on the sphere that is parallel to the complex plane (these are called parallels of latitude). What is its image under $P$ ?
(b) Which points on the sphere are mapped to the set of all $z$ in the plane such that $|z|>R$. Can you now justify the terminology "neighborhood of infinity"?
(c) What is the image under $P$ of a great circle passing through the poles?
(d) What is the image under $P$ of a circle passing through the north pole but not the south pole?
(e) Argue geometrically that $z^{\star}$ approaches $N$ if and only if $P\left(z^{\star}\right) \rightarrow \infty$.

Your answers in (a)-(e) can be justified also with the help of the formulas that you will derive in parts (f)-(h).
(f) Let $z^{\star}=\left(x_{1}, x_{2}, x_{3}\right)$ and $P\left(z^{\star}\right)=x+i y=(x, y)$. Show that the equation of the line through $z^{\star}$ and $z$ is

$$
\frac{x_{1}-0}{x-0}=\frac{x_{2}-0}{y-0}=\frac{x_{3}-1}{0-1} .
$$

(g) Use $(f)$ and the equation of the Riemann sphere $x_{1}^{2}+x_{2}^{2}+x_{3}^{2}=1$ to derive

$$
x_{1}=\frac{2 x}{x^{2}+y^{2}+1}, \quad x_{2}=\frac{2 y}{x^{2}+y^{2}+1}, \quad x_{3}=1-\frac{2}{x^{2}+y^{2}+1}
$$

(h) Conversely, solve for $x$ and $y$ in (f) and get

$$
x=\frac{x_{1}}{1-x_{3}}, \quad y=\frac{x_{2}}{1-x_{3}}
$$

### 2.2 Limits and Continuity

When we define the derivative of a complex-valued function in Section 2.3, we will model our definition after the familiar derivative of a real-valued function from calculus. As you recall, such a derivative was defined by taking limits. Therefore, before we study differentiation, we must define limits of complex functions. We will also define continuous functions by appealing to limits.

DEFINITION 1 LIMITS OF COMPLEX-VALUED FUNCTIONS

Figure 1 To say that $f(z) \rightarrow L$ as $z \rightarrow z_{0}$ is a strong assertion; it states that no matter how $z$ approaches $z_{0}$ (and there are many possible ways in the plane), the distance from $f(z)$ to $L$ will tend to zero. By contrast, for limits of functions on the real line, a point $x$ can approach $x_{0}$ from only two directions.

We say that a complex-valued function $f(z)$ has a limit $L$ as $z$ approaches $z_{0}$, and we write

$$
\lim _{z \rightarrow z_{0}} f(z)=L \quad \text { or } \quad f(z) \rightarrow L \text { as } z \rightarrow z_{0},
$$

if given any $\epsilon>0$, there exists a $\delta>0$ such that

$$
|f(z)-L|<\epsilon \quad \text { whenever } 0<\left|z-z_{0}\right|<\delta .
$$

If the limit of a function exists at a point, then it is unique (Exercise 27). This is referred to as the uniqueness property of limits.
![](af4f9593-dec7-4bc0-8d78-d25500419ec9-09_461_1109_1442_746.jpg)

Geometrically, interpreting the absolute value $|f(z)-L|$ as the distance between $f(z)$ and $L$, we see from (1) that the function $f(z)$ has limit $L$ as $z \rightarrow z_{0}$ if and only if the distance from $f(z)$ to $L$ tends to zero as $z$ tends to $z_{0}$. Thus, $\lim _{z \rightarrow z_{0}} f(z)=L$ if and only if

$$
\lim _{z \rightarrow z_{0}}|f(z)-L|=0
$$

Note that in (1) the value of $f$ at $z_{0}$ is immaterial, and in fact $f$ need not even be defined at $z_{0}$. Note also that the expression $|f(z)-L|$ that appears
in (1) and (2) is real-valued. So even though we will be computing limits of complex-valued functions, we will be working with real quantities.

## EXAMPLE 1 Two simple limits

Prove that:
(a) $\lim _{z \rightarrow z_{0}} z=z_{0}$; and (b) $\lim _{z \rightarrow z_{0}} c=c$, where $c$ is a constant.

Solution (a) Given $\epsilon>0$, we want to pick a $\delta>0$ so that

$$
0<\left|z-z_{0}\right|<\delta \Rightarrow|f(z)-L|<\epsilon .
$$

Identifying $f(z)=z$ and $L=z_{0}$, this becomes

$$
0<\left|z-z_{0}\right|<\delta \Rightarrow\left|z-z_{0}\right|<\epsilon .
$$

Clearly, the choice $\delta=\epsilon$ will do.
For (b), the inequality $|f(z)-L|=|c-c|<\epsilon$ holds for any choice of $\delta$, which shows that $\lim _{z \rightarrow z_{0}} c=c$. $\square$

Computing more complicated limits by recourse to the $\epsilon \delta$-definition (1) is not always easy. To simplify this task, we will use properties of limits.

## THEOREM 1 OPERATIONS WITH LIMITS

Suppose $\lim _{z \rightarrow z_{0}} f(z)$ and $\lim _{z \rightarrow z_{0}} g(z)$ both exist and $c_{1}, c_{2}$ are complex constants, Then
(3)

$$
\lim _{z \rightarrow z_{0}}\left[c_{1} f(z)+c_{2} g(z)\right]=c_{1} \lim _{z \rightarrow z_{0}} f(z)+c_{2} \lim _{z \rightarrow z_{0}} g(z),
$$

$$
\lim _{z \rightarrow z_{0}}[f(z) g(z)]=\lim _{z \rightarrow z_{0}} f(z), \lim _{z \rightarrow z_{0}} g(z),
$$

(5) $\lim _{z \rightarrow z_{0}}\left[\frac{f(z)}{g(z)}\right]=\frac{\lim _{z \rightarrow z_{0}} f(z)}{\lim _{z \rightarrow z_{0}} g(z)}$, provided $\lim _{z \rightarrow z_{0}} g(z) \neq 0$.

If $\lim _{z \rightarrow z_{0}} g(z)=w_{0}$ and $\lim _{w \rightarrow w_{0}} f(w)=A$, then
(6)

$$
\lim _{z \rightarrow z_{0}} f(g(z))=A=f\left(\lim _{z \rightarrow z_{0}} g(z)\right)
$$

The function $f(g(z))$ is called the composition of $f$ and $g$ and is also denoted $(f \circ g)(z)$. The proofs of (3)-(6) are similar to the proofs of the corresponding results from calculus. They are left to the exercises. Next, we illustrate these properties with some applications.

THEOREM 2 THE SQUEEZE THEOREM

It is interesting to note that if $h(z)$ is real-valued, then $\left|e^{i h(z)}\right|=1$ no matter how large $h(z)$ is. In Example 3, $h(z)=1 /|z| \rightarrow \infty$ as $z \rightarrow 0$, and still $\left|e^{i /|z|}\right|=1$.

## EXAMPLE 2 Operations on limits

Suppose that $\lim _{z \rightarrow i} f(z)=2+i$ and $\lim _{z \rightarrow i} g(z)=3-i$. Find

$$
L=\lim _{z \rightarrow i}\left[(f(z))^{2}+\frac{(3+i) g(z)}{z}\right]
$$

Solution Since the limits of $f(z), g(z)$, and $z$ all exist as $z \rightarrow i$, and the denominator in the expression (7) tends to $i \neq 0$, we conclude that

$$
\begin{aligned}
L & =\left(\lim _{z \rightarrow i} f(z)\right)^{2}+(3+i) \frac{\lim _{z \rightarrow i} g(z)}{\lim _{z \rightarrow i} z}=(2+i)^{2}+\overbrace{(3+i) \frac{3-i}{i}}^{-i(10)} \\
& =3+4 i-10 i=3-6 i
\end{aligned}
$$

Our next result is an analog of the squeeze theorem from calculus. To state it we will need the following definition. A function $g(z)$ is bounded in a set $S$ if there is a positive real number $M$ such that $|g(z)| \leq M$ for all $z$ in $S$.
(i) Suppose that $f(z) \rightarrow 0$ as $z \rightarrow z_{0}$ and $|g(z)| \leq|f(z)|$ in a deleted neighborhood of $z_{0}$. Then $g(z) \rightarrow 0$ as $z \rightarrow z_{0}$.
(ii) Suppose that $f(z) \rightarrow 0$ as $z \rightarrow z_{0}$ and $g(z)$ is bounded in a deleted neighborhood of $z_{0}$. Then $f(z) g(z) \rightarrow 0$ as $z \rightarrow z_{0}$.
Proof (i) Since $f(z) \rightarrow 0$, given $\epsilon>0$, there is a $\delta$ such that $|f(z)|<\epsilon$ whenever $0<\left|z-z_{0}\right|<\delta$. But since $|g(z)| \leq|f(z)|$, we also have $|g(z)-0|<\epsilon$ whenever $0<\left|z-z_{0}\right|<\delta$, which implies that $g(z) \rightarrow 0$ as $z \rightarrow z_{0}$.
(ii) Since $g$ is bounded in a deleted neighborhood of $z_{0}$, we can find $M>0$ and $r>0$ such that $|g(z)| \leq M$ for $0<\left|z-z_{0}\right|<r$. For $0<\left|z-z_{0}\right|<r$, we have

$$
0 \leq|f(z) g(z)| \leq M|f(z)| .
$$

Since $M|f(z)| \rightarrow 0$, it follows from (i) that $f(z) g(z) \rightarrow 0$.
EXAMPLE 3 An application of the squeeze theorem Compute $\lim _{z \rightarrow 0} y e^{i /|z|}$.

Solution Let $f(z)=y$ and $g(z)=e^{i /|z|}$. As $z \rightarrow 0, f(z) \rightarrow 0$. Also, for $z \neq 0$, since $1 /|z|$ is a purely real number, we have $\left|e^{i /|z|}\right|=1$, by (6), Section 1.5. Thus we can apply (ii) from the squeeze theorem and conclude that

$$
\lim _{z \rightarrow 0} y e^{i /|z|}=0 .
$$

Consider a complex-valued function $f(z)=u(x, y)+i v(x, y)$. It is often advantageous to study the limit of $f$ by using properties of the limits of the real and imaginary parts of $f$. This is possible because of the following fact.

## THEOREM 3 REAL AND IMAGINARY PARTS OF LIMITS

Inequalities (14), Section 1.2, state that for any complex number $w$,

$$
|\operatorname{Re} w| \leq|w|
$$

and

$$
|\operatorname{Im} w| \leq|w| .
$$

Inequality (15), Section 1.2, states that

$$
|w| \leq|\operatorname{Re} w|+|\operatorname{Im} w| .
$$

## DEFINITION 2 LIMITS INVOLVING INFINITY

Given a complex-valued function $f(z)=u(x, y)+i v(x, y)$ and a complex number $L=a+i b$, then
(8) $\lim _{z \rightarrow z_{0}} f(z)=L \Longleftrightarrow \lim _{z \rightarrow z_{0}} u(x, y)=a$ and $\lim _{z \rightarrow z_{0}} v(x, y)=b$.

Thus the existence of one complex-valued limit is equivalent to the existence of two real-valued limits.
Proof Suppose that $\lim _{z \rightarrow z_{0}} f(z)=L$ as $z \rightarrow z_{0}$. By (2), we have

$$
\lim _{z \rightarrow z_{0}}|f(z)-L|=0
$$

Now

$$
|f(z)-L|=|\overbrace{(u(x, y)-a)}^{\operatorname{Re}(f(z)-L)}+i \overbrace{(v(x, y)-b)}^{\operatorname{Im}(f(z)-L)}| .
$$

Appealing to inequalities (14), Section 1.2, we obtain

$$
0 \leq|u(x, y)-a| \leq|f(z)-L| \text { and } 0 \leq|v(x, y)-b| \leq|f(z)-L| .
$$

Since $|f(z)-L| \rightarrow 0$ as $z \rightarrow z_{0}$, it follows from Theorem 2 and (10) that $\mid u(x, y)- a \mid \rightarrow 0$ and $|v(x, y)-b| \rightarrow 0$ as $z \rightarrow z_{0}$. This shows that $u(x, y) \rightarrow a$ and $v(x, y) \rightarrow b$ as $z \rightarrow z_{0}$. For the other direction, we use the inequality

$$
|f(z)-L| \leq|\operatorname{Re}(f(z)-L)|+|\operatorname{Im}(f(z)-L)|=|u(x, y)-a|+|v(x, y)-b|,
$$

which is a consequence of (15), Section 1.2 . As $z \rightarrow z_{0}$, the right side goes to 0 , implying that $|f(z)-L| \rightarrow 0$. $\square$

We have avoided thus far dealing with limits that involve $\infty$. What do we mean by statements such as $\lim _{z \rightarrow z_{0}} f(z)=\infty$ or $\lim _{z \rightarrow \infty} f(z)=L$ or even $\lim _{z \rightarrow \infty} f(z)=\infty$ ? We answer these questions and complete our discussion of limits by introducing the following definitions.
(i) We write $\lim _{z \rightarrow z_{0}} f(z)=\infty$ to mean that for any $M>0$ there is a $\delta>0$ such that $\left|z-z_{0}\right|<\delta \Rightarrow|f(z)|>M$.
(ii) We write $\lim _{z \rightarrow \infty} f(z)=L$ to mean that for any $\epsilon>0$ there is an $R>0$ such that $|z|>R \Rightarrow|f(z)-L|<\epsilon$.
(iii) We write $\lim _{z \rightarrow \infty} f(z)=\infty$ to mean that for any $M>0$ there is an $R>0$ such that $|z|>R \Rightarrow|f(z)|>M$.

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

## EXAMPLE 4 Limits at $\infty$

Find:
(a) $\lim _{z \rightarrow \infty} \frac{z-1}{z+i} ; \quad$ and
(b) $\lim _{z \rightarrow \infty} \frac{2 z+3 i}{z^{2}+z+1}$.

Solution (a) Since we are concerned with the behavior of the function for $|z|$ large, it is safe to divide both numerator and denominator of $\frac{z-1}{z+i}$ by $z$, and we conclude

$$
\begin{aligned}
\lim _{z \rightarrow \infty} \frac{z-1}{z+i} & =\lim _{z \rightarrow \infty} \frac{1-\frac{1}{z}}{1+\frac{i}{z}} \\
& =\frac{1-\lim _{z \rightarrow \infty} \frac{1}{z}}{1+i \lim _{z \rightarrow \infty} \frac{1}{z}} \quad[\text { by (5) and (3)] } \\
& =1 \quad[\text { by (16)]. }
\end{aligned}
$$

(b) Similarly, we divide both numerator and denominator of $\frac{2 z+3 i}{z^{2}+z+1}$ by $z^{2}$ and conclude

$$
\lim _{z \rightarrow \infty} \frac{2 z+3 i}{z^{2}+z+1}=\lim _{z \rightarrow \infty} \frac{\frac{2}{z}+\frac{3 i}{z^{2}}}{1+\frac{1}{z}+\frac{1}{z^{2}}}=\frac{0+0}{1+0+0}=0
$$

While we have successfully used skills from calculus to guide us in taking complex-valued limits, you should be cautioned in using real-variable intuition. For example, the $\operatorname{limit}_{\text {lim }} \lim _{z \rightarrow \infty} e^{-z}$ is not 0 ; in fact, the limit does not exist (Exercise 21).

## DEFINITION 3 CONTINUOUS FUNCTIONS

THEOREM 4 PROPERTIES OF CONTINUOUS FUNCTIONS

## Continuous Functions

Often, the limit of $f(z)$ as $z$ approaches $z_{0}$ will equal $f\left(z_{0}\right)$. Functions that satisfy this requirement are said to be continuous.

Suppose $f(z)$ is defined on a neighborhood of $z_{0}$. We say that $f(z)$ is continuous at the point $z_{0}$ if $\lim _{z \rightarrow z_{0}} f(z)$ exists and equals $f\left(z_{0}\right)$. We say $f$ is continuous on a set $S$ if it is continuous at every point in $S$.

We see from Example 1 that the functions $f(z)=z$ and $f(z)=c$ are continuous at all points in the plane. To check the continuity of more complicated functions, we can appeal to the properties of limits. Since continuity is defined in terms of limits, many properties of limits extend to continuous functions.
(i) If $f(z)$ and $g(z)$ are continuous at $z_{0}$, and $c_{1}, c_{2}$ are complex constants, then the following functions are continuous at $z_{0}$ :

$$
c_{1} f(z)+c_{2} g(z), \quad f(z) g(z), \quad \frac{f(z)}{g(z)}\left(\text { provided } g\left(z_{0}\right) \neq 0\right)
$$

(ii) If $g$ is continuous at $z_{0}$ and $f$ is continuous at $g\left(z_{0}\right)$, then the composition $h(z)=f(g(z))$ is continuous at $z_{0}$.
(iii) If $g(z)$ is real-valued and continuous at $z_{0}$ and $f(x)$ is continuous at $x_{0}=g\left(z_{0}\right)$, then the composition $h(z)=f(g(z))$ is continuous at $z_{0}$.
(iv) The function $f(z)=u(z)+i v(z)$ is continuous if and only if $u$ and $v$ are continuous.

The proofs of (i), (ii), and (iv) follow from Theorems 1 and 3. The proof of (iii) follows from the definitions of continuity for complex- and real-valued functions. We apply these results and check the continuity of polynomials and rational functions.

## EXAMPLE 5 Polynomial and rational functions

(a) Show that a polynomial $p(z)=a_{n} z^{n}+a_{n-1} z^{n-1}+\cdots+a_{0}$ is continuous at all points in the plane.
(b) A rational function is a function of the form

$$
r(z)=\frac{p(z)}{q(z)}
$$

where $p$ and $q$ are polynomials. Show that a rational function is continuous at all points where $q(z) \neq 0$.
Solution (a) Since the function $f(z)=z$ is continuous, we repeatedly use the fact that the product of two continuous functions is continuous to conclude that $z^{2}, z^{3}, \ldots, z^{n}$ are continuous. Then, by repeated applications of the fact that a linear combination of continuous functions is continuous, we conclude that the

![](af4f9593-dec7-4bc0-8d78-d25500419ec9-15_463_496_1517_102.jpg)
Figure 2 If $L \neq L^{\prime}$, then the limit at $z_{0}$ cannot exist.

function $a_{n} z^{n}+a_{n-1} z^{n-1}+\cdots+a_{0}$ is continuous.
(b) By part (a), the polynomials $p(z)$ and $q(z)$ are continuous in the entire plane. Hence $r(z)=\frac{p(z)}{q(z)}$ is continuous in the entire plane except those points where $q(z)=0$. $\square$

## EXAMPLE 6 Limits and continuity of rational functions

For the given rational function $f(z)=p(z) / q(z)$, find the limit and determine if the function is continuous at the given point.
(a) $\lim _{z \rightarrow 2 i} \frac{2 z^{2}-i}{z+2}$.
(b) $\lim _{z \rightarrow i} \frac{z-i}{z^{2}+1}$.

Solution (a) Since $q(2 i)=2 i+2 \neq 0, f(z)$ is continuous at $z=2 i$, by Example 5(b). To find the limit as $z \rightarrow 2 i$, we simply evaluate $f(2 i)$ :

$$
\lim _{z \rightarrow 2 i} \frac{2 z^{2}-i}{z+2}=f(2 i)=\frac{2(2 i)^{2}-i}{2 i+2}=\frac{-8-i}{2+2 i}=\frac{1}{4}(-9+7 i) .
$$

(b) The denominator $q(z)=z^{2}+1$ vanishes at $z=i$ and so $f(z)=p(z) / q(z)$ is not continuous at $z=i$. Does the limit exist at $z=i$ ? We have

$$
f(z)=\frac{z-i}{z^{2}+1}=\frac{z-i}{(z-i)(z+i)}
$$

For $z \neq i$, we cancel the factor $z-i$ and get

$$
\lim _{z \rightarrow i} \frac{z-i}{z^{2}+1}=\lim _{z \rightarrow i} \frac{1}{z+i}=\frac{1}{2 i}=\frac{-i}{2} .
$$ $\square$

In Example 6(b), because $\lim _{z \rightarrow i} f(z)$ exists at the point of discontinuity $z=i$, we can remove the discontinuity of $f(z)$ and make it continuous at $z=i$ by redefining $f(i)=-i / 2$. Such a point of discontinuity is called a removable discontinuity. If the discontinuity at a point cannot be removed, then it is called a nonremovable discontinuity.

Our next example involves a function with infinitely many nonremovable discontinuities. In the example, we will use the uniqueness property of limits to show that a limit fails to exist. The method works as follows. If you can show that $f(z) \rightarrow L$ as $z$ approaches $z_{0}$ on curve $C$ (Figure 2), but $f(z) \rightarrow L^{\prime}$ as $z$ approaches $z_{0}$ on curve $C^{\prime}$, and $L \neq L^{\prime}$, then, by the uniqueness of limits, we conclude that $\lim _{z \rightarrow z_{0}} f(z)$ does not exist.

## EXAMPLE 7 The nonremovable discontinuities of $\operatorname{Arg} z$

The principal branch of the argument $\operatorname{Arg} z$ takes the value of argument $z$ that is in the interval $-\pi<\operatorname{Arg} z \leq \pi$. It is not defined at $z=0$ and hence $\operatorname{Arg} z$ is not continuous at $z=0$. We will show that $z=0$ is not a removable discontinuity by showing that $\lim _{z \rightarrow 0} \operatorname{Arg} z$ does not exist. Indeed, if $z=x>0$, then $\operatorname{Arg} z=0$ and so $\lim _{z=x \nmid 0} \operatorname{Arg} z=0$, where the down-arrow denotes the limit from the right, also denoted by $\lim _{z=x \rightarrow 0+} \operatorname{Arg} z$. However, if $z=x<0$, then $\operatorname{Arg} z=\pi$ and so $\lim _{z=x \uparrow 0} \operatorname{Arg} z=\pi$, where the up-arrow denotes the limit from the left, also denoted

![](./images/af4f9593-dec7-4bc0-8d78-d25500419ec9-16_476_537_281_116.jpg)
Figure $3 \operatorname{Arg} z$ has nonremovable discontinuities at $z=$ 0 and at all negative real $z$. For all other $z, \operatorname{Arg} z$ is continuous.

## PROPOSITION 1

by $\lim _{z=x \rightarrow 0^{-}} \operatorname{Arg} z$. By the uniqueness of limits, we conclude that $\lim _{z \rightarrow 0} \operatorname{Arg} z$ doe not exist.

Also, for a point on the negative $x$-axis, $z_{0}=x_{0}<0$, we have $\operatorname{Arg} z_{0}=\pi$. If $z$ approaches $z_{0}$ from the second quadrant, say along curve $C$ in Figure 3, we have $\lim _{z \rightarrow z_{0}} \operatorname{Arg} z=\pi=\operatorname{Arg} z_{0}$. But if $z$ approaches $z_{0}$ from the third quadrant, say along curve $C^{\prime}$ in Figure 3, we have $\lim _{z \rightarrow z_{0}} \operatorname{Arg} z=-\pi$. Hence $\operatorname{Arg} z$ is not continuous at $z_{0}$ and the discontinuity is not removable, because $\lim _{z \rightarrow z_{0}} \operatorname{Arg} z$ does not exist for such $z_{0}$.

It is not hard to show, using geometric considerations, that for $z \neq 0$ and $z$ not on the negative $x$-axis, $\operatorname{Arg} z$ is continuous. Since the set of points of continuity of $\operatorname{Arg} z$ is the complex plane $\mathbb{C}$ minus the interval $(-\infty, 0]$ on the real line, the principal branch of the argument is continuous on $\mathbb{C} \backslash(\infty, 0]$.

Many important functions of several variables are made up of products, quotients and linear combinations of functions of a single variable. For example, the function $u(x, y)=e^{x} \cos y$ is the product of two functions of a single variable each; namely, $e^{x}$ and $\cos y$. The exponential function $e^{z}=e^{x}(\cos y+i \sin y)$ is a linear combination of two products of functions of a single variable. In establishing the continuity of such functions, the following simple observations are very useful.

Suppose that $\phi(x)$ is a continuous function of a single variable $x$ over an interval $(a, b)$. Then the function of two variables $f(x, y)=\phi(x)$ is continuous at $\left(x_{0}, y_{0}\right)$ whenever $x_{0}$ is in $(a, b)$. Similarly, $g(x, y)=\phi(y)$ is continuous, at $\left(x_{0}, y_{0}\right)$ whenever $y_{0}$ is in $(a, b)$.
Proof If $(x, y) \rightarrow\left(x_{0}, y_{0}\right)$, then $x \rightarrow x_{0}$ and so $\phi(x) \rightarrow \phi\left(x_{0}\right)$ and, consequently, $f(x, y)=\phi(x) \rightarrow \phi\left(x_{0}\right)=f\left(x_{0}, y_{0}\right)$. Thus $f$ is continuous at $\left(x_{0}, y_{0}\right)$ as claimed. The second part of the proposition follows similarly.

Combined with Theorem 4, this proposition becomes a very powerful tool. Here are some interesting applications.

## EXAMPLE 8 Exponential and trigonometric functions

Show that the following are continuous functions of $z$.
(a) $e^{z}$.
(b) $\cos z$.

Solution (a) We know from calculus that the functions $e^{x}, \cos x$, and $\sin x$ are continuous for all $x$. By Proposition 1 , the functions $f_{1}(x, y)=e^{x}, f_{2}(x, y)=\cos y_{1}$ and $f_{3}(x, y)=\sin y$ are continuous for all $(x, y)$. Appealing to Theorem 4, we see that $e^{x} \cos y+i e^{x} \sin y=e^{z}$ is continuous for all $(x, y)$.
(b) The function $e^{i z}$ is continuous because it is the composition of two continuous functions; namely, $i z$ and $e^{z}$. Similarly, $e^{-i z}$ is continuous, and hence the linear combination $\frac{e^{i z}+e^{-i z}}{2}=\cos z$ is also continuous.

We give one more example of a continuous function.

## EXAMPLE 9 The absolute value $|z|$ is continuous

Let $f(z)=|z|$. By the triangle inequality, $0 \leq|z|=|x+i y| \leq|x|+|y|$. As $z \rightarrow 0$,

## THEOREM 5 CONTINUITY OF THE LOGARITHM

![](./images/af4f9593-dec7-4bc0-8d78-d25500419ec9-17_465_517_903_94.jpg)
Figure $4 \log z$ has nonremovable discontinuities at $z=$ 0 and at all negative real $z$. For all other $z, \log z$ is continuous.

![](./images/af4f9593-dec7-4bc0-8d78-d25500419ec9-17_461_507_1586_104.jpg)
Figure 5 The branch cut of $\log _{\alpha} z$ is the ray at angle $\alpha$. The branch cut is the set of nonremovable discontinuities of $\log _{\alpha} z$.

we have $x \rightarrow 0$ and $y \rightarrow 0$; consequently, $|x|,|y|$, and $|x|+|y|$ all tend to 0 , implying that $|z|=|x+i y|$ tends to 0 , by the squeeze theorem. This proves the continuity at 0 . We now show that $\lim _{z \rightarrow z_{0}}\left|f(z)-f\left(z_{0}\right)\right|=\lim _{z \rightarrow z_{0}}| | z\left|-\left|z_{0}\right|\right|=0$, for arbitrary $z_{0}$. By the lower estimate (19), Section 1.2, we have $\left||z|-\left|z_{0}\right|\right| \leq\left|z-z_{0}\right|$. As $z \rightarrow z_{0},\left(z-z_{0}\right) \rightarrow 0$, hence $\left|z-z_{0}\right| \rightarrow 0$, by the continuity of the absolute value at 0 , and so $\left||z|-\left|z_{0}\right|\right| \rightarrow 0$, by the squeeze theorem. $\square$

## Continuity of the Logarithms

Understanding the behavior of the logarithm is crucial to certain applications. We will prove the following important result, which should not surprise you in view of what we already know about $\operatorname{Arg} z$ and $|z|$.

## The principal branch of the logarithm

$$
\log (z)=\ln |z|+i \operatorname{Arg}(z), \quad-\pi<\operatorname{Arg} z \leq \pi \quad(z \neq 0),
$$

is continuous for all $z$ in $\mathbb{C} \backslash(-\infty, 0]$. For $z$ in $(-\infty, 0]$, the discontinuities of $\log z$ are not removable (Figure 4).

Proof We just showed in Example 9 that $|z|$ is a continuous function of $z$. Composing the continuous function $\ln x$, for $x>0$, with the real-valued function $|z|$, it follows from Theorem 4(iii) that $\ln |z|$ is continuous for all $z \neq 0$. We showed in Example 7 that $\operatorname{Arg} z$ is continuous except for nonremovable discontinuities at $z=0$ and $z$ on the negative $x$-axis. Appealing to Theorem 4(iv), we see that a discontinuity at $z=z_{0}$ of a function $f(z)=u(z)+i v(z)$ is removable if and only if $z_{0}$ is a removable discontinuity of both $u$ and $v$ (Exercise 43). Thus because of the nonremovable discontinuities of $\operatorname{Arg} z$, it follows that $z=0$ and $z$ on the negative $x$-axis are also nonremovable discontinuities of $\log z$. Thus the set of points of continuity of $\log z$ is $\mathbb{C} \backslash(-\infty, 0]$. $\square$

A discussion similar to the preceding one shows that a branch of the logarithm, $\log _{\alpha} z$, is continuous at all $z$ except for nonremovable discontinuities at $z=0$ and $z$ on the ray at angle $\alpha$. The set of nonremovable discontinuities of $\log _{\alpha} z$ is called a branch cut. Thus, for example, the branch cut of $\log z$ is $(-\infty, 0]$ (Figure 4), and the branch cut of $\log _{\alpha} z$ is the ray at angle $\alpha$ (Figure 5).

## Exercises 2.2

In Exercises 1-12, evaluate the given limit and justify each step by using properties of limits from this section. [Hint: In evaluating limits involving elementary functions such as exponential or trigonometric functions, you may want to express them in terms of their real and imaginary parts and use results from calculus.]

1. $\lim _{z \rightarrow i} 3 z^{2}+2 z-1$.
2. $\lim _{z \rightarrow 2+i} z+\frac{1}{z}$.
3. $\lim _{z \rightarrow 0} \frac{z}{\cos z}$.
4. $\lim _{z \rightarrow 2} \frac{z^{4}-16}{z-2}$.
5. $\lim _{z \rightarrow i} \frac{1}{z-i}-\frac{1}{z^{2}+1}$.
6. $\lim _{z \rightarrow 0} z \operatorname{Arg} z$.
7. $\lim _{z \rightarrow 0} z e^{i \operatorname{Re} z}$.
8. $\lim _{z \rightarrow i} \operatorname{Re}(z) \sin z$.
9. $\lim _{z \rightarrow-3}(\operatorname{Arg} z)^{2}$.
10. $\lim _{z \rightarrow 1}(z+1) \operatorname{Im}(i z)$.
11. $\lim _{z \rightarrow 0} \sin \bar{z}$.
12. $\lim _{z \rightarrow 0} z e^{i /|z|^{2}}$.

In Exercises 13-18, evaluate the given limit involving $\infty$. Justify your steps.
13. $\lim _{z \rightarrow \infty} \frac{z+1}{3 i z+2}$.
14. $\lim _{z \rightarrow \infty} \frac{z^{2}+i}{z^{3}+3 z^{2}+z+1}$.
15. $\lim _{z \rightarrow \infty}\left(\frac{z^{3}+i}{z^{3}-i}\right)^{2}$.
16. $\lim _{z \rightarrow i} \frac{1}{z^{2}+1}$.
17. $\lim _{z \rightarrow 1} \frac{-1}{(z-1)^{2}}$.
18. $\lim _{z \rightarrow \infty} \frac{\log z}{z}$.

In Exercises 19-26, show that the given limit at $z_{0}$ does not exist by approaching $z_{0}$ from different directions. If the limit involves $z \rightarrow \infty$, try some of the following directions: the positive $x$-axis, the negative $x$-axis, the positive $y$-axis ( $z=i y, y>$ 0 ), or the negative $y$-axis ( $z=i y, y<0$ ).
19. $\lim _{z \rightarrow-3} \operatorname{Arg} z$.
20. $\lim _{z \rightarrow-1} \log z$.
21. $\lim _{z \rightarrow \infty} e^{-z}$.
22. $\lim _{z \rightarrow 0} \frac{\bar{z}}{z}$.
23. $\lim _{z \rightarrow 0} e^{1 / z}$.
24. $\lim _{z \rightarrow 0} \frac{\operatorname{Re} z}{|z|^{2}}$.
25. $\lim _{z \rightarrow 0} \frac{z}{|z|}$.
26. $\lim _{z \rightarrow 0} \frac{\operatorname{Im} z}{z}$.
27. Show that if the limit of a function exists then it is unique. [Hint: For the case of a finite limit, suppose $L_{1}$ and $L_{2}$ are two limits. Then $\left|L_{1}-L_{2}\right| \leq \left|L_{1}-f(z)\right|+\left|L_{2}-f(z)\right|$ (why?). As $z \rightarrow z_{0}$, what happens to the right side?]
28. Use the triangle inequality and (2) to prove (3).
29. Prove (14).
30. Prove (15).
31. Show that $\lim _{z \rightarrow z_{0}} f(z)=0 \Leftrightarrow \lim _{z \rightarrow z_{0}} \frac{1}{f(z)}=\infty$.
32. Use the result of Exercise 31 to evaluate $\lim _{z \rightarrow 0} \frac{\cos z}{z}$.

In Exercises 33-40, determine the set of points where the given function is continuous. For a point of discontinuity, determine whether it is removable or not. Whenever possible, use properties from this section; in particular, use Proposition 1 and Theorem 4.
33. $\frac{z-i}{z+1+3 i}$.
34. $\frac{2 z+1}{z^{2}+3 z+2}$.
35. $\bar{z}$.
36. $\log (z+1)$.
37. $\sin z$.
38. $(\operatorname{Arg} z)^{2}$.
39. $z(\operatorname{Arg} z)^{2}$.
40. $\frac{z}{|z|}$.
41. Pre-image of sets. Let $f$ be a complex-valued function defined on a subset $S$ of $\mathbb{C}$. If $A$ is a set of complex numbers, the pre-image or inverse image of $A$ by $f$ is the set $f^{-1}[A]=\{z \in S: f(z)$ belongs to $A\}$. The following statements are true for arbitrary sets $S$. To simplify the proofs, take $S=\mathbb{C}$.
(a) Show that $f$ is continuous if and only if $f^{-1}[A]$ is open whenever $A$ is open.
(b) Show that $f$ is continuous if and only if $f^{-1}[A]$ is closed whenever $A$ is closed. (If $S$ is a proper subset of $\mathbb{C}$, (a) and (b) still hold, but we have to define what we mean for a set such as $f^{-1}[A]$ to be open or closed in $S$. These topics are part of elementary topology and will not be emphasized in this book.)
42. Continuity and boundedness. Show that if $f$ is continuous at $z_{0}$, then
43. Show that a discontinuity at $z=z_{0}$ of a function $f(z)=u(z)+i v(z)$ is it is bounded in a neighborhood of $z_{0}$. removable if and only if $z_{0}$ is a removable discontinuity of both $u$ and $v$.

### 2.3 Analytic Functions

For a real-valued function $f(x)$ defined on an open interval containing the point $x_{0}$, we defined the derivative at $x_{0}$ to be $f^{\prime}\left(x_{0}\right)=\lim _{x \rightarrow x_{0}} \frac{f(x)-f\left(x_{0}\right)}{x-x_{0}}$, when the limit exists. Our definition for the derivative of a complex function $f(z)$ is a natural extension of the real case.

## DEFINITION 1 COMPLEX DERIVATIVE

DEFINITION 2 ANALYTIC FUNCTIONS

Let $f(z)$ be defined on a neighborhood of $z_{0}$. If

$$
\lim _{z \rightarrow z_{0}} \frac{f(z)-f\left(z_{0}\right)}{z-z_{0}}
$$

exists, then $f$ is said to be differentiable at the point $z_{0}$, and the number

$$
f^{\prime}\left(z_{0}\right)=\lim _{z \rightarrow z_{0}} \frac{f(z)-f\left(z_{0}\right)}{z-z_{0}}
$$

is called the derivative of $f$ at $z_{0}$.
We can also use the Leibniz notation for the derivative, $\frac{d f}{d z}\left(z_{0}\right)$, or $\left.\frac{d f}{d z}\right|_{z=z_{0}}$. We can recast the difference quotient and define the derivative as

$$
f^{\prime}\left(z_{0}\right)=\lim _{\Delta z \rightarrow 0} \frac{f\left(z_{0}+\Delta z\right)-f\left(z_{0}\right)}{\Delta z}
$$

While this extension looks similar to the definition of a derivative for functions defined on the real line, we are asking a lot more in the complex case. In the real case, $x$ can only approach $x_{0}$ from either the right or the left. In the complex case, $z$ can approach $z_{0}$ from any number of directions. For the derivative to exist, we are requiring that the limit exists no matter how we approach $z_{0}$ in (1).

We now introduce a fundamental definition in the theory of complex variables.

A function $f(z)$ defined on an open set $S$ is said to be analytic on $S$ if $f^{\prime}(z)$ exists and is continuous for all $z$ in $S$. We say $f(z)$ is analytic at a point if $f(z)$ is analytic on some open set containing that point. We say $f(z)$ is entire if $f(z)$ is analytic on $\mathbb{C}$.

It is important to note that while differentiability is defined at a specific point, analyticity is defined on an open set. Even when we say "analytic at a point," we really mean analytic on some open set containing this point.

In Section 3.9, we will prove a theoretical result, called Goursat's theorem. It asserts that the mere existence of $f^{\prime}(z)$ in an open set implies that $f^{\prime}(z)$ is continuous. Thus our requirement that $f^{\prime}(z)$ be continuous in the definition of analytic functions is redundant; we have included it to make some initial proofs easier to understand.

EXAMPLE 1 Some simple entire functions
Show the following functions are entire (analytic at every point in the complex plane), and find their derivatives.
(a) $f(z)=2+4 i$.
(b) $f(z)=(3-i) z$.
(c) $f(z)=z^{2}$.

Solution We use the difference quotient as in (1) to calculate the derivatives.
(a) Fix any $z_{0}$ in the plane. Since $f=2+4 i$ is constant, $f(z)=f\left(z_{0}\right)$ for any $z$. Hence $\frac{f(z)-f\left(z_{0}\right)}{z-z_{0}}=0$. Taking the limit as $z \rightarrow z_{0}$, we get $f^{\prime}\left(z_{0}\right)=0$. Thus $f^{\prime}(z)=0$ for all $z$. Since $f^{\prime}(z)$ is obviously continuous, it follows that $f(z)=2+4 i$ is analytic on $\mathbb{C}$, or entire.
(b) Fix any $z_{0}$ in the plane. We have

$$
f^{\prime}\left(z_{0}\right)=\lim _{z \rightarrow z_{0}} \frac{f(z)-f\left(z_{0}\right)}{z-z_{0}}=\lim _{z \rightarrow z_{0}} \frac{(3-i)(z)-(3-i)\left(z_{0}\right)}{z-z_{0}}=3-i
$$

Thus $f^{\prime}(z)=3-i$ for all $z$. Since $f^{\prime}(z)$ is continuous, it follows that $f(z)=(3-i) z$ is entire.
(c) Fix any $z_{0}$ in the plane. We have

$$
f^{\prime}\left(z_{0}\right)=\lim _{z \rightarrow z_{0}} \frac{z^{2}-z_{0}^{2}}{z-z_{0}}=\lim _{z \rightarrow z_{0}} \frac{\left(z-z_{0}\right)\left(z+z_{0}\right)}{z-z_{0}}=\lim _{z \rightarrow z_{0}} z+z_{0}=2 z_{0}
$$

Thus $f^{\prime}(z)=2 z$ for all $z$. Since $f^{\prime}(z)$ is continuous, it follows that $f(z)=z^{2}$ is entire.

The following useful formulas can be derived by the methods of Example 1(a) and (b):

$$
\begin{aligned}
f(z)=c(\text { a constant }) & \Rightarrow f^{\prime}(z)=0 \\
f(z)=z & \Rightarrow f^{\prime}(z)=1
\end{aligned}
$$

Our first theorem is the analog of the well-known fact from calculus that states that if a function has a derivative then it is continuous. The proof is also similar to the real variable case.

THEOREM 1 DIFFERENTIABLE IMPLIES CONTINUOUS

Suppose $f(z)$ is differentiable at $z_{0}$. Then $f(z)$ is continuous at $z_{0}$.
Proof We must show that $\lim _{z \rightarrow z_{0}} f(z)=f\left(z_{0}\right)$. Equivalently, we will show that $\lim _{z \rightarrow z_{0}}\left(f(z)-f\left(z_{0}\right)\right)=0$. Using the fact that the limit of a product is the product of the limits ((4), Section 2.2), we have

$$
\begin{aligned}
\lim _{z \rightarrow z_{0}} f(z)-f\left(z_{0}\right) & =\lim _{z \rightarrow z_{0}} \frac{f(z)-f\left(z_{0}\right)}{z-z_{0}}\left(z-z_{0}\right) \\
& =\lim _{z \rightarrow z_{0}} \frac{f(z)-f\left(z_{0}\right)}{z-z_{0}} \lim _{z \rightarrow z_{0}}\left(z-z_{0}\right)=f^{\prime}\left(z_{0}\right) \cdot 0=0
\end{aligned}
$$

Equivalently, Theorem 1 states that if a function is not continuous, it cannot be differentiable. The converse of Theorem 1, however, is not trueFor example, $\bar{z}$ is continuous but nowhere differentiable (see Example 4 in this section).

Because the definition of the derivative in the complex case is modeled after the definition of the derivative in the real case, it should not surprise you that many of the properties of derivatives that you are familiar with from calculus hold for analytic functions.

## THEOREM 2 PROPERTIES OF ANALYTIC FUNCTIONS

Suppose that $f$ and $g$ are analytic on an open set $S$ and $c_{1}, c_{2}$ are complex constants. Then $c_{1} f+c_{2} g$ and $f g$ are analytic on $S$ with

$$
\begin{aligned}
\left(c_{1} f+c_{2} g\right)^{\prime}(z) & =c_{1} f^{\prime}(z)+c_{2} g^{\prime}(z) \text { and } \\
(f g)^{\prime}(z) & =f^{\prime}(z) g(z)+f(z) g^{\prime}(z) .
\end{aligned}
$$

Also, $\frac{f}{g}$ is analytic on $S$ minus the points where $g=0$, and

$$
\left(\frac{f}{g}\right)^{\prime}(z)=\frac{f^{\prime}(z) g(z)-f(z) g^{\prime}(z)}{(g(z))^{2}} \quad(g(z) \neq 0) .
$$

If $g$ is analytic at $z_{0}$ and $f$ is analytic at $g\left(z_{0}\right)$, then the composition $(f \circ g)(z)$ is analytic at $z_{0}$ and we have the chain rule

$$
(f \circ g)^{\prime}\left(z_{0}\right)=f^{\prime}\left(g\left(z_{0}\right)\right) g^{\prime}\left(z_{0}\right) .
$$

Proof The proof of each part involves two steps. First we must establish the existence of a derivative, then show that it is continuous. Because the right side of each formula in the theorem is constructed using continuous functions according to rules that preserve continuity, the continuity of the derivatives follows immediately once we establish the formulas (5)-(8).

We will prove the product rule (6) to illustrate to you that the methods from calculus apply here. The proofs of (5) and (7) are relegated to the exercises. The chain rule (8) is more delicate-we will prove it in the appendix to this section, where we use a new formalism to express differentiability.

Appealing to the definition of the derivative and using the continuity of $g$ (Theorem 1), we have

$$
\begin{aligned}
(f g)^{\prime}\left(z_{0}\right) & =\lim _{z \rightarrow z_{0}} \frac{f(z) g(z)-f\left(z_{0}\right) g\left(z_{0}\right)}{z-z_{0}} \\
& =\lim _{z \rightarrow z_{0}} \frac{f(z) g(z)-f\left(z_{0}\right) g(z)+f\left(z_{0}\right) g(z)-f\left(z_{0}\right) g\left(z_{0}\right)}{z-z_{0}} \\
& =\lim _{z \rightarrow z_{0}} g(z) \frac{f(z)-f\left(z_{0}\right)}{z-z_{0}}+\lim _{z \rightarrow z_{0}} f\left(z_{0}\right) \frac{g(z)-g\left(z_{0}\right)}{z-z_{0}} \\
& =g\left(z_{0}\right) f^{\prime}\left(z_{0}\right)+f\left(z_{0}\right) g^{\prime}\left(z_{0}\right)
\end{aligned}
$$ $\square$

## EXAMPLE 2 Analyticity of $z^{n}$ for $n=1,2, \ldots$

Use (1) to show that for $n=1,2, \ldots$

$$
\frac{d}{d z} z^{n}=n z^{n-1} .
$$

Conclude that $f(z)=z^{n}$ is entire.
Solution We give a proof by induction. The case $n=1$ was already stated in (4). Suppose as an induction hypothesis that (9) holds for $n$; we will prove that it holds for $n+1$. Given $h(z)=z^{n+1}$, write it as a product, $h(z)=z^{n} z$. Applying the product rule for differentiation (6) and the induction hypothesis, we get

$$
h^{\prime}(z)=\left(z^{n}\right)^{\prime} z+z^{n} z^{\prime}=n z^{n-1} z+z^{n}=(n+1) z^{n}
$$

as desired. Hence (9) holds for all $n$. Looking at the right side of (9), it is clear that the derivative of $f(z)=z^{n}$ is continuous for all $z$. Hence $z^{n}$ is entire.

## EXAMPLE 3 Analyticity of a rational function

Find the derivative of

$$
f(z)=\frac{(z+1)(z+i)^{2}}{z+1-3 i}
$$

and determine where $f(z)$ is analytic.
Solution The formal manipulations are exactly as if we were working with a real function and treating the complex numbers as real constants. We use the quotient and product rules for differentiation, (7) and (6), and get

$$
\begin{aligned}
f^{\prime}(z) & =\frac{\left((z+i)^{2}+(z+1) 2(z+i)\right)(z+1-3 i)-(z+1)(z+i)^{2}}{(z+1-3 i)^{2}} \\
& =\frac{2 z^{3}+(4-7 i) z^{2}+(14-2 i) z+(6+5 i)}{(z+1-3 i)^{2}}
\end{aligned}
$$

The function is analytic at all $z$ except at $z=-1+3 i$, where the denominator vanishes.

By using linear combinations of powers of $z$ and appealing to the result of Example 2 and the linearity of the derivative (5), we conclude that a polynomial is an entire function. By appealing now to the quotient rule, as we did in Example 3, we see that a rational function is analytic at all $z$ where $g(z) \neq 0$.

THEOREM 3 POLYNOMIALS AND RATIONAL FUNCTIONS

Let $n$ be a nonnegative integer. A polynomial of degree $n, p(z)=a_{n} z^{n}+ a_{n-1} z^{n-1}+\cdots+a_{1} z+a_{0}$, is entire. Its derivative is given by

$$
p^{\prime}(z)=n a_{n} z^{n-1}+(n-1) a_{n-1} z^{n-1}+\cdots+a_{1} z .
$$

A rational function $f(z)=p(z) / q(z)$, where $p(z)$ and $q(z)$ are polynomials, is analytic at all points $z$ where $q(z) \neq 0$. Its derivative is given by

$$
f^{\prime}(z)=\frac{p^{\prime}(z) q(z)-p(z) q^{\prime}(z)}{q(z)^{2}}
$$

Typically, any function that algebraically manipulates $z$ will be differentiable; however, not every complex-valued function is analytic. Functions like $\operatorname{Re} z, \operatorname{Im} z, \bar{z}$, and $|z|$ will have at best limited differentiability.

![](af4f9593-dec7-4bc0-8d78-d25500419ec9-23_463_509_480_116.jpg)
Figure 1 On $C, \Delta z=\Delta x$. On $C^{\prime}, \Delta z=i \Delta y$.

## EXAMPLE 4 Functions that are nowhere analytic

Show that the functions
(a) $f(z)=\bar{z}$ and
(b) $f(z)=\operatorname{Re} z$
are not analytic at any point.
Solution In order to show that a function $f(z)$ is not analytic at a point $z_{0}$, we will show that the limit (1) that defines the derivative does not exist. For this purpose, we will approach $z_{0}$ from two different directions and show that the limits that we obtain are not equal. Since the value of a limit must be unique, we will then conclude that the limit and hence the derivative do not exist.
(a) Fix a point $z_{0}=x_{0}+i y_{0}$ in the plane. Our goal is to show that the limit

$$
\lim _{z \rightarrow z_{0}} \frac{f(z)-f\left(z_{0}\right)}{z-z_{0}}
$$

does not exist. We will approach $z_{0}$ from the two directions as indicated in Figure 1. For $z$ on $C$, we have

$$
z=z_{0}+\Delta x ; \quad z-z_{0}=\Delta x ; \quad f(z)-f\left(z_{0}\right)=\bar{z}-\overline{z_{0}}=\overline{z-z_{0}}=\overline{\Delta x}=\Delta x,
$$

because $\Delta x$ is real. Thus,

$$
\lim _{\substack{z \rightarrow z_{0} \\ z \text { on } C}} \frac{f(z)-f\left(z_{0}\right)}{z-z_{0}}=\lim _{\substack{z \rightarrow z_{0} \\ z \text { on } C}} \frac{\Delta x}{\Delta x}=\lim _{\substack{z \rightarrow z_{0} \\ z \text { on } C}} 1=1 .
$$

For $z$ on $C^{\prime}$, we have

$$
z=z_{0}+i \Delta y ; \quad z-z_{0}=i \Delta y ; \quad \bar{z}-\overline{z_{0}}=\overline{z-z_{0}}=\overline{i \Delta y}=-i \Delta y,
$$

because $i \Delta y$ is purely imaginary. Thus,

$$
\lim _{\substack{z \rightarrow z_{0} \\ z \text { on } C^{\prime}}} \frac{f(z)-f\left(z_{0}\right)}{z-z_{0}}=\lim _{\substack{z \rightarrow z_{0} \\ z \text { on } C^{\prime}}} \frac{-i \Delta y}{i \Delta y}=\lim _{\substack{z \rightarrow z_{0} \\ z \text { on } C^{\prime}}}-1=-1 .
$$

Since the limit along $C$ is not equal to the limit along $C^{\prime}$, we conclude that the limit in (12) does not exist. Hence the function $f(z)=\bar{z}$ is nowhere analytic.
(b) We take the same approach as in (a) and use the same directions along $C$ and $C^{\prime}$. It is easy to check that for $z$ on $C f(z)-f\left(z_{0}\right)=\operatorname{Re} z-\operatorname{Re} z_{0}= x_{0}+\Delta x-x_{0}=\Delta x$, while for $z$ on $C^{\prime} f(z)-f\left(z_{0}\right)=\operatorname{Re} z-\operatorname{Re} z_{0}=x_{0}-x_{0}=0$. Using this information, we obtain

$$
\lim _{\substack{z \rightarrow z_{0} \\ z \text { on } C}} \frac{f(z)-f\left(z_{0}\right)}{z-z_{0}}=\lim _{\substack{z \rightarrow z_{0} \\ z \text { on } C}} \frac{\Delta x}{\Delta x}=1
$$

and

$$
\lim _{\substack{z \rightarrow z_{0} \\ z \text { on } C^{\prime}}} \frac{f(z)-f\left(z_{0}\right)}{z-z_{0}}=\lim _{\substack{z \rightarrow z_{0} \\ z \text { on } C^{\prime}}} \frac{0}{i \Delta y}=0 .
$$

This shows that the limit defining the derivative of $\operatorname{Re} z$ does not exist at any point; and hence $\operatorname{Re} z$ is nowhere analytic.

There is another quick proof of (b) based on the result of (a) and the identity $\bar{z}=2 \operatorname{Re} z-z$. In fact, if $\operatorname{Re} z$ has a derivative at $z_{0}$, then by the properties of the derivative it would follow that $\bar{z}$ has a derivative at $z_{0}$, which contradicts (a).

Other interesting examples of functions that fail to be analytic at certain points in the plane are presented in the exercises.

So far we have been successful at differentiating polynomials and rational functions. To go beyond these examples we need more tools. In Section 2.4 we will present the Cauchy-Riemann equations, which are the most important tools for checking analyticity. The following result, which is an inside-out chain rule of sorts, is useful when dealing with inverse functions such as logarithms and powers.

## THEOREM 4 ANALYTICITY OF COMPOSED FUNCTIONS

Figure 2 Unlike the chain rule, where we suppose that $f$ and $g$ are analytic and conclude that $h=g \circ f$ is analytic, in Theorem 4, we suppose that $g$ is continuous, and $f$ and the composed function $h$ are analytic, and then we conclude that $g$ is analytic.
![](af4f9593-dec7-4bc0-8d78-d25500419ec9-24_506_536_1985_96.jpg)

Figure 3 Branch cut of $\log z$.

Suppose that $h(z)=f(g(z))$ is analytic on a region $\Omega$, and $f$ is analytic at $g(z)$ with $f^{\prime}(g(z)) \neq 0$ for all $z$ in $\Omega$. Suppose further that $g(z)$ is continuous on $\Omega$ (Figure 2). Then $g$ is analytic on $\Omega$ and

$$
g^{\prime}(z)=\frac{h^{\prime}(z)}{f^{\prime}(g(z))}
$$

As in the case of the chain rule, the proof of this theorem will be greatly simplified by using the formalisms presented in the appendix. We postpone the proof and give instead an application.

Figure 2 Unlike the chain rule, where we suppose that $f$ and $g$ are analytic and conclude that $h=g \circ f$ is analytic, in Theorem 4, we suppose that $g$ is continuous, and $f$ and the composed function $h$ are analytic, and then we conclude that $g$ is analytic.
![](af4f9593-dec7-4bc0-8d78-d25500419ec9-24_544_1431_1357_676.jpg)

## EXAMPLE 5 Analyticity of $n$th roots

Show that the principal branch of the $n$th root, $g(z)=z^{1 / n}(n=0,1,2, \ldots)$, is analytic in the region $\Omega$ that consists of all $z \neq 0$ and not on the negative real axis. Also show that for $z$ in $\Omega$, we have

$$
g^{\prime}(z)=\frac{1}{n} z^{(1-n) / n}
$$

Solution From (10), Section 1.7, we have

$$
g(z)=e^{\frac{1}{n} \log z}
$$

where $\log z$ is the principal branch of the logarithm. We showed in the previous section that $e^{z}$ is continuous for all $z$, and since $\log z$ is continuous in $\Omega$ (see

THEOREM 5 DIFFERENTIABILITY

Figure 3), it follows that $g(z)$ is continuous in $\Omega$, being the composition of two continuous functions. Taking $f(z)=z^{n}, h(z)=f(g(z))=\left(z^{1 / n}\right)^{n}=z$, we see clearly that $f$ and $h$ are analytic, and thus the hypotheses of Theorem 4 are satisfied. Consequently, $g(z)$ is analytic on $\Omega$ and

$$
g^{\prime}(z)=\frac{h^{\prime}(z)}{f^{\prime}(g(z))}=\frac{1}{n\left(z^{1 / n}\right)^{n-1}}=\frac{1}{n} z^{(1-n) / n}
$$

## Appendix: Proofs Related to Differentiation

Suppose that $f(z)$ has a derivative at $z_{0}$ and let

$$
\epsilon(z)=\frac{f(z)-f\left(z_{0}\right)}{z-z_{0}}-f^{\prime}\left(z_{0}\right)
$$

Then $\epsilon(z) \rightarrow 0$ as $z \rightarrow z_{0}$, because the difference quotient in (14) tends to $f^{\prime}\left(z_{0}\right)$. Solving for $f(z)$ in (14) we obtain

$$
f(z)=\overbrace{f\left(z_{0}\right)+f^{\prime}\left(z_{0}\right)\left(z-z_{0}\right)}^{\text {linear function of } z}+\epsilon(z)\left(z-z_{0}\right) .
$$

This expression shows that, near a point where $f$ is differentiable, $f(z)$ is approximately a linear function. The converse is also true. We summarize these results as follows.

A function $f(z)$ is differentiable at $z_{0}$ if and only if it can be written in the form

$$
f(z)=f\left(z_{0}\right)+A\left(z-z_{0}\right)+\epsilon(z)\left(z-z_{0}\right)
$$

where $A=f^{\prime}\left(z_{0}\right)$ and $\epsilon(z) \rightarrow 0$ as $z \rightarrow z_{0}$.
Proof We have already established the theorem in one direction. For the other direction, suppose that $f(z)$ can be written as in (16). Then, for $z \neq z_{0}$,

$$
\frac{f(z)-f\left(z_{0}\right)}{z-z_{0}}=A+\epsilon(z) .
$$

Taking the limit as $z \rightarrow z_{0}$ and using the fact that $\epsilon(z) \rightarrow 0$, we conclude that $f^{\prime}\left(z_{0}\right)$ exists and equals $A$.
The formalism of Theorem 5 simplifies greatly proofs related to differentiation.
Proof of the chain rule Suppose $g$ is analytic at $z_{0}$ and $f$ is analytic at $g\left(z_{0}\right)$. We want to show that

$$
(f \circ g)^{\prime}\left(z_{0}\right)=f^{\prime}\left(g\left(z_{0}\right)\right) g^{\prime}\left(z_{0}\right)
$$

Since $g$ is differentiable at $z_{0}$, appealing to Theorem 5 , we can write

$$
\frac{g(z)-g\left(z_{0}\right)}{z-z_{0}}=g^{\prime}\left(z_{0}\right)+\epsilon(z), \quad \epsilon(z) \rightarrow 0 \text { as } z \rightarrow z_{0}
$$

Also, $f$ is differentiable at $g\left(z_{0}\right)$, so by Theorem 5 we can write

$$
f(w)-f\left(g\left(z_{0}\right)\right)=f^{\prime}\left(g\left(z_{0}\right)\right)\left(w-g\left(z_{0}\right)\right)+\eta(w)\left(w-g\left(z_{0}\right)\right), \quad \eta(w) \rightarrow 0 \text { as } w \rightarrow g\left(z_{0}\right) .
$$

Replacing $w$ by $g(z)$, dividing by $z-z_{0}$, and using (19), we obtain
(20) $\frac{f(g(z))-f\left(g\left(z_{0}\right)\right)}{z-z_{0}}=f^{\prime}\left(g\left(z_{0}\right)\right)\left(g^{\prime}\left(z_{0}\right)+\epsilon(z)\right)+\eta(g(z))\left(g^{\prime}\left(z_{0}\right)+\epsilon(z)\right)$.

As $z \rightarrow z_{0}, \epsilon(z) \rightarrow 0, g(z) \rightarrow g\left(z_{0}\right)$ by continuity, and so $\eta(g(z)) \rightarrow 0$. Using this in (20), we conclude that

$$
\lim _{z \rightarrow z_{0}} \frac{f(g(z))-f\left(g\left(z_{0}\right)\right)}{z-z_{0}}=f^{\prime}\left(g\left(z_{0}\right)\right) g^{\prime}\left(z_{0}\right),
$$

as asserted by the chain rule.
Proof of Theorem 4 Let $z_{0}$ be in $\Omega$. Given $h(z)=f(g(z))$ analytic at $z_{0}, f$ analytic at $g\left(z_{0}\right)$ with $f^{\prime}\left(g\left(z_{0}\right)\right) \neq 0$, and $g$ continuous at $z_{0}$, once we show that

$$
g^{\prime}\left(z_{0}\right)=\frac{h^{\prime}\left(z_{0}\right)}{f^{\prime}\left(g\left(z_{0}\right)\right)}
$$

then since $h^{\prime}, f^{\prime}$ and $g$ are continuous and $f^{\prime}\left(g\left(z_{0}\right)\right) \neq 0$, it will follow that $g^{\prime}$ is continuous at $z_{0}$ and hence $g$ is analytic at $z_{0}$. Applying Theorem 5 to $h(z)= f(g(z))$, we have

$$
f(g(z))=f\left(g\left(z_{0}\right)\right)+h^{\prime}\left(z_{0}\right)\left(z-z_{0}\right)+\epsilon(z)\left(z-z_{0}\right), \quad \epsilon(z) \rightarrow 0 \text { as } z \rightarrow z_{0}
$$

Applying Theorem 5 to $f$ at $g\left(z_{0}\right)$, we have

$$
f(g(z))=f\left(g\left(z_{0}\right)\right)+f^{\prime}\left(g\left(z_{0}\right)\right)\left(g(z)-g\left(z_{0}\right)\right)+\eta(g(z))\left(g(z)-g\left(z_{0}\right)\right)
$$

where $\eta(g(z)) \rightarrow 0$ as $g(z) \rightarrow g\left(z_{0}\right)$ or, equivalently, as $z \rightarrow z_{0}$ by continuity of $g$ at $z_{0}$. Subtract (23) from (22) and rearrange the terms to get

$$
\frac{g(z)-g\left(z_{0}\right)}{z-z_{0}}=\frac{h^{\prime}\left(z_{0}\right)+\epsilon(z)}{f^{\prime}\left(g\left(z_{0}\right)\right)+\eta(g(z))}
$$

As $z \rightarrow z_{0}, \epsilon(z) \rightarrow 0$ and $\eta(g(z)) \rightarrow 0$, implying (21).

## Exercises 2.3

In Exercises 1-12, determine the set on which the given function is analytic and compute its derivative. In Exercises 9-12, use the principal branch of the power.

1. $3(z-1)^{2}+2(z-1)$.
2. $z^{3}+\frac{z}{1+i}$.
3. $\operatorname{Im} z$.
4. $\left(\frac{z-2+i}{z-1+i}\right)^{2}$.
5. $\frac{1}{z^{3}+1}$.
6. $8 \bar{z}+i$.
7. $\frac{1}{z^{2}-(1-2 i) z-3-i}$.
8. $\frac{1}{z^{2}+(1+2 i) z+3-i}$.
9. $z^{2 / 3}$.
10. $(z-1)^{\frac{1}{2}}$.
11. $(z-3+i)^{1 / 10}$.
12. $\frac{1}{(z+1)^{1 / 2}}$.

In Exercises 13-16, evaluate the given limit by identifying it with a derivative at a point. In Exercises 15-16, use the principal branch of the power.
13. $\lim _{z \rightarrow 1} \frac{z^{100}-1}{z-1}$.
14. $\lim _{z \rightarrow i} \frac{z^{99}+i}{z-i}$.
15. $\lim _{z \rightarrow 0} \frac{1}{z \sqrt{1+z}}-\frac{1}{z}$.
16. $\lim _{z \rightarrow 1} \frac{z^{1 / 3}-1}{z-1}$.
17. Determine the set on which

$$
f(z)= \begin{cases}z & \text { if }|z| \leq 1 \\ z^{2} & \text { if }|z|>1\end{cases}
$$

is analytic and compute its derivative. Justify your answer.
18. (a) Show that the derivative of $f(z)=|z|^{2}$ exists at $z=0$ and does not exist at all other points. [Hint: Proceed as in Example 4.]
(b) At which points is $f$ analytic?
19. Show that $f(z)=|z|$ is nowhere differentiable. [Hint: Compute the limit in
(1) by letting $z=\alpha z_{0}$ with $\alpha>0$; then $\alpha<0$.]
20. For this exercise, refer to (10), Section 1.7.
(a) Show that the three branches of $z^{1 / 3}$ are

$$
b_{1}(z)=e^{\frac{1}{3} \log z} ; \quad b_{2}(z)=e^{\frac{1}{3} \log z} e^{\frac{2 \pi i}{3}} ; \quad b_{3}(z)=e^{\frac{1}{3} \log z} e^{\frac{4 \pi i}{3}} .
$$

(b) Use Theorem 4 to show that

$$
b_{j}^{\prime}(z)=\frac{b_{j}(z)}{3 z} \quad(j=1,2,3) .
$$

21. Refer to (10), Section 1.7. Use Theorem 4 to show that for any integer $p$ and positive integer $q$,

$$
\frac{d}{d z} z^{p / q}=\frac{p}{q z} z^{p / q},
$$

where we are using the same branch of the power on both sides. [Hint: In applying Theorem 4, take $g(z)=z^{p / q}$ and $f(z)=z^{q}$.]
22. Linearity of the derivative. Prove (5) using the definition (1) and appealing to the linearity of limits, (3), Section 2.2.
23. Quotient rule. (a) Prove the following special case of the quotient rule (7):

$$
\left(\frac{1}{f}\right)^{\prime}\left(z_{0}\right)=-\frac{f^{\prime}\left(z_{0}\right)}{\left(f\left(z_{0}\right)\right)^{2}} \quad\left(f\left(z_{0}\right) \neq 0\right) .
$$

[Hint: Start by writing the difference quotient for $\frac{1}{f(z)}$ as

$$
\left.\frac{\frac{1}{f(z)}-\frac{1}{f\left(z_{0}\right)}}{z-z_{0}}=-\frac{1}{f(z) f\left(z_{0}\right)} \frac{f(z)-f\left(z_{0}\right)}{z-z_{0}}\right]
$$

(b) Prove the quotient rule (7) by using the product rule (6) and (25).
24. Product rule. We proved the product rule (6) in the text by mimicking the usual proof from calculus. Provide a shorter proof by using Theorem 5.
25. Derivative of $z^{n}$. In the text we showed that for positive integers $n, \frac{d}{d z} z^{n}= n z^{n-1}$. Construct a different proof starting with the definition (1) and using the identity

$$
z^{n}-z_{0}^{n}=\left(z-z_{0}\right)\left(z^{n-1}+z^{n-2} z_{0}+\cdots+z_{0}^{n-1}\right) .
$$

26. Derivative of $z^{n}, n$ negative. Show that the formula in Example 2 holds for negative $n$ where $z \neq 0$. Conclude that $z^{n}$ is analytic for all $z \neq 0$, when $n$ is a negative integer.
27. L'Hospital's rule. Prove the following version of L'Hospital's rule. If $f(z)$ and $g(z)$ are differentiable at $z_{0}$ and $f\left(z_{0}\right)=g\left(z_{0}\right)=0$, but $g^{\prime}\left(z_{0}\right) \neq 0$, then

$$
\lim _{z \rightarrow z_{0}} \frac{f(z)}{g(z)}=\frac{f^{\prime}\left(z_{0}\right)}{g^{\prime}\left(z_{0}\right)}
$$

[Hint: $\frac{f(z)}{g(z)}=\frac{f(z)-f\left(z_{0}\right)}{z-z_{0}} \frac{1}{\frac{g(z)-g\left(z_{0}\right)}{z-z_{0}}}$. Another way to proceed is to use Theorem 5.]
28. Find the following limits by using L'Hospital's rule.
(a) $\lim _{z \rightarrow i} \frac{\left(z^{2}+1\right)^{7}}{z^{6}+1}$.
(b) $\lim _{z \rightarrow i} \frac{z^{3}+(1-3 i) z^{2}+(i-3) z+2+i}{z-i}$.

### 2.4 The Cauchy-Riemann Equations

The fact that the derivative of $\bar{z}$ does not exist (Example 4, Section 2.3) should tell you that there is something special about complex-valued functions with derivatives. As you will see, the existence of the derivative implies special relationships between the real and imaginary parts of the functions. These relationships are known as the Cauchy-Riemann equations, which we now derive.

Suppose that $f(z)=f(x+i y)=u(x, y)+i v(x, y)$ is analytic in an open set $S$ and let $z_{0}=x_{0}+i y_{0}=\left(x_{0}, y_{0}\right)$ be a point in $S$. Consequently, the derivative at $z_{0}$ exists and is given by

$$
f^{\prime}\left(z_{0}\right)=\lim _{z \rightarrow z_{0}} \frac{f(z)-f\left(z_{0}\right)}{z-z_{0}}=\lim _{\Delta z \rightarrow 0} \frac{f\left(z_{0}+\Delta z\right)-f\left(z_{0}\right)}{\Delta z}
$$

To derive the Cauchy-Riemann equations, we will simply compute this limit

![](af4f9593-dec7-4bc0-8d78-d25500419ec9-28_512_557_1699_86.jpg)
Figure 1 For $z$ approaching $z_{0}$ in the direction of the $x$ axis, $\Delta z=\Delta x$.

Suppose that $z$ approaches $z_{0}$ along the direction of the $x$-axis, as in Figure 1 . Then $z=z_{0}+\Delta x=\left(x_{0}+\Delta x, y_{0}\right), \Delta z=z-z_{0}=\Delta x$, and (1) becomes

$$
\begin{aligned}
& \text { 2) } f^{\prime}\left(z_{0}\right)=\lim _{\Delta x \rightarrow 0} \frac{f\left(x_{0}+\Delta x+i y_{0}\right)-f\left(x_{0}+i y_{0}\right)}{\Delta x} \\
& =\lim _{\Delta x \rightarrow 0}\left(\frac{u\left(x_{0}+\Delta x, y_{0}\right)-u\left(x_{0}, y_{0}\right)}{\Delta x}+i \frac{v\left(x_{0}+\Delta x, y_{0}\right)-v\left(x_{0}, y_{0}\right)}{\Delta x}\right) \\
& =\lim _{\Delta x \rightarrow 0} \frac{u\left(x_{0}+\Delta x, y_{0}\right)-u\left(x_{0}, y_{0}\right)}{\Delta x}+i \lim _{\Delta x \rightarrow 0} \frac{v\left(x_{0}+\Delta x, y_{0}\right)-v\left(x_{0}, y_{0}\right)}{\Delta x},
\end{aligned}
$$

where the last step is justified by Theorem 3, Section 2.2, which asserts that the limit of a complex-valued function exists if and only if the limits

![](af4f9593-dec7-4bc0-8d78-d25500419ec9-29_492_505_394_101.jpg)
Figure 2 For $z$ approaching $z_{0}$ in the direction of the $y$ axis, $\Delta z=i \Delta y$.

## THE CAUCHY-RIEMANN EQUATIONS

of its real and imaginary parts exist. Recognizing the last two limits on the right as the partial derivatives with respect to $x$ of $u$ and $v$ (see (2) and (3), Section 2.1), we obtain
which is an expression of the derivative of $f$ in terms of the partial derivatives with respect to $x$ of $u$ and $v$. We now repeat the preceding steps, going back to (1) and taking the limit as $z$ approaches $z_{0}$ from the direction of the $y$ axis, as in Figure 2. Then $z=z_{0}+i \Delta y=\left(x_{0}, y_{0}+\Delta y\right), \Delta z=z-z_{0}=i \Delta y$. Proceed as in (2), note that $i \Delta y \rightarrow 0$ if and only if $\Delta y \rightarrow 0$, and obtain

$$
\begin{aligned}
& f^{\prime}\left(z_{0}\right)=\lim _{\Delta y \rightarrow 0} \frac{f\left(x_{0}+i\left(y_{0}+\Delta y\right)\right)-f\left(x_{0}+i y_{0}\right)}{i \Delta y} \\
= & \lim _{\Delta y \rightarrow 0}\left(\frac{u\left(x_{0}, y_{0}+\Delta y\right)-u\left(x_{0}, y_{0}\right)}{i \Delta y}+i \frac{v\left(x_{0}, y_{0}+\Delta y\right)-v\left(x_{0}, y_{0}\right)}{i \Delta y}\right) \\
= & \lim _{\Delta y \rightarrow 0} \frac{v\left(x_{0}, y_{0}+\Delta y\right)-v\left(x_{0}, y_{0}\right)}{\Delta y}-i \lim _{\Delta y \rightarrow 0} \frac{u\left(x_{0}, y_{0}+\Delta y\right)-u\left(x_{0}, y_{0}\right)}{\Delta y},
\end{aligned}
$$

where in the last step we have used $1 / i=-i$ and rearranged the terms. Recognizing the partial derivatives with respect to $y$ of $v$ and $u$, we obtain

$$
f^{\prime}\left(z_{0}\right)=\frac{\partial v}{\partial y}\left(x_{0}, y_{0}\right)-i \frac{\partial u}{\partial y}\left(x_{0}, y_{0}\right),
$$

which is this time an expression of the derivative of $f$ in terms of the partial derivatives with respect to $y$ of $u$ and $v$. Now comes the startling result. Equate real and imaginary parts in (3) and (5) and get

$$
\frac{\partial u}{\partial x}=\frac{\partial v}{\partial y} \quad \text { and } \quad \frac{\partial u}{\partial y}=-\frac{\partial v}{\partial x}
$$

Thus, in order for $f$ to be analytic, $u$ and $v$ must satisfy the Cauchy-Riemann equations. Moreover, since $f$ is analytic, $f^{\prime}$ is continuous, and it follows from (3) and (5) and Theorem 4(iv), Section 2.2, that $\frac{\partial u}{\partial x}, \frac{\partial v}{\partial x}, \frac{\partial u}{\partial y}$, and $\frac{\partial v}{\partial y}$ are all continuous. The converse of these statements is also true. In applications, we will need the converse, since to establish the analyticity of a function, it is often easier to check the Cauchy-Riemann equations and the continuity of the partial derivatives. Because the proof of the converse requires advanced topics from calculus of several variables, we postpone it until Section 2.6, where it will be treated in detail. Let us now summarize our discussion
and proceed with the applications. To simplify the notation, we will denote partial derivatives with subscripts, $\frac{\partial u}{\partial x}=u_{x}, \frac{\partial u}{\partial y}=u_{y}$, and so on.

THEOREM 1
CAUCHY-RIEMANN EQUATIONS

The function $f(z)=u(x, y)+i v(x, y)$ is analytic in an open set $S$ if and only if the partial derivatives of $u$ and $v$ are continuous and satisfy the Cauchy-Riemann equations
(7)

$$
u_{x}=v_{y} \quad \text { and } \quad u_{y}=-v_{x} .
$$

The derivative $f^{\prime}(z)$ is given as either of

$$
f^{\prime}(z)=u_{x}(x, y)+i v_{x}(x, y) \text { or } f^{\prime}(z)=v_{y}(x, y)-i u_{y}(x, y) .
$$

The Cauchy-Riemann equations appeared in 1821 in the early work of Cauchy on integrals of complex-valued functions. Their connection to the existence of the derivative, as stated in Theorem 1, appeared in 1851 in the doctoral dissertation of the great German mathematician, Bernhard Riemann (1826-1866). As it should be obvious to any one who has studied calculus, Riemann's work shaped the development of modern calculus. His study of complex functions was motivated by his work in hydrodynamics, fluid flow and other applied problems. Some of these applications and their connection to the Cauchy-Riemann equations will be explored in the following section and Chapter 6.

Our first example is perhaps the most important example of an analytic function.

## EXAMPLE $1 e^{z}$ is entire.

Show that $e^{z}$ is entire and

$$
\frac{d}{d z} e^{z}=e^{z} .
$$

Solution We will use Theorem 1. From (4), Section 1.5, we have $e^{z}=e^{x} \cos y+ i e^{x} \sin y$. Thus, $u(x, y)=e^{x} \cos y$ and $v(x, y)=e^{x} \sin y$. Differentiating $u$ with respect to $x$ and $y$, we find

$$
\frac{\partial u}{\partial x}=e^{x} \cos y, \quad \frac{\partial u}{\partial y}=-e^{x} \sin y .
$$

Differentiating $v$ with respect to $x$ and $y$, we find

$$
\frac{\partial v}{\partial x}=e^{x} \sin y, \quad \frac{\partial v}{\partial y}=e^{x} \cos y .
$$

Comparing these derivatives, we see clearly that $\frac{\partial u}{\partial x}=\frac{\partial v}{\partial y}$ and $\frac{\partial u}{\partial y}=-\frac{\partial v}{\partial x}$. Hence the Cauchy-Riemann equations are satisfied at all points. The continuity of the partial
derivatives follows from Proposition 1, Section 2.2 (see the discussion preceding the proposition). Appealing to Theorem 1, we conclude that $e^{z}$ is analytic at all points, or entire. For the derivative, we appeal to either formula from (8), say the first, and use the formulas that we derived for the partial derivatives of $u$ and $v$. We get

$$
\frac{d}{d z} e^{z}=\frac{\partial u}{\partial x}+i \frac{\partial v}{\partial x}=e^{x} \cos y+i e^{x} \sin y=e^{z}
$$

Combining the chain rule with the result of Example 1, we see that $e^{f(z)}$ is analytic wherever $f(z)$ is analytic and

$$
\frac{d}{d z} e^{f(z)}=f^{\prime}(z) e^{f(z)}
$$

EXAMPLE $2 \sin z$ is entire.
Show that $\sin z$ is entire and

$$
\frac{d}{d z} \sin z=\cos z
$$

Solution There are at least two ways to do this problem. Since

$$
\sin z=\frac{e^{i z}-e^{-i z}}{2 i},
$$

(see (3), Section 1.6), we can appeal to (10) and conclude that $\sin z$ is entire and

$$
\frac{d}{d z} \sin z=\frac{d}{d z}\left(\frac{e^{i z}-e^{-i z}}{2 i}\right)=\frac{i e^{i z}-(-i) e^{-i z}}{2 i}=\frac{e^{i z}+e^{-i z}}{2}=\cos z,
$$

by (2), Section 1.6. The second method is a little longer but it will afford us the opportunity to practice the Cauchy-Riemann equations. From (16), Section 1.6, we have

$$
\sin z=\sin x \cosh y+i \cos x \sinh y .
$$

We have

$$
\begin{aligned}
& u(x, y)=\sin x \cosh y \Rightarrow u_{x}(x, y)=\cos x \cosh y, \quad u_{y}(x, y)=\sin x \sinh y \\
& v(x, y)=\cos x \sinh y \Rightarrow v_{x}(x, y)=-\sin x \sinh y, \quad v_{y}(x, y)=\cos x \cosh y .
\end{aligned}
$$

Comparing partial derivatives, we see that the Cauchy-Riemann equations are satisfied at all points. Moreover, the partial derivatives are continuous. Appealing to Theorem 1, we see that $\sin z$ is entire and

$$
\frac{d}{d z} \sin z=u_{x}(x, y)+i v_{x}(x, y)=\cos x \cosh y-i \sin x \sinh y=\cos z
$$

by (15), Section 1.6.
Following the methods of Example 2, we can check the analyticity and compute the derivatives of $\cos z, \tan z$, and all other trigonometric and hyperbolic functions. Among the elementary functions, we are then left with
the logarithm and those functions defined using the logarithm, such as complex powers. To handle them, we will appeal to Theorem 4, Section 2.3.

EXAMPLE $3 \log z$ is analytic except on the branch cut.
Show that the principal branch of the logarithm, $\log z$, is analytic on $\mathbb{C} \backslash(-\infty, 0]$, and that

$$
\frac{d}{d z} \log z=\frac{1}{z}
$$

Thus the familiar formula from calculus still holds.
Solution The result is straightforward from Theorem 4, Section 2.3, and the fact that $e^{z}$ is entire with $\frac{d}{d z} e^{z}=e^{z}$. In the notation of Theorem 4, Section 2.3, set $f(z)=e^{z}, g(z)=\log z$, and $h(z)=z$. Since $h(z)$ is analytic, $f(z)$ is analytic with $f^{\prime}(z)=e^{z} \neq 0$, and $g(z)$ is continuous everywhere except on the branch cut, we conclude that $g(z)$ is analytic there with

$$
\frac{d}{d z} \log z=\frac{h^{\prime}(z)}{f^{\prime}(g(z))}=\frac{1}{e^{\log z}}=\frac{1}{z}
$$

The logarithm cannot be analytic on the branch cut, because it is not continuous there (see Theorem 5, Section 2.2). $\square$

Using the method of Example 3, we can show that any branch of the logarithm, $\log _{\alpha} z$, is analytic everywhere except at its branch cut (the ray at angle $\alpha$ ), and

$$
\frac{d}{d z} \log _{\alpha} z=\frac{1}{z}
$$

As a consequence, any function constructed from the logarithms according to rules that preserve analyticity will be analytic on an appropriate domain. As an illustration, take the principal branch of a power,

$$
z^{a}=e^{a \log z} \quad(\text { where } a \neq 0 \text { is a complex number }) .
$$

Since $\log z$ is analytic except at its branch cut, and $e^{z}$ is entire, it follows that $z^{a}$ is analytic, except at the branch cut of $\log z$. To compute its derivative, we use the chain rule and the derivatives of $e^{z}$ and $\log z$ and get

$$
\frac{d}{d z} z^{a}=a z^{a-1}
$$

with principal branches of the power on both sides.
We started this section with the example of $\bar{z}$ and how it fails to be analytic at all points. This should be obvious now from the Cauchy-Riemann equations. If you write $\bar{z}=x-i y$, then $u_{x}=1, v_{y}=-1$, showing that the

## THEOREM 2

![](af4f9593-dec7-4bc0-8d78-d25500419ec9-33_492_505_1222_112.jpg)
Figure 3 A nonconstant function with zero derivative. Its domain of definition is the nonconnected shaded area.

## COROLLARY 1

Cauchy-Riemann equations do not hold at any point. As our next example illustrates, we can use the Cauchy-Riemann equations to show the failure of analyticity in less obvious situations.

## EXAMPLE 4 Failure of analyticity

Use the Cauchy-Riemann equations to show that $f(z)=x^{2}+i(2 y+x)$ fails to be analytic at all points.
Solution We have $u(x, y)=x^{2}$ and $v(x, y)=2 y+x$. Since $u_{y}=0$ and $v_{x}=1$, the Cauchy-Riemann equations are not satisfied at any point and hence the function cannot be analytic at any point.

The Cauchy-Riemann equations may hold only at one point (see Exercise 13 for an illustration). This does not imply that the function is analytic at that point, since analyticity requires that these equations be satisfied in a neighborhood.

The final applications show how the Cauchy-Riemann equations can be used to derive important results of theoretical nature.

Suppose that $f(z)=u(x, y)+i v(x, y)$ is analytic in a region (open and connected) $\Omega$ and $f^{\prime}(z)=0$ for all $z$ in $\Omega$. Then $f$ is constant in $\Omega$.

Proof By Theorem 1, we have

$$
f^{\prime}(z)=u_{x}(x, y)+i v_{x}(x, y) \text { and } f^{\prime}(z)=v_{y}(x, y)-i u_{y}(x, y), \quad z \text { in } \Omega .
$$

Since $f^{\prime}(z)=0$ it follows that $u_{x}=u_{y}=0$ and $v_{x}=v_{y}=0$ in $\Omega$. Appealing to Theorem 1, Section 2.1, we conclude that $u$ is constant and $v$ is constant, and hence $f=u+i v$ is constant.

The connectedness of $\Omega$ in the theorem is essential. For example, the function $f$, defined on the set $S$ in Figure 3, by

$$
f(z)= \begin{cases}1 & \text { if }|z|<2 \\ 0 & \text { if }|z|>3\end{cases}
$$

has zero derivative but is not constant.
Suppose that $f$ and $g$ are analytic in a region $\Omega$. If either $\operatorname{Re} f=\operatorname{Re} g$ on $\Omega$ or $\operatorname{Im} f=\operatorname{Im} g$ on $\Omega$, then $f(z)=g(z)+c$ on $\Omega$, where $c$ is a constant.

Proof We do the case $\operatorname{Re} f=\operatorname{Re} g$ on $\Omega$. The case $\operatorname{Im} f=\operatorname{Im} g$ is very similar and is left to Exercise 32. Let $h(z)=f(z)-g(z)=u(z)+i v(z)$. We want to show that $h(z)=c$ on $\Omega$. Since $h$ is analytic, it is enough by Theorem 1 to show that $h^{\prime}(z)=0$ on $\Omega$. We have $u=\operatorname{Re} h=\operatorname{Re} f-\operatorname{Re} g=0$ on $\Omega$, and so $u_{x}=u_{y}=0$ on $\Omega$. By the Cauchy-Riemann equations, $v_{x}=-u_{y}=0$. Consequently, by (8), $h^{\prime}(z)=u_{x}+i v_{x}=0$ on $\Omega$.

## Exercises 2.4

In Exercises 1-14, use the Cauchy-Riemann equations (Theorem 1) to determine the set on which the given function is analytic and compute its derivative using either one of equations (8).

1. $z$.
2. $z^{2}$.
3. $e^{z^{2}}$.
4. $2 x+3 i y$.
5. $e^{\bar{z}}$.
6. $\frac{y-i x}{x^{2}+y^{2}}$.
7. $\left(\frac{1}{z+1}\right)^{2}$.
8. $\frac{z}{z-i}$.
9. $z e^{z}$.
10. $\cos z$.
11. $\tan z$.
12. $\cosh z$.
13. $|z|^{2}$.
14. $\frac{x^{4}+i 2 x y\left(x^{2}+y^{2}\right)-y^{4}+x-i y}{x^{2}+y^{2}}$.

In Exercises 15-26, use properties of the derivative to compute the derivative of the given function and determine the set on which it is analytic. In Exercises 23-26, use the principal branch of the power.
15. $z e^{z^{2}}$.
16. $\left(1+e^{z}\right)^{5}$.
17. $\sin z \cos z$.
18. $\log (z+1)$.
19. $\frac{\log (3 z-1)}{z^{2}+1}$.
20. $\sinh (3 z+i)$.
21. $\cosh \left(z^{2}+3 i\right)$.
22. $\log _{\frac{\pi}{2}}(z+1)$.
23. $z^{i}$.
24. $(z+1)^{1 / 2}$.
25. $\frac{1}{(z-i)^{1 / 2}}$.
26. $z^{z}$.

In Exercises 27-30, compute the given limit by identifying it as a derivative; alternatively, you may use L'Hospital's rule (Exercise 27, Section 2.3).
27. $\lim _{z \rightarrow 0} \frac{\sin z}{z}$.
28. $\lim _{z \rightarrow 0} \frac{e^{z}-1}{z}$.
29. $\lim _{z \rightarrow 0} \frac{\log (z+1)}{z}$.
30. $\lim _{z \rightarrow i} \frac{1+i z}{z(z-i)}$.
31. Define the principal branch of the inverse tangent by taking the principal branch of the logarithm in (13), Section 1.7:

$$
\tan ^{-1} z=\frac{i}{2} \log \left(\frac{1-i z}{1+i z}\right)
$$

Compute the derivative of $\tan ^{-1} z$. 32. Complete the proof of Corollary 1 by treating the case $\operatorname{Im} f=\operatorname{Im} g$ on $\Omega$.
33. Suppose that $f=u+i v$ is analytic in a region $\Omega$. Show that
(a) $f^{\prime}(z)=u_{x}-i u_{y}$, also $f^{\prime}(z)=v_{y}+i v_{x}$; and
(b) $\left|f^{\prime}(z)\right|^{2}=u_{x}^{2}+u_{y}^{2}=v_{x}^{2}+v_{y}^{2}$.
(c) Conclude from (a) or (b) that if either Re $f$ or $\operatorname{Im} f$ is constant in $\Omega$, then $f$ is constant in $\Omega$.
34. Suppose that $f(z)$ and $\overline{f(z)}$ are analytic in a region $\Omega$. Show that $f(z)$ must be constant in $\Omega$. [Hint: Consider $f(z)+\overline{f(z)}$ and use Exercise 33.]
35. Let us define the partial derivatives of a complex-valued function $f=u+i v$ as $f_{x}=u_{x}+i v_{x}$ and $f_{y}=u_{y}+i v_{y}$. Show that the Cauchy-Riemann equations are equivalent to $f_{x}+i f_{y}=0$.
36. Suppose that $f$ is analytic in a region $\Omega$ and $f[\Omega]$ is a subset of a line. Show that $f$ must be constant in $\Omega$. [Hint: Rotate the line to make it horizontal or vertical and apply one of Exercise 33.]
37. Suppose that $f=u+i v$ is analytic in a region $\Omega$ and $\operatorname{Re} f=\operatorname{Im} f$. Show that $f$ must be constant in $\Omega$. [Hint: Use Exercise 36 or prove it directly from the Cauchy-Riemann equations.]
38. Suppose that $f=u+i v$ is analytic in a region $\Omega$ and $|f|$ is constant in $\Omega$. Show that $f$ must be constant in $\Omega$ as follows.
(a) Show that $u^{2}+v^{2}=c$ where $c$ is a nonnegative constant, and that we need only consider the case $c>0$.
(b) Obtain the following system of equations in the unknowns $u_{x}, u_{y}$ :

$$
\left\{\begin{array}{l}
u u_{x}-v u_{y}=0 \\
v u_{x}+u u_{y}=0
\end{array}\right.
$$

[Hint: Differentiate $u^{2}+v^{2}=c$ with respect to $x$ then differentiate it with respect to $y$ and use the Cauchy-Riemann equations.]
(c) Show that the only solutions of the equations in (b) are $u_{x}=0$ and $u_{y}=0$.
[Hint: The determinant of the system is $>0$.]
(d) Show that $v_{x}, v_{y}$ and $f^{\prime}$ are zero on $\Omega$, and conclude that $f$ is constant.
39. Project Problem: Cauchy-Riemann equations in polar form. In this problem we express the Cauchy-Riemann equations in polar coordinates. Recall the relationships between Cartesian and polar coordinates:

$$
x=r \cos \theta \quad \text { and } \quad y=r \sin \theta
$$

For convenience, we write $u(r, \theta)=u(r \cos \theta, r \sin \theta)=u(x, y)$ and $v(r, \theta)= v(r \cos \theta, r \sin \theta)=v(x, y)$.
(a) The multivariable chain rule from calculus (see also (13), Section 2.6) states that

$$
\begin{array}{ll}
\frac{\partial u}{\partial r}=\frac{\partial u}{\partial x} \frac{\partial x}{\partial r}+\frac{\partial u}{\partial y} \frac{\partial y}{\partial r}, & \frac{\partial u}{\partial \theta}=\frac{\partial u}{\partial x} \frac{\partial x}{\partial \theta}+\frac{\partial u}{\partial y} \frac{\partial y}{\partial \theta} \\
\frac{\partial v}{\partial r}=\frac{\partial v}{\partial x} \frac{\partial x}{\partial r}+\frac{\partial v}{\partial y} \frac{\partial y}{\partial r}, & \frac{\partial v}{\partial \theta}=\frac{\partial v}{\partial x} \frac{\partial x}{\partial \theta}+\frac{\partial v}{\partial y} \frac{\partial y}{\partial \theta} .
\end{array}
$$

Show that

$$
\begin{array}{ll}
\frac{\partial u}{\partial r}=\cos \theta \frac{\partial u}{\partial x}+\sin \theta \frac{\partial u}{\partial y}, & \frac{\partial u}{\partial \theta}=-r \sin \theta \frac{\partial u}{\partial x}+r \cos \theta \frac{\partial u}{\partial y} \\
\frac{\partial v}{\partial r}=\cos \theta \frac{\partial v}{\partial x}+\sin \theta \frac{\partial v}{\partial y}, & \frac{\partial v}{\partial \theta}=-r \sin \theta \frac{\partial v}{\partial x}+r \cos \theta \frac{\partial v}{\partial y}
\end{array}
$$

(b) Derive the polar form of the Cauchy-Riemann equations:

$$
u_{r}=\frac{1}{r} v_{\theta} \quad \text { and } \quad v_{r}=-\frac{1}{r} u_{\theta}
$$

Thus we can state Theorem 1 in polar form as follows. The function $f(z)= u(r, \theta)+i v(r, \theta)$ is analytic at $z_{0} \neq 0$ if and only if, in a neighborhood of $z_{0}$,
$u_{r}, u_{\theta}, v_{r}$, and $v_{\theta}$ are continuous and satisfy the polar form of the Cauchy-Riemann equations.
(c) Show that the derivative $f^{\prime}(z)$ is given by

$$
f^{\prime}(z)=e^{-i \theta}\left(u_{r}+i v_{r}\right) .
$$

This represents $f^{\prime}(z)$ in terms of a radial directional derivative of $u$ and $v$ divided by the unimodular number $e^{i \theta}$ that gives the direction of $f^{\prime}(z)$.
In Exercises 40-42, use the polar form of the Cauchy-Riemann equations to check the analyticity and find the derivative of the given function.
40. $f(z)=z^{n}=r^{n}(\cos (n \theta)+i \sin (n \theta))(n= \pm 1, \pm 2, \ldots)$.
41. $f(z)=\log z=\ln |z|+i \operatorname{Arg} z$.
42. $f(z)=\sin (\log z)$.
43. Jacobian of a transformation. The Jacobian of the mapping $(x, y) \mapsto (u(x, y), v(x, y))$ is the following determinant:

$$
J=\operatorname{det}\left|\begin{array}{ll}
\frac{\partial u}{\partial x} & \frac{\partial u}{\partial y} \\
\frac{\partial v}{\partial x} & \frac{\partial v}{\partial y}
\end{array}\right| .
$$

Suppose that $f=u+i v$ is analytic. Show that the Jacobian equals $\left|f^{\prime}(z)\right|^{2}$. You may recall from calculus of several variables that a mapping is locally invertible at every point where the Jacobian is nonzero. This exercise suggests that a similar result holds for $f$. Indeed, there is an inverse function theorem that states that if $f^{\prime}\left(z_{0}\right) \neq 0$, then in some neighborhood of $z_{0}, f$ is one-to-one and has an inverse function that is itself analytic in a neighborhood of $f\left(z_{0}\right)$ (see Section 5.7).

### 2.5 Harmonic Functions and Laplace's Equation

There are many important applications of complex analysis that highlight its pivotal place in the solution of real-world problems. The ones that we present in this section deal with a fundamental equation of applied mathematics, known as Laplace's equation. This equation models important phenomena in engineering and physics, such as steady-state temperature distributions, electrostatic potentials, and fluid flow, to name just a few. For clarity's sake, we will base our presentation around steady-state temperature problems. The solutions that we present use almost all the material that we have covered thus far, and more important, they stress the need for further development of the theory.

## Laplace's Equation and Harmonic Functions

Consider a two-dimensional plate of homogeneous material, with instlated lateral surfaces. We represent this plate by a region $\Omega$ in the complex plane (see Figure 1). Suppose that the temperature of the points on the boundary of the plate is given by a function of position $b(x, y)$ that does not change with time. It is a fact from thermodynamics that the temperature inside the plate will eventually reach and remain at an equilibrium

![](af4f9593-dec7-4bc0-8d78-d25500419ec9-37_459_508_201_110.jpg)
Figure 1 The steady-state temperature distribution satisfies Laplace's equation.

The Laplacian is named after the great French mathematician and physicist PierreSimon de Laplace (17491827). The Laplacian appeared for the first time in a memoir of Laplace in 1784, in which he completely determined the attraction of a spheroid on the points outside it. The Laplacian of a function measures the difference between the value of the function at a point and the average value of the function in a neighborhood of that point. Thus a function that does not vary abruptly has a very small Laplacian. Harmonic functions have a zero Laplacian; they vary in a very regular way. Examples of such functions include the temperature distribution in a plate, the potential of the attractive force due to a sphere, the function that gives the brightness of colors in an image.
distribution, known as the steady-state distribution. For ( $x, y$ ) in $\Omega$, let $u(x, y)$ denote this steady-state temperature distribution. It is also a fact from thermodynamics that $u(x, y)$ satisfies the (two-dimensional) Laplace's equation

$$
\Delta u=\frac{\partial^{2} u}{\partial x^{2}}+\frac{\partial^{2} u}{\partial y^{2}}=0
$$

Here $\Delta u$ is the Laplacian of $u$, which by definition is $\frac{\partial^{2} u}{\partial x^{2}}+\frac{\partial^{2} u}{\partial y^{2}}$. Since Laplace's equation involves partial derivatives, it is called a partial differential equation. Any real-valued function that satisfies Laplace's equation on a region $\Omega$ and has continuous first and second partial derivatives is called harmonic on $\Omega$. Constant functions are clearly harmonic on the entire plane, and so are the functions $u(x, y)=x, u(x, y)=y, u(x, y)=x y$. Less obvious examples of harmonic functions will be derived from Theorem 1 later in this section.

To determine the steady-state temperature inside the plate, we must solve Laplace's equation inside of $\Omega$ subject to the condition $u(x, y)= b(x, y)$ on the boundary of $\Omega$, known as a boundary condition. A problem consisting of a partial differential equation along with specified boundary conditions is known as a boundary value problem. The special case involving Laplace's equation with specified boundary values is known as a Dirichlet problem. Solving Dirichlet problems is of paramount importance in applied mathematics, engineering, and physics. Many methods have been developed. The ones that we will present in this section provide a beautiful application of complex analysis.

## Connection with Analytic Functions

Let $f=u+i v$ be an analytic function. We know that $u$ and $v$ satisfy the Cauchy-Riemann equations (Theorem 1, Section 2.4),

$$
\frac{\partial u}{\partial x}=\frac{\partial v}{\partial y} \quad \text { and } \quad \frac{\partial u}{\partial y}=-\frac{\partial v}{\partial x} .
$$

Let us suppose for a moment that we can differentiate $u$ and $v$ twice and interchange the order of partial derivatives. Then

$$
\frac{\partial^{2} u}{\partial x^{2}}=\frac{\partial}{\partial x}\left(\frac{\partial u}{\partial x}\right)=\frac{\partial}{\partial x}\left(\frac{\partial v}{\partial y}\right)=\frac{\partial}{\partial y}\left(\frac{\partial v}{\partial x}\right)=\frac{\partial}{\partial y}\left(-\frac{\partial u}{\partial y}\right)=-\frac{\partial^{2} u}{\partial y^{2}},
$$

and hence $\frac{\partial^{2} u}{\partial x^{2}}+\frac{\partial^{2} u}{\partial y^{2}}=0$. In other words, $u$ satisfies Laplace's equation. Reasoning in a similar way, we can show that $v$ also satisfies Laplace's equation.

Recall from calculus that in order to justify the interchange of partial derivatives as we needed to do above, it is enough to know that all first and

THEOREM 1 ANALYTIC AND HARMONIC FUNCTIONS
second partial derivatives are continuous. One of the major results that we will develop in the following chapter guarantees that the real and imaginary parts of an analytic function have continuous partial derivatives of all orders. Thus, the steps that we used above are justified and $u$ and $v$ are harmonic.

## Suppose that $f=u+i v$ is analytic on an open set $S$. Then its real and inaginary parts $u(x, y)$ and $v(x, y)$ are harmonic on $S$.

What this result effectively does for us is provide us with many examples of harmonic functions; simply take the real or imaginary part of any analytic function.

## EXAMPLE 1 Harmonic functions

Show that the following are harmonic functions in the stated region.
(a) $u(x, y)=x^{2}-y^{2}$ on $\mathbb{C}$.
(b) $u(x, y)=e^{x} \sin y$ on $\mathbb{C}$.
(c) $u(x, y)=\operatorname{Arg} z(z=(x, y))$ on the region $\Omega=\mathbb{C} \backslash(-\infty, 0]$.
(d) $u(x, y)=\ln |z|=\ln \sqrt{x^{2}+y^{2}}$ on the region $\mathbb{C} \backslash\{0\}$.

Solution (a) It is easy to see that $u$ is harmonic here by direct verification of Laplace's equation; but we recognize that $u(x, y)=x^{2}-y^{2}$ is the real part of the entire function $f(z)=z^{2}=\left(x^{2}-y^{2}\right)+2 i x y$. Thus from Theorem 1 we conclude that $u$ is harmonic on $\mathbb{C}$.
(b) Recognizing $u(x, y)=e^{x} \sin y$ as the imaginary part of the entire function $f(z)=e^{z}$ (see (16), Section 1.6), we conclude from Theorem 1 that $u$ is harmonic on $\mathbb{C}$.
(c) We have $\operatorname{Arg} z=\operatorname{Im}(\log z)$, where $\log z=\ln |z|+i \operatorname{Arg} z$ is the principal branch of the logarithm (see (4), Section 1.7). Since $\log z$ is analytic on $\Omega$, we conclude that $\operatorname{Arg} z$ is harmonic on $\Omega$, by Theorem 1.
(d) This part is interesting because we will need two different analytic functions to establish the desired result. Arguing as in (c), it follows that $\ln |z|=\ln \sqrt{x^{2}+y^{2}}$ is harmonic on $\Omega=\mathbb{C} \backslash(-\infty, 0]$, being the real part of $\log z$, which is analytic on $\mathbb{C} \backslash(-\infty, 0]$. This establishes that $\ln |z|$ is harmonic on the desired region except on the negative $x$-axis, $(-\infty, 0)$. To show that $\ln |z|$ is harmonic on $(-\infty, 0)$, we will use $\log _{\alpha} z$, which is a branch of $\log z$ with branch cut at angle $\alpha$, with $-\pi<\alpha<\pi$. We have from (6), Section 1.7, $\log _{\alpha} z=\ln |z|+\arg _{\alpha} z$, and from our discussion in Section 2.4 leading to (13), $\log _{\alpha} z$ is analytic except at the branch cut and, in particular, is analytic on the negative $x$-axis. Hence, its real part, $\ln |z|$, is harmonic on the negative $x$-axis.

You can also answer part (d) directly by verifying that $\ln \sqrt{x^{2}+y^{2}}=\frac{1}{2} \ln \left(x^{2}+\right. y^{2}$ ) satisfies Laplace's equation and the first and second partial derivatives are continuous everywhere except at the origin.

The following property of harmonic functions is very useful. Its proof is left to Exercise 18.
Suppose that $u$ and $v$ are harmonic on an open set $S$, and $a, b$ are resed constants. Then $a u(x, y)+b v(x, y)$ is harmonic on $S$.

PROPOSITION 1 LINEARITY

For example, $\phi(x, y)=2\left(x^{2}-y^{2}\right)+7$ is harmonic, being of the form $\phi(x, y)=2 u(x, y)+7$ where $u$ is the harmonic function of Example 1(a). Also the function $\phi(x, y)=(a x+b)(c y+d)$, where $a, b, c, d$ are real constants, is harmonic, being a linear combination of the harmonic functions $x, y, x y$, and constants.

You should be cautioned that the product of two harmonic functions need not be harmonic. For example, $u(x, y)=x$ is harmonic, but $(u(x, y))^{2}=x^{2}$ is not.

## Harmonic Conjugates

Reading Theorem 1, it is natural to ask the following question: Given a harmonic function $u$ in a region $\Omega$, can we find another harmonic function $v$ in $\Omega$ such that $f=u+i v$ is analytic in $\Omega$ ? Such a function $v$ is called a harmonic conjugate of $u$. Conditions for the existence of a harmonic conjugate will be established in Chapter 3. For now, just keep in mind that the existence of a harmonic conjugate depends on the nature of the region under consideration. For example, the function $\ln |z|$ is harmonic in $\Omega= \mathbb{C} \backslash\{0\}$ (Example 1(d)); but $\ln |z|$ has no harmonic conjugate in that region (Exercise 33). It does, however, have a harmonic conjugate in $\mathbb{C} \backslash(-\infty, 0]$, namely $\operatorname{Arg} z$. As our next example shows, by integrating the CauchyRiemann equations, we can always find the harmonic conjugate in a region such as the entire complex plane, a disk, or a rectangle. (More generally, we will show in Chapter 3 that we can find a harmonic conjugate if the region is simply connected. This more restrictive concept of connectedness is extremely important and will be at the heart of Chapter 3.)

## EXAMPLE 2 Finding harmonic conjugates

Show that $u(x, y)=x^{2}-y^{2}+x$ is harmonic in the entire plane and find a harmonic conjugate.
Solution That $u$ is harmonic follows from $u_{x x}=2$ and $u_{y y}=-2$. To find a harmonic conjugate $v$, we use the Cauchy-Riemann equations as follows. We want $u+i v$ to be analytic. Hence $v$ must satisfy the Cauchy-Riemann equations

$$
\frac{\partial u}{\partial x}=\frac{\partial v}{\partial y}, \quad \text { and } \quad \frac{\partial u}{\partial y}=-\frac{\partial v}{\partial x} .
$$

Since $\frac{\partial u}{\partial x}=2 x+1$, the first equation implies that

$$
2 x+1=\frac{\partial v}{\partial y}
$$

To get $v$ we will integrate both sides of this equation with respect to $y$. However, because $v$ is a function of $x$ and $y$, the constant of integration in your answer may be a function of $x$. Thus integrating with respect to $y$ yields

$$
v(x, y)=(2 x+1) y+c(x)
$$

## PROPOSITION 2

## PROPOSITION 3

![](af4f9593-dec7-4bc0-8d78-d25500419ec9-40_480_528_1485_142.jpg)
Figure 2 The curves $C_{1}$ and $C_{2}$ are orthogonal at $A$ if the tangent lines $L_{1}$ and $L_{2}$ (at $A$ ) are orthogonal.

where $c(x)$ is a function of $x$ alone. Plugging this into the second equation in (2), we get

$$
-2 y=-\left(2 y+\frac{d}{d x} c(x)\right)
$$

and hence $c(x)$ has zero derivative and must be a constant. Let us pick any such constant and write $c(x)=C$. Substituting into the expression for $v$ we get $v(x, y)= (2 x+1) y+c(x)=2 x y+y+C$. You should verify the Cauchy-Riemann equations for the pair of functions $u$ and $v$ and conclude that $\left(x^{2}-y^{2}+x\right)+i(2 x y+y+C)$ is entire.

So, from Example 2, a harmonic conjugate of $u(x, y)=x^{2}-y^{2}+x$ is $v(x, y)=2 x y+y$. What is a harmonic conjugate of $v(x, y)=2 x y+y$ ? Surely it is related to $u$. Indeed, you can check that a conjugate of $v$ is $-u(x, y)=-x^{2}+y^{2}-x$. More generally, we have the following useful result.
Suppose that $u$ is harmonic and that $v$ is a harmonic conjugate of $u$. Then $-u$ is a harmonic conjugate of $v$.
Proof We know that $f=u+i v$ is analytic. It follows that the function $(-i) f= v-i u$ is analytic, and hence $-u$ is a harmonic conjugate of $v$.

In Example 2, we found the harmonic conjugate of $u$ up to an arbitrary additive real constant. In fact, the following properties of the harmonic conjugate are not hard to prove (Exercise 18).
Suppose that $u$ is a harmonic function in a region $\Omega$. Then
(i) if $v_{1}$ and $v_{2}$ are harmonic conjugates of $u$ in $\Omega$, then $v_{1}$ and $v_{2}$ must differ by a real constant.
(ii) If $v$ is a harmonic conjugate of $u$, then $v$ is also a harmonic conjugate of $u+c$ where $c$ is any real constant.

The function $u$ and its conjugate $v$ have a very interesting geometric relationship based on the notion of orthogonal curves.

Suppose that two curves $C_{1}$ and $C_{2}$ meet at a point $A$. The curves are said to be orthogonal if their respective tangent lines $L_{1}$ and $L_{2}$ (at $A$ ) are orthogonal (Figure 2). We also say that $C_{1}$ and $C_{2}$ intersect at a right angle at $A$. Recall that if $m_{1}$ and $m_{2}$ denote the respective slopes of the tangent lines, and if neither is zero, then $L_{1}$ and $L_{2}$ are orthogonal if and only if

$$
m_{1} m_{2}=-1
$$

Two families of curves are said to be orthogonal if each curve from one family intersects the curves from the other family at right angles.

Consider the level curves of a harmonic function $u(x, y)$ in a region $\Omega$. These are the curves determined by the implicit relation

$$
u(x, y)=C_{1}
$$

THEOREM 2 ORTHOGONALITY OF LEVEL CURVES
where $C_{1}$ is a constant (in the range of $u$ ). Since $u$ is harmonic, it has continuous partial derivatives, and hence we can use the chain rule, Theorem 4, Section 2.6, to differentiate both sides of (4) with respect to $x$ and get

$$
\frac{\partial u}{\partial x} \frac{d x}{d x}+\frac{\partial u}{\partial y} \frac{d y}{d x}=0
$$

But $d x / d x=1$, so if $\frac{\partial u}{\partial y} \neq 0$, we can solve for $d y / d x$ and get

$$
\frac{d y}{d x}=-\frac{\frac{\partial u}{\partial x}}{\frac{\partial u}{\partial y}}
$$

This gives the slope of the tangent line at a point on a level curve. Now suppose that we can find a harmonic conjugate $v(x, y)$ of $u(x, y)$ in $\Omega$ and let us consider the level curves

$$
v(x, y)=C_{2}
$$

where $C_{2}$ is a constant (in the range of $v$ ). Since $v$ is harmonic, arguing as we did with $u$, we find that the slope of the tangent line at a point on a level curve is

$$
\frac{d y}{d x}=-\frac{\frac{\partial v}{\partial x}}{\frac{\partial v}{\partial y}}=\frac{\frac{\partial u}{\partial y}}{\frac{\partial u}{\partial x}}
$$

since by the Cauchy-Riemann equations, $\partial v / \partial x=-\partial u / \partial y$ and $\partial v / \partial y= \partial u / \partial x$. Comparing (6) and (7), we see that the slopes of the tangent lines satisfy the orthogonality relation (3), and hence the level curves of $u$ are orthogonal to the level curves of $v$. This orthogonality relation also holds when the tangents are horizontal and vertical. We thus have the following result.

Suppose that $u$ is a harmonic function in a region $\Omega$ and let $v$ be a harmonic conjugate of $u$ in $\Omega$, so that $f=u+i v$ is analytic in $\Omega$. Then, the two families of level curves, $u(x, y)=C_{1}$ and $v(x, y)=C_{2}$, are orthogonal at every point where $f^{\prime}(z) \neq 0$.

As an illustration, we show in Figure 3(a) and (b) the level curves of the harmonic function $u=x^{2}-y^{2}+x$ and its conjugate $v(x, y)=2 x y+y$ (see Example 2). The graphs of the two families are superposed in Figure 3(c) to illustrate their orthogonality.

Figure 3 (a) Level curves of $u(x, y)=x^{2}-y^{2}+x$.
(b) Level curves of $v(x, y)=2 x y+y$.
(c) The level curves of $u$ and $v$ are orthogonal.

![](af4f9593-dec7-4bc0-8d78-d25500419ec9-42_485_542_1401_100.jpg)
Figure 4 Dirichlet problem in Example 3.

![](af4f9593-dec7-4bc0-8d78-d25500419ec9-42_421_423_278_686.jpg)
(a)

![](af4f9593-dec7-4bc0-8d78-d25500419ec9-42_419_417_278_1164.jpg)
(b)

![](af4f9593-dec7-4bc0-8d78-d25500419ec9-42_415_406_278_1639.jpg)
(c)

## Solving and Interpreting Dirichlet Problems

We now return to our main topic: that of solving Dirichlet problems. Let us first mention an interesting example of a harmonic function, $u(x, y)= a \operatorname{Arg} z+b$, which is harmonic by Example 1(c) and Proposition 1. Because $\operatorname{Arg} z$ is constant on rays (independent of $r$ ), it follows that $u=a \operatorname{Arg} z+b$ is also constant on rays. (In fact, this is the only harmonic function with such a property. See Exercise 49.) Thus $u$ is a good candidate for a solution of Dirichlet problems in which the boundary data is constant on rays or independent of $r$. We illustrate these ideas with an example.

## EXAMPLE 3 A Dirichlet problem in a quadrant

The boundary of a large sheet of metal is kept at the constant temperatures $100^{\circ}$ on the bottom and $50^{\circ}$ on the left, as illustrated in Figure 4. After a long enough period of time, the temperature inside the plate reaches an equilibrium distribution. Find this steady-state temperature $u(x, y)$.
Solution The steady-state temperature is a solution of the Dirichlet problem, which consists of Laplace's equation

$$
\Delta u=0, \quad \text { inside } \Omega ;
$$

along with the boundary conditions

$$
u(x, 0)=100, x>0, \quad u(0, y)=50, y>0
$$

Based on our discussion preceding the example, because the boundary data is independent of $r$, we will try for a solution the harmonic function

$$
u(x, y)=a \operatorname{Arg} z+b
$$

where $a$ and $b$ are real constants to be determined so as to satisfy the boundary conditions. From the first condition

$$
u(x, 0)=100 \Rightarrow a \operatorname{Arg} x+b=100 \Rightarrow b=100
$$

because $\operatorname{Arg} x=0$ for $x>0$. From the second condition

$$
u(0, y)=50 \Rightarrow a \operatorname{Arg}(i y)+b=50 \Rightarrow a \frac{\pi}{2}+100=50 \Rightarrow a=-\frac{100}{\pi}
$$

![](af4f9593-dec7-4bc0-8d78-d25500419ec9-43_452_470_196_132.jpg)
Figure 5
A three-dimensional picture representing the temperature distribution of the plate. Note the boundary values on the graph.

![](af4f9593-dec7-4bc0-8d78-d25500419ec9-43_469_503_1047_101.jpg)
Figure 6 Dirichlet problem in Example 4.

because $\operatorname{Arg}(i y)=\frac{\pi}{2}$ for $y>0$, and $b=100$. Thus the steady-state temperature inside the plate is $u(x, y)=-\frac{100}{\pi} \operatorname{Arg}(z)+100$. Now for $z=x+i y$ with $x>0$, we have $\operatorname{Arg} z=\tan ^{-1}\left(\frac{y}{x}\right)$, and so another way of expressing the solution is

$$
u(x, y)=-\frac{100}{\pi} \tan ^{-1}\left(\frac{y}{x}\right)+100
$$

The graph of $u$ is shown in Figure 5. Note the temperature on the boundary; it matches the boundary conditions.

In contrast to $\operatorname{Arg} z$ we can find harmonic functions which are independent of the argument and depend only on $r=|z|$. An example of such a function is $u(z)=a \ln |z|+b$, where $a$ and $b$ are real constants. By Example $1(\mathrm{~d})$, this function is harmonic in $\mathbb{C} \backslash\{0\}$. It is a good candidate for a solution of Dirichlet problems in which the boundary data is constant on circles. See Exercises 29-32 for illustrations.

## EXAMPLE 4 A Dirichlet problem in an infinite strip

Solve the Dirichlet problem shown in Figure 6.
Solution Since the boundary data does not depend on $x$, it is plausible to guess that the solution will also not depend on $x$. In this case, $u(x, y)$ is a function of $y$ alone, hence $u_{x}=0$ and $u_{x x}=0$, and Laplace's equation becomes $u_{y y}=0$, implying that $u$ is a linear function of $y$. Hence $u(x, y)=a y+b$. Using the boundary conditions, we have

$$
\begin{aligned}
& u(x, 0)=0 \Rightarrow b=0 \\
& u(x, 1)=100 \Rightarrow a=100
\end{aligned}
$$

Hence the solution of the problem is $u(x, y)=100 y$, which is clearly harmonic and satisfies the boundary conditions.

In Example 4 we used a harmonic function that was independent of $x$. Similarly, we can find harmonic functions that are independent of $y$ (hence $u_{y}=0$ and $u_{y y}=0$ ). You can show in this case that $u=a x+b$, where $a$ and $b$ are real constants. This function is a good candidate for solving Dirichlet problems in infinite vertical strips with constant boundary data. See Exercises 25 and 26 for illustrations.

## Harmonic Conjugates, Isotherms, and Heat Flow

In Example 3, the temperature of the boundary is kept at two constant values, $100^{\circ}$ and $50^{\circ}$. Our physical intuition tells us that, because the plate is insulated, the temperature of the points inside the plate will vary between these two values and will equal those values only at the boundary. It is natural to ask for those points inside the plate with the same temperature $u(x, y)=T$, where $50<T<100$. These points lie on curves inside the plate, called curves of constant temperature or isotherms. Isotherms have many practical applications. Computing them will lead us to interesting properties of harmonic functions.
![](af4f9593-dec7-4bc0-8d78-d25500419ec9-44_487_543_244_106.jpg)

Figure 7 Isotherms in Example 5.

You should recall from vector calculus that the gradient vector $\nabla u=\left(u_{x}, u_{y}\right)$ points in the direction of greatest change in a function. The gradient is perpendicular to level curves of $u(x, y)$. Fourier's law states that heat flows along $-\nabla u$, and thus curves of heat flow are orthogonal to level curves of $u$, and hence coincident with level curves of $v$.

## EXAMPLE 5 Isotherms

Find the isotherms in Example 3.
Solution Since the temperature inside the plate will vary between $50^{\circ}$ and $100^{\circ}$, to find the isotherms, we must solve

$$
u(x, y)=T, \quad \text { where } \quad 50<T<100
$$

where ( $x, y$ ) is a point inside the first quadrant, not on the boundary. Appealing to the solution from Example 3, (8) becomes
(9) $\quad-\frac{100}{\pi} \tan ^{-1}\left(\frac{y}{x}\right)+100=T$, where $50<T<100, \quad x>0, y>0$.

Thus,

$$
\begin{aligned}
\tan ^{-1}\left(\frac{y}{x}\right)=\pi-\frac{\pi T}{100} & \Rightarrow \frac{y}{x}=\tan \left(\pi-\frac{\pi T}{100}\right) \\
& \Rightarrow \frac{y}{x}=-\tan \frac{\pi T}{100} \\
& \Rightarrow y=\overbrace{-\left(\tan \frac{\pi T}{100}\right)}^{\text {a positive constant }} x
\end{aligned}
$$

where we have used the identity $\tan (\pi-\alpha)=-\tan \alpha$ (check it!). Since $50< T<100, \frac{\pi}{2}<\frac{\pi T}{100}<\pi$ and so $-\tan \frac{\pi T}{100}>0$. Thus the equation of the isotherms $y=-\left(\tan \frac{\pi T}{100}\right) x$ corresponds to rays in the first quadrant emanating from the origin. As $T \rightarrow 100$, the slope of the ray $y=-\left(\tan \frac{\pi T}{100}\right) x$ goes to 0 , showing that the ray tends to the positive $x$-axis. As $T \rightarrow 50$, the slope of the ray $-\tan \frac{\pi T}{100} \rightarrow \infty$, showing that the ray tends to the positive $y$-axis. This agrees with our intuition, since points near the $x$-axis have temperature close to $100^{\circ}$, and points near the $y$-axis have temperature close to $50^{\circ}$. The isotherms corresponding to $T=90^{\circ}, 80^{\circ}, 70^{\circ}$, and $60^{\circ}$ are shown in Figure 7.

Related to the topic of isotherms is the topic of curves of heat flow. These are the curves along which the heat is flowing inside the plate. To determine these curves, we use Fourier's law of heat conduction, which states that heat flows from hot to cold in the direction in which the temperature difference is the greatest. If along the isotherms the temperature difference is zero, then it should make sense that in the direction perpendicular to the isotherms the temperature difference is the greatest. Hence the curves of heat flow are orthogonal to the isotherms.

So to find the curves of heat flow in a plate, it is enough to find a harmonic conjugate $v(x, y)$ of the steady-state temperature distribution $u(x, y)$, since by Theorem 2 the level curves of $v$ are orthogonal to the level curves of $u$ We illustrate this process with an example.

![](af4f9593-dec7-4bc0-8d78-d25500419ec9-45_477_510_300_76.jpg)
Figure 8 Curves of heat flow in Example 6, along with the isotherms.

## EXAMPLE 6 Curves of heat flow <br> Find the curves of heat flow in Example 3.

Solution The isotherms were found in Example 5 and are given by $u(x, y)=C_{1}$, where $u(x, y)=-\frac{100}{\pi} \operatorname{Arg}(z)+100$. To determine the curves of heat flow, we must find a harmonic conjugate of $u$. By Proposition 3(ii), it is enough to find a harmonic conjugate of $-\frac{100}{\pi} \operatorname{Arg}(z)$. From our knowledge of analytic functions, we see that $f(z)=-\frac{100}{\pi}(\ln |z|+i \operatorname{Arg}(z))=-\frac{100}{\pi} \log z$ is analytic in $\mathbb{C} \backslash(-\infty, 0]$. Hence by Theorem 1, a harmonic conjugate of $-\frac{100}{\pi} \ln |z|$ is $-\frac{100}{\pi} \operatorname{Arg} z$. By Proposition 2, it follows that a harmonic conjugate of $-\frac{\pi 00}{\pi} \operatorname{Arg} z$ is $\frac{{ }^{\pi} 00}{\pi} \ln |z|$. Hence the curves of heat flow are given by

$$
\frac{100}{\pi} \ln |z|=\text { constant } \quad \Leftrightarrow \quad|z|=\text { constant } \quad \Leftrightarrow \quad x^{2}+y^{2}=c^{2} .
$$

Thus the curves of heat flow are arcs of circles centered at the origin. In Figure 8 , we show the isotherms along with the curves of heat flow to illustrate their orthogonality. $\square$

## Conformal Mappings

We conclude our panoramic overview of Dirichlet problems and their solutions by mentioning the method of conformal mappings, which is of wide use in complex analysis. In the past you have certainly used methods to transform a difficult problem to one with a known solution or whose solution is easier to find. For example, some integrals are simplified by using changes of variables, some differential equations are simplified by applying a Laplace transform, and so on. In solving Dirichlet problems, it is sometimes advantageous to map the region under consideration to a simpler region or one on which the transformed problem is easier to solve. This is the idea behind the method of conformal mappings, which we now explain.

Let a Dirichlet problem be given on a region $\Omega$ with boundary $\Gamma$. Suppose that we want to solve this problem by somehow transforming it first to the $w$ plane by means of a mapping $w=f(z)$, where $f$ is analytic in $\Omega$. If $f^{\prime}(z) \neq 0$ for all $z$ in $\Omega$, we call $f$ a conformal mapping of $\Omega$. Conformal mappings have important properties that will be studied in detail in Chapter 6. For example, if $f$ is conformal, then the image of $\Omega, \Omega^{\prime}=f[\Omega]$, is also a region (open, connected set); moreover, if $f$ is one-to-one, then $f$ will map $\Gamma$ onto $\Gamma^{\prime}$, the boundary of $\Omega^{\prime}$. In the examples of this section, these properties can be checked on a case-by-case basis.

In transforming the Dirichlet problem, we need to know what happens to Laplace's equation under our transformation $w=f(z)$ and what happens to the boundary conditions. Because $f$ maps boundary to boundary, the boundary conditions on $\Gamma$ will be transformed into boundary conditions on $\Gamma^{\prime}$ as we will explain shortly. However, the most important feature of this method is stated in the next theorem and tells us that Laplace's equation

## THEOREM 3 INVARIANCE OF LAPLACE'S EQUATION

To understand the meaning of $U \circ f(z)$ where $f$ is complexvalued and $U$ is a function of two variables, write $U \circ f(z)=U(\operatorname{Re} f(z), \operatorname{Im} f(z))$. For example, if $f(z)= e^{z}=e^{x} \cos y+i e^{x} \sin y$ and $U(s, t)=s t$, then $U \circ f(z)= e^{2 x} \cos y \sin y$.

Figure 9 The conformal mapping method. If $f(z)$ is analytic and one-to-one on $\Omega$ and its boundary $\Gamma$, then $\Omega^{\prime}= f[\Omega]$ is a region with boundary $\Gamma^{\prime}=f[\Gamma]$. The boundary function $b(z)$ ( $z$ on $\Gamma$ ) is used to define a boundary function $b \circ f^{-1}(w)$ for all $w$ on $\Gamma$, where $f^{-1}$ is the inverse of $f$.
is invariant under a change of variables using a conformal mapping.
Suppose that $f$ is an analytic mapping of $\Omega$ into $\Omega^{\prime}$ and $U$ is a harmonic function on $\Omega^{\prime}$. Then $U \circ f$ is harmonic in $\Omega$. Thus, if $U$ satisfies $\Delta U=0$ on $\Omega^{\prime}$, then $u=U \circ f$ satisfies $\Delta u=0$ on $\Omega$.

Proof Let $z_{0}$ be a point in $\Omega$ and $w_{0}=f\left(z_{0}\right)$. We will show in Section 3.8 that $U$ has a harmonic conjugate $V$ in a disk around $w_{0}$. Then $U+i V$ is analytic in this disk, and by the composition of analytic functions, $(U+i V) \circ f$ is analytic at $z_{0}$. Hence by Theorem 1, $\operatorname{Re}[(U+i V) \circ f]=\operatorname{Re}[U \circ f+i(V \circ f)]=U \circ f$ is harmonic at $z_{0}$. Since $z_{0}$ was arbitrary, $U \circ f$ is harmonic in $\Omega$. An alternate proof may be given by direct application of the chain rule and Cauchy-Riemann equations.

Now suppose that you want to use a conformal mapping $w=f(z)$ to solve the Dirichlet problem $\Delta u=0$ in $\Omega$ and $u(z)=b(z)$ on the boundary $\Gamma$ of $\Omega$. Suppose also that $f$ is one-to-one on $\Omega$ and its boundary $\Gamma$. Here is how the method works (see Figure 9 as you read through the steps).
![](af4f9593-dec7-4bc0-8d78-d25500419ec9-46_519_1162_1082_766.jpg)

Step 1: Describe clearly the region $\Omega^{\prime}=f[\Omega]$ and its boundary $\Gamma^{\prime}=f[\Gamma]$ in the $w$-plane.
Step 2: Since $f$ is one-to-one, we have an inverse function $f^{-1}$ defined on $\Omega^{\prime}$ and $\Gamma^{\prime}$. For $w$ on $\Gamma^{\prime}, f^{-1}(w)$ is on $\Gamma$ and so we can define the function $b \circ f^{-1}(w)$ for all $w$ on $\Gamma^{\prime}$. This determines the boundary values on $\Gamma^{\prime}$.
Step 3: Set up and solve the Dirichlet problem on $\Omega^{\prime}$ consisting of Laplace's equation $\Delta U(w)=0$ for all $w$ in $\Omega^{\prime}$ and $U(w)=b \circ f^{-1}(w)$ for all $w$ on $\Gamma^{\prime}$. (This is our transformed Dirichlet problem.)
Step 4 Let $u(z)=U \circ f(z)$ for all $z$ in $\Omega$. Then $u(z)$ is a solution of out original Dirichlet problem on $\Omega$. Indeed, by Theorem 3, $u$ is harmonic in $\Omega$. For $z$ on the boundary $\Gamma$, we have $f(z)$ on the boundary $\Gamma^{\prime}$, and using the fact that $U(w)=b \circ f^{-1}(w)$ on $\Gamma^{\prime}$, we obtain for $z$ on $\Gamma, u(z)=U \circ f(z)= b \circ f^{-1}(f(z))=b(z)$. Hence $u$ satisfies the desired boundary condition.

In most examples, Steps 2 and 3 can be done without actually computives $f^{-1}$, as we illustrate in our next example.

![](af4f9593-dec7-4bc0-8d78-d25500419ec9-47_468_498_188_96.jpg)
Figure 10 Dirichlet problem in Example 7.

Figure 11 Mapping the semiinfinite vertical strip onto the upper half-plane. Note the boundary correspondence.

## EXAMPLE 7 Conformal mapping solution of a Dirichlet problem

(a) Solve the Dirichlet problem in the semi-infinite strip $\Omega$ shown in Figure 10.
(b) Discuss the isotherms and lines of heat flow of the solution.

Solution (a) We will transform the given problem on the region $\Omega$ into a problem in the upper half-plane. As we will see momentarily, the transformed problem is easy to solve. We will follow the basic four steps of the solution.
Step 1: Recall from Example 4, Section 1.6, that the mapping $f(z)=\sin z$ takes $\Omega$ in the $z$-plane onto the upper half of the $w$-plane (Figure 11). Moreover, the boundary of $\Omega$ is mapped to the boundary of the upper half-plane as follows. The line segment on the $x$-axis, $\left[0, \frac{\pi}{2}\right]$, and the vertical half-line $y=\frac{\pi}{2}$ are mapped onto $[0, \infty)$, the nonnegative real axis in the $w$-plane. The line segment on the $x$-axis, $\left[-\frac{\pi}{2}, 0\right)$, and the vertical half-line $y=-\frac{\pi}{2}$ are mapped onto $(-\infty, 0)$, the negative real axis in the $w$-plane. (As you can verify in this case, $\frac{d}{d z} \sin z=\cos z$ and since the zeros of $\cos z$ are at the points $\frac{\pi}{2}+k \pi, k$ an integer, we conclude that $f^{\prime}(z) \neq 0$ for all $z$ strictly in $\Omega$. Hence $f$ is a conformal mapping of $\Omega$ onto the upper half-plane. Moreover, using the fact that $\sin z$ is $2 \pi$-periodic, it follows that $\sin z$ is one-to-one on $\Omega$.)
Step 2: Describe the boundary function in the Dirichlet problem in the $w$-plane. The boundary function in the $w$-plane is $b \circ f^{-1}(w)$, where $b(z)$ is the boundary function in the $z$-plane. From Figure 11, we have $b(z)=0$ if $z$ is real and positive or $z=\frac{\pi}{2}+i y$, where $y>0$; and $b(z)=100$ if $z$ is real and negative or $z=-\frac{\pi}{2}+i y$, where $y>0$. With this definition of $b$ and the way the boundary is mapped to the boundary, it becomes clear that the boundary function in the $w$-plane is $b \circ f^{-1}(w)=0$ if $w>0$ and $b \circ f^{-1}(w)=100$ if $w<0$.
Step 3: The transformed Dirichlet problem in the upper half-plane is described by Figure 11 and is given by

$$
\begin{aligned}
& \Delta U(w)=0, w \text { in the upper half-plane, } \\
& U(w)=0, w>0, \quad U(w)=100, w<0
\end{aligned}
$$

![](af4f9593-dec7-4bc0-8d78-d25500419ec9-47_424_1237_1573_689.jpg)

Since the transformed boundary data is constant along rays, we can solve the problem in the $w$-plane as we did in Example 3 by trying for a solution the harmonic function $U(w)=a \operatorname{Arg} w+b$, where $a$ and $b$ are real constants. Using the boundary conditions, we see that $100=a \pi$ or $a=\frac{100}{\pi}$, and $0=b$. Hence $U(w)=\frac{100}{\pi} \operatorname{Arg} w$. Step 4: The solution of the original Dirichlet problem in the $z$-plane is $u(z)= U(f(z))=\frac{100}{\pi} \operatorname{Arg}(\sin z)$. If we want to express our answer in terms of $x$ and $y$, we use the real and imaginary parts of $\sin z((16)$, Section 1.6): $\sin z=\sin x \cosh y+$

![](af4f9593-dec7-4bc0-8d78-d25500419ec9-48_307_553_372_104.jpg)
Figure 12 The inverse cotangent takes its values in $(0, \pi)$.

![](af4f9593-dec7-4bc0-8d78-d25500419ec9-48_609_553_1350_112.jpg)

Figure 13 Isotherms and curves of heat flow in Example 7. Note the orthogonality of the curves.
$i \cos x \sinh y$. It is not convenient to use the inverse tangent formula (14), Section 1.3, to express $\operatorname{Arg}(\sin z)$, because the real part of $\sin z$ takes on positive and negative values. It is more convenient in this case to use the inverse cotangent. We have

$$
\operatorname{Arg}(\sin z)=\cot ^{-1}\left(\frac{\sin x \cosh y}{\cos x \sinh y}\right)=\cot ^{-1}(\tan x \operatorname{coth} y)
$$

where the inverse cotangent takes its values between 0 and $\pi$ (see Figure 12). Hence

$$
u(z)=u(x, y)=\frac{100}{\pi} \cot ^{-1}(\tan x \operatorname{coth} y)
$$

(b) The isotherms are the level curves $u(x, y)=T$, where $0<T<100$. The curves of heat flow are the level curves of a harmonic conjugate $v$ of $u$. To find $v$, it is enough to find a harmonic conjugate $V$ of $U$ and then set $v(z)=V(\sin z)$ (Exercise 34). Since $\operatorname{Arg} w$ is the harmonic conjugate of $\ln |w|$, it follows from Proposition 2 that $-\ln |w|$ is the harmonic conjugate of $\operatorname{Arg} w$. Hence $V(w)= -\ln |w|$ and $v(x, y)=-\ln |\sin z|$. Some isotherms and curves of heat flow are shown in Figure 13.

A few geometric observations can be made. Note that at the top of Figure 13, the isotherms look like vertical lines. This is to be expected, since the lower boundary, being remote, can be ignored, and we may think of the problem as one on a doubly infinite vertical strip, in which the isotherms are vertical lines. Near the origin, the isotherms look like rays, and the curves of heat flow like circles. These are the isotherms and curves of heat flow in a Dirichlet problem with boundary data constant on rays (see Examples 3, 5, and 6). This too is to be expected since near the origin the vertical boundary data have less effect as compared with the boundary data on the $x$-axis. So near the origin, we can ignore the vertical boundary data and consider only the horizontal boundary data, which is constant on rays in this case, and so the isotherms and curves of heat flow are like those in Examples 5 and 6 .

So far we have used our knowledge of analytic functions to solve Dirichlet problems by guessing the solution. Guessing is certainly a legitimate method that you have used in solving differential equations and computing indefinite integrals. Further development of the theory of analytic and harmonic functions will be necessary to tackle more general Dirichlet problems. Topics such as the Poisson integral formula, Fourier series, and conformal mappings are examples of theories and tools that will provide us with systematic ways for solving Dirichlet problems.

Other issues that we need to address concern the uniqueness of the solution of a Dirichlet problem. Consider the problem in Example 3, whose solution is $u(x, y)=-\frac{100}{\pi} \tan ^{-1}\left(\frac{y}{x}\right)+100$. If we add to this solution the harmonic function $\phi(x, y)=x y$, we obtain the harmonic function $\psi(x, y)= u(x, y)+x y$, which solves Laplace's equation. Moreover, because $x y$ vanishes on the boundary of the first quadrant, $\psi(x, y)$ and $u(x, y)$ have the same boundary values. Thus, $\psi$ is another solution of the Dirichlet problem in Example 3. This is quite disturbing since we want to think of the solution ${ }^{25}$
representing a temperature distribution and as such it must be unique. As it turns out, if in addition to the boundary conditions in a Dirichlet problem we add the condition that the solution be bounded (which is effectively a boundary condition at infinity), then the solution will be unique. For example, with this additional boundedness assumption, we can no longer add the function $x y$ to the solution in Example 3 to obtain another solution.

Uniqueness results for the solution of Dirichlet problems will be derived from theoretical properties of analytic and harmonic functions, including results such as the maximum principle. All these topics will be addressed as part of the remainder of this book.

## Exercises 2.5

In Exercises 1-12, determine the set on which the given function is harmonic. You may verify Laplace's equation (1) directly or use Theorem 1.

1. $x^{2}-y^{2}+2 x-y$.
2. $\frac{1}{x^{2}-y^{2}}$.
3. $e^{x} \cos y$.
4. $\frac{y}{x^{2}+y^{2}}$.
5. $\frac{1}{x+y}$.
6. $\sinh x \cos y$.
7. $\cos x \cosh y$.
8. $e^{2 x} \cos (2 y)$.
9. $e^{x^{2}-y^{2}} \cos (2 x y)$.
10. $\ln \left(x^{2}+y^{2}\right)$.
11. $\ln \left((x-1)^{2}+y^{2}\right)$.
12. $\arg _{\frac{\pi}{2}} z$.

In Exercises 13-16, find a harmonic conjugate $v(x, y)$ of the given harmonic function $u(x, y)$ by using the method of Example 2 . Check your answer by verifying the Cauchy-Riemann equations.
13. $x+2 y$.
14. $x^{2}-y^{2}-x y$.
15. $e^{y} \cos x$.
16. $\cos x \sinh y$.
17. Let $n$ be any integer. (a) Show that $u(r, \theta)=r^{n} \cos (n \theta)$ and $v(r, \theta)= r^{n} \sin (n \theta)$ are harmonic on $\mathbb{C}$ if $n \geq 0$ and on $\mathbb{C} \backslash\{0\}$ if $n<0$. (b) Find their respective harmonic conjugates. [Hint: Consider $f(z)=z^{n}$ in polar coordinates.]
18. (a) Prove Proposition 1.
(b) Prove Proposition 3.
19. Show that if $u$ and $u^{2}$ are both harmonic in a region $\Omega$, then $u$ must be constant. [Hint: Plug $u^{2}$ into Laplace's equation and show that $u_{x}=u_{y}=0$.]
20. Show that if $u, v$, and $u^{2}+v^{2}$ are harmonic in a region $\Omega$, then $u$ and $v$ must be constant. [Hint: Plug $u^{2}+v^{2}$ into Laplace's equation and show that $u_{x}=u_{y}=0$ and $v_{x}=v_{y}=0$.]
21. Suppose that $u$ is harmonic and $v$ is a harmonic conjugate of $u$. Show that $u^{2}-v^{2}$ and $u v$ are both harmonic. [Hint: Consider $(u+i v)^{2}$.]
22. Use Exercises 20 and 21 to show that if $f$ is analytic in a region $\Omega$ and $|f|$ is constant in $\Omega$, then $f$ must be constant in $\Omega$. (A different proof was outlined in Exercise 38, Section 2.4.)
23. Translating and dilating a harmonic function. Suppose that $u$ is harmonic. Show that the following functions are also harmonic:
(a) $\quad u(x-\alpha, y-\beta)$, where $\alpha$ and $\beta$ are real numbers;
(b) $u(\alpha x, \alpha y)$, where $\alpha \neq 0$ is a real number.
24. (a) Suppose that $u(x, y)$ is harmonic. Show that $u(x,-y)$ is also harmonic.

![](af4f9593-dec7-4bc0-8d78-d25500419ec9-50_493_558_342_84.jpg)
Figure 14 Dirichlet problem in Exercise 25.

(b) Suppose that $u(x, y)$ is harmonic. Show that $u\left(\frac{x}{x^{2}+y^{2}}, \frac{y}{x^{2}+y^{2}}\right)$ is harmonic.
[Hint: Compose $u$ with the analytic function $\frac{1}{z}$; use Theorem 3 and part (a).]
25. Harmonic functions independent of $y$. (a) Suppose that $u(x, y)$ is a harmonic function whose values depend only on $x$ and not on $y$. Using Laplace's equation, show that $u(x, y)=a x+b$, where $a$ and $b$ are real constants.
(b) Consider the Dirichlet problem in the infinite vertical strip in Figure 14. Because the boundary values do not depend on $y$, it is plausible to try for a solution a harmonic function whose values do not depend on $y$. Solve the problem, using (a).
(c) Determine and plot the isotherms and curves of heat flow.
26. A Dirichlet problem in an infinite vertical strip. (a) Solve the Dirichlet problem in Figure 15.
(b) Determine and plot the isotherms and curves of heat flow.
27. Harmonic functions independent of $r$. (a) Solve the Dirichlet problem in Figure 16. Because the boundary values do not depend on $r$, you should try for a solution a harmonic function whose values do not depend on $r$.
(b) Determine and plot the isotherms and curves of heat flow.

![](af4f9593-dec7-4bc0-8d78-d25500419ec9-50_495_535_1109_852.jpg)
Figure 16 Dirichlet problem in Exercise 27.

![](af4f9593-dec7-4bc0-8d78-d25500419ec9-50_498_503_1097_1592.jpg)
Figure 17 Dirichlet problem in Exercise 28.

28. A Dirichlet problem in a wedge. (a) Solve the Dirichlet problem in Figure 17.
(b) Determine and plot the isotherms and curves of heat flow.
29. Harmonic functions independent of $\theta$. Suppose that $u(r, \theta)$ is a harmonic function, in polar coordinates.
(a) Suppose that $u$ depends only on $r$ and not $\theta$; hence $u(r, \theta)=u(r)$. Using the polar form of the Laplacian (12) in Exercise 47, show that $u(r)$ satisfies the (ordinary) differential equation in $r$

$$
u_{r r}+\frac{1}{r} u_{r}=0,
$$

known as an Euler equation. This is perhaps the simplest second order linear differential equation with nonconstant coefficients. To find its general solution, we
(b) Multiply the Euler equation by the integrating factor $r$ and notice that the need two linearly independent solutions. left side is now exact. Integrate to conclude $r u_{r}=c_{1}$, where $c_{1}$ is the constant of

![](af4f9593-dec7-4bc0-8d78-d25500419ec9-51_461_492_971_97.jpg)
Figure 18 Dirichlet problem in Exercise 30.

![](af4f9593-dec7-4bc0-8d78-d25500419ec9-51_470_496_1775_89.jpg)
Figure 21 Dirichlet problem for Exercise 35.

integration. Integrate again and find the general solution

![](af4f9593-dec7-4bc0-8d78-d25500419ec9-51_457_500_979_802.jpg)
Figure 19 Dirichlet problem in Exercise 31.

$$
u(r)=c_{1} \ln r+c_{2} .
$$

30. Dirichlet problems in annular regions. The annular region $A_{R_{1}, R_{2}}$ in Figure 18 is centered at the origin with inner radius $R_{1}$ and outer radius $R_{2}$. Consider the Dirichlet problem in $A_{R_{1}, R_{2}}$ with constant boundary conditions $u\left(R_{1}, \theta\right)= T_{1}$ and $u\left(R_{2}, \theta\right)=T_{2}$ for all $\theta$. Show that the solution of the problem is

![](af4f9593-dec7-4bc0-8d78-d25500419ec9-51_461_508_981_1511.jpg)
Figure 20 Dirichlet problem in Exercise 32.

$$
u(r, \theta)=u(r)=T_{1}+\left(T_{2}-T_{1}\right) \frac{\ln \left(r / R_{1}\right)}{\ln \left(R_{2} / R_{1}\right)}
$$

[Hint: Since the boundary conditions are independent of $\theta$, you should try a harmonic function independent of $\theta$. According to Exercise 29, try $u(r)=c_{1} \ln r+c_{2}$.] Exercises 31-32 are Dirichlet problems described by the corresponding figures. In each case, (a) solve the Dirichlet problem. (b) Determine the isotherms. (c) Determine the curves of heat flow. (d) Plot the isotherms and curves of heat flow.
33. Nonexistence of a harmonic conjugate. In Example 1(d), we showed that $\ln |z|$ is harmonic in $\mathbb{C} \backslash\{0\}$. We also know that $\ln |z|$ has a harmonic conjugate in $\mathbb{C} \backslash(-\infty, 0]$. In fact, since $\ln |z|$ is the real part of the analytic function $\log _{\alpha} z$, it has a harmonic conjugate in the complex plane minus the ray emanating from the origin at angle $\alpha$. In this exercise, we will show that $\ln |z|$ does not have a harmonic conjugate in $\mathbb{C} \backslash\{0\}$.
(a) Suppose that $\phi(z)$ is a harmonic conjugate of $\ln |z|$ in $\mathbb{C} \backslash\{0\}$. Show that $\phi(z)=\operatorname{Arg}(z)+c$ for all $z$ in $\mathbb{C} \backslash(-\infty, 0]$. [Hint: The functions $\ln |z|+i \phi(z)$ and $\log z$ are analytic in the region $\mathbb{C} \backslash(-\infty, 0]$ and have the same real parts. Use Corollary 1, Section 2.4.]
(b) Argue that, since $\phi(z)$ is harmonic in $\mathbb{C} \backslash\{0\}, \phi(z)$ is continuous on $(-\infty, 0)$. Obtain a contradiction using (a) and the fact that the discontinuities of $\operatorname{Arg} z$ are not removable on the negative $x$-axis (Example 7, Section 2.2).
34. (a) Suppose that $f$ is analytic on $\Omega, U$ is harmonic on $f[\Omega]$, and $u=U \circ f$. Then $u$ is harmonic in $\Omega$ by Theorem 3. Suppose that $V$ is a harmonic conjugate of $U$. Show that $V \circ f$ is a harmonic conjugate of $u$.
(b) Derive the isotherms and curves of heat flow in Example 7.
![](af4f9593-dec7-4bc0-8d78-d25500419ec9-52_489_547_289_83.jpg)

Figure 22 The harmonic measure of an interval is the difference of two translated arguments:

$$
\begin{aligned}
\alpha(z)=\operatorname{Arg} & (z-b) \\
& -\operatorname{Arg}(z-a)
\end{aligned}
$$

![](af4f9593-dec7-4bc0-8d78-d25500419ec9-52_497_553_1152_91.jpg)
Figure 23 Dirichlet problem for Exercise 36.

![](af4f9593-dec7-4bc0-8d78-d25500419ec9-52_514_544_1860_102.jpg)
Figure 24 Dirichlet problem for Exercise 38.

35. Harmonic measure of an interval. A very important Dirichlet problem is described in the upper half-plane with boundary data on the $x$-axis given by

$$
u(x, 0)= \begin{cases}1 & \text { if } a<x<b \\ 0 & \text { otherwise }\end{cases}
$$

where $a<b$ are fixed real numbers (see Figure 21). We will outline a solution of this problem using basic geometry and properties of harmonic functions.
(a) For $z$ in the upper half-plane, let $\alpha(z)$ denote the angle at $z$ subtended by the interval $[a, b]$ (Figure 22). Show that $\alpha(z)=\operatorname{Arg}(z-b)-\operatorname{Arg}(z-a)$. The function $\alpha(z)$ is called the harmonic measure of the interval $(a, b)$. [Hint: We have $\alpha_{1}=\operatorname{Arg}(z-b), \alpha_{2}=\operatorname{Arg}(z-a)$, and $\alpha(z)=\alpha_{1}-\alpha_{2}$ (Figure 22).]
(b) Show that $\alpha(z)$ is harmonic. [Hint: Exercise 23(a).]
(c) Show geometrically that

$$
\lim _{y \downarrow 0} \alpha(x+i y)= \begin{cases}0 & \text { if } x>b, \\ \pi & \text { if } a<x<b, \\ 0 & \text { if } x<a .\end{cases}
$$

(d) Conclude that $u(x, y)=\frac{1}{\pi} \alpha(x+i y)$ is a solution of the Dirichlet problem in Figure 21.
36. (a) Solve the Dirichlet problem in Figure 23.
(b) Show that the isotherm corresponding to the temperature $0<T<100$ consists of the arc in the upper half-plane of the circle with center $\left(0, \cot \frac{\pi T}{100}\right)$ and radius $\left|\csc \frac{\pi T}{100}\right|$. Justify your answer using facts from plane geometry.
(c) What are the curves of heat flow? [Hint: You know a harmonic conjugate of $\operatorname{Arg} z$. Show that if $v$ is a harmonic conjugate of $u$, then a harmonic conjugate of $u(z-a) \pm u(z-b)$ is $v(z-a) \pm v(z-b)$.]
(d) Plot the isotherms and curves of heat flow.
37. Solve the Dirichlet problem in the upper half-plane with boundary data on the $x$-axis given by

$$
u(x, 0)= \begin{cases}T_{1} & \text { if } a<x<b \\ T_{2} & \text { otherwise }\end{cases}
$$

where $a<b$ are fixed real numbers. [Hint: Use Exercise 35 and the fact that constant functions are harmonic.]
38. Project Problem: Harmonic measures of two disjoint intervals. In this exercise, we generalize the result of Exercise 35 by solving the Dirichlet problem in the upper half-plane with boundary data

$$
u(x, 0)= \begin{cases}T_{1} & \text { if } a<x<b \\ T_{2} & \text { if } c<x<d \\ 0 & \text { otherwise }\end{cases}
$$

where $a<b \leq c<d$ (Figure 24).
(a) Show that if $u_{1}$ is a solution of the Dirichlet problem in the upper half-plane with boundary conditions

$$
u_{1}(x, 0)= \begin{cases}T_{1} & \text { if } a<x<b \\ 0 & \text { otherwise }\end{cases}
$$

and $u_{2}$ is a solution of the Dirichlet problem in the upper half-plane with boundary conditions

$$
u_{2}(x, 0)= \begin{cases}T_{2} & \text { if } c<x<d \\ 0 & \text { otherwise }\end{cases}
$$

then the solution of the Dirichlet problem in the upper half-plane with boundary data $u(x, 0)$ is $u(x, y)=u_{1}(x, y)+u_{2}(x, y)$.
(b) Show that $u(x, y)=\frac{T_{1}}{\pi} \alpha_{1}(z)+\frac{T_{2}}{\pi} \alpha_{2}(z)$ where $\alpha_{1}(z)$, respectively, $\alpha_{2}(z)$, is the angle at $z$ subtended by the interval $(a, b)$, respectively, $(c, d)$.
39. (a) Solve the Dirichlet problem in Figure 25.
(b) Plot the isotherms.

![](af4f9593-dec7-4bc0-8d78-d25500419ec9-53_474_503_734_104.jpg)
Figure 25 Dirichlet problem for Exercise 39.

40. Project Problem: Harmonic measures of several disjoint intervals. Generalize the result of Exercise 38 as follows. Suppose that $I_{1}, I_{2}, \ldots, I_{n}$ are disjoint open intervals on the $x$-axis, and $T_{1}, T_{2}, \ldots, T_{n}$ are real numbers. Consider the Dirichlet problem in the upper half-plane with boundary condition

$$
u(x, 0)= \begin{cases}T_{j} & \text { if } x \in I_{j} \\ 0 & \text { otherwise }\end{cases}
$$

Show that the solution is

$$
u(x, y)=\frac{1}{\pi} \sum_{j=1}^{n} T_{j} \alpha_{j}(z)
$$

where $\alpha_{j}(z)$ is the angle at $z$ subtended by the interval $I_{j}$.
41. Project Problem: Approximation of steady-state solutions. Consider the Dirichlet problem in the upper half-plane with boundary values $u(x, 0)= f(x)(-\infty<x<\infty)$, where $f(x)$ is an arbitrary function that represents the temperature of the points on the $x$-axis. Such a temperature distribution will be bounded and piecewise continuous. There is an analytical solution of the Dirichlet problem, given by an integral involving $f(x)$, known as the Poisson integral of $f$ (see Exercise 42). In this exercise, we will show how we can use the result of Exercise 40 to approximate the solution for a given $f(x)$. The approach that we take has some merit, since it can be used to obtain approximate numerical values for the steady-state temperature. Moreover, we will use it in Exercise 42 to justify the Poisson integral formula. The rigorous derivation of this formula will be given in a later chapter.

To be able to compare our numerical approximation with the exact solution, let us take $f(x)=\frac{1}{1+x^{2}},-\infty<x<\infty$. In this case, using properties of the Poisson integral, we will show in a later chapter that the solution is

$$
u(x, y)=\frac{1+y}{x^{2}+(1+y)^{2}}
$$

(a) Verify that $u$ is indeed harmonic in the upper half-plane and that it equals $f(x)=\frac{1}{1+x^{2}}$ on the $x$-axis.
(b) We now pretend that we do not know the exact solution and proceed to find an approximate solution. The idea is to approximate $f(x)$ by a function that takes on constant values on disjoint intervals. Take the interval ( $-5,5$ ) and subdivide it
into 40 smaller intervals of equal length, $\left(x_{j}, x_{j+1}\right), j=1,2, \ldots, 40$. Approximate $f$ on ( $x_{j}, x_{j+1}$ ) by $f\left(x_{j}\right)$, and by 0 outside the interval ( $-5,5$ ). Thus the boundary values are now replaced by

$$
u(x, 0)= \begin{cases}\frac{1}{1+x_{j}^{2}} & \text { if } x_{j}<x<x_{j+1} \\ 0 & \text { otherwise }\end{cases}
$$

Show that the solution is

$$
u(x, y)=\frac{1}{\pi} \sum_{j=1}^{40} \frac{1}{1+x_{j}^{2}} \alpha_{j}(z)
$$

where $\alpha_{j}(z)$ is the angle at $z$ subtended by the interval $\left(x_{j}, x_{j+1}\right)$.
(c) With the help of a computer, evaluate your approximate solution at various points, $z_{0}=x_{0}+i y_{0}$, in the upper half-plane and compare with the exact solution (10).
42. Project Problem: Justifying the Poisson integral formula. Consider the Dirichlet problem in the upper half-plane with boundary values $u(x, 0)=f(x)$, $-\infty<x<\infty$. One of the major results that we will derive in this book gives the solution as

$$
u(s, y)=\frac{y}{\pi} \int_{-\infty}^{\infty} \frac{f(x)}{(s-x)^{2}+y^{2}} d x, \quad-\infty<s<\infty, y>0
$$

This is known as the Poisson integral formula or the Poisson integral of $f$. Our goal in this exercise is to motivate this formula by sketching a proof using the numerical scheme of Exercise 41.
(a) Based on the approach in Exercise 41, explain how you would derive the approximate solution

$$
u_{\mathrm{app}}(s, y)=\frac{1}{\pi} \sum_{j=1}^{n} f\left(x_{j}\right) \alpha_{j}(s, y)
$$

where $x_{j}$ are equally spaced points on the $x$-axis and $\alpha_{j}(s, y)$ is the angle at $z= s+i y$ subtended by the interval ( $x_{j}, x_{j+1}$ ).
(b) Use the result of Exercise 35(a) to write

$$
u_{\mathrm{app}}(s, y)=\frac{1}{\pi} \sum_{j=1}^{n} f\left(x_{j}\right)\left(\operatorname{Arg}\left(z-x_{j+1}\right)-\operatorname{Arg}\left(z-x_{j}\right)\right)
$$

where $z=s+i y$.
(c) Use the mean value theorem to show that there exists a $\xi_{j}$ in the interval $\left(x_{j}, x_{j+1}\right)$ such that $\operatorname{Arg}\left(z-x_{j+1}\right)-\operatorname{Arg}\left(z-x_{j}\right)=\frac{y}{\left(s-\xi_{j}\right)^{2}+y^{2}} \Delta x$, where $\Delta x= x_{j+1}-x_{j}$.
(d) Thus the approximate solution

$$
u_{\mathrm{app}}(s, y)=\frac{y}{\pi} \sum_{j=1}^{n} \frac{f\left(x_{j}\right)}{\left(s-\xi_{j}\right)^{2}+y^{2}} \Delta x
$$

[Hints: In Exercise 43, use the conformal mapping $f(z)= \sin z$.
In Exercise 44, use the conformal mapping $f(z)=z^{2}$. Solve the transformed problem by using Exercise 36.]
[Hints: In Exercise 45, use the conformal mapping $f(z)= \sin z$, then the result of Exercise 36.
In Exercise 46, use the conformal mapping $f(z)=z^{4}$, then the result of Exercise 36.]

Let $\Delta x \rightarrow 0$ and explain why $u_{\mathrm{app}}(s, y)$ should approach the Poisson integral (11). [Hint: Interpret $u_{\mathrm{app}}(s, y)$ as a Riemann sum that approximates the Poisson integral (11).]

What we have done in Exercise 42 is not exactly a proof of the Poisson integral formula, since Riemann sums are defined for functions on finite intervals and we have used them on the interval $(-\infty, \infty)$. However, if we know that $f(x)$ is continuous and equal to zero outside an interval $[a, b]$ (no matter how large the interval is), then the preceding proof works, giving you a simple proof of an important result in applied mathematics for the class of continuous functions vanishing outside a bounded interval. Often in analysis, knowing that a result is true for this class of continuous functions is a good indication that the result is also true for a larger class of functions. In particular, to extend the Poisson integral formula to a larger class of functions $f(x)$ satisfying some general integrability conditions, we use standard techniques from analysis to approximate $f(x)$ by continuous functions that vanish outside a bounded interval, and then use this approximation to establish the Poisson integral formula for $f$.

Project Problems: Conformal mapping method. Exercises 43-46 are Dirichlet problems described by the corresponding figures. In each case, (a) solve the problem by following the four steps, as we did in Example 7.
(b) Determine and plot the isotherms.

![](af4f9593-dec7-4bc0-8d78-d25500419ec9-55_491_517_1272_690.jpg)
Figure 26 Dirichlet problem in Exercise 43.

![](af4f9593-dec7-4bc0-8d78-d25500419ec9-55_508_520_1892_680.jpg)
Figure 28 Dirichlet problem in Exercise 45.

![](af4f9593-dec7-4bc0-8d78-d25500419ec9-55_495_516_1272_1280.jpg)
Figure 27 Dirichlet problem in Exercise 44.

![](af4f9593-dec7-4bc0-8d78-d25500419ec9-55_508_516_1890_1278.jpg)
Figure 29 Dirichlet problem in Exercise 46.

47. Project Problem: Laplacian in polar coordinates. In this exercise, you are asked to derive the polar form of the Laplacian

$$
\Delta u=\frac{\partial^{2} u}{\partial r^{2}}+\frac{1}{r} \frac{\partial u}{\partial r}+\frac{1}{r^{2}} \frac{\partial^{2} u}{\partial \theta^{2}}
$$

The derivation is straightforward but a little tedious. To organize your approach, follow the outlined steps.
(a) Recall the relationship between rectangular and polar coordinates

$$
x=r \cos \theta, \quad y=r \sin \theta, \quad r^{2}=x^{2}+y^{2}, \quad \tan \theta=\frac{y}{x}
$$

Differentiate $r^{2}=x^{2}+y^{2}$ with respect to $x$ once, then a second time, and obtain

$$
\frac{\partial r}{\partial x}=\frac{x}{r}, \quad \frac{\partial^{2} r}{\partial x^{2}}=\frac{y^{2}}{r^{3}}
$$

(b) Differentiate $\tan \theta=\frac{y}{x}$ with respect to $x$ once, then a second time, and get

$$
\frac{\partial \theta}{\partial x}=-\frac{y}{r^{2}}, \quad \frac{\partial^{2} \theta}{\partial x^{2}}=\frac{2 x y}{r^{4}}
$$

(c) In a similar way, differentiate with respect to $y$ and obtain

$$
\frac{\partial r}{\partial y}=\frac{y}{r}, \quad \frac{\partial^{2} r}{\partial y^{2}}=\frac{x^{2}}{r^{3}}, \quad \frac{\partial \theta}{\partial y}=\frac{x}{r^{2}}, \quad \frac{\partial^{2} \theta}{\partial y^{2}}=-\frac{2 x y}{r^{4}}
$$

(d) From the previous identities, derive

$$
\frac{\partial^{2} \theta}{\partial x^{2}}+\frac{\partial^{2} \theta}{\partial y^{2}}=0 \quad \text { and } \quad \frac{\partial \theta}{\partial x} \frac{\partial r}{\partial x}+\frac{\partial \theta}{\partial y} \frac{\partial r}{\partial y}=0
$$

(What does the first equation say about the function $\theta(x, y) ?$ )
(e) Use the chain rule in two dimensions ((13), Section 2.6) to derive

$$
\frac{\partial^{2} u}{\partial x^{2}}=\frac{\partial^{2} u}{\partial r^{2}}\left(\frac{\partial r}{\partial x}\right)^{2}+2 \frac{\partial^{2} u}{\partial \theta \partial r} \frac{\partial r}{\partial x} \frac{\partial \theta}{\partial x}+\frac{\partial u}{\partial r} \frac{\partial^{2} r}{\partial x^{2}}+\frac{\partial^{2} u}{\partial \theta^{2}}\left(\frac{\partial \theta}{\partial x}\right)^{2}+\frac{\partial u}{\partial \theta} \frac{\partial^{2} \theta}{\partial x^{2}}
$$

Change $x$ to $y$ and obtain

$$
\frac{\partial^{2} u}{\partial y^{2}}=\frac{\partial^{2} u}{\partial r^{2}}\left(\frac{\partial r}{\partial y}\right)^{2}+2 \frac{\partial^{2} u}{\partial \theta \partial r} \frac{\partial r}{\partial y} \frac{\partial \theta}{\partial y}+\frac{\partial u}{\partial r} \frac{\partial^{2} r}{\partial y^{2}}+\frac{\partial^{2} u}{\partial \theta^{2}}\left(\frac{\partial \theta}{\partial y}\right)^{2}+\frac{\partial u}{\partial \theta} \frac{\partial^{2} \theta}{\partial y^{2}}
$$

(f) Add $\frac{\partial^{2} u}{\partial x^{2}}$ and $\frac{\partial^{2} u}{\partial y^{2}}$ and simplify with the help of (d) to derive (12).
48. (a) Use (12) to give a direct proof of the result of Exercise 17(a).
(b) Use (12) to give a direct proof that $\log |z|$ is harmonic for all $z \neq 0$.
49. Show that if $u$ is harmonic and independent of $r$, then $u_{\theta \theta}=0$. Conclude that $u=a \theta+b$; equivalently, $u=a \arg _{\alpha} z+b$, where $\arg _{\alpha} z$ is a branch of the argument.

### 2.6 Differentiation of Functions of Several Variables

Our goal in this section is to fulfill our promise of completing the proof of the Cauchy-Riemann theorem, which we stated in Section 2.4. The material that is required for the proof is interesting in its own right. It deals with the concept of differentiation for functions of several variables. We will also apply it to give simple proofs of the chain rule and the mean value theorem in two dimensions.

As a motivation, let us begin by reviewing a geometric interpretation of the derivative of a real-valued function of one variable, $\phi(x)$. When we say that $\phi^{\prime}\left(x_{0}\right)$ exists, we mean that the limit $\lim _{x \rightarrow x_{0}} \frac{\phi(x)-\phi\left(x_{0}\right)}{x-x_{0}}$ exists and equals a finite number $\phi^{\prime}\left(x_{0}\right)$. If we set

$$
r(x)=\phi^{\prime}\left(x_{0}\right)-\frac{\phi(x)-\phi\left(x_{0}\right)}{x-x_{0}}
$$

then $\lim _{x \rightarrow x_{0}} r(x)=0$. Solving for $\phi(x)$, we obtain

$$
\phi(x)=\phi\left(x_{0}\right)+\phi^{\prime}\left(x_{0}\right)\left(x-x_{0}\right)+r(x)\left(x-x_{0}\right) .
$$

![](af4f9593-dec7-4bc0-8d78-d25500419ec9-57_461_497_1149_109.jpg)
Figure 1 Approximation of a differentiable function by the tangent line.

## DEFINITION 1 DIFFERENTIABILITY OF REAL-VALUED FUNCTIONS OF TWO VARIABLES

Let $\epsilon(x)=r(x) \frac{x-x_{0}}{\left|x-x_{0}\right|}$, then, because $\frac{x-x_{0}}{\left|x-x_{0}\right|}= \pm 1$ and $r(x) \rightarrow 0$ as $x \rightarrow x_{0}$, it follows that $\epsilon(x) \rightarrow 0$ as $x \rightarrow x_{0}$, and we have

$$
\phi(x)=\overbrace{\phi\left(x_{0}\right)+\phi^{\prime}\left(x_{0}\right)\left(x-x_{0}\right)}^{\text {tangent line at } x_{0}}+\epsilon(x)\left|x-x_{0}\right| .
$$

This expresses the well-known geometric fact that, near a point $x=x_{0}$ where the function $\phi(x)$ is differentiable with derivative $\phi^{\prime}\left(x_{0}\right)$, the tangent line approximates the graph of the function with an error that tends to 0 faster than $\left|x-x_{0}\right|$ (Figure 1).

With (1) in mind, we introduce the notion of differentiability for realvalued functions of two variables. To simplify the notation, we will sometimes denote a point $(x, y)$ by the complex number $z$.

We call a real-valued function $u(x, y)$ differentiable at $z_{0}=\left(x_{0}, y_{0}\right)$ if it can be written in the form

$$
u(z)=u\left(z_{0}\right)+A\left(x-x_{0}\right)+B\left(y-y_{0}\right)+\epsilon(z)\left|z-z_{0}\right|
$$

where $A$ and $B$ are (real) constants and $\epsilon(z) \rightarrow 0$ as $z \rightarrow z_{0}$.
In proofs, we will need to know limits such as
(3) $\lim _{z \rightarrow z_{0}} \epsilon(z) \frac{\left|z-z_{0}\right|}{z-z_{0}}=0, \quad \lim _{z \rightarrow z_{0}} \epsilon(z) \frac{\left|x-x_{0}\right|}{x-x_{0}}=0, \quad \lim _{z \rightarrow z_{0}} \epsilon(z) \frac{x-x_{0}}{\left|z-z_{0}\right|}=0$.

## THEOREM 1

![](af4f9593-dec7-4bc0-8d78-d25500419ec9-58_426_543_1783_113.jpg)
Figure 2 A discontinuous function with partial derivatives at $(0,0)$. The function is not differentiable at $(0,0)$.

These are all of the form $\epsilon(z)$ times a bounded function, and hence by the squeeze theorem they tend to zero as $z \rightarrow z_{0}$, because $\epsilon(z)$ tends to zero. For example,

$$
\left|\epsilon(z) \frac{x-x_{0}}{\left|z-z_{0}\right|}\right|=|\epsilon(z)| \overbrace{\frac{\left|x-x_{0}\right|}{\left|z-z_{0}\right|}}^{\leq 1} \leq|\epsilon(z)|
$$

where the inequality $\frac{\left|x-x_{0}\right|}{\left|z-z_{0}\right|}=\frac{\left|\operatorname{Re}\left(z-z_{0}\right)\right|}{\left|z-z_{0}\right|} \leq 1$ follows from (14), Section 1.2.
Our first result states that a differentiable function is continuous and has partial derivatives.
Suppose $u(x, y)$ is differentiable at $z_{0}=x_{0}+i y_{0}$, so that (2) holds. Then (i) $u(x, y)$ is continuous at $z_{0}$; and
(ii) $u_{x}, u_{y}$ exist at $z_{0}$ and $u_{x}\left(z_{0}\right)=A, u_{y}\left(z_{0}\right)=B$.

Proof (i) Taking limits on both sides of (2), we obtain

$$
\lim _{z \rightarrow z_{0}} u(z)=\lim _{z \rightarrow z_{0}}(u\left(z_{0}\right)+\overbrace{A\left(x-x_{0}\right)}^{\rightarrow 0}+\overbrace{B\left(y-y_{0}\right)}^{\rightarrow 0}+\overbrace{\epsilon(z)\left|z-z_{0}\right|}^{\rightarrow 0})=u\left(z_{0}\right) .
$$

Hence $u(x, y)$ is continuous at $z_{0}$. For (ii), we will only prove that $u_{x}\left(x_{0}, y_{0}\right)=A$, the second part being similar. To compute $u_{x}\left(x_{0}, y_{0}\right)$, we fix $y=y_{0}$ and take the derivative of $u\left(x, y_{0}\right)$ with respect to $x$. From (2) we have

$$
\begin{aligned}
u_{x}\left(x_{0}, y_{0}\right) & =\lim _{x \rightarrow x_{0}} \frac{u\left(x, y_{0}\right)-u\left(x_{0}, y_{0}\right)}{x-x_{0}} \\
& =A+\lim _{x \rightarrow x_{0}} \epsilon\left(x, y_{0}\right) \frac{\left|x-x_{0}\right|}{x-x_{0}}=A
\end{aligned}
$$

since $\lim _{x \rightarrow x_{0}} \epsilon\left(x, y_{0}\right) \frac{\left|x-x_{0}\right|}{x-x_{0}}=0$ as a consequence of (3).
The converse of part (ii) of Theorem 1 is not true. A function of two variables may have partial derivatives and yet fail to be differentiable at a point. In fact, the function may not even be continuous at that point. As an illustration, consider

$$
u(x, y)= \begin{cases}\frac{x y}{x^{2}+y^{2}} & (x, y) \neq(0,0) \\ 0 & (x, y)=(0,0)\end{cases}
$$

It is a good exercise to check that $u_{x}(0,0)=0$ and $u_{y}(0,0)=0$, but $u$ is not continuous at $(0,0)$. Hence by Theorem 1(i), $u$ is not differentiable at $(0,0)$. The graph of $u$ is shown in Figure 2.

THEOREM 2 SUFFICIENT CONDITIONS FOR DIFFERENTIABILITY

![](af4f9593-dec7-4bc0-8d78-d25500419ec9-59_465_484_1527_122.jpg)
Figure 3 In the expression

$u(x, y)-u\left(x, y_{0}\right)$, think of $x$ as fixed, and apply the mean value theorem in the second variable.

To obtain differentiability at a point, more is needed than the existence of the partial derivatives. We have the following interesting result.

Let $u$ be a real-valued function defined on a neighborhood of $z_{0}$. If
(i) $u_{x}\left(z_{0}\right)$ and $u_{y}\left(z_{0}\right)$ exist, and
(ii) either $u_{x}(z)$ or $u_{y}(z)$ is continuous at $z_{0}$,
then $u$ is differentiable at $z_{0}$, and (2) holds with $A=u_{x}\left(x_{0}, y_{0}\right), B= u_{y}\left(x_{0}, y_{0}\right)$.

Proof By reversing the roles of $x$ and $y$, it is enough to prove either one of the cases in (ii). Let us take the case where $u_{y}(z)$ is continuous at $z_{0}$. We have

$$
u(z)-u\left(z_{0}\right)=\left[u\left(x, y_{0}\right)-u\left(x_{0}, y_{0}\right)\right]+\left[u(x, y)-u\left(x, y_{0}\right)\right]
$$

For fixed $y_{0}$, we think of $u\left(x, y_{0}\right)$ as a function of $x$ alone. Since this function (of one variable) has a derivative $u_{x}\left(x, y_{0}\right)$, it is differentiable and we can write

$$
u\left(x, y_{0}\right)-u\left(x_{0}, y_{0}\right)=u_{x}\left(x_{0}, y_{0}\right)\left(x-x_{0}\right)+\epsilon_{1}(x)\left(x-x_{0}\right),
$$

where $\epsilon_{1}(x) \rightarrow 0$ as $x \rightarrow x_{0}$. Now for fixed $x$, we think of $u(x, y)$ as a function of $y$ alone, with derivative $u_{y}(x, y)$. Applying the mean value theorem from singlevariable calculus, we obtain

$$
u(x, y)-u\left(x, y_{0}\right)=u_{y}\left(x, y_{1}\right)\left(y-y_{0}\right),
$$

where $y_{1}$ lies between $y_{0}$ and $y$ (Figure 3). Substituting (6) and (7) into (5), we get

$$
u(z)-u\left(z_{0}\right)=\left[u_{x}\left(x_{0}, y_{0}\right)+\epsilon_{1}(x)\right]\left(x-x_{0}\right)+u_{y}\left(x, y_{1}\right)\left(y-y_{0}\right),
$$

where $y_{1}$ lies between $y$ and $y_{0}$. As $z \rightarrow z_{0}, y$ tends to $y_{0}$ and hence $y_{1} \rightarrow y_{0}$, and so $u_{y}\left(x, y_{1}\right) \rightarrow u_{y}\left(x_{0}, y_{0}\right)$, by the continuity of $u_{y}$ at ( $x_{0}, y_{0}$ ). That is, $\lim _{z \rightarrow z_{0}} u_{y}\left(x, y_{1}\right)=u_{y}\left(x_{0}, y_{0}\right)$; equivalently,

$$
u_{y}\left(x, y_{1}\right)=u_{y}\left(x_{0}, y_{0}\right)+\epsilon_{2}(z), \quad \epsilon_{2}(z) \rightarrow 0 \text { as } z \rightarrow z_{0} .
$$

Putting this in (7) and rearranging,

$$
\begin{aligned}
u(z)-u\left(z_{0}\right) & =\left[u_{x}\left(x_{0}, y_{0}\right)+\epsilon_{1}(x)\right]\left(x-x_{0}\right)+\left[u_{y}\left(x_{0}, y_{0}\right)+\epsilon_{2}(z)\right]\left(y-y_{0}\right) \\
& =u_{x}\left(z_{0}\right)\left(x-x_{0}\right)+u_{y}\left(z_{0}\right)\left(y-y_{0}\right)+\epsilon_{1}(x)\left(x-x_{0}\right)+\epsilon_{2}(z)\left(y-y_{0}\right) \\
& =u_{x}\left(z_{0}\right)\left(x-x_{0}\right)+u_{y}\left(z_{0}\right)\left(y-y_{0}\right)+\epsilon(z)\left|z-z_{0}\right|
\end{aligned}
$$

where

$$
\epsilon(z)=\epsilon_{1}(x) \frac{\left(x-x_{0}\right)}{\left|z-z_{0}\right|}+\epsilon_{2}(z) \frac{\left(y-y_{0}\right)}{\left|z-z_{0}\right|}
$$

Since $\frac{\left(x-x_{0}\right)}{\left|z-z_{0}\right|}$ and $\frac{\left(y-y_{0}\right)}{\left|z-z_{0}\right|}$ are bounded in absolute value (see $(3), \epsilon(z) \rightarrow 0$ as $z \rightarrow z_{0}$, and the differentiability of $u(x, y)$ at $z_{0}$ follows from (10). Comparing (10) with (2), we identify $A=u_{x}\left(x_{0}, y_{0}\right)$ and $B=u_{y}\left(x_{0}, y_{0}\right)$.

We are now in a position to complete the proof of the Cauchy-Riemann equations theorem.

## THEOREM 3

## THEOREM 4 THE CHAIN RULE

Let $f(z)=u(x, y)+i v(x, y)$ be a complex-valued function, defined in an open set $S$. If $u_{x}, u_{y}, v_{x}$, and $v_{y}$ are continuous and satisfy the CauchyRiemann equations in $S$, then $f(z)$ is analytic on $S$.
Proof Let $z_{0}$ be any point in $S$. By Theorem 2, $u$ and $v$ are differentiable at $z_{0}$. Using (2), we have

$$
\begin{aligned}
& u(z)=u\left(z_{0}\right)+u_{x}\left(z_{0}\right)\left(x-x_{0}\right)+u_{y}\left(z_{0}\right)\left(y-y_{0}\right)+\epsilon_{1}(z)\left|z-z_{0}\right| \\
& v(z)=v\left(z_{0}\right)+v_{x}\left(z_{0}\right)\left(x-x_{0}\right)+v_{y}\left(z_{0}\right)\left(y-y_{0}\right)+\epsilon_{2}(z)\left|z-z_{0}\right|
\end{aligned}
$$

where $\epsilon_{1}(z), \epsilon_{2}(z) \rightarrow 0$ as $z \rightarrow z_{0}$. Hence by the Cauchy-Riemann equations,

$$
\begin{aligned}
& u(z)=u\left(z_{0}\right)+u_{x}\left(z_{0}\right)\left(x-x_{0}\right)-v_{x}\left(z_{0}\right)\left(y-y_{0}\right)+\epsilon_{1}(z)\left|z-z_{0}\right| \\
& v(z)=v\left(z_{0}\right)+v_{x}\left(z_{0}\right)\left(x-x_{0}\right)+u_{x}\left(z_{0}\right)\left(y-y_{0}\right)+\epsilon_{2}(z)\left|z-z_{0}\right|
\end{aligned}
$$

Consequently,

$$
\begin{aligned}
f(z)= & u(z)+i v(z) \\
= & u\left(z_{0}\right)+i v\left(z_{0}\right)+u_{x}\left(z_{0}\right)\left(x-x_{0}\right)-v_{x}\left(z_{0}\right)\left(y-y_{0}\right)+\epsilon_{1}(z)\left|z-z_{0}\right| \\
& \quad+i v_{x}\left(z_{0}\right)\left(x-x_{0}\right)+i u_{x}\left(z_{0}\right)\left(y-y_{0}\right)+i \epsilon_{2}(z)\left|z-z_{0}\right| \\
= & f\left(z_{0}\right)+\left(u_{x}\left(z_{0}\right)+i v_{x}\left(z_{0}\right)\right)\left[\left(x-x_{0}\right)+i\left(y-y_{0}\right)\right] \\
& \quad+\left(\epsilon_{1}(z)+i \epsilon_{2}(z)\right)\left|z-z_{0}\right| \\
= & f\left(z_{0}\right)+\left(u_{x}\left(z_{0}\right)+i v_{x}\left(z_{0}\right)\right)\left(z-z_{0}\right)+\epsilon(z)\left(z-z_{0}\right)
\end{aligned}
$$

where $\epsilon(z)=\left(\epsilon_{1}(z)+i \epsilon_{2}(z)\right) \frac{\left|z-z_{0}\right|}{z-z_{0}}$. Since $\left(\epsilon_{1}(z)+i \epsilon_{2}(z)\right) \rightarrow 0$ as $z \rightarrow z_{0}$ and $\frac{\left|z-z_{0}\right|}{z-z_{0}}$ is bounded, it follows that $\epsilon(z) \rightarrow 0$ as $z \rightarrow z_{0}$, showing that $f$ is differentiable at $z_{0}$ in the sense of Theorem 5, Section 2.3. Moreover, it follows from that theorem that $f^{\prime}\left(z_{0}\right)=u_{x}\left(z_{0}\right)+i v_{x}\left(z_{0}\right)$. Since $z_{0}$ is arbitrary in $S$, we have $f^{\prime}(z)=u_{x}(z)+ i v_{x}(z)$ for all $z$ in $S$. Also, by Theorem 4(iv), Section 2.2, $f^{\prime}(z)$ is continuous because $u_{x}$ and $v_{x}$ are continuous. Thus $f$ is analytic on $S$.

## Chain Rule and Mean Value Theorems

We can use Definition 1 and basic properties of differentiability to give simple proofs of the chain rule and the mean value theorem in two dimensions. These fundamental results were already used in this chapter and will be used again.
Suppose that $u(x, y)$ is a differentiable function of $(x, y)$ in an open set $S$, where $x=x(t)$ and $y=y(t)$ are both differentiable functions of $t$. Then the function $U(t)=u(x(t), y(t))$ is a differentiable function of $t$ and

$$
\frac{d U}{d t}=\frac{\partial u}{\partial x} \frac{d x}{d t}+\frac{\partial u}{\partial y} \frac{d y}{d t}
$$

In particular, if the partial derivatives of $u$ are continuous, then by Theorem $2, u$ is differentiable and the chain rule (11) holds.
Proof Here again, we will use the notation $z=(x, y)$. For $z_{0}=\left(x\left(t_{0}\right), y\left(t_{0}\right)\right)$ in $S$, by Definition 1 and Theorem 1(ii), we have

$$
u(z)-u\left(z_{0}\right)=u_{x}\left(z_{0}\right)\left(x-x_{0}\right)+u_{y}\left(z_{0}\right)\left(y-y_{0}\right)+\epsilon(z)\left|z-z_{0}\right|
$$

and so

$$
\begin{aligned}
& \frac{u(x(t), y(t))-u\left(x\left(t_{0}\right), y\left(t_{0}\right)\right)}{t-t_{0}} \\
& \quad=u_{x}\left(z_{0}\right) \frac{x(t)-x\left(t_{0}\right)}{t-t_{0}}+u_{y}\left(z_{0}\right) \frac{y(t)-y\left(t_{0}\right)}{t-t_{0}}+\epsilon(z) \frac{\left|z-z_{0}\right|}{t-t_{0}}
\end{aligned}
$$

As $t \rightarrow t_{0}, \frac{x(t)-x\left(t_{0}\right)}{t-t_{0}} \rightarrow \frac{d x}{d t}\left(t_{0}\right)$ and $\frac{y(t)-y\left(t_{0}\right)}{t-t_{0}} \rightarrow \frac{d y}{d t}\left(t_{0}\right)$, and hence (11) will follow from (12) once we prove that $\lim _{t \rightarrow t_{0}} \epsilon(z) \frac{\left|z-z_{0}\right|}{t-t_{0}}=0$. As $t \rightarrow t_{0}, z \rightarrow z_{0}$ and hence $\epsilon(z) \rightarrow 0$. So it suffices to show that $\frac{\left|z-z_{0}\right|}{t-t_{0}}$ is bounded in a neighborhood of $t_{0}$. We have

$$
\left|\frac{\left|z-z_{0}\right|}{t-t_{0}}\right|=\left|\frac{x-x_{0}}{t-t_{0}}+i \frac{y-y_{0}}{t-t_{0}}\right| \rightarrow\left|\frac{d x}{d t}\left(t_{0}\right)+i \frac{d y}{d t}\left(t_{0}\right)\right|
$$

and since this function has a limit, it is bounded in a neighborhood of $t_{0}$.
There is also a version of the chain rule in the situation where $x$ and $y$ are differentiable functions of two variables, $s$ and $t$. In that case, we set $U(s, t)=u(x(s, t), y(s, t))$, and then

$$
\begin{aligned}
& \frac{\partial U}{\partial s}=\frac{\partial u}{\partial x} \frac{\partial x}{\partial s}+\frac{\partial u}{\partial y} \frac{\partial y}{\partial s} \\
& \frac{\partial U}{\partial t}=\frac{\partial u}{\partial x} \frac{\partial x}{\partial t}+\frac{\partial u}{\partial y} \frac{\partial y}{\partial t}
\end{aligned}
$$

The first formula follows by applying (11) to $U(s, t)$ while keeping $t$ fixed, and the second follows by applying (11) while keeping $s$ fixed.

We conclude this section with the mean value theorem in two dimensions.

THEOREM 5 THE MEAN VALUE THEOREM IN TWO DIMENSIONS

Suppose $u(x, y)$ is a differentiable real-valued function of $(x, y)$ in an open set $S$. Suppose that the line segment $\left[z_{1}, z_{2}\right]$ joining $z_{1}=\left(x_{1}, y_{1}\right)$ to $z_{2}=$ ( $x_{2}, y_{2}$ ) lies entirely in $S$. Then there exists a point $\zeta$ on $\left[z_{1}, z_{2}\right]$ (see Figure 4) such that

$$
u\left(z_{2}\right)-u\left(z_{1}\right)=u_{x}(\zeta)\left(x_{2}-x_{1}\right)+u_{y}(\zeta)\left(y_{2}-y_{1}\right)
$$

Proof Parametrize the line segment $\left[z_{1}, z_{2}\right]$ by $x(t)=x_{1}+t\left(x_{2}-x_{1}\right), y(t)= y_{1}+t\left(y_{2}-y_{1}\right), 0 \leq t \leq 1$. We have $\frac{d x}{d t}=x_{2}-x_{1}$ and $\frac{d y}{d t}=y_{2}-y_{1}$. Form the

![](af4f9593-dec7-4bc0-8d78-d25500419ec9-62_500_557_272_99.jpg)
Figure 4 Mean value theorem in two dimensions.

function $U(t)=u(x(t), y(t))$ for $0 \leq t \leq 1$. We have $U(0)=u\left(z_{1}\right), U(1)=u\left(z_{2}\right)$, and by Theorem 4,

$$
\begin{aligned}
\frac{d U}{d t} & =\frac{\partial u}{\partial x} \frac{d x}{d t}+\frac{\partial u}{\partial y} \frac{d y}{d t} \\
& =\frac{\partial u}{\partial x}\left(x_{2}-x_{1}\right)+\frac{\partial u}{\partial y}\left(y_{2}-y_{1}\right)
\end{aligned}
$$

Applying the mean value theorem in one variable to $U(t)$, there is a $t_{0}$ in $(0,1)$ such that $U(1)-U(0)=\frac{d U}{d t}\left(t_{0}\right)(1-0)$. Hence

$$
u\left(z_{2}\right)-u\left(z_{1}\right)=\frac{\partial u}{\partial x}\left(x\left(t_{0}\right), y\left(t_{0}\right)\right)\left(x_{2}-x_{1}\right)+\frac{\partial u}{\partial y}\left(x\left(t_{0}\right), y\left(t_{0}\right)\right)\left(y_{2}-y_{1}\right)
$$

and so (15) follows with $\zeta=\left(x\left(t_{0}\right), y\left(t_{0}\right)\right)$.

## Exercises 2.6

1. Show that the partial derivatives $u_{x}$ and $u_{y}$ of the function given by (4) exist for all $(x, y)$ but that the function is not continuous at $(0,0)$.
2. The function $\phi(x)=x^{2}$ is differentiable at $x_{0}=1$. Find the function $\epsilon(x)$ such that

$$
\phi(x)=\phi(1)+\phi^{\prime}(1)(x-1)+\epsilon(x)|x-1|
$$

and verify directly that $\epsilon \rightarrow 0$ as $x \rightarrow 1$.
3. Show directly from Definition 1 that any linear function $u(x, y)=A x+B y+C$ is differentiable.
4. Prove that if $\epsilon(z) \rightarrow 0$ as $z \rightarrow z_{0}$, then (a) $\epsilon(z) \frac{x-x_{0}}{\left|x-x_{0}\right|} \rightarrow 0$ as $z \rightarrow z_{0}$, and (b) $\epsilon(z) \frac{z-z_{0}}{\left|z-z_{0}\right|} \rightarrow 0$ as $z \rightarrow z_{0}$.
5. Using (1), (2), and the squeeze theorem, show that if $f(x)$ is differentiable at $x_{0}$ and $g(y)$ is differentiable at $y_{0}$, then $u(x, y)=f(x) g(y)$ is differentiable at $\left(x_{0}, y_{0}\right)$.
6. Show that if $u(x, y), v(x, y)$ are differentiable and $c_{1}, c_{2}$ are constants, then $c_{1} u(x, y)+c_{2} v(x, y)$ and $u(x, y) v(x, y)$ are also differentiable.
7. Recast the function $u(x, y)$ in (4) in polar coordinates by setting $x=r \cos \theta$, $y=r \sin \theta$. Show that $u(x, y)=\frac{1}{2} \sin (2 \theta)$, and use this formulation to describe the behavior of the function.
8. By reversing the steps of Theorem 3, show that if $f=u+i v$ is analytic on an open set $S$, then $u$ and $v$ are differentiable on $S$.

