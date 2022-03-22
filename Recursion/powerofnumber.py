def powerOfNumber(base, exponent):
    assert exponent >= 0 and int(exponent) == exponent, "The exponent should always be positive integer only"
    if exponent == 0:
        return 1
    if exponent == 1:
        return base
    return base * powerOfNumber(base, exponent-1)

base = 2.5
exponent = 5
print("{} power of {} is {}".format(exponent, base, powerOfNumber(base, exponent)))
