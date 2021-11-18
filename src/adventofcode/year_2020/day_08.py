from typing import List, Tuple

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


OPERATION_ACC = 'acc'
OPERATION_JMP = 'jmp'
OPERATION_NOP = 'nop'


@solution_timer(2020, 8, 1)
def part_one(input_data: List[str]) -> int:
    instructions = [parse_instruction(line) for line in input_data]
    accumulator = isolation_run(instructions)
    return accumulator[0]


@solution_timer(2020, 8, 2)
def part_two(input_data: List[str]) -> int:
    instructions = [parse_instruction(line) for line in input_data]
    accumulator = correcting_run(instructions)
    return accumulator


def parse_instruction(line: str) -> Tuple[str, int]:
    parsed = line.split(' ')
    operation = parsed[0]
    argument = int(parsed[1])
    return operation, argument


def isolation_run(instructions: List[Tuple[str, int]]) -> Tuple[int, int]:
    accumulator = 0
    idx = 0
    seen_idxs = []

    while idx not in seen_idxs:
        if idx == len(instructions):
            return accumulator, 1

        seen_idxs.append(idx)
        operation, argument = instructions[idx]

        if operation == OPERATION_NOP:
            idx += 1
        elif operation == OPERATION_ACC:
            accumulator += argument
            idx += 1
        elif operation == OPERATION_JMP:
            idx += argument
        else:
            raise ValueError('unrecognized operation received')

    return accumulator, 0


def verify_correction(instructions: List[Tuple[str, int]]) -> int:
    return len([i for i in instructions if i[0] == OPERATION_JMP and i[1] == 0]) == 0


def correcting_run(instructions: List[Tuple[str, int]]) -> int:
    for idx, (operation, argument) in enumerate(instructions):
        if operation in [OPERATION_JMP, OPERATION_NOP]:
            if operation == OPERATION_JMP:
                instructions[idx] = OPERATION_NOP, argument
            elif operation == OPERATION_NOP:
                instructions[idx] = OPERATION_JMP, argument
            accumulator, end_code = isolation_run(instructions)

            if end_code == 1:
                return accumulator
            else:
                instructions[idx] = operation, argument


if __name__ == '__main__':
    data = get_input_for_day(2020, 8)
    part_one(data)
    part_two(data)
