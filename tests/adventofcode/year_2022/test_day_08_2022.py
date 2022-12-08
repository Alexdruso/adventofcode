from adventofcode.year_2022.day_08_2022 import part_two, part_one

test_input = [
    '30373',
    '25512',
    '65332',
    '33549',
    '35390',
]


def test_part_one():
    assert part_one(test_input) == 21


def test_part_two():
    assert part_two(test_input) == 8
