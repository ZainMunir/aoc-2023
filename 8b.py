import re
import sys
from datetime import timedelta, datetime
import numpy as np
import math

instructions = sys.stdin.readline().rstrip()
instructions = instructions.replace(" ", "")
instructions = instructions.replace("\ufeff", "")

dictionary = dict()

a_nodes = []
for line in sys.stdin:
    line = line.rstrip()
    if line == "":
        continue
    froms, tos = line.split(" = ")
    lhs, rhs = tos.split(", ")
    lhs = lhs[1:]
    rhs = rhs[:-1]
    dictionary[froms] = (lhs, rhs)
    if froms[-1] == "A":
        a_nodes.append(froms)

steps = 0
done = 0
paths = [-1] * len(a_nodes)
while True:
    curr_step = instructions[steps % len(instructions)]
    for i in range(len(a_nodes)):
        if paths[i] != -1:
            continue
        if curr_step == 'L':
            a_nodes[i] = dictionary[a_nodes[i]][0]
        else:
            a_nodes[i] = dictionary[a_nodes[i]][1]
        if a_nodes[i][-1] == 'Z':
            done += 1
            paths[i] = steps + 1
    steps += 1
    if done == len(a_nodes):
        break
print(paths)
print(math.lcm(*paths))
