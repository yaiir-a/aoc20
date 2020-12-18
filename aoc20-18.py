from all_inputs import day_18

def calc(loc, inp, adv):
    if len(inp) == 1:
        return int(inp[0])
    
    left, op, right = inp[loc:loc+3]
    if '(' in right:
        return calc(loc+2, inp, adv)
    if adv and (op == '*') and ('+' in inp) and (')' not in right):
        return calc(loc+2, inp, adv)
    
    paren_open, paren_close = left.count('('), right.count(')')
    num_left, num_right = int(left[paren_open:]), int(right[:-paren_close if paren_close else None])

    if op == '*':
        val = num_left * num_right
    elif op == '+':
        val = num_left + num_right
        
    val_str = (paren_open - paren_close)*'(' + str(val) + (paren_close - paren_open)*')'
        
    new_inp = inp[:loc] + [val_str] + inp[loc+3:]
    return calc(0, new_inp, adv)
    
    



inps = day_18.splitlines()

print(sum(calc(0, inp.split(' '), adv=False) for inp in inps))
print(sum(calc(0, inp.split(' '), adv=True) for inp in inps))