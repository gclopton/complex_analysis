
# Editorial records

Reading note: 6.5 Green's Functions.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Move editorial commentary out of the reading note.

### Before

````text
*Editorial clarification: the boundary representation statements explicitly require bounded harmonic functions with the stated boundary limits, rather than arbitrary independently assigned boundary values. The missing Green-function properties were restored from the printed theorem; Exercise 11’s conjugates and imaginary unit were corrected against the PDF.*
````
### After

````text

````

## Additional source comparison

## 1. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!lemma|4b5f04b0-9d32-53f2-9c90-5a528244ebc7.local at=d91b3ab8-bb1d-5cc2-ae3b-b8cbb188941f] Boundary Integral Formula at the Center of a Conformal Disk Map
> Let $\Omega$ be a bounded simply connected region with a smooth simple boundary $\Gamma$, and let $\phi$ map $\Omega$ conformally onto the unit disk, extending analytically and one-to-one to the boundary. Let $u$ be a bounded harmonic function on $\Omega$ whose boundary limits give piecewise continuous data on $\Gamma$. Values at the finitely many discontinuities do not affect the integral. The derivative $\partial/\partial n_\zeta$ is along the outward unit normal at $\zeta\in\Gamma$, and $ds=|d\zeta|$ is arc length.
>
> If $z_0\in\Omega$ satisfies $\phi(z_0)=0$, then
>
> $$
> u(z_0)=\frac1{2\pi}\int_\Gamma u(\zeta)\frac{\partial}{\partial n_\zeta}\ln|\phi(\zeta)|\,ds.
> $$
````
### After

````text
> [!lemma|4b5f04b0-9d32-53f2-9c90-5a528244ebc7.local at=d91b3ab8-bb1d-5cc2-ae3b-b8cbb188941f] Change of Variables
> Suppose that $w=\phi(z)$ is a one-to-one analytic mapping of a simply connected region $\Omega$ and its boundary $\Gamma$ onto the open unit disk $D$ and its boundary $C$. Let $u$ be a bounded function harmonic on $\Omega$ and with piecewise continuous boundary limits on the boundary $\Gamma$. Let $z_{0}$ in $\Omega$ be the point such that $\phi\left(z_{0}\right)=0$. Then
>
> $$
> u\left(z_{0}\right)=\frac{1}{2 \pi} \int_{\Gamma} u(\zeta) \frac{\partial \ln |\phi(\zeta)|}{\partial n} d s
> $$
>
> where $d s=|d \zeta|$ is the element of arc length on $\Gamma$. Hence if $\Gamma$ is parametrized by $\gamma(t), a \leq t \leq b$, then $d s=\left|\gamma^{\prime}(t)\right| d t$. The boundary is smooth, and $\partial/\partial n$ denotes the outward normal derivative in $\zeta$.
````

## 2. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|73626c8b-8bf6-5626-ab7f-b5d56507a6bc.local at=a64f3bd8-f4e9-5b3c-bb32-6159d228c043] Green Function Boundary Representation for Planar Harmonic Functions
> Let $\Omega$ be a bounded simply connected region with a smooth simple boundary $\Gamma$, and let $\phi$ map $\Omega$ conformally onto the unit disk, extending analytically and one-to-one to the boundary. Let $u$ be a bounded harmonic function on $\Omega$ whose boundary limits give piecewise continuous data on $\Gamma$. Values at the finitely many discontinuities do not affect the integral. The derivative $\partial/\partial n_\zeta$ is along the outward unit normal at $\zeta\in\Gamma$, and $ds=|d\zeta|$ is arc length.
>
> For $z\in\Omega$, put
>
> $$
> \Phi(z,\zeta)=\frac{\phi(\zeta)-\phi(z)}{1-\overline{\phi(z)}\phi(\zeta)}.
> $$
>
> Then
>
> $$
> u(z)=\frac1{2\pi}\int_\Gamma u(\zeta)\frac{\partial}{\partial n_\zeta}\ln|\Phi(z,\zeta)|\,ds.
> $$
````
### After

````text
> [!theorem|73626c8b-8bf6-5626-ab7f-b5d56507a6bc.local at=a64f3bd8-f4e9-5b3c-bb32-6159d228c043] Green Function Boundary Representation for Planar Harmonic Functions
> Suppose that $\Omega$ is a simply connected region with boundary $\Gamma$, and $\phi$ is a one-to-one analytic function on $\Omega$ and its boundary onto the unit disk and its boundary. Let $u(z)$ be a bounded function harmonic on $\Omega$ and with piecewise continuous boundary limits on $\Gamma$. For $z$ and $\zeta$ in $\Omega$, let $\Phi(z, \zeta)$ $\Phi(z,\zeta)=(\phi(\zeta)-\phi(z))/(1-\overline{\phi(z)}\phi(\zeta))$. Then, for any $z$ in $\Omega$, we have
> $$
> u(z)=\frac{1}{2 \pi} \int_{\Gamma} u(\zeta) \frac{\partial}{\partial n} \ln |\Phi(z, \zeta)| d s
> $$
>
> where $d s=|d \zeta|$ is the element of arc length on $\Gamma$. The boundary is smooth; the normal derivative is outward in $\zeta$.
````

## 3. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!definition|22294c03-a159-5ada-85fa-bda8ea638b64.local at=a0780b4a-230d-5bab-9756-cb379d15b1d0] Logarithmically Normalized Dirichlet Green Function of a Simply Connected Planar Region
> Let $\Omega\subsetneq\mathbb C$ be a simply connected region and let $\phi:\Omega\to\mathbb D$ be a conformal bijection. For distinct $z,\zeta\in\Omega$, the Dirichlet Green function with logarithmic normalization is
>
> $$
> G(z,\zeta)=\ln\left|\frac{\phi(\zeta)-\phi(z)}{1-\overline{\phi(z)}\phi(\zeta)}\right|.
> $$
>
> It has a logarithmic singularity as $\zeta\to z$. This convention makes $G$ negative in the interior; its definition is independent of the choice of $\phi$.
````
### After

````text
> [!definition|22294c03-a159-5ada-85fa-bda8ea638b64.local at=a0780b4a-230d-5bab-9756-cb379d15b1d0] Logarithmically Normalized Dirichlet Green Function of a Simply Connected Planar Region
> Let $\phi$ be a one-to-one analytic map of a simply connected region $\Omega$ onto the unit disk. Put $\Phi(z,\zeta)=(\phi(\zeta)-\phi(z))/(1-\overline{\phi(z)}\phi(\zeta))$.
>
> The function
>
> $$
> G(z, \zeta)=\ln |\Phi(z, \zeta)|=\ln \left|\frac{\phi(\zeta)-\phi(z)}{1-\overline{\phi(z)} \phi(\zeta)}\right|, \quad z,\zeta\in\Omega,\ z\ne\zeta
> $$
>
> is called the Green's function for the region $\Omega$.
````

## 4. Restore author wording/title with only necessary missing context and genuine corrections.

### Before

````text
> [!theorem|0bf7894d-52ad-5799-bf75-03148eb29f36.local at=42dc429e-e2cb-51f6-a7e0-31b8aca25f4d] Sign, Symmetry, and Logarithmic Decomposition of Planar Dirichlet Green Functions
> Let $\Omega$ be a simply connected planar region with boundary $\Gamma$, and let $\phi$ be a conformal bijection to the unit disk that extends analytically and one-to-one to the boundary. Define, for $z\ne\zeta$ in $\Omega$,
>
> $$
> G(z,\zeta)=\ln\left|\frac{\phi(\zeta)-\phi(z)}{1-\overline{\phi(z)}\phi(\zeta)}\right|.
> $$
>
> (i) $G(z,\zeta)\leq0$ in the interior (with $G(z,z)=-\infty$ understood at its logarithmic singularity).
>
> (ii) For $z\in\Omega$ and $\zeta\in\Gamma$, the boundary value is $G(z,\zeta)=0$.
>
> (iii) $G(z,\zeta)=G(\zeta,z)$.
>
> (iv) For every fixed $z\in\Omega$, there is a function $u_1(z,\zeta)$ harmonic in $\zeta$ throughout $\Omega$, with boundary values $-\ln|z-\zeta|$, such that
>
> $$
> G(z,\zeta)=u_1(z,\zeta)+\ln|z-\zeta|\qquad(\zeta\ne z).
> $$
````
### After

````text
> [!theorem|0bf7894d-52ad-5799-bf75-03148eb29f36.local at=42dc429e-e2cb-51f6-a7e0-31b8aca25f4d] Properties of Green's Functions
> Suppose that $\Omega$ is a simply connected region with boundary $\Gamma$, and let $\phi$ be a one-to-one analytic mapping of $\Omega$ and its boundary onto the unit disk and its boundary. Put
>
> $$
> \Phi(z,\zeta)=\frac{\phi(\zeta)-\phi(z)}{1-\overline{\phi(z)}\phi(\zeta)},\qquad G(z,\zeta)=\ln|\Phi(z,\zeta)|.
> $$
>
> Then the Green's function $G(z,\zeta)$ has the following properties:
>
> (i) $G(z,\zeta)\leq0$ for all $z$ and $\zeta$ in $\Omega$ (with the logarithmic value $-\infty$ at $z=\zeta$);
>
> (ii) $G(z,\zeta)=0$ for all $z$ in $\Omega$ and $\zeta$ on $\Gamma$;
>
> (iii) $G(z,\zeta)=G(\zeta,z)$ for all $z$ and $\zeta$ in $\Omega$ (symmetric property);
>
> (iv) for each $z$ in $\Omega$, there is a function $\zeta\mapsto u_1(z,\zeta)$, such that $u_1(z,\zeta)$ is harmonic for all $\zeta$ in $\Omega$, $u_1(z,\zeta)=-\ln|z-\zeta|$ for all $\zeta$ on the boundary $\Gamma$, and $G(z,\zeta)=u_1(z,\zeta)+\ln|z-\zeta|$ for all $\zeta\ne z$ in $\Omega$.
````

## Additional source comparison

## 1. Correct duplicated notation in restored sentence.

### Before

````text
let $\Phi(z, \zeta)$ $\Phi(z,\zeta)=(\phi(\zeta)-\phi(z))/(1-\overline{\phi(z)}\phi(\zeta))$
````
### After

````text
let $\Phi(z,\zeta)=(\phi(\zeta)-\phi(z))/(1-\overline{\phi(z)}\phi(\zeta))$
````

## Source-to-current comparison

Source: /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 06 Conformal Mappings/6.5 Green's Functions.md

This exact comparison preserves the full change evidence, including formatting, OCR corrections, restored source wording, and required standalone context. The entries above explain the recovery edits. The comparison is not a claim that every difference is a correction; component serialization, callout wrapping, and printed labels outside callouts are formatting.

