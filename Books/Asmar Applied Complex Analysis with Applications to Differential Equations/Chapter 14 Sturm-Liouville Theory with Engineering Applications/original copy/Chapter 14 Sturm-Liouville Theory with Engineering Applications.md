<!-- Page 1 -->

Left margin note (page 1)

Topics to Review
In studying this chapter, it will help to keep in mind some specific examples of orthogonal functions and their associated expansion theory. For example, you might use Fourier series or Bessel expansions as your basis for comparison. Sections 6.1, 6.2, and 6.4 are self-contained. Sections 6.1 and 6.2 develop the general subject of Sturm-Liouville theory for boundary value problems associated with second order linear ordinary differential equations. Section 6.4 develops a corresponding theory for certain fourth-order problems. In Sections 6.3 and 6.5 we look at specific classical applications of the second and fourth-order theories, respectively.
Looking Ahead...
The applications in this chapter are some of the most beautiful in physics and engineering. They put together different theories and use almost all our knowledge of special series expansions. Even though these applications are all classical, they are presented in a way that invites the use of computers. For example, in the hanging chain problem (Section 6.3), the solution is carried out to a point where it can be fed into a computer to generate pictures that simulate the motion of the hanging chain. The computer can be used in a similar way to illustrate the new expansion results arising in SturmLiouville theory, especially the complicated fourth-order expansions and their related applications to the elastic vibrations of beams (Sections 6.4, 6.5).

Right margin note (page 1)

ideas

TLE
ne in case, blem were peing able ecial essel, lated part
that usly, endre who udies work
apwill them ented (Seclates

++++

6

STURM-LIOUVILLE THEORY WITH ENGINEERING APPLICATIONS
It is not once nor twice but times without number that the same make their appearance in the world.
-ARISTO,

In the previous chapters you may have noticed a common then the solutions of the various boundary value problems. In each after separating variables, we had to solve a boundary value pro for an ordinary differential equation. Although the equations often different, their solutions shared the common properties of orthogonal and of having expansion theorems. We were then to express an arbitrary function in a series in terms of these sp orthogonal solutions. In this way, we encountered Legendre, B Fourier, and other related expansions. Are these expansions iso theories that happened to share common properties, or are they of a general theory that unifies them all?

The main focus of this chapter is to develop a general theory encompasses all the specific expansion theorems considered previc including Fourier, Fourier sine, Fourier cosine, Bessel, and Lege expansions. This theory is named after Sturm and Liouville, developed it in the early part of the nineteenth century in their st of heat conduction problems, not long after the ground-breaking of Fourier.

Beyond its esthetic appeal, Sturm-Liouville theory has man plications in applied mathematics, physics, and engineering. W use it to obtain further expansion results rather than developing on a case-by-case basis. Several classical applications are prese in this chapter, including the problems of the hanging chain tion 6.3), the vibrating beam (Section 6.5), and the theory of p and the biharmonic operator (Sections 6.6-6.7).

---

<!-- Page 2 -->

Left margin note (page 2)

326 Chapter 6 S
6.1 Orthogo

Right margin note (page 2)

ertain cential order show ее Арbasis, fferenpuville ewhat al vecbasic ns. and Two set of from ists of inner
stigate hat is r $\boldsymbol{v}=$ f their egrate on an $f$ and

++++

turm-Liouville Theory with Engineering Applications

nal Functions
You may recall from your first course in differential equations how notions from linear algebra were crucial in studying solutions of differ equations. For example, to check whether two solutions of a second linear differential equation yield the general solution, it is enough to that the determinant of a certain matrix (the Wronskian) is nonzero (s pendix A.1). These and other notions, such as linear independence and contributed in an essential way to our understanding of solutions of di tial equations. Similarly, our development of the theory of Sturm-Li in this chapter will require notions from linear algebra that are som abstract but simple to explain in the context of a finite-dimensiona tor space. For this reason, we start our discussion by reviewing some concepts from linear algebra, specialized to vectors in three dimensio

Recall that the inner product of two vectors $\boldsymbol{x}=\left(x_{1}, x_{2}, x_{3}\right. \boldsymbol{y}=\left(y_{1}, y_{2}, y_{3}\right)$ is the number $\boldsymbol{x} \cdot \boldsymbol{y}=(\boldsymbol{x}, \boldsymbol{y})=x_{1} y_{1}+x_{2} y_{2}+x_{3} y_{3}$. nonzero vectors $\boldsymbol{x}$ and $\boldsymbol{y}$ are said to be orthogonal if $\boldsymbol{x} \cdot \boldsymbol{y}=0$. A nonzero vectors is said to be orthogonal if any two distinct vectors this set are orthogonal. A simple example of an orthogonal set cons the vectors $\boldsymbol{e}_{\mathbf{1}}=(1,0,0), \boldsymbol{e}_{\mathbf{2}}=(0,1,0)$, and $\boldsymbol{e}_{3}=(0,0,1)$. The product is also used to define the norm of a vector $\boldsymbol{v}$ by
$$
\|\boldsymbol{v}\|=\sqrt{(\boldsymbol{v}, \boldsymbol{v})}=\left(\sum_{j=1}^{3} v_{j}^{2}\right)^{1 / 2} .
$$

Here are two properties of the set $\left\{e_{1}, e_{2}, e_{3}\right\}$ that we wish to inves for sets of functions:
- The set $\left\{e_{1}, e_{2}, e_{3}\right\}$ is complete. That is, if $v$ is a vector orthogonal to $\boldsymbol{e}_{1}, \boldsymbol{e}_{2}$, and $\boldsymbol{e}_{3}$ then $\boldsymbol{v}=0$.
- The set $\left\{e_{1}, e_{2}, e_{3}\right\}$ is a generating set. That is, every vecto $\left(v_{1}, v_{2}, v_{3}\right)$ can be written as
$$
\boldsymbol{v}=\sum_{j=1}^{3}\left(\boldsymbol{v}, \boldsymbol{e}_{j}\right) \boldsymbol{e}_{j} .
$$

Inner Products and Orthogonality of Functions
In defining the inner product of two vectors, we summed the products o components. To define the inner product of two functions, we will int their product as follows. Let $f$ and $g$ be real-valued functions defined interval ( $a, b$ ) (the interval may be infinite). The inner product of $g$, denoted $(f, g)$, is the number

---

<!-- Page 3 -->

Left margin note (page 3)

If $f$ and $g$ are complex-valued, then define
$$
(f, g)=\int_{a}^{b} f(x) \overline{g(x)} d x
$$

ORTHOGONAL FUNCTIONS

In the definitions of orthogonality and norm, you should use the appropriate definition of ( $f, g$ ) for complex-valued functions.

Right margin note (page 3)

327
cause
inner
$s$ are
his is

$f$ is then 1, are ional d on and m) = ed an set
n the ctions

ining

++++

Section 6.1 Orthogonal Functions
$$
(f, g)=\int_{a}^{b} f(x) g(x) d x
$$

This terminology is the same as for the inner product of vectors bec the function $(\cdot, \cdot)$ defined in (3) satisfies the same properties as the product of vectors (see Exercise 21). We will assume that the function real-valued and nice enough that all integrals of the form (3) exist. T for example the case, if the functions are piecewise continuous.

The functions $f$ and $g$ are called orthogonal on the interval ( $a, b$ ) if
$$
(f, g)=\int_{a}^{b} f(x) g(x) d x=0
$$

We define the norm of $f$, denoted $\|f\|$, by
$$
\|f\|=\sqrt{(f, f)}=\left(\int_{a}^{b}|f(x)|^{2} d x\right)^{1 / 2}
$$

If $\|f\|<\infty$, we also say that $f$ is square integrable on $(a, b)$. If real-valued, then $|f(x)|^{2}$ is simply $f^{2}(x)$. But if $f$ is complex-valued, $|f(x)|^{2}=f(x) \overline{f(x)}$. Note how both definitions, orthogonality and norm based on the notion of inner products as they were in the finite-dimens case. (Compare with (2).) A set of functions $\left\{f_{1}, f_{2}, f_{3}, \ldots\right\}$ define the interval ( $a, b$ ) is called an orthogonal set if $\left\|f_{n}\right\| \neq 0$ for all $n$, each distinct pair of functions from the set is orthogonal, that is, ( $f_{n}, f$ 0 for $n \neq m$. If, in addition, the norm of each $f_{n}$ is 1 , the set is call orthonormal set. Hence, if we divide each function in an orthogon by its norm we obtain an orthonormal set.

EXAMPLE 1 Orthogonal functions
Show that the set of functions $f_{n}(x)=\sin n x(n=1,2, \ldots)$ is orthogonal o interval $[-\pi, \pi]$ and obtain the corresponding orthonormal set.
Solution We need to show that $\|\sin n x\| \neq 0$ and each distinct pair of fun in the given set is orthogonal. We have
$$
\|\sin n x\|^{2}=\int_{-\pi}^{\pi} \sin ^{2} n x d x=\int_{-\pi}^{\pi} \frac{1-\cos 2 n x}{2} d x=\pi
$$

Thus the norm of $\sin n x$ is $\|\sin n x\|=\sqrt{\pi} \neq 0$. For $m \neq n$ we have
$$
\int_{-\pi}^{\pi} \sin m x \sin n x d x=\frac{1}{2} \int_{-\pi}^{\pi}[\cos (m-n) x-\cos (m+n) x] d x=0
$$

To obtain an orthonormal set we divide each function by its norm, thus obta functions of norm 1. The corresponding orthonormal set is

---

<!-- Page 4 -->

Left margin note (page 4)

328
Chapter 6
Sturm-Liou

Right margin note (page 4)

er se-
onding $2, \ldots$. ual to
class cewise ctions in $A$.
nction
ts $a_{j}$ ?
eyond ogonal stions

++++

ville Theory with Engineering Applications
$$
\frac{\sin x}{\sqrt{\pi}}, \frac{\sin 2 x}{\sqrt{\pi}}, \frac{\sin 3 x}{\sqrt{\pi}}, \ldots
$$

The next example deals with the trigonometric system from Four ries. Note that this set has the set from Example 1 as a subset.

EXAMPLE 2 The trigonometric system
The set of functions
$$
1, \sin x, \cos x, \sin 2 x, \cos 2 x, \sin 3 x, \cos 3 x, \ldots
$$
is orthogonal on the interval $[-\pi, \pi]$ (see Section 2.1). To obtain the correspo orthonormal set, we compute $\|\cos n x\|=\|\sin n x\|=\sqrt{\pi} \neq 0$, for $n=1$, Also, the norm of the function identically 1 over the interval $[-\pi, \pi]$ is eq $\sqrt{2 \pi}$. Thus the orthonormal set is
$$
\frac{1}{\sqrt{2 \pi}}, \frac{\sin x}{\sqrt{\pi}}, \frac{\cos x}{\sqrt{\pi}}, \frac{\sin 2 x}{\sqrt{\pi}}, \frac{\cos 2 x}{\sqrt{\pi}}, \frac{\sin 3 x}{\sqrt{\pi}}, \frac{\cos 3 x}{\sqrt{\pi}}, \ldots
$$

EXAMPLE 3 Legendre polynomials
It was shown in Section 5.6 that the Legendre polynomials satisfy
$$
\int_{-1}^{1} P_{n}^{2}(x) d x=\frac{2}{2 n+1} \quad \text { and } \quad \int_{-1}^{1} P_{m}(x) P_{n}(x) d x=0 \quad \text { for } m \neq n
$$

Thus the Legendre polynomials form an orthogonal set on $[-1,1]$.
Generalized Fourier Series
Let $A$ be a class of functions on $(a, b)$. For example, $A$ could be the of all continuous functions on $(a, b)$; or $A$ could be the class of all pie smooth functions; or $A$ could be the class of all square integrable fun $f$ on $(a, b)$. Suppose $f_{1}, f_{2}, f_{3}, \ldots$ is an orthogonal set of functions As in the finite-dimensional case, the following questions arise:
1. Do the functions $f_{1}, f_{2}, f_{3}, \ldots$ generate $A$ ? That is, given a fu $f$ in $A$, is it possible to express $f$ as a series of the form
$$
f(x)=\sum_{j=1}^{\infty} a_{j} f_{j}(x),
$$
where the $a_{j}$ 's are real or complex numbers?
2. If the representation (4) is possible, how do we find the coefficien

A complete treatment of these questions requires machinery that is b the scope of this text. Without going far into the theory of orth functions, we will try to motivate the answers to these fundamental que

---

<!-- Page 5 -->

Left margin note (page 5)

THEOREM 1
GENERALIZED FOURIER SERIES

Right margin note (page 5)

329

from the have and
right
right
an be
such ers.
the t we in $A$ form al to
$\cos x$, m an ation ooth if all cally since

++++

Section 6.1 Orthogonal Functions

through examples. Starting with the second question, and taking a hint (1), our guess is that the coefficients in (4) should be given in terms o inner products of $f$ with $f_{1}, f_{2}, f_{3}, \ldots$. To see this, we proceed as we done before with Fourier series. We multiply both sides of (4) by $f_{k}$ integrate term by term on the interval $(a, b)$. This gives
$$
\int_{a}^{b} f(x) f_{k}(x) d x=\sum_{j=1}^{\infty} a_{j} \int_{a}^{b} f_{j}(x) f_{k}(x) d x
$$

Because of orthogonality, the $k$ th term is the only nonzero term on the side and so
$$
\int_{a}^{b} f(x) f_{k}(x) d x=a_{k} \int_{a}^{b} f_{k}^{2}(x) d x
$$

The left side is the inner product of $f$ and $f_{k}$, and the integral on the side is the square of the norm of $f_{k}$, so $\left(f, f_{k}\right)=a_{k}\left\|f_{k}\right\|^{2}$. Thus
$$
a_{k}=\frac{\left(f, f_{k}\right)}{\left\|f_{k}\right\|^{2}}=\frac{1}{\left\|f_{k}\right\|^{2}} \int_{a}^{b} f(x) f_{k}(x) d x
$$

This motivates the following answer to the second question.
If $f_{1}, f_{2}, f_{3}, \ldots$ is a set of orthogonal functions on $(a, b)$ and if $f$ ca represented as a series in the form (4), then
$$
f(x)=\sum_{j=1}^{\infty} \frac{\left(f, f_{j}\right)}{\left\|f_{j}\right\|^{2}} f_{j}(x)
$$

The series (6) is called a generalized Fourier series. Examples of series include Fourier, Legendre, and Bessel series of the previous chapt

We now turn to the first question. Again, we take a hint from three-dimensional real vector space. For the classes of functions tha will consider in this book, a set of orthogonal functions $f_{1}, f_{2}, f_{3}, \ldots$ generates $A$ if and only if the the orthogonal functions $f_{1}, f_{2}, f_{3}, \ldots$ a complete set of functions in the following sense: If $f$ is orthogon every $f_{j}, j=1,2,3, \ldots$, then $f$ must be identically 0 .

In the case of Fourier series on the interval [ $-\pi, \pi$ ], the functions $1, \mathrm{c} \cos 2 x, \cos 3 x, \ldots, \cos n x, \ldots, \sin x, \sin 2 x, \sin 3 x, \ldots, \sin n x, \ldots$ for orthogonal set of functions on $[-\pi, \pi]$. By the Fourier series represent theorem, this set also generates the class $A$ of $2 \pi$-periodic, piecewise sm functions. What does completeness mean in this case? It means that the Fourier coefficients of a function $f$ are zero, then $f$ must be identi zero. This fact follows from the Fourier series representation theorem,

---

<!-- Page 6 -->

Left margin note (page 6)

330
Chapter 6
S

ORTHOGON WITH RESPE A W

Right margin note (page 6)

of $f$ is zero. neral. ill enit the these ouville
are such valued o the
on on onding
tion $w$
$=0$ for $x)=1$

From hus the weight
with

++++

turm-Liouville Theory with Engineering Applications

if we set all the coefficients of $f$ equal to 0 , then the Fourier series identically 0 . But the Fourier series converges to $f$, and so $f$ must be

To establish the completeness of a set of functions is difficult in ge The good news is that most orthogonal sets of functions that we w counter arise from solutions of ordinary differential equations that so-called Sturm-Liouville theory form. The completeness property of sets of functions is a consequence of general results from the Sturm-Lic theory. (See Theorem 3, Section 6.2.)
Orthogonality with Respect to a Weight
What we have presented thus far can be extended to functions the orthogonal with respect to a weight function. We have encounterec situations in the study of Bessel series. In general, if $f$ and $g$ are realfunctions on $(a, b)$, we define their inner product with respect t weight $\boldsymbol{w}$ to be the number
$$
(f, g)=\int_{a}^{b} f(x) g(x) w(x) d x
$$

We assume that $w(x)$ is a nonnegative piecewise continuous functi $[a, b]$ that is not identically 0 on any subinterval of $[a, b]$. The correspc definition of orthogonality is as follows.

ALITY CT TO EIGHT

The functions $f$ and $g$ are orthogonal with respect to the weight func on the interval $[a, b]$ if
$$
\int_{a}^{b} f(x) g(x) w(x) d x=0
$$

The norm of $\boldsymbol{f}$ with respect to the weight function $\boldsymbol{w}$ is
$$
\|f\|=\left(\int_{a}^{b}|f(x)|^{2} w(x) d x\right)^{1 / 2}
$$

EXAMPLE 4 Orthogonality with respect to a weight
(a) The functions $f_{n}(x)=\cos n x(n=1,2, \ldots)$ satisfy $\int_{-\pi}^{\pi} f_{m}(x) f_{n}(x) d x m \neq n$. So these functions form an orthogonal set with weight function $w($ on the interval $(-\pi, \pi)$.
(b) Let $\alpha_{1}, \alpha_{2}, \alpha_{3}, \ldots$ denote the positive zeros of the Bessel function $J_{0}$. Theorem 1, Section 4.8, we have $\int_{0}^{1} J_{0}\left(\alpha_{m} x\right) J_{0}\left(\alpha_{n} x\right) x d x=0$ for $m \neq n$. Tl functions $J_{0}\left(\alpha_{n} x\right), n=1,2, \ldots$ form an orthogonal set with respect to the function $w(x)=x$ on the interval $(0,1)$.

The following is the analog of Theorem 1 for expansions in serie respect to functions that are orthogonal with respect to a weight.

---

<!-- Page 7 -->

Left margin note (page 7)

THEOREM 2
GENERALIZED FOURIER SERIES

Although (8) looks identical to (6), you should keep in mind that computing the inner products and norms in (8) involves a weight function.

THEOREM 3
PARSEVAL'S IDENTITY

Right margin note (page 7)

331

eight
onal 4.8 this the lete
ct to nite.
tity ince ions nted s of we nner , we
ct to etric hev

++++

Section 6.1 Orthogonal Functions

If $f_{1}, f_{2}, f_{3}, \ldots$ is a set of orthogonal functions with respect to the w $w$ on $[a, b]$ and if $f$ can be represented as a series in the form (4), then
$$
f(x)=\sum_{j=1}^{\infty} \frac{\left(f, f_{j}\right)}{\left\|f_{j}\right\|^{2}} f_{j}(x)
$$

In Example 4(b) we observed that the functions $J_{0}\left(\alpha_{n} x\right)$ are orthog with weight $w(x)=x$ on the interval $(0,1)$. In Example 1 of Section we derived the series expansion of the function $f(x)=1$ in terms of orthogonal series. You should check that the series obtained there is same as that in (8).

We end this section with a statement of Parseval's identity for comp orthogonal systems.

Let $f_{1}, f_{2}, f_{3}, \ldots$ be a complete set of orthogonal functions with respe the weight $w$ on $[a, b]$ and let $f$ be such that its norm as given by (7) is fi (That is, $f$ is square integrable with respect to the weight $w$.) Then
$$
\int_{a}^{b}|f(x)|^{2} w(x) d x=\sum_{j=1}^{\infty} \frac{\left|\left(f, f_{j}\right)\right|^{2}}{\left\|f_{j}\right\|^{2}}
$$

As we have seen in Section 2.5 with Fourier series, Parseval's ider has many important applications. We can motivate it as follows. S the functions $f_{1}, f_{2}, f_{3}, \ldots$ form a complete orthogonal set of funct with respect to the weight $w$ on $[a, b]$, the function $f$ can be represer in a generalized series as in (8). If $f$ is real-valued, multiply both side (8) by $f(x) w(x)$, and integrate over the interval $[a, b]$. Assuming that can integrate the series term by term and using the definition of the ir product with respect to the weight $w$, we get (9). If $f$ is complex-valued multiply both sides of (8) by $\overline{f(x)} w(x)$ and repeat the same proof.

Exercises 6.1
In Exercises 1-8, show that the given set of functions is orthogonal with respe the given weight on the prescribed interval.
1. $1, \sin \pi x, \cos \pi x, \sin 2 \pi x, \cos 2 \pi x, \sin 3 \pi x, \cos 3 \pi x, \ldots ; w(x)=1$ on $[0,2]$.
2. $f(x)$ is an even function, $g(x)$ is an odd function; $w(x)=1$ on any symm interval about 0 .
3. $1, x,-1+2 x^{2} ; w(x)=\frac{1}{\sqrt{1-x^{2}}}$ on $[-1,1]$. (These are examples of Chebys polynomials of the first kind. See Exercises 6.2 for further details.)
4. $-3 x+4 x^{3}, 1-8 x^{2}+8 x^{4} ; w(x)=\frac{1}{\sqrt{1-x^{2}}}$ on $[-1,1]$.

---

<!-- Page 8 -->

Left margin note (page 8)

332
Chapter 6 Sturm

Right margin note (page 8)

yshev
guerre
rmite
$x+x^{2}$
t $w(x)$ D?
on the
with $(a, b)$. weight t func-
metric
ntity
$p$, and
ive the
8 with

++++

-Liouville Theory with Engineering Applications
5. $1,2 x,-1+4 x^{2} ; w(x)=\sqrt{1-x^{2}}$ on $[-1,1]$. (These are examples of Cheb polynomials of the second kind.)
6. $1,1-x,\left(2-4 x+x^{2}\right) / 2 ; w(x)=e^{-x}$ on $[0, \infty)$. (These are examples of $\mathbf{L a}$ polynomials.)
7. $1,2 x,-2+4 x^{2} ; w(x)=e^{-x^{2}}$ on $(-\infty, \infty)$. (These are examples of He polynomials. [Hint: Exercise 33(a), Section 4.7.]
8. $\left(2-4 x+x^{2}\right) / 2,-12 x+8 x^{3} ; w(x)=e^{-x}$ on $[0, \infty)$.
9. Determine the constants $a$ and $b$ so that the functions $1, x$, and $a+b$ become orthogonal on the interval $[-1,1]$.
10. If the functions $f(x)$ and $g(x)$ are orthogonal with respect to a weigh on $[0, L]$, what can be said about the functions $f(a x)$ and $g(a x)$ where $a>$
11. Compute the norms of the functions in Exercise 1.
12. Compute the norms of the functions in Exercise 5.
13. What is the orthonormal set corresponding to the Legendre polynomials interval $[-1,1]$ ?
14. Show that if $f$ and $g$ are continuous functions on $[a, b]$ that are orthogon respect to the weight function 1 , then either $f$ or $g$ must vanish somewhere in
15. Show that if $f_{1}(x), f_{2}(x), \ldots$ are orthogonal on $[0,1]$ with respect to the $x$, then $f_{1}(\sqrt{x}), f_{2}(\sqrt{x}), \ldots$ are orthogonal on $[0,1]$ with respect to the weigh tion 1.
16. Parseval's identity for Fourier series. Specialize (9) to the trigonc system (of period $2 p$ ) to obtain (6) of Section 2.5.
17. Parseval's identity for Legendre series. Use (9) to derive the ide
$$
\int_{-1}^{1} f(x)^{2} d x=\sum_{n=0}^{\infty} \frac{2 A_{n}^{2}}{2 n+1},
$$
where $A_{n}$ is the $n$th Legendre coefficient of $f$. (See Section 5.6.)
18. Parseval's identity for Bessel series. Use (9) to derive the identit
$$
\int_{0}^{R} f(x)^{2} x d x=\sum_{j=1}^{\infty} \frac{R^{2} J_{p+1}^{2}\left(\alpha_{p j}\right)}{2} A_{j}^{2}
$$
where $A_{j}$ is the $j$ th coefficient of the Bessel series expansion of $f$ of order $\alpha_{p j}$ is the $j$ th positive zero of $J_{p}$. (See Section 4.8.)
19. Sums of reciprocals of squares of zeros of Bessel functions. Der following interesting formula: $\frac{1}{4(p+1)}=\sum_{j=1}^{\infty} \frac{1}{\alpha_{p j}^{2}}$. [Hint: Apply Exercise ] $R=1$ to the Bessel series expansion found in Exercise 20, Section 4.8.]
20. By specializing Exercise 19 to the case $p=\frac{1}{2}$, derive the identity
$$
\frac{\pi^{2}}{6}=\sum_{j=1}^{\infty} \frac{1}{j^{2}}
$$

---

<!-- Page 9 -->

Left margin note (page 9)

6.2 Sturm-L

REG
STURM-LIOUY
PRO]

