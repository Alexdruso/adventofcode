

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_for_day


@register_solution(2023, 7, 1)
def part_one(input_data: list[str]):
    print(input_data)

    answer = ...

    if not answer:
        raise SolutionNotFoundException(2023, 7, 1)

    return answer


@register_solution(2023, 7, 2)
def part_two(input_data: list[str]):
    answer = ...

    if not answer:
        raise SolutionNotFoundException(2023, 7, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2023, 7)
    part_one(data)
    part_two(data)
