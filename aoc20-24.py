from all_inputs import day_24
from _collections import defaultdict


def parse_line(line):
    i = 0
    moves = []
    while i < len(line):
        move = line[i]
        if move in ('e', 'w'):
            moves += [move]
            i += 1
            continue

        move = line[i:i+2]
        moves += [move]
        i += 2
    return moves


def parse(r_inp):
    lines = r_inp.splitlines()
    out = []
    for line in lines:
        out += [parse_line(line)]
    return out


def move(coord, inst):
    x, y, z = coord
    if 'e' == inst:
        x += 1
        y -= 1
    elif 'w' == inst:
        x -= 1
        y += 1
    elif 'ne' == inst:
        x += 1
        z -= 1
    elif 'nw' == inst:
        y += 1
        z -= 1

    elif 'se' == inst:
        y -= 1
        z += 1

    elif 'sw' == inst:
        x -= 1
        z += 1

    return x, y, z


def get_black(inp):
    floor = defaultdict(int)

    for row in inp:
        coord = 0, 0, 0

        for inst in row:
            coord = move(coord, inst)
        floor[coord] = not floor[coord]

    blacks = set()
    for tile, black in floor.items():
        if black:
            blacks.add(tile)
    return blacks


inp = day_24
inp = parse(inp)
active_cubes = get_black(inp)
print(f'Part 1: {len(active_cubes)}')


def get_neighbors(tile):  # Changed from Day 17
    x, y, z = tile
    neighbors = [
        (1, -1, 0),
        (0, -1, 1),
        (-1, 0, 1),
        (-1, 1, 0),
        (0, 1, -1),
        (1, 0, -1)
    ]
    out = []
    for xo, yo, zo in neighbors:
        out += [(x+xo, y+yo, z+zo)]
    return out

def get_potentially_active(active_cubes):
    with_neighbors = set()
    for cube in active_cubes:
        with_neighbors.add(cube)
        for neighbor in get_neighbors(cube):
            with_neighbors.add(neighbor)
    return with_neighbors


def count_active_neighbors(cube):
    active_neighbors = 0
    for neighbor in get_neighbors(cube):
        if neighbor in active_cubes:
            active_neighbors += 1
    return active_neighbors


def cycle(active_cubes):
    potentially_active = get_potentially_active(active_cubes)
    new_active_cubes = set()
    for pa_cube in potentially_active:
        cube_active = pa_cube in active_cubes
        neighbors_active = count_active_neighbors(pa_cube)
        if cube_active and neighbors_active in (1, 2):  # Changed from Day 17
            new_active_cubes.add(pa_cube)
        elif not cube_active and neighbors_active == 2:  # Changed from Day 17
            new_active_cubes.add(pa_cube)
    return new_active_cubes


for _ in range(100):
    active_cubes = cycle(active_cubes)

print(f'Part 2: {len(active_cubes)}')