from adventofcode.year_2022.day_02_2022 import part_two, part_one

test_input = ['A Y',
              'B X',
              'C Z']


def test_part_one():
    assert part_one(test_input) == 15


def test_part_two():
    assert part_two(test_input) == 12
