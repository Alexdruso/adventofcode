from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_for_day


@register_solution(2025, 5, 1)
def part_one(input_data: list[str]):
    ranges = []

    for index, line in enumerate(input_data):
        if line.strip() == "":
            break
        start, end = line.split("-")
        ranges.append((int(start), int(end) + 1))

    def is_in_ranges(num: int) -> bool:
        return any(start <= num < end for start, end in ranges)

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
    ranges = set()

    for line in input_data:
        if line.strip() == "":
            break
        start, end = line.split("-")
        ranges.add((int(start), int(end) + 1))

    merged = []
    for start, end in sorted(ranges):
        if merged and start <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            merged.append((start, end))

    answer = sum(end - start for start, end in merged)

    if not answer:
        raise SolutionNotFoundError(2025, 5, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2025, 5)
    part_one(data)
    part_two(data)
