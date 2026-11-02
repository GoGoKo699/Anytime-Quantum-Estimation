#!/usr/bin/env python3
"""Finite charged-query ledgers for all-time replay confidence schedules.

This checks deterministic schedule arithmetic, amplification bounds and the
known-final-level boundary. It does not simulate a quantum experiment or prove
Cantor propagation, a lower bound, or simultaneous coverage.
"""
import argparse
import hashlib
import json
import math
from pathlib import Path

RHO = math.pi / 8
SENSITIVITY = 4 / math.pi


def amplification_length(p0, m):
    bound = min(m // 2, 1 / (4 * math.sqrt(p0)))
    length = int(math.floor(bound))
    if length % 2 == 0:
        length -= 1
    if length < 1:
        raise ValueError('the replay construction requires m>=2 and p0<=1/16')
    if 2 * length > m or length * length * p0 > 1 / 16 + 1e-15:
        raise AssertionError('amplification violates the replay/first-lobe cap')
    return length


def phase_width(p0, length):
    q1 = math.sin(length * math.asin(math.sqrt(p0))) ** 2
    q2 = math.sin(length * math.asin(math.sqrt(2 * p0))) ** 2
    # Stable atan-difference formula: direct subtraction loses digits at rare p0.
    return 2 * math.atan(2 * (q2 - q1) / (1 + (1 - 2*q1) * (1 - 2*q2)))


def allocation(alpha, levels, mode):
    if mode == 'horizon_free':
        return [alpha / ((j+1)*(j+2)) for j in range(levels)]
    if mode == 'finite_equal':
        return [alpha / levels] * levels
    if mode == 'known_final':
        normalizer = (1 << levels) - 1
        return [alpha * (1 << j) / normalizer for j in range(levels)]
    raise ValueError(mode)


def schedule(p0, m, alpha, levels, mode):
    length = amplification_length(p0, m)
    width = phase_width(p0, length)
    lower = SENSITIVITY * length * length * p0
    upper = 4 * length * length * p0
    if not lower <= width <= upper:
        raise AssertionError('prior phase width violates the analytical sensitivity bounds')
    cumulative = 0
    rows = []
    for j, beta in enumerate(allocation(alpha, levels, mode)):
        epsilon = p0 / (64 * (1 << j))
        target = RHO / (SENSITIVITY * length * length * epsilon)
        inner_levels = max(0, math.ceil(math.log2(target)))
        L = 1 << inner_levels
        # Certify the rounding in the last Ramsey length explicitly.
        while L < target:
            inner_levels += 1
            L <<= 1
        accepted = 0
        coordinate_failure_budget = 0.0
        finest_repetitions = None
        for inner in range(inner_levels + 1):
            inner_beta = beta * 2.0 ** (inner - inner_levels - 2)
            repetitions = math.ceil(128 * math.log(4 / inner_beta))
            accepted += 2 * (1 << inner) * repetitions
            # Two quadratures; each has failure at most inner_beta/2.
            coordinate_bound = 4 * math.exp(-repetitions / 128)
            if coordinate_bound > inner_beta * (1 + 1e-12):
                raise AssertionError('inner coordinate ledger exceeds its allocation')
            coordinate_failure_budget += inner_beta
            finest_repetitions = repetitions
        # At very rare scales the omitted geometric tail is below float
        # precision, so the represented sum can equal beta/2 exactly.
        if coordinate_failure_budget > beta / 2 * (1 + 1e-12):
            raise AssertionError('terminal Ramsey coordinates exceed beta/2')
        # Integer arithmetic avoids rounding away the cap correction when p0 is tiny.
        attempts = 4 * accepted + math.ceil(16 * math.log(2 / beta))
        call_cap = 2 * length * attempts
        cumulative += call_cap
        certified_epsilon = RHO / (SENSITIVITY * length * length * L)
        if certified_epsilon > epsilon:
            raise AssertionError('terminal Ramsey precision exceeds its target')
        if -attempts / 16 > math.log(beta / 2):
            raise AssertionError('attempt-cap ledger exceeds its confidence allocation')
        if attempts < 4 * accepted:
            raise AssertionError('attempt cap does not cover corrected failures')
        # N attempts cost 2*ell*N even on an all-failure path. Counting accepted
        # operations alone would undercharge this path by the displayed factor.
        all_failure_path_calls = 2 * length * attempts
        if all_failure_path_calls != call_cap:
            raise AssertionError('failed attempts were not fully charged')
        rows.append({
            'stage': j,
            'allocated_failure': beta,
            'finest_accepted_rotations_per_shot': L,
            'inner_Ramsey_levels': inner_levels + 1,
            'finest_shots_per_quadrature': finest_repetitions,
            'inner_coordinate_failure_budget': coordinate_failure_budget,
            'prescribed_accepted_rotations': accepted,
            'attempt_cap': attempts,
            'primitive_calls_per_attempt': 2 * length,
            'primitive_call_cap': call_cap,
            'all_failure_path_calls': all_failure_path_calls,
            'accepted_only_call_count': 2 * length * accepted,
            'cumulative_primitive_call_cap': cumulative,
            'epsilon': epsilon,
            'certified_terminal_epsilon': certified_epsilon,
            'normalized_cumulative': cumulative * epsilon * length,
        })
    failure_sum = sum(row['allocated_failure'] for row in rows)
    if mode == 'horizon_free':
        expected = alpha * levels / (levels + 1)
        if not math.isclose(failure_sum, expected, rel_tol=1e-12):
            raise AssertionError('telescoping horizon-free allocation failed')
    elif not math.isclose(failure_sum, alpha, rel_tol=1e-12):
        raise AssertionError('finite allocation failed to use exactly alpha')
    if not all(rows[j]['cumulative_primitive_call_cap'] < rows[j+1]['cumulative_primitive_call_cap']
               for j in range(levels-1)):
        raise AssertionError('deterministic deadlines did not increase')
    if not all(rows[j]['epsilon'] == 2 * rows[j+1]['epsilon']
               for j in range(levels-1)):
        raise AssertionError('target radii did not refine geometrically')
    return {
        'parameters': {'p0':p0,'m':m,'alpha':alpha,'levels':levels,'mode':mode},
        'amplification_length': length,
        'frontier_A': max(math.sqrt(p0), 1/m),
        'construction_A': 1/length,
        'prior_phase_width': width,
        'failure_sum': failure_sum,
        'max_normalized_deadline': max(row['normalized_cumulative'] for row in rows),
        'final_normalized_deadline': rows[-1]['normalized_cumulative'],
        'final_normalized_over_log1alpha': rows[-1]['normalized_cumulative'] / math.log(1/alpha),
        'rows': rows,
    }


def build():
    cases = [(1/16,2),(2**-10,2),(2**-40,2),(2**-40,64),(2**-40,2**22)]
    horizon_free = [schedule(p0,m,0.05,16,'horizon_free') for p0,m in cases]
    # The extremely rare m=2 case must retain ell=1: p0 does not grant free replay.
    if horizon_free[2]['amplification_length'] != 1:
        raise AssertionError('m=2 rare-event case did not use exactly two calls per attempt')
    terminal = []
    for levels in [4,12,32,80]:
        final = schedule(2**-40,2,0.05,levels,'known_final')
        equal = schedule(2**-40,2,0.05,levels,'finite_equal')
        if final['final_normalized_over_log1alpha'] > 100000:
            raise AssertionError('terminal cost acquired an unexpected scale-count factor')
        terminal.append({
            'levels':levels,
            'known_final_failure_sum':final['failure_sum'],
            'equal_failure_sum':equal['failure_sum'],
            'known_final_final_normalized_over_log1alpha':final['final_normalized_over_log1alpha'],
            'known_final_max_normalized_deadline':final['max_normalized_deadline'],
            'equal_final_normalized_over_log1alpha':equal['final_normalized_over_log1alpha'],
        })
    confidence = []
    for alpha in [0.2, 0.01, 1e-6, 1e-12]:
        final = schedule(2**-40,2,alpha,32,'known_final')
        if final['final_normalized_over_log1alpha'] > 100000:
            raise AssertionError('terminal confidence dependence exceeded the analytical order')
        confidence.append({
            'alpha':alpha,
            'levels':32,
            'final_normalized_over_log1alpha':final['final_normalized_over_log1alpha'],
            'failure_sum':final['failure_sum'],
        })
    return {
        'scope':'finite schedule arithmetic and full failed-attempt ledger; not a proof or hardware experiment',
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'normalization':'D_j * epsilon_j / A_construction, where A_construction=1/ell',
        'horizon_free':horizon_free,
        'known_final_boundary':terminal,
        'terminal_confidence_dependence':confidence,
        'finite_checks_pass':True,
    }


def equivalent(left, right):
    if isinstance(left,dict) and isinstance(right,dict):
        return left.keys()==right.keys() and all(equivalent(left[k],right[k]) for k in left)
    if isinstance(left,list) and isinstance(right,list):
        return len(left)==len(right) and all(equivalent(a,b) for a,b in zip(left,right))
    if isinstance(left,float) or isinstance(right,float):
        return isinstance(left,(int,float)) and isinstance(right,(int,float)) and math.isclose(left,right,rel_tol=1e-12,abs_tol=1e-14)
    return left==right


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write',type=Path)
    parser.add_argument('--check',type=Path)
    args=parser.parse_args()
    result=build()
    if args.check and not equivalent(json.loads(args.check.read_text()),result):
        raise SystemExit('schedule result differs from the reference')
    encoded=json.dumps(result,indent=2,sort_keys=True)+'\n'
    if args.write:
        args.write.write_text(encoded)
    print(encoded,end='')


if __name__=='__main__':
    main()
