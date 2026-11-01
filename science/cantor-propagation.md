# Cantor norming and local probability propagation

The second proof ingredient turns finite Fourier bandwidth into a local statement: an event that has substantial probability on one small Cantor parameter child cannot have exponentially smaller average probability on its adjacent child unless the query budget resolves that scale.

## Cantor measure

Let mu be the middle-thirds Cantor probability measure on

$$
C=
\left\{
\sum_{j\ge1}2v_j3^{-j}:v_j\in\{0,1\}
\right\}
\subset[0,1],
$$

and let d=log 2/log 3. Every interval J with |J|<=1 obeys

$$
\mu(J)\le4|J|^d.
$$

Indeed, choose m with 3^{-(m+1)}<=|J|<3^{-m}. The interval meets at most two level-m cylinders, so its mass is at most 2*2^{-m}<=4|J|^d.

## Specialized polynomial norming lemma

There is a universal A>1 such that, for every real polynomial P of degree m>=1 and every z in [-2,1],

$$
\boxed{
|P(z)|
\le
A^m\int_C|P(x)|\,d\mu(x).
}
$$

This is a self-contained specialization of established Remez/norming theory on fractal sets.

### Quantile-interpolation proof

Let

$$
L=\int_C|P(x)|\,d\mu(x).
$$

Partition the atomless Cantor measure into 2(m+1) consecutive equal-mass bins and select every other bin. From selected bin j choose x_j with

$$
|P(x_j)|\le2(m+1)L.
$$

For j>i, the measure between chosen bins is at least (j-i)/(2(m+1)). The Frostman bound gives

$$
|x_j-x_i|
\ge
\left(\frac{j-i}{8(m+1)}\right)^{1/d}.
$$

Hence the jth Lagrange denominator is at least

$$
\left(
\frac{j!(m-j)!}{[8(m+1)]^m}
\right)^{1/d}
\ge
(32e)^{-m/d}.
$$

For z in [-2,1] and x_i in [0,1], every numerator factor is at most three. Thus each Lagrange basis value is at most exponential in m, and summing the m+1 interpolation terms yields the displayed norming inequality after increasing the universal base A.

The point is transparency, not a new general Remez theorem.

## Local propagation lemma

Let p be a real trigonometric polynomial of degree N with 0<=p<=1 on the full circle. Let nu be an affine Cantor measure on [b,b+ell]. If z lies in [b-2ell,b+ell] and p(z)>=1/2, then universal c,C>0 obey

$$
\boxed{
\int p(\theta)\,d\nu(\theta)
\ge
c\exp[-C(N\ell+1)].
}
$$

### Proof

Bernstein's inequality gives

$$
\|p^{(j)}\|_\infty\le N^j.
$$

Taylor-expand p about b to ordinary polynomial degree m. On [b-2ell,b+ell], the remainder satisfies

$$
R
\le
\frac{(2N\ell)^{m+1}}{(m+1)!}
\le
\left(\frac{2eN\ell}{m+1}\right)^{m+1}.
$$

Choose m=ceil(K(N ell+1)) with one sufficiently large universal K, so R<=(4A)^{-m}. After affine rescaling, apply the Cantor norming lemma to the Taylor polynomial. Since p(z)>=1/2,

$$
\frac12
\le
A^m\left(\int p\,d\nu+R\right)+R.
$$

Therefore

$$
\int p\,d\nu
\ge\frac14 A^{-m},
$$

which has the claimed exponential form.

For a T-query transcript event, N<=2T. Thus a constant event probability on one child forces average probability at least exp[-O(T ell+1)] on its neighbor. This is the quantum replacement for the unavailable iid-KL step.
