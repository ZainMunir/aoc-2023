import sys
from heapq import heappop, heappush
import math

# Looking at the input file (and the graph), we see that rx is only reached from kz.
# Logically, as rx is a conjunction, it will only be low if all of it's inputs send it a high right before,
# and as each of those are also conjunctions, they will only output high if all of their inputs are also high.
# From the graph, we can also see that each of these 4 inputs are disjoint as well
# If we find the number of presses for each of inputs, we can find out when kz outputs high which is when rx will also output high
# However, this ends up taking a very long time, so it's faster to instead find when each of the 4 inputs to kz outputs high individually,
# and take the Lowest Common Multiple of this to find the actual number


class Flip_flop:
    def __init__(self, mod_type, dest):
        self.mod_type = mod_type  # 0 for %, 1 for &, 2 for broadcast
        self.dest = dest
        self.on = 0


class Conjunction:
    def __init__(self, mod_type, dest):
        self.mod_type = mod_type  # 0 for %, 1 for &, 2 for broadcast
        self.dest = dest
        self.inputs = {}

    def add_conns(self, input):
        self.inputs[input] = 0


class Broadcaster:
    def __init__(self, mod_type, dest):
        self.mod_type = mod_type  # 0 for %, 1 for &, 2 for broadcast
        self.dest = dest


modules = {}
conjunctions = []
flip_flops = []
for line in sys.stdin:
    line = line.rstrip()
    line = line.replace("\ufeff", "")
    if line == "":
        break
    # print(line[1:])
    line = line.split(" -> ")
    name = line[0]
    dest = line[-1].split(", ")
    if name.startswith("%"):
        name = name[1:]
        modules[name] = Flip_flop(0, dest)
        flip_flops.append(name)
    elif name.startswith("&"):
        name = name[1:]
        modules[name] = Conjunction(1, dest)
        conjunctions.append(name)
    else:
        modules[name] = Broadcaster(2, dest)
    # print(name, dest, modules[name].mod_type)

for flip in flip_flops:
    flop = modules[flip]
    for dest in flop.dest:
        if dest in conjunctions:
            modules[dest].add_conns(flip)

kz_inputs = {}
found = False
presses = 0
while not found:
    queue = [(0, "broadcaster", "button")]  # signal, dest, src
    presses += 1
    while queue:
        signal, name, src = heappop(queue)
        # print(src, "-", signal, "->", name)
        if name == "kz" and signal:
            if src not in kz_inputs:
                kz_inputs[src] = presses
            if len(kz_inputs) == 4:
                found = True
                break
        if name not in modules:
            continue
        module = modules[name]
        if module.mod_type == 2:
            for dest in module.dest:
                heappush(queue, (signal, dest, name))
        elif module.mod_type == 0:
            if signal:
                continue
            module.on = 1 - module.on
            for dest in module.dest:
                heappush(queue, (module.on, dest, name))
        elif module.mod_type == 1:
            module.inputs[src] = signal
            if all(module.inputs.values()):
                send = 0
            else:
                send = 1
            for dest in module.dest:
                heappush(queue, (send, dest, name))

print(kz_inputs)
print(math.lcm(*[value for value in kz_inputs.values()]))
