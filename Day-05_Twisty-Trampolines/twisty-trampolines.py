import sys


def read_input(file):

    with open(file) as f:

        lines = f.readlines()

    for i in range(len(lines)):

        # remove \n 
        lines[i] = lines[i][:(len(lines[i]) - 1)]

    return(lines)


def twisty_trampolines(input):




if __name__ == '__main__':

    valid_passphrase(sys.argv[1])
