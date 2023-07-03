#include <stdio.h>
#include <string.h>
#include <stdlib.h>

struct ElfInventory {
    int elf_number;
    long total_calories;
};

int main(int argc, char const *argv[])
{
    FILE* in_file = fopen("../day1_input.txt", "r");

    long running_total = 0;
    int elf_num = 0;
    char line[100];
    struct ElfInventory elf_inventory[300];

    while (fgets(line, 100, in_file) != NULL)
    {
        if (strcmp(line, "\n") == 0) {
            struct ElfInventory inventory;
            inventory.elf_number = elf_num;
            inventory.total_calories = running_total;
            elf_inventory[elf_num] = inventory;
            elf_num++;
            running_total = 0;
        }
        else {
            running_total = running_total + strtol(line, NULL, 10);
        }
    }

    long max_calories = 0;
    for (int idx=0; idx < elf_num; idx++){
        if (elf_inventory[idx].total_calories > max_calories) {
            max_calories = elf_inventory[idx].total_calories;
        }
    }
    printf("max calories is %ld\n", max_calories);

    return 0;
}
