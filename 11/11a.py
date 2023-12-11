import sys


class Pos:
    def __init__(self, galaxy, id):
        self.galaxy = galaxy
        self.id = id
        
def print_space():
    for i in range(len(space)):
        for j in range(len(space[i])):
            if space[i][j].galaxy:
                print("#", end="")
            else:
                print(".", end="")
        print()
    print()
            
total_galaxies = -1
space = []
for line in sys.stdin:
    line = line.rstrip()
    line = line.replace("\ufeff", "")
    if line == "":
        continue
    space.append([])
    for i, c in enumerate(line):
        if c == "#":
            total_galaxies += 1
            space[-1].append(Pos(True, total_galaxies))
        elif c == ".":
            space[-1].append(Pos(False, -1))

print_space()


empty_rows = []
for i in range(len(space)):
    if all(not space[i][j].galaxy for j in range(len(space[i]))):
        empty_rows.append(i)

empty_cols = []
for j in range(len(space[0])):
    if all(not space[i][j].galaxy for i in range(len(space))):
        empty_cols.append(j)

for j, col in enumerate(empty_cols):
    # print(empty_cols)
    for i in range(len(space)):
        # print(len(row), end=" ")
        space[i].insert(col, space[i][col])
        # print(len(row))
    empty_cols[j+1:] = [c + 1 for c in empty_cols[j+1:]]
print_space()
   
for i, row in enumerate(empty_rows):
    # print(empty_rows)
    space.insert(row, space[row])
    empty_rows[i+1:] = [r + 1 for r in empty_rows[i+1:]]
print_space()

galaxy_locations = []
for i in range(len(space)):
    for j in range(len(space[i])):
        if space[i][j].galaxy:
            galaxy_locations.append((j, i))

pairs = []
for i in range(len(galaxy_locations)):
    for j in range(i + 1, len(galaxy_locations)):
        pairs.append((galaxy_locations[i], galaxy_locations[j]))

total_distance = 0
for pair in pairs:
    (x1, y1) = pair[0]
    (x2, y2) = pair[1]
    total_distance += abs(x1 - x2) + abs(y1 - y2)
    # print(pair, abs(x1 - x2) + abs(y1 - y2))
print(total_distance)