import corruption_checksum as cc
import corruption_checksum_pt2 as cc2

if __name__ == '__main__':

    file = "input.txt"

    cc.corruption_checksum(file)

    cc2.corruption_checksum_pt2(file)
