from math import sqrt


def find_divisor(numba):
    divisor = 2
    number_of_n = 0

    while divisor <= sqrt(numba):
        if numba % divisor == 0:
            print(number_of_n)
            return divisor
        divisor += 1

        number_of_n += 1
    print(number_of_n)

    return "Numba ist prvočíslo"


nummer = 1933*1933
print(find_divisor(nummer))
