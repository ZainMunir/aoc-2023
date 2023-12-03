import re
import sys

schematic = []

for line in sys.stdin:
    line = line.replace("\ufeff", "")
    schematic.append(line.rstrip())

total = 0


def check_adjacent(x, y):
    # print("char ", x, y, schematic[y][x])
    for i in range(-1, 2):
        for j in range(-1, 2):
            new_x = x + i
            new_y = y + j
            if 0 <= new_x < len(schematic) and 0 <= new_y < len(schematic[0]):
                if new_x != x or new_y != y:
                    # print(new_x, new_y, schematic[new_y][new_x])
                    if (
                        not schematic[new_y][new_x].isnumeric()
                        and schematic[new_y][new_x] != "."
                    ):
                        return True

    return False


for i, row in enumerate(schematic):
    current = ""
    add = False
    for j, char in enumerate(row):
        if char.isnumeric():
            current += char
        elif current.isnumeric():
            if add:
                total += int(current)
                # print(current)
                add = False
            current = ""
            continue
        else:
            continue

        if not add and check_adjacent(j, i):
            add = True
        if j == len(row) - 1:
            print(current)
            if add:
                total += int(current)
                add = False
            current = ""
print(total)
