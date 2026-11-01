# Upper bounds, expected refinement costs, and reductions

## Horizon-free matching construction

At stage k target error epsilon_k=3^{-k} and allocate

```math
\alpha_k=\frac{6\alpha}{\pi^2k^2}.
```
A standard fixed-confidence phase estimator costs

```math
O\!\left(
3^k[\log k+\log(1/\alpha)]
\right)
```
queries. Geometric growth makes the cumulative cost through stage k of the same order. The union bound gives one event of probability at least 1-alpha on which every stage is correct. Hold the latest completed estimate between stages. Inverting the relation between T and k yields

```math
r(T)=
O\!\left(
\frac{\log\log T+\log(1/\alpha)}{T}
\right).
```
This upper mechanism is routine; the contribution is the matching universal lower law.

## Finite K and the known-final-horizon boundary

If only K specified scales are required, equal allocation alpha/K gives

```math
T_k=
O\!\left(
3^k\log\frac{K}{\alpha}
\right),
```
matching the maximum-normalized-deadline lower bound.

If the final level K is known beforehand, choose instead a backward-geometric failure allocation proportional to alpha 3^{k-K}. Stage k then costs

```math
O\!\left(
3^k[\log(1/\alpha)+(K-k)]
\right),
```
and the geometric sum through K is

```math
O\!\left(3^K\log\frac1\alpha\right).
```
Thus emitting intermediate estimates does not by itself make the final known target more expensive. The price appears in poor normalized efficiency at some earlier scales. Modified iterative amplitude estimation is an important external illustration of this fixed-final-tolerance boundary.

## Expected refinement times

Let tau_k be increasing stopping times at which committed estimates reach precision below a3^{-k}/2 and let

```math
q_k=\sup_\theta\mathbb E_\theta[\tau_k].
```
Assume alpha<=1/4 and set Q_k=ceil(4q_k). For a Cantor prefix s use the truncated event

```math
E_{s,k}
=
\{W_1\cdots W_{k-1}=s,\;W_k=0,\;\tau_k\le Q_k\}.
```
Markov's inequality gives P_theta(tau_k>Q_k)<=1/4. On every left-child parameter, simultaneous correctness therefore gives P_theta(E_{s,k})>=1/2. The event is determined by the first Q_k queries, so its likelihood has degree at most 2Q_k. On the right child it remains a subset of the first-error event.

The deterministic proof then yields

```math
\boxed{
\sum_k e^{-D'q_k a3^{-k}}
\le B'\alpha.
}
```
The ceiling changes only constants. For any fixed alpha<1/2, use a larger truncation factor depending on the margin from one half.

## Confidence sequences and optional stopping

If intervals C_T satisfy

```math
\Pr_\theta\{\theta\in C_T\text{ for all }T\}\ge1-\alpha
```
and have deterministic diameter at most 2r(T), their midpoints reduce directly to the deterministic theorem.

For arbitrary data-dependent intervals, let tau_k be the first time their diameter falls below a3^{-k}. Midpoints at those hitting times reduce to the expected-refinement theorem whenever sup_theta E_theta tau_k is finite.

Optional stopping adds no separate penalty after simultaneous coverage is available: it merely selects one member of an already-valid sequence. The lower theorem instead constrains how quickly those valid intervals can shrink across all scales.

## Explicit amplitude-estimation reduction

Consider

```math
A_\theta=e^{-i\theta Y},
```
so

```math
A_\theta|0\rangle
=
\cos\theta|0\rangle+
\sin\theta|1\rangle,
\qquad
p(\theta)=\sin^2\theta.
```
Restrict theta to [pi/6,pi/3]. Then

```math
\frac{dp}{d\theta}
=
\sin(2\theta)
\ge\frac{\sqrt3}{2},
```
so theta=arcsin(sqrt(p)) is Lipschitz with constant at most 2/sqrt(3) on p in [1/4,3/4].

A fixed basis change diagonalizes Y. With the eigenvalues ordered appropriately, the exact identity

```math
U_\theta X U_\theta^{-1}X
=
\mathrm{diag}(e^{-i\theta},e^{i\theta}),
```
therefore simulates A_theta using parameter-independent basis changes and two phase queries. The identity includes its phase exactly, so controlling the entire construction also simulates a controlled preparation correctly. One preparation, inverse, or controlled-preparation query in this two-dimensional amplitude family costs at most two corresponding phase-oracle queries.

Clip any amplitude estimate to [1/4,3/4] and map it through arcsin(sqrt(.)); clipping cannot increase its error. An all-time amplitude envelope o(log log T/T) would therefore produce a forbidden phase envelope with only constant query overhead.

The reduction is a worst-case coherent-query statement. It does not automatically apply to copy-only tomography or to hardware models where inversion has a different physical cost.
