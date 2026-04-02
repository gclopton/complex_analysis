## Topics to Review

Fourier scrics (Sections 2.1-2.4) and the separation of variables method (Section 3.3) are crucial in this chapter. Section 4.1 is self-contained. It presents the Laplacian in polar, cylindrical, and spherical coordinates. Sections 4.2 and 4.3 deal with the vibrating circular membrane. These require knowledge of Bessel functions (Sections 4.7, 4.8) and Fourier series. Section 4.4 requires Fourier series. For Section 4.5, further properties of Bessel functions from Sections 4.7 and 4.8 are needed. Section 4.6 develops the eigenfunction expansions method on the disk. For this section, it is recommended to review the material of Section 3.9.

## Looking Ahead...

You recall from Section 3.6 how by varying the boundary conditions we were led to new types of series expansions. In this chapter we will solve boundary value problems over circular and cylindrical domains. It should not surprise you that the solutions will entail new series expansions; for example, Bessel series. These series look quite complicated at first, but with the help of a computer system, you will be able to plot them and see that they behave very much like Fourier series. The ideas of this chapter will be developed further in Chapter 5, where we will consider problems in spherical coordinates, giving rise to new families of special functions.

## 4

# PARTIAL DIFFERENTIAL EQUATIONS IN POLAR AND CYLINDRICAL COORDINATES 

One cannot understand ... the universality of laws of nature, the relationship of things, without an understanding of mathematics. There is no other way to do it.
-RICHARD P. FEYNMAN

In the previous chapter we used our knowledge of Fourier series to solve several interesting boundary value problems by the method of separation of variables. The success of our method depended to a large extent on the fact that the domains under consideration were easily described in Cartesian coordinates. In this chapter we address problems where the domains are easily described in polar and cylindrical coordinates. Specifically, we consider boundary value problems for the wave, heat, Laplace, and Poisson equations over disks or cylinders. Upon restating these problems in suitable coordinate systems and separating variables, we will encounter new ordinary differential equations, Bessel's equation, whose solutions are called Bessel functions. The full implementation of the separation of variables method will lead us to study expansions of functions in terms of Bessel functions in ways analogous to Fourier series expansions.

You do not need to know about Bessel series to start the chapter. As needed, we will refer to Sections 4.7 and 4.8, where you will find a comprehensive treatment of these special series expansions. Section 4.9 contains mostly proofs of interesting properties of Bessel functions, with surprising connections to Fourier series. This section can be omitted without affecting the rest of the chapter.

### 4.1 The Laplacian in Various Coordinate Systems

The two dimensional Laplacian and its higher dimensional versions are of paramount importance in applications. They appear, for example, in the wave and heat equations, and also in Laplace's equation. In previous sections we solved these equations over rectangular and box shaped regions. To extend our applications to regions such as the disk, the sphere or the cylinder, it is to our advantage to use new coordinate systems in which the region and its boundary have simple expressions. For example, for problems over a disk we change to polar coordinates, where the equation of a circle centered at the origin reduces to $r=a$. Similarly, problems over spheres are simplified by a change to spherical coordinates. For later applications, in this section we express the Laplacian in various coordinate systems.

## The Laplacian in Polar Coordinates

We recall the relationship between rectangular and polar coordinates

$$
\begin{array}{cc}
x=r \cos \theta, & y=r \sin \theta \\
r^{2}=x^{2}+y^{2}, & \tan \theta=\frac{y}{x}
\end{array}
$$

(Since the inverse tangent takes its values in the interval ( $-\pi / 2, \pi / 2$ ), we have $\theta=\tan ^{-1}\left(\frac{y}{x}\right) \pm k \pi$, where $k=0,1$, or -1 , depending on whether $x>0, x<0$ and $y \geq 0$, or $x<0$ and $y<0$. Also, if $x=0$, then $\theta=\pi / 2$ if $y>0$ and $-\pi / 2$ if $y<0$. See Figure 1.) Differentiating $r^{2}=x^{2}+y^{2}$ with respect to $x$, we obtain

$$
2 r \frac{\partial r}{\partial x}=2 x \quad \text { or } \quad \frac{\partial r}{\partial x}=\frac{x}{r} .
$$

![](./images/1c611338-958a-44f7-9d79-2dde87e6ac2a-02_359_370_1357_63.jpg)
Figure 1 Polar coordinates.

Differentiating a second time with respect to $x$ and simplifying, we obtain

$$
\frac{\partial^{2} r}{\partial x^{2}}=\frac{r-x \frac{\partial r}{\partial x}}{r^{2}}=\frac{r-x \frac{x}{r}}{r^{2}}=\frac{r^{2}-x^{2}}{r^{3}}=\frac{y^{2}}{r^{3}}
$$

Differentiating $\theta=\tan ^{-1} \frac{y}{x} \pm \pi$ with respect to $x$ yields

$$
\frac{\partial \theta}{\partial x}=\frac{1}{1+\left(\frac{y}{x}\right)^{2}}\left(-\frac{y}{x^{2}}\right)=-\frac{y}{r^{2}} .
$$

Differentiating a second time with respect to $x$ and simplifying yields

$$
\frac{\partial^{2} \theta}{\partial x^{2}}=\frac{2 y}{r^{3}} \frac{\partial r}{\partial x}=\frac{2 x y}{r^{4}} .
$$

Differentiating now with respect to $y$, we obtain in a similar way

$$
\frac{\partial r}{\partial y}=\frac{y}{r}, \frac{\partial \theta}{\partial y}=\frac{x}{r^{2}}, \text { and } \frac{\partial^{2} r}{\partial y^{2}}=\frac{x^{2}}{r^{3}}, \frac{\partial^{2} \theta}{\partial y^{2}}=-\frac{2 x y}{r^{4}} .
$$

(Check these identities.) From what we have done so far, it is easy to derive the following interesting identities

$$
\frac{\partial^{2} \theta}{\partial x^{2}}+\frac{\partial^{2} \theta}{\partial y^{2}}=0
$$

and

$$
\frac{\partial \theta}{\partial x} \frac{\partial r}{\partial x}+\frac{\partial \theta}{\partial y} \frac{\partial r}{\partial y}=0
$$

We are now ready to change to polar coordinates in the Laplacian. Using the chain rule in two dimensions, we have

$$
\frac{\partial u}{\partial x}=\frac{\partial u}{\partial r} \frac{\partial r}{\partial x}+\frac{\partial u}{\partial \theta} \frac{\partial \theta}{\partial x}
$$

Applying the product rule for differentiation and the chain rule, we obtain

$$
\begin{aligned}
\frac{\partial^{2} u}{\partial x^{2}}= & \frac{\partial}{\partial x}\left(\frac{\partial u}{\partial r}\right) \frac{\partial r}{\partial x}+\frac{\partial u}{\partial r} \frac{\partial^{2} r}{\partial x^{2}}+\frac{\partial}{\partial x}\left(\frac{\partial u}{\partial \theta}\right) \frac{\partial \theta}{\partial x}+\frac{\partial u}{\partial \theta} \frac{\partial^{2} \theta}{\partial x^{2}} \\
= & \left(\frac{\partial^{2} u}{\partial r^{2}} \frac{\partial r}{\partial x}+\frac{\partial^{2} u}{\partial r \partial \theta} \frac{\partial \theta}{\partial x}\right) \frac{\partial r}{\partial x}+\frac{\partial u}{\partial r} \frac{\partial^{2} r}{\partial x^{2}} \\
& +\left(\frac{\partial^{2} u}{\partial r \partial \theta} \frac{\partial r}{\partial x}+\frac{\partial^{2} u}{\partial \theta^{2}} \frac{\partial \theta}{\partial x}\right) \frac{\partial \theta}{\partial x}+\frac{\partial u}{\partial \theta} \frac{\partial^{2} \theta}{\partial x^{2}} \\
= & \frac{\partial^{2} u}{\partial r^{2}}\left(\frac{\partial r}{\partial x}\right)^{2}+2 \frac{\partial^{2} u}{\partial r \partial \theta} \frac{\partial \theta}{\partial x} \frac{\partial r}{\partial x}+\frac{\partial u}{\partial r} \frac{\partial^{2} r}{\partial x^{2}} \\
& +\frac{\partial^{2} u}{\partial \theta^{2}}\left(\frac{\partial \theta}{\partial x}\right)^{2}+\frac{\partial u}{\partial \theta} \frac{\partial^{2} \theta}{\partial x^{2}} .
\end{aligned}
$$

Changing $x$ to $y$, we obtain

$$
\frac{\partial^{2} u}{\partial y^{2}}=\frac{\partial^{2} u}{\partial r^{2}}\left(\frac{\partial r}{\partial y}\right)^{2}+2 \frac{\partial^{2} u}{\partial r \partial \theta} \frac{\partial \theta}{\partial y} \frac{\partial r}{\partial y}+\frac{\partial u}{\partial r} \frac{\partial^{2} r}{\partial y^{2}}+\frac{\partial^{2} u}{\partial \theta^{2}}\left(\frac{\partial \theta}{\partial y}\right)^{2}+\frac{\partial u}{\partial \theta} \frac{\partial^{2} \theta}{\partial y^{2}} .
$$

Adding and simplifying with the help of (1) and (2), we get

$$
\begin{aligned}
\frac{\partial^{2} u}{\partial x^{2}}+\frac{\partial^{2} u}{\partial y^{2}}= & \frac{\partial^{2} u}{\partial r^{2}}\left\{\left(\frac{\partial r}{\partial x}\right)^{2}+\left(\frac{\partial r}{\partial y}\right)^{2}\right\}+2 \frac{\partial^{2} u}{\partial r \partial \theta}\left\{\frac{\partial \theta}{\partial x} \frac{\partial r}{\partial x}+\frac{\partial \theta}{\partial y} \frac{\partial r}{\partial y}\right\} \\
& +\frac{\partial u}{\partial r}\left\{\frac{\partial^{2} r}{\partial x^{2}}+\frac{\partial^{2} r}{\partial y^{2}}\right\}+\frac{\partial^{2} u}{\partial \theta^{2}}\left\{\left(\frac{\partial \theta}{\partial x}\right)^{2}+\left(\frac{\partial \theta}{\partial y}\right)^{2}\right\} \\
& +\frac{\partial u}{\partial \theta}\left\{\frac{\partial^{2} \theta}{\partial x^{2}}+\frac{\partial^{2} \theta}{\partial y^{2}}\right\} \\
= & \frac{\partial^{2} u}{\partial r^{2}}\left\{\left(\frac{\partial r}{\partial x}\right)^{2}+\left(\frac{\partial r}{\partial y}\right)^{2}\right\}+\frac{\partial u}{\partial r}\left\{\frac{\partial^{2} r}{\partial x^{2}}+\frac{\partial^{2} r}{\partial y^{2}}\right\} \\
& +\frac{\partial^{2} u}{\partial \theta^{2}}\left\{\left(\frac{\partial \theta}{\partial x}\right)^{2}+\left(\frac{\partial \theta}{\partial y}\right)^{2}\right\}
\end{aligned}
$$

![](./images/1c611338-958a-44f7-9d79-2dde87e6ac2a-04_410_392_913_63.jpg)
Figure 2 Cylindrical coordinates.

We should note that there is no unanimity about which spherical coordinates to call $\theta$ and which to call $\phi$. Calculus texts tend to use $\theta$ for longitude and $\phi$ for colatitude. Our notation is more common in physics texts and hence more convenient for the physical applications of Chapter 5.

Replacing the partial derivatives with respect to $x$ and $y$ by their expressions in terms of $r$ and $\theta$, we arrive at

$$
\frac{\partial^{2} u}{\partial x^{2}}+\frac{\partial^{2} u}{\partial y^{2}}=\frac{\partial^{2} u}{\partial r^{2}}\left(\frac{x^{2}}{r^{2}}+\frac{y^{2}}{r^{2}}\right)+\frac{\partial u}{\partial r}\left(\frac{x^{2}}{r^{3}}+\frac{y^{2}}{r^{3}}\right)+\frac{\partial^{2} u}{\partial \theta^{2}}\left(\frac{x^{2}}{r^{4}}+\frac{y^{2}}{r^{4}}\right) .
$$

Simplifying with the help of the identity $x^{2}+y^{2}=r^{2}$, we get the polar form of the Laplacian

$$
\Delta u=\nabla^{2} u=\frac{\partial^{2} u}{\partial r^{2}}+\frac{1}{r} \frac{\partial u}{\partial r}+\frac{1}{r^{2}} \frac{\partial^{2} u}{\partial \theta^{2}}
$$

## The Laplacian in Cylindrical Coordinates

If $u$ is a function of three variables $x, y$, and $z$, the Laplacian is

$$
\Delta u=\nabla^{2} u=\frac{\partial^{2} u}{\partial x^{2}}+\frac{\partial^{2} u}{\partial y^{2}}+\frac{\partial^{2} u}{\partial z^{2}}
$$

The relationships between rectangular and cylindrical coordinates are

$$
x=\rho \cos \phi, \quad y=\rho \sin \phi, \quad z=z
$$

where we now use $\rho$ and $\phi$ to denote polar coordinates in the $x y$-plane as illustrated in Figure 2. The cylindrical form of the Laplacian is now evident from (3):

$$
\Delta u=\nabla^{2} u=\frac{\partial^{2} u}{\partial \rho^{2}}+\frac{1}{\rho} \frac{\partial u}{\partial \rho}+\frac{1}{\rho^{2}} \frac{\partial^{2} u}{\partial \phi^{2}}+\frac{\partial^{2} u}{\partial z^{2}}
$$

## The Laplacian in Spherical Coordinates

We will use $(r, \theta, \phi)$ to denote the spherical coordinates of the point $(x, y, z)$. We have

$$
\begin{gathered}
x=r \cos \phi \sin \theta, \quad y=r \sin \phi \sin \theta, \quad z=r \cos \theta \\
r^{2}=x^{2}+y^{2}+z^{2}
\end{gathered}
$$

From the geometry in Figure 3, we have

$$
\rho=r \sin \theta, \quad x=\rho \cos \phi, \quad y=\rho \sin \phi, \quad \rho^{2}=x^{2}+y^{2} .
$$

![](./images/1c611338-958a-44f7-9d79-2dde87e6ac2a-05_409_436_306_42.jpg)
Figure 3 Spherical coordinates.

Our goal is to express $\nabla^{2} u$ in terms of $r, \theta$, and $\phi$. From the polar form of the Laplacian (3), we have

$$
\frac{\partial^{2} u}{\partial x^{2}}+\frac{\partial^{2} u}{\partial y^{2}}=\frac{\partial^{2} u}{\partial \rho^{2}}+\frac{1}{\rho} \frac{\partial u}{\partial \rho}+\frac{1}{\rho^{2}} \frac{\partial^{2} u}{\partial \phi^{2}} .
$$

Observe that the relations

$$
z=r \cos \theta, \quad \rho=r \sin \theta
$$

are analogous to those between polar and rectangular coordinates. So, by using again the polar form of the Laplacian with $z$ and $\rho$ (in place of $x$ and $y$ ), we get from (3)

$$
\frac{\partial^{2} u}{\partial z^{2}}+\frac{\partial^{2} u}{\partial \rho^{2}}=\frac{\partial^{2} u}{\partial r^{2}}+\frac{1}{r} \frac{\partial u}{\partial r}+\frac{1}{r^{2}} \frac{\partial^{2} u}{\partial \theta^{2}} .
$$

Adding $\frac{\partial^{2} u}{\partial z^{2}}$ to (5) and using (6) gives

$$
\frac{\partial^{2} u}{\partial x^{2}}+\frac{\partial^{2} u}{\partial y^{2}}+\frac{\partial^{2} u}{\partial z^{2}}=\frac{\partial^{2} u}{\partial r^{2}}+\frac{1}{r} \frac{\partial u}{\partial r}+\frac{1}{r^{2}} \frac{\partial^{2} u}{\partial \theta^{2}}+\frac{1}{\rho} \frac{\partial u}{\partial \rho}+\frac{1}{\rho^{2}} \frac{\partial^{2} u}{\partial \phi^{2}} .
$$

It remains to express $\partial u / \partial \rho$ in spherical coordinates. From the relation $\theta=\tan ^{-1}(\rho / z)$, we get

$$
\frac{\partial \theta}{\partial \rho}=\frac{1}{1+(\rho / z)^{2}} \frac{1}{z}=\frac{z}{z^{2}+\rho^{2}}=\frac{z}{r^{2}}=\frac{\cos \theta}{r} .
$$

Differentiating $\rho=r \sin \theta$ with respect to $\rho$, we get

$$
1=\frac{\partial r}{\partial \rho} \sin \theta+r \cos \theta \frac{\partial \theta}{\partial \rho}=\frac{\partial r}{\partial \rho} \sin \theta+\cos ^{2} \theta .
$$

Hence

$$
\frac{\partial r}{\partial \rho}=\frac{1-\cos ^{2} \theta}{\sin \theta}=\sin \theta .
$$

Now note that $\phi$ and $\rho$ are polar coordinates in the $x y$-plane, hence $\partial \phi / \partial \rho=$ 0 . Using the chain rule, we get

$$
\frac{\partial u}{\partial \rho}=\frac{\partial u}{\partial r} \frac{\partial r}{\partial \rho}+\frac{\partial u}{\partial \theta} \frac{\partial \theta}{\partial \rho}+\frac{\partial u}{\partial \phi} \frac{\partial \phi}{\partial \rho}=\frac{\partial u}{\partial r} \frac{\rho}{r}+\frac{\partial u}{\partial \theta} \frac{\cos \theta}{r} .
$$

Substituting this in (7) and simplifying, we get the spherical form of the Laplacian:
(8) $\Delta u=\nabla^{2} u=\frac{\partial^{2} u}{\partial r^{2}}+\frac{2}{r} \frac{\partial u}{\partial r}+\frac{1}{r^{2}}\left(\frac{\partial^{2} u}{\partial \theta^{2}}+\cot \theta \frac{\partial u}{\partial \theta}+\csc ^{2} \theta \frac{\partial^{2} u}{\partial \phi^{2}}\right)$.

EXAMPLE 1 Use spherical coordinates to compute the Laplacian of

$$
f(x, y, z)=\ln \left(x^{2}+y^{2}+z^{2}\right), \quad(x, y, z) \neq(0,0,0)
$$

Solution In spherical coordinates, we have

$$
f(r, \theta, \phi)=\ln r^{2}=2 \ln r
$$

Since $f$ is independent of $\theta$ and $\phi$, all partial derivatives in these variables are zero. From (8) we get

$$
\nabla^{2} f=\frac{\partial^{2} f}{\partial r^{2}}+\frac{2}{r} \frac{\partial f}{\partial r}=-\frac{2}{r^{2}}+\frac{4}{r^{2}}=\frac{2}{r^{2}}
$$

## Exercises 4.1

In Exercises 1-8, compute the Laplacian in an appropriate coordinate system and decide if the given function satisfies Laplace's equation $\nabla^{2} u=0$. The appropriate dimension is indicated by the number of variables.

1. $u(x, y)=\frac{x}{x^{2}+y^{2}}$.
2. $u(x, y)=\tan ^{-1}\left(\frac{y}{x}\right)$.
3. $u(x, y)=\frac{1}{\sqrt{x^{2}+y^{2}}}$.
4. $u(x, y, z)=\frac{z}{\sqrt{x^{2}+y^{2}}}$.
5. $u(x, y, z)=\left(x^{2}+y^{2}+z^{2}\right)^{3 / 2}$.
6. $u(x, y)=\ln \left(x^{2}+y^{2}\right)$.
7. $u(x, y, z)=\left(x^{2}+y^{2}+z^{2}\right)^{-1 / 2}$.
8. $u(x, y)=\tan ^{-1}\left(\frac{y}{x}\right) \frac{y}{x^{2}+y^{2}}$.
9. (a) Show that if $u(r, \theta, \phi)$ depends only on $r$, then the Laplacian takes the form $\nabla^{2} u=\frac{\partial^{2} u}{\partial r^{2}}+\frac{2}{r} \frac{\partial u}{\partial r}$.
(b) What is the form of the Laplacian if the function $u$ depends only on $r$ and $\theta$ ?
10. Supply all the details to derive (8) from (7).
11. Project Problem: Harmonic functions. Recall from Section 3.1 that $u(x, y)$ is called a harmonic function if it satisfies Laplace's equation.
(a) Show that if $u$ and $v$ are harmonic and $\alpha$ and $\beta$ are numbers, then $\alpha u+\beta v$ is harmonic.
(b) Give an example of two harmonic functions $u$ and $v$ such that $u v$ is not harmonic.
(c) Show that if $u$ and $u^{2}$ are both harmonic, then $u$ must be constant. [Hint: Write down what it means for $u$ and $u^{2}$ to be harmonic in terms of their partial derivatives.]
(d) Show that if $u, v$ and $u^{2}+v^{2}$ are harmonic, then $u$ and $v$ must be constant.

### 4.2 Vibrations of a Circular Membrane: Symmetric Case

In this and the next section we study the vibrations of a thin circular membrane with uniform mass density, clamped along its circumference. We place the center of the membrane at the origin, and we denote the radius by $a$. The vibrations of the membrane are governed by the two-dimensional wave equation, which will be expressed in polar coordinates, because these are the coordinates best suited to this problem. Using the polar form of the Lapla-

![](./images/1c611338-958a-44f7-9d79-2dde87e6ac2a-07_411_465_275_38.jpg)
Figure 1 A radially symmetric shape.

The initial conditions are radially symmetric, so they depend only on $r$.
cian ((3), Section 4.1), the two dimensional wave equation becomes

$$
\frac{\partial^{2} u}{\partial t^{2}}=c^{2}\left(\frac{\partial^{2} u}{\partial r^{2}}+\frac{1}{r} \frac{\partial u}{\partial r}+\frac{1}{r^{2}} \frac{\partial^{2} u}{\partial \theta^{2}}\right) .
$$

The initial shape of the membrane will be modeled by the function $f(r, \theta)$, and its initial velocity by $g(r, \theta)$.

In this section we confine our study to the case where $f$ and $g$ are radially symmetric or axisymmetric, that is, they depend only on the radius $r$ and not on $\theta$. It is reasonable on physical grounds that in this case the solution also does not depend on $\theta$ (see Figure 1). Consequently, $\partial u / \partial \theta=0$, and (1) becomes

$$
\frac{\partial^{2} u}{\partial t^{2}}=c^{2}\left(\frac{\partial^{2} u}{\partial r^{2}}+\frac{1}{r} \frac{\partial u}{\partial r}\right),
$$

where $u=u(r, t), 0<r<a$, and $t>0$. Since the membrane is clamped at the circumference, we have the boundary condition

$$
u(a, t)=0, \quad t \geq 0 .
$$

The radially symmetric initial conditions are

$$
u(r, 0)=f(r), \quad \frac{\partial u}{\partial t}(r, 0)=g(r), \quad 0<r<a .
$$

We solve the boundary value problem (2)-(4) using the separation of variables method, as we did throughout Chapter 3. The goal is to separate the variables in the partial differential equation (2) and reduce the problem to two ordinary differential equations in $r$ and $t$. As you will see, the equation in $t$ is the same as the one that we obtained after separating variables in the wave equation in rectangular coordinates. Hence the solution in $t$ will consist of sines and cosines. The equation in the spatial variable $r$ is new, and its solution will involve the so-called Bessel functions.

## Separating Variables

We assume that the solution is of the form $u(r, t)=R(r) T(t)$. After differentiating, plugging into (2), and separating variables, we get

$$
\frac{T^{\prime \prime}}{c^{2} T}=\frac{1}{R}\left(R^{\prime \prime}+\frac{1}{r} R^{\prime}\right)=-\lambda^{2} .
$$

Because we expect periodic solutions in $T$, we have set the sign of the separation constant negative. (For a more rigorous argument based on the fact that

![](./images/1c611338-958a-44f7-9d79-2dde87e6ac2a-08_343_420_777_51.jpg)
Figure 2 The Bessel functions of order 0 .

the solution in $R$ should be bounded in the interval [ $0, a$ ], see the solution of the Dirichlet problem in Section 4.5.) Hence

$$
\begin{gathered}
r R^{\prime \prime}+R^{\prime}+\lambda^{2} r R=0, \quad R(a)=0 \quad(\text { from }(3)), \\
T^{\prime \prime}+c^{2} \lambda^{2} T=0 .
\end{gathered}
$$

## Solving the Separated Equations

Here again, we begin by solving the equation with the boundary conditions to narrow down the possible solutions. Equation (5) is known as the parametric form of Bessel's equation of order zero (here $\lambda$ is the parameter). This equation arises so frequently in applications that its solutions have been named. Since the equation is second order and homogeneous, we need only two linearly independent solutions to be able to write its general solution. By convention, these two linearly independent solutions are called Bessel functions of order 0 of the first and second kind, and are denoted $J_{0}(\lambda r)$ and $Y_{0}(\lambda r)$, respectively. Hence the general solution to the parametric form of Bessel's equation in (5) is

$$
R(r)=c_{1} J_{0}(\lambda r)+c_{2} Y_{0}(\lambda r)
$$

where $r>0$ (Theorem 3, Section 4.8). The functions $J_{0}$ and $Y_{0}$ are treated in great detail in Sections 4.7-4.9; here we recall facts only as needed. Figure 2 shows the graphs of $J_{0}$ and $Y_{0}$.

Since on physical grounds the solutions to the wave equation are expected to be bounded, it follows that the spatial part of the solution, $R(r)$, has to be bounded near $r=0$. This is effectively a second boundary condition on $R$. Now the fact that $Y_{0}$ is unbounded near 0 forces us to choose $c_{2}=0$ in (7). To avoid trivial solutions, we will take $c_{1}=1$ and get

$$
R(r)=J_{0}(\lambda r)
$$

The condition $R(a)=0$ (see (5)) implies that

$$
J_{0}(\lambda a)=0
$$

and so $\lambda a$ must be a root of the Bessel function $J_{0}$. As Figure 2 suggests, $J_{0}$ has infinitely many positive zeros, which we denote by

$$
\alpha_{1}<\alpha_{2}<\alpha_{3}<\cdots<\alpha_{n}<\cdots
$$

(For a proof of this fact, see Section 4.9, or Exercise 35, Section 4.8.) Thus

$$
\lambda=\lambda_{n}=\frac{\alpha_{n}}{a}, \quad n=1,2, \ldots,
$$

and the corresponding solutions of (5) are

$$
R_{n}(r)=J_{0}\left(\frac{\alpha_{n}}{a} r\right), \quad n=1,2, \ldots
$$

where $\alpha_{n}$ is the $n$th positive zero of $J_{0}$. These solutions are analogous to the solutions $\sin \frac{n \pi}{L} x$ that we have encountered several times previously, in particular, while solving the one dimensional wave equation. The only difference is that the function sine and its zeros $n \pi$ are now replaced by the function $J_{0}$ and its zeros $\alpha_{n}$. Returning to (6) with $\lambda=\lambda_{n}$, we find

$$
T(t)=T_{n}(t)=A_{n} \cos c \lambda_{n} t+B_{n} \sin c \lambda_{n} t
$$

We thus obtain the product solutions of (2) and (3)

$$
u_{n}(r, t)=\left(A_{n} \cos c \lambda_{n} t+B_{n} \sin c \lambda_{n} t\right) J_{0}\left(\lambda_{n} r\right) \quad n=1,2, \ldots
$$

## Bessel Series Solution of the Entire Problem

To satisfy the initial conditions, motivated by the superposition principle, we let

$$
u(r, t)=\sum_{n=1}^{\infty}\left(A_{n} \cos c \lambda_{n} t+B_{n} \sin c \lambda_{n} t\right) J_{0}\left(\lambda_{n} r\right)
$$

We determine the unknown coefficients by evaluating the series at $t=0$ and using the initial conditions. We get from the first condition in (4)

$$
u(r, 0)=f(r)=\sum_{n=1}^{\infty} A_{n} J_{0}\left(\lambda_{n} r\right), \quad 0<r<a
$$

This series representation of $f(r)$ is akin to a Fourier sine series, except that the sine functions are now replaced by Bessel functions. There are analogous expansion theorems that apply in such cases; the series expansions that arise are known as Bessel, or Fourier-Bessel, expansions (see Theorem 2, Section 4.8). For the case at hand, we make use of Theorem 2, Section 4.8, with $p=0$. The Bessel coefficients $A_{n}$ are given by

$$
A_{n}=\frac{2}{a^{2} J_{1}^{2}\left(\alpha_{n}\right)} \int_{0}^{a} f(r) J_{0}\left(\lambda_{n} r\right) r d r
$$

where $J_{1}$ is the Bessel function of order 1. Now, differentiating the series for $u$ term by term with respect to $t$, and then setting $t=0$, we get from the second initial condition

$$
u_{t}(r, 0)=g(r)=\sum_{n=1}^{\infty} c \lambda_{n} B_{n} J_{0}\left(\lambda_{n} r\right)
$$

## THEOREM 1 WAVE EQUATION IN POLAR COORDINATES

There is a clear analogy between the solution (9) and the solution of the onedimensional wave equation (8), Section 3.3. The only difference is that spatial variations are now determined by Bessel functions rather than the simpler sine functions.

From (7), Section 4.8,

$$
\begin{aligned}
& \int x^{p+1} J_{p}(x) d x= \\
& x^{p+1} J_{p+1}(x)+C
\end{aligned}
$$

Thus $c \lambda_{n} B_{n}=c \frac{\alpha_{n}}{a} B_{n}$ is the $n$th Bessel coefficient of $g$, and so

