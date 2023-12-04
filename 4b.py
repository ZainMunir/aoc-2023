import re
import sys


class Card:
    def __init__(self, winning_numbers, actual_numbers, matches):
        self.winning_numbers = winning_numbers
        self.actual_numbers = actual_numbers
        self.matches = matches
        self.instances = 1


cards = []

for line in sys.stdin:
    line = line.rstrip()
    card = line.split(":")
    [winnings, gotten] = card[1].split("|")
    pattern = re.compile(r"\d+")
    winning_nums = re.findall(pattern, winnings)
    numbers = re.findall(pattern, gotten)
    card_num = re.findall(pattern, card[0])
    matches = 0
    for num in numbers:
        if num in winning_nums:
            matches += 1
    cards.append(Card(winning_nums, numbers, matches))

total = 0

for i, card in enumerate(cards):
    for k in range(card.instances):
        for j in range(card.matches):
            cards[i + j + 1].instances += 1

for card in cards:
    total += card.instances
print(total)
