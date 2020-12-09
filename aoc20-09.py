from itertools import combinations
from all_inputs import day_9

def parse_input(raw):
    return [int(x) for x in raw.splitlines()]


def cant_be_sum(target_number, number_set):
    for a, b in combinations(number_set, 2):
        if a + b == target_number:
            return False
    return True


inp = parse_input(day_9)


preamble = 25
for i, n in enumerate(inp[:-preamble]):
    target_number = inp[preamble + i]
    number_set = set(inp[i: i + preamble])
    if cant_be_sum(target_number, number_set):
        print(target_number)
        break

### Part 2 ###

target = 731031916

subtotal = 0
for i, n in enumerate(inp):
    subtotal = n
    j = i
    sublist = [n]
    while subtotal < target:
        j += 1
        subtotal += inp[j]
        sublist += [inp[j]]
    if subtotal == target:
        print(min(sublist) + max(sublist))
        break
        
        
