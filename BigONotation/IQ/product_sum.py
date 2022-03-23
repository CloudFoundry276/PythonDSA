# IQ - 1
# Time Complexity is O(N)
def foo(array):
    sum = 0
    product = 1

    for i in array:
        sum += i
    
    for i in array:
        product *= i
    
    print("Sum of elements of array {} is {}".format(array, sum))
    print("Product of elements of array {} is {}".format(array, product))

array = [5,4,10,8,11]
foo(array)