Right margin note (page 9)

333

oralled value ually lized
m on
and orm. $r(x) >0 <b$ ns.
blem ne of the (2a) use it goes nt to erval case some

++++

Section 6.2 Sturm-Liouville Theory
21. Show that the inner product satisfies the following properties:
(a) $(a f, g)=a(f, g)$ for any number $a$,
(b) $(f+g, h)=(f, h)+(g, h)$,
(c) $(f, f) \geq 0$ for any function $f$.
iouville Theory

In this section we explore the interplay between orthogonal functions thogonal expansions, and differential equations. We study the so-c Sturm-Liouville problems, which comprise a general class of boundary problems with sets of solutions that have the property of being mut orthogonal. Moreover, a given function can be expressed as a genera Fourier series in terms of these sets of orthogonal solutions.

A regular Sturm-Liouville problem is a boundary value proble a closed finite interval $[a, b]$ of the form

ULAR
VILLE
$$
\left[p(x) y^{\prime}\right]^{\prime}+[q(x)+\lambda r(x)] y=0, \quad a<x<b
$$
(a) $\left\{\begin{array}{l}c_{1} y(a)+c_{2} y^{\prime}(a)=0, \\ d_{1} y(b)+d_{2} y^{\prime}(b)=0 .\end{array}\right.$
where at least one of $c_{1}$ and $c_{2}$ and at least one of $d_{1}$ and $d_{2}$ are nonzero $\lambda$ is a parameter. Equation (1) is said to be in Sturm-Liouville f We further assume the regularity conditions: $p(x), p^{\prime}(x), q(x)$, and are continuous on the closed interval $a \leq x \leq b$, with $p(x)>0$ and $r(x)$ for $a \leq x \leq b$. Often there is no need to mention the interval $a<x$ explicitly, since $a$ and $b$ can be understood from the boundary conditic

A singular Sturm-Liouville problem is a boundary value pro consisting of equation (1) either on a finite interval where at least o the regularity properties fails or on an infinite interval. In this case boundary conditions are not always described by sets of equations like and (2b). Typically, a Sturm-Liouville problem is singular either becau occurs on an infinite interval, or because one or more of the coefficients to 0 or $\infty$ at an endpoint of the interval, or both. Indeed, it is convenie require that $p(x), p^{\prime}(x), q(x)$, and $r(x)$ are continuous on the open int $a<x<b$, with $p(x)>0$ and $r(x)>0$ for $a<x<b$. This will be the for all singular problems encountered in this book. We illustrate with examples.

---

<!-- Page 10 -->

Left margin note (page 10)

334
Chapter 6 Sturm-Liou

![](./images/b6761637-e91c-4988-8637-83a0e794256f-10_303_442_1477_61.jpg)

Figure $1 \sinh x$ is always increasing.

Right margin note (page 10)

in the
L) $=0$,
18) in
ouville
ularity
D) $=0$.
onzero
of the nd are values
e prob-
c) $=0$, 1 and

