from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_for_day
import re
from string import digits

spelled = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def _to_number(line: str) -> int:
    answer = [
        character
        for character
        in line
        if ord(character) in range(ord('0'), ord('9') + 1)
    ]

    return int(answer[0] + answer[-1])


def _to_number_v2(line: str) -> int:
    numbers = []
    for d in digits:
        idx = line.find(d)
        if idx != -1:
            numbers.append((idx, d))
        idx = line.rfind(d)
        if idx != -1:
            numbers.append((idx, d))
    for d, v in spelled.items():
        idx = line.find(d)
        if idx != -1:
            numbers.append((idx, v))
        idx = line.rfind(d)
        if idx != -1:
            numbers.append((idx, v))
    numbers.sort()
    return int(numbers[0][1] + numbers[-1][1])


@register_solution(2023, 1, 1)
def part_one(input_data: list[str]):
    answer = sum(_to_number(line) for line in input_data)

    if not answer:
        raise SolutionNotFoundException(2023, 1, 1)

    return answer


@register_solution(2023, 1, 2)
def part_two(input_data: list[str]):
    answer = sum(_to_number_v2(line) for line in input_data)

    if not answer:
        raise SolutionNotFoundException(2023, 1, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2023, 1)
    part_one(data)
    part_two(data)
