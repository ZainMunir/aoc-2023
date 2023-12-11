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


for convert in conversions:
    sdr = zip(convert.destination, convert.source, convert.range)
    sdr = sorted(sdr)
    convert.destination = [x[0] for x in sdr]
    convert.source = [x[1] for x in sdr]
    convert.range = [x[2] for x in sdr]


seed_ranges = []

for j, seed in enumerate(seeds):
    if j % 2 == 0:
        seed_ranges.append(range(seed, seed + seeds[j + 1]))


def in_range(num):
    for r in seed_ranges:
        if num in r:
            return True
    return False


conversions.reverse()

possible_seeds = []
for i in range(len(conversions[0].destination)):
    possible_seeds.append(
        range(
            conversions[0].destination[i],
            conversions[0].destination[i] + conversions[0].range[i],
        )
    )

print(possible_seeds)

for rng in possible_seeds:
    for seed in rng:
        curr_seed = seed
        for convert in conversions:
            for i in range(len(convert.destination)):
                r = range(
                    convert.destination[i], convert.destination[i] + convert.range[i]
                )
                if curr_seed in r:
                    curr_seed = convert.source[i] + r.index(curr_seed)
                    break

        if in_range(curr_seed):
            print(seed)
            exit()


# This is technically wrong as it doens't consider the case where the smallest seed is obtained in a situation without a conversion (I think since the example fails)