Sturmso we
ecomes e need ng the 0 (see case.
is $y=$ Thus
uation From
low we seeking

++++

ville Theory with Engineering Applications

EXAMPLE 1 Classical singular Sturm-Liouville problems
(a) Legendre's equation $\left(1-x^{2}\right) y^{\prime \prime}-2 x y^{\prime}+n(n+1) y=0$ can be put Sturm-Liouville form
$$
\left[\left(1-x^{2}\right) y^{\prime}\right]^{\prime}+n(n+1) y=0, \quad-1<x<1,
$$
with $p(x)=1-x^{2}, q(x)=0, r(x)=1$, and $\lambda=n(n+1)$. Note that $p( \pm 1$ and so one of the regularity conditions is not satisfied.
(b) Parametric form of Bessel's equation This refers to equation Section 4.8. It is easy to check that this equation can be put in the Sturm-Li form
$$
\left[x y^{\prime}\right]^{\prime}+\left[-\frac{p^{2}}{x}+\lambda^{2} x\right] y=0, \quad 0<x<a, \quad y(a)=0
$$

So $p(x)=r(x)=x, q(x)=-\frac{p^{2}}{x}$, and the parameter is written as $\lambda^{2}$. The reg conditions are not all met, because $q(x)$ is not defined at 0 , and also $p(0)=r($ Hence, this problem is a singular Sturm-Liouville problem.

Clearly $y=0$ is a solution of every Sturm-Liouville problem. The no solutions of a Sturm-Liouville problem are called the eigenfunctions problem, and those values of $\lambda$ for which nonzero solutions can be fou called the eigenvalues. In Example 2 we see how to determine eigen and eigenfunctions.

EXAMPLE 2 A regular Sturm-Liouville problem
Find the eigenvalues and corresponding eigenfunctions of the Sturm-Liouvill lem
$$
y^{\prime \prime}+\lambda y=0, \quad y(0)=y(\pi)=0
$$

Solution This differential equation fits the form of (1) with $p(x)=1, q(x)$ and $r(x)=1$. In the boundary conditions, $a=0$ and $b=\pi$, with $c_{1}=d_{1}= c_{2}=d_{2}=0$, so this is a regular Sturm-Liouville problem.

We seek nonzero solutions of the problem. As is often the case with Liouville problems, the nature of the solution depends on the sign of $\lambda$, consider three cases.
CASE 1: $\lambda<0$. Let us write $\lambda=-\alpha^{2}$, where $\alpha>0$. Then the equation b $y^{\prime \prime}-\alpha^{2} y=0$, and its general solution is $y=c_{1} \sinh \alpha x+c_{2} \cosh \alpha x$. $y(0)=0$, so substituting into the general solution gives $c_{2}=0$. Now usi condition $y(\pi)=0$, we get $0=c_{1} \sinh \alpha \pi$, and since $\sinh x \neq 0$ unless $x=$ Figure 1), we infer that $c_{1}=0$. Thus there are no nonzero solutions in this

CASE 2: $\lambda=0$. Here the general solution of the differential equation $c_{1} x+c_{2}$, and as in Case 1 the boundary conditions force $c_{1}$ and $c_{2}$ to be 0 . again there is no nonzero solution.
CASE 3: $\lambda>0$. In this case we can write $\lambda=\alpha^{2}$ with $\alpha>0$, and so the ed becomes $y^{\prime \prime}+\alpha^{2} y=0$. The general solution is $y=c_{1} \cos \alpha x+c_{2} \sin \alpha x$. $y(0)=0$ we get $0=c_{1} \cos 0+c_{2} \sin 0$, or $0=c_{1}$. Thus $y=c_{2} \sin \alpha x$. substitute the other boundary condition to get $0=c_{2} \sin \alpha \pi$. Since we are

---

<!-- Page 11 -->

Left margin note (page 11)

THEOREM 1
EIGENVALUES OF REGULAR STURM-LIOUVILLE PROBLEMS

Right margin note (page 11)

335
hence

ill be
igenrated m an corwhen form that r the tions ofs of by G.
form
orops. To y de-urm-

1ville ions.

++++

Section 6.2 Sturm-Liouville Theory

nonzero solutions, we take $c_{2} \neq 0$. Thus we must have $\sin \alpha \pi=0$, and $\alpha=1,2,3, \ldots$. This means that, since $\lambda=\alpha^{2}$, the problem has eigenvalues
$$
\lambda_{1}=1, \lambda_{2}=4, \lambda_{3}=9, \ldots
$$
and corresponding eigenfunctions
$$
y_{1}=\sin x, y_{2}=\sin 2 x, y_{3}=\sin 3 x, \ldots .
$$

We have let the constant $c_{2}$ be 1 in each case. All other eigenfunctions w nonzero multiples of these.

We now describe some fundamental properties of eigenvalues and e functions of regular Sturm-Liouville problems, all of which are illust by the solution to Example 2. In that example, the eigenvalues for increasing sequence of real numbers. Moreover, to each eigenvalue there responds just one linearly independent eigenfunction. For instance, $\lambda=4$ in Example 2, the corresponding eigenfunctions are all of the $c_{2} \sin 2 x$; that is, they are all multiples of $\sin 2 x$. It can be checked easily the eigenfunctions $\sin x, \sin 2 x, \sin 3 x, \ldots$ form an orthogonal set ove interval $0<x<\pi$. As Theorems 1 and 2 below indicate, these observa hold for all regular second order Sturm-Liouville problems. The proc these theorems are found in Ordinary Differential Equations, 2nd ed., Birkhoff and G. Rota, Wiley, 1969.

The eigenvalues of a regular Sturm-Liouville problem are all real and an increasing sequence
$$
\lambda_{1}<\lambda_{2}<\lambda_{3}<\cdots
$$
where $\lambda_{j} \rightarrow \infty$ as $j \rightarrow \infty$.
Our next result deals with the orthogonality of eigenfunctions. This erty holds for regular as well as some singular Sturm-Liouville problem: understand the reason behind the orthogonality property, we start b riving some consequences of the boundary conditions (2), in regular St Liouville problems.

Let $\lambda_{j}$ and $\lambda_{k}$ be two distinct eigenvalues of the regular Sturm-Lio problem (1)-(2), and let $y_{j}$ and $y_{k}$ denote their corresponding eigenfunct From (2a) we have
$$
\begin{aligned}
c_{1} y_{j}(a)+c_{2} y_{j}^{\prime}(a) & =0 \\
c_{1} y_{k}(a)+c_{2} y_{k}^{\prime}(a) & =0
\end{aligned}
$$

In matrix form this becomes
$$
\left[\begin{array}{ll}
y_{j}(a) & y_{j}^{\prime}(a) \\
y_{k}(a) & y_{k}^{\prime}(a)
\end{array}\right]\left[\begin{array}{l}
c_{1} \\
c_{2}
\end{array}\right]=\left[\begin{array}{l}
0 \\
0
\end{array}\right] .
$$

---

<!-- Page 12 -->

Left margin note (page 12)

336
Chapter 6
S

CONDITIO ORTHOGON IN SINC STURM-LIOU PROI

THEO
UNIQUENES ORTHOGON

EIGENFUNC

Right margin note (page 12)

ffuncthese

0 .
ration
als, or (2) we ws.
oblem, require
$=0$.
olems, many us (see
of (1) equire tly in s easy
ne lin-
regular unction oblems
to the ig that $\left./_{2}\right)=0$

++++

urm-Liouville Theory with Engineering Applications

Since not both $c_{1}$ and $c_{2}$ are 0 , we must have that
$$
\operatorname{det}\left[\begin{array}{ll}
y_{j}(a) & y_{j}^{\prime}(a) \\
y_{k}(a) & y_{k}^{\prime}(a)
\end{array}\right]=0,
$$
or, equivalently, $y_{k}(a) y_{j}^{\prime}(a)-y_{j}(a) y_{k}^{\prime}(a)=0$. Similarly, since the eiger tions satisfy (2b), we get that $y_{k}(b) y_{j}^{\prime}(b)-y_{j}(b) y_{k}^{\prime}(b)=0$. Combining two identities and the fact that $p(a)$ and $p(b)$ are finite, we infer that
$$
p(b)\left(y_{k}(b) y_{j}^{\prime}(b)-y_{j}(b) y_{k}^{\prime}(b)\right)-p(a)\left(y_{k}(a) y_{j}^{\prime}(a)-y_{j}(a) y_{k}^{\prime}(a)\right)=
$$

As you will see from the proof of Theorem 2, it is precisely this equ that will imply the orthogonality of the eigenfunctions.

In singular problems, since we may be dealing with infinite interv with functions that may be unbounded near the endpoints, instead of will require a condition similar to (3), but stated using limits as follov

N FOR
ALITY
ZULAR
VILLE
BLEMS

REM 2
S AND
ALITY
OF
TIONS

Suppose that $y_{1}$ and $y_{2}$ are eigenfunctions of a Sturm-Liouville pr corresponding to two distinct eigenvalues $\lambda_{1}$ and $\lambda_{2}$, respectively. We that
(4)
$$
\lim _{x \uparrow b} p(x)\left(y_{1}(x) y_{2}^{\prime}(x)-y_{2}(x) y_{1}^{\prime}(x)\right)-\lim _{x \downarrow a} p(x)\left(y_{1}(x) y_{2}^{\prime}(x)-y_{2}(x) y_{1}^{\prime}(x)\right.
$$

As we just noted, (4) reduces to (3) for regular Sturm-Liouville prol and thus it holds for regular Sturm-Liouville problems. It also holds in important singular problems, such as Legendre's and Bessel's equatior Example 3, below).

For another interesting example where (4) holds, consider the case when $a$ and $b$ are both finite and $p(a)=p(b)>0$. Instead of (2), we r that $y(a)=y(b)$ and $y^{\prime}(a)=y^{\prime}(b)$. These conditions appear frequer applications. They are called periodic boundary conditions. It i to verify that (4) holds in this case.
(a) Each eigenvalue of a regular Sturm-Liouville problem has just c early independent eigenfunction corresponding to it,
(b) Eigenfunctions corresponding to different eigenvalues of a Sturm-Liouville problem are orthogonal with respect to the weight fi $r(x)$. This assertion is also valid for the other Sturm-Liouville pr allowed by condition (4).

Proof (a) Suppose that $y_{1}$ and $y_{2}$ are two eigenfunctions corresponding eigenvalue $\lambda$. We will show that $y_{1}$ and $y_{2}$ are linearly dependent by provir their Wronskian $W\left(y_{1}, y_{2}\right)$ is 0 . Recall that we need only prove that $W\left(y_{1}\right.$, ?

---

<!-- Page 13 -->

Left margin note (page 13)

The reason we can use a Wronskian argument to prove the linear dependence of $y_{1}$ and $y_{2}$ is because $y_{1}$ and $y_{2}$ are eigenfunctions corresponding to the same eigenvalue, and hence they are solutions of the same ordinary differential equation. This argument will not work with eigenfunctions corresponding to distinct eigenvalues.

Right margin note (page 13)

337
et us
also
2 are
This
at is,
cor-
ns of
ify to
and
infer
lems s as-
igentwo

++++

Section 6.2 Sturm-Liouville Theory

at one point to show that $W\left(y_{1}, y_{2}\right)=0$ (Theorem 7 , Appendix A.1), so 1 evaluate the Wronskian at $x=a$. We have
$$
W\left(y_{1}, y_{2}\right)(a)=\left|\begin{array}{ll}
y_{1}(a) & y_{2}(a) \\
y_{1}^{\prime}(a) & y_{2}^{\prime}(a)
\end{array}\right|=y_{1}(a) y_{2}^{\prime}(a)-y_{2}(a) y_{1}^{\prime}(a) .
$$

Since $y_{1}$ and $y_{2}$ satisfy (2a), we have
$$
\left\{\begin{array}{l}
c_{1} y_{1}(a)+c_{2} y_{1}^{\prime}(a)=0, \\
c_{1} y_{2}(a)+c_{2} y_{2}^{\prime}(a)=0 .
\end{array}\right.
$$

Note that if we take $c_{1}=c_{2}=0$, then the system of equations is satisfied. We know from our assumptions that the system is verified when not both $c_{1}$ and zero. Thus the system of equations has more than one solution in $c_{1}$ and $c_{2}$. can happen if and only if the determinant of the coefficient matrix is zero. Th $y_{1}(a) y_{2}^{\prime}(a)-y_{1}^{\prime}(a) y_{2}(a)=0$, or, equivalently, $W\left(y_{1}, y_{2}\right)(a)=0$.
(b) Suppose $\lambda_{j} \neq \lambda_{k}$ are eigenvalues of a Sturm-Liouville problem, with responding eigenfunctions $y_{j}$ and $y_{k}$, respectively. Since $y_{j}$ and $y_{k}$ are solutic (1), we have
$$
\begin{array}{l}
{\left[p(x) y_{j}^{\prime}\right]^{\prime}+\left[q(x)+\lambda_{j} r(x)\right] y_{j}=0} \\
{\left[p(x) y_{k}^{\prime}\right]^{\prime}+\left[q(x)+\lambda_{k} r(x)\right] y_{k}=0}
\end{array}
$$

We multiply the first equation by $y_{k}$, the second by $y_{j}$, subtract, and simpl get
$$
y_{k}\left[p(x) y_{j}^{\prime}\right]^{\prime}-y_{j}\left[p(x) y_{k}^{\prime}\right]^{\prime}=\left(\lambda_{k}-\lambda_{j}\right) y_{j} y_{k} r(x) .
$$

Since $\frac{d}{d x}\left(p(x)\left(y_{k} y_{j}^{\prime}-y_{j} y_{k}^{\prime}\right)\right)=y_{k}\left[p(x) y_{j}^{\prime}\right]^{\prime}-y_{j}\left[p(x) y_{k}^{\prime}\right]^{\prime}$ (use the product rule simplify to see this), we get
$$
\begin{aligned}
\left(\lambda_{k}-\lambda_{j}\right) \int_{a}^{b} y_{j}(x) y_{k}(x) r(x) d x= & \int_{a}^{b} \frac{d}{d x}\left(p(x)\left(y_{k} y_{j}^{\prime}-y_{j} y_{k}^{\prime}\right)\right) d x \\
= & \left.p(x)\left(y_{k} y_{j}^{\prime}-y_{j} y_{k}^{\prime}\right)\right|_{a} ^{b} \\
= & p(b)\left[y_{k}(b) y_{j}^{\prime}(b)-y_{j}(b) y_{k}^{\prime}(b)\right] \\
& -p(a)\left[y_{k}(a) y_{j}^{\prime}(a)-y_{j}(a) y_{k}^{\prime}(a)\right]
\end{aligned}
$$

Appealing to (4), we see that the right side of (5) is 0 . Since $\lambda_{k}-\lambda_{j} \neq 0$, we that
$$
\int_{a}^{b} y_{j}(x) y_{k}(x) r(x) d x=0
$$
that is, $y_{j}$ and $y_{k}$ are orthogonal with respect to the weight function $r(x)$.
Note that part (a) of Theorem 2 may fail for Sturm-Liouville prob with periodic boundary conditions, because they do not satisfy (2a), a sumed in the proof. In particular, the equation
$$
y^{\prime \prime}+\lambda y=0
$$
with periodic boundary conditions $y(-\pi)=y(\pi), y^{\prime}(-\pi)=y^{\prime}(\pi)$ has e values $\lambda_{n}=n^{2}, n=0,1,2, \ldots$ and for each $\lambda_{n}$ with $n \geq 1$ there are

---

<!-- Page 14 -->

Left margin note (page 14)

338
Chapter 6 S

THEO
EIGENFUN
EXPAN

Right margin note (page 14)

4). In ouville nfuncve are
is put hus (4) omials, to the

Sturmhe fact es that nterval
ndition do not ctions,
values nfuncn $r(x)$. funclowing prodnorm

Sturmon the
and to
func-

++++

turm-Liouville Theory with Engineering Applications

linearly independent eigenfunctions $\sin n x$ and $\cos n x$ (see Exercise 1 general, as illustrated by this example, in any second-order Sturm-Li problem, each eigenvalue has at most two linearly independent eige tions corresponding to it. This is a consequence of the fact that dealing with a second-order differential equation.

EXAMPLE 3 Legendre polynomials and Bessel functions
(a) Looking back at Example 1(a), we see that, when Legendre's equation in Sturm-Liouville form, the function $p(x)=1-x^{2}$ satisfies $p( \pm 1)=0$. T holds, and so Theorem 2 implies that its eigenfunctions, the Legendre polyn $P_{n}(x)(n=0,1,2, \ldots)$, are orthogonal on the interval $(-1,1)$ with respect weight function $r(x) \equiv 1$.
(b) In Example 1(b), we put the parametric form of Bessel's equation in Liouville form and obtained the functions $p(x)=x$ and $r(x)=x$. Using t that $p(0)=0$ and $y(R)=0$, we see that (4) holds. Thus Theorem 2 impli the solutions of this equation, $J_{p}\left(\frac{\alpha_{p j}}{R} x\right), j=1,2, \ldots$, are orthogonal on the i $(0, R)$ with respect to the weight function $r(x)=x$.

It is interesting to note that we do not have to impose a boundary co (other than boundedness) at one of the singular points in (a) or (b). We apply a boundary condition at $\rho=0$ in cylindrical problems with Bessel fun or at $x= \pm 1$ for Legendre polynomials.

Eigenfunction Expansions
From Theorem 2 it follows that if $\lambda_{1}<\lambda_{2}<\lambda_{3}<\cdots$ is the set of eigen for a regular Sturm-Liouville problem, then a corresponding set of eige tions $\left\{y_{1}, y_{2}, y_{3}, \ldots\right\}$ is orthogonal with respect to the weight function Thus, as in Section 6.1, we can find orthogonal expansions for suitable tions in terms of $y_{1}, y_{2}, y_{3}, \ldots$. More precisely, we have the fol fundamental result in Sturm-Liouville theory. Recall that the inner uct $\left(y_{j}, y_{k}\right)$ with weight $r(x)$ is defined as $\int_{a}^{b} y_{j} y_{k} r(x) d x$ and that the $\left\|y_{j}\right\|$ is $\sqrt{\left(y_{j}, y_{j}\right)}$.

REM 3
CTION
JSIONS

Let $y_{1}, y_{2}, y_{3}, \ldots$ be the collection of eigenfunctions for a regular Liouville problem on an interval $[a, b]$. If $f$ is piecewise smooth interval $[a, b]$, then we have $f(x)=\sum_{j=1}^{\infty} A_{j} y_{j}(x)$, where
$$
A_{j}=\frac{\left(f, y_{j}\right)}{\left\|y_{j}\right\|^{2}}=\int_{a}^{b} f(x) y_{j}(x) r(x) d x / \int_{a}^{b} y_{j}^{2}(x) r(x) d x
$$

For $a<x<b$, the series converges to $f(x)$ if $f$ is continuous at $x$, $\frac{f(x+)+f(x-)}{2}$ otherwise.

The series expansion is called the eigenfunction expansion of the

---

<!-- Page 15 -->

Right margin note (page 15)

339

ints. Exrem. can this, asion ries. exasion robone rmle of ions, m
b. It $a= <0$, $-\lambda x$. will When f the
ation. rsect nany

++++

Section 6.2 Sturm-Liouville Theory

tion $f$, and the coefficients $A_{j}$ are called generalized Fourier coefficie Fourier sine (for the corresponding regular Sturm-Liouville problem, see ample 2 above) and cosine expansions provide illustrations of this theo The full proof of Theorem 3 is beyond the scope of this book. But we derive the formula for the $A_{j}$ 's from Theorem 2 of Section 6.1. Beyond it is clear that much more is true. We have already seen that the conclu of this theorem is valid for the singular cases of Legendre and Bessel se Thus, Legendre series and Bessel series are examples of eigenfunctior pansions. Similarly, the example of Fourier series shows that the conclu also holds in a case where periodic boundary conditions are imposed.

Eigenfunction expansions arise naturally in the solution of applied p lems. For example, when we studied heat conduction in a bar with radiating end (Example 2, Section 3.6), we encountered a regular Stu Liouville problem. As a further illustration, which demonstrates the ro the boundary conditions in determining the eigenvalues and eigenfunct we solve a related problem with altered boundary conditions.

EXAMPLE 4 Eigenvalues and eigenfunctions
Find the eigenvalues and eigenfunctions of the regular Sturm-Liouville proble
$$
X^{\prime \prime}+\lambda X=0, \quad X^{\prime}(0)=0, \quad X(1)+X^{\prime}(1)=0 .
$$

Solution If $\lambda=0$, the general solution of the differential equation is $X=a x+$ is easy to check that the only way to satisfy the boundary conditions is to take $b=0$. Thus $\lambda=0$ is not an eigenvalue since no nontrivial solutions exist. If $\lambda$ the general solution of the differential equation is $X=c_{1} \cosh \sqrt{-\lambda} x+c_{2} \sinh \sqrt{ }$ It is a straightforward exercise to check that no nontrivial solution of this form satisfy the boundary conditions. Thus there are no negative eigenvalues. $\lambda>0$, for convenience, we set $\lambda=\mu^{2}$ and find that the general solution o differential equation is
$$
X=A \cos \mu x+B \sin \mu x
$$

We now apply the boundary conditions:
$$
\begin{aligned}
X^{\prime}(0)=0 \Rightarrow B=0 \\
X(1)+X^{\prime}(1)=0 \Rightarrow A(\cos \mu-\mu \sin \mu)=0 .
\end{aligned}
$$

To ensure that we get nonzero eigenfunctions, we take $A=1$ and set
$$
\cos \mu-\mu \sin \mu=0
$$
equivalently,
$$
\cot \mu=\mu
$$

Thus the eigenvalues $\lambda=\mu^{2}$ correspond to the positive roots $\mu$ of this equa If we plot the graphs of $y=\cot \mu$ and $y=\mu$, we see that these graphs inte infinitely often (see Figure 2 for an illustration). Thus, (6) has infinitely

---

<!-- Page 16 -->

Left margin note (page 16)

340
Chapter 6
S

![](./images/b6761637-e91c-4988-8637-83a0e794256f-16_520_1022_410_647.jpg)

Figure 2 Roots of

Right margin note (page 16)

d their ow, we are
mple 4 sion of ording quation ions to

ficients

++++

turm-Liouville Theory with Engineering Applications

roots. Although we cannot compute these roots in simple form, we can fin numerical values and use them in our subsequent computations. For no denote the roots by $\mu_{1}, \mu_{2}, \ldots, \mu_{n}, \ldots$ and conclude that the eigenfunctions
$$
X=X_{n}=\cos \mu_{n} x, \quad n=1,2, \ldots .
$$

The eigenvalues are $\mu_{1}^{2}, \mu_{2}^{2}, \ldots, \mu_{n}^{2}, \ldots$.

$\cot \mu=\mu$.

EXAMPLE 5 Eigenfunction expansions
(a) Compute the first five eigenfunctions $X_{1}(x), X_{2}(x), \ldots, X_{5}(x)$ in Exa explicitly.
(b) Given $f(x)=x(1-x), 0<x<1$. What is the eigenfunction expan $f$ ? Plot $f$ and some partial sums of the eigenfunction expansion.
Solution (a) Figure 2 shows the graphs of $y=\cot \mu$ and $y=\mu$. Acc to the solution of Example 4, to find the eigenvalues, we must solve the ec $\cot \mu=\mu$. With the help of a computer system, we find the first five solut be approximately
$$
\mu_{1}=0.860, \mu_{2}=3.426, \mu_{3}=6.437, \mu_{4}=9.529, \mu_{5}=12.645 .
$$

Thus the first five eigenfunctions are
$$
\begin{array}{c}
X_{1}(x)=\cos (0.860 x), \quad X_{2}(x)=\cos (3.426 x) \\
X_{3}(x)=\cos (6.437 x), \quad X_{4}(x)=\cos (9.529 x), \quad X_{5}(x)=\cos (12.645 x)
\end{array}
$$
(b) By Theorem 3, the eigenfunction expansion of $f$ is
$$
f(x)=\sum_{j=1}^{\infty} A_{j} \cos \mu_{j} x,
$$
where
$$
A_{j}=\int_{0}^{1} x(1-x) \cos \mu_{j} x d x / \int_{0}^{1} \cos ^{2} \mu_{j} x d x
$$
with the numerical values of the $\mu_{j}$ 's given in (a). We evaluate these coef with the help of a computer and find
$$
A_{1}=.189, A_{2}=-0.032, A_{3}=-0.091, A_{4}=-0.001, A_{5}=-0.025 .
$$

---

<!-- Page 17 -->

Left margin note (page 17)

![](./images/b6761637-e91c-4988-8637-83a0e794256f-17_449_822_421_795.jpg)

Figure 3 Eigenfunction expansion of $f(x)=x(1-x)$.

Right margin note (page 17)

341
ol
can em 2
ation use
lem
of the stead,
ion of $[0, a]$
culus ver is Using

++++

Section 6.2 Sturm-Liouville Theory

Thus the eigenfunction expansion of $f$ is
$$
\begin{aligned}
f(x)= & .189 \cos (0.860 x)-0.032 \cos (3.426 x)-0.091 \cos (6.437 x) \\
& -0.001 \cos (9.529 x)-0.025 \cos (12.645 x)+\cdots
\end{aligned}
$$

As guaranteed by Theorem 3 and illustrated in Figure 3, the partial su the eigenfunction expansion converge to $f(x)$.

Further information about the eigenfunctions in Examples 4 and be obtained by quoting results from this section. For example, Theor implies the orthogonality of these eigenfunctions on the interval $(0,1)$.

The problem that we consider next arises in the solution a heat equ on a disk with Robin-type boundary conditions (Exercise 35). We wi a notation that reflects this connection with the heat equation.

EXAMPLE 6 Bessel's equation with Robin conditions
Find the eigenvalues and eigenfunctions of the singular Sturm-Liouville prob
$$
r R^{\prime \prime}+R^{\prime}+\lambda^{2} r R=0 \quad(0 \leq r<a), \quad R^{\prime}(a)=-\kappa R(a) .
$$

Here $\kappa>0$ is a heat transfer constant or coefficient, and $a>0$ is the radius disk. Note that we do not give a boundary condition at the 0 endpoint. In we usually require that the solutions be bounded in the interval $[0, a]$.
Solution We recognize the equation as a parametric form of Bessel's equat order 0 (see Theorem 3, Section 4.8). Its bounded solutions in the interval are of the form
$$
R(r)=J_{0}(\lambda r),
$$
where the eigenvalue $\lambda$ is determined from the boundary condition:
$$
R^{\prime}(a)=-\kappa R(a) \Rightarrow \lambda J_{0}^{\prime}(\lambda a)=-\kappa J_{0}(\lambda a) .
$$

Does this equation have infinitely many solutions in $\lambda$ ? Using facts from ca and properties of Bessel functions, it is not difficult to show that the ans affirmative (Exercise 36). Here we shall give an approximation of the roots. the formula $J_{0}^{\prime}(x)=-J_{1}(x)((1)$, Section 4.8), the equation becomes
$$
\lambda J_{1}(a \lambda)=\kappa J_{0}(a \lambda)
$$

---

<!-- Page 18 -->

Left margin note (page 18)

342
Chapter 6 S

The fact that the the equations $J_{0}(\lambda)$ and $-\lambda=\tan (\lambda+$ approximately equa used to estimate the ues in Example 6. I ple, by considering cal asymptotes of the can you justify the cl. for large $k, \lambda_{k} \approx \frac{\pi}{4}$

Right margin note (page 18)

$$
=\lambda_{k},
$$
ble 1.

206

$\lambda$
ling to e have pots of $\left.\frac{3 \pi}{4}\right)= \left.\lambda+\frac{\pi}{4}\right)$,
own in
Cable 1
larger larger ${ }_{0}\left(\lambda_{k} r\right)$. gure 6. olution qual to

++++

turm-Liouville Theory with Engineering Applications

The graphs in Figure 4 suggest that indeed we do have infinitely many roots $\rangle k=1,2, \ldots$. The first six of these, for the case $\kappa=a=1$, are shown in Tal

\begin{table}
| $k$ | 1 | 2 | 3 | 4 | 5 | 6 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $\lambda_{k}$ | 1.25578 | 4.07948 | 7.1558 | 10.271 | 13.3984 | 16.5312 |
\captionsetup{labelformat=empty}
\caption{Table 1. Positive roots of $\lambda J_{1}(\lambda)=J_{0}(\lambda)$.}
\end{table}
roots of $=\lambda J_{1}(\lambda) \pi / 4$ ) are $l$ can be eigenvalor examthe vertitangent, aim that, $-k \pi$ ?

![](./images/b6761637-e91c-4988-8637-83a0e794256f-57_412_463_856_24.jpg)
Figure 4

![](./images/b6761637-e91c-4988-8637-83a0e794256f-40_281_734_183_645.jpg)
Figure 5

A more accurate description of the eigenvalues can be obtained by appea the asymptotic formulas for Bessel functions (Theorem 3, Section 4.9). W $J_{0}(\lambda) \sim \sqrt{\frac{2}{\pi \lambda}} \cos \left(\lambda-\frac{\pi}{4}\right)$ and $J_{1}(\lambda) \sim \sqrt{\frac{2}{\pi \lambda}} \cos \left(\lambda-\frac{\pi}{4}-\frac{\pi}{2}\right)$. Hence the r $\lambda J_{1}(a \lambda)=\kappa J_{0}(a \lambda)$ are approximately the roots of the equation $\lambda \cos (a \lambda- \kappa \cos \left(a \lambda-\frac{\pi}{4}\right) ;$ and since $\cos \left(a \lambda-\frac{3 \pi}{4}\right)=-\cos \left(a \lambda+\frac{\pi}{4}\right)$ and $\cos \left(a \lambda-\frac{\pi}{4}\right)=\sin (a$ the equation becomes
$$
-\frac{1}{\kappa} \lambda=\tan \left(a \lambda+\frac{\pi}{4}\right) .
$$

The first six roots of this equation with $\kappa=a=1$ (denoted $\alpha_{k}$ ) are sh Table 2 (Figure 5), whose entries should be compared with the entries in ? (Figure 4):

\begin{table}
| $k$ | 1 | 2 | 3 | 4 | 5 | 6 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $\alpha_{k}$ | 1.40422 | 4.16275 | 7.20647 | 10.3069 | 13.4261 | 16.5537 |
\captionsetup{labelformat=empty}
\caption{Table 2. Positive roots of $-\lambda=\tan \left(\lambda+\frac{\pi}{4}\right)$.}
\end{table}

Because the asymptotic formulas for Bessel functions give better results for values of $\lambda$, the entries in Table 2 give a much better approximation for eigenvalues. To each eigenvalue $\lambda_{k}$ corresponds one eigenfunction $R_{k}(r)=J$ We took $\kappa=a=1$ and plotted the eigenfunctions for $k=1,2$, and 3 in Fi These should not be confused with the Bessel functions that arise from the s of the heat equation on a disk, with 0 boundary condition. The latter are e 0 when $r=a$, which is not the case with the functions shown in Figure 6.

---

<!-- Page 19 -->

Left margin note (page 19)

![](./images/b6761637-e91c-4988-8637-83a0e794256f-19_414_458_627_33.jpg)

Figure 6 Eigenfunctions in Examples 6 and 7.

Right margin note (page 19)

343
a),
ville
g to
ition
last
will y of cific with our n of ether

++++

Section 6.2 Sturm-Liouville Theory

EXAMPLE 7 Orthogonality
Show that the eigenfunctions in Example 6 are orthogonal on the interval ( 0 with respect to the weight $r$. More explicitely, show that
$$
\int_{0}^{a} J_{0}\left(\lambda_{j} r\right) J_{0}\left(\lambda_{k} r\right) r d r=0 \quad(j \neq k)
$$
where $\lambda_{k}(k=1,2, \ldots)$ are the positive roots of (7).
Solution It is enough to show that condition (4) is satisfied. The Sturm-Liou form of the equation is (recall the result of Example 1(b) with order $p=0$ ):
$$
\left[r R^{\prime}\right]^{\prime}+\lambda^{2} r R=0, \quad 0<r<a, \quad R^{\prime}(a)=-\kappa R(a) .
$$

So in (4), take $p(r)=r$ and let $y_{1}$ and $y_{2}$ be two eigenfunctions correspondin distinct eigenvalues. In our notation, (4) becomes
$$
\lim _{r \uparrow \alpha} p(r)\left(y_{1}(r) y_{2}^{\prime}(r)-y_{2}(r) y_{1}^{\prime}(r)\right)-\lim _{r \downarrow 0} p(r)\left(y_{1}(r) y_{2}^{\prime}(r)-y_{2}(r) y_{1}^{\prime}(r)\right)=0,
$$
and since $p(0)=0, p(a)=a$, and all the functions are continuous, the cond becomes
$$
a\left(y_{1}(a) y_{2}^{\prime}(a)-y_{2}(a) y_{1}^{\prime}(a)\right)=0 ; \text { equivalently, } y_{1}(a) y_{2}^{\prime}(a)-y_{2}(a) y_{1}^{\prime}(a)=0 .
$$

At the endpoint $r=a$, we have $y_{k}^{\prime}(a)=-\kappa y_{k}(a)$. So the left side of the displayed condition becomes
$$
y_{1}(a)\left(-\kappa y_{2}(a)\right)-y_{2}(a)\left(-\kappa y_{1}(a)\right)=0
$$
which is a true statement. Hence (4) holds, and by Theorem 2 the eigenfunct are orthogonal with respect to the weight $r$.

Additional properties of the eigenfunctions in Examples 6 and 7 be investigated in the exercises. In particlar, the completeness propert the eigenfunctions will be illustrated by studying the convergence of spe eigenfunction expansions.

In Section 6.4, we will study Sturm-Liouville problems associated differential equations of order 4. This generalization is motivated by later study of the vibrations of a beam which will require the solutio such problems.

Exercises 6.2
In Exercises 1-10, put the given equation in Sturm-Liouville form and decide wh the problem is regular or singular.
1. $x y^{\prime \prime}+y^{\prime}+\lambda y=0, y(0)=0, y(1)=0$.
2. $x y^{\prime \prime}+y^{\prime}+\lambda y=0, y(1)=0, y(2)=0$.
3. $x y^{\prime \prime}+2 y^{\prime}+\lambda y=0, y(1)=0, y^{\prime}(2)=0$. [Hint: Multiply by $x$.]
4. $y^{\prime \prime}+(x+\lambda) y=0, y(0)=0, y(1)=0$.

---

<!-- Page 20 -->

Left margin note (page 20)

344
Chapter 6
Sturm

Right margin note (page 20)

Sturm-
$=0$ has
$y(1)+$
$x<\pi$,
ion and
in the
enfunc-
asion of
what
enfunc-
unction
e eigen-
unction

++++

Liouville Theory with Engineering Applications
5. $x y^{\prime \prime}-y^{\prime}+\lambda x y=0, y(0)=0, y(1)=0$. [Hint: Divide by $x^{2}$.]
6. $y^{\prime \prime}+\left[\frac{1+\lambda x}{x}\right] y=0, y(1)=0, y(2)=0$.
7. $y^{\prime \prime}+\lambda x y=0, y(-1)=0, y(1)=0$.
8. $\left(1-x^{2}\right) y^{\prime \prime}-2 x y^{\prime}+(1+\lambda x) y=0, y(-1)=0, y(1)=0$.
9. $\left(1-x^{2}\right) y^{\prime \prime}-2 x y^{\prime}+\lambda y=0, y(-1)=0, y(1)=0$.
10. $y^{\prime \prime}-\frac{x}{1-x^{2}} y^{\prime}+\lambda y=0, y(-1)=0, y(1)=0$.

In Exercises 11-20, determine the eigenvalues and eigenfunctions of the given Liouville problem.
11. $y^{\prime \prime}+\lambda y=0, y(0)=0, y(2 \pi)=0$.
12. $y^{\prime \prime}+\lambda y=0, y(0)=0, y(\pi / 2)=0$.
13. $y^{\prime \prime}+\lambda y=0, y(0)=0, y^{\prime}(\pi)=0$.
14. $y^{\prime \prime}+\lambda y=0, y(-\pi)=y(\pi), y^{\prime}(-\pi)=y^{\prime}(\pi)$.
15. $y^{\prime \prime}+\lambda y=0, y(0)=0, y(\pi)+y^{\prime}(\pi)=0$.
16. $y^{\prime \prime}+\lambda y=0, y(0)+y^{\prime}(0)=0, y(2 \pi)=0$.
17. $y^{\prime \prime}+\lambda y=0, y(0)+y^{\prime}(0)=0, y(1)+y^{\prime}(1)=0$.
18. $y^{\prime \prime}+\lambda y=0, y(0)+2 y^{\prime}(0)=0, y(1)=0$.
19. $x y^{\prime \prime}+y^{\prime}+\left[-\frac{4}{x}+\lambda x\right] y=0,0<x<1, y(0)$ is finite, $y(1)=0$.
20. $x y^{\prime \prime}+y^{\prime}+\left[-\frac{1}{x}+\lambda x\right] y=0,0<x<3, y(0)$ is finite, $y(3)=0$.
21. Show that the boundary value problem $y^{\prime \prime}-\lambda y=0, y(0)=0, y(1)$ no positive eigenvalues. Does this contradict Theorem 1?
22. Show that the boundary value problem $y^{\prime \prime}-\lambda y=0, y(0)+y^{\prime}(0)=0$, $y^{\prime}(1)=0$ has one positive eigenvalue. Does this contradict Theorem 1?
23. (a) Find the eigenfunction expansion of the function $f(x)=x, 0<$ using the eigenfunctions of the Sturm-Liouville problem of Example 2.
(b) Plot the function and several partial sums of the eigenfunction expans comment on the graphs.
24. Repeat Exercise 23 with the function $f(x)=1,0<x<\pi$.
25. Repeat Exercise 23 with the function $f(x)=\sin x, 0<x<\pi$.
26. (a) Approximate the numerical values of the first eight eigenvalues Sturm-Liouville problem of Exercise 15, and describe the corresponding eig tions.
(b) Approximate the first eight nonzero terms of the eigenfunction expan $\sin x$. Plot the function and several partial sums of the expansion. Descrit is happening in the picture that you obtain.
27. Expand the function $f(x)=1,0<x<\pi$, in a series in terms of the eig tions of Exercise 26. Plot the function and the partial sums of the eigenf expansion and comment on the graphs.
28. Expand the function $f(x)=\sin \pi x, 0<x<1$, in a series in terms of th functions of Example 5. Plot the function and the partial sums of the eigenf expansion and comment on the graphs.

---

<!-- Page 21 -->

Right margin note (page 21)

345

e are $y^{\prime}(1) r(x)$. ation, The 2 and ed at with ation $n$ are only os $n \theta$. omial $2 \theta=$ gonal
1.

++++

Section 6.2 Sturm-Liouville Theory
29. Verify the orthogonality of the eigenfunctions of Exercise 11.
30. Verify numerically the orthogonality of the eigenfunctions of Example 5.
31. The second order, linear ordinary differential equation
$$
\left(1-x^{2}\right) y^{\prime \prime}-x y^{\prime}+n^{2} y=0, \quad-1<x<1,
$$
where $n=0,1,2, \ldots$, is known as Chebyshev's differential equation. W interested in solving this equation with the boundary conditions $y(1)=1$ and is finite.
(a) Put the equation in Sturm-Liouville form and determine $p(x), q(x)$, and [Hint: First, divide through by $\left(1-x^{2}\right)^{1 / 2}$.]
(b) Use the power series method, as we did in Section 5.5 with Legendre's equ and show that Chebyshev's equation has one polynomial solution of degree $n$ one that satisfies $y(1)=1$ is called the Chebyshev polynomial of degree is denoted by $T_{n}(x)$.

It is a fact that the derivative of the nonpolynomial solution is not bound $x=1$. Thus $T_{n}(x)$ is the only solution that satisfies the boundary conditions (c) Using (4), show that the Chebyshev polynomials are orthogonal on $(-1,1)$ respect to the weight function $r(x)=\frac{1}{\sqrt{1-x^{2}}}$.
32. (a) Show that the change of variables $x=\cos \theta$ transforms Chebyshev's equ into $y^{\prime \prime}+n^{2} y=0,0<\theta<\pi$.
(b) Conclude that two linearly independent solutions of Chebyshev's equatio $y_{1}(x)=y_{1}(\cos \theta)=\cos n \theta$ and $y_{2}(x)=y_{2}(\cos \theta)=\sin n \theta$
(c) Show that $y_{2}^{\prime}(x)$ is not bounded at $x=1$. Hence $y_{1}(x)=\cos n \theta$ is the solution that satisfies $y(1)=1$ and $y^{\prime}(1)$ is finite. Conclude that $T_{n}(x)=\mathrm{c}$ As you know, $\cos n \theta$ can be expressed as a polynomial in $\cos \theta$. This polyn expression is precisely $T_{n}(x)$ : for example, $T_{1}(x)=\cos \theta=x ; T_{2}(x)=\cos 2 \cos ^{2} \theta-1=2 x^{2}-1$, and so on.
(d) Find $T_{3}(x)$ and $T_{4}(x)$.
33. (a) Show that the eigenfunctions in Example 6 satisfy
$$
\int_{0}^{a}\left[J_{0}\left(\lambda_{k} r\right)\right]^{2} r d r=\frac{a^{2}}{2}\left(\left[J_{0}\left(\lambda_{k} a\right)\right]^{2}+\left[J_{1}\left(\lambda_{k} a\right)\right]^{2}\right)
$$
[Hint: Exercise 36(b), Section 4.8.]
(b) Suppose that you know that the eigenfunctions form a complete set of ortho functions on the interval $(0, a)$. Show that if
$$
f(r)=\sum_{k=1}^{\infty} A_{k} J_{0}\left(\lambda_{k} r\right) \quad(0 \leq r<a),
$$
then
$$
A_{k}=\frac{2}{a^{2}\left(\left[J_{0}\left(\lambda_{k} a\right)\right]^{2}+\left[J_{1}\left(\lambda_{k} a\right)\right]^{2}\right)} \int_{0}^{a} f(r) J_{0}\left(\lambda_{k} r\right) r d r
$$
34. Consider the eigenfunctions in the preceeding exercise, and take $a=\kappa=$ (a) Derive the following eigenfunction expansion of $f(r)=100$ for $0 \leq r<1$ :
$$
100=200 \sum_{k=1}^{\infty} \frac{J_{1}\left(\lambda_{k}\right)}{\lambda_{k}\left(\left[J_{0}\left(\lambda_{k}\right)\right]^{2}+\left[J_{1}\left(\lambda_{k}\right)\right]^{2}\right)} J_{0}\left(\lambda_{k} r\right)
$$

---

<!-- Page 22 -->

Left margin note (page 22)

346
Chapter 6
St
6.3 The Ha

![](./images/b6761637-e91c-4988-8637-83a0e794256f-22_424_419_1569_58.jpg)

Figure 1 Hanging

Right margin note (page 22)

proxirgence tions. disk of indary
lateral a rate nstant
istinct $h\left(a \lambda_{2}\right)$ values ns.]
$$
(a \lambda)+
$$
illusThis f parDaniel k the all the Bessel
in, we chain The value

++++

urm-Liouville Theory with Engineering Applications
(b) Show that $J_{1}\left(\lambda_{k}\right)=\frac{J_{0}\left(\lambda_{k}\right)}{\lambda_{k}}$ and conclude that $0 \leq r<1$ :
$$
100=200 \sum_{k=1}^{\infty} \frac{J_{0}\left(\lambda_{k}\right)}{\left(1+\lambda_{k}^{2}\right)\left[J_{0}\left(\lambda_{k}\right)\right]^{2}} J_{0}\left(\lambda_{k} r\right) .
$$
(c) Use the numerical values from Table 1 to obtain a six-term partial sum ap mation of the function in part (b). Plot this partial sum to illustrate the conve of the eigenfunction expansion.
35. Project Problem: Heat problem on a disk with Robin condi Use the method of separation of variable to solve the heat equation on a unit radius
$$
\frac{\partial u}{\partial t}=\frac{\partial^{2} u}{\partial r^{2}}+\frac{1}{r} \frac{\partial u}{\partial r}, \quad 0 \leq r<1, t>0,
$$
with initial temperature distribution $u(r, 0)=100(0 \leq r<1)$, and Robin bot condition
$$
\left.\frac{\partial u}{\partial r}(r, t)\right|_{r=1}=-u(1, t) .
$$

The problem models the temperature distribution in a plate with insulated surface, whose boundary is exchanging heat with the surrounding medium at proportional to the temperature at the boundary. Here the heat transfer co or convection constant $\kappa$ is equal to 1 .
36. Fix $a, \kappa>0$ and let $h(\lambda)=\kappa J_{0}(a \lambda)+\lambda J_{0}^{\prime}(a \lambda)$, and $\lambda_{1}$ and $\lambda_{2}$ be two d consecutive zeros of $J_{0}(a \lambda)$ such that $0<\lambda_{1}<\lambda_{2}$.
(a) Show that $h\left(\lambda_{1}\right)=\lambda_{1} J_{0}^{\prime}\left(a \lambda_{1}\right), h\left(\lambda_{2}\right)=\lambda_{2} J_{0}^{\prime}\left(a \lambda_{2}\right)$ and that $h\left(a \lambda_{1}\right)$ and have opposite signs. [Hint: Since $\lambda_{1}, \lambda_{2}>0$, it is enough to argue that the of the derivative of $J_{0}$ at two consecutive roots of $J_{0}$ must have opposite sig
(b) Conclude that $h(a \lambda)=0$ for some $\lambda_{3}$ in the interval $\left(\lambda_{1}, \lambda_{2}\right)$.
(c) Using the fact that $J_{0}(a \lambda)$ has infinitely many positive zeros, show that $\kappa J_{0} J_{0}^{\prime}(a \lambda)=0$ has infinitely many positive roots.
nging Chain
Having studied Sturm-Liouville theory for second order equations, we trate the theory as it applies to the oscillations of the hanging chain. problem played an important role in the development of the theory o tial differential equations. It was while solving this problem that I Bernoulli first discovered Bessel functions in 1732. Although we lir solution to general Sturm--Liouville theory, our presentation contains necessary details to solve this problem based on the properties of functions from Section 4.8.

To describe the equation governing the motion of the hanging cha hain. place the $x$-axis in a vertical position, pointing upward. Consider a of length $L$, hanging down with one end fastened at $x=L$ (Figure 1). small transverse oscillations of the chain are described by the boundary

---

<!-- Page 23 -->

Left margin note (page 23)

Physically, another boundary condition that should be applied is $u(0, t)$ finite for all $t>$ 0 . This condition states that the vibrations of the free end remain bounded. It will be needed to rule out unbounded solutions.

Here we have reversed our usual procedure in that we have argued on physical grounds that only negative values of the separating constant lead to nontrivial solutions.

Right margin note (page 23)

347
of
in
sing
the
ging
side
ce to
the
near
tical
nply

++++

Section 6.3 The Hanging Chain

problem
$$
\begin{array}{l}
\frac{\partial^{2} u}{\partial t^{2}}=g\left[x \frac{\partial^{2} u}{\partial x^{2}}+\frac{\partial u}{\partial x}\right], \quad 0<x<L, t>0 \\
u(L, t)=0, \quad t>0 \\
u(x, 0)=f(x), \quad u_{t}(x, 0)=v(x)
\end{array}
$$

Here $g$ is the gravitational acceleration, $f(x)$ is the initial displacemer the chain, and $v(x)$ its initial velocity. The derivation of (1) is outline Exercise 6, Section 3.2. We will solve this boundary value problem $u$ separation of variables. The method will lead to Bessel's equation, and solution will involve a form of Bessel series.

Separation of Variables
We assume a product solution of the form $u(x, t)=X(x) T(t)$. Plug this into (1) and separating the variables, we get
$$
\begin{array}{c}
X T^{\prime \prime}=g T\left(x X^{\prime \prime}+X^{\prime}\right), \\
\frac{1}{g} \frac{T^{\prime \prime}}{T}=\frac{x X^{\prime \prime}+X^{\prime}}{X} .
\end{array}
$$

Since the variables are separated, for the last equality to hold, each must be equal to a constant. Thus
$$
\frac{1}{g} \frac{T^{\prime \prime}}{T}=\lambda \quad \text { and } \quad \frac{x X^{\prime \prime}+X^{\prime}}{X}=\lambda
$$

The boundary condition implies that $T(t) X(L)=0$ for all $t>0$. Hend avoid the trivial solution, we require that $X(L)=0$. Thus we arrive at equations
$$
T^{\prime \prime}-\lambda g T=0 \quad \text { and } \quad x X^{\prime \prime}+X^{\prime}-\lambda X=0, \quad X(L)=0
$$

Solving the Separated Equations
If $\lambda \geq 0$, the solutions of the differential equation in $T$ are either li or exponential functions. We discard these solutions for obvious prac reasons. Thus $\lambda$ must be negative. To simplify notation, we will sir replace $\lambda$ in the equations by $-\lambda^{2}$ and get
$$
T^{\prime \prime}+\lambda^{2} g T=0
$$
and
$$
x X^{\prime \prime}+X^{\prime}+\lambda^{2} X=0, \quad X(L)=0
$$

---

<!-- Page 24 -->

Left margin note (page 24)

348
Chapter 6
Sturm-Liou

Right margin note (page 24)

iew of equa-

0, and ngular finitely s, and, nctions 11 then roblem many e since change
(Thelutions 0) and
these to the ad (12)

++++

ille Theory with Engineering Applications

The general solution of (2) is
$$
T(t)=A \cos (\sqrt{g} \lambda t)+B \sin (\sqrt{g} \lambda t) .
$$

Next we consider the differential equation in $X$ from the point of Sturm-Liouville theory. By rewriting (3), we see that the differentia tion can be put in the Sturm-Liouville form
$$
\left(x X^{\prime}\right)^{\prime}+\lambda^{2} X=0 .
$$

Comparing this to (1) from Section 6.2, we find that $p(x)=x, q(x)= r(x)=1$ and also that $a=0$ and $b=L$. Since $p(0)=0$, this is a si Sturm-Liouville problem. We will show that this problem has in many eigenvalues and a corresponding complete set of eigenfunction by Theorem 2(b) of the previous section, it follows that these eigenfur are orthogonal with respect to the weight function $r(x)=1$. It wi follow that we can construct the solution $u(x, t)$ to the hanging chain p by superposing the corresponding product solutions, as we have done times before.

In this particular example it is possible to be much more concret (3) is closely related to Bessel's equation. To see this, we make the of variables $s=2 \sqrt{x}$. Using the chain rule, we verify that
$$
\begin{array}{c}
X^{\prime}=\frac{d X}{d x}=\frac{d X}{d s} \frac{1}{\sqrt{x}} ; \\
X^{\prime \prime}=\frac{d^{2} X}{d x^{2}}=\frac{1}{x} \frac{d^{2} X}{d s^{2}}-\frac{1}{2 x^{3 / 2}} \frac{d X}{d s} .
\end{array}
$$

Substituting in (3) and simplifying, we get
$$
s^{2} \frac{d^{2} X}{d s^{2}}+s \frac{d X}{d s}+\lambda^{2} s^{2} X=0 \quad X(2 \sqrt{L})=0
$$
which is precisely the parametric form of Bessel's equation of order C orem 3, Section 4.8). Since we are only interested in the bounded so of this equation, we can apply Theorem 3 of Section 4.8 (with $p=$ obtain that
$$
\lambda=\lambda_{j}=\frac{\alpha_{j}}{2 \sqrt{L}}, \quad \text { and } \quad X(s)=X_{j}(s)=J_{0}\left(\frac{\alpha_{j}}{2 \sqrt{L}} s\right) \text {, }
$$
where $j=1,2,3, \ldots$, and $\alpha_{j}$ denotes the $j$ th zero of $J_{0}$. Moreover functions are orthogonal on the interval $0 \leq s \leq 2 \sqrt{L}$ with respect weight function $s$. The orthogonality relations expressed by (11) an of Section 4.8 (with $a=2 \sqrt{L}$ ) become
$$
\int_{0}^{2 \sqrt{L}} J_{0}\left(\frac{\alpha_{j}}{2 \sqrt{L}} s\right) J_{0}\left(\frac{\alpha_{k}}{2 \sqrt{L}} s\right) s d s=0, \quad j \neq k
$$

---

<!-- Page 25 -->

Left margin note (page 25)

SNOILONAANAYIA HO
XLITVNO OPOHLYO

Right margin note (page 25)

349

that on is
hain.
tain

++++

Section 6.3 The Hanging Chain

and
$$
\int_{0}^{2 \sqrt{L}} J_{0}^{2}\left(\frac{\alpha_{j}}{2 \sqrt{L}} s\right) s d s=2 L J_{1}^{2}\left(\alpha_{j}\right), \quad j=1,2, \ldots
$$

Substituting $s=2 \sqrt{x}$ back into (5), (6), and (7), we find the solutions
$$
X_{j}(2 \sqrt{x})=J_{0}\left(\alpha_{j} \sqrt{\frac{x}{L}}\right), \quad j=1,2,3, \ldots,
$$
and their orthogonality relations
$$
\begin{array}{c}
\int_{0}^{L} J_{0}\left(\alpha_{j} \sqrt{\frac{x}{L}}\right) J_{0}\left(\alpha_{k} \sqrt{\frac{x}{L}}\right) d x=0, \quad j \neq k \\
\frac{1}{L J_{1}^{2}\left(\alpha_{j}\right)} \int_{0}^{L} J_{0}^{2}\left(\alpha_{j} \sqrt{\frac{x}{L}}\right) d x=1, \quad j=1,2, \ldots
\end{array}
$$

Having solved the equation in $X$, we combine (4) and (8) and conclude a product solution of (1) satisfying the accompanying boundary conditi
$$
u_{j}(x, t)=J_{0}\left(\alpha_{j} \sqrt{\frac{x}{L}}\right)\left[A_{j} \cos \left(\sqrt{\frac{g}{L}} \frac{\alpha_{j}}{2} t\right)+B_{j} \sin \left(\sqrt{\frac{g}{L}} \frac{\alpha_{j}}{2} t\right)\right] .
$$

The functions $u_{j}(j=1,2, \ldots)$ are called the normal modes of the c For $j=1$ we get the fundamental mode of the chain. From (9), we ob the frequency of the $j$ th normal mode
$$
\nu_{j}=\frac{\alpha_{j}}{4 \pi} \sqrt{\frac{g}{L}} .
$$

Bessel Series Solution of the Entire Problem
By superposing all the product solutions, we get
$$
u(x, t)=\sum_{j=1}^{\infty} J_{0}\left(\alpha_{j} \sqrt{\frac{x}{L}}\right)\left[A_{j} \cos \left(\sqrt{\frac{g}{L}} \frac{\alpha_{j}}{2} t\right)+B_{j} \sin \left(\sqrt{\frac{g}{L}} \frac{\alpha_{j}}{2} t\right) .\right.
$$

Setting $t=0$ and using the initial condition, we find that
$$
f(x)=u(x, 0)=\sum_{j=1}^{\infty} A_{j} J_{0}\left(\alpha_{j} \sqrt{\frac{x}{L}}\right) .
$$

---

<!-- Page 26 -->

Left margin note (page 26)

350
Chapter 6 S

![](./images/b6761637-e91c-4988-8637-83a0e794256f-26_419_435_1676_52.jpg)

Figure 2 Initial sha chain.

Right margin note (page 26)

$\left.k \sqrt{\frac{\underline{x}}{L}}\right)$ nality we get
$$
v(x) .
$$
$$
\text { to } x
$$
itions.
of the ed (see
$$
=9.8
$$
$x, t$ ) at
graphs of the

Hence,
$$
\frac{\alpha_{2}}{4 \pi} \sqrt{g} .
$$

++++

turm-Liouville Theory with Engineering Applications

To determine the $A_{j}$ 's we multiply both sides of the equality by $J_{0}(\alpha$ and then integrate with respect to $x$ from 0 to $L$. By the orthogo relations, all the terms with $j \neq k$ are equal to zero, and when $j=k$
$$
A_{j}=\frac{1}{L J_{1}^{2}\left(\alpha_{j}\right)} \int_{0}^{L} f(x) J_{0}\left(\alpha_{j} \sqrt{\frac{x}{L}}\right) d x, \quad j=1,2, \ldots
$$

To determine $B_{j}$ we proceed in a similar way using the initial velocity Differentiating $u$ with respect to $t$ and then setting $t=0$, we get
$$
v(x)=u_{t}(x, 0)=\sum_{j=1}^{\infty} B_{j} \sqrt{\frac{g}{L}} \frac{\alpha_{j}}{2} J_{0}\left(\alpha_{j} \sqrt{\frac{x}{L}}\right) .
$$

Multiplying both sides by $J_{0}\left(\alpha_{k} \sqrt{\frac{x}{L}}\right)$ and then integrating with respec from 0 to $L$, the orthogonality properties yield
$$
B_{j}=\frac{2}{\alpha_{j} J_{1}^{2}\left(\alpha_{j}\right)} \frac{1}{\sqrt{g L}} \int_{0}^{L} v(x) J_{0}\left(\alpha_{j} \sqrt{\frac{x}{L}}\right) d x, \quad j=1,2, \ldots
$$

This completely determines the solution in terms of the initial cond We illustrate this solution with a numerical example.

EXAMPLE 1 Vibrating chain
A chain of length 1 meter is hanging from one end. An initial displacement chain is done by pulling the center .005 m while keeping the lower end fix Figure 2). The chain is then left to vibrate freely.
(a) What are the frequencies of the first three normal modes? (Take $g \mathrm{m} / \mathrm{sec}^{2}$.)
(b) Plot the graphs of the first three normal modes $u_{1}(x, t), u_{2}(x, t), u_{3}( t=0$.
(c) Determine the motion of the chain by finding $u(x, t)$.
(d) Approximate the solution with three terms of the series and plot the of the approximating function at various values of $t$ to illustrate the motion chain.

-x)

Solution (a) Note that $B_{j}=0$ for all $j$ because the initial velocity is zero. from (9), the $j$ th normal mode is
$$
u_{j}(x, t)=A_{j} J_{0}\left(\alpha_{j} \sqrt{x}\right) \cos \left(\sqrt{9.8} \frac{\alpha_{j}}{2} t\right),
$$
where $\alpha_{j}$ is the $j$ th zero of $J_{0}$. The frequency of the $j$ th normal mode is $\nu_{j}=$ Using the numerical values of $\alpha_{j}$ from Table 1 below, we find

ape of the
$$
\nu_{1}=.5990, \quad \nu_{2}=1.375, \quad \nu_{3}=2.1558 .
$$

---

<!-- Page 27 -->

Left margin note (page 27)

![](./images/b6761637-e91c-4988-8637-83a0e794256f-27_320_1173_382_587.jpg)

Figure 3 Normal modes of the chain.

Right margin note (page 27)

351
$$
\sqrt{x}),
$$
s , we

c)
$$
\overrightarrow{1}
$$
laced mple ained
al to ation
stituuter. gging

++++

Section 6.3 The Hanging Chain
(b) At time $t=0$ we have $u_{1}(x, 0)=A_{1} J_{0}(2.4048 \sqrt{x}), u_{2}(x, 0)=A_{2} J_{0}(5.5201$ and $u_{3}(x, 0)=A_{3} J_{0}(8.6537 \sqrt{x})$. To illustrate the shape of the normal mode set the $A_{j}$ 's equal to 1 and plot the corresponding graphs (Figure 3).

Note how the fundamental mode looks like a chain whose free end is disp from its equilibrium position. The other modes correspond to other possible si motions of the chain. And, as seen from (10), the motion of the chain is obt by superposing these special modes of vibration.
(c) The function $u(x, t)$ is given by (10), where the coefficients $B_{j}$ are all equ 0 . It remains to compute the $A_{j}$ 's. For this purpose, we use (11) and the equ of the initial displacement $f(x)$ given in Figure 2. We get
$$
A_{j}=\frac{1}{J_{1}^{2}\left(\alpha_{j}\right)}\left[\int_{0}^{1 / 2} \frac{1}{100} x J_{0}\left(\alpha_{j} \sqrt{x}\right) d x+\int_{1 / 2}^{1} \frac{1}{100}(1-x) J_{0}\left(\alpha_{j} \sqrt{x}\right) d x\right]
$$

These integrals are computed with the help of the following identities:
$$
\begin{array}{c}
\int x J_{0}\left(\alpha_{j} \sqrt{x}\right) d x=\frac{2}{\alpha_{j}} x^{3 / 2} J_{1}\left(\alpha_{j} \sqrt{x}\right)-\frac{4}{\alpha_{j}^{2}} x J_{2}\left(\alpha_{j} \sqrt{x}\right)+C \\
\int J_{0}\left(\alpha_{j} \sqrt{x}\right) d x=\frac{2}{\alpha_{j}} x^{1 / 2} J_{1}\left(\alpha_{j} \sqrt{x}\right)+C
\end{array}
$$
which can be derived from (7), Section 4.8 (with $p=0$ ), after making the subs tion $t=\alpha_{j} \sqrt{x}$. Applying these formulas and simplifying, we get
$$
A_{j}=\frac{J_{2}\left(\alpha_{j}\right)-J_{2}\left(\alpha_{j} / \sqrt{2}\right)}{25 \alpha_{j}^{2} J_{1}^{2}\left(\alpha_{j}\right)} .
$$

Numerical values of the $A_{j}$ 's can be approximated with the help of a comp They are presented Table 1 along with other pertinent numerical data. Plu the numerical data into (10), we get
$$
\begin{array}{c}
u(x, t)=0.003847 J_{0}(2.4048 \sqrt{x}) \cos (3.76415 t)-0.005787 J_{0}(5.52008 \sqrt{x}) \\
\times \cos (8.64029 t)+0.002371 J_{0}(8.65373 \sqrt{x}) \cos (13.5452 t)-\cdots
\end{array}
$$

\begin{table}
| $j$ | 1 | 2 | 3 |
| :---: | :---: | :---: | :---: |
| $\alpha_{j}$ | 2.40483 | 5.52008 | 8.65373 |
| $\nu_{j}$ | .5990 | 1.375 | 2.1558 |
| $A_{j}$ | .003847 | -.005787 | .002371 |
\captionsetup{labelformat=empty}
\caption{Table 1 Numerical data for Example 1.}
\end{table}

---

<!-- Page 28 -->

Left margin note (page 28)

354
Chapter 6

THEC
EIGENFUN
EXPAN

Right margin note (page 28)

unction
points
n
$X_{2}(x)$,
he first is of its
xample
0 , so as $\alpha^{4}$,
e given
differ-
o funcditions,
ast two

++++

turm-Liouville Theory with Engineering Applications
REM 2
CTION
NSIONS

If $f$ is piecewise smooth on the interval $[a, b]$, then we have the eigenf expansion
$$
f(x)=\sum_{j=1}^{\infty} A_{j} X_{j}(x)
$$
where
$$
A_{j}=\frac{\int_{a}^{b} f(x) X_{j}(x) r(x) d x}{\int_{a}^{b} X_{j}^{2}(x) r(x) d x}
$$

For $a<x<b$, the eigenfunction expansion converges to $f(x)$ at the of continuity, and otherwise it converges to $\frac{f(x+)+f(x-)}{2}$.

EXAMPLE 1 A fourth-order Sturm-Liouville problem
(a) Find the eigenvalues and eigenfunctions of the Sturm-Liouville problen
$$
\begin{array}{c}
X^{(4)}-\lambda X=0, \\
X(0)=0, \quad X^{\prime}(0)=0, \quad X(L)=0, X^{\prime}(L)=0 .
\end{array}
$$
(Here $L$ is a positive constant and stands for the length of a bar.)
(b) Take $L=1$ and compute explicitly the first five eigenfunctions $X_{1}(x)$, $X_{3}(x), X_{4}(x), X_{5}(x)$.
(c) Given $f(x)=\sin ^{2} \pi x, 0<x<1$, approximate the numerical values of t five terms of the eigenfunction expansion of $f$. Plot $f$ and some partial sum eigenfunction expansion.
Solution Note that this problem is of the form (1)-(2). We will show in E 2 below that in this kind of problem nontrivial solutions occur only if $\lambda$ we focus exclusively on that case here. For $\lambda>0$ we write the parameter $\lambda$ with $\alpha>0$, to simplify the computations. The characteristic equation of th differential equation is
$$
r^{4}-\alpha^{4}=0, \quad \text { or } \quad\left(r^{2}-\alpha^{2}\right)\left(r^{2}+\alpha^{2}\right)=0
$$

The characteristic roots are $r= \pm \alpha, \pm i \alpha$, and so the general solution of the ential equation is
$$
X=A \cosh \alpha x+B \sinh \alpha x+C \cos \alpha x+D \sin \alpha x .
$$

To determine the eigenvalues and eigenfunctions, we must find all the nonzer tions of the form (3) that satisfy the boundary conditions. Using these con we see that
$$
\begin{array}{r}
A+C=0, B+D=0 \\
A \cosh \alpha L+B \sinh \alpha L+C \cos \alpha L+D \sin \alpha L=0 \\
A \sinh \alpha L+B \cosh \alpha L-C \sin \alpha L+D \cos \alpha L=0
\end{array}
$$

The first two equations imply that $A=-C, B=-D$. Substituting in the 1 equations gives
$$
\left\{\begin{array}{l}
A(\cosh \alpha L-\cos \alpha L)+B(\sinh \alpha L-\sin \alpha L)=0 \\
A(\sinh \alpha L+\sin \alpha L)+B(\cosh \alpha L-\cos \alpha L)=0
\end{array}\right.
$$

---

<!-- Page 29 -->

Left margin note (page 29)

![](./images/b6761637-e91c-4988-8637-83a0e794256f-29_273_396_271_38.jpg)

Figure 1

Right margin note (page 29)

355

zero.

$\cos L \alpha$
, ...,
rma-
hogo-
on
erical
$0 x)$ ),
$08 x)$ ),
c),
c),
c).
clude
mpute
this

