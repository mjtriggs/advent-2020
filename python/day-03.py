# Day Three
# Parts One and Two
# Crashing a Toboggan into Trees

import numpy as np

def load_data():
    with open('../data/day-3.txt', 'r') as infile:
        data = infile.read().splitlines()
        return np.array(data)

def count_trees(data, start_x = 0, start_y = 0, down_size = 1, right_size = 3):
    """Specifying a starting position and step size, this function will 
    count how many trees are hit by the toboggan.
    """
    # stop condition: when the current y value > the end
    end = len(data) - 1

    # total tree indicator
    total_trees = 0

    # Define x and y locations
    current_x = start_x
    current_y = start_y

    # Do this in a for loop
    while current_y < end:
        current_x += right_size
        current_y += down_size

        # adjust y for repeating pattern
        current_x = current_x % len(data[0])

        # increment count if we crash into a tree
        if data[current_y][current_x] == '#':
            total_trees += 1

    return total_trees

if __name__ == '__main__':
    
    data = load_data()
    
    pt_1 = count_trees(data, right_size=3, down_size=1)
    print('Answer to Part One: ', pt_1)

    pt_2 = count_trees(data, right_size=1, down_size=1) * \
        count_trees(data, right_size=3, down_size=1) * \
        count_trees(data, right_size=5, down_size=1) * \
        count_trees(data, right_size=7, down_size=1) * \
        count_trees(data, right_size=1, down_size=2)
    print('Answer to Part Two: ', pt_2)