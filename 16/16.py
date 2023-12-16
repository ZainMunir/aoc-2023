import sys
import copy


def print_tiles(tiles):
    for tile in tiles:
        for t in tile:
            if t.energized:
                print(t.dirs.count(True), end="")
            else:
                print(t.type, end="")
        print()


class Tile:
    def __init__(self, type):
        self.type = type
        self.dirs = [False, False, False, False]  # UP, DOWN, LEFT, RIGHT
        self.energized = False


tiles = []
for line in sys.stdin:
    line = line.rstrip()
    line = line.replace("\ufeff", "")
    if line == "":
        continue
    tiles.append([])
    for c in line:
        tiles[-1].append(Tile(c))


def find_total(tiles, init):
    stack = [init]
    while len(stack) > 0:
        dir, x, y = stack.pop()
        if x < 0 or y < 0 or x >= len(tiles[0]) or y >= len(tiles):
            continue
        tile = tiles[y][x]
        if tile.dirs[dir]:
            continue
        tile.dirs[dir] = True
        tile.energized = True

        if (
            tile.type == "."
            or ((dir == 2 or dir == 3) and tile.type == "-")
            or ((dir == 0 or dir == 1) and tile.type == "|")
        ):
            if dir == 0:
                y -= 1
            elif dir == 1:
                y += 1
            elif dir == 2:
                x -= 1
            elif dir == 3:
                x += 1
            stack.append((dir, x, y))
        elif tile.type == "\\" and dir == 3 or tile.type == "/" and dir == 2:
            stack.append((1, x, y + 1))
        elif tile.type == "\\" and dir == 2 or tile.type == "/" and dir == 3:
            stack.append((0, x, y - 1))
        elif tile.type == "\\" and dir == 0 or tile.type == "/" and dir == 1:
            stack.append((2, x - 1, y))
        elif tile.type == "\\" and dir == 1 or tile.type == "/" and dir == 0:
            stack.append((3, x + 1, y))
        elif tile.type == "|":
            stack.append((0, x, y - 1))
            stack.append((1, x, y + 1))
        elif tile.type == "-":
            stack.append((2, x - 1, y))
            stack.append((3, x + 1, y))

    total = 0
    for tile in tiles:
        for t in tile:
            if t.energized:
                total += 1
    # print_tiles(tiles)
    return total


options = []
for i in range(len(tiles)):
    options.append((3, 0, i))
    options.append((2, len(tiles) - 1, i))
for j in range(len(tiles[0])):
    options.append((1, j, 0))
    options.append((0, j, len(tiles) - 1))

overall_total = []
for option in options:
    overall_total.append(find_total(copy.deepcopy(tiles), option))
    # print(option, overall_total[-1])
    # print()

# print(options)
# print(overall_total)
print(overall_total[0])
print(max(overall_total))
