def recursiveRange(num):
    assert num >= 0 and int(num) == num, "The number should always be a positive integer only"
    if num == 0:
        return 0
    else:
        return num + recursiveRange(num-1)

print("The recursive range of {} is {}".format(6, recursiveRange(6)))
print("The recursive range of {} is {}".format(10, recursiveRange(10)))
