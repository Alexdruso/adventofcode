from adventofcode.year_2023.day_08_2023 import part_two, part_one

test_input = [
    "RL",
    "",
    "AAA = (BBB, CCC)",
    "BBB = (DDD, EEE)",
    "CCC = (ZZZ, GGG)",
    "DDD = (DDD, DDD)",
    "EEE = (EEE, EEE)",
    "GGG = (GGG, GGG)",
    "ZZZ = (ZZZ, ZZZ)",
]


def test_part_one():
    assert part_one(test_input) == 2


def test_part_two():
    assert part_two(test_input) == 2
