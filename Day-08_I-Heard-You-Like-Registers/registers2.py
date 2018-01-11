import sys


def read_input(file):
    """Read input file and return in a nested list.
    Each element of the list is a different line from file.
    Each line is split by spaces.

    Keyword arguments:
    file - name of file to read (str)
    """

    output = []

    with open(file) as f:

        lines = f.readlines()

    for i in range(len(lines)):

        # remove \n at end of line and split by spaces
        output = output + [lines[i][:(len(lines[i]) - 1)].split(" ")]

        assert len(output[i]) == 7, "line %r is not length 7" % i

        # convert increment value to integer
        output[i][2] = int(output[i][2])

        # convert condition value to integer
        output[i][6] = int(output[i][6])

    return(output)


def update_register_largest(input):
    """Creates and updates the register according to the rules in the input.
    Returns the largest value held by the register during update.

    Keyword arguments:
    input - output from read_input function giving update instructions (list)
    """

    register = {}

    largest_value = 0

    # loop through all input lines
    for i in range(len(input)):

        name = input[i][0]

        # check register value to change is in the register, add it if not
        if not name in register:

            register[name] = 0

        condition_name = input[i][4]

        # check register value in condition in the register, add it if not
        if not condition_name in register:

            register[condition_name] = 0

        condition = input[i][5]

        condition_value = input[i][6]

        condition_satisfied = False

        # check condition is safisfied
        if condition == "==":

            if register[condition_name] == condition_value:

                condition_satisfied = True

        elif condition == "!=":

            if register[condition_name] != condition_value:

                condition_satisfied = True

        elif condition == "<":

            if register[condition_name] < condition_value:

                condition_satisfied = True

        elif condition == ">":

            if register[condition_name] > condition_value:

                condition_satisfied = True

        elif condition == "<=":

            if register[condition_name] <= condition_value:

                condition_satisfied = True

        elif condition == ">=":

            if register[condition_name] >= condition_value:

                condition_satisfied = True

        else:

            print("condition", condition, "not recognised for input row", i)

        # if the condition is satisfied then update the registry value
        if condition_satisfied:

            update_direction = input[i][1]

            update_value = input[i][2]

            if update_direction == "inc":

                register[name] = register[name] + update_value

            elif update_direction == "dec":

                register[name] = register[name] - update_value

            else:

                print("update_direction",
                      update_direction,
                      "not recognised for input row",
                      i)

            if register[name] > largest_value:

                largest_value = register[name]

    return(largest_value)


def find_largest_value(file, verbose = False):
    """Reads the input file.
    Updates the register according to the instructions in the input.
    Finds and returns the largest value in the register at any point during
    the update.

    Keyword arguments:
    file - name of input file (str)
    verbose - not used (bool)
    """

    input = read_input(file)

    largest_value = update_register_largest(input)

    print(largest_value)

    return(largest_value)


if __name__ == '__main__':

    if len(sys.argv[1:]) > 1:

        find_largest_value(sys.argv[1], sys.argv[2])

    else:

        find_largest_value(sys.argv[1])
