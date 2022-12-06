

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_for_day


@register_solution(2022, 6, 1)
def part_one(input_data: list[str]):
    signal = input_data[0]
    string_length = len(signal)
    input_data = map(lambda index: signal[index:index+4], range(0, string_length-4))
    input_data = filter(lambda item: len(set(item[1])) == len(item[1]), zip(range(4, string_length+1), input_data))
    input_data = map(lambda item: item[0], input_data)
    answer = next(input_data)

    if not answer:
        raise SolutionNotFoundException(2022, 6, 1)

    return answer


@register_solution(2022, 6, 2)
def part_two(input_data: list[str]):
    signal = input_data[0]
    string_length = len(signal)
    input_data = map(lambda index: signal[index:index+14], range(0, string_length-14))
    input_data = filter(lambda item: len(set(item[1])) == len(item[1]), zip(range(14, string_length+1), input_data))
    input_data = map(lambda item: item[0], input_data)
    answer = next(input_data)

    if not answer:
        raise SolutionNotFoundException(2022, 6, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2022, 6)
    part_one(data)
    part_two(data)
