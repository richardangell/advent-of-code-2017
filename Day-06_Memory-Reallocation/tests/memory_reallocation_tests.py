import sys
sys.path.insert(0, '..')
import memory_reallocation as mr


def memory_reallocation_tests():

    assert mr.count_memory_reallocations('input_test1.txt', 1) == 5, "test 1 failed"


if __name__ == '__main__':
    memory_reallocation_tests()
