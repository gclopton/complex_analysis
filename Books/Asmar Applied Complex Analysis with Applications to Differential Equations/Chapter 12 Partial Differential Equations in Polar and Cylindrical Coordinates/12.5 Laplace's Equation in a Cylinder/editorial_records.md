
# Editorial records

Reading note: 12.5 Laplace's Equation in a Cylinder.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

No recovery content changes were needed in this note. Existing genuine corrections and formatting were retained.

## Source-to-current comparison

Source: /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 12 Partial Differential Equations in Polar and Cylindrical Coordinates/12.5 Laplace's Equation in a Cylinder.md

This exact comparison preserves the full change evidence, including formatting, OCR corrections, restored source wording, and required standalone context. The entries above explain the recovery edits. The comparison is not a claim that every difference is a correction; component serialization, callout wrapping, and printed labels outside callouts are formatting.

`````diff
--- /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 12 Partial Differential Equations in Polar and Cylindrical Coordinates/12.5 Laplace's Equation in a Cylinder.md
+++ /Users/gradyclopton/ObsidianVaults/complex_analysis/Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 12 Partial Differential Equations in Polar and Cylindrical Coordinates/12.5 Laplace's Equation in a Cylinder.md
@@ -1,50 +1,60 @@
+
 ### 12.5 Laplace's Equation in a Cylinder
 
-![](./images/1c611338-958a-44f7-9d79-2dde87e6ac2a-36_530_373_700_63.jpg)
-Figure 1
-DIRICHLET PROBLEM IN A CYLINDER WITH ZERO LATERAL TEMPERATURE
+```scientific-figure
+id: c41257ae-8ff8-4c35-9c08-cd303f0c026d
+numbered: false
+title: ""
+caption: Figure 1 Cylinder with zero temperature on its base and lateral surface.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 12 Partial Differential Equations in Polar and Cylindrical Coordinates/images/1c611338-958a-44f7-9d79-2dde87e6ac2a-36_530_373_700_63.jpg
+    caption: ""
+```
+
 
 In this section we treat certain radially symmetric Dirichlet problems in cylindrical regions. In cylindrical coordinates, Laplace's equation, with no $\phi$ dependence, is
 
 $$
 \nabla^{2} u=\frac{\partial^{2} u}{\partial \rho^{2}}+\frac{1}{\rho} \frac{\partial u}{\partial \rho}+\frac{\partial^{2} u}{\partial z^{2}}=0
+\tag{1}
 $$
 
 (See (4), Section 12.1.) The first problem that we will consider models the steady-state temperature distribution inside a cylinder with lateral surface and bottom kept at zero temperature and with radially symmetric temperature distribution at the top, as shown in Figure 1.
 
-The solution of Laplace's equation (1) with boundary conditions
-
-$$
-\begin{array}{r}
-u(\rho, 0)=0, \quad 0<\rho<a \\
-u(a, z)=0, \quad 0<z<h \\
-u(\rho, h)=f(\rho), \quad 0<\rho<a
-\end{array}
-$$
-
-is
-
-$$
-u(\rho, z)=\sum_{n=1}^{\infty} A_{n} J_{0}\left(\lambda_{n} \rho\right) \sinh \lambda_{n} z
-$$
-
-where
-
-$$
-A_{n}=\frac{2}{\sinh \left(\lambda_{n} h\right) a^{2} J_{1}^{2}\left(\alpha_{n}\right)} \int_{0}^{a} f(\rho) J_{0}\left(\lambda_{n} \rho\right) \rho d \rho, \quad \lambda_{n}=\frac{\alpha_{n}}{a}
-$$
-
-and $\alpha_{n}$ is the $n$th positive zero of $J_{0}$, the Bessel function of order 0 .
-Proof Using the method of separation of variables and setting $u(\rho, z)=R(\rho) Z(z)$, we get the equations $\rho^{2} R^{\prime \prime}+\rho R^{\prime}-k \rho^{2} R=0, R(a)=0$, and $Z^{\prime \prime}+k Z=0$, $Z(0)=0$, where $k$ is the separation constant. We also require that $R$ be bounded
-
-![](./images/1c611338-958a-44f7-9d79-2dde87e6ac2a-37_398_440_310_37.jpg)
-Figure 2 Modified Bessel functions.
-
-![](./images/1c611338-958a-44f7-9d79-2dde87e6ac2a-37_500_401_918_42.jpg)
-Figure 3
-
-DIRICHLET PROBLEM IN A CYLINDER WITH NONZERO LATERAL TEMPERATURE
-at $\rho=0$, since we are solving for the temperature inside the cylinder. If $k=0$, it is straightforward to check that we only get the solution $R=0$. If $k>0$, say $k=\lambda^{2}$, then we get the parametric form of the modified Bessel equation of order 0 defined in Exercise 7 (see also Exercises 29 and 30, Section 12.7). The general solution in this case is a linear combination of the modified Bessel functions of the first and second kind, $I_{0}$ and $K_{0}$, shown in Figure 2 (see Exercise 7). Since the first one is positive and strictly increasing for $\rho>0$, and the second one is unbounded near zero, we conclude that no nontrivial bounded linear combination of these functions can satisfy the boundary conditions on $R$. So this leaves the only possibility $k=-\lambda^{2}<0$. In this case we have
+> [!equation|759e4cfd-19fb-55c3-9d13-1fc494493637.local at=989cdb39-f93c-5465-a81f-e6666e444d27] Axisymmetric Dirichlet solution in a cylinder with zero lateral and bottom temperatures
+> Let $a,h>0$. The solution of $u_{\rho\rho}+\rho^{-1}u_\rho+u_{zz}=0$ in $0<\rho<a$, $0<z<h$, regular at the cylinder axis and independent of azimuth, with boundary conditions
+>
+> $$
+> \begin{array}{r}
+> u(\rho, 0)=0, \quad 0<\rho<a \\
+> u(a, z)=0, \quad 0<z<h \\
+> u(\rho, h)=f(\rho), \quad 0<\rho<a
+> \end{array}
+> $$
+>
+> is
+>
+> $$
+> u(\rho, z)=\sum_{n=1}^{\infty} A_{n} J_{0}\left(\lambda_{n} \rho\right) \sinh \lambda_{n} z
+> $$
+>
+> where
+>
+> $$
+> A_{n}=\frac{2}{\sinh \left(\lambda_{n} h\right) a^{2} J_{1}^{2}\left(\alpha_{n}\right)} \int_{0}^{a} f(\rho) J_{0}\left(\lambda_{n} \rho\right) \rho d \rho, \quad \lambda_{n}=\frac{\alpha_{n}}{a}
+> $$
+>
+> and $\alpha_{n}$ is the $n$th positive zero of $J_{0}$, the Bessel function of order 0 .
+>
+>
+> Assume piecewise smooth prescribed temperature data. Boundary limits are taken on the open faces at continuity points; continuity across the circular edges requires matching data. The functions $J_0,J_1$ are Bessel functions of the first kind and $I_0$ is the modified Bessel function of the first kind.
+
+*Printed equation labels: (2) solution series; (3) coefficients $A_n$.*
+
+Proof Using the method of separation of variables and setting $u(\rho, z)=R(\rho) Z(z)$, we get the equations $\rho^{2} R^{\prime \prime}+\rho R^{\prime}-k \rho^{2} R=0, R(a)=0$, and $Z^{\prime \prime}+k Z=0$, $Z(0)=0$, where $k$ is the separation constant. We also require that $R$ be bounded at $\rho=0$, since we are solving for the temperature inside the cylinder. If $k=0$, it is straightforward to check that we only get the solution $R=0$. If $k>0$, say $k=\lambda^{2}$, then we get the parametric form of the modified Bessel equation of order 0 defined in Exercise 7 (see also Exercises 29 and 30, Section 12.7). The general solution in this case is a linear combination of the modified Bessel functions of the first and second kind, $I_{0}$ and $K_{0}$, shown in Figure 2 (see Exercise 7). Since the first one is positive and strictly increasing for $\rho>0$, and the second one is unbounded near zero, we conclude that no nontrivial bounded linear combination of these functions can satisfy the boundary conditions on $R$. So this leaves the only possibility $k=-\lambda^{2}<0$. In this case we have
 
 $$
 \begin{gathered}
@@ -67,105 +77,199 @@
 
 Thus $A_{n} \sinh \lambda_{n} h$ must be the $n$th Bessel coefficient of $f(\rho)$, and so (3) follows from Theorem 2, Section 12.8. $\square$
 
+```scientific-figure
+id: 7d5b682d-29aa-4d0e-8092-7ffe1b718b68
+numbered: false
+title: ""
+caption: Figure 2 Modified Bessel functions.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 12 Partial Differential Equations in Polar and Cylindrical Coordinates/images/1c611338-958a-44f7-9d79-2dde87e6ac2a-37_398_440_310_37.jpg
+    caption: ""
+```
+
+
+```scientific-figure
+id: 39c64728-d24d-4c44-9733-643dc73ff3e0
+numbered: false
+title: ""
+caption: Figure 3 Cylinder with zero temperature on both bases and prescribed temperature on the lateral surface.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 12 Partial Differential Equations in Polar and Cylindrical Coordinates/images/1c611338-958a-44f7-9d79-2dde87e6ac2a-37_500_401_918_42.jpg
+    caption: ""
+```
+
+
 As a second illustration, we consider a boundary value problem with a nonzero boundary condition on the lateral surface of the cylinder (see Figure 3).
 
-The solution of Laplace's equation (1) with boundary conditions
-
-$$
-\begin{gathered}
-u(\rho, 0)=u(\rho, h)=0, \quad 0<\rho<a \\
-u(a, z)=f(z), \quad 0<z<h
-\end{gathered}
-$$
-
-is
-
-$$
-u(\rho, z)=\sum_{n=1}^{\infty} B_{n} I_{0}\left(\frac{n \pi}{h} \rho\right) \sin \frac{n \pi}{h} z,
-$$
-
-where $I_{0}$ is the modified Bessel function of the first kind of order 0, and
-
-$$
-B_{n}=\frac{2}{I_{0}\left(\frac{n \pi a}{h}\right) h} \int_{0}^{h} f(z) \sin \frac{n \pi}{h} z d z .
-$$
-
-![](./images/1c611338-958a-44f7-9d79-2dde87e6ac2a-38_500_378_705_65.jpg)
-Figure 4 for Exercise 5.
+> [!equation|bf8bfac8-6676-537a-a7f2-11398f29b5e7.local at=8e9d1cca-bb7f-5992-8f06-67f8d96d1b5f] Axisymmetric Dirichlet solution in a cylinder with zero base temperatures
+> Let $a,h>0$. The solution of $u_{\rho\rho}+\rho^{-1}u_\rho+u_{zz}=0$ in $0<\rho<a$, $0<z<h$, regular at the cylinder axis and independent of azimuth, with boundary conditions
+>
+> $$
+> \begin{gathered}
+> u(\rho, 0)=u(\rho, h)=0, \quad 0<\rho<a \\
+> u(a, z)=f(z), \quad 0<z<h
+> \end{gathered}
+> $$
+>
+> is
+>
+> $$
+> u(\rho, z)=\sum_{n=1}^{\infty} B_{n} I_{0}\left(\frac{n \pi}{h} \rho\right) \sin \frac{n \pi}{h} z,
+> $$
+>
+> where $I_{0}$ is the modified Bessel function of the first kind of order 0, and
+>
+> $$
+> B_{n}=\frac{2}{I_{0}\left(\frac{n \pi a}{h}\right) h} \int_{0}^{h} f(z) \sin \frac{n \pi}{h} z d z .
+> $$
+>
+>
+>
+> Assume piecewise smooth prescribed temperature data. Boundary limits are taken on the open faces at continuity points; continuity across the circular edges requires matching data. The functions $J_0,J_1$ are Bessel functions of the first kind and $I_0$ is the modified Bessel function of the first kind.
+
+*Printed equation labels: (4) solution series; (5) coefficients $B_n$.*
 
 The derivation of the solution is very much like the one we did previously, except that now the interesting case of the separation constant is $k=\nu^{2}>0$. The details are left to Exercise 8.
 
-## Exercises 4.5
-
-In Exercises 1-4, find the steady-state temperature in the cylinder of Figure 1 for the given temperature distribution of its top. Take $a=1$, and $h=2$.
-
-1. $f(\rho)=100$.
-2. $f(\rho)=100-\rho^{2}$.
-3. $f(\rho)= \begin{cases}100 & \text { if } 0<\rho<\frac{1}{2}, \\ 0 & \text { if } \frac{1}{2}<\rho<1 .\end{cases}$
-4. $f(\rho)=70 J_{0}(\rho)$.
-5. (a) Find the steady-state temperature in the cylinder with boundary values as shown in Figure 4.
-(b) Solve (1) for the boundary conditions
-
-$$
-\begin{gathered}
-u(\rho, 0)=f_{1}(\rho), \quad 0<\rho<a \\
-u(a, z)=0, \quad 0<z<h \\
-u(\rho, h)=f_{2}(\rho), \quad 0<\rho<a
-\end{gathered}
-$$
-
-[Hint: Combine (a) with the solution in this section.]
-6. Solve (1) for the boundary conditions
-
-$$
-\begin{array}{cc}
-u(\rho, 0)=100, & 0<\rho<1, \\
-u(1, z)=0, & 0<z<2, \\
-u(\rho, 2)=100, & 0<\rho<1 .
-\end{array}
-$$
-
-7. Make the substitution $x=\lambda \rho(\lambda>0)$ in the parametric form of the modified Bessel equation $\rho^{2} R^{\prime \prime}+\rho R^{\prime}-\lambda^{2} \rho^{2} R=0$ and obtain that its general solution is $y=c_{1} I_{0}(\lambda \rho)+c_{2} K_{0}(\lambda \rho)$, where $I_{0}$ and $K_{0}$ are the modified Bessel functions of the first and second kind. [Hint: Use Exercises 29 and 30, Section 12.7.]
-
-Project Problem: Lateral surface with nonzero temperature. Do Exercises 8 and 9.
-8. In this exercise we derive (4) and (5).
-(a) Refer to the Dirichlet problem in the cylinder with boundary conditions as given just before (4). Use the separation of variables method and obtain
-
-$$
-\begin{gathered}
-Z^{\prime \prime}+\nu^{2} Z=0, \quad Z(0)=0 \text { and } Z(h)=0, \\
-\rho^{2} R^{\prime \prime}+\rho R^{\prime}-\nu^{2} \rho^{2} R=0 .
-\end{gathered}
-$$
-
-(b) Show that the only possible solutions of the first equation correspond to $\nu_{n}=\frac{n \pi}{h}$ and hence are
-
-$$
-Z_{n}(z)=\sin \frac{n \pi}{h} z, \quad n=1,2, \ldots
-$$
-
-(c) Derive (4) and (5). [Hint: Use Exercise 7.]
-9. Solve (1) for the boundary conditions
-
-$$
-\begin{gathered}
-u(\rho, 0)=u(\rho, 2)=0, \quad 0<\rho<1, \\
-u(1, z)=10 z, \quad 0<z<2 .
-\end{gathered}
-$$
-
-![](./images/1c611338-958a-44f7-9d79-2dde87e6ac2a-39_289_417_165_33.jpg)
-Figure 5 for Exercise 11.
-
-10. Solve (1) for the boundary conditions
-
-$$
-\begin{array}{ll}
-u(\rho, 0)=100, & 0<\rho<1, \\
-u(1, z)=10 z, & 0<z<2, \\
-u(\rho, 2)=100, & 0<\rho<1 .
-\end{array}
-$$
-
-[Hint: Combine the solutions of Exercises 6 and 9.]
-11. Find the steady-state temperature in a cylindrical barrel floating in water as shown in Figure 5.
+## Exercises 12.5
+
+
+> [!prompt|456fdce1-c80d-56d4-b8a7-617de0848b83.local at=40e410f1-f6aa-5f15-a7e5-01b5de306772] Shared exercise instructions
+> In Exercises 1-4, find the steady-state temperature in the cylinder of Figure 1 for the given temperature distribution of its top. Take $a=1$, and $h=2$.
+
+
+> [!exercise|e3c16dcf-5e5e-5568-8b91-fcff5c77353d.local at=71f606dc-b632-56d0-a029-6cf6915e8254] Exercise 1
+> $f(\rho)=100$.
+
+
+> [!exercise|8e861274-b92c-518a-8007-62ab13d72a16.local at=03f9e2f8-5c42-5103-928d-2b5b1813bed0] Exercise 2
+> $f(\rho)=100-\rho^{2}$.
+
+
+> [!exercise|d0160f10-0b8f-576b-98df-ae1c784d0da3.local at=66462b6b-c476-5785-a9b4-822e0a49958c] Exercise 3
+> $f(\rho)= \begin{cases}100 & \text { if } 0<\rho<\frac{1}{2}, \\ 0 & \text { if } \frac{1}{2}<\rho<1 .\end{cases}$
+
+
+> [!exercise|3392660f-e0de-5aed-a434-60ed1637ba8f.local at=5c3d259f-7b40-5220-bb20-286165494117] Exercise 4
+> $f(\rho)=70 J_{0}(\rho)$.
+
+
+> [!exercise|4765b5fa-f520-5f13-9cb0-5221724af05d.local at=a170b5d3-d412-58f2-9143-9c95deb67f37] Exercise 5
+> (a) Find the steady-state temperature in the cylinder with boundary values as shown in Figure 4.
+>
+> (b) Solve (1) for the boundary conditions
+>
+> $$
+> \begin{gathered}
+> u(\rho, 0)=f_{1}(\rho), \quad 0<\rho<a \\
+> u(a, z)=0, \quad 0<z<h \\
+> u(\rho, h)=f_{2}(\rho), \quad 0<\rho<a
+> \end{gathered}
+> $$
+>
+> [Hint: Combine (a) with the solution in this section.]
+
+
+```scientific-figure
+id: 9db392ae-5466-4503-bdc9-a30102fc109d
+numbered: false
+title: ""
+caption: Figure 4 for Exercise 5.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 12 Partial Differential Equations in Polar and Cylindrical Coordinates/images/1c611338-958a-44f7-9d79-2dde87e6ac2a-38_500_378_705_65.jpg
+    caption: ""
+```
+
+
+
+
+> [!exercise|f091c524-ad02-5688-b3eb-1f04d3b49c27.local at=7ecf783a-58a3-50e8-9dab-28b9de2bf9f7] Exercise 6
+> Solve (1) for the boundary conditions
+>
+> $$
+> \begin{array}{cc}
+> u(\rho, 0)=100, & 0<\rho<1, \\
+> u(1, z)=0, & 0<z<2, \\
+> u(\rho, 2)=100, & 0<\rho<1 .
+> \end{array}
+> $$
+
+
+> [!exercise|8ec40307-fa41-5490-8648-bb5c203b6d9a.local at=ebd423d8-32c9-510d-acbf-823ac098fdbd] Exercise 7
+> Make the substitution $x=\lambda \rho(\lambda>0)$ in the parametric form of the modified Bessel equation $\rho^{2} R^{\prime \prime}+\rho R^{\prime}-\lambda^{2} \rho^{2} R=0$ and obtain that its general solution is $R(\rho)=c_{1} I_{0}(\lambda \rho)+c_{2} K_{0}(\lambda \rho)$, where $I_{0}$ and $K_{0}$ are the modified Bessel functions of the first and second kind. [Hint: Use Exercises 29 and 30, Section 12.7.]
+
+
+> [!prompt|139f96f8-5250-5e49-8c41-06ca2416b275.local at=594ecc7c-ce15-5591-b959-5bda491cf6d4] Shared exercise instructions
+> Project Problem: Lateral surface with nonzero temperature. Do Exercises 8 and 9.
+
+
+> [!exercise|31adf718-8ca4-549f-8189-b71844ce1cc4.local at=f025ed05-a90c-5e84-b012-3e4bc98c3779] Exercise 8
+> In this exercise we derive (4) and (5).
+> (a) Refer to the Dirichlet problem in the cylinder with boundary conditions as given just before (4). Use the separation of variables method and obtain
+>
+> $$
+> \begin{gathered}
+> Z^{\prime \prime}+\nu^{2} Z=0, \quad Z(0)=0 \text { and } Z(h)=0, \\
+> \rho^{2} R^{\prime \prime}+\rho R^{\prime}-\nu^{2} \rho^{2} R=0 .
+> \end{gathered}
+> $$
+>
+> (b) Show that the only possible solutions of the first equation correspond to $\nu_{n}=\frac{n \pi}{h}$ and hence are
+>
+> $$
+> Z_{n}(z)=\sin \frac{n \pi}{h} z, \quad n=1,2, \ldots
+> $$
+>
+> (c) Derive (4) and (5). [Hint: Use Exercise 7.]
+
+
+> [!exercise|86bd1fd7-511a-5bfb-9e25-f71d3847451e.local at=d261cfad-ef0c-5815-ac61-833e03f86f2d] Exercise 9
+> Solve (1) for the boundary conditions
+>
+> $$
+> \begin{gathered}
+> u(\rho, 0)=u(\rho, 2)=0, \quad 0<\rho<1, \\
+> u(1, z)=10 z, \quad 0<z<2 .
+> \end{gathered}
+> $$
+
+
+> [!exercise|8d69744a-25cf-5c44-a1d8-a6c7db362405.local at=79f10149-a9a5-56b0-bef1-2f3e7b3b9de6] Exercise 10
+> Solve (1) for the boundary conditions
+>
+> $$
+> \begin{array}{ll}
+> u(\rho, 0)=100, & 0<\rho<1, \\
+> u(1, z)=10 z, & 0<z<2, \\
+> u(\rho, 2)=100, & 0<\rho<1 .
+> \end{array}
+> $$
+>
+> [Hint: Combine the solutions of Exercises 6 and 9.]
+
+
+> [!exercise|9e3e5b97-b1e3-5b1f-ba80-386e6bcc3b83.local at=73348869-e16c-5e6d-86ab-028bc1fde3b3] Exercise 11
+> Find the steady-state temperature in a cylindrical barrel floating in water as shown in Figure 5.
+
+
+```scientific-figure
+id: 02f9d20c-5e18-42f4-a962-d4a10ff6905d
+numbered: false
+title: ""
+caption: Figure 5 for Exercise 11.
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 12 Partial Differential Equations in Polar and Cylindrical Coordinates/images/1c611338-958a-44f7-9d79-2dde87e6ac2a-39_289_417_165_33.jpg
+    caption: ""
+```

`````
