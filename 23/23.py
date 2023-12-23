import sys

lines = []
for line in sys.stdin:
    line = line.rstrip()
    line = line.replace("\ufeff", "")
    if line == "":
        break
    lines.append(line)

starting_point = (-1, -1)  # row, col
ending_point = (-1, -1)
for i, col in enumerate(lines[0]):
    if col == ".":
        starting_point = (0, i)
for i, col in enumerate(lines[-1]):
    if col == ".":
        ending_point = (len(lines) - 1, i)

print(starting_point, ending_point)
dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]  # right, left, up, down


def add_dir(row, col, dir):
    return row + dirs[dir][0], col + dirs[dir][1]


def find_longest(starting, ending):
    traversed = {}

    def move(row, col, length, path, dir):
        new = add_dir(row, col, dir)
        if (
            new[0] < 0
            or new[0] >= len(lines)
            or new[1] < 0
            or new[1] >= len(lines[new[0]])
        ):
            return -1

        path = path + [(new[0], new[1])]
        if lines[new[0]][new[1]] == "#":
            return -1
        if lines[new[0]][new[1]] == ">":
            return f(new[0], new[1], length, path, dir)
        if lines[new[0]][new[1]] == "<":
            return f(new[0], new[1], length, path, dir)
        # if lines[new[0]][new[1]] == "^":
        #     return f(new[0], new[1], length, dir)
        if lines[new[0]][new[1]] == "v":
            return f(new[0], new[1], length, path, dir)
        if lines[new[0]][new[1]] == ".":
            return f(new[0], new[1], length, path)

    def f(row, col, length, path, dir=-1):
        if row < 0 or row >= len(lines) or col < 0 or col >= len(lines[row]):
            return 0

        if (row, col) in traversed:
            return traversed[(row, col)]
        if (row, col) == ending:
            return length
        traversed[(row, col)] = -1
        if dir != -1:
            new_row, new_col = add_dir(row, col, dir)
            if (
                new_row < 0
                or new_row >= len(lines)
                or new_col < 0
                or new_col >= len(lines[new_row])
            ):
                return -1
            elif lines[new_row][new_col] == ".":
                return f(new_row, new_col, length + 1, path + [(new_row, new_col)])
            return -1

        for dir in range(4):
            traversed[(row, col)] = max(
                move(row, col, length, path, dir), traversed[(row, col)]
            )
        print(length)
        return traversed[(row, col)]

    path = []
    val = f(starting[0], starting[1], 0, path)
    # print(traversed)
    return val


print(find_longest(starting_point, ending_point))
