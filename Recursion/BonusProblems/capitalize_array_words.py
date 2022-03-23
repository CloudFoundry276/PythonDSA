def capitalizeWords(arr):
    for i in range(len(arr)):
        arr[i] = arr[i].upper()
    return arr

words = ["i", "am", "learning", "recursion"]
print("Capitalization of {} is {}".format(words, capitalizeWords(words)))
