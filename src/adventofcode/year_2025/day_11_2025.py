from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_for_day

import networkx as nx


@register_solution(2025, 11, 1)
def part_one(input_data: list[str]):
    G = nx.DiGraph()

    for line in input_data:
        if not line.strip():
            continue
        left, right = line.split(":")
        src = left.strip()
        targets = right.strip().split()
        for dst in targets:
            G.add_edge(src, dst)

    try:
        count = sum(1 for _ in nx.all_simple_paths(G, source="you", target="out"))
    except nx.NetworkXNoPath:
        raise SolutionNotFoundError(2025, 11, 1)

    if count is None:
        raise SolutionNotFoundError(2025, 11, 1)

    return count


@register_solution(2025, 11, 2)
def part_two(input_data: list[str]):
    G = nx.DiGraph()

    for line in input_data:
        if not line.strip():
            continue
        left, right = line.split(":")
        src = left.strip()
        targets = right.strip().split()
        for dst in targets:
            G.add_edge(src, dst)

    result = (set(path) for path in nx.all_simple_paths(G, source="svr", target="out"))

    result = (1 for path in result if ("dac" in path and "fft" in path))
    result = sum(result)

    if result is None:
        raise SolutionNotFoundError(2025, 11, 1)

    return result


if __name__ == "__main__":
    data = get_input_for_day(2025, 11)
    part_one(data)
    part_two(data)
