def part_1(inp):
    inp = inp.splitlines()
    width_map = len(inp[0])

    i = 0
    num_trees = 0
    for row in inp:
        if row[i] == '#':
            num_trees += 1
        i = (i + 3) % width_map
    
    return num_trees


### Part 2 ###

slopes = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))

def part_2(inp):
    inp = inp.splitlines()
    final_answer = 1
    for r, d in slopes:
        final_answer *= check_slope(inp, r, d)
    return final_answer


def check_slope(inp, r, d):
    width_map = len(inp[0])

    i = 0
    num_trees = 0
    for row in inp[::d]:
        if row[i] == '#':
            num_trees += 1
        i = (i + r) % width_map
    return num_trees
    