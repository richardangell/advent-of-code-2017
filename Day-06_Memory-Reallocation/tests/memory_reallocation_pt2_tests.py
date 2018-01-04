import sys
sys.path.insert(0, '..')
import memory_reallocation_pt2 as mr2


def memory_reallocation_tests():

    assert mr2.count_memory_cycles('input_test1.txt', 1) == 4, "test 1 failed"


if __name__ == '__main__':
    memory_reallocation_tests()
