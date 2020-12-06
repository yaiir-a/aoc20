from all_inputs import day_6

inp = day_6.split('\n\n')

print(sum(len(set(group.replace('\n', ''))) for group in inp))


### Part 2 ###

from collections import Counter

total_answer = 0
for group in inp:
    group = Counter(group)
    num_people = group['\n'] + 1
    del group['\n']
    total_answer += sum(group[question] == num_people for question in group)

print(total_answer)

one_liner = sum(sum(Counter(group)[q] == Counter(group)['\n']+1 for q in Counter(group)) for group in inp)
print(one_liner)

