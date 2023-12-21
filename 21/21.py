import sys
from heapq import heappop, heappush

starting_pos = (-1, -1)

grid = []
for line in sys.stdin:
    line = line.rstrip()
    line = line.replace("\ufeff", "")
    if line == "":
        break
    if "S" in line:
        starting_pos = (len(grid), line.index("S"))
    grid.append(line)


def print_grid(queue):
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if (y, x) in queue:
                print("O", end="")
            else:
                print(char, end="")
        print()
    print()


dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

queue = [starting_pos]

steps = 64

# print_grid(queue)
for i in range(steps):
    new_queue = []
    while queue:
        y, x = heappop(queue)
        for dy, dx in dirs:
            new_y, new_x = y + dy, x + dx
            if new_y < 0 or new_y >= len(grid) or new_x < 0 or new_x >= len(grid[0]):
                continue
            if (new_y, new_x) in new_queue:
                continue
            if grid[new_y][new_x] == "#":
                continue
            heappush(new_queue, (new_y, new_x))
    # print_grid(new_queue)
    queue = new_queue
print(len(queue))
print_grid(queue)
