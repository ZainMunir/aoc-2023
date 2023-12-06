import re
import sys
import numpy as np
pattern = re.compile(r"\d+")

times = sys.stdin.readline().rstrip()
times = list(map(int, re.findall(pattern, times)))

distances = sys.stdin.readline().rstrip()
distances = list(map(int, re.findall(pattern, distances)))

print(times, distances)

num_wins = []

for i, time in enumerate(times):
    num_wins.append(0)
    for j in range(time):
        if j * (time - j) > distances[i]:
            num_wins[i] += 1

print(np.prod(num_wins))


# Part B

time = int("".join(map(str,times)))
distance = int("".join(map(str, distances)))

print(time, distance)

num_wins = 0
for j in range(time):
    if j * (time - j) > distance:
        num_wins += 1
print(num_wins)