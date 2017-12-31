import sys


def read_input(file):

    with open(file) as f:

        lines = f.readlines()

    for i in range(len(lines)):

        lines[i] = lines[i][:(len(lines[i]) - 1)].split("\t")

        for j in range(len(lines[i])):

            lines[i][j] = int(lines[i][j])

    return(lines)




def corruption_checksum(file):

    ss = read_input(file)

    total = 0

    for i in range(len(ss)):

        row_max = max(ss[i])

        row_min = min(ss[i])

        total = total + row_max - row_min

    print(total)

    return(total)









if __name__ == '__main__':
    corruption_checksum(sys.argv[1])
