from all_inputs import day_5

inp = day_5.splitlines()

def parse(code):
    row = int( code[:7].replace('B', '1').replace('F', '0'), 2)
    seat = int( code[7:].replace('R', '1').replace('L', '0'), 2)
    s_id = (row * 8) + seat
    return (row, seat, s_id)

seats = sorted([parse(code) for code in inp], key = lambda x: x[2])

### Part 2 ###

s_ids = set((s[2] for s in seats))

for i in range(min(s_ids), max(s_ids)):
    if i not in s_ids:
        print(i)
        