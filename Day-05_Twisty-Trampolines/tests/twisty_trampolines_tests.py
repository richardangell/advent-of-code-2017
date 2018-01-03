import sys
sys.path.insert(0, '..')
import twisty_trampolines as tt


def twisty_trampolines_tests():

    assert tt.escape_steps('input_test1.txt', 1) == 5, "test 1 failed"


if __name__ == '__main__':
    twisty_trampolines_tests()
