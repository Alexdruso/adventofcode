from typing import Tuple

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_for_day

from itertools import groupby
from collections import deque
from typing import Deque
from functools import reduce


def prepare_crates(crates: list[str]) -> list[Deque[str]]:
    num_towers = len(crates[-1].split())

    output = [deque() for _ in range(num_towers)]

    for line in crates[:-1]:
        for index in range(num_towers):
            if index * 4 + 1 >= len(line): break
            crate = line[index * 4 + 1]
            if crate != ' ': output[index].append(crate)

    return output


def _prepare_action(action: str) -> tuple[int, int, int]:
    temp = action.split()
    return int(temp[1]), int(temp[3]) - 1, int(temp[5]) - 1


def prepare_actions(actions: list[str]):
    return map(_prepare_action, actions)


@register_solution(2022, 5, 1)
def part_one(input_data: list[str]):
    crates, actions = [list(group) for k, group in groupby(input_data, lambda x: x == "") if not k]

    crates = prepare_crates(crates)
    actions = prepare_actions(actions)

    for num_crates, origin, destination in actions:
        for _ in range(num_crates):
            crate = crates[origin].popleft()
            crates[destination].appendleft(crate)

    answer = reduce(lambda crate1, crate2: crate1 + crate2, map(lambda tower: tower[0], crates))

    if not answer:
        raise SolutionNotFoundException(2022, 5, 1)

    return answer


@register_solution(2022, 5, 2)
def part_two(input_data: list[str]):
    crates, actions = [list(group) for k, group in groupby(input_data, lambda x: x == "") if not k]

    crates = prepare_crates(crates)
    actions = prepare_actions(actions)

    for num_crates, origin, destination in actions:
        temp = [crates[origin].popleft() for _ in range(num_crates)]
        temp.reverse()
        crates[destination].extendleft(temp)

    answer = reduce(lambda crate1, crate2: crate1 + crate2, map(lambda tower: tower[0], crates))

    if not answer:
        raise SolutionNotFoundException(2022, 5, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2022, 5)
    part_one(data)
    part_two(data)
