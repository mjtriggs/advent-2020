# Day 11
# Seating System

import numpy as np
from collections import Counter
import copy

def load_data(t):
    '''load in test or full data'''
    if t == 'test':
        fp = '../data/day-11-test.txt'
    elif t == 'full':
        fp = '../data/day-11.txt'
    else:
        raise Exception('Invalid File Input.')
    with open(fp, 'r') as infile:
        data = infile.read().split()
        data = [list(i) for i in data]
        return np.array(data)


def get_adjacent_seats(data, x, y):
    '''Get valid adjacent seats to a particular value'''
    # get possible combinations
    possible_combinations = [(i, j) for i in range(x - 1, x + 2) for j in range(y - 1, y + 2)]
    invalid_combinations = []
    # print(possible_combinations)

    m_x, m_y = data.shape
    m_x -= 1
    m_y -= 1

    for comb in possible_combinations:
        if comb[0] < 0 or comb[1] < 0 or comb[0] > m_x or comb[1] > m_y or comb == (x, y):
            invalid_combinations.append(comb)

    for comb in invalid_combinations:
        possible_combinations.remove(comb)

    return possible_combinations 

def change_seat(data, x, y):
    '''change seat by the part one rules'''
    adj = Counter([data[i] for i in get_adjacent_seats(data, x, y)])
    # print(adj)
    if data[x, y] == '.':
        return '.'
    elif data[x,y] == 'L' and adj['#'] == 0:
        return '#'
    elif data[x,y] == '#' and adj['#'] >= 4:
        return 'L'
    else:
        return data[x, y]

def change_all_seats(data):
    '''apply the change seat function to the full array'''
    x_lim, y_lim = data.shape
    arr = np.array([])
    for x in range(0, x_lim):
        for y in range(0, y_lim):
            arr = np.append(arr, change_seat(data, x, y))
    arr = arr.reshape(data.shape)
    return arr

def part_one():
    data = load_data('full')
    while True:
        old_grid = copy.deepcopy(data)
        data = change_all_seats(data)
        if np.array_equal(old_grid, data):
            return np.count_nonzero(data == '#')

def main():
    print('Part One:', part_one())

if __name__ == "__main__":
    main()