from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_for_day
from functools import reduce
from math import sqrt, ceil, floor


def _ways_to_win(time: int, distance: int) -> int:
    # (-time - sqrt(time**2 - 4 * (distance)))/-2 <= hold_button <= (-time + sqrt(time**2 - 4 * (distance)))/-2
    delta = time ** 2 - 4 * distance
    return ceil((time + sqrt(delta)) / 2 - 1) - floor((time - sqrt(delta)) / 2 + 1) + 1


@register_solution(2023, 6, 1)
def part_one(input_data: list[str]):
    times = (int(time) for time in input_data[0].split()[1:])
    distances = (int(distance) for distance in input_data[1].split()[1:])

    answer = reduce(
        lambda x, y: x * y,
        (_ways_to_win(time, distance) for time, distance in zip(times, distances)),
        1
    )

    if not answer:
        raise SolutionNotFoundException(2023, 6, 1)

    return answer


@register_solution(2023, 6, 2)
def part_two(input_data: list[str]):
    answer = _ways_to_win(
        int("".join(input_data[0].split()[1:])),
        int("".join(input_data[1].split()[1:]))
    )

    if not answer:
        raise SolutionNotFoundException(2023, 6, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2023, 6)
    part_one(data)
    part_two(data)
