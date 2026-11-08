
# Editorial records

Reading note: 12.1 The Laplacian in Various Coordinate Systems.md

Original OCR/PDF and before-recovery snapshot are preserved. This record documents the recovery edits; formatting does not authorize changes to author wording. No Index admission was performed.

## 1. Restore author’s quadrant explanation; correct the redundant plus/minus sign.

### Before

````text
For $r>0$, the angle is determined modulo $2\pi$. A principal choice is $\theta=\operatorname{atan2}(y,x)$: use $\arctan(y/x)$ for $x>0$, add $\pi$ for $x<0,y\ge0$, and subtract $\pi$ for $x<0,y<0$. At $x=0$, take $\theta=\pi/2$ when $y>0$ and $-\pi/2$ when $y<0$. Derivatives below are taken on a continuous local angular branch away from the origin (Figure 1).
````
### After

````text
(Since the inverse tangent takes its values in the interval ( $-\pi / 2, \pi / 2$ ), we have $\theta=\tan ^{-1}\left(\frac{y}{x}\right) +k\pi$, where $k=0,1$, or -1 , depending on whether $x>0, x<0$ and $y \geq 0$, or $x<0$ and $y<0$. Also, if $x=0$, then $\theta=\pi / 2$ if $y>0$ and $-\pi / 2$ if $y<0$. See Figure 1.)
````
