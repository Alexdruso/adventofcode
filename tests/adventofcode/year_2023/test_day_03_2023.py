from adventofcode.year_2023.day_03_2023 import part_two, part_one

test_input = [
    "12.......*..",
    "+.........34",
    ".......-12..",
    "..78........",
    "..*....60...",
    "78..........",
    ".......23...",
    "....90*12...",
    "............",
    "2.2......12.",
    ".*.........*",
    "1.1.......56",
]


def test_part_one():
    assert part_one(test_input) == 413


def test_part_two():
    assert part_two(test_input) == 'x'
