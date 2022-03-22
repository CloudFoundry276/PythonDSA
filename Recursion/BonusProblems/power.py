def power(base, exponent):
    assert exponent >= 0 and int(exponent) == exponent, "The exponent should always be a positive integer only"
    if exponent == 0:
        return 1
    if exponent == 1:
        return base
    return base * power(base, exponent-1)

print("{} power of {} is {}".format(0, 2, power(2, 0)))
print("{} power of {} is {}".format(2, 2, power(2, 2)))
print("{} power of {} is {}".format(4, 2, power(2, 4)))
