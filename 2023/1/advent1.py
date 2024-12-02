import re


f = open('advent1.txt','r')
lo
# Part 1
int_str = [str(i) for i in range(0,10)]
sum = 0

for line in f.readlines():
    first_int,last_int = None,None
    for c in line:
        if c in int_str:
            if first_int is None:
                first_int = c
                last_int = c
            else:
                last_int = c
    sum += int(first_int+last_int)

print(sum)
f.close()

# Part 2
sum = 0
num_str = ['one','two','three','four','five','six','seven','eight','nine']
num_str_fixed = ['o1e','t2o','th3ee','f4ur','f5ve','s6x','se7en','ei8ht','n9ne']
conv_to_ridiculous_half_nums = {num_str[i]:num_str_fixed[i] for i in range(len(num_str))}

f = open('advent1.txt','r')

for line in f.readlines():
    print(line)
    first_int,last_int = None,None
    
    for dig,num in conv_to_ridiculous_half_nums.items():
        line = line.replace(dig,num)
    for c in line:
        if c in int_str:
            print(c)
            if first_int is None:
                first_int = c
            last_int = c

    print(line+': '+first_int+last_int)
    sum += int(first_int+last_int)

print(sum)