$$
B_{n}=\frac{2}{c \alpha_{n} a J_{1}^{2}\left(\alpha_{n}\right)} \int_{0}^{a} g(r) J_{0}\left(\lambda_{n} r\right) r d r
$$

This completely determines the solution.
The solution of the radially symmetric two-dimensional wave equation (2) with boundary and initial conditions (3) and (4) is

$$
u(r, t)=\sum_{n=1}^{\infty}\left(A_{n} \cos c \lambda_{n} t+B_{n} \sin c \lambda_{n} t\right) J_{0}\left(\lambda_{n} r\right)
$$

where
(10)

$$
\begin{gathered}
A_{n}=\frac{2}{a^{2} J_{1}^{2}\left(\alpha_{n}\right)} \int_{0}^{a} f(r) J_{0}\left(\lambda_{n} r\right) r d r \\
B_{n}=\frac{2}{c \alpha_{n} a J_{1}^{2}\left(\alpha_{n}\right)} \int_{0}^{a} g(r) J_{0}\left(\lambda_{n} r\right) r d r \\
\lambda_{n}=\frac{\alpha_{n}}{a}, \quad \text { and } \quad \alpha_{n}=n \text {th positive zero of } J_{0}
\end{gathered}
$$

When applying (10) in concrete situations, we are required to evaluate integrals involving Bessel functions that are quite complicated. In many interesting cases these integrals can be evaluated with the help of integral formulas developed in the exercises and in Section 4.8. As an illustration, consider the integral

$$
\int_{0}^{a} x^{p+1} J_{p}\left(\frac{\alpha}{a} x\right) d x, \quad p \geq 0, \alpha>0
$$

Let $u=\frac{\alpha}{a} x, d u=\frac{\alpha}{a} d x$, then

$$
\begin{aligned}
\int x^{p+1} J_{p}\left(\frac{\alpha}{a} x\right) d x & =\frac{a^{p+2}}{\alpha^{p+2}} \int u^{p+1} J_{p}(u) d u \\
& =\frac{a^{p+2}}{\alpha^{p+2}} u^{p+1} J_{p+1}(u)+C
\end{aligned}
$$

where the last equality follows from (7), Section 4.8. Substituting back $u=\frac{\alpha x}{a}$, simplifying, and then evaluating at $x=0$ and $x=a$, we obtain the very useful identity

$$
\int_{0}^{a} x^{p+1} J_{p}\left(\frac{\alpha}{a} x\right) d x=\frac{a^{p+2}}{\alpha} J_{p+1}(\alpha)
$$

## EXAMPLE 1 A circular membrane with constant initial velocity

An explosion near the surface of a flexible circular membrane with clamped edges imparts a uniform initial velocity equal to $-100 \mathrm{~m} / \mathrm{sec}$. Assume the initial shape of the membrane to be flat, take $a=1$ and $c=100$, and determine the subsequent vibrations of the membrane.

Solution The solution is given by (9), where $A_{n}=0$ for all $n$, since $f(r)=0$. From (10) we have

$$
\begin{aligned}
B_{n} & =\frac{-2}{\alpha_{n} J_{1}^{2}\left(\alpha_{n}\right)} \int_{0}^{1} J_{0}\left(\alpha_{n} r\right) r d r \\
& =\frac{-2}{\alpha_{n}^{2} J_{1}\left(\alpha_{n}\right)} \quad(\text { by }(11) \text { with } p=0)
\end{aligned}
$$

Thus, from (9), we obtain the solution

$$
u(r, t)=\sum_{n=1}^{\infty} \frac{-2}{\alpha_{n}^{2} J_{1}\left(\alpha_{n}\right)} \sin \left(100 \alpha_{n} t\right) J_{0}\left(\alpha_{n} r\right) .
$$

To get numerical values from our answer in Example 1, it is clearly necessary to know the values of the zeros of the Bessel function $J_{0}$. Since these values are useful in solving many problems, they have been computed and tabulated to a high degree of accuracy. With the help of a computer system, we approximated the first five positive roots of the equation $J_{0}(x)=$ 0 . These and other relevant numerical data are given in Table 1.

| $j$ | 1 | 2 | 3 | 4 | 5 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $\alpha_{j}$ | 2.4048 | 5.5201 | 8.6537 | 11.7915 | 14.9309 |
| $J_{1}\left(\alpha_{j}\right)$ | .5191 | -.3403 | .2714 | -.2325 | .2065 |
| $\frac{-2}{\alpha_{j}^{2} J_{1}\left(\alpha_{j}\right)}$ | -0.6662 | 0.1929 | -.0984 | 0.0619 | -0.0434 |

Table 1 Numerical data for Example 1.

With the help of this table, we find the first three terms of the solution in Example 1:

$$
\begin{aligned}
u(r, t) \approx & -0.6662 J_{0}(2.40 r) \sin (240 t) \\
& +0.1929 J_{0}(5.52 r) \sin (552 t)-.0984 J_{0}(8.65 r) \sin (865 t) .
\end{aligned}
$$

We used these terms to plot the shape of the membrane at various values of $t>0$ in Figure 3.

As expected, soon after the explosion, the elastic membrane starts to vibrate downward.

Figure 3 Vibrating circular membrane with radial symmetry in Example 1.
![](./images/1c611338-958a-44f7-9d79-2dde87e6ac2a-12_354_331_163_620.jpg)
![](./images/1c611338-958a-44f7-9d79-2dde87e6ac2a-12_308_444_627_539.jpg)
![](./images/1c611338-958a-44f7-9d79-2dde87e6ac2a-12_292_417_176_1019.jpg)
![](./images/1c611338-958a-44f7-9d79-2dde87e6ac2a-12_285_370_176_1454.jpg)
![](./images/1c611338-958a-44f7-9d79-2dde87e6ac2a-12_301_416_627_1022.jpg)
![](./images/1c611338-958a-44f7-9d79-2dde87e6ac2a-12_294_417_629_1401.jpg)

The next example treats the case of a vibrating membrane with nonzero initial displacement and zero initial velocity.

EXAMPLE 2 A circular membrane with radially symmetric initial shape Solve the boundary value problem (2)-(4), given that

$$
f(r)=1-r^{2}, \quad g(r)=0, \quad a=c=1 .
$$

Solution Note that the problem is radially symmetric because of the boundary and initial conditions. The solution is given by (9), where $B_{n}=0$ for all $n$ since $g(r)=0$, and $A_{n}$ is the Bessel coefficient of the function $1-r^{2}$, given by (10). We have

$$
\begin{aligned}
A_{n} & =\frac{2}{J_{1}^{2}\left(\alpha_{n}\right)} \int_{0}^{1}\left(1-r^{2}\right) J_{0}\left(\alpha_{n} r\right) r d r \\
& =\frac{2}{\alpha_{n}^{4} J_{1}^{2}\left(\alpha_{n}\right)} \int_{0}^{\alpha_{n}}\left(\alpha_{n}^{2}-s^{2}\right) J_{0}(s) s d s \quad\left(s=\alpha_{n} r\right)
\end{aligned}
$$

Integrating by parts, with $u=\alpha_{n}^{2}-s^{2}, d v=J_{0}(s) s d s$, and hence $d u=-2 s d s, v= J_{1}(s) s$ (by (7), Section 4.8 , with $p=0$ ), we find

$$
\begin{aligned}
A_{n} & =\frac{2}{\alpha_{n}^{4} J_{1}^{2}\left(\alpha_{n}\right)}\left[\left.\left(\alpha_{n}^{2}-s^{2}\right) J_{1}(s) s\right|_{0} ^{\alpha_{n}}+2 \int_{0}^{\alpha_{n}} J_{1}(s) s^{2} d s\right] \\
& =\frac{4}{\alpha_{n}^{4} J_{1}^{2}\left(\alpha_{n}\right)} \int_{0}^{\alpha_{n}} J_{1}(s) s^{2} d s
\end{aligned}
$$

To evaluate the integral, we appeal to (11) and arrive at

$$
A_{n}=\frac{4}{\alpha_{n}^{2} J_{1}^{2}\left(\alpha_{n}\right)} J_{2}\left(\alpha_{n}\right)
$$

At this point, we could appeal to (9) to write the explicit form of the solution. However, before doing so, we mention one more worthy simplification based on yet another property of Bessel functions. Appealing to (6), Section 4.8, with $p=1$, and recalling that $\alpha_{n}$ is a zero of $J_{0}$, we find

From (6), Section 4.8, $J_{p+1}(x)=\frac{2 p}{x} J_{p}(x)-J_{p-1}(x)$.
and hence

$$
J_{2}\left(\alpha_{n}\right)=\frac{2}{\alpha_{n}} J_{1}\left(\alpha_{n}\right)
$$

$$
A_{n}=\frac{8}{\alpha_{n}^{3} J_{1}\left(\alpha_{n}\right)}
$$

Thus, from (9), we obtain the solution

$$
u(r, t)=\sum_{n=1}^{\infty} \frac{8}{\alpha_{n}^{3} J_{1}\left(\alpha_{n}\right)} \cos \left(\alpha_{n} t\right) J_{0}\left(\alpha_{n} r\right)
$$

Setting $t=0$ in the solution of Example 2, we should get the initial displacement, that is, we should get

$$
1-r^{2}=\sum_{n=1}^{\infty} \frac{8}{\alpha_{n}^{3} J_{1}\left(\alpha_{n}\right)} J_{0}\left(\alpha_{n} r\right), \quad 0<r<1 .
$$

This is the Bessel series of the function $1-r^{2}$ that we have computed in passing as we worked out the solution to Example 2. Figure 4 shows some partial sums of this series converging to $1-r^{2}, 0<r<1$.

We end this section with a remark concerning the physical interpretation of the solution of Example 2. In our derivation of the wave equation, we always assumed small displacements, but you may not be willing to call a unit displacement at the center of a drum of unit radius small. To give our problem a meaningful interpretation, we could rescale the initial data. Because of the linearity of the boundary value problem this leads only to the same rescaling of the solution.

## Exercises 4.2

In Exercises 1-8, solve the vibrating membrane problem (2)-(4) for the given data. If possible, with the help of a computer, find numerical values for the first five nonzero coefficients of the series solution and plot the shape of the membrane at various values of $t$. (Formula (11) is useful in all these exercises.)

1. $a=2, c=1, f(r)=0, g(r)=1$.
2. $a=1, c=10, f(r)=1-r^{2}, g(r)=1$.
3. $a=1, c=1, f(r)=0$,

$$
g(r)= \begin{cases}1 & \text { if } 0<r<\frac{1}{2}, \\ 0 & \text { if } \frac{1}{2}<r<1 .\end{cases}
$$

[Hint: Follow Example 1.]
4. $a=1, c=1, f(r)=0, g(r)=J_{0}\left(\alpha_{3} r\right)$.
[Hint: Orthogonality relations in Section 4.8.]
5. $a=1, c=1, f(r)=J_{0}\left(\alpha_{1} r\right), g(r)=0$.
[Hint: Orthogonality relations in Section 4.8.]
6. $a=2, c=1, f(r)=1-r, g(r)=0$.
7. $a=1, c=1, f(r)=J_{0}\left(\alpha_{3} r\right), g(r)=1-r^{2}$.
8. $a=1, c=1, f(r)=\frac{1}{128}\left(3-4 r^{2}+r^{4}\right), g(r)=0$.
[Hint: Integration by parts, Example 2.]
9. (a) Find the solution in Exercise 3 for an arbitrary value of $c>0$.
(b) Describe what happens to the solution as $c$ increases.

## 10. Project Problem: Radially symmetric heat equation on a disk.

Use the methods of this section to show that the solution of the heat boundary value problem

$$
\begin{array}{cl}
\frac{\partial u}{\partial t}=c^{2}\left(\frac{\partial^{2} u}{\partial r^{2}}+\frac{1}{r} \frac{\partial u}{\partial r}\right), & 0<r<a, t>0, \\
u(a, t)=0, & t>0, \\
u(r, 0)=f(r), & 0<r<a,
\end{array}
$$

is

$$
u(r, t)=\sum_{n=1}^{\infty} A_{n} e^{-c^{2} \lambda_{n}^{2} t} J_{0}\left(\lambda_{n} r\right)
$$

with

$$
A_{n}=\frac{2}{a^{2} J_{1}^{2}\left(\alpha_{n}\right)} \int_{0}^{a} f(r) J_{0}\left(\lambda_{n} r\right) r d r
$$

where $\lambda_{n}=\frac{\alpha_{n}}{a}$, and $\alpha_{n}=n$th positive zero of $J_{0}$.
11. (a) Solve the heat problem of Exercise 10 when $f(r)=100,0<r<a$. What does your solution represent?
(b) Approximate the temperature of the hottest point on the plate at time $t=3$, given that $a=1$ and $c=1$. Where is this point on the plate? Justify your answer intuitively.

## 12. Project Problem: Integral identities with Bessel functions.

(a) Use (7) and (8), Section 4.8, to establish the identities

$$
\int J_{1}(x) d x=-J_{0}(x)+C \quad \text { and } \quad \int x J_{0}(x) d x=x J_{1}(x)+C
$$

In the rest of this problem we generalize these identities.
(b) By integrating (5), Section 4.8, show that

$$
\int J_{p+1}(x) d x=\int J_{p-1}(x) d x-2 J_{p}(x)
$$

(c) Use the first integral in (a), (b), and induction to establish that

$$
\int J_{2 n+1}(x) d x=-J_{0}(x)-2 \sum_{k=1}^{n} J_{2 k}(x)+C, \quad n=0,1,2, \ldots
$$

As an illustration, derive the following identities:

$$
\begin{gathered}
\int J_{3}(x) d x=-J_{0}(x)-2 J_{2}(x)+C \\
\int J_{5}(x) d x=-J_{0}(x)-2 J_{2}(x)-2 J_{4}(x)+C
\end{gathered}
$$

(d) By integrating (3), Section 4.8, show that

$$
x J_{p+1}(x)+p \int J_{p+1}(x) d x=\int x J_{p}(x) d x
$$

[Hint: Evaluate the integral of $x J_{p}^{\prime}(x)$ by parts.] (e) Take $p=2 n$ in (d) and use (c) to prove that for $n=0,1,2, \ldots$,

$$
\int x J_{2 n}(x) d x=x J_{2 n+1}(x)-2 n J_{0}(x)-4 n \sum_{k=1}^{n} J_{2 k}(x)+C
$$

Derive the following identities:

$$
\begin{gathered}
\int x J_{2}(x) d x=x J_{3}(x)-2 J_{0}(x)-4 J_{2}(x)+C \\
\int x J_{4}(x) d x=x J_{5}(x)-4 J_{0}(x)-8 J_{2}(x)-8 J_{4}(x)+C
\end{gathered}
$$

### 4.3 Vibrations of a Circular Membrane: General Case

We continue our study of the vibrating circular membrane, now without any symmetry assumptions. We will solve the two dimensional wave equation in polar coordinates:

$$
\frac{\partial^{2} u}{\partial t^{2}}=c^{2}\left(\frac{\partial^{2} u}{\partial r^{2}}+\frac{1}{r} \frac{\partial u}{\partial r}+\frac{1}{r^{2}} \frac{\partial^{2} u}{\partial \theta^{2}}\right)
$$

where $0<r<a, 0<\theta<2 \pi, t>0$. Here $u=u(r, \theta, t)$ denotes the deflection of the membrane at the point $(r, \theta)$ at time $t$. The initial conditions (displacement and velocity) are

$$
u(r, \theta, 0)=f(r, \theta), \quad \frac{\partial u}{\partial t}(r, \theta, 0)=g(r, \theta)
$$

$0<r<a, 0<\theta<2 \pi$. The requirement that the edges of the membrane be held fixed translates into the boundary condition

$$
u(a, \theta, t)=0, \quad 0<\theta<2 \pi, t>0
$$

Since $\theta$ is a polar angle, ( $r, \theta$ ) and ( $r, \theta+2 \pi$ ) represent the same point, and hence $u(r, \theta, t)=u(r, \theta+2 \pi, t)$. In other words, $u$ is $2 \pi$-periodic in $\theta$. Consequently,

$$
u(r, 0, t)=u(r, 2 \pi, t) \quad \text { and } \quad \frac{\partial u}{\partial \theta}(r, 0, t)=\frac{\partial u}{\partial \theta}(r, 2 \pi, t) .
$$

## Separation of Variables

We start by deriving the general solution of (1) subject to the boundary condition (3). We use the method of separation of variables and set $u(r, \theta, t)=R(r) \Theta(\theta) T(t)$. Differentiating $u$, substituting into (1), and separating variables gives

$$
\frac{T^{\prime \prime}}{c^{2} T}=\frac{R^{\prime \prime}}{R}+\frac{R^{\prime}}{r R}+\frac{\Theta^{\prime \prime}}{r^{2} \Theta}
$$

The left side depends only on $t$ and the right side only on $r$ and $\theta$. Therefore, each side must equal a constant $k$. Expecting periodic solutions in $T$, we take $k=-\lambda^{2}$. Thus

$$
\frac{T^{\prime \prime}}{c^{2} T}=-\lambda^{2}, \quad \text { and } \quad \frac{R^{\prime \prime}}{R}+\frac{R^{\prime}}{r R}+\frac{\Theta^{\prime \prime}}{r^{2} \Theta}=-\lambda^{2}
$$

Separating variables in the second equation we get

$$
\lambda^{2} r^{2}+\frac{r^{2} R^{\prime \prime}}{R}+\frac{r R^{\prime}}{R}=\mu^{2} \quad \text { and } \quad-\frac{\Theta^{\prime \prime}}{\Theta}=\mu^{2} .
$$

We have chosen a nonnegative sign for the separating constant $\mu^{2}$ because the solutions of the equation in $\Theta$ have to be $2 \pi$-periodic. The boundary condition (3) becomes $R(a) \Theta(\theta) T(t)=0$ for $0<\theta<2 \pi$ and $t>0$. To avoid the trivial solution, we impose the condition $R(a)=0$. Similarly, using (4), we find that $\Theta(0)=\Theta(2 \pi)$ and $\Theta^{\prime}(0)=\Theta^{\prime}(2 \pi)$. Thus we have arrived at the following separated equations:

$$
\begin{gathered}
\Theta^{\prime \prime}+\mu^{2} \Theta=0, \quad \Theta(0)=\Theta(2 \pi), \quad \Theta^{\prime}(0)=\Theta^{\prime}(2 \pi) \\
r^{2} R^{\prime \prime}+r R^{\prime}+\left(\lambda^{2} r^{2}-\mu^{2}\right) R=0, \quad R(a)=0 \\
T^{\prime \prime}+c^{2} \lambda^{2} T=0
\end{gathered}
$$

Note that we start with the $\Theta$ equation, since we have a full complement of boundary conditions for it, and it contains only one separation constant. After determining that $\mu=m, m=0,1,2,3, \ldots$, we can turn to the equation in $R$ and determine which values of the separation constant $\lambda$ allow for nontrivial solutions. The $T$ equation is dealt with last.

We get $J_{m}$ 's here, and not $Y_{m}$ 's or a combination of $J_{m}$ 's and $Y_{m}$ 's because, on physical grounds, we insist that our solutions remain bounded at $r=0$.

## Solving the Separated Equations

We begin by solving for $\Theta$. For $\mu=0$ the solution is a constant $A_{0}$. If $\mu \neq 0$, the general solution is of the form $\Theta(\theta)=c_{1} \cos \mu \theta+c_{2} \sin \mu \theta$. To satisfy the boundary conditions we must take $\mu$ to be an integer. Thus

$$
\Theta_{m}(\theta)=A_{m} \cos m \theta+B_{m} \sin m \theta, \quad m=0,1,2, \ldots
$$

(Note that negative values of $m$ do not contribute any new solutions.) Setting $\mu=m$ in the equation for $R$, we get

$$
r^{2} R^{\prime \prime}+r R^{\prime}+\left(\lambda^{2} r^{2}-m^{2}\right) R=0, \quad R(a)=0
$$

This is the parametric form of Bessel's equation of order $m$ which is treated in Theorem 3, Section 4.8. Quoting from this theorem, we have

$$
R(r)=R_{m n}(r)=J_{m}\left(\lambda_{m n} r\right), \quad m=0,1,2, \ldots, n=1,2, \ldots,
$$

where $\lambda_{m n}=\alpha_{m n} / a$ and $\alpha_{m n}$ is the $n$th positive zero of the Bessel function $J_{m}$. For $\lambda=\lambda_{m n}$ the equation in $T$ becomes $T^{\prime \prime}+c^{2} \lambda_{m n}^{2} T=0$ with solutions

$$
A_{m n} \cos c \lambda_{m n} t \quad \text { and } \quad B_{m n} \sin c \lambda_{m n} t
$$

Using the expressions for $R, \Theta$, and, $T$, we arrive at the product solutions of (1) and (3):

$$
u_{m n}(r, \theta, t)=J_{m}\left(\lambda_{m n} r\right)\left(a_{m n} \cos m \theta+b_{m n} \sin m \theta\right) \cos c \lambda_{m n} t
$$

and

$$
u_{m n}^{*}(r, \theta, t)=J_{m}\left(\lambda_{m n} r\right)\left(a_{m n}^{*} \cos m \theta+b_{m n}^{*} \sin m \theta\right) \sin c \lambda_{m n} t
$$

where $m=0,1,2, \ldots, n=1,2, \ldots$. Note that we have replaced the coefficient $A_{m} A_{m n}$ by $a_{m n}$, and similarly for $b_{m n}, a_{m n}^{*}$, and $b_{m n}^{*}$. While this may appear to be just relabeling of the unknown coefficients, in fact, it provides a more convenient choice of solutions that will be needed as we proceed. Note too that $b_{0 n}$ and $b_{0 n}^{*}$ will never be needed, since $\sin m \theta=0$ when $m=0$, and so for the sake of definiteness we take them to be 0 .

## Superposition Principle and the General Solution

The superposition principle suggests adding all the functions in (5) and (6). The resulting sum is displayed in (16) below. Because of the complexity of this solution, we consider two cases separately: one in which the initial velocity $g$ is zero, and a second in which the initial displacement $f$ is zero. The general solution is then obtained by combining these two cases.

## EXAMPLE 1 Vibrations of a membrane with zero initial velocity

Solve the boundary value problem consisting of (1)-(3) given that $g=0$.
Solution The initial conditions in this case are

$$
u(r, \theta, 0)=f(r, \theta), \quad \frac{\partial u}{\partial t}(r, \theta, 0)=0, \quad 0<r<a, 0<\theta<2 \pi .
$$

It is easily seen that the only product solutions that meet the second condition are those given by ( 5 ). Thus the superposition principle suggests a solution of the form

$$
u(r, \theta, t)=\sum_{m=0}^{\infty} \sum_{n=1}^{\infty} J_{m}\left(\lambda_{m n} r\right)\left(a_{m n} \cos m \theta+b_{m n} \sin m \theta\right) \cos c \lambda_{m n} t
$$

Setting $t=0$, we get

$$
f(r, \theta)=\sum_{m=0}^{\infty} \sum_{n=1}^{\infty} J_{m}\left(\lambda_{m n} r\right)\left(a_{m n} \cos m \theta+b_{m n} \sin m \theta\right) .
$$

This surely is a sort of a generalized Fourier series of $f(r, \theta)$ in terms of the functions $J_{m}\left(\lambda_{m n} r\right) \cos m \theta$ and $J_{m}\left(\lambda_{m n} r\right) \sin m \theta$, and hence $a_{m n}$ and $b_{m n}$ are the corresponding generalized Fourier coefficients of the function $f$. This fact and many important related applications are explored in Section 4.6 (see in particular Theorems 1 and 2 of that section). We now proceed to determine $a_{m n}$ and $b_{m n}$, using properties of the usual Fourier series and Bessel series.

Fix $r$ and think of $f(r, \theta)$ as a ( $2 \pi$-periodic) function of $\theta$. To facilitate the use of Fourier series, we write (8) as

$$
\begin{aligned}
f(r, \theta)= & \overbrace{\sum_{n=1}^{\infty} a_{0 n} J_{0}\left(\lambda_{0 n} r\right)}^{=a_{0}(r)}+\sum_{m=1}^{\infty}\{\overbrace{\left(\sum_{n=1}^{\infty} a_{m n} J_{m}\left(\lambda_{m n} r\right)\right)}^{=a_{m}(r)} \cos m \theta \\
& +\overbrace{\left(\sum_{n=1}^{\infty} b_{m n} J_{m}\left(\lambda_{m n} r\right)\right)}^{=b_{m}(r)} \sin m \theta\} \\
= & a_{0}(r)+\sum_{m=1}^{\infty}\left(a_{m}(r) \cos m \theta+b_{m}(r) \sin m \theta\right) .
\end{aligned}
$$

Now we see clearly that (for fixed $r$ ) $a_{0}(r), a_{m}(r)$, and $b_{m}(r)$ are the Fourier coefficients in the Fourier series expansion of $\theta \mapsto f(r, \theta)$. Using (2)-(4), Section 2.2, we
conclude that

$$
\begin{gathered}
a_{0}(r)=\frac{1}{2 \pi} \int_{0}^{2 \pi} f(r, \theta) d \theta=\sum_{n=1}^{\infty} a_{0 n} J_{0}\left(\lambda_{0 n} r\right), \\
a_{m}(r)=\frac{1}{\pi} \int_{0}^{2 \pi} f(r, \theta) \cos m \theta d \theta=\sum_{n=1}^{\infty} a_{m n} J_{m}\left(\lambda_{m n} r\right), \\
b_{m}(r)=\frac{1}{\pi} \int_{0}^{2 \pi} f(r, \theta) \sin m \theta d \theta=\sum_{n=1}^{\infty} b_{m n} J_{m}\left(\lambda_{m n} r\right),
\end{gathered}
$$

for $m=1,2, \ldots$. Now let $r$ vary and think of the last three series as the Bessel series expansions of order $m=0,1,2, \ldots$ of the functions $a_{0}(r), a_{m}(r)$, and $b_{m}(r)$, respectively. The coefficients in these series are Bessel coefficients and so from (17), Section 4.8, we obtain

$$
\begin{gathered}
a_{0 n}=\frac{2}{a^{2} J_{1}^{2}\left(\alpha_{0 n}\right)} \int_{0}^{a} a_{0}(r) J_{0}\left(\lambda_{0 n} r\right) r d r \\
a_{m n}=\frac{2}{a^{2} J_{m+1}^{2}\left(\alpha_{m n}\right)} \int_{0}^{a} a_{m}(r) J_{m}\left(\lambda_{m n} r\right) r d r \\
b_{m n}=\frac{2}{a^{2} J_{m+1}^{2}\left(\alpha_{m n}\right)} \int_{0}^{a} b_{m}(r) J_{m}\left(\lambda_{m n} r\right) r d r
\end{gathered}
$$

Now using (9)-(11), we get

$$
\begin{gathered}
a_{0 n}=\frac{1}{\pi a^{2} J_{1}^{2}\left(\alpha_{0 n}\right)} \int_{0}^{a} \int_{0}^{2 \pi} f(r, \theta) J_{0}\left(\lambda_{0 n} r\right) r d \theta d r \\
a_{m n}=\frac{2}{\pi a^{2} J_{m+1}^{2}\left(\alpha_{m n}\right)} \int_{0}^{a} \int_{0}^{2 \pi} f(r, \theta) \cos m \theta J_{m}\left(\lambda_{m n} r\right) r d \theta d r \\
b_{m n}=\frac{2}{\pi a^{2} J_{m+1}^{2}\left(\alpha_{m n}\right)} \int_{0}^{a} \int_{0}^{2 \pi} f(r, \theta) \sin m \theta J_{m}\left(\lambda_{m n} r\right) r d \theta d r
\end{gathered}
$$

for $m, n=1,2 \ldots$. Substituting these coefficients in (7) completes the solution of the problem. $\square$

Before giving a numerical application, we present a useful identity involving Bessel functions.

## A USEFUL IDENTITY

For any $k \geq 0, a>0$, and $\alpha>0$, we have

$$
\int_{0}^{a}\left(a^{2}-r^{2}\right) r^{k+1} J_{k}\left(\frac{\alpha}{a} r\right) d r=2 \frac{a^{k+4}}{\alpha^{2}} J_{k+2}(\alpha)
$$

Proof We first make a change of variables, $\frac{\alpha}{a} r=x, d r=\frac{a}{\alpha} d x$, and transform the integral into

$$
\begin{aligned}
& \frac{a^{k+2}}{\alpha^{k+2}} \int_{0}^{\alpha}\left(a^{2}-\frac{a^{2} x^{2}}{\alpha^{2}}\right) x^{k+1} J_{k}(x) d x \\
& \quad=\frac{a^{k+4}}{\alpha^{k+2}} \int_{0}^{\alpha} x^{k+1} J_{k}(x) d x-\frac{a^{k+4}}{\alpha^{k+4}} \int_{0}^{\alpha} x^{k+3} J_{k}(x) d x
\end{aligned}
$$

![](./images/1c611338-958a-44f7-9d79-2dde87e6ac2a-20_285_455_1666_59.jpg)
Figure $1 J_{1}(r)$ and its first four positive zeros.

From (7), Section 4.8, with $p=k$, the first term is

$$
\frac{a^{k+4}}{\alpha^{k+2}}\left[x^{k+1} J_{k+1}(x)\right]_{0}^{\alpha}=\frac{a^{k+4}}{\alpha} J_{k+1}(\alpha) .
$$

The second integral can be evaluated with the help of (7), Section 4.8, and integration by parts. Let $u=x^{2}, d v=x^{k+1} J_{k}(x) d x$, then $d u=2 x d x, v=x^{k+1} J_{k+1}(x)$. Hence the second term becomes

