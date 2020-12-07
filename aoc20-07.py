from all_inputs import day_7


def parse_inp(bag_rules):
    parsed_bag_rules = {}
    for rule in bag_rules:
        rule = rule[:-1]
        rule = rule.replace('bags', '').replace('bag', '')
        r_colour, r_bags = rule.split(' contain ')
        r_bags = r_bags.split(', ')
        r_bags = [(int(bag[0]), bag[2:]) for bag in r_bags if bag !='no other ']
        parsed_bag_rules[r_colour] = r_bags
    return parsed_bag_rules

inp = day_7.splitlines()
inp = parse_inp(inp)

### Part 1 ###

def contains_shiny_gold(o_colour):
    if o_colour == 'shiny gold ':
        return True
    for n, i_colour  in inp[o_colour]:
        if contains_shiny_gold(i_colour):
            return True
    return False


part_1 = sum(contains_shiny_gold(outermost) for outermost in inp) - 1
part_1


### part 2 ###

bags = inp['shiny gold ']

for n, i_colour in bags:
    bags += n * inp[i_colour]

part_2 = sum((b[0]) for b in bags)
part_2