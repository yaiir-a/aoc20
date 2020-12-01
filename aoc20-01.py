def prep_inp(inp):
    return set(int(n) for n in inp.split('\n'))

inp = prep_inp(r_inp)

def part1():
    for n in inp:
        pair = 2020 - n
        if pair in inp:
            return n * pair
            
            
from itertools import combinations

def part2_naive():
    for comb in combinations(inp, 3):
        if sum(comb) == 2020:
            return comb[0] * comb[1] * comb[2]

def prep_inp_l(inp):
    return sorted(list(int(n) for n in inp.split('\n')))

def part2_improved():
    for i_1 in range(len(inp)):
        for i_2 in range(i_1+1, len(inp)):
            for i_3 in range(i_2+1, len(inp)):
                total = inp[i_1] + inp[i_2] + inp[i_3]
                if total == 2020:
                    return inp[i_1] * inp[i_2] * inp[i_3]
                if total > 2020:
                    break