$$
-\frac{a^{k+4}}{\alpha^{k+4}}\left[x^{k+3} J_{k+1}(x)\right]_{0}^{\alpha}+2 \frac{a^{k+4}}{\alpha^{k+4}} \int_{0}^{\alpha} x^{k+2} J_{k+1}(x) d x
$$

Using (7), Section 4.8, one more time and simplifying, we get

$$
-\frac{a^{k+4}}{\alpha} J_{k+1}(\alpha)+2 \frac{a^{k+4}}{\alpha^{2}} J_{k+2}(\alpha),
$$

and (15) follows.

## EXAMPLE 2 A vibrating membrane

Refer to Example 1 and determine the solution $u(r, \theta, t)$ when $a=c=1, f(r, \theta)= \left(1-r^{2}\right) r \sin \theta, g(r, \theta)=0$.
Solution From (12), we have

$$
a_{0 n}=\frac{1}{\pi J_{1}^{2}\left(\alpha_{0 n}\right)} \int_{0}^{1} \int_{0}^{2 \pi}\left(1-r^{2}\right) r \sin \theta J_{0}\left(\alpha_{0 n} r\right) r d \theta d r=0
$$

because $\int_{0}^{2 \pi} \sin \theta d \theta=0$. A similar argument using (13), (14), and the orthogonality of the trigonometric functions shows that $a_{m n}=0$ for all $m$ and $n$, and $b_{m n}=0$, except when $m=1$, in which case we have

$$
\begin{aligned}
b_{1 n} & =\frac{2}{\pi J_{2}^{2}\left(\alpha_{1 n}\right)} \int_{0}^{1} \int_{0}^{2 \pi}\left(1-r^{2}\right) r \sin ^{2} \theta J_{1}\left(\alpha_{1 n} r\right) r d \theta d r \\
& =\frac{2}{J_{2}^{2}\left(\alpha_{1 n}\right)} \int_{0}^{1}\left(1-r^{2}\right) r^{2} J_{1}\left(\alpha_{1 n} r\right) d r
\end{aligned}
$$

because $\frac{1}{\pi} \int_{0}^{2 \pi} \sin ^{2} \theta d \theta=1$. We now appeal to (15) with $a=1, k=1$ and get

$$
b_{1 n}=\frac{4 J_{3}\left(\alpha_{1 n}\right)}{\alpha_{1 n}^{2} J_{2}^{2}\left(\alpha_{1 n}\right)}=\frac{16}{\alpha_{1 n}^{3} J_{2}\left(\alpha_{1 n}\right)},
$$

where in the last step we have used (6) from Section 4.8 with $p=2$, and the fact that $J_{1}\left(\alpha_{1 n}\right)=0$. Recall that $\alpha_{1 n}$ denotes the $n$th positive zero of $J_{1}$. See Figure 1 for an illustration and Table 1, Section 4.8 for a list of numerical values of the first five $\alpha_{1 n}$. Substituting $b_{1 n}$ into (7), we arrive at the solution

$$
u(r, \theta, t)=\sin \theta \sum_{n=1}^{\infty} \frac{16}{\alpha_{1 n}^{3} J_{2}\left(\alpha_{1 n}\right)} J_{1}\left(\alpha_{1 n} r\right) \cos \alpha_{1 n} t
$$

With the help of a computer system we found approximate numerical values of the first three coefficients in the series and plotted in Figure 2 the partial sum of the series solution (with $n$ up to 3) at various values of $t$.

![](./images/1c611338-958a-44f7-9d79-2dde87e6ac2a-21_766_1683_190_10.jpg)
Figure 2 Vibrating circular membrane: a nonradially symmetric case.

To complete the solution of the vibrating membrane, we need to treat the case of a nonzero initial velocity. Save for some minor differences, this case is similar to the one we just treated. The proof is outlined in Exercises 7 and 8 . For ease of reference, we state the entire solution for this case in the following box.

## THE WAVE EQUATION IN POLAR COORDINATES: GENERAL CASE

The solution of the boundary value problem (1)-(3) is given by

$$
u(r, \theta, t)=\sum_{m=0}^{\infty} \sum_{n=1}^{\infty} J_{m}\left(\lambda_{m n} r\right)\left(a_{m n} \cos m \theta+b_{m n} \sin m \theta\right) \cos c \lambda_{m n} t
$$

$$
+\sum_{m=0}^{\infty} \sum_{n=1}^{\infty} J_{m}\left(\lambda_{m n} r\right)\left(a_{m n}^{*} \cos m \theta+b_{m n}^{*} \sin m \theta\right) \sin c \lambda_{m n} t
$$

where $\lambda_{m n}=\frac{\alpha_{m n}}{a} ; \alpha_{m n}$ is the $n$th positive zero of $J_{m} ; a_{m n}, b_{m n}$ are given by (12)-(14); and

$$
a_{0 n}^{*}=\frac{1}{\pi c \alpha_{0 n} a J_{1}^{2}\left(\alpha_{0 n}\right)} \int_{0}^{a} \int_{0}^{2 \pi} g(r, \theta) J_{0}\left(\lambda_{0 n} r\right) r d \theta d r
$$

$$
a_{m n}^{*}=\frac{2}{\pi c \alpha_{m n} a J_{m+1}^{2}\left(\alpha_{m n}\right)} \int_{0}^{a} \int_{0}^{2 \pi} g(r, \theta) \cos m \theta J_{m}\left(\lambda_{m n} r\right) r d \theta d r
$$

$$
b_{m n}^{*}=\frac{2}{\pi c \alpha_{m n} a \cdot J_{m+1}^{2}\left(\alpha_{m n}\right)} \int_{0}^{a} \int_{0}^{2 \pi} g(r, \theta) \sin m \theta \cdot J_{m}\left(\lambda_{m n} r\right) r d \theta d r
$$

for $m, n=1,2, \ldots$.

## EXAMPLE 3 Nonzero initial displacement and velocity

Determine the solution $u(r, \theta, t)$ of (1)-(3) when

$$
a=c=1, f(r, \theta)=\left(1-r^{2}\right) r \sin \theta, g(r, \theta)=\left(1-r^{2}\right) r^{2} \sin 2 \theta
$$

Solution The solution is given by (16). We only need to compute the second double series since the first one is computed in Example 2. Using the orthogonality of the trigonometric functions and arguing as we did in Example 2, we find that $a_{m n}^{*}=0$ for all $m$ and $n$, and $b_{m n}^{*}=0$, except when $m=2$. To compute $b_{2 n}^{*}$, we use (19) with $g(r, \theta)=\left(1-r^{2}\right) r^{2} \sin 2 \theta, a=c=1$, and $\lambda_{m n}=\alpha_{m n}$, and get

$$
\begin{aligned}
b_{2 n}^{*} & =\frac{2}{\pi \alpha_{2 n} J_{3}^{2}\left(\alpha_{2 n}\right)} \int_{0}^{1} \int_{0}^{2 \pi}\left(1-r^{2}\right) r^{2} \sin ^{2} 2 \theta J_{2}\left(\alpha_{2 n} r\right) r d \theta d r \\
& =\frac{2}{\alpha_{2 n} J_{3}^{2}\left(\alpha_{2 n}\right)} \int_{0}^{1}\left(1-r^{2}\right) r^{3} J_{2}\left(\alpha_{2 n} r\right) d r
\end{aligned}
$$

because $\frac{1}{\pi} \int_{0}^{2 \pi} \sin ^{2} 2 \theta d \theta=1$. To compute the last integral we apply (15) with $a=1, k=2$, and obtain

$$
b_{2 n}^{*}=\frac{4 J_{4}\left(\alpha_{2 n}\right)}{\alpha_{2 n}^{3} J_{3}^{2}\left(\alpha_{2 n}\right)}=\frac{24}{\alpha_{2 n}^{4} J_{3}\left(\alpha_{2 n}\right)},
$$

where in the last step we have used (6) from Section 4.8 with $p=3$ and the fact that $J_{2}\left(\alpha_{2 n}\right)=0$. Substituting in the second double series in (16) and using the solution of Example 2, we get the solution

$$
\begin{aligned}
u(r, \theta, t)= & \sin \theta \sum_{n=1}^{\infty} \frac{16}{\alpha_{1 n}^{3} J_{2}\left(\alpha_{1 n}\right)} J_{1}\left(\alpha_{1 n} r\right) \cos \alpha_{1 n} t \\
& +\sin 2 \theta \sum_{n=1}^{\infty} \frac{24}{\alpha_{2 n}^{4} J_{3}\left(\alpha_{2 n}\right)} J_{2}\left(\alpha_{2 n} r\right) \sin \alpha_{2 n} t
\end{aligned}
$$

The coefficients in the series can be approximated with the help of a computer, as we did in Example 2.

In the exercises, we will use the methods of this section to solve the general heat problem on the disk.

## Exercises 4.3

In Exercises 1-8, solve the vibrating membrane problem (1)-(3) for the given data. If possible, with the help of a computer, find numerical values for the first five nonzero coefficients of the series solution and plot the shape of the membrane at various values of $t$. (Formula (15) is helpful in doing these problems.)

1. $f(r, \theta)=\left(1-r^{2}\right) r^{2} \sin 2 \theta, g(r, \theta)=0, a=c=1$.
2. $f(r, \theta)=\left(9-r^{2}\right) \cos 2 \theta, g(r, \theta)=0, a=3, c=1$.
3. $f(r, \theta)=\left(4-r^{2}\right) r \sin \theta, g(r, \theta)=1, a=2, c=1$.
4. $f(r, \theta)=J_{3}\left(\alpha_{32} r\right) \sin 3 \theta, g(r, \theta)=0, a=c=1$.
5. $f(r, \theta)=0, g(r, \theta)=\left(1-r^{2}\right) r^{2} \sin 2 \theta, a=c=1$.
6. $f(r, \theta)=1-r^{2}, g(r, \theta)=J_{0}(r), a=c=1$.
7. Project Problem: Circular membrane with zero initial displacement. Follow the steps outlined in this exercise to determine the vibrations of a circular membrane with radius $a$ and fixed boundary, given that the initial displacement of the membrane is 0 , and its initial velocity is $g(r, \theta)$. Review the solution of Example 1 for hints.
(a) Write down explicitly the differential equation, the boundary conditions, and the initial conditions.
(b) Assume a product solution of the form $R(r) \Theta(\theta) T(t)$ and show that $T(0)=0$. Conclude that

$$
u(r, \theta, t)=\sum_{m=0}^{\infty} \sum_{n=1}^{\infty} J_{m}\left(\lambda_{m n} r\right)\left(a_{m n}^{*} \cos m \theta+b_{m n}^{*} \sin m \theta\right) \sin c \lambda_{m n} t
$$

(c) Use the given initial velocity and (b) to obtain

$$
\begin{array}{r}
g(r, \theta)=\sum_{n=1}^{\infty} c \lambda_{0 n} a_{0 n}^{*} J_{0}\left(\lambda_{0 n} r\right)+\sum_{m=1}^{\infty}\left\{\left(\sum_{n=1}^{\infty} c \lambda_{m n} a_{m n}^{*} J_{m}\left(\lambda_{m n} r\right)\right) \cos m \theta\right. \\
\left.+\left(\sum_{n=1}^{\infty} c \lambda_{m n} b_{m n}^{*} J_{m}\left(\lambda_{m n} r\right)\right) \sin m \theta\right\}
\end{array}
$$

(d) Derive (17)-(19) by proceeding from here as we did in the derivation of (12)(14).
8. General solution of the vibrating circular membrane problem.
(a) Show that the solution of the boundary value problem (1)-(3) can be written as $u(r, \theta, t)=u_{1}(r, \theta, t)+u_{2}(r, \theta, t)$, where $u_{1}$ and $u_{2}$ satisfy (1) and (3) and the following initial conditions:

$$
\begin{aligned}
& u_{1}(r, \theta, 0)=f(r, \theta), \quad \frac{\partial u_{1}}{\partial t}(r, \theta, 0)=0 ; \\
& u_{2}(r, \theta, 0)=0, \quad \frac{\partial u_{2}}{\partial t}(r, \theta, 0)=g(r, \theta) .
\end{aligned}
$$

(b) Combine the results of Example 1 and Exercise 7 to derive the general solution (16).
9. Project Problem: An integral formula for Bessel functions. Follow the outlined steps to prove that for any $k \geq 0$, and any integer $l \geq 0$, we have

$$
\int r^{k+1+2 l} J_{k}(r) d r=\sum_{n=0}^{l}(-1)^{n} 2^{n} \frac{l!}{(l-n)!} r^{k+1+2 l-n} J_{k+n+1}(r)+C .
$$

(a) Show that the formula holds for $l=0$ and all $k \geq 0$. [Hint: Use (7), Section 4.8.]
(b) Complete the proof by induction on $l$. [Hint: Assume the formula is true for $l-1$ and all $k$. To establish the formula for $l$, integrate by parts and use the formula with $l-1$ and $k+1$.]
10. Solve the boundary value problem (1)-(3) when $a=c=1, f(r, \theta)=(1- \left.r^{2}\right)\left(\frac{1}{4}-r^{2}\right) r^{3} \sin 3 \theta$, and $g(r, \theta)=0$. [Hint: Exercise 9 is useful.]
11. Project Problem: Two-dimensional heat equation (general case). Use the methods of this section to show that the solution of heat boundary value problem

$$
\begin{gathered}
\frac{\partial u}{\partial t}=c^{2}\left(\frac{\partial^{2} u}{\partial r^{2}}+\frac{1}{r} \frac{\partial u}{\partial r}+\frac{1}{r^{2}} \frac{\partial^{2} u}{\partial \theta^{2}}\right), \quad 0<r<a, 0<\theta<2 \pi, t>0, \\
u(a, \theta, t)=0, \quad 0<\theta<2 \pi, t>0, \\
u(r, \theta, 0)=f(r, \theta), \quad 0<r<a, 0<\theta<2 \pi,
\end{gathered}
$$

is

$$
u(r, \theta, t)=\sum_{m=0}^{\infty} \sum_{n=1}^{\infty} J_{m}\left(\lambda_{m n} r\right)\left(a_{m n} \cos m \theta+b_{m n} \sin m \theta\right) e^{-c^{2} \lambda_{m n}^{2} t}
$$

where $\lambda_{m n}=\frac{\alpha_{m n}}{a} ; \alpha_{m n}$ is the $n$th positive zero of $J_{m}$; and $a_{m n}, b_{m n}$ are given by (12)-(14).
12. (a) Solve the heat problem in Exercise 11 for the following data: $a=c=$ 1, $f(r, \theta)=\left(1-r^{2}\right) r \sin \theta$. [Hint: Example 2.]
(b) What are the hottest points when $t=0$ ?
(c) Locate the hottest point in the plate for $t=1,2$. Approximate the temperature of these points at the given times.
13. Solve the heat equation

$$
\frac{\partial u}{\partial t}=\frac{\partial^{2} u}{\partial r^{2}}+\frac{1}{r} \frac{\partial u}{\partial r}+\frac{1}{r^{2}} \frac{\partial^{2} u}{\partial \theta^{2}}, \quad 0<r<1,0<\theta<2 \pi, t>0,
$$

given the nonzero boundary condition

$$
u(1, \theta, t)=\sin 3 \theta
$$

and the initial condition $u(r, \theta, 0)=0$.

### 4.4 Laplace's Equation in Circular Regions

The steady-state (or time independent) temperature distribution in a circular plate of radius $a$, with prescribed temperature at the boundary, satisfies the two-dimensional Laplace equation (in polar coordinates):

$$
\nabla^{2} u=\frac{\partial^{2} u}{\partial r^{2}}+\frac{1}{r} \frac{\partial u}{\partial r}+\frac{1}{r^{2}} \frac{\partial^{2} u}{\partial \theta^{2}}=0, \quad 0<r<a, 0<\theta<2 \pi
$$

and the boundary condition

$$
u(a, \theta)=f(\theta), \quad 0<\theta<2 \pi
$$

(Note that $f$ is necessarily $2 \pi$-periodic.) Equations (1) and (2) describe a Dirichlet problem over a disk of radius $a$. We have solved this kind of
problems over a rectangle in Section 3.8. Problems over other regions, such as a cylinder or a sphere, will be studied in the following sections and in Chapter 5.

Following the method of separation of variables, we will look for product solutions of (1) of the form $u(r, \theta)=R(r) \Theta(\theta)$. Plugging this into (1) and simplifying, we obtain

