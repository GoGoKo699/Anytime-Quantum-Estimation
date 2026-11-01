# Transcript probability polynomials

The first proof ingredient is that quantum adaptivity does not destroy the finite Fourier bandwidth imposed by a finite number of phase-oracle calls.

## Lemma

For any event E determined by the classical transcript through at most T charged queries,

$$
p_E(\theta)=\Pr_\theta(E)
$$

is a real nonnegative trigonometric polynomial of degree at most 2T and satisfies

$$
0\le p_E(\theta)\le1
$$

for every real theta.

This remains true with arbitrary parameter-independent ancillas, adaptive instruments, classical randomization, and persistent quantum memory.

## Amplitude-polynomial proof

Coherently defer intermediate measurements and retain their records. Each query multiplies selected amplitude components by e^{i theta} or e^{-i theta}. After at most T queries every amplitude is a Laurent polynomial with exponents in [-T,T]:

$$
\sum_{j=-T}^{T} c_j e^{ij\theta}.
$$

A coarse-grained event probability is a sum of squared moduli and cross terms, so its Fourier exponents lie between -2T and 2T.

Adaptive query choices do not create new parameter dependence: they are controlled by records produced by parameter-independent maps. External classical randomness only averages coefficients.

## Density-operator audit

Grant the algorithm the stronger multiplexed one-query oracle

$$
O_\theta=\operatorname{diag}(1,e^{i\theta},e^{-i\theta})
$$

plus identity/control blocks. It can implement either query sign and can pad an early-stopping branch with an idle block.

Conjugation by one oracle call changes a density-operator Fourier exponent by at most two. Inductively, the unnormalized state associated with any finite record after T calls has form

$$
\rho_T(\theta)
=
\sum_{j=-2T}^{2T}e^{ij\theta}R_j,
$$

with operator coefficients R_j independent of theta. Every parameter-independent completely positive map preserves this span. Tracing the record event E yields p_E.

## Why bandwidth replaces iid likelihood control

Classical time-uniform lower bounds can compare nearby fixed distributions with relative entropy. That route is not universal under coherent phase queries: distinct point phases may become exactly distinguishable after enough queries.

What remains universal is **bandwidth**. A finite query budget restricts every physical transcript-event likelihood to a globally bounded trigonometric polynomial. The next step exploits this rigidity over a neighboring continuum of parameters rather than through pairwise KL divergence.

## Scope

The theorem is stated for the conventional finite-query circuit/instrument model. Continuous-outcome coarse grainings can be handled by integrating the finitely many Fourier coefficients. The lower bound uses a fixed eigenbasis and supplied eigenstate, so a broader task with additional advice cannot invalidate the hard subfamily.
