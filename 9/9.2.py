
with open('9.1.txt', 'r') as f:
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



low_points = []
for r in range(len(heights)):
    for c in range(len(heights[r])):
        if is_low(r,c):
            low_points.append({'r':r,'c':c,'v':heights[r][c]})


def get_adjacent(p):
    adj = []
    r = p['r']
    c = p['c']
    if r > 0:
        adj.append({'r':r-1,'c':c,'v':heights[r-1][c]})
    if r < len(heights)-1:
        adj.append({'r':r+1,'c':c,'v':heights[r+1][c]})
    if c > 0:
        adj.append({'r':r,'c':c-1,'v':heights[r][c-1]})
    if c < len(heights[r])-1:
        adj.append({'r':r,'c':c+1,'v':heights[r][c+1]})
    return adj


def add_to_basin(caller,p,basin):
    adj = get_adjacent(p)
    if caller['v'] <= min([a['v'] for a in adj]):
        basin.append(p)
        for a in adj:
            if a['v'] >= p['v'] and a not in basin and a['v'] < 9:
                basin = add_to_basin(p,a,basin)
    return basin

basin_lengths = []
for p in low_points:
    basin = [p]
    for adj in get_adjacent(p):
        if adj['v'] < 9:
            basin = add_to_basin(p,adj,basin)
    basin_lengths.append(len(basin))

largest_basins = sorted(basin_lengths,reverse=True)[:3]
print(largest_basins[0]*largest_basins[1]*largest_basins[2])