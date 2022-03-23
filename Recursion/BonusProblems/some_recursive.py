import re


def isOdd(num):
    if num%2 == 0:
        return False
    else:
        return True

def someRecursive(arr, cb):
    cb = []
    for x in arr:
        if isOdd(x) == True:
            cb.append("Odd")
        else:
            cb.append("Even")
    
    if "Odd" in cb:
        return True
    else:
        return False

print("{} contains odd number(s): {}".format([1,2,3,4], someRecursive([1,2,3,4], isOdd)))
print("{} contains odd number(s): {}".format([4,6,8,9], someRecursive([4,6,8,9], isOdd)))
print("{} contains odd number(s): {}".format([4,6,8], someRecursive([4,6,8], isOdd)))
