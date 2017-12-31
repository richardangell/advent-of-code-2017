

import sys


def inverse_captcha(digits):

    total = 0

    for i in range(0, len(digits) - 1):

        if digits[i] == digits[i+1]:

            total = total + int(digits[i])

    if digits[0] == digits[len(digits) - 1]:

        total = total + int(digits[0])

    print(total)

    return(total)


if __name__ == '__main__':
    inverse_captcha(sys.argv[1])