$$
\begin{array}{cl}
R^{\prime \prime} \Theta+\frac{1}{r} R^{\prime} \Theta+\frac{1}{r^{2}} R \Theta^{\prime \prime}=0 & \text { (Plug into (1).) } \\
r^{2} \frac{R^{\prime \prime}}{R}+r \frac{R^{\prime}}{R}+\frac{\Theta^{\prime \prime}}{\Theta}=0 & \text { (Multiply by } r^{2} \\
\left.r^{2} \frac{R^{\prime \prime}}{R}+r \frac{R^{\prime}}{R}=\lambda \text { and } \quad \frac{\Theta^{\prime \prime}}{\Theta}=-\lambda \quad \text { (Separation constant } \lambda .\right) \\
r^{2} R^{\prime \prime}+r R^{\prime}-\lambda R=0 \text { and } \quad \Theta^{\prime \prime}+\lambda \Theta=0 \quad \text { (Simplify.) }
\end{array}
$$

Recall that $\Theta$ is necessarily $2 \pi$-periodic. From our knowledge of the solutions of the equation $\Theta^{\prime \prime}+\lambda \Theta=0$, we conclude that $\lambda=n^{2}(n=0,1,2 \ldots)$, in order to get $2 \pi$-periodic functions in $\theta$. Thus the separated equations become

$$
\begin{gathered}
r^{2} R^{\prime \prime}+r R^{\prime}-n^{2} R=0 \\
\Theta^{\prime \prime}+n^{2} \Theta=0
\end{gathered}
$$

We have the $2 \pi$-periodic solutions

$$
\Theta=\Theta_{n}=a_{n} \cos n \theta+b_{n} \sin n \theta, n=0,1,2, \ldots .
$$

Recall from Appendix A.3, Euler's equation
$x^{2} y^{\prime \prime}+\alpha x y^{\prime}+\beta y=0$,
with indicial equation
$\rho^{2}+(\alpha-1) \rho+\beta=0$
and indicial roots $\rho_{1}$ and $\rho_{2}$.
If $\rho_{1} \neq \rho_{2}$, the general solution is
$y=c_{1} x^{\rho_{1}}+c_{2} x^{\rho_{2}}$.
If $\rho_{1}=\rho_{2}$, the general solution is
$y=c_{1} x^{\rho_{1}}+c_{2} x^{\rho_{1}} \ln x$.

We recognize the equation for $R$ as an Euler equation. Appealing to results from Appendix A.3, we find that the indicial roots are $\pm n$, and hence the solutions
and

$$
R(r)=c_{1}+c_{2} \ln \left(\frac{r}{a}\right), \quad n=0
$$

For the Dirichlet problem in the disk, the solution should remain bounded at 0 . So we take $c_{2}=0$, since $\left(\frac{r}{a}\right)^{-n}$ and $\ln \left(\frac{r}{a}\right)$ are not bounded when $r=0$. (Other choices of the constant will be needed in Dirichlet problem outside a disk or on an annular region. See Exercises 12, 21, and 24.) We thus arrive at the product solutions

$$
u_{0}(r, \theta)=a_{0} \quad \text { and } \quad u_{n}(r, \theta)=\left(\frac{r}{a}\right)^{n}\left(a_{n} \cos n \theta+b_{n} \sin n \theta\right), n=1,2, \ldots
$$

## SOLUTION OF THE DIRICHLET PROBLEM ON THE DISK

![](./images/1c611338-958a-44f7-9d79-2dde87e6ac2a-26_407_470_1657_56.jpg)
Figure 1 A Dirichlet problem.

Superposing these solutions, we get

$$
u(r, \theta)=a_{0}+\sum_{n=1}^{\infty}\left(\frac{r}{a}\right)^{n}\left[a_{n} \cos n \theta+b_{n} \sin n \theta\right] .
$$

As we now show, the unknown coefficients $a_{0}, a_{n}, b_{n}$ are precisely the Fourier coefficients of the boundary function $f(\theta)$.

The solution of Laplace's equation (1) satisfying the prescribed boundary condition (2) is given by (4), where $a_{0}, a_{n}, b_{n}$ are the Fourier coefficients of the $2 \pi$-periodic function $f(\theta)$ :

$$
a_{0}=\frac{1}{2 \pi} \int_{0}^{2 \pi} f(\theta) d \theta
$$

(5)

$$
a_{n}=\frac{1}{\pi} \int_{0}^{2 \pi} f(\theta) \cos n \theta d \theta, \quad b_{n}=\frac{1}{\pi} \int_{0}^{2 \pi} f(\theta) \sin n \theta d \theta
$$

$n=1,2, \ldots$.
Proof Putting $r=a$ in (4) and using (2) we get

$$
f(\theta)=u(a, \theta)=a_{0}+\sum_{n=1}^{\infty}\left(a_{n} \cos n \theta+b_{n} \sin n \theta\right)
$$

This is clearly the Fourier series representation of $f$, and hence the coefficients are given by the Euler formulas (Section 2.2).

Since (4) gives the steady-state temperature of the points inside the disk, by taking $r=0$ in (4), we get $a_{0}$ as the temperature of the center. Now

$$
a_{0}=\frac{1}{2 \pi} \int_{0}^{2 \pi} f(\theta) d \theta
$$

which shows that the temperature of the center is equal to the average value of the temperature on the boundary.

## EXAMPLE 1 A Dirichlet problem on the disk

Find the steady-state temperature distribution in a disk of radius 1 if the upper half of the circumference is kept at $100^{\circ}$ and the lower half is kept at $0^{\circ}$.
Solution The boundary values are described by the function

$$
u(1, \theta)=f(\theta)= \begin{cases}100 & \text { if } 0<\theta<\pi, \\ 0 & \text { if } \pi<\theta<2 \pi .\end{cases}
$$

Substituting in (5), we get

$$
a_{0}=\frac{1}{2 \pi} \int_{0}^{\pi} 100 d \theta=50, \quad a_{n}=\frac{1}{\pi} \int_{0}^{\pi} 100 \cos n \theta d \theta=0
$$

![](./images/1c611338-958a-44f7-9d79-2dde87e6ac2a-27_366_463_645_35.jpg)
Figure 2 Fourier series of $f(\theta)$.

and

$$
b_{n}=\frac{1}{\pi} \int_{0}^{\pi} 100 \sin n \theta d \theta=\frac{100}{n \pi}[1-\cos n \pi]
$$

Substituting in (4) we find the solution

$$
u(r, \theta)=50+\frac{100}{\pi} \sum_{n=1}^{\infty} \frac{1}{n}(1-\cos n \pi) r^{n} \sin n \theta
$$

Setting $r=0$, we see that the temperature of the center is $50^{\circ}$, which corresponds to the average of the temperature on the boundary of the disk.

On the boundary of the disk, when $r=1$, the series becomes

$$
u(1, \theta)=50+\frac{200}{\pi} \sum_{k=0}^{\infty} \frac{1}{(2 k+1)} \sin (2 k+1) \theta
$$

According to the given boundary values, this series should represent the function $f(\theta)$. In fact, this is the Fourier series of $f(\theta)$. Some of its partial sums are plotted in Figure 2.

In many interesting situations, the series solution of the Dirichlet problem can be computed in closed form with the help of the formula

$$
\sum_{n=1}^{\infty} r^{n} \frac{\sin n \theta}{n}=\tan ^{-1}\left(\frac{r \sin \theta}{1-r \cos \theta}\right)
$$

which is valid for $0<r<1$, and all $\theta$. A derivation of this formula, using the complex logarithm, is presented in Exercise 19. We can give an indirect proof based on the uniqueness property of the solution of the Dirichlet problem (1)-(2). Properties of this nature were discussed and proved in Section 3.10 for the Dirichlet problem in a rectangle. To prove (6), it is enough to show that the left and the right sides are solutions of the same Dirichlet problem. Indeed, we will show that they satisfy ( 1 ), with $a=1$, and ( 2 ) with $f(\theta)= \frac{1}{2}(\pi-\theta), 0<\theta<2 \pi$. To verify the assertion for the left side of (6), it suffices to use (4) and the fact that the Fourier series of $f(\theta)$ is $\sum_{n=1}^{\infty} \frac{\sin n \theta}{n}$. To verify the assertion for the right side of (6), let $u(r, \theta)=\tan ^{-1}\left(\frac{r \sin \theta}{1-r \cos \theta}\right)$. We must show that $\nabla^{2} u=0$ and $u(1, \theta)=\frac{1}{2}(\pi-\theta)$. The first part is straightforward and is left to Exercise 6. For the second part, we have

$$
\begin{aligned}
u(1, \theta) & =\tan ^{-1}\left(\frac{\sin \theta}{1-\cos \theta}\right) \\
& =\tan ^{-1}\left(\frac{\cos \frac{\theta}{2}}{\sin \frac{\theta}{2}}\right) \quad\left(\sin \theta=2 \cos \frac{\theta}{2} \sin \frac{\theta}{2} ; 1-\cos \theta=2 \sin ^{2} \frac{\theta}{2}\right) \\
& =\tan ^{-1} \cot \left(\frac{\theta}{2}\right)=\frac{\pi}{2}-\frac{\theta}{2}
\end{aligned}
$$

which completes the proof of (6).

## EXAMPLE 2 Converting to Cartesian coordinates

Show that in Cartesian coordinates the steady-state solution in Example 1 is

$$
u(x, y)=50+\frac{100}{\pi}\left[\tan ^{-1}\left(\frac{y}{1-x}\right)+\tan ^{-1}\left(\frac{y}{1+x}\right)\right],
$$

for $x^{2}+y^{2}<1$.
Solution We start by rewriting the solution of Example 1 as

$$
\begin{aligned}
u(r, \theta) & =50+\frac{100}{\pi} \sum_{n=1}^{\infty} \frac{1}{n}(1-\cos n \pi) r^{n} \sin n \theta \\
& =50+\frac{100}{\pi} \sum_{n=1}^{\infty} \frac{\sin n \theta}{n} r^{n}-\frac{100}{\pi} \sum_{n=1}^{\infty} \frac{\cos n \pi}{n} r^{n} \sin n \theta
\end{aligned}
$$

Noting that $\cos n \pi \sin n \theta=\sin n(\theta-\pi)$ and using (6), we get

$$
u(r, \theta)=50+\frac{100}{\pi} \tan ^{-1}\left(\frac{r \sin \theta}{1-r \cos \theta}\right)-\frac{100}{\pi} \tan ^{-1}\left(\frac{r \sin (\theta-\pi)}{1-r \cos (\theta-\pi)}\right) .
$$

We now use the identities $\sin (\theta-\pi)=-\sin \theta ; \cos (\theta-\pi)=-\cos \theta ; \tan ^{-1}(-x)= -\tan ^{-1} x$, and get

$$
u(r, \theta)=50+\frac{100}{\pi}\left[\tan ^{-1}\left(\frac{r \sin \theta}{1-r \cos \theta}\right)+\tan ^{-1}\left(\frac{r \sin \theta}{1+r \cos \theta}\right)\right] .
$$

Passing to rectangular coordinates by using $x=r \cos \theta, y=r \sin \theta$, we get (7). $\square$

When dealing with steady-state problems, we are often interested in determining the points with the same temperature. These points lie on curves called isotherms. We illustrate this notion by finding the isotherms of the solution in Example 1.

## EXAMPLE 3 Isotherms or curves of constant temperature

Two extreme isotherms are easy to guess in Example 1: The upper semicircle corresponds to the temperature $100^{\circ}$, and the lower semicircle corresponds to the temperature $0^{\circ}$. The temperature of all other isotherms is clearly between these two values. Let $0<T<100$. Our goal is to determine the points ( $x, y$ ) such that $u(x, y)=T$. Setting the right side of (7) equal to $T$ and simplifying, we get

$$
\frac{\pi(T-50)}{100}=\tan ^{-1}\left(\frac{y}{1-x}\right)+\tan ^{-1}\left(\frac{y}{1+x}\right) .
$$

When $T=50$, the left side equals 0 , and the solution in this case is $y=0$ ( $x$ is arbitrary). This corresponds to the set of points on the $x$-axis. Intuitively this answer is clear. Do you see why? For $T \neq 50$, apply the tangent to both sides of (8), use the identity

$$
\tan (a+b)=\frac{\tan a+\tan b}{1-\tan a \tan b},
$$

The larger circle in Figure 3(a) determines the isotherm $u(r, \theta)=30$ in the unit disk. It is centered at $\left(0, \tan \left(\frac{3 \pi}{10}\right)\right)$ with radius $\sec \left(\frac{3 \pi}{10}\right)$. We have $\tan \left(\frac{3 \pi}{10}\right)=$

$$
\frac{1+\sqrt{5}}{\sqrt{2}(5-\sqrt{5})} \approx 1.38
$$

and

$$
\sec \left(\frac{3 \pi}{10}\right) \approx 1.7
$$

Figure 3(b) shows various isotherms inside the unit disk.

![](./images/1c611338-958a-44f7-9d79-2dde87e6ac2a-29_745_647_969_419.jpg)
Figure 3(a)

![](./images/1c611338-958a-44f7-9d79-2dde87e6ac2a-29_738_674_982_1130.jpg)
Figure 3(b)

and get

$$
\frac{\left(\frac{y}{1-x}\right)+\left(\frac{y}{1+x}\right)}{1-\left(\frac{y}{1-x}\right)\left(\frac{y}{1+x}\right)}=\tan \left(\frac{\pi T}{100}-\frac{\pi}{2}\right)=-\cot \left(\frac{\pi T}{100}\right) .
$$

Straightforward manipulations lead to

$$
x^{2}+y^{2}-1-2 y \tan \left(\frac{\pi T}{100}\right)=0
$$

Completing the square yields

$$
x^{2}+\left[y-\tan \left(\frac{\pi T}{100}\right)\right]^{2}=1+\tan ^{2}\left(\frac{\pi T}{100}\right)
$$

Hence the isotherm corresponding to the value $T$ consists of the arc of the circle with center $\left(0, \tan \left(\frac{\pi T}{100}\right)\right)$ and radius $\sqrt{1+\tan ^{2}\left(\frac{\pi T}{100}\right)}=\left|\sec \frac{\pi T}{100}\right|$. Figure 3(a) shows the isotherm $T=30$. Figure 3(b) shows various other isotherms.

## Varying the Region and the Boundary Conditions

We can use the methods of this section to solve problems over planar regions other than disks. These are regions that are conveniently described in polar coordinates, such as a wedge, an annulus, or a region outside a circle. Furthermore, we can vary the boundary conditions and consider Neumann and Robin conditions. Recall that these are linear conditions that involve the function $u$ and its normal derivative on the boundary. In polar coordinates, the normal derivative of $u$ at points lying on a circle centered at the origin

![](./images/1c611338-958a-44f7-9d79-2dde87e6ac2a-30_422_456_208_63.jpg)
Figure 4 The normal derivative of $u, \frac{\partial u}{\partial n}$, is $\frac{\partial u}{\partial r}$.

![](./images/1c611338-958a-44f7-9d79-2dde87e6ac2a-30_278_466_973_63.jpg)
Figure 5 The wedge shaped region bounded by the rays $\theta=0$ and $\theta=\alpha$, and the circle $r=1$.

is simply the partial derivative of $u$ with respect to $r$ (Figure 4). Thus for a boundary lying on a circle centered at the origin, a Neumann condition specifies $u_{r}(r, \theta)$; and a Robin condition specifies $u_{r}(r, \theta)+a(\theta) u(r, \theta)$, where $a$ is a function of $\theta$. The following example illustrates how we can solve such problems.

## EXAMPLE 4 A Robin condition on a wedge

Solve Laplace's equation (1) over the wedge region in Figure 5, supplied with the boundary conditions: for $0<r<1$ and $0<\theta<\alpha$,

$$
u(r, 0)=0, \quad u(r, \alpha)=0, \quad \frac{\partial}{\partial r} u(1, \theta)=-u(1, \theta)-\theta .
$$

The boundary conditions represent a wedge whose sides along the rays $\theta=0$ and $\theta=\alpha$ are kept at 0 temperature, and the wedge is exchanging heat along its circular boundary at a rate given by the Robin condition $u_{r}(1, \theta)=-u(1, \theta)-\theta$. Presumably, the insulation of the wedge along the circular boundary is better for smaller values of $\theta$, since the rate of heat loss is smaller for $\theta$ near 0 .

Solution Before we proceed with the solution, note how the points ( $r, \theta$ ) in the wedge region are conveniently described in polar coordinates by the inequalities $0<r<1$ and $0<\theta<\alpha$. Applying the method of separation of variables as we did at the outset of this section, we arrive at the equations

$$
\begin{gathered}
\Theta^{\prime \prime}+\lambda \Theta=0, \quad \Theta(0)=0, \Theta(\alpha)=0 \\
r^{2} R^{\prime \prime}+r R^{\prime}-\lambda R=0
\end{gathered}
$$

where $\lambda$ is a separation constant. We have new conditions on $\Theta$, which follow from the boundary conditions $u(r, 0)=0$ and $u(r, \alpha)=0$. For example, from $u(r, \alpha)=0$, we get $R(r) \Theta(\alpha)=0$, and so $\Theta(\alpha)=0$. The initial value problem in $\theta$ is different from the one that we encountered at the beginning of this section, but it is a familiar problem that we solved in Section 3.3, with the variable $x$ instead of $\theta$. The nonzero solutions are

$$
\Theta_{n}(\theta)=\sin \frac{n \pi}{\alpha} \theta \quad(n=1,2, \ldots),
$$

and these correspond to the separation constants $\lambda=\left(\frac{n \pi}{\alpha}\right)^{2}$. Plugging the value of $\lambda$ into the radial equation yields the Euler equation

$$
r^{2} R^{\prime \prime}+r R^{\prime}-\left(\frac{n \pi}{\alpha}\right)^{2} R=0 .
$$

The indicial equation for this Euler equation is $\rho^{2}-\left(\frac{n \pi}{\alpha}\right)^{2}=0$, with roots $\rho= \pm \frac{n \pi}{\alpha}$. Hence, the bounded solutions for $0 \leq r<a$ are constant multiples of $R(r)= R_{n}(r)=r^{\frac{n \pi}{\alpha}}$. We thus have the product solutions

$$
b_{n} r^{\frac{n \pi}{\alpha}} \sin \frac{n \pi}{\alpha} \theta,
$$

and the superposition principle leads us to the following form of the solution:

$$
u(r, \theta)=\sum_{n=1}^{\infty} b_{n} r^{\frac{n \pi}{\alpha}} \sin \frac{n \pi}{\alpha} \theta, \quad 0<r<1,0<\theta<\alpha .
$$

You should check at this point that this solution satisfies the boundary conditions $u(r, 0)=0$ and $u(r, \alpha)=0$ for all choices of $b_{n}$. Next, we determine $b_{n}$ so as to satisfy the given Robin condition. Setting $r=1$ in $u(r, \theta)$, we obtain $u(1, \theta)= \sum_{n=1}^{\infty} b_{n} \sin \frac{n \pi}{\alpha} \theta$. Differentiating $u(r, \theta)$ with respect to $r$ and then setting $r=1$, we obtain

$$
\begin{aligned}
u_{r}(1, \theta) & =\left.\frac{\partial}{\partial r}\left(\sum_{n=1}^{\infty} b_{n} r^{\frac{n \pi}{\alpha}} \sin \left(\frac{n \pi}{\alpha} \theta\right)\right)\right|_{r=1} \\
& =\left.\sum_{n=1}^{\infty} b_{n} \sin \left(\frac{n \pi}{\alpha} \theta\right) \frac{\partial}{\partial r}\left(r^{\frac{n \pi}{\alpha}}\right)\right|_{r=1} \\
& =\sum_{n=1}^{\infty} \frac{n \pi}{\alpha} b_{n} \sin \left(\frac{n \pi}{\alpha} \theta\right) .
\end{aligned}
$$

The condition $u_{r}(1, \theta)=-u(1, \theta)-\theta$ implies that, for all $0<\theta<\alpha$,

$$
\sum_{n=1}^{\infty} \frac{n \pi}{\alpha} b_{n} \sin \left(\frac{n \pi}{\alpha} \theta\right)=-\sum_{n=1}^{\infty} b_{n} \sin \left(\frac{n \pi}{\alpha} \theta\right)-\theta ;
$$

equivalently,

$$
-\theta=\sum_{n=1}^{\infty} b_{n}\left(1+\frac{n \pi}{\alpha}\right) \sin \frac{n \pi}{\alpha} \theta, \quad 0<\theta<\alpha .
$$

We recognize this as the half-range sine Fourier series expansion of the function $f(\theta)=-\theta$ on the interval $(0, \alpha)$, where $b_{n}\left(1+\frac{n \pi}{\alpha}\right)$ is the $n$th sine coefficient:

$$
\begin{aligned}
b_{n}\left(1+\frac{n \pi}{\alpha}\right) & =-\frac{2}{\alpha} \int_{0}^{\alpha} \theta \sin \frac{n \pi}{\alpha} \theta d \theta \\
& =-\frac{2}{\alpha}\left[-\left.\theta\left(\frac{\alpha}{n \pi}\right) \cos \frac{n \pi}{\alpha} \theta\right|_{0} ^{\alpha}+\frac{\alpha}{n \pi} \int_{0}^{\alpha} \cos \frac{n \pi}{\alpha} \theta d \theta\right] \\
& =\frac{2 \alpha(-1)^{n}}{n \pi}
\end{aligned}
$$

Solving for $b_{n}$ and substituting into (9), we get the solution

$$
u(r, \theta)=\frac{2 \alpha^{2}}{\pi} \sum_{n=1}^{\infty} \frac{(-1)^{n}}{n(\alpha+n \pi)} r^{\frac{n \pi}{\alpha}} \sin \frac{n \pi}{\alpha} \theta, \quad 0<r<1,0<\theta<\alpha
$$

## Exercises 4.4

In Exercises 1-5, solve the Dirichlet problem on the unit disk for the given boundary values.

1. $f(\theta)=\cos \theta$.
2. $f(\theta)=\sin 2 \theta$.
3. $f(\theta)=\frac{1}{2}(\pi-\theta), 0<\theta<2 \pi$.
4. $f(\theta)= \begin{cases}\pi-\theta & \text { if } 0 \leq \theta \leq \pi, \\ 0 & \text { if } \pi \leq \theta<2 \pi .\end{cases}$
5. $f(\theta)= \begin{cases}100 & \text { if } 0 \leq \theta \leq \pi / 4, \\ 0 & \text { if } \pi / 4<\theta<2 \pi .\end{cases}$
6. Verify that

$$
u(r, \theta)=\tan ^{-1}\left(\frac{r \sin \theta}{1-r \cos \theta}\right)
$$

![](./images/1c611338-958a-44f7-9d79-2dde87e6ac2a-32_442_454_874_74.jpg)
Figure 6 for Exercise 12(b).

is a solution of (1). [Hint: Change to Cartesian coordinates.]
7. Determine the isotherms in Exercise 3.
8. Show that the isotherms in Exercise 1 lie on vertical lines.
9. Show that the isotherms in Exercise 2 lie on branches of hyperbolas centered at the origin.
10. (a) Solve the Dirichlet problem

$$
\begin{aligned}
& \nabla^{2} u(r, \theta)=0, \quad 0<r<1,0<\theta<2 \pi, \\
& u(1, \theta)=1+\sin 2 \theta .
\end{aligned}
$$

(b) Determine the isotherms. [Hint: $\sin 2 \theta=2 \sin \theta \cos \theta$.]
11. Independence of $r$. (a) Suppose that $u(r, \theta)$ is a solution of Laplace's equation that does not depend on $r$. Show that $u(r, \theta)=a \theta+b$ where $a$ and $b$ are constants.
(b) Determine $a$ and $b$ in order for $u(r, \theta)$ to be a solution of Laplace's equation in the wedge $0<r<1,0<\theta<\alpha$, with the boundary conditions $u=T_{1}$ when $\theta=0$ and $u=T_{2}$ when $\theta=\alpha$. What are the values of $u$ on the circular boundary of the wedge, when $r=1$ ?
12. Independence of $\theta$. (a) Suppose that $u(r, \theta)$ is a solution of Laplace's equation that does not depend on $\theta$. Show that $u(r \theta)=a \ln r+b$ where $a$ and $b$ are constants.
(b) Find a solution of Laplace's equation in the annulus in Figure 6 satisfying $u=1$ when $r=\frac{1}{2}$ and $u=2$ when $r=1$.
13. Solve Laplace's equation in the wedge $0<r<1,0<\theta<\frac{\pi}{4}$, subject to the boundary conditions $u=0$ when $\theta=0, u=0$ when $\theta=\frac{\pi}{4}$, and $\frac{\partial u}{\partial r}(\theta, 1)=\sin \theta$.
14. Solve Laplace's equation in the wedge $0<r<1,0<\theta<\frac{\pi}{2}$, subject to the boundary $u=0$ when $\theta=0, u=0$ when $\theta=\frac{\pi}{2}$, and $\frac{\partial u}{\partial r}(\theta, 1)=\theta$.
15. Consider the problem in the wedge in Figure 7(a). Show that this problem can be decomposed into two subproblems as indicated in Figure 7. That is, show that if $u_{1}$ is a solution of the problem in Figure 7(b) and $u_{2}$ is a solution of the problem in Figure 7(c), then $u=u_{1}+u_{2}$ is a solution of the problem in Figure 7(a).

![](./images/1c611338-958a-44f7-9d79-2dde87e6ac2a-32_328_1599_1639_130.jpg)
Figure 7

16. Consider the problem in the wedge in Figure 7(a). Take $\alpha=\frac{\pi}{4}$ and solve the problem subject to the conditions $u=0$ when $\theta=0, u=1$ when $\theta=\frac{\pi}{4}$, and $u(1, \theta)=3 \sin 4 \theta$. [Hint: For the problem in Figure 7(b), see Exercise 11.]

![](./images/1c611338-958a-44f7-9d79-2dde87e6ac2a-33_443_446_1495_29.jpg)
Figure 8 for Exercise 21.

17. A Neumann problem on the disk. Solve the Neumann problem $\nabla^{2} u=0$ for $0 \leq r<a$ with boundary condition $u_{r}(a, \theta)=f(\theta)$, where $f(\theta)$ determines the normal derivative on the circle $r=a$. For this problem to have a solution, we require the compatibility condition

$$
\int_{0}^{2 \pi} f(\theta) d \theta=0
$$

Explain why this condition is necessary for your solution.
18. A Robin condition. Solve Laplace's equation on the unit disk, subject to the Robin condition $u_{r}(1, \theta)+2 u(1, \theta)=100-2 \cos 2 \theta$.
19. A proof of (6). Let $z$ be a complex number with $|z|<1$. Write $z=r e^{i \theta}= r(\cos \theta+i \sin \theta)$. Consider the series expansion

$$
\log \left[(1-z)^{-1}\right]=z+\frac{1}{2} z^{2}+\frac{1}{3} z^{3}+\cdots
$$

which is valid for $|z|<1$. Compute the imaginary part of this series and derive (6). [Hint: Recall that if $w=r e^{i \theta}=x+i y$, with $-\pi<\theta<\pi$, then $\operatorname{Re}(\log (w))=\ln r$, and $\operatorname{Im}(\log (w))=\theta=\tan ^{-1} \frac{y}{x}$.]
20. Further identities. Taking real and imaginary parts in the series expansion

$$
\log (1+z)=\sum_{n=1}^{\infty}(-1)^{n+1} \frac{z^{n}}{n}, \quad|z|<1
$$

derive the identities: for $0 \leq r<1,0<\theta<2 \pi$,

$$
\begin{array}{r}
\sum_{n=1}^{\infty}(-1)^{n+1} \frac{\sin n \theta}{n} r^{n}=\tan ^{-1}\left(\frac{r \sin \theta}{1+r \cos \theta}\right) \\
\sum_{n=1}^{\infty}(-1)^{n+1} \frac{\cos n \theta}{n} r^{n}=\frac{1}{2} \ln \left(1+2 r \cos \theta+r^{2}\right)
\end{array}
$$

21. Dirichlet problem outside a disk. Show that the bounded solution of the Dirichlet problem outside the disk $r=a$ (Figure 8) is given by the series

$$
u(r, \theta)=a_{0}+\sum_{n=1}^{\infty}\left(\frac{a}{r}\right)^{n}\left(a_{n} \cos n \theta+b_{n} \sin n \theta\right), \quad r>a
$$

where the coefficients are given by (5). [Hint: Proceed as in the solution of the Dirichlet problem inside the disk. Choose the bounded solutions from (3).]
22. Solve the Dirichlet problem outside the unit disk with boundary values as in Example 1. What are the isotherms in this case?
23. (a) Solve the Dirichlet problem outside the unit disk with boundary values as in Exercise 5.
(b) Show that the isotherms are circles passing through the points $(1,0)$ and $\left(\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}\right)$.

![](./images/1c611338-958a-44f7-9d79-2dde87e6ac2a-34_438_445_532_74.jpg)
Figure 9 for Exercise 24.

## 24. Project Problem: Dirichlet problems on annular regions.

(a) Show that the steady-state solution in the annular region shown in Figure 9 is

$$
u(r, \theta)=a_{0} \frac{\ln r-\ln R_{2}}{\ln R_{1}-\ln R_{2}}+\sum_{n=1}^{\infty}\left[a_{n} \cos n \theta+b_{n} \sin n \theta\right]\left(\frac{R_{1}}{r}\right)^{n}\left(\frac{R_{2}^{2 n}-r^{2 n}}{R_{2}^{2 n}-R_{1}^{2 n}}\right),
$$

( $R_{1}<r<R_{2}$ ) where $a_{0}, a_{n}$, and $b_{n}$ are the Fourier coefficients of $f_{1}(\theta)$. [Hint: Proceed as in the solution derived in this section, and use the condition $R\left(R_{2}\right)=0$.]
(b) What is the steady-state solution if the boundary conditions are $u\left(R_{1}, \theta\right)=0$, and $u\left(R_{2}, \theta\right)=f_{2}(\theta)$, for all $\theta$ ?
(c) Combine (a) and (b) to find the steady-state solution in the annular region given that $u\left(R_{1}, \theta\right)=f_{1}(\theta)$, and $u\left(R_{2}, \theta\right)=f_{2}(\theta)$ for all $\theta$.
25. Project Problem: Two dimensional heat equation with a nonhomogeneous boundary condition. Show that the solution of the two dimensional heat equation

$$
u_{t}=c^{2}\left(\frac{\partial^{2} u}{\partial r^{2}}+\frac{1}{r} \frac{\partial u}{\partial r}+\frac{1}{r^{2}} \frac{\partial^{2} u}{\partial \theta^{2}}\right), \quad 0<r<a, 0<\theta<2 \pi, t>0,
$$

subject to the nonhomogeneous boundary condition

$$
u(\alpha, \theta, t)=G(\theta), \quad 0<\theta<2 \pi, t>0,
$$

and the initial condition

$$
u(r, \theta, 0)=F(r, \theta), \quad 0<\theta<2 \pi, 0 \leq r<a,
$$

is

$$
\begin{aligned}
u(r, \theta, t)= & a_{0}+\sum_{m=1}^{\infty}\left[a_{m} \cos m \theta+b_{m} \sin m \theta\right]\left(\frac{r}{a}\right)^{m} \\
& +\sum_{m=0}^{\infty} \sum_{n=1}^{\infty} J_{m}\left(\lambda_{m n} r\right)\left(a_{m n} \cos m \theta+b_{m n} \sin m \theta\right) e^{-c^{2} \lambda_{m n}^{2} t}
\end{aligned}
$$

where the coefficients $a_{0}, a_{m}, b_{m}$ are the Fourier coefficients of the $2 \pi$-periodic function $G(\theta) ; \lambda_{m n}=\frac{\alpha_{m n}}{a}$ where $\alpha_{m n}$ is the $n$th positive zero of the Bessel function of order $m, J_{m}$; and $a_{m n}, b_{m n}$ are given by (12)-(14) of Section 4.3 with $f(r, \theta)= F(r, \theta)-u_{1}(r, \theta)$, where $u_{1}$ represents the steady-state solution. [Hint: Consider two separate problems. First problem (steady-state solution): $\nabla^{2} u_{1}=0,0<r<a, \theta$ arbitrary, subject to the boundary condition $u_{1}(a, \theta)=G(\theta)$ for all $\theta$. Second problem: $v_{t}=c^{2} \nabla^{2} v, 0<r<a, \theta$ arbitrary, and $t>0$, subject to the boundary condition $v(a, \theta, t)=0$ for all $\theta$ and $t>0$, and the initial condition $v(r, \theta, 0)= F(r, \theta)-u_{1}(r, \theta)$ for all $\theta$ and $0 \leq r<a$. Combine the solution of the Dirichlet problem with that of Exercise 11, Section 4.3.]
26. A circular plate of radius 1 was placed in a freezer and its temperature was brought to $0^{\circ}$. The plate was then insulated and removed from the freezer. The edge of the plate was kept at a temperature varying from $0^{\circ}$ to $100^{\circ}$ according to the formula $f(\theta)=50(1-\cos \theta), 0 \leq \theta \leq 2 \pi$.
(a) Plot the temperature of the boundary as a function of $\theta$, and find its Fourier
series.
(b) Find the steady-state temperature,
(c) Plot the steady-state temperature and from your graph determine the points of the plate with temperature $0^{\circ}$, respectively, $100^{\circ}$.
(d) Determine and plot the isotherms. Confirm your answer in (c).
(e) Solve the heat problem in the plate given that the thermal conductivity $c=1$ and given that the initial temperature distribution is $0^{\circ}$.
(f) Plot the temperature distribution at various values of $t>0$ and estimate the time it takes to raise the temperature of the center to $25^{\circ}$. What is the limiting value of the temperature of the center? Verify your answer using (b).
27. (a) Solve the heat problem in Exercise 26 for the following data: $a=c=$ 1, $F(r, \theta)=\left(1-r^{2}\right) r \sin \theta, G(\theta)=\sin 2 \theta$ for $0<\theta<2 \pi$. [Hint: See Example 2, Section 4.3.]
(b) What is the steady-state solution in this case?
(c) Plot the solution for several values of $t$ and compare with the graph of your answer in (b).
Project Problem: Poisson integral formula on a disk. This important formula expresses the solution of the Dirichlet problem (4) in terms of an integral involving the boundary data function. Derive this formula following the steps outlined in Exercises 28 and 29.
28. The Poisson kernel. Let $z=r e^{i \theta}$, and consider the power series

$$
\frac{1}{1-z}=\sum_{n=0}^{\infty} z^{n}, \quad|z|<1
$$

(a) Show that

$$
1+2 \operatorname{Re}\left(\frac{1}{1-z}-1\right)=1+2 \sum_{n=1}^{\infty} r^{n} \cos n \theta, \quad 0<r<1, \text { all } \theta
$$

(b) Obtain the identity

$$
1+2 \sum_{n=1}^{\infty} r^{n} \cos n \theta=\frac{1-r^{2}}{1-2 r \cos \theta+r^{2}}, \quad 0<r<1, \text { all } \theta
$$

The function $P(r, \theta)=\frac{1-r^{2}}{1-2 r \cos \theta+r^{2}}$ is known as the Poisson kernel on the disk. It plays an important role in the theory of partial differential equations, complex and harmonic analysis.
29. Poisson integral formula on the disk. In this exercise we derive the integral form of the solution (4) of the Dirichlet problem (1)-(2), known as the Poisson integral formula: for $0<r<a$, and all $\theta$,

$$
\begin{aligned}
u(r, \theta) & =\frac{1}{2 \pi} \int_{0}^{2 \pi} f(\phi) P\left(\frac{r}{a}, \theta-\phi\right) d \phi \\
& =\frac{1}{2 \pi} \int_{0}^{2 \pi} f(\phi) \frac{a^{2}-r^{2}}{a^{2}-2 a r \cos (\theta-\phi)+r^{2}} d \phi
\end{aligned}
$$

Thus this formula is an alternative way of writing the series solution (4). (a) Substitute the coefficients (5) in the series solution (4) and obtain

$$
u(r, \theta)=\frac{1}{2 \pi} \int_{0}^{2 \pi} f(\phi)\left\{1+2 \sum_{n=1}^{\infty} \cos [n(\theta-\phi)]\left(\frac{r}{a}\right)^{n}\right\} d \phi
$$

[Hint: Before you do the substitution, replace the dummy variable $\theta$ in (5) by $\phi$.] (b) Derive the Poisson formula using (a) and Exercise 28.

### 4.5 Laplace's Equation in a Cylinder

![](./images/1c611338-958a-44f7-9d79-2dde87e6ac2a-36_530_373_700_63.jpg)
Figure 1
DIRICHLET PROBLEM IN A CYLINDER WITH ZERO LATERAL TEMPERATURE

In this section we treat certain radially symmetric Dirichlet problems in cylindrical regions. In cylindrical coordinates, Laplace's equation, with no $\phi$ dependence, is

$$
\nabla^{2} u=\frac{\partial^{2} u}{\partial \rho^{2}}+\frac{1}{\rho} \frac{\partial u}{\partial \rho}+\frac{\partial^{2} u}{\partial z^{2}}=0
$$

(See (4), Section 4.1.) The first problem that we will consider models the steady-state temperature distribution inside a cylinder with lateral surface and bottom kept at zero temperature and with radially symmetric temperature distribution at the top, as shown in Figure 1.

The solution of Laplace's equation (1) with boundary conditions

$$
\begin{array}{r}
u(\rho, 0)=0, \quad 0<\rho<a \\
u(a, z)=0, \quad 0<z<h \\
u(\rho, h)=f(\rho), \quad 0<\rho<a
\end{array}
$$

is

$$
u(\rho, z)=\sum_{n=1}^{\infty} A_{n} J_{0}\left(\lambda_{n} \rho\right) \sinh \lambda_{n} z
$$

where

$$
A_{n}=\frac{2}{\sinh \left(\lambda_{n} h\right) a^{2} J_{1}^{2}\left(\alpha_{n}\right)} \int_{0}^{a} f(\rho) J_{0}\left(\lambda_{n} \rho\right) \rho d \rho, \quad \lambda_{n}=\frac{\alpha_{n}}{a}
$$

and $\alpha_{n}$ is the $n$th positive zero of $J_{0}$, the Bessel function of order 0 .
Proof Using the method of separation of variables and setting $u(\rho, z)=R(\rho) Z(z)$, we get the equations $\rho^{2} R^{\prime \prime}+\rho R^{\prime}-k \rho^{2} R=0, R(a)=0$, and $Z^{\prime \prime}+k Z=0$, $Z(0)=0$, where $k$ is the separation constant. We also require that $R$ be bounded

![](./images/1c611338-958a-44f7-9d79-2dde87e6ac2a-37_398_440_310_37.jpg)
Figure 2 Modified Bessel functions.

![](./images/1c611338-958a-44f7-9d79-2dde87e6ac2a-37_500_401_918_42.jpg)
Figure 3

DIRICHLET PROBLEM IN A CYLINDER WITH NONZERO LATERAL TEMPERATURE
at $\rho=0$, since we are solving for the temperature inside the cylinder. If $k=0$, it is straightforward to check that we only get the solution $R=0$. If $k>0$, say $k=\lambda^{2}$, then we get the parametric form of the modified Bessel equation of order 0 defined in Exercise 7 (see also Exercises 29 and 30, Section 4.7). The general solution in this case is a linear combination of the modified Bessel functions of the first and second kind, $I_{0}$ and $K_{0}$, shown in Figure 2 (see Exercise 7). Since the first one is positive and strictly increasing for $\rho>0$, and the second one is unbounded near zero, we conclude that no nontrivial bounded linear combination of these functions can satisfy the boundary conditions on $R$. So this leaves the only possibility $k=-\lambda^{2}<0$. In this case we have

$$
\begin{gathered}
\rho^{2} R^{\prime \prime}+\rho R^{\prime}+\lambda^{2} \rho^{2} R=0, \quad R(a)=0, \\
Z^{\prime \prime}-\lambda^{2} Z=0, \quad Z(0)=0 .
\end{gathered}
$$

Applying Theorem 3, Section 4.8, we find that $R=R_{n}(\rho)=J_{0}\left(\lambda_{n} \rho\right)$, where $\lambda_{n}= \alpha_{n} / a, n=1,2, \ldots$. Solving the equation for $Z$ with $\lambda=\lambda_{n}$, we find

$$
Z_{n}(z)=\sinh \lambda_{n} z \quad n=1,2, \ldots .
$$

Superposing the product solutions we get (2) as a solution. To determine the unknown coefficients $A_{n}$, we set $z=h$ and get the Bessel series expansion

$$
f(\rho)=\sum_{n=1}^{\infty} A_{n} J_{0}\left(\lambda_{n} \rho\right) \sinh \lambda_{n} h .
$$

Thus $A_{n} \sinh \lambda_{n} h$ must be the $n$th Bessel coefficient of $f(\rho)$, and so (3) follows from Theorem 2, Section 4.8. $\square$

As a second illustration, we consider a boundary value problem with a nonzero boundary condition on the lateral surface of the cylinder (see Figure 3).

The solution of Laplace's equation (1) with boundary conditions

$$
\begin{gathered}
u(\rho, 0)=u(\rho, h)=0, \quad 0<\rho<a \\
u(a, z)=f(z), \quad 0<z<h
\end{gathered}
$$

is

$$
u(\rho, z)=\sum_{n=1}^{\infty} B_{n} I_{0}\left(\frac{n \pi}{h} \rho\right) \sin \frac{n \pi}{h} z,
$$

where $I_{0}$ is the modified Bessel function of the first kind of order 0, and

$$
B_{n}=\frac{2}{I_{0}\left(\frac{n \pi a}{h}\right) h} \int_{0}^{h} f(z) \sin \frac{n \pi}{h} z d z .
$$

![](./images/1c611338-958a-44f7-9d79-2dde87e6ac2a-38_500_378_705_65.jpg)
Figure 4 for Exercise 5.

The derivation of the solution is very much like the one we did previously, except that now the interesting case of the separation constant is $k=\nu^{2}>0$. The details are left to Exercise 8.

## Exercises 4.5

In Exercises 1-4, find the steady-state temperature in the cylinder of Figure 1 for the given temperature distribution of its top. Take $a=1$, and $h=2$.

1. $f(\rho)=100$.
2. $f(\rho)=100-\rho^{2}$.
3. $f(\rho)= \begin{cases}100 & \text { if } 0<\rho<\frac{1}{2}, \\ 0 & \text { if } \frac{1}{2}<\rho<1 .\end{cases}$
4. $f(\rho)=70 J_{0}(\rho)$.
5. (a) Find the steady-state temperature in the cylinder with boundary values as shown in Figure 4.
(b) Solve (1) for the boundary conditions

