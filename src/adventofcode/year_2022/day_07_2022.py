from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_for_day
from collections import defaultdict
import os


def _parse(lines):
    cwd, sizes = '/', defaultdict(int)
    for line in lines:
        match line.split():
            case ('$', 'ls') | ('dir', *_):
                continue
            case ('$', 'cd', path):
                cwd = os.path.join(cwd, path)
            case (size, *_):
                cwd = os.path.normpath(cwd)
                size = int(size)
                path = '/'
                for directory in cwd.split('/'):
                    path += directory
                    sizes[path] += size
    return sizes


@register_solution(2022, 7, 1)
def part_one(input_data: list[str]):
    answer = sum(filter(lambda size: size <= 100000, _parse(input_data).values()))

    if not answer:
        raise SolutionNotFoundException(2022, 7, 1)

    return answer


@register_solution(2022, 7, 2)
def part_two(input_data: list[str]):
    sizes = _parse(input_data)

    space_to_free = 30000000-(70000000 - sizes['/'])

    answer = next(
        filter(
            lambda value: value >= space_to_free,
            sorted(sizes.values())
        )
    )

    if not answer:
        raise SolutionNotFoundException(2022, 7, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2022, 7)
    part_one(data)
    part_two(data)
