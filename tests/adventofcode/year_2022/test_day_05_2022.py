from adventofcode.year_2022.day_05_2022 import part_two, part_one

test_input = [
    '    [D]',
    '[N] [C]',
    '[Z] [M] [P]',
    ' 1   2   3',
    '',
    'move 1 from 2 to 1',
    'move 3 from 1 to 3',
    'move 2 from 2 to 1',
    'move 1 from 1 to 2',
]


def test_part_one():
    assert part_one(test_input) == 'CMZ'


def test_part_two():
    assert part_two(test_input) == 'MCD'
