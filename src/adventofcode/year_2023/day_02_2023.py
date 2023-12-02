from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_for_day
import re
from functools import reduce
from collections import defaultdict


def _id(game: str) -> int:
    return int(game.lstrip("Game ").split(':')[0])


limits = {
    "red": 12,
    "blue": 14,
    "green": 13
}


def _check_combo(combo: str) -> bool:
    number, color = combo.split()
    return int(number) <= limits[color]


def _is_possible(game: str) -> bool:
    game = game.split(': ')[1]
    game = re.split('; |, ', game)
    game = map(_check_combo, game)

    return reduce(lambda x, y: x and y, game, True)


@register_solution(2023, 2, 1)
def part_one(input_data: list[str]):
    answer = sum(_id(game) for game in input_data if _is_possible(game))

    if not answer:
        raise SolutionNotFoundException(2023, 2, 1)

    return answer


def _min_set(game: str) -> tuple[int, int, int]:
    game = game.split(': ')[1]
    game = re.split('; |, ', game)

    minimum_set = defaultdict(int)

    for number, color in map(lambda combo: combo.split(), game):
        minimum_set[color] = max(minimum_set[color], int(number))

    return minimum_set["red"], minimum_set["blue"], minimum_set["green"]


@register_solution(2023, 2, 2)
def part_two(input_data: list[str]):
    answer = sum(
        reduce(
            lambda x, y: x * y,
            _min_set(game),
            1)
        for game in input_data
    )

    if not answer:
        raise SolutionNotFoundException(2023, 2, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2023, 2)
    part_one(data)
    part_two(data)
