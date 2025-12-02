from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_for_day


@register_solution(2025, 2, 1)
def part_one(input_data: list[str]):
    input_data = input_data[0].split(",")

    input_data = (line.split("-") for line in input_data)

    input_data = ((int(start), int(end)) for (start, end) in input_data)

    answer = 0

    for start, end in input_data:
        # NOTE: this is dumb, there must be a better way
        for element in range(start, end + 1):
            element = str(element)

            if len(element) % 2 == 0:
                if element[: len(element) // 2] == element[len(element) // 2 :]:
                    answer += int(element)

    if not answer:
        raise SolutionNotFoundError(2025, 2, 1)

    return answer


@register_solution(2025, 2, 2)
def part_two(input_data: list[str]):
    answer = ...

    if not answer:
        raise SolutionNotFoundError(2025, 2, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2025, 2)
    part_one(data)
    part_two(data)
