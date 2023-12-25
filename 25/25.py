import sys
import networkx as nx
import matplotlib.pyplot as plt

graph = {}

for line in sys.stdin:
    line = line.rstrip()
    line = line.replace("\ufeff", "")
    if line == "":
        break
    left, right = line.split(":")
    right = right.split(" ")
    for edge in right:
        if edge == "":
            continue
        if left not in graph:
            graph[left] = set()
        graph[left].add(edge)
        if edge not in graph:
            graph[edge] = set()
        graph[edge].add(left)
# print(graph)


# def find_bridges(graph):
#     timer = 0
#     visited = set()
#     tin = [False] * len(graph)
#     low = [False] * len(graph)

#     def dfs(v, key, p=-1):
#         nonlocal timer
#         visited.add(key)
#         low[v] = timer
#         tin[v] = timer
#         timer += 1
#         for i, to in enumerate(graph[key]):
#             if to == p:
#                 continue
#             if to in visited:
#                 low[v] = min(low[v], tin[i])
#             else:
#                 dfs(i, key, v)
#                 low[v] = min(low[v], low[i])
#                 if low[i] > tin[v]:
#                     print("bridge", key, to)

#     for i, (key, _) in enumerate(graph.items()):
#         if key not in visited:
#             dfs(i, key)


# find_bridges(graph)

G = nx.Graph(graph)
# nx.draw(G)
# plt.show()


G.remove_edge("zjm", "zcp")
G.remove_edge("nsk", "rsg")
G.remove_edge("rfg", "jks")

pieces = [len(c) for c in sorted(nx.connected_components(G), key=len, reverse=True)]
print(pieces[0] * pieces[1])
