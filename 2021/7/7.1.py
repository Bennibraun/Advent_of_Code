with open('7.1.txt','r') as f:
    crabs = [int(c) for c in f.readline().split(',')]

steps = [sum(list(range(1,n))) for n in range(2,max(crabs)+3)]
print(steps)
min_fuel = 100000000000
for pos in range(min(crabs),max(crabs)+1):
    fuel = 0
    for crab in crabs:
        fuel += steps[abs(crab-pos)-1]
    if fuel < min_fuel:
        min_fuel = fuel

print(min_fuel)