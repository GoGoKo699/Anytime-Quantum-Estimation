# Verification

The central lower theorem is analytical. Finite computation cannot certify its universal query lower bound, literature comparison, or asymptotic limsup statement.

The repository includes a deterministic arithmetic check for three confidence schedules:

    python3 verification/check_schedule.py --check verification/results.json

The reference run uses alpha=0.05 and K=12 geometric refinement levels. It verifies:

1. the horizon-free allocation 6 alpha/(pi^2 k^2) sums to less than alpha;
2. equal allocation across K levels uses total failure budget alpha and exhibits the expected logarithmic normalized cost;
3. a backward-geometric allocation for a known final level uses the same total failure budget while its final cumulative cost stays a constant multiple of 3^K log(1/alpha).

The third item is a boundary check: it prevents the finite-K first-error theorem from being misreported as T_K=Omega(3^K log K).

Regenerate the reference with:

    python3 verification/check_schedule.py --write verification/results.json

The script uses only Python's standard library.

## Charged local-replay schedules

The sister result has an additional deterministic check:

```bash
python3 verification/check_anytime_replay.py --check verification/replay-schedule-results.json
```

It follows the constructive schedule, including its conservative constants,
rather than fitting an asymptotic formula. The supplied scales are
$`p_0=1/16,2^{-10},2^{-40}`$. Cases include $`m=2`$ even at
$`p_0=2^{-40}\ll1/m^2`$, a larger replay budget before saturation, and a
budget beyond the rare-event crossover. The amplification length is the
largest positive odd $`\ell\le\min\{m/2,1/(4\sqrt{p_0})\}`$.

Each of 16 committed refinement stages runs the complete terminal Ramsey
subroutine at its own target precision. Its internal dyadic lengths and
backward-geometric confidence allocation reproduce the canonical construction;
the ledger records those internal levels, prescribed accepted rotations $`S_j`$, attempt cap
$`N_j=4S_j+\lceil16\log(2/\beta_j)\rceil`$, and actual physical-call
cap $`2\ell N_j`$. Each failed attempt costs the same $`2\ell`$ calls as
a successful one. An all-failure path therefore exhausts the full cap; counting
only accepted rotations would undercharge it. Integer arithmetic preserves the
cap correction even when the rare-event case produces very large integers.
The report checks the coordinate and cap failure allocations separately, the
telescoping horizon-free confidence budget, increasing deadlines and geometrically
shrinking precision targets. These are budget calculations, not executions of
that many oracle calls.

The known-final-level check uses 4, 12, 32 and 80 levels. A backward-geometric
allocation uses total failure budget $`\alpha`$ and keeps the final normalized
cost bounded after division by $`\log(1/\alpha)`$. Some earlier normalized
deadlines grow instead. This guards against assigning the finite-scale
$`\log K`$ cost to the final deadline alone. The normalization in the report is
$`D_j\epsilon_j/A_{\rm construction}`$, with $`A_{\rm construction}=1/\ell`$;
this is within universal constant factors of
$`A_m=\max\{\sqrt{p_0},1/m\}`$.

A separate 32-level terminal check varies $`\alpha`$ from $`0.2`$ to
$`10^{-12}`$ and records the final normalized cost divided by
$`\log(1/\alpha)`$. This tests the confidence allocation arithmetic as well
as the number-of-scales boundary. The constants are those of the conservative
proved schedule and are not optimized implementation estimates.

The script uses only the standard library. Its source identity and complete
stage ledgers are in [replay-schedule-results.json](replay-schedule-results.json).
Regenerate with `--write verification/replay-schedule-results.json`.

The [canonical finite source-twirl and macroblock check](https://github.com/GoGoKo699/Quantum-Mean-Replay/blob/main/verification/check_twirl_degree.py)
and its [recorded results](https://github.com/GoGoKo699/Quantum-Mean-Replay/blob/main/verification/twirl-degree-results.json)
live in Quantum Mean Replay. That matrix calculation tests polynomial cancellation
and an outcome-adaptive charged block; it is not duplicated here. Neither the
matrix checks nor the schedule arithmetic certify the Banach-valued Markov
inequality, Cantor propagation, universal first-error summability, scientific
priority or a hardware performance claim. Those remain analytical and literature
questions.
