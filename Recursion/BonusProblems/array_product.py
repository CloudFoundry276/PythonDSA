def productOfArray(arr):
    product = 1
    for i in arr:
        product *= i
    return product

print("Product of array {} is {}".format([1,2,3], productOfArray([1,2,3])))
print("Product of array {} is {}".format([1,2,3,10], productOfArray([1,2,3,10])))
