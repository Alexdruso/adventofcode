from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_for_day


@register_solution(2025, 12, 1)
def part_one(input_data: list[str]):
    answer = ...

    if not answer:
        raise SolutionNotFoundError(2025, 12, 1)

    return answer


@register_solution(2025, 12, 2)
def part_two(input_data: list[str]):
    answer = ...

    if not answer:
        raise SolutionNotFoundError(2025, 12, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2025, 12)
    part_one(data)
    part_two(data)
