
with open('6.1.txt', 'r') as f:
    fish = f.readline().split(',')

fish = [int(f) for f in fish]

print('Initial state: ', fish)

n = 80

for day in range(1,n+1):
    for f in range(len(fish)):
        if fish[f] == 0:
            fish.append(8)
            fish[f] = 6
        else:
            fish[f] -= 1
    # print('after ', day, ' day(s): ',fish)
print(len(fish))