$$
\begin{gathered}
u(\rho, 0)=f_{1}(\rho), \quad 0<\rho<a \\
u(a, z)=0, \quad 0<z<h \\
u(\rho, h)=f_{2}(\rho), \quad 0<\rho<a
\end{gathered}
$$

[Hint: Combine (a) with the solution in this section.]
6. Solve (1) for the boundary conditions

$$
\begin{array}{cc}
u(\rho, 0)=100, & 0<\rho<1, \\
u(1, z)=0, & 0<z<2, \\
u(\rho, 2)=100, & 0<\rho<1 .
\end{array}
$$

7. Make the substitution $x=\lambda \rho(\lambda>0)$ in the parametric form of the modified Bessel equation $\rho^{2} R^{\prime \prime}+\rho R^{\prime}-\lambda^{2} \rho^{2} R=0$ and obtain that its general solution is $y=c_{1} I_{0}(\lambda \rho)+c_{2} K_{0}(\lambda \rho)$, where $I_{0}$ and $K_{0}$ are the modified Bessel functions of the first and second kind. [Hint: Use Exercises 29 and 30, Section 4.7.]

Project Problem: Lateral surface with nonzero temperature. Do Exercises 8 and 9.
8. In this exercise we derive (4) and (5).
(a) Refer to the Dirichlet problem in the cylinder with boundary conditions as given just before (4). Use the separation of variables method and obtain

$$
\begin{gathered}
Z^{\prime \prime}+\nu^{2} Z=0, \quad Z(0)=0 \text { and } Z(h)=0, \\
\rho^{2} R^{\prime \prime}+\rho R^{\prime}-\nu^{2} \rho^{2} R=0 .
\end{gathered}
$$

(b) Show that the only possible solutions of the first equation correspond to $\nu_{n}=\frac{n \pi}{h}$ and hence are

$$
Z_{n}(z)=\sin \frac{n \pi}{h} z, \quad n=1,2, \ldots
$$

(c) Derive (4) and (5). [Hint: Use Exercise 7.]
9. Solve (1) for the boundary conditions

$$
\begin{gathered}
u(\rho, 0)=u(\rho, 2)=0, \quad 0<\rho<1, \\
u(1, z)=10 z, \quad 0<z<2 .
\end{gathered}
$$

![](./images/1c611338-958a-44f7-9d79-2dde87e6ac2a-39_289_417_165_33.jpg)
Figure 5 for Exercise 11.

10. Solve (1) for the boundary conditions

$$
\begin{array}{ll}
u(\rho, 0)=100, & 0<\rho<1, \\
u(1, z)=10 z, & 0<z<2, \\
u(\rho, 2)=100, & 0<\rho<1 .
\end{array}
$$

[Hint: Combine the solutions of Exercises 6 and 9.]
11. Find the steady-state temperature in a cylindrical barrel floating in water as shown in Figure 5.

### 4.6 The Helmholtz and Poisson Equations

We know from Section 3.9 that several important boundary value problems can be solved by applying the method of eigenfunction expansions. In this section, we will present some applications of this method on the disk. For this purpose, we start by solving the eigenvalue problem consisting of the Helmholtz equation on a disk of radius $a$,

$$
\nabla^{2} \phi(r, \theta)=-k \phi(r, \theta), 0<r<a, 0<\theta<2 \pi,
$$

with the boundary condition

$$
\phi(a, \theta)=0,0<\theta<2 \pi .
$$

To solve this problem means to determine the values of $k$ (or eigenvalues) for which we have nontrivial solutions and find these nontrivial solutions (or eigenfunctions).

Substituting $\phi(r, \theta)=R(r) \Theta(\theta)$ into ( 1 ), separating variables, and using the fact that $\Theta$ is $2 \pi$-periodic, we arrive at the equations

$$
\begin{gathered}
\Theta^{\prime \prime}+m^{2} \Theta=0, \quad m=0,1,2, \ldots, \\
r^{2} R^{\prime \prime}+r R^{\prime}+\left(k r^{2}-m^{2}\right) R=0, \quad R(a)=0 .
\end{gathered}
$$

The solutions of (3) are

$$
\cos m \theta, \text { and } \sin m \theta, \quad m=0,1,2, \ldots .
$$

If $k<0$, equation (4) becomes the modified Bessel equation of order $m$, and it can be shown that in this case the only bounded solution with $R(a)=0$ is the zero solution. So we take $k \geq 0$ and (4) becomes the parametric form of Bessel's equation of order $m$. We know from Theorem 3, Section 4.8, that the nontrivial solutions of (4) are constant multiples of $J_{m}\left(\lambda_{m n} r\right)$, which is the solution corresponding to the eigenvalue $k=\lambda_{m n}^{2}$. Piecing together the product solutions, we obtain the following important result.

THEOREM 1 THE HELMHOLTZ EQUATION IN A DISK

THEOREM 2 EXPANSIONS IN TERMS OF THE EIGENFUNCTIONS OF THE HELMHOLTZ EQUATION

The eigenvalues of the problem (1)-(2) are

$$
k=\lambda_{m n}^{2}=\left(\alpha_{m n} / a\right)^{2}, \quad m=0,1,2, \ldots, n=1,2, \ldots
$$

where $\alpha_{m n}$ is the $n$th positive zero of the Bessel function $J_{m}$. To each eigenvalue $\lambda_{m n}^{2}$ correspond the eigenfunctions

$$
\cos m \theta J_{m}\left(\lambda_{m n} r\right) \text { and } \sin m \theta J_{m}\left(\lambda_{m n} r\right) .
$$

(Note that for $m=1,2, \ldots$ we have two distinct eigenfunctions for a given eigenvalue.)

In other words, if $\phi_{m n}(r, \theta)=\cos m \theta J_{m}\left(\lambda_{m n} r\right)$ or $\phi_{m n}(r, \theta)=\sin m \theta J_{m}\left(\lambda_{m n} r\right)$, then $\nabla^{2} \phi_{m n}=-\lambda_{m n}^{2} \phi_{m n}$ and $\phi(a, \theta)=0$.

As you will discover, the eigenfunctions satisfy orthogonality relations that can be used to expand functions on the disk, much as we used $\cos n x$ and $\sin n x$ to expand functions in terms of Fourier series. The orthogonality here follows as a consequence of the orthogonality of the Bessel functions and the trigonometric system. Because the orthogonality relations for the Bessel functions are expressed with respect to the weight function $r$ (Theorem 1, Section 4.8), the orthogonality of the eigenfunctions in (6) will be expressed by integrals over the disk with respect to $r d r d \theta$. For example, we have

$$
\int_{0}^{2 \pi} \int_{0}^{a} \sin m \theta J_{m}\left(\lambda_{m n} r\right) \cos m \theta J_{m}\left(\lambda_{m n} r\right) r d r d \theta=0
$$

Putting these facts together, we obtain the following expansion theorem, which was already used in (8), Section 4.3.

Suppose that $f(r, \theta)$ is defined for all $0<r<a$ and $0<\theta<2 \pi$. Then

$$
f(r, \theta)=\sum_{m=0}^{\infty} \sum_{n=1}^{\infty} J_{m}\left(\lambda_{m n} r\right)\left(a_{m n} \cos m \theta+b_{m n} \sin m \theta\right)
$$

where (the generalized Fourier coefficients) $a_{m n}$ and $b_{m n}$ are given by (12)(14), Section 4.3.

In Section 4.3, we established (8) as a consequence of Fourier series and Bessel-Fourier series. A simpler and more direct derivation can be obtained using the orthogonality of the eigenfunctions (6) (see Exercise 4).

## EXAMPLE 1 The method of eigenfunction expansions

Solve $\nabla^{2} u(r, \theta)=u(r, \theta)+3 r^{2} \cos 2 \theta$ in the unit disk, given that $u=0$ on the boundary.

Solution We look for a solution in the form of an eigenfunction expansion

$$
u(r, \theta)=\sum_{m=0}^{\infty} \sum_{n=1}^{\infty} J_{m}\left(\alpha_{m n} r\right)\left(A_{m n} \cos m \theta+B_{m n} \sin m \theta\right)
$$

Since each eigenfunction satisfies the boundary condition, our candidate for a solution, $u(r, \theta)$, also satisfies the boundary condition. Plugging $u$ into the equation and using the fact that, for an eigenfunction $\phi_{m n}, \nabla^{2} \phi_{m n}=-\alpha_{m n}^{2} \phi_{m n}$, we get

$$
\begin{aligned}
\sum_{m=0}^{\infty} & \sum_{n=1}^{\infty}-\alpha_{m n}^{2} J_{m}\left(\alpha_{m n} r\right)\left(A_{m n} \cos m \theta+B_{m n} \sin m \theta\right) \\
& =\sum_{m=0}^{\infty} \sum_{n=1}^{\infty} J_{m}\left(\alpha_{m n} r\right)\left(A_{m n} \cos m \theta+B_{m n} \sin m \theta\right)+3 r^{2} \cos 2 \theta
\end{aligned}
$$

hence

$$
\sum_{m=0}^{\infty} \sum_{n=1}^{\infty}\left(-1-\alpha_{m n}^{2}\right) J_{m}\left(\alpha_{m n} r\right)\left(A_{m n} \cos m \theta+B_{m n} \sin m \theta\right)=3 r^{2} \cos 2 \theta
$$

Thus $\left(-1-\alpha_{m n}^{2}\right) A_{m n}$ and $\left(-1-\alpha_{m n}^{2}\right) B_{m n}$ are the generalized Fourier coefficients of the function $f(r, \theta)=3 r^{2} \cos 2 \theta$. Note that the orthogonality of the trigonometric system will imply that only $A_{2 n}$ is nonzero. All other coefficients will be zero. Appealing to (13), Section 4.3, with $m=2$, we find

$$
\begin{aligned}
\left(-1-\alpha_{2 n}^{2}\right) A_{2 n} & =\frac{2}{\pi J_{3}^{2}\left(\alpha_{2 n}\right)} \int_{0}^{1} \int_{0}^{2 \pi} 3 \cos ^{2} 2 \theta d \theta r^{2} J_{2}\left(\alpha_{2 n} r\right) r d r \\
& =\frac{6}{J_{3}^{2}\left(\alpha_{2 n}\right)} \int_{0}^{1} r^{3} J_{2}\left(\alpha_{2 n} r\right) d r \quad\left(\int_{0}^{2 \pi} \cos ^{2} 2 \theta d \theta=\pi\right) \\
& =\frac{6}{J_{3}^{2}\left(\alpha_{2 n}\right)} \frac{J_{3}\left(\alpha_{2 n}\right)}{\alpha_{2 n}} \quad(\text { by (11), Section 4.2) } \\
& =\frac{6}{\alpha_{2 n} J_{3}\left(\alpha_{2 n}\right)}
\end{aligned}
$$

Solving for $A_{2 n}$ and plugging into the eigenfunction expansion of $u$, we find

$$
u(r, \theta)=\cos 2 \theta \sum_{n=1}^{\infty} \frac{-6}{\left(1+\alpha_{2 n}^{2}\right) \alpha_{2 n} J_{3}\left(\alpha_{2 n}\right)} J_{2}\left(\alpha_{2 n} r\right)
$$

The collapsing of the double sum in (8) to a single sum is due to the fact that only the terms in $\cos 2 \theta$ are needed here. In general, you may need the entire double sum.

## Poisson's Equation in a Disk

Consider the Poisson problem

$$
\begin{gathered}
\nabla^{2} u=f(r, \theta), \quad 0<r<a, \quad 0<\theta<2 \pi \\
u(a, \theta)=g(\theta), \quad 0<\theta<2 \pi
\end{gathered}
$$

Figure 1 Decomposition of a Poisson problem.

Our first step is to decompose the problem into the two simpler subproblems in Figure 1.

![](./images/1c611338-958a-44f7-9d79-2dde87e6ac2a-42_534_1209_253_593.jpg)
(a) Poisson problem with zero boundary data
(b) Dirichlet problem

The Dirichlet problem in Figure 1(b) can be solved by the methods of Section 4.4. Thus, to complete the solution, we need only solve Poisson's equation with zero boundary data (Figure 1(a)). We will use the method of eigenfunction expansions. This method tells us to look for a solution of (9) (with zero boundary data) in the form

$$
u(r, \theta)=\sum_{m=0}^{\infty} \sum_{n=1}^{\infty} J_{m}\left(\lambda_{m n} r\right)\left(A_{m n} \cos m \theta+B_{m n} \sin m \theta\right)
$$

Plugging into (9) and using the fact that each eigenfunction satisfies (1), we obtain

$$
\sum_{m=0}^{\infty} \sum_{n=1}^{\infty}-\lambda_{m n}^{2} J_{m}\left(\lambda_{m n} r\right)\left(A_{m n} \cos m \theta+B_{m n} \sin m \theta\right)=f(r, \theta) .
$$

This being the eigenfunction expansion of $f(r, \theta)$, we apply Theorem 2, solve for $A_{m n}$ and $B_{m n}$, and obtain, for $m, n=1,2, \ldots$,

$$
A_{0 n}=\frac{-1}{\pi \alpha_{0 n}^{2} J_{1}^{2}\left(\alpha_{0 n}\right)} \int_{0}^{a} \int_{0}^{2 \pi} f(r, \theta) J_{0}\left(\lambda_{0 n} r\right) r d \theta d r
$$

$$
A_{m n}=\frac{-2}{\pi \alpha_{m n}^{2} J_{m+1}^{2}\left(\alpha_{m n}\right)} \int_{0}^{a} \int_{0}^{2 \pi} f(r, \theta) \cos m \theta J_{m}\left(\lambda_{m n} r\right) r d \theta d r
$$

$$
B_{m n}=\frac{-2}{\pi \alpha_{m n}^{2} J_{m+1}^{2}\left(\alpha_{m n}\right)} \int_{0}^{a} \int_{0}^{2 \pi} f(r, \theta) \sin m \theta J_{m}\left(\lambda_{m n} r\right) r d \theta d r
$$

This completely determines the solutions of the problem in Figure 1(a). We summarize our findings as follows.

## SOLUTION OF POISSON'S PROBLEM IN A DISK

The solution of the Poisson problem (9)-(10) is given by

$$
u(r, \theta)=u_{1}(r, \theta)+u_{2}(r, \theta),
$$

where $u_{1}$ is the solution of the Poisson problem with zero boundary data in Figure 1(a), and $u_{2}$ is the solution of the Dirichlet problem in Figure 1(b). The function $u_{1}$ is given by (11)-(14), and the function $u_{2}$ is given by (4)-(5), Section 4.4.

## EXAMPLE 2 A Poisson problem with zero boundary data

Solve $\nabla^{2} u=1$ in the unit disk, given that $u=0$ on the boundary.
Solution Note that in this case $u_{2}=0$ in (15). The function $u_{1}$ is given by (11). Since the whole problem is independent of $\theta$, we expect the solution to be inclependent of $\theta$. Indeed, plugging $f(r, \theta)=1$ into (13) and (14), we get 0 because of the integral in $\theta$. Now (12) yields

$$
A_{0 n}=\frac{-2}{\alpha_{0 n}^{2} J_{1}^{2}\left(\alpha_{0 n}\right)} \int_{0}^{1} J_{0}\left(\alpha_{0 n} r\right) r d r
$$

Using (11), Section 4.2, to evaluate the integral and simplifying, we get $A_{0 n}= \frac{-2}{\alpha_{0 n}^{3} J_{1}\left(\alpha_{0 n}\right)}$. Substituting into (11), we obtain

$$
u(r, \theta)=\sum_{n=1}^{\infty} \frac{-2}{\alpha_{0 n}^{3} J_{1}\left(\alpha_{0 n}\right)} J_{0}\left(\alpha_{0 n} r\right)
$$

Interesting applications of the eigenfunction expansions method are presented in the exercises.

## Exercises 4.6

1. Derive (3) and (4) from (1) and (2).
2. State and prove all the orthogonality relations for the eigenfunctions of the Helmholtz problem (1) and (2) ((7) is one of them).
3. Let $\phi_{m n}(r, \theta)$ denote either one of the eigenfunctions in (6). Evaluate

$$
\int_{0}^{2 \pi} \int_{0}^{a} \phi_{m n}^{2}(r, \theta) r d r d \theta
$$

Treat the case $m=0$ separately. [Hint: Use (12), Section 4.8.]
4. Derive the coefficients in Theorem 2 by using the orthogonality of the eigenfunctions (6). [Hint: Multiply both sides of (8) by an eigenfunction, interchange integrals and summation signs, then integrate over the disk with respect to $r d \theta d r$.]

In Exercises 5-12, use the method of eigenfunction expansions to solve the given problem in the unit disk.
5. $\nabla^{2} u=-u+1, u(1, \theta)=0$.
6. $\nabla^{2} u=3 u+r \sin \theta, u(1, \theta)=0$.
7. $\nabla^{2} u=2+r^{3} \cos 3 \theta, u(1, \theta)=0$.
8. $\nabla^{2} u=r^{2}, u(1, \theta)=0$.
9.

$$
\begin{gathered}
\nabla^{2} u= \begin{cases}r \sin \theta & \text { if } 0<r<\frac{1}{2} \\
0 & \text { if } \frac{1}{2}<r<1\end{cases} \\
u(1, \theta)=0 .
\end{gathered}
$$

10. $\nabla^{2} u=r^{m} \sin m \theta, u(1, \theta)=0$.
11. $\nabla^{2} u=1, u(1, \theta)=\sin 2 \theta$.
12. $\nabla^{2} u=1+r \cos \theta, u(1, \theta)=1$.
13. A heat problem. Do Exercise 11, Section 4.3, using the method of eigenfunction expansions.
14. Project Problem: A nonhomogeneous heat problem. For this project, you are asked to use the eigenfunction expansions method to solve the nonhomogeneous heat boundary value problem, with time-dependent heat source,

$$
\begin{gathered}
\frac{\partial u}{\partial t}=c^{2}\left(\frac{\partial^{2} u}{\partial r^{2}}+\frac{1}{r} \frac{\partial u}{\partial r}+\frac{1}{r^{2}} \frac{\partial^{2} u}{\partial \theta^{2}}\right)+q(r, \theta, t) \\
u(a, \theta, t)=0 \\
u(r, \theta, 0)=f(r, \theta)
\end{gathered}
$$

where $0<r<a, 0<\theta<2 \pi$, and $t>0$. Justify the following steps.
(a) Let

$$
\begin{gathered}
u(r, \theta, t)=\sum_{m=0}^{\infty} \sum_{n=1}^{\infty} J_{m}\left(\lambda_{m n} r\right)\left(A_{m n}(t) \cos m \theta+B_{m n}(t) \sin m \theta\right) \\
f(r, \theta)=\sum_{m=0}^{\infty} \sum_{n=1}^{\infty} J_{m}\left(\lambda_{m n} r\right)\left(a_{m n} \cos m \theta+b_{m n} \sin m \theta\right) \\
q(r, \theta, t)=\sum_{m=0}^{\infty} \sum_{n=1}^{\infty} J_{m}\left(\lambda_{m n} r\right)\left(c_{m n}(t) \cos m \theta+d_{m n}(t) \sin m \theta\right)
\end{gathered}
$$

(Why should this be your starting point?) What are $a_{m n}, b_{m n}, c_{m n}(t)$, and $d_{m n}(t)$, in terms of $f$ and $q$ ?
(b) Show that $A_{m n}$ and $B_{m n}$ are solutions of the following initial value problems:

$$
\begin{array}{ll}
A_{m n}^{\prime}(t)+\lambda_{m n}^{2} A_{m n}(t)=c_{m n}(t), & A_{m n}(0)=a_{m n} \\
B_{m n}^{\prime}(t)+\lambda_{m n}^{2} B_{m n}(t)=d_{m n}(t), & B_{m n}(0)=b_{m n}
\end{array}
$$

(c) Complete the solution by showing that

$$
A_{m n}(t)=e^{-\lambda_{m n}^{2} t}\left(a_{m n}+\int_{0}^{t} e^{\lambda_{m n}^{2} s} c_{m n}(s) d s\right)
$$

and

$$
B_{m n}(t)=e^{-\lambda_{m n}^{2} t}\left(b_{m n}+\int_{0}^{t} e^{\lambda_{m n}^{2} s} d_{m n}(s) d s\right)
$$

15. (a) Work out the details in Exercise 14 when $c=1, f=1$, and $q(r, \theta, t)=e^{-t}$.
(b) Plot the temperature of the center and describe what happens as $t \rightarrow \infty$.
16. (a) Work out the details in Exercise 14 when $c=1, f=r \sin \theta$, and $q=1$.
(b) Plot the temperature of the center and describe what happens as $t \rightarrow \infty$.

### 4.7 Bessel's Equation and Bessel Functions

We saw in this chapter that Bessel's equation of order $p \geq 0$,

$$
x^{2} y^{\prime \prime}+x y^{\prime}+\left(x^{2}-p^{2}\right) y=0, \quad x>0
$$

arises when solving partial differential equations involving the Laplacian in polar and cylindrical coordinates. Note that Bessel's equation is a whole family of differential equations, one for each value of $p$. Note also the unfortunate clash of terminology-Bessel's equation of order $p$ is a differential equation of order 2 .

Bessel's equation also appears in solving various other classical problems. Historically, the equation with $p=0$ was first encountered and solved by Daniel Bernoulli in 1732 in his study of the hanging chain problem (Section 6.3). Similar equations appeared later in 1770 in the work of Lagrange on astronomical problems. In 1824, while investigating the problem of elliptic planetary motion, the great German astronomer F. W. Bessel encountered a special form of (1). Influenced by the monumental work of Fourier that had just appeared in 1822 (see Chapter 2), Bessel conducted a systematic study of (1).

## Solution of Bessel's Equation

We will apply the method of Frobenius from Appendix A.6. It is easy to show that $x=0$ is a regular singular point of Bessel's equation. So, as suggested by the method of Frobenius, we try for a solution

$$
y=\sum_{m=0}^{\infty} a_{m} x^{r+m}
$$

where $a_{0} \neq 0$. Substituting this into (1) yields

We have shifted the index of summation by 2 in the third series so that each series is expressed in terms of $x^{r+m}$.

$$
\begin{aligned}
& \sum_{m=0}^{\infty} a_{m}(r+m)(r+m-1) x^{r+m}+\sum_{m=0}^{\infty} a_{m}(r+m) x^{r+m} \\
& \quad+\sum_{m=2}^{\infty} a_{m-2} x^{r+m}-p^{2} \sum_{m=0}^{\infty} a_{m} x^{r+m}=0
\end{aligned}
$$

Writing the terms corresponding to $m=0$ and $m=1$ separately gives

$$
\begin{aligned}
& a_{0}\left(r^{2}-p^{2}\right) x^{r}+a_{1}\left[(r+1)^{2}-p^{2}\right] x^{r+1} \\
& \quad+\sum_{m=2}^{\infty}\left(a_{m}\left[(r+m)^{2}-p^{2}\right]+a_{m-2}\right) x^{r+m}=0
\end{aligned}
$$

Equating coefficients of the series to zero gives

$$
\begin{gathered}
a_{0}\left(r^{2}-p^{2}\right)=0 \quad(m=0) \\
a_{1}\left[(r+1)^{2}-p^{2}\right]=0 \quad(m=1) \\
a_{m}\left[(r+m)^{2}-p^{2}\right]+a_{m-2}=0 \quad(m \geq 2)
\end{gathered}
$$

From (3), since $a_{0} \neq 0$, we get the indicial equation

$$
(r+p)(r-p)=0
$$

with indicial roots $r=p$ and $r=-p$.

## First Solution of Bessel's Equation

Setting $r=p$ in (5) gives the recurrence relation

$$
a_{m}=\frac{-1}{m(m+2 p)} a_{m-2}, \quad m \geq 2
$$

This is a two-step recurrence relation, so the even- and odd-indexed terms are determined separately. We deal with the odd-indexed terms first. With $r=p$, (4) becomes $a_{1}\left[(p+1)^{2}-p^{2}\right]=0$ which implies that $a_{1}=0$ (recall that $p \geq 0$ in (1)), and so $a_{3}=a_{5}=\cdots=0$. To make it easier to find a pattern for the even-indexed terms we rewrite the recurrence relation with $m=2 k$ and get

$$
a_{2 k}=\frac{-1}{2^{2} k(k+p)} a_{2(k-1)}, \quad k \geq 1
$$

This gives

$$
\begin{aligned}
& a_{2}=\frac{-1}{2^{2}(1+p)} a_{0} \\
& a_{4}=\frac{-1}{2^{2} 2(2+p)} a_{2}=\frac{1}{2^{4} 2!(1+p)(2+p)} a_{0} \\
& a_{6}=\frac{-1}{2^{2} 3(3+p)} a_{4}=\frac{-1}{2^{6} 3!(1+p)(2+p)(3+p)} a_{0}
\end{aligned}
$$

and so on. Substituting these coefficients into (2) gives one solution to Bessel's equation:

$$
y=a_{0} \sum_{k=0}^{\infty} \frac{(-1)^{k}}{2^{2 k} k!(1+p)(2+p) \cdots(k+p)} x^{2 k+p},
$$

where $a_{0} \neq 0$ is arbitrary. This solution may be written in a nicer way with the aid of the gamma function. (If you have not previously encountered this function, it is described at the end of this section.) We choose

$$
a_{0}=\frac{1}{2^{p} \Gamma(p+1)}
$$

and simplify the terms in the series using the basic property of the gamma function, $\Gamma(x+1)=x \Gamma(x)$, as follows:

$$
\begin{aligned}
\Gamma(1+p)[(1+p)(2+p) \cdots(k+p)] & =\Gamma(2+p)[(2+p) \cdots(k+p)] \\
& =\Gamma(3+p)[\cdots(k+p)] \\
& =\cdots=\Gamma(k+p+1) .
\end{aligned}
$$

After this simplification, (6) yields the first solution, denoted by $J_{p}$ and called the Bessel function of order $p$,

$$
J_{p}(x)=\sum_{k=0}^{\infty} \frac{(-1)^{k}}{k!\Gamma(k+p+1)}\left(\frac{x}{2}\right)^{2 k+p} .
$$

When $p=n$, we have $\Gamma(k+p+1)=(k+n)$ ! (see (14) below), and so the Bessel function of order $n$ is

$$
J_{n}(x)=\sum_{k=0}^{\infty} \frac{(-1)^{k}}{k!(k+n)!}\left(\frac{x}{2}\right)^{2 k+n} .
$$

To get an idea of the behavior of the Bessel functions, we sketch the graphs of $J_{0}, J_{1 / 2}, J_{1}, J_{2}$ and $J_{7}$ in Figure 1.

$$
\begin{aligned}
& J_{0}(0)=1 \\
& J_{p}(0)=0 \text { if } p>0
\end{aligned}
$$

![](./images/1c611338-958a-44f7-9d79-2dde87e6ac2a-48_509_1237_188_544.jpg)
Figure 1 Graphs of $J_{p}(x)$ for $p=0, \frac{1}{2}, 1,2,7$.

Note that $J_{p}$ is bounded at 0 . As we will see shortly, this property is not shared by the second linearly independent solution.

## Second Solution of Bessel's Equation

If in (2) we replace $r$ by the second indicial root $-p$, we arrive as before at the solution

$$
J_{-p}(x)=\sum_{k=0}^{\infty} \frac{(-1)^{k}}{k!\Gamma(k-p+1)}\left(\frac{x}{2}\right)^{2 k-p}
$$

It turns out that if $p$ is not an integer, then (8) is linearly independent of $J_{p}$. Thus when $p$ is not an integer, (7) and (8) determine a fundamental set of solutions of Bessel's equation of order $p$. Before turning to the case when $p$ is an integer, we compute the Bessel functions $J_{p}$ and $J_{-p}$ for the value $p=\frac{1}{2}$.

## EXAMPLE 1 Bessel functions of order $p= \pm \frac{1}{2}$

Show that

$$
J_{1 / 2}(x)=\sqrt{\frac{2}{\pi x}} \sin x \quad \text { and } \quad J_{-1 / 2}(x)=\sqrt{\frac{2}{\pi x}} \cos x .
$$

Solution Substituting $p=\frac{1}{2}$ in (7), we get

$$
J_{1 / 2}(x)=\sum_{k=0}^{\infty} \frac{(-1)^{k}}{k!\Gamma\left(k+\frac{1}{2}+1\right)}\left(\frac{x}{2}\right)^{2 k+\frac{1}{2}} .
$$

To simplify this expression, we use the result of Exercise 44(b), which implies that

$$
\Gamma\left(k+\frac{1}{2}+1\right)=\frac{(2 k+1)!}{2^{2 k+1} k!} \sqrt{\pi} .
$$

![](./images/1c611338-958a-44f7-9d79-2dde87e6ac2a-49_369_444_178_47.jpg)
Figure 2 Graphs of $J_{1 / 2}$, $J_{-1 / 2}$, and their envelopes $y= \pm \sqrt{\frac{2}{\pi x}}$.

![](./images/1c611338-958a-44f7-9d79-2dde87e6ac2a-49_362_467_1026_45.jpg)
Figure 3 Approximation of $Y_{2}$.

Thus

$$
\begin{aligned}
J_{1 / 2}(x) & =\frac{1}{\sqrt{\pi}} \sum_{k=0}^{\infty} \frac{(-1)^{k} 2^{2 k+1} k!}{k!(2 k+1)!}\left(\frac{x}{2}\right)^{2 k+\frac{1}{2}} \\
& =\sqrt{\frac{2}{\pi x}} \sum_{k=0}^{\infty} \frac{(-1)^{k}}{(2 k+1)!} x^{2 k+1}=\sqrt{\frac{2}{\pi x}} \sin x
\end{aligned}
$$

