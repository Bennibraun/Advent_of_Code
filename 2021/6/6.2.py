
with open('6.1.txt', 'r') as f:
    fish = f.readline().split(',')

fish = [int(f) for f in fish]

fish_counts = [0]*9
for f in fish:
    fish_counts[f] += 1

n = 256

for day in range(1,n+1):
    new_fish = fish_counts[0]
    for i in range(0,8):
        fish_counts[i] = fish_counts[i+1]
    fish_counts[8] = new_fish
    fish_counts[6] += new_fish
    # print(fish_counts)
    # [5,3,4,2,3,4,5,7,4]
    # [3,4,2,3,4,5,7+5,4,5]

print(sum(fish_counts))

# wrong: 26984457539