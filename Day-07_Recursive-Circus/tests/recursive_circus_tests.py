import sys
sys.path.insert(0, '..')
import recursive_circus as rc


def recursive_circus_tests():

    assert rc.get_bottom_program('input_test1.txt') == "tknk", "test 1 failed"


if __name__ == '__main__':
    recursive_circus_tests()
