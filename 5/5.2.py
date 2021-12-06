
def transpose(l1):
    l2 =[[row[i] for row in l1] for i in range(len(l1[0]))]
    return l2


def add_line(board,line):
    if line[0]==line[2]:
        x = line[0]
        y1 = min(line[1],line[3])
        y2 = max(line[1],line[3])
        for y in range(y1,y2+1):
            board[y][x] += 1
    elif line[1]==line[3]:
        y = line[1]
        x1 = min(line[0],line[2])
        x2 = max(line[0],line[2])
        for x in range(x1,x2+1):
            board[y][x] += 1
    else:
        x1,y1,x2,y2 = line
        if x2>x1:
            xi = 1
        else:
            xi = -1
        if y2>y1:
            yi = 1
        else:
            yi = -1
        
        x = x1
        y = y1
        while (xi==1 and x<=x2) or (xi==-1 and x>=x2):
            board[x][y] += 1
            y += yi
            x += xi

    return board


with open('5.1.txt', 'r') as f:
    data = f.read().splitlines()
    data = [d.split(' -> ') for d in data]
    data = [[d[0].split(),d[1].split()] for d in data]
    data = [[d[0][0].split(','),d[1][0].split(',')] for d in data]
    data = [[[int(e[0]),int(e[1])] for e in d] for d in data]
    data = [d[0]+d[1] for d in data]

    board = [[0]*1000 for _ in range(1000)]

    for line in data:
        board = add_line(board,line)
    
    # board = transpose(board)

    # print([i for i in range(60)])
    # for i in range(60):
    #     print([i]+board[i][:60])

    overlaps = 0
    for b in board:
        for n in b:
            if n > 1:
                overlaps += 1


    print(overlaps)