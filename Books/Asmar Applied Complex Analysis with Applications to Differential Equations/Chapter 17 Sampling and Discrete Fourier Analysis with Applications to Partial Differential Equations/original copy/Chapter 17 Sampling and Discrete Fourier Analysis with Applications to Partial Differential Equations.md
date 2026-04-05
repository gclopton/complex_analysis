<!-- Page 1 -->

Left margin note (page 1)

Topics to Review
This chapter contains numerical techniques for computing the Fourier transform and Fourier series, and for solving boundary value problems. Sections 10.1 and 10.2 deal with the sampling theorem and some of its applications. They are not required for the rest of the chapter. In Section 10.3 we present the discrete and fast Fourier transforms. In studying this section, it will help to keep in mind the basic properties of the Fourier transform as presented in Section 7.2. Similar properties will be established for the discrete Fourier transform. In Section 10.4 we show a connection between the Fourier transform and the discrete Fourier transform. To appreciate this connection, you need to do the exercises of Section 10.4 which deal with the topics of Sections 7.4 and 7.5.

Looking Ahead...
This chapter introduces basic ideas that are used in the numerical computation of Fourier transforms. With the availability of the fast Fourier transform algorithm as a standard command in many computer algebra systems, we hope that you will be able to experiment with and appreciate the effectiveness of this important algorithm. We also hope that the sample of applications that you will encounter in this chapter will entice you to explore others from the vast and diverse fields where Fourier transforms are applied.

Right margin note (page 1)

AL
ic ideas. EHEAD
ries are se tools al-world les, and ze these er transFourier Fourier
e 1960s ast and as the ss. But mputer-
heorem. Claude mission

++++

10

SAMPLING AND DISCRETE FOURIER ANALYSIS WITH APPLICATIONS TO PARTIAL DIFFERENTI EQUATIONS

Fundamental progress has to do with the reinterpretation of bas
-ALFRED N. WHITI

By now it is clear that the Fourier transform and Fourier se essential tools in applications. To analyze a function with the requires knowledge of the function over a whole interval. In rea applications, functions are measured over discrete sets of valu hence they are usually given as sequences of values. To analy discrete functions, we will introduce and use the discrete Fourie form. Among other important applications of the discrete transform, we will show how we can use it to approximate transforms and solve boundary value problems.

The discrete Fourier transform became widely used in th after the discovery of a numerical algorithm that gives a $f$ efficient method for computing it. This algorithm is known fast Fourier transform. The ideas behind it date back to Gau it was Cooley and Tukey who emphasized its significance to co based Fourier analysis.

Another topic covered in this chapter is the sampling t This important result was discovered by the American engineer Shannon in the 1940s. It has numerous applications to trans and information theory.

---

<!-- Page 2 -->

Left margin note (page 2)

10.1 The Sam

BAND LIM]
FUNCT

It is important to not only $\widehat{f}$ is required to outside a finite interv not $f$. Indeed, it can be that $f$ and $\widehat{f}$ cannot bo ish off a finite interval.

++++

Section 10.1 The Sampling Thoorem

pling Theorem
The sampling theorem is a striking result that states that certain funct; can be reconstructed completely from a discrete set of measurements samples taken at equal intervals. This very important result has many in esting applications, some of which will be discussed in the following scct Let us recall the definition of the Fourier transform
$$
\widehat{f}(\omega)=\frac{1}{\sqrt{2 \pi}} \int_{-\infty}^{x} f(x) e^{-i \omega x} d x, \quad-\infty<\omega<\infty .
$$

