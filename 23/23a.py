import sys

lines = []
for line in sys.stdin:
    line = line.rstrip()
    line = line.replace("\ufeff", "")
    if line == "":
        break
    lines.append(line)
sys.setrecursionlimit(1000000)


starting_point = (-1, -1)  # row, col
ending_point = (-1, -1)
for i, col in enumerate(lines[0]):
    if col == ".":
        starting_point = (0, i)
for i, col in enumerate(lines[-1]):
    if col == ".":
        ending_point = (len(lines) - 1, i)

print(starting_point, ending_point)


def search(start, end):
    visited = set()

    def is_valid(point, dir):
        if point[0] < 0 or point[0] >= len(lines):
            return False
        char = lines[point[0]][point[1]]
        match char:
            case ">":
                if dir == 0:
                    return True
                return False
            case "<":
                if dir == 1:
                    return True
                return False
            case "^":
                if dir == 2:
                    return True
                return False
            case "v":
                if dir == 3:
                    return True
                return False
            case ".":
                return True

    def dfs(point, end, curr_path):
        if point == end:
            return curr_path + [point]
        longest_path = []
        visited.add(point)

        right = (point[0], point[1] + 1)
        left = (point[0], point[1] - 1)
        up = (point[0] - 1, point[1])
        down = (point[0] + 1, point[1])

        if is_valid(right, 0) and right not in visited:
            path = dfs(right, end, curr_path + [point])
            if len(longest_path) < len(path):
                longest_path = path
        if is_valid(left, 1) and left not in visited:
            path = dfs(left, end, curr_path + [point])
            if len(longest_path) < len(path):
                longest_path = path
        if is_valid(up, 2) and up not in visited:
            path = dfs(up, end, curr_path + [point])
            if len(longest_path) < len(path):
                longest_path = path
        if is_valid(down, 3) and down not in visited:
            path = dfs(down, end, curr_path + [point])
            if len(longest_path) < len(path):
                longest_path = path
        visited.discard(point)
        return longest_path

    return dfs(start, end, [])


longest = search(starting_point, ending_point)
# print(longest)
print(len(longest) - 1)

for i, row in enumerate(lines):
    for j, col in enumerate(row):
        if (i, j) == starting_point:
            print("S", end="")
        elif (i, j) in longest:
            print("O", end="")
        else:
            print(col, end="")
    print()
