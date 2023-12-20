import sys


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


high = 0
low = 0

button_presses = 1000
for i in range(button_presses):
    queue = [(0, "broadcaster", "button")]  # signal, dest, src

    while queue:
        signal, name, src = queue.pop(0)
        # print(src, "-", signal, "->", name)
        if signal:
            high += 1
        else:
            low += 1
        if name not in modules:
            continue
        module = modules[name]
        if module.mod_type == 2:
            for dest in module.dest:
                queue.append((signal, dest, name))
        elif module.mod_type == 0:
            if signal:
                continue
            module.on = 1 - module.on
            for dest in module.dest:
                queue.append((module.on, dest, name))
        elif module.mod_type == 1:
            module.inputs[src] = signal
            if all(module.inputs.values()):
                send = 0
            else:
                send = 1
            for dest in module.dest:
                queue.append((send, dest, name))

print(high, low)
print(high * low)
