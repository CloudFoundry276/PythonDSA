def findBiggestNumber(sampleArray):
    biggestNumber = sampleArray[0]
    for index in range(1, len(sampleArray)):
        if sampleArray[index] > biggestNumber:
            biggestNumber = sampleArray[index]
    return biggestNumber

print("Biggest Number from Sample Array {} is {}".format([5,4,10,8,11,68,87], findBiggestNumber([5,4,10,8,11,68,87])))
