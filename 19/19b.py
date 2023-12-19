import sys
from itertools import product


class WorkFlow:
    def __init__(self, xmas, val, condition, result, bypass=False):
        self.xmas = xmas
        self.val = val
        self.condition = condition
        self.result = result
        self.bypass = bypass


workflows = {"A": True, "R": False}
for line in sys.stdin:
    line = line.rstrip()
    line = line.replace("\ufeff", "")
    if line == "":
        break
    name, steps = line.split("{")
    steps = steps[:-1].split(",")

    step_list = []
    for i in range(len(steps) - 1):
        if steps[i].find(">") == 1:
            xmas, other = steps[i].split(">")
            condition = 0
        else:
            xmas, other = steps[i].split("<")
            condition = 1
        val, res = other.split(":")
        step_list.append(WorkFlow(xmas, int(val), condition, res))
        # print(xmas, val, condition, res)
    step_list.append(WorkFlow(-1, 0, 0, steps[-1], True))
    workflows[name] = step_list


def solve(input, workflow):
    # print(input, workflow)
    if not isinstance(workflow, list):
        if not workflow:
            return 0
        # print(input)
        return len(input["x"]) * len(input["m"]) * len(input["a"]) * len(input["s"])
    total = 0
    for step in workflow:
        if step.bypass:
            total += solve(input, workflows[step.result])
        elif step.val in input[step.xmas]:
            new_input = input.copy()
            if step.condition == 0:
                new_input[step.xmas] = range(step.val + 1, new_input[step.xmas].stop)
                input[step.xmas] = range(input[step.xmas].start, step.val + 1)
            else:
                new_input[step.xmas] = range(new_input[step.xmas].start, step.val)
                input[step.xmas] = range(step.val, input[step.xmas].stop)
            total += solve(new_input, workflows[step.result])
    return total


init_input = {
    "x": range(1, 4001),
    "m": range(1, 4001),
    "a": range(1, 4001),
    "s": range(1, 4001),
}
result = solve(init_input, workflows["in"])
print(result)
