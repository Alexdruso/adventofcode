

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_for_day

from itertools import groupby


@register_solution(2022, 1, 1)
def part_one(input_data: list[str]):
    input_data = [list(group) for k, group in groupby(input_data, lambda x: x == "") if not k]
    input_data = list(map(lambda elf: list(map(int, elf)), input_data))
    answer = max(map(sum, input_data))

    if not answer:
        raise SolutionNotFoundException(2022, 1, 1)

    return answer


@register_solution(2022, 1, 2)
def part_two(input_data: list[str]):
    input_data = [list(group) for k, group in groupby(input_data, lambda x: x == "") if not k]
    input_data = list(map(lambda elf: list(map(int, elf)), input_data))
    answer = sum(sorted(list(map(sum, input_data)))[-3:])

    if not answer:
        raise SolutionNotFoundException(2022, 1, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2022, 1)
    part_one(data)
    part_two(data)
