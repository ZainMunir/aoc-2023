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
    nums = list(map(int, pattern.findall(nums)))
    all_springs.append(SpringLine(springs, nums))


def check_line(springs, config):
    groups = springs.split(".")
    hash_counts = [group.count("#") for group in groups if group.count("#") > 0]
    return hash_counts == config


def make_configs(memo, springs, config, curr_spring, group_index=0, group_count=0):
    if springs.count("#") > sum(config):
        return 0
    elif springs.count("#") + springs.count("?") < sum(config):
        return 0
    key = "".join(springs)
    if key in memo:
        return 0
    global iter
    iter += 1
    if iter % 1000000 == 0:
        print(iter)

    count = 0
    if "?" not in springs:
        count = check_line(springs, config)
    else:
        for i in range(curr_spring, len(springs)):
            if springs[i] == "#":
                group_count += 1
            elif springs[i] == ".":
                if group_index == len(config):
                    group_count = 0
                elif group_count == config[group_index] or group_count != 0:
                    group_count = 0
                    group_index += 1
            elif springs[i] == "?":
                if group_index == len(config):
                    count += make_configs(
                        memo,
                        springs[:i] + "." + springs[i + 1 :],
                        config,
                        i + 1,
                        group_index,
                    )
                elif group_count == config[group_index]:
                    count += make_configs(
                        memo,
                        springs[:i] + "." + springs[i + 1 :],
                        config,
                        i + 1,
                        group_index + 1,
                    )
                elif group_count != 0:
                    count += make_configs(
                        memo,
                        springs[:i] + "#" + springs[i + 1 :],
                        config,
                        i + 1,
                        group_index,
                        group_count + 1,
                    )
                    count += make_configs(
                        memo,
                        springs[:i] + "." + springs[i + 1 :],
                        config,
                        i + 1,
                        group_index + 1,
                    )
                else:
                    count += make_configs(
                        memo,
                        springs[:i] + "#" + springs[i + 1 :],
                        config,
                        i + 1,
                        group_index,
                        group_count + 1,
                    )
                    count += make_configs(
                        memo,
                        springs[:i] + "." + springs[i + 1 :],
                        config,
                        i + 1,
                        group_index,
                    )
                break
    memo[key] = count
    return count


total = 0
for spring in all_springs:
    iter = 0
    print(math.pow(4, spring.springs.count("?")))
    val = make_configs(dict(), spring.springs, spring.config, 0)
    total += val
    print(val, total, iter, spring.config)
print(total)


# total = 0
# for spring in all_springs:
#     iter = 0
#     spring.springs = "?".join([spring.springs] * 5)
#     spring.config = spring.config * 5
#     memo = dict()
#     print("".join(spring.springs), spring.config)
#     val = make_configs(memo, spring.springs, spring.config, 0)
#     total += val
#     print(val, total, spring.config)
# print(total)
