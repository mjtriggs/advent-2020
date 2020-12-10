# Day 10

import numpy as np
import collections

def load_data(t):
    if t == 'test':
        fp = '../data/day-10-test.txt'
    elif t == 'full':
        fp = '../data/day-10.txt'
    else:
        raise Exception('Invalid File Input.')
    with open(fp, 'r') as f:
        lines = f.readlines()
        return np.array([int(line.strip()) for line in lines])

def get_jolt_differences(dat):
    # Add 0 and max + 3 for start and final value
    dat = np.append(dat, [0, max(dat) + 3])
    dat.sort()
    diffs = np.ediff1d(dat)
    c = collections.Counter(diffs)
    return {1:c[1], 3:c[3]}


def part_one():
    data = load_data('full')
    r = get_jolt_differences(data)
    print('Part One:', r[1] * r[3])

def part_two():
    data = load_data('full')
    data.sort()
    possibilities = collections.defaultdict(int)
    # intialise with 1 to represent the final possible step
    possibilities[0] = 1

    for val in data:
        possibilities[val] = possibilities[val - 1] + possibilities[val - 2] + possibilities[val - 3] 
    
    print('Part Two:', possibilities[max(data)])

if __name__ == "__main__":
    part_one()
    part_two()