`````diff
--- /Users/gradyclopton/Documents/ChatGPT/Mathematics/asmar-admission-20261107/baseline/Chapter 06 Conformal Mappings/6.5 Green's Functions.md
+++ /Users/gradyclopton/ObsidianVaults/complex_analysis/Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 06 Conformal Mappings/6.5 Green's Functions.md
@@ -1,656 +1,646 @@
 
-In this section we use Green's functions to solve the Poisson boundary value problem on a region $\Omega$, then apply similar techniques to solve another important type of problem known as a Neumann problem. Suppose $h$ is a continuous function on the region $\Omega$ and $f$ is a piecewise continuous function on the boundary $\Gamma$ of $\Omega$, which is a closed simple curve with positive orientation. We start with the Poisson problem, which consists of the inhomogeneous Laplace equation known as Poisson's equation along with a condition specifying the values of the function on the boundary $\Gamma$ of $\Omega$ (Figure 7.116):
+# 6.5 Green’s Functions
+
+What is a Green's function and what can it do for us? To answer these questions, let us review a few facts about the solution of a Dirichlet problem. Suppose that $\Omega$ is a simply connected region bounded by a simple path $\Gamma$. Let $f$ be a piecewise continuous function on $\Gamma$ and consider the Dirichlet problem (Figure 1)
+
+```scientific-figure
+id: 5412c1f9-d3d9-4514-a659-b8f7a5a8519a
+numbered: false
+title: ""
+caption: "**Figure 1.** A Dirichlet problem in a simply connected region."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 06 Conformal Mappings/images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-50_460_542_1377_93.jpg
+    caption: ""
+```
+
+$$
+\begin{gathered}
+\Delta u(z)=0 \quad \text { for all } z \text { in } \Omega \\
+u(\zeta)=f(\zeta) \quad \text { for all } \zeta \text { on } \Gamma
+\end{gathered}
+$$
+
+If $\Omega$ is the unit disk $D$, then the solution of the problem (1)-(2) is given by the Poisson formula (see (12), Section 3.8). The importance of this formula is that it depends only on the region and the boundary function $f$. For an arbitrary simply connected region $\Omega$, we saw in Section 6.1 that, as a consequence of the Riemann mapping theorem and the Poisson formula on the disk, the Dirichlet problem (1)-(2) on $\Omega$ has a solution. It is natural to ask whether we can express this solution as an integral that depends only on the region $\Omega$ and works for any piecewise continuous boundary function $f$. Amazingly, the answer is affirmative! Our goal in this section is to derive a formula that expresses the solution as a path integral over $\Gamma$, involving the boundary function $f$ and the so-called Green's function of the region $\Omega$, which is a function that depends only on $\Omega$. The formula is named in honor of its discoverer, one of the leading mathematicians and physicists of the nineteenth century, George Green (1793-1841), who was a self-taught mathematician from England. The importance of Green's functions will be appreciated in later sections, where they will be presented as the only tools
+for solving boundary value problems on certain regions involving Poisson's equation and other important equations in applied mathematics.
+
+If you recall in Section 3.8, we used a change of variables to derive the Poisson integral on the unit disk from the mean value property of harmonic functions. We will take the same approach on $\Omega$, and so we begin by explaining the change of variables that is a key to deriving and understanding Green's functions.
+
+Suppose that $\Omega$ and $\Omega^{\prime}$ are two regions bounded by simple paths $\Gamma$ and $\Gamma^{\prime}$. Let $\phi$ be a one-to-one analytic map of $\Omega$ onto $\Omega^{\prime}$. We will further suppose that $\phi$ is analytic and one-to-one on $\Gamma$. It follows from Section 6.1 that $\phi$ maps boundary to boundary. Suppose that $F$ is a real differentiable function of two variables defined on $\Gamma^{\prime}$. We will think of complex numbers as points in the complex plane, and consider $F(z)$ for $z$ on $\Gamma^{\prime}$. We will write $\frac{\partial F}{\partial n_{\Gamma^{\prime}}}$ or simply $\frac{\partial F}{\partial n}$ to denote the directional derivative of $F$ in the direction of the outward unit normal vector to the path $\Gamma^{\prime}$. By definition, this is the dot product of the gradient of $F, \nabla F=\left(F_{x}, F_{y}\right)$, with the outward unit normal vector $n_{\Gamma}^{\prime}$. Thus
+
+$$
+\frac{\partial F}{\partial n_{\Gamma^{\prime}}}=\nabla F \cdot n_{\Gamma^{\prime}}
+$$
+
+where each expression is computed at a given point on $\Gamma^{\prime}$ (Figure 2).
+
+```scientific-figure
+id: 33d3ccec-ef39-4bb4-bf2a-981ded4847c5
+numbered: false
+title: ""
+caption: "**Figure 2.** The mapping $\\phi$ is analytic and one-to-one on $\\Omega$. It maps boundary to boundary and preserves angles."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 06 Conformal Mappings/images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-51_484_1117_1244_709.jpg
+    caption: ""
+```
+
+```scientific-figure
+id: 38a3f458-0b1a-400c-9ed3-2ce154a68fdf
+numbered: false
+title: ""
+caption: "**Figure 3.** For a circle centered at the origin, the normal derivative is the radial derivative."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 06 Conformal Mappings/images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-51_488_489_1764_55.jpg
+    caption: ""
+```
+
+Although normal derivatives are tedious to compute in general, they are easy to express in some important special cases. For example, if $\Gamma^{\prime}$ is any circle centered at the origin, then $\frac{\partial F}{\partial n_{\Gamma^{\prime}}}$ is just the radial derivative of $F$ (Figure 3):
+
+$$
+\frac{\partial F}{\partial n_{\Gamma^{\prime}}}=\frac{\partial F}{\partial r}
+$$
+
+If $F(z)=\ln |z|$ and $\Gamma^{\prime}$ is the unit circle, then for all points on the unit circle
+
+$$
+\left.\frac{\partial F}{\partial n_{\Gamma^{\prime}}}\right|_{|z|=1}=\left.\frac{\partial}{\partial r} \ln r\right|_{r=1}=\left.\frac{1}{r}\right|_{r=1}=1
+$$
+
+Our goal is to relate the normal derivative of $F$ on $\Gamma^{\prime}$ to the normal derivative of $F(\phi(z))$ on $\Gamma$. Recall that if $\phi$ is analytic and $\left|\phi^{\prime}(z)\right| \neq 0$, then $\phi$ rotates
+a path through $z$ by a fixed angle and scales by $\left|\phi^{\prime}(z)\right|$. So $\phi$ will map a normal vector to $\Gamma$ at $\zeta$ to a normal vector to $\Gamma^{\prime}$ at $\phi(\zeta)$, and it will scale its modulus by $\left|\phi^{\prime}(\zeta)\right|$. Since the normal derivative measures the rate of change of the function in the direction of the normal vector to the curve, thinking as we do with the chain rule, we expect the normal derivative of $F \circ \phi$ at $\zeta$ to equal the normal derivative of $F$ at $\phi(\zeta)$ times $\left|\phi^{\prime}(\zeta)\right|$. This expectation turns out to be correct, and we have the following change of variables formula:
+
+$$
+\frac{\partial(F \circ \phi)}{\partial n_{\Gamma}}(\zeta)=\left|\phi^{\prime}(\zeta)\right| \frac{\partial F}{\partial n_{\Gamma^{\prime}}}(\phi(\zeta)) .
+$$
+
+The proof of (3) is a nice application of conformal properties, the chain rule in two dimensions, and the Cauchy-Riemann equations. We give it at the end of this section in order not to interrupt the presentation. The importance of this formula is that it incorporates the effect of the conformal properties of analytic functions. Let us move a step closer to the desired formula for Green's functions and derive a formula that uses the boundary values of $u$ to reproduce its value at a special point inside $\Omega$. You should note the role of the mean value property of harmonic functions in the proof.
+
+<!-- Source: Lemma 1, equation (4). -->
+> [!lemma|4b5f04b0-9d32-53f2-9c90-5a528244ebc7.local at=d91b3ab8-bb1d-5cc2-ae3b-b8cbb188941f] Change of Variables
+> Suppose that $w=\phi(z)$ is a one-to-one analytic mapping of a simply connected region $\Omega$ and its boundary $\Gamma$ onto the open unit disk $D$ and its boundary $C$. Let $u$ be a bounded function harmonic on $\Omega$ and with piecewise continuous boundary limits on the boundary $\Gamma$. Let $z_{0}$ in $\Omega$ be the point such that $\phi\left(z_{0}\right)=0$. Then
+>
+> $$
+> u\left(z_{0}\right)=\frac{1}{2 \pi} \int_{\Gamma} u(\zeta) \frac{\partial \ln |\phi(\zeta)|}{\partial n} d s
+> $$
+>
+> where $d s=|d \zeta|$ is the element of arc length on $\Gamma$. Hence if $\Gamma$ is parametrized by $\gamma(t), a \leq t \leq b$, then $d s=\left|\gamma^{\prime}(t)\right| d t$. The boundary is smooth, and $\partial/\partial n$ denotes the outward normal derivative in $\zeta$.
+
+Proof We will apply (3), but first we note one useful result. (Refer to Figure 4 for help with the notation.)
+```scientific-figure
+id: 6f10ad22-2e3f-43ce-897f-ed79d1577b9c
+numbered: false
+title: ""
+caption: "**Figure 4.** If $\\phi$ is analytic and one-to-one, then $\\phi^{-1}$ is also analytic."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 06 Conformal Mappings/images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-52_524_1097_1892_786.jpg
+    caption: ""
+```
+
+The function $\phi^{-1}$ is analytic from the closed unit disk (in the $w$-plane) onto $\Omega$ and its boundary (in the $z$-plane). So the function $u\left(\phi^{-1}(w)\right)$ is harmonic on the open
+unit disk, being the composition of a harmonic function $u$ with an analytic function $\phi^{-1}$ (Theorem 3, Section 2.5). Moreover, $u\left(\phi^{-1}(w)\right)$ is piecewise continuous on $C$. Thus, by the mean value property of harmonic functions (Corollary 7, Section 3.8), we have
+
+$$
+\frac{1}{2 \pi} \int_{0}^{2 \pi} u\left(\phi^{-1}\left(e^{i t}\right)\right) d t=u\left(\phi^{-1}(0)\right)=u\left(z_{0}\right)
+$$
+
+Our goal now is to show that the integral in (4) is precisely the integral that we just evaluated in (5). Parametrize $C$ by $e^{i t}, 0 \leq t \leq 2 \pi$. Then $\Gamma$ will be parametrized by $\phi^{-1}\left(e^{i t}\right), 0 \leq t \leq 2 \pi$. The element of arc length on $\Gamma$ is
+
+$$
+\left|\frac{d}{d t} \phi^{-1}\left(e^{i t}\right)\right| d t=\left|\frac{i e^{i t}}{\phi^{\prime}\left(\phi^{-1}\left(e^{i t}\right)\right)}\right| d t=\frac{1}{\left|\phi^{\prime}\left(\phi^{-1}\left(e^{i t}\right)\right)\right|} d t
+$$
+
+Using (3) to perform the change of variables $\zeta=\phi^{-1}\left(e^{i t}\right)$, we transform the integral in (4) into
+
+$$
+\begin{gathered}
+\left.\frac{1}{2 \pi} \int_{0}^{2 \pi} u\left(\phi^{-1}\left(e^{i t}\right)\right) \frac{\partial \ln |w|}{\partial r}\right|_{w=e^{i t}}\left|\phi^{\prime}\left(\phi^{-1}\left(e^{i t}\right)\right)\right| \frac{d t}{\left|\phi^{\prime}\left(\phi^{-1}\left(e^{i t}\right)\right)\right|} \\
+=\frac{1}{2 \pi} \int_{0}^{2 \pi} u\left(\phi^{-1}\left(e^{i t}\right)\right) d t=u\left(z_{0}\right)
+\end{gathered}
+$$
+
+by (5).
+Let us note the following interesting property of the logarithm that we derived in the preceding proof: If $\phi$ is a conformal mapping of $\Gamma$ and its interior onto the unit circle $C$ and its interior, then for a point $\zeta$ on $\Gamma$ we have
+
+$$
+\left.\frac{\partial \ln |\phi(z)|}{\partial n_{\Gamma}}\right|_{z=\zeta}=\left|\phi^{\prime}(\zeta)\right|
+$$
+
+By composing $\phi$ with an appropriate linear fractional transformation, we will be able to reproduce the values of $u$ at any point inside $\Omega$, not just $z_{0}=\phi^{-1}(0)$ as shown in (4). Let $z$ be in $\Omega$ and think of $\phi(z)$ as a fixed point inside the unit disk in the $w$-plane. Consider the linear fractional transformation
+
+$$
+\tau_{z}(w)=\frac{w-\phi(z)}{1-\overline{\phi(z)} w}
+$$
+
+It is one-to-one and maps the unit disk onto the unit disk and the unit circle onto the unit circle (Example 3, Section 3.7). Let us compose $\tau_{z}$ with $\phi$ and define
+
+$$
+\Phi(z, \zeta)=\tau_{z}(\phi(\zeta))=\frac{\phi(\zeta)-\phi(z)}{1-\overline{\phi(z)} \phi(\zeta)}, \quad z, \zeta \text { in } \Omega
+$$
+
+This is a function of two variables $z$ and $\zeta$, but we will often think of it as a function of $\zeta$ alone for a fixed value of $z$. As a function of $\zeta$, it clearly maps $z$ to 0 ; that is, $\Phi(z, z)=0$ (Figure 5).
+
+```scientific-figure
+id: a346871f-7d7e-4bd3-9faa-dba9c05799dc
+numbered: false
+title: ""
+caption: "**Figure 5.** We think of $\\Phi(z, \\zeta)$ as a function of one variable $\\zeta$ in $\\Omega$, for fixed $z$ in $\\Omega$. As a function of $\\zeta, \\Phi(z, \\zeta)$ is analytic and one-to-one from $\\Omega$ onto the unit disk and takes $z$ to 0 ; that is, $\\Phi(z, z)=0$."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 06 Conformal Mappings/images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-54_554_1119_333_736.jpg
+    caption: ""
+```
+
+Using $\Phi(z, \zeta)$ in place of $\phi(\zeta)$ in (4), we are able to reproduce the value of $u$ at any point $z$ in $\Omega$.
+<!-- Source: Theorem 1, equation (9). -->
+> [!theorem|73626c8b-8bf6-5626-ab7f-b5d56507a6bc.local at=a64f3bd8-f4e9-5b3c-bb32-6159d228c043] Green Function Boundary Representation for Planar Harmonic Functions
+> Suppose that $\Omega$ is a simply connected region with boundary $\Gamma$, and $\phi$ is a one-to-one analytic function on $\Omega$ and its boundary onto the unit disk and its boundary. Let $u(z)$ be a bounded function harmonic on $\Omega$ and with piecewise continuous boundary limits on $\Gamma$. For $z$ and $\zeta$ in $\Omega$, let $\Phi(z,\zeta)=(\phi(\zeta)-\phi(z))/(1-\overline{\phi(z)}\phi(\zeta))$. Then, for any $z$ in $\Omega$, we have
+> $$
+> u(z)=\frac{1}{2 \pi} \int_{\Gamma} u(\zeta) \frac{\partial}{\partial n} \ln |\Phi(z, \zeta)| d s
+> $$
+>
+> where $d s=|d \zeta|$ is the element of arc length on $\Gamma$. The boundary is smooth; the normal derivative is outward in $\zeta$.
+
+<!-- Source: definition following Theorem 1, equation (10). -->
+> [!definition|22294c03-a159-5ada-85fa-bda8ea638b64.local at=a0780b4a-230d-5bab-9756-cb379d15b1d0] Logarithmically Normalized Dirichlet Green Function of a Simply Connected Planar Region
+> Let $\phi$ be a one-to-one analytic map of a simply connected region $\Omega$ onto the unit disk. Put $\Phi(z,\zeta)=(\phi(\zeta)-\phi(z))/(1-\overline{\phi(z)}\phi(\zeta))$.
+>
+> The function
+>
+> $$
+> G(z, \zeta)=\ln |\Phi(z, \zeta)|=\ln \left|\frac{\phi(\zeta)-\phi(z)}{1-\overline{\phi(z)} \phi(\zeta)}\right|, \quad z,\zeta\in\Omega,\ z\ne\zeta
+> $$
+>
+> is called the Green's function for the region $\Omega$.
+
+It plays a fundamental role in the solution of important partial differential equations (Laplace's equation and Poisson's equation). Formula (9) is a generalized Poisson integral formula for the simply connected region $\Omega$.
+
+Like the Poisson formulas on the disk and in the upper half-plane, formula (9) can be used to solve a general Dirichlet problem in a simply connected region $\Omega$, where the boundary data is piecewise continuous. Of course, this solution depends on the explicit formula for the conformal mapping of $\Omega$ onto the unit disk. Once this mapping is determined, Green's functions can be used to solve the Dirichlet problem. We illustrate these ideas with several examples and show how we can recapture the Poisson formulas from Green's functions.
+
+```scientific-figure
+id: 40758360-8666-4962-b104-3d4f778ca0fe
+numbered: false
+title: ""
+caption: "**Figure 6.** Green's function $G\\left(\\frac{2}{5}, \\zeta\\right)$ for the unit disk anchored at $z=\\frac{2}{5}$. Note that $G\\left(\\frac{2}{5}, \\zeta\\right)=0$ for all $\\zeta$ on the boundary and $G\\left(\\frac{2}{5}, \\zeta\\right)$ has a singularity at $\\zeta=\\frac{2}{5}$."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 06 Conformal Mappings/images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-55_360_455_243_50.jpg
+    caption: ""
+```
+
+We will often write the Green's function $G(z, \zeta)$ in terms of the real and imaginary parts of $z=x+i y$ and $\zeta=s+i t$. We will also write the Green's function using polar coordinates of $z$ and $\zeta$, where $z=r e^{i \theta}$ and $\zeta=\rho e^{i \eta}$
+
+> [!exercise|9b9a018c-cde0-5bdf-8177-8bfe96377325.local at=63f37193-50a6-51aa-bed7-fd2dab93155d] EXAMPLE 1 Green's function and Poisson formula for the disk
+> (a) Show that the Green's function for the unit disk in polar coordinates is
+>
+> $$
+> G(z, \zeta)=\ln \left|\frac{\rho e^{i \eta}-r e^{i \theta}}{1-r \rho e^{i(\eta-\theta)}}\right|, \quad \text { for } z=r e^{i \theta} \text { and } \zeta=\rho e^{i \eta}
+> $$
+>
+> As a specific illustration, we fix $z=\frac{2}{5}$ in the unit disk, and plot in Figure 6 the function $\zeta \mapsto G\left(\frac{2}{5}, \zeta\right)$, for $\zeta$ in the unit disk. This is Green's function for the unit disk anchored at a specific point $z=\frac{2}{5}$ in the unit disk.
+> (b) Derive the Poisson integral formula for the unit disk.
+
+##### solution
+
+(a) We will use (10). In this case, the conformal mapping $\phi(z)$ of the unit disk onto itself is simply $\phi(z)=z$, and so
+
+$$
+G(z, \zeta)=\ln |\Phi(z, \zeta)|=\ln \left|\frac{\phi(\zeta)-\phi(z)}{1-\overline{\phi(z)} \phi(\zeta)}\right|=\ln \left|\frac{\zeta-z}{1-\bar{z} \zeta}\right|
+$$
+
+and (11) follows upon replacing $z$ by $r e^{i \theta}$ and $\zeta$ by $\rho e^{i \eta}$.
+(b) To derive the Poisson integral formula for the unit disk, we must write out (9) when $\Gamma$ is the unit circle. In this case, $d s=d \eta$, where $0 \leq \eta \leq 2 \pi$. Using (6), we find that
 
 $$
 \begin{aligned}
-& \Delta u(z)=h(z) \quad \text { for all } z \text { in } \Omega \\
-& u(\zeta)=f(\zeta) \quad \text { for all } \zeta \text { on } \Gamma
+\frac{\partial}{\partial n} \ln \left|\frac{\zeta-z}{1-\bar{z} \zeta}\right|_{|\zeta|=1} & =\left|\frac{d}{d \zeta}\left(\frac{\zeta-z}{1-\bar{z} \zeta}\right)\right|_{\zeta=e^{i \eta}}=\left|\frac{1-|z|^{2}}{(1-\bar{z} \zeta)^{2}}\right|_{\zeta=e^{i \eta}} \\
+& =\frac{1-r^{2}}{\left|1-r e^{-i \theta} e^{i \eta}\right|^{2}}=\frac{1-r^{2}}{1-2 r \cos (\theta-\eta)+r^{2}}
 \end{aligned}
 $$
 
-
-> [!figure]
-> 
-> ![](Pasted%20image%2020260421224102.png)
-> Fig. 7.116 A Poisson problem in a region $\Omega$.
-
-
-
-
-We now express the solution of the Poisson problem on $\Omega$ in terms of Green's functions. We use the notation of the previous section and suppose that $f$ and $h$ have enough smoothness and integrability properties for the formulas in Theorems 2 and 3 to hold.
-
-
-> [!theorem] Solution of the Poisson Problem
-> Suppose that $\Omega$ is a region with boundary $\Gamma$, and let $G(z, \zeta)$ denote the Green's function for $\Omega$. If $u(z)$ is a solution of Poisson's problem (1)-(2). then
-> 
-> $$
-> u(z)=\frac{1}{2 \pi} \iint_{\Omega} h(\zeta) G(z, \zeta) d A+\frac{1}{2 \pi} \int_{\Gamma} f(\zeta) \frac{\partial}{\partial n} G(z, \zeta) d s
-> $$
-> 
-> where $d A$ is the element of area and $d s$ is the element of arc length.
-
-
-This equation models, for example, the time-independent (or steady-state) temperature distribution in a medium in the presence of heat sources. It also arises in the study of the velocity potential of an incompressible ideal fluid flow in the presence of sources or sinks. In this section we show that the solution of (7.6.1)-(7.6.2) has a simple expression in terms of the Green's function of $\Omega$. Obviously, if $h$ is identically 0 in $\Omega$, (7.6.1) reduces to Laplace's equation.
-
-
-Before we solve the problem, we would like to state the following simple but important superposition principle.
-
-
-> [!exercise] Theorem 7.6.1. (Superposition Principle)
-> 
-> Suppose that $u_1$ satisfies (7.6.1) in $\Omega$ and $u_1(\zeta)=0$ for all $\zeta$ on $\Gamma$. Suppose that $u_2$ satisfies Laplace's equation in $\Omega$ and $u_2(\zeta)=f(\zeta)$ for all $\zeta$ on $\Gamma$. Then $u=u_1+u_2$ satisfies Poisson's equation (7.6.1) with boundary conditions (7.6.2).
-
-
-The proof is immediate and is omitted. Theorem 7.6.1 allows us to decompose the general Poisson problem (7.6.1)-(7.6.2) into the sum of a Dirichlet problem with boundary values $f$ and a Poisson problem with zero boundary values as illustrated in Figure 7.117.
-
-
-
-> [!figure]
-> 
-> ![](Pasted%20image%2020260421224407.png)
-> Fig. 7.117 Decomposition of a general Poisson problem into the sum of a Poisson problem with zero boundary data plus a Dirichlet problem.
-
-
-
-We now express the solution of the Poisson problem on $\Omega$ in terms of Green's functions. We use the notation of the previous section and suppose that $f$ and $h$ have enough smoothness and integrability properties for the formulas in Theorems 2 and 3 to hold.
-
-> [!theorem] Solution of Poission Problem
-> 
-> Suppose that $\Omega$ is a region with boundary $\Gamma$, and let $G(z, \zeta)$ denote the Green's function for $\Omega$. If $u(z)$ is a solution of Poisson's problem (1)-(2), then
-> 
-> $$
-> u(z)=\frac{1}{2 \pi} \iint_{\Omega} h(\zeta) G(z, \zeta) d A+\frac{1}{2 \pi} \int_{\Gamma} f(\zeta) \frac{\partial}{\partial n} G(z, \zeta) d s
-> $$
-> 
-> where $d A$ is the element of area and $d s$ is the element of arc length.
-
-**Proof is given below**
-
-
-This form of the solution clearly illustrates the superposition principle. We recognize the second term on the right side of (3) as the solution of the Dirichlet problem on $\Omega$ with boundary values $f$ (compare with Theorem 1, Section 6.5). Looking at the other term, we also have
-
-$$
-u(z)=\frac{1}{2 \pi} \iint_{\Omega} h(\zeta) G(z, \zeta) d A
-$$
-
-as a solution of Poisson's equation (1) with zero boundary values.
-The proof of Theorem 2 is based on the following Green's identities.
-
-
-> [!theorem] Green's Identities
-> Suppose that $\Omega$ is a bounded region whose boundary $\Gamma$ consists of a finite number of simple closed positively oriented paths (as in Theorem 6, Section 3.4). Let $u(x, y)$ and $v(x, y)$ have continuous second partial derivatives on $\Omega$ and $\Gamma$. Then we have Green's first identity
-> 
-> $$
-> \iint_{\Omega}(u \Delta v+\nabla u \cdot \nabla v) d A=\int_{\Gamma} u \frac{\partial v}{\partial n} d s,
-> $$
-> 
-> and Green's second identity
-> 
-> $$
-> \iint_{\Omega}(u \Delta v-v \Delta u) d A=\int_{\Gamma}\left(u \frac{\partial v}{\partial n}-v \frac{\partial u}{\partial n}\right) d s
-> $$
-> 
-
-
-
-**Proof** We will appeal to Green's theorem from calculus. For simply connected regions, this theorem is stated in Exercise 40, Section 3.4. For multiply connected regions, the version goes as follows. Let $p(x, y)$ and $q(x, y)$ have continuous first partial derivatives in $\Omega$ and on its positively oriented boundary $\Gamma$. Then, using subscripts to denote partial derivatives, we have
-
-$$
-\iint_{\Omega}\left(p_x(x, y)+q_y(x, y)\right) d x d y=\int_{\Gamma}(p(x, y) d y-q(x, y) d x) .
-$$
-
-
-
-Apply (7) with
-
-$$
-p(x, y)=u v_x \quad \text { and } \quad q(x, y)=u v_y \text {, }
-$$
-
-and get
-
-$$
-\iint_{\Omega}\left(u\left(v_{x x}+v_{y y}\right)+\left(u_x v_x+u_y v_y\right)\right) d x d y=\int_{\Gamma} u\left(v_x d y-v_y d x\right)
-$$
-
-
-The integrand on the left is the same as the integrand on the left of (5). To understand the integrand on the right, let us recall that for a positively oriented curve parametrized by $\gamma(t)=x(t)+i y(t)$, the outward unit normal may be obtained by rotating the tangent $\gamma^{\prime}(t)=x^{\prime}(t)+i y^{\prime}(t)$ clockwise by $\frac{\pi}{2}$ and dividing by its absolute value. Hence
-
-$$
-n(t)=\frac{\gamma^{\prime}(t)}{i\left|\gamma^{\prime}(t)\right|}=\frac{1}{\left|\gamma^{\prime}(t)\right|}\left(y^{\prime}(t), x^{\prime}(t)\right) .
-$$
-
-
-Thus since the normal derivative $\frac{\partial v}{\partial n}$ is by definition the gradient of $v$ dotted with the outward unit normal vector and $d s=\left|\gamma^{\prime}(t)\right| d t$, we have
-
-$$
-\frac{\partial v}{\partial n} d s=\left(v_x, v_y\right) \cdot\left(y^{\prime}(t),-x^{\prime}(t)\right) d t=v_x d y-v_y d x
-$$
-
-which shows that the right side of (8) is the same as the right side of (5), and so (5) follows. To prove (6), we reverse the roles of $u$ and $v$ in (5) and get
-
-$$
-\iint_{\Omega}(v \Delta u+\nabla u \cdot \nabla v) d x d y=\int_{\Gamma} v \frac{\partial u}{\partial n} d s
-$$
-
-
-Subtracting this from (5), we get (6).
-
-
-+++
-
-
-Green's formulas do not hold in general on unbounded regions. Since we will use them to prove (4), we will suppose throughout the proof that $\Omega$ is bounded. Nevertheless, formula (3) can be used on unbounded regions and its validity there can be checked on a case by case basis.
-
-
-**Proof of Theorem 2** Fix $z$ in $\Omega$ and let $S_\epsilon(z)$ denote the closed disk of radius $\epsilon>0$ around $z$ in $\Omega$, and $\Omega_e=\Omega \backslash S_e$. We are going to apply Green's second identity in $\Omega_c$. By Theorem 2(iv) of Section 6.5, $G(z, \zeta)$ is a harmonic function of $\zeta$ for all $\zeta \neq z$ in $\Omega$. In particular, for $\zeta$ in $\Omega_e, \Delta G(z, \zeta)=0$, we also have $\Delta u(\zeta)=h(\zeta)$ because $u$ satisfies Poisson's equation (1). We apply Green's second identity on the region $\Omega_e$ whose boundary $\Gamma_e$ consists of $\Gamma$ and the circle $C_e(z)$ (Figure 3), taking $v=G(z, \zeta)$ and $u$ equal the solution of the Poisson problem, and get
+Plugging into (9), we find, for $z=r e^{i \theta}$ with $0 \leq r<1$,
+
+$$
+u(z)=\frac{1-r^{2}}{2 \pi} \int_{0}^{2 \pi} \frac{u\left(e^{i \eta}\right)}{1-2 r \cos (\theta-\eta)+r^{2}} d \eta
+$$
+
+which is Poisson's formula on the unit disk. $\square$
+
+Before we move to our next example, let us understand the role of $\Phi(z, \zeta)$ in (8). Since $\Phi$ is the composition of two conformal mappings, it is itself a conformal mapping of $\Omega$ onto the unit disk, and from (8) we have $\Phi(z, z)=0$. By the Riemann mapping theorem, $\Phi(z, \zeta)$ is uniquely determined by these properties, up to a unimodular multiplicative constant. In particular $|\Phi(z, \zeta)|$ is uniquely determined and so is the Green's function for the region. (The uniqueness part in the Riemann mapping theorem is not difficult to prove, and so we are not appealing to a deep result here.) Consider, for example, the linear fractional transformation
+
+$$
+\tau(\zeta)=\frac{z-\zeta}{\bar{z}-\zeta}
+$$
+
+```scientific-figure
+id: 96c58992-87c2-4567-ad75-7379abad54d5
+numbered: false
+title: ""
+caption: "**Figure 7.** Green's function $G(1+i, \\zeta)$ for the upper halfplane anchored at $z=1+i$. Note that $G(1+i, \\zeta)=0$ for all $\\zeta$ on the boundary and $G(1+i, \\zeta)$ has a singularity at $\\zeta=1+i$."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 06 Conformal Mappings/images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-56_319_529_797_106.jpg
+    caption: ""
+```
+
+```scientific-figure
+id: 45d18d09-3102-43d5-a268-5526ce8f9772
+numbered: false
+title: ""
+caption: "**Figure 8.** for Example 3."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 06 Conformal Mappings/images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-56_508_543_1954_108.jpg
+    caption: ""
+```
+
+where $z$ is in the upper half-plane. If $\zeta$ is real so that $\bar{\zeta}=\zeta$, then
+
+$$
+\left|\frac{z-\zeta}{\bar{z}-\zeta}\right|=\left|\frac{z-\zeta}{\bar{z}-\bar{\zeta}}\right|=\frac{|z-\zeta|}{|\overline{z-\zeta}|}=1
+$$
+
+Thus $\tau(\zeta)$ maps the real line onto the unit circle and since it takes $z$ onto the origin, it follows that $\tau$ maps the upper half-plane onto the unit disk, and thus $\tau(\zeta)=\Phi(z, \zeta)$ for the upper half-plane.
+
+> [!exercise|f16a7438-beec-5f78-8e2c-290a94dde11a.local at=ba29b309-63cd-5b3b-9669-43ffc8f5410e] EXAMPLE 2 Green's function and Poisson's formula in the upper halfplane
+> (a) Show that the Green's function for the upper half-plane is
+>
+> $$
+> G(z, \zeta)=\frac{1}{2} \ln \frac{(x-s)^{2}+(y-t)^{2}}{(x-s)^{2}+(y+t)^{2}}, \text { for } z=x+i y, \zeta=s+i t(y, t>0)
+> $$
+>
+> As a specific illustration, we fix $z=1+i$ in the upper half-plane, and plot in Figure 7 the function $\zeta \mapsto G(1+i, \zeta)$, for $\zeta$ in the upper half-plane. This is Green's function for the upper half-plane anchored at a specific point $z=1+i$ in the upper half-plane.
+> (b) Derive the Poisson integral formula for the upper half-plane.
+
+##### solution
+
+According to (10), Green's function for the upper half-plane is $\ln |\Phi(z, \zeta)|$ where $\Phi(z, \zeta)$ is given by (12). Thus,
+
+$$
+G(z, \zeta)=\ln \left|\frac{z-\zeta}{\bar{z}-\zeta}\right|=\frac{1}{2} \ln \frac{|z-\zeta|^{2}}{|\bar{z}-\zeta|^{2}}=\frac{1}{2} \ln \frac{(x-s)^{2}+(y-t)^{2}}{(x-s)^{2}+(-y-t)^{2}},
+$$
+
+which is equivalent to (13).
+(b) To derive Poisson's integral formula in the upper half-plane we compute the normal derivative in (9). If $\Gamma$ is the real $s$-axis, then the normal derivative is clearly the derivative in the negative direction along the imaginary $t$-axis. Thus,
+
+$$
+\frac{\partial}{\partial n} G(z, \zeta)=-\frac{1}{2} \frac{\partial}{\partial t} \ln \frac{(x-s)^{2}+(y-t)^{2}}{(x-s)^{2}+(y+t)^{2}}
+$$
+
+A straightforward calculation of the derivative, then setting $t=0$, yields
+
+$$
+\frac{\partial}{\partial n} G(z, \zeta)=\frac{2 y}{(x-s)^{2}+y^{2}}
+$$
+
+Plugging into (9) yields
+
+$$
+u(z)=\frac{y}{\pi} \int_{-\infty}^{\infty} \frac{u(s)}{(x-s)^{2}+y^{2}} d s \quad(z=x+i y)
+$$
+
+which is Poisson's formula for the upper half-plane.
+We give one more example of a Green's function.
+
+> [!exercise|31858515-bbc8-5829-ad33-a6ba67aacbf3.local at=11c6a3a7-f21a-5cae-96df-468f6db9cb51] Example 3: Green Function for a Semi-infinite Vertical Strip
+> Determine the Green function for the semi-infinite vertical strip $\Omega=\{x+iy:-\pi/2<x<\pi/2,\ y>0\}$ shown in Figure 8, using a conformal map to the upper half-plane.
+
+##### solution
+
+
+We can map the strip $\Omega$ in Figure 8 conformally onto the upper half-plane using the mapping $w=\sin z$. Composing the function (12) with this, we obtain a one-to-one
+analytic mapping of $\Omega$ onto the unit disk, taking $z$ in $\Omega$ onto the origin. Thus the Green's function for $\Omega$ is
+
+$$
+G(z, \zeta)=\ln \left|\frac{\sin z-\sin \zeta}{\overline{\sin z}-\sin \zeta}\right|
+$$
+
+$\square$
+
+We prove next some interesting properties of Green's functions.
+
+<!-- Source: Theorem 2, printed page 441; statement recovered from PDF. -->
+> [!theorem|0bf7894d-52ad-5799-bf75-03148eb29f36.local at=42dc429e-e2cb-51f6-a7e0-31b8aca25f4d] Properties of Green's Functions
+> Suppose that $\Omega$ is a simply connected region with boundary $\Gamma$, and let $\phi$ be a one-to-one analytic mapping of $\Omega$ and its boundary onto the unit disk and its boundary. Put
+>
+> $$
+> \Phi(z,\zeta)=\frac{\phi(\zeta)-\phi(z)}{1-\overline{\phi(z)}\phi(\zeta)},\qquad G(z,\zeta)=\ln|\Phi(z,\zeta)|.
+> $$
+>
+> Then the Green's function $G(z,\zeta)$ has the following properties:
+>
+> (i) $G(z,\zeta)\leq0$ for all $z$ and $\zeta$ in $\Omega$ (with the logarithmic value $-\infty$ at $z=\zeta$);
+>
+> (ii) $G(z,\zeta)=0$ for all $z$ in $\Omega$ and $\zeta$ on $\Gamma$;
+>
+> (iii) $G(z,\zeta)=G(\zeta,z)$ for all $z$ and $\zeta$ in $\Omega$ (symmetric property);
+>
+> (iv) for each $z$ in $\Omega$, there is a function $\zeta\mapsto u_1(z,\zeta)$, such that $u_1(z,\zeta)$ is harmonic for all $\zeta$ in $\Omega$, $u_1(z,\zeta)=-\ln|z-\zeta|$ for all $\zeta$ on the boundary $\Gamma$, and $G(z,\zeta)=u_1(z,\zeta)+\ln|z-\zeta|$ for all $\zeta\ne z$ in $\Omega$.
+
+
+
+```scientific-figure
+id: a25d5e5c-62a8-479b-88b9-12dba58018af
+numbered: false
+title: ""
+caption: "**Figure 9.** A Green's function $G\\left(z_{0}, \\zeta\\right)$ anchored at $z_{0}=1+i$ is the sum of a logarithm, $\\ln \\left|z_{0}-\\zeta\\right|$, and a harmonic function, $u_{1}(\\zeta)$, such that $u_{1}(\\zeta)=-\\ln \\left|z_{0}-\\zeta\\right|$ on the boundary. As a result, $G\\left(z_{0}, \\zeta\\right)$ vanishes on the boundary and has a singularity at $z_{0}$ like $\\ln \\left|z_{0}-\\zeta\\right|$."
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 06 Conformal Mappings/images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-57_427_1842_1086_41.jpg
+    caption: ""
+```
+
+Proof Fix $z$ in $\Omega$. From the definition of $\phi$ and $\Phi$ (see (7) and (8)), we have that $\Phi(z, \zeta)$ is in the open unit disk $D$ (that is, $|\Phi(z, \zeta)|<1$ ) for all $\zeta$ in $\Omega$ and $\Phi(z, \zeta)$ is on the unit circle $C$ (that is, $|\Phi(z, \zeta)|=1$ ) for all $\zeta$ on $\Gamma$. This clearly proves (i) and (ii), because $\ln |x|<0$ if $|x|<1$ and $\ln |x|=0$ if $|x|=1$. For (iii), we have
+
+$$
+G(z, \zeta)=\ln \left|\frac{\phi(\zeta)-\phi(z)}{1-\overline{\phi(z)} \phi(\zeta)}\right|=\ln \left|\frac{\phi(z)-\phi(\zeta)}{1-\overline{\phi(z)} \phi(\zeta)}\right|=\ln \left|\frac{\phi(\zeta)-\phi(z)}{1-\overline{\phi(\zeta)} \phi(z)}\right|=G(\zeta, z)
+$$
+
+To prove (iv), fix $z$ in $\Omega$ and consider
+
+$$
+\psi(z, \zeta)=\frac{\phi(\zeta)-\phi(z)}{\zeta-z} \frac{1}{1-\overline{\phi(z)} \phi(\zeta)} \quad(\zeta \neq z \text { in } \Omega)
+$$
+
+Clearly, $\psi(z, \zeta)$ is analytic for all $\zeta \neq z$ in $\Omega$. What happens as $\zeta$ approaches $z$ ? We have
+
+$$
+\lim _{\zeta \rightarrow z} \psi(z, \zeta)=\lim _{\zeta \rightarrow z} \frac{\phi(\zeta)-\phi(z)}{\zeta-z} \frac{1}{1-\overline{\phi(z)} \phi(\zeta)}=\frac{\phi^{\prime}(z)}{1-|\phi(z)|^{2}}
+$$
+
+which is finite because $|\phi(z)|<1$ and nonzero because $\phi$ is one-to-one and so $\phi^{\prime}(z) \neq 0$. Hence $\psi(z, \zeta)$ has a removable singularity at $z$ (Theorem 6, Section 4.6). By defining $\psi$ at $\zeta=z$ to be
+
+$$
+\psi(z, z)=\frac{\phi^{\prime}(z)}{1-|\phi(z)|^{2}}
+$$
+
+$\psi(z, \zeta)$ becomes analytic and nonzero for all $\zeta$ in $\Omega$. Set $u_{1}(z, \zeta)=\ln |\psi(z, \zeta)|$; then $u_{1}$ is harmonic for all $\zeta$ in $\Omega$. But for $\zeta \neq z$
+
+$$
+u_{1}(z, \zeta)=\ln |\psi(z, \zeta)|=\ln \left|\frac{\phi(\zeta)-\phi(z)}{1-\overline{\phi(z)} \phi(\zeta)}\right|-\ln |\zeta-z|=G(z, \zeta)-\ln |z-\zeta|
+$$
+
+Also, $u_{1}(z, \zeta)=-\ln |z-\zeta|$ on the boundary because $G(z, \zeta)=0$ on the boundary, and so (iv) holds.
+
+Because the function $\zeta \mapsto u_{1}(z, \zeta)$ is the solution of a Dirichlet problem in $\Omega$ with boundary values $-\ln |z-\zeta|$, if $\Omega$ is bounded, this solution is unique. Thus the representation of Green's function in Theorem 2(iv) is unique when $\Omega$ is bounded. Property (iv) in Theorem 2 can be used to define the Green's function of a domain. That is, any function $G(z, \zeta)$ that satisfies (iv) also satisfies (9).
+
+## Appendix: Proof of the change of variables formula (3)
+
+```scientific-figure
+id: 9c472289-e730-4370-9d3a-59e52f0c08fb
+numbered: false
+title: ""
+caption: "**Figure 10.** "
+captionVisible: true
+captionPosition: below
+columns: 1
+panels:
+  - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 06 Conformal Mappings/images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-58_500_529_1600_108.jpg
+    caption: ""
+```
+
+Suppose that $\gamma(t)=x(t)+i y(t)$ is a parametrization of a smooth path with $\gamma^{\prime}(t)= x^{\prime}(t)+i y(t) \neq 0$. If we assume our path has a positive orientation, then an outward unit normal may be obtained by rotating the tangent $\gamma^{\prime}(t)$ clockwise by $\pi / 2$ and dividing by its absolute value (Figure 10). Hence $n(t)=\frac{\gamma^{\prime}(t)}{i\left|\gamma^{\prime}(t)\right|}$ or
+
+$$
+n_{\Gamma}=\frac{1}{\left|\gamma^{\prime}(t)\right|}\left(y^{\prime}(t),-x^{\prime}(t)\right)
+$$
+
+Let $\phi(z)$ be as in the text preceding (3). To simplify the notation, let us write $\phi(z)=u(x, y)+i v(x, y)$, write $F$ as $F(u, v)$, and denote partial derivatives by subscripts. So
+
+$$
+(F \circ \phi)_{x}=\frac{\partial}{\partial x} F(u(x, y), v(x, y))=F_{u} u_{x}+F_{v} v_{x}
+$$
+
+where the last equality follows from the chain rule in two dimensions. Similarly,
+
+$$
+(F \circ \phi)_{y}=\frac{\partial}{\partial y} F(u(x, y), v(x, y))=F_{u} u_{y}+F_{v} v_{y}
+$$
+
+Using the definition of the normal derivative, (14), (15), and (16), we get
 
 $$
 \begin{aligned}
--\iint_{\Omega_0} G(z, \zeta) h(\zeta) d A= & \int_{\Gamma}(u(\zeta) \frac{\partial G(z, \zeta)}{\partial n}-\overbrace{G(z, \zeta)}^{=0} \frac{\partial u(\zeta)}{\partial n}) d s \\
-& +\int_{C_0(z)}\left(u(\zeta) \frac{\partial G(z, \zeta)}{\partial n}-G(z, \zeta) \frac{\partial u(\zeta)}{\partial n}\right) d s,
+\frac{\partial}{\partial n_{\Gamma}} F \circ \phi & =\nabla(F \circ \phi) \cdot n_{\Gamma}=\frac{1}{\left|\gamma^{\prime}(t)\right|}\left((F \circ \phi)_{x},(F \circ \phi)_{y}\right) \cdot\left(y^{\prime}(t),-x^{\prime}(t)\right) \\
+& =\frac{1}{\left|\gamma^{\prime}(t)\right|}\left(\left(F_{u} u_{x}+F_{v} v_{x}\right) y^{\prime}(t)-\left(F_{u} u_{y}+F_{v} v_{y}\right) x^{\prime}(t)\right)
 \end{aligned}
 $$
 
-
-
-because $G(z, \zeta)=0$ for $\zeta$ on $\Gamma$. We will let $\epsilon \downarrow 0$ and show that
+Consider now the path $\Gamma^{\prime}$, which is parametrized by
+
+$$
+\phi(\gamma(t))=u(x(t), y(t))+i v(x(t), y(t)) .
+$$
+
+Conformality ensures that the outward normal to $\phi(\gamma(t))$ is still turned clockwise from the tangent; so in analogy with (14) we obtain
 
 $$
 \begin{aligned}
-& \iint_{\Omega_*} G(z, \zeta) h(\zeta) d A \rightarrow \iint_{\Omega} G(z, \zeta) h(\zeta) d A \\
-& \int_{C_*(z)} u(\zeta) \frac{\partial G(z, \zeta)}{\partial n} d s \rightarrow-2 \pi u(z) \\
-& \int_{C_*(z)} G(z, \zeta) \frac{\partial u(\zeta)}{\partial n} d s \rightarrow 0
+n_{\Gamma^{\prime}} & =\frac{1}{\left|\frac{d}{d t} \phi(\gamma(t))\right|}\left(\frac{d}{d t} v(x(t), y(t)),-\frac{d}{d t} u(x(t), y(t))\right) \\
+& =\frac{1}{\left|\phi^{\prime}(\gamma(t)) \gamma^{\prime}(t)\right|}\left(v_{x} x^{\prime}(t)+v_{y} y^{\prime}(t),-u_{x} x^{\prime}(t)-u_{y} y^{\prime}(t)\right)
 \end{aligned}
 $$
 
-
-
-> [!figure]
-> 
-> ![](Pasted%20image%2020260421225524.png)
-> 
-
-
-
-This will imply (3) and complete the proof. Let us start with (11). Write $G(z, \zeta)= u_1(z, \zeta)+\ln |z-\zeta|$, where $u_1(z, \zeta)$ is harmonic, hence bounded by a constant $M$ in some fixed disk centered at $z$. Also, $\frac{\partial u}{\partial n}$ is bounded in this fixed disk (say, $\left|\frac{\partial u}{\partial n}\right| \leq A$ ). since $u$ has continuous partial derivatives in $\Omega$. For $\zeta$ on $C_e(z)$, we have $|z-\zeta|=t$, hence $\left|G(z, \zeta) \frac{\partial u}{\partial n}\right| \leq(M+|\ln \epsilon|) A$, and so
-
-$$
-\left|\int_{C_e(z)} G(z, \zeta) \frac{\partial u(\zeta)}{\partial n} d s\right| \leq(M+|\ln \epsilon|) A \int_{C_e(z)} d s=2 \pi \epsilon(M+|\ln \epsilon|) A \rightarrow 0, \text { as } \epsilon \rightarrow 0
-$$
-
-
-To prove (10), we note that on $C_{\varepsilon}(z)$,
-
-$$
-\frac{\partial G(z, \zeta)}{\partial n}=\frac{\partial}{\partial n}\left(u_1(z, \zeta)+\ln |z-\zeta|\right)=\frac{\partial}{\partial n} u_1(z, \zeta)-\frac{1}{\epsilon}
-$$
-
-
-Now
-
-$$
-\int_{C_*(z)} u(\zeta) \frac{\partial G(z, \zeta)}{\partial n} d s=\int_{C_*(z)} u(\zeta) \frac{\partial}{\partial n} u_1(z, \zeta) d s-\frac{1}{\epsilon} \int_{C_*(z)} u(\zeta) d s
-$$
-
-
-The first integral on the right tends to 0 as $\epsilon \rightarrow 0$, because $u(\zeta) \frac{\partial}{\partial n} u_1(z, \zeta)$ is bounded in $S_c(z)$, as in the proof of (10). To handle the second integral, note that the function $I(\epsilon)=\frac{1}{\epsilon} \int_{C_{,}(z)} u(\zeta) d s=\int_0^{2 \pi} u\left(z+\epsilon e^{i \theta}\right) d \theta$ is continuous (Theorem 5 . Section 3.5). So
-
-$$
-\lim _{\epsilon \rightarrow 0} \int_0^{2 \pi} u\left(z+\epsilon e^{i \theta}\right) d \theta=I(0)=\int_0^{2 \pi} u(z) d \theta=2 \pi u(z)
-$$
-
-which completes the proof of (10). The proof of (9) is similar (see Exercise 9).
-
-+++
-
-
-In practice, (3) is difficult to compute in its present form. In later sections, we will relate it to generalized Fourier series and offer alternative ways for computing the solution of Poisson's equation. We now turn our attention to a different problem, which can be solved using an approach similar to the one we took with Green's functions.
-
-
-# Neumann Condition and Neumann Problems
-
-
-
-When modeling heat problems in an insulated plate $\Omega$, where heat exchange on the boundary is prescribed, we are led to a boundary value problem that consists of Laplace's equation along with a condition that describes the values of the normal derivative on the boundary (Figure 4):
-
-$$
-\begin{gathered}
-\Delta u(z)=0 \text { for all } z \text { in } \Omega ; \\
-\frac{\partial u}{\partial n}(\zeta)=f(\zeta) \text { for all } \zeta \text { on } \Gamma .
-\end{gathered}
-$$
-
-
-
-
-> [!figure] Figure 4
-> ![](Pasted%20image%2020260421225715.png)
-> 
-
-
-
-Such a problem is called a Neumann problem (after the German mathematician Carl Gottfried Neumann (1832-1925)) and sometime referred to as a Dirichlet problem of the second kind. Condition (13) is known as a Neumann condition. The normal derivative at the boundary describes the rate of exchange of heat with the surrounding medium or the flux of heat across the boundary. For example, the condition $f(\zeta)=0$ corresponds to an insulated point where there is no exchange of heat with the surrounding medium. Since $f(\zeta)$ represents the flux of heat across the boundary of $u$ and $u$ represents a steady-state temperature distribution inside $\Omega$, we would expect the total flux across the boundary to be zero; that is, $f$ cannot be arbitrary, it has to satisfy the compatibility condition
-
-$$
-\int_{\Gamma} f(\zeta) d s=0
-$$
-
-
-Indeed, (14) follows from the following useful property of harmonic functions, by setting $f(\zeta)=\frac{\partial u}{\partial n}$.
-
-
-> [!proposition] Normal Derivative of Harmonic Functions
-> Suppose that $u$ is harmonic in a bounded region $\Omega$ and its boundary $\Gamma$. Then
-> 
-> $$
-> \int_{\Gamma} \frac{\partial u}{\partial n} d s=0
-> $$
-> 
-
-**Proof** Reversing the roles of $u$ and $v$ in Green's first identity (5) and then picking $v=1$, we get
-
-$$
-\iint_{\Omega} \Delta u d A=\int_{\Gamma} \frac{\partial u}{\partial n} d s
-$$
-
-
-Since $\Delta u=0$, the proposition follows.
-
-+++
-
-
-
-In a Neumann problem, we are asked to find a harmonic function given the values of its normal derivative on the boundary. Such a solution is not unique, since we can add an arbitrary constant to a solution of (12)-(13) and get another solution of (12)-(13). So now we ask: Is the solution unique up
-
-
-to an arbitrary constant? The answer is affirmative. To show this, consider the difference between two solutions, which is harmonic and has zero normal derivative on the boundary. As we now show, a function that is harmonic and has zero normal derivative is a constant.
-
-
-> [!theorem] Uniqueness of Neumann Solution
-> Suppose that $u$ is harmonic on a bounded region $\Omega$ such that $\frac{\partial u}{\partial n}=0$ on the boundary $\Gamma$ of $\Omega$. Then $u$ is identically constant in $\Omega$.
-
-
-**Proof** Suppose that $u$ is harmonic in $\Omega$ and take $u=v$ in Green's first formula, so that $\Delta v=0$ in $\Omega$, and get
-
-$$
-\iint_{\Omega}(\nabla u \cdot \nabla u) d A=\int_{\Gamma} u \frac{\partial u}{\partial n} d s=0
-$$
-
-because $\frac{\partial u}{\partial n}=0$ on $\Gamma$. Now the function $\nabla u \cdot \nabla u=\left(u_x\right)^2+\left(u_y\right)^2$ is $\geq 0$ and continuous on $\Omega$. The only way for a nonnegative continuous function to integrate to zero is to vanish identically. (This fact is proved in Lemma 1, Section 3.7 in one dimension, but the argument works in higher dimensions.) Hence $\left(u_x\right)^2+\left(u_y\right)^2$ is identically zero in $\Omega$, and so $u_x=0$ and $u_y=0$ identically in $\Omega$. Applying Theorem 1, Section 2.1, we see that $u$ is constant on $\Omega$.
-
-+++
-
-
-In order to express the solution of the Neumann problem as an integral, motivated by Green's function and the solution of the Dirichlet problem, we make the following definition.
-
-
-
-> [!definition] Neumann Functions
-> Suppose that $\Omega$ is a simply connected region with boundary $\Gamma$. A Neumann function $N(z, \zeta)(z, \zeta$ in $\Omega)$ for the region $\Omega$ is a function with the following properties:
-> (i) for each $z$ in $\Omega, N(z, \zeta)$ is harmonic for all $\zeta \neq z$ in $\Omega$;
-> (ii) $\frac{\partial N}{\partial n}(z, \zeta)=C$ for all $z$ in $\Omega$ and $\zeta$ on $\Gamma$;
-> (iii) for each $z$ in $\Omega$, there is a function $\zeta \mapsto u_1(z, \zeta)$ such that $u_1(z, \zeta)$ is harmonic for all $\zeta$ in $\Omega$, and $N(z, \zeta)=\ln |z-\zeta|+u_1(z, \zeta)$ for all $\zeta$ in $\Gamma$.
-
-
-
-Parts (i) and (iii) state that Neumann functions, like Green's functions, are harmonic inside $\Omega$ except for a singularity at $z=\zeta$, which is similar to the singularity of $\ln |z-\zeta|$. Part (ii) tells us that the boundary values of the normal derivative of the Neumann function are constant. This is the counterpart of the boundary condition for a Green's function, which states that a Green's function must vanish identically on the boundary. As we now show, the constant $C$ in (ii) depends on the length of the boundary $\Gamma$.
-
-
-
-> [!proposition]
-> The constant $C$ in Definition 1(ii), which represents the boundary value of the normal derivative of the Neumann function, is given by
-> (17)
-> 
-> $$
-> C=\frac{2 \pi}{L},
-> $$
-> 
-> where $L=\int_{\Gamma} d s$ is the length of $\Gamma$. If $L$ is infinite, we take $C=0$.
-
-
-
-**Proof** The proof is based on the following interesting property of the logarithm.
-
-
-For any fixed $z$ inside $\Omega$, we have
-
-$$
-\int_{\Gamma} \frac{\partial}{\partial n} \ln |z-\zeta| d s=2 \pi
-$$
-
-
-To sce this, let $S_\epsilon(z)$ be a disk of radius $\epsilon>0$ centered at $z$ and contained in $\Omega$, and let $C_c(z)$ denote the circle centered at $z$ with radius $\epsilon$. The function $\zeta \mapsto \ln |z-\zeta|$ is harmonic in $\Omega \backslash S_\epsilon$, so according to Proposition 1, we have
-
-$$
-0=\int_{C_{,}(z)} \frac{\partial}{\partial n} \ln |z-\zeta| d s+\int_{\Gamma} \frac{\partial}{\partial n} \ln |z-\zeta| d s
-$$
-
-
-Parametrizing $C_c(z)$ by $\zeta=z+\epsilon e^{i t}, 0 \leq t \leq 2 \pi, \frac{\partial}{\partial n} \ln |z-\zeta|=-\frac{1}{\epsilon}$ and $d s=\epsilon d t$, and so
-
-$$
-0=-\int_0^{2 \pi} d t+\int_{\Gamma} \frac{\partial}{\partial n} \ln |z-\zeta| d s
-$$
-
-implying (18). Now, using (ii) and (iii) of Definition 1, write
-
-$$
-C L=\int_{\Gamma} C d s=\int_{\Gamma} \frac{\partial N}{\partial n} d s=\overbrace{\int_{\Gamma} \frac{\partial N_1}{\partial n} d s}^{=0, \text { by Proposition } 1}+\int_{\Gamma} \frac{\partial}{\partial n} \ln |z-\zeta| d s=0+2 \pi
-$$
-
-which implies (17).
-
-+++
-
-
-Neumann functions are not unique for a region (two Neumann functions can differ by a function of $z$ and not $\zeta$; see Exercise 12). However, any Neumann function satisfying Definition 1 will work to solve a Neumann problem. Before we express the solution of the Neumann problem in terms of the Neumann function, we note that from Theorem 4 if a solution of a Neumann problem exists, then it is unique up to an additive constant.
-
-
-
-> [!theorem] Solution of Neumann Problems
-> Suppose that $\Omega$ is a region bounded by a simple path $\Gamma$, and let $N(z, \zeta)$ denote a Neumann function, where $z$ and $\zeta$ are in $\Omega$. Then, up to an additive constant, the solution $u(z)$ of the Neumann problem (12)-(14) is given by
-> 
-> $$
-> u(z)=-\frac{1}{2 \pi} \int_{\Gamma} N(z, \zeta) f(\zeta) d s
-> $$
-> 
-> 
-
-
-
-The proof of Theorem 5 is just like the proof of Theorem 2 (see Exercise 10). Now we derive some classical Neumann functions.
-
-
-
-> [!exercise] EXAMPLE 1 Neumann function for the upper half-plane
-> 
-> Show that the Neumann function for the upper half-plane is
-> 
+Thus
+
+$$
+\begin{aligned}
+\frac{\partial F}{\partial n_{\Gamma^{\prime}}} & =\nabla F \cdot n_{\Gamma^{\prime}} \\
+& =\frac{1}{\left|\gamma^{\prime}(t)\right|\left|\phi^{\prime}(\gamma(t))\right|}\left(F_{u}, F_{v}\right) \cdot\left(v_{x} x^{\prime}(t)+v_{y} y^{\prime}(t),-u_{x} x^{\prime}(t)-u_{y} y^{\prime}(t)\right)
+\end{aligned}
+$$
+
+$$
+=\frac{1}{\left|\gamma^{\prime}(t)\right|\left|\phi^{\prime}(\gamma(t))\right|}\left(F_{u}\left(v_{x} x^{\prime}(t)+v_{y} y^{\prime}(t)\right)+F_{v}\left(-u_{x} x^{\prime}(t)-u_{y} y^{\prime}(t)\right)\right) .
+$$
+
+Comparing (17) and (18) and using the Cauchy-Riemann equations, $u_{x}=v_{y}, u_{y}= -v_{x}$, we see that (3) holds.
+
+## Exercises 6.5
+
+In Exercises 1-8, derive the Green's function for the region depicted in the accompanying figure (Figures 11-18).
+
+> [!exercise|b2c66fe5-0393-5db5-80e3-0d207947dfa7.local at=51ea9d56-56db-5608-b819-c9a6150382e6] Exercise 6.5.1
+> Derive the Green function for the region shown.
+>
+> ```scientific-figure
+> id: 8e217d2c-bb2d-4a9c-b7fb-c3e7f3c412b5
+> numbered: false
+> title: ""
+> caption: "**Figure 11.** "
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 06 Conformal Mappings/images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-59_487_467_1934_48.jpg
+>     caption: ""
+> ```
+
+> [!exercise|71839c8d-ad2b-52cc-bd28-c26d445b5f81.local at=4791b8bc-4629-5969-a391-275942377ad5] Exercise 6.5.2
+> Derive the Green function for the region shown.
+>
+> ```scientific-figure
+> id: 03f9df8b-54d6-46ff-958e-a33d42c8fe85
+> numbered: false
+> title: ""
+> caption: "**Figure 12.** "
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 06 Conformal Mappings/images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-59_491_526_1932_674.jpg
+>     caption: ""
+> ```
+
+> [!exercise|d7455404-ab76-5d01-898e-f7a2999c9d53.local at=420c7708-b017-5b26-b590-758b11b2f2b9] Exercise 6.5.3
+> Derive the Green function for the region shown.
+>
+> ```scientific-figure
+> id: 2a2a29f5-2112-4a64-91f1-a0b5ca039b17
+> numbered: false
+> title: ""
+> caption: "**Figure 13.** "
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 06 Conformal Mappings/images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-59_491_538_1934_1361.jpg
+>     caption: ""
+> ```
+
+> [!exercise|870d4405-3ffe-51a2-b125-fff3f5ad9fd4.local at=d5a72d4e-bae1-5a0b-af22-1b20bb4eaaa1] Exercise 6.5.4
+> Derive the Green function for the region shown.
+>
+> ```scientific-figure
+> id: 1f11a3bd-cca0-4162-a779-8247cc6a5611
+> numbered: false
+> title: ""
+> caption: "**Figure 14.** "
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 06 Conformal Mappings/images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-60_512_526_235_94.jpg
+>     caption: ""
+> ```
+
+> [!exercise|7f741eb7-c54f-5e44-a904-a23df41e2258.local at=5eefb029-f6b1-5f2f-a0f5-ebb55f2739b0] Exercise 6.5.5
+> Derive the Green function for the region shown.
+>
+> ```scientific-figure
+> id: 7f6b347d-d215-4269-be63-f351843a8d9f
+> numbered: false
+> title: ""
+> caption: "**Figure 15.** "
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 06 Conformal Mappings/images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-60_514_528_227_771.jpg
+>     caption: ""
+> ```
+
+> [!exercise|ce7dd377-e9f1-5d00-81fd-94bb464d5162.local at=4c980329-3926-543f-a733-02ea476ba094] Exercise 6.5.6
+> Derive the Green function for the region shown.
+>
+> ```scientific-figure
+> id: 7f04e2b9-42ae-4b06-8d4c-967a035dc838
+> numbered: false
+> title: ""
+> caption: "**Figure 16.** "
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 06 Conformal Mappings/images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-60_515_547_218_1444.jpg
+>     caption: ""
+> ```
+
+> [!exercise|f6c62b20-5850-5a94-9ed4-94045a4f687b.local at=8a81242e-22a5-5ebb-b3c7-5ddee8ddb29f] Exercise 6.5.7
+> Derive the Green function for the region shown.
+>
+> ```scientific-figure
+> id: 603b2e4d-0e21-4c77-bb3d-e61e27273360
+> numbered: false
+> title: ""
+> caption: "**Figure 17.** "
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 06 Conformal Mappings/images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-60_482_533_851_102.jpg
+>     caption: ""
+> ```
+
+> [!exercise|8522e68e-37f4-53e9-ab4c-d53ffa58054c.local at=653434df-5cbc-50f1-bf76-9d0caecd1421] Exercise 6.5.8
+> Derive the Green function for the region shown.
+>
+> ```scientific-figure
+> id: a856575a-2937-4a55-8558-51cf193a98f8
+> numbered: false
+> title: ""
+> caption: "**Figure 18.** "
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 06 Conformal Mappings/images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-60_492_513_838_785.jpg
+>     caption: ""
+> ```
+
+> [!exercise|c5977880-95c3-5dac-8459-ca83bb69f6fe.local at=458287d4-a32c-5a83-a598-2672a95f64c9] Exercise 6.5.9
+> ```scientific-figure
+> id: ca724c33-4eae-4bf1-ab5e-f058d3225d68
+> numbered: false
+> title: ""
+> caption: "**Figure 19.** for Exercise 9."
+> captionVisible: true
+> captionPosition: below
+> columns: 1
+> panels:
+>   - path: Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 06 Conformal Mappings/images/7efaf102-2f40-4f0a-b342-71e0a729dc8e-60_495_549_828_1440.jpg
+>     caption: ""
+> ```
+>
+> Project Problem: Poisson's formula in the first quadrant. (a) Derive the following Poisson formula in the first quadrant for the Dirichlet problem in Figure 19, using Green's function:
+>
 > $$
 > \begin{aligned}
-> N(z, \zeta) & =\ln |z-\zeta|+\ln |\bar{z}-\zeta| \\
-> & =\frac{1}{2} \ln \left((x-s)^2+(y-t)^2\right)+\frac{1}{2} \ln \left((x-s)^2+(y+t)^2\right) .
+> u(x+i y)= & \frac{y}{\pi} \int_{0}^{\infty} f(s)\left(\frac{1}{(x-s)^{2}+y^{2}}-\frac{1}{(x+s)^{2}+y^{2}}\right) d s \\
+> & +\frac{x}{\pi} \int_{0}^{\infty} g(t)\left(\frac{1}{x^{2}+(y-t)^{2}}-\frac{1}{x^{2}+(y+t)^{2}}\right) d t
 > \end{aligned}
 > $$
-> 
-> for $z=x+i y$ and $\zeta=s+i t, y, t>0$ (Figure 5).
-> 
-
-
-
-> [!figure]
-> 
-> ![300](Pasted%20image%2020260421230708.png)
-> Figure 5 A Neumann function for the upper half-plane, anchored at $z=1+i$.
-
-
-
-**Solution** We know that $N(z, \zeta)=\ln |z-\zeta|+N_1(z, \zeta)$. Computing the normal derivative of $\ln |z-\zeta|=\frac{1}{2} \ln \left((x-s)^2+(y-t)^2\right)$ along the real axis, we find
-
-$$
--\left.\frac{d}{d t} \frac{1}{2} \ln \left((x-s)^2+(y-t)^2\right)\right|_{t=0}=\left.\frac{y-t}{(x-s)^2+(y-t)^2}\right|_{t=0}=\frac{y}{(x-s)^2+y^2} .
-$$
-
-
-By adding $\frac{1}{2} \ln |\bar{z}-\zeta|=\frac{1}{2} \ln \left((x-s)^2+(y+t)^2\right)$ to $\ln |z-\zeta|$, this adds $\frac{-y}{(x-s)^2+y^2}$ to the normal derivative along the real axis, making the normal derivative of $\left.\frac{1}{2} \ln \right\rvert\, z$ $\left.\zeta\left|+\frac{1}{2} \ln \right| \bar{z}-\zeta \right\rvert\,$ zero along the real axis. This shows that $N(z, \zeta)$ as defined by (20) has 0 normal derivative along the boundary, in accordance with Proposition 2. All other properties of the Neumann function in Definition 1 are easily verified.
-
-
-++++
-
-
-
-The fact that the normal derivative of the Neumann function of an unbounded region is zero on the boundary allows us to construct the Neumann function for this region by using the Neumann function for the upper halfplane and a change of variables via a conformal mapping. More precisely, we have the following construction, which is valid for unbounded regions.
-
-
-> [!proposition] Neumann Function for Unbounded Regions
-> Suppose that $\Omega$ is an unbounded region with boundary $\Gamma$, and $\phi$ is a one-toone analytic mapping of $\Omega$ onto the upper half-plane, taking $\Gamma$ onto the real axis. Then the Neumann function for $\Omega$ is given by
-> 
-> $$
-> N(z, \zeta)=\ln |\phi(z)-\phi(\zeta)|+\ln |\overline{\phi(z)}-\phi(\zeta)| \quad(z, \zeta \text { in } \Omega) .
-> $$
-> 
-
-
-**Proof** Fix $z$ in $\Omega$ and consider the function $F(w)=\ln |\phi(z)-w|+\ln |\overline{\phi(z)}-w|$. where $\phi(z)$ and $w$ are in the upper half-plane. By Example $1, \frac{\partial F}{\partial n}(w)=0$, for all $w$ on the real axis. Applying the change of variables formula (3), Section 6.5, it follows that $\frac{\partial F \circ \phi}{\partial n}(\zeta)=0$ for all $\zeta$ on $\Gamma$. So $N(z, \zeta)$ has the right normal derivative on the boundary $\Gamma$. Does it have the right singularity at $\zeta=z$ ? Since $\overline{o(z)}$ is in the lower half-plane, it follows that $\ln |\overline{\varphi(z)}-\phi(\zeta)|$ is harmonic for all $\zeta$ in $\Omega$. Now let us compare $\ln |\phi(z)-\phi(\zeta)|$ to $\ln |z-\zeta|$. We have
-
-$$
-\lim _{\zeta \rightarrow z}(\ln |\phi(z)-\phi(\zeta)|-\ln |z-\zeta|)=\lim _{\zeta \rightarrow z} \ln \left|\frac{\phi(z)-\phi(\zeta)}{z-\zeta}\right|=\ln \left|\phi^{\prime}(z)\right|,
-$$
-
-because $\phi$ is analytic. Since $\phi^{\prime}(z) \neq 0, \ln |\phi(z)-\phi(\zeta)|$ and $\ln |z-\zeta|$ differ by a finite constant near $z$. Hence the function $N(z, \zeta)=\ln |z-\zeta|$ plus a harmonic function in $\Omega$.
-
-
-+++
-
-
-Let us give an application of Proposition 3.
-
-
-
-> [!exercise]
-> EXAMPLE 2 Neumann function for the first quadrant
-> <span style="color:#ff0000; font-weight:bold">Exercise Statement Neededd</span>
-> 
-
-
-Applying Proposition 3 with $\phi(z)=z^2$, we obtain the Neumann function for the first quadrant (shown in Figure 6 at $z=1+i$ )
-
-$$
-\begin{aligned}
-N(z, \zeta) & =\ln \left|z^2-\zeta^2\right|+\ln \left|\overline{z^2}-\zeta^2\right| \\
-& =\ln |z-\zeta|+\ln |z+\zeta|+\ln |\bar{z}-\zeta|+\ln |\bar{z}+\zeta| .
-\end{aligned}
-$$
-
-
-> [!figure] Figure 6
-> 
-> ![](Screenshot%202026-04-21%20at%2011.13.53%20PM.png)
-> Figure 6 A Neumann function for the first quadrant, anchored at $z=1+i$. Note the singularity at $\zeta=1+i$.
-
-
-++++
-
-
-Finding Neumann functions for bounded regions is more difficult because the condition $\frac{\partial N}{\partial n}=C$ is not preserved by a conformal mapping $\phi(z)$; the normal derivative is scaled by $\left|\phi^{\prime}(z)\right|$. In the exercises, we will compute the Neumann function for the unit disk.
-
-What if we are to solve Poisson's equation (1) with Neumann boundary conditions (13)? The compatibility condition on $h$ and $f$ has already been handled by (16); it is
-
-$$
-\iint_{\Omega} h(\zeta) d A=\int_{\Gamma} f(\zeta) d s
-$$
-
-
-This problem is also solvable with the Neumann function, and for reference, we present an analog of Theorem 2.
-
-
-
-> [!theorem] Solution of Poisson-Neumann Problem
-> Suppose that $\Omega$ is a region with boundary $\Gamma$, let $N(z, \zeta)$ denote a Neumann function for this region, where $z$ and $\zeta$ are in $\Omega$. If $u(z)$ is a solution to Poisson's equation (1) subject to a Neumann boundary condition (13) and satisfying (23), then up to an additive constant
-> 
-> $$
-> u(z)=\frac{1}{2 \pi} \iint_{\Omega} h(\zeta) N(z, \zeta) d A-\frac{1}{2 \pi} \int_{\Gamma} N(z, \zeta) f(\zeta) d s
-> $$
-> 
-
-
-
-# Exercises 6.6
-
-
-> [!exercise]
-> In Exercises 1-6, derive the Neumann function for the region depicted in the accompanying figure (Figures 7-12).
-> 
-> 
-> > [!figure] Figures 7-12
-> > 
-> > ![](Pasted%20image%2020260421231529.png)
-> > 
-> > 
-> > ![](Screenshot%202026-04-21%20at%2011.15.39%20PM.png)
-> > 
-> > 
-> 
-> 
-
-
-
-
-
-
-> [!exercise]
-> 7. Uniqueness of the solution in a Poisson problem. Show that the solution of the Poisson problem in a bounded region $\Omega$ is unique. **(Hint: The difference between any two solutions is harmonic and has zero boundary values.)**
-
-
-> [!exercise]
-> 8. Neumann function for the unit disk. Show that this function is defined for $z, \zeta$ in the unit disk by
-> 
-> $$
-> N(z, \zeta)= \begin{cases}\ln |z-\zeta|+\ln \left|\frac{1}{z}-\zeta\right|+\ln |z| & \text { if } z \neq 0 \\ \ln |\zeta| & \text { if } z=0\end{cases}
-> $$
-> 
-> 
-> Derive this function by following the outlined steps.
-> (a) Write $z=r e^{i \theta}$ and $\zeta=\rho e^{i \eta}$. Fix $z \neq 0$, and show that
-> 
-> $$
-> \begin{aligned}
-> \left.\frac{\partial}{\partial n} \ln |z-\zeta|\right|_{\rho=1} & =\left.\frac{\partial}{\partial \rho} \frac{1}{2} \ln |z-\zeta|^2\right|_{\rho=1}=\left.\frac{1}{2} \frac{\partial}{\partial \rho} \ln \left(r^2+\rho^2+2 r \rho \cos (\theta-\eta)\right)\right|_{\rho=1} \\
-> & =\frac{1+r \cos (\theta-\eta)}{1+r^2+2 r \cos (\theta-\eta)}
-> \end{aligned}
-> $$
-> 
-> (b) Write $\frac{1}{\frac{1}{2}}=\frac{1}{r} e^{i \theta}$, use (a), and conclude that
-> 
-> $$
-> \left.\frac{\partial}{\partial n} \ln \left|\frac{1}{z}-\zeta\right|\right|_{\rho=1}=\frac{1+\frac{1}{r} \cos (\theta-\eta)}{\left(\frac{1}{r}\right)^2+1+2 \cos (\theta-\eta)}=\frac{r^2+r \cos (\theta-\eta)}{1+r^2+2 r \cos (\theta-\eta)} .
-> $$
-> 
-> (c) Use (a) and (b) to show that for $z \neq 0,\left.\frac{\partial}{\partial n} N(z, \zeta)\right|_{|\varsigma|=1}=1$.
-> (d) Verify the remaining properties of the Neumann function for the given $N(z, \zeta)$.
-> 
-> 
-> 
-
-
-
-
-
-> [!exercise]
-> 9. Prove (9) by justifying the following steps:
-> 
-> $$
-> \begin{aligned}
-> & \left|\iint_{\Omega_r} G(z, \zeta) h(\zeta) d A-\iint_{\Omega} G(z, \zeta) h(\zeta) d A\right| \\
-> & \quad=\left|\iint_{B_r(z)} G(z, \zeta) h(\zeta) d A\right| \\
-> & \quad \leq \iint_{B_r(z)}\left|u_1(z, \zeta) h(\zeta)\right| d A+\iint_{B_r(z)}|\ln | z-\zeta|h(\zeta)| d A \\
-> & \quad \leq C_1 \iint_{B_r(z)} d A+C_2 \iint_{C_r(z)} \ln |z-\zeta| d A \\
-> & \quad=C_1 \epsilon^2 \pi+C_2 \int_0^{2 \pi} \int_0^e r \ln |r| d r d \theta
-> \end{aligned}
-> $$
-> 
-> Evaluate the last integral and show that the resulting expression on the right side tends to 0 as $\epsilon \rightarrow 0$.
-> 
-> 
-
-
-
-> [!exercise]
-> 10. Proof of Theorem 5. In addition to the hypothesis of the theorem, we further suppose that $\int_{\Gamma} u(\zeta) d s=A$ is finite.
-> (a) For fixed $z$ in $\Omega$, let $C_e(z), S_e(z)$, and $\Gamma_{\mathrm{t}}$ be as in the proof of Theorem 2. Since $f(\zeta)=\frac{\partial u}{\partial n}$ in (19), we have
-> 
-> $$
-> \begin{aligned}
-> \int_{\Gamma} N(z, \zeta) \frac{\partial u}{\partial n} d s & =\int_{\Gamma} N(z, \zeta) \frac{\partial u}{\partial n} d s+\int_{C_*(z)} N(z, \zeta) \frac{\partial u}{\partial n} d s-\int_{C_*(z)} N(z, \zeta) \frac{\partial u}{\partial n} d s \\
-> & =\int_{\Gamma_*} N(z, \zeta) \frac{\partial u}{\partial n} d s-\int_{C_*(z)} N(z, \zeta) \frac{\partial u}{\partial n} d s \\
-> & =\int_{\Gamma_*} u(\zeta) \frac{\partial}{\partial n} N(z, \zeta) d s+\int_{C_*(z)} N(z, \zeta) \frac{\partial u}{\partial n} d s
-> \end{aligned}
-> $$
-> 
-> (b) As in the proof of (11)), show that $\int_{C_{\varepsilon}(z)} N(z, \zeta) \frac{\partial u}{\partial n} d s \rightarrow 0$ as $\epsilon \rightarrow 0$.
-> (c) Justify the following steps:
-> 
-> $$
-> \int_{\Gamma_{+}} u(\zeta) \frac{\partial}{\partial n} N(z, \zeta) d s=\int_{C_{+}(z)} u(\zeta) \frac{\partial}{\partial n} N(z, \zeta) d s+\int_{\Gamma} u(\zeta) \frac{\partial}{\partial n} N(z, \zeta) d s
-> $$
-> 
-> $\int_{C_s(z)} u(\zeta) \frac{\partial}{\partial n} N(z, \zeta) d s \rightarrow-2 \pi u(z)$ (see the proof of $\left.(10)\right)$, and $\int_{\Gamma} u(\zeta) \frac{\partial}{\partial n} N(z, \zeta) d s= C \int_{\Gamma} u(\zeta) d s=A C=C^{\prime}$, where $C$ is as in Definition 1(ii).
-> (d) Complete the proof of Theorem 5.
-> 
-> 
-
-
-
-> [!exercise]
-> 11. Proof of Theorem 6. The proof mirrors the proof in the text of Theorem 2, using Green's second identity.
-> (a) Let $\Omega_\epsilon=\Omega \backslash S_c(z)$, where $S_\epsilon(z)$ is the closed disk of radius $\epsilon>0$, centered at $z$. Apply Green's second identity to $u$ and $N$ over the region $\Omega_c$ to get
-> 
-> $$
-> \begin{aligned}
-> -\iint_{\Omega_e} N(z, \zeta) h(\zeta) d A= & C \int_{\Gamma} u(\zeta) d s-\int_{\Gamma} N(z, \zeta) \frac{\partial u}{\partial n} d s \\
-> & +\int_{C_e} u(\zeta) \frac{\partial N}{\partial n} d s-\int_{C_e} N(z, \zeta) \frac{\partial u}{\partial n} d s
-> \end{aligned}
-> $$
-> 
-> where $C$ is the fixed value of the normal derivative of $N$ along $\Gamma$.
-> (b) Argue, as in Exercise 10, that as $\epsilon \rightarrow 0$,
-> 
-> $$
-> \iint_{\Omega,} N(z, \zeta) h(\zeta) d A \rightarrow \iint_{\Omega} N(z, \zeta) h(\zeta) d A
-> $$
-> 
-> (c) Note that $C \int_{\Gamma} u(\zeta) d s$ is a constant; in fact, it is $2 \pi$ times the average value of $u$ on $\Gamma$.
-> (d) Just as we proved (10), show that $\int_{C_{\mathrm{c}}} u(\zeta) \frac{\partial N}{\partial n} d s \rightarrow-2 \pi u(z)$, as $\epsilon \rightarrow 0$.
-> (e) Just as we proved (11), show that $\int_C, N(z, \zeta) \frac{\partial u}{\partial n} d s \rightarrow 0$, as $\epsilon \rightarrow 0$.
-> (f) Complete the proof of Theorem 6.
-> 
-> 
-
-
-
-> [!exercise]
-> 12. Project Problem: On the uniqueness of the Neumann function. Suppose we have two Neumann functions $N_1(z, \zeta)$ and $N_2(z, \zeta)$ for the same region $\Omega$. They can be written in the form $N_1(z, \zeta)=\ln |z-\zeta|+u_1(z, \zeta), N_2(z, \zeta)=$
-> 
-> $\ln |z-\zeta|+u_2(z, \zeta)$, where $u_1$ and $u_2$ are harmonic functions of $\zeta$.
-> (a) Show that $N_2-N_1$ is harmonic. What is its normal derivative on $\Gamma$, the boundary of $\Omega$ ?
-> (b) Apply Theorem 4 and conclude that $N_1$ and $N_2$ differ by a constant-that is, an expression independent of $\zeta$. Can this expression depend on $z$ ?
-> (c) Conclude that $N_1(z, \zeta)$ and $N_2(z, \zeta)$ are two Neumann functions for the same region if and only if they differ by any function of $z$ alone.
-> 
-
-
-
-
-> [!exercise]
-> 13. Project Problem: Symmetry of the Neumann function. Unlike Theorem 2 of Section 6.5 for Green's functions, Definition 1 in this section for Neumann functions does not mention that they are symmetric, and in general it is not the case that $N(z, \zeta)=N(\zeta, z)$. In this problem we discover that symmetry can be recaptured by imposing an extra condition on the Neumann function, and that this can always be done without disrupting its role in the solution of the NeumannPoisson problem.
-> (a) Refer to Exercise 12. We may add a function of $z$ to a Neumann function and get another Neumann function. Let $N(z, \zeta)$ be a given Neumann function for $\Omega$. Show that we can find a function $F(z)$ and a Neumann function $N_0(z, \zeta)=N(z, \zeta)-F(z)$ such that $\int_{\Gamma} N_0(z, \zeta) d s(d s=|d \zeta|)$ is independent of $z$. (It is crucial that $\Gamma$ has finite length.)
-> (b) Applying Green's second identity to $N\left(z_1, \zeta\right)$ and $N\left(z_2, \zeta\right)$ over the region $\Omega_{\varepsilon}$ and taking the limit as $\epsilon \rightarrow 0$ (as in the proof of Theorem 2), we get
-> 
-> $$
-> N\left(z_1, z_2\right)-N\left(z_2, z_1\right)=\int_{\Gamma}\left(N\left(z_1, \zeta\right) \frac{\partial N\left(z_2, \zeta\right)}{\partial n}-N\left(z_2, \zeta\right) \frac{\partial N\left(z_1, \zeta\right)}{\partial n}\right) d s
-> $$
-> 
-> 
-> Use the fact that the normal derivative of $N(z, \zeta)$ is $C$ (a constant) and part (a) to conclude that $N_0(z, \zeta)=N_0(\zeta, z)$.
-> (c) As a double-check, replace $N(z, \zeta)$ by $N_0(z, \zeta)$ in (24) and show that the equation remains unchanged. **(Hint: Remember that $F(z)$ is a constant as far as the integration is concerned, and use the compatibility condition (23).)**
-> 
-> 
-
-
-
-
-
-> [!exercise]
-> 14. Neumann problem with odd boundary data. Consider a Neumann problem in the unit disk in which $f(\zeta)=f\left(e^{(\theta)}\right)$ is an odd function of $\theta$, where $-\pi \leq \theta \leq \pi$. Show that $u(z)=0$ for all $z$ on the real axis inside the unit disk. **(Hint: The functions $\ln \left|z-e^{i \theta}\right| f\left(e^{i \theta}\right)$ and $\ln \left|\frac{1}{z}-e^{i \theta}\right| f\left(e^{i \theta}\right)$ are odd functions of $\theta$ if $z$ is a real number.)**
-> 
-> 
-
-
-
-
-
-
-
-
-
-
+>
+> (b) Consider the special case in which $g(t)=0$. Use a symmetry argument to show that the solution in this case is the same as the restriction to the first quadrant of the solution of the Dirichlet problem in the upper half-plane with boundary data on the real axis given by $u(s)=f(s)$ if $s>0$ and $u(s)=-f(-s)$ if $s<0$.
+> (c) Consider the special case in Figure 19 in which $f(s)=0$. Use a symmetry argument to show that the solution in this case is the same as the restriction to the first quadrant of the solution of the Dirichlet problem in the right half-plane with boundary data on the imaginary axis given by $u(i t)=g(t)$ if $t>0$ and $u(i t)=-g(-t)$ if $t<0$.
+> (d) Write your answers in (b) and (c) using the Poisson integral formula for the upper half-plane and the right half-plane. Then sum the solutions to rederive your answer in (a).
+
+> [!exercise|1a6061b9-f92a-5531-a3a1-d8d39ab9578d.local at=fabe5dc0-be1c-5acb-9df1-a60e0414ece5] Exercise 6.5.10
+> Poisson's formula in a semi-infinite vertical strip. Derive Poisson's formula in the region of Example 3, using Green's function.
+
+> [!exercise|ca1d46a2-2989-590d-9a1d-1bc0135c8445.local at=5984012a-73e3-5ee2-a8ea-ec05ce2f9d6b] Exercise 6.5.11
+> By composing $\phi_{\alpha}(z)=\frac{z-\alpha}{1-\bar{\alpha} z}$ with $\psi(z)=\frac{i-z}{i+z}$, you should be able to construct your own map $\Phi(z, \zeta)$ from the upper half-plane to the disk, satisfying $\Phi(z, z)=0$.
+> (a) Find the value of $\alpha$ (it will depend on $z$ ).
+> (b) Check that your final map $\Phi(z, \zeta)$ is the same as given in this section, $\frac{z-\zeta}{\bar z-\zeta}$, times the unimodular constant $\frac{\bar z-i}{z+i}$.
+
+

`````
