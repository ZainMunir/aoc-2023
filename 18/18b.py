import sys

instructions = []

perimeter = 0
for line in sys.stdin:
    line = line.rstrip()
    line = line.replace("\ufeff", "")
    if line == "":
        continue
    garbage_1, garbage_2, code = line.split(" ")
    code = code[1:-1]
    length = int(code[1:-1], 16)
    instructions.append((code[-1], length))
    perimeter += length
# print(instructions)

coords = [(0, 0)]  # (row, col)

for dir, length in instructions:
    if dir == "0":
        coords.append((coords[-1][0], coords[-1][1] + length))
    elif dir == "2":
        coords.append((coords[-1][0], coords[-1][1] - length))
    elif dir == "3":
        coords.append((coords[-1][0] - length, coords[-1][1]))
    elif dir == "1":
        coords.append((coords[-1][0] + length, coords[-1][1]))

min_row = min(coords, key=lambda x: x[0])[0]
max_row = max(coords, key=lambda x: x[0])[0]
min_col = min(coords, key=lambda x: x[1])[1]
max_col = max(coords, key=lambda x: x[1])[1]


def polygon_area(vertices):  # row == y, col == x
    num_vertices = len(vertices)
    sum_1 = 0
    sum_2 = 0
    for i in range(0, num_vertices):
        row_1, col_1 = vertices[i]
        row_2, col_2 = vertices[(i + 1) % num_vertices]
        sum_1 += col_1 * row_2
        sum_2 += row_1 * col_2
    return abs(sum_1 - sum_2 + perimeter) // 2 + 1


inside_area = polygon_area(coords)
print(inside_area)
