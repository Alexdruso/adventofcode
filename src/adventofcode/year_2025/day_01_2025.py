from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_for_day
from itertools import accumulate


@register_solution(2025, 1, 1)
def part_one(input_data: list[str]):
    answer = ((-1 if line[0] == "L" else 1) * int(line[1:]) for line in input_data)

    answer = accumulate(answer, initial=50)

    answer = (element % 100 for element in answer)

    answer = len([element for element in answer if element == 0])

    if not answer:
        raise SolutionNotFoundError(2025, 1, 1)

    return answer


@register_solution(2025, 1, 2)
def part_two(input_data: list[str]):
    answer = ...

    if not answer:
        raise SolutionNotFoundError(2025, 1, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2025, 1)
    part_one(data)
    part_two(data)
