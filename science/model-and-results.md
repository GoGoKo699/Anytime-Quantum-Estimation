# Model and main results

## Phase-oracle model

Fix an interval I=[theta_0,theta_0+a] of width 0<a<1. Translation is immaterial, so proofs may take theta_0=0. The unknown parameter enters through

```math
U_\theta=\mathrm{diag}(1,e^{i\theta}).
```
One query is one invocation of U_theta, U_theta^{-1}, or a controlled version. The algorithm may otherwise use arbitrary parameter-independent operations, ancillas, intermediate instruments, classical feedback, and persistent quantum memory.

The resource is oracle calls, not physical evolution time or gate synthesis cost.

## Committed sequential outputs

One run emits a classical estimate hat(theta)_T after at most T oracle queries on every branch. Earlier reported values are part of the classical record and cannot be retracted.

A deterministic radius r(T) is (1-alpha)-anytime valid when

```math
\inf_{\theta\in I}
\Pr_\theta\!\left(
|\widehat\theta_T-\theta|\le r(T)
\text{ for every }T\ge1
\right)
\ge1-\alpha,
\qquad 0<\alpha<\frac12.
```
The joint event is load-bearing. Separate marginal guarantees at each fixed T are a different task.

## Theorem 1: first-error summability

Let T_1<T_2<... be deterministic query deadlines satisfying

```math
r(T_k)<\frac{a3^{-k}}2.
```
There are universal constants B,D>0 such that

```math
\boxed{
\sum_{k\ge1}
\exp[-D T_k a3^{-k}]
\le B\alpha.
}
```
The constants absorb the degree-2T convention for transcript probabilities and a fixed additive constant in the propagation lemma.

## Corollary 1: sharp all-time envelope

There is a universal c_0>0 such that every nontrivial anytime-valid deterministic envelope obeys

```math
\boxed{
\limsup_{T\to\infty}
\frac{T r(T)}{\log\log T}
\ge c_0.
}
```
Equivalently, r(T)=o(log log T/T) is impossible. A standard staged construction attains

```math
r(T)
\le
\min\!\left\{
a,
C\frac{\log\log(e^e+T)+\log(1/\alpha)}{T}
\right\},
```
so the iterated-logarithm overhead is order-optimal for maintaining a uniformly efficient all-time Heisenberg envelope.

The lower statement is infinitely-often/limsup, not a pointwise lower bound at every T.

## Corollary 2: finite number of refinement levels

If only K prescribed increasing deadlines are required, with simultaneous correctness and precision below a3^{-k}/2 at deadline k, then

```math
\sum_{k=1}^K e^{-D T_k a3^{-k}}\le B\alpha,
```
and hence

```math
\boxed{
\max_{1\le k\le K}
T_k a3^{-k}
\ge
D^{-1}\log\frac{K}{B\alpha}.
}
```
By convexity, the same order holds for the average normalized deadline.

This is **not** a theorem that T_K=Omega(3^K log K). When K is known in advance, the final target can retain O(3^K log(1/alpha)) query cost by shifting confidence budget toward the expensive late stages.

## Theorem 2: expected refinement costs

Let tau_k be increasing stopping times at which committed estimates reach precision below a3^{-k}/2, with joint correctness at least 1-alpha. Define

```math
q_k=\sup_{\theta\in I}\mathbb E_\theta[\tau_k]<\infty.
```
For alpha<=1/4, universal B',D'>0 satisfy

```math
\boxed{
\sum_k e^{-D'q_k a3^{-k}}
\le B'\alpha.
}
```
For any fixed alpha<1/2 the same statement holds with constants depending only on the margin from one half. The theorem controls expected **precision-hitting costs**, not expected width at a deterministic time.

## Corollary 3: coherent amplitude estimation

In the standard coherent amplitude-estimation interface with access to a preparation unitary A, A^{-1}, controlled versions, and a known success projector, an interior two-dimensional subfamily reduces to the phase oracle with constant query overhead. Therefore an all-time amplitude envelope o(log log T/T) is impossible as well, while standard fixed-confidence amplitude estimation supplies the matching staged upper order.

The explicit reduction is in [upper bounds, extensions, and boundaries](upper-bounds-extensions.md).
