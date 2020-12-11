from all_inputs import day_10

def get_neighbors(x,y):
    temp = [
        (x-1, y-1), (x-1, y), (x-1, y+1),
        (x, y-1), (x, y+1),
        (x+1, y-1), (x+1, y), (x+1, y+1)
    ]
    return ((x,y) for (x,y) in temp if (0<=x<max_x) and( 0<=y<max_y))
    
def apply_round(curr):
    seating_new = []
    for x in range(max_x):
        row_new = []
        for y in range(max_y):
            seat_current = curr[x][y]
            if seat_current == '.':
                seat_new = '.'
            elif seat_current =='L':
                occupied_neighbors = sum(1 for (xn,yn) in get_neighbors(x, y) if curr[xn][yn] == "#" )
                seat_new = '#' if occupied_neighbors == 0 else 'L'
            elif seat_current == '#':
                occupied_neighbors = sum(1 for (xn,yn) in get_neighbors(x, y) if curr[xn][yn] == "#" )
                seat_new = 'L' if occupied_neighbors > 3 else '#'
            else:
                raise Exception()
            row_new += [seat_new]
        seating_new += [row_new]
    return seating_new

def same_seating(seating_current, seating_new):
    for r_c, r_n in zip(seating_current, seating_new):
        for c, n in zip(r_c, r_n):
            if c != n:
                return False
    return True

def part_1(inp):
    global max_x, max_y
    max_x, max_y = len(inp), len(inp[0])


    current, new = inp, apply_round(inp)

    seats_same = same_seating(current, new)

    while not seats_same:
        new_t = apply_round(new)
        current = new
        new = new_t
        seats_same = same_seating(current, new)

    total_occupied = 0
    for r in new:
        for s in r:
            if s == '#':
                total_occupied +=1
    return total_occupied



inp = day_10
inp = [list(r) for r in inp.splitlines()]



part_1(inp)

### part 2 ###



def get_visible(x, y):
    global inp
    visible = []
    # right
    for i in range(y+1, len(inp[0])):
        if inp[x][i] == 'L':
            visible += [(x,i)]
            break

    # down 
    for i in range(x+1,len(inp)):
        if inp[i][y] == 'L':
            visible += [(i, y)]
            break
            
    # left        
    for i in range(y-1,-1,-1):
        if inp[x][i] == 'L':
            visible += [(x,i)]
            break
    # up
    for i in range(x-1,-1,-1):
        if inp[i][y] == 'L':
            visible += [(i, y)]
            break
            
    # down right
    dist = 1
    _x, _y = x, y
    
    while True:
        _x += 1
        _y += 1
        if (_x >= len(inp)) or (_y >= len(inp[0])):
            break
        if inp[_x][_y] == 'L':
            visible += [(_x, _y)]
            break
        
    # up right
    dist = 1
    _x, _y = x, y
    
    while True:
        _x -= 1
        _y += 1
        if (_x < 0) or (_y >= len(inp[0])):
            break
        if inp[_x][_y] == 'L':
            visible += [(_x, _y)]
            break
        
    # down left
    dist = 1
    _x, _y = x, y
    
    while True:
        _x += 1
        _y -= 1
        if (_x >= len(inp)) or (_y < 0):
            break
        if inp[_x][_y] == 'L':
            visible += [(_x, _y)]
            break
    
    # up left
    dist = 1
    _x, _y = x, y
    
    while True:
        _x -= 1
        _y -= 1
        if (_x < 0) or (_y < 0):
            break
        if inp[_x][_y] == 'L':
            visible += [(_x, _y)]
            break

    return visible


    
def apply_round2(curr):
    seating_new = []
    for x in range(max_x):
        row_new = []
        for y in range(max_y):
            seat_current = curr[x][y]
            if seat_current == '.':
                seat_new = '.'
            elif seat_current =='L':
                occupied_neighbors = sum(1 for (xn,yn) in get_visible(x, y) if curr[xn][yn] == "#" )
                seat_new = '#' if occupied_neighbors == 0 else 'L'
            elif seat_current == '#':
                occupied_neighbors = sum(1 for (xn,yn) in get_visible(x, y) if curr[xn][yn] == "#" )
                seat_new = 'L' if occupied_neighbors > 4 else '#'
            else:
                raise Exception()
            row_new += [seat_new]
        seating_new += [row_new]
    return seating_new


def part_2(inp):
    global max_x, max_y
    max_x, max_y = len(inp), len(inp[0])
    current, new = inp, apply_round2(inp)
    
    seats_same = same_seating(current, new)

    while not seats_same:
        new_t = apply_round2(new)
        current = new
        new = new_t
        seats_same = same_seating(current, new)

    total_occupied = 0
    for r in new:
        for s in r:
            if s == '#':
                total_occupied +=1
    return total_occupied

inp = day_10
inp = [list(r) for r in inp.splitlines()]

part_2(inp)
