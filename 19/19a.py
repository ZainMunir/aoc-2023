import sys


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

inputs = []
for line in sys.stdin:
    line = line.rstrip()
    line = line.replace("\ufeff", "")
    if line == "":
        break
    line = line[1:-1].split(",")
    temp_dict = {}
    for i in range(len(line)):
        temp_dict[line[i][0]] = int(line[i][2:])
    inputs.append(temp_dict)


def solve(input, workflow):
    # print(input, workflow)
    if not isinstance(workflow, list):
        return workflow
    for step in workflow:
        if step.bypass:
            return solve(input, workflows[step.result])
        if step.condition == 0:
            if input[step.xmas] > step.val:
                return solve(input, workflows[step.result])
        else:
            if input[step.xmas] < step.val:
                return solve(input, workflows[step.result])


total = 0
for input in inputs:
    if solve(input, workflows["in"]):
        total += sum(input.values())
print(total)
