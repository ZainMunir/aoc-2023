import sys
import re
import copy
import math
import functools


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


def check_line(springs, config):
    groups = "".join(springs).split(".")
    hash_counts = [group.count("#") for group in groups if group.count("#") > 0]
    return hash_counts == config


def make_configs(springs, config, curr_spring, group_index=0, group_count=0):
    global iter
    iter += 1

    count = 0
    if "?" not in springs:
        if "".join(springs) not in handled_combos:
            handled_combos.add("".join(springs))
            count = check_line(springs, config)
    else:
        for i in range(curr_spring, len(springs)):
            if springs[i] == "#":
                count += make_configs(
                    springs, config, i + 1, group_index, group_count + 1
                )
            elif springs[i] == ".":
                if group_index == len(config):
                    count += make_configs(springs, config, i + 1, group_index)
                elif group_count == config[group_index]:
                    count += make_configs(springs, config, i + 1, group_index + 1)
                elif group_count != 0:
                    count += make_configs(springs, config, i + 1, group_index + 1)
            elif springs[i] == "?":
                if group_index == len(config):
                    springs[i] = "."
                    count += make_configs(springs, config, i + 1, group_index)
                    springs[i] = "?"
                elif group_count == config[group_index]:
                    springs[i] = "."
                    count += make_configs(springs, config, i + 1, group_index + 1)
                    springs[i] = "?"
                elif group_count != 0:
                    springs[i] = "#"
                    count += make_configs(
                        springs, config, i + 1, group_index, group_count + 1
                    )
                    springs[i] = "."
                    count += make_configs(springs, config, i + 1, group_index + 1)
                    springs[i] = "?"
                else:
                    springs[i] = "#"
                    count += make_configs(
                        springs, config, i + 1, group_index, group_count + 1
                    )
                    springs[i] = "."
                    count += make_configs(springs, config, i + 1, group_index)
                    springs[i] = "?"
                break
    return count


total = 0
for spring in all_springs:
    handled_combos = set()
    iter = 0
    print(math.pow(4, spring.springs.count("?")))
    handled_combos = set()
    val = make_configs(spring.springs, spring.config, 0)
    total += val
    print(val, total, spring.config)
print(total)
