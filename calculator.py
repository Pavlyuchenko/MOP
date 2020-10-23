def count_numbers(a, b):
    first = [int(x) for x in reversed(str(a))]
    second = [int(x) for x in reversed(str(b))]

    if len(first) < len(second):
        for _ in range(len(second) - len(first)):
            first.append(0)
    
    if len(first) > len(second):
        for _ in range(len(first) - len(second)):
            second.append(0)

    prenos = 0
    vysledek = []

    for i, j in zip(first, second):
        vysledek.append((i + j + prenos) % 10)
        prenos = 0
        if i + j + prenos >= 10:
            prenos = 1

    if prenos == 1:
        vysledek.append(1)

    [print(x, end="") for x in reversed(vysledek)]


a = 187481619815849471971478198191498449*9848949848981516515150984810
b = 200054515*54981515490905090*981808098051980504505401406098106
count_numbers(a, b)
print()
print(a + b)


def soucet(n):
    res = 0
    for i in range(n):
        res += 1/n
    return res


print(soucet(18198114))
