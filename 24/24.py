import sys
from operator import add
from itertools import combinations


class Stone:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity
        self.extra_point = list(map(add, position, velocity))


stones = []
for i, line in enumerate(sys.stdin):
    line = line.rstrip()
    line = line.replace("\ufeff", "")
    if line == "":
        break
    pos, vel = line.split("@")
    pos = pos.split(",")
    vel = vel.split(",")
    pos = list(map(int, pos))
    vel = list(map(int, vel))
    stones.append(Stone(pos, vel))


# https://stackoverflow.com/questions/20677795/how-do-i-compute-the-intersection-point-of-two-lines


def intersection(stone1, stone2):
    line1 = (
        (stone1.position[0], stone1.position[1]),
        (stone1.extra_point[0], stone1.extra_point[1]),
    )
    line2 = (
        (stone2.position[0], stone2.position[1]),
        (stone2.extra_point[0], stone2.extra_point[1]),
    )

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    div = det(xdiff, ydiff)
    if div == 0:
        return None

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div

    if (stone1.velocity[0] > 0 and (x < stone1.position[0])) or (
        stone1.velocity[1] > 0 and (y < stone1.position[1])
    ):
        return None
    if (stone1.velocity[0] < 0 and (x > stone1.position[0])) or (
        stone1.velocity[1] < 0 and (y > stone1.position[1])
    ):
        return None
    if (stone2.velocity[0] > 0 and (x < stone2.position[0])) or (
        stone2.velocity[1] > 0 and (y < stone2.position[1])
    ):
        return None
    if (stone2.velocity[0] < 0 and (x > stone2.position[0])) or (
        stone2.velocity[1] < 0 and (y > stone2.position[1])
    ):
        return None

    return x, y


# test_area_min = (7, 7)
# test_area_max = (27, 27)
test_area_min = (200000000000000, 200000000000000)
test_area_max = (400000000000000, 400000000000000)


total_intersections = 0
for i, stone1 in enumerate(stones):
    for j, stone2 in enumerate(stones[i:]):
        res = intersection(stone1, stone2)
        if res:
            x, y = res
            if (
                x >= test_area_min[0]
                and x <= test_area_max[0]
                and y >= test_area_min[1]
                and y <= test_area_max[1]
            ):
                # print(stone1.position, stone2.position, x, y)
                total_intersections += 1

print(total_intersections)
