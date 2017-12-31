import sys


def read_input(file):

    with open(file) as f:

        lines = f.readlines()

    for i in range(len(lines)):

        lines[i] = lines[i][:(len(lines[i]) - 1)].split("\t")

        for j in range(len(lines[i])):

            lines[i][j] = int(lines[i][j])

    return(lines)




def corruption_checksum_pt2(file):

    ss = read_input(file)

    total = 0

    for i in range(len(ss)):

        x = len(ss[i])

        for j in range(x):

            for k in [k for k in range(x) if k != j]:

                if ss[i][j] % ss[i][k] == 0:

                    total = total + (ss[i][j] / ss[i][k])

    print(total)

    return(total)





if __name__ == '__main__':
    corruption_checksum_pt2(sys.argv[1])
