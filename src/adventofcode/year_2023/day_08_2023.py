from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_for_day
from itertools import cycle
from collections.abc import Iterator
from math import lcm

START: str = 'AAA'
END: str = 'ZZZ'


def _map_move(move: str) -> int:
    return 0 if move == 'L' else 1


def _steps(moves: Iterator[int] | list[int], game_map: dict[str, list[str]], start=START) -> int:
    current_node = start
    for step, move in enumerate(cycle(moves), 1):
        current_node = game_map[current_node][move]
        if current_node.endswith('Z'):
            return step


@register_solution(2023, 8, 1)
def part_one(input_data: list[str]):
    moves = (_map_move(move) for move in input_data[0])

    input_data = map(
        lambda line: line.split(' = '),
        input_data[2:]
    )

    game_map = {
        node: link.lstrip('(').rstrip(')').split(', ')
        for node, link in input_data
    }

    answer = _steps(moves, game_map)

    if not answer:
        raise SolutionNotFoundException(2023, 8, 1)

    return answer


@register_solution(2023, 8, 2)
def part_two(input_data: list[str]):
    moves = [_map_move(move) for move in input_data[0]]

    input_data: Iterator[list[str]] = map(
        lambda line: line.split(' = '),
        input_data[2:]
    )

    game_map: dict[str, list[str]] = {
        node: link.lstrip('(').rstrip(')').split(', ')
        for node, link in input_data
    }

    starting_nodes = (node for node in game_map.keys() if node.endswith('A'))
    steps = []

    for starting_node in starting_nodes:
        steps.append(_steps(moves, game_map, starting_node))

    answer = lcm(*steps)

    if not answer:
        raise SolutionNotFoundException(2023, 8, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2023, 8)
    part_one(data)
    part_two(data)
