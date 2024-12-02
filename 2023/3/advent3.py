# 467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..


f = open('advent3.txt','r')
         
# What is the sum of all of the part numbers in the engine schematic?

integers = [str(i) for i in range(0,10)]

def fix_symbols(x):
    if x == '.':
        return ' '
    elif x in integers:
        return x
    else:
        return 'X'

m = []
for line in f.readlines():
    m.append([fix_symbols(x) for x in line.strip()])

def find_nums(row):
    nums = {}
    current = ''
    for i,e in enumerate(row):
        if e in integers:
            if current == '':
                start = i
            current += e
        elif current != '':
            nums[(start,i)] = int(current)
            current = ''
    if current != '':
        nums[(start,i)] = int(current)
    return nums

def adjacent_symbol(row,start,end):
    total_checks = 0
    for i in range(max(0,row-1),min(row+2,len(m))):
        for j in range(max(0,start-1),min(end+1,len(m[0]))):
            total_checks += 1
            if m[i][j] == 'X':
                return True
    return False


# 1. find numbers with coordinates
# 2. check whether they have a symbol adjacent
# 3. add up the valid numbers

sum = 0
for i,row in enumerate(m):
    nums = find_nums(row)
    for loc,n in nums.items():
        if adjacent_symbol(i,loc[0],loc[1]):
            sum += n

print(sum)





f = open('advent3.txt','r')
         
# What is the sum of all of the part numbers in the engine schematic?

integers = [str(i) for i in range(0,10)]

def fix_symbols(x):
    if x == '*':
        return '*'
    elif x == '.':
        return ' '
    elif x in integers:
        return x
    else:
        return 'X'

m = []
for line in f.readlines():
    m.append([fix_symbols(x) for x in line.strip()])


def find_nums(row):
    nums = {}
    current = ''
    for i,e in enumerate(row):
        if e in integers:
            if current == '':
                start = i
            current += e
        elif current != '':
            nums[(start,i)] = int(current)
            current = ''
    if current != '':
        nums[(start,i)] = int(current)
    return nums

def adjacent_symbol(row,start,end):
    for i in range(max(0,row-1),min(row+2,len(m))):
        for j in range(max(0,start-1),min(end+1,len(m[0]))):
            if m[i][j] == 'X':
                return True
    return False

def adjacent_nums(nums,row,col):
    adj_nums = []
    used = []
    for i in range(max(0,row-1),min(row+2,len(m))):
        for j in range(max(0,col-1),min(col+2,len(m[0]))):
            for start,end in nums[i].keys():
                if start <= j <= end-1:
                    if (i,start,end) not in used:
                        adj_nums.append(nums[i][(start,end)])
                        used.append((i,start,end))
    return adj_nums

# 1. find numbers with coordinates
# 2. check whether they have a symbol adjacent
# 3. add up the valid numbers

nums = {}
for i,row in enumerate(m):
    nums[i] = find_nums(row)

gear_ratio_sum = 0
for i,row in enumerate(m):
    for ie,e in enumerate(row):
        if e == '*':
            # find adjacent numbers
            adj_nums = adjacent_nums(nums,i,ie)
            if len(adj_nums) == 2:
                gear_ratio_sum += adj_nums[0] * adj_nums[1]

print(gear_ratio_sum)
