import sys


class Brick:
    def __init__(self, id, left, right):
        self.id = id
        self.left = left
        self.right = right
        self.on_top_of = set()
        self.supporting = set()


max_x = 0
max_y = 0
max_z = 0
bricks = {}
for i, line in enumerate(sys.stdin):
    line = line.rstrip()
    line = line.replace("\ufeff", "")
    if line == "":
        break
    left, right = line.split("~")
    left = list(map(int, left.split(",")))
    right = list(map(int, right.split(",")))
    bricks[i] = Brick(i, left, right)
    max_x = max(max(left[0], right[0]), max_x)
    max_y = max(max(left[1], right[1]), max_y)
    max_z = max(max(left[2], right[2]), max_z)


placed_brick_cubes = []
placed_brick_points = []

for i in range(max_x + 1):
    placed_brick_cubes.append([])
    for j in range(max_y + 1):
        placed_brick_cubes[i].append([])
        for k in range(max_z + 1):
            placed_brick_cubes[i][j].append(-2)


def place_brick(brick):
    lx, ly, lz = brick.left
    rx, ry, rz = brick.right

    placed = set()
    if lz == 1 or rz == 1:
        placed.add(-1)

    while len(placed) == 0:
        for x in range(lx, rx + 1):
            for y in range(ly, ry + 1):
                for z in range(lz, rz + 1):
                    if placed_brick_cubes[x][y][z] != -2:
                        # print(brick.id, "collides with", placed_brick_cubes[x][y][z])
                        placed.add(placed_brick_cubes[x][y][z])
                        placed.discard(-1)
                    elif (lz == 0 or rz == 0) and len(placed) == 0:
                        # print(brick.id, "collides with floor")
                        placed.add(-1)
        if len(placed) == 0:
            lz -= 1
            rz -= 1
        else:
            lz += 1
            rz += 1
    for x in range(lx, rx + 1):
        for y in range(ly, ry + 1):
            for z in range(lz, rz + 1):
                placed_brick_cubes[x][y][z] = brick.id
                placed_brick_points.append((x, y, z, brick.id))
    brick.left = (lx, ly, lz)
    brick.right = (rx, ry, rz)
    if -1 not in placed:
        for place in placed:
            # print(brick.id, "on top of", place)
            bricks[place].supporting.add(brick.id)
            brick.on_top_of.add(place)


bricks_sorted = sorted(bricks.items(), key=lambda x: min(x[1].left[2], x[1].right[2]))

for key, brick in bricks_sorted:
    lx, ly, lz = brick.left
    rx, ry, rz = brick.right

    place_brick(brick)


def find_effect(brick, cascade):
    cascade.add(brick.id)
    queue = set()
    queue.add(brick.id)

    while len(queue) > 0:
        id = queue.pop()
        for supporting in bricks[id].supporting:
            if bricks[supporting].on_top_of.issubset(cascade):
                queue.add(supporting)
                cascade.add(supporting)

    return len(cascade) - 1  # don't count the brick itself


total = 0
brick_effects = {}
for key, brick in bricks.items():
    add = find_effect(brick, set())
    total += add
print(total)
