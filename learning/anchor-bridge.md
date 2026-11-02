# From phase estimation to trustworthy continuing estimates

## One educational anchor

Michael A. Nielsen and Isaac L. Chuang, **_Quantum Computation and Quantum Information_, 10th Anniversary Edition (2010)**, Cambridge University Press, ISBN 9781107002173. The [publisher page](https://www.cambridge.org/highereducation/books/quantum-computation-and-quantum-information/01E10196D0A682A6AEFFEA52D53BE9AE) and [official contents](https://assets.cambridge.org/97811070/02173/toc/9781107002173_toc.pdf) identify the edition and section titles. Section references below are selective foundations, rather than a requirement to read the whole book.

| Anchor sections | Foundation used here | Project bridge |
|---|---|---|
| §§2.2.2, 2.2.3, 2.2.7 and 4.3–4.4 | Unitary dynamics, measurement, relative phase and controlled circuits | Physical committed-output events, including adaptive records |
| §5.2, **Phase estimation**, and §5.2.1 | Repeated access magnifies an eigenphase and yields a terminal estimate | Charge every power, then require one continuing record to be simultaneously reliable |
| §§6.1 and 6.3, **Quantum counting** | Reflections, amplitude amplification and the amplitude–phase connection | Transfer to amplitude families and distinguish locally reusable from expired sources |
| §8.2.3, **Operator-sum representation** | Instruments, auxiliary-system measurements and completely positive maps | Average complete source-window instruments, preserving references and unnormalized outcome probabilities |
| §9.2.1, **Trace distance** | Operational distinguishability and contraction under physical channels | Keep the converse valid for arbitrary retained quantum memory |
| Appendix 1 | Basic conditional probability and averages | Distinguish marginal confidence, simultaneous coverage and first-error events |

The source supplies quantum foundations. The repository supplies the finite-transcript polynomial proof, Bernstein and Markov derivative steps, Cantor norming and first-error summability. The expiring-source extension additionally supplies its continuous finite-twirl channel family, actual-call blocks and replay-sensitive propagation. Research references give attribution and proof dependencies; they are not additional educational anchors.

## Notation and charged access

Phase estimation may write an eigenvalue as a fraction of a full turn. Here the angle is in radians:

```math
e^{2\pi i\phi}=e^{i\theta},\qquad \theta=2\pi\phi.
```
The unknown phase lies in an interval of width $`a<1`$, so the error is ordinary absolute error within that interval, with no ambiguity from wrapping around a full circle. The oracle is

```math
U_\theta=\mathrm{diag}(1,e^{i\theta}).
```
The budget $`T`$ counts oracle invocations. Implementing $`U_\theta^m`$ by repeated access costs $`m`$ queries for a positive integer $`m`$. An inverse or controlled call also counts. Parameter-independent gates and persistent memory are allowed without query charge. Query complexity alone does not specify hardware runtime or fault-tolerant gate cost.

The estimate $`\widehat\theta_T`$ is classical and committed: later quantum processing cannot erase the fact that it was reported. The radius $`r(T)`$ is deterministic, while the estimate is random. The error budget $`\alpha`$ controls the probability that any reported answer fails.

## A complete one-query example

Prepare $`|+\rangle=(|0\rangle+|1\rangle)/\sqrt2`$, apply the oracle once, apply a Hadamard gate, and measure in the computational basis. The state before measurement is

```math
\frac{(1+e^{i\theta})|0\rangle+(1-e^{i\theta})|1\rangle}{2}.
```
Therefore

```math
\Pr_\theta(0)=\frac{1+\cos\theta}{2},\qquad
\Pr_\theta(1)=\frac{1-\cos\theta}{2}.
```
One oracle call turns phase into a measured probability with finite Fourier bandwidth. This particular measurement cannot distinguish opposite phase signs, and one outcome does not accurately determine a continuous parameter. Its purpose is to exhibit how the oracle enters a physical event probability. General circuits may be far more capable; their finite transcript events still have bounded bandwidth.

For $`T`$ queries, amplitudes are Laurent polynomials with exponents between $`-T`$ and $`T`$. Squaring and summing to obtain an event probability gives degree at most $`2T`$. [Probability polynomials](../science/probability-polynomials.md) proves that the same conclusion survives intermediate measurements, classical feedback and retained quantum memory. Postselecting and renormalizing a rare branch would produce a different, conditional object; the proof uses unnormalized physical event probabilities.

## One chosen answer versus one trustworthy history

At a fixed budget, an estimator can guarantee that its error is small with probability at least $`1-\alpha`$. Repeating that marginal statement at many times does not give the same confidence for the whole history: the failures may occur at different times on different runs.

Here the guarantee is the single event

```math
\Pr_\theta\!\left\{
|\widehat\theta_T-\theta|\le r(T)
\text{ for every }T\ge1
\right\}\ge1-\alpha.
```
For example, assigning failure probability $`\alpha/2`$ to each of two stages bounds the probability of either failure by $`\alpha`$. This union bound does not require independent stages. Assigning failure probability $`\alpha`$ separately to each stage does not provide that joint guarantee. For infinitely many stages, a summable allocation such as $`6\alpha/(\pi^2k^2)`$ works.

Standard fixed-confidence phase estimation and geometric refinement then provide an upper envelope of order

```math
\frac{\log\log T+\log(1/\alpha)}{T}
```
at large $`T`$, with the precise early-time cap in [the main results](../science/model-and-results.md). The new issue is whether a more coherent, adaptive protocol could avoid the iterated logarithm altogether.

## Why a Cantor parameter family helps

Encode the phase by digits $`v_j\in\{0,1\}`$:

```math
\theta=a\sum_{j\ge1}2v_j3^{-j}.
```
Each successive digit selects the left or right third of the preceding interval. At level $`k`$, cylinders have width $`\ell_k=a3^{-k}`$ and neighboring cylinders are separated by a gap of at least that width. An estimate with error strictly below $`\ell_k/2`$ identifies the correct level-$`k`$ cylinder. The Cantor family is a hard subset of the continuous phase interval; it is not a discrete promise imposed on the estimator.

The proof needs more than distinguishing two isolated phases. Coherent queries can sometimes distinguish such point hypotheses perfectly. Instead, [Cantor propagation](../science/cantor-propagation.md) shows that a bounded finite-bandwidth event probability which is large in one child must retain average probability at least exponentially small in $`T\ell_k`$ on its neighbor.

For each true prefix, use the event that previous decoded digits equal that prefix and the next decoded digit is zero. It is likely on the left child. On the right child, the same event is the first wrong digit. First errors at different levels are disjoint, even when the outputs are strongly dependent. Their total probability is at most $`\alpha`$. Consequently, for deadlines reaching all requested precisions,

```math
\sum_k\exp[-D T_k\ell_k]\le B\alpha.
```
The [first-error proof](../science/first-error-summability.md) supplies the prior weights and constants. A constant normalized cost $`T_k\ell_k`$ at every level would make this series diverge. This is the mechanism that rules out a uniformly constant-overhead all-time Heisenberg envelope.


## From expiring sources to replay-sensitive confidence

The [expiring-sampler extension](../science/expiring-samplers.md) is readable independently of the companion. Each source supplies an unknown unitary $`U_i`$ and its exact inverse for at most $`m`$ total physical calls. After retirement it cannot be revisited; no coherent selector over source identities is supplied. The common mean is $`p\in[p_0,2p_0]`$ with known $`p_0`$. Zero drift is assumed. Forward, inverse and controlled invocations all count, including failed repeat-until-success attempts.

Section 8.2.3 supplies the language for two distinct instruments. The attaining algorithm's corrected failure restores the probe; a success adds a useful phase. The lower proof instead averages over finite nuisance phases fixed within each source window. The latter map remains a physical channel, including its classical outcomes, for every real $`p\in[0,1]`$. A successful branch normalized by its probability would not satisfy that channel premise.

For $`m=2`$, averaging at most four matrix-entry factors removes odd powers of both square roots. The resulting two-call instrument is a degree-two channel polynomial in $`p`$. In general, whole source windows are grouped until a block has made order $`m`$ actual calls. No source crosses a boundary. Channel-norm polynomial derivative bounds and block composition then replace the phase-only Fourier derivative estimate. This is the missing transfer step; a constant-confidence replay lower bound cannot simply be multiplied by the phase all-time lower bound.

The shared result uses

```math
A_m(p_0)=\max\{\sqrt{p_0},1/m\},\qquad
\sum_k\exp\!\left[-D T_k\epsilon_k/A_m(p_0)\right]
\le B\alpha.
```

The replay-sensitive propagation law supplies the $`1/m`$ branch; a clean rotation family supplies the $`\sqrt{p_0}`$ branch. The same first-error architecture then applies with its assumptions verified. Thus both branches pay the all-scale confidence price. In particular, $`m=2`$ and arbitrarily small $`p_0`$ still give order $`[\log\log T+\log(1/\alpha)]/T`$ after initialization.

The upper construction prescribes a deterministic number $`S`$ of accepted rotations and caps actual attempts at

```math
N=\left\lceil4S+16\log\frac2\beta\right\rceil.
```

For two-call attempts the physical cap is $`2N`$, including failures. General amplification costs $`2\ell N`$, with legal odd $`\ell=\Theta(\min\{m,p_0^{-1/2}\})`$. A summable outer confidence allocation produces one all-time good event. The companion owns the [canonical shared proof](https://github.com/GoGoKo699/Quantum-Mean-Replay/blob/a0eaeaba3381af105d1456f230279d47e9c26cf6/science/anytime-confidence.md); this repository owns the committed-confidence interpretation and transfer account. Neither a fixed positive drift nor an unknown scale is covered by the extension as stated.

## Read the conclusion with its quantifiers

The asymptotic lower bound is a positive lower bound on $`\limsup_{T\to\infty}Tr(T)/\log\log T`$. It does not lower-bound the error at every individual time. For $`K`$ required levels, the theorem controls the maximum or average normalized deadline, rather than the final deadline alone.

If the final level is known beforehand, giving the expensive late stages more failure budget preserves the usual terminal order. [Upper bounds and extensions](../science/upper-bounds-extensions.md) also handles expected refinement-hitting costs, optional stopping after simultaneous coverage, and the explicit constant-query amplitude-estimation reduction.

Continue with [M01–M30](milestones.md), or use [model and results](../science/model-and-results.md) for the exact theorem before following its proof dependencies.
