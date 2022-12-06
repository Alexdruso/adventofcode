from adventofcode.year_2022.day_06_2022 import part_two, part_one


test_input = ['mjqjpqmgbljsphdztnvjfqwrcgsmlb']


def test_part_one():
    assert part_one(test_input) == 7


def test_part_two():
    assert part_two(test_input) == 19
