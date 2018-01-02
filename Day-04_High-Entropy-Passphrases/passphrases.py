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

def valid_passphrase_pt2(pp):

    for i in range(len(pp)):

        for j  in range(i + 1, len(pp)):

            if len(pp[i]) == len(pp[j]):

                letters_i = sorted(list(pp[i]))

                letters_j = sorted(list(pp[j]))

                if letters_i == letters_j:

                    return(False)

    return(True)
                
def valid_passphrases(file):

    passphrases = read_input(file)

    valid_passphrases_count = 0

    for pp in passphrases:

        if valid_passphrase(pp):

            valid_passphrases_count = valid_passphrases_count + 1

    print(valid_passphrases_count)

    return(valid_passphrases_count)

def valid_passphrases_pt2(file):

    passphrases = read_input(file)

    valid_passphrases_count = 0

    for pp in passphrases:

        if valid_passphrase_pt2(pp):

            valid_passphrases_count = valid_passphrases_count + 1

    print(valid_passphrases_count)

    return(valid_passphrases_count)


if __name__ == '__main__':

    valid_passphrase(sys.argv[1])
