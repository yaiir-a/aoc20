from all_inputs import day_10

def parse_inp(r_inp):
    return sorted([int(n) for n in r_inp.splitlines()])


inp = parse_inp(day_10)


inp_shifted = [0] + inp
inp += [inp[-1] + 3]

from collections import Counter
differences = []
for a, b in zip(inp, inp_shifted):
    differences += [a - b]
    
c = Counter(differences)
print(c[1] * c[3])

### Part 2 ###

def findStep( n) : 
    if (n == 1 or n == 0) : 
        return 1
    elif (n == 2) : 
        return 2
    else : 
        return findStep(n - 3) + findStep(n - 2) + findStep(n - 1)  

def run_length(differences):
    diff_str = ''.join((str(i) for i in differences))
    split_str = diff_str.split('3')
    return [len(sub) if sub else 1 for sub in split_str]

def num_combinations(run_lengths):
    combinations = 1
    for l in run_lengths:
        combinations *= findStep(l)
    return combinations


r = run_length(differences)

print(num_combinations(r))