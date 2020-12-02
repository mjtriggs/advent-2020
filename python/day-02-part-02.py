# Day Two
# Part One
# Password Validation

import importlib
part_one = importlib.import_module('day-02-part-01') 

def check_valid_password_part_two(s):
    """Check if passcode is value"""

    # get the location that the passwords have to match
    first_location, second_location = tuple(map(int, s[0].split("-")))

    # get the letter to compare
    letter = s[1][0]

    # do the comparison - "^" represents XOR
    if (s[2][first_location - 1] == letter) ^ (s[2][second_location - 1] == letter):
        return True
    else:
        return False


if __name__ == '__main__':
    
    # load data
    data = part_one.load_data() 

    # sum the logical vector
    print("Valid Passwords: ", sum(list(map(check_valid_password_part_two, data))))