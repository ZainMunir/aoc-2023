import sys

lines = []
for line in sys.stdin:
    line = line.rstrip()
    line = line.replace("\ufeff", "")
    if line == "":
        break
    line = line.replace(">", ".")
    line = line.replace("v", ".")
    line = line.replace("<", ".")
    lines.append(line)


def adjacent(point):
    row, col = point
    return [(row, col + 1), (row, col - 1), (row - 1, col), (row + 1, col)]


nodes = []
edges = {}
for i, row in enumerate(lines):
    for j, col in enumerate(row):
        if col == ".":
            nodes.append((i, j))

for node in nodes:
    edges[node] = []
    for point in adjacent(node):
        if point in nodes:
            edges[node].append((point, 1))


# print(len(nodes), len(edges))

to_pop = []
for key, val in edges.items():
    if len(val) == 2:
        to_pop.append(key)
        node1, node2 = val
        node1, weight1 = node1
        node2, weight2 = node2
        edges[node1].remove((key, weight1))
        edges[node2].remove((key, weight2))
        edges[node1].append((node2, weight1 + weight2))
        edges[node2].append((node1, weight1 + weight2))

for key in to_pop:
    edges.pop(key)
    nodes.remove(key)

# print(len(nodes), len(edges))
# for key, val in edges.items():
#     print(key, val)

starting_point = (-1, -1)  # row, col
ending_point = (-1, -1)
for i, col in enumerate(lines[0]):
    if col == ".":
        starting_point = (0, i)
for i, col in enumerate(lines[-1]):
    if col == ".":
        ending_point = (len(lines) - 1, i)

print(starting_point, ending_point)


def search(start, end):
    visited = set()

    def dfs(point, end, curr_path):
        if point == end:
            return curr_path
        longest_path = 0
        visited.add(point)

        for next_point, weight in edges[point]:
            if next_point not in visited:
                path = dfs(next_point, end, curr_path + weight)
                if longest_path < path:
                    longest_path = path

        visited.discard(point)
        return longest_path

    return dfs(start, end, 0)


longest = search(starting_point, ending_point)
print(longest)