++++

Section 6.4 Fourth-Order Sturm-Liouville Theory

For this system to have nonzero solutions $A$ and $B$ its determinant must be In this case, $A$ can assume any value and
$$
B=-A \frac{\cosh \alpha L-\cos \alpha L}{\sinh \alpha L-\sin \alpha L} .
$$

Computing the determinant and setting it to zero, we arrive at the equation
$$
\cosh \alpha L \cos \alpha L=1, \quad \text { or } \quad \cos \alpha L=\frac{1}{\cosh \alpha L}
$$

Thus the admissible values of $\alpha$ are the roots of this equation. The graphs of c and $1 / \cosh L \alpha$ in Figure 1 show that there are infinitely many roots $\alpha_{1}, \alpha_{2} \alpha_{n}, \ldots$. For each value of $\alpha_{n}$ we take $A=1$; it then follows that
$$
C=-1, \quad B=-\frac{\cosh \alpha_{n} L-\cos \alpha_{n} L}{\sinh \alpha_{n} L-\sin \alpha_{n} L}, \quad D=-B .
$$

The corresponding eigenfunctions are obtained from (3):
$$
X_{n}(x)=\cosh \alpha_{n} x-\cos \alpha_{n} x-\frac{\cosh \alpha_{n} L-\cos \alpha_{n} L}{\sinh \alpha_{n} L-\sin \alpha_{n} L}\left(\sinh \alpha_{n} x-\sin \alpha_{n} x\right) .
$$

Although the eigenfunctions have a complicated form, we can get valuable info tion about them by simply appealing to Theorem 1. For example, their ort nality on the interval $[0, L]$ is guaranteed by this theorem.
(b) We take $L=1$ and compute the first five positive roots of the equati
$$
\cos \alpha=\frac{1}{\cosh \alpha}
$$
with the help of a computer algebra system. These and other relevant num values are shown in Table 1.

\begin{table}
| $n$ | 1 | 2 | 3 | 4 | 5 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $\alpha_{n}$ | 4.7300 | 7.8532 | 10.9956 | 14.1372 | 17.2788 |
| $\frac{\cosh \alpha_{n}-\cos \alpha_{n}}{\sinh \alpha_{n}-\sin \alpha_{n}}$ | .9825 | 1.0008 | 1.0000 | 1.0000 | 1.0000 |
\captionsetup{labelformat=empty}
\caption{Table 1 Numerical data for Example 1.}
\end{table}

