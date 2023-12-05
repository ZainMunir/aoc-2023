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


def new_ranges(old_ranges, updated_ranges):
    new_ranges = []

    for curr in old_ranges:
        no_intersection = True
        for updated in updated_ranges:
            intersection = range(
                max(curr[0], updated[0]), min(curr[-1], updated[-1]) + 1
            )
            if len(intersection):
                no_intersection = False
                min_curr = min(curr)
                max_curr = max(curr)
                min_updated = min(updated)
                max_updated = max(updated)
                below_range = range(min_curr, min_updated)
                if len(below_range):
                    new_ranges.append(below_range)
                new_ranges.append(updated)
                above_range = range(max_updated + 1, max_curr)
                if len(above_range):
                    new_ranges.append(above_range)
        if no_intersection:
            new_ranges.append(curr)

    return new_ranges


locations = []
for j, seed in enumerate(seeds):
    if j % 2 == 0:
        curr_seeds = [range(seed, seed + seeds[j + 1])]
    else:
        continue
    for convert in conversions:
        new_seeds = []
        for i in range(len(convert.source)):
            r = range(convert.source[i], convert.source[i] + convert.range[i], 1)
            for curr_range in curr_seeds:
                intersection = range(
                    max(curr_range[0], r[0]), min(curr_range[-1], r[-1]) + 1
                )
                if len(intersection):
                    new_seeds.append(
                        range(
                            convert.destination[i] + r.index(min(intersection)),
                            convert.destination[i] + r.index(max(intersection)) + 1,
                        )
                    )
        curr_seeds = new_ranges(curr_seeds, new_seeds)
        new_seeds = []
    locations.append(curr_seeds)
