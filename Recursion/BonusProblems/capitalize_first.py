def capitalizeFirst(arr):
    for i in range(len(arr)):
        arr[i] = arr[i].capitalize()
    return arr

print(capitalizeFirst(['car', 'taco', 'banana']))
