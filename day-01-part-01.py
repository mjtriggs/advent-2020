# Day One
# Part One
# Two numbers sum to 2020 from a list

import numpy as np

if __name__ == '__main__':

    # Load Data from Text File
    expenses = np.loadtxt("data/day-1.txt", comments="#", delimiter=",", unpack=False)

    # get possible paired values
    possible_pairs = 2020 - expenses

    # get values duplicated in both lists (i.e. the pair that sum to the target)
    a = np.concatenate([expenses, possible_pairs])
    u, c = np.unique(a, return_counts = True)

    # output the product
    out = u[c > 1].prod()
    print(int(out))