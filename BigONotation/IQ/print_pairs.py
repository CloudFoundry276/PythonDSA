# IQ - 2
# Time Compexity is O(n^2)
def printPairs(array):
    for i in array:
        for j in array:
            print("i: {} and j: {}".format(i, j))

array = [5,4,10,8,11]
printPairs(array)
