from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_for_day
import numpy as np
from numpy import typing


def _get_input(input_data: list[str]) -> typing.NDArray:
    return np.array(
        [[int(number) for number in line.split()] for line in input_data],
        dtype=np.int32
    )


@register_solution(2023, 9, 1)
def part_one(input_data: list[str]):
    input_data = _get_input(input_data)

    state = input_data[:, -1]

    while not np.all(input_data == 0):
        input_data = np.diff(input_data)
        state += input_data[:, -1]

    answer = state.sum()

    if not answer:
        raise SolutionNotFoundException(2023, 9, 1)

    return answer


@register_solution(2023, 9, 2)
def part_two(input_data: list[str]):
    input_data = _get_input(input_data)[:, ::-1]

    state = input_data[:, -1]

    while not np.all(input_data == 0):
        input_data = np.diff(input_data)
        state += input_data[:, -1]

    answer = state.sum()

    if not answer:
        raise SolutionNotFoundException(2023, 9, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2023, 9)
    part_one(data)
    part_two(data)
