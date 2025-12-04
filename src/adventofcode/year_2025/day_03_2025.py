from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_for_day


@register_solution(2025, 3, 1)
def part_one(input_data: list[str]):
    results = []

    for line in input_data:
        idx_max = 0
        max_digit = "0"

        for index, digit in enumerate(line[:-1]):
            if digit > max_digit:
                max_digit = digit
                idx_max = index

        result = line[idx_max] + max(list(line)[idx_max + 1 : :])
        results.append(int(result))

    answer = sum(results)

    if not answer:
        raise SolutionNotFoundError(2025, 3, 1)

    return answer


@register_solution(2025, 3, 2)
def part_two(input_data: list[str]):
    n_digits_needed = 12

    answer = 0

    for line in input_data:
        result = ""
        for digits_left in range(n_digits_needed, 0, -1):
            idx_max = 0
            max_digit = "0"

            for index, digit in enumerate(line[: len(line) - digits_left + 1]):
                if digit > max_digit:
                    max_digit = digit
                    idx_max = index

            result += line[idx_max]
            line = line[idx_max + 1 : :]

        answer += int(result)

    if not answer:
        raise SolutionNotFoundError(2025, 3, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2025, 3)
    part_one(data)
    part_two(data)
