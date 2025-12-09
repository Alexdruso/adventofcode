from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_for_day
import itertools


@register_solution(2025, 9, 1)
def part_one(input_data: list[str]):
    coordinates = [
        (int(x), int(y)) for x, y in (line.split(",") for line in input_data)
    ]

    pairs = itertools.combinations(coordinates, 2)

    answer = max(abs(x1 - x2 + 1) * abs(y1 - y2 + 1) for ((x1, y1), (x2, y2)) in pairs)

    if not answer:
        raise SolutionNotFoundError(2025, 9, 1)

    return answer


@register_solution(2025, 9, 2)
def part_two(input_data: list[str]):
    answer = ...

    if not answer:
        raise SolutionNotFoundError(2025, 9, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2025, 9)
    part_one(data)
    part_two(data)
