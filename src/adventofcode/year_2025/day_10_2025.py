from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_for_day
import numpy as np

from functools import lru_cache


def parse_machine(line: str):
    # Example line:
    # [.##.] (3) (1,3) (2,3) {3,4,5}
    parts = line.strip().split()
    # First part = diagram in brackets
    diagram = parts[0].strip()[1:-1]
    target = [1 if c == "#" else 0 for c in diagram]
    n = len(target)

    buttons = []
    for p in parts[1:]:
        if p.startswith("("):
            inside = p[1:-1].strip()
            if inside == "":
                buttons.append([])
            else:
                buttons.append([int(x) for x in inside.split(",")])
        # ignore {...} joltage spec

    return target, buttons, n


def solve_machine(target, buttons, n):
    """
    We want A * x = target  over GF(2)
    A: n x m matrix, each column is a button, rows represent lights.
    x_j = number of presses mod 2
    We must also select the solution with minimal L1 norm (# of presses),
    but actual number of presses is integer, and pressing twice cancels,
    so only mod2 matters and weight is number of 1s.
    """
    m = len(buttons)

    # Build matrix A over integers (we will mod2)
    A = []
    for i in range(n):
        row = []
        for b in buttons:
            row.append(1 if i in b else 0)
        A.append(row)

    # Gaussian elimination to find one solution + basis for nullspace.
    # Standard GF(2) elimination.

    A = [row[:] for row in A]
    b = target[:]

    pivots = []
    row = 0
    for col in range(m):
        # find pivot row
        sel = None
        for r in range(row, n):
            if A[r][col] % 2 == 1:
                sel = r
                break
        if sel is None:
            continue
        # swap
        A[row], A[sel] = A[sel], A[row]
        b[row], b[sel] = b[sel], b[row]
        pivots.append((row, col))

        # eliminate other rows
        for r in range(n):
            if r != row and A[r][col] % 2 == 1:
                for c in range(col, m):
                    A[r][c] ^= A[row][c]
                b[r] ^= b[row]

        row += 1
        if row == n:
            break

    # Check consistency
    for r in range(row, n):
        if b[r] % 2 == 1:
            # no solution
            return None

    # Identify free variables
    pivot_cols = {c for (_, c) in pivots}
    free_cols = [c for c in range(m) if c not in pivot_cols]

    # Solve for pivot variables as a function of free vars
    # A is in row-echelon form.
    def particular_solution():
        x = [0] * m
        # Back-substitute pivots
        for r, c in reversed(pivots):
            acc = b[r]
            for c2 in range(c + 1, m):
                acc ^= A[r][c2] & x[c2]
            x[c] = acc
        return x

    base = particular_solution()

    # Nullspace basis vectors
    nullvecs = []
    for free in free_cols:
        v = [0] * m
        v[free] = 1
        # For each pivot variable, pivot var = sum of A[r][col]*v[col]
        for r, c in pivots:
            acc = 0
            for c2 in range(c + 1, m):
                if A[r][c2] % 2 == 1 and v[c2] == 1:
                    acc ^= 1
            # pivot column
            v[c] = acc
        nullvecs.append(v)

    # Evaluate all combinations of nullspace vectors to find minimal Hamming weight
    best = None
    for mask in range(1 << len(nullvecs)):
        x = base[:]
        for i in range(len(nullvecs)):
            if (mask >> i) & 1:
                for j in range(m):
                    x[j] ^= nullvecs[i][j]
        w = sum(x)
        if best is None or w < best:
            best = w

    return best


@register_solution(2025, 10, 1)
def part_one(input_data: list[str]):
    total = 0
    for line in input_data:
        target, buttons, n = parse_machine(line)
        best = solve_machine(target, buttons, n)
        if best is None:
            raise SolutionNotFoundError(2025, 10, 1)
        total += best

    if total is None:
        raise SolutionNotFoundError(2025, 10, 1)

    return total


def parse_joltage_machine(line: str):
    parts = line.strip().split()
    buttons = []
    target = None
    for p in parts:
        if p.startswith("("):
            inner = p[1:-1].strip()
            if inner == "":
                buttons.append([])
            else:
                buttons.append([int(x) for x in inner.split(",")])
        elif p.startswith("{"):
            inner = p[1:-1].strip()
            target = np.array([int(x) for x in inner.split(",")], dtype=np.int16)
    return target, buttons


def solve_machine_branch_and_bound(target: list[int], buttons: list[list[int]]):
    """
    Solve A x = target, x >= 0 integer, minimizing sum(x).
    target: list of k nonnegative ints
    buttons: list of m lists of indices indicating which counters each button increments
    Returns minimal total presses (int) or None if impossible.
    """

    k = len(target)
    m = len(buttons)

    # Quick infeasibility check: every counter with positive target must be covered by >=1 button
    for i, ti in enumerate(target):
        if ti > 0:
            covered = False
            for b in buttons:
                if i in b:
                    covered = True
                    break
            if not covered:
                return None  # impossible

    # Precompute button columns as tuple vectors for fast arithmetic
    cols = [tuple(1 if i in b else 0 for i in range(k)) for b in buttons]

    # Upper bound: greedy constructive solution (fast, gives initial best)
    def greedy_upper_bound():
        rem = list(target)
        presses = 0
        # while any remaining >0, pick button with highest "useful coverage" per press
        while True:
            if all(r == 0 for r in rem):
                return presses
            best_idx = None
            best_gain = 0
            # compute how many remaining units each single press of button would decrease (sum of min(1,rem_i) over its columns)
            for j in range(m):
                gain = 0
                for i in range(k):
                    if cols[j][i] and rem[i] > 0:
                        gain += 1
                if gain > best_gain:
                    best_gain = gain
                    best_idx = j
            if best_gain == 0:
                return None  # stuck -> infeasible
            # compute how many times we should press that button greedily:
            # limited by the smallest remaining count among the counters it affects
            ub = min((rem[i] for i in range(k) if cols[best_idx][i]), default=0)
            if ub <= 0:
                # fallback press once
                ub = 1
            # pressing ub times
            presses += ub
            for i in range(k):
                if cols[best_idx][i]:
                    rem[i] = max(0, rem[i] - ub)
            # loop continues
        # unreachable

    initial_ub = greedy_upper_bound()
    if initial_ub is None:
        return None
    best_global = initial_ub

    # Precompute for subset LB: for each subset S of counters, compute max coverage per press
    # We'll iterate 1..(1<<k)-1 subsets. For empty subset skip.
    subset_maxcov = {}
    subset_sumreq = {}
    for s in range(1, 1 << k):
        # S indices
        S_indices = [i for i in range(k) if (s >> i) & 1]
        sumreq = sum(target[i] for i in S_indices)
        maxcov = 0
        for j in range(m):
            cov = sum(1 for i in S_indices if cols[j][i])
            if cov > maxcov:
                maxcov = cov
        subset_maxcov[s] = maxcov
        subset_sumreq[s] = sumreq

    # lower bound function using all subsets: LB = max_S ceil(sumreq_S / maxcov_S)
    def lower_bound_on_total(rem):
        # rem is tuple/list of remaining requirements
        sumrem = sum(rem)
        if sumrem == 0:
            return 0
        lb = 0
        # full-sum simple bound: at least ceil(sumrem / max_cov_over_all_buttons)
        overall_maxcov = max(sum(cols[j][i] for i in range(k)) for j in range(m))
        if overall_maxcov == 0:
            return 10**18  # impossible
        lb = (sumrem + overall_maxcov - 1) // overall_maxcov
        # try subsets (k small)
        for s in range(1, 1 << k):
            maxcov = subset_maxcov[s]
            if maxcov == 0:
                # if any counter in subset has >0 and no button covers it, infeasible
                # but pre-check should have caught it
                continue
            ssum = 0
            bit = s
            idx = 0
            while bit:
                if bit & 1:
                    ssum += rem[idx]
                idx += 1
                bit >>= 1
            if ssum == 0:
                continue
            candidate = (ssum + maxcov - 1) // maxcov
            if candidate > lb:
                lb = candidate
        return lb

    # Memoization: map remaining target tuple -> best found cost from this state (or INF if impossible)
    INF = 10**18

    @lru_cache(maxsize=None)
    def dfs(rem_tuple):
        nonlocal best_global
        rem = list(rem_tuple)
        # finished?
        if all(x == 0 for x in rem):
            return 0
        # lower bound pruning:
        lb = lower_bound_on_total(rem)
        if lb >= best_global:
            return INF
        # Additional quick bound: sum of rem is at least lb (already)
        # Choose branching variable (button) heuristically:
        # choose button that covers the largest sum of remaining requirements (most impact)
        best_button = None
        best_impact = -1
        for j in range(m):
            impact = 0
            for i in range(k):
                if cols[j][i]:
                    impact += rem[i]
            if impact > best_impact:
                best_impact = impact
                best_button = j
        if best_impact <= 0:
            return INF  # stuck
        j = best_button
        # upper bound for this button: cannot press more than min_i rem[i] for i in its coverage
        ub = min((rem[i] for i in range(k) if cols[j][i]), default=0)
        # If button affects no counters, skip it
        if ub <= 0:
            # but other buttons might; find next best button
            # as fallback, iterate all buttons with ub>0
            candidates = [
                idx
                for idx in range(m)
                if any(cols[idx][i] and rem[i] > 0 for i in range(k))
            ]
        else:
            candidates = [j]

        best_here = INF

        # try candidate buttons; for each, try pressing from ub down to 0 (try larger presses first to find good solution quickly)
        for btn in candidates:
            ub_btn = min((rem[i] for i in range(k) if cols[btn][i]), default=0)
            # iterate number of presses t from ub_btn down to 0
            # small optimization: cap attempted t by best_global - 1 (if t >= best_global prune)
            max_try = min(ub_btn, best_global - 1)
            for t in range(max_try, -1, -1):
                if t == 0:
                    new_rem = tuple(rem)
                else:
                    new_rem_list = rem.copy()
                    for i in range(k):
                        if cols[btn][i]:
                            # subtract t but don't go negative
                            new_rem_list[i] = new_rem_list[i] - t
                            if new_rem_list[i] < 0:
                                new_rem_list[i] = 0
                    new_rem = tuple(new_rem_list)
                # Quick lower bound: cost_so_far + lb(new_rem) must be < best_global
                lb2 = lower_bound_on_total(new_rem)
                if t + lb2 >= best_global:
                    continue
                sub = dfs(new_rem)
                if sub != INF:
                    cand_total = t + sub
                    if cand_total < best_here:
                        best_here = cand_total
                        if cand_total < best_global:
                            best_global = cand_total
                # If best_here is 0 then can't get better
                if best_here == 0:
                    break
            if best_here == 0:
                break

        return best_here

    res = dfs(tuple(target))
    if res >= INF:
        return None
    return res


@register_solution(2025, 10, 2)
def part_two(input_data: list[str]):
    total = 0
    for line in input_data:
        target, buttons = parse_joltage_machine(line)  # returns Python lists
        presses = solve_machine_branch_and_bound(target, buttons)
        print(presses)  # optional, for debugging
        if presses is None:
            raise SolutionNotFoundError(2025, 10, 2)
        total += presses
    return total


if __name__ == "__main__":
    data = get_input_for_day(2025, 10)
    part_one(data)
    part_two(data)
