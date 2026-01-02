from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_for_day
from typing import NamedTuple


class Region(NamedTuple):
    area: int
    shape_number: tuple[int, ...]


class ParsedInput(NamedTuple):
    shapes_to_area: dict[str, int]
    regions: list[Region]


def parse_input(input_data: list[str]) -> ParsedInput:
    lines = [line.strip() for line in input_data]

    # Find the split point between shapes and regions
    split_index = next(
        (idx for idx, line in enumerate(lines) if "x" in line), len(lines)
    )

    shapes_lines = lines[:split_index]
    regions_lines = lines[split_index:]

    # Parse shapes
    shapes_to_area = {}
    current_shape_index = None
    grid = []

    for line in shapes_lines:
        if not line:
            continue
        if ":" in line and "x" not in line:
            # Finish previous shape if any
            if current_shape_index is not None:
                shape_area = sum(row.count("#") for row in grid)
                shapes_to_area[current_shape_index] = shape_area
            # Start new shape
            current_shape_index = line.split(":")[0].strip()
            grid = []
        else:
            # Add grid row
            grid.append(line)

    # Finish the last shape
    if current_shape_index is not None:
        shape_area = sum(row.count("#") for row in grid)
        shapes_to_area[current_shape_index] = shape_area

    # Parse regions
    regions = []
    for line in regions_lines:
        if not line or "x" not in line:
            continue
        size_str, counts_str = line.split(":", 1)
        width, height = map(int, size_str.split("x"))
        region_area = width * height
        shape_counts = tuple(map(int, counts_str.split()))
        regions.append(Region(area=region_area, shape_number=shape_counts))

    return ParsedInput(shapes_to_area=shapes_to_area, regions=regions)


@register_solution(2025, 12, 1)
def part_one(input_data: list[str]):
    parsed_input = parse_input(input_data)

    print(parsed_input.regions)

    answer = sum(
        1
        for region in parsed_input.regions
        if sum(
            count * parsed_input.shapes_to_area.get(str(idx), 0)
            for idx, count in enumerate(region.shape_number)
        )
        <= region.area
    )

    if not answer:
        raise SolutionNotFoundError(2025, 12, 1)

    return answer


@register_solution(2025, 12, 2)
def part_two(input_data: list[str]):
    answer = ...

    if not answer:
        raise SolutionNotFoundError(2025, 12, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2025, 12)
    part_one(data)
    part_two(data)
