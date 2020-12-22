from all_inputs import day_22


def parse(inp):
    p1, p2 = inp.split('\n\n')
    p1 = [int(n) for n in p1.splitlines()[1:]]
    p2 = [int(n) for n in p2.splitlines()[1:]]
    return p1, p2


def play_round(p1, p2):
    c1, p1 = p1[0], p1[1:]
    c2, p2 = p2[0], p2[1:]
    if c1 > c2:
        p1 += [c1, c2]
    else:
        p2 += [c2, c1]
    return p1, p2


def combat(p1, p2):
    while p1 and p2:
        p1, p2 = play_round(p1, p2)

    return p1, p2

inp = day_22
p1, p2 = parse(inp)
p1, p2 = combat(p1, p2)
winner = max(p1, p2)

total = 0
for n, i in zip(winner, range(len(winner), 0, -1)):
    total += n * i

print(f'Part 1 total: {total}')

### Part 2 ###

def entered_loop(p1, p2, p1hist, p2hist):
    return p1 in p1hist or p2 in p2hist


def recursive_combat(p1, p2, p1hist, p2hist, lvl):
    if not (p1 and p2):
        return p1, p2

    while p1 and p2:
        if entered_loop(p1, p2, p1hist, p2hist):
            return p1, []

        p1hist += [p1]
        p2hist += [p2]

        c1, p1 = p1[0], p1[1:]
        c2, p2 = p2[0], p2[1:]

        if len(p1) < c1 or len(p2) < c2:
            if c1 > c2:
                p1 += [c1, c2]
            else:
                p2 += [c2, c1]
        else:
            r1, r2 = recursive_combat(p1[:c1], p2[:c2], [], [], lvl + 1)
            if r1 > r2:
                p1 += [c1, c2]
            else:
                p2 += [c2, c1]
    return [p1, p2]


inp = day_22
p1, p2 = parse(inp)

f1, f2 = recursive_combat(p1, p2, [], [], 0)

winner = max(f1, f2)

total = 0
for n, i in zip(winner, range(len(winner), 0, -1)):
    total += n * i

print(f'Part 2 total: {total}')