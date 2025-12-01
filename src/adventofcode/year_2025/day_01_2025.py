from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_for_day
from itertools import accumulate


@register_solution(2025, 1, 1)
def part_one(input_data: list[str]):
    answer = (
        (-int(line[1:]) if line[0] == "L" else int(line[1:])) for line in input_data
    )

    answer = accumulate(answer, initial=50)

    answer = (element % 100 for element in answer)

    answer = len([element for element in answer if element == 0])

    if not answer:
        raise SolutionNotFoundError(2025, 1, 1)

    return answer


@register_solution(2025, 1, 2)
def part_two(input_data: list[str]):
    moves = [
        (-int(line[1:]) if line[0] == "L" else int(line[1:])) for line in input_data
    ]

    position = 50
    crossings = 0

    for delta in moves:
        sign = 1 if delta > 0 else -1
        steps = abs(delta)

        # Solve for k in 1..steps such that (pos + k*sign) % 100 == 0
        # smallest positive k satisfying this is r = (-pos * sign) % 100
        # if r == 0 then the smallest positive hit is at k = 100
        rotations = (-position * sign) % 100
        if rotations == 0:
            rotations = 100

        if rotations <= steps:
            crossings += 1 + (steps - rotations) // 100

        position = (position + delta) % 100

    answer = crossings

    if not answer:
        raise SolutionNotFoundError(2025, 1, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2025, 1)
    part_one(data)
    part_two(data)
