# All-time confidence with expiring reversible samplers

The coherent-phase theorem extends to a source that disappears after a bounded number of local replays. The relevant confidence cost multiplies the **full replay-dependent frontier**, including its rare-probability replay term. This requires a new probability-propagation argument; the two earlier lower bounds alone do not imply it.

This is a shared result with [Quantum Mean Replay](https://github.com/GoGoKo699/Quantum-Mean-Replay). That repository owns the [canonical shared proof and charged construction](https://github.com/GoGoKo699/Quantum-Mean-Replay/blob/99d19bf29d1be3f6d88edcca86f0214a9495c78b/science/anytime-confidence.md). This page states the complete transfer model, result and proof interface so the confidence account can be read independently. The existing [phase theorem](model-and-results.md) retains its original assumptions and conclusions.

## 1. Source, commitment and cost model

Fix a known scale $`0\lt p_0\le1/16`$ and an unknown common probability $`p\in[p_0,2p_0]`$. Source $`i`$ is an otherwise unknown unitary $`U_i`$ on a known initialized workspace, with a known success projector $`\Pi`$ and

```math
\langle0|U_i^\dagger\Pi U_i|0\rangle=p.
```

Output garbage, phases and unitary completions may change arbitrarily. This is the **zero-drift** class. A source is available only in its chronological window, with at most $`m\ge2`$ forward, inverse or allowed controlled calls in total. Its inverse must be exact during that window. Source retirement and progression are classical; there are no revisits or coherent SELECT calls across source identities. Arbitrary persistent quantum memory, intermediate instruments and classical feedback are allowed.

Every executed physical invocation costs one call, including a controlled invocation and an attempt that later fails. A classically omitted call costs zero. The charged resource $`T`$ is the cumulative actual source-call budget, with a deterministic cap on every outcome path. Gates, workspace and probe coherence are separate resources.

One continuing run emits committed classical estimates $`\widehat p_T`$ with a deterministic radius $`r(T)`$. Its guarantee is

```math
\inf_{p,\{U_i\}}
\Pr_{p,\{U_i\}}
\left\{ |\widehat p_T-p|\le r(T)
\text{ for every }T\ge1\right\}
\ge1-\alpha,
\qquad 0<\alpha\le\frac14.
```

The infimum ranges over all fixed valid source lists. Keeping the last completed estimate between stages is permitted. Separate marginal confidence at each time is a different guarantee. The results below use deterministic call deadlines; the expected-refinement theorem for phase queries is not being silently transferred to this source model.

## 2. Full-frontier summability theorem

Define

```math
A_m(p_0)=\max\!\left\{\sqrt{p_0},\frac1m\right\}.
```

**Shared theorem.** There are absolute positive constants $`c,B,D`$ such that, for geometric tolerances $`\epsilon_k=c p_0 3^{-k}`$ and increasing deterministic deadlines $`T_k`$ satisfying $`r(T_k)<\epsilon_k`$,

```math
\boxed{
\sum_{k\ge1}
\exp\!\left[-D\frac{T_k\epsilon_k}{A_m(p_0)}\right]
\le B\alpha.
}
```

For any finite set of the first $`K`$ required refinements, the same sum restricted to $`k\le K`$ holds. Consequently,

```math
\max_{1\le k\le K}
\frac{T_k\epsilon_k}{A_m(p_0)}
\ge \frac1D\log\frac{K}{B\alpha}.
```

Convexity gives the same lower order for the average normalized deadline. The statement constrains simultaneous efficiency across scales; it does not force the displayed overhead at every individual deadline.

A horizon-free construction attains cumulative deadlines

```math
T_k\le
C\frac{A_m(p_0)}{\epsilon_k}
\left[\log(k+2)+\log(1/\alpha)\right].
```

Thus, for fixed $`p_0,m`$, an all-time envelope of order

```math
r(T)=O\!\left(
\frac{A_m(p_0)}{T}
[\log\log T+\log(1/\alpha)]
\right)
```

is attainable after initialization, and every valid shrinking envelope satisfies

```math
\limsup_{T\to\infty}
\frac{T r(T)}{A_m(p_0)\log\log T}>0.
```

Before initialization, the known midpoint $`3p_0/2`$ with radius $`p_0/2`$ suffices. The geometric-deadline statement is the precise confidence-dependent result; the limsup formulation concerns the asymptotic cost of indefinite refinement.

### Two calls and very rare probabilities

For $`m=2`$ throughout the promised scale range, $`A_2(p_0)=1/2`$. Therefore

```math
r(T)=O\!\left(
\frac{\log\log T+\log(1/\alpha)}{T}
\right)
```

is achievable, while the displayed limsup lower bound makes its iterated-logarithm order unavoidable across indefinite refinement. There is no extra $`\sqrt{p_0}`$ suppression, even when $`p_0\ll1/m^2`$. At relative tolerance $`\epsilon=\rho p_0`$ with $`0<\rho\le1/64`$, the uniformly efficient refinement scale is $`[\log(k+2)+\log(1/\alpha)]/(\rho p_0)`$, up to absolute factors. Small $`p_0`$ changes the cost of reaching relative accuracy and the stage index; it does not move the confidence price solely onto the ordinary amplitude-estimation branch.

## 3. Why the replay branch also pays

The new input to this repository's [Cantor propagation](cantor-propagation.md) argument is a derivative bound for **unnormalized physical transcript events**. Its proof has four steps; the full channel and call-accounting details are in the canonical shared proof.

### Step 1 — One continuous hard family Independently for each source, draw fixed phases $`a,b\in\{0,1\}`$ and $`c\in\{0,1,2,3\}`$, and supply

```math
U_{a,b,c;p}=i^c Z^a R_p Z^b,
\qquad
R_p=\begin{pmatrix}
\sqrt{1-p}&-\sqrt p\\
\sqrt p&\sqrt{1-p}
\end{pmatrix}.
```

Every fixed draw has exact mean $`p`$ and its matching inverse. The whole source list is fixed before the run. The phase distribution is separately invariant under either square root changing sign. After averaging, a finite instrument using at most $`L`$ physical calls is therefore polynomial in $`p`$ of degree at most $`L`$. This includes arbitrary references and adaptive controls; conditioning and renormalizing an outcome would invalidate this polynomial assertion.

### Step 2 — Blocks charged by actual calls At a prefix cap $`Q\ge1`$, put $`h=\min(m,Q)`$. Begin a block with an unused source. Once its actual-call count reaches $`h`$, finish the current source window and end the block. Full blocks cost between $`h`$ and $`2h-1`$ calls; the final block is truncated at $`Q`$. There are at most $`\lfloor Q/h\rfloor+1`$ blocks, and no source crosses a boundary. Untouched skipped source labels can be integrated away because the hard labels are independent. Full histories, counters, outputs and persistent memory remain at interfaces. Local and global counters are enforced on all parameters, with a fixed abort output outside the cap, so each averaged block is a CPTP channel on the full interval $`p\in[0,1]`$.

### Step 3 — A replay-sensitive derivative estimate Each block channel has polynomial degree at most $`2h`$. Markov's polynomial inequality applied to norming linear functionals bounds its derivatives in diamond norm by $`(C h^2)^j`$. Leibniz's rule, channel-norm submultiplicativity and the block count then give, for every finite-prefix event likelihood $`f_Q`$,

```math
0\le f_Q(p)\le1,
\qquad
\sup_{p\in[0,1]}|f_Q^{(j)}(p)|
\le [C Q\min(m,Q)]^j.
```

The bound charges actual calls rather than $`m`$ padded calls for every source. It already uses only one-qubit hard sources.

### Step 4 — Propagate first errors Substitute this derivative estimate for Fourier bandwidth in the existing Taylor-plus-Cantor lemma. An event likely on one child of width $`\ell`$ has average probability at least $`c\exp[-C(Q\min(m,Q)\ell+1)]`$ on its neighbor. The same disjoint first-error events as in [the phase proof](first-error-summability.md) yield

```math
\sum_k
\exp[-D T_k\min(m,T_k)\epsilon_k]
\le B\alpha.
```

Since $`\min(m,T_k)\le m`$, this implies replay summability with exponent $`mT_k\epsilon_k`$ without requiring $`T_k\ge m`$.

Separately, choose all sources to be the same clean rotation $`R_p`$. On the known-scale interval, $`p=\sin^2\theta`$ has $`dp/d\theta=\Theta(\sqrt{p_0})`$. The original phase theorem directly gives

```math
\sum_k
\exp[-D T_k\epsilon_k/\sqrt{p_0}]
\le B\alpha.
```

Use the fresh-phase family when $`m\le p_0^{-1/2}`$ and the clean-rotation family otherwise. This selects the stronger of two proved **multiscale** laws and establishes the full-frontier theorem. It is not an inference obtained by multiplying a fixed-confidence replay lower bound by an unrelated all-time factor.

## 4. Charged construction and the final-horizon boundary

At $`m=2`$, one gearbox attempt invokes $`U_i`$ and $`U_i^\dagger`$: exactly two calls on success or failure. Success has probe-independent probability

```math
s(p)=(1-p)^2+p^2\ge\frac12
```

and adds relative probe phase $`\varphi(p)=2\arctan(1-2p)`$, with $`2\le|\varphi'(p)|\le4`$. A known correction restores the incoming probe after failure. With zero drift, accepted phases agree despite arbitrary changing source garbage.

If the terminal Ramsey schedule needs $`S`$ accepted rotations, cap attempts at

```math
N=\left\lceil4S+16\log(2/\beta)\right\rceil.
```

Charge $`2N`$ physical calls. Exhausting the cap is a recorded failure included in $`\beta`$; it is never postselected away. General $`m`$ uses local odd-length Grover amplification and its inverse, with $`2\ell\le m`$ calls per attempt, yielding terminal cost $`O(A_m(p_0)\epsilon^{-1}\log(1/\beta))`$. The canonical construction supplies its amplification range and Ramsey schedule.

For indefinite refinement, use $`\epsilon_k=c p_0 3^{-k}`$ and allocate $`\beta_k`$ proportional to $`\alpha/(k+1)^2`$. The attempt caps and the estimation failures share this budget. A union bound gives one joint correctness event, and geometric accumulation gives the displayed cumulative deadlines.

If the last target $`\epsilon_K`$ is known beforehand, a backward-geometric allocation proportional to $`\alpha3^{k-K}`$ instead gives terminal cost

```math
O\!\left(
\frac{A_m(p_0)}{\epsilon_K}\log(1/\alpha)
\right).
```

Earlier normalized deadlines may be inefficient. Neither emitting intermediate answers nor the summability theorem alone forces a $`\log K`$ factor into that final deadline.

## 5. Ownership and limits

Quantum Mean Replay supplies the source model, terminal gearbox composition, amplification and Ramsey estimator. The gearbox primitive is inherited from Wiebe--Kliuchnikov and Wiebe--Roetteler, and amplification from Brassard et al.; Hu et al. supply material non-identical-sampling foundations. This repository supplies the existing Cantor norming and unconditioned first-error architecture, following Duchi--Haque's classical architecture and the phase-query polynomial method. The fresh-phase channel polynomial, actual-call blocks and replay-sensitive propagation theorem are the shared addition, with one canonical proof in Quantum Mean Replay.

The all-time upper statement here has zero drift. A fixed positive drift tolerance cannot support radii shrinking indefinitely to zero. Exact inverses, classical chronological retirement and absence of revisits or coherent source selection remain load-bearing. Unknown probability scales, expected stopping-cost frontiers, physical runtime and noise robustness are not established by this transfer. Finite arithmetic checks illustrate the schedule and polynomial identities; they do not certify the infinite-scale theorem or constitute independent expert verification.
