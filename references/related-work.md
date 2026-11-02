# Related work and novelty boundary

This comparison concerns the exact coherent-query all-time theorem, not generic uses of the words online, sequential, or confidence sequence.

## Duchi and Haque: classical time-uniform estimation

John Duchi and Saminul Haque, *An information-theoretic lower bound in time-uniform estimation*, COLT 2024, PMLR 247, 1486-1500.

- https://proceedings.mlr.press/v247/duchi24a.html
- https://arxiv.org/abs/2402.08794

Their reduction encodes progressively finer parameter information in a Cantor tree and relates time-uniform estimation to sequential testing. This is the closest conceptual architecture for the first-error argument.

Their model is iid and their decisive lower step uses relative-entropy control between nearby distributions. A coherent phase oracle has no analogous universal point-hypothesis KL bound: enough coherent queries can make distinct phases exactly distinguishable. The present proof inherits the Cantor/first-error architecture but replaces the KL step by bandlimited transcript-probability propagation over adjacent Cantor cylinders.

## Mande and de Wolf: fixed-horizon phase estimation

Nikhil S. Mande and Ronald de Wolf, *Tight Bounds for Quantum Phase Estimation and Related Problems*, Quantum 10, 2140 (2026).

- https://quantum-journal.org/papers/q-2026-06-15-2140/
- https://arxiv.org/abs/2305.04908

They establish tight fixed-time confidence dependence: precision delta and failure epsilon require Theta(delta^{-1} log(1/epsilon)) applications of U and U^{-1}. Their lower bound uses trigonometric acceptance polynomials. The degree-2T transcript-likelihood lemma here is therefore an inherited quantum-query ingredient.

Their theorem is fixed horizon. It does not impose one simultaneous confidence event on an indefinite sequence of committed estimates and does not itself force first-error summability across scales.

## Iterative and modified iterative amplitude estimation

Dmitry Grinko, Julien Gacon, Christa Zoufal, and Stefan Woerner, *Iterative Quantum Amplitude Estimation*, npj Quantum Information 7, 52 (2021), arXiv:1912.05559.

Shion Fukuzawa, Christopher Ho, Sandy Irani, and Jasen Zion, *Modified Iterative Quantum Amplitude Estimation is Asymptotically Optimal*, arXiv:2208.14612.

These works establish sequential amplitude-estimation upper algorithms. Modified IQAE reaches optimal terminal order O(epsilon^{-1} log(1/alpha)) when final tolerance is known. This is an essential boundary: merely emitting intermediate estimates does not force a larger final deadline. The lower law here concerns simultaneous near-optimality across every refinement scale of an indefinitely extendable run.

## Anytime-valid quantum tomography

Aldo Cumitini, Luca Barletta, and Osvaldo Simeone, *Anytime-Valid Quantum Tomography via Confidence Sequences*, arXiv:2601.20761 (2026).

This work constructs confidence sets that remain valid throughout sequential measurements of identically prepared quantum states. It establishes that anytime-valid quantum inference is already prior art. Its resource model is measured copies and tomography, not coherent repeated access to an unknown unitary at Heisenberg query scaling.

## Other 2026 comparisons

Kaur Kristjuhan and Dominic W. Berry, *Quantum phase estimation with optimal confidence interval using three control qubits*, arXiv:2601.16474 (2026), studies efficient fixed-horizon confidence-interval phase estimation and control-register implementation.

Simon Morelli, Ricard Ravell Rodríguez, John Calsamiglia, Ramón Muñoz-Tapia, Gael Sentís, and Michalis Skotiniotis, *Quantum sequential parameter testing*, arXiv:2608.01248 (2026), studies variable-stopping continuous-parameter certification, including qubit phase and purity, under a prescribed tolerance. Its task and measured-copy resource model differ from one coherent oracle run whose entire refinement history must remain jointly valid. This comparison is based on the primary abstract; a full-text proof comparison was unavailable.

## Fractal Remez and norming theory

