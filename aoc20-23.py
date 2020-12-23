

t_inp = [3, 8, 9, 1, 2, 5, 4, 6, 7]
day_23 = [3,6,2,9,8,1,7,5,4]
cups = t_inp
cups = day_23
current_cup_label = 3

# cups, current_cup_label = [8, 4, 1, 3, 6, 7, 9, 2, 5], 1

def destination_cup_label(remaining_cups, current_cup_label):
    searching_for = current_cup_label - 1
    while searching_for not in remaining_cups:
        searching_for = (searching_for - 1) % 10
    return searching_for


def move(cups, current_cup_label):

    moved = []
    for _ in range(3):
        current_cup_i = cups.index(current_cup_label)
        moved += [cups.pop((current_cup_i + 1) % len(cups))]

    dest_cup_label = destination_cup_label(cups, current_cup_label)
    destination_cup_index = (cups.index(dest_cup_label)+1) % 6
    moved
    for _ in range(3):
        cups.insert(destination_cup_index, moved.pop())
    return cups



for _ in range(1,101):
    # print(_, cups, current_cup_label)

    prev_dest = current_cup_label
    cups = move(cups, current_cup_label)
    new_index = cups.index(current_cup_label)
    current_cup_label = cups[(new_index + 1) % 9]


print(cups)
print()