from adventofcode.year_2022.day_04_2022 import part_two, part_one

test_input = [
    '2-4,6-8',
    '2-3,4-5',
    '5-7,7-9',
    '2-8,3-7',
    '6-6,4-6',
    '2-6,4-8'
]


def test_part_one():
    assert part_one(test_input) == 2


def test_part_two():
    assert part_two(test_input) == 4
