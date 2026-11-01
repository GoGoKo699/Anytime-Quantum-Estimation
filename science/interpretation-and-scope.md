# Interpretation, novelty, and scope

## Operational distinction

At one terminal precision, quantum phase and amplitude estimation can achieve Heisenberg query scaling with optimal confidence dependence. The result here asks for more: one indefinitely extendable run must keep producing committed classical estimates whose entire history is jointly correct, while every reached scale remains near the fixed-horizon optimum.

The answer is that uniform efficiency is impossible without an iterated-logarithm overhead somewhere across scales.

The lower law survives arbitrary persistent quantum memory, adaptive intermediate measurements, classical feedback, controlled and inverse phase queries, and data-dependent refinement times when worst-case expected query costs are charged.

## Inherited ingredients

The project explicitly credits the following prior ingredients.

- Duchi and Haque: Cantor parameter trees, sequential testing, and first-error architecture for classical time-uniform lower bounds.
- Mande and de Wolf: tight fixed-horizon confidence dependence in quantum phase estimation and the trigonometric-polynomial method.
- Brudnyi, Brudnyi, and Yomdin: Remez/norming theory on Ahlfors-regular and Cantor-type sets. The interpolation lemma here is a specialized self-contained proof, not a new general approximation theorem.
- Grinko et al. and Fukuzawa et al.: iterative amplitude-estimation upper algorithms, including optimal terminal complexity when final tolerance is specified.
- Cumitini, Barletta, and Simeone: anytime-valid quantum tomography through confidence sequences on measured copies.
- Recent fixed-confidence and sequential quantum-estimation work: Kristjuhan-Berry phase estimation and Morelli et al. sequential parameter testing.

## Consequential remainder

The new conclusion is the coherent-query transfer:

> finite query bandwidth plus local Cantor probability propagation forces disjoint first-error probabilities to be summable, preventing a constant-overhead Heisenberg envelope from remaining valid at all successively finer committed resolutions.

Classical iid relative-entropy control does not establish this because coherent point hypotheses may become perfectly distinguishable. Fixed-time quantum polynomial lower bounds do not by themselves couple indefinitely many successive commitments.

## Claims deliberately not made

The project does not claim:

- the first quantum confidence sequence or sequential quantum estimator;
- that every individual time T requires Omega(log log T/T) error;
- a log K penalty on the last deadline when a final horizon K is known;
- a penalty for marginal confidence guarantees without one joint event;
- a lower bound for a final quantum state decoded only after the horizon is selected;
- a new general Remez inequality;
- a physical-runtime, gate-count, noise-robustness, or copy-complexity theorem.

A finite discrete phase promise can allow exact discrimination and lies outside the continuous-family lower argument.

## Resource ledger

Charged: every U_theta, U_theta^{-1}, and controlled query, including preprocessing before a reported deadline.

Allowed without query charge: parameter-independent gates, ancillas and persistent memory, adaptive classical computation, intermediate instruments, and storage of previous classical outputs.

Not analyzed: physical duration of one query, oracle decomposition, fault-tolerant overhead, device noise, memory optimization, QRAM, or data loading. The theorem requires neither QRAM nor a free data-loading interface.

## Evidence boundary

The analytical proof has been reconstructed in two separate internal checks and the finite schedule arithmetic is reproducible. That is not independent expert verification. The literature comparison is scoped; absence of a located identical theorem is not a priority certificate.
