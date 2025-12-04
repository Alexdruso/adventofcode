from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_for_day


@register_solution(2025, 4, 1)
def part_one(input_data: list[str]):
    answer = 0

    for x_idx, line in enumerate(input_data):
        for y_idx, element in enumerate(line):
            if element == "@":
                surrounding_papers = 0

                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if (
                            0 <= x_idx + dx < len(input_data)
                            and 0 <= y_idx + dy < len(line)
                            and not (dx == 0 and dy == 0)
                            and input_data[x_idx + dx][y_idx + dy] == "@"
                        ):
                            surrounding_papers += 1

                if surrounding_papers < 4:
                    answer += 1

    if not answer:
        raise SolutionNotFoundError(2025, 4, 1)

    return answer


@register_solution(2025, 4, 2)
def part_two(input_data: list[str]):
    answer = ...

    if not answer:
        raise SolutionNotFoundError(2025, 4, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2025, 4)
    part_one(data)
    part_two(data)
