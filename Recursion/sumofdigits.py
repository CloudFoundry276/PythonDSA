def sumOfDigits(n):
    assert n >= 0 and int(n) == n, "The number should be always a positive integer"
    if n == 0:
        return 0
    else:
        return int(n%10) + sumOfDigits(int(n//10))

print("Sum of digits of {} is {}".format(45, sumOfDigits(45)))
