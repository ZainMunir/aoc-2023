import sys
import re
import copy
import math


class SpringLine:
    def __init__(self, springs, config):
        self.springs = springs
        self.config = config


pattern = re.compile(r"\d+")

all_springs = []
for line in sys.stdin:
    line = line.rstrip()
    line = line.replace("\ufeff", "")
    if line == "":
        continue
    springs, nums = line.split(" ")
    springs = list(springs)
    nums = list(map(int, pattern.findall(nums)))
    all_springs.append(SpringLine(springs, nums))


def check_line(spring_line):
    springs = spring_line.springs
    config = spring_line.config
    groups = "".join(springs).split(".")
    hash_counts = [group.count("#") for group in groups if group.count("#") > 0]
    return hash_counts == config


def make_configs(springLine, curr_spring):
    new = copy.deepcopy(springLine)
    springs_1 = new.springs
    springs_2 = copy.copy(new.springs)
    config = new.config
    if "?" not in springs_1:
        if "".join(springs_1) in handled_combos:
            return 0
        handled_combos.append("".join(springs_1))
        return_val = check_line(new)
        # if return_val:
        #     print(handled_combos[-1], config)
        return return_val

    for i in range(curr_spring, len(springs_1)):
        if springs_1[i] == "?":
            if "".join(springs_1) in handled_combos:
                return 0
            handled_combos.append("".join(springs_1))
            springs_1[i] = "#"
            springs_2[i] = "."
            return make_configs(SpringLine(springs_1, config), i + 1) + make_configs(
                SpringLine(springs_2, config), i + 1
            )


total = 0
for spring in all_springs:
    handled_combos = []
    handled_potential_combos = []
    # print(check_line(spring))
    print(math.pow(2, spring.springs.count("?")))
    val = make_configs(spring, 0)
    total += val
    print(val)

print(total)
# 52 + answer
