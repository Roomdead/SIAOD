a, b, f, k = [int(x) for x in input("Input a b f k\n").split()]


def calculate(a, b, f, k):
    i = 0
    tank = b
    refuels = 0
    if b < 2 * f or b < 2 * (a - f):
        refuels = -1
    else:
        while i < k:
            if i % 2:
                tank -= (a - f)
                if (tank < 2 * f) and not (k - i == 1 and tank >= f):
                    tank = b
                    refuels += 1
                tank -= f
            else:
                tank -= f
                if (tank < 2 * (a - f)) and not (k - i == 1 and tank >= a - f):
                    tank = b
                    refuels += 1
                tank -= (a - f)
            i += 1
            print(i, tank)
    return refuels


print(calculate(a, b, f, k))
