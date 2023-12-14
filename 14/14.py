import sys


lines = []
for line in sys.stdin:
    line = line.rstrip()
    line = line.replace("\ufeff", "")
    if line == "":
        continue
    lines.append(list(line))


def move_rocks():
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == ".":
                for k in range(i + 1, len(lines)):
                    if lines[k][j] == "#":
                        break
                    if lines[k][j] == "O":
                        line[j] = "O"
                        lines[k][j] = "."
                        break


def print_map():
    for line in lines:
        print("".join(line))
    print()


# Part 1
move_rocks()
total = 0
for i, line in enumerate(lines):
    total += line.count("O") * (len(lines) - i)
print(total)

grids = {}
# print_map()
loops = 4 * 1000000000
for i in range(loops):
    move_rocks()
    lines = list(zip(*reversed(lines)))
    lines = [list(line) for line in lines]
    key = tuple(["".join(line) for line in lines])
    if key in grids:
        cycle = i - grids[key]
        i += cycle * ((loops - i) // cycle)
        # print(i, grids[key])
        break
    grids[key] = i

while i < loops - 1:
    move_rocks()
    lines = list(zip(*reversed(lines)))
    lines = [list(line) for line in lines]
    i += 1

total = 0
for i, line in enumerate(lines):
    total += line.count("O") * (len(lines) - i)
print(total)
