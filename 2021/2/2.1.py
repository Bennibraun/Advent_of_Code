
with open('2.1.txt', 'r') as f:
    pos, depth = 0, 0
    for line in f:
        direction, distance = line.split()
        distance = int(distance)
        if direction == 'forward':
            pos += distance
        elif direction == 'up':
            depth -= distance
        else:
            depth += distance
    print(pos*depth)