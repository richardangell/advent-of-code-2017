import sys
sys.path.insert(0, '..')
import spiral_memory as sm


def spiral_memory_tests():

    assert sm.spiral_memory(1) == 0, "test 1 failed"

    assert sm.spiral_memory(12) == 3, "test 2 failed"

    assert sm.spiral_memory(23) == 2, "test 3 failed"

    assert sm.spiral_memory(1024) == 31, "test 4 failed"


if __name__ == '__main__':

    spiral_memory_tests()
