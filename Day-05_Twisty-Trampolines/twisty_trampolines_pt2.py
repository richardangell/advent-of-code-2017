import sys


def read_input(file):

    with open(file) as f:

        lines = f.readlines()

    for i in range(len(lines)):

        # remove \n
        lines[i] = int(lines[i][:(len(lines[i]) - 1)])

    return(lines)


def twisty_trampolines_pt2(input, verbose = False):

    n = len(input)

    verbose = bool(verbose)

    steps = 0

    pos = 0

    while pos <= n - 1:

        prev_pos = pos

        if verbose:

            print("step:", steps)

            print("input:", input)

            print("pos:", pos)

        # move that many steps in current position
        pos = pos + input[pos]

        if input[prev_pos] >= 3:

            input[prev_pos] = input[prev_pos] - 1

        else:
        
            # increment the value in the position moved from
            input[prev_pos] = input[prev_pos] + 1

        steps = steps + 1

    return(steps)


def escape_steps(file, verbose = False):

    input = read_input(file)

    steps = twisty_trampolines_pt2(input, verbose = verbose)

    print(steps)

    return(steps)


if __name__ == '__main__':

    if len(sys.argv[1:]) > 1:

        escape_steps(sys.argv[1], sys.argv[2])

    else:

        escape_steps(sys.argv[1])
