from itertools import product 

t_inp = """.#.
..#
###"""


day_17 = """##.#####
#.##..#.
.##...##
###.#...
.#######
##....##
###.###.
.#.#.#.."""

inp = t_inp



def parse(r_inp):
    inp = r_inp
    inp = inp.splitlines()
    
    active_cubes = set()
    for y, row in enumerate(inp):
        for x, state in enumerate(row):
            if state == '#':
                active_cubes.add((x,y,0))
    return active_cubes

def get_neighbors(pos):
    x, y, z = pos
    out = []
    for xo, yo, zo in product((-1,0,1), repeat =3):
        if any((xo, yo, zo)):
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
        if cube_active and neighbors_active in (2,3):
            new_active_cubes.add(pa_cube)
        elif not cube_active and neighbors_active == 3:
            new_active_cubes.add(pa_cube)
    return new_active_cubes
        
        
inp = day_17
active_cubes = parse(inp)
for _ in range(6):
    active_cubes = cycle(active_cubes)
    
len(active_cubes)

### Part 2 ###





def parse2(r_inp):
    inp = r_inp
    inp = inp.splitlines()
    
    active_cubes = set()
    for y, row in enumerate(inp):
        for x, state in enumerate(row):
            if state == '#':
                active_cubes.add((x,y,0,0))
    return active_cubes


def get_neighbors2(pos):
    x, y, z, w = pos
    out = []
    for xo, yo, zo, wo in product((-1,0,1), repeat =4):
        if any((xo, yo, zo, wo)):
            out += [(x+xo, y+yo, z+zo, w+wo)]
    return out
    

def get_potentially_active2(active_cubes):
    with_neighbors = set()
    for cube in active_cubes:
        with_neighbors.add(cube)
        for neighbor in get_neighbors2(cube):
            with_neighbors.add(neighbor) 
    return with_neighbors
        

def count_active_neighbors2(cube):
    active_neighbors = 0
    for neighbor in get_neighbors2(cube):
        if neighbor in active_cubes:
            active_neighbors += 1
    return active_neighbors
        

def cycle2(active_cubes):
    potentially_active = get_potentially_active2(active_cubes)
    new_active_cubes = set()
    for pa_cube in potentially_active:
        cube_active = pa_cube in active_cubes
        neighbors_active = count_active_neighbors2(pa_cube)
        if cube_active and neighbors_active in (2,3):
            new_active_cubes.add(pa_cube)
        elif not cube_active and neighbors_active == 3:
            new_active_cubes.add(pa_cube)
    return new_active_cubes
        
        
inp = day_17
active_cubes = parse2(inp)
for _ in range(6):
    active_cubes = cycle2(active_cubes)
    
len(active_cubes)
