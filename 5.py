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

# for convert in conversions:
#     for i in range(len(convert.source)):
#         print(convert.destination[i], convert.source[i], convert.range[i])
#     print()

locations = []
for seed in seeds:
    loc = seed
    for convert in conversions:
        for i in range(len(convert.source)):
            r = range(convert.source[i], convert.source[i] + convert.range[i], 1)
            if loc in r:
                loc = convert.destination[i] + r.index(loc)
                break
    locations.append(loc)

print(min(locations))

# Part 5b


class MarkedRanges:
    def __init__(self, range):
        self.range = range
        self.marked = False


locations = []
for j, seed in enumerate(seeds):
    if j % 2 == 0:
        curr_seeds = [MarkedRanges(range(seed, seed + seeds[j + 1]))]
    else:
        continue
    for convert in conversions:
        new_seeds = []
        for i in range(len(convert.source)):
            r = range(convert.source[i], convert.source[i] + convert.range[i])
            for curr_range in curr_seeds:
                intersection = range(
                    max(r[0], curr_range.range[0]), min(r[-1], curr_range.range[-1]) + 1
                )
                if len(intersection) > 0:
                    curr_range.marked = True
                    min_curr = curr_range.range[0]
                    max_curr = curr_range.range[-1]
                    min_r = r[0]
                    max_r = r[-1]
                    min_intersection = intersection[0]
                    max_intersection = intersection[-1]
                    if min_curr < min_intersection:
                        new_seeds.append(range(min_curr, min_intersection))
                    if max_intersection < max_curr:
                        new_seeds.append(range(max_intersection + 1, max_curr + 1))

                    new_seeds.append(
                        range(
                            convert.destination[i] + r.index(min_intersection),
                            convert.destination[i] + r.index(max_intersection) + 1,
                        )
                    )

        filtered_seeds = list(filter(lambda x: not x.marked, curr_seeds))
        curr_seeds = [MarkedRanges(x) for x in new_seeds] + filtered_seeds

    locations.append(min([x.range[0] for x in curr_seeds]))

print(min(locations))

# if min_r == 0 and max_r == 7716721:
#     print()
#     print(
#         min_curr,
#         max_curr,
#         min_r,
#         max_r,
#         min_intersection,
#         max_intersection,
#     )
#     print(curr_range.range, r, intersection)
#     print(one, two)