We now define a class of functions by a property of the Fourier transfor
[TED [ONS
that vanish al and shown th van-

A function $f(x)$ is called band limited if its Fourier transform $\widehat{f}$ van outside a finite interval. In this case, there is a positive number $W$ such $\widehat{f}(\omega)=0$ for all $|\omega|>W$. Any such number $W$ is called a band widt $f$.

Although "most" functions are not band limited, we can show tha least all the functions that we have dealt with in this text can be appr mated as closely as we want by band limited functions (see Exercises 7 8). This makes the class of band limited functions very useful in applicati

We have encountered many band limited functions before. Here is as ple example that will play an important role in our development.

EXAMPLE 1 A band limited function
(a) The function $s(x)=\frac{\sin x}{x}$ is shown in Figure 1. From the table of For transforms, we find that
$$
\widehat{s}(\omega)=\left\{\begin{array}{ll}
\sqrt{\frac{\pi}{2}} & \text { if }|\omega|<1, \\
\frac{1}{2} \sqrt{\frac{\pi}{2}} & \text { if } \omega= \pm 1, \\
0 & \text { if }|\omega|>1 .
\end{array}\right.
$$

Since $\widehat{s}$ vanishes for all $|\omega|>1$, we conclude that $s$ is band limited with band w 1 (sce Figure 2).

![](./images/6e437500-ecf9-454e-b7bf-eff2df5aa97e-25_361_395_186_574.jpg)
Figure 1 The function $\frac{\sin x}{x}$ is band limited with band width 1 .

![](./images/6e437500-ecf9-454e-b7bf-eff2df5aa97e-25_433_507_119_1223.jpg)
Figure 2 The Fourier transform of s vanishes for all $|\omega|>1$.

---

<!-- Page 3 -->

Left margin note (page 3)

548
Chapter 10 Sampling an

As $W$ increases, the frequency of $\sin W x$ increases, and this causes the graph of $\frac{\sin W x}{W x}$ to be more wavy and more squished toward the origin (Figure 3). On the Fourier transform side, increasing $W$ has the opposite effect of spreading or stretching the graph.

THEOREM 1
PROPERTIES OF BAND LIMITED FUNCTIONS

![](./images/6e437500-ecf9-454e-b7bf-eff2df5aa97e-03_465_580_701_597.jpg)
![](./images/6e437500-ecf9-454e-b7bf-eff2df5aa97e-03_417_644_749_1190.jpg)

Right margin note (page 3)

n Figure te of the
ith band
$$
|\omega|>W
$$
$$
=20
$$
will be
sectively, equal to
$$
f \text { by } a,
$$
avolution
(b), we
vanishes
$$
=\widehat{f} \widehat{g} .
$$
th band

++++

Discrete Fourier Analysis with Applications
(b) Let $W>0$ and consider the function $s_{W^{\prime}}(x)=\frac{\sin W x}{W x}$, which is shown i 3 for various values of $W$. We have $s_{W}(x)=s(W x)$, hence $s_{W^{\prime}}$ is a dila function $s$. Again, from the table of Fourier transforms, we find that
$$
\widehat{s_{W}}\left(\omega^{\prime}\right)=\left\{\begin{array}{ll}
\sqrt{\frac{\pi}{2}} \frac{1}{W} & \text { if }|\omega|<W^{\prime}, \\
\frac{1}{2 W} \sqrt{\frac{\pi}{2}} & \text { if } \omega= \pm W^{\prime}, \\
0 & \text { if }|\omega|>W^{\prime} .
\end{array}\right.
$$

Since $s_{W}$ vanishes for all $|\omega|>W$, we conclude that $s_{W}$ is band limited $w$ width $W$ (see Figure 1).

![](./images/6e437500-ecf9-454e-b7bf-eff2df5aa97e-25_356_465_595_84.jpg)
Figure 3

![](./images/6e437500-ecf9-454e-b7bf-eff2df5aa97e-25_399_616_1652_578.jpg)
Figure 4

We now list some basic properties of band limited functions that useful in building more interesting examples.

Suppose that $a, b$ are constants and $f, g$ are functions.
(a) If $f$ and $g$ are band limited with band widths $W_{1}$ and $W_{2}$, resp then $a f+b g$ is band limited with band width $W$ smaller than or the larger of $W_{1}$ and $W_{2}$.
(b) If $f$ is band limited with band width $W$, then the translate o $f(x-a)$, is also band limited with band width $W$.
(c) If either $f$ or $g$ is band limited with band width $W$, then the cor $f * g$ is also band limited with band width $W$.

Proof Part (a) is straightforward and is left as an exercise. To prove simply recall that
$$
\mathcal{F}(f(x-a))(\omega)=e^{-i a \omega} \widehat{f}(\omega) .
$$

So, if $\widehat{f}$ vanishes for $|\omega|>W$, then clearly the Fourier transform of $f(x-a)$ for $|\omega|>W$. Finally, (c) is an immediate consequence of the fact that $\widehat{f * g}$

Recall that the function $s_{W}$ of Example 1 (b) is band limited wi

---

<!-- Page 4 -->

Left margin note (page 4)

| SNOILONOA GGLINIT-GWIL HOJ NAYOJHL ONITINWS \& NGHOGHL |
| :--- |
| SNOILONOA σέιεινίτ αΝνε HOA NAMOAHL ONITINWVS z NAHOGHL |

Right margin note (page 4)

549

by also out and n of sely its.
have
$n=$
ries the unit ate
this n in $11 \mathrm{C}-$ cise ling
$$
n=
$$
ited

++++

Section 10.1 The Sampling Theorem

width $W$. Shifting this function by $n \pi / W$ yields
$$
s_{W}\left(x-\frac{n \pi}{W}\right)=\frac{\sin (W x-n \pi)}{(W x-n \pi)} .
$$
which is also band limited with band width $W$, by Theorem 1(b). Also Theorem 1(a), any linear combination of functions of the form (2) is band limited with band width $W$. The powerful result that we are al to state tells us that a converse of sorts is also true. That is, every b limited function with band width $W$ can be written as an infinite sur functions of the form (2). Moreover, the coefficients in this sum are preci the values of the function at an evenly spaced discrete set of sample poin

Suppose that $f$ is band limited with band width $W$. Then for all $x$ we
$$
f(x)=\sum_{n=-\infty}^{\infty} f\left(\frac{n \pi}{W}\right) \frac{\sin (W x-n \pi)}{(W x-n \pi)} .
$$

Thus $f$ can be constructed completely from its sample values $f\left(\frac{n \pi}{W}\right)$, $0, \pm 1, \pm 2, \ldots$.

If $W$ and $W^{\prime}$ are two band widths of $f$ with $W^{\prime}>W$, then the se corresponding to $W^{\prime}$ requires more sample points per unit length than one for $W$, since $\frac{\pi}{W^{7}}>\frac{\pi}{W^{7}}$. The least number of sample points per length that is required for (3) to hold is called the Nyquist sampling I and corresponds to the least band width of $f$.

The proof of Theorem 2 is presented in the appendix at the end of section. By reversing the roles of the function and its Fourier transforr the sampling theorem, we obtain a sampling theorem for time-limited f tions. These are functions vanishing outside a finite interval. The pre statement follows. The proof can be reconstructed from that of the samp theorem by interchanging $f$ and $\widehat{f}$.

Suppose that $f(t)=0$ for all $|t|>T$. Then for all $\omega$ we have
$$
\hat{f}(\omega)=\sum_{n=-\infty}^{\infty} \hat{f}\left(\frac{n \pi}{T}\right) \frac{\sin (T \omega-n \pi)}{(T \omega-n \pi)} .
$$

Thus $\widehat{f}$ is completely determined by sampling at the points $\frac{n \pi}{T}$, $0, \pm 1, \pm 2, \ldots$.

In the following example we show how to approximate a band lim function using the sampling theorem.

---

<!-- Page 5 -->

Left margin note (page 5)

550
Chapter 10 Sampling as

![](./images/6e437500-ecf9-454e-b7bf-eff2df5aa97e-05_511_602_1385_608.jpg)

Figure 5 Approximation of a band limited function using sample points. We have a better approximation over the interval where the sample points were chosen.

![](./images/6e437500-ecf9-454e-b7bf-eff2df5aa97e-05_515_595_1385_1241.jpg)

Right margin note (page 5)

width
points
t using ain
$\frac{-5 \pi)}{5 \pi}$.
5. For enerate cept for
$x$
better
d, since
o comampled

++++

ad Discrete Fourier Analysis with Applications

EXAMPLE 2 Sampling of a band limited function
The initial temperature distribution of a bar, $f(x)(-\infty<x<\infty)$, has banc $W=2$. Some of its values are shown in Table 1.

\begin{table}
| $x$ | 0 | $\pi / 2$ | $\pi$ | $3 \pi / 2$ | $2 \pi$ | $5 \pi / 2$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $f(x)$ | .001765 | .382839 | .792567 | .266685 | .0014741 | .03319 |
\captionsetup{labelformat=empty}
\caption{Table 1}
\end{table}

Using the sampling theorem, approximate the initial heat distribution at the .1, .2, .8.

Solution Since $f(x)$ is band limited with band width 2, we can reconstruct (3), by sampling at the points $x=\frac{n \pi}{2}$. Using the values in Table 1, we obt
$$
\begin{aligned}
f(x) \approx & \sum_{n=0}^{5} f\left(\frac{n \pi}{2}\right) \frac{\sin (2 x-n \pi)}{(2 x-n \pi)} \\
= & .001765 \frac{\sin (2 x)}{2 x}+.382839 \frac{\sin (2 x-\pi)}{2 x-\pi}+.792567 \frac{\sin (2 x-2 \pi)}{2 x-2 \pi} \\
& +.266685 \frac{\sin (2 x-3 \pi)}{2 x-3 \pi}+.0014741 \frac{\sin (2 x-4 \pi)}{2 x-4 \pi}+.03319 \frac{\sin (2 x}{2 x}
\end{aligned}
$$

We can now compute the desired values (with the help of a calculator):
$$
f(.1) \approx .0079, \quad f(.2) \approx .0159, \quad f(.8) \approx .1165 .
$$

The graph of $f^{*}$, the partial sum approximation of $f$, is shown in Figure comparison's sake, we have also plotted the function $f$ which was used to $g$ the values in Table 1. (Of course, in real-life applications $f$ is unknown, exc its sampled values.)

![](./images/6e437500-ecf9-454e-b7bf-eff2df5aa97e-25_404_609_1651_1220.jpg)
Figure 5(b) shows that the approximation of $f$ by its partial sum is mucl on the interval $x>0$ compared to the interval $x<0$. This is to be expected all the sample points were chosen from the interval $x \geq 0$.

In the remainder of this section we apply the sampling theorem t pute Fourier transforms of band limited functions, by using only sa

---

<!-- Page 6 -->

Left margin note (page 6)

![](./images/6e437500-ecf9-454e-b7bf-eff2df5aa97e-06_375_452_234_33.jpg)

Figure 6

++++

Section 10.1 The Sampling Theorem

values. Before we state the theorem, we recall the Heaviside step functi
$$
\mathcal{U}_{0}(\omega)=\left\{\begin{array}{ll}
1 & \text { if } \omega>0, \\
0 & \text { otherwise } .
\end{array}\right.
$$

Using translates of this function, we have
$$
\mathcal{U}_{0}(\omega-W)=\left\{\begin{array}{ll}
1 & \text { if } \omega>W, \\
0 & \text { otherwise },
\end{array}\right.
$$
and the step function in Figure 6, which is given by
$$
\mathcal{U}_{0}(\omega+W)-\mathcal{U}_{0}(\omega-W)=\left\{\begin{array}{ll}
1 & \text { if }-W<\omega<W, \\
0 & \text { otherwise } .
\end{array}\right.
$$

Suppose that $f$ is band limited with band width $W$. Then
$$
\widehat{f}(\omega)=\frac{1}{W} \sqrt{\frac{\pi}{2}}\left(\mathcal{U}_{0}(\omega+W)-\mathcal{U}_{0}(\omega-W)\right) \sum_{n=-\infty}^{\infty} f\left(\frac{n \pi}{W}\right) e^{-i n \frac{\pi}{W} \omega} .
$$

Thus to compute the Fourier transform of a band limited function with 1 width $W$, we only need to sample the function on a discrete set of point a sampling rate of $\pi / W$. In the expression on the right side of (5) the fa $\mathcal{U}_{0}(\omega+W)-\mathcal{U}_{0}(\omega-W)$ vanishes for all $|\omega|>W$, which has the effec truncating the whole expression on the right side for all $|\omega|>W$.
Proof The idea is to use the sampling theorem to write $f$ as specified by (3), use (1) to compute the Fourier transform. We have
$$
\begin{aligned}
\hat{f}(\omega) & =\frac{1}{\sqrt{2 \pi}} \int_{-\infty}^{\infty} f(x) e^{-i \omega x} d x \\
& =\sum_{n=-\infty}^{\infty} f\left(\frac{n \pi}{W}\right) \overbrace{\frac{1}{\sqrt{2 \pi}} \int_{-\infty}^{\infty} \frac{\sin (W x-n \pi)}{(W x-n \pi)} e^{-i \omega x} d x}^{\text {Fourier transform of } \sin (W x-n \pi) /(W x-n \pi)} \\
& =\frac{1}{W} \sqrt{\frac{\pi}{2}}\left(\mathcal{U}_{0}(\omega+W)-\mathcal{U}_{0}(\omega-W)\right) \sum_{n=-\infty}^{\infty} f\left(\frac{n \pi}{W}\right) e^{-i n \frac{\pi}{W} \omega} .
\end{aligned}
$$

To justify the last step, you are asked to show that the Fourier transfori $\frac{\sin (W x-n \pi)}{(W x-n \pi)}$ is
$$
\frac{1}{W} \sqrt{\frac{\pi}{2}}\left(\mathcal{U}_{0}(\omega+W)-\mathcal{U}_{0}(\omega-W)\right) e^{-i n \frac{\pi}{W} \omega}=\left\{\begin{array}{ll}
\frac{1}{W} \sqrt{\frac{\pi}{2}} e^{-i n \frac{\pi}{W} \omega} & \text { if }|\omega|<W, \\
0 & \text { otherwise }
\end{array}\right.
$$
(sec Exercise 5).

---

<!-- Page 7 -->

Left margin note (page 7)

552
Chapter 10 Sampling an

THEOREM 5 FOURIER TRANSFORMS OF EVEN FUNCTIONS USING SAMPLING

![](./images/6e437500-ecf9-454e-b7bf-eff2df5aa97e-07_414_396_946_75.jpg)

Figure 7

![](./images/6e437500-ecf9-454e-b7bf-eff2df5aa97e-07_355_442_1433_77.jpg)

Figure 8 Approximation of $\widehat{k}$ using three nonzero terms of the sampled series.

Right margin note (page 7)

ms are

11
$\left.\left.\frac{\tau}{7} \omega\right)\right]$
terms
ed with
tructing
ty good he sum. did not of $\widehat{f}$ by

2, (2))

++++

Discrete Fourier Analysis with Applications

Interesting applications of Theorem 4 to boundary value proble presented in the following section.

The following special case of Theorem 4 is worth noting.

Suppose that $f$ is even and band limited with band width $W$. The
$$
\hat{f}(\omega)=\frac{1}{W} \sqrt{\frac{\pi}{2}}\left(\mathcal{U}_{0}(\omega+W)-\mathcal{U}_{0}(\omega-W)\right)\left[f(0)+2 \sum_{n=1}^{\infty} f\left(\frac{n \pi}{W}\right) \cos \left(\frac{n}{U}\right.\right.
$$

Proof Consider the symmetric partial sums in (5), and add together th corresponding to $n$ and $-n$. Simplify, using $f\left(-\frac{n \pi}{W}\right)=f\left(\frac{n \pi}{W}\right)$ and
$$
e^{i n \frac{\pi}{W} \omega}+e^{-i \frac{n \pi}{W} \omega}=2 \cos \left(n \frac{\pi}{W} \omega\right) .
$$

We illustrate the last two theorems with a numerical example.

EXAMPLE 3 Computing a Fourier transform using sampling Let
$$
k(x)=\frac{\sin ^{2} x}{x^{2}}
$$

From the table of Fourier transforms, we have
$$
\widehat{k}(\omega)=\left\{\begin{array}{ll}
\sqrt{\frac{\pi}{2}}\left(1-\frac{|\omega|}{2}\right) & \text { if }|\omega| \leq 2, \\
0 & \text { otherwise } .
\end{array}\right.
$$

As illustrated in Figure 7, $\widehat{k}$ vanishes outsicle $[-2,2]$, and so $k$ is band limit band width $W=2$. We will verify the assertion of Theorem 5 by recons the Fourier transform from sample values of $f$. Applying (6).
$$
\widehat{k}(\omega)=\frac{1}{2} \sqrt{\frac{\pi}{2}}\left(\mathcal{U}_{0}(\omega+2)-\mathcal{U}_{0}(\omega-2)\right)\left[1+2 \sum_{n=1}^{\infty} \frac{\sin ^{2}\left(\frac{n \pi}{2}\right)}{\left(\frac{n \pi}{2}\right)^{2}} \cos \left(\frac{n \pi}{2} \omega\right)\right.
$$

Note that all the terms for even $n$ are zero, except for $n=0$. A pret approximation of $\widehat{f}$ is obtained by taking only three nonzero terms from t This partial sum approximation of $\widehat{f}$ is shown in Figure 8. Thus, if we know the Fourier transform, we would obtain a pretty good approximation sampling the function at six points: $x=\frac{n \pi}{2}, n=1,2, \ldots, 6$.

Appendix: Proof of the Sampling Theorem
Since $\widehat{f}$ vanishes outside $[-W, W]$, we have by Fourier inversion (Section 7 .
$$
f(x)=\frac{1}{\sqrt{2 \pi}} \int_{-W}^{W} \hat{f}(\omega) e^{j} d \omega
$$

---

<!-- Page 8 -->

Section 10.1 The Sampling Theorem

Also, since $\widehat{f}$ vanishes outside $[-W, W]$, we can extend $\widehat{f}$ periodically (with pe 2 W ) on the $\omega$-axis and then use a Fourier series (Section 2.6, (3)) to represent
$$
\hat{f}(\omega)=\sum_{n=-\infty}^{\infty} c_{n} e^{i \frac{n \pi}{W} \omega}=\sum_{n=-\infty}^{\infty} c_{-n} e^{-i \frac{n \pi}{W} \omega} \quad(|\omega|<W) .
$$

Using the definition of the Fourier coefficients (Section 2.6, (4)) and (7), we ge
$$
c_{-n}=\frac{1}{2 W} \int_{-W}^{W} \widehat{f}(\omega) e^{i \frac{n \pi}{W} \omega} d \omega=\frac{\sqrt{2 \pi}}{2 W} f\left(\frac{n \pi}{W}\right) .
$$

Before we finish off the proof, we evaluate one more integral. Keeping in $n$ Euler's identity ( $e^{i \theta}=\cos \theta+i \sin \theta$ ) and the fact that the integral of an function over a symmetric interval about zero is zero, we have
$$
\begin{aligned}
\frac{1}{2 W} \int_{-W}^{W} e^{-i \frac{n \pi}{W} \omega} e^{i \omega x} d \omega & =\frac{1}{2 W} \int_{-W}^{W} e^{i(W x-n \pi) \omega / W} d \omega \\
& =\frac{1}{2 W} \int_{-W}^{W} \cos \left(\frac{W x-n \pi}{W} \omega\right) d \omega \\
& =\frac{\sin (W x-n \pi)}{W x-n \pi}
\end{aligned}
$$

We can now establish (3) as follows:
$$
\begin{aligned}
f(x) & =\frac{1}{\sqrt{2 \pi}} \int_{-W}^{W} \overbrace{\sum_{n=-\infty}^{\infty} c_{-n} e^{-i \frac{n \pi}{W} \omega} e^{i \omega x} d \omega \quad(\text { by (7) and (8)) }}^{f(\omega)} \\
& =\frac{1}{\sqrt{2 \pi}} \int_{-W}^{W} \overbrace{n=-\infty}^{\infty} \overbrace{\frac{\sqrt{2 \pi}}{2 W} f\left(\frac{n \pi}{W}\right)}^{c_{-n}} e^{-i \frac{n \pi}{W} \omega} e^{i \omega x} d \omega \quad(\text { by (9)) } \\
& =\sum_{n=-\infty}^{\infty} f\left(\frac{n \pi}{W}\right) \frac{1}{2 W} \int_{-W}^{W} e^{-i \frac{n \pi}{W} \omega} e^{i \omega x} d \omega
\end{aligned}
$$
(interchanging the order of the sum and the integral)
$$
=\sum_{n=-\infty}^{\infty} f\left(\frac{n \pi}{W}\right) \frac{\sin (W x-n \pi)}{W x-n \pi} \quad(\text { by }(10)) .
$$

Exercises 10.1
1. Prove Theorem 1, (a) and (c).
2. Use the table of Fourier transforms to decide which of the following funct are band limited. For such functions, determine a band width.
(a) $f(x)=\frac{\sin 2 x}{x}$.
(b) $f(x)=\frac{1-\cos x}{x^{2}}$.
(c) $f(x)=\mathcal{U}_{0}(1-|x|)$.
(d) $f(x)=\frac{\sin ^{4} x}{x^{4}}$.

---

<!-- Page 9 -->

Left margin note (page 9)

554 Chapter 10 Sat

Right margin note (page 9)

on $f(x)$ roxima-
function obtained
$$
\frac{5 \pi / 3}{-0.02}
$$
dth 1.
ntioned rbitrary xercises
of these

++++

npling and Discrete Fourier Analysis with Applications

In Exercises 3-4, you are given the sampled values of a band limited functi and its band width $W$. (a) Use the sampling theorem to construct an app tion of $f(x)$ (see Example 2).
(b) To verify the sampling theorem, in this part you are also given the $f(x)$. Plot and compare $f(x)$ and your approximating function that you in (a).
3. (a) $W=4$,

| $x$ | 0 | $\pm \pi / 4$ | $\pm \pi / 2$ | $\pm 3 \pi / 4$ | $\pm \pi$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $f(x)$ | -0.05068 | -0.24400 | 1.73064 | 1.92217 | -0.15555 |
(b) $f(x)=\sqrt{\frac{2}{\pi}} \frac{\sin ^{2}(2(x-2))-\sin ^{2}(x-2)}{(x-2)^{2}}$.
4. (a) $W=6$,

| $x$ | 0 | $\pi / 6$ | $\pi / 3$ | $\pi / 2$ | $2 \pi / 3$ | $5 \pi / 6$ | $\pi$ | $7 \pi / 6$ | $4 \pi / 3$ | $3 \pi / 2$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $f(x)$ | 3.59 | 0.97 | -0.18 | 0.11 | 0 | 0.04 | -0.05 | 0.02 | 0 | 0.01 |
(b) $f(x)=\frac{4}{3 \sqrt{2 \pi}} \frac{\sin ^{2}(3 x)-\sin ^{2}\left(\frac{3}{2} x\right)}{x^{2}}$.
5. Compute the Fourier transform of $\frac{\sin (W x-n \pi)}{W x-n \pi}$.
6. The table below contains a set of samples of a function $f$ with band wi

| $x$ | $-4 \pi$ | $-3 \pi$ | $-2 \pi$ | $-\pi$ | 0 | $\pi$ | $2 \pi$ | $3 \pi$ | $4 \pi$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $f(x)$ | 0 | 1 | 0 | -1 | 0 | -1 | 0 | 1 | 0 |

Approximate $\widehat{f}$ at the points $\omega=0, \pm .5, \pm .75, \pm 2$.
Project Problem: Approximation by band limited functions. We me in this section that band limited functions can be used to approximate a functions as closely as we want. Do Exercises 7 and 8 to justify this result. 9 and 10 describe alternative proofs.
7. Fejér's kernel. For $n=1,2,3, \ldots$ define
$$
k_{n}(x)=\frac{1}{\sqrt{2 \pi}} n\left(\frac{\sin \left(\frac{1}{2} n x\right)}{\frac{1}{2} n x}\right)^{2}=\frac{4}{\sqrt{2 \pi}} \frac{\sin ^{2}\left(\frac{1}{2} n x\right)}{n x^{2}} .
$$

The function $k_{n}(x)$ is known as a Fejér kernel.
(a) Use the table of Fourier transforms to show that
$$
\widehat{k}_{n}(\omega)=\left(1-\frac{|\omega|}{n}\right) \mathcal{U}_{0}(n-|\omega|) .
$$
(b) Plot the graphs of $k_{n}$ for various values of $n$, and describe the behavior graphs near 0 , as $n$ increases.
(c) Show that $\lim _{n}, \hat{k}_{n}(\omega)=1$ for all $\omega$.
(d) Plot several graphs to illustrate the result in (c).

---

<!-- Page 10 -->

Left margin note (page 10)

10.2 Partial

Right margin note (page 10)

555
are
us $f$
and
$h_{n} *$
Ilée
7).

rier
le la
cerlary

++++

Section 10.2 Partial Differential Equations and the Sampling Theorem
8. In this exercise, we suppose that all functions that we are dealing with defined on the real line and have Fourier transforms.
(a) Let $k_{n}$ be as in Exercise 7. Show that $f * k_{n}$ is band limited.
(b) Use Exercise 7(c) to justify the fact that $\lim _{n \rightarrow \infty} f * k_{n}(x)=f(x)$. may be approximated by the band limited functions $f * k_{n}$.
9. Abel's kernel For $n=1,2, \ldots$ define
$$
h_{n}(t)=\sqrt{\frac{2}{\pi}} \frac{n}{1+n^{2} t^{2}}
$$

The function $h_{n}$ is known as Abel kernel.
(a) Show that $\widehat{h}_{n}(\omega)=e^{-\frac{|\omega|}{n}}$.
(b) Illustrate graphically the fact that as $n \rightarrow \infty$, the graphs of $h_{n}(t)$ are more more concentrated around the origin, while the graphs of $\widehat{h}_{n}(\omega)$ spread out.
(c) Show that $\lim _{n \rightarrow \infty} \widehat{h}_{n}(\omega)=1$. Based on this result, explain why $\lim _{n \rightarrow \infty} f(x)=f(x)$.
10. De la Vallée Poussin kernel. For $n=1,2, \ldots$ define the de la Va Poussin kernel by $v_{n}(t)=2 k_{2 n}(t)-k_{n}(t)$, where $k_{n}$ is Fejér's kernel (Excrcis Show the following.
(a) $v_{n}(t)$ is band limited with band width $2 n$.
(b)
$$
\hat{v}_{n}(\omega)=\left\{\begin{array}{ll}
1 & \text { if }|\omega|<n, \\
0 & \text { if }|\omega|>2 n, \\
(-\omega+2 n) / n & \text { if } n \leq \omega \leq 2 n, \\
(\omega+2 n) / n & \text { if }-2 n \leq \omega \leq-n .
\end{array}\right.
$$

Plot $\widehat{v}_{n}(\omega)$ for $n=1.2, \ldots, 5$. Can you justify calling $\widehat{v}_{n}(\omega)$ a tent function? (c) Obtain the explicit formulas for the de la Vallée Poussin kernel and its For transform
$$
\begin{array}{c}
v_{n}(t)=\frac{4}{\sqrt{2 \pi}} \frac{\sin ^{2}(n t)-\sin ^{2}\left(\frac{1}{2} n t\right)}{n t^{2}}, \\
\widehat{v}_{n}(\omega)=(|2 n+\omega|+|2 n-\omega|-|n+\omega|-|n-\omega|) / 2 n .
\end{array}
$$
(d) Plot the tents $\widehat{v}_{1}(\omega), \widehat{v}_{2}(\omega), \widehat{v}_{4}(\omega)$.
(r) How can you approximate a function by band limited functions using the Vallée Poussin kernel? Justify your answer.

Differential Equations and the Sampling Theorem
In this section, we show how the sampling theorem can be used to solve tain boundary value problems in terms of sample values of initial or bound data. We illustrate the method by considering the heat equation
$$
\frac{\partial u}{\partial t}=c^{2} \frac{\partial^{2} u}{\partial x^{2}}, \quad-\infty<x<\infty, t>0
$$
with initial temperature distribution
$$
u(. r, 0)=f(x)
$$

---

<!-- Page 11 -->

Left margin note (page 11)

556 Chapter 10 Sampling an

Right margin note (page 11)

hat is, ection,
$\omega$, its
rms of e have ted, its pproxy large pproxierature ere we uncered is of r large

++++

Discrete Fourier Analysis with Applications

From (10), Section 7.3, we have the solution
$$
u(x, t)=\frac{1}{\sqrt{2 \pi}} \int_{-\infty}^{\lambda} \widehat{f}(\omega) e^{-c^{2} \omega^{2} t} e^{i \omega x} d \omega
$$

Suppose for now that $f(x)$ is band limited with band width $W$. suppose that $\widehat{f}(\omega)=0$ for $|\omega|>W$. By Theorem 4 of the previous s we have
$$
\widehat{f}(\omega)=\frac{1}{W} \sqrt{\frac{\pi}{2}}\left(\mathcal{U}_{0}(\omega+W)-\mathcal{U}_{0}(\omega-W)\right) \sum_{n=-\infty}^{\infty} f\left(\frac{n \pi}{W}\right) e^{-i \frac{\pi}{W} n \omega}
$$

Substituting this in (3), and using the fact that
$$
\mathcal{U}_{0}(\omega+W)-\mathcal{U}_{0}(\omega-W)=\left\{\begin{array}{ll}
1 & \text { if }|\omega|<W \\
0 & \text { otherwise }
\end{array}\right.
$$
we obtain
$$
\begin{aligned}
u(x, t) & =\frac{1}{2 W} \int_{-W}^{W}\left(\sum_{n=-\infty}^{\infty} f\left(\frac{n \pi}{W}\right) e^{-i \frac{\pi}{W} n \omega}\right) e^{-c^{2} \omega^{2} t} e^{i \omega x} d \omega \\
& =\frac{1}{2 W} \sum_{n=-\infty}^{\infty} f\left(\frac{n \pi}{W}\right) \int_{-W}^{W} e^{-c^{2} \omega^{2} t} e^{i \omega\left(x-n \frac{\pi}{W}\right)} d \omega
\end{aligned}
$$

Since the imaginary part of $e^{-c^{2} \omega^{2} t} e^{i \omega\left(x-n \frac{\pi}{W}\right)}$ is an odd function of integral over a symmetric interval is 0 . Thus, we obtain the formula
$$
u(x, t)=\frac{1}{W} \sum_{n=-\infty}^{\infty} f\left(\frac{n \pi}{W}\right) \int_{0}^{W} e^{-c^{2} \omega^{2} t} \cos \left(\omega\left(x-n \frac{\pi}{W}\right)\right) d \omega
$$

This useful formula expresses the solution of the heat problem in te sample values of the initial temperature distribution $f(x)$. So far w assumed that $f$ is band limited. In general, even if $f$ is not band limi Fourier transform may tend to zero at infinity so fast that we can a imate $f$ very well by a band limited function with an appropriatel value of $W$. In that case, we can still appeal to (5) to obtain an a mation of the solution in terms of sample values of the initial tempe distribution. It should be noted that in this kind of situations (wh are sampling at a few discrete places) there is always a measurement tainty. Therefore, the approximation of the solution being band limit small importance compared to the uncertainty in the values of $f$ (fo enough $W$ ).

We illustrate these ideas with two numerical examples.

---

<!-- Page 12 -->

Left margin note (page 12)

![](./images/6e437500-ecf9-454e-b7bf-eff2df5aa97e-12_504_464_410_37.jpg)

Figure 1 Approxim $u(x, t)$.

![](./images/6e437500-ecf9-454e-b7bf-eff2df5aa97e-12_333_435_1165_42.jpg)

Figure 2

Right margin note (page 12)

557
$$
\frac{\sin ^{2} x}{x^{2}} .
$$
on in band are
ain
grals mate heat of the
$$
x<
$$
heat
ll be
an be
t, we ice of more d the

++++

Section 10.2 Partial Differential Equations and the Sampling Theorem

EXAMPLE 1 A heat problem using sampling
(a) Use (5) to solve the initial value problem (1)-(2), where $c=1$, and $f(x)=$
(b) Approximate your solution by using only a few terms of the series soluti
(a), then plot the approximate solution at time $t=0,1,2,3,4$.

Solution (a) We know from Example 3 of the previous section that $f$ is limited with band width $W=2$. Thus, from (5), we get
$$
u(x, t)=2 \sum_{n=-\infty}^{\infty} \frac{\sin ^{2}\left(\frac{n \pi}{2}\right)}{n^{2} \pi^{2}} \int_{0}^{2} e^{-\omega^{2} t} \cos \left(\omega\left(x-n \frac{\pi}{2}\right)\right) d \omega
$$

Because $\sin ^{2}\left(\frac{n \pi}{2}\right)=0$ for even $n \neq 0$, only the terms with $n=0$ or $n$ od nonzero.
(b) By taking a symmetric partial sum with $n$ ranging from -3 to 3 , we obt:
$$
u(x, t) \approx 2 \sum_{n=-3}^{3} \frac{\sin ^{2}\left(\frac{n \pi}{2}\right)}{n^{2} \pi^{2}} \int_{0}^{2} e^{-\omega^{2} t} \cos \left(\omega\left(. x-n \frac{\pi}{2}\right)\right) d \omega
$$

For each value of $t$, the approximate solution is a function of $x$ in terms of inte that can be evaluated using a computer system. The graphs of the approxi solution at the desired values of $t$ are shown in Figure 1. As expected. the is spreading out and is tending to zero. In Figure 2 we present the graph o approximate solution as a function of ( $r . t$ ) over the rectangular region $-1< 4,0<t<4$.

In the following example we consider a heat problem with an initial distribution that is not band limited. We will show that (5) can sti used to obtain a fairly good approximation of the solution.

EXAMPLE 2 A heat problem with a Gaussian heat distribution Consider the initial value problem (1)-(2), where $c=1$ and $f(x)=e^{-x^{2}}$. It ca shown that in this case the exact solution of (1)-(2) is
$$
u(x, t)=\frac{1}{\sqrt{4 t+1}} e^{-\frac{x^{2}}{4 t+1}}, \quad-\infty<x<\infty, t>0 .
$$
(See Exercise 24, Section 7.4.) Since the Fourier transform of $f(x)=e^{-x^{2}}$ is
$$
\widehat{f}(\omega)=\frac{1}{\sqrt{2}} e^{-\omega^{2} / 4},
$$
we see that $f$ is not band limited. However, because $\widehat{f}$ tends to zero very fas can assume that $f$ is band limited and try a band width $W=2$. (The cho this value yields satisfactory numerical results. as we show below. If you want accurate results, you can take a larger value of W.) Now, (5) does not yiel exact solution, but it will give an approximate solution. We have, from (5).
$$
u(x, t) \approx \frac{1}{2} \sum_{n=-\infty}^{\infty} e^{-\left(\frac{n \pi}{2}\right)^{2}} \int_{0}^{2} e^{-\omega^{2} t} \cos \left(\omega\left(x-n \frac{\pi}{2}\right)\right) d \omega
$$

---

<!-- Page 13 -->

Left margin note (page 13)

558
Chapter 10

![](./images/6e437500-ecf9-454e-b7bf-eff2df5aa97e-13_355_464_303_74.jpg)

Figure 3 Compari exact solution (thic to the approximat (thin graphs).

Right margin note (page 13)

pproxiseries.) of inten. The 3. For t. The tion. If e of the
is exeron 7.5) of the ition of t
unction ed, you form of dth $W^{\prime}$, obtain. dutions ith the

++++

Sampling and Discrete Fourier Analysis with Applications

By taking a partial sum, we get
$$
u(x, t) \approx \frac{1}{2} \sum_{n=-5}^{5} e^{-\left(\frac{n \pi}{2}\right)^{2}} \int_{0}^{2} e^{-\omega^{2} t} \cos \left(\omega\left(x-n \frac{\pi}{2}\right)\right) d \omega
$$
(Here again, the choice of the partial sum yields a satisfactory numerical a mation of the solution. For better results, you can add more terms from the For each value of $t$, the approximate solution is a function of $x$ in terms grals that were evaluated in Example 1, with the help of a computer syster graphs of the approximate solution at various values of $t$ are shown in Figure comparison, we have also plotted the exact solution at the same values of graphs show that we have obtained a pretty good approximation of the solu we want a better approximation, we can repeat the above with a larger valu band width $\mathrm{H}^{-}$.

Exercises 10.2
1. Repeat Example 1 with $f(x)=\frac{\sin x}{x}$.
2. Repeat Example 2 with $f(x)=\frac{1}{1+x^{2}}$.
3. Project Problem: Poisson integral formula with sampling. In th cise, we derive an alternative form of the Poisson integral formula ((5), Secti for band limited functions. The new formula is in terms of sample values boundary function.

Suppose that $f$ is band limited with band width $W$. Show that the soly the Dirichlet problem given by (1) (2). Section 7.5 , is
$$
u(x, y)=\frac{1}{W} \sum_{n=-\infty}^{\infty} f\left(\frac{n \pi}{W}\right) \int_{0}^{W} e^{-y \omega} \cos \left(\omega\left(x-n \frac{\pi}{W}\right)\right) d \omega
$$
[Hint: Use the solution of the Dirichlet problem in Section 7.5 to show tha
$$
u(x, y)=\frac{1}{\sqrt{2 \pi}} \int_{-\infty}^{\infty} \hat{f}(\omega) e^{-y|\omega|} e^{i \omega x} d \omega
$$

Then use Theorem 4 of the previous section.]
4. (a) Show that $f(x)=\frac{1}{1+x^{2}}$ is not band limited.
(b) Suppose that you want to solve the Dirichlet problem with boundary f $f(x)$ given by (a), by using sampled values of $f$. Since $f$ is not band limit cannot use the formula in Exercise 3. However, because the Fourier trans $f$ tends to 0 very fast, you may assume that $f$ is band limited with band wi where $W$ is to be determined according to the accuracy that you wish to Follow the same steps as in Example 2, and derive various approximate so corresponding to different values of $W$. Plot and compare these solutions v exact solution
$$
u(x, y)=\frac{1+y}{x^{2}+(1+y)^{2}} .
$$
(Note: This exact solution can be derived using Exercise 6, Section 7.5.)

---

<!-- Page 14 -->

Left margin note (page 14)

10.3 The Discrete

Right margin note (page 14)

559

tant form r, in and pute ents. s us ge of nited this from urier ge of urier rical ting
sting n , it urier

$N-$
$1\}$.
their
ence

++++

Section 10.3 The Discrete and Fast Fourier Transforms

and Fast Fourier Transforms
As you saw in Chapter 7, the Fourier transform is one of the most impor tools for solving boundary value problems. Computing a Fourier trans requires knowing a function on a continuous set of values. Howeve practical applications, a function is measured on a discrete set of values, for that reason it is important to know how to solve problems and com Fourier transforms from just the knowledge of a discrete set of measurem In Section 10.1 we learned about the sampling theorem, which enable to reconstruct functions and their Fourier transforms from our knowled a discrete set of sampled values. These techniques apply for band-lin functions and can be used to approximate more general functions. In section we will develop new tools for computing Fourier transforms sampled values. These tools are based on the so-called discrete Fo transform (DFT). Not only can this transform be applied to a wide ran functions, but there is a very efficient algorithm, known as the fast Fo transform (FFT), for computing it. Because of this successful nume algorithm, the DFT is the most commonly used method for approxima Fourier transforms.

As a transform that acts on sequences, the DFT has many interes properties similar to those of the Fourier transform. In exploring then will help to recall in your mind the corresponding properties of the Fo transform.

The Discrete Fourier Transform
We will denote a finite sequence of $N$ real or complex numbers, or an sequence, by
$$
x=(x(j))_{j=0}^{N-1}=(x(0), x(1), \ldots, x(N-1)) .
$$

We think of this as a function over the discrete domain $\{0,1, \ldots, N-$
Basic Operations on Sequences
If $x$ and $y$ are two sequences, we define their sum $x+y$, respectively, product, $x y$, by
$$
(x+y)(j)=x(j)+y(j),
$$
respectively,
$$
x y(j)=x(j) y(j) .
$$

Also, if $x$ is a sequence and $a$ is a number, then by $a x$ we mean the sequ whose $j$ th term is $a x(j)$. We now come to a fundamental definition.

---

<!-- Page 15 -->

Left margin note (page 15)

560
('hapter 10

DISCRETE FO
TRANS

Caution: Our defini DFT may differ fr found in the literat

Right margin note (page 15)

-point

num-
tation
re we
n sum
m, we
whole
of the
ppro-
omain
ite the

++++

Sampling and Discrete Fourier Analysis with Applications
URIER
FORM

Given an $N$-sequence $x \approx(x(0), x(1), \ldots, x(N-1))$, we define the $N$ discrete Fourier transform of $x$, abbreviated DFT, by
$$
X(k)=\frac{1}{\sqrt{N}} \sum_{j=0}^{N-1} x(j) e^{2 \pi i j \frac{k}{N}}, \quad k=0,1, \ldots, N-1
$$

Thus the DFT of an $N$-sequence $x$ is another $N$-sequence of comples bers $X=(X(0), X(1), \ldots . X(N-1))$. We will also use the no $X=\mathcal{F}_{N}(x)$.

Note the similarity with the definition of the Fourier transform. multiply the values of the sequence by a complex exponential and the over the whole domain of the sequence. With the Fourier transfor multiply the function by a complex exponential and integrate over the domain of the function. In fact, you will see that many properties Fourier transform will be translated to properties of the DFT by an a priate conversion involving changing an integral over a continuous d to a sum over a discrete domain.

EXAMPLE 1 Computing a DFT
To compute the (4-point) DFT of $x=(0,1,1,-1)$, we appeal to (1) and wr four terms of the DFT as
$$
\mathcal{F}_{4}(x)(k)=\frac{1}{\sqrt{4}} \sum_{j=0}^{3} x:(j) e^{2 \pi i j \frac{k}{4}}, \quad k=0,1,2,3 .
$$

Replacing $x(j)$ by its value, we get for the first term
$$
\mathcal{F}_{4}(x)(0)=\frac{1}{2} \sum_{j=0}^{3} x(j)=\frac{1}{2}(0+1+1+(-1))=\frac{1}{2}
$$

For the second term we have
$$
\begin{aligned}
\mathcal{F}_{4}(x)(1) & =\frac{1}{2} \sum_{j=0}^{3} x(j) e^{i \frac{j \pi}{2}}=\frac{1}{2}\left(0+e^{i \frac{\pi}{2}}+e^{i \pi}-e^{i \frac{3 \pi}{2}}\right) \\
& =\frac{1}{2}\left(\cos \frac{\pi}{2}+i \sin \frac{\pi}{2}+\cos \pi+i \sin \pi \cdots \cos \frac{3 \pi}{2}-i \sin \frac{3 \pi}{2}\right) \\
& =-\frac{1}{2}+i
\end{aligned}
$$

Similarly, we have
$$
\mathcal{F}_{4}(x)(2)=\frac{1}{2} \quad \text { and } \quad \mathcal{F}_{4}(x)(3)=-\frac{1}{2}-i
$$

Thus the DFT of $x=(0,1,1,-1)$ is $X=\left(\frac{1}{2},-\frac{1}{2}+i, \frac{1}{2} .-\frac{1}{2}-i\right)$.

---

<!-- Page 16 -->

Left margin note (page 16)

LAG
SHAL HO NOISHAΛNI I NAYO'SHL

NYOASNV\&L
ΨᲛᲟᲧᲘΟᲰ
ᲤᲡᲪᲧᲔ

Right margin note (page 16)

561
has
T),
arity
ct of
is is
ndix
FT,
then
DFT

++++

Section 10.3 The Discrete and Fast Fourier Transforms

Like other transforms that we have encountered previously, the DFT an inverse, known as the inverse discrete Fourier transform (IDF given by
$$
\mathcal{F}_{N}^{-1}(X)(k)=\frac{1}{\sqrt{N}} \sum_{j=0}^{N-1} X(j) e^{-2 \pi i j \frac{k}{N}}, \quad k=0,1, \ldots, N-1
$$

Thus the IDFT of an $N$-sequence is another $N$-sequence. Note the simila between the two definitions (1) and (2). As you would expect, the effec the inverse transform is to give you back your original sequence. Th expressed in the following theorem whose proof is presented in the appe at the end of the section.

For any $N$-sequence $x$ we have
$$
\mathcal{F}_{N}^{-1}\left(\mathcal{F}_{N}(x)\right)(k)=x(k), \quad k=0,1, \ldots, N-1 .
$$

As an immediate consequence we get the uniqueness property of the D which states that if $x$ and $y$ are two $N$-sequences such that $X=Y$, $x=y$.

EXAMPLE 2 Computing an IDFT
Let $X$ denote the DFT in Example 1. Verify Theorem 1 by computing the I of $X$, using (2).
Solution Applying (2) with $X=\left(\frac{1}{2},-\frac{1}{2}+i, \frac{1}{2},-\frac{1}{2}-i\right)$, we get
$$
\mathcal{F}_{1}^{-1}(X)(k)=\frac{1}{2} \sum_{j=0}^{3} X(j) e^{-2 \pi i j \frac{k}{4}}, \quad k=0,1,2.3
$$

Carrying out the necessary operations and simplifying, we find
$$
\begin{aligned}
& \mathcal{F}_{4}^{-1}(X)(0)=\frac{1}{2} \sum_{j=0}^{3} X(j)=0=x(0) \\
\mathcal{F}_{4}^{-1}(X)(1) & =\frac{1}{2} \sum_{j=0}^{3} X(j) e^{-i \frac{i \pi}{2}} \\
& =\frac{1}{2}\left(\frac{1}{2}+\left(-\frac{1}{2}+i\right) e^{-i \frac{\pi}{2}}+\frac{1}{2} e^{-\pi i}+\left(-\frac{1}{2}-i\right) e^{-i \frac{3 \pi}{2}}\right) \\
& =\frac{1}{2}\left(\frac{1}{2}+\left(-\frac{1}{2}+i\right)(-i)+\frac{1}{2}(-1)+\left(-\frac{1}{2}-i\right) i\right) \\
& =1=x(1)
\end{aligned}
$$

---

<!-- Page 17 -->

Left margin note (page 17)

562
Chapter 10 Sampling as
CONVOLUTION OF
SEQUENCES

Right margin note (page 17)

linear.
s, then

When
the set DFT of allowed omplex
shows ad that at all
infinite an $N$ eriodic or both
dic se-

++++

id Discrete Fourier Analysis with Applications

Similarly, we find that
$$
\mathcal{F}_{4}^{-1}(X)(2)=1=x(2) \quad \text { and } \quad \mathcal{F}_{1}^{\prime}(X)(3)=-1=x(3) .
$$

Thus, as asserted by Theorem 1, we have $\mathcal{F}_{4}^{-1}(X)=\mathcal{F}_{1}^{-1}\left(\mathcal{F}_{1}(x)\right)=x$.
Operational Properties
As you would expect from transforms, the DFT and IDFT are both That is, if $a$ and $b$ are complex numbers and $x$ and $y$ are $N$-sequence
$$
\mathcal{F}_{N}(a r+b y)=a \mathcal{F}_{N}(x)+b \mathcal{F}_{N}(y)
$$
and
$$
\mathcal{F}_{N}^{-1}(a x+b y)=a \mathcal{F}_{N}^{-1}(x)+b \mathcal{F}_{N}^{-1}(y) .
$$

The next property deals with the issue of periodicity of the DFT. we defined the DFT in (1), we restricted $k$ to be an integer in $\{0,1,2, \ldots, N-1\}$. This restriction allowed us to think of the an $N$-sequence as another $N$-sequence. What would happen if we $k$ to be any integer? To answer this question, remember that the c exponential function $e^{z}$ is $2 \pi i$-periodic, and so
$$
e^{2 \pi i j \frac{k+N}{N}}=e^{2 \pi i j \frac{k}{N}+2 \pi i j}=e^{2 \pi i j \frac{k}{N}} e^{2 \pi i j}=e^{2 \pi i j \frac{k}{N}} .
$$

Substituting this in (1), we find that
$$
X(k)=X(k+N),
$$
and hence the DFT is periodic with period $N$. A similar argument that the IDFT is periodic with period $N$. You should keep in mi the notion of periodicity applies only when you evaluate (1) and (2 integers $k$, and not just $k=0,1,2, \ldots, N-1$.

In what follows we shall identify a finite $N$-sequence with the sequence obtained from it by $N$-periodic extension. That is, given sequence $x(k), k=0,1, \ldots, N-1$, we construct an infinite $N$-p sequence by defining $x(k+N)=x(k)$. We use the same notation f finite and infinite sequences without comment.

Given two $N$-sequences $x$ and $y$, with both viewed as $N$-peric quences on the integers, we can define their convolution by
$$
x * y(k)=\frac{1}{\sqrt{N}} \sum_{j=0}^{N-1} x(j) y(k-j), \quad k=0,1, \ldots, N-1 .
$$

---

<!-- Page 18 -->

Right margin note (page 18)

563
$N-$ omAs

encss
after
fol-
gain

++++

Section 10.3 The Discrete and Fast Fourier Transforms

Since $x$ and $y$ are periodic with period $N$, it follows that $x * y$ is also periodic. Using Theorem 2 below, it can be shown that convolution is c mutative, associative, and distributive over addition (see Exercise 7). expected from a convolution, we have the following crucial property.

EM 2
IS OF
IONS

For any two $N$-sequences $x$ and $y$ we have
$$
\mathcal{F}_{N}(x * y)=\mathcal{F}_{N}(x) \mathcal{F}_{N}(y),
$$
and
$$
\mathcal{F}_{N}^{-1}(X Y)=x * y .
$$

Proof Note that the second equality is a consequence of the first one and unique of the DFT. To prove the first equality we use (1) and (4), and we get, interchanging sums,
$$
\mathcal{F}_{N}(x * y)(k)=\frac{1}{\sqrt{N}} \sum_{l=0}^{N-1} x(l) \frac{1}{\sqrt{N}} \sum_{j=0}^{N-1} y(j-l) e^{2 \pi i j \frac{k}{N}} .
$$

Shifting the index of summation in the inner sum, we get
$$
\begin{aligned}
\mathcal{F}_{N}(x * y)(k) & =\frac{1}{\sqrt{N}} \sum_{l=0}^{N-1} x(l) \frac{1}{\sqrt{N}} \sum_{j=-l}^{N-l-1} y(j) e^{2 \pi i(j+l) \frac{k}{N}} \\
& =\overbrace{\frac{1}{\sqrt{N}} \sum_{l=0}^{N-1} x(l) e^{2 \pi i l \frac{k}{N}}}^{\frac{1}{\sqrt{N}} \sum_{j=0}^{N-1} y(j) \epsilon^{2 \pi i j \frac{k}{N}}} \\
& =X(k) Y(k),
\end{aligned}
$$
which proves the theorem.
Theorem 2 can be used to compute convolutions, as we illustrate in the lowing example.

EXAMPLE 3 Convolution of sequences
Let $x=(1,1,1,2)$ and $y=(-1,1,3,-2)$. Find $x * y$.
Solution We first compute the DFT's $X$ and $Y$ with the help of a computer
$$
X=(2.5,-0.5 i,-0.5,0.5 i) \quad \text { and } \quad Y=(0.5,-2+1.5 i, 1.5,-2-1.5 i) .
$$

Thus $X Y^{\prime}=(1.25,0.75+i,-0.75,0.75-i)$ and so with the help of a computer a to compute the IDFT, we find
$$
x * y=\mathcal{F}_{4}^{-1}(X Y)=(1,2,-.5,0) .
$$

---

<!-- Page 19 -->

Left margin note (page 19)

564 Chapter 10 Sampling an

Right margin note (page 19)

puting Tukey portant et $x=$ s given
equired multiomplex (1) reers, we $N$ is a uposite
${ }_{1}+N_{2}$ ) orithm, present orming savings nber of
oute $X$ ys from
$N_{1} . V_{2}$.
m 0 to

++++

Discrete Fourier Analysis with Applications

The Fast Fourier Transform
The fast Fourier transform (FFT) is an efficient algorithm for con the discrete Fourier transform. It was discovered in 1965 by J. W. and J. W. Cooley and is considered one of the century's most imp contributions to numerical analysis. To describe this algorithm, l $\left(x_{0} \cdot r_{1}, \ldots, x_{N} \cdot 1\right)$ be an $N$-sequence of complex numbers. Its $\mathrm{DF}^{\prime} \Gamma \mathrm{i}$ by (1):
$$
X(k)=\frac{1}{\sqrt{N}} \sum_{j=0}^{N-1} x(j) e^{2 \pi i j \frac{k}{v}}, \quad k=0,1, \ldots, N-1
$$

We shall be interested in comparing numbers of operations that are re to perform a DFT. Let us define an elementary operation to be a plication of two complex numbers followed by the addition of two c numbers. It is clear that computing $X(k)$ in the way suggested by quires $N$ elementary operations, and since there are $N$ such numb need $N^{2}$ elementary operations to compute the $N$-sequence $X$. If prime number, there is not much that we can do. But if $N$ is a con number, say
$$
\Lambda=N_{1} \cdot V_{2},
$$
then we will show that we can compute the DFT by performing $N(N$ operations. Before we delve into the technicalities of the FFT alg we discuss how it is usually applied. The same proof that we will shows that if $N=N_{1} N_{2} N_{3}$, then the DFT can be computed by perf $N\left(N_{1}+N_{2}+N_{3}\right)$ elementary operations, and so on. To maximize the using the FFT, in practice, we would choose $N=2^{\nu}$. Then the nu elementary operations required to compute the DFT becomes
$$
N \underbrace{(2+2+\cdots+2)}_{\nu \text { times }}=2 \nu N=2 N \ln _{2} N .
$$

When compared to $N^{2}$, the number of operations required to comy in the most straightforward way, we see that, for large $N$, the saving using the FFT are enormous.

We now explain the ideas behind the FFT for the case when $N=$ For $j, k=0,1,2, \ldots, N-1$, use long division to write
$$
j=j_{1} N_{1}+j_{2}, \quad \text { and } \quad k=k_{1} N_{2}+k_{2} .
$$
where $j_{2}$ and $k_{1}$ range from 0 to $N_{1}-1$, and $j_{1}$ and $k_{2}$ range fro $N_{2}-1$. Then
$$
\begin{aligned}
e^{2 \pi i j k / N} & =e^{2 \pi i\left(j_{1} N_{1}+j_{2}\right)\left(k_{1} N_{2}+k_{2}\right) / N} \\
& =e^{2 \pi i\left(j_{1} k_{1}+j_{1} k_{2} / N_{2}+k_{1} j_{2} / N_{1}+j_{2} k_{2} / N\right)} \\
& =e^{2 \pi i\left(j_{1} k_{2} / N_{2}+k_{1} j_{2} / N_{1}+j_{2} k_{2} / N\right)},
\end{aligned}
$$

---

<!-- Page 20 -->

Right margin note (page 20)

565
ning

d to each nely, aires $0 \leq$ ll of the are ions we 1 the is a the

++++

Section 10.3 The Discrete and Fast Fourier Transforms

because $e^{2 \pi i j_{1} k_{1}}=1$. Putting this in (1), we find that
$$
X(k)=\frac{1}{\sqrt{N}} \sum_{j=0}^{N-1} x(j) e^{2 \pi i\left(j_{1} k_{2} / N_{2}+k_{1} j_{2} / N_{1}+j_{2} k_{2} / N\right)} .
$$

Now summing over all the $j=0,1, \ldots, N-1$ is the same thing as sumn over all $j_{1}=0,1, \ldots, N_{2}-1$ and all $j_{2}=0,1, \ldots, N_{1}-1$. Thus,
$$
\begin{aligned}
X(k) & =\frac{1}{\sqrt{N}} \sum_{j_{2}=0}^{N_{1}-1} e^{2 \pi i\left(k_{1} j_{2} / N_{1}+j_{2} k_{2} / N\right)} \sum_{j_{1}=0}^{N_{2}-1} x\left(j_{1} N_{1}+j_{2}\right) e^{2 \pi i j_{1} k_{2} / N_{2}} \\
& =\frac{1}{\sqrt{N}} \sum_{j_{2}=0}^{N_{1}-1} e^{2 \pi i\left(k_{1} j_{2} / N_{1}+j_{2} k_{2} / N\right)} C\left(j_{2}, k_{2}\right)
\end{aligned}
$$
where
$$
C\left(j_{2}, k_{2}\right)=\sum_{j_{1}=0}^{N_{2}-1} x\left(j_{1} N_{1}+j_{2}\right) e^{2 \pi i j_{1} k_{2} / N_{2}} .
$$

We are now ready to count the number of elementary operations require compute all the $X(k)$ 's. The most important step is to observe that $C\left(j_{2}, k_{2}\right)$ appears in the computation of $X(k)$ for $N_{1}$ different $k$ 's, nan $k=k_{2}, N_{2}+k_{2}, 2 N_{2}+k_{2}, \ldots,\left(N_{1}-1\right) N_{2}+k_{2}$. Each $C\left(j_{2}, k_{2}\right)$ requ $N_{2}$ elementary operations. Since there are $N C\left(j_{2}, k_{2}\right)$ (recall that $j_{2} \leq N_{1}-1,0 \leq k_{2} \leq N_{2}-1$ ), we need $N N_{2}$ operations to compute a them. Having computed all the $C\left(j_{2}, k_{2}\right)$, we use them in (5) to compute $X(k)$ 's. From (5), it takes $N_{1}$ operations to compute $X(k)$. Since there $N$ of them, we need $N N_{1}$ operations. Hence the total number of operat
$$
N N_{2}+N N_{1}=N\left(N_{1}+N_{2}\right),
$$
as claimed.
Appendix: Proof of Theorem 1
We start by establishing an interesting identity. For $j, k=0,1.2, \ldots, N-$ have
$$
\sum_{n=0}^{N-1} e^{2 \pi i n \frac{j-k}{N}}=\left\{\begin{array}{ll}
0 & \text { if } j \neq k, \\
N & \text { if } j=k .
\end{array}\right.
$$

Note that the second part of the identity is obvious, since if $j=k$, each term in sum is 1 , and so the total sum is $N$. To prove the first part, we write
$$
e^{2 \pi i n \frac{j-k}{N}}=z^{n} .
$$
where $z=e^{2 \pi i \frac{i-k}{N}}$. With this notation, it becomes clear that the sum in (6) gcometric sum which equals $\frac{1-z^{N}}{1-z}$. Since $z^{N}=e^{2 \pi i(j-k)}=1$, it follows that

---

<!-- Page 21 -->

Left margin note (page 21)

566
Chapter 10
Sar

Right margin note (page 21)

oroof of
$x y$, (d)

Exercise
ting the
$=y * x$,
$y$ are as
te other
unit for
ny $l$

++++

mpling and Discrete Fourier Analysis with Applications

sum is 0 as claimed (note that for $j \neq k, z \neq 1$ ). With (6) in hand, the Theorem 1 becomes straightforward. Using (1) and (2), we get
$$
\begin{aligned}
\mathcal{F}_{N}^{-1}\left(\mathcal{F}_{N}(x)\right)(k) & =\frac{1}{\sqrt{N}} \sum_{n=0}^{N-1} \overbrace{\frac{1}{\sqrt{N}} \sum_{j=0}^{N-1} x(j) e^{2 \pi i j \frac{n}{N}}}^{X(n)} e^{-2 \pi i n \frac{k}{N}} \\
& =\frac{1}{N} \sum_{j=0}^{N-1} x(j) \sum_{n=0}^{N-1} e^{2 \pi i(j-k) \frac{n}{N}}
\end{aligned}
$$

By (6), the inner sum is zero unless $j=k$, in which case the sum is $N$. Th
$$
\mathcal{F}_{N}^{-1}\left(\mathcal{F}_{N}(x)\right)(k)=\frac{1}{N} x(k) N=x(k),
$$
which completes the proof.
Exercises 10.3
1. Let $x=(1,2,3)$ and $y=(4,-1,0)$. Compute (a) $x+y$, (b) $x-2 y$, (c) $x(x+y)$, (e) $X$, (f) $Y$.
2. Compute $\mathcal{F}_{3} x$ and $\mathcal{F}_{3}^{-1} x$ for the given $x$.
(a) $x=(0,1,1)$.
(b) $x=(-1,0,1)$.
(c) $x=(-1,1,2)$.
[Hint: For (c), use your results from (a) and (b).]
In Exercises $3-4$, compute $X, Y$, and $x * y$, using the method of Example 3
3. $x=(1,2,0,1), y=(1,1,1,1)$.
4. $x=(0,0,1,-1), y=(1,2,-1,1)$.
5. Compute $x * y(0)$ and $x * y(1)$ directly from (4), where $x$ and $y$ are as in I
3. [Hint: Extend $y$ periodically before you carry out the computation.]
6. Let $x$ and $y$ be as in Exercise 1. Show that $x * y=y * x$ by comput convolutions using (1).
7. Use Theorem 2 to show that for any $N$-sequences $x, y, z$, we have $x * y x *(y * z)=(x * y) * z$, and $x *(y+z)=x * y+x * z$.
8. Use the method of Example 3 to compute $x * y, y * x, x * y * z$, where $x$, in Exercise 3 and $z=(1,-1,0,0)$.
9. Let $\epsilon$ denote the $N$-sequence in which the first term is $\sqrt{N}$ and all th terms are 0 .
(a) Show that $\mathcal{F}_{N}(\epsilon)(k)=1$ for all $k$.
(b) Conclude from (a) that $\epsilon * x=x$ for all $N$-sequences $x$. Thus $\epsilon$ is the the operation of convolution for $N$-sequences.
10. Sums of periodic sequences.
(a) Suppose that $(f(n))_{n=-\infty}^{\infty}$ is an $N$-periodic sequence. Show that for a
$$
\sum_{n=0}^{N-1} f(n)=\sum_{n=1}^{N+l-1} f(n) .
$$

---

<!-- Page 22 -->

Left margin note (page 22)

10.4 The Fourier

Right margin note (page 22)

567
tant.
roof
o $N$ -
rties
d by
urier
tion
egral
inite
etter
]eft-
nber

++++

Section 10.4 The Fourier and Discrete Fourier Transforms

Thus the sum of any $N$ consecutive terms of an $N$-periodic sequence is cons This result is the analog of Theorem 1, Section 2.1. To prove it, mimic the outlined in Exercise 18, Section 2.1.
(b) Conclude from (a) that for any $N$-sequence $y$, we have
$$
Y(k)=\frac{1}{\sqrt{N}} \sum_{j=-1}^{N-1-1} y(j) e^{2 \pi i j \frac{k}{N}} .
$$
[Hint: Remember that $y$ is $N$-periodic and show that $\left(e^{2 \pi i j \frac{k}{N}}\right)_{j=-\infty}^{\infty}$ is als periodic.]
11. Let $x$ be an $N$-sequence and $k$ an integer. Establish the following prope of the DFT and its inverse. Assume $x$ is real-valued in parts (a) and (d).
(a) $\mathcal{F}_{N}(x)(k)=\overline{\mathcal{F}_{N}(x)(-k)}$.
(b) $\mathcal{F}_{N}(x)(-k)=\mathcal{F}_{N^{-}}^{-1}(x)(k)$.
(c) $\mathcal{F}_{N}(x)(-k)=\mathcal{F}_{N}(x)(N-k)$.
(d) $\mathcal{F}_{N}(x)(N-k)=\overline{\mathcal{F}_{N}(x)(k)}$.
and Discrete Fourier Transforms
In this section we show how the Fourier transform can be approximate the discrete Fourier transform. This will enable us to use the fast Fo transform to approximate Fourier transforms numerically. The connec that we explore is based on a Riemann sum approximation of the inte defining the Fourier transform
$$
\widehat{f}(\omega)=\frac{1}{\sqrt{2 \pi}} \int_{-\infty}^{\infty} f(x) e^{-i \omega x} d x, \quad-\infty<\omega<\infty
$$

To simplify the presentation, we start with a special case.
CASE I: $f(x)=0$ for all $x<0$. Then (1) becomes
$$
\widehat{f}(\omega)=\frac{1}{\sqrt{2 \pi}} \int_{0}^{\infty} f(x) e^{-i \omega x} d x, \quad-\infty<\omega<\infty
$$

Now suppose that the improper integral can be approximated by a def integral over a finite range as follows:
$$
\widehat{f}(\omega) \approx \frac{1}{\sqrt{2 \pi}} \int_{0}^{M I} f(x) e^{-i \omega x} d x, \quad-\infty<\omega<\infty
$$
where $M$ is a fixed large number. The larger the value of $M$, the be the approximation of $\widehat{f}$. We now approximate the definite integral by a endpoint Riemann sum, with increments $\Delta x=\frac{M}{N}$, where $N$ is the nu of subdivisions of the interval $[0, M]$, and get
$$
\begin{aligned}
\widehat{f}(\omega) & \approx \frac{1}{\sqrt{2 \pi}} \frac{M}{N} \sum_{j=0}^{N-1} f\left(j \frac{M}{N}\right) e^{-i \omega j \frac{M}{N}} \\
& =\frac{M}{\sqrt{2 N \pi}} \frac{1}{\sqrt{N}} \sum_{j=0}^{N-1} f\left(j \frac{M}{N}\right) e^{-i \omega j \frac{M}{N}} .
\end{aligned}
$$

---

<!-- Page 23 -->

Left margin note (page 23)

568
Chapter 10 Sampling at

Right margin note (page 23)

we find liscrete e
t to (1) $d x$. hat

++++

id Discrete Fourier Analysis with Applications

Evaluating $\widehat{f}$ at $\omega=\frac{2 \pi k}{M}$, for $k=0,1, \ldots, N-1$, we get
$$
\widehat{f}\left(\frac{2 \pi k}{M}\right) \approx \frac{M}{\sqrt{2 N} \pi} \overbrace{\frac{1}{\sqrt{N}} \sum_{j=1}^{N-1} f\left(j \frac{M}{N}\right) e^{-i \frac{2 \pi k}{N} j}}^{\operatorname{IDFT} \text { of }\left(f\left(j \frac{M}{N}\right)\right)_{j=0}^{N-1}}
$$

Comparing this with the definition of the IDFT ((2), Section 10.3), that the values of $\widehat{f}\left(\frac{2 \pi k}{M}\right)$ are given by a scalar multiple of the inverse Fourier transform of the sequence $\left(f\left(j \frac{M I}{N}\right)\right)_{j-0}^{N-1}$. In symbols, we hav
$$
\widehat{f}\left(\frac{2 \pi k}{M}\right) \approx \frac{M}{\sqrt{2 N \pi}} \mathcal{F}_{N}^{-1}\left(f\left(j \frac{M}{N}\right)\right)(k), \quad k=0,1, \ldots, N-1 .
$$

Evaluating $\widehat{f}$ at negative values and using a similar argument, we ge
$$
\widehat{f}\left(-\frac{2 \pi k}{M}\right) \approx \frac{M}{\sqrt{2 N \pi}} \mathcal{F}_{N}\left(f\left(j \frac{M}{N}\right)\right)(k), \quad k=0,1, \ldots, N-1
$$

Case II: $f$ is an arbitrary function defined for all $x$. We go back and choose a very large value of $M$ so that
$$
\widehat{f}(\omega) \approx \frac{1}{\sqrt{2 \pi}} \int_{-M / 2}^{M / 2} f(x) e^{-i \omega x} d x, \quad-\infty<\omega<\infty
$$

Splitting the integral and changing variables, we get
$$
\widehat{f}(\omega) \approx \frac{1}{\sqrt{2 \pi}} \int_{M / 2}^{M} f(x-M) e^{-i \omega(x-M)} d x+\frac{1}{\sqrt{2 \pi}} \int_{0}^{M / 2} f(x) e^{-i \omega x}
$$

Evaluating at $\omega=\frac{2 \pi k}{M}$, for $k=0,1, \ldots, N-1$, and using the fact t
$$
e^{-i \frac{2 \pi k}{M}(x-M)}=e^{-i \frac{2 \pi k}{M} x} e^{i 2 \pi k}=e^{-i \frac{2 \pi k}{M} x},
$$
we get
$$
\begin{aligned}
\widehat{f}\left(\frac{2 \pi k}{M}\right) \approx & \frac{1}{\sqrt{2 \pi}} \int_{M / 2}^{M} f(x-M) e^{-i \frac{2 \pi k}{M} x} d x \\
& +\frac{1}{\sqrt{2 \pi}} \int_{0}^{M / 2} f(x) e^{-i \frac{2 \pi k}{M} x} d x
\end{aligned}
$$

---

<!-- Page 24 -->

Left margin note (page 24)

Caution: This app tion is good only fo $0.1 \ldots, N / 2$. See the sion following Exampl low, and particularly (

Right margin note (page 24)

569
$I / 2]$
can

orm DFT $N-$ sizes ome test We

++++

Section 10.4 The Fourier and Discrete Fourier Transforms

Now define a function $g$ by
$$
g(x)=\left\{\begin{array}{ll}
0 & \text { if } x<0, \\
f(x) & \text { if } 0 \leq x \leq \frac{M}{2}, \\
f(x-M) & \text { if } \frac{M}{2} \leq x \leq M, \\
0 & \text { if } x>M .
\end{array}\right.
$$

Note that $g$ fits Case I. It is constructed by cutting off $f$ outside $[-M / 2, \lambda$ and translating the portion over $[-M / 2,0]$ to $[M / 2, M]$. Using (7), we rewrite the right side of (6) in terms of $g$, as follows:
$$
\begin{aligned}
\widehat{f}\left(\frac{2 \pi k}{M}\right) & \approx \frac{1}{\sqrt{2 \pi}} \int_{0}^{\Lambda I} g(x) e^{-i \frac{2 \pi k}{M} x} d x \\
& =\frac{1}{\sqrt{2 \pi}} \int_{-\infty}^{\infty} g(x) e^{-i \frac{2 \pi k}{U} x} d x=\widehat{g}\left(\frac{2 \pi k}{M}\right)
\end{aligned}
$$

Since $g$ fits Case I, we can apply (4) to approximate $\widehat{g}$. Thus
$$
\hat{f}\left(\frac{2 \pi k}{M}\right) \approx \frac{M}{\sqrt{2 N \pi}} \mathcal{F}_{N}^{-1}\left(g\left(j \frac{M}{N}\right)\right)(k), \quad k=0,1, \ldots, N-1 .
$$

This is the formula that we are aiming for. It expresses the Fourier transf of $f$ in terms of an inverse discrete Fourier transform. Notice that the II is really a discrete Fourier transform evaluated at $-k$ for $k=0,1,2, \ldots$, 1. There are several important comments to be made about the relatives of $M, N$, and $k$. These remarks will be more meaningful as we look at s numerical examples.

In the following example, we use a well-known Fourier transform to the validity and accuracy of the formulas that we have derived thus far

EXAMPLE 1 Approximation of the Fourier transform
Consider the function $f(x)=1$ if $-1<x<1$ and 0 otherwise (Figure 1). have, from the table of Fourier transforms,
$$
\widehat{f}(\omega)=\sqrt{\frac{2}{\pi}} \frac{\sin \omega}{\omega}, \quad-\infty<\omega<\infty .
$$

---

<!-- Page 25 -->

Left margin note (page 25)

570
Chapter 10 Sampling an

![](./images/6e437500-ecf9-454e-b7bf-eff2df5aa97e-25_361_395_186_574.jpg)

Figure 3 Graph of $g(x)$.

![](./images/6e437500-ecf9-454e-b7bf-eff2df5aa97e-25_433_507_119_1223.jpg)
![](./images/6e437500-ecf9-454e-b7bf-eff2df5aa97e-25_356_465_595_84.jpg)
![](./images/6e437500-ecf9-454e-b7bf-eff2df5aa97e-25_399_616_1652_578.jpg)
![](./images/6e437500-ecf9-454e-b7bf-eff2df5aa97e-25_404_609_1651_1220.jpg)

Right margin note (page 25)

discrete $N=2^{6}$,
generate
to form from 0 ansform aphs are e. There dic with to get a icity, we
$\omega$
40
FT and

++++

Discrete Fourier Analysis with Applications

![](./images/6e437500-ecf9-454e-b7bf-eff2df5aa97e-25_361_395_186_574.jpg)
Figure 1 Graph of $f(x)$.

![](./images/6e437500-ecf9-454e-b7bf-eff2df5aa97e-25_433_507_119_1223.jpg)
Figure 2 Graph of $\hat{f}(\omega)$.

The graph of this transform is shown in Figure 2. Our goal is to use a Fourier transform to approximate $\widehat{f}$. For this purpose, we apply (8) with $M=10$, and compute the IDFT of the sequence
$$
x=\left(g\left(j \frac{10}{2^{6}}\right)\right)_{j=0}^{2^{6}-1},
$$
where $g(x)$ is given by (7). (The graph of $g$ is shown in Figure 3.) This will approximate values of the Fourier transform at the points
$$
\omega=\frac{2 \pi k}{10} \quad k=0,1,2, \ldots, 2^{6}-1 .
$$

The resulting values are plotted in Figure 4 and connected by line scgments a continuous graph. As $k$ ranges from 0 to $2^{6}-1$, the values of $\omega$ vary to $\frac{2 \pi(63)}{10} \approx 40$. In Figure 5, we superposed the graphs of the Fourier tr and the one in Figure 4, for comparison's sake. Notice that the two gre pretty close near 0 , but as we get beyond 20 the approximation gets worse is an important reason for this phenomenon. Recall that the IDFT is perio period $N$, but the Fourier transform is not. So, in general, it is impossible good approximation past the points $k= \pm N / 2$. Indeed, because of period have
$$
\operatorname{IDFT}(x)(-k)=\operatorname{IDFT}(x)(N-k) .
$$

![](./images/6e437500-ecf9-454e-b7bf-eff2df5aa97e-25_399_616_1652_578.jpg)
Figure 4 Graph of the IDFT.

![](./images/6e437500-ecf9-454e-b7bf-eff2df5aa97e-25_404_609_1651_1220.jpg)
Figure 5 Comparison of the ID the Fourier transform.

---

<!-- Page 26 -->

Left margin note (page 26)

![](./images/6e437500-ecf9-454e-b7bf-eff2df5aa97e-26_419_471_613_0.jpg)

Figure 6

![](./images/6e437500-ecf9-454e-b7bf-eff2df5aa97e-26_395_705_633_435.jpg)
![](./images/6e437500-ecf9-454e-b7bf-eff2df5aa97e-26_401_665_631_1146.jpg)

Right margin note (page 26)

571

ield a ed in econd over d the n the o our over ${ }^{0}$ ).

20
m by
It
the

ond-ond1 the
d $N$. techusing

++++

Section 10.4 The Fourier and Discrete Fouricr Transforms

Thus, we expect the points corresponding to $k=N / 2, N / 2+1, \ldots, N-1$ to y good approximation of the Fourier transform at $\omega=\frac{-2 \pi(N-k)}{10}$. This is illustra Figure 6, where the portion of the graph in Figure 4, corresponding to the se half of the $\omega$-interval (those values of $\omega$ between 20 and 40 ), is translated to the negative $\omega$-axis. In Figure 7 we combined the graphs in Figure 6 an first half in Figure 5 to form our approximation of the Fourier transform o interval ( $-20,20$ ). Finally, in Figure 8 we compared the Fourier transform $t$ approximation in Figure 7. As you can see, the approximation is quite good the entire interval. You can obtain better results by increasing $N$ (try $N=2^{1}$

![](./images/6e437500-ecf9-454e-b7bf-eff2df5aa97e-26_395_705_633_435.jpg)
Figure 7

![](./images/6e437500-ecf9-454e-b7bf-eff2df5aa97e-26_401_665_631_1146.jpg)
Figure 8

Let us now outline a method for approximating the Fourier transfor the IDFT, following the steps in Example 1.

DFT Approximation of the Fourier Transform
Step 1: Choose and fix $M$ and $N$ to prepare for the application of (8 is customary to choose V to be a power of 2 .
Step 2: Form the function $g$ as described by (7). On the $\omega$-axis, mar points
$$
\omega=\frac{2 \pi k}{M}, \quad k=0, \pm 1, \ldots, \pm N / 2 .
$$

Step 3: To approximate the Fourier transform at the points $\omega$ corresp ing to $k=0,1, \ldots, N / 2$, use (8).
Step 4: 'To approximate the Fourier transform at the points $\omega$ corresp ing to $k=-1, \ldots,-\frac{N}{2}+1$, use (11). This amounts to using (8) in following form: For $k=1,2, \ldots, N / 2$,
$$
\widehat{f}\left(-\frac{2 \pi k}{M}\right) \approx \frac{M}{\sqrt{2 N \pi}} \mathcal{F}_{N}^{-1}\left(g\left(j \frac{M}{N}\right)\right)(N-k) .
$$

Step 5: For better results, repeat Steps 1-4 with larger values of $M$ an The methods of this section can be applied to develop numerical niques for approximating Fourier series and convolution of functions by the IDFT. These important techniques are described in the exercises.

---

<!-- Page 27 -->

Left margin note (page 27)

572
Chapter 10 Sal

Right margin note (page 27)

pute its and its
be two nula for

Using a
lly, with $\left.-t_{j}\right)=$ former
ns using ed using
esults of imation.
out this on 2.6). icient of
se $c_{k} \approx$
and its

++++

npling and Discrete Fourier Analysis with Applications

Exercises 10.4
In Exprises 1-4, find $\widehat{f}$ in the table of Fourier transforms and then com approximation as we did in Example 1. Plot and compare the graphs of $\hat{f}$ approximation.
1. $f(x)=e^{-x^{2}}$.
2. $f(x)=e^{-|x|}$.
3. $f(x)=\frac{\sin ^{2} x}{x^{2}}$.
4. $f(x)=\frac{1}{1+x^{2}}$.
5. Approximation of the convolution by the DFT. Let $f$ and $g$ functions defined on the real line, and recall from Section 7.2, (3), the form the convolution: $f * g(x)=\frac{1}{\sqrt{2 \pi}} \int_{-\infty}^{\infty} f(x-t) g(t) d t$.
(a) Pick a large number $M$ so that $f * g(x) \approx \frac{1}{\sqrt{2 \pi}} \int_{-M}^{M} f(x-t) g(t) d t$. left-endpoint Riemann sum approximation, argue that
$$
f * g(x) \approx \frac{2 M}{N \sqrt{2 \pi}} \sum_{j=0}^{N-1} f\left(x-t_{j}\right) g\left(t_{j}\right)
$$
where $t_{j}=-M+j \frac{2 M}{N}$.
(b) Let $\boldsymbol{f}=\left(f\left(t_{j}\right)\right)_{j=0}^{N-1}, \boldsymbol{g}=\left(g\left(t_{j}\right)\right)_{j=0}^{N-1}$. Extend both sequences periodica period $N$. For $m=0, \pm 1, \pm 2, \ldots$, let $x_{m}=m \frac{2 M}{N}$. Show that $f\left(x_{m}\right. \boldsymbol{f}\left(t_{m-\jmath}\right)$. (Here we are using the notation $\boldsymbol{f}\left(x_{m}\right)$ instead of $\boldsymbol{f}(m)$, since th is more suggestive.) Conclude that
$$
f * g\left(x_{m}\right) \approx \frac{2 M}{\sqrt{2 \pi N}} f * g\left(x_{m}\right)
$$

This formula provides a way to approximate the convolution of two functio the DFT, since we know that convolutions of two sequences can be evaluat the DFT.
In Exercises $6-7$, compute $f * g$ directly and then approximate $f * g$ using the $r$ Excrise 5. Plot and compare the graphs of the function $f * g$ and its approx
6. $f(x)=g(x)=\mathcal{U}_{0}(x+1)-\mathcal{U}_{0}(x-1)$ (see Section 7.2, Example 3).
7. $f(x)=x e^{-x^{2}}, g(x)=e^{-x^{2}}$ (see Section 7.2, Exercise 45).
8. Relationship between Fourier series and the DFT. Through exercisc. we will be dealing with the complex form of Fourier series (Secti Suppose that $f$ is a $T$-periodic function, and let $c_{k}$ denote the Fourier coeff $f$ (see (4), Section 2.6).
(a) Show that $c_{-k} \approx \frac{1}{N} \sum_{j=0}^{N-1} f\left(j \frac{T}{N}\right) e^{2 \pi i j k / N}$.
(b) Let $\boldsymbol{f}=\left(f\left(j \frac{T}{N}\right)\right)_{j=0}^{N-1}$. Show that $c_{-k} \approx \frac{1}{\sqrt{N}} \mathcal{F}_{N}(\boldsymbol{f})(k)$, and likew $\frac{1}{\sqrt{N}} \mathcal{F}_{N}^{-1}(\boldsymbol{f})(k)$. (As a rule of thumb, this formula is good for $|k| \leq N / 8$.)
(c) Conclude that $f(x) \approx \frac{1}{\sqrt{N}} \sum_{|k| \leq N / 8} \mathcal{F}_{N}^{-1}(f)(k) e^{2 \pi i k x / T}$.

In Exercises 9-10, test the validity of the rrsults of Exercise 8 by plotting $f$ approximation given by Exercise 8(c).
9. $f(x)=\frac{1}{2}(\pi-x)$ for $0<x<2 \pi, T=2 \pi$.
10. $f(x)=\sin x$ for $-\pi<x<\pi, T=2 \pi$.