The other part is proved similarly by substituting $p=-\frac{1}{2}$ into (8) and simplifying with the help Exercise 44(a) (see Exercise 21). In Figure 2 we plotted $J_{\frac{1}{2}}$ and $J_{-\frac{1}{2}}$. Clearly these two functions are linearly independent, since the first one is bounded while the second one is not.

It is important to keep in mind that $J_{p}$ and $J_{-p}$ are linearly independent only when $p$ is not an integer. In fact, when $p$ is a positive integer, we observe that $k-p+1 \leq 0$ for $k=0,1, \ldots, p-1$, and so the coefficients in (8) are not even defined for $k=0,1, \ldots, p-1$, because the gamma function is not defined at 0 and negative integers. It is useful, however, to have a definition for $J_{-n}$ for $n=1,2, \ldots$. A simple construction of this function is presented in Exercise 16. It yields a second linearly dependent solution that satisfies

$$
J_{-n}(x)=(-1)^{n} J_{n}(x) \quad(n \text { integer } \geq 0)
$$

We could use the Frobenius method to derive a second linearly independent solution. However, we will describe an alternative method that is commonly used in applied mathematics. We start again with the case when $p$ is not an integer and define

$$
Y_{p}(x)=\frac{J_{p}(x) \cos p \pi-J_{-p}(x)}{\sin p \pi} \quad(p \text { not an integer }) .
$$

Since $J_{p}$ and $J_{-p}$ are in this case linearly independent solutions of Bessel's equation, it follows from (10) that $Y_{p}$ is also a solution of Bessel's equation that is linearly independent of $J_{p}$. The function $Y_{p}$ is called a Bessel function of the second kind of order $p$. For integer $p$, this function is constructed by a limiting process from the noninteger values as follows:

![](./images/1c611338-958a-44f7-9d79-2dde87e6ac2a-49_373_467_1777_45.jpg)
Figure $4 Y_{0}, Y_{1}, Y_{2}$.

$$
Y_{p}=\lim _{\nu \rightarrow p} Y_{\nu}
$$

It can be shown that this limit exists (see Figure 3 for an illustration) and defines a solution of Bessel's equation of order $p$ which is also linearly independent of $J_{p}$. As illustrated in Figure 4, we have

## GENERAL

SOLUTION OF BESSEL'S EQUATION OF ORDER $p$

In particular, the Bessel functions of the second kind are not bounded near 0 . We summarize our analysis of (1) as follows.

The general solution of Bessel's equation (1) of order $p$ is

$$
y(x)=c_{1} J_{p}(x)+c_{2} Y_{p}(x)
$$

where $J_{p}$ is given by (7) and $Y_{p}$ is given by (10) or (11). When $p$ is not an integer, a general solution is also given by

$$
y(x)=c_{1} J_{p}(x)+c_{2} J_{-p}(x),
$$

where $J_{p}$ is given by (7) and $J_{-p}$ is given by (8).
Explicit formulas and computations of the Bessel functions are presented in the exercises. We next investigate the gamma function.

## The Gamma Function

The gamma function is defined for $x>0$ by

$$
\Gamma(x)=\int_{0}^{\infty} t^{x-1} e^{-t} d t
$$

This integral is improper and converges for all $x>0$. The basic property of the gamma function is

$$
\Gamma(x+1)=x \Gamma(x) .
$$

To prove this we use integration by parts as follows:

$$
\Gamma(x+1)=\int_{0}^{\infty} t^{x} e^{-t} d t=-\left.t^{x} e^{-t}\right|_{0} ^{\infty}+x \int_{0}^{\infty} t^{x-1} e^{-t} d t=x \Gamma(x)
$$

where in the first integral we let $u(t)=t^{x}, d v=e^{-t} d t, d u=x t^{x-1} d t, v(t)= -e^{-t}$.

We can easily find the values of the gamma function at the positive integers. For example,

$$
\Gamma(1)=\int_{0}^{\infty} e^{-t} d t=1
$$

The basic property now gives

$$
\Gamma(2)=1 \Gamma(1)=1!, \quad \Gamma(3)=2 \Gamma(2)=2!, \quad \Gamma(4)=3 \Gamma(3)=3!, \ldots
$$

Continuing in this manner, we see that

$$
\Gamma(n+1)=n!
$$

for all $n=0,1,2,3, \ldots$, where we have set $0!=1$. For this reason the gamma function is sometimes called the generalized factorial function. Other values of the gamma function can be found with various degrees of difficulty. From the value

$$
\Gamma\left(\frac{1}{2}\right)=\sqrt{\pi}
$$

(Exercise 34) and the basic property we find

$$
\Gamma\left(\frac{3}{2}\right)=\frac{1}{2} \Gamma\left(\frac{1}{2}\right)=\frac{\sqrt{\pi}}{2} \quad \text { and } \quad \Gamma\left(\frac{5}{2}\right)=\frac{3}{2} \Gamma\left(\frac{3}{2}\right)=\frac{3}{2} \frac{\sqrt{\pi}}{2}=\frac{3}{4} \sqrt{\pi} .
$$

Although we have defined the gamma function for $x>0$, it is possible to extend its definition to all real numbers other than $0,-1,-2,-3, \ldots$ in such a way that the basic property continues to hold. To do so, we write the basic property as

$$
\Gamma(x)=\frac{1}{x} \Gamma(x+1)
$$

and then define the value of the gamma function at $x$ from its value at $x+1$. For example, we have

$$
\Gamma\left(-\frac{1}{2}\right)=-2 \Gamma\left(\frac{1}{2}\right)=-2 \sqrt{\pi} \quad \text { and } \quad \Gamma\left(-\frac{3}{2}\right)=-\frac{2}{3} \Gamma\left(-\frac{1}{2}\right)=\frac{4}{3} \sqrt{\pi} .
$$

This clearly extends the definition of the gamma function to negative numbers other than $-1,-2,-3, \ldots$. The graph of the gamma function is sketched in Figure 5. Notice the vertical asymptotes at $x=0,-1,-2$, ... Also notice the alternating sign of the gamma function over negative intervals.

For $n=0,1,2, \ldots$,
$\Gamma(n+1)=n!$
$\Gamma(1)=0!=1$
$\Gamma(-n)$ is not defined
$\Gamma(x)>0$ for $x>0$
$\Gamma(x)$ alternates signs on the negative axis.

![](./images/1c611338-958a-44f7-9d79-2dde87e6ac2a-52_528_1248_208_558.jpg)
Figure $5 \Gamma(x)$, the generalized factorial function.

## Exercises 4.7

In Exercises 1-4, determine the order $p$ of the given Bessel equation. Use (7) to write down three terms of the first series solution.

1. $x^{2} y^{\prime \prime}+x y^{\prime}+\left(x^{2}-9\right) y=0$.
2. $x^{2} y^{\prime \prime}+x y^{\prime}+x^{2} y=0$.
3. $x^{2} y^{\prime \prime}+x y^{\prime}+\left(x^{2}-\frac{1}{4}\right) y=0$.
4. $x^{2} y^{\prime \prime}+x y^{\prime}+\left(x^{2}-\frac{1}{9}\right) y=0$.

In Exercises 5-8, find the general solution of the given differential equation on $(0, \infty)$. Write down two terms of the series expansions of each part of the solution. [Hint: Use (8).]
5. $x^{2} y^{\prime \prime}+x y^{\prime}+\left(x^{2}-\frac{9}{4}\right) y=0$.
6. $x^{2} y^{\prime \prime}+x y^{\prime}+\left(x^{2}-\frac{25}{4}\right) y=0$.
7. $x^{2} y^{\prime \prime}+x y^{\prime}+\left(x^{2}-\frac{1}{16}\right) y=0$.
8. $x^{2} y^{\prime \prime}+x y^{\prime}+\left(x^{2}-\frac{1}{25}\right) y=0$.
9. Find at least three terms of a second linearly independent solution of the equation of Exercise 1 using the Frobenius method. (A first solution is given by (7).)
10. Verify that $y_{1}=x^{p} J_{p}(x)$ and $y_{2}=x^{p} Y_{p}(x)$ are linearly independent solutions of

$$
x y^{\prime \prime}+(1-2 p) y^{\prime}+x y=0, \quad x>0
$$

In Exercises 11-14, use the result of Exercise 10 to solve the given equation for $x>0$.
11. $x y^{\prime \prime}-y^{\prime}+x y=0$.
12. $y^{\prime \prime}+y=0$.
13. $x y^{\prime \prime}-2 y^{\prime}+x y=0$.
14. $x y^{\prime \prime}-3 y^{\prime}+x y=0$.
15. Establish the following properties:
(a) $J_{0}(0)=1, J_{p}(0)=0$ if $p>0$;
(b) $J_{n}(x)$ is an even function if $n$ is even, and odd if $n$ is odd;
(c) $\lim _{x \rightarrow 0^{+}} \frac{J_{p}(x)}{x^{p}}=\frac{1}{2^{p} \Gamma(p+1)}$.
16. Suppose in (7) we replace $p$ by a negative integer $-n$.
(a) Based on the properties of the gamma function, explain why in (7) it makes sense to set $1 / \Gamma(k-p+1)=0$ for $k=0,1,2, \ldots, p-1$. [Hint: Exercise 32 below.]
(b) By reindexing the series that you obtain, show that $J_{-n}(x)=(-1)^{n} J_{n}(x)$.

In Exercises 17-20, solve the given equation by reducing it first to a Bessel's equation. Use the suggested change of variables and take $x>0$.
17. $x y^{\prime \prime}+(1+2 p) y^{\prime}+x y=0, y=x^{-p} u$.
18. $x y^{\prime \prime}+y^{\prime}+\frac{1}{4} y=0, z=\sqrt{x}$.
19. $y^{\prime \prime}+e^{-x} y=0, \quad z=2 e^{-\frac{x}{2}}$.
20. $x^{2} y^{\prime \prime}+x y^{\prime}+\left(4 x^{4}-\frac{1}{4}\right) y=0, z=x^{2}$.
21. Show that $J_{-1 / 2}(x)=\sqrt{\frac{2}{\pi x}} \cos x$.
22. Establish the identities
(a) $J_{3 / 2}(x)=\sqrt{\frac{2}{\pi x}}\left[\frac{\sin x}{x}-\cos x\right]$.
(b) $J_{-3 / 2}(x)=\sqrt{\frac{2}{\pi x}}\left[-\frac{\cos x}{x}-\sin x\right]$.

## 23. General solution of Bessel's equation of order 0.

(a) Use (7) to derive the first six terms of the series solution $J_{0}$ of the Bessel's equation $x^{2} y^{\prime \prime}+x y^{\prime}+x^{2} y=0$.
(b) Use (a) and the reduction of order formula to find six terms of $y_{2}$, the second series solution. [Hint: See Example 5, Appendix A.6.]
(b) Plot your answers and compare their graphs to those of $J_{0}$ and $Y_{0}$ for $x$ near zero, say $0<x<4$. Describe what you find.
(c) Explain why we must have $Y_{0}=a J_{0}+b y_{2}$, where $a$ and $b$ are some constants. Evaluate the functions at two points in the interval $0<x<4$, say at $x=.2$ and $x=.3$, and obtain two equations in the unknown coefficients $a$ and $b$. Solve the equations to determine $a$ and $b$, and then plot and compare the graphs of $Y_{0}$ and $a J_{0}+b y_{2}$.
24. Repeat Exercise 23 with Bessel's equation of order 1.
25. Project Problem: The aging spring problem. The equation

$$
y^{\prime \prime}(t)+e^{-a t+b} y(t)=0 \quad(a>0), \quad t>0
$$

models the vibrations of a spring whose spring constant is tending to zero with time.
(a) Show that the change of variables $u=\frac{2}{a} e^{-\frac{1}{2}(a t-b)}$ transforms the differential equation into Bessel's equation of order zero (with the new variable $u$ ). [Hint: Let $\left.Y(u)=y(t), e^{-a t+b}=\frac{a^{2}}{4} u^{2} ; \quad \frac{d y}{d t}=-\frac{a}{2} u \frac{d Y}{d u} ; \quad \frac{d^{2} y}{d t^{2}}=\frac{a^{2}}{4} u\left[\frac{d Y}{d u}+u \frac{d^{2} Y}{d u^{2}}\right].\right]$
(b) Obtain the general solution of the differential equation in the form

$$
y(t)=c_{1} J_{0}\left(\frac{2}{a} e^{-\frac{1}{2}(a t-b)}\right)+c_{2} Y_{0}\left(\frac{2}{a} e^{-\frac{1}{2}(a t-b)}\right),
$$

where $c_{1}$ and $c_{2}$ are arbitrary constants, $J_{0}$ is the Bessel function of order 0 , and $Y_{0}$ is the Bessel function of order 0 of the second kind.
(c) Discuss the behavior of the solution as $t \rightarrow \infty$ in the following three cases: $c_{1}=0, c_{2} \neq 0 ; c_{1} \neq 0, c_{2}=0 ; c_{1} \neq 0, c_{2} \neq 0$. Does it make sense to have unbounded solutions of the differential equation? [Hint: What happens to the differential equation as $t \rightarrow \infty$ ?]

In Exercises 26-27, solve the given aging spring problem. In each case determine whether the solution is bounded or unbounded as $t \rightarrow \infty$.
26. $y^{\prime \prime}(t)+e^{-2 t} y(t)=0, y(0)=J_{0}(1) \approx .765, y^{\prime}(0)=-J_{0}^{\prime}(1) \approx .440$.
27. $y^{\prime \prime}(t)+e^{-2 t} y(t)=0, y(0)=.1, y^{\prime}(0)=0$. [Use $J_{0}(1) \approx .765 ; J_{0}^{\prime}(1) \approx-.440$; $Y_{0}(1) \approx .088 ; Y_{0}^{\prime}(1) \approx .781$.]
28. Bessel's function of the second kind of order zero. The Bessel function of the second kind of order 0 is given explicitly by the formula

$$
Y_{0}(x)=\frac{2}{\pi}\left[J_{0}(x)(\ln x+\gamma)+\sum_{m=1}^{\infty} \frac{(-1)^{m-1} h_{m}}{2^{2 m}(m!)^{2}} x^{2 m}\right],
$$

where $h_{m}=1+\frac{1}{2}+\frac{1}{3}+\ldots+\frac{1}{m}$ and $\gamma$ is Euler's constant:

$$
\gamma=\lim _{m \rightarrow \infty}\left(h_{m}-\ln m\right) \approx 0.577216 .
$$

(a) Approximate the numerical value of Euler's constant.
(b) Justify the property $\lim _{x \rightarrow 0^{+}} Y_{0}(x)=-\infty$.
29. Modified Bessel function. In some applications the Bessel function $J_{p}$ appears as a function of the pure imaginary number $i x$.
(a) Show that $J_{p}(i x)=i^{p} \sum_{k=0}^{\infty} \frac{(x / 2)^{2 k+p}}{k!\Gamma(k+p+1)}$. Thus except for the factor $i^{p}$ the function that we get is real-valued. This function defines the so-called modified Bessel function of order $p$,

$$
I_{p}(x)=\sum_{k=0}^{\infty} \frac{(x / 2)^{2 k+p}}{k!\Gamma(k+p+1)} .
$$

(b) Verify that the modified Bessel function of order $p$ satisfies the modified Bessel's differential equation

$$
x^{2} y^{\prime \prime}+x y^{\prime}-\left(x^{2}+p^{2}\right) y=0 .
$$

(c) Plot the modified Bessel function of order 0 and note that it is positive and increasing for $x>0$.
30. Modified Bessel functions of the second kind.
(a) Show that $K_{p}(x)=\frac{\pi}{2 \sin p \pi}\left[I_{-p}(x)-I_{p}(x)\right]$ is also a solution of the modified Bessel's equation of Exercise 29. This function is called the modified Bessel function of the second kind (sometimes called of the third kind).
(b) Show that when $p$ is not an integer $I_{p}(x)$ and $K_{p}(x)$ are linearly independent.
(c) How would you construct $K_{p}(x)$ when $p$ is an integer?

## The Gamma Function

31. (a) Compute the numerical values of $\Gamma(1)$ and $\Gamma(2)$ starting from (13).
(b) Use (15) and the basic property of the gamma function to compute the values of $\Gamma\left(\frac{5}{2}\right)$ and $\Gamma\left(-\frac{3}{2}\right)$.
32. The reciprocal of the gamma function.
(a) Show that $1 / \Gamma(x) \rightarrow 0$ as $x$ approaches a negative integer or 0 . For this reason, we define $1 / \Gamma(x)=0$ for $x=0,-1,-2, \ldots$.
(b) Plot the graph of $1 / \Gamma(x)$ and show that it is continuous for all $x$.
33. For $x, y>0$,

$$
\frac{\Gamma(x) \Gamma(y)}{\Gamma(x+y)}=2 \int_{0}^{\pi / 2} \cos ^{2 x-1} \theta \sin ^{2 y-1} \theta d \theta .
$$

Derive this useful formula as follows.
(a) Make the change of variables $u^{2}=t$ in (13) and obtain

$$
\Gamma(x)=2 \int_{0}^{\infty} e^{-u^{2}} u^{2 x-1} d u, \quad x>0
$$

(b) Use (a) to show that for $x, y>0$,

$$
\Gamma(x) \Gamma(y)=4 \int_{0}^{\infty} \int_{0}^{\infty} e^{-\left(u^{2}+v^{2}\right)} u^{2 x-1} v^{2 y-1} d u d v
$$

(c) Change to polar coordinates in (b) ( $u=r \cos \theta, v=r \sin \theta, \quad d u d v=r d r d \theta$ ) and obtain that for $x, y>0$,

$$
\Gamma(x) \Gamma(y)=2 \Gamma(x+y) \int_{0}^{\pi / 2} \cos ^{2 x-1} \theta \sin ^{2 y-1} \theta d \theta
$$

[Hint: After you change coordinates, keep in mind (a) as you compute the integral in $r$.]
34. Use the result of Exercise 33 to obtain (15).
35. Derive the formula

$$
\frac{1}{\sqrt{\pi}} \int_{-\infty}^{\infty} e^{-u^{2}} d u=1
$$

[Hint: Use (15) and Exercise 33(a).]
In Exercises 36-39, use the result of Exercise 33 to compute the given integral.
36. $\int_{0}^{\pi / 2} \cos \theta \sin \theta d \theta$.
37. $\int_{0}^{\pi / 2} \cos ^{2} \theta \sin ^{3} \theta d \theta$.
38. $\int_{0}^{\pi / 2} \cos ^{5} \theta \sin ^{6} \theta d \theta$.
39. $\int_{0}^{\pi / 2} \cos ^{8} \theta d \theta$.

Use the result of Exercise 33 to establish the following Wallis's formulas.
40. $\int_{0}^{\pi / 2} \sin ^{2 k} \theta d \theta=\frac{\pi}{2} \frac{(2 k)!}{2^{2 k}(k!)^{2}}, \quad k=0,1,2, \ldots$.
41. $\int_{0}^{\pi / 2} \sin ^{2 k+1} \theta d \theta=\frac{2^{2 k}(k!)^{2}}{(2 k+1)!}, \quad k=0,1,2, \ldots$.
42. (a) Explain with the help of a graph why

$$
\int_{0}^{\pi / 2} \cos ^{2 k} \theta d \theta=\int_{0}^{\pi / 2} \sin ^{2 k} \theta d \theta
$$

and

$$
\int_{0}^{\pi / 2} \cos ^{2 k+1} \theta d \theta=\int_{0}^{\pi / 2} \sin ^{2 k+1} \theta d \theta
$$

(b) Use (a) and Exercises 40, and 41 to show that for $k=0,1,2, \ldots$,

$$
\int_{0}^{\pi / 2} \cos ^{2 k} \theta d \theta=\frac{\pi}{2} \frac{(2 k)!}{2^{2 k}(k!)^{2}} \quad \text { and } \quad \int_{0}^{\pi / 2} \cos ^{2 k+1} \theta d \theta=\frac{2^{2 k}(k!)^{2}}{(2 k+1)!}
$$

43. Derive the following formulas using Exercise 42: for $k=0,1,2, \ldots$

$$
\frac{1}{\pi} \int_{0}^{\pi} \cos ^{2 k} \theta d \theta=\frac{(2 k)!}{2^{2 k}(k!)^{2}} \quad \text { and } \quad \int_{0}^{\pi} \cos ^{2 k+1} \theta d \theta=0
$$

44. Show that (a) $\quad \Gamma\left(n+\frac{1}{2}\right)=\frac{(2 n)!}{2^{2 n} n!} \sqrt{\pi}$. (b) $\quad \Gamma\left(n+\frac{1}{2}+1\right)=\frac{(2 n+1)!}{2^{2 n+1} n!} \sqrt{\pi}$.
45. (a) Use the result of Exercise 33 to obtain that the arc length of the lemniscate $r^{2}=2 \cos 2 \theta$ is $2 \sqrt{2 \pi} \Gamma\left(\frac{1}{4}\right) / \Gamma\left(\frac{3}{4}\right)$. [Hint: Arc length in polar coordinates is $L=\int_{a}^{b} \sqrt{r^{2}+\left(\frac{d r}{d \theta}\right)^{2}} d \theta$.]
(b) Approximate the arc length in (a).
46. The beta function is defined for $r, s>0$ by

$$
\beta(r, s)=\int_{0}^{1} t^{r-1}(1-t)^{s-1} d t
$$

(a) Use the change of variables $t=\sin ^{2} \theta$ to obtain

$$
\beta(r, s)=2 \int_{0}^{\pi / 2} \cos ^{2 s-1} \theta \sin ^{2 r-1} \theta d \theta
$$

(b) From Exercise 33 conclude that

$$
\beta(r, s)=\frac{\Gamma(r) \Gamma(s)}{\Gamma(r+s)}
$$

### 4.8 Bessel Series Expansions

In this section we explore some recurrence relations, orthogonality properties of Bessel functions, and expansions of functions in Bessel series. Many of these properties are used in solving the boundary value problems occurring in this chapter and throughout this book.

## Identities Involving Bessel Functions

We start with two basic identities. For any $p \geq 0$,

$$
\frac{d}{d x}\left[x^{p} J_{p}(x)\right]=x^{p} J_{p-1}(x)
$$

$$
\frac{d}{d x}\left[x^{-p} J_{p}(x)\right]=-x^{-p} J_{p+1}(x)
$$

Note that for $p=0$, the second identity yields

$$
\frac{d}{d x}\left[J_{0}(x)\right]=-J_{1}(x)
$$

To prove (1) we recall the definition of $J_{p}$ from (7) of Section 4.7 and write

$$
\begin{aligned}
\frac{d}{d x}\left[x^{p} J_{p}(x)\right] & =\frac{d}{d x} \sum_{k=0}^{\infty} \frac{(-1)^{k} 2^{p}}{k!\Gamma(k+p+1)}\left(\frac{x}{2}\right)^{2 k+2 p} \\
& =\sum_{k=0}^{\infty} \frac{(-1)^{k} 2^{p}(k+p)}{k!\Gamma(k+p+1)}\left(\frac{x}{2}\right)^{2 k+2 p-1} \\
& =x^{p} \sum_{k=0}^{\infty} \frac{(-1)^{k}}{k!\Gamma(k+p)}\left(\frac{x}{2}\right)^{2 k+p-1} \\
& =x^{p} J_{p-1}(x)
\end{aligned}
$$

In the next to last step we used the basic property of the gamma function to write $\Gamma(k+p+1)=(p+k) \Gamma(p+k)$. The second identity is proved similarly (Exercise 1(a)).

Many other useful identities follow from (1) and (2). We list some of the most commonly used ones:

$$
\begin{gathered}
x J_{p}^{\prime}(x)+p J_{p}(x)=x J_{p-1}(x) \\
x J_{p}^{\prime}(x)-p J_{p}(x)=-x J_{p+1}(x) \\
J_{p-1}(x)-J_{p+1}(x)=2 J_{p}^{\prime}(x) \\
J_{p-1}(x)+J_{p+1}(x)=\frac{2 p}{x} J_{p}(x)
\end{gathered}
$$

(We note that the corresponding formulas for Bessel functions of the second kind also hold.) To prove (3), we expand the left side of (1) using the product rule and get

$$
x^{p} J_{p}^{\prime}(x)+p x^{p-1} J_{p}(x)=x^{p} J_{p-1}(x)
$$

Dividing through by $x^{p-1}$ gives (3). Identity (4) is proved similarly by starting with (2) and expanding using the product rule. Adding (3) and (4) and simplifying yields (5). Subtracting (4) from (3) and simplifying yields (6)

There are similar identities involving integrals of Bessel functions. For example, the identities

$$
\int x^{p+1} J_{p}(x) d x=x^{p+1} J_{p+1}(x)+C
$$

and

$$
\int x^{-p+1} J_{p}(x) d x=-x^{-p+1} J_{p-1}(x)+C
$$

follow easily by integrating both sides of (1) and (2) (Exercise 1).

## Orthogonality of Bessel Functions

To understand the orthogonality relations of Bessel functions, let us recall the familiar example of the functions $\sin n \pi x, n=1,2,3, \ldots$. We know that these functions are orthogonal on the interval $[0,1]$, in the sense that $\int_{0}^{1} \sin n \pi x \sin m \pi x d x=0$ if $n \neq m$. The key here is to note that the functions $\sin n \pi x$ are constructed from a single function, namely $\sin x$, and its positive zeros, namely $n \pi, n=1,2,3, \ldots$.

In constructing systems of orthogonal Bessel functions, we will proceed in a similar way by using a single Bessel function and its zeros. Fix an order $p \geq 0$, and consider the graph of $J_{p}(x)$ for $x>0$. Figure 1 shows typical graphs of Bessel functions.

![](./images/1c611338-958a-44f7-9d79-2dde87e6ac2a-58_468_1196_1190_559.jpg)
Figure 1 A Bessel function $J_{p}(x)$ has infinitely many positive zeros.

We see from Figure 1 that the Bessel function $J_{p}$ has infinitely many zeros on the positive axis $x>0$ (just like $\sin x$ ). This important fact is proved in the following section (see Exercises 14 and 35 for the cases $p=0, \pm 1, \pm 2, \ldots$, and $\frac{1}{2}$ ). We denote these zeros in ascending order

$$
0<\alpha_{p 1}<\alpha_{p 2}<\cdots<\alpha_{p j}<\cdots .
$$

Hence $\alpha_{p j}$ denotes the $j$ th positive zero of $J_{p}$. (Sometimes the notation $\alpha_{p, j}$ will be used.) Unlike the case of the sine function, where the zeros are easily determined by $n \pi$, there is no formula for the positive zeros of the Bessel

Let $a$ be a positive number. To generate orthogonal functions on the interval $[0, a]$ from $J_{p}$, we proceed as in the case of the sine function, using $\alpha_{p j}$, the zeros of the Bessel function. We obtain the functions

$$
J_{p}\left(\frac{\alpha_{p j}}{a} x\right), \quad j=1,2,3, \ldots
$$

The first four functions, corresponding to $p=0$, are shown in Figure 2.

It is interesting to note that all these functions are bounded by 1 and their number of zeros increase in the interval $(0,1)$. These properties are shared by other systems of orthogonal functions encountered earlier, in particular, the
functions. Since the numerical values of these zeros are very important in applications, they are found in most mathematical tables and computer systems. For later use, we list in Table 1 the first five positive zeros of $J_{0}$, $J_{1}$, and $J_{2}$.

| $j$ | 1 | 2 | 3 | 4 | 5 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $\alpha_{0 j}$ | 2.40483 | 5.52008 | 8.65373 | 11.7915 | 14.9309 |
| $\alpha_{1 j}$ | 3.83171 | 7.01559 | 10.1735 | 13.3237 | 16.4706 |
| $\alpha_{2 j}$ | 5.13562 | 8.41724 | 11.6198 | 14.796 | 18.9801 |

Table 1 Positive zeros of $J_{0}, J_{1}$, and $J_{2}$.

functions. Since the numerical values of these zeros are very important in applications, they are found in most mathematical tables and computer systems. For later use, we list in Table 1 the first five positive zeros of $J_{0}$,
$J_{1}$, and $J_{2}$. | $j$ | 1 | 2 | 3 | 4 | 5 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $\alpha_{0 j}$ | 2.40483 | 5.52008 | 8.65373 | 11.7915 | 14.9309 |
| $\alpha_{1 j}$ | 3.83171 | 7.01559 | 10.1735 | 13.3237 | 16.4706 |
| $\alpha_{2 j}$ | 5.13562 | 8.41724 | 11.6198 | 14.796 | 18.9801 | trigonometric functions.

![](./images/1c611338-958a-44f7-9d79-2dde87e6ac2a-59_481_1075_1262_502.jpg)
Figure 2 Orthogonal functions generated with $J_{0}(x): J_{0}\left(\alpha_{01} x\right), J_{0}\left(\alpha_{02} x\right), \ldots$.

To simplify the notation, we let

$$
\lambda_{p j}=\frac{\alpha_{p j}}{a} \quad j=1,2,3, \ldots
$$

So $\lambda_{p j}$ is the value of the $j$ th positive zero of $J_{p}$ scaled by a fixed factor $1 / a$. We are now in a position to state some fundamental identities.

THEOREM 1 ORTHOGONALITY OF BESSEL FUNCTIONS WITH RESPECT TO A WEIGHT

Fix $p \geq 0$ and $a>0$. Let $J_{p}\left(\lambda_{p j} x\right)(j=1,2, \ldots)$ be as in (9) and (10). Then

