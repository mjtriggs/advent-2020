# Day Four
# Part Two
# Passport Validation

import pandas as pd
import re
import math

def list_to_dict(rlist):
    return dict(map(lambda s : s.split(':'), rlist))

def load_data(file):
    """load the test data file"""
    if file == "test":
        file_path = '../data/day-4-test-2.txt'
    elif file == "full":
        file_path = '../data/day-4.txt'
    else:
        raise Exception('load_data() must take the input argument "test" or "full"')

    # read file
    with open(file_path) as f:
        lines = f.read().split("\n\n")

    # turn into a dictionary, then a data frame
    f = lambda x: pd.DataFrame(list_to_dict(x.split()), index = [0])
    x = [f(x) for x in lines]
    return pd.concat(x, ignore_index=True, sort=True)

def check_byr(x):
    try:
        x = int(x)
        if (x >= 1920) & (x <= 2002):
            return True
        else:
            return False
    except:
        return False

def check_iyr(x):
    try:
        x = int(x)
        if (x >= 2010) & (x <= 2020):
            return True
        else:
            return False
    except:
        return False

def check_eyr(x):
    try:
        x = int(x)
        if (x >= 2020) & (x <= 2030):
            return True
        else:
            return False
    except:
        return False

def check_hgt(x):
    try:
        match = re.match(r"([0-9]+)([a-z]+)", x, re.I)
        if match:
            items = list(match.groups())
            items[0] = int(items[0])
            if items[1] == 'cm':
                if (items[0] >= 150) & (items[0] <= 193):
                    return True
                else:
                    return False
            elif items[1] == 'in':
                if (items[0] >= 59) & (items[0] <= 76):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    except:
        return False

def check_hcl(x):
    try:
        if math.isnan(x):
            return False
    except:
        pass    
    try:
        match = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', x)
        if match:
            return True
        else:
            return False
    except:
        return False

def check_ecl(x):
    if x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return True
    else:
        return False   

def check_pid(x):
    try:
        if pd.isnull(x):
            return False
        
        match = re.search(r'(^[0-9]{9}$)', x)
        if match:
            return True
        else:
            return False
    except:
        False

def check_valid_columns(data):
    """Run all validation functions against the dataframe and output if they pass or not"""

    # Drop the column not used in validation
    data = data.drop(['cid'], axis = 1)

    data['byr'] = data['byr'].apply(check_byr)
    data['iyr'] = data['iyr'].apply(check_iyr)
    data['eyr'] = data['eyr'].apply(check_eyr)
    data['hgt'] = data['hgt'].apply(check_hgt)
    data['hcl'] = data['hcl'].apply(check_hcl)
    data['ecl'] = data['ecl'].apply(check_ecl)
    data['pid'] = data['pid'].apply(check_pid)
    
    # Check if all values in a row are True
    return data.all(axis = 1)

def main():
    data = load_data('full')
    print("Valid Passports: ", sum(check_valid_columns(data)))

if __name__ == '__main__':
    main()
