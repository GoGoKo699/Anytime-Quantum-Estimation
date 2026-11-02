# Anytime Quantum Estimation

**What does a quantum estimator pay if every intermediate answer must remain trustworthy whenever the computation is stopped?** This project gives a sharp query-complexity law for one coherent phase-estimation run that emits committed classical estimates at progressively finer resolutions.

**Sister project: [Quantum Mean Replay](https://github.com/GoGoKo699/Quantum-Mean-Replay).** Together the projects establish the all-time confidence law for expiring reversible samplers. This repository supplies the [committed-confidence interpretation and transfer](science/expiring-samplers.md); its sister owns the [canonical joint sampler proof and charged construction](https://github.com/GoGoKo699/Quantum-Mean-Replay/blob/99d19bf29d1be3f6d88edcca86f0214a9495c78b/science/anytime-confidence.md).

For the phase oracle

```math
U_\theta=\mathrm{diag}(1,e^{i\theta}),
```
all uses of the oracle, its inverse, and controlled versions are charged. The algorithm may keep arbitrary quantum memory, make adaptive measurements, and use parameter-independent controls. A deterministic radius r(T) is anytime-valid at confidence 1-alpha if

```math
\inf_\theta
\Pr_\theta\!\left\{
|\widehat\theta_T-\theta|\le r(T)
\text{ for every query budget }T
\right\}
\ge 1-\alpha.
```
The optimal all-time shrinking envelope has order

```math
r(T)=\Theta\!\left(
\frac{\log\log T+\log(1/\alpha)}{T}
\right)
```
in the precise sense developed in the scientific account. The upper bound is a geometric schedule of standard fixed-confidence phase estimators. The lower bound shows that coherent memory and adaptive quantum control cannot remove the iterated-logarithm price of keeping **all** committed resolutions simultaneously reliable.

The stronger statement is a multiscale summability law. Let a in (0,1) be the phase-interval width. If geometric precision a 3^{-k}/2 is reached at deterministic deadlines T_k, then universal constants B,D>0 obey

```math
\sum_{k\ge1}
\exp[-D T_k a3^{-k}]
\le B\alpha.
```
Consequently,

```math
\limsup_{T\to\infty}
\frac{T r(T)}{\log\log T}>0,
```
and for K prescribed refinement levels,

```math
\max_{1\le k\le K}
T_k a3^{-k}
=
\Omega\!\left(\log\frac{K}{\alpha}\right).
```
The finite-K theorem is a tradeoff over **all normalized deadlines**, not a lower bound on the last deadline alone. If the final precision is known in advance, the usual O(epsilon^{-1} log(1/alpha)) terminal complexity remains possible. That distinction is essential.

## Joint result: expiring samplers and bounded replay

Suppose every source has the same mean $`p\in[p_0,2p_0]`$ and expires after at most $`m`$ total forward/inverse calls, with $`m\ge2`$ and known $`0\lt p_0\le1/16`$. Put $`A_m=\max\{\sqrt{p_0},1/m\}`$. Geometric committed errors $`\epsilon_k=c p_0 3^{-k}`$ obey the joint lower law

```math
\sum_k \exp[-D T_k\epsilon_k/A_m]\le B\alpha.
```

A matching schedule attains $`T_k=O(A_m\epsilon_k^{-1}[\log(k+2)+\log(1/\alpha)])`$. The replay term itself pays the confidence overhead, including $`m=2`$ and $`p_0\ll1/m^2`$. A new finite-phase / polynomial-channel argument establishes this transfer; multiplying the two earlier bounds would not establish it.

The [standalone sampler account](science/expiring-samplers.md) states the model, scientific ownership and proof dependencies. It charges actual calls and failed RUS attempts, requires classical source retirement without revisits, and preserves the distinction between multiscale efficiency and the cost of one final known target. This joint theorem is zero drift and uses deterministic pathwise deadlines; the phase model's expected-cost extension is not automatically imported.

## Read the science

Start with [the exact model and results](science/model-and-results.md), then follow the proof route:

1. [Probability polynomials](science/probability-polynomials.md): every finite-prefix transcript event has a globally bounded trigonometric-polynomial likelihood of degree at most 2T after T queries, even with adaptive instruments and persistent quantum memory.
2. [Cantor propagation](science/cantor-propagation.md): a specialized Cantor norming lemma turns finite Fourier bandwidth into a quantitative probability-propagation bound between neighboring parameter cylinders.
3. [First-error summability](science/first-error-summability.md): disjoint first-error events across successive Cantor digits yield the summability theorem and the sharp asymptotic and finite-scale consequences.
4. [Upper bounds, extensions, and boundaries](science/upper-bounds-extensions.md): matching schedules, the known-final-horizon counterboundary, expected refinement costs, confidence-sequence stopping, and the amplitude-estimation reduction.
5. [Expiring reversible samplers](science/expiring-samplers.md): joint replay-dependent confidence law, rare-event regime and charged transfer.
6. [Interpretation and scope](science/interpretation-and-scope.md): inherited ingredients, the consequential remainder, resource accounting, and excluded claims.

See [related work](references/related-work.md), [bibliographic records](references/bibliography.bib), and [verification](verification/README.md). The [LLM reading guide](llms.txt) maps questions to authoritative files.

## Learn the project

The learning route uses **Nielsen and Chuang's _Quantum Computation and Quantum Information_, 10th Anniversary Edition (2010)** as its single educational anchor, shared with Quantum Mean Replay. Start with [the phase-estimation bridge](learning/anchor-bridge.md), then follow [the 30-milestone map](learning/milestones.md). The [learning entrypoint](learning/README.md) explains the route from quantum-query foundations to the probability-propagation proof and its operational boundaries.

## Why this is not a classical theorem in new notation

Duchi and Haque established a Cantor-tree sequential-testing architecture for classical time-uniform estimation. Their lower step uses iid likelihoods and relative-entropy control between nearby hypotheses. That step does not directly transfer to a coherent phase oracle: with enough coherent queries, distinct point phases can become perfectly distinguishable.

The replacement here is a **bandlimited probability-propagation principle**. Finite query count restricts every physical transcript-event probability to a globally bounded trigonometric polynomial. A Cantor norming argument then shows that an event likely throughout one parameter child cannot become arbitrarily unlikely throughout its adjacent child unless the query budget is large relative to that child width. This supplies the missing coherent-query transfer step.

## Random refinement times and amplitude estimation

If tau_k is the data-dependent time at which the kth committed estimate reaches precision a3^{-k}/2 and

```math
q_k=\sup_\theta\mathbb E_\theta[\tau_k]<\infty,
```
then an analogous law holds at fixed confidence below one half:

```math
\sum_k \exp[-D' q_k a3^{-k}]\le B'\alpha.
```
An explicit constant-query reduction transfers the lower law to coherent amplitude estimation on an interior two-dimensional family, where p(theta)=sin^2(theta) is uniformly invertible.

## Reproduce the finite checks

From the repository root run:

    python3 verification/check_schedule.py --check verification/results.json
    python3 verification/check_anytime_replay.py --check verification/replay-schedule-results.json

The deterministic script checks the geometric confidence schedules, finite-K normalized-deadline behavior, and the known-final-horizon allocation that avoids an unnecessary final log K factor. These calculations illustrate theorem boundaries. The probability-polynomial lemma, Cantor propagation, and asymptotic lower law are analytical results and are not certified by finite enumeration.

## Scope

This is an oracle-query theorem for a continuous phase family. It does not claim a lower bound on physical evolution time, fault-tolerant gate count, state-copy complexity, or noise robustness. Outputs are committed classical estimates and the guarantee is simultaneous across one run. Marginal fixed-time correctness, a final quantum state decoded only after choosing a horizon, finitely many possible phases, and a single tolerance fixed before the run are different tasks.

Anytime-valid quantum inference itself is prior work, including confidence-sequence tomography from measured state copies. The contribution here is the sharp lower law in the coherent Heisenberg-scaling phase/amplitude query model.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
