
with open('9.1.1.txt', 'r') as f:
    heights = []
    for line in f:
        heights.append([int(n) for n in line.strip()])

def is_low(r,c):
    pt = heights[r][c]
    try:
        if heights[r-1][c] <= pt:
            return False
    except:
        pass
    try:
        if heights[r+1][c] <= pt:
            return False
    except:
        pass
    try:
        if heights[r][c-1] <= pt:
            return False
    except:
        pass
    try:
        if heights[r][c+1] <= pt:
            return False
    except:
        pass

    return True

summa = 0
for r in range(len(heights)):
    for c in range(len(heights[r])):
        if is_low(r,c):
            # print(r,c,': ',heights[r][c])
            summa += 1 + heights[r][c]

print(summa)