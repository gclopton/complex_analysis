
# Chapter 17 Sampling and Discrete Fourier Analysis with Applications to Partial Differential Equations

## Topics to Review

This chapter contains numerical techniques for computing the Fourier transform and Fourier series, and for solving boundary value problems. Sections 17.1 and 17.2 deal with the sampling theorem and some of its applications. They are not required for the rest of the chapter. In Section 17.3 we present the discrete and fast Fourier transforms. In studying this section, it will help to keep in mind the basic properties of the Fourier transform as presented in Section 8.2. Similar properties will be established for the discrete Fourier transform. In Section 17.4 we show a connection between the Fourier transform and the discrete Fourier transform. To appreciate this connection, you need to do the exercises of Section 17.4 which deal with the topics of Sections 8.4 and 8.5.

## Looking Ahead

This chapter introduces basic ideas that are used in the numerical computation of Fourier transforms. With the availability of the fast Fourier transform algorithm as a standard command in many computer algebra systems, we hope that you will be able to experiment with and appreciate the effectiveness of this important algorithm. We also hope that the sample of applications that you will encounter in this chapter will entice you to explore others from the vast and diverse fields where Fourier transforms are applied.

## Introduction

> Fundamental progress has to do with the reinterpretation of basic ideas.
> — Alfred N. Whitehead

By now it is clear that the Fourier transform and Fourier series are essential tools in applications. To analyze a function with these tools requires knowledge of the function over a whole interval. In real-world applications, functions are measured over discrete sets of values, and hence they are usually given as sequences of values. To analyze these discrete functions, we will introduce and use the discrete Fourier transform. Among other important applications of the discrete Fourier transform, we will show how we can use it to approximate Fourier transforms and solve boundary value problems.

The discrete Fourier transform became widely used in the 1960s after the discovery of a numerical algorithm that gives a fast and efficient method for computing it. This algorithm is known as the fast Fourier transform. The ideas behind it date back to Gauss. But it was Cooley and Tukey who emphasized its significance to computer-based Fourier analysis.

Another topic covered in this chapter is the sampling theorem. This important result was discovered by the American engineer Claude Shannon in the 1940s. It has numerous applications to transmission and information theory.

## Sections

[[Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 17 Sampling and Discrete Fourier Analysis with Applications to Partial Differential Equations/17.1 The Sampling Theorem|17.1 The Sampling Theorem]]

[[Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 17 Sampling and Discrete Fourier Analysis with Applications to Partial Differential Equations/17.2 Partial Differential Equations and the Sampling Theorem|17.2 Partial Differential Equations and the Sampling Theorem]]

[[Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 17 Sampling and Discrete Fourier Analysis with Applications to Partial Differential Equations/17.3 The Discrete and Fast Fourier Transforms|17.3 The Discrete and Fast Fourier Transforms]]

[[Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 17 Sampling and Discrete Fourier Analysis with Applications to Partial Differential Equations/17.4 The Fourier and Discrete Fourier Transforms|17.4 The Fourier and Discrete Fourier Transforms]]
