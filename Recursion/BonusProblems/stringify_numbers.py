obj = {
    "num": 1,
    "test": [],
    "data": {
        "val": 4,
        "info": {
            "isRight": True,
            "random": 66
        }
    }
}

def stringifyNumbers(obj):
    for x in obj:
        if not isinstance(obj[x], dict):
            if isinstance(obj[x], int) and not isinstance(obj[x], bool):
                obj[x] = str(obj[x])
        else:
            stringifyNumbers(obj[x])
    return obj

print(stringifyNumbers(obj))
