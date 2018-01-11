import sys
sys.path.insert(0, '..')
import registers2 as r2

def registers2_tests():

    assert r2.find_largest_value('input_test1.txt', 1) == 10, "test 1 failed"



if __name__ == '__main__':
    registers2_tests()
