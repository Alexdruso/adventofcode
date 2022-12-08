
from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_for_day
import numpy as np


@register_solution(2022, 8, 1)
def part_one(input_data: list[str]):
    input_data = np.array([[element for element in row] for row in input_data], dtype=np.uint8)
    num_rows, num_cols = input_data.shape
    visible = np.ones(shape=(num_rows, num_cols), dtype=bool)
    for row in range(1, num_rows - 1):
        for column in range(1, num_cols - 1):
            height = input_data[row, column]
            visible[row, column] = (
                height > input_data[row + 1:, column].max()
                or height > input_data[:row, column].max()
                or height > input_data[row, column + 1:].max()
                or height > input_data[row, :column].max()
            )
    answer = visible.sum()

    if not answer:
        raise SolutionNotFoundException(2022, 8, 1)

    return answer


@register_solution(2022, 8, 2)
def part_two(input_data: list[str]):
    input_data = np.array([[int(element) for element in row] for row in input_data])
    num_rows, num_cols = input_data.shape
    scenic_score = np.zeros(shape=(num_rows, num_cols), dtype=np.uint32)
    for row in range(1, num_rows - 1):
        for column in range(1, num_cols - 1):

            height = input_data[row, column]

            scenic_score[row, column] = (
                (np.argwhere(height <= input_data[row + 1:, column]).min(initial=num_rows-row-2) + 1)
                * (row - np.argwhere(height <= input_data[: row, column]).max(initial=0))
                * (np.argwhere(height <= input_data[row, column + 1:]).min(initial=num_cols-column-2) + 1)
                * (column - np.argwhere(height <= input_data[row, : column]).max(initial=0))
            )

    answer = scenic_score.max()

    if not answer:
        raise SolutionNotFoundException(2022, 8, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2022, 8)
    part_one(data)
    part_two(data)
