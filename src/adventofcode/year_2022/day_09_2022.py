from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_for_day

command_out = {
    'U': 1,
    'D': -1,
    'L': -1j,
    'R': 1j
}


def _distance(x, y):
    return max(abs(x.real - y.real), abs(x.imag - y.imag))


@register_solution(2022, 9, 1)
def part_one(input_data: list[str]):
    input_data = map(lambda command: command.split(), input_data)
    input_data = ((command, int(repetition)) for command, repetition in input_data)
    input_data = (command for command, repetition in input_data for _ in range(repetition))
    current_head_position = current_tail_position = 0j
    visited = {current_tail_position}

    for command in input_data:
        temp = current_head_position
        current_head_position = current_head_position + command_out[command]
        if _distance(current_head_position, current_tail_position) > 1:
            current_tail_position = temp
            visited.add(current_tail_position)

    answer = len(visited)

    if not answer:
        raise SolutionNotFoundException(2022, 9, 1)

    return answer


@register_solution(2022, 9, 2)
def part_two(input_data: list[str]):
    input_data = map(lambda command: command.split(), input_data)
    input_data = ((command, int(repetition)) for command, repetition in input_data)
    input_data = (command for command, repetition in input_data for _ in range(repetition))
    current_positions = [0j for _ in range(10)]
    visited = {current_positions[-1]}

    for command in input_data:
        current_positions[0] += command_out[command]

        for index in range(1, len(current_positions)):
            if _distance(current_positions[index-1], current_positions[index]) > 1:
                if current_positions[index].imag == current_positions[index-1].imag:
                    current_positions[index] += 1 if current_positions[index-1].real > current_positions[index].real else -1
                elif current_positions[index].real == current_positions[index-1].real:
                    current_positions[index] += 1j if current_positions[index - 1].imag > current_positions[index].imag else -1j
                else:
                    current_positions[index] += 1 if current_positions[index - 1].real > current_positions[index].real else -1
                    current_positions[index] += 1j if current_positions[index - 1].imag > current_positions[index].imag else -1j

        visited.add(current_positions[-1])

    answer = len(visited)

    if not answer:
        raise SolutionNotFoundException(2022, 9, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2022, 9)
    part_one(data)
    part_two(data)
