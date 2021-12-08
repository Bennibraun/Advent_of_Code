from itertools import permutations

with open('8.1.txt','r') as f:
    lines = f.read().strip().split('\n')


display = {'0': 'abcefg', '1': 'cf', '2': 'acdeg', '3': 'acdfg', '4': 'bcdf','5': 'abdfg', '6': 'abdefg','7': 'acf', '8': 'abcdefg', '9': 'abcdfg'}
display_r = {v:k for k, v in display.items()}

summa=0
for line in lines:
    inp, outp = line.strip().split('|')
    inp = [set(x) for x in inp.strip().split()]
    outp = [set(x) for x in outp.strip().split()]
    
    for p in permutations('abcdefg'):
        mapping = dict(zip(p, list('abcdefg')))
        for o in inp:
            dig = ''.join(sorted(mapping[c] for c in o))
            if not dig in display.values():
                break
        else:
            break

    summa += int(''.join(display_r[''.join(sorted(mapping[c] for c in o))] for o in outp))
    
print(summa)