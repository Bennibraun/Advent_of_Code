
with open('2.1.txt', 'r') as f:
    pos, depth, aim = 0, 0, 0
    for line in f:
        direction, distance = line.split()
        distance = int(distance)
        if direction == 'forward':
            pos += distance
            depth += aim*distance
        elif direction == 'up':
            aim -= distance
        elif direction == 'down':
            aim += distance
    print(pos*depth)