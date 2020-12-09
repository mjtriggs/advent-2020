# Day 9
# Encoding Error

import numpy as np

def load_data(t):
    if t == 'test':
        fp = '../data/day-9-test.txt'
    elif t == 'full':
        fp = '../data/day-9.txt'
    else:
        raise Exception('Invalid File Input.')
    with open(fp, 'r') as f:
        lines = f.readlines()
        return np.array([int(line.strip()) for line in lines])

def check_sum_possible(preamble, value):
    '''calculates if any two numbers in the preamble can be added to make the 
    target value
    '''
    # taken from day 1
    counterpart = value - preamble
    a = np.concatenate([preamble, counterpart])
    u, c = np.unique(a, return_counts=True)
    if any(c > 1):
        return True
    else:
        return False

def find_first_invalid_value(dat, preamble_length):
    '''given a preamble length, find the first value that cannot be made as a 
    sum of two numbers in the preamble
    '''
    vec = np.arange(0, preamble_length)
    i = preamble_length

    while True:
        
        if check_sum_possible(dat[vec], int(dat[i])):
            i += 1
            vec += 1
        else:
            return dat[i]


def get_contiguous_sum(data, target):
    '''return a contiguous series of numbers in the data that add to the target'''
    i = 1

    while True:

        s = data[0:i].sum()
        if s == target:
            return True, data[0:i-1]
        elif s > target:
            return False, []
        else:
            i += 1

def find_max_min_contiguous_values(data, target):
    j = 0

    while True:
        r = get_contiguous_sum(data[j:], target)
        if r[0] == True:
            return min(r[1]) + max(r[1])
        else:
            j += 1

def part_one():
    data = load_data('full')
    return find_first_invalid_value(data, 25)

def part_two(target):
    data = load_data('full')
    return find_max_min_contiguous_values(data, target)

def main():
    pt_1 = part_one()
    print('Part One:', pt_1)
    pt_2 = part_two(pt_1)
    print('Part Two:', pt_2)

if __name__ == '__main__':
    main()