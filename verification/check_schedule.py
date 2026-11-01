#!/usr/bin/env python3
"""Finite arithmetic checks for the schedule claims.

This script does not test the analytical lower bound. It checks only the
confidence allocations and geometric sums used to explain upper bounds
and theorem boundaries.
"""

import argparse
import json
import math
from pathlib import Path


def horizon_free(alpha, K):
    rows = []
    cumulative = 0.0
    for k in range(1, K + 1):
        eps = 3.0 ** (-k)
        alpha_k = 6.0 * alpha / (math.pi ** 2 * k ** 2)
        stage = eps ** -1 * math.log(1.0 / alpha_k)
        cumulative += stage
        rows.append({
            "k": k,
            "epsilon": eps,
            "alpha_k": alpha_k,
            "stage_cost": stage,
            "cumulative_cost": cumulative,
            "normalized_cumulative": cumulative * eps,
        })
    return rows


def equal_finite(alpha, K):
    rows = []
    cumulative = 0.0
    for k in range(1, K + 1):
        eps = 3.0 ** (-k)
        alpha_k = alpha / K
        stage = eps ** -1 * math.log(1.0 / alpha_k)
        cumulative += stage
        rows.append({
            "k": k,
            "epsilon": eps,
            "alpha_k": alpha_k,
            "stage_cost": stage,
            "cumulative_cost": cumulative,
            "normalized_cumulative": cumulative * eps,
        })
    return rows


def known_final(alpha, K):
    weights = [3.0 ** (k - K) for k in range(1, K + 1)]
    norm = sum(weights)
    rows = []
    cumulative = 0.0
    for k, weight in enumerate(weights, start=1):
        eps = 3.0 ** (-k)
        alpha_k = alpha * weight / norm
        stage = eps ** -1 * math.log(1.0 / alpha_k)
        cumulative += stage
        rows.append({
            "k": k,
            "epsilon": eps,
            "alpha_k": alpha_k,
            "stage_cost": stage,
            "cumulative_cost": cumulative,
            "normalized_cumulative": cumulative * eps,
        })
    return rows


def build(alpha=0.05, K=12):
    hf = horizon_free(alpha, K)
    eq = equal_finite(alpha, K)
    fh = known_final(alpha, K)
    return {
        "parameters": {"alpha": alpha, "K": K},
        "horizon_free": {
            "failure_sum": sum(x["alpha_k"] for x in hf),
            "max_normalized": max(x["normalized_cumulative"] for x in hf),
        },
        "finite_equal_allocation": {
            "failure_sum": sum(x["alpha_k"] for x in eq),
            "max_normalized": max(x["normalized_cumulative"] for x in eq),
        },
        "known_final_horizon": {
            "failure_sum": sum(x["alpha_k"] for x in fh),
            "max_normalized": max(x["normalized_cumulative"] for x in fh),
            "final_normalized": fh[-1]["normalized_cumulative"],
            "final_cost_over_3K_log1a": (
                fh[-1]["cumulative_cost"] /
                ((3.0 ** K) * math.log(1.0 / alpha))
            ),
        },
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--alpha", type=float, default=0.05)
    parser.add_argument("--levels", type=int, default=12)
    parser.add_argument("--check", type=Path)
    parser.add_argument("--write", type=Path)
    args = parser.parse_args()

    result = build(args.alpha, args.levels)
    assert result["horizon_free"]["failure_sum"] < args.alpha
    assert abs(result["finite_equal_allocation"]["failure_sum"] - args.alpha) < 1e-12
    assert abs(result["known_final_horizon"]["failure_sum"] - args.alpha) < 1e-12
    assert result["known_final_horizon"]["final_cost_over_3K_log1a"] < 3.0

    encoded = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.write:
        args.write.write_text(encoded)
    if args.check:
        expected = json.loads(args.check.read_text())
        if expected != result:
            raise SystemExit("verification result differs from committed reference")
    print(encoded, end="")


if __name__ == "__main__":
    main()
