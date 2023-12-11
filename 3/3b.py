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
                        and schematic[new_y][new_x] == "*"
                    ):
                        return True

    return False


def find_star(x, y):
    for i in range(-1, 2):
        for j in range(-1, 2):
            new_x = x + i
            new_y = y + j
            if 0 <= new_x < len(schematic) and 0 <= new_y < len(schematic[0]):
                if new_x != x or new_y != y:
                    # print(new_x, new_y, schematic[new_y][new_x])
                    if (
                        not schematic[new_y][new_x].isnumeric()
                        and schematic[new_y][new_x] == "*"
                    ):
                        return (new_x, new_y)


total = []
for i, row in enumerate(schematic):
    current = ""
    star = False
    star_pos = ()
    for j, char in enumerate(row):
        if char.isnumeric():
            current += char
        elif current.isnumeric():
            if star:
                total.append((int(current), star_pos))
                star = False
                star_pos = ()
            current = ""
            continue
        else:
            continue

        if not star and check_adjacent(j, i):
            star = True
            star_pos = find_star(j, i)
        if j == len(row) - 1:
            # print(current)
            if star:
                total.append((int(current), star_pos))
                star = False
                star_pos = ()
            current = ""
# print(total)

filtered = []
for i, item in enumerate(total):
    count = 1
    for j, item2 in enumerate(total):
        if i != j:
            if item[1] == item2[1]:
                count += 1
    if count == 2:
        filtered.append(item)
# print(filtered)

solution = 0
for i, item in enumerate(filtered):
    for j, item2 in enumerate(filtered):
        if i != j:
            if item[1] == item2[1]:
                solution += item[0] * item2[0]
print(solution / 2)