$$
\int_{0}^{a} J_{p}\left(\lambda_{p j} x\right) J_{p}\left(\lambda_{p k} x\right) x d x=0 \text { for } j \neq k
$$

and

$$
\int_{0}^{a} J_{p}^{2}\left(\lambda_{p j} x\right) x d x=\frac{a^{2}}{2} J_{p+1}^{2}\left(\alpha_{p j}\right) \text { for } j=1,2, \ldots
$$

Note that (12) involves $\lambda_{p j}$ and $\alpha_{p j}$. Property (11) is described by saying that the functions $J_{p}\left(\lambda_{p j} x\right), j=1,2, \ldots$ are orthogonal on the interval $[0, a]$ with respect to the weight $x$. The phrase "with respect to the weight $x$ " refers to the presence of the function $x$ in the integrand in (11). On the interval [ 0,1 ]-that is when $a=1$-formulas (11) and (12) take on a simpler form

$$
\begin{gathered}
\int_{0}^{1} J_{p}\left(\alpha_{p j} x\right) J_{p}\left(\alpha_{p k} x\right) x d x=0 \quad \text { for } j \neq k \\
\int_{0}^{1} J_{p}^{2}\left(\alpha_{p j} x\right) x d x=\frac{1}{2} J_{p+1}^{2}\left(\alpha_{p j}\right) \quad \text { for } j=1,2, \ldots
\end{gathered}
$$

The proof of (11) is found in the proof of Theorem 3. The proof of (12) is outlined in Exercise 36.

## Bessel Series and Bessel-Fourier Coefficients

Just as we used the functions $\sin n \pi x$ to expand functions in sine Fourier series, now we will see how we can expand functions using Bessel series. More precisely, a given function $f$ on the interval $[0, a]$ can be expressed as a series

$$
f(x)=\sum_{j=1}^{\infty} A_{j} J_{p}\left(\lambda_{p j} x\right)
$$

called the Bessel series of order $p$ of $f$. Putting aside questions of convergence, let us assume (15) is valid and proceed to find the coefficients in the series. Multiplying both sides of (15) by $J_{p}\left(\lambda_{p k} x\right) x$ and integrating term by term on the interval $[0, a]$ gives

$$
\int_{0}^{a} f(x) J_{p}\left(\lambda_{p k} x\right) x d x=\sum_{j=1}^{\infty} A_{j} \overbrace{\int_{0}^{a} J_{p}\left(\lambda_{p j} x\right) J_{p}\left(\lambda_{p k} x\right) x d x}^{=0 \text { except when } j=k}
$$

The orthogonality property (11) shows that all the terms on the right side of (16) are 0 except when $j=k$. Canceling the zero terms and using (12), we get

$$
A_{j}=\frac{\int_{0}^{a} f(x) J_{p}\left(\lambda_{p j} x\right) x d x}{\int_{0}^{a} J_{p}^{2}\left(\lambda_{p j} x\right) x d x}=\frac{2}{a^{2} J_{p+1}^{2}\left(\alpha_{p j}\right)} \int_{0}^{a} f(x) J_{p}\left(\lambda_{p j} x\right) x d x
$$

The number $A_{j}$ is called the $\boldsymbol{j}$ th Bessel-Fourier coefficient or simply the Bessel coefficient of the function $f$.

The next theorem gives conditions under which the Bessel series expansion of a function is valid. For the meaning of piecewise smooth, refer to Section 2.2.

THEOREM 2 BESSEL SERIES OF ORDER $p$

Note the similarity with Fourier series. At the points of discontinuity the Bessel series converges to the average of the function.

If $f$ is piecewise smooth on $[0, a]$, then $f$ has a Bessel series expansion of order $p$ on the interval $(0, a)$ given by

$$
f(x)=\sum_{j=1}^{\infty} A_{j} J_{p}\left(\lambda_{p j} x\right),
$$

where $\lambda_{p 1}, \lambda_{p 2}, \ldots$ are the scaled positive zeros of the Bessel function $J_{p}$ given by ( 10 ), and $A_{j}$ is given by ( 17 ). In the interval ( $0, a$ ), the series converges to $f(x)$ where $f$ is continuous and converges to the average $\frac{f(x+)+f(x-)}{2}$ at the points of discontinuity.

Before giving an example of a Bessel series, we make a useful remark about the notation. While the notation $\alpha_{p j}$ and $\lambda_{p j}$ is appropriate to denote the zeros and scaled zeros of the Bessel function of order $p$, it is a little cumbersome to work with. For this reason, when it is understood which order we are dealing with, and so there is no risk of confusion, we will drop the index $p$ and write $\alpha_{j}$ and $\lambda_{j}$ instead of $\alpha_{p j}$ and $\lambda_{p j}$.

EXAMPLE 1 A Bessel series on the interval [0,1]
Find the Bessel series expansion of order 0 of the function $f(x)=1,0<x<1$.
Solution Applying Theorem 2, we get

$$
f(x)=\sum_{j=1}^{\infty} A_{j} J_{0}\left(\alpha_{j} x\right)
$$

where $\alpha_{j}$ is the $j$ th positive zero of $J_{0}$, and

![](./images/1c611338-958a-44f7-9d79-2dde87e6ac2a-62_390_470_268_59.jpg)
Figure 3 Partial sums of the Bessel series.

$$
\begin{aligned}
A_{j} & =\frac{2}{J_{1}^{2}\left(\alpha_{j}\right)} \int_{0}^{1} f(x) J_{0}\left(\alpha_{j} x\right) x d x \\
& =\frac{2}{J_{1}^{2}\left(\alpha_{j}\right)} \int_{0}^{1} J_{0}\left(\alpha_{j} x\right) x d x \\
& =\frac{2}{\alpha_{j}^{2} J_{1}^{2}\left(\alpha_{j}\right)} \int_{0}^{\alpha_{j}} J_{0}(t) t d t \quad\left(t=\alpha_{j} x\right) \\
& \left.=\left.\frac{2}{\alpha_{j}^{2} J_{1}^{2}\left(\alpha_{j}\right)} J_{1}(t) t\right|_{0} ^{\alpha_{j}} \quad \text { (by (7) with } p=0\right) \\
& =\frac{2}{\alpha_{j} J_{1}\left(\alpha_{j}\right)}
\end{aligned}
$$

Theorem 2 asserts that the Bessel series converges to $f(x)$ at all points in the interval. Thus

$$
1=\sum_{j=1}^{\infty} \frac{2}{\alpha_{j} J_{1}\left(\alpha_{j}\right)} J_{0}\left(\alpha_{j} x\right) \quad 0<x<1 .
$$

| $j$ | 1 | 2 | 3 | 4 | 5 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $\alpha_{j}$ | 2.4048 | 5.5201 | 8.6537 | 11.7915 | 14.9309 |
| $J_{1}\left(\alpha_{j}\right)$ | .5191 | -.3403 | .2714 | -.2325 | .2065 |
| $\frac{2}{\alpha_{j} J_{1}\left(\alpha_{2}\right)}$ | 1.6020 | -1.0648 | .8514 | -.7295 | .6487 |

Table 2 Numerical data for Example 1

Using the numerical data provided by Tables 1 and 2, we can write explicitly the first few terms of the series:

$$
\begin{aligned}
1= & 1.6020 J_{0}(2.4048 x)-1.0648 J_{0}(5.5201 x)+.8514 J_{0}(8.6537 x) \\
& -.7295 J_{0}(11.7915 x)+.6487 J_{0}(14.9309 x)+\cdots
\end{aligned}
$$

It is worth noticing that the Bessel coefficients tend to 0 as $j \rightarrow \infty$. This is a property that holds in general.

Note that Theorem 2 tells us nothing about the behavior of the Bessel series at the endpoints of the interval. In this example, if we take $x=1$ in the series all the terms become zero, since we are evaluating $J_{0}$ at its zeros. This is also clear from the graphs of the partial sums in Figure 3. So, in this example, the Bessel series does not converge to the function at one of the endpoints.

## Parametric Form of Bessel's Equation

In the remainder of this section, we explore two important differential equations that are closely related to Bessel's equation.

THEOREM 3 PARAMETRIC FORM OF BESSEL'S EQUATION

The condition that $y(0)$ be finite is effectively a second boundary condition on $y$.

Let $p \geq 0, a>0$, and let $\alpha_{p j}$ denote the $j$ th positive zero of $J_{p}(x)$. For $j=1,2, \ldots$, the functions $J_{p}\left(\frac{\alpha_{p j}}{\alpha} x\right)$ are solutions of the parametric form of Bessel's equation of order $p$,

$$
x^{2} y^{\prime \prime}(x)+x y^{\prime}(x)+\left(\lambda^{2} x^{2}-p^{2}\right) y(x)=0
$$

together with the boundary conditions

$$
y(0) \text { finite, } y(a)=0
$$

when $\lambda=\lambda_{p j}=\frac{\alpha_{p j}}{a}$, and these are the only solutions of (18), aside from scalar multiples, with these properties. Moreover, these solutions satisfy (11) and (12) and so they are orthogonal on the interval $[0, a]$ with respect to the weight function $x$.

Proof We will make a change of variables in (18) and reduce it to Bessel's equation as follows. Let $u=\lambda x, d u=\lambda d x$, and let $y(x)=y\left(\frac{u}{\lambda}\right)=Y(u)$. From the chain rule, $y^{\prime}(x)=Y^{\prime}(u) \frac{d u}{d x}=\lambda Y^{\prime}(u)$, and, likewise, $y^{\prime \prime}(x)=\lambda^{2} Y^{\prime \prime}(u)$. Substituting in (18), we get Bessel's equation of order $p$ in $Y(u)$

$$
u^{2} Y^{\prime \prime}(u)+u Y^{\prime}(u)+\left(u^{2}-p^{2}\right) Y(u)=0
$$

Thus the general solution is

$$
Y(u)=c_{1} J_{p}(u)+c_{2} Y_{p}(u)=c_{1} J_{p}(\lambda x)+c_{2} Y_{p}(\lambda x)=y(x)
$$

For $y(0)$ to be finite, we must set $c_{2}=0$, because $Y_{p}$ blows up at 0 . So $y(x)= c_{1} J_{p}(\lambda x)$, and the boundary condition $y(a)=0$ holds (for $c_{1} \neq 0$ ) if and only if $\lambda a=\alpha_{p j}$. Hence,

$$
\lambda=\lambda_{p j}=\frac{\alpha_{p j}}{a}
$$

are the only positive values of $\lambda$ for which there are nontrivial solutions. Therefore, the solutions of (18) and (19) are as claimed.

We come now to the proof of (11). To simplify notation, let us write $\lambda_{j}$ for $\lambda_{p j}$, and $\phi_{j}(x)$ for $J_{p j}\left(\lambda_{p j} x\right)$. The goal is to show that for $j \neq k$

$$
\int_{0}^{a} \phi_{j}(x) \phi_{k}(x) x d x=0
$$

Let us write (18) in the form $\left(x y^{\prime}\right)^{\prime}=-\frac{\left(\lambda^{2} x^{2}-p^{2}\right)}{x} y$. Since the $\phi$ 's satisfy this equation with the corresponding $\lambda$ 's, we have

$$
\left(x \phi_{j}^{\prime}\right)^{\prime}=-\frac{\left(\lambda_{j}^{2} x^{2}-p^{2}\right)}{x} \phi_{j}
$$

and

$$
\left(x \phi_{k}^{\prime}\right)^{\prime}=-\frac{\left(\lambda_{k}^{2} x^{2}-p^{2}\right)}{x} \phi_{k}
$$

Multiplying the first equation by $\phi_{k}$ and the second one by $\phi_{j}$ and then subtracting the resulting equations, we get, after simplifying,

$$
\left(\lambda_{k}^{2}-\lambda_{j}^{2}\right) \phi_{j} \phi_{k} x=\phi_{k}\left(x \phi_{j}^{\prime}\right)^{\prime}-\phi_{j}\left(x \phi_{k}^{\prime}\right)^{\prime} .
$$

Note that

$$
\phi_{k}\left(x \phi_{j}^{\prime}\right)^{\prime}-\phi_{j}\left(x \phi_{k}^{\prime}\right)^{\prime}=\frac{d}{d x}\left[\phi_{k} x \phi_{j}^{\prime}-\phi_{j} x \phi_{k}^{\prime}\right]
$$

Hence

$$
\left(\lambda_{k}^{2}-\lambda_{j}^{2}\right) \int_{0}^{a} \phi_{j}(x) \phi_{k}(x) x d x=\phi_{k} x \phi_{j}^{\prime}-\left.\phi_{j} x \phi_{k}^{\prime}\right|_{0} ^{a}=0
$$

because $\phi_{j}(a)=\phi_{k}(a)=0$, and the desired result follows, since $\lambda_{k}^{2}-\lambda_{j}^{2} \neq 0$. For the proof of (12), see Exercise 36. $\square$

Our last example is a differential equation that gives rise to yet another important family of functions.

## EXAMPLE 2 Spherical Bessel functions

The equation

$$
x^{2} y^{\prime \prime}+2 x y^{\prime}+\left(k x^{2}-n(n+1)\right) y=0, \quad 0<x<a, \quad y(a)=0,
$$

arises in many important applications in Chapter 5. In this equation, $k$ is a nonnegative real number and $n=0,1,2, \ldots$. We are seeking bounded solutions in the interval $0 \leq x \leq a$. You can check that the substitution

$$
y=x^{-1 / 2} w
$$

transforms (20) into the following parametric form of Bessel's equation:

$$
x^{2} w^{\prime \prime}+x w^{\prime}+\left(k x^{2}-\left(n+\frac{1}{2}\right)^{2}\right) w=0, \quad w(a)=0
$$

(Exercise 37). We know from Theorem 3 (with $p=n+1 / 2$ ) that bounded solutions arise only when

$$
k=\lambda^{2}
$$

and

$$
\lambda=\lambda_{n, j}=\frac{\alpha_{n+1 / 2, j}}{a},
$$

where $\alpha_{n+1 / 2, j}$ denotes the $j$ th positive zero of $J_{n+\frac{1}{2}}$. The corresponding solutions are scalar multiples of

$$
w_{n, j}(x)=J_{n+\frac{1}{2}}\left(\lambda_{n, j} x\right), \quad n=0,1,2, \ldots, \quad j=1,2, \ldots
$$

Hence, using (21), it follows that the solutions $y_{n j}$ of (20) are scalar multiples of

Figure 4 Spherical Bessel functions, $j_{0}, j_{1}, j_{2}, j_{3}$.

$$
x^{-1 / 2} J_{n+\frac{1}{2}}\left(\lambda_{n}, j x\right), \quad n=0,1,2, \ldots, \quad j=1,2, \ldots .
$$

It is customary to express the solutions in terms of the spherical Bessel functions of the first kind (see Figure 4):

$$
j_{n}(x)=\left(\frac{\pi}{2 x}\right)^{1 / 2} J_{n+\frac{1}{2}}(x), \quad n=0,1,2, \ldots
$$

Choosing a specific multiple of the functions in (22), we obtain the solutions of (20) as the spherical Bessel functions:

$$
y_{n, j}(x)=j_{n}\left(\lambda_{n, j} x\right), \quad n=0,1,2, \ldots, \quad j=1,2, \ldots .
$$ $\square$

In the exercises you are asked to study the spherical Bessel functions, including their orthogonality. In most cases, the results are simple consequences of properties of Bessel functions and (23).

## Exercises 4.8

1. (a) Supply the details of the proof of (2), (7), and (8). [Hint: To prove (2), show that the derivative is $\sum_{k=1}^{\infty} \frac{(-1)^{k} 2 k}{k!\Gamma(k+p+1) 2^{2 k+p}} x^{2 k-1}$. Then change $k$ to $k+1$ to start the sum at 0 .]
(b) Supply the details of the proof of (4), (5), and (6).
2. (a) On the graphs of $J_{0}$ and $J_{1}$ in Figure 1, Section 4.7, note that the maxima and minima of $J_{0}$ occur at the zeros of $J_{1}$. Prove this fact.
(b) Show that the maximum and minimum values of $J_{p}$ occur when

$$
x=\frac{p J_{p}(x)}{J_{p+1}(x)} \quad \text { or } \quad x=\frac{p J_{p}(x)}{J_{p-1}(x)} \quad \text { or } \quad J_{p-1}(x)=J_{p+1}(x) .
$$

(c) Illustrate (b) graphically when $p=2$.
(d) Show that at the zeros of $J_{p}, J_{p-1}$ and $J_{p+1}$ have equal absolute values but opposite signs.

In Exercises 3-10, evaluate the given integral.
3. $\int x J_{0}(x) d x$.
4. $\int x^{4} J_{3}(x) d x$.
5. $\int J_{1}(x) d x$.
6. $\int x^{-2} J_{3}(x) d x$.
7. $\int x^{3} J_{2}(x) d x$.
8. $\int x^{3} J_{0}(x) d x$.
9. $\int J_{3}(x) d x$.
10. $\int_{0}^{\infty} J_{1}(x)\left[J_{0}(x)\right]^{n} d x$.
[Hint: Let $u=J_{0}(x)$.]
11. Use (2) and Example 1 of Section 4.7 to derive the formula

$$
J_{3 / 2}(x)=\sqrt{\frac{2}{\pi x}}\left[\frac{\sin x}{x}-\cos x\right]
$$

12. Use (2) and Exercise 11 to derive

$$
J_{5 / 2}(x)=\sqrt{\frac{2}{\pi x}}\left[\left(\frac{3}{x^{2}}-1\right) \sin x-\frac{3}{x} \cos x\right] .
$$

13. Express $J_{5}$ in terms of $J_{0}$ and $J_{1}$.
14. Use the explicit formula for $J_{1 / 2}$ given in Example 1 of Section 4.7 to show that $J_{1 / 2}$ has infinitely many positive zeros in the interval $0<x<\infty$. What are these zeros?
15. (a) Plot the functions $\frac{\sin x}{x}$ and $\cos x$ on the same graph to illustrate the fact that they intersect at infinitely many points. Conclude that the function $J_{3 / 2}(x)$ has infinitely many zeros in ( $0, \infty$ ).
(b) Approximate the first three roots of the equation $\frac{\sin x}{x}=\cos x$.
16. (a) Let $0<\alpha_{p 1}<\alpha_{p 2}<\cdots<\alpha_{p j}<\cdots$ denote the positive zeros of $J_{p}$. How many roots does the function $J_{p}\left(\frac{\alpha_{p j}}{a} x\right)$ have in the interval $0<x<a$ ? Justify your answer.
(b) Illustrate your answer graphically with $p=2, a=1$, and $j=5$.
17. Let $0<c<1$, and let

$$
f(x)= \begin{cases}1 & \text { if } 0<x<c \\ 0 & \text { if } c<x<1\end{cases}
$$

(a) Derive the Bessel series of order 0 of $f$

$$
\sum_{j=1}^{\infty} \frac{2 c J_{1}\left(c \alpha_{j}\right)}{\alpha_{j} J_{1}\left(\alpha_{j}\right)^{2}} J_{0}\left(\alpha_{j} x\right), \quad 0<x<1
$$

(b) Discuss the convergence of the series in the interval $0<x<1$.
(c) Take $c=\frac{1}{2}$. Investigate the convergence of the series at $x=0$ and $x=1$ numerically. Does the series seem to converge at one or both points? To what values? (Note that convergence at these points is not covered by Theorem 2.)
18. Take $a=\frac{1}{3}$ in Exercise 17 and write explicitly the first five terms of the series in this case. Plot several partial sums and describe the behavior at and around the point $x=\frac{1}{3}$. Observe how the partial sums overshoot their limiting values regardless of the increase in the number of terms in the approximating partial sums. This illustrates the Gibbs phenomenon at a point of discontinuity for Bessel series expansions.
19. (a) Obtain the Bessel series expansion

$$
x^{4}=2 \sum_{j=1}^{\infty} \frac{1}{\alpha_{j} J_{5}\left(\alpha_{j}\right)} J_{4}\left(\alpha_{j} x\right), \quad 0<x<1
$$

where the $\alpha_{j}$ 's are the positive zeros of $J_{4}$.
(b) Plot some partial sums and discuss their behavior on the interval $0<x<1$.
20. Bessel series of order $m$. Fix a number $m \geq 0$ and let $0<\alpha_{1}<\alpha_{2}< \ldots<\alpha_{j}<\ldots$ denote the sequence of positive zeros of $J_{m}$. Obtain the Bessel series expansion

$$
x^{m}=2 \sum_{j=1}^{\infty} \frac{1}{\alpha_{j} J_{m+1}\left(\alpha_{j}\right)} J_{m}\left(\alpha_{j} x\right), \quad 0<x<1
$$

21. Refer to Exercise 20.
(a) Take $m=\frac{1}{2}$, and determine the exact values of the $\alpha_{j}$ 's in this case? [Hint: Example 1 of Section 4.7.]
(b) Compute explicitly the coefficients in the Bessel series expansion of $f(x)=\sqrt{x}$, $0<x<1$.
(c) Recall the formula for $J_{\frac{1}{2}}$ in terms of $\sin x$ and show that the expansion in (b) is really a sine Fourier series expansion of $x$.
(d) Plot some partial sums of the Bessel series and discuss the convergence on the interval $0<x<1$.
22. Study the behavior of the partial sums of the Bessel series in Exercise 20 when $m=\frac{3}{2}$. What do they converge to in the interval $0<x<1$ ?
In Exercises 23-30, approximate the given function by a Bessel series of the given order $p$. Plot several partial sums of the series and discuss their convergence on the given interval.
23. $f(x)=x^{2} ; 0<x<1 ; p=2$.
24. $f(x)=x^{3} ; 0<x<1 ; p=3$.
25. $f(x)= \begin{cases}0 & \text { if } 0<x<\frac{1}{2}, \\ \frac{1}{x} & \text { if } \frac{1}{2}<x<1 ;\end{cases}$
26. $f(x)=x^{2}, 0<x<1, p=0$.
$p=1$.
27. $f(x)= \begin{cases}0 & \text { if } 0<x<\frac{1}{2}, \\ \frac{1}{x^{2}} & \text { if } \frac{1}{2}<x<1 ;\end{cases}$
28. $f(x)= \begin{cases}0 & \text { if } 0<x<\frac{1}{30}, \\ \frac{1}{x^{3}} & \text { if } \frac{1}{30}<x<1 ;\end{cases}$
$p=2$ 。 $p=3$.
29. $f(x)=1 ; 0<x<2 ; p=1$.
30. $f(x)=J_{0}(x) ; 0<x<\alpha_{01} ; p=0$.

In Exercises 31-34, find all $\lambda>0$ for which the given parametric form of Bessel's equation has a solution that is finite at $x=0$ and satisfies the given boundary condition.
31. $x^{2} y^{\prime \prime}(x)+x y^{\prime}(x)+\left(\lambda^{2} x^{2}-1\right) y(x)=0, \quad y(1)=0$.
32. $x^{2} y^{\prime \prime}(x)+x y^{\prime}(x)+\lambda^{2} x^{2} y(x)=0, \quad y(2)=0$.
33. $x^{2} y^{\prime \prime}(x)+x y^{\prime}(x)+\left(\lambda^{2} x^{2}-\frac{1}{4}\right) y(x)=0, \quad y(\pi)=0$.
34. $x^{2} y^{\prime \prime}(x)+x y^{\prime}(x)+\left(\lambda^{2} x^{2}-1\right) y(x)=0, \quad y\left(\frac{\pi}{2}\right)=0$.
35. Project Problem: Zeros of $\boldsymbol{J}_{\boldsymbol{n}}$. We will prove that the positive zeros of $J_{n}(x)(n=0 \pm 1, \pm 2, \ldots)$ form an increasing sequence

$$
0<\alpha_{n 1}<\alpha_{n 2}<\cdots<\alpha_{n k}<\cdots \rightarrow \infty
$$

Parts (a)-(g) deal with the case $n=0$.
(a) Plot the graph of $J_{0}(x)$ and note that there are infinitely many positive zeros that we will denote in ascending order by $0<\alpha_{1}<\alpha_{2}<\alpha_{3}<\ldots$
(b) Show that the substitution $y(x)=\frac{1}{\sqrt{x}} u(x)$ transforms Bessel's equation of order 0 into

$$
u^{\prime \prime}+\left(1+\frac{1}{4 x^{2}}\right) u=0
$$

Conclude that $u(x)=\sqrt{x} J_{0}(x)$ is a solution of this differential equation.
(c) Let $v(x)=\sin x$. Check that

$$
-\left(u^{\prime \prime}+u\right) v(x)=\frac{d}{d x}\left(u v^{\prime}-u^{\prime} v\right)
$$

(d) Using (b), show that $-\left(u^{\prime \prime}+u\right)=\frac{u}{4 x^{2}}$.
(e) Show that $\int \frac{u(x) v(x)}{4 x^{2}} d x=u v^{\prime}-u^{\prime} v+C$ and hence

$$
\int_{2 k \pi}^{(2 k+1) \pi} \frac{u(x) \sin x}{4 x^{2}} d x=-[u(2 k \pi)+u(2 k \pi+\pi)]
$$

(f) Conclude from (e) that $u(x)$ has at least one zero in $[2 k \pi,(2 k+1) \pi]$. [Hint: Assume the contrary, say $u(x)>0$ for all $x$ in the interval, and get a contradiction by studying the signs of the terms on both sides of the last equality in (e).]
(g) Conclude that $J_{0}(x)$ has infinitely many positive zeros.
(h) Suppose that $f$ and $g$ are differentiable functions such that $\frac{d}{d x} f(x)=g(x)$. Show that between any two zeros of $f$ there is at least one zero of $g$.
(i) Use (2) with $p=0$ to show that $J_{1}$ has infinitely many zeros that tend to $\infty$.
(j) Use (2) and induction to show that $J_{n}(n>0)$ has infinitely many zeros that tend to $\infty$. Prove this result for all integers $n$.
36. Project Problem: A proof of (12). Let $0<\alpha_{1}<\alpha_{2}<\cdots<\alpha_{k}<\cdots$ denote the sequence of zeros of $J_{p}$ in ( $0, \infty$ ), and let $\lambda_{k}=\frac{\alpha_{k}}{a}$.
(a) Rewrite (18) as

$$
\left(x y^{\prime}\right)^{\prime}+\left(\lambda^{2} x-\frac{p^{2}}{x}\right) y=0, \quad y(a)=0
$$

Multiply both sides of the equation by $x y^{\prime}$ and put it in the form

$$
\left[\left(x y^{\prime}\right)^{2}\right]^{\prime}+\left(\lambda^{2} x^{2}-p^{2}\right)\left(y^{2}\right)^{\prime}=0
$$

(b) Take $y=J_{p}\left(\lambda_{k} x\right)$ and $\lambda=\lambda_{k}$, integrate the equation in (a) over $0<x<a$, and obtain

$$
\left[a y^{\prime}(a)\right]^{2}+\left(\lambda^{2} a^{2}-p^{2}\right) y(a)^{2}-2 \lambda^{2} \int_{0}^{a} y(x)^{2} x d x=0
$$

[Hint: Use integration by parts on the second term in (a). Justify the equality $p y(0)=0$.]
(c) For $y=J_{p}\left(\lambda_{k} x\right)$ and $\lambda=\lambda_{k}$, justify the equality $y(a)=0$, and get

$$
\left[y^{\prime}(a)\right]^{2}=\frac{2 \lambda^{2}}{a^{2}} \int_{0}^{a} x[y(x)]^{2} d x
$$

(d) For $y=J_{p}\left(\lambda_{k} x\right)$, use (4) to show that $y^{\prime}(a)=-\lambda_{k} J_{p+1}\left(\alpha_{k}\right)$. Derive (12) from (c).

## Spherical Bessel Functions

37. Use (21) to transform (20) into one of the equations of the form (18).
38. Use (23) and explicit formulas for the Bessel functions to show that

$$
\begin{gathered}
j_{0}(x)=\frac{\sin x}{x} \\
j_{1}(x)=\frac{\sin x-x \cos x}{x^{2}} \\
j_{2}(x)=\frac{\left(3-x^{2}\right) \sin x-3 x \cos x}{x^{3}} .
\end{gathered}
$$

[Hint: See Exercises 11 and 12.]
In Exercises 39-42, derive the given recurrence relation for the spherical Bessel functions. [Hint: Use (23) and the corresponding formulas for the Bessel functions.]
39. $\frac{d}{d x}\left[x^{n+1} j_{n}(x)\right]=x^{n+1} j_{n-1}(x)$.
40. $\frac{d}{d x}\left[x^{-n} j_{n}(x)\right]=-x^{-n} j_{n+1}(x)$.
41. $\int x^{n+2} j_{n}(x) d x=x^{n+2} j_{n+1}(x)+C$.
42. $\int x^{-n+1} j_{n}(x) d x=-x^{-n+1} j_{n-1}(x)+C$.
43. Recurrence relations. Use the results of Exercises 39 and 40 to obtain that

$$
j_{n-1}(x)+j_{n+1}(x)=\frac{2 n+1}{x} j_{n}(x)
$$

and

$$
n j_{n-1}(x)-(n+1) j_{n+1}(x)=(2 n+1) j_{n}^{\prime}(x) .
$$

44. Use the results of Exercises 43 and 38 to obtain that

$$
j_{3}(x)=\frac{\left(15-6 x^{2}\right) \sin x-\left(15 x-x^{3}\right) \cos x}{x^{4}} .
$$

45. Orthogonality of the spherical Bessel functions. Use (11) and (12) to show that

