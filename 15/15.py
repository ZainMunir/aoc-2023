import sys


line = sys.stdin.readline().rstrip()
line = line.replace("\ufeff", "")
operations = line.split(",")
# print(operations)

totals = []
for op in operations:
    vals = [ord(c) for c in op]
    total = 0
    for val in vals:
        total += val
        total *= 17
        total = total % 256
    totals.append(total)
# print(totals)
print(sum(totals))

hashmap = {}
for i in range(256):
    hashmap[i] = {}

for op in operations:
    equal = False
    if "=" in op:
        label = op.split("=")[0]
        equal = True
    elif "-" in op:
        label = op.split("-")[0]
    vals = [ord(c) for c in label]
    total = 0
    for val in vals:
        total += val
        total *= 17
        total = total % 256
    bucket = hashmap[total]
    if not equal:
        bucket.pop(label, None)
    else:
        bucket[label] = op[-1]


total = 0
for key, val in hashmap.items():
    if val == {}:
        continue
    for i, (key2, val2) in enumerate(val.items()):
        total += (key + 1) * (i + 1) * int(val2)
print(total)
