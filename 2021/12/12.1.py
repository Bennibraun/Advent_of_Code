i = []
paths = []

# Part 1
track = [True, 'start']
# Part 2
track = [False, 'start']

for line in open("12.1.txt"):
    line = line.replace('\n','')
    i += [line.split('-')]

# generators are cool
def next_cave(m):
    if m[-1] == 'end':
        yield m
    else:
        for j in i:
            # if first path is current cave, take second path
            if j[0] == m[-1]:
                # small cave
                if j[1].islower():
                    # take path
                    if j[1] not in m:
                        yield from next_cave(m + [j[1]])
                    # take path as second visit for small cave
                    elif m[0] == False and j[1] != 'start':
                        # Use up the small cave double visit
                        yield from next_cave([True] + m[1:] + [j[1]])
                # large cave
                else:
                    yield from next_cave(m + [j[1]])
            # if second path is current cave, take first path
            elif j[1] == m[-1]:
                if j[0].islower():
                    if j[0] not in m:
                        yield from next_cave(m + [j[0]])
                    elif m[0] == False and j[0] != 'start':
                        yield from next_cave([True] + m[1:] + [j[0]])
                else:
                    yield from next_cave(m + [j[0]])

for a in next_cave(track):
    paths.append(a)

print(len(paths))