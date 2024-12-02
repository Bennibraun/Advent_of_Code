
def find_error(line):
    stack = []
    open_b = ['(', '[', '{', '<']
    close_b = [')', ']', '}', '>']
    value = {')': 3, ']': 57, '}': 1197, '>': 25137}

    for char in line:
        if char in open_b:
            stack.append(char)
        elif char in close_b:
            pos = close_b.index(char)
            if len(stack) > 0 and open_b[pos] == stack[-1]:
                stack.pop()
            else:
                return value[char]
    
    return 0




with open('10.1.txt','r') as f:
    summa = 0
    for line in f:
        summa += find_error(line)
    print(summa)