from adventofcode.year_2022.day_03_2022 import part_two, part_one


test_input = [
'vJrwpWtwJgWrhcsFMMfFFhFp',
'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
'PmmdzqPrVvPwwTWBwg',
'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
'ttgJtRGJQctTZtZT',
'CrZsJsPPZsGzwwsLwLmpwMDw'
]


def test_part_one():
    assert part_one(test_input) == 157


def test_part_two():
    assert part_two(test_input) == 70
