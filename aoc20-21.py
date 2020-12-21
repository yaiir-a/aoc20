from itertools import product
from collections import defaultdict
from all_inputs import day_21

def parse(inp):
    inp = inp.replace('(', '').replace(')','').splitlines()
    
    out = []
    for f, food in enumerate(inp):
        ingredients, allergens = food.split(' contains ')
        ingredients = set(ingredients.split(' '))
        allergens = set(allergens.split(', '))
        out += [(f, ingredients, allergens)]
    return out

inp = parse(t_inp)

inp = parse(day_21)



allergens = defaultdict(set)
ingredients = defaultdict(set)

for f, ings, als in inp:
    for ing, al in product(ings, als):
        allergens[al].add(f)
        ingredients[ing].add(f)


safe = []
for ing in ingredients:
    if not any(not allergens[al] - ingredients[ing] for al in allergens):
        safe += [ing]

safe = set(safe)

print(sum([len(ingredients[ing]) for ing in safe]))

### Part 2 ###

potentials = []
for f, ings, als in inp:
    potentials+= [(als, ings - safe)]

for s in safe:
    del ingredients[s]




foo = defaultdict(set)

for al in allergens:
    for ing in ingredients:
        if not allergens[al] - ingredients[ing]:
            foo[al].add(ing)

foo = defaultdict(set)

for al in allergens:
    for ing in ingredients:
        if not allergens[al] - ingredients[ing]:
            foo[al].add(ing)

final = []
while len(final) < len(foo):
    for al, ings in foo.items():
        if len(ings) == 1:
            final += [(al, list(ings)[0])]
            for al in foo:
                foo[al] = foo[al] - ings
            
s = sorted(final, key=lambda x: x[0])
','.join([i for a, i in s])