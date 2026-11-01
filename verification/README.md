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
