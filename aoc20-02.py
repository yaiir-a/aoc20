valid_pass = 0
for inp in r_inp_full:
    nums, letter, pwd = inp.split(' ')
    n_min, n_max = [int(_) for _ in nums.split('-')]
    if n_min <= pwd.count(letter[0]) <= n_max:
        valid_pass += 1
        
valid_pass



# Part 2

valid_pass = 0
for inp in r_inp_full:
    nums, letter, pwd = inp.split(' ')
    i_1, i_2 = (int(_)-1 for _ in nums.split('-'))
    if (pwd[i_1] == letter[0]) + (pwd[i_2] == letter[0]) == 1 : 
        valid_pass += 1
        
valid_pass