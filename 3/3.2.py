
with open('3.1.txt','r') as f:
    lines = f.read().splitlines()
    num_digits = len(lines[0])
    count1 = [0]*num_digits
    
    ogr_lines = lines.copy()
    i = 0
    while len(ogr_lines) > 1:
        count1 = 0
        removal_list = []
        for line in ogr_lines:
            count1 += int(line[i]) if line[i] == '1' else 0
        if count1 >= len(ogr_lines)/2:
            for line in ogr_lines:
                if line[i] == '0':
                    removal_list.append(line)
        else:
            for line in ogr_lines:
                if line[i] == '1':
                    removal_list.append(line)
        for line in removal_list:
            ogr_lines.remove(line)
        i += 1
    
    ogr = int(ogr_lines[0], 2)

    csr_lines = lines.copy()
    i = 0
    while len(csr_lines) > 1:
        count1 = 0
        removal_list = []
        for line in csr_lines:
            count1 += int(line[i]) if line[i] == '1' else 0
        if count1 < len(csr_lines)/2:
            for line in csr_lines:
                if line[i] == '0':
                    removal_list.append(line)
        else:
            for line in csr_lines:
                if line[i] == '1':
                    removal_list.append(line)
        for line in removal_list:
            csr_lines.remove(line)
        i += 1
    
    csr = int(csr_lines[0], 2)

    print(ogr*csr)