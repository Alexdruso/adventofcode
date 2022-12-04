from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_for_day
from itertools import starmap


@register_solution(2022, 4, 1)
def part_one(input_data: list[str]):
    input_data = map(lambda assignment_pair: assignment_pair.split(','), input_data)
    input_data = map(
        lambda assignment_pair: tuple(assignment.split('-') for assignment in assignment_pair),
        input_data
    )
    input_data = map(
        lambda assignment_pair: tuple(tuple(int(section) for section in assignment) for assignment in assignment_pair),
        input_data
    )
    input_data = starmap(
        lambda assignment_0, assignment_1: (
                (assignment_0[0] >= assignment_1[0] and assignment_0[1] <= assignment_1[1])
                or (assignment_1[0] >= assignment_0[0] and assignment_1[1] <= assignment_0[1])
        ),
        input_data
    )
    input_data = map(int, input_data)
    answer = sum(input_data)

    if not answer:
        raise SolutionNotFoundException(2022, 4, 1)

    return answer


@register_solution(2022, 4, 2)
def part_two(input_data: list[str]):
    input_data = map(lambda assignment_pair: assignment_pair.split(','), input_data)
    input_data = map(
        lambda assignment_pair: tuple(assignment.split('-') for assignment in assignment_pair),
        input_data
    )
    input_data = map(
        lambda assignment_pair: tuple(tuple(int(section) for section in assignment) for assignment in assignment_pair),
        input_data
    )
    input_data = starmap(
        lambda assignment_0, assignment_1: (
                assignment_1[0] <= assignment_0[0] <= assignment_1[1]
                or assignment_0[0] <= assignment_1[0] <= assignment_0[1]
        ),
        input_data
    )
    input_data = map(int, input_data)
    answer = sum(input_data)

    if not answer:
        raise SolutionNotFoundException(2022, 4, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2022, 4)
    part_one(data)
    part_two(data)
