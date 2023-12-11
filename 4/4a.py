import re
import sys

total = 0
for line in sys.stdin:
    line = line.rstrip()
    card = line.split(":")
    [winnings, gotten] = card[1].split("|")
    pattern = re.compile(r"\d+")
    winning_nums = re.findall(pattern, winnings)
    numbers = re.findall(pattern, gotten)

    points = 0
    for num in numbers:
        if num in winning_nums and points == 0:
            points = 1
        elif num in winning_nums:
            points *= 2
    total += points
print(total)
