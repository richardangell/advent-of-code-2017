import sys
sys.path.insert(0, '/Users/richardangell/Projects/advent-of-code-2017/Day-04_High-Entropy-Passphrases')
import passphrases as pp


def passphrases_pt2_tests():

    assert pp.valid_passphrases_pt2('input_test4.txt') == 1, "test 4 failed"

    assert pp.valid_passphrases_pt2('input_test5.txt') == 0, "test 5 failed"

    assert pp.valid_passphrases_pt2('input_test6.txt') == 1, "test 6 failed"

    assert pp.valid_passphrases_pt2('input_test7.txt') == 1, "test 7 failed"

    assert pp.valid_passphrases_pt2('input_test8.txt') == 0, "test 8 failed"


if __name__ == '__main__':
    passphrases_pt2_tests()
