import sys
sys.path.insert(0, '..')
import corruption_checksum as cc


def corruption_checksum_tests():

    assert cc.corruption_checksum('input_test1.txt') == 18, "test 1 failed"


if __name__ == '__main__':
    corruption_checksum_tests()
