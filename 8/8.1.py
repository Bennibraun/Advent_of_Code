with open('8.1.txt', 'r') as f:
    total = 0
    for line in f:
        input, output = line.split('|')
        input = input.strip().split(' ')
        output = output.strip().split(' ')

        for i in range(len(output)):
            seg = len(output[i])
            if seg in [2,4,3,7]:
                total += 1
    print(total)

