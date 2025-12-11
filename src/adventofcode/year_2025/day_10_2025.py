from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_for_day
import numpy as np


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


def parse_machine_joltage(line: str):
    """
    Parse one line into (targets, buttons, n)
    - targets: list[int] target integer counters (from {...})
    - buttons: list[list[int]] each button's affected counter indices
    - n: number of counters
    """
    parts = line.strip().split()
    if not parts:
        return [], [], 0

    # diagram may be first (ignore for part 2), then parentheses and curly braces
    # find the curly-brace token for targets
    curly_token = None
    for p in parts:
        if p.startswith("{") and p.endswith("}"):
            curly_token = p
            break
    if curly_token is None:
        # try concatenated tokens (space separated values unlikely but handle)
        raise ValueError(f"Missing joltage target specification in line: {line}")

    inside = curly_token[1:-1].strip()
    if inside == "":
        targets = []
    else:
        targets = [int(x) for x in inside.split(",")]
    n = len(targets)

    # collect button specs: tokens that start with '(' and end with ')'
    buttons = []
    for p in parts:
        if p.startswith("(") and p.endswith(")"):
            inner = p[1:-1].strip()
            if inner == "":
                buttons.append([])
            else:
                buttons.append([int(x) for x in inner.split(",")])
    return targets, buttons, n


@register_solution(2025, 10, 2)
def part_two(input_data: list[str]):
    total_presses = 0

    # delayed import of cvxpy so we can raise a helpful error
    try:
        import cvxpy as cp
    except Exception as e:
        raise RuntimeError(
            "cvxpy is required for part_two but could not be imported. "
            "Install it with `pip install cvxpy` and a compatible solver (GLPK or ECOS)."
        ) from e

    for line in input_data:
        if not line.strip():
            continue
        targets, buttons, n = parse_machine_joltage(line)
        m = len(buttons)

        # Trivial case: no counters
        if n == 0:
            continue

        # Build integer matrix A of shape (n, m)
        A = np.zeros((n, m), dtype=int)
        for j, b in enumerate(buttons):
            for idx in b:
                if idx < 0 or idx >= n:
                    raise ValueError(
                        f"Button index {idx} out of range for line: {line}"
                    )
                A[idx, j] += (
                    1  # counts are additive; but entries are 0/1 in given input
                )

        b = np.array(targets, dtype=int)

        # If there are no buttons but targets nonzero -> infeasible
        if m == 0:
            if np.any(b != 0):
                raise SolutionNotFoundError(2025, 10, 2)
            else:
                continue

        # cvxpy integer variable (nonnegative)
        x = cp.Variable(m, integer=True, nonneg=True)

        constraints = [A @ x == b]

        objective = cp.Minimize(cp.sum(x))

        prob = cp.Problem(objective, constraints)

        # Try GLPK_MI first, else ECOS_BB as fallback
        solved = False
        for solver in ("GLPK_MI", "ECOS_BB"):
            try:
                prob.solve(solver=solver, verbose=False)
                solved = True
                break
            except Exception:
                # try next solver
                solved = False

        if not solved:
            # Try default solve (may still work)
            try:
                prob.solve()
                solved = True
            except Exception as e:
                raise RuntimeError(
                    "CVXPY failed to solve the integer program. Ensure a mixed-integer solver is available "
                    "(GLPK_MI or ECOS_BB are recommended)."
                ) from e

        # Check feasibility and extract integer solution
        if x.value is None:
            raise SolutionNotFoundError(2025, 10, 2)

        # numerical rounding to nearest integer (should be integral)
        x_sol = np.rint(x.value).astype(int)

        # verify solution exactly satisfies constraints (A @ x_sol == b)
        if not np.array_equal(A.dot(x_sol), b):
            # It's possible solver returned fractional/inexact result; try to round and re-check
            raise SolutionNotFoundError(2025, 10, 2)

        # ensure non-negative
        if np.any(x_sol < 0):
            raise SolutionNotFoundError(2025, 10, 2)

        total_presses += int(np.sum(x_sol))

    if total_presses is None:
        raise SolutionNotFoundError(2025, 10, 2)

    return total_presses


if __name__ == "__main__":
    data = get_input_for_day(2025, 10)
    part_one(data)
    part_two(data)
