# Day Two
# Part One
# Password Validation

def get_number_of_occurances(password, value):
    """Count the number of letters of a given value in a longer string"""
    return password.count(value)

def check_valid_password_part_one(s):
    """Check if passcode is value"""
    freq = get_number_of_occurances(s[2], s[1][0])
    min_valid, max_valid = tuple(map(int, s[0].split("-")))
    if (freq >= min_valid) & (freq <= max_valid):
        return True
    else:
        return False

def load_data():
    """Load data file for day two - not to be reused outside this day"""
    with open('../data/day-2.txt', 'r') as infile:
        data = infile.readlines()
        data = [i.split() for i in data]
        return data


if __name__ == '__main__':
    
    # load data
    data = load_data() 

    # sum the logical vector
    print("Valid Passwords: ", sum(list(map(check_valid_password_part_one, data))))