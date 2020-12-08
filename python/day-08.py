# Day 08
# Handheld Halting

def load_data(dat = 'full'):
    if dat == 'full':
        file_path = '../data/day-8.txt'
    elif dat == 'test':
        file_path = '../data/day-8-test.txt'
    else:
        raise Exception('Enter full or test for the file path.')
    with open(file_path, 'r') as f:
        lines = f.read().splitlines()
        return lines

def run_program(prog):
    # initialise values
    acc = 0
    start_loc = 0
    idx = start_loc
    idx_list = [idx]

    while True:
        command = prog[idx]
        instruction, value = command.split()
        if instruction == "nop":
            idx += 1
        if instruction == "acc":
            acc += int(value)
            idx += 1
        if instruction == "jmp":
            idx += int(value)
        
        if idx in idx_list:
            return acc
        if idx >= len(prog):
            # added this in for part two
            raise Exception('Out of bounds. Final value of accumulator: {}'.format(acc))
        else:
            idx_list.append(idx)

def change_prog(prog, idx):
    '''Change the program per instructions for one line'''
    new_prog = prog.copy()
    if prog[idx].split()[0] == 'nop':
        new_prog[idx] = 'jmp ' + prog[idx].split()[1]
    elif prog[idx].split()[0] == 'jmp':
        new_prog[idx] = 'nop ' + prog[idx].split()[1]
    else:
        pass
    return new_prog

def part_one(prog):
    val = run_program(prog)
    print('Part One:', val)

def part_two(program):
    '''change each line in turn and error out when the program successfully completes'''
    # not the best way of handling this, but meh
    for i in range(len(program)):
        tmp_prog = change_prog(program, i)
        run_program(tmp_prog)

def main():
    # Note: Part Two returns the answer in an exception message.
    data = load_data('full')
    part_one(data)
    part_two(data)

if __name__ == '__main__':
    main()