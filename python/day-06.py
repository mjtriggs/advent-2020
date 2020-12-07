# Day 06
# Custom Customs
# Part One and Two
# Note: I couldn't do part two - this is a solution copied from https://dev.to/qviper/advent-of-code-2020-python-solution-day-6-248d

from collections import Counter
import numpy as np

def load_test_data():
    file_path = '../data/day-6-test.txt'
    with open(file_path) as f:
        lines = f.read().split("\n\n")
        return lines

def load_data():
    file_path = '../data/day-6.txt'
    with open(file_path) as f:
        lines = f.read().split("\n\n")
        return lines

def get_unique_chars(lines):
    return [len(set(x.replace('\n', ''))) for x in lines]

def part_one():
    data = load_data()
    print('Solution 1:', sum(get_unique_chars(data)))

def part_two():
    # load data differently - list of lists
    with open("../data/day-6.txt", "r") as fp:
        lines=fp.readlines()

    groups = []
    group = []
    for question in lines:
        if question!="\n":
            # if it's not a new line, then add it to the current group
            group.append(question.split("\n")[0])
        else:
            # for a new line, start a new group and update the list of groups
            groups.append(group)
            group=[]
    groups.append(group)

    total = 0
    for group in groups:
        group_size = len(group)

        # make single list of enitire group and count occurence
        counts = Counter("".join(group))

        counts = Counter(list(counts.values()))[group_size]
        total+=counts
    print(f"Solution 2:", total)


def main():
    part_one()
    part_two()

if __name__ == '__main__':
    main()