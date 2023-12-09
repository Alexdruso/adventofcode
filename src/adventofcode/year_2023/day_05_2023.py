from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_for_day
from collections.abc import Iterator


def _seeds(seeds: str) -> Iterator[int]:
    return (int(seed) for seed in seeds.lstrip('seeds:').split())


def _apply_map(seed: int, transformation_map: list[tuple[int, int, int]]):
    for destination_start, source_start, range_len in transformation_map:
        source_range = range(source_start, source_start + range_len)
        if seed in source_range:
            return destination_start + (seed - source_start)
    return seed


@register_solution(2023, 5, 1)
def part_one(input_data: list[str]):
    print(input_data)
    seeds = _seeds(input_data.pop(0))
    transformation_maps = []
    transformation_map = []
    for line in input_data:
        if line == "" or line.endswith("map:"):
            transformation_maps.append(transformation_map)
            transformation_map = []
        else:
            transformation_map.append(tuple(int(number) for number in line.split()))

    for transformation_map in transformation_maps:
        seeds = [_apply_map(seed, transformation_map) for seed in seeds]
        print(seeds)

    answer = min(seeds)

    if not answer:
        raise SolutionNotFoundException(2023, 5, 1)

    return answer


@register_solution(2023, 5, 2)
def part_two(input_data: list[str]):
    answer = ...

    if not answer:
        raise SolutionNotFoundException(2023, 5, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2023, 5)
    part_one(data)
    part_two(data)
