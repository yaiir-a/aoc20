from all_inputs import input_4

inp = input_4.replace('\n\n', '\t').replace('\n', ' ').split('\t')

valid = 0
for passport in inp:
    all_data = passport.count(':') == 8
    missing_country_only = (passport.count(':') == 7) and ('cid' not in passport)
    if all_data or missing_country_only:
        valid += 1
        
valid

### Part 2 ###


import re

inp = input_4.replace('\n\n', '\t').replace('\n', ' ').split('\t')

valid = 0

def valid_height(v):
    unit = v[-2:]
    height = int(v[:-2])
    if unit == 'cm':
        if 150<= height <= 193:
            return True
    if unit == 'in':
        if 59<=height<=76:
            return True
    

for passport in inp:
    all_data = passport.count(':') == 8
    missing_country_only = (passport.count(':') == 7) and ('cid' not in passport)
    if not (all_data or missing_country_only):
        continue
        
    pp = dict([k_v.split(':') for k_v in passport.split(' ')])
    
    try:
        if not 1920 <= int(pp['byr']) <= 2002:
            continue
        
        if not 2010 <=int(pp['iyr']) <= 2020:
            continue
        
        if not 2020 <=int(pp['eyr']) <= 2030:
            continue

        if not valid_height(pp['hgt']):
            continue
            
        if not re.search('^#[a-f0-9]{6}$', pp['hcl']):
            continue
            
        if not pp['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            continue
        
        if not re.search('^[0-9]{9}$', pp['pid']):
            continue
        
        valid += 1 
    
    except:
        continue
    
valid