from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_for_day
from functools import reduce

priority = {
    chr(index + ord('a') - 1): index for index in range(1, 27)
} | {
    chr(index + ord('A') - 27): index for index in range(27, 53)
}


@register_solution(2022, 3, 1)
def part_one(input_data: list[str]):
    solution = map(
        lambda rucksack: (rucksack[:len(rucksack) // 2], rucksack[len(rucksack) // 2:]),
        input_data
    )

    solution = map(
        lambda rucksack: (set(rucksack[0]), set(rucksack[1])),
        solution
    )

    solution = map(
        lambda rucksack: rucksack[0] & rucksack[1],
        solution
    )

    solution = map(lambda rucksack: rucksack.pop(), solution)
    solution = map(priority.get, solution)
    answer = sum(solution)
    if not answer:
        raise SolutionNotFoundException(2022, 3, 1)

    return answer


@register_solution(2022, 3, 2)
def part_two(input_data: list[str]):
    solution = map(set, input_data)
    solution = list(solution)
    solution = [solution[index:index+3] for index in range(0, len(solution) - 2, 3)]
    solution = map(lambda team: reduce(lambda member_1, member_2: member_1 & member_2, team), solution)
    solution = map(lambda common_item: common_item.pop(), solution)
    solution = map(priority.get, solution)
    answer = sum(solution)

    if not answer:
        raise SolutionNotFoundException(2022, 3, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2022, 3)
    part_one(data)
    part_two(data)
