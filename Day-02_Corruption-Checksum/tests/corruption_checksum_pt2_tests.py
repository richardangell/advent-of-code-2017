import sys
sys.path.insert(0, '..')
import corruption_checksum_pt2 as cc2


def corruption_checksum_pt2_tests():

    assert cc2.corruption_checksum_pt2('input_test2.txt') == 9, "test 1 failed"


if __name__ == '__main__':
    corruption_checksum_pt2_tests()