$$
\int_{0}^{a} j_{n}\left(\lambda_{n, j} x\right) j_{n}\left(\lambda_{n, j^{\prime}} x\right) x^{2} d x=0 \quad \text { for } j \neq j^{\prime}
$$

and

$$
\int_{0}^{a} j_{n}^{2}\left(\lambda_{n, j} x\right) x^{2} d x=\frac{a^{3}}{2} j_{n+1}^{2}\left(\alpha_{n+\frac{1}{2}, j}\right)
$$

where $\alpha_{n+\frac{1}{2}, j}$ is the $j$ th positive zero of $j_{n}$ (equivalently, of $J_{n+\frac{1}{2}}$ ). Hence the spherical Bessel functions are orthogonal on the interval $[0, a]$ with respect to the weight function $x^{2}$.

### 4.9 Integral Formulas and Asymptotics for Bessel Functions

Bessel functions are widely used in mathematics, engineering, and physics, because they are at the heart of so many important applications. It is thus essential to get familiarized with their basic properties. To gain insight into the theory of Bessel functions we will represent them by formulas and integrals involving more familiar functions, such as the cosine and sine functions. Let us start by deriving an important integral representation for Bessel functions and then use it to show a surprising connection with Fourier series.

## THEOREM 1 INTEGRAL REPRESENTATION

 □Let $n=0, \pm 1, \pm 2, \ldots$. Then for all $x$, we have

$$
J_{n}(x)=\frac{1}{\pi} \int_{0}^{\pi} \cos (n \theta-x \sin \theta) d \theta
$$

Proof We do the case $n \geq 0$, and in the exercises you can show that this case implies the formula when $n<0$. Let $x$ and $\theta$ be real numbers and set $\zeta=e^{i \theta}$. For all $\theta$, we have $|\zeta|=\left|e^{i \theta}\right|=1$. So $\zeta$ lies on the unit circle. The function $e^{-\frac{x}{2 \zeta}}$ has a series expansion about 0 in $-\frac{x}{2 \zeta}$, which is obtained by plugging $-\frac{x}{2 \zeta}$ in place of $z$ in the series expansion of $e^{z}=\sum_{k=0}^{\infty} \frac{z^{k}}{k!}$. Thus

$$
e^{\frac{x}{2}\left(\zeta-\frac{1}{\zeta}\right)}=e^{\frac{x}{2} \zeta} e^{-\frac{x}{2 \zeta}}=e^{\frac{x}{2} \zeta} \sum_{k=0}^{\infty} \frac{1}{k!}\left(-\frac{x}{2 \zeta}\right)^{k}=\sum_{k=0}^{\infty} \frac{(-1)^{k}}{k!2^{k}} x^{k} \frac{e^{\frac{x}{2} \zeta}}{\zeta^{k}} .
$$

For fixed $x$, the series is absolutely convergent for all $\theta$ (remember, $\zeta=e^{i \theta}$ ). So we can multiply both sides by $\zeta^{-n}$, integrate term by term, and get

$$
\frac{1}{2 \pi} \int_{0}^{2 \pi} e^{\frac{x}{2}\left(\zeta-\frac{1}{\zeta}\right)} \zeta^{-n} d \theta=\sum_{k=0}^{\infty} \frac{(-1)^{k}}{k!2^{k}} x^{k} \frac{1}{2 \pi} \int_{0}^{2 \pi} \frac{e^{\frac{x}{2} \zeta}}{\zeta^{k+n}} d \theta
$$

We claim that, for $n \geq 0$, the left side is equal to $\frac{1}{\pi} \int_{0}^{\pi} \cos (n \theta-x \sin \theta) d \theta$, and the right side is equal to $J_{n}(x)$. Obviously, we will be done once we prove these claims. We need the identities

$$
\zeta-\frac{1}{\zeta}=e^{i \theta}-e^{-i \theta}=2 i \sin \theta \quad \text { and } \quad \zeta^{-n}=e^{-i n \theta}
$$

Proof of first claim: For any integer $n$, write

$$
e^{\frac{x}{2}\left(\zeta-\frac{1}{\zeta}\right)} \zeta^{-n}=e^{i(x \sin \theta-n \theta)}=\cos (x \sin \theta-n \theta)+i \sin (x \sin \theta-n \theta) .
$$

The terms on the right side are $2 \pi$-periodic functions of $\theta$; moreover, the first one is even and the second one is odd. Using Theorem 1, Section 2.1, we obtain

$$
\begin{aligned}
& \frac{1}{2 \pi} \int_{0}^{2 \pi} e^{\frac{x}{2}\left(\zeta-\frac{1}{\zeta}\right)} \zeta^{-n} d \theta \\
& \quad=\frac{1}{2 \pi} \int_{-\pi}^{\pi} \cos (x \sin \theta-n \theta) d \theta+i \overbrace{\frac{1}{2 \pi} \int_{-\pi}^{\pi} \sin (x \sin \theta-n \theta) d \theta}^{=0} \\
& \quad=\frac{1}{\pi} \int_{0}^{\pi} \cos (x \sin \theta-n \theta) d \theta
\end{aligned}
$$

Proof of second claim: Take $n \geq 0$. It is enough to show that

$$
\frac{1}{2 \pi} \int_{0}^{2 \pi} \frac{e^{\frac{x}{2} \zeta}}{\zeta^{k+n}} d \theta=\left(\frac{x}{2}\right)^{k+n} \frac{1}{(k+n)!}
$$

Then substituting this value of the integral into the right side of (2), we obtain the series expansion for $J_{n}(x)$ (see the formula following (7), Section 4.7), which would complete the proof. To prove (3), we use the Taylor series expansion of $e^{z}$, as we did before, and integrate term by term (recall $\zeta=e^{i \theta}$ ):

$$
\begin{aligned}
\frac{e^{\frac{x}{2} \zeta}}{\zeta^{k+n}} & =\zeta^{-(k+n)} \sum_{j=0}^{\infty} \frac{1}{j!}\left(\frac{x}{2} \zeta\right)^{j}=\sum_{j=0}^{\infty} \frac{1}{j!}\left(\frac{x}{2}\right)^{j} \zeta^{j-k-n} \\
& =\sum_{j=0}^{\infty} \frac{1}{j!}\left(\frac{x}{2}\right)^{j} e^{i(j-k-n) \theta} ; \\
\frac{1}{2 \pi} \int_{0}^{2 \pi} \frac{e^{\frac{x}{2} \zeta}}{\zeta^{k+n}} d \theta & =\sum_{j=0}^{\infty} \frac{1}{j!}\left(\frac{x}{2}\right)^{j} \frac{1}{2 \pi} \int_{0}^{2 \pi} e^{i(j-k-n) \theta} d \theta .
\end{aligned}
$$

But $\frac{1}{2 \pi} \int_{0}^{2 \pi} e^{i(j-k-n) \theta} d \theta=0$ if $j-k-n \neq 0$ and 1 if $j=k+n$ (see Section 2.6); so only one term of the series is nonzero (when $j=k+n$ ) and (3) follows.

## EXAMPLE $1 \quad J_{0}$ is bounded by 1

Show that for all $x,\left|J_{0}(x)\right| \leq 1$. (Since $J_{0}(0)=1$, this inequality is best possible.)
Solution Using (1) with $n=0$, we have

$$
\left|J_{0}(x)\right|=\frac{1}{\pi}\left|\int_{0}^{\pi} \cos (x \sin \theta) d \theta\right| \leq \frac{1}{\pi} \int_{0}^{\pi} \overbrace{|\cos (x \sin \theta)|}^{\leq 1} d \theta \leq \frac{1}{\pi} \int_{0}^{\pi} d \theta=1
$$

We now explore a surprising connection with Fourier series. Consider the function $f(\theta)=e^{\frac{x}{2}\left(\zeta-\frac{1}{\zeta}\right)}=e^{i x \sin \theta}$, which appears in the integral in (2) (recall $\zeta=e^{i \theta}$ ). Express the complex exponential in terms of the cosine and sine functions, as we did previously in the proof of Theorem 1, and get

$$
f(\theta)=\cos (x \sin \theta)+i \sin (x \sin \theta)
$$

For fixed $x$, the real and imaginary parts of $f(\theta)$ are $2 \pi$-periodic and smooth. Thus $f$ has a Fourier series representation, with complex Fourier coefficients

$$
c_{n}=\frac{1}{2 \pi} \int_{0}^{2 \pi} f(\theta) e^{-i n \theta} d \theta
$$

This integral is precisely the integral that appears in (1) (see the first claim in the proof of Theorem 1). So, from Theorem 1,

$$
J_{n}(x)=\frac{1}{2 \pi} \int_{0}^{2 \pi} f(\theta) e^{-i n \theta} d \theta=c_{n}
$$

Substituting into the Fourier series representation of $f(\theta)=\sum_{n=-\infty}^{\infty} c_{n} e^{i n \theta}$ (Theorem 1, Section 2.6), we obtain the following interesting result, which provides a Fourier series generating the Bessel functions.

THEOREM 2 FOURIER SERIES GENERATING BESSEL FUNCTIONS

For all $x$ and all $\theta$, we have

$$
e^{i x \sin \theta}=\sum_{n=-\infty}^{\infty} J_{n}(x) e^{i n \theta}
$$

Formula (4) has many interesting consequences that follow by simply evaluating the series at particular values of $\theta$ (see the exercises). We illustrate with an example.

![](./images/1c611338-958a-44f7-9d79-2dde87e6ac2a-72_329_470_622_63.jpg)
Figure 1 Approximation of $\cos x$ by the partial sum $J_{0}(x)+2\left(-J_{2}(x)+J_{4}(x)-\right. J_{6}(x)$ ). The graphs are almost indistinguishable on the interval $[-2 \pi, 2 \pi]$.

EXAMPLE 2 Bessel functions related to $\cos x$ and $\sin x$
Derive the following identities: For all $x$,

$$
\begin{gathered}
\cos x=J_{0}(x)+2 \sum_{n=1}^{\infty}(-1)^{n} J_{2 n}(x) \\
\sin x=2 \sum_{n=0}^{\infty}(-1)^{n} J_{2 n+1}(x)
\end{gathered}
$$

Solution Put $\theta=\frac{\pi}{2}$ in (4). Then for all $x$,

$$
\begin{aligned}
e^{i x \sin \frac{\pi}{2}} & =\sum_{n=-\infty}^{\infty} J_{n}(x) e^{i n \frac{\pi}{2}} ; \\
\cos x+i \sin x & =\sum_{n=-\infty}^{\infty} J_{n}(x)\left(\cos \left(\frac{n \pi}{2}\right)+i \sin \left(\frac{n \pi}{2}\right)\right) .
\end{aligned}
$$

Taking real parts, then using that $\cos \frac{n \pi}{2}=0$ if $n$ is odd and $(-1)^{m}$ if $n=2 m$ and that $J_{-2 n}(x)=(-1)^{2 n} J_{2 n}(x)=J_{2 n}(x)$, we obtain

$$
\begin{aligned}
\cos x & =\sum_{n=-\infty}^{\infty} \cos \left(\frac{n \pi}{2}\right) J_{n}(x) \\
& =J_{0}(x)+\sum_{n=1}^{\infty}(-1)^{n} J_{2 n}(x)+\sum_{n=-1}^{-\infty}(-1)^{n} J_{2 n}(x) \\
& =J_{0}(x)+\sum_{n=1}^{\infty}(-1)^{n}\left(J_{2 n}(x)+J_{-2 n}(x)\right)=J_{0}(x)+2 \sum_{n=1}^{\infty}(-1)^{n} J_{2 n}(x) .
\end{aligned}
$$

This proves the identity with the cosine. The one with the sine follows similarly and is left to the exercises. The series is illustrated in Figure 1.

## Asymptotics for Bessel Functions

Looking at the graph of a Bessel function, say $J_{0}(x)$, we notice two features: As $x$ tends to $\infty$, the graph oscillates like a cosine or sine wave and its amplitude decays like a negative power of $x$. In Figure 2, we show the graphs of $J_{0}(x)$ and $\sqrt{\frac{2}{\pi x}} \cos \left(x-\frac{\pi}{4}\right)$. The graphs are almost identical for large $x$. In fact, a more delicate analysis reveals that the difference between them is tending to 0 at the same rate as $1 / x^{3 / 2}$. We write $J_{0}(x) \sim \sqrt{\frac{2}{\pi x}} \cos \left(x-\frac{\pi}{4}\right)$ or, more precisely,

$$
J_{0}(x) \sim \sqrt{\frac{2}{\pi x}} \cos \left(x-\frac{\pi}{4}\right)+\mathcal{O}\left(\frac{1}{x^{3 / 2}}\right),
$$

and say that $J_{0}(x)$ is asymptotic to $\sqrt{\frac{2}{\pi x}} \cos \left(x-\frac{\pi}{4}\right)$ plus a big oh of $1 / x^{3 / 2}$. The expression "big on of $1 / x^{3 / 2}$ " means that there is a constant $C>0$ such

THEOREM 3 ASYMPTOTIC FORMULA

## LEMMA 1 METHOD OF STATIONARY PHASE

that $\left|J_{0}(x)-\sqrt{\frac{2}{\pi x}} \cos \left(x-\frac{\pi}{4}\right)\right| \leq C / x^{3 / 2}$ for all large $x$. Thus the error in the approximation tends to zero like $1 / x^{3 / 2}$. This asymptotic formula has many important consequences. For example, it follows immediately from it that $J_{0}(x)$ has infinitely many zeros and that these zeros are approximately the same as the zeros of $\cos \left(x-\frac{\pi}{4}\right)$ (Figure 2).

Figure 2 The asymptotic formula says that $J_{0}(x) \sim \sqrt{\frac{2}{\pi x}} \cos \left(x-\frac{\pi}{4}\right)$ with an error of the order $1 / x^{3 / 2}$. See how well the zeros of $J_{0}(x)$ are approximated by the zeros of $\cos \left(x-\frac{\pi}{4}\right)$, which are $\frac{3 \pi}{4} \approx 2.35619, \frac{7 \pi}{4} \approx 5.49779$, $\frac{11 \pi}{4} \approx 8.63938, \ldots$. Compare with the table of zeros of $J_{0}(x)$ in the previous section.
![](./images/1c611338-958a-44f7-9d79-2dde87e6ac2a-73_480_865_504_625.jpg)

In general, we have the following asymptotic formula.
Let $n \geq 0$ be an integer. Then for all large $x$, we have

$$
J_{n}(x) \sim \sqrt{\frac{2}{\pi x}} \cos \left(x-\frac{\pi}{4}-\frac{n \pi}{2}\right)+\mathcal{O}\left(\frac{1}{x^{3 / 2}}\right)
$$

where the big oh notation means that the approximation is of the order $\frac{1}{x^{3 / 2}}$.
Asymptotic formulas can be derived using the method of stationary phase, from which we quote the following result.

Suppose that $f(t)$ is a real-valued function with a Taylor series centered at $t_{0}$ in the interval $[a, b]$, such that $f^{\prime}\left(t_{0}\right)=0, f^{\prime}(t) \neq 0$ for all $t \neq t_{0}$, and $f^{\prime \prime}\left(t_{0}\right) \neq 0$. Let $g(t)$ be an arbitrary smooth complex-valued function on $[a, b]$. Then for large $x$
(6)

$$
\int_{a}^{b} e^{i x f(t)} g(t) d t \sim \sqrt{\frac{2 \pi}{x}} g\left(t_{0}\right) \frac{e^{i\left(x f\left(t_{0}\right) \pm \frac{\pi}{4}\right)}}{\sqrt{\left|f^{\prime \prime}\left(t_{0}\right)\right|}}
$$

where we use the plus sign if $f^{\prime \prime}\left(t_{0}\right)>0$ and the minus sign if $f^{\prime \prime}\left(t_{0}\right)<0$.
The function $f(t)$ is called a phase function and the point $t_{0}$ is called a stationary point. The lemma states that most of the contribution to the integral comes from the part of the function near the stationary point. To understand the reason behind this, look at the graph in Figure 3, where we have plotted the function $e^{t} \cos \left(40(t-1 / 2)^{2}\right)$, which is the real part of

![](./images/1c611338-958a-44f7-9d79-2dde87e6ac2a-74_389_430_370_59.jpg)
Figure 3 Concentration of area around the stationary point $t=1 / 2$.

the function $e^{t} e^{40 i(t-1 / 2)^{2}}$. The phase function is in this case $(t-1 / 2)^{2}$. Its derivative vanishes at $t=1 / 2$, which is the stationary point. The area bounded by the graph and the $t$-axis over any interval $[a, b]$ that contains $t_{0}=1 / 2$ is equal to the integral $\int_{a}^{b} e^{t} \cos \left(40(t-1 / 2)^{2}\right) d t$. It is clear from Figure 3 that the area is concentrated around the stationary point $t=1 / 2$. Away from the stationary point, the graph oscillates and the areas cancel out. This is basically what the lemma is saying, only it is about the complex exponential and not the cosine function. However, because the phase function $f(t)$ is real-valued, $e^{i x f(t)}$ is the sum of a cosine and a sine, and so its integral is the sum of two integrals like the one we just described.

We will sketch the proof of the lemma, but before we do so, let us see how the lemma applies toward the proof of Theorem 3.

Proof of Theorem 3. To see how (5) follows from Lemma 1, recall the integral representation that we derived in the proof of the first claim in Theorem 1:

$$
\begin{aligned}
J_{n}(x) & =\frac{1}{2 \pi} \int_{0}^{2 \pi} e^{\frac{x}{2}\left(\zeta-\frac{1}{\zeta}\right)} \zeta^{-n} d \theta=\frac{1}{2 \pi} \int_{0}^{2 \pi} e^{i x \sin \theta} e^{-i n \theta} d \theta \\
& =\frac{1}{2 \pi} \int_{-\pi}^{\pi} e^{i x \sin \theta} e^{-i n \theta} d \theta \\
& =\frac{1}{2 \pi} \int_{0}^{\pi} e^{i x \sin \theta} e^{-i n \theta} d \theta+\frac{1}{2 \pi} \int_{0}^{\pi} e^{-i x \sin \theta} e^{i n \theta} d \theta
\end{aligned}
$$

where the last integral follows by changing the variable $\theta$ to $-\theta$ on the interval $[-\pi, 0]$. Consider the first integral in this representation:

$$
\frac{1}{2 \pi} \int_{0}^{\pi} e^{i x \sin \theta} e^{-i n \theta} d \theta
$$

In Lemma 1, take $f(\theta)=\sin \theta$ and $g(\theta)=e^{-i n \theta}$. Clearly, $f^{\prime}(\theta)=0$ only at $\theta=\frac{\pi}{2}$ in the interval $[0, \pi]$, and $f^{\prime \prime}\left(\frac{\pi}{2}\right)=-\sin \frac{\pi}{2}=-1 \neq 0$. From Lemma 1, it follows that the asymptotic for the integral is

$$
\frac{1}{2 \pi} \sqrt{\frac{2 \pi}{x}} e^{-i n \frac{\pi}{2}} e^{i\left(x-\frac{\pi}{4}\right)}=\frac{1}{2} \sqrt{\frac{2}{\pi x}} e^{i\left(x-\frac{\pi}{4}-n \frac{\pi}{2}\right)}
$$

Similarly, the asymptotic formula for the second integral is

$$
\frac{1}{2 \pi} \int_{0}^{\pi} e^{-i x \sin \theta} e^{i n \theta} d \theta \sim \frac{1}{2} \sqrt{\frac{2}{\pi x}} e^{-i\left(x-\frac{\pi}{4}-n \frac{\pi}{2}\right)}
$$

and (5) follows upon adding the two asymptotics and simplifying with the help of the identity

$$
e^{i\left(x-\frac{\pi}{4}-n \frac{\pi}{2}\right)}+e^{-i\left(x-\frac{\pi}{4}-n \frac{\pi}{2}\right)}=2 \cos \left(x-\frac{\pi}{4}-n \frac{\pi}{2}\right)
$$

Sketch of proof of Lemma 1. Let $I$ denote the integral on the left side of (6), and suppose that $f^{\prime \prime}\left(t_{0}\right)>0$. Expand the function $f(t)$ in a Taylor series about $t_{0}$ :

$$
f(t)=f\left(t_{0}\right)+f^{\prime}\left(t_{0}\right)\left(t-t_{0}\right)+\frac{f^{\prime \prime}\left(t_{0}\right)}{2}\left(t-t_{0}\right)^{2}+\cdots
$$

Since $f^{\prime}\left(t_{0}\right)=0$, approximate $f(t)$ by $f\left(t_{0}\right)+\frac{f^{\prime \prime}\left(t_{0}\right)}{2}\left(t-t_{0}\right)^{2}$, and approximate $g(t)$ by a constant $g\left(t_{0}\right)$. Then

$$
\begin{aligned}
I & \approx \int_{a}^{b} e^{i x\left(f\left(t_{0}\right)+\frac{f^{\prime \prime}\left(t_{0}\right)}{2}\left(t-t_{0}\right)^{2}\right)} g\left(t_{0}\right) d t \\
& =g\left(t_{0}\right) e^{i x f\left(t_{0}\right)} \int_{a}^{b} e^{i x\left(\frac{f^{\prime \prime}\left(t_{0}\right)}{2}\left(t-t_{0}\right)^{2}\right)} d t=g\left(t_{0}\right) e^{i x f\left(t_{0}\right)} \int_{a}^{b} e^{i\left(\left[\frac{x f^{\prime \prime}\left(t_{0}\right)}{2}\right]^{1 / 2}\left(t-t_{0}\right)\right)^{2}} d t \\
& =\sqrt{\frac{2}{x}} g\left(t_{0}\right) \frac{e^{i x f\left(t_{0}\right)}}{\sqrt{f^{\prime \prime}\left(t_{0}\right)}} \int_{A}^{B} e^{i u^{2}} d u
\end{aligned}
$$

where in the last step we used the change of variables $u=\left[\frac{x f^{\prime \prime}\left(t_{0}\right)}{2}\right]^{1 / 2}\left(t-t_{0}\right)$, $d u=\left[\frac{x f^{\prime \prime}\left(t_{0}\right)}{2}\right]^{1 / 2} d t, A=\left[\frac{x f^{\prime \prime}\left(t_{0}\right)}{2}\right]^{1 / 2}\left(a-t_{0}\right)$, and $B=\left[\frac{x f^{\prime \prime}\left(t_{0}\right)}{2}\right]^{1 / 2}\left(b-t_{0}\right)$. As $x \rightarrow \infty, A \rightarrow-\infty$ and $B \rightarrow \infty$, and the integral converges to

$$
\int_{-\infty}^{\infty} e^{i u^{2}} d u=\int_{-\infty}^{\infty} \cos \left(u^{2}\right) d u+i \int_{-\infty}^{\infty} \sin \left(u^{2}\right) d u=\sqrt{\pi}\left[\cos \frac{\pi}{4}+i \sin \frac{\pi}{4}\right]=\sqrt{\pi} e^{i \frac{\pi}{4}}
$$

The last displayed integrals are known as the Fresnel integrals. See [1] for their evaluation. This justifies the asymptotic formula (6) in the case $f^{\prime \prime}\left(t_{0}\right)>0$. The case $f^{\prime \prime}\left(t_{0}\right)<0$ is handled similarly.

## Exercises 4.9

1. Use the integral representation (1) to show that $J_{0}(0)=1$ and $J_{n}(0)=0$ for all integers $n \neq 0$.
2. Use the integral representation (1) to show that $\left|J_{n}(x)\right| \leq 1$ for all integers $n$ and all $x$. (A better bound for $n \neq 0$ is given in Exercise 5.)
3. Derive the series expansion for $\sin x$ in Example 2.
4. (a) Show that $\left|e^{i x \sin \theta}\right|=1$ for all real $x$ and $\theta$.
(b) Use Parseval's identity (Section 2.6) and the Fourier series (4) to prove that for all $x$

$$
1=\left|J_{0}(x)\right|^{2}+2 \sum_{n=1}^{\infty}\left|J_{n}(x)\right|^{2}
$$

(c) For any fixed $x$, show that $\lim _{n \rightarrow \infty} J_{n}(x)=0$.
5. Use Exercise 4(b) to show that, for all $x,\left|J_{0}(x)\right| \leq 1$ and $\left|J_{n}(x)\right| \leq \frac{1}{\sqrt{2}}$.
6. Take real and imaginary parts on both sides of (4) and show that, for all $x$ and all $\theta$,

$$
\begin{aligned}
& \cos (x \sin \theta)=J_{0}(x)+2 \sum_{n=1}^{\infty} J_{2 n}(x) \cos (2 n \theta) \\
& \sin (x \sin \theta)=2 \sum_{n=1}^{\infty} J_{2 n+1}(x) \sin (2 n+1) \theta
\end{aligned}
$$

7. A useful fact. Suppose that $f(t)$ and $g(t)$ are continuous functions for $0 \leq t \leq \pi$, such that $f(t)=f(\pi-t)$ ( $f$ is symmetric with respect to the line $x=\frac{\pi}{2}$ ), and
$g(t)=-g(\pi-t)$ ( $g$ is symmetric with respect to the point $\left.\left(\frac{\pi}{2}, 0\right)\right)$. Show that

$$
\int_{0}^{\pi} f(t) g(t) d t=0
$$

[Hint: Break up the integral over $\left[0, \frac{\pi}{2}\right]$ plus over $\left[\frac{\pi}{2}, \pi\right]$.]
8. Apply the result of Exercise 7 to show that
(a) $\int_{0}^{\pi} \cos \theta \cos (x \sin \theta) d \theta=0$;
(b) $\int_{0}^{\pi} \sin (n \theta) \sin (x \sin \theta) d \theta=0$.
9. Use the integral representation (1) to show that $\frac{d}{d x} J_{0}(x)=-J_{1}(x)$. [Hint: Differentiate under the integral sign. The result of Exercise 8(a) is also useful.]
10. Completing the proof of Theorem 1. Let $\mathcal{I}_{n}(x)$ denote the right side of
(1). We proved in the section that for $n \geq 0, \mathcal{I}_{n}(x)=J_{n}(x)$. We have defined $J_{-n}(x)$ to be $(-1)^{n} J_{n}(x)$. Thus in order to show that (1) holds for $n<0$, it is enough to show that $\mathcal{I}_{-n}(x)=(-1)^{n} \mathcal{I}_{n}(x)$.
(a) Show that $\mathcal{I}_{-n}(x)=\frac{1}{\pi} \int_{0}^{\pi} \cos (n \theta+x \sin \theta) d \theta$.
(b) Use the addition formula for the cosine to expand the integrands in $\mathcal{I}_{n}$ and $\mathcal{I}_{-n}$. Then apply the result of Exercise 7 to conclude that $\mathcal{I}_{n}=(-1)^{n} \mathcal{I}_{n}$.
In Exercises 11-12, find an asymptotic formula for the given function as $x \rightarrow \infty$. If the interval of integration contains more than one stationary point, write your integral as a sum of integrals over intervals that contain one stationary point each.
11. $\int_{-1}^{1} e^{i x^{2} \cos t} d t$.
12. $\int_{-10}^{10} e^{i x \cos t} \sin ^{2} t d t$.
13. Project Problem: Zeros of Bessel functions. The asymptotic formula (5) says that there is a constant $C$ such that, for all large $x$,

$$
\left|J_{n}(x)-\sqrt{\frac{2}{\pi x}} \cos \left(x-\frac{\pi}{4}-\frac{n \pi}{2}\right)\right| \leq \frac{C}{x^{3 / 2}}
$$

(a) Show that, for all large $x,\left|\sqrt{x} J_{n}(x)-\sqrt{\frac{2}{\pi}} \cos \left(x-\frac{\pi}{4}-\frac{n \pi}{2}\right)\right| \leq \frac{C}{x}$.
(b) Show that the function $\cos \left(x-\frac{\pi}{4}-\frac{n \pi}{2}\right)$ equals to $\pm 1$ for $x=k \pi+\frac{\pi}{4}+\frac{n \pi}{2}$, $k=0,1,2, \ldots$.
(c) Show that for large values of $x$, the function $\sqrt{x} J_{n}(x)$ has at least one zero in the interval $I_{k}=\left[k \pi+\frac{\pi}{4}+\frac{n \pi}{2},(k+1) \pi+\frac{\pi}{4}+\frac{n \pi}{2}\right]$. Conclude that $J_{n}(x)$ has infinitely many zeros; at least one in each interval $I_{k}$, for $k$ sufficiently large.
(d) Show that the function $\cos \left(x-\frac{\pi}{4}-\frac{n \pi}{2}\right)$ is equal to 0 for $x=\alpha_{k}=\frac{\pi}{4}+\frac{(n+1) \pi}{2}+k \pi$, $k=0,1,2, \ldots$. You can actually show that the zeros of $J_{n}(x)$ are approximated by the $\alpha_{k} \mathrm{~s}$. Thus, for large $x$, the zeros of $J_{n}(x)$ are approximately $\alpha_{k}= \frac{\pi}{4}+\frac{(n+1) \pi}{2}+k \pi, k=0,1,2, \ldots$.
(e) Test the last assertion by computing the first ten zeros of $J_{0}(x), J_{1}(x)$, and $J_{2}(x)$, and then comparing them with the sequences $\frac{\pi}{4}+\frac{(n+1) \pi}{2}+k \pi k=0,1,2, \ldots$, for $n=0,1,2$.
(f) Use the result in (d) to show that if $\lambda_{n, j}<\lambda_{n, j+1}$ are two consecutive positive zeros of $J_{n}$, then $\lim _{j \rightarrow \infty}\left(\lambda_{n, j+1}-\lambda_{n, j}\right)=\pi$.

