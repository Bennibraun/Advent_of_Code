
with open('3.1.txt','r') as f:
    lines = f.read().splitlines()
    num_digits = len(lines[0])
    count1 = [0]*num_digits
    num_lines = len(lines)
    for line in lines:
        for i in range(num_digits):
            if line[i] == '1':
                count1[i] += 1
    gamma = ''
    for i in range(num_digits):
        gamma += '1' if num_lines-count1[i] < num_lines/2 else '0'
    epsilon = ''.join(['0' if gamma[i] == '1' else '1' for i in range(num_digits)])
    product = int(gamma, 2) * int(epsilon,2)
    print(gamma, epsilon, product)