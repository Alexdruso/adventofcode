from __future__ import annotations
from typing import List, Generator

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


class Fish:
    def __init__(self, internal_timer: int = 8):
        self.internal_timer = internal_timer
        self.can_spawn = False

    def __eq__(self, other):
        if not isinstance(other, Fish):
            return False

        return self.internal_timer == other.internal_timer

    def __str__(self):
        return str(self.internal_timer)

    def __repr__(self):
        return str(self)

    def live_a_day(self):
        if self.internal_timer == 0:
            self.internal_timer = 6
            self.can_spawn = True
        else:
            self.internal_timer -= 1

    def spawn_offspring(self) -> Fish:
        if not self.can_spawn:
            raise ValueError('cannot spawn offspring too quick')

        self.can_spawn = False
        return Fish()


def get_starting_fish(input_data: List[str]) -> Generator[Fish, None, None]:
    for x in map(int, input_data[0].split(',')):
        yield Fish(x)


def iterate_day(fish: List[Fish]) -> List[Fish]:
    new_fish: List[Fish] = []

    for f in fish:
        f.live_a_day()

        try:
            spawn = f.spawn_offspring()
            new_fish.append(spawn)
        except ValueError:
            pass

    return fish + new_fish


def count_fish_after_days(input_data: List[str], days: int) -> int:
    fish = [fish for fish in get_starting_fish(input_data)]

    for day in range(days):
        fish = iterate_day(fish)

    return len(fish)


def count_fish_faster(input_data: List[str], stop_after: int) -> int:
    number_of_days = 9
    cyclic_days = [0] * number_of_days

    for f in get_starting_fish(input_data):
        cyclic_days[f.internal_timer] += 1

    for day in range(stop_after):
        target_day = day % len(cyclic_days)  # This will make it loop back to the start of the days list
        fish = cyclic_days[target_day]

        next_spawn_day_existing_fish = (target_day + 7) % number_of_days
        cyclic_days[next_spawn_day_existing_fish] += fish

        next_spawn_day_baby_fish = (target_day + 9) % number_of_days
        cyclic_days[next_spawn_day_baby_fish] += fish

        cyclic_days[target_day] -= fish

    return sum(cyclic_days)


@solution_timer(2021, 6, 1)
def part_one(input_data: List[str]):
    # answer = count_fish_after_days(input_data, 80)
    answer = count_fish_faster(input_data, 80)

    if not answer:
        raise SolutionNotFoundException(2021, 6, 1)

    return answer


@solution_timer(2021, 6, 2)
def part_two(input_data: List[str]):
    # answer = count_fish_after_days(input_data, 256) <- don't run this :)
    answer = count_fish_faster(input_data, 256)

    if not answer:
        raise SolutionNotFoundException(2021, 6, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2021, 6)
    part_one(data)
    part_two(data)
