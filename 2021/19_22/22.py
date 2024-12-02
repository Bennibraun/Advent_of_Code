

card = 2020
m = 119315717514047 # of cards
d = 101741582076661 # of shuffles

# def increment(card,incr):
#     return (incr*card)%m

# def cut(card,x):
#     return (card-x)%m

# def stack(card):
#     return (-(card+1))%m


a,b = 1,0
with open('22.1.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if 'increment' in line:
            i = int(line.split(' ')[-1])
            a = (i * a) % m
            b = (i * b) % m
        elif 'cut' in line:
            c = int(line.split(' ')[-1])
            a = (a)%m
            b = (b-c)%m
        else:
            a = (-a)%m
            b = (-b-1)%m

# print((a*card+b)%m)


# Fermat's Little Theorem 
def inv(a,m):
    return pow(a,m-2,m)

# Find a card
a_d = pow(a,d,m)
b_d = ((b * (a_d-1)) * inv(a-1,m)) % m

print((a_d*card+b_d)%m)

# Find a position
print(((card-b_d) * inv(a_d,m)) % m)