Alexander Brudnyi and Yuri Brudnyi, *Remez Type Inequalities and Morrey-Campanato Spaces on Ahlfors Regular Sets*, arXiv:math/0609623.

Alexander Brudnyi and Yosef Yomdin, *Norming sets and related Remez-type inequalities*, Journal of the Australian Mathematical Society 100, 163-181 (2016), DOI 10.1017/S1446788715000488.

These works place exponential-in-degree norm control on fractal and Cantor-type sets within established approximation theory. The elementary Cantor interpolation lemma in this repository keeps the proof self-contained; it is not presented as a new general result.

## Internal comparison: Online Quantum Readout

GoGoKo699/Online-Quantum-Readout studies a different online quantum-query resource: a finite known menu of observables is revealed in batches and must be answered at one fixed precision. Its source-query law depends on the request schedule, up to logarithmic factors, as

```math
\widetilde\Theta\!\left(
\frac{\min\{\sum_r\sqrt{b_r},\sqrt L\}}{\epsilon}
\right).
```
Both projects allow persistent quantum memory and committed outputs. Their online axes differ: Online Quantum Readout asks how many different observables arrive and when; Anytime Quantum Estimation asks how many successively finer resolutions of one parameter can remain uniformly efficient under one simultaneous confidence event. The inspected Online Quantum Readout proof does not imply the first-error summability law here.

## Shared result with Quantum Mean Replay

[Quantum Mean Replay](https://github.com/GoGoKo699/Quantum-Mean-Replay) studies sequential reversible samplers that expire after at most $`m`$ total local forward/inverse calls. Its constant-confidence mean-estimation frontier is $`\max\{\sqrt{p_0},1/m\}/\epsilon`$ for known probability scale $`p_0`$ and $`m\ge2`$. The source model allows arbitrary changing output garbage and unitary completions, exact within-window inverses and unrestricted persistent memory.

That frontier and this repository's phase theorem do not alone prove an all-time confidence multiplier on the replay term. The [shared transfer](../science/expiring-samplers.md) supplies the missing result: a fresh-phase channel polynomial, grouping by actual source calls and a derivative bound replace Fourier bandwidth in the Cantor propagation step. Both branches of the frontier consequently pay the simultaneous-confidence overhead. Quantum Mean Replay owns the [canonical shared proof](https://github.com/GoGoKo699/Quantum-Mean-Replay/blob/99d19bf29d1be3f6d88edcca86f0214a9495c78b/science/anytime-confidence.md); this repository records its committed-confidence consequence and exact transfer hypotheses.

Material inherited ingredients include Hu et al., *Quantum Non-Identical Mean Estimation: Efficient Algorithms and Fundamental Limits*, TQC 2024, LIPIcs 310, article 9 ([published primary source](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.TQC.2024.9)); the gearbox constructions of Wiebe--Kliuchnikov, *Floating Point Representations in Quantum Circuit Synthesis* ([arXiv:1305.5528](https://arxiv.org/abs/1305.5528)), and Wiebe--Roetteler, *Quantum arithmetic and numerical analysis using Repeat-Until-Success circuits* ([arXiv:1406.2040](https://arxiv.org/abs/1406.2040)); and Brassard et al.'s amplitude amplification ([arXiv:quant-ph/0005055](https://arxiv.org/abs/quant-ph/0005055)). Those primitives and the earlier terminal estimator are credited separately from the new all-time replay-sensitive propagation theorem.

## Review limits

Searches covered time-uniform/anytime phase and amplitude estimation, quantum confidence sequences, sequential quantum estimation, iterated-logarithm terminology, fixed-horizon phase-estimation bounds, iterative amplitude estimation, the closest internal online-readout project, bounded local replay and non-identical mean estimation. The shared sampler comparison additionally checks the receiving theorem's exact source-access, confidence and charged-call conventions. The account records what inspected sources establish; it does not certify absence of unpublished, unindexed, or concurrent work.
