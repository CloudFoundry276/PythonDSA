def fib(num):
    assert num >= 0 and int(num) == num, "The fibonacci number should always be a positive integer only"
    if num in [0,1]:
        return num
    else:
        return fib(num-1) + fib(num-2)

print("Fibonacci number at {} index position is {}".format(4, fib(4)))
print("Fibonacci number at {} index position is {}".format(10, fib(10)))
print("Fibonacci number at {} index position is {}".format(28, fib(28)))
print("Fibonacci number at {} index position is {}".format(35, fib(35)))
