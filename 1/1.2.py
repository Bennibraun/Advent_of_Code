import math

with open('1.1.txt', 'r') as f:
    prev_window = [int(f.readline()) for _ in range(3)]
    incr_ct = 0
    for line in f:
        window = prev_window[1:] + [int(line)]
        if sum(window) > sum(prev_window):
            incr_ct += 1
        prev_window = window
    print(incr_ct)