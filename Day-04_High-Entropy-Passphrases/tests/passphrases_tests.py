import sys
sys.path.insert(0, '/Users/richardangell/Projects/advent-of-code-2017/Day-04_High-Entropy-Passphrases')
import passphrases as pp


def passphrases_tests():

    assert pp.valid_passphrases('input_test1.txt') == 1, "test 1 failed"

    assert pp.valid_passphrases('input_test2.txt') == 0, "test 2 failed"

    assert pp.valid_passphrases('input_test3.txt') == 1, "test 3 failed"


if __name__ == '__main__':
    passphrases_tests()
