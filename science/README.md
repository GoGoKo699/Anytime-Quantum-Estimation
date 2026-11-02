# Scientific reading route

The central question is not how accurately one can estimate a phase at one chosen terminal budget. Fixed-horizon quantum phase estimation already has the optimal confidence-dependent query law. The question here is whether **one continuing coherent computation can remain near that optimum at every successively finer resolution while all committed classical outputs are jointly correct**.

The answer is no by an iterated-logarithm factor.

1. [Model and results](model-and-results.md) fixes the oracle, output semantics, simultaneous confidence event, and the deterministic, finite-resolution, expected-refinement, and amplitude-estimation statements.
2. [Probability polynomials](probability-polynomials.md) proves the finite-query Fourier-bandwidth lemma under arbitrary persistent memory and adaptive instruments.
3. [Cantor propagation](cantor-propagation.md) develops a self-contained Cantor norming lemma and local propagation inequality.
4. [First-error summability](first-error-summability.md) decodes successive Cantor digits and derives the all-time lower law from disjoint first errors.
5. [Upper bounds, extensions, and boundaries](upper-bounds-extensions.md) gives matching schedules, the known-final-horizon boundary, random refinement times, optional stopping, and amplitude estimation.
6. [Expiring reversible samplers](expiring-samplers.md) transfers committed confidence to bounded local replay, including the rare-probability regime. A fresh-phase channel polynomial and actual-call blocks show that the full replay frontier pays the all-time price. [Quantum Mean Replay](https://github.com/GoGoKo699/Quantum-Mean-Replay/blob/99d19bf29d1be3f6d88edcca86f0214a9495c78b/science/anytime-confidence.md) owns the canonical shared proof.
7. [Interpretation and scope](interpretation-and-scope.md) separates inherited methods, the actual contribution, and resource-model exclusions.

The [related-work account](../references/related-work.md) records the closest external and internal comparisons. [Verification](../verification/README.md) covers finite schedule arithmetic and its limits.
