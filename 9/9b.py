import sys
from itertools import groupby


def all_equal(iterable):
    g = groupby(iterable)
    return next(g, True) and not next(g, False)


total = 0
for line in sys.stdin:
    line = line.rstrip()
    line = line.replace("\ufeff", "")

    nums = [list(map(int, line.split(" ")))]

    while not all_equal(nums[-1]):
        nums.append([y - x for x, y in zip(nums[-1][:-1], nums[-1][1:])])

    nums.reverse()
    for i, num in enumerate(nums):
        if i == len(nums) - 1:
            total += num[0]
        else:
            nums[i + 1].insert(0, (nums[i + 1][0] - num[0]))

print(total)
