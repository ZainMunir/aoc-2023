import re
import sys


instructions = sys.stdin.readline().rstrip()
instructions = instructions.replace(" ", "")
instructions = instructions.replace("\ufeff", "")

dictionary = dict()

for line in sys.stdin:
    line = line.rstrip()
    if line == "":
        continue
    froms, tos = line.split(" = ")
    lhs, rhs = tos.split(", ")
    lhs = lhs[1:]
    rhs = rhs[:-1]
    dictionary[froms] = (lhs, rhs)

steps = 0

curr_pos = "AAA"
while True:
    curr_step = instructions[steps % len(instructions)]
    if curr_step == 'L':
        curr_pos = dictionary[curr_pos][0]
    elif curr_step == 'R':
        curr_pos = dictionary[curr_pos][1]
    print(steps, curr_step, curr_pos)
    steps += 1
    if curr_pos == "ZZZ":
        break

    

print(steps)