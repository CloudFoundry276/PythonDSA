def flatten(arr):
    if arr == []:
        return arr
    if isinstance(arr[0], list):
        return flatten(arr[0]) + flatten(arr[1:])
    return arr[:1] + flatten(arr[1:])

print("Flatten array of {} is {}".format([1,2,3,[4,5]], flatten([1,2,3,[4,5]])))
print("Flatten array of {} is {}".format([1,[2,[3,4],[[5]]]], flatten([1,[2,[3,4],[[5]]]])))
print("Flatten array of {} is {}".format([[1],[2],[3]], flatten([[1],[2],[3]])))
print("Flatten array of {} is {}".format([[[[1], [[[2]]], [[[[[[[3]]]]]]]]]], flatten([[[[1], [[[2]]], [[[[[[[3]]]]]]]]]])))
