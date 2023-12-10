import sys
import copy

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


pipes = {
    "S": (False, False, False, False),
    "|": (True, False, True, False),
    "-": (False, True, False, True),
    "L": (True, True, False, False),
    "J": (True, False, False, True),
    "7": (False, False, True, True),
    "F": (False, True, True, False),
    ".": (False, False, False, False),
}
opp_pipes = {
    (True, False, True, False): "|",
    (False, True, False, True): "-",
    (True, True, False, False): "L",
    (True, False, False, True): "J",
    (False, False, True, True): "7",
    (False, True, True, False): "F",
}

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
        if c == "S":
            start_pos = (len(tiles) - 1, i)
        (north, east, south, west) = pipes[c]
        tiles[-1].append(Pipe(north, east, south, west, c))
        if c == ".":
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
        curr_tile.char = opp_pipes[
            (curr_tile.north, curr_tile.east, curr_tile.south, curr_tile.west)
        ]
        print(curr_tile.char)
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
#             print("  .  ", end=" ")
#         else:
#             print(f"{tile.distance:05d}", end=" ")

#     print()

print(len(ground_tiles))
total = 0
for y, x in ground_tiles:
    curr_tile = tiles[y][x]
    winding_num = 0
    for i in range(0, y):
        if tiles[i][x].distance != -1:
            if tiles[i][x].north and tiles[i][x].south:
                continue
            winding_num += 1

    if winding_num % 2 == 1:
        tiles[y][x].contained = True
        # print(y, x)
        total += 1

print(total)
