import re
import sys


class Conversion:
    def __init__(self, destination, source, range):
        self.destination = destination
        self.source = source
        self.range = range


pattern = re.compile(r"\d+")
seeds = sys.stdin.readline().rstrip()
seeds = list(map(int, re.findall(pattern, seeds)))

i = -1
conversions = []
for line in sys.stdin:
    line = line.rstrip()
    matches = re.findall(pattern, line)
    if line == "":
        continue
    if not matches:
        i += 1
        conversions.append(Conversion([], [], []))
        continue
    [dest, src, r] = line.split()
    conversions[i].destination.append(int(dest))
    conversions[i].source.append(int(src))
    conversions[i].range.append(int(r))

# locations = []
# for seed in seeds:
#     loc = seed
#     for convert in conversions:
#         for i in range(len(convert.source)):
#             r = range(convert.source[i], convert.source[i] + convert.range[i], 1)
#             if loc in r:
#                 loc = convert.destination[i] + r.index(loc)
#                 break
#     locations.append(loc)

# print(min(locations))

# Part 5b


class MarkedSeeds:
    def __init__(self, seed):
        self.val = seed
        self.marked = False


new_seeds = []
for j, seed in enumerate(seeds):
    if j % 2 == 0:
        new_seeds += [val for val in range(seed, seed + seeds[j + 1])]

min = -1

for i, seed in enumerate(new_seeds):
    for convert in conversions:
        for i in range(len(convert.source)):
            r = range(convert.source[i], convert.source[i] + convert.range[i], 1)
            if seed in r:
                seed = convert.destination[i] + r.index(seed)
                break
    if min == -1 or seed < min:
        min = seed
print(min)
