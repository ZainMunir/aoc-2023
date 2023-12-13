import sys
import itertools


def print_map(lines):
    for line in lines:
        print(line)
    print()


def find_num_diffs(lhs, rhs):
    total = 0
    for i in range(len(lhs)):
        for j in range(len(lhs[0])):
            if lhs[i][j] != rhs[i][j]:
                total += 1
    # print(total)
    return total


def find_horizontal_reflection(lines):
    val = 0
    for i in range(len(lines)):
        lhs = lines[:i]
        rhs = lines[i : 2 * i]
        rhs.reverse()
        if len(lhs) == 0:
            continue
        if len(lhs) > len(rhs):
            if find_num_diffs(lhs[-len(rhs) :], rhs) == 1:
                val += len(lhs)
        elif len(lhs) < len(rhs):
            if find_num_diffs(lhs, rhs[: -len(lhs)]) == 1:
                val += len(lhs)
        elif find_num_diffs(lhs, rhs) == 1:
            val += len(lhs)
    if val != 0:
        print_map(lines)
        print(val)
    return val


def find_vertical_reflection(lines):
    print("VERTICAL")
    print_map(lines)
    lines = [list(line) for line in lines]
    lines = list(zip(*lines))
    lines = ["".join(line) for line in lines]
    return find_horizontal_reflection(lines)


maps = [[]]
for line in sys.stdin:
    line = line.rstrip()
    line = line.replace("\ufeff", "")
    if line == "":
        maps.append([])
        continue
    maps[-1].append(line)

total = 0
for current in maps:
    val = find_horizontal_reflection(current)
    if val > 0:
        total += val * 100
    else:
        total += find_vertical_reflection(current)
    print()
print(total)
