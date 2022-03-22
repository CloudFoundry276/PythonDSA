def gcd(a, b):
    assert int(a) == a and int(b) == b, "The numbers should always be integers"
    if a < 0:
        a = -1 * a
    if b < 0:
        b = -1 * b
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

a = 48
b = 18
print("Greatest Common Divisor (GCD) of {} and {} is {}".format(a, b, gcd(a, b)))