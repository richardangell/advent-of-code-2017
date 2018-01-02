import sys

def read_input(file):

    with open(file) as f:

        lines = f.readlines()

    for i in range(len(lines)):

        # remove \n and split into list
        lines[i] = lines[i][:(len(lines[i]) - 1)].split(" ")

    return(lines)

def valid_passphrase(pp):

    pp_set = set(pp)

    if len(pp) == len(pp_set):

        return(True)

    else:

        return(False)

def valid_passphrases(file):

    passphrases = read_input(file)

    valid_passphrases_count = 0

    for pp in passphrases:

        if valid_passphrase(pp):

            valid_passphrases_count = valid_passphrases_count + 1

    print(valid_passphrases_count)

    return(valid_passphrases_count)


if __name__ == '__main__':

    valid_passphrase(sys.argv[1])
