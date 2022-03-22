def factorial(num):
    assert num >= 0 and int(num) == num, "The number should always be a positive integer only"
    if num in [0, 1]:
        return 1
    else:
        return num * factorial(num-1)

print("Factorial of {} is {}".format(1, factorial(1)))
print("Factorial of {} is {}".format(2, factorial(2)))
print("Factorial of {} is {}".format(4, factorial(4)))
print("Factorial of {} is {}".format(7, factorial(7)))
