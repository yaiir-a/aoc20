from all_inputs import day_24
from _collections import defaultdict

t_inp = """sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew"""

t_inp_min = "nwwswee"


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


inp = t_inp
# inp = t_inp_min
inp = day_24



inp = parse(inp)

black_tiles = get_black(inp)
print(f'Part 1: {len(black_tiles)}')


def get_neighbors(tile):
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


def get_potentially_active(black_tiles):
    potentially_active = set()
    for tile in black_tiles:
        potentially_active.add(tile)
        for neighbor in get_neighbors(tile):
            potentially_active.add(neighbor)
    return potentially_active


def count_active_neighbors(tile):
    active_neighbors = 0
    for neighbor in get_neighbors(tile):
        if neighbor in black_tiles:
            active_neighbors += 1
    return active_neighbors


def cycle(black_tiles):
    potentially_active = get_potentially_active(black_tiles)
    new_active_tiles = set()
    for pa_tile in potentially_active:
        tile_active = pa_tile in black_tiles
        neighbors_active = count_active_neighbors(pa_tile)

        if tile_active and neighbors_active in (1, 2):
            new_active_tiles.add(pa_tile)
        elif not tile_active and neighbors_active == 2:
            new_active_tiles.add(pa_tile)
    return new_active_tiles



for _ in range(100):
    black_tiles = cycle(black_tiles)
    print(len(black_tiles))