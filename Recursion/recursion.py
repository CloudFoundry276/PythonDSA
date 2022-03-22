def factorial(n):
    assert n >= 0 and int(n) == n, "The number should be positive integer only!"
    if n in [0, 1]:
        return 1
    else:
        return n * factorial(n-1)

print("Factorial of {} is {}".format(4, factorial(4)))
