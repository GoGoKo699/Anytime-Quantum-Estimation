# From phase estimation to trustworthy continuing estimates

## One educational anchor

Andrew M. Childs, **_Lecture Notes on Quantum Algorithms_**, dated **17 April 2025**: [author-hosted PDF](https://www.cs.umd.edu/~amchilds/qa/qa.pdf).

Use §1.1 for quantum states, §§4.1–4.3 for Fourier phase estimation, and §§21.1–21.3 for query models and the polynomial method. The section identifiers refer to that dated version. These are selected entry points, not a requirement to read the whole source.

| Foundation | Connection supplied here |
|---|---|
| A controlled unitary exposes its eigenphase | Fix a continuous, one-parameter phase oracle and charge each use. |
| Phase estimation reports an answer at a chosen precision | Require all committed answers from one continuing run to be jointly correct. |
| A query algorithm constrains acceptance polynomials | Prove a trigonometric bandwidth bound for any finite transcript event, including adaptive instruments. |

The anchor supplies the algorithmic foundations. The Cantor construction, norming estimate, probability propagation and first-error argument are developed in the repository's [scientific account](../science/README.md). Research references are attribution and proof dependencies, rather than additional educational anchors.

## Notation and charged access

The eigenvalue convention in the phase-estimation section is often written as a fraction of a full turn. Here the angle is in radians:

$$
e^{2\pi i\phi}=e^{i\theta},\qquad \theta=2\pi\phi.
$$

The unknown phase lies in an interval of width $a<1$, so the error is ordinary absolute error within that interval, with no ambiguity from wrapping around a full circle. The oracle is

$$
U_\theta=\operatorname{diag}(1,e^{i\theta}).
$$

The budget $T$ counts oracle invocations. Implementing $U_\theta^m$ by repeated access costs $m$ queries for a positive integer $m$. An inverse or controlled call also counts. Parameter-independent gates and persistent memory are allowed without query charge. Query complexity alone does not specify hardware runtime or fault-tolerant gate cost.

The estimate $\widehat\theta_T$ is classical and committed: later quantum processing cannot erase the fact that it was reported. The radius $r(T)$ is deterministic, while the estimate is random. The error budget $\alpha$ controls the probability that any reported answer fails.

## A complete one-query example

Prepare $|+\rangle=(|0\rangle+|1\rangle)/\sqrt2$, apply the oracle once, apply a Hadamard gate, and measure in the computational basis. The state before measurement is

$$
\frac{(1+e^{i\theta})|0\rangle+(1-e^{i\theta})|1\rangle}{2}.
$$

Therefore

$$
\Pr_\theta(0)=\frac{1+\cos\theta}{2},\qquad
\Pr_\theta(1)=\frac{1-\cos\theta}{2}.
$$

One oracle call turns phase into a measured probability with finite Fourier bandwidth. This particular measurement cannot distinguish opposite phase signs, and one outcome does not accurately determine a continuous parameter. Its purpose is to exhibit how the oracle enters a physical event probability. General circuits may be far more capable; their finite transcript events still have bounded bandwidth.

For $T$ queries, amplitudes are Laurent polynomials with exponents between $-T$ and $T$. Squaring and summing to obtain an event probability gives degree at most $2T$. [Probability polynomials](../science/probability-polynomials.md) proves that the same conclusion survives intermediate measurements, classical feedback and retained quantum memory. Postselecting and renormalizing a rare branch would produce a different, conditional object; the proof uses unnormalized physical event probabilities.

## One chosen answer versus one trustworthy history

At a fixed budget, an estimator can guarantee that its error is small with probability at least $1-\alpha$. Repeating that marginal statement at many times does not give the same confidence for the whole history: the failures may occur at different times on different runs.

Here the guarantee is the single event

$$
\Pr_\theta\!\left\{
|\widehat\theta_T-\theta|\le r(T)
\text{ for every }T\ge1
\right\}\ge1-\alpha.
$$

For example, assigning failure probability $\alpha/2$ to each of two stages bounds the probability of either failure by $\alpha$. This union bound does not require independent stages. Assigning failure probability $\alpha$ separately to each stage does not provide that joint guarantee. For infinitely many stages, a summable allocation such as $6\alpha/(\pi^2k^2)$ works.

Standard fixed-confidence phase estimation and geometric refinement then provide an upper envelope of order

$$
\frac{\log\log T+\log(1/\alpha)}{T}
$$

at large $T$, with the precise early-time cap in [the main results](../science/model-and-results.md). The new issue is whether a more coherent, adaptive protocol could avoid the iterated logarithm altogether.

## Why a Cantor parameter family helps

Encode the phase by digits $v_j\in\{0,1\}$:

$$
\theta=a\sum_{j\ge1}2v_j3^{-j}.
$$

Each successive digit selects the left or right third of the preceding interval. At level $k$, cylinders have width $\ell_k=a3^{-k}$ and neighboring cylinders are separated by a gap of at least that width. An estimate with error strictly below $\ell_k/2$ identifies the correct level-$k$ cylinder. The Cantor family is a hard subset of the continuous phase interval; it is not a discrete promise imposed on the estimator.

The proof needs more than distinguishing two isolated phases. Coherent queries can sometimes distinguish such point hypotheses perfectly. Instead, [Cantor propagation](../science/cantor-propagation.md) shows that a bounded finite-bandwidth event probability which is large in one child must retain average probability at least exponentially small in $T\ell_k$ on its neighbor.

For each true prefix, use the event that previous decoded digits equal that prefix and the next decoded digit is zero. It is likely on the left child. On the right child, the same event is the first wrong digit. First errors at different levels are disjoint, even when the outputs are strongly dependent. Their total probability is at most $\alpha$. Consequently, for deadlines reaching all requested precisions,

$$
\sum_k\exp[-D T_k\ell_k]\le B\alpha.
$$

The [first-error proof](../science/first-error-summability.md) supplies the prior weights and constants. A constant normalized cost $T_k\ell_k$ at every level would make this series diverge. This is the mechanism that rules out a uniformly constant-overhead all-time Heisenberg envelope.

## Read the conclusion with its quantifiers

The asymptotic lower bound is a positive lower bound on $\limsup_{T\to\infty}Tr(T)/\log\log T$. It does not lower-bound the error at every individual time. For $K$ required levels, the theorem controls the maximum or average normalized deadline, rather than the final deadline alone.

If the final level is known beforehand, giving the expensive late stages more failure budget preserves the usual terminal order. [Upper bounds and extensions](../science/upper-bounds-extensions.md) also handles expected refinement-hitting costs, optional stopping after simultaneous coverage, and the explicit constant-query amplitude-estimation reduction.

Continue with [M01–M30](milestones.md), or use [model and results](../science/model-and-results.md) for the exact theorem before following its proof dependencies.
