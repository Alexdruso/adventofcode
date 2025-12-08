from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_for_day
import numpy as np


@register_solution(2025, 6, 1)
def part_one(input_data: list[str]):
    input_data = [line.split() for line in input_data]

    numbers = np.asarray(input_data[:-1], dtype=int).T
    commands = input_data[-1]

    answer = sum(
        column.sum() if command == "+" else column.prod()
        for column, command in zip(numbers, commands)
    )

    if not answer:
        raise SolutionNotFoundError(2025, 6, 1)

    return answer


@register_solution(2025, 6, 2)
def part_two(input_data: list[str]):
    answer = ...

    if not answer:
        raise SolutionNotFoundError(2025, 6, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2025, 6)
    part_one(data)
    part_two(data)
