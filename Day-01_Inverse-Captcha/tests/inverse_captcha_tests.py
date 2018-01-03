import sys
sys.path.insert(0, '..')
import inverse_captcha as ic


def inverse_captcha_tests():

    assert ic.inverse_captcha('1122') == 3, "test 1 failed"

    assert ic.inverse_captcha('1111') == 4, "test 2 failed"

    assert ic.inverse_captcha('1234') == 0, "test 3 failed"

    assert ic.inverse_captcha('91212129') == 9, "test 4 failed"


if __name__ == '__main__':
    inverse_captcha_tests()
