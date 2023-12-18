import sys
from heapq import heappush, heappop
import numpy as np
from matplotlib.patches import Polygon

instructions = []

for line in sys.stdin:
    line = line.rstrip()
    line = line.replace("\ufeff", "")
    if line == "":
        continue
    dir, length, code = line.split(" ")
    code = code[1:-1]
    instructions.append((dir, int(length), code))
# print(instructions)

coords = [(0, 0)]  # (row, col)

for dir, length, code in instructions:
    if dir == "R":
        for i in range(length):
            coords.append((coords[-1][0], coords[-1][1] + 1))
    elif dir == "L":
        for i in range(length):
            coords.append((coords[-1][0], coords[-1][1] - 1))
    elif dir == "U":
        for i in range(length):
            coords.append((coords[-1][0] - 1, coords[-1][1]))
    elif dir == "D":
        for i in range(length):
            coords.append((coords[-1][0] + 1, coords[-1][1]))

min_row = min(coords, key=lambda x: x[0])[0]
max_row = max(coords, key=lambda x: x[0])[0]
min_col = min(coords, key=lambda x: x[1])[1]
max_col = max(coords, key=lambda x: x[1])[1]
# print(min_row, max_row, min_col, max_col)
# for i in range(min_row, max_row + 1):
#     for j in range(min_col, max_col + 1):
#         if (i, j) in coords:
#             print("#", end="")
#         else:
#             print(".", end="")
#     print()

new_coords = [(i - min_row, j - min_col) for i, j in coords]

min_row = min(new_coords, key=lambda x: x[0])[0]
max_row = max(new_coords, key=lambda x: x[0])[0]
min_col = min(new_coords, key=lambda x: x[1])[1]
max_col = max(new_coords, key=lambda x: x[1])[1]
# print(min_row, max_row, min_col, max_col)
# for i in range(min_row, max_row + 1):
#     for j in range(min_col, max_col + 1):
#         if (i, j) in new_coords:
#             print("#", end="")
#         else:
#             print(".", end="")
#     print()

# https://stackoverflow.com/questions/36399381/whats-the-fastest-way-of-checking-if-a-point-is-inside-a-polygon-in-python


def inside(x, y, poly):
    n = len(poly)
    p1x, p1y = poly[0]
    inside = False
    for i in range(n + 1):
        p2x, p2y = poly[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xints = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xints:
                        inside = not inside
        p1x, p1y = p2x, p2y
    return inside


def find_inside():
    for i in range(min_row, max_row + 1):
        for j in range(min_col, max_col + 1):
            if inside(i, j, new_coords):
                return (i, j)


extra_coords = []
queue = [find_inside()]

polygon = Polygon(new_coords)
while len(queue) > 0:
    row, col = heappop(queue)
    if (row, col) in new_coords:
        continue
    if row < min_row or row > max_row or col < min_col or col > max_col:
        continue
    if (row, col) in extra_coords:
        continue
    if inside(row, col, new_coords):
        heappush(extra_coords, (row, col))
        heappush(queue, (row + 1, col))
        heappush(queue, (row - 1, col))
        heappush(queue, (row, col + 1))
        heappush(queue, (row, col - 1))

set_1 = set(extra_coords)
set_2 = set(new_coords)
print(len(set_1), len(set_2), len(set_1) + len(set_2))

for i in range(min_row, max_row + 1):
    for j in range(min_col, max_col + 1):
        if (i, j) in new_coords:
            print("#", end="")
        elif (i, j) in extra_coords:
            print("O", end="")
        else:
            print(".", end="")
    print()
