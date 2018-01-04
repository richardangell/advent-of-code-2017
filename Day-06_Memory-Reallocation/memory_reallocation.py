import sys


def read_input(file):

    with open(file) as f:

        lines = f.readlines()

    for i in range(len(lines)):

        lines[i] = lines[i][:(len(lines[i]) - 1)].split("\t")

        for j in range(len(lines[i])):

            lines[i][j] = int(lines[i][j])

    return(lines)


def reallocate_memory(config, verbose = False):

    # have to make sure to copy the input list so we don't change the original
    config_reallocated = config[:]

    if verbose:

        print("reallocate_memory call:", config)

    l = len(config)

    m = max(config)

    # gives all indices
    #max_indices = [i for i, j in enumerate(config) if j == m]

    max_index = config.index(m)

    config_reallocated[max_index] = 0

    fill_index = max_index + 1

    if fill_index > (l - 1):

        fill_index = 0

    for i in range(m):

        config_reallocated[fill_index] = config_reallocated[fill_index] + 1

        fill_index = fill_index + 1

        if fill_index > (l - 1):

            fill_index = 0

    if verbose:

        print("reallocate_memory output:", config_reallocated)

    return(config_reallocated)



def count_memory_reallocations(file, verbose = False):

    redistribution_cycles = 0

    config_seen_before = False

    config_history = read_input(file)

    print("initial config:", config_history)

    while config_seen_before == False:

        if verbose:

            print("redistribution_cycles:", redistribution_cycles)

        x = [reallocate_memory(config_history[redistribution_cycles], verbose)]

        config_history = config_history + x

        if verbose:

            print("config_history:", config_history)

        redistribution_cycles = redistribution_cycles + 1

        for i in range(redistribution_cycles):

            if config_history[redistribution_cycles] == config_history[i]:

                config_seen_before = True

                break

    print(redistribution_cycles)

    return(redistribution_cycles)



if __name__ == '__main__':

    if len(sys.argv[1:]) > 1:

        count_memory_reallocations(sys.argv[1], sys.argv[2])

    else:

        count_memory_reallocations(sys.argv[1])
