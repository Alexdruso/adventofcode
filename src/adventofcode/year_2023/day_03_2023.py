from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_for_day
from collections.abc import Iterator
from collections import defaultdict
from functools import reduce

directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]


def _adjacent_coordinates(row: int, column: int) -> Iterator[tuple[int, int]]:
    for dr, dc in directions:
        new_row, new_column = row + dr, column + dc
        yield new_row, new_column


def _valid_numbers(row_idx: int, row: str, symbols: set[tuple[int, int]]) -> Iterator[int]:
    valid = False
    temp = ''
    for index in range(len(row)):
        symbol = row[index]
        if ord(symbol) in range(ord('0'), ord('9') + 1):
            temp += symbol
            if not valid:
                valid = reduce(
                    lambda x, y: x or y in symbols,
                    _adjacent_coordinates(row_idx, index),
                    False
                )
        else:
            if valid:
                yield int(temp)
            valid = False
            temp = ''
    if valid:
        yield int(temp)


def _numbers_to_operators(row_idx: int, row: str, symbols: set[tuple[int, int]]) -> Iterator[
    tuple[int, set[tuple[int, int]]]]:
    linked_symbols: set[tuple[int, int]] = set()
    temp = ''
    for index in range(len(row)):
        symbol = row[index]
        if ord(symbol) in range(ord('0'), ord('9') + 1):
            temp += symbol
            linked_symbols |= {
                x
                for x in _adjacent_coordinates(row_idx, index)
                if x in symbols
            }
        else:
            if len(linked_symbols) > 0:
                yield int(temp), linked_symbols
            linked_symbols = set()
            temp = ''
    if len(linked_symbols) > 0:
        yield int(temp), linked_symbols


@register_solution(2023, 3, 1)
def part_one(input_data: list[str]):
    symbols = {
        (x, y)
        for x, row in enumerate(input_data)
        for y, symbol in enumerate(row)
        if symbol != '.'
           and ord(symbol) not in range(ord('0'), ord('9') + 1)
    }

    answer = sum(
        number
        for row_idx, row in enumerate(input_data)
        for number in _valid_numbers(row_idx, row, symbols)
    )

    if not answer:
        raise SolutionNotFoundException(2023, 3, 1)

    return answer


@register_solution(2023, 3, 2)
def part_two(input_data: list[str]):
    potential_gears = {
        (x, y)
        for x, row in enumerate(input_data)
        for y, symbol in enumerate(row)
        if symbol == '*'
    }

    operators_to_numbers = defaultdict(list)
    for row_idx, row in enumerate(input_data):
        for number, operators in _numbers_to_operators(row_idx, row, potential_gears):
            for operator in operators:
                operators_to_numbers[operator].append(number)

    answer = sum(
        reduce(lambda x, y: x * y, operators_to_numbers[operator], 1)
        for operator in potential_gears
        if len(operators_to_numbers[operator]) == 2
    )

    if not answer:
        raise SolutionNotFoundException(2023, 3, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2023, 3)
    part_one(data)
    part_two(data)
