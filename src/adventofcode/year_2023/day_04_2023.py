from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_for_day
from collections import defaultdict


def _won_scratchcards(scratchcard: str) -> int:
    winning_numbers, card = scratchcard.split(':')[1].split('|')
    winning_numbers = set(winning_numbers.split())
    card = set(card.split())

    return len(winning_numbers & card)


def _points(scratchcard: str) -> int:
    return int(2 ** (_won_scratchcards(scratchcard) - 1))


@register_solution(2023, 4, 1)
def part_one(input_data: list[str]):
    answer = sum(
        _points(scratchcard)
        for scratchcard
        in input_data
    )

    if not answer:
        raise SolutionNotFoundException(2023, 4, 1)

    return answer


@register_solution(2023, 4, 2)
def part_two(input_data: list[str]):
    scratchcards_number = [1] * len(input_data)

    for index, scratchcard in enumerate(input_data):
        won_scratchcards = _won_scratchcards(scratchcard)
        for won_scratchcard in range(index+1, index + won_scratchcards+1):
            scratchcards_number[won_scratchcard] += scratchcards_number[index]

    answer = sum(scratchcards_number)

    if not answer:
        raise SolutionNotFoundException(2023, 4, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2023, 4)
    part_one(data)
    part_two(data)
