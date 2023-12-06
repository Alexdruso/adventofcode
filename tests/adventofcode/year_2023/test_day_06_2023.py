from adventofcode.year_2023.day_06_2023 import part_two, part_one

test_input = [
    "Time:      7  15   30",
    "Distance:  9  40  200"
]


def test_part_one():
    assert part_one(test_input) == 288


def test_part_two():
    assert part_two(test_input) == 71503
