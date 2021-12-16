import numpy as np

def parse_packet(data,cur):

    global version_sum
    
    V = int(data[cur:cur+3],2)
    version_sum += V
    cur += 3

    T = int(data[cur:cur+3],2)
    cur += 3

    val = 0
    if T==4:
        #literal value
        start = cur
        bin_num = ''
        while True:
            bin_num += data[cur+1:cur+5]
            if data[cur] == '0':
                cur += 5
                break
            else:
                cur += 5

        val = int(bin_num,2)
        return cur, val
    else:
        #operator
        length = int(data[cur],2)
        length = 15 if length==0 else 11
        cur += 1

        vals = []
        start = cur
        if length == 15:
            # length-based subpackets
            sub_length = int(data[cur:cur+length],2)
            cur += length
            start = cur
            while cur-start < sub_length:
                cur, val = parse_packet(data,cur)
                vals.append(val)
        else:
            # num-based subpackets
            num_packets = int(data[cur:cur+length],2)

            cur += length
            start = cur
            for i in range(num_packets):
                cur,val = parse_packet(data,cur)
                vals.append(val)
        
        if T == 0:
            val = sum(vals)
        elif T == 1:
            val = np.prod(vals)
        elif T == 2:
            val = min(vals)
        elif T == 3:
            val = max(vals)
        elif T == 5:
            val = 1 if vals[0]>vals[1] else 0
        elif T == 6:
            val = 1 if vals[0]<vals[1] else 0
        elif T == 7:
            val = 1 if vals[0]==vals[1] else 0

        
        return cur, val
            

with open("16.txt") as f:
    data = f.read()

data = bin(int('1'+data,16))[3:]

version_sum = 0
cur = 0

while cur < len(data)-1 and int(data[cur:],2) != 0:   
    cur, val = parse_packet(data,cur)

print(version_sum)
print(val)