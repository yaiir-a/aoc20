from math import sqrt
from itertools import product
from all_inputs import day_20

def parse(r_inp):
    tiles = []
    for _ in r_inp.split('\n\n'):
        tile = _.splitlines()
        tid, tile = tile[0], tile[1:]
        tid = tid[5:-1]
        t = Tile(tid, tile)
        tiles += [Tile(tid, tile)]
    return tiles


class Tile(object):
    def __init__(self, id_, tile):
        self.id_ = int(id_)
        self.top = list(tile[0])
        self.right = [r[-1] for r in tile]
        self.bottom = list(tile[-1][::-1])
        self.left = [r[0] for r in tile[::-1]]
        self.tile = tile
        
    def __str__(self):
        return '\n'.join(self.tile)
    
    def __repr__(self):
        return self.__str__()
    
    def __iter__(self):
        self.iter_i = 0
        return self
    
    def __next__(self):
        i = self.iter_i
        if i == 0:
            out = self.top
        elif i == 1:
            out = self.right
        elif i == 2:
            out = self.bottom
        elif i == 3:
            out = self.left
        else:
            raise StopIteration
        self.iter_i +=1
        return out
        
    def flip(self):
        self.top, self.bottom = self.bottom[::-1], self.top[::-1]
        self.right, self.left = self.right[::-1], self.left[::-1]     
        
        self.tile = self.tile[::-1]
        return self
        
    def mirror(self):
        self.right, self.left = self.left[::-1], self.right[::-1]
        self.top, self.bottom = self.top[::-1], self.bottom[::-1]
        
        self.tile = [r[::-1] for r in self.tile]
        return self
        
    def rotate(self):
        self.top, self.right,self.bottom, self.left = self.left, self.top, self.right, self.bottom
        self.tile = [''.join(r) for r in zip(*reversed(self.tile))]
        return self
            
class Board(object):
    def __init__(self, tiles, width):
        self.tiles_list = tiles
        self.width = width
        self.tiles = {t.id_: t for t in tiles}
        
    def get_potential_matches(self):
        self.potential_matches = {}
        for id_f in self.tiles:
            self.potential_matches[id_f] = []
            for id_l in self.tiles:
                if id_f == id_l:
                    continue
                if self.potential_match(self.tiles[id_f], self.tiles[id_l]):
                    self.potential_matches[id_f] += [id_l]
            if len(self.potential_matches[id_f]) == 2:
                self.corner = id_f
        return self
    
    def potential_match(self, fixed, loose):
        for f, l in product(fixed, loose):
            if f == l:
                return True
        for f, l in product(fixed, loose.mirror()):
            if f == l:
                return True
        return False
    
    def build_grid(self):
        pms = self.potential_matches
        next_id = pms[self.corner][0]
        used_ids = set((self.corner, next_id))
        grid = []
        row = [self.corner, next_id]
        for c in range(self.width - 2):
            for pm in pms[next_id]:
                if pm not in used_ids:  # to not choose one which has been chosen before
                    if len(pms[pm]) < 4:  # to only get edges+ corner, not the row below
                        used_ids.add(pm)
                        row += [pm]
                        next_id = pm
        grid += [row]
        for r in range(self.width-1):  # Repeat for the remaining rows
            previous_row = grid[r]
            row = []
            for elem in previous_row:  # look at the row above and find the one not matched
                new_elem = [e for e in pms[elem] if e not in used_ids][0]
                used_ids.add(new_elem)
                row += [new_elem]
            grid += [row]
        self.grid = grid
        return self
    
    def stitch_grid(self):
        self.build_grid()
        corner = self.grid[0][0]

        # Hard coded :shrug:
        self.tiles[corner].mirror()
        self.tiles[self.grid[0][1]].rotate().rotate()
        # Assuming each potential match can only stitch on one way..
        
        for i in range(2, self.width):
            prev_tile = self.tiles[self.grid[0][i-1]]
            tile = self.tiles[self.grid[0][i]]
            self.orient_left(prev_tile, tile)
            
        for i in range(1, self.width):
            for j in range(self.width):
                prev_tile = self.tiles[self.grid[i-1][j]]
                tile = self.tiles[self.grid[i][j]]
                self.orient_bottom(prev_tile, tile)
                
        out = ''
        for tile_row in b.grid:
            for tile_row_line in zip(*[b.tiles[tile_id].tile[1:-1] for tile_id in tile_row]):  # removing top and bottom of each tile 
                tile_row_line = [trl[1:-1] for trl in tile_row_line]  # removing ends of each tile row line
                out += ''.join(tile_row_line) + '\n'
        self.stitched_grid = out.splitlines()
        return self.stitched_grid


            
    def orient_left(self, fixed, loose):
        for _ in range(4):
            if fixed.right == loose.left[::-1]:
                return 
            loose.flip()
            if fixed.right == loose.left[::-1]:
                return 
            loose.flip()
            loose.rotate()
        fuck
        
    def orient_bottom(self, fixed, loose):
        for _ in range(4):
            if fixed.bottom == loose.top[::-1]:
                return 
            loose.flip()
            if fixed.bottom == loose.top[::-1]:
                return 
            loose.flip()
            loose.rotate()
        fuck    

tiles = parse(day_20)
b = Board(tiles, 12)
b.get_potential_matches()
b.build_grid()
b.stitch_grid()


for item in row
    for all the potential matches that arent in used ids
         if also item matches row above
             add item to row. this is the next item



a = """                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """.splitlines()

coords =[]
for i, row in enumerate(a):
    for j, char in enumerate(row):
        if char == '#':
            coords += [(i, j)]
            

def rotate(grid):
      return [''.join(r) for r in zip(*reversed(grid))] 
    
def flip(grid):
    return grid[::-1]


def count_dragons(img):
    count = 0
    for y, row in enumerate(img[:-2]):
        for x, pixel in enumerate(row[:-19]):
    #         print(i, j)
            start_pixel = y, x
            if all(img[y+y_o][x+x_o]=='#' for y_o, x_o in coords):
                count += 1
    return count

                

img = b.stitched_grid
for _ in range(4):
    print(count_dragons(img))
    img = flip(img)
    print(count_dragons(img))
    img = flip(img)
    img = rotate(img)


    
part_2 = ''.join(b.stitched_grid).count('#') - (21 * 15)