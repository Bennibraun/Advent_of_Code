import numpy as np

with open('13.txt','r') as f:
    paper = set()
    for line in f:
        if line == '\n':
            break
        paper.add(tuple([int(i) for i in line.strip().split(',')]))
    folds = []
    for line in f:
        line = line.strip()
        if line[:-1] == 'fold along y=':
            folds.append(['y',int(line[len('fold along y='):])])
        else:
            folds.append(['x',int(line[len('fold along x='):])])

# print(paper)
# print(folds)

def fold(dots, f, i):
    new_dots = set()
    for dot in [list(d) for d in dots]:
        if dot[i] > f:
            dot[i] -= (dot[i] - f) * 2
        new_dots.add(tuple(dot))
    return new_dots

for f in folds:
    paper = fold(paper, f[1], f[0] == 'y')

# print(len(paper))


def print_dots(dots):
    y_max = max(map(lambda d: d[1], dots))
    x_max = max(map(lambda d: d[0], dots))
    for y in range(y_max+1):
        print(''.join(['#' if (x,y) in dots else '.' for x in range(x_max+1)]))

print_dots(paper)