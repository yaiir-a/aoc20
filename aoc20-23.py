
from datetime import datetime


#
# t_inp = [3, 8, 9, 1, 2, 5, 4, 6, 7]
# day_23 = [3,6,2,9,8,1,7,5,4]
# cups = t_inp
# # # cups = day_23
# # current_cup_label = 3
#
# # cups, current_cup_label = [8, 4, 1, 3, 6, 7, 9, 2, 5], 1
#
#
# def destination_cup_label(remaining_cups, current_cup_label):
#     searching_for = current_cup_label - 1
#     while searching_for not in remaining_cups:
#         searching_for = (searching_for - 1) % 10
#     return searching_for
#
#
# def move(cups, current_cup_label):
#
#     moved = []
#     for _ in range(3):
#         current_cup_i = cups.index(current_cup_label)
#         moved += [cups.pop((current_cup_i + 1) % len(cups))]
#
#     dest_cup_label = destination_cup_label(cups, current_cup_label)
#     destination_cup_index = (cups.index(dest_cup_label)+1) % 6
#     moved
#     for _ in range(3):
#         cups.insert(destination_cup_index, moved.pop())
#     return cups
#
#
# from datetime import datetime
#
# start = datetime.now()
#
# #
# # for _ in range(1,11):
# #     # print(_, cups, current_cup_label)
# #     if _ % 1000 == 0:
# #         time_taken = datetime.now() - start
# #         print(_, time_taken, 'remaining time- ', time_taken/_ * 10000000 - time_taken)
# #     prev_dest = current_cup_label
# #     cups = move(cups, current_cup_label)
# #     new_index = cups.index(current_cup_label)
# #     current_cup_label = cups[(new_index + 1) % 9]
#
#
# # print(cups)
# print('DONE?')
# print()
#
# ### Part 2 ###
#
#
#
#
#
#
# t_inp = "389125467"
#
#
# class Cup(object):
#     def __init__(self, label, prev=None, next=None):
#         self.label = label
#         self.prev = prev
#         self.next = next
#
#
# def parse(inp):
#     inp = [int(n) for n in inp]
#
#     prev_cup = Cup(3)
#     cups = {
#         3: prev_cup
#     }
#     for n in inp[1:]:
#         cups[n] = Cup(n, prev_cup)
#     return cups
#
#
#

#
# inp = t_inp
#
# cups = parse(inp)
#
#
#
#
# current_cup = 3
#
#


# a = _3_| 8, '9', 1 | 2
#
#
# destination_cup = current_cup - 1
#
#
# def get_moved_cups(current_cup):
#     moved = []
#     starting_cup = current_cup
#     for _ in range(3):
#         starting_cup = inp[starting_cup][1]
#         moved += [starting_cup]
#     return moved
#
#
# inp = t_inp
# starting_cup = 3
#
# moved_cups = get_moved_cups(starting_cup)
#
#
# print()


### Dict attempt ###

#
# inp = {
#     1: (9, 2),
#     2: (1, 5),
#     3: (7, 8),
#     4: (5, 6),
#     5: (2, 4),
#     6: (4, 7),
#     7: (6, 3),
#     8: (3, 9),
#     9: (8, 1)
# }
#
#
#
#
# 362981754
#
# day_23 = {
#     1: (8, 7),
#     2: (6, 9),
#     3: (4, 6),
#     4: (5, 3),
#     5: (7, 4),
#     6: (3, 2),
#     7: (1, 5),
#     8: (9, 1),
#     9: (2, 8)
#
# }
# #
#
#
# t_inp_full = {
#     1: (9, 2),
#     2: (1, 5),
#     3: (1000000, 8),
#     4: (5, 6),
#     5: (2, 4),
#     6: (4, 7),
#     7: (6, 10),
#     8: (3, 9),
#     9: (8, 1)
# }
#
#
# inp = t_inp_full
# for i in range(10, 1000001):
#     inp[i] = i-1, (i+1)%1000001
#
# inp[10] = (7, 11)
# inp[1000000] = (999999, 3)



day_23_full = {
    1: (8, 7),
    2: (6, 9),
    3: (1000000, 6),
    4: (5, 10),
    5: (7, 4),
    6: (3, 2),
    7: (1, 5),
    8: (9, 1),
    9: (2, 8)
}

inp = day_23_full
for i in range(10, 1000001):
    inp[i] = i-1, (i+1) % 1000001

inp[10] = (4, 11)
inp[1000000] = (999999, 3)


def get_destination_cup(curr_cup):
    dest_cup = current_cup - 1
    while dest_cup in removed or not dest_cup:
        dest_cup = (dest_cup - 1) % (num_cups + 1)
    return dest_cup


def remove_three_cups(curr_cup):
    start_cup = curr_cup
    next_cups = []
    next_cup = curr_cup
    for _ in range(4):
        next_cup = inp[next_cup][1]
        next_cups += [next_cup]
    inp[start_cup] = inp[start_cup][0], next_cup
    inp[next_cup] = start_cup, inp[next_cup][1]
    return next_cups[:-1]


def insert_three_cups(dest_cup, removed):
    global inp
    a, b, c = removed
    o_p, o_n = inp[dest_cup]

    inp[dest_cup] = (o_p, a)
    inp[a] = (dest_cup, b)
    inp[c] = (b, o_n)
    inp[o_n] = (c, inp[o_n][1])


# [3, 2, (8,_9_,1), 5, 4, 6, 7]



def pprint():
    global current_cup
    curr_cup = current_cup
    out = []
    while curr_cup not in out:
        out += [curr_cup]
        curr_cup = inp[curr_cup][1]
    print(out)


print('lol')


current_cup = 3
num_cups = len(inp)



start = datetime.now()
for _ in range(10000000):
    removed = remove_three_cups(current_cup)
    dest_cup = get_destination_cup(current_cup)
    insert_three_cups(dest_cup, removed)
    current_cup = inp[current_cup][1]

end = datetime.now()
print('DONE')
print(end - start)

ns = []
n = 1
for i in range(2):
    n = inp[n][1]
    print(n)
    ns += [n]


#### Unrolled ####


print('Starting unrolled')

day_23_full = {
    1: (8, 7),
    2: (6, 9),
    3: (1000000, 6),
    4: (5, 10),
    5: (7, 4),
    6: (3, 2),
    7: (1, 5),
    8: (9, 1),
    9: (2, 8)
}

inp = day_23_full
for i in range(10, 1000001):
    inp[i] = i - 1, (i + 1) % 1000001

inp[10] = (4, 11)
inp[1000000] = (999999, 3)






# [3, 2, (8,_9_,1), 5, 4, 6, 7]

print('lol')

current_cup = 3
num_cups = len(inp)

start = datetime.now()
for _ in range(10000000):

    start_cup = current_cup
    next_cups = []
    next_cup = current_cup
    for _ in range(4):
        next_cup = inp[next_cup][1]
        next_cups += [next_cup]
    inp[start_cup] = inp[start_cup][0], next_cup
    inp[next_cup] = start_cup, inp[next_cup][1]
    a, b, c = next_cups[:-1]

    dest_cup = current_cup - 1
    while dest_cup in removed or not dest_cup:
        dest_cup = (dest_cup - 1) % (num_cups + 1)

    o_p, o_n = inp[dest_cup]

    inp[dest_cup] = (o_p, a)
    inp[a] = (dest_cup, b)
    inp[c] = (b, o_n)
    inp[o_n] = (c, inp[o_n][1])
    current_cup = inp[current_cup][1]

end = datetime.now()
print('DONE')
print(end - start)

ns = []
n = 1
for i in range(2):
    n = inp[n][1]
    print(n)
    ns += [n]
