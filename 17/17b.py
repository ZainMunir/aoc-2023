import sys
from heapq import heappop, heappush

lines = []
for line in sys.stdin:
    line = line.rstrip()
    line = line.replace("\ufeff", "")
    if line == "":
        continue
    lines.append(list(map(int, list(line))))
    # print(lines[-1])

directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]  # right, left, up, down


def left_right(dir):
    if dir == 0:
        return (2, 3)
    elif dir == 1:
        return (3, 2)
    elif dir == 2:
        return (1, 0)
    elif dir == 3:
        return (0, 1)


def print_route(route):
    for row in range(len(lines)):
        for col in range(len(lines[0])):
            if (row, col) in route:
                print("-", end="")
            else:
                print(lines[row][col], end="")
        print()


def make_route(lines):
    routes = {}

    stack = [(0, 1, 0, 1, 0, []), (1, 0, 3, 1, 0, [])]

    while len(stack) > 0:
        row, col, dir, consecutive_straight, total_loss, route = heappop(stack)
        # print(row, col, dir, consecutive_straight, total_loss)
        if row < 0 or col < 0 or row >= len(lines) or col >= len(lines[0]):
            continue
        key = (row, col, dir, consecutive_straight)
        total_loss += lines[row][col]
        if key in routes:
            if routes[key] > total_loss:
                routes[key] = total_loss
            else:
                continue
        route = route + [(row, col)]
        routes[key] = total_loss

        if consecutive_straight > 3:
            dir1, dir2 = left_right(dir)
            row1, col1 = row + directions[dir1][0], col + directions[dir1][1]
            row2, col2 = row + directions[dir2][0], col + directions[dir2][1]
            heappush(stack, (row1, col1, dir1, 1, total_loss, route))
            heappush(stack, (row2, col2, dir2, 1, total_loss, route))
        if consecutive_straight < 10:
            row3, col3 = row + directions[dir][0], col + directions[dir][1]
            heappush(
                stack,
                (
                    row3,
                    col3,
                    dir,
                    consecutive_straight + 1,
                    total_loss,
                    route,
                ),
            )

    possible_routes = []
    for key, val in routes.items():
        if key[0] == len(lines) - 1 and key[1] == len(lines[0]) - 1 and key[3] > 3:
            possible_routes.append(val)
    print(possible_routes)
    return min(possible_routes)


print(make_route(lines))
