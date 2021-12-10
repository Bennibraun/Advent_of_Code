import numpy as np


def find_error(line):
    stack = []
    open_b = ['(', '[', '{', '<']
    close_b = [')', ']', '}', '>']

    for char in line:
        if char in open_b:
            stack.append(char)
        elif char in close_b:
            pos = close_b.index(char)
            if len(stack) > 0 and open_b[pos] == stack[-1]:
                stack.pop()
            else:
                return True
    return False



def auto_complete(line):
    value = {')': 1, ']': 2, '}': 3, '>': 4}

    stack = []
    open_b = ['(', '[', '{', '<']
    close_b = [')', ']', '}', '>']
    completion = ''

    for char in line:
        if char in open_b:
            stack.append(char)
        elif char in close_b:
            pos = close_b.index(char)
            if len(stack) > 0 and open_b[pos] == stack[-1]:
                stack.pop()
    
    while len(stack) > 0:
        b = stack.pop()
        completion += close_b[open_b.index(b)]
    
    val = 0
    for b in completion:
        val *= 5
        val += value[b]
    
    return val

with open('10.1.txt','r') as f:
    scores = []
    for line in f:
        if not find_error(line):
            scores.append(auto_complete(line))
    print(int(np.median(scores)))
