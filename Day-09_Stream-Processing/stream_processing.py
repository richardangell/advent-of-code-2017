import sys


def read_input(file):
    """Read input file and return it in a single str.

    Keyword arguments:
    file - name of file to read (str)
    """

    output = []

    with open(file) as f:

        lines = f.readlines()

    # remove \n at line end
    lines = lines[0][:(len(lines[0]) - 1)]

    return(lines)


def remove_garbage(input, verbose = False):

    garbage_indices = []

    i = 0

    in_garbage = False

    garbage_start_index = 0

    garbage_end_index = 0

    while i < len(input):

        # if the ith character is ! then skip the next character
        if input[i] == "!":

            i += 1

            continue

        elif input[i] == "<":

            if not in_garbage:

                in_garbage = True

                garbage_start_index = i

        elif input[i] == ">":

            if in_garbage:

                in_garbage = False

                garbage_end_index = i

                garbage_indices = garbage_indices + [x for x in range(garbage_start_index,
                                                                      garbage_end_index + 1)]

        # increment counter
        i += 1

    print(garbage_indices)




def total_group_score(file, verbose = False):
    """Reads the input file.

    Keyword arguments:
    file - name of input file (str)
    verbose - not used (bool)
    """

    input = read_input(file)

    for i in range(len(input)):

        #if input[i] == ",":

        #elif input[i] == "{":

        #elif input[i] == "}":

        #elif input[i] == "<":

        #elif input[i] == ">":

        #elif input[i] == "!":

        a = 1




if __name__ == '__main__':

    if len(sys.argv[1:]) > 1:

        remove_garbage(sys.argv[1], sys.argv[2])

    else:

        remove_garbage(sys.argv[1])
