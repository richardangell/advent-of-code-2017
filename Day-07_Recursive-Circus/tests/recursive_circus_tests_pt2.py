import sys
sys.path.insert(0, '..')
import recursive_circus_pt2 as rc2

def recursive_circus_tests_pt2():

    assert rc2.find_correct_weight('input_test1.txt', 1) == 60, "test 1 failed"
    
   

if __name__ == '__main__':
    recursive_circus_tests_pt2()
