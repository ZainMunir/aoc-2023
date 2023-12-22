import sys
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from itertools import cycle
from matplotlib.lines import Line2D


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


removable = 0
for key, brick in bricks.items():
    # print(brick.id, brick.left, brick.right, brick.supporting, brick.on_top_of)
    if len(brick.supporting) == 0:
        removable += 1
        # print(brick.id, brick.left, brick.right)
        continue
    can_remove = True
    for supporting in brick.supporting:
        if len(bricks[supporting].on_top_of) <= 1:
            can_remove = False
            break
    if can_remove:
        removable += 1
        # print(brick.id, brick.left, brick.right)
print(removable)


# Visualizing - very bad for actual input
exit()

unique_groups = set(point[3] for point in placed_brick_points)

color_cycle = cycle(plt.cm.tab10.colors)  # You can use any colormap here
colors = {group: next(color_cycle) for group in unique_groups}

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

legend_elements = []

for group in unique_groups:
    bar = ax.bar3d(0, 0, 0, dx=0, dy=0, dz=0, color=colors[group])
    legend_elements.append(
        Line2D(
            [0], [0], marker="s", color="w", label=group, markerfacecolor=colors[group]
        )
    )

for x, y, z, group in placed_brick_points:
    ax.bar3d(x, y, z, dx=1, dy=1, dz=1, color=colors[group])

ax.legend(handles=legend_elements, loc="upper right")

ax.set_xlabel("X Label")
ax.set_ylabel("Y Label")
ax.set_zlabel("Z Label")
ax.set_title("3D Bar Plot with Cubes and Legend")

plt.show()
