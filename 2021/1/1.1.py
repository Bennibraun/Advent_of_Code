import math
with open('1.1.txt', 'r') as f:
    prev = math.inf
    incr_ct = 0
    for line in f:
        if int(line) > prev:
            incr_ct += 1
        prev = int(line)
    print(incr_ct)