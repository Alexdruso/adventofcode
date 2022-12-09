from adventofcode.year_2022.day_09_2022 import part_two, part_one

test_input = [
    'R 5',
    'U 8',
    'L 8',
    'D 3',
    'R 17',
    'D 10',
    'L 25',
    'R 20',
]


def test_part_one():
    assert part_one(test_input) == 79


def test_part_two():
    assert part_two(test_input) == 36
