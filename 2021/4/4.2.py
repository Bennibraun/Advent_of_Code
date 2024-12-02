
def add_num(n):
    remove_boards = []
    for board in boards:
        for row in board:
            for i in row:
                if i[0] == n:
                    # if n == 16:
                    #     for row in board:
                    #         print(row)
                    i[1] = True
                    if board_wins(board):
                        if len(boards) == 1:
                            print(score(board,n))
                        remove_boards.append(board)
    for board in remove_boards:
        boards.remove(board)

def transpose(l1):
    l2 =[[row[i] for row in l1] for i in range(len(l1[0]))]
    return l2

def board_wins(board):
    for row in board:
        if all(flag==True for (_,flag) in row):
            # print('winning row:',row)
            return True
    T_board = transpose(board)
    for row in T_board:
        if all(flag==True for (_,flag) in row):
            # print('winning col:',row)
            return True

def score(board,last):
    total = 0
    for row in board:
        total += sum([x[0] if not x[1] else 0 for x in row])
    print(total,last)
    return total*last

with open('4.1.txt', 'r') as f:
    nums = [int(n) for n in f.readline().split(',')]
    boards = [[]]
    i = 0
    f.readline()
    for line in f:
        if line == '\n':
            i += 1
            boards.append([])
        else:
            row = [n for n in line.replace('\n','').replace('  ',' ').split(' ')]
            while '' in row:
                row.remove('')
            row = [[int(n),False] for n in row]
            boards[i].append(row)

    i = 0
    for n in nums:
        add_num(n)
        if len(boards) == 0:
            exit()