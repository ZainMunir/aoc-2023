import sys

# https://en.wikipedia.org/wiki/Jordan_curve_theorem


class Pipe:
    def __init__(self, north, east, south, west, char):
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.distance = -1
        self.contained = False
        self.char = char


start_pos = (-1, -1)

tiles = []

ground_tiles = []
for line in sys.stdin:
    line = line.rstrip()
    line = line.replace("\ufeff", "")
    if line == "":
        continue
    tiles.append([])
    for i, c in enumerate(line):
        match c:
            case "S":
                start_pos = (len(tiles) - 1, i)
                tiles[-1].append(Pipe(False, False, False, False, c))
            case "|":
                tiles[-1].append(Pipe(True, False, True, False, c))
            case "-":
                tiles[-1].append(Pipe(False, True, False, True, c))
            case "L":
                tiles[-1].append(Pipe(True, True, False, False, c))
            case "J":
                tiles[-1].append(Pipe(True, False, False, True, c))
            case "7":
                tiles[-1].append(Pipe(False, False, True, True, c))
            case "F":
                tiles[-1].append(Pipe(False, True, True, False, c))
            case ".":
                tiles[-1].append(Pipe(False, False, False, False, c))
                ground_tiles.append((len(tiles) - 1, i))

rows = len(tiles)
cols = len(tiles[0])

queue = [start_pos]
starting = True

max_distance = 0
while len(queue) > 0:
    (y, x) = queue.pop(0)
    curr_tile = tiles[y][x]
    new_distance = curr_tile.distance + 1

    if starting:
        starting = False
        curr_tile.distance = 0
        new_distance = 1
        if y - 1 >= 0:
            if tiles[y - 1][x].south and tiles[y - 1][x].distance == -1:
                queue.append((y - 1, x))
                tiles[y - 1][x].distance = new_distance
                tiles[y][x].north = True
        if x + 1 < cols:
            if tiles[y][x + 1].west and tiles[y][x + 1].distance == -1:
                queue.append((y, x + 1))
                tiles[y][x + 1].distance = new_distance
                tiles[y][x].east = True
        if y + 1 < rows:
            if tiles[y + 1][x].north and tiles[y + 1][x].distance == -1:
                queue.append((y + 1, x))
                tiles[y + 1][x].distance = new_distance
                tiles[y][x].south = True
        if x - 1 >= 0:
            if tiles[y][x - 1].east and tiles[y][x - 1].distance == -1:
                queue.append((y, x - 1))
                tiles[y][x - 1].distance = new_distance
                tiles[y][x].west = True
    else:
        if y - 1 >= 0:
            if (
                tiles[y - 1][x].south
                and curr_tile.north
                and tiles[y - 1][x].distance == -1
            ):
                queue.append((y - 1, x))
                tiles[y - 1][x].distance = new_distance
        if x + 1 < cols:
            if (
                tiles[y][x + 1].west
                and curr_tile.east
                and tiles[y][x + 1].distance == -1
            ):
                queue.append((y, x + 1))
                tiles[y][x + 1].distance = new_distance
        if y + 1 < rows:
            if (
                tiles[y + 1][x].north
                and curr_tile.south
                and tiles[y + 1][x].distance == -1
            ):
                queue.append((y + 1, x))
                tiles[y + 1][x].distance = new_distance
        if x - 1 >= 0:
            if (
                tiles[y][x - 1].east
                and curr_tile.west
                and tiles[y][x - 1].distance == -1
            ):
                queue.append((y, x - 1))
                tiles[y][x - 1].distance = new_distance

# for row in tiles:
#     for tile in row:
#         if tile.distance == -1:
#             print(".", end="  ")
#         else:
#             print(tile.distance, end=" ")
#     print()


def adjacent(y, x):
    adj = []
    if tiles[y][x].north:
        if y - 1 >= 0:
            adj.append((y - 1, x))
    if tiles[y][x].east:
        if x + 1 < cols:
            adj.append((y, x + 1))
    if tiles[y][x].south:
        if y + 1 < rows:
            adj.append((y + 1, x))
    if tiles[y][x].west:
        if x - 1 >= 0:
            adj.append((y, x - 1))
    if len(adj) == 0:
        if y - 1 >= 0:
            adj.append((y - 1, x))
        if x + 1 < cols:
            adj.append((y, x + 1))
        if y + 1 < rows:
            adj.append((y + 1, x))
        if x - 1 >= 0:
            adj.append((y, x - 1))
    return adj


print(len(ground_tiles))
total = 0
for y, x in ground_tiles:
    curr_tile = tiles[y][x]
    winding_num = 0
    right_angles = 0
    for i in range(0, y):
        if tiles[i][x].distance != -1:
            if tiles[i][x].north and tiles[i][x].south:
                continue
            winding_num += 1
    if winding_num % 2 == 1:
        tiles[y][x].contained = True
        print(y, x)
        total += 1
        continue


print(total)
