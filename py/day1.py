"""
https://adventofcode.com/2022/day/1
Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?  # noqa E501
"""

import os
from dataclasses import dataclass
from typing import List

test_elf_raw_inventory = """1000 
2000 
3000 

4000 

5000 
6000 

7000 
8000 
9000 

10000"""  # noqa: W291


def test_challenge_test_data():
    result = who_has_most_calories(test_elf_raw_inventory)
    assert result.elf_num == 4
    assert result.total_calories == 24000

    assert who_has_most_calories_v2(test_elf_raw_inventory) == 24000
    assert who_has_most_calories_v3(test_elf_raw_inventory) == 24000
    assert who_has_most_calories_v4(test_elf_raw_inventory) == 24000


def who_has_most_calories_v4(elf_raw_inventory: str) -> int:
    inventories = []
    for group in filter(None, elf_raw_inventory.split('\n\n')):
        inventories.append(sum(map(int, group.split('\n'))))
    return max(inventories)


def who_has_most_calories_v3(elf_raw_inventory: str) -> int:
    # is this even readable?
    return max(
        [
            sum(map(int, group.split('\n')))
            for group in filter(None, elf_raw_inventory.split('\n\n'))
        ])  # noqa: E501


def who_has_most_calories_v2(elf_raw_inventory: str) -> int:

    lines = elf_raw_inventory.split('\n')

    max_calories = 0
    running_total = 0
    for line in lines:
        if not line:
            if running_total > max_calories:
                max_calories = running_total
            running_total = 0
        else:
            running_total += int(line)

    return max_calories


@dataclass
class ElfInventory:
    elf_num: int
    total_calories: int


def who_has_most_calories(elf_raw_inventory: str) -> ElfInventory:

    elf_results = load_elf_inventory(elf_raw_inventory)
    elf_most = elf_results[0]
    for elf in elf_results:
        if elf.total_calories > elf_most.total_calories:
            elf_most = elf

    return elf_most


def top_3_elves_total_calories(elf_raw_inventory: str) -> ElfInventory:
    elf_results = load_elf_inventory(elf_raw_inventory)
    elf_results = sorted(map(lambda er: er.total_calories, elf_results), reverse=True)  # noqa E501
    return sum(elf_results[:3])


def load_elf_inventory(elf_raw_inventory: str) -> List[ElfInventory]:
    lines = elf_raw_inventory.split('\n')

    elves = []
    running_total = 0
    for line in lines:
        if line == "":
            elves.append(ElfInventory(len(elves) + 1, running_total))
            running_total = 0
        else:
            running_total += int(line)
    if running_total != 0:
        elves.append(ElfInventory(len(elves) + 1, running_total))
    return elves


if __name__ == '__main__':
    path_to_file = os.path.join(os.path.dirname(__file__), '../day1_input.txt')
    with open(path_to_file, 'r') as file:
        raw_inventory = file.read()

    max_calories = who_has_most_calories(raw_inventory)
    print(max_calories)

    print(top_3_elves_total_calories(raw_inventory))
