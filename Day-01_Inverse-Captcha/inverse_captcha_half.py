import sys


def inverse_captcha_half(digits):

    total = 0

    n = len(digits)

    steps = n // 2

    for i in range(n):

        if digits[i] == digits[(i + steps) % n]:

            total = total + int(digits[i])

    print(total)

    return(total)


if __name__ == '__main__':
    inverse_captcha_half(sys.argv[1])
