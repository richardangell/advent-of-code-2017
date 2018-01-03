import sys
sys.path.insert(0, '..')
import twisty_trampolines_pt2 as tt2


def twisty_trampolines_pt2_tests():

    assert tt2.escape_steps('input_test1.txt', 1) == 10, "test 1 failed"


if __name__ == '__main__':
    twisty_trampolines_pt2_tests()
