from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_for_day


@register_solution(2025, 5, 1)
def part_one(input_data: list[str]):
    ranges = set()

    for index, line in enumerate(input_data):
        if line.strip() == "":
            break
        start, end = line.split("-")
        ranges.add(range(int(start), int(end) + 1))

    def is_in_ranges(num: int) -> bool:
        return any(num in range_elem for range_elem in ranges)

    answer = sum(
        1
        for ingredient in input_data[index + 1 :]
        if is_in_ranges(int(ingredient.strip()))
    )

    if not answer:
        raise SolutionNotFoundError(2025, 5, 1)

    return answer


@register_solution(2025, 5, 2)
def part_two(input_data: list[str]):
    answer = ...

    if not answer:
        raise SolutionNotFoundError(2025, 5, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2025, 5)
    part_one(data)
    part_two(data)
