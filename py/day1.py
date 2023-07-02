"""
https://adventofcode.com/2022/day/1
Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?  # noqa E501
"""

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
    with open('day1_input.txt', 'r') as file:
        raw_inventory = file.read()

    result = who_has_most_calories(raw_inventory)
    print(result.total_calories)
    pass
