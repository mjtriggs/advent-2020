# Day One
# Part Two
# Three numbers sum to 2020 from a list

import numpy as np

if __name__ == '__main__':

    # Load Data from Text File
    expenses = np.loadtxt("../data/day-1.txt", comments="#", delimiter=",", unpack=False)

    # loop through the values to find a possible answer
    # for a value i, calculate 2020 - i, then repeat the previous solution
    # if there are no duplicates, then i is not a possible solution

    for i in range(0, len(expenses)):
        # solution = []
        new_target = 2020 - expenses[i]
        new_combined = np.concatenate([expenses[i:], new_target - expenses[i:]])
        u, c = np.unique(new_combined, return_counts = True)
        
        if len(u[c > 1]) > 0:
            out = u[c > 1].prod() * expenses[i]
    
    print(int(out))