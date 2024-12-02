import collections

with open('14.txt', 'r') as f:
    polymer = f.readline().strip()
    inp = [line for line in f.read().strip().splitlines()]
    inp = [[p for p in line.split(' -> ')] for line in inp]
    rules = {}
    for rule in inp:
        rules[rule[0]] = rule[1]


def insert (source_str, insert_str, pos):
    return source_str[:pos]+insert_str+source_str[pos:]


def step(polymer):
    new_polymer = polymer
    np = 1
    for p in range(len(polymer) - 1):
        # print(new_polymer)
        pair = polymer[p:p + 2]
        if pair in rules.keys():
            new_polymer = insert(new_polymer, rules[pair], np)
            np += 1
        np += 1
    return new_polymer

# part 1
# for i in range(40):
    # print(polymer)
    # polymer = step(polymer)

# counts = collections.Counter(polymer)
# print(counts.most_common()[0])
# print(counts.most_common()[-1])
# print(counts.most_common()[0][1]-counts.most_common()[-1][1])

# part 2

def step_c(counts,letters):
    new_counts = counts.copy()
    for pair in counts.keys():
        if pair in rules.keys():
            # print('removing', pair)
            new_counts[pair] -= counts[pair]
            # print('adding',pair[0]+rules[pair])
            new_counts[pair[0]+rules[pair]] += counts[pair]
            # print('adding',rules[pair]+pair[1])
            new_counts[rules[pair]+pair[1]] += counts[pair]
            letters[rules[pair]] += counts[pair]
    return new_counts,letters

counts = rules.copy()
letters = {'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'I':0,'J':0,'K':0,'L':0,'M':0,'N':0,'O':0,'P':0,'Q':0,'R':0,'S':0,'T':0,'U':0,'V':0,'W':0,'X':0,'Y':0,'Z':0}
for l in polymer:
    letters[l] += 1
for key in counts.keys():
    counts[key] = polymer.count(key)

# print(counts)

for i in range(40):
    counts,letters = step_c(counts,letters)
    # print(counts)

letters = {key:value for key,value in letters.items() if value > 0}
print(letters)
print(max(letters.values()))
print(min(letters.values()))
print(max(letters.values())-min(letters.values()))