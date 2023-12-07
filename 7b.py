import re
import sys
from enum import Enum
from collections import Counter
from functools import cmp_to_key, total_ordering
import operator
from copy import copy


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


num_to_val = dict(
    {
        "A": Val.A,
        "K": Val.K,
        "Q": Val.Q,
        "J": Val.J,
        "T": Val.T,
        "9": Val.NINE,
        "8": Val.EIGHT,
        "7": Val.SEVEN,
        "6": Val.SIX,
        "5": Val.FIVE,
        "4": Val.FOUR,
        "3": Val.THREE,
        "2": Val.TWO,
    }
)


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
        valEnums.append(num_to_val.get(char))
    cards.append(Card(vals[0], valEnums, bid))


def get_better(counter):
    if len(counter) == 1:
        return counter.items()
    elif Val.J in counter:
        j_num = counter.pop(Val.J)
        max_val = max(counter.items(), key=operator.itemgetter(1))[0]
        counter[max_val] = counter.get(max_val) + j_num
        return sorted(counter.items(), key=lambda x: x[1], reverse=True)
    else:
        return sorted(counter.items(), key=lambda x: x[1], reverse=True)


def compare(a, b):
    best_a = get_better(copy(a.counter))
    best_b = get_better(copy(b.counter))

    if max([x[1] for x in best_a]) > max([x[1] for x in best_b]):
        return 1
    elif max([x[1] for x in best_a]) < max([x[1] for x in best_b]):
        return -1

    if len(best_a) != 1:
        if best_a[1][1] > best_b[1][1]:
            return 1
        elif best_a[1][1] < best_b[1][1]:
            return -1

    for i, valA in enumerate(a.vals):
        if valA > b.vals[i]:
            return 1
        elif valA < b.vals[i]:
            return -1
    return 0


sorted_cards = sorted(cards, key=cmp_to_key(compare))
total = 0
for i, card in enumerate(sorted_cards):
    # print(card.chars)
    # print(card.counter)
    # print()
    total += (i + 1) * int(card.bid)

print(total)
