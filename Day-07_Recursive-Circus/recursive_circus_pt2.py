import sys


def read_input(file):
    """ Function to read the input file and output a dict with named
    elements being dicts of structure {"weight": int, "children": list}
    where weight is the weight of the program and children is a list
    of it's children. If the program has not children then the list is
    empty. """

    file_dict = dict()

    with open(file) as f:

        lines = f.readlines()

    for i in range(len(lines)):

        split = lines[i][:(len(lines[i]) - 1)].split(" ")

        name = split[0]

        weight = int(split[1].replace("(", "").replace(")", ""))

        if len(split) > 2:

            children = [x.replace(",", "") for x in split[3:]]

        else:

            children = []

        file_dict[name] = {"weight": weight, "children": children}

    file_dict_keys = list(file_dict.keys())

    for i in range(len(file_dict_keys)):

        children = file_dict[file_dict_keys[i]]["children"]

        n_children = len(children)

        if n_children > 0:

            for j in range(n_children):

                file_dict[children[j]]["parent"] = file_dict_keys[i]

    return(file_dict)


def print_dict(dict):
    """ Function to print all elements of the input dict. """

    dict_keys = list(dict.keys())

    for i in range(len(dict_keys)):

        print(dict_keys[i], ":", dict[dict_keys[i]])


def get_cumulative_weights(dict, prog, verbose = False):
    """ Function to traverse tree struture of dict and add get_cumulative_weights
    element to each dict. """

    if verbose:

        print("get_cumulative_weights called from", prog, ":", dict[prog])

    if len(dict[prog]["children"]) == 0:

        dict[prog]["cumulative_weight"] = dict[prog]["weight"]

    else:

        dict[prog]["cumulative_weight"] = dict[prog]["weight"] + \
            sum([get_cumulative_weights(dict, x) for x in dict[prog]["children"]])

    return(dict[prog]["cumulative_weight"])


def find_unbalanced_children(dict, prog, verbose):

    if len(dict[prog]["children"]) > 0:

        child_weights = [dict[x]["cumulative_weight"] for x in dict[prog]["children"]]

        # if all child weights are not equal
        if child_weights.count(child_weights[0]) != len(child_weights):

            # return
            return(dict[prog])

        else:

            for i in range(len(dict[prog]["children"])):

                find_unbalanced_children(dict, dict[prog]["children"][i], verbose)

def are_children_unbalanced(dict, prog):

    if len(dict[prog]["children"]) > 0:

        child_weights = [dict[x]["cumulative_weight"] for x in dict[prog]["children"]]

        # if all child weights are not equal
        if child_weights.count(child_weights[0]) != len(child_weights):

            return(False)

        else:

            return(True)

    else:

        return(True)


def unbalance_start(dict, prog, verbose):

    if are_children_unbalanced(dict, prog):

        grandchildren_unbalanced = [are_children_unbalanced(dict, x) for x in dict[prog]["children"]]

        if any(grandchildren_unbalanced):

            unbalanced_grandchild = grandchildren_unbalanced.index(True)

            unbalance_start(dict, , verbose)

        # if none of the grandchildren are unbalanced find the child where the unbalance starts
        else:




    else:






def find_correct_weight(file, verbose = False):

    dict = read_input(file)

    verbose = bool(verbose)

    dict_keys = list(dict.keys())

    if verbose:

        print_dict(dict)

    for i in range(len(dict_keys)):

        if not "parent" in dict[dict_keys[i]]:

            bottom_program = dict_keys[i]

            break

    total_weight = get_cumulative_weights(dict, bottom_program, verbose)

    if verbose:

        print_dict(dict)

    # find the program which has unbalanced children i.e. all children cumulative weights are not equal
    # we actually don't want to find the progam with unbalanced children we want to find the first
    #   program with balanced children - because everything above this will be unbalanced hence
    #   this is where the unbalancing starts
    #prog_with_unbalanced_children = find_unbalanced_children(dict, bottom_program, verbose)

    # find the first program with balanced children
    prog_with_balanced_children = find_last_unbalanced_children(dict, bottom_program, verbose)

    if verbose:

        print("prog_with_balanced_children:", prog_with_balanced_children)

    # find the cumulative weights for the programs children
    child_cum_weights = [dict[x]["cumulative_weight"] for x in prog_with_balanced_children["children"]]

    child_cum_weights_set = set(child_cum_weights)

    child_cum_weights_count = []

    # find which is the odd one out weight and the correct weight value
    for i in child_cum_weights_set:

        if child_cum_weights.count(i) == 1:

            incorrect_weight = i

        else:

            correct_weight = i

    # find the index of the incorrect weight
    for i in range(len(child_cum_weights)):

        if child_cum_weights[i] == incorrect_weight:

            incorrect_weight_index = i

            break

    required_weight_difference = correct_weight - incorrect_weight

    # add the required change in weight (can be -ve) onto the odd one out child
    new_weight_for_prog = required_weight_difference + \
        dict[prog_with_balanced_children["children"][incorrect_weight_index]]["weight"]

    if verbose:

        print("bottom_program:", dict[bottom_program])

        print("prog_with_unbalanced_children:", prog_with_balanced_children)

        print("child_cum_weights:", child_cum_weights)

        print("incorrect_weight:", incorrect_weight)

        print("correct_weight:", correct_weight)

        print("child needing rebalancing:", dict[prog_with_unbalanced_children["children"][incorrect_weight_index]])

        print("required_weight_difference:", required_weight_difference)

        print("new_weight_for_prog:", new_weight_for_prog)

    #print(dict['onnfacs'])

    print(new_weight_for_prog)

    return(new_weight_for_prog)


if __name__ == '__main__':

    if len(sys.argv[1:]) > 1:

        find_correct_weight(sys.argv[1], sys.argv[2])

    else:

        find_correct_weight(sys.argv[1])