Thus the first five eigenfunctions are
$$
\begin{array}{l}
X_{1}(x)=\cosh (4.7300 x)-\cos (4.7300 x)+.9825(\sin (4.7300 x)-\sinh (4.730 \\
X_{2}(x)=\cosh (1.0008 x)-\cos (1.0008 x)+1.0008(\sin (1.0008 x)-\sinh (1.00 \\
X_{3}(x)=\cosh (10.9956 x)-\cos (10.9956 x)+\sin (10.9956 x)-\sinh (10.9956 x \\
X_{4}(x)=\cosh (14.1372 x)-\cos (14.1372 x)+\sin (14.1372 x)-\sinh (14.1372 x \\
X_{5}(x)=\cosh (17.2788 x)-\cos (17.2788 x)+\sin (17.2788 x)-\sinh (17.2788 x
\end{array}
$$

Note that without computing the inner product $\int_{0}^{1} X_{m}(x) X_{n}(x) d x$ we can con from Theorem 1 that it is 0 when $m \neq n$.
(c) To find the eigenfunction expansion of $f(x)=\sin ^{2} \pi x$, we must con the numerical values of the coefficients in the series $\sum_{j=1}^{\infty} A_{j} X_{j}(x)$. We do

---

<!-- Page 30 -->

Left margin note (page 30)

356
Chapter 6

![](./images/b6761637-e91c-4988-8637-83a0e794256f-30_544_991_747_641.jpg)

Figure 2 The par of the eigenfunctior sion with three nonz yields a very good mation of $f$ over t val $(0,1)$. This is in Figure 2, which sl the graphs of $f$ and t, sum are very close ov terval $(0,1)$.

Right margin note (page 30)

sing a
ansion ted by
hould is of a point, e.

s

d by
uation orward initial that $\lambda$

++++

urm-Liouville Theory with Engineering Applications

for the first five terms using the explicit formulas for the $X_{j}$ 's from (b). computer algebra system, we find
$$
A_{1}=\frac{\int_{0}^{1} \sin ^{2} \pi x X_{1}(x) d x}{\int_{0}^{1} X_{1}^{2}(x) d x}=.612, \quad A_{2}=\frac{\int_{0}^{1} \sin ^{2} \pi x X_{2}(x) d x}{\int_{0}^{1} X_{2}^{2}(x) d x}=0 .
$$

Similarly, we find
$$
A_{3}=-.022, A_{4}=0, A_{5}=-.002 .
$$

Thus
$$
f(x)=.612 X_{1}(x)-.022 X_{3}(x)-.002 X_{5}(x)+\cdots .
$$

In Figure 2 we plotted $f$ and the fifth partial sum of the eigenfunction $\exp .612 X_{1}-.022 X_{3}-.002 X_{5}$. The graphs show clearly that $f$ is approxima its eigenfunction expansion.
tial sum n expanero terms approxihe intervidenced hows that he partial er the in-

We next show that the eigenvalues in Example 1 are positive. You s note that while the proof uses the equation and the given conditions, it general nature and can be used with other problems. To illustrate this we give another set of conditions for which the eigenvalues are positiv

EXAMPLE 2 Sturm-Liouville problems with positive eigenvalue
(a) Show that the eigenvalues of the Sturm-Liouville problem
$$
\begin{array}{c}
X^{(4)}-\lambda X=0 \\
X(0)=0, \quad X^{\prime}(0)=0, \quad X(L)=0, \quad X^{\prime}(L)=0
\end{array}
$$
are positive.
(b) Show that the conclusion of (a) holds if the initial conditions are replace
$$
X(0)=0, X^{\prime \prime}(0)=0, \quad X(L)=0, X^{\prime \prime}(L)=0 .
$$

Proof We solve (a) and (b) simultaneously. The case $\lambda=0$ leads to the eq $X^{(4)}=0$, whose general solution is a polynomial of degree 3 . It is straightf to show that in this case the zero polynomial is the only one that satisfies the conditions (Exercise 17). Hence $\lambda=0$ is not an eigenvalue. We now show

---

<!-- Page 31 -->

Right margin note (page 31)

357
value
tions
left
nneg-
Also,
urm--

using
sums
urm-
erent
mply
lated
esult

++++

Section 6.4 Fourth-Order Sturm-Liouville Theory

must be $>0$. Suppose that $X$ is an eigenfunction corresponding to the eigen $\lambda$. Then
$$
\begin{aligned}
X^{(4)}-\lambda X=0 & \Rightarrow X^{(4)}=\lambda X \\
& \Rightarrow X X^{(4)}=\lambda X^{2} \quad \text { (multiply both sides by } X \text { ) } \\
& \Rightarrow \int_{0}^{L} X(x) X^{(4)}(x) d x=\lambda \int_{0}^{L} X^{2}(x) d x
\end{aligned}
$$

Integrating the left side of the last equation by parts and using the initial condi $X(0)=0, X(L)=0$, we obtain
$$
-\int_{0}^{L} X^{\prime}(x) X^{(3)}(x) d x=\lambda \int_{0}^{L} X^{2}(x) d x
$$

Integrating the left side once more by parts, we obtain
$$
-\left.X^{\prime}(x) X^{\prime \prime}(x)\right|_{0} ^{L}+\int_{0}^{L} X^{\prime \prime}(x)^{2} d x=\lambda \int_{0}^{L} X^{2}(x) d x
$$

Note that the initial conditions in (a) or (b) imply that the first term on th side is 0 . Thus
$$
\int_{0}^{L} X^{\prime \prime}(x)^{2} d x=\lambda \int_{0}^{L} X^{2}(x) d x
$$

Now $X$ is not identically zero (by definition of an eigenfunction). So $X^{2}$ is no ative and not identically zero on the interval $(0, L)$. Hence $\int_{0}^{L} X^{2}(x) d x>0$. $\int_{0}^{L} X^{\prime \prime}(x)^{2} d x \geq 0$, and so $\lambda \geq 0$. But $\lambda \neq 0$, hence $\lambda>0$.

Exercises 6.4
In Exercises 1-2, find the eigenvalues and eigenfunctions of the given St Liouville problem.
1. $X^{(4)}-\alpha^{4} X=0, X(0)=0, X^{\prime}(0)=0, X(2)=0, X^{\prime}(2)=0$.
2. $X^{(4)}-\alpha^{4} X=0, X(-1)=0, X^{\prime}(-1)=0, X(1)=0, X^{\prime}(1)=0$.
[Hint: Reduce to Exercise 1 by a change of variables.]
In Exercises 3-6, (a) find the eigenfunction expansion of the given function the prescribed set of eigenfunctions. (b) Plot the function and several partial of the eigenfunction expansion.
3. $f(x)=x(2-x), 0<x<2$; use the eigenfunctions of Exercise 1.
4. $f(x)=\sin \pi x, 0<x<2$; use the eigenfunctions of Exercise 1.
5. $f(x)=x(1-x), 0<x<1$; use the eigenfunctions of Example 1.
6. $f(x)=x^{2}(1-x)^{2}, 0<x<1$, use the eigenfunctions of Example 1.

Project Problem: In Exercise 7, you are asked to solve a fourth-order St Liouville problem dealing with the same equation as Example 1 but with diff boundary conditions. This variation on Example 1 arises in the study of si supported beams (see Section 6.5). Do also Exercise 8 to experiment with a re eigenfunction expansion. Model your solution after Example 1 and use the of Example 2.

---

<!-- Page 32 -->

Left margin note (page 32)

358
Chapter 6 Sturm

Right margin note (page 32)

anctions oblem
in Ex-
ction of
diouville
ction of sure to

Sturm-
n eigen-

11, you nich the ould do ansions.
root of sely the

++++

Liouville Theory with Engineering Applications
7. (a) Show that the eigenvalues $\lambda$ of
$$
\begin{array}{c}
X^{(4)}-\lambda X=0 \\
X(0)=0, X^{\prime \prime}(0)=0, X(L)=0, X^{\prime \prime}(L)=0
\end{array}
$$
are $\lambda_{n}=\frac{n^{4} \pi^{4}}{L^{4}}, n=1,2, \ldots$
(b) Obtain the eigenfunctions $X_{n}(x)=\sin \frac{n \pi}{L} x$. Observe that the eigenfu are exactly what you would obtain in the second-order Sturm-Liouville pro
$$
X^{\prime \prime}+\mu X=0, \quad X(0)=0, \quad X(L)=0,
$$
and the eigenvalues are related by $\lambda=\mu^{2}$. This connection is investigated ercises 9 and 10 below.
8. Take $L=1$ in Exercise 7 and find the eigenfunction expansion of
$$
f(x)=\left\{\begin{array}{ll}
x & 0<x<\frac{1}{2}, \\
1-x & \frac{1}{2}<x<1 .
\end{array}\right.
$$
9. Assume that $\mu$ and $X$ are an eigenvalue and a corresponding eigenfun the Sturm-Liouville problem
$$
X^{\prime \prime}+\mu X=0, \quad X(0)=0, \quad X(L)=0 .
$$

Differentiate twice to see that $X$ also satisfies the fourth-order Sturm-L problem
$$
\begin{array}{c}
X^{(4)}-\lambda X=0 \\
X(0)=0, X^{\prime \prime}(0)=0, X(L)=0, X^{\prime \prime}(L)=0 .
\end{array}
$$
[Hint: Use the equation $X^{\prime \prime}=-\mu X$.]
10. Assume that $\lambda$ and $X$ are an eigenvalue and a corresponding eigenfun the fourth-order Sturm-Liouville problem in Exercise 9.
(a) Show that $Y=X^{\prime \prime}$ is also an eigenfunction of the same problem. (Be check the boundary conditions.)
(b) Show that the function $u=\alpha^{2} X-Y$ is a solution to the second-order Liouville problem in Exercise 9 for the eigenvalue $\alpha^{2}$, where $\lambda=\alpha^{4}$.
(c) By using the explicit form $X=\sin \alpha x$, conclude from (b) that $u$ is a function of the second-order Sturm-Liouville problem.

Project Problem: Eigenvalues with multiplicity two. In Exercise are asked to develop the solutions of a fourth-order Sturm-Liouville in wl first eigenvalue has multiplicity two. In addition to Exercise 11, you sh one of Exercises 12 or 13 to experiment with the related eigenfunction exp Model your solution after Example 1.
11. (a) Show that the eigenvalues $\lambda$ of
$$
\begin{array}{c}
X^{(4)}-\lambda X=0 \\
X^{\prime \prime}(0)=0, X^{\prime \prime \prime}(0)=0, X^{\prime \prime}(L)=0, X^{\prime \prime \prime}(L)=0
\end{array}
$$
are $\lambda_{1}=0, \lambda_{2}=0$, and all values of the form $\lambda=\alpha^{4}$, where $\alpha$ is a positive $\cosh \alpha L \cos \alpha L=1$. Note that, aside from the eigenvalue 0 , these are preci

---

<!-- Page 33 -->

Right margin note (page 33)

359

does ution em of g the funcof the everal
prob6.5). with
$$
=-1 .
$$
funcof the everal of the etions
$$
{ }_{j} y_{k} .
$$

++++

Section 6.4 Fourth-Order Sturm-Liouville Theory

eigenvalues of Example 1.
(b) Derive the eigenfunctions
$$
\begin{array}{c}
X_{1}=1, \quad X_{2}=x-\frac{L}{2} \\
X_{n}(x)=\cosh \alpha_{n} x+\cos \alpha_{n} x-\frac{\cosh \alpha_{n} L-\cos \alpha_{n} L}{\sinh \alpha_{n} L-\sin \alpha_{n} L}\left(\sin \alpha_{n} x+\sinh \alpha_{n} x\right)
\end{array}
$$
for $n=3,4, \ldots$, where $\alpha_{n+2}$ is the $n$th positive root of
$$
\cosh \alpha L \cos \alpha L=1
$$
(Note that $X_{2}$ was chosen so as to be orthogonal to $X_{1}$. The choice $X_{2}=x$ not share this property.) [Hint: You can do this problem by following the sol of Example 1 or by noting that $X^{\prime \prime}$ is a solution of the Sturm-Liouville probl Example 1. So the eigenfunctions for $n \geq 3$ can be obtained by integratin eigenfunctions of Example 1 twice.]
12. (a) Take $L=1$ in Exercise 11 and compute explicitly the first six eigen tions $X_{1}(x), \ldots, X_{6}(x)$. You may use the numerical data of Example 1.
(b) Given $f(x)=x(1-x), 0<x<1$, approximate the numerical values first six terms of the eigenfunction expansion of $f$. Plot the function and s partial sums of its eigenfunction expansion.
13. Repeat Exercise 12 (b) with $f(x)=x^{4}(1-x)^{4}, 0<x<1$.

Project Problem: In Exercise 14 you are asked to solve a Sturm-Liouville lem that arises in the study of the vibrating clamped-free beam (see Section Model your solution after Examples 1 and 2, and do Exercise 15 to experiment eigenfunction expansions.
14. (a) Show that the eigenvalues $\lambda$ of
$$
\begin{array}{c}
X^{(4)}-\lambda X=0 \\
X(0)=0, \quad X^{\prime}(0)=0, \quad X^{\prime \prime}(L)=0, \quad X^{\prime \prime \prime}(L)=0
\end{array}
$$
are all values of the form $\lambda=\alpha^{4}$, where $\alpha$ is a positive root of $\cosh \alpha L \cos \alpha L=$
(b) Derive the eigenfunctions
$$
X_{n}(x)=\cos \alpha_{n} x-\cosh \alpha_{n} x-\frac{\cosh \alpha_{n} L+\cos \alpha_{n} L}{\sinh \alpha_{n} L+\sin \alpha_{n} L}\left(\sin \alpha_{n} x-\sinh \alpha_{n} x\right)
$$
for $n=1,2, \ldots$, where $\alpha_{n}$ is the $n$th positive root of $\cosh \alpha L \cos \alpha L=-1$.
15. (a) Take $L=1$ in Exercise 14 and compute explicitly the first five eigen tions $X_{1}(x), \ldots, X_{5}(x)$.
(b) Given $f(x)=x(1-x), 0<x<1$, approximate the numerical values first six terms of the eigenfunction expansion of $f$. Plot the function and s partial sums of its eigenfunction expansion.
16. Orthogonality of eigenfunctions. Let $\lambda_{j} \neq \lambda_{k}$ be two eigenvalues fourth-order Sturm-Liouville problem (1)-(2), with corresponding eigenfund $y_{j}$ and $y_{k}$, respectively.
(a) Check that
$$
\frac{d}{d x}\left[y_{k}\left(p(x) y_{j}^{\prime \prime}\right)^{\prime}-y_{j}\left(p(x) y_{k}^{\prime \prime}\right)^{\prime}-y_{k}^{\prime}\left(p(x) y_{j}^{\prime \prime}\right)+y_{j}^{\prime}\left(p(x) y_{k}^{\prime \prime}\right)\right]=-\left(\lambda_{k}-\lambda_{j}\right) r(x) ?
$$

---

<!-- Page 34 -->

Left margin note (page 34)

360
Chapter 6
s
6.5 Elastic

Right margin note (page 34)

$y_{j}$ and
a) and
$L / 2$ by
f these
icients
cential er the pports ckling
to the resent ompliement
se ed by
ve mabeam to the ss secat the enters ariable onding
a pin aid to ports, ctions,

++++

turm-Liouville Theory with Engineering Applications
(b) Integrate from $a$ to $b$, and use the boundary conditions (2) to show that $y_{k}$ are orthogonal with respect to the weight function $r(x)$.
17. (a) Verify that $\lambda=0$ is not an eigenvalue for the problems in Example $2($ (b).
(b) In Example 1, show that each $X_{n}(x)$ is either even or odd about $x=$ showing, specifically, that $X_{n}(L-x)=(-1)^{n-1} X_{n}(x)$.
(c) Plot the first five eigenfunctions for Example 1, and observe that each o has the symmetry property about $x=L / 2$ set forth in part (a).
(d) Based on part (b) or (c), can you explain why the second and fourth coeff in the eigenfunction expansion in Example 1(c) are 0? Generalize.

Vibrations and Buckling of Beams
The applications that we consider in this section lead to partial differ equations that are fourth order in the space variables. We consid transverse vibrations of an elastic homogeneous beam with various su at its ends. We also consider the problem of determining the critical bu load of a vertical column.

The modeling of these problems can be carried out in a way similar problems considered in Section 3.2. Because beams and columns p resistance to bending, the derivations of their equations are more c cated and, in particular, involve the fourth derivative of the displac with respect to $x$.

Transverse Vibrations of a Beam: Simply Supported Ca
The free vertical vibrations of a uniform beam of length $L$ are describ the equation
$$
u_{t t}=-c^{2} u_{x x x x}
$$
where $c^{2}=\frac{E I}{\rho A}, E=$ Young's constant (determined by the constituti terial of the beam), $I=$ moment of inertia of a cross section of the with respect to an axis through its center of mass and perpendicular ( $x, u$ )-plane, $\rho=$ density (mass per unit volume), and $A=$ area of cro tion. It is assumed that the beam is of uniform density throughout, th cross sections are constant, and that in its equilibrium position the $c$ of mass of the cross sections lie on the $x$-axis (see Figure 1). The ve $u(x, t)$ represents the displacement of the point on the beam correspe to position $x$ at time $t$.

It is customary in engineering to show a simple beam resting on and a roller and not, say, on two pins. In this manner, the beam is s be statically determinate. If the beam were to have two pins as sup it would become statically indeterminate and develop horizontal rea

---

<!-- Page 35 -->

Left margin note (page 35)

![](./images/b6761637-e91c-4988-8637-83a0e794256f-35_299_817_853_578.jpg)

Figure 1 A simply supported beam is pinned at one end and roller supported at the other. The ends can rotate freely but do not move vertically.

Right margin note (page 35)

361

posvent d or en a oller poth eam two tion ins, ure. eam end sup-
supthe e or h of astic orts can the eads

++++

Section 6.5 Elastic Vibrations and Buckling of Beams

which is still acceptable; however, it would not constitute the simplest sible beam. As far as the boundary conditions are concerned, both prevertical translation (completely) and both allow rotation (unlike a fixe clamped support, which locks also rotation). The only difference betwe pin and a roller is that a pin prevents horizontal movement, whereas a $r$ does not (it can roll horizontally). However, both allow rotation and 1 prevent vertical translation as we said.

A structure in equilibrium must also be stable. A simply supported b is the simplest structure that is also stable. If the supports were to be rollers, the beam would be unstable (it would not resist any perturba in the horizontal direction). On the other hand, if it is to rest on two it would have one additional reaction in excess of being a stable struct Therefore, a pin and a roller are the simplest possible supports for a b to be both in equilibrium and stable.

The boundary conditions that accompany equation (1) depend on the supports of the beam. The case under consideration, that of simply ported ends, is described by
$$
u(0, t)=0, \quad u(L, t)=0, \quad u_{x x}(0, t)=0, \quad u_{x x}(L, t)=0 .
$$

The fact that the beam is prevented from translating vertically at its ports is expressed by the first two equations in (2). To understand remaining equations in (2), recall that $u_{x x}(x, t)$ represents the curvatur concavity of the beam at any $x$. It is a fact from the theory of strengt materials that curvature is proportional to bending moment for an ela beam. The last two equations in (2) state that the moments at the supp are zero, as is the case for a simply supported beam, since the beam rotate at its ends.

To complete the description of the initial value problem, we specify initial conditions
$$
u(x, 0)=f(x), u_{t}(x, 0)=g(x), \quad 0<x<L,
$$
which give the initial displacement and velocity of the beam.
To solve (1)-(3), we use the method of separation of variables. This l to the equations
$$
\frac{X^{(4)}}{X}=-\frac{T^{\prime \prime}}{c^{2} T}=\alpha^{4} .
$$

---

<!-- Page 36 -->

Left margin note (page 36)

362
Chapter 6 Sturm-Liou

Right margin note (page 36)

ct pentarily eness, $X=0$ l solumple 2
pe deand e solve pendix
andary
nich it $X_{n}$ are of Sec-

++++

ville Theory with Engineering Applications

We have chosen the separation constant to be positive because we expe riodic behavior in $t$, and for reasons that will become apparent mome it is convenient to denote this constant by $\alpha^{4}$. For the sake of complet we note that it can be shown that the boundary value problem $X^{(4)}-\lambda$ together with the boundary conditions implied by (2) has nontrivia tions only for positive choices of the separation constant $\lambda$ (see Exar (a), Section 6.4).

We begin by considering the boundary value problem for $X$ :
$$
\begin{array}{c}
X^{(4)}-\alpha^{4} X=0 \\
X(0)=0, \quad X(L)=0, \quad X^{\prime \prime}(0)=0, X^{\prime \prime}(L)=0 .
\end{array}
$$

Note that this is a fourth-order Sturm-Liouville problem of the ty scribed in the previous section, with $\lambda=\alpha^{4}, p(x)=1, q(x)= r(x)=1$. Since (5) is a linear equation with constant coefficients, w it by passing to the characteristic equation in the familiar way (Apt
A.2). We find
$$
r^{4}-\alpha^{4}=0 \Rightarrow r= \pm \alpha, \quad \text { and } \quad r= \pm i \alpha .
$$

Thus the general solution is
$$
X(x)=A \cosh \alpha x+B \sinh \alpha x+C \cos \alpha x+D \sin \alpha x,
$$
where $A, B, C$, and $D$ are arbitrary constants. The first and third bou conditions imply that
$$
A+C=0, \quad A-C=0 \Rightarrow A=C=0 .
$$

The second and fourth conditions then imply
$$
\left\{\begin{array}{l}
B \sinh \alpha L+D \sin \alpha L=0 \\
B \sinh \alpha L-D \sin \alpha L=0
\end{array}\right.
$$

These are equivalent to $B \sinh \alpha L=0$ and $D \sin \alpha L=0$, from w) follows that $B=0$ (since $\sinh \alpha L \neq 0$ for $\alpha>0$ ) and
$$
\alpha=\alpha_{n}=\frac{n \pi}{L}, \quad n=1,2, \ldots .
$$

We thus obtain the solutions in $x$ :
$$
X_{n}(x)=\sin \frac{n \pi}{L} x, \quad n=1,2, \ldots .
$$

Note that in this case it is easy to verify that the eigenfunctions orthogonal on the interval $0<x<L$ as guaranteed by Theorem 1 tion 6.4.

---

<!-- Page 37 -->

Left margin note (page 37)

![](./images/b6761637-e91c-4988-8637-83a0e794256f-37_274_736_1936_680.jpg)

Figure 2 A beam with two clamped ends.

Right margin note (page 37)

363
corre-
rm of
erval

cients
the
or the ation, main

++++

Section 6.5 Elastic Vibrations and Buckling of Beams

Going back to (4) and solving for $T$ with $\alpha=\alpha_{n}$, we obtain the sponding solutions
$$
T_{n}(t)=A_{n} \cos c \alpha_{n}^{2} t+A_{n}^{*} \sin c \alpha_{n}^{2} t
$$

Forming the product solutions and superposing, we find the general fo the solution:
$$
u(x, t)=\sum_{n=1}^{\infty} \sin \frac{n \pi}{L} x\left(A_{n} \cos c \alpha_{n}^{2} t+A_{n}^{*} \sin c \alpha_{n}^{2} t\right) .
$$

Using the initial conditions (3), we get
$$
f(x)=\sum_{n=1}^{\infty} A_{n} \sin \frac{n \pi}{L} x,
$$
and
$$
g(x)=\sum_{n=1}^{\infty} A_{n}^{*} c \alpha_{n}^{2} \sin \frac{n \pi}{L} x .
$$

Since these should just be the sine expansions of $f$ and $g$ on the in $0<x<L$, it follows directly from Section 2.4 that
$$
\begin{array}{c}
A_{n}=\frac{2}{L} \int_{0}^{L} f(x) \sin \frac{n \pi}{L} x d x \\
A_{n}^{*}=\frac{2 L}{n^{2} \pi^{2} c} \int_{0}^{L} g(x) \sin \frac{n \pi}{L} x d x, \quad n=1,2, \ldots
\end{array}
$$

The solution of (1)-(3) is thus given by the series (6) with the coeffic determined by (7) and (8).
Transverse Vibrations of a Beam: Clamped Case If the ends of the beam in the previous example are clamped (Figure 2 boundary conditions become
$$
u(0, t)=0, u(L, t)=0, \quad u_{x}(0, t)=0, u_{x}(L, t)=0,
$$
for all $t>0$. While the first two conditions in (9) are the same as those fo simply supported case, the last two impose a restraint against end rot since the beam does resist moments at its ends. The initial conditions re
$$
u(x, 0)=f(x), u_{t}(x, 0)=g(x), \quad 0<x<L .
$$

---

<!-- Page 38 -->

Left margin note (page 38)

364
Chapter 6
Sturm

Right margin note (page 38)

e way
at the

vious
$$
\left.{ }_{2} x\right),
$$
oduct
d ap-
oblem

++++

a-Liouville Theory with Engineering Applications

We solve the boundary value problem (1), (9), (10), in much the sam as in the previous example. After separating the variables, we arrive : fourth order Sturm-Liouville problem
$$
\begin{array}{c}
X^{(4)}-\lambda X=0 \\
X(0)=0, \quad X(L)=0, \quad X^{\prime}(0)=0, \quad X^{\prime}(L)=0 .
\end{array}
$$

This is precisely the problem solved in Examples 1 and 2 of the pre section, where we found that $\lambda=\lambda_{n}=\alpha_{n}^{4}$, and
$$
X_{n}(x)=\cosh \alpha_{n} x-\cos \alpha_{n} x-\frac{\cosh \alpha_{n} L-\cos \alpha_{n} L}{\sinh \alpha_{n} L-\sin \alpha_{n} L}\left(\sinh \alpha_{n} x-\sin \alpha_{n}\right.
$$
where the $\alpha_{n}$ 's are the positive roots of the equation
$$
\cosh \alpha L \cos \alpha L=1, \quad \text { or } \quad \cos \alpha L=\frac{1}{\cosh \alpha L}
$$

Using the solution for $T$ from the previous example and superposing pr solutions, we arrive at
$$
\begin{aligned}
u(x, t) & =\sum_{n=1}^{\infty}\left\{\cosh \alpha_{n} x-\cos \alpha_{n} x\right. \\
& \left.-\frac{\cosh \alpha_{n} L-\cos \alpha_{n} L}{\sinh \alpha_{n} L-\sin \alpha_{n} L}\left(\sinh \alpha_{n} x-\sin \alpha_{n} x\right)\right\} \\
& \times\left\{A_{n} \cos \alpha_{n}^{2} c t+A_{n}^{*} \sin \alpha_{n}^{2} c t\right\}
\end{aligned}
$$

We now determine the coefficients by using the initial conditions an pealing to Theorem 2 of Section 6.4. We get
$$
A_{n}=\frac{1}{\kappa_{n}} \int_{0}^{L} f(x) X_{n}(x) d x, \quad A_{n}^{*}=\frac{1}{\alpha_{n}^{2} c \kappa_{n}} \int_{0}^{L} g(x) X_{n}(x) d x
$$
where
$$
\kappa_{n}=\int_{0}^{L} X_{n}^{2}(x) d x
$$
and the $\alpha_{n}$ 's are the positive roots of (12). We illustrate this pr numerically.

EXAMPLE 1 Vibrating elastic beam: clamped case
Consider the boundary value problem (1), (9), (10), with
$$
L=1, c=1, f(x)=\sin ^{2} \pi x, g(x)=0 .
$$

---

<!-- Page 39 -->

Left margin note (page 39)

![](./images/b6761637-e91c-4988-8637-83a0e794256f-39_443_814_1206_31.jpg)

Figure 3 Eigenfu

![](./images/b6761637-e91c-4988-8637-83a0e794256f-39_422_744_1227_969.jpg)

Right margin note (page 39)

365
(14),
ple 1 s , for
igure d up
n.
and

++++

Section 6.5 Elastic Vibrations and Buckling of Beams

The solution of this problem is given by (13), where $A_{n}$ and $A_{n}^{*}$ are given by and $\alpha_{n}$ is the $n$th positive root of (12), with $L=1$. The eigenfunctions are
$$
X_{n}(x)=\cosh \alpha_{n} x-\cos \alpha_{n} x-\frac{\cosh \alpha_{n}-\cos \alpha_{n}}{\sinh \alpha_{n}-\sin \alpha_{n}}\left(\sinh \alpha_{n} x-\sin \alpha_{n} x\right) .
$$

Since $g$ is identically zero, we have $A_{n}^{*}=0$. In Table 1, we recall from Exam of the previous section the coefficients $A_{n}$ and the numerical values of the $\alpha_{n}$, $n=1,2, \ldots, 5$. We also compute the values of $\alpha_{n}^{2}$.

\begin{table}
| $n$ | 1 | 2 | 3 | 4 | 5 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $\alpha_{n}$ | 4.7300 | 7.8532 | 10.9956 | 14.1372 | 17.2788 |
| $\alpha_{n}^{2}$ | 22.3729 | 61.6727 | 120.9032 | 199.8604 | 298.5569 |
| $A_{n}$ | .612 | 0 | -.022 | 0 | -.002 |
\captionsetup{labelformat=empty}
\caption{Table 1 Numerical data for Example 1.}
\end{table}

Using the data from Table 1, we find
$$
u(x, t)=.612 X_{1}(x) \cos \alpha_{1}^{2} t-.022 X_{3}(x) \cos \alpha_{3}^{2} t-.002 X_{5}(x) \cos \alpha_{5}^{2} t+\cdots
$$

![](./images/b6761637-e91c-4988-8637-83a0e794256f-54_408_604_1710_1172.jpg)
Figure 3 shows the graphs of the first four eigenfunctions of this problem. F 4 shows the position of the beam at various values of $t$. Here $u$ is approximate to the fifth partial sum,
$$
u(x, t) \approx .612 X_{1}(x) \cos \alpha_{1}^{2} t-.022 X_{3}(x) \cos \alpha_{3}^{2} t-.002 X_{5}(x) \cos \alpha_{5}^{2} t
$$

nctions for the clamped beam.

![](./images/b6761637-e91c-4988-8637-83a0e794256f-57_412_463_856_24.jpg)
Figure 4 Snapshots of the vibrating clamped bear

Transverse Vibrations of a Beam: Clamped-Free Case
Consider the cantilevered beam in Figure 5, where one end is clamped the other is free. We have the boundary conditions
$$
u(0, t)=0, u_{x}(0, t)=0, u_{x x}(L, t)=0, u_{x x x}(L, t)=0
$$
and the initial conditions
$$
u(x, 0)=f(x), u_{t}(x, 0)=g(x), \quad 0<x<L .
$$

---

<!-- Page 40 -->

Left margin note (page 40)

366
Chapter 6

![](./images/b6761637-e91c-4988-8637-83a0e794256f-40_281_734_183_645.jpg)

Figure 5 A ca beam is fixed at on free at the other.

Right margin note (page 40)

ouville

We
roduct
eal to

++++

turm-Liouville Theory with Engineering Applications
ntelivered
end and

We separate the variables and arrive at the fourth order Sturm-Li problem
$$
\begin{array}{c}
X^{(4)}-\lambda X=0 \\
X(0)=0, X^{\prime}(0)=0, X^{\prime \prime}(L)=0, X^{\prime \prime \prime}(L)=0
\end{array}
$$

The solution of this problem is outlined in Exercise 14, Section 6.4 have
$$
\lambda=\lambda_{n}=\alpha_{n}^{4},
$$
and
$$
\begin{aligned}
X_{n}(x)= & \cos \alpha_{n} x-\cosh \alpha_{n} x \\
& -\frac{\cosh \alpha_{n} L+\cos \alpha_{n} L}{\sinh \alpha_{n} L+\sin \alpha_{n} L}\left(\sin \alpha_{n} x-\sinh \alpha_{n} x\right),
\end{aligned}
$$
for $n=1,2, \ldots$, where $\alpha_{n}$ is the $n$th positive root of
$$
\cosh \alpha L \cos \alpha L=-1 .
$$

Using the solution for $T$ from the previous example and superposing p solutions, we arrive at
$$
\begin{aligned}
u(x, t)= & \sum_{n=1}^{\infty}\left\{\cos \alpha_{n} x-\cosh \alpha_{n} x\right. \\
& \left.-\frac{\cosh \alpha_{n} L+\cos \alpha_{n} L}{\sinh \alpha_{n} L+\sin \alpha_{n} L}\left(\sin \alpha_{n} x-\sinh \alpha_{n} x\right)\right\} \\
& \times\left\{A_{n} \cos \alpha_{n}^{2} c t+A_{n}^{*} \sin \alpha_{n}^{2} c t\right\}
\end{aligned}
$$

To determine the coefficients, we use the initial conditions and app Theorem 2, Section 6.4, and get
$$
A_{n}=\frac{1}{\kappa_{n}} \int_{0}^{L} f(x) X_{n}(x) d x, \quad A_{n}^{*}=\frac{1}{\alpha_{n}^{2} c \kappa_{n}} \int_{0}^{L} g(x) X_{n}(x) d x
$$
where
$$
\kappa_{n}=\int_{0}^{L} X_{n}^{2}(x) d x
$$
and the $\alpha_{n}$ 's are the positive roots of (18).

---

<!-- Page 41 -->

Left margin note (page 41)

![](./images/b6761637-e91c-4988-8637-83a0e794256f-41_340_405_495_42.jpg)

Figure 6

![](./images/b6761637-e91c-4988-8637-83a0e794256f-41_373_700_1782_149.jpg)

Figure 7 Eige

![](./images/b6761637-e91c-4988-8637-83a0e794256f-41_334_759_1805_908.jpg)

Right margin note (page 41)

367
$$
\alpha_{n} \text { 's }
$$
h the sitive

Table with ction al to rding
puter
$t$
ure 8
fifth

++++

Section 6.5 Elastic Vibrations and Buckling of Beams

EXAMPLE 2 Vibrating elastic beam: clamped-free case
Solve the boundary value problem (1), (15), (16), with
$$
L=1, f(x)=x^{2}, g(x)=0, c=1 .
$$

Solution Here the solution is given by (19) and (20), with $A_{n}^{*}=0$, and the are determined from the equation
$$
\cos \alpha=-\frac{1}{\cosh \alpha} .
$$

As shown in Figure 6, this equation has infinitely many positive real roots. Wit help of a computer, we approximated the numerical values of the first five po roots and included them in Table 2.

\begin{table}
| $n$ | 1 | 2 | 3 | 4 | 5 |
| :--- | :---: | :---: | :---: | :---: | :---: |
| $\alpha_{n}$ | 1.875 | 4.694 | 7.855 | 10.995 | 14.137 |
\captionsetup{labelformat=empty}
\caption{Table 2 Numerical data for Example 2.}
\end{table}

Note that in Table 2, starting with $n=2$, the values are close to those in 1 (starting with $n=1$ ). This is because $1 / \cosh \alpha$ goes to zero very rapidly increasing $\alpha$. Hence the intersection points in Figure 6 above and Figure 1, Se 6.4, have very nearly equal $\alpha$ coordinates, which in turn are very nearly equ $(n+1 / 2) \pi$. To determine the coefficients $A_{n}$ in the series solution (19), acco to (20), we must compute the inner products of $f$ with the eigenfunctions
$$
X_{n}=\cos \alpha_{n} x-\cosh \alpha_{n} x-\frac{\cosh \alpha_{n}+\cos \alpha_{n}}{\sinh \alpha_{n}+\sin \alpha_{n}}\left(\sin \alpha_{n} x-\sinh \alpha_{n} x\right) .
$$

While these inner products can be performed by hand, here again we use a com to approximate the coefficients. We have
$$
\begin{aligned}
u(x, t)= & -0.445 X_{1}(x) \cos \alpha_{1}^{2} t+.039 X_{2}(x) \cos \alpha_{2}^{2} t-.008 X_{3}(x) \cos \alpha_{3}^{2} \\
& +.003 X_{4}(x) \cos \alpha_{4}^{2} t-.001 X_{5}(x) \cos \alpha_{5}^{2} t \ldots
\end{aligned}
$$

![](./images/b6761637-e91c-4988-8637-83a0e794256f-41_334_759_1805_908.jpg)
Figure 7 shows the graphs of the first four eigenfunctions of this problem. Fig shows the position of the beam at various values of $t$. Here also, we used the partial sum to approximate $u$.

nfunctions for the cantilevered beam.

![](./images/b6761637-e91c-4988-8637-83a0e794256f-41_334_759_1805_908.jpg)
Figure 8 Snapshots of the vibrating cantilevered beam.

---

<!-- Page 42 -->

Left margin note (page 42)

368
Chapter 6 S

![](./images/b6761637-e91c-4988-8637-83a0e794256f-42_479_313_363_65.jpg)

Figure 9 Vertica with axial loading
(a) Clamped-free
$$
\begin{array}{l}
y(0)=0, y^{\prime}(0)=0 \\
y(L)=\delta, y^{\prime \prime}(L)=0
\end{array}
$$

![](./images/b6761637-e91c-4988-8637-83a0e794256f-42_494_308_1243_719.jpg)
![](./images/b6761637-e91c-4988-8637-83a0e794256f-42_422_137_1315_1336.jpg)
![](./images/b6761637-e91c-4988-8637-83a0e794256f-42_471_313_1266_95.jpg)

Right margin note (page 42)

s- secrested ckling. $P_{1}$ is ion:
olumn are 10. d $P_{1}$ is ditions
tion of erpenves an In the cases
blve for uation

++++

turm-Liouville Theory with Engineering Applications

Buckling of Columns under Axial Loading
Consider a vertical column of length $L$ of constant density and cros tional shape with a load $P$ at its top, as shown in Figure 9. We are inte in finding the largest load $P$ that the column can withstand before bu This critical value $P_{1}$ is known as the Euler load. It turns out that determined by the first eigenvalue of the following fourth-order equat
$$
y^{(4)}+\lambda y^{\prime \prime}=0,
$$
with boundary conditions corresponding to the manner in which the c is fastened at its ends. Typical boundary conditions are shown in Fig

From the theory of strength of materials, the critical buckling load related to the first eigenvalue of (21) with appropriate boundary cond by

1 column
$$
P_{1}=E I \lambda_{1},
$$
where $E=$ Young's constant and $I=$ moment of inertia of a cross sec the column with respect to an axis through its center of mass and $p$ dicular to the ( $x, y$ )-plane. The eigenfunction corresponding to $\lambda_{1} \mathrm{gi}$ indication of the deformation of the column as it begins to buckle. following examples, we solve for the Euler load in the second and thir in Figure 10. We begin with the third case.
(b) Clamped-clamped case:
$$
\begin{array}{l}
y(0)=0, y^{\prime}(0)=0 \\
y(L)=0, y^{\prime}(L)=0
\end{array}
$$
(c) Simply supported case: $y(0)=0, y^{\prime \prime}(0)=0$,

Figure 10 Boundary conditions for a vertical column with axial loading.

EXAMPLE 3 Buckling of a column: simply supported case To s the critical load (Euler load) of a hinged-hinged column, we consider the eq
$$
y^{(4)}+\lambda y^{\prime \prime}=0,
$$

---

<!-- Page 43 -->

Right margin note (page 43)

369
$$
y=0
$$
it is

2 ) is
ourth
e. In
$$
y=0
$$

From

++++

Section 6.5 Elastic Vibrations and Buckling of Beams

together with the boundary conditions
$$
y(0)=0, y^{\prime \prime}(0)=0, y(L)=0, y^{\prime \prime}(L)=0
$$

It can be shown that nonpositive values of $\lambda$ lead only to the trivial solution (see Exercise 9). Therefore, we concentrate on the case $\lambda>0$, and hence convenient to set $\lambda=\alpha^{2}$ with $\alpha>0$. The characteristic equation of (22) is
$$
r^{4}+\alpha^{2} r^{2}=r^{2}\left(r^{2}+\alpha^{2}\right)=0
$$
which has roots $r=0$ (double) and $r= \pm i \alpha$. Thus the general solution to (2
$$
y=A+B x+C \cos \alpha x+D \sin \alpha x .
$$

Using the first two boundary conditions, we find $A=C=0$. The third and f imply that $B=0$ and $\sin \alpha L=0$. The last equation implies that
$$
\alpha=\alpha_{n}=\frac{n \pi}{L},
$$
and hence the first eigenvalue is
$$
\lambda_{1}=\alpha_{1}^{2}=\frac{\pi^{2}}{L^{2}}
$$

The corresponding buckling mode is
$$
y_{1}=\sin \frac{\pi}{L} x
$$
and gives the shape of the deflection when the column first begins to buckl conclusion, we find that the Euler load for this column is $E I \frac{\pi^{2}}{L^{2}}$.

EXAMPLE 4 Buckling of a column: clamped-clamped case
For this case, we must solve equation (22) with the boundary conditions
$$
y(0)=0, y^{\prime}(0)=0, y(L)=0, y^{\prime}(L)=0 .
$$

It can be shown that nonpositive values of $\lambda$ lead only to the trivial solution (see Exercise 10). We therefore concentrate on the case $\lambda=\alpha^{2}$ with $\alpha>0$. Example 3, we have
$$
y=A+B x+C \cos \alpha x+D \sin \alpha x .
$$

The boundary conditions yield the following equations for the coefficients:
$$
\begin{array}{l}
A+C=0 \Rightarrow A=-C, \\
B+\alpha D=0 \Rightarrow B=-\alpha D, \\
A+B L+C \cos \alpha L+D \sin \alpha L=0, \\
B-\alpha C \sin \alpha L+\alpha D \cos \alpha L=0 .
\end{array}
$$

Using the first and second of these equations in the third and fourth, we get
$$
\left\{\begin{array}{l}
(1-\cos \alpha L) C+(\alpha L-\sin \alpha L) D=0 \\
\sin \alpha L C+(1-\cos \alpha L) D=0
\end{array}\right.
$$

---

<!-- Page 44 -->

Left margin note (page 44)

370
Chapter 6 S

![](./images/b6761637-e91c-4988-8637-83a0e794256f-44_507_1019_1105_685.jpg)

Figure 11 The tra tal equation $\tan x$ infinitely many posit one in each interval $\left(k \pi+\frac{\pi}{2},(k+1) \pi+\right. k=0,1,2, \ldots$.

Right margin note (page 44)

ons are
trivial
rmines
metric

uation
ve have gure 11 $L$, and
ported have to uation related

++++

turm-Liouville Theory with Engineering Applications

If this system of equations has a nonzero determinant, then its only solutic $C=D=0$. This leads to a trivial solution for $y$. Hence, to get nor solutions, we must set the determinant equal to 0 . We get
$$
(1-\cos \alpha L)^{2}-\sin \alpha L(\alpha L-\sin \alpha L)=0,
$$
or, equivalently,
$$
2-2 \cos \alpha L-\alpha L \sin \alpha L=0,
$$
since $\cos ^{2} \alpha L+\sin ^{2} \alpha L=1$. The first positive root $\alpha_{1}$ of this equation dete the first eigenvalue, and thus the critical load. Using the half-angle trigono identities, we have
$$
4 \sin ^{2} \frac{\alpha L}{2}-2 \alpha L \sin \frac{\alpha L}{2} \cos \frac{\alpha L}{2}=0 .
$$

Thus the roots we seek are the positive roots of
$$
\sin \frac{\alpha L}{2}\left[2 \sin \frac{\alpha L}{2}-\alpha L \cos \frac{\alpha L}{2}\right]=0 .
$$

The equation $\sin \frac{\alpha L}{2}=0$ has for its smallest positive root $\alpha=\frac{2 \pi}{L}$. The eq $2 \sin \frac{\alpha L}{2}-\alpha L \cos \frac{\alpha L}{2}=0$ transforms to
$$
\tan \frac{\alpha L}{2}=\frac{\alpha L}{2} .
$$

The roots of this transcendental equation cannot be found explicitly, but as v done before, we can use a computer system to approximate them. As Fig shows, the first positive root is certainly larger than $2 \pi / L$. Hence $\alpha_{1}=2 \pi /$ the Euler load is
$$
P_{1}=\frac{4 \pi^{2}}{L^{2}} E 1 .
$$

Note that the critical load is four times greater than its value in the simply sup case. Finally, if we are interested in the shape of the column as it buckles, we compute the eigenfunction corresponding to $\alpha_{1}$. With $\alpha_{1}=\frac{2 \pi}{L}$, the first ec in (24) implies that $D=0$, and hence $B=0$. The coefficients $A$ and $C$ are by $A=-C$. Taking $A=1$, we get the eigenfunction
$$
y_{1}=1-\cos \frac{2 \pi}{L} x,
$$

---

<!-- Page 45 -->

Left margin note (page 45)

6.6 The Biha

Right margin note (page 45)

371
jiven the the s on rder dity role, eart
llike onic

++++

Section 6.6 The Biharmonic Operator

or, equivalently,
$$
y_{1}=2 \sin ^{2} \frac{\pi}{L} x
$$

Exercises 6.5
In Exercises 1-2, solve the boundary value problem (1), (2), (3) subject to the conditions.
1. $f(x)=x \sin \pi x, g(x)=0, c=\pi, L=1$.
2. $f(x)=x(1-x), g(x)=0, c=\pi, L=1$.

In Exercises 3-4, solve the boundary value problem (1), (9), (10) subject to given conditions.
3. $f(x)=x(1-x), \quad g(x)=x, c=1, L=1$.
4. $f(x)=1-\cos 4 \pi x, \quad g(x)=\sin 2 \pi x, c=1, L=1$.

In Exercises 5-6, solve the boundary value problem (1), (15), (16) subject t given conditions.
5. $f(x)=x^{3}, g(x)=0, c=\pi, L=1$.
6. $f(x)=x^{2} \cos \pi x, g(x)=0, c=\pi, L=1$.
7. (a) Determine the eigenvalues of the problem in Figure 10(a).
(b) Determine the critical buckling load for a clamped-free column.
8. Show that the eigenvalues in Example 3 are positive.
9. Show that the eigenvalues in Example 4 are positive.
rmonic Operator
In this and the following sections we consider boundary value problem plates. As in the case of beams, the equations will involve fourth-o partial derivatives with respect to the spacial variables, due to the rig of the plates. Whereas with membranes the Laplacian plays a central here the iterated Laplacian or biharmonic operator will be at the h of most equations. The biharmonic operator of $u(x, y)$ is defined as
$$
\nabla^{4} u=\nabla^{2}\left(\nabla^{2} u\right) .
$$

In Cartesian coordinates,
$$
\begin{aligned}
\nabla^{4} u(x, y) & =\nabla^{2}\left(u_{x x}+u_{y y}\right)=\left(u_{x x}+u_{y y}\right)_{x x}+\left(u_{x x}+u_{y y}\right)_{y y} \\
& =u_{x x x x}+u_{y y x x}+u_{x x y y}+u_{y y y y} \\
& =u_{x x x x}+2 u_{y y x x}+u_{y y y y}
\end{aligned}
$$

The fourth partial derivatives present a new challenge. Moreover, un Laplace's equation, you cannot separate the variables in the biharm equation in Cartesian coordinates:
$$
u_{x x x x}+2 u_{y y x x}+u_{y y y y}=0
$$

---

<!-- Page 46 -->

Left margin note (page 46)

372
Chapter 6
Sturm-Liou

Right margin note (page 46)

get
ns out, tion in biharas we probdinates go the lutions
equaclear, ig prossarily
ntity
$$
\begin{array}{l}
y+D, \\
x+B,
\end{array}
$$

Also,
C) $=0$.
$$
\nabla^{4} v=
$$

++++

ville Theory with Engineering Applications

In fact, if we set $u(x, y)=X(x) Y(y)$ and plug into the equation, we
$$
X^{\prime \prime \prime \prime} Y+2 X^{\prime \prime} Y^{\prime \prime}+X Y^{\prime \prime \prime \prime}=0
$$
and clearly the variables cannot be separated in this equation. It turn however, that we can separate the variables in the biharmonic equa polar coordinates. It is still an overwhelming task to work with the monic equation directly. Instead, in this and the following section, search for analytical solutions, we will use clever methods to reduce to lems involving the Laplacian. These reductions work in polar coor but again fail in Cartesian coordinates. Because of this fact, we will for search for analytical solutions in Cartesian coordinates (numerical so can be used for such problems) and work in polar coordinates.

We call a biharmonic function any solution of the biharmonic tion. Observe that any harmonic function $u$ is also biharmonic. This is since if $\nabla^{2} u=0$, then $\nabla^{4}(u)=\nabla^{2}\left(\nabla^{2}(u)\right)=\nabla^{2}(0)=0$. The followir vides a way to construct biharmonic functions, which are not nece harmonic.

EXAMPLE 1 Biharmonic functions

Show that if $u=u(x, y)$ is harmonic and
$$
v=u \cdot\left(A\left(x^{2}+y^{2}\right)+B x+C y+D\right),
$$
where $A, B, C$, and $D$ are constants, then $v$ is biharmonic.
Solution We have to verify that $\nabla^{4} v=0$. As a first step, establish the ide
$$
\nabla^{2}(\phi \cdot \psi)=\psi \nabla^{2}(\phi)+\phi \nabla^{2}(\psi)+2 \phi_{x} \psi_{x}+2 \phi_{y} \psi_{y}
$$
(Exercise 10). Apply this identity with $u=\phi$ and $\psi=A\left(x^{2}+y^{2}\right)+B x+C \nabla^{2} u=0(u$ is harmonic $), \nabla^{2}\left(A\left(x^{2}+y^{2}\right)+B x+C y+D\right)=4 A, \psi_{x}=2 A$ and $\psi_{y}=2 A y+C$; then
$$
\begin{aligned}
\nabla^{4} v & =\nabla^{2} \nabla^{2}\left(u \cdot\left(A\left(x^{2}+y^{2}\right)+B x+C y+D\right)\right) \\
& =\nabla^{2}\left(4 A u+2 u_{x}(2 A x+B)+2 u_{y}(2 A y+C)\right) \\
& =4 A \nabla^{2} u+2 \nabla^{2}\left(u_{x}(2 A x+B)\right)+2 \nabla^{2}\left(u_{y}(2 A y+C)\right) \\
& =2 \nabla^{2}\left(u_{x}(2 A x+B)\right)+2 \nabla^{2}\left(u_{y}(2 A y+C)\right) .
\end{aligned}
$$

Since $\nabla^{2} u=0$, then $\nabla^{2}\left(u_{x}\right)=\left(\nabla^{2} u\right)_{x}=0$, and, similarly, $\nabla^{2}\left(u_{y}\right)=0 2 A x+B$ is a linear function, so $\nabla^{2}(2 A x+B)=0$. Similarly, $\nabla^{2}(2 A y+$ Applying (4), we find
$$
\nabla^{2}\left(u_{x}(2 A x+B)\right)=2\left(u_{x}\right)_{x}(2 A x+B)_{x}+2\left(u_{x}\right)_{y}(2 A x+B)_{y}=4 A u_{x y}
$$
because $(2 A x+B)_{y}=0$. Similarly, $\nabla^{2}\left(u_{y}(2 A y+C)\right)=4 A u_{y y}$. Hence $8 A u_{x x}+8 A u_{y y}=8 A\left(u_{x x}+u_{y y}\right)=0$.

---

<!-- Page 47 -->

Left margin note (page 47)

![](./images/b6761637-e91c-4988-8637-83a0e794256f-47_486_463_359_42.jpg)

Figure 1 A biharmonic function that attains its maximum inside a region.

Right margin note (page 47)

373

cted, $-1 \leq$ onic point tions (the vhich
ation imof $u$ y $u_{r}$ ) chlet
ple 1 $t$ the ions. dary d by using
with Next, tself.

++++

Section 6.6 The Biharmonic Operator

Taking $u(x, y)=1, A=-1, D=1$, and $B=C=0$ in (3), we obtain
$$
v(x, y)=1-x^{2}-y^{2}
$$

We have $\nabla^{2} v=-2-2=-4$ and $\nabla^{4} v=\nabla^{2}(-4)=0$. Thus, as expe $v$ is biharmonic but not harmonic. The graph of $v$ over the rectangle $x, y \leq 1$, in Figure 1, illustrates an important distinction between harn and biharmonic functions. The maximum value of $v$ is attained at the $(0,0)$ inside the rectangle, which is unlike nonconstant harmonic func whose maximum and minimum values must occur on the boundary maximum principle, Section 3.11). Thus the maximum principle, v holds for harmonic functions, fails for biharmonic functions.

Solution of the Biharmonic Equation
We switch to polar coordinates $(r, \theta)$ and consider the biharmonic equ on a disk with center at the origin and radius $a>0$ :
$$
\nabla^{4} u=0, \quad 0 \leq r<a, \quad 0 \leq \theta \leq 2 \pi .
$$

Because the biharmonic equation involves fourth order derivatives, w pose two conditions on the boundary that specify the boundary values and its normal derivative. Since the normal derivative is $\frac{\partial u}{\partial r}$ (or simpl) for the disk, we will consider (5) subject to the boundary conditions
$$
u(a, \theta)=f(\theta), \quad \frac{\partial u}{\partial r}(a, \theta)=g(\theta), \quad 0 \leq \theta \leq 2 \pi .
$$

We solve the boundary value problem (5)-(6) by reducing it to two Diri problems on the disk, as follows. Consider a function of the form
$$
u(r, \theta)=\left(a^{2}-r^{2}\right) v(r, \theta)+w(r, \theta),
$$
where $v$ and $w$ are harmonic. Since $r^{2}=x^{2}+y^{2}$, it follows from Exam that $\left(a^{2}-r^{2}\right) v$ is biharmonic. And since $w$ is biharmonic, it follows tha right side of (7) is biharmonic, being the sum of two biharmonic funct So $u$ satisfies (5). We next determine $v$ and $w$ so as to satisfy the boun conditions (6). Since both $v$ and $w$ are harmonic, they are determine their values on the boundary of the disk. Setting $r=a$ in (7) and $u(a, \theta)=f(\theta)$, we determine the boundary values for $w$ :
$$
w(a, \theta)=f(\theta)
$$

Thus $w$ is the (unique) solution of the Dirichlet problem on the disk boundary values (8). To find $w$, we use techniques from Section 4.4. we determine the boundary values of $v$, which in turn will determine $v$ i

---

<!-- Page 48 -->

Left margin note (page 48)

374
Chapter 6
S

![](./images/b6761637-e91c-4988-8637-83a0e794256f-48_472_1287_564_567.jpg)

Figure 2 Decom of a biharmonic with two bounda ditions into two problems with one ary condition each.

THEO
SOLUTION O
BIHARI
EQU

Right margin note (page 48)

$$
r=a,
$$
$-g(\theta))$
a
ation
ad the nique)
es (9).
n (5)-
m 1 .
c funcoblems undary
uation s of $v$

++++

turm-Liouville Theory with Engineering Applications

For this purpose, differentiate both sides of (7) with respect to $r$, set use $u_{r}(a, \theta)=g(\theta)$, and get
$$
\begin{aligned}
u_{r}(r, \theta) & =-2 r v(r, \theta)+\left(a^{2}-r^{2}\right) v_{r}(r, \theta)+w_{r}(r, \theta) ; \\
u_{r}(a, \theta)=g(\theta) & =-2 a v(a, \theta)+w_{r}(a, \theta) ; \\
v(a, \theta) & =\frac{1}{2 a}\left(w_{r}(a, \theta)-g(\theta)\right) .
\end{aligned}
$$

position
problem
ry con-
Dirichlet
bound-

(a) Biharmonic equation

(b) Laplace's equation

(c) Laplace's equ

Since $w$ is determined at this point, $w_{r}(a, \theta)$ is therfore known an last equation determines the boundary values of $v$. Thus $v$ is the (u solution of the Dirichlet problem inside the disk with boundary value This determines $v$ and $w$ in (7) and solves the boundary value probler (6). The method is illustrated in Figure 2 and summarized in Theore

The solution of the boundary value problem (5)-(6) is the biharmoni tion $u$ given by (7), where $v$ and $w$ are solutions of the Dirichlet pr on the disk with boundary values for $w$ given by (8) (same as the bo values of $u$ ) and boundary values for $v$ given by (9).

As in the derivation of the solution, when solving a biharmonic eq inside the disk, we first find $w$ and then $v$, since the boundary value depend on those of $w$.

EXAMPLE 2 Biharmonic equation
On the unit disk, solve
$$
\nabla^{4} u=0, \quad u(1, \theta)=\cos \theta \quad \text { and } \quad u_{r}(1, \theta)=\sin \theta .
$$

Solution According to Theorem 1, the solution is of the form
$$
u(r, \theta)=\left(1-r^{2}\right) v+w,
$$

---

<!-- Page 49 -->

Right margin note (page 49)

375

of $w$ ct to given urier that
rsing
$t$ the $\theta)=$
harnot
spe-reone
dary,

++++

Section 6.6 The Biharmonic Operator

where $v$ and $w$ are harmonic functions in the unit disk. The boundary values are the same as those of $u$. Thus, to find $w$, we must solve $\nabla^{2} w=0$ subje $w(1, \theta)=\cos \theta$. We know from Section 4.4 that the solution of this problem is by $w(r, \theta)=a_{0}+\sum_{n=1}^{\infty} r^{n}\left(a_{n} \cos n \theta+b_{n} \sin n \theta\right)$, where $a_{n}$ and $b_{n}$ are the Fo coefficients of the boundary function, $f(\theta)=\cos \theta$. Immediately, we conclude $a_{1}=1$ and all other coefficients are 0 . So $w(r, \theta)=r \cos \theta$.

Having found $w$, we can determine the boundary values of $v$ from (9), $g(\theta)=\sin \theta$ and $\left.w_{r}(r, \theta)\right|_{r=1}=\cos \theta$. We have
$$
v(1, \theta)=\frac{1}{2}(\cos \theta-\sin \theta)
$$

Arguing as we did with the solution of the Dirichlet problem for $w$, we see tha solution of the Dirichlet problem with boundary values $\frac{1}{2}(\cos \theta-\sin \theta)$ is $v(r$, $\frac{1}{2} r(\cos \theta-\sin \theta)$. Thus the solution of the biharmonic problem is
$$
u(r, \theta)=\left(1-r^{2}\right) \frac{1}{2} r(\cos \theta-\sin \theta)+r \cos \theta
$$

You should check that this function is indeed a solution. Note that $r \cos \theta$ is monic but $\left(1-r^{2}\right) \frac{1}{2} r(\cos \theta-\sin \theta)$ is not. As a consequence, the function $u$ i harmonic on the disk.

Even though the boundary conditions in Example 2 are somewhat cial, they do illustrate the process of solving a biharmonic equation by ducing to two Dirichlet problems and the role of Fourier series. Here is more illustration.

EXAMPLE 3 Biharmonic function with 0 boundary values
On the unit disk, show that the solution of the boundary value problem
$$
\nabla^{4} u=0, \quad u(1, \theta)=0 \text { and } u_{r}(1, \theta)=g(\theta)
$$
is given by
$$
u(r, \theta)=-\frac{1}{2}\left(1-r^{2}\right)\left[a_{0}+\sum_{n=1}^{\infty} r^{n}\left(a_{n} \cos n \theta+b_{n} \sin n \theta\right)\right]
$$
where $a_{0}, a_{n}$ and $b_{n}$ are the Fourier coefficients of $g$.
Solution By Theorem 1, the solution is of the form
$$
u(r, \theta)=\left(1-r^{2}\right) v+w
$$
where $v$ and $w$ are harmonic functions on the unit disk. Since $w$ is 0 on the boun we conclude that $w$ is identically 0 inside the unit disk. Thus,
$$
u(r, \theta)=\left(1-r^{2}\right) v
$$

---

<!-- Page 50 -->

Left margin note (page 50)

376
Chapter 6
S

To solve the given start with a biharm tion of the form des Exercise 9 and deter constants in order the boundary condit

Right margin note (page 50)

coblem
shows
sult of inates,
$\frac{x y}{2+y^{2}}$.
$\ln r$.
stants.
bound-
$$
)=0 .
$$
1.
$\cos \theta$.
$<\pi$.
$g(\theta)$.
$=0$.

++++

turm-Liouville Theory with Engineering Applications

Using (9) and the fact that $w_{r}=0$, we obtain the boundary values of $v$ :
$$
v(1, \theta)=-\frac{1}{2} g(\theta) .
$$

Using results from Section 4.4, we find that the solution of the Dirichlet p with boundary values $-\frac{1}{2} g(\theta)$ is
$$
v(r, \theta)=-\frac{1}{2}\left[a_{0}+\sum_{n=1}^{\infty} r^{n}\left(a_{n} \cos n \theta+b_{n} \sin n \theta\right)\right],
$$
where $a_{0}, a_{n}$ and $b_{n}$ are the Fourier coefficients of $g$. This determines $v$ and that the desired solution is as claimed.
Exercises 6.6
In Exercises 1-8, verify that the given function is biharmonic. Use the re Example 1 where appropriate. In what follows, $(x, y)$ denote Cartesian coord $(r, \theta)$ polar coordinates, and $n$ an integer.
1. $x^{4}-y^{4}$.
2. $x y^{2}+y x^{2}+x^{3}-2 y^{3}$.
3. $\frac{x^{2}}{x^{2}+y^{2}}$.
4.
5. $\left(1-r^{2}\right) r^{2} \cos 2 \theta$.
6. $r^{3}(\cos \theta+\sin \theta)$.
7. $r^{n+2} \cos n \theta$.
8. $r^{2}$
9. Show that $a r^{2} \ln r+b r^{2}+c \ln r+d$ is biharmonic, where $a, b, c, d$ are con This function is useful in solving the biharmonic equation in an annulus with ary data independent of $\theta$. See Exercises 11 and 12 .
10. Prove (4).

In Exercises 11 and 12, solve the problem that is described in the figure.
11.

![](./images/b6761637-e91c-4988-8637-83a0e794256f-54_408_604_1710_1172.jpg)
Figure 3 for Exercise 11.
12.

![](./images/b6761637-e91c-4988-8637-83a0e794256f-57_412_463_856_24.jpg)
Figure 4 for Exercise 12.
problem, onic funccribed by mine the to satisfy ions.
13. On the unit disk, solve $\nabla^{4} u=0$, subject to $u(1, \theta)=\cos 2 \theta$ and $u_{r}(1, \theta$
14. On the unit disk, solve $\nabla^{4} u=0$, subject to $u(1, \theta)=0$ and $u_{r}(1, \theta)=$
15. On the unit disk, solve $\nabla^{4} u=0$, subject to $u(1, \theta)=1$ and $u_{r}(1, \theta)=$
16. On the unit disk, solve $\nabla^{4} u=0, u(1, \theta)=0$ and $u_{r}(1, \theta)=\theta^{2},-\pi<\theta$
17. On the unit disk, solve $\nabla^{4} u=0$, subject to $u(1, \theta)=0$ and $u_{r}(1, \theta)=$
18. On the unit disk, solve $\nabla^{4} u=0$, subject to $u(1, \theta)=f(\theta)$ and $u_{r}(1, \theta)$

---

<!-- Page 51 -->

Left margin note (page 51)

6.7 Vibratio

Right margin note (page 51)

377

the
$y)$, the ates, oolar ation
gine, oratthe and dary ll be

++++

Section 6.7 Vibrations of Circular Plates

as of Circular Plates
The vibrations of plates are governed by the two-dimensional analog o equation for the vibrations of beams (Section 6.4):
$$
\frac{\partial^{2} u}{\partial t^{2}}+c^{2} \nabla^{4} u=0
$$

Here $u=u(x, y, t)$ denotes the deflection of the plate at the point ( $x$ at time $t>0$, and $\nabla^{4} u$ is the biharmonic operator of $u$, with respect to variables $x$ and $y$. Because of difficulties that arise in Cartesian coordin as we explained in the previous section, we will consider problems in coordinates. On a disk of radius $a>0$ and center at the origin, the equa becomes
$$
u_{t t}+c^{2} \nabla^{4} u=0, \quad 0 \leq r<a, 0 \leq \theta \leq 2 \pi, t>0 .
$$

The appropriate boundary conditions for a clamped plate are
$$
u(a, \theta, t)=0 \text { and } u_{r}(a, \theta, t)=0,
$$
and the initial conditions are
$$
u(r, \theta, 0)=f(r, \theta), u_{t}(r, \theta, 0)=g(r, \theta), 0 \leq r<a, 0 \leq \theta \leq 2 \pi
$$

We will also consider the nonhomogeneous equation
$$
u_{t t}+c^{2} \nabla^{4} u=F(r, \theta, t), \quad 0 \leq r<a, 0 \leq \theta \leq 2 \pi, t>0,
$$
supplied with similar boundary and initial conditions. As you can ima the task ahead of us is at least as complicated as the solution of the vil ing membrane problem from Sections 4.2-4.3. We will first determine eigenvalues and eigenfunctions of the biharmonic operator on the disk, then use the eigenfunction expansion method to solve the stated boun value problems. The good news is that the eigenfunction problem wi reduced to the one that we solved in Section 4.6.

Eigenfunctions of the Biharmonic Operator Consider the eigenvalue problem on a disk of radius $a$,
$$
\nabla^{4} \phi(r, \theta)=k^{4} \phi(r, \theta), 0 \leq r<a, 0 \leq \theta \leq 2 \pi,
$$

---

<!-- Page 52 -->

Left margin note (page 52)

378
Chapter 6

PROPOSI
DILATI
EIGENFUNC

Right margin note (page 52)

ound-conveat the
nvalue nding it the at the
$=k^{4} u$.
they e first
$(\alpha r, \theta)$,
is an
$, \theta)=$

++++

turm-Liouville Theory with Engineering Applications

with the boundary conditions
$$
\phi(a, \theta)=0, \phi_{r}(a, \theta)=0, \quad 0 \leq \theta \leq 2 \pi .
$$

Here we have an additional condition on the normal derivative at the $b$ ary, which we did not have with the Laplacian. Also, for the sake of nience, we wrote the constant in (5) as $k^{4}$. The important fact is th, constant should be positive.

Note that if $\phi$ satisfies $\nabla^{2} \phi= \pm k^{2} \phi$, then
$$
\nabla^{4}(\phi)=\nabla^{2}\left(\nabla^{2} \phi\right)=\nabla^{2}\left( \pm k^{2} \phi\right)= \pm k^{2} \nabla^{2}(\phi)=k^{4} \phi .
$$

So if $\phi$ is an eigenfunction of the Laplacian corresponding to the eiger $\pm k^{2}$, then $\phi$ is an eigenfunction of the biharmonic operator correspo to the eigenvalue $k^{4}$. With this in mind and without worrying abov boundary conditions for now, looking back at Section 4.6, we find th. functions
$$
\phi(r, \theta)=J_{m}(k r) \cos m \theta \text { or } J_{m}(k r) \sin m \theta \quad(m=0,1,2, \ldots)
$$
are solutions of $\nabla^{2} \phi=-k^{2} \phi$, and thus they satisfy the equation $\nabla^{4} u=$ We next ask, What are the nonzero solutions of $\nabla^{2} \phi=+k^{2} \phi$ ? Ar related to the solutions of $\nabla^{2} \phi=-k^{2} \phi$ ? To answer these questions, w prove the following useful proposition.

TION 1 ON OF TIONS

Suppose that $\phi(r, \theta)$ satisfies $\nabla^{2} \phi=\lambda \phi(\lambda \neq 0)$, and let $\psi(r, \theta)=A \phi$ where $A$ and $\alpha$ are nonzero constants. Then $\nabla^{2} \psi=\alpha^{2} \lambda \psi$.

In other words, the radial dilate of an eigenfunction by a factor $\alpha$ eigenfunction that corresponds to the same eigenvalue scaled by $\alpha^{2}$.
Proof The equation $\nabla^{2} \phi=\lambda \phi$ tells us that
$$
\phi_{r r}(r, \theta)+\frac{1}{r} \phi_{r}(r, \theta)+\frac{1}{r^{2}} \phi_{\theta \theta}(r, \theta)=\lambda \phi(r, \theta) .
$$

To avoid confusion, let us denote the radial variable by $\rho$. Then
$$
\phi_{r r}(\rho, \theta)+\frac{1}{\rho} \phi_{r}(\rho, \theta)+\frac{1}{\rho^{2}} \phi_{\theta \theta}(\rho, \theta)=\lambda \phi(\rho, \theta) .
$$

We now compute the Laplacian of $\psi$ using $\psi_{r}(\alpha r, \theta)=A \alpha \phi_{r}(\alpha r, \theta), \psi_{r r}(\alpha A \alpha^{2} \phi_{r r}(\alpha r, \theta)$, and $\psi_{\theta \theta}(\alpha r, \theta)=A \phi_{\theta \theta}(\alpha r, \theta)$ :
$$
\begin{aligned}
\nabla^{2} \psi & =\psi_{r r}(r, \theta)+\frac{1}{r} \psi_{r}(r, \theta)+\frac{1}{r^{2}} \psi_{\theta \theta}(r, \theta) \\
& =A \alpha^{2}\left[\phi_{r r}(\alpha r, \theta)+\frac{1}{(\alpha r)} \phi_{r}(\alpha r, \theta)+\frac{1}{(\alpha r)^{2}} \phi_{\theta \theta}(\alpha r, \theta)\right] \\
& \left.=A \alpha^{2} \nabla^{2} \phi(\alpha r, \theta) \quad \quad \text { (by (8), with } \rho=\alpha r\right) \\
& =A \alpha^{2} \lambda \phi(\alpha r, \theta)=\alpha^{2} \lambda \psi(r, \theta) . \quad
\end{aligned}
$$

---

<!-- Page 53 -->

Left margin note (page 53)

ΨΟίνΨᲪᲫᲫ DINOWYVHIG THLL HO SNOILONOANǴMA I NAYOTHL

Right margin note (page 53)

379
er $m$
hen,
en by
$\mathrm{s} m \theta$,
$k^{4} \phi$.
ction
igen-
(12),
Take
that
$<a$.
(11)

++++

Section 6.7 Vibrations of Circular Plates

This shows that $\psi$ is an eigenfunction that corresponds to the eigenvalue $\alpha^{2} \lambda$
Recall the definition of the modified Bessel function of integer ord (Section 4.7, Exercise 29): $I_{m}(r)=\frac{1}{i^{m}} J_{m}(i r)$. Let
$$
\psi(r, \theta)=I_{m}(k r) \cos m \theta \text { or } I_{m}(k r) \sin m \theta \quad(m=0,1,2, \ldots)
$$

We have $\psi(r, \theta)=\frac{1}{i^{m}} \phi(i r, \theta)$, where $\phi$ is as in (7). Since $\nabla^{2} \phi=-k^{2} \phi$, by Proposition 1,
$$
\nabla^{2} \psi=-k^{2}(i)^{2} \psi=k^{2} \psi \Rightarrow \nabla^{4} \psi=k^{4} \psi
$$

We now summarize our findings and give a formula for the eigenvalues
For $m=0,1,2, \ldots, n=1,2, \ldots$, consider the function $\phi_{m n}(r, \theta)$ give
$$
\left[I_{m}\left(k_{m n} a\right) J_{m}\left(k_{m n} r\right)-J_{m}\left(k_{m n} a\right) I_{m}\left(k_{m n} r\right)\right] \cos m \theta
$$
or
$$
\left[I_{m}\left(k_{m n} a\right) J_{m}\left(k_{m n} r\right)-J_{m}\left(k_{m n} a\right) I_{m n}\left(k_{m n} r\right)\right] \sin m \theta,
$$
where $k_{m n}$ is a positive root of
$$
J_{m}(k a) I_{m}^{\prime}(k a)-I_{m}(k a) J_{m}^{\prime}(k a)=0
$$

Then $\nabla^{4} \phi_{m n}=k_{m n}^{4} \phi_{m n}$ and $\phi_{m n}$ satisfies the boundary conditions ( 6
Proof We have already established that $J_{m}\left(k_{m n} r\right) \cos m \theta, \quad I_{m}\left(k_{m n} r\right) \operatorname{co} J_{m}\left(k_{m n} r\right) \sin m \theta$, and $I_{m}\left(k_{m n} r\right) \sin m \theta$ are all eigenfunctions satisfying $\nabla^{4} \phi=$ Consequently, any linear combination of these functions is also an eigenfun corresponding to $k^{4}$, and, in particular, the functions in (10) and (11) are $\epsilon$ functions corresponding to $k^{4}$. We now show that if $k_{m n}$ is a root of equation then the functions in (10) and (11) also satisfy the boundary conditions (6). $\phi(r, \theta)=\left[I_{m}\left(k_{m n} a\right) J_{m}\left(k_{m n} r\right)-J_{m}\left(k_{m n} a\right) I_{m}\left(k_{m n} r\right)\right] \cos m \theta$. Then
$$
\phi(a, \theta)=\left[I_{m}\left(k_{m n} a\right) J_{m}\left(k_{m n} a\right)-I_{m}\left(k_{m n} a\right) J_{m}\left(k_{m n} a\right)\right] \cos m \theta=0
$$
and
$$
\phi_{r}(a, \theta)=k_{m n}\left[I_{m}\left(k_{m n} a\right) J_{m}^{\prime}\left(k_{m n} a\right)-J_{m}\left(k_{m n} a\right) I_{m}^{\prime}\left(k_{m n} a\right)\right] \cos m \theta=0
$$
because $k_{m n}$ is a root of (12). The same is true if $\phi_{m n}$ is given by (11).
The most important property of the eigenfunctions in Theorem 1 is they form a complete orthogonal set of functions in the disk $0 \leq r$ That is, any two distinct functions $\phi_{m n}$ and $\phi_{m^{\prime} n^{\prime}}$ from the sets (10) or satisfy the orthogonality relation
$$
\int_{0}^{2 \pi} \int_{0}^{a} \phi_{m n}(r, \theta) \phi_{m^{\prime} n^{\prime}}(r, \theta) r d r d \theta=0
$$

---

<!-- Page 54 -->

Left margin note (page 54)

380
Chapter 6 Sturm-Liou

![](./images/b6761637-e91c-4988-8637-83a0e794256f-54_410_442_1708_63.jpg)

Figure 1

![](./images/b6761637-e91c-4988-8637-83a0e794256f-54_408_439_1710_597.jpg)
![](./images/b6761637-e91c-4988-8637-83a0e794256f-54_408_604_1710_1172.jpg)

Right margin note (page 54)

nction
$\cos m \theta$
$\theta]$,
eigenart of more
quires umerinsider
unit do not = 1)
$=0$,
we can mes

++++

ville Theory with Engineering Applications

and any reasonably smooth function $f(r, \theta)$ on the disk has an eigenfu expansion of the form
$$
f(r, \theta)=\sum_{m=0}^{\infty} \sum_{n=1}^{\infty}\left[A_{m n}\left[I_{m}\left(k_{m n} a\right) J_{m}\left(k_{m n} r\right)-J_{m}\left(k_{m n} a\right) I_{m}\left(k_{m n} r\right)\right]\right.
$$
$$
+B_{m n}\left[I_{m}\left(k_{m n} a\right) J_{m}\left(k_{m n} r\right)-J_{m}\left(k_{m n} a\right) I_{m n}\left(k_{m n} r\right)\right] \sin m
$$
where the coefficients are given by the inner product of $f$ against the functions. We will prove these facts when $m=0$ in the second F this section. The general case is similar, but the notation is much cumbersome.

To solve problems with the results that we have derived thus far re knowledge of the eigenvalues, which can be obtained by estimating $n$ cally the solutions of (12). To keep the presentation clear, we will cc radially symmetric problems only.

Radially Symmetric Problems
We will solve radially symmetric cases of equations (1) and (4) on th disk $(a=1)$. When a problem is radially symmetric, the functions depend on $\theta$ and the eigenfunction expansion (14) becomes (with $a=$
$$
f(r)=\sum_{n=1}^{\infty} A_{n}\left[I_{0}\left(k_{n}\right) J_{0}\left(k_{n} r\right)-J_{0}\left(k_{n}\right) I_{0}\left(k_{n} r\right)\right],
$$
where $k_{n}$ is the $n$th positive root of equation (12) with $a=1$ and $m$
$$
J_{0}(k) I_{0}^{\prime}(k)-I_{0}(k) J_{0}^{\prime}(k)=0 .
$$

We know from Section 4.8 that $J_{0}^{\prime}(k)=-J_{1}(k)$ and, in a similar way, prove that $I_{0}^{\prime}(k)=I_{1}(k)$. Thus the equation for the eigenvalues beco
$$
J_{0}(k) I_{1}(k)+I_{0}(k) J_{1}(k)=0 .
$$

![](./images/b6761637-e91c-4988-8637-83a0e794256f-54_408_439_1710_597.jpg)
Figure 2

![](./images/b6761637-e91c-4988-8637-83a0e794256f-54_408_604_1710_1172.jpg)
Figure 3

---

<!-- Page 55 -->

Right margin note (page 55)

381
e 1),
e 2).
llate
esti-
ot is
hese
ons
sion
rals.
or $I_{0}$
er 0 ,

++++

Section 6.7 Vibrations of Circular Plates

The graphs of $J_{0}$ and $J_{1}$ oscillate and have infinitely many zeros (Figur while the graphs of $I_{0}$ and $I_{1}$ are increasing and tend to infinity (Figur It is thus conceivable that the graph of $J_{0}(k) I_{1}(k)+I_{0}(k) J_{1}(k)$ will osci and have infinitely many zeros (Figure 3). Table 1 shows numerical mates of the first six roots. It is interesting to observe that the $n$th ro approximately $n \pi$.

\begin{table}
| $n$ | 1 | 2 | 3 | 4 | 5 | 6 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $k_{n}$ | 3.1962 | 6.3064 | 9.4395 | 12.5771 | 15.7164 | 18.8565 |
| $n \pi$ | 3.1416 | 6.2832 | 9.4248 | 12.5664 | 15.7080 | 18.8496 |
\captionsetup{labelformat=empty}
\caption{Table 1. $k_{n}$, positive roots of $J_{0}(k) I_{1}(k)+I_{0}(k) J_{1}(k)=0$.}
\end{table}

Let us now describe the generalized Fourier coefficients $A_{n}$ in (15). T are derived in the usual way, using the orthogonality of the eigenfuncti
$$
\phi_{n}(r)=I_{0}\left(k_{n}\right) J_{0}\left(k_{n} r\right)-J_{0}\left(k_{n}\right) I_{0}\left(k_{n} r\right)
$$
on the interval $(0,1)$, with respect to the weight $r$. Thus,
$$
A_{n}=\frac{1}{\int_{0}^{1} \phi_{n}(r)^{2} r d r} \int_{0}^{1} f(r) \phi_{n}(r) r d r
$$

To handle integrals involving $J_{0}$ and $I_{0}$ (in particular, to find an expres for $\int_{0}^{1} \phi_{n}(r)^{2} r d r$, we will appeal to various integral identities, such as
$$
\int I_{0}(\lambda x) J_{0}(\lambda x) x d x=\frac{1}{2 \lambda} x\left(I_{1}(\lambda x) J_{0}(\lambda x)+I_{0}(\lambda x) J_{1}(\lambda x)\right)+C
$$

You can verify these identities by simply differentiating to undo the integ You can also derive them by appealing to the differential equations fo and $J_{0}$. Let us illustrate this important technique by proving (20).

Proof of (20). We know that $y=J_{0}(x)$ satisfies Bessel's equation of ord

---

<!-- Page 56 -->

Left margin note (page 56)

382
Chapter 6
Sturm-Liou

Right margin note (page 56)

ises 11
cise to

2
ch will
18).
already

++++

ville Theory with Engineering Applications

$x^{2} y^{\prime \prime}+x y^{\prime}+x^{2} y=0$. Transform the equation as follows:
$$
\begin{array}{rlr}
x y^{\prime \prime}+y^{\prime}+x y & =0 & \text { (Divide by } x . \text { ) } \\
\left(x y^{\prime}\right)^{\prime}+x y & =0 & \text { (Combine the derivatives.) } \\
2 x y^{\prime}\left(x y^{\prime}\right)^{\prime}+x^{2} 2 y y^{\prime} & =0 & \text { (Multiply by } \left.2 x y^{\prime} .\right) \\
\left(\left(x y^{\prime}\right)^{2}\right)^{\prime}+x^{2}\left(y^{2}\right)^{\prime} & =0 & \text { (Chain rule, twice.) } \\
\int\left(\left(x y^{\prime}\right)^{2}\right)^{\prime} d x+\int x^{2}\left(y^{2}\right)^{\prime} d x & =C & \text { (Integrate.) } \\
\left(x y^{\prime}\right)^{2}+\int x^{2}\left(y^{2}\right)^{\prime} d x & =C &
\end{array}
$$

Now $y^{\prime}=J_{0}^{\prime}(x)=J_{1}(x)$. So
$$
x^{2} J_{1}^{2}(x)+\int x^{2}\left(y^{2}\right)^{\prime} d x=C
$$

Evaluate the integral by parts with $u=x^{2}, d v=\left(y^{2}\right)^{\prime} d x, d u=2 x d x, v=$ get
$$
\int x^{2}\left(y^{2}\right)^{\prime} d x=x^{2} y^{2}-2 \int y^{2} x d x
$$

Combining the last two equations and using $y=J_{0}(x)$, we get
$$
x^{2} J_{1}^{2}(x)+x^{2} J_{0}^{2}(x)=2 \int J_{0}^{2}(x) x d x+C
$$
which is equivalent to (20). (Use a change of variables in (20), $t=\lambda x$.)
The other two identities (21) and (22) are proved similarly (Exerc and 12). With the help of these identities and (17), it is a good exer show that
$$
\begin{array}{c}
\int_{0}^{1} \phi_{n}^{2}(r) r d r \\
=\int_{0}^{1}\left[I_{0}\left(k_{n}\right) J_{0}\left(k_{n} r\right)-J_{0}\left(k_{n}\right) I_{0}\left(k_{n} r\right)\right]^{2} r d r \\
=\left[I_{0}\left(k_{n}\right)\right]^{2}\left[J_{0}\left(k_{n}\right)\right]^{2}+\frac{1}{2}\left[I_{0}\left(k_{n}\right)\right]^{2}\left[J_{1}\left(k_{n}\right)\right]^{2}-\frac{1}{2}\left[J_{0}\left(k_{n}\right)\right]^{2}\left[I_{1}\left(k_{n}\right)\right]
\end{array}
$$

We are now ready to compute a simple eigenfunction expansion, whi be needed later to solve a forced vibrations problem.

EXAMPLE 1 An eigenfunction expansion
Expand the function $f(r)=1$ for $0 \leq r<1$ in terms of the eigenfunctions ( Solution We have to evaluate the coefficients $A_{n}$ in the series (15). We have computed the integral $\int_{0}^{1} \phi_{n}(r)^{2} r d r$ in (23). We now compute
$$
\begin{aligned}
\int_{0}^{1} f(r) \phi_{n}(r) r d r & =\int_{0}^{1}\left[I_{0}\left(k_{n}\right) J_{0}\left(k_{n} r\right)-J_{0}\left(k_{n}\right) I_{0}\left(k_{n} r\right)\right] r d r \\
& =I_{0}\left(k_{n}\right) \int_{0}^{1} J_{0}\left(k_{n} r\right) r d r-J_{0}\left(k_{n}\right) \int_{0}^{1} I_{0}\left(k_{n} r\right) r d r
\end{aligned}
$$

---

<!-- Page 57 -->

Left margin note (page 57)

![](./images/b6761637-e91c-4988-8637-83a0e794256f-57_412_463_856_24.jpg)

Figure 4 Eigenfunction expansion of $f(r)=1$, $1<r<1$. Note the overshoot at the endpoints.

Right margin note (page 57)

383

ble 1,
the
start
3).

etric.

++++

Section 6.7 Vibrations of Circular Plates

The first integral on the right side is similar to one that we computed in Examy Section 4.8. We have
$$
\int_{0}^{1} J_{0}\left(k_{n} r\right) r d r=\frac{1}{k_{n}^{2}} \int_{0}^{k_{n}} J_{0}(r) r d r=\left.\frac{1}{k_{n}^{2}} J_{1}(r) r\right|_{0} ^{k_{n}}=\frac{1}{k_{n}} J_{1}\left(k_{n}\right) .
$$

A similar computation using the identity $\int r I_{0}(r) d r=r I_{1}(r)+C$ yields
$$
\int_{0}^{1} I_{0}\left(k_{n} r\right) r d r=\frac{1}{k_{n}} I_{1}\left(k_{n}\right)
$$

Thus,
$$
\int_{0}^{1} f(r) \phi_{n}(r) r d r=\frac{1}{k_{n}}\left(J_{1}\left(k_{n}\right) I_{0}\left(k_{n}\right)-J_{0}\left(k_{n}\right) I_{1}\left(k_{n}\right)\right),
$$
and so, combining (19) and (23), we find
$$
\begin{array}{c}
A_{n}=\frac{1}{k_{n}}\left(J_{1}\left(k_{n}\right) I_{0}\left(k_{n}\right)-J_{0}\left(k_{n}\right) I_{1}\left(k_{n}\right)\right) / \\
\left(\left[I_{0}\left(k_{n}\right)\right]^{2}\left[J_{0}\left(k_{n}\right)\right]^{2}+\frac{1}{2}\left[I_{0}\left(k_{n}\right)\right]^{2}\left[J_{1}\left(k_{n}\right)\right]^{2}-\frac{1}{2}\left[J_{0}\left(k_{n}\right)\right]^{2}\left[I_{1}\left(k_{n}\right)\right]^{2}\right) .
\end{array}
$$

Numerical values of the first six coefficients are shown in Table 2.

\begin{table}
| $n$ | 1 | 2 | 3 | 4 | 5 | 6 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $A_{n}$ | 0.2812 | -0.0145 | 0.0007 | -0.00003 | 0.0 | 0.0 |
\captionsetup{labelformat=empty}
\caption{Table 2. Numerical values of the generalized Fourier coefficients $A_{n}$.}
\end{table}

The eigenfunction expansion is illustrated in Figure 4, where we have plottec third, fifth, and tenth partial sums of the eigenfunction expansion (15).

Next, we examine problems related to the vibrations of plates. We with a radially symmetric version of the boundary value problem (1)-(

EXAMPLE 2 Vibrations of a plate
Solve the equation
$$
u_{t t}+c^{2} \nabla^{4} u=0, \quad 0 \leq r<1,0 \leq \theta \leq 2 \pi, t>0,
$$
subject to the boundary conditions
$$
u(1, \theta, t)=0 \text { and } u_{r}(1, \theta, t)=0,
$$
and the radially symmetric initial conditions
$$
u(r, \theta, 0)=f(r), u_{t}(r, \theta, 0)=0,0 \leq r<a, 0 \leq \theta \leq 2 \pi
$$

Solution We outline a step-by-step strategy.
Step 1. Use a radially symmetric solution, since the data is radially symm Thus, $u(r, \theta, t)=u(r, t)$, and there is no dependence on $\theta$.

---

<!-- Page 58 -->

Left margin note (page 58)

384
Chapter 6
Sturm-Liou

Right margin note (page 58)

of the order
r),
te that ditions.
${ }^{4} \phi_{n}=$ ossible,
qual to
ith the
9). We

++++

ille Theory with Engineering Applications

Step 2. Assume that the solution has an eigenfunction expansion in terms functions in Theorem 1. Since there is no dependence on $\theta$, we only need th 0 Bessel functions. Thus, following (15), we set
$$
u(r, t)=\sum_{n=1}^{\infty} A_{n}(t)\left[I_{0}\left(k_{n}\right) J_{0}\left(k_{n} r\right)-J_{0}\left(k_{n}\right) I_{0}\left(k_{n} r\right)\right]=\sum_{n=1}^{\infty} A_{n}(t) \phi_{n}(
$$
where here, unlike (15), we allow the coefficients $A_{n}$ to be functions of $t$. No because $\phi_{n}(1)=0$ and $\phi_{n}^{\prime}(1)=0$, the series (25) satisfies the boundary cond Now comes the crux of the method.
Step 3: Plug this solution into the equation (24), and use the fact that $k_{n}^{4} \phi_{n}$. Assuming all interchanges of derivatives and summation signs are p we have
$$
\begin{aligned}
\nabla^{4} u(r, t) & =\sum_{n=1}^{\infty} A_{n}(t) \nabla^{4} \phi_{n}(r)=\sum_{n=1}^{\infty} A_{n}(t) k_{n}^{4} \phi_{n}(r) ; \\
\frac{\partial^{2}}{\partial t^{2}} u(r, t) & =\sum_{n=1}^{\infty} \frac{\partial^{2}}{\partial t^{2}} A_{n}(t) \phi_{n}(r)=\sum_{n=1}^{\infty} A_{n}^{\prime \prime}(t) \phi_{n}(r) ; \\
u_{t t}+c^{2} \nabla^{4} u=0 & \Rightarrow \sum_{n=1}^{\infty}\left(A_{n}^{\prime \prime}(t)+k_{n}^{4} c^{2} A_{n}(t)\right) \phi_{n}(r)=0 .
\end{aligned}
$$

The only way for this series to be identically zero is to have all coefficients e 0 . Thus, for all $n$
$$
A_{n}^{\prime \prime}(t)+k_{n}^{4} c^{2} A_{n}(t)=0
$$
and so
$$
A_{n}(t)=\alpha_{n} \cos \left(k_{n}^{2} c t\right)+\beta_{n} \sin \left(k_{n}^{2} c t\right) .
$$

We thus have the solution in the form
$$
u(r, t)=\sum_{n=1}^{\infty}\left(\alpha_{n} \cos \left(k_{n}^{2} c t\right)+\beta_{n} \sin \left(k_{n}^{2} c t\right)\right) \phi_{n}(r) .
$$

Step 4. Determine $\alpha_{n}$ and $\beta_{n}$ by using the initial conditions. Let us start w initial velocity $u_{t}(r, 0)=0$, which implies that
$$
\sum_{n=1}^{\infty} k_{n}^{2} c \beta_{n} \phi_{n}(r)=0,
$$
and so $\beta_{n}=0$ for all $n$. Now the initial condition $u(r, 0)=f(r)$ implies
$$
f(r)=\sum_{n=1}^{\infty} \alpha_{n} \phi_{n}(r) .
$$

Thus $\alpha_{n}$ is the $n$th generalized Fourier coefficient of $f$, which is given by ( 1 conclude that the solution of our problem is
$$
u(r, t)=\sum_{n=1}^{\infty} \alpha_{n} \cos \left(k_{n}^{2} c t\right)\left[I_{0}\left(k_{n}\right) J_{0}\left(k_{n} r\right)-J_{0}\left(k_{n}\right) I_{0}\left(k_{n} r\right)\right],
$$

---

<!-- Page 59 -->

Right margin note (page 59)

385

in
m of
n on
ions
(4),
ime.
tions
n the
asion
es in
ole 1.

ble 1.

++++

Section 6.7 Vibrations of Circular Plates

where, as we just stated, $\alpha_{n}$ is computed using (19).
To solve more general vibration problems, you can repeat the ster the previous solution and modify them as needed. The most general for the solutions is given by a double eigenseries expansion as the one show the right side of (14), where you must allow $A_{m n}$ and $B_{m n}$ to be funct of $t$.

In what follows, we consider a radially symmetric case of equation in which the external force depends only on time and is decaying with t

EXAMPLE 3 Forced vibrations of a plate
Solve the equation
$$
u_{t t}+c^{2} \nabla^{4} u=e^{-t}, \quad 0 \leq r<1,0 \leq \theta \leq 2 \pi, t>0,
$$
subject to the boundary conditions
$$
u(1, \theta, t)=0 \text { and } u_{r}(1, \theta, t)=0
$$
and the radially symmetric initial conditions
$$
u(r, \theta, 0)=0, u_{t}(r, \theta, 0)=0,0 \leq r<a, 0 \leq \theta \leq 2 \pi .
$$

Solution Use a radially symmetric solution and allow the coefficients to be func of $t$ :
$$
u(r, t)=\sum_{n=1}^{\infty} a_{n}(t)\left[I_{0}\left(k_{n}\right) J_{0}\left(k_{n} r\right)-J_{0}\left(k_{n}\right) I_{0}\left(k_{n} r\right)\right]=\sum_{n=1}^{\infty} a_{n}(t) \phi_{n}(r) .
$$

Plug this solution into equation (26), and use the fact that $\nabla^{4} \phi_{n}=k_{n}^{4} \phi_{n}$, as i previous example. Then
$$
u_{t t}+c^{2} \nabla^{4} u=e^{-t} \Rightarrow \sum_{n=1}^{\infty}\left(a_{n}^{\prime \prime}(t)+k_{n}^{4} c^{2}\right) \phi_{n}(r)=e^{-t} .
$$

To go any further, we have to think of the right side as an eigenfunction expas in $r$. Indeed, think of it as $e^{-t} \cdot 1$ and expand the constant function 1 in a seri terms of the $\phi_{n}(r)$. This is precisely the expansion that we computed in Exam Thus,
$$
\sum_{n=1}^{\infty}\left(a_{n}^{\prime \prime}(t)+k_{n}^{4} c^{2} a_{n}(t)\right) \phi_{n}(r)=e^{-t} \overbrace{\sum_{n=1}^{\infty} A_{n} \phi_{n}(r)}^{=1}=\sum_{n=1}^{\infty} A_{n} e^{-t} \phi_{n}(r),
$$
where $A_{n}$ is the (complicated) coefficient in the series expansion in Examp Equating coefficients, we derive the differential equation for $a_{n}(t)$ :
$$
a_{n}^{\prime \prime}(t)+k_{n}^{4} c^{2} a_{n}(t)=A_{n} e^{-t} .
$$

---

<!-- Page 60 -->

Left margin note (page 60)

386
Chapter 6
Sturm-Liou

Right margin note (page 60)

$$
C e^{-t} .
$$
$$
{ }_{n}(t)=
$$
ve each ctions. and the

++++

ville Theory with Engineering Applications

A particular solution $b_{n}(t)$ of this equation can be found by setting $b_{n}(t)=$ Plugging into the equation, we find
$$
C e^{-t}+k_{n}^{4} c^{2} C e^{-t}=A_{n} e^{-t} \Rightarrow C=\frac{A_{n}}{1+k_{n}^{4} c^{2}}
$$

The general solution of the homogeneous equation $a_{n}^{\prime \prime}(t)+k_{n}^{4} c^{2} a_{n}(t)=0$ is $\alpha_{n} \cos k_{n}^{2} c t+\beta_{n} \sin k_{n}^{2} c t$. Thus the general solution of (28) is
$$
a_{n}(t)=\alpha_{n} \cos k_{n}^{2} c t+\beta_{n} \sin k_{n}^{2} c t+\frac{A_{n}}{1+k_{n}^{4} c^{2}} e^{-t} .
$$

The solution of the boundary value problem is now of the form
$$
u(r, t)=\sum_{n=1}^{\infty}\left[\alpha_{n} \cos k_{n}^{2} c t+\beta_{n} \sin k_{n}^{2} c t+\frac{A_{n}}{1+k_{n}^{4} c^{2}} e^{-t}\right] \phi_{n}(r) .
$$

Applying the initial conditions, $u(r, 0)=0$, we get
$$
0=\sum_{n=1}^{\infty}\left[\alpha_{n}+\frac{A_{n}}{1+k_{n}^{4} c^{2}}\right] \phi_{n}(r),
$$
and so $\alpha_{n}=-\frac{A_{n}}{1+k_{n}^{4} c^{2}}$. Applying the initial conditions, $u_{t}(r, 0)=0$, we get
$$
0=\sum_{n=1}^{\infty}\left[k_{n}^{2} c \beta_{n}-\frac{A_{n}}{1+k_{n}^{4} c^{2}}\right] \phi_{n}(r),
$$
and so $\beta_{n}=\frac{A_{n}}{k_{n}^{2} c\left(1+k_{n}^{4} c^{2}\right)}$, which leads us to the solution
$$
u(r, t)=\sum_{n=1}^{\infty}\left[-\cos k_{n}^{2} c t+\frac{1}{k_{n}^{2} c} \sin k_{n}^{2} c t+e^{-t}\right] \frac{A_{n}}{1+k_{n}^{4} c^{2}} \phi_{n}(r) .
$$

The validity of this solution can be checked without too much trouble.
Exercises 6.7
In Exercises 1-10, we list properties of the modified Bessel functions. Pro property by modifying the proof of the corresponding property for Bessel fur Alternatively, you can use the corresponding property of the Bessel function definition of $I_{p}$ from Exercise 29, Section 4.7: $I_{p}(x)=\frac{1}{i^{p}} J_{p}(i x)$.
1. $\left[x^{p} I_{p}(x)\right]^{\prime}=x^{p} I_{p-1}$.
2. $\left[x^{-p} I_{p}(x)\right]^{\prime}=-x^{-p} I_{p+1}$.
3. $x I_{p}^{\prime}(x)=x I_{p-1}(x)-p I_{p}(x)$.
4. $x I_{p}^{\prime}(x)=x I_{p+1}(x)+p I_{p}(x)$.
5. $2 I_{p}^{\prime}(x)=I_{p-1}(x)+I_{p+1}(x)$.
6. $2 p I_{p}^{\prime}(x)=x\left[I_{p-1}(x)-I_{p+1}(x\right.$
7. $I_{-p}(x)=I_{p}(x)$.
8. $\frac{d}{d x} I_{0}(x)=I_{1}(x)$.
9. $\int x^{p+1} I_{p}(x) d x=x^{p+1} I_{p+1}(x)+C$.
10. $\int x^{-p+1} I_{p}(x) d x=-x^{-p+1} I_{p-1}(x)+C$.

---

<!-- Page 61 -->

Right margin note (page 61)

387
ration
proof
the
ctions

++++

Section 6.7 Vibrations of Circular Plates
11. Prove (21) by modifying the proof of (20). (Recall that the differential equ for the modified Bessel function of order 0 is $x^{2} y^{\prime \prime}+x y^{\prime}-x^{2} y=0$.)
12. Project Problem: Proof of (22). Justify each step in the following of (22). Let $y_{1}=J_{0}(x)$ and $y_{2}=J_{1}(x)$. Then
$$
\begin{array}{c}
x\left(y_{1}+y_{2}\right)^{\prime \prime}+\left(y_{1}+y_{2}\right)^{\prime}+x\left(y_{1}-y_{2}\right)=0 \\
{\left[x\left(y_{1}+y_{2}\right)^{\prime}\right]^{\prime}+x\left(y_{1}-y_{2}\right)=0} \\
{\left[\left[x\left(y_{1}+y_{2}\right)^{\prime}\right]^{2}\right]^{\prime}+2 x^{2}\left(y_{1}-y_{2}\right)\left(y_{1}^{\prime}-y_{2}^{\prime}\right)=0} \\
{\left[x\left(y_{1}+y_{2}\right)^{\prime}\right]^{2}=-2 \int x^{2}\left(y_{1}-y_{2}\right)\left(y_{1}^{\prime}-y_{2}^{\prime}\right) d x}
\end{array}
$$

Finish off the proof of (22) by using $y_{1}^{\prime}=-J_{1}(x), y_{2}^{\prime}=I_{1}(x)$, and evaluatir integral by parts. You will also need (20) and (21).
13. Prove (23) by using (20)--(22).
14. Expand the function $f(r)=1-r^{2}$ for $0 \leq r<1$ in terms of the eigenfun (18).
15. Solve equation (24) subject to the boundary conditions
$$
u(1, \theta, t)=0 \text { and } u_{r}(1, \theta, t)=0
$$
and the radially symmetric initial conditions
$$
u(r, \theta, 0)=0, u_{t}(r, \theta, 0)=g(r), 0 \leq r<a, 0 \leq \theta \leq 2 \pi .
$$
16. Solve equation (24) subject to the boundary conditions
$$
u(1, \theta, t)=0 \text { and } u_{r}(1, \theta, t)=0
$$
and the radially symmetric initial conditions
$$
u(r, \theta, 0)=f(r), u_{t}(r, \theta, 0)=g(r), 0 \leq r<a, 0 \leq \theta \leq 2 \pi .
$$
17. Solve equation (26) subject to the boundary conditions
$$
u(1, \theta, t)=0 \text { and } u_{r}(1, \theta, t)=0
$$
and the radially symmetric initial conditions
$$
u(r, \theta, 0)=f(r), u_{t}(r, \theta, 0)=0,0 \leq r<a, 0 \leq \theta \leq 2 \pi .
$$
18. Solve the equation
$$
u_{t t}+c^{2} \nabla^{4} u=1-r^{2}, \quad 0 \leq r<1,0 \leq \theta \leq 2 \pi, t>0,
$$
subject to the boundary conditions
$$
u(1, \theta, t)=0 \text { and } u_{r}(1, \theta, t)=0
$$
and the radially symmetric initial conditions
$$
u(r, \theta, 0)=0, u_{t}(r, \theta, 0)=0,0 \leq r<a, 0 \leq \theta \leq 2 \pi .
$$

---

<!-- Page 62 -->

Left margin note (page 62)

388
Chapter 6 Sturm-Liou

Right margin note (page 62)

tion of tation tation
al sat-
ptotic
$$
\frac{+e^{-i u}}{2},
$$

++++

ville Theory with Engineering Applications
19. Let $u=u(r, \theta, t)$. Solve the equation
$$
u_{t}+c^{2} \nabla^{4} u=0, \quad 0 \leq r<1,0 \leq \theta \leq 2 \pi, t>0,
$$
subject to the boundary conditions
$$
u(1, \theta, t)=0 \text { and } u_{r}(1, \theta, t)=0
$$
and the radially symmetric initial conditions
$$
u(r, \theta, 0)=100,0 \leq r<a, 0 \leq \theta \leq 2 \pi
$$
20. Let $u=u(r, \theta)$. Solve the equation
$$
\nabla^{4} u=100, \quad 0 \leq r<1,0 \leq \theta \leq 2 \pi
$$
subject to the boundary conditions
$$
u(1, \theta, t)=0 \text { and } u_{r}(1, \theta, t)=0
$$
21. Project Problem: Integral representation of $I_{0}(x)$. Recall the defini $I_{0}$ from Exercise 29, Section 4.7: $I_{0}(x)=J_{0}(i x)$. Recall the integral represen
$$
J_{0}(x)=\frac{1}{2 \pi} \int_{-\pi}^{\pi} e^{i x \sin t} d t
$$
(see Section 4.9, Theorem 1 and its proof).
(a) Even though we have not established the validity of the integral represen of $J_{0}$ with complex variables, use it with $i x$ in place of $x$ to obtain
$$
I_{0}(x)=\frac{1}{2 \pi} \int_{-\pi}^{\pi} e^{-x \sin t} d t
$$
(b) Confirm the formula by verifying that the function defined by the integr isfies the modified Bessel equation of order 0: $x^{2} y^{\prime \prime}+x y^{\prime}+x^{2} y=0$.
22. Project Problem: Asymptotics for $I_{0}(x)$. Starting from the asym formula for $J_{0}(x)$ (Theorem 3, Section 4.9) and using the identity $\cos u=\frac{e^{i u}}{e^{u} \text { 的 }}$ show that, as $x \rightarrow \infty$,
$$
I_{0}(x) \sim \frac{1}{\sqrt{2 \pi x}} e^{x}
$$
