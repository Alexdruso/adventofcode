from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_for_day

points = {
    'A X': 4,
    'A Y': 8,
    'A Z': 3,
    'B X': 1,
    'B Y': 5,
    'B Z': 9,
    'C X': 7,
    'C Y': 2,
    'C Z': 6,
}

actions = {
    'A X': 'Z',
    'A Y': 'X',
    'A Z': 'Y',
    'B X': 'X',
    'B Y': 'Y',
    'B Z': 'Z',
    'C X': 'Y',
    'C Y': 'Z',
    'C Z': 'X',
}


@register_solution(2022, 2, 1)
def part_one(input_data: list[str]):

    answer = sum(map(points.get, input_data))

    if not answer:
        raise SolutionNotFoundException(2022, 2, 1)

    return answer


@register_solution(2022, 2, 2)
def part_two(input_data: list[str]):

    answer = sum(
        map(
            points.get,
            map(
                lambda line: line[0] + ' ' + actions[line],
                input_data
            )
        )
    )

    if not answer:
        raise SolutionNotFoundException(2022, 2, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2022, 2)
    part_one(data)
    part_two(data)
