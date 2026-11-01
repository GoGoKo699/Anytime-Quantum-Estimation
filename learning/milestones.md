# A 30-milestone understanding map

The map follows one question: what prevents a continuing coherent quantum estimator from making every committed resolution as efficient as a separately chosen terminal estimate?

There are **13 background/preliminaries milestones** and **17 narrative/innovation milestones**. The background assembles quantum access, joint probability, bandwidth and Cantor geometry into the exact task. The narrative connects local propagation to a global resource law and then tests its operational boundaries. This allocation reflects the several mathematical ingredients needed for one central mechanism. Within each phase, the route moves from individual objects to an integrated account.

The single educational anchor is Childs's _Lecture Notes on Quantum Algorithms_, 17 April 2025, with the [section and notation bridge](anchor-bridge.md). A pointer to the bridge's local derivation means that the anchor does not supply that ingredient. The targets express global understanding; specialist proof details remain in `science/`.

## Background and preliminaries: M01–M13

### M01 — An observable relative phase

- **Central question:** How can an eigenphase affect a measurement?
- **Understanding target:** Explain phase relative to a reference component, and distinguish it from a physically irrelevant global phase.
- **Dependencies and story role:** None; introduces the parameter the whole task estimates.
- **Conceptual connection:** A controlled phase query makes an unknown angle accessible through interference.
- **Sources:** Childs §1.1 and §4.3; [oracle model](../science/model-and-results.md#phase-oracle-model).

### M02 — A physical event probability

- **Central question:** What does one phase query reveal?
- **Understanding target:** Follow the preparation, oracle, Hadamard and measurement example, including its sign ambiguity.
- **Dependencies and story role:** M01; turns a phase into a concrete classical event.
- **Conceptual connection:** The cosine likelihood foreshadows finite Fourier bandwidth.
- **Sources:** Childs §1.1; [one-query example](anchor-bridge.md#a-complete-one-query-example).

### M03 — The query ledger

- **Central question:** Which operations consume the resource?
- **Understanding target:** Charge powers, inverse calls and controlled calls while separating query count from gates and physical duration.
- **Dependencies and story role:** M01–M02; fixes the comparison before discussing efficiency.
- **Conceptual connection:** High coherent powers amplify phase only by using the charged access.
- **Sources:** Childs §4.3 and §21.2; [resource ledger](../science/interpretation-and-scope.md#resource-ledger).

### M04 — A terminal phase estimate

- **Central question:** What is already possible at one chosen precision?
- **Understanding target:** Explain inverse-precision query scaling and the role of a separate confidence requirement.
- **Dependencies and story role:** M03; establishes the inherited terminal baseline.
- **Conceptual connection:** Fourier phase estimation supplies an estimator; the optimal confidence dependence comes from the cited research literature.
- **Sources:** Childs §§4.1–4.3; [fixed-horizon comparison](../references/related-work.md#mande-and-de-wolf-fixed-horizon-phase-estimation).

### M05 — Error and confidence are different

- **Central question:** What can fail in a claimed accurate estimate?
- **Understanding target:** Distinguish the unknown phase, random estimate, deterministic radius and failure probability.
- **Dependencies and story role:** M04; makes the statistical statement precise.
- **Conceptual connection:** A smaller radius is not a stronger guarantee unless its coverage is specified.
- **Sources:** [notation bridge](anchor-bridge.md#notation-and-charged-access); [committed outputs](../science/model-and-results.md#committed-sequential-outputs).

### M06 — A guarantee for an entire history

- **Central question:** Why do marginal guarantees not imply simultaneous correctness?
- **Understanding target:** Use a union bound without independence and distinguish one joint event from separately reliable answers.
- **Dependencies and story role:** M05; introduces the operational demand driving the result.
- **Conceptual connection:** Confidence must cover the committed record of a single run.
- **Sources:** [trustworthy history](anchor-bridge.md#one-chosen-answer-versus-one-trustworthy-history); [joint event](../science/model-and-results.md#committed-sequential-outputs).

### M07 — Adaptive quantum memory and classical records

- **Central question:** What freedom does the lower bound allow the algorithm?
- **Understanding target:** Explain intermediate instruments, feedback, retained memory and immutable reported values.
- **Dependencies and story role:** M03 and M06; prevents a restart-only interpretation of the theorem.
- **Conceptual connection:** Powerful internal coherence coexists with a classical event in the observable transcript.
- **Sources:** Childs §21.2 as a query-model entry point; [adaptive event proof](../science/probability-polynomials.md).

### M08 — Finite queries imply finite bandwidth

- **Central question:** Why is a transcript event's likelihood a trigonometric polynomial?
- **Understanding target:** Track Laurent exponents through queries and explain why probabilities have degree at most twice the query count.
- **Dependencies and story role:** M02–M03 and M07; supplies the universal quantum constraint.
- **Conceptual connection:** The polynomial-method idea extends from a terminal acceptance bit to a finite transcript event.
- **Sources:** Childs §21.3; [amplitude and density proofs](../science/probability-polynomials.md).

### M09 — Global probability bounds control derivatives

- **Central question:** Why is being a physical probability important beyond polynomial degree?
- **Understanding target:** Explain how a globally bounded trigonometric polynomial obeys Bernstein derivative bounds.
- **Dependencies and story role:** M08; prepares the local Taylor approximation.
- **Conceptual connection:** The range from zero to one supplies analytic rigidity, even outside the promised phase interval.
- **Sources:** [local propagation proof](../science/cantor-propagation.md#local-propagation-lemma); [global event bound](../science/probability-polynomials.md#lemma).

### M10 — Refinement as Cantor digits

- **Central question:** How can a continuous parameter encode a sequence of bits?
- **Understanding target:** Identify cylinder widths, gaps and prefixes in a scaled middle-thirds Cantor family.
- **Dependencies and story role:** M05; gives refinement levels a nested geometric meaning.
- **Conceptual connection:** Sufficiently accurate estimates identify successive digits on a hard continuum subset.
- **Sources:** [Cantor bridge](anchor-bridge.md#why-a-cantor-parameter-family-helps); [encoding](../science/first-error-summability.md#encode-the-phase-by-cantor-digits).

### M11 — Cantor mass and separated nodes

- **Central question:** How can an interval's length constrain its prior mass?
- **Understanding target:** Explain the Frostman mass bound and why equal-mass bins contain well-separated interpolation nodes.
- **Dependencies and story role:** M10; relates probability over parameters to geometry.
- **Conceptual connection:** Cantor dimension replaces ordinary length as the scale of available mass.
- **Sources:** [Cantor measure and interpolation](../science/cantor-propagation.md#cantor-measure).

### M12 — An inherited norming estimate

- **Central question:** How does small average polynomial size constrain a nearby value?
- **Understanding target:** Explain the role of Lagrange interpolation and exponential-in-degree norm control without claiming a new general Remez theorem.
- **Dependencies and story role:** M11; completes the approximation-theory ingredient.
- **Conceptual connection:** A fractal prior can still constrain an ordinary polynomial away from its support.
- **Sources:** [specialized norming lemma](../science/cantor-propagation.md#specialized-polynomial-norming-lemma); [attribution](../references/related-work.md#fractal-remez-and-norming-theory).

### M13 — Assemble the precise estimation task

- **Central question:** Which assumptions must be present together?
- **Understanding target:** State continuous phase access, charged queries, committed outputs and one simultaneous confidence event, and identify what the model leaves uncharged.
- **Dependencies and story role:** M01–M12; integrates the background before the new transfer argument.
- **Conceptual connection:** The exact task links physical event bandwidth with nested estimation errors.
- **Sources:** [model and main results](../science/model-and-results.md); [scope](../science/interpretation-and-scope.md).

## Narrative and innovation: M14–M30

### M14 — From norming to local propagation

- **Central question:** How does ordinary polynomial norming constrain a trigonometric likelihood locally?
- **Understanding target:** Explain Taylor truncation, degree proportional to bandwidth times interval width, and absorption of the remainder.
- **Dependencies and story role:** M09 and M12–M13; builds the key transfer step.
- **Conceptual connection:** Query-limited oscillation becomes an exponential lower bound on neighboring average probability.
- **Sources:** [local propagation lemma and proof](../science/cantor-propagation.md#local-propagation-lemma).

### M15 — Why a neighboring continuum is needed

- **Central question:** Why not compare only two fixed phase hypotheses?
- **Understanding target:** Distinguish coherent perfect point discrimination from probability propagation averaged over a Cantor child.
- **Dependencies and story role:** M08, M10 and M14; identifies the obstacle the transfer resolves.
- **Conceptual connection:** The continuous family supplies rigidity unavailable from a universal pointwise KL comparison.
- **Sources:** [bandwidth versus iid likelihoods](../science/probability-polynomials.md#why-bandwidth-replaces-iid-likelihood-control); [classical comparison](../references/related-work.md#duchi-and-haque-classical-time-uniform-estimation).

### M16 — Decode estimates into digits

- **Central question:** When does a small numerical error determine a Cantor digit?
- **Understanding target:** Use the strict half-gap condition to explain nearest-cylinder decoding and correctness on the global success event.
- **Dependencies and story role:** M10 and M13; translates estimation into sequential decisions.
- **Conceptual connection:** Refinement deadlines become query budgets for decoding nested parameter information.
- **Sources:** [digit decoding](../science/first-error-summability.md#encode-the-phase-by-cantor-digits).

### M17 — A physical prefix event

- **Central question:** Which event can the polynomial lemma actually analyze?
- **Understanding target:** Define the event that earlier decoded bits match a fixed prefix and the next bit is zero, without conditioning or renormalizing.
- **Dependencies and story role:** M07–M08 and M16; keeps the lower-bound object physically valid.
- **Conceptual connection:** A joint event retains bounded bandwidth even when its components are highly dependent.
- **Sources:** [physical transcript events](../science/first-error-summability.md#use-physical-transcript-events).

### M18 — Uniform left-child probability

- **Central question:** Why is that prefix event likely for every parameter in the left child?
- **Understanding target:** Explain containment of the all-time success event and transfer its uniform confidence to the finite transcript event.
- **Dependencies and story role:** M06, M15 and M17; establishes propagation's hypothesis.
- **Conceptual connection:** The confidence guarantee is pointwise in the parameter before any prior averaging.
- **Sources:** [left-child event likelihood](../science/first-error-summability.md#use-physical-transcript-events).

### M19 — The same event becomes a first error

- **Central question:** What does the propagated event mean on the right child?
- **Understanding target:** Show why the earlier decoded bits are correct and the next one is the first wrong bit.
- **Dependencies and story role:** M14 and M17–M18; converts likelihood leakage into an unavoidable failure.
- **Conceptual connection:** One fixed observable event has different correctness meanings under neighboring parameter children.
- **Sources:** [right-child interpretation](../science/first-error-summability.md#the-same-event-is-a-first-error-on-the-right-child).

### M20 — Prior weights and disjoint errors

- **Central question:** Why does summing over exponentially many prefixes leave a constant factor?
- **Understanding target:** Combine right-child mass with the number of prefixes, then explain disjointness of first errors across levels.
- **Dependencies and story role:** M11 and M19; assembles the local bounds into one global probability budget.
- **Conceptual connection:** Prior averaging removes the prefix count without requiring independence across scales.
- **Sources:** [first-error averaging](../science/first-error-summability.md#the-same-event-is-a-first-error-on-the-right-child).

### M21 — The summability law

- **Central question:** What must the normalized refinement costs satisfy jointly?
- **Understanding target:** Explain the exponential summability inequality, its constants and its contradiction with bounded normalized cost at every level.
- **Dependencies and story role:** M18–M20; reaches the principal theorem.
- **Conceptual connection:** A fixed total failure allowance constrains an entire resource schedule.
- **Sources:** [Theorem 1](../science/model-and-results.md#theorem-1-first-error-summability); [proof](../science/first-error-summability.md).

### M22 — The all-time limsup consequence

- **Central question:** How does summability force an iterated logarithm?
- **Understanding target:** Follow the deadlines proportional to three to the level times log of the level, and explain the divergent-series contradiction.
- **Dependencies and story role:** M21; translates the schedule law into an all-time envelope obstruction.
- **Conceptual connection:** Geometric precision makes the logarithm of the refinement level an iterated logarithm of query count.
- **Sources:** [infinite-scale consequence](../science/first-error-summability.md#infinite-scale-consequence).

### M23 — The matching horizon-free schedule

- **Central question:** How can one construct a valid envelope with the matching order?
- **Understanding target:** Combine summable confidence allocation, fixed-confidence estimators, geometric cumulative cost and holding the last completed answer.
- **Dependencies and story role:** M04, M06 and M22; distinguishes the routine upper mechanism from the new converse.
- **Conceptual connection:** The union bound supplies joint validity while geometric budgets preserve query efficiency.
- **Sources:** [horizon-free construction](../science/upper-bounds-extensions.md#horizon-free-matching-construction); [finite schedule check](../verification/README.md).

### M24 — A finite set of refinement levels

- **Central question:** What exactly does the theorem force for a finite number of deadlines?
- **Understanding target:** Derive a maximum normalized-deadline bound and explain the Jensen average version without selecting the penalized level.
- **Dependencies and story role:** M21; gives a finite operational consequence with correct quantifiers.
- **Conceptual connection:** Summability restricts efficiency across the requested resolutions collectively.
- **Sources:** [finite-scale consequence](../science/first-error-summability.md#finite-k-consequence); [Corollary 2](../science/model-and-results.md#corollary-2-finite-number-of-refinement-levels).

### M25 — The known-final-horizon boundary

- **Central question:** Why can the last target avoid an extra logarithm of the number of levels?
- **Understanding target:** Explain backward-geometric failure allocation and the larger normalized costs it permits at early levels.
- **Dependencies and story role:** M23–M24; checks the strongest tempting overinterpretation.
- **Conceptual connection:** Simultaneous efficiency at every scale is more demanding than optimal cost at one known final precision.
- **Sources:** [known final horizon](../science/upper-bounds-extensions.md#finite-k-and-the-known-final-horizon-boundary); [schedule reproduction](../verification/README.md).

### M26 — Random refinement-hitting times

- **Central question:** Does allowing random query deadlines escape the mechanism?
- **Understanding target:** Apply Markov truncation to worst-case expected hitting cost, and identify the required finite-expectation and joint-correctness assumptions.
- **Dependencies and story role:** M17–M21; extends the physical-event argument to a fixed truncation cap.
- **Conceptual connection:** Random stopping is handled by a bounded-prefix event, rather than an unjustified polynomial for an unlimited transcript.
- **Sources:** [expected refinement times](../science/upper-bounds-extensions.md#expected-refinement-times); [Theorem 2](../science/model-and-results.md#theorem-2-expected-refinement-costs).

### M27 — Confidence intervals and optional stopping

- **Central question:** What does simultaneous coverage imply for a data-dependent stopping rule?
- **Understanding target:** Reduce deterministic diameters or expected precision-hitting times to the appropriate theorem and separate coverage from shrinkage speed.
- **Dependencies and story role:** M06 and M26; connects the query law to sequential inference.
- **Conceptual connection:** Selecting an already-covered interval adds no new failure event, while attaining its precision consumes resources.
- **Sources:** [confidence sequences and optional stopping](../science/upper-bounds-extensions.md#confidence-sequences-and-optional-stopping).

### M28 — Transfer to coherent amplitude estimation

- **Central question:** Which amplitude interface inherits the phase obstruction?
- **Understanding target:** Explain the two-query rotation simulation, clipping and the interior inverse Lipschitz bound, including controlled and inverse access.
- **Dependencies and story role:** M03, M21 and M26; tests a concrete task-to-task transfer with charged resources.
- **Conceptual connection:** An interior two-dimensional subfamily converts amplitude accuracy into phase accuracy at constant query overhead.
- **Sources:** [explicit reduction](../science/upper-bounds-extensions.md#explicit-amplitude-estimation-reduction); [Corollary 3](../science/model-and-results.md#corollary-3-coherent-amplitude-estimation).

### M29 — What the result adds

- **Central question:** What remains after inherited ingredients are credited?
- **Understanding target:** Distinguish classical first-error architecture, quantum polynomial methods, norming theory, terminal estimation and copy-based confidence sequences from the coherent all-scale lower law.
- **Dependencies and story role:** M14–M28; integrates the mechanism with the closest work and its operational significance.
- **Conceptual connection:** Novelty lies in a justified coherent-query transfer and consequence, rather than the presence of familiar tools.
- **Sources:** [related work](../references/related-work.md); [interpretation](../science/interpretation-and-scope.md).

### M30 — The complete operational story

- **Central question:** When does this theorem change an estimator's claimed resource guarantee?
- **Understanding target:** State the task, proof chain, matching upper order and quantifier limits; identify different access/output models and distinguish analytical proof from finite arithmetic checks.
- **Dependencies and story role:** M13 and M21–M29; synthesizes the entire project without adding a new task.
- **Conceptual connection:** A trustworthy continuing classical record has a multiscale cost even when quantum memory and adaptive control are unrestricted.
- **Sources:** [main results](../science/model-and-results.md), [scope and resource ledger](../science/interpretation-and-scope.md), and [verification limits](../verification/README.md).
