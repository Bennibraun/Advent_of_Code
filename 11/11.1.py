
with open('11.1.txt', 'r') as f:
    octos = []
    for line in f:
        octos.append([int(n) for n in line.strip()])


def flash(r,c):
    global octos
    global count
    global flashed
    if [r,c] in flashed:
        return
    count += 1
    octos[r][c] = 0
    flashed.append([r,c])
    for rs in range(r-1,r+2):
        for cs in range(c-1,c+2):
            if rs == r and cs == c:
                pass
            elif rs >= 0 and rs < len(octos) and cs >= 0 and cs < len(octos[0]) and [rs,cs] not in flashed:
                octos[rs][cs] += 1
                if octos[rs][cs] > 9:
                    flash(rs,cs)

def step():
    global octos
    flash_locs = []
    for r in range(len(octos)):
        for c in range(len(octos[0])):
            octos[r][c] += 1
            if octos[r][c] > 9:
                flash_locs.append([r,c])
    for (r,c) in flash_locs:
        flash(r,c)

count = 0
flashed = []
for i in range(500):
    flashed = []
    step()

print(count)