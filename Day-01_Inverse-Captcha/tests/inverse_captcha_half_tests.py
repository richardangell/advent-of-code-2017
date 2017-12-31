import sys
sys.path.insert(0, '/Users/richardangell/Projects/advent-of-code-2017/Day-01_Inverse-Captcha')
import inverse_captcha_half as ich


def inverse_captcha_half_tests():

    assert ich.inverse_captcha_half('1212') == 6, "test 1 failed"

    assert ich.inverse_captcha_half('1221') == 0, "test 2 failed"

    assert ich.inverse_captcha_half('123425') == 4, "test 3 failed"

    assert ich.inverse_captcha_half('123123') == 12, "test 4 failed"

    assert ich.inverse_captcha_half('12131415') == 4, "test 5 failed"
    

if __name__ == '__main__':
    inverse_captcha_half_tests()
