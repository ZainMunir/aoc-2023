import re
import sys
from enum import Enum
from collections import Counter
from functools import cmp_to_key, total_ordering
import operator

Val = Enum("Val", ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"])


@total_ordering
class Val(Enum):
    A = 14
    K = 13
    Q = 12
    T = 10
    NINE = 9
    EIGHT = 8
    SEVEN = 7
    SIX = 6
    FIVE = 5
    FOUR = 4
    THREE = 3
    TWO = 2
    J = 1

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented


class Card:
    def __init__(self, chars, vals, bid):
        self.chars = chars
        self.vals = vals
        self.bid = bid
        self.counter = Counter(vals)


cards = []

for line in sys.stdin:
    line = line.rstrip()
    line = line.replace("\ufeff", "")
    if line == "":
        continue
    vals = line.split()
    bid = vals.pop()
    valEnums = []
    for char in vals[0]:
        if char == "A":
            valEnums.append(Val.A)
        elif char == "K":
            valEnums.append(Val.K)
        elif char == "Q":
            valEnums.append(Val.Q)
        elif char == "J":
            valEnums.append(Val.J)
        elif char == "T":
            valEnums.append(Val.T)
        elif char == "9":
            valEnums.append(Val.NINE)
        elif char == "8":
            valEnums.append(Val.EIGHT)
        elif char == "7":
            valEnums.append(Val.SEVEN)
        elif char == "6":
            valEnums.append(Val.SIX)
        elif char == "5":
            valEnums.append(Val.FIVE)
        elif char == "4":
            valEnums.append(Val.FOUR)
        elif char == "3":
            valEnums.append(Val.THREE)
        elif char == "2":
            valEnums.append(Val.TWO)

    cards.append(Card(vals[0], valEnums, bid))

# for card in cards:
#     print(card.vals, card.bid, card.counter)


def compare(a, b):
    sorted_a = sorted(a.counter.items(), key=operator.itemgetter(1), reverse=True)
    sorted_b = sorted(b.counter.items(), key=operator.itemgetter(1), reverse=True)

    aJ = False
    bJ = False

    condA = sorted_a[0][1] + (a.counter.get(Val.J, 0) if sorted_a[0][0] != Val.J else 0)
    condB = sorted_b[0][1] + (b.counter.get(Val.J, 0) if sorted_b[0][0] != Val.J else 0)

    if condA > sorted_a[0][1]:
        aJ = True
    if condB > sorted_b[0][1]:
        bJ = True

    if condA > condB:
        return 1
    elif condA < condB:
        return -1

    if len(sorted_a) != 1 and len(sorted_b) != 1:
        condA = sorted_a[1][1] + (
            a.counter.get(Val.J, 0)
            if sorted_a[1][0] != Val.J and sorted_a[0][0] != Val.J and not aJ
            else 0
        )
        condB = sorted_b[1][1] + (
            b.counter.get(Val.J, 0)
            if sorted_b[1][0] != Val.J and sorted_b[0][0] != Val.J and not bJ
            else 0
        )

        if condA > condB:
            return 1
        elif condA < condB:
            return -1

    for i, valA in enumerate(a.vals):
        if valA > b.vals[i]:
            return 1
        elif valA < b.vals[i]:
            return -1
    return 0


sorted_cards = sorted(cards, key=cmp_to_key(compare))
# print()
total = 0
for i, card in enumerate(sorted_cards):
    print(card.chars)
    # print(card.counter)
    # print()
    total += (i + 1) * int(card.bid)

print(total)
