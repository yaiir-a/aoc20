from all_inputs import day_12


def move(sloc, sang, inst):
    x, y = sloc
    code, amount = inst[0], int(inst[1:])
    
    if code == 'F':
        dirs = 'NESW'
        code = dirs[int(sang/90)]
        
    if code == 'N':
        sloc = (x, y + amount)
    elif code == 'S':
        sloc = (x, y - amount)
    elif code == 'E':
        sloc = (x + amount, y)
    elif code == 'W':
        sloc = (x - amount, y)
    elif code == 'R':
        sang = (sang + amount) % 360
    elif code == 'L':
        sang = (sang - amount) % 360
            
    return sloc, sang
    
    
inp = day_12.splitlines()

loc, ang = (0,0), 90

for inst in inp:
    loc, ang = move(loc, ang, inst)
    
print( sum(abs(d) for d in loc))


### Part 2 ###



def move_waypoint(loc, wp, inst):
    code, amount = inst[0], int(inst[1:])
    
    # Move ship
    if code == 'F':
        x = loc[0] +(wp[0]* amount)
        y = loc[1] + (wp[1] * amount) 
        loc = x, y
                
    # Move WP
    x, y = wp
    if code == 'N':
        wp = (x, y + amount)
    elif code == 'S':
        wp = (x, y - amount)
    elif code == 'E':
        wp = (x + amount, y)
    elif code == 'W':
        wp = (x - amount, y)

    # Rotate WP
    if code == 'L':
        code, amount = 'R', 360 - amount
    if code == 'R':
        if amount == 90:
            wp = (y, -x)
        elif amount == 180:
            wp = (-x, -y)
        elif amount == 270:
            wp = (-y, x)
        else:
            iojoijoi
    return loc, wp
        

loc, wp = (0,0), (10, 1)
for inst in inp:
    loc, wp = move_waypoint(loc, wp, inst)
    
print( sum(abs(d) for d in loc))