valid_pass = 0
for password in r_inp_full:
    nums, letter, pwd = password.split(' ')
    n_min, n_max = [int(_) for _ in nums.split('-')]
    if n_min <= pwd.count(letter[0]) <= n_max:
        valid_pass += 1
        
valid_pass



# Part 2

valid_pass = 0
for password in r_inp_full:
    nums, letter, pwd = password.split(' ')
    n_1, n_2 = [int(_) for _ in nums.split('-')]
    if (pwd[n_1-1] == letter[0]) + (pwd[n_2-1] == letter[0]) == 1 : 
        valid_pass += 1
        
valid_pass