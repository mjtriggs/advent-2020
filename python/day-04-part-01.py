# Day Four
# Part One
# Passport Validation

import pandas as pd

def list_to_dict(rlist):
    return dict(map(lambda s : s.split(':'), rlist))

def load_data(file):
    """load the test data file"""
    if file == "test":
        file_path = '../data/day-4-test.txt'
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

def check_valid_columns(data, col_names):
    data = data[col_names]
    return len(data) - len(data[data.isnull().any(axis=1)])

def main():
    data = load_data('full')
    print("Valid Passports: ", check_valid_columns(data, col_names = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']))

if __name__ == '__main__':
    main()
