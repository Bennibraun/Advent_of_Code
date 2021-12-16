
with open('15.txt', 'r') as f:
    grid = [[int(x) for x in line.strip()] for line in f.readlines()]

g = len(grid)

full_grid = [[0]*(5*g) for _ in range(5*g)]
for i in range(5):
    for j in range(5):
        for r in range(g):
            for c in range(g):
                val = grid[r][c]+i+j
                if val > 9:
                    val = val%10 + 1
                full_grid[(i*g)+r][(j*g)+c] = val

def djikstra(grid, cur, visited, shortest_paths):
    print('started 8:48')
    while cur != (len(grid[0])-1,len(grid)-1):
        visited.add(cur)
        dest = []
        if cur[0] > 0 and (cur[0]-1,cur[1]) not in visited:
            dest.append((cur[0]-1,cur[1]))
        if cur[0] < len(grid[0])-1 and (cur[0]+1,cur[1]) not in visited:
            dest.append((cur[0]+1,cur[1]))
        if cur[1] > 0 and (cur[0],cur[1]-1) not in visited:
            dest.append((cur[0],cur[1]-1))
        if cur[1] < len(grid)-1 and (cur[0],cur[1]+1) not in visited:
            dest.append((cur[0],cur[1]+1))
        # print(dest)
        weight_to_cur = shortest_paths[cur][1]
        for next_node in dest:
            weight = weight_to_cur + grid[next_node[0]][next_node[1]]
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (cur, weight)
            else:
                cur_shortest_weight = shortest_paths[next_node][1]
                if cur_shortest_weight > weight:
                    shortest_paths[next_node] = (cur, weight)
        
        next_dest = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
        if not next_dest:
            return('impossible route')
        
        cur = min(next_dest, key=lambda x: next_dest[x][1])

    path = []
    while cur is not None:
        path.append(cur)
        cur = shortest_paths[cur][0]

    path = path[::-1]
    return path

cur = (0,0)
shortest_paths = {(0,0): (None, 0)}
visited = set()

# path = djikstra(grid, cur, visited, shortest_paths)
# print(sum([grid[x[0]][x[1]] for x in path])-grid[0][0])


path = djikstra(full_grid, cur, visited, shortest_paths)
print(sum([full_grid[x[0]][x[1]] for x in path])-full_grid[0][0])
