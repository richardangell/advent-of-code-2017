import sys
sys.path.insert(0, '..')
import registers as r

def registers_tests():

    assert r.find_largest_value('input_test1.txt', 1) == 1, "test 1 failed"



if __name__ == '__main__':
    registers_tests()
