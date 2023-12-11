import sys


class Pipe:
    def __init__(self, north, east, south, west):
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.distance = -1


start_pos = (-1, -1)

tiles = []

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
                tiles[-1].append(Pipe(False, False, False, False))
            case "|":
                tiles[-1].append(Pipe(True, False, True, False))
            case "-":
                tiles[-1].append(Pipe(False, True, False, True))
            case "L":
                tiles[-1].append(Pipe(True, True, False, False))
            case "J":
                tiles[-1].append(Pipe(True, False, False, True))
            case "7":
                tiles[-1].append(Pipe(False, False, True, True))
            case "F":
                tiles[-1].append(Pipe(False, True, True, False))
            case ".":
                tiles[-1].append(Pipe(False, False, False, False))

rows = len(tiles)
cols = len(tiles[0])

queue = [start_pos]
starting = True

max_distance = 0
while len(queue) > 0:
    (y, x) = queue.pop(0)
    curr_tile = tiles[y][x]
    max_distance = curr_tile.distance
    new_distance = curr_tile.distance + 1
    # print(y, x)

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
#             print(".", end=" ")
#         else:
#             print(tile.distance, end=" ")
#     print()

print(max_distance)
