with open('1.txt', 'r') as file:
    n1,n2 = [],[]
    for line in file:
        n1.append(line.split()[0])
        n2.append(line.split()[1])

#part 1
n1 = sorted(n1)
n2 = sorted(n2)
dist_sum = 0
for i in range(len(n1)):
    dist_sum += abs(int(n1[i])-int(n2[i]))
print(dist_sum)

#part 2
dict = {}
dict_sum = 0
for i in range(len(n1)):
    if n1[i] not in dict:
        dict[n1[i]] = int(n1[i]) * len([x for x in n2 if x == n1[i]])
    dict_sum += dict[n1[i]]
print(dict_sum)
