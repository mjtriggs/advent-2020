# Day Five
# Part One
# Boarding Passes

import numpy as np

def load_data():
    with open('../data/day-5.txt', 'r') as infile:
        data = infile.read().split()
        return data

def to_binary_row(letter):
    if letter == 'F':
        return '0'
    else:
        return '1'

def to_binary_col(letter):
    if letter == 'L':
        return '0'
    else:
        return '1'

def get_row_value(input_string):
    return int(''.join([to_binary_row(x) for x in input_string]), 2)

def get_col_value(input_string):
    return int(''.join([to_binary_col(x) for x in input_string]), 2)

def get_seat(input):

    # get row
    row = get_row_value(input[0:7])

    # get seat number
    seat_no = get_col_value(input[7:])

    # output as tuple
    return row, seat_no

def get_seat_id(input):

    row, seat_no = get_seat(input)
    return row * 8 + seat_no

def main():
    data = load_data()
    boarding_passes = [int(get_seat_id(x)) for x in data]
    print('Maximum Seat ID: ', max(boarding_passes))
    print('Missing Seat ID: ', int(np.setdiff1d(list(np.arange(start = min(boarding_passes), stop = max(boarding_passes) + 1)), boarding_passes)))

if __name__ == '__main__':
    